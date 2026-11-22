#!/usr/bin/env python3
"""Erzeugt den vollständigen Plugin-Katalog in der Repository-README."""

from __future__ import annotations


if __name__ == "__main__":
    from generator_cli import parse_generator_cli

    parse_generator_cli(__doc__)

import json
import re
from pathlib import Path
from release_routing import rewrite_case_asset_urls, validate_plugin_version, validate_version

from readme_display import catalog_description
from testakte_zip_common import working_dump_flat_pairs


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
README = REPO / "README.md"
TESTAKTEN_README = REPO / "testakten" / "README.md"
DIRECTORY_BEGIN = "<!-- BEGIN HAUPTVERZEICHNIS (auto-generated) -->"
DIRECTORY_END = "<!-- END HAUPTVERZEICHNIS (auto-generated) -->"
BEGIN = "<!-- BEGIN PLUGIN-KATALOG (auto-generated) -->"
END = "<!-- END PLUGIN-KATALOG (auto-generated) -->"
SKIP_TESTAKTEN = {"formatvorlagen-paradebeispiele", "megaprompts"}


def source_rel(plugin: dict) -> str:
    source = plugin.get("source") or f"./{plugin['name']}"
    return source.removeprefix("./")


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
    # Die Vergabewerkstatt wird aus ihrem eigenen Marketplace installiert.
    suites = {REPO / "vergaberecht-werkstatt/testakten"}
    suites.update(REPO / source_rel(plugin) / "testakten" for plugin in plugins)
    separate_testakten = sum(
        1 for suite in suites for readme in suite.glob("*/README.md")
        if readme.parent.name not in SKIP_TESTAKTEN and (readme.parent / "gesamt-pdf").is_dir()
    )
    return {
        "plugins": len(plugins),
        "skills": skills,
        "werkstatt": werkstatt,
        "schnellstart": schnellstart,
        "central_testakten": central_testakten,
        "testakten": central_testakten + pluginlocal_testakten + separate_testakten,
        "separate_testakten": separate_testakten,
    }


def build_directory(plugins: list[dict]) -> str:
    counts = inventory_counts(plugins)
    return "\n".join(
        [
            DIRECTORY_BEGIN,
            "| Bestand | Umfang | Kurzbeschreibung | Vollständige alphabetische Liste |",
            "| --- | ---: | --- | --- |",
            f"| **Plugins** | {counts['plugins']} | Installierbare Fachpakete | [Katalog](#was-ist-drin) · [Downloads](./ASSET_INDEX.md) |",
            f"| **Skills** | {counts['skills']} | Arbeitsabläufe für einzelne Aufgaben | [Alle Skills](./SKILLS.md) · [Einzeldownloads je Plugin](./skills-index/) |",
            f"| **Werkstatt-Prompts** | {counts['werkstatt']} | Ausführliche Anweisungen für mehrstufige Vorgänge | [Werkstatt auswählen](./docs/werkstatt-und-schnellstart-coverage.md#werkstatt-prompts) |",
            f"| **Schnellstart-/Mini-Prompts** | {counts['schnellstart']} | Kurze Anweisungen für den Einstieg im Chat | [Mini-Prompt auswählen](./docs/werkstatt-und-schnellstart-coverage.md#schnellstart-prompts) |",
            f"| **Testakten** | {counts['central_testakten']} zentral / {counts['testakten']} gesamt | Übungsfälle mit Arbeitsaufträgen und Unterlagen | [Zentrale Sammlung](./testakten/README.md#verfügbare-akten) · [Akten einzelner Plugins](#testakten) |",
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
                f'<a id="{label.lower()}"></a>',
                "<details>",
                f"<summary>{label}</summary>",
                "",
                "| Plugin | Beschreibung |",
                "| --- | --- |",
            ]
        )
        for plugin in groups[label]:
            name = plugin["name"]
            description = catalog_description(plugin, REPO / source_rel(plugin))
            lines.append(f"| [`{name}`](./{source_rel(plugin)}) | {description} |")
        lines.extend(["", "</details>", ""])
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


