# The method

The rules themselves. What problem they address and where they come from is in the
[repository readme](../README.md); this file says what is in this folder, and how to use it.

Three ideas run through everything here:

- **documents separated by tense** — what *is* (atlas), what is *open* (todo), what is
  *volatile* (handoff), what is *finished* (`done/`). An item lives in exactly one of them,
  and `_planning/` holds the long form of anything that does not fit on a line, at any stage;
- **reading by trigger** — almost nothing is read unconditionally. Each file states in its
  own header when it is to be read, and when it is not;
- **a measured bootstrap load** — the sum of what is read at every start is a budget, and
  the lint reports it. A rule nobody can afford to read is not a rule.

## Layout

| | |
| --- | --- |
| `organization.md` | The single entry point: the map, and the reading order |
| `onboarding.md` | Building a first instance, when there is none — an interview, offered and never started unasked |
| `corpus.md` | Writing a trigger, and cutting a set of files by it |
| `tracking.md` | Roles and life cycle of the framing documents, the todo grammar, the closing protocol |
| `bootstrap.md` | The reading chain, its load and its budget |
| `memory.md` | A tool's private memory versus memory shared between agents |
| `git.md` | Repository creation, the versioned / local boundary, publication |
| `lint/` | The checks, in one place, with per-workshop thresholds |
| `setup/` | Creating a workshop: the contract, and the installer |
| `templates/` | What a new workshop is created with |
| `VERSION` | Stamped into every workshop the installer creates |

## Reading it for the first time

Read `organization.md`. It is the only file meant to be read in full and in order — the
others are reached from it, when their trigger fires. Reading them all up front is the one
way to spend the budget the method exists to protect.

## Adopting it

Copy the repository to a folder of your own — `_workshop/` by habit, though nothing reads the
name — and fill the `instance/` it ships empty: an `index.md` declaring an identity file and the
trigger of every other file it carries. Then run `setup/workshop-setup.py` once per workshop; it
resolves the corpus around it and refuses to write if it cannot. The instance is yours and stays
yours: the method never reads its contents, only the index it declares.

⚠ **A copy, not a clone.** Your folder holds your profile and your conventions; this repository
is upstream and nothing travels back to it. Updating means copying a newer `method/` over yours,
and leaving `instance/` alone — it is the one folder an update must never touch.

⚠ `instance/` ships with a readme and nothing else. Shipping a skeleton `index.md` would be
shipping an untested model, which costs more than an absent one, since a model is copied without
being re-read. **You do not have to write the first one alone**: the first session that finds no
instance offers to build it with you, in ten minutes of questions — `onboarding.md`. It offers
and waits; it never takes over a session you opened for something else.

## A worked example

`../sample/` is a framing written under these rules — atlas, todo and handoff of a workshop
that names no product and no person. It is drawn from the framing of this method's own
development, which stays private for the same reason every workshop's does.
