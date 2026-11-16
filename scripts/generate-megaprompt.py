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
- Fachaufgabe und Bearbeitungsweg
- Zusammensetzung des Dokuments
- Inhaltsverzeichnis
- Konkatenierter Skill-Inhalt (Frontmatter entfernt)
- Footer: Hinweise
"""
from __future__ import annotations


if __name__ == "__main__":
    from generator_cli import parse_generator_cli

    parse_generator_cli(__doc__)
import json
import re
from pathlib import Path

from prompt_profiles import enabled, hand_curated, standalone_kinds
from skill_sources import original_skill_sources, replacements
from werkstatt_visualisierung import block as visual_block, remove_block as remove_visual_block
from urllib.parse import quote

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
    priority_first = ['einfuehrung-pruefauftrag',
                      'juristischer-argumentationskern',
                      'bea-versandmappe-endfertigung',
                      'versandmappe-endfertigen',
                      'anlagen-zu-schriftsaetzen',
                      'vergaberechtliche-pruefung-anwaltlich-vollpruefung',
                      'einstieg-routing', 'kaltstart-triage', 'mandat-triage',
                      'orientierung', 'mandat-intake-und-konfliktpruefung',
                      'erstgespraech-mandatsannahme', 'erstpruefung-und-mandatsziel']
    skills = []
    for skill_md in original_skill_sources(plugin_dir):
        text = skill_md.read_text(encoding='utf-8', errors='ignore')
        fm, body = extract_frontmatter_and_body(text)
        desc = get_description(fm)
        skills.append((skill_md.parent.name, skill_md, desc, body))

    # Sortierung: Prioritaeten zuerst, dann Description-Laenge (= Substanz-Proxy)
    def keyfn(item):
        slug = item[0]
        prio_idx = next((i for i, p in enumerate(priority_first)
                         if p in slug), 999)
        return (prio_idx, -len(item[2]))

    skills.sort(key=keyfn)
    return skills


GITHUB_BLOB = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main"


def rewrite_relative_links(body: str, skill_path: Path) -> str:
    """Schreibt Repo-interne relative Markdown-Links in absolute GitHub-URLs um.

    Im konkatenierten Vollprüfung funktionieren die urspruenglichen
    Referenzpfade nicht, weil die Datei unter `testakten/megaprompts/` liegt.
    Jeder lokale Pfad wird deshalb relativ zum ursprünglichen Skill-Verzeichnis
    aufgelöst und als absolute Repository-URL ausgegeben.
    """

    def repl(m: re.Match[str]) -> str:
        target = m.group(1).strip()
        if target.startswith(("http://", "https://", "mailto:", "#", "/")):
            return m.group(0)
        raw_path, separator, fragment = target.partition("#")
        resolved = (skill_path.parent / raw_path).resolve()
        try:
            repo_path = resolved.relative_to(REPO.resolve())
        except ValueError:
            return m.group(0)
        if not resolved.exists():
            return m.group(0)
        url = f"{GITHUB_BLOB}/{quote(repo_path.as_posix(), safe='/')}"
        if separator:
            url += f"#{fragment}"
        return f"]({url})"

    return re.sub(r"\]\(([^)]+)\)", repl, body)


def workflow_opening(plugin_dir: Path) -> str:
    """Übernimmt den fachlichen Einstieg aus dem jeweiligen Einzelprompt."""

    plugin = plugin_dir.name
    purpose = ""
    for kind in standalone_kinds(plugin):
        prompt = plugin_dir / f'{plugin}-{kind}.md'
        if prompt.is_file():
            text = re.sub(r'<!--.*?-->', '', prompt.read_text(encoding='utf-8'), flags=re.S)
            purpose = next(
                (part.strip() for part in re.split(r'\n\s*\n', text)
                 if part.strip() and not part.lstrip().startswith('#')),
                '',
            )
            if purpose:
                purpose = rewrite_relative_links(purpose, prompt)
                break
    if not purpose:
        path = plugin_dir / '.claude-plugin/plugin.json'
        purpose = json.loads(path.read_text(encoding='utf-8')).get('description', '') if path.is_file() else ''
    return '\n\n'.join(part for part in (
        purpose,
        'Lies zuerst die zum Auftrag gehörenden Unterlagen und nutze die passenden Fachabschnitte. '
        'Wenn das gewünschte Ergebnis offen ist, frage danach. Bei einem klaren Auftrag beginne mit '
        'dem bestellten Arbeitsprodukt. Kläre nur Lücken, die es verändern. Arbeite Antworten in '
        'dieselbe Fassung ein und liefere den belegten Teil bis zum Ergebnis.',
    ) if part)


def render_skill(skill_path: Path, description: str, body: str) -> str:
    sections = [f'## Skill: `{skill_path.parent.name}`']
    if description:
        sections.append(f'_{description}_')
    sections.append(rewrite_relative_links(remove_visual_block(body).strip(), skill_path))
    return '\n\n'.join(sections)


def build_megaprompt(plugin_dir: Path) -> str | None:
    """Erzeugt Vollprüfung-Markdown fuer ein Plugin. None bei skip."""
    if not enabled(plugin_dir.name, "megaprompt"):
        return None
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
    lines.append(workflow_opening(plugin_dir))
    lines.append('')
    lines.append('## Zusammensetzung')
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

    for _slug, skill_path, desc, body in skills:
        lines.append(render_skill(skill_path, desc, body))
        lines.append('')
        lines.append('---')
        lines.append('')

    replacement = replacements().get(plugin)
    if replacement and plugin_dir.resolve() == (REPO / replacement['source']).resolve():
        for relative in replacement['chapters']:
            chapter = plugin_dir / relative
            if not chapter.is_file() or not chapter.resolve().is_relative_to(plugin_dir.resolve()):
                raise ValueError(f'Fachkapitel fehlt oder liegt außerhalb des Plugins: {relative}')
            lines.append(rewrite_relative_links(chapter.read_text(encoding='utf-8').strip(), chapter))
            lines.extend(['', '---', ''])

    lines.append('## Anwendungshinweise')
    lines.append('')
    if plugin == 'arbeitszeugnispruefer':
        lines.append('1. Diese Vollprüfung zur Zeugnisprüfung als einzelne Datei hochladen oder in den Chat einfügen; sie beginnt ohne weitere Startformel mit dem oben geregelten Dialog.')
        lines.append('2. Vorhandenes Zeugnis und Prüfziel bereitstellen. Fehlt das Zeugnis, konkret danach fragen, statt diese Anweisung zusammenzufassen.')
        lines.append('3. Tatsächliche Antworten im bestehenden Stand verarbeiten; nach Klärung oder festgestellter Beweisgrenze die geschuldeten Schreiben vollständig erstellen. Arbeitgeberantwort und neue Fassung lösen die gezielte Kontrollschleife aus.')
        lines.append('4. Ohne Quellenzugriff die eingebetteten Anker als bereitgestelltes, nicht live geprüftes Material behandeln; keine Verifikation behaupten und keine Nachweise erfinden.')
    else:
        lines.append(
            'Verwende diese Datei als Arbeitsanweisung. Prüfe den einschlägigen Normstand '
            'und die falltragenden Entscheidungen in einer amtlichen oder frei zugänglichen '
            'Quelle. Prüfe dabei auch Reichweite und spätere Rechtsprechung zur konkreten Frage.'
        )
    lines.append('')
    return visual_block('\n'.join(lines).rstrip() + '\n', plugin)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    created = 0
    skipped = 0
    marketplace = json.loads((REPO / '.claude-plugin/marketplace.json').read_text(encoding='utf-8'))
    candidate_dirs = [REPO / entry['source'] for entry in marketplace['plugins']]
    for plugin_dir in sorted(candidate_dirs, key=lambda p: p.name):
        if not plugin_dir.is_dir():
            continue
        # nur echte Plugin-Verzeichnisse (mit .claude-plugin/plugin.json)
        if not (plugin_dir / '.claude-plugin' / 'plugin.json').is_file():
            continue
        if plugin_dir.name in EXCLUDE_PLUGINS or not enabled(plugin_dir.name, 'megaprompt'):
            skipped += 1
            continue
        out_path = OUT / f'{plugin_dir.name}.md'
        if (hand_curated(plugin_dir.name) and out_path.is_file()
                and not out_path.read_text(encoding='utf-8').startswith(f'# Vollprüfung: {plugin_dir.name}\n')):
            # Ein eigenständig redigierter Master-Prompt ist kein Generator-Export.
            skipped += 1
            continue
        mp = build_megaprompt(plugin_dir)
        if mp is None:
            skipped += 1
            continue
        out_path.write_text(mp, encoding='utf-8')
        size_kb = out_path.stat().st_size / 1024
        if size_kb > 200:
            print(f'  WARN {plugin_dir.name}: {size_kb:.0f} KB (gross fuer Chat-Fenster)')
        created += 1
    print(f'Vollprüfungen erstellt: {created} | übersprungen: {skipped}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
