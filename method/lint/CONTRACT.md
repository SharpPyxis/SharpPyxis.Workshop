# Lint contract — what must be checked

> **Read when** running the checks, changing their configuration, or reimplementing them.
> **Do not read** during ordinary work.

This file is the portable part. It states **what** a workshop's framing must be checked for,
and why each check exists. `workshop-lint.py` is one implementation of it — the reference one,
shipped so that adopting the method does not start with writing a tool.

⚠ **One implementation, and only one.** This method exists partly because the same lint was
found in two divergent forks — 269 lines against 198, with 77 in common — and absent from a
third workshop, precisely the one where an unfiled document was sitting at the root of a framing
folder against a rule the other two enforced. Shipping a second implementation would reproduce
that fault by design. A workshop that cannot run the reference implementation reimplements from
**this file**, not from that code.

---

## Resolving the layout

Everything below is checked against a layout that must be **resolved by disposition, never by
name** — a hard-coded folder name breaks at the first rename, and for everyone who adopts the
method under other names.

| | How it is found |
| --- | --- |
| the workshop | the parent of the framing folder the checks were pointed at |
| the root | the parent of that workshop |
| the meta level | the folder under the root holding **`method/organization.md` and `instance/`** — that pair is the whole test |
| the instance | `instance/` inside the meta level |
| the method | `method/` inside the meta level — **except** in a workshop that contains the method itself, where the working copy prevails |
| a node | a declared sub-folder of the framing holding an atlas (`tree.md`); the framing the checks are pointed at is always the root, the one holding `lint.toml` |

⚠ The meta-level rule used to read *"the workshop that also hosts the instance"*, and it was
wrong in a way only another machine could reveal. It was inferred from the one corpus where the
method is **developed** — and there alone the meta level carries a framing folder as well.
Everywhere else the condition is false by construction, so the reference implementation refused
to resolve a correct layout. **A rule inferred from the only instance you can see is a rule you
have not tested.**

⚠ The exception on the last line is not a convenience. Without it, a session enlarging the entry
point has its bootstrap budget measured against the *received copy* — a green report at the exact
place where the budget is decided, saying nothing. An implementation reports which of the two it
used, so the reader can contradict it.

## Levels

| Level | Means | Exit |
| --- | --- | --- |
| `OK` | The check passed | — |
| `WARN` | A drift worth seeing, that does not block a commit | 0 |
| `FAIL` | A rule is broken; fix before committing the session close | 1 |

⚠ The distinction is not severity, it is **who decides**. A `FAIL` is mechanical: the rule says
so, and no judgement is involved. A `WARN` is a measurement handed to the owner — a threshold
crossed, a date drifting, a document that may have outlived its subject. A check that guesses at
intent produces `WARN`, never `FAIL`.

## The socle — every workshop, no exception

**Handoff — bounded number of sessions.** The volatile file is re-read at every start; one that
grows without bound damages exactly what it exists to help. Counting a session means recognizing
its entry heading, and that heading is **workshop-declared, never assumed**: a cadrage whose
title form diverges from the reference implementation's default must still be caught, not read as
empty. `tracking.md` § `memories/handoff.md` requires one entry per session and requires several
sessions on the same day to be numbered rather than spread over consecutive ones — the form
`## Session <date>`, and `## Session <date> (2)` for a second session that day — but only the
fixed part before the date is what a check matches on; the date and the optional `(N)` are free
text.

**Todo — nothing finished left in place.** A closed item leaves: notable ones become a line in
the atlas, minor ones disappear. A todo crowded with closed items loses its steering value.

**Sizes — per file, in characters.** ⚠ **Characters, not lines.** Lines measure formatting as
much as volume: a consolidation pass was once measured removing 15% of a file's content while
its line count did not move, because the file mixed prose wrapped at 100 columns with paragraphs
held on single 200-to-1200-character lines. A line-based threshold therefore penalises readable
text and rewards a wall. Characters are deterministic, need no dependency, and track tokens at
roughly 3.5:1 — closer to 3 on passages dense in identifiers, which is why words are worse
still: they undercount precisely the passages that cost the most.

**Growth without pruning — a report, never a verdict.** A framing document that has only ever
grown has never been pruned, and that is measurable where the drift behind it is not. Measure it
over a declared window of the recent commits that touched the file: **per piece of work for the
todo**, keyed on the `[TAG]`, which this method already defines as a stable key reused by commit
messages and delivered narratives; **per file for the atlas**, whose headings are prose and are
renamed often enough that a per-section history would reset on the very sections that were just
reworked.

