#!/usr/bin/env python3
"""workshop-lint.py — the framing checks of the method, in one file.

    py -3 workshop-lint.py <framing folder>       # Windows
    python3 workshop-lint.py <framing folder>     # elsewhere

WHAT is checked, and why, lives in CONTRACT.md — that file is the portable part.
This one is the reference implementation of it. A workshop that cannot run Python
reimplements from the contract, never from this code: the method exists partly
because this lint was once found in two divergent forks, and shipping a second
implementation would reproduce that fault by design.

Standard library only: no third-party package, no virtual environment, no
dependency file. That constraint is what keeps "install Python" a non-event on
the machine of whoever adopts the method — not on the author's, where the package
is already there. It is also what sets the floor at 3.11, where TOML parsing
entered the standard library.

Exit codes: 0 clean or warnings only, 1 at least one FAIL, 2 cannot run.
"""

from __future__ import annotations

import sys

# --- Runtime guard -------------------------------------------------------------------------
# Before any 3.11-only import, and in syntax old interpreters can still parse — a guard that
# fails with ImportError has not guarded anything. bootstrap.md carries the same rule for the
# agent; this is its half that runs, and therefore its half that catches a machine which
# changed after the workshop was set up.
if sys.version_info < (3, 11):
    _v = ".".join(str(n) for n in sys.version_info[:3])
    sys.stderr.write(
        "workshop-lint needs Python 3.11 or later; this interpreter is %s.\n"
        "\n"
        "  Windows        winget install --id Python.Python.3.13 -e\n"
        "  macOS          brew install python@3.13\n"
        "  Debian/Ubuntu  sudo apt install python3\n"
        "\n"
        "Then invoke it as `py -3` on Windows, `python3` elsewhere.\n"
        "\N{WARNING SIGN} On Windows, `python3` resolves to the Microsoft Store stub and fails\n"
        "with a message that reads as an absence, on a machine where Python is installed\n"
        "and working. Check with `py --list` before installing anything.\n" % _v
    )
    raise SystemExit(2)

import argparse
import os
import re
import subprocess
import tomllib
from datetime import date, datetime
from pathlib import Path

# The report is dense in symbols the framing itself uses. A console that cannot print them
# would fail on the message rather than on the finding.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        try:
            _stream.reconfigure(encoding="utf-8")
        except (AttributeError, OSError):
            pass


# ============================================================================================
# Reporting
# ============================================================================================

COLORS = {"OK": "\033[32m", "WARN": "\033[33m", "FAIL": "\033[31m"}
RESET = "\033[0m"


class Report:
    """Collects results. FAIL is mechanical; WARN is a measurement handed to the owner."""

    def __init__(self, color: bool) -> None:
        self.color = color
        self.failed = False
        self.counts = {"OK": 0, "WARN": 0, "FAIL": 0}

    def __call__(self, level: str, message: str) -> None:
        self.counts[level] += 1
        if level == "FAIL":
            self.failed = True
        tag = "[%-4s]" % level
        if self.color:
            tag = COLORS[level] + tag + RESET
        print("%s %s" % (tag, message))

    def detail(self, message: str) -> None:
        print("        " + message)


# ============================================================================================
# Layout — resolved by disposition, never by name
# ============================================================================================
#
# organization.md states the tests, and they are mechanical:
#   a workshop is any folder containing a framing folder — that is the only test;
#   the framing folder sits outside every code repository;
#   the meta level is the workshop that also hosts the instance, which is transverse.
#
# Resolving any of this by a hard-coded folder name would break at the first rename and for
# everyone who adopts the method under other names — which is the failure the whole "cite by
# identity, not by location" rule exists against.


