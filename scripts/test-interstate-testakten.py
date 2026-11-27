#!/usr/bin/env python3
"""Prüft die ausgelieferten Unterlagen der Niederlassung West gegen die Falldaten."""
from __future__ import annotations

import csv
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from email import policy
from email.parser import BytesParser
from email.utils import parseaddr, parsedate_to_datetime
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unicodedata
import unittest
from urllib.parse import quote
from zipfile import ZipFile
from zoneinfo import ZoneInfo

from docx import Document
from openpyxl import load_workbook
from pypdf import PdfReader

from testakte_disclaimer import NOTICE_BYTES, NOTICE_DE, NOTICE_EN, NOTICE_MARKDOWN, notice_text_errors

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "scripts/data/interstate-ag"
COLLECTION = ROOT / "vergaberecht-werkstatt/vergabestelle-behoerden/Interstate AG"
OPENING_DOCUMENTS = {
    "01-alleinstellung": "01_bedarf_und_freigabe.docx",
    "02-fachlose": "01_bauauftrag_weidenstueck.docx",
    "03-ausschluss": "00_pruefbitte_wertung_w668.eml",
    "04-oekopunkte": "00_mitzeichnung_punktekauf.eml",
    "05-baustreit": "00_klageerwiderung_beweisangebote.eml",
    "06-nachtrag": "00_abschlag_4_zahlungslauf.eml",
    "07-vertragsmuster": "01_pruefbitte_einkauf.eml",
    "08-leitplanung": "00_rueckfrage_referenz.eml",
    "09-brueckenneubau": "00_freigabe_los_b.eml",
    "10-fahrbahnmarkierung": "00_disposition_kolonnen.eml",
    "11-it-baupruefung": "00_wertungsunterlagen_export.eml",
}
CASES = tuple(OPENING_DOCUMENTS)
FORM = "Einwendungen-Pruefbogen.xlsx"


def condensed(value):
    text = unicodedata.normalize("NFKC", str(value)).replace("\u00ad", "")
    return "".join(text.split())


def native_text(path):
    if path.suffix == ".docx":
        doc = Document(path)
        cells = [cell.text for table in doc.tables for row in table.rows for cell in row.cells]
        return "\n".join([p.text for p in doc.paragraphs] + cells)
    if path.suffix == ".xlsx":
        book = load_workbook(path, read_only=True)
        try:
            return "\n".join(str(cell) for sheet in book for row in sheet.values for cell in row if cell is not None)
        finally:
            book.close()
    if path.suffix == ".eml":
        mail = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
        return mail.get_body(preferencelist=("plain",)).get_content()
    if path.suffix == ".csv":
        with path.open(encoding="utf-8-sig", newline="") as stream:
            sample = stream.readline()
            stream.seek(0)
            rows = list(csv.reader(stream, delimiter=";" if ";" in sample else ","))
        return "\n".join(cell for row in rows for cell in row)
    if path.suffix == ".txt":
        return path.read_text(encoding="utf-8-sig")
    raise AssertionError(f"Unbekanntes Aktenformat: {path}")


