"""Gattungsspezifischer Satz der Uferwerk-Akte, Grundschrift TNR 11 pt.

Kanzleischriftsatz, Gerichtsschreiben, Urteil, Niederschrift und Mailausdruck
haben eigene Satzspiegel. Die Wortmarken sind eigens gezeichnet; echte
Dienstsiegel, eingescannte Unterschriften oder Transportzertifikate werden
nicht verwendet. Archivalische V/P/N-Kennungen stehen im Aktenverzeichnis,
nicht als angebliche Anlagenbezeichnungen auf historischen Originalen.
"""

from datetime import date
import os
from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    BaseDocTemplate, Frame, KeepTogether, LongTable, PageBreak, PageTemplate,
    Paragraph, Spacer, Table, TableStyle,
)

PAGE_W, PAGE_H = A4
LEFT, RIGHT, BOTTOM = 70, 55, 69
WIDTH = PAGE_W - LEFT - RIGHT
INK = colors.HexColor("#17212A")
MUTED = colors.HexColor("#53616C")
PALE = colors.HexColor("#E4E8EA")
TEAL = colors.HexColor("#143E4A")
CORAL = colors.HexColor("#B46554")
NAVY = colors.HexColor("#22283B")
BRONZE = colors.HexColor("#96764E")
GREEN = colors.HexColor("#285D55")


def register_fonts():
    configured = os.environ.get("UFERWERK_FONT_DIR")
    candidates = [Path(configured)] if configured else []
    candidates += [Path("/System/Library/Fonts/Supplemental"),
                   Path("/usr/share/fonts/truetype/msttcorefonts")]
    fonts = {
        "TNR": ("Times New Roman.ttf", "Times_New_Roman.ttf", "times.ttf"),
        "TNR-Bold": ("Times New Roman Bold.ttf", "Times_New_Roman_Bold.ttf", "timesbd.ttf"),
        "TNR-Italic": ("Times New Roman Italic.ttf", "Times_New_Roman_Italic.ttf", "timesi.ttf"),
        "TNR-BoldItalic": ("Times New Roman Bold Italic.ttf", "Times_New_Roman_Bold_Italic.ttf", "timesbi.ttf"),
    }
    for name, alternatives in fonts.items():
        if name in pdfmetrics.getRegisteredFontNames():
            continue
        found = next((directory / filename for directory in candidates for filename in alternatives
                      if (directory / filename).is_file()), None)
        if found is None:
            raise RuntimeError("Lizenzierte Times-New-Roman-TTFs fehlen; UFERWERK_FONT_DIR setzen")
        pdfmetrics.registerFont(TTFont(name, str(found)))
    pdfmetrics.registerFontFamily("TNR", normal="TNR", bold="TNR-Bold", italic="TNR-Italic", boldItalic="TNR-BoldItalic")


def clean(value):
    return str(value).replace("\u2011", "-").replace("\u2013", "-").replace("\u2014", "-")


def rich(value):
    result = escape(clean(value)).replace("\n", "<br/>")
    if result.startswith("Beweis:"):
        result = "<b>Beweis:</b>" + result[len("Beweis:"):]
    result = re.sub(r"^((?:Frage|Antwort|Vorhalt)[^:]{0,100}:)", r"<b>\1</b>", result)
    for prefix in ("Frage des Gerichts:", "Antwort des Zeugen:", "Antwort der Zeugin:",
                   "Frage der Klägervertreterin:", "Frage des Beklagtenvertreters:"):
        if result.startswith(prefix):
            result = "<b>" + prefix + "</b>" + result[len(prefix):]
    return result


def address_lines(value):
    value = clean(value)
    if "\n" in value:
        return value
    value = re.sub(r", (?=(?:Seestraße|Robert-Bosch-Straße|Hafenstraße|Rheinsteig|Seetorstraße|Habsburgerstraße)\b)", "\n", value)
    value = re.sub(r", (?=\d{5} [A-ZÄÖÜ])", "\n", value)
    value = value.replace("Kammern Radolfzell, ", "Kammern Radolfzell\n")
    return value


def spec_for(item):
    brand = item["brand"]
    if item["id"] == "00":
        mode = "index"
    elif item["kind"] == "judgment":
        mode = "judgment"
    elif item["kind"] == "email":
        mode = "email"
    elif brand == "court" and re.search(r"protokoll|niederschrift", item["title"], re.I):
        mode = "protocol"
    elif item["id"] == "P30":
        mode = "court_order"
    elif brand == "court":
        mode = "court_letter"
    elif brand in ("employee_firm", "employer_firm") and item["kind"] in ("pleading", "letter"):
        mode = "firm_letter"
    elif item["kind"] == "contract":
        mode = "contract"
    elif brand == "client" and item["kind"] == "letter":
        mode = "personal_letter"
    elif brand == "employer" and item["kind"] == "letter":
        mode = "employer_letter"
    elif brand == "agency":
        mode = "insurer_letter"
    elif item["id"] in ("P03", "P32", "P33"):
        mode = "receipt"
    else:
        mode = "record"
    if item["id"] in ("P03", "P32", "P33"):
        mode = "receipt"
    top = {"index": 698, "judgment": 711, "protocol": 703,
           "court_letter": 617, "firm_letter": 610, "personal_letter": 630,
           "employer_letter": 628, "insurer_letter": 628, "email": 735,
           "record": 701, "contract": 700, "receipt": 703, "court_order": 703}[mode]
    return {"mode": mode, "brand": brand, "top": top}


