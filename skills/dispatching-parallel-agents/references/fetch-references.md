# Fetch references

Run `scripts/fetch_resources.py` to pull fresh copies of official documentation into this directory.

## Sources

| File | Source | Description |
| ------ | -------- | ------------- |
| `claude-code-agent-teams.md` | [Claude Code Docs](https://code.claude.com/docs/en/agent-teams) | Official Claude Code documentation on agent teams and parallel orchestration. |
| `anthropic-multi-agent-research-system.md` | [Anthropic Engineering](https://www.anthropic.com/engineering/multi-agent-research-system) | How Anthropic built their multi-agent research system — orchestrator-worker patterns and prompt engineering lessons. |
| `azure-ai-agent-design-patterns.md` | [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) | Microsoft's guide to AI agent orchestration patterns including fan-out/fan-in and supervisor patterns. |

## Usage

```bash
python scripts/fetch_resources.py
```

Fetched files are saved to `references/` and overwrite existing content only when changes are detected. Run before major skill revisions.
