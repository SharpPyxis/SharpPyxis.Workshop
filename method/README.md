# The method

The rules themselves. What problem they address and where they come from is in the
[repository readme](../README.md); this file says what is in this folder, and how to use it.

Three ideas run through everything here:

- **documents separated by tense** — what *is* (atlas), what is *open* (todo), what is
  *volatile* (handoff), what is *done* (a delivered narrative), what is *not yet scoped*
  (planning). An item lives in exactly one of them;
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
| `templates/` | An empty workshop, an empty instance, and the installer |
| `VERSION` | Stamped into every workshop the installer creates |

## Reading it for the first time

Read `organization.md`. It is the only file meant to be read in full and in order — the
others are reached from it, when their trigger fires. Reading them all up front is the one
way to spend the budget the method exists to protect.

## Adopting it

Copy `templates/instance/` **beside the repository** — a sibling folder named `instance/`,
its own private repository — fill in the profile, then run the installer for each workshop.
The instance is yours and stays yours: the method never reads its contents, only the index
it declares.

## A worked example

`../sample/` is a framing written under these rules — atlas, todo and handoff of a workshop
that names no product and no person. It is drawn from the framing of this method's own
development, which stays private for the same reason every workshop's does.