Two guards, and both are what keep it usable: report only above a declared floor, so a young piece
of work stays quiet until it has something to prune; and report a **WARN**, never a FAIL. False
positives are expected — a subject can legitimately grow for months — so the output is a report
someone reads, which is the model this contract uses wherever judgment cannot be mechanised.

⚠ **Pruning has a declared minimum.** A decrease counts only if it removes at least a declared
number of characters, set just under the size of the smallest item. Any decrease used to count, and
a thirteen-character trim of a section's heading was measured silencing the check with nothing
pruned. The minimum is absolute rather than relative because what pruning removes is an item, and
an item's size does not scale with the piece of work that carries it.

⚠ **Two limits are known and kept, and both make the report noisy rather than wrong.** Measured on
a real todo the day the check went into service:

- **renaming a tag resets its series.** The check keys on the `[TAG]` because the method defines it
  as stable — and it is, except on the day a scope turns out to be wrong. That day the history
  starts again under the new name, and a subject is reported over the life of its name rather than
  of its work. Following renames would need a declared old → new mapping; the retired-names list
  carries free text, not a target tag;
- **the window slides.** A subject nobody touched can enter the report because the commits that
  carried its last pruning have aged out of the window. Widening the window moves the edge without
  removing it.

Neither is fixed mechanically, and that is consistent with what the check claims: a report someone
reads tells these cases apart in a glance, which is cheaper than a rule that tries to.

⚠ **What it stands in for.** `tracking.md` § *Closing a session*, step 3, asks the session to name
what it renders false before writing. That is a rule, it fires when attention is lowest, and it
loses against the concrete case like every rule read early. The semantic half of the drift — a new
line that contradicts an old one — cannot be detected by a machine at all. **A file that only grows
can.** This check is that half, and claiming more for it would be dishonest: it says a document was
never pruned, never that it is wrong.

⚠ **No stored state.** The history is in the repository; a check that kept its own measurements
between runs would be a second source of truth for something git already holds exactly.

**Bootstrap load — the sum.** The per-file thresholds are a distribution guard-rail; the number
that actually constrains a session is the **total** re-read at every start, before a line of
code is opened: the method's map, the instance index and the identity file it declares, and the
workshop's tensed documents. ⚠ A workshop that checks only the per-file sizes is not measuring
its budget — it is measuring its balance.

**Planning documents — a status header, and a resolvable tag.** Every document in the long-form
folder carries `> Statut :` (or its local equivalent). Without it the folder holds documents at
four different stages and says so nowhere. A `[TAG]` cited in that header must be findable in
the todo; if it is not, the scoping has probably been executed and the document has outlived it.

⚠ **And the check reports when the folder is absent.** A check that returns in silence cannot be
told apart from one that did not run. This matters more than it looks: the folder's name is
configurable while the implementation is shared, so a workshop whose configuration lags behind a
changed default loses the check entirely, with nothing in the report to say so. Observed in this
method's own workshop, which has no long-form folder and whose report said nothing about it for
as long as the check existed.

**No stray document at the root of the framing folder.** A scoping document sitting beside the
atlas is read by nobody and contradicts it in silence. Either it is a planning document and it
goes in the long-form folder with a status header, or its content belongs in one of the tensed
documents.

**Todo grammar.** A piece of work is `## [TAG] Title` followed within two lines by a status line
drawn from a **closed vocabulary**. Tags are unique. Item prefixes come from the declared set,
and the prefixes reserved for other tenses are refused outright — an item marked done inside the
todo is an item nobody moved to the atlas or to the delivered narrative.

⚠ **The declared set is a whitelist, and the reserved list does not stand in for it.** An
implementation that only hunts the reserved prefixes passes anything nobody thought to reserve,
while its own success line names the declared set — asserting what it never looked at. Measured:
a sixth prefix in use thirty-nine times across a workshop, reported green as *prefixes within the
vocabulary*. Refusing an undeclared sign is also what fixes its **code point**: a prefix nobody
declared has no identity, and one of two look-alikes (U+29D7 against U+23F3) silently defeated a
rewriting script, which dropped the items carrying the other. The two failures are the same
omission seen twice.

⚠ **A workshop that reserves nothing still gets a line.** Returning in silence when the reserved
list is empty cannot be told apart from a check that did not run — the same argument as the
long-form folder above, and the reason the declared set has to be what drives the check.

