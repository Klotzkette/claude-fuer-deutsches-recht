#!/usr/bin/env python3
"""Prüft Textabdeckung, Lesbarkeit und engen Geltungsbereich der AML-PDFs."""

from __future__ import annotations

from collections import Counter
from datetime import date, datetime
import hashlib
import io
from pathlib import Path
import re
import shutil
import tempfile
import unittest
from unittest.mock import patch
import zipfile
import xml.etree.ElementTree as ET

import openpyxl
import pdfplumber

import aml_fallregister_pdf as aml
import testakte_office_pdf as office

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [ROOT / "testakten" / case / "04_Tabellen/Fallregister.xlsx" for case in sorted(aml.CASES)]


def compact(text):
    return re.sub(r"\s+", "", text).replace("\u00ad", "")


def displayed_value(cell):
    """Erwarteter sichtbarer Wert nach dem Zahlenformat der Originalzelle."""
    value = cell.value
    if isinstance(value, (date, datetime)):
        return value.strftime("%d.%m.%Y")
    if isinstance(value, (float, int)):
        fmt = cell.number_format
        precision = 2 if ".00" in fmt else (1 if ".0" in fmt else 0)
        percent = "%" in fmt
        number = value * 100 if percent else value
        if precision or "#,##" in fmt:
            text = format(number, f",.{precision}f").translate(str.maketrans(",.", ".,"))
        else:
            text = format(number, "g")
        return text + (" %" if percent else "")
    return str(value)


class AMLFallregisterPDF(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.hashes = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in SOURCES}
        cls.pdfs = {path: aml.render(path) for path in SOURCES}

    def test_all_actual_cells_are_visible_and_readable(self):
        # Spaltenweise Extraktion verhindert, dass mehrzeilige Nachbarzellen
        # beim Textabgleich ineinanderlaufen. Ganze Zeilen decken Vollbreite ab.
        layouts = [
            (0.22, 0.16, 0.12, 0.50), (0.20, 0.23, 0.34, 0.23),
            (0.15, 0.45, 0.14, 0.26), (0.17, 0.20, 0.20, 0.43), (0.28, 0.72),
        ]
        for path, data in self.pdfs.items():
            with self.subTest(case=path.parts[-3]), pdfplumber.open(io.BytesIO(data)) as pdf:
                self.assertTrue(data.startswith(b"%PDF-"))
                whole = "\n".join(page.extract_text() or "" for page in pdf.pages)
                views = [compact(whole)]
                for ratios in layouts:
                    left = aml.MARGIN + 6  # Platypus-Innenrand des Textrahmens.
                    for ratio in ratios:
                        right = left + aml.WIDTH * ratio
                        text = "\n".join(
                            page.crop((left + 0.1, 45, right - 0.1, page.height - 35)).extract_text() or ""
                            for page in pdf.pages
                        )
                        views.append(compact(text))
                        left = right
                workbook = openpyxl.load_workbook(path, data_only=True)
                try:
                    self.assertEqual(workbook.sheetnames, ["Übersicht", "Zahlungen", "Beteiligte", "Verlauf"])
                    for sheet in workbook:
                        self.assertIn(sheet.title, whole)
                        for row in sheet:
                            for cell in row:
                                if cell.value is None or cell.value == "":
                                    continue
                                expected = compact(displayed_value(cell))
                                self.assertTrue(any(expected in view for view in views),
                                                f"Zellinhalt fehlt: {path.parts[-3]} {sheet.title}!{cell.coordinate}: {cell.value!r}")
                finally:
                    workbook.close()
                for number, page in enumerate(pdf.pages, 1):
                    self.assertAlmostEqual(page.width, 595.2756, delta=1)
                    self.assertAlmostEqual(page.height, 841.8898, delta=1)
                    self.assertTrue(page.chars, f"Leere PDF-Seite {number}")
                    for char in page.chars:
                        self.assertGreaterEqual(char["size"], 9 - 0.01)
                        self.assertGreaterEqual(char["x0"], -0.1)
                        self.assertLessEqual(char["x1"], page.width + 0.1)
                        self.assertGreaterEqual(char["top"], -0.1)
                        self.assertLessEqual(char["bottom"], page.height + 0.1)
                    body_sizes = Counter(round(char["size"], 1) for char in page.chars if 45 < char["top"] < page.height - 35)
                    self.assertGreater(body_sizes[9.5], 0, f"Tabellentext fehlt auf Seite {number}")

    def test_source_hashes_and_rendering_stable(self):
        for path in SOURCES:
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), self.hashes[path])
            self.assertEqual(aml.render(path), self.pdfs[path])

    def test_unknown_cases_and_wrong_locations_are_untouched(self):
        for path in (
            ROOT / "testakten/anderer-fall/04_Tabellen/Fallregister.xlsx",
            ROOT / "testakten" / next(iter(aml.CASES)) / "05_Tabellen/Fallregister.xlsx",
            SOURCES[0].with_name("Andere_Tabelle.xlsx"),
        ):
            self.assertIsNone(aml.render(path))

    def test_missing_formula_cache_is_rejected(self):
        namespace = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory).joinpath(*SOURCES[0].parts[-4:])
            target.parent.mkdir(parents=True)
            removed = False
            with zipfile.ZipFile(SOURCES[0]) as original, zipfile.ZipFile(target, "w") as altered:
                for item in original.infolist():
                    data = original.read(item.filename)
                    if item.filename == "xl/worksheets/sheet1.xml":
                        sheet = ET.fromstring(data)
                        for cell in sheet.iter(namespace + "c"):
                            cached = cell.find(namespace + "v")
                            if cell.find(namespace + "f") is not None and cached is not None:
                                cell.remove(cached)
                                removed = True
                                break
                        data = ET.tostring(sheet, encoding="utf-8", xml_declaration=True)
                    altered.writestr(item, data)
            self.assertTrue(removed)
            with self.assertRaisesRegex(ValueError, "Formelcache fehlt"):
                aml.render(target)

    def test_hook_keeps_aml_results_without_libreoffice(self):
        with tempfile.TemporaryDirectory() as directory:
            other = Path(directory) / "Fallregister.xlsx"
            shutil.copyfile(SOURCES[0], other)
            with patch.object(office, "office_binary", return_value=None):
                results = office.render_office_batch([*SOURCES, other])
            self.assertEqual(set(results), set(SOURCES))
            for path in SOURCES:
                self.assertEqual(results[path], self.pdfs[path])
            with patch.object(office, "office_binary", return_value="office"), patch.object(
                office, "_render_office_group", return_value={other: b"unchanged-office-result"}
            ) as ordinary:
                results = office.render_office_batch([SOURCES[0], other])
            ordinary.assert_called_once_with([other], "office")
            self.assertEqual(results[other], b"unchanged-office-result")
            self.assertEqual(results[SOURCES[0]], self.pdfs[SOURCES[0]])


if __name__ == "__main__":
    unittest.main(verbosity=2)
