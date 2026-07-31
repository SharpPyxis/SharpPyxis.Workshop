# Memory — a tool's private store versus shared memory

> **Read when** deciding where a fact should be stored, or wiring a second tool or surface to
> a workshop.
> **Do not read** to write a handoff — that is `tracking.md`.

---

## Two systems, and only one of them is authoritative

| | Private store | Shared memory |
| --- | --- | --- |
| Where | Inside the tool, keyed by the session's root directory | `_workspace/memories/` |
| Read by | That tool only | Every agent, every surface, and a human |
| Partitioned by workshop | **No** — by root directory, which is not the same thing | **Yes**, by construction |
| Role | Recall cache, tool-specific | **Durable source of truth** |

The distinction that matters is not privacy, it is **reach**. A fact useful to one tool and
invisible to the next is a fact that will be rediscovered, contradicted, or lost.

## The rule

- **Durable, shareable, workshop-scoped → `_workspace/memories/`**, alongside the atlas, the
  todo and the handoff. Portable, readable by any tool, versioned with the framing.
- **A tool's private store → a disposable session cache.** Never put a source of truth
  there.

⚠ A private store keyed by the session's **root directory** is not partitioned by workshop.
Observed: a single key held the memories of four different workshops, because they all opened
an editor workspace whose first folder was the same one. Anything written there is therefore
liable to be recalled while working on something else entirely.

Two consequences, if such a store is used at all:

- every entry must name the workshop it belongs to, and must not be applied to another
  without re-verification against that workshop's own files;
- an entry is a **dated observation, not a living fact**. Confront it with the code before
  asserting it.

## Structure of the shared memory

| | |
| --- | --- |
| `memories/handoff.md` | Volatile inter-session context — life cycle in `tracking.md` |
| `memories/shared/` | Stable facts useful across several sessions, with an index |
| `memories/sessions/` | Dated notes, when a local convention needs them |

Rules: keep the notes short, factual and reusable; do not duplicate the atlas or the todo
there; re-read the relevant files at the start of a session or before significant work.

⚠ Anything in `memories/shared/` must be reachable from its index. A memory file that no
index names is a memory nobody reads.

## Sharing a workshop with another surface

Sharing does not go through a tool's private store — it is keyed per root directory and is
empty on every new surface. It goes through `_workspace/`: point the other surface at the
workshop's folder, and it reads the framing natively.

⚠ Context **pasted** into a tool's own project settings drifts from the repository the moment
either changes. Point at the versioned files instead of copying them; they are the portable
context, which is exactly their reason to exist.
