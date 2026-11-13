#!/usr/bin/env python3
"""Erzeugt Bankbelege, Korrespondenz und Verfahrensunterlagen für drei Insolvenzreifeakten."""
from __future__ import annotations

import argparse
from collections import defaultdict
import csv
from datetime import date, datetime, time, timezone
from email import policy
from email.message import EmailMessage
from email.utils import format_datetime
import json
import os
from shutil import copyfile
from pathlib import Path
import re
from xml.sax.saxutils import escape

from docx import Document
from docx.shared import Cm, Pt, RGBColor
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from insolvenzreife_grundakten import build_supplements
from insolvenzreife_anfechtung_faelle import build_avoidance_material
from insolvenzreife_anfechtung_vorlagen import build_templates

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "scripts/data/zu-insolvenzfaelle.json"
SELECTION = ROOT / "scripts/data/testakten-grundakten-insolvenzreife.json"
INK = "#183039"
ACCENT = "#006663"
PAPER = "#EAF2F1"
MONTHS = ("Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August",
          "September", "Oktober", "November", "Dezember")


def register_letter_fonts():
    """Original-TTFs nutzen; keine stillschweigende Ersatzschrift für Kanzleibriefe."""
    candidates = [Path(os.environ["INSOLVENZREIFE_FONT_DIR"])] if os.environ.get("INSOLVENZREIFE_FONT_DIR") else [
        Path("/System/Library/Fonts/Supplemental"), Path("/Library/Fonts"),
        Path("/usr/share/fonts/truetype/msttcorefonts")]
    variants = {
        "InsoTimes": ("Times New Roman.ttf", "times.ttf", "Times_New_Roman.ttf"),
        "InsoTimes-Bold": ("Times New Roman Bold.ttf", "timesbd.ttf", "Times_New_Roman_Bold.ttf"),
        "InsoTimes-Italic": ("Times New Roman Italic.ttf", "timesi.ttf", "Times_New_Roman_Italic.ttf"),
        "InsoTimes-BoldItalic": ("Times New Roman Bold Italic.ttf", "timesbi.ttf", "Times_New_Roman_Bold_Italic.ttf"),
    }
    for directory in candidates:
        files = {name: next((directory / filename for filename in filenames if (directory / filename).is_file()), None)
                 for name, filenames in variants.items()}
        if all(files.values()):
            for name, file in files.items():
                pdfmetrics.registerFont(TTFont(name, str(file)))
            pdfmetrics.registerFontFamily("InsoTimes", normal="InsoTimes", bold="InsoTimes-Bold",
                                          italic="InsoTimes-Italic", boldItalic="InsoTimes-BoldItalic")
            return
    raise RuntimeError("Lizenzierte Times-New-Roman-TTFs fehlen (Regular, Bold, Italic, Bold Italic); INSOLVENZREIFE_FONT_DIR setzen")


def eur(cents):
    euros, fraction = divmod(abs(cents), 100)
    return f"{'−' if cents < 0 else ''}{euros:,}".replace(",", ".") + f",{fraction:02d}"


def de_date(value):
    return date.fromisoformat(value).strftime("%d.%m.%Y")


