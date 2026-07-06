# Zone Memory Bootstrap Reference

This skill packages the durable parts of a multi-zone coding workflow while
avoiding app-specific coupling.

## What To Preserve

### 1. Clear zone split

Keep four zones with distinct jobs:

- Planning: clarify goals, constraints, risks, options, and acceptance criteria.
- Execution: implement the smallest working change and collect evidence.
- Acceptance: independently judge pass/fail and regression risk without editing code.
- Maintenance: inspect Git, environment, dependencies, runtime artifacts, and hygiene.

### 2. Standard memory file layout

Use `docs/project_notes/` with these files:

- `bugs.md`
- `decisions.md`
- `key_facts.md`
- `issues.md`
- `zone_operating_model.md`

### 3. Evidence-based execution and independent acceptance

Keep this pattern:

- Execution reports evidence: changed files, commands, manual checks, skipped scope, blockers.
- Acceptance reviews the diff and high-signal checks instead of repeating the full execution flow.

### 4. Authoritative behavior and phase docs when needed

For greenfield or under-specified projects, seed:

- `docs/product_consensus/...`
- `docs/architecture.md`
- `docs/implementation-plan.md`

### 5. Short cards over long handoffs

Default to a short task card plus a short Acceptance Contract.

Use full handoffs only for:

- complex multi-stage work
- architecture-affecting changes
- risky product behavior
- ambiguous tasks
- failed acceptance that needs transfer

## Improvements To Bake In

### 1. One authoritative Acceptance rule

Use this rule everywhere:

`Every execution task gets a short Acceptance Contract. A separate Acceptance pass is required only for risky, user-critical, or explicitly requested work.`

### 2. `issues.md` needs a live summary block

Put this at the top of `issues.md`:

- Current phase
- Current recommended next task
- Latest accepted slice
- Open blockers
- Last updated

### 3. `key_facts.md` must stay stable

Use two groups:

- stable facts: paths, commands, ports, bundle IDs, env-var names
- last verified environment: short, dated, drift-prone facts

### 4. Standardize compact evidence

Each execution entry in `issues.md` should prefer:

- Changed
- Verified
- Manual
- Scope skipped

### 5. Prompts should reference stable docs, not restate them

Opening prompts should point to stable docs by path and only add current-task context.

## Portability Rule

The workflow must still work if the agent supports only:

- reading Markdown files
- editing repo files
- following role boundaries

Anything beyond that, such as auto-created threads, is optional sugar.

## Zone Creation Rule

Use this exact split:

- In Codex, when thread creation tools are available, create `规划区`, `执行区`, `验收区`, and `维护区` automatically.
- Immediately send each created zone its matching opening prompt.
- Outside Codex, do not pretend automatic creation happened.
- Instead, return:
  - the four exact zone names
  - one short manual setup procedure
  - four copy-ready opening prompts

## First Invocation Requirement

On the first invocation in a project, the user must always receive four opening
prompts for the four zones.

- Codex path: the prompts are sent automatically into the created zones.
- Non-Codex path: the prompts are returned inline so the user can paste them into four manually created chats or threads.