class Layout:
    def __init__(self, framing: Path) -> None:
        self.framing = framing
        self.workshop = framing.parent
        self.root = self.workshop.parent
        self.meta = self._find_meta()
        self.instance = (self.meta / "instance") if self.meta else None
        self.method = self._find_method()

    def _find_meta(self):
        """The meta level is the workshop that hosts the instance — a folder holding both a
        framing folder and an `instance/`. Nothing here depends on what it is called."""
        candidates = []
        for child in sorted(self.root.iterdir()):
            if not child.is_dir():
                continue
            if (child / self.framing.name).is_dir() and (child / "instance").is_dir():
                candidates.append(child)
        if len(candidates) == 1:
            return candidates[0]
        return candidates[0] if candidates else None

    def _find_method(self):
        """The method repository is the one declaring the entry point. Same reasoning: the
        entry point is named by the method, the repository holding it is not."""
        if not self.meta:
            return None
        for child in sorted(self.meta.iterdir()):
            entry = child / "method" / "organization.md"
            if entry.is_file():
                return child / "method"
        return None

    def describe(self) -> str:
        def rel(p):
            return p.name if p else "not found"

        return "framing %s · workshop %s · meta %s · method %s" % (
            rel(self.framing),
            rel(self.workshop),
            rel(self.meta),
            "found" if self.method else "not found",
        )


# ============================================================================================
# Configuration
# ============================================================================================


def load_config(framing: Path, report: Report) -> dict:
    path = framing / "lint.toml"
    if not path.is_file():
        report("FAIL", "lint.toml: absent from the framing folder — nothing declares what to check")
        raise SystemExit(1)
    with path.open("rb") as handle:
        return tomllib.load(handle)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def read_lines(path: Path) -> list:
    return read_text(path).splitlines()


# ============================================================================================
# Socle checks
# ============================================================================================


def check_handoff(cfg, layout, report) -> None:
    section = cfg.get("framing", {})
    maximum = section.get("handoff_sessions")
    relative = section.get("handoff", "memories/handoff.md")
    if maximum is None:
        return
    path = layout.framing / relative
    if not path.is_file():
        report("FAIL", "%s: missing — the volatile tense has no file" % relative)
        return
    sessions = len(re.findall(r"^## Session ", read_text(path), re.M))
    if sessions <= maximum:
        report("OK", "%s: %d session(s), max %d" % (relative, sessions, maximum))
    else:
        report("FAIL", "%s: %d sessions — prune to the archive (max %d)" % (relative, sessions, maximum))


def check_todo_closed(cfg, layout, report) -> None:
    """A closed piece of work leaves the todo. One left in place is one nobody moved."""
    for name in todo_names(cfg):
        path = layout.framing / name
        stale = [
            (n + 1, line)
            for n, line in enumerate(read_lines(path))
            if re.match(r"^#{2,3} .*(✅|TERMIN)", line)
        ]
        if not stale:
            report("OK", "%s: no closed heading left in place" % name)
        else:
            report("FAIL", "%s: %d closed piece(s) of work to file away" % (name, len(stale)))
            for number, line in stale:
                report.detail("l.%d %s" % (number, line.strip()))


def check_sizes(cfg, layout, report) -> None:
    """Characters, not lines — see CONTRACT.md § Sizes for the measurement that settled it."""
    for name, maximum in cfg.get("sizes", {}).items():
        path = layout.framing / name
        if not path.is_file():
            report("WARN", "%s: declared a size threshold but the file is absent" % name)
            continue
        size = len(read_text(path))
        if size <= maximum:
            report("OK", "%s: %d characters (threshold %d)" % (name, size, maximum))
        else:
            report(
                "WARN",
                "%s: %d characters > threshold %d — prune, and file the delivered work away"
                % (name, size, maximum),
            )


def check_bootstrap_load(cfg, layout, report) -> None:
    """The sum re-read at every start. The per-file thresholds guard its distribution; this
    guards the budget itself."""
    section = cfg.get("bootstrap", {})
    budget = section.get("budget")
    if budget is None:
        return
    ratio = section.get("chars_per_token", 3.5)

    chain = []
    if layout.method:
        chain.append(layout.method / "organization.md")
    if layout.instance:
        # The method declares the slot; the instance fills it. Which files the instance reads
        # unconditionally is the instance's business, so the workshop declares them here.
        for name in section.get("instance_files", ["index.md"]):
            chain.append(layout.instance / name)
    for name in section.get("framing_files", list(cfg.get("sizes", {}).keys())):
        chain.append(layout.framing / name)

    found = [p for p in chain if p.is_file()]
    missing = [p for p in chain if not p.is_file()]
    total = sum(len(read_text(p)) for p in found)
    tokens = round(total / ratio)

    if missing:
        report(
            "WARN",
            "bootstrap load: %d characters over %d/%d files — %d unreachable, partial total"
            % (total, len(found), len(chain), len(missing)),
        )
        for path in missing:
            report.detail("unreachable: %s" % path)
    elif total <= budget:
        report("OK", "bootstrap load: %d characters (~%d tokens, budget %d)" % (total, tokens, budget))
    else:
        report(
            "WARN",
            "bootstrap load: %d characters (~%d tokens) > budget %d — this total is re-read at every session"
            % (total, tokens, budget),
        )


