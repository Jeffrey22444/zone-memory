# Zone Operating Model

## Low-Overhead Defaults

- Use the shortest artifact that safely carries the work.
- Do not repeat stable project rules in every prompt; reference `AGENTS.md`, this file, product consensus docs, architecture docs, and the implementation plan.
- Start with only these files, then expand only when needed:
  - `AGENTS.md` or `CLAUDE.md` workflow section
  - this file
  - `docs/project_notes/key_facts.md`
  - `docs/project_notes/issues.md` Current Summary plus the relevant latest block
- Prefer short task cards over full handoffs for small and medium work.
- Do not split work so finely that `执行区` loses momentum; prefer medium-sized coherent slices with clear gates.
- Use `/private/tmp` handoffs only for complex, risky, ambiguous, multi-stage, or failed-acceptance work.
- For long-running multi-phase projects, use `docs/project_notes/current_task.md` as the active task surface and overwrite it for each new task.
- Treat old task-card files as archives; do not append detailed task cards there by default.
- Every execution task gets a short Acceptance Contract.
- A separate Acceptance pass is required only for risky, user-critical, or explicitly requested work.
- Do not wake all four zones by default. Activate only the zones that have a concrete job for the current slice.
- After bootstrap, do not reread the packaged skill files during ordinary project work unless the workflow itself is being revised.

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

Preferred output:

- short discussion and recommendation first
- then either a short task card or a full handoff when complexity warrants it
- for simple, small work, give `执行区` a short task card directly and do not default to a separate `验收区` task
- when task cards start accumulating, write the active task card and Acceptance Contract to `current_task.md` instead of growing a historical prompt file
- when `current_task.md` is the active task surface, do not repeat the full task card in the Planning reply; end with short copy-ready prompts that tell `执行区` or `验收区` to read `current_task.md` and name the task ID
- when routing complex work with a handoff doc, end with a copy-ready block for `执行区`: absolute path plus a short prompt
- when a handoff doc is used for complex work, default to including a second copy-ready block for `验收区`
- when pairing execution and acceptance, avoid duplicate reading and duplicate test instructions unless risk warrants it

Verification defaults:

- For small Planning doc-only updates, do not run `git diff --check` by default.
- Use `git status --short` or targeted file reads when the goal is only to confirm touched files.
- Run `git diff --check` only for larger Markdown rewrites, complex fenced code blocks, `.gitignore` edits, or concrete whitespace/conflict-marker risk.
- Do not run full `git diff` as a routine Planning check; use targeted diffs only when exact changed lines are needed.

## Execution

Responsibilities:

- read the relevant docs, task card, and memory files
- if `current_task.md` exists, read it for the assigned active task; do not scan historical task-card archives unless the current task explicitly says to
- do not open product, architecture, implementation-plan, bugs, or decisions docs unless the task actually triggers them
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

Preferred output:

- short implementation summary
- required evidence report using the fixed template below

## Acceptance

Responsibilities:

- inspect the diff, tests, and behavior against the task
- verify acceptance criteria, safety boundaries, and regression risk
- decide pass or fail
- use the Acceptance Contract plus execution evidence plus current diff as the default input set
- if `current_task.md` exists, read the current Acceptance Contract there
- do not reread the full execution history when the current task block and latest evidence block are enough

Boundaries:

- do not modify code
- do not redesign the solution
- do not repeat the full execution task unless the handoff explicitly requires it

Preferred output:

- pass/fail first
- findings by severity with file and line references
- if the verdict is fail, provide a minimal rework task for `执行区`
- if the verdict is pass, omit the rework task unless the user explicitly asks for follow-up work

## Maintenance

Responsibilities:

- inspect Git status, branches, diffs, remotes, and untracked files
- inspect environment, dependency, and runtime-state problems
- route product-code changes back to execution

Boundaries:

- do not design product behavior
- do not modify code or config unless explicitly asked
- do not merge, rebase, reset, push, or delete branches without explicit approval

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

## Project Note File Rules

- `current_task.md` optional: current active task card and/or Acceptance Contract only; overwrite it for the next task instead of preserving detailed historical prompts.
- `issues.md`: keep concise summaries, changed files, evidence, blockers, and acceptance outcomes; do not store full prompt archives.

## Anti-Patterns

- Do not keep appending full task cards to a growing archive when `current_task.md` is enough.
- Do not reread the whole project-note set when the startup read set already answers the current slice.
- Do not wake unused zones just because they exist.
