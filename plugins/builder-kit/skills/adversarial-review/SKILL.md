---
name: adversarial-review
description: Read-only pressure test for a specification, plan, architecture, implementation, current diff, or readiness claim. Use only when explicitly requested to run an adversarial review, challenge assumptions, find hidden flaws, pressure-test decisions, or argue against readiness. Report three or four evidence-aware findings per pass without inventing objections.
---

# Adversarial Review

Read [the adversarial lens](../../references/lenses/adversarial-review.md), [lens routing](../../references/lenses/lens-routing.md), and only the domain lenses relevant to the target.

## Procedure

1. Identify the artifact, approved objective, relevant constraints, and evidence available.
2. State the review boundary and whether this is a same-context pass, fresh-context pass, automated evidence, or human review. Do not imply independence that did not occur.
3. Challenge material assumptions, decision tradeoffs, failure modes, scale, trust boundaries, operability, and verification gaps.
4. Verify claims against repository evidence where possible. Label observation, inference, hypothesis, and unanswered question distinctly.
5. Report the three or four most material findings by default. Report fewer when fewer are real; do not fill the batch with style preferences or speculative criticism. For code, anchor each finding to the tightest useful path and line range.
6. Include overlooked strengths, residual risks, and one verdict: `ready`, `ready with accepted risks`, `revise`, or `blocked on decision`.

Remain read-only unless the user separately authorizes changes. A finding does not overrule repository evidence or user authority; document accepted risks clearly.
