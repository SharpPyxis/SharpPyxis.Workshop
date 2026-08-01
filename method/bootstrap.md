# Bootstrap — the reading chain and its budget

> **Read when** setting up a workshop, wiring an agent to it, or diagnosing why an agent
> started a session knowing nothing.
> **Do not read** during ordinary work — the chain it describes has already run.

---

## What actually reaches an agent

An agent reads what is inside the folders it has been given, and nothing else. How that set is
expressed is the tool's business — a multi-root editor workspace, a launch directory, a list of
allowed paths — but every tool has one, and it is always finite. Two consequences that decide
the whole design:

- the **method** and the **instance** must both be declared folders. A file outside the list
  is not merely inconvenient to reach — it is unreachable;
- naming the entry-point path at the start of a session is the reliable gesture. It costs one
  sentence and it never silently fails.

⚠ Measured on the repositories this method came from: **seven per-tool trigger files existed,
and not one of them reached the agent.**

It is tempting to read that as a placement mistake — put the file where the tool looks, and it
works. It is not. The anchor a tool resolves from is a property of the **editor's state when
the session opens**: which node of the tree is selected, which file holds focus. That state
changes between one session and the next while nothing in the repository changes, so a file
placed for one of them is missing for the next. There is no "right folder" to find, because
the folder is not a property of the project.

⚠ And the failure is not "nothing loads". It is **"something else loads"**: the agent starts,
confidently, from a corpus that is not the one you meant, and goes straight into work built on
it. A visible non-start costs one sentence to repair. A silent wrong start costs the session,
and costs it without a signal.

That is why the entry path is named by hand. Not as a fallback for when the wiring fails — as
the contract, because the wiring cannot be made deterministic from where the developer stands.

## Tool-specific files are not part of the method

Filenames and auto-loading rules differ per tool and change with tool versions. A published
method that mandated them would ship rules that are wrong everywhere they were not tested.

If a workshop uses such a file anyway, it must stay **thin**. Its entire job is:

- consult the workspace folder list to locate the method and the instance;
- read `method/organization.md`;
- follow what that file references.

It must never carry a rule of its own. The moment it explains *why*, it has become a second
source of truth in the least reliable location available.

The harm such a file does is proportional to **how confidently it is wrong**. One that only
names a path misleads about a location, and the error surfaces on the first read that fails.
One that carries doctrine misleads about the rules — and nothing in the session will
contradict it, because the rules are exactly what nobody goes back to check.

⚠ A thin file is therefore never redundant safety. It is a second starting point, and one that
can win. A workshop that keeps one accepts that risk deliberately; a workshop that has none
loses nothing, because the reliable gesture was never the file.

## Wiring a workshop

Each workshop's editor workspace declares four kinds of folder:

| Folder | Why |
| --- | --- |
| the method's `method/` | Holds the entry point. Point at `method/`, not at the repository root — a workshop that consumes the method has no business seeing its sample or its plumbing |
| `instance/` | The identity and conventions, read from step 0 |
| the workshop's repositories | The work itself |
| the workshop's `_workspace/` | Its framing |

The workshop where the **method itself** is developed is the exception: it declares the
method repository's root, because there the method is the work.

⚠ A lint over these declarations must check the **folder paths**, not only the instruction
files some tools declare. Observed: three folder paths changed, and the lint stayed green. A
wrong path there breaks nothing visible — it only makes the method unreadable, silently.

## Changing a wiring, and from where

A workshop's folder list is changed **from a session of that workshop**.

The file that carries it invites the opposite: it sits at the root, outside every repository,
and holds nothing but paths. Three properties make it the worst thing to edit from a
neighbouring session:

- it is **outside every perimeter**. The file sits at the root; everything it decides happens
  inside one workshop. It is that workshop's starting point, and nobody else's;
- it is **outside every history**. Editor workspace files are routinely ignored, and the root
  is not a repository. The change therefore enters no `git log` — so the factual record the
  method leans on, precisely so that a handover need not carry it, is missing here;
- it is **confirmed only at the next bootstrap**. Whether a folder list works is seen when a
  session opens against it. From elsewhere one can write the file; one cannot watch it load.

An act with no trace and no confirmation, on someone else's entry point — and a framing
document that prescribes it has stepped past describing, into acting abroad.

⚠ **Creating a wiring is not changing one**, and the exception is mechanical rather than
permissive: a workshop being created has no session of its own yet, so no other author is
possible. The right is therefore **unique and non-renewable** — the second time a session from
elsewhere touches those same files, it is the neighbour again. An installer keys on exactly
that: it refuses to run against anything that already exists, because the existence of the
target is what tells it which side of the rule it is on. The rest is in `setup/CONTRACT.md`.

