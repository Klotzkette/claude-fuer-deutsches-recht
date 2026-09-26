#!/usr/bin/env python3
"""Individuelle Originale der Gebäudephasen 1 bis 3. Autor: Klotzkette."""
from __future__ import annotations

import argparse
import csv
from datetime import datetime
from email import policy
from email.message import EmailMessage
from email.utils import format_datetime
import json
import os
from pathlib import Path
import subprocess
from xml.sax.saxutils import escape
from zoneinfo import ZoneInfo

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import Image, PngImagePlugin
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from akten_build_runtime import node_binary, serif_font_path

ROOT = Path(__file__).resolve().parents[1]
AUTHOR = "Klotzkette"
CASES = {
    1: dict(slug="bauwirtschaft-hoai-1-grundlagen-kulturhof-detmold", code="KD-26-01", city="Detmold", title="Kulturhof Am Buchenrain", files=[
        "01_2026-02-02_Eigentuemerbeschluss.docx", "02_2026-02-05_Planungsvertrag.pdf",
        "03_2026-02-06_Abruf.eml", "04_2026-02-09_Nutzerangaben.docx",
        "05_2026-02-10_Belegung.csv", "06_1998-06-16_Altplan.pdf",
        "07_2026-02-12_Ortsbesichtigung.docx", "08_2026-02-12_Begehungsskizze.png",
        "09_2026-02-13_Hausmeisternotiz.txt", "10_2026-02-16_Angebot_Tragwerk.pdf",
        "11_2026-02-16_Angebot_Schadstofferkundung.pdf", "12_2026-02-17_Untersuchungsbudget.xlsx",
        "13_2026-02-18_Finanzrahmen.pdf", "14_2026-02-19_Betreiberabweichung.eml",
        "15_2026-02-20_Archivantwort.eml", "16_2026-02-23_Sitzungsauszug.docx"], actors={
            "owner": ("Stiftung Buchenrain Kultur", "Am Buchenrain 14 · 32760 Detmold", "vorstand@buchenrain.example", "Hanna Wendt, Vorstand"),
            "plan": ("Marlene Voss Architektur", "Lerchenstieg 8 · 32756 Detmold", "mv@voss-plan.example", "Marlene Voss, Architektin"),
            "user": ("Kulturkreis Buchenrain e.V.", "Am Buchenrain 14 · 32760 Detmold", "betrieb@kulturkreis.example", "Ruben Kersten, Betriebsleitung"),
            "stat": ("Ingenieurbüro Fenn und Partner", "Feldwinkel 9 · 32805 Horn-Bad Meinberg", "post@fenn-tragwerk.example", "Joris Fenn, Tragwerksplaner"),
            "lab": ("Materiallabor Lippe Nord GmbH", "Gewerbeweg 22 · 32657 Lemgo", "proben@lippe-nord.example", "Dr. Nora Breden, Projektleitung"),
        }),
    2: dict(slug="bauwirtschaft-hoai-2-vorplanung-kita-bad-pyrmont", code="KP-26-02", city="Bad Pyrmont", title="Kita Wiesenbogen", files=[
        "01_2026-03-02_Planungsabruf.pdf", "02_2026-03-04_Betreiberprogramm.docx",
        "03_2026-03-05_Grundstuecksskizze.png", "04_2026-03-12_V1_Erdgeschoss.pdf",
        "05_2026-03-12_V2_Erdgeschoss_Obergeschoss.pdf", "06_2026-03-13_Vorplanungserlaeuterung.docx",
        "07_2026-03-16_Technikkonzept.eml", "08_2026-03-17_Tragwerkskonzept.pdf",
        "09_2026-03-18_Gespraechsvermerk.docx", "10_2026-03-19_Kostenschaetzung.xlsx",
        "11_2026-03-19_Mengenauszug.csv", "12_2026-03-20_Kuechenangebot.pdf",
        "13_2026-03-20_Rahmentermine.txt", "14_2026-03-23_Betreiberantwort.eml",
        "15_2026-03-24_Finanzausschuss.pdf", "16_2026-03-25_Nachbarschaft.eml"], actors={
            "owner": ("Wiesenbogen Bildung gGmbH", "Wiesenbogen 6 · 31812 Bad Pyrmont", "bau@wiesenbogen.example", "Edda Lammers, Geschäftsführung"),
            "plan": ("Büro Sander Gebäudeplanung", "Quellenstieg 11 · 31812 Bad Pyrmont", "planung@sander-bau.example", "Levin Sander, Architekt"),
            "user": ("Kinderhaus Wiesenbogen", "Wiesenbogen 6 · 31812 Bad Pyrmont", "leitung@kinderhaus.example", "Mira Töpel, Einrichtungsleitung"),
            "tga": ("Ingenieurbüro Oertel Haustechnik", "Talwiese 4 · 31855 Aerzen", "ao@oertel-tga.example", "Arne Oertel, Fachplanung"),
            "stat": ("Sanderau Tragwerk", "Holzacker 12 · 32676 Lügde", "statik@sanderau.example", "Fenja Sanderau, Tragwerksplanung"),
            "kitchen": ("Küchenbau Rieken GmbH", "Werkhof 3 · 31860 Emmerthal", "angebot@rieken-kueche.example", "Lutz Rieken, Vertrieb"),
            "neighbor": ("Mara Lindhoff", "Wiesenbogen 8 · 31812 Bad Pyrmont", "ml@lindhoff.example", "Mara Lindhoff"),
        }),
    3: dict(slug="bauwirtschaft-hoai-3-entwurf-aerztehaus-stadthagen", code="AS-26-03", city="Stadthagen", title="Ärztehaus Am Mühlenanger", files=[
        "01_2026-04-08_Entwurfsabruf.pdf", "02_2026-04-10_Vorplanungsentscheidung.docx",
        "03_2026-06-01_Entwurf_EG.pdf", "04_2026-06-01_Entwurf_OG.pdf",
        "05_2026-06-01_Schnitt_Ansicht.pdf", "06_2026-06-02_Objektbeschreibung.docx",
        "07_2026-06-03_TGA_Schacht.png", "08_2026-06-03_Tragwerksnotiz.pdf",
        "09_2026-06-04_TGA_Beitrag.pdf", "10_2026-06-05_Raumliste.csv",
        "11_2026-06-08_Kostenberechnung.xlsx", "12_2026-04-01_Kostenschaetzung.pdf",
        "13_2026-06-09_Koordination.docx", "14_2026-06-10_Terminfortschreibung.xlsx",
        "15_2026-06-11_Betreiberwunsch.eml", "16_2026-06-12_Planversand.txt"], actors={
            "owner": ("Mühlenanger Immobilien KG", "Am Mühlenanger 9 · 31655 Stadthagen", "projekt@muehlenanger.example", "Theda Mertin, Projektleitung"),
            "plan": ("Architektur Heller und Seifert", "Lindenbreite 17 · 31655 Stadthagen", "hs@heller-seifert.example", "Janne Heller, Architektin"),
            "tga": ("Technikplanung Rötte", "Am Südhang 5 · 31675 Bückeburg", "planung@roette.example", "Malte Rötte, Fachplaner"),
            "stat": ("Ingenieurbüro Rabe Tragwerk", "Wiesenort 21 · 31553 Sachsenhagen", "rabe@tragwerk-rabe.example", "Svea Rabe, Tragwerksplanerin"),
            "user": ("Praxisgemeinschaft Mühlenanger", "Am Mühlenanger 9 · 31655 Stadthagen", "verwaltung@praxis-muehlenanger.example", "Dr. Enno Felder, Sprecher der Praxisgemeinschaft"),
        }),
}
DOCS: dict[int, dict[int, dict]] = {1: {}, 2: {}, 3: {}}
BODY = ParagraphStyle("Text", fontName="AktenSerif", fontSize=11, leading=14.2, spaceAfter=8)
SMALL = ParagraphStyle("Klein", parent=BODY, fontSize=9, leading=11, spaceAfter=5)
HEAD = ParagraphStyle("Abschnitt", parent=BODY, fontName="AktenSerifB", spaceBefore=8, spaceAfter=8, keepWithNext=True)
TITLE = ParagraphStyle("Titel", parent=HEAD, fontSize=15, leading=18, spaceAfter=12)


def register_fonts():
    for name, bold in (("AktenSerif", False), ("AktenSerifB", True)):
        pdfmetrics.registerFont(TTFont(name, str(serif_font_path(bold))))
    pdfmetrics.registerFontFamily("AktenSerif", normal="AktenSerif", bold="AktenSerifB", italic="AktenSerif", boldItalic="AktenSerifB")


def para(text, style=BODY):
    return Paragraph(escape(str(text)).replace("\n", "<br/>"), style)


def table(rows, widths=None):
    widths = widths or [491 / len(rows[0])] * len(rows[0])
    result = Table([[para(v, SMALL) for v in row] for row in rows], colWidths=widths, repeatRows=1, hAlign="LEFT")
    result.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e4e9e7")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("GRID", (0, 0), (-1, -1), .3, colors.HexColor("#c4ccca")),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    return result


def record(phase, number, sender, recipient, title, body, signer=None):
    c = CASES[phase]
    DOCS[phase][number] = dict(number=number, sender=sender, recipient=recipient, title=title,
        body=body, date=c["files"][number-1][3:13], signer=signer or c["actors"][sender][3])


def make_pdf(phase, d, dest):
    c = CASES[phase]; issuer = c["actors"][d["sender"]]; recipient = c["actors"][d["recipient"]]
    def frame(cv, doc):
        cv.setFont("AktenSerifB", 12); cv.drawString(52, 798, issuer[0])
        cv.setFont("AktenSerif", 9); cv.drawString(52, 783, issuer[1]); cv.drawString(52, 770, issuer[2])
        cv.setFont("AktenSerif", 8); cv.drawString(52, 31, c["code"] + " · " + d["date"])
        cv.drawRightString(543, 31, f"Seite {doc.page}")
    flow = [para(recipient[0]+"\n"+recipient[1], SMALL), para(f"{c['city']}, {datetime.fromisoformat(d['date']):%d.%m.%Y} · {c['code']}", SMALL),
            para(d["title"], TITLE), para("Sehr geehrte Damen und Herren,")]
    for item in d["body"]:
        if isinstance(item, str): flow.append(para(item))
        elif item[0] == "h": flow.append(para(item[1], HEAD))
        elif item[0] == "t": flow.extend([table(item[1], item[2] if len(item)>2 else None), Spacer(1, 8)])
    flow.append(KeepTogether([Spacer(1, 6), para("Mit freundlichen Grüßen"), para("gez. "+d["signer"]), para("Bezug: "+c["code"]+" · Anlagen wie im Text bezeichnet.", SMALL)]))
    SimpleDocTemplate(str(dest), pagesize=A4, leftMargin=52, rightMargin=52, topMargin=91, bottomMargin=51,
                      title=d["title"], author=AUTHOR, creator=AUTHOR, invariant=1).build(flow, onFirstPage=frame, onLaterPages=frame)


def make_docx(phase, d, dest):
    c = CASES[phase]; doc = Document(); sec = doc.sections[0]
    compact_table = phase == 2 and d["number"] == 2
    sec.page_width=Cm(21); sec.page_height=Cm(29.7); sec.top_margin=Cm(1.6); sec.bottom_margin=Cm(1.8)
    sec.left_margin=Cm(2); sec.right_margin=Cm(2); sec.footer_distance=Cm(.8)
    for style in doc.styles:
        if style.type != 1: continue
        style.font.name="Times New Roman"; style.font.size=Pt(11); style.font.color.rgb=RGBColor(0,0,0)
        style.paragraph_format.space_after=Pt(5 if compact_table else 7)
        fonts=style.element.get_or_add_rPr().get_or_add_rFonts()
        for key in list(fonts.attrib):
            if key.endswith("Theme"): del fonts.attrib[key]
        for key in ("ascii","hAnsi","eastAsia","cs"): fonts.set(qn("w:"+key),"Times New Roman")
        for border in style.element.xpath("./w:pPr/w:pBdr"): border.getparent().remove(border)
    doc.styles["Title"].font.size=Pt(15); doc.styles["Title"].paragraph_format.space_after=Pt(10)
    doc.styles["Heading 1"].font.size=Pt(12); doc.styles["Heading 1"].font.bold=True
    doc.styles["Heading 1"].paragraph_format.space_before=Pt(8)
    p=doc.core_properties; p.author=AUTHOR; p.last_modified_by=AUTHOR; p.title=d["title"]; p.language="de-DE"
    p.created=datetime.fromisoformat(d["date"]); p.modified=p.created
    sender=c["actors"][d["sender"]]; recipient=c["actors"][d["recipient"]]
    doc.add_paragraph(sender[0]).runs[0].bold=True
    doc.add_paragraph(sender[1]+"\n"+sender[2]); doc.add_paragraph(recipient[0]+"\n"+recipient[1])
    doc.add_paragraph(f"{c['city']}, {datetime.fromisoformat(d['date']):%d.%m.%Y} · {c['code']}")
    doc.add_paragraph(d["title"],"Title"); doc.add_paragraph("Sehr geehrte Damen und Herren,")
    for item in d["body"]:
        if isinstance(item,str): doc.add_paragraph(item).paragraph_format.keep_together=True
        elif item[0]=="h":
            heading=doc.add_paragraph(item[1],"Heading 1")
            if phase==3 and d["number"]==6 and item[1].startswith("3."):
                heading.paragraph_format.page_break_before=True
        elif item[0]=="t":
            t=doc.add_table(rows=0,cols=len(item[1][0])); t.style="Table Grid"
            widths=item[2] if len(item)>2 else [491/len(item[1][0])]*len(item[1][0])
            t.autofit=False
            for col,w in zip(t.columns,widths): col.width=Pt(w)
            for ri,row in enumerate(item[1]):
                cells=t.add_row().cells; t.rows[ri]._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))
                for cell,value,w in zip(cells,row,widths):
                    cell.width=Pt(w); cell.text=str(value)
                    for paragraph in cell.paragraphs:
                        padding=2 if compact_table else 4
                        paragraph.paragraph_format.space_after=Pt(padding); paragraph.paragraph_format.space_before=Pt(padding)
                        for run in paragraph.runs: run.font.size=Pt(10); run.bold=ri==0
                    if ri==0:
                        shade=OxmlElement("w:shd"); shade.set(qn("w:fill"),"E4E9E7"); cell._tc.get_or_add_tcPr().append(shade)
                if ri==0: t.rows[ri]._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))
            doc.add_paragraph()
    doc.add_paragraph("Mit freundlichen Grüßen").paragraph_format.keep_with_next=True
    doc.add_paragraph("gez. "+d["signer"]).paragraph_format.keep_with_next=True
    doc.add_paragraph("Bezug: "+c["code"]+" · Anlagen wie im Text bezeichnet.")
    footer=sec.footer.paragraphs[0]; footer.text=c["code"]+" · Seite "
    field=OxmlElement("w:fldSimple"); field.set(qn("w:instr"),"PAGE"); footer._p.append(field)
    doc.save(dest)


