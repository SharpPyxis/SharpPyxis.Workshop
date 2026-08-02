# Tracking — life cycle of the framing documents

> **Read when** writing in a framing document, or closing a session.
> **Do not read** to answer a question or write code — the map (`organization.md`) already
> says what each document holds.

Four tenses and one format. An item lives in exactly one **tense**; the format is where
anything too long for a line goes, whatever its tense. Most drift in a framing folder is one
document quietly taking on the job of another.

---

## `atlas.md` — what exists and works

- Architecture, inventory, structuring decisions. **Decision level, not implementation
  level** — the code and the commits are authoritative for how.
- Evolves slowly. A closed, significant piece of work earns a concise entry — a few lines,
  not a session report.
- It is the starting point for resuming on solid ground: it must let a reader understand the
  state of the system **without reading the history**.
- It also serves as the index of the workshop: the repositories it frames, and where they
  are hosted.

**Factual and imperative, never a chronicle.** Write what *is* and what *must be*. How it came to
be that way belongs in `done/`, and the factual record is already in the `git log`. Three questions
sort it, and they are mechanical enough to apply without arbitration:

- *what is, or must be?* — it stays, in the imperative;
- *how did we get here?* — it goes. A section narrating a superseded state, the rule that was
  replaced, the exception that fell, reads as live context to the next session and is paid for out
  of the reading budget at every start;
- *is it already written in a document that has authority?* — then the atlas does not repeat it.
  Cite it and move on. A rule living in two places is two sources of truth, and the copy drifts in
  silence. ⚠ Check this one rather than assume it: an atlas measured against its own method corpus
  was two thirds duplication, none of it visible from inside the file.

⚠ **A reason stays when it explains why a rule is counter-intuitive; it goes when it recounts the
incident.** Strip a rule of the reason that makes it survive and a later session judges it
superfluous and skips it — the same failure as a threshold posted without its reason, which gets
raised to silence the lint rather than discussed.

## `todo.md` — what is open

Prolongs the atlas, never duplicates it. A finished item **leaves**: notable ones become a
line in the atlas, minor ones simply disappear. A todo crowded with closed items loses all
its steering value.

Two rules decide where an item goes and how it is written:

- **A guard-rail that must outlive the work it came from belongs in the atlas.** Left in the
  todo, it disappears with its section the day the work ships. And if it does not need to
  outlive that day, it was not a guard-rail but an execution precaution — its place is then
  in the code, as a comment, where someone would go to contradict it.
  **Special case**: the guard-rail of a component **not yet born** stays in the todo until
  that component's reference exists. It migrates on the day of delivery, and is even its
  first content.
- **An item must stand on its own**: either it carries its meaning, or it cites the document
  that does. An allusive reference to a past conversation is neither — legible the same
  evening, opaque three weeks later. Accepted consequence: **pruning a todo can make it
  grow**, so line count is not the measure of a successful pruning pass.

### Grammar

Work is grouped under a `[TAG]` in capitals — a stable key, reused by the delivered
narrative and by commit messages. Each group opens with a `> status:` line saying whether it
is active, on hold, or blocked, and by what.

| Prefix | Means |
| --- | --- |
| ⬜ | To do |
| ⚠ | A guard-rail, or a fact that must be read before acting |
| ❓ | An open decision, deliberately not guessed |
| 💡 | An idea, not committed to |
| ✅ | Done — and therefore on its way out of this file |

⚠ ✅ is a transition, not a resting state. An item that stays checked in the todo is an item
nobody moved to the atlas or the delivered narrative.

## `done/` — what is finished

A closed piece of work leaves the todo, but its story is often worth keeping: why it was done
that way, what was tried, what was rejected. That belongs in `done/<TAG>.md` — one file per
`[TAG]` — outside both the atlas and the todo.

The atlas keeps the consolidated result in a few lines; the narrative keeps the account. The
todo keeps neither.

## `_planning/` — the long form, at any stage

Not a tense: a **format**. A subject whose reasoning does not fit on a line gets a document of
its own, and it may enter before anything is decided, stay through the work, and leave only
when it has shrunk to a few lines of atlas.

What supplies the tense is the mandatory `> status:` header on each document — still valid,
superseded, pending, under active development. That is what lets a later pivot be assessed
document by document rather than wholesale, and it is why the header is not a convenience:
without it, the folder holds documents at four different stages and says so nowhere.

⚠ **A todo item citing a planning document is the normal case, not a violation of "one item,
one tense".** It is the self-sufficiency rule doing its job: an item either carries its
meaning or cites the document that does — and `_planning/` is where that cited document
lives. The two are complementary; only *duplication* between them is drift.

