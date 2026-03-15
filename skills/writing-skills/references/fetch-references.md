# Fetch references

Run `scripts/fetch_resources.py` to pull fresh copies of official documentation into this directory.

## Sources

| File | Source | Description |
| ------ | -------- | ------------- |
| `anthropic-best-practices.md` | [Anthropic Docs](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/best-practices) | Official skill authoring best practices from Anthropic. |
| `anthropic-skills-overview.md` | [Anthropic Docs](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview) | Official skills overview and conceptual background. |

## Manually maintained

| File | Description |
| ------ | ------------- |
| `testing-skills-with-subagents.md` | Complete methodology for RED-GREEN-REFACTOR testing of skills using subagents. |
| `persuasion-principles.md` | Research-backed persuasion principles (Cialdini, Meincke et al.) for designing effective discipline skills. |
| `graphviz-conventions.dot` | Style conventions for Graphviz diagrams used in skill flowcharts. |

## Usage

```bash
python scripts/fetch_resources.py
```

Fetched files are saved to `references/` and overwrite existing content only when changes are detected. Run before major skill revisions.
