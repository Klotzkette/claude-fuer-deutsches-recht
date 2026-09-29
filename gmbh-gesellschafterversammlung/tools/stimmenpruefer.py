#!/usr/bin/env python3
"""Rechnet vorgegebene Abstimmungsvarianten ohne rechtliche Einstufung.

Aufruf: python3 stimmenpruefer.py eingabe.json
Zahlen als ganze Stimmen oder exakte Zeichenfolgen wie "12.5" bzw. "1/3".
Die rechtlich einschlägige Stimmenbasis und etwaige Ausschlüsse sind Eingaben.
"""
from __future__ import annotations
import json
import sys
from fractions import Fraction
from pathlib import Path

BASES = {'abgegebene-gueltige-stimmen', 'stimmberechtigtes-gesamtkapital',
         'vertretenes-stimmberechtigtes-kapital', 'gesamtkapital'}
VOTES = {'ja', 'nein', 'enthaltung', 'ungueltig', 'abwesend'}


def exact(value):
    if isinstance(value, bool) or not isinstance(value, (str, int)):
        raise ValueError('Stimmen und Schwellen als ganze Zahl oder exakte Zeichenfolge angeben.')
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError('Ungültige rationale Zahl.') from exc


def unique_pairs(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError('Doppeltes JSON-Feld: ' + key)
        out[key] = value
    return out


def calculate(data):
    if not isinstance(data, dict):
        raise ValueError('Ein JSON-Objekt ist erforderlich.')
    if set(data) - {'basis', 'schwelle', 'vergleich', 'gesellschafter', 'ausschluesse', 'alternative_ausschluesse'}:
        raise ValueError('Unbekanntes Eingabefeld.')
    basis = data.get('basis')
    if basis not in BASES or data.get('vergleich') not in {'>', '>='}:
        raise ValueError('Stimmenbasis und Vergleich (> oder >=) ausdrücklich festlegen.')
    threshold = exact(data.get('schwelle'))
    if not 0 < threshold <= 1:
        raise ValueError('Die Schwelle muss größer als null und höchstens eins sein.')
    people = data.get('gesellschafter')
    if not isinstance(people, list) or not people:
        raise ValueError('Vollständige Gesellschafterliste erforderlich.')
    rows = {}
    for person in people:
        if not isinstance(person, dict) or set(person) != {'id', 'stimmen', 'votum'}:
            raise ValueError('Jeder Eintrag benötigt genau id, stimmen und votum.')
        ident = person['id']
        if not isinstance(ident, str) or not ident.strip() or ident in rows:
            raise ValueError('Eindeutige nicht leere Gesellschafterkennungen erforderlich.')
        weight = exact(person['stimmen'])
        if weight <= 0 or person['votum'] not in VOTES:
            raise ValueError('Positive Stimmenzahl und bekanntes Votum erforderlich.')
        rows[ident] = (weight, person['votum'])
    results = []
    for key in ['ausschluesse', 'alternative_ausschluesse']:
        if key not in data:
            if key == 'ausschluesse':
                raise ValueError('Ausschlüsse ausdrücklich als Liste angeben, nötigenfalls leer.')
            continue
        excluded = data[key]
        if not isinstance(excluded, list) or any(not isinstance(x, str) for x in excluded):
            raise ValueError('Ausschlüsse benötigen eine Liste von Kennungen.')
        if len(set(excluded)) != len(excluded) or not set(excluded) <= set(rows):
            raise ValueError('Unbekannte oder doppelte Ausschlusskennung.')
        totals = {vote: sum((w for ident, (w, v) in rows.items() if v == vote and ident not in excluded), Fraction()) for vote in VOTES}
        if basis == 'abgegebene-gueltige-stimmen':
            denominator = totals['ja'] + totals['nein']
        elif basis == 'stimmberechtigtes-gesamtkapital':
            denominator = sum(totals.values(), Fraction())
        elif basis == 'vertretenes-stimmberechtigtes-kapital':
            denominator = sum(totals.values(), Fraction()) - totals['abwesend']
        else:
            denominator = sum((w for w, _ in rows.values()), Fraction())
        ratio = totals['ja'] / denominator if denominator else None
        reached = None if ratio is None else (ratio > threshold if data['vergleich'] == '>' else ratio >= threshold)
        results.append({'variante': key, 'ausschluesse': excluded,
                        'stimmen': {v: str(totals[v]) for v in sorted(VOTES)},
                        'nenner': str(denominator), 'ja_anteil_exakt': str(ratio) if ratio is not None else None,
                        'arithmetische_schwelle_erreicht': reached})
    return {'basis': basis, 'schwelle': str(threshold), 'vergleich': data['vergleich'],
            'hinweis': 'Nur Rechenbefund. Stimmrecht, Stimmengewicht, Nenner, Beschlussfähigkeit, Format, Form und Feststellungsbefugnis werden nicht rechtlich entschieden.',
            'varianten': results}


def main():
    if len(sys.argv) != 2:
        raise ValueError('Aufruf: stimmenpruefer.py eingabe.json')
    raw = Path(sys.argv[1]).read_bytes()
    if len(raw) > 1_000_000:
        raise ValueError('Eingabedatei ist zu groß.')
    data = json.loads(raw, object_pairs_hook=unique_pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError('Nicht endliche Zahl.')))
    print(json.dumps(calculate(data), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print('Stimmenprüfung: ' + str(exc), file=sys.stderr)
        raise SystemExit(1)