⚠ A corpus-wide move is the case this rule cannot cover: the method changes location and every
workshop must follow at once, which no single workshop's session can do. Then **name the
operation to the developer, do it in one pass, and record it in the same breath.** Observed: a
session was interrupted between writing four of these files and recording the fact. The framing
announced three workshops still waiting while every one of them had been migrated, and nothing
short of opening the files one by one could tell. A todo line is an acceptable record when it is
the last gesture of a short action; it is no record at all when it is the only one.

⚠ Reading these files globally is not writing them globally. A lint that sweeps every workspace
file at the root — from any session — only checks that the declared paths resolve. It decides
nothing for a neighbour, and it is what makes the exception above survivable after the fact.

## A prerequisite the agent resolves is not a prerequisite

The reference lint needs a runtime. Listing it as a prerequisite in a readme puts the cost on
the reader who skimmed it — and that reader is precisely the one who meets the failure, at the
moment they were closing a session.

The rule is placed on the agent instead: **when the checks are first run, verify the runtime and
offer to install it.** A missing interpreter is then a step, not a wall.

| | |
| --- | --- |
| Runtime | Python, **3.11 minimum** |
| Dependencies | none — standard library only: no third-party package, no virtual environment, no dependency file |
| Invocation | `py -3` on Windows, `python3` elsewhere |

None of the three is a taste, and each carries the reason it exists:

- **standard library only** is what keeps "install Python" a non-event. A lint that pulls a
  package restores the friction the choice was made to avoid — and restores it on every machine
  that adopts the method, not on the author's, where the package is already there;
- **3.11** is set by the configuration format rather than picked. A per-workshop configuration
  must carry the reason for each threshold it declares; a format without comments cannot, and
  any other that can costs a parser, which the line above forbids. TOML carries them, and TOML
  parsing entered the standard library at 3.11;
- ⚠ **the invocation differs per platform and must not be guessed.** On Windows, `python3`
  resolves to a store stub and fails with a message that reads as *Python was not found* — on a
  machine where it is installed and working. An agent that trusts that message diagnoses an
  absence, offers an installation, and puts a second interpreter beside a working one.

⚠ The check belongs in the **script** as much as in this file. This file is read when a workshop
is set up; a machine that changes afterwards is caught only by a guard that runs. A guard that
executes beats a rule that was read once, six months ago.

⚠ And the offer stays an offer. Installing a runtime modifies the developer's machine, which is
theirs to decide: propose the command and the version, then wait.

## Migrating a workshop: sweep for dead instructions, not only dead paths

A path that no longer resolves is mechanical, and a lint finds every one of them. **A sentence
that no longer holds is not**, and it does far more damage: a dangling path fails visibly at
the first read, while a stale instruction is followed.

Observed on the first workshop migrated under this method: every retired path was found and
rewritten, the lint went green, and the session that followed was still redirected out of the
workshop by a handoff sentence that had been true the day before. The sweep had looked for
locations, not for imperatives.

So a migration ends with a reading of the framing documents asking one question — **does any
sentence here still tell an agent what to do, on the strength of a situation that has since
changed?** Handover notes, "read this first" headers, and next-step lines are where they live.

⚠ A lint can narrow the reading without replacing it: a framing document citing a location
**outside its own workshop** — the method and the instance excepted — is a redirect candidate,
and that is mechanically detectable.

## The load is a budget

The sum of what is read at every session start is measured, and the lint reports it. A rule
nobody can afford to read is not a rule.

The lever is **not compression**. Squeezing a document loses the reasons, and a rule without
its reason is the first thing an agent overrides when it seems inconvenient. The lever is
splitting by **reading temporality**:

- what is read *always* is a map — structure, vocabulary, index, reading order;
- everything else is reached by a trigger stated in its own header.

This is why the rule that makes a todo self-sufficient — an item carries its meaning or cites
the document that does — deliberately makes it grow, and why that growth is not fought.
Fighting it would fight the rule. Moving what is rarely needed behind a trigger does not.

## Fallback

In `organization.md` § *Robustness and fallback*, and only there. It is needed at the moment
the instance cannot be found — which is a moment for reading one file, not two.

This file said the same thing in its own words for a while, which is how a second source of
truth starts: not by contradicting the first, but by agreeing with it until one of them is
edited.
