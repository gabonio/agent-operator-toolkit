# Jenkins and CI Standards

Separate job generation, orchestration, dependency gathering, and low-level testable payloads.

Team defaults:

- Make parameters/preconditions explicit and follow local Groovy/Python style.
- Validate preconditions before payload execution and fail fast when they are unavailable.
- Pass payload configuration explicitly; avoid hidden environment/path inference.
- Prefer clear stages over deeply nested job hierarchies.
- Minimize plugin dependencies and justify each addition.
- Log enough command context to diagnose failures without exposing secrets.
- Unit-test payloads/helpers and mock CI steps; validate pipeline syntax with repository tooling.
- Preserve release, credential, agent-label, artifact, and notification conventions unless they are the approved target.
