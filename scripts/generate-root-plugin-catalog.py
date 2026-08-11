#!/usr/bin/env python3
"""Erzeugt den vollständigen Plugin-Katalog in der Repository-README."""

from __future__ import annotations

import json
import re
from pathlib import Path

from readme_display import display_prose
from testakte_zip_common import working_dump_flat_pairs


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
README = REPO / "README.md"
DIRECTORY_BEGIN = "<!-- BEGIN HAUPTVERZEICHNIS (auto-generated) -->"
DIRECTORY_END = "<!-- END HAUPTVERZEICHNIS (auto-generated) -->"
BEGIN = "<!-- BEGIN PLUGIN-KATALOG (auto-generated) -->"
END = "<!-- END PLUGIN-KATALOG (auto-generated) -->"
SKIP_TESTAKTEN = {"formatvorlagen-paradebeispiele", "megaprompts"}


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


def inventory_counts(plugins: list[dict]) -> dict[str, int]:
    skills = 0
    werkstatt = 0
    schnellstart = 0
    pluginlocal_testakten = 0
    for plugin in plugins:
        directory = REPO / source_rel(plugin)
        skills += sum(1 for _ in (directory / "skills").glob("*/SKILL.md"))
        name = plugin["name"]
        werkstatt += int((directory / f"{name}-werkstatt.md").is_file())
        schnellstart += int((directory / f"{name}-schnellstart.md").is_file())
        testakte = directory / "testakte"
        if testakte.is_dir() and working_dump_flat_pairs(
            testakte,
            include_gesamt_pdf=False,
        ):
            pluginlocal_testakten += 1

    central_testakten = sum(
        1
        for child in (REPO / "testakten").iterdir()
        if child.is_dir() and child.name not in SKIP_TESTAKTEN
    )
    return {
        "plugins": len(plugins),
        "skills": skills,
        "werkstatt": werkstatt,
        "schnellstart": schnellstart,
        "central_testakten": central_testakten,
        "testakten": central_testakten + pluginlocal_testakten,
    }


def build_directory(plugins: list[dict]) -> str:
    counts = inventory_counts(plugins)
    labels = sorted({group_label(plugin["name"]) for plugin in plugins})
    plugin_navigation = " · ".join(
        f"[{label}](#{label.lower()})" for label in labels
    )
    return "\n".join(
        [
            DIRECTORY_BEGIN,
            "Die fünf vollständigen Register sind alphabetisch sortiert und werden bei jedem Release gegen Marketplace und Dateibestand geprüft. Jede Liste nennt zu jedem Eintrag eine Kurzbeschreibung und führt von dort unmittelbar zur Datei, zum Download oder zur passenden Detailseite.",
            "",
            "| Bestand | Umfang | Kurzbeschreibung | Vollständige alphabetische Liste |",
            "| --- | ---: | --- | --- |",
            f"| **Plugins** | {counts['plugins']} | Installierbare Pakete für Rechtsgebiete und Arbeitsbereiche; jede Zeile beschreibt Zweck und fachlichen Zuschnitt. | [Plugin-Katalog mit Kurzbeschreibungen](#was-ist-drin) · [ZIPs und Einzeldateien](./ASSET_INDEX.md) |",
            f"| **Skills** | {counts['skills']} | Eng abgegrenzte Arbeitsabläufe; die Detailseiten führen jeden Skill mit Kurzbeschreibung und einzelnem Markdown-Download auf. | [Skill-Gesamtübersicht](./SKILLS.md) · [Detailseiten je Plugin](./skills-index/) |",
            f"| **Werkstatt-Prompts** | {counts['werkstatt']} | Ausführliche eigenständige Arbeitsmodi für komplexe Vorgänge; je Plugin mit Kurzbeschreibung und direktem Markdown-Download. | [Werkstatt-Prompts von A bis Z](./docs/werkstatt-und-schnellstart-coverage.md#werkstatt-prompts) |",
            f"| **Schnellstart-/Mini-Prompts** | {counts['schnellstart']} | Kompakte eigenständige Einstiege für den Kernworkflow und ein erstes belastbares Arbeitsprodukt. | [Schnellstart-Prompts von A bis Z](./docs/werkstatt-und-schnellstart-coverage.md#schnellstart-prompts) |",
            f"| **Testakten** | {counts['central_testakten']} zentral / {counts['testakten']} gesamt | Praxisnahe Dokumentensammlungen; jede Zeile skizziert den Fall, nennt passende Plugins und bietet drei Downloadformen. Drei weitere Akten liegen unmittelbar bei ihren Plugins. | [Zentrale Testakten mit Kurzbeschreibungen von A bis Z](./testakten/README.md#verfügbare-akten) · [pluginlokale Akten über den Plugin-Katalog](#was-ist-drin) |",
            "",
            f"Sortierlogik: Plugins, Werkstatt- und Schnellstart-Prompts folgen dem Plugin-Slug; Skills sind zuerst nach Plugin und dort nach Skill-Slug sortiert; Testakten folgen dem Aktenordner. Die großen Bestände bleiben auf eigenen, schnell ladenden Registerseiten, damit der Haupt-README trotz {counts['skills']} Skills benutzbar bleibt.",
            "",
            f"Plugin-Schnellwahl: {plugin_navigation}",
            DIRECTORY_END,
        ]
    )


def replace_directory(text: str, directory: str) -> str:
    if DIRECTORY_BEGIN not in text or DIRECTORY_END not in text:
        raise RuntimeError("Hauptverzeichnis-Markierungen in README.md fehlen")
    pattern = re.compile(
        re.escape(DIRECTORY_BEGIN)
        + r"[\s\S]*?"
        + re.escape(DIRECTORY_END)
    )
    return pattern.sub(directory, text, count=1)


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
    updated = replace_directory(original, build_directory(plugins))
    updated = replace_catalog(updated, build_catalog(plugins))
    README.write_text(updated, encoding="utf-8")
    print(
        "README.md: Hauptverzeichnis und vollständiger A-Z-Katalog "
        f"mit {len(plugins)} Plugins."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
