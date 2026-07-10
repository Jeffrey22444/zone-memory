# Zone Memory Bootstrap Reference

This skill packages the parts of the Desktop Pet workflow that were worth
keeping, while baking in the improvements that reduce drift and token waste.

## What To Preserve

### 1. Clear zone split

Keep four zones with distinct jobs:

- Planning: clarify goals, constraints, risks, options, and acceptance criteria.
- Execution: implement the smallest working change and collect evidence.
- Acceptance: independently judge pass/fail and regression risk without editing code.
- Maintenance: inspect Git, environment, dependencies, runtime artifacts, and mainline hygiene.

This keeps planning from silently coding, execution from silently redesigning,
and acceptance from turning into another implementation pass.

### 2. Standard memory file layout

Use `docs/project_notes/` with these files:

- `bugs.md`
- `decisions.md`
- `key_facts.md`
- `issues.md`
- `zone_operating_model.md`

For long-running multi-phase projects, optionally add:

- `current_task.md` for the active task card or active Acceptance Contract only

The names are plain engineering documentation, not AI-specific artifacts.

### 2.5. Chinese-first zone naming

When this skill creates zones automatically, use these Chinese names by default:

- `规划区`
- `执行区`
- `验收区`
- `维护区`

English role names can still appear inside the opening prompts for clarity, but
the visible zone names should default to Chinese.

### 3. Evidence-based execution and independent acceptance

Keep the ADR-002 pattern:

- Execution reports evidence: changed files, commands, manual checks, skipped scope, blockers.
- Acceptance reviews the diff and high-signal checks instead of repeating the full execution flow.

This is the highest-value token saver in the system.

### 4. Authoritative behavior and phase docs when the project needs them

For greenfield or under-specified projects, seed tracked docs that answer the
questions execution should not answer implicitly:

- `docs/product_consensus/...` for confirmed behavior and undecided behavior
- `docs/architecture.md` for module and dependency boundaries
- `docs/implementation-plan.md` for phase deliverables, verification, and gates

Without these docs, execution will start filling in product and architecture
gaps on its own.

### 5. Short cards over long handoffs

Default to a short task card plus a short Acceptance Contract.
Use full `/private/tmp` handoffs only for:

- complex multi-stage work
- architecture-affecting changes
- risky product behavior
- ambiguous tasks
- failed acceptance that needs transfer

## Improvements To Bake In

### 1. One authoritative Acceptance rule

Avoid rule drift. Use this rule everywhere:

`Every execution task gets a short Acceptance Contract. A separate Acceptance pass is required only for risky, user-critical, or explicitly requested work.`

That keeps the contract cheap while avoiding forced review loops for trivial work.

If Acceptance returns fail, it should also send back a minimal rework task for
`执行区`, not only a problem list.

### 2. `issues.md` needs a live summary block

Put this at the top of `issues.md`:

- Current phase
- Current recommended next task
- Latest accepted slice
- Open blockers
- Last updated

Below that, keep the full chronological log. Agents should scan the summary
first, then read only the relevant latest entry.

### 3. `key_facts.md` must stay stable

Split it mentally into two categories:

- stable facts: paths, ports, commands, bundle IDs, environment variable names
- last verified environment: short, dated, drift-prone facts

Do not let `key_facts.md` turn into a work-progress ledger.

### 4. Standardize compact evidence

Each execution entry in `issues.md` should prefer:

- Changed
- Verified
- Manual
- Scope skipped

This keeps the log searchable without turning each entry into a report.

### 5. Prompts should reference stable docs, not restate them

Zone opening prompts should point to stable docs by path and only add
this-turn context. Repeating the full rulebook in every task card wastes tokens.

### 6. Ultra-lean startup profile

After bootstrap, default every zone to this startup read set only:

- `AGENTS.md` or `CLAUDE.md` workflow section
- `docs/project_notes/zone_operating_model.md`
- `docs/project_notes/key_facts.md`
- `docs/project_notes/issues.md` Current Summary plus the latest relevant block

Add these only on demand:

- `docs/project_notes/current_task.md` when the active task or Acceptance Contract is parked there
- `docs/project_notes/decisions.md` before workflow or architecture changes
- `docs/project_notes/bugs.md` before debugging a likely-known issue
- `docs/product_consensus/...` before product or strategy behavior changes
- `docs/architecture.md` before boundary or dependency changes
- `docs/implementation-plan.md` before phase or gate changes

Do not reread the packaged skill files during ordinary project work unless the
workflow itself is being revised.

### 7. Planning outputs must be copy-ready

Planning should choose the smallest transfer shape that safely fits the work.

- For simple, small work, give `执行区` a short task card directly in the reply.
  Do not default to a handoff doc, and do not default to a separate `验收区`
  task.
- For medium or risky work, default to paired low-overlap artifacts:
  - execution task
  - execution evidence report template
  - acceptance contract
  - acceptance review task
- Use a handoff doc only for more complex work. When a handoff doc is used,
  end the reply with direct paste targets instead of only linking the doc.
- Always include the absolute handoff-doc path and a short prompt for `执行区`
  when a handoff doc is used.
- When a handoff doc is used for complex work, default to including a second
  short prompt for `验收区` in the same reply.
- Keep `issues.md` minimal: current recommended next task plus a short decision
  summary. Do not store paste-ready prompts there.
- For long-running multi-phase projects, prefer a single
  `docs/project_notes/current_task.md` active task surface over a growing task-card
  archive. Overwrite it for each new task; store only summaries and evidence in
  `issues.md`.
- When `current_task.md` is the active task surface, Planning's chat reply should
  not repeat the full task card. End with short paste-ready prompts that point
  `执行区` or `验收区` to `current_task.md` and name the task ID.
