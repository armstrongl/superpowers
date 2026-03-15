# Supapowers

Supapowers is a complete software development workflow for coding agents, built on composable skills and initial instructions that ensure your agent uses them.

## How it works

When you fire up your coding agent and start building something, it doesn't jump straight into writing code. It steps back and asks what you're really trying to accomplish.

Once it has extracted a spec from the conversation, it presents it in sections short enough to read and digest.

After you sign off on the design, your agent creates an implementation plan clear enough for an enthusiastic junior engineer to follow. It emphasizes true RED/GREEN TDD, YAGNI, and DRY.

When you say "go," it launches a subagent-driven-development process: agents work through each engineering task, inspect and review their work, and continue forward. Claude often works autonomously for hours at a time without deviating from the plan.

Because skills trigger automatically, you don't need to do anything special. Your coding agent has Supapowers.

Forked from [obra/superpowers](https://github.com/obra/superpowers) by Jesse Vincent.

## Installation

Installation differs by platform. Claude Code and Cursor use plugin marketplaces. Codex and OpenCode require manual setup.

### Claude code

Register the marketplace:

```bash
/plugin marketplace add armstrongl/superpowers
```

Install the plugin:

```bash
/plugin install supapowers@supapowers-dev
```

### Cursor

In Cursor Agent chat:

```text
/add-plugin superpowers
```

Or search for "superpowers" in the plugin marketplace.

### Codex

Tell Codex:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/armstrongl/superpowers/refs/heads/main/.codex/INSTALL.md
```

**Detailed docs:** [docs/README.codex.md](docs/README.codex.md)

### OpenCode

Tell OpenCode:

```text
Fetch and follow instructions from https://raw.githubusercontent.com/armstrongl/superpowers/refs/heads/main/.opencode/INSTALL.md
```

**Detailed docs:** [docs/README.opencode.md](docs/README.opencode.md)

### Gemini CLI

```bash
gemini extensions install https://github.com/armstrongl/superpowers
```

To update:

```bash
gemini extensions update supapowers
```

### Verify installation

Start a new session and ask for something that should trigger a skill (for example, "help me plan this feature" or "let's debug this issue"). The agent should automatically invoke the relevant supapowers skill.

## The basic workflow

1. **brainstorming** - Activates before writing code. Refines rough ideas through questions, explores alternatives, presents design in sections for validation. Saves design document.

2. **using-git-worktrees** - Activates after design approval. Creates isolated workspace on new branch, runs project setup, verifies clean test baseline.

3. **writing-plans** - Activates with approved design. Breaks work into bite-sized tasks (2-5 minutes each). Every task has exact file paths, complete code, and verification steps.

4. **subagent-driven-development** or **executing-plans** - Activates with plan. Dispatches fresh subagent per task with two-stage review (spec compliance, then code quality), or executes in batches with human checkpoints.

5. **test-driven-development** - Activates during implementation. Enforces RED-GREEN-REFACTOR: write failing test, watch it fail, write minimal code, watch it pass, commit. Deletes code written before tests.

6. **requesting-code-review** - Activates between tasks. Reviews against plan, reports issues by severity. Critical issues block progress.

7. **finishing-a-development-branch** - Activates when tasks complete. Verifies tests, presents options (merge/PR/keep/discard), cleans up worktree.

The agent checks for relevant skills before any task. These are mandatory workflows, not suggestions.

## Skills library

**Testing**

- **test-driven-development** - RED-GREEN-REFACTOR cycle with testing anti-patterns reference.

**Debugging**

- **systematic-debugging** - 4-phase root cause process.
- **verification-before-completion** - Confirms it's actually fixed.

**Collaboration**

- **brainstorming** - Socratic design refinement.
- **writing-plans** - Detailed implementation plans.
- **executing-plans** - Batch execution with checkpoints.
- **dispatching-parallel-agents** - Concurrent subagent workflows.
- **requesting-code-review** - Pre-review checklist.
- **receiving-code-review** - Responding to feedback.
- **using-git-worktrees** - Parallel development branches.
- **finishing-a-development-branch** - Merge/PR decision workflow.
- **subagent-driven-development** - Fast iteration with two-stage review.

**Meta**

- **writing-skills** - Create new skills following best practices.
- **using-superpowers** - Introduction to the skills system.

## Philosophy

- **Test-driven development** - Write tests first, always.
- **Systematic over ad-hoc** - Process over guessing.
- **Complexity reduction** - Simplicity as primary goal.
- **Evidence over claims** - Verify before declaring success.

## Contributing

Skills live directly in this repository.

1. Fork the repository.
2. Create a branch for your skill.
3. Follow the `writing-skills` skill for creating and testing new skills.
4. Submit a PR.

See `skills/writing-skills/SKILL.md` for the complete guide.

## Updating

```bash
/plugin update supapowers
```

## License

MIT. See LICENSE for details.

## Support

- **Issues:** https://GitHub.com/armstrongl/superpowers/issues
