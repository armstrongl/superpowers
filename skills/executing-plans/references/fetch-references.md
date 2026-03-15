# Fetching references

The `scripts/fetch_resources.py` script pulls the latest content from authoritative sources on
implementation plan execution and project management. Run it to keep reference material current.

## When to run

- **Before a major skill revision.** Ensure reference content reflects current best practices
  before making changes to SKILL.md or the agent.
- **When guidance feels outdated.** If the references mention tools or patterns that seem stale,
  fetch fresh versions.
- **Periodically.** Project management practices evolve; refresh references every few months.
- **After installing the skill.** Bundled references reflect a point in time; fetching ensures
  you start with current content.

## How to run

From the skill's root directory:

```bash
python scripts/fetch_resources.py
```

The script will:

1. Iterate through its configured `SOURCES` list.
2. Fetch each URL.
3. Extract the readable text content.
4. Write (or overwrite) the corresponding file in `references/`.
5. Print a summary of what was fetched, what failed, and what changed.

## Sources fetched

| File | Source | What it provides |
| --- | --- | --- |
| `implementation-plan-guide.md` | Asana | Components, steps, and best practices for implementation plans. |
| `project-execution-guide.md` | Smartsheet | Expert guide to project execution, monitoring, and control. |
| `program-implementation-guide.md` | ProjectManager.com | Program implementation guide with templates. |

## Error handling

The script handles errors per source. If one URL fails (network error, 404, access denied), the
remaining sources still get fetched. The summary at the end reports which sources succeeded and
which failed, so you can investigate individually.

## No dependencies required

The script uses only Python stdlib (`urllib`, `html.parser`). Nothing to install.
