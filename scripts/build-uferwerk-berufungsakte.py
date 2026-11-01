#!/usr/bin/env python3
"""Baut die ausdrücklich nur als PDF-ZIP bestellte Uferwerk-Berufungsakte.

Die drei redaktionellen JSON-Dateien sind die reproduzierbaren Satzquellen.
Sie werden weder dem installierten Plugin noch dem Teilnehmerpaket beigelegt.
Times New Roman 11 pt ist die Grundschrift; Briefmarken und Tabellen sind
aus Gründen ihrer jeweiligen Funktion gesondert gestaltet.
"""

import argparse
from datetime import date
import hashlib
import json
import os
from pathlib import Path
import re
import unicodedata
from xml.sax.saxutils import escape
import zipfile

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, LongTable,
    TableStyle, KeepTogether, PageBreak,
)
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "arbeitsrecht-kuendigungsschutzklagewerkstatt"
FILENAME = "testakte-arbeitsrecht-muster-uferwerk-berufung-einzelpdfs.zip"
STAMP = (2026, 10, 30, 12, 0, 0)
NOTICE = (
    "Diese Testakte wurde mit KI generiert und ist ein Experiment. "
    "Benutzung auf eigene Verantwortung und eigene Gefahr.\n\n"
    "This test case file was generated with AI and is an experiment. "
    "Use at your own responsibility and risk.\n\n"
)
SOURCES = [ROOT / "scripts/data" / ("uferwerk-" + part + ".json")
           for part in ("vorgeschichte", "prozess", "nachurteil")]

BRANDS = {
    "employee_firm": {"title": "FALKENHORST & FLOW", "subtitle": "Rechtsanwältin Dr. Johanna Falkenhorst",
        "address": "Seestraße 18 · 78464 Konstanz", "contact": "j.falkenhorst@falkenhorst-flow.example",
        "color": "#143E4A", "accent": "#D66D58", "tag": "ARBEITSRECHT · PROZESSFÜHRUNG"},
    "employer_firm": {"title": "KNIGGE / NORTH", "subtitle": "Rechtsanwalt Caspar Finley von Knigge",
        "address": "Robert-Bosch-Straße 6 · 78467 Konstanz", "contact": "kanzlei@knigge-north.example",
        "color": "#252844", "accent": "#A5783C", "tag": "UNTERNEHMEN · ARBEITSRECHT"},
    "employer": {"title": "uferwerk", "subtitle": "VERLAG · IDEEN AM SEE",
        "address": "Hafenstraße 24 · 78462 Konstanz", "contact": "personal@uferwerk.example",
        "color": "#24615D", "accent": "#C5AA66", "tag": "UFERWERK VERLAG GMBH"},
    "court": {"title": "Arbeitsgericht Villingen-Schwenningen", "subtitle": "Kammern Radolfzell",
        "address": "Seetorstraße 5 · 78315 Radolfzell", "contact": "",
        "color": "#273D55", "accent": "#8793A0", "tag": "7. KAMMER"},
    "agency": {"title": "Schriftstück der Leistungsverwaltung", "subtitle": "",
        "address": "", "contact": "", "color": "#3C5061", "accent": "#97A8B4", "tag": "LEISTUNG · VERFAHREN"},
    "client": {"title": "Lisa Muster", "subtitle": "Persönliche Unterlagen und Korrespondenz",
        "address": "Rheinsteig 8 · 78462 Konstanz", "contact": "lisa.muster@postfach.example",
        "color": "#6E5168", "accent": "#C5A2B8", "tag": ""},
    "neutral": {"title": "Muster ./. Uferwerk Verlag GmbH", "subtitle": "Unterlagen der Handakte",
        "address": "F26-041LM", "contact": "", "color": "#334554", "accent": "#91A0A8", "tag": ""},
}


def text(value):
    return escape(str(value)).replace("\n", "<br/>").replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", "-")


def slug(value):
    value = value.replace("ß", "ss")
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_")[:100]


