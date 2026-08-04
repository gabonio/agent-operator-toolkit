---
name: marketplace-management
description: Create, add, update, validate, or release Agent Operator components for Codex, Claude Code, and Gemini CLI. Use when a user asks to scaffold a marketplace plugin, synchronize manifests or registries, maintain the Gemini extension surface, diagnose distribution drift, prepare a release, or improve contributor tooling. Preserve unrelated entries and validate duplicated metadata before publishing.
---

# Marketplace Management

Treat marketplace registries, plugin manifests, and the Gemini extension manifest as an integrity boundary. Read repository instructions and the target plugin before changing them.

## Classify the task

- **Add plugin:** scaffold a self-contained `plugins/<name>/` root and append registry entries.
- **Update plugin:** change the owning plugin, bump its version, and synchronize shared metadata.
- **Validate:** remain read-only and report drift, malformed metadata, unsafe paths, or missing assets.
- **Release:** regenerate when supported, validate, review the complete diff, and publish only authorized changes.
- **Setup problem:** route user installation and discovery issues to an available setup or doctor skill.

## Add or update a plugin

1. Discover the marketplace root and read its contributor instructions.
2. Prefer an available plugin scaffolder over hand-creating schema-sensitive manifests.
3. Keep the outer directory and manifest `name` identical, lowercase, and hyphenated.
4. Keep plugin content self-contained. Use relative paths beginning with `./` and do not depend on sibling checkouts or machine-specific locations.
5. Maintain `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`. Shared identity fields must agree; Codex-only interface fields stay in the Codex manifest.
6. Append matching entries to both marketplace registries without reordering or replacing unrelated plugins.
7. Include explicit Codex installation, authentication, and category policy.
8. Validate each `SKILL.md`, the plugin manifest, the marketplace registries, and referenced assets.
9. Keep Gemini's root `skills/` entrypoints and TOML commands synchronized with their authoritative plugin skills.

## Release discipline

1. Use semantic versioning and never publish changed plugin or extension content under an existing version.
2. If the repository has a generator, edit its declared source of truth and regenerate; do not hand-edit generated outputs.
3. Run the repository's strict check—`./scripts/check` in Agent Operator—then inspect Git status for generated drift and unrelated changes.
4. Confirm install and update documentation matches the current marketplace name and repository URL.
5. Do not install, stage, commit, push, or publish unless the user authorized that action.

## Review checklist

- Same plugin set in Claude and Codex registries.
- Valid local source path for every plugin.
- Matching name, version, description, author, repository, keywords, and skills path across manifests.
- Valid semantic versions and no placeholder metadata.
- Existing marketplace display name and plugin order preserved.
- No employer-specific systems, credentials, private hosts, or machine-specific paths.
- Setup, doctor, update, and failure-recovery instructions are explicit.
- `gemini-extension.json`, Gemini root skills, and Gemini commands are valid and self-contained.

Report what changed, checks run, generated artifacts, unresolved drift, and the exact release boundary.
