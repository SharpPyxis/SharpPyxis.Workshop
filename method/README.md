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

Create an `instance/` folder **beside this repository** — a sibling, its own private
repository — holding an `index.md` that declares an identity file and the trigger of every
other file it carries. Then run `setup/workshop-setup.py` once per workshop; it resolves the
corpus around it and refuses to write if it cannot. The instance is yours and stays yours: the
method never reads its contents, only the index it declares.

⚠ There is no template for the instance yet. Creating one is the adopter's path, it has never
been exercised, and shipping an untested skeleton for it would be worse than saying so.

## A worked example

`../sample/` is a framing written under these rules — atlas, todo and handoff of a workshop
that names no product and no person. It is drawn from the framing of this method's own
development, which stays private for the same reason every workshop's does.
