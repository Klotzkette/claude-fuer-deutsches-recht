#!/usr/bin/env python3
"""Erzeugt den vollständigen Plugin-Katalog in der Repository-README."""

from __future__ import annotations

import json
import re
from pathlib import Path

from readme_display import display_prose


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
README = REPO / "README.md"
BEGIN = "<!-- BEGIN PLUGIN-KATALOG (auto-generated) -->"
END = "<!-- END PLUGIN-KATALOG (auto-generated) -->"


def source_rel(plugin: dict) -> str:
    source = plugin.get("source") or f"./{plugin['name']}"
    return source.removeprefix("./")


def display_description(plugin: dict) -> str:
    readme = REPO / source_rel(plugin) / "README.md"
    if readme.is_file():
        text = readme.read_text(encoding="utf-8", errors="ignore")
        match = re.search(
            r"<!-- BEGIN direkt-loslegen \(autogen\) -->[\s\S]*?"
            r"## Was ist das hier\?\n\n(.+?)\n\n",
            text,
        )
        if match:
            return display_prose(re.sub(r"\s+", " ", match.group(1)).strip())
    return display_prose(
        re.sub(r"\s+", " ", str(plugin.get("description", ""))).strip()
    )


def group_label(name: str) -> str:
    first = name[:1].upper()
    return first if first.isalpha() else "0-9"


def build_catalog(plugins: list[dict]) -> str:
    ordered = sorted(plugins, key=lambda item: item["name"].lower())
    groups: dict[str, list[dict]] = {}
    for plugin in ordered:
        groups.setdefault(group_label(plugin["name"]), []).append(plugin)

    labels = sorted(groups, key=lambda value: (value != "0-9", value))
    lines = [
        BEGIN,
        "Alphabetisch: "
        + " · ".join(f"[{label}](#{label.lower()})" for label in labels),
        "",
    ]
    for label in labels:
        lines.extend(
            [
                f"### {label}",
                "",
                "| Plugin | Beschreibung |",
                "| --- | --- |",
            ]
        )
        for plugin in groups[label]:
            name = plugin["name"]
            description = display_description(plugin).replace("|", "\\|")
            lines.append(f"| [`{name}`](./{source_rel(plugin)}) | {description} |")
        lines.append("")
    lines.append(END)
    return "\n".join(lines)


def replace_catalog(text: str, catalog: str) -> str:
    if BEGIN in text and END in text:
        pattern = re.compile(re.escape(BEGIN) + r"[\s\S]*?" + re.escape(END))
        return pattern.sub(catalog, text, count=1)

    pattern = re.compile(
        r"^\| Plugin \| Beschreibung \|\n"
        r"^\| --- \| --- \|\n"
        r"(?:^\|.*\|\n)+",
        flags=re.MULTILINE,
    )
    if not pattern.search(text):
        raise RuntimeError("Plugin-Tabelle in README.md nicht gefunden")
    return pattern.sub(catalog + "\n", text, count=1)


def main() -> int:
    marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    plugins = marketplace["plugins"]
    original = README.read_text(encoding="utf-8")
    updated = replace_catalog(original, build_catalog(plugins))
    README.write_text(updated, encoding="utf-8")
    print(f"README.md: vollständiger A-Z-Katalog mit {len(plugins)} Plugins.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
