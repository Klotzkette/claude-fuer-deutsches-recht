#!/usr/bin/env python3
"""Generiert die globale SKILLS.md (Skill-Gesamtübersicht) aus dem Repo.

Wird bei jeder Release-Vorbereitung gelaufen. Garantiert, dass jeder neue
Skill, der irgendwo unter <plugin>/skills/<skill>/SKILL.md angelegt wird,
automatisch in der SKILLS.md auftaucht — mit:

- Direkter Dateidownload des unveränderten SKILL.md-Inhalts über die
  statische Downloadseite des Repositorys.
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
from urllib.parse import quote

from readme_display import display_prose

REPO_ROOT = Path(__file__).resolve().parent.parent
GH_OWNER = "Klotzkette"
GH_REPO = "claude-fuer-deutsches-recht"
GH_RELEASE = f"https://github.com/{GH_OWNER}/{GH_REPO}/releases/latest/download"
DOWNLOAD_BASE = f"https://{GH_OWNER.lower()}.github.io/{GH_REPO}/download.html?path="
SKILLS_INDEX_DIR = REPO_ROOT / "skills-index"


def markdown_download_url(repo_path: str) -> str:
    return DOWNLOAD_BASE + quote(repo_path, safe="/")


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
    desc = ""
    for line in fm.splitlines():
        if line.startswith("description:"):
            desc = line.split(":", 1)[1].strip()
            break
    if not desc:
        return ""
    if desc.startswith('"') and desc.endswith('"'):
        desc = desc[1:-1]
    desc = display_prose(clean_description(desc.replace("\n", " ").strip()))
    desc = desc.replace("|", "\\|").strip()
    if len(desc) > 280:
        desc = desc[:277].rstrip() + "..."
    return desc


def natural_key(text: str) -> list[object]:
    normalized = text.lower()
    if re.match(r"^lph\d", normalized):
        normalized = f"lphz-{normalized}"
    normalized = re.sub(r"(?<=[a-z])(?=\d)", "-", normalized)
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", normalized)]


def collect_plugins() -> list[tuple[str, list[str]]]:
    """Liest marketplace.json und scannt jeden Plugin-Ordner alphabetisch."""
    market = json.loads((REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text())
    out: list[tuple[str, list[str]]] = []
    for plugin in market["plugins"]:
        name = plugin["name"]
        source = plugin.get("source", f"./{name}")
        rel = source[2:] if source.startswith("./") else source
        skills_dir = REPO_ROOT / rel / "skills"
        if not skills_dir.is_dir():
            continue
        skills = sorted(
            (
                d.name
                for d in skills_dir.iterdir()
                if d.is_dir() and (d / "SKILL.md").is_file()
            ),
            key=natural_key,
        )
        if skills:
            out.append((name, skills))
    return sorted(out, key=lambda item: natural_key(item[0]))


def group_label(name: str) -> str:
    first = name[:1].upper()
    return first if first.isalpha() else "0-9"


def grouped_plugins(
    plugins: list[tuple[str, list[str]]],
) -> list[tuple[str, list[tuple[str, list[str]]]]]:
    groups: dict[str, list[tuple[str, list[str]]]] = {}
    for plugin in plugins:
        groups.setdefault(group_label(plugin[0]), []).append(plugin)
    labels = sorted(groups, key=lambda value: (value != "0-9", value))
    return [(label, groups[label]) for label in labels]


def alphabetical_navigation(plugins: list[tuple[str, list[str]]]) -> str:
    labels = [label for label, _ in grouped_plugins(plugins)]
    return " · ".join(f"[{label}](#{label.lower()})" for label in labels)


def header(total_skills: int, total_plugins: int, version: str) -> str:
    megazip = f"{GH_RELEASE}/alle-plugins-megazip.zip"
    komplett = f"{GH_RELEASE}/alles-komplettpaket.zip"
    alle_md = f"{GH_RELEASE}/alle-skills-markdown.zip"
    return f"""# Skill-Gesamtübersicht

Automatisch generierte Gesamtübersicht aller **{total_skills} Skills** in **{total_plugins} Plugins**.

Stand: `{version}`.

