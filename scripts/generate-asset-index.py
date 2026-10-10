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
from release_routing import RELEASE_BASE, case_asset_url, companion_case_groups, companion_cases, companion_tag, plugin_asset_url

from prompt_profiles import enabled, formats
from urllib.parse import quote

from readme_display import display_plugin_description
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


def companion_section(version: str) -> list[str]:
    slugs = companion_cases()
    if not slugs:
        return []
    tags = [companion_tag(version, part) for part, _ in enumerate(companion_case_groups(slugs), 1)]
    release_links = ", ".join(f"[`{tag}`]({RELEASE_BASE}/tag/{tag})" for tag in tags)
    lines = [
        "## Akten-Begleitrelease",
        "",
        f"Die Akten-ZIPs liegen grundsätzlich in den versionsgleichen Begleitreleases {release_links}. "
        "Je Teil werden höchstens 499 Akten mit beiden ZIP-Varianten und einer eigenen Prüfsummenliste veröffentlicht. "
        "Die vollständigen Akten-Sammelpakete und `alles-komplettpaket.zip` bleiben im Hauptrelease. "
        "Ein ausdrücklich verlinktes Komponentenrelease kann eine neue Akte bereits vor dem nächsten vollständigen Release bereitstellen. Maßgeblich ist der jeweilige Downloadlink.",
        "",
        "| Akte | Originaldateien | Einzel-PDFs |",
        "| --- | --- | --- |",
    ]
    for slug in slugs:
        lines.append(
            f"| [{slug}](testakten/{slug}/README.md) | "
            f"[Akten-ZIP]({case_asset_url(slug, version=version)}) | "
            f"[Einzel-PDF-ZIP]({case_asset_url(slug, '-einzelpdfs', version=version)}) |"
        )
    lines.extend([
        "",
        "Prüfsummen: " + ", ".join(f"[SHA-256 `{tag}`]({RELEASE_BASE}/download/{tag}/checksums-sha256.txt)" for tag in tags) + ". "
        "Jede Prüfsummenliste gilt ausschließlich für die Dateien ihres eigenen Releases.",
        "",
    ])
    return lines


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
        "[Repository-Start](README.md) · [Plugin-Katalog](README.md#was-ist-drin) · [Skill-Gesamtübersicht](SKILLS.md) · [Schwerpunkt-Prompts](SCHWERPUNKTE.md) · [HOAI-Phasen-Werkstätten](docs/bauwirtschaft-hoai-phasen.md) · [Qualitätslabor](QUALITY.md) · [Testakten](testakten/README.md) · [Aktueller Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest)",
        "",
        "## Sammel-Assets",
        "",
        "Die allgemeinen Sammelpakete v445.35.3 enthalten den geprüften Bestand vom 9. Oktober 2026 mit 297 Plugins. Spätere Komponenten ergänzen den Repository-Bestand, ohne diese unveränderten Archive nachträglich zu erweitern. Bei der [Rechtsabteilung Forderungsmanagement Immobilienunternehmen](./projekte/rechtsabteilung-forderungsmanagement-immobilienunternehmen/README.md) ist das installierbare Rollen-Plugin zusätzlich im Plugin-Sammelpaket enthalten. Der gesonderte Projektbestand mit seinen zusätzlichen Akten und der Vollkopie bleibt über die Projektübersicht zugänglich.",
        "",
        "[Due Diligence 1.0.0](./due-diligence/README.md) mit elf Skills und drei DD-Akten sowie [GVB-Reinigungsvergabe 1.0.0](./gvb-reinigungsvergabe/README.md) sind gesonderte Komponenten vom 10. Oktober 2026. Ihre aktuellen Einzelpakete sind über die jeweiligen Pluginseiten erreichbar; sie fehlen in den unveränderten Sammelarchiven v445.35.3.",
        "",
        "Die drei Rollen-Plugins der [Vergaberecht-Werkstatt](./vergaberecht-werkstatt/README.md) gehören zum Plugin-Sammelpaket. Die sieben gesondert verwalteten Akten und die Projektkopie bleiben über das Komponentenrelease erreichbar. Die Plugin-Einzelzeilen unten behalten ihre ausdrücklich zugeordneten Komponentendownloads.",
        "",
        f"[Betreuungsrecht 445.33.3](./betreuungsrecht/README.md) ergänzt den Unterlagen-Auswerter, eine [eigenständige Unterlagen-Werkstatt]({DOWNLOAD_BASE}betreuungsrecht/betreuungsrecht-unterlagen-werkstatt.md), eine [Excel-Vorlage](./betreuungsrecht/templates/unterlagen-abrechnung.xlsx) und die Dreijahresakte Adelheid Pfister. Plugin und zentrale Akte sind ab v445.35.3 zusätzlich in den Sammelarchiven enthalten; die Werkstatt bleibt ein eigenständiger Download.",
        "[Gesellschafterstreit 445.34.2](./gesellschafterstreit/README.md) erweitert die Berliner Testakte um eine ausführliche Klage mit den Anlagen K1–K9 und einen Vergleichsnachtrag mit Vertragsentwurf und E-Mails. Plugin und Akten sind ab v445.35.3 auch in den allgemeinen Paketen enthalten.",
        "[Geldwäschebeauftragter 445.34.0](./geldwaeschebeauftragter/README.md) ergänzt elf Skills, drei eigenständige Prompts und drei zentrale Akten für Unternehmen, Kanzlei und Notariat. Plugin und Akten gehören ab v445.35.3 zusätzlich zu den allgemeinen Sammelpaketen.",
        "[KI-Verordnung 445.35.2](./ki-vo-ai-act-pruefer/README.md) aktualisiert den Hauptprüfer und vier Spezialwege für verbotene Praktiken, Hochrisiko, Register/Meldungen und Konformität. Die 80 betroffenen Plugins und die zentralen Fallakten sind ab v445.35.3 auch über die allgemeinen Sammlungen zugänglich.",
        "",
        "",
        "| Asset | Verwendung |",
        "| --- | --- |",
        f"| [`marketplace.json`]({RELEASE}/marketplace.json) | Marketplace-Manifest des Sammelreleases vom 9. Oktober 2026; den aktuellen Bestand zeigt die Repository-Datei `.claude-plugin/marketplace.json`. |",
        f"| [`alle-plugins-megazip.zip`]({RELEASE}/alle-plugins-megazip.zip) | Die 297 installierbaren Plugin-ZIPs des Sammelreleases vom 9. Oktober 2026 plus dessen `marketplace.json`. |",
        f"| [`alle-skills-markdown.zip`]({RELEASE}/alle-skills-markdown.zip) | Skills des Sammelstands vom 9. Oktober 2026 samt zugehörigen Markdown-Referenzen als Markdown-Bundles, zusätzlich pro Plugin einzeln im Komplettpaket. |",
        f"| [`alle-testakten.zip`]({RELEASE}/alle-testakten.zip) | Sammelpaket der zentralen Akten-ZIPs mit Originalformaten und zugehörigem Gesamt-PDF. Ausdrücklich strukturierte Projektakten behalten ihre Unterordner. |",
        f"| [`alle-testakten-einzelpdfs.zip`]({RELEASE}/alle-testakten-einzelpdfs.zip) | Sammelpaket der zentralen Einzel-PDF-ZIPs; jede auswertbare Unterlage liegt als eigene A4-PDF vor. Strukturierte Projektakten behalten ihre Unterordner. |",
        f"| [`alle-pluginlokalen-testakten.zip`]({RELEASE}/alle-pluginlokalen-testakten.zip) | Ergänzende Sammlung der Akten aus den `testakte/`-Ordnern einzelner Plugins in Originalformaten und mit zugehörigem Gesamt-PDF. |",
        f"| [`alle-pluginlokalen-testakten-einzelpdfs.zip`]({RELEASE}/alle-pluginlokalen-testakten-einzelpdfs.zip) | Dieselben pluginlokalen Akten als Einzel-PDF-ZIPs mit einer separaten PDF je Unterlage. |",
        f"| [`alles-komplettpaket.zip`]({RELEASE}/alles-komplettpaket.zip) | Plugins, Skills, Testakten, Marketplace und Übersichten. Werkstatt und Schnellstart bleiben außerhalb der Archive als Markdown-Direktdownloads. |",
        f"| [`checksums-sha256.txt`]({RELEASE}/checksums-sha256.txt) | SHA-256-Prüfsummen für die Assets des Hauptreleases. |",
        "",
        *companion_section(marketplace["version"]),
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
                "| Plugin | Beschreibung | Werkstatt (Markdown) | Schnellstart (Markdown) | Schwerpunkt (Markdown) | Plugin-ZIP | Navigation |",
                "| --- | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for plugin in items:
            name = plugin["name"]
            rel = source_rel(plugin)
            description = html.escape(
                display_plugin_description(str(plugin.get("description", "")), REPO / rel).replace("|", "\\|")
            )
            werkstatt_file = f"{name}-werkstatt.md"
            schnellstart_file = f"{name}-schnellstart.md"
            werkstatt_path = f"{rel}/{werkstatt_file}"
            schnellstart_path = f"{rel}/{schnellstart_file}"
            focus_path = f"{rel}/{name}-hauptproblem.md"
            focus_download = " · ".join(markdown_download(f"{rel}/{name}-hauptproblem.{ext}", f"{name}-hauptproblem.{ext}") for ext in formats(name) if (REPO / f"{rel}/{name}-hauptproblem.{ext}").is_file()) if (REPO / focus_path).is_file() else "Nicht vorgesehen"
            workshop_download = " · ".join(markdown_download(f"{rel}/{name}-werkstatt.{ext}", f"{name}-werkstatt.{ext}") for ext in formats(name)) if enabled(name, "werkstatt") else "Nicht vorgesehen"
            quickstart_download = " · ".join(markdown_download(f"{rel}/{name}-schnellstart.{ext}", f"{name}-schnellstart.{ext}") for ext in formats(name)) if enabled(name, "schnellstart") else "Nicht vorgesehen"
            zip_url = plugin_asset_url(name, root=REPO)
            navigation = f"[README]({rel}/README.md) · [Skills](skills-index/{name}.md)"
            lines.append(
                "| "
                f"[`{name}`]({rel}/README.md) | "
                f"{description} | "
                f"{workshop_download} | "
                f"{quickstart_download} | "
                f"{focus_download} | "
                f"[`{name}.zip`]({zip_url}) | "
                f"{navigation} |"
            )
        lines.append("")

    (REPO / "ASSET_INDEX.md").write_text(ensure_download_notices("\n".join(lines)), encoding="utf-8")
    print(f"ASSET_INDEX.md: {len(plugins)} Plugins, Stand {version}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
