# Changelog

What each version changes, and **what updating to it requires of you**. That second half is what
the version number promises here — see § *Versions and updates* in the readme.

This file ships inside the archive, which is the point: a copy has no git history to consult.

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
