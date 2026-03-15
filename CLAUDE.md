# supapowers — Plugin Development Guide

This is the supapowers Claude Code plugin: a composable skills library for structured
AI-assisted development workflows.

## Project Structure

```text
skills/          # One folder per skill — SKILL.md + agents/ + references/
commands/        # Slash command definitions
hooks/           # Plugin hook definitions and runner
agents/          # Shared agent definitions
tests/           # Test suites by platform (claude-code, opencode, etc.)
docs/            # Community-visible documentation and plans
.claude/         # AI assistant work products (audits, plans, specs)
.claude-plugin/  # Claude Code plugin manifest
.cursor-plugin/  # Cursor plugin manifest
.opencode/       # OpenCode integration
.codex/          # Codex integration
```

## Key Conventions

### Versioning

All four manifests must stay in sync. When bumping the version:

- `.claude-plugin/plugin.json`
- `.claude-plugin/marketplace.json`
- `.cursor-plugin/plugin.json`
- `gemini-extension.json`

### Adding a Skill

Follow `skills/writing-skills/SKILL.md` exactly. Every skill needs:

1. `skills/<name>/SKILL.md` — the skill content
2. `skills/<name>/agents/<name>-agent.md` — delegated agent version
3. `skills/<name>/references/fetch-references.md` — reference loader

### Markdown

Run `rumdl` on every `.md` file you create or edit.

### Plans and Specs

- AI work products (audits, plans, reflections) → `.claude/`
- Community-visible docs (install guides, design docs) → `docs/`

### Testing

Use TDD. Tests live in `tests/` organized by platform. Run existing tests before
adding new skills or changing skill behavior.

## Development Workflow

1. Brainstorm the skill design
2. Write failing tests
3. Implement the skill
4. Verify tests pass
5. Run rumdl on all changed `.md` files
6. Bump version across all four manifests if it's a release
