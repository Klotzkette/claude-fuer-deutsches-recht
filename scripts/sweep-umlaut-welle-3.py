#!/usr/bin/env python3
"""
Welle 3 — Komposita-Stamm-Sweep + description-Frontmatter.

Erweitert Welle 2 um:
- Stamm-Ersetzungen (Wortanfang \\b, kein \\b am Ende) — erfasst Komposita
  wie Pruefungsschritt, Geschaeftsbereich, Beschaeftigungsverhaeltnis.
- Separates Pass fuer YAML-Frontmatter description-Feld (nur dieses Feld,
  nicht name).
- Behaelt Schutz fuer Code-Bloecke, URLs, Hashes, Slugs.

Aufruf:
    python3 scripts/sweep-umlaut-welle-3.py             # apply
    python3 scripts/sweep-umlaut-welle-3.py --dry-run   # only count
"""
import re
import sys
from pathlib import Path

# Stamm-Ersetzungen: nur \b am Anfang, KEIN \b am Ende.
# Reihenfolge: laengere/spezifischere zuerst (avoid Pruef vor Pruefung etc.).
STEMS = [
    # zusammengesetzte Stamm-Spezialfaelle zuerst
    ('Verhaeltnismaessigkeit', 'Verhältnismäßigkeit'),
    ('verhaeltnismaessigkeit', 'verhältnismäßigkeit'),
    ('Verhaeltnismaessig', 'Verhältnismäßig'),
    ('verhaeltnismaessig', 'verhältnismäßig'),
    ('Beschaeftigung', 'Beschäftigung'),
    ('beschaeftigung', 'beschäftigung'),
    ('Beschaeftigte', 'Beschäftigte'),
    ('beschaeftigte', 'beschäftigte'),
    ('Beschaeftig', 'Beschäftig'),
    ('beschaeftig', 'beschäftig'),
    ('Pruefungsentscheid', 'Prüfungsentscheid'),
    ('pruefungsentscheid', 'prüfungsentscheid'),
    ('Pruefungsordnung', 'Prüfungsordnung'),
    ('pruefungsordnung', 'prüfungsordnung'),
    ('Pruefungsrecht', 'Prüfungsrecht'),
    ('pruefungsrecht', 'prüfungsrecht'),
    ('Pruefungstermin', 'Prüfungstermin'),
    ('pruefungstermin', 'prüfungstermin'),
    ('Pruefungs', 'Prüfungs'),
    ('pruefungs', 'prüfungs'),
    ('Pruefung', 'Prüfung'),
    ('pruefung', 'prüfung'),
    ('Pruefer', 'Prüfer'),
    ('pruefer', 'prüfer'),
    ('Pruef', 'Prüf'),
    ('pruef', 'prüf'),
    ('Geschaeftsfuehr', 'Geschäftsführ'),
    ('geschaeftsfuehr', 'geschäftsführ'),
    ('Geschaeftsbereich', 'Geschäftsbereich'),
    ('geschaeftsbereich', 'geschäftsbereich'),
    ('Geschaeftsleitung', 'Geschäftsleitung'),
    ('geschaeftsleitung', 'geschäftsleitung'),
    ('Geschaeftsgeheim', 'Geschäftsgeheim'),
    ('geschaeftsgeheim', 'geschäftsgeheim'),
    ('Geschaeftsstelle', 'Geschäftsstelle'),
    ('geschaeftsstelle', 'geschäftsstelle'),
    ('Geschaeftspartner', 'Geschäftspartner'),
    ('geschaeftspartner', 'geschäftspartner'),
    ('Geschaeftsordnung', 'Geschäftsordnung'),
    ('geschaeftsordnung', 'geschäftsordnung'),
    ('Geschaefts', 'Geschäfts'),
    ('geschaefts', 'geschäfts'),
    ('Geschaeft', 'Geschäft'),
    ('geschaeft', 'geschäft'),
    ('Massnahmen', 'Maßnahmen'),
    ('massnahmen', 'maßnahmen'),
    ('Massnahme', 'Maßnahme'),
    ('massnahme', 'maßnahme'),
    ('Massstab', 'Maßstab'),
    ('massstab', 'maßstab'),
    ('Verhaeltnisse', 'Verhältnisse'),
    ('verhaeltnisse', 'verhältnisse'),
    ('Verhaeltnis', 'Verhältnis'),
    ('verhaeltnis', 'verhältnis'),
    ('Klaegerin', 'Klägerin'),
    ('klaegerin', 'klägerin'),
    ('Klaeger', 'Kläger'),
    ('klaeger', 'kläger'),
    ('Klaerung', 'Klärung'),
    ('klaerung', 'klärung'),
    ('Klaeren', 'Klären'),
    ('klaeren', 'klären'),
    ('Aenderung', 'Änderung'),
    ('aenderung', 'änderung'),
    ('Aender', 'Änder'),
    ('aender', 'änder'),
    ('Erlaeuter', 'Erläuter'),
    ('erlaeuter', 'erläuter'),
    ('Aequivalent', 'Äquivalent'),
    ('aequivalent', 'äquivalent'),
    ('Aequival', 'Äquival'),
    ('aequival', 'äquival'),
    ('Schluessel', 'Schlüssel'),
    ('schluessel', 'schlüssel'),
    ('Bezuegliche', 'Bezügliche'),
    ('bezuegliche', 'bezügliche'),
    ('Hoehepunkt', 'Höhepunkt'),
    ('hoehepunkt', 'höhepunkt'),
    ('Hoehepkt', 'Höhepkt'),
    ('Selbstaendig', 'Selbständig'),
    ('selbstaendig', 'selbständig'),
    ('Auslaendisch', 'Ausländisch'),
    ('auslaendisch', 'ausländisch'),
    ('Auslaender', 'Ausländer'),
    ('auslaender', 'ausländer'),
    ('Glaeubiger', 'Gläubiger'),
    ('glaeubiger', 'gläubiger'),
    ('Glaeubig', 'Gläubig'),
    ('glaeubig', 'gläubig'),
    ('Verfahrensgrund', 'Verfahrensgrund'),  # noop reserved
    # ueber/Ueber als Praefix (häufige Komposita)
    ('Ueberpruefung', 'Überprüfung'),
    ('ueberpruefung', 'überprüfung'),
    ('Ueberpruef', 'Überprüf'),
    ('ueberpruef', 'überprüf'),
    ('Ueberlassung', 'Überlassung'),
    ('ueberlassung', 'überlassung'),
    ('Uebergabe', 'Übergabe'),
    ('uebergabe', 'übergabe'),
    ('Ueberlast', 'Überlast'),
    ('Uebersetz', 'Übersetz'),
    ('uebersetz', 'übersetz'),
    ('Ueberblick', 'Überblick'),
    ('ueberblick', 'überblick'),
    ('Ueberweisung', 'Überweisung'),
    ('ueberweisung', 'überweisung'),
    ('Ueberhang', 'Überhang'),
    ('ueberhang', 'überhang'),
    # fuer/Fuer als Praefix (Komposita)
    ('Fuersorge', 'Fürsorge'),
    ('fuersorge', 'fürsorge'),
    ('Fuerstent', 'Fürstent'),
    ('fuerstent', 'fürstent'),
    # Begriffe um Massstab
    ('Pruefmassstab', 'Prüfmaßstab'),
    ('pruefmassstab', 'prüfmaßstab'),
    ('Bewertungsmassstab', 'Bewertungsmaßstab'),
    # Aufsichts/Aufsicht
    ('Aufgepraegt', 'Aufgeprägt'),
    # Truncated common compounds
    ('Vermoegens', 'Vermögens'),
    ('vermoegens', 'vermögens'),
    ('Selbstaendig', 'Selbständig'),
]


