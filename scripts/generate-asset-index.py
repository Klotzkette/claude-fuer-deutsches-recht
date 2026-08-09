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

REPO = Path(__file__).resolve().parent.parent
OWNER = "Klotzkette"
NAME = "claude-fuer-deutsches-recht"
RELEASE = f"https://github.com/{OWNER}/{NAME}/releases/latest/download"
RAW = f"https://raw.githubusercontent.com/{OWNER}/{NAME}/main"


def source_rel(plugin: dict[str, str]) -> str:
    source = plugin.get("source") or f"./{plugin['name']}"
    return source.removeprefix("./")


def markdown_download(url: str, label: str) -> str:
    return f'<a href="{url}" download><code>{html.escape(label)}</code></a>'


def main() -> int:
    marketplace = json.loads((REPO / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    version = f"v{marketplace['version']}"
    plugins = marketplace["plugins"]

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
        f"| [`alle-skills-markdown.zip`]({RELEASE}/alle-skills-markdown.zip) | Alle Skills als Markdown-Bundles, zusätzlich pro Plugin einzeln im Komplettpaket. |",
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
        "Werkstatt- und Schnellstart-Prompts sind Markdown-Direkt-Downloads über `raw.githubusercontent.com`. Es gibt dafür keine eigenen ZIP-Assets im Release.",
        "",
        "| Plugin | Beschreibung | Werkstatt (Markdown) | Schnellstart (Markdown) | Plugin-ZIP | Navigation |",
        "| --- | --- | --- | --- | --- | --- |",
    ]

    for plugin in plugins:
        name = plugin["name"]
        rel = source_rel(plugin)
        description = html.escape(str(plugin.get("description", "")).replace("|", "\\|"))
        werkstatt_file = f"{name}-werkstatt.md"
        schnellstart_file = f"{name}-schnellstart.md"
        werkstatt_url = f"{RAW}/{rel}/{werkstatt_file}"
        schnellstart_url = f"{RAW}/{rel}/{schnellstart_file}"
        zip_url = f"{RELEASE}/{name}.zip"
        navigation = f"[README]({rel}/README.md) · [Skills](skills-index/{name}.md)"
        lines.append(
            "| "
            f"[`{name}`]({rel}/README.md) | "
            f"{description} | "
            f"{markdown_download(werkstatt_url, werkstatt_file)} | "
            f"{markdown_download(schnellstart_url, schnellstart_file)} | "
            f"[`{name}.zip`]({zip_url}) | "
            f"{navigation} |"
        )

    lines.append("")
    (REPO / "ASSET_INDEX.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"ASSET_INDEX.md: {len(plugins)} Plugins, Stand {version}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