def update_testakten_version(text: str, version: str, central_count: int | None = None) -> str:
    updated, count = re.subn(
        r"^Stand v\d+\.\d+\.\d+(?=:)",
        lambda _: "Stand v" + version,
        text,
        flags=re.MULTILINE,
    )
    if count != 1:
        raise RuntimeError("Eindeutiger Versionsstand in testakten/README.md fehlt")
    if central_count is not None:
        updated, count = re.subn(
            r"^(Stand v\d+\.\d+\.\d+: )\d+(?= zentrale Testakten)",
            lambda match: match[1] + str(central_count),
            updated,
            flags=re.MULTILINE,
        )
        if count != 1:
            raise RuntimeError("Eindeutige Aktenzahl in testakten/README.md fehlt")
    return updated


def build_subject_index(plugins: list[dict], version: str) -> str:
    skill_count = sum(sum(1 for _ in (REPO / source_rel(p) / "skills").glob("*/SKILL.md")) for p in plugins)
    lines = [
        "# Rechtsgebiete und Plugins in diesem Repository", "",
        "Vollständiger alphabetischer Katalog mit Kurzbeschreibung, Paketversion und Skill-Quellbestand. Große Spezialserien werden im installierten Paket teilweise über Fachrouter geöffnet; die Zahl ist deshalb keine Zusage entsprechend vieler Menüeinträge.", "",
        "[Startseite](../README.md) · [Skills und Einzel-Downloads](../SKILLS.md) · [Werkstatt und Mini](../docs/werkstatt-und-schnellstart-coverage.md) · [Downloads](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)", "",
        f"Stand v{version}: {len(plugins)} Plugins, {skill_count} Skills.", "",
        "| Plugin | Beschreibung | Version | Skills |", "| --- | --- | --- | ---: |",
    ]
    for plugin in sorted(plugins, key=lambda p: p["name"]):
        source = source_rel(plugin)
        count = sum(1 for _ in (REPO / source / "skills").glob("*/SKILL.md"))
        description = catalog_description(plugin, REPO / source_rel(plugin))
        lines.append(f"| [`{plugin['name']}`](../{source}/) | {description} | `{plugin['version']}` | {count} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    plugins = marketplace["plugins"]
    original = README.read_text(encoding="utf-8")
    updated = replace_directory(original, build_directory(plugins))
    updated = replace_catalog(updated, build_catalog(plugins))
    counts = inventory_counts(plugins)
    updated = update_summary_counts(updated, counts)
    updated = re.sub(r"(\| \*\*Skills \(SKILL\.md\)\*\* \| )\d+", lambda m: m[1] + str(counts["skills"]), updated)
    version = validate_version(marketplace["version"])
    for plugin in plugins:
        validate_plugin_version(plugin, version, root=REPO)
    updated = re.sub(r"(\| \*\*Plugin-Version / Arbeitsstand\*\* \| `)v\d+\.\d+\.\d+", lambda m: m[1] + "v" + version, updated)
    testakten = update_testakten_version(TESTAKTEN_README.read_text(encoding="utf-8"), version, counts["central_testakten"])
    updated = rewrite_case_asset_urls(updated, version=marketplace["version"])
    testakten = rewrite_case_asset_urls(testakten, version=marketplace["version"])
    README.write_text(updated, encoding="utf-8")
    TESTAKTEN_README.write_text(testakten, encoding="utf-8")
    (REPO / "references" / "rechtsgebiete-uebersicht.md").write_text(
        build_subject_index(plugins, version), encoding="utf-8"
    )
    print(
        "README.md: Hauptverzeichnis und vollständiger A-Z-Katalog "
        f"mit {len(plugins)} Plugins."
    )
    return 0


def update_summary_counts(text: str, counts: dict[str, int]) -> str:
    text = re.sub(
        r"(\| \*\*Plugins\*\* \| )\d+\b",
        lambda match: match[1] + str(counts["plugins"]),
        text,
    )
    return re.sub(
        r"(\| \*\*Testakten\*\* \| )\d+ zentral / \d+ gesamt(?= \|)",
        lambda match: match[1] + f"{counts['central_testakten']} zentral / {counts['testakten']} gesamt",
        text,
    )


if __name__ == "__main__":
    raise SystemExit(main())