def make_eml(phase, d, dest):
    c=CASES[phase]; sender=c["actors"][d["sender"]]; recipient=c["actors"][d["recipient"]]
    dt=datetime.fromisoformat(d["date"]+"T10:32:00").replace(tzinfo=ZoneInfo("Europe/Berlin"))
    msg=EmailMessage(policy=policy.SMTP)
    msg["From"]=f"{sender[3]} <{sender[2]}>"; msg["To"]=f"{recipient[3]} <{recipient[2]}>"
    msg["Date"]=format_datetime(dt); msg["Subject"]=c["code"]+" / "+d["title"]
    msg["Message-ID"]=f"<{c['code'].lower()}.{d['number']}@{sender[2].split('@')[1]}>"
    msg["Content-Language"]="de-DE"
    msg.set_content("Sehr geehrte Damen und Herren,\n\n"+"\n\n".join(d["body"])+"\n\nMit freundlichen Grüßen\n"+sender[3]+"\n"+sender[0]+"\n"+sender[1]+"\n"+sender[2]+"\n", charset="utf-8")
    dest.write_bytes(msg.as_bytes())


def phase_one():
    record(1,1,"owner","plan","Beschluss zur Vorbereitung des Kulturhofs",[
        "Der Stiftungsvorstand hat am 02.02.2026 mit drei Stimmen bei einer Enthaltung beschlossen, die Umnutzung des ehemaligen Packhauses Am Buchenrain 14 vorzubereiten. Das Gebäude steht seit Ende 2024 leer. Der Kulturkreis soll Saal und Werkbereich betreiben; Eigentümerin und Auftraggeberin bleibt die Stiftung.",
        ("h","1. Verbindlicher Ausgangsrahmen"),
        "Für den Saal werden zunächst 120 Besucher auf Sitzplätzen zugrunde gelegt. Die Bestuhlung soll für Proben entfernbar sein. Im Westanbau sollen Werkangebote stattfinden. Über eine gleichzeitige Nutzung von Saal und Werkbereich hat der Vorstand noch nicht entschieden. Eine gastronomische Vollküche ist nicht vorgesehen; gewünscht sind Getränkeausgabe und eine kleine Teeküche.",
        "Als Ziel gilt die erste reguläre Veranstaltung am 01.10.2028. Das verfügbare Projektbudget beträgt 1.450.000 EUR brutto einschließlich Planung, Ausstattung und einer vorläufigen Reserve von 180.000 EUR. Der Grundstückserwerb ist nicht Teil dieses Betrags, weil das Objekt bereits der Stiftung gehört. Ein Förderantrag ist noch nicht gestellt.",
        ("h","2. Vorbereitung und Zuständigkeit"),
        "Hanna Wendt darf die Grundlagenermittlung bis zu einer Vergütung von 8.500 EUR netto beauftragen. Weitere Planungsstufen werden durch einen gesonderten Beschluss abgerufen. Für Untersuchungen stehen zunächst höchstens 12.000 EUR brutto bereit; die Auswahl der Leistungen wird nach Vorlage von Angeboten im Vorstand beraten.",
        "Der Kulturkreis übermittelt seine Nutzungsangaben bis 09.02.2026. Die Stiftung stellt den vorhandenen Altplan und Zugang zu den zugänglichen Gebäudeteilen bereit. Die Dachbodentür ist derzeit verschlossen. Eine Belastbarkeit des Dachbodens für Besucher wird nicht vorausgesetzt.",
        "Anwesend waren Hanna Wendt, Ole Reimer, Fenja Kuhl und Timo Werth. Der Beschluss wurde am Sitzungsende verlesen und von Hanna Wendt und Ole Reimer für die Niederschrift bestätigt."],"Hanna Wendt und Ole Reimer, Vorstand")
    record(1,2,"plan","owner","Vereinbarung zur Grundlagenermittlung",[
        "Zwischen der Stiftung Buchenrain Kultur, vertreten durch Hanna Wendt, und Marlene Voss Architektur wird für das Gebäude Am Buchenrain 14 in Detmold folgende Vereinbarung geschlossen. Grundlage ist der Vorstandsbeschluss vom 02.02.2026.",
        ("h","1. Gegenstand"),
        "Das Büro klärt die Aufgabenstellung für die Umnutzung auf Grundlage der Angaben der Stiftung und des Kulturkreises, führt eine Ortsbesichtigung durch, berät zum gesamten Leistungs- und Untersuchungsbedarf, formuliert Entscheidungshilfen zur Auswahl weiterer fachlich Beteiligter und fasst die Ergebnisse schriftlich zusammen. Der Auftrag bezieht sich auf die Grundlagenermittlung für das Gebäude. Die Parteien verwenden die Bezeichnung Leistungsphase 1 der Gebäudeplanung.",
        "Der bisherige Altplan wird auf erkennbare Abweichungen zu den zugänglichen Bereichen bezogen. Eine vollständige Neuvermessung, Bestandsaufnahme oder Substanzerkundung ist damit nicht vereinbart. Das Büro weist auf den nach Sichtung erkennbaren zusätzlichen Untersuchungsbedarf hin. Ein neues Raum- oder Funktionsprogramm sowie eine Wirtschaftlichkeitsuntersuchung sind nicht Gegenstand dieser Vereinbarung.",
        ("h","2. Mitwirkung und Untersuchungen"),
        "Die Stiftung stellt vorhandene Unterlagen und rechtmäßigen Zutritt bereit. Öffnungen, Probenahmen und Fachgutachten werden nur auf gesonderter Grundlage beauftragt. Die Auswahlhilfe des Büros enthält Untersuchungsfrage, angebotenen Umfang und die für die Weiterplanung bedeutsamen Grenzen. Die Beauftragung eines Fachbüros erklärt die Stiftung selbst.",
        ("h","3. Vergütung und Termine"),
        "Die Vergütung beträgt pauschal 8.500 EUR netto zuzüglich 19 Prozent Umsatzsteuer, insgesamt 10.115 EUR brutto. Vereinbart sind eine gemeinsame Besichtigung und zwei Abstimmungsgespräche. Die schriftliche Zusammenfassung soll bis 27.02.2026 vorliegen, sofern die bis 20.02.2026 angekündigten Unterlagen eingehen. Bei späterer Zuarbeit stimmen die Parteien den Abgabetermin neu ab.",
        ("h","4. Weitere Planung und Erklärungen"),
        "Weitere Leistungsphasen sind nicht abgerufen. Eine zusätzliche Untersuchung oder Programmaufstellung bedarf einer Vereinbarung über Gegenstand und Vergütung. Das Büro erhält keine Vollmacht für Grundstücksgeschäfte, Bauaufträge, Anträge oder technische Freigaben. Die Entscheidung über Nutzungsziele verbleibt bei der Stiftung.",
        "Detmold, 05.02.2026. Für die Stiftung erklärt Hanna Wendt die Annahme. Für das Büro erklärt Marlene Voss die Annahme. Beide Parteien erhalten eine gleichlautende Ausfertigung."],"Hanna Wendt, Stiftung · Marlene Voss, Architektur")
    record(1,3,"owner","plan","Beginn und Schlüssel zum Ortstermin",[
        "Bitte beginnen Sie auf Grundlage der gestern geschlossenen Vereinbarung. Für den Termin am 12.02.2026 um 09:00 Uhr kommt unser Hausmeister Benno Tesch hinzu. Er hat Schlüssel für Saal, Westanbau und Heizung. Für den Dachboden ist der Schlüssel noch nicht gefunden.",
        "Unsere Zusage umfasst vorerst die vereinbarte Grundlagenermittlung. Bitte holen Sie für nötige zusätzliche Untersuchungen Angebote ein, soweit dies mit einer bloßen Anfrage möglich ist. Eine Beauftragung dieser Untersuchungen möchte ich erst nach der Vorstandssitzung erklären.",
        "Die Zahl von 120 Sitzplätzen stammt aus unserem Beschluss. Herr Kersten wird vermutlich auch über größere Stehveranstaltungen sprechen. Das ist noch keine Erweiterung des Beschlusses. Der Altplan aus der Grundstücksmappe liegt am Termin als Papierausdruck bereit. Weitere digitale Pläne besitzen wir bislang nicht." ])
    record(1,4,"user","plan","Nutzungsangaben des Kulturkreises",[
        "Wir möchten den Kulturhof an vier Nachmittagen pro Woche für offene Werkangebote und an zwei Abenden für Musik und Lesungen nutzen. Unsere Angaben beruhen auf dem bisherigen Betrieb in gemieteten Räumen; sie sind mit den Kursleitungen, noch nicht in allen Punkten mit der Stiftung abgestimmt.",
        ("h","1. Saal und Nebenbetrieb"),
        "Für Lesungen benötigen wir 120 Sitzplätze einschließlich einer kleinen Vortragsfläche. Bei Konzerten ohne Bestuhlung rechnen wir mit bis zu 160 Besuchern. Das betrifft voraussichtlich sechs Abende im Jahr. Währenddessen läuft der Werkbetrieb üblicherweise nicht, bei unserem Sommerfest war das in der Vergangenheit jedoch anders.",
        "Der Saal soll tagsüber auch für eine Bewegungsgruppe mit 24 Personen zur Verfügung stehen. Eine feste Bühne ist nicht nötig. Tische und Stühle müssen im Haus lagern können; bisher lagern wir 90 Stühle und 18 Klapptische in einem angemieteten Container. Der Containervertrag endet am 31.12.2027.",
        ("h","2. Werkbereich und Zugang"),
        "Im Werkbereich arbeiten maximal 18 Teilnehmende und zwei Betreuende. Es werden Wasseranschlüsse, robuste Arbeitsflächen und abschließbare Materialschränke gebraucht. Brennofen, Lackierkabine und schwere Maschinen gehören nicht zum Programm. Eine Kursleitung hat einen Keramikofen vorgeschlagen; darüber gibt es noch keinen Beschluss.",
        "Menschen mit Rollstuhl oder Gehhilfe sollen Saal und Werkbereich ohne fremde Hilfe erreichen können. Der bestehende Eingang hat drei Stufen. Zur konkreten Ausführung können wir keine Maße vorgeben. Für Anlieferungen reicht nach unserer bisherigen Erfahrung ein Transporter, der etwa zweimal wöchentlich kommt.",
        ("h","3. Personal und Betrieb"),
        "Eine Betriebsleitung und zwei Teilzeitkräfte benötigen einen gemeinsamen Arbeitsplatz und einen abschließbaren Aktenbereich. Eine Teeküche mit Getränkekühlschrank genügt. Speisen werden für einzelne Veranstaltungen geliefert. Wir gehen vorläufig davon aus, dass der Dachboden als Lager genutzt werden kann, haben ihn aber selbst seit der Übergabe nicht betreten.",
        "Die Belegungsübersicht vom 10.02.2026 wird die tatsächlich durchgeführten Termine ergänzen. Unsere Wünsche sind keine Aussage darüber, welche Nutzung im ehemaligen Packhaus bisher genehmigt war." ])
    record(1,7,"plan","owner","Vermerk zum Ortstermin am Kulturhof",[
        "Am 12.02.2026 wurden von 09:00 bis 10:45 Uhr das Erdgeschoss des Packhauses, der Westanbau und der Hof begangen. Teilgenommen haben Hanna Wendt, Ruben Kersten, Benno Tesch und Marlene Voss. Es war trocken bei etwa 4 Grad Celsius; in den beiden vorherigen Tagen hatte es nach Angabe von Herrn Tesch geregnet.",
        ("h","1. Zugängliche Bereiche"),
        "Das Packhaus zeigt im Erdgeschoss die im Altplan dargestellte äußere Grundform von 24,00 mal 14,00 m. Die Maße wurden nicht neu vermessen. Die südliche Eingangstür liegt hinter drei Stufen. Der im Altplan eingezeichnete Durchgang vom Saal zum Westanbau ist zugemauert. Stattdessen besteht ein etwa 1,10 m breiter Durchgang weiter nördlich; seine lichte Breite wurde mit einem Bandmaß orientierend abgelesen.",
        "Am nördlichen Saalsockel waren dunkle Verfärbungen auf einer Länge von etwa 3,5 m sichtbar. Die Oberfläche fühlte sich an zwei Stellen kühl an. Es wurden keine Feuchtemessung und keine Probeentnahme durchgeführt. Herr Tesch berichtete, der Bereich sei seit einem Regenereignis im November 2025 auffälliger. Die Ursache wurde beim Termin nicht festgestellt.",
        ("h","2. Nicht zugängliche Teile"),
        "Die Dachbodentür blieb verschlossen. Dachtragwerk und Bodenaufbau konnten nicht von innen besichtigt werden. Durch das außen sichtbare Dachfenster war keine belastbare Zustandsbeurteilung möglich. Die frühere Nutzung als Lager ergibt sich aus dem Altplan, nicht aus einer aktuellen Tragfähigkeitsprüfung.",
        "Der Heizraum war zugänglich, die Rückseite des Kessels jedoch durch gelagerte Möbel verdeckt. Eine Anlagenprüfung fand nicht statt. Im Westanbau lag unter einer losen Fußmatte ein älterer dunkler Bodenbelag; Materialart und Klebstoff wurden nicht bestimmt.",
        ("h","3. Unterlagen und Äußerungen"),
        "Frau Wendt übergab eine Kopie des Altplans vom 16.06.1998. Herr Kersten erläuterte 120 Sitzplätze sowie gelegentliche Konzerte mit 160 Stehplätzen. Frau Wendt verwies auf den noch nicht erweiterten Vorstandsbeschluss. Der Verlauf einer vermuteten Entwässerungsleitung im Hof wurde nur von Herrn Tesch gezeigt und nicht geortet.",
        "Die Begehungsskizze B-01 vom selben Tag ordnet die besichtigten Bereiche und Beobachtungspunkte zu. Sie beruht auf dem Altplan und enthält keine neue Bestandsvermessung. Öffnungen, Prüfungen und Aufträge an Fachbüros wurden beim Termin nicht veranlasst." ])
    record(1,10,"stat","owner","Angebot F 26 041 zur orientierenden Tragwerkssichtung",[
        "Vielen Dank für die Anfrage zum ehemaligen Packhaus. Wir bieten einen Ortstermin mit einer Tragwerksplanerin und eine schriftliche Kurzstellungnahme zu den erkennbaren Lastabtragungswegen an. Grundlage sind der Altplan vom 16.06.1998 und die geplante Nutzung des Erdgeschosses mit Veranstaltungen.",
        ("h","1. Umfang"),
        "Der Termin dauert voraussichtlich einen halben Tag. Voraussetzung sind freier Zugang zum Dachboden und eine sichere, vorhandene Zugangsmöglichkeit. Wir sichten zugängliche tragende Bauteile und benennen für die weitere Planung erforderliche Bestandsinformationen. Nicht enthalten sind Bauteilöffnungen, Materialprüfungen, Aufmaß, Lastannahmen für eine neue Dachbodennutzung und eine rechnerische Bestandsstatik.",
        "Unsere Kurzstellungnahme enthält keine Freigabe des Dachbodens für Lager oder Besucher. Wenn diese Nutzung weiterverfolgt wird, legen wir nach der Sichtung ein ergänzendes Untersuchungsangebot vor. Der verschlossene Dachboden darf nicht als mitbesichtigt gelten.",
        ("h","2. Vergütung und Termin"),
        ("t",[["Leistung","Menge","Netto EUR"],["Ortstermin und Kurzstellungnahme","1 pauschal","1.850,00"],["Anfahrt","1 pauschal","120,00"],["Summe netto","","1.970,00"],["Umsatzsteuer 19 Prozent","","374,30"],["Gesamt brutto","","2.344,30"]],[285,80,126]),
        "Das Angebot gilt bis 06.03.2026. Ein Termin wäre am 04.03.2026 möglich, sofern der Zugang bis 27.02.2026 bestätigt wird. Zahlung nach Übergabe der Kurzstellungnahme innerhalb von 14 Tagen. Bisher liegt uns kein Auftrag vor." ])
    record(1,11,"lab","owner","Angebot L 26 118 zur Materialerkundung",[
        "Für die zugänglichen Boden- und Wandaufbauten des Kulturhofs bieten wir eine orientierende Materialerkundung an. Anlass sind der geplante Umbau und die bislang fehlenden Angaben zu älteren Belägen und Klebstoffen. Eine konkrete Schadstoffbelastung ist durch Ihre Anfrage nicht nachgewiesen.",
        ("h","1. Vorgehen und Leistungsumfang"),
        "Eine sachkundige Person begeht die zugänglichen Erdgeschossbereiche, legt die Probenstellen nach Materialbild fest und dokumentiert sechs Einzelproben. Der angebotene Laborumfang bezieht sich auf die im Probenplan festzulegenden Verdachtsparameter. Die Untersuchung ist keine vollständige Gebäudeschadstoffkartierung und keine Freigabe für Abbrucharbeiten.",
        "Der Dachboden, verdeckte Schichten hinter festen Einbauten und die Heizungsisolierung sind mangels Zugangs nicht enthalten. Zusätzliche Proben werden nur nach Abstimmung entnommen und mit 145 EUR netto je Probe einschließlich Labor abgerechnet. Größere Bauteilöffnungen und Wiederherstellung übernimmt ein gesondert beauftragter Betrieb.",
        ("h","2. Angebotspreis"),
        ("t",[["Bestandteil","Ansatz","Netto EUR"],["Begehung und Probenplanung","1 pauschal","1.250,00"],["Sechs Einzelproben","6 mal 145 EUR","870,00"],["Befundbericht","1 pauschal","420,00"],["Summe netto","","2.540,00"],["Umsatzsteuer 19 Prozent","","482,60"],["Gesamt brutto","","3.022,60"]],[250,115,126]),
        "Ein Ortstermin ist nach schriftlicher Beauftragung und Zustimmung der Eigentümerin zur Probenahme innerhalb von zehn Arbeitstagen möglich. Der Bericht folgt voraussichtlich sieben Arbeitstage nach Eingang der Proben im Labor. Das Angebot gilt bis 13.03.2026; eine konkrete Terminzusage erfolgt erst nach Beauftragung." ])
    record(1,13,"owner","plan","Finanzieller Rahmen des Vorhabens",[
        "Für Ihre Zusammenfassung bestätige ich den vom Vorstand am 02.02.2026 festgelegten Rahmen von 1.450.000 EUR brutto. Die Stiftung setzt hierfür 950.000 EUR eigene Mittel und eine zugesagte, zweckgebundene Spende von 500.000 EUR an. Die Spende ist nach dem Schreiben der Fördergemeinschaft vom 28.01.2026 für Kulturangebote im Erdgeschoss bestimmt; wir verwahren das Original in der Finanzakte.",
        "Der Betrag umfasst Umbau, Planung, Untersuchungen, bewegliche Ausstattung und 180.000 EUR vorläufige Reserve. Grundstückskosten fallen nicht mehr an. Der Planungsvertrag vom 05.02.2026 ist innerhalb dieses Rahmens zu berücksichtigen. Die Untersuchungsfreigabe von höchstens 12.000 EUR brutto ist keine zusätzliche Finanzierung außerhalb des Projektbudgets.",
        "Ein möglicherweise späterer Förderantrag ist weder eingereicht noch bewilligt. Wir möchten ihn derzeit nicht zur Deckung einer höheren Grundvariante ansetzen. Die Nutzung des Dachbodens ist finanziell nicht eigens beschlossen; sollte sie größere Eingriffe erfordern, muss der Vorstand darüber gesondert entscheiden.",
        "Die Tabellenübersicht vom 17.02.2026 stellt Angebote und einen internen Ansatz für Öffnungsarbeiten zusammen. Sie ist keine Bestellung an die genannten Büros. Bitte teilen Sie uns in der Zusammenfassung mit, welche Informationen für die nächste Planungsentscheidung fehlen. Eine Kostenschätzung des gesamten Umbaus liegt uns noch nicht vor." ])
    record(1,14,"user","plan","Stehkonzerte und Dachbodenlager",[
        "Ich möchte die Angaben aus unserem Schreiben vom 09.02. präzisieren: Die 160 Besucher betreffen ausschließlich unbestuhlte Konzerte. Für normale Lesungen bleiben es 120 Sitzplätze. Die sechs Konzertabende sind wirtschaftlich für uns wichtig, weil sie einen Teil der offenen Werkangebote finanzieren sollen.",
        "Herr Tesch hat mir gestern gesagt, auf dem Dachboden hätten früher schwere Papierrollen gestanden. Daraus hatte ich geschlossen, dass dort unsere Stühle lagern könnten. Einen Nachweis oder ein Foto davon habe ich nicht. Falls das nicht ohne Weiteres geht, benötigen wir im Erdgeschoss etwa 25 m² Lagerfläche. In der ursprünglichen Flächenvorstellung waren nur 12 m² für Lager enthalten.",
        "Frau Wendt ist über den Wunsch informiert. Eine schriftliche Zustimmung zu 160 Besuchern oder zur zusätzlichen Lagerfläche habe ich nicht. Den vorgeschlagenen Keramikofen möchte ich vorerst zurückstellen; wir haben weder ein Gerät noch eine abgestimmte Betriebsbeschreibung." ])
    record(1,15,"owner","plan","Unterlagen aus der Grundstücksmappe",[
        "Ich habe die übernommene Grundstücksmappe und die Unterlagen des früheren Betriebs nochmals durchgesehen. Außer dem bereits übergebenen Plan vom 16.06.1998 liegen uns keine Statik, keine aktuelle Vermessung und keine vollständige Genehmigungsakte vor. Der Plan trägt die Überschrift Packhausbestand, aber keinen mir zuordenbaren Genehmigungsvermerk.",
        "In einer Rechnung von 2011 wird eine Türöffnung im Westanbau erwähnt. Die dazugehörige Zeichnung fehlt. Herr Tesch erinnert sich an eine Verlegung des Durchgangs, konnte das Datum aber nicht sicher nennen. Ich kann deshalb nicht bestätigen, dass der Altplan den heutigen Zustand vollständig abbildet.",
        "Ein Schlüssel für den Dachboden wurde inzwischen gefunden. Der Zugang wäre ab 02.03.2026 nach Abstimmung mit Herrn Tesch möglich. Damit ist noch keine Untersuchung beauftragt. Bitte führen Sie den bisher nicht besichtigten Dachboden in Ihrer Zusammenfassung weiterhin entsprechend, bis ein Termin tatsächlich stattgefunden hat." ])
    record(1,16,"owner","plan","Auszug aus der Vorstandssitzung vom 23 Februar",[
        "Der Vorstand hat am 23.02.2026 die ergänzenden Nutzerangaben und die Angebote F 26 041 und L 26 118 besprochen. Hanna Wendt, Ole Reimer und Fenja Kuhl waren anwesend. Timo Werth war entschuldigt. Die Beratung endete um 18:40 Uhr.",
        ("h","1. Nutzungsstand"),
        "Für die weitere Grundlagenermittlung bleiben 120 Sitzplätze die bestätigte Basis. Die Konzertnutzung mit 160 Stehplätzen wird als zusätzliche Möglichkeit offengehalten, ist aber nicht beschlossen. Der Werkbetrieb soll im Regelfall nicht gleichzeitig mit einer voll belegten Saalveranstaltung laufen. Für das Sommerfest fehlt noch eine belastbare Ablaufbeschreibung.",
        "Die Lagerung auf dem Dachboden soll nicht ohne weitere Erkenntnisse vorausgesetzt werden. Die zusätzliche Erdgeschosslagerfläche von 25 m² ist als Nutzerwunsch aufzunehmen. Der Vorstand hat noch nicht entschieden, welche andere Nutzung dafür gegebenenfalls verkleinert werden könnte.",
        ("h","2. Angebote"),
        "Der Vorstand bittet um Erläuterung, welche Entscheidung die orientierende Tragwerkssichtung ermöglicht und welche Nachweise danach noch erforderlich sein könnten. Beim Materiallabor soll geklärt werden, ob die sechs Proben für die beim Ortstermin gesehenen unterschiedlichen Beläge vorgesehen sind. Die Preisgrenze von 12.000 EUR brutto bleibt bestehen.",
        "Eine Beauftragung der beiden Angebote wurde in dieser Sitzung nicht erklärt. Hanna Wendt wird die Entscheidung nach Eingang der angeforderten Erläuterung schriftlich mitteilen. Eine Freigabe zur Bauteilöffnung oder zur Nutzung des Dachbodens wurde ebenfalls nicht erteilt.",
        "Die Zusammenfassung der Grundlagenermittlung soll den erreichten Stand wiedergeben. Der Vorstand erwartet noch keine Vorplanungszeichnung und keine Kostenschätzung des vollständigen Umbaus. Über den Abruf der nächsten Phase wird gesondert beraten." ],"Hanna Wendt, Sitzungsleitung · Fenja Kuhl, Niederschrift")


