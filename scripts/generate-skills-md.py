#!/usr/bin/env python3
"""Generiert die globale SKILLS.md (Skill-Gesamtuebersicht) aus dem Repo.

Wird bei jeder Release-Vorbereitung gelaufen. Garantiert, dass jeder neue
Skill, der irgendwo unter <plugin>/skills/<skill>/SKILL.md angelegt wird,
automatisch in der SKILLS.md auftaucht — mit:

- Direkt-Download des SKILL.md als rohe Markdown-Datei (im Browser per
  Rechtsklick "Ziel speichern unter" oder "?raw=1" laedt sofort herunter).
- Pro Plugin: ZIP-Download-Link auf das Release-Asset
  https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/<plugin>.zip
- Oben prominenter Hinweis: Skills sind reine Markdown-Prompts und
  funktionieren per Copy-Paste in jedem Chatbot.

Idempotent: schreibt SKILLS.md neu. Liest Version aus marketplace.json.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GH_OWNER = "Klotzkette"
GH_REPO = "claude-fuer-deutsches-recht"
GH_BLOB = f"https://github.com/{GH_OWNER}/{GH_REPO}/blob/main"
GH_RAW = f"https://raw.githubusercontent.com/{GH_OWNER}/{GH_REPO}/main"
GH_RELEASE = f"https://github.com/{GH_OWNER}/{GH_REPO}/releases/latest/download"
SKILLS_INDEX_DIR = REPO_ROOT / "skills-index"


def read_description(skill_md: Path) -> str:
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return ""
    fm = m.group(1)
    dm = re.search(
        r"^description:\s*(.+?)(?=\n[a-zA-Z_-]+:|\Z)",
        fm,
        re.DOTALL | re.MULTILINE,
    )
    if not dm:
        return ""
    desc = dm.group(1).strip()
    if desc.startswith('"') and desc.endswith('"'):
        desc = desc[1:-1]
    desc = desc.replace("\n", " ").replace("|", "\\|").strip()
    if len(desc) > 280:
        desc = desc[:277].rstrip() + "..."
    return desc


def collect_plugins() -> list[tuple[str, list[str]]]:
    """Liest Plugin-Reihenfolge aus marketplace.json und scannt jeden Plugin-Ordner."""
    market = json.loads((REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text())
    out: list[tuple[str, list[str]]] = []
    for plugin in market["plugins"]:
        name = plugin["name"]
        skills_dir = REPO_ROOT / name / "skills"
        if not skills_dir.is_dir():
            continue
        skills = sorted(
            d.name
            for d in skills_dir.iterdir()
            if d.is_dir() and (d / "SKILL.md").is_file()
        )
        if skills:
            out.append((name, skills))
    return out


def header(total_skills: int, total_plugins: int, version: str) -> str:
    megazip = f"{GH_RELEASE}/alle-plugins-megazip.zip"
    komplett = f"{GH_RELEASE}/alles-komplettpaket.zip"
    return f"""# Skill-Gesamtuebersicht

Automatisch generierte Gesamtuebersicht aller **{total_skills} Skills** in **{total_plugins} Plugins**.

Stand: `{version}`.

## ⬇️ Alle Skills auf einmal herunterladen

| Paket | Inhalt | Download |
| --- | --- | --- |
| **Alle Skills (kompakt)** | Alle {total_plugins} Plugin-ZIPs in einem Archiv (ca. 11 MB) | [`alle-plugins-megazip.zip`]({megazip}) |
| **Komplettpaket (alles)** | Plugins + Testakten + Uebersichten (ca. 80 MB) | [`alles-komplettpaket.zip`]({komplett}) |

Das erste Paket reicht, wenn man nur die Prompts (Skills) braucht. Das zweite enthaelt zusaetzlich die 63 Testakten und alle Repo-Uebersichten.

Wer nur **ein bestimmtes Plugin** will: weiter unten in der Plugin-Tabelle pro Plugin ein eigener `[Download]`-Link.

## Worum es hier geht: alles nur grosse Prompts

Diese Skills sind am Ende **nichts weiter als grosse, sehr sorgfaeltig formulierte System-Prompts in Markdown**. Sie wurden fuer das Claude-Code-Plugin-System geschrieben, **funktionieren aber in jedem anderen Chatbot genauso**.

So benutzt man einen Skill ausserhalb von Claude Code:

1. Unten in der Plugin-Tabelle auf das gewuenschte Plugin klicken — die Detailseite mit allen Skills oeffnet sich.
2. Auf der Detailseite den gewuenschten Skill suchen und `[Markdown]` klicken — die Datei `SKILL.md` oeffnet sich im Browser.
3. **Entweder** den kompletten Text mit `Strg+A` / `Cmd+A` kopieren und in den Chat einfuegen (ChatGPT, Mistral, Gemini, DeepSeek, Le Chat, ...).
4. **Oder** auf `[Raw .md]` klicken und die Datei direkt herunterladen, dann als Anhang in den Chatbot ziehen oder den Inhalt einfuegen.
5. Danach die eigene Frage / das eigene Dokument hinterherschicken — der Chatbot uebernimmt die Rolle aus dem Skill.

So bekommt man die komplette Sammlung als ZIP:

- In der Plugin-Tabelle unten in der Spalte **ZIP** auf den Download-Link klicken. Das laedt eine ZIP-Datei mit **allen** Skills dieses Plugins (mitsamt Hilfsdateien, Pruefrastern und Vorlagen).
- Wer Claude Code nutzt, kann das ZIP direkt als Plugin installieren. Alle anderen koennen die enthaltenen `SKILL.md`-Dateien einzeln in jeden Chatbot kopieren.

