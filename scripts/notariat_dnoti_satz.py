#!/usr/bin/env python3
"""Setzt eigenständig lesbare DNotI-Anfragen auf notariellem Briefpapier.

Die Schreiben sind fiktive Aktenstücke. Die inhaltliche Fallgestaltung wird
unverändert aus JSON übernommen; dieses Modul erzeugt keine Rechtsauskunft.
"""

from __future__ import annotations

import argparse
from functools import partial
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import tempfile
from xml.sax.saxutils import escape

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    BaseDocTemplate, Frame, KeepTogether, PageTemplate, Paragraph, Spacer,
)


SENDER_NAME = "Dr. Lennox Hieronymus von Tannried-Eichenau"
SENDER_OFFICE = "Notar in Berlin"
SENDER_ADDRESS = "Kastanienallee 74 · 10435 Berlin"
SENDER_CONTACT = "Telefon 030 / 555 018 70 · post@notar-tannried.example"
RECIPIENT = ("Deutsches Notarinstitut (DNotI)", "Gerberstraße 19", "97070 Würzburg")
FOREST = colors.HexColor("#173F39")
GOLD = colors.HexColor("#9C875E")
MUTED = colors.HexColor("#59615D")
LEFT, RIGHT, BOTTOM = 62.0, 57.0, 78.0
WIDTH, HEIGHT = A4
TEXT_WIDTH = WIDTH - LEFT - RIGHT
FONT_NAMES = ("DNotI-Times", "DNotI-Times-Bold", "DNotI-Times-Italic", "DNotI-Times-BoldItalic")


def register_fonts() -> None:
    """Lädt nur echte Times-New-Roman-TTFs aus vorhandenen Installationen."""
    if all(name in pdfmetrics.getRegisteredFontNames() for name in FONT_NAMES):
        return
    directories = []
    for key in ("DNOTI_FONT_DIR", "UFERWERK_FONT_DIR", "AKTEN_FONT_DIR"):
        if os.environ.get(key):
            directories.append(Path(os.environ[key]).expanduser())
    directories.extend((
        Path("/System/Library/Fonts/Supplemental"),
        Path("/usr/share/fonts/truetype/msttcorefonts"),
        Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts",
    ))
    filenames = (
        ("Times New Roman.ttf", "times.ttf"),
        ("Times New Roman Bold.ttf", "timesbd.ttf"),
        ("Times New Roman Italic.ttf", "timesi.ttf"),
        ("Times New Roman Bold Italic.ttf", "timesbi.ttf"),
    )
    for name, aliases in zip(FONT_NAMES, filenames):
        source = next((directory / alias for directory in directories for alias in aliases
                       if (directory / alias).is_file()), None)
        if source is None:
            raise RuntimeError("Lizenzierte Times-New-Roman-TTFs fehlen; DNOTI_FONT_DIR setzen.")
        font = TTFont(name, str(source))
        face_name = font.face.name.decode("latin1", errors="replace")
        if not re.search(r"times.?new.?roman", face_name, re.I):
            raise RuntimeError(f"Die Schrift ist keine Times New Roman: {source.name}")
        pdfmetrics.registerFont(font)
    pdfmetrics.registerFontFamily(FONT_NAMES[0], normal=FONT_NAMES[0], bold=FONT_NAMES[1],
                                 italic=FONT_NAMES[2], boldItalic=FONT_NAMES[3])


def plain(value: str) -> str:
    # Diese Bindestriche sind beim Kopieren aus PDF weniger zuverlässig.
    return str(value).replace("\u2011", "-").replace("\u00ad", "")


def markup(value: str) -> str:
    return escape(plain(value)).replace("\n", "<br/>")


class NumberedCanvas(canvas.Canvas):
    """Zählt die Seiten ohne zweifachen Umbruch des Dokumentstroms."""

    def __init__(self, *args, **kwargs):
        kwargs["invariant"] = 1
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        count = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.saveState()
            self.setFont(FONT_NAMES[0], 8.5)
            self.setFillColor(MUTED)
            self.drawRightString(WIDTH - RIGHT, 39,
                                 f"Seite {self._pageNumber} von {count}")
            self.restoreState()
            super().showPage()
        super().save()


