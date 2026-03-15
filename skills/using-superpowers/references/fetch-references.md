# Fetch references

This document explains when and how to run `scripts/fetch_resources.py` to
refresh the reference files in this directory.

## When to run

Run the fetch script when:

- Reference files feel outdated (the Agent Skills specification has been
  updated, Claude Code docs have changed, etc.).
- You are about to do a major revision of `SKILL.md` and want current source
  material.
- A reference file is missing and needs to be populated for the first time.
- More than 30 days have passed since the last fetch.

Do not run the script during normal skill use. Reference files are read by
agents on demand; they do not need to be live.

## How to run

From the skill root directory:

```bash
python scripts/fetch_resources.py
```

The script requires no external dependencies. It uses only Python standard
library modules (`urllib`, `html.parser`, `hashlib`, `pathlib`).

## What it fetches

| Output file | Source URL |
| ------------- | ------------ |
| `agentskills-specification.md` | <https://agentskills.io/specification> |
| `claude-code-skills.md` | <https://code.claude.com/docs/en/skills> |
| `claude-api-agent-skills-overview.md` | <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview> |

## Output

The script prints a summary of new, updated, unchanged, and failed fetches.
If any fetch fails, it exits with a non-zero status code so CI can detect
failures.

Updated files are written to `references/` with a source comment header so
you can always trace where the content came from.

## Adding or changing sources

Edit the `SOURCES` list at the top of `scripts/fetch_resources.py`. Each
entry requires `url` and `filename`; `description` is optional.
