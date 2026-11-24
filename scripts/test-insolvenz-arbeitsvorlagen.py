#!/usr/bin/env python3
"""Prüft Aktenzuordnung, bearbeitbare Originalvorlagen und Offline-Sammeldownload."""
import hashlib
import importlib
import io
import json
import re
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from docx import Document
from docx.oxml.ns import qn
from docx.shared import Cm
from openpyxl import load_workbook

from testakte_disclaimer import NOTICE_BYTES


build = importlib.import_module("build-insolvenz-arbeitsvorlagen")
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / build.SOURCES
CASE_NAMES = re.compile(r"ChainCortex|Voracis Ventures|Kiezflitzer|Trave Clean|Vondering Metallform|"
                        r"Blechliebe|Domblick Weinkellerei|Weserfunken|Hollmann Bau- und Sanierungs|"
                        r"Großbach Druckguss|Vellnitz Kunststofftechnik", re.I)


def sources():
    for file in sorted((SOURCE / "faelle").glob("*.json")):
        raw = json.loads(file.read_bytes())
        for spec in raw if isinstance(raw, list) else [raw]:
            yield file.stem, spec


def file_path(case, spec):
    return ROOT / "testakten" / case / "Arbeitsvorlagen" / build.filename(spec)


class Arbeitsvorlagen(unittest.TestCase):
    def test_zugeordnete_akten_und_zusaetzlicher_querverweis(self):
        cases = build.case_list(ROOT)
        self.assertEqual(len(cases), 25)
        self.assertEqual(len({name for name, title in cases}), 25)
        self.assertEqual(cases[-1][0], "fintech-darlehen-vertragsuebernahme-bremen")
        actual = {file.stem for file in (SOURCE / "faelle").glob("*.json")}
        self.assertEqual({name for name, _ in cases}, actual)
        common = build.GENERAL + ".docx"
        reference = (ROOT / "testakten" / cases[0][0] / "Arbeitsvorlagen" / common).read_bytes()
        for case, _ in cases:
            with self.subTest(akte=case):
                folder = ROOT / "testakten" / case / "Arbeitsvorlagen"
                expected = {build.filename(spec) for slug, spec in sources() if slug == case}
                self.assertTrue(expected)
                self.assertEqual({f.name for f in folder.iterdir()}, expected | {common})
                self.assertEqual((folder / common).read_bytes(), reference)

    def test_echte_wordtexte_befuellen_und_wieder_oeffnen(self):
        general = json.loads((SOURCE / "asset-deal.json").read_bytes())
        first_case = build.case_list(ROOT)[0][0]
        for case, spec in [(first_case, general), *sources()]:
            if spec.get("format", "docx") != "docx":
                continue
            path = file_path(case, spec)
            with self.subTest(akte=case, datei=path.name):
                doc = Document(path)
                texts = [p.text for p in doc.paragraphs]
                full = "\n".join(texts)
                self.assertNotRegex(full, CASE_NAMES)
                self.assertEqual(texts[:2], [spec["titel"], spec["zweck"]])
                headings = [p.text for p in doc.paragraphs if p.style.name == "Heading 1"]
                self.assertEqual(len(headings), len(spec["abschnitte"]))
                self.assertTrue(all(re.match(r"^\d+", text) for text in headings))
                for index, paragraph in enumerate(doc.paragraphs):
                    if paragraph.style.name == "Heading 1" and paragraph.text.endswith(" Abschluss"):
                        self.assertTrue(doc.paragraphs[index - 1].paragraph_format.keep_with_next)
                for block in spec["abschnitte"]:
                    for paragraph in block.get("absaetze", []):
                        self.assertIn(paragraph, texts)
                self.assertEqual(doc.styles["Normal"].font.name, "Times New Roman")
                self.assertEqual(doc.styles["Normal"].font.size.pt, 11)
                self.assertIsNone(doc.settings.element.find(qn("w:documentProtection")))
                self.assertAlmostEqual(doc.sections[0].page_width / Cm(1), 21.0, places=2)
                self.assertAlmostEqual(doc.sections[0].page_height / Cm(1), 29.7, places=2)
                definitions = [s for s in spec["abschnitte"] if "spalten" in s]
                self.assertEqual(len(definitions), len(doc.tables))
                for table, definition in zip(doc.tables, definitions):
                    self.assertEqual([c.text for c in table.rows[0].cells], definition["spalten"])
                    self.assertEqual(len(table.rows) - 1, definition.get("zeilen", 3))
                    self.assertIsNotNone(table.rows[0]._tr.trPr.find(qn("w:tblHeader")))
                    self.assertTrue(all(not c.text for row in table.rows[1:] for c in row.cells))
                # Befüllbarkeit der echten Datei prüfen, einschließlich Speichern und erneutem Öffnen.
                field = next((r for p in doc.paragraphs for r in p.runs if build.PLACEHOLDER.fullmatch(r.text)), None)
                self.assertIsNotNone(field)
                field.text = "Eingabe aus der Mandatsakte"
                if doc.tables:
                    doc.tables[0].cell(1, 0).text = "Arbeitsstand"
                buffer = io.BytesIO()
                doc.save(buffer)
                saved = Document(buffer)
                self.assertTrue(any("Eingabe aus der Mandatsakte" in p.text for p in saved.paragraphs))
                if doc.tables:
                    self.assertEqual(saved.tables[0].cell(1, 0).text, "Arbeitsstand")

    def test_excel_ist_leer_editierbar_und_formeln_beziehen_sich_auf_die_eingabezeile(self):
        for case, spec in sources():
            if spec.get("format") != "xlsx":
                continue
            with self.subTest(akte=case, datei=spec["slug"]):
                path = file_path(case, spec)
                book = load_workbook(path)
                self.assertEqual(book.sheetnames, [b["titel"] for b in spec["blaetter"]])
                self.assertNotRegex(spec["titel"] + spec["zweck"], CASE_NAMES)
                for sheet, definition in zip(book, spec["blaetter"]):
                    self.assertEqual((sheet["A1"].value, sheet["A2"].value), (spec["titel"], spec["zweck"]))
                    self.assertEqual(sheet.freeze_panes, "A5")
                    self.assertFalse(sheet.protection.sheet)
                    labels = definition["spalten"]
                    self.assertEqual([c.value for c in sheet[4]], labels)
                    self.assertEqual(sheet.max_row, 4 + definition.get("zeilen", 15))
                    formulas, formats = definition.get("formeln", {}), definition.get("formate", {})
                    for row in sheet.iter_rows(min_row=5):
                        for label, cell in zip(labels, row):
                            if label in formulas:
                                self.assertEqual(cell.data_type, "f")
                                self.assertEqual(cell.value, formulas[label].format(r=cell.row))
                            else:
                                self.assertIsNone(cell.value)
                            self.assertEqual(cell.number_format, formats.get(label, "General"))
                    data_column = next(i for i, name in enumerate(labels, 1) if name not in formulas)
                    sheet.cell(5, data_column).value = "Arbeitsstand"
                buffer = io.BytesIO()
                book.save(buffer)
                reopened = load_workbook(buffer)
                for sheet in reopened:
                    self.assertIn("Arbeitsstand", [c.value for c in sheet[5]])

    def test_zip_ist_einzeln_nutzbar_und_pruefsummen_decken_alle_dateien_ab(self):
        common = build.GENERAL + ".docx"
        with ZipFile(ROOT / build.COLLECTION) as archive:
            self.assertIsNone(archive.testzip())
            names = archive.namelist()
            self.assertEqual(names[0], "README.txt")
            self.assertEqual(len(names), len(set(names)))
            readme = archive.read("README.txt")
            self.assertTrue(readme.startswith(NOTICE_BYTES))
            index = readme.decode("utf-8").splitlines()
            self.assertEqual([n for n in names if n.endswith("/" + common)], ["Gemeinsam/" + common])
            expected = {"README.txt", "SHA256SUMS.txt", "Gemeinsam/" + common}
            cases = build.case_list(ROOT)
            self.assertEqual(archive.read("Gemeinsam/" + common), (ROOT / "testakten" / cases[0][0] / "Arbeitsvorlagen" / common).read_bytes())
            for case, spec in sources():
                path = file_path(case, spec)
                name = f"Akten/{case}/{path.name}"
                self.assertIn(name, index)
                self.assertEqual(archive.read(name), path.read_bytes())
                expected.add(name)
            self.assertEqual(set(names), expected)
            checksums = {name: checksum for checksum, name in (line.split("  ", 1) for line in
                         archive.read("SHA256SUMS.txt").decode("utf-8").splitlines())}
            self.assertEqual(set(checksums), expected - {"SHA256SUMS.txt"})
            for name, checksum in checksums.items():
                self.assertEqual(hashlib.sha256(archive.read(name)).hexdigest(), checksum)

    def test_check_erkennt_manipulierte_fehlende_und_fremde_dateien_ohne_zu_schreiben(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            path = Path("testakten/beispiel/Arbeitsvorlagen/vertrag.docx")
            expected = {path: b"Vorlage"}
            with self.assertRaisesRegex(ValueError, "Fehlt"):
                build.publish(root, expected, check=True)
            self.assertFalse((root / path).exists())
            build.publish(root, expected, check=False)
            (root / path).write_bytes(b"Geaendert")
            extra = (root / path).with_name("alter-entwurf.docx")
            extra.write_bytes(b"gefuellt")
            with self.assertRaisesRegex(ValueError, "Unerwartete Vorlage"):
                build.publish(root, expected, check=True)
            self.assertEqual((root / path).read_bytes(), b"Geaendert")
            self.assertEqual(extra.read_bytes(), b"gefuellt")


if __name__ == "__main__":
    unittest.main()
