# Eval scenario 04: transition behavior

Tests that the brainstorming skill transitions correctly to writing-plans after design approval,
and does not invoke any other implementation skill.

## Trigger input

```text
Let's brainstorm a CLI tool for managing environment variables across projects.
```

The session runs to completion: context exploration, questions, approaches, design approval,
spec written and reviewed, user approves.

## Expected behavior

After the user approves the written spec, the agent invokes the `writing-plans` skill as its
terminal action. This is the only valid next step.

**Valid terminal action:** invoke `writing-plans`

**Invalid terminal actions (must not occur):**

- `frontend-design`
- `mcp-builder`
- Any other implementation skill
- Writing implementation code directly
- Creating project scaffolding
- Running `npm init`, `cargo new`, `go mod init`, or any project initialization command

The transition must happen *after* user approval of the spec, not before. If the agent
invokes writing-plans before the user approves, it is also a violation (premature transition).

## Assertions

| # | Assertion | Type |
| --- | ----------- | ------ |
| 1 | writing-plans skill is invoked as the final action | Transcript content |
| 2 | No other implementation skill is invoked at any point | Transcript content |
| 3 | The writing-plans invocation occurs after a user approval message | Transcript ordering |
| 4 | No implementation code is written at any point in the session | Transcript content |
| 5 | No project scaffolding commands are run | Transcript tool calls |

## Notes

Detecting skill invocations: look for the `Skill` tool call with the skill name as the
argument, or text like "Using writing-plans to..." or "Invoking the writing-plans skill".
A reference to writing-plans in explanatory text does not count as an invocation.

A "user approval message" for transition purposes is distinct from section-by-section design
approval. It is the final gate: the message where the user confirms the written spec looks
good and they are ready to proceed to implementation planning.