def check_planning(cfg, layout, report) -> None:
    name = cfg.get("framing", {}).get("planning", "_planning")
    folder = layout.framing / name
    if not folder.is_dir():
        # ⚠ Silence cannot be told apart from a check that did not run. The folder name is
        # configurable and this implementation is shared by every workshop, so a default that
        # changes lands everywhere at the instant it is committed — and a workshop whose
        # configuration lags behind would lose this check without a line saying so.
        stripped = name.lstrip("_")
        neighbour = next(
            (p.name for p in sorted(layout.framing.iterdir()) if p.is_dir() and p.name != name and p.name.lstrip("_") == stripped),
            None,
        )
        if neighbour:
            report("WARN", "%s/: absent, but %s/ sits beside it — declare framing.planning or rename the folder" % (name, neighbour))
        else:
            report("OK", "%s/: absent — no long-form document in this workshop" % name)
        return
    documents = sorted(folder.glob("*.md"))
    if not documents:
        report("OK", "%s/: present, no long-form document yet" % folder.name)
        return

    todo_text = "\n".join(read_text(layout.framing / n) for n in todo_names(cfg))
    for path in documents:
        head = read_lines(path)[:8]
        status = next((l for l in head if re.match(r"^> [Ss]tatut ?:|^> [Ss]tatus ?:", l)), None)
        if not status:
            report("FAIL", "%s/%s: no status header — the folder holds documents at four stages and says so nowhere" % (folder.name, path.name))
            continue
        match = re.search(r"\[([A-Z0-9-]+)\]", status)
        if not match:
            report("OK", "%s/%s: status present" % (folder.name, path.name))
        elif re.search(r"\[%s\]" % re.escape(match.group(1)), todo_text):
            report("OK", "%s/%s: status present, [%s] indexed in the todo" % (folder.name, path.name, match.group(1)))
        else:
            report("WARN", "%s/%s: [%s] not found in the todo — scoping executed, document outlived?" % (folder.name, path.name, match.group(1)))


def check_root_files(cfg, layout, report) -> None:
    known = set(cfg.get("framing", {}).get("root_files", []))
    known.add("lint.toml")
    strays = [p for p in sorted(layout.framing.glob("*.md")) if p.name not in known]
    if not strays:
        report("OK", "framing root: no parallel document")
    for path in strays:
        report("FAIL", "framing root: %s outside the convention — file it away or absorb it" % path.name)


def todo_names(cfg) -> list:
    return cfg.get("todo", {}).get("files", ["todo.md"])


