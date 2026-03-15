---
description: Execute a written implementation plan step by step with review checkpoints, task tracking, and verification. Use when the user has a plan file ready to implement, says "execute this plan," "implement this plan," "run this plan," or "start on this plan." Prefer supapowers:subagent-driven-development when subagents are available.
name: executing-plans
---

# Executing plans

Load a plan, review it critically, execute all tasks with verification, and hand off to the
finishing workflow when done.

**Announce at start:** "I'm using the executing-plans skill to implement this plan."

**Note:** This skill works best on platforms with subagent support (Claude Code, Codex). If
subagents are available, consider `supapowers:subagent-driven-development` instead — it provides
higher-quality parallel execution.

## The process

### Step 1: load and review the plan

1. Read the plan file.
2. Review critically — check for:
   - Ambiguous or underspecified instructions.
   - Missing prerequisites or dependencies.
   - Verification steps that reference things that do not exist yet.
   - Anything that would prevent starting task 1.
3. If concerns exist: list them and stop. Raise them with your human partner before starting.
4. If no concerns: create a task tracking list and proceed.

### Step 2: prepare the workspace

1. Confirm you are on the correct working branch (not `main` or `master` unless explicitly
   authorized).
2. Confirm the working directory state is clean or that any uncommitted changes are intentional.
3. Complete any environment setup steps the plan specifies.

### Step 3: execute tasks

For each task, in order:

1. Mark as `in_progress`.
2. Read the task description and all subtasks.
3. Execute each subtask exactly as written. Do not improvise.
4. Run the verification steps the plan specifies for this task.
5. If verification passes: mark as `completed` and continue.
6. If verification fails: diagnose the failure. If the fix is clear and low-risk, apply it
   and re-verify once. If still failing or the fix is unclear, stop — report the failure with
   full context and wait for guidance.

If a task depends on a previous task that failed or was skipped, do not continue. Report the
dependency issue.

### Step 4: complete development

After all tasks are completed and verified:

- Announce: "I'm using the finishing-a-development-branch skill to complete this work."
- **Required sub-skill:** Use `supapowers:finishing-a-development-branch`.
- Follow that skill to verify tests, present options, and execute the chosen action.

## When to stop and ask for help

Stop executing immediately when:

- A blocker appears: missing dependency, failing test, unclear instruction.
- The plan has critical gaps that prevent starting the next task.
- Verification fails repeatedly and the cause is not clear.

When stopping, report: which task failed, the exact error or ambiguity, what you already tried,
and what information you need to proceed. Vague reports delay resolution.

Ask for clarification rather than guessing. Guessing and executing the wrong thing is harder
to undo than pausing.

## When to revisit earlier steps

Return to the review in Step 1 when:

- Your human partner updates the plan based on your feedback.
- A blocker reveals that the fundamental approach needs rethinking.

Do not force through blockers.

## Checklist

- [ ] Plan loaded and reviewed critically.
- [ ] Workspace confirmed on correct branch.
- [ ] All tasks executed in order with verifications.
- [ ] Plan-level verifications passed.
- [ ] `finishing-a-development-branch` invoked.

## Remember

- Review the plan critically before starting — catch problems before they cost execution time.
- Follow plan steps exactly — the plan was written with specific intent.
- Skip no verifications — they exist to catch specific failure modes.
- Invoke referenced skills when the plan says to — do not replicate their logic inline.
- Never start implementation on `main`/`master` without explicit user consent.

## Integration

| Skill | Role |
| --- | --- |
| `supapowers:using-git-worktrees` | Required: set up isolated workspace before starting. |
| `supapowers:writing-plans` | Creates the plan this skill executes. |
| `supapowers:finishing-a-development-branch` | Required: complete development after all tasks. |

## Reference and script index

| Reference | Load when |
| --- | --- |
| `references/fetch-references.md` | Before running `scripts/fetch_resources.py`. |

| Agent | Purpose |
| --- | --- |
| `agents/executing-plans-agent.md` | Primary agent for independent plan execution. |

| Script | Usage |
| --- | --- |
| `scripts/fetch_resources.py` | Fetch latest reference content for this skill. |