def register_fonts():
    configured = os.environ.get("UFERWERK_FONT_DIR")
    candidates = [Path(configured)] if configured else []
    candidates += [Path("/System/Library/Fonts/Supplemental"),
                   Path("/usr/share/fonts/truetype/msttcorefonts")]
    names = [("TNR", ("Times New Roman.ttf", "Times_New_Roman.ttf", "times.ttf")),
             ("TNR-Bold", ("Times New Roman Bold.ttf", "Times_New_Roman_Bold.ttf", "timesbd.ttf")),
             ("TNR-Italic", ("Times New Roman Italic.ttf", "Times_New_Roman_Italic.ttf", "timesi.ttf")),
             ("TNR-BoldItalic", ("Times New Roman Bold Italic.ttf", "Times_New_Roman_Bold_Italic.ttf", "timesbi.ttf"))]
    for family, filenames in names:
        path = next((directory / filename for directory in candidates for filename in filenames
                     if (directory / filename).is_file()), None)
        if path is None:
            raise RuntimeError("Times New Roman fehlt; UFERWERK_FONT_DIR auf lizenzierte TTF-Dateien setzen")
        pdfmetrics.registerFont(TTFont(family, str(path)))
    pdfmetrics.registerFontFamily("TNR", normal="TNR", bold="TNR-Bold", italic="TNR-Italic", boldItalic="TNR-BoldItalic")


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        self.doc_info = kwargs.pop("doc_info")
        super().__init__(*args, **kwargs)
        self.saved_states = []

    def showPage(self):
        self.saved_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        page_count = len(self.saved_states)
        for state in self.saved_states:
            self.__dict__.update(state)
            self.saveState()
            self.setStrokeColor(colors.HexColor("#CDD3D8"))
            self.setLineWidth(.4)
            self.line(55, 43, A4[0] - 55, 43)
            self.setFont("TNR", 8)
            self.setFillColor(colors.HexColor("#53616A"))
            self.drawString(55, 29, f"{self.doc_info['id']}  |  {self.doc_info.get('reference', '')[:65]}")
            self.drawRightString(A4[0] - 55, 29, f"Seite {self._pageNumber} von {page_count}")
            self.restoreState()
            super().showPage()
        super().save()


def brand_for(doc):
    brand = dict(BRANDS.get(doc["brand"], BRANDS["neutral"]))
    sender = doc.get("sender", "").split("\n")[0]
    if doc["brand"] == "client" and sender and "Lisa Muster" not in sender:
        brand.update(title=sender.split(" <")[0], subtitle="Korrespondenz und Unterlagen", address="", contact="")
    if doc["brand"] == "agency":
        if "Küstenklar" in sender:
            brand.update(title="KÜSTENKLAR", subtitle="Rechtsschutz AG · Leistungsabteilung Arbeitsrecht",
                         address="Postfach 1104 · 78401 Konstanz", contact="leistung@kuestenklar.example")
        elif "Agentur" in sender or "Arbeitsagentur" in sender:
            brand.update(title="Agentur für Arbeit Konstanz-Ravensburg", subtitle="Arbeitgeber-Service",
                         address="Standort Konstanz", contact="")
    if "Betriebsrat" in sender or sender.startswith("Cem Aydin"):
        brand["subtitle"] = "BETRIEBSRAT · UFERWERK VERLAG"
        brand["contact"] = "betriebsrat@uferwerk.example"
    return brand


def header(canv, document, item, brand):
    width, height = A4
    canv.saveState()
    primary = colors.HexColor(brand["color"])
    accent = colors.HexColor(brand["accent"])
    canv.setFillColor(primary)
    if document.page == 1:
        if item["brand"] == "court":
            canv.setFont("TNR-Bold", 16)
            canv.drawString(55, height - 54, brand["title"])
            canv.setFont("TNR", 14)
            canv.drawString(55, height - 74, brand["subtitle"])
        else:
            canv.setFont("Helvetica-Bold", 25 if item["brand"] == "employer" else 19)
            label = brand["title"]
            if pdfmetrics.stringWidth(label, "Helvetica-Bold", 19) > width - 110:
                canv.setFont("Helvetica-Bold", 15)
            canv.drawString(55, height - 57, label)
            canv.setFont("Helvetica", 8.5)
            canv.drawString(55, height - 76, brand["subtitle"])
        canv.setStrokeColor(accent)
        canv.setLineWidth(2.3 if item["brand"] != "court" else .8)
        canv.line(55, height - 94, width - 55, height - 94)
        canv.setFont("TNR", 8)
        canv.setFillColor(colors.HexColor("#59636D"))
        canv.drawString(55, height - 110, brand["address"])
        canv.drawRightString(width - 55, height - 110, brand["contact"])
        if item["brand"] in ("employee_firm", "employer_firm"):
            canv.setFillColor(accent)
            canv.rect(width - 62, height - 82, 7, 33, fill=1, stroke=0)
    else:
        canv.setFont("TNR-Bold", 10)
        canv.drawString(55, height - 42, brand["title"])
        canv.setFont("TNR", 9)
        canv.drawRightString(width - 55, height - 42, item["id"])
        canv.setStrokeColor(accent)
        canv.setLineWidth(.6)
        canv.line(55, height - 51, width - 55, height - 51)
    canv.restoreState()