def csv_file(path, fieldnames, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=";", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def bank_statements(case, directory):
    monthly = defaultdict(list)
    for row in case["transactions"]:
        monthly[row["date"][:7]].append(row)
    assert len(monthly) == 24, (case["slug"], list(monthly))
    opening = case["opening_bank_balance_cents"]
    names = []
    for month, rows in monthly.items():
        year, month_number = map(int, month.split("-"))
        month_label = f"{MONTHS[month_number - 1]} {year}"
        path = directory / f"Auszug_{month}.pdf"
        names.append(path)
        width, height = landscape(A4)
        canvas = Canvas(str(path), pagesize=(width, height), invariant=1)
        canvas.setTitle(f"Kontoauszug {month_label} | {case['company']}")
        canvas.setAuthor(case["bank_name"])
        page_size = 12
        booking_style = ParagraphStyle("Buchung", fontName="Helvetica", fontSize=8,
                                       leading=9, textColor=HexColor(INK))
        for start in range(0, len(rows), page_size):
            part = rows[start:start + page_size]
            canvas.setFillColor(HexColor(INK))
            canvas.rect(0, height - 92, width, 92, fill=1, stroke=0)
            canvas.setFillColor(HexColor("#FFFFFF"))
            canvas.setFont("Helvetica-Bold", 21)
            canvas.drawString(35, height - 39, case["bank_name"])
            canvas.setFont("Helvetica", 11)
            canvas.drawString(35, height - 62, f"Geschäftskonto   |   Kontoauszug {month_label}")
            canvas.drawRightString(width - 35, height - 62, f"{year}/{month_number:02d}    Seite {start // page_size + 1} / {(len(rows) + page_size - 1) // page_size}")
            canvas.setFillColor(HexColor(INK))
            canvas.setFont("Helvetica-Bold", 11)
            canvas.drawString(35, height - 115, case["company"])
            canvas.setFont("Helvetica", 9)
            canvas.drawString(35, height - 132, f"IBAN {case['iban']}   |   EUR   |   Buchungstag und Wertstellung identisch")
            canvas.drawRightString(width - 35, height - 124, f"Übertrag {eur(opening)} EUR")
            y = height - 162
            for x, heading in ((38, "Buchung"), (115, "Referenz"), (215, "Zahlungspartner"), (392, "Verwendungszweck")):
                canvas.drawString(x, y, heading)
            canvas.drawRightString(697, y, "Betrag EUR")
            canvas.drawRightString(803, y, "Saldo EUR")
            for index, item in enumerate(part):
                y -= 26
                if index % 2 == 0:
                    canvas.setFillColor(HexColor(PAPER))
                    canvas.rect(33, y - 11, width - 66, 26, fill=1, stroke=0)
                canvas.setFillColor(HexColor(INK))
                canvas.setFont("Helvetica", 8)
                for x, max_width, value in (
                    (38, 72, de_date(item["date"])),
                    (115, 95, item["id"]),
                    (215, 169, item["counterparty"]),
                    (392, 211, item["description"]),
                ):
                    paragraph = Paragraph(escape(str(value)), booking_style)
                    _, wrapped_height = paragraph.wrap(max_width, 21)
                    if wrapped_height > 21:
                        raise ValueError(f"Buchungstext passt nicht in zwei Zeilen: {item['id']}")
                    paragraph.drawOn(canvas, x, y + 7 - wrapped_height)
                opening += item["amount_cents"]
                if opening != item["balance_cents"]:
                    raise ValueError(f"Saldo weicht ab: {case['slug']} / {item['id']}")
                canvas.drawRightString(697, y, eur(item["amount_cents"]))
                canvas.drawRightString(803, y, eur(opening))
            canvas.setStrokeColor(HexColor(ACCENT))
            canvas.line(35, 65, width - 35, 65)
            canvas.setFillColor(HexColor(INK))
            canvas.setFont("Helvetica-Bold", 10)
            label = "Schlusssaldo" if start + len(part) == len(rows) else "Übertrag auf Folgeseite"
            canvas.drawRightString(width - 35, 46, f"{label} {eur(opening)} EUR")
            canvas.setFont("Helvetica", 8)
            canvas.drawString(35, 27, "Elektronischer Kontoauszug   |   Buchungsreferenz dient dem Belegabgleich")
            canvas.showPage()
        canvas.save()
    return names


def body_paragraphs(item):
    body = item["body"]
    return body if isinstance(body, list) else body.split("\n\n")


def letter_pdf(path, case, item):
    is_court = item["type"] in {"interim_order", "opening_notice", "opening_order"}
    color = item.get("color", "#344351" if is_court else "#304E6C" if item["type"] == "bank" else ACCENT)
    title = item["subject"]
    issuer = item["issuer"]
    kwargs = dict(pagesize=A4, leftMargin=56, rightMargin=56, topMargin=114, bottomMargin=66,
                  title=title, author=issuer)
    document = SimpleDocTemplate(str(path), **kwargs)
    body = ParagraphStyle("Brief", fontName="InsoTimes", fontSize=11, leading=15, spaceAfter=11,
                          textColor=HexColor(INK))
    heading = ParagraphStyle("Betreff", parent=body, fontName="InsoTimes-Bold", fontSize=16, leading=20,
                             spaceBefore=12, spaceAfter=17)
    section_heading = ParagraphStyle("Abschnitt", parent=body, fontName="InsoTimes-Bold", keepWithNext=True,
                                     spaceBefore=4, spaceAfter=5)
    meta = ParagraphStyle("Aktenzeichen", parent=body, fontName="Helvetica", fontSize=9, leading=13,
                          spaceAfter=5)

    def text(value, style):
        return Paragraph(escape(str(value)).replace("\n", "<br/>"), style)

    flow = [text(item.get("recipient", case["company"]), meta)]
    if item.get("address"):
        flow.append(text(item["address"], meta))
    flow.extend([Spacer(1, 10), text(f"{de_date(item['date'])}   |   Geschäftszeichen {item['id']}", meta),
                 text(title, heading)])
    for paragraph in body_paragraphs(item):
        style = section_heading if re.fullmatch(r"\d+(?:\.\d+)* [^\n]{1,80}", paragraph) else body
        flow.append(text(paragraph, style))
    if item.get("signature"):
        flow.extend([Spacer(1, 9), text(item["signature"], body)])

    def letterhead(canvas, doc):
        w, h = A4
        canvas.setFillColor(HexColor(color))
        canvas.rect(55, h - 91, w - 110, 2, fill=1, stroke=0)
        canvas.setFont("Helvetica-Bold", 16 if len(issuer) < 45 else 12)
        canvas.drawString(56, h - 61, issuer)
        canvas.setFont("Helvetica", 8)
        line = item.get("letterhead_line") or ("Insolvenzsachen" if is_court else {
            "bank": "Firmenkunden und Kreditverwaltung", "contract": "Vertragsverwaltung",
            "valuation": "Bewertung und Vermarktung", "demand": "Forderungsmanagement",
            "profile": "Betrieb und Organisation", "accounting": "Rechnungswesen", "petition": "Beitrags- und Forderungskonto",
            "handover": "Insolvenzverwaltung"}.get(item["type"], "Rechnungswesen"))
        canvas.drawString(56, h - 78, line)
        canvas.drawString(56, 40, item["id"])
        canvas.drawRightString(w - 56, 40, f"Seite {doc.page}")

    def invariant(*args, **kwargs):
        kwargs["invariant"] = 1
        return Canvas(*args, **kwargs)

    document.build(flow, onFirstPage=letterhead, onLaterPages=letterhead, canvasmaker=invariant)


def mail_file(path, case, item):
    mail = EmailMessage(policy=policy.SMTP)
    mail["From"] = item.get("from", f"{item['issuer']} <buchhaltung@{case['slug']}.example>")
    mail["To"] = item.get("to", f"Aktenübernahme <eingang@{case['slug']}.example>")
    mail["Subject"] = item["subject"]
    mail["Date"] = format_datetime(datetime.combine(date.fromisoformat(item["date"]), time(9, 30), timezone.utc))
    mail["Message-ID"] = f"<{case['slug']}-{path.stem}@akten.example>"
    mail["Content-Language"] = "de-DE"
    mail.set_content("\n\n".join(body_paragraphs(item)), charset="utf-8")
    path.write_bytes(mail.as_bytes())


def mandate(path, case):
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Cm(2.5)
    section.bottom_margin = Cm(2.2)
    section.left_margin = section.right_margin = Cm(2.5)
    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(11)
    style.paragraph_format.space_after = Pt(9)
    title = doc.styles["Title"]
    title.font.name = "Times New Roman"
    title.font.size = Pt(22)
    title.font.color.rgb = RGBColor.from_string("111111")
    for border in title.element.xpath(".//w:pBdr"):
        border.getparent().remove(border)
    header = section.header.paragraphs[0]
    administrator = case["procedure"]["administrator"]
    header.add_run(administrator.upper() + "  |  INSOLVENZVERWALTUNG").bold = True
    header.runs[0].font.color.rgb = RGBColor.from_string("006663")
    section.footer.paragraphs[0].text = f"Interne Beauftragung  ·  {case['company']}"
    doc.add_paragraph("Auftrag zur Auswertung der Zahlungsunterlagen", "Title")
    doc.add_paragraph(case["company"])
    doc.add_paragraph(str(case["address"]))
    doc.add_paragraph(f"Von {administrator} an das Team Anfechtung und Rechnungswesen")
    doc.add_paragraph(
        "Bitte rekonstruieren Sie aus den übergebenen Unterlagen, ab wann Zahlungsunfähigkeit und "
        "insolvenzrechtliche Überschuldung jeweils belastbar feststellbar sind. Ich brauche die Feststellungen "
        "als Grundlage für die spätere Prüfung einzelner Zahlungen an Lieferanten, Finanzamt und Einzugsstellen."
    )
    doc.add_paragraph(
        f"Die Bankunterlagen decken den Zeitraum vom {de_date(case['history_start'])} bis zum "
        f"{de_date(case['history_end'])} ab. Beginnen Sie mit der Abstimmung der Salden und ziehen Sie "
        "die offenen Posten, Zahlungsabreden, die Wertunterlagen und die Finanzplanung hinzu. "
        "Behalten Sie offene Annahmen mit Quelle, Betrag und frühestem Nachweistermin im Blick."
    )
    doc.add_paragraph(
        "Halten Sie den letzten belastbar unauffälligen und den ersten belastbar auffälligen Stichtag "
        "für jeden Insolvenzgrund fest. Begründen Sie die Grenzen der Rückrechnung und nennen Sie "
        "die Unterlage, mit der sich die Lücke am ehesten schließen lässt. Bitte ordnen Sie den "
        "Fremdantrag und den Eröffnungsbeschluss zeitlich ein und stellen Sie die Ergebnisse in einer "
        "kurzen Entscheidungsvorlage und zwei nachvollziehbaren Berechnungen dar."
    )
    doc.add_paragraph(f"{administrator}\nInsolvenzverwaltung")
    doc.save(path)


def make_cases(data, root):
    register_letter_fonts()
    template_source = root / "zahlungsunfaehigkeits-und-ueberschuldungspruefer/vorlagen"
    build_templates(template_source)
    selection = {}
    for case in data["cases"]:
        directory = root / "testakten" / case["slug"]
        bank = directory / "01_Bank"
        books = directory / "02_Buchhaltung"
        mail = directory / "03_Korrespondenz"
        proceedings = directory / "10_Verfahren"
        for folder in (bank, books, mail, proceedings):
            folder.mkdir(parents=True, exist_ok=True)
        sources = bank_statements(case, bank)
        ledger = books / "01_Buchungsjournal_EUR_Cent.csv"
        csv_file(ledger, ("date", "value_on", "id", "counterparty", "description", "amount_cents", "balance_cents",
                          "ledger_account"), case["transactions"])
        sources.append(ledger)
        for filename, key, fields in (
            ("02_Kreditoren_OP.csv", "obligations", ("id", "creditor", "description", "arose_on", "due_on",
               "amount_cents", "paid_on", "payment_id", "defer_until", "disputed", "source")),
            ("03_Debitoren_OP.csv", "receivables", ("id", "debtor", "description", "available_on", "amount_cents",
               "received_on", "payment_id", "confirmed_on", "source")),
            ("04_Kreditlinien.csv", "facilities", ("id", "from", "through", "amount_cents", "drawable", "source")),
        ):
            target = books / filename
            rows = case[key]
            if rows:
                columns = (*fields, *sorted(set().union(*(row.keys() for row in rows)) - set(fields)))
                csv_file(target, columns, rows)
                sources.append(target)
        workbook = books / "05_Stichtagsunterlagen.xlsx"
        sources.append(workbook)
        order = directory / "00_Auftrag.docx"
        mandate(order, case)
        sources.append(order)
        for item in case["documents"]:
            if "/" in item["id"] or "\\" in item["id"]:
                raise ValueError(f"Unzulässige Beleg-ID {item['id']}")
            procedural = item["type"] in {"petition", "interim_order", "opening_notice", "opening_order", "handover"}
            if item["type"] == "email":
                target = (proceedings if procedural else mail) / f"{item['id']}.eml"
                mail_file(target, case, item)
            else:
                target = (proceedings if procedural else mail) / f"{item['id']}.pdf"
                letter_pdf(target, case, item)
            if not procedural:
                sources.append(target)
        sources.extend(build_supplements(case, directory, letter_pdf, csv_file))
        sources.extend(build_avoidance_material(case, directory, letter_pdf, csv_file))
        templates = directory / "20_Vorlagen"
        templates.mkdir(exist_ok=True)
        for name in ("01_Anfechtungsschreiben.docx", "02_Anfechtungsklage.docx"):
            copyfile(template_source / name,
                     templates / name)
        selection[case["slug"]] = [path.relative_to(directory).as_posix() for path in sorted(sources)]
    return selection


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    selection = make_cases(json.loads(DATA.read_text(encoding="utf-8")), args.root)
    target = args.root / SELECTION.relative_to(ROOT)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(selection, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(" / ".join(f"{slug}: {len(paths)} Eingangsdateien" for slug, paths in selection.items()))


if __name__ == "__main__":
    main()
