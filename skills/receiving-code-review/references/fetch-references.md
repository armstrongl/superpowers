# Fetch references

This skill includes a script that fetches updated reference content from authoritative sources on code review practices.

## When to run

Run `scripts/fetch_resources.py` when:

- Preparing a major revision of the skill.
- The sourced guides feel outdated or reference stale tooling.
- You want to verify the current upstream guidance from Google Engineering Practices.

## What it fetches

| Source | Output file | Content |
| --- | --- | --- |
| Google Eng Practices: Handling Comments | `references/google-eng-practices-handling-comments.md` | Google's guidance for authors on how to handle reviewer comments, seek clarification, and respond to disagreement |
| Google Eng Practices: Handling Pushback | `references/google-eng-practices-handling-pushback.md` | Google's guidance on how reviewers and authors should navigate pushback situations |
| Code Review Guidelines for Humans | `references/code-review-guidelines-for-humans.md` | Practical principles for giving and receiving code review feedback with technical rigour |

## How to run

```bash
python scripts/fetch_resources.py
```

The script requires no external dependencies — it uses only the Python standard library. Run it from the skill root directory or any directory; it resolves paths relative to the script location.

## After fetching

Review fetched content before using it. The pages are saved as plain text extracted from HTML. Check that:

- The Google Engineering Practices pages still reflect current guidance (they are updated occasionally).
- The content covers the situations described in `SKILL.md` and the agent definition.

Fetched files supplement but do not replace `SKILL.md` or the agent definition.
