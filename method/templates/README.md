# templates/ — what gets copied

> **Read when** changing what a new workshop is created with.
> **Do not read** to create one — that is the installer's job (`method/setup/`).

This folder holds **material**, not a tool. The tool that copies it lives in `method/setup/`,
for the same reason the lint's contract lives beside its implementation and not inside the
workshops it checks: what is copied and what does the copying are two different things, and
merging them is how a template starts carrying behaviour.

## What is deliberately absent

**Prose.** The framing files created here are a title and, where the lint needs one, a date
line. No explanatory header. A header that restates `tracking.md` is a second source of truth,
posted at creation, in a file nobody will re-read — and it goes stale exactly like every other
sentence that was true the day it was written.

The one exception is the `[SETUP]` piece of work in the todo: it lists the decisions the
installer deliberately did **not** take. It is the accompanying note, it is written to be
deleted, and it says so.

**Numbers.** No threshold is posted. A threshold set before a workshop has any content is
guesswork that will be either ignored or wrong. See `method/lint/CONTRACT.md` § *Configuration*.

**A language.** Nothing here has to be English for the lint to pass: its default patterns accept
both `Last updated:` and `Dernière mise à jour :`, both `> status:` and `> statut :`. A workshop
that writes its framing in another language translates the three status values in `lint.toml`
and changes nothing else.

## Dotfiles are stored without their dot

`gitattributes`, `editorconfig`, `gitignore` — the installer renames them on copy. Stored with
their leading dot they would take effect **inside this repository**, which is a template acting
at a distance on the corpus that ships it.

## Layout

| | |
| --- | --- |
| `repo/` | The two line-ending files every repository gets, the framing folder included (`method/git.md` § *Creating a repository*) |
| `code-repo/` | What only a code repository gets on top: its `.gitignore`, and a readme holding its name |
| `workshop/` | An empty workshop: its framing folder, and nothing else |

⚠ **No `src/`, no `tests/`, no `docs/`.** `organization.md` says a repository's internal skeleton
is whatever its stack expects and that the method says nothing about it — and the repository
readme illustrates exactly that, laying its two example repositories out differently on purpose.
A tree posted here would contradict the rule, and would have to be held up by placeholder files,
since git does not keep empty folders. What a stack expects is the stack's tooling to create, or
the instance's to declare; it is not the method's to guess.

⚠ `templates/instance/` does not exist yet. Creating an instance is the other path — an adopter
setting the method up on a machine — and it has never been exercised. `organization.md` announces
this folder for both; that half is not delivered.
