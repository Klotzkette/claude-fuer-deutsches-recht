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
    return f"""# Skill-Gesamtuebersicht

Automatisch generierte Gesamtuebersicht aller **{total_skills} Skills** in **{total_plugins} Plugins**.

Stand: `{version}`.

## Worum es hier geht: alles nur grosse Prompts

Diese Skills sind am Ende **nichts weiter als grosse, sehr sorgfaeltig formulierte System-Prompts in Markdown**. Sie wurden fuer das Claude-Code-Plugin-System geschrieben, **funktionieren aber in jedem anderen Chatbot genauso**.

So benutzt man einen Skill ausserhalb von Claude Code:

1. In der Tabelle unten den gewuenschten Skill suchen.
2. Auf `[Markdown]` klicken — die Datei `SKILL.md` oeffnet sich im Browser.
3. **Entweder** den kompletten Text mit `Strg+A` / `Cmd+A` kopieren und in den Chat einfuegen (ChatGPT, Mistral, Gemini, DeepSeek, Le Chat, ...).
4. **Oder** auf `[Raw .md]` klicken und die Datei direkt herunterladen, dann als Anhang in den Chatbot ziehen oder den Inhalt einfuegen.
5. Danach die eigene Frage / das eigene Dokument hinterherschicken — der Chatbot uebernimmt die Rolle aus dem Skill.

So bekommt man die komplette Sammlung als ZIP:

- In der Plugin-Liste oben rechts neben jedem Plugin-Namen auf `[ZIP]` klicken. Das laedt eine ZIP-Datei mit **allen** Skills dieses Plugins (mitsamt Hilfsdateien, Pruefrastern und Vorlagen).
- Wer Claude Code nutzt, kann das ZIP direkt als Plugin installieren. Alle anderen koennen die enthaltenen `SKILL.md`-Dateien einzeln in jeden Chatbot kopieren.

**Wichtig:** Wenn irgendwo im Repo ein neuer Skill angelegt wird (also ein neuer Ordner `<plugin>/skills/<skill>/SKILL.md`), erscheint er beim naechsten Lauf von `scripts/generate-skills-md.py` automatisch in dieser Liste. Es kann hier also nichts fehlen.

"""


def plugin_overview_table(plugins: list[tuple[str, list[str]]]) -> str:
    lines = [
        "## Plugins (Schnellzugriff)",
        "",
        "Pro Plugin: Sprung in die Detailtabelle und ZIP-Download mit allen Skills.",
        "",
        "| Plugin | Skills | ZIP-Download |",
        "| --- | --- | --- |",
    ]
    for name, skills in plugins:
        anchor = name.lower()
        zip_url = f"{GH_RELEASE}/{name}.zip"
        lines.append(
            f"| [{name}](#{anchor}) | {len(skills)} | [`{name}.zip`]({zip_url}) |"
        )
    lines.append("")
    return "\n".join(lines)


def plugin_section(name: str, skills: list[str]) -> str:
    skills_dir = REPO_ROOT / name / "skills"
    plugin_zip = f"{GH_RELEASE}/{name}.zip"
    plugin_readme = f"{GH_BLOB}/{name}/README.md"
    lines = [
        f"## {name}",
        "",
        f"**{len(skills)} Skills** · [Plugin-README]({plugin_readme}) · [Alle Skills als ZIP herunterladen]({plugin_zip})",
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


def main() -> int:
    plugins = collect_plugins()
    total_skills = sum(len(skills) for _, skills in plugins)
    total_plugins = len(plugins)
    version = (
        "v" + json.loads((REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text())["version"]
    )

    parts = [
        header(total_skills, total_plugins, version),
        plugin_overview_table(plugins),
    ]
    for name, skills in plugins:
        parts.append(plugin_section(name, skills))

    text = "\n".join(parts).rstrip() + "\n"
    out = REPO_ROOT / "SKILLS.md"
    old = out.read_text(encoding="utf-8") if out.is_file() else ""
    out.write_text(text, encoding="utf-8")
    print(
        f"SKILLS.md geschrieben: {total_skills} Skills in {total_plugins} Plugins, "
        f"Stand {version}, {len(text)} Zeichen ({'identisch' if text == old else 'GEAENDERT'})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
