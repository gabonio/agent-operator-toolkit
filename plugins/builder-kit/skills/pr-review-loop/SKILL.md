---
name: pr-review-loop
description: Bounded GitHub pull-request AI review workflow. Use only when explicitly requested to run Builder Kit's PR review loop, trigger /ai-review, or repeatedly address AI review comments. Verify findings, fix worthwhile issues, reply with pushed-commit evidence, resolve addressed conversations, and stop after ten iterations.
disable-model-invocation: true
---

# PR Review Loop

Use the repository's authenticated GitHub workflow and local rules. Stop after ten iterations without a new user decision.

## Scope and authorization

Choose the review scope:

- **Incremental checkpoint:** one coherent, verified slice; record the last clean head as baseline.
- **Final integrated review:** the complete, cross-slice result. Earlier clean checkpoints do not replace this pass.

Record authorization separately:

- **Inspect:** read-only PR, branch, checks, and thread inspection.
- **Trigger:** explicit permission to post `/ai-review`; this authorizes no other write.
- **Fix/sync:** explicit permission for the named merge, edit, commit, push, reply, or resolve scope.

Do not infer writes from skill invocation, a PR URL, or earlier permission. Before any fix/sync action, confirm the checkout is the fetched PR head (or contains only authorized descendants), the upstream is expected, and every staged, unstaged, and untracked change belongs to this PR. Otherwise stop or use a clean isolated worktree. Recheck outgoing commits and diff before each push.

## Loop

1. Inspect the PR head/base, checks, mergeability, base freshness, unresolved threads, scope, baseline, and authorizations.
2. Fetch the base. If the head is behind, report it in inspect mode; when sync is authorized, merge the base without rewriting published history, resolve only evidence-backed conflicts, verify, and push. Ask before resolving conflicts that alter behavior, contracts, security, migrations, or scope.
3. When trigger permission exists, post exactly `/ai-review`, record its time or ID, and wait for stable output. Inspect threads, not only top-level comments.
4. Check each finding against code, tests, the approved design, and local rules. Classify it as fix, false positive, duplicate, or user decision.
5. In inspect mode, report and stop. In authorized fix/sync mode, make only scoped fixes, add focused tests when behavior changes, verify, commit, and push.
6. After pushing, reply to each addressed thread with the fixing commit and useful evidence, then resolve it. Resolve false positives or duplicates only with supporting evidence. Leave partial, unverified, unpushed, security/product, and user decisions open.
7. Recheck base freshness. Repeat after fixes or synchronization until clean, blocked, or capped.

After an incremental checkpoint, record the clean head before the next slice. After the final pass, report iterations, findings, base syncs, commits, verification, checks, mergeability, and remaining threads.
