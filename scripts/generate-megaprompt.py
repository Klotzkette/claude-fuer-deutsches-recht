#!/usr/bin/env python3
"""generate-megaprompt.py - Konkateniert pro Plugin die Kern-Skills in ein
einzelnes Markdown ('Vollprüfung'), das man ohne Plugin-Installation als
ein-Schuss-Prompt verwenden kann.

Ausgabe: testakten/megaprompts/<plugin>.md

Auswahl-Heuristik:
- Plugins mit <= 20 Fachskills: ALLE Skills (Vollintegration)
- Plugins mit 21-60 Fachskills: top-15 Skills (Priorisierungsliste pro Plugin)
- Plugins mit 61-100 Fachskills: top-10 Skills
- Plugins mit > 100 Fachskills: top-8 Skills
- Der pluginweite Argumentationskern zählt für die Schwelle nicht als
  zusätzlicher Fachskill, wird aber in der Auswahl vorrangig berücksichtigt.
- Skill-Auswahl bei mittlerer Groesse:
    * einstieg-routing / kaltstart-triage / mandat-triage immer first
    * weiter nach Frontmatter-description-Laenge (laengere=substantieller)

Pro Vollprüfung:
- Header mit Disclaimer + Anleitung
- Inhaltsverzeichnis
- Konkatenierter Skill-Inhalt (Frontmatter entfernt)
- Footer: Hinweise
"""
from __future__ import annotations
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / 'testakten' / 'megaprompts'

# Plugins, die wir explizit AUSSCHLIESSEN:
# Aktuell keine Ausschluesse — alle vier ehemals ausgeschlossenen Plugins
# (corporate-kanzlei, urteilsbauer-relationsmacher, verlagsredaktion,
# zwangsverwaltung-zvg) werden jetzt mit dem Top-N-Tiering ueber
# entries_for_size() abgedeckt und bekommen Vollprüfungs.
EXCLUDE_PLUGINS: set[str] = set()

# Hinweis: Der Disclaimer- und Verwendungs-Block steht im jeweiligen
# Plugin-README, nicht im Vollprüfung-Markdown selbst — der Vollprüfung
# soll moeglichst rauschfrei in einen Chat-Agenten kopierbar sein.


def extract_frontmatter_and_body(text: str) -> tuple[str, str]:
    """Trennt YAML-Frontmatter vom Body."""
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            return parts[1].strip(), parts[2].strip()
    return '', text.strip()


def get_description(frontmatter: str) -> str:
    m = re.search(r'description:\s*"?([^"\n]+)"?', frontmatter)
    return m.group(1).strip().rstrip('"') if m else ''


def collect_skills(plugin_dir: Path) -> list[tuple[str, Path, str, str]]:
    """Liefert (slug, path, description, body) je Skill, sortiert nach Wichtigkeit."""
    out = []
    skills_dir = plugin_dir / 'skills'
    if not skills_dir.is_dir():
        return []
    priority_first = ['juristischer-argumentationskern',
                      'bea-versandmappe-endfertigung',
                      'versandmappe-endfertigen',
                      'anlagen-zu-schriftsaetzen',
                      'vergaberechtliche-pruefung-anwaltlich-vollpruefung',
                      'einstieg-routing', 'kaltstart-triage', 'mandat-triage',
                      'orientierung', 'mandat-intake-und-konfliktpruefung',
                      'erstgespraech-mandatsannahme', 'erstpruefung-und-mandatsziel']
    skills = []
    for sd in sorted(skills_dir.iterdir()):
        if not sd.is_dir():
            continue
        skill_md = sd / 'SKILL.md'
        if not skill_md.is_file():
            continue
        text = skill_md.read_text(encoding='utf-8', errors='ignore')
        fm, body = extract_frontmatter_and_body(text)
        desc = get_description(fm)
        skills.append((sd.name, skill_md, desc, body))

    # Sortierung: Prioritaeten zuerst, dann Description-Laenge (= Substanz-Proxy)
    def keyfn(item):
        slug = item[0]
        prio_idx = next((i for i, p in enumerate(priority_first)
                         if p in slug), 999)
        return (prio_idx, -len(item[2]))

    skills.sort(key=keyfn)
    return skills


GITHUB_BLOB = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main"


