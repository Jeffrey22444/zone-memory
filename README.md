# Zone Memory Skill

`Zone Memory` is a portable skill pack that bootstraps a lean multi-zone way of
working for coding projects:

- Planning / Execution / Acceptance / Maintenance zones
- `docs/project_notes/` memory files
- `AGENTS.md` and `CLAUDE.md` workflow rules
- short task cards and low-token handoffs

This package is designed to work for Codex, Claude Code, and similar agents.
The core value is the workflow and templates, but this package now defines one
platform-specific behavior clearly:

- Codex: auto-create the four zones and auto-send the four opening prompts
- non-Codex agents: return manual setup steps plus four copy-ready opening prompts

## Repository Layout

- `skills/zone-memory`: installable skill payload
- `install.py`: install into Codex and/or Claude skill directories
- `build_release.py`: build a ZIP release artifact
- `tests/test_delivery.py`: small delivery check

## Install From A Local Checkout

```bash
python3 install.py --agent codex
python3 install.py --agent claude
python3 install.py --agent both
```

Preview without writing:

```bash
python3 install.py --agent both --dry-run
```

Upgrade an existing install:

```bash
python3 install.py --agent both --upgrade
```

## Install From GitHub Repo

```bash
git clone https://github.com/Jeffrey22444/zone-memory.git
cd zone-memory
python3 install.py --agent both
```

Recommended per-agent commands:

```bash
git clone https://github.com/Jeffrey22444/zone-memory.git
cd zone-memory
python3 install.py --agent codex
```

```bash
git clone https://github.com/Jeffrey22444/zone-memory.git
cd zone-memory
python3 install.py --agent claude
```

If the target agent does not support local skill installation, copy the files
under `skills/zone-memory` into that agent's equivalent prompt or skill
directory, or reuse the Markdown files directly in your project.

## How To Use

1. Install the skill.
2. In a project, invoke `zone-memory`.
3. Let the agent inspect the repo and seed:
   - `docs/project_notes/bugs.md`
   - `docs/project_notes/decisions.md`
   - `docs/project_notes/key_facts.md`
   - `docs/project_notes/issues.md`
   - `docs/project_notes/zone_operating_model.md`
4. Merge the workflow section into the project's `AGENTS.md` or `CLAUDE.md`.
5. If you are in Codex, the agent should create these four zones automatically:
   - `规划区`
   - `执行区`
   - `验收区`
   - `维护区`
6. If you are not in Codex, create four chats or threads manually with those exact names, then paste the matching opening prompts from `skills/zone-memory/references/opening_prompts.md`.

## Manual Setup For Non-Codex Agents

If the agent cannot create threads or chats for you:

1. Open four separate chats, threads, or saved prompts.
2. Name them exactly:
   - `规划区`
   - `执行区`
   - `验收区`
   - `维护区`
3. Paste the matching opening prompt from `skills/zone-memory/references/opening_prompts.md` into each one.
4. Keep using those four zones for the same project instead of opening fresh ad hoc chats each time.

## First-Run Behavior

- In Codex, first run should create the four zones and send the four opening prompts automatically.
- Outside Codex, first run should return the four opening prompts inline, so the user can paste them manually.

## Recommended Distribution

Use the GitHub repository itself as the primary delivery unit.

- Users clone the repo
- Users run `python3 install.py --agent codex` or `--agent claude`
- No extra package manager is required

## Design Choices

- Portable core, Codex adapter behavior
- Standard library only
- Minimal install contract
- Templates stay plain Markdown so they can be copied without tooling

## License

MIT. See [LICENSE.txt](LICENSE.txt).
