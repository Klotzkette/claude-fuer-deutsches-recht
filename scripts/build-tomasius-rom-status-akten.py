#!/usr/bin/env python3
"""Rendert die nativen Nachtragsunterlagen zur Tomasius-Akte."""
from __future__ import annotations

import argparse
import csv
from datetime import date
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'scripts/data/tomasius-rom-status-nachtrag.json'
CASE = {'id': 'HT-2025', 'project': 'Einkommensteuer 2025 · Hubertus Tomasius',
        'message_domain': 'tomasius.example'}
FOLDERS = {'musik': '13_Musikschule_Erwerbsstatus', 'rom': '14_Wohnung_Rom',
           'arbeitsauftrag': '15_Einkommensteuer_Arbeitsauftrag'}
LEDGER_NAME = '11_Objektkonto_LT7_2025'
HEADERS = ['Wertstellung', 'Buchungsbeleg', 'Buchungstext', 'Eingang EUR', 'Ausgang EUR', 'Beleggruppe']


def document_writer():
    path = ROOT / 'scripts/build-projekteinkauf-baubranche-akten.py'
    spec = importlib.util.spec_from_file_location('document_writer', path)
    writer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(writer)
    return writer


def transactions():
    dates = ['01-03', '02-04', '03-04', '04-03', '05-05', '06-04',
             '07-03', '08-04', '09-03', '10-03', '11-04', '12-03']
    payments = [[f'2025-{day}', f'MIETE-{n:02}', 'Oliver Mercer · Miete 620 + Vorschuss 60', 680, 0, 'Miete']
                for n, day in enumerate(dates, 1)]
    expenses = [
        ['02-11', 'VERS-2025', 'Gebäudeversicherung für int. 7', 168, 'Eigentümerkosten'],
        ['03-31', 'NK-2025-1', 'Umlagefähige Hauskosten Quartal 1', 165, 'Mieternebenkosten'],
        ['05-22', 'IDR-2025', 'Reparatur der Wasserleitung', 285, 'Eigentümerkosten'],
        ['06-16', 'IMU-2025-1', 'IMU acconto 2025', 195, 'IMU'],
        ['06-30', 'NK-2025-2', 'Umlagefähige Hauskosten Quartal 2', 165, 'Mieternebenkosten'],
        ['09-30', 'NK-2025-3', 'Umlagefähige Hauskosten Quartal 3', 165, 'Mieternebenkosten'],
        ['11-28', 'F24-2025-1', 'IRPEF acconto 2025 laut Zahlungsauftrag', 360, 'IRPEF-Abschlag'],
        ['12-16', 'IMU-2025-2', 'IMU saldo 2025', 195, 'IMU'],
        ['12-30', 'NK-2025-4', 'Umlagefähige Hauskosten Quartal 4', 165, 'Mieternebenkosten'],
        ['12-30', 'VERW-2025', 'Jahreshonorar der Hausverwaltung', 420, 'Eigentümerkosten'],
        ['12-30', 'CONDO-2025', 'Hauskosten allein zu Lasten des Eigentümers', 186, 'Eigentümerkosten'],
    ]
    payments.extend([f'2025-{day}', ref, label, 0, amount, group] for day, ref, label, amount, group in expenses)
    return sorted(payments, key=lambda row: (date.fromisoformat(row[0]), row[1]))


