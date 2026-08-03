# messages/ — what one workshop leaves for another

This folder ships holding **no message**, and it fills up as you work. It is the only place a
session can leave something for a workshop it is not in, since nothing is ever written into another
workshop's framing.

**One file per target workshop, named exactly as that workshop's folder** — `Ledger.md`,
`TinyParse.md`. The name is the address: a session opening on `Ledger` looks up `Ledger` and finds
a file or finds nothing, which is one listing at the start of a session and nothing more.

## A message is not an item

An item is stored and maintained. A message is delivered, read once, turned into whatever the
receiving workshop actually keeps — a todo item, a line in the atlas, or the decision to do nothing
— and then **deleted**. A file that stays here to be read again has become a second todo, in the
one folder that belongs to nobody.

Three rules follow from that, and `method/tracking.md` § *Work found for another workshop* carries
the reasoning:

- **the receiving session consumes the message** and records its decision in its own framing;
- **a message carries a finding, not an instruction.** What becomes of it belongs to the workshop
  it names;
- **it cites rather than copies.** What was found usually lives somewhere with authority already,
  and nobody maintains a copy meant to be deleted.

⚠ **The address is resolved, never inferred**, and its exact case is part of it. A message
addressed to `ledger` when the folder is `Ledger` is delivered to nobody, and it fails silently on
any file system that tells the two apart. In doubt, ask rather than guess: a sentence against the
whole message.

⚠ This readme is addressed to you rather than to an agent, and nothing reads it. Delete it or keep
it; the folder works either way.
