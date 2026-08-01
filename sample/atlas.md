# Ledger — atlas

> Consolidated state. Read at the start of a session on this workshop; what is open lives in
> `todo.md`. An illustration; the repository readme says what it shows.
> Last updated: 2026-06-14

---

## What Ledger is

A double-entry ledger. Every movement is two entries summing to zero, and a balance is never
stored: it is the sum of the entries up to a date.

Two repositories, one workshop. `ledger.api` owns the rules, `ledger.web` shows them — and a
change to what a balance *means* touches both. It is that shared framing, not the shared
language, that makes them one workshop.

| Repository | Holds |
| --- | --- |
| `ledger.api` | The entries, the rules, the exports |
| `ledger.web` | The client. Displays; decides nothing |

## Money is an integer of the currency's minor unit (settled 2026-03-02)

Amounts are stored as integers of the minor unit — cents for the euro — never as a decimal
type and never as a float.

The reason is an incident rather than a preference. A monthly report came out 0.03 € short
over 12 000 lines, and the gap could not be attributed to any one of them: floating point had
rounded every line correctly and the total wrongly. The error was invisible per line, which is
what made it expensive — it was found by a reader who added a column by hand.

⚠ The guard-rail outlives the report that produced it, so it lives here rather than in the
todo: **anything crossing a boundary carries its minor-unit integer and its currency code
together.** An amount without its currency has been read as euros twice, once in an export
consumed by an external tool.

## The client computes nothing (settled 2026-04-19)

`ledger.web` displays balances; it never derives one. A balance shown next to a balance
computed differently is two answers to one question, and the user is left to arbitrate.

This was not free: three screens gained a round trip they did not have. It was accepted because
the alternative had already cost more — a summary page and a detail page had disagreed for two
weeks about the same account, each correct under its own rule.

## Exports are a published surface (settled 2026-05-30, narrative in `done/EXPORT.md`)

An export is consumed by tools nobody here controls, so its format is a contract: a column that
moves breaks a spreadsheet on someone else's machine, silently and months later.

Consequences: the column order is fixed and versioned, a new column is only ever appended, and
the file carries its format version in the first line. The narrative holds what was tried and
what was rejected — in particular why the format is not negotiated per client.

## The framing is private, and the repositories are not

`_workspace/` is not published and is not inside either repository. It carries decisions,
session context and names; the repositories carry code and its reference documentation,
versioned with what they document.

⚠ Reference documentation for reusable code belongs **with the code**, not here. Twice, a
description of an API has been written into the framing and drifted away from the endpoint it
described, because the two were updated by different gestures.