class InterstateAktenTests(unittest.TestCase):
    def test_fallauswahl(self):
        self.assertEqual({p.stem for p in INPUT.glob("*.json")}, set(CASES))
        self.assertEqual({p.name for p in COLLECTION.iterdir() if p.is_dir()}, set(CASES))
        index = (COLLECTION / "README.md").read_text()
        for slug in CASES:
            self.assertIn(f"({slug}/README.md)", index)

    def test_sammelpaket(self):
        bundle = ROOT / "docs/downloads/interstate-ag-nl-west-testakten.zip"
        expected = {FORM: COLLECTION / FORM}
        for slug in CASES:
            folder = COLLECTION / slug
            for phase in ("Grundakte", "Nachreichungen", "gesamt-pdf", "downloads"):
                for path in (folder / phase).iterdir():
                    if phase != "downloads" or path.name.endswith("-einzelpdfs.zip"):
                        expected[path.relative_to(COLLECTION).as_posix()] = path
        with ZipFile(bundle) as archive:
            self.assertEqual(archive.namelist()[0], "README.txt")
            for slug, filename in OPENING_DOCUMENTS.items():
                entries = [name for name in archive.namelist() if name.startswith(f"{slug}/Grundakte/")]
                self.assertEqual(entries[0], f"{slug}/Grundakte/{filename}")
            notice = archive.read("README.txt").decode("utf-8")
            self.assertIn(NOTICE_DE, notice.split(NOTICE_EN)[0])
            self.assertIn(NOTICE_EN, notice)
            self.assertEqual(len(archive.namelist()), len(expected) + 1)
            self.assertEqual(set(archive.namelist()), set(expected) | {"README.txt"})
            for member, source in expected.items():
                self.assertEqual(archive.read(member), source.read_bytes(), member)

    def test_pruefbogen_ist_leer_und_beschreibbar(self):
        book = load_workbook(COLLECTION / FORM)
        self.assertEqual(book.sheetnames, ["Eingang", "Prüfung", "Entscheidung"])
        for sheet in book:
            self.assertEqual(sheet["A3"].value, "Kennung")
            self.assertGreater(sheet.max_column, 3)
            for row in sheet.iter_rows(min_row=4):
                self.assertTrue(all(cell.value is None for cell in row))
            sheet["A4"] = "E-01"
        result = io.BytesIO()
        book.save(result)
        result.seek(0)
        checked = load_workbook(result)
        self.assertEqual([sheet["A4"].value for sheet in checked], ["E-01"] * 3)
        checked.close()
        book.close()

    def test_falllieferungen(self):
        for slug in CASES:
            with self.subTest(fall=slug):
                self.check_case(slug)

    def check_case(self, slug):
        case = json.loads((INPUT / (slug + ".json")).read_bytes())
        root = COLLECTION / slug
        rows = case["dokumente"]
        initial = [row for row in rows if row["phase"] == "Grundakte"]
        later = [row for row in rows if row["phase"] == "Nachreichungen"]
        self.assertEqual(rows, initial + later)
        self.assertGreaterEqual(len(initial), 6)
        self.assertGreaterEqual(len(later), 2)
        self.assertLess(max(date.fromisoformat(d["datum"]) for d in initial),
                        min(date.fromisoformat(d["datum"]) for d in later))
        self.assertEqual(len({r["datei"] for r in rows}), len(rows))
        opening = initial[0]
        self.assertEqual(opening["datei"], OPENING_DOCUMENTS[slug])
        self.assertEqual(min(p.name for p in (root / "Grundakte").iterdir()), opening["datei"])
        originals = [f"{row['phase']}/{row['datei']}" for row in rows]
        on_disk = {p.relative_to(root).as_posix() for phase in ("Grundakte", "Nachreichungen")
                   for p in (root / phase).rglob("*") if p.is_file()}
        self.assertEqual(on_disk, set(originals))

        label = "testakte-" + slug
        combined_path = root / "gesamt-pdf" / (label + "_gesamt.pdf")
        originals_path = root / "downloads" / (label + ".zip")
        pdfs_path = root / "downloads" / (label + "-einzelpdfs.zip")
        readme = (root / "README.md").read_text()
        self.assertIn(NOTICE_MARKDOWN, readme)
        grundakte = readme.split("## Grundakte\n", 1)[1].split("\n## ", 1)[0]
        first_link = next(line for line in grundakte.splitlines() if "](Grundakte/" in line)
        self.assertIn(f"({quote(originals[0])})", first_link)
        pairs = case["einwendungspruefung"]
        self.assertTrue(pairs)
        review = readme.split("## Eingaben prüfen\n", 1)[1].split("\n## ", 1)[0]
        self.assertIn(f"(../{FORM})", review)
        documents = {row["datei"]: row for row in rows}
        for pair in pairs:
            self.assertNotEqual(pair["eingabe"], pair["gegenpruefung"])
            for member in (pair["eingabe"], pair["gegenpruefung"]):
                local_path = f'{documents[member]["phase"]}/{member}'
                self.assertIn(local_path, originals)
                self.assertIn(f"({quote(local_path)})", review)
        for export in (combined_path, originals_path, pdfs_path):
            self.assertIn(export.relative_to(root).as_posix(), readme)

        combined = PdfReader(combined_path)
        named_pages = {}
        for item in combined.outline:
            if isinstance(item, list):
                for target in item:
                    named_pages[target.title] = combined.get_destination_page_number(target)
        self.assertEqual([o.title for o in combined.outline if not isinstance(o, list)], ["Grundakte", "Nachreichungen"])
        self.assertEqual(list(named_pages), [r["titel"] for r in rows])
        self.assertEqual(combined.get_destination_page_number(combined.outline[0]), 0)
        self.assertEqual(named_pages[opening["titel"]], 0)
        all_pages = [condensed(p.extract_text()) for p in combined.pages]
        self.assertTrue(all(all_pages))
        for value in (opening["titel"], opening["von"], opening["an"], *opening["text"][:2]):
            self.assertIn(condensed(value), all_pages[0])
        self.assertFalse(any(condensed(notice) in page for notice in (NOTICE_DE, NOTICE_EN) for page in all_pages))

        expected_pdfs = [f"{row['phase']}__{Path(row['datei']).stem}.pdf" for row in rows]
        with ZipFile(originals_path) as files, ZipFile(pdfs_path) as singles:
            for archive, names in ((files, originals), (singles, expected_pdfs)):
                self.assertEqual(archive.namelist(), ["README.txt", *names])
                self.assertEqual(notice_text_errors(archive.read("README.txt")), [])
            for row in rows:
                original = f"{row['phase']}/{row['datei']}"
                path = root / original
                with self.subTest(akte=slug, dokument=original):
                    self.assertEqual(files.read(original), path.read_bytes())
                    part = PdfReader(io.BytesIO(singles.read(f"{row['phase']}__{path.stem}.pdf")))
                    pages = [condensed(p.extract_text()) for p in part.pages]
                    start = named_pages[row["titel"]]
                    self.assertEqual(pages, all_pages[start:start + len(pages)])
                    pdf = "".join(pages)
                    native = condensed(native_text(path))
                    for paragraph in row["text"]:
                        self.assertIn(condensed(paragraph), native)
                        self.assertIn(condensed(paragraph), pdf)
                    for cells in row.get("tabelle", []):
                        for cell in cells:
                            if isinstance(cell, str) and cell.strip():
                                self.assertIn(condensed(cell), native)
                                self.assertIn(condensed(cell), pdf)
                    if path.suffix == ".eml":
                        mail = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
                        self.assertEqual(str(mail["Subject"]), row["titel"])
                        self.assertEqual(parseaddr(str(mail["From"]))[1], row["absender"])
                        self.assertEqual(parseaddr(str(mail["To"]))[1], row["empfaenger"])
                        sent = parsedate_to_datetime(str(mail["Date"])).astimezone(ZoneInfo("Europe/Berlin"))
                        self.assertEqual(sent.isoformat(timespec="minutes")[:16], f'{row["datum"]}T{row["uhrzeit"]}')


