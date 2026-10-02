#!/usr/bin/env python3
"""Regression gegen veraltete WEG-Originale, Anhänge und Tabellen-Caches.

Liest ausschließlich die vier erzeugten Akten. Kein Office-Neubau und keine
rechtliche Ergebnisbewertung. Die Rubriken bleiben aus dem Arbeitsbestand.
"""
from collections import Counter
from datetime import datetime
from decimal import Decimal
from email import policy
from email.parser import BytesParser
from email.utils import parsedate_to_datetime
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET
import zipfile

from testakte_file_filter import include_in_working_dump
from weg_hausverwaltungsakten_daten import CASES

ROOT = Path(__file__).resolve().parents[1]
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
REL = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id'


def cached_number(path, sheet_name, cell):
    with zipfile.ZipFile(path) as package:
        book = ET.fromstring(package.read('xl/workbook.xml'))
        sheet = next(s for s in book.find('s:sheets', NS) if s.get('name') == sheet_name)
        relations = ET.fromstring(package.read('xl/_rels/workbook.xml.rels'))
        target = next(r.get('Target') for r in relations if r.get('Id') == sheet.get(REL))
        member = target.lstrip('/') if target.startswith('/') else 'xl/' + target
        tree = ET.fromstring(package.read(member))
        node = tree.find(f".//s:c[@r='{cell}']", NS)
        if node is None or node.get('t') in {'e', 's', 'inlineStr'}:
            raise AssertionError(f'{path.name}/{sheet_name}/{cell}: kein numerischer Cache')
        value = node.find('s:v', NS)
        if value is None or value.text is None:
            raise AssertionError(f'{path.name}/{sheet_name}/{cell}: Cache fehlt')
        return Decimal(value.text)


class NativeWegCaseTest(unittest.TestCase):
    def test_originale_anhaenge_und_unabhaengige_rechenkontrollen(self):
        total = Counter()
        for case in CASES:
            folder = ROOT / 'testakten' / case['slug']
            expected = {d['file'] for d in case['documents']}
            actual = {p.name for p in folder.iterdir() if include_in_working_dump(p, folder)}
            with self.subTest(akte=case['slug']):
                self.assertEqual(len(expected), len(case['documents']))
                self.assertEqual(actual, expected)
                self.assertFalse(include_in_working_dump(folder / 'rubric.yaml', folder))
            for item in case['documents']:
                path = folder / item['file']
                total[path.suffix] += 1
                if path.suffix != '.eml':
                    continue
                with self.subTest(nachricht=str(path.relative_to(ROOT))):
                    message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                    self.assertEqual(message['Subject'], item['title'])
                    self.assertEqual(message['From'], item['from'])
                    self.assertEqual(message['To'], item['to'])
                    self.assertEqual(parsedate_to_datetime(message['Date']), datetime.fromisoformat(item['date']))
                    body = message.get_body(preferencelist=('plain',))
                    self.assertIsNotNone(body)
                    self.assertEqual(body.get_content().replace('\r\n', '\n').strip(), item['body'].strip())
                    attachments = list(message.iter_attachments())
                    names = [part.get_filename() for part in attachments]
                    self.assertEqual(names, case.get('attachments', {}).get(path.name, []))
                    for part in attachments:
                        self.assertEqual(part.get_payload(decode=True), (folder / part.get_filename()).read_bytes(), part.get_filename())
        self.assertEqual(total, {'.docx': 80, '.eml': 41, '.txt': 5, '.xlsx': 6})
        # Fachlich unabhängige Kontrollen; diese Werte werden nicht aus den
        # Builder-Erwartungsfeldern übernommen. Sie entdecken alte Formel-Caches.
        checks = [
            ('weg-lindenhof-jahresabrechnung-2025', '03_Eigentuemer_und_Vorschuesse.xlsx', 'Vorschuesse', 'G10', 32000 - 31680),
            ('weg-lindenhof-jahresabrechnung-2025', '05_Buchhaltung_2025.xlsx', 'Betriebskonto', 'E6', 3000 + 31680 - 24360 - 7920),
            ('weg-lindenhof-jahresabrechnung-2025', '05_Buchhaltung_2025.xlsx', 'Ruecklage', 'E4', 40000 + 7920 + 80),
            ('weg-kastanienhof-kellerdiebstahl', '19_Kosten_und_Schaeden.xlsx', 'Private_Meldungen', 'C5', 2299 + 420 + 180),
            ('weg-kastanienhof-kellerdiebstahl', '19_Kosten_und_Schaeden.xlsx', 'Verteilung_Arbeitsblatt', 'D2', Decimal('714') * 80 / 1000),
            ('weg-sonnenwinkel-bettwanzen', '27_Kosten_und_Termine.xlsx', 'Kosten', 'D7', Decimal('714') + Decimal('535.50')),
        ]
        for slug, filename, sheet, cell, expected in checks:
            with self.subTest(kontrolle=f'{slug}/{filename}/{sheet}/{cell}'):
                value = cached_number(ROOT / 'testakten' / slug / filename, sheet, cell)
                self.assertLessEqual(abs(value - Decimal(expected)), Decimal('0.000001'))


if __name__ == '__main__':
    unittest.main()
