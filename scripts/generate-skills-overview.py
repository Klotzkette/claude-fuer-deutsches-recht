#!/usr/bin/env python3
"""
Generiert in jeder Plugin-README einen Abschnitt
'## Alle Skills im Überblick (automatisch generiert)'
am Ende der Datei. Der Abschnitt listet alle Skills mit Description
aus den jeweiligen SKILL.md-Dateien.

Aktualisiert vorhandene Beschreibungszellen anhand der Skillnamen.
Bestehende, manuell gepflegte Skills-Sektionen werden NICHT angetastet.
"""

from __future__ import annotations


if __name__ == "__main__":
    from generator_cli import parse_generator_cli

    parse_generator_cli(__doc__)

import re
import sys
import json
from pathlib import Path
from urllib.parse import quote

from skill_overview_text import description

BEGIN = "<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->"
END = "<!-- END SKILLS-OVERVIEW (auto-generated) -->"
REPO = Path(__file__).resolve().parent.parent
DOWNLOAD_BASE = "https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path="


def markdown_download_url(repo_path: str) -> str:
    return DOWNLOAD_BASE + quote(repo_path, safe="/")


def natural_key(text: str) -> list[object]:
    normalized = text.lower()
    if re.match(r"^lph\d", normalized):
        normalized = f"lphz-{normalized}"
    normalized = re.sub(r"(?<=[a-z])(?=\d)", "-", normalized)
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", normalized)]


def inventory_sentences(count: int) -> tuple[str, str]:
    if count == 1:
        return "Dieses Plugin enthält einen Skill.", "This plugin contains one skill."
    return (f"Automatisch generierte Komplett-Liste aller {count} Skills in diesem Plugin.",
            f"Complete list of all {count} skills in this plugin.")


def build_overview(plugin_dir: Path) -> str:
    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        return ""
    skills = sorted(
        (
            d.name
            for d in skills_dir.iterdir()
            if d.is_dir() and (d / "SKILL.md").is_file()
        ),
        key=natural_key,
    )
    if not skills:
        return ""

    inventory_de, inventory_en = inventory_sentences(len(skills))

    lines = [
        BEGIN,
        "",
        "## Alle Skills im Überblick",
        "",
        f"{inventory_de} "
        "Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. "
        "Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.",
        "",
        f"English: {inventory_en} Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.",
        "",
        "| Skill | Beschreibung | Markdown-Download |",
        "| --- | --- | --- |",
    ]
    plugin_rel = plugin_dir.relative_to(REPO).as_posix()
    for s in skills:
        desc = description(skills_dir / s / "SKILL.md", vergaberolle=plugin_dir.parent.name == "vergaberecht-werkstatt")
        download_url = markdown_download_url(f"{plugin_rel}/skills/{s}/SKILL.md")
        lines.append(
            f"| [`{s}`]({download_url}) | {desc} | "
            f"[MD herunterladen / Download MD]({download_url}) |"
        )
    lines.append("")
    lines.append(END)
    return "\n".join(lines)


SKILL_ROW = re.compile(
    r"^(?P<first>\| \[[^\]\n]+\]\((?:[^)\n]+/)?skills/(?P<slug>[a-z0-9-]+)/SKILL\.md\) \| )"
    r"(?P<description>.*?)(?P<last> \| \[.*?\|)$", re.MULTILINE
)


def updated_overview(original: str, overview: str) -> str:
    if BEGIN not in original and END not in original:
        return original.rstrip() + "\n\n" + overview + "\n"
    if original.count(BEGIN) != 1 or original.count(END) != 1:
        raise ValueError("Markierungsblock der Skillübersicht ist nicht eindeutig")
    start = original.index(BEGIN)
    end = original.index(END, start)
    block = original[start:end]
    desired = {row["slug"]: row for row in SKILL_ROW.finditer(overview)}
    old_rows = list(SKILL_ROW.finditer(block))
    existing = {row["slug"]: row for row in old_rows}
    if not desired or not existing or len(existing) != len(old_rows):
        raise ValueError("Skill-Tabelle fehlt oder enthält doppelte Zeilen")

    def updated(row):
        return row["first"] + desired[row["slug"]]["description"] + row["last"]

    if desired.keys() == existing.keys():
        block = SKILL_ROW.sub(updated, block)
    else:
        # Neue Skills erhalten die bestehende Tabellenform. Erläuterungen,
        # aufklappbare Abschnitte und zusätzliche Dateitabellen bleiben erhalten.
        first, last = old_rows[0], old_rows[-1]
        if block[first.start():last.end()].count("\n") + 1 != len(existing):
            raise ValueError("Skill-Zeilen sind nicht in einer zusammenhängenden Tabelle angeordnet")
        rows = []
        download_label = "Raw .md" if "| Skill | Beschreibung | Rohdatei |" in block else "MD herunterladen / Download MD"
        for slug, row in desired.items():
            if slug in existing:
                rows.append(updated(existing[slug]))
            else:
                rows.append(row.group().replace("[MD herunterladen / Download MD]", f"[{download_label}]"))
        block = block[:first.start()] + "\n".join(rows) + block[last.end():]
        old_count, new_count = len(existing), len(desired)
        for before, after in zip(inventory_sentences(old_count), inventory_sentences(new_count)):
            block = block.replace(before, after)
        block = block.replace(f"Katalog enthält {old_count} Skills", f"Katalog enthält {new_count} Skills")
        block = block.replace(f"Alle {old_count} Skills mit Beschreibung", f"Alle {new_count} Skills mit Beschreibung")
    return original[:start] + block + original[end:]


def update_readme(readme: Path, overview: str) -> bool:
    original = readme.read_text(encoding="utf-8")
    new = updated_overview(original, overview)
    if new == original:
        return False
    readme.write_text(new, encoding="utf-8")
    return True


def main() -> int:
    repo = REPO
    marketplace = json.loads((repo / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    changed = 0
    total = 0
    for plugin in marketplace["plugins"]:
        source = plugin.get("source") or f"./{plugin['name']}"
        plugin_dir = repo / source.removeprefix("./")
        readme = plugin_dir / "README.md"
        if not readme.is_file():
            print(f"  SKIP {plugin['name']}: keine README.md")
            continue
        overview = build_overview(plugin_dir)
        if not overview:
            continue
        total += 1
        if update_readme(readme, overview):
            changed += 1
            print(f"  UPD  {plugin_dir.name}")
    print(f"\nFertig: {changed}/{total} READMEs aktualisiert.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
