#!/usr/bin/env python3
"""Generiert die globale SKILLS.md (Skill-Gesamtübersicht) aus dem Repo.

Wird bei jeder Release-Vorbereitung gelaufen. Garantiert, dass jeder neue
Skill, der irgendwo unter <plugin>/skills/<skill>/SKILL.md angelegt wird,
automatisch in der SKILLS.md auftaucht — mit:

- Direkt-Download des SKILL.md als rohe Markdown-Datei (im Browser per
  Rechtsklick "Ziel speichern unter" oder "?raw=1" lädt sofort herunter).
- Pro Plugin: ZIP-Download-Link auf das Release-Asset
  https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/vergaberecht-werkstatt-v445.33.1/<plugin>.zip
- Oben prominenter Hinweis: Skills sind reine Markdown-Prompts und
  funktionieren per Copy-Paste in jedem Chatbot.

Idempotent: schreibt SKILLS.md neu. Liest Version aus marketplace.json.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from public_release import BLOB_BASE as GH_BLOB, RAW_BASE as GH_RAW, RELEASE_BASE as GH_RELEASE
from public_release import with_working_downloads
from testakte_notices import with_case_warnings

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_INDEX_DIR = REPO_ROOT / "skills-index"

PLUGIN_PROFILES = {
    "vergabestelle-behoerden": {
        "rolle": "Vergabestelle",
        "kurz": "Vergabe planen, Unterlagen bauen, Bestangebot werten, Rüge/VK/OLG verteidigen",
        "prompt": "vergaberecht-arbeitsprompt-vergabestelle.md",
        "kurzprompt": "vergaberecht-kurzprompt-vergabestelle.md",
    },
    "bieter-unternehmen": {
        "rolle": "Bieter",
        "kurz": "Unterlagen prüfen, Angebot liefern, Qualitätsvorsprung belegen, Rüge/VK/OLG führen",
        "prompt": "vergaberecht-arbeitsprompt-bieter.md",
        "kurzprompt": "vergaberecht-kurzprompt-bieter.md",
    },
    "konkurrenten-rechtsschutz": {
        "rolle": "Konkurrent",
        "kurz": "Billigzuschlag, Produktvorgabe, Wertung, Eignung und De-facto-Lage angreifen",
        "prompt": "vergaberecht-arbeitsprompt-konkurrenten.md",
        "kurzprompt": "vergaberecht-kurzprompt-konkurrenten.md",
    },
}


def clean_description(desc: str) -> str:
    """Bereinigt Beschreibungen für die menschenlesbare Markdown-Ausgabe."""
    desc = re.sub(
        r"\s+[—-]\s*Arbeitskontext:\s*[^.]+,\s*Schwerpunkt\s+[^.]+\.?",
        "",
        desc,
    )
    desc = re.sub(r"\s+im Plugin\s+[^.:\"`|]+(?=[:.])", "", desc)
    desc = re.sub(r"\s+im Plugin\s+[^\"`|]+$", "", desc)
    # Frontmatter muss für den Marketplace "Paragraf" ausschreiben. In der
    # sichtbaren Dokumentation ist dagegen das juristisch übliche Zeichen klarer.
    desc = re.sub(r"\b(?:Paragrafen|Paragraphen)\s+(?=\d)", "§§ ", desc)
    desc = re.sub(r"\b(?:Paragraf|Paragraph)\s+(?=\d)", "§ ", desc)
    desc = re.sub(r"\b(?:Paragraf|Paragraph)-(?=\d)", "§-", desc)
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
    if len(desc) >= 2 and desc[0] == desc[-1] and desc[0] in {'"', "'"}:
        desc = desc[1:-1]
    desc = clean_description(desc.replace("\n", " ").strip())
    desc = desc.replace("|", "\\|").strip()
    return desc


def read_title(skill_md: Path) -> str:
    """Liest die erste H1 als sprechenden Arbeitsnamen des Skills."""
    for line in skill_md.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            title = re.sub(r"\s+", " ", title).replace("|", "\\|")
            return title
    return skill_md.parent.name


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
    alle_md = f"{GH_RELEASE}/alle-skills-markdown.zip"
    return f"""# Skill-Gesamtübersicht