class InterstateLeistungsverzeichnisTests(unittest.TestCase):
    def positions(self, slug, name):
        case = json.loads((INPUT / (slug + ".json")).read_bytes())
        doc = next(d for d in case["dokumente"] if d["datei"] == name)
        path = COLLECTION / slug / doc["phase"] / name
        fields = doc["tabelle"][0]
        amount = fields.index(doc["lv"]["menge"])
        price = fields.index(doc["lv"]["einheitspreis"])
        total = fields.index(doc["lv"]["gesamtpreis"])
        formulas = load_workbook(path, read_only=True)
        try:
            rows = iter(formulas.active.rows)
            next(row for row in rows if [cell.value for cell in row] == fields)
            for row in rows:
                self.assertEqual(row[total].data_type, "f", f"{name}: {row[total].coordinate}")
        finally:
            formulas.close()
        with path.open("rb") as stream:
            book = load_workbook(stream, read_only=True, data_only=True)
            try:
                rows = iter(book.active.values)
                next(row for row in rows if list(row) == fields)
                items = {}
                for position in doc["tabelle"][1:]:
                    row = next(rows)
                    self.assertEqual(row[0], position[0])
                    self.assertNotIn(row[0], items)
                    qty, ep, gp = row[amount], row[price], row[total]
                    self.assertIsInstance(qty, (int, float))
                    self.assertGreater(qty, 0)
                    self.assertNotIsInstance(qty, bool)
                    if ep is None:
                        self.assertIn(gp, (None, ""))
                    else:
                        expected = (Decimal(str(qty)) * Decimal(str(ep))).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
                        self.assertEqual(Decimal(str(gp)), expected)
                    items[row[0]] = (qty, ep, gp)
                summary = next(rows)
                priced = [item[2] for item in items.values() if item[1] is not None]
                if len(priced) == len(items):
                    self.assertEqual(Decimal(str(summary[total])), sum(Decimal(str(p)) for p in priced))
                else:
                    self.assertIn(summary[total], (None, ""))
                if "losspalte" in doc["lv"]:
                    lot_column = fields.index(doc["lv"]["losspalte"])
                    by_lot = {}
                    for position in doc["tabelle"][1:]:
                        by_lot.setdefault(position[lot_column], []).append(items[position[0]][2])
                    summaries = {row[lot_column]: row[total] for row in rows if row[lot_column]}
                    self.assertEqual(set(summaries), set(by_lot))
                    for lot, amounts in by_lot.items():
                        if all(value is not None for value in amounts):
                            self.assertEqual(Decimal(str(summaries[lot])), sum(Decimal(str(p)) for p in amounts))
                        else:
                            self.assertIn(summaries[lot], (None, ""))
                return items
            finally:
                book.close()

    def test_leistungsverzeichnisse_der_vier_fachvergaben(self):
        for slug in CASES[7:]:
            with self.subTest(fall=slug):
                case = json.loads((INPUT / (slug + ".json")).read_text())
                workbooks = [doc for doc in case["dokumente"] if "lv" in doc]
                self.assertTrue(workbooks, f"{slug}: kalkulierbares Leistungsverzeichnis fehlt")
                for doc in workbooks:
                    self.assertTrue(self.positions(slug, doc["datei"]))

    def test_teillose_fachlose_und_marktpreise(self):
        slug = "02-fachlose"
        north = self.positions(slug, "02a_lv_nord.xlsx")
        south = self.positions(slug, "02b_lv_sued.xlsx")
        self.assertTrue(north.keys().isdisjoint(south))
        self.assertEqual({key.split(".")[1] for key in north}, {"B", "O", "M"})
        self.assertEqual({key.split(".")[1] for key in south}, {"B", "O", "M"})
        blank = north | south
        self.assertTrue(all(item[1] is None for item in blank.values()))
        priced = self.positions(slug, "09_richtpreis_gewerke.xlsx")
        self.assertEqual({k: v[0] for k, v in blank.items()}, {k: v[0] for k, v in priced.items()})
        self.assertTrue(all(item[1] is not None for item in priced.values()))
        lots = {}
        for code, (_, _, value) in priced.items():
            lot = code.rsplit(".", 1)[0]
            lots[lot] = lots.get(lot, 0) + value
        self.assertEqual(lots, {"N.B": 2519500, "N.O": 1231200, "N.M": 503400,
                                "S.B": 1720750, "S.O": 820800, "S.M": 335600})
        self.assertEqual(sum(lots.values()), 7131250)

    def test_wertbarer_preis_und_vertragsvergleich(self):
        blank = self.positions("03-ausschluss", "02a_bieter_lv_messstationen.xlsx")
        offered = self.positions("03-ausschluss", "04a_preisblatt_w668.xlsx")
        self.assertEqual({k: v[0] for k, v in blank.items()}, {k: v[0] for k, v in offered.items()})
        self.assertTrue(all(item[1] is None for item in blank.values()))
        self.assertEqual(offered["2.4"], (24, 1700, 40800))
        self.assertEqual(sum(item[2] for item in offered.values()), 418800)
        contract = self.positions("06-nachtrag", "00_auftrags_lv_kf3.xlsx")
        supplement = self.positions("06-nachtrag", "11_nachtrags_lv_n7.xlsx")
        self.assertEqual(sum(item[2] for item in contract.values()), 486230)
        self.assertEqual({key: vals[0] for key, vals in supplement.items()},
                         {"N7.1": 124, "N7.2": 44, "N7.3": 4, "N7.4": 16})
        self.assertEqual(sum(item[2] for item in supplement.values()), 12924)


