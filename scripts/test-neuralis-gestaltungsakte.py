#!/usr/bin/env python3
"""Offline-Regressionsprüfung für die gestufte Neuralis-Akte und ihre fünf Ausgabeformen."""

import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

from openpyxl import load_workbook
from pypdf import PdfReader

from akteneingang.quellen import digest
from release_asset_common import sha256_file
from testakte_gestufte_lesefassung import NEURALIS, STAGES

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "testakten" / NEURALIS
GRUND, BESCHEID, ENTWUERFE = STAGES[NEURALIS]


class NeuralisTests(unittest.TestCase):
    def test_reisekosten_summe_und_erstattung(self):
        path = CASE / GRUND / "A12_Reisekosten_Pruefzentrum.xlsx"
        values = load_workbook(path, data_only=True)
        formulas = load_workbook(path)
        self.addCleanup(values.close)
        self.addCleanup(formulas.close)
        sheet = values["RK-2307-04"]
        self.assertEqual(formulas[sheet.title]["E15"].value, "=SUM(E11:E13)")
        receipts = [sheet[f"E{row}"].value for row in (11, 12, 13)]
        self.assertEqual(receipts, [54.80, 18.60, 3.00])
        self.assertEqual(sheet["E15"].value, round(sum(receipts), 2))
        self.assertEqual(sheet["E18"].value, sheet["E15"].value)
        self.assertEqual(sheet["A18"].value.date().isoformat(), "2023-07-12")

    def test_stimmanteile_kaufpreis_und_liquiditaet(self):
        path = CASE / ENTWUERFE / "G10_Kapitalvarianten_zur_Finanzierungsrunde.xlsx"
        values = load_workbook(path, data_only=True)
        formulas = load_workbook(path)
        self.addCleanup(values.close)
        self.addCleanup(formulas.close)
        capital = values["Kapital"]
        for column, shares in (("B", [51_000, 32_000, 17_000, 100_000]),
                               ("D", [33_000, 50_000, 17_000, 100_000]),
                               ("F", [51_000, 68_000, 17_000, 136_000])):
            self.assertEqual([capital[f"{column}{row}"].value for row in range(7, 11)], shares)
            for row, share in enumerate(shares, start=7):
                self.assertAlmostEqual(capital.cell(row, capital[column + "7"].column + 1).value, share / shares[-1])
        self.assertEqual([capital[f"B{n}"].value for n in (13, 14, 15, 16)], [18_000, 36_000, 2_000_000, 120_000])
        self.assertEqual([capital[f"B{n}"].value for n in (18, 19, 20)], [360_000, 240_000, 36_000])

        # Teilnahme, abgegebene Stimmen und Zustimmung sind verschiedene Bezugsgrößen.
        voting = values["Zählprobe"]
        expected = ((100_000, 68_000, 32_000, 0, .68), (100_000, 50_000, 50_000, 0, .5),
                    (100_000, 50_000, 0, 50_000, 1), (50_000, 50_000, 0, 0, 1),
                    (136_000, 68_000, 68_000, 0, .5))
        self.assertEqual(tuple(voting.iter_rows(min_row=7, max_row=11, min_col=3, max_col=7, values_only=True)), expected)
        for sheet, cells in (("Kapital", ("D7", "D8", "F8", "B18", "B19", "B20")),
                             ("Zählprobe", ("G7", "G8", "G9", "G10", "G11"))):
            for cell in cells:
                self.assertEqual(formulas[sheet][cell].data_type, "f", (sheet, cell))

    def test_aktenstaende_lesefassungen_und_exporte(self):
        # Der Release-Builder gleicht Originalbytes, Einzel-PDFs und sämtliche
        # Seiten samt Lesezeichen im Gesamt-PDF mit dem Checkout ab.
        with tempfile.TemporaryDirectory() as scratch:
            dist = Path(scratch)
            builder = [sys.executable, str(ROOT / "scripts/build-werkstatt-partnerakten-release.py")]
            subprocess.run([*builder, "--dist", str(dist)], cwd=ROOT, check=True)
            subprocess.run([*builder, "--verify", str(dist)], cwd=ROOT, check=True)
            inventory = json.loads((dist / "release-bestand.json").read_text(encoding="utf-8"))
            self.assertEqual(set(inventory["akten"]), {NEURALIS})
            report = inventory["akten"][NEURALIS]
            expected = {
                GRUND: [f"A{i:02d}" for i in range(1, 14)],
                BESCHEID: [f"B{i:02d}" for i in range(1, 6)] + ["B05a"] + [f"B{i:02d}" for i in range(6, 14)],
                ENTWUERFE: [f"G{i:02d}" for i in range(1, 11)],
            }
            # Die PDF-Reihenfolge folgt dem dokumentierten Aktenzeichen.
            records = report["dokumente"]
            readme = (CASE / "README.md").read_text(encoding="utf-8")
            self.assertIn(f"{len(records)} Belege mit Lesezeichen auf {report['seiten']} Seiten", readme)
            fach = report["fachausgabe"]
            self.assertIn(f"{fach['druckseiten']} Seiten und ein ZIP mit {fach['aktenstuecke']} Einzel-PDFs", readme)
            for asset in dist.glob("*.zip"):
                self.assertIn(f"/releases/download/{inventory['release']}/{asset.name})", readme)
            self.pruefe_einzelabruf(dist)
            for stage, identifiers in expected.items():
                actual = [Path(row["original"]).name.split("_", 1)[0] for row in records
                          if Path(row["original"]).parent.name == stage]
                self.assertEqual(actual, identifiers, stage)

            # In der erweiterten Druckakte müssen auch die zusätzlichen
            # Eingangsunterlagen und die Arbeitsfassung am richtigen Leseziel stehen.
            with ZipFile(dist / f"druckakte-{NEURALIS}.zip") as bundle:
                merged = PdfReader(io.BytesIO(bundle.read(f"{NEURALIS}/Gesamtakte.pdf")))
                with ZipFile(io.BytesIO(bundle.read(f"{NEURALIS}/Einzel-PDFs.zip"))) as singles:
                    pdf_names = [name for name in singles.namelist() if name.endswith(".pdf")]
                    self.assertEqual({Path(name).stem for name in pdf_names}, {item.title for item in merged.outline})
                    self.assertEqual(len(merged.outline), len(records) + 5 + 1)
                    page_count = 0
                    for bookmark in merged.outline:
                        part = PdfReader(io.BytesIO(singles.read(bookmark.title + ".pdf")))
                        self.assertEqual(merged.get_destination_page_number(bookmark), page_count)
                        for page in part.pages:
                            self.assertEqual(merged.pages[page_count].extract_text(), page.extract_text(), bookmark.title)
                            page_count += 1
                    self.assertEqual(len(merged.pages), page_count)

            # Kontrollstellen beziehen sich auf die lesbaren Dokumente. Auch eine
            # vertauschte oder inhaltlich falsche PDF mit aktualisiertem Hash fällt auf.
            witnesses = {
                "A04": ("51.000", "32.000", "17.000"), "A05": ("23.06.2023", "E-2306-19"),
                "B04": ("09.02.2026", "1. März 2023", "Beschäftigung"),
                "B05": ("2026-02-11", "08:12", "09:06"), "B05a": ("18. Februar 2026", "Widersprüche"),
                "B07": ("24.02.2026", "100.000 Ja-Stimmen", "neunzig Prozent"),
                "B09": ("26.02.2026", "Anmeldung"), "B10": ("09.03.2026", "Eintragung"),
                "B11": ("19.03.2026", "68.000 Ja-", "32.000 Nein-Stimmen"),
                "B12": ("E-2603-11", "21.600", "Einzelfreigabe"),
                "G02": ("2. April 2026", "Zustimmung"), "G04": ("9. April 2026", "18.000"),
                "A11": ("E-2306-19", "62.400"), "A12": ("RK-2307-04", "76,40"),
                "A13": ("2021-0417", "400.000"), "B13": ("E-2603-11", "21.600"),
                "G06": ("6.5.1", "Zustimmung", "7.3", "Umlauf"),
                "G07": ("fünften Werktags", "31. März 2027"),
                "G08": ("18.000", "360.000", "120.000", "240.000"),
                "G09": ("Vollmacht", "Gesamtbudget", "360.000"),
                "G10": ("136.000", "360.000", "240.000", "36.000"),
            }
            with ZipFile(dist / f"testakte-{NEURALIS}-einzelpdfs.zip") as printed:
                for row in records:
                    identifier = Path(row["original"]).name.split("_", 1)[0]
                    if identifier in witnesses:
                        pdf = PdfReader(io.BytesIO(printed.read(row["lesefassung"])))
                        text = " ".join(" ".join(page.extract_text() for page in pdf.pages).split())
                        with self.subTest(akte=identifier):
                            for marker in witnesses[identifier]:
                                self.assertIn(marker, text)

    def pruefe_einzelabruf(self, release):
        # Der eigenständige Fachakten-Aufruf muss denselben Fallstand bauen.
        with tempfile.TemporaryDirectory() as scratch:
            work = Path(scratch)
            index = work / "quellen.json"
            referenzen = json.loads((ROOT / "scripts/data/grundakten-vertiefung/einzelausgaben.json").read_text())
            pfade = {}
            for feld, suffix in (("source", ""), ("print", "-einzelpdfs")):
                quelle = release / f"testakte-{NEURALIS}{suffix}.zip"
                self.assertEqual(referenzen["testakten/" + NEURALIS][feld],
                                 {"sha256": sha256_file(quelle), "size": quelle.stat().st_size})
                pfade[quelle.name] = [str(quelle)]
            index.write_text(json.dumps(pfade))
            stage = work / "stage"
            dist = work / "dist"
            subprocess.run([
                sys.executable, str(ROOT / "scripts/build-grundakten-lebenswelt.py"),
                "--vertiefung", "--akte", NEURALIS, "--local-index", str(index),
                "--stage", str(stage), "--dist", str(dist),
            ], cwd=ROOT, check=True)
            akte = stage / NEURALIS
            bestand = json.loads((akte / "bestand.json").read_text())
            self.assertEqual((bestand["aktenstuecke"], bestand["eingangspost"]), (43, 5))
            self.assertEqual(len(PdfReader(akte / "Gesamtakte.pdf").pages), 62)
            name = f"lebensakte-{NEURALIS}.zip"
            self.assertEqual(sha256_file(dist / name), sha256_file(release / name))
            with ZipFile(release / f"druckakte-{NEURALIS}.zip") as archiv:
                for name in ("Gesamtakte.pdf", "Einzel-PDFs.zip"):
                    self.assertEqual(sha256_file(akte / name), digest(archiv.read(f"{NEURALIS}/{name}")), name)


if __name__ == "__main__":
    unittest.main()
