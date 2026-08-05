# Corpus — writing a trigger, and cutting a set of files by it

> **Read when** adding a file to a corpus read by trigger, or splitting, merging or renaming
> one. The instance is the usual case; this method's own files are the other.
> **Do not read** to *use* such a corpus — its index already says when each file is read.

---

## A trigger is a situation, not a subject

A subject is a shelf: *SQL*, *C#*, *the frontend*. A situation is a moment in a task: *writing
a migration*, *designing a schema*, *laying out a screen*. Shelves feel tidier and are the
reason a corpus stops working, because the question an index has to answer is never "what is
this about" — it is **"do I need this, now, for what I am about to do?"**

The test is mechanical: **the trigger must be decidable before the file is opened.** If you have
to read the file to know whether it applied, it has no trigger, only a title.

```text
✗  sql-conventions.md      Database conventions
✓  data.modeling.md        Designing or changing a schema, whatever the engine
✓  data.postgresql.md      Writing PostgreSQL — DDL, a migration, a query
```

The first line cannot be acted on. Someone about to write a `select` does not know whether
"database conventions" is meant for them, so they either read 30 kB they did not need or skip
something they did.

## Say what it excludes

The negative half is what actually saves the budget, because it is what stops the hedging. A
trigger with no *do not read* is read defensively, which is the same as being read always.

```text
Read when: writing or changing a web interface — components, layout, styles.
Do not read for a pure C#, SQL, documentation or organisation session: it adds
nothing there and costs context.
```

## One file, one trigger

**Two subjects always read together are one file. One subject read in two distinct situations
is two files.** That rule is what keeps an index a list of situations rather than a list of
shelves, and it is the only one that reliably tells you where to cut.

Applied to a real split: *designing a schema* and *writing the DDL for a given engine* are two
moments — the first is engine-independent and happens once, the second happens every time and
differs per engine. Two files. Whereas *responsive layout* and *container fluidity* are never
needed apart: one file.

⚠ **Do not file by conceptual generality.** A rule may be perfectly portable — independent of
the language, the engine, the framework — and still not deserve a file, because nobody ever sits
down to "write something portable". A file no situation opens is a dead file, however true its
contents. A portable rule earns a file only when its own, **wider** trigger can be named out
loud: *"writing application code, in any language"* is such a trigger; *"patterns"* is not.

## ⚠ A section's trigger can be wider than its file's

This is the failure that no index catches and no proofreading finds, because the file looks
perfectly coherent from the inside.

Measured on the corpus this method came from. A file triggered by *writing C#* held:

- a section on **monetary rounding** — which binds the SQL that computes the same totals;
- a section on **wording shown to end users** — which binds every interface, in any language.

Both were correct, indexed, and reachable. Both were unreachable from the sessions that needed
them most, because they sat behind a trigger that was not theirs. **When adding a section, read
its own trigger, not its file's.** If they differ, the section is in the wrong file — or is a
file.

## The name says *what*, the index says *when*

Flat, prefixed names; folders only once a prefix passes four or five files. Nobody navigates the
tree — the index is what is read — so the sort order on disk serves the human eye alone, and the
1:1 correspondence between index and files is what stops a file becoming invisible again.

```text
data.modeling.md   data.postgresql.md   data.sqlserver.md
code.patterns.md   code.csharp.md       code.persistence.md
ui.responsive.md   ui.wording.md
```

⚠ These are an illustration of the shape, not a corpus to reproduce. The method declares the
slot; what fills it, and what it is called, is the instance's.

## ⚠ Splitting a corpus rewrites every citation

`organization.md` § *Cite by identity* protects against a corpus that **moves**. It does not
protect against one that is **cut**: in a flat corpus the file name *is* the identity, so every
cross-reference in every file breaks at once — and so does anything outside the corpus that
named a file, which is the part nobody remembers. Count that cost before starting, and check
what cites the corpus from outside before renaming anything inside it.

⚠ **Including the citations that name no file at all.** A cut turns *intra*-file references into
cross-file ones, and no search for names can find them, because they carry none: *"see
§ Nullability"*, written inside an example that leaves for another file; *"skip § Book theme"*, in a
header whose section becomes a file of its own. Both measured on a real cut, of twelve files into
nineteen, and both would have shipped. Read the **pointers**, not only the names.

## A first index, and what it looks like later

Day one, after `onboarding.md`, an index has one line, and that is a correct index:

```markdown
## Read always, and first

| File         | Contents                                          |
| ------------ | ------------------------------------------------- |
| `profile.md` | Identity, communication rules, working principles |

## Technical conventions — read by trigger

*(nothing yet — a file is written the first time its absence is felt)*
```

Later it is the same table, longer. Every addition declares its trigger **in the same gesture**
as the file itself.

## The index is the last gesture, and it is not optional

A new file, a split or a rename is **not finished until the index of its own corpus says so**, in
the same session. Not the next one: an index updated later is an index updated never, and the file
it was meant to declare is already invisible.

Which index is its corpus's own, and nothing else decides it:

- the **instance** declares its files in the index that `organization.md` § *Step 0* names. The
  instance owns that location; the method declares the slot and never hardcodes the path;
- the **method** declares its own in `organization.md` § *Index of the method, by trigger*.

⚠ **Both directions fail, and both have been observed.** A file no index names is read by nobody —
two genuinely useful files lived outside every index for months, one of them a todo. An index line
no file answers is the same failure mirrored, and harder to see from the other side: a folder was
declared in the method's index and did not exist.

## Every file restates its own trigger

The index says when each file is read, and each file says it again in its own header. The two are
held in step by the check above, and four things pay for the repetition:

- **the header is the authority; the index line is a copy.** A copy drifts, and this one drifts in
  silence — nothing about an index line shows that the file it points at has since changed what it
  is for;
- **the check reads both**, which is what makes the copy safe instead of a second source of truth;
- **a file opened for the wrong reason says so on its first lines.** An agent that arrived by a bad
  inference meets the trigger it does not satisfy, and the *do not read* half tells it what not to
  apply — reached at the only moment it can still prevent something;
- **whoever opens the file to change it reads who it is meant to serve** before changing it. That
  one assumes no agent, no index and no check, which is why it is the reason to keep if the others
  ever stop holding.

⚠ **The header saves no context.** Reading a file is atomic: its content is paid for the moment the
file is opened, header included. What saves the budget is the index, read in place of the files —
so a header earns its place by what it prevents, never by what it spares.