def styles(spec):
    body = ParagraphStyle("body", fontName="TNR", fontSize=11, leading=15.1,
                          textColor=INK, spaceAfter=7.5, allowWidows=0, allowOrphans=0,
                          splitLongWords=True)
    heading = ParagraphStyle("heading", parent=body, fontName="TNR-Bold", fontSize=11.5,
                             leading=15.5, spaceBefore=13, spaceAfter=7.5, keepWithNext=True)
    return {
        "body": body,
        "heading": heading,
        "title": ParagraphStyle("title", parent=heading, fontSize=14, leading=18,
                                spaceBefore=0, spaceAfter=17),
        "small": ParagraphStyle("small", parent=body, fontSize=9.2, leading=12, spaceAfter=5),
        "micro": ParagraphStyle("micro", parent=body, fontSize=8, leading=10.5, spaceAfter=0),
        "date": ParagraphStyle("date", parent=body, alignment=TA_RIGHT, spaceAfter=16),
        "center": ParagraphStyle("center", parent=body, alignment=TA_CENTER, spaceAfter=14),
        "court_title": ParagraphStyle("court_title", parent=heading, fontSize=18, leading=23,
                                     alignment=TA_CENTER, spaceBefore=2, spaceAfter=25),
        "court_caps": ParagraphStyle("court_caps", parent=body, fontName="TNR-Bold",
                                    fontSize=13, leading=17, alignment=TA_CENTER, spaceAfter=14),
        "party": ParagraphStyle("party", parent=body, spaceAfter=7, leading=15.5),
        "role": ParagraphStyle("role", parent=body, fontName="TNR-Bold", alignment=TA_RIGHT),
        "counsel": ParagraphStyle("counsel", parent=body, leftIndent=15, spaceAfter=16),
        "evidence": ParagraphStyle("evidence", parent=body, leftIndent=15, rightIndent=8,
                                  spaceBefore=1, spaceAfter=10),
        "request": ParagraphStyle("request", parent=body, leftIndent=18, firstLineIndent=-3, spaceAfter=12),
        "dialogue": ParagraphStyle("dialogue", parent=body, leftIndent=14, rightIndent=5,
                                  spaceAfter=9),
        "cell": ParagraphStyle("cell", parent=body, fontSize=10, leading=13, spaceAfter=0),
        "th": ParagraphStyle("th", parent=body, fontName="TNR-Bold", fontSize=9.5,
                             leading=12.5, spaceAfter=0),
        "meta_key": ParagraphStyle("meta_key", parent=body, fontName="Helvetica", fontSize=7.8,
                                   leading=10.5, textColor=MUTED, spaceAfter=3),
        "meta_value": ParagraphStyle("meta_value", parent=body, fontSize=9.5, leading=12, spaceAfter=0),
    }


def _draw_paragraph(canv, value, x, top, width, style):
    paragraph = Paragraph(rich(value), style)
    _, height = paragraph.wrap(width, PAGE_H)
    paragraph.drawOn(canv, x, top - height)
    return height


def firm_identity(brand):
    if brand == "employer_firm":
        return {"name": "KNIGGE / NORTH", "lawyer": "Caspar Finley von Knigge", "role": "Rechtsanwalt",
                "address": "Robert-Bosch-Straße 6\n78467 Konstanz", "email": "kanzlei@knigge-north.example",
                "sign": "KN", "color": NAVY, "accent": BRONZE}
    return {"name": "FALKENHORST & FLOW", "lawyer": "Dr. Johanna Falkenhorst", "role": "Rechtsanwältin",
            "address": "Seestraße 18\n78464 Konstanz", "email": "j.falkenhorst@falkenhorst-flow.example",
            "sign": "FF", "color": TEAL, "accent": CORAL}


