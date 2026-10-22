# Nodes — a workshop whose framing is split

> **Read when** the framing you opened holds a `nodes.md`, or its atlas says in its header that
> it is a node of a root.
> **Do not read** in a workshop without nodes: nothing here applies there, and one framing is the
> ordinary case. A workshop without nodes is exactly the workshop the rest of the method describes.

---

## Why a second level, and why only one

A workshop owns one framing. Measured on a family of a dozen packages and one platform, both
shapes that rule allows failed, in opposite ways:

- **one workshop**: the vision of the product and the detail of twelve modules in one set of
  documents — an atlas of 28,000 characters, a todo of 80,000, and holding the context had become
  the work itself;
- **thirteen workshops**: each package framed cleanly and tightly, but the overall view had no
  home, a transverse decision was three commits in three framing repositories, and the only link
  between them was the mailbox — built for the outside.

What the split lost was the **global context**: the view of the whole, available at every session.
A node restores the detail without losing that view. The root is read always; a node is read when
the work calls for it.

**One level, and no more.** A node has no nodes. A real case may ask for a second level one day,
and will be handled then; providing for it now would be deciding ahead on a case nobody has seen,
which this method refuses everywhere else.

## What a node is

A folder **inside the framing**, holding the same documents as the framing itself — `atlas.md`,
`todo.md`, `memories/handoff.md`, `done/`, `_planning/` — for one part of the workshop. Same
tenses, same grammar, same closing protocol, same lint keys: everything `tracking.md` says about a
framing document holds inside a node, file for file.

- **A node is named after its code repository** when it has one, and the framing's tree then
  mirrors the workshop's. A repository without a node is ordinary — it is part of the main
  project; a node without a repository is allowed — a transverse subject that deserves a framing
  and no code.
- **The main project is the root.** What everything else revolves around has no sub-folder: its
  framing is the workshop's own. In a family of packages around a platform, the platform is the
  root and every package is a node — the foundation package included, which underlies everything
  and is the center of nothing.
- **A small part has no node.** It is a paragraph of the root's atlas and a section of its todo.
  It earns a node the day the paragraph stops being enough, and loses it when it closes.
- **One framing repository for the root and its nodes.** A transverse decision is then one commit,
  which is the whole reason the second level exists. `git.md` has the consequences.
- Each node's atlas says in its header that it is a node of this root, so a file opened on its own
  says where it belongs.

## The index: `nodes.md`

The root carries a `nodes.md`, present **only in a workshop that has nodes**, and read at every
session start with the root's atlas, todo and handoff. It is a little more than an index: one
**card** per node, each on the same template, carrying what a session needs in order to decide
whether to open the node — and nothing it would read once inside.

```markdown
## `billing/` — invoices, rates and payments, and nothing else

| | |
| --- | --- |
| Packages | `Ledger.Billing`, `.PostgreSQL`, `.AspNetCore` — 3.2.0 |
| Depends on | `Ledger.Core` (`.Hosting`, `.Data`) |
| Consumed by | the platform's billing host; the partner API |
| Owns | the `billing` schema, the `/invoices` routes, two events |
| State | published; `[NEXT]` on hold until a real case |
| Open when | the work touches an invoice, a rate, a payment or the billing routes |
```

The heading is the node's folder, quoted and ending in `/`, then one sentence saying what it is.
The method fixes two rows, because they are what the reading decision needs: **State** — the
node's durable state, and the status of what is open there — and **Open when**, the node's
**trigger**, written as the instance's index writes one: a situation in the work, decidable before
anything is opened. The other rows are the workshop's, the same for every node of the workshop,
declared once in its `lint.toml` so that the checks see a card missing one. A family of packages
carries *Packages*, *Depends on*, *Consumed by* and *Owns*; a family of sites carries other rows.

⚠ **A card carries what decides the opening, never what is read once inside.** No rule, no
invariant, no decision: those are the node's atlas, one file away, and a card that summarizes them
is a copy that drifts in silence — measured on an earlier attempt at several atlases inside one
workshop, before the lint existed. A version and a state drift too, and that is accepted: they are
what steers, they cost a line each to keep, and the checks can hold part of it — a version against
what the repository declares, a state against the todo's status line.