**Wichtig:** Wenn irgendwo im Repo ein neuer Skill angelegt wird (also ein neuer Ordner `<plugin>/skills/<skill>/SKILL.md`), erscheint er beim naechsten Lauf von `scripts/generate-skills-md.py` automatisch -- sowohl in dieser Liste als auch auf der jeweiligen Plugin-Detailseite. Es kann also nichts fehlen.

Die Detailseiten liegen unter [`skills-index/`](skills-index/) -- eine eigene `.md`-Datei pro Plugin. So bleibt diese Hauptseite klein und laedt schnell, statt mit 2617 Tabellenzeilen den Browser-Renderer von GitHub zu ueberfordern.

"""


def plugin_overview_table(plugins: list[tuple[str, list[str]]]) -> str:
    lines = [
        "## Alle Plugins",
        "",
        "Pro Plugin: Klick auf den Namen oeffnet die Detailseite mit allen Skills, Beschreibungen und Einzel-Downloads. **ZIP** laedt die komplette Plugin-Sammlung direkt.",
        "",
        "| Plugin | Skills | Detailseite | ZIP |",
        "| --- | ---: | --- | --- |",
    ]
    for name, skills in plugins:
        zip_url = f"{GH_RELEASE}/{name}.zip"
        detail = f"skills-index/{name}.md"
        lines.append(
            f"| **{name}** | {len(skills)} | [Skills ansehen]({detail}) | [Download]({zip_url}) |"
        )
    lines.append("")
    return "\n".join(lines)


def plugin_detail_page(name: str, skills: list[str], version: str) -> str:
    skills_dir = REPO_ROOT / name / "skills"
    plugin_zip = f"{GH_RELEASE}/{name}.zip"
    plugin_readme = f"{GH_BLOB}/{name}/README.md"
    lines = [
        f"# {name}",
        "",
        f"**{len(skills)} Skills** · Stand `{version}`",
        "",
        f"- [← Zurueck zur Gesamtuebersicht](../SKILLS.md)",
        f"- [Plugin-README]({plugin_readme})",
        f"- [Alle Skills als ZIP herunterladen]({plugin_zip}) (komplettes Plugin)",
        "",
        "## So benutzt man einen Skill",
        "",
        "Skills sind reine Markdown-Prompts und funktionieren in jedem Chatbot (ChatGPT, Mistral, Gemini, DeepSeek, Le Chat, ...).",
        "",
        "- **`[Markdown]`** oeffnet die `SKILL.md` im Browser. Inhalt mit `Strg+A` / `Cmd+A` kopieren und in den Chat einfuegen.",
        "- **`[Raw .md]`** laedt die Datei direkt herunter. Als Anhang in den Chatbot ziehen oder Inhalt einfuegen.",
        "",
        "## Skills in diesem Plugin",
        "",
        "| Skill | Beschreibung | Download |",
        "| --- | --- | --- |",
    ]
    for s in skills:
        skill_md = skills_dir / s / "SKILL.md"
        desc = read_description(skill_md)
        rel_md = f"{name}/skills/{s}/SKILL.md"
        blob_url = f"{GH_BLOB}/{rel_md}"
        raw_url = f"{GH_RAW}/{rel_md}"
        lines.append(
            f"| [`{s}`]({blob_url}) | {desc} | [Markdown]({blob_url}) · [Raw .md]({raw_url}) |"
        )
    lines.append("")
    return "\n".join(lines)


def write_detail_index(plugins: list[tuple[str, list[str]]], version: str) -> str:
    """Schreibt skills-index/README.md mit Liste aller Detailseiten."""
    lines = [
        "# Skills-Index: Detailseiten pro Plugin",
        "",
        f"Eine Detailseite pro Plugin mit allen Skills, Beschreibungen und Einzel-Downloads. Stand: `{version}`.",
        "",
        "Die Aufteilung verhindert, dass GitHubs Markdown-Renderer bei 2600+ Tabellenzeilen abstuerzt oder die Seite endlos neu laedt.",
        "",
        "- [← Zurueck zur Gesamtuebersicht](../SKILLS.md)",
        "",
        "## Alle Detailseiten",
        "",
    ]
    for name, skills in plugins:
        lines.append(f"- [{name}](./{name}.md) ({len(skills)} Skills)")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    plugins = collect_plugins()
    total_skills = sum(len(skills) for _, skills in plugins)
    total_plugins = len(plugins)
    version = (
        "v" + json.loads((REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text())["version"]
    )

    # 1) Schlanke Hauptseite SKILLS.md
    main_text = (
        header(total_skills, total_plugins, version)
        + plugin_overview_table(plugins)
    )
    main_text = main_text.rstrip() + "\n"
    out_main = REPO_ROOT / "SKILLS.md"
    out_main.write_text(main_text, encoding="utf-8")

    # 2) Detailseiten pro Plugin
    SKILLS_INDEX_DIR.mkdir(exist_ok=True)
    # Alte Detailseiten loeschen, falls Plugins entfernt wurden
    current_names = {name for name, _ in plugins} | {"README"}
    for old in SKILLS_INDEX_DIR.glob("*.md"):
        if old.stem not in current_names:
            old.unlink()
    for name, skills in plugins:
        page = plugin_detail_page(name, skills, version)
        (SKILLS_INDEX_DIR / f"{name}.md").write_text(page.rstrip() + "\n", encoding="utf-8")
    # Index der Detailseiten
    idx = write_detail_index(plugins, version)
    (SKILLS_INDEX_DIR / "README.md").write_text(idx.rstrip() + "\n", encoding="utf-8")

    print(
        f"SKILLS.md: {len(main_text)} Zeichen ({total_plugins} Plugins). "
        f"skills-index/: {total_plugins} Detailseiten + Index. "
        f"Insgesamt {total_skills} Skills, Stand {version}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
