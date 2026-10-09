#!/usr/bin/env python3
"""Fuegt in die Top-Level README.md ganz oben (direkt nach dem H1) eine
prominente 'Sofort-Downloads'-Sektion ein.

Inhalt der Sektion:
- Plugin-ZIPs (installierbar in Claude Code) je Plugin und als Sammel-ZIP
- Skills als Markdown (echte Datei-Downloads) je Plugin und als Sammel-ZIP
- Arbeitsprompts (Vollworkflow) und Kurzprompts je Marktseite als einzelne .md-Datei zum Direkt-Download
- Unified Mini Prompts (Sammel-ZIP und einzeln)
- Testakten je Akte (ZIP) und als Sammel-ZIP
- marketplace.json für Claude-Code-Plugin-Konfiguration

Idempotent über HTML-Marker. Position: ZWISCHEN H1 und dem restlichen Inhalt.

Aufruf:
    python3 scripts/inject-top-readme-downloads.py

Daten kommen aus:
- .claude-plugin/marketplace.json  -> Plugin-Liste
- testakten/<slug>/                -> Akten-Liste (ohne SKIP_TESTAKTEN_DIRS)
- testakten/<slug>/README.md       -> Akten-Titel (H1)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from public_release import RAW_BASE, RELEASE_BASE, RELEASE_TAG, REPOSITORY, plugin_download
from testakte_notices import with_case_warnings

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN_DIR = REPO_ROOT / "testakten"
README_PATH = REPO_ROOT / "README.md"
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"

SKIP_TESTAKTEN_DIRS = {
    "formatvorlagen-paradebeispiele",
    "megaprompts",
}

MARKER_BEGIN = "<!-- BEGIN top-readme-downloads-section (autogen) -->"
MARKER_END = "<!-- END top-readme-downloads-section (autogen) -->"


# Root-Promptdateien (Dateiname, Anzeigename, Beschreibung)
ROOT_PROMPTS = [
    ("vergaberecht-arbeitsprompt-vergabestelle.md",
     "Vergaberecht-Arbeitsprompt - Vergabestelle",
     "Vollworkflow für öffentliche Auftraggeber"),
    ("vergaberecht-arbeitsprompt-bieter.md",
     "Vergaberecht-Arbeitsprompt - Bieter",
     "Vollworkflow für Bieter, Bewerber, Kanzleien"),
    ("vergaberecht-arbeitsprompt-konkurrenten.md",
     "Vergaberecht-Arbeitsprompt - Konkurrenten",
     "Vollworkflow für Konkurrentenrechtsschutz, Nachprüfung, OLG"),
    ("vergaberecht-kurzprompt-vergabestelle.md",
     "Vergaberecht-Kurzprompt - Vergabestelle",
     "Kompakter Fachworkflow für die Vergabestelle ohne 7.500-Zeichenlimit"),
    ("vergaberecht-kurzprompt-bieter.md",
     "Vergaberecht-Kurzprompt - Bieter",
     "Kompakter Fachworkflow für Bieter und Bewerber ohne 7.500-Zeichenlimit"),
    ("vergaberecht-kurzprompt-konkurrenten.md",
     "Vergaberecht-Kurzprompt - Konkurrenten",
     "Kompakter Fachworkflow für Konkurrentenrechtsschutz ohne 7.500-Zeichenlimit"),
]

PLUGIN_PROFILES = {
    "vergabestelle-behoerden": {
        "rolle": "Vergabestelle",
        "zweck": "Verfahren planen, Bestangebot gestalten, werten, dokumentieren und verteidigen",
        "suffix": "vergabestelle",
    },
    "bieter-unternehmen": {
        "rolle": "Bieter",
        "zweck": "Unterlagen prüfen, Angebot bauen, Qualitätsvorsprung belegen und Rechtsschutz führen",
        "suffix": "bieter",
    },
    "konkurrenten-rechtsschutz": {
        "rolle": "Konkurrent",
        "zweck": "Billigzuschlag, Unterlagen, Wertung, Eignung und De-facto-Lagen angreifen",
        "suffix": "konkurrenten",
    },
}

H1_RE = re.compile(r"^# .+$", re.MULTILINE)


def slurp_h1(path: Path) -> str:
    """Erste H1-Zeile aus einer Markdown-Datei holen."""
    if not path.is_file():
        return path.parent.name
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.parent.name


def list_plugins() -> list[dict]:
    """Plugin-Liste aus marketplace.json."""
    manifest = json.loads(MARKETPLACE_PATH.read_text(encoding="utf-8"))
    return manifest.get("plugins", [])


def list_testakten() -> list[tuple[str, str]]:
    """Liste (slug, h1-titel) sortiert nach slug."""
    if not TESTAKTEN_DIR.exists():
        return []
    result = []
    for sub in sorted(TESTAKTEN_DIR.iterdir()):
        if not sub.is_dir() or sub.name in SKIP_TESTAKTEN_DIRS:
            continue
        title = slurp_h1(sub / "README.md")
        result.append((sub.name, title))
    return result


def build_section() -> str:
    plugins = list_plugins()
    testakten = list_testakten()

    lines = []
    lines.append(MARKER_BEGIN)
    lines.append("")
    lines.append("## Sofort-Downloads")
    lines.append("")
    lines.append(
        "Die Links in der Spalte `Herunterladen` sind stabile Release-Downloads und "
        "gehören zum angegebenen Komponentenstand. Links in der Spalte `Ansehen` öffnen "
        "dagegen die jeweilige Datei oder Übersicht im Browser."
    )
    lines.append("")

    lines.append("### Alles mit einem Klick")
    lines.append("")
    lines.append("| Paket | Inhalt | Herunterladen |")
    lines.append("| --- | --- | --- |")
    lines.append(
        f"| Vollständiges Quellarchiv (nicht installierbar) | Komponentenquellen unter `vergaberecht-werkstatt/`, einschließlich Prompts, Testakten, Audits, Skripten und Lizenzen; README.txt mit Warnhinweis | "
        f"[`alles-komplettpaket.zip`]({RELEASE_BASE}/alles-komplettpaket.zip) |"
    )
    lines.append(
        "| Quellcode | Vollständiger Stand des Branches `main` | "
        "[`main.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/archive/refs/heads/main.zip) |"
    )
    lines.append(
        f"| Prüfsummen | SHA-256-Prüfsummen aller Release-Dateien | "
        f"[`checksums-sha256.txt`]({RELEASE_BASE}/checksums-sha256.txt) |"
    )
    lines.append(
        "| Release-Seite | Versionshinweise, Einzeldateien und Quellcode-Snapshots | "
        f"[Komponenten-Release](https://github.com/{REPOSITORY}/releases/tag/{RELEASE_TAG}) |"
    )
    lines.append("")

    lines.append("### Welche Datei brauche ich?")
    lines.append("")
    lines.append("| Lage | Einstieg | Link |")
    lines.append("| --- | --- | --- |")
    lines.append("| Ich suche eine bestimmte Repo-Datei | Vollständigen Dateikatalog oder GitHub-Dateibaum öffnen | [Dateikatalog](#dateikatalog) |")
    lines.append("| Ich arbeite in Claude Desktop oder Cowork | Rollenpassendes Plugin-ZIP in `Customize`, `Plugins`, `+` hochladen | [Plugin-ZIPs](#plugins-installation) |")
    lines.append("| Ich arbeite in Claude Code | Repo als Marketplace hinzufügen und genau ein Rollenplugin installieren | [Installationsbefehle](#plugins-installation) |")
    lines.append("| Ich arbeite ohne Plugin in einem normalen Chatbot | Arbeitsprompt als empfohlene Vollfassung anhängen | [Arbeitsprompts](#arbeits--und-kurzprompts-je-marktseite-einzelne-markdown-dateien) |")
    lines.append("| Mein Chat hat wenig Kontextplatz | Rollenpassenden Unified Mini Prompt anhängen | [Mini-Prompts](unified-mini-prompts/README.md) |")
    lines.append("| Ich will nur einzelne Spezialfähigkeiten nutzen | Skills-Markdown-ZIP nehmen oder einzelne `SKILL.md` aus dem Index öffnen | [SKILLS.md](SKILLS.md) |")
    lines.append("| Ich will realistische Unterlagen testen | Testakte als ZIP laden oder Gesamt-PDF lesen | [Testakten](testakten/README.md) |")
    lines.append("| Ich prüfe Release- oder Marketplace-Fähigkeit | Validatoren und Smoke-Tests ausführen | [tests/smoke-tests.md](tests/smoke-tests.md) |")
    lines.append("")

    # ---------- Plugins ----------
    lines.append('<a id="plugins-installation"></a>')
    lines.append("")
    lines.append("### Plugins für Claude Code, Desktop und Cowork")
    lines.append("")
    lines.append(
        "In Claude Code zuerst einmal `/plugin marketplace add "
        "Klotzkette/claude-fuer-deutsches-recht` ausführen, danach `/plugin install "
        "[plugin-name]@klotzkette-german-legal-skills` und `/reload-plugins`. In Claude "
        "Desktop oder Cowork das Plugin-ZIP über `Customize`, `Plugins`, `+` "
        "hochladen. Danach weder einen Arbeitsprompt zusätzlich laden noch einen "
        "Skill auswählen: Fallunterlagen anhängen und den Startsatz oben senden. "
        "[Offizielle Installationshinweise](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)."
    )
    lines.append("")
    lines.append("| Plugin | Rolle | Zweck | Ansehen | Plugin-ZIP | Skills-ZIP | Mini-Prompt |")
    lines.append("| --- | --- | --- | --- | --- | --- | --- |")
    for p in plugins:
        name = p["name"]
        profile = PLUGIN_PROFILES.get(name, {})
        lines.append(
            f"| {name} "
            f"| {profile.get('rolle', 'Plugin')} "
            f"| {profile.get('zweck', 'Vergaberechtlicher Arbeitsworkflow')} "
            f"| [README]({name}/README.md) "
            f"| [`{name}.zip`]({plugin_download(name)}) "
            f"| [`{name}-skills-markdown.zip`]({RELEASE_BASE}/{name}-skills-markdown.zip) "
            f"| [`{name}-unified-mini-prompt.md`]({RELEASE_BASE}/{name}-unified-mini-prompt.md) |"
        )
    lines.append(
        f"| Alle Plugins zusammen "
        f"| alle "
        f"| Komplettpaket der installierbaren Arbeitsumgebung "
        f"| [`SKILLS.md`](SKILLS.md) "
        f"| [`alle-plugins-megazip.zip`]({RELEASE_BASE}/alle-plugins-megazip.zip) "
        f"| [`alle-skills-markdown.zip`]({RELEASE_BASE}/alle-skills-markdown.zip) "
        f"| [Einzelne Markdown-Dateien](unified-mini-prompts/README.md) |"
    )
    lines.append("")

    # ---------- Arbeits- und Kurzprompts ----------
    lines.append("### Arbeits- und Kurzprompts je Marktseite (einzelne Markdown-Dateien)")
    lines.append("")
    lines.append(
        "Jeder Prompt ist eine einzelne `.md`-Datei zum direkten Datei-Download. "
        "In jedem Chatbot (ChatGPT, Mistral, Gemini, DeepSeek, Le Chat, Perplexity, "
        "Claude) als Anhang nutzbar oder per Copy & Paste."
    )
    lines.append(
        "Der Kurzprompt ist ein ausführlicher Fachworkflow ohne starres Zeichenlimit. "
        "Nur der Unified Mini Prompt ist auf höchstens 7.500 Zeichen begrenzt."
    )
    lines.append(
        "Diese Prompts sind eigenständige Alternativen für Chats ohne Plugin; bei "
        "installiertem Plugin werden sie nicht zusätzlich benötigt."
    )
    lines.append("")
    lines.append("| Prompt | Inhalt | Direkt-Download |")
    lines.append("| --- | --- | --- |")
    for fname, label, beschreibung in ROOT_PROMPTS:
        lines.append(
            f"| {label} | {beschreibung} | [`{fname}`]({RELEASE_BASE}/{fname}) |"
        )
    for p in plugins:
        name = p["name"]
        lines.append(
            f"| Unified Mini Prompt — {name} "
            f"| Verdichteter Workflow bis 7.500 Zeichen "
            f"| [`{name}-unified-mini-prompt.md`]({RELEASE_BASE}/{name}-unified-mini-prompt.md) |"
        )
    lines.append("")

    # ---------- Testakten ----------
    lines.append("### Testakten (anonymisierte Demonstrations-Vergabeakten)")
    lines.append("")
    lines.append("| Akte | Aktenübersicht | PDF ansehen | PDF herunterladen | Akten-ZIP | Einzel-PDF-ZIP |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for slug, title in testakten:
        pdf_rel = f"testakten/{slug}/gesamt-pdf/{slug}_gesamt.pdf"
        pdf_raw = f"{RAW_BASE}/{pdf_rel}"
        lines.append(
            f"| {title} (`{slug}`) "
            f"| [`README`](testakten/{slug}/README.md) "
            f"| [Gesamt-PDF]({pdf_rel}) "
            f"| [`{slug}_gesamt.pdf`]({RELEASE_BASE}/{slug}_gesamt.pdf) "
            f"| [`testakte-{slug}.zip`]({RELEASE_BASE}/testakte-{slug}.zip) "
            f"| [`testakte-{slug}-einzelpdfs.zip`]({RELEASE_BASE}/testakte-{slug}-einzelpdfs.zip) |"
        )
    lines.append(
        f"| Alle Testakten zusammen "
        f"| [`testakten/README.md`](testakten/README.md) "
        f"| — "
        f"| — "
        f"| [`testakten-vergaberecht-werkstatt.zip`]({RELEASE_BASE}/testakten-vergaberecht-werkstatt.zip) | - |"
    )
    lines.append("")

    # ---------- Sonstige ----------
    lines.append("### Konfiguration und Einzel-Skills")
    lines.append("")
    lines.append(
        f"- Marketplace-Manifest für Claude Code: "
        f"[`marketplace.json`]({RELEASE_BASE}/marketplace.json)"
    )
    lines.append(
        f"- Pro Skill ein eigener Download: "
        f"siehe [`SKILLS.md`](SKILLS.md) (Gesamtübersicht) oder die "
        f"[Plugin-Detailseiten](skills-index/README.md). "
        f"Jede `SKILL.md` ist als `[Raw .md]`-Link verfügbar und einzeln "
        f"abrufbar."
    )
    lines.append(
        f"- Vollständige Asset-Prüfliste: "
        f"[`checksums-sha256.txt`]({RELEASE_BASE}/checksums-sha256.txt)."
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(MARKER_END)
    return with_case_warnings("\n".join(lines))


def upsert_section(readme_text: str, section: str) -> str:
    """Bestehende Sektion ersetzen, sonst direkt nach dem H1 einfuegen."""
    if MARKER_BEGIN in readme_text and MARKER_END in readme_text:
        pattern = re.compile(
            re.escape(MARKER_BEGIN) + r".*?" + re.escape(MARKER_END),
            re.DOTALL,
        )
        return pattern.sub(section, readme_text)

    # Wenn die manuelle Einleitung existiert, Sektion direkt dahinter einsetzen.
    intro_end = "<!-- END top-readme-intro (manual) -->"
    idx = readme_text.find(intro_end)
    if idx != -1:
        end = idx + len(intro_end)
        return readme_text[:end] + "\n\n" + section + "\n" + readme_text[end:]

    match = H1_RE.search(readme_text)
    if not match:
        # Kein H1 — einfach an den Anfang setzen
        return section + "\n\n" + readme_text

    end = match.end()
    return readme_text[:end] + "\n\n" + section + "\n" + readme_text[end:]


def main() -> int:
    if not README_PATH.is_file():
        print(f"README.md nicht gefunden unter {README_PATH}", file=sys.stderr)
        return 1
    if not MARKETPLACE_PATH.is_file():
        print(f"marketplace.json nicht gefunden unter {MARKETPLACE_PATH}", file=sys.stderr)
        return 1

    readme_text = README_PATH.read_text(encoding="utf-8")
    section = build_section()
    new_text = upsert_section(readme_text, section)

    if new_text == readme_text:
        print("README.md unveraendert (Sektion bereits aktuell).")
        return 0

    README_PATH.write_text(with_case_warnings(new_text), encoding="utf-8")
    print(f"README.md aktualisiert: Sofort-Download-Sektion gesetzt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