class InterstatePluginTests(unittest.TestCase):
    def test_installierbares_desktop_paket(self):
        scope = ROOT / "scripts/data/qualitaetsrunde-v445.36.17-scope.json"
        edition = json.loads(scope.read_text())
        tag = edition["tag"]
        with tempfile.TemporaryDirectory() as output:
            subprocess.run([sys.executable, str(ROOT / "scripts/build-skill-quality-release.py"),
                            "--scope", str(scope), "--dist", output], cwd=ROOT, check=True)
            name = "vergabestelle-behoerden.zip"
            with ZipFile(Path(output) / name) as package:
                from skill_sources import original_skill_sources
                plugin = COLLECTION.parent
                active = sorted((plugin / "skills").glob("*/SKILL.md"))
                modules = original_skill_sources(plugin)
                self.assertEqual(len(active), 8)
                self.assertEqual(len(modules), 122)
                for path in set(active) | set(modules):
                    member = path.relative_to(plugin).as_posix()
                    self.assertEqual(package.read(member), path.read_bytes(), member)
                readme = package.read("README.md").decode()
                self.assertIn(f"/releases/download/{tag}/{name}", readme)
                self.assertNotIn(f"/releases/download/{edition['plugins'][0]['previous_release']['tag']}/{name}", readme)
                self.assertEqual(json.loads(package.read(".claude-plugin/plugin.json"))["version"], edition["version"])
                self.assertIn("(Interstate%20AG/README.md)", package.read("README.md").decode())
                self.assertEqual(package.read("README.txt"), NOTICE_BYTES)
                index = package.read("Interstate AG/README.md").decode()
                self.assertEqual(package.read(f"Interstate AG/{FORM}"), (COLLECTION / FORM).read_bytes())
                for slug in CASES:
                    with self.subTest(akte=slug):
                        self.assertIn(f"({slug}/README.md)", index)
                        label = f"testakte-{slug}"
                        for path in (f"Grundakte/{OPENING_DOCUMENTS[slug]}",
                                     f"downloads/{label}.zip", f"downloads/{label}-einzelpdfs.zip",
                                     f"gesamt-pdf/{label}_gesamt.pdf"):
                            self.assertEqual(package.read(f"Interstate AG/{slug}/{path}"),
                                             (COLLECTION / slug / path).read_bytes())


if __name__ == "__main__":
    unittest.main()
