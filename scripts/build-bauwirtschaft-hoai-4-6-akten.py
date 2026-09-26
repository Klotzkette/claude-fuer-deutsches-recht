#!/usr/bin/env python3
"""Drei eigenständige Originalakten für LPH 4 bis 6. Autor: Klotzkette."""
from __future__ import annotations

import argparse
import csv
from datetime import datetime
from email import policy
from email.message import EmailMessage
from email.utils import format_datetime
import json
from pathlib import Path
import subprocess
import tempfile
from xml.sax.saxutils import escape
from zoneinfo import ZoneInfo

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import Image, ImageDraw, PngImagePlugin
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, A3, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from akten_build_runtime import node_binary, screen_font, serif_font_path
from readme_decimal_headings import normalize_decimal_headings
from testakte_disclaimer import NOTICE_MARKDOWN

ROOT = Path(__file__).resolve().parents[1]
AUTHOR = "Klotzkette"
CASES = {
    4: {"slug": "bauwirtschaft-hoai-4-genehmigung-werkhof-celle", "code": "CE-WU26", "city": "Celle",
        "title": "HOAI Leistungsphase 4: Werkhof Uhlenried in Celle - Bauantrag, Nachforderung und Grenzabstand",
        "short": "Werkhof Uhlenried", "date": "2026-09-23", "count": 17},
    5: {"slug": "bauwirtschaft-hoai-5-ausfuehrung-schule-hameln", "code": "HM-BA26", "city": "Hameln",
        "title": "HOAI Leistungsphase 5: Schule Brückenanger in Hameln - Flurdetails, Fachkollision und Montageplan",
        "short": "Schule Brückenanger", "date": "2026-09-24", "count": 17},
    6: {"slug": "bauwirtschaft-hoai-6-lv-sporthalle-peine", "code": "PE-OB26", "city": "Peine",
        "title": "HOAI Leistungsphase 6: Sporthalle Okerbogen in Peine - Mengen, Langtext-LV und Kostenvergleich",
        "short": "Sporthalle Okerbogen", "date": "2026-09-24", "count": 18},
}
ACTORS = {
 4: {
  "bau": ("Stadt Celle · Gebäudebetrieb Uhlenried", "Uhlenrieder Weg 26 · 29225 Celle", "f.seidel@werkhof-uhlenried.example", "Fiona Seidel, Projektleitung"),
  "plan": ("Cordes Bauatelier", "Am Lindenbogen 14 · 29225 Celle", "r.cordes@cordes-bauatelier.example", "Rieke Cordes, Architektin"),
  "amt": ("Stadt Celle · Bauaufsicht", "Verwaltungshof 8 · 29221 Celle", "bauaufsicht@celle-verfahren.example", "Mareike Drenker, im Auftrag"),
  "statik": ("Hohenfeld Tragwerk", "An der Feldmühle 6 · 29227 Celle", "j.wendt@hohenfeld-tragwerk.example", "Jorit Wendt, Tragwerksplanung"),
  "brand": ("Kammann Brandschutzplanung", "Birkenstieg 19 · 29313 Hambühren", "n.kammann@kammann-brand.example", "Nele Kammann, Brandschutzplanung"),
  "mess": ("Vermessungsbüro Hohenfeld", "Am Kieselgarten 3 · 29223 Celle", "p.hohenfeld@vermessung-hohenfeld.example", "Peer Hohenfeld, Vermessung"),
  "nachbar": ("Lüders Gartenbedarf GmbH", "Uhlenrieder Weg 28 · 29225 Celle", "s.lueders@lueders-garten.example", "Saskia Lüders, Geschäftsführerin"),
  "wasser": ("Ingenieurbüro Beeken", "Am Südanger 7 · 29227 Celle", "planung@beeken-wasser.example", "Ole Beeken, Entwässerungsplanung"),
 },
 5: {
  "bau": ("Schulbau Brückenanger gGmbH", "Brückenanger 12 · 31787 Hameln", "j.vollmer@schulbau-brueckenanger.example", "Janne Vollmer, Geschäftsführerin"),
  "plan": ("Nordfeld Architektur", "Am Buchenhof 9 · 31785 Hameln", "l.wernicke@nordfeld-architektur.example", "Lea Wernicke, Architektin"),
  "amt": ("Stadt Hameln · Bauaufsicht", "Verwaltungsbogen 4 · 31785 Hameln", "post@hameln-bauverfahren.example", "Tessa Riemer, im Auftrag"),
  "statik": ("Rautenberg Tragwerksbüro", "An der Sandbreite 6 · 31860 Emmerthal", "i.rautenberg@rautenberg-tragwerk.example", "Iven Rautenberg, Tragwerksplaner"),
  "tga": ("Behrens Gebäudetechnik", "Am Hainfeld 15 · 31789 Hameln", "t.behrens@behrens-tga.example", "Tammo Behrens, Fachplaner Lüftung"),
  "metall": ("Lenz Metallbau GmbH", "Gewerbeanger 18 · 31855 Aerzen", "f.lenz@lenz-metallbau.example", "Fenja Lenz, technische Leitung"),
  "brand": ("Röwe Brandschutzkonzepte", "Am Wiesensteg 2 · 31787 Hameln", "s.roewe@roewe-brandschutz.example", "Sören Röwe, Brandschutzplanung"),
 },
 6: {
  "bau": ("Sportgemeinschaft Okerbogen e.V.", "Am Sportanger 8 · 31226 Peine", "t.riekert@sg-okerbogen.example", "Torben Riekert, Vorsitzender"),
  "plan": ("Falkenhain Architektur", "Am Lindenrain 5 · 31224 Peine", "m.falkenhain@falkenhain-architektur.example", "Mira Falkenhain, Architektin"),
  "tga": ("Harms Gebäudetechnik", "An der Koppel 11 · 31228 Peine", "e.harms@harms-tga.example", "Enno Harms, Fachplaner"),
  "metall": ("Büro Kestner Bauelemente", "Am Werkanger 4 · 31241 Ilsede", "planung@kestner-bauelemente.example", "Sina Kestner, Planung Bauelemente"),
  "brand": ("Lindau Brandschutz", "Am Weidenhof 7 · 31224 Peine", "a.lindau@lindau-brand.example", "Arne Lindau, Brandschutzplanung"),
  "nutzer": ("Sportgemeinschaft Okerbogen · Hallenbetrieb", "Am Sportanger 8 · 31226 Peine", "h.brock@sg-okerbogen.example", "Hella Brock, Hallenwartin"),
 },
}
RECORDS: dict[int, list[dict]] = {4: [], 5: [], 6: []}
INVENTORY: dict[int, list[tuple[str, str]]] = {4: [], 5: [], 6: []}


def register_fonts():
    for name, bold in (("CaseSerif", False), ("CaseSerifB", True)):
        pdfmetrics.registerFont(TTFont(name, str(serif_font_path(bold))))
    pdfmetrics.registerFontFamily("CaseSerif", normal="CaseSerif", bold="CaseSerifB", italic="CaseSerif", boldItalic="CaseSerifB")


BODY = ParagraphStyle("CaseBody", fontName="CaseSerif", fontSize=10.5, leading=13, spaceAfter=6)
SMALL = ParagraphStyle("CaseSmall", parent=BODY, fontSize=9, leading=11, spaceAfter=5)
HEAD = ParagraphStyle("CaseHead", parent=BODY, fontName="CaseSerifB", spaceBefore=10, spaceAfter=9, keepWithNext=True)
TITLE = ParagraphStyle("CaseTitle", parent=HEAD, fontSize=16, leading=19, spaceAfter=13)


def para(text, style=BODY):
    return Paragraph(escape(str(text)).replace("\n", "<br/>"), style)


