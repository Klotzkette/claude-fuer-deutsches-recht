#!/usr/bin/env python3
"""Erzeugt ausschließlich die beiden Arbeitsakten Dortmund und Aachen."""

from __future__ import annotations

import argparse
import csv
import os
import re
from datetime import datetime
from email.message import EmailMessage
from email.policy import SMTP
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
DORTMUND = "anwaltschaft-dienstleister-datenzugang-dortmund"
AACHEN = "corporate-contract-law-rahmenlieferung-sensorik-aachen"
DISCLAIMER = (
    "Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.",
    "This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.",
)
K = "Kettenlicht Fahrradhandel GmbH"
N = "Netzraum Digital OHG"
R = "Rheinkern Anlagenbau GmbH"
T = "Talbruck Sensorik GmbH"
CONTACT = {
    K: "Lindemannstraße 41, 44137 Dortmund\nGeschäftsführerin Jana Römer · Amtsgericht Dortmund HRB 34718\nTelefon 0231 580 62 40 · buero@kettenlicht-fahrradhandel.de",
    N: "Rheinische Straße 168, 44147 Dortmund\nGesellschafter Felix Sander und Nils Böttcher · Amtsgericht Dortmund HRA 19342\nTelefon 0231 971 43 20 · service@netzraum-digital.de",
    R: "Jülicher Straße 318, 52070 Aachen\nGeschäftsführer Dr. Leonhard Evers und Miriam Küppers · Amtsgericht Aachen HRB 24681\nTelefon 0241 936 42 0 · einkauf@rheinkern-anlagenbau.de",
    T: "Gewerbepark 17, 52249 Eschweiler\nGeschäftsführer Henning Voß · Amtsgericht Aachen HRB 22874\nTelefon 02403 748 61 0 · vertrieb@talbruck-sensorik.de",
}


def write_text(path, text):
    path.write_text(text.strip() + "\n", encoding="utf-8")


def docx(path, org, title, meta, sections, closing=None):
    d = Document()
    s = d.sections[0]
    s.page_width, s.page_height = Cm(21), Cm(29.7)
    s.top_margin, s.bottom_margin = Cm(2), Cm(1.9)
    s.left_margin, s.right_margin = Cm(2.2), Cm(2.2)
    for name in ("Normal", "Title", "Heading 1", "Heading 2"):
        st = d.styles[name]
        st.font.name = "Times New Roman"
        for element in st.element.xpath(".//w:rFonts"):
            for attr in list(element.attrib):
                if "theme" in attr.lower():
                    del element.attrib[attr]
            for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
                element.set(qn("w:" + attr), "Times New Roman")
        for element in st.element.xpath(".//w:pBdr"):
            element.getparent().remove(element)
        st.font.size = Pt(11 if name == "Normal" else 13)
        st.font.color.rgb = RGBColor(0, 0, 0)
        st.paragraph_format.space_after = Pt(7)
        if name != "Normal":
            st.font.bold = True
            st.paragraph_format.space_before = Pt(9)
            st.paragraph_format.keep_with_next = True
    d.styles["Title"].font.size = Pt(16)
    d.styles["Normal"].paragraph_format.line_spacing = 1.08
    if len(sections) >= 10:
        d.styles["Normal"].paragraph_format.line_spacing = 1.0
        d.styles["Normal"].paragraph_format.space_after = Pt(5)
        d.styles["Heading 1"].font.size = Pt(12)
        d.styles["Heading 1"].paragraph_format.space_before = Pt(7)
        d.styles["Heading 1"].paragraph_format.space_after = Pt(5)
    d.add_paragraph(org).runs[0].bold = True
    d.add_paragraph(CONTACT.get(org, ""))
    d.add_paragraph(title, "Title")
    for key, value in meta:
        p = d.add_paragraph()
        p.add_run(key + ": ").bold = True
        p.add_run(value)
    for heading, paragraphs in sections:
        if heading:
            d.add_paragraph(heading, "Heading 1")
        for text in paragraphs:
            d.add_paragraph(text)
    if closing:
        d.add_paragraph(closing)
    footer = s.footer.paragraphs[0]
    footer.add_run(org + " · Seite ")
    field = OxmlElement("w:fldSimple")
    field.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}instr", "PAGE")
    footer._p.append(field)
    for run in footer.runs:
        run.font.size = Pt(9)
    d.core_properties.language = "de-DE"
    d.core_properties.author = org
    d.core_properties.last_modified_by = org
    d.core_properties.title = title
    d.core_properties.created = datetime(2026, 9, 23, 8)
    d.core_properties.modified = datetime(2026, 9, 23, 8)
    d.save(path)


def fonts():
    paths = [Path(os.environ.get("AKTEN_FONT_DIR", "/Library/Fonts")), Path("/System/Library/Fonts/Supplemental")]
    for base in paths:
        regular, bold = base / "Times New Roman.ttf", base / "Times New Roman Bold.ttf"
        if regular.exists() and bold.exists():
            pdfmetrics.registerFont(TTFont("AktenTimes", str(regular)))
            pdfmetrics.registerFont(TTFont("AktenTimesBold", str(bold)))
            pdfmetrics.registerFontFamily("AktenTimes", normal="AktenTimes", bold="AktenTimesBold")
            return "AktenTimes", "AktenTimesBold"
    return "Times-Roman", "Times-Bold"


FONT, BOLD = fonts()


def pdf(path, org, title, meta, paragraphs, table=None, after=(), terms_on_new_page=False):
    style = ParagraphStyle("body", fontName=FONT, fontSize=11, leading=14, spaceAfter=8)
    small = ParagraphStyle("table", parent=style, fontSize=10, leading=12, spaceAfter=0)
    heading = ParagraphStyle("title", parent=style, fontName=BOLD, fontSize=16, leading=19, spaceAfter=14)
    section = ParagraphStyle("section", parent=style, fontName=BOLD, spaceBefore=5, spaceAfter=8, keepWithNext=True)
    p = lambda text, s=style: Paragraph(escape(str(text)).replace("\n", "<br/>"), s)
    def flow(text):
        first, sep, body = text.partition("\n")
        if sep and re.match(r"^\d+\.\s", first):
            return [p(first, section), p(body)]
        return [p(text)]
    story = [p(org, ParagraphStyle("org", parent=style, fontName=BOLD)), p(CONTACT.get(org, "")), Spacer(1, 8), p(title, heading)]
    story += [p(f"{key}: {value}") for key, value in meta]
    story += [Spacer(1, 7)]
    for text in paragraphs:
        story.extend(flow(text))
    if table:
        headers, rows, widths = table
        tab = Table([[p(c, small) for c in row] for row in [headers] + rows], colWidths=[w * mm for w in widths], repeatRows=1, hAlign="LEFT")
        tab.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#eceff1")),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ("TOPPADDING", (0, 0), (-1, -1), 7),
            ("LINEBELOW", (0, 0), (-1, 0), .5, colors.grey),
            ("LINEBELOW", (0, -1), (-1, -1), .5, colors.grey),
        ]))
        story += [tab, Spacer(1, 10)]
    if terms_on_new_page:
        story.append(PageBreak())
    for text in after:
        story.extend(flow(text))
    def footer(canvas, document):
        canvas.setFont(FONT, 9)
        canvas.drawString(22 * mm, 13 * mm, org)
        canvas.drawRightString(188 * mm, 13 * mm, f"Seite {document.page}")
    SimpleDocTemplate(str(path), pagesize=A4, rightMargin=22*mm, leftMargin=22*mm, topMargin=19*mm, bottomMargin=22*mm, title=title, author=org).build(story, onFirstPage=footer, onLaterPages=footer)


def eml(path, sender, to, date, subject, body, cc=None, attachments=(), reply=None):
    m = EmailMessage(policy=SMTP)
    m["From"], m["To"], m["Subject"] = sender, to, subject
    if cc:
        m["Cc"] = cc
    m["Date"] = format_datetime(datetime.fromisoformat(date))
    ident = f"<{path.stem}@{sender.split('@')[-1].rstrip('>')}>"
    m["Message-ID"] = ident
    if reply:
        m["In-Reply-To"] = reply
        m["References"] = reply
    m["MIME-Version"] = "1.0"
    m["Content-Language"] = "de-DE"
    m.set_content(body.strip() + "\n", charset="utf-8")
    for name in attachments:
        f = path.parent / name
        subtype = {".docx": "vnd.openxmlformats-officedocument.wordprocessingml.document", ".pdf": "pdf", ".xlsx": "vnd.openxmlformats-officedocument.spreadsheetml.sheet", ".csv": "octet-stream"}[f.suffix]
        m.add_attachment(f.read_bytes(), maintype="application", subtype=subtype, filename=f.name)
    path.write_bytes(m.as_bytes())