def workbook_spec(target, entries):
    last = len(entries) + 3
    return {'path': str(target), 'caseId': CASE['id'], 'sheets': [
        {'name': 'Objektkonto', 'title': 'Fremdgeldkonto LT7-2025 · Objektbewegungen',
         'note': 'Anfangssaldo 0,00 EUR. Kaution separat auf LT7-K. Der Saldo ist ein Geldbestand. Steuerliche Zuordnung erfolgt im Arbeitsbogen.',
         'headers': [*HEADERS, 'Saldo EUR'],
         'rows': [[*row, None] for row in entries], 'textColumns': ['A', 'B'],
         'formulas': {f'G{i}': f'=ROUND(SUM(D$4:D{i})-SUM(E$4:E{i}),2)' for i in range(4, last + 1)}},
        {'name': 'Arbeitsbogen', 'title': 'Einkommensteuer 2025 · Belege und offene Zuordnung',
         'note': 'Die ersten drei Zeilen prüfen das Objektkonto. Darunter stehen Belege und freie Felder für die eigene Prüfung.',
         'headers': ['Position', 'Betrag EUR', 'Fundstelle / Beleg', 'Zuordnung / offene Frage'],
         'rows': [
             ['Summe Eingänge', None, 'Objektkonto, Spalte D', None],
             ['Summe Ausgänge', None, 'Objektkonto, Spalte E', None],
             ['Endsaldo', None, 'Objektkonto, Spalte G', None],
             ['Grundmiete und Nebenkosten', None, 'Mietvertrag und Jahresabrechnung', None],
             ['Kaution und Guthaben des Mieters', None, 'Jahresabrechnung und Kautionsbestand', None],
             ['Objektkosten und italienische Steuern', None, 'Abrechnung und Zahlungsbelege', None],
             ['Italienischer Erklärungsstand', None, 'RLI-Vermerk, F24 und E-Mail vom 06.11.', None],
             ['Zurechnung und Erwerbstitel', None, 'Kataster, Nachlassunterlagen, Auskunft', None],
             ['Deutsche Erklärung und Progression', None, 'Arbeitsauftrag und amtliche Fundstellen', None],
         ],
         'formulas': {'B4': f'=SUM(Objektkonto!D4:D{last})', 'B5': f'=SUM(Objektkonto!E4:E{last})',
                      'B6': f'=Objektkonto!G{last}'},
        },
    ]}


def build(target, fonts, node, node_modules, previews):
    writer = document_writer()
    writer.set_fonts(fonts)
    data = json.loads(DATA.read_text(encoding='utf-8'))
    for group, folder in FOLDERS.items():
        directory = target / folder
        directory.mkdir(parents=True, exist_ok=True)
        docs = {doc['filename']: doc for doc in data[group]}
        if len(docs) != len(data[group]) or any(Path(name).name != name for name in docs):
            raise ValueError('Ungültiger Aktenbestand in ' + folder)
        for name, doc in docs.items():
            path = directory / name
            if path.suffix == '.pdf':
                writer.write_pdf(path, doc, CASE)
            elif path.suffix == '.docx':
                writer.write_docx(path, doc, CASE)
            elif path.suffix != '.eml':
                raise ValueError('Unerwartetes Format in ' + name)
        for name, doc in docs.items():
            if name.endswith('.eml'):
                writer.write_eml(directory / name, doc, CASE, directory, docs)

    rom = target / FOLDERS['rom']
    entries = transactions()
    with (rom / f'{LEDGER_NAME}.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        csv.writer(stream, delimiter=';', lineterminator='\n').writerows([HEADERS, *entries])
    spec = workbook_spec(rom / f'{LEDGER_NAME}.xlsx', entries)
    with TemporaryDirectory(prefix='tomasius-rom-xlsx-') as scratch:
        stage = Path(scratch)
        (stage / 'node_modules').symlink_to(node_modules, target_is_directory=True)
        script = stage / 'build.mjs'
        shutil.copyfile(ROOT / 'scripts/build-projekteinkauf-xlsx.mjs', script)
        path = stage / 'workbook.json'
        path.write_text(json.dumps([spec], ensure_ascii=False), encoding='utf-8')
        cmd = [str(node), str(script), str(path)]
        if previews:
            cmd.append(str(previews))
        subprocess.run(cmd, check=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--fonts', type=Path, default=Path('/System/Library/Fonts/Supplemental'))
    parser.add_argument('--node', type=Path, required=True)
    parser.add_argument('--node-modules', type=Path, required=True)
    parser.add_argument('--previews', type=Path)
    args = parser.parse_args()
    build(args.output.resolve(), args.fonts, args.node, args.node_modules, args.previews)