def phase_two():
    record(2,1,"owner","plan","Abruf der Vorplanung für die Kita Wiesenbogen",[
        "Auf Grundlage unseres Rahmenvertrags vom 12.01.2026 rufen wir die Vorplanung für das Gebäude der Kita Wiesenbogen ab. Der Standort Wiesenbogen 6 in Bad Pyrmont bleibt gesetzt. Auftraggeberin ist die Wiesenbogen Bildung gGmbH; die Einrichtung wird durch unsere eigene Betriebsgesellschaft geführt.",
        ("h","1. Aufgabe und Ergebnisse"),
        "Zu untersuchen sind eine eingeschossige Lösung V1 und eine kompakte zweigeschossige Lösung V2 mit jeweils drei Gruppen und insgesamt 75 Plätzen für Kinder ab drei Jahren. Grundlage sind die abgestimmten Nutzerangaben vom 04.03.2026, soweit diese den hier genannten Umfang nicht erweitern. Vorzulegen sind gezeichnete Varianten, eine Erläuterung der funktionalen Unterschiede, Kostenschätzung und ein Terminplan mit wesentlichen Vorgängen.",
        "Beide Varianten sollen dieselbe Ausgabeküchenleistung für täglich bis zu 75 Mahlzeiten ermöglichen. Ob vorhandene Ausstattung übernommen werden kann, klärt die Betreiberin. Ein Neubau einer Produktionsküche und eine vierte Gruppe sind nicht bestellt. Der Außenbereich ist mit seiner Schnittstelle zu den Zugängen zu berücksichtigen; eine vollständige Freianlagenplanung ist nicht Gegenstand dieses Gebäudeabrufs.",
        ("h","2. Vergütung und Grenzen"),
        "Für den beschriebenen Vorplanungsumfang sind 24.000 EUR netto zuzüglich 19 Prozent Umsatzsteuer vereinbart. Die Beiträge von Tragwerks- und Technikplanung werden durch uns gesondert beauftragt und dem Büro zur Koordination bereitgestellt. Eine förmliche Bauvoranfrage, Fördermittelbeschaffung und Wirtschaftlichkeitsberechnung sind nicht abgerufen. Gespräche über die Genehmigungsfähigkeit sollen dokumentiert werden.",
        ("h","3. Finanzrahmen und Entscheidung"),
        "Der derzeitige Finanzrahmen beträgt 3.200.000 EUR brutto einschließlich 200.000 EUR Reserve, Ausstattung und Planung. Grundstückskosten sind nicht enthalten, weil das Grundstück bereits erworben ist. Der Ansatz für Gebühren ist noch festzulegen und darf nicht als zusätzlich gesicherte Finanzierung gelten. Die Variantenentscheidung soll nach Beratung am 27.03.2026 schriftlich erklärt werden.",
        "Die Geschäftsführung entscheidet über die Weiterbearbeitung. Eine fachliche Zustimmung eines Beteiligten ersetzt diesen Beschluss nicht. Der Abruf berechtigt nicht zur Vergabe von Bauleistungen oder zur Einreichung eines förmlichen Antrags. Levin Sander hat den Abruf am 03.03.2026 per E-Mail bestätigt." ])
    record(2,2,"user","plan","Betriebsangaben für drei Kindergartengruppen",[
        "Für die Vorplanung bestätige ich nach unserer Besprechung mit Frau Lammers drei Gruppen mit jeweils 25 Kindern ab drei Jahren. Die Öffnungszeit soll montags bis freitags von 07:00 bis 16:30 Uhr sein. Wir rechnen mit 75 ausgegebenen Mittagessen und einer zeitversetzten Nutzung des gemeinsamen Mehrzweckraums.",
        ("h","1. Räumliche Angaben"),
        ("t",[["Nutzung","Anzahl","Gewünschte nutzbare Fläche"],["Gruppenraum","3","je 60 m²"],["Gruppennebenraum","3","je 20 m²"],["Mehrzweckraum","1","60 m²"],["Ausgabeküche mit Lager","1","40 m²"],["Leitung und Besprechung","2","zusammen 32 m²"],["Personalraum","1","24 m²"],["Sanitär und Pflege","3 Bereiche","zusammen 54 m²"],["Material und Reinigung","mehrere","zusammen 30 m²"]],[240,80,171]),
        "Die Angaben sind betriebliche Wünsche aus unserer jetzigen Einrichtung. Verkehrs-, Konstruktions- und Technikflächen sind darin nicht enthalten. Die Tabelle ist keine Flächenvorgabe einer Behörde und keine technische Normprüfung.",
        ("h","2. Wege und Außenraum"),
        "Jede Gruppe soll einen gut auffindbaren Weg zum Außenspielbereich erhalten. Bei der zweigeschossigen Variante möchten wir wissen, wie Kinder und Personal den Wechsel zwischen Obergeschoss und Garten organisieren können. Ein Aufzug ersetzt in unserem Betrieb nicht die Aufsicht auf den Wegen. Die Essensanlieferung soll möglichst nicht durch die Garderobe laufen.",
        "Für Fahrräder und Kinderwagen benötigen wir einen überdachten Bereich nahe dem Eingang. Eltern sollen das Gelände zu Fuß von Süden erreichen. Auf dem östlichen Nachbargrundstück liegen Wohnräume; ein Anlieferpunkt unmittelbar an dieser Grenze ist deshalb für uns nicht die erste Wahl.",
        ("h","3. Ausstattung"),
        "Wir prüfen noch, ob die Küchengeräte aus der bisherigen Einrichtung übernommen werden dürfen. Sie gehören nicht unserer Betriebsgesellschaft, sondern dem bisherigen Vermieter. Eine Zusage liegt nicht vor. Die geplante Küche soll angelieferte Speisen annehmen, warmhalten und ausgeben; eigenes Kochen ist nicht vorgesehen." ])
    record(2,6,"plan","owner","Erläuterung der Vorplanungsstände V1 und V2",[
        "Die Pläne V1-01 und V2-01 vom 12.03.2026 zeigen zwei Gebäudeorganisationen für dasselbe dreigruppige Programm. Beide Varianten haben in der äußeren Flächenbetrachtung 864 m² Bruttogrundfläche. Die Raumzonen der Zeichnungen enthalten konstruktive und verteilende Anteile; sie sind nicht mit den gewünschten nutzbaren Raumflächen gleichzusetzen.",
        ("h","1. Eingeschossige Variante V1"),
        "V1 hat einen Baukörper von 36,00 mal 24,00 m. Die drei Gruppen liegen nebeneinander an der Nordseite. Der gemeinsame Flur trennt diese Zone von Mehrzweckraum, Verwaltung, Küche und Nebenbereichen im Süden. Die Gruppen können den nördlichen Garten ohne Geschosswechsel erreichen. Der Hauptzugang liegt südlich, die Küchenanlieferung ist zunächst an der Südostecke vorgesehen.",
        "Die große Grundfläche beansprucht mehr zusammenhängende Grundstücksfläche. Die verbleibenden Außenräume liegen überwiegend nördlich und westlich. Der Anschluss an den westlichen Geländesprung ist noch mit der Außenplanung zu besprechen. Im Flächenansatz sind 1.500 m² bearbeitete Außenfläche vorgesehen, nicht die gesamte Grundstücksfläche.",
        ("h","2. Zweigeschossige Variante V2"),
        "V2 hat je Geschoss 24,00 mal 18,00 m. Zwei Gruppen liegen im Erdgeschoss und eine Gruppe im Obergeschoss. Der Aufzug und die Haupttreppe liegen an der Südseite. Ein zweiter Treppenbereich ist im Nordosten als räumlicher Ansatz dargestellt; dessen Ausbildung ist fachlich noch nicht abgestimmt. Das Obergeschoss enthält außerdem Personal- und Mehrzweckbereiche.",
        "Die kleinere Gebäudegrundfläche lässt einen größeren zusammenhängenden Garten zu. Dafür entstehen Geschosswechsel im täglichen Betrieb. Die gemeinsame Küchenfläche liegt im Erdgeschoss. Ob Geräte aus dem Altstandort übernommen werden können, wird durch die Betreiberin geprüft; eine Bestätigung liegt noch nicht vor.",
        ("h","3. Weitere Beiträge"),
        "Die Fachbüros haben diese Geometrien erhalten. Technikbeitrag und Tragwerkskonzept stehen noch aus; eine Bemessung ist damit nicht verbunden. Das Vorgespräch zur Genehmigungsfähigkeit ist für den 18.03. vorgesehen. Eine förmliche Voranfrage wurde nicht gestellt. Die Kostenschätzung soll auf dem Preisstand März 2026 folgen." ])
    record(2,7,"tga","plan","Technikansätze zu V1 und V2",[
        "Für die beiden Vorplanungsgeometrien vom 12.03.2026 haben wir die Flächenansätze gesichtet. Für V1 setzen wir für die allgemeinen technischen Anlagen vorläufig 480 EUR netto je m² BGF an, für V2 520 EUR netto je m² BGF. Die Ansätze beziehen sich jeweils auf 864 m² und enthalten Heizung, Sanitär, Lüftung und Elektro als frühe Gesamtannahme.",
        "Die unterschiedlichen Ansätze berücksichtigen bei V2 zusätzliche vertikale Verteilung und die zweite Ebene. Ein Aufzug ist darin nicht enthalten; hierfür verwenden wir einen gesonderten Ansatz von 45.000 EUR netto. Die Ausgabeküche ist in beiden allgemeinen Technikansätzen nicht enthalten. Bitte die Küchengeräte nicht zugleich in unserem Ansatz und in der Ausstattung addieren.",
        "Für die Technikfläche sind in V1 und V2 zunächst jeweils 28 m² nutzbare Fläche vorgesehen. Die Aufstellung der Außeneinheit und eine gegebenenfalls erforderliche Schallbetrachtung sind noch offen. Die östliche Nachbargrenze sollte nicht ohne weitere Abstimmung als Aufstellort festgelegt werden.",
        "Dies ist ein Vorplanungsbeitrag, keine Berechnung der Anlagenleistung. Die angenommene Nutzungszeit und 75 Mahlzeiten täglich stammen aus dem Betreiberprogramm. Bei Änderung der Gruppenzahl oder einer Produktionsküche müssen wir die Ansätze neu betrachten. Eine Geräteübernahme aus der alten Einrichtung haben wir nicht geprüft." ])
    record(2,8,"stat","plan","Tragwerkskonzept der Vorplanungsvarianten",[
        "Wir haben die Vorplanungszeichnungen V1-01 und V2-01 vom 12.03.2026 hinsichtlich eines möglichen Tragwerksrasters gesichtet. Die nachfolgenden Angaben sind ein Konzeptbeitrag für die Variantenuntersuchung, keine statische Berechnung und keine Freigabe von Bauteilen.",
        ("h","1. V1"),
        "Für den eingeschossigen Baukörper kann ein wiederkehrendes Raster von etwa 6,00 m vorgesehen werden. Die größere Spannweite des Mehrzweckbereichs ist gesondert zu bearbeiten. Der flache Dachaufbau wird zunächst mit einer Holzkonstruktion angenommen. Die in der Zeichnung dargestellten Raumtrennungen sind nicht sämtlich tragend.",
        ("h","2. V2"),
        "Für den zweigeschossigen Baukörper sind tragende Linien über beide Ebenen abzustimmen. Der Küchen- und Ausgabebereich im Erdgeschoss liegt unter dem Personal- und Besprechungsbereich. Die offenen Arbeitsbereiche und Raumtrennungen sind mit den tragenden Linien abzugleichen; eine zusätzliche Abfangung kann erforderlich werden. Im derzeitigen Baukostenkennwert ist ein üblicher Ansatz enthalten, jedoch keine detaillierte Mengenermittlung.",
        "Die Schacht- und Treppenbereiche müssen in beiden Ebenen übereinanderliegen. Der zweite Treppenbereich im Nordosten ist räumlich vorgesehen, seine bauliche Ausbildung jedoch noch nicht abgestimmt. Die Darstellung ist kein Nachweis einer Rettungswegführung. Bitte vor einer Festlegung den Brandschutzbeitrag einbeziehen.",
        ("h","3. Baugrund"),
        "Uns liegt kein Baugrundbericht vor. Gründung und Umgang mit dem Geländesprung im Westen sind deshalb nur vorläufig berücksichtigt. Wir empfehlen, die für die Gründungsentscheidung erforderlichen Angaben rechtzeitig bereitzustellen. Eine Bodenverbesserung ist in diesem Schreiben weder bemessen noch bepreist. Beide Varianten sind unter demselben derzeitigen Erkenntnisstand zu vergleichen." ])
    record(2,9,"plan","owner","Vermerk zum Vorgespräch über die Kita Planung",[
        "Am 18.03.2026 von 10:00 bis 10:35 Uhr führte Levin Sander ein telefonisches Vorgespräch mit der für das Grundstück angesprochenen Bauaufsicht. Frau Edda Lammers nahm ab 10:10 Uhr teil. Besprochen wurden die als V1-01 und V2-01 bezeichneten Vorplanungsstände vom 12.03.2026. Dieser Vermerk gibt die Notizen des Planungsbüros wieder.",
        "Die Ansprechperson hielt eine Prüfung beider Baukörper grundsätzlich für möglich. Sie verwies auf die noch zu klärende Erschließung, den Geländeverlauf und die Abstimmung der besonderen Nutzung. Für eine belastbare Aussage sollten Lage, Höhen und Zufahrt in geeigneten Unterlagen dargestellt werden. Eine abschließende Aussage zur Zweigeschossigkeit wurde nicht getroffen.",
        "Zum östlichen Lieferzugang wurde auf die angrenzende Wohnnutzung hingewiesen. Eine konkrete immissionsrechtliche Bewertung war nicht Gegenstand des Gesprächs. Das Büro sagte zu, zunächst mit der Betreiberin die Lieferzeiten und die Möglichkeit eines südlichen Zugangs zu besprechen.",
        "Eine förmliche Bauvoranfrage wurde weder vorbereitet noch eingereicht. Es wurde kein Vorbescheid erteilt und keine Genehmigung zugesagt. Der Gesprächsstand soll der Variantenberatung dienen. Für ein förmliches Verfahren wären gesonderte Unterlagen und ein entsprechender Auftrag erforderlich.",
        "Frau Lammers bat darum, beide Varianten bis zur Sitzung am 27.03. weiter gegenüberzustellen. Die mündliche Äußerung zum grundsätzlich möglichen Prüfweg soll nicht als Freigabe in einer Investitionsvorlage bezeichnet werden. Weitere Gesprächsunterlagen wurden nicht übergeben." ])
    record(2,12,"kitchen","owner","Angebot KR 260320 Ausgabeküche",[
        "Auf Ihre Anfrage bieten wir die Ausstattung einer Ausgabeküche für angelieferte Speisen und bis zu 75 Mahlzeiten täglich an. Grundlage ist die im Betreiberprogramm vom 04.03.2026 genannte Betriebsweise. Eine Produktionsküche mit Kochlinie ist nicht enthalten.",
        ("t",[["Bestandteil","Netto EUR"],["Kühlung und Warenannahme","8.400,00"],["Warmhaltung und Ausgabe","11.600,00"],["Spültechnik","9.800,00"],["Edelstahlmöbel und Arbeitstische","10.200,00"],["Montage und Einweisung","8.000,00"],["Summe netto","48.000,00"],["Umsatzsteuer 19 Prozent","9.120,00"],["Gesamt brutto","57.120,00"]],[350,141]),
        "Bauseitige Elektro-, Wasser- und Abwasseranschlüsse sowie raumlufttechnische Einrichtungen sind nicht Bestandteil dieses Geräteangebots. Ihre Fachplanung erhält nach Beauftragung die gerätebezogenen Anschlusswerte. Der Raum muss vor Montage fertiggestellt und zugänglich sein.",
        "Die angebotene Geräteleistung ist für V1 und V2 gleich. Transportwege und Einbringung sind anhand der späteren Planung zu bestätigen. Die Lieferung erfolgt nach endgültiger technischer Abstimmung voraussichtlich innerhalb von 14 Wochen. Das Angebot gilt bis 30.04.2026.",
        "Gebrauchtgeräte aus der bisherigen Einrichtung wurden von uns nicht besichtigt und sind nicht Gegenstand des Angebots. Eine Verrechnung oder Übernahme ist nicht vereinbart. Ein Auftrag liegt uns noch nicht vor." ])
    record(2,14,"user","owner","Keine Küchenübernahme aus dem Altstandort",[
        "Der Vermieter hat uns heute schriftlich mitgeteilt, dass sämtliche fest eingebauten Küchengeräte am bisherigen Standort verbleiben. Wir können daher weder Kühlung noch Spültechnik übernehmen. Meine telefonische Vermutung vom 18.03. hat sich nicht bestätigt.",
        "Die Ausgabeküchenleistung brauchen wir in beiden Varianten. Das Angebot KR 260320 über 48.000 EUR netto beschreibt den von uns besprochenen Geräteumfang. Die Anschlüsse müssen nach der Angebotsbeschreibung zusätzlich in der Haustechnik abgestimmt werden. Eine Produktionsküche wünschen wir weiterhin nicht.",
        "Bei V2 sehen wir außerdem die tägliche Bewegung der oberen Gruppe zum Garten noch nicht gelöst. Die dargestellte Treppe muss betrieblich mit zwei gleichzeitig anwesenden Betreuungspersonen nutzbar organisiert werden. Eine zusätzliche Personalstelle ist im laufenden Budget nicht eingeplant.",
        "Bitte lassen Sie diese Angaben in die Beratung am 27.03. einfließen. Ich habe damit keine Variante ausgewählt und keine Bestellung bei Küchenbau Rieken ausgelöst." ])
    record(2,15,"owner","plan","Beratungsstand des Finanzausschusses",[
        "Der Finanzausschuss hat am 24.03.2026 die Kostenschätzung vom 19.03. zur Kenntnis genommen. Der Gesamtfinanzrahmen von 3.200.000 EUR brutto bleibt unverändert. Darin sollen die vorgesehene Reserve und die noch zu bestimmenden Gebühren Platz finden. Eine zusätzliche Finanzierung wurde nicht beschlossen.",
        "Die ursprünglich notierte Geräteübernahme bei V2 ist nach der Betreiberantwort vom 23.03. nicht möglich. Der Ausschuss hat das Küchenangebot noch nicht in einer neuen Kostentabelle vorliegen. Er bittet um Erläuterung, ob die vorhandenen Ansätze dieselbe Küchenleistung und dieselben Anschlussleistungen enthalten.",
        "Für die Entscheidung sind uns neben den Investitionskosten die tägliche Betriebsorganisation und die verbleibende Gartenfläche wichtig. Es wurde keine Punktegewichtung beschlossen. Die Geschäftsführung möchte keine Variante allein anhand des bislang niedrigeren Tabellenbetrags auswählen.",
        "Die Sitzung am 27.03. bleibt vorgesehen. Bis dahin wird kein Bauauftrag und kein förmlicher Antrag ausgelöst. Die Geschäftsführung hat beide Vorplanungsstände lediglich zur Beratung entgegengenommen; eine Freigabe zur Entwurfsplanung liegt noch nicht vor.",
        "Teilgenommen haben Edda Lammers, Arvid Mollen und Daria Wessel. Der vorliegende Vermerk wurde am 24.03. um 17:20 Uhr durch Edda Lammers bestätigt." ])
    record(2,16,"neighbor","owner","Anlieferung an der östlichen Grundstücksgrenze",[
        "Vielen Dank für die Vorstellung der beiden Skizzen am vergangenen Freitag. Mein Schlafzimmer liegt zur Grenze mit Ihrem Grundstück. Auf der eingeschossigen Skizze war die Anlieferung nahe dieser Grenze eingezeichnet. Ich möchte wissen, zu welchen Uhrzeiten dort Fahrzeuge fahren und ob Kühlaggregate laufen sollen.",
        "Gegen eine Kita auf dem Grundstück habe ich mich in dem Gespräch nicht grundsätzlich ausgesprochen. Ich habe aber auch keiner konkreten Zufahrt oder Aufstellung technischer Geräte zugestimmt. Bitte halten Sie diese beiden Punkte auseinander.",
        "Eine südliche Anlieferung erscheint mir weniger störend. Ob dies mit Ihrem Betrieb möglich ist, kann ich nicht beurteilen. Bitte informieren Sie mich vor einer endgültigen Festlegung über den vorgesehenen Verlauf. Eine Vereinbarung über die Nutzung meines Grundstücks besteht nicht." ])


