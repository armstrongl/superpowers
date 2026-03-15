# Eval scenario 03: design doc quality

Tests that the written spec document contains all five required sections and is saved to
the correct path.

## Trigger input

```text
I want to add user authentication with email and password to my Express API. Let's brainstorm this.
```

## Expected behavior

After the full brainstorming session (context, questions, approaches, design), the agent writes
a spec document containing all required sections. The document is saved to the correct path
pattern and committed to git.

**Required spec sections** (all five must be present):

1. **Architecture** — overall system structure, components and how they relate, key design
   decisions.
2. **Components** — individual pieces that make up the system, their responsibilities, and
   interfaces.
3. **Data flow** — how data moves through the system: request lifecycle, state changes,
   async operations.
4. **Error handling** — failure modes, error responses, edge cases, and how they are managed.
5. **Testing** — test strategy: what is unit-tested, what is integration-tested, and how
   the implementation is validated.

**Required path pattern:** `docs/supapowers/specs/YYYY-MM-DD-<topic>-design.md`

The spec must be committed to git after writing.

## Assertions

| # | Assertion | Type |
| --- | ----------- | ------ |
| 1 | Spec file exists at path matching `docs/supapowers/specs/*-design.md` | File existence |
| 2 | Spec contains an architecture section (heading or content) | File content |
| 3 | Spec contains a components section | File content |
| 4 | Spec contains a data flow section | File content |
| 5 | Spec contains an error handling section | File content |
| 6 | Spec contains a testing section | File content |
| 7 | Spec was committed to git (git log shows the spec file in a recent commit) | Git log |

## Notes

Section detection: look for markdown headings (`##`, `###`) or prominent paragraph labels
containing the section keywords. Acceptable variations:

- "Architecture" / "System architecture" / "Architecture overview"
- "Components" / "Component design" / "Key components"
- "Data flow" / "Request flow" / "Data model and flow"
- "Error handling" / "Errors" / "Error cases"
- "Testing" / "Test strategy" / "Testing approach"

A section counts as present if its heading appears AND the section has substantive content
(more than one line). An empty section heading does not pass.
