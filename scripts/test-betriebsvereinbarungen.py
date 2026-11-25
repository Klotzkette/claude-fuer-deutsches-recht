#!/usr/bin/env python3
"""Abnahme der tatsächlich ausgelieferten Copilot-Verhandlungsakte und Arbeitsvorlagen."""
import io
import json
import unittest
from email import policy
from email.parser import BytesParser
from importlib import import_module
from zipfile import ZipFile

from docx import Document
from openpyxl import load_workbook
from pypdf import PdfReader

from testakte_disclaimer import NOTICE_BYTES, NOTICE_FILENAME
from testakte_einzelpdf_common import document_arcname_pairs
from testakte_zip_common import editable_working_forms, working_dump_archive_pairs

build = import_module("build-betriebsvereinbarungen")
case = build.ROOT / "testakten" / build.CASE


class BetriebsvereinbarungenTest(unittest.TestCase):
    def test_native_ordner_und_getrennte_arbeitsvorlagen(self):
        expected = working_dump_archive_pairs(case, include_gesamt_pdf=False) + editable_working_forms(case)
        with ZipFile(build.DOWNLOADS / ("testakte-" + build.CASE + ".zip")) as archive:
            names = archive.namelist()
            self.assertEqual(names[0], NOTICE_FILENAME)
            self.assertTrue(archive.read(NOTICE_FILENAME).startswith(NOTICE_BYTES))
            self.assertEqual(set(names[1:]), {name for _, name in expected})
            for path, name in expected:
                self.assertEqual(archive.read(name), path.read_bytes())
            self.assertEqual([sum(n.startswith(p + "/") for n in names) for p in (*build.PHASES, "Arbeitsvorlagen")], [8, 8, 3])
            for name in [n for n in names if n.endswith(".eml")]:
                mail = BytesParser(policy=policy.default).parsebytes(archive.read(name))
                self.assertIsNotNone(mail["Date"])
                self.assertTrue(mail.get_body(preferencelist=("plain",)).get_content().strip())

    def test_lesefassungen_enthalten_dieselben_aktenstuecke_in_reihenfolge(self):
        expected = [name for _, name in document_arcname_pairs(case)]
        output = build.DOWNLOADS / ("testakte-" + build.CASE + "-einzelpdfs.zip")
        with ZipFile(output) as archive:
            self.assertEqual(archive.namelist(), [NOTICE_FILENAME, *expected])
            self.assertTrue(archive.read(NOTICE_FILENAME).startswith(NOTICE_BYTES))
            texts = []
            for name in expected:
                texts.extend(pg.extract_text() for pg in PdfReader(io.BytesIO(archive.read(name))).pages)
            combined = PdfReader(case / "gesamt-pdf" / (build.CASE + "_gesamt.pdf"))
            self.assertEqual([pg.extract_text() for pg in combined.pages], texts)
            self.assertEqual(len(expected), 16)
            self.assertTrue(all(s and "Diese Testakte wurde mit KI generiert" not in s for s in texts))
            self.assertTrue(any("3,5 Tage" in s and "4.480" in s for s in texts))
            self.assertTrue(any("Copilot Chat" in s and "Zusatzlizenz" in s for s in texts))

    def test_installierbare_skills_und_ausfuellbare_office_dateien(self):
        with ZipFile(build.DOWNLOADS / (build.PLUGIN + ".zip")) as archive:
            for manifest in ["plugin.json", ".claude-plugin/plugin.json", ".codex-plugin/plugin.json"]:
                self.assertEqual(json.loads(archive.read(manifest))["name"], build.PLUGIN)
            self.assertEqual(sum(n.endswith("/SKILL.md") for n in archive.namelist()), 10)
            self.assertFalse(any(n.endswith(("-schnellstart.md", "-werkstatt.md")) for n in archive.namelist()
                                 if n.count("/") == 0))
            for path in sorted((case / "Arbeitsvorlagen").iterdir()):
                self.assertEqual(archive.read("vorlagen/" + path.name), path.read_bytes())
                result = io.BytesIO()
                if path.suffix == ".docx":
                    doc = Document(path)
                    field = next(p for p in doc.paragraphs if "[" in p.text)
                    field.text = "Verhandlungsfassung zur gemeinsamen Prüfung"
                    doc.save(result)
                    self.assertIn(field.text, [p.text for p in Document(result).paragraphs])
                else:
                    book = load_workbook(path)
                    self.assertEqual(len(book.sheetnames), 3)
                    self.assertTrue(all(all(cell.value is None for cell in sheet[5]) for sheet in book))
                    book.worksheets[0]["A5"] = "Rollenprüfung vereinbart"
                    book.save(result)
                    self.assertEqual(load_workbook(result).worksheets[0]["A5"].value, "Rollenprüfung vereinbart")


if __name__ == "__main__":
    unittest.main()