PROTECT_PATTERNS = [
    re.compile(r'```.*?```', re.DOTALL),
    re.compile(r'`[^`\n]+`'),
    re.compile(r'\]\([^)\n]+\)'),
    re.compile(r'https?://[^\s)\]>]+'),
    re.compile(r'\b[A-Za-z0-9_-]*[0-9][0-9a-fA-F]{3,}[A-Za-z0-9_-]*\b'),
    re.compile(r'\b[0-9a-fA-F]{4,}\b'),
    re.compile(r'\b[a-z]+(?:-[a-z0-9]+){2,}\b'),
    re.compile(r'\b[a-z]+(?:_[a-z0-9]+)+\b'),
    re.compile(r'\b[a-z]{18,}\b'),
]


# Pattern: nur \b am Anfang, KEIN \b am Ende — fuer Stamm-Match.
COMPILED_STEMS = [
    (re.compile(r'\b' + re.escape(old)), new)
    for old, new in STEMS
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


def apply_stem_replacements(text):
    for pat, new in COMPILED_STEMS:
        text = pat.sub(new, text)
    return text


# Frontmatter description-Feld separate behandeln
FRONTMATTER_RE = re.compile(r'\A(---\n)(.*?)(\n---\n)', re.DOTALL)
DESCRIPTION_FIELD_RE = re.compile(
    r'^(description:\s*)(.+?)(?=^[a-z_]+:\s|\Z)', re.MULTILINE | re.DOTALL
)


def process_frontmatter_description(text):
    """Wendet Stamm-Ersetzungen NUR auf description: Feld an, NICHT auf name:."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return text
    fm = m.group(2)
    new_fm = DESCRIPTION_FIELD_RE.sub(
        lambda dm: dm.group(1) + apply_stem_replacements(dm.group(2)),
        fm,
    )
    if new_fm != fm:
        return m.group(1) + new_fm + m.group(3) + text[m.end():]
    return text


SKIP_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'venv',
             'docs', 'scripts', 'testakten'}


def process_file(path, dry_run=False):
    try:
        original = path.read_text(encoding='utf-8')
    except (UnicodeDecodeError, OSError):
        return False, 0

    # Schritt 1: Frontmatter-description bearbeiten (vor dem Protect-Stash)
    after_fm = process_frontmatter_description(original)

    # Schritt 2: Body mit Schutz bearbeiten
    # Frontmatter durch Stash schützen, damit es nicht doppelt geändert wird
    fm_match = FRONTMATTER_RE.match(after_fm)
    if fm_match:
        fm_block = fm_match.group(0)
        body = after_fm[fm_match.end():]
    else:
        fm_block = ''
        body = after_fm

    protected, placeholders = stash_protected(body)
    replaced = apply_stem_replacements(protected)
    restored = unstash_protected(replaced, placeholders)

    final = fm_block + restored

    if final != original:
        # Sanity-Check
        for m in re.finditer(r'[äöüÄÖÜß]', final):
            i = m.start()
            left = final[max(0, i - 6):i]
            right = final[i + 1:i + 7]
            if re.search(r'[0-9a-f]{4,}$', left) and re.match(r'[A-Za-z0-9_-]', right):
                print(f'  CORRUPTION RISK in {path}: ...{left}{m.group(0)}{right}...',
                      file=sys.stderr)
                return False, 0
            if re.match(r'^[0-9a-f]{4,}', right) and re.search(r'[A-Za-z0-9_-]$', left):
                print(f'  CORRUPTION RISK in {path}: ...{left}{m.group(0)}{right}...',
                      file=sys.stderr)
                return False, 0
        diff_count = sum(1 for a, b in zip(original, final) if a != b)
        if not dry_run:
            path.write_text(final, encoding='utf-8')
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
