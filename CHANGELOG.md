# Changelog

What each version changes, and **what updating to it requires of you**. That second half is what
the version number promises here — see § *Versions and updates* in the readme.

This file ships inside the archive, which is the point: a copy has no git history to consult.

---

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
