#!/usr/bin/env python3
"""
Umlaut-Fix mit Hash/ID-Schutz.

Sicher gegen:
- Hash-Strings (SHA-Fragmente, jede Hex-Sequenz >=4 Zeichen)
- Code-Bloecke (``` ... ```)
- Inline-Code (`...`)
- URLs
- YAML-Frontmatter
- Slug-aehnliche Tokens (lowercase + Hex/Bindestriche)
- CSV-Zellen-Inhalt der Hash-Spalten

Nur ganze Woerter \\b...\\b in Plaintext werden ersetzt.
"""
import re
import sys
from pathlib import Path

# Wort-Mapping. Reihenfolge: laengere/spezifischere ZUERST.
REPLACEMENTS = [
    # zusammengesetzte/spezifische zuerst
    ('Aussenwirtschaft', 'Außenwirtschaft'),
    ('Aussendienst', 'Außendienst'),
    ('Praezisions', 'Präzisions'),
    ('Rangruecktritt', 'Rangrücktritt'),
    ('sinngemaess', 'sinngemäß'),
    ('maszgeblich', 'maßgeblich'),
    ('Maszgaben', 'Maßgaben'),
    ('Maszgabe', 'Maßgabe'),
    ('Maszstab', 'Maßstab'),
    ('maszstaeblich', 'maßstäblich'),
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

# Schutz-Patterns: VOR Ersetzung stashen, NACH Ersetzung zuruecktauschen
# Reihenfolge wichtig: zuerst die groebsten Bereiche, dann die feinen Tokens.
PROTECT_PATTERNS = [
    # YAML-Frontmatter
    re.compile(r'\A---\n.*?\n---\n', re.DOTALL),
    # Fenced code blocks
    re.compile(r'```.*?```', re.DOTALL),
    # Inline code
    re.compile(r'`[^`\n]+`'),
    # Markdown-Links/Bilder: (path/URL)-Teil schützen ZUERST (vor URL-only).
    # Anchor-Text bleibt frei, nur ](...)-Klammerinhalt wird geschützt.
    re.compile(r'\]\([^)\n]+\)'),
    # URLs (http/https) — KEIN \S+ wegen schliessender Klammern!
    # Erlaubte URL-Zeichen ohne ) und ohne Whitespace.
    re.compile(r'https?://[^\s)\]>]+'),
    # Hex-Hashes / IDs / SHA-Fragmente: jede Sequenz mit >=4 Hex-Zeichen
    # zusammen mit angrenzenden Buchstaben/Ziffern/Bindestrichen.
    # Beispiel: 6d7712ae8f, sha256: abc1234..., file_a1b2c3
    re.compile(r'\b[A-Za-z0-9_-]*[0-9][0-9a-fA-F]{3,}[A-Za-z0-9_-]*\b'),
    re.compile(r'\b[0-9a-fA-F]{4,}\b'),
    # Slug-aehnliche Tokens: lowercase + Bindestrich (z.B. Verzeichnisnamen)
    re.compile(r'\b[a-z]+(?:-[a-z0-9]+){2,}\b'),
    # CSV-Spaltenheader (snake_case mit Unterstrich) — typisch sha256_kurz, groesse_kb
    re.compile(r'\b[a-z]+(?:_[a-z0-9]+)+\b'),
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
    # Iterativ aufloesen: Placeholder koennen geschachtelt sein
    # (ein gestashter Bereich enthielt selbst schon einen aelteren Placeholder).
    prev = None
    while prev != text:
        prev = text
        text = re.sub(r'\x00PROTECT(\d+)\x00', replacer, text)
    return text


def apply_replacements(text):
    for old, new in REPLACEMENTS:
        # Wort-Grenzen: nur ganze Woerter ersetzen
        text = re.sub(r'\b' + re.escape(old) + r'\b', new, text)
    return text


def process_file(path):
    try:
        original = path.read_text(encoding='utf-8')
    except (UnicodeDecodeError, OSError):
        return False, 0

    protected, placeholders = stash_protected(original)
    replaced = apply_replacements(protected)
    restored = unstash_protected(replaced, placeholders)

    if restored != original:
        # Sanity-Check: KEINE neuen Umlaute neben Hex-Strings entstanden
        # (z.B. 6d7712ä waere eine Korruption)
        # Pruefe: jede [äöüÄÖÜß] darf NICHT direkt vor/nach Hex-Sequenz stehen,
        # die selbst Teil eines laengeren alnum-Tokens ist.
        for m in re.finditer(r'[äöüÄÖÜß]', restored):
            i = m.start()
            # 6 Zeichen Kontext links
            left = restored[max(0, i - 6):i]
            right = restored[i + 1:i + 7]
            # Wenn links eine reine Hex-Sequenz steht UND rechts alnum -> verdaechtig
            if re.search(r'[0-9a-f]{4,}$', left) and re.match(r'[A-Za-z0-9_-]', right):
                print(f'  CORRUPTION RISK in {path}: ...{left}{m.group(0)}{right}...', file=sys.stderr)
                return False, 0
            if re.match(r'^[0-9a-f]{4,}', right) and re.search(r'[A-Za-z0-9_-]$', left):
                print(f'  CORRUPTION RISK in {path}: ...{left}{m.group(0)}{right}...', file=sys.stderr)
                return False, 0
        path.write_text(restored, encoding='utf-8')
        # Anzahl Ersetzungen grob
        diff_count = sum(1 for a, b in zip(original, restored) if a != b)
        return True, diff_count
    return False, 0


def main(root='testakten'):
    base = Path(root)
    if not base.exists():
        print(f'no such dir: {root}', file=sys.stderr)
        sys.exit(1)
    changed_files = 0
    total_chars = 0
    extensions = ('*.md', '*.eml', '*.txt', '*.csv')
    for ext in extensions:
        for p in base.rglob(ext):
            ok, n = process_file(p)
            if ok:
                changed_files += 1
                total_chars += n
                print(f'  {p}: ~{n} chars changed')
    print(f'\nDone: {changed_files} files changed (~{total_chars} chars).')


if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else 'testakten'
    main(root)
