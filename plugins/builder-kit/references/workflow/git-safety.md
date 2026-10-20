# Git Safety

Inspect branch, status, upstream, and relevant diff before editing.

Preserve all unrelated staged, unstaged, and untracked work. If ownership is uncertain, stop or use a clean isolated worktree; never discard, reset, overwrite, stage, stash, or absorb it merely to proceed.

Use one coherent workstream per branch/PR:

- start independent work from a current base on a semantic branch;
- continue an existing PR on its head branch;
- do not create a branch for every message in one workstream.

Before publishing, require authorization and confirm the branch/head/upstream, outgoing commits, intended diff, base freshness, and that relevant checks plus the closest feasible production-like build pass. If a check/build is infeasible, document the limitation and closest available evidence. Prefer non-rewriting history for published branches.

Deleting or merging a branch/PR requires explicit authorization for the resolved source and target. Prefer recoverable, non-force operations.
