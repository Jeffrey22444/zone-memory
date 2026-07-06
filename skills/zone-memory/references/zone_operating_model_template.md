# Zone Operating Model

## Low-Overhead Defaults

- Use the shortest artifact that safely carries the work.
- Do not repeat stable project rules in every prompt; reference `AGENTS.md`, this file, product consensus docs, architecture docs, and the implementation plan.
- Start with 3-5 files to read, then expand only when needed.
- Prefer short task cards over full handoffs for small and medium work.
- Every execution task gets a short Acceptance Contract.
- A separate Acceptance pass is required only for risky, user-critical, or explicitly requested work.

## Planning

Responsibilities:

- clarify goals, constraints, risks, assumptions, and acceptance criteria
- discuss options and recommendations before handing work to execution
- create short task cards for small and medium work

Boundaries:

- do not edit production code unless explicitly asked
- do not silently decide unclear product behavior

## Execution

Responsibilities:

- read the relevant docs, task card, and memory files
- implement the smallest working change
- run focused verification
- report evidence

Boundaries:

- do not redesign scope
- do not silently decide unresolved product or architecture questions

## Acceptance

Responsibilities:

- inspect the diff, tests, and behavior against the task
- verify acceptance criteria, safety boundaries, and regression risk
- decide pass or fail

Boundaries:

- do not modify code
- do not redesign the solution

## Maintenance

Responsibilities:

- inspect Git status, environment, dependencies, and runtime-state problems
- route product-code changes back to execution

Boundaries:

- do not design product behavior
- do not modify code or config unless explicitly asked

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
