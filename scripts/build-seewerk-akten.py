#!/usr/bin/env python3
"""Rendert ausschließlich die beiden redaktionellen Fassungen Muster / Seewerk."""

import argparse
from collections import Counter
import csv
from datetime import datetime
from email.message import EmailMessage
from email import policy
from email.utils import format_datetime
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import zipfile

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from docx.table import Table
from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table as PDFTable, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from xml.sax.saxutils import escape

from testakte_disclaimer import NOTICE_BYTES, NOTICE_MARKDOWN, pdf_content_errors
from testakte_office_pdf import render_office_batch

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "arbeitsrecht-kuendigungsschutzklagewerkstatt"
DATA = ROOT / "scripts/data/seewerk-kern.json"
EXPANSION = ROOT / "scripts/data/seewerk-ergaenzungen.json"
TAG = "arbeitsrecht-kuendigungsschutzklagewerkstatt-v1.1.0"
BASE = f"https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{TAG}"
SLUGS = ["arbeitsrecht-muster-seewerk-konzept-radolfzell", "arbeitsrecht-muster-seewerk-lebensakte-radolfzell"]
STAMP = (2026, 10, 22, 12, 0, 0)
FONTS = Path(os.environ.get("CISG_FONT_DIR", "/System/Library/Fonts/Supplemental"))
EMPLOYER = "Seewerk Präzisionsguss GmbH\nAm Gießereihof 1\n78315 Radolfzell am Bodensee"
LAWYER = "Seeblick Rechtsanwälte\nRechtsanwältin Lea Brandt\nMarktstätte 3\n78462 Konstanz"
EMPLOYEE = "Herrn\nDaniel Muster\nUferweg 7\n78464 Konstanz"


def module(name):
    spec = importlib.util.spec_from_file_location(name.replace("-", "_"), ROOT / "scripts" / (name + ".py"))
    value = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = value
    spec.loader.exec_module(value)
    return value


