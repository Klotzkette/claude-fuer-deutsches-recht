#!/usr/bin/env python3
"""
Umlaut-Hygiene Welle 2.

Erweiterung von fix-umlaute-protected.py mit groesserer Wortliste fuer
juristische Standardbegriffe. Schuetzt zusaetzlich lange Lowercase-Slugs
(z.B. Plugin-Verzeichnisnamen wie verhaeltnismaessigkeitspruefer).

Default-Lauf nur ueber *.md im Repo, NICHT in testakten/, docs/, scripts/,
node_modules/, .git/. Beachtet Frontmatter, Code-Bloecke, URLs, Hashes,
Slugs.

Aufruf:
    python3 scripts/sweep-umlaut-welle-2.py             # Repo-Root, sicher
    python3 scripts/sweep-umlaut-welle-2.py --dry-run   # nur zaehlen
"""
import re
import sys
from pathlib import Path

REPLACEMENTS = [
    # zusammengesetzte/spezifische zuerst
    ('Verhaeltnismaessigkeit', 'Verhältnismäßigkeit'),
    ('verhaeltnismaessigkeit', 'verhältnismäßigkeit'),
    ('Verhaeltnismaessig', 'Verhältnismäßig'),
    ('verhaeltnismaessig', 'verhältnismäßig'),
    ('Aussenwirtschaft', 'Außenwirtschaft'),
    ('Aussendienst', 'Außendienst'),
    ('Praezisions', 'Präzisions'),
    ('Rangruecktritt', 'Rangrücktritt'),
    ('sinngemaess', 'sinngemäß'),
    ('Sinngemaess', 'Sinngemäß'),
    ('maszgeblich', 'maßgeblich'),
    ('Maszgaben', 'Maßgaben'),
    ('Maszgabe', 'Maßgabe'),
    ('Maszstab', 'Maßstab'),
    ('maszstaeblich', 'maßstäblich'),
    ('grundsaetzlich', 'grundsätzlich'),
    ('Grundsaetzlich', 'Grundsätzlich'),
    ('grundsaetz', 'grundsätz'),
    ('Grundsaetz', 'Grundsätz'),
    ('ausschliesslich', 'ausschließlich'),
    ('Ausschliesslich', 'Ausschließlich'),
    ('ausgepraegt', 'ausgeprägt'),
    ('Ausgepraegt', 'Ausgeprägt'),
    ('Erlaeuter', 'Erläuter'),
    ('erlaeuter', 'erläuter'),
    ('saemtlich', 'sämtlich'),
    ('Saemtlich', 'Sämtlich'),
    # Pruefung-Familie
    ('Pruefungs', 'Prüfungs'),
    ('pruefungs', 'prüfungs'),
    ('Pruefung', 'Prüfung'),
    ('pruefung', 'prüfung'),
    ('Pruefer', 'Prüfer'),
    ('pruefer', 'prüfer'),
    ('pruefen', 'prüfen'),
    ('Pruefen', 'Prüfen'),
    ('Pruefe', 'Prüfe'),
    ('prueft', 'prüft'),
    # Klaeger-Familie
    ('Klaeger', 'Kläger'),
    ('klaeger', 'kläger'),
    ('Klaerung', 'Klärung'),
    ('klaerung', 'klärung'),
    ('Klaeren', 'Klären'),
    ('klaeren', 'klären'),
    # Massnahme
    ('Massnahmen', 'Maßnahmen'),
    ('massnahmen', 'maßnahmen'),
    ('Massnahme', 'Maßnahme'),
    ('massnahme', 'maßnahme'),
    # Beschluss-Plural
    ('Beschluesse', 'Beschlüsse'),
    ('beschluesse', 'beschlüsse'),
    # Verguetung / Schluessel / Hoehe
    ('Verguetung', 'Vergütung'),
    ('verguetung', 'vergütung'),
    ('Schluessel', 'Schlüssel'),
    ('schluessel', 'schlüssel'),
    ('Hoehe', 'Höhe'),
    ('hoehe', 'höhe'),
    ('Aequivalenz', 'Äquivalenz'),
    ('aequivalent', 'äquivalent'),
    ('Aequivalent', 'Äquivalent'),
    # Gross-Familie (kurz, deshalb wortgrenzenstreng)
    ('grosser', 'großer'),
    ('Grosser', 'Großer'),
    ('grossen', 'großen'),
    ('Grossen', 'Großen'),
    ('grosses', 'großes'),
    ('Grosses', 'Großes'),
    ('grosse', 'große'),
    ('Grosse', 'Große'),
    ('gross', 'groß'),
    ('Gross', 'Groß'),
    # laesst
    ('laesst', 'lässt'),
    ('Laesst', 'Lässt'),
    # Naeher
    ('naeher', 'näher'),
    ('Naeher', 'Näher'),
    # Ausuebung
    ('ausuebung', 'ausübung'),
    ('Ausuebung', 'Ausübung'),
    # uebersicht etc.
    ('uebersicht', 'Übersicht'),
    ('Uebersicht', 'Übersicht'),
    ('uebertrag', 'übertrag'),
    ('Uebertrag', 'Übertrag'),
    ('vertraege', 'verträge'),
    ('Vertraege', 'Verträge'),
    ('bezueglich', 'bezüglich'),
    ('Bezueglich', 'Bezüglich'),
    ('genuegen', 'genügen'),
    ('Genuegen', 'Genügen'),
    ('eroeffn', 'eröffn'),
    ('Eroeffn', 'Eröffn'),
    ('zulaessig', 'zulässig'),
    ('Zulaessig', 'Zulässig'),
    ('zustaendig', 'zuständig'),
    ('Zustaendig', 'Zuständig'),
    ('oeffentlich', 'öffentlich'),
    ('Oeffentlich', 'Öffentlich'),
    ('voellig', 'völlig'),
    ('Voellig', 'Völlig'),
    ('aehnlich', 'ähnlich'),
    ('Aehnlich', 'Ähnlich'),
    ('nächst', 'nächst'),
    ('Nächst', 'Nächst'),
    ('später', 'später'),
    ('Spaeter', 'Später'),
    ('möglich', 'möglich'),
    ('Möglich', 'Möglich'),
    ('taetig', 'tätig'),
    ('Taetig', 'Tätig'),
    ('Vermoegen', 'Vermögen'),
    ('vermoegen', 'vermögen'),
    ('Geschaeft', 'Geschäft'),
    ('geschaeft', 'geschäft'),
    ('Eigentuemer', 'Eigentümer'),
    ('eigentuemer', 'eigentümer'),
    ('Gruender', 'Gründer'),
    ('gruender', 'gründer'),
    ('aendern', 'ändern'),
    ('Aendern', 'Ändern'),
    ('koennen', 'können'),
    ('Koennen', 'Können'),
    ('muessen', 'müssen'),
    ('Muessen', 'Müssen'),
    ('duerfen', 'dürfen'),
    ('Duerfen', 'Dürfen'),
    ('gemaess', 'gemäß'),
    ('Gemaess', 'Gemäß'),
    # kurze Woerter ZULETZT
    ('fuer', 'für'),
    ('Fuer', 'Für'),
    ('ueber', 'über'),
    ('Ueber', 'Über'),
]

