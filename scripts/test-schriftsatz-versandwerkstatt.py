#!/usr/bin/env python3
"""End-to-End-Test der fokussierten Schriftsatz-Versandwerkstatt."""

from __future__ import annotations

import importlib.util
import contextlib
import csv
import io
import json
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch
from email.message import EmailMessage
from pathlib import Path
from types import ModuleType

from docx import Document
from openpyxl import Workbook
from pypdf import PdfReader, PdfWriter
from pypdf.generic import ArrayObject, DictionaryObject, NameObject, TextStringObject
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


REPO = Path(__file__).resolve().parent.parent
TOOL = (
    REPO
    / "schriftsatz-versandwerkstatt"
    / "skills"
    / "versandmappe-endfertigen"
    / "werkzeuge"
    / "build_versandmappe.py"
)


def load_tool() -> ModuleType:
    spec = importlib.util.spec_from_file_location("build_versandmappe", TOOL)
    if spec is None or spec.loader is None:
        raise AssertionError(f"Werkzeug nicht ladbar: {TOOL}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def write_pdf(path: Path, title: str, pages: int) -> None:
    pdf = canvas.Canvas(str(path), pagesize=A4)
    _, height = A4
    for page in range(1, pages + 1):
        pdf.setFont("Helvetica-Bold", 15)
        pdf.drawString(56, height - 72, title)
        pdf.setFont("Helvetica", 11)
        pdf.drawString(56, height - 106, f"Seite {page} von {pages}")
        for row in range(8):
            pdf.drawString(56, height - 145 - row * 22, f"Dokumentinhalt {row + 1} auf Seite {page}.")
        pdf.showPage()
    pdf.save()


def write_eml(path: Path) -> None:
    message = EmailMessage()
    message["From"] = "bauleitung@example.org"
    message["To"] = "kanzlei@example.org"
    message["Date"] = "Tue, 14 Jul 2026 09:30:00 +0200"
    message["Subject"] = "Abnahme und Restarbeiten"
    message.set_content("Die Abnahme fand am 13. Juli 2026 statt. Die Restarbeiten sind bis zum 20. Juli auszuführen.")
    path.write_bytes(message.as_bytes(policy=message.policy))


def write_office_sources(docx_path: Path, xlsx_path: Path) -> None:
    document = Document()
    document.add_heading("Klageerwiderung", level=1)
    document.add_paragraph("Landgericht Essen")
    document.add_paragraph("Aktenzeichen 12 O 34/26")
    document.add_paragraph("Der Beklagte beantragt, die Klage abzuweisen.")
    document.add_paragraph("Rechtsanwalt Max Muster")
    document.save(docx_path)

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Berechnung"
    sheet.append(["Position", "Betrag", "Datum"])
    sheet.append(["Hauptforderung", 12500, "2026-06-30"])
    sheet.append(["Zahlung", -2500, "2026-07-03"])
    workbook.save(xlsx_path)


class Produktionsschutz(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="versand-schutz-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "eingang"
        self.source.mkdir()
        self.target = self.root / "ausgang"
        self.lead = self.source / "Schriftsatz.pdf"
        write_pdf(self.lead, "Schriftsatz", 1)
        self.tool = load_tool()

    def run_tool(self, *extra: str, target: Path | None = None) -> int:
        args = ["--eingang", str(self.source), "--ausgang", str(target or self.target),
                "--hauptdokument", str(self.lead), "--gericht", "Landgericht Berlin II",
                "--aktenzeichen", "12 O 34/26", "--frist", "2026-09-30 23:59",
                "--verantwortlich", "Rechtsanwalt Jan Müller", "--versender", "Jan Müller",
                "--signaturweg", "persoenlich-sicher", "--sichtpruefung-bestaetigt", "--strict", *extra]
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return self.tool.main(args)

    def plan(self, *rows: list[str]) -> Path:
        path = self.source / "Anlagenplan.csv"
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream, delimiter=";")
            writer.writerow(["quelle", "anlage", "beschreibung", "auslassen_grund"])
            writer.writerows(rows)
        return path

    def report(self) -> str:
        return (self.target / "intern" / "Preflight-Bericht.md").read_text(encoding="utf-8")

    def test_originals_survive_overlapping_output(self) -> None:
        original = self.lead.read_bytes()
        for target in (self.source, self.source / "export", self.root):
            with self.subTest(target=target):
                self.assertEqual(self.run_tool("--ueberschreiben", target=target), 2)
                self.assertEqual(self.lead.read_bytes(), original)
        self.target.mkdir()
        self.lead = self.target / "extern.pdf"
        write_pdf(self.lead, "Original außerhalb des Eingangs", 1)
        self.assertEqual(self.run_tool("--ueberschreiben"), 2)
        self.assertTrue(self.lead.is_file())

    def test_output_file_rejected_without_deletion(self) -> None:
        self.target.write_text("behalten", encoding="utf-8")
        self.assertEqual(self.run_tool("--ueberschreiben"), 2)
        self.assertEqual(self.target.read_text(), "behalten")

    def test_plan_keeps_original_names_and_documents_exclusions(self) -> None:
        scan = self.source / "Scan Müller.pdf"
        write_pdf(scan, "Kaufvertrag Müller", 1)
        original = scan.read_bytes()
        (self.source / "interne Notiz.txt").write_text("Rückruf vereinbart", encoding="utf-8")
        plan = self.plan([scan.name, "K 1", "Kaufvertrag", ""],
                         ["interne Notiz.txt", "", "", "Interne Gesprächsnotiz; keine Anlage"])
        self.assertEqual(self.run_tool("--anlagenplan", str(plan)), 0)
        self.assertEqual(scan.read_bytes(), original)
        self.assertEqual(len(list((self.target / "versandfertig").glob("*.pdf"))), 2)
        self.assertIn("Interne Gesprächsnotiz; keine Anlage", self.report())

    def test_unknown_files_and_incomplete_plan_stop(self) -> None:
        write_pdf(self.source / "Anlage_K1_Vertrag.pdf", "Vertrag", 1)
        (self.source / "Notiz.txt").write_text("Noch zuzuordnen", encoding="utf-8")
        self.assertEqual(self.run_tool(), 3)
        self.assertIn("Keine Anlagenkennung", self.report())
        plan = self.plan(["Anlage_K1_Vertrag.pdf", "K 1", "Vertrag", ""])
        self.assertEqual(self.run_tool("--anlagenplan", str(plan), "--ueberschreiben"), 3)
        self.assertIn("Datei fehlt im Anlagenplan", self.report())

    def test_invalid_plans_fail_before_output(self) -> None:
        (self.source / "Notiz.txt").write_text("Notiz", encoding="utf-8")
        rows = (["../fremd.pdf", "K 1", "", ""], ["fehlt.pdf", "K 1", "", ""],
                ["Notiz.txt", "K 0", "", ""], ["Notiz.txt", "K 1", "", "beides"],
                ["Notiz.txt", "K 1", "", "", "fünfte Spalte"],
                [str(self.lead), "K 1", "", ""], [self.lead.name, "K 1", "", ""])
        for row in rows:
            with self.subTest(row=row):
                plan = self.plan(row)
                self.assertEqual(self.run_tool("--anlagenplan", str(plan)), 2)
                self.assertFalse(self.target.exists())
        row = ["Notiz.txt", "K 1", "", ""]
        self.assertEqual(self.run_tool("--anlagenplan", str(self.plan(row, row))), 2)

    def test_duplicate_labels_do_not_choose_arbitrary_version(self) -> None:
        for name in ("Anlage_K1_Erster.pdf", "Anlage_K1_Zweiter.pdf"):
            write_pdf(self.source / name, name, 1)
        self.assertEqual(self.run_tool(), 3)
        self.assertEqual(len(list((self.target / "versandfertig").glob("*.pdf"))), 1)
        self.assertIn("keine Fassung ausgewählt", self.report())

    def test_nrw_suffixes_remain_distinct(self) -> None:
        for suffix in ("a", "b"):
            write_pdf(self.source / f"Anlage_K1{suffix}_Vertrag.pdf", f"Vertrag {suffix}", 1)
        self.assertEqual(self.run_tool("--profil", "nrw"), 0)
        self.assertTrue((self.target / "versandfertig" / "Anlage_01a_Vertrag.pdf").exists())
        self.assertTrue((self.target / "versandfertig" / "Anlage_01b_Vertrag.pdf").exists())

    def test_multipage_tiff_keeps_all_pages(self) -> None:
        image = Image.new("RGB", (240, 120), "red")
        second = Image.new("RGB", (240, 120), "blue")
        image.save(self.source / "Anlage_K1_Scan.tiff", save_all=True, append_images=[second])
        self.assertEqual(self.run_tool(), 0)
        output = next((self.target / "versandfertig").glob("*AnlageK1*.pdf"))
        self.assertEqual(len(PdfReader(output).pages), 2)

    def test_federal_profile_fits_actual_bea_filename_limit(self) -> None:
        write_pdf(self.source / ("Anlage_K1_" + "Lang" * 25 + ".pdf"), "Vertrag", 1)
        self.assertEqual(self.run_tool("--profil", "bund", "--dokumentart", "Lang" * 25), 0)
        self.assertTrue(all(len(p.name) <= 84 for p in (self.target / "versandfertig").glob("*.pdf")))

    def test_signature_markers_block_stamping_but_main_is_unchanged(self) -> None:
        signed = self.source / "Anlage_K1_Signatur.pdf"
        writer = PdfWriter(clone_from=self.lead)
        # Strukturmerkmal, keine kryptografisch gültige Signatur.
        field = DictionaryObject({NameObject("/FT"): NameObject("/Sig"),
                                  NameObject("/T"): TextStringObject("Unterschrift"),
                                  NameObject("/V"): DictionaryObject({NameObject("/Type"): NameObject("/Sig")})})
        writer.pages[0][NameObject("/Annots")] = ArrayObject([writer._add_object(field)])
        writer.write(signed)
        original = signed.read_bytes()
        self.assertEqual(self.run_tool(), 3)
        self.assertIn("Signaturfeld", self.report())
        self.assertEqual(signed.read_bytes(), original)
        self.lead.unlink()
        self.lead = signed
        self.assertEqual(self.run_tool("--ohne-anlagen", "--ueberschreiben"), 0)
        output = next((self.target / "versandfertig").glob("*.pdf"))
        self.assertEqual(output.read_bytes(), original)

    def test_partial_failure_cleans_output_and_keeps_diagnostics(self) -> None:
        write_pdf(self.source / "Anlage_K1_Vertrag.pdf", "Vertrag", 1)
        def broken(source, target, *args):
            target.write_bytes(b"incomplete PDF")
            raise RuntimeError("Abgebrochene PDF-Ausgabe")
        with patch.object(self.tool, "anlage_stempeln", side_effect=broken):
            self.assertEqual(self.run_tool(), 3)
        self.assertEqual(len(list((self.target / "versandfertig").glob("*.pdf"))), 1)
        self.assertIn("Abgebrochene PDF-Ausgabe", self.report())
        manifest = json.loads((self.target / "intern" / "Versandmanifest.json").read_text())
        self.assertEqual(manifest["metadaten"]["status"], "STOP")

    def test_email_attachment_must_be_accounted_for(self) -> None:
        attachment = self.source / "Anlage_K2_Vertrag.pdf"
        write_pdf(attachment, "Vertrag", 1)
        payload = attachment.read_bytes()
        attachment.unlink()
        message = EmailMessage()
        message["Subject"] = "Vertrag im Anhang"
        message.set_content("Anbei der Vertrag.")
        message.add_attachment(payload, maintype="application", subtype="pdf", filename="Vertrag.pdf")
        (self.source / "Anlage_K1_Mail.eml").write_bytes(message.as_bytes())
        self.assertEqual(self.run_tool(), 3)
        self.assertIn("E-Mail-Anhang Vertrag.pdf", self.report())
        part = next(message.iter_attachments())
        del part["Content-Disposition"]
        part.set_param("name", "Vertrag.pdf", header="Content-Type")
        (self.source / "Anlage_K1_Mail.eml").write_bytes(message.as_bytes())
        self.assertEqual(self.run_tool("--ueberschreiben"), 3)
        self.assertIn("nicht als eigene unveränderte Anlagenquelle", self.report())
        part["Content-Disposition"] = "inline"
        (self.source / "Anlage_K1_Mail.eml").write_bytes(message.as_bytes())
        self.assertEqual(self.run_tool("--ueberschreiben"), 3)
        attachment.write_bytes(payload)
        self.assertEqual(self.run_tool("--ueberschreiben"), 0)
        plan = self.plan(["Anlage_K1_Mail.eml", "K 1", "Mail", ""],
                         [attachment.name, "", "", "Vertrag wird nicht eingereicht"])
        self.assertEqual(self.run_tool("--anlagenplan", str(plan), "--ueberschreiben"), 0)
        self.assertIn("ausdrücklich ausgeschlossen", self.report())

    def test_no_annex_requires_explicit_choice(self) -> None:
        self.assertEqual(self.run_tool(), 3)
        self.assertEqual(self.run_tool("--ohne-anlagen", "--ueberschreiben"), 0)
        write_pdf(self.source / "Anlage_K1_Vertrag.pdf", "Vertrag", 1)
        self.assertEqual(self.run_tool("--ohne-anlagen", "--ueberschreiben"), 3)

    def test_nested_inline_image_is_not_silently_lost(self) -> None:
        buffer = io.BytesIO()
        Image.new("RGB", (120, 80), "green").save(buffer, format="PNG")
        payload = buffer.getvalue()
        message = EmailMessage()
        message.set_content("Das Foto steht in der HTML-Fassung.")
        message.add_alternative('<html><body>Abnahmefoto<img src="cid:foto"></body></html>', subtype="html")
        message.get_payload()[1].add_related(payload, maintype="image", subtype="png", cid="<foto>",
                                             disposition="inline", filename="Foto.png")
        (self.source / "Anlage_K1_Mail.eml").write_bytes(message.as_bytes())
        self.assertEqual(self.run_tool(), 3)
        self.assertIn("E-Mail-Anhang Foto.png", self.report())
        (self.source / "Anlage_K2_Foto.png").write_bytes(payload)
        self.assertEqual(self.run_tool("--ueberschreiben"), 0)

    def test_unsupported_glyphs_do_not_silently_disappear(self) -> None:
        (self.source / "Anlage_K1_Nachricht.txt").write_text("\u0418\u043c\u044f", encoding="utf-8")
        self.assertEqual(self.run_tool(), 3)
        self.assertIn("nicht durch Fragezeichen ersetzen", self.report())

    def test_qes_allows_authorized_staff_but_needs_verification(self) -> None:
        self.assertEqual(self.run_tool("--ohne-anlagen", "--signaturweg", "qes",
                                       "--versender", "Kanzleimitarbeiter Otto Weber", "--qes-geprueft"), 0)

    def test_visual_gate_remains_open_on_first_run(self) -> None:
        args = ["--eingang", str(self.source), "--ausgang", str(self.target),
                "--hauptdokument", str(self.lead), "--ohne-anlagen", "--strict"]
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(self.tool.main(args), 3)
        self.assertIn("visuelle Prüfung", self.report())


def main() -> int:
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Produktionsschutz))
    if not result.wasSuccessful():
        return 1
    tool = load_tool()
    with tempfile.TemporaryDirectory(prefix="versandwerkstatt-test-") as tmp:
        root = Path(tmp)
        source = root / "eingang"
        target = root / "ausgang"
        source.mkdir()

        office_test = bool(shutil.which("soffice") or shutil.which("libreoffice"))
        if office_test:
            lead = source / "Klageerwiderung.docx"
            write_office_sources(lead, source / "Anlage_B-04_Berechnung.xlsx")
        else:
            lead = source / "Klageerwiderung.pdf"
            write_pdf(lead, "Klageerwiderung", 2)
        write_pdf(source / "Anlage_B-01_Kaufvertrag.pdf", "Kaufvertrag", 2)
        write_pdf(source / "Anlage_B-02_Mahnung.pdf", "Mahnung", 1)
        email_dir = source / "e-mails"
        email_dir.mkdir()
        write_eml(email_dir / "Anlage_B-03_E-Mail-Abnahme.eml")

        exit_code = tool.main(
            [
                "--eingang",
                str(source),
                "--ausgang",
                str(target),
                "--praefix",
                "B",
                "--hauptdokument",
                str(lead),
                "--dokumentart",
                "Klageerwiderung_12_O_34_26",
                "--gericht",
                "Landgericht Essen",
                "--aktenzeichen",
                "12 O 34/26",
                "--frist",
                "2026-07-15 23:59",
                "--verantwortlich",
                "Rechtsanwalt Max Muster",
                "--versender",
                "Max Muster",
                "--signaturweg",
                "persoenlich-sicher",
                "--sichtpruefung-bestaetigt",
                "--strict",
            ]
        )
        if exit_code != 0:
            raise AssertionError(f"Werkzeuglauf endete mit Status {exit_code}")

        shipping = target / "versandfertig"
        shipped = sorted(shipping.glob("*.pdf"))
        expected_files = 5 if office_test else 4
        if len(shipped) != expected_files:
            raise AssertionError(f"{expected_files} Versanddateien erwartet, erhalten: {shipped}")
        if any(len(path.name) > 80 or not path.name.isascii() or " " in path.name for path in shipped):
            raise AssertionError(f"Dateinamensprofil verletzt: {[p.name for p in shipped]}")

        email_pdf = next(path for path in shipped if "AnlageB3" in path.name)
        email_text = "\n".join((page.extract_text() or "") for page in PdfReader(str(email_pdf)).pages)
        for marker in ("Anlage B 3", "Abnahme und Restarbeiten", "bauleitung@example.org"):
            if marker not in email_text:
                raise AssertionError(f"E-Mail-PDF enthält {marker!r} nicht")

        manifest = json.loads((target / "intern" / "Versandmanifest.json").read_text(encoding="utf-8"))
        if manifest["metadaten"]["signaturweg"] != "persoenlich-sicher":
            raise AssertionError("Signaturweg fehlt im Manifest")
        email_entry = next(entry for entry in manifest["anlagen"] if entry["anlage"] == "Anlage B 3")
        if email_entry["quelle"] != "e-mails/Anlage_B-03_E-Mail-Abnahme.eml":
            raise AssertionError("Relativer Quellpfad der E-Mail fehlt im Manifest")
        for name in ("Freigabevermerk.md", "Eingangskontrolle.md", "Preflight-Bericht.md"):
            if not (target / "intern" / name).is_file():
                raise AssertionError(f"Interne Prüfausgabe fehlt: {name}")
        if "| STOP |" in (target / "intern" / "Preflight-Bericht.md").read_text(encoding="utf-8"):
            raise AssertionError("Preflight enthält unerwarteten Stop-Befund")

        mismatch = root / "mismatch"
        mismatch_code = tool.main(
            [
                "--eingang",
                str(source),
                "--ausgang",
                str(mismatch),
                "--praefix",
                "B",
                "--hauptdokument",
                str(lead),
                "--gericht",
                "Landgericht Essen",
                "--aktenzeichen",
                "12 O 34/26",
                "--frist",
                "2026-07-15 23:59",
                "--verantwortlich",
                "Rechtsanwalt Max Muster",
                "--versender",
                "Kanzleimitarbeiterin Jana Winter",
                "--signaturweg",
                "persoenlich-sicher",
                "--sichtpruefung-bestaetigt",
                "--strict",
            ]
        )
        if mismatch_code != 3:
            raise AssertionError("Fremdversand ohne qualifizierte elektronische Signatur wurde nicht gestoppt")
        mismatch_preflight = (mismatch / "intern" / "Preflight-Bericht.md").read_text(encoding="utf-8")
        if "stimmen beim persönlichen sicheren Versand nicht überein" not in mismatch_preflight:
            raise AssertionError("Absenderkonflikt fehlt im Preflight")

        qes = root / "qes"
        qes_code = tool.main(
            [
                "--eingang",
                str(source),
                "--ausgang",
                str(qes),
                "--praefix",
                "B",
                "--hauptdokument",
                str(lead),
                "--gericht",
                "Landgericht Essen",
                "--aktenzeichen",
                "12 O 34/26",
                "--frist",
                "2026-07-15 23:59",
                "--verantwortlich",
                "Rechtsanwalt Max Muster",
                "--versender",
                "Kanzleimitarbeiterin Jana Winter",
                "--signaturweg",
                "qes",
                "--sichtpruefung-bestaetigt",
                "--strict",
            ]
        )
        if qes_code != 3:
            raise AssertionError("Nicht bestätigte qualifizierte elektronische Signatur wurde nicht gestoppt")
        qes_preflight = (qes / "intern" / "Preflight-Bericht.md").read_text(encoding="utf-8")
        if "qualifizierte elektronische Signatur ist nicht als manuell geprüft bestätigt" not in qes_preflight:
            raise AssertionError("Signaturprüf-Stop fehlt im Preflight")

    office_status = "mit Office-Konvertierung" if office_test else "ohne verfügbares LibreOffice"
    print(f"test-schriftsatz-versandwerkstatt OK (Positivlauf {office_status}, EML, Absenderkonflikt und Signatur-Stop)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
