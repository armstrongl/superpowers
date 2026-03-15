# Fetching references

Every skill includes a `scripts/fetch_resources.py` script that pulls the latest content from official sources. This keeps the skill's reference material current without manual updates.

## When to run

Run `fetch_resources.py` in these situations:

- **Before a major skill revision.** Ensure reference content reflects the latest upstream documentation before making changes.
- **When something feels outdated.** If a reference file mentions APIs, tools, or patterns that seem stale, fetch the latest versions.
- **Periodically.** For skills that depend on evolving documentation (e.g., GitHub Docs), run the fetch script as part of routine maintenance.
- **After installing or updating this skill.** The bundled references may have been written at a point in time. Fetching ensures you start with current content.

## How to run

From the skill's root directory:

```bash
python scripts/fetch_resources.py
```

The script will:

1. Iterate through its configured `SOURCES` list.
2. Fetch each URL.
3. Extract readable text from the HTML.
4. Write (or overwrite) the corresponding file in `references/`.
5. Print a summary of what was fetched, what failed, and what changed.

## Sources configured for this skill

| Filename | Source URL | Description |
| --- | --- | --- |
| `git-branching-workflows.md` | <https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows> | Official Git documentation on branching workflows |
| `git-basic-branching-and-merging.md` | <https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging> | Official Git documentation on basic branching and merging |
| `github-flow.md` | <https://docs.github.com/en/get-started/using-github/github-flow> | GitHub Flow: lightweight branch-based PR workflow |
| `github-merge-methods.md` | <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/configuring-pull-request-merges/about-merge-methods-on-github> | GitHub merge commit, squash, and rebase methods |

## How it works

The `SOURCES` list at the top of `fetch_resources.py` defines what to fetch. Each entry is a dictionary with:

- `url`: The source URL to fetch.
- `filename`: Where to save it in `references/` (relative to the skill root).
- `description` (optional): What this source provides.

The script uses only Python stdlib (`urllib`, `html.parser`) so there are no dependencies to install.

## Error handling

The script handles errors per-source. If one URL fails (network error, 404, access denied), the remaining sources still get fetched. The summary at the end reports which sources succeeded and which failed, so you can investigate individually.

## Adding new sources

Edit the `SOURCES` list in `scripts/fetch_resources.py` and add a new entry:

```python
{
    "url": "https://example.com/relevant-docs",
    "filename": "relevant-docs.md",
    "description": "What this source covers.",
},
```

Good candidates for this skill:

- Git merge strategy documentation (`git-scm.com/docs/merge-strategies`)
- GitHub CLI PR creation reference (`cli.github.com/manual/gh_pr_create`)
- Atlassian Git tutorials on branching strategies