def _firm_mark(canv, x, y, brand, compact=False):
    ident = firm_identity(brand)
    canv.setFillColor(ident["color"])
    if brand == "employer_firm":
        canv.setFont("Helvetica-Bold", 20 if not compact else 13)
        canv.drawString(x, y, "KNIGGE")
        offset = pdfmetrics.stringWidth("KNIGGE", "Helvetica-Bold", 20 if not compact else 13) + 8
        canv.setStrokeColor(ident["accent"])
        canv.setLineWidth(1.2)
        canv.line(x + offset, y - 2, x + offset + 9, y + (17 if not compact else 11))
        canv.setFont("Helvetica", 20 if not compact else 13)
        canv.drawString(x + offset + 18, y, "NORTH")
    else:
        canv.setFont("TNR-Bold", 23 if not compact else 14)
        canv.drawString(x, y, "Falkenhorst")
        offset = pdfmetrics.stringWidth("Falkenhorst", "TNR-Bold", 23 if not compact else 14) + 8
        canv.setFont("TNR-Italic", 21 if not compact else 13)
        canv.drawString(x + offset, y + .3, "& Flow")
        if not compact:
            canv.setStrokeColor(ident["accent"])
            canv.setLineWidth(1.1)
            path = canv.beginPath()
            path.moveTo(x, y - 13)
            path.curveTo(x + 40, y - 7, x + 64, y - 18, x + 105, y - 12)
            path.curveTo(x + 140, y - 7, x + 170, y - 14, x + 208, y - 11)
            canv.drawPath(path)


def _employer_mark(canv, y, is_br=False):
    canv.setFillColor(GREEN)
    canv.setFont("Helvetica", 27)
    canv.drawString(LEFT, y, "uferwerk")
    canv.setFont("Helvetica", 7.7)
    canv.drawString(LEFT + 140, y + 1, "VERLAG")
    canv.setStrokeColor(colors.HexColor("#AA925B"))
    canv.setLineWidth(.8)
    canv.line(LEFT, y - 12, PAGE_W - RIGHT, y - 12)
    if is_br:
        canv.setFillColor(INK)
        canv.setFont("Helvetica-Bold", 8)
        canv.drawString(LEFT, y - 30, "BETRIEBSRAT")


def _recipient(canv, item, spec, sty):
    address = address_lines(item.get("recipient", ""))
    if spec["mode"] == "court_letter" and ";" in address:
        address = "An die Prozessbevollmächtigten\nin Sachen Muster ./. Uferwerk Verlag GmbH"
    if spec["mode"] == "firm_letter":
        transmission = re.compile(
            r"^\s*(?:Über das besondere elektronische Anwaltspostfach|per beA)\s*$",
            re.I | re.M,
        )
        per_bea = bool(transmission.search(address))
        address = transmission.sub("", address).strip()
        address = address.replace(" - Kammern Radolfzell", "\nKammern Radolfzell")
        if address.startswith("Arbeitsgericht") and "\n" not in address:
            address = "Arbeitsgericht Villingen-Schwenningen\nKammern Radolfzell\nSeetorstraße 5\n78315 Radolfzell"
        _draw_paragraph(canv, address, LEFT, 728, 287, sty["body"])
        if per_bea:
            _draw_paragraph(canv, "per beA", LEFT, 742, 200, sty["small"])
    else:
        _draw_paragraph(canv, address, LEFT, 725, 310, sty["body"])


