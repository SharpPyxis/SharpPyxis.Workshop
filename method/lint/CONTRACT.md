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

**Repository state.** For every repository the workshop frames: the line-ending files present,
no file drifted back to the other convention on disk, a tracking remote, and the count of
commits not yet pushed. ⚠ A commit that is never pushed protects nothing.

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
