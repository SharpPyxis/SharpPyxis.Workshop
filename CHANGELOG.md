# Changelog

What each version changes, and **what updating to it requires of you**. That second half is what
the version number promises here — see § *Versions and updates* in the readme.

This file ships inside the archive, which is the point: a copy has no git history to consult.

---

## 0.4.0 — what a close hands over, one name the mailbox cannot carry, and a copy that can ask

**Updating from `0.3.0`**: copy the new `method/` over yours. Nothing in an instance has to change.
⚠ **One exception, and it is checkable in a second**: if a workshop of yours is named `README` — in
any case — the name is now refused, and you have to rename that folder. It could never have worked:
its address in the mailbox was indistinguishable from the mailbox's own readme, so it received
nothing, silently. Everything else is a copy.

⚠ **Two of the three clauses came from a mechanism failing against itself**, and the third from a
neighbouring workshop reading this repository's own readme. None came from re-reading the rules.

### Added

- **`tracking.md` — what the close hands to you is spoken, not recorded.** The closing protocol ends
  by listing what is left to push, deploy or publish. That list is addressed to someone who acts on
  it within the hour, so it is already false the next time the handoff is read — and it escapes the
  pruning rule, because the entry carrying it is the most recent one there is. The test is
  mechanical: **if the disk can answer it, do not assert it.** A push state, a tag on a remote, a
  clean tree are re-established in seconds by the next session; a reason, a blocker, an intent are
  not, and those are what the file is for. Measured here: *"the received copy has 3 unpushed
  commits"*, written at one close and still read as current two sessions after the commits had gone.
- **`tracking.md`, the installer and the check — a workshop may not be named `README`.** It would be
  addressed by exactly the file every reader of the mailbox has to exempt. The refusal falls on the
  name rather than on the readme, and the asymmetry is the argument: the readme travels into every
  copy and belongs to the method, the name belongs to one workshop. **Case-folded**, which is the
  half that matters — where the file system folds case, `Readme.md` and `README.md` are one file, so
  the exemption swallows the address and nothing reports it.
- **`corpus.md` — why each file restates a trigger the index already gives.** Four reasons, and the
  last assumes no agent, no index and no check, which is why it is the one to keep if the others
  stop holding. With the warning that prevents the wrong reason being read into it: a header saves
  no context, since a file is paid for the moment it is opened.
- **`workshop-lint.py --check-updates`** — compares your `method/VERSION` to the latest published
  release and says whether a newer one exists. A warning and nothing more: no download, no write, no
  step towards updating. It is the only check that reads a remote, behind a flag so the others stay
  offline, and **silence is never read as agreement** — no network, a rate limit, a moved repository
  each end in *could not check*, never in *up to date*.

### Changed

- **The readme situates the method against the layer under it.** A new § *Where it sits* names three
  layers — the model, the harness, the method — and states that the third adds no capability to act
  and depends entirely on the second. The opening no longer claims an agent starts every session
  knowing nothing: agent tooling already keeps a notebook and re-reads an instructions file, and
  what remains yours is deciding what goes in them and knowing they are reached.
- **The readme states that workshops are watertight.** A session reads the framing it was opened on
  and leaves the others closed. The mailbox is the consequence of that boundary rather than a
  convenience beside it — which was visible in the arithmetic: more situations described than
  mechanisms answering them, and the one with no answer was a piece of work polluted by a
  neighbour's conventions.
- **§ *Status* separates the machine from the operating system.** The four steps have now been
  walked by somebody other than the author, on their own machine, from an empty root and the
  published archive. What is still untested is a **case-sensitive file system**: every run so far has
  been on Windows, where a path whose case is wrong loads anyway.

---

## 0.3.0 — a mailbox that answered itself, and a cut that broke what no search could find

**Updating from `0.2.0`**: copy the new `method/` over yours. Nothing in an instance or a workshop
has to change, and no check behaves differently.

⚠ **Every clause here was produced by using the mechanisms, in one day, and none by re-reading
them.** Three came from the mailbox and one from re-cutting a corpus of a dozen files into nineteen.
That is worth knowing before adopting either: both are young, both work, and both had gaps that only
appeared under real traffic.

⚠ **One clause has an effect you can check today.** If a message is waiting in your mailbox and you
have renamed anything in the corpus it cites, it is already broken — a message cites rather than
copies, so its content depends on names it does not control.

### Added

- **`tracking.md` — consuming a message does not entitle you to answer it.** The mailbox had three
  rules, all describing what a receiving session must *do* and none what it may *produce*. So every
  consumption was a licence to deposit, and nothing declared an exchange over. The counter-example is
  the mechanism's own: a workshop received a finding, consumed it, answered; the answering session
  consumed that answer and deposited its own — emptying the mailbox and refilling it in the same
  commit. Three hops, with the payload thinning at each. A mailbox whose emptying is simultaneous
  with its refilling is a channel rather than a deposit, and that defeats the cost the mechanism was
  accepted on, which was one listing per session. The fourth rule closes it, with a test that is
  decidable before writing: *would you deposit this if the first message had never existed?*
- **`tracking.md` — a finding is written in the indicative, never the imperative.** The two existing
  tests catch what a message says and where it comes from; neither catches its mood. *"The same
  gesture is still to be done here"* names the gesture. The same information, stated as what is
  rather than what to do, leaves the conclusion to the reader — which is the whole rule. Mood is
  mechanically checkable where intent is not.