def table(rows, widths=None):
    widths = widths or [495 / len(rows[0])] * len(rows[0])
    out = Table([[para(c, SMALL) for c in row] for row in rows], colWidths=widths, repeatRows=1, hAlign="LEFT")
    out.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e4e9ed")),
        ("GRID", (0, 0), (-1, -1), .3, colors.HexColor("#d9d9d9")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return out


def add(phase, number, name, date, issuer, recipient, title, sections, attachments=(), salutation="Sehr geehrte Damen und Herren,"):
    filename = f"{number:02d}_{name}"
    RECORDS[phase].append(dict(file=filename, date=date, issuer=issuer, recipient=recipient,
                               title=title, sections=sections, attachments=list(attachments), salutation=salutation))
    INVENTORY[phase].append((filename, title))


def inventory(phase, number, name, title):
    filename = f"{number:02d}_{name}"
    INVENTORY[phase].append((filename, title))
    return ROOT / "testakten" / CASES[phase]["slug"] / filename


def letter_pdf(phase, record, target):
    cfg = CASES[phase]
    issuer = ACTORS[phase][record["issuer"]]
    recipient = ACTORS[phase][record["recipient"]]
    def frame(c, doc):
        c.setFont("CaseSerifB", 13); c.drawString(50, 803, issuer[0])
        c.setFont("CaseSerif", 9); c.drawString(50, 788, issuer[1]); c.drawString(50, 775, issuer[2])
        c.setFont("CaseSerif", 8); c.drawString(50, 30, cfg["code"] + " · " + record["date"])
        c.drawRightString(545, 30, f"Seite {doc.page}")
    flow = [para(recipient[0] + "\n" + recipient[1], SMALL),
            para(f"{cfg['city']}, {datetime.fromisoformat(record['date']):%d.%m.%Y} · Bezug {cfg['code']}", SMALL),
            para(record["title"], TITLE), para(record["salutation"])]
    for item in record["sections"]:
        if isinstance(item, str): flow.append(para(item))
        elif item[0] == "h": flow.append(para(item[1], HEAD))
        elif item[0] == "t": flow.extend([table(item[1], item[2] if len(item) > 2 else None), Spacer(1, 8)])
    flow.append(KeepTogether([Spacer(1, 5), para("Mit freundlichen Grüßen"), para("gez. " + issuer[3]),
                             para("Anlagen: " + ("; ".join(record["attachments"]) or "keine"), SMALL)]))
    SimpleDocTemplate(str(target), pagesize=A4, leftMargin=50, rightMargin=50, topMargin=92, bottomMargin=49,
                      author=AUTHOR, title=record["title"], creator=AUTHOR).build(flow, onFirstPage=frame, onLaterPages=frame)


def letter_docx(phase, record, target):
    cfg = CASES[phase]; issuer = ACTORS[phase][record["issuer"]]; recipient = ACTORS[phase][record["recipient"]]
    doc = Document(); sec = doc.sections[0]
    sec.page_width = Cm(21); sec.page_height = Cm(29.7)
    sec.top_margin = Cm(1.8); sec.bottom_margin = Cm(1.8); sec.left_margin = Cm(2); sec.right_margin = Cm(2)
    for style in doc.styles:
        if style.type != 1: continue
        style.font.name = "Times New Roman"; style.font.size = Pt(11); style.font.color.rgb = RGBColor(0, 0, 0)
        style.paragraph_format.space_after = Pt(6)
        fonts = style.element.get_or_add_rPr().get_or_add_rFonts()
        for key in list(fonts.attrib):
            if key.endswith("Theme"): del fonts.attrib[key]
        for key in ("ascii", "hAnsi", "eastAsia", "cs"): fonts.set(qn("w:" + key), "Times New Roman")
        for border in style.element.xpath("./w:pPr/w:pBdr"): border.getparent().remove(border)
    doc.styles["Title"].font.size = Pt(16)
    doc.styles["Heading 1"].font.size = Pt(12)
    doc.styles["Heading 1"].font.bold = True
    doc.styles["Heading 1"].paragraph_format.space_before = Pt(10)
    doc.styles["Heading 1"].paragraph_format.space_after = Pt(9)
    props = doc.core_properties; props.author = AUTHOR; props.last_modified_by = AUTHOR
    props.title = record["title"]; props.language = "de-DE"
    props.created = datetime.fromisoformat(record["date"]); props.modified = props.created
    doc.add_paragraph(issuer[0]).runs[0].bold = True
    doc.add_paragraph(issuer[1] + "\n" + issuer[2])
    doc.add_paragraph(recipient[0] + "\n" + recipient[1])
    doc.add_paragraph(f"{cfg['city']}, {datetime.fromisoformat(record['date']):%d.%m.%Y} · Bezug {cfg['code']}")
    doc.add_paragraph(record["title"], "Title"); doc.add_paragraph(record["salutation"])
    for item in record["sections"]:
        if isinstance(item, str):
            paragraph = doc.add_paragraph(item)
            if item.startswith("Menge: "): paragraph.paragraph_format.keep_with_next = True
        elif item[0] == "h": doc.add_paragraph(item[1], "Heading 1")
        elif item[0] == "t":
            grid = doc.add_table(rows=0, cols=len(item[1][0])); grid.style = "Table Grid"
            for index, row in enumerate(item[1]):
                cells = grid.add_row().cells
                grid.rows[index]._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
                if index == 0: grid.rows[index]._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
                for cell, value in zip(cells, row):
                    cell.text = str(value)
                    for p in cell.paragraphs:
                        for run in p.runs: run.font.size = Pt(10); run.bold = index == 0
                    if index == 0:
                        shade = OxmlElement("w:shd"); shade.set(qn("w:fill"), "E4E9ED"); cell._tc.get_or_add_tcPr().append(shade)
            doc.add_paragraph("")
    doc.add_paragraph("Mit freundlichen Grüßen").paragraph_format.keep_with_next = True
    doc.add_paragraph("gez. " + issuer[3]).paragraph_format.keep_with_next = True
    doc.add_paragraph("Anlagen: " + ("; ".join(record["attachments"]) or "keine"))
    footer = sec.footer.paragraphs[0]; footer.text = cfg["code"] + " · " + record["date"] + " · Seite "
    field = OxmlElement("w:fldSimple"); field.set(qn("w:instr"), "PAGE"); footer._p.append(field)
    doc.save(target)


def letter_eml(phase, record, target):
    issuer = ACTORS[phase][record["issuer"]]; recipient = ACTORS[phase][record["recipient"]]
    msg = EmailMessage(policy=policy.SMTP)
    msg["From"] = f"{issuer[3]} <{issuer[2]}>"; msg["To"] = f"{recipient[3]} <{recipient[2]}>"
    msg["Date"] = format_datetime(datetime.fromisoformat(record["date"] + "T14:25:00").replace(tzinfo=ZoneInfo("Europe/Berlin")))
    msg["Subject"] = CASES[phase]["code"] + " | " + record["title"]
    msg["Message-ID"] = f"<{CASES[phase]['code']}.{record['file'][:2]}.{record['date']}@projektpost.example>"
    text = [record["salutation"], ""]
    for item in record["sections"]:
        if isinstance(item, str): text.extend([item, ""])
        elif item[0] == "h": text.extend([item[1], ""])
        elif item[0] == "t": text.extend([" | ".join(map(str, row)) for row in item[1]])
    text += ["Mit freundlichen Grüßen", issuer[3], issuer[0], issuer[1], issuer[2],
             "Anlagen: " + ("; ".join(record["attachments"]) or "keine")]
    msg.set_content("\n".join(text), charset="utf-8")
    target.write_bytes(msg.as_bytes())


def define_celle():
    add(4, 1, "Planervertrag.pdf", "2026-02-12", "bau", "plan", "Planervertrag Werkhof Uhlenried", [
      "Wir bestätigen den am 12.02.2026 abgestimmten Auftrag für den Neubau einer Fahrzeug- und Gerätehalle mit Sozialtrakt auf dem Grundstück Uhlenrieder Weg 26, Gemarkung Uhlenried, Flur 7, Flurstück 118/6. Die Projektkennung lautet CE-WU26. Die Halle dient dem kommunalen Grünpflegebetrieb; eine öffentliche Annahmestelle für Abfälle ist nicht Gegenstand des Vorhabens.",
      ("h", "1 Leistungsgegenstand und Stufen"),
      "Beauftragt werden die Grundleistungen der Gebäudeplanung in den Leistungsphasen 1 bis 4. Der Abruf der Genehmigungsplanung ist mit Unterzeichnung erklärt. Die Leistungsphasen 5 bis 9 sind nicht beauftragt; ein späterer Abruf bedarf einer gesonderten Vereinbarung. Die Entwurfsplanung soll eine Halle mit 24,00 m mal 15,00 m Außenmaß und einen südöstlich anschließenden Sozialtrakt mit 12,00 m mal 8,00 m Außenmaß zugrunde legen.",
      "Cordes Bauatelier koordiniert die Beiträge von Hohenfeld Tragwerk, Kammann Brandschutzplanung und Ingenieurbüro Beeken. Diese Büros sind durch die Stadt gesondert beauftragt. Die Objektplanung übernimmt nicht die fachliche Erstellung ihrer statischen, brandschutztechnischen oder entwässerungstechnischen Nachweise. Ein amtlicher Lageplan wird separat beauftragt.",
      ("h", "2 Genehmigungsplanung und besondere Leistungen"),
      "Der Auftrag umfasst die Zusammenstellung und Erarbeitung der Bauvorlagen, die im vereinbarten Verfahren erforderliche Abstimmung, die autorisierte Einreichung und die Ergänzung beziehungsweise Anpassung des Antragsstands. Die Unterstützung bei nachbarlichen Erklärungen ist zunächst auf eine gemeinsame Ortsbesprechung begrenzt. Weitergehende Beschaffung von Zustimmungserklärungen, besondere technische Nachweise für eine Zustimmung im Einzelfall und Rechtsbehelfsverfahren sind nicht beauftragt.",
      "Die Stadt entscheidet über Änderungen von Nutzung, Baukörper und Kostenrahmen. Eine notwendige Korrektur eigener Planungsfehler wird durch diese Regelung nicht zu einer zusätzlich vergüteten Leistung. Für nachträglich geänderte Planungsziele sind Inhalt und Vergütung vor Durchführung abzustimmen, soweit die sofortige Bearbeitung nicht zur Abwendung eines konkreten Nachteils erforderlich ist.",
      ("h", "3 Vergütung und Termine"),
      "Für die beauftragte Stufe wird ein Pauschalhonorar von 68.000,00 EUR netto zuzüglich gesetzlicher Umsatzsteuer vereinbart. Die Baukostenberechnung vom 20.05.2026 ist mit 1.240.000,00 EUR netto als Planungsrahmen bestätigt; sie ist kein garantierter Endpreis. Der intern angestrebte Baubeginn ist der 15.03.2027. Eine Genehmigung bis zu einem bestimmten Datum wird nicht zugesagt.",
      ("h", "4 Vertretung und Dokumentation"),
      "Rieke Cordes darf den Bauantrag in der am 26.05.2026 von Fiona Seidel bestätigten Entwurfsfassung übermitteln und die technische Korrespondenz führen. Änderungen des Antragsgegenstands, Anträge auf Abweichung sowie rechtsverbindliche Nachbarerklärungen bedürfen einer vorherigen Freigabe durch Fiona Seidel. Kostenanerkenntnisse, Rechtsmittelverzicht und Beauftragung weiterer Unternehmen sind nicht umfasst.",
      "Planrevisionen sind mit Datum, Inhalt und tatsächlichem Übermittlungsnachweis zu dokumentieren. Die Stadt erhält nach jeder Einreichung das Anlagenverzeichnis und den Eingangsbeleg. Eine landesrechtliche Bauleiterfunktion und technische Prüfaufgaben werden mit diesem Vertrag nicht übertragen. Beide Parteien bestätigen die Vereinbarung in Textform am 12.02.2026: Fiona Seidel für die Stadt und Rieke Cordes für Cordes Bauatelier.",
    ])
    add(4, 2, "Entwurfsentscheidung.docx", "2026-05-26", "bau", "plan", "Entwurfsentscheidung und Betriebsdaten", [
      "Nach der Nutzerbesprechung vom 19.05.2026 bestätigen wir die Variante Osthof als Grundlage des Bauantrags. Der Rat hat für das Gesamtvorhaben 1.475.600,00 EUR brutto auf Basis der Kostenberechnung von 1.240.000,00 EUR netto bereitgestellt. Eine zusätzliche Flächenerweiterung ist darin nicht enthalten.",
      ("h", "1 Betrieb und Flächen"),
      "Am Standort arbeiten zwölf Beschäftigte in zwei zeitlich überlappenden Teams. Der Regelbetrieb findet montags bis freitags zwischen 06:30 und 17:30 Uhr statt. In der Halle werden vier kleine Pflegefahrzeuge, zwei Anhänger und handgeführte Geräte eingestellt. Kraftstoff wird nicht in Vorratstanks gelagert. Für Kleingebinde ist der im Brandschutzbeitrag gesondert beschriebene Schrank vorgesehen.",
      "Die Außenkontur der Halle beträgt 24,00 m mal 15,00 m. Der Sozialtrakt mit Umkleiden, Büro und Aufenthaltsraum hat 12,00 m mal 8,00 m Außenmaß. Der Hof muss eine durchgehend nutzbare Rangiertiefe von 10,00 m vor den Toren behalten. Besucher melden sich am Büro an; ein regelmäßiger Publikumsbetrieb ist nicht vorgesehen.",
      ("h", "2 Lage und Planfreigabe"),
      "Wir geben den Entwurf G-01/A und G-02/A vom 20.05.2026 für die weitere Antragsbearbeitung frei. Der nördliche Grenzabstand ist nach dem aktuellen Vermessungsstand einzutragen. Die in der Vorbesprechung verwendeten 3,00 m waren eine Entwurfsannahme und sind nicht als vermessen bestätigt.",
      "Eine Verkleinerung der Halle nach Norden ist aus betrieblicher Sicht möglich, wenn mindestens 14,60 m äußere Tiefe erhalten bleiben. Ob dies rechtlich und konstruktiv sinnvoll ist, ist noch nicht entschieden. Eine Abweichung von Grenzabstandsanforderungen ist nicht durch diesen Beschluss freigegeben. Bitte legen Sie eine solche Entscheidung gesondert vor.",
      ("h", "3 Weiterer Ablauf"),
      "Die Fachplaner sollen ihre Beiträge auf diesen Entwurfsstand beziehen. Der Termin 15.03.2027 bleibt Ziel für den Baustart; eine Vorwegnahme der behördlichen Entscheidung ist damit nicht verbunden. Für verbindliche Änderungen bleibt Fiona Seidel zuständig. Die Niederschrift gibt die am 26.05.2026 von Fiona Seidel bestätigte Entscheidung wieder.",
    ], attachments=("G-01/A Lageplan", "G-02/A Grundriss und Schnitt"))
    add(4, 5, "Baubeschreibung.docx", "2026-08-27", "plan", "amt", "Baubeschreibung zum Antrag CE-WU26", [
      "Für die Stadt Celle wird der Neubau des Werkhofs Uhlenried auf dem Grundstück Flur 7, Flurstück 118/6 beantragt. Die Beschreibung bezieht sich auf die Bauzeichnungen G-02/B und den Lageplan G-01/B vom 27.08.2026. Die bestehende offene Lagerfläche wird für Fahrzeughalle, Sozialtrakt und befestigten Hof neu geordnet.",
      ("h", "1 Gebäude und Nutzung"),
      "Die eingeschossige Halle hat 360,00 m² äußere Grundfläche. Vier nach Süden gerichtete Tore mit jeweils 3,50 m lichter Breite erschließen die Fahrzeugstände. Die nördliche Wand enthält keine Fenster und keine Türen. Der Sozialtrakt ist mit 96,00 m² äußerer Grundfläche angesetzt. Zwischen Halle und Sozialtrakt ist der im Brandschutzbeitrag bezeichnete Abschluss vorgesehen.",
      "Der Hallenboden liegt auf 42,10 m im verwendeten Projekthöhensystem. Die Traufe Nord liegt 4,80 m über Hallenfertigfußboden, der First 6,20 m. Das Gelände an der Nordseite liegt nach Vermessungsangabe zwischen 41,96 m und 42,02 m. Die genaue Zuordnung der Geländepunkte zum Schnitt ist im Blatt G-02/B dargestellt.",
      ("h", "2 Konstruktion und Technik"),
      "Die Halle erhält eine Stahlrahmenkonstruktion mit gedämmten Dach- und Wandpaneelen. Die Tragwerksplanung Hohenfeld vom 24.08.2026 beschreibt die Vorbemessung; die endgültige prüffähige Statik ist nicht Bestandteil dieser Beschreibung. Der Sozialtrakt wird in Mauerwerksbauweise errichtet. Die Gebäudeentwässerung wird in die von Beeken geplante Rückhaltung geführt.",
      "Das auf dem Dach anfallende Wasser wird gesammelt; eine Ableitung auf das Nachbargrundstück ist nicht vorgesehen. Die Außengeräte der Wärmeversorgung stehen an der Ostseite des Sozialtrakts. Die Betriebszeiten und Zahl der Beschäftigten entsprechen der Entwurfsentscheidung vom 26.05.2026. Eine Ladestation für externe Fahrzeuge oder öffentliche Werkstattnutzung ist nicht beantragt.",
      ("h", "3 Grundstück und Erschließung"),
      "Das Grundstück hat nach vorgelegter Vermessungsunterlage 2.880,00 m². Die Zufahrt erfolgt ausschließlich vom Uhlenrieder Weg im Süden. Acht Pkw-Stellplätze und zwölf Fahrradplätze sind im Lageplan dargestellt. Der Abstand der nördlichen Hallenaußenwand zur Grundstücksgrenze ist in G-01/B mit 2,70 m angegeben; im älteren Entwurf waren 3,00 m angesetzt.",
      "Die befestigte Hof- und Zufahrtsfläche beträgt im Rechenblatt 864,00 m². Die unbefestigte Fläche ergibt sich aus der Grundstücksfläche nach Abzug der dort einzeln aufgeführten Flächen. Dieser Flächennachweis ist keine abschließende Prüfung sämtlicher planungs- und bauordnungsrechtlicher Kennwerte.",
    ])
    add(4, 7, "Tragwerksbeitrag.pdf", "2026-08-24", "statik", "plan", "Vorbemessung der Hallenkonstruktion", [
      "Unser Beitrag bezieht sich auf G-02/A vom 20.05.2026 und die am 18.08.2026 übersandten Profilskizzen. Die Halle ist als fünf Rahmenachsen mit 6,00 m Achsabstand vorgesehen. Die äußere Tiefe beträgt 15,00 m. Die Lastannahmen aus Photovoltaik und Dachaufbau sind in der beigefügten Projektberechnung erfasst; diese Berechnung wird gesondert zur Prüfung vorgelegt.",
      ("h", "1 Planungsstand"),
      "Für den Bauantrag können die angegebenen Trauf- und Firsthöhen verwendet werden. Die vorliegende Stellungnahme ist keine Bescheinigung einer abgeschlossenen bautechnischen Prüfung. Fundamentabmessungen und Verbindungsmittel werden erst nach Abschluss der Baugrundabstimmung endgültig festgelegt. Bohrungen oder Änderungen an Rahmenquerschnitten dürfen aus diesem Schreiben nicht abgeleitet werden.",
      ("h", "2 Mögliche Verringerung der Hallentiefe"),
      "Eine Verringerung der äußeren Hallentiefe von 15,00 m auf 14,70 m ist konstruktiv grundsätzlich in der Rahmengeometrie darstellbar. Damit ist weder die neue Statik gerechnet noch eine Änderung freigegeben. Die Traufhöhe soll nach bisheriger Abstimmung unverändert bleiben. Eine Veränderung der nördlichen Stützenlage betrifft die Fundamentplanung und die Dachentwässerung.",
      "Bitte geben Sie uns den endgültigen Lage- und Schnittstand mit Bezug auf die vermessene Grenze. Wir benötigen die Entscheidung spätestens am 05.10.2026, wenn die Fachunterlagen für den nächsten Antragslauf rechtzeitig vorliegen sollen. Der Termin ist unser interner Bearbeitungsvorlauf und keine behördliche Frist.",
    ])
    add(4, 8, "Brandschutzbeitrag.pdf", "2026-08-25", "brand", "plan", "Brandschutzbeitrag zum Werkhofantrag", [
      "Die Stellungnahme betrifft den von Ihnen übersandten Hallenentwurf G-02/A und die Betriebsdaten vom 26.05.2026. Sie enthält die für die weitere Antragskoordination abgestimmten Angaben. Eine Genehmigung oder abschließende Bestätigung der gesamten Bauvorlage wird hiermit nicht erklärt.",
      ("h", "1 Nutzungsannahmen"),
      "Wir legen zwölf Beschäftigte, vier Pflegefahrzeuge und zwei Anhänger zugrunde. Die Halle wird nicht für Veranstaltungen genutzt. Kraftstoffe werden nur in betriebsüblichen Kleingebinden in einem dafür gesondert nachzuweisenden Schrank vorgehalten. Eine offene Lagerung an der Nordwand ist nicht Bestandteil unseres Ansatzes. Der Sozialtrakt besitzt einen eigenen Ausgang nach Süden.",
      ("h", "2 Nordwand und Grundstücksbezug"),
      "Die Nordwand ist im vorliegenden Entwurf öffnungslos. Im uns vorliegenden Lageplan ist ein Abstand von 3,00 m zur nördlichen Grenze dargestellt. Eine Verringerung dieses Abstands war nicht Gegenstand unserer Bearbeitung. Für einen abweichenden Grenzabstand benötigen wir den vermessenen Lageplan, die tatsächliche Wandhöhe und die vorgesehene Wand-/Dachausbildung.",
      "Eine bloße Zustimmung des Nachbarn würde die brandschutztechnische Beurteilung nicht ersetzen. Ob eine besondere Anforderung oder eine zusätzliche Maßnahme erforderlich wird, kann erst anhand des aktualisierten Satzes bewertet werden. Wir bestätigen deshalb derzeit keine Kompensationsmaßnahme für 2,70 m Abstand.",
      ("h", "3 Rettungswege und weitere Bearbeitung"),
      "Die im Grundriss dargestellten Ausgänge nach Süden und Osten sind freizuhalten. Die Flächen vor den Ausgängen dürfen nicht als feste Lagerplätze genutzt werden. Die genaue Türqualität am Übergang zum Sozialtrakt wird mit dem abschließenden Nachweis abgestimmt. Bitte übersenden Sie die endgültige Revision einschließlich Schnitt, damit keine unterschiedlichen Geometrien im Antragsverfahren verbleiben.",
    ])
    add(4, 9, "Bauantrag.pdf", "2026-09-02", "plan", "amt", "Bauantrag Neubau Werkhof Uhlenried", [
      "Namens und in Vollmacht der Stadt Celle beantragen wir die Baugenehmigung für den Neubau der Fahrzeug- und Gerätehalle mit Sozialtrakt auf dem Grundstück Uhlenrieder Weg 26, Gemarkung Uhlenried, Flur 7, Flurstück 118/6. Die Bauherrschaft wurde über die Übermittlung am heutigen Tag unterrichtet. Das Projekt wird unter CE-WU26 geführt.",
      ("h", "1 Antragsgegenstand"),
      "Beantragt sind eine eingeschossige Halle mit 24,00 m mal 15,00 m Außenmaß, ein Sozialtrakt mit 12,00 m mal 8,00 m Außenmaß sowie die in G-01/B dargestellte Erschließung. Maßgeblich sind die beigefügten Bauzeichnungen vom 27.08.2026. Eine öffentliche Abfallannahme, zusätzliche Lagerhalle oder Tankanlage ist nicht Gegenstand dieses Antrags.",
      ("h", "2 Bauvorlagen"),
      ("t", [["Kennung", "Unterlage", "Stand"], ["G-01/B", "Lageplan mit Grenzabstand Nord", "27.08.2026"], ["G-02/B", "Grundriss, Schnitt und Höhen", "27.08.2026"], ["BB-01", "Baubeschreibung", "27.08.2026"], ["FL-01", "Flächenberechnung", "27.08.2026"], ["BS-01", "Brandschutzbeitrag Kammann", "25.08.2026"], ["TW-01", "Tragwerksbeitrag Hohenfeld", "24.08.2026"]], [80, 300, 115]),
      "Der nördliche Grenzabstand ist im aktualisierten Lageplan mit 2,70 m dargestellt. Eine gesonderte Erklärung der Bauherrschaft zu einem Abweichungsantrag liegt uns noch nicht vor. Wir bitten um Mitteilung, welche ergänzenden Unterlagen für die Bearbeitung dieses Punkts benötigt werden. Der Antrag soll nicht als Erklärung einer nachbarlichen Zustimmung verstanden werden.",
      ("h", "3 Bevollmächtigung und Korrespondenz"),
      "Ansprechpartnerin der Bauherrschaft ist Fiona Seidel. Die technische Korrespondenz bitten wir über Rieke Cordes zu führen. Die Vollmacht ergibt sich aus dem Planervertrag vom 12.02.2026 in Verbindung mit der Entwurfsentscheidung vom 26.05.2026. Eine Erweiterung des Antragsgegenstands bleibt einer gesonderten Erklärung vorbehalten.",
    ], attachments=("G-01/B", "G-02/B", "BB-01", "FL-01", "BS-01", "TW-01"))
    add(4, 11, "Nachforderung.pdf", "2026-09-09", "amt", "plan", "Nachforderung zum Bauantrag CE-BA-2026-184", [
      "Der am 02.09.2026 eingegangene Antrag zum Werkhof Uhlenried wird unter dem Aktenzeichen CE-BA-2026-184 geführt. Bei der Vorprüfung wurden die nachstehenden Unstimmigkeiten festgestellt. Bitte reichen Sie die bezeichneten Unterlagen bis zum 30.09.2026 nach und ordnen Sie die Antwort den folgenden Ziffern zu.",
      ("h", "1 Nördliche Grundstücksgrenze"),
      "Im Lageplan G-01/B ist ein Abstand der Hallenaußenwand zur Nordgrenze von 2,70 m eingetragen. Der Brandschutzbeitrag geht dagegen von 3,00 m aus. Bitte legen Sie einen auf den Vermessungsstand bezogenen Schnitt mit Wandhöhe und Geländeangaben sowie eine nachvollziehbare Abstandsberechnung vor. Falls eine Abweichung beantragt werden soll, ist der Antrag konkret zu begründen und von der hierzu befugten Person zu veranlassen.",
      ("h", "2 Flächennachweis"),
      "Die Baubeschreibung nennt 864,00 m² Hof- und Zufahrtsfläche. Die schraffierte Fläche im Lageplan ist nicht eindeutig von den Stellplätzen abgegrenzt. Bitte erläutern Sie, ob die Stellplätze in diesem Ansatz enthalten sind, und reichen Sie eine übereinstimmende Flächenaufstellung nach. Die Grundstücksfläche von 2.880,00 m² ist durch den vorgelegten Vermessungsbezug zu belegen.",
      ("h", "3 Fachbeiträge"),
      "Die Beiträge zu Tragwerk und Brandschutz beziehen sich auf G-02/A. Bitte legen Sie die Bestätigung vor, welche Angaben auf den eingereichten Stand G-02/B übertragen werden können. Eine technische Bestätigung für einen gegenüber dem Fachbeitrag geänderten Grenzabstand liegt bislang nicht vor.",
      ("h", "4 Weiteres Verfahren"),
      "Die Eingangsquittung vom 02.09.2026 bestätigt den Eingang des dort genannten Dateisatzes, nicht dessen inhaltliche Vollständigkeit oder Genehmigungsfähigkeit. Über den Bauantrag ist noch nicht entschieden. Eine etwa benötigte Verlängerung der oben genannten Nachreichungsfrist ist mit konkreter Begründung vor Fristablauf anzufragen; eine Verlängerung ist derzeit nicht gewährt.",
      "Bitte teilen Sie bei Ihrer Antwort mit, ob die bisherige Geometrie beibehalten oder ein geänderter Plansatz vorgelegt wird. Dieses Schreiben enthält keine Zustimmung zu einer Ausführung mit 2,70 m Grenzabstand und keine Erlaubnis zum Baubeginn.",
    ])
    add(4, 12, "Vermessung.eml", "2026-09-14", "mess", "plan", "Nordgrenze und Bezugspunkte G-01/B", [
      "anbei die Erläuterung zu unserem bereits übergebenen Lagebezug V-26-118. Die nördliche Grenze liegt im Projektkoordinatensystem bei y = 48,00 m. Die in G-01/B dargestellte Nordkante der Halle liegt bei y = 45,30 m. Daraus ergibt sich senkrecht zur Grenze ein Abstand von 2,70 m. Die Grenzpunkte wurden am 17.08.2026 aufgenommen; eine Verschiebung der Grenze ist nicht Gegenstand unserer Unterlage.",
      "Die Grundstücksecken liegen bei (0,00/0,00), (60,00/0,00), (60,00/48,00) und (0,00/48,00). Die Fläche beträgt 2.880,00 m². Die Geländepunkte Nordwest 41,96 m und Nordost 42,02 m beziehen sich auf dasselbe Projekthöhensystem wie der Hallenfertigfußboden 42,10 m. Die alte Skizze mit 3,00 m war keine Vermessungszeichnung.",
      "Eine Verschiebung der Nordwand auf y = 45,00 m würde den geometrischen Abstand auf 3,00 m vergrößern. Ob dies die bauordnungsrechtlich erforderliche Tiefe erfüllt, haben wir nicht geprüft. Bitte verwenden Sie unsere Maße nicht als rechtliche Abstandsbescheinigung. Die Südwandlage y = 30,30 m bliebe bei der von Ihnen diskutierten Verkürzung unverändert.",
    ], salutation="Sehr geehrte Frau Cordes,")
    add(4, 13, "Nachbarantwort.eml", "2026-09-16", "nachbar", "bau", "Werkhof Nordwand und Lieferzufahrt", [
      "wir haben Ihre Skizze vom 11.09.2026 mit der 24 m langen Nordwand gesehen. Gegen den Werkhofbetrieb tagsüber haben wir grundsätzlich nichts einzuwenden. Wichtig ist uns, dass Regenwasser auf Ihrem Grundstück bleibt und unsere Lieferzufahrt nicht als Rangierfläche verwendet wird. Die in der Besprechung gezeigte Wand hatte keine Öffnungen.",
      "Die Aussage unseres Lagerleiters, der Bau sei für uns in Ordnung, bezog sich auf die Nutzung und nicht auf eine bestimmte Unterschreitung eines Grenzabstands. Wir möchten vor einer förmlichen Erklärung den endgültigen Lageplan und die Wandansicht erhalten. Eine Eintragung im Baulastenverzeichnis oder eine Übernahme von Abstandsflächen haben wir nicht zugesagt.",
      "Bitte richten Sie weitere Unterlagen an mich. Das Grundstück wird von unserer Gesellschaft gehalten; unser Pächter im hinteren Hofteil ist nicht befugt, für uns Grundstückserklärungen abzugeben. Für ein Gespräch stehen wir am 28.09.2026 zur Verfügung.",
    ], salutation="Sehr geehrte Frau Seidel,")
    add(4, 15, "Entwaesserung.eml", "2026-09-21", "wasser", "plan", "Rückhaltung bei verkürzter Halle", [
      "unser Entwässerungsansatz EW-02 vom 19.08.2026 enthält 456,00 m² Dachfläche aus Halle und Sozialtrakt sowie 864,00 m² befestigte Hoffläche. Die acht Pkw-Stellplätze mit zusammen 100,00 m² sind in den 864,00 m² nicht enthalten. Die Fahrradfläche von 18,00 m² ist unbefestigt mit wasserdurchlässigem Belag angesetzt und nicht in der angeschlossenen Fläche enthalten.",
      "Bei einer Hallentiefe von 14,70 m reduziert sich die Hallendachfläche um 7,20 m². Die angeschlossene Dachfläche wäre dann 448,80 m². Der Rückhalteraum wird dadurch nicht automatisch um denselben Prozentsatz kleiner; Zuflussansatz, Drosselung und Regenereignis sind gemeinsam neu zu rechnen. Eine neue Berechnung liegt noch nicht vor.",
      "Die Nordrinne kann nach Süden versetzt werden, sofern die konstruktive Dachausbildung dies zulässt. Wir benötigen dafür den ausgewählten Schnitt und den abgestimmten Dachplan. Eine Ableitung über das Grundstück Lüders ist in keiner Variante vorgesehen. Bitte kennzeichnen Sie im Lageplan Hof, Stellplätze und Fahrradfläche getrennt.",
    ], salutation="Sehr geehrte Frau Cordes,")
    add(4, 16, "Bauherrenstand.eml", "2026-09-23", "bau", "plan", "Entscheidung zur Nordwand noch offen", [
      "die Variante mit 14,70 m Hallentiefe ist nach Rücksprache mit dem Werkhofleiter betrieblich nutzbar. Wir haben sie aber noch nicht für die Einreichung ausgewählt. Die Variantenentscheidung soll am 25.09.2026 zwischen mir und der Betriebsleitung fallen. Bitte halten Sie bis dahin die bisherige Fassung und die verkürzte Variante getrennt.",
      "Der Kämmerer fragt, ob das Verfahren wegen der kommunalen Bauherrschaft als behördliche Zustimmung laufen könne. Eine schriftliche Auskunft dazu liegt uns nicht vor. Die vorhandene Portalquittung wurde intern bereits als Zustimmung bezeichnet; ich habe diese Formulierung nicht bestätigt.",
      "Die Nachreichungsfrist 30.09.2026 ist bekannt. Eine Verlängerung haben wir bislang weder beantragt noch erhalten. Ein Abweichungsantrag ist weiterhin nicht freigegeben. Für den heutigen Stand bitte keine Erklärung an den Nachbarn und keine neue Portalübermittlung veranlassen.",
    ], salutation="Sehr geehrte Frau Cordes,")


def write_csv(path, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        csv.writer(handle, delimiter=";").writerows(rows)


def plan_canvas(path, phase, title, planid, date, scale):
    c = canvas.Canvas(str(path), pagesize=landscape(A3), invariant=1)
    c.setAuthor(AUTHOR); c.setCreator(AUTHOR); c.setTitle(title)
    c.setSubject("Technische Bauzeichnung")
    c.setFont("CaseSerifB", 17); c.drawString(40, 800, title)
    c.setFont("CaseSerif", 11); c.drawString(40, 778, f"{CASES[phase]['code']} · {planid} · {date} · {scale}")
    c.setLineWidth(.7); c.rect(28, 28, 1135, 795)
    return c


def label(c, x, y, text, size=10, bold=False):
    c.setFillColor(colors.black); c.setFont("CaseSerifB" if bold else "CaseSerif", size)
    c.drawString(x, y, text)


def dimension(c, x1, y1, x2, y2, text):
    c.setStrokeColor(colors.HexColor("#46505b")); c.setLineWidth(.6)
    c.line(x1, y1, x2, y2)
    if abs(y1-y2) < .1:
        for x in (x1,x2): c.line(x-3,y1-5,x+3,y1+5)
        label(c,(x1+x2)/2-22,y1+7,text,10)
    else:
        for y in (y1,y2): c.line(x1-5,y-3,x1+5,y+3)
        c.saveState(); c.translate(x1-8,(y1+y2)/2-18); c.rotate(90); label(c,0,0,text,10); c.restoreState()


def celle_plans():
    path = inventory(4,3,"Lageplan_G01B.pdf","Lageplan G-01/B mit vermessener Nordgrenze")
    c = plan_canvas(path,4,"Werkhof Uhlenried Lageplan","G-01/B","27.08.2026","Schematisch vermasster Lagebezug")
    s=11; ox=110; oy=155
    c.setLineWidth(1.7); c.rect(ox,oy,60*s,48*s)
    c.setFillColor(colors.HexColor("#e2e8eb")); c.rect(ox+18*s,oy+30.3*s,24*s,15*s,fill=1)
    c.setFillColor(colors.HexColor("#edf0df")); c.rect(ox+30*s,oy+22.3*s,12*s,8*s,fill=1)
    c.setFillColor(colors.HexColor("#f0f0f0")); c.rect(ox+8*s,oy+4.3*s,48*s,18*s,fill=1)
    c.setStrokeColor(colors.HexColor("#a4a4a4"))
    for x in range(11,56,3): c.line(ox+x*s,oy+4.3*s,ox+x*s,oy+22.3*s)
    c.setStrokeColor(colors.black)
    for i in range(8): c.rect(ox+2*s,oy+(7+i*2.5)*s,5*s,2.5*s)
    for i in range(4): c.setLineWidth(4); c.line(ox+(19+i*6)*s,oy+30.3*s,ox+(22.5+i*6)*s,oy+30.3*s)
    c.setLineWidth(.7)
    label(c,ox+20*s,oy+38*s,"Fahrzeughalle 24,00 x 15,00 m",12,True)
    label(c,ox+20*s,oy+36*s,"Nordwand ohne Öffnungen",10)
    label(c,ox+31*s,oy+27*s,"Sozialtrakt",11,True); label(c,ox+31*s,oy+25*s,"12,00 x 8,00 m",10)
    label(c,ox+16*s,oy+17*s,"Hof / Zufahrt 48,00 x 18,00 m",12)
    label(c,ox+16*s,oy+14*s,"Schraffur endet an Gebäuden",10)
    label(c,ox+1*s,oy+30*s,"8 Pkw",10); label(c,ox+46*s,oy+4*s,"Fahrräder 18 m²",10)
    c.rect(ox+46*s,oy+1*s,6*s,3*s)
    label(c,ox+20*s,oy-35,"Uhlenrieder Weg / Zufahrt Süd",12)
    c.setLineWidth(3);c.line(ox+27*s,oy,ox+33*s,oy)
    label(c,ox+15*s,oy+49*s,"Nachbar Flurstück 118/7 · Lüders Gartenbedarf",11)
    dimension(c,ox,oy-65,ox+60*s,oy-65,"60,00 m")
    dimension(c,ox-35,oy,ox-35,oy+48*s,"48,00 m")
    dimension(c,ox+44*s,oy+45.3*s,ox+44*s,oy+48*s,"2,70 m")
    dimension(c,ox+18*s,oy+28.5*s,ox+42*s,oy+28.5*s,"24,00 m")
    label(c,825,680,"N",16,True);c.line(832,600,832,660);c.line(832,660,824,643);c.line(832,660,840,643)
    notes=["Grundstück 60,00 x 48,00 m = 2.880,00 m²","Flur 7, Flurstück 118/6","Hallensüdwand y = 30,30 m","Hallennordwand y = 45,30 m","Nordgrenze y = 48,00 m","Hofansatz ohne Pkw-Stellplätze","Höhenbezug: FFB Halle 42,10 m","Vermessung V-26-118, 17.08.2026","Stand: zur Einreichung","gez. Rieke Cordes"]
    for i,line in enumerate(notes):label(c,805,540-i*25,line,10)
    label(c,45,55,"Cordes Bauatelier · Bezug CE-WU26 · Darstellung der beantragten Lage, keine Ausführungszeichnung",10)
    c.save()
    path=inventory(4,4,"Bauzeichnung_G02B.pdf","Grundriss und Schnitt G-02/B")
    c=plan_canvas(path,4,"Werkhof Grundriss und Nord-Süd-Schnitt","G-02/B","27.08.2026","Grundriss schematisch vermasst")
    ox=80;oy=420;s=21
    c.setLineWidth(4);c.rect(ox,oy,24*s,15*s)
    c.setLineWidth(1)
    for x in (0,6,12,18,24):
        c.setDash(4,3);c.line(ox+x*s,oy-25,ox+x*s,oy+15*s+18);c.setDash()
        label(c,ox+x*s-3,oy+15*s+25,str(int(x/6)+1),10)
    for i in range(4):
        tx=ox+(1+i*6)*s;c.setStrokeColor(colors.white);c.setLineWidth(6);c.line(tx,oy,tx+3.5*s,oy)
        c.setStrokeColor(colors.black);c.setLineWidth(1);c.line(tx,oy+7,tx+3.5*s,oy+7)
        label(c,tx,oy-19,f"Tor {i+1} 3,50 m",9)
    label(c,ox+120,oy+180,"Fahrzeughalle",16,True);label(c,ox+110,oy+155,"Außenkontur 360,00 m²",11)
    c.rect(710,420,12*25,8*25)
    c.line(860,420,860,620);c.line(710,520,1010,520);c.line(935,420,935,520)
    for x,y,t in [(725,570,"Aufenthalt"),(875,570,"Büro"),(725,465,"Umkleiden"),(870,465,"WC"),(945,465,"Technik")]:label(c,x,y,t,10)
    label(c,710,644,"Sozialtrakt 12,00 x 8,00 m",12,True)
    dimension(c,ox,oy-50,ox+24*s,oy-50,"24,00 m")
    dimension(c,ox-30,oy,ox-30,oy+15*s,"15,00 m")
    # Der Schnitt zeigt die tatsächlichen Höhen und den strittigen Abstand, nicht nur einen Textverweis.
    x=130;y=170;sc=26
    c.setFillColor(colors.HexColor("#e7ecef"));c.setStrokeColor(colors.black);c.setLineWidth(1.5)
    pts=[(x,y),(x,y+4.8*sc),(x+7.5*sc,y+6.2*sc),(x+15*sc,y+4.8*sc),(x+15*sc,y)]
    p=c.beginPath();p.moveTo(*pts[0]);[p.lineTo(*q) for q in pts[1:]];p.close();c.drawPath(p,fill=1)
    c.line(x-35,y-3,x+18*sc,y-3)
    c.setDash(5,3);c.line(x+17.7*sc,y-25,x+17.7*sc,y+6.5*sc);c.setDash()
    dimension(c,x+15*sc,y-28,x+17.7*sc,y-28,"2,70 m")
    label(c,x-60,y+4.8*sc,"+4,80",10);label(c,x+7.5*sc-15,y+6.2*sc+12,"+6,20",10)
    label(c,x+17.7*sc+12,y+75,"Nordgrenze",10)
    label(c,740,300,"Schnitt: Süd links / Nord rechts",12,True)
    for i,t in enumerate(["FFB Halle = 42,10 m", "Gelände Nordwest = 41,96 m", "Gelände Nordost = 42,02 m", "Traufe relativ FFB = 4,80 m", "Brandschutzbeitrag noch auf Stand A", "gez. Rieke Cordes"]):label(c,740,273-i*25,t,11)
    label(c,45,55,"G-02/B · Planungsstand zum Bauantrag · Nordwand ohne Öffnungen",10);c.save()
    path=inventory(4,14,"Nordvariante_G03.png","Planbild G-03 mit unverändertem und verkürztem Hallenkörper")
    image=Image.new("RGB",(1800,1200),"white");d=ImageDraw.Draw(image)
    d.text((65,40),"Werkhof Uhlenried · Nordvariante G-03 · 18.09.2026",font=screen_font(34,True),fill="#17242d")
    d.text((65,92),"CE-WU26 · Cordes Bauatelier · zur Entscheidung · keine Einreichung",font=screen_font(22),fill="black")
    # Beide Konturen sind in demselben Bezugssystem sichtbar; der Detailausschnitt vergrößert die 0,30 m.
    d.rectangle((120,260,1080,860),outline="#263b4a",width=6)
    d.line((120,272,1080,272),fill="#ae3d43",width=6)
    d.line((65,152,1170,152),fill="black",width=3)
    d.text((500,165),"Nordgrenze y = 48,00 m",font=screen_font(24),fill="black")
    for x in (120,360,600,840,1080):d.line((x,250,x,890),fill="#bcc3c8",width=2)
    d.text((300,530),"Halle 24,00 m breit",font=screen_font(34,True),fill="#263b4a")
    d.text((280,585),"Bestand der Planung: 15,00 m tief",font=screen_font(24),fill="#263b4a")
    d.text((280,625),"Variante: 14,70 m tief",font=screen_font(24),fill="#ae3d43")
    d.line((1200,152,1200,260),fill="#263b4a",width=3);d.text((1240,195),"2,70 m",font=screen_font(28),fill="#263b4a")
    d.line((1390,152,1390,272),fill="#ae3d43",width=3);d.text((1430,226),"3,00 m",font=screen_font(28),fill="#ae3d43")
    d.rectangle((1250,400,1700,810),outline="#777777",width=2)
    d.text((1270,420),"Nordwanddetail",font=screen_font(27,True),fill="black")
    d.line((1280,510,1660,510),fill="#263b4a",width=7);d.line((1280,690,1660,690),fill="#ae3d43",width=7)
    d.line((1640,510,1640,690),fill="black",width=3);d.text((1285,570),"0,30 m nach Süden",font=screen_font(24),fill="black")
    d.text((120,925),"Südwand bleibt y = 30,30 m. Neue Nordwand y = 45,00 m.",font=screen_font(26),fill="black")
    d.text((120,970),"Hallenfläche 352,80 m² statt 360,00 m². Maßangaben gelten vor Bildskalierung.",font=screen_font(24),fill="black")
    d.text((120,1015),"Tragwerk, Dachentwässerung und Brandschutz noch nicht auf Variante bestätigt.",font=screen_font(24),fill="black")
    d.text((120,1090),"gez. Rieke Cordes · Darstellungsmaßstab variabel, vollständig vermasste Projektstudie",font=screen_font(22),fill="black")
    info=PngImagePlugin.PngInfo();info.add_text("Author",AUTHOR);info.add_text("Title","CE-WU26 G-03 Nordvariante")
    image.save(path,pnginfo=info)


def celle_misc():
    inventory(4,6,"Flaechen.xlsx","Rechnende Flächenaufstellung FL-01 mit zwei Hallentiefen")
    p=inventory(4,10,"Portalquittung.txt","Technischer Eingangsbeleg vom 02.09.2026")
    p.write_text("Projektpost Bauverfahren Celle\nTransaktion CE-20260902-091842\nEmpfänger: Bauaufsicht Celle\nAbsender: Rieke Cordes, Cordes Bauatelier\nBauherrschaft: Stadt Celle, Gebäudebetrieb Uhlenried\nZeitpunkt: 02.09.2026 09:18:42 +02:00\nVorgang: Antrag übermittelt\n\nDateisatz\n1 Antrag_CE-WU26.pdf, 184 kB\n2 G-01_B_Lageplan.pdf, 612 kB\n3 G-02_B_Bauzeichnung.pdf, 940 kB\n4 BB-01_Baubeschreibung.pdf, 221 kB\n5 FL-01_Flaechen.pdf, 97 kB\n6 BS-01_Kammann.pdf, 176 kB\n7 TW-01_Hohenfeld.pdf, 164 kB\n\nTechnische Übertragung abgeschlossen. Die fachliche und rechtliche Prüfung steht aus.\nEmpfangsreferenz: CE-BA-2026-184\nAutomatisch erzeugter Eingangsbeleg. Keine Unterschrift.\n",encoding="utf-8")
    p=inventory(4,17,"Planindex.csv","Büro-Planindex mit Versand- und Entscheidungsstand")
    write_csv(p,[["Projekt","Plan","Revision","Datum","Inhalt","Verwendung","Versand","Verfasser"],
      ["CE-WU26","G-01","A","2026-05-20","Entwurf Lage 3,00 m Annahme","Entwurf bestätigt","2026-05-26 Bauherr","Rieke Cordes"],
      ["CE-WU26","G-02","A","2026-05-20","Entwurf Halle 24 x 15 m","Entwurf bestätigt","2026-05-26 Fachplaner","Rieke Cordes"],
      ["CE-WU26","G-01","B","2026-08-27","Vermessene Lage Nord 2,70 m","eingereicht","2026-09-02 Portal","Rieke Cordes"],
      ["CE-WU26","G-02","B","2026-08-27","Schnitt mit Geländehöhen","eingereicht","2026-09-02 Portal","Rieke Cordes"],
      ["CE-WU26","G-03","0","2026-09-18","Nordwand 0,30 m eingerückt","zur Entscheidung","2026-09-18 Bauherr","Rieke Cordes"],
      ["CE-WU26","BS-01","0","2026-08-25","Brandschutz auf G-02/A","Fachbeitrag","2026-09-02 Portal","Nele Kammann"],
      ["CE-WU26","EW-02","0","2026-08-19","Dach 456 m², Hof 864 m²","Fachplanung","2026-08-20 Objektplanung","Ole Beeken"],
    ])


def define_hameln():
    add(5,1,"Planungsauftrag.pdf","2026-03-06","bau","plan","Abruf Ausführungsplanung Schulumbau Brückenanger",[
      "Auf Grundlage unseres Planervertrags vom 15.10.2025 rufen wir die Gebäude-Leistungsphase 5 für den Umbau des Ostflügels der Schule Brückenanger ab. Das Gebäude steht im Eigentum der Schulbau Brückenanger gGmbH. Der Auftrag betrifft den eingeschossigen Unterrichtsflügel mit vier Unterrichtsräumen, gemeinsamem Flur und zwei Gruppenräumen. Die Genehmigungsunterlagen vom 12.02.2026 sind Ausgangspunkt der Bearbeitung.",
      ("h","1 Geschuldete Unterlagen"),
      "Nordfeld Architektur erstellt die Ausführungsgrundrisse, Schnitte, Tür- und Öffnungslisten sowie die für die Ausführung notwendigen Anschlussdetails. Einzubeziehen sind die Beiträge von Rautenberg Tragwerksbüro, Behrens Gebäudetechnik und Röwe Brandschutzkonzepte. Die Fachplaner sind jeweils unmittelbar durch uns beauftragt. Die Koordination umfasst insbesondere den Flur F-01, den Anschluss der neuen Lüftung und den Austausch der Fenster im Ostflügel.",
      "Erforderliche Montagepläne für die von Nordfeld geplanten baukonstruktiven Einbauten werden auf Übereinstimmung mit der Ausführungsplanung geprüft. Die eigenständige Bemessung von TGA-Komponenten, Tragwerk und Befestigungen, soweit fachplanerisch zu führen, wird dadurch nicht übertragen. Die Werkstattplanung der Metallbaufirma muss auf den bezeichneten Ausführungsstand zurückgeführt werden.",
      ("h","2 Planungsziele und Entscheidungsrechte"),
      "Im Flur F-01 ist eine durchgehend lichte Höhe von mindestens 2,75 m nach der bestätigten Nutzungsvorgabe einzuhalten. Die abgehängte Decke wird im Entwurf mit Unterkante 2,80 m geführt. Der Flur muss für Wartungsarbeiten zugänglich bleiben; Leitungen dürfen die erforderlichen Türdurchgänge nicht einschränken. Diese Werte sind Projektvorgaben und keine Aussage über allgemeine gesetzliche Mindestmaße.",
      "Die Bauherrschaft entscheidet über sichtbare Materialien, Budgetänderungen und Änderungen der Nutzung. Technische Bestätigungen erteilen die jeweils beauftragten Fachplaner in ihrer Zuständigkeit. Eine Entscheidung von Janne Vollmer über eine bevorzugte Leitungsroute ersetzt keinen Nachweis zur Dimensionierung, Befestigung oder Abschottung. Die öffentlich-rechtliche Bauleiterbestellung erfolgt gesondert vor Beginn der Bauausführung.",
      ("h","3 Termine und Vergütung"),
      "Für den Abruf wird ein Honorar von 47.500,00 EUR netto vereinbart. Der koordinierte Ausbauplansatz soll am 09.10.2026 an die Vergabevorbereitung übergeben werden. Für die Fertigung der Flurverglasung ist nach gegenwärtiger Auskunft ein Vorlauf von 35 Kalendertagen nach bestätigtem Montageplan vorgesehen. Der Ausbau soll am 11.01.2027 beginnen; technische Voraussetzungen und Vergabe sind noch nicht abgeschlossen.",
      ("h","4 Revision und Kommunikation"),
      "Planänderungen sind mit Anlass, Datum, betroffenem Bauteil und ersetzter Revision zu dokumentieren. Nordfeld darf Koordinationsanfragen stellen, aber keine kostenpflichtigen Unternehmensänderungen in unserem Namen beauftragen. Ein Planversand zur Ausführung bedarf der dokumentierten fachlichen Prüfung und unserer projektbezogenen Freigabe. Die Parteien bestätigen den Abruf in Textform: Janne Vollmer und Lea Wernicke, jeweils am 06.03.2026.",
    ])
    add(5,2,"Genehmigungsbescheid.pdf","2026-02-27","amt","bau","Baugenehmigung HM-BA-2026-073",[
      "Auf Ihren Antrag vom 12.02.2026 wird der Umbau des Ostflügels der Schule Brückenanger auf dem Grundstück Brückenanger 12, Flur 4, Flurstück 72/3, im nachfolgend bestimmten Umfang genehmigt. Gegenstand sind die Umgestaltung der Unterrichtsräume, der Austausch der Fenster und die in den genehmigten Unterlagen dargestellte technische Erneuerung.",
      ("h","1 Maßgebliche Unterlagen"),
      "Der genehmigte Gegenstand ergibt sich aus dem Grundriss A-100/G und Schnitt A-210/G, jeweils vom 12.02.2026, der Baubeschreibung vom selben Tag und dem Brandschutzbeitrag BS-02 vom 09.02.2026. Die in der Baubeschreibung zugrunde gelegte Nutzung als Unterrichtsflügel mit maximal 120 gleichzeitig anwesenden Personen ist Bestandteil des Antragsgegenstands. Eine Veranstaltungsnutzung wird nicht genehmigt.",
      ("h","2 Anforderungen an die weitere Bearbeitung"),
      "Die im Brandschutzbeitrag bezeichneten Rettungswege und Abschlüsse sind entsprechend den dort beschriebenen Anforderungen herzustellen. Die im Schnitt angegebene Flurhöhe darf durch nachträgliche Leitungsführung nicht ohne vorherige Klärung des geänderten Gegenstands unterschritten werden. Die Genehmigung bestätigt keine noch nicht vorgelegte Montageplanung einzelner Unternehmen.",
      "Bautechnische Nachweise und erforderliche Prüfungen sind durch die verantwortlichen Personen nach den einschlägigen Bestimmungen zu führen. Die Darstellung einer Leitungsöffnung im Architekturgrundriss ersetzt nicht deren statischen Nachweis. Änderungen an tragenden Bauteilen sind nicht Gegenstand einer allgemeinen Freigabe durch diesen Bescheid.",
      ("h","3 Hinweise zum Umfang"),
      "Diese Entscheidung umfasst ausschließlich den beschriebenen Umbau. Sie ersetzt keine privatrechtlichen Erklärungen Dritter und keine außerhalb ihres Prüfgegenstands erforderlichen fachlichen Nachweise. Der Beginn der Arbeiten und die verantwortlichen Personen sind nach den maßgeblichen Verfahrensvorgaben anzuzeigen. Der Bescheid ist mit den bezeichneten Unterlagen zusammen aufzubewahren.",
      "Für Rückfragen zum Inhalt verwenden Sie bitte das Aktenzeichen HM-BA-2026-073. Der Bescheid wurde am 27.02.2026 elektronisch an die bevollmächtigte Entwurfsverfasserin übermittelt. Die Kostenentscheidung erfolgt gesondert.",
    ])
    add(5,3,"Entwurfsuebergabe.docx","2026-03-03","plan","bau","Übergabe Entwurf und Ausstattungsentscheidungen",[
      "Wir übergeben den bestätigten Entwurfsstand des Ostflügels als Grundlage der Ausführungsplanung. Der Flur F-01 verläuft zwischen den Achsen 1 bis 5 und den Unterrichtsräumen U-01 bis U-04. Der Bestand wurde mit einem Achsraster von 6,00 m aufgenommen; der Flur hat 2,40 m lichte Breite.",
      ("h","1 Bestätigte Nutzung"),
      "Die vier Unterrichtsräume werden mit jeweils bis zu 25 Lernenden und einer Lehrkraft belegt. Die Gruppenräume G-01 und G-02 werden nicht gleichzeitig mit voller Unterrichtsbelegung zusätzlich genutzt. Die durch die Bauherrschaft bestätigte Gesamtbelegung beträgt höchstens 120 Personen. Die Flurhöhe von mindestens 2,75 m wurde aus dem Nutzungskonzept übernommen; die Entwurfsdecke liegt bei 2,80 m.",
      ("h","2 Materialien und Anschlüsse"),
      "Im Flur ist eine demontierbare Unterdecke vorgesehen. Die Fenster erhalten innen eine Holzwerkstoffbank; außen ist eine Metallfensterbank mit seitlichen Abschlüssen vorgesehen. Die Leibungsdämmung wird nach dem bauphysikalischen Detail abgestimmt. Die im Entwurf gezeichneten 30 mm sind ein geometrischer Platzansatz, kein bereits bestätigter Systemnachweis.",
      "Die Flurverglasung V-01 trennt den Eingangsbereich vom Unterrichtsflur. Die lichte Durchgangsbreite am Türfeld T-01 beträgt nach der Nutzungsvorgabe 1,20 m. Die Rohbauöffnung wird in A-101 mit 1,36 m vorgesehen. Das endgültige Profil-/Zargenmaß ist mit dem Montageplan abzugleichen; die Rohbauöffnung ist nicht mit der nutzbaren Breite gleichzusetzen.",
      ("h","3 Noch zu koordinierende Beiträge"),
      "Die Lüftungsplanung ist mit dem Unterzug in Achse 3 abzugleichen. Der Tragwerksplan weist die Unterkante auf 3,15 m über Fertigfußboden aus. Im Vorentwurf der TGA war eine Kanalhülle von 0,28 m angesetzt. Eine neue Fachauslegung liegt zum Zeitpunkt dieser Übergabe noch nicht vor. Die spätere Ausführungsplanung soll die vollständige Einbauhülle einschließlich Dämmung, Aufhängung und Deckenunterkonstruktion zeigen.",
      "Die Übergabe ersetzt keine Ausführungsfreigabe. Janne Vollmer hat am 03.03.2026 die beschriebenen Nutzungs- und Materialentscheidungen bestätigt; Fachnachweise und Unternehmensplanung bleiben im weiteren Ablauf zu bearbeiten.",
    ])
    add(5,10,"Koordinationsprotokoll.docx","2026-09-15","plan","bau","Koordinationsbesprechung Ostflügel vom 15.09.2026",[
      "Teilgenommen haben Lea Wernicke für Nordfeld Architektur, Tammo Behrens für die Lüftungsplanung, Iven Rautenberg für das Tragwerk und Janne Vollmer für die Bauherrschaft. Besprochen wurden die Planstände A-101/C, T-201/B und L-301/D. Die nachfolgenden Angaben geben den Gesprächsstand wieder; sie enthalten keine gemeinsame technische Freigabe.",
      ("h","1 Flur F-01 und Unterzug Achse 3"),
      "Die aktuelle TGA benötigt am Hauptkanal einen freien Querschnitt von 600 mm mal 280 mm. Behrens setzt umlaufend 40 mm Dämmung an. Die äußere Kanalhöhe beträgt damit 360 mm. Die im Architekturentwurf übernommene Hülle von 280 mm entspricht nicht mehr diesem Fachstand. Rautenberg bestätigt für den vorhandenen Unterzug eine Unterkante von 3,15 m über Fertigfußboden.",
      "Wernicke zeigt zwei räumliche Wege: Führung unter dem Unterzug oder seitliches Umfahren im Deckenfeld der Achse 2 bis 3. Für die seitliche Route muss Behrens Druckverlust, Wartung und Anschluss an die Klassenräume prüfen. Rautenberg lehnt eine ungeprüfte Durchdringung des Unterzugs ab. Eine neue Trägeröffnung wurde nicht beauftragt.",
      ("h","2 Flurverglasung"),
      "Der Montageplan M-17/0 von Lenz Metallbau verwendet A-101/B als Referenz. Im Plan ist für das Türfeld T-01 eine lichte Breite von 1,16 m eingetragen. Die Bauherrschaft hält an 1,20 m fest. Die Rohbauöffnung von 1,36 m wird nicht durch eine reine Beschriftungsänderung größer. Lenz wird die Profilkombination und die tatsächliche Durchgangsbreite erläutern.",
      ("h","3 Termine und Unterlagen"),
      "Als interner Antworttermin für die Fachbeiträge wurde der 24.09.2026 vereinbart. Das Ausbaupaket soll am 09.10.2026 an die Vergabevorbereitung gehen. Die Angabe von 35 Kalendertagen Fertigungsvorlauf stammt aus der Mail von Lenz vom 10.09.2026 und beginnt erst nach bestätigtem Montageplan. Eine Bestellung oder Ausführungsfreigabe wurde in der Sitzung nicht erklärt.",
      "Korrekturen dieser Niederschrift sind bis zum 21.09.2026 mitzuteilen. Bis zum heutigen Versand liegt keine Bestätigung einer Kanalroute und keine korrigierte Türzeichnung vor. Versand durch Lea Wernicke am 15.09.2026 an die genannten Teilnehmer.",
    ])
    add(5,12,"TGA_Antwort.eml","2026-09-22","tga","plan","Seitliche Kanalroute F-01",[
      "die seitliche Route im Deckenfeld zwischen Achse 2 und 3 ist hinsichtlich des freien Querschnitts mit 600 x 280 mm weiter bearbeitbar. Wir benötigen zwei zusätzliche Bögen und eine zugängliche Revisionsstelle vor dem Abzweig U-03. Die äußere Hülle bleibt mit 680 x 360 mm unverändert. Eine Reduzierung auf 600 x 200 mm frei bestätigen wir nicht.",
      "Unser Blatt L-301/D enthält noch die direkte Route. Die seitliche Variante wird als Revision E erst nach dem Abgleich mit Leuchten und Revisionsöffnungen ausgegeben. Die Befestigung an der Bestandsdecke ist nicht Gegenstand dieser Mail; hierfür benötigen wir den bestätigten Befestigungsgrund und die Lastangaben des gewählten Systems.",
      "Bitte halten Sie den Zugang zur Brandschutzklappe an Wand W-04 frei. Der dafür benötigte Wartungsraum ist im Fachblatt dargestellt. Die vorliegende Aussage betrifft keine brandschutztechnische Freigabe der gesamten Unterdecke und keine Ausführung vor Abschluss der Koordination.",
    ],salutation="Sehr geehrte Frau Wernicke,")
    add(5,13,"Metallbau_Antwort.eml","2026-09-23","metall","plan","M-17 lichte Breite Tür T-01",[
      "unser Montageplan M-17/0 vom 11.09.2026 beruht auf dem am 04.09.2026 erhaltenen Grundriss A-101/B. Mit der dargestellten Profilkombination verbleiben aus der Rohbauöffnung 1,36 m rechnerisch 1,16 m lichte Durchgangsbreite. Die 1,20 m aus Ihrer Mail vom 16.09.2026 werden damit nicht erreicht.",
      "Wir können eine schmalere Profilkombination untersuchen. Dazu benötigen wir die abschließend geforderte Funktion des Türfelds und die Anschlussausbildung an die flankierende Wand. Alternativ wäre eine größere Rohbauöffnung zu prüfen. Eine solche Änderung haben wir weder kalkuliert noch technisch freigegeben. Bitte die vorliegende Zeichnung nicht zur Fertigung verwenden.",
      "Der Fertigungsvorlauf von 35 Kalendertagen beginnt mit der bestätigten Montagezeichnung und der Beauftragung. Die Prüfung durch die Objektplanung auf Übereinstimmung mit deren Planung ersetzt nicht unsere Fertigungsplanung. Eine neue Revision wird nach Klärung der Maße erstellt.",
    ],salutation="Sehr geehrte Frau Wernicke,")
    add(5,14,"Bauherrenentscheidung.eml","2026-09-24","bau","plan","Flurhöhe und seitliche Route",[
      "wir bevorzugen die seitliche Leitungsführung, sofern die Fachplanung deren Funktion bestätigt und die Revisionsöffnungen zugänglich bleiben. Eine Absenkung der Flurdecke unter die vereinbarte lichte Höhe von 2,75 m geben wir nicht frei. Die Ausführung soll weiterhin ruhig und durchgehend wirken; lokale Abkofferungen sind uns vor einer Entscheidung zeichnerisch zu zeigen.",
      "Am Türfeld T-01 halten wir an der nutzbaren Breite 1,20 m fest. Eine Bestellung der derzeitigen Profilkombination ist nicht freigegeben. Bitte unterscheiden Sie in der Planliste unsere gestalterische Präferenz von der noch offenen technischen Bestätigung und vom Versand zur Ausführung.",
      "Der Ausbauplantermin 09.10.2026 bleibt unser Ziel. Für zusätzliche Kosten der seitlichen Route liegt uns noch kein Betrag vor. Wir haben weder einen Nachtrag beauftragt noch eine Kostenneutralität bestätigt. Die Montagezeichnung M-17/0 soll bis zur Überarbeitung nur als vorliegender Unternehmerstand im Archiv bleiben.",
    ],salutation="Sehr geehrte Frau Wernicke,")
    add(5,17,"Brandschutz_Flur.pdf","2026-09-18","brand","plan","Flurdecke und Wartungszugang W-04",[
      "Unser Schreiben bezieht sich auf den Brandschutzbeitrag BS-02 und die Koordinationsskizze K-07 vom 15.09.2026. Die geänderte Leitungsführung ist noch nicht abschließend im Gesamtzusammenhang bewertet. Insbesondere liegt uns kein revidierter TGA-Plan mit den endgültigen Revisionsöffnungen vor.",
      ("h","1 Wand W-04"),
      "Die Durchführung an W-04 bleibt an der im Fachplan bezeichneten Stelle. Die Brandschutzklappe muss für Inspektion und Instandhaltung erreichbar sein. Eine durchgehende Bekleidung ohne zugeordnete Revisionsöffnung entspricht nicht dem vorgesehenen Wartungszugang. Die genaue Öffnungsgröße ist mit dem ausgewählten System und der TGA-Planung abzustimmen.",
      ("h","2 Abgehängte Decke"),
      "Die im Entwurf dargestellte demontierbare Decke dient hier nicht als pauschaler Ersatz für die erforderlichen Abschottungen der durchdrungenen Bauteile. Die Leitungsroute darf keine offenen Durchführungen schaffen. Die Anforderungen an den jeweiligen Abschluss sind positions- und bauteilbezogen in der Ausführungsplanung zu übernehmen.",
      "Wir benötigen für die weitere Prüfung die Lage der zusätzlichen Revisionsstelle, den Abstand zu Leuchten und das Anschlussdetail an W-04. Eine Zustimmung zur seitlichen Route in der TGA-Mail beantwortet diese Punkte nicht vollständig. Dieses Schreiben ist keine Freigabe des Montageplans M-17 oder der gesamten Ausführungsplanung.",
    ])


def hameln_plans():
    p=inventory(5,4,"Grundriss_A101C.pdf","Ausführungsgrundriss A-101/C mit Raum- und Türbezug")
    c=plan_canvas(p,5,"Schule Brückenanger Ausführungsgrundriss","A-101/C","14.09.2026","Vermaßte Koordinationsdarstellung")
    ox=100;oy=280;s=35
    c.setLineWidth(3);c.rect(ox,oy,24*s,8.4*s);c.line(ox,oy+2.4*s,ox+24*s,oy+2.4*s)
    raw_bottom=oy+(2.4-1.36)/2*s;raw_top=raw_bottom+1.36*s
    hinge=raw_bottom+.08*s;clear=1.20*s
    c.setStrokeColor(colors.white);c.setLineWidth(6);c.line(ox,raw_bottom,ox,raw_top)
    c.setStrokeColor(colors.black);c.setLineWidth(3)
    c.line(ox,raw_bottom,ox,hinge);c.line(ox,hinge+clear,ox,raw_top)
    c.setLineWidth(1);c.line(ox,hinge,ox+clear,hinge)
    c.arc(ox-clear,hinge-clear,ox+clear,hinge+clear,startAng=0,extent=90)
    label(c,ox+8,oy+7,"T-01",10,True)
    for i in range(1,4):c.line(ox+i*6*s,oy+2.4*s,ox+i*6*s,oy+8.4*s)
    for i in range(4):
        x=ox+i*6*s
        label(c,x+38,oy+5.5*s,f"U-0{i+1}",15,True);label(c,x+28,oy+4.8*s,"Unterricht",11)
        c.setStrokeColor(colors.white);c.setLineWidth(5);c.line(x+4*s,oy+2.4*s,x+5.2*s,oy+2.4*s)
        c.setStrokeColor(colors.black);c.setLineWidth(1);c.line(x+4*s,oy+2.4*s,x+4*s,oy+3.6*s)
        c.arc(x+4*s,oy+2.4*s-1.2*s,x+6.4*s,oy+3.6*s,startAng=90,extent=90)
        label(c,x+4*s,oy+3.9*s,f"T-0{i+2}",10)
    label(c,ox+80,oy+35,"F-01 Flur · lichte Breite 2,40 m · Decke UK +2,80 m",13,True)
    c.setDash(5,3);c.line(ox+12*s,oy-45,ox+12*s,oy+8.4*s+65);c.setDash()
    c.setStrokeColor(colors.HexColor("#a63f46"));c.setLineWidth(5);c.line(ox+11.85*s,oy,ox+11.85*s,oy+8.4*s)
    c.line(ox+12.15*s,oy,ox+12.15*s,oy+8.4*s);c.setStrokeColor(colors.black)
    label(c,ox+12*s+20,oy+8.4*s+35,"Unterzug Achse 3, UK +3,15 m",11)
    for i in range(5):label(c,ox+i*6*s-3,oy+8.4*s+65,str(i+1),12,True)
    dimension(c,ox,oy-65,ox+24*s,oy-65,"24,00 m")
    dimension(c,ox-38,oy,ox-38,oy+2.4*s,"2,40 m")
    dimension(c,ox-38,oy+2.4*s,ox-38,oy+8.4*s,"6,00 m")
    label(c,95,150,"Türfeld T-01 am Eingang West: Rohbau 1,36 m, gefordert lichte Breite 1,20 m.",12)
    label(c,95,120,"TGA-Route und Deckenraster siehe L-301/D und K-07; Planstand zur Koordination.",11)
    label(c,95,90,"Bezugshöhe: FFB EG = 0,00 m. Nordfeld Architektur · gez. Lea Wernicke",11)
    c.save()
    p=inventory(5,6,"Tragwerksplan_T201B.pdf","Tragwerksplan T-201/B mit Unterzug und Bohrvorbehalt")
    c=plan_canvas(p,5,"Bestandsunterzug Achse 3","T-201/B","08.09.2026","Schnitt vermasst, nicht zur Maßentnahme")
    c.setFillColor(colors.HexColor("#e0e0e0"));c.rect(100,460,830,100,fill=1)
    c.rect(420,280,160,180,fill=1)
    label(c,135,505,"Bestandsdecke Stahlbeton",14,True)
    label(c,440,365,"UZ 3",14,True)
    dimension(c,980,280,980,460,"0,45 m")
    dimension(c,420,242,580,242,"0,40 m")
    dimension(c,75,460,75,560,"0,25 m Decke")
    label(c,950,470,"UK Decke +3,60 m",12);label(c,620,288,"UK Unterzug +3,15 m",12)
    label(c,100,205,"Unterzugbreite 0,40 m · Lage in Achse 3 · FFB EG = 0,00 m",12)
    label(c,100,165,"Keine Bohrung oder Aussparung im Unterzug ohne gesonderten statischen Nachweis.",12,True)
    label(c,100,130,"Befestigungslasten der TGA sind mit Lage und Lastangabe vorzulegen.",12)
    label(c,100,95,"Rautenberg Tragwerksbüro · gez. Iven Rautenberg · Bestand aufgenommen 02.09.2026",11)
    c.save()
    p=inventory(5,7,"TGA_Plan_L301D.pdf","TGA-Grundriss L-301/D mit Kanalhülle und Wartungszone")
    c=plan_canvas(p,5,"Lüftung Flur F-01","L-301/D","12.09.2026","Grundriss mit Querschnitt")
    c.setLineWidth(2);c.rect(90,480,880,180)
    c.setFillColor(colors.HexColor("#dcebf2"));c.rect(110,535,840,51,fill=1)
    c.setStrokeColor(colors.HexColor("#b64940"));c.setLineWidth(5);c.line(530,450,530,695)
    label(c,550,692,"Achse 3 / Unterzug",12)
    c.setStrokeColor(colors.black);c.setLineWidth(1)
    for x in (250,450,650,850):c.rect(x,586,24,74)
    label(c,120,617,"Anschlüsse Unterrichtsräume",12)
    label(c,130,515,"Direkte Route unter Unterzug",12,True)
    c.rect(990,480,120,180);label(c,1000,640,"W-04",12,True);label(c,1000,605,"BSK",12)
    label(c,965,450,"Wartungszone",11)
    c.setFillColor(colors.HexColor("#dcebf2"));c.rect(160,190,340,180,fill=1)
    c.setFillColor(colors.white);c.rect(180,210,300,140,fill=1)
    label(c,220,275,"frei 600 x 280 mm",12,True)
    dimension(c,160,165,500,165,"außen 680 mm")
    dimension(c,535,190,535,370,"außen 360 mm")
    for i,t in enumerate(["Dämmung umlaufend 40 mm", "Montageabstand oben 50 mm", "Deckenunterkonstruktion 60 mm", "Keine bestätigte Querschnittsreduzierung", "Revision D enthält noch keine seitliche Route", "gez. Tammo Behrens"]):label(c,650,365-i*35,t,12)
    label(c,90,85,"Behrens Gebäudetechnik · Bezug A-101/C und T-201/B · zur Fachkoordination",11);c.save()
    p=inventory(5,11,"Montageplan_M17.pdf","Montagezeichnung M-17/0 mit abweichender lichter Türbreite")
    c=plan_canvas(p,5,"Flurverglasung Türfeld T-01","M-17/0","11.09.2026","Ansicht, Maße in mm")
    x=150;y=170;w=544;h=480
    c.setFillColor(colors.HexColor("#d8e8ed"));c.rect(x,y,w,h,fill=1)
    c.setFillColor(colors.HexColor("#777777"));c.rect(x,y,40,h,fill=1);c.rect(x+w-40,y,40,h,fill=1);c.rect(x,y+h-40,w,40,fill=1)
    c.setStrokeColor(colors.black);c.setLineWidth(2);c.line(x+40,y,x+w-40,y+h-40)
    dimension(c,x,y-55,x+w,y-55,"Rohbau 1360")
    dimension(c,x+40,y+100,x+w-40,y+100,"licht 1160")
    dimension(c,x+w+45,y,x+w+45,y+h,"Rohbau 2400")
    for i,t in enumerate(["Grundlage A-101/B vom 02.09.2026", "Profilansatz seitlich je 100 mm", "Lichte Höhe nach Bodenanschluss prüfen", "Türanschlag gemäß Ansicht", "Status: zur Prüfung, nicht zur Fertigung", "Maße vor Fertigung am Bau nehmen", "gez. Fenja Lenz"]):label(c,800,610-i*44,t,11)
    label(c,80,60,"Lenz Metallbau GmbH · keine statische Bemessung mit dieser Zeichnung verbunden",11);c.save()
    p=inventory(5,16,"Fensterdetail_D12.pdf","Fensterbrüstungsdetail D-12 mit Schichten und Anschlussmaßen")
    c=plan_canvas(p,5,"Fensterbrüstung Ostflügel","D-12/B","16.09.2026","Detail vermasst, schematischer Schnitt")
    c.setFillColor(colors.HexColor("#d5d2cc"));c.rect(400,180,150,340,fill=1)
    c.setFillColor(colors.HexColor("#e5ead4"));c.rect(550,180,100,340,fill=1)
    c.setFillColor(colors.HexColor("#d4e6ed"));c.rect(475,520,55,160,fill=1)
    c.setFillColor(colors.HexColor("#70777c"));c.rect(455,490,95,38,fill=1)
    c.setLineWidth(4);c.line(530,490,705,467)
    c.setLineWidth(2);c.line(320,495,455,495);c.line(320,489,455,489)
    c.setStrokeColor(colors.HexColor("#a44145"));c.setLineWidth(3);c.line(455,485,455,450);c.line(455,450,550,450);c.line(550,450,550,485)
    c.setStrokeColor(colors.black)
    dimension(c,400,140,550,140,"240 mm Bestand")
    dimension(c,550,140,650,140,"160 mm Dämmung")
    label(c,80,630,"Innen",14,True);label(c,820,630,"Außen",14,True)
    notes=[(90,560,"Innenfensterbank 25 mm",320,495),(760,550,"Rahmen, System noch festzulegen",505,530),(760,470,"Außenbank mit Gefälle und Tropfkante",650,473),(760,360,"Leibungsdämmung 30 mm Platzansatz",565,510),(80,345,"Anschlussabdichtung Systemnachweis offen",455,450)]
    for tx,ty,t,ex,ey in notes:label(c,tx,ty,t,11);c.setLineWidth(.7);c.line(tx+80,ty-5,ex,ey)
    label(c,80,88,"D-12/B ersetzt den Brüstungsanschluss A. Kein Nachweis des Wärmebrücken- oder Feuchteschutzes.",11)
    label(c,80,58,"Nordfeld Architektur · gez. Lea Wernicke · zur bauphysikalischen Abstimmung",11);c.save()
    p=inventory(5,5,"Koordinationsschnitt_K07.png","Bildplan K-07 mit Kanalhülle, Unterzug und lichter Höhe")
    im=Image.new("RGB",(1800,1150),"white");d=ImageDraw.Draw(im)
    d.text((65,40),"Schule Brückenanger · Koordinationsschnitt K-07",font=screen_font(34,True),fill="black")
    d.text((65,90),"15.09.2026 · F-01 / Achse 3 · Bezug FFB EG = 0,00 m · zur Koordination",font=screen_font(24),fill="black")
    d.rectangle((150,215,1500,325),fill="#d6d6d6",outline="black",width=3)
    d.rectangle((660,325,1000,460),fill="#b8b8b8",outline="black",width=3)
    d.rectangle((340,475,1370,583),fill="#bfd9e4",outline="#295368",width=4)
    d.rectangle((370,487,1340,571),fill="white",outline="#295368",width=2)
    d.line((150,601,1500,601),fill="#ac4048",width=5)
    d.line((150,580,1500,580),fill="#797979",width=2)
    d.line((150,825,1500,825),fill="black",width=4)
    d.text((1060,347),"UK Unterzug +3,15 m",font=screen_font(27),fill="black")
    d.text((440,510),"Kanal frei 600 x 280 mm; außen 680 x 360 mm",font=screen_font(24),fill="black")
    d.text((160,660),"Direkte Route: 3,15 - 0,05 - 0,36 - 0,06 = 2,68 m",font=screen_font(30,True),fill="#ac4048")
    d.text((160,710),"Projektvorgabe lichte Höhe mindestens 2,75 m; Entwurfsdecke +2,80 m",font=screen_font(26),fill="black")
    d.text((160,875),"Seitliche Route liegt außerhalb dieses Schnitts und ist in L-301/D noch nicht eingetragen.",font=screen_font(24),fill="black")
    d.text((160,925),"50 mm Montageabstand und 60 mm Deckenunterkonstruktion gemäß Koordination 15.09.",font=screen_font(24),fill="black")
    d.text((160,1000),"Nordfeld Architektur · gez. Lea Wernicke · Darstellung nicht zur Maßentnahme",font=screen_font(24),fill="black")
    info=PngImagePlugin.PngInfo();info.add_text("Author",AUTHOR);info.add_text("Title","HM-BA26 K-07 Flurschnitt")
    im.save(p,pnginfo=info)


def hameln_misc():
    inventory(5,8,"Hoehenketten.xlsx","Rechnende Höhenketten direkte und seitliche Kanalroute")
    p=inventory(5,9,"Planindex.csv","Planindex mit unterschiedlichen Revisionen und Verwendungszwecken")
    write_csv(p,[["Projekt","Plan","Revision","Datum","Inhalt","Verwendung","Versand","Verfasser"],
      ["HM-BA26","A-100","G","2026-02-12","Genehmigungsgrundriss","genehmigter Satz","2026-02-27 Bescheid","Lea Wernicke"],
      ["HM-BA26","A-101","B","2026-09-02","Ausbaugrundriss","ersetzt durch C","2026-09-04 Lenz","Lea Wernicke"],
      ["HM-BA26","A-101","C","2026-09-14","Flur und Tür T-01","zur Koordination","2026-09-15 Fachplaner","Lea Wernicke"],
      ["HM-BA26","T-201","B","2026-09-08","Unterzug Achse 3","Fachplan Bestand","2026-09-09 Nordfeld","Iven Rautenberg"],
      ["HM-BA26","L-301","D","2026-09-12","direkte Kanalroute","zur Koordination","2026-09-12 Nordfeld","Tammo Behrens"],
      ["HM-BA26","M-17","0","2026-09-11","Flurverglasung T-01","zur Prüfung","2026-09-11 Nordfeld","Fenja Lenz"],
      ["HM-BA26","D-12","B","2026-09-16","Fensterbrüstung","zur Fachabstimmung","2026-09-16 Bauherr","Lea Wernicke"],
    ])
    p=inventory(5,15,"Planraum_Export.txt","Planraumereignisse ohne behauptete Gesamtfreigabe")
    p.write_text("Planraum Nordfeld Architektur\nProjekt HM-BA26 / Schule Brückenanger\nExport durch Lea Wernicke am 24.09.2026, 16:10 Uhr\n\n02.09.2026 09:30 A-101/B eingestellt, Zweck Koordination\n04.09.2026 11:02 A-101/B an Lenz Metallbau versandt\n08.09.2026 15:42 T-201/B von Rautenberg eingegangen\n11.09.2026 10:18 M-17/0 von Lenz eingegangen, zur Prüfung\n12.09.2026 14:05 L-301/D von Behrens eingegangen\n14.09.2026 17:20 A-101/C eingestellt, B im Büroarchiv ersetzt\n15.09.2026 08:15 A-101/C an Behrens und Rautenberg versandt\n16.09.2026 13:12 D-12/B an Bauherrschaft versandt\n22.09.2026 14:25 TGA-Mail seitliche Route abgelegt\n24.09.2026 14:25 Bauherren-Mail abgelegt\n\nFür A-101/C ist im Export kein Versand an Lenz Metallbau erfasst.\nEine Freigabe zur Ausführung ist für die oben aufgeführten Ausbaupläne nicht eingetragen.\nDie Ereignisliste gibt den gespeicherten Planraumstand wieder; mündliche Erklärungen werden hier nicht erfasst.\ngez. Lea Wernicke\n",encoding="utf-8")


PEINE_POSITIONS = [
 ("01.010","Untergrund Sportboden",288,"m²",12,"Hallengrundriss A-601/B, 24,00 x 12,00 m", "Vorhandenen mineralischen Untergrund der Halle auf der gesamten Innenfläche reinigen und für den neuen Sportboden vorbereiten. Lose Bestandteile entfernen, geeignete Grundierung aufbringen und kleinere örtliche Unebenheiten im vereinbarten Aufbau ausgleichen. Die ausgeschriebene Leistung umfasst keine Sanierung unbekannter Feuchteursachen. Der Untergrundzustand ist vor Beginn gemeinsam aufzunehmen; abweichende Befunde sind vor Überdeckung mitzuteilen."),
 ("01.020","Sportboden Halle",288,"m²",89,"A-601/B Halle, lichte Innenmaße", "Sportboden für die Halle H-01 auf vorbereitetem Untergrund liefern und verlegen. Der Aufbau muss für Schulungs- und Vereinssport geeignet sein und die im Nutzerkonzept beschriebene Nutzung ohne feste Tribüne aufnehmen. Feldmarkierungen für ein Volleyballfeld und ein Badmintonfeld sind enthalten. Die Systemhöhe von 45 mm ist mit Türanschlüssen und Geräteraumübergang abzustimmen. Ein abweichendes System bedarf vor Ausführung des dokumentierten Funktions- und Anschlussnachweises."),
 ("01.030","Sockel Halle",69.48,"m",18,"Umfang 72,00 m abzüglich zwei Türen je 1,26 m", "Sockelabschluss am Sportboden umlaufend an den Hallenwänden herstellen. Die Anschlussfuge des Bodens darf nicht starr überbrückt werden. Innen- und Außenecken, Endstücke an den beiden Hallenausgängen sowie Anschlüsse an die Prallwand sind enthalten. Türbreiten werden vollständig von der geometrischen Länge abgezogen. Die Sockelleistung ist nicht Bestandteil der Prallwandposition."),
 ("02.010","Prallwand Halle",138.96,"m²",115,"Abwicklung A-602/B, 72,00 x 2,00 m minus 5,04 m²", "Prallwandbekleidung in Halle H-01 bis 2,00 m über Fertigfußboden herstellen. Die Bekleidung umfasst die im System erforderliche Unterkonstruktion und geschlossene, für die vereinbarte Sportnutzung geeignete Oberfläche. Die beiden Ausgangsöffnungen werden bis zur Bekleidungshöhe vollständig ausgespart. Geräteraum und Sozialtrakt sind nicht enthalten. Anschlüsse an Türzargen sind ohne vorstehende Kanten auszubilden und mit dem Türlieferanten abzustimmen."),
 ("02.020","Einbauausschnitte Prallwand",8,"St",45,"Elektrobeitrag E-04, acht Einbaupunkte", "Acht Ausschnitte für die bezeichneten Elektroeinbauten in der Prallwand herstellen und deren Ränder systemgerecht schließen. Lage und fertige Einbautiefe sind vor Bearbeitung anhand des Elektroplans E-04 abzustimmen. Die elektrischen Geräte, Leitungen und deren Anschluss sind nicht enthalten. Der Ausschnitt darf die zugesagte Eignung des Bekleidungssystems nicht beeinträchtigen; der erforderliche Systembezug ist vor Ausführung nachzuweisen."),
 ("03.010","Hallendecke",286.56,"m²",64,"A-603/B, 288,00 m² minus vier Öffnungen 0,60 x 0,60 m", "Demontierbare Akustikdecke unter der Hallentragkonstruktion herstellen. Die Unterkonstruktion ist auf den bestätigten Befestigungsgrund und die Lasten des gewählten Systems abzustimmen. Leuchten und Lüftungsauslässe werden nach den Fachplänen integriert; ihre technischen Komponenten gehören zu den Fachlosen. Vier gesondert vergütete Revisionsöffnungen sind in der geometrischen Fläche abgezogen. Die Decke ist nicht als Ersatz für erforderliche Bauteilabschottungen beschrieben."),
 ("03.020","Revisionsklappen",4,"St",145,"A-603/B R-01 bis R-04", "Vier Revisionsklappen mit lichter Öffnung 600 mm mal 600 mm in der Hallendecke liefern und einbauen. Die Ausführung muss zur angrenzenden Decke passen und den Zugang zu den in A-603/B bezeichneten Wartungsstellen erlauben. Verstärkungen der Unterkonstruktion und saubere Randanschlüsse sind enthalten. Die Klappen dürfen nicht durch Leuchten oder Einbauten blockiert werden. Zusätzliche Wartungsstellen sind in dieser Position nicht mengenmäßig erfasst."),
 ("04.010","Trennwände Sozialtrakt",100.1746,"m²",76,"W-01 bis W-05, 34,00 x 3,20 m minus vier Türöffnungen", "Nichttragende Trennwände im Sozialtrakt gemäß Wandliste und Grundriss A-601/B herstellen. Der ausgeschriebene Wandaufbau hat 125 mm Gesamtdicke mit beidseitiger zweilagiger Bekleidung und Hohlraumdämmung. Beide Wandseiten und die erforderliche Unterkonstruktion sind im Einheitspreis der Wandansichtsfläche enthalten. Türöffnungen werden geometrisch vollständig abgezogen. Oberflächenendbehandlung wird in den nachfolgenden Positionen gesondert vergütet."),
 ("04.020","Wandoberflächen vorbereiten",200.3492,"m²",12,"Beide Seiten der Netto-Wandansicht aus 04.010", "Beide sichtbaren Seiten der Trennwände im Sozialtrakt für den vereinbarten Anstrich vorbereiten. Fugen und Befestigungspunkte sind systemgerecht zu bearbeiten; die Fläche muss für den in der nächsten Position beschriebenen Beschichtungsaufbau geeignet sein. Die Leistung wird nach der tatsächlich beschriebenen beidseitigen Fläche angesetzt. Sonderanforderungen aus später gewählten Streiflicht- oder Hochglanzoberflächen sind nicht Bestandteil dieses Textstands."),
 ("04.030","Wandanstrich Sozialtrakt",200.3492,"m²",9.5,"Flächen wie 04.020", "Vorbereitete Wandflächen im Sozialtrakt mit einem für die vereinbarte Nutzung geeigneten, reinigungsfähigen Innenanstrich beschichten. Grundierung und deckender Beschichtungsaufbau in einem hellen Farbton nach Bemusterung sind enthalten. Die Bemusterung betrifft den Farbton, nicht eine offene Änderung der technischen Qualität. Zargen, Bodenflächen und Einbauten sind während der Arbeiten zu schützen. Die Leistung umfasst beide in der Mengenermittlung bezeichneten Wandseiten."),
 ("05.010","Innentüren T-01 bis T-04",4,"St",620,"Türliste TL-02/B, vier Innentüren", "Vier Innentürelemente T-01 bis T-04 für die Räume des Sozialtrakts liefern und einbauen. Türblatt, Zarge, Standardbeschläge und Anschluss an die Trockenbauwand sind enthalten. Die Rohbauöffnungen betragen nach diesem Textstand jeweils 1,01 m mal 2,135 m. Besondere Feuer- oder Rauchschutzanforderungen sind in dieser Position nicht beschrieben. Bodenanschluss und Anschlagrichtung sind vor Fertigung mit der aktuellen Türliste abzugleichen."),
 ("05.020","Hallenausgänge T-05 und T-06",2,"St",1750,"A-601/B zwei Ausgangsöffnungen", "Zwei Türanlagen an den Hallenausgängen T-05 und T-06 gemäß Türliste liefern und einbauen. Die geometrischen Öffnungen betragen jeweils 1,26 m mal 2,26 m. Der Anschluss an Sportboden und Prallwand ist enthalten; vorstehende Kanten im Sportbereich sind zu vermeiden. Die betriebliche Funktion aus dem Brandschutzbeitrag ist mit den vorgesehenen Beschlägen nachzuweisen. Elektroantriebe und Zutrittssteuerung sind nicht vorgesehen."),
 ("06.010","Boden Sozialtrakt",108,"m²",48,"A-601/B lichte Nutzfläche 18,00 x 6,00 m", "Elastischen Bodenbelag im Sozialtrakt auf vorbereitetem Untergrund verlegen. Die Gesamtfläche umfasst Umkleiden, Aufenthaltsraum, Geräteraum und internen Verbindungsbereich gemäß A-601/B. Untergrundvorbereitung im vereinbarten Umfang, Klebung und Übergangsprofile an den Türöffnungen sind enthalten. Nassbelastete Sonderflächen sind nach diesem Stand nicht Bestandteil des Leistungsbereichs. Der Anschluss an den Hallenboden erfolgt höhengleich nach dem bezeichneten Detail."),
 ("06.020","Sockel Sozialtrakt",98,"m",9,"Raumweise Längenliste ML-01, Stand 04.09.2026", "Sockelleisten im Sozialtrakt einschließlich Ecken, Endstücke und Anschlüsse an Türzargen liefern und montieren. Die Länge von 98,00 m stammt aus der raumweisen Längenaufnahme ML-01. Türöffnungen sind darin abgezogen. Leitungsdurchführungen dürfen nicht verdeckt werden, wenn hierfür ein Wartungszugang vorgesehen ist. Die Sockelleisten sind auf den gewählten Bodenbelag abzustimmen; zusätzliche Wandbekleidungen sind nicht enthalten."),
 ("07.010","Schutz und Abschnittstrennung",1,"psch",1450,"Betriebsabstimmung vom 31.08.2026", "Für die Dauer der Ausbauarbeiten den Zugang zum nicht umgebauten Vereinsbüro staubgeschützt vom Arbeitsbereich trennen. Enthalten sind eine provisorische Trennwand mit verschließbarem Durchgang, Schutz der verbleibenden Bodenflächen und Rückbau nach Abschluss. Die Vorhaltung ist für sechs Kalenderwochen angesetzt. Ein öffentlicher Sportbetrieb in der Halle während der Arbeiten ist nicht vorgesehen und wird durch diese Position nicht ermöglicht."),
 ("07.020","Bauendreinigung Ausbau",396,"m²",3.2,"Halle 288,00 m² und Sozialtrakt 108,00 m²", "Die durch dieses Los bearbeiteten Flächen nach Abschluss der Arbeiten von baubedingten Verschmutzungen reinigen. Schutzfolien und eigene Verpackungsreste entfernen, Tür- und Bodenoberflächen entsprechend den Pflegevorgaben des gewählten Systems behandeln. Die Leistung umfasst Halle und Sozialtrakt mit zusammen 396,00 m². Eine laufende Unterhaltsreinigung nach Aufnahme des Betriebs und die Entsorgung fremder Reststoffe sind nicht enthalten."),
]


def define_peine():
    add(6,1,"Planungsauftrag.pdf","2026-04-07","bau","plan","Auftrag Vorbereitung der Vergabe Sporthalle Okerbogen",[
      "Die Sportgemeinschaft Okerbogen e.V. beauftragt Falkenhain Architektur mit der Vorbereitung der Vergabe für den Umbau der vereinseigenen Sporthalle Am Sportanger 8 in Peine. Der Verein handelt für eigene Rechnung. Für das Vorhaben sind nach dem gegenwärtigen Finanzierungsbeschluss keine öffentlichen Zuschüsse beantragt oder bewilligt; die Finanzierung erfolgt aus Eigenmitteln und einem Vereinsdarlehen.",
      ("h","1 Leistungsumfang"),
      "Beauftragt sind die Gebäude-Grundleistungen der Leistungsphase 6 für Rohbauanpassungen, Gebäudehülle und Ausbau. Dazu gehören Mengen aus der abgestimmten Ausführungsplanung, Leistungsbeschreibungen mit Leistungsverzeichnissen, Koordination der Fachschnittstellen, vom Planer bepreiste Leistungsverzeichnisse, Vergleich mit der Kostenberechnung und ein Vergabeterminplan. Angebote werden erst nach gesonderter Entscheidung des Vorstands eingeholt.",
      "Die Technische Ausrüstung plant Harms Gebäudetechnik im eigenen Auftrag. Die Tür- und Verglasungselemente werden fachlich mit Büro Kestner Bauelemente abgestimmt. Falkenhain übernimmt die Koordination der Leistungsgrenzen, nicht die eigenständige Bemessung der technischen Anlagen. Der derzeit zu bearbeitende Ausbauabschnitt ist kein vollständiges LV des Gesamtvorhabens.",
      ("h","2 Unterlagen und Preise"),
      "Für jeden ausgeschriebenen Bereich sind eine ungepreiste externe Fassung und eine getrennte interne Planer-Bepreisung zu liefern. Beide Fassungen müssen dieselben Positionen, Texte, Mengen und Einheiten verwenden. Preisannahmen und Quellen sind intern zu dokumentieren. Eine Kostenspanne aus älteren Projekten ist nicht als aktuelles Angebot zu bezeichnen.",
      "Die Mengen werden auf Basis der projektseitigen geometrischen Ansätze ermittelt. Alle in der Mengenermittlung bezeichneten Öffnungen werden vollständig abgezogen. Eine abweichende Abrechnungsregel ist vor Verwendung ausdrücklich zu vereinbaren und mit den tatsächlich einbezogenen Vertragsbedingungen abzugleichen. Geschützte Standardleistungs- oder Normtexte sind nicht ungeprüft zu übernehmen.",
      ("h","3 Entscheidungen und Termine"),
      "Der Vorstand entscheidet über Qualitätsänderungen, Budget und Aufforderung zur Angebotsabgabe. Die Objektplanung darf keine Unternehmen beauftragen und keine Preisangebote im Namen des Vereins annehmen. Als interner Paketabschluss ist der 16.10.2026 vorgesehen. Der Ausbau soll am 11.01.2027 beginnen. Die Verfahrenszeiten im Terminplan sind zunächst interne Annahmen und keine behaupteten gesetzlichen Mindestfristen.",
      "Für die bezeichnete Stufe wird ein Honorar von 31.000,00 EUR netto vereinbart. Der Auftrag umfasst keine vollständig alternative Leistungsbeschreibung mit Leistungsprogramm. Änderungen des Leistungsziels sind vor Bearbeitung in ihrem Umfang abzustimmen. Torben Riekert und Mira Falkenhain bestätigen den Auftrag am 07.04.2026 in Textform.",
    ])
    add(6,2,"Vorstandsbeschluss.docx","2026-08-28","bau","plan","Vorstandsbeschluss zu Ausbau und Budget",[
      "Der Vorstand hat am 28.08.2026 mit Torben Riekert, Gesa Ahrens und Malte Bredow die Ausbaumaßnahmen beraten. Grundlage waren die Kostenberechnung KB-03 vom 15.07.2026 und das Nutzungskonzept vom 22.06.2026. Der Verein bleibt alleiniger Bauherr und Eigentümer des Grundstücks Am Sportanger 8.",
      ("h","1 Kostenrahmen"),
      "Die Kostenberechnung beträgt 1.065.000,00 EUR netto. Zusätzlich wird eine gesonderte Reserve von 65.000,00 EUR netto geführt. Der Finanzierungsrahmen beträgt damit 1.130.000,00 EUR netto beziehungsweise 1.344.700,00 EUR bei dem für die Planung angesetzten Umsatzsteuersatz von 19 Prozent. Die Reserve ist nicht in die Einheitspreise der Leistungsverzeichnisse einzurechnen.",
      "Für den in dieser Runde bearbeiteten Ausbau sind in KB-03 insgesamt 94.000,00 EUR netto enthalten. Der Betrag setzt sich aus Bodenarbeiten 30.400,00 EUR, Wänden/Oberflächen 38.200,00 EUR, Decken 19.000,00 EUR und Türen 6.400,00 EUR zusammen. Andere Leistungsbereiche des Gesamtprojekts sind davon nicht erfasst.",
      ("h","2 Nutzung und Qualität"),
      "Die Halleninnenfläche von 24,00 m mal 12,00 m bleibt erhalten. Es werden keine Zuschauertribüne und kein regelmäßiger Veranstaltungsbetrieb eingerichtet. Die Prallwand soll in der Halle bis 2,00 m Höhe ausgeführt werden. Im Geräteraum ist keine zusätzliche Prallwand beschlossen. Die vier im bisherigen Ausbauentwurf vorgesehenen Innentüren sind mit dem aktualisierten Brandschutzbeitrag abzugleichen.",
      ("h","3 Einholung von Angeboten"),
      "Nach Fertigstellung und Freigabe der Unterlagen sollen je Leistungsbereich drei geeignete Unternehmen angefragt werden. Diese interne Vereinsregel ist keine Festlegung eines öffentlich-rechtlichen Vergabeverfahrens. Es liegt derzeit keine Förderauflage vor. Sollte sich Finanzierung oder Auftraggeberstatus ändern, ist die Verfahrensgrundlage vor Versand erneut zu prüfen.",
      "Die Angebotsunterlagen dürfen erst nach Entscheidung des Vorstands versandt werden. Planerpreise und interne Kostenvergleiche sind nicht an die angefragten Unternehmen zu geben. Der Beschluss wurde durch Torben Riekert am 28.08.2026 festgestellt und durch Gesa Ahrens protokolliert.",
    ])
    sections=["Das Leistungsverzeichnis LV-AU/02 beschreibt den Ausbau der Sporthalle Okerbogen. Mengen und Texte beruhen auf den Ausführungsplänen A-601/B, A-602/B und A-603/B vom 04.09.2026. Die Unterlage wurde am 14.09.2026 für die interne Abstimmung zusammengestellt. Sie ist noch nicht an Unternehmen versandt.",
      ("h","1 Allgemeine Angaben"),
      "Die Arbeiten betreffen die Halle H-01 und den südlich anschließenden Sozialtrakt. Der Hallenbetrieb ruht während des Ausbaus; das Vereinsbüro bleibt über den westlichen Zugang erreichbar. Die Ausführung ist ab 11.01.2027 für sechs Kalenderwochen vorgesehen. Die endgültige Terminvereinbarung erfolgt mit dem späteren Vertrag.",
      "Die Mengenansätze sind geometrisch aus den bezeichneten Plänen abgeleitet. Die dort aufgeführten Öffnungen werden vollständig abgezogen. Eine andere Abrechnungsmethode ist in diesem Textstand nicht vereinbart. Technische Anlagen und elektrische Anschlüsse sind nur enthalten, soweit eine Position sie ausdrücklich beschreibt. Die Fachlose werden gesondert bearbeitet.",
      ("h","2 Positionen")]
    for oz,title,qty,unit,price,source,body in PEINE_POSITIONS:
        sections += [("h",f"2.{len([x for x in sections if isinstance(x,tuple) and x[0]=='h'])-1}. {oz} {title}"),
                     f"Menge: {qty:.4f} {unit}.".replace(".", ",", 1) + f" Mengenbezug: {source}.",body]
    sections += [("h","3 Anlagen und Textstand"),"Zugehörige Pläne sind A-601/B, A-602/B und A-603/B. Die Türliste TL-02/B ist Grundlage der Türpositionen dieses Stands. Später eingegangene Fachbeiträge sind noch nicht in diese Fassung eingearbeitet. Preise sind in dieser Unterlage nicht enthalten. Die externe Versandfassung wird nach Abschluss der Abstimmung gesondert gekennzeichnet."]
    add(6,7,"LV_Ausbau_ungepreist.docx","2026-09-14","plan","bau","Leistungsverzeichnis Ausbau LV-AU 02",sections)
    add(6,9,"TGA_Schnittstelle.eml","2026-09-18","tga","plan","Wartungsöffnungen Hallendecke",[
      "unser TGA-Stand L-410/C vom 16.09.2026 benötigt insgesamt sechs zugängliche Wartungsstellen in der Hallendecke. Neben R-01 bis R-04 sind R-05 am östlichen Abzweig und R-06 vor der Regelgruppe hinzugekommen. Jede Öffnung ist mit 600 x 600 mm licht angesetzt. Die Lage ist im beigefügten Fachstand bemaßt.",
      "Die Lieferung und der Einbau der Klappen einschließlich Verstärkung der Deckenunterkonstruktion liegen nach unserer bisherigen Abstimmung im Ausbau-LV. Das TGA-LV enthält die zu wartenden Komponenten und deren Kennzeichnung, aber keine Deckenklappen. Die Abschottungen an massiven Bauteilen verbleiben im TGA-Los und sind nicht Bestandteil der Akustikdecke.",
      "Bitte beachten Sie, dass A-603/B noch vier Öffnungen zeigt. Eine Reduzierung auf vier Wartungsstellen bestätigen wir nicht. Für die beiden zusätzlichen Stellen sind keine elektrischen Antriebe erforderlich. Diese Mail enthält keine Aussage zum Preis des Ausbauloses.",
    ],salutation="Sehr geehrte Frau Falkenhain,")
    add(6,11,"Bauelemente.pdf","2026-09-19","metall","plan","Tür T-04 im Leistungsbereich Bauelemente",[
      "Unser Bearbeitungsstand BE-02/C enthält die Tür T-04 zwischen Geräteraum und Verbindungsflur. Die Position wird als vollständiges Element mit Zarge, Türblatt, Beschlägen und den im Brandschutzbeitrag bezeichneten Eigenschaften beschrieben. Der bisherige Standard-Innentüransatz aus TL-02/B ist hierfür nicht ausreichend bestimmt.",
      ("h","1 Mengen- und Leistungsbezug"),
      "Die Rohbauöffnung T-04 bleibt nach dem aktuellen Grundriss A-601/C mit 1,01 m mal 2,135 m geometrisch unverändert. Die Änderung betrifft die Funktion und Ausführung des Elements, nicht eine zusätzliche Öffnung. In unserem Leistungsbereich ist genau ein Element T-04 enthalten. T-01 bis T-03 werden von uns nicht beschrieben.",
      "Die Montage einschließlich Zarge und Anschluss an die Trockenbauwand ist im Bauelemente-Langtext enthalten. Der reine Wandflächenansatz des Ausbaus bleibt davon getrennt. Eine doppelte Lieferung derselben Tür über das Ausbau-LV ist nicht vorgesehen. Der abschließende Schnittstellentext wurde uns noch nicht zur Gegenzeichnung übersandt.",
      ("h","2 Preis- und Terminstand"),
      "Für das Element T-04 führen wir intern einen vorläufigen Planeransatz von 1.850,00 EUR netto. Dieser Betrag ist kein Unternehmensangebot. Er ist in der von uns bearbeiteten Bauelemente-Kostengruppe enthalten und darf nicht zusätzlich als zweite Standardtür in den Ausbaukosten erscheinen. Fertigungszeiten sind erst nach endgültiger Leistungsdefinition verlässlich abzufragen.",
      "Wir bitten um Rückmeldung, welche LV-Version künftig maßgeblich ist. Bis dahin bleibt BE-02/C ein Fachplanungsstand zur Koordination, nicht eine freigegebene Vergabeunterlage.",
    ])
    add(6,12,"Preisannahmen.pdf","2026-09-14","plan","bau","Interne Preisansätze Ausbau September 2026",[
      "Die Planer-Bepreisung LV-AU/02 verwendet die nachstehenden Arbeitsannahmen. Es wurden noch keine aktuellen verbindlichen Angebote eingeholt. Die Ansätze dienen der Kostenkontrolle und dürfen nicht in die ungepreisten Unterlagen für Unternehmen übernommen werden.",
      ("h","1 Herkunft und Preisstand"),
      "Für Sportboden, Prallwand und Akustikdecke wurden interne Vergleichsansätze aus zwei abgeschlossenen kleineren Vereinsumbauten verwendet und auf den Preisstand September 2026 eingeschätzt. Die Vergleichsprojekte sind nicht Bestandteil dieser Akte; die Ansätze sind daher als planerische Annahmen und nicht als nachprüfbare aktuelle Marktangebote zu behandeln. Besondere Lieferbedingungen des späteren Unternehmens sind darin nicht abschließend geklärt.",
      ("t",[["Leistung","Ansatz netto","Umfang"],["Sportboden","89,00 EUR/m²","Systemaufbau und zwei Feldmarkierungen"],["Prallwand","115,00 EUR/m²","Unterkonstruktion und Oberfläche"],["Hallendecke","64,00 EUR/m²","ohne gesonderte Revisionsklappen"],["Revisionsklappe","145,00 EUR/St","600 x 600 mm einschließlich Randverstärkung"],["Standard-Innentür","620,00 EUR/St","ohne besondere Brandschutzqualität"]],[130,115,250]),
      ("h","2 Behandlung von Änderungen"),
      "Die Ansätze gelten nur für den bezeichneten Leistungsumfang. Eine besondere Türfunktion ist nicht mit dem Preis einer Standard-Innentür abgegolten. Zusätzliche Wartungsöffnungen ändern sowohl die Klappenanzahl als auch die geometrische Deckenfläche. Ein pauschaler Reserveaufschlag wurde nicht in die Einheitspreise eingerechnet.",
      "Die Kostenberechnung KB-03 enthält für den betrachteten Ausbau 94.000,00 EUR netto. Die Gesamtkosten und die gesonderte Reserve bleiben in der Kostenberechnung erhalten. Ein günstiger Ausbauvergleich allein erlaubt keine Aussage, dass sämtliche anderen Leistungsbereiche das Gesamtbudget einhalten.",
    ])
    add(6,16,"Brandschutz.eml","2026-09-21","brand","plan","Türfunktion T-04 und Hallenausgänge",[
      "die im aktuellen Brandschutzbeitrag bezeichnete Funktion von T-04 ist mit dem Bauelementeplan BE-02/C abzustimmen. Eine normale Innentür ohne die dort vorgesehene Eigenschaft bestätigt unseren Planungsstand nicht. Die geometrische Rohbauöffnung bleibt nach unserer Unterlage unverändert.",
      "Die beiden Hallenausgänge T-05 und T-06 bleiben in ihrer bisherigen Lage. Die Anschlüsse der Prallwand dürfen deren nutzbare Durchgänge nicht einschränken. Für die endgültige Ausschreibung benötigen wir den konsistenten Türtext und den Anschluss an den Bodenaufbau. Die Auswahl eines konkreten Systems ist noch nicht erfolgt.",
      "Unsere Aussage ersetzt keine Prüfung der gesamten Vergabeunterlage. Bitte führen Sie die Türkennungen in Architektur, Ausbau und Bauelementen identisch weiter. Ein zweites Element T-04 ist nicht vorgesehen.",
    ],salutation="Sehr geehrte Frau Falkenhain,")
    add(6,17,"Nutzerpost.eml","2026-09-24","nutzer","bau","Geräteraum und Prallwand",[
      "beim letzten Gespräch wurde gefragt, ob auch der Geräteraum eine Prallwand erhalten soll. Wir benötigen dort keine zusätzliche Prallwand. Die Geräte werden in den vorgesehenen Schränken und auf mobilen Wagen gelagert; der Raum ist nicht für Ballspiele bestimmt. Die Prallwand in der Halle bis 2,00 m Höhe soll unverändert bleiben.",
      "Bitte die Wartungsöffnungen in der Hallendecke nicht über fest eingebauten Schränken anordnen. Der Zugang zu den technischen Komponenten muss mit einer mobilen Leiter möglich bleiben. Welche Größe und technische Ausführung erforderlich ist, können wir als Nutzer nicht bestätigen.",
      "Die Halle ist vom 11.01.2027 bis 19.02.2027 für den Vereinsbetrieb gesperrt. Für die Woche danach sind noch keine Veranstaltungen gebucht. Eine Verlängerung der Bauzeit haben wir bisher nicht beschlossen. Die Nachricht ist eine Nutzerangabe und keine Vergabe- oder Kostenfreigabe des Vorstands.",
    ],salutation="Sehr geehrter Herr Riekert,")
    add(6,18,"Koordinationsprotokoll.docx","2026-09-22","plan","bau","Unterlagenstand Ausbau und Bauelemente",[
      "Am 22.09.2026 wurden die eingegangenen Fachbeiträge zwischen Mira Falkenhain, Enno Harms und Sina Kestner besprochen. Torben Riekert nahm für den Verein teil. Gegenstand waren die Ausbauliste LV-AU/02 vom 14.09.2026, die Türliste TL-02/C vom 19.09.2026 und die TGA-Mail vom 18.09.2026.",
      ("h","1 Türen"),
      "Kestner führt T-04 im Bauelemente-Leistungsbereich BE-02/C. Falkenhain weist darauf hin, dass LV-AU/02 noch vier Standard-Innentüren enthält. Die Rohbauöffnung T-04 bleibt unverändert. Die Endfassung des Schnittstellentextes soll mit beiden Leistungsbereichen abgeglichen werden; in der Sitzung wurde kein korrigiertes LV ausgegeben.",
      ("h","2 Decke"),
      "Harms bestätigt sechs Wartungsstellen. Der Architektur-Deckenplan A-603/B enthält vier Revisionsöffnungen. Die beiden zusätzlichen Stellen werden im nächsten Planlauf räumlich mit Leuchten und Unterkonstruktion abgestimmt. Die Planer-Bepreisung vom 14.09.2026 wurde während der Sitzung nicht neu gerechnet.",
      ("h","3 Kosten und Termine"),
      "Der Vorstand hält den internen Paketabschluss 16.10.2026 fest. Für die Angebotsphase sind vorläufig 21 Kalendertage und für Prüfung/Entscheidung 14 Kalendertage angesetzt. Diese Zeiträume sind interne Annahmen. Die Rückmeldung eines Unternehmens zu 35 Kalendertagen Fertigungsvorlauf liegt nur als unverbindliche telefonische Auskunft vor; eine verbindliche Lieferzusage besteht nicht.",
      "Die ursprüngliche Kostenberechnung KB-03 bleibt als Vergleichsbasis erhalten. Planänderungen und Preisänderungen sollen in der nächsten Planerfassung erkennbar sein. Der Vorstand hat noch keine Versandfreigabe erteilt. Das Protokoll wurde am 22.09.2026 durch Mira Falkenhain versandt; Einwendungen zum Gesprächsinhalt lagen bei Versand nicht vor.",
    ])


def peine_plans():
    p=inventory(6,4,"Grundriss_A601C.pdf","Ausführungsgrundriss A-601/C mit Hallenmaßen und Türkennungen")
    c=plan_canvas(p,6,"Sporthalle Okerbogen Ausbaugrundriss","A-601/C","19.09.2026","Vermasste Projektzeichnung")
    ox=100;oy=355;s=30
    c.setLineWidth(3);c.rect(ox,oy,24*s,12*s);c.rect(ox+3*s,oy-6*s,18*s,6*s)
    for x in (7,12,16):c.line(ox+x*s,oy-6*s,ox+x*s,oy)
    label(c,ox+250,oy+190,"H-01 Sporthalle",18,True);label(c,ox+230,oy+150,"lichte Innenmaße 24,00 x 12,00 m",13)
    label(c,ox+270,oy+115,"Bodenfläche 288,00 m²",12)
    for i,x in enumerate((4,8,13,17)):
        label(c,ox+x*s,oy-75,["Umkleide 1","Umkleide 2","Aufenthalt","Geräte"][i],10)
        label(c,ox+x*s,oy-35,f"T-0{i+1}",11,True)
    for x,t in ((0,"T-05"),(24,"T-06")):
        c.setStrokeColor(colors.white);c.setLineWidth(7);c.line(ox+x*s,oy+1*s,ox+x*s,oy+2.26*s)
        c.setStrokeColor(colors.black);c.setLineWidth(1);label(c,ox+x*s-15,oy+15,t,11,True)
    dimension(c,ox,oy+12*s+35,ox+24*s,oy+12*s+35,"24,00 m")
    dimension(c,ox-40,oy,ox-40,oy+12*s,"12,00 m")
    dimension(c,ox+3*s,oy-6*s-30,ox+21*s,oy-6*s-30,"18,00 m")
    dimension(c,ox+22*s,oy-6*s,ox+22*s,oy,"6,00 m")
    for i,t in enumerate(["Halle: lichte Höhe 4,80 m", "Prallwand bis 2,00 m", "6 Fenster je 1,50 x 1,20 m", "2 Hallentüren je 1,26 x 2,26 m", "Sozialtrakt: Höhe 3,20 m", "Innenwände Länge gesamt 34,00 m", "4 Öffnungen je 1,01 x 2,135 m", "T-04 Funktion geändert, Öffnung gleich", "Revision C: Türzuordnung T-04", "gez. Mira Falkenhain"]):label(c,880,700-i*40,t,11)
    label(c,80,75,"Maßangaben sind lichte Rechenmaße des Ausbaus. Wanddicken werden in den Flächenansätzen nicht zusätzlich abgezogen.",10)
    label(c,80,50,"Falkenhain Architektur · Bezug PE-OB26 · Planstand zur LV-Koordination",11);c.save()
    p=inventory(6,5,"Wandabwicklung_A602B.png","Bildplan Hallenwandabwicklung A-602/B mit Öffnungen und Prallwandhöhe")
    im=Image.new("RGB",(1900,1350),"white");d=ImageDraw.Draw(im)
    d.text((60,35),"Sporthalle Okerbogen · Hallenwandabwicklung A-602/B",font=screen_font(34,True),fill="black")
    d.text((60,87),"04.09.2026 · Innenumfang 72,00 m · Höhe 4,80 m · Prallwand bis 2,00 m",font=screen_font(24),fill="black")
    def elevation(x,y,length,windows,door,title):
        sc=26;w=int(length*sc);h=int(4.8*sc)
        d.rectangle((x,y,x+w,y+h),fill="#f5f5f5",outline="#202020",width=3)
        d.rectangle((x,y+h-52,x+w,y+h),fill="#d5dfc8",outline="#455d39",width=2)
        for wx in windows:
            d.rectangle((x+int(wx*sc),y+20,x+int((wx+1.5)*sc),y+20+31),fill="#c9dfec",outline="#284657",width=2)
        if door:d.rectangle((x+int(door*sc),y+h-59,x+int((door+1.26)*sc),y+h),fill="white",outline="black",width=3)
        d.text((x,y-40),title,font=screen_font(25,True),fill="black")
        d.text((x,y+h+18),f"Länge {length:.2f} m",font=screen_font(23),fill="black")
    elevation(100,240,24,[3,10,17],None,"Nord 24,00 m")
    elevation(1050,240,12,[],3,"Ost 12,00 m / T-06")
    elevation(100,620,24,[3,10,17],None,"Süd 24,00 m")
    elevation(1050,620,12,[],3,"West 12,00 m / T-05")
    lines=["Fenster: 6 x 1,50 x 1,20 m. Unterkante 2,85 m über FFB.","Hallentüren: 2 x 1,26 x 2,26 m. Im Prallwandband werden je 1,26 x 2,00 m abgezogen.","Prallwandband: 72,00 x 2,00 m abzüglich 5,04 m² = 138,96 m².","Grüne Fläche = Prallwand. Blaue Fläche = Fenster. Weiße Aussparung = Tür.","Geräteraum ist in dieser Abwicklung nicht enthalten. Keine Maßentnahme aus Bildpixeln.","Falkenhain Architektur · gez. Mira Falkenhain · PE-OB26 · zur Mengenermittlung"]
    for i,t in enumerate(lines):d.text((100,955+i*48),t,font=screen_font(24),fill="black")
    info=PngImagePlugin.PngInfo();info.add_text("Author",AUTHOR);info.add_text("Title","PE-OB26 A-602/B Wandabwicklung")
    im.save(p,pnginfo=info)


def peine_misc():
    for n,name,title in [(3,"Kostenberechnung.xlsx","Kostenberechnung KB-03 mit Ausbauanteil und getrennter Reserve"),(6,"Mengenermittlung.xlsx","Rechnende geometrische Ansätze ML-01"),(8,"Planer_LV.xlsx","Interne Planer-Bepreisung LV-AU/02 und Kostenüberleitung"),(13,"Vergabetermine.xlsx","Rechnender interner Vergabeterminplan mit Rückwärtsterminen")]:inventory(6,n,name,title)
    p=inventory(6,10,"Tuerliste.csv","Türliste TL-02/C mit Leistungsbereichszuordnung")
    write_csv(p,[["Projekt","Tür","Raum","Breite_m","Höhe_m","Funktion","Leistungsbereich","Revision","Datum","Verfasser"],
      ["PE-OB26","T-01","Umkleide 1",1.01,2.135,"Innentür Standard","Ausbau","C","2026-09-19","Mira Falkenhain"],
      ["PE-OB26","T-02","Umkleide 2",1.01,2.135,"Innentür Standard","Ausbau","C","2026-09-19","Mira Falkenhain"],
      ["PE-OB26","T-03","Aufenthalt",1.01,2.135,"Innentür Standard","Ausbau","C","2026-09-19","Mira Falkenhain"],
      ["PE-OB26","T-04","Geräteraum",1.01,2.135,"gemäß BS-03 und BE-02/C","Bauelemente","C","2026-09-19","Sina Kestner"],
      ["PE-OB26","T-05","Halle West",1.26,2.26,"Hallenausgang","Ausbau","C","2026-09-19","Mira Falkenhain"],
      ["PE-OB26","T-06","Halle Ost",1.26,2.26,"Hallenausgang","Ausbau","C","2026-09-19","Mira Falkenhain"],
    ])
    p=inventory(6,14,"Planindex.csv","Planindex mit älterer Mengenbasis und neuen Fachbeiträgen")
    write_csv(p,[["Plan","Revision","Datum","Inhalt","Status","Empfänger","Verfasser"],
      ["A-601","B","2026-09-04","Grundriss mit vier Standard-Innentüren","Basis LV-AU/02","Vorstand","Mira Falkenhain"],
      ["A-601","C","2026-09-19","T-04 Bauelemente, Geometrie unverändert","zur Koordination","Kestner/Harms","Mira Falkenhain"],
      ["A-602","B","2026-09-04","Hallenwandabwicklung","Mengengrundlage","Vorstand","Mira Falkenhain"],
      ["A-603","B","2026-09-04","Hallendecke mit vier Öffnungen","Basis LV-AU/02","Harms","Mira Falkenhain"],
      ["L-410","C","2026-09-16","sechs Wartungsstellen","Fachbeitrag","Falkenhain","Enno Harms"],
      ["TL-02","C","2026-09-19","Türliste T-04 zugeordnet","zur Koordination","Vorstand","Sina Kestner"],
      ["BE-02","C","2026-09-19","Bauelemente einschließlich T-04","Fachbeitrag","Falkenhain","Sina Kestner"],
    ])
    p=inventory(6,15,"Projektkalender.txt","Projektkalender und dokumentierte interne Terminannahmen")
    p.write_text("Sportgemeinschaft Okerbogen e.V.\nPE-OB26 · Projektkalender\nStand 22.09.2026 · erfasst von Torben Riekert\n\nPaketabschluss intern angestrebt: 16.10.2026\nPrüfung und Versandentscheidung Vorstand: 7 Kalendertage\nAngebotszeit als interne Annahme: 21 Kalendertage\nPrüfung und Entscheidung: 14 Kalendertage\nFertigungsvorlauf als unbestätigte Annahme: 35 Kalendertage\nGeplanter Ausbaubeginn: 11.01.2027\nHallenbelegung gesperrt: 11.01.2027 bis 19.02.2027\n\nDie Rechnung verwendet Kalendertage ohne gesonderten Feiertagskalender.\nDer Zeitraum 24.12.2026 bis 03.01.2027 ist bei mehreren Unternehmen als mögliche Betriebspause angesprochen worden, aber noch nicht verbindlich geklärt.\nEine Angebotsaufforderung ist noch nicht versandt.\nKeine der internen Zeitannahmen wird als gesetzliche Mindestfrist bezeichnet.\nFertigung beginnt erst nach Beauftragung und bestätigter Montageplanung.\ngez. Torben Riekert\n",encoding="utf-8")


def write_readme_rubric(phase):
    cfg=CASES[phase]; case=ROOT/"testakten"/cfg["slug"]
    intro={4:"Eigenständiger Werkhofneubau mit eingereichtem Plansatz, vermessener Nordgrenze, Nachforderung und noch offener Bauherrenentscheidung. Übungsgebiet: Antragszusammenstellung, Abweichung oder Plananpassung, Landesrecht und Nachreichungsstand.",
           5:"Eigenständiger Schulumbau mit Genehmigungsvorlauf, ausführungsbezogenen Details, widersprüchlichen Kanalhöhen und einem Montageplan mit abweichender Türbreite. Übungsgebiet: Fachkoordination, Maßketten, Revisionsführung und begrenzter Montageplanabgleich.",
           6:"Eigenständiger privater Sporthallenumbau mit Kostenberechnung, geometrischen Mengen, vollständigem Langtext-LV und neuerer Fachkorrespondenz. Übungsgebiet: Mengen-/Leistungsabgleich, ungepreiste und Planerfassung, Schnittstellen, Kostenkontrolle und Vergabetermine."}[phase]
    inv="\n".join(f"| [{name}]({name}) | {title} |" for name,title in sorted(INVENTORY[phase]))
    text=f'''<!-- decimal-headings -->
# {cfg['title']}

<!-- BEGIN gesamt-pdf-section (autogen) -->
## Downloads

{NOTICE_MARKDOWN}

| Fassung | Download |
| --- | --- |
| Gesamt-PDF | [Gesamtakte](gesamt-pdf/{cfg['slug']}_gesamt.pdf) |
| Originalformat-ZIP | [Originale](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-{cfg['slug']}.zip) |
| Einzel-PDF-ZIP | [Einzel-PDFs](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-{cfg['slug']}-einzelpdfs.zip) |
<!-- END gesamt-pdf-section (autogen) -->

Autor: Klotzkette. Aktenstand: {cfg['date']}. {cfg['count']} eigenständige Originalunterlagen. {intro}

## Herkunft und Abgrenzung

Alle Personen, Firmen, Vereins-/Behördenvorgänge, Grundstücke, Anschriften, Planungen und Zahlen wurden für diese Akte neu erfunden. Die Ortsnamen Celle, Hameln und Peine sowie die verlinkten Rechtsquellen sind real. Scheinbar behördliche Schreiben stammen nicht von einer Behörde. Es werden keine echten Identitätsnachweise, Siegel, Stempel oder Bankdaten verwendet. Kontaktadressen verwenden die reservierte Endung .example. Die Akte enthält keine Musterlösung; interne Rubrik und Builder werden nicht als Originalunterlagen ausgeliefert.
<!-- reserved-example-contacts -->

Die Fälle betreffen Gebäude. Gebäude und Innenräume bilden gemeinsam das Leistungsbild nach Paragraf 34 HOAI; bei Innenraumaufträgen sind Vertragsumfang und abweichende Bewertungen gesondert zu prüfen. Fachplanungsbeiträge sind keine Übernahme anderer Leistungsbilder.

## Originalinventar

| Datei | Inhalt |
| --- | --- |
{inv}

## Quellen und technische Grenzen

[HOAI Anlage 10](https://www.gesetze-im-internet.de/hoai_2013/anlage_10.html), [Paragraf 34 HOAI](https://www.gesetze-im-internet.de/hoai_2013/__34.html) und [Paragraf 650p BGB](https://www.gesetze-im-internet.de/bgb/__650p.html) wurden am 25.09.2026 gezielt gelesen. Einzelheiten und Zugriffsgrenzen stehen im [Phasenprotokoll](../../bauwirtschaft/references/hoai-{phase}-fachquellen.md). Keine vollständige Landesrechts-, DIN-/ATV- oder Rechtsprechungsprüfung und kein Live-Modelltest. Projektspezifische Maße und Rechenregeln sind keine allgemeinen technischen Normen. Honoraranteile sind keine Baufortschrittsanteile; der HOAI-Leistungsbeschrieb ersetzt keinen Vertrag.

## Reproduktion und Prüfung

`scripts/build-bauwirtschaft-hoai-4-6-akten.py --phase {phase}` erzeugt ausschließlich diese Originale und Begleitdateien. Die Excel-Autorenschaft erfolgt mit Artifact Tool über den phasenbezogenen Workbook-Builder. `scripts/build-bauwirtschaft-hoai-4-6-qa.py` führt native Neuberechnung, Eingabemutationen und Renderprüfungen aus. `scripts/test-bauwirtschaft-hoai-4-6.py` prüft offline die Originale; `--assets DIR` ergänzt die Prüfung kanonischer Exporte. Der zentrale Gesamt-PDF-Builder wird für die Lesefassung verwendet. Kein vorhandenes Gesamt-PDF wird durch den Originalbuilder gelöscht.
'''
    (case/"README.md").write_text(normalize_decimal_headings(text),encoding="utf-8")
    focus={4:[("vertrag","01_Planervertrag.pdf","Stufenauftrag, begrenzte Vollmacht und offene Abweichungsentscheidung."),("bildplan","14_Nordvariante_G03.png","Echte gezeichnete Varianten mit geometrischem Bezug."),("berechnung","06_Flaechen.xlsx","Formelbasierte Flächen und separate Stellplatzansätze."),("nachforderung","11_Nachforderung.pdf","Antragseingang und Genehmigung sind nicht gleichgesetzt.")],
           5:[("vertrag","01_Planungsauftrag.pdf","Begrenzter Planungsabruf und getrennte Fachverantwortung."),("bildplan","05_Koordinationsschnitt_K07.png","Kanalhülle und Unterzug räumlich sichtbar."),("berechnung","08_Hoehenketten.xlsx","Nachvollziehbare Höhenkette statt behaupteter Ausführungsreife."),("montage","11_Montageplan_M17.pdf","Eigenständiger Unternehmerplan mit älterem Bezugsstand.")],
           6:[("vertrag","01_Planungsauftrag.pdf","Privater Auftrag und interne Einholungsregeln."),("bildplan","05_Wandabwicklung_A602B.png","Tatsächliche Öffnungen und Prallwandband dargestellt."),("berechnung","06_Mengenermittlung.xlsx","Geometrische Mengen mit Formeln und Planbezug."),("langtext","07_LV_Ausbau_ungepreist.docx","Individuelle vollständige Leistungsbeschreibungen.")]}[phase]
    lines=[f"name: {cfg['slug']}","plugin: bauwirtschaft","author: Klotzkette",f"description: Gebäude-Leistungsphase {phase} im eigenständigen Projekt {cfg['short']}.","checks:"]
    for id_,path,desc in focus:lines += [f"  - id: {id_}","    check_type: file_exists",f"    path: {path}",f"    description: {desc}"]
    lines += ["  - id: belegbezogenes-endprodukt","    check_type: human_review","    description: Beauftragtes Dokument vollständig ausformulieren und Aussagen konkreten Planständen und Absendern zuordnen.","  - id: fortsetzung-und-befugnis","    check_type: human_review","    description: Folgeantworten im selben Stand einarbeiten, Fachfreigaben und Außenhandlungen nicht erfinden.","  - id: norm-und-vertrag","    check_type: human_review","    description: Auftrag, Grundleistung und Besondere Leistung trennen und tragende Normen zeitbezogen verifizieren."]
    (case/"rubric.yaml").write_text("\n".join(lines)+"\n",encoding="utf-8")


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--phase",type=int,choices=[4,5,6],action="append")
    parser.add_argument("--qa-dir",type=Path,default=Path(tempfile.gettempdir())/"hoai-4-6-qa")
    parser.add_argument("--without-workbooks",action="store_true")
    args=parser.parse_args(); phases=args.phase or [4,5,6]
    args.qa_dir.mkdir(parents=True,exist_ok=True);register_fonts()
    for phase in phases:
        case=ROOT/"testakten"/CASES[phase]["slug"];case.mkdir(parents=True,exist_ok=True)
        if phase==4:define_celle();celle_plans();celle_misc()
        elif phase==5:define_hameln();hameln_plans();hameln_misc()
        else:define_peine();peine_plans();peine_misc()
        for record in RECORDS[phase]:
            target=case/record["file"]
            {".pdf":letter_pdf,".docx":letter_docx,".eml":letter_eml}[target.suffix](phase,record,target)
        write_readme_rubric(phase)
        assert len(INVENTORY[phase])==CASES[phase]["count"],INVENTORY[phase]
        print(f"LPH {phase}: {len(INVENTORY[phase])} Originale",flush=True)
    data={str(p):{"directory":str(ROOT/"testakten"/CASES[p]["slug"]),"files":sorted(INVENTORY[p])} for p in phases}
    if 6 in phases:data["6"]["positions"]=PEINE_POSITIONS
    (args.qa_dir/"build-data.json").write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding="utf-8")
    if not args.without_workbooks:
        subprocess.run([node_binary(),str(ROOT/"scripts/build-bauwirtschaft-hoai-4-6-workbooks.mjs"),"--qa-dir",str(args.qa_dir)],check=True)


if __name__=="__main__":main()
