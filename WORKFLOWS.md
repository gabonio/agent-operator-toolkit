# Marketplace workflows

These workflows keep Agent Operator portable, reviewable, and consistent across Codex, Claude Code, GitHub Copilot, and Gemini CLI.

## Add a plugin

1. Create `plugins/<plugin-name>/` with matching `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json` manifests.
2. Keep the plugin self-contained. Paths must be relative to its root and durable instructions belong in its skills or references.
3. Add matching entries to `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json`.
4. Default Codex plugins to `AVAILABLE` and `ON_INSTALL` unless a different policy is explicitly required.
5. Add or update Gemini root skill entrypoints for portable skills.
6. Run `./scripts/check`.

Copilot consumes the shared `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json` manifests using its supported legacy format. Keep skills under `skills/<name>/SKILL.md` and relative resources inside the plugin; do not add duplicate Copilot manifests or workflow copies.

## Update a plugin

1. Read the plugin's primary `SKILL.md` and release guidance.
2. Make the smallest coherent change and update directly affected references, prompts, and manifests.
3. Bump both plugin manifests using semantic versioning. Never publish changed instructions under an existing version.
4. Update the Claude marketplace entry to the same version.
5. Update `gemini-extension.json` or Gemini skill/command entrypoints when extension behavior changes.
6. Run focused skill validation, then `./scripts/check`.

## Keep plugins generic

1. Search the complete plugin for employer names, internal hosts, private commands, proprietary platform types, and private workflow dependencies.
2. Replace organizational policy with repository discovery and evidence-backed local rules.
3. Route specialized work to an available owning skill without assuming that skill is installed.
4. Ensure the plugin has a safe fallback or a clear stop condition when optional integrations are unavailable.

## Release

1. Confirm both marketplace registries list the same plugins and valid relative sources.
2. Confirm each plugin's Claude and Codex manifests have the same version and identity.
3. Confirm the Gemini extension manifest, commands, and root skills are valid and synchronized.
4. Run `./scripts/check` from the marketplace root.
5. Review the release diff for generated files, secrets, machine-specific paths, and unrelated changes.
6. Commit and publish only after the validation output and release version are recorded.

## Setup documentation

1. Keep [README-CODEX.md](./README-CODEX.md), [README-CLAUDE.md](./README-CLAUDE.md), [README-COPILOT.md](./README-COPILOT.md), and [README-GEMINI.md](./README-GEMINI.md) aligned with their native commands and available setup skills.
2. Treat Codex, Claude Code, and Copilot as marketplace clients and Gemini CLI as an extension client; do not invent a shared command syntax. Copilot currently uses the documented native install path, not the three-client setup router/doctor.
3. Prefer native install, update, reload/restart, and doctor flows over direct edits to user configuration.
4. When setup plugin behavior changes, bump its version and verify its three client surfaces. Validate Copilot's shared manifests, Builder Kit skill metadata, and resource links with `./scripts/check`; smoke-test installation and `/skills list` with Copilot CLI when available.

## Adversarial review changes

Builder Kit's review loop is local and integration-agnostic. It reviews the complete current diff, reports three or four material findings per pass, fixes authorized findings, verifies the result, and repeats. GitHub comments, commits, pushes, and thread resolution are optional delivery actions and must respect the active environment's normal authorization boundary.