def phase_three():
    record(3,1,"owner","plan","Abruf der Entwurfsplanung Ärztehaus",[
        "Wir rufen auf Grundlage des Planungsvertrags vom 15.01.2026 die Entwurfsplanung für das Ärztehaus Am Mühlenanger 9 in Stadthagen ab. Die Vorplanung sieht einen zweigeschossigen Baukörper von 30,00 mal 18,00 m und 1.080 m² Bruttogrundfläche vor. Die schriftliche Bestätigung der Nutzungszuordnung folgt mit dem Protokoll vom 10.04.2026.",
        ("h","1. Beauftragtes Ergebnis"),
        "Zu erstellen sind der Gebäudeentwurf mit Grundrissen, Schnitten und Ansichten, die Objektbeschreibung, die Integration der gesondert beauftragten Fachbeiträge sowie die Kostenberechnung mit Vergleich zur Kostenschätzung vom 01.04.2026. Der Terminplan ist anhand des abgestimmten Entwurfsstands fortzuschreiben. Gespräche zur Genehmigungsfähigkeit sind mit Bezug auf die besprochenen Unterlagen zu dokumentieren.",
        "Die Objektplanung koordiniert die Beiträge von Technikplanung Rötte und Ingenieurbüro Rabe Tragwerk. Die Fachbüros bleiben für ihre Berechnungen und fachlichen Bestätigungen verantwortlich. Ein Prüfauftrag an Prüfsachverständige wird durch diesen Abruf nicht ersetzt.",
        ("h","2. Vereinbarte Rahmenbedingungen"),
        "Der Finanzrahmen beträgt 3.800.000 EUR brutto einschließlich 200.000 EUR Reserve, beweglicher Ausstattung und Planung. Grundstückskosten sind ausgeschlossen. Die gesondert anfallenden öffentlich-rechtlichen Gebühren sind innerhalb des Finanzrahmens zu decken, aber noch nicht beziffert. Ziel ist ein Betriebsbeginn am 01.10.2027.",
        "Die Vergütung für den abgerufenen Umfang beträgt nach unserer Pauschalvereinbarung 61.000 EUR netto zuzüglich 19 Prozent Umsatzsteuer. Vertiefte Wirtschaftlichkeitsuntersuchungen, eine neue Variantenoptimierung mit geändertem Betreiberprogramm und die Genehmigungsplanung sind nicht zusätzlich abgerufen.",
        ("h","3. Entscheidungen"),
        "Theda Mertin bündelt die Nutzerentscheidungen. Eine technische Abstimmungsnotiz eines Fachbüros ist keine Bauherrenentscheidung über zusätzliche Fläche oder Kosten. Die Unterlagen sollen am 12.06.2026 zur Entscheidung vorliegen. Falls bis dahin entscheidende Fachbeiträge fehlen, ist der konkret erreichte Stand mit den fehlenden Angaben vorzulegen. Bauleistungen dürfen nicht beauftragt werden." ])
    record(3,2,"owner","plan","Bestätigung der Vorplanungsbasis",[
        "In der Besprechung vom 10.04.2026 haben Theda Mertin, Dr. Enno Felder und Janne Heller den Vorplanungsstand VP-02 vom 01.04.2026 als Grundlage der Entwurfsplanung bestätigt. Der Baukörper bleibt zweigeschossig mit 30,00 mal 18,00 m Außenmaß. Die südliche Seite nimmt den Haupteingang auf.",
        ("h","1. Nutzungen"),
        "Im Erdgeschoss sind allgemeinmedizinische Sprech- und Behandlungsräume, ein diagnostischer Bereich ohne festgelegte strahlende Geräte, Anmeldung und Wartebereiche vorgesehen. Im Obergeschoss sollen weitere Sprechzimmer, Therapie- und Personalräume liegen. Es ist kein ambulanter Operationsbereich beschlossen. Eine besondere Reinraum- oder Sterilgutversorgung ist nicht Teil der bestätigten Basis.",
        "Ein gemeinsamer Aufzug verbindet die beiden Ebenen. Die Betreiber legen Wert auf kurze Wege zwischen Anmeldung, Diagnostik und Behandlungsräumen. Die endgültige Zuordnung einzelner Nebenräume wird mit den Fachbeiträgen abgestimmt. Eine Verringerung der bestätigten Behandlungsraumzahl bedarf der Zustimmung der Eigentümerin nach Rücksprache mit der Praxisgemeinschaft.",
        ("h","2. Kosten und Ausstattung"),
        "Die Kostenschätzung vom 01.04.2026 beträgt 2.780.000 EUR netto vor Umsatzsteuer und Reserve. Darin sind 150.000 EUR netto für lose Ausstattung enthalten. Medizinische Sondergeräte sind nicht als allgemeine Gebäudeausstattung erfasst. Das vereinbarte Gesamtbudget von 3.800.000 EUR brutto wird nicht erhöht.",
        "Die Fachplanung soll die zentralen Technikflächen und vertikalen Verteilungen im Entwurf konkretisieren. Die Vorplanung zeigt hierzu noch schematische Bereiche. Die Bestätigung des Vorplanungsstands ist keine Zustimmung zu beliebigen späteren Schachtgrößen oder zur Änderung tragender Bauteile.",
        ("h","3. Weiterer Ablauf"),
        "Die Fachbeiträge sollen bis Ende Mai vorliegen. Die Entscheidung über den abgestimmten Entwurf war für den 12.06.2026 vorgesehen. Ein Folgeabruf für Genehmigungsplanung oder Ausführungsplanung wurde in dieser Besprechung nicht erklärt. Das Protokoll wurde den Teilnehmenden am 10.04.2026 übersandt und von Frau Mertin am selben Tag bestätigt." ])
    record(3,6,"plan","owner","Objektbeschreibung zum Entwurfsstand E 03",[
        "Der Entwurfsstand E-03 vom 01.06.2026 entwickelt die bestätigte Vorplanung für das Ärztehaus Am Mühlenanger weiter. Das Gebäude hat zwei oberirdische Geschosse mit jeweils 540 m² Bruttogrundfläche. Die nachfolgenden Angaben beziehen sich auf die Zeichnungen E-03-EG, E-03-OG und E-03-S vom 01.06.2026.",
        ("h","1. Nutzung und Erschließung"),
        "Der Haupteingang liegt an der Südseite. Anmeldung und Wartebereich sind im Erdgeschoss nahe dem Eingang angeordnet. Ein zentraler Flur erschließt die nördlichen Behandlungs- und Diagnostikzonen. Treppe und Aufzug bilden einen gemeinsamen Kern. Das Obergeschoss enthält zusätzliche Sprechzimmer, Therapie-, Besprechungs- und Personalbereiche.",
        "Die Raumzonen werden in einer gesonderten Raumliste zusammengestellt. Die Rasterflächen der Zeichnung enthalten Wand- und Verteilanteile; sie ersetzen keine abschließende Nutzflächenberechnung. Die Zahl und Zuordnung der Behandlungsräume entsprechen dem bestätigten Betreiberstand vom 10.04.2026. Ein Operationsbereich ist nicht vorgesehen.",
        ("h","2. Konstruktion und Hülle"),
        "Vorgesehen ist ein regelmäßiges Tragwerksraster mit Stahlbetondecken und tragenden Linien nach dem Konzept T-02. Die Fassade erhält gedämmte geschlossene Flächen und Fensterbänder entsprechend den Ansichten. Das Dach ist als flach geneigter, gedämmter Dachaufbau vorgesehen. Im Kostenansatz werden 540 m² Dachfläche und 720 m² geschlossene Fassadenfläche geführt.",
        "Die Geschosshöhe beträgt im Entwurf 3,60 m; die Oberkante der Attika liegt bei 7,80 m über dem Bezugspunkt des Erdgeschosses. Die zeichnerische Darstellung ist ein Entwurfsstand und enthält keine ausführungsreifen Anschlussdetails. Baugrund- und Gründungsangaben sind durch die hierfür beauftragten Fachleute zu bestätigen.",
        ("h","3. Technische Konzeption"),
        "Heizung, Lüftung, Sanitär und Elektro werden durch Technikplanung Rötte bearbeitet. Der Entwurf hält einen zentralen Technikbereich und einen vertikalen Schacht vor. Die eingezeichnete Schachtgeometrie ist ein vorläufiger Ansatz; die schriftliche Fachbestätigung steht aus. Der Schacht ist noch nicht abschließend in das Tragwerkskonzept integriert.",
        "Die technischen Anlagen und der Aufzug werden als gesonderte Ansätze in der Kostenberechnung geführt. Die Eignung für besondere medizinische Nutzungen wird durch diese Objektbeschreibung nicht bestätigt. Änderungen an der Nutzung müssen mit Betreiber, Bauherr und Fachplanung abgestimmt werden.",
        ("h","4. Unterlagenstand"),
        "Eine abschließende Genehmigungsentscheidung liegt nicht vor. Die Kostenberechnung wird nach Eingang der Fachansätze fortgeschrieben. Die vorliegende Beschreibung enthält keine Freigabe zur Ausführung. Offene Punkte aus der Fachkoordination werden unter der Kennung K-07 im Besprechungsstand weitergeführt." ])
    record(3,8,"stat","plan","Tragwerksnotiz T 02 zum Schachtbereich",[
        "Wir haben den am 03.06.2026 erhaltenen TGA-Ausschnitt L-04 mit unserem Tragwerkskonzept T-02 verglichen. Beide Unterlagen beziehen sich auf die Decke über dem Erdgeschoss. Der in L-04 mit 1,80 mal 2,00 m dargestellte Schacht liegt zwischen den Gebäudeachsen 3 und 4 und schneidet in der dargestellten Lage die vorgesehene Unterzugslinie bei y = 11,20 m.",
        ("h","1. Gegenwärtiger Stand"),
        "Im Konzept T-02 verläuft diese tragende Linie von x = 6,00 bis x = 24,00 m. Die Schachtöffnung aus L-04 liegt von x = 12,20 bis 14,00 m und von y = 10,20 bis 12,20 m. Eine Öffnung in dieser Größe ist in unserer bisherigen Vorbemessung nicht berücksichtigt. Die Darstellung im Objektgrundriss E-03 ist deshalb nicht als von uns bestätigte Durchdringung zu verwenden.",
        "Die Entwurfsgrundlage enthielt zuvor nur einen schematischen Technikbereich. Ob der Schacht verschoben, aufgeteilt oder das Tragwerk geändert werden kann, erfordert eine gemeinsame Abstimmung. Eine Verlegung nach Süden kann den Flur oder den gemeinsamen Kern berühren; eine Änderung des Unterzugs hat andere Folgen. Wir geben mit diesem Schreiben keine dieser Lösungen frei.",
        ("h","2. Benötigte Angaben"),
        "Für die weitere Bearbeitung benötigen wir den verbindlichen lichten Schachtquerschnitt, erforderliche Abstände und die zulässigen Leitungsumlenkungen aus der Technikplanung. Die Objektplanung soll die betroffenen Raum- und Verkehrsflächen kennzeichnen. Anschließend können wir die statisch zu untersuchende Geometrie festlegen.",
        "Der bisherige Kostenansatz für Tragwerk und Decken enthält keine zusätzlich bemessene Abfangung für K-07. Eine Mehrkostenzahl können wir vor dieser Abstimmung nicht bestätigen. Der Termin für einen überarbeiteten Beitrag hängt vom Eingang der abgestimmten Geometrie ab. Unsere übrigen Konzeptangaben bleiben unverändert als Vorbemessungsstand bestehen." ])
    record(3,9,"tga","plan","Technischer Beitrag und Kostenansatz L 04",[
        "Für den aktuellen Entwurf bestätigen wir den in unserem Ausschnitt L-04 dargestellten Platzbedarf des zentralen Installationsschachts von 1,80 mal 2,00 m als derzeitigen Koordinationsansatz. Darin sind die vorgesehenen vertikalen Leitungsführungen und ein zugänglicher Revisionsbereich berücksichtigt. Die Lage ist mit dem Tragwerk noch nicht abgestimmt.",
        ("h","1. Anlagenkonzept"),
        "Der Technikraum im südöstlichen Erdgeschossbereich bleibt vorgesehen. Die Verteilung erfolgt über den zentralen Schacht in das Obergeschoss. Eine Aufteilung in zwei kleinere Schächte könnte zusätzliche horizontale Verteilung erfordern. Wir haben diese Alternative noch nicht bemessen und nicht bepreist.",
        "Die Ansätze beziehen sich auf die allgemeine Praxisnutzung aus dem Protokoll vom 10.04.2026. Sie enthalten keine Raumlufttechnik für einen ambulanten Operationsbereich und keine besondere Sterilgutversorgung. Für solche Nutzungen wären gesonderte Betreiberangaben und Fachbeiträge erforderlich.",
        ("h","2. Kostenansatz netto"),
        ("t",[["Anlagenbereich","Netto EUR"],["Heizung und Wärmeverteilung","185.000,00"],["Lüftung allgemeine Praxisbereiche","165.000,00"],["Sanitär","125.000,00"],["Elektro und Datentechnik","215.000,00"],["Technische Anlagen ohne Aufzug","690.000,00"],["Aufzug mit zwei Haltestellen","48.000,00"]],[350,141]),
        "Preisstand ist Juni 2026. Die Ansätze enthalten die üblichen Montageleistungen der jeweiligen Anlagen, nicht die Honorare unserer Fachplanung und nicht eine Änderung des Gebäudetragwerks. Der Aufzug wird separat geführt und darf nicht nochmals in den 690.000 EUR addiert werden.",
        "Für die Koordination schlagen wir einen gemeinsamen Termin am 15.06.2026 vor. Ein überarbeiteter Beitrag kann erst nach Festlegung der Geometrie zugesagt werden. Dieses Schreiben ist keine Ausführungsfreigabe und keine Bestätigung der kollisionsfreien Integration." ])
    record(3,12,"plan","owner","Kostenschätzung zum Vorplanungsstand VP 02",[
        "Zum Vorplanungsstand VP-02 vom 01.04.2026 stellen wir den folgenden Kostenrahmen der Gebäude- und Projektbestandteile zusammen. Grundlage sind 1.080 m² Bruttogrundfläche, zwei Geschosse und die bisher beschriebene allgemeine Praxisnutzung. Die Zahlen sind Planungsansätze, keine eingeholten Bauangebote.",
        ("t",[["Projektbestandteil","Netto EUR"],["Baukonstruktion einschließlich Innenausbau","1.400.000,00"],["Technische Anlagen einschließlich Aufzug","720.000,00"],["Außenanlagen","130.000,00"],["Lose Ausstattung","150.000,00"],["Planung und steuerpflichtige Nebenkosten","380.000,00"],["Summe netto","2.780.000,00"],["Umsatzsteuer 19 Prozent","528.200,00"],["Kosten brutto","3.308.200,00"],["Reserve brutto","200.000,00"],["Mit Reserve brutto","3.508.200,00"]],[350,141]),
        "Grundstückskosten und öffentlich-rechtliche Gebühren sind in dieser Aufstellung nicht enthalten. Das Grundstück steht bereits zur Verfügung; die Gebühren sind noch nicht beziffert und müssen innerhalb des Gesamtfinanzrahmens von 3.800.000 EUR berücksichtigt werden. Die Reserve ist kein erteilter Auftrag.",
        "Die technischen Ansätze beruhen auf dem Flächen- und Nutzungsstand der Vorplanung. Schachtgrößen und tragende Linien sind noch nicht integriert. Besondere medizinische Geräte, ein Operationsbereich und eine zusätzliche Etage sind nicht Bestandteil dieser Schätzung.",
        "Die spätere Kostenberechnung soll den konkretisierten Entwurf und die Fachbeiträge abbilden. Mengen- und Preisänderungen sind dann gegenüber diesem Stand zu erläutern. Die vorliegende Aufstellung trifft keine Aussage über die Fälligkeit von Planungshonoraren." ])
    record(3,13,"plan","owner","Protokoll der Entwurfskoordination vom 9 Juni",[
        "Am 09.06.2026 haben Theda Mertin, Janne Heller, Malte Rötte und Svea Rabe von 14:00 bis 15:10 Uhr den Stand E-03, T-02 und L-04 besprochen. Dr. Felder war nicht anwesend. Die Sitzung fand im Büro Heller und Seifert statt.",
        ("h","1. Schacht K-07"),
        "Der geometrische Konflikt aus der Tragwerksnotiz wurde anhand des Ausschnitts L-04 nachvollzogen. Frau Rabe bestätigte keine Durchdringung der Unterzugslinie. Herr Rötte erläuterte, dass der angesetzte Querschnitt derzeit nicht ohne weitere Prüfung verkleinert werden kann. Eine Aufteilung in zwei Schächte wurde angesprochen, aber nicht beschlossen.",
        "Frau Mertin bat um Darstellung der betroffenen Räume, falls eine Verlegung nach Süden erforderlich wird. Sie erklärte keine Zustimmung zum Verlust eines Behandlungsraums. Eine Änderung des Tragwerks blieb als weitere Möglichkeit offen. Es wurde weder eine technische Freigabe noch eine zusätzliche Bauleistung beauftragt.",
        ("h","2. Kostenstand"),
        "Die Kostenberechnung vom 08.06. wurde als aktueller Bürostand übergeben. Sie enthält den TGA-Ansatz von 690.000 EUR netto und den Aufzug gesondert mit 48.000 EUR netto. Für eine aus K-07 folgende Änderung des Tragwerks liegt noch kein belastbarer Ansatz vor. Der Gesamtfinanzrahmen bleibt unverändert.",
        ("h","3. Termine und weiterer Austausch"),
        "Der ursprünglich für 12.06. vorgesehene abschließend abgestimmte Entwurf wird nicht als erreicht bestätigt. Die Beteiligten wollen am 15.06. die geometrischen Möglichkeiten besprechen. Frau Heller soll den Terminstand anhand dieser offenen Koordination fortführen. Eine Dauer für die anschließende Fachbearbeitung ist noch nicht zugesagt.",
        "Frau Mertin wird die Raumfolgen mit der Praxisgemeinschaft besprechen. Das Protokoll wurde am 09.06. um 17:00 Uhr versandt. Rückmeldungen lagen bei Ablage noch nicht vor. Der Versand gilt nicht als stillschweigende Zustimmung zu einer der besprochenen Lösungen." ])
    record(3,15,"user","owner","Zusätzlicher Wunsch für einen ambulanten Eingriffsbereich",[
        "Nach einem Gespräch mit einer möglichen weiteren Partnerpraxis möchten wir prüfen lassen, ob im Obergeschoss künftig ambulante Eingriffe möglich wären. Wir haben dazu noch keine abgestimmte Betriebsbeschreibung. Die Partnerpraxis denkt an einen gesonderten Eingriffsraum und eine andere Materialversorgung als bisher.",
        "Uns ist bekannt, dass der bestätigte Stand vom 10.04. keinen Operationsbereich enthält. Ich möchte diese Nutzung daher zunächst als Möglichkeit zur Diskussion stellen. Eine Zustimmung der Eigentümerin zu einem neuen Programm oder zu Mehrkosten liegt nicht vor.",
        "Bitte den bisherigen Entwurf nicht schon als hierfür geeignet gegenüber der Partnerpraxis bezeichnen. Wir benötigen zunächst eine Aussage, welche Betreiber- und Fachangaben für die Prüfung erforderlich wären. Die Anzahl der bislang bestätigten allgemeinen Behandlungsräume möchten wir vor einer Entscheidung nicht reduzieren.",
        "Für den Termin am 15.06. kann ich ab 15:00 Uhr telefonisch hinzukommen. Eine verbindliche Zusage der Partnerpraxis gibt es noch nicht. Diese Nachricht ist kein Auftrag an die Fachbüros und keine Freigabe einer technischen Lösung." ])


