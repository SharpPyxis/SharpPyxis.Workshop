# SharpPyxis.Workshop

A tracking method for one developer working with AI agents.

**[www.sharppyxis.fr](https://www.sharppyxis.fr)** — the same method in prose: who reads what and
when, what happens during a session, what the close records. English and French.

> **Opening a session, name the workshop and the entry point.** One sentence, and it never
> silently fails:
>
> ```text
> Hello — we are working on Ledger today.
> Entry point: projects/_workshop/method/organization.md
> ```
>
> That is the whole gesture. Why it is typed rather than configured: § *Entry point*, below.
>
> **Arriving for the first time?** That sentence is not yours yet — it names a workshop, and you
> have none. Start at § *Getting started*: a copy, a folder, and one conversation.

Its subject is narrow on purpose: **what an agent must read before it can be useful, and
what a session must leave behind so the next one starts informed.**

The upkeep is the agent's job. Yours is to review it.

## The problem it addresses

An agent starts every session knowing nothing. What it reads first decides the quality of
everything that follows, and that reading is paid again at every start.

The obvious answer — write things down — fails in a specific way, and usually in this
order:

- the notes grow until reading them costs more than they save. Since they are re-read at
  every session start, that cost is paid again and again;
- the same fact ends up in three files that disagree. You stop trusting them, and shortly
  after, you stop writing them;
- a decision taken three weeks ago is contradicted by one taken today, and nothing
  notices — you kept the whole picture in your head, and the agent never had it;
- the conventions file you were certain the agent had read was never within its reach.

None of these is a failure of discipline. They are what happens to notes that have no
assigned place, no reading budget, and no check.

## What it gives you

- **One place per kind of fact, so there is exactly one.** Four tenses — what *is*, what is
  *open*, what is *volatile*, what is *finished* — and an item lives in exactly one of them,
  plus one long form for whatever does not fit on a line. Most drift in a framing folder is
  one document quietly taking on another's job.
- **A reading budget that does not grow with your notes.** What is read at every start is a
  map. Everything else is reached by a trigger stated in the file's own header: conventions
  before writing that kind of code, the closing protocol before closing. Your framing can
  grow; your start-up cost does not.
- **A session that ends in a defined state.** A closing protocol says what to record, where,
  and in what order — so the next session starts from something written rather than from a
  reconstruction.
- **Checks rather than good intentions.** A lint reports the drift the rules exist to
  prevent, including the size of what is read at every start. A rule nobody can afford to
  read is not a rule.
- **The same layout everywhere.** An installer lays out each workshop identically, so what
  you learn in one applies to the next — including the one you create in six months.

## Written to be executed, not only respected

Most of what is written here is addressed to the agent rather than to you. The rules are
specific enough to be applied without a judgement call: what to record at the end of a
session, in which file, in what order, with what grammar; when an item leaves the todo;
where a guard-rail goes once the work that produced it closes.

That is the point of the whole thing: **the framing maintains itself as a by-product of the
work.** The agent writes the handoff entry, moves out what closed, updates the atlas, runs
the lint and commits. Upkeep stops being a task to remember at the end of a long session —
which is precisely when it does not get done.

You stay the arbiter, and the design assumes it. What is a guard-rail rather than a passing
precaution, what is genuinely finished, which decision must not be guessed — those are
yours. The todo grammar gives each its own mark (⚠, ✅, ❓) so that an agent **flags** them
instead of deciding them, and the lint keeps the review cheap: you read a report, not every
file.

## What you have to say

The writing is mostly the agent's; the sentences are yours, and there are few of them. Two in the
ordinary life of a session, four that come up only when their case does.

None of them is a command or a keyword. They are the facts the corpus cannot know — which workshop,
that the last session was cut, that we are closing. Everything else fires because a trigger was
read, which is what keeps this list short.

| Every session | |
| --- | --- |
| Opening | The two lines at the top of this page: the workshop, and the entry point |
| Closing | *"Let's close the session."* The protocol then runs in order — the todo keeps only what is open, what closed leaves for its story or for the atlas, the handoff is written, the lint runs, one commit per repository touched, and you get the list of what is left to push |

| When the case arises | |
| --- | --- |
| Nothing exists yet | *"I have just copied the method here. There is nothing else yet."* — plus the entry point. The agent finds no instance and **offers** to build one |
| The last session was cut before it recorded anything | Say so. The state is then established from the disk, mechanically, and the trace of that session is looked for before its reasons are called lost. The work is not replayed |
| A workshop is to be created | *"Create the workshop Ledger, with the repositories ledger.api and ledger.web."* The installer lays it out, so it matches every other one |
| A repository is to be published | Say so. The private-to-public pass is a procedure rather than a case-by-case call |

Two more are answers rather than sentences: the agent offers the onboarding interview, and offers
to install the runtime the checks need. Both stay offers, because the cost falls on your machine
and on your session.

⚠ **These are rules an agent reads, not mechanisms that fire.** A rule read at the start of a
session loses against a concrete case three hours later, and the method says so about its own. Where
the cost of missing one is real, a workshop owes itself a check that fails as well — and owes itself
to know which of the two it is relying on.

## Where it comes from

It was not designed and then applied. It was extracted, over months of sessions, from the
day-to-day development of several projects of different natures — worked out across them
rather than for any one of them. Every rule in it exists because something went wrong
first.

Some of those failures are quoted in the files, with their numbers, because a rule is
easier to respect when the cost of ignoring it is visible: a tracking lint that had become
two divergent forks and was missing from a third workshop; seven per-tool trigger files, of
which not one ever reached the agent; a framing folder found holding four repositories,
three of them with no framing at all.

The method is applied to its own development. Its framing is written under its own rules,
and `sample/` shows what that looks like.

## Who it is for

One developer, working with AI agents, on more than one thing at a time. It is not a
project-management framework: no estimation, no board, no ceremony, and nothing to fill in
for anyone else's benefit.

## The unit of work

A **workshop** is a unit of work that owns its framing. It may hold one product spread over
several repositories, or a single independent library. Each workshop carries a `_workspace/`
folder holding its atlas, its todo and its handoff. This repository defines what workshops
are, and how one developer and their agents work inside them.

## The layout, in full

Everything below sits under whatever folder you keep your work in. That root has no
meaning of its own — the method never reads anything from it.

The root is the only position the method depends on: `_workshop/` and every workshop are its
direct children, and that is what lets any of them find the others.

```text
projects/                        THE ROOT — you choose it. Not a repository, nothing read from it
│
├── _workshop/                   THE META LEVEL — one per machine, shared by every workshop.
│   │                            This repository, copied, with instance/ filled in.
│   │                            Private in full. Call it what you like; nothing reads the name.
│   ├── method/                    the rules — one entry point, the rest behind triggers
│   ├── sample/                    a worked example of a framing
│   └── instance/                  YOURS — profile, transverse conventions, notebooks.
│                                  This repository ships the folder empty; you fill it.
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
│       ├── done/                    what is finished — one file per [TAG]
│       ├── _planning/               the long form, at any stage — status in each header
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
  workshops.
- **The meta level is the folder holding `method/organization.md` and `instance/`.** That
  pair is its whole test, and nothing depends on what it is called — but it does depend on where
  it sits: **directly inside the root, beside the workshops**, which is what makes it findable
  from any of them. It is **not** a workshop: it holds no framing, because there is nothing to
  frame — you are reading the method there, not writing it.
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
| `sample/` | A worked example of a framing, naming no product and no person. |
| `instance/` | Empty on purpose. The slot you fill in your own copy — see below. |

### Reading `sample/`

It is the framing of `Ledger`, the workshop drawn in the layout above: a double-entry ledger
with an API and a web client, held in one workshop because they serve one framing. `Ledger` is
invented, and every figure in it is illustrative.

| | What it is there to show |
| --- | --- |
| `atlas.md` | Decision level, not implementation level — and a guard-rail that outlived the work that produced it |
| `todo.md` | The grammar, the four marks, and an item that **cites** the document carrying its reasoning instead of duplicating it |
| `memories/handoff.md` | Volatile only. Note what the last entry does *not* say: work moved, and the entry stops there |
| `done/EXPORT.md` | A closed piece of work keeps its story — what was tried, what was rejected — out of both the atlas and the todo |
| `_planning/rounding.md` | The long form, with the status header that says which stage it is at |

Read them in that order and the four tenses separate on their own.

⚠ **It is an example, not a template.** What you copy is `method/templates/`, and the installer
fills it in. Two things follow, and both are deliberate:

- **there is no `lint.toml` in it.** A configuration is something you copy; this folder is
  something you read, and the two must never be confusable — an adopter who copies an example
  inherits someone else's thresholds in silence;
- **there is no readme in it either.** A framing folder carries no loose document beside its
  atlas, and an example that broke the rule it illustrates would teach the wrong half. That is
  why this section is here rather than there.

⚠ And it is never placed next to a real `_workspace/`. Two framings side by side are two
sources of truth, which is the exact drift the method exists to prevent.

## Getting started

**What you need**: an agent that can be pointed at a set of folders and told to read a file.
That is what coding agents do; which one is not the method's business, and § *Entry point* says
why it refuses to have an opinion.

**1. Choose the root, then copy into it.** The root is the folder that will hold all your
workshops — whatever your projects already sit under is usually the right answer. **Download the
archive of the [latest release](https://github.com/SharpPyxis/SharpPyxis.Workshop/releases/latest)**
and unpack it *inside* that root, as `_workshop/` or any name you prefer.

The archive rather than a clone, and it is not a preference: what you unpack has no `.git`, so it
has no remote, and no command you could mistype would send your instance anywhere. § *The half you
write* explains why that boundary matters; the archive is that boundary drawn by structure instead
of by care.

> ⚠ **The position is the one thing that is not negotiable.** The name is not read, the host is
> yours, versioning it is optional — but the copy must sit **directly inside that root, beside
> your workshops**, never inside one. Every resolution starts from a workshop, climbs to the root,
> and looks for the method among its children; anywhere else, it is simply not found, and the
> checks refuse rather than guess. Everything else in this method is deliberately loose. This is
> the one thing it needs.

**2. Open a session on that folder** and say, in your own words:

```text
I have just copied the method here. There is nothing else yet.
Entry point: projects/_workshop/method/organization.md
```

There is no workshop yet and no editor wiring file, and neither is needed. ⚠ The wiring file
later sessions use sits at the corpus **root**, outside every repository — so nothing you copy
or clone could have delivered it, and the first session is opened by hand whatever the method
ships. From the second session on, the gesture at the top of this page applies.

**3. Answer the questions.** The agent reads the map, finds no instance, and offers to build one
with you: your language, your register, how you work. Ten minutes, and it writes the two files
that everything else reads. Say *later* and it carries on without them, telling you so rather
than guessing.

**4. Create your first workshop.** `method/setup/workshop-setup.py`, like every workshop after it.
With none to learn from yet, it reads the corpus root and the framing folder's name off the meta
level instead — and refuses rather than guess, including when it finds it is running from a
working copy of the method rather than a received one.

### The half you write

`instance/` ships **empty**, and it is the one folder you are expected to fill: your profile
and how you want an agent to address you, your transverse technical conventions, your
notebooks. The method never reads its contents — only the `index.md` you put there, which
declares what exists and **when** each file is read. Everything else in your copy is received:
you read `method/`, you do not edit it.

It does not arrive all at once. Step 3 above writes the identity file and the index; the rest of
the corpus follows one file at a time, each written the first time its absence is actually felt.

The rule that decides every borderline case:

> **The method declares slots; the instance fills them.** *That there is a corpus of
> transverse technical conventions, read on demand before writing that kind of code*
> is method. What that corpus says is instance.

⚠ **A copy rather than a clone, and the difference is the whole safety.** Your copy holds your
profile and your conventions; this repository is upstream, and nothing travels back. Updating
is copying a newer `method/` over yours — there is no push, no remote, and therefore no command
that could publish what you wrote. Downloading a release archive is what makes that structural:
there is no remote to remove, because there never was one. A boundary drawn by structure holds against a mistyped
command; one drawn by an entry in a `.gitignore` holds only as long as the entry does.

One thing is deliberately **not** here, and stays that way: the **framing of this repository's
own development**. The method is developed in a workshop like any other — the repository plus
its `_workspace/` — and `_workspace/` is private, here as everywhere. `sample/` is what lets an
example ship without shipping someone's working notes.

⚠ `sample/` must **not** be placed next to an actual `_workspace/` when the method is
adopted — it would become a second source of truth for framing, which is exactly the
drift the method is designed to prevent.

A third destination exists and is not here: reusable **code** and its reference
documentation live in a code repository, versioned with what they document. If it
compiles, it does not belong here.

## Entry point

The method declares **one** path: `method/organization.md`. Everything else is reached
from there, so that adopting the method never means rewriting a dozen hardcoded
locations. The instance is found **beside `method/`, inside your copy**, by the layout the
method declares — not by a path written into it.

That is also why the path above is the same sentence on every machine. It was not, until the
layout in this readme was written from the one machine that develops the method rather than
from the one that reads it — which made a published example path that nobody else could type.

How an agent comes to read that file is tool-specific, changes with tool versions, and
is deliberately **not** part of the method. Naming the path at the start of a session is
the reliable gesture. Measured on the repositories this method came from: seven per-tool
trigger files existed, and not one of them reached the agent.

## Status

Under construction, and in use. Five workshops read `method/organization.md` at the start of
every session, from a copy of this repository laid out exactly as described above.

The published name is settled: `method/` names its function and stands against `sample/`,
while the repository above it carries the belonging.

Both tools have now resolved a second corpus — a separate root, other workshop names, no wiring
to read from — and the four steps above were walked end to end on it, day zero included.

⚠ What has still **not** been exercised: another machine, and a case-sensitive file system. The
layout resolves by structure rather than by hardcoded names, which is what makes the copy above
the whole procedure — but a check that never ran on a second operating system is a hypothesis,
and case is where a path that works on the author's machine loads nothing at all elsewhere.

## Versions and updates

Releases are tagged, and [`CHANGELOG.md`](CHANGELOG.md) travels inside the archive — a copy has no
history to consult, so the file has to be there. `method/VERSION` says which one you hold, and the
installer stamps it into every workshop it creates.

The number answers one question, because it is the only one an update raises here: **can you copy
the new `method/` over yours and carry on?**

| | |
| --- | --- |
| **Patch** | Wording, clarifications. Copy over. |
| **Minor** | New rules, new files. Copy over — your instance and your workshops are untouched. |
| **Major** | Copying is not enough: something of yours changes by hand — a file renamed, an index line now required, a folder moved. The changelog entry carries what to do. |

There is no API here, so the usual compatibility contract has nothing to attach to. What a version
can honestly promise is the cost of taking it, and that is what these three levels measure.

⚠ **Nothing is pushed to you.** Watching *Releases only* on this repository is what tells you a
newer one exists; a copy cannot find out on its own, and pretending otherwise would be the kind of
convenience this method does not offer.

## Contributing

**Issues are open** — corrections, questions and reports are welcome.

**Pull requests are restricted to collaborators.** The rules carry the reasons that hold them, but
the arbitrations behind their exact wording are not published: they live in the framing of this
repository's own development, which is private like every other `_workspace/`. Weighing a change to
the text against them is something only the maintainer can do, and an issue is the way to reach
them.

This is a solo project assisted by an AI agent. Everything that arrives is read; no response time
is promised.

## License

MIT — see [LICENSE](LICENSE).

It redistributes no third-party component, and there is no notice file for that reason: the
reference lint and the installer use the Python standard library alone, with no package, no
virtual environment and no dependency file. That constraint is what keeps *"install Python"* a
non-event for anyone adopting the method, and it is stated in
[`method/lint/CONTRACT.md`](method/lint/CONTRACT.md).
