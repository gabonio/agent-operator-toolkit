# Prototype Delivery

Use only after explicit prototype/POC confirmation.

Record the learning goal, users/environment/lifetime, data bounds, approved shortcuts, replacement triggers, and production-promotion work.

Proportionally relax mocks, synthetic or deliberately bounded data, in-memory/local state, replaceable architecture, test breadth, and production-like build depth. A full-dataset shortcut is acceptable only for synthetic or explicitly small bounded data, with the ceiling and replacement trigger documented.

Never relax secrets, destructive safety, unrelated-work preservation, approval gates, truthful reporting, or authorization/privacy. Reapply production controls such as retries, observability, rollback, and rate limits when a prototype touches production systems, external writes, regulated data, or meaningful security paths. Never deploy or describe a prototype as production-ready without a separately approved hardening plan.