def _letterhead(c, doc, *, first: bool, record: dict):
    c.saveState()
    if first:
        c.setFillColor(FOREST)
        c.setFont(FONT_NAMES[1], 27)
        c.drawString(LEFT, 786, "LH")
        c.setStrokeColor(GOLD)
        c.setLineWidth(0.65)
        c.line(106, 778, 106, 817)
        c.setFont(FONT_NAMES[0], 15)
        c.drawString(119, 804, SENDER_NAME)
        c.setFont(FONT_NAMES[0], 10)
        c.drawString(120, 784, SENDER_OFFICE.upper())
        c.setFillColor(MUTED)
        c.setFont(FONT_NAMES[0], 8)
        c.drawString(LEFT, 734, "Notar Dr. von Tannried-Eichenau · " + SENDER_ADDRESS)
        c.setFillColor(colors.black)
        c.setFont(FONT_NAMES[0], 11)
        for i, line in enumerate(RECIPIENT):
            c.drawString(LEFT, 709 - i * 15, line)
        c.setFont(FONT_NAMES[0], 9.5)
        c.drawRightString(WIDTH - RIGHT, 709, "Berlin, " + str(record.get("date", "6. November 2026")))
        c.setFillColor(MUTED)
        c.setFont(FONT_NAMES[0], 8.5)
        c.drawRightString(WIDTH - RIGHT, 687, "Unser Zeichen: " + str(record.get("reference", "DNotI / Auslandsbeteiligung")))
        c.drawRightString(WIDTH - RIGHT, 673, "Fachkollegiale Anfrage")
    else:
        c.setFillColor(FOREST)
        c.setFont(FONT_NAMES[0], 9)
        c.drawString(LEFT, 806, "NOTAR DR. VON TANNRIED-EICHENAU")
        c.setFillColor(MUTED)
        c.setFont(FONT_NAMES[0], 8.5)
        c.drawRightString(WIDTH - RIGHT, 806, str(record.get("reference", "DNotI-Anfrage")))
        c.setStrokeColor(GOLD)
        c.setLineWidth(0.45)
        c.line(LEFT, 791, WIDTH - RIGHT, 791)
    c.setStrokeColor(colors.HexColor("#D4D7D3"))
    c.setLineWidth(0.4)
    c.line(LEFT, 57, WIDTH - RIGHT, 57)
    c.setFillColor(MUTED)
    c.setFont(FONT_NAMES[0], 8.5)
    c.drawString(LEFT, 39, SENDER_NAME + " · " + SENDER_OFFICE)
    c.setFont(FONT_NAMES[0], 8)
    c.drawString(LEFT, 25, SENDER_ADDRESS + " · " + SENDER_CONTACT)
    c.restoreState()


def _paragraphs(values):
    if isinstance(values, str):
        return [part.strip() for part in re.split(r"\n\s*\n", values) if part.strip()]
    if isinstance(values, list) and all(isinstance(value, str) for value in values):
        return [value for value in values if value.strip()]
    raise ValueError("Absätze müssen Text oder eine Liste von Textabsätzen sein.")