def check_todo_grammar(cfg, layout, report) -> dict:
    """`## [TAG] Title` plus a status line from a closed vocabulary. Returns the tags found,
    because the roadmap check needs their status."""
    section = cfg.get("todo", {})
    statuses = section.get("statuses", [])
    whitelist = section.get("heading_whitelist", [])
    required = section.get("required_fields", {})
    tags = {}
    errors = 0

    for name in todo_names(cfg):
        lines = read_lines(layout.framing / name)
        for index, line in enumerate(lines):
            if not line.startswith("## "):
                continue
            if any(re.match(pattern, line) for pattern in whitelist):
                continue
            match = re.match(r"^## \[([A-Z0-9-]+)\] \S", line)
            if not match:
                report("FAIL", "%s l.%d: heading outside the « ## [TAG] Title » template — %s" % (name, index + 1, line.strip()))
                errors += 1
                continue
            tag = match.group(1)
            if tag in tags:
                report("FAIL", "%s l.%d: [%s] duplicated (first at l.%d)" % (name, index + 1, tag, tags[tag]["line"]))
                errors += 1
            window = lines[index + 1 : index + 3]
            status_line = next((l for l in window if re.match(r"^> statut ?:|^> status ?:", l)), None)
            if not status_line:
                report("FAIL", "%s: [%s] has no status line" % (name, tag))
                errors += 1
                continue
            status = re.sub(r"^> statu[st] ?: ", "", status_line)
            status = re.sub(r" —.*$", "", status).strip()
            if statuses and status not in statuses:
                report("FAIL", "%s: [%s] status « %s » outside the vocabulary (%s)" % (name, tag, status, " / ".join(statuses)))
                errors += 1
            for field, vocabulary in required.items():
                found = re.search(r"%s ?: (\S+)" % re.escape(field), status_line)
                if not found:
                    report("FAIL", "%s: [%s] status line without « %s: » (%s)" % (name, tag, field, " / ".join(vocabulary)))
                    errors += 1
                elif found.group(1) not in vocabulary:
                    report("FAIL", "%s: [%s] %s « %s » outside the vocabulary (%s)" % (name, tag, field, found.group(1), " / ".join(vocabulary)))
                    errors += 1
            tags[tag] = {"line": index + 1, "status": status, "file": name}

    if errors == 0:
        report("OK", "todo grammar: %d piece(s) of work, heading and status conform" % len(tags))
    return tags


def check_item_prefixes(cfg, layout, report) -> None:
    """A prefix reserved for another tense inside the todo is an item nobody moved."""
    section = cfg.get("todo", {})
    allowed = section.get("item_prefixes", [])
    forbidden = section.get("forbidden_prefixes", [])
    if not forbidden:
        return
    pattern = re.compile(r"^\s*-\s*(%s)" % "|".join(re.escape(p) for p in forbidden))
    bad = 0
    for name in todo_names(cfg):
        for index, line in enumerate(read_lines(layout.framing / name)):
            match = pattern.match(line)
            if match:
                report("FAIL", "%s l.%d: prefix « %s » forbidden (vocabulary: %s — what is done leaves the todo)" % (name, index + 1, match.group(1), " ".join(allowed)))
                bad += 1
    if bad == 0:
        report("OK", "todo items: prefixes within the vocabulary (%s)" % " ".join(allowed))


def check_roadmap(cfg, layout, report, tags) -> None:
    heading = cfg.get("todo", {}).get("roadmap_heading")
    if not heading:
        return
    dormant = set(cfg.get("todo", {}).get("dormant_statuses", []))
    for name in todo_names(cfg):
        lines = read_lines(layout.framing / name)
        start = next((i for i, l in enumerate(lines) if re.match(heading, l)), None)
        if start is None:
            continue
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        cited = sorted({m for line in lines[start:end] for m in re.findall(r"\[([A-Z0-9-]+)\]", line)})
        stale = [t for t in cited if t not in tags or tags[t]["status"] in dormant]
        if stale:
            for tag in stale:
                report("WARN", "roadmap: [%s] closed or dormant — the snapshot is stale" % tag)
        else:
            report("OK", "roadmap: %d tag(s) cited, all still open" % len(cited))


def check_delivered(cfg, layout, report) -> set:
    """One narrative per tag, named after it, and every reference to one must resolve."""
    folder = layout.framing / cfg.get("framing", {}).get("delivered", "done")
    delivered = set()
    if not folder.is_dir():
        report("WARN", "%s/: absent — a tag that closes leaves no trace, and citations of it become unrepairable" % cfg.get("framing", {}).get("delivered", "done"))
        return delivered

    bad = [p for p in sorted(folder.glob("*.md")) if p.name != "README.md" and not re.match(r"^[A-Z0-9-]+\.md$", p.name)]
    for path in bad:
        report("FAIL", "%s/%s: name outside the tag convention" % (folder.name, path.name))
    files = [p for p in folder.glob("*.md") if p.name != "README.md"]
    delivered = {p.stem for p in files}
    if not bad:
        report("OK", "%s/: named by tag (%d file(s))" % (folder.name, len(files)))

    text = "\n".join(read_text(layout.framing / n) for n in todo_names(cfg))
    cited = sorted(set(re.findall(r"%s/([A-Z0-9-]+\.md)" % re.escape(folder.name), text)))
    dead = [c for c in cited if not (folder / c).is_file()]
    for name in dead:
        report("FAIL", "todo: dangling reference to %s/%s" % (folder.name, name))
    if not dead:
        report("OK", "todo: %d reference(s) to %s/ resolved" % (len(cited), folder.name))
    return delivered