def styles(brand):
    body = ParagraphStyle("body", fontName="TNR", fontSize=11, leading=13.5,
                          spaceAfter=6, allowWidows=0, allowOrphans=0, splitLongWords=True)
    return {
        "body": body,
        "small": ParagraphStyle("small", parent=body, fontSize=9.5, leading=12, spaceAfter=5),
        "date": ParagraphStyle("date", parent=body, alignment=TA_RIGHT, spaceAfter=13),
        "title": ParagraphStyle("title", parent=body, fontName="TNR-Bold", fontSize=14,
                                leading=17, spaceBefore=9, spaceAfter=12, keepWithNext=True,
                                textColor=colors.HexColor(brand["color"])),
        "section": ParagraphStyle("section", parent=body, fontName="TNR-Bold", fontSize=11,
                                  leading=14, spaceBefore=9, spaceAfter=7, keepWithNext=True),
        "cell": ParagraphStyle("cell", parent=body, fontSize=10, leading=12.5, spaceAfter=0),
        "th": ParagraphStyle("th", parent=body, fontName="TNR-Bold", fontSize=10,
                             leading=12.5, textColor=colors.white, spaceAfter=0),
    }


def make_table(table, sty, brand):
    headers, rows = table["headers"], table["rows"]
    if any(len(row) != len(headers) for row in rows):
        raise ValueError("Tabellenspalten stimmen nicht überein")
    def cell(value, style):
        formatted = text(value)
        # Ein Sozialdatum oder Jahr darf nie mitten in der Ziffernfolge
        # umbrechen; echte Wortgrenzen bleiben für schmale Tabellen erhalten.
        formatted = re.sub(r"(?<![\d.])\d{2}\.\d{2}\.\d{4}(?!\d)",
                           lambda match: "<nobr>" + match.group() + "</nobr>", formatted)
        formatted = re.sub(r"(?<![\d.>])(?:19|20)\d{2}(?![\d<])",
                           lambda match: "<nobr>" + match.group() + "</nobr>", formatted)
        return Paragraph(formatted, style)

    cells = [[cell(x, sty["th"]) for x in headers]]
    cells += [[cell(x, sty["cell"]) for x in row] for row in rows]
    width = A4[0] - 110
    ratios = table.get("widths")
    if ratios is None:
        if len(headers) == 2:
            ratios = [.31, .69]
        else:
            # Grobe Wortlängen liefern bei stark unterschiedlich langen Spalten
            # bessere Ergebnisse als gleich breite Felder.
            weights = [min(55, max(13, max(len(str(row[i])) for row in [headers] + rows) ** .65 * 4))
                       for i in range(len(headers))]
            ratios = [weight / sum(weights) for weight in weights]
    tbl = LongTable(cells, colWidths=[width * ratio / sum(ratios) for ratio in ratios],
                    repeatRows=1, hAlign="LEFT", splitByRow=1, splitInRow=1)
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(brand["color"])),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#F3F5F6"), colors.white]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LINEBELOW", (0, 0), (-1, 0), .7, colors.HexColor(brand["accent"])),
        ("LINEBELOW", (0, 1), (-1, -1), .25, colors.HexColor("#D5DBDF")),
    ]))
    return tbl


