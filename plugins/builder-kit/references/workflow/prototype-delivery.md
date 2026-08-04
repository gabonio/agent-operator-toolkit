# Prototype Delivery

Use only after explicit prototype/POC confirmation.

Record:

- learning goal and success signal;
- intended users, environment, and lifetime;
- synthetic/real data and explicit size bounds;
- shortcuts taken and why they are proportional;
- replacement triggers and production-promotion work.

Proportionally relax mocks, synthetic or deliberately bounded data, in-memory/local state, replaceable architecture, test breadth, and production-like build depth. A full-dataset shortcut is acceptable only for synthetic or explicitly small bounded data, with the ceiling and replacement trigger documented.

Never relax secrets, destructive safety, preservation of unrelated work, approval gates, truthful readiness reporting, or authorization/privacy when real users or data are involved. Reapply production controls for production systems, external writes, regulated data, or meaningful security impact. Never deploy or describe a prototype as production-ready without a separately approved hardening plan.
