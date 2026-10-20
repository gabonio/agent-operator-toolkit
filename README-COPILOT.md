# GitHub Copilot setup

Builder Kit uses Copilot's native plugin and agent-skill support. Copilot reads the existing `.claude-plugin/marketplace.json` catalog and each plugin's `.claude-plugin/plugin.json` manifest; no duplicate Copilot catalog or copy of the instructions is needed.

## Copilot CLI

Register the marketplace and install Builder Kit:

```sh
copilot plugin marketplace add gabonio/agent-operator-toolkit
copilot plugin install builder-kit@agent-operator-toolkit
copilot plugin list
```

Start a new session and run `/skills list`. Builder Kit provides `builder-kit`, `start-new-app`, `develop-from-spec`, `adversarial-review`, and `pr-review-loop`.

Invoke a skill explicitly, for example:

```text
Use the builder-kit skill to plan this feature.
Use the pr-review-loop skill to review the current diff.
```

The `$skill-name` spelling used in Codex examples is not required in Copilot. Skills load only relevant references, preserve repository instructions, and require approval before non-trivial implementation. Review runs locally using the agent's available tools.

## GitHub Copilot app

Open **Customize > Plugins**, add the `gabonio/agent-operator-toolkit` marketplace, and install **Builder Kit**. Start a new session, then explicitly ask to use a Builder Kit skill as above. Installation in a separate CLI may not affect the app's environment; install through the client you use.

## Other Copilot environments

The plugin commands above are for Copilot CLI, not a universal command syntax for every editor or cloud environment. Copilot also supports repository skills in `.github/skills/`, `.claude/skills/`, or `.agents/skills/`. When using repository skills instead of plugins, preserve the full Builder Kit resource tree: copying only a `SKILL.md` breaks its relative references.

For example, a repository may vendor `plugins/builder-kit/` under `.github/builder-kit/` and expose each of its five skills through a small `.github/skills/<skill-name>/SKILL.md` entrypoint. Give the entrypoint the matching `name`, an explicit-invocation `description`, and `disable-model-invocation: true`, then instruct it to read `../../builder-kit/skills/<skill-name>/SKILL.md` and resolve references from that authoritative file's directory. Commit the complete bundle and entrypoints for environments that run from the repository. Do not replace existing skills or instructions.

## Updates and local development

```sh
copilot plugin marketplace update agent-operator-toolkit
copilot plugin update builder-kit@agent-operator-toolkit
```

Start a new session after updating. To try unpublished changes from this checkout:

```sh
copilot plugin install ./plugins/builder-kit
copilot plugin list
```

Local installs are cached. Re-run the local install after editing, then start a new session. Avoid enabling both a local and a marketplace copy of Builder Kit at once.

## Troubleshooting

- If commands are unavailable, check `copilot plugin --help` and use a Copilot CLI version with plugin support.
- If marketplace installation fails, check authentication and repository access. For local-only work, install from the plugin path above.
- If skills are missing, confirm the plugin is installed and enabled in the same client, restart its session, and inspect `/skills list`.
- Do not copy Gemini's root `skills/` wrappers by themselves: they depend on the rest of this repository.

References: [Copilot plugin format](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference), [marketplaces](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-marketplace), and [agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills).
