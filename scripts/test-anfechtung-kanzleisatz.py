#!/usr/bin/env python3
"""Prüft die native Form der überarbeiteten Rückforderungen und Kölner Schriftsätze."""
import io
import json
from pathlib import Path
import re
import subprocess
import unittest
from docx import Document

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'scripts/data/insolvenzanfechtung-akten.json').read_text())


def check_document(data, item):
    doc = Document(io.BytesIO(data))
    text = '\n\n'.join(p.text for p in doc.paragraphs)
    header = '\n'.join(p.text for p in doc.sections[0].header.paragraphs)
    assert item['letterhead']['firm'] in header, 'Kanzleibriefkopf fehlt'
    assert item['letterhead']['contact'] in header, 'Kanzleikontakt fehlt'
    assert item['to'] in text, 'Empfängeranschrift fehlt'
    assert item['letterhead']['reference'] in text, 'Aktenzeichen fehlt'
    assert item['body'] in text, 'Ausformulierter Text unvollständig'
    assert doc.styles['Normal'].font.name == 'Times New Roman'
    assert doc.styles['Normal'].font.size.pt == 11
    headings = [p.text for p in doc.paragraphs if p.style.name.startswith('Heading')]
    assert headings and all(re.match(r'^\d+(?:\.\d+)* ', h) for h in headings)
    assert not re.search(r'\bper beA\b', text), 'Keine Versandart ohne ausdrückliche Quellenangabe'
    if 'Klageschrift' in item['name']:
        assert 'Luxemburger Straße 101, 50939 Köln' in text
        assert '1.1.1 Zahlung' in headings and '1.1.2 Kosten' in headings
        assert '1.2 Streitwert' in headings
        assert 'Beweis:' in text
    footer = doc.sections[0].footer._element.xml
    assert 'PAGE' in footer


class Kanzleisatz(unittest.TestCase):
    def test_current_originals(self):
        count = 0
        for case in DATA:
            for item in case['files']:
                if not item.get('letterhead'):
                    continue
                with self.subTest(case=case['slug'], document=item['name']):
                    check_document((ROOT / 'testakten' / case['slug'] / item['name']).read_bytes(), item)
                count += 1
        self.assertEqual(count, 5)

    def test_previous_plain_layout_is_rejected(self):
        # Festes Baseline-Objekt; kein Test gegen einen beweglichen HEAD.
        for case in DATA:
            for item in case['files']:
                if not item.get('letterhead'):
                    continue
                path = f"testakten/{case['slug']}/{item['name']}"
                old = subprocess.check_output(['git', 'show', 'baf4b61f1d10e699886f3e51a99eceef3604a41e:' + path], cwd=ROOT)
                with self.subTest(path=path), self.assertRaisesRegex(AssertionError, 'Kanzleibriefkopf fehlt'):
                    check_document(old, item)


if __name__ == '__main__':
    unittest.main()
