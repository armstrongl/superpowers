# Skill research and plan: brainstorming (evals)

> **Scope note:** This is an improvement task, not a new skill. The brainstorming skill already exists
> and is production-ready. This document plans the addition of a structured eval suite to the existing
> skill. Changes are additive only — no existing behavior is modified.

---

# Part 1: research

## Research questions

1. What are best practices for structuring LLM skill/agent eval scenarios (format, inputs, assertions)?
2. How can behavioral compliance be verified in multi-step LLM workflows (checklist order, gate enforcement)?
3. What grader agent patterns produce reliable pass/fail verdicts on semi-structured outputs?
4. What assertion strategies work for outputs that are partially subjective (design documents)?
5. How should an eval suite be organized across files for maintainability and reuse?

## User requirements

Requirements gathered through structured interviews before research began. Every answer is documented
verbatim.

### Round 1: eval scope and format

- **What should the evals verify?:** Checklist order, HARD-GATE, Output quality, Transition behavior
- **How should the evals be run?:** Automated assertions
- **Where should the evals live?:** Rename + restructure (rename eval/ → evals/, restructure with
  separate files per eval scenario)

### Round 2: output and structure

- **What should the automated grader produce?:** Pass/Fail per eval (with reason why it passed or
  failed)
- **How should eval test prompts be structured?:** Scenario files (one .md file per scenario with a
  system prompt, user input, and expected behavior description)

## Domain classification

**Type:** Technical/engineering.

**Reasoning:** This task involves implementing an LLM evaluation framework using specific tools,
file formats, and agent patterns. It does not involve scientific research or psychological methodology
— it is a software engineering task with well-defined implementation patterns.

## Source summary

