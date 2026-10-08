#!/usr/bin/env python3
"""
Regel 12: Anwendungsbereich nur im README.
Migiert ## Anwendungsbereich aus allen VORLAGE.md in die jeweilige README.md
und entfernt den Abschnitt aus VORLAGE.md.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECTION_RE = re.compile(
    r'^(## Anwendungsbereich|## Anwendungshinweise|## Geeignet(?:e Einsatzfälle)?|## Einsatzbereich|## Hinweise zur Verwendung|## Typische Einsatzfälle)\s*$',
    re.MULTILINE
)

def extract_section(text, header_match):
    """Gibt (section_text, remaining_text) zurück."""
    start = header_match.start()
    # Nächste ## auf gleicher Ebene
    rest_after = text[header_match.end():]
    next_h2 = re.search(r'^## ', rest_after, re.MULTILINE)
    if next_h2:
        end = header_match.end() + next_h2.start()
    else:
        end = len(text)
    section = text[start:end].rstrip('\n') + '\n'
    remaining = text[:start].rstrip('\n') + '\n' + text[end:]
    # Doppelte Leerzeilen bereinigen
    remaining = re.sub(r'\n{3,}', '\n\n', remaining)
    return section, remaining


def inject_into_readme(readme_text, section_text):
    """Fügt den Abschnitt vor ## Warnung (oder am Ende) ein, falls noch nicht vorhanden."""
    existing = re.search(r'^## Anwendungsbereich.*?(?=\n## |\Z)', readme_text,
                         re.MULTILINE | re.DOTALL)
    if existing:
        # Nicht verwerfen: inhaltsreichere Fassung behalten. Ist der aus der
        # VORLAGE.md extrahierte Abschnitt laenger, ersetzt er den vorhandenen.
        if len(section_text.strip()) > len(existing.group(0).strip()):
            return readme_text[:existing.start()] + section_text.rstrip('\n') + '\n' + readme_text[existing.end():]
        return readme_text
    # Vor ## Warnung einfügen
    warnung = re.search(r'^## Warnung', readme_text, re.MULTILINE)
    if warnung:
        pos = warnung.start()
        return readme_text[:pos] + section_text.rstrip('\n') + '\n\n' + readme_text[pos:]
    # Fallback: ans Ende
    return readme_text.rstrip('\n') + '\n\n' + section_text.rstrip('\n') + '\n'


def process_template(vorlage_path):
    readme_path = os.path.join(os.path.dirname(vorlage_path), 'README.md')
    with open(vorlage_path, encoding='utf-8') as f:
        vorlage = f.read()

    m = SECTION_RE.search(vorlage)
    if not m:
        return False  # Kein Abschnitt gefunden

    section, vorlage_new = extract_section(vorlage, m)

    # README laden oder anlegen
    if os.path.exists(readme_path):
        with open(readme_path, encoding='utf-8') as f:
            readme = f.read()
    else:
        readme = ''

    readme_new = inject_into_readme(readme, section)

    # Nur schreiben, wenn sich etwas geändert hat
    if vorlage_new != vorlage:
        with open(vorlage_path, 'w', encoding='utf-8') as f:
            f.write(vorlage_new)
    if readme_new != readme:
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_new)

    return True


def main():
    changed = 0
    skipped = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in sorted(dirnames)
                       if not d.startswith('.') and d != 'scripts' and d != 'templates'
                       and d != 'references' and d != 'runs']
        if 'VORLAGE.md' in filenames:
            vorlage_path = os.path.join(dirpath, 'VORLAGE.md')
            if process_template(vorlage_path):
                rel = os.path.relpath(vorlage_path, ROOT)
                print(f'  migriert: {rel}')
                changed += 1
            else:
                skipped += 1

    print(f'\nFertig: {changed} migriert, {skipped} ohne Anwendungsbereich-Abschnitt.')


if __name__ == '__main__':
    main()
