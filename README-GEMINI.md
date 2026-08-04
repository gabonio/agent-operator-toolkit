# Agent Operator for Gemini CLI

Agent Operator is distributed to Gemini CLI as one native extension containing portable setup, development, review, and marketplace-management skills.

## Install

Run from a terminal, outside the Gemini interactive session:

```sh
gemini extensions install https://github.com/gabonio/agent-operator-toolkit
```

To opt into automatic updates:

```sh
gemini extensions install https://github.com/gabonio/agent-operator-toolkit --auto-update
```

For local development, link the checkout instead of copying it:

```sh
gemini extensions link /path/to/agent-operator-toolkit
```

Restart Gemini CLI after installation or extension-management changes.

## Verify and use

Inside Gemini CLI:

```text
/extensions list
/skills list
/commands list
```

The easiest setup entrypoint is:

```text
/agent-operator:setup install
```

After changing linked skills or commands, reload them:

```text
/skills reload
/commands reload
```

## Update

Run from a terminal:

```sh
gemini extensions update agent-operator-toolkit
```

Then restart Gemini CLI. To update all extensions, use `gemini extensions update --all` only when updating every installed extension is intended.

## Diagnose

From a checkout:

```sh
python3 plugins/agent-operator-setup/scripts/doctor.py --client gemini --marketplace-root .
```

The doctor validates the extension manifest and cross-client distribution metadata without editing Gemini settings.

## Disable, enable, or uninstall

```sh
gemini extensions disable agent-operator-toolkit --scope user
gemini extensions enable agent-operator-toolkit --scope user
gemini extensions uninstall agent-operator-toolkit
```

Do not use `--consent`, automatic updates, or workspace-scoped changes unless you understand and want those effects.

For the current native command and manifest reference, see the official [Gemini CLI extension documentation](https://geminicli.com/docs/extensions/) and [extension reference](https://github.com/google-gemini/gemini-cli/blob/main/docs/extensions/reference.md).
