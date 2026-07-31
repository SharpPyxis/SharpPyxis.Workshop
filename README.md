# workshop

A **workshop** is a unit of work that owns its framing. It may hold one product spread
over several repositories, or a single independent library. Each workshop carries a
`_workspace/` folder holding its atlas, its todo and its handoff. This repository
defines what workshops are, and how one developer and their AI agents work inside them.

## What is here

| | Contents |
| --- | --- |
| `method/` | Rules, lints, templates and the installer. What anyone can adopt. |
| `sample/` | A worked example of a framing — atlas, todo, handoff — naming no product and no person. |

## What is deliberately not

Two things live **outside** this repository, in sibling repositories that are never
published:

- an **instance** — one owner's profile, transverse technical conventions and
  notebooks. The method never reads its contents, only the index it declares;
- the **framing of this repository's own development** — its `_workspace/`, held to the
  same rule as every workshop's: private. `sample/` exists so that an example can ship
  without shipping someone's working notes.

The rule that decides every borderline case:

> **The method declares slots; the instance fills them.** *That there is a corpus of
> transverse technical conventions, read on demand before writing that kind of code*
> is method. What that corpus says is instance.

Because nothing private is inside this tree, publishing is pushing the repository as it
stands — no export step, no filtering, and no rule to remember at the moment it matters.
A boundary drawn by structure holds against a mistyped command; one drawn by an entry in
a `.gitignore` holds only as long as the entry does.

⚠ `sample/` must **not** be placed next to an actual `_workspace/` when the method is
adopted — it would become a second source of truth for framing, which is exactly the
drift the method is designed to prevent.

A third destination exists and is not here: reusable **code** and its reference
documentation live in a code repository, versioned with what they document. If it
compiles, it does not belong here.

## Entry point

The method declares **one** path: `method/organisation.md`. Everything else is reached
from there, so that adopting the method never means rewriting a dozen hardcoded
locations. The instance is found **beside** this repository, by the layout the method
declares — not by a path written into it.

How an agent comes to read that file is tool-specific, changes with tool versions, and
is deliberately **not** part of the method. Naming the path at the start of a session is
the reliable gesture. Measured on the repositories this method came from: seven per-tool
trigger files existed, and not one of them reached the agent.

## Status

Under construction. Nothing here is referenced by any workspace yet — the previous
corpus stays authoritative until the switch happens in one step.

Two decisions are deliberately left open rather than guessed:

- ⬜ the published name of `method/`;
- ⬜ its license, to be chosen before the first publication.
