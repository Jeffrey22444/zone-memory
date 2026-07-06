---
name: zone-memory
description: Bootstraps a reusable multi-zone collaboration system and project memory baseline for coding projects. Use when starting a new project or when the user wants Planning, Execution, Acceptance, and Maintenance zones plus lightweight project memory docs.
---

# Zone Memory

Use this skill to set up a lean project operating system:

- Planning / Execution / Acceptance / Maintenance zones
- `docs/project_notes/` memory files
- optional tracked `docs/product_consensus/...`, `docs/architecture.md`, and `docs/implementation-plan.md`
- `AGENTS.md` and `CLAUDE.md` protocols
- Chinese zone naming by default
- Codex auto-creation of the four zones when thread tools are available
- manual fallback for non-Codex agents
- low-token handoffs and short acceptance contracts

## Quick Start

1. Inspect existing `AGENTS.md`, `CLAUDE.md`, `docs/`, and project conventions.
2. Create or update:
   - `docs/project_notes/bugs.md`
   - `docs/project_notes/decisions.md`
   - `docs/project_notes/key_facts.md`
   - `docs/project_notes/issues.md`
   - `docs/project_notes/zone_operating_model.md`
3. For greenfield or under-specified projects, also create or update:
   - `docs/product_consensus/...`
   - `docs/architecture.md`
   - `docs/implementation-plan.md`
4. Add or merge the workflow section from [references/agents_section.md](references/agents_section.md).
5. Seed the project-note files from `references/`.
6. If running in Codex with thread creation support, automatically create four work zones and send each one its opening prompt:
   - `规划区`
   - `执行区`
   - `验收区`
   - `维护区`
7. If not running in Codex, return manual setup steps plus four copy-ready opening prompts from [references/opening_prompts.md](references/opening_prompts.md).
8. Log the bootstrap in `docs/project_notes/issues.md`.

## Defaults

- Keep stable rules in `AGENTS.md`, `CLAUDE.md`, and `zone_operating_model.md`, not in every prompt.
- Keep `issues.md` two-layered: current summary first, chronological log below.
- Keep `key_facts.md` stable-facts-first; drift-prone items go in a short "Last Verified Environment" section.
- Every execution task gets a short Acceptance Contract.
- A separate Acceptance pass is required only for risky, user-critical, or explicitly requested work.
- Name the four zones in Chinese by default: `规划区`, `执行区`, `验收区`, `维护区`.
- Use the shortest artifact that safely carries the work.
- On the first invocation, always ensure the user gets four opening prompts, either by automatic thread seeding or by copy-ready manual output.

## Workflow

1. Read [REFERENCE.md](REFERENCE.md).
2. Copy the templates under `references/`.
3. Customize read order, product docs, commands, and safety rules for the project.
4. If the project lacks authoritative behavior, architecture, or phase docs, seed tracked docs for product consensus, architecture, and implementation phases.
5. Merge with any existing workflow system instead of replacing it wholesale.
6. In Codex, prefer automatic zone creation plus auto-sent opening prompts.
7. Outside Codex, do not claim zones were created. Instead, tell the user exactly how to create four chats or threads manually and provide the four prompts inline.
8. Keep the diff minimal; do not add extra zones or files unless the project actually needs them.

## Portability Notes

- Codex and Claude can both use the same Markdown templates and workflow rules.
- In Codex, this skill should auto-create the four zones when the thread tools exist.
- Outside Codex, this skill should fall back to manual setup and return four copy-ready opening prompts on first use.
- The portable contract is the file layout and behavior boundaries, not a specific app integration.

## References

- [REFERENCE.md](REFERENCE.md)
- [references/agents_section.md](references/agents_section.md)
- [references/product_consensus_template.md](references/product_consensus_template.md)
- [references/architecture_template.md](references/architecture_template.md)
- [references/implementation_plan_template.md](references/implementation_plan_template.md)
- [references/zone_operating_model_template.md](references/zone_operating_model_template.md)
- [references/opening_prompts.md](references/opening_prompts.md)
