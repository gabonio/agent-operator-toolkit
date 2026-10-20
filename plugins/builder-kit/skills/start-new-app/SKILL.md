---
name: start-new-app
description: Guided, approval-gated workflow for designing and scaffolding a sustainable new application. Use only when explicitly requested or routed by Builder Kit for greenfield work. Discover product, users, data, scale, platform, integrations, security, local development, deployment, and ownership before generating code.
disable-model-invocation: true
---

# Start New App

1. Resolve [profiles](../../references/workflow/profiles.md) and ask only about unknowns that change the design: users/outcomes, data and growth, platform, integrations, trust boundaries, local development, deployment, ownership, and prototype limits.
2. Use [lens routing](../../references/lenses/lens-routing.md) for relevant product and engineering questions, then turn answers into decisions.
3. Follow [develop-from-spec](../develop-from-spec/SKILL.md); do not scaffold before approval.
4. For specialized platform work, delegate through [external capability routing](../../references/workflow/external-capabilities.md). Deployment is separate and requires explicit authorization naming the application and environment.
5. Establish and verify a production-like local run path. Scaffold only the approved minimum and report deferred hardening.
6. Add [AGENTS.md](../../templates/AGENTS.md.tmpl) or [CLAUDE.md](../../templates/CLAUDE.md.tmpl) guidance only with explicit permission; merge without overwriting existing rules.

Prototype projects must also read [prototype delivery](../../references/workflow/prototype-delivery.md). Never present a prototype as production-ready.
