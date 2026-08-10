#!/usr/bin/env python3
"""Schreibt docs/werkstatt-und-schnellstart-coverage.md."""

from __future__ import annotations

import html
import json
from pathlib import Path

from readme_display import display_prose


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
DOCS = REPO / "docs"
RAW_BASE = "https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main"


def prompt_stem(plugin_name: str) -> str:
    return plugin_name


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def direct_download(url: str, label: str) -> str:
    return f'<a href="{url}" download><code>{html.escape(label)}</code></a>'


def prompt_table(plugins: list[dict], kind: str) -> list[str]:
    title = "Werkstatt-Prompts" if kind == "werkstatt" else "Schnellstart-Prompts"
    purpose = (
        "Ausführlicher Arbeitsmodus für komplexe oder mehrstufige Vorgänge."
        if kind == "werkstatt"
        else "Kompakter Einstieg für den Kernworkflow und ein erstes belastbares Arbeitsprodukt."
    )
    lines = [
        f"## {title}",
        "",
        purpose,
        "",
        "| Plugin | Kurzbeschreibung | Im Repository | Direktdownload | Navigation |",
        "| --- | --- | --- | --- | --- |",
    ]
    for plugin in plugins:
        name = plugin["name"]
        directory = plugin_dir(plugin)
        prompt = directory / f"{name}-{kind}.md"
        rel = prompt.relative_to(REPO).as_posix()
        description = html.escape(
            display_prose(str(plugin.get("description", ""))).replace("|", "\\|")
        )
        raw = f"{RAW_BASE}/{rel}"
        plugin_rel = directory.relative_to(REPO).as_posix()
        lines.append(
            f"| `{name}` | {description} | [`{prompt.name}`](../{rel}) | "
            f"{direct_download(raw, prompt.name)} | "
            f"[README](../{plugin_rel}/README.md) · [Skills](../skills-index/{name}.md) |"
        )
    lines.append("")
    return lines


def main() -> int:
    DOCS.mkdir(exist_ok=True)
    plugins = sorted(
        json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"],
        key=lambda plugin: plugin["name"].lower(),
    )
    ok = 0
    lines = [
        "# Werkstatt- und Schnellstart-Coverage",
        "",
        "Vollständige, alphabetisch sortierte Übersicht der ausführlichen Werkstatt-Prompts und kompakten Schnellstart-Prompts. Beide Formate werden ausschließlich als einzelne Markdown-Dateien angeboten, nicht als ZIP und nicht als installierbarer Skill.",
        "",
        "[Repository-Start](../README.md) · [Download-Index](../ASSET_INDEX.md) · [Skill-Gesamtübersicht](../SKILLS.md) · [Testakten](../testakten/README.md)",
        "",
        "[Werkstatt-Prompts](#werkstatt-prompts) · [Schnellstart-Prompts](#schnellstart-prompts)",
        "",
    ]
    for plugin in plugins:
        directory = plugin_dir(plugin)
        stem = prompt_stem(plugin["name"])
        werkstatt = directory / f"{stem}-werkstatt.md"
        schnellstart = directory / f"{stem}-schnellstart.md"
        if werkstatt.is_file() and schnellstart.is_file():
            ok += 1
    percent = 100 if not plugins else round(ok * 100 / len(plugins), 2)
    lines += [
        f"Vollständigkeit: **{ok} von {len(plugins)} Plugins**, also {percent} Prozent.",
        "",
    ]
    lines.extend(prompt_table(plugins, "werkstatt"))
    lines.extend(prompt_table(plugins, "schnellstart"))
    (DOCS / "werkstatt-und-schnellstart-coverage.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Coverage geschrieben: {ok}/{len(plugins)} Plugins")
    return 0 if ok == len(plugins) else 1


if __name__ == "__main__":
    raise SystemExit(main())
