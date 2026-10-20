---
name: pr-review-loop
description: Bounded local adversarial review-and-fix loop for current changes or a pull request. Use only when explicitly requested to repeatedly review changes until merge-ready. Return up to three or four evidence-backed findings per pass, fix authorized issues, verify, and stop when ready or after ten iterations.
disable-model-invocation: true
---

# PR Review Loop

Use the [adversarial reviewer](../adversarial-review/SKILL.md), repository instructions, and available Git/GitHub tools. Read [Git Safety](../../references/workflow/git-safety.md). Stop after ten iterations without a new user decision.

## Scope and authorization

Choose the review scope:

- **Incremental checkpoint:** one coherent, verified slice; record the last clean head as baseline.
- **Final integrated review:** the complete, cross-slice result. Earlier clean checkpoints do not replace this pass.

Record authorization separately:

- **Inspect:** read-only local diff, PR, branch, checks, and thread inspection.
- **Fix/sync:** explicit permission for the named merge, edit, commit, push, reply, or resolve scope.

Do not infer writes from skill invocation, a PR URL, or earlier permission. Preserve unrelated changes. Before published-PR fix/sync actions, confirm the checkout is the fetched PR head (or only authorized descendants), the upstream is expected, and the outgoing diff contains only authorized work. If ownership is uncertain, stop or use a clean isolated worktree. Recheck outgoing commits and diff before each push.

## Loop

1. Identify the complete working-tree/index diff or PR diff, real base branch, starting head, checks, scope, baseline, and authorizations. When a PR exists, inspect checks, mergeability, base freshness, and unresolved threads.
2. For a published PR, fetch the base when authorized. If behind, report it in inspect mode; when sync is authorized, merge without rewriting published history, resolve evidence-backed conflicts, verify, and push. Ask before conflicts that alter behavior, contracts, security, migrations, or scope.
3. Review the complete current diff locally across behavior, security, data integrity, compatibility, operations, tests, and the approved objective. Report only the three or four highest-value findings, fewer when fewer are real, with severity, evidence, impact, fix/validation, and a useful `path:line` anchor.
4. Verify findings against code, tests, design, and local rules. Classify as fix, false positive, duplicate, accepted risk, or user decision. Present local review comments; use inline annotations when available. Publish comments only when authorized.
5. In inspect mode, report and stop. When fixes are authorized, make scoped changes, add focused tests for behavior changes, and verify. Commit and push only when separately authorized.
6. Mark local findings addressed after verification. For authorized remote replies/resolution, include evidence and a fixing commit when pushed; resolve only fully addressed findings. Leave partial, unverified, unpushed, and security/product decisions open.
7. Recompute and review the complete diff after fixes or synchronization, not just the last batch's files. Recheck published-PR base freshness and unresolved threads before declaring readiness.

Stop with `ready` only when no actionable findings remain, required checks pass, and any published PR contains the required base and has no unresolved blocking conversations. Otherwise use `ready with accepted risks`, `blocked on decision`, or `iteration limit reached`. Record the clean head after an incremental checkpoint; it does not replace final integrated review. Report iterations, findings fixed/open, verification, actual publication actions, base state, and verdict.
