# Release and update policy

Use this only when maintaining or publishing Builder Kit itself.

## Release contract

- Bump both `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` for every published Builder Kit change. Use a patch release for compatible guidance or fixes, a minor release for new capabilities, and a major release for breaking workflow changes.
- Keep the two manifests' identity, version, description, author, repository, license, keywords, and skills path aligned.
- Never publish changed Builder Kit content under an existing version. Both clients cache plugins by version and may otherwise retain stale instructions.

## Client delivery

- Claude: refresh the configured marketplace, update Builder Kit, and start a new session if the active session still holds older skill instructions.
- Codex: upgrade the configured marketplace, update Builder Kit, and start a new task if the active task still holds older skill context.
- Marketplace maintainers must validate both registries and the embedded plugin before publishing.
- Do not add a self-modifying Builder Kit hook. Installed plugins run from versioned caches, and silently replacing agent instructions during startup creates avoidable integrity and stability risk.
