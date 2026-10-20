# Release and update policy

Use this only when maintaining or publishing Builder Kit itself.

## Release contract

- Bump `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` together for every published change: patch for compatible guidance/fixes, minor for capabilities, major for breaking workflows. Never publish changed content under a cached version.
- Refresh [standards provenance](../../docs/standards-provenance.md) only when its sources change.
- Announce the version, important changes, update path, and any restart/manual action in the agreed channel.

## Client delivery

- Claude: workspace settings control marketplace auto-update; refresh occurs at startup when enabled.
- Codex native marketplace: run `codex plugin marketplace upgrade agent-operator-toolkit`, then start a new task if needed.
- Codex manual checkout: pull the latest checkout and restart the session.
- Do not add self-modifying startup hooks; installed instructions are versioned artifacts.
