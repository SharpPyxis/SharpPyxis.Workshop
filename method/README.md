# The workshop method

A tracking method for a solo developer working with AI agents.

Its subject is narrow on purpose: **what an agent must read before being useful, and
what a session must leave behind so the next one starts informed.** It is not a
project-management framework — there is no estimation, no board, no ceremony.

## The problem it addresses

An agent starts every session knowing nothing. What it reads first decides the
quality of everything that follows, and that reading has a cost paid again at every
start. Left untended, the framing files grow until the essential drowns in the
merely true.

The method answers with three ideas:

- **documents separated by tense** — what *is* (atlas), what is *open* (todo), what
  is *volatile* (handoff), what is *done* (a delivered narrative), what is *not yet
  scoped* (planning). An item lives in exactly one of them;
- **reading by trigger** — almost nothing is read unconditionally. Conventions are
  read before writing that kind of code, the closing protocol before closing;
- **a measured bootstrap load** — the sum of what is read at every start is a budget,
  and the lint reports it. A rule that nobody can afford to read is not a rule.

## Layout

| | |
| --- | --- |
| `organisation.md` | The single entry point: the map, and the reading order |
| `tracking.md` | Roles and life cycle of the framing documents, the todo grammar, the closing protocol |
| `bootstrap.md` | The reading chain, its load and its budget |
| `memory.md` | A tool's private memory versus memory shared between agents |
| `lint/` | The checks, in one place, with per-workshop thresholds |
| `templates/` | An empty workshop, an empty instance, and the installer |
| `VERSION` | Stamped into every workshop the installer creates |

## Adopting it

Copy `templates/instance/` **beside the repository** — a sibling folder named
`instance/`, its own private repository — fill in the profile, then run the installer
for each workshop. The instance is yours and stays yours: the method never reads its
contents, only the index it declares.

## A worked example

`../sample/` is a framing written under these rules — atlas, todo and handoff of a
workshop that names no product and no person. It is drawn from the framing of this
method's own development, which stays private for the same reason every workshop's
does.
