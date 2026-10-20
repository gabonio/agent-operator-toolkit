# Task Classification

Classify briefly and allow user override. Prototype status does not reduce risk.

## Tiny fix

Treat work as tiny only when all are true:

- one localized behavior changes;
- inspection reveals an evident root cause;
- no architecture, public contract, schema, authorization, persistence, dependency, migration, or deployment behavior changes;
- focused verification exists;
- the change does not conceal a broader design problem.

A tiny fix may skip durable spec/plan documents but still requires repository inspection, unrelated-work preservation, and appropriate verification.

## Planned work

Everything else uses `$develop-from-spec`. Security, credentials/secrets, permissions, destructive actions, migrations, cross-service contracts, large data paths, concurrency, deployment, and production integration are always planned work.

If uncertain, classify as planned work.
