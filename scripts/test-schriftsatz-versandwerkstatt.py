#!/usr/bin/env python3
"""End-to-End-Test der fokussierten Schriftsatz-Versandwerkstatt."""

from __future__ import annotations

import importlib.util
import contextlib
import csv
import hashlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch
from email.message import EmailMessage
from email import policy
from email.parser import BytesParser
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

    def test_email_main_document_attachment_identity(self) -> None:
        original = self.lead.read_bytes()
        message = EmailMessage()
        message.set_content("Anbei der Schriftsatz.")
        message.add_attachment(original, maintype="application", subtype="pdf", filename=self.lead.name)
        (self.source / "Anlage_K1_Mail.eml").write_bytes(message.as_bytes())
        self.assertEqual(self.run_tool(), 0)
        manifest = json.loads((self.target / "intern" / "Versandmanifest.json").read_text())
        self.assertEqual(manifest["metadaten"]["sha256_hauptquelle"], hashlib.sha256(original).hexdigest())
        write_pdf(self.lead, "Geaenderter Schriftsatz", 1)
        self.assertEqual(self.run_tool("--ueberschreiben"), 3)
        self.assertIn("E-Mail-Anhang Schriftsatz.pdf", self.report())

    def rfc822_mail(self, payload: bytes, linesep: bytes = b"\n") -> Path:
        prefix = (b'MIME-Version: 1.0\nContent-Type: multipart/mixed; boundary="outer-boundary"\n'
                  b'Subject: Weiterleitung\n\n--outer-boundary\nContent-Type: text/plain\n\nAnbei.\n'
                  b'--outer-boundary\nContent-Type: message/rfc822\nContent-Transfer-Encoding: 8bit\n'
                  b'Content-Disposition: attachment; filename="Original.eml"\n\n')
        raw = prefix.replace(b"\n", linesep) + payload + linesep + b"--outer-boundary--" + linesep
        path = self.source / "Anlage_K1_Mail.eml"
        path.write_bytes(raw)
        return path

    def test_main_eml_attachments_are_audited_even_when_attached_as_binary(self) -> None:
        attachment = self.source / "Anlage_K2_Vertrag.pdf"
        write_pdf(attachment, "Vertrag", 1)
        payload = attachment.read_bytes()
        attachment.unlink()
        main = EmailMessage()
        main["Subject"] = "Hauptnachricht"
        main.set_content("Anbei der Vertrag.")
        main.add_attachment(payload, maintype="application", subtype="pdf", filename="Vertrag.pdf")
        self.lead.unlink()
        self.lead = self.source / "Haupt.eml"
        self.lead.write_bytes(main.as_bytes())
        outer = EmailMessage()
        outer.set_content("Anbei die Hauptnachricht.")
        outer.add_attachment(self.lead.read_bytes(), maintype="application", subtype="octet-stream",
                             filename="Haupt.eml")
        (self.source / "Anlage_K1_Mail.eml").write_bytes(outer.as_bytes())
        self.assertEqual(self.run_tool(), 3)
        self.assertIn("E-Mail-Anhang Vertrag.pdf", self.report())
        self.assertIn("Haupt.eml", self.report())
        attachment.write_bytes(payload)
        self.assertEqual(self.run_tool("--ueberschreiben"), 0)

    def test_main_eml_without_annexes_still_checks_embedded_attachments(self) -> None:
        main = EmailMessage()
        main["Subject"] = "Hauptnachricht"
        main.set_content("Anbei der Vertrag.")
        main.add_attachment(self.lead.read_bytes(), maintype="application", subtype="pdf", filename="Vertrag.pdf")
        self.lead.unlink()
        self.lead = self.source / "Haupt.eml"
        self.lead.write_bytes(main.as_bytes())
        self.assertEqual(self.run_tool("--ohne-anlagen"), 3)
        self.assertIn("E-Mail-Anhang Vertrag.pdf", self.report())
        main.clear_content()
        main.set_content("Diese Nachricht hat keine Anlagen.")
        self.lead.write_bytes(main.as_bytes())
        self.assertEqual(self.run_tool("--ohne-anlagen", "--ueberschreiben"), 0)

    def test_explicit_rfc822_exclusion_skips_only_its_own_subtree(self) -> None:
        nested = EmailMessage()
        nested["Subject"] = "Ausgeschlossene Nachricht"
        nested.set_content("Anbei der Vertrag.")
        nested.add_attachment(b"Nicht separat eingereichter Vertrag", maintype="application", subtype="pdf",
                              filename="Vertrag.pdf")
        raw = nested.as_bytes()
        excluded = self.source / "Original.eml"
        excluded.write_bytes(raw)
        outer = self.rfc822_mail(raw)
        reason = "Gesamte Nachricht einschliesslich aller eingebetteten Anlagen nicht eingereicht"
        rows = [[outer.name, "K 1", "Begleitnachricht", ""], [excluded.name, "", "", reason]]
        plan = self.plan(*rows)
        self.assertEqual(self.run_tool("--anlagenplan", str(plan)), 0, self.report())
        self.assertIn("E-Mail-Anhang Original.eml ausdrücklich ausgeschlossen", self.report())
        self.assertNotIn("E-Mail-Anhang Vertrag.pdf", self.report())

        independent = self.source / "Anlage_K2_Unabhaengige_Nachricht.eml"
        independent.write_bytes(raw)
        plan = self.plan(*rows, [independent.name, "K 2", "Separat eingereichte Nachricht", ""])
        self.assertEqual(self.run_tool("--anlagenplan", str(plan), "--ueberschreiben"), 3)
        self.assertIn("E-Mail-Anhang Vertrag.pdf", self.report())
        manifest = json.loads((self.target / "intern" / "Versandmanifest.json").read_text())
        stops = [b for b in manifest["metadaten"]["befunde"] if b["stufe"] == "STOP"]
        self.assertTrue(any(b["datei"] == independent.name and "Vertrag.pdf" in b["text"] for b in stops))
        self.assertFalse(any(b["datei"] == outer.name for b in stops))

        independent.unlink()
        plan = self.plan(*rows)
        self.rfc822_mail(raw.replace(b"Subject: Ausgeschlossene Nachricht", b"Subject: Andere Nachricht"))
        self.assertEqual(self.run_tool("--anlagenplan", str(plan), "--ueberschreiben"), 3)
        self.assertIn("E-Mail-Anhang Original.eml ist nicht", self.report())
        self.assertIn("E-Mail-Anhang Vertrag.pdf", self.report())

    def test_rfc822_complete_identity_lf_crlf_and_raw_hashes(self) -> None:
        original = (b'From: sender@example.org\nTo: recipient@example.org\nSubject:  Original\n'
                    b'X-Trace:\tfirst\n\tsecond\nContent-Type: text/plain; charset="utf-8"\n\nUnveraendert.\n')
        source = self.source / "Anlage_K2_Original.eml"
        for source_sep in (b"\n", b"\r\n"):
            for attached_sep in (b"\n", b"\r\n"):
                with self.subTest(source=source_sep, attachment=attached_sep):
                    raw = original.replace(b"\n", source_sep)
                    source.write_bytes(raw)
                    mail = self.rfc822_mail(original.replace(b"\n", attached_sep), attached_sep)
                    self.assertEqual(self.run_tool("--ueberschreiben"), 0, self.report())
                    manifest = json.loads((self.target / "intern" / "Versandmanifest.json").read_text())
                    hashes = {a["quelle"]: a["sha256_quelle"] for a in manifest["anlagen"]}
                    self.assertEqual(hashes[source.name], hashlib.sha256(raw).hexdigest())
                    self.assertEqual(hashes[mail.name], hashlib.sha256(mail.read_bytes()).hexdigest())
                    self.assertIn("nur CRLF nach LF normalisiert", self.report())
                    self.assertIn(hashlib.sha256(original).hexdigest(), self.report())
                    self.assertEqual(source.read_bytes(), raw)

    def test_rfc822_missing_and_changed_message_stop(self) -> None:
        original = b"Subject: Original\nContent-Type: text/plain\n\nUnveraenderter Inhalt.\n"
        source = self.source / "Anlage_K2_Original.eml"
        self.rfc822_mail(original)
        self.assertEqual(self.run_tool(), 3)
        self.assertIn("E-Mail-Anhang Original.eml", self.report())
        source.write_bytes(original)
        for changed in (original.replace(b"Original", b"Andere Nachricht"),
                        original.replace(b"Inhalt", b"Text"),
                        original.replace(b"Subject: ", b"Subject:  "),
                        original.replace(b"\n", b"\r"), original + b"\n"):
            with self.subTest(payload=changed):
                self.rfc822_mail(changed)
                self.assertEqual(self.run_tool("--ueberschreiben"), 3)
                self.assertIn("E-Mail-Anhang Original.eml", self.report())

    def test_rfc822_nested_attachments_remain_checked(self) -> None:
        nested = EmailMessage()
        nested["Subject"] = "Original mit Anlage"
        nested.set_content("Anbei der Vertrag.")
        attachment = self.source / "Anlage_K3_Vertrag.pdf"
        write_pdf(attachment, "Vertrag", 1)
        original = attachment.read_bytes()
        nested.add_attachment(original, maintype="application", subtype="pdf", filename="Vertrag.pdf")
        nested_raw = nested.as_bytes()
        mail = self.rfc822_mail(nested_raw)
        (self.source / "Anlage_K2_Original.eml").write_bytes(nested_raw)
        parsed = BytesParser(policy=policy.default).parsebytes(mail.read_bytes())
        parts = list(self.tool.email_anhaenge(parsed))
        self.assertEqual([p.get_filename() for p in parts], ["Original.eml", "Vertrag.pdf"])
        self.assertIsInstance(parts[0].get_payload(), list)
        self.assertIsNone(parts[0].get_payload(decode=True))
        self.assertEqual(self.run_tool(), 0)
        attachment.unlink()
        self.assertEqual(self.run_tool("--ueberschreiben"), 3)
        self.assertIn("E-Mail-Anhang Vertrag.pdf", self.report())
        write_pdf(attachment, "Geaenderter Vertrag", 1)
        self.assertEqual(self.run_tool("--ueberschreiben"), 3)
        self.assertIn("E-Mail-Anhang Vertrag.pdf", self.report())

    def test_two_rfc822_levels_preserve_payloads_and_audit_inner_sources(self) -> None:
        attachment = self.source / "Anlage_K4_Vertrag.pdf"
        write_pdf(attachment, "Innerer Vertrag", 1)
        pdf_raw = attachment.read_bytes()
        inner = EmailMessage()
        inner["Subject"] = "Innere Nachricht"
        inner.set_content("Anbei der innere Vertrag.")
        inner.add_attachment(pdf_raw, maintype="application", subtype="pdf", filename="Vertrag.pdf")
        inner.set_boundary("inner-pdf-boundary")
        inner_raw = inner.as_bytes()
        inner_source = self.source / "Anlage_K3_Innere_Nachricht.eml"
        inner_source.write_bytes(inner_raw)
        middle_source = self.source / "Anlage_K2_Original.eml"
        outer_source = self.source / "Anlage_K1_Weiterleitung.eml"

        for outer_cte in ("7bit", "8bit", "binary"):
            for inner_cte in ("7bit", "8bit", "binary"):
                with self.subTest(outer_encoding=outer_cte, inner_encoding=inner_cte):
                    middle = EmailMessage()
                    middle["Subject"] = "Erste Weiterleitung"
                    middle.set_content("Anbei die innere Nachricht.")
                    middle.add_attachment(inner, filename="Inner.eml", cte=inner_cte)
                    middle.set_boundary("middle-message-boundary")
                    middle_raw = middle.as_bytes()
                    middle_source.write_bytes(middle_raw)
                    outer = EmailMessage()
                    outer["Subject"] = "Zweite Weiterleitung"
                    outer.set_content("Anbei die erste Weiterleitung.")
                    outer.add_attachment(middle, filename="Middle.eml", cte=outer_cte)
                    outer.set_boundary("outer-message-boundary")
                    outer_raw = outer.as_bytes()
                    outer_source.write_bytes(outer_raw)
                    parsed = BytesParser(policy=policy.default).parsebytes(outer_raw)
                    parts = list(self.tool.email_anhaenge(parsed))
                    self.assertEqual([p.get_filename() for p in parts],
                                     ["Middle.eml", "Inner.eml", "Vertrag.pdf"])
                    payloads = self.tool.email_rfc822_rohpayloads(parsed, outer_raw)
                    self.assertEqual(set(payloads), {id(parts[0]), id(parts[1])})
                    self.assertEqual(payloads[id(parts[0])], middle_raw)
                    self.assertEqual(payloads[id(parts[1])], inner_raw)
                    self.assertEqual(self.run_tool("--ueberschreiben"), 0, self.report())

        inner_source.unlink()
        self.assertEqual(self.run_tool("--ueberschreiben"), 3)
        self.assertIn("E-Mail-Anhang Inner.eml ist nicht", self.report())
        for changed in (inner_raw.replace(b"Subject: Innere Nachricht", b"Subject: Andere Nachricht"),
                        inner_raw.replace(b"Anbei der innere Vertrag.", b"Anbei ein anderer Vertrag.")):
            with self.subTest(changed_inner_message=changed):
                inner_source.write_bytes(changed)
                self.assertEqual(self.run_tool("--ueberschreiben"), 3)
                self.assertIn("E-Mail-Anhang Inner.eml ist nicht", self.report())
        inner_source.write_bytes(inner_raw)
        attachment.unlink()
        self.assertEqual(self.run_tool("--ueberschreiben"), 3)
        self.assertIn("E-Mail-Anhang Vertrag.pdf ist nicht", self.report())
        write_pdf(attachment, "Geaenderter innerer Vertrag", 1)
        self.assertEqual(self.run_tool("--ueberschreiben"), 3)
        self.assertIn("E-Mail-Anhang Vertrag.pdf ist nicht", self.report())
        attachment.write_bytes(pdf_raw)
        self.assertEqual(self.run_tool("--ueberschreiben"), 0, self.report())

    def test_rfc822_malformed_boundary_stops_without_aborting(self) -> None:
        original = b"Subject: Original\n\nUnveraendert.\n"
        source = self.source / "Anlage_K2_Original.eml"
        source.write_bytes(original)
        for boundary in (b"caf\xc3\xa9", b"caf\xff"):
            with self.subTest(boundary=boundary):
                mail = self.rfc822_mail(original)
                raw = mail.read_bytes().replace(b"outer-boundary", boundary)
                mail.write_bytes(raw)
                parsed = BytesParser(policy=policy.default).parsebytes(raw)
                self.assertEqual(self.tool.email_rfc822_rohpayloads(parsed, raw), {})
                self.assertEqual(self.run_tool("--ueberschreiben"), 3)
                self.assertIn("Fehlerhafte MIME-Struktur", self.report())

    def test_rfc822_unsupported_transfer_encoding_stops(self) -> None:
        original = b"Subject: Original\n\nUnveraendert.\n"
        (self.source / "Anlage_K2_Original.eml").write_bytes(original)
        mail = self.rfc822_mail(original)
        mail.write_bytes(mail.read_bytes().replace(b"Content-Transfer-Encoding: 8bit",
                                                  b"Content-Transfer-Encoding: x-unknown"))
        self.assertEqual(self.run_tool(), 3)
        self.assertIn("E-Mail-Anhang Original.eml", self.report())

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
