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

**An editor wiring** listing, at minimum: the **meta level as a single folder**, and the new
framing folder. One entry, not one per folder inside the copy — the reason is in `bootstrap.md`
§ *Wiring a workshop*, and it is that the copy's composition belongs to its owner, not to the
method.

**The method's version, stamped** into the workshop's configuration, so a later lint can tell a
framing that is merely old from one that has drifted.

## What must be resolved, never assumed

**The corpus layout.** The relative path from the new workshop to the method and to the instance
is *computed*, not written in. It is resolved the same way the lint resolves it: **the meta level
is the folder holding `method/organization.md` and `instance/`**. That pair is the whole test, and
nothing depends on what any of it is called.

⚠ The rule used to read *"the folder holding both a framing folder and an instance folder"*, and
it was wrong in a way worth recording, because nothing short of standing on another machine would
have shown it. It was read off the one corpus where the method is **developed** — and there, and
only there, the meta level carries a framing folder too. For everyone else the condition is false
by construction, so both this installer and the lint refused to resolve a perfectly correct
layout. **A rule inferred from the only instance you can see is a rule you have not tested**, and
the meta level is the one place where the author's machine is not like anyone else's.

**A new workshop is wired to the received copy**, never to a working copy of the method. On the
machine where the method is written both exist, and the distinction stops being academic: the
installer refuses to run when the script it was launched from is not the one the corpus resolves.
⚠ That check needs an existing workshop to resolve the corpus from, so it cannot guard the first
one — § *The first workshop on a machine* says what replaces it there.

⚠ If either cannot be resolved, the installer **stops without writing**. The alternative — emit a
plausible relative path and let it be wrong — produces a workshop that starts every session from
a corpus that is not the one intended, which is the failure mode this method was written against:
not "nothing loads" but "something else loads", confidently, with no signal.

### The first workshop on a machine

An implementation learns the corpus root and the framing-folder name from an existing workshop.
On a fresh machine there is none, and that must not make the first workshop the one laid out by
hand: the argument for having an installer at all is that a hand-made workshop drifts from the
others, so the very first one would be the most likely to.

Both unknowns are **read**, and neither is assumed — no `--root` flag, which would move the
decision to someone with less to go on than the corpus has:

- **the root is the parent of the meta level**, and the meta level is where the implementation
  itself lives;
- **the framing folder's name is the name of the single folder under `templates/workshop/`**.

⚠ **This path loses the guard that protects the other one, and must replace it.** Deriving the
meta level *from the implementation* makes "the script must be the one the corpus resolves"
compare a thing to itself. Three refusals stand in its place, and the first is the one that
matters:

- **the root must not itself be a workshop** — it holds no framing folder. A root that does means
  the implementation is running from a **working copy of the method**, one level too deep, and
  creating a workshop from there wires it to files no session will ever read;
- **the root must hold no workshop at all.** Day zero is a state of the disk, not a mode to
  select: where a workshop exists, its conventions are read rather than rebuilt from templates;
- **an origin that was given and does not resolve is a mistake to report**, never a reason to
  fall back. A mistyped path silently treated as day zero is the same failure in a new place.

⚠ What day zero cannot learn, it must **under-declare rather than invent**. Which instance files
are read unconditionally is one: `index.md` is the only name the method guarantees, and the
identity file beside it is named by the index — reading a name out of someone's prose is exactly
the guess this contract exists to forbid. Declare the index alone and **say so in the report**, so
the developer adds the other name while the corpus is in front of them. It is the call `[sizes]`
already makes by shipping empty: a value invented at creation is worse than one posted at the
first close.

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

⚠ **What is learned must be reported, one line per thing copied.** Learning from a corpus
reproduces its accidents as faithfully as its conventions, and nothing in the reading tells the
two apart — so the only person who can is the developer, at the moment the copy happens.
Observed on the first workshop this installer created: it faithfully reproduced lists of
instruction files that an agent had added to every wiring unasked, and its report said only
*"conventions read from the corpus"*. A summary that cannot be contradicted is not a report.

⚠ And a wiring an installer writes declares **folders, and nothing that names a file to read**.
A per-tool list of instruction files is a second starting point; § *Tool-specific files* in
`bootstrap.md` lets a workshop keep one deliberately, which is exactly why a script must not
create one on the developer's behalf.

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