[Repository-Start](README.md) · [Download-Index](ASSET_INDEX.md) · [Werkstatt und Schnellstart](docs/werkstatt-und-schnellstart-coverage.md) · [Testakten](testakten/README.md) · [Plugin-Katalog](README.md#was-ist-drin) · [Detailseiten](skills-index/)

## Alle Skills auf einmal herunterladen

| Paket | Inhalt | Download |
| --- | --- | --- |
| **Alle Skills als Markdown** | `SKILL.md`-Dateien, zugehörige Markdown-Referenzen und Plugin-READMEs aller {total_plugins} Plugins; Werkstatt und Schnellstart bleiben einzelne Markdown-Direktdownloads | [`alle-skills-markdown.zip`]({alle_md}) |
| **Alle Plugins (installierbar)** | Alle {total_plugins} Plugin-ZIPs in einem Archiv für kompatible Plugin-Oberflächen | [`alle-plugins-megazip.zip`]({megazip}) |
| **Komplettpaket (alles)** | Plugins + Skill-Markdowns + Testakten + Übersichten | [`alles-komplettpaket.zip`]({komplett}) |

Das Markdown-Paket reicht, wenn man die vollständigen Skills in einem beliebigen Chat-System nutzen will. Werkstatt- und Schnellstart-Prompts liegen pro Plugin direkt als Markdown-Datei zum Download (oben in jeder Plugin-Detailseite und in jeder Plugin-README). Links mit **MD herunterladen** führen über die statische Downloadseite und speichern die Datei, statt nur die GitHub-Vorschau zu öffnen. Das Plugin-Paket ist für kompatible Plugin-Oberflächen. Das Komplettpaket enthält zusätzlich Testakten und alle Repo-Übersichten.

Wer nur **ein bestimmtes Plugin** will: weiter unten in der Plugin-Tabelle pro Plugin eigene Links (Werkstatt-Markdown, Schnellstart-Markdown, Plugin-ZIP).

## Worum es hier geht: alles nur große Prompts

Diese Skills sind am Ende **nichts weiter als große, sehr sorgfältig formulierte System-Prompts in Markdown**. Sie wurden für ein Plugin-System geschrieben, **funktionieren aber in jedem anderen Chat-System genauso**.

So benutzt man einen Skill außerhalb eines Plugin-Setups:

1. Unten in der Plugin-Tabelle auf das gewünschte Plugin klicken — die Detailseite mit allen Skills öffnet sich.
2. Auf der Detailseite oben auf **Werkstatt** oder **Schnellstart** klicken — die `.md`-Datei wird als Datei heruntergeladen.
3. **Entweder** den kompletten Text mit `Strg+A` / `Cmd+A` kopieren und in das eigene Chat-System einfügen.
4. **Oder** die `.md`-Datei als Anhang in den Chatbot ziehen.
5. Danach die eigene Frage / das eigene Dokument hinterherschicken — der Chatbot übernimmt die Rolle aus dem Skill.

So bekommt man die komplette Sammlung als installierbares ZIP:

- In der Plugin-Tabelle unten in der Spalte **Plugin-ZIP** auf den Download-Link klicken. Das lädt eine ZIP-Datei mit **allen** Skills dieses Plugins inkl. Hilfsdateien, Prüfrastern und Vorlagen — direkt in kompatiblen Plugin-Oberflächen installierbar.
- Wer kein Plugin-Setup nutzt, nimmt **Werkstatt** oder **Schnellstart** als Markdown-Direkt-Download. Beide sind je eine `.md`-Datei, die in beliebige Chatbots gezogen oder kopiert werden kann.
- Wer die volle Skilltiefe als Markdown will, nimmt zusätzlich das Sammelpaket `alle-skills-markdown.zip`; es enthält auch die von Skills bei Bedarf geladenen Markdown-Referenzen.

**Wichtig:** Wenn irgendwo im Repo ein neuer Skill angelegt wird (also ein neuer Ordner `<plugin>/skills/<skill>/SKILL.md`), erscheint er beim nächsten Lauf von `scripts/generate-skills-md.py` automatisch -- sowohl in dieser Liste als auch auf der jeweiligen Plugin-Detailseite. Es kann also nichts fehlen.

Die Detailseiten liegen unter [`skills-index/`](skills-index/) -- eine eigene `.md`-Datei pro Plugin. So bleibt diese Hauptseite klein und lädt schnell, statt mit {total_skills} Tabellenzeilen den Browser-Renderer von GitHub zu überfordern.

English: Plugin and index links open navigation pages. Links labelled **Download MD** download the unchanged skill, workshop or quick-start Markdown file instead of opening a source preview.

"""


def plugin_overview_table(plugins: list[tuple[str, list[str]]]) -> str:
    lines = [
        "## Alle Plugins",
        "",
        "Die Plugins sind alphabetisch sortiert. Der Name öffnet die Detailseite mit allen Skills, Beschreibungen und Einzel-Downloads. **Werkstatt** und **Schnellstart** laden die Ein-Datei-Prompts direkt als Markdown. **Plugin-ZIP** lädt die installierbare Plugin-Sammlung.",
        "",
        alphabetical_navigation(plugins),
        "",
    ]
    for label, items in grouped_plugins(plugins):
        lines.extend(
            [
                f"### {label}",
                "",
                "| Plugin | Skills | Detailseite | Werkstatt (Markdown) | Schnellstart (Markdown) | Plugin-ZIP |",
                "| --- | ---: | --- | --- | --- | --- |",
            ]
        )
        for name, skills in items:
            source_rel = _source_rel_for(name)
            zip_url = f"{GH_RELEASE}/{name}.zip"
            werkstatt_url = markdown_download_url(f"{source_rel}/{name}-werkstatt.md")
            schnellstart_url = markdown_download_url(f"{source_rel}/{name}-schnellstart.md")
            detail = f"skills-index/{name}.md"
            lines.append(
                f"| **{name}** | {len(skills)} | [Skills ansehen]({detail}) | [Werkstatt-MD herunterladen]({werkstatt_url}) | [Schnellstart-MD herunterladen]({schnellstart_url}) | [Plugin]({zip_url}) |"
            )
        lines.append("")
    return "\n".join(lines)


def _source_rel_for(name: str) -> str:
    market = json.loads((REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text())
    for p in market["plugins"]:
        if p["name"] == name:
            src = p.get("source", f"./{name}")
            return src[2:] if src.startswith("./") else src
    return name


def plugin_detail_page(name: str, skills: list[str], version: str) -> str:
    _source_rel = _source_rel_for(name)
    skills_dir = REPO_ROOT / _source_rel / "skills"
    plugin_zip = f"{GH_RELEASE}/{name}.zip"
    werkstatt_md = markdown_download_url(f"{_source_rel}/{name}-werkstatt.md")
    schnellstart_md = markdown_download_url(f"{_source_rel}/{name}-schnellstart.md")
    md_zip = f"{GH_RELEASE}/alle-skills-markdown.zip"
    plugin_readme = f"../{_source_rel}/README.md"
    lines = [
        f"# {name}",
        "",
        f"**{len(skills)} Skills** · Stand `{version}`",
        "",
        f"[Repository-Start](../README.md) · [Skill-Gesamtübersicht](../SKILLS.md) · [Plugin-README]({plugin_readme}) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)",
        "",
        "## Downloads",
        "",
        "| Paket | Format | Link |",
        "| --- | --- | --- |",
        f"| **Großer Prompt (Werkstatt)** | Markdown | [`{name}-werkstatt.md` herunterladen]({werkstatt_md}) |",
        f"| **Kleiner Prompt (Schnellstart)** | Markdown | [`{name}-schnellstart.md` herunterladen]({schnellstart_md}) |",
        f"| **Alle Skills als Markdown** | ZIP | [alle-skills-markdown.zip]({md_zip}) |",
        f"| **Plugin (installierbar)** | ZIP | [{name}.zip]({plugin_zip}) |",
        "",
        "## So benutzt man einen Skill",
        "",
        "Skills sind eng abgegrenzte Markdown-Arbeitsabläufe und funktionieren in jedem geeigneten Chat-System. Werkstatt und Schnellstart sind dagegen eigenständige Ein-Datei-Prompts und nicht Teil des Plugin-ZIPs.",
        "",
        "English: Skills are focused Markdown workflows. Workshop and quick-start files are standalone prompts and are not included in the plugin ZIP. Every skill link below downloads the unchanged Markdown content with a unique filename.",
        "",
        "- **Schnelltest mit einer Datei:** oben auf den Schnellstart-Markdown klicken, die `.md` als Anhang in den Chatbot ziehen.",
        "- **Volle Ein-Datei-Tiefe:** oben auf den Werkstatt-Markdown klicken, die `.md` als ausführlichen Arbeitsmodus verwenden.",
        "- **Volle Skill-Tiefe:** das Sammel-ZIP `alle-skills-markdown.zip` herunterladen und entpacken. Es enthält neben jeder `SKILL.md` auch deren Markdown-Referenzen; beim manuellen Einsatz die benötigten Dateien gemeinsam bereitstellen.",
        "- **Einzelnen Skill laden:** in der Tabelle auf den Skillnamen oder auf `MD herunterladen` klicken. Beide Wege speichern dieselbe Markdown-Datei.",
        "",
        "## Skills in diesem Plugin",
        "",
        "| Skill | Beschreibung | Markdown-Datei |",
        "| --- | --- | --- |",
    ]
    for s in skills:
        skill_md = skills_dir / s / "SKILL.md"
        desc = read_description(skill_md)
        rel_md = f"{_source_rel}/skills/{s}/SKILL.md"
        download_url = markdown_download_url(rel_md)
        lines.append(
            f"| [`{s}`]({download_url}) | {desc} | [MD herunterladen / Download MD]({download_url}) |"
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
        f"Die Aufteilung verhindert, dass eine einzige Seite alle {sum(len(skills) for _, skills in plugins)} Skillzeilen rendern muss. Die Detailseiten bleiben dadurch schnell und einzeln verlinkbar.",
        "",
        "English: Each plugin has one lightweight detail page containing its complete skill list, descriptions and direct Markdown downloads. Open a plugin page to choose a skill; links labelled `Download MD` save the file instead of opening a source preview.",
        "",
        "[Repository-Start](../README.md) · [Skill-Gesamtübersicht](../SKILLS.md) · [Download-Index](../ASSET_INDEX.md) · [Werkstatt und Schnellstart](../docs/werkstatt-und-schnellstart-coverage.md) · [Testakten](../testakten/README.md)",
        "",
        "## Alle Detailseiten",
        "",
        "Alphabetisch sortiert: " + alphabetical_navigation(plugins),
        "",
    ]
    for label, items in grouped_plugins(plugins):
        lines.extend([f"### {label}", ""])
        for name, skills in items:
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
