# Git Safety

Inspect branch, status, upstream, and relevant diff before editing.

When uncommitted changes exist, explain plainly: the project contains changes not yet saved in a commit and they may belong to other work. Ask how the user wants to protect them. If the user does not know, inspect and preserve them, avoid overlapping files, and prefer a clean isolated branch/worktree or another recoverable separation. Never discard, reset, overwrite, stage, or absorb unrelated changes.

Use one coherent workstream per branch/PR:

- new independent feature, fix, conversation workstream, or change of track: create a semantic branch from a current base;
- existing PR/workstream: continue its branch;
- do not create a new branch for every message.

Before pushing, confirm only intended changes are included, relevant focused checks pass, the closest local production-like build passes when feasible, and base conflicts are resolved locally. Never publish or push unless authorized by the user's workflow.
