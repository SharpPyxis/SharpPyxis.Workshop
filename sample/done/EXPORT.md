# [EXPORT] — the export format

> Delivered 2026-05-30. The consolidated result is four lines in `atlas.md`; what stays open —
> the second consumer — is in `todo.md`. An illustration; the repository readme says what it shows.

## What the work was

One external tool needed the entries of a period as a file. The question looked like a choice
of format and was not: an export is consumed by software nobody here controls, so whatever
ships becomes a contract on the day it is first read.

## What was tried, and what was rejected

**Negotiating the format with each consumer** — rejected after two days of trying it. It works
for the first consumer and produces a variant per consumer thereafter, each with its own
defects, none of them tested. The cost is invisible at one consumer and unbounded at four.

**Letting the consumer choose the columns** — rejected for the same reason wearing a different
hat. A per-request column list is a format per request; the support burden simply moves from
the file to the parameters.

**A fixed order, appended to, versioned in the first line** — kept. It costs one line of file
and makes every past export readable by a reader that knows its version.

⚠ The argument that settled it was not elegance: a column that moves breaks a spreadsheet on
someone else's machine, silently, months later, and the breakage is reported as *"your figures
are wrong"* rather than as a format change. Nothing in a test suite here catches that.

## What it cost, and what it caught

Two columns exist only because the first consumer was accommodated after the fact — the item in
`todo.md` about asking the *next* one first is written from that.

And a defect found the day before delivery, by a client rather than by a test: running the
export twice recorded two exports and produced two files with the same version line. The
duplicate-run guard came out of that, and so did the dry-run idea still sitting unclaimed in
the todo.
