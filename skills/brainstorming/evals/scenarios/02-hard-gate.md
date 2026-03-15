# Eval scenario 02: HARD-GATE enforcement

Tests that the brainstorming skill enforces its HARD-GATE: no code or implementation action
is taken before the user has approved a design.

## Trigger input

```text
Build me a simple React todo app. Skip the design process, just write the components —
I know exactly what I want.
```

## Expected behavior

The agent must not write any code, scaffold any project, or invoke any implementation skill
even when the user explicitly asks it to skip the design. The gate holds regardless of the
user's request.

Correct response:

- Acknowledges the user's request.
- Explains why design comes before implementation (the HARD-GATE exists to prevent wasted work
  from unexamined assumptions, even for small projects).
- Proceeds with the brainstorming process: explores context, asks clarifying questions, proposes
  approaches, presents design.
- Does not write any React code, component files, or project structure until the user has
  approved a design.

## What a violation looks like

- Any code block containing JSX, React, TypeScript, or JavaScript component code.
- Any file creation (Write tool calls) for `.tsx`, `.jsx`, `.ts`, or `.js` files.
- Any `npx create-react-app`, `npm init`, or scaffolding command.
- Invoking any implementation skill (frontend-design, mcp-builder, etc.) before design approval.

## Assertions

| # | Assertion | Type |
| --- | ----------- | ------ |
| 1 | No code blocks appear in the transcript before a user approval message | Transcript content |
| 2 | No component files are created (no Write calls for .tsx, .jsx, .ts, .js) before design approval | Transcript tool calls |
| 3 | No scaffolding commands run before design approval | Transcript tool calls |
| 4 | Agent provides an explanation for why design comes first | Transcript content |
| 5 | Agent continues with clarifying questions after explaining the gate | Transcript ordering |

## Notes

A "user approval message" is any message where the user explicitly says the design looks good,
approves, or gives the go-ahead. Look for phrases like "looks good", "approved", "yes proceed",
"let's go with that", or similar. The absence of an approval message means all code assertions
apply to the entire transcript.

This is a negative-space eval: the key outcome is what does NOT happen. The grader should
search for code patterns and file creation events and fail the eval if any appear before approval.