def csv_file(path, headers, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(headers)
        writer.writerows(rows)


def dortmund():
    d = ROOT / "testakten" / DORTMUND
    d.mkdir(parents=True, exist_ok=True)
    docx(d / "01_firmenbogen_und_zugaenge.docx", K, "Firmenbogen und Zugangsübersicht", [("Stand", "21.09.2026"), ("Geführt von", "Maren Fink, Büro und Buchhaltung"), ("Kundennummer bei Netzraum", "KD-1048")], [
        ("1. Betrieb und Ansprechpartner", ["Unsere Geschäftsführerin ist Jana Römer, einzelvertretungsberechtigt. Neben ihr beschäftigen wir sieben Personen: zwei im Verkauf, drei in der Werkstatt, eine im Versand und eine im Büro. Sitz und Werkstatt sind in der Lindemannstraße 41. Die Umsatzsteuer-ID lautet DE358214697. Frau Römer zeichnet Verträge; Maren Fink bearbeitet Rechnungen, Tom Bremer pflegt Artikel und Bestellungen im Webshop."]),
        ("2. Konten und Datenbestände", ["Der Webshop und das Kundenportal unter shop.kettenlicht-fahrradhandel.de laufen seit 02.04.2024 bei Netzraum. Der Vertragspartner heißt Netzraum Digital OHG; Ansprechpartner für Technik ist Nils Böttcher, für Preise Felix Sander. Beide sind laut ihrem Firmenbogen einzeln zur Vertretung berechtigt. Unser Domainkonto liegt auf Jana Römers Firmenadresse. Zugang zum Domainkonto und zur Warenwirtschaft ist vorhanden, ein Datenbankzugang wurde uns nicht eingerichtet.", "Tom hat die Rolle Shop-Admin, Maren die Rolle Abrechnung. Das Portal zeigt 1.284 Kundenkonten, 3.612 Bestellungen und 417 aktive Marketingeinträge. Die Werte stammen aus dem Bildschirm vom 21.09., nicht aus einem heruntergeladenen Bestand. In der Warenwirtschaft liegen nur Rechnungsnummern, Artikel und Beträge; Nachrichten aus dem Kundenportal werden dort nicht gespeichert."]),
        ("3. Letzte Ablage", ["Im Vertragsordner liegen die E-Mail vom 18.01.2024, das Leistungsblatt 1.2, der Vertragsentwurf 0.9 und die AV-Anlage 1.1. Eine Datei mit Unterschriften unter dem Vertragsentwurf oder der AV-Anlage habe ich im gemeinsamen Laufwerk nicht gefunden. Nils Böttcher hat am 17.09.2026 eine AV-Anlage 1.4 nachgesandt. Das Schreiben liegt unter Nummer 18, die Anlage unter Nummer 19."])
    ], "Maren Fink\nBüro und Buchhaltung")
    docx(d / "03_vertragsentwurf_2024_v09.docx", N, "Vertrag über Webshop und Kundenportal", [("Dokumentstand", "Entwurf 0.9 vom 16.01.2024"), ("An", K + ", zu Händen Jana Römer"), ("Projekt", "KL-Shop / KD-1048")], [
        ("1. Leistungsgegenstand", ["Netzraum richtet für Kettenlicht einen Webshop mit Kundenkonto, Bestellhistorie und Nachrichtenfunktion ein. Inhalt und Schnittstellen richten sich nach dem technischen Leistungsblatt 1.2 vom 16.01.2024. Kettenlicht liefert Artikelstammdaten, Bilder, Preislisten und Versandregeln. Weitere Schnittstellen werden nur nach gesonderter Abstimmung eingerichtet."]),
        ("2. Einrichtung und Übergabe", ["Die Einrichtung kostet insgesamt 9.000,00 EUR netto. 4.500,00 EUR netto werden bei Projektbeginn, 4.500,00 EUR netto nach produktiver Bereitstellung berechnet. Netzraum stellt eine Vorschau bereit. Kettenlicht meldet bei der gemeinsamen Durchsicht erkannte Abweichungen innerhalb von zehn Arbeitstagen. Nicht zum Leistungsblatt gehörende Wünsche werden vor Umsetzung bepreist."]),
        ("3. Betrieb", ["Ab Produktivstart berechnet Netzraum monatlich 450,00 EUR netto für Hosting, Sicherung, Updates und das im Leistungsblatt bezeichnete Supportfenster. Die Vergütung wird jeweils zu Monatsbeginn mit zehn Tagen Zahlungsziel berechnet. Umsatzsteuer wird gesondert ausgewiesen. Ein zusätzlicher Entwicklungsauftrag wird nach Angebot oder nach freigegebenem Stundenumfang berechnet."]),
        ("4. Verfügbarkeit und Störungsmeldung", ["Netzraum überwacht den Webdienst alle fünf Minuten. Geplante Wartung wird möglichst zwei Arbeitstage vorher angekündigt. Störungen meldet Kettenlicht an service@netzraum-digital.de. Netzraum bestätigt Meldungen innerhalb von vier Stunden während des Supportfensters. Eine feste Wiederherstellungszeit wird in dieser Fassung nicht zugesagt."]),
        ("5. Daten und technische Komponenten", ["Kettenlicht kann eigene Artikel-, Kunden- und Bestelldaten über die vorgesehenen Oberflächen abrufen. Netzraum behält die wiederverwendbaren Programmbibliotheken, die Orchestrierung und mandantenübergreifende Systemkonfiguration. Bei Vertragsende erstellt Netzraum auf Anforderung einen Standardexport der Kettenlicht-Daten in CSV sowie der hochgeladenen Medien in einem Archiv. Anpassungen für ein fremdes Zielsystem bedürfen eines gesonderten Angebots."]),
        ("6. Offene Rechnungen", ["Bei seit mehr als zehn Tagen nach Fälligkeit offenen Beträgen kann Netzraum nach schriftlicher Erinnerung neue Entwicklungsleistungen aussetzen. Für den abschließenden Datenexport sieht Netzraum in diesem Entwurf eine Freigabe nach Ausgleich aller Projektforderungen vor. Die laufende Datensicherung wird während einer solchen Aussetzung fortgesetzt."]),
        ("7. Laufzeit und Wechsel", ["Der Betrieb beginnt am Tag des Produktivstarts und läuft zunächst zwölf Monate. Danach verlängert er sich jeweils um einen Monat, sofern nicht mit vier Wochen zum Monatsende gekündigt wird. Nach Ende des Betriebs hält Netzraum den letzten Datenbestand für dreißig Tage in einem gesperrten Übergabebereich vor. Ein längerer Parallelbetrieb muss gesondert bestellt werden."]),
        ("8. Datenverarbeitung und Abschluss", ["Die AV-Anlage 1.1 wird gesondert abgestimmt. Änderungen des Hostingstandorts teilt Netzraum der benannten Kontaktperson mit. Dieser Entwurf wird zur Durchsicht versandt; mit der E-Mail-Übermittlung wird keine Unterschrift erklärt. Die Unterschriftsfelder bleiben bis zur Abstimmung des Exportabschnitts und der AV-Anlage frei.", "Für Kettenlicht: ____________________   Datum: ____________________\nFür Netzraum: ____________________   Datum: ____________________"])
    ])
    docx(d / "04_av_anlage_2024_v11.docx", N, "Anlage zur Verarbeitung der Shopdaten", [("Fassung", "1.1 vom 16.01.2024, zur Abstimmung"), ("Projekt", "KD-1048"), ("Parteien", K + " und " + N)], [
        ("1. Umfang", ["Netzraum verarbeitet für den Betrieb des Shops Kundenstammdaten, Liefer- und Rechnungsadressen, Bestellpositionen, Zahlungsstatus, Portalnachrichten und Marketingpräferenzen. Kreditkartennummern werden im Shop nicht gespeichert. Die Verarbeitung erfolgt für die Dauer des Shopbetriebs und der vereinbarten Rückgabephase. Kettenlicht bestimmt die Inhalte der Kundenkommunikation und benennt die Benutzer mit Verwaltungsrechten."]),
        ("2. Zugriff und Weisungen", ["Weisungen erteilen Jana Römer und eine von ihr benannte Vertretung per E-Mail. Netzraum setzt benutzerbezogene Zugänge, verschlüsselte Übertragung und tägliche Sicherungen ein. Administrative Zugriffe werden mit Benutzer, Zeitpunkt und Vorgangsnummer protokolliert. Mitarbeiter erhalten Zugang nur für ihre betreuten Projekte und werden zur Vertraulichkeit verpflichtet."]),
        ("3. Unterauftrag und Standort", ["Für virtuelle Server und Sicherungsspeicher wird Serverhain Rechenzentrum GmbH, Hanauer Landstraße 291, 60314 Frankfurt am Main, eingesetzt. Der Hauptbestand und die nächtlichen Sicherungen liegen in Frankfurt am Main. Weitere Dienstleister und Standortwechsel teilt Netzraum vor ihrer Einrichtung per E-Mail mit; Kettenlicht kann binnen vierzehn Tagen Einwendungen mitteilen."]),
        ("4. Anfragen und Vorfälle", ["Anfragen von Kunden leitet Netzraum an die Kontaktperson bei Kettenlicht weiter. Auf deren Weisung stellt Netzraum die zum jeweiligen Konto vorhandenen Daten zusammen und ändert oder entfernt die bezeichneten Einträge. Störungen mit möglichem Verlust oder unbefugtem Zugriff meldet Netzraum unverzüglich mit den zu diesem Zeitpunkt bekannten Angaben. Fehlende Einzelheiten werden nachgereicht."]),
        ("5. Rückgabe und Sicherungen", ["Nach Ende der Verarbeitung werden die Daten nach Wahl von Kettenlicht zurückgegeben oder im aktiven System gelöscht. Umlaufende Sicherungen werden nach spätestens dreißig Tagen überschrieben und bis dahin nicht für den laufenden Betrieb genutzt. Eine Rücksicherung wird dokumentiert. Netzraum gibt auf Anfrage Auskunft über die eingerichteten Zugänge und Sicherungsläufe.", "Rückmeldung Kettenlicht zur Fassung 1.1: noch ausstehend. Unterzeichnete Ausfertigungen liegen diesem Dokument nicht bei."])
    ])
    pdf(d / "05_leistungsblatt_2024_v12.pdf", N, "Technisches Leistungsblatt KL-Shop", [("Stand", "16.01.2024 / Revision 1.2"), ("Angebot", "ND-24-0118"), ("Geplanter Start", "02.04.2024")], ["1. Produktivsystem\nEin Shopmandant mit bis zu 5.000 Artikeln, Kundenkonto, Nachrichtenpostfach und Bestellhistorie. Ein nächtlicher Import übernimmt Artikel und Lagerstände aus der Warenwirtschaft. Bestellungen werden nach erfolgreicher Zahlung an die Warenwirtschaft übertragen. Nachrichten bleiben im Portal.", "2. Betrieb\n450,00 EUR netto monatlich umfassen einen virtuellen Server, 80 GB Speicher, tägliche Sicherung mit dreißig Tagen Umlauf, Sicherheitsupdates sowie Support montags bis freitags von 9 bis 17 Uhr. Außerhalb dieses Fensters werden Meldungen gesammelt. Die technische Überwachung läuft durchgehend."], (["Funktion", "Umfang", "Zugang"], [["Kunden und Bestellungen", "CSV, UTF-8; eindeutige Konto- und Bestellnummern", "Shop-Admin"], ["Portalnachrichten", "JSON mit Konto, Zeitstempel und Nachrichtentext", "Serviceanforderung"], ["Bilder und Dateien", "ZIP mit Verzeichnisstruktur", "Serviceanforderung"], ["Sicherung", "Täglich 02:00 Uhr; Rücksicherung nach Ticket", "Betriebsteam"], ["Konfiguration", "Mandantenparameter und gemeinsame Laufzeitumgebung", "Betriebsteam"]], [40, 86, 40]), ["3. Einrichtung\nDie einmaligen 9.000,00 EUR netto decken Gestaltung, Einrichtung eines Warenwirtschaftsmandanten, Import der vorhandenen Artikel und eine zweistündige Einweisung. Ein zweiter Testmandant und spätere Datenbereinigungen sind nicht enthalten. Die Exportfelder werden während der Einweisung gezeigt; eine direkte Datenbankverbindung für Kettenlicht ist nicht vorgesehen."])
    eml(d / "02_auftrag_per_email_2024.eml", "Jana Römer <jana.roemer@kettenlicht-fahrradhandel.de>", "Felix Sander <felix.sander@netzraum-digital.de>", "2024-01-18T10:14:00+01:00", "KL-Shop / Beauftragung ND-24-0118", """Guten Morgen Herr Sander,

bitte beginnen Sie auf Grundlage Ihres Angebots ND-24-0118 und des technischen Leistungsblatts 1.2. Die Einrichtung für 9.000 EUR netto in zwei gleichen Raten sowie der Betrieb ab Start für 450 EUR netto im Monat passen. Den ersten Artikelbestand liefert Tom am Montag. Der gewünschte Produktivstart bleibt der 2. April.

Den Vertrag 0.9 habe ich gelesen, aber nicht unterschrieben. Zu Ziffer 6 möchte ich noch besprechen, dass wir unsere Bestellungen auch bei einer strittigen Zusatzrechnung erhalten. Bitte lassen Sie diesen Punkt und die AV-Anlage bis zu unserem Termin offen. Meine heutige Zusage betrifft die genannten Leistungen und Preise, nicht die noch zu besprechenden Texte. Ich sende Ihre drei Dateien zur eindeutigen Zuordnung mit zurück.

Freundliche Grüße
Jana Römer
Geschäftsführerin
Kettenlicht Fahrradhandel GmbH
Lindemannstraße 41, 44137 Dortmund
Telefon 0231 580 62 40
Amtsgericht Dortmund HRB 34718""", cc="Tom Bremer <tom.bremer@kettenlicht-fahrradhandel.de>", attachments=["03_vertragsentwurf_2024_v09.docx", "04_av_anlage_2024_v11.docx", "05_leistungsblatt_2024_v12.pdf"])
    for num, invoice, date, description, due in [(6,"ND-2024-021","19.01.2024","Erste Einrichtungsrate bei Projektbeginn","29.01.2024"), (7,"ND-2024-119","03.04.2024","Zweite Einrichtungsrate nach Produktivstart am 02.04.2024","13.04.2024")]:
        pdf(d / f"{num:02d}_rechnung_einrichtung_{1 if num == 6 else 2}.pdf", N, "Rechnung " + invoice, [("Rechnungsdatum",date),("Kunde",K + ", Lindemannstraße 41, 44137 Dortmund"),("Kundennummer","KD-1048"),("Umsatzsteuer-ID","DE349716285")], [description + ". Bezug: ND-24-0118, Gesamtpreis Einrichtung 9.000,00 EUR netto."], (["Leistung", "Netto EUR", "USt 19 % EUR", "Brutto EUR"], [[description,"4.500,00","855,00","5.355,00"]], [76,30,30,30]), ["Zahlbar bis " + due + " ohne Abzug. Empfänger: Netzraum Digital OHG. Bankverbindung endet auf 4819. Bitte verwenden Sie Rechnungsnummer und KD-1048.", "Der monatliche Betrieb ab April wird separat berechnet."])
    pdf(d / "08_kontobeleg_einrichtungsraten.pdf", "Ruhrbogen Bank eG", "Umsatzanzeige Geschäftskonto", [("Kontoinhaberin",K),("Konto","Geschäftskonto, Endziffern 2096"),("Abruf","21.09.2026, 11:02 Uhr"),("Filter","Empfänger Netzraum / Verwendungszweck ND-2024-021 oder ND-2024-119")], ["Die folgende Anzeige enthält die beiden zum Filter passenden gebuchten Umsätze. Sie ist kein vollständiger Kontoauszug. Auftragsstatus jeweils ausgeführt."], (["Buchung / Valuta","Empfänger und Verwendungszweck","Belastung EUR"], [["25.01.2024 / 25.01.2024","Netzraum Digital OHG\nND-2024-021 / KD-1048\nReferenz RB240125-1862","5.355,00"],["10.04.2024 / 10.04.2024","Netzraum Digital OHG\nND-2024-119 / KD-1048\nReferenz RB240410-0941","5.355,00"]],[39,95,32]), ["Summe der angezeigten Belastungen: 10.710,00 EUR. Empfängerkonto bei beiden Buchungen: Endziffern 4819."])
    eml(d / "09_angebot_zusatzarbeiten.eml", "Felix Sander <felix.sander@netzraum-digital.de>", "Jana Römer <jana.roemer@kettenlicht-fahrradhandel.de>", "2026-08-24T15:26:00+02:00", "KD-1048 / zweiter Warenwirtschaftsmandant und Importbereinigung", """Guten Tag Frau Römer,

für den von Tom gewünschten zweiten Warenwirtschaftsmandanten auf der Testumgebung rechnen wir mit einmalig 800 EUR netto. Darin sind die neue Verbindung, ein eigener Schlüssel und ein Probelauf enthalten. Das ist nicht die Einrichtung des Produktivshops aus 2024.

Die Zusammenführung der alten Artikelnummern und Dubletten ist gesonderte Handarbeit. Wir schätzen zwölf Stunden zu 125 EUR netto, mithin 1.500 EUR netto. Wir können zunächst vier Stunden einsetzen und danach sagen, wie viele Datensätze noch offen sind. Ein zusätzlicher Dauerbetrieb wird für die Testumgebung bis Ende Oktober nicht berechnet; die 450 EUR für den Produktivbetrieb bleiben unverändert.

Geplant sind Einrichtung am 1. September und Bereinigung am 2. bis 4. September. Bitte teilen Sie uns mit, welchen Umfang wir einplanen dürfen. Die Abrechnung erfolgt zusammen mit dem Septemberbetrieb. Einen Komplettwechsel zu einem anderen Shopsystem enthält dieses Angebot nicht.

Viele Grüße
Felix Sander
Gesellschafter, Netzraum Digital OHG
Rheinische Straße 168, 44147 Dortmund
Telefon 0231 971 43 20
Amtsgericht Dortmund HRA 19342""", cc="Tom Bremer <tom.bremer@kettenlicht-fahrradhandel.de>")
    eml(d / "10_antwort_freigabe_zusatzarbeiten.eml", "Jana Römer <jana.roemer@kettenlicht-fahrradhandel.de>", "Felix Sander <felix.sander@netzraum-digital.de>", "2026-08-25T09:18:00+02:00", "Re: KD-1048 / zweiter Warenwirtschaftsmandant und Importbereinigung", """Hallo Herr Sander,

die 800 EUR für die zweite Verbindung gebe ich frei. Bei der Bereinigung bitte erst vier Stunden zu 125 EUR einsetzen. Danach brauche ich die Liste der noch offenen Dubletten und eine Rückmeldung, bevor weitere Stunden entstehen. Tom kann während meiner Messetage einzelne Artikelzuordnungen erklären. Er gibt damit keine weiteren Stunden frei.

Die Trennung vom bezahlten Einrichtungsprojekt 2024 ist für Maren wichtig. Bitte auf der Rechnung die neue Verbindung und die Bereinigungsstunden getrennt aufführen. Wir brauchen den Testmandanten für die Inventur, nicht für einen zusätzlichen öffentlichen Shop.

Danke und freundliche Grüße
Jana Römer
Geschäftsführerin, Kettenlicht Fahrradhandel GmbH
Telefon 0231 580 62 40""", cc="Maren Fink <maren.fink@kettenlicht-fahrradhandel.de>, Tom Bremer <tom.bremer@kettenlicht-fahrradhandel.de>", reply="<09_angebot_zusatzarbeiten@netzraum-digital.de>")
    pdf(d / "11_rechnung_nd_2026_388.pdf", N, "Rechnung ND-2026-388", [("Datum","07.09.2026"),("Empfänger",K + ", Lindemannstraße 41, 44137 Dortmund"),("Kundennummer","KD-1048"),("Umsatzsteuer-ID","DE349716285"),("Fälligkeit","17.09.2026 ohne Abzug")], ["Abrechnung für September und Zusatzauftrag vom August. Die ursprüngliche Einrichtung 2024 ist nicht Gegenstand dieser Rechnung."], (["Position und Leistungszeit", "Menge", "Einzel netto EUR", "Netto EUR"], [["1 Betrieb 01. bis 30.09.2026", "1 Monat", "450,00", "450,00"], ["2 Einrichtung zweiter Warenwirtschaftsmandant, 01.09.2026", "1", "800,00", "800,00"], ["3 Importbereinigung Artikelnummern, 02. bis 04.09.2026", "12 Std.", "125,00", "1.500,00"], ["Summe netto", "", "", "2.750,00"], ["Umsatzsteuer 19 %", "", "", "522,50"], ["Rechnungsbetrag", "", "", "3.272,50"]], [82,22,30,32]), ["Zeitbuchungen zu Position 3: 02.09. 09:00 bis 13:00 Uhr vier Stunden; 03.09. 10:00 bis 15:00 Uhr fünf Stunden; 04.09. 09:00 bis 12:00 Uhr drei Stunden. Bearbeitung: Nils Böttcher. Rückfragevermerk am 03.09.: Artikelzuordnung telefonisch mit Tom Bremer.", "Empfänger Netzraum Digital OHG, Bankverbindung Endziffern 4819. Verwendungszweck ND-2026-388 / KD-1048."])
    events = [
        ["2026-09-09T08:10:00+02:00","ND-6721","Monitoring","Web und Portal","HTTP 503; erste negative Prüfung","offen"],
        ["2026-09-09T08:17:00+02:00","ND-6721","Tom Bremer","Telefon","Kunden melden leeren Warenkorb; Portal nicht erreichbar","offen"],
        ["2026-09-09T09:04:00+02:00","ND-6721","Nils Böttcher","Support","Meldung bestätigt; Datenbankvolume nicht eingebunden","in Arbeit"],
        ["2026-09-09T11:32:00+02:00","ND-6721","Betrieb","Host","Neustart ohne dauerhaften Erfolg; Dateisystemprüfung","in Arbeit"],
        ["2026-09-09T16:48:00+02:00","ND-6721","Jana Römer","E-Mail","Sieben telefonisch angenommene Bestellungen separat notiert","in Arbeit"],
        ["2026-09-10T09:15:00+02:00","ND-6721","Betrieb","Sicherung","Sicherung vom 09.09. 02:00 Uhr lesbar; Kopie begonnen","in Arbeit"],
        ["2026-09-10T14:26:00+02:00","ND-6721","Nils Böttcher","Support","Kein Hinweis auf Anmeldung fremder Konten in sichtbaren Zugriffslogs","in Arbeit"],
        ["2026-09-11T10:08:00+02:00","ND-6721","Betrieb","Datenbank","Neuaufbau auf Ersatzvolume; Bestellqueue noch gesperrt","in Arbeit"],
        ["2026-09-11T17:42:00+02:00","ND-6721","Tom Bremer","Kontrolle","Produktvorschau erreichbar; Kundenanmeldung weiter 503","in Arbeit"],
        ["2026-09-12T08:10:00+02:00","ND-6721","Monitoring","Web und Portal","Erster vollständiger grüner Bestell- und Loginlauf","beobachtet"],
        ["2026-09-12T09:03:00+02:00","ND-6721","Tom Bremer","Kontrolle","Bestellung KL-3612 und Nachrichten sichtbar; keine Vollzählung","beobachtet"],
        ["2026-09-14T10:12:00+02:00","ND-6764","Jana Römer","E-Mail","Datenübergabe für Dienstleisterwechsel angefragt","offen"],
        ["2026-09-16T14:05:00+02:00","ND-6764","Felix Sander","Abrechnung","Exportfreigabe bis Zahlung ND-2026-388 angehalten","wartet"],
        ["2026-09-18T12:42:00+02:00","ND-6782","Maren Fink","Support","Konto K-00817; Datenzusammenstellung und Marketinglöschung angefragt","offen"],
        ["2026-09-21T10:43:18+02:00","ND-6764","Tom Bremer","Admin","Exportjob EXP-260921-1043: EXPORT_ACCOUNT_HOLD","wartet"],
        ["2026-09-22T14:10:00+02:00","ND-6782","Nils Böttcher","Support","Marketingkennzeichen am 18.09. aus Versand genommen; Löschlauf noch offen","in Arbeit"],
    ]
    csv_file(d / "12_supporttickets_september.csv", ["Zeitpunkt","Ticket","Urheber","Kanal","Eintrag","Status"], events)
    eml(d / "13_wechsel_und_exportwunsch.eml", "Jana Römer <jana.roemer@kettenlicht-fahrradhandel.de>", "Felix Sander <felix.sander@netzraum-digital.de>", "2026-09-14T10:12:00+02:00", "KL-Shop / Wechsel und vollständiger Datenbestand", """Guten Tag Herr Sander,

von Mittwochmorgen bis Samstagmorgen konnten unsere Kunden drei Tage weder bestellen noch ihre Nachrichten lesen. Wir werden den Shop deshalb zu Ufercode Webbetrieb in Bochum verlegen. Frau Deniz Aydin dort hat für den 28. September einen Importtermin reserviert; ein neuer öffentlicher Shop ist für den 5. Oktober vorgesehen.

Bitte schicken Sie uns bis zum 24. September Kundenkonten, Bestellungen mit Positionen, Portalnachrichten und Medien. Frau Aydin braucht Feldbeschreibungen und die Zuordnung zwischen Konto und Bestellnummer. Zugangsdaten der Kunden sollen nicht unverschlüsselt versendet werden. Eine Übernahme Ihrer allgemeinen Programmbibliotheken ist nicht geplant. Sagen Sie bitte, was bei Nachrichtenanhängen technisch möglich ist und ob der laufende Shop während des Exports erreichbar bleibt.

Wir möchten den laufenden Betrieb zum 31. Oktober beenden und bis zum geprüften Import keine Daten gelöscht haben. Bitte bestätigen Sie den Termin. Zur Rechnung vom 7. September: Den 800-EUR-Aufbau erkenne ich als ausgeführte Arbeit wieder. Bei zwölf statt vier Stunden fehlt mir die Freigabe. Auch über den Septemberbetrieb nach diesem Ausfall müssen wir sprechen. Maren hat die Rechnung deshalb noch nicht angewiesen.

Freundliche Grüße
Jana Römer
Geschäftsführerin, Kettenlicht Fahrradhandel GmbH
Lindemannstraße 41, 44137 Dortmund
Telefon 0231 580 62 40""", cc="Maren Fink <maren.fink@kettenlicht-fahrradhandel.de>")
    csv_file(d / "15_dateiliste_netzraum_auszug.csv", ["Pfad","Kategorie","Format","Datensätze_oder_Dateien","Größe_Bytes","Stand","Exportstatus","Bemerkung"], [
        ["tenant1048/orders","Kundenbestellungen","CSV",3612,1873640,"2026-09-21T09:00:00+02:00","gesperrt","Bestellköpfe mit Konto-ID"],
        ["tenant1048/order_items","Kundenbestellungen","CSV",8940,2611050,"2026-09-21T09:00:00+02:00","gesperrt","Positionen; Verknüpfung order_id"],
        ["tenant1048/customers","Kundenkonten","CSV",1284,684210,"2026-09-21T09:00:00+02:00","gesperrt","Ohne Kennworthashes im Standardexport"],
        ["tenant1048/messages","Kundenkommunikation","JSON",218,312890,"2026-09-21T09:00:00+02:00","Serviceauftrag offen","Text und account_id; Anlagen gesondert"],
        ["tenant1048/message_uploads","Kundenkommunikation","ZIP",36,18631124,"2026-09-21T09:00:00+02:00","Serviceauftrag offen","Dateinamen mit message_id"],
        ["tenant1048/marketing","Marketing","CSV",417,98100,"2026-09-21T09:00:00+02:00","gesperrt","Aktive Einträge; ausgesetzte nicht mitgezählt"],
        ["tenant1048/media","Produktmedien","ZIP",684,918736400,"2026-09-21T09:00:00+02:00","gesperrt","Artikelbilder und Anleitungen"],
        ["runtime/shared/pipeline.yaml","Proprietäre Konfiguration","YAML",1,18210,"2026-09-16T18:10:00+02:00","nicht im Paket","Mandantenübergreifende Bereitstellung"],
        ["runtime/tenant1048/routing.enc","Proprietäre Konfiguration","BIN",1,9842,"2026-09-16T18:10:00+02:00","nicht im Paket","Schlüssel und interne Dienstadressen"],
    ])
    eml(d / "14_antwort_exportsperre.eml", "Felix Sander <felix.sander@netzraum-digital.de>", "Jana Römer <jana.roemer@kettenlicht-fahrradhandel.de>", "2026-09-16T14:05:00+02:00", "Re: KL-Shop / Wechsel und vollständiger Datenbestand", """Sehr geehrte Frau Römer,

wir haben den Wechselwunsch notiert. Den 31. Oktober kann ich nach Abgleich des Vertragskontos bestätigen; die Bestätigung sende ich noch. ND-2026-388 steht mit 2.750 EUR netto, 3.272,50 EUR brutto offen. Die beiden Einrichtungsraten aus 2024 sind bezahlt. Unsere Abrechnung betrifft den Septemberbetrieb, den zweiten Warenwirtschaftsmandanten und zwölf Stunden Bereinigung.

Nils hat nach den ersten vier Stunden mit Tom telefoniert und anschließend weitergearbeitet. Wir haben Toms Aussage, die restlichen Zuordnungen müssten bis Freitag fertig sein, als Fortsetzung verstanden. Den genauen Wortlaut hat er nicht mitgeschrieben.

Die Exportfreigabe bleibt bis zum Zahlungseingang gesperrt. Wir beziehen uns dafür auf Ziffer 6 unserer Vertragsfassung 0.9. Sie können weiterhin einzelne Bestellungen im Portal ansehen und ausdrucken. Eine Freischaltung nur der Bestelltabellen habe ich derzeit nicht veranlasst. Für die Serverkonfiguration geben wir keine Kopie heraus.

Ich kann am Montag eine begrenzte Dateiliste nachreichen. Sie wird Kundenbestellungen und unsere Konfiguration getrennt aufführen. Der Export der Nachrichten ist ein anderer Prozess als die Schaltfläche im Adminbereich. Bitte senden Sie noch die technische Adresse von Frau Aydin.

Freundliche Grüße
Felix Sander
Netzraum Digital OHG
Telefon 0231 971 43 20""", reply="<13_wechsel_und_exportwunsch@kettenlicht-fahrradhandel.de>")
    eml(d / "16_kundin_graefe_datenanfrage.eml", "Elisabeth Gräfe <elisabeth.graefe@graefe-postfach-dortmund.de>", "Kettenlicht Kundenservice <service@kettenlicht-fahrradhandel.de>", "2026-09-18T08:36:00+02:00", "Mein Kundenkonto K-00817 / Bestellungen, Nachrichten und Werbung", """Guten Morgen,

ich möchte bitte eine Kopie der zu meinem Konto gespeicherten Daten. Mich interessieren besonders meine drei Bestellungen, die Lieferanschriften und die Nachrichten zur Rückgabe der Packtasche. Die Bestellnummern, die ich noch finde, sind KL-2981 vom 12. April und KL-3449 vom 27. August. Die dritte Bestellung war 2024. Bitte schicken Sie auch mit, welche Angaben Sie für Werbung gespeichert haben und woher diese stammen.

Die Werbedaten, die Sie nicht mehr benötigen, sollen gelöscht werden. Ich möchte keinen Newsletter und keine Werbe-SMS mehr. Meine noch laufende Rückgabe soll dadurch nicht verschwinden. Für Rechnungen benötige ich weiterhin die Kopien. Falls Sie etwas nicht löschen, sagen Sie mir bitte, um welche Angaben es geht und weshalb Sie sie behalten.

Ich schreibe von der Adresse, mit der das Konto angelegt ist. Im Portal kann ich mich heute anmelden, finde aber nur die Bestellübersicht. Für die Rückgabe hatte ich am 29. August zwei Nachrichten und ein Foto geschickt. Eine Antwort per E-Mail an diese Adresse passt mir.

Viele Grüße
Elisabeth Gräfe
Kundennummer K-00817""")
    eml(d / "17_eingang_kundenanfrage.eml", "Maren Fink <service@kettenlicht-fahrradhandel.de>", "Elisabeth Gräfe <elisabeth.graefe@graefe-postfach-dortmund.de>", "2026-09-18T11:21:00+02:00", "Re: Mein Kundenkonto K-00817 / Bestellungen, Nachrichten und Werbung", """Guten Tag Frau Gräfe,

Ihre Nachricht ist angekommen. Ich habe die E-Mail-Adresse mit Ihrem Kundenkonto abgeglichen. Sie müssen uns dafür keine Ausweiskopie senden. Den Newsletterversand habe ich heute um 11:10 Uhr für Ihr Konto ausgesetzt. Eine Werbe-SMS-Nummer sehe ich in unserer Büroansicht nicht.

Wir stellen die Bestellungen, Nachrichten und Angaben zu den Werbeeinträgen zusammen. Den Nachrichtenanhang kann ich in meiner Ansicht öffnen, aber nicht zusammen mit den übrigen Daten herunterladen. Dazu habe ich unseren technischen Dienstleister eingeschaltet. Ich melde mich, sobald die Zusammenstellung vorliegt, und erläutere dann auch, welche Einträge entfernt wurden. Die Bearbeitung Ihrer Rückgabe läuft unabhängig davon weiter.

Freundliche Grüße
Maren Fink
Kundenservice, Kettenlicht Fahrradhandel GmbH
Lindemannstraße 41, 44137 Dortmund
Telefon 0231 580 62 40""", reply="<16_kundin_graefe_datenanfrage@graefe-postfach-dortmund.de>")
    docx(d / "19_av_anlage_2025_v14.docx", N, "Anlage zur Verarbeitung der Shopdaten", [("Fassung", "1.4 vom 01.07.2025"), ("Kundenzuordnung im Portal", "KD-1048, eingestellt am 01.07.2025"), ("Ausfertigung", "Download am 17.09.2026; keine Unterschriften")], [
        ("1. Gegenstand und Zugriff", ["Netzraum verarbeitet Kundenstammdaten, Bestellinformationen, Portalnachrichten und Marketingpräferenzen für den Betrieb des Kundenportals. Zugriffsrechte werden nach Aufgaben zugeteilt. Administrative Anmeldungen werden mit Zeitstempel protokolliert. Weisungen werden über die im Kundenkonto hinterlegte Geschäftsadresse entgegengenommen."]),
        ("2. Betriebsorte", ["Der Produktivbestand liegt bei Serverhain Rechenzentrum GmbH in Frankfurt am Main. Verschlüsselte nächtliche Sicherungen werden zusätzlich bei Europuffer Hosting B.V., Kabelweg 37, 1014 BA Amsterdam, Niederlande, gespeichert. Der Sicherungsstandort ist Amsterdam. Die Schlüsselverwaltung und Wiederherstellung erfolgen durch Netzraum in Dortmund. Die Bereitstellung dieser Unterauftragnehmerliste erfolgt im Kundenportal."]),
        ("3. Änderungen und Unterstützung", ["Neue Unterauftragnehmer werden mindestens sieben Tage vor Zuschaltung im Portal angekündigt. Einwände sind an die Serviceadresse von Netzraum zu senden. Netzraum unterstützt Kettenlicht bei kundenspezifischen Datenzusammenstellungen, Berichtigungen und Löschungen anhand der Konto-ID. Jede Bearbeitung wird im Supportticket dokumentiert. Ereignisse mit möglichem Verlust oder fremdem Zugriff werden an die Geschäftsadresse gemeldet."]),
        ("4. Rückgabe und Aufbewahrung", ["Nach Vertragsende erstellt Netzraum einen Rückgabestand in den angebotenen Exportformaten. Die aktive Datenbank wird nach Bestätigung der Übernahme gelöscht. Sicherungsstände werden nach spätestens neunzig Tagen überschrieben. Bis dahin dürfen sie nur zur Wiederherstellung genutzt werden; bereits ausgeführte Löschungen werden nach einer Wiederherstellung erneut eingespielt.", "Diese Fassung ersetzt im Kundenportal die Fassung 1.1. Ein gesonderter Empfangsvermerk der Kettenlicht Fahrradhandel GmbH ist im Dokument nicht eingetragen."])
    ])
    eml(d / "18_email_sicherungsstandort_av_version.eml", "Nils Böttcher <nils.boettcher@netzraum-digital.de>", "Maren Fink <maren.fink@kettenlicht-fahrradhandel.de>", "2026-09-17T16:44:00+02:00", "KD-1048 / Sicherungsort und AV-Fassung im Portal", """Hallo Frau Fink,

anbei die AV-Anlage, die unser Portal seit Juli 2025 für KD-1048 führt. Die Frankfurter Produktivumgebung ist unverändert. Die zweite Sicherung liegt seit 15. Juli 2025 bei Europuffer Hosting B.V. in Amsterdam. Zugriff erfolgt durch unser Dortmunder Betriebsteam; der Speicher wird in Amsterdam betrieben.

Sie hatten die Version 1.1 mit dreißig Tagen genannt. In der aktuellen Datei stehen neunzig Tage. Ich kann aus der Portalhistorie sehen, wann wir die Datei eingestellt haben, aber nicht, ob Frau Römer sie geöffnet hat. Eine unterschriebene neue Anlage habe ich nicht. Ob damals zusätzlich eine E-Mail herausging, muss Felix noch in seinem Postfach suchen.

Die Rücksicherung letzte Woche stammte vom 9. September, 02:00 Uhr. Die Bestellwarteschlange wurde vor Wiederöffnung abgearbeitet. Wir haben die sichtbaren Zugriffslogs durchgesehen; eine vollständige Untersuchung aller Komponenten liegt damit noch nicht vor.

Grüße
Nils Böttcher
Gesellschafter, Netzraum Digital OHG
Rheinische Straße 168, 44147 Dortmund
Telefon 0231 971 43 22""", attachments=["19_av_anlage_2025_v14.docx"])
    write_text(d / "20_rueckruf_felix_sander.txt", """Kettenlicht Fahrradhandel GmbH
Telefonnotiz / Rückruf zu ND-6764
21.09.2026, 15:05 bis 15:18 Uhr
Aufgenommen unmittelbar danach: Jana Römer
Gesprächspartner: Felix Sander, Durchwahl 0231 971 43 20

Herr Sander rief auf meine Mailboxnachricht von 13:42 Uhr zurück. Ich habe gesagt, dass der Importtermin am 28. September ohne Bestellungen und Nachrichten nicht nutzbar ist. Er möchte eine Zahlung vor Freigabe des Exportjobs. Nach seiner Rechnung sind alle 3.272,50 EUR brutto offen.

Ich habe vorgeschlagen, zunächst die 800 EUR für die neue Verbindung und die ersten vier Stunden Bereinigung, insgesamt 1.300 EUR netto beziehungsweise 1.547 EUR brutto, nach Erhalt einer passenden Abrechnung zu zahlen. Über die weiteren Stunden und den Septemberbetrieb möchte ich noch sprechen. Eine Überweisung habe ich im Gespräch nicht zugesagt.

Herr Sander sagte, er könne vielleicht 2.000 EUR netto als erste Zahlung und den Rest nach dem Umzug vertreten. Er müsse das mit Nils besprechen. Die Nachrichten solle man separat betrachten; das würde sonst an der Exporttaste hängen bleiben. Er sagte nicht, wann das Paket fertig wäre. Ich habe keine Einigung bestätigt.

Zur Anfrage von Frau Gräfe habe ich Konto K-00817 genannt. Herr Sander will Nils fragen, ob der Einzelkontoauszug unabhängig vom Gesamtexport erzeugt werden kann. Ich habe um Rückruf am Dienstag gebeten.

Um 15:23 Uhr ging die angekündigte Dateiliste über das Ticketportal ein. Sie enthält neun Pfade, nicht den vollständigen Serverbestand. Ich habe sie als CSV abgelegt.
""")
    write_text(d / "21_chat_importtermin.txt", """Chat-Export / KL-Shop Umzug
Teilnehmer: Jana Römer (Kettenlicht), Tom Bremer (Kettenlicht), Deniz Aydin (Ufercode Webbetrieb)
Export durch Tom Bremer am 22.09.2026, 16:30 Uhr
Zeitzone: Europe/Berlin

22.09.2026 09:02 Deniz Aydin: Der Importslot am 28.09. von 9 bis 13 Uhr bleibt reserviert. Ich brauche bis Donnerstag ein kleines Datenpaket mit Feldnamen, sonst können wir nur die Artikel vorbereiten.
22.09.2026 09:06 Tom Bremer: Anbei kann ich noch nichts hochladen. Die Exporttaste meldet seit gestern Kontosperre. Einzelne Aufträge lassen sich ansehen.
22.09.2026 09:08 Deniz Aydin: Bitte keine Kundenbestellungen in diesen Chat kopieren. Wir richten einen Übertragungsordner mit zeitlich begrenztem Zugang ein.
22.09.2026 09:13 Jana Römer: Eine Dateiliste haben wir. Darin sind Bestellköpfe und Positionen getrennt. Nachrichten sind JSON und 36 Anhänge.
22.09.2026 09:18 Deniz Aydin: Das reicht als Beschreibung für meine Vorbereitung. Wir benötigen keine gemeinsame Laufzeitkonfiguration von Netzraum. Die Verknüpfung account_id zu order_id muss erhalten bleiben.
22.09.2026 09:24 Tom Bremer: Die Passwörter sind laut Liste nicht dabei.
22.09.2026 09:27 Deniz Aydin: Dann planen wir einen neuen Aktivierungslink für Kundenkonten. Nicht automatisch alte Hashes übernehmen. Den Text stimmt ihr bitte selbst ab.
22.09.2026 12:10 Jana Römer: Können wir am 5. Oktober starten, wenn der Export erst am 30. kommt?
22.09.2026 12:17 Deniz Aydin: Das kann ich noch nicht bestätigen. Am 1. und 2. Oktober ist das Team anderweitig gebunden. Ich kann den Slot vom 28. bis Donnerstagabend halten.
22.09.2026 15:56 Tom Bremer: Die 800 EUR in der Rechnung sind unser Testmandant, nicht ein Umzugsauftrag. Bei dem Telefonat am 3. September ging es darum, welche Artikelnummer zur Nabenschaltung gehört. Ich habe gesagt, die Liste müsse bis Freitag fertig werden. Einen Betrag haben wir nicht genannt.
22.09.2026 16:02 Jana Römer: Danke, ich habe von Herrn Sander eine andere Darstellung gehört. Bitte den alten Testmandanten noch nicht löschen.
""")
    admin_png(d / "22_admin_exportfehler_20260921.png")
    eml(d / "24_mandatsanfrage_jana_roemer.eml", "Jana Römer <jana.roemer@kettenlicht-fahrradhandel.de>", "Rechtsanwältin Miriam Lenz <kanzlei@lenz-kanzlei-dortmund.de>", "2026-09-23T09:12:00+02:00", "Mandatsanfrage / Kettenlicht und Netzraum / Datenzugang vor dem 28. September", """Sehr geehrte Frau Lenz,

über Herrn Seifert aus der Nachbarwerkstatt habe ich Ihre Adresse erhalten. Können Sie unsere Firma gegenüber Netzraum Digital OHG beraten und, wenn es zeitlich passt, die erste Kontaktaufnahme übernehmen? Wir sind ein Fahrradhandel mit sieben Beschäftigten und mir als Geschäftsführerin. Nach drei Tagen Shopausfall möchten wir den Dienstleister wechseln. Ohne den Datenexport verlieren wir voraussichtlich den reservierten Importtermin am kommenden Montag.

Die Einrichtung aus 2024 ist mit zweimal 4.500 EUR netto bezahlt. Offen ist die Rechnung über 2.750 EUR netto, die ich beifüge. Den zweiten Testmandanten für 800 EUR habe ich bestellt. Bei der Handarbeit waren zunächst vier Stunden abgesprochen, abgerechnet wurden zwölf. Netzraum verknüpft die Exportfreigabe mit vollständiger Zahlung. Bei den damaligen Vertragsdateien kann ich Ihnen nur Entwürfe und meine Beauftragungsmail geben; unterzeichnete Exemplare habe ich nicht gefunden.

Daneben wartet Frau Elisabeth Gräfe seit dem 18. September auf ihre eigenen Daten und die Entfernung von Werbeeinträgen. Ich möchte ihr ordentlich antworten und den Umzug nicht auf ihrem Rücken austragen. Ihre Anfrage und unsere Eingangsantwort liegen als E-Mail-Dateien für die Übertragung bereit. Netzraum hat inzwischen einen Sicherungsort in Amsterdam genannt, den ich aus unserer alten Anlage nicht kenne.

Ich kann heute von 12 bis 13 Uhr und ab 16 Uhr telefonieren. Bitte nennen Sie uns vorab die Bedingungen Ihrer Beauftragung und die voraussichtlichen Kosten für die erste Sichtung. Zahlungen oder einen endgültigen Vergleich möchte ich erst nach Rücksprache freigeben. Die übrigen Unterlagen kann Maren in Ihren Übertragungsordner einstellen. Die Daten von Frau Gräfe bitte nur für diese Angelegenheit verwenden.

Mit freundlichen Grüßen
Jana Römer
Geschäftsführerin, Kettenlicht Fahrradhandel GmbH
Lindemannstraße 41, 44137 Dortmund
Telefon 0231 580 62 40
Amtsgericht Dortmund HRB 34718""", attachments=["11_rechnung_nd_2026_388.pdf"])
    readme(d, "Datenzugang beim Wechsel des Shopdienstleisters in Dortmund", "anwaltschaft-generell", "Kettenlicht Fahrradhandel GmbH führt nach einem dreitägigen Ausfall Gespräche über den Wechsel ihres Webshops und Kundenportals. Netzraum Digital OHG verlangt vor der Exportfreigabe Zahlung einer Rechnung. Die Unterlagen reichen von der Beauftragung 2024 bis zum Schriftwechsel am 23. September 2026. Eine Kundin bittet um ihre Bestell- und Kommunikationsdaten sowie die Entfernung von Marketingeinträgen.", DORTMUND_FILES)


def admin_png(path):
    im = Image.new("RGB", (1440, 920), "#f5f6f7")
    draw = ImageDraw.Draw(im)
    fontpath = "/System/Library/Fonts/Supplemental/Arial.ttf"
    def f(size):
        return ImageFont.truetype(fontpath, size)
    draw.rectangle((0, 0, 1440, 60), fill="#e8ebee")
    draw.text((34, 19), "shop.kettenlicht-fahrradhandel.de/admin/export", fill="#323b42", font=f(20))
    draw.rectangle((0, 60, 240, 920), fill="#243e42")
    draw.text((26, 91), "KETTENLICHT", fill="white", font=f(23))
    for y, label in [(170,"Bestellungen"),(220,"Kunden"),(270,"Artikel"),(320,"Nachrichten"),(370,"Datenexport"),(420,"Einstellungen")]:
        if y == 370:
            draw.rectangle((12, y-9, 225, y+34), fill="#3d6569")
        draw.text((28, y), label, fill="white", font=f(20))
    draw.text((286, 97), "Datenexport", fill="#172b2f", font=f(34))
    draw.text((286, 151), "Mandant KD-1048   ·   Tom Bremer / Shop-Admin", fill="#4e5d63", font=f(20))
    draw.text((286, 207), "Bestellungen und Kundenkonten", fill="#24363b", font=f(24))
    for y, label, value in [(263,"Format","CSV / UTF-8"),(313,"Zeitraum","02.04.2024 bis 21.09.2026"),(363,"Bestellungen","3.612"),(413,"Kundenkonten","1.284")]:
        draw.text((286, y), label, fill="#56636a", font=f(20))
        draw.text((540, y), value, fill="#192b31", font=f(21))
    draw.rectangle((286, 485, 1370, 676), fill="#fae8e6", outline="#d19a93", width=1)
    draw.text((312, 512), "Export konnte nicht gestartet werden", fill="#842d25", font=f(27))
    draw.text((312, 564), "EXPORT_ACCOUNT_HOLD", fill="#842d25", font=f(21))
    draw.text((312, 603), "Die Exportfreigabe für Ihr Vertragskonto ist ausgesetzt.", fill="#503b38", font=f(21))
    draw.text((312, 638), "Bitte wenden Sie sich an den Support. Ticket ND-6764", fill="#503b38", font=f(21))
    draw.rectangle((286, 718, 566, 774), fill="#d3dadb")
    draw.text((315, 736), "Export erneut anfordern", fill="#3f5155", font=f(20))
    draw.text((286, 824), "Job EXP-260921-1043   ·   21.09.2026, 10:43:18 +02:00", fill="#5b686d", font=f(19))
    draw.text((286, 860), "Nachrichten und Anhänge: Bereitstellung über Serviceanforderung", fill="#5b686d", font=f(19))
    im.save(path)


DORTMUND_FILES = [
    ("01_firmenbogen_und_zugaenge.docx", "Firmenbogen, Ansprechpartner und Portalzugänge"),
    ("02_auftrag_per_email_2024.eml", "Beauftragung mit drei beigefügten Vertrags- und Leistungsdateien"),
    ("03_vertragsentwurf_2024_v09.docx", "Vertragsentwurf 0.9 vom Januar 2024"),
    ("04_av_anlage_2024_v11.docx", "AV-Anlage 1.1 zur Abstimmung"),
    ("05_leistungsblatt_2024_v12.pdf", "Technisches Leistungsblatt und Exportwege"),
    ("06_rechnung_einrichtung_1.pdf", "Erste Einrichtungsrate"),
    ("07_rechnung_einrichtung_2.pdf", "Zweite Einrichtungsrate"),
    ("08_kontobeleg_einrichtungsraten.pdf", "Gebuchte Überweisungen der beiden Raten"),
    ("09_angebot_zusatzarbeiten.eml", "Angebot Testmandant und Importbereinigung"),
    ("10_antwort_freigabe_zusatzarbeiten.eml", "Antwort zum freigegebenen Umfang"),
    ("11_rechnung_nd_2026_388.pdf", "Betrieb, weitere Einrichtung und Stundenabrechnung"),
    ("12_supporttickets_september.csv", "16 Ticketereignisse mit Zeitstempeln"),
    ("13_wechsel_und_exportwunsch.eml", "Wechselwunsch, Datenumfang und Zieltermine"),
    ("14_antwort_exportsperre.eml", "Antwort zur Rechnung und Exportfreigabe"),
    ("15_dateiliste_netzraum_auszug.csv", "Neun Pfade mit getrennten Datenkategorien"),
    ("16_kundin_graefe_datenanfrage.eml", "Kundenschreiben vom 18. September"),
    ("17_eingang_kundenanfrage.eml", "Eingangsantwort des Kundenservice"),
    ("18_email_sicherungsstandort_av_version.eml", "E-Mail mit AV-Anlage 1.4 als Anhang"),
    ("19_av_anlage_2025_v14.docx", "Im Portal hinterlegte AV-Fassung"),
    ("20_rueckruf_felix_sander.txt", "Telefonnotiz zum Rückruf am 21. September"),
    ("21_chat_importtermin.txt", "Chat zum Importtermin und Artikelabgleich"),
    ("22_admin_exportfehler_20260921.png", "Adminansicht des gesperrten Exportjobs"),
    ("23_rechnungs_leistungsabgleich.xlsx", "Rechnungspositionen, Stunden und Zahlungseingänge"),
    ("24_mandatsanfrage_jana_roemer.eml", "Anfrage an eine Rechtsanwältin"),
]


def readme(d, title, plugin, intro, files):
    rows = "\n".join(f"| [{name}]({name}) | {desc} |" for name, desc in files)
    write_text(d / "README.md", f"""<!-- decimal-headings -->
# 1. {title}

## 1. Gegenstand

{intro}

Passendes Plugin: [`{plugin}`](../../{plugin}/README.md).

## 2. Quellen

Die Akte umfasst {len(files)} eigenständige Quellen. In E-Mails beigefügte Kopien bereits separat aufgeführter Dokumente werden nicht zusätzlich gezählt. Die Tabellen enthalten editierbare Eingaben und berechnete Beträge. Stand der Unterlagen ist der 23. September 2026.

> {DISCLAIMER[0]}
>
> {DISCLAIMER[1]}

| Datei | Inhalt |
| --- | --- |
{rows}

## 3. Auswahl der Arbeitsfassung

Zum Lesen eignet sich das Gesamt-PDF. Für die Bearbeitung mit Tabellenformeln und E-Mail-Anhängen das Originalformat-ZIP wählen; das Einzel-PDF-ZIP enthält jede Unterlage getrennt. Die Links zu allen drei Fassungen stehen oben. Keine dieser Fassungen enthält eine Musterlösung.
""")


def aachen():
    d = ROOT / "testakten" / AACHEN
    d.mkdir(parents=True, exist_ok=True)
    docx(d / "01_lieferantenstamm_d400.docx", R, "Lieferantenstamm und Projektkontakte D400", [("Erfasst", "01.09.2026 von Eva Schulte, Einkauf"), ("Aktualisiert", "22.09.2026"), ("Projekt", "RK-Linie 7 / Sensor D400")], [
        ("1. Käufer", ["Rheinkern Anlagenbau GmbH, Jülicher Straße 318, 52070 Aachen, baut Montage- und Prüfanlagen. Die Gesellschaft hat 84 Beschäftigte. Geschäftsführer sind Dr. Leonhard Evers und Miriam Küppers, jeweils einzelvertretungsberechtigt. Die Umsatzsteuer-ID lautet DE329481756. Liefer- und Rechnungsanschrift sind identisch; Warenannahme ist Tor 2, montags bis freitags 7 bis 15 Uhr. Einkaufskontakt ist Eva Schulte, Durchwahl 0241 936 42 31, eva.schulte@rheinkern-anlagenbau.de."]),
        ("2. Lieferant", ["Talbruck Sensorik GmbH, Gewerbepark 17, 52249 Eschweiler, Lieferantennummer 70182. Geschäftsführer Henning Voß ist einzelvertretungsberechtigt. Umsatzsteuer-ID DE318642975, Amtsgericht Aachen HRB 22874. Vertriebskontakt ist Paul Reuter, paul.reuter@talbruck-sensorik.de, Durchwahl 02403 748 61 24. Qualität und Muster betreut Dr. Selma Berg, Durchwahl 02403 748 61 38. Das Lieferantenkonto für Werkzeugzahlungen endet auf 6842."]),
        ("3. Projektzugriffe und Zeichnung", ["Die kaufmännische Verhandlung führt Eva Schulte, die Messprüfung Anja Heil und die mechanische Integration Tobias Frings. Technische E-Mails aus diesen Bereichen werden im Projektordner abgelegt. Die Freigabe einer Serie erfolgt bei Rheinkern durch Qualitätsleitung und Einkauf gemeinsam. Tobias Frings kann Versuchsläufe organisieren, aber keine Jahresmengen oder Serienfreigaben unterschreiben.", "Das Werkzeug ist separat mit Bestellung RK-WZ-260828 bestellt. Im Rahmenvertrag sollen Lieferung, Abrufe und Bestandsführung für drei Jahre geregelt werden. Der aktuelle Entwurf ist noch nicht durch die Geschäftsführung gezeichnet. Im Bestellsystem ist D400 bis zur Serienfreigabe als projektgebundener Artikel geführt."])
    ], "Eva Schulte\nEinkauf")
    pdf(d / "02_angebot_ts_260902.pdf", T, "Angebot TS-260902", [("Datum", "02.09.2026"), ("An", R + ", Frau Eva Schulte"), ("Kundenreferenz", "RK-Linie 7 / D400"), ("Bindung des Angebots", "bis 25.09.2026")], ["Sehr geehrte Frau Schulte,\nwir bieten Ihnen den Distanzsensor D400 für Ihre Montageanlage an. Grundlage der technischen Ausführung ist unser Datenblatt Revision B vom 20.08.2026. Den Rahmenvertragsentwurf 0.6 übersenden wir gesondert zusammen mit diesem Angebot.", "1. Serienpreis\nDer Ausgangspreis beträgt 186,00 EUR netto je Stück bei Abrufen ab 100 Stück. Für eine feste Jahresmenge von 1.200 Stück bieten wir 3 % Nachlass auf alle in diesem Jahr abgenommenen Stücke, ab 1.800 fest zugesagten Stück 5 %. Ohne feste Jahreszusage gilt der Ausgangspreis. Abrufe unter 100 Stück tragen 8,00 EUR netto Rüstzuschlag je Stück. Die Jahresstaffel und der Rüstzuschlag werden getrennt berechnet."], (["Gegenstand", "Umfang", "Preis netto EUR"], [["D400, Revision B", "Stückpreis vor Staffel", "186,00"], ["Werkzeug WZ-D400-17", "Separate Bestellung RK-WZ-260828", "12.400,00"], ["Zwölf Versuchsmuster", "Einmalige Bemusterung aus Werkzeugauftrag", "im Werkzeugpreis"], ["Anlieferung", "DAP Jülicher Straße 318, Tor 2, 52070 Aachen, Incoterms 2020", "im Stückpreis"]], [43,93,30]), ["2. Anlauf\nDie ersten zwölf Versuchsmuster sollen bis zum 17. September eintreffen. Nach gemeinsamer Bestätigung der Messwerte planen wir den ersten Serienabruf am 19. Oktober. Ein zugesagter Serientermin setzt die Freigabe der technischen Ausführung bis zum 25. September voraus. Werkzeugfertigung und Musterauftrag laufen unabhängig von der Unterzeichnung des Rahmenvertrags.", "3. Zahlung\nSerienlieferungen sind binnen dreißig Tagen nach Rechnungseingang zu zahlen. Die Werkzeugrechnung wird entsprechend der gesonderten Bestellung fällig. Preise verstehen sich zuzüglich 19 % Umsatzsteuer. Eine automatische Verrechnung des Werkzeugpreises mit späteren Stückpreisen ist nicht vorgesehen.", "Freundliche Grüße\nPaul Reuter\nVertrieb, Talbruck Sensorik GmbH"], terms_on_new_page=True)
    docx(d / "03_rahmenvertrag_lieferant_v06.docx", T, "Rahmenliefervertrag für Sensoren D400", [("Verhandlungsstand", "Lieferantenentwurf 0.6 vom 02.09.2026"), ("Käufer", R + ", vertreten durch Miriam Küppers"), ("Lieferant", T + ", vertreten durch Henning Voß"), ("Projekt", "RK-Linie 7")], [
        ("1. Gegenstand und Dokumente", ["Talbruck liefert Rheinkern Distanzsensoren des Typs D400 für die Montageanlagen der Linie 7. Die Ausführung richtet sich nach Datenblatt Revision B vom 20.08.2026 und einer schriftlich vereinbarten späteren Revision. Angebot TS-260902 bildet die Preisgrundlage. Bei abweichenden technischen Angaben soll die zuletzt von beiden technischen Ansprechpartnern bestätigte Revision maßgeblich sein; eine bloße Übersendung eines Datenblatts ändert die Ausführung nicht."]),
        ("2. Laufzeit", ["Der Rahmen beginnt am 01.10.2026 und endet am 30.09.2029. Eine Fortführung bedarf einer neuen Vereinbarung. Vor dem Beginn ausgelöste Werkzeug- und Musterbestellungen bleiben gesonderte Aufträge. Bereits bestätigte Serienabrufe sind auch nach Ablauf des Rahmens zu erfüllen, wenn ihr Liefertermin innerhalb von acht Wochen nach dem Enddatum liegt."]),
        ("3. Jahresmenge und Planung", ["Die im Gespräch genannte Jahresmenge von 1.200 Stück wird für jedes Vertragsjahr als Mindestabnahme vereinbart. Rheinkern übermittelt jeweils bis zum zwanzigsten Kalendertag eine rollierende Planung für die nächsten sechs Monate. Die Planung dient Talbruck zur Beschaffung; die ersten drei Monate werden mit Zugang der Planung hinsichtlich der Mengen verbindlich. Änderungen der späteren Monate sollen die vereinbarte Jahresmenge nicht unterschreiten.", "Vermerk Vertrieb vom 02.09.: Frau Schulte hat bislang nur eine unverbindliche Jahresplanung bestätigt. Die vorstehende Mindestabnahme ist unser Vorschlag für die Freigabe der Staffel und der Bauteilbeschaffung."]),
        ("4. Einzelabrufe", ["Rheinkern benennt in jedem Abruf Artikel, Revision, Stückzahl und Liefertermin. Talbruck bestätigt innerhalb von drei Arbeitstagen. Ohne Widerspruch innerhalb dieser Frist gilt der Abruf als angenommen, soweit er die vorherige verbindliche Planung nicht übersteigt und mindestens sechs Wochen Vorlauf hat. Lieferlose sollen mindestens 100 Stück umfassen. Kleinere Lose werden gegen den angebotenen Rüstzuschlag ausgeführt."]),
        ("5. Preise und Fracht", ["Der Ausgangspreis beträgt 186,00 EUR netto je Stück. Bei 1.200 fest zugesagten Stück je Vertragsjahr beträgt der Nachlass 3 %, bei 1.800 Stück 5 %. Die Staffel wird zum Beginn des Vertragsjahres festgelegt und bei Unterschreitung auf Basis der tatsächlichen Jahresabnahme nachberechnet. Lieferung erfolgt DAP Rheinkern Anlagenbau GmbH, Jülicher Straße 318, Tor 2, 52070 Aachen, Incoterms 2020. Die Entladung am Tor übernimmt Rheinkern. Rechnungen sind binnen dreißig Tagen ohne Abzug zahlbar."]),
        ("6. Werkzeug", ["Das Werkzeug WZ-D400-17 wird nach vollständiger Zahlung dem Projekt Rheinkern zugeordnet und ausschließlich für dessen Sensoren eingesetzt. Talbruck verwahrt und wartet das Werkzeug während der Laufzeit. Änderungen an Formeinsätzen setzen eine technische Freigabe von Rheinkern voraus. Eine Herausgabe erfolgt nach Abrechnung sämtlicher offenen Projektkosten. Über Art und Umfang der bei Vertragsende noch ausstehenden Wartung ist anhand des dann vorhandenen Werkzeugprotokolls abzurechnen."]),
        ("7. Muster und Serienfreigabe", ["Die zwölf Versuchsmuster dienen der ersten mechanischen und elektrischen Prüfung. Rheinkern meldet Messabweichungen mit Prüfbedingungen und Seriennummern. Die Serienfreigabe soll spätestens am 25.09.2026 erfolgen. Bleibt eine Rückmeldung bis dahin aus, verschieben sich angekündigte Serientermine um die Dauer der fehlenden Rückmeldung und der erforderlichen Neuplanung. Schweigen ersetzt keine technische Serienfreigabe."]),
        ("8. Änderungen und Abkündigungen", ["Talbruck zeigt Änderungen an Messkern, Firmware und Gehäuse an, bevor geänderte Teile in Serie geliefert werden. Bei einer Bauteilabkündigung nennt Talbruck den verfügbaren Altbestand und eine Ersatzlösung. Rheinkern entscheidet binnen fünf Arbeitstagen über eine Versuchslieferung. Die Kosten zusätzlicher Versuchsreihen und einer erneuten Freigabe werden im Änderungsangebot benannt. Eine technisch bestätigte Ersatzrevision kann Talbruck nach Freigabe in die laufenden Abrufe übernehmen."]),
        ("9. Qualität und Beanstandungen", ["Jede Lieferung enthält Loskennung, Revisionsstand und Prüfbestätigung der vereinbarten Endprüfung. Rheinkern prüft Menge und sichtbare Transportschäden nach Eingang und meldet erkannte Messabweichungen mit den verfügbaren Messdaten. Talbruck erhält Gelegenheit, betroffene Teile zu untersuchen und Ersatzteile bereitzustellen. Ausgesonderte Teile werden bis zur Abstimmung gekennzeichnet verwahrt."]),
        ("10. Feldmaßnahmen und Kosten", ["Vor einem Rückruf oder einer Nachprüfung außerhalb des Werks informiert Rheinkern Talbruck über die betroffenen Lose, die Fehlerbeschreibung und die geplanten Maßnahmen. Talbruck trägt nach diesem Vorschlag die nachgewiesenen Kosten der von ihm gelieferten Ersatzsensoren und des Rücktransports. Ausbau, Anreise, Stillstandszeiten und Einbau beim Anlagenkunden sollen gesondert vereinbart werden. Für eilbedürftige Maßnahmen ist ein telefonischer Kontakt mit nachfolgender schriftlicher Dokumentation vorgesehen.", "Der Einkaufswunsch nach einer weitergehenden Kostenregelung ist noch nicht eingearbeitet; Talbruck wartet auf eine Kostengliederung typischer Serviceeinsätze."]),
        ("11. Vorräte und Beendigung", ["Talbruck darf Material für die ersten drei Monate der Planung beschaffen. Bei Reduzierung oder Ende der Zusammenarbeit übernimmt Rheinkern die dafür nachweislich beschafften, nicht anderweitig verwendbaren Bauteile und angearbeiteten Teile zum belegten Einkaufspreis zuzüglich dokumentierter Bearbeitung. Für spätere Planmonate besteht diese Übernahme nur nach ausdrücklicher Beschaffungsfreigabe. Talbruck legt Bestände nach Teilenummer, Stufe und Bestelldatum offen und verrechnet Erlöse einer anderweitigen Verwendung."]),
        ("12. Abschlussstand", ["Die Parteien stimmen vor Unterzeichnung insbesondere den Bindungszeitraum der Planung, die Werkzeugherausgabe und die Kosten von Feldmaßnahmen ab. Dieser Entwurf enthält noch keine Erklärung von Rheinkern zur Mindestmenge. Änderungen sollen in einer gemeinsamen Fassung zusammengeführt werden.", "Für Rheinkern: ____________________   Datum: ____________________\nFür Talbruck: ____________________   Datum: ____________________"])
    ])
    docx(d / "04_gegenvorschlag_rheinkern_v08.docx", R, "Gegenvorschlag zum Rahmenliefervertrag D400", [("Stand", "0.8 vom 10.09.2026"), ("An", "Talbruck Sensorik GmbH, Herrn Paul Reuter"), ("Bearbeitung", "Eva Schulte nach Rücksprache mit Miriam Küppers"), ("Bezug", "Lieferantenentwurf 0.6 vom 02.09.2026")], [
        ("1. Gegenstand und Laufzeit", ["Talbruck liefert Rheinkern Sensoren D400 für die Linie 7. Der Rahmen soll vom 01.10.2026 bis 30.09.2029 gelten. Maßgeblich ist Datenblatt Revision B vom 20.08.2026. Eine andere Ausführung wird erst nach schriftlicher Bestätigung durch Qualitätsleitung und Einkauf bestellt. Die Vorabfertigung der Werkzeuge und die zwölf Versuchsmuster bleiben dem Auftrag RK-WZ-260828 zugeordnet."]),
        ("2. Bedarf und Forecast", ["Die Angabe von 1.200 Stück pro Jahr ist eine unverbindliche Bedarfsplanung. Eine Mindestabnahme wird nicht vereinbart. Rheinkern übermittelt monatlich eine Planung für sechs Monate und kennzeichnet darin die bereits gesondert bestellten Mengen. Die Planung allein löst keine Materialbestellung auf Rechnung von Rheinkern aus. Eine ausnahmsweise Materialfreigabe muss die Teilenummern, Höchstmenge und den maximalen Nettobetrag nennen."]),
        ("3. Abrufe und Bestätigung", ["Verbindliche Abrufe erfolgen durch den Einkauf unter Angabe von Revision, Menge und Liefertermin. Talbruck bestätigt oder benennt Abweichungen binnen drei Arbeitstagen. Schweigen gilt nicht als Bestätigung. Die Serienfreigabe ist zusätzlich erforderlich; eine Terminreservierung ersetzt sie nicht. Für das erste Quartal können Lose unter 100 Stück erforderlich sein. Der Zuschlag hierfür bleibt Gegenstand der Preisabstimmung."]),
        ("4. Preise", ["Der Ausgangspreis beträgt 186,00 EUR netto je Stück. Rheinkern schlägt vor, einen Nachlass von 3 % bei tatsächlich erreichten 1.200 Stück je Vertragsjahr nachträglich gutzuschreiben, ohne vorherige Mindestabnahme. Ab 1.800 Stück soll die Gutschrift 5 % betragen. Werkzeugkosten werden nicht ein zweites Mal auf den Stückpreis aufgeschlagen. Preisänderungen während des ersten Vertragsjahres bedürfen einer gesonderten Zustimmung.", "Talbruck hat die nachträgliche Staffel bislang nicht angeboten. Bis zur Abstimmung kalkuliert der Einkauf mit dem Ausgangspreis und weist den möglichen Nachlass getrennt aus."]),
        ("5. Lieferung und Zahlung", ["Geliefert wird DAP Rheinkern Anlagenbau GmbH, Jülicher Straße 318, Tor 2, 52070 Aachen, Incoterms 2020. Rheinkern entlädt zu den im Lieferantenstamm genannten Zeiten. Ein Lieferavis mit Losnummern geht spätestens am Vortag ein. Teilmengenlieferungen bedürfen der Zustimmung des Einkaufs. Die Zahlung erfolgt dreißig Tage nach Eingang von Rechnung und zugehöriger Lieferung; streitige einzelne Positionen werden gesondert bezeichnet."]),
        ("6. Werkzeug und Nutzung", ["Nach vollständiger Zahlung wird das Werkzeug WZ-D400-17 Rheinkern zugeordnet und von Talbruck ausschließlich für D400-Bestellungen von Rheinkern genutzt. Talbruck kennzeichnet die Formeinsätze mit der Werkzeugnummer und führt ein Wartungsblatt. Nach Ende des Rahmens soll das Werkzeug binnen zehn Arbeitstagen zusammen mit den vorhandenen Maßblättern herausgegeben werden. Noch nicht abgerechnete Serienlieferungen sollen die Herausgabe nicht verzögern.", "Der Einkauf schlägt die vorstehende Herausgaberegel vor. Für den Fall eines noch offenen Änderungsauftrags am Werkzeug haben die Parteien bisher keinen gesonderten Ablauf vereinbart."]),
        ("7. Technische Freigabe", ["Rheinkern prüft die zwölf Muster zunächst bei Raumtemperatur und im mechanischen Aufbau. Danach werden Temperaturgang und Störfestigkeit in einem zweiten Termin geprüft. Die Serienfreigabe wird in einem gesonderten Schreiben erklärt. Der Einbau einzelner Muster in einen Versuchsstand und das Ausbleiben einer kurzfristigen Beanstandung gelten nicht als Freigabe für Serienlieferungen. Beide Parteien gleichen die verwendeten Messbedingungen ab, bevor sie eine Abweichung bewerten."]),
        ("8. Bauteiländerungen", ["Talbruck informiert den Einkauf und die Qualitätsleitung über Abkündigungen und beabsichtigte Änderungen. Die Mitteilung nennt den betroffenen Bauteilstand, den letzten Bestelltermin und die abweichenden Messwerte der Ersatzlösung. Ohne Freigabe der Ersatzrevision werden Serienabrufe nicht auf diese umgestellt. Für Versuchsmuster kann eine begrenzte Freigabe mit ausdrücklich benannter Stückzahl erteilt werden."]),
        ("9. Qualität und Nachverfolgung", ["Die Sensoren tragen eine Seriennummer und einen lesbaren Revisionsstand. Talbruck hält die Zuordnung zu Fertigungslos und Endprüfung bereit. Rheinkern dokumentiert eingegangene Mengen und die Zuordnung zu seinen Anlagen. Bei wiederholten Abweichungen stimmen beide Qualitätsstellen eine zusätzliche Eingangskontrolle ab; Umfang und Dauer werden im Prüfplan festgehalten."]),
        ("10. Nacharbeit und Feldmaßnahmen", ["Rheinkern schlägt vor, dass Talbruck die erforderlichen und belegten Kosten von Prüfung, Ausbau, Ersatz und Wiedereinbau trägt, soweit die Maßnahme auf einer Abweichung des gelieferten Sensors von der vereinbarten Ausführung beruht. Rheinkern stellt vor einer planbaren Maßnahme eine Kostenschätzung zur Verfügung. Bei einer unmittelbar erforderlichen Stillsetzung informiert Rheinkern Talbruck am selben Arbeitstag und bewahrt die betroffenen Teile auf.", "Reise- und Stillstandskosten sind noch nicht beziffert. Der Einkauf kann die von Talbruck gewünschte Begrenzung auf Ersatzsensor und Rückfracht nicht bestätigen. Eine endgültige Kostenregelung ist in dieser Fassung nicht abgestimmt."]),
        ("11. Bestand bei Reduzierung und Ende", ["Bei Ablauf des Rahmens werden bestätigte Abrufe abgewickelt. Für darüber hinaus vorhandene Bauteile legt Talbruck vor einer Übernahmeforderung die gesonderte Materialfreigabe, Bestellnachweise und den verbleibenden Bestand vor. Eine reine Forecastmenge begründet keine Bestandsübernahme. Eine mögliche Weiterverwendung, Rückgabe an den Vorlieferanten und der daraus erzielte Betrag werden offengelegt. Über einen Übergangsbestand für Ersatzteile wird sechs Monate vor Vertragsende gesondert verhandelt."]),
        ("12. Weiteres Verfahren", ["Dieser Text ist ein Gegenvorschlag des Einkaufs und noch nicht von den Geschäftsführungen freigegeben. Die Parteien möchten Mengenbindung, Staffel, Werkzeug und Feldkosten im Gespräch am 24.09.2026 zusammenführen. Bis zur Unterzeichnung bleiben Einzelaufträge auf ihren jeweils bestätigten Umfang begrenzt.", "Für Rheinkern: ____________________   Datum: ____________________\nFür Talbruck: ____________________   Datum: ____________________"])
    ])
    for rev, date, chip, accuracy, repeatability, response in [("B","20.08.2026","Messkern MK-41","±0,20 mm","0,05 mm","5 ms"),("C","14.09.2026","Messkern MK-42","±0,35 mm","0,08 mm","8 ms")]:
        num = "05" if rev == "B" else "06"
        pdf(d / f"{num}_datenblatt_d400_rev_{rev.lower()}.pdf", T, "Datenblatt D400 Revision " + rev, [("Ausgabe",date),("Freigabe Dokument","Dr. Selma Berg, Entwicklung"),("Artikel","D400-24-M12 / Messbereich 40 bis 400 mm")], ["1. Aufbau\nOptischer Distanzsensor für den Einbau in geschlossene Montageanlagen. Versorgung 24 V DC, Ausgang 4 bis 20 mA, M12-Steckverbinder, Gehäuse Aluminium. Der Messwert wird auf das Referenzziel in Achsrichtung bezogen. Versorgung und Auswertung müssen vor dem Versuch stabilisiert sein."], (["Merkmal","Wert","Bedingung"], [["Messkern",chip,"Firmware " + ("2.6" if rev == "B" else "2.8")],["Abweichung bei 200 mm",accuracy,"23 ±2 °C; mattweiße Referenzplatte"],["Wiederholstreuung",repeatability,"Maximalspanne aus zehn Wiederholungen"],["Ansprechzeit",response,"Nach Stabilisierung der Versorgung"],["Betriebstemperatur","0 bis 50 °C","Temperaturgang gesondert messen"],["Befestigungsabstand","32,00 ±0,10 mm","Zwei Bohrungen im Gehäuse"],["Schutzart","IP54","Gesteckter Anschluss im eingebauten Zustand"]],[50,49,67]), ["2. Prüfbedingungen\nDie Raumtemperaturwerte beruhen auf einem Abstand von 200,00 mm nach zehn Minuten Aufwärmzeit. Sie ersetzen keine Messreihe über den vollständigen Arbeitsbereich oder bei wechselnder Temperatur. Für die Anwendung in Linie 7 sind Gegenlicht, Vibration und der Abgleich mit der Steuerung im Aufbau des Käufers zu prüfen.", ("3. Revisionsnotiz\nRevision B verwendet den Messkern MK-41. Außenmaße und Steckbelegung sind gegenüber Revision A unverändert. Dieses Datenblatt lag dem Angebot TS-260902 zugrunde." if rev == "B" else "3. Revisionsnotiz\nRevision C verwendet wegen der angekündigten Abkündigung den Messkern MK-42. Außenmaße und Steckbelegung bleiben unverändert; Abweichung, Wiederholstreuung und Ansprechzeit ändern sich wie oben angegeben. Die Revision ist zunächst für zwölf Versuchsmuster vorgesehen. Eine Serienfreigabe durch Rheinkern ist hier nicht eingetragen.")])
    eml(d / "07_versand_angebot_entwurf.eml", "Paul Reuter <paul.reuter@talbruck-sensorik.de>", "Eva Schulte <eva.schulte@rheinkern-anlagenbau.de>", "2026-09-02T14:18:00+02:00", "D400 / Angebot, Rahmen 0.6 und Datenblatt B", """Guten Tag Frau Schulte,

anbei erhalten Sie das Angebot TS-260902, unseren Vertragsstand 0.6 und Datenblatt B. Der Werkzeugauftrag vom 28. August läuft schon. Die zwölf Muster sind für den 17. September eingeplant.

Ich habe die im Gespräch genannten 1.200 Stück in Ziffer 3 als Mindestmenge formuliert, damit wir die Staffel und die Beschaffung über drei Monate abbilden können. Mir ist bewusst, dass Ihre Bedarfsliste bisher als unverbindliche Planung überschrieben war. Bitte sagen Sie, ob die Geschäftsführung eine feste Menge vertreten kann. Die Staffel in unserer Kalkulation setzt diese Bindung voraus.

Bei den Feldkosten haben wir noch nicht zusammengefunden. Unsere Fassung enthält Ersatzsensor und Rückfracht, Ihre Servicekosten fehlen uns noch. Auch die Werkzeugherausgabe sollten wir ausdrücklich besprechen; wir möchten keine offene Bearbeitung zurückbehalten müssen, ohne vorher die Rechnung abgestimmt zu haben.

Freundliche Grüße
Paul Reuter
Vertrieb, Talbruck Sensorik GmbH
Gewerbepark 17, 52249 Eschweiler
Telefon 02403 748 61 24
Geschäftsführer Henning Voß, Amtsgericht Aachen HRB 22874""", cc="Dr. Selma Berg <selma.berg@talbruck-sensorik.de>", attachments=["02_angebot_ts_260902.pdf", "03_rahmenvertrag_lieferant_v06.docx", "05_datenblatt_d400_rev_b.pdf"])
    eml(d / "08_versand_gegenvorschlag.eml", "Eva Schulte <eva.schulte@rheinkern-anlagenbau.de>", "Paul Reuter <paul.reuter@talbruck-sensorik.de>", "2026-09-10T10:41:00+02:00", "Re: D400 / unser Stand 0.8", """Guten Morgen Herr Reuter,

ich sende unseren Gegenentwurf 0.8. Die 1.200 Stück pro Jahr sind weiterhin eine unverbindliche Planung. Wir können keine Mindestabnahme unterschreiben, solange die Aufträge unserer Anlagenkunden noch nicht vorliegen. Für bestätigte Einzelabrufe möchten wir dagegen einen klaren Ablauf und verlässliche Termine.

Wir haben die drei Monate Materialbindung deshalb nicht übernommen. Eine gesonderte Freigabe für konkret bezeichnete Bauteile können wir besprechen. Das Werkzeug soll bei Ende des Projekts verfügbar sein; es ist bereits bezahlt. Die Zahlungsbestätigung liegt bei unserer Buchhaltung.

Unsere Qualitätsleitung benötigt zunächst die Musterprüfung. Danach folgt die Prüfung im Aufbau. Die vorgeschlagene Kostenzuordnung für Feldmaßnahmen ist noch nicht abschließend mit unserer Geschäftsführung besprochen; zu Anreise und Anlagenstillstand stelle ich eine typische Serviceabrechnung zusammen. Am 24. September könnten wir ab 10 Uhr gemeinsam die offenen Texte durchgehen.

Viele Grüße
Eva Schulte
Einkauf, Rheinkern Anlagenbau GmbH
Jülicher Straße 318, 52070 Aachen
Telefon 0241 936 42 31
Amtsgericht Aachen HRB 24681""", cc="Miriam Küppers <miriam.kueppers@rheinkern-anlagenbau.de>, Anja Heil <anja.heil@rheinkern-anlagenbau.de>", attachments=["04_gegenvorschlag_rheinkern_v08.docx"], reply="<07_versand_angebot_entwurf@talbruck-sensorik.de>")
    eml(d / "09_bauteilabkuendigung.eml", "Dr. Selma Berg <selma.berg@talbruck-sensorik.de>", "Anja Heil <anja.heil@rheinkern-anlagenbau.de>, Eva Schulte <eva.schulte@rheinkern-anlagenbau.de>", "2026-09-14T08:52:00+02:00", "D400 / MK-41 abgekündigt, Entscheidung zu zwölf Mustern bis morgen", """Guten Morgen Frau Heil, guten Morgen Frau Schulte,

unser Vorlieferant hat uns am Freitag mitgeteilt, dass der Messkern MK-41 nach dem letzten Bestellfenster am 30. September ausläuft. Wir können derzeit 96 Stück MK-41 aus eigenem Bestand zuordnen. Eine weitere Altteilbestellung wäre nicht stornierbar und müsste gesondert freigegeben werden.

Als Ersatz können wir MK-42 einsetzen. Das angehängte Datenblatt C nennt die Unterschiede: bei 200 mm jetzt ±0,35 statt ±0,20 mm, Wiederholstreuung 0,08 statt 0,05 mm, Ansprechzeit 8 statt 5 ms. Gehäuse und Anschluss passen unverändert. Der Stückpreis für die erste Serie soll unverändert bleiben; über spätere Bauteilpreise sprechen wir, sobald ein verbindliches Angebot vorliegt.

Für die Musterlieferung am Donnerstag benötigen wir bis morgen 12 Uhr eine Entscheidung, ob wir die zwölf Stück mit MK-42 fertigstellen dürfen. Das ist ein kurzer Termin, weil morgen die Endprüfung eingeplant ist. Eine Temperaturreihe ist in diesem Zeitfenster nicht möglich. Bitte unterscheiden Sie bei Ihrer Rückmeldung die zwölf Muster und eine etwaige Beschaffung für die Serie.

Freundliche Grüße
Dr. Selma Berg
Entwicklung und Qualität, Talbruck Sensorik GmbH
Gewerbepark 17, 52249 Eschweiler
Telefon 02403 748 61 38""", cc="Paul Reuter <paul.reuter@talbruck-sensorik.de>, Tobias Frings <tobias.frings@rheinkern-anlagenbau.de>", attachments=["06_datenblatt_d400_rev_c.pdf"])
    eml(d / "10_expressfreigabe_muster.eml", "Tobias Frings <tobias.frings@rheinkern-anlagenbau.de>", "Dr. Selma Berg <selma.berg@talbruck-sensorik.de>", "2026-09-15T11:34:00+02:00", "Re: D400 / zwölf Muster mit MK-42", """Hallo Frau Berg,

für die zwölf Versuchsmuster können Sie MK-42 einbauen. Ich habe mit Anja gesprochen; wir wollen Freitag zunächst die Einbaulage und die 200-mm-Messung sehen. Damit bleiben wir im Zeitplan für den Versuchsstand. Das Datenblatt C ist angekommen.

Am Telefon habe ich gesagt, dass 0,35 mm für den ersten mechanischen Aufbau wahrscheinlich reichen. Bitte verstehen Sie das nicht als Änderung unserer Serienspezifikation. Wir haben die Auswirkungen auf die Abschaltschwelle der Anlage noch nicht durchgemessen. Die Temperaturreihe und die Freigabe durch Anja und Einkauf fehlen weiterhin.

Ich kann auch keine Bestellung von Serienbauteilen freigeben. Für die zwölf Stück gilt der vorhandene Musterauftrag ohne zusätzliche Kosten. Bitte auf dem Lieferschein C und die Seriennummern angeben. Paul hatte gestern nach 300 Stück für ein Quartal gefragt; dazu muss Eva antworten, ich habe nur den Versuchstermin bestätigt.

Viele Grüße
Tobias Frings
Konstruktion, Rheinkern Anlagenbau GmbH
Jülicher Straße 318, 52070 Aachen
Telefon 0241 936 42 46""", cc="Eva Schulte <eva.schulte@rheinkern-anlagenbau.de>, Anja Heil <anja.heil@rheinkern-anlagenbau.de>, Paul Reuter <paul.reuter@talbruck-sensorik.de>", reply="<09_bauteilabkuendigung@talbruck-sensorik.de>")
    csv_file(d / "11_erp_abrufe_20260921.csv", ["Exportstand","Beleg","Position","Artikel","Revision","Menge_Stück","Wunschtermin","Status","Versand_an_Lieferant","Lieferantenbestätigung","Bemerkung"], [
        ["2026-09-21T14:00:00+02:00","RK-AB-261001",10,"D400-24-M12","offen",60,"2026-10-19","Termin angefragt","2026-09-21","","Erster Serienanlauf; technische Freigabe fehlt"],
        ["2026-09-21T14:00:00+02:00","RK-AB-261102",10,"D400-24-M12","offen",80,"2026-11-16","Termin angefragt","2026-09-21","","Los unter 100 Stück"],
        ["2026-09-21T14:00:00+02:00","RK-AB-261203",10,"D400-24-M12","offen",100,"2026-12-14","Termin angefragt","2026-09-21","","Anlagenkunde hat Menge noch nicht finalisiert"],
        ["2026-09-21T14:00:00+02:00","RK-FC-2027",10,"D400-24-M12","offen",300,"2027-03-31","Unverbindlicher Forecast","2026-09-21","","Quartal 1; Sammeltermin, kein Einzelabruf"],
        ["2026-09-21T14:00:00+02:00","RK-FC-2027",20,"D400-24-M12","offen",300,"2027-06-30","Unverbindlicher Forecast","2026-09-21","","Quartal 2; Sammeltermin, kein Einzelabruf"],
        ["2026-09-21T14:00:00+02:00","RK-FC-2027",30,"D400-24-M12","offen",300,"2027-09-30","Unverbindlicher Forecast","2026-09-21","","Quartal 3; Sammeltermin, kein Einzelabruf"],
        ["2026-09-21T14:00:00+02:00","RK-FC-2027",40,"D400-24-M12","offen",300,"2027-12-31","Unverbindlicher Forecast","2026-09-21","","Quartal 4; Sammeltermin, kein Einzelabruf"],
    ])
    eml(d / "13_bestellung_werkzeug.eml", "Eva Schulte <eva.schulte@rheinkern-anlagenbau.de>", "Paul Reuter <paul.reuter@talbruck-sensorik.de>", "2026-08-28T09:42:00+02:00", "Bestellung RK-WZ-260828 / Werkzeug D400 und zwölf Muster", """Sehr geehrter Herr Reuter,

wir bestellen das Werkzeug WZ-D400-17 gemäß Ihrem Werkzeugangebot vom 26. August zum Festpreis von 12.400 EUR netto zuzüglich Umsatzsteuer. Enthalten sind Formeinsätze, Bemusterung und zwölf Sensoren für unsere Versuchsprüfung. Sie hatten am Telefon bestätigt, dass für diese zwölf Stück kein separater Stückpreis berechnet wird. Die Werkzeugrechnung können Sie nach Fertigungsbeginn stellen, zahlbar binnen zehn Tagen.

Bitte kennzeichnen Sie das Werkzeug mit WZ-D400-17 und unserer Firma. Die erste Musterlieferung erwarten wir am 17. September an Tor 2 in Aachen. Der Auftrag bezieht sich auf die technische Grundlage Datenblatt B. Änderungen müssen Sie vor Ausführung mit Anja Heil abstimmen. Eine Serienmenge bestellen wir heute nicht.

Die Bedingungen zur Verwahrung und Herausgabe möchten wir im Rahmenvertrag festhalten. Bis dahin bitte keine Nutzung für andere Kunden. Frau Küppers hat diese Werkzeugbestellung freigegeben; der geplante dreijährige Lieferrahmen ist noch in Verhandlung. Als Bestellreferenz muss RK-WZ-260828 auf Rechnung und Lieferschein stehen.

Mit freundlichen Grüßen
Eva Schulte
Einkauf, Rheinkern Anlagenbau GmbH
Jülicher Straße 318, 52070 Aachen
Telefon 0241 936 42 31""", cc="Miriam Küppers <miriam.kueppers@rheinkern-anlagenbau.de>, Anja Heil <anja.heil@rheinkern-anlagenbau.de>")
    pdf(d / "14_werkzeugrechnung_ts_2026_491.pdf", T, "Rechnung TS-2026-491", [("Rechnungsdatum","01.09.2026"),("Leistungsbeginn","31.08.2026"),("Rechnungsempfänger",R + ", Jülicher Straße 318, 52070 Aachen"),("Bestellreferenz","RK-WZ-260828"),("Umsatzsteuer-ID","DE318642975")], ["Werkzeug WZ-D400-17 für Sensor D400. Festpreis gemäß Werkzeugbestellung vom 28.08.2026, einschließlich Formeinsätzen, Bemusterung und zwölf Versuchssensoren. Weitere Serienlieferungen sind nicht enthalten."], (["Position","Netto EUR","USt EUR","Brutto EUR"], [["Werkzeugpaket WZ-D400-17","12.400,00","2.356,00","14.756,00"]],[76,30,30,30]), ["Umsatzsteuersatz 19 %. Zahlbar bis 11.09.2026 ohne Abzug auf das Lieferantenkonto Endziffern 6842. Bitte TS-2026-491 und RK-WZ-260828 als Verwendungszweck angeben.", "Das Werkzeug verbleibt für die Bemusterung im Werkzeugraum Eschweiler. Die angekündigte Musterlieferung für den 17.09.2026 erhält einen eigenen Lieferschein. Ein Abzug von späteren Stückpreisen ist mit dieser Rechnung nicht verbunden."])
    pdf(d / "15_zahlungsbeleg_werkzeug.pdf", "Aachener Gewerbebank eG", "Buchungsbestätigung Firmenkonto", [("Kontoinhaber",R),("Konto","Endziffern 3307"),("Buchungstag und Valuta","04.09.2026"),("Belegnummer","AGB-260904-7319")], ["Die nachfolgend bezeichnete SEPA-Überweisung wurde ausgeführt und dem Firmenkonto belastet. Der Beleg wurde am 07.09.2026 um 08:12 Uhr im Firmenportal abgerufen."], (["Feld","Buchungsangabe"], [["Empfänger",T],["Empfängerkonto","Endziffern 6842"],["Belastungsbetrag","14.756,00 EUR"],["Verwendungszweck","TS-2026-491 / RK-WZ-260828 / Werkzeug D400"],["Auftragsfreigabe","Miriam Küppers, 03.09.2026, 16:42 Uhr"],["Ende-zu-Ende-Referenz","RK-WZ-260828-491"]],[48,118]), ["Die Anzeige bezieht sich ausschließlich auf die oben genannte Buchung und enthält keine weiteren Kontoumsätze. Eine Rückgabe oder Stornierung ist zum Abrufzeitpunkt nicht im Auftragsstatus vermerkt. Der Rechnungsbetrag von 14.756,00 EUR wurde ohne Skontoabzug angewiesen. Gebühren wurden für diese Buchung nicht gesondert belastet."])
    docx(d / "16_werkzeugblatt_wz_d400_17.docx", T, "Werkzeugblatt WZ D400 17", [("Datum", "16.09.2026"), ("Bearbeiter", "Karsten Lück, Werkzeugbau"), ("Auftrag", "RK-WZ-260828"), ("Standort", "Werkzeugraum Eschweiler, Regal 3 Fach 2")], [
        ("1. Fertigungsstand", ["Die beiden Formeinsätze sind gefertigt und mit WZ-D400-17 gekennzeichnet. Die Grundaufnahme gehört zum allgemeinen Maschinenbestand von Talbruck und ist nicht Bestandteil des berechneten Werkzeugpakets. Das auftragsbezogene Paket umfasst die beiden Einsätze, einen Zentrierring und das Maßblatt vom 15.09.2026. Die Rechnung TS-2026-491 ist laut Buchhaltung am 07.09. als bezahlt verbucht worden."]),
        ("2. Bemusterung", ["Am 15.09. wurden zwölf Gehäuse für die Muster D400-C-260915-01 bis -12 hergestellt. Sichtkontrolle und Lehrenprüfung des Befestigungsabstands ergaben keinen Ausschuss. Die Formeinsätze wurden nach dem Versuch gereinigt und konserviert. Der mechanische Aufbau unterscheidet sich zwischen Revision B und C nicht. Der geänderte Messkern wird nach der Gehäusefertigung eingesetzt."]),
        ("3. Nutzung und Übergabe", ["Es wurde noch keine Serie mit dem Werkzeug gefahren. Eine Übernahmebestätigung des Käufers für die Einsätze liegt im Werkzeugraum nicht vor. Der Lieferschein für die Muster wird davon getrennt geführt. Herr Reuter hat um Verbleib des Werkzeugs für die geplante Oktoberfertigung gebeten. Eine endgültige Abrede zu Transportverpackung, Abholung und Wartung nach Projektende ist im Werkzeugblatt noch nicht hinterlegt."])
    ], "Karsten Lück\nWerkzeugbau")
    pdf(d / "17_lieferschein_muster_ls_260917.pdf", T, "Lieferschein LS-260917-14", [("Versand","16.09.2026, 16:10 Uhr"),("Anlieferung","17.09.2026, 09:26 Uhr"),("Empfänger",R + ", Tor 2, Jülicher Straße 318, 52070 Aachen"),("Bestellung","RK-WZ-260828"),("Empfang erfasst","Lukas Dorn, Warenannahme; Eingang WE-260917-083")], ["Zwölf Versuchsmuster, keine Serienlieferung. Fertigung mit Messkern MK-42 entsprechend der E-Mail von Tobias Frings vom 15.09.2026. Seriennummern D400-C-260915-01 bis D400-C-260915-12. Revisionskennzeichnung C, Firmware 2.8."], (["Artikel","Menge","Verpackung","Bemerkung"], [["D400-24-M12 / C","12 Stück","1 Karton, 12 Einzelhülsen","Gehäuse aus Werkzeug WZ-D400-17"]],[53,25,42,46]), ["Frachtbedingung: DAP Rheinkern Anlagenbau GmbH, Jülicher Straße 318, Tor 2, 52070 Aachen, Incoterms 2020. Fracht im Werkzeug- und Musterauftrag enthalten. Transportreferenz TB-0916-204. Bruttogewicht 4,8 kg.", "Wareneingangsvermerk: Karton trocken und außen unbeschädigt. Zwölf Hülsen gezählt, Seriennummern zur Messstelle weitergegeben. Kein Funktionslauf in der Warenannahme. Empfangsbuchung durch Lukas Dorn am 17.09.2026 um 09:31 Uhr."])
    measurements = [(200.10,200.13,200.12),(200.15,200.17,200.16),(200.19,200.21,200.20),(200.24,200.26,200.25),(200.28,200.31,200.29),(200.11,200.14,200.12),(200.18,200.20,200.19),(200.22,200.24,200.23),(200.16,200.18,200.17),(200.25,200.28,200.27),(200.12,200.15,200.13),(200.17,200.19,200.18)]
    csv_file(d / "18_messwerte_muster_200mm.csv", ["Protokoll","Datum","Seriennummer","Revision","Referenz_mm","Messung_1_mm","Messung_2_mm","Messung_3_mm","Temperatur_C","Versorgung_V","Aufwärmzeit_min","Prüferin"], [["RK-QM-260918","2026-09-18",f"D400-C-260915-{i:02d}","C","200.00",*(f"{v:.2f}" for v in vals),"23.1","24.02",10,"Anja Heil"] for i, vals in enumerate(measurements,1)])
    docx(d / "19_pruefprotokoll_muster.docx", R, "Prüfprotokoll Versuchsmuster D400", [("Nummer", "RK-QM-260918"), ("Datum und Dauer", "18.09.2026, 10:05 bis 11:40 Uhr"), ("Prüferin", "Anja Heil, Qualitätssicherung"), ("Eingang", "LS-260917-14 / WE-260917-083")], [
        ("1. Prüflinge und Aufbau", ["Geprüft wurden die zwölf am Vortag angelieferten Sensoren D400-C-260915-01 bis -12. Das Etikett bezeichnet Revision C, Firmware 2.8. Alle Sensoren wurden vor der ersten Ablesung zehn Minuten gemeinsam am Labornetzteil aufgewärmt und blieben während der Reihe eingeschaltet. Nacheinander erfolgten je drei Ablesungen bei 200,00 mm Abstand zu einer mattweißen Referenzplatte. Die Referenz wurde mit Lehrenaufbau RK-LM-18 eingestellt. Der Prüfraum hatte 23,1 °C."]),
        ("2. Aufzeichnung", ["Die Rohwerte stehen in 18_messwerte_muster_200mm.csv. Die Versorgung wurde einmal zu Beginn mit 24,02 V gemessen und während der Reihe nicht verändert. Ein einzelner Nullabgleich je Sensor wurde vor der Aufzeichnung vorgenommen. Danach wurde nicht nachjustiert. Die Messuhr trägt Inventarnummer RK-MU-044; der letzte interne Vergleich ist im Gerätebuch für den 03.08.2026 vermerkt."]),
        ("3. Begrenzung des Versuchs", ["Es wurden weder der gesamte Messbereich noch der Temperaturgang, Gegenlicht, Vibration oder die Abschaltschwelle der Anlage geprüft. Die im Datenblatt genannte Wiederholstreuung bezieht sich auf zehn Wiederholungen; diese Reihe enthält nur drei. Daraus wurde keine Bestätigung dieses Datenblattmerkmals erstellt. Ein Prüfungslauf im Anlagenaufbau ist für den 29.09.2026 reserviert."]),
        ("4. Weitergabe", ["Die Rohdaten wurden am 18.09. um 14:16 Uhr in den gemeinsamen Projektordner gestellt. Herr Reuter kann auf die Datei lesend zugreifen. Die zwölf Sensoren bleiben im Versuchsraum bei Tobias Frings. Eine Serienfreigabe ist in diesem Protokoll nicht erteilt. Die zum Versuch übersandte Revision C und die im Einkaufsentwurf genannte Revision B liegen beide im Projektordner."])
    ], "Anja Heil\nQualitätssicherung")
    eml(d / "20_lieferant_mengen_toleranzen.eml", "Paul Reuter <paul.reuter@talbruck-sensorik.de>", "Eva Schulte <eva.schulte@rheinkern-anlagenbau.de>", "2026-09-18T16:02:00+02:00", "D400 / Jahresmenge und bestätigte Revision C", """Guten Tag Frau Schulte,

die zwölf Muster sind angekommen und die Messdatei konnten wir öffnen. Nach dem Telefonat mit Herrn Frings hatte ich Revision C mit 0,35 mm als bestätigt notiert. Er sagte, das passe für den Aufbau und wir sollten den Termin halten. Ich hatte daraus nicht nur den Einbau in die zwölf Muster verstanden. Frau Berg hat mir inzwischen seine E-Mail weitergeleitet; bitte lassen Sie uns die Reichweite am 24. September festhalten.

Für die Beschaffung bin ich weiterhin von 1.200 Stück pro Jahr und 300 Stück je Quartal ausgegangen. Diese Menge stand im August in Ihrer Planung. Wir haben 360 Messkerne MK-42 beim Vorlieferanten reserviert, davon 240 bereits bestellt. Die Reserve ist bis zum 24. September, 12 Uhr kostenfrei löschbar; die 240 bestellten Kerne sind es nicht mehr. Eine gesonderte Einkaufsnummer von Ihnen habe ich dafür nicht.

Den Preisnachlass von 3 % können wir bei dieser Menge halten. Wenn die ersten Lose kleiner als 100 Stück werden, bleibt der Rüstzuschlag relevant. Bitte schicken Sie uns die konkreten Oktobermengen vor unserem Gespräch. Sonst steht die geplante Fertigungswoche ab 12. Oktober nur unter Vorbehalt im Kalender.

Freundliche Grüße
Paul Reuter
Vertrieb, Talbruck Sensorik GmbH
Gewerbepark 17, 52249 Eschweiler
Telefon 02403 748 61 24""", cc="Dr. Selma Berg <selma.berg@talbruck-sensorik.de>")
    eml(d / "21_kaeufer_abrufe_und_revision.eml", "Eva Schulte <eva.schulte@rheinkern-anlagenbau.de>", "Paul Reuter <paul.reuter@talbruck-sensorik.de>", "2026-09-21T14:08:00+02:00", "Re: D400 / Terminabfrage 60, 80 und 100 Stück, Forecast 2027", """Guten Tag Herr Reuter,

anbei der heutige Export aus unserem Bestellsystem. Wir fragen für 2026 Termine für 60, 80 und 100 Stück an, also zusammen 240 Stück. Die zwölf Versuchsmuster sind darin nicht enthalten. Die vier Zeilen mit je 300 Stück betreffen das Kalenderjahr 2027 und sind ausdrücklich Forecast. Sie sind keine bestätigten Abrufe und keine Mindestabnahme.

Bitte bestätigen Sie, welche Termine nach Abschluss der Messprüfung möglich wären. Für die erste Serie steht die Revision noch offen. Herr Frings hat am 15. September zwölf Muster freigegeben, nicht die geänderte Toleranz für sämtliche Lieferungen. Unsere Qualitätsleitung hat bisher keine Serienfreigabe versandt. Die Prüfung im Aufbau ist erst am 29. September, danach können wir sagen, ob C für unsere Anlage genügt.

Eine Materialbestellung über 240 oder 360 Messkerne haben wir nicht freigegeben. Bitte senden Sie eine Liste, die bestellte, nur reservierte und bereits verbaute Teile unterscheidet. Frau Küppers möchte außerdem wissen, welche Reservierungen am Donnerstag noch kostenlos aufgehoben werden können. Den Lieferrahmen möchten wir weiter verhandeln; die heutigen Terminfragen sind keine Zustimmung zu Ihrem Stand 0.6.

Viele Grüße
Eva Schulte
Einkauf, Rheinkern Anlagenbau GmbH
Jülicher Straße 318, 52070 Aachen
Telefon 0241 936 42 31""", cc="Miriam Küppers <miriam.kueppers@rheinkern-anlagenbau.de>, Anja Heil <anja.heil@rheinkern-anlagenbau.de>", attachments=["11_erp_abrufe_20260921.csv"], reply="<20_lieferant_mengen_toleranzen@talbruck-sensorik.de>")
    csv_file(d / "22_lager_und_beschaffung_20260922.csv", ["Stand","Teilenummer","Bezeichnung","Stufe","Menge_Stück","Einstand_EUR_je_Stück","Beleg","Bestelldatum","Stornofrist","Projektzuordnung","Bemerkung"], [
        ["2026-09-22","MK-41","Messkern alt","Lager verfügbar",96,"61.00","LG-260922-41","2026-06-18","","D400 noch nicht exklusiv","Kein Teil der 360 MK-42"],
        ["2026-09-22","MK-42","Messkern neu","Fest bestellt, noch nicht geliefert",240,"64.00","TB-EK-260916-77","2026-09-16","keine","Rheinkern intern vorgemerkt","Vorlieferant bestätigt 25.09.; keine Käuferfreigabenummer"],
        ["2026-09-22","MK-42","Messkern neu","Nur reserviert",120,"64.00","TB-RES-260918-12","2026-09-18","2026-09-24T12:00:00+02:00","Rheinkern intern vorgemerkt","Kostenfrei lösbar; zusammen mit Festbestellung 360"],
        ["2026-09-22","GEH-D400","Leergehäuse","Gefertigt, unbestückt",120,"18.00","FA-260917-32","2026-09-17","keine","Rheinkern intern vorgemerkt","Keine Messkerne enthalten"],
        ["2026-09-22","PCB-D400","Leiterplatte","Bestückt ohne Messkern",48,"27.50","FA-260918-04","2026-09-18","keine","D400 allgemein","MK-42 noch nicht eingesetzt; auch für andere D400 nutzbar"],
        ["2026-09-22","D400-C-MUSTER","Versuchssensor komplett","Ausgeliefert",12,"0.00","LS-260917-14","2026-08-28","","RK-WZ-260828","Nicht Lagerbestand; im Werkzeugpreis enthalten"],
    ])
    docx(d / "23_schreiben_bestaende_vertragsende.docx", T, "Bestände und Übergabe bei Projektende", [("Datum", "22.09.2026"), ("An", "Rheinkern Anlagenbau GmbH, Frau Miriam Küppers, Jülicher Straße 318, 52070 Aachen"), ("Unser Zeichen", "HV / D400 / 26-92"), ("Anlage", "22_lager_und_beschaffung_20260922.csv, im Projektportal bereitgestellt")], [
        (None, ["Sehr geehrte Frau Küppers,\nFrau Schulte hat um eine Trennung der Beschaffungsstände gebeten. Die beigefügte Portalliste enthält 240 fest bestellte Messkerne und 120 nur reservierte Kerne. Es handelt sich also nicht um 360 bereits vorhandene Sensoren. Die zwölf gelieferten Muster sind gesondert aufgeführt und keine zusätzliche Serienbestellung."]),
        ("1. Beschaffung", ["Die feste Bestellung vom 16. September erfolgte aus unserem Vertrieb heraus nach den Telefonaten zur Expressbemusterung. Eine schriftliche Materialfreigabe Ihres Einkaufs kann ich derzeit nicht beifügen. Ich möchte die Bestandsthematik deshalb im Vertragsgespräch am Donnerstag behandeln. Die Reservierung über 120 Kerne kann bis 12 Uhr desselben Tages ohne Kosten aufgehoben werden. Bitte geben Sie uns vorher Nachricht, ob Sie diese Reserve für die weitere Planung halten möchten."]),
        ("2. Werkzeug und Restmaterial", ["Das Werkzeugpaket ist bezahlt und mit Ihrer Projektnummer gekennzeichnet. Es liegt in unserem Werkzeugraum, nicht beim Vorlieferanten. Für die von Ihnen gewünschte Herausgabe bei Vertragsende brauchen wir eine Vereinbarung über Verpackung und Termin. Die universelle Grundaufnahme unserer Maschine gehört nicht zum bezahlten Paket. Bei den 120 Leergehäusen prüfen wir noch, ob sie für andere D400-Projekte verwendet werden können. Die 48 bestückten Leiterplatten ohne Messkern sind nicht exklusiv für Rheinkern."]),
        ("3. Fortsetzung", ["Wir möchten den Rahmen für drei Jahre abschließen, benötigen aber einen beschaffbaren Vorlauf. Eine unbeschränkte Übernahme von Service- und Stillstandskosten kann ich auf Basis der bisher genannten Daten nicht zusagen. Bitte bringen Sie die angekündigte Kostengliederung und Ihren Vorschlag zum Umgang mit freigegebenem Restmaterial mit. Bis zur Besprechung haben wir keine weiteren Kerne bestellt."])
    ], "Mit freundlichen Grüßen\nHenning Voß\nGeschäftsführer")
    eml(d / "24_rechtsabteilung_verhandlung.eml", "Miriam Küppers <miriam.kueppers@rheinkern-anlagenbau.de>", "Jonas Westphal <jonas.westphal@rheinkern-anlagenbau.de>", "2026-09-23T08:47:00+02:00", "D400 / Vertragsgespräch am 24. September, 10 Uhr", """Guten Morgen Herr Westphal,

bitte begleiten Sie als unsere Rechtsabteilung die morgige Verhandlung mit Talbruck. Eva hat beide Vertragsfassungen in den Projektordner gestellt; ich hänge sie und das Schreiben von Herrn Voß nochmals an. Wir wollen einen dreijährigen Lieferrahmen, aber die Jahresplanung von 1.200 Stück ist noch nicht durch Anlagenaufträge gedeckt. Der Ausgangspreis von 186 EUR netto ist in der Kalkulation berücksichtigt. Über Mengenstaffel und kleinere Anlauflose müssen wir noch sprechen.

Das Werkzeug ist mit 14.756 EUR brutto bezahlt. Zwölf Muster sind tatsächlich angekommen. Die ersten Messungen bei Raumtemperatur liegen vor, der Aufbauversuch folgt am 29. September. Vertrieb und Konstruktion scheinen unter dem Telefonat zur Expressfreigabe unterschiedliche Dinge verstanden zu haben. Ich möchte vor dem Gespräch wissen, welche Rückfragen wir dazu noch an Frings und Berg stellen sollten.

Bitte stimmen Sie mit Eva einen verhandelbaren Text zu Abrufen, Änderungen, Qualität, Werkzeug und dem Bestand bei Vertragsende ab. Zu möglichen Rückrufkosten kann unser Serviceleiter heute bis 15 Uhr den letzten vergleichbaren Einsatz erläutern. Ein Anlagenstillstand kann teuer werden, aber wir haben hierfür noch keine verbindliche Kalkulation. Versprechen Sie bitte weder eine feste Jahresmenge noch die Übernahme der bereits bestellten Kerne ohne meine Rücksprache.

Die Reservierung über weitere 120 Kerne läuft morgen um 12 Uhr aus. Wenn wir sie halten wollen, brauche ich vor Ablauf die Menge und den maximalen Betrag auf dem Tisch. Die Rechnung und der Bankbeleg betreffen nur Werkzeug und Muster, nicht die Serie.

Viele Grüße
Miriam Küppers
Geschäftsführerin, Rheinkern Anlagenbau GmbH
Jülicher Straße 318, 52070 Aachen
Telefon 0241 936 42 12
Amtsgericht Aachen HRB 24681""", cc="Eva Schulte <eva.schulte@rheinkern-anlagenbau.de>", attachments=["03_rahmenvertrag_lieferant_v06.docx", "04_gegenvorschlag_rheinkern_v08.docx", "23_schreiben_bestaende_vertragsende.docx"])
    measurement_png(d / "25_messplatz_muster_05.png")
    readme(d, "Rahmenlieferung von D400-Sensoren nach Aachen", "corporate-contract-law", "Rheinkern Anlagenbau GmbH und Talbruck Sensorik GmbH verhandeln im September 2026 einen dreijährigen Lieferrahmen. Vorhanden sind getrennte Vertragsfassungen, ein Angebot, zwei technische Revisionen, Korrespondenz und betriebliche Aufzeichnungen. Werkzeugzahlung, zwölf angelieferte Muster und ein begrenzter Messversuch stehen neben noch nicht bestätigten Serienterminen und einer Jahresplanung von 1.200 Stück.", AACHEN_FILES)


def measurement_png(path):
    im = Image.new("RGB", (1440, 920), "#f2f4f5")
    draw = ImageDraw.Draw(im)
    def f(size):
        return ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", size)
    draw.rectangle((0, 0, 1440, 65), fill="#29383f")
    draw.text((30, 21), "RHEINKERN   /   Messwerterfassung RK-LM-18", fill="white", font=f(23))
    draw.text((36, 102), "Versuchsreihe RK-QM-260918", fill="#26373f", font=f(34))
    draw.text((38, 155), "18.09.2026, 10:52:14   ·   Benutzerin Anja Heil   ·   Prüfling 05 / 12", fill="#55656b", font=f(22))
    for y, label, value in [(224,"Seriennummer","D400-C-260915-05"),(275,"Etikett / Firmware","Revision C / 2.8"),(326,"Referenzabstand","200,00 mm"),(377,"Raumtemperatur","23,1 °C"),(428,"Versorgung / Aufwärmzeit","24,02 V / 10 min")]:
        draw.text((38,y),label,fill="#607078",font=f(22))
        draw.text((390,y),value,fill="#1f3039",font=f(24))
    draw.rectangle((38,504,1402,552),fill="#dce4e8")
    for x,label in [(60,"Ablesung"),(300,"Zeitpunkt"),(630,"Messwert mm"),(1000,"Referenz mm")]:
        draw.text((x,517),label,fill="#26373f",font=f(22))
    for index, (stamp, value) in enumerate([("10:52:10","200,28"),("10:52:12","200,31"),("10:52:14","200,29")],1):
        y=565+(index-1)*52
        for x,txt in [(60,str(index)),(300,stamp),(630,value),(1000,"200,00")]:
            draw.text((x,y),txt,fill="#20353d",font=f(24))
    draw.line((38,737,1402,737),fill="#bccad0",width=2)
    draw.text((38,770),"Aufzeichnung gespeichert   ·   3 Ablesungen   ·   Nullabgleich vor Beginn",fill="#385953",font=f(22))
    draw.text((38,819),"Temperaturreihe: nicht gestartet   |   Anlagenaufbau: nicht geprüft",fill="#52636b",font=f(21))
    draw.text((38,861),"Versuchsmuster / Freigabedokument zur Serie: nicht hinterlegt",fill="#52636b",font=f(21))
    im.save(path)


AACHEN_FILES = [
    ("01_lieferantenstamm_d400.docx", "Firmenstamm, Vertretung und Zuständigkeiten"),
    ("02_angebot_ts_260902.pdf", "Angebot mit Staffel, Rüstzuschlag und Lieferort"),
    ("03_rahmenvertrag_lieferant_v06.docx", "Ausformulierter Lieferantenentwurf 0.6"),
    ("04_gegenvorschlag_rheinkern_v08.docx", "Ausformulierter Käufergegenvorschlag 0.8"),
    ("05_datenblatt_d400_rev_b.pdf", "Technisches Datenblatt Revision B"),
    ("06_datenblatt_d400_rev_c.pdf", "Technisches Datenblatt Revision C"),
    ("07_versand_angebot_entwurf.eml", "Angebotsversand mit drei Dateianhängen"),
    ("08_versand_gegenvorschlag.eml", "Käuferantwort mit Gegenfassung als Anhang"),
    ("09_bauteilabkuendigung.eml", "Bauteilabkündigung und Bitte um Musterentscheidung"),
    ("10_expressfreigabe_muster.eml", "Antwort der Konstruktion zur Versuchslieferung"),
    ("11_erp_abrufe_20260921.csv", "Terminabfragen 2026 und Forecast 2027"),
    ("12_preisstaffeln_d400.xlsx", "Berechnete Preise und Anlaufkosten"),
    ("13_bestellung_werkzeug.eml", "Separate Bestellung von Werkzeug und zwölf Mustern"),
    ("14_werkzeugrechnung_ts_2026_491.pdf", "Rechnung über Werkzeug und Bemusterung"),
    ("15_zahlungsbeleg_werkzeug.pdf", "Ausgeführte Werkzeugzahlung"),
    ("16_werkzeugblatt_wz_d400_17.docx", "Fertigungs- und Verwahrstand des Werkzeugs"),
    ("17_lieferschein_muster_ls_260917.pdf", "Musterlieferung mit Wareneingangsvermerk"),
    ("18_messwerte_muster_200mm.csv", "Drei Raumtemperaturmessungen je Muster"),
    ("19_pruefprotokoll_muster.docx", "Prüfaufbau und Umfang der Messreihe"),
    ("20_lieferant_mengen_toleranzen.eml", "Lieferantensicht zu Menge und Revision"),
    ("21_kaeufer_abrufe_und_revision.eml", "Käuferantwort mit ERP-Auszug"),
    ("22_lager_und_beschaffung_20260922.csv", "Bestellte, reservierte und bearbeitete Komponenten"),
    ("23_schreiben_bestaende_vertragsende.docx", "Geschäftsführerschreiben zu Bestand und Übergabe"),
    ("24_rechtsabteilung_verhandlung.eml", "Interne E-Mail vor dem Vertragsgespräch"),
    ("25_messplatz_muster_05.png", "Messplatzanzeige des fünften Versuchsmusters"),
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", choices=["dortmund", "aachen", "both"], default="both")
    args = parser.parse_args()
    if args.case in ("dortmund", "both"):
        dortmund()
    if args.case in ("aachen", "both"):
        aachen()


if __name__ == "__main__":
    main()
