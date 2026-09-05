#!/usr/bin/env python3
"""Hinweise neben Downloads und in ZIPs; PDF-Akten bleiben ohne Vorspruch."""

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
NOTICE_MARKDOWN = f"> {NOTICE_DE}\n>\n> {NOTICE_EN}"

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
    """Bildet das alte Seitenformat ausschließlich für Migrationstests nach."""
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


def _has_notice(page) -> bool:
    contents = page.get_contents()
    raw = contents.get_data() if contents is not None else b""
    if PDF_MARKER_DE in raw or PDF_MARKER_EN in raw:
        return True
    text = normalize_text(page.extract_text() or "")
    return (
        "Diese Testakte wurde mit KI generiert" in text
        or "This test case file was generated with AI" in text
    )


def without_notice_pages(data: bytes) -> bytes:
    """Entfernt nur eindeutig erkannte alte Hinweisblätter, nie Mischseiten."""
    from pypdf import PdfReader, PdfWriter

    reader = PdfReader(io.BytesIO(data))
    if not reader.pages:
        raise ValueError("PDF enthält keine Seite")
    kept = []
    for page in reader.pages:
        if not _has_notice(page):
            kept.append(page)
            continue
        text = normalize_text(page.extract_text() or "")
        legacy = (
            r"Hinweis / Notice Akte: \S+ Deutsch "
            + re.escape(NORMALIZED_NOTICE_DE)
            + r" English " + re.escape(NORMALIZED_NOTICE_EN)
        )
        if re.fullmatch(legacy, text) is None:
            raise ValueError("Hinweis und Akteninhalt auf derselben Seite: manuelle Prüfung erforderlich")
    if len(kept) == len(reader.pages):
        return data
    if not kept:
        raise ValueError("PDF enthält außer dem Hinweis keine Aktenunterlage")
    writer = PdfWriter()
    for page in kept:
        writer.add_page(page)
    if reader.metadata:
        writer.add_metadata({str(k): str(v) for k, v in reader.metadata.items() if v is not None})
    output = io.BytesIO()
    writer.write(output)
    return output.getvalue()


def pdf_content_errors(data: bytes) -> list[str]:
    """Prüft lesbaren Akteninhalt ohne eingebetteten Herkunftsvorspruch."""
    from pypdf import PdfReader

    try:
        reader = PdfReader(io.BytesIO(data))
    except Exception as exc:
        return [f"PDF nicht lesbar: {exc}"]
    if len(reader.pages) == 0:
        return ["PDF enthaelt keine Seite"]

    errors: list[str] = []
    for number, page in enumerate(reader.pages, start=1):
        if _has_notice(page):
            errors.append(f"Seite {number}: Herkunftshinweis gehört an den Download und in README.txt")
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