def page_header(canv, doc, item, spec):
    sty = styles(spec)
    canv.saveState()
    mode, brand = spec["mode"], spec["brand"]
    if doc.page > 1:
        if mode in ("judgment", "protocol", "court_letter", "court_order"):
            canv.setFont("TNR", 10)
            canv.setFillColor(INK)
            canv.drawString(LEFT, PAGE_H - 37, "7 Ca 87/26")
            canv.drawCentredString(PAGE_W / 2, PAGE_H - 37, f"- {doc.page} -")
        else:
            canv.setFillColor(MUTED)
            canv.setFont("TNR", 9)
            label = (firm_identity(brand)["name"] if brand in ("employee_firm", "employer_firm")
                     else "Uferwerk Verlag GmbH" if brand == "employer"
                     else "E-Mail-Ausdruck" if mode == "email" else item.get("reference", "Muster ./. Uferwerk"))
            if mode == "email":
                label = "E-Mail | " + item["subject"][:65]
            canv.drawString(LEFT, PAGE_H - 35, clean(label)[:85])
            canv.drawRightString(PAGE_W - RIGHT, PAGE_H - 35, f"Seite {doc.page}")
            canv.setStrokeColor(PALE)
            canv.setLineWidth(.45)
            canv.line(LEFT, PAGE_H - 44, PAGE_W - RIGHT, PAGE_H - 44)
        canv.restoreState()
        return

    if mode == "judgment":
        canv.setFillColor(INK)
        canv.setFont("TNR", 10)
        canv.drawRightString(PAGE_W - RIGHT, 814, "Beglaubigte Abschrift")
        canv.setFont("TNR-Bold", 16)
        canv.drawCentredString(PAGE_W / 2, 782, "Arbeitsgericht Villingen-Schwenningen")
        canv.setFont("TNR", 12)
        canv.drawCentredString(PAGE_W / 2, 762, "Kammern Radolfzell")
        canv.setFont("TNR", 10)
        canv.drawString(LEFT, 735, "7 Ca 87/26")
        canv.drawRightString(PAGE_W - RIGHT, 735, "Verkündet am 8. Oktober 2026")
    elif mode == "protocol":
        canv.setFillColor(INK)
        canv.setFont("TNR-Bold", 14)
        canv.drawString(LEFT, 794, "Arbeitsgericht Villingen-Schwenningen")
        canv.setFont("TNR", 11)
        canv.drawString(LEFT, 776, "Kammern Radolfzell")
        canv.setFont("TNR-Bold", 11)
        canv.drawString(LEFT, 747, "7 Ca 87/26")
        canv.setFont("TNR", 10)
        canv.drawRightString(PAGE_W - RIGHT, 747, date.fromisoformat(item["date"]).strftime("%d.%m.%Y"))
        canv.setStrokeColor(INK)
        canv.setLineWidth(.5)
        canv.line(LEFT, 733, PAGE_W - RIGHT, 733)
    elif mode == "firm_letter":
        ident = firm_identity(brand)
        _firm_mark(canv, LEFT, 792, brand)
        _draw_paragraph(canv, ident["role"] + "\n" + ident["lawyer"] + "\n\n" + ident["address"],
                        427, 808, 113, sty["small"])
        _draw_paragraph(canv, ident["email"].replace("@", "@\n"), 427, 713, 113, sty["micro"])
        _draw_paragraph(canv, "UNSER ZEICHEN", 427, 674, 113, sty["meta_key"])
        _draw_paragraph(canv, "KN26-118" if brand == "employer_firm" else "F26-041LM", 427, 659, 113, sty["meta_value"])
        _draw_paragraph(canv, "Konstanz, " + date.fromisoformat(item["date"]).strftime("%d.%m.%Y"),
                        355, 629, 185, ParagraphStyle("right_date", parent=sty["body"], alignment=TA_RIGHT))
        canv.setFont("TNR", 7.5)
        canv.setFillColor(MUTED)
        canv.drawString(LEFT, 760, ident["name"] + " · " + clean(ident["address"]).replace("\n", " · "))
        _recipient(canv, item, spec, sty)
    elif mode == "court_order":
        canv.setFillColor(INK)
        canv.setFont("TNR-Bold", 14)
        canv.drawString(LEFT, 794, "Arbeitsgericht Villingen-Schwenningen")
        canv.setFont("TNR", 11)
        canv.drawString(LEFT, 776, "Kammern Radolfzell")
        canv.drawString(LEFT, 746, "7 Ca 87/26")
        canv.drawRightString(PAGE_W - RIGHT, 746, "12. Oktober 2026")
        canv.setLineWidth(.5)
        canv.line(LEFT, 733, PAGE_W - RIGHT, 733)
    elif mode == "court_letter":
        canv.setFillColor(INK)
        canv.setFont("TNR-Bold", 14)
        canv.drawString(LEFT, 796, "Arbeitsgericht Villingen-Schwenningen")
        canv.setFont("TNR", 11)
        canv.drawString(LEFT, 777, "Kammern Radolfzell")
        canv.setFont("TNR", 7.5)
        canv.drawString(LEFT, 755, "Arbeitsgericht · Seetorstraße 5 · 78315 Radolfzell")
        _recipient(canv, item, spec, sty)
        _draw_paragraph(canv, "Geschäftsstelle\nSeetorstraße 5\n78315 Radolfzell\n\nBitte bei Antwort angeben:\n7 Ca 87/26", 427, 729, 113, sty["small"])
        _draw_paragraph(canv, date.fromisoformat(item["date"]).strftime("%d.%m.%Y"), 427, 633, 113, sty["body"])
    elif mode in ("employer_letter", "contract") or (mode == "record" and brand == "employer"):
        is_br = "Betriebsrat" in item.get("sender", "") or item.get("sender", "").startswith("Cem Aydin")
        _employer_mark(canv, 791, is_br)
        if mode == "employer_letter":
            canv.setFont("TNR", 7.5)
            canv.setFillColor(MUTED)
            canv.drawString(LEFT, 745 if is_br else 755, ("Betriebsrat Uferwerk Verlag GmbH" if is_br else "Uferwerk Verlag GmbH") + " · Hafenstraße 24 · 78462 Konstanz")
            _recipient(canv, item, spec, sty)
            _draw_paragraph(canv, date.fromisoformat(item["date"]).strftime("%d.%m.%Y"), 430, 647, 110, sty["body"])
        else:
            _draw_paragraph(canv, ("Betriebsratsunterlagen" if is_br else "Vertriebsorganisation" if item["id"] == "N07" else "Projektkoordination · Bildbrücke" if item["id"] == "N12" else "Personal und Organisation"), LEFT, 742, 290, sty["small"])
            _draw_paragraph(canv, ({"N07": "15.04.2020", "N12": "Auswertung Aug./Sept. 2026", "N10": "23./24.03.2026"}.get(item["id"], date.fromisoformat(item["date"]).strftime("%d.%m.%Y"))), 376, 742, 164, sty["small"])
    elif mode == "personal_letter":
        _draw_paragraph(canv, address_lines(item.get("sender", "")), LEFT, 801, 380, sty["body"])
        _recipient(canv, item, spec, sty)
        _draw_paragraph(canv, date.fromisoformat(item["date"]).strftime("%d.%m.%Y"), 430, 652, 110, sty["body"])
    elif mode == "email":
        canv.setFillColor(INK)
        canv.setFont("Helvetica-Bold", 12)
        canv.drawString(LEFT, 800, "E-Mail")
        canv.setFont("Helvetica", 8)
        canv.setFillColor(MUTED)
        canv.drawRightString(PAGE_W - RIGHT, 800, "Ausdruck für die Handakte · 30.10.2026")
        canv.setStrokeColor(PALE)
        canv.line(LEFT, 786, PAGE_W - RIGHT, 786)
    elif mode == "insurer_letter":
        canv.setFillColor(colors.HexColor("#254F75"))
        canv.setFont("Helvetica-Bold", 22)
        canv.drawString(LEFT, 792, "KÜSTENKLAR")
        canv.setFont("Helvetica", 9)
        canv.drawString(LEFT, 774, "Rechtsschutz AG · Leistungsabteilung Arbeitsrecht")
        _recipient(canv, item, spec, sty)
        _draw_paragraph(canv, "Postfach 1104\n78401 Konstanz\n\nleistung@kuestenklar.example", 427, 734, 113, sty["small"])
        _draw_paragraph(canv, date.fromisoformat(item["date"]).strftime("%d.%m.%Y"), 427, 647, 113, sty["body"])
    elif mode == "index":
        _firm_mark(canv, LEFT, 794, "employee_firm")
        canv.setFillColor(TEAL)
        canv.rect(LEFT, 738, WIDTH, 2, fill=1, stroke=0)
        canv.setFont("Helvetica", 8)
        canv.drawString(LEFT, 719, "PROZESSAKTE · F26-041LM · UNTERLAGENSTAND 30. OKTOBER 2026")
    elif mode == "receipt":
        canv.setFillColor(INK)
        canv.setFont("Helvetica-Bold", 13)
        canv.drawString(LEFT, 797, "Elektronischer Rechtsverkehr")
        canv.setFont("Helvetica", 9)
        canv.drawString(LEFT, 777, "Nachrichten- und Zustellungsnachweis")
        canv.setStrokeColor(PALE)
        canv.line(LEFT, 759, PAGE_W - RIGHT, 759)
        _draw_paragraph(canv, item.get("reference", ""), LEFT, 739, WIDTH, sty["small"])
    else:
        if item["id"] == "N20":
            _firm_mark(canv, LEFT, 794, "employee_firm", compact=True)
        elif brand in ("employee_firm", "employer_firm"):
            _firm_mark(canv, LEFT, 794, brand, compact=True)
        else:
            canv.setFillColor(INK)
            canv.setFont("TNR-Bold", 13)
            canv.drawString(LEFT, 794, "Lisa Muster" if brand == "client" else "Handakte Muster ./. Uferwerk")
        canv.setStrokeColor(PALE)
        canv.line(LEFT, 778, PAGE_W - RIGHT, 778)
        _draw_paragraph(canv, item.get("reference", ""), LEFT, 756, WIDTH, sty["small"])
        _draw_paragraph(canv, date.fromisoformat(item["date"]).strftime("%d.%m.%Y"), LEFT, 737, WIDTH, sty["small"])
    canv.restoreState()


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, item, spec, **kwargs):
        super().__init__(*args, **kwargs)
        self.item, self.spec, self.saved_states = item, spec, []

    def showPage(self):
        self.saved_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        count = len(self.saved_states)
        for state in self.saved_states:
            self.__dict__.update(state)
            self.saveState()
            mode = self.spec["mode"]
            if mode not in ("judgment", "protocol", "court_letter", "court_order"):
                self.setStrokeColor(PALE)
                self.setLineWidth(.35)
                self.line(LEFT, 52, PAGE_W - RIGHT, 52)
                self.setFillColor(MUTED)
                self.setFont("TNR", 8)
                if self.spec["brand"] in ("employee_firm", "employer_firm") and mode != "email":
                    ident = firm_identity(self.spec["brand"])
                    self.drawString(LEFT, 39, ident["role"] + " " + ident["lawyer"])
                    self.drawString(LEFT, 27, ident["address"].replace("\n", " · ") + " · " + ident["email"])
                elif self.spec["brand"] == "employer" and mode != "email":
                    is_br = "Betriebsrat" in self.item.get("sender", "") or self.item.get("sender", "").startswith("Cem Aydin")
                    self.drawString(LEFT, 38, ("Betriebsrat Uferwerk Verlag GmbH" if is_br else "Uferwerk Verlag GmbH") + " · Hafenstraße 24 · 78462 Konstanz")
                    self.drawString(LEFT, 26, "Cem Aydin · betriebsrat@uferwerk.example" if is_br else "Geschäftsführerin Dr. Mara Ufer · personal@uferwerk.example")
                else:
                    self.drawString(LEFT, 37, clean(self.item.get("reference", ""))[:75])
                self.drawRightString(PAGE_W - RIGHT, 39, f"Seite {self._pageNumber} von {count}")
            elif mode == "judgment" and self._pageNumber == 1:
                self.setFont("TNR", 8)
                self.setFillColor(MUTED)
                self.drawRightString(PAGE_W - RIGHT, 36, "Beglaubigte Abschrift")
            self.restoreState()
            super().showPage()
        super().save()


