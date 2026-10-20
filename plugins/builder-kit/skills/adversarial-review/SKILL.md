---
name: adversarial-review
description: Read-only pressure test for a specification, plan, architecture, implementation, diff, or readiness claim. Use only when explicitly requested to run an adversarial review, challenge assumptions, find hidden flaws, pressure-test decisions, or argue against readiness. Report bounded, evidence-aware findings without inventing objections.
disable-model-invocation: true
---

# Adversarial Review

Read [the adversarial lens](../../references/lenses/adversarial-review.md), [lens routing](../../references/lenses/lens-routing.md), and only the domain lenses relevant to the target. For code, queries, or pipelines, use [standards routing](../../references/standards/routing.md) and load only matching guides.

Establish the artifact, objective, constraints, evidence, and review boundary. State whether the pass is same-context, fresh-context, automated, or human; do not imply independence.

Apply the lens, verify claims where possible, and label inference or uncertainty. Report at most five material findings, overlooked strengths, residual risks, and one verdict: `ready`, `ready with accepted risks`, `revise`, or `blocked on decision`.

Remain read-only unless changes are separately authorized.
