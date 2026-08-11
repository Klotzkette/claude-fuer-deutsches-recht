#!/usr/bin/env python3
"""Verbindlicher zweisprachiger Hinweis fuer alle Testakten-Artefakte."""

from __future__ import annotations

import io
import re


NOTICE_FILENAME = "README.txt"
NOTICE_DE = (
    "Diese Testakte wurde mit KI generiert und ist ein Experiment. "
    "Benutzung auf eigene Verantwortung und eigene Gefahr."
)
NOTICE_EN = (
    "This test case file was generated with AI and is an experiment. "
    "Use at your own responsibility and risk."
)
NOTICE_TEXT = (
    "HINWEIS / NOTICE\n"
    "=================\n\n"
    f"{NOTICE_DE}\n\n"
    f"{NOTICE_EN}\n"
)
NOTICE_BYTES = NOTICE_TEXT.encode("utf-8")

TEAL = "#01696F"
MUTED = "#6B6A66"
SURFACE = "#F7F6F2"


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


NORMALIZED_NOTICE_DE = normalize_text(NOTICE_DE)
NORMALIZED_NOTICE_EN = normalize_text(NOTICE_EN)
PDF_MARKER_DE = b"Diese Testakte wurde mit KI generiert"
PDF_MARKER_EN = b"This test case file was generated with AI"


def pdf_notice_marker_counts(reader) -> tuple[int, int]:
    """Zaehlt die stabilen Marker direkt in den Seitenstroemen."""
    de_count = 0
    en_count = 0
    for page in reader.pages:
        contents = page.get_contents()
        if contents is None:
            continue
        raw = contents.get_data()
        de_count += raw.count(PDF_MARKER_DE)
        en_count += raw.count(PDF_MARKER_EN)
    return de_count, en_count


def notice_pdf_bytes(testakte_name: str) -> bytes:
    """Erzeugt eine reproduzierbare A4-Hinweisseite fuer eine Testakte."""
    from reportlab.lib.colors import HexColor, black
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.pdfgen import canvas

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4, invariant=1)
    width, height = A4
    pdf.setTitle(f"Hinweis zur Testakte {testakte_name}")
    pdf.setAuthor("Kanzleiakte")

    pdf.setFillColor(HexColor(SURFACE))
    pdf.roundRect(2 * cm, height - 13.2 * cm, width - 4 * cm, 8.8 * cm, 6, fill=1, stroke=0)
    pdf.setFillColor(HexColor(TEAL))
    pdf.rect(2 * cm, height - 13.2 * cm, 0.18 * cm, 8.8 * cm, fill=1, stroke=0)

    x = 2.8 * cm
    pdf.setFillColor(HexColor(TEAL))
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(x, height - 5.5 * cm, "Hinweis / Notice")

    pdf.setFillColor(HexColor(MUTED))
    pdf.setFont("Helvetica", 8)
    pdf.drawString(x, height - 6.2 * cm, f"Akte: {testakte_name}")

    pdf.setFillColor(black)
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(x, height - 7.4 * cm, "Deutsch")
    pdf.setFont("Helvetica", 11)
    pdf.drawString(x, height - 8.1 * cm, "Diese Testakte wurde mit KI generiert und ist ein Experiment.")
    pdf.drawString(x, height - 8.8 * cm, "Benutzung auf eigene Verantwortung und eigene Gefahr.")

    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(x, height - 10.0 * cm, "English")
    pdf.setFont("Helvetica", 11)
    pdf.drawString(x, height - 10.7 * cm, "This test case file was generated with AI and is an experiment.")
    pdf.drawString(x, height - 11.4 * cm, "Use at your own responsibility and risk.")

    pdf.showPage()
    pdf.save()
    return buffer.getvalue()


def add_notice_page(writer, testakte_name: str) -> None:
    """Fuegt genau eine erzeugte Hinweisseite in einen PDF-Writer ein."""
    from pypdf import PdfReader

    pages = list(PdfReader(io.BytesIO(notice_pdf_bytes(testakte_name))).pages)
    if len(pages) != 1:
        raise ValueError("Hinweis-PDF muss genau eine Seite enthalten")
    writer.add_page(pages[0])


def prepend_notice_page(data: bytes, testakte_name: str) -> bytes:
    """Stellt einem vorhandenen PDF genau eine Hinweisseite voran."""
    from pypdf import PdfReader, PdfWriter

    reader = PdfReader(io.BytesIO(data))
    pages = list(reader.pages)
    if not pages:
        raise ValueError("PDF ohne Seite kann keinen Testakten-Hinweis erhalten")
    writer = PdfWriter()
    add_notice_page(writer, testakte_name)
    for page in pages:
        writer.add_page(page)
    writer.add_metadata(
        {
            "/Title": f"Akte {testakte_name}",
            "/Author": "Kanzleiakte",
            "/Subject": "Testakten-Hinweis und Aktenstueck",
        }
    )
    output = io.BytesIO()
    writer.write(output)
    return output.getvalue()


def ensure_notice_page(data: bytes, testakte_name: str) -> tuple[bytes, bool]:
    """Ergaenzt den Hinweis nur, wenn bislang keinerlei Hinweis vorhanden ist."""
    from pypdf import PdfReader

    errors = pdf_notice_errors(data, exactly_once=True)
    if not errors:
        return data, False

    reader = PdfReader(io.BytesIO(data))
    de_count, en_count = pdf_notice_marker_counts(reader)
    if de_count == 0 and en_count == 0:
        return prepend_notice_page(data, testakte_name), True
    raise ValueError("vorhandener Testakten-Hinweis ist unvollstaendig oder mehrfach enthalten")


def pdf_notice_errors(data: bytes, *, exactly_once: bool) -> list[str]:
    """Prueft Position, Wortlaut und auf Wunsch Einmaligkeit des Hinweises."""
    from pypdf import PdfReader

    try:
        reader = PdfReader(io.BytesIO(data))
    except Exception as exc:
        return [f"PDF nicht lesbar: {exc}"]
    if len(reader.pages) == 0:
        return ["PDF enthaelt keine Seite"]

    first_page = normalize_text(reader.pages[0].extract_text() or "")
    errors: list[str] = []
    if NORMALIZED_NOTICE_DE not in first_page:
        errors.append("deutscher Hinweis fehlt auf der ersten Seite")
    if NORMALIZED_NOTICE_EN not in first_page:
        errors.append("englischer Hinweis fehlt auf der ersten Seite")
    if exactly_once:
        de_count, en_count = pdf_notice_marker_counts(reader)
        if de_count != 1:
            errors.append("deutscher Hinweis steht nicht genau einmal im PDF")
        if en_count != 1:
            errors.append("englischer Hinweis steht nicht genau einmal im PDF")
    return errors


def notice_text_errors(data: bytes) -> list[str]:
    """Prueft die README.txt eines Originalformat-ZIPs bytegenau."""
    if data == NOTICE_BYTES:
        return []
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return ["README.txt ist nicht UTF-8-kodiert"]
    errors: list[str] = []
    normalized = normalize_text(text)
    if NORMALIZED_NOTICE_DE not in normalized:
        errors.append("deutscher Hinweis fehlt in README.txt")
    if NORMALIZED_NOTICE_EN not in normalized:
        errors.append("englischer Hinweis fehlt in README.txt")
    if not errors:
        errors.append("README.txt weicht vom verbindlichen Wortlaut ab")
    return errors
