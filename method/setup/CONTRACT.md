# Setup contract — what creating a workshop must produce

> **Read when** creating a workshop, or reimplementing the installer for another environment.
> **Do not read** during ordinary work.

This file is the portable part. It states **what** a creation must produce and why each piece is
there. `workshop-setup.py` is one implementation of it — the reference one, shipped so that
adopting the method does not start with writing a tool. What it copies lives in `templates/`.

⚠ Creating a workshop is mechanical, and that is the whole argument for a script. An agent that
deviates from a copy procedure produces a workshop subtly different from the others — which
nobody notices for six months, and which then has to be reconciled by hand across every
workshop that drifted.

---

## The one rule that bounds the whole thing

**Creating a wiring is a right; changing one is not.** `bootstrap.md` § *Changing a wiring, and
from where* says a workshop's folder list is changed from a session of that workshop. Creation is
the exception, and for a mechanical reason rather than a permissive one: the target workshop has
no session yet, so no other author is possible.

The right is therefore **unique and non-renewable**. The installer writes the new workshop's
files once, at birth. The second time a session from elsewhere touches those same files it is no
longer the author, it is the neighbour, and the rule applies in full. That is why the installer
**refuses to run against anything that already exists** rather than merging or updating: the
existence of the target is exactly what tells it which side of the rule it is on.

⚠ And it stops at the skeleton. The installer creates; it does not migrate content, does not open
the new workshop, and does not continue working in it.

## What must be produced

**A workshop folder**, named as the developer named it, at the corpus root — beside the other
workshops, never inside one.

**A framing folder inside it**, which is a repository of its own, holding: the atlas, the todo,
the handoff under `memories/`, the delivered-narrative folder, the long-form folder, and the
workshop's lint configuration. ⚠ The delivered-narrative and long-form folders are created
**empty and from the start**. Both have been observed missing from a workshop that needed them
on its first day, and the first is worse than an inconvenience: a tag that closes with nowhere to
leave its narrative makes every earlier citation of it unrepairable.

**One commit** in that repository, and **no remote**. Where a framing is pushed is an owner's
decision, and guessing a host is not a service. ⚠ The state that leaves is therefore *not backed
up*, and the created todo says so rather than leaving it to be discovered.

**Optionally, the workshop's code repositories**, each initialised the same way.

**An editor wiring** listing, at minimum: the method's `method/` folder, the instance folder, and
the new framing folder. Point at `method/`, not at the repository root — a workshop that consumes
the method has no business seeing its sample or its plumbing.

**The method's version, stamped** into the workshop's configuration, so a later lint can tell a
framing that is merely old from one that has drifted.

## What must be resolved, never assumed

**The corpus layout.** The relative path from the new workshop to the method and to the instance
is *computed*, not written in. It is resolved the same way the lint resolves it: the meta level is
the folder holding both a framing folder and an instance folder; the method is the repository
inside it that declares the entry point. Nothing depends on what any of them is called.

⚠ If either cannot be resolved, the installer **stops without writing**. The alternative — emit a
plausible relative path and let it be wrong — produces a workshop that starts every session from
a corpus that is not the one intended, which is the failure mode this method was written against:
not "nothing loads" but "something else loads", confidently, with no signal.

## What must be learned, never invented

The editor wiring file is **tool-specific, and the method says nothing about which tool**.
Filenames and auto-loading rules differ per tool and change with tool versions; a method that
mandated them would ship rules that are wrong everywhere they were not tested.

An implementation may nonetheless emit one, on one condition: **it derives the convention from
what the corpus already shows, rather than probing the machine or hard-coding a preference.** If
sibling workshops already carry a wiring file, its format, its folder labels and its settings are
read from them and reproduced. If none exists, the implementation asks rather than choosing.

The distinction matters and is not pedantry: reading the corpus is deterministic and inspectable;
detecting an installed editor is a guess about a machine that changes.

## What must not be produced

**Nothing in the parent workshop.** Not a pointer, not a tag, not a path — the installer writes
no file outside the workshop it creates.

This is the moment the sentence "the follow-up is steered over there" gets written, and it is
true the day it is written, which is exactly what makes it dangerous afterwards. A vigilance rule
would not survive; a mechanism does. The installer's entire output towards the parent is a line
**printed to the developer**: the workshop exists, here is what to open. Whether that fact is
worth one factual sentence in the parent's handoff is the developer's call, made in their own
words, in their own session.

⚠ The symmetric failure is already recorded: three citations of a closed tag survived it, stayed
readable and plausible, and two of them announced a blocker that had been lifted. A citation left
behind by a workshop that moved on fails nowhere at all.

## Levels

The implementation reports what it did, one line per artefact, and exits non-zero on refusal.
⚠ A refusal is a normal outcome, not an error to work around: every refusal in this contract
exists because the alternative is a silently wrong workshop.
