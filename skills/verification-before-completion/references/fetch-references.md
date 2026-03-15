# Fetch references

The `scripts/fetch_resources.py` script pulls current documentation from
authoritative external sources and saves the results to this `references/`
directory.

## When to run

Run the fetch script before:

- A major revision of `SKILL.md` or any technique reference
- Reference content feels stale or out of date
- Adding new sources to keep in sync with upstream documentation

## How to run

From the skill root directory:

```sh
python scripts/fetch_resources.py
```

No external dependencies are required. The script uses Python's standard
library only.

## What it fetches

The script is configured with three authoritative sources:

| File | Source |
| ------ | -------- |
| `atlassian-definition-of-done.md` | Atlassian guide to Definition of Done in Agile |
| `agile-alliance-definition-of-done.md` | Agile Alliance glossary entry on Definition of Done |
| `code-review-verification-checklist.md` | Augment Code: 40 verification questions before approving a code review |

## Adding sources

Edit the `SOURCES` list in `scripts/fetch_resources.py`. Each entry needs:

- `url` - The page to fetch
- `filename` - Where to save it under `references/`
- `description` - Optional note on what the source provides

## Output

The script prints a summary of new, updated, unchanged, and failed fetches.
It exits with a non-zero status if any source fails so CI pipelines can
detect problems.
