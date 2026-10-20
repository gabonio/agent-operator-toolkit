# Security and Privacy

Load whenever work touches identities, permissions, secrets, user-controlled input, sensitive data, external access, or destructive actions.

- Identify assets, entry points, trust boundaries, abuse cases, and least-privilege access.
- Enforce authentication and object/action authorization on trusted backends; hidden UI is not access control.
- Validate inputs with schemas/allow-lists and encode outputs for their destination.
- Use approved auth, cryptography, secret-storage, and dependency mechanisms; never invent security primitives.
- Never commit, expose, or log secrets, tokens, credentials, or unnecessary personal/sensitive data.
- Minimize fields and retention; define classification, permitted users, deletion, caching, export, and audit behavior when relevant.
- Fail safely without exposing upstream internals; cover applicable injection, XSS, CSRF, object-access, SSRF, traversal, deserialization, and resource-exhaustion risks.
- Test negative authorization, boundary validation, sensitive-field omission, and safe failure behavior.

If a request conflicts with these guardrails, stop before implementation, explain the risk, and propose a safe design that still meets the goal.
