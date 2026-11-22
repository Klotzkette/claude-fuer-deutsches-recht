"""Erzeugt die vier ergänzenden Geschäftsunterlagen der Neuralis-Akte."""

from datetime import datetime
from decimal import Decimal
from email import policy
from email.message import EmailMessage
from pathlib import Path
from zipfile import ZipFile

from lxml import etree

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.page import PageMargins
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas


def auftragsbestaetigung(path):
    pdf = Canvas(str(path), pagesize=A4, invariant=True)
    pdf.setTitle("Auftragsbestätigung AP-230627-04")
    pdf.setAuthor("Altmühl Prüftechnik GmbH")
    petrol, tint, ink = "#144548", "#EDF3F2", "#202B31"

    def line(x, y, text, font="Times-Roman", size=11, color=ink):
        pdf.setFont(font, size)
        pdf.setFillColor(HexColor(color))
        pdf.drawString(x, y, text)

    pdf.setFillColor(HexColor(petrol))
    pdf.rect(0, 821, A4[0], 21, fill=1, stroke=0)
    line(54, 774, "ALTMÜHL", "Helvetica-Bold", 24, petrol)
    line(55, 755, "P R Ü F T E C H N I K   G M B H", "Helvetica", 9, petrol)
    line(54, 707, "Neuralis MedTech GmbH")
    line(54, 692, "Einkauf · z. Hd. Frau Eva Dorn")
    line(54, 677, "Henkestraße 91")
    line(54, 662, "91054 Erlangen")
    line(359, 708, "VERTRIEB INNENDIENST", "Helvetica-Bold", 8, petrol)
    line(359, 688, "Lea Körner")
    line(359, 671, "auftraege@altmuehl-prueftechnik.example", "Helvetica", 8.5)
    line(359, 650, "27. Juni 2023 · 14:20 Uhr", "Helvetica", 9)
    line(54, 600, "Auftragsbestätigung", "Times-Bold", 23)
    line(54, 578, "AP-230627-04    /    Ihre Bestellung E-2306-19", "Helvetica-Bold", 10, petrol)

    line(54, 536, "Sehr geehrte Frau Dorn,")
    for i, row in enumerate([
        "vielen Dank für die heute von Herrn Dr. Henrik Vogt unterzeichnete Bestellung. Wir",
        "haben den Klimaschrank für Ihren Prüfraum reserviert. Die heute Vormittag ergänzte",
        "Aufstellung aus unserem Angebot ist Bestandteil des Auftrags.",
    ]):
        line(54, 510 - 15 * i, row)
    pdf.setFillColor(HexColor(petrol))
    pdf.rect(54, 430, 487, 25, fill=1, stroke=0)
    line(64, 439, "POSITION", "Helvetica-Bold", 8, "#FFFFFF")
    line(108, 439, "LEISTUNG", "Helvetica-Bold", 8, "#FFFFFF")
    line(440, 439, "NETTO / EUR", "Helvetica-Bold", 8, "#FFFFFF")
    for pos, (desc, price) in enumerate([
        ("Klimaschrank einschließlich Anlieferung", "54.900,00"),
        ("Einbau und Anschluss am vorhandenen Messplatz", "5.800,00"),
        ("Funktionsabnahme mit Messprotokoll", "1.700,00"),
    ], start=1):
        y = 437 - pos * 25
        if pos % 2:
            pdf.setFillColor(HexColor(tint))
            pdf.rect(54, y - 8, 487, 25, fill=1, stroke=0)
        line(64, y, f"{pos:02}", "Helvetica", 9)
        line(108, y, desc)
        pdf.drawRightString(527, y, price)
    pdf.setStrokeColor(HexColor(petrol))
    pdf.line(54, 350, 541, 350)
    line(108, 330, "Auftragswert netto", "Times-Bold", 11)
    pdf.drawRightString(527, 330, "62.400,00")
    for i, row in enumerate([
        "Den Schrank liefern wir am Freitag, 30. Juni, an Ihre Warenannahme in Erlangen.",
        "Für den Einbau nach den Betriebsferien stimmen wir den Zugang zum Prüfraum",
        "gesondert mit Ihnen ab. Den Technikereinsatz und die Abnahme rechnen wir nach",
        "dem Termin unter derselben Bestellnummer ab.",
    ]):
        line(54, 290 - 15 * i, row)
    line(54, 207, "Freundliche Grüße")
    line(54, 178, "Lea Körner", "Times-Bold")
    line(54, 160, "Auftragsabwicklung", "Times-Roman", 10)
    pdf.line(54, 60, 541, 60)
    line(54, 42, "ALTMÜHL PRÜFTECHNIK GMBH  /  AUFTRAGSABWICKLUNG", "Helvetica", 8, petrol)
    line(426, 42, "AP-230627-04   ·   1 / 1", "Helvetica", 8, petrol)
    pdf.showPage()
    pdf.save()


