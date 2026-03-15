# Eval scenario 01: checklist order

Tests that the brainstorming skill follows its 9-step checklist in sequence.
Steps must occur in the correct order — later steps must not precede earlier ones.

## Trigger input

```text
I want to add real-time notifications to my web app.
```

## Expected behavior

1. **Context exploration** (step 1) — agent reads project files, recent commits, and existing
   docs *before* asking any clarifying question.
2. **Visual companion offer** (step 2, conditional) — if visual questions are anticipated, this
   offer appears as its own message with no other content. Skipped if not applicable.
3. **Clarifying questions** (step 3) — questions asked one at a time, never multiple in one
   message. Questions focus on purpose, constraints, and success criteria.
4. **Approach proposals** (step 4) — 2–3 distinct approaches presented with trade-offs and a
   recommendation *before* any design content is written.
5. **Design presentation** (step 5) — design presented in sections, one section at a time.
   User asked to confirm each section before the next is presented.
6. **Spec document written** (step 6) — spec saved to
   `docs/supapowers/specs/YYYY-MM-DD-<topic>-design.md` and committed to git.
7. **Spec review loop** (step 7) — spec-document-reviewer subagent dispatched; issues fixed
   and re-dispatched until approved (max 5 iterations).
8. **User review gate** (step 8) — user asked to review the spec before proceeding.
9. **Transition** (step 9) — writing-plans skill invoked as the final action.

## Assertions

| # | Assertion | Type |
| --- | ----------- | ------ |
| 1 | Context exploration occurs before the first clarifying question | Transcript ordering |
| 2 | No more than one question appears per agent message during the clarification phase | Transcript content |
| 3 | At least two distinct approaches are proposed before any design content is presented | Transcript ordering |
| 4 | Design sections are presented before the spec document is written | Transcript ordering |
| 5 | No code is written at any point in the session | Transcript content |

## Notes

The grader must check **ordering** in the transcript, not presence alone. An agent that asks
questions and explores context but does so in the wrong order fails this eval even if all steps
eventually complete.

The "one question per message" assertion fails if a message contains more than one `?` in the
clarifying question phase, unless the extras are clearly rhetorical or embedded in quoted text.
