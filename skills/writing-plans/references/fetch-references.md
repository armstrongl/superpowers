# Writing plans: reference sources

Authoritative references for implementation planning, task decomposition, and TDD methodology.
Run `scripts/fetch_resources.py` to download current versions of these resources.

## Sources

### TDD - martin fowler

- **URL:** <https://martinfowler.com/bliki/TestDrivenDevelopment.html>
- **File:** `references/tdd-martinfowler.md`
- **Covers:** Red-Green-Refactor cycle, task decomposition as a core TDD practice,
  atomic test design, minimal implementation discipline.

### Implementation plan guide - ProjectManager

- **URL:** <https://www.projectmanager.com/blog/implementation-plan>
- **File:** `references/implementation-plan-guide.md`
- **Covers:** Key components of an implementation plan (goal, scope, tasks, milestones,
  resources, risk management), step-by-step structure, success criteria definition.

### Work breakdown structure - workbreakdownstructure.com

- **URL:** <https://www.workbreakdownstructure.com/>
- **File:** `references/work-breakdown-structure.md`
- **Covers:** Hierarchical task decomposition (WBS), deliverable-oriented breakdown,
  Agile WBS patterns (epics to stories to tasks), progressive elaboration.

## Key concepts from research

### Task decomposition (TDD)

Kent Beck's formulation: break each large task into several smaller tasks in priority order.
Each small cycle completes one task — a separate task might be as small as changing a variable
name. Decomposition forces focus on limited content and keeps code under proper control.

### WBS best practices

- Start with clear scope; identify major deliverables before decomposing further.
- Each element must be formulated with concrete, measurable terms.
- Avoid over-decomposition: 3-4 levels maximum.
- Use deliverable-oriented decomposition rather than activity-based planning.
- Keep the WBS updated iteratively as requirements evolve.

### Implementation plan components

An implementation plan must include: goal/scope, task breakdown, file/component ownership,
success criteria, verification steps, and a communication/handoff mechanism.
