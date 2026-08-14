# Organization — the map

The single entry point of the method. Everything else is reached from here.

This file is read at the start of **every** session, so its concision is a functional
property, not a matter of taste. What is read rarely lives in another file, behind a
trigger.

---

## Step 0 — read the instance, before producing anything

> Read `instance/index.md` and the identity file it declares. **Do this before writing a
> single line of prose**, including an acknowledgement of the request.

The instance declares who is being worked with and how to address them — the language to
answer in, the register, whether the person works alone or in a team. These are not
preferences to apply once noticed: they shape the first sentence, so they cannot be read
after it.

This method declares the slot and its timing. It does not declare the content: a published
method that hardcoded a language or a name would be wrong everywhere it was not written.

⚠ This and the section that follows are the only instructions **not** behind a trigger.
Everything else in the method is read when a condition is met; these two are read always,
first, unconditionally.

**If there is no instance, or it holds no index** — the case on a fresh copy, since the
repository ships `instance/` empty — read `onboarding.md`. It turns the absence into a short
interview producing a first identity file and the index that declares it.

⚠ It **offers**; it does not start. The absence is found in the first seconds of a session
opened to do something else, and nothing justifies taking that session over. State it in one
sentence, offer, and wait — then either write the instance or carry on without it, saying
plainly that you are working without the identity rules. This is the same discipline as
offering to install a missing runtime, and for the same reason: the cost falls on someone
else's machine.

## Precedence — what you already remember does not decide here

If you carry a memory of your own — a private store, a project note, a fact recalled from an
earlier session — **the corpus overrides it.** Where the two disagree, what you remembered is an
observation to re-verify against the files, never a fact to apply. And write nothing durable into
it: such a store is keyed by the session's root rather than by workshop, so what you put there
working on one is recalled working on another.

⚠ **This cannot live behind a trigger of its own.** A trigger fires when a question is asked, and
a memory that answers first is exactly what stops the question from being asked — so the cost is
not the duplicate, it is the file you never open. Same argument as § *Step 0*, against a different
failure: that one protects the order of reading, this one a source that removes the reading.

`memory.md` has the rest.

## Vocabulary

| Term | Meaning |
| --- | --- |
| **workshop** | A unit of work that owns its framing. It may hold one product across several repositories, or a single independent library. |
| **`_workspace/`** | The folder holding a workshop's framing documents. One per workshop, outside every code repository. |
| **project** | Keeps its ordinary technical meaning — a `.csproj`, an npm package. Do not confuse it with a workshop. |
| **instance** | One owner's profile, transverse conventions and notebooks. Private, and never part of this method. |

> **Two sets with independent framing are two workshops.** A workshop may hold several
> repositories as long as they serve **one** framing.

That rule replaced a mechanism that declined framing documents by filename suffix inside a
single workspace. It held at two projects and broke at four: one family was found holding
four repositories, of which three had no framing at all and one carried 85% of the folder.
It was never a special case — it was four workshops disguised as one.

⚠ Legacy accepted: the folder is still called `_workspace`, which no longer matches the
vocabulary. Renaming it would touch every path of every lint, every document and every
workshop — and a half-rename is worse than none.

## Layout

```text
<root>/                          ROOT      no meaning, not a repository, nothing read from it
├── _workshop/                   META      one per machine, shared by all. Private in full.
│   ├── method/                            the rules — one entry point, the rest by trigger
│   ├── sample/                            a worked example of a framing
│   └── instance/                          yours: identity, conventions, notebooks
├── <WorkshopName>/              WORKSHOP  owns exactly one framing
│   ├── <repo-a>/                REPO      code — src/, tests/, docs/, per its stack
│   ├── <repo-b>/                REPO      code — same workshop, same framing
│   └── _workspace/              FRAMING   a repository of its own, outside the code ones
│       ├── atlas.md                       what exists and works
│       ├── todo.md                        what is open
│       ├── done/                          what is finished — one file per [TAG]
│       ├── _planning/                     the long form, at any stage — status in each header
│       └── memories/handoff.md            what is volatile — one entry per session
└── <OtherWorkshop>/             WORKSHOP  a single library is still a workshop
    ├── <repo>/                  REPO
    └── _workspace/              FRAMING
```

### The meta level is a copy, and it is yours

`_workshop/` is the method **as you received it**, with `instance/` filled in. You get it by
copying the published repository, which ships `instance/` empty for exactly that purpose, and
from then on it is a private folder of your own — versioned wherever you keep private things,
or not at all.

⚠ **Its position is the one thing that is not free.** The name is not read, the host is yours,
versioning it is optional — but it sits **directly inside the root, beside the workshops**, never
within one and never elsewhere on the disk. Every resolution in this method starts from a
workshop's framing folder, climbs to the root, and looks for the meta level among its children.
Placed anywhere else it is not found, and the checks refuse rather than guess.

Two consequences follow, and both matter more than they look:

- **it is private in full**, not selectively. Nothing has to be filtered out of it, because
  nothing in it is meant to travel back. What is published is the repository it came from;