def write_csv(path, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        csv.writer(stream, delimiter=";").writerows(rows)


def write_case_data(phase, directory):
    if phase == 1:
        write_csv(directory/CASES[1]["files"][4], [
            ["Datum","Angebot","Besucher","Betriebsform","Ort","Vermerk"],
            ["2025-09-06","Lesung Herbstbeginn",84,"Sitzplätze","Mietsaal","gez. Ruben Kersten"],
            ["2025-09-13","Werkstatt Holz",16,"Kurs","Werkraum","2 Betreuende zusätzlich"],
            ["2025-09-20","Akustikabend",112,"Sitzplätze","Mietsaal","18 Klapptische nicht benutzt"],
            ["2025-10-04","Konzert Nordlicht",148,"Stehplätze","Mietsaal","Zahl aus Einlasszählung"],
            ["2025-10-11","Werkstatt Papier",18,"Kurs","Werkraum","2 Betreuende zusätzlich"],
            ["2025-10-18","Bewegungsgruppe",24,"Kurs","Mietsaal","Ohne Bestuhlung"],
            ["2025-11-01","Lesung Stadtgeschichten",96,"Sitzplätze","Mietsaal","90 eigene; 10 geliehene Stühle"],
            ["2025-11-08","Konzert Abendwind",157,"Stehplätze","Mietsaal","Zahl aus Kartenverkauf"],
            ["2025-11-15","Werkstatt Holz",17,"Kurs","Werkraum","2 Betreuende zusätzlich"],
            ["2025-12-06","Wintermarkt",210,"Wechselnde Besucher","Mietsaal und Hof","Tageszählung; nicht gleichzeitig"],
            ["2025-12-13","Lesung Winter",118,"Sitzplätze","Mietsaal","28 Stühle geliehen"],
            ["2026-01-10","Bewegungsgruppe",22,"Kurs","Mietsaal","1 Leitung zusätzlich"],
            ["2026-01-17","Werkstatt Papier",15,"Kurs","Werkraum","2 Betreuende zusätzlich"],
            ["2026-01-24","Konzert Nordlicht",152,"Stehplätze","Mietsaal","Zahl aus Einlasszählung"],
            ["2026-02-07","Lesung Februar",108,"Sitzplätze","Mietsaal","Auszug erstellt 10.02.2026"],
        ])
        (directory/CASES[1]["files"][8]).write_text(
            "Kulturhof Am Buchenrain\nHausmeister Benno Tesch\nAm Buchenrain 14, 32760 Detmold\n\n13.02.2026, 07:40 Uhr\nAn Hanna Wendt\nBezug KD-26-01 / Ergänzung zum gestrigen Rundgang\n\n"
            "Guten Morgen Frau Wendt,\n\nbei der Nordwand habe ich seit November einen dunkleren Rand bemerkt. Beim Starkregen stand draußen Wasser an der Ecke zum Westanbau. Ich habe den Hofablauf danach gereinigt. Ob der Fleck schon vorher unter den alten Regalen vorhanden war, weiß ich nicht. Die Regale wurden erst im Dezember abgebaut.\n\n"
            "Die eingezeichnete Leitung im Hof ist meine Erinnerung an eine Reparatur um 2011. Ich war damals nicht bei den Erdarbeiten dabei. Der Ablaufdeckel ist sichtbar, der weitere Verlauf nicht. Einen Leitungsplan habe ich nicht.\n\n"
            "Den Durchgang zum Westanbau hat der frühere Betrieb einmal versetzt. Ich meine, das war im selben Jahr wie die Heizungsreparatur, kann es aber nicht sicher sagen. Der neue Durchgang ist seit meiner Übernahme 2015 vorhanden.\n\n"
            "Auf dem Dachboden standen früher wohl Papierrollen. Das wurde mir bei der Übergabe erzählt; ich habe die Rollen nie gesehen. Seit 2024 war ich dort nicht mehr. Ich suche den Schlüssel weiter in der alten Schlüsselbox. Bitte meine Erinnerung nicht als Belastungsnachweis verwenden.\n\n"
            "Viele Grüße\nBenno Tesch\nHausmeister\nAnlagen: keine\n", encoding="utf-8")
    elif phase == 2:
        write_csv(directory/CASES[2]["files"][10],[
            ["Stand","Plan","Bezug","Menge","Einheit","Herkunft"],
            ["19.03.2026","V1-01","Gebäudelänge",36,"m","Zeichnung 12.03."],
            ["19.03.2026","V1-01","Gebäudebreite",24,"m","Zeichnung 12.03."],
            ["19.03.2026","V1-01","Geschosse",1,"St","Zeichnung 12.03."],
            ["19.03.2026","V1-01","BGF",864,"m²","36 mal 24"],
            ["19.03.2026","V1-01","Gruppen",3,"St","Betreiberprogramm"],
            ["19.03.2026","V1-01","Plätze",75,"St","Betreiberprogramm"],
            ["19.03.2026","V2-01","Gebäudelänge",24,"m","Zeichnung 12.03."],
            ["19.03.2026","V2-01","Gebäudebreite",18,"m","Zeichnung 12.03."],
            ["19.03.2026","V2-01","Geschosse",2,"St","Zeichnung 12.03."],
            ["19.03.2026","V2-01","BGF",864,"m²","24 mal 18 mal 2"],
            ["19.03.2026","V2-01","Gruppen",3,"St","Betreiberprogramm"],
            ["19.03.2026","V2-01","Plätze",75,"St","Betreiberprogramm"],
            ["19.03.2026","Beide","Außenfläche bearbeitet",1500,"m²","Ansatz Sander"],
            ["19.03.2026","Beide","Grundstück",3224,"m²","62 mal 52 schematisch"],
            ["19.03.2026","Beide","Mahlzeiten täglich",75,"St","Betreiberprogramm"],
            ["19.03.2026","Beide","Bearbeitung","Levin Sander","","An Wiesenbogen Bildung gGmbH"],
        ])
        (directory/CASES[2]["files"][12]).write_text(
            "Büro Sander Gebäudeplanung\nQuellenstieg 11, 31812 Bad Pyrmont\nplanung@sander-bau.example\n\nAn Wiesenbogen Bildung gGmbH\n20.03.2026 / KP-26-02\nRahmentermine zur Variantenberatung\n\n"
            "Sehr geehrte Frau Lammers,\n\ndie nachfolgenden Termine bilden den Arbeitsstand für die Beratung ab. Es handelt sich nicht um Zusagen von Behörden oder späteren Auftragnehmern. Die Bauzeit ist für beide Varianten bislang mit demselben Rahmen angesetzt.\n\n"
            "27.03.2026: vorgesehene Beratung über die Varianten.\n31.03.2026: erhoffte schriftliche Auswahlentscheidung.\n13.04.2026: frühester Beginn Entwurfsplanung bei Folgeabruf.\n15.05.2026: benötigter Baugrundbeitrag für weitere Gründungsannahmen.\n29.05.2026: vorgesehener abgestimmter Entwurfsstand.\n26.06.2026: angestrebte Zusammenstellung von Antragsunterlagen.\n29.06.2026 bis 30.09.2026: zunächst angenommener Verfahrenszeitraum.\n01.10.2026 bis 18.12.2026: weitere Planung und Vorbereitung der Vergabe.\n11.01.2027 bis 26.02.2027: vorgesehene Vergabezeit.\n15.03.2027: angestrebter Baubeginn.\n29.10.2027: angenommene bauliche Fertigstellung.\nNovember 2027: Ausstattung, Nachweise und betriebliche Vorbereitung.\n01.12.2027: gewünschter Betriebsbeginn.\n\n"
            "Die Betreiberin hat für eine mögliche Küchenlieferung noch keinen Auftrag ausgelöst. Ein zusätzlicher Klärungsbedarf für den Lieferzugang oder die obere Gruppe ist nicht mit einer eigenen Dauer eingerechnet. Wird die Variantenentscheidung verschoben, muss der Folgeablauf neu abgestimmt werden.\n\n"
            "Mit freundlichen Grüßen\nLevin Sander\nArchitekt\nAnlagen: keine\n",encoding="utf-8")
    elif phase == 3:
        rows=[["Stand","Plan","Zone","Nutzung","Rasterfläche m²","Hinweis"]]
        for floor in ("EG","OG"):
            north_names=["Behandlung 1","Behandlung 2","Diagnostik","Warten Nord","Behandlung 3"] if floor=="EG" else ["Sprechzimmer 4","Sprechzimmer 5","Therapie","Personal","Besprechung"]
            south_names=["Anmeldung und Warten","Nebenräume","Treppe und Aufzug","Sanitär","Technik"] if floor=="EG" else ["Therapie Nebenbereich","Material","Treppe und Aufzug","Sanitär","Verwaltung"]
            for i,name in enumerate(north_names+south_names,1):rows.append(["05.06.2026",f"E-03-{floor}",f"{floor}-{i:02d}",name,48,"6 mal 8 m Außenraster; keine NRF"])
            rows.append(["05.06.2026",f"E-03-{floor}",f"{floor}-11","Flur und Verteilung",60,"30 mal 2 m Raster"])
        rows.extend([["05.06.2026","E-03","Gesamt","Zwei Ebenen",1080,"Wand- und Verteilanteile enthalten"],
                     ["05.06.2026","L-04","K-07","Schacht",3.6,"Bereits in Rasterzone enthalten"],
                     ["05.06.2026","AS-26-03","Bearbeitung","Janne Heller","","An Mühlenanger Immobilien KG"]])
        write_csv(directory/CASES[3]["files"][9],rows)
        (directory/CASES[3]["files"][15]).write_text(
            "Heller und Seifert Architektur\nLindenbreite 17, 31655 Stadthagen\nhs@heller-seifert.example\n\nAn Theda Mertin\n12.06.2026, 16:25 Uhr\nAS-26-03 / Versandjournal Entwurfsunterlagen\n\n"
            "Sehr geehrte Frau Mertin,\n\nwir halten für Ihre Projektablage den folgenden Versandstand fest. Die Einträge dokumentieren die Übermittlung, nicht eine technische oder rechtsgeschäftliche Freigabe.\n\n"
            "01.06.2026, 15:10: E-03-EG, E-03-OG und E-03-S an Mertin, Rötte und Rabe; Zweck Entwurfskoordination.\n02.06.2026, 11:40: Objektbeschreibung E-03 an Mertin; Zweck Lesestand.\n03.06.2026, 09:15: L-04 von Rötte empfangen; Zweck Schachtkoordination.\n03.06.2026, 16:00: T-02 Notiz von Rabe empfangen; keine Durchdringung bestätigt.\n04.06.2026, 14:20: TGA-Kostenansatz empfangen.\n05.06.2026, 12:05: Raumliste E-03 an Mertin und Felder.\n08.06.2026, 17:10: Kostenberechnung an Mertin; K-07 noch offen.\n09.06.2026, 17:00: Koordinationsprotokoll an alle Teilnehmenden.\n10.06.2026, 13:30: Terminfortschreibung an Mertin.\n11.06.2026, 10:32: Betreiberwunsch zu Eingriffen von Felder eingegangen.\n12.06.2026, 16:25: keine neue geometrische Schachtfassung eingegangen.\n\n"
            "Der Termin am 15.06. bleibt zur Abstimmung vorgesehen. Eine Revision E-04 ist bislang nicht erstellt. Die Unterlagen E-03 dürfen deshalb nicht mit einer später bestätigten Schachtlösung bezeichnet werden. Eine Einreichung bei der Bauaufsicht wurde durch unser Büro nicht veranlasst.\n\n"
            "Mit freundlichen Grüßen\nJanne Heller\nArchitektin\nAnlagen: keine neuen Unterlagen\n",encoding="utf-8")


def plan_canvas(path, phase, title, plan_id, date, purpose):
    cv=canvas.Canvas(str(path), pagesize=landscape(A4), invariant=1)
    cv.setAuthor(AUTHOR); cv.setCreator(AUTHOR); cv.setTitle(title)
    cv.setSubject("Technische Bauzeichnung")
    plan_frame(cv, phase, title, plan_id, date, purpose)
    return cv


def plan_frame(cv, phase, title, plan_id, date, purpose):
    c=CASES[phase]; cv.setStrokeColor(colors.black); cv.setFillColor(colors.black)
    cv.setFont("AktenSerifB", 15); cv.drawString(35, 560, c["title"])
    cv.setFont("AktenSerif", 11); cv.drawString(35, 542, title)
    cv.setFont("AktenSerif", 9); cv.drawString(35, 30, f"{c['code']} · {plan_id} · {date} · {purpose}")
    signer="F. Linde" if plan_id=="B-98-01" else c["actors"]["tga"][3] if plan_id=="L-04" else c["actors"]["plan"][3]
    cv.drawRightString(805, 30, "gez. "+signer)


def room(cv, x, y, w, h, lines, fill="#f2f4f3"):
    cv.setFillColor(colors.HexColor(fill)); cv.setStrokeColor(colors.HexColor("#28352f")); cv.setLineWidth(1)
    cv.rect(x,y,w,h,fill=1,stroke=1); cv.setFillColor(colors.black); cv.setFont("AktenSerif",9)
    for i,line in enumerate(lines): cv.drawCentredString(x+w/2,y+h/2+5-(i*12),line)


def dimension(cv,x1,y1,x2,y2,text):
    cv.setFillColor(colors.black)
    cv.setStrokeColor(colors.HexColor("#525e58")); cv.setLineWidth(.5); cv.line(x1,y1,x2,y2)
    if y1==y2:
        cv.line(x1,y1-4,x1,y1+4); cv.line(x2,y2-4,x2,y2+4); cv.setFont("AktenSerif",9); cv.drawCentredString((x1+x2)/2,y1+5,text)
    else:
        cv.line(x1-4,y1,x1+4,y1); cv.line(x2-4,y2,x2+4,y2); cv.saveState(); cv.translate(x1-5,(y1+y2)/2); cv.rotate(90); cv.setFont("AktenSerif",9); cv.drawCentredString(0,0,text); cv.restoreState()


def door(cv,x,y,size=16,angle=0):
    cv.saveState(); cv.translate(x,y); cv.rotate(angle); cv.setStrokeColor(colors.white); cv.setLineWidth(3); cv.line(0,0,size,0)
    cv.setStrokeColor(colors.HexColor("#28352f")); cv.setLineWidth(.6); cv.line(0,0,0,size); cv.arc(0,0,size*2,size*2,180,90); cv.restoreState()


def north(cv,x,y):
    cv.setFillColor(colors.black); cv.setStrokeColor(colors.black); cv.setFont("AktenSerifB",11); cv.drawCentredString(x,y+30,"N")
    cv.line(x,y,x,y+22); cv.line(x,y+22,x-4,y+14); cv.line(x,y+22,x+4,y+14)


def phase_one_plans(directory, qa):
    p=directory/CASES[1]["files"][5]
    cv=plan_canvas(p,1,"Packhausbestand Erdgeschoss und Dachraum", "B-98-01", "16.06.1998", "Plan aus der Grundstücksmappe")
    cv.setFont("AktenSerif",9); cv.drawString(35,520,"Zeichnung: Baubüro F. Linde · Maßstab 1:200 bei A4 · Außenmaße in m")
    u=14.17322835; x=220; y=130
    room(cv,x,y,24*u,14*u,["Packhalle", "24,00 x 14,00 m Außenmaß", "EG ±0,00"],"#f4f4f1")
    room(cv,x-8*u,y,8*u,10*u,["Westanbau", "8,00 x 10,00 m"])
    room(cv,x-8*u,y,8*u,3*u,["Lager / Nebenraum"])
    door(cv,x+10*u,y,1.4*u); door(cv,x,y+4*u,1.1*u,90)
    for i in range(1,4): cv.line(x+10*u-6,y-i*5,x+11.4*u+6,y-i*5)
    cv.setFont("AktenSerif",8); cv.drawString(x+10*u-20,y-30,"Eingang / drei Stufen")
    for xx in (x+4*u,x+12*u,x+20*u):
        cv.setLineWidth(3); cv.setStrokeColor(colors.HexColor("#60848a")); cv.line(xx,y+14*u,xx+2*u,y+14*u)
    cv.setStrokeColor(colors.black); cv.setLineWidth(.5)
    dimension(cv,x,y+14*u+18,x+24*u,y+14*u+18,"24,00")
    dimension(cv,x+24*u+18,y,x+24*u+18,y+14*u,"14,00")
    dimension(cv,x-8*u,y-42,x,y-42,"8,00")
    north(cv,730,445)
    cv.setFont("AktenSerif",10); cv.drawString(625,335,"Dachraum über Packhalle")
    cv.setFont("AktenSerif",9)
    for i,line in enumerate(["Holzkonstruktion, geneigtes Dach", "Nutzung im Plan: Lager", "Keine Bauteilbemessung enthalten", "Dachraumzugang innen Nordwest", "Türlage schematisch", "Planmaß ersetzt kein Aufmaß"]): cv.drawString(625,316-i*16,line)
    cv.save()
    sketch=qa/"phase-1-begehung.pdf"
    cv=plan_canvas(sketch,1,"Begehungsskizze B 01", "B-01", "12.02.2026", "Ortszuordnung, nicht maßstäblich")
    x=220;y=160;u=15
    room(cv,x,y,24*u,14*u,["Saal / Packhalle", "besichtigt"])
    room(cv,x-8*u,y,8*u,10*u,["Westanbau", "besichtigt"])
    room(cv,x-8*u,y,8*u,3*u,["Heizraum"])
    door(cv,x+10*u,y,21);door(cv,x,y+6*u,17,90)
    cv.setStrokeColor(colors.HexColor("#b84535")); cv.setLineWidth(4);cv.line(x+2*u,y+14*u,x+5.5*u,y+14*u)
    cv.setFont("AktenSerifB",10); cv.drawString(x+2*u,y+14*u+10,"B1 Sockelverfärbung")
    cv.setFillColor(colors.HexColor("#b84535"));cv.circle(x-4*u,y+5*u,5,fill=1);cv.drawString(x-7*u,y+5*u+17,"B2 Altbelag")
    cv.setFillColor(colors.black); cv.setStrokeColor(colors.HexColor("#52727b"));cv.setDash(5,3);cv.line(90,110,625,110);cv.setDash()
    cv.setFont("AktenSerif",9);cv.drawString(190,90,"B3 Leitungsverlauf nur nach Erinnerung Tesch, nicht geortet")
    north(cv,700,440)
    for i,line in enumerate(["Dachraum: nicht betreten, Tür verschlossen.","Durchgang zum Anbau gegenüber Altplan versetzt.","B1: keine Messung. B2: keine Materialbestimmung.","Grundform aus Plan B-98-01, keine Bestandsaufnahme."]):cv.drawString(110,470-i*17,line)
    cv.save(); raster(sketch,directory/CASES[1]["files"][7])


def phase_two_plans(directory, qa):
    sketch=qa/"phase-2-grundstueck.pdf"
    cv=plan_canvas(sketch,2,"Grundstück und räumliche Randbedingungen", "L-01", "05.03.2026", "Schematische Projektzeichnung")
    x=170;y=105;u=6.2
    cv.setStrokeColor(colors.black);cv.setLineWidth(1.2);cv.rect(x,y,62*u,52*u)
    cv.setFillColor(colors.HexColor("#e3eddc"));cv.rect(x+4,y+4,62*u-8,52*u-8,fill=1,stroke=0)
    cv.setFillColor(colors.HexColor("#dadfe0"));cv.rect(x-20,y-35,62*u+40,28,fill=1,stroke=0)
    cv.setFillColor(colors.black);cv.setFont("AktenSerif",10);cv.drawCentredString(x+31*u,y-25,"Wiesenbogen / Zugang von Süden")
    room(cv,x+62*u+25,y+130,140,110,["Nachbarhaus", "Wiesenbogen 8", "Wohnfenster zur Grenze"],"#eee5e2")
    cv.setStrokeColor(colors.HexColor("#8c6f4c"));cv.setLineWidth(3);cv.line(x+4,y+30,x+4,y+240)
    cv.setFont("AktenSerif",9);cv.drawString(35,420,"Westen:");cv.drawString(35,405,"Geländesprung");cv.drawString(35,390,"etwa 0,8 m");cv.drawString(35,375,"nach Ortsnotiz")
    cv.setStrokeColor(colors.HexColor("#45655a"));cv.setLineWidth(1);cv.setDash(5,3);cv.rect(x+10*u,y+10*u,36*u,24*u);cv.setDash()
    cv.setFont("AktenSerif",11);cv.drawCentredString(x+28*u,y+22*u,"möglicher Baubereich V1")
    cv.setFont("AktenSerif",10);cv.drawString(x+40,y+285,"Nördlicher Gartenbereich")
    dimension(cv,x,y+52*u+20,x+62*u,y+52*u+20,"62,00 m");dimension(cv,x-18,y,x-18,y+52*u,"52,00 m")
    north(cv,735,460)
    cv.setFont("AktenSerif",9);cv.drawString(110,65,"Grundstücksfläche 3.224 m² aus schematischen Außenmaßen. Keine amtliche Vermessung.")
    cv.save();raster(sketch,directory/CASES[2]["files"][2])
    cv=plan_canvas(directory/CASES[2]["files"][3],2,"V1 Erdgeschoss / drei Gruppen", "V1-01", "12.03.2026", "Vorplanung 1:200 bei A4")
    x=145;y=110;u=14.17322835
    for i in range(3):
        room(cv,x+i*12*u,y+18*u,12*u,6*u,[f"Gruppe {i+1}","Hauptzone"],"#e2eddf")
        room(cv,x+i*12*u,y+16*u,12*u,2*u,[f"Nebenraum {i+1}"],"#edf1e8")
        door(cv,x+(i*12+5)*u,y+24*u,18,180)
    room(cv,x,y+12*u,36*u,4*u,["Flur / Garderoben / gemeinsame Verteilung"],"#f0efdf")
    room(cv,x,y,8*u,12*u,["Mehrzweck", "und Material"])
    room(cv,x+8*u,y,8*u,12*u,["Leitung", "Personal", "Besprechung"])
    room(cv,x+16*u,y,8*u,12*u,["Ausgabeküche", "Lager", "75 Mahlzeiten"])
    room(cv,x+24*u,y,12*u,12*u,["Sanitär", "Technik", "Reinigung"])
    for xx in (4,12,20,30):door(cv,x+xx*u,y+12*u,18)
    door(cv,x+14*u,y,22);door(cv,x+23*u,y,18)
    cv.setFont("AktenSerif",9);cv.drawString(x+12*u,y-23,"Haupteingang");cv.drawString(x+23*u,y-23,"Anlieferung")
    dimension(cv,x,y+24*u+17,x+36*u,y+24*u+17,"36,00 m");dimension(cv,x-18,y,x-18,y+24*u,"24,00 m")
    north(cv,745,440)
    for i,line in enumerate(["BGF 864 m²", "75 Plätze", "1 Geschoss", "Außenraster", "Zonen enthalten", "Wandanteile", "Raumflächen:", "Programm 04.03."]):cv.setFont("AktenSerif",9);cv.drawString(695,340-i*17,line)
    cv.save()
    cv=plan_canvas(directory/CASES[2]["files"][4],2,"V2 Erdgeschoss / zwei Gruppen", "V2-01 Blatt 1", "12.03.2026", "Vorplanung 1:150 bei A4")
    x=145;y=110;u=18.8976378
    for floor in (0,1):
        if floor:
            cv.showPage();plan_frame(cv,2,"V2 Obergeschoss / eine Gruppe", "V2-01 Blatt 2", "12.03.2026", "Vorplanung 1:150 bei A4")
        for i in range(2):
            label=f"Gruppe {i+1}" if not floor else ("Gruppe 3" if i==0 else "Mehrzweck / Material")
            room(cv,x+i*12*u,y+12*u,12*u,6*u,[label,"Hauptzone"],"#e2eddf")
            room(cv,x+i*12*u,y+10*u,12*u,2*u,["Nebenraum / Verteilung"],"#edf1e8")
        room(cv,x,y+8*u,24*u,2*u,["Flur / Garderoben"],"#f0efdf")
        room(cv,x,y,8*u,8*u,["Küche / Ausgabe" if not floor else "Leitung / Personal","Lager" if not floor else "Besprechung"])
        room(cv,x+8*u,y,8*u,8*u,[""])
        cv.drawCentredString(x+12*u,y+7.2*u,"Treppe / Aufzug")
        room(cv,x+16*u,y,8*u,8*u,["Sanitär / Pflege","Technik" if not floor else "Material"])
        for stair in range(7):cv.line(x+9*u,y+(stair+.5)*u,x+11.5*u,y+(stair+.5)*u)
        room(cv,x+12*u,y+u,2.8*u,3*u,["Lift"],"#dce5ea")
        room(cv,x+21*u,y+13*u,3*u,5*u,["2. Treppe"],"#e1e6ed")
        for xx in (4,12,20):door(cv,x+xx*u,y+8*u,18)
        if not floor:door(cv,x+13*u,y,22)
        dimension(cv,x,y+18*u+18,x+24*u,y+18*u+18,"24,00 m");dimension(cv,x-18,y,x-18,y+18*u,"18,00 m")
        north(cv,735,445)
        lines=["432 m² BGF je Ebene", "Gesamt 864 m² BGF", "75 Plätze / 3 Gruppen", "Außenraster", "Zonen mit Wandanteilen", "Treppenanordnung", "noch fachlich abzustimmen"]
        for i,line in enumerate(lines):cv.setFont("AktenSerif",9);cv.drawString(635,330-i*17,line)
    cv.save()


def phase_three_plans(directory,qa):
    for floor,number in (("EG",3),("OG",4)):
        cv=plan_canvas(directory/CASES[3]["files"][number-1],3,f"Entwurf {floor} / Raum- und Tragwerksbezug",f"E-03-{floor}","01.06.2026","Entwurf 1:150 bei A4")
        x=85;y=115;u=18.8976378
        north_names=["Behandlung 1","Behandlung 2","Diagnostik","Warten Nord","Behandlung 3"] if floor=="EG" else ["Sprechzimmer 4","Sprechzimmer 5","Therapie","Personal","Besprechung"]
        south_names=["Anmeldung / Warten","Nebenräume","Treppe / Aufzug","Sanitär","Technik"] if floor=="EG" else ["Therapie Nebenbereich","Material","Treppe / Aufzug","Sanitär","Verwaltung"]
        for i,label in enumerate(north_names):
            room(cv,x+i*6*u,y+10*u,6*u,8*u,[label,f"{floor}-{i+1:02d}","Raster 6 x 8 m"],"#e4ebdf")
            door(cv,x+(i*6+2)*u,y+10*u,16)
        room(cv,x,y+8*u,30*u,2*u,[f"{floor}-11 Flur und Verteilung"],"#edeada")
        for i,label in enumerate(south_names):
            room(cv,x+i*6*u,y,6*u,8*u,[label,f"{floor}-{i+6:02d}","Raster 6 x 8 m"])
            door(cv,x+(i*6+2)*u,y+8*u,16)
        if floor=="EG":door(cv,x+2*u,y,22)
        room(cv,x+15.2*u,y+.6*u,2*u,2.4*u,["Lift"],"#d8e3e8")
        for i in range(8):cv.line(x+12.5*u,y+(.5+i*.32)*u,x+14.7*u,y+(.5+i*.32)*u)
        cv.setStrokeColor(colors.HexColor("#b04135"));cv.setLineWidth(1.6);cv.setDash(4,3)
        cv.line(x+6*u,y+11.2*u,x+24*u,y+11.2*u);cv.setDash()
        cv.setFillColor(colors.HexColor("#efd0bc"));cv.rect(x+12.2*u,y+10.2*u,1.8*u,2*u,fill=1,stroke=1)
        cv.setFillColor(colors.black);cv.setFont("AktenSerif",8);cv.drawString(x+14.3*u,y+11*u,"K-07")
        dimension(cv,x,y+18*u+18,x+30*u,y+18*u+18,"30,00 m")
        dimension(cv,x-20,y,x-20,y+18*u,"18,00 m")
        for i in range(6):
            cv.setFont("AktenSerif",8);cv.drawCentredString(x+i*6*u,y-18,f"{i+1}")
        for i in range(5):dimension(cv,x+i*6*u,y-38,x+(i+1)*6*u,y-38,"6,00")
        north(cv,757,442)
        for i,line in enumerate(["540 m² BGF", "Achsraster 6,00 m", "Rot gestrichelt:", "Unterzugsansatz", "Orange: Schachtansatz", "K-07 nicht abgestimmt", "Raumflächen im Raster", "einschließlich Wände", "EG ±0,00 / OG +3,60"]):cv.setFont("AktenSerif",9);cv.drawString(675,357-i*19,line)
        cv.save()
    cv=plan_canvas(directory/CASES[3]["files"][4],3,"Schnitt 1 und Südansicht", "E-03-S", "01.06.2026", "Entwurf 1:150 bei A4")
    x=85;u=18.8976378;y=340
    cv.setFont("AktenSerifB",11);cv.drawString(x,505,"1. Schnitt durch Treppen- und Technikkern")
    cv.setFillColor(colors.HexColor("#f1f3f0"));cv.rect(x,y,18*u,7.8*u,fill=1,stroke=1)
    for height in (0,3.6,7.2):cv.setLineWidth(3);cv.line(x,y+height*u,x+18*u,y+height*u)
    cv.setLineWidth(1);cv.line(x+9*u,y,x+9*u,y+7.2*u)
    cv.setFont("AktenSerif",9);cv.setFillColor(colors.black)
    cv.drawString(x+15,y+25,"Erdgeschoss")
    cv.drawString(x+15,y+3.6*u+25,"Obergeschoss / Flachdach über +7,20")
    for height,label in ((0,"±0,00"),(3.6,"+3,60"),(7.2,"+7,20"),(7.8,"+7,80 Attika")):cv.drawString(x+18*u+15,y+height*u-3,label)
    dimension(cv,x,y-20,x+18*u,y-20,"18,00 m")
    cv.drawString(590,435,"Technikansatz: keine Detailplanung")
    cv.drawString(590,417,"Dachfläche 540 m²")
    cv.drawString(590,399,"Geschosshöhen 3,60 m")
    cv.drawString(590,381,"Installationshöhen noch abzustimmen")
    cv.setFont("AktenSerifB",11);cv.drawString(x,285,"2. Südansicht")
    y=100;cv.setFillColor(colors.HexColor("#eeeae2"));cv.rect(x,y,30*u,7.8*u,fill=1,stroke=1)
    for level in (0,3.6):
        for i in range(5):
            cv.setFillColor(colors.HexColor("#cadce2"));cv.rect(x+(i*6+1)*u,y+(level+1)*u,4*u,1.7*u,fill=1,stroke=1)
    cv.setFillColor(colors.HexColor("#b9c7cc"));cv.rect(x+2*u,y,2*u,2.4*u,fill=1,stroke=1)
    dimension(cv,x,y-20,x+30*u,y-20,"30,00 m")
    cv.setFillColor(colors.black);cv.setFont("AktenSerif",9);cv.drawString(420,287,"Fassadenansätze gesamt:")
    cv.drawString(420,272,"720 m² geschlossen / 180 m² Öffnungen")
    cv.drawString(420,257,"Ansatz inkl. Rücksprünge, alle Ansichten")
    cv.save()
    p=qa/"phase-3-tga-schacht.pdf"
    cv=plan_canvas(p,3,"L 04 Schacht und Unterzug über Erdgeschoss", "L-04", "03.06.2026", "Koordinationsausschnitt 1:50 bei A4")
    x=180;y=140;u=56.6929134
    room(cv,x,y,6*u,6*u,[""],"#f4f5f1")
    cv.setFillColor(colors.HexColor("#e9c8b0"));cv.rect(x+2.2*u,y+2.2*u,1.8*u,2*u,fill=1,stroke=1)
    cv.setFont("AktenSerif",10);cv.setFillColor(colors.black);cv.drawCentredString(x+3.1*u,y+2.8*u,"Schacht")
    cv.drawCentredString(x+3.1*u,y+2.5*u,"1,80 x 2,00 m")
    cv.setStrokeColor(colors.HexColor("#a33b33"));cv.setLineWidth(10);cv.line(x,y+3.2*u,x+6*u,y+3.2*u)
    cv.setFillColor(colors.black);cv.setFont("AktenSerif",9);cv.drawString(570,395,"K-07 / Decke über EG")
    lines=["Unterzugslinie T-02:","y = 11,20 m im Gesamtplan", "Schachtlage im Gesamtplan:","x = 12,20 bis 14,00 m", "y = 10,20 bis 12,20 m", "Lage nicht bestätigt", "Bezug: E-03 / T-02", "gez. Malte Rötte"]
    for i,line in enumerate(lines):cv.drawString(570,373-i*20,line)
    dimension(cv,x+2.2*u,y+4.2*u+18,x+4*u,y+4.2*u+18,"1,80 m")
    dimension(cv,x+4*u+20,y+2.2*u,x+4*u+20,y+4.2*u,"2,00 m")
    cv.setFont("AktenSerif",9);cv.drawString(180,105,"Rot: Unterzug aus T-02. Orange: Schachtbedarf aus L-04. Keine Durchdringung freigegeben.")
    cv.save();raster(p,directory/CASES[3]["files"][6])


def raster(source, target):
    subprocess.run(["pdftoppm","-f","1","-singlefile","-scale-to","2400","-png",str(source),str(target.with_suffix(""))],check=True,capture_output=True)
    with Image.open(target) as im:
        meta=PngImagePlugin.PngInfo(); meta.add_text("Author",AUTHOR);meta.add_text("Title",target.stem)
        im.save(target,pnginfo=meta)


def main():
    parser=argparse.ArgumentParser(); parser.add_argument("--phase",type=int,choices=[1,2,3],action="append")
    parser.add_argument("--assets",type=Path,default=Path(os.environ.get("HOAI_1_3_ASSETS","/tmp/bauwirtschaft-hoai-1-3-assets")))
    args=parser.parse_args(); qa=args.assets/"qa-hoai-1-3"; qa.mkdir(parents=True,exist_ok=True)
    register_fonts()
    for phase in args.phase or [1,2,3]:
        globals()[{1:"phase_one",2:"phase_two",3:"phase_three"}[phase]]()
        c=CASES[phase]; directory=ROOT/"testakten"/c["slug"]; directory.mkdir(parents=True,exist_ok=True)
        write_case_data(phase,directory)
        for number,d in DOCS[phase].items():
            dest=directory/c["files"][number-1]
            {".docx":make_docx,".pdf":make_pdf,".eml":make_eml}[dest.suffix](phase,d,dest)
        globals()[{1:"phase_one_plans",2:"phase_two_plans",3:"phase_three_plans"}[phase]](directory,qa)
        print(f"Phase {phase}: {len(DOCS[phase])} Textdokumente und fallbezogene Daten/Pläne erstellt.",flush=True)
    (qa/"aktenmodell.json").write_text(json.dumps(CASES,ensure_ascii=False,indent=2),encoding="utf-8")


if __name__=="__main__": main()