def make_table(data, sty, spec):
    headers, rows = data["headers"], data["rows"]
    if any(len(row) != len(headers) for row in rows):
        raise ValueError("Unterschiedliche Tabellenspalten")
    def cell(value, style):
        value = rich(value).replace("Nutzerin/Nutzer", "Nutzerin /<br/>Nutzer").replace("Rabattfreigabe", "Rabatt-<br/>freigabe")
        value = re.sub(r"(?<![\d.])\d{2}\.\d{2}\.\d{4}(?!\d)", lambda m: "<nobr>" + m.group() + "</nobr>", value)
        value = re.sub(r"(?<![\d.])(?:19|20)\d{2}(?![\d<])", lambda m: "<nobr>" + m.group() + "</nobr>", value)
        return Paragraph(value, style)
    matrix = [[cell(value, sty["th"]) for value in headers]]
    matrix += [[cell(value, sty["cell"]) for value in row] for row in rows]
    ratios = data.get("widths")
    if headers == ["Zeitraum", "Inhalte", "Begleitung und Ziel"]:
        ratios = [.25, .38, .37]
    if headers == ["Nutzerin/Nutzer", "Angebot und Auftrag", "Rabattfreigabe", "Kundenstamm / Rechnung"]:
        ratios = [.18, .27, .18, .37]
    if ratios is None:
        if len(headers) == 2:
            ratios = [.32, .68]
        else:
            weights = [max(18, min(55, max(len(str(row[i])) for row in [headers] + rows) ** .64 * 4))
                       for i in range(len(headers))]
            ratios = [value / sum(weights) for value in weights]
    table = LongTable(matrix, colWidths=[WIDTH * x / sum(ratios) for x in ratios], repeatRows=1,
                      hAlign="LEFT", splitByRow=1, splitInRow=1)
    line_color = colors.HexColor("#C5CCD0")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EEF1F2")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LINEABOVE", (0, 0), (-1, 0), .7, INK),
        ("LINEBELOW", (0, 0), (-1, 0), .7, INK),
        ("LINEBELOW", (0, 1), (-1, -1), .3, line_color),
    ]))
    return table