def build_pdf(item, output):
    brand = brand_for(item)
    sty = styles(brand)
    document = BaseDocTemplate(str(output), pagesize=A4,
                              title=item["title"], author=item.get("sender", "Klotzkette").split("\n")[0],
                              subject=item.get("subject", ""), creator="Uferwerk Akten-Satz", invariant=1,
                              pageCompression=1, allowSplitting=1)
    first_frame = Frame(55, 61, A4[0] - 110, A4[1] - 195, leftPadding=0, rightPadding=0,
                        topPadding=0, bottomPadding=0, id="first")
    later_frame = Frame(55, 61, A4[0] - 110, A4[1] - 130, leftPadding=0, rightPadding=0,
                        topPadding=0, bottomPadding=0, id="later")
    document.addPageTemplates([
        PageTemplate(id="First", frames=first_frame, onPage=lambda c, d: header(c, d, item, brand), autoNextPageTemplate="Later"),
        PageTemplate(id="Later", frames=later_frame, onPage=lambda c, d: header(c, d, item, brand)),
    ])
    story = []
    date_de = date.fromisoformat(item["date"]).strftime("%d.%m.%Y")
    if item.get("recipient") and item["kind"] != "email":
        story += [Paragraph(text(item["recipient"]), sty["body"]), Spacer(1, 8)]
    story += [Paragraph(date_de, sty["date"]),
              Paragraph(text(item["title"]), sty["title"])]
    if item.get("subject") and item["subject"] != item["title"]:
        story.append(Paragraph(text(item["subject"]), sty["section"]))
    if item.get("reference"):
        story += [Paragraph("Aktenzeichen / Bezug: " + text(item["reference"]), sty["small"]), Spacer(1, 8)]
    if item["kind"] == "email":
        story += [Paragraph("Von: " + text(item["sender"]), sty["small"]),
                  Paragraph("An: " + text(item["recipient"]), sty["small"]), Spacer(1, 8)]
    for i, section in enumerate(item["sections"]):
        if section.get("page_break") or i in item.get("page_break_before_sections", []):
            story.append(PageBreak())
        if section.get("heading"):
            story.append(Paragraph(text(section["heading"]), sty["section"]))
        for value in section.get("paragraphs", []):
            story.append(Paragraph(text(value), sty["body"]))
        if section.get("table"):
            story += [make_table(section["table"], sty, brand), Spacer(1, 12)]
    ending = []
    if item.get("signature"):
        ending += [Spacer(1, 9), Paragraph(text(item["signature"]), sty["body"])]
    if item.get("attachments"):
        ending += [Spacer(1, 5), Paragraph("Anlagen / Bezüge", sty["section"])]
        for attachment in item["attachments"]:
            ending.append(Paragraph(text(attachment), sty["small"]))
    if ending:
        # Keine eigene Seite allein für Signatur oder einzelne Anlagenkürzel.
        # Die letzte Textpassage bleibt mit dem vollständigen Schlussblock
        # zusammen, soweit dessen Umfang eine Seite nicht überschreitet.
        while story and isinstance(story[-1], Spacer):
            story.pop()
        tail = []
        if story and isinstance(story[-1], Paragraph):
            tail.insert(0, story.pop())
            if story and isinstance(story[-1], Paragraph):
                tail.insert(0, story.pop())
            if story and isinstance(story[-1], Paragraph) and story[-1].style.name == "section":
                tail.insert(0, story.pop())
        story.append(KeepTogether(tail + ending))
    document.build(story, canvasmaker=lambda *a, **kw: NumberedCanvas(*a, doc_info=item, **kw))


def load_documents():
    documents = []
    for source in SOURCES:
        documents.extend(json.loads(source.read_text(encoding="utf-8"))["documents"])
    ids = [item["id"] for item in documents]
    if len(ids) != len(set(ids)):
        raise ValueError("Doppelte Dokumentnummer")
    for item in documents:
        if item["brand"] not in BRANDS or not item.get("sections"):
            raise ValueError(item["id"] + ": Marke oder Inhalt fehlt")
        if date.fromisoformat(item["date"]) > date(2026, 10, 30):
            raise ValueError(item["id"] + ": Nach dem Aktenstichtag")
    return documents


