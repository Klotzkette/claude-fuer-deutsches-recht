#!/usr/bin/env python3
"""Native Quellen der Kasseler Wartungsverhandlung; kein Release- oder ZIP-Bau.

Aufruf mit .venv/bin/python. SOFFICE bezeichnet die vorhandene Headless-Runtime.
Office-Zwischendateien liegen ausschließlich in automatisch bereinigten Tempverzeichnissen.
"""

from __future__ import annotations

import csv
from datetime import datetime
from email import policy
from email.message import EmailMessage
from email.utils import format_datetime
import mimetypes
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
from xml.sax.saxutils import escape

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from openpyxl import load_workbook
from PIL import Image, ImageDraw
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)

from akten_build_runtime import node_binary, screen_font
from akten_docx_format import separate_section_headings
from office_process import run_office
from testakte_office_pdf import office_binary


ROOT = Path(__file__).resolve().parents[1]
SLUG = "vertragserstellung-wartungsvertrag-druckerei-kassel"
CASE = ROOT / "testakten" / SLUG
FILES = {
    1: "01_2026-09-14_Druckerei_Vertragsfortsetzung.eml",
    2: "02_Altvertrag_WS-2023-44.pdf",
    3: "03_Anlagenregister_Kassel_2026-09-08.pdf",
    4: "04_Schichtbuch_2026-09-10_bis_12.csv",
    5: "05_Wartung_K1_2026-08-19.pdf",
    6: "06_Wartung_K2_2026-08-20.pdf",
    7: "07_Anrufnotiz_2026-09-12.txt",
    8: "08_Servicebericht_SR-260912.pdf",
    9: "09_Rechnung_WS-260701.pdf",
    10: "10_Rechnung_WS-260914.pdf",
    11: "11_Zahlungsjournal_2026-09-22.csv",
    12: "12_Angebot_WS-260828.pdf",
    13: "13_2026-08-28_Angebotsmail.eml",
    14: "14_Remotezugang_RZ-06.pdf",
    15: "15_2026-09-16_Einkauf_Leistungsumfang.eml",
    16: "16_Lieferantenfassung_2026-09-18.docx",
    17: "17_Aufstellplan_Halle2_2026-09-08.png",
    18: "18_Betriebschat_2026-09-15.txt",
    19: "19_2026-09-18_Lieferant_Vertragsfassung.eml",
    20: "20_Druckereifassung_2026-09-21.docx",
    21: "21_2026-09-22_Einkauf_Gegenfassung.eml",
    22: "22_Kostenvergleich_2027.xlsx",
    23: "23_Umbauangebot_U-260917.pdf",
    24: "24_Materialentnahmen_2026.csv",
    25: "25_Budgetansatz_Einkauf_2026-09-22.pdf",
    26: "26_2026-09-23_Lieferant_Rueckmeldung.eml",
}

PRINTER = {
    "name": "Fuldabogen Spezialdruck GmbH",
    "line": "Sonderdruck und technische Etiketten",
    "address": "Am Farbhof 18 · 34123 Kassel",
    "contact": "einkauf@fuldabogen-spezialdruck.de · Zentrale 0561 000 8420",
    "footer": "Fuldabogen Spezialdruck GmbH · Geschäftsführung Maren Brückner · Sitz Kassel",
    "color": "#344b40",
}
SERVICE = {
    "name": "Werkspur Maschinenservice GmbH",
    "line": "Servicezentrum Nordhessen",
    "address": "Werkhof 7 · 34253 Lohfelden",
    "contact": "service@werkspur-maschinenservice.de · Disposition 0561 000 9170",
    "footer": "Werkspur Maschinenservice GmbH · Geschäftsführung Dirk Seidel · Sitz Lohfelden",
    "color": "#394754",
}


def register_fonts():
    choices = [Path(os.environ["AKTEN_FONT_DIR"]).expanduser()] if os.environ.get("AKTEN_FONT_DIR") else []
    choices += [Path("/System/Library/Fonts/Supplemental"), Path("/usr/share/fonts/truetype/msttcorefonts"),
                Path("/usr/share/fonts/truetype/liberation2"), Path("/usr/share/fonts/truetype/liberation"),
                Path(os.environ.get("WINDIR", "C:/Windows")) / "Fonts"]
    for directory in choices:
        for regular, bold in [("Times New Roman.ttf", "Times New Roman Bold.ttf"),
                              ("times.ttf", "timesbd.ttf"),
                              ("LiberationSerif-Regular.ttf", "LiberationSerif-Bold.ttf")]:
            if (directory / regular).is_file() and (directory / bold).is_file():
                pdfmetrics.registerFont(TTFont("CaseSerif", str(directory / regular)))
                pdfmetrics.registerFont(TTFont("CaseSerifBold", str(directory / bold)))
                pdfmetrics.registerFontFamily("CaseSerif", normal="CaseSerif", bold="CaseSerifBold")
                return
    raise RuntimeError("Times New Roman oder Liberation Serif fehlt; AKTEN_FONT_DIR verwenden.")


BODY = ParagraphStyle("Text", fontName="CaseSerif", fontSize=11, leading=14.2, spaceAfter=8)
HEAD = ParagraphStyle("Abschnitt", parent=BODY, fontName="CaseSerifBold", spaceBefore=7, spaceAfter=11,
                      keepWithNext=True)
SMALL = ParagraphStyle("Klein", parent=BODY, fontSize=9.2, leading=11.5, spaceAfter=5)
TITLE = ParagraphStyle("Titel", parent=HEAD, fontSize=16, leading=19, spaceAfter=14)


def para(text, style=BODY):
    return Paragraph(escape(text).replace("\n", "<br/>"), style)


