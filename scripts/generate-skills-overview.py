#!/usr/bin/env python3
"""
Generiert in jeder Plugin-README einen Abschnitt
'## Alle Skills im Ueberblick (automatisch generiert)'
am Ende der Datei. Der Abschnitt listet alle Skills mit Description
aus den jeweiligen SKILL.md-Dateien.

Idempotent: erkennt vorhandene Markierungsblöcke und ersetzt sie.
Bestehende, manuell gepflegte Skills-Sektionen werden NICHT angetastet.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

BEGIN = "<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->"
END = "<!-- END SKILLS-OVERVIEW (auto-generated) -->"


def read_description(skill_md: Path) -> str:
    """Liest description aus YAML-Frontmatter einer SKILL.md."""
    if not skill_md.is_file():
        return ""
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return ""
    fm = m.group(1)
    # description kann mehrzeilig (mit Anführungszeichen) oder einzeilig sein
    dm = re.search(r"^description:\s*(.+?)(?=\n[a-zA-Z_-]+:|\Z)", fm, re.DOTALL | re.MULTILINE)
    if not dm:
        return ""
    desc = dm.group(1).strip()
    # Anfuehrungszeichen entfernen
    if desc.startswith('"') and desc.endswith('"'):
        desc = desc[1:-1]
    # Pipes für Tabelle escapen, Zeilenumbrueche in Spaces
    desc = desc.replace("\n", " ").replace("|", "\\|").strip()
    # Lange Beschreibungen abkuerzen
    if len(desc) > 240:
        desc = desc[:237].rstrip() + "..."
    return desc


def build_overview(plugin_dir: Path) -> str:
    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        return ""
    skills = sorted(
        d.name
        for d in skills_dir.iterdir()
        if d.is_dir() and (d / "SKILL.md").is_file()
    )
    if not skills:
        return ""

    lines = [
        BEGIN,
        "",
        "## Alle Skills im Ueberblick",
        "",
        f"Automatisch generierte Komplett-Liste aller {len(skills)} Skills in diesem Plugin. "
        "Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.",
        "",
        "| Skill | Beschreibung |",
        "| --- | --- |",
    ]
    for s in skills:
        desc = read_description(skills_dir / s / "SKILL.md")
        lines.append(f"| `{s}` | {desc} |")
    lines.append("")
    lines.append(END)
    return "\n".join(lines)


def update_readme(readme: Path, overview: str) -> bool:
    """Returns True if file was changed."""
    if not overview:
        return False
    original = readme.read_text(encoding="utf-8") if readme.is_file() else ""
    new = original

    if BEGIN in new and END in new:
        # Ersetze bestehenden Block
        new = re.sub(
            re.escape(BEGIN) + r".*?" + re.escape(END),
            overview,
            new,
            count=1,
            flags=re.DOTALL,
        )
    else:
        # Anhaengen am Ende, mit Trenner
        sep = "" if new.endswith("\n\n") else ("\n" if new.endswith("\n") else "\n\n")
        new = new + sep + "\n" + overview + "\n"

    if new == original:
        return False
    readme.write_text(new, encoding="utf-8")
    return True


def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    os.chdir(repo)
    changed = 0
    total = 0
    for plugin_json in sorted(repo.glob("*/.claude-plugin/plugin.json")):
        plugin_dir = plugin_json.parent.parent
        readme = plugin_dir / "README.md"
        if not readme.is_file():
            print(f"  SKIP {plugin_dir.name}: keine README.md")
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
