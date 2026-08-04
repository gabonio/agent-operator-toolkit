# Security and Privacy

Load whenever work touches identities, permissions, secrets, user-controlled input, sensitive data, external access, or destructive actions.

- Identify assets, entry points, trust boundaries, likely abuse cases, and least-privilege access before implementation.
- Enforce authentication and object/action authorization on trusted backends; hidden UI is not access control.
- Validate inputs with strict schemas/allow-lists and encode outputs for their destination.
- Use approved authentication, session, cryptography, secret-storage, and dependency mechanisms; never invent security primitives.
- Never commit, expose, or log secrets, tokens, credentials, or unnecessary personal/sensitive data.
- Minimize fields and retention; define classification, permitted users, deletion, caching, export, and audit behavior when relevant.
- Fail safely without exposing upstream errors or internals. Protect against injection, XSS, CSRF, SSRF, IDOR, traversal, unsafe deserialization, and resource-exhaustion paths as applicable.
- Test negative authorization, boundary validation, sensitive-field omission, and safe failure behavior.

If the requested implementation conflicts with these guardrails, do not build the unsafe version. Explain the risk in the active communication profile and propose the safest design that meets the goal.