- **it is not a workshop.** It holds no framing, because there is nothing to frame: you are
  not developing the method, you are reading it. It is the one folder in this layout that
  holds neither code nor a `_workspace/`.

⚠ Updating it is a copy, not a merge — the published repository is upstream, and nothing flows
back. A method whose upstream is a repository you cannot write to is a boundary held by
permissions rather than by care, which is the only kind that survives a mistyped command.

### Resolving what you are looking at

Apply in order. Each test is mechanical — do not infer a level from a folder's name, its
depth, or how important it looks.

1. **Contains a `_workspace/`** → it is a **workshop**. This is the only test. A workshop is
   never itself a repository.
2. **Is a repository and contains no `_workspace/`** → it is **code**, and it belongs to the
   workshop that contains it. Its internal skeleton is whatever its stack expects, and the
   method says nothing about it.
3. **Is named `_workspace/`** → it is the **framing** of the workshop that contains it. It is
   **a repository of its own**, sitting outside every code repository: the method leans on its
   `git log` for the factual record, which is what lets the handoff stay short. Keep it
   private (§ *Never*, below); `git.md` has the rest.
4. **Holds `method/organization.md` and `instance/`** → it is the **meta level**. That pair is
   the whole test, and nothing depends on what the folder is called.
5. **Contains workshops and nothing else of interest** → it is the **root**. Read nothing
   from it.

Consequences worth stating, because each has been got wrong:

- several repositories may share one workshop, **as long as they serve one framing**. Two
  sets with independent framing are two workshops;
- the instance is found **inside the meta level**, beside `method/`, in a folder named
  `instance/`. A workshop that places it elsewhere declares the path in its own configuration;
  the method never hardcodes it;
- ⚠ **the workshop where the method is developed is a workshop like any other** — the method's
  repository plus its `_workspace/`, sitting beside the other workshops. It is *not* the meta
  level, and the two must not be confused: the meta level is the copy every workshop reads
  from, and it stays a copy even on the machine where the method is written. Stated because it
  was got wrong here first, and in five places at once: the layout was described from the one
  machine that develops the method, which made the description true nowhere else.

### Never

- **Never publish a `_workspace/`**, including the method's own. Framing documents carry
  names, decisions and session context belonging to their owner. The published example is
  `sample/`, written for that purpose.
- **Never place `sample/` next to a real `_workspace/`.** Two framings side by side are two
  sources of truth — the exact drift this method exists to prevent.
- **Never put private content inside a published tree, not even ignored.** A boundary drawn
  by structure holds against a mistyped command; a `.gitignore` entry holds only as long as
  the entry does, and `git clean -xdf` deletes exactly what is ignored.
  ⚠ The published repository ships an **empty** `instance/`, and that is not an exception to
  this: what ships is the slot, and it is filled only in the copy, which is nobody's published
  tree. The distinction is worth holding on to — a slot travelling outward is a rule waiting to
  be broken, while a slot filled downstream cannot travel at all.
- **Never write framing into a code repository**, and never write code doctrine into the
  framing. Reusable code and its reference documentation are versioned with what they
  document.

## The three framing documents

Each has one tense, and an item lives in exactly one of them.

| | Holds | Changes |
| --- | --- | --- |
| `atlas.md` | What **exists and works**: architecture, inventory, structuring decisions. | Slowly |
| `todo.md` | What is **open**: current work and next steps. Prolongs the atlas, never duplicates it. | Constantly |
| `memories/handoff.md` | What is **volatile**: in progress, blocked, intended next. | Every session |

A fourth tense and one format are covered in `tracking.md`: what is **finished** (`done/`, one
narrative per tag, out of the todo), and `_planning/` — the **long form**, where a subject
whose reasoning does not fit on a line lives at any stage of its life, each document carrying
its own status header.

> Read `tracking.md` before writing in any of these files, and before closing a session.
> It holds their life cycle, the todo grammar, and the closing protocol.

## Reading order

Before substantial work. The first three interleave, and that is by design — § *Step 0* sits at
the top of this file so that reading the map in order produces the right sequence:

1. **this file, as far as § *Precedence*** — its two opening sections, the only ones read
   unconditionally;
2. `instance/index.md` and the identity file it declares — before a single line of prose;
3. **the rest of this file**;
4. identify the workshop concerned by the request;
5. **any message addressed to it** — `instance/messages/` holds one file per workshop, named after
   it. Usually there is none: a listing, and nothing more. `tracking.md` § *Work found for another
   workshop* has the rest;
6. its `_workspace/atlas.md` and `_workspace/todo.md`;
7. the relevant files of `_workspace/memories/`;
8. only then, the code needed for the work asked.

⚠ Steps 1 and 3 were once a single entry, placed second — which had this file being read after
a list that lives inside it. Harmless to a reader who already knew, and misleading to the only
audience that matters here: one arriving with nothing.

For a trivial or very local request this may be reduced to what is strictly needed — but
never at the expense of step 1, and never by inventing a structure instead of reading one.

