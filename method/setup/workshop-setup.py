#!/usr/bin/env python3
"""workshop-setup.py — create a workshop, and stop there.

Reference implementation of `setup/CONTRACT.md`. What it copies lives in `templates/`.

    py -3 <method>/setup/workshop-setup.py <Name> [--repos a b] [--from <framing>] [--dry-run]

Run it from the framing folder of the workshop you are currently in, or point `--from` at one.
That folder is not decoration: it is what tells the installer the corpus root, the naming
convention of a framing folder, and which instance files this corpus reads unconditionally —
all of which are conventions to be *read*, never guessed.

⚠ The installer refuses to touch anything that already exists. Creating a wiring is a right,
changing one is not, and the existence of the target is exactly what tells it which of the two
it is being asked to do. See CONTRACT.md § *The one rule that bounds the whole thing*.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter
from datetime import date
from pathlib import Path

# The runtime check belongs in the script as much as in `bootstrap.md`: a rule read once, the day
# a workshop was set up, does not catch a machine that changed afterwards.
if sys.version_info < (3, 11):
    sys.exit(
        "This installer needs Python 3.11 or later (found %d.%d).\n"
        "The floor is set by TOML parsing entering the standard library at 3.11 — the method\n"
        "requires a configuration format whose values can carry the reason that holds them.\n"
        "On Windows invoke `py -3`; `python3` there resolves to a store stub that reports an\n"
        "absence on a machine where Python is installed and working."
        % sys.version_info[:2]
    )

import tomllib  # noqa: E402  — after the version guard, which exists to make this import safe

# Same reason as the lint: the report is dense in symbols the corpus itself uses, and a console
# that cannot print them would fail on the message rather than on the work.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        try:
            _stream.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass


DOTFILES = {"gitignore": ".gitignore", "gitattributes": ".gitattributes", "editorconfig": ".editorconfig"}


# ============================================================================================
# Report
# ============================================================================================


class Report:
    """One line per artefact. A refusal is a normal outcome — every refusal in the contract
    exists because the alternative is a silently wrong workshop."""

    def __init__(self, dry_run: bool) -> None:
        self.dry_run = dry_run

    def did(self, message: str) -> None:
        print("[%s] %s" % ("would" if self.dry_run else " ok  ", message))

    def note(self, message: str) -> None:
        print("[note ] %s" % message)

    def warn(self, message: str) -> None:
        print("[warn ] %s" % message)

    def refuse(self, message: str) -> None:
        sys.exit("[stop ] %s" % message)


# ============================================================================================
# Resolving the corpus — computed, never assumed
# ============================================================================================


class Corpus:
    """The layout is resolved exactly as the lint resolves it, and for the same reason: naming
    any of these folders in the code would break at the first rename, and for everyone who
    adopts the method under other names."""

    def __init__(self, framing: Path, report: Report) -> None:
        if not framing.is_dir():
            report.refuse("%s is not a folder — point --from at the framing folder of the workshop you are in" % framing)
        self.framing_name = framing.name
        self.here = framing.parent
        self.root = self.here.parent

        self.meta = self._find_meta()
        if not self.meta:
            report.refuse(
                "no meta level found under %s — expected one folder holding both a %s/ and an instance/.\n"
                "        Refusing to write rather than emit a plausible relative path: a workshop wired to the\n"
                "        wrong corpus does not fail visibly, it starts every session from the wrong rules."
                % (self.root, self.framing_name)
            )
        self.instance = self.meta / "instance"
        self.method = self._find_method()
        if not self.method:
            report.refuse("no folder under %s declares method/organization.md — cannot wire a workshop to a method it cannot find" % self.meta)

    def _find_meta(self):
        """The meta level is the workshop that also hosts the instance, which is transverse and
        belongs to no single workshop."""
        for child in sorted(self.root.iterdir()):
            if child.is_dir() and (child / self.framing_name).is_dir() and (child / "instance").is_dir():
                return child
        return None

    def _find_method(self):
        """The method repository is the one declaring the entry point. The entry point is named
        by the method; the repository holding it is not."""
        for child in sorted(self.meta.iterdir()):
            if child.is_dir() and (child / "method" / "organization.md").is_file():
                return child / "method"
        return None

    def relative(self, path: Path) -> str:
        """Every path in an editor wiring is relative to the corpus root, forward slashes."""
        return path.resolve().relative_to(self.root.resolve()).as_posix()


def instance_files(corpus: Corpus, report: Report) -> list:
    """Which instance files are read unconditionally is the instance's business, and the workshop
    repeats it so the lint does not guess. Read it from the workshop we are standing in rather
    than inventing a default: that is the convention already in force in this corpus."""
    config = corpus.here / corpus.framing_name / "lint.toml"
    if config.is_file():
        try:
            declared = tomllib.loads(config.read_text(encoding="utf-8")).get("bootstrap", {}).get("instance_files")
        except tomllib.TOMLDecodeError:
            declared = None
        if declared:
            return list(declared)
    report.warn("no instance_files declared in the current workshop — falling back to index.md alone")
    return ["index.md"]


# ============================================================================================
# The editor wiring — learned from the corpus, never invented
# ============================================================================================


def read_workspaces(corpus: Corpus) -> list:
    """Sibling wiring files, parsed. Unparseable ones are skipped rather than guessed at: a file
    carrying comments is valid for the editor and not for a JSON reader, and half-reading one
    would produce a convention nobody wrote."""
    found = []
    for path in sorted(corpus.root.glob("*.code-workspace")):
        try:
            found.append(json.loads(path.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError):
            continue
    return found


def consensus(values: list):
    """Most frequent, ties broken by sort order. Determinism matters more than cleverness here —
    the same corpus must always produce the same wiring."""
    if not values:
        return None
    counted = Counter(values)
    top = max(counted.values())
    return sorted(k for k, v in counted.items() if v == top)[0]


class Conventions:
    """What the corpus already shows about how a wiring is written. Reading the corpus is
    deterministic and inspectable; detecting an installed editor is a guess about a machine."""

    def __init__(self, corpus: Corpus, report: Report) -> None:
        self.ok = False
        workspaces = read_workspaces(corpus)
        if not workspaces:
            report.warn("no editor wiring found at %s — writing a minimal one, with plain labels" % corpus.root)
            self.method_label = "Method"
            self.instance_label = "Instance"
            self.framing_pattern = "{} - Workspace"
            self.icon = ""
            self.instruction_keys = {}
            self.plain_settings = {}
            return

        self.ok = True
        method_labels, instance_labels, framing_patterns, icons = [], [], [], []
        for data in workspaces:
            for folder in data.get("folders", []):
                label, path = folder.get("name", ""), folder.get("path", "")
                target = (corpus.root / path.replace("/", os.sep)).resolve()
                match = re.match(r"^([^\w\s]+)\s+", label)
                if match:
                    icons.append(match.group(1))
                if target == corpus.method.resolve() or target == corpus.method.parent.resolve():
                    method_labels.append(label)
                elif target == corpus.instance.resolve():
                    instance_labels.append(label)
                elif target.name == corpus.framing_name and target.parent.parent == corpus.root.resolve():
                    # « 🗂️ CraftNorma - Workspace » against workshop CraftNorma gives the pattern;
                    # a label that never names its workshop is a constant, and stays one.
                    framing_patterns.append(label.replace(target.parent.name, "{}"))

        self.icon = consensus(icons) or ""
        self.method_label = consensus(method_labels) or "Method"
        self.instance_label = consensus(instance_labels) or "Instance"
        self.framing_pattern = consensus(framing_patterns) or "{} - Workspace"
        self.plain_settings = self._plain_settings(workspaces)

    def _plain_settings(self, workspaces: list) -> dict:
        """Scalar settings held, with the same value, by a majority of siblings. One that appears
        in a single wiring is that workshop's business — `powershell.cwd`, naming one of its own
        folders, is the case that made this rule explicit."""
        seen = Counter()
        for data in workspaces:
            for key, value in data.get("settings", {}).items():
                if isinstance(value, (str, int, float, bool)):
                    seen[(key, value)] += 1
        return {key: value for (key, value), count in seen.items() if count * 2 > len(workspaces)}

    def label(self, text: str) -> str:
        """Only for labels this installer *builds*. The ones read from the corpus already carry
        their icon, and prepending a second one is how a convention gets copied wrong."""
        return ("%s %s" % (self.icon, text)).strip()

    def describe(self) -> list:
        """⚠ What is learned must be reported. Learning from the corpus reproduces its accidents
        as faithfully as its conventions, and nothing in the reading tells the two apart — so the
        developer is the one who has to see what was copied, at the moment it is copied.
        Observed: instruction-file lists, added to every wiring by an agent nobody had asked, were
        reproduced into a new workshop without a line saying so."""
        if not self.ok:
            return ["no sibling wiring to read from — plain labels, no settings"]
        told = ['labels « %s » and « %s »' % (self.method_label, self.instance_label),
                'framing label pattern « %s »' % self.framing_pattern]
        for key, value in sorted(self.plain_settings.items()):
            told.append("setting %s = %s" % (key, json.dumps(value)))
        return told


def build_wiring(corpus: Corpus, conventions: Conventions, name: str, framing: Path, repos: list) -> dict:
    folders = [
        {"name": conventions.method_label, "path": corpus.relative(corpus.method)},
        {"name": conventions.instance_label, "path": corpus.relative(corpus.instance)},
    ]
    for repo in repos:
        folders.append({"name": conventions.label(repo.name), "path": corpus.relative(repo)})
    folders.append({"name": conventions.framing_pattern.format(name), "path": corpus.relative(framing)})

    # ⚠ Folders, and nothing that names a file to read. What reaches an agent is the folder list;
    # a per-tool list of instruction files is a **second starting point**, and one that can win.
    # `bootstrap.md` allows a workshop to keep one deliberately — which is precisely why an
    # installer must not create one on the developer's behalf.
    return {"folders": folders, "settings": dict(conventions.plain_settings)}


# ============================================================================================
# Writing
# ============================================================================================


def substitute(text: str, values: dict) -> str:
    for key, value in values.items():
        text = text.replace("{{%s}}" % key, value)
    return text


def toml_array(values: list) -> str:
    return "[%s]" % ", ".join('"%s"' % v for v in values)


def copy_template(source: Path, target: Path, values: dict, report: Report) -> None:
    """Dotfiles are stored without their dot so that a template cannot act on the repository that
    ships it; the dot is restored here."""
    for path in sorted(source.rglob("*")):
        relative = path.relative_to(source)
        parts = list(relative.parts)
        parts[-1] = DOTFILES.get(parts[-1], parts[-1])
        destination = target.joinpath(*parts)
        if path.is_dir():
            if not report.dry_run:
                destination.mkdir(parents=True, exist_ok=True)
            continue
        if path.name == ".gitkeep":
            if not report.dry_run:
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(b"")
            continue
        if not report.dry_run:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(substitute(path.read_text(encoding="utf-8"), values), encoding="utf-8", newline="\n")


def git(repo: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(repo)] + list(args), capture_output=True, text=True)


def init_repository(repo: Path, message: str, report: Report) -> None:
    """One commit, and no remote. Where a repository is pushed is an owner's decision, and
    guessing a host is not a service."""
    if report.dry_run:
        report.did("git init + first commit in %s" % repo)
        return
    result = git(repo, "init", "-b", "main")
    if result.returncode != 0:
        git(repo, "init")
    git(repo, "add", "-A")
    committed = git(repo, "commit", "-m", message)
    if committed.returncode != 0:
        report.warn("%s: initialised but not committed — %s" % (repo.name, committed.stderr.strip().splitlines()[-1:] or "git declined"))
        return
    report.did("%s: repository initialised, one commit, no remote" % repo.name)


# ============================================================================================
# Main
# ============================================================================================


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a workshop, and stop there.")
    parser.add_argument("name", help="the workshop's name — it names the folder and the wiring file alike")
    parser.add_argument("--repos", nargs="*", default=[], help="code repositories to create inside it, each initialised")
    parser.add_argument("--from", dest="origin", default=".", help="framing folder of the workshop you are in (default: .)")
    parser.add_argument("--dry-run", action="store_true", help="report what would be written, write nothing")
    args = parser.parse_args()

    report = Report(args.dry_run)
    setup_dir = Path(__file__).resolve().parent
    corpus = Corpus(Path(args.origin).resolve(), report)

    if corpus.method.resolve() != setup_dir.parent.resolve():
        report.refuse(
            "this script lives under %s but the corpus resolves its method to %s.\n"
            "        Two methods in one corpus is a second source of truth; refusing rather than picking one."
            % (setup_dir.parent, corpus.method)
        )

    name = args.name.strip()
    if not name or re.search(r"[\\/:*?\"<>|]", name):
        report.refuse("« %s » is not usable as a folder name" % args.name)

    workshop = corpus.root / name
    wiring_file = corpus.root / ("%s.code-workspace" % name)
    for existing in (workshop, wiring_file):
        if existing.exists():
            report.refuse(
                "%s already exists.\n"
                "        Creating a wiring is a right; changing one is not, and it belongs to a session of that\n"
                "        workshop. See method/setup/CONTRACT.md." % existing
            )

    framing = workshop / corpus.framing_name
    repos = [workshop / repo for repo in args.repos]
    version = (corpus.method / "VERSION").read_text(encoding="utf-8").strip() if (corpus.method / "VERSION").is_file() else "unknown"

    values = {
        "WORKSHOP": name,
        "DATE": date.today().isoformat(),
        "METHOD_VERSION": version,
        "REPOSITORIES": toml_array([corpus.framing_name] + [r.name for r in repos]),
        "INSTANCE_FILES": toml_array(instance_files(corpus, report)),
    }

    print("workshop  %s" % workshop)
    print("method    %s" % corpus.method)
    print("instance  %s" % corpus.instance)
    print()

    templates = corpus.method / "templates"
    copy_template(templates / "workshop" / "_workspace", framing, values, report)
    copy_template(templates / "repo", framing, values, report)
    report.did("framing folder %s/ — atlas, todo, handoff, done/, _planning/, lint.toml" % corpus.relative(framing))
    init_repository(framing, "setup: %s — framing skeleton, created from the method installer" % name, report)

    for repo in repos:
        if not args.dry_run:
            repo.mkdir(parents=True, exist_ok=True)
        # `repo/` is what every repository gets, the framing included; `code-repo/` is what only
        # code gets. ⚠ Neither carries a src/tests/docs skeleton: `organization.md` says the method
        # says nothing about a repository's internals, and the two example repositories in the
        # readme are laid out differently on purpose.
        copy_template(templates / "repo", repo, values, report)
        copy_template(templates / "code-repo", repo, dict(values, REPOSITORY=repo.name), report)
        report.did("repository %s/" % repo.name)
        init_repository(repo, "setup: %s — repository skeleton" % repo.name, report)

    conventions = Conventions(corpus, report)
    wiring = build_wiring(corpus, conventions, name, framing, repos)
    rendered = json.dumps(wiring, indent=2, ensure_ascii=False) + "\n"
    if not args.dry_run:
        wiring_file.write_text(rendered, encoding="utf-8", newline="\n")
    report.did("editor wiring %s — %d folder(s)" % (wiring_file.name, len(wiring["folders"])))
    for line in conventions.describe():
        report.note("read from the corpus: %s" % line)
    if args.dry_run:
        # The wiring is the one artefact worth reading before it is written: it is what an agent
        # will and will not reach, and a wrong path there breaks nothing visible.
        print()
        print(rendered, end="")

    print()
    print("Open « %s » to work in this workshop." % wiring_file.name)
    if conventions.ok:
        # Tool-specific, and deliberately printed rather than written into the method: a wiring
        # opened for the first time is untrusted, and an editor that answers by disabling its
        # extensions looks exactly like an editor that lost them.
        print("It has never been opened, so the editor may hold it in restricted mode until you")
        print("trust it — extensions stay disabled meanwhile, and none of them were uninstalled.")
    print("Nothing was written outside it. Whether this session's handoff mentions the creation is")
    print("yours to decide, in your own words — the installer does not write in a parent workshop.")
    if repos:
        print()
        print("Folder labels for the repositories are the folder names; rename them in the wiring if")
        print("this corpus words them differently.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
