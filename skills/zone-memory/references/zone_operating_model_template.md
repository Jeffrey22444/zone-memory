# Zone Operating Model

## Low-Overhead Defaults

- Use the shortest artifact that safely carries the work.
- Do not repeat stable project rules in every prompt; reference `AGENTS.md`, this file, product consensus docs, architecture docs, and the implementation plan.
- After bootstrap, use the local project docs as the default source of truth and do not default to rereading the skill package.
- Start with 3-5 files to read, then expand only when needed.
- Prefer short task cards over full handoffs for small and medium work.
- Keep `issues.md` excerpt-only; use it for summaries and routing, not for storing full task cards.
- Do not split work so finely that `执行区` loses momentum; prefer medium-sized coherent slices with clear gates.
- Use `/private/tmp` handoffs only for complex, risky, ambiguous, multi-stage, or failed-acceptance work.
- Every execution task gets a short Acceptance Contract.
- By default, every execution task also gets an independent `验收区` review pass unless the user explicitly says to skip it.

## Planning

Responsibilities:

- clarify goals, constraints, risks, assumptions, and acceptance criteria
- discuss options and recommendations before handing work to execution
- create short task cards for small and medium work
- lock down which decisions remain with Planning and must not be silently made by `执行区`
- make execution tasks specific enough that `执行区` does not need to invent unconfirmed strategy or product decisions

Boundaries:

- do not edit production code unless explicitly asked
- do not silently decide unclear product behavior
- do not switch identities; if asked to implement code, stay in `规划区` and route the task to `执行区`

Preferred output:

- short discussion and recommendation first
- wait for user agreement before producing a task card or handoff
- then either a short task card or a full handoff when complexity warrants it
- for simple, small work, give `执行区` a short task card directly and still default to a short `验收区` review task
- when routing complex work with a handoff doc, end with a copy-ready block for `执行区`: absolute path plus a short prompt
- when a handoff doc is used for complex work, default to including a second copy-ready block for `验收区`
- when pairing execution and acceptance, avoid duplicate reading and duplicate test instructions unless risk warrants it

Complexity rule:

- use a short task card when the scope is narrow, the behavior is already clear, and verification is short
- use a full handoff when at least two of these are true:
  - multiple files or modules are involved
  - product or architecture ambiguity must be locked down
  - regression risk is meaningful
  - verification is multi-step or manual
  - implementation is mixed with migration, cleanup, or coordinated follow-up

## Execution

Responsibilities:

- read the relevant docs, task card, and memory files
- implement the smallest working change
- reuse existing patterns
- run focused verification
- report evidence
- stop when the task depends on an undecided planning item

Boundaries:

- do not redesign scope
- do not change product behavior beyond the task
- stop if the task conflicts with safety rules, consensus docs, or code reality
- do not silently decide unresolved product, architecture, or phase-gate questions
- do not switch identities; if asked to perform final acceptance, stay in `执行区` and route the task to `验收区`

Preferred output:

- short implementation summary
- required evidence report using the fixed template below

## Acceptance

Responsibilities:

- inspect the diff, tests, and behavior against the task
- verify acceptance criteria, safety boundaries, and regression risk
- decide pass or fail
- use the Acceptance Contract plus execution evidence plus current diff as the default input set

Boundaries:

- do not modify code
- do not redesign the solution
- do not repeat the full execution task unless the handoff explicitly requires it
- do not switch identities; if asked to implement fixes, stay in `验收区` and route the work back to `执行区`
- may discuss product details when needed for review, but do not edit code unless the user explicitly asks

Preferred output:

- pass/fail first
- findings by severity with file and line references
- a minimal return task only when needed

## Maintenance

Responsibilities:

- inspect Git status, branches, diffs, remotes, and untracked files
- inspect environment, dependency, and runtime-state problems
- route product-code changes back to execution

Boundaries:

- may discuss product details when needed for diagnosis or routing
- do not modify code or config unless explicitly asked
- do not merge, rebase, reset, push, or delete branches without explicit approval
- do not switch identities; if the task becomes product implementation, route it to `执行区`

Preferred output:

- current state summary
- key evidence
- safe next step

## Standard Cards

Execution task card:

```text
Goal:
Out of scope:
Read first:
Deliver:
Edit targets:
Execution self-check:
Stop if:
```

Task-card rule:

- A Planning-generated execution task must be specific enough that `执行区`
  does not have to invent strategy, product behavior, runtime, storage, or
  other unresolved user decisions.

Acceptance Contract:

```text
Task ID:
Goal:
Must not do:
Required checks:
Key risks:
Review input: Acceptance Contract + execution evidence + current diff
```

Execution evidence report:

```text
Task ID:
Changed files:
Scope boundaries:
Commands run:
Results:
Manual checks:
Scope skipped:
Blocked / needs planning:
```

Acceptance review task:

```text
Goal:
Read first:
Review input:
Focus checks:
Do not repeat:
Output:
```

Maintenance handoff:

```text
Status:
Evidence:
Risk:
Route to:
Three-line handoff:
```