**Delivered narratives — named by tag, and cited without dangling.** One file per `[TAG]`, named
after it. Every reference to such a file must resolve, **from anywhere in the framing** — the
long-form folder cites them most, and a reference stranded there by a deletion dangles exactly as
one in the todo does.

**Cited tags exist.** ⚠ Any `[TAG]` cited anywhere in the framing must exist as a section of the
todo or as a delivered narrative. Citing by identity protects a reference against a corpus that
*moves*; it does nothing against one that *closes*. A tag does not go stale visibly — it stays
readable, plausible and wrong. Observed: three citations of a tag survived its closure, and two
of them announced a blocker that had been lifted, one of them gating a publication.

**And a citation that names a location resolves against that location.** `todo.md § [X]` asserts
that `X` is a piece of work in the todo; the check above sees only that the tag exists somewhere,
so the citation goes on resolving while `X` lives on in the delivered narrative alone. **A rename
produces that state mechanically** — the todo is corrected, the narrative keeps its original name,
and every citation of the old address survives it. ⚠ `FAIL` rather than `WARN`, unlike a bare tag:
the form is unambiguous, so it cannot be a turn of phrase. Observed: two such citations outlived a
rename by fifteen days, through a pass that was hunting for exactly that residue and found four
others; what finally surfaced them was the narrative being deleted, which made the tag stop
existing — at a moment when the rename that caused them had nothing to do with the work in hand.

**Header dates.** A document whose declared date lags well behind its last modification is a
document whose header no longer describes it. ⚠ `WARN` only: modification times do not survive a
clone, so this check measures a working copy, not a truth.

**Citations resolve.** Three checks, and their narrowness is deliberate:

- **links** — every markdown link target must resolve. A link is unambiguously a location: it is
  clickable, and a dangling one sends a reader to a file that is not there;
- **declared prefixes** — a quoted token starting with a prefix the workshop declares
  *structural* must resolve;
- **retired names** — names declared retired must appear nowhere, including outside the framing
  folder. Paths leak into code comments and dotfile headers, which have no reason to follow the
  corpus when it moves. This is the migration check, and its list belongs to the workshop being
  migrated, never to all of them.

⚠ **Why the first two must stay narrow.** An early implementation tried to resolve every quoted
token that *looked like* a path. It produced several hundred false failures on a real workshop,
because almost every such token is an **identity**, not a location: a document named without its
folder, a URL route, a MIME type, a date format. The corpus was already citing by identity —
which is the rule — and the check punished it. **A lint verifies what is declared to be a
location; it does not guess.**

⚠ And the failure mode to design against: an early sweep escaped its pattern for a regular
expression while asking for a literal match. It searched for the escape characters themselves
and reported only the one token that had none — **seventeen occurrences missed in silence**. A
lint that under-reports is worse than no lint, because it returns a green that means nothing.

**Redirect candidates.** A framing document citing a location **outside its own workshop** — the
method and the instance excepted — is a candidate. ⚠ `WARN`, and it narrows a reading rather
than replacing it: the sentence that caused this check to exist did cite an outside path, but a
wording without any path passes straight through. The defect is semantic; this is only its
mechanical shadow.

**Index coverage — both directions.** Every document of a corpus read by trigger is named by
that corpus's index, and every index line is answered by something on disk, in exact case. Two
corpora are covered: the **instance**, and the **method** itself.

⚠ **Both directions fail, and both have been observed.** A file no index names is read by
nobody — two genuinely useful files lived outside every index for months, one of them a todo. An
index line no file answers is the same failure mirrored, and harder to see from the other side: a
folder was declared in the method's index and did not exist. `corpus.md` § *The index is the last
gesture* carries the rule; this is the check that makes it more than a rule.

What an index declares is read from **table rows** — the first cell, quoted, ending in `.md` or
`/`. ⚠ Prose is not scanned, and that narrowness is the same one the citation checks need: an
index names neighbouring corpora in its own sentences, and reading those as declarations
over-declares, which silences the check rather than failing it.

Two shapes, because the two indexes genuinely differ:

- the **instance's** index is a file, so it is read whole;
- the **method's** is a *section* of the entry point, which carries other tables — one of them
  naming the framing documents, which do not live in `method/`. That section is delimited by a
  marker. ⚠ Locating it by its heading was the other candidate and has already failed in the
  field: a section was cited under its former title and nothing noticed, because a lint checks
  tags and paths, not prose. Where the marker is absent the check **says so** rather than
  passing — silence cannot be told apart from a check that did not run.