def rewrite_relative_links(body: str, plugin: str) -> str:
    """Schreibt Repo-interne relative Markdown-Links in absolute GitHub-URLs um.

    Im konkatenierten Vollprüfung funktionieren die urspruenglichen
    `../../references/...`-Pfade nicht, weil die Datei unter
    `testakten/megaprompts/<plugin>.md` liegt. Wir loesen sie zum Skill-
    Verzeichnis hin auf und erzeugen GitHub-Blob-URLs.
    """
    # Pattern: ](../*pfad) — wir ersetzen den (../)+ Praefix.
    def repl(m: re.Match[str]) -> str:
        ups = m.group(1).count('../')
        rest = m.group(2)
        # Skill liegt unter <plugin>/skills/<slug>/SKILL.md.
        # Mit ups=3 wandert man zum Repo-Root. Sonst Pfad als-ist verwenden.
        if ups >= 3:
            return f"]({GITHUB_BLOB}/{rest})"
        if ups == 2:
            return f"]({GITHUB_BLOB}/{plugin}/{rest})"
        if ups == 1:
            return f"]({GITHUB_BLOB}/{plugin}/skills/{rest})"
        return m.group(0)

    return re.sub(r"\]\((\.\./(?:\.\./)*)([^)]+)\)", repl, body)


def build_megaprompt(plugin_dir: Path) -> str | None:
    """Erzeugt Vollprüfung-Markdown fuer ein Plugin. None bei skip."""
    plugin = plugin_dir.name
    if plugin in EXCLUDE_PLUGINS:
        return None
    skills = collect_skills(plugin_dir)
    if not skills:
        return None
    n_total = len(skills)
    has_argumentation_core = any(slug == "juristischer-argumentationskern" for slug, *_ in skills)
    tier_total = n_total - int(has_argumentation_core)
    if tier_total > 100:
        # Mega-grosse Plugins (z.B. arbeitsrecht, gesellschaftsrecht): top-8
        skills = skills[:8]
        coverage = f"top-8 von {n_total} Skills (gekürzt für das Arbeitsfenster)"
    elif tier_total > 60:
        # Grosse Plugins (z.B. insolvenzrecht): top-10
        skills = skills[:10]
        coverage = f"top-10 von {n_total} Skills"
    elif tier_total > 20:
        skills = skills[:15]
        coverage = f"top-15 von {n_total} Skills"
    else:
        coverage = f"alle {n_total} Skills"

    lines = []
    lines.append(f'# Vollprüfung: {plugin}')
    lines.append('')
    lines.append(f'## Zusammensetzung')
    lines.append('')
    lines.append(f'Diese Vollprüfung enthält {coverage} des Plugins `{plugin}`.')
    lines.append('')
    lines.append('## Inhaltsverzeichnis')
    lines.append('')
    for i, (slug, _, desc, _) in enumerate(skills, 1):
        short = desc[:120] + ('…' if len(desc) > 120 else '')
        lines.append(f'{i}. **{slug}** — {short}')
    lines.append('')
    lines.append('---')
    lines.append('')

    for slug, _, desc, body in skills:
        lines.append(f'## Skill: `{slug}`')
        lines.append('')
        if desc:
            lines.append(f'_{desc}_')
            lines.append('')
        lines.append(rewrite_relative_links(body, plugin))
        lines.append('')
        lines.append('---')
        lines.append('')

    lines.append('## Anwendungshinweise')
    lines.append('')
    lines.append('1. Diese Vollprüfung als Kontext einfügen oder als Datei hochladen.')
    lines.append('2. Den eigentlichen juristischen Fall beschreiben.')
    lines.append('3. Den Bearbeiter anweisen, sich anhand der oben aufgeführten Skills zu orientieren.')
    lines.append('4. Entscheidungen nur nach Prüfung von Gericht, Datum, Aktenzeichen, tragender Aussage und amtlicher oder frei zugänglicher Quelle verwenden.')
    lines.append('')
    return '\n'.join(lines).rstrip() + '\n'


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    created = 0
    skipped = 0
    too_big_skip = 0
    # Top-Level-Plugins plus Sammelordner gerichtsplugins/
    candidate_dirs = list(REPO.iterdir())
    gerichts_dir = REPO / 'gerichtsplugins'
    if gerichts_dir.is_dir():
        candidate_dirs.extend(gerichts_dir.iterdir())
    for plugin_dir in sorted(candidate_dirs, key=lambda p: p.name):
        if not plugin_dir.is_dir():
            continue
        # nur echte Plugin-Verzeichnisse (mit .claude-plugin/plugin.json)
        if not (plugin_dir / '.claude-plugin' / 'plugin.json').is_file():
            continue
        if plugin_dir.name in EXCLUDE_PLUGINS:
            skipped += 1
            continue
        mp = build_megaprompt(plugin_dir)
        if mp is None:
            skipped += 1
            continue
        out_path = OUT / f'{plugin_dir.name}.md'
        out_path.write_text(mp, encoding='utf-8')
        size_kb = out_path.stat().st_size / 1024
        if size_kb > 200:
            print(f'  WARN {plugin_dir.name}: {size_kb:.0f} KB (gross fuer Chat-Fenster)')
        created += 1
    print(f'Vollprüfungen erstellt: {created} | übersprungen: {skipped}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
