# workshop

A **workshop** is a unit of work that owns its framing. It may hold one product spread
over several repositories, or a single independent library. Each workshop carries a
`_workspace/` folder holding its atlas, its todo and its handoff. This repository
defines what workshops are, and how one developer and their AI agents work inside them.

## The layout, in full

Everything below sits under whatever folder you keep your work in. That root has no
meaning of its own — the method never reads anything from it.

```text
projects/                        the root. Not a repository. Nothing is read from it.
│
├── _workshop/                   THE META LEVEL — one per machine, shared by every workshop
│   ├── workshop/                  public repository: the method (this one)
│   │   ├── method/                  the rules — one entry point, the rest behind triggers
│   │   └── sample/                  a worked example of a framing
│   ├── instance/                  PRIVATE repository: profile, conventions, notebooks
│   └── _workspace/                PRIVATE repository: framing of the method's own work
│
├── Ledger/                      A WORKSHOP — not a repository, owns exactly one framing
│   ├── ledger.api/                a repository — a project in the ordinary sense
│   │   ├── src/
│   │   ├── tests/
│   │   ├── docs/
│   │   ├── README.md
│   │   ├── .gitignore
│   │   └── .gitattributes
│   ├── ledger.web/                another repository — same workshop, same framing
│   │   ├── src/
│   │   ├── tests/
│   │   └── package.json
│   └── _workspace/                THE FRAMING — outside every code repository
│       ├── atlas.md                 what exists and works
│       ├── todo.md                  what is open
│       ├── planning/                what is not yet scoped
│       ├── delivered/               what is done — one file per [TAG]
│       └── memories/
│           ├── handoff.md           what is volatile — one entry per session
│           └── shared/              stable facts, reachable from an index
│
└── TinyParse/                   ANOTHER WORKSHOP — a single independent library
    ├── tinyparse/                 one repository is enough
    └── _workspace/                it still owns its framing
```

### Four levels, and one test to tell them apart

- **A workshop is any folder that contains a `_workspace/`.** That is the whole test — not
  its name, not its depth, not whether it looks important. `Ledger/` and `TinyParse/` are
  workshops; so is `_workshop/`, and that is not a coincidence: the method is developed
  under its own rules.
- **A repository is where code lives**, with whatever skeleton its stack expects. A
  repository never contains a `_workspace/`, and a workshop is never itself a repository —
  the folder `Ledger/` is not versioned; `ledger.api/` and `ledger.web/` are.
- **`_workspace/` sits outside every code repository**, so the framing never rides along in
  a code commit. It may have a private backup repository of its own — that is a backup, not
  a tracking tool; the tracking is the files.
- **Several repositories, one workshop, as long as they serve one framing.** Two sets with
  independent framing are two workshops, however tempting it is to keep them together.

### What the layout is designed to prevent

- **A `_workspace/` is never published**, including this repository's own. Framing documents
  carry names, decisions and session context that belong to their owner. What ships as an
  example is `sample/`, written for that purpose.
- **`sample/` is never placed next to a real `_workspace/`.** Two framings side by side is
  two sources of truth, which is the exact drift the method exists to prevent.
- **Nothing private ever sits inside a published tree, not even ignored.** A boundary drawn
  by structure holds against a mistyped command; a `.gitignore` entry holds only as long as
  the entry does.

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

The method declares **one** path: `method/organization.md`. Everything else is reached
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