def check_cited_tags(cfg, layout, report, tags, delivered) -> None:
    """Citing by identity protects a reference against a corpus that moves; nothing protects
    it against one that closes. A dead tag stays readable, plausible, and wrong."""
    known = set(tags) | set(delivered)
    # A framing that talks about the method writes the placeholder rather than a tag. Leaving
    # it to each workshop's configuration would mean every adopter meets the same false
    # positive and declares the same exception.
    excluded = {"TAG"} | set(cfg.get("todo", {}).get("known_foreign_tags", []))
    # Hyphens only between alphanumeric groups, never trailing. Without that, a character class
    # written in prose — `[A-Z0-9-]` — reads as a tag named "A-Z0-9-" and is reported as an
    # orphan. The check would then punish a document for explaining a pattern.
    shaped = re.compile(r"^[A-Z][A-Z0-9]*(-[A-Z0-9]+)*$")
    orphans = {}
    for path in framing_documents(cfg, layout):
        for index, line in enumerate(read_lines(path)):
            for tag in re.findall(r"\[([A-Z][A-Z0-9-]{2,})\]", line):
                if tag in known or tag in excluded or not shaped.match(tag):
                    continue
                orphans.setdefault(tag, []).append("%s:%d" % (path.name, index + 1))
    if not orphans:
        report("OK", "cited tags: all resolve to an open piece of work or a delivered narrative")
        return
    for tag, places in sorted(orphans.items()):
        report("WARN", "cited tag [%s] exists nowhere — %s" % (tag, ", ".join(places[:4])))


def check_header_dates(cfg, layout, report) -> None:
    """WARN only: modification times do not survive a clone, so this measures a working copy."""
    section = cfg.get("framing", {})
    pattern = section.get("date_pattern", r"(?:Dernière mise à jour|Last updated) ?: (\d{4}-\d{2}-\d{2})")
    tolerance = section.get("date_tolerance_days", 3)
    for name in section.get("dated_files", []):
        path = layout.framing / name
        if not path.is_file():
            continue
        match = re.search(pattern, read_text(path))
        if not match:
            report("WARN", "%s: no « last updated » line" % name)
            continue
        declared = datetime.strptime(match.group(1), "%Y-%m-%d").date()
        modified = date.fromtimestamp(path.stat().st_mtime)
        if (modified - declared).days > tolerance:
            report("WARN", "%s: header dated %s but modified %s — refresh the header" % (name, declared, modified))
        else:
            report("OK", "%s: header date consistent" % name)


# ============================================================================================
# Citations
# ============================================================================================


def framing_documents(cfg, layout) -> list:
    excluded = cfg.get("references", {}).get("exclude", [])
    documents = []
    for path in sorted(layout.framing.rglob("*.md")):
        if ".git" in path.parts:
            continue
        if any(path.match(pattern) for pattern in excluded):
            continue
        documents.append(path)
    return documents


class Resolver:
    def __init__(self, cfg, layout):
        self.layout = layout
        roots = [layout.framing, layout.workshop, layout.root]
        if layout.meta:
            roots.append(layout.meta)
        for extra in cfg.get("references", {}).get("extra_roots", []):
            candidate = (layout.workshop / extra).resolve()
            if candidate.exists():
                roots.append(candidate)
        self.roots = roots

    def resolve(self, token: str, from_dir: Path):
        """Returns the absolute path a citation resolves to, or None."""
        relative = token.replace("/", os.sep)
        if re.match(r"^([A-Za-z]:|[\\/])", relative):
            candidate = Path(relative)
            return candidate if candidate.exists() else None
        for root in [from_dir] + self.roots:
            candidate = root / relative
            if candidate.exists():
                return candidate.resolve()
        return None

    def is_outside(self, resolved: Path) -> bool:
        """Method and instance excepted, a citation leaving the workshop is a redirect
        candidate. WARN, not FAIL — the defect is semantic and this is only its shadow."""
        allowed = [self.layout.workshop]
        if self.layout.method:
            allowed.append(self.layout.method)
        if self.layout.instance:
            allowed.append(self.layout.instance)
        for base in allowed:
            try:
                resolved.relative_to(base)
                return False
            except ValueError:
                continue
        return True