- Every execution task card must be specific enough that `执行区` does not need
  to invent strategy, product behavior, runtime choice, storage design, or
  other unresolved user decisions.

### 8. Activate only the zones you need

Do not wake all four zones for every slice.

- trivial, low-risk, clear work: one active working zone plus at most one short handoff
- medium or risky work: Planning plus Execution, and Acceptance when review is in scope
- Maintenance: only when Git state, environment state, dependencies, or runtime hygiene are actually part of the task

Symmetry is not a goal. Lower context load is.

### 9. No silent execution decisions

Planning should explicitly mark items that remain under Planning control, such
as:

- runtime or framework choice
- storage design
- additional product rules
- phase deliverables or gates not yet agreed

If execution hits one of these, it should stop and route back instead of
silently choosing.

## Bootstrap Procedure

1. Inspect the repo for existing docs and workflow rules.
2. Create `docs/project_notes/` if missing.
3. Seed the files from this skill's `references/`.
4. For greenfield or under-specified projects, also seed:
   - `docs/product_consensus/...`
   - `docs/architecture.md`
   - `docs/implementation-plan.md`
5. Merge the AGENTS/CLAUDE workflow section into the project's existing files.
6. Initialize Git if the workspace is not already a repository.
7. Create four zone threads automatically: `规划区`, `执行区`, `验收区`, `维护区`.
8. Send each zone its opening prompt so the user does not have to create or prime the zones manually.
9. Customize project-specific read order and safety rules.
10. Add one bootstrap entry to `issues.md`.
11. Stop. Do not invent extra files, roles, or ceremony unless the project needs them.

## Git Bootstrap Default

Use the smallest useful Git setup:

- initialize with `git init -b main` when `.git/` is missing
- create a minimal `.gitignore` only when the file is missing
- do not invent remotes, hooks, CI, branching strategies, or commit history
- record the Git status in `key_facts.md` or `issues.md`

If the user asks for more, that can be a separate step.

## Zone Auto-Creation Default

When the app supports thread creation or forking, this skill should create four
zone threads automatically and send each one a short opening message that:

- states its zone responsibility
- tells it which project-note files to read first
- tells it what it must not do
- asks it to start with a concise status or next step

Default opening intent by zone:

- `规划区`: clarify goals, constraints, options, and acceptance criteria before execution
- `执行区`: implement the assigned slice, gather evidence, and respect scope
- `验收区`: judge pass/fail only, do not edit code
- `维护区`: inspect Git, environment, dependencies, runtime, and workspace hygiene

Use these exact Chinese zone names by default when the skill auto-creates them:

- `规划区`
- `执行区`
- `验收区`
- `维护区`

Do not auto-create English-named zone threads unless the user explicitly asks.

## File Rules

### `bugs.md`

- Log only resolved or recurring bugs.
- Capture issue, root cause, solution, and prevention.
- Skip one-off noise that teaches nothing.

### `decisions.md`

- Store durable ADRs and workflow decisions.
- Update an existing ADR when the decision changes; do not let conflicting decisions pile up.

### `key_facts.md`

- Store only non-secret facts.
- Prefer durable paths, commands, URLs, and conventions.
- Keep the environment subsection short and dated.

### `issues.md`

- Put the live summary first.
- Use the chronological log for plans, execution evidence, acceptance outcomes, maintenance notes, and blockers.
- When updating, touch only the relevant latest entry when possible.
- Keep detailed task cards and paste-ready prompts out of this file; record concise task intent, changed files, evidence, blockers, and acceptance outcomes instead.
- Keep the Current Summary short enough that a new zone can read it quickly without paying for a mini project-history replay.

### `current_task.md` optional

- Use only when a project has enough phases or cross-thread handoffs that an active task file saves tokens.
- Store the current execution task, Acceptance Contract, or acceptance task only.
- Overwrite it when the next task starts.
- Do not preserve detailed historical prompts here; history belongs in `issues.md` as concise summaries and evidence.
- `执行区` should read this file for the active assignment plus only the listed supporting files.
- `验收区` should read the current Acceptance Contract here plus the latest matching evidence block in `issues.md` and the current diff.

### `zone_operating_model.md`

- Define zone responsibilities and boundaries.
- Keep the standard card formats here, including execution evidence and acceptance review shapes.
- Keep this file short enough that agents can reread it quickly.

### `docs/product_consensus/...`

- Record confirmed behavior and locked non-goals.
- Also list unresolved product decisions that execution must not make silently.

### `docs/architecture.md`

- Record required module boundaries and dependency direction.
- Keep the first version small and concrete.

### `docs/implementation-plan.md`

- Record phase deliverables, verification, and gates.
- Make the phase gates explicit so later slices do not start early.

## Output Shapes

### Execution task card

```text
Goal:
Out of scope:
Read first:
Deliver:
Edit targets:
Execution self-check:
Stop if:
```

### Acceptance Contract

```text
Task ID:
Goal:
Must not do:
Required checks:
Key risks:
Review input: Acceptance Contract + execution evidence + current diff
```

### Execution evidence report

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

### Acceptance review task

```text
Goal:
Read first:
Review input:
Focus checks:
Do not repeat:
Output:
```

### Maintenance handoff

```text
Status:
Evidence:
Risk:
Route to:
Three-line handoff:
```

## Anti-Patterns

Do not ship these into a new project:

- making `issues.md` the only source of current truth with no summary block
- mixing stable facts with drifting progress in `key_facts.md`
- forcing a full Acceptance pass on every trivial slice
- repeating stable rules in every task card
- growing a long task-card archive when a single overwritten `current_task.md` would do
- making execution invent runtime, storage, or new product rules because planning left them implicit
- sending acceptance the full execution prompt when a contract plus evidence would do
- creating more zones, files, or roles before there is a real need
