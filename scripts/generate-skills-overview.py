#!/usr/bin/env python3
"""
Generiert in jeder Plugin-README einen Abschnitt
'## Alle Skills im Überblick (automatisch generiert)'
am Ende der Datei. Der Abschnitt listet alle Skills mit Description
aus den jeweiligen SKILL.md-Dateien.

Idempotent: erkennt vorhandene Markierungsblöcke und ersetzt sie.
Bestehende, manuell gepflegte Skills-Sektionen werden NICHT angetastet.
"""

from __future__ import annotations

import re
import sys
import json
from pathlib import Path

from readme_display import display_prose

BEGIN = "<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->"
END = "<!-- END SKILLS-OVERVIEW (auto-generated) -->"
REPO = Path(__file__).resolve().parent.parent
RAW_BASE = "https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main"


def clean_description(desc: str) -> str:
    """Entfernt alte Generator-/Konsolidierungsfloskeln aus Tabellenbeschreibungen."""
    desc = re.sub(
        r"\s+[—-]\s*Arbeitskontext:\s*[^.]+,\s*Schwerpunkt\s+[^.]+\.?",
        "",
        desc,
    )
    desc = re.sub(r"\s+im Plugin\s+[^.:\"`|]+(?=[:.])", "", desc)
    desc = re.sub(r"\s+im Plugin\s+[^\"`|]+$", "", desc)
    desc = re.sub(r"\s{2,}", " ", desc)
    return desc.strip()


def read_description(skill_md: Path) -> str:
    """Liest description aus YAML-Frontmatter einer SKILL.md."""
    if not skill_md.is_file():
        return ""
    with skill_md.open("r", encoding="utf-8") as fh:
        first = fh.readline()
        if first.strip() != "---":
            return ""
        frontmatter_lines: list[str] = []
        for idx, line in enumerate(fh, start=1):
            if idx > 200:
                return ""
            if line.strip() == "---":
                break
            frontmatter_lines.append(line)
        else:
            return ""
    fm = "".join(frontmatter_lines)
    if not fm:
        return ""
    # description kann mehrzeilig (mit Anführungszeichen) oder einzeilig sein
    desc = ""
    for line in fm.splitlines():
        if line.startswith("description:"):
            desc = line.split(":", 1)[1].strip()
            break
    if not desc:
        return ""
    # Anführungszeichen entfernen
    if desc.startswith('"') and desc.endswith('"'):
        desc = desc[1:-1]
    # Pipes für Tabelle escapen, Zeilenumbrüche in Spaces
    desc = display_prose(clean_description(desc.replace("\n", " ").strip()))
    desc = desc.replace("|", "\\|").strip()
    # Lange Beschreibungen abkürzen
    if len(desc) > 240:
        desc = desc[:237].rstrip() + "..."
    return desc


def natural_key(text: str) -> list[object]:
    normalized = text.lower()
    if re.match(r"^lph\d", normalized):
        normalized = f"lphz-{normalized}"
    normalized = re.sub(r"(?<=[a-z])(?=\d)", "-", normalized)
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", normalized)]


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

    lines = [
        BEGIN,
        "",
        "## Alle Skills im Überblick",
        "",
        f"Automatisch generierte Komplett-Liste aller {len(skills)} Skills in diesem Plugin. "
        "Jeder Skillname öffnet die zugehörige `SKILL.md`; der Direktdownload lädt dieselbe Datei als Markdown. "
        "Beschreibungen stammen aus dem jeweiligen `description`-Feld.",
        "",
        "| Skill | Beschreibung | Markdown-Download |",
        "| --- | --- | --- |",
    ]
    plugin_rel = plugin_dir.relative_to(REPO).as_posix()
    for s in skills:
        desc = read_description(skills_dir / s / "SKILL.md")
        raw_url = f"{RAW_BASE}/{plugin_rel}/skills/{s}/SKILL.md"
        lines.append(
            f"| [`{s}`](skills/{s}/SKILL.md) | {desc} | "
            f'<a href="{raw_url}" download><code>SKILL.md</code></a> |'
        )
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
        # Ersetze bestehende Autogen-Blöcke und ziehe versehentliche
        # Duplikate zu genau einem aktuellen Block zusammen.
        start = new.find(BEGIN)
        end = new.rfind(END) + len(END)
        new = new[:start] + overview + new[end:]
    else:
        # Anhängen am Ende, mit Trenner
        sep = "" if new.endswith("\n\n") else ("\n" if new.endswith("\n") else "\n\n")
        new = new + sep + "\n" + overview + "\n"

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
