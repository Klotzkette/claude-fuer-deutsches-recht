#!/usr/bin/env python3
"""Generiert ASSET_INDEX.md aus marketplace.json.

Der Index ist bewusst rein datengetrieben: Plugin-Reihenfolge, Beschreibung,
Version und Source-Pfad kommen aus dem Marketplace. Dadurch können sich
Downloadspalten nicht durch Markdown-Tabellen-Umbauten verschieben.
"""

from __future__ import annotations

import html
import json
from pathlib import Path
from urllib.parse import quote

from readme_display import display_prose
from testakte_download_notices import ensure_download_notices

REPO = Path(__file__).resolve().parent.parent
OWNER = "Klotzkette"
NAME = "claude-fuer-deutsches-recht"
RELEASE = f"https://github.com/{OWNER}/{NAME}/releases/latest/download"
DOWNLOAD_BASE = f"https://{OWNER.lower()}.github.io/{NAME}/download.html?path="


def source_rel(plugin: dict[str, str]) -> str:
    source = plugin.get("source") or f"./{plugin['name']}"
    return source.removeprefix("./")


def markdown_download(repo_path: str, label: str) -> str:
    url = DOWNLOAD_BASE + quote(repo_path, safe="/")
    return f"[`{html.escape(label)}` herunterladen]({url})"


def group_label(name: str) -> str:
    first = name[:1].upper()
    return first if first.isalpha() else "0-9"


def plugin_groups(plugins: list[dict]) -> list[tuple[str, list[dict]]]:
    groups: dict[str, list[dict]] = {}
    for plugin in plugins:
        groups.setdefault(group_label(plugin["name"]), []).append(plugin)
    labels = sorted(groups, key=lambda value: (value != "0-9", value))
    return [(label, groups[label]) for label in labels]


def main() -> int:
    marketplace = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    version = f"v{marketplace['version']}"
    plugins = sorted(marketplace["plugins"], key=lambda plugin: plugin["name"].lower())
    groups = plugin_groups(plugins)

    lines: list[str] = [
        "# Release-Asset-Index",
        "",
        f"Stand: {version}, automatisch aktualisierte Asset-Übersicht",
        "",
        "[Repository-Start](README.md) · [Plugin-Katalog](README.md#was-ist-drin) · [Skill-Gesamtübersicht](SKILLS.md) · [Testakten](testakten/README.md) · [Aktueller Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest)",
        "",
        "## Sammel-Assets",
        "| Asset | Verwendung |",
        "| --- | --- |",
        f"| [`marketplace.json`]({RELEASE}/marketplace.json) | Marketplace-Manifest für alle Plugins. |",
        f"| [`alle-plugins-megazip.zip`]({RELEASE}/alle-plugins-megazip.zip) | Alle installierbaren Plugin-ZIPs plus `marketplace.json`. |",
        f"| [`alle-skills-markdown.zip`]({RELEASE}/alle-skills-markdown.zip) | Alle Skills samt zugehörigen Markdown-Referenzen als Markdown-Bundles, zusätzlich pro Plugin einzeln im Komplettpaket. |",
        f"| [`alle-testakten.zip`]({RELEASE}/alle-testakten.zip) | Sammelpaket der jeweils flachen Akten-ZIPs mit Originalformaten und zugehörigem Gesamt-PDF. |",
        f"| [`alle-testakten-einzelpdfs.zip`]({RELEASE}/alle-testakten-einzelpdfs.zip) | Sammelpaket der jeweils flachen Einzel-PDF-ZIPs; jede auswertbare Unterlage liegt darin als eigene A4-PDF vor. |",
        f"| [`alles-komplettpaket.zip`]({RELEASE}/alles-komplettpaket.zip) | Plugins, Skills, Testakten, Marketplace und Übersichten. Werkstatt und Schnellstart bleiben außerhalb der Archive als Markdown-Direktdownloads. |",
        f"| [`checksums-sha256.txt`]({RELEASE}/checksums-sha256.txt) | SHA-256-Prüfsummen für Release-Assets. |",
        "",
        "## Kanzleianleitungen",
        "| Dokument | Verwendung |",
        "| --- | --- |",
        "| "
        '<a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/docs/anbieterneutrale-schnittstelle-kanzlei.odt" download>'
        "<code>anbieterneutrale-schnittstelle-kanzlei.odt</code></a> | "
        "Anbieterneutrale Einrichtung, technischer Dummy-Test, Fachabnahme und Freigabevermerk für kleine Kanzleien. |",
        "",
        f"## Plugin-Assets ({len(plugins)} Stück)",
        "",
        "Alle Plugins sind alphabetisch sortiert. Werkstatt- und Schnellstart-Prompts werden über die statische Downloadseite als Markdown-Dateien gespeichert, statt in einer Quelltextvorschau geöffnet zu werden. Es gibt dafür keine eigenen ZIP-Assets im Release.",
        "",
        "English: Workshop and quick-start links download the unchanged Markdown files. README and skill-index links remain normal navigation pages.",
        "",
        " · ".join(f"[{label}](#{label.lower()})" for label, _ in groups),
        "",
    ]

    for label, items in groups:
        lines.extend(
            [
                f"### {label}",
                "",
                "| Plugin | Beschreibung | Werkstatt (Markdown) | Schnellstart (Markdown) | Plugin-ZIP | Navigation |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for plugin in items:
            name = plugin["name"]
            rel = source_rel(plugin)
            description = html.escape(
                display_prose(str(plugin.get("description", ""))).replace("|", "\\|")
            )
            werkstatt_file = f"{name}-werkstatt.md"
            schnellstart_file = f"{name}-schnellstart.md"
            werkstatt_path = f"{rel}/{werkstatt_file}"
            schnellstart_path = f"{rel}/{schnellstart_file}"
            zip_url = f"{RELEASE}/{name}.zip"
            navigation = f"[README]({rel}/README.md) · [Skills](skills-index/{name}.md)"
            lines.append(
                "| "
                f"[`{name}`]({rel}/README.md) | "
                f"{description} | "
                f"{markdown_download(werkstatt_path, werkstatt_file)} | "
                f"{markdown_download(schnellstart_path, schnellstart_file)} | "
                f"[`{name}.zip`]({zip_url}) | "
                f"{navigation} |"
            )
        lines.append("")

    (REPO / "ASSET_INDEX.md").write_text(ensure_download_notices("\n".join(lines)), encoding="utf-8")
    print(f"ASSET_INDEX.md: {len(plugins)} Plugins, Stand {version}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