| Source | Type | Tier | Grade | Key contribution |
| --- | --- | --- | --- | --- |
| [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | Engineering blog | 3 | A | Core eval structure (task/trial/grader/transcript), pass/fail criteria design, behavioral compliance via transcript reading |
| [Promptfoo — Test case configuration](https://www.promptfoo.dev/docs/configuration/test-cases/) | Official docs | 1 | A | Test case file format, assertion structure, CSV/YAML/JSON scenario formats |
| [Promptfoo — LLM Rubric](https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/llm-rubric/) | Official docs | 1 | A | Model-graded assertions, pass/fail JSON structure `{reason, score, pass}`, rubric criteria writing |
| `better-skill-creator/references/eval-system.md` | Internal reference | 1 | A | Canonical eval format for this project: evals/evals.json manifest, workspace structure, eval_metadata.json schema |
| `better-skill-creator/agents/grader.md` | Internal reference | 1 | A | Grader agent pattern: transcript reading, pass/fail evidence format, grading.json schema |

## Thematic findings

### Theme 1: eval structure — scenario-based testing with a manifest

According to [Anthropic engineering](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents),
an eval is fundamentally: "give an AI an input, then apply grading logic to its output to measure
success." For multi-step agents, the key is evaluating the **transcript** (the full record of tool
calls and reasoning), not the final output alone. Scenarios should be discrete, independently
executable tests with defined success criteria.

The better-skill-creator eval system (`eval-system.md`) defines
the canonical format for this project: `evals/evals.json` as the machine-readable manifest with
`{skill_name, evals: [{id, prompt, expected_output, files}]}`. Each eval also gets an
`eval_metadata.json` in the workspace with its assertions.

### Theme 2: grader patterns — LLM-as-judge for behavioral compliance

[Promptfoo's llm-rubric](https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/llm-rubric/)
produces `{reason, score, pass}` — exactly matching the user's requirement for "pass/fail per eval
with reason." The better-skill-creator grader (`agents/grader.md`) extends
this with a transcript-reading step: read the full execution transcript, examine output files, then
evaluate each assertion with specific evidence cited.

For behavioral compliance evals (checklist order, HARD-GATE), the grader must search the transcript
for **order of events** — whether something happened, and when it happened relative to
other steps.

### Theme 3: assertion quality — specific, observable, discriminating

The [Anthropic eval blog](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
defines a good eval as one where "two domain experts would independently reach the same pass/fail
verdict." The better-skill-creator eval system distinguishes good
assertions ("The output file is valid JSON", "Context explored before first question") from weak
ones ("The output is good").

For the brainstorming skill specifically:

- **Good**: "Context exploration messages appear before the first clarifying question in the transcript"
- **Good**: "No code blocks appear in the transcript before a user approval message"
- **Weak**: "The design looks thorough"

### Theme 4: file organization — scenario files supplement the machine-readable manifest

[Promptfoo's configuration](https://www.promptfoo.dev/docs/configuration/parameters/) supports
`.md`, `.yaml`, `.json`, and `.csv` formats for test scenarios. Human-readable scenario `.md` files
serve as specification documents describing the test intent, while `evals.json` serves the
machine-readable format. These are complementary, not redundant.

## Conflicts and resolutions

No significant conflicts identified among sources. The internal better-skill-creator format is
authoritative for this project and is consistent with industry patterns.

## Research limitations

- Limited research on behavioral compliance assertions specifically for conversational workflow skills
  (most LLM eval literature focuses on task completion, not conversation structure).
- The brainstorming grader must evaluate conversation **ordering** from a transcript — this is a
  less-studied pattern than output quality evaluation.

## Planning inputs

**Domain analysis signals:**

- Claude knows general LLM eval concepts but not the brainstorming-specific behavioral criteria
  (what constitutes checklist order compliance, HARD-GATE violation, complete design doc).
- The better-skill-creator eval format is authoritative for this project and must be followed exactly
  — Claude needs it explicitly rather than inventing a format.
- Behavioral compliance requires transcript-reading, not output inspection alone — this is an
  under-documented pattern in LLM eval literature.

**Requirements signals:**

- 4 eval dimensions: checklist order, HARD-GATE enforcement, output quality, transition behavior.
- Format: scenario `.md` files (one per scenario) + `evals/evals.json` manifest.
- Grader output: pass/fail per assertion with a reason string.
- Directory rename: `eval/` → `evals/`.

**Scope signals:**

- In scope: 4 eval scenarios for the 4 selected dimensions; specialized brainstorming grader agent;
  populated `evals.json` manifest.
- Out of scope: CI/CD integration, promptfoo integration, visual companion evals, performance/timing
  evals.
- The `agents/brainstorming-agent.md` and `SKILL.md` require only minor updates (adding grader
  reference to the agent index in SKILL.md).

---

*Research checkpoint: research sections above are complete and ready for review.*

---

# Part 2: plan

## Problem statement

The brainstorming skill has a well-defined 9-step workflow, a HARD-GATE against premature
implementation, required design document sections, and a strict transition to `writing-plans`. There
is no eval suite to verify these behavioral properties — the existing `eval/evals.json` is empty.
This plan adds a populated eval suite with 4 scenario files, a specialized grader agent, and
renames `eval/` → `evals/` to align with the better-skill-creator system.

## Skill metadata

- **Name:** `brainstorming`
- **Description:** `Use when starting any creative work — creating features, building components, adding functionality, or modifying behavior — before any implementation begins.`

## Domain analysis

What Claude already knows (omit from skill content):

- General LLM eval concepts (pass/fail, grader agents, assertions).
- How to read a conversation transcript and look for patterns.
- JSON file formats and markdown file formats.
- What "checklist order" means generically.

What Claude needs to be told (include in skill/grader content):

- The specific 9-step brainstorming checklist and what compliance looks like for each step.
- What a HARD-GATE violation looks like in a transcript (code blocks before approval message).
- What sections a brainstorming design doc must contain (architecture, components, data flow, error
  handling, testing).
- What "correct transition behavior" means (writing-plans invoked; no frontend-design, mcp-builder,
  or other implementation skills).
- The grading.json schema required by the better-skill-creator eval system.
- What constitutes a "user approval message" for HARD-GATE and transition purposes.

## Scope boundaries

In scope:

- Rename `eval/` → `evals/` directory.
- Populate `evals/evals.json` with 4 test scenarios.
- Create `evals/scenarios/` with one `.md` file per scenario.
- Create `agents/brainstorming-grader.md` specialized for brainstorming behavioral evals.
- Update `SKILL.md` agent index to reference the new grader.

Out of scope:

- Changes to any existing skill behavior (SKILL.md content, brainstorming-agent.md process).
- CI/CD automation for running evals.
- Visual companion evals.
- Promptfoo or other external eval framework integration.
- Performance/timing assertions.
- Changes to `agents/spec-document-reviewer.md`.

## Degrees of freedom

**Level:** Low.

**Rationale:** The eval format is defined by the better-skill-creator system (evals.json schema,
grading.json schema, eval_metadata.json schema). The grader output format is fixed. The scenario
file structure is specified by the user (system prompt, user input, expected behavior). Deviation
from these formats would break integration with the eval runner. The brainstorming criteria
(checklist, HARD-GATE, required sections) are defined by the existing SKILL.md. This is a
deterministic implementation task with minimal judgment needed.

## Architecture pattern

**Pattern:** Hybrid (existing skill + eval additions).

**Rationale:** The brainstorming skill already has a complete architecture (SKILL.md, agent,
scripts, references, assets). The eval additions follow the better-skill-creator pattern:
`evals/evals.json` manifest + scenario files + specialized grader agent. No new reference files
needed — the grader agent carries all the brainstorming-specific criteria inline.

## File manifest

| File path | Purpose | Estimated size | Load trigger |
| --- | --- | --- | --- |
| `SKILL.md` | Core workflow, checklist, visual companion, reference index | 260 lines | Skill activation. |
| `agents/brainstorming-agent.md` | Primary agent for independent execution | 155 lines | Agent delegation, eval runs. |
| `agents/spec-document-reviewer.md` | Subagent template for spec review loop | 50 lines | Step 7 of brainstorming process. |
| `agents/brainstorming-grader.md` | Specialized grader for brainstorming behavioral evals | 80 lines | When grading brainstorming eval runs. |
| `scripts/fetch_resources.py` | Fetches latest reference content from official sources | 60 lines | Before major revisions. |
| `scripts/start-server.sh` | Start the visual companion server | 40 lines | Visual companion activation. |
| `scripts/stop-server.sh` | Stop the visual companion server | 20 lines | After visual companion session. |
| `scripts/server.js` | Visual companion Node.js server | 200 lines | Started by start-server.sh. |
| `scripts/helper.js` | Client-side helper script injected into served pages | 60 lines | Injected by server.js. |
| `references/visual-companion.md` | Full visual companion guide | 200 lines | When user accepts visual companion offer. |
| `references/fetch-references.md` | When and how to run the fetch script | 30 lines | When updating reference content. |
| `assets/frame-template.html` | HTML frame template with CSS theme and mock elements | 150 lines | Visual companion page generation. |
| `evals/evals.json` | Machine-readable eval manifest with 4 scenarios | 40 lines | When running the eval suite. |
| `evals/scenarios/01-checklist-order.md` | Scenario: 9-step checklist is followed in sequence | 40 lines | Human reference when running or reviewing evals. |
| `evals/scenarios/02-hard-gate.md` | Scenario: no code written before design is approved | 40 lines | Human reference when running or reviewing evals. |
| `evals/scenarios/03-design-doc-quality.md` | Scenario: spec contains all required sections | 40 lines | Human reference when running or reviewing evals. |
| `evals/scenarios/04-transition-behavior.md` | Scenario: writing-plans invoked, no implementation skills | 40 lines | Human reference when running or reviewing evals. |

## Fetchable sources configuration

No fetchable sources identified for the eval additions. The brainstorming skill's existing
`scripts/fetch_resources.py` is already configured for its reference sources. The grader and
scenario files carry all needed criteria inline.

## Eval strategy

**Output type:** Mixed (behavioral compliance is objectively verifiable; design doc quality has
verifiable structural properties with a subjective quality dimension).

**Rationale:** Checklist order, HARD-GATE compliance, and transition behavior can be verified by
reading a transcript and checking for the presence/absence/ordering of specific events. Design doc
quality can be partially automated (section presence, file existence, git commit) with subjective
quality left to human review.

**Recommended approach:** Structured evals with assertions for the 4 verifiable dimensions.
Assertions are evaluated by `agents/brainstorming-grader.md` reading the execution transcript.

Verifiable assertions per scenario:

| Scenario | Assertion | Check type |
| --- | --- | --- |
| Checklist order | Context exploration appears before first clarifying question | Transcript ordering |
| Checklist order | Only one question per agent message during clarification phase | Transcript content |
| Checklist order | 2-3 approaches proposed before design is presented | Transcript ordering |
| HARD-GATE | No code blocks appear before a user approval message | Transcript content |
| HARD-GATE | No implementation files created before design approval | Output files check |
| Design doc quality | Spec file exists at `docs/supapowers/specs/YYYY-MM-DD-*-design.md` | File existence |
| Design doc quality | Spec contains architecture section | File content |
| Design doc quality | Spec contains components section | File content |
| Design doc quality | Spec contains data flow section | File content |
| Design doc quality | Spec contains error handling section | File content |
| Design doc quality | Spec contains testing section | File content |
| Transition behavior | writing-plans skill invoked after design approval | Transcript content |
| Transition behavior | No other implementation skills invoked (frontend-design, mcp-builder, etc.) | Transcript content |

## Agent design

**Primary agent:** `agents/brainstorming-agent.md`

**Scope:** Leads a complete brainstorming session independently from initial idea to approved spec.
Receives `task` and `project_dir` as inputs, produces a committed spec document as output. Already
implemented; no changes needed.

**Additional agents:**

- `agents/spec-document-reviewer.md` — Reviews spec completeness and consistency. Already
  implemented; no changes needed.
- `agents/brainstorming-grader.md` — **New.** Specialized grader for brainstorming evals. Receives
  a transcript path, outputs directory, and list of expectations. Evaluates behavioral compliance
  assertions against the transcript and returns `grading.json` in the better-skill-creator format.
  Carries brainstorming-specific criteria inline: the 9-step checklist, HARD-GATE definition,
  required spec sections, and valid vs. invalid transition targets.

## SKILL.md outline

The existing SKILL.md requires only one addition: a `brainstorming-grader.md` entry in the Agent
index section. No other changes to the 260-line SKILL.md body.

```text
## Agent index (current)
| brainstorming-agent.md    | Primary agent: leads a full brainstorming session |
| spec-document-reviewer.md | Subagent prompt template: reviews spec completeness |

## Agent index (after)
| brainstorming-agent.md    | Primary agent: leads a full brainstorming session |
| spec-document-reviewer.md | Subagent prompt template: reviews spec completeness |
| brainstorming-grader.md   | Eval grader: verifies behavioral compliance in eval runs |
```

Estimated SKILL.md size after change: ~265 lines (unchanged at functional level).

## Reference file details

No new reference files. The grader carries all brainstorming-specific criteria inline to keep
it self-contained and avoid the need to load references during eval runs.

## Script details

No new scripts. The existing `scripts/fetch_resources.py` is already configured.

## Asset details

No new assets.

## Dependencies

- `better-skill-creator` eval system format (evals.json, eval_metadata.json, grading.json schemas).
- Existing brainstorming skill structure (unchanged).

## Integration

- **Upstream:** User invokes the brainstorming skill on a task, producing a transcript and spec doc.
- **Downstream:** `better-skill-creator` Phase 4 eval runner consumes `evals/evals.json` and
  dispatches the grader agent.
- **Complementary:** `better-skill-creator` grader.md (the new brainstorming-grader follows the
  same format and can be used as a drop-in replacement for brainstorming evals).

## Verification criteria

1. `evals/evals.json` is valid JSON with 4 eval entries, each having `id`, `prompt`,
   `expected_output`, and `files` fields.
2. Each `evals/scenarios/*.md` file exists and contains scenario title, trigger input, expected
   behavior description, and assertions list.
3. `agents/brainstorming-grader.md` can be invoked as a subagent and produces `grading.json` in the
   correct schema (expectations array with `text`, `passed`, `evidence` fields; summary with
   `passed`, `failed`, `total`, `pass_rate`).
4. `SKILL.md` agent index includes the `brainstorming-grader.md` entry.
5. `evals/` directory exists; `eval/` directory does not exist.
6. `validate_plan.py` passes with 0 errors.

## Open questions

None.
