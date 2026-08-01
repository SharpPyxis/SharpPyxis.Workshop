# Rounding — the two candidates, and what each gets wrong

> Status: under active development — `[ROUNDING]`. Written 2026-06-14; the decision is not
> taken. An illustration; the repository readme says what it shows.

The todo carries the item and the arbitration; this document carries the reasoning, because it
does not fit on a line and because repeating it in both would make two versions of it.

## Where rounding happens at all

Amounts are integers of the minor unit (`atlas.md` § *Money is an integer*), so nothing rounds
until a value is **divided** — splitting a charge across accounts, applying a rate, prorating a
period. That is the whole surface, and it is smaller than it looked: three call sites.

## Candidate A — round each part, give the remainder to the last

Split 100 across 3: `33, 33, 34`. Simple, and the parts always sum to the whole.

What it gets wrong: the last account is systematically favoured. Over a year of monthly
splits it is not noise, it is a drift with a name — and the name is on the account statement of
whoever happens to be last in the sort order.

## Candidate B — largest-remainder

Distribute the floor, then hand the leftover units to the parts with the largest remainders.
Split 100 across 3 gives the same `33, 33, 34`, but *which* part gets the 34 depends on the
amounts rather than on the order.

What it gets wrong: it needs a tie-break, and a tie-break is a rule someone has to be able to
explain to a person reading their statement. "The largest remainder, and on a tie the lowest
account number" is explainable. "Whatever the sort returned" is not, and that is what an
implementation does when nobody decides.

## The third one, found while writing this

Rounding at display time, and letting the stored parts stay exact — attractive, and worse than
both. Two screens showing the same split would each round independently, so a total would stop
matching the sum of its lines, which is the defect `[ROUNDING]` exists to close. It is recorded
here precisely because it reads well: it will be proposed again.

⚠ Whichever is chosen, the rule applies **where the amount is produced**, once. Treating
rounding as a display concern is what produced the current state, and it took a month to see.