⚠ If several workshops are open, choose the target from the request, the cited files, or the
active file. **When in doubt, ask rather than explore.** The open editor and the current
selection are signals of intent; they do not define the perimeter of the work.

## Perimeter — the workshop you were asked to work on

The request names a workshop. **That workshop is the perimeter of the session**: its
repositories, its `_workspace/`, plus `method/` and `instance/`. Nothing else is opened
without the developer asking for it.

Three rules, each of them written after it was got wrong:

- **A framing document describes; it does not redirect.** It may point to a reading inside its
  own workshop. It may not move the session to another one. Observed: a handoff said the
  follow-up was being steered elsewhere, and the agent went — obeying a document over the
  request that opened the session. A document is a statement of state; only the developer, the
  method and the instance are addressed to you.
- **An incidental discovery is reported, not pursued.** Finding something wrong outside what
  was asked is useful; investigating it is not. Name it in a sentence or two, say what it would
  take, and carry on with the work asked. When it belongs to another workshop, `tracking.md`
  § *Work found for another workshop* says where the report goes so that it outlives the session.
  Observed: a real defect was found and turned into an
  unrequested audit — which spends the session's attention on a problem the developer may
  already know about, and does so silently, since what falls behind is the work asked for.
- **Reading widely is not working widely.** Reading a workshop's framing is the job.
  Enumerating repositories, grepping across the root, or comparing one workshop with another is
  not — unless that is what was asked.

⚠ None of this restricts curiosity. What is found is worth having; it is **acting on it** that
must stay the developer's call — exactly as ⚠ and ❓ let a todo flag an arbitration instead of
taking it.

⚠ **Expect the first rule to lose on its own, and plan for it.** It is abstract and read early;
the sentence that contradicts it is concrete, read late, and speaks about the case at hand. In
that contest the second wins — not by disobedience, by apparent relevance. Observed the day
after the rule was written: a handoff still said where the follow-up was steered, and it was
followed. **Writing the rule here is necessary and not sufficient. The documents that redirect
have to be corrected, one by one.**

## Index of the method, by trigger

Almost nothing here is read unconditionally. Each file states its own trigger in its header.

<!-- lint:corpus-index -->

| File | Read when |
| --- | --- |
| `organization.md` | Always — this file |
| `onboarding.md` | There is no instance, or it holds no index — fires at most once per machine |
| `corpus.md` | Adding a file to a corpus read by trigger, or splitting or renaming one |
| `tracking.md` | Writing in a framing document, closing a session, or resuming one that was cut |
| `bootstrap.md` | Setting up a workshop, or diagnosing why an agent read nothing |
| `memory.md` | Deciding where a fact should be stored |
| `git.md` | Creating a repository, drawing a versioned / local boundary, preparing a publication |
| `lint/` | Running the checks, or changing their configuration |
| `setup/` | Creating a workshop |
| `templates/` | Changing what a new workshop is created with |

The instance declares its own files and their triggers, in `instance/index.md`. The method
never reads their contents.

⚠ A file that is in neither index is read by nobody. That is not a hypothesis: two such
files were found in the corpus this method came from — a reference note and the corpus's own
todo — both useful, both invisible.

⚠ **Cite by identity, not by location.** A path is where a file sits today; a name is what it
is. The corpus moves — folders are renamed, a workshop is restructured — and everything that
hardcoded a path breaks silently, most painfully in places that had no reason to follow it.
Observed: convention files cited by path from inside code comments and from `.gitignore`
headers, all dangling the day the corpus was reorganised. "The transverse SQL conventions"
would have survived it untouched. Reserve real paths for the two indexes, which are the two
files whose job is to know where things are.

## Commits — read at every commit

Only two rules are frequent enough to live in the map. The rest is in `git.md`.

- **Message language follows the repository's destination.** The `git log` is part of the
  published surface: a repository meant for publication writes its history in the language
  of its audience, and private framing repositories write in the language of their owner.
  The workshop states which is which; the criterion is the destination, not the habit.
- **The scope of a commit stays honest.** If the working tree holds uncommitted work of
  mixed origins — several sessions, several subjects — say so and propose a split, rather
  than packaging everything and hiding the fact.

A commit accompanies, and reflects, the update of the framing documents concerned at the
same moment. The documents and the commit tell the same story, without contradiction — which
is what lets the `git log` carry the factual record, so the handoff no longer has to.

## Robustness and fallback

The set of folders the agent has been given is stated in its environment context, however the
tool expresses it. **Locating the instance means consulting that list** — not running a file
search inside one repository. The instance may be any of them, including the primary one.

If, that check made, the instance is genuinely absent:

- use the local files of the repository at hand;
- **state explicitly** that the standard bootstrap is unavailable;
- do not invent a structure that has not been confirmed.

## Philosophy

- One source of truth per subject.
- The method declares slots; the instance fills them.
- What is read always is a map; everything else is reached by trigger.
- Attention, not volume, is what the reading budget protects.
