# Git — repositories, boundaries, publication

> **Read when** creating a repository, writing or changing a `.gitignore`, deciding whether a
> file should be tracked, or preparing a publication.
> **Do not read** to commit normally — the two frequent rules, message language and honest
> scope, are in the map (`organisation.md` § *Commits*).

---

## Creating a repository

Two files at creation, every time:

- **`.gitattributes`** with `* text=auto eol=lf`, so the checkout writes LF whatever the
  cloner's configuration. Command scripts that require CRLF are the exception and are listed
  explicitly.
- **`.editorconfig`** with `end_of_line = lf`, respected by editors for new files.

Both, plus a global `core.autocrlf=false`, because each covers a hole the others leave.
Without them, a clone on a foreign platform rewrites every line and the next commit shows
thousands of phantom diffs.

## The `.gitignore` is authoritative

It is the reference on the versioned / local boundary. It decides — the name of a folder does
not. A folder called `local/` is **not** automatically excluded; only this file, or its
silence, decides.

**It must be richly commented.** Every entry, or group of entries, says *why* it is ignored:
secret, build artefact, local tooling, machine configuration. A readable `.gitignore`
prevents case-by-case judgement, by a human as much as by an agent.

### The criterion is not "anchored", it is "can this rule be wrong?"

An unanchored ignore rule is a decision taken in advance about cases nobody has seen yet.

Observed: a `dist/` rule, posted in an empty section for a stack the repository did not use,
silently ignored a vendored library folder several levels down. Nothing failed, nothing was
reported — the folder was simply absent from `git status`, and would have been absent from
the clone. A library shipped under that conventional name would have vanished without an
error, and the clone on the other side would no longer build with nothing to say why.

The costs are not symmetric: **a file wrongly ignored is invisible, a file wrongly tracked is
obvious immediately.** So the test is whether the rule can ever be wrong. A dependency
directory nobody would ever version is safe unanchored; a name as common as `dist/` is not.

A rule that protects nothing is deleted rather than anchored. When the case it anticipated
actually arrives, it arrives with its own rule, anchored to its own folder.

## Publication

### A boundary drawn by structure, not by a rule

Private content does not belong inside a published tree, **not even ignored**.

An entry in a `.gitignore` is a *declared* safety: it holds as long as the rule is respected.
Structure is a safety that holds against a mistyped command — what is not in the tree cannot
be pushed, whatever is typed.

Three ways to lose the declared version, all observed or one command away:

- `git clean -xdf` deletes ignored content — including a nested repository and its history;
- one edited line in the `.gitignore` makes the content publishable, with no signal;
- `git status` never shows what changes under an ignored path, so the blindness is permanent
  and has to be compensated by tooling built for that purpose alone.

The same principle applies one level up: **visibility is safer carried by the host than by a
setting.** Public and private repositories on separate hosts cannot be confused by a
mis-clicked toggle. In a single place where both natures coexist, one stops reading the badge
— vigilance wears out, a host separation does not.

### Untracking does not erase history

`git rm --cached` removes a file from tracking, **not from the history**. A repository that
once committed private content still contains it, in full, for anyone who clones it.

The fix is to restart or rewrite the history, and its cost only grows: at four commits it is
free, at four hundred it means losing the record of real work. **After the first push it is
permanent.** Any repository intended for publication is therefore checked for this *before*
its first push, not before its first release.

### The commit header is a public surface too

Clean content is not a clean repository. Every commit carries an author name and address, and
these are published with it. They are easy to forget precisely because they are never typed
by hand.

Set the identity **local to the repository** — a no-reply address where the host provides one,
so attribution survives without publishing a real address. And prefer, where the host offers
it, the setting that makes a push **fail** when it would expose a real address: a local
setting protects one repository, and the next one will inherit the global default.

### Publication files

A repository meant for publication carries a readme, a license, and a notice of the
third-party components it redistributes with their licenses. **Coherence is checked at commit
time, not at release time**: the commit that adds a dependency updates the notices in the same
commit, and a notable change of surface re-reads the readme. Create a missing file rather than
defer it.

### The private-to-public pass

Opening a repository is a **dedicated pass**, not a series of case-by-case calls made along
the way: review the `.gitignore`, the tracked content, the history, and the commit identities,
and decide what must not become public.

Deciding it in advance, file by file, over months, is how something is missed.
