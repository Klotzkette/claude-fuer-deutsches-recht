#!/usr/bin/env python3
"""Rendert die fiktive Freiburger Arbeitsakte zum CEO-Fraud."""
from __future__ import annotations

import argparse
import csv
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'scripts/data/freiburg-do-regress.json'
CASE = {
    'id': 'AF-01',
    'slug': 'arbeitsrecht-ceo-fraud-do-regress-freiburg',
    'title': 'Fünf Freigaben · Arbeitnehmerhaftung und D&O in Freiburg',
    'company': 'Dreisamtal Sensorik GmbH',
    'project': 'Dreisamtal Sensorik · Freiburg',
    'message_domain': 'dreisamtal-sensorik.example',
}
WORKBOOK = '35_Zahlungs_und_Deckungsmatrix.xlsx'
JOURNAL = '36_Buchungsjournal_Treasury.csv'
HEADERS = ['Buchung', 'Tag', 'Ausgang EUR', 'Rückfluss EUR']
PAYMENTS = [
    ('T01', '2026-09-14', 480000, 300000),
    ('T02', '2026-09-15', 920000, 0),
    ('T03', '2026-09-16', 1550000, 450000),
    ('T04', '2026-09-17', 1700000, 0),
    ('T05', '2026-09-18', 1850000, 250000),
]


def load_case():
    payload = json.loads(DATA.read_text(encoding='utf-8'))
    return {**CASE, 'documents': payload['documents']}


def document_writer():
    path = ROOT / 'scripts/build-projekteinkauf-baubranche-akten.py'
    spec = importlib.util.spec_from_file_location('do_case_writer', path)
    writer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(writer)
    return writer


def workbook_spec(path):
    payment_rows = [[*row, None] for row in PAYMENTS] + [['Gesamt', None, None, None, None]]
    formulas = {f'E{i}': f'=C{i}-D{i}' for i in range(4, 9)}
    formulas.update({f'{column}9': f'=SUM({column}4:{column}8)' for column in 'CDE'})
    return {'path': str(path), 'caseId': CASE['id'], 'sheets': [
        {'name': 'Zahlungen', 'title': 'Treasury · Überweisungen und Rückflüsse',
         'note': 'Buchungen T01 bis T05. Rückflüsse sind einzelnen Ausgangsbuchungen zugeordnet. Die Differenz enthält keine Haftungsquote.',
         'headers': [*HEADERS, 'Saldo EUR'], 'rows': payment_rows,
         'textColumns': ['A', 'B'], 'formulas': formulas},
        {'name': 'D&O', 'title': 'Deckungsrechnung · Stand 6. November 2026',
         'note': 'Zeilen 8 und 9 sind Eingaben für ein Szenario. Der rechnerische Rest ist keine Deckungszusage.',
         'headers': ['Position', 'Betrag EUR', 'Quelle / Einordnung'],
         'rows': [
             ['Jahresaggregat', 4000000, '16 Versicherungsschein und 22 Aggregatkonto'],
             ['Andere Angelegenheit', 750000, '22 tatsächlich gezahlte Entschädigung'],
             ['Abwehrkosten dieses Falls', 120000, '21/22 bezahlt und vorläufig belastet'],
             ['Rechnerischer Rest', None, 'Vor weiteren Belastungen oder Korrekturen'],
             ['Unterstellte Regresshaftung', None, 'Eingabe ohne Zinsen und Kosten'],
             ['Unterstellte Versicherungsleistung', None, 'Eingabe bei angenommenem Schutz'],
             ['Verbleibender persönlicher Betrag', None, 'Nur bei zwei schlüssigen Eingaben'],
         ],
         'formulas': {'B7': '=B4-B5-B6',
                      'B10': '=IF(COUNT(B8:B9)=2,IF(AND(B8>=0,B9>=0,B9<=B7,B9<=B8,B8<=Zahlungen!E9),B8-B9,""),"")'}},
        {'name': 'Beweiszuordnung', 'title': 'Arbeitstabelle · Haftung je Zahlung',
         'note': 'Tragen Sie Belegstellen und die Tatsachen für die einzelnen Zahlungen ein. Prüfen Sie die Deckung auf dem gesonderten Blatt.',
         'headers': ['Buchung', 'Pflicht und Freigabe', 'Kenntnisstand', 'Mitverursachung', 'Beweisangebot'],
         'rows': [[row[0], None, None, None, None] for row in PAYMENTS]},
    ]}


def build(output, fonts, node, node_modules, previews):
    case = load_case()
    writer = document_writer()
    font_paths = writer.set_fonts(fonts)
    output.mkdir(parents=True, exist_ok=True)
    names = {record['filename']: record for record in case['documents']}
    if len(names) != len(case['documents']) or any(Path(name).name != name for name in names):
        raise ValueError('Doppelte oder ungültige Aktenstücknamen')
    for name, doc in names.items():
        path = output / name
        if path.suffix == '.pdf':
            writer.write_pdf(path, doc, case)
        elif path.suffix == '.docx':
            writer.write_docx(path, doc, case)
        elif path.suffix == '.png':
            writer.write_png(path, doc, font_paths)
        elif path.suffix != '.eml' and name not in {WORKBOOK, JOURNAL}:
            raise ValueError('Unerwartetes Aktenformat: ' + name)
    with (output / JOURNAL).open('w', encoding='utf-8-sig', newline='') as stream:
        csv.writer(stream, delimiter=';', lineterminator='\n').writerows([HEADERS, *PAYMENTS])
    for name, doc in names.items():
        if name.endswith('.eml'):
            writer.write_eml(output / name, doc, case, output, names)
    with TemporaryDirectory(prefix='freiburg-do-xlsx-') as scratch:
        stage = Path(scratch)
        (stage / 'node_modules').symlink_to(node_modules, target_is_directory=True)
        builder = stage / 'build.mjs'
        shutil.copyfile(ROOT / 'scripts/build-projekteinkauf-xlsx.mjs', builder)
        spec = stage / 'workbook.json'
        spec.write_text(json.dumps([workbook_spec(output / WORKBOOK)], ensure_ascii=False), encoding='utf-8')
        command = [str(node), str(builder), str(spec)]
        if previews:
            command.append(str(previews))
        subprocess.run(command, check=True)
    payload = json.loads(DATA.read_text(encoding='utf-8'))
    writer.write_pdf(output.parent / 'AF-01_Nachbesprechung.pdf', {
        **payload['debrief'], 'issuer': 'Schulungsleitung · Arbeitsrecht', 'date': '2026-11-09',
    }, case)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--node', type=Path, required=True)
    parser.add_argument('--node-modules', type=Path, required=True)
    parser.add_argument('--fonts', type=Path, default=Path('/System/Library/Fonts/Supplemental'))
    parser.add_argument('--previews', type=Path)
    args = parser.parse_args()
    build(args.output.resolve(), args.fonts, args.node, args.node_modules, args.previews)
