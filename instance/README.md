# instance/ — the half you write

This folder ships **empty**. In your copy of this repository it holds your own corpus, and the
method reads it from step 0 of every session.

> **The method declares slots; the instance fills them.** *That there is a corpus of transverse
> technical conventions, read on demand before writing that kind of code* is method. What that
> corpus says is instance.

## You do not have to write the first one alone

Nothing works before this folder has an `index.md` and the identity file it declares — so the
first session that finds them missing **offers to build them with you**: a handful of questions
about your language, your register and how you work, and it writes both. Say yes, or say later
and it carries on without them, telling you so rather than guessing.

It offers and waits. A session you opened to do something else is not taken over by this.

## What goes here

| | |
| --- | --- |
| `index.md` | **The only file the method reads in this folder.** It declares what exists here and, for each file, *when* it is read. |
| An identity file | Who you are and how you want to be addressed — the language to answer in, the register, whether you work alone. `organization.md` § *Step 0* has it read before an agent writes a single line of prose, acknowledgement included. `index.md` names it; the method does not. |
| Your technical conventions | One file per **situation of work**, not per shelf: writing C#, designing a schema, writing an interface. Each declares its own trigger. |
| Your notebooks | Backlogs, dated observations, anything transverse to every workshop and belonging to none. |

## Writing a line of the index

The index answers one question, and it is never *"what is this file about?"* — it is **"do I
need this, now, for what I am about to do?"** So a line describes a **situation**, not a subject,
and it has to be decidable **before** the file is opened.

| | |
| --- | --- |
| ✗ | `sql-conventions.md` — *Database conventions* |
| ✓ | `data.modeling.md` — *Designing or changing a schema, whatever the engine* |
| ✓ | `data.postgresql.md` — *Writing PostgreSQL: DDL, a migration, a query* |

The first is a shelf. Someone about to write a `select` cannot tell whether it is meant for
them, so they either read all of it for nothing or skip something they needed.

Two habits make the difference, and both are cheap:

- **say what it excludes.** The negative half is what saves the reading, because it is what
  stops an agent reading defensively — *"do not read for a pure documentation, C# or frontend
  session: it adds nothing there and costs context"*;
- **one file, one trigger.** Two subjects always read together are one file; one subject read in
  two distinct situations is two files. It is the only rule that reliably tells you where to
  cut, and it is what keeps this index a list of situations rather than a list of shelves.

⚠ The examples above illustrate the *shape*. What your corpus holds, and what its files are
called, is yours — the method declares the slot and never its content. The full reasoning, with
the failure modes worth knowing before you cut, is in the method's `corpus.md`.

## The two rules that keep it usable

- ⚠ **A file that `index.md` does not name is read by nobody.** Not "harder to find" —
  unreachable. Adding a file and declaring it are one gesture, or the file does not exist.
  Observed on the corpus this method came from: two genuinely useful files lived outside every
  index, invisible for months.
- ⚠ **One file, one trigger.** Two subjects always read together are one file; one subject read
  in two distinct situations is two files. That is what keeps the index a list of *situations*
  rather than a list of shelves — and what keeps a session from paying for conventions it will
  not use.

## Nothing here travels back

This folder is filled in a copy, and a copy is downstream. Updating the method means copying a
newer `method/` over yours — **never** this folder, which is the one thing an update must leave
alone. There is no push and no remote toward the published repository, so no command can send
what you wrote here anywhere.

⚠ This readme is the exception to the index rule above, and the only one: it is addressed to
you, on the day you open the folder, and it is not part of what an agent reads. Delete it once
your `index.md` exists, or keep it — nothing depends on it either way.
