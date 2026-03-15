# Reference sources

Reference documents for the subagent-driven-development skill. Run
`scripts/fetch_resources.py` to pull the latest content from each source.

## Sources

### Azure AI agent design patterns

- **File:** `azure-agent-design-patterns.md`
- **URL:** <https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns>
- **Description:** Microsoft Azure reference covering sequential, routing, handoff,
  and hierarchical agent orchestration patterns with architectural guidance.

### OpenAI Multi-Agent orchestration

- **File:** `openai-multi-agent-orchestration.md`
- **URL:** <https://openai.github.io/openai-agents-python/multi_agent/>
- **Description:** OpenAI Agents SDK guide to multi-agent coordination — handoffs,
  agents-as-tools, and delegation patterns relevant to subagent dispatch workflows.

### LangChain: how and when to build Multi-Agent systems

- **File:** `langchain-when-to-use-multi-agent.md`
- **URL:** <https://blog.langchain.com/how-and-when-to-build-multi-agent-systems/>
- **Description:** Decision-oriented guidance on when multi-agent architectures are
  appropriate, covering task decomposition, parallelism, and specialization trade-offs.

## Refreshing references

```bash
python scripts/fetch_resources.py
```

Run this before major skill revisions or when reference content feels outdated.
