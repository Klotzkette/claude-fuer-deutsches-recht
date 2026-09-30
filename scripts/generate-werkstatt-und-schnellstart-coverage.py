#!/usr/bin/env python3
"""Schreibt docs/werkstatt-und-schnellstart-coverage.md."""

from __future__ import annotations

import html
import json
from pathlib import Path

from prompt_profiles import enabled, formats, standalone_kinds
from urllib.parse import quote

from readme_display import display_plugin_description
from bauwirtschaft_hoai import PHASEN, werkstatt_path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
DOCS = REPO / "docs"
DOWNLOAD_BASE = "https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path="


def prompt_stem(plugin_name: str) -> str:
    return plugin_name


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def direct_download(repo_path: str, label: str) -> str:
    url = DOWNLOAD_BASE + quote(repo_path, safe="/")
    return f"[`{html.escape(label)}` herunterladen]({url})"


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
        "| Plugin | Kurzbeschreibung | Datei | Direktdownload | Navigation |",
        "| --- | --- | --- | --- | --- |",
    ]
    for plugin in plugins:
        name = plugin["name"]
        if not enabled(name, kind):
            continue
        directory = plugin_dir(plugin)
        prompt = directory / f"{name}-{kind}.md"
        rel = prompt.relative_to(REPO).as_posix()
        description = html.escape(
            display_plugin_description(str(plugin.get("description", "")), directory).replace("|", "\\|")
        )
        plugin_rel = directory.relative_to(REPO).as_posix()
        downloads = " · ".join(direct_download(f"{plugin_rel}/{name}-{kind}.{ext}", f"{name}-{kind}.{ext}") for ext in formats(name))
        lines.append(
            f"| `{name}` | {description} | `{prompt.name}` | "
            f"{downloads} | "
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
        "Vollständige, alphabetisch sortierte Übersicht der ausführlichen Werkstatt-Prompts und kompakten Schnellstart-Prompts. Beide Formate werden ausschließlich als einzelne Markdown-Dateien angeboten, nicht als ZIP und nicht als installierbarer Skill. Jeder Dateilink startet den Download, statt die Markdown-Quelle im Browser anzuzeigen.",
        "",
        "English: Workshop prompts are the detailed standalone workflow; quick-start prompts are the compact standalone entry point. Every file link downloads the unchanged Markdown file. Neither format is an installable skill or part of the plugin ZIP.",
        "",
        "Nicht jedes Paket bietet beide Formen: [beA-Versand](../bea-versand/README.md) hat bewusst nur einen Skill und eine eigenständige Werkstatt, keinen separaten Mini-Prompt. Angebotenes TXT enthält denselben Text wie die MD-Fassung. Die Vollständigkeitsprüfung berücksichtigt diese vorgesehenen Formate.",
        "",
        "English: Available formats vary by package. beA-Versand has a workshop but no separate mini prompt; TXT alternatives contain the same text as their MD version. Completeness is measured against the intended formats.",
        "",
        "[Repository-Start](../README.md) · [Download-Index](../ASSET_INDEX.md) · [Skill-Gesamtübersicht](../SKILLS.md) · [Testakten](../testakten/README.md)",
        "",
        "[Werkstatt-Prompts](#werkstatt-prompts) · [HOAI-Phasen-Werkstätten](#hoai-phasen-werkstätten) · [Schnellstart-Prompts](#schnellstart-prompts)",
        "",
    ]
    for plugin in plugins:
        directory = plugin_dir(plugin)
        stem = prompt_stem(plugin["name"])
        if all((directory / f"{stem}-{kind}.{ext}").is_file()
               for kind in standalone_kinds(stem) for ext in formats(stem)):
            ok += 1
    percent = 100 if not plugins else round(ok * 100 / len(plugins), 2)
    lines += [
        f"Vollständigkeit: **{ok} von {len(plugins)} Plugins**, also {percent} Prozent.",
        "",
    ]
    lines.extend(prompt_table(plugins, "werkstatt"))
    lines.extend([
        "## HOAI-Phasen-Werkstätten", "",
        "Neun zusätzliche eigenständige Werkstätten für das Leistungsbild Gebäude und Innenräume. Jeweils eine Datei für den konkreten Phasenauftrag wählen; die Dateien sind nicht Teil des installierten Plugins. [Skills, Schulungsakten und fachliche Abgrenzung](bauwirtschaft-hoai-phasen.md).", "",
        "| Phase | Arbeitsbereich | Markdown-Download |", "| --- | --- | --- |",
    ])
    for phase, title, _, _, purpose in PHASEN:
        path = werkstatt_path(phase)
        if not (REPO / path).is_file():
            raise FileNotFoundError(path)
        lines.append(f"| {phase}: {title} | {purpose} | {direct_download(path, Path(path).name)} |")
    lines.append("")
    lines.extend(prompt_table(plugins, "schnellstart"))
    (DOCS / "werkstatt-und-schnellstart-coverage.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Coverage geschrieben: {ok}/{len(plugins)} Plugins")
    return 0 if ok == len(plugins) else 1


if __name__ == "__main__":
    raise SystemExit(main())
