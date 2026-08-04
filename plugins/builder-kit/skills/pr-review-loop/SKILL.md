---
name: pr-review-loop
description: Bounded adversarial review-and-fix loop for the current changes or pull request. Use only when explicitly requested to run Builder Kit's PR review loop or repeatedly review changes until merge-ready. Generate three or four evidence-backed findings per pass, fix worthwhile issues, verify the result, and stop when ready or after ten iterations.
---

# PR Review Loop

This loop runs locally with Builder Kit's adversarial reviewer. It requires no organization-specific review bot or slash command. Use repository instructions and the available Git/GitHub workflow.

1. Identify the review target: the current working-tree and index changes, or the pull-request diff when a PR exists. Discover the base branch; never assume `main` or `master`.
2. Record the starting head, diff boundary, repository status, checks available, and any pre-existing review comments. Protect unrelated changes throughout the loop.
3. For a published PR, check base freshness before the first pass and before declaring it ready. Fetching, merging, pushing, posting GitHub comments, and resolving threads still require the authority normally required by the active environment.
4. Start an iteration counter at one. Never exceed ten without a new user decision.
5. Invoke the [adversarial review](../adversarial-review/SKILL.md) against the complete current diff. Review behavior, security, data integrity, compatibility, operability, tests, and the approved objective—not just modified lines.
6. Return only the three or four highest-value new findings in the iteration. Report fewer when fewer are real. Each finding must include severity, evidence, impact, a concrete fix or validation, and the tightest useful `path:line` anchor.
7. Present findings as review comments. When the active interface supports inline comments, attach them to the anchored lines. Publish them to GitHub only when the user requested remote review activity; otherwise keep the comments in the task.
8. Verify each finding against code, tests, specifications, and local rules. Classify it as `fix`, `false positive`, `duplicate`, `accepted risk`, or `user decision`.
9. Fix the current batch when changes are authorized. Keep fixes scoped, add focused tests for behavior changes, and run proportionate verification. Do not commit, push, or resolve remote conversations unless that action is authorized.
10. Mark local comments addressed only after the fix is verified. For remote threads, reply with the disposition and verification evidence; include a fixing commit link when one has been pushed, then resolve only fully addressed threads.
11. Recompute the complete diff and run a fresh adversarial pass. Do not restrict later passes to the previous batch's files; fixes can expose or introduce other problems.
12. If no actionable findings remain, run the repository's merge-readiness checks and recheck base freshness and unresolved conversations when a PR exists.

Stop with `ready` only when there are no actionable findings, required checks pass, no unresolved blocking conversations remain, and the reviewed head contains the required base. Stop earlier with `ready with accepted risks`, `blocked on decision`, or `iteration limit reached` when appropriate. Report the boundary, iterations, findings fixed/declined/open, verification, commits or remote comments actually made, base state, and final verdict.
