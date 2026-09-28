#!/usr/bin/env python3
"""Prüft Schnittflugs neue Finanzmappen mit echter LibreOffice-Neuberechnung.

Aufruf: SOFFICE=/pfad/zu/soffice python3 scripts/test-schnittflug-finanz-native.py
Optional: --report DATEI.json. Ohne SOFFICE wird soffice bzw. libreoffice im PATH
gesucht. Fehlt LibreOffice, endet der Test mit Fehler statt mit einem stillen Skip.
Alle bearbeiteten XLSX liegen in einem TemporaryDirectory. Die Originale bleiben
unverändert. Benötigt ausschließlich die Python-Standardbibliothek.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import posixpath
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import xml.etree.ElementTree as ET
import zipfile


ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / 'testakten/startup-gruender-schnittflug-berlin'
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
TAG = '{' + NS['s'] + '}'
RID = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'
EXPENSES = '140_Nachgereichte_Auslagen_20260928.xlsx'
FINANCING = '141_Finanzierungsbedingungen_und_Faelligkeiten.xlsx'

CASES = [
    {'source': EXPENSES, 'name': '', 'expected': {
        'Abgleich!D9': 3896.89, 'Abgleich!E9': 3261.61, 'Abgleich!F9': 635.28,
        'Abgleich!J33': 0, 'Abgleich!F22': 299.80,
    }},
    {'source': FINANCING, 'name': '', 'expected': {
        'Finanzierung!E7': 0, 'Finanzierung!E8': 0,
        'Finanzierung!E25': 3, 'Finanzierung!E26': 4,
        'Fälligkeiten!G12': 635.28, 'Fälligkeiten!E23': 21420,
        'Mittelverwendung!G28': 6365, 'Mittelverwendung!C8': 35000,
    }},
    {'source': EXPENSES, 'name': 'teilfreigabe',
     'change': ('Abgleich', 'G22', 'Ja'), 'expected': {'Abgleich!J22': 0}},
    {'source': EXPENSES, 'name': 'vollzahlung',
     'change': ('Zahlungen', 'F20', 499.80), 'expected': {
         'Abgleich!F22': 0, 'Abgleich!F9': 335.48, 'Abgleich!E9': 3561.41,
     }},
    {'source': EXPENSES, 'name': 'doppelte_id',
     'change': ('Kosten', 'B8', 'SF-A001'),
     'expected': {'Abgleich!D16': 'Beleg-ID prüfen'},
     'expected_errors': {'Abgleich': [
         ['F16', '#VALUE!'], ['F17', '#VALUE!'], ['F33', '#VALUE!'],
         ['F37', '#VALUE!'], ['F38', '#VALUE!'],
     ]}},
    {'source': FINANCING, 'name': 'spaeteres_budget',
     'change': ('Mittelverwendung', 'C26', 5000), 'expected': {
         'Mittelverwendung!G26': 6067, 'Mittelverwendung!G28': 5565,
     }},
    {'source': FINANCING, 'name': 'erste_bedingung',
     'change': ('Finanzierung', 'E16', 'Erfüllt'), 'expected': {
         'Finanzierung!E25': 2, 'Finanzierung!E7': 0, 'Finanzierung!E8': 0,
     }},
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def sheet_paths(parts: dict[str, bytes]) -> dict[str, str]:
    relationships = ET.fromstring(parts['xl/_rels/workbook.xml.rels'])
    targets = {node.get('Id'): node.get('Target') for node in relationships}
    workbook = ET.fromstring(parts['xl/workbook.xml'])
    result = {}
    for node in workbook.find('s:sheets', NS):
        target = targets[node.get(RID)]
        result[node.get('name')] = (
            target.lstrip('/') if target.startswith('/')
            else posixpath.normpath(posixpath.join('xl', target))
        )
    return result


def load_parts(path: Path) -> dict[str, bytes]:
    with zipfile.ZipFile(path) as archive:
        return {name: archive.read(name) for name in archive.namelist()}


def create_input(source: Path, output: Path, change: tuple | None) -> int:
    """Ändert nur eine Eingabe in einer Wegwerfkopie und leert alle Formelcaches."""
    parts = load_parts(source)
    paths = sheet_paths(parts)
    if change:
        sheet, address, value = change
        xml = ET.fromstring(parts[paths[sheet]])
        cell = xml.find(f'.//s:c[@r="{address}"]', NS)
        require(cell is not None, f'Eingabezelle fehlt: {sheet}!{address}')
        require(cell.find('s:f', NS) is None,
                f'Der Test darf keine Formel überschreiben: {sheet}!{address}')
        for child in list(cell):
            if child.tag in {TAG + 'v', TAG + 'is'}:
                cell.remove(child)
        if isinstance(value, str):
            cell.set('t', 'inlineStr')
            ET.SubElement(ET.SubElement(cell, TAG + 'is'), TAG + 't').text = value
        else:
            cell.attrib.pop('t', None)
            ET.SubElement(cell, TAG + 'v').text = str(value)
        parts[paths[sheet]] = ET.tostring(xml, encoding='utf-8', xml_declaration=True)

    formulas = 0
    for filename in paths.values():
        xml = ET.fromstring(parts[filename])
        for cell in xml.findall('.//s:c', NS):
            if cell.find('s:f', NS) is not None:
                formulas += 1
                cached = cell.find('s:v', NS)
                if cached is not None:
                    cell.remove(cached)
                require(cell.find('s:v', NS) is None, 'Formelcache blieb erhalten.')
        parts[filename] = ET.tostring(xml, encoding='utf-8', xml_declaration=True)
    require(formulas > 0, f'Keine Formeln in {source.name} gefunden.')
    xml = ET.fromstring(parts['xl/workbook.xml'])
    settings = xml.find('s:calcPr', NS)
    if settings is None:
        settings = ET.SubElement(xml, TAG + 'calcPr')
    for key, value in {'calcMode': 'auto', 'fullCalcOnLoad': '1', 'forceFullCalc': '1'}.items():
        settings.set(key, value)
    parts['xl/workbook.xml'] = ET.tostring(xml, encoding='utf-8', xml_declaration=True)
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
        for filename, content in parts.items():
            archive.writestr(filename, content)
    return formulas


def read_results(path: Path) -> tuple[dict, dict]:
    parts = load_parts(path)
    strings = []
    if 'xl/sharedStrings.xml' in parts:
        for item in ET.fromstring(parts['xl/sharedStrings.xml']):
            strings.append(''.join(node.text or '' for node in item.iter(TAG + 't')))
    result, errors = {}, {}
    for sheet, filename in sheet_paths(parts).items():
        xml = ET.fromstring(parts[filename])
        for cell in xml.findall('.//s:c', NS):
            kind = cell.get('t')
            cached = cell.find('s:v', NS)
            value = cached.text if cached is not None else ''
            if kind == 's':
                value = strings[int(value)]
            elif kind == 'inlineStr':
                value = ''.join(node.text or '' for node in cell.iter(TAG + 't'))
            elif kind not in {'str', 'e'} and value not in {'', None}:
                value = float(value)
            result[f"{sheet}!{cell.get('r')}"] = value
            if kind == 'e':
                errors.setdefault(sheet, []).append([cell.get('r'), value])
    return result, errors


def find_soffice() -> str:
    requested = os.environ.get('SOFFICE')
    executable = shutil.which(requested) if requested else (
        shutil.which('soffice') or shutil.which('libreoffice')
    )
    require(bool(executable),
            'LibreOffice fehlt. SOFFICE auf die ausführbare Datei setzen oder soffice im PATH bereitstellen.')
    return executable


def run() -> list[dict]:
    soffice = find_soffice()
    original_hashes = {}
    for filename in (EXPENSES, FINANCING):
        source = CASE / filename
        require(source.is_file(), f'Finanzmappe fehlt: {filename}')
        original_hashes[filename] = hashlib.sha256(source.read_bytes()).hexdigest()
    report = []
    with TemporaryDirectory(prefix='schnittflug-finanz-native-') as temporary:
        folder = Path(temporary)
        inputs, outputs = folder / 'inputs', folder / 'outputs'
        inputs.mkdir(); outputs.mkdir()
        prepared = []
        for case in CASES:
            suffix = '-' + case['name'] if case['name'] else ''
            filename = case['source'].replace('.xlsx', suffix + '.xlsx')
            count = create_input(CASE / case['source'], inputs / filename, case.get('change'))
            prepared.append((case, filename, count))
        command = [
            soffice, '-env:UserInstallation=' + (folder / 'lo-profile').as_uri(),
            '--headless', '--convert-to', 'xlsx:Calc MS Excel 2007 XML',
            '--outdir', str(outputs), *[str(inputs / name) for _, name, _ in prepared],
        ]
        completed = subprocess.run(command, text=True, capture_output=True, timeout=180)
        require(completed.returncode == 0,
                f'LibreOffice-Konvertierung fehlgeschlagen (Exit {completed.returncode}).')
        for case, filename, count in prepared:
            output = outputs / filename
            require(output.is_file(), f'LibreOffice hat keine Ergebnisdatei erzeugt: {filename}')
            actual, errors = read_results(output)
            for key, expected in case['expected'].items():
                value = actual.get(key)
                equal = value == expected if isinstance(expected, str) else (
                    isinstance(value, (int, float)) and abs(value - expected) < 0.0000001
                )
                require(equal, f'{filename}, {key}: erwartet {expected!r}, erhalten {value!r}')
            require(errors == case.get('expected_errors', {}),
                    f'Unerwartete Fehlerzellen in {filename}: {errors!r}')
            report.append({
                'file': filename,
                'source_file': case['source'],
                'source_sha256': original_hashes[case['source']],
                'input_change': list(case['change']) if case.get('change') else None,
                'expected': case['expected'],
                'actual': {key: actual[key] for key in case['expected']},
                'status': 'bestanden',
                'errors': errors,
                'formula_caches_removed_before_open': True,
                'formulas_without_cache_before_open': count,
            })
    for filename, expected in original_hashes.items():
        require(hashlib.sha256((CASE / filename).read_bytes()).hexdigest() == expected,
                f'Originaldatei wurde während des Tests verändert: {filename}')
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--report', type=Path, help='Optionaler JSON-Prüfnachweis ohne lokale Pfade.')
    args = parser.parse_args()
    try:
        report = run()
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    except (RuntimeError, OSError, ValueError, KeyError, ET.ParseError,
            zipfile.BadZipFile, subprocess.TimeoutExpired) as error:
        print(f'Finanz-Rechentest fehlgeschlagen: {error}', file=sys.stderr)
        return 1
    print('Schnittflug Finanz: 2 Basismappen und 5 Eingabevarianten in LibreOffice bestanden.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
