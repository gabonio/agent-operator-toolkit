#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"{path}: expected a JSON object")
        return {}
    return value


def discover_root(explicit_root: Path | None, client: str) -> Path | None:
    if explicit_root is not None:
        return explicit_root.expanduser().resolve()

    plugin_root = Path(__file__).resolve().parent.parent
    bundled_root = plugin_root.parent.parent
    if (bundled_root / ".agents" / "plugins" / "marketplace.json").is_file():
        return bundled_root

    checkout_roots = {
        "claude": Path.home() / ".claude" / "plugins" / "marketplaces" / "agent-operator-toolkit",
        "codex": Path.home() / ".codex" / "marketplaces" / "agent-operator-toolkit",
        "gemini": Path.home() / ".gemini" / "extensions" / "agent-operator-toolkit",
    }
    default_checkout = checkout_roots[client]
    if default_checkout.is_dir():
        return default_checkout.resolve()
    return None


def plugin_entries(data: dict, label: str, errors: list[str]) -> dict[str, dict]:
    raw_entries = data.get("plugins")
    if not isinstance(raw_entries, list):
        errors.append(f"{label} marketplace plugins must be an array")
        return {}
    entries: dict[str, dict] = {}
    for index, entry in enumerate(raw_entries):
        if not isinstance(entry, dict):
            errors.append(f"{label} plugin at index {index} must be an object")
            continue
        name = entry.get("name")
        if not isinstance(name, str) or not name:
            errors.append(f"{label} plugin at index {index} has no valid name")
            continue
        if name in entries:
            errors.append(f"{label} marketplace contains duplicate plugin {name}")
            continue
        entries[name] = entry
    return entries


def diagnose(root: Path | None, client: str) -> list[str]:
    errors: list[str] = []
    for command in ("git", client):
        resolved = shutil.which(command)
        print(f"{'OK' if resolved else 'MISSING'}: {command}{f' -> {resolved}' if resolved else ''}")
        if not resolved:
            errors.append(f"required command is unavailable: {command}")

    if root is None:
        errors.append("Agent Operator checkout or extension was not found; pass --marketplace-root")
        return errors

    print(f"CHECKOUT: {root}")
    claude = load_json(root / ".claude-plugin" / "marketplace.json", errors)
    codex = load_json(root / ".agents" / "plugins" / "marketplace.json", errors)
    gemini = load_json(root / "gemini-extension.json", errors)
    claude_plugins = plugin_entries(claude, "Claude", errors)
    codex_plugins = plugin_entries(codex, "Codex", errors)

    if claude.get("name") != codex.get("name"):
        errors.append("Claude and Codex marketplace names differ")
    if gemini.get("name") != claude.get("name"):
        errors.append("Gemini extension and marketplace names differ")
    if set(claude_plugins) != set(codex_plugins):
        errors.append("Claude and Codex registries list different plugins")

    for name in sorted(set(claude_plugins) | set(codex_plugins)):
        if not isinstance(name, str) or not name:
            errors.append("registry contains a plugin without a valid name")
            continue
        plugin_root = root / "plugins" / name
        if not plugin_root.is_dir():
            errors.append(f"missing plugin source: plugins/{name}")
            continue
        claude_manifest = load_json(plugin_root / ".claude-plugin" / "plugin.json", errors)
        codex_manifest = load_json(plugin_root / ".codex-plugin" / "plugin.json", errors)
        if claude_manifest.get("name") != name or codex_manifest.get("name") != name:
            errors.append(f"manifest name mismatch for {name}")
        if claude_manifest.get("version") != codex_manifest.get("version"):
            errors.append(f"manifest version mismatch for {name}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Agent Operator distribution doctor")
    parser.add_argument("--marketplace-root", type=Path)
    parser.add_argument("--client", choices=("claude", "codex", "gemini"), default="codex")
    args = parser.parse_args()
    errors = diagnose(discover_root(args.marketplace_root, args.client), args.client)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"FAIL: {len(errors)} setup issue(s) found.")
        return 1
    print("OK: Agent Operator distribution setup looks healthy.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