PROTECT_PATTERNS = [
    re.compile(r'\A---\n.*?\n---\n', re.DOTALL),
    re.compile(r'```.*?```', re.DOTALL),
    re.compile(r'`[^`\n]+`'),
    re.compile(r'\]\([^)\n]+\)'),
    re.compile(r'https?://[^\s)\]>]+'),
    re.compile(r'\b[A-Za-z0-9_-]*[0-9][0-9a-fA-F]{3,}[A-Za-z0-9_-]*\b'),
    re.compile(r'\b[0-9a-fA-F]{4,}\b'),
    re.compile(r'\b[a-z]+(?:-[a-z0-9]+){2,}\b'),
    re.compile(r'\b[a-z]+(?:_[a-z0-9]+)+\b'),
    # NEU: lange Lowercase-Wörter (>=18 Zeichen) wahrscheinlich Slugs
    re.compile(r'\b[a-z]{18,}\b'),
]


def stash_protected(text):
    placeholders = []

    def replacer(m):
        placeholders.append(m.group(0))
        return f'\x00PROTECT{len(placeholders) - 1}\x00'

    for pat in PROTECT_PATTERNS:
        text = pat.sub(replacer, text)
    return text, placeholders


def unstash_protected(text, placeholders):
    def replacer(m):
        idx = int(m.group(1))
        return placeholders[idx]
    prev = None
    while prev != text:
        prev = text
        text = re.sub(r'\x00PROTECT(\d+)\x00', replacer, text)
    return text


COMPILED_REPLACEMENTS = [
    (re.compile(r'\b' + re.escape(old) + r'\b'), new)
    for old, new in REPLACEMENTS
]


def apply_replacements(text):
    for pat, new in COMPILED_REPLACEMENTS:
        text = pat.sub(new, text)
    return text


SKIP_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'venv',
             'docs', 'scripts', 'testakten'}


def process_file(path, dry_run=False):
    try:
        original = path.read_text(encoding='utf-8')
    except (UnicodeDecodeError, OSError):
        return False, 0

    protected, placeholders = stash_protected(original)
    replaced = apply_replacements(protected)
    restored = unstash_protected(replaced, placeholders)

    if restored != original:
        # Sanity-Check: keine neuen Umlaute neben Hex-Strings
        for m in re.finditer(r'[äöüÄÖÜß]', restored):
            i = m.start()
            left = restored[max(0, i - 6):i]
            right = restored[i + 1:i + 7]
            if re.search(r'[0-9a-f]{4,}$', left) and re.match(r'[A-Za-z0-9_-]', right):
                print(f'  CORRUPTION RISK in {path}: ...{left}{m.group(0)}{right}...',
                      file=sys.stderr)
                return False, 0
            if re.match(r'^[0-9a-f]{4,}', right) and re.search(r'[A-Za-z0-9_-]$', left):
                print(f'  CORRUPTION RISK in {path}: ...{left}{m.group(0)}{right}...',
                      file=sys.stderr)
                return False, 0
        diff_count = sum(1 for a, b in zip(original, restored) if a != b)
        if not dry_run:
            path.write_text(restored, encoding='utf-8')
        return True, diff_count
    return False, 0


def walk(root, dry_run=False):
    base = Path(root)
    changed_files = 0
    total_chars = 0
    for p in base.rglob('*.md'):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        ok, n = process_file(p, dry_run=dry_run)
        if ok:
            changed_files += 1
            total_chars += n
            marker = '[DRY]' if dry_run else ''
            print(f'  {marker} {p}: ~{n} chars')
    mode = 'dry-run' if dry_run else 'applied'
    print(f'\n{mode}: {changed_files} files changed (~{total_chars} chars).')


def main():
    dry_run = '--dry-run' in sys.argv
    root = '.'
    for arg in sys.argv[1:]:
        if not arg.startswith('--'):
            root = arg
            break
    walk(root, dry_run=dry_run)


if __name__ == '__main__':
    main()
