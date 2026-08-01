# Ledger — todo

> What is open, only. A finished item leaves: the notable ones become a line in `atlas.md`,
> the minor ones simply disappear. An illustration; the repository readme says what it shows.
> Last updated: 2026-06-14

---

## [ROUNDING] Rounding is decided once, and in one place

> status: active — blocked on nothing; the reasoning is written and the arbitration is open

- ⚠ **Rounding is not a display concern.** It was treated as one for a month, and each screen
  ended up rounding on its own — which is how a total stopped matching the sum of its lines.
  Whatever is decided, the rule is applied where the amount is produced, once
- ⬜ Decide between the two candidates and write the choice into `atlas.md`. The comparison,
  the cases each one gets wrong, and the two that a naive reading gets backwards are in
  `_planning/rounding.md` — this item deliberately does not repeat them
- ❓ Whether a rounding difference is recorded as its own entry. It is what an accountant would
  expect and it makes every total explainable; it also puts entries in the ledger that no user
  ever made. Not guessed

## [EXPORT] The export format, after the first external consumer

> status: on hold — the format is delivered; what is open is the second consumer, who does not
> exist yet

Delivered on 2026-05-30. The story — what was tried, what was rejected, and why the format is
not negotiated per client — is in `done/EXPORT.md`.

- ⬜ Ask the next consumer for a sample of what they expect **before** promising anything. The
  first one was accommodated after the fact, and two columns exist today only because of it
- 💡 A dry-run mode that produces the file without recording that the export happened. Cheap,
  and it would have caught the duplicate-run defect before a client did. Not committed

## [ACCOUNTS] Closing an account that still has a balance

> status: blocked — on the arbitration in `[OPEN]`, and nothing else

- ⬜ Refuse the closure, or accept it and carry the balance forward. The code is ready for both
  and the difference is one branch; what is missing is the decision
- ⚠ Do not add a third state. An account that is "closing" would have to be handled by every
  report, every export and every screen, and each of them would get it wrong once

## [OPEN] Decisions deliberately not guessed

> status: on hold — these are the owner's calls

- ❓ What closing an account with a non-zero balance does (`[ACCOUNTS]`). It is a rule of the
  domain, not a technical trade-off: whichever branch is written, someone will be told their
  money moved without asking
- ❓ Whether the ledger is ever multi-currency. Answering *no* today costs nothing and removes a
  column from four tables; answering *yes* later costs a migration. The question is which of
  those is the honest bet
