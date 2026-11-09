#!/usr/bin/env python3
"""Erstellt die Originalunterlagen der Bremer Kontorwerft-Akte."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
from tempfile import TemporaryDirectory

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SLUG = 'gesellschaftsrecht-egbr-grundbuch-register-bremen'
SOURCE = ROOT / 'scripts/data/egbr-grundbuch-bremen.json'
CASE = {
    'slug': SLUG,
    'id': 'GR-01',
    'title': 'Zwei Blätter, ein falscher Name · Kontorwerft eGbR',
    'company': 'Kontorwerft eGbR',
    'project': 'Kontorwerft · Bremen-Walle',
    'message_domain': 'kontorwerft.example',
}
MAP = '33_Flurstueckskizze_Kontorwerft.png'
WORKBOOK = '32_Register_und_Ereignisakte.xlsx'


def load_case():
    payload = json.loads(SOURCE.read_text(encoding='utf-8'))
    return {**CASE, 'documents': payload['documents']}


def load_script():
    path = ROOT / 'scripts/build-projekteinkauf-baubranche-akten.py'
    spec = importlib.util.spec_from_file_location('case_writer', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def plot_sketch(path, fonts):
    width, height = 1280, 780
    image = Image.new('RGB', (width, height), '#FAF8F3')
    d = ImageDraw.Draw(image)
    normal, bold = fonts[:2]
    def label(xy, value, size=26, *, heading=False, color='#182F36'):
        font = ImageFont.truetype(str(bold if heading else normal), size)
        d.text(xy, value, font=font, fill=color)

    d.rectangle((0, 0, width, 132), fill='#173D42')
    label((58, 27), 'WESERANKER   |   PROJEKTENTWICKLUNG', 24, heading=True, color='#B5D6CC')
    label((58, 63), 'Lageskizze zum Grundstückspaket', 37, heading=True, color='white')
    label((60, 162), 'Bremen-Walle   ·   Flur 17   ·   Arbeitsstand vom 10. Juni 2026', 25)
    d.rounded_rectangle((62, 230, 1218, 635), radius=16, outline='#97A7A6', width=2, fill='#EFF3F1')
    d.rectangle((144, 300, 634, 560), outline='#2E6863', width=4, fill='#D0E5DD')
    d.rectangle((634, 300, 1134, 560), outline='#9E6047', width=4, fill='#F0DCD0')
    for x, text, sheet, color in [(180, '413/6', 'Grundbuchblatt 9104', '#245752'),
                                  (670, '413/9', 'Grundbuchblatt 9109', '#7E4531')]:
        label((x, 336), 'FLURSTÜCK', 23, heading=True, color=color)
        label((x, 378), text, 60, heading=True, color=color)
        label((x, 467), sheet, 27, color=color)
    label((66, 674), 'Interne Übersicht zu den beiden getrennt geführten Blättern.', 25)
    label((66, 711), 'Schematisch und ohne Maßstab. Eigentümerangaben ergeben sich aus den jeweiligen Unterlagen.', 23)
    image.save(path)


def workbook_spec(path, payload):
    records = sorted((doc for doc in payload['documents'] if doc['filename'][:2].isdigit()
                      and 1 <= int(doc['filename'][:2]) <= 30 and doc.get('date')),
                     key=lambda doc: (doc['date'], doc['filename']))
    return {'caseId': CASE['id'], 'path': str(path), 'sheets': [
        {'name': 'Dokumente', 'title': 'Kontorwerft · Dokumentenregister',
         'note': 'Die Dokumentdaten geben den jeweiligen Belegstand wieder. Maßgebliche Zeitpunkte sind im Dokument selbst zu prüfen.',
         'headers': ['Dokumentdatum', 'Aktenstück', 'Betreff / Bezeichnung'],
         'textColumns': ['A'],
         'rows': [[doc['date'][:10], doc['filename'], doc.get('title') or doc['subject']] for doc in records]},
        {'name': 'Erwerbsmatrix', 'title': 'Kontorwerft · Prüfstand pro Flurstück',
         'note': 'Führen Sie 413/6 und 413/9 getrennt. Tragen Sie Zeitpunkt, Aktenfundstelle und Schlussfolgerung erst nach der Prüfung ein.',
         'headers': ['Prüfschritt', '413/6 · Blatt 9104', '413/9 · Blatt 9109', 'Zeitpunkt / Beleg', 'Restfrage'],
         'rows': [[label, None, None, None, None] for label in (
             'Identität der Gesellschaft', 'Vertragslage und Vertretung', 'Vertretung im Gesellschaftsregister',
             'Dingliche Einigung', 'Eigentümer vor dem Antrag', 'Inhalt des Grundbuchs', 'Antrag auf Umschreibung',
             'Kenntnis der Erwerberin', 'Widerspruch im Grundbuch', 'Eintragung der Erwerberin',
             'Berichtigung, Sicherung, weiterer Nachweis',
         )]},
    ]}


def build(target, node, node_modules, fonts, previews):
    case = load_case()
    payload = json.loads(SOURCE.read_text(encoding='utf-8'))
    writer = load_script()
    font_paths = writer.set_fonts(fonts)
    target.mkdir(parents=True, exist_ok=True)
    names = {record['filename']: record for record in case['documents']}
    if len(names) != len(case['documents']) or any(Path(name).name != name for name in names):
        raise ValueError('Doppelte oder ungültige Aktenstücknamen.')
    for name, record in names.items():
        path = target / name
        if path.suffix == '.pdf':
            writer.write_pdf(path, record, case)
        elif path.suffix == '.docx':
            writer.write_docx(path, record, case)
        elif path.suffix != '.eml' and name not in {MAP, WORKBOOK}:
            raise ValueError('Unerwartetes Aktenformat: ' + name)
    plot_sketch(target / MAP, font_paths)
    for name, record in names.items():
        if name.endswith('.eml'):
            writer.write_eml(target / name, record, case, target, names)

    with TemporaryDirectory(prefix='egbr-workbook-') as scratch:
        stage = Path(scratch)
        (stage / 'node_modules').symlink_to(node_modules, target_is_directory=True)
        builder = stage / 'build.mjs'
        shutil.copyfile(ROOT / 'scripts/build-projekteinkauf-xlsx.mjs', builder)
        spec = stage / 'workbook.json'
        spec.write_text(json.dumps([workbook_spec(target / WORKBOOK, payload)], ensure_ascii=False), encoding='utf-8')
        command = [str(node), str(builder), str(spec)]
        if previews:
            command.append(str(previews))
        subprocess.run(command, check=True)
    debrief = target.parent / 'GR-01_Nachbesprechung.pdf'
    writer.write_pdf(debrief, {**payload['debrief'], 'issuer': 'Schulungsleitung · Gesellschaftsrecht',
                               'date': '2026-07-13'}, case)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--node', type=Path, required=True)
    parser.add_argument('--node-modules', type=Path, required=True)
    parser.add_argument('--fonts', type=Path, default=Path('/System/Library/Fonts/Supplemental'))
    parser.add_argument('--previews', type=Path)
    args = parser.parse_args()
    build(args.output.resolve(), args.node, args.node_modules, args.fonts, args.previews)
