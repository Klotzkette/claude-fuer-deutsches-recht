#!/usr/bin/env python3
"""
Regel 13: Ungewöhnliche Abkürzungen beim ersten Auftreten ausschreiben.
Fügt in jede README.md und Vorlagen-Markdown-Datei bei der jeweils ersten Nennung
einer ungewöhnlichen Abkürzung die Langform in Klammern hinzu.
"""
import os
import re
import sys
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _vorlagen_dateien import md_in  # noqa: E402

# Abkürzung → Langform; Format: "ABBR" → "Langform (ABBR)"
# Wird nur dann eingefügt, wenn die Langform noch nicht im Text steht.
ABBREVS = [
    # Besonders ungewöhnlich (internationales Recht, Spezialbereiche)
    ("CMR",    "Übereinkommen über den Beförderungsvertrag im internationalen Straßengüterverkehr (CMR)"),
    ("CISG",   "UN-Kaufrecht (Convention on Contracts for the International Sale of Goods, CISG)"),
    ("VOB/B",  "Vergabe- und Vertragsordnung für Bauleistungen, Teil B (VOB/B)"),
    ("ADSP",   "Allgemeine Deutsche Spediteurbedingungen (ADSP)"),
    ("ZVG",    "Zwangsversteigerungsgesetz (ZVG)"),
    ("StaRUG", "Unternehmensstabilisierungs- und -restrukturierungsgesetz (StaRUG)"),
    # Bekannt, aber für Nichtjuristen erklärungswürdig
    ("WEG",    "Wohnungseigentumsgesetz (WEG)"),
    ("UmwG",   "Umwandlungsgesetz (UmwG)"),
    ("GmbHG",  "GmbH-Gesetz (GmbHG)"),
    ("AktG",   "Aktiengesetz (AktG)"),
    ("InsO",   "Insolvenzordnung (InsO)"),
]

# Schlüsselwörter, deren Vorhandensein auf eine bereits erfolgte Erklärung
# hinweist (je Abkürzung die ersten ~10 Zeichen der Langform).
LONGFORM_HINTS = {
    "CMR":    "Beförderungsvertrag im internationalen",
    "CISG":   "Convention on Contracts",
    "VOB/B":  "Vergabe- und Vertragsordnung",
    "ADSP":   "Allgemeine Deutsche Spediteurbedingungen",
    "ZVG":    "Zwangsversteigerungsgesetz",
    "StaRUG": "Unternehmensstabilisierungs",
    "WEG":    "Wohnungseigentumsgesetz",
    "UmwG":   "Umwandlungsgesetz",
    "GmbHG":  "GmbH-Gesetz",
    "AktG":   "Aktiengesetz",
    "InsO":   "Insolvenzordnung",
}

# In Titeln/H1 kein Einschub — dort nur Fließtextabschnitt prüfen.
# Wir überspringen Zeilen, die mit # beginnen (Markdown-Überschriften).

def already_explained(text, abbrev):
    hint = LONGFORM_HINTS.get(abbrev, "")
    return hint.lower() in text.lower()


def expand_first_occurrence(text, abbrev, longform):
    """
    Findet das erste Vorkommen von 'abbrev' als ganzes Wort und ersetzt es
    durch 'longform', sofern die Abkürzung nicht schon in Klammern nach einem
    Langtext steht. Überschriftenzeilen werden übersprungen.
    """
    # Regex: Abkürzung als ganzes Wort; nicht innerhalb von Klammern direkt nach Langform
    pattern = re.compile(r'(?<!\()\b' + re.escape(abbrev) + r'\b(?!\s*\()')

    lines = text.split('\n')
    for i, line in enumerate(lines):
        # Überschriften überspringen (aber Normzitate wie "§ 1 CMR" in Überschriften
        # können hier trotzdem bearbeitet werden — wir überspringen nur H1)
        if line.startswith('# ') and not line.startswith('## '):
            continue
        m = pattern.search(line)
        if m:
            # Ersetze NUR die erste Fundstelle in dieser Zeile
            new_line = line[:m.start()] + longform + line[m.end():]
            lines[i] = new_line
            return '\n'.join(lines)
    return text  # Keine Fundstelle → unverändert


def process_file(path):
    with open(path, encoding='utf-8') as f:
        original = f.read()

    text = original
    changed = False

    for abbrev, longform in ABBREVS:
        # Schnellcheck: Abkürzung überhaupt im Text?
        if not re.search(r'\b' + re.escape(abbrev) + r'\b', text):
            continue
        # Schon erklärt?
        if already_explained(text, abbrev):
            continue
        # Erste Nennung ausschreiben
        new_text = expand_first_occurrence(text, abbrev, longform)
        if new_text != text:
            text = new_text
            changed = True

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
    return changed


def main():
    changed = 0
    skipped = 0
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in sorted(dirnames)
                       if not d.startswith('.') and d not in
                       ('scripts', 'templates', 'references', 'runs')]
        md = md_in(Path(dirpath))
        allowed = {'README.md'}
        if md is not None:
            allowed.add(md.name)
        for fn in filenames:
            if fn in allowed:
                path = os.path.join(dirpath, fn)
                if process_file(path):
                    print(f'  aktualisiert: {os.path.relpath(path, ROOT)}')
                    changed += 1
                else:
                    skipped += 1

    print(f'\nFertig: {changed} aktualisiert, {skipped} bereits korrekt oder ohne Treffer.')


if __name__ == '__main__':
    main()