Exemptions belong to the implementation, never to the configuration: an index does not declare
itself, and a readme is addressed to a reader rather than to a trigger. ⚠ Same arbitration as the
`[TAG]` metavariable — an exemption left to each workshop is a false positive every adopter meets
on their first run. Files that are not documents are out of scope for the same reason a trigger
index only indexes documents.

A declared `folder/` is declared whole and its contents are not corpus entries; a declared
`folder/file.md` extends the corpus into that folder, which is then walked as well.

⚠ **This check has the meta level as its subject, not the workshop** — so every workshop reports
the same finding until it is fixed. That is the mechanism rather than noise: the corpus is read
by all of them, so the first session opened anywhere sees it, and one correction clears all of
them. It takes no configuration key, because both locations are named by the method and a key
would carry a value that never varies.

**The method's version, against the one this framing was set up under.** `setup/CONTRACT.md`
promises it: the installer stamps the version into every workshop it creates, so a later check can
tell a framing that is merely **old** from one that has **drifted**. The separation is the one the
readme publishes — a minor or a patch means copying the new `method/` over yours is enough, a major
means something of yours changes by hand — so the major is what parts the two messages.

⚠ **A number no check reads does not move.** This one held `0.1.0-draft` from an initial commit
through some forty of them, stamped into every workshop meanwhile. The stamp existed, the copies
existed, and the whole mechanism was inert for want of anything depending on it.

⚠ **The stamp records what the owner has reconciled to, not an archaeological fact.** Taking a new
version means doing whatever its changelog entry asks and then moving the number. Without that
second half the warning can never be cleared — and a warning nobody can clear is the one that gets
silenced rather than discussed.

⚠ **WARN throughout, never FAIL.** Reading an older method breaks no rule; when to update is the
owner's call, and a FAIL would block the close of a session that has nothing to do with it.

⚠ **A stale stamp also compares `lint.toml` against the reference template, key for key** —
`[sizes]` excepted, since those keys are the workshop's own filenames rather than a fixed
vocabulary. A minor can add a structural key the same way it adds a rule (`handoff_session_heading`
did), and nothing re-runs the installer against a workshop already framed: copying the new
`method/` over does not by itself carry a new key into an existing `lint.toml`. Listing what the
template declares and this framing's `lint.toml` does not turns *an update is due* into *these keys
are missing* — the part of the reconciliation that does not need the changelog to be found.

⚠ **`--fix` closes what it safely can, on its own — the rest still asks.** Same shape as
`propagate-copy.py --apply`: report by default, write only on the flag. It adds a missing key
bare, without the template's own commentary — that prose is English, and a workshop's own
`lint.toml` is free to be written in the owner's language, so copying it in would plant the exact
drift a duplicated rule becomes. A key whose template value is still an unresolved
`{{PLACEHOLDER}}` — `name`, `repositories`, `instance_files` — is never written this way: that
value is workshop-specific data, and only `workshop-setup.py`, at the one moment it is free to
choose it, has a right to it. **Additive only**, in both senses of the word: it appends the field
to the end of its `[section]`, and it never rewrites a key already present — the same asymmetry
`setup/CONTRACT.md` draws between creating a wiring and changing one.

**The mailbox — every address resolves to a workshop.** One file per target workshop, named
exactly as that workshop's folder. Anything else in the folder is not an address.

⚠ **Note which of the two failures this catches.** A wrong but existing address is recoverable:
whoever opens the file sees it is not theirs. A misspelled one is delivered to nobody, and on a
file system that tells case apart it fails without a sound. The second is why this is worth a
machine rather than a proof-reading, and why the report distinguishes them — a case mismatch names
the workshop it should have been.

The folder is named by the method, and a workshop is resolved by the test the layout already
applies. Neither takes a configuration key. ⚠ A mailbox that is absent is **reported**, not passed
over: the method ships that folder, so its absence means a finding for a neighbour has nowhere to
go — and silence there would be indistinguishable from an empty one.

## Nodes — a framing split in one level

`tree.md` lets a workshop too large for one framing split it into **nodes**, each a sub-folder of
the framing holding the same documents, with a `nodes.md` at the root saying when to open each. The
checks are pointed at the root — the folder holding `lint.toml` — and they see the nodes from there.