def build(output, register_inventory=True):
    register_fonts()
    documents = load_documents()
    output.mkdir(parents=True, exist_ok=True)
    for path in output.glob("*.pdf"):
        raise ValueError("Satzordner enthält bereits PDFs: " + str(path))
    files = []
    for item in documents:
        filename = item["id"] + "_" + item["date"] + "_" + slug(item["title"]) + ".pdf"
        path = output / filename
        build_pdf(item, path)
        reader = PdfReader(path)
        extracted = "\n".join(page.extract_text() or "" for page in reader.pages)
        if "Diese Testakte wurde" in extracted or "Use at your own" in extracted:
            raise ValueError("Warntext gehört nicht in PDFs")
        files.append({"id": item["id"], "date": item["date"], "title": item["title"], "file": filename,
                      "pages": len(reader.pages), "characters": len(extracted),
                      "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    index_rows = [[file["id"], date.fromisoformat(file["date"]).strftime("%d.%m.%Y"), file["title"], str(file["pages"])]
                  for file in files]
    index = {"id": "00", "date": "2026-10-30", "kind": "memo", "brand": "employee_firm",
             "title": "Aktenverzeichnis", "sender": "FALKENHORST & FLOW", "recipient": "Handakte F26-041LM",
             "reference": "Muster ./. Uferwerk Verlag GmbH / 7 Ca 87/26",
             "subject": "Unterlagenstand 30. Oktober 2026",
             "sections": [{"paragraphs": [
                 "Die Akte umfasst die vorvertraglichen Unterlagen, das Arbeitsverhältnis, den Personalabbau, "
                 "das erstinstanzliche Verfahren und die Korrespondenz nach dem Urteil. Die Nummern V, P und N "
                 "bezeichnen die Ablageabschnitte Vorgeschichte, Prozess und Nachurteil. Sie sind keine gerichtlichen Anlagennummern.",
                 "Die Berufungsschrift und die zugehörige Ausgangskontrolle befinden sich im Abschnitt N. "
                 "Ein zweitinstanzliches Aktenzeichen ist noch nicht mitgeteilt. Der weitere Bearbeitungsauftrag "
                 "ergibt sich aus dem Mandat und der Korrespondenz. Abweichende Angaben in Schriftsätzen und "
                 "Zeugenaussagen werden in den jeweiligen Dokumenten wiedergegeben; dieses Verzeichnis bewertet sie nicht."]},
                 {"table": {"headers": ["Nr.", "Datum", "Dokument", "Seiten"], "rows": index_rows,
                             "widths": [.07, .16, .68, .09]}}]}
    index_file = output / "00_Aktenverzeichnis.pdf"
    build_pdf(index, index_file)
    index_pages = len(PdfReader(index_file).pages)
    readme = NOTICE + (
        "Muster gegen Uferwerk Verlag GmbH - Berufungswerkstatt\n"
        "Aktenstand: 30. Oktober 2026. Workshop: 12. November 2026.\n\n"
        f"{len(documents)} Aktenunterlagen und ein Aktenverzeichnis; insgesamt "
        f"{sum(file['pages'] for file in files) + index_pages} PDF-Seiten.\n"
        "Das Paket enthält ausschließlich PDFs und diese README.txt. Es enthält keine Berufungsbegründung.\n"
        "Die Berufungseinlegung ist innerhalb der erfundenen Fallgeschichte bereits dokumentiert.\n"
        "Sämtliche Parteien, Personen, Vorgänge und Kommunikationsdaten sind erfunden. Die Gerichtsnamen "
        "und Gerichtsanschriften dienen der realistischen Verfahrensdarstellung. Die Aktenzeichen gehören "
        "zur Fallfiktion; die Dokumente sind keine echten gerichtlichen oder anwaltlichen Erklärungen.\n"
        "Die reservierte Domain .example wird ausschließlich für erfundene Kontakte verwendet.\n"
        "Vorgeschichte (V), erste Instanz (P), Nachurteil und Berufungseinlegung (N). "
        "Das Aktenverzeichnis nennt alle Unterlagen mit Datum und Seitenzahl.\n"
        "Datumsangaben in Dateinamen bezeichnen das Ablagedatum; ein später übermittelter Ausdruck kann "
        "einen älteren Vorgang enthalten. Gerichtliche Anlagenkürzel stehen in den Schriftsätzen; "
        "sie sind vom Ablagekennzeichen der PDF-Dateien zu unterscheiden.\n"
        "Rechtsstand der Prompt-Begleitung: 1. November 2026; die Fallunterlagen bilden den jeweiligen "
        "historischen Dokumentstand ab. Prozessbehauptungen und Urteilsbegründungen sind selbst zu prüfen.\n"
    )
    archive_path = output.parent / FILENAME
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for filename, data in [("README.txt", readme.encode("utf-8"))] + [
                (path.name, path.read_bytes()) for path in [index_file] + [output / file["file"] for file in files]]:
            info = zipfile.ZipInfo(filename, STAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    inventory = {"schema_version": 1, "case": "muster-uferwerk-berufung", "cutoff": "2026-10-30",
                 "source_date": "2026-11-01", "format": "pdf-zip-only-user-request",
                 "documents": len(documents), "index_pages": index_pages,
                 "pages": sum(file["pages"] for file in files) + index_pages,
                 "pdf_files": len(documents) + 1, "archive": FILENAME,
                 "archive_sha256": hashlib.sha256(archive_path.read_bytes()).hexdigest(), "files": files,
                 "sources": [{"path": path.relative_to(ROOT).as_posix(),
                              "sha256": hashlib.sha256(path.read_bytes()).hexdigest()} for path in SOURCES]}
    if register_inventory:
        inventory_path = PLUGIN / "testakte/pruefung/uferwerk-bestand.json"
        inventory_path.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: inventory[key] for key in ("documents", "pdf_files", "pages", "archive_sha256")}, ensure_ascii=False))
    print(archive_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Leerer Satzordner für temporäre Einzel-PDFs")
    parser.add_argument("--no-register", action="store_true", help="Bestandsnachweis nicht aktualisieren")
    args = parser.parse_args()
    build(args.output, register_inventory=not args.no_register)