**A line deposited for a node not opened.** A session that has something to say to a node it did
not open writes it as a line under that node's card — a finding, in the indicative, as the mailbox
requires. The next session that opens the node **consumes** it: reads it once, turns it into what
the node keeps, deletes it. It stays inside the framing, in the same commit, and it spares opening
a node for one sentence. ⚠ A line left in place to be read again is an item sitting where items do
not belong, exactly as in `tracking.md` § *Work found for another workshop*.

**Nodes are declared, never discovered.** The framing's `lint.toml` lists them, and the checks hold
three things in step: the declaration, the index, and the folders on disk. A folder nobody declared,
a card no folder answers, a declared node with no card — each is a failure, so the index cannot fall
behind the tree in silence.

## Reading: the root always, a node when the work calls for it

A session opens **on the workshop**, never on a node. It reads the root — atlas, todo, handoff,
index — as it reads any framing. Then it reads the nodes the work calls for, and only those:

- **the request may name the node**, with the workshop. That is the cheapest case, and it costs
  the developer three words;
- **otherwise the index decides**: the agent reads the triggers against the request, proposes the
  nodes concerned, and the developer confirms;
- **a node found concerned later is opened then**, and the session says so. A node is a depth of
  reading decided case by case, not a boundary set at the start.

Naming a node saves no reading — the root is read anyway, and the root is the global context the
split had lost. It saves the exchange, in the common case where the developer knows where the
work is.

⚠ **Naming a node steers; it does not bound.** The perimeter stays the workshop. A rejected
design had a session open *on* a node, with a wiring file and a perimeter of its own, writing in
its node and in its index card and nowhere else. It would have rebuilt, inside one workshop, the
very fragmentation the node exists to undo.

⚠ **The node comes from the developer's sentence, never from a document.** The root's handoff says
which nodes the last session touched; it does not say where the next one goes. This is
`organization.md` § *Perimeter* — a document describes, it does not redirect — applied one level
down, and it loses to the concrete sentence exactly as the rule above it does.

**The budget** is the root's: the map, the instance's unconditional files, and the root's framing
documents, index included. A node is measured file by file against the same thresholds, so that
opening one stays affordable; the lint says what the heaviest costs, as information.

## Writing: the root, and the nodes opened

The session writes in the root and in every node it opened. It writes nothing in a node it did not
open — except a line deposited in the index, above.

**Two handoffs record the same work.** The root's entry lists the nodes the session touched. Each
node touched gets an entry of its own, saying what was done there. ⚠ A session that opens that node
later must not learn from the `git log` what the root changed under it: the history is the factual
record, and the handoff is what lets it stay unread.

## Citing across nodes

- **A tag is unique within its node.** Two nodes may both carry `[RELEASE]`, and a bare citation
  resolves in the node where it is written.
- **A citation that leaves its node is qualified**: `billing:[RELEASE]` names the node, `:[RELEASE]`
  names the root. The lint resolves a qualified citation in the node it names, a bare one in the
  current node, and fails a bare one that resolves nowhere — the warning that a tag is cited from
  outside the workshop no longer has a reason to fire inside a family.
- **A delivered narrative of another node is cited by its path from the framing root**:
  `billing/done/RELEASE.md`. A narrative is a location, and the path is what makes it resolve from
  anywhere in the framing.

## What does not change

The meaning of the atlas, the todo, the handoff, `done/` and `_planning/`; the todo's vocabulary;
the commit rules; the mailbox, which stays the channel for the **outside** of a workshop — another
family, the meta level — and is addressed to the workshop, naming the node inside the message; the
boundary between method and instance; the meta level, which is not a workshop; one wiring file per
workshop, listing the repositories of its nodes among its folders, since a folder absent from that
list is out of reach (`bootstrap.md`).

## Adding a node

A node is added to an **existing** workshop, from a session of that workshop: the folder from the
template, the code repository beside the others, the card in the index, the declaration in
`lint.toml`. The installer does it (`setup/CONTRACT.md`), and refuses a node whose folder already
exists, as it refuses to write over anything that exists. The wiring entry for the new repository is
the one thing it prints rather than writes: a wiring is changed last, after the handover
(`bootstrap.md` § *Changing a wiring, and from where*).