def check_citations(cfg, layout, report) -> None:
    section = cfg.get("references", {})
    prefixes = section.get("must_resolve_prefixes", [])
    resolver = Resolver(cfg, layout)
    documents = framing_documents(cfg, layout)

    links = bad_links = 0
    outside = []

    # 1. LINKS — a link is unambiguously a location: it is clickable.
    for document in documents:
        for index, line in enumerate(read_lines(document)):
            for match in re.finditer(r"\]\(([^)\s]+)\)", line):
                target = match.group(1)
                if re.match(r"^(https?:|mailto:|#)", target):
                    continue
                target = target.split("#")[0]
                if not target:
                    continue
                links += 1
                resolved = resolver.resolve(target, document.parent)
                if resolved is None:
                    bad_links += 1
                    report("FAIL", "dangling link — %s:%d « %s »" % (document.name, index + 1, target))
                elif resolver.is_outside(resolved):
                    outside.append("%s:%d « %s »" % (document.name, index + 1, target))
    if bad_links == 0:
        report("OK", "markdown links: %d target(s), all resolved" % links)

    # 2. DECLARED PREFIXES — narrow on purpose. A lint verifies what is declared to be a
    # location; it does not guess. Resolving every path-shaped token produced several hundred
    # false failures on a real workshop, because almost all of them are identities.
    if prefixes:
        cited = bad = 0
        for document in documents:
            for index, line in enumerate(read_lines(document)):
                for match in re.finditer(r"`([^`]+)`", line):
                    token = match.group(1).strip().rstrip(".,;:")
                    if re.search(r"[\s<>*?|\"…]", token):
                        continue
                    if not any(token.startswith(p) for p in prefixes):
                        continue
                    cited += 1
                    resolved = resolver.resolve(token, document.parent)
                    if resolved is None:
                        bad += 1
                        report("FAIL", "dangling location — %s:%d « %s »" % (document.name, index + 1, token))
                    elif resolver.is_outside(resolved):
                        outside.append("%s:%d « %s »" % (document.name, index + 1, token))
        if bad == 0:
            report("OK", "declared locations: %d cited, all resolved" % cited)

    # 3. REDIRECT CANDIDATES
    if outside:
        report("WARN", "%d citation(s) leaving the workshop — redirect candidates, to be read" % len(outside))
        for place in outside[:10]:
            report.detail(place)
    else:
        report("OK", "no citation leaves the workshop")

    # 4. RETIRED NAMES — the migration check. The list belongs to the workshop being migrated.
    # ⚠ The pattern is matched LITERALLY. An early version escaped it for a regular expression
    # while asking for a literal match: it searched for the escape characters themselves and
    # reported only the one token that had none — seventeen occurrences missed in silence.
    retired = section.get("retired", {})
    if retired:
        scan = [layout.framing] + [
            layout.workshop / name for name in section.get("also_scan", [])
        ]
        files = []
        for base in scan:
            if not base.is_dir():
                continue
            for path in base.rglob("*"):
                if not path.is_file():
                    continue
                if {".git", "bin", "obj", "node_modules"} & set(path.parts):
                    continue
                if any(path.match(pattern) for pattern in section.get("exclude", [])):
                    continue
                if path.stat().st_size > 1_000_000:
                    continue
                files.append(path)
        hits = 0
        for old, replacement in retired.items():
            for path in files:
                try:
                    content = read_text(path)
                except (UnicodeDecodeError, OSError):
                    continue
                for index, line in enumerate(content.splitlines()):
                    if old in line:
                        hits += 1
                        report("FAIL", "retired name « %s » — %s:%d → %s" % (old, path.name, index + 1, replacement))
        if hits == 0:
            report("OK", "retired names: no occurrence of the %d declared name(s)" % len(retired))


