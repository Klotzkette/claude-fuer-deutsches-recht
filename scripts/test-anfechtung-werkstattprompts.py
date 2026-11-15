#!/usr/bin/env python3
"""Prüft echte Werkstattexporte und gezielte Manipulationen trotz neuer Hashwerte.

Die Positivprobe liest die gebauten Dateien; Negativproben arbeiten ausschließlich
in temporären Kopien. Sie erzeugen keine Ersatz-Werkstätten und setzen keine
Prüfgrenze herab. Aufruf nach build-anfechtung-werkstattprompts.py.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import io
import json
from pathlib import Path
import re
import tempfile
import unittest
import warnings
import zipfile

from pypdf import PdfReader, PdfWriter
from pypdf.generic import ContentStream, NameObject, TextStringObject

from anfechtung_werkstatt_contract import EVIDENCE, validate_exports


ROOT = Path(__file__).resolve().parents[1]
EXPORTS = ROOT / 'docs/werkstattprompts/insolvenzanfechtung'
PROOF = ROOT / EVIDENCE
ARCHIVE_NAME = 'insolvenzanfechtung-tatbestandswerkstaetten.zip'
HANDBOOK_NAME = 'insolvenzanfechtung-tatbestandswerkstaetten.pdf'


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rewrite_text_operator(data: bytes, *, footer: bool = False) -> bytes:
    """Ändert echten sichtbaren PDF-Text; Seitenzahl und Schrift bleiben erhalten."""
    reader = PdfReader(io.BytesIO(data))
    writer = PdfWriter(clone_from=reader)
    page = writer.pages[0]
    content = ContentStream(page.get_contents(), writer)
    seen_text = 0
    replaced = False
    for operands, operator in content.operations:
        if operator != b'Tj' or not operands:
            continue
        value = str(operands[0])
        seen_text += 1
        # Die ersten drei Textoperationen sind Überschrift, Quellenstand, Seite.
        if footer:
            if 'Quellenpr' not in value:
                continue
            new_value = value.replace('2026', '1999', 1)
        elif seen_text > 3 and re.search(r'[A-Za-z]{4}', value):
            new_value = re.sub(r'[A-Za-z]', 'X', value, count=1)
        else:
            continue
        if new_value == value:
            continue
        operands[0] = TextStringObject(new_value)
        replaced = True
        break
    if not replaced:
        raise AssertionError('Keine geeignete echte Textoperation im generierten PDF gefunden')
    page.replace_contents(content)
    output = io.BytesIO()
    writer.write(output)
    changed = output.getvalue()
    assert len(PdfReader(io.BytesIO(changed)).pages) == len(reader.pages)
    assert PdfReader(io.BytesIO(changed)).pages[0].extract_text() != PdfReader(io.BytesIO(data)).pages[0].extract_text()
    return changed


class ExportContractTests(unittest.TestCase):
    """Beobachtbares Exportverhalten statt Wiederholung der Prüfimplementierung."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.proof_bytes = PROOF.read_bytes()
        cls.original_report = json.loads(cls.proof_bytes)
        cls.archive_bytes = (EXPORTS / ARCHIVE_NAME).read_bytes()
        cls.handbook_bytes = (EXPORTS / HANDBOOK_NAME).read_bytes()
        with zipfile.ZipFile(io.BytesIO(cls.archive_bytes)) as archive:
            cls.original_members = {name: archive.read(name) for name in archive.namelist()}
        cls.sources = {
            row['source']: (ROOT / row['source']).read_bytes()
            for row in cls.original_report['modules']
        }

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix='anfechtung-export-test-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.report = copy.deepcopy(self.original_report)
        self.members = dict(self.original_members)
        for source, data in self.sources.items():
            path = self.root / source
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        self.proof = self.root / 'umfang.json'
        self.archive = self.root / ARCHIVE_NAME
        self.handbook = self.root / HANDBOOK_NAME
        self.handbook.write_bytes(self.handbook_bytes)
        self.row = self.report['modules'][0]
        self.source_name = Path(self.row['source']).name
        self.pdf_member = 'PDF/' + self.row['pdf']

    def write_candidate(self, *, duplicate: str | None = None) -> None:
        evidence = (json.dumps(self.report, ensure_ascii=False, indent=2) + '\n').encode()
        self.proof.write_bytes(evidence)
        self.members['umfang.json'] = evidence
        with zipfile.ZipFile(self.archive, 'w', compression=zipfile.ZIP_DEFLATED) as z:
            for name, data in self.members.items():
                z.writestr(name, data)
            if duplicate:
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore', UserWarning)
                    z.writestr(duplicate, self.members[duplicate])

    def validate(self) -> dict:
        return validate_exports(self.root, self.proof, self.archive, self.handbook)

    def replace_source_and_refresh(self, data: bytes) -> None:
        """Auch MD/TXT und Bericht ändern: ein bloßer Hashvergleich darf nicht genügen."""
        (self.root / self.row['source']).write_bytes(data)
        self.members['Markdown/' + self.source_name] = data
        self.members['Text/' + Path(self.source_name).with_suffix('.txt').name] = data
        self.row.update(source_sha256=digest(data), utf8_bytes=len(data), words=len(data.decode().split()))

    def test_original_generated_exports(self) -> None:
        # Originale bytegenau nutzen, nicht zuvor neu schreiben.
        self.proof.write_bytes(self.proof_bytes)
        self.archive.write_bytes(self.archive_bytes)
        result = self.validate()
        self.assertEqual(result['module_count'], 10)
        self.assertEqual(result['pages'], len(PdfReader(io.BytesIO(self.handbook_bytes)).pages))

    def test_changed_source_with_refreshed_hash_and_matching_md_txt(self) -> None:
        source = (self.root / self.row['source']).read_text()
        old = re.search(r'[A-Za-zÄÖÜäöüß]{8,}', source)
        self.assertIsNotNone(old)
        revised = source[:old.start()] + 'FALSCHBEHAUPTUNG' + source[old.end():]
        self.replace_source_and_refresh(revised.encode())
        self.write_candidate()
        with self.assertRaisesRegex(ValueError, 'PDF enthält nicht'):
            self.validate()

    def test_changed_pdf_body_with_refreshed_hash(self) -> None:
        modified = rewrite_text_operator(self.members[self.pdf_member])
        self.members[self.pdf_member] = modified
        self.row['pdf_sha256'] = digest(modified)
        self.write_candidate()
        with self.assertRaisesRegex(ValueError, 'PDF enthält nicht'):
            self.validate()

    def test_changed_pdf_amount_punctuation_with_refreshed_hash(self) -> None:
        reader = PdfReader(io.BytesIO(self.members[self.pdf_member]))
        writer = PdfWriter(clone_from=reader)
        amount = re.compile(r'(\d{1,3})\.(\d{3})(?=\s+(?:Euro|EUR))')
        replaced = None
        for page in writer.pages:
            content = ContentStream(page.get_contents(), writer)
            for operands, operator in content.operations:
                if operator != b'Tj' or not operands:
                    continue
                value = str(operands[0])
                match = amount.search(value)
                if not match:
                    continue
                digits = match.group(1) + match.group(2)
                changed_amount = digits[:-2] + ',' + digits[-2:]
                new_value = value[:match.start()] + changed_amount + value[match.end():]
                operands[0] = TextStringObject(new_value)
                replaced = changed_amount
                break
            if replaced:
                page.replace_contents(content)
                break
        self.assertIsNotNone(replaced, 'Ein echter Eurobetrag wird für diese Manipulationsprobe benötigt')
        output = io.BytesIO()
        writer.write(output)
        modified = output.getvalue()
        self.assertIn(replaced, ''.join(page.extract_text() or '' for page in PdfReader(io.BytesIO(modified)).pages))
        self.members[self.pdf_member] = modified
        self.row['pdf_sha256'] = digest(modified)
        self.write_candidate()
        # Ziffernfolge identisch, Betrag aber Faktor 100 kleiner: 18.000 -> 180,00.
        with self.assertRaisesRegex(ValueError, 'PDF enthält nicht'):
            self.validate()

    def test_changed_hyperlink_target_with_refreshed_source_hash(self) -> None:
        source = (self.root / self.row['source']).read_text()
        target = re.search(r'\]\((https://[^)]+)\)', source)
        self.assertIsNotNone(target)
        revised = source[:target.start(1)] + 'https://example.invalid/falsche-rechtsprechung' + source[target.end(1):]
        self.replace_source_and_refresh(revised.encode())
        self.write_candidate()
        with self.assertRaisesRegex(ValueError, 'Link|Verweis|Quelle|Ziel|Annotation'):
            self.validate()

    def test_missing_module_member(self) -> None:
        self.members.pop(self.pdf_member)
        self.write_candidate()
        with self.assertRaisesRegex(ValueError, 'fehlende'):
            self.validate()

    def test_changed_pdf_link_target_with_refreshed_hash(self) -> None:
        reader = PdfReader(io.BytesIO(self.members[self.pdf_member]))
        changed = False
        for page in reader.pages:
            for reference in page.get('/Annots', []):
                annotation = reference.get_object()
                action = annotation.get('/A')
                if action is not None and action.get_object().get('/S') == '/URI':
                    action.get_object()[NameObject('/URI')] = TextStringObject('https://example.invalid/falsches-pdf-linkziel')
                    changed = True
                    break
            if changed:
                break
        self.assertTrue(changed, 'Echte generierte PDF muss Quellenlinks enthalten')
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        output = io.BytesIO()
        writer.write(output)
        modified = output.getvalue()
        self.members[self.pdf_member] = modified
        self.row['pdf_sha256'] = digest(modified)
        self.write_candidate()
        with self.assertRaisesRegex(ValueError, 'PDF-Linkziele'):
            self.validate()

    def test_duplicate_module_member(self) -> None:
        self.write_candidate(duplicate=self.pdf_member)
        with self.assertRaisesRegex(ValueError, 'doppelte'):
            self.validate()

    def test_truncated_pdf_with_refreshed_hash_and_page_count(self) -> None:
        original = PdfReader(io.BytesIO(self.members[self.pdf_member]))
        writer = PdfWriter()
        for page in original.pages[:-1]:
            writer.add_page(page)
        output = io.BytesIO()
        writer.write(output)
        modified = output.getvalue()
        self.members[self.pdf_member] = modified
        self.row.update(pdf_sha256=digest(modified), pages=len(original.pages) - 1)
        self.report['pages'] -= 1
        self.write_candidate()
        with self.assertRaisesRegex(ValueError, 'PDF.*(enthält nicht|Seitenumfang)'):
            self.validate()

    def test_false_word_count_in_evidence_and_zip(self) -> None:
        self.row['words'] += 123
        self.write_candidate()
        with self.assertRaisesRegex(ValueError, 'Wörtern'):
            self.validate()

    def test_false_page_count_in_evidence_and_zip(self) -> None:
        self.row['pages'] += 1
        self.report['pages'] += 1
        self.write_candidate()
        with self.assertRaisesRegex(ValueError, 'Seitenumfang'):
            self.validate()

    def test_changed_handbook_with_refreshed_hash(self) -> None:
        modified = rewrite_text_operator(self.handbook_bytes)
        self.handbook.write_bytes(modified)
        self.report['handbook_sha256'] = digest(modified)
        self.write_candidate()
        with self.assertRaisesRegex(ValueError, 'Sammel-PDF.*verändert'):
            self.validate()

    def test_handbook_footer_with_wrong_source_date_despite_refreshed_hash(self) -> None:
        modified = rewrite_text_operator(self.handbook_bytes, footer=True)
        self.handbook.write_bytes(modified)
        self.report['handbook_sha256'] = digest(modified)
        self.write_candidate()
        with self.assertRaisesRegex(ValueError, 'Sammel-PDF|Fuß|Quellen|Kopf'):
            self.validate()

    def test_unexpected_archive_member(self) -> None:
        self.members['unbeabsichtigte-datei.txt'] = b'Nicht Teil des freigegebenen Pakets.'
        self.write_candidate()
        with self.assertRaisesRegex(ValueError, 'zusätzliche'):
            self.validate()


def main() -> None:
    global EXPORTS, PROOF
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exports', type=Path, default=EXPORTS)
    parser.add_argument('--proof', type=Path, default=PROOF)
    args = parser.parse_args()
    EXPORTS, PROOF = args.exports.resolve(), args.proof.resolve()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ExportContractTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(not result.wasSuccessful())


if __name__ == '__main__':
    main()