**Declared, never discovered.** `[nodes] names` lists them. Three things are held in step, and each
mismatch is a `FAIL`: a declared node without its folder (a sub-folder holding an atlas), a folder
holding an atlas that nothing declares, a declared node without its card in `nodes.md`, a card that
names no declared node, a `nodes.md` with no `[nodes]` at all. ⚠ A workshop without nodes gets one
`OK` line saying so — silence cannot be told apart from a check that did not run, and a stray
`nodes.md` or an undeclared sub-folder is exactly the case this check exists for.

**A card is read by its heading and its two fixed rows.** The heading is the node's folder,
backticked and ending in `/`; the rows are the two `tree.md` fixes — *State* and *Open when*, or
the local equivalents the workshop declares in `[nodes] card_rows`. A card lacking one is a `FAIL`:
they are what the reading decision needs. The other rows are the node's own and are not read — a
rule there would assume what a node is.

**The socle runs once per node, with the root's keys.** Handoff, todo, sizes, growth, long-form
folder, stray documents, grammar, item prefixes, delivered narratives, cited tags, header dates and
citations — the same checks, the same thresholds, each line of the report prefixed with the node's
name. A node that has measured its own thresholds overrides them in `[nodes.<name>.sizes]`. The
root's documents are walked without the nodes', and each node's without the root's: a tag is
unique **within its node**, so a node's tags read from the root would be tags that exist nowhere.

**Citations cross nodes by a qualifier, and bare ones fall back to the root.** `billing:[RELEASE]`
resolves in the node `billing`, `:[RELEASE]` in the root, and a qualified citation that resolves
nowhere — no such node, no such tag there — is a `FAIL`, as an addressed citation is: the form is
unambiguous, so it cannot be a turn of phrase. A bare `[RELEASE]` resolves in the scope where it is
written, **then in the root** — the family's common ground, visible from every node; a sibling's
tags are not — and stays a `WARN` when it resolves nowhere, as everywhere else. A delivered
narrative follows the same rule: `billing/done/RELEASE.md` resolves in that node from anywhere,
`done/RELEASE.md` in the current scope then in the root. ⚠ The fallback is what keeps `:[TAG]`
rare: it is needed only where the root's tag is shadowed by the node's own, and a bare citation
then means the node's.

**The budget stays the root's.** `nodes.md` joins the chain the budget sums, since it is read at
every start; a node is not in the sum, and its documents are bounded one by one by `[sizes]`. One
`OK` line says what opening the heaviest node costs, on top of the budget — information, not a
verdict, since a node is read only when the work calls for it.

**A node's repository is a repository of the workshop.** `[nodes.<name>] repository` names it; the
folder must exist (`FAIL`), and it belongs in `[workshop] repositories` like the others (`WARN` when
it is not), so that its line endings and push state are checked with the rest. A node without a
repository is ordinary.

⚠ **Two limits are known and kept.** A version written on a card and the one the repository
declares can drift, and so can a card's state and the todo's status line; both are reported by
nobody today. Either could be held by a check reading the repository and the todo, and both are
cheap — they wait for a real workshop to show which drifts first. And `git cat-file --batch` reads
its paths from the repository root while `git log` reads them from the current folder: the growth
check prefixes the path it asks for, because run from a node it would otherwise fetch the root's
file of the same name — the root's todo in place of the node's — and report it in silence.

## Asking whether a newer version is published — the only check that reads a remote

**Behind an explicit flag, never in the socle.** It compares the local `method/VERSION` to the
latest release published by the method's own repository, and reports whether a newer one exists.
Nothing else: no download, no write, no step towards updating, which stays a copy of `method/` as
the readme describes it.

Three properties make it safe to add to a corpus whose whole value is that its checks are cheap:

- **the socle stays offline.** A network call fails or hangs for reasons that have nothing to do
  with a framing, and a check that does that at every close is a check people stop running. The
  flag is what keeps the two apart;
- ⚠ **silence is never read as agreement.** No network, a rate limit, a moved repository, a reply
  that does not parse — each ends in *could not check*, never in *up to date*. A version check that
  reassures when it has learned nothing is worse than none, because it answers a question it was
  not asked;
- **WARN throughout, never FAIL.** Holding an older method breaks no rule. What to do about it, and
  when, belongs to the owner.

⚠ **It is the one place this corpus hardcodes a location**, and the only one where it can be
argued: everything else cites by identity, because a name survives a move and an address does not —
but a copy has no remote and no history, so there is nothing to resolve a name against. The
implementation writes it once, and the third property above is what makes a dead address harmless.

