# Task Classification

Classify at invocation, explain the result briefly, and allow user override. Delivery profile is separate: a prototype may still be non-trivial or high-risk.

## Tiny fix

Treat work as tiny only when all are true:

- one localized behavior changes;
- inspection reveals an evident root cause;
- no architecture, public contract, schema, authorization, persistence, dependency, migration, or deployment behavior changes;
- focused verification exists;
- the change does not conceal a broader design problem.

A tiny fix may skip durable spec/plan documents, but still requires repository inspection, unrelated-work preservation, appropriate verification, and an evidence-backed report.

## Planned work

Everything else uses `$develop-from-spec`. Treat security, credentials, permissions, destructive operations, migrations, cross-service contracts, large/growing data paths, concurrency, deployment, and production integration as high-risk.

If uncertain, classify as planned work and explain the uncertainty rather than silently reducing the process.