- **`corpus.md` — a cut breaks citations that name no file at all.** Splitting a corpus turns
  *intra*-file references into cross-file ones, and no search for names can find them, because they
  carry none: *"see § Nullability"* inside an example that leaves for another file, *"skip § Book
  theme"* in a header whose section becomes a file of its own. Two were measured on a real cut, and
  both would have shipped.

### Changed

- **`tracking.md` — the mailbox joins the surfaces to sweep when a piece of work moves.** The
  enumeration listed the todo, the handoff and the delivered narratives. It is the mailbox that is
  most exposed of the four, and by design, since a message cites rather than copies: a pending one
  can be broken by a rename it never saw. Measured — a waiting message cited two files that a re-cut
  renamed, one of them a section that became a file. An enumeration listing three surfaces out of
  four is more dangerous than one listing none, because it reads as exhaustive.

---

## 0.2.0 — the checks that were promised, and one that verified nothing

**Updating from `0.1.0`**: copy the new `method/` over yours. Nothing in an instance or a workshop
has to change. One optional gesture is worth the minute it costs — see § *Your `lint.toml`* below.

⚠ **Take this one for the fix**, not for the additions. A check that had been reporting success
since it was written was in fact verifying nothing, on exactly the systems where it is the only
thing standing between a corpus and a name that loads nothing elsewhere.

### Fixed

- **The exact-case check verified nothing on Windows or macOS.** `exists_exact_case` resolved the
  path before comparing it, and resolving canonicalises the case — so it compared the name on disk
  with itself and returned success for exactly the input it exists to reject. On a case-sensitive
  file system the preceding existence test fails first, so the result was right there, by accident;
  everywhere else the check was inert. This affected the editor-workspace check, whose report said
  *exact case* without having established it. Measured on the author's corpus after the fix: the
  22 declared paths do resolve, case for case — the green was accurate, and nothing could have
  shown that beforehand.

### Added

- **Index coverage, in both directions.** Every document of a corpus read by trigger is named by
  that corpus's index, and every index line is answered by something on disk, in exact case. Two
  corpora are covered, the instance's and the method's own. `corpus.md` carried the rule; nothing
  enforced it, and both directions had already failed in the field.
- **The mailbox is checked.** Every file in `instance/messages/` names an existing workshop, case
  for case, because the name *is* the address. A misspelled address is delivered to nobody and
  fails silently on the file systems that tell case apart.
- **The method's version is read.** The installer has stamped it into every workshop it creates
  since it existed, and nothing had ever compared it to `method/VERSION` — which is how that number
  sat at `0.1.0-draft` for some forty commits. The check now tells a framing that is merely old
  from one a major version apart, which is where copying stops being enough.
- **`tracking.md` — a finding is deposited, a proposal is asked for.** The mailbox rule said a
  message carries a finding rather than an instruction, which treats its form and lets its origin
  through: a perfectly descriptive message can still have no business being there, because its
  subject did not exist until a session invented it. What parts them is written now.

### Changed

- **A new workshop ships with size thresholds instead of empty ones.** They were left blank on the
  principle that a template must declare no number — while the same template shipped three, a
  bootstrap budget among them, and nobody thought those wrong. The line that actually holds is
  narrower: a template may declare a **reader's capacity**, never a **workshop's size**. What is
  re-read at every session start bounds any reader, whatever the project.

  The cost of the old rule was measured rather than argued. On a workshop created and closed by an
  agent following every written instruction, the thresholds stayed empty, the per-file guard-rail
  never ran, and the close left behind an obligation to post them that should never have existed.
  The instruction it followed — *post them at the first session close* — was itself wrong: on a
  workshop created and closed the same day there is nothing to measure, and a threshold read off an
  empty workshop is crossed by the second session and raised to silence the lint.

  Existing workshops are untouched. Only the ones created from now on carry the defaults, and each
  says in its own comment that it holds the method's numbers rather than a measurement of itself.

### Your `lint.toml`

Workshops created before the installer existed have no `method_version` key, and the new check
reports that rather than passing over it. Declaring it under `[workshop]` clears the warning and
gives the number something to be compared against:

```toml
[workshop]
method_version = "0.2.0"
```

⚠ It records what you have **reconciled to**, not when the workshop was born: take a version, do
whatever its entry here asks, then move the number. A warning that can never be cleared is one that
gets silenced rather than discussed.

## 0.1.0 — first release

The first tagged version. The repository was made public a few hours before it, at `0.1.0-draft`,
which is the only state anyone could hold that this release supersedes.

**Updating from `0.1.0-draft`**: copy the new `method/` over yours. Nothing in an instance or a
workshop has to change.

### What this version is

A tracking method for one developer working with AI agents: what an agent must read before it can
be useful, and what a session must leave behind so the next one starts informed. `method/` holds
the rules, one entry point and the rest behind triggers; `sample/` is a worked example of a
framing; `instance/` is the half you write, and ships empty.

### Added since the repository was made public

- **Messages between workshops.** A session that finds work belonging to a workshop it is not in
  leaves a message in `instance/messages/`, one file per target workshop named exactly as that
  workshop's folder. It is read once, turned into whatever the receiving workshop keeps, and
  deleted. The folder ships with its own readme and no message in it.
- **The reading order gained a step**: any message addressed to the workshop being opened, which
  costs one listing.
- **`What you have to say`** in this readme — the sentences that trigger something, collected in
  one place for the first time. Two in the ordinary life of a session, four cases that arise only
  when they do, two offers that are answered rather than triggered.
- **A contribution policy**, and a link to the site that describes the method in prose.
