#!/usr/bin/env python3
"""Native Rechentests des bestehenden Builders; SOFFICE muss verfügbar sein.

Prüft echte Neuberechnung der exportierten Formeln, nicht bloß Formeltext.
Aufruf: SOFFICE=/pfad/soffice python3 scripts/test-liquiditaetsplanung-excel.py
"""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / 'liquiditaetsplanung/skills/liquiditaetsvorschau-3-6-12-monate/werkzeuge/build_liquiditaetsplan.py'
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}


def cell_values(path, sheet='xl/worksheets/sheet1.xml'):
    with zipfile.ZipFile(path) as archive:
        strings = []
        if 'xl/sharedStrings.xml' in archive.namelist():
            strings = [''.join(e.itertext()) for e in ET.fromstring(archive.read('xl/sharedStrings.xml')).findall('s:si', NS)]
        cells = {}
        for cell in ET.fromstring(archive.read(sheet)).findall('.//s:c', NS):
            value = cell.find('s:v', NS)
            value = value.text if value is not None else None
            if cell.get('t') == 's':
                value = strings[int(value)]
            elif cell.get('t') == 'inlineStr':
                value = ''.join(cell.find('s:is', NS).itertext())
            elif value is not None and cell.get('t') not in ('str', 'e'):
                value = float(value)
            cells[cell.get('r')] = value
        return cells


def run():
    soffice = os.environ.get('SOFFICE') or shutil.which('libreoffice') or shutil.which('soffice')
    if not soffice:
        raise SystemExit('SOFFICE fehlt; native Neuberechnung nicht geprüft.')
    with tempfile.TemporaryDirectory(prefix='liquiditaet-native-') as folder:
        folder = Path(folder)
        native = folder / 'native'
        native.mkdir()
        zero = {'einnahmen': {}, 'ausgaben': {}}
        cases = {
            'leer': ({}, ('offen', 'offen', 'OFFEN')),
            'gedeckt': ({'kassenbestand_start': 0, 'kontostand_start': 0, 'daten_bestaetigt': True,
                         'plan': [{'einnahmen': {'umsatz': 100}, 'ausgaben': {'miete': 100}}, zero, zero]}, (0, 0, 'PLAN GEDECKT')),
            'frueher-engpass': ({'kassenbestand_start': 0, 'kontostand_start': 0, 'daten_bestaetigt': True,
                                 'plan': [{'einnahmen': {}, 'ausgaben': {'miete': 100}}, zero,
                                          {'einnahmen': {'umsatz': 100}, 'ausgaben': {}}]}, (100, 1, 'BEDARF')),
            'nur-zwei-wochen': ({'kassenbestand_start': 0, 'kontostand_start': 500, 'daten_bestaetigt': True,
                                'plan': [zero, zero]}, ('offen', 'offen', 'OFFEN')),
            'kein-belegabgleich': ({'kassenbestand_start': 0, 'kontostand_start': 500,
                                  'plan': [zero, zero, zero]}, ('offen', 'offen', 'OFFEN')),
            'null': ({'kassenbestand_start': 0, 'kontostand_start': 0, 'daten_bestaetigt': True,
                      'plan': [zero, zero, zero]}, (0, 'n.a.', 'PLAN GEDECKT')),
            'vorwoche-fehlt': ({'kassenbestand_start': 0, 'kontostand_start': 500, 'daten_bestaetigt': True,
                                'plan': [{}, zero, zero, zero]}, ('offen', 'offen', 'OFFEN')),
            'vier-wochen-gedeckt': ({'kassenbestand_start': 0, 'kontostand_start': 500, 'daten_bestaetigt': True,
                                     'plan': [zero, zero, zero, zero]}, (0, 'n.a.', 'PLAN GEDECKT')),
        }
        # Fenster 2 übernimmt einen Anfangsbestand aus Woche 1. Auch wenn die
        # eigenen drei Wochen bestätigt sind, muss eine frühere Lücke wirken.
        following_windows = {
            'vorwoche-fehlt': ('offen', 'offen', 'OFFEN'),
            'vier-wochen-gedeckt': (0, 'n.a.', 'PLAN GEDECKT'),
        }
        for name, (data, _) in cases.items():
            data['stichtag'] = '2026-09-28'
            source = folder / f'{name}.json'
            source.write_text(json.dumps(data), encoding='utf-8')
            subprocess.run([sys.executable, str(BUILDER), '--eingabe', str(source), '--ausgabe', str(folder / f'{name}.xlsx')], check=True, capture_output=True, text=True)
        result = subprocess.run([soffice, f'-env:UserInstallation={folder.as_uri()}/profile', '--headless', '--convert-to', 'xlsx', '--outdir', str(native), *[str(p) for p in folder.glob('*.xlsx')]], check=True, capture_output=True, text=True, timeout=120)
        for name, (_, expected) in cases.items():
            target = native / f'{name}.xlsx'
            if not target.exists():
                raise AssertionError(f'Keine native Ausgabe für {name}: {result.stdout} {result.stderr}')
            cells = cell_values(target)
            actual = tuple(cells.get(c) for c in ('C42', 'C43', 'C44'))
            assert actual == expected, (name, actual, expected)
            if name in following_windows:
                actual_following = tuple(cells.get(c) for c in ('D42', 'D43', 'D44'))
                assert actual_following == following_windows[name], (name, 'Folgefenster', actual_following, following_windows[name])
            assert cells.get('N44') == 'OFFEN', (name, 'verkürzter Horizont')
            assert cells.get('O44') == 'OFFEN', (name, 'verkürzter Horizont')
            errors = {c: v for c, v in cells.items() if isinstance(v, str) and v.startswith(('#REF!', '#DIV/0!', '#VALUE!', '#NAME?', '#NUM!'))}
            assert not errors, (name, errors)
            print(f'OK native Neuberechnung: {name}')
        print(f'{len(cases)} native Szenarien bestanden; unvollständige Endhorizonte bleiben offen.')


if __name__ == '__main__':
    run()
