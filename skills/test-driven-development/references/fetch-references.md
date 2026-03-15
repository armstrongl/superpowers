# Fetch references

This document explains when and how to run `scripts/fetch_resources.py` to pull fresh content from the authoritative TDD sources configured in the script.

## When to run

Run the fetch script when:

- Reference files feel outdated or links in SKILL.md seem stale.
- Preparing for a major revision of the skill.
- A source URL has been updated and you want to capture current content.

## How to run

From the skill root directory:

```bash
python scripts/fetch_resources.py
```

The script saves fetched content into `references/` and prints a summary of what changed.

## Sources

| Filename | URL | Description |
| --- | --- | --- |
| `martinfowler-tdd.md` | <https://martinfowler.com/bliki/TestDrivenDevelopment.html> | Martin Fowler's canonical TDD bliki entry: the red-green-refactor cycle and principles. |
| `kent-beck-canon-tdd.md` | <https://tidyfirst.substack.com/p/canon-tdd> | Kent Beck's "Canon TDD" post clarifying the authoritative methodology directly from its creator. |
| `tdd-mooc-chapter1.md` | <https://tdd.mooc.fi/1-tdd/> | TDD MOOC Chapter 1: structured academic introduction to the discipline. |

## Notes

- The script uses only Python stdlib — no dependencies to install.
- Files already in `references/` that have not changed are left untouched (hash comparison).
- If a fetch fails, the script exits with a non-zero status and lists the failed URLs.
- Fetched files are not committed to the repository. They are reference snapshots for local use.
