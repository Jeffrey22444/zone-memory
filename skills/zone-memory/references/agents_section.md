## Project Memory And Zone Workflow

### Read Order

Use progressive disclosure. Read only what is needed for the current task.

1. Read this file first.
2. Read `docs/project_notes/zone_operating_model.md`.
3. Read `docs/project_notes/key_facts.md` before assuming commands, paths, ports, or conventions.
4. Read `docs/product_consensus/...` before discussing or changing product or strategy behavior.
5. Read `docs/architecture.md` before changing module boundaries, data flow, or dependency direction.
6. Read `docs/implementation-plan.md` before sequencing phases, deliverables, or verification gates.
7. Search `docs/project_notes/bugs.md` before debugging familiar errors.
8. Read `docs/project_notes/decisions.md` before proposing workflow or architecture changes.
9. Scan the current summary and relevant latest entry in `docs/project_notes/issues.md` when starting or handing off work.

### Project Memory System

This project keeps institutional knowledge in `docs/project_notes/`.

- `bugs.md`: resolved or recurring bugs with causes and fixes
- `decisions.md`: durable architectural or workflow decisions
- `key_facts.md`: non-secret stable project facts plus a short last-verified environment section
- `issues.md`: current-state summary plus chronological work log
- `zone_operating_model.md`: zone responsibilities, boundaries, and standard card shapes

### Memory Protocol

- Before proposing architecture or workflow changes, check `docs/project_notes/decisions.md`.
- Before debugging an error, search `docs/project_notes/bugs.md`.
- Before assuming project configuration, check `docs/project_notes/key_facts.md`.
- Update `docs/project_notes/issues.md` with meaningful work progress and completion notes.
- When resolving a reusable bug, add or update `docs/project_notes/bugs.md`.
- When making or changing a durable decision, add or update `docs/project_notes/decisions.md`.
- Do not store secrets, tokens, passwords, private keys, credential JSON, or credential values in project notes.

### Zone Defaults

- Planning discusses goals, constraints, risks, options, and acceptance criteria before execution.
- Execution implements only clearly assigned work, uses the smallest working change, and gathers evidence.
- Acceptance reviews only, returns pass/fail plus findings, and does not modify code.
- Maintenance inspects Git, environment, dependencies, runtime state, and mainline hygiene.

### Zone Identity And Boundaries

- Each agent must keep track of the active zone and stay inside that zone's responsibilities.
- If the active zone is unclear, stop and ask the user to confirm it before doing substantive work.
- A zone must not silently take over another zone's job.
- Planning must not perform Acceptance or Maintenance work unless explicitly reassigned.
- Execution must not redesign scope, perform final acceptance, or manage Git history unless explicitly assigned.
- Acceptance must not edit code or docs.
- Maintenance must not design product behavior or implement feature code.

### Acceptance Routing Rule

Every execution task gets a short Acceptance Contract. A separate Acceptance pass is required only for risky, user-critical, or explicitly requested work.

### Editing Rules

- Keep changes small and localized.
- Prefer existing code, standard library, native platform features, and existing dependencies.
- Do not add abstractions, services, factories, dependencies, or broad refactors without a current concrete need.
- Do not revert user changes or unrelated workspace changes.
