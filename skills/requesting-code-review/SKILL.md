---
description: Use when completing tasks, implementing major features, or before merging to verify work meets requirements
name: requesting-code-review
---

# Requesting code review

Dispatch `supapowers:code-reviewer` subagent to catch issues before they cascade. The reviewer gets precisely crafted context for evaluation — never your session's history. This keeps the reviewer focused on the work product, not your thought process, and preserves your own context for continued work.

**Core principle:** Review early, review often.

## When to request review

**Mandatory:**

- After each task in subagent-driven development
- After completing major feature
- Before merge to main

**Optional but valuable:**

- When stuck (fresh perspective)
- Before refactoring (baseline check)
- After fixing complex bug

## How to request

**1. Get git SHAs:**

```bash
BASE_SHA=$(git rev-parse HEAD~1)  # or origin/main
HEAD_SHA=$(git rev-parse HEAD)
```

**2. Dispatch code-reviewer subagent:**

Use Task tool with `supapowers:code-reviewer` type, fill template at `agents/code-reviewer.md`.

**Placeholders:**

- `{WHAT_WAS_IMPLEMENTED}` - What was built
- `{PLAN_OR_REQUIREMENTS}` - What it should do
- `{BASE_SHA}` - Starting commit
- `{HEAD_SHA}` - Ending commit
- `{DESCRIPTION}` - Brief summary

**3. Act on feedback:**

- Fix Critical issues immediately
- Fix Important issues before proceeding
- Note Minor issues for later
- Push back if reviewer is wrong (with reasoning)

## Example

```text
[Just completed Task 2: Add verification function]

You: Let me request code review before proceeding.

BASE_SHA=$(git log --oneline | grep "Task 1" | head -1 | awk '{print $1}')
HEAD_SHA=$(git rev-parse HEAD)

[Dispatch supapowers:code-reviewer subagent]
  WHAT_WAS_IMPLEMENTED: Verification and repair functions for conversation index
  PLAN_OR_REQUIREMENTS: Task 2 from docs/supapowers/plans/deployment-plan.md
  BASE_SHA: a7981ec
  HEAD_SHA: 3df7661
  DESCRIPTION: Added verifyIndex() and repairIndex() with 4 issue types

[Subagent returns]:
  Strengths: Clean architecture, real tests
  Issues:
    Important: Missing progress indicators
    Minor: Magic number (100) for reporting interval
  Assessment: Ready to proceed

You: [Fix progress indicators]
[Continue to Task 3]
```

## Integration with workflows

**Subagent-Driven Development:**

- Review after EACH task
- Catch issues before they compound
- Fix before moving to next task

**Executing Plans:**

- Review after each batch (3 tasks)
- Get feedback, apply, continue

**Ad-Hoc Development:**

- Review before merge
- Review when stuck

## Red flags

**Never:**

- Skip review because "it's trivial"
- Ignore Critical issues
- Proceed with unfixed Important issues
- Argue with valid technical feedback

**If reviewer is wrong:**

- Push back with technical reasoning
- Show code/tests that prove it works
- Request clarification

## File index

### Agents

| File | Purpose |
| ------ | --------- |
| `agents/requesting-code-review-agent.md` | Primary orchestration agent: gathers context, dispatches reviewer, surfaces feedback |
| `agents/code-reviewer.md` | Reviewer subagent prompt template: performs the actual code review |

### Scripts

| File | Purpose |
| ------ | --------- |
| `scripts/fetch_resources.py` | Fetches reference documents from Google Engineering Practices and other authoritative sources |

### References

| File | Purpose |
| ------ | --------- |
| `references/fetch-references.md` | Index of reference sources and instructions for refreshing them |

### Evals

| File | Purpose |
| ------ | --------- |
| `eval/evals.json` | Evaluation suite for this skill (currently empty, to be populated) |