def reisekosten(path):
    from grundakte_bauen import stable_office

    book = Workbook()
    book.properties.creator = "Caroline Benkert · Neuralis MedTech GmbH"
    book.properties.title = "Reisekosten RK-2307-04"
    sheet = book.active
    sheet.title = "RK-2307-04"
    sheet.sheet_view.showGridLines = False
    widths = [13, 16, 45, 23, 15]
    for i, width in enumerate(widths, 1):
        sheet.column_dimensions[get_column_letter(i)].width = width

    def band(row, value, dark=False):
        sheet.merge_cells(start_row=row, start_column=1, end_row=row, end_column=5)
        cell = sheet.cell(row, 1, value)
        cell.font = Font(name="Arial", size=13 if dark else 10, bold=True,
                         color="FFFFFF" if dark else "144548")
        cell.fill = PatternFill("solid", fgColor="144548" if dark else "DCEBE8")
        cell.alignment = Alignment(vertical="center", indent=1)
        sheet.row_dimensions[row].height = 28 if dark else 22

    band(1, "Neuralis MedTech GmbH    /    Reisekosten", True)
    band(2, "Finanzen Erlangen     ·     Abrechnung RK-2307-04")
    entries = {
        4: ("Reisender", "Dr. Henrik Vogt · Personalnummer 04"),
        5: ("Reiseweg", "Erlangen – Würzburg – Erlangen, 4. Juli 2023"),
        6: ("Termin", "Abstimmung zur Geräteübergabe mit der Studienkoordination"),
        7: ("Abrechnung", "5. Juli eingereicht · Belegabgleich Caroline Benkert am 10. Juli"),
    }
    for row, (label, value) in entries.items():
        sheet.merge_cells(start_row=row, start_column=1, end_row=row, end_column=2)
        sheet.merge_cells(start_row=row, start_column=3, end_row=row, end_column=5)
        sheet.cell(row, 1, label).font = Font(name="Arial", size=10, bold=True, color="144548")
        sheet.cell(row, 3, value).font = Font(name="Arial", size=10)
        sheet.row_dimensions[row].height = 17
    band(9, "Belege zur Reise")
    for col, label in enumerate(["Datum", "Beleg", "Ausgabe", "Zahlweg", "Betrag EUR"], 1):
        cell = sheet.cell(10, col, label)
        cell.font = Font(name="Arial", size=10, bold=True, color="144548")
    rows = [
        ("01", "Bahnfahrt, Hin- und Rückfahrt", "Karte Vogt", 54.80),
        ("02", "Taxi vom Hauptbahnhof zum Prüfzentrum", "bar, Vogt", 18.60),
        ("03", "Straßenbahn zurück zum Hauptbahnhof", "bar, Vogt", 3.00),
    ]
    for row, (ref, item, payer, amount) in enumerate(rows, 11):
        for col, value in enumerate([datetime(2023, 7, 4), ref, item, payer, amount], 1):
            cell = sheet.cell(row, col, value)
            cell.font = Font(name="Arial", size=10)
            cell.fill = PatternFill("solid", fgColor="EDF3F2" if row % 2 else "FFFFFF")
        sheet.cell(row, 1).number_format = "dd.mm.yyyy"
        sheet.cell(row, 5).number_format = "#,##0.00"
        sheet.row_dimensions[row].height = 20
    sheet["C15"] = "Summe der eingereichten Belege"
    sheet["E15"] = "=SUM(E11:E13)"
    band(17, "Auszahlung")
    sheet["A18"] = datetime(2023, 7, 12)
    sheet["A18"].number_format = "dd.mm.yyyy"
    sheet["B18"] = "ZA-0712-08"
    sheet["C18"] = "Überweisung Neuralis MedTech GmbH"
    sheet["D18"] = "Empfänger Dr. Vogt"
    sheet["E18"] = 76.40
    for col in ("E15", "E18"):
        sheet[col].number_format = "#,##0.00"
        sheet[col].font = Font(name="Arial", size=10, bold=True)
    sheet.freeze_panes = "C11"
    sheet.print_area = "A1:E18"
    sheet.print_options.horizontalCentered = True
    sheet.page_setup.orientation = "landscape"
    sheet.page_setup.paperSize = sheet.PAPERSIZE_A4
    sheet.sheet_properties.pageSetUpPr.fitToPage = True
    sheet.page_setup.fitToWidth = sheet.page_setup.fitToHeight = 1
    sheet.page_margins = PageMargins(left=.45, right=.45, top=.55, bottom=.55, header=.2, footer=.2)
    sheet.oddFooter.left.text = "Neuralis MedTech GmbH · Finanzen"
    sheet.oddFooter.right.text = "RK-2307-04  |  &P"
    book.save(path)
    # openpyxl schreibt die Excel-Formel ohne das Ergebnis der Abrechnung.
    # Auch Leser ohne eigene Tabellenkalkulation benötigen beide Angaben.
    member = "xl/worksheets/sheet1.xml"
    with ZipFile(path) as archive:
        xml = etree.fromstring(archive.read(member))
    total_cell = xml.find(".//{*}c[@r='E15']")
    if total_cell.findtext("{*}f") != "SUM(E11:E13)":
        raise ValueError("Unerwartete Summenformel in E15")
    total_cell.find("{*}v").text = str(sum(Decimal(str(row[3])) for row in rows))
    stable_office(path, moment=datetime(2023, 7, 12, 13, 25),
                  replacements={member: etree.tostring(xml)})


