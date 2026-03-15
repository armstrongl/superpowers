# Fetch references

When and how to run the fetch script for the `using-git-worktrees` skill.

## When to run

Run `scripts/fetch_resources.py` in these situations:

- Before a major revision of this skill, to ensure reference content reflects the latest git-worktree behavior.
- When git releases a new version and you suspect command flags or behavior have changed.
- When the fetched reference files feel stale (older than a few months).
- After adding a new source to the SOURCES list in `scripts/fetch_resources.py`.

You do not need to run this script during normal skill use. The fetched references are supplementary context for skill improvement, not runtime requirements.

## How to run

From the skill root directory:

```bash
python scripts/fetch_resources.py
```

The script saves fetched content to `references/` using the filenames configured in its SOURCES list. It skips files whose content has not changed (hash comparison) and reports a summary at the end.

## Sources

| File | Source URL | What it provides |
| --- | --- | --- |
| `git-worktree-official.md` | <https://git-scm.com/docs/git-worktree> | Official git-scm documentation: all subcommands, flags, and behavior. |
| `git-worktree-kernel.md` | <https://www.kernel.org/pub/software/scm/git/docs/git-worktree.html> | Kernel.org man page: low-level reference for edge cases and flags. |
| `git-worktree-best-practices.md` | <https://www.datacamp.com/tutorial/git-worktree-tutorial> | Best practices for parallel development workflows including AI agent patterns. |

## Load these references when

- `git-worktree-official.md`: Any time you need exact syntax for `git worktree add`, `prune`, `remove`, `repair`, `lock`, or `move`.
- `git-worktree-kernel.md`: When debugging unexpected worktree behavior or verifying a flag's exact semantics.
- `git-worktree-best-practices.md`: When advising on directory structure, cleanup workflows, or multi-agent parallelism patterns.