⚠ **No loose `.md` at the root of a framing folder.** A scoping document sitting beside the
atlas is read by nobody and contradicts it in silence. Either it is a planning document, and
it goes in `_planning/` with a status header, or it is not, and its content belongs in one of
the tensed documents. The lint enforces this.

> The leading underscore is the same one everywhere: it marks a folder that holds **structure**
> rather than content, and sorts it above what sits beside it. `_workspace/` and `_planning/`
> read that way at two different levels, and `_workshop/` is the same habit applied to the meta
> level — with the difference that nothing reads *that* name, so it is a convention of the eye
> alone.
>
> ⚠ This note replaced one claiming `_planning/` was the odd one out — a sorting habit set
> against `_workspace/`'s supposed meaning. The distinction did not exist, and the note was read
> exactly as its wording invited: as a sign the folder had been named carelessly.

## `memories/handoff.md` — what is volatile

- Carries **short-lived context** between two close sessions: what was in progress, where it
  is stuck, what was intended next.
- Must **not** become a historical journal. That job is already covered — the atlas holds the
  consolidated state, the todo the next steps, and the `git log` the factual record of what
  changed.
- **One entry per session.** Enriching the current entry as the session goes is correct;
  opening a second one for the same session is not.
- ⚠ **It may state that work has moved; it may not say where the session goes.** "The method is
  now developed in another workshop" is a fact, and belongs here. "That is where the follow-up
  is steered, not here" is an instruction — and the next agent will obey it, after the map and
  about the case at hand, over any rule that says otherwise. A handover records the fact and
  stops there. This is the single most likely sentence to survive a migration and mislead
  afterwards, because it was true the day it was written. There is a moment when it gets
  written, and it is worth knowing: **when one workshop gives birth to another.** Check the
  parent's handoff that day, not months later when a session has already followed it.
- **Keep the recent sessions only** — of the order of three to five — and archive the rest in
  a companion file, consulted on explicit request and never re-read at the start of a
  session.

A file that grows indefinitely damages context uptake, since its volume is re-read at every
resumption. Pruning it is ordinary maintenance, not a chore.

## Sizes

Thresholds are declared **per workshop**, because a workshop with eighteen open subjects and
one with three do not have the same natural floor. Document the **formula**, not a number:
a todo's floor is roughly *number of open subjects × lines per subject + header*. A threshold
posted at creation time, before the workshop has any content, is guesswork that will be
either ignored or wrong.

## Gestures a workshop declares

Some workshops carry an operation that has to happen when something is touched: a folder that must
be mirrored, an index regenerated, a file rebuilt when its source changes. The method knows nothing
about any of them, and must not — but it declares where they are written and **when they fire**.

A workshop declares them in its atlas, one line each: **the trigger, the gesture, and the reason
that holds it.** The trigger is a condition, most often a path that was touched — not a moment in
the session.

⚠ **Do not fold them into the closing checklist by default.** § *Closing a session* is one trigger
among others, and it is the wrong one for anything whose value decays: a gesture postponed to the
close is the gesture a cut session skips, and it leaves the corpus inconsistent for everyone who
opens a session meanwhile. Ask what it costs between the moment the gesture becomes due and the
close. If the answer is anything but nothing, the trigger is the action, not the end.

⚠ **A declared gesture is not a guaranteed one.** It is read at the start of a session and comes
due hours later, which is the contest the concrete case wins. Where the cost of missing it is real,
the workshop owes itself a mechanism too — a hook, a check that fails — and says which, so a later
session knows whether it is relying on a rule or on a machine.

## Closing a session

In order:

1. **Record the work** in the framing documents: the todo carries only what is open — the
   delivered narrative leaves for its own file, durable decisions go to the atlas or the
   documentation.
2. **Write the session's handoff entry** — volatile only: what was done in brief with
   pointers, what is in progress, blocked, or next. Reference the commits; do not paraphrase
   them. Then prune the handoff per the workshop's rule.
3. **Update the atlas** if notable work closed; refresh the header dates of the files
   touched.
4. **Run the workshop's lint**; fix every FAIL before committing.
5. **Commit each repository touched**, then list what is left to push.

⚠ If a workshop's atlas defines a more precise closing checklist, **it prevails** — it adds
the local specifics: tooling, sites, scripts. What belongs there is what is genuinely due *at the
close*; anything due earlier is declared under § *Gestures a workshop declares*.
