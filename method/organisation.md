# Organisation — the map

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

⚠ This is the one instruction that is **not** behind a trigger. Everything else in the
method is read when a condition is met; this is read always, first, unconditionally.

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
<workshop>/
  <repository>/       one or more code repositories, each a repository in its own right
  _workspace/         the framing, outside every code repository
    atlas.md          what exists and works
    todo.md           what is open
    memories/         shared between agents, including handoff.md
```

The method itself is distributed as a repository laid out the same way:

```text
<root>/
  <method repository>/   public — method/ and sample/
  instance/              private, sibling — never inside the public tree
  _workspace/            private, sibling — the framing of the method's own development
```

The instance is found **beside** the method repository, in a folder named `instance/`. A
workshop that places it elsewhere declares the path in its own configuration; the method
never hardcodes it.

⚠ Nothing private ever lives inside the published tree, not even ignored. A boundary drawn
by structure holds against a mistyped command; a boundary drawn by a `.gitignore` entry
holds only as long as the entry does — and `git clean -xdf` deletes exactly what is ignored.

## The three framing documents

Each has one tense, and an item lives in exactly one of them.

| | Holds | Changes |
| --- | --- | --- |
| `atlas.md` | What **exists and works**: architecture, inventory, structuring decisions. | Slowly |
| `todo.md` | What is **open**: current work and next steps. Prolongs the atlas, never duplicates it. | Constantly |
| `memories/handoff.md` | What is **volatile**: in progress, blocked, intended next. | Every session |

Two more tenses exist and are covered in `tracking.md`: what is **done** (a delivered
narrative, out of the todo) and what is **not yet scoped** (planning).

> Read `tracking.md` before writing in any of these files, and before closing a session.
> It holds their life cycle, the todo grammar, and the closing protocol.

## Reading order

Before substantial work:

1. `instance/index.md` and the identity file it declares — always, first (§ *Step 0*);
2. this file;
3. identify the workshop concerned by the request;
4. its `_workspace/atlas.md` and `_workspace/todo.md`;
5. the relevant files of `_workspace/memories/`;
6. only then, the code needed for the work asked.

For a trivial or very local request this may be reduced to what is strictly needed — but
never at the expense of step 1, and never by inventing a structure instead of reading one.

⚠ If several workshops are open, choose the target from the request, the cited files, or the
active file. **When in doubt, ask rather than explore.** The open editor and the current
selection are signals of intent; they do not define the perimeter of the work.

## Index of the method, by trigger

Almost nothing here is read unconditionally. Each file states its own trigger in its header.

| File | Read when |
| --- | --- |
| `organisation.md` | Always — this file |
| `tracking.md` | Writing in a framing document, or closing a session |
| `bootstrap.md` | Setting up a workshop, or diagnosing why an agent read nothing |
| `memory.md` | Deciding where a fact should be stored |
| `git.md` | Creating a repository, drawing a versioned / local boundary, preparing a publication |
| `lint/` | Running the checks, or changing their configuration |
| `templates/` | Creating a workshop or an instance |

The instance declares its own files and their triggers, in `instance/index.md`. The method
never reads their contents.

⚠ A file that is in neither index is read by nobody. That is not a hypothesis: two such
files were found in the corpus this method came from — a reference note and the corpus's own
todo — both useful, both invisible.

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

The list of the workspace's folders is given to the agent in its environment context.
**Locating the instance means consulting that list** — not running a file search inside one
repository. The instance may be any of the folders, including the primary one.

If, that check made, the instance is genuinely absent:

- use the local files of the repository at hand;
- **state explicitly** that the standard bootstrap is unavailable;
- do not invent a structure that has not been confirmed.

## Philosophy

- One source of truth per subject.
- The method declares slots; the instance fills them.
- What is read always is a map; everything else is reached by trigger.
- Attention, not volume, is what the reading budget protects.