def email_file(path, date, sender, recipient, subject, body, *, cc=None):
    message = EmailMessage(policy=policy.SMTP)
    message["Date"] = datetime.fromisoformat(date)
    message["From"] = sender
    message["To"] = recipient
    if cc:
        message["Cc"] = cc
    message["Subject"] = subject
    domain = sender.split("@")[-1].rstrip(">")
    message["Message-ID"] = f"<{date[:10]}.{path.stem.lower()}@{domain}>"
    message.set_content(body)
    path.write_bytes(message.as_bytes())


def build():
    from grundakte_bauen import BASE, CASE, FIRST, HERE, ROOT

    order = CASE / BASE / "A11_Auftragsbestaetigung_Altmuehl.pdf"
    travel = CASE / BASE / "A12_Reisekosten_Pruefzentrum.xlsx"
    credit = CASE / BASE / "A13_Rueckfrage_Privater_Kreditrahmen.eml"
    translation = CASE / FIRST / "B13_Angebotsfrist_Uebersetzung.eml"
    order.parent.mkdir(parents=True, exist_ok=True)
    translation.parent.mkdir(parents=True, exist_ok=True)
    auftragsbestaetigung(order)
    reisekosten(travel)
    email_file(credit, "2023-07-18T09:18:00+02:00",
               "Guido Landmann <g.landmann@firmenkunden-erlangen.example>",
               "Dr. Henrik Vogt <h.vogt@neuralis.example>",
               "Ihr Rückruf gestern / Unterlagen für das Privatkundenteam",
               """Guten Morgen Herr Dr. Vogt,

die Bestätigung vom Freitag zum Investitionskredit 771-4402 habe ich mit Ihrer Einwilligung an meine Kollegin im Privatkundenteam weitergegeben. Sie prüft Ihre Anfrage, den persönlichen Kreditrahmen für den Dachausbau zu erhöhen.

Sie hatten in der Vermögensaufstellung die nächste Tilgungsrate der GmbH eingetragen. Wir brauchen für das private Kreditgespräch daneben den Bestand der übernommenen Sicherheiten. Bitte tragen Sie unter „Bürgschaften“ die Nummer 2021-0417 und den vereinbarten Höchstbetrag von 400.000 Euro ein. Das Feld „Zahlungen aus der Bürgschaft“ können Sie für das erste Halbjahr mit 0 Euro ausfüllen. Die Raten sind vom Geschäftskonto eingegangen.

Sobald die ergänzte Seite vorliegt, meldet sich die Kollegin mit einem Terminvorschlag. Über den zusätzlichen Rahmen ist noch nicht entschieden. Für die vertraulichen Unterlagen können Sie wieder das Postfach im Onlinebanking verwenden.

Freundliche Grüße
Guido Landmann
Firmenkunden Erlangen · Kreditadministration""")
    email_file(translation, "2026-03-19T16:18:00+01:00",
               "Pauline Riedel <p.riedel@riedel-fachuebersetzungen.example>",
               "Dr. Henrik Vogt <h.vogt@neuralis.example>",
               "Zwei Klinikverträge / Reservierung bis morgen Mittag",
               """Guten Tag Herr Dr. Vogt,

die beiden Fassungen können wir zu den besprochenen 21.600 Euro netto zusammen bearbeiten. Das Vieraugenlektorat ist darin enthalten. Die Frage zur einheitlichen Bezeichnung der Vertragspartner im englischen Text hat Ihre Erläuterung heute Vormittag geklärt.

Für die kommende Woche halte ich Ihnen zwei Plätze bis Freitag, 20. März, 12 Uhr, frei. Eine schriftliche Bestellung zu Ihrem Vorgang E-2603-11 ist heute noch nicht bei uns eingegangen. Bis sie vorliegt, reservieren wir lediglich die Termine und geben die Unterlagen nicht an die Übersetzerinnen weiter. Falls Sie morgen mehr Zeit brauchen, rufen Sie mich bitte kurz vor Mittag an.

Beste Grüße
Pauline Riedel
Projektleitung · Riedel Fachübersetzungen""",
               cc="Eva Dorn <e.dorn@neuralis.example>")
    records = []
    for source in (order, travel, credit, translation):
        relative = source.relative_to(CASE)
        pdf = source if source.suffix == ".pdf" else HERE / "lesefassungen" / relative.with_suffix(".pdf")
        records.append({"source": source.relative_to(ROOT).as_posix(), "archive": relative.as_posix(),
                        "pdf": pdf.relative_to(ROOT).as_posix()})
    return records


if __name__ == "__main__":
    build()
