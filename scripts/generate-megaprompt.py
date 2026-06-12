#!/usr/bin/env python3
"""generate-megaprompt.py - Konkateniert pro Plugin die Kern-Skills in ein
einzelnes Markdown ('Megaprompt'), das man ohne Claude Code als ein-Schuss-
Prompt verwenden kann.

Ausgabe: testakten/megaprompts/<plugin>.md

Auswahl-Heuristik:
- Plugins mit <= 20 Skills: ALLE Skills (Vollintegration)
- Plugins mit 21-60 Skills: top-15 Skills (Priorisierungsliste pro Plugin)
- Plugins mit > 60 Skills: SKIP (zu gross fuer Megaprompt)
- Skill-Auswahl bei mittlerer Groesse:
    * einstieg-routing / kaltstart-triage / mandat-triage immer first
    * weiter nach Frontmatter-description-Laenge (laengere=substantieller)

Pro Megaprompt:
- Header mit Disclaimer + Anleitung
- Inhaltsverzeichnis
- Konkatenierter Skill-Inhalt (Frontmatter entfernt)
- Footer: Hinweise
"""
from __future__ import annotations
import re
from pathlib import Path

REPO = Path('/home/user/claude-fuer-deutsches-recht')
OUT = REPO / 'testakten' / 'megaprompts'

# Plugins, die wir explizit AUSSCHLIESSEN (zu gross, zu fragmentiert,
# Megaprompt nicht sinnvoll):
EXCLUDE_PLUGINS = {
    'corporate-kanzlei',  # zu gross fuer ein Mega-Prompt
    'urteilsbauer-relationsmacher',  # tooling, kein workflow
    'verlagsredaktion',
    'zwangsverwaltung-zvg',
}

# Hinweis: Der Disclaimer- und Verwendungs-Block steht im jeweiligen
# Plugin-README, nicht im Megaprompt-Markdown selbst — der Megaprompt
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
    priority_first = ['einstieg-routing', 'kaltstart-triage', 'mandat-triage',
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


def build_megaprompt(plugin_dir: Path) -> str | None:
    """Erzeugt Megaprompt-Markdown fuer ein Plugin. None bei skip."""
    plugin = plugin_dir.name
    if plugin in EXCLUDE_PLUGINS:
        return None
    skills = collect_skills(plugin_dir)
    if not skills:
        return None
    n_total = len(skills)
    if n_total > 100:
        # Mega-grosse Plugins (z.B. arbeitsrecht, gesellschaftsrecht): top-8
        skills = skills[:8]
        coverage = f"top-8 von {n_total} Skills (gekuerzt fuer Chat-Fenster)"
    elif n_total > 60:
        # Grosse Plugins (z.B. insolvenzrecht): top-10
        skills = skills[:10]
        coverage = f"top-10 von {n_total} Skills"
    elif n_total > 20:
        skills = skills[:15]
        coverage = f"top-15 von {n_total} Skills"
    else:
        coverage = f"alle {n_total} Skills"

    lines = []
    lines.append(f'# Megaprompt: {plugin}')
    lines.append('')
    lines.append(f'## Zusammensetzung')
    lines.append('')
    lines.append(f'Dieser Megaprompt enthaelt {coverage} des Plugins `{plugin}`.')
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
        lines.append(body)
        lines.append('')
        lines.append('---')
        lines.append('')

    lines.append('## Anwendungshinweise')
    lines.append('')
    lines.append('1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.')
    lines.append('2. Den eigentlichen juristischen Fall beschreiben.')
    lines.append('3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.')
    lines.append('4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.')
    lines.append('')
    return '\n'.join(lines) + '\n'


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    created = 0
    skipped = 0
    too_big_skip = 0
    for plugin_dir in sorted(REPO.iterdir()):
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
    print(f'Megaprompts erstellt: {created} | uebersprungen: {skipped}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