def import_source(path):
    """Übernimmt nur den Anlagenanhang; Referenten- und Lösungsseiten bleiben außen vor."""
    document = Document(path)
    blocks, active = [], False
    for element in document.element.body:
        text = "".join(node.text or "" for node in element.iter(qn("w:t")))
        if text == "Anlage K1":
            active = True
        if not active or not text:
            continue
        if element.tag == qn("w:tbl"):
            blocks.append({"rows": [[cell.text.replace("§", "Paragraf") for cell in row.cells]
                                    for row in Table(element, document).rows]})
        else:
            blocks.append({"text": text.replace("§", "Paragraf")})
    if len(blocks) != 154 or blocks[117].get("text") != "Anlage K12":
        raise ValueError("Der freigegebene Anlagenanhang wurde verändert")
    DATA.write_text(json.dumps({"source_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                                "blocks": blocks}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def core_documents(blocks):
    def doc(key, annex, title, indices, date, sender=EMPLOYER, recipient=EMPLOYEE, suffix="docx"):
        return {"key": key, "annex": annex, "title": title, "filename": key + "." + suffix,
                "date": date, "sender": sender, "recipient": recipient,
                "blocks": [blocks[index] for index in indices]}
    return [
        doc("K01_Arbeitsvertrag", 1, "Arbeitsvertrag vom 15.03.2012 (Auszug)", range(2, 9), "2012-03-15", recipient="Daniel Muster"),
        doc("K01_Aenderung2019", 1, "Änderungsvereinbarung vom 18.12.2019", range(10, 12), "2019-12-18", recipient="Daniel Muster"),
        doc("K01_Gehaltsstand", 1, "Gehaltsstand", [12], "2026-11-23", LAWYER, "Handakte Muster", "txt"),
        doc("K02_Betriebsvereinbarung", 2, "Betriebsvereinbarung Nr. 7/2020 „Variable Vergütung“ (Auszug)", range(15, 21), "2020-01-15", recipient="Betrieb Radolfzell / Betriebsrat"),
        doc("K03_Bonus2024", 3, "Ihr Bonus für das Geschäftsjahr 2024", [31, 32], "2025-03-21"),
        doc("K04_Bonus2025", 4, "Ihr Bonus für das Geschäftsjahr 2025", [43, 44], "2026-03-20"),
        doc("K05_Bonusforderung", 5, "Widerspruch Bonus 2025", [48], "2026-04-14T21:17:00+02:00", "Daniel Muster <daniel.muster@privatpost.example>", "Sabine Kraus <personal@seewerk-guss.example>", "eml"),
        doc("K05_Bonusantwort", 5, "AW: Widerspruch Bonus 2025", [50], "2026-04-22T10:03:00+02:00", "Sabine Kraus <personal@seewerk-guss.example>", "Daniel Muster <daniel.muster@privatpost.example>", "eml"),
        doc("K06_Abmahnung", 6, "Abmahnung", [62, 63], "2026-01-12"),
        doc("K06_Sendungsstatus", 6, "Sendungsverfolgung", [64], "2026-01-13", "Sendungsverfolgung", "RT 4471 0923 6DE", "pdf"),
        doc("K06_Kenntnisvermerk", 6, "Vermerk der Kanzlei", [65], "2026-11-23", LAWYER, "Handakte Muster", "txt"),
        doc("K07_Einladung", 7, "Einladung zu einem Anhörungsgespräch", [77, 78], "2026-10-27"),
        doc("K08_Anhoerung", 8, "Protokoll der Anhörung", range(81, 88), "2026-10-29", recipient="Personalakte 20417"),
        doc("K09_Hinweisschild", 9, "Hinweisschild Tor 1", [90], "2026-10-22", EMPLOYER, "Tor 1 / Empfang", "pdf"),
        doc("K09_Videovermerk", 9, "Auswertungsvermerk Video", range(91, 95), "2026-10-22", recipient="Personalakte 20417"),
        doc("K10_Zeiterfassung", 10, "Auszug Zeiterfassung", range(97, 100), "2026-10-22", recipient="Personalakte 20417", suffix="xlsx"),
        doc("K11_Kuendigung", 11, "Kündigung Ihres Arbeitsverhältnisses", range(111, 116), "2026-11-05"),
        doc("K11_Zustellvermerk", 11, "Zustellvermerk", [116], "2026-11-06", "Michael Lang / Werkschutz", "Personalabteilung", "txt"),
        doc("K12_Bildschirmabschrift", 12, "Screenshots aus der Lauf-App „RunTrack“", range(119, 122), "2026-10-23", "Jonas Petersen / Tablet Schichtbüro-02", "Personalakte 20417"),
        doc("K13_Zurueckweisung", 13, "Muster ./. Seewerk Präzisionsguss GmbH – Ihre Kündigung vom 05.11.2026", [132], "2026-11-11", LAWYER, EMPLOYER),
        doc("K13_Antwort", 13, "Antwort auf Ihr Schreiben vom 11.11.2026 (Auszug)", [134], "2026-11-13", recipient=LAWYER),
        doc("K14_Anwaltsschreiben", 14, "Muster ./. Seewerk Präzisionsguss GmbH", range(144, 152), "2026-11-12", LAWYER, EMPLOYER),
        doc("K14_Antwort", 14, "Antwort auf Ihr Schreiben vom 12.11.2026 (Auszug)", [153], "2026-11-18", recipient=LAWYER),
    ]


def write_docx(path, item, additions):
    document = Document()
    section = document.sections[0]
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    section.top_margin, section.bottom_margin = Cm(1.9), Cm(1.8)
    section.left_margin = section.right_margin = Cm(2.2)
    section.different_first_page_header_footer = True
    normal = document.styles["Normal"]
    normal.font.name, normal.font.size = "Times New Roman", Pt(11)
    normal.paragraph_format.space_after = Pt(7)
    normal.paragraph_format.line_spacing = 1.08
    for name, size in (("Title", 16), ("Heading 1", 12), ("Heading 2", 11)):
        style = document.styles[name]
        style.font.name, style.font.size, style.font.color.rgb = "Times New Roman", Pt(size), RGBColor(0, 0, 0)
    head = section.header.paragraphs[0]
    head.text = item["sender"].split("\n")[0]
    head.runs[0].font.size = Pt(9)
    for line in item["sender"].split("\n"):
        paragraph = document.add_paragraph(line)
        paragraph.paragraph_format.space_after = Pt(1)
    document.add_paragraph("")
    document.add_paragraph(item["recipient"])
    date = datetime.fromisoformat(item["date"]).strftime("%d.%m.%Y")
    p = document.add_paragraph(date)
    p.alignment = 2
    document.add_paragraph(item["title"], "Heading 1")
    if item.get("reference"):
        document.add_paragraph(item["reference"])
    content = list(item["blocks"])
    # Ergänzungen stehen vor der Zeichnung, nicht hinter einer bereits abgeschlossenen Urkunde.
    insert_at = len(content)
    if content and "text" in content[-1] and re.search(r"gez\.|i\. A\.|Mit freundlichen", content[-1]["text"]):
        insert_at -= 1
    for index, block in enumerate(content):
        if block.get("text", "").startswith("i. A."):
            insert_at = index
            break
    for text in reversed(additions):
        if not any(text in block.get("text", "") for block in content):
            content.insert(insert_at, {"text": text})
    for block in content:
        if "rows" in block:
            rows = block["rows"]
            table = document.add_table(rows=1, cols=len(rows[0]))
            table.style = "Table Grid"
            for cell, value in zip(table.rows[0].cells, rows[0]):
                cell.text = value
                for run in cell.paragraphs[0].runs:
                    run.bold = True
            table.rows[0]._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
            for values in rows[1:]:
                for cell, value in zip(table.add_row().cells, values):
                    cell.text = value
            for row in table.rows:
                row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
            document.add_paragraph("")
        else:
            text = block["text"]
            if item["key"] == "K14_Anwaltsschreiben" and block in item["blocks"][1:7]:
                text = str(item["blocks"].index(block)) + ". " + text
            paragraphs = re.split(r" (?=[1-4]\. [A-ZÄÖÜ])", text) if item["key"] == "K01_Aenderung2019" else [text]
            for value in paragraphs:
                paragraph = document.add_paragraph(value)
                paragraph.paragraph_format.widow_control = True
                if item["key"] == "K01_Arbeitsvertrag" and additions and value == additions[0]:
                    paragraph.paragraph_format.page_break_before = True
    for footer in (section.footer.paragraphs[0], section.first_page_footer.paragraphs[0]):
        footer.text = "Seite "
        field = OxmlElement("w:fldSimple")
        field.set(qn("w:instr"), "PAGE")
        footer._p.append(field)
        footer.runs[0].font.size = Pt(9)
    paragraphs = list(document.paragraphs)
    paragraphs += [paragraph for table in document.tables for row in table.rows
                   for cell in row.cells for paragraph in cell.paragraphs]
    for paragraph in paragraphs:
        for run in paragraph.runs:
            fonts = run._r.get_or_add_rPr().get_or_add_rFonts()
            fonts.attrib.clear()
            for key in ("ascii", "hAnsi", "eastAsia", "cs"):
                fonts.set(qn("w:" + key), "Times New Roman")
    properties = document.core_properties
    properties.author = properties.last_modified_by = "Klotzkette"
    properties.created = properties.modified = datetime.fromisoformat(item["date"]).replace(tzinfo=None)
    properties.title, properties.comments = item["title"], ""
    document.save(path)
    # Zeitstempel der Containerdateien dürfen den gleichen Aktenbestand nicht verändern.
    content = io.BytesIO(path.read_bytes())
    with zipfile.ZipFile(content) as original:
        normalized = io.BytesIO()
        with zipfile.ZipFile(normalized, "w", zipfile.ZIP_DEFLATED) as target:
            for name in sorted(original.namelist()):
                entry = zipfile.ZipInfo(name, STAMP)
                entry.compress_type = zipfile.ZIP_DEFLATED
                target.writestr(entry, original.read(name))
        path.write_bytes(normalized.getvalue())


def paragraph_pdf(item):
    stream = io.BytesIO()
    style = ParagraphStyle("Text", fontName="SeewerkTimes", fontSize=11, leading=15, spaceAfter=10)
    title = ParagraphStyle("Titel", parent=style, fontName="SeewerkBold", fontSize=15, leading=19, spaceAfter=18)
    story = [Paragraph(escape(item["sender"]).replace("\n", "<br/>"), style), Spacer(1, 18),
             Paragraph(escape(item["title"]), title)]
    for block in item["blocks"]:
        if "rows" in block:
            table = PDFTable([[Paragraph(escape(value), style) for value in row] for row in block["rows"]])
            table.setStyle(TableStyle([("GRID", (0,0), (-1,-1), .3, "#9CA3AF"), ("VALIGN", (0,0), (-1,-1), "TOP")]))
            story.append(table)
        else:
            story.append(Paragraph(escape(block["text"]), style))
    SimpleDocTemplate(stream, pagesize=A4, rightMargin=62, leftMargin=62, topMargin=60, bottomMargin=55,
                      title=item["title"], author="Klotzkette").build(story)
    return stream.getvalue()


def write_mail(path, item, expanded, directory):
    mail = EmailMessage(policy=policy.SMTP)
    mail["From"], mail["To"] = item["sender"], item["recipient"]
    mail["Date"] = format_datetime(datetime.fromisoformat(item["date"]))
    mail["Subject"] = item["title"]
    mail["Message-ID"] = f"<{item['key'].lower()}.{item['date'][:10]}@postfach.example>"
    mail["MIME-Version"] = "1.0"
    mail["X-Mailer"] = "Mail"
    if item["key"] == "K05_Bonusantwort":
        mail["In-Reply-To"] = mail["References"] = "<k05_bonusforderung.2026-04-14@postfach.example>"
    text = "\n\n".join(block["text"] for block in item["blocks"])
    if expanded and item["key"] == "K05_Bonusantwort":
        from email.parser import BytesParser
        previous = BytesParser(policy=policy.default).parsebytes((directory / "K05_Bonusforderung.eml").read_bytes())
        text += "\n\n----- Ursprüngliche Nachricht -----\nVon: Daniel Muster\nDatum: 14.04.2026, 21:17 Uhr\nBetreff: Widerspruch Bonus 2025\n\n" + previous.get_body(preferencelist=("plain",)).get_content()
    mail.set_content(text, charset="utf-8")
    for name in item.get("attachments", []):
        source = directory / name
        mail.add_attachment(source.read_bytes(), maintype="application", subtype="vnd.openxmlformats-officedocument.wordprocessingml.document", filename=name)
    if mail.is_multipart():
        mail.set_boundary("seewerk-" + hashlib.sha256(text.encode("utf-8")).hexdigest()[:24])
    path.write_bytes(mail.as_bytes())


def draw_screens(directory):
    """Erzeugt die erfundene App-Oberfläche unmittelbar aus denselben Aktenwerten."""
    regular = ImageFont.truetype(str(FONTS / "Arial.ttf"), 26)
    small = ImageFont.truetype(str(FONTS / "Arial.ttf"), 21)
    bold = ImageFont.truetype(str(FONTS / "Arial Bold.ttf"), 37)
    results = []
    history = [("13.10.2026", "06:15–07:02", "5,8 km"), ("16.10.2026", "07:05–07:48", "6,1 km")]
    for n in range(28):
        from datetime import timedelta
        date = datetime(2026, 10, 11) - timedelta(days=n*2)
        history.append((date.strftime("%d.%m.%Y"), "18:10–18:52", f"{4+n%3},2 km"))
    for index in range(5):
        image = Image.new("RGB", (1480, 1120), "#f4f6f7")
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, 1480, 100), fill="#174d42")
        draw.text((45, 25), "RunTrack", font=bold, fill="white")
        draw.text((780, 36), "Dani M.  |  Konstanz", font=regular, fill="white")
        draw.text((45, 122), "Ruhepuls 52  |  Wochenziel 25 km", font=small, fill="#344b49")
        if index < 2:
            date, period, distance = history[index]
            draw.text((45, 180), f"Morgenlauf · {date}", font=bold, fill="#152c29")
            draw.text((45, 240), f"{period} Uhr     {distance}", font=bold, fill="#152c29")
            draw.rectangle((45, 315, 1415, 760), fill="#e6eddf")
            draw.polygon([(800,315),(1415,315),(1415,760),(1050,760),(920,570)], fill="#b9dce8")
            for x in (180,390,580,730):
                draw.line([(x,330),(x+70,740)], fill="white", width=16)
            for y in (400,540,670):
                draw.line([(60,y),(920,y-35)], fill="white", width=12)
            points=[(220,460),(450,420),(720,440),(880,525),(1000,670),(740,700),(430,590),(220,460)]
            draw.line(points, fill="#d25225", width=8, joint="curve")
            draw.text((110,345), "Am Gießereihof", font=small, fill="#344b49")
            draw.text((840,695), "Seeufer / Mettnau" if index else "Seeufer Radolfzell", font=small, fill="#344b49")
            draw.text((45,790), "Herzfrequenz", font=regular, fill="#152c29")
            draw.line([(65+x*13, 925-(x%9)*6-((x*7)%13)) for x in range(100)], fill="#b33b46", width=3)
            draw.text((45,965), "Profil / Aktivitäten / Morgenlauf", font=small, fill="#344b49")
        else:
            start=(index-2)*10
            draw.text((45,180), f"Letzte Aktivitäten · {start+1}–{start+10} von 30", font=bold, fill="#152c29")
            ordered = sorted(history, key=lambda item: datetime.strptime(item[0], "%d.%m.%Y"), reverse=True)
            for row,(date,period,distance) in enumerate(ordered[start:start+10]):
                y=260+row*70
                draw.line((45,y-10,1415,y-10), fill="#d0d9d5", width=1)
                draw.text((55,y), date, font=regular, fill="#152c29")
                draw.text((390,y), "Laufen", font=regular, fill="#152c29")
                draw.text((670,y), period+" Uhr", font=regular, fill="#152c29")
                draw.text((1190,y), distance, font=regular, fill="#152c29")
        draw.rectangle((0, 1050, 1480,1120), fill="white")
        draw.text((35,1075), "Erstellt am 23.10.2026, 14:12 Uhr, Gerät Tablet Schichtbüro-02, J. Petersen", font=small, fill="#394746")
        name=f"K12_Screenshot_{index+1:02d}.png"
        image.save(directory/name)
        results.append({"key":Path(name).stem,"filename":name,"annex":12,"title":f"RunTrack Bildschirm {index+1}","date":"2026-10-23","blocks":[]})
    return results


def write_zip(path, entries):
    with zipfile.ZipFile(path, "w") as archive:
        for name,data in [("README.txt",NOTICE_BYTES),*entries]:
            info=zipfile.ZipInfo(name,STAMP)
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644<<16
            archive.writestr(info,data)


def annex_pdf(writer, number):
    for page in writer.pages:
        overlay = io.BytesIO()
        width, height = float(page.mediabox.width), float(page.mediabox.height)
        surface = canvas.Canvas(overlay, pagesize=(width, height), invariant=1)
        surface.setFont("Times-Roman", 10)
        surface.drawRightString(width-40, height-26, f"Anlage K{number}")
        surface.save()
        page.merge_page(PdfReader(io.BytesIO(overlay.getvalue())).pages[0])
    stream = io.BytesIO()
    writer.write(stream)
    return stream.getvalue()


def downloads(slug, prefix=BASE+"/"):
    total = prefix + slug + "_gesamt.pdf" if prefix == "downloads/" else "gesamt-pdf/" + slug + "_gesamt.pdf"
    return f"""{NOTICE_MARKDOWN}

| Format | Download |
| --- | --- |
| Gesamt-PDF | [Durchsuchbare Gesamtakte]({total}) |
| Einzel-PDF-ZIP | [Jedes tatsächliche Dokument als eigenes PDF]({prefix}testakte-{slug}-einzelpdfs.zip) |
| Akten-ZIP | [Bearbeitbare Originaldateien]({prefix}testakte-{slug}.zip) |
| Anlagen K1 bis K14 | [Vierzehn geordnete Anlagen-PDFs]({prefix}testakte-{slug}-anlagen-k1-k14.zip) |"""


def write_register():
    small = json.loads((ROOT / "scripts/data/kuendigungsschutz-akten.json").read_text(encoding="utf-8"))
    reports = json.loads((PLUGIN / "testakte/pruefung/seewerk-bestand.json").read_text(encoding="utf-8"))
    sections = []
    for number, case in enumerate(small, 1):
        slug = case["slug"]
        sections.append(f"## 1.{number}. {case['title']}\n\n{case['summary']}\n\n"
                        f"[Originale und Verzeichnis](../../testakten/{slug}/README.md)\n\n"
                        + module("build-kuendigungsschutz-akten").download_table(case))
    for number, report in enumerate(reports, 4):
        slug = report["slug"]
        sections.append(f"## 1.{number}. {report['title']}\n\n"
                        f"{report['documents']} Originale, {report['pages']} PDF-Seiten, vierzehn logische Kernanlagen. "
                        "Simulierter Bearbeitungstag: 23.11.2026.\n\n"
                        f"[Originale und Dokumentenverzeichnis](../../testakten/{slug}/README.md)\n\n"
                        + downloads(slug, "downloads/"))
    text = """# 1. Kündigungsschutz Aktenregister

Drei kleine Arbeitsakten und zwei Fassungen des großen Kündigungsschutzmandats Muster / Seewerk. Jede Fassung liefert eine Gesamt-PDF, ein flaches ZIP mit einer PDF je tatsächlichem Dokument und ein flaches ZIP der nativen Originale. Bei Seewerk steht zusätzlich ein ausdrücklich gebündelter Anlagen-Satz mit genau K1 bis K14 bereit.

Die drei kleinen Akten haben den Aktenstand 22.10.2026 und bleiben unverändert. Die beiden Seewerk-Fassungen verwenden den simulierten Bearbeitungstag 23.11.2026. Der tatsächliche Quellenprüfstand ist 22.10.2026. Das [Referentenmaterial](../referentenmaterial/README.md) bleibt vollständig außerhalb der Akten-Downloads.

<!-- reserved-example-contacts -->

Personen, Unternehmen, Anschriften und Vorgangsnummern sind erfunden. Kontaktadressen verwenden reservierte .example-Domains. Die App-Bilder sind Rekonstruktionen einer erfundenen Oberfläche. Kein Download enthält Lösungsblätter oder nachträglich erfundene Gerichtsentscheidungen. README.txt steht in jedem ZIP zuerst; in den PDFs steht kein Warnhinweis. Alle folgenden Links führen auf vorhandene lokale Dateien.

""" + "\n\n".join(sections) + "\n"
    (PLUGIN / "testakte/README.md").write_text(text, encoding="utf-8")


def build():
    source=json.loads(DATA.read_text(encoding="utf-8"))
    expanded=json.loads(EXPANSION.read_text(encoding="utf-8"))
    basis=module("build-kuendigungsschutz-akten")
    fonts=basis.configure_office_fonts()
    cisg=module("build-cisg-akten")
    renderer=module("build-testakten-einzelpdf-zips")
    cisg.configure_text_fonts(renderer)
    pdfmetrics.registerFont(TTFont("SeewerkTimes",str(FONTS/"Times New Roman.ttf")))
    pdfmetrics.registerFont(TTFont("SeewerkBold",str(FONTS/"Times New Roman Bold.ttf")))
    target=PLUGIN/"testakte/downloads"
    target.mkdir(exist_ok=True,parents=True)
    reports=[]
    for variant,slug in enumerate(SLUGS):
        directory=ROOT/"testakten"/slug
        directory.mkdir(exist_ok=True,parents=True)
        items=core_documents(source["blocks"])
        if variant:
            # Die ursprünglich fehlende Gehaltsmitteilung wird erst am 23.11. nachgereicht.
            next(item for item in items if item["key"] == "K01_Gehaltsstand")["date"] = "2026-11-10"
            for extra in expanded["extras"]:
                filename=extra["filename"]
                for original,replacement in (("ä","ae"),("ö","oe"),("ü","ue"),("ß","ss"),("Ä","Ae"),("Ö","Oe"),("Ü","Ue")):
                    filename=filename.replace(original,replacement)
                items.append({"key":Path(filename).stem,"filename":filename,"annex":None,
                              "title":extra["subject"],"date":extra["date"],"sender":extra["sender"],
                              "recipient":extra["recipient"],"reference":extra["reference"],
                              "blocks":[{"text":text} for text in extra["paragraphs"]],
                              **({"rows":extra["rows"]} if extra.get("rows") else {})})
                if extra["id"] == "E16":
                    items[-1]["attachments"] = ["K11_Kuendigung.docx", "E01_Gehaltsmitteilung_Januar_2025.docx"]
            items+=draw_screens(directory)
        for item in items:
            path=directory/item["filename"]
            suffix=path.suffix
            additions=expanded["core_additions"].get(item["key"],[]) if variant else []
            if suffix==".docx":
                write_docx(path,item,additions)
            elif suffix==".eml":
                if item["key"].startswith("E") and "T" not in item["date"]:
                    item["date"] += "T10:15:00" + ("+02:00" if "-06-" in item["date"] else "+01:00")
                write_mail(path,item,bool(variant),directory)
            elif suffix==".txt":
                path.write_text(item["sender"]+"\n"+item["title"]+"\n"+item["date"]+"\n\n"+"\n\n".join(block["text"] for block in item["blocks"])+"\n",encoding="utf-8")
            elif suffix==".pdf":
                path.write_bytes(paragraph_pdf(item))
            elif suffix==".csv":
                with path.open("w",encoding="utf-8-sig",newline="") as stream:
                    csv.writer(stream,delimiter=";").writerows(item["rows"])
        subprocess.run([os.environ.get("NODE_BINARY","node"),str(ROOT/"scripts/build-seewerk-zeiterfassung.mjs"),str(directory)],check=True)
        paths=[directory/item["filename"] for item in items]
        cache=render_office_batch(paths)
        writer=PdfWriter()
        original_entries=[]
        single_entries=[]
        annex_writers={number:PdfWriter() for number in range(1,15)}
        documents=[]
        for path,item in zip(paths,items):
            pdf=renderer.render_document_pdf(path,directory,cache)
            if pdf_content_errors(pdf):
                raise ValueError(path.name)
            reader=PdfReader(io.BytesIO(pdf))
            start=len(writer.pages)
            for page in reader.pages:
                writer.add_page(page)
                if item["annex"]:
                    annex_writers[item["annex"]].add_page(page)
            writer.add_outline_item(item["title"],start)
            original_entries.append((path.name,path.read_bytes()))
            single_entries.append((path.stem+".pdf",pdf))
            documents.append({"file":path.name,"title":item["title"],"annex":item["annex"],"pages":len(reader.pages),"start_page":start+1,
                              "sha256":hashlib.sha256(path.read_bytes()).hexdigest(),"pdf_sha256":hashlib.sha256(pdf).hexdigest()})
        writer.add_metadata({"/Title":"Muster ./. Seewerk – "+("Lebensakte" if variant else "Konzeptfassung"),"/Author":"Klotzkette"})
        output=directory/"gesamt-pdf"/(slug+"_gesamt.pdf")
        output.parent.mkdir(exist_ok=True)
        writer.write(output)
        (target/output.name).write_bytes(output.read_bytes())
        write_zip(target/f"testakte-{slug}.zip",original_entries)
        write_zip(target/f"testakte-{slug}-einzelpdfs.zip",single_entries)
        annex_entries=[]
        for number,annex in annex_writers.items():
            annex_entries.append((f"K{number:02d}.pdf",annex_pdf(annex,number)))
        write_zip(target/f"testakte-{slug}-anlagen-k1-k14.zip",annex_entries)
        title="Muster ./. Seewerk – "+("ausführliche Lebensakte" if variant else "vorlagengetreue Konzeptfassung")
        rows="\n".join(f"| [{entry['file']}]({entry['file']}) | {('K'+str(entry['annex'])) if entry['annex'] else 'Ergänzung'} | {entry['title']} | {entry['pages']} |" for entry in documents)
        readme=f"""# 1. {title}

Arbeitsunterlagen zum Kündigungsschutzmandat eines Schichtleiters in Radolfzell. Simulierter Bearbeitungstag ist Montag, der 23.11.2026. Die Kündigung ist am 06.11.2026 zugegangen. Das Kalenderdatum dieser Akte ist von ihrem Erstellungsdatum zu unterscheiden.

## 1.1. Benutzung

{'Die vierzehn Anlagen des Konzeptpapiers sind inhaltlich übernommen. Typografie und ausgeschriebene Normbezeichnungen sind vereinheitlicht. Mehrteilige Anlagen werden dokumentweise getrennt; die historischen Vertragsauszüge bleiben ausdrücklich Auszüge.' if not variant else 'Die vierzehn Kernanlagen enthalten weiterhin sämtliche Aussagen der Konzeptfassung. Hinzu kommen ausführlichere Schreiben, Abrechnungsunterlagen, Korrespondenz, technische Vorgänge und rekonstruierte Ansichten der erfundenen Lauf-App. Die Ergänzungen sind ein gesonderter Bestand und keine heimlich hinzugefügten Klageanlagen.'}

{len(items)} Originaldateien, {len(writer.pages)} PDF-Seiten, vierzehn logische Kernanlagen. Im Einzel-PDF-ZIP ist jedes eigenständige Dokument eine eigene PDF-Datei. Der zusätzliche Anlagen-Satz bündelt dagegen bewusst genau K1 bis K14; Ergänzungen außerhalb dieser Nummerierung sind dort nicht enthalten. Der Gesamtband enthält alle Dokumente in der unten bezeichneten Reihenfolge.

Die persönlichen Zusatzangaben aus dem Mandantengespräch und die rechtliche Gegenprüfung stehen nur im getrennten Referentenmaterial des Plugins. Sie werden keinem dieser Downloads beigelegt. Es sind keine Musterklage, Bewertung, Lösungsmatrix oder späteren Gerichtsentscheidungen enthalten. Eine Anlagenzuordnung ist kein vorweggenommener Klageentwurf.

<!-- reserved-example-contacts -->

Alle Personen, Unternehmen, Anschriften und Vorgangsnummern sind erfunden. Kontaktadressen verwenden reservierte .example-Domains. Die App-Ansichten sind Rekonstruktionen einer erfundenen Oberfläche und keine Aufnahmen eines realen Kontos. Originale und PDFs enthalten bewusst die unterschiedlichen Tatsachenbehauptungen ihrer jeweiligen Absender.

<!-- BEGIN gesamt-pdf-section (autogen) -->

## 1.2. Downloads

{downloads(slug)}

<!-- END gesamt-pdf-section (autogen) -->

Alle ZIPs sind flach. README.txt steht zuerst und enthält den zweisprachigen Hinweis. PDFs enthalten weder Warnhinweis noch Lösungsseiten. Native Dateien sind zusätzlich einzeln unten zugänglich; der Gehaltsstand von 2025 ist nicht in die unterschriebene Änderungsvereinbarung von 2019 hineindatiert.

## 1.3. Dokumentenverzeichnis

{NOTICE_MARKDOWN}

| Original | Anlage | Gegenstand | Seiten |
| --- | --- | --- | ---: |
{rows}

[Plugin-Aktenregister](../../arbeitsrecht-kuendigungsschutzklagewerkstatt/testakte/README.md) · [Alle Fallakten](../README.md)
"""
        (directory/"README.md").write_text(readme,encoding="utf-8")
        report={"slug":slug,"title":title,"documents":len(items),"pages":len(writer.pages),"files":documents}
        reports.append(report)
        print(f"{slug}: {len(items)} Originale, {len(writer.pages)} Seiten",flush=True)
    (PLUGIN/"testakte/pruefung/seewerk-bestand.json").write_text(json.dumps(reports,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    write_register()
    fonts.cleanup()


if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--import-source",type=Path)
    arguments=parser.parse_args()
    if arguments.import_source:
        import_source(arguments.import_source)
    else:
        build()