def render_request(record: dict, output: Path) -> dict:
    """Erzeugt genau das angegebene Anfrage-PDF und meldet tatsächliche Kennzahlen."""
    register_fonts()
    output = Path(output)
    if output.suffix.lower() != ".pdf":
        raise ValueError("Das Ausgabeziel muss eine PDF-Datei sein.")
    sections = record.get("sections")
    if not isinstance(sections, list) or not sections:
        raise ValueError("Eine vollständige Anfrage benötigt Abschnitte.")
    body = ParagraphStyle("DNotI-Fließtext", fontName=FONT_NAMES[0], fontSize=11,
        leading=14.6, alignment=TA_JUSTIFY, spaceAfter=8.0, allowWidows=0,
        allowOrphans=0, splitLongWords=True, hyphenationLang="de_DE")
    heading = ParagraphStyle("DNotI-Abschnitt", parent=body, fontName=FONT_NAMES[1],
        fontSize=11, leading=14.6, alignment=TA_LEFT, spaceBefore=11,
        spaceAfter=6, keepWithNext=True)
    subject = ParagraphStyle("DNotI-Betreff", parent=heading, fontSize=12,
        leading=15.6, spaceBefore=0, spaceAfter=14)
    formal = ParagraphStyle("DNotI-Formaler-Text", parent=body, alignment=TA_LEFT)
    source_style = ParagraphStyle("DNotI-Quellennachweis", parent=formal,
        fontSize=9, leading=12, spaceAfter=6)
    story = [Paragraph(markup(record.get("subject") or record.get("title") or "Anfrage zur Auslandsvertretung"), subject)]
    salutation = record.get("salutation", "Sehr geehrte Damen und Herren,\nsehr geehrte Kolleginnen und Kollegen,")
    story.extend((Paragraph(markup(salutation), formal), Spacer(1, 3)))
    for paragraph in _paragraphs(record.get("introduction", [])):
        story.append(Paragraph(markup(paragraph), body))
    top_level = 0
    for section in sections:
        title = section.get("heading", "")
        match = re.match(r"^(\d+)(?:\.\d+)*\.?\s+\S", title)
        if not match:
            raise ValueError("Abschnittsüberschriften benötigen eine dezimale Nummer: " + title)
        top_level = max(top_level, int(match[1]))
        story.append(Paragraph(markup(title), heading))
        for paragraph in _paragraphs(section.get("paragraphs", [])):
            story.append(Paragraph(markup(paragraph), body))
    closing = record.get("closing", "Mit verbindlichem Dank und kollegialer Hochachtung")
    if isinstance(closing, dict):
        closing = closing.get("greeting", "Mit kollegialer Hochachtung")
    closing_parts = _paragraphs(closing)
    signature = [Spacer(1, 8)]
    for paragraph in closing_parts:
        signature.append(Paragraph(markup(paragraph), formal))
    signature.append(Spacer(1, 9))
    if not any(SENDER_NAME in paragraph for paragraph in closing_parts):
        signature.extend((Paragraph(markup(SENDER_NAME), formal),
                          Paragraph("Notar", formal)))
    story.append(KeepTogether(signature))
    attachments = record.get("attachments", [])
    if attachments:
        top_level += 1
        story.append(Paragraph(f"{top_level} Anlagenverzeichnis", heading))
        for i, item in enumerate(attachments, 1):
            text = item if isinstance(item, str) else item.get("description", item.get("title", ""))
            story.append(Paragraph(markup(f"{i}. {text}"), source_style))
    sources = record.get("sources", [])
    if sources:
        top_level += 1
        story.append(Paragraph(f"{top_level} Nachweise zu den angesprochenen Prüfungsfragen", heading))
        for i, source in enumerate(sources, 1):
            if isinstance(source, str):
                story.append(Paragraph(markup(source), source_style))
                continue
            label = source.get("label") or source.get("citation") or source.get("title") or f"Quelle {i}"
            url = source.get("url", "")
            if url and not url.startswith(("https://", "http://")):
                raise ValueError("Quellenlinks müssen HTTP(S)-Adressen sein.")
            text = markup(label)
            if url:
                text = f'<link href="{escape(url, {chr(34): "&quot;"})}" color="#173F39">{text}</link>'
            story.append(Paragraph(text, source_style))
    output.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".dnoti-", suffix=".pdf", dir=output.parent)
    os.close(fd)
    temporary = Path(temporary)
    try:
        document = BaseDocTemplate(str(temporary), pagesize=A4, leftMargin=LEFT,
            rightMargin=RIGHT, topMargin=72, bottomMargin=BOTTOM,
            title=record.get("title", record.get("subject", "Notarielle Anfrage")),
            author="Notar " + SENDER_NAME, subject=record.get("subject", "DNotI-Anfrage"))
        first = Frame(LEFT, BOTTOM, TEXT_WIDTH, 627 - BOTTOM, id="Erste-Seite",
                      leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        following = Frame(LEFT, BOTTOM, TEXT_WIDTH, 773 - BOTTOM, id="Fortsetzung",
                          leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        document.addPageTemplates((
            PageTemplate(id="Erste-Seite", frames=[first], autoNextPageTemplate="Fortsetzung",
                         onPage=partial(_letterhead, first=True, record=record)),
            PageTemplate(id="Fortsetzung", frames=[following],
                         onPage=partial(_letterhead, first=False, record=record)),
        ))
        document.build(story, canvasmaker=NumberedCanvas)
        reader = PdfReader(temporary)
        if not reader.pages or any(not (p.extract_text() or "").strip() for p in reader.pages):
            raise ValueError("Die Anfrage enthält keine oder eine leere PDF-Seite.")
        pages = len(reader.pages)
        characters = sum(len(p.extract_text() or "") for p in reader.pages)
        data = temporary.read_bytes()
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    return {"output": str(output), "pages": pages, "text_characters": characters,
            "sha256": sha256(data).hexdigest(), "bytes": len(data)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(render_request(json.loads(args.input.read_text(encoding="utf-8")), args.output),
                     ensure_ascii=False, indent=2))