⚠ The distinction it reports is the readme's own: **a major means copying is not enough**, and the
changelog entry says what changes by hand. Same separation as the version stamp, asked of the other
side.

## Checks a workshop declares for itself

Off unless configured. Each exists because a real workshop needed it and another did not.

⚠ **Off is reported, in one line for the whole family.** Each of these returns at once when its key
is absent, so removing a key used to make the check vanish from the report — the silence the
long-form folder is already reported against, and more common here, since a workshop that drops a
roadmap it no longer needs is legitimate, not lagging. And where a key is declared but what it names
is not found — a roadmap heading no todo carries — that is a configuration drifting from its framing,
and it is a `WARN`, never a skip.

**Repository state.** For every repository the workshop frames: the line-ending files present,
no file drifted back to the other convention on disk, a tracking remote, and the count of
commits not yet pushed. ⚠ A commit that is never pushed protects nothing.

⚠ **The meta level is checked too, for line endings only**, when it is a repository. It belongs to
no workshop, so no workshop declares it, and it is the one surface every session reads: its files
were measured CRLF on disk for five weeks, git silent throughout since it normalises at staging.
Every workshop's run reports it, which is redundant and costs a line. Its push state stays out — an
owner who versions the meta level knows where it goes, and declaring it among a workshop's
repositories would make one workshop the owner of what belongs to none.

**Editor workspace.** The folder list an agent is actually given must resolve, **in exact case**.
⚠ Both halves have failed in the field. Three folder paths were changed and the lint stayed
green — a wrong path there breaks nothing visible, it only makes the method unreadable, in
silence. And a name whose case differs from disk loads nothing at all on a case-sensitive file
system, while working perfectly on the author's machine.

**Publication files.** For a repository meant to be published: the files its audience expects.

**Roadmap freshness.** Where a workshop keeps an ordered snapshot of its work, a tag that has
closed or gone dormant since means the snapshot is stale.

**Echoed items.** A workshop may mark items that must be read out at every run — publication
blockers, typically. ⚠ A blocker that has to be remembered is a blocker that gets forgotten, and
echoing it costs one line.

**Tags cited from outside the framing.** A static site, a code repository or any surface that
references the workshop's tags. A citation left behind by a closed tag points at nothing, and —
unlike a dangling path — it fails nowhere at all.

**Extra fields on the status line.** A workshop that classifies its work along an axis of its own
declares the field and its closed vocabulary.

## Configuration

Declared **per workshop**, in the framing folder — the configuration of a framing belongs to
what it frames. ⚠ Hard-coding it is what produced the forks: the two divergent versions differ
almost entirely in constants, not in logic.

The format must let a declared value carry the **reason** it holds. A threshold without its
reason is raised to silence the lint; a threshold with its reason gets discussed instead. That
requirement excludes any format without comments, and — combined with the standard-library-only
constraint — settles the format as TOML and the runtime floor as Python 3.11.

⚠ **What a template may declare is a reader's capacity, never a workshop's size.** The two look
alike and behave nothing alike. What is re-read at every session start bounds what any reader can
afford, whatever the project — that number ships, generous enough to catch a file that has swollen
without constraining one still growing. A threshold claiming to describe *this* workshop before it
has any content is guesswork that will be either ignored or wrong, and that one does not ship.

A shipped threshold therefore says in the same breath that it is the method's default and not a
measurement of the workshop reading it, and points at the formula that replaces it: a todo's floor
is roughly *open subjects × cost per subject + header*, measured once there is something to
measure.

⚠ **This reverses a flat ban on shipping any number, and both halves of why it fell are worth
keeping.** The template already contradicted it, shipping three — a bootstrap budget, a token
ratio, a session count — none of which anybody thought wrong, which is the sign a rule is drawn in
the wrong place. And the measurement invoked against defaults, *400 lines posted for a todo whose
floor turned out to be around 420*, was taken **in lines**, the unit this contract has since
rejected on its own evidence. A rule cannot outlive the scheme its proof was gathered under.

⚠ The cost of the ban was measured before it was lifted: on a workshop created and closed by an
agent that followed every written instruction, the thresholds stayed empty, the per-file guard-rail
never ran, and the closing left behind an obligation to post them that should never have existed.
A guard-rail waiting on a gesture nobody makes is a guard-rail that is off.

## Runtime

Stated in `bootstrap.md` § *A prerequisite the agent resolves is not a prerequisite*, and
enforced by the implementation itself rather than by this document alone: a rule read once, when
a workshop was set up, does not catch a machine that changed afterwards.
