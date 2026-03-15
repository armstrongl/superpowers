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
| `elastic-root-cause-analysis.md` | Elastic comprehensive RCA guide |
| `cisco-devops-rca-guide.md` | Cisco DevNet DevOps RCA in application monitoring |
| `softwaretestinghelp-rca-guide.md` | Software Testing Help RCA steps and techniques |

## Adding sources

Edit the `SOURCES` list in `scripts/fetch_resources.py`. Each entry needs:

- `url` - The page to fetch
- `filename` - Where to save it under `references/`
- `description` - Optional note on what the source provides

## Output

The script prints a summary of new, updated, unchanged, and failed fetches.
It exits with a non-zero status if any source fails so CI pipelines can
detect problems.