def _metadata(story, item, sty, fields=None):
    fields = fields or [("VORGANG", item.get("reference", "")),
                        ("ADRESSAT / VERTEILER", item.get("recipient", ""))]
    cells = [[Paragraph(rich(key), sty["meta_key"]) for key, value in fields],
             [Paragraph(rich(value), sty["meta_value"]) for key, value in fields]]
    table = Table(cells, colWidths=[WIDTH / len(fields)] * len(fields), hAlign="LEFT")
    table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                               ("LEFTPADDING", (0, 0), (-1, -1), 0),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 14),
                               ("TOPPADDING", (0, 0), (-1, -1), 1),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
    story += [table, Spacer(1, 18)]


def _judgment_caption(story, item, sty):
    story += [Paragraph("IM NAMEN DES VOLKES", sty["court_caps"]),
              Paragraph("Urteil", sty["court_title"]),
              Paragraph("In dem Rechtsstreit", sty["body"]), Spacer(1, 6)]
    party_sets = [
        ("<b>Lisa Muster</b>,<br/>geboren am 19. Juli 1982,<br/>Rheinsteig 8, 78462 Konstanz,", "Klägerin",
         "Prozessbevollmächtigte:<br/>Rechtsanwältin Dr. Johanna Falkenhorst,<br/>FALKENHORST &amp; FLOW, Seestraße 18, 78464 Konstanz,"),
        ("<b>Uferwerk Verlag GmbH</b>,<br/>Hafenstraße 24, 78462 Konstanz,<br/>vertreten durch die Geschäftsführerin Dr. Mara Ufer,", "Beklagte",
         "Prozessbevollmächtigter:<br/>Rechtsanwalt Caspar Finley von Knigge,<br/>KNIGGE / NORTH, Robert-Bosch-Straße 6, 78467 Konstanz,"),
    ]
    for i, (party, role, counsel) in enumerate(party_sets):
        if i:
            story.append(Paragraph("gegen", sty["center"]))
        table = Table([[Paragraph(party, sty["party"]), Paragraph("- " + role + " -", sty["role"])]],
                      colWidths=[WIDTH - 105, 105], hAlign="LEFT")
        table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                   ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                   ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                   ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
        story += [table, Paragraph(counsel, sty["counsel"])]
    raw = " ".join(item.get("court_caption_paragraphs", []))
    if not raw:
        raw = " ".join(item["sections"][0].get("paragraphs", []))
    match = re.search(r"hat das Arbeitsgericht.*", raw, re.S)
    intro = match.group() if match else (
        "hat das Arbeitsgericht Villingen-Schwenningen, Kammern Radolfzell, durch den Vorsitzenden Richter "
        "Dr. Balthasar Jay von Sausewind sowie die ehrenamtliche Richterin Hedwig Sky Pfefferle und den "
        "ehrenamtlichen Richter Ottokar Finn Leicht aufgrund der mündlichen Verhandlung vom 24. September 2026 "
        "für Recht erkannt:")
    if "für Recht erkannt" in intro:
        intro = intro.split("für Recht erkannt", 1)[0] + "für Recht erkannt:"
    story += [Paragraph(rich(intro), sty["body"]), Spacer(1, 13)]