# ============================================================================================
# Checks a workshop declares for itself
# ============================================================================================


def git(repository: Path, *args):
    try:
        done = subprocess.run(
            ["git", *args], cwd=str(repository), capture_output=True, text=True, encoding="utf-8"
        )
    except FileNotFoundError:
        return None
    return done


def check_repositories(cfg, layout, report) -> None:
    """Every repository the workshop frames. A commit that is never pushed protects nothing."""
    repositories = cfg.get("workshop", {}).get("repositories", [])
    if not repositories:
        return
    expected = cfg.get("checks", {}).get("line_ending_files", [])

    for name in repositories:
        path = layout.framing if name == layout.framing.name else layout.workshop / name
        if not path.is_dir():
            report("FAIL", "%s: declared by the workshop but absent from disk" % name)
            continue
        if not (path / ".git").exists():
            report("WARN", "%s: not a Git repository — the work there is not saved" % name)
            continue

        missing = [f for f in expected if not (path / f).is_file()]
        if expected:
            if missing:
                report("FAIL", "%s: missing %s (line-ending convention)" % (name, ", ".join(missing)))
            else:
                report("OK", "%s: line-ending files present" % name)

        if cfg.get("checks", {}).get("line_endings"):
            done = git(path, "ls-files", "--eol")
            if done and done.returncode == 0:
                drifted = len([l for l in done.stdout.splitlines() if re.search(r"\sw/crlf\s", l)])
                if drifted == 0:
                    report("OK", "%s: no file drifted to CRLF on disk" % name)
                else:
                    report("WARN", "%s: %d file(s) CRLF on disk — an editor re-derived them" % (name, drifted))

        done = git(path, "log", "--oneline", "@{u}..HEAD")
        if done is None:
            report("WARN", "%s: git is not available — repository state unknown" % name)
        elif done.returncode != 0:
            report("WARN", "%s: no tracking remote — nothing is saved off this machine" % name)
        else:
            pending = len([l for l in done.stdout.splitlines() if l.strip()])
            if pending == 0:
                report("OK", "%s: nothing waiting to be pushed" % name)
            else:
                report("WARN", "%s: %d commit(s) waiting to be pushed" % (name, pending))


def exists_exact_case(path: Path) -> bool:
    """A name whose case differs from disk loads nothing on a case-sensitive file system, and
    works perfectly on the author's machine. That asymmetry is the whole point of the check."""
    if not path.exists():
        return False
    current = path.resolve()
    while True:
        parent = current.parent
        if parent == current:
            return True
        try:
            entries = os.listdir(parent)
        except OSError:
            return True
        if current.name not in entries:
            return False
        current = parent


def check_editor_workspaces(cfg, layout, report) -> None:
    """The folder list an agent is actually given. A wrong path here breaks nothing visible —
    it only makes the method unreadable, in silence."""
    if not cfg.get("checks", {}).get("editor_workspaces"):
        return
    files = sorted(layout.root.glob("*.code-workspace"))
    if not files:
        report("WARN", "no editor workspace found at the root — nothing declares what an agent reaches")
        return
    for workspace in files:
        content = read_text(workspace)
        folders = re.findall(r'"path"\s*:\s*"([^"]+)"', content)
        instructions = re.findall(r'"file"\s*:\s*"([^"]+)"', content)
        bad = []
        for reference in folders + instructions:
            target = layout.root / reference.replace("/", os.sep)
            if not target.exists():
                bad.append("%s (not found)" % reference)
            elif not exists_exact_case(target):
                bad.append("%s (case differs from disk)" % reference)
        if bad:
            for item in bad:
                report("FAIL", "%s: « %s »" % (workspace.name, item))
        else:
            report("OK", "%s: %d folder(s) and %d instruction file(s) resolved, exact case" % (workspace.name, len(folders), len(instructions)))