[Repo-Start](README.md) | [Dateikatalog](README.md#dateikatalog) | [Sofort-Downloads](README.md#sofort-downloads) | [Vergabestelle](vergabestelle-behoerden/README.md) | [Bieter](bieter-unternehmen/README.md) | [Konkurrent](konkurrenten-rechtsschutz/README.md) | [Plugin-Detailseiten](skills-index/README.md) | [Testakten](testakten/README.md) | [Rechtsprechung](references/leitentscheidungen-anker.md)

Automatisch generierte Gesamtübersicht aller {total_skills} Skills in {total_plugins} Plugins.

Stand: `{version}`.

## Alle Skills auf einmal herunterladen

| Paket | Inhalt | Download |
| --- | --- | --- |
| Alle Skills als Markdown | Reine `SKILL.md`-Dateien aller {total_plugins} Plugins — als echte Datei-Downloads | [`alle-skills-markdown.zip`]({alle_md}) |
| Unified Mini Prompts | Pro Marktrolle ein kompakter Ein-Datei-Prompt | [Einzelne Markdown-Dateien](unified-mini-prompts/README.md) |
| Alle Plugins (installierbar) | Alle {total_plugins} Plugin-ZIPs in einem Archiv (für Claude Code) | [`alle-plugins-megazip.zip`]({megazip}) |
| Vollständiges Quellarchiv (nicht installierbar) | Alle Komponentenquellen unter `vergaberecht-werkstatt/` und README.txt mit Warnhinweis | [`alles-komplettpaket.zip`]({komplett}) |

Das Markdown-Paket reicht, wenn man die vollständigen Skills in ChatGPT, Gemini, Mistral, Le Chat oder Perplexity nutzen will. Die Unified Mini Prompts sind die Sparvariante: ein kurzer Workflow pro Plugin, wenn man nur eine einzige Markdown-Datei verwenden möchte. Das Plugin-Paket ist für Claude-Code-/Cowork-Nutzer. Das Komplettpaket enthält zusätzlich Testakten und alle Repo-Übersichten.

Wer nur ein bestimmtes Plugin will: weiter unten in der Plugin-Tabelle pro Plugin eigene Download-Links (Plugin-ZIP, Markdown-ZIP und Unified Mini Prompt).

## Welche Datei nehme ich?

| Bedarf | Beste Wahl | Warum |
| --- | --- | --- |
| Plugin in Claude Code nutzen | Plugin-ZIP der Marktrolle | Enthält Skills, Hilfsdateien, Vorlagen und Referenzen als installierbares Paket. |
| Ohne Plugin schnell starten | Unified Mini Prompt | Eine Markdown-Datei pro Marktrolle, autark und kurz genug für normale Chatfenster. |
| Ohne Plugin tief arbeiten | Markdown-ZIP der Marktrolle | Enthält alle `SKILL.md`-Dateien dieser Marktrolle. |
| Einzelnen Spezialfall lösen | Detailseite des Plugins öffnen und passende `SKILL.md` wählen | Jede Zeile enthält Beschreibung, Browser-Ansicht und Raw-Link. |
| Alles lokal prüfen oder weiterbauen | Komplettpaket oder Repo-Checkout | Enthält Plugins, Testakten, Übersichten, Validatoren und Release-Struktur. |

## Ohne Skillauswahl starten

Wenn ein Aktenordner, ZIP, Portalexport, DMS-Export oder Projektordner vorliegt, zuerst die Marktrolle wählen und den Ordner mit einem Satz wie `Hier ist der neue Fall, bitte vorbereiten` übergeben. Das passende Plugin startet über Orchestrator und Kaltstart selbst mit Fallkarte, Fristenampel, Dokumentenmatrix, Belegmatrix, Output-Weiche, Lückenliste und erstem Arbeitsauftrag. Die technischen Skill-Slugs bleiben stabile Links; die sprechenden Arbeitsnamen stehen in den Detailseiten in einer eigenen Spalte und stammen direkt aus der H1 der jeweiligen `SKILL.md`.

## Worum es hier geht: alles nur große Prompts

Diese Skills sind am Ende nichts weiter als große, sehr sorgfältig formulierte System-Prompts in Markdown. Sie wurden für das Claude-Code-Plugin-System geschrieben, funktionieren aber in jedem anderen Chatbot genauso.

So benutzt man einen Skill außerhalb von Claude Code:

1. Unten in der Plugin-Tabelle auf das gewünschte Plugin klicken — die Detailseite mit allen Skills öffnet sich.
2. Auf der Detailseite oben auf Markdown-ZIP klicken — die `<plugin>-skills-markdown.zip` landet direkt im Download-Ordner. Entpacken, gewünschte `SKILL.md` öffnen.
3. Entweder den kompletten Text mit `Strg+A` / `Cmd+A` kopieren und in den Chat einfügen (ChatGPT, Mistral, Gemini, DeepSeek, Le Chat oder andere Chatbots).
4. Oder die einzelne `SKILL.md` als Anhang in den Chatbot ziehen.
5. Danach die eigene Frage / das eigene Dokument hinterherschicken — der Chatbot übernimmt die Rolle aus dem Skill.

Hinweis zu Browser-Links: `[Markdown]` zeigt die Datei im Browser an (zum Lesen oder Kopieren). `[Raw .md]` öffnet den Rohtext — GitHub liefert ihn als `text/plain` aus, manche Browser zeigen ihn deshalb als Text statt als Download. Wenn ein echter Datei-Download gewünscht ist, immer das Plugin-Markdown-ZIP nehmen.

So bekommt man die komplette Sammlung als installierbares ZIP:

- In der Plugin-Tabelle unten in der Spalte Plugin-ZIP auf den Download-Link klicken. Das lädt eine ZIP-Datei mit allen Skills dieses Plugins inkl. Hilfsdateien, Prüfrastern und Vorlagen — direkt in Claude Code installierbar.
- Wer kein Claude Code nutzt, nimmt stattdessen Markdown-ZIP — das enthält nur die `SKILL.md` als reine Markdown-Dateien zum Einlesen in beliebige Chatbots.
- Wer nur schnell eine einzige Datei ausprobieren will, nimmt Unified Mini Prompt. Das ist bewusst nicht die volle Skilltiefe, sondern der verdichtete Arbeitsmodus des jeweiligen Plugins.

Wichtig: Wenn irgendwo im Repo ein neuer Skill angelegt wird (also ein neuer Ordner `<plugin>/skills/<skill>/SKILL.md`), erscheint er beim nächsten Lauf von `scripts/generate-skills-md.py` automatisch -- sowohl in dieser Liste als auch auf der jeweiligen Plugin-Detailseite. Es kann also nichts fehlen.

Die Detailseiten liegen unter [`skills-index/`](skills-index/) -- eine eigene `.md`-Datei pro Plugin. So bleibt diese Hauptseite klein und lädt schnell, statt mit {total_skills} Tabellenzeilen den Browser-Renderer von GitHub zu überfordern.

"""


def plugin_overview_table(plugins: list[tuple[str, list[str]]]) -> str:
    lines = [
        "## Alle Plugins",
        "",
        "Pro Plugin: Klick auf die Detailseite öffnet alle Skills, Beschreibungen und Einzel-Downloads. Plugin-ZIP lädt die installierbare Claude-Code-/Cowork-Sammlung. Markdown-ZIP lädt die reinen `SKILL.md`-Dateien. Mini-Prompt ist eine einzelne Markdown-Datei bis 7.500 Zeichen für ChatGPT, Gemini, Mistral oder andere Chatbots.",
        "",
        "| Plugin | Rolle | Wofür | Skills | README | Detailseite | Plugin-ZIP | Markdown-ZIP | Mini-Prompt |",
        "| --- | --- | --- | ---: | --- | --- | --- | --- | --- |",
    ]
    for name, skills in plugins:
        profile = PLUGIN_PROFILES.get(name, {})
        zip_url = f"{GH_RELEASE}/{name}.zip"
        md_url = f"{GH_RELEASE}/{name}-skills-markdown.zip"
        mini_url = f"{GH_RELEASE}/{name}-unified-mini-prompt.md"
        detail = f"skills-index/{name}.md"
        readme = f"{name}/README.md"
        lines.append(
            f"| {name} | {profile.get('rolle', 'Plugin')} | {profile.get('kurz', 'Vergaberechtlicher Workflow')} | {len(skills)} | [README]({readme}) | [Skills ansehen]({detail}) | [Plugin]({zip_url}) | [Markdown]({md_url}) | [Mini]({mini_url}) |"
        )
    lines.append("")
    return "\n".join(lines)


def plugin_detail_page(name: str, skills: list[str], version: str) -> str:
    skills_dir = REPO_ROOT / name / "skills"
    plugin_zip = f"{GH_RELEASE}/{name}.zip"
    md_zip = f"{GH_RELEASE}/{name}-skills-markdown.zip"
    mini_prompt = f"{GH_RELEASE}/{name}-unified-mini-prompt.md"
    plugin_readme = f"{GH_BLOB}/{name}/README.md"
    profile = PLUGIN_PROFILES.get(name, {})
    root_prompt = profile.get("prompt")
    short_prompt = profile.get("kurzprompt")
    lines = [
        f"# {name}",
        "",
        "[Repo-Start](../README.md) | [Dateikatalog](../README.md#dateikatalog) | "
        "[Vergabestelle](../vergabestelle-behoerden/README.md) | "
        "[Bieter](../bieter-unternehmen/README.md) | "
        "[Konkurrent](../konkurrenten-rechtsschutz/README.md) | "
        "[Alle Skills](../SKILLS.md) | [Plugin-Index](./README.md) | "
        "[Testakten](../testakten/README.md) | "
        "[Rechtsprechung](../references/leitentscheidungen-anker.md)",
        "",
        f"{len(skills)} Skills · Stand `{version}` · Rolle: {profile.get('rolle', 'Plugin')}",
        "",
        "## Schnellnavigation",
        "",
        "| Bedarf | Link |",
        "| --- | --- |",
        f"| Installierbares Plugin | [{name}.zip]({plugin_zip}) |",
        f"| Alle Skills als Markdown | [{name}-skills-markdown.zip]({md_zip}) |",
        f"| Kompakter Ein-Datei-Start | [{name}-unified-mini-prompt.md]({mini_prompt}) |",
    ]
    if root_prompt:
        lines.append(f"| Vollworkflow-Arbeitsprompt | [{root_prompt}]({GH_RELEASE}/{root_prompt}) |")
    if short_prompt:
        lines.append(f"| Kurzprompt | [{short_prompt}]({GH_RELEASE}/{short_prompt}) |")
    lines.extend([
        f"| Plugin-README im Repo | [{name}/README.md]({plugin_readme}) |",
        "",
        "## Downloads",
        "",
        "| Paket | Inhalt | Link |",
        "| --- | --- | --- |",
        f"| Unified Mini Prompt | Eine einzelne Markdown-Datei bis 7.500 Zeichen: Sparversion des Plugin-Workflows für Chatbots ohne Plugin-Installation | [{name}-unified-mini-prompt.md]({mini_prompt}) |",
        f"| Markdown-ZIP | Alle `SKILL.md`-Dateien als reine Markdown — echter Datei-Download für ChatGPT, Gemini, Mistral, Le Chat usw. | [{name}-skills-markdown.zip]({md_zip}) |",
        f"| Plugin-ZIP | Installierbares Claude-Code-Plugin (Skills + Hilfsdateien + Prüfrastern + Vorlagen) | [{name}.zip]({plugin_zip}) |",
        "",
        "## So benutzt man einen Skill",
        "",
        "Skills sind reine Markdown-Prompts und funktionieren in jedem Chatbot (ChatGPT, Mistral, Gemini, DeepSeek, Le Chat oder andere Chatbots).",
        "",
        "- Ohne manuelle Skillwahl starten: Aktenordner, ZIP, Portalexport oder Projektordner anhängen und schreiben: `Hier ist der neue Fall, bitte vorbereiten`. Der Orchestrator bildet Fallkarte, Fristenampel, Dokumentenmatrix, Belegmatrix, Output-Weiche und ersten Arbeitsauftrag.",
        "- Schnelltest mit einer Datei: den Unified Mini Prompt oben herunterladen und als Markdown-Datei in den Chatbot ziehen.",
        "- Volle Markdown-Tiefe: das Markdown-ZIP oben herunterladen, entpacken, gewünschte `SKILL.md` als Anhang in den Chatbot ziehen oder kopieren.",
        "- Im Browser lesen: in der Tabelle unten `[Markdown]` klicken — die `SKILL.md` öffnet sich auf GitHub. Inhalt mit `Strg+A` / `Cmd+A` kopieren und einfügen.",
        "- `[Raw .md]` zeigt den Rohtext. Manche Browser zeigen das als Text statt als Download — für echte Downloads das Markdown-ZIP oben nehmen.",
        "",
        "## Skills in diesem Plugin",
        "",
        "| Technischer Skill | Arbeitsname | Beschreibung | Browser-Ansicht |",
        "| --- | --- | --- | --- |",
    ])
    for s in skills:
        skill_md = skills_dir / s / "SKILL.md"
        title = read_title(skill_md)
        desc = read_description(skill_md)
        rel_md = f"{name}/skills/{s}/SKILL.md"
        blob_url = f"{GH_BLOB}/{rel_md}"
        raw_url = f"{GH_RAW}/{rel_md}"
        lines.append(
            f"| [`{s}`]({blob_url}) | {title} | {desc} | [Markdown]({blob_url}) · [Raw .md]({raw_url}) |"
        )
    lines.append("")
    return "\n".join(lines)


def write_detail_index(plugins: list[tuple[str, list[str]]], version: str) -> str:
    """Schreibt skills-index/README.md mit Liste aller Detailseiten."""
    lines = [
        "# Skills-Index: Detailseiten pro Plugin",
        "",
        "[Repo-Start](../README.md) | [Dateikatalog](../README.md#dateikatalog) | "
        "[Alle Skills](../SKILLS.md) | [Downloads](../README.md#sofort-downloads) | "
        "[Vergabestelle](../vergabestelle-behoerden/README.md) | "
        "[Bieter](../bieter-unternehmen/README.md) | "
        "[Konkurrent](../konkurrenten-rechtsschutz/README.md) | "
        "[Testakten](../testakten/README.md) | "
        "[Rechtsprechung](../references/leitentscheidungen-anker.md)",
        "",
        f"Eine Detailseite pro Plugin mit allen Skills, Beschreibungen und Einzel-Downloads. Stand: `{version}`.",
        "",
        "Die Aufteilung hält die einzelnen Seiten trotz der umfangreichen Skill-Tabellen schnell und übersichtlich.",
        "",
        "## Alle Detailseiten",
        "",
        "| Plugin | Rolle | Skills | Detailseite | Plugin-README | Markdown-ZIP | Mini-Prompt |",
        "| --- | --- | ---: | --- | --- | --- | --- |",
    ]
    for name, skills in plugins:
        profile = PLUGIN_PROFILES.get(name, {})
        lines.append(
            f"| {name} | {profile.get('rolle', 'Plugin')} | {len(skills)} | "
            f"[Detailseite](./{name}.md) | [README](../{name}/README.md) | "
            f"[Markdown-ZIP]({GH_RELEASE}/{name}-skills-markdown.zip) | "
            f"[Mini-Prompt]({GH_RELEASE}/{name}-unified-mini-prompt.md) |"
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

    # 1) Schlanke Hauptseite SKILLS.md
    main_text = (
        header(total_skills, total_plugins, version)
        + plugin_overview_table(plugins)
    )
    main_text = main_text.rstrip() + "\n"
    out_main = REPO_ROOT / "SKILLS.md"
    out_main.write_text(with_case_warnings(main_text), encoding="utf-8")

    # 2) Detailseiten pro Plugin
    SKILLS_INDEX_DIR.mkdir(exist_ok=True)
    # Alte Detailseiten loeschen, falls Plugins entfernt wurden
    current_names = {name for name, _ in plugins} | {"README"}
    for old in SKILLS_INDEX_DIR.glob("*.md"):
        if old.stem not in current_names:
            old.unlink()
    for name, skills in plugins:
        page = plugin_detail_page(name, skills, version)
        output = SKILLS_INDEX_DIR / f"{name}.md"
        output.write_text(with_working_downloads(with_case_warnings(page.rstrip() + "\n"), output), encoding="utf-8")
    # Index der Detailseiten
    idx = write_detail_index(plugins, version)
    (SKILLS_INDEX_DIR / "README.md").write_text(with_case_warnings(idx.rstrip() + "\n"), encoding="utf-8")

    print(
        f"SKILLS.md: {len(main_text)} Zeichen ({total_plugins} Plugins). "
        f"skills-index/: {total_plugins} Detailseiten + Index. "
        f"Insgesamt {total_skills} Skills, Stand {version}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