def _split_sent(value):
    value = value.removeprefix("Gesendet:").strip()
    match = re.match(r"(.+?\b\d{2}:\d{2}(?:\s*Uhr)?)(.*)", value, re.S)
    return (match[1].strip(), match[2].lstrip(" .\n")) if match else (value, "")


def _email_header(story, item, sty):
    sent = next((_split_sent(p)[0] for sec in item["sections"] for p in sec.get("paragraphs", []) if p.startswith("Gesendet:")), date.fromisoformat(item["date"]).strftime("%d.%m.%Y"))
    fields = [("Von", item["sender"]), ("An", item["recipient"]),
              ("Gesendet", sent),
              ("Betreff", item["subject"])]
    matrix = [[Paragraph("<b>" + key + ":</b>", sty["small"]), Paragraph(rich(value), sty["small"])]
              for key, value in fields]
    table = Table(matrix, colWidths=[56, WIDTH - 56], hAlign="LEFT")
    table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                               ("LEFTPADDING", (0, 0), (-1, -1), 0),
                               ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                               ("TOPPADDING", (0, 0), (-1, -1), 2),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                               ("LINEBELOW", (0, -1), (-1, -1), .5, PALE)]))
    table.keepWithNext = True
    gap = Spacer(1, 19)
    gap.keepWithNext = True
    story += [table, gap]


def _attachments(item):
    introductions = {"P01": "K1 bis K9 gemäß gesondertem Anlagenverzeichnis.",
                     "P10": "B1 bis B10 gemäß gesondertem Anlagenverzeichnis.",
                     "P13": "K10 bis K14 gemäß ergänzendem Anlagenverzeichnis.",
                     "P15": "B11 bis B13 gemäß ergänzendem Anlagenverzeichnis."}
    if item["id"] in introductions:
        return [introductions[item["id"]]]
    return [value for value in item.get("attachments", []) if not re.match(r"^[VPN]\d{2}(?:\b|/)", value)]