def check_echoed_items(cfg, layout, report) -> None:
    """Items a workshop wants read out at every run. A blocker that has to be remembered is a
    blocker that gets forgotten — echoing it costs nothing and removes the excuse."""
    prefixes = cfg.get("todo", {}).get("echo_prefixes", [])
    if not prefixes:
        return
    pattern = re.compile(r"^\s*-\s*(%s)" % "|".join(re.escape(p) for p in prefixes))
    found = []
    for name in todo_names(cfg):
        for line in read_lines(layout.framing / name):
            if pattern.match(line):
                found.append(line.strip().replace("**", ""))
    if not found:
        report("OK", "no item marked %s left open" % " ".join(prefixes))
        return
    report("WARN", "%d item(s) marked %s still open:" % (len(found), " ".join(prefixes)))
    for line in found:
        report.detail(line)


def check_external_tags(cfg, layout, report, tags) -> None:
    """Tags cited from outside the framing — a static site, a code repository — must still
    match an open piece of work. A citation left behind by a closed tag points at nothing, and
    unlike a dangling path it fails nowhere."""
    section = cfg.get("checks", {}).get("external_tags")
    if not section:
        return
    folder = layout.workshop / section["folder"]
    if not folder.is_dir():
        return
    pattern = re.compile(section["pattern"])
    cited = set()
    for path in folder.rglob(section.get("glob", "*.md")):
        for match in pattern.finditer(read_text(path)):
            cited.add(match.group(1))
    orphans = sorted(t for t in cited if t not in tags)
    if not orphans:
        report("OK", "%s: %d tag(s) cited, all attached to an open piece of work" % (section["folder"], len(cited)))
    else:
        report("WARN", "%s: orphan tag(s) — %s (closed? remove the marker or reopen the item)" % (section["folder"], ", ".join(orphans)))


def check_publication_files(cfg, layout, report) -> None:
    expected = cfg.get("checks", {}).get("publication_files", {})
    for repository, files in expected.items():
        path = layout.workshop / repository
        missing = [f for f in files if not (path / f).exists()]
        if missing:
            report("FAIL", "%s: missing publication file(s) — %s" % (repository, ", ".join(missing)))
        else:
            report("OK", "%s: publication files present" % repository)


# ============================================================================================
# Entry point
# ============================================================================================


def main(argv) -> int:
    parser = argparse.ArgumentParser(description="Framing checks of the method. See CONTRACT.md.")
    parser.add_argument("framing", nargs="?", default=".", help="the workshop's framing folder")
    parser.add_argument("--no-color", action="store_true")
    parser.add_argument("--layout", action="store_true", help="print what was resolved, and stop")
    arguments = parser.parse_args(argv)

    framing = Path(arguments.framing).resolve()
    if not framing.is_dir():
        sys.stderr.write("not a folder: %s\n" % framing)
        return 2

    color = not arguments.no_color and sys.stdout.isatty()
    report = Report(color)
    layout = Layout(framing)

    if arguments.layout:
        print(layout.describe())
        return 0

    config = load_config(framing, report)

    if layout.method is None:
        report("WARN", "method entry point not found by layout — reading-chain checks are partial")
    if layout.instance is None:
        report("WARN", "instance not found by layout — the identity slot cannot be measured")

    check_handoff(config, layout, report)
    check_todo_closed(config, layout, report)
    check_sizes(config, layout, report)
    check_bootstrap_load(config, layout, report)
    check_planning(config, layout, report)
    check_root_files(config, layout, report)
    tags = check_todo_grammar(config, layout, report)
    check_item_prefixes(config, layout, report)
    check_roadmap(config, layout, report, tags)
    delivered = check_delivered(config, layout, report)
    check_cited_tags(config, layout, report, tags, delivered)
    check_echoed_items(config, layout, report)
    check_external_tags(config, layout, report, tags)
    check_header_dates(config, layout, report)
    check_citations(config, layout, report)
    check_repositories(config, layout, report)
    check_editor_workspaces(config, layout, report)
    check_publication_files(config, layout, report)

    print("")
    counts = report.counts
    print("%d OK · %d WARN · %d FAIL" % (counts["OK"], counts["WARN"], counts["FAIL"]))
    if report.failed:
        print("Some checks FAIL — fix them before committing the session close.")
        return 1
    print("Framing sound.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
