# Fetch references

Reference documents for the `requesting-code-review` skill are fetched from authoritative sources using the fetch script.

## How to refresh

```bash
python scripts/fetch_resources.py
```

Run this command from the skill root directory before major skill revisions or when reference content feels outdated.

## Sources

| File | Source | Description |
| ------ | -------- | ------------- |
| `google-eng-practices-review-intro.md` | <https://google.github.io/eng-practices/review/> | Google Engineering Practices: Code Review introduction |
| `google-eng-practices-what-to-look-for.md` | <https://google.github.io/eng-practices/review/reviewer/looking-for.html> | Google Engineering Practices: What to look for in a code review |
| `google-eng-practices-author-guide.md` | <https://google.github.io/eng-practices/review/developer/> | Google Engineering Practices: The CL author's guide to getting through code review |

## Why these sources

**Google Engineering Practices** (<https://google.github.io/eng-practices/>) is the canonical public reference for large-scale code review process. It covers:

- What reviewers should look for (design, functionality, complexity, tests, naming, comments, style)
- The standard of code review: continuous improvement over perfection
- How authors should respond to and handle review feedback
- Conflict resolution and escalation paths

These documents directly inform the review checklist in `agents/code-reviewer.md` and the orchestration logic in `agents/requesting-code-review-agent.md`.

## Additional reference

The following sources were consulted during skill design but are not fetched automatically:

- LinearB code review checklist guide: <https://linearb.io/blog/code-review-checklist>
- GitKraken code review best practices: <https://www.gitkraken.com/blog/code-review-best-practices-2024>