def build_pdf(item, output):
    spec = spec_for(item)
    sty = styles(spec)
    document = BaseDocTemplate(str(output), pagesize=A4,
                              title=item["title"], author=item.get("sender", "").split("\n")[0],
                              subject=item.get("subject", ""), creator="Dokumentensatz",
                              invariant=1, pageCompression=1, allowSplitting=1)
    first = Frame(LEFT, BOTTOM, WIDTH, spec["top"] - BOTTOM,
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="first")
    later = Frame(LEFT, BOTTOM, WIDTH, PAGE_H - 129,
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0, id="later")
    document.addPageTemplates([
        PageTemplate(id="First", frames=first, onPage=lambda c, d: page_header(c, d, item, spec), autoNextPageTemplate="Later"),
        PageTemplate(id="Later", frames=later, onPage=lambda c, d: page_header(c, d, item, spec)),
    ])
    story = []
    mode = spec["mode"]
    if mode == "judgment":
        _judgment_caption(story, item, sty)
    elif mode == "email":
        _email_header(story, item, sty)
    elif mode == "index":
        story += [Paragraph("Muster ./. Uferwerk Verlag GmbH", ParagraphStyle("cover", parent=sty["title"], fontSize=24, leading=29)),
                  Paragraph("Aktenverzeichnis", sty["title"])]
        _metadata(story, item, sty, [("KANZLEIZEICHEN", "F26-041LM"),
                                    ("ERSTE INSTANZ", "7 Ca 87/26"), ("STAND", "30.10.2026")])
    elif mode == "protocol":
        story += [Paragraph("Niederschrift", sty["court_title"]),
                  Paragraph(rich(item.get("subject", item["title"])), sty["center"]),
                  Paragraph("Muster ./. Uferwerk Verlag GmbH", sty["heading"]), Spacer(1, 5)]
    else:
        if mode in ("record", "receipt", "contract", "court_order"):
            story.append(Paragraph(rich(item["title"]), sty["title"]))
            if mode not in ("receipt", "court_order", "contract"):
                _metadata(story, item, sty)
        else:
            title = item["title"]
            if item["kind"] == "pleading":
                story.append(Paragraph("Muster ./. Uferwerk Verlag GmbH", sty["heading"]))
                if item["id"] != "P01":
                    story.append(Paragraph("Arbeitsgericht Villingen-Schwenningen - Kammern Radolfzell · 7 Ca 87/26",
                                           sty["small"]))
            story.append(Paragraph(rich(title), sty["title"]))
            if item["kind"] not in ("pleading",) and item.get("subject") != title:
                story.append(Paragraph(rich(item.get("subject", "")), sty["small"]))
            story.append(Spacer(1, 7))
    sections = item["sections"]
    if mode == "judgment" and not item.get("court_caption_paragraphs") and "Rubrum" in sections[0].get("heading", ""):
        sections = sections[1:]
    for i, section in enumerate(sections):
        if section.get("page_break") or i in item.get("page_break_before_sections", []):
            story.append(PageBreak())
        if section.get("heading"):
            story.append(Paragraph(rich(section["heading"]), sty["heading"]))
        for value in section.get("paragraphs", []):
            if item["id"] == "N10":
                parsed = re.match(r"Von: (.*?)\. An: (.*?)\. Betreff: (.*?)\. Text: (.*)", value, re.S)
                if parsed:
                    original = dict(item, sender=parsed[1], recipient=parsed[2], subject=parsed[3],
                                    sections=[{"paragraphs": ["Gesendet: " + section.get("heading", "").split("Nachricht vom ")[-1]]}])
                    _email_header(story, original, sty)
                    story.append(Paragraph(rich(parsed[4]), sty["body"]))
                    story.append(Spacer(1, 13))
                    continue
            if mode == "email" and i == 0 and re.match(r"^Gesendet:", value):
                value = _split_sent(value)[1]
                if not value:
                    continue
            p_style = sty["evidence"] if value.startswith("Beweis:") else (
                sty["dialogue"] if re.match(r"^(?:Frage |Antwort |Vorhalt )", value) else sty["body"])
            if item["id"] == "P01" and re.match(r"^(?:(?:1\.[1-3][.)]?|[12]\.)\s|Es wird festgestellt|Die Beklagte wird)", value):
                p_style = sty["request"]
            story.append(Paragraph(rich(value), p_style))
        if section.get("table"):
            story += [make_table(section["table"], sty, spec), Spacer(1, 12)]
    ending = []
    last_text = " ".join(p for sec in sections for p in sec.get("paragraphs", []))
    signature_name = item.get("signature", "").split("\n", 1)[0]
    signature_duplicate = (mode == "email" and (
        re.sub(r"\W", "", last_text.lower()).endswith(re.sub(r"\W", "", item.get("signature", "").lower()))
        or (signature_name and re.search(r"(?:Grüße|Gruß|Grüßen).{0,150}" + re.escape(signature_name), last_text, re.I | re.S))))
    if item.get("signature") and not signature_duplicate:
        if mode == "contract" and ";" in item["signature"]:
            parties = item["signature"].split(";", 1)
            sign_table = Table([[Paragraph(rich(p.strip()), sty["body"]) for p in parties]],
                               colWidths=[WIDTH * .56, WIDTH * .44], hAlign="LEFT")
            sign_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"),
                                           ("LEFTPADDING", (0, 0), (-1, -1), 0),
                                           ("RIGHTPADDING", (0, 0), (-1, -1), 16),
                                           ("TOPPADDING", (0, 0), (-1, -1), 13)]))
            ending += [Spacer(1, 28), sign_table]
        else:
            ending += [Spacer(1, 15), Paragraph(rich(item["signature"]), sty["body"])]
    actual_attachments = _attachments(item)
    if actual_attachments:
        ending += [Spacer(1, 8), Paragraph("Anlagen:", sty["small"])]
        for value in actual_attachments:
            ending.append(Paragraph(rich(value), sty["small"]))
    if ending:
        while story and isinstance(story[-1], Spacer):
            story.pop()
        tail = []
        if story and isinstance(story[-1], Paragraph):
            tail.insert(0, story.pop())
            if story and isinstance(story[-1], Paragraph):
                tail.insert(0, story.pop())
            if story and isinstance(story[-1], Paragraph) and story[-1].style.name == "heading":
                tail.insert(0, story.pop())
        story.append(KeepTogether(tail + ending))
    document.build(story, canvasmaker=lambda *a, **kw: NumberedCanvas(*a, item=item, spec=spec, **kw))
