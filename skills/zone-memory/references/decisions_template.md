# Architectural Decisions

Use this file for durable ADRs. Check it before planning or changing architecture or workflow.

### ADR-001: Establish Project Memory And Zone Workflow (YYYY-MM-DD)

**Context:**

- The project needs shared memory across sessions and tools.
- The project benefits from separated planning, execution, acceptance, and maintenance work.

**Decision:**

- Use `AGENTS.md` plus `docs/project_notes/` as the shared workflow and memory system.
- Keep task artifacts short by default.
- Require a short Acceptance Contract on every execution task.
- Require a separate Acceptance pass only for risky, user-critical, or explicitly requested work.

**Alternatives Considered:**

- No shared workflow -> rejected because handoffs drift too easily.
- A heavier framework with more files and roles -> rejected because it adds overhead before the project earns it.

**Consequences:**

- Agents have one standard place to look for memory and boundaries.
- The process stays small enough to reread quickly.
- The system can evolve through later ADRs when the project proves a need.

## Security

Do not store secrets, tokens, passwords, private keys, credential JSON, or credential values here.
