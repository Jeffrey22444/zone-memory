# Example Bootstrap Flow

## When to use this skill

Use it when a project needs:

- reusable Planning / Execution / Acceptance / Maintenance boundaries
- persistent project memory across agent sessions
- low-token handoffs instead of verbose prompts

## Typical flow

1. Read the project's current `AGENTS.md`, `CLAUDE.md`, and `docs/`.
2. Create `docs/project_notes/`.
3. Copy and customize the templates from `references/`.
4. Merge the workflow section into the project's `AGENTS.md`.
5. If `CLAUDE.md` exists, mirror the memory protocol there.
6. Add one bootstrap entry to `docs/project_notes/issues.md`.

## Expected result

The project ends up with:

- one standard place for memory
- one standard place for zone boundaries
- cheap execution evidence
- acceptance that stays independent without duplicating execution work
- fewer repeated prompt tokens on future tasks
