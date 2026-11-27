#!/usr/bin/env python3
"""Zählt Plugins, Skills und Testakten aus einer Repo-Quelle."""

from __future__ import annotations

import json
from pathlib import Path

from aktenbestand import zaehlung


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"


def load_plugins() -> list[dict]:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def main() -> int:
    plugins = load_plugins()
    skill_files = []
    for plugin in plugins:
        directory = plugin_dir(plugin)
        skill_files.extend(sorted((directory / "skills").glob("*/SKILL.md")))

    result = {
        "plugins": len(plugins),
        "skills": len(skill_files),
        **zaehlung(REPO),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
