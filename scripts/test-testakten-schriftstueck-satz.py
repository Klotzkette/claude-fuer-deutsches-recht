#!/usr/bin/env python3
"""Prüft Zeichenerhalt, Bearbeitbarkeit, Folgeseiten und reproduzierbare Aktenpost."""

import unittest
from io import BytesIO
from zipfile import ZipFile

from docx import Document
from docx.oxml.ns import qn
from pypdf import PdfReader

from testakten_schriftstueck_satz import render_pair


class SchriftstueckTest(unittest.TestCase):
    def test_korrespondenz(self):
        body = "Prüfung ≥ 3, Überweisung → Łódź, Maß CO₂. Nguyễn & Tanrıöver. 🙈 👍"
        case = dict(kind="brief", sender="Rechtsamt", recipient="Frau Nguyễn\nGeschäftsstelle",
                    reference="WA-482", title="Rückfrage zum Zahlungseingang", intro=body,
                    fields=["Welche Gutschrift gehört zur Zahlung?"])
        word, pdf = render_pair(case)
        self.assertEqual((word, pdf), render_pair(case))
        doc = Document(BytesIO(word))
        self.assertIs(doc.styles["Text"].font.italic, False)
        self.assertIn(body, [p.text for p in doc.paragraphs])
        self.assertIn("Frau Nguyễn\nGeschäftsstelle", [p.text for p in doc.paragraphs])
        self.assertEqual(doc.core_properties.modified.year, 2000)
        with ZipFile(BytesIO(word)) as archive:
            footers = [n for n in archive.namelist() if n.startswith("word/footer")]
            self.assertEqual(len(footers), 2)
            for name in footers:
                self.assertIn(b'w:instr="PAGE"', archive.read(name))
        reader = PdfReader(BytesIO(pdf))
        self.assertEqual(len(reader.pages), 1)
        text = reader.pages[0].extract_text()
        self.assertIn(body, text)
        self.assertIn("Welche Gutschrift gehört zur Zahlung?", text)
        self.assertNotIn("■", text)

    def test_tabellenumbruch(self):
        header = ["Vorgang", "Fachlicher Bezug"]
        entries = [[f"Posten-{i:03}", f"Abgleich des Vorgangs {i}"] for i in range(90)]
        case = dict(kind="protokoll", sender="Sitzungsdienst", title="Belegabgleich",
                    sections=[dict(heading="Eingänge", table=dict(headers=header, rows=entries))])
        word, pdf = render_pair(case)
        table = Document(BytesIO(word)).tables[0]
        self.assertEqual(len(table.rows), len(entries) + 1)
        self.assertIsNotNone(table.rows[0]._tr.trPr.find(qn("w:tblHeader")))
        self.assertEqual([c.text for c in table.rows[-1].cells], entries[-1])
        text = [p.extract_text() for p in PdfReader(BytesIO(pdf)).pages]
        self.assertGreater(len(text), 1)
        self.assertIn(entries[0][0], text[0])
        for i, page in enumerate(text, 1):
            self.assertIn(f"Seite {i}", page)
            self.assertIn(header[1], page)
        all_pages = "\n".join(text)
        for key, _ in entries:
            self.assertEqual(all_pages.count(key), 1)

    def test_mehrseitiger_auszug(self):
        paragraphs = [f"Sachverhalt {i:03}. " + "Die Leistungsmenge ist zu belegen. " * 12
                      for i in range(15)]
        case = dict(kind="vermerk", sender="Vergabestelle", title="Aufmaß prüfen",
                    evidence=[dict(title="Baustellenprotokoll", source="Anlage 2",
                                   text="\n".join(paragraphs))])
        word, pdf = render_pair(case)
        self.assertTrue(any(p.text.startswith(paragraphs[0]) for p in Document(BytesIO(word)).paragraphs))
        pages = PdfReader(BytesIO(pdf)).pages
        self.assertGreater(len(pages), 1)
        text = "\n".join(p.extract_text() for p in pages)
        for i in range(15):
            self.assertEqual(text.count(f"Sachverhalt {i:03}."), 1)


if __name__ == "__main__":
    unittest.main()
