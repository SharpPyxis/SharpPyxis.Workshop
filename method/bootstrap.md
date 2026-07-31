# Bootstrap — the reading chain and its budget

> **Read when** setting up a workshop, wiring an agent to it, or diagnosing why an agent
> started a session knowing nothing.
> **Do not read** during ordinary work — the chain it describes has already run.

---

## What actually reaches an agent

An agent reads what is inside the folders declared by the editor's workspace, and nothing
else. Two consequences that decide the whole design:

- the **method** and the **instance** must both be declared folders. A file outside the list
  is not merely inconvenient to reach — it is unreachable;
- naming the entry-point path at the start of a session is the reliable gesture. It costs one
  sentence and it never silently fails.

⚠ Measured on the repositories this method came from: **seven per-tool trigger files existed,
and not one of them reached the agent** — the session's primary folder held none. Worse than
useless, those files carried *doctrine*, which made them a second source of truth living in a
file that may never be read.

## Tool-specific files are not part of the method

Filenames and auto-loading rules differ per tool and change with tool versions. A published
method that mandated them would ship rules that are wrong everywhere they were not tested.

If a workshop uses such a file anyway, it must stay **thin**. Its entire job is:

- consult the workspace folder list to locate the method and the instance;
- read `method/organization.md`;
- follow what that file references.

It must never carry a rule of its own. The moment it explains *why*, it has become a second
source of truth in the least reliable location available.

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

Before concluding that the instance is absent, consult the workspace folder list. It
corresponds to the folders declared by the open editor workspace, possibly extended by the
tool. The instance may be any of them, including the primary folder.

If it is genuinely absent:

- use the local files of the repository at hand;
- **state explicitly** that the standard bootstrap is unavailable, rather than proceeding as
  if it had run;
- do not invent a structure that has not been confirmed.