def tab(rows, widths):
    table = Table([[para(str(cell), SMALL) for cell in row] for row in rows], colWidths=widths,
                  repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e9edf0")),
        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#c7cccf")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


def pdf(number, issuer, recipient, date, reference, title, greeting, content, signer):
    path = CASE / FILES[number]

    def frame(canvas, document):
        canvas.saveState()
        canvas.setFillColor(colors.HexColor(issuer["color"]))
        canvas.setFont("CaseSerifBold", 16)
        canvas.drawString(50, 798, issuer["name"])
        canvas.setFillColor(colors.black)
        canvas.setFont("CaseSerif", 9)
        canvas.drawString(50, 783, issuer["line"])
        canvas.drawRightString(545, 782, issuer["address"])
        canvas.setFont("CaseSerif", 8)
        canvas.drawString(50, 768, issuer["contact"])
        canvas.setStrokeColor(colors.HexColor(issuer["color"]))
        canvas.line(50, 760, 545, 760)
        canvas.setFont("CaseSerif", 8)
        canvas.drawString(50, 39, issuer["footer"])
        canvas.drawString(50, 27, reference)
        canvas.drawRightString(545, 27, f"Seite {document.page}")
        canvas.restoreState()

    story = [para(recipient, SMALL), para(f"{date} · Bezug: {reference}", SMALL), Spacer(1, 6),
             para(title, TITLE), para(greeting)]
    for item in content:
        if isinstance(item, str):
            story.append(para(item))
        elif item[0] == "h":
            story.append(para(item[1], HEAD))
        elif item[0] == "table":
            story.extend([tab(item[1], item[2]), Spacer(1, 10)])
        elif item[0] == "page":
            story.append(PageBreak())
    closing = [para("Mit freundlichen Grüßen"), para(signer)]
    # Die letzte Sachpassage bleibt mit der Zeichnung auf derselben Seite.
    story[-1:] = [KeepTogether(story[-1:] + [Spacer(1, 7)] + closing)]
    SimpleDocTemplate(str(path), pagesize=A4, leftMargin=50, rightMargin=50, topMargin=100,
                      bottomMargin=61, title=title, author=issuer["name"]).build(
                          story, onFirstPage=frame, onLaterPages=frame)


def make_pdfs():
    pdf(2, SERVICE, "Fuldabogen Spezialdruck GmbH\nFrau Maren Brückner · Am Farbhof 18 · 34123 Kassel",
        "15. Dezember 2023", "WS-2023-44 · Kundenkonto FB-118", "Wartungsvereinbarung für Halle 2",
        "Sehr geehrte Frau Brückner, sehr geehrter Herr Seidel,", [
        "Fuldabogen Spezialdruck GmbH, vertreten durch Maren Brückner, beauftragt die Werkspur Maschinenservice GmbH, vertreten durch Dirk Seidel, mit den nachstehenden Arbeiten an den bereits betriebenen Drucklinien. Ein Erwerb oder eine Vermietung von Maschinen ist nicht Gegenstand dieser Vereinbarung.",
        ("h", "1 Anlagen und vorhandener Zustand"),
        "Erfasst sind die Sonderoffsetlinie K1, Typ FB-450, Baujahr 2018, Seriennummer K1-18442, und die Siebdrucklinie K2, Typ SD-720, Baujahr 2020, Seriennummer K2-20117. Die Versorgungseinheit P-17 der K2 gehört zur Linie. Die K1 besitzt vier Druckwerke und den UV-Trockner U1; die K2 besitzt den IR-Trockner T2. Beide Trockner werden bei der planmäßigen Wartung mit geprüft. Nicht erfasst sind Hallenkompressor, Absaugzentrale, Netzwerkinfrastruktur und Produktionsleitsystem der Druckerei. Neue Komponenten werden nur durch eine beiderseitige Ergänzung aufgenommen.",
        ("h", "2 Planmäßige Wartung"),
        "Werkspur führt jährlich im April und August je einen Wartungstermin an jeder Linie durch. Ein Termin umfasst Reinigung zugänglicher Sensoren, Schmierung, Prüfung der Antriebsriemen, der Führungen, der Temperaturregelung und der Schutzeinrichtungen sowie einen dokumentierten Probelauf. Die Druckerei stellt jede Linie für vier Stunden frei und stellt einen eingewiesenen Bediener. Ein ausgefallener Termin wird innerhalb von vier Wochen nachgeholt. Die Terminverschiebung allein verlängert die Vertragslaufzeit nicht.",
        "Arbeitszeit und Anfahrt dieser vier planmäßigen Termine sind in der Pauschale enthalten. Für planmäßige Wartung entnommene Filter, Rollen und Dichtungen sind zusammen bis zu 400,00 EUR netto je Kalenderjahr enthalten. Nicht verbrauchtes Materialbudget verfällt zum Jahresende. Störungsbedingte Teile und darüber hinausgehender Verbrauch werden nach Freigabe gesondert berechnet.",
        ("h", "3 Störungsmeldung und Einsatz"),
        "Meldungen nimmt die Disposition montags bis freitags von 07:00 bis 17:00 Uhr entgegen; gesetzliche Feiertage in Hessen sind ausgenommen. Werkspur bestätigt eine Meldung innerhalb von vier Service-Stunden und vereinbart anschließend einen Einsatz. Eine bestimmte Wiederherstellungszeit wird nicht geschuldet. Außerhalb dieser Zeiten kann die Druckerei die bekannte Störungsnummer anwählen. Ein erreichbarer Techniker darf einen Einsatz übernehmen; eine ständig besetzte Rufbereitschaft ist nicht Bestandteil der Pauschale.",
        ("page",),
        ("h", "4 Vergütung und Freigaben"),
        "Die jährliche Wartungspauschale beträgt 19.200,00 EUR netto. Sie wird in vier gleichen Teilbeträgen von 4.800,00 EUR netto zu Beginn jedes Kalenderquartals in Rechnung gestellt. Hinzu kommt die gesetzliche Umsatzsteuer. Die Zahlung ist jeweils 14 Kalendertage nach Rechnungsdatum ohne Abzug fällig. Der Preis gilt für die gesamte feste Laufzeit; eine jährliche Preisänderung ist nicht vorgesehen.",
        "Störungsarbeiten werden mit 112,00 EUR netto je Technikerstunde nach tatsächlich angefallenen Viertelstunden berechnet. Remote-Arbeit und Arbeit vor Ort dürfen nicht zeitgleich doppelt berechnet werden. Für einen übernommenen Einsatz zwischen 17:00 und 07:00 Uhr oder am Wochenende fallen einmalig 240,00 EUR netto an. Die Anfahrtspauschale beträgt je Einsatz 145,00 EUR netto einschließlich Fahrzeit. Ersatzteile werden nach dem vor Einbau genannten Nettopreis abgerechnet. Ohne Freigabe darf Werkspur Maßnahmen bis insgesamt 1.000,00 EUR netto je Störung ausführen. Darüber hinaus genügt die telefonisch dokumentierte Zustimmung der Betriebsleitung.",
        ("h", "5 Mitwirkung und Fernzugriff"),
        "Die Druckerei hält die täglichen Reinigungs- und Kontrollintervalle ein, bewahrt Fehlermeldungen auf und gewährt sicheren Zugang. Arbeiten unter Spannung oder bei geöffneten Schutzhauben sind der Druckerei nicht aufgegeben. Eine Fernverbindung darf nur nach Freigabe des Schichtleiters und nur für den einzelnen Einsatz geöffnet werden. Werkspur protokolliert Beginn, Ende und ausgeführte Änderungen. Ein dauerhafter Zugang oder die Übertragung von Druckauftragsdaten wird hierdurch nicht gestattet.",
        ("h", "6 Reparaturen und Änderungen"),
        "Der Austausch eines verschlissenen Teils setzt die restliche Anlage nicht in einen neuwertigen Zustand. Werkspur dokumentiert das ausgetauschte Teil, das Fehlerbild und den Probelauf. Zusätzliche Umbauten mit geänderter Steuerungslogik werden separat angeboten. Sie werden nach gemeinsamem Funktionstest abgenommen. Die bloße Wiederaufnahme der Produktion nach einer Entstörung stellt keine Abnahme eines später angebotenen Umbaus dar. Mängel eigener Arbeiten beseitigt Werkspur nach Meldung ohne zusätzliche Arbeitsvergütung.",
        ("h", "7 Verantwortung und Schäden"),
        "Werkspur haftet unbeschränkt bei Vorsatz, grober Fahrlässigkeit und Schäden aus Verletzung von Leben, Körper oder Gesundheit. Bei leicht fahrlässiger Verletzung einer wesentlichen Vertragspflicht ist die Haftung auf den bei Vertragsschluss vorhersehbaren, vertragstypischen Schaden begrenzt, höchstens jedoch auf 50.000,00 EUR je Kalenderjahr. Im Übrigen ist eine Haftung für leichte Fahrlässigkeit ausgeschlossen. Zwingende Haftung bleibt unberührt. Die Druckerei meldet Schäden zeitnah und erhält ausgebaute Teile auf Verlangen zur Untersuchung zurück.",
        ("page",),
        ("h", "8 Laufzeit und Vertragsende"),
        "Die Vereinbarung beginnt am 1. Januar 2024 und endet ohne Kündigung am 31. Dezember 2026. Eine automatische Verlängerung findet nicht statt. Beide Parteien können aus wichtigem Grund kündigen; bei einer behebbaren Pflichtverletzung ist grundsätzlich zuvor eine angemessene Abhilfefrist zu setzen. Bei Vertragsende gibt Werkspur noch nicht übermittelte Wartungsprotokolle heraus und schließt bestehende Fernverbindungen. Bis zum Vertragsende bereits beauftragte Einzelreparaturen sind zu den vereinbarten Bedingungen fertigzustellen, soweit die Parteien nichts anderes abstimmen.",
        ("h", "9 Ansprechpartner und Erklärungen"),
        "Für die Druckerei ist René Möller für technische Freigaben, für Werkspur Tobias Grebe für Einsatzplanung zuständig. Vertragsänderungen bedürfen der Bestätigung durch die Geschäftsführungen in Textform. Technische Freigaben nach Ziffer 4 sind davon nicht betroffen. Diese Vereinbarung enthält die vollständige Leistungs- und Vergütungsabrede; weitere Anlagen oder allgemeine Geschäftsbedingungen werden nicht einbezogen. Für die Vereinbarung gilt deutsches Recht. Als Gerichtsstand vereinbaren die Parteien Kassel.",
        "Die Parteien bestätigen, dass ihnen die Ausfertigung mit allen neun Ziffern vorliegt. Die erste Terminabstimmung erfolgt im März 2024. Das Kundenkonto FB-118 wird auch für gesonderte Reparaturrechnungen verwendet.",
        ], "gez. Maren Brückner · Geschäftsführerin · Kassel, 15.12.2023\ngez. Dirk Seidel · Geschäftsführer · Lohfelden, 15.12.2023")

    pdf(3, PRINTER, "Werkspur Maschinenservice GmbH · Herrn Tobias Grebe", "8. September 2026",
        "FB-118 · Anlagenstand AR-09", "Anlagenregister Halle 2", "Sehr geehrter Herr Grebe,", [
        "für die Vertragsfortsetzung erhalten Sie den abgeglichenen Anlagenstand. Die Maschinen verbleiben am bisherigen Standort. Die Betriebsstundenzähler zählen eingeschaltete Linien, nicht die Zahl der gleichzeitig eingesetzten Mitarbeiter.",
        ("table", [
            ["Kennung", "Bestand und Seriennummer", "Einbindung"],
            ["K1", "FB-450 · K1-18442 · 2018\nVier Druckwerke, UV-Trockner U1", "Etiketten auf Metallfolie; 2 bis 3 Schichten"],
            ["K2", "SD-720 · K2-20117 · 2020\nIR-Trockner T2, Versorgung P-17", "Sonderfarben auf Kunststoff; 3 Schichten"],
            ["Z1", "Zuführmodul ZF-22 · Z1-22083 · 2022", "Fremdfabrikat vor K1; gemeinsamer Not-Halt"],
            ["G1", "Gateway GW-19 · G1-19006 · 2019", "Wartungsnetz, bislang lokal freigeschaltet"],
        ], [49, 242, 204]),
        "Z1 wurde von unserer Werkstatt 2022 mechanisch angebaut. Die Not-Halt-Kette beider Module ist gekoppelt. Die Zuordnung in Ihren älteren Wartungslisten nennt Z1 nicht. Der Linienbediener sieht jedoch nur eine gemeinsame Störanzeige. Im Aufstellplan sind die Übergabepunkte und der Hauptschalter eingezeichnet.",
        "Zähler am 31.08.2026: K1 28.440 h, K2 31.910 h. Für Januar bis August ergeben unsere Monatsablesungen zusammen 7.260 h. Das ist ein Zwischenstand, keine Jahreshochrechnung. Die geplanten Stunden 2027 folgen gesondert aus dem Einkauf, weil zwei neue Nachtaufträge erst ab Januar anlaufen sollen.",
        "Kompressor, zentrale Absaugung, Hallennetz und Leitstand bleiben bei unserer Haustechnik. Bitte sagen Sie uns ausdrücklich, ob Sie Z1, die Trockner und das Gateway in Ihrem neuen Preis mitführen. Ein zusätzliches Rücklaufmodul an K2 ist noch nicht eingebaut.",
        f"Anlage: {FILES[17]}. Die Maße dienen der Einsatzplanung; sie ersetzen kein Aufmaß für einen Umbau.",
        ], "René Möller\nBetriebsleiter")

    pdf(5, SERVICE, "Fuldabogen Spezialdruck GmbH · Betriebsleitung", "19. August 2026",
        "W-260819 · K1-18442 · WS-2023-44", "Wartungsprotokoll K1", "Sehr geehrter Herr Möller,", [
        "Miriam Hesse führte die planmäßige Wartung von 08:00 bis 12:00 Uhr durch. Die Linie war leergefahren, die UV-Lampen waren vor Arbeitsbeginn abgekühlt. Der Zähler zeigte 28.210 h. Ihr Bediener Jan Faber begleitete den Probelauf.",
        ("table", [["Prüfbereich", "Befund und ausgeführte Arbeit"],
            ["Antrieb und Führung", "Führungen gereinigt und geschmiert. Riemenspannung nachgestellt; kein Austausch erforderlich."],
            ["Sensorik", "Registersensor S4 gereinigt. Zwei Filter F-8 zu je 48,00 EUR netto erneuert."],
            ["Auslage", "Andruckrolle R-12 zu 160,00 EUR netto erneuert. Gleichmäßiger Lauf bei 4.800 Bogen/h."],
            ["UV-Trockner U1", "Temperatur 51 °C nach 20 Minuten. Verriegelung geprüft; keine Sicherheitsüberbrückung."],
            ["Zuführmodul Z1", "Not-Halt-Kette gemeinsam ausgelöst. Das Fremdmodul wurde nicht geöffnet und nicht gewartet."],
        ], [110, 385]),
        "Der Wartungsverbrauch von 256,00 EUR netto wird dem jährlichen Materialkontingent nach Ziffer 2 des Altvertrags zugeordnet. In dieser Summe sind nur die oben genannten Filter und die Rolle enthalten. Eine gesonderte Rechnung für diese Entnahme wird nicht gestellt.",
        "Beim Hochfahren rutschte ein steifer Folienbogen am Übergang Z1/K1. Nach Ausrichten der Anschläge trat der Effekt im 20-minütigen Probelauf nicht erneut auf. Die Ursache ist damit nicht abschließend bestimmt. Herr Möller möchte die Einlaufstrecke beim nächsten Besuch mit dem Zuführhersteller ansehen; ein Termin ist nicht vereinbart.",
        "Die K1 wurde um 12:00 Uhr für die Produktion zurückgegeben. Die Übergabe bestätigt die ausgeführten Wartungsarbeiten, nicht die Abnahme einer veränderten Zuführkonstruktion.",
        ], "Miriam Hesse · Servicetechnikerin\nKenntnis genommen: René Möller · Betriebsleiter")

    pdf(6, SERVICE, "Fuldabogen Spezialdruck GmbH · Betriebsleitung", "20. August 2026",
        "W-260820 · K2-20117 · WS-2023-44", "Wartungsprotokoll K2", "Sehr geehrter Herr Möller,", [
        "Die zweite Augustwartung fand von 07:30 bis 11:30 Uhr statt. Techniker war Tobias Grebe, begleitende Bedienerin Selin Krüger. Der Zähler der K2 stand bei 31.620 h. Die Linie wurde vor Beginn gereinigt und spannungsfrei geschaltet.",
        ("table", [["Prüfbereich", "Messung oder Beobachtung"],
            ["Versorgung P-17", "Betriebsdruck 4,8 bar; Sollbereich 4,5 bis 5,1 bar. Dichtungssatz D-17 für 125,00 EUR netto erneuert."],
            ["Rücklauf", "Pulsation nur beim Farbwechsel sichtbar. Schlauchoberfläche ohne Riss; kein Austausch beauftragt."],
            ["IR-Trockner T2", "Regelung bei 82 °C stabil. Temperaturfühler und Türverriegelung geprüft."],
            ["Schutzfunktionen", "Not-Halt und Wiederanlaufsperre ausgelöst. Keine Abweichung im Probelauf."],
        ], [110, 385]),
        "Das Dichtungsmaterial fällt in das Wartungskontingent. Zusammen mit den Entnahmen an K1 vom Vortag sind im vorliegenden Augustpaket 381,00 EUR netto verbraucht. Die planmäßige Aprilwartung benötigte kein Kontingentmaterial. Es verbleiben 19,00 EUR netto im Jahreskontingent.",
        "Herr Grebe vermutet, dass die Pulsation mit den zäheren Nachtfarben zusammenhängt. Frau Krüger berichtet dagegen von kurzen Druckabfällen auch bei Standardfarbe. Im halbstündigen Probelauf mit Standardfarbe ließ sich kein Abschalten auslösen. Ein belasteter Dauerlauf mit Nachtfarbe fand nicht statt, weil der Folgeauftrag bereits aufgerüstet werden musste.",
        "Wir empfehlen eine separate Messung unter dem Nachtauftrag. Herr Möller will dafür ein Zeitfenster benennen. Mit diesem Protokoll ist weder ein Pumpentausch bestellt noch ein Umbau der Rücklaufüberwachung freigegeben.",
        ], "Tobias Grebe · Serviceleiter\nKenntnis genommen: René Möller · Betriebsleiter")

    pdf(8, SERVICE, "Fuldabogen Spezialdruck GmbH · Frau Maren Brückner", "14. September 2026",
        "SR-260912 · Einsatz K2 am 12.09.2026", "Servicebericht zur nächtlichen Störung",
        "Sehr geehrte Frau Brückner,", [
        "der Einsatz betraf die Versorgung P-17 der K2. Der Antrieb verriegelte mit Druckalarm. René Möller hatte vor Ort bereits angehalten; wir haben keine Weiterfahrt mit überbrückter Überwachung angewiesen. Die nachfolgenden Zeiten stammen aus unserem Telefonjournal und dem Technikerbericht.",
        ("table", [["Zeit am 12.09.", "Ereignis"],
            ["00:40", "Stillstand laut Schichtleitung; kein Werkspur-Techniker am Telefon."],
            ["00:48", "Meldung im Telefonservice aufgenommen; Weitergabe an Bereitschaftskontakt."],
            ["01:25 bis 01:55", "Telefonische Diagnose durch Tobias Grebe. Remote-Verbindung kam nicht zustande."],
            ["03:25", "Ankunft an K2 und Beginn der Arbeiten durch Tobias Grebe."],
            ["04:10", "Vorläufiger Wiederanlauf mit 60 Prozent Geschwindigkeit nach Tausch P-17."],
            ["06:55", "Volle Geschwindigkeit nach Schlauchwechsel, Entlüftung und Probelauf erreicht."],
        ], [104, 391]),
        "Der Techniker fand eine klemmende Pumpeneinheit P-17 und Abrieb im Rücklaufschlauch. Die ausgebauten Teile verbleiben im Teilelager der Druckerei, Fach R3. Ob der Abrieb Ursache oder Folge des Druckabfalls war, ist nicht geklärt. Die Reinigung vor Schichtbeginn ließ sich anhand des vorliegenden Schichtbuchs nicht verifizieren.",
        "Berechnet werden 0,5 Stunden telefonische Diagnose und 3,5 Stunden vor Ort, insgesamt 4 Stunden. Eingebaut wurden P-17 für 680,00 EUR, ein Schlauchkit für 180,00 EUR und Kleinteile für 42,00 EUR, jeweils netto. Herr Möller genehmigte telefonisch um 01:51 Uhr einen Gesamtbetrag bis 1.800,00 EUR netto einschließlich Einsatz- und Anfahrtspauschale.",
        "Der uneingeschränkte Betrieb um 06:55 Uhr ist nicht mit dem ersten Wiederanlauf gleichzusetzen. Die K2 produzierte dazwischen eingeschränkt. Die Ausgabe von 1.120 Bogen Ausschuss wurde von Frau Krüger gemeldet, jedoch nicht durch Werkspur gezählt. Auftragsbedingte Folgekosten sind nicht Gegenstand dieses Berichts.",
        ], "Tobias Grebe\nServiceleiter")

    pdf(9, SERVICE, "Fuldabogen Spezialdruck GmbH\nRechnungswesen · Am Farbhof 18 · 34123 Kassel",
        "1. Juli 2026", "Rechnung WS-260701 · Kundenkonto FB-118", "Wartungspauschale drittes Quartal",
        "Sehr geehrte Damen und Herren,", [
        "wir berechnen den dritten Teilbetrag der Jahrespauschale nach WS-2023-44. Der Leistungszeitraum ist der 1. Juli bis 30. September 2026. Die Augustwartungen werden gesondert mit der Betriebsleitung terminiert; ihr Arbeits- und Anfahrtsanteil ist mit dieser Pauschale abgegolten.",
        ("table", [["Leistung", "Netto EUR"], ["Quartalspauschale K1 und K2", "4.800,00"],
                   ["Umsatzsteuer 19 %", "912,00"], ["Rechnungsbetrag", "5.712,00"]], [350, 145]),
        "Bitte zahlen Sie 5.712,00 EUR bis zum 15. Juli 2026 unter Angabe der Rechnungsnummer auf das Ihnen bekannte Geschäftskonto, Konto-Endung 0041. Es wird kein Skonto eingeräumt. Für Rückfragen zur Zuordnung steht Ihnen Nora Weiß im Rechnungswesen zur Verfügung.",
        "Die Jahrespauschale von 19.200,00 EUR netto bleibt bis zum 31. Dezember 2026 unverändert. Diese Rechnung enthält keine Vergütung für einen Anschlussvertrag ab 2027 und keine Bestellung zusätzlicher Umbauten.",
        "Steuernummer 026/219/84017. Diese Rechnung gehört zum bestehenden Kundenkonto; die Zahlungsdaten wurden nicht geändert.",
        ], "Nora Weiß\nRechnungswesen")

    pdf(10, SERVICE, "Fuldabogen Spezialdruck GmbH\nRechnungswesen · Am Farbhof 18 · 34123 Kassel",
        "14. September 2026", "Rechnung WS-260914 · Kundenkonto FB-118", "Entstörung der Linie K2",
        "Sehr geehrte Damen und Herren,", [
        f"für den Einsatz am 12. September 2026 berechnen wir gemäß WS-2023-44 die nachstehend ausgeführten Arbeiten. Der Leistungsnachweis ist {FILES[8]}; die dort vermerkten Zeiten enthalten keine doppelt gezählte Fahrzeit.",
        ("table", [["Position", "Menge", "Einzel EUR", "Netto EUR"],
            ["Diagnose und Arbeit vor Ort", "4 h", "112,00", "448,00"],
            ["Nacht-/Wochenendeinsatz", "1", "240,00", "240,00"],
            ["Anfahrt einschließlich Fahrzeit", "1", "145,00", "145,00"],
            ["Versorgungseinheit P-17", "1", "680,00", "680,00"],
            ["Schlauchkit SK-17", "1", "180,00", "180,00"],
            ["Kleinteilesatz KL-4", "1", "42,00", "42,00"],
            ["Summe netto", "", "", "1.735,00"],
            ["Umsatzsteuer 19 %", "", "", "329,65"],
            ["Rechnungsbetrag", "", "", "2.064,65"],
        ], [255, 55, 90, 95]),
        "Bitte zahlen Sie den Rechnungsbetrag bis zum 28. September 2026 ohne Abzug auf unser bekanntes Geschäftskonto, Konto-Endung 0041. Der von Herrn Möller genehmigte Rahmen von 1.800,00 EUR netto wird eingehalten. Die Teile dieser Störungsreparatur sind nicht dem Kontingent für planmäßige Wartung zugeordnet.",
        "Die Rechnung trifft keine Aussage über den Umfang einer künftigen Rufbereitschaft. Rückfragen zur Einsatzzeit beantwortet Tobias Grebe; Zahlungszuordnungen bearbeitet Nora Weiß. Steuernummer 026/219/84017.",
        ], "Nora Weiß\nRechnungswesen")

    pdf(12, SERVICE, "Fuldabogen Spezialdruck GmbH · Frau Maren Brückner", "28. August 2026",
        "Angebot WS-260828 · gültig bis 30.09.2026", "Wartung und Entstörung ab 2027",
        "Sehr geehrte Frau Brückner,", [
        "wir bieten die Betreuung Ihrer vorhandenen Drucklinien für den Zeitraum vom 1. Januar 2027 bis 31. Dezember 2029 an. Dieses Angebot kalkuliert K1 und K2 mit drei planmäßigen Wartungen je Linie und Jahr. Ein Maschinenkauf ist nicht enthalten. Die konkrete Vertragsfassung wollen wir nach Rückmeldung zu Betriebszeiten und Fernzugriff abstimmen.",
        ("table", [["Paket oder Option", "Leistungsansatz", "Netto pro Monat"],
            ["Grundwartung", "Sechs Termine; Entstörung stets nach Aufwand", "1.650,00 EUR"],
            ["Betrieb bis 9.600 h/Jahr", "Sechs Termine, 40 h Entstörung, Teilebudget 3.500 EUR", "2.150,00 EUR"],
            ["Betrieb bis 12.000 h/Jahr", "Gleicher Umfang, höhere Nutzungsstufe", "2.390,00 EUR"],
            ["Rufbereitschaft", "Montag 00:00 bis Samstag 24:00, zusätzlich", "450,00 EUR"],
            ["Remote-Plattform", "Zugangsbetrieb, Protokollierung, zusätzlich", "120,00 EUR"],
        ], [136, 257, 102]),
        "Betriebsstunden sind die Summe der Zählerdifferenzen beider Linien im Kalenderjahr. Die Anfangsstufe richtet sich nach Ihrer Jahresplanung. Bei Überschreitung von 9.600 Stunden wird die höhere Stufe rückwirkend für das gesamte Kalenderjahr berechnet. Über 12.000 Stunden stimmen wir eine neue Vergütung ab; bis dahin bleibt die laufende Betreuung zum Preis der höheren Stufe bestehen.",
        "Beim Paket Betrieb gilt das Teilebudget nur für gedeckte Teile bis 750,00 EUR netto je Stück. Druckfarben, Waschmittel, UV-Leuchtmittel, Antriebsmotoren und Steuerungsrechner sind ausgenommen. Das Budget ist kein pauschaler Rabatt auf diese ausgenommenen Positionen. Entstörungszeit oberhalb von 40 Stunden kostet 125,00 EUR netto je Stunde, Anfahrt ist im Paket enthalten.",
        ("page",),
        ("h", "1 Erreichbarkeit und Terminierung"),
        "Ohne Rufbereitschaft arbeiten wir montags bis freitags von 07:00 bis 18:00 Uhr. In gedeckten Zeiten ruft bei vollständigem Stillstand ein Techniker innerhalb von 60 Minuten zurück. Wenn Remote-Diagnose nicht genügt, soll er innerhalb von sechs Stunden vor Ort sein. Eine feste Wiederherstellung innerhalb von acht Stunden können wir wegen der Ersatzteilversorgung nicht anbieten. Sonntage und hessische Feiertage sind nicht in der Rufbereitschaft eingeschlossen.",
        ("h", "2 Zugang und Anlagenumfang"),
        f"Die Remote-Plattform setzt die Anschlussvoraussetzungen in {FILES[14]} voraus. Ein dauerhaft erreichbares Gateway ist in der Kalkulation vorgesehen. Arbeitsrechner der Druckvorstufe sind nicht Gegenstand des Zugangs. Trockner U1 und T2 sind erfasst; das Fremdmodul Z1 ist ausgenommen. Umbauten und ein Austausch des Gateways werden gesondert angeboten.",
        ("h", "3 Laufzeit und Preisfortschreibung"),
        "Wir kalkulieren mit 36 Monaten fester Laufzeit ohne ordentliches Kündigungsrecht. Die Monatsentgelte können erstmals zum 1. Januar 2028 angepasst werden. Maßgeblich sind 60 Prozent der nachgewiesenen Veränderung unserer Techniker-Lohnkosten und 40 Prozent der nachgewiesenen Veränderung unserer Beschaffungskosten für gedeckte Teile. Änderungen nach oben und unten sind zu berücksichtigen; die jährliche Änderung ist auf jeweils fünf Prozent begrenzt. Die Mitteilung soll bis zum 30. September des Vorjahres erfolgen.",
        "Die Grundwartung ist eine Alternative zum Paket Betrieb, nicht dessen zusätzlicher Preisbestandteil. Alle Entgelte verstehen sich zuzüglich gesetzlicher Umsatzsteuer. Eine Umbauleistung ist in keinem Paket enthalten. Wir bitten um Benennung der geplanten Jahresstunden, damit die Vertragsfassung die richtige Anfangsstufe nennt.",
        ], "Dirk Seidel\nGeschäftsführer")

    pdf(14, SERVICE, "Fuldabogen Spezialdruck GmbH · IT und Betriebsleitung", "28. August 2026",
        "RZ-06 · Anschlussblatt zu WS-260828", "Technischer Remotezugang",
        "Sehr geehrte Frau Brückner, sehr geehrter Herr Möller,", [
        "unser Servicezugang trennt die Maschinendiagnose vom Büronetz. Das vorhandene Gateway G1 eröffnet ausgehend eine verschlüsselte Verbindung zum Werkspur-Serviceportal. Von außen geöffnete Eingangsports werden nicht benötigt. Wir benötigen in einem eigenen Wartungssegment ausschließlich die Steuerungen von K1 und K2; Z1 ist technisch nicht separat ansprechbar.",
        ("h", "1 Zugänge und Daten"),
        "Zugreifen dürfen Tobias Grebe und Miriam Hesse mit persönlichen Konten und zweitem Faktor. Die Disposition kann Verbindungen vermitteln, besitzt aber kein Schreibrecht auf Steuerungen. Werkspur will den Tunnel ständig erreichbar halten. Schreibzugriffe auf Parameter werden erst nach telefonischer Freigabe des Schichtleiters ausgeführt. Ein lokaler Hauptschalter kann die Verbindung jederzeit trennen.",
        "Übertragen werden Maschinenkennung, Fehlercode, Betriebsstunden und Diagnosekurven. Benutzerkennungen der Bediener können in der Steuerungshistorie enthalten sein. Druckauftragsnamen und Kundendateien sollen nicht übertragen werden. Der bisherige Diagnoseexport enthält jedoch ein frei beschreibbares Auftragsfeld; dessen Ausblendung muss mit der Druckerei eingerichtet und erprobt werden.",
        ("h", "2 Protokolle und Betrieb"),
        "Das Serviceportal wird auf einem Werkspur-Server in Deutschland betrieben. Externe Supportfirmen erhalten keinen eigenen Zugang. Werkspur speichert Verbindungs- und Änderungsprotokolle 180 Tage und stellt sie auf Anfrage als CSV bereit. Die Druckerei soll die lokale Freigabe mindestens ein Jahr dokumentieren. Notfallkennwörter sind nicht in E-Mails zu übermitteln.",
        "Der Zugang ist vor dem ersten Remote-Einsatz gemeinsam zu prüfen. G1 unterstützt die vorgesehene Protokollversion, bietet aber keine zentrale Benutzerpflege. Ein neues Gateway kann als Zusatzumbau eingebaut werden. Das ist eine eigene Entscheidung und keine bereits ausgelöste Bestellung. Dieses technische Anschlussblatt ersetzt keine noch abzustimmende Vereinbarung über Datenverarbeitung und Vertraulichkeit.",
        ], "Tobias Grebe\nServiceleiter")

    pdf(23, SERVICE, "Fuldabogen Spezialdruck GmbH · Herrn René Möller", "17. September 2026",
        "U-260917 · Bezug SR-260912", "Rücklaufüberwachung und Gatewaytausch",
        "Sehr geehrter Herr Möller,", [
        "nach Ihrem Anruf bieten wir eine zusätzliche Druckmessstelle am Rücklauf der K2 und den Ersatz des Gateways G1 durch G2 an. Die Druckmessstelle protokolliert den Verlauf vor einem Abschalten. Sie verhindert nicht jeden Pumpenausfall. Die im September eingesetzte P-17 bleibt weiter in Betrieb und wird nicht noch einmal berechnet.",
        ("table", [["Leistung", "Ansatz", "Netto EUR"],
            ["Messstelle, Sensor, Gateway G2 und Kabel", "Pauschal", "2.250,00"],
            ["Montage und Steuerungsanpassung", "18 h × 125,00 EUR", "2.250,00"],
            ["Dokumentation und Einweisung", "Pauschal", "300,00"],
            ["Angebotssumme", "", "4.800,00"],
            ["Umsatzsteuer 19 %", "", "912,00"],
            ["Gesamt", "", "5.712,00"],
        ], [275, 110, 110]),
        "Im Pauschalbetrag sind Material und insgesamt 18 Arbeitsstunden einschließlich zweistündigem Probelauf enthalten. Der Probelauf erfolgt mit Standardfarbe und soll Druckverlauf, Alarm und sichere Abschaltung prüfen. Für einen zusätzlichen sechsstündigen Produktionslauf mit Sonderfarbe ist im Angebot keine Technikerzeit vorgesehen. Änderungen an der Hallenverkabelung außerhalb von Halle 2 sind ausgenommen.",
        "Wir reservieren vorläufig den 4. und 5. Januar 2027. Voraussetzung ist eine Bestellung bis zum 15. Oktober 2026 und ein achtstündiges Montagefenster ohne Produktion an K2. Die Druckerei stellt Sonderfarbe und Probematerial. Zahlung: 50 Prozent bei Bestellung, 50 Prozent nach Abnahme. Eine bloße Terminreservierung ist kein Auftrag.",
        "Die Abnahme soll im gemeinsamen Protokoll nach dem zweistündigen Probelauf erklärt werden. Geringfügige Restpunkte werden mit Erledigungstermin vermerkt. Für von uns zu vertretende Mängel leisten wir zwölf Monate ab Abnahme Nachbesserung. Weitere Haftungs- und Beendigungsregeln sind mit dem noch zu schließenden Wartungsvertrag abzustimmen; das Angebot zieht dessen Abschluss nicht vor.",
        ], "Dirk Seidel\nGeschäftsführer")

    pdf(25, PRINTER, "Intern · Maren Brückner und René Möller", "22. September 2026",
        "Einkauf B-2027/09 · Stand 09:15 Uhr", "Kostenansatz für den Wartungseinkauf",
        "Sehr geehrte Frau Brückner, sehr geehrter Herr Möller,", [
        "für unsere Besprechung habe ich die Entgeltansätze in der Arbeitsmappe nebeneinandergestellt. In den Zahlen steckt noch keine Freigabe an Werkspur. Unser Betrag von 2.450,00 EUR monatlich ist ein eigener Vorschlag und kein vom Lieferanten bestätigter Preis.",
        ("h", "1 Auslastung und Material"),
        "Die Produktionsplanung für 2027 nennt 5.400 Betriebsstunden an K1 und 5.500 Stunden an K2, zusammen 10.900 Stunden. Die Werte stammen aus den von Herrn Möller am 21. September freigegebenen Schichtansätzen für bestehende und vorgesehene Nachtaufträge. Nicht jede Nacht ist schon verkauft. Wir setzen die Stunden dennoch für die Budgetplanung an. Damit liegen wir über der im Angebot genannten Grenze von 9.600 Stunden.",
        "Ich habe als Einkaufsreserve 3.900,00 EUR netto für gedeckte Ersatzteile angesetzt. Das ist eine Schätzung für 2027, keine Hochrechnung der Materialliste 2026. In dieser Reserve sind nur Teile bis 750,00 EUR je Stück berücksichtigt; Motoren, Rechner und UV-Leuchtmittel sind nicht enthalten. Wenn solche Teile anfallen, reicht diese Rechnung nicht aus. 36 Stunden ungeplante Technikerarbeit erscheinen Herrn Möller als Arbeitsannahme vertretbar, sind aber keine zugesicherte Obergrenze.",
        ("h", "2 Vergleichsbasis"),
        "Für Werkspur werden Paket Betrieb, Rufbereitschaft und Remote-Plattform gemeinsam gerechnet. Das Grundwartungspaket wird nicht addiert. Der Zusatzumbau geht mit 4.800,00 EUR ein. Für unsere Gegenfassung rechnen wir mit 4.200,00 EUR für denselben Umbau. Beide Beträge sind einmalig, nicht jährlich. Der alte Jahrespreis von 19.200,00 EUR netto ist nur ein Bestandswert bis Ende 2026 und keine angebotene Verlängerungsalternative.",
        "Die Mappe zeigt außerdem die vertraglichen Obergrenzen einer ersten Anpassung 2028 als Rechenobergrenzen, nicht als Prognose: fünf Prozent im Lieferantentext und drei Prozent in unserer Gegenfassung. Tatsächliche Kosten- oder Indexnachweise für 2028 liegen nicht vor. Umsatzsteuer wird mit 19 Prozent angesetzt; eine bereits feststehende Steueränderung ist uns nicht bekannt.",
        f"Anlage: {FILES[22]}. Die Teilzahlungen zur Entstörung werden unabhängig von dieser Planung im Zahlungsjournal geführt; sie sind kein Abschlag auf das Angebot 2027.",
        ], "Leonie Hartung\nEinkauf und Controlling")


SUPPLIER_PAGES = [
    [
        ("1 Vertragsparteien und Zweck", "Die Fuldabogen Spezialdruck GmbH, Am Farbhof 18, 34123 Kassel, vertreten durch Maren Brückner, nachfolgend Auftraggeberin, und die Werkspur Maschinenservice GmbH, Werkhof 7, 34253 Lohfelden, vertreten durch Dirk Seidel, nachfolgend Auftragnehmerin, vereinbaren Wartung und Entstörung an den vorhandenen Maschinen am Standort Kassel. Maschinen werden weder verkauft noch vermietet. Diese Fassung vom 18. September 2026 ist der Vertragsvorschlag der Auftragnehmerin und noch nicht unterzeichnet."),
        ("2 Gedeckte Anlagen", "Erfasst sind K1 mit Seriennummer K1-18442 einschließlich UV-Trockner U1 und K2 mit Seriennummer K2-20117 einschließlich IR-Trockner T2 und Versorgung P-17. Grundlage ist das Anlagenregister AR-09 vom 8. September 2026. Das Fremdzuführmodul Z1, Hallenkompressor, Absaugzentrale und Produktionsleitsystem sind ausgenommen. Bei einem Fehler an der Schnittstelle Z1/K1 prüft die Auftragnehmerin den gedeckten Teil; Arbeiten am Fremdmodul bedürfen eines Zusatzauftrags. G1 wird nur für den Servicezugang unterstützt; ein Austausch ist nicht in der Wartungspauschale enthalten."),
        ("3 Regelmäßige Wartung", "Die Auftragnehmerin führt pro Kalenderjahr drei Wartungen je Linie im Januar, Mai und September durch. Jede Wartung umfasst Funktions- und Sicherheitskontrolle, Schmierung, Sensorreinigung, Prüfung der Trockner und einen halbstündigen Probelauf. Die Auftraggeberin stellt pro Linie vier Stunden Stillstandszeit und einen eingewiesenen Bediener bereit. Termine werden vier Wochen vorher abgestimmt. Muss ein Termin aus betrieblichen Gründen verlegt werden, ist er innerhalb von sechs Wochen nachzuholen. Die Auftragnehmerin übermittelt binnen drei Arbeitstagen ein Protokoll mit Befunden und Materialentnahmen."),
        ("4 Entstörung und Kontingente", "Im Paket Betrieb sind neben der Wartung insgesamt 40 Technikerstunden zur ungeplanten Entstörung pro Kalenderjahr enthalten, gleichgültig ob vor Ort oder per Fernzugriff. Fahrzeit und Anfahrt sind abgegolten und werden nicht auf das Stundenkontingent angerechnet. Die Auftragnehmerin führt ein nachvollziehbares Stundenkonto. Nicht verbrauchte Stunden werden nicht übertragen. Darüber hinausgehende Arbeit wird mit 125,00 EUR netto je Stunde in Viertelstunden berechnet; sie ist vorher freizugeben, außer bei unmittelbar erforderlichen Sicherungsmaßnahmen bis 500,00 EUR netto."),
    ],
    [
        ("5 Servicezeiten und Rufbereitschaft", "Die reguläre Servicezeit ist montags bis freitags von 07:00 bis 18:00 Uhr. Ergänzend wird die kostenpflichtige Rufbereitschaft für Montag 00:00 Uhr bis Samstag 24:00 Uhr vereinbart. Hessische Feiertage sowie Sonntage sind ausgenommen. Die Auftraggeberin meldet Störungen telefonisch unter der bekannten Störungsnummer und nennt Anlagenkennung, Fehlerbild, Rückrufkontakt und einen sicheren Zugang. Ein unvollständiges Fehlerbild hindert die Annahme der Meldung nicht. Die Meldestelle vergibt eine Vorgangsnummer."),
        ("6 Reaktion und Wiederherstellung", "Bei vollständigem Stillstand einer gedeckten Linie beginnt innerhalb von 60 Minuten nach Eingang der Meldung ein qualifizierter Techniker mit Rückruf und Diagnose. Eine automatische Empfangsbestätigung genügt dafür nicht. Bei eingeschränkter Produktion beträgt die Frist vier Stunden. Die Fristen laufen nur innerhalb gedeckter Service- und Bereitschaftszeiten. Soweit ein Vor-Ort-Einsatz erforderlich ist, ist eine Ankunft innerhalb von sechs solchen Stunden angestrebt, aber nicht garantiert. Die Wiederherstellung hängt von Befund und Teileverfügbarkeit ab; eine feste Wiederherstellungsfrist wird nicht vereinbart. Die Auftragnehmerin berichtet während eines vollständigen Stillstands spätestens alle zwei Stunden über Fortschritt, benötigte Teile und den nächsten Schritt. Die Produktion mit verringerter Geschwindigkeit ist als Zwischenzustand zu dokumentieren."),
        ("7 Ersatzteile und Verbrauch", "Im Jahresentgelt sind gedeckte Ersatzteile bis insgesamt 3.500,00 EUR netto enthalten, sofern der einzelne Stückpreis 750,00 EUR netto nicht überschreitet. Maßgeblich ist der vor Einbau mitgeteilte Listenpreis ohne weiteren Zuschlag. Teurere Einzelteile sind vollständig gesondert zu bezahlen und werden nicht auf das Budget angerechnet. Antriebsmotoren, Steuerungsrechner, UV-Leuchtmittel, Farben und Waschmittel sind unabhängig vom Preis ausgenommen. Nach Ausschöpfung des Budgets werden gedeckte Teile gesondert bezahlt. Nicht verbrauchtes Budget verfällt am Jahresende. Die Auftragnehmerin weist jede Entnahme aus; Teile aus Zusatzumbauten belasten das Budget nicht. Für einen Beschaffungspreis über 500,00 EUR netto ist vorher eine Freigabe einzuholen."),
        ("8 Mitwirkung der Druckerei", "Die Auftraggeberin führt die täglichen Reinigungen und Bedienerkontrollen durch, sichert die Fehlerspeicher und schafft einen sicheren Arbeitsplatz. Sie muss Schutzvorrichtungen nicht überbrücken und keine Fachreparatur selbst vornehmen. Fehlende Mitwirkung verlängert eine betroffene Frist nur um die nachweislich hierdurch verursachte Verzögerung; die Auftragnehmerin benennt diese unverzüglich. Die Ursache einer Störung wird nicht allein wegen eines fehlenden Reinigungseintrags der Auftraggeberin zugerechnet."),
    ],
    [
        ("9 Fernzugriff und Vertraulichkeit", "Die Auftraggeberin ermöglicht einen dauernd erreichbaren verschlüsselten Tunnel im Wartungsnetz nach Anschlussblatt RZ-06 vom 28. August 2026. Nur persönliche Konten von Tobias Grebe und Miriam Hesse mit zweitem Faktor erhalten Diagnosezugriff. Parameteränderungen bedürfen einer dokumentierten Freigabe des Schichtleiters. Der lokale Trennschalter bleibt verfügbar. Druckdateien und Kundenaufträge dürfen nicht eingesehen werden. Das freie Auftragsfeld ist vor Beginn auszublenden. Die Auftragnehmerin speichert Zugriffsprotokolle 180 Tage auf ihrem Server in Deutschland und gibt sie auf Anfrage heraus. Geheimhaltungsbedürftige Informationen dürfen nur für die Leistung verwendet werden. Vor Verarbeitung personenbezogener Daten klären die Parteien ihre jeweiligen Rollen und schließen, soweit erforderlich, eine gesonderte Vereinbarung; bis dahin werden solche Daten nicht übertragen. Ein Unterauftragnehmer erhält keinen Fernzugriff ohne vorherige Zustimmung der Auftraggeberin."),
        ("10 Vergütung und Nutzungsstufen", "Bei zusammen bis zu 9.600 Betriebsstunden beider Linien pro Kalenderjahr beträgt das Monatsentgelt für das Paket Betrieb 2.150,00 EUR netto. Über 9.600 bis zu 12.000 Stunden beträgt es 2.390,00 EUR netto. Hinzu kommen monatlich 450,00 EUR netto für Rufbereitschaft und 120,00 EUR netto für die Remote-Plattform. Die Auftraggeberin meldet ihre Planung vor Jahresbeginn und die Zählerstände jeweils zum Quartalsende. Die anfängliche Abrechnung richtet sich nach der gemeldeten Planung. Wird die Grenze von 9.600 Stunden überschritten, gilt die höhere Stufe rückwirkend ab 1. Januar des laufenden Jahres; gezahlte Beträge werden angerechnet. Oberhalb von 12.000 Stunden vereinbaren die Parteien einen neuen Preis; bis zu einer Einigung werden die bestehenden Leistungen zum Preis der höheren Stufe fortgeführt. Das alternative Grundwartungspaket ist nicht vereinbart."),
        ("11 Rechnung und Anpassung", "Die Monatsentgelte sind monatlich im Voraus in Rechnung zu stellen und binnen 14 Kalendertagen ab Rechnungszugang zu zahlen. Hinzu kommt die gesetzliche Umsatzsteuer. Erstmals zum 1. Januar 2028 darf das wiederkehrende Entgelt anhand der nachgewiesenen Veränderung der durchschnittlichen Techniker-Lohnkosten der Auftragnehmerin zu 60 Prozent und ihrer Beschaffungskosten gedeckter Ersatzteile zu 40 Prozent angepasst werden. Verglichen werden die Kostenstände vom 30. Juni des Vorjahres und vom 30. Juni des laufenden Jahres. Die Berechnung ist bis zum 30. September für das Folgejahr nachvollziehbar mitzuteilen. Senkungen sind ebenso weiterzugeben; der Veränderungssatz ist in beide Richtungen auf fünf Prozent pro Jahr begrenzt. Ohne fristgerechten Nachweis bleibt das Entgelt unverändert. Ein besonderes Kündigungsrecht allein wegen dieser Anpassung wird nicht eingeräumt."),
    ],
    [
        ("12 Zusatzumbau und Abnahme", "Der Umbau nach Angebot U-260917 vom 17. September 2026 kann gesondert für 4.800,00 EUR netto beauftragt werden. Er gehört nicht zur monatlichen Wartung. Die Auftraggeberin zahlt bei Bestellung 50 Prozent, den Rest nach Abnahme. Die angebotene Rücklaufmessung und G2 werden nach gemeinsamem zweistündigem Probelauf mit Standardfarbe anhand von Druckanzeige, Alarm, Abschaltung und Zugriffsprotokoll geprüft. Die Parteien halten Restpunkte fest; unwesentliche Mängel hindern die Abnahme nicht. Die Produktionsnutzung allein gilt nicht als Abnahme. Bei Mängeln der Umbauleistung bessert die Auftragnehmerin innerhalb angemessener Frist nach. Die Frist für Mängelansprüche beträgt zwölf Monate ab Abnahme; zwingende längere Fristen bleiben unberührt. Eine Bestellung des Umbaus ist mit Unterzeichnung dieses Wartungsvertrags noch nicht erklärt."),
        ("13 Haftung", "Bei Vorsatz, grober Fahrlässigkeit und Verletzung von Leben, Körper oder Gesundheit haftet die Auftragnehmerin unbeschränkt. Bei leicht fahrlässiger Verletzung wesentlicher Vertragspflichten ist die Haftung auf den vorhersehbaren vertragstypischen Schaden und insgesamt auf ein im Schadensjahr geschuldetes Netto-Jahresentgelt der laufenden Betreuung begrenzt. Für leichte Fahrlässigkeit im Übrigen wird nicht gehaftet. In der begrenzten Haftung sind Produktionsausfall und entgangener Gewinn ausgeschlossen. Zwingende Haftung und ausdrücklich übernommene Garantien bleiben unberührt. Die Auftraggeberin dokumentiert behauptete Schäden und ergreift zumutbare Maßnahmen zur Schadensminderung; ein Ersatzanspruch wird durch eine technische Einsatzfreigabe nicht anerkannt."),
        ("14 Laufzeit und Kündigung", "Der Vertrag beginnt am 1. Januar 2027 und endet am 31. Dezember 2029 ohne automatische Verlängerung. Eine ordentliche Kündigung innerhalb dieser Zeit ist ausgeschlossen. Das Recht zur Kündigung aus wichtigem Grund bleibt beiden Parteien erhalten. Bei behebbaren Pflichtverletzungen ist zuvor eine angemessene Abhilfefrist zu setzen. Bei Vertragsende übergibt die Auftragnehmerin sämtliche noch nicht übermittelten Protokolle und sperrt ihre Konten; die Auftraggeberin trennt den Tunnel. Offene Einzelaufträge werden gesondert abgestimmt. Die Vereinbarung WS-2023-44 läuft unabhängig hiervon am 31. Dezember 2026 aus."),
        ("15 Unterlagen und Schlussbestimmungen", f"Vertragsbestandteile sind diese Fassung, {FILES[3]} und {FILES[14]}. Die abweichenden Regelungen dieses Vertrags gehen den Anlagen vor. {FILES[23]} gilt nur für eine gesonderte Bestellung. Andere Allgemeine Geschäftsbedingungen werden nicht einbezogen. Vertragsänderungen und Kündigungen sind in Textform zu erklären. Individuelle Abreden bleiben unberührt. Deutsches Recht gilt; Gerichtsstand zwischen den Unternehmen ist Kassel. Sollte eine Bestimmung unwirksam sein, berührt dies die übrigen Bestimmungen nicht. Eine Ersatzregelung bedarf einer Vereinbarung und wird nicht automatisch fingiert."),
    ],
]

BUYER_PAGES = [
    [
        ("1 Vertragsparteien und Zweck", "Die Fuldabogen Spezialdruck GmbH, Am Farbhof 18, 34123 Kassel, vertreten durch Maren Brückner, nachfolgend Auftraggeberin, und die Werkspur Maschinenservice GmbH, Werkhof 7, 34253 Lohfelden, vertreten durch Dirk Seidel, nachfolgend Auftragnehmerin, vereinbaren die Betreuung der vorhandenen Sonderdrucklinien. Ein Kauf oder eine Anmietung der Maschinen findet nicht statt. Diese Fassung vom 21. September 2026 ist der Gegenentwurf der Auftraggeberin auf die Fassung vom 18. September 2026 und noch nicht unterzeichnet."),
        ("2 Gedeckte Anlagen und Schnittstellen", "Der Vertrag erfasst K1 mit Seriennummer K1-18442 samt UV-Trockner U1 und Zuführmodul Z1 sowie K2 mit Seriennummer K2-20117 samt IR-Trockner T2 und Versorgung P-17. Grundlage ist das Anlagenregister AR-09 vom 8. September 2026. Die gemeinsame Not-Halt-Kette zwischen Z1 und K1 wird einschließlich des Zuführmoduls betreut. Muss ein Fremdhersteller hinzugezogen werden, koordiniert ihn die Auftragnehmerin; eine gesonderte Vergütung ist zuvor zu vereinbaren. Die Diagnosefunktion des Gateways G1 ist eingeschlossen. Ein neuer G2 wird erst mit gesondert bestelltem Umbau aufgenommen. Kompressor, Absaugzentrale, Büronetz und Produktionsleitsystem verbleiben bei der Auftraggeberin."),
        ("3 Planmäßige Wartung", "Die Auftragnehmerin führt jährlich drei Wartungen pro Linie im Januar, Mai und September durch. Die Leistung umfasst Reinigung der Sensoren, Schmierung, Prüfung von Führungen, Antrieben, Trocknern, Zuführung und Sicherheitsketten sowie einen mindestens halbstündigen Probelauf. Für jede Linie wird vier Wochen vorher ein Stillstandsfenster von vier Stunden abgestimmt. Die Auftragnehmerin trägt die Verantwortung für die vollständige Dokumentation ihrer Arbeiten und übermittelt das Protokoll binnen drei Arbeitstagen. Kann ein Termin wegen eines Produktionsauftrags nicht stattfinden, stimmen beide Parteien einen Ersatztermin innerhalb von vier Wochen ab."),
        ("4 Entstörung und Arbeitsstunden", "Die Pauschale umfasst 60 Stunden ungeplante Technikerarbeit pro Kalenderjahr. Wartungsstunden und Fahrzeiten werden darauf nicht angerechnet. Fernarbeit und Vor-Ort-Zeit sind getrennt mit Beginn, Ende und Tätigkeit nachzuweisen; gleichzeitige Zeiten dürfen nicht doppelt zählen. Zusätzliche Arbeitsstunden kosten 115,00 EUR netto und bedürfen vor Ausführung einer Freigabe des Betriebsleiters. Unaufschiebbare Sicherungsmaßnahmen bis 500,00 EUR netto darf die Auftragnehmerin ohne vorherige Freigabe durchführen. Ungenutzte Stunden verfallen zum Jahresende; eine pauschale Nachbelastung ohne nachgewiesene Arbeit ist ausgeschlossen."),
    ],
    [
        ("5 Rufbereitschaft und Meldung", "Die Auftragnehmerin hält für beide Linien an allen Kalendertagen einschließlich Sonn- und Feiertagen eine rund um die Uhr erreichbare Rufbereitschaft vor. Meldungen werden telefonisch angenommen; fehlende Diagnosekenntnisse der Schichtleitung hindern den Fristbeginn nicht. Erforderlich sind nur Anlagenkennung, beobachtetes Fehlerbild und Rückrufkontakt. Die Meldestelle dokumentiert den tatsächlichen Eingang. Die regelmäßige Wartung wird unabhängig davon montags bis freitags terminiert."),
        ("6 Reaktionszeit und Wiederherstellung", "Bei vollständigem Stillstand beginnt ein fachkundiger Techniker spätestens 30 Minuten nach Eingang der Meldung mit Diagnose und Rückruf. Eine automatische Nachricht oder die Annahme durch einen Telefonservice genügt nicht. Falls ein Einsatz vor Ort erforderlich ist, trifft der Techniker spätestens vier Zeitstunden nach Meldung ein. Die uneingeschränkte Betriebsfähigkeit ist innerhalb von acht Zeitstunden nach Meldung wiederherzustellen. Ein Lauf mit reduzierter Geschwindigkeit wahrt diese Frist nicht. Bei eingeschränkter Produktion erfolgt die technische Reaktion binnen zwei Zeitstunden und die Wiederherstellung binnen zwölf Zeitstunden. Alle Fristen laufen auch nachts, sonntags und an Feiertagen."),
        "Eine Frist verlängert sich nur um die dokumentierte Dauer einer von der Auftraggeberin verursachten Zugangssperre oder eines von keiner Partei beherrschbaren Ereignisses. Gewöhnliche Beschaffungszeiten für gedeckte Verschleißteile gehören nicht dazu. Ist die Wiederherstellung absehbar nicht erreichbar, meldet die Auftragnehmerin unverzüglich Ursache, Zwischenmaßnahmen und einen belastbaren Zeitplan. Überschreitet sie die Wiederherstellungsfrist aus von ihr zu vertretenden Gründen, wird für jede angefangene zusätzliche Vierstundenperiode eine Gutschrift von zwei Prozent des Monatsentgelts, höchstens zehn Prozent je Monat, erteilt. Weitergehende Ansprüche bleiben unter Anrechnung der Gutschrift unberührt.",
        ("7 Teileversorgung und Verbrauch", "Gedeckte Ersatz- und Verschleißteile sind bis insgesamt 6.000,00 EUR netto je Kalenderjahr enthalten. Eine zusätzliche Stückpreisgrenze gibt es nicht. Farben und Waschmittel sind ausgenommen; Pumpen, Antriebsmotoren und Steuerungsrechner sind eingeschlossen. UV-Leuchtmittel bleiben ausgenommen. Die Auftragnehmerin hält für P-17 ein geeignetes Austauschteil sowie ein Schlauchkit verfügbar. Einbaupreise werden vorab offengelegt. Nach Ausschöpfung des Jahresbudgets bedarf jede weitere Teilebestellung einer Freigabe. Im Zusatzumbau enthaltenes Material wird nicht auf das Budget angerechnet. Nicht verbrauchtes Budget wird nicht ausgezahlt und nicht übertragen."),
    ],
    [
        ("8 Mitwirkung und Beweissicherung", "Die Auftraggeberin führt Bedienerkontrollen und tägliche Reinigung durch, stellt Probematerial sowie sichere Zugänge bereit und sichert die Fehlerspeicher. Sie ist nicht zu Reparaturen oder zur Überbrückung von Schutzschaltungen verpflichtet. Die Auftragnehmerin dokumentiert einen behaupteten Mitwirkungsmangel und dessen konkrete Auswirkung. Fehlende Einträge allein beweisen keine Fehlerursache. Ausgebaute schadhafte Teile werden gekennzeichnet und mindestens drei Monate zur gemeinsamen Untersuchung aufbewahrt."),
        ("9 Einzelzugriff und Vertraulichkeit", "Jeder Fernzugriff bedarf einer gesonderten, zeitlich auf den Einsatz begrenzten Freigabe durch den Schichtleiter. Ein dauernd offener Tunnel wird nicht eingerichtet. Die Auftragnehmerin verwendet persönliche Konten mit zweitem Faktor und trennt den Zugang nach Abschluss. Druckdateien, Kundendaten und Auftragsnamen dürfen nicht übertragen werden; das freie Auftragsfeld ist vor Inbetriebnahme auszublenden. Verbindungs- und Änderungsprotokolle sind der Auftraggeberin binnen eines Arbeitstags zu übergeben und bei Werkspur nach 30 Tagen zu löschen, soweit keine konkrete Störung weiter untersucht werden muss. Die Parteien klären vor einer Verarbeitung personenbezogener Daten ihre Rollen und schließen erforderliche zusätzliche Vereinbarungen. Ohne diese Klärung bleibt der Fernzugriff auf nicht personenbezogene Maschinendaten beschränkt. Das Anschlussblatt RZ-06 gilt nur, soweit es diesem Abschnitt nicht widerspricht. Externer Zugriff und Unterauftragnehmer bedürfen einer ausdrücklichen Zustimmung."),
        ("10 Monatspreis und Mehrnutzung", "Für insgesamt bis zu 12.000 Betriebsstunden beider Linien je Kalenderjahr beträgt das einheitliche Monatsentgelt 2.450,00 EUR netto. Es umfasst Wartung, das Arbeits- und Teilekontingent, Anfahrt, die Rufbereitschaft an allen Tagen und die Remote-Plattform. Separate Monatsaufschläge werden nicht erhoben. Die Auftraggeberin meldet quartalsweise die Zählerdifferenzen. Über 12.000 Stunden ist die zusätzliche Belastung zu besprechen; ein neuer Preis gilt nur aufgrund einer Vereinbarung für die Zukunft. Eine rückwirkende Nachbelastung oder ein Wegfall laufender Pflichten ohne Vereinbarung ist ausgeschlossen. Die Rechnung wird am Monatsende gestellt und ist 30 Kalendertage nach Zugang zahlbar. Die gesetzliche Umsatzsteuer kommt hinzu."),
        ("11 Jährliche Anpassung", "Erstmals zum 1. Januar 2028 ändert sich das wiederkehrende Monatsentgelt im Verhältnis der Veränderung des vom Statistischen Bundesamt veröffentlichten Verbraucherpreisindex für Deutschland, Gesamtindex, Juni 2027 gegenüber Juni 2026; danach werden jeweils die beiden letzten Juniwerte verglichen. Erhöhungen und Senkungen werden gleichermaßen berücksichtigt und sind auf drei Prozent pro Jahr begrenzt. Die Auftragnehmerin legt die verwendeten Werte und die Rechnung bis zum 30. September vor. Ohne fristgerechte Mitteilung wird eine Erhöhung nicht wirksam; eine Senkung bleibt zu berücksichtigen. Bei jeder Erhöhung darf die Auftraggeberin innerhalb von vier Wochen nach Mitteilung zum Jahresende kündigen. Einmalige Umbaupreise werden nicht indexiert."),
    ],
    [
        ("12 Zusatzumbau und Abnahme", "Die Auftraggeberin kann die Rücklaufmessung und den Gatewaytausch gemäß Angebot U-260917 gesondert zu einem Festpreis von 4.200,00 EUR netto bestellen. Der Preis umfasst Montage, Dokumentation, Einweisung und einen sechsstündigen begleitenden Produktionslauf mit der im Nachtauftrag verwendeten Sonderfarbe. Die Parteien prüfen stabile Druckanzeige, Fehlerspeicher, Alarm, sichere Abschaltung und den nur einzeln freigegebenen Fernzugriff. Die Abnahme erfolgt ausdrücklich in einem gemeinsamen Protokoll. Produktionsnutzung oder Schweigen allein ersetzen sie nicht. Wesentliche Mängel hindern die Abnahme; unwesentliche Restpunkte erhalten einen Erledigungstermin. Der Preis wird 30 Tage nach Abnahme und Rechnung fällig, eine Anzahlung erfolgt nicht. Mängel der Umbauleistung werden auf Kosten der Auftragnehmerin behoben; Ansprüche verjähren in 24 Monaten ab Abnahme, soweit zwingendes Recht keine längere Frist vorgibt. Der Wartungsvertrag selbst löst keine Umbau-Bestellung aus."),
        ("13 Haftung und Ausfallschäden", "Die Auftragnehmerin haftet unbeschränkt bei Vorsatz, grober Fahrlässigkeit, Verletzung von Leben, Körper oder Gesundheit und nach zwingenden Haftungsvorschriften. Bei leicht fahrlässiger Verletzung wesentlicher Pflichten haftet sie für vorhersehbare vertragstypische Schäden bis 250.000,00 EUR je Schadensfall und 500.000,00 EUR je Kalenderjahr. Nachgewiesener Produktionsausfall und entgangener Gewinn sind innerhalb dieser Grenzen nicht pauschal ausgeschlossen. Im Übrigen ist die Haftung für leichte Fahrlässigkeit ausgeschlossen. Die Auftraggeberin legt konkrete Auftrags- und Schadensdaten vor und mindert Schäden, soweit zumutbar. Pauschale Umsatzausfälle ohne Nachweis werden hierdurch nicht anerkannt."),
        ("14 Laufzeit und Beendigung", "Der Vertrag beginnt am 1. Januar 2027 mit einer festen Erstlaufzeit bis zum 31. Dezember 2027. Er verlängert sich jeweils um ein Jahr, wenn keine Partei spätestens drei Monate vor Ablauf in Textform kündigt. Sonderkündigung nach Ziffer 11 und Kündigung aus wichtigem Grund bleiben unberührt. Bei behebbaren Pflichtverletzungen ist zuvor eine angemessene Abhilfefrist zu setzen. Bei Ende erhält die Auftraggeberin alle noch fehlenden Protokolle und Änderungen an den Steuerungen in einem gebräuchlichen lesbaren Format; die Auftragnehmerin sperrt ihre Zugänge. Begonnene Einzelaufträge werden gesondert abgestimmt. WS-2023-44 endet unabhängig davon am 31. Dezember 2026."),
        ("15 Anlagen und Schlussregelungen", f"Bestandteile sind dieser Vertrag, {FILES[3]} und {FILES[14]}, letzteres nur mit Vorrang der hier vereinbarten Beschränkungen. {FILES[23]} ist Grundlage eines gesonderten Auftrags und wird durch Ziffer 12 nur für einen solchen Auftrag modifiziert. Weitere Allgemeine Geschäftsbedingungen gelten nicht. Änderungen und Kündigungen erfolgen in Textform; individuelle Abreden bleiben unberührt. Deutsches Recht ist vereinbart, Gerichtsstand zwischen den Unternehmen ist Kassel. Unwirksamkeit einer Bestimmung lässt die übrigen Regelungen bestehen; eine Ersatzbestimmung setzt eine gesonderte Vereinbarung voraus."),
    ],
]


def make_contract(number, issuer, pages, date, version):
    doc = Document()
    doc.settings.odd_and_even_pages_header_footer = False
    section = doc.sections[0]
    section.different_first_page_header_footer = False
    section.top_margin = Cm(2.4)
    section.bottom_margin = Cm(1.9)
    section.left_margin = section.right_margin = Cm(2.0)
    section.header_distance = Cm(0.8)
    section.footer_distance = Cm(0.7)
    section.page_width, section.page_height = Cm(21), Cm(29.7)
    for name in ["Normal", "Title", "Heading 1", "Heading 2"]:
        style = doc.styles[name]
        style.font.name = "Times New Roman"
        style.font.size = Pt(11)
        style.font.color.rgb = RGBColor(0, 0, 0)
        fonts = style.element.get_or_add_rPr().find(qn("w:rFonts"))
        for attr in list(fonts.attrib):
            if "theme" in attr.lower():
                del fonts.attrib[attr]
        for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
            fonts.set(qn("w:" + attr), "Times New Roman")
        props = style.element.find(qn("w:pPr"))
        if props is not None:
            for border in list(props.findall(qn("w:pBdr"))):
                props.remove(border)
        style.paragraph_format.space_after = Pt(7)
        style.paragraph_format.line_spacing = 1.04
    doc.styles["Title"].font.size = Pt(16)
    doc.styles["Title"].font.bold = True
    doc.styles["Heading 1"].font.bold = True
    doc.styles["Heading 1"].paragraph_format.space_before = Pt(8)
    header = section.header.paragraphs[0]
    run = header.add_run(issuer["name"])
    run.bold, run.font.size = True, Pt(13)
    header.add_run(f"\n{issuer['address']} · {issuer['contact'].split(' · ')[0]}").font.size = Pt(9)
    footer = section.footer.paragraphs[0]
    footer.add_run(f"{version} · {date} · FB-118\n").font.size = Pt(8)
    footer.add_run("Seite ").font.size = Pt(8)
    field = OxmlElement("w:fldSimple")
    field.set(qn("w:instr"), "PAGE")
    footer._p.append(field)
    doc.add_paragraph("Wartung und Entstörung der Drucklinien", "Title")
    doc.add_paragraph(f"{version} · {date}\nBezug: WS-260828 · Betreuung Halle 2 ab 2027")
    doc.add_paragraph("Sehr geehrte Vertragspartner,")
    for index, page in enumerate(pages):
        if index:
            doc.add_page_break()
        for block in page:
            if isinstance(block, tuple):
                doc.add_paragraph(block[0], "Heading 1")
                doc.add_paragraph(block[1])
            else:
                doc.add_paragraph(block)
    p = doc.add_paragraph("Die Unterzeichnung steht aus. Die nachstehenden Unterschriftsfelder gehören zu dieser vollständigen Vertragsfassung.")
    p.paragraph_format.keep_with_next = True
    for text in ["Kassel / Lohfelden, Datum: ____________________",
                 "__________________________          __________________________",
                 "Maren Brückner                                 Dirk Seidel",
                 "Fuldabogen Spezialdruck GmbH           Werkspur Maschinenservice GmbH"]:
        p = doc.add_paragraph(text)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.keep_with_next = True
    doc.paragraphs[-1].paragraph_format.keep_with_next = False
    separate_section_headings(doc)
    doc.core_properties.author = issuer["name"]
    doc.core_properties.title = "Wartungs- und Entstörungsvertrag Halle 2"
    doc.core_properties.created = datetime(2026, 9, 18 if number == 16 else 21, 9, 0)
    doc.core_properties.modified = doc.core_properties.created
    doc.save(CASE / FILES[number])


def write_csv(number, rows):
    with (CASE / FILES[number]).open("w", encoding="utf-8", newline="") as handle:
        csv.writer(handle, delimiter=";", quoting=csv.QUOTE_ALL, lineterminator="\r\n").writerows(rows)


def make_records():
    rows = [["Schichtbeginn", "Schichtende", "Linie", "Stillstand_min", "Reduziert_min", "Gutbogen", "Vermerk"]]
    for day in [10, 11]:
        for start, end, next_day in [(6, 14, day), (14, 22, day), (22, 6, day + 1)]:
            for line in ["K1", "K2"]:
                outage = day == 11 and start == 22 and line == "K2"
                rows.append([f"2026-09-{day:02} {start:02}:00", f"2026-09-{next_day:02} {end:02}:00", line,
                             210 if outage else 0, 110 if outage else 0,
                             13100 if outage else (34000 if line == "K1" else 26000),
                             'Druckabfall; 1.120 Bogen Ausschuss, "P-17"' if outage else "Planbetrieb, Reinigung vermerkt"])
    rows += [["2026-09-12 06:00", "2026-09-12 14:00", "K1", 0, 0, 33200, "Samstagsauftrag"],
             ["2026-09-12 06:00", "2026-09-12 14:00", "K2", 0, 55, 24700, "Volle Leistung ab 06:55; Schichtübergabe Krüger/Faber"]]
    write_csv(4, rows)
    write_csv(11, [
        ["Buchungstag", "Beleg", "Rechnung", "Soll_Haben", "Betrag_EUR", "Konto", "Verwendungszweck"],
        ["2026-07-14", "ZA-0714-18", "WS-260701", "Ausgang", "3000,00", "Geschäftskonto 7702", "Erste Teilzahlung Q3"],
        ["2026-07-15", "ZA-0715-09", "WS-260701", "Ausgang", "2712,00", "Geschäftskonto 7702", "Rest Wartung Q3"],
        ["2026-09-18", "ZA-0918-31", "WS-260914", "Ausgang", "1000,00", "Geschäftskonto 7702", "Entstörung K2; Teilzahlung"],
        ["2026-09-21", "ZA-0921-07", "WS-260914", "Ausgang", "500,00", "Geschäftskonto 7702", "Weitere Teilzahlung; Rückfrage offen"],
    ])
    write_csv(24, [
        ["Datum", "Linie", "Artikel", "Menge", "Einzel_netto_EUR", "Gesamt_netto_EUR", "Zuordnung", "Beleg"],
        ["2026-08-19", "K1", "Filter F-8", "2", "48,00", "96,00", "Wartungskontingent", "W-260819"],
        ["2026-08-19", "K1", "Andruckrolle R-12", "1", "160,00", "160,00", "Wartungskontingent", "W-260819"],
        ["2026-08-20", "K2", "Dichtungssatz D-17", "1", "125,00", "125,00", "Wartungskontingent", "W-260820"],
        ["2026-09-12", "K2", "Versorgungseinheit P-17", "1", "680,00", "680,00", "Störung, gesondert", "SR-260912"],
        ["2026-09-12", "K2", "Schlauchkit SK-17", "1", "180,00", "180,00", "Störung, gesondert", "SR-260912"],
        ["2026-09-12", "K2", "Kleinteilesatz KL-4", "1", "42,00", "42,00", "Störung, gesondert", "SR-260912"],
    ])
    (CASE / FILES[7]).write_text(
        "Fuldabogen Spezialdruck GmbH\nBetriebsleitung Halle 2\n"
        "Anrufnotiz vom 12.09.2026, niedergeschrieben 08:20 Uhr\n"
        "René Möller an Maren Brückner / Leonie Hartung\nBezug: K2, Störung vom 12.09., Service SR-260912\n\n"
        "Guten Morgen Frau Brückner, guten Morgen Frau Hartung,\n\n"
        "K2 stand ab 00:40. Selin rief mich um 00:42 an. Ich wählte um 00:44 die Werkspur-Nummer; "
        "nach Warteschleife nahm um 00:48 ein Telefonservice die Meldung auf. Dort wurde mir gesagt, man gebe es "
        "sofort weiter. Ich habe das zunächst als Beginn der Hilfe verstanden. Ein Techniker meldete sich aber erst "
        "um 01:25. Es war Herr Grebe, nicht die Person am Empfang.\n\n"
        "Wir wollten das Gateway einschalten. Selin hatte den Schlüsselschalter freigegeben, die Verbindung kam "
        "trotzdem nicht hoch. Unsere IT vermutet die neue Firewallregel vom Donnerstag; ein belastbarer Nachweis "
        "liegt mir noch nicht vor. Herr Grebe konnte nur telefonisch anleiten. Er untersagte ausdrücklich das "
        "Überbrücken der Drucküberwachung. Um 01:51 sagte ich ihm bis zu 1.800 EUR netto für den Einsatz zu. "
        "Ich wollte die Freigabe nicht bis zur Geschäftsführung liegenlassen.\n\n"
        "Um 03:25 war Herr Grebe an der Linie. Ab 04:10 liefen wieder Bogen, aber nur mit ungefähr 60 Prozent. "
        "Selin hat deshalb im Schichtbuch zwischen Stillstand und eingeschränktem Betrieb getrennt. Volle Leistung "
        "hatten wir erst um 06:55. Die Meldung 'läuft wieder' an den Versand um 04:15 war zu optimistisch. "
        "Die 1.120 Ausschussbogen wurden am Schichtende separat gezählt; sie sind nicht in Gutbogen enthalten.\n\n"
        "Für den nächsten Vertrag brauche ich nachts jemanden, der tatsächlich entscheiden kann. Ich kann "
        "die Aussage 'Reaktion in einer Stunde' gegenüber dem Versand nicht als Zusage verwenden, dass die "
        "Maschine nach einer Stunde läuft. Sonntag haben wir im Oktober zwei Einrichtefenster, auch wenn bisher "
        "kein regelmäßiger Sonntagsbetrieb vorgesehen ist.\n\n"
        "Viele Grüße\nRené Möller\nBetriebsleiter\n", encoding="utf-8")
    (CASE / FILES[18]).write_text(
        "Fuldabogen Betriebsnachrichten\nKanal: Halle 2 / Instandhaltung\n"
        "Export durch René Möller am 15.09.2026 um 16:45 Uhr, Zeitzone Europe/Berlin\n\n"
        "15.09.2026 15:42 Selin Krüger: Für das Gespräch morgen: Am Samstag war bei 04:10 nicht alles gut. "
        "Wir mussten die Auflage reduzieren, sonst kam der Druckalarm zurück. Erst nach dem Schlauchwechsel lief es normal.\n"
        "15.09.2026 15:46 René Möller: Ja. Der Bericht unterscheidet das jetzt. Bitte die Zeiten nicht in der "
        "Schichtliste zu einem einzigen Feld zusammenziehen.\n"
        f"15.09.2026 15:47 René Möller: Datei angehängt: {FILES[8]}\n"
        "15.09.2026 15:50 Jan Faber: Am K1-Einlauf ist das Problem anders. Z1 hält an, und dann steht K1 "
        "über dieselbe Not-Halt-Kette. Wenn Werkspur nur die K1 anschaut, warten wir wieder auf zwei Firmen.\n"
        f"15.09.2026 15:53 René Möller: Datei angehängt: {FILES[17]}\n"
        "15.09.2026 15:54 René Möller: Das ist die Skizze vom letzten Rundgang. Der Platz am Servicetor muss frei "
        "bleiben. Am Samstag standen dort zwei Paletten; wir haben sie weggezogen, bevor Grebe ankam.\n"
        "15.09.2026 16:02 Selin Krüger: Zum Gateway: Ich habe den Schlüssel gedreht, das weiß ich sicher. "
        "Ob die Firewall davor offen war, sehe ich am Schrank nicht. Ich will keine dauernde Freigabe unterschreiben, "
        "nur damit die Diagnose schneller startet.\n"
        "15.09.2026 16:14 Jan Faber: Für einen Umbautest bitte unsere dicke Nachtfarbe nehmen. Der Probelauf im "
        "August war mit Standardfarbe; da gab es keinen Alarm. Sechs Stunden wären ein kompletter sauberer Vergleichslauf.\n"
        "15.09.2026 16:29 René Möller: Ich gebe das so an Einkauf weiter. Es gibt noch keinen Umbauauftrag. "
        "P-17 und der alte Schlauch bleiben beschriftet in Fach R3, bis beide Seiten sie gesehen haben.\n",
        encoding="utf-8")


def make_plan():
    im = Image.new("RGB", (1800, 1240), "#fafafa")
    d = ImageDraw.Draw(im)
    regular, small, bold = screen_font(26), screen_font(21), screen_font(30, bold=True)
    d.text((75, 48), "FULDABOGEN SPEZIALDRUCK", font=bold, fill="#253a32")
    d.text((75, 96), "Halle 2   Aufstellskizze Instandhaltung   Stand 08.09.2026", font=regular, fill="black")
    d.text((75, 136), "Am Farbhof 18, Kassel   Gezeichnet: René Möller   AR-09 / Blatt 1", font=small, fill="#444444")
    d.rectangle((160, 250, 1630, 970), outline="#444444", width=12)
    # Durchgänge und getrennte Wartungswege sind die operative Information des Plans.
    d.rectangle((580, 950, 840, 985), fill="#fafafa")
    d.line((580, 970, 580, 825), fill="#777777", width=3)
    d.arc((580, 825, 870, 1115), 180, 270, fill="#777777", width=2)
    d.text((580, 990), "Servicetor / frei halten", font=small, fill="black")
    for x in range(260, 570, 35):
        d.line((x, 880, x + 70, 940), fill="#d8dddd", width=2)
    d.rectangle((255, 865, 550, 945), outline="#9b5050", width=2)
    d.text((270, 890), "Keine Paletten", font=small, fill="#793f3f")
    d.rectangle((275, 340, 410, 500), fill="#dfe7de", outline="#344b40", width=3)
    d.text((295, 360), "Z1", font=bold, fill="black")
    d.text((290, 407), "Zuführer", font=small, fill="black")
    for x in [440, 585, 730, 875]:
        d.rectangle((x, 340, x + 132, 500), fill="#e1e5e8", outline="#53616c", width=3)
    d.text((555, 375), "K1   FB-450", font=bold, fill="black")
    d.rectangle((1040, 340, 1240, 500), fill="#ece5d9", outline="#83755c", width=3)
    d.text((1070, 385), "U1 / UV", font=regular, fill="black")
    d.line((410, 515, 1020, 515), fill="#884e4e", width=3)
    d.text((440, 530), "Gemeinsame Not-Halt-Kette Z1 / K1", font=small, fill="#713d3d")
    d.rectangle((440, 670, 1010, 810), fill="#e1e5e8", outline="#53616c", width=3)
    d.text((605, 711), "K2   SD-720", font=bold, fill="black")
    d.rectangle((1040, 670, 1240, 810), fill="#ece5d9", outline="#83755c", width=3)
    d.text((1070, 720), "T2 / IR", font=regular, fill="black")
    d.rectangle((288, 685, 408, 790), fill="#dde5e4", outline="#536b68", width=3)
    d.text((313, 720), "P-17", font=regular, fill="black")
    d.line((408, 730, 440, 730), fill="#536b68", width=8)
    d.text((270, 820), "Versorgung / Rücklauf", font=small, fill="black")
    d.rectangle((1390, 330, 1570, 515), fill="#e8e8e8", outline="#444444", width=3)
    d.text((1410, 348), "G1", font=bold, fill="black")
    d.text((1405, 395), "Wartungsnetz", font=small, fill="black")
    d.text((1405, 429), "Schlüssel vor Ort", font=small, fill="black")
    d.rectangle((1400, 695, 1560, 815), outline="#777777", width=3)
    d.text((1420, 715), "Teile R3", font=regular, fill="black")
    for x in range(460, 1240, 25):
        d.line((x, 617, x + 12, 617), fill="#989898", width=3)
    d.text((705, 574), "Wartungsgang 1,8 m", font=small, fill="#555555")
    d.line((160, 210, 1630, 210), fill="#666666", width=2)
    d.line((160, 192, 160, 228), fill="#666666", width=2)
    d.line((1630, 192, 1630, 228), fill="#666666", width=2)
    d.text((750, 173), "ca. 24,0 m", font=small, fill="black")
    d.text((75, 1090), "Bestand: G1 und P-17 vorhanden. Neue Rücklaufmessstelle und G2 noch nicht eingebaut.", font=regular, fill="black")
    d.text((75, 1140), "Skizze ohne Maßstab. Für Montage aufmessen. Kompressor und Absaugzentrale außerhalb Halle 2.", font=small, fill="#444444")
    im.save(CASE / FILES[17], dpi=(150, 150))


def recalculate(source):
    binary = office_binary()
    if not binary:
        raise RuntimeError("SOFFICE setzen: gespeicherte Formelergebnisse erfordern Headless-Office.")
    with tempfile.TemporaryDirectory(prefix="kassel-recalc-") as temporary:
        root = Path(temporary)
        out = root / "out"
        out.mkdir()
        command = [binary, f"-env:UserInstallation={(root / 'profile').as_uri()}", "--headless",
                   "--convert-to", "xlsx", "--outdir", str(out), str(source)]
        code, details = run_office(command, env=os.environ.copy(), timeout=180)
        result = out / source.name
        if code or not result.is_file():
            raise RuntimeError(f"Office-Neuberechnung fehlgeschlagen: {details}")
        shutil.copyfile(result, source)


def make_workbook(destination=None, changes=None):
    rows = [
        ["Fuldabogen Spezialdruck GmbH"],
        ["Kostenvergleich 2027"],
        ["Leonie Hartung · 22.09.2026 · Nettobeträge in EUR; keine Preisfreigabe"],
        [],
        ["Position", "Werkspur bis 9.600 h", "Werkspur bei Planung", "Druckerei Vorschlag"],
        ["Jährliche Betreuung", "=B14*'Ansätze'!$B$19", "=C14*'Ansätze'!$B$19", "=D14*'Ansätze'!$B$19"],
        ["Material über Kontingent", "=MAX('Ansätze'!$B$7-'Ansätze'!C10,0)", "=MAX('Ansätze'!$B$7-'Ansätze'!C11,0)", "=MAX('Ansätze'!$B$7-'Ansätze'!C12,0)"],
        ["Einmaliger Umbau", "='Ansätze'!E10", "='Ansätze'!E11", "='Ansätze'!E12"],
        ["Gesamt netto 2027", "=SUM(B6:B8,B18)", "=SUM(C6:C8,C18)", "=SUM(D6:D8,D18)"],
        ["Umsatzsteuer", "=ROUND(B9*'Ansätze'!$B$8,2)", "=ROUND(C9*'Ansätze'!$B$8,2)", "=ROUND(D9*'Ansätze'!$B$8,2)"],
        ["Gesamt brutto 2027", "=SUM(B9:B10)", "=SUM(C9:C10)", "=SUM(D9:D10)"],
        ["Mehrbetrag zur Gegenfassung netto", "=B9-$D$9", "=C9-$D$9", "=D9-$D$9"],
        [],
        ["Monat inkl. Bereitschaft / Remote", "=SUM('Ansätze'!B10,'Ansätze'!$B$14:$B$15)", "=IF(SUM('Ansätze'!B5:B6)<='Ansätze'!B20,'Ansätze'!B10,'Ansätze'!B11)+SUM('Ansätze'!B14:B15)", "='Ansätze'!B12"],
        ["Jahresstunden des Preisstands", "='Ansätze'!B20", "=SUM('Ansätze'!B5:B6)", "=C15"],
        ["Enthaltene Entstörungsstunden", "='Ansätze'!D10", "='Ansätze'!D11", "='Ansätze'!D12"],
        ["Angenommene Entstörungsstunden", "='Ansätze'!$B$18", "='Ansätze'!$B$18", "='Ansätze'!$B$18"],
        ["Zusätzliche Entstörungsstunden netto", "=MAX(B17-B16,0)*'Ansätze'!$B$21", "=MAX(C17-C16,0)*'Ansätze'!$B$21", "=MAX(D17-D16,0)*'Ansätze'!$C$21"],
        ["Betreuung 2028 nur bei maximaler Erhöhung", "=ROUND(B6*(1+'Ansätze'!F10),2)", "=ROUND(C6*(1+'Ansätze'!F11),2)", "=ROUND(D6*(1+'Ansätze'!F12),2)"],
        ["Mehrbetrag Betreuung gegenüber 2027", "=B19-B6", "=C19-C6", "=D19-D6"],
        [],
        ["Bis 9.600 h: Angebotsuntergrenze, nicht die Planung von 10.900 h."],
        ["Materialansatz ohne Motoren, Rechner und UV-Leuchtmittel; nur Stückpreise bis 750 EUR."],
        ["36 Entstörungsstunden liegen in allen Kontingenten. Zusätzliche Stunden sind hier nicht angesetzt."],
        ["2028: vertragliche Erhöhungsgrenzen, keine Prognose und kein vorhandener Indexnachweis."],
        ["Altvertrag: 19.200 EUR netto pro Jahr, Ende 31.12.2026; keine Verlängerungsofferte."],
    ]
    sources = [
        ["Ansätze und Quellen"],
        ["Budget B-2027/09 · Eingaben aus den bezeichneten Unterlagen"],
        [],
        ["Treiber", "Wert", "Einheit", "", "Quelle"],
        ["K1 Planung 2027", 5400, "h", "", f"{FILES[25]}, Ziffer 1"],
        ["K2 Planung 2027", 5500, "h", "", f"{FILES[25]}, Ziffer 1"],
        ["Gedeckter Teileverbrauch", 3900, "EUR netto", "", f"{FILES[25]}, Ziffer 1; Einkaufsreserve"],
        ["Umsatzsteuer", 0.19, "Satz", "", f"{FILES[25]}, Ziffer 2"],
        ["Preisstand", "Monat EUR", "Teile EUR/Jahr", "Arbeit h/Jahr", "Umbau EUR", "Anpassung max."],
        ["Werkspur ≤ 9.600 h", 2150, 3500, 40, 4800, 0.05],
        ["Werkspur > 9.600 h", 2390, 3500, 40, 4800, 0.05],
        ["Druckerei ≤ 12.000 h", 2450, 6000, 60, 4200, 0.03],
        [],
        ["Werkspur Bereitschaft", 450, "EUR/Monat", "", f"{FILES[16]}, Ziffer 10"],
        ["Werkspur Remote", 120, "EUR/Monat", "", f"{FILES[16]}, Ziffer 10"],
        ["Werkspur Zeilen 10/11", "", "", "", f"{FILES[16]}, Ziffern 4, 7, 10 bis 12"],
        ["Druckerei Zeile 12", "", "", "", f"{FILES[20]}, Ziffern 4, 7, 10 bis 12"],
        ["Entstörungsansatz 2027", 36, "h", "", f"{FILES[25]}, Ziffer 1"],
        ["Monate im Kalenderjahr", 12, "Monate", "", "Rechenkonstante: Januar bis Dezember"],
        ["Untere Stufengrenze", 9600, "h", "", f"{FILES[16]}, Ziffer 10"],
        ["Mehrstunde Anbieter / Kunde", 125, 115, "EUR/h", "Vertragsfassungen, jeweils Ziffer 4"],
        ["Zahlungsabgleich Bestand", "Brutto EUR", "Bezahlt EUR", "Offen EUR", "Quelle"],
        ["WS-260701", 5712, "=3000+2712", "=B23-C23", f"{FILES[9]}; {FILES[11]}"],
        ["WS-260914", 2064.65, "=1000+500", "=B24-C24", f"{FILES[10]}; {FILES[11]}"],
        [],
        ["Budgetmaterial 2027 ist kein Ist-Verbrauch. Materialliste 2026 enthält 1.283 EUR netto."],
    ]
    source = destination or CASE / FILES[22]
    with tempfile.TemporaryDirectory(prefix="kassel-workbook-payload-") as directory:
        payload = Path(directory) / "source.json"
        payload.write_text(json.dumps({"Vergleich": rows, "Ansätze": sources}, ensure_ascii=False), encoding="utf-8")
        subprocess.run([node_binary(), str(ROOT / "scripts/build-vertragserstellung-kassel-workbook.mjs"),
                        str(payload), str(source), json.dumps(changes or {})], check=True, timeout=180)
    recalculate(source)
    computed = load_workbook(source, data_only=True, read_only=True)
    print("Gespeicherte Nettosummen:", [computed["Vergleich"].cell(9, c).value for c in (2, 3, 4)])


def mail(number, sender_name, sender, recipient, date, subject, body, attachments=(), reply=None, cc=None):
    message = EmailMessage(policy=policy.SMTP)
    message["From"] = f"{sender_name} <{sender}>"
    message["To"] = recipient
    if cc:
        message["Cc"] = cc
    message["Date"] = format_datetime(datetime.fromisoformat(date))
    message["Message-ID"] = f"<fb118-{number:02}-2026@{sender.split('@')[1]}>"
    message["Subject"] = subject
    message["X-Mailer"] = "Office Mail 16.0"
    message["Return-Path"] = f"<{sender}>"
    message["Received"] = f"from mail.{sender.split('@')[1]} by archive.fuldabogen-spezialdruck.de with ESMTP; {message['Date']}"
    if reply:
        message["In-Reply-To"] = f"<fb118-{reply[0]:02}-2026@{reply[1]}>"
        message["References"] = message["In-Reply-To"]
    if attachments:
        body += "\n\nAnlagen:\n" + "\n".join(FILES[n] for n in attachments)
    message.set_content(body + "\n", charset="utf-8")
    for n in attachments:
        path = CASE / FILES[n]
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        main, sub = mime.split("/", 1)
        message.add_attachment(path.read_bytes(), maintype=main, subtype=sub, filename=path.name)
    (CASE / FILES[number]).write_bytes(message.as_bytes())


def make_mails():
    mail(1, "Maren Brückner", "m.brueckner@fuldabogen-spezialdruck.de", "Dirk Seidel <d.seidel@werkspur-maschinenservice.de>",
         "2026-09-14T10:12:00+02:00", "FB-118 / Anschluss ab Januar und Stillstand vom Samstag",
         "Sehr geehrter Herr Seidel,\n\n"
         "unser Vertrag endet am 31. Dezember. Wir wollen die vorhandenen Linien weiter betreiben, aber nicht mit "
         "einem unbesetzten Wochenende im neuen Jahr starten. Ihr Angebot vom August liegt im Einkauf. Nach der "
         "Nacht von Freitag auf Samstag brauchen wir eine genauere Beschreibung dessen, was im Stillstand passiert.\n\n"
         "Herr Möller hat die Zeiten getrennt: 00:40 Stillstand, 04:10 langsamer Wiederanlauf, 06:55 volle Leistung. "
         "Der Vertrieb hatte aus dem ersten Rückruf bereits eine Fertigmeldung gemacht. Das war für die "
         "Versandplanung nicht brauchbar. Bitte lassen Sie uns Reaktion, Ankunft und Wiederherstellung einzeln benennen.\n\n"
         "Unsere Maschinen werden nicht ersetzt. Die Zuführung Z1 ist praktisch Teil der Linie, auch wenn sie "
         "nicht von demselben Hersteller stammt. Für mich muss im Ernstfall eine Firma koordinieren. Die "
         "IT wird einem Zugriff auf Kundenaufträge nicht zustimmen. Herr Möller kann lokale Zugriffe freigeben.\n\n"
         "Ich sende den Altvertrag, das aktuelle Register und den Schichtauszug. Bitte stimmen Sie die "
         "Fassung mit Frau Hartung ab. Eine Verlängerung zu Ihren Angebotsbedingungen ist damit noch nicht erklärt.\n\n"
         "Mit freundlichen Grüßen\nMaren Brückner\nGeschäftsführerin\nFuldabogen Spezialdruck GmbH\nAm Farbhof 18, 34123 Kassel",
         (2, 3, 4), cc="Leonie Hartung <l.hartung@fuldabogen-spezialdruck.de>")
    mail(13, "Dirk Seidel", "d.seidel@werkspur-maschinenservice.de", "Maren Brückner <m.brueckner@fuldabogen-spezialdruck.de>",
         "2026-08-28T14:36:00+02:00", "WS-260828 / Betreuung Ihrer Linien ab 2027",
         "Sehr geehrte Frau Brückner,\n\n"
         "anbei die Preise für die Weiterbetreuung. Die reine Grundwartung ist nur die kleine Variante. "
         "Wenn Sie Entstörungsstunden und Teile mit absichern möchten, ist das Paket Betrieb die passende "
         "Kalkulationsgrundlage. Bereitschaft und Plattform stehen separat darunter, damit Sie diese Kosten erkennen.\n\n"
         "Wir haben zunächst die Stufe bis 9.600 gemeinsamen Betriebsstunden gerechnet. Beim letzten Gespräch "
         "war von zwei Schichten plus Spitzen die Rede. Bitte teilen Sie uns Ihre Planung für beide Linien "
         "zusammen mit. Eine dritte Schicht auf nur einer Anlage kann die Stufe bereits verändern.\n\n"
         "Unser Anschlussblatt zeigt den Zugang, mit dem die Techniker ohne lange Einrichtung diagnostizieren "
         "können. Ein neues Gateway ist dafür nicht zwingend, würde aber die Kontenverwaltung vereinfachen. "
         "Farbdateien sollen auf Ihrer Seite bleiben. Das freie Auftragsfeld müssen wir vor dem Start ausblenden.\n\n"
         "Ich halte das Angebot bis zum 30. September offen. Über eine feste Wiederherstellungsfrist kann ich "
         "ohne Lagerkonzept für die Sonderteile noch keine Zusage machen.\n\nMit freundlichen Grüßen\nDirk Seidel\n"
         "Geschäftsführer\nWerkspur Maschinenservice GmbH\nWerkhof 7, 34253 Lohfelden", (12, 14))
    mail(15, "Leonie Hartung", "l.hartung@fuldabogen-spezialdruck.de", "Dirk Seidel <d.seidel@werkspur-maschinenservice.de>",
         "2026-09-16T11:08:00+02:00", "Re: FB-118 / Reichweite und Materialkontingent",
         "Sehr geehrter Herr Seidel,\n\n"
         "wir benötigen ein einheitliches Monatsentgelt, das auch die Nachtbereitschaft und den Zugang enthält. "
         "Die Beschränkung auf Montag bis Samstag passt nicht zu unseren Einrichtefenstern am Sonntag. "
         "Nur Wartung plus ein Rückrufversprechen wird die Geschäftsführung nicht freigeben.\n\n"
         "Bitte nehmen Sie Z1 in die Betreuung auf. Im August hat Ihre Technikerin zwar die gemeinsame "
         "Not-Halt-Kette geprüft, die Mechanik des Zuführers aber nicht. Genau zwischen diesen Zuständigkeiten "
         "bleiben wir im Alltag hängen. Bei den Trocknern gehen wir davon aus, dass sie weiterhin erfasst sind.\n\n"
         "Das Teilebudget von 3.500 EUR sagt ohne Einzelpreisgrenze wenig aus. Eine einzelne Komponente kann "
         "teurer sein. Wir wünschen 6.000 EUR ohne 750-EUR-Grenze; Farben und Waschmittel beschaffen wir selbst. "
         "Für 24/7 und die höheren Kontingente würden wir 2.450 EUR netto im Monat vorschlagen, bis zu "
         "12.000 Stunden für beide Linien. Das ist unser Verhandlungsangebot, nicht die Bestätigung Ihres Preises.\n\n"
         "Bei der Rechnung WS-260914 lassen wir zunächst 1.000 EUR überweisen. Wir wollen die "
         "Bereitschaftspauschale verstehen, obwohl der Techniker erst um 01:25 zurückrief. Die technische "
         "Leistung und die Preisfrage des neuen Vertrags sollten wir nicht miteinander verrechnen.\n\n"
         "Mit freundlichen Grüßen\nLeonie Hartung\nEinkauf und Controlling\nFuldabogen Spezialdruck GmbH",
         reply=(1, "fuldabogen-spezialdruck.de"))
    mail(19, "Dirk Seidel", "d.seidel@werkspur-maschinenservice.de", "Leonie Hartung <l.hartung@fuldabogen-spezialdruck.de>",
         "2026-09-18T09:24:00+02:00", "FB-118 / Vollständige Vertragsfassung vom 18. September",
         "Sehr geehrte Frau Hartung,\n\n"
         "ich sende Ihnen unsere vollständig durchgeschriebene Fassung. Die sechs Wartungen enthalten die "
         "Trockner. Z1 können wir ohne Zugriff auf die Herstellerdiagnose nicht in die Pauschale nehmen. "
         "Wir würden dort die Schnittstelle prüfen und einen Zusatzauftrag abstimmen.\n\n"
         "Das Paket ist mit 40 Stunden, 3.500 EUR Teilebudget und gesonderter Bereitschaft kalkuliert. "
         "Eine feste Achtstunden-Wiederherstellung haben wir nicht aufgenommen. Die Formulierung zur "
         "Ankunft ist bewusst ein Ziel, keine garantierte Frist. Eine Ersatzpumpe P-17 können wir beschaffen, "
         "aber nicht jede Sondersteuerung vorhalten.\n\n"
         "Im September-Einsatz waren 00:48 die telefonische Annahme und 01:25 der technische Rückruf. "
         "Der Altvertrag enthält nachts keine zugesagte Bereitschaft; die 240 EUR fallen für den "
         "übernommenen Einsatz an. Frau Weiß erwartet Ihre restliche Zahlung zur Rechnung wie ausgewiesen.\n\n"
         "Die Laufzeit von drei Jahren brauchen wir für die Personalplanung. Auch die Haftungsgrenze "
         "ist Bestandteil dieser Kalkulation. Bitte schicken Sie eine zusammenhängende Gegenfassung, "
         "damit wir nicht mit einzelnen E-Mail-Sätzen arbeiten. Das Umbauangebot bleibt ein eigener Auftrag.\n\n"
         "Mit freundlichen Grüßen\nDirk Seidel\nGeschäftsführer\nWerkspur Maschinenservice GmbH",
         (16, 23), reply=(15, "fuldabogen-spezialdruck.de"))
    mail(21, "Leonie Hartung", "l.hartung@fuldabogen-spezialdruck.de", "Dirk Seidel <d.seidel@werkspur-maschinenservice.de>",
         "2026-09-22T10:40:00+02:00", "FB-118 / Gegenfassung und Stundenplanung 2027",
         "Sehr geehrter Herr Seidel,\n\n"
         "anbei unsere Fassung vom 21. September und die heute ergänzte Kostenrechnung. Wir planen "
         "5.400 Stunden K1 und 5.500 Stunden K2. Damit würden wir in Ihrem Paket bereits in der "
         "höheren Stufe beginnen. Bitte vergleichen Sie unseren Monatsbetrag daher nicht nur mit 2.150 EUR.\n\n"
         "Wir haben eine einjährige Erstlaufzeit mit Verlängerung vorgesehen. Eine Preisänderung soll "
         "an einen veröffentlichten Index anknüpfen, nicht nur an Ihre eigenen Kosten. Bei einer "
         "Erhöhung möchten wir aussteigen können. Ihr Ausschluss sämtlicher Produktionsausfälle "
         "ist für uns bei einem Vertrag über Entstörung schwer vermittelbar.\n\n"
         "Für den Zusatzumbau bieten wir 4.200 EUR nach ausdrücklicher Abnahme. Der Produktionslauf "
         "muss sechs Stunden mit Sonderfarbe umfassen. Der erfolgreiche Standardfarbenlauf im August "
         "hat uns die spätere Störung nicht erklärt. Bitte keine Anzahlung ohne gesonderte Bestellung anfordern.\n\n"
         "Für WS-260914 sind nach der zweiten Zahlung insgesamt 1.500 EUR angewiesen. Über den "
         "Rest von 564,65 EUR wollen Frau Weiß und ich am Donnerstag sprechen. Wir behaupten damit "
         "keine abschließende Kürzung und erkennen auch keinen bestimmten Abzug an.\n\n"
         "Frau Brückner hat mich zur Verhandlung, nicht zur Unterzeichnung bevollmächtigt. Die "
         "Gegenfassung ist daher noch keine Abschlussfreigabe.\n\nMit freundlichen Grüßen\nLeonie Hartung\n"
         "Einkauf und Controlling\nFuldabogen Spezialdruck GmbH", (20, 22), reply=(19, "werkspur-maschinenservice.de"),
         cc="Maren Brückner <m.brueckner@fuldabogen-spezialdruck.de>")
    mail(26, "Dirk Seidel", "d.seidel@werkspur-maschinenservice.de", "Leonie Hartung <l.hartung@fuldabogen-spezialdruck.de>",
         "2026-09-23T08:52:00+02:00", "Re: FB-118 / Besprechung am Freitag",
         "Sehr geehrte Frau Hartung,\n\n"
         "die 10.900 Stunden habe ich an die Disposition gegeben. Auf dieser Basis kostet unser "
         "Paket 2.390 EUR zuzüglich 450 EUR Bereitschaft und 120 EUR Plattform im Monat. Die "
         "ältere 2.150-EUR-Stufe ist für Ihre Planung nicht der Ansatz.\n\n"
         "Ich kann Ihre Gegenfassung noch nicht annehmen. Wir sprechen am Freitag, dem 25. September, "
         "um 10:00 Uhr. Besonders 24/7, die zugesagten Wiederherstellungszeiten, Motoren im "
         "Teilebudget und die Höhe der Ausfallhaftung muss ich mit Serviceleitung und Versicherer besprechen. "
         "Auch die 4.200 EUR für sechs Stunden Umbau-Probelauf sind nicht bestätigt.\n\n"
         "Anbei die Materialentnahmen aus den beiden Augustwartungen und der Septemberstörung. "
         "Das ist nur dieser Ausschnitt, nicht eine vollständige Verbrauchsstatistik Ihrer Produktion. "
         "Die 381 EUR gehören in das alte Wartungskontingent, die 902 EUR aus dem Einsatz sind "
         "gesonderte Teile. Bitte das nicht doppelt in die offene Rechnung übernehmen.\n\n"
         "Die Reservierung Anfang Januar bleibt vorläufig. Ohne separaten Auftrag lösen wir weder "
         "die Teilebestellung für G2 noch den Umbau aus. Die Bindung unseres Angebots bis "
         "30. September bleibt zunächst bestehen. Aus unserem Termin ergibt sich keine "
         "Verlängerung des alten Vertrags.\n\nMit freundlichen Grüßen\nDirk Seidel\nGeschäftsführer\n"
         "Werkspur Maschinenservice GmbH", (24,), reply=(21, "fuldabogen-spezialdruck.de"))


def main():
    CASE.mkdir(parents=True, exist_ok=True)
    register_fonts()
    make_pdfs()
    make_contract(16, SERVICE, SUPPLIER_PAGES, "18.09.2026", "Lieferantenfassung")
    make_contract(20, PRINTER, BUYER_PAGES, "21.09.2026", "Druckereifassung")
    make_records()
    make_plan()
    make_workbook()
    make_mails()
    print(f"{len(FILES)} native Quellen erstellt: {CASE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
