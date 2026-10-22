#!/usr/bin/env python3
"""Erzeugt die Abschlussunterlagen der Testakten Nordlicht und Havelberg.

Die Unterlagen sind synthetische Schulungsunterlagen. Das Skript schreibt nur
in die beiden zugehörigen Testakten und hält Rechenwerte und Dateinamen an
einer Stelle reproduzierbar zusammen.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_DOWN
from email.message import EmailMessage
from pathlib import Path
import csv

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter


ROOT = Path(__file__).resolve().parents[1]
NORD = ROOT / "testakten" / "insolvenzverwaltung-nordlicht-handels-kiel"
HAVEL = ROOT / "testakten" / "insolvenzverwaltung-moebelwerk-havelberg-regelverfahren"

BLUE = "1F4E78"
LIGHT = "D9EAF7"
GREY = "E7E6E6"
FIXED_CREATED = "2026-10-22T00:00:00Z"


def eur(value: Decimal | int | str) -> str:
    amount = Decimal(str(value)).quantize(Decimal("0.01"))
    return f"{amount:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") + " EUR"


def allocate(total: Decimal, claims: list[tuple[str, Decimal]]) -> list[tuple[str, Decimal, Decimal]]:
    """Verteilt centgenau nach Hare-Niemeyer-Restbeträgen."""
    denominator = sum(amount for _, amount in claims)
    quota = total / denominator
    rows: list[list[object]] = []
    for name, amount in claims:
        exact = amount * quota
        payout = exact.quantize(Decimal("0.01"), rounding=ROUND_DOWN)
        rows.append([name, amount, payout, exact - payout])
    cents = int((total - sum(row[2] for row in rows)) * 100)
    for row in sorted(rows, key=lambda item: item[3], reverse=True)[:cents]:
        row[2] += Decimal("0.01")
    return [(str(name), amount, payout) for name, amount, payout, _ in rows]


def shade(cell, fill: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    tc_pr.append(shd)


def new_doc(title: str, subtitle: str = "") -> Document:
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Cm(2.1)
    section.bottom_margin = Cm(2.0)
    section.left_margin = Cm(2.3)
    section.right_margin = Cm(2.1)
    styles = doc.styles
    styles["Normal"].font.name = "Times New Roman"
    styles["Normal"]._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
    styles["Normal"].font.size = Pt(11)
    for style_name, size in (("Title", 16), ("Heading 1", 14), ("Heading 2", 12), ("Heading 3", 11)):
        style = styles[style_name]
        style.font.name = "Times New Roman"
        style._element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = None
    title_p = doc.add_paragraph(style="Title")
    title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title_p.add_run(title)
    if subtitle:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(subtitle)
        r.bold = True
    doc.core_properties.title = title
    doc.core_properties.author = "Synthetische Testakte"
    doc.core_properties.subject = "Insolvenzverwaltung"
    return doc


def heading(doc: Document, number: str, title: str, level: int = 1) -> None:
    doc.add_heading(f"{number}. {title}", level=level)


def para(doc: Document, text: str, bold_prefix: str | None = None) -> None:
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(6)
    if bold_prefix and text.startswith(bold_prefix):
        p.add_run(bold_prefix).bold = True
        p.add_run(text[len(bold_prefix):])
    else:
        p.add_run(text)


def table(doc: Document, headers: list[str], rows: list[list[object]], widths: list[float] | None = None) -> None:
    t = doc.add_table(rows=1, cols=len(headers))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for index, value in enumerate(headers):
        cell = t.rows[0].cells[index]
        cell.text = value
        shade(cell, LIGHT)
        for run in cell.paragraphs[0].runs:
            run.bold = True
            run.font.name = "Times New Roman"
            run.font.size = Pt(10)
    for source in rows:
        cells = t.add_row().cells
        for index, value in enumerate(source):
            cells[index].text = str(value)
            cells[index].vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
            for paragraph in cells[index].paragraphs:
                for run in paragraph.runs:
                    run.font.name = "Times New Roman"
                    run.font.size = Pt(9)
    if widths:
        for row in t.rows:
            for index, width in enumerate(widths):
                row.cells[index].width = Cm(width)
    doc.add_paragraph()


def save_doc(doc: Document, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(path)


@dataclass(frozen=True)
class Case:
    directory: Path
    company: str
    court: str
    docket: str
    administrator: str


NORD_CASE = Case(NORD, "Nordlicht Handels GmbH", "Amtsgericht Kiel", "10 IN 127/13", "Dr. Jens-Peter Hartmann")
HAVEL_CASE = Case(HAVEL, "Möbelwerk Havelberg GmbH", "Amtsgericht Stendal", "7 IN 41/26", "Dr. Nora Westphal")


def letter_head(doc: Document, case: Case, date: str, subject: str) -> None:
    table(doc, ["Verfahrensangabe", "Wert"], [
        ["Insolvenzgericht", case.court],
        ["Aktenzeichen", case.docket],
        ["Schuldnerin", case.company],
        ["Insolvenzverwaltung", case.administrator],
        ["Datum", date],
        ["Gegenstand", subject],
    ], [5.0, 11.0])


def nord_interim() -> None:
    doc = new_doc("14. Zwischenbericht", "Nordlicht Handels GmbH – AG Kiel 10 IN 127/13")
    letter_head(doc, NORD_CASE, "31. Dezember 2023", "Berichtszeitraum 1. Januar bis 31. Dezember 2023")
    heading(doc, "1", "Auftrag und Stichtag")
    para(doc, "Dieser Bericht schreibt den bisherigen Verfahrensstand bis zum 31. Dezember 2023 fort. Er trennt tatsächlich eingegangene Masse von lediglich erwarteten Zuflüssen. Beträge nach dem Stichtag werden nicht vorweggenommen.")
    heading(doc, "2", "Verfahrensstand")
    para(doc, "Der Geschäftsbetrieb ist seit dem 31. August 2013 eingestellt. Die Waren, Einrichtungen und freien Forderungen sind verwertet. Die Haftungs- und Anfechtungskomplexe sind durch Vergleich und Zahlung erledigt. Die Schlussbearbeitung war zuletzt wegen der steuerlichen Außenprüfung der Jahre 2008 bis 2012 und der abschließenden Kontenabstimmung noch nicht reif.")
    heading(doc, "3", "Steuererstattung und Begriffskorrektur")
    para(doc, "Das Finanzamt Kiel-Süd zahlte am 28. Juni 2023 einen Erstattungsbetrag von 18.420,00 EUR auf das Massekonto. Da das Insolvenzverfahren fortbesteht, handelt es sich um einen späten Massezufluss innerhalb des laufenden Verfahrens. Eine Nachtragsverteilung setzt demgegenüber ein aufgehobenes Verfahren voraus. Der Betrag wird deshalb in die Schlussrechnung und die reguläre Schlussverteilung eingestellt.")
    heading(doc, "4", "Masse und Tabelle")
    table(doc, ["Kontrollgröße", "Stand", "Belegstatus"], [
        ["Massebestand vor Schlusskosten", eur("138564"), "Kontoauszug und Buchungsjournal abgestimmt"],
        ["Noch abzudeckende Schlusskosten", eur("8420"), "Einzelansätze im Kostenblatt"],
        ["Noch nicht gezahlte Restvergütung", eur("9682"), "Festsetzung und Zahlung stehen aus"],
        ["Voraussichtliche Teilungsmasse", eur("120462"), "Erst nach Freigabe und gerichtlicher Zustimmung verfügbar"],
        ["Festgestellte Forderungen nach § 38 InsO", eur("509842"), "Tabellenauszug zum 31.12.2023"],
    ])
    heading(doc, "5", "Offene Abschlussarbeiten")
    table(doc, ["Arbeitsschritt", "Verantwortlich", "Sperrwirkung"], [
        ["Schlusskonto und Buchungsjournal centgenau abstimmen", "Sachbearbeitung und Verwalter", "Sperrt Schlussrechnung"],
        ["Restvergütung und Gerichtskosten belegen", "Verwalter und Gericht", "Sperrt Teilungsmasse"],
        ["Schlussverzeichnis mit gerichtlicher Tabelle abgleichen", "Sachbearbeitung", "Sperrt Quote"],
        ["Schlussbericht, Schlussrechnung und Verzeichnis gemeinsam freigeben", "Dr. Hartmann", "Sperrt Einreichung"],
    ])
    heading(doc, "6", "Ausblick")
    para(doc, "Nach Erledigung der vier Kontrollen soll der Schlussbericht im März 2024 eingereicht werden. Eine Auszahlung wird erst nach gerichtlicher Zustimmung zur Schlussverteilung, Behandlung der fristgebundenen Nachweise und gesonderter menschlicher Zahlungsfreigabe vorbereitet.")
    para(doc, "Dr. Jens-Peter Hartmann\nRechtsanwalt und Insolvenzverwalter")
    save_doc(doc, NORD / "27_zwischenbericht_nr_14_31-12-2023.docx")


def nord_final_report() -> None:
    claims = [("Kieler Volksbank eG", Decimal("214302")), ("Fashion Forward KG", Decimal("23960")),
              ("DAK-Gesundheit", Decimal("12320")), ("IKK Nord", Decimal("9610")),
              ("Bundesagentur für Arbeit", Decimal("84220")),
              ("Übrige Lieferanten und sonstige Gläubiger", Decimal("165430"))]
    payouts = allocate(Decimal("120462"), claims)
    doc = new_doc("Schlussbericht und Schlussrechnung", "Nordlicht Handels GmbH – AG Kiel 10 IN 127/13")
    letter_head(doc, NORD_CASE, "15. März 2024", "Abschlussbericht mit Schlussrechnung und Verteilungsvorschlag")
    heading(doc, "1", "Verfahrensgang")
    para(doc, "Die Schuldnerin beantragte am 14. Januar 2013 die Eröffnung des Insolvenzverfahrens. Das Amtsgericht Kiel eröffnete das Verfahren am 1. Juni 2013 und bestellte Dr. Jens-Peter Hartmann zum Insolvenzverwalter. Nach einem bis zum 31. August 2013 geführten Räumungsverkauf wurde der Geschäftsbetrieb stillgelegt. Die anschließende Abwicklung umfasste Forderungseinzug, Anfechtungsvergleiche, einen Geschäftsführerhaftungsvergleich, die steuerliche Außenprüfung sowie die Schlussbearbeitung.")
    table(doc, ["Datum", "Ereignis", "Abschlussbedeutung"], [
        ["01.06.2013", "Eröffnung und Bestellung", "Beginn der Schlussrechnungsperiode"],
        ["31.08.2013", "Betriebseinstellung", "Ende der Fortführung"],
        ["12.05.2015", "Vergleich Geschäftsführerhaftung", "60.000,00 EUR in Raten vollständig eingegangen"],
        ["28.06.2023", "Steuererstattung", "18.420,00 EUR als laufender Massezufluss verbucht"],
        ["15.03.2024", "Abschlussstichtag", "Konten und Tabelle abgestimmt"],
    ])
    heading(doc, "2", "Sicherung, Betrieb und Buchführung")
    para(doc, "Die bei Eröffnung vorhandenen Kassen- und Bankbestände wurden auf das Massekonto überführt. Die Buchführung wurde aus Bankauszügen, Kassenunterlagen, Debitorenlisten und Einzelbelegen rekonstruiert. Interne Umbuchungen sind in der Schlussrechnung neutralisiert. Der rechnerische Endbestand von 138.564,00 EUR stimmt zum Stichtag mit dem Massekonto überein; ein Kassenbestand besteht nicht mehr.")
    heading(doc, "3", "Verwertung und Anspruchsverfolgung")
    table(doc, ["Vorgang", "Ergebnis", "Status"], [
        ["Räumungsverkauf und Restwaren", eur("176840"), "Belegt und bezahlt"],
        ["Domain, Kundenstamm und Einrichtungen", eur("19540"), "Belegt und bezahlt"],
        ["Freie Forderungen", eur("18420"), "Beitreibung beendet"],
        ["Geschäftsführerhaftung", eur("60000"), "Vergleich vollständig erfüllt"],
        ["Anfechtungsvergleiche DAK und IKK", eur("9260"), "Vollständig erfüllt"],
        ["Steuererstattung", eur("18420"), "Am 28.06.2023 eingegangen"],
        ["Zinsen und sonstige Einnahmen", eur("4484"), "Gebucht"],
    ])
    para(doc, "Die Summe der vorstehenden Positionen beträgt 306.964,00 EUR. Die Schlussrechnung weist 306.764,00 EUR aus, weil ein in den Räumungsverkauf einbezogener Rückläufer von 200,00 EUR im Verwertungsbericht brutto, im Konto aber nach Rückzahlung an den Kunden netto dargestellt war. Die Schlussrechnung folgt dem Konto; die Abweichung ist mit Buchungsbeleg N-2013-0814 dokumentiert.")
    heading(doc, "4", "Schlussrechnung")
    incomes = [("Anfangsbestand und Verwertung", "195580"), ("Forderungseinzug", "18420"),
               ("Haftungs- und Anfechtungserlöse", "69260"), ("Steuererstattung", "18420"),
               ("Zinsen und sonstige Einnahmen", "5084")]
    expenses = [("Stilllegung und Personal", "38420"), ("Lager und Logistik", "18420"),
                ("Versicherungen, Steuern und Verbrauch", "14840"), ("Rechts- und Gutachterkosten", "36460"),
                ("Gerichts- und Verfahrenskosten", "7420"), ("Verwaltervergütung einschließlich noch offener Restvergütung", "48420"),
                ("Sonstige Ausgaben", "4220")]
    table(doc, ["Einnahmeposition", "Betrag"], [[n, eur(v)] for n, v in incomes] + [["Summe Einnahmen", eur("306764")]])
    table(doc, ["Ausgabeposition", "Betrag"], [[n, eur(v)] for n, v in expenses] + [["Summe Ausgaben", eur("168200")]])
    table(doc, ["Abstimmung", "Betrag"], [
        ["Summe Einnahmen", eur("306764")], ["Abzüglich Summe Ausgaben", eur("168200")],
        ["Rechnerischer und tatsächlicher Endbestand", eur("138564")], ["Konkrete Schlusskosten", eur("8420")],
        ["Restvergütung", eur("9682")], ["Teilungsmasse", eur("120462")],
    ])
    heading(doc, "5", "Forderungstabelle und Schlussverzeichnis")
    para(doc, "Die festgestellten Forderungen nach § 38 InsO betragen 509.842,00 EUR. Nachrangige Forderungen und vollständig bestrittene, nicht fristgerecht nachgewiesene Forderungen sind nicht Bestandteil dieser Verteilungsbasis. Absonderungsrechte bestehen nach den abschließenden Prüfungen nicht mehr.")
    table(doc, ["Gläubigergruppe", "Festgestellt", "Auszahlung"], [[n, eur(a), eur(p)] for n, a, p in payouts] + [["Summe", eur("509842"), eur("120462")]])
    quota = Decimal("120462") / Decimal("509842") * Decimal("100")
    para(doc, f"Die ungerundete Quote beträgt {str(quota.quantize(Decimal('0.000001'))).replace('.', ',')} Prozent. Für die Auszahlung wird je Forderung zunächst auf Cent abgerundet. Die verbleibenden vier Cent werden nach den größten Bruchteilsresten verteilt. Dadurch stimmt die Auszahlungssumme centgenau mit der Teilungsmasse überein.")
    heading(doc, "6", "Abschlussreife und mögliche Nachtragspositionen")
    para(doc, "Alle bekannten verwertbaren Massegegenstände sind realisiert. Die Haftungs- und Anfechtungsverfahren sind erledigt. Die Steuererstattung vom 28. Juni 2023 ist in die reguläre Schlussverteilung einbezogen. Ein später tatsächlich zufließender, derzeit weder festgesetzter noch verfügbarer Steuerzins wäre gesondert auf Massezugehörigkeit und die Voraussetzungen einer Nachtragsverteilung zu prüfen; er wird nicht vorweggenommen.")
    heading(doc, "7", "Anträge")
    para(doc, "Es wird beantragt, die Schlussrechnung zu prüfen, der Schlussverteilung nach § 196 Absatz 2 InsO zuzustimmen, den Schlusstermin nach § 197 InsO zu bestimmen und das Verfahren nach belegtem Vollzug der Schlussverteilung gemäß § 200 InsO aufzuheben. Die Auszahlung wird erst nach gerichtlicher Zustimmung und dokumentierter Zahlungsfreigabe ausgeführt.")
    heading(doc, "8", "Anlagen")
    table(doc, ["Anlage", "Bezeichnung", "Kontrollstand"], [
        ["S 1", "Schlussrechnung und Kontenabstimmung", "centgenau abgestimmt"],
        ["S 2", "Schlussverzeichnis", "mit gerichtlicher Tabelle abgeglichen"],
        ["S 3", "Vergütungsantrag und Kostenblatt", "offener Zahlungsbetrag ausgewiesen"],
        ["S 4", "Verwertungs- und Prozessübersicht", "Vollzug belegt"],
        ["S 5", "Freigabevermerk", "gesondert nach interner Prüfung"],
    ])
    para(doc, "Dr. Jens-Peter Hartmann\nRechtsanwalt und Insolvenzverwalter")
    for name in ("05_Schlussbericht_15-03-2024.docx", "24_schlussbericht.docx"):
        save_doc(doc, NORD / name)


def nord_closing_docs() -> None:
    claims = [("Kieler Volksbank eG", Decimal("214302")), ("Fashion Forward KG", Decimal("23960")),
              ("DAK-Gesundheit", Decimal("12320")), ("IKK Nord", Decimal("9610")),
              ("Bundesagentur für Arbeit", Decimal("84220")),
              ("Übrige Lieferanten und sonstige Gläubiger", Decimal("165430"))]
    payouts = allocate(Decimal("120462"), claims)

    doc = new_doc("Schlussverzeichnis", "Nordlicht Handels GmbH – Stand 15. März 2024")
    letter_head(doc, NORD_CASE, "15. März 2024", "Verzeichnis für die Schlussverteilung")
    heading(doc, "1", "Rechenbasis")
    para(doc, "Die Teilungsmasse beträgt 120.462,00 EUR. Die festgestellten Forderungen nach § 38 InsO betragen 509.842,00 EUR. Die Quote wird ungerundet berechnet und erst beim einzelnen Auszahlungsbetrag auf Cent abgerundet.")
    heading(doc, "2", "Verzeichnis")
    table(doc, ["Laufende Nummer und Gläubiger", "Forderung", "Auszahlung", "Status"],
          [[f"{i}. {n}", eur(a), eur(p), "festgestellt; zahlbar nach Freigabe"] for i, (n, a, p) in enumerate(payouts, 1)] +
          [["Summe", eur("509842"), eur("120462"), "Kontrollsumme stimmt"]])
    heading(doc, "3", "Ausgeschlossene und gesondert geführte Positionen")
    para(doc, "Vollständig bestrittene Forderungen ohne fristgerechten Nachweis werden nicht in die Verteilungsbasis eingestellt. Ein nachrangiger Anspruch würde erst nach vollständiger Befriedigung der Forderungen nach § 38 InsO berücksichtigt. Nach der Aktenprüfung liegt keine solche Auszahlungsvoraussetzung vor.")
    save_doc(doc, NORD / "25_schlussverzeichnis.docx")

    doc = new_doc("Interner Freigabevermerk", "Nordlicht Handels GmbH – Abschlussprodukte")
    letter_head(doc, NORD_CASE, "18. März 2024", "Freigabe von Schlussbericht, Schlussrechnung und Schlussverzeichnis")
    heading(doc, "1", "Geprüfte führende Fassungen")
    table(doc, ["Produkt", "Fassung", "Ergebnis"], [
        ["Schlussbericht und Schlussrechnung", "15.03.2024", "inhaltlich und rechnerisch geprüft"],
        ["Schlussverzeichnis", "15.03.2024", "509.842,00 EUR Forderungsbasis; 120.462,00 EUR Auszahlung"],
        ["Kontrollarbeitsmappe", "15.03.2024", "sämtliche Kontrollfelder ohne Differenz"],
    ])
    heading(doc, "2", "Vier-Augen-Prüfung")
    table(doc, ["Kontrolle", "Prüferin oder Prüfer", "Feststellung"], [
        ["Bank gegen Schlussrechnung", "Maren Clausen, Sachbearbeitung", "0,00 EUR Differenz"],
        ["Tabelle gegen Schlussverzeichnis", "RA Dr. Jens-Peter Hartmann", "0,00 EUR Differenz"],
        ["Quote und Centausgleich", "Maren Clausen", "Auszahlung exakt 120.462,00 EUR"],
        ["Rechtliche Einreichungsreife", "RA Dr. Jens-Peter Hartmann", "freigegeben"],
    ])
    heading(doc, "3", "Freigabegrenze")
    para(doc, "Diese Freigabe erlaubt die Einreichung beim Insolvenzgericht. Sie erlaubt keine Auszahlung. Der Zahlungslauf bedarf nach gerichtlicher Zustimmung einer erneuten namentlichen Freigabe.")
    save_doc(doc, NORD / "29_freigabevermerk_abschluss_18-03-2024.docx")

    doc = new_doc("Gerichtliche Verfügung zur Schlussverteilung", "Synthetisches Aktenstück – AG Kiel 10 IN 127/13")
    letter_head(doc, NORD_CASE, "22. März 2024", "Prüfung der Schlussrechnung und Zustimmung zur Schlussverteilung")
    heading(doc, "1", "Verfügung")
    para(doc, "Die Schlussrechnung und das Schlussverzeichnis sind zur Akte genommen. Nach dem derzeitigen Prüfstand wird der Schlussverteilung gemäß § 196 Absatz 2 InsO zugestimmt. Der Verwalter hat vor Auszahlung Änderungen der Tabelle und fristgerechte Nachweise nach den §§ 189 bis 193 InsO zu berücksichtigen.")
    heading(doc, "2", "Schlusstermin")
    para(doc, "Der Schlusstermin wird auf den 19. April 2024 bestimmt. Gegenstand sind die Erörterung der Schlussrechnung, Einwendungen gegen das Schlussverzeichnis und die Entscheidung über nicht verwertbare Gegenstände. Die öffentliche Bekanntmachung und die Niederlegung der Unterlagen erfolgen gesondert.")
    heading(doc, "3", "Vollzugsnachweis")
    para(doc, "Der Verwalter reicht nach Auszahlung eine Summenliste, den Kontennachweis und eine Erklärung über den vollständigen Vollzug ein. Erst danach wird über die Aufhebung des Verfahrens entschieden.")
    save_doc(doc, NORD / "30_verfuegung_schlussverteilung_22-03-2024.docx")

    doc = new_doc("Vollzugsprotokoll der Schlussverteilung", "Nordlicht Handels GmbH – Zahlungslauf 22. April 2024")
    letter_head(doc, NORD_CASE, "24. April 2024", "Zahlung, Rückläuferkontrolle und Kontenabgleich")
    heading(doc, "1", "Freigabe und Ausführung")
    para(doc, "Dr. Jens-Peter Hartmann gab den Zahlungslauf am 22. April 2024 um 09:10 Uhr nach Abgleich der Empfängerdaten frei. Maren Clausen erzeugte die Sammelüberweisung. Eine zweite Kontrolle der Gesamtsumme erfolgte vor der Bankfreigabe durch den Verwalter.")
    heading(doc, "2", "Zahlungslauf")
    table(doc, ["Gläubigergruppe", "Auszahlungsbetrag", "Bankstatus"], [[n, eur(p), "ausgeführt; kein Rückläufer"] for n, _, p in payouts] + [["Summe", eur("120462"), "stimmt mit Teilungsmasse überein"]])
    heading(doc, "3", "Nachkontrolle")
    para(doc, "Der Kontoauszug vom 23. April 2024 weist sämtliche sechs Sammelpositionen aus. Es bestehen keine Rückläufer. Der zur Verteilung bestimmte Betrag ist vollständig ausgekehrt. Kontoschlusskosten von 0,00 EUR sind bestätigt; ein Fremdgeldbestand besteht nicht.")
    save_doc(doc, NORD / "31_vollzugsprotokoll_schlussverteilung_24-04-2024.docx")

    doc = new_doc("Schlussmitteilung", "Nordlicht Handels GmbH – AG Kiel 10 IN 127/13")
    letter_head(doc, NORD_CASE, "24. April 2024", "Nachweis des Vollzugs der Schlussverteilung")
    heading(doc, "1", "Mitteilung")
    para(doc, "Die mit Zustimmung vom 22. März 2024 vorbereitete Schlussverteilung ist vollständig vollzogen. Auf festgestellte Forderungen von 509.842,00 EUR wurden insgesamt 120.462,00 EUR ausgekehrt. Die Auszahlungen und der fehlende Rücklauf sind durch den beigefügten Kontoauszug belegt.")
    heading(doc, "2", "Anregung")
    para(doc, "Es wird angeregt, das Insolvenzverfahren nach § 200 InsO aufzuheben. Ein derzeit nicht vorhandener späterer Massezufluss bleibt einer gesonderten Prüfung nach den §§ 203 bis 205 InsO vorbehalten.")
    save_doc(doc, NORD / "32_schlussmitteilung_24-04-2024.docx")

    doc = new_doc("Beschluss über die Aufhebung", "Synthetisches Aktenstück – AG Kiel 10 IN 127/13")
    letter_head(doc, NORD_CASE, "30. April 2024", "Aufhebung nach vollzogener Schlussverteilung")
    heading(doc, "1", "Entscheidung")
    para(doc, "Das Insolvenzverfahren über das Vermögen der Nordlicht Handels GmbH wird nach vollzogener Schlussverteilung gemäß § 200 Absatz 1 InsO aufgehoben.")
    heading(doc, "2", "Hinweis")
    para(doc, "Sollte nach der Aufhebung ein bislang nicht verfügbarer Massegegenstand ermittelt oder ein zur Masse gehörender Betrag zurückgezahlt werden, bleibt eine Anordnung der Nachtragsverteilung nach § 203 InsO vorbehalten. Dieser Hinweis stellt weder eine solche Anordnung noch die Feststellung der Massezugehörigkeit eines künftigen Anspruchs dar.")
    save_doc(doc, NORD / "26_aufhebungsbeschluss.docx")

    doc = new_doc("Prüf- und Verteilungsvermerk Nachtragsmasse", "Nordlicht Handels GmbH – Steuerzins 2024")
    letter_head(doc, NORD_CASE, "20. Oktober 2024", "Nach Aufhebung zugeflossener Erstattungszins")
    heading(doc, "1", "Neuer Vorgang")
    para(doc, "Das Finanzamt Kiel-Süd zahlte am 12. Oktober 2024 einen Erstattungszins von 3.180,00 EUR aus. Der zugrunde liegende Steuerbescheid betrifft die Veranlagungszeiträume 2008 bis 2012. Der Betrag war beim Vollzug der Schlussverteilung weder festgesetzt noch verfügbar.")
    heading(doc, "2", "Prüfung")
    para(doc, "Vor einem Antrag auf Nachtragsverteilung sind Massezugehörigkeit, Bestandskraft des Bescheids, Abzug konkret entstehender Kosten und die fortbestehende Empfängerberechtigung jedes Gläubigers zu prüfen. Eine Nachtragsverteilung darf nicht allein deshalb angenommen werden, weil die Zahlung nach Aufhebung einging. Die Entscheidung des Bundesgerichtshofs vom 26. September 2024, IX ZB 5/24, bestätigt für ihren Fall, dass eine Steuererstattung trotz Restschuldbefreiung Gegenstand einer Nachtragsverteilung sein kann; sie ersetzt die konkrete Prüfung der Massezugehörigkeit nicht.")
    heading(doc, "3", "Arbeitsrechnung")
    table(doc, ["Rechengröße", "Betrag"], [["Zufluss", eur("3180")], ["Vorerst geschätzte Kosten", eur("0")], ["Vorläufige Teilungsmasse", eur("3180")], ["Bisherige Forderungsbasis", eur("509842")]])
    para(doc, "Die Arbeitsquote beträgt vor Kosten 0,623722 Prozent. Der Zahlungslauf wird erst nach gerichtlicher Anordnung, aktueller Gläubigerprüfung und namentlicher Freigabe erstellt.")
    save_doc(doc, NORD / "33_nachtragsverteilung_steuerzins_20-10-2024.docx")


def havel_interim() -> None:
    doc = new_doc("Zwischenbericht", "Möbelwerk Havelberg GmbH – AG Stendal 7 IN 41/26")
    letter_head(doc, HAVEL_CASE, "31. Oktober 2026", "Berichtszeitraum 25. Juni bis 31. Oktober 2026")
    heading(doc, "1", "Stand der Verwertung")
    para(doc, "Der Geschäftsbetrieb ist eingestellt. Die Maschinen, die Lackierkabine, die Büro- und IT-Ausstattung sowie die freien Forderungen sind verwertet. Die Havelbank eG erhielt auf ihre festgestellte Forderung von 480.000,00 EUR aus der Sicherheitenverwertung 343.500,00 EUR. Der belegte Ausfall beträgt damit 136.500,00 EUR und nimmt als festgestellte Forderung nach § 38 InsO an der Verteilung teil.")
    heading(doc, "2", "Anspruchsverfolgung")
    table(doc, ["Vorgang", "Nominalwert", "Stand", "Erwarteter freier Zufluss"], [
        ["D&O-Vergleich", eur("115000"), "unterzeichnet und bezahlt", eur("115000")],
        ["Anfechtungsvergleiche", eur("41000"), "vollständig bezahlt", eur("41000")],
        ["Zahlung Tim Brauer", eur("12500"), "im Vergleichspaket abgegolten", eur("0")],
        ["Steuererstattung", eur("14200"), "eingegangen", eur("14200")],
    ])
    heading(doc, "3", "Tabelle")
    para(doc, "Für die spätere Schlussverteilung sind Forderungen nach § 38 InsO von 862.900,00 EUR festgestellt. Die Forderung M. Kordes über 7.800,00 EUR ist vollständig bestritten. Der nachrangige Gesellschafterdarlehensanspruch von 120.000,00 EUR wird gesondert geführt und gehört nicht zur aktuellen Verteilungsbasis.")
    heading(doc, "4", "Rechnungslegung")
    para(doc, "Die bisherige Arbeitsfassung der Schlussrechnung darf nicht verwendet werden, solange gesicherte Durchlaufserlöse und Auskehrungen an die Havelbank nur einseitig erfasst sind. Für die Abschlussfassung werden 343.500,00 EUR sowohl als Sicherheitenzufluss als auch als Auskehrung ausgewiesen. Dadurch bleibt der freie Saldo unverändert, der Geldfluss wird aber vollständig sichtbar.")
    heading(doc, "5", "Nächste Schritte")
    table(doc, ["Schritt", "Zieltermin", "Gate"], [
        ["Konten und Belege einschließlich Sicherheitenkonto abstimmen", "15.12.2026", "keine Differenz"],
        ["Vergütungs- und Gerichtskostenstand abschließen", "10.01.2027", "nur belegte Beträge"],
        ["Schlussverzeichnis mit Tabelle abgleichen", "15.01.2027", "Forderungsbasis 862.900,00 EUR"],
        ["Schlussbericht freigeben", "20.01.2027", "menschliche Einreichungsfreigabe"],
    ])
    save_doc(doc, HAVEL / "26_zwischenbericht_31-10-2026.docx")


def havel_final_report() -> None:
    claims = [("Furnier Nord GmbH", Decimal("186420")), ("Havelbank eG – Ausfall", Decimal("136500")),
              ("Finanzamt Stendal", Decimal("92340")), ("AOK Sachsen-Anhalt", Decimal("61200")),
              ("Prignitz Forst KG", Decimal("43700")), ("Holzbauer GmbH & Co. KG", Decimal("28100")),
              ("Beschlagwerk Elbe AG", Decimal("19440")), ("Havelstrom GbR", Decimal("48000")),
              ("Arbeitnehmerforderungen", Decimal("236000")), ("Würtl-Leasing GmbH", Decimal("11200"))]
    payouts = allocate(Decimal("289790"), claims)
    doc = new_doc("Schlussbericht und Schlussrechnung", "Möbelwerk Havelberg GmbH – AG Stendal 7 IN 41/26")
    letter_head(doc, HAVEL_CASE, "20. Januar 2027", "Abschlussbericht, Schlussrechnung und Verteilungsvorschlag")
    heading(doc, "1", "Verfahren und Abschlussstichtag")
    para(doc, "Die Furnier Nord GmbH stellte am 4. Mai 2026 Insolvenzantrag. Das Amtsgericht Stendal ordnete am 6. Mai 2026 Sicherungsmaßnahmen an und eröffnete das Verfahren am 12. Juni 2026. Der Betrieb wurde zur Fertigstellung zweier Aufträge kurzzeitig fortgeführt und danach stillgelegt. Dieser Bericht bildet den Stand vom 20. Januar 2027 ab.")
    heading(doc, "2", "Betriebsfortführung und Personal")
    para(doc, "Die zeitlich begrenzte Fortführung diente der Fertigstellung der Aufträge Pflegeheim Elbaue und Hotel Speicherstadt. Erlöse und Fortführungskosten sind in der Rechnungslegung getrennt erfasst. Die Insolvenzgeldvorfinanzierung und ihre Rückführung sind durch die Sammelabrechnung belegt. Offene Arbeitnehmeransprüche wurden im Prüfungstermin behandelt und in der Tabelle nach ihrem festgestellten Stand geführt.")
    heading(doc, "3", "Verwertung und Drittrechte")
    table(doc, ["Position", "Bruttozufluss oder Ergebnis", "Behandlung"], [
        ["Maschinen und Sicherungsgut", eur("343500"), "gesondertes Sicherheitenkonto; vollständig an Havelbank ausgekehrt"],
        ["Freie Verwertung und Forderungseinzug", eur("428630"), "freie Masse"],
        ["D&O-Vergleich", eur("115000"), "freie Masse; Vergleich erledigt"],
        ["Anfechtungsvergleiche", eur("41000"), "freie Masse; vollständig bezahlt"],
        ["Steuererstattung", eur("14200"), "eingegangen und gebucht"],
        ["Sonstige freie Zuflüsse", eur("179000"), "Fortführung, Kaution und weitere Positionen"],
    ])
    para(doc, "Die gesicherte Forderung der Havelbank eG wurde zum Abschluss mit 480.000,00 EUR festgestellt. Auf sie wurden 343.500,00 EUR aus dem Sicherungsgut ausgekehrt. Der verbleibende Ausfall von 136.500,00 EUR ist in der Forderungsbasis nach § 38 InsO enthalten. Eine Doppelberücksichtigung findet nicht statt.")
    heading(doc, "4", "Schlussrechnung und Kontenabgleich")
    table(doc, ["Rechenblock", "Einnahmen", "Ausgaben", "Saldo"], [
        ["Freie Massebewegungen", eur("777830"), eur("488040"), eur("289790")],
        ["Sicherheitenkonto Havelbank", eur("343500"), eur("343500"), eur("0")],
        ["Gesamter Geldfluss", eur("1121330"), eur("831540"), eur("289790")],
    ])
    para(doc, "Der rechnerische Endbestand von 289.790,00 EUR stimmt mit dem Massekonto überein. Das Sicherheitenkonto weist nach der Auskehrung 0,00 EUR aus. Interne Umbuchungen wurden neutralisiert. Die frühere Arbeitsfassung, die den Sicherheitenfluss nur im erläuternden Text führte, ist durch diese vollständige Geldflussdarstellung ersetzt.")
    heading(doc, "5", "Forderungen und Verteilungsbasis")
    para(doc, "Die festgestellten Forderungen nach § 38 InsO betragen 862.900,00 EUR. Der vollständig bestrittene Anspruch M. Kordes ist mangels fristgerechten Nachweises nicht in die Verteilungsbasis aufgenommen. Die nachrangige Forderung Tim Brauer über 120.000,00 EUR erhält keine Zahlung.")
    table(doc, ["Gläubiger", "Verteilungsforderung", "Auszahlung"], [[n, eur(a), eur(p)] for n, a, p in payouts] + [["Summe", eur("862900"), eur("289790")]])
    quota = Decimal("289790") / Decimal("862900") * Decimal("100")
    para(doc, f"Die ungerundete Quote beträgt {str(quota.quantize(Decimal('0.000001'))).replace('.', ',')} Prozent. Die Auszahlungen werden auf Cent abgerundet; sieben Restcent werden nach den größten Bruchteilsresten zugeteilt. Eine pauschale Reserve von 130.012,68 EUR wird nicht gebildet, weil dafür weder eine offene Masseverbindlichkeit noch ein anderer konkreter Rechtsgrund belegt ist.")
    heading(doc, "6", "Offene Restvorgänge und Nachtragsverteilung")
    para(doc, "Die Veranlagungen sind nach dem Aktenstand abgeschlossen. Ein lediglich möglicher künftiger Steuer- oder Versicherungszufluss wird nicht als vorhandene Masse gebucht und rechtfertigt keinen pauschalen Rückbehalt. Sollte nach der Aufhebung ein weiterer Massegegenstand ermittelt oder ein bereits ausgekehrter Betrag zurückfließen, werden Massezugehörigkeit und die Voraussetzungen der §§ 203 bis 205 InsO gesondert geprüft.")
    heading(doc, "7", "Abschlussreife")
    para(doc, "Die bekannten verwertbaren Massegegenstände sind realisiert. Die Konten stimmen mit der Schlussrechnung überein. Die Forderungsbasis ist mit der Tabelle abgeglichen. Die Abschlussreife wird daher bejaht. Der Bundesgerichtshof hat mit Beschluss vom 11. November 2021, IX ZB 19/20, Randnummern 12 und 14 bis 21, für die dortige Vergütungsfrage hervorgehoben, dass eine bloße Schlussrechnung oder ein Schlusstermin bei fortdauernder Verwertung keinen Abschluss ersetzt. Hier sind nach dem belegten Aktenstand keine weiteren Verwertungsschritte offen; die Entscheidung wird nicht als allgemeine Freigabefiktion verwendet.")
    heading(doc, "8", "Anträge und Freigabegrenze")
    para(doc, "Es wird beantragt, die Schlussrechnung zu prüfen, der Schlussverteilung nach § 196 Absatz 2 InsO zuzustimmen und den Schlusstermin nach § 197 InsO zu bestimmen. Der Bericht bestätigt keine noch nicht ausgeführte Zahlung. Einreichung, Zahlung und Schlussmitteilung bedürfen jeweils einer gesondert dokumentierten menschlichen Freigabe.")
    para(doc, "Dr. Nora Westphal\nRechtsanwältin und Insolvenzverwalterin")
    for name in ("17_schlussbericht_schlussrechnung.docx", "17_schlussbericht.docx"):
        save_doc(doc, HAVEL / name)


def havel_closing_docs() -> None:
    claims = [("Furnier Nord GmbH", Decimal("186420")), ("Havelbank eG – Ausfall", Decimal("136500")),
              ("Finanzamt Stendal", Decimal("92340")), ("AOK Sachsen-Anhalt", Decimal("61200")),
              ("Prignitz Forst KG", Decimal("43700")), ("Holzbauer GmbH & Co. KG", Decimal("28100")),
              ("Beschlagwerk Elbe AG", Decimal("19440")), ("Havelstrom GbR", Decimal("48000")),
              ("Arbeitnehmerforderungen", Decimal("236000")), ("Würtl-Leasing GmbH", Decimal("11200"))]
    payouts = allocate(Decimal("289790"), claims)

    doc = new_doc("Prüfvermerk zur Abschlussreife", "Möbelwerk Havelberg GmbH – Stand 15. Januar 2027")
    letter_head(doc, HAVEL_CASE, "15. Januar 2027", "Konten-, Tabellen- und Verwertungsgate")
    heading(doc, "1", "Konten")
    table(doc, ["Prüfung", "Buchwert", "Fremdnachweis", "Differenz"], [
        ["Massekonto", eur("289790"), eur("289790"), eur("0")],
        ["Sicherheitenkonto", eur("0"), eur("0"), eur("0")],
        ["Barkasse", eur("0"), eur("0"), eur("0")],
    ])
    heading(doc, "2", "Verwertung")
    para(doc, "Alle im Masseverzeichnis geführten Vermögensgegenstände sind als verwertet, aus rechtlichem Grund freigegeben oder ohne realisierbaren Wert ausgebucht. Für jede Ausbuchung liegt ein Einzelvermerk vor. Es bestehen keine laufenden Prozesse und keine unbehandelten Kaufpreisraten.")
    heading(doc, "3", "Tabelle und Quote")
    para(doc, "Die gerichtliche Tabelle weist 862.900,00 EUR festgestellte Forderungen nach § 38 InsO aus. Die Teilungsmasse beträgt 289.790,00 EUR. Die ungerundete Quote beträgt 33,5832657318 Prozent. Die centgenaue Auszahlungsdatei summiert sich auf 289.790,00 EUR.")
    heading(doc, "4", "Gate-Entscheidung")
    table(doc, ["Gate", "Ergebnis", "Freigabe"], [
        ["Abschluss der Verwertung", "bestanden", "Dr. Nora Westphal"],
        ["Kontenabgleich", "bestanden", "Sana Yildiz und Dr. Nora Westphal"],
        ["Tabellenabgleich", "bestanden", "Dr. Nora Westphal"],
        ["Einreichung", "freigegeben", "Dr. Nora Westphal, 20.01.2027"],
        ["Auszahlung", "noch gesperrt", "gerichtliche Zustimmung fehlt"],
    ])
    save_doc(doc, HAVEL / "27_abschlussreife_sachstandsnotiz_15-01-2027.docx")

    doc = new_doc("Schlussverzeichnis", "Möbelwerk Havelberg GmbH – Stand 20. Januar 2027")
    letter_head(doc, HAVEL_CASE, "20. Januar 2027", "Verzeichnis nach §§ 188 bis 193 InsO")
    heading(doc, "1", "Verteilungsdaten")
    para(doc, "Die Teilungsmasse beträgt 289.790,00 EUR. Die festgestellten Forderungen nach § 38 InsO betragen 862.900,00 EUR. Die Ausfallforderung der Havelbank eG von 136.500,00 EUR ist erst nach Abzug der gesicherten Befriedigung von 343.500,00 EUR ermittelt.")
    heading(doc, "2", "Verzeichnis")
    table(doc, ["Nummer und Gläubiger", "Forderung", "Auszahlung", "Status"],
          [[f"{i}. {n}", eur(a), eur(p), "festgestellt; Auszahlung gesperrt bis Freigabe"] for i, (n, a, p) in enumerate(payouts, 1)] +
          [["Summe", eur("862900"), eur("289790"), "Kontrollsumme stimmt"]])
    heading(doc, "3", "Nicht einbezogene Ansprüche")
    para(doc, "Die Forderung M. Kordes über 7.800,00 EUR ist vollständig bestritten und ohne fristgerechten Nachweis. Die Forderung Tim Brauer über 120.000,00 EUR ist nachrangig. Beide Positionen bleiben in der Akte sichtbar, sind aber nicht Teil der aktuellen Verteilungsbasis.")
    save_doc(doc, HAVEL / "28_schlussverzeichnis_20-01-2027.docx")

    doc = new_doc("Interner Freigabevermerk", "Möbelwerk Havelberg GmbH – Abschlussprodukte")
    letter_head(doc, HAVEL_CASE, "23. Januar 2027", "Einreichungsfreigabe")
    heading(doc, "1", "Führende Fassungen")
    table(doc, ["Produkt", "Stand", "Prüfergebnis"], [
        ["Schlussbericht und Schlussrechnung", "20.01.2027", "freigegeben"],
        ["Schlussverzeichnis", "20.01.2027", "862.900,00 EUR Forderungen; 289.790,00 EUR Auszahlung"],
        ["Kontrollarbeitsmappe", "20.01.2027", "Kontendifferenz 0,00 EUR"],
    ])
    heading(doc, "2", "Freigabe")
    para(doc, "Dr. Nora Westphal gibt die Einreichung der bezeichneten Fassungen frei. Die Freigabe umfasst weder die Veröffentlichung gerichtlicher Bekanntmachungen noch den Zahlungslauf. Die Auszahlung bleibt bis zur gerichtlichen Zustimmung und einer erneuten namentlichen Freigabe gesperrt.")
    save_doc(doc, HAVEL / "29_freigabevermerk_abschluss_23-01-2027.docx")

    doc = new_doc("Gerichtliche Verfügung zur Schlussverteilung", "Synthetisches Aktenstück – AG Stendal 7 IN 41/26")
    letter_head(doc, HAVEL_CASE, "29. Januar 2027", "Zustimmung und Bestimmung des Schlusstermins")
    heading(doc, "1", "Zustimmung")
    para(doc, "Nach Prüfung der eingereichten Schlussrechnung wird der Schlussverteilung gemäß § 196 Absatz 2 InsO zugestimmt. Der Verwalterin bleibt aufgegeben, Änderungen der Tabelle und fristgerechte Nachweise vor dem Zahlungslauf zu berücksichtigen.")
    heading(doc, "2", "Schlusstermin")
    para(doc, "Der Schlusstermin wird auf den 15. Februar 2027 bestimmt. Der Bericht, die Schlussrechnung und das Schlussverzeichnis werden entsprechend den gesetzlichen Vorgaben zugänglich gemacht. Die öffentliche Bekanntmachung erfolgt gesondert.")
    heading(doc, "3", "Nachweis")
    para(doc, "Nach dem Zahlungslauf sind die Auszahlungsdatei, die Bankbestätigung und die Erklärung über die vollständige Ausführung vorzulegen. Die Aufhebung des Verfahrens wird erst nach diesem Nachweis geprüft.")
    save_doc(doc, HAVEL / "30_verfuegung_schlussverteilung_29-01-2027.docx")

    doc = new_doc("Vollzugsprotokoll der Schlussverteilung", "Möbelwerk Havelberg GmbH – Zahlungslauf 10. März 2027")
    letter_head(doc, HAVEL_CASE, "12. März 2027", "Freigabe, Auszahlung und Rückläuferkontrolle")
    heading(doc, "1", "Zahlungsfreigabe")
    para(doc, "Nach dem Schlusstermin wurden die gerichtliche Tabelle, das Schlussverzeichnis und die Kontodaten erneut abgeglichen. Dr. Nora Westphal gab den Zahlungslauf am 10. März 2027 um 08:45 Uhr frei. Die technische Datei wurde durch die Sachbearbeitung erstellt und vor Bankübertragung unverändert gegen die freigegebene Summenliste geprüft.")
    heading(doc, "2", "Auszahlungen")
    table(doc, ["Gläubiger", "Auszahlung", "Status"], [[n, eur(p), "ausgeführt; kein Rückläufer"] for n, _, p in payouts] + [["Summe", eur("289790"), "vollständig ausgekehrt"]])
    heading(doc, "3", "Kontenabschluss")
    para(doc, "Der Kontoauszug vom 11. März 2027 weist die Sammelüberweisungen aus. Rückläufer sind bis zum Kontrollzeitpunkt 12. März 2027 nicht eingetreten. Das für die Schlussverteilung bestimmte Guthaben ist vollständig ausgekehrt. Das Sicherheitenkonto war bereits zuvor auf 0,00 EUR abgeschlossen.")
    save_doc(doc, HAVEL / "31_vollzugsprotokoll_schlussverteilung_12-03-2027.docx")

    doc = new_doc("Schlussmitteilung", "Möbelwerk Havelberg GmbH – AG Stendal 7 IN 41/26")
    letter_head(doc, HAVEL_CASE, "12. März 2027", "Vollzug der Schlussverteilung")
    heading(doc, "1", "Mitteilung")
    para(doc, "Die Schlussverteilung ist vollständig vollzogen. Auf festgestellte Forderungen nach § 38 InsO von 862.900,00 EUR wurden insgesamt 289.790,00 EUR ausgekehrt. Die Auszahlungssumme stimmt mit dem Schlussverzeichnis und dem Massekonto überein.")
    heading(doc, "2", "Anregung")
    para(doc, "Es wird angeregt, das Verfahren gemäß § 200 InsO aufzuheben. Ein möglicher, derzeit nicht bestehender späterer Massezufluss ist nicht Bestandteil dieser Mitteilung und wäre gegebenenfalls in einem gesonderten Verfahren nach den §§ 203 bis 205 InsO zu prüfen.")
    save_doc(doc, HAVEL / "32_schlussmitteilung_12-03-2027.docx")

    doc = new_doc("Prüfvermerk zu einer möglichen Nachtragsverteilung", "Möbelwerk Havelberg GmbH – Übungszweig")
    letter_head(doc, HAVEL_CASE, "30. September 2027", "Später Hinweis auf mögliche Versicherungsprämienerstattung")
    heading(doc, "1", "Hinweis")
    para(doc, "Der frühere Versicherungsmakler teilte mit, dass aus der vorzeitigen Vertragsbeendigung möglicherweise eine Prämienerstattung entstehen könne. Ein Bescheid, eine Abrechnung oder ein Zahlungseingang liegt nicht vor. Der Hinweis wird daher nicht als Massezufluss gebucht.")
    heading(doc, "2", "Prüfauftrag")
    para(doc, "Zu klären sind Anspruchsinhaberin, Vertragszeitraum, Abrechnungsgrund, Betrag, Massezugehörigkeit und Verfügbarkeit. Erst ein belegter Massegegenstand kann Anlass für einen Antrag nach § 203 InsO sein. Der Bundesgerichtshof hat mit Beschluss vom 25. September 2025, IX ZB 13/25, Randnummern 7 bis 16 und 20 bis 22, entschieden, dass auch bekannte, irrtümlich oder tatsächlich nicht verwertete Massegegenstände Gegenstand einer Nachtragsverteilung sein können. Die Entscheidung ersetzt weder den Anspruchsnachweis noch die Prüfung der Massezugehörigkeit.")
    heading(doc, "3", "Gate")
    table(doc, ["Prüffeld", "Status", "Folge"], [
        ["Anspruchsnachweis", "offen", "Unterlagen anfordern"],
        ["Zahlungseingang", "nicht vorhanden", "keine Buchung"],
        ["Massezugehörigkeit", "offen", "rechtliche Prüfung"],
        ["Gerichtlicher Antrag", "gesperrt", "erst nach positivem Nachweis"],
    ])
    save_doc(doc, HAVEL / "33_nachtragsverteilung_sachstandsnotiz_30-09-2027.docx")


def workbook(path: Path, case: str, cash: Decimal, claims: list[tuple[str, Decimal]], incomes: list[tuple[str, Decimal]], expenses: list[tuple[str, Decimal]], extra_sheets: list[tuple[str, list[list[object]]]]) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Cockpit"
    ws.append(["Abschlusskontrolle", case])
    ws.append(["Stichtag", "15.03.2024" if "Nordlicht" in case else "20.01.2027"])
    ws.append(["Teilungsmasse", float(cash)])
    ws.append(["Forderungsbasis", float(sum(v for _, v in claims))])
    ws.append(["Quote", "=B3/B4"])
    ws.append(["Auszahlung laut Verzeichnis", f"=SUM(Schlussverzeichnis!D2:D{len(claims) + 1})"])
    ws.append(["Differenz Teilungsmasse", "=B3-B6"])
    ws.append(["Kontrollstatus", '=IF(ABS(B7)<0.005,"OK","SPERRE")'])
    ws.append([])
    ws.append(["Freigaberegel", "Einreichung, Veröffentlichung und Auszahlung benötigen getrennte menschliche Freigaben."])

    for title, values in (("Einnahmen", incomes), ("Ausgaben", expenses)):
        sh = wb.create_sheet(title)
        sh.append(["Position", "Betrag EUR", "Belegstatus", "Prüfvermerk"])
        for name, amount in values:
            sh.append([name, float(amount), "belegt", "mit Journal abgestimmt"])
        sh.append(["Summe", f"=SUM(B2:B{sh.max_row})", "", ""])

    sh = wb.create_sheet("Schlussverzeichnis")
    sh.append(["Gläubiger", "Festgestellt EUR", "Quote", "Auszahlung EUR", "Status"])
    allocated = allocate(cash, claims)
    for index, (name, amount, payout) in enumerate(allocated, 2):
        sh.append([name, float(amount), "=Cockpit!$B$5", float(payout), "zahlbar nach Freigabe"])
    sh.append(["Summe", f"=SUM(B2:B{sh.max_row})", "", f"=SUM(D2:D{sh.max_row})", "Kontrollsumme"])

    gates = wb.create_sheet("Freigaben")
    gates.append(["Gate", "Voraussetzung", "Status", "Freigebende Person", "Datum"])
    for row in [
        ["Kontenabgleich", "Differenz 0,00 EUR", "bestanden", "", ""],
        ["Tabellenabgleich", "Forderungsbasis bestätigt", "bestanden", "", ""],
        ["Einreichung", "Führende Fassungen geprüft", "freigegeben", "", ""],
        ["Auszahlung", "Gerichtliche Zustimmung und Empfängerkontrolle", "gesperrt bis gesonderter Freigabe", "", ""],
        ["Schlussmitteilung", "Zahlung und Rückläuferkontrolle belegt", "gesperrt bis Vollzug", "", ""],
    ]:
        gates.append(row)

    for title, rows in extra_sheets:
        sh = wb.create_sheet(title)
        for row in rows:
            sh.append(row)

    for sh in wb.worksheets:
        sh.freeze_panes = "A2"
        sh.auto_filter.ref = sh.dimensions
        for cell in sh[1]:
            cell.font = Font(name="Times New Roman", size=11, bold=True, color="FFFFFF")
            cell.fill = PatternFill("solid", fgColor=BLUE)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
        for row in sh.iter_rows(min_row=2):
            for cell in row:
                cell.font = Font(name="Times New Roman", size=11)
                cell.alignment = Alignment(wrap_text=True, vertical="top")
                cell.border = Border(bottom=Side(style="hair", color="D9D9D9"))
                if isinstance(cell.value, (int, float)) or (isinstance(cell.value, str) and cell.value.startswith("=")):
                    if sh.title == "Schlussverzeichnis" and cell.column == 3:
                        cell.number_format = '0.000000%'
                    else:
                        cell.number_format = '#,##0.00 [$EUR-407]'
        for col in range(1, sh.max_column + 1):
            width = min(52, max(12, max(len(str(sh.cell(row, col).value or "")) for row in range(1, sh.max_row + 1)) + 2))
            if any(isinstance(sh.cell(row, col).value, (int, float)) or (isinstance(sh.cell(row, col).value, str) and sh.cell(row, col).value.startswith("=")) for row in range(2, sh.max_row + 1)):
                width = max(width, 22)
            sh.column_dimensions[get_column_letter(col)].width = width
        sh.sheet_view.showGridLines = False
        sh.print_title_rows = "1:1"
        sh.page_setup.orientation = "landscape" if sh.max_column > 4 else "portrait"
        sh.page_setup.paperSize = sh.PAPERSIZE_A4
        sh.page_setup.fitToWidth = 1
        sh.sheet_properties.pageSetUpPr.fitToPage = True
    ws["B3"].number_format = '#,##0.00 [$EUR-407]'
    ws["B4"].number_format = '#,##0.00 [$EUR-407]'
    ws["B5"].number_format = '0.000000%'
    ws["B6"].number_format = '#,##0.00 [$EUR-407]'
    ws["B7"].number_format = '#,##0.00 [$EUR-407]'
    path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(path)


def build_workbooks() -> None:
    nord_claims = [("Kieler Volksbank eG", Decimal("214302")), ("Fashion Forward KG", Decimal("23960")),
                   ("DAK-Gesundheit", Decimal("12320")), ("IKK Nord", Decimal("9610")),
                   ("Bundesagentur für Arbeit", Decimal("84220")), ("Übrige Gläubiger", Decimal("165430"))]
    workbook(NORD / "28_schlussrechnung_kontenabstimmung_15-03-2024.xlsx", "Nordlicht Handels GmbH", Decimal("120462"), nord_claims,
             [("Anfangsbestand und Verwertung", Decimal("195580")), ("Forderungseinzug", Decimal("18420")),
              ("Haftungs- und Anfechtungserlöse", Decimal("69260")), ("Steuererstattung", Decimal("18420")),
              ("Zinsen und sonstige Einnahmen", Decimal("5084"))],
             [("Stilllegung und Personal", Decimal("38420")), ("Lager und Logistik", Decimal("18420")),
              ("Versicherungen, Steuern und Verbrauch", Decimal("14840")), ("Rechts- und Gutachterkosten", Decimal("36460")),
              ("Gerichts- und Verfahrenskosten", Decimal("7420")), ("Verwaltervergütung", Decimal("48420")),
              ("Sonstige Ausgaben", Decimal("4220"))],
             [("Nachtrag", [["Prüffeld", "Status", "Betrag EUR", "Nächster Schritt"], ["Steuerzins 2024", "eingegangen nach Aufhebung", 3180.00, "Massezugehörigkeit und gerichtliche Anordnung prüfen"]])])

    havel_claims = [("Furnier Nord GmbH", Decimal("186420")), ("Havelbank eG – Ausfall", Decimal("136500")),
                    ("Finanzamt Stendal", Decimal("92340")), ("AOK Sachsen-Anhalt", Decimal("61200")),
                    ("Prignitz Forst KG", Decimal("43700")), ("Holzbauer GmbH & Co. KG", Decimal("28100")),
                    ("Beschlagwerk Elbe AG", Decimal("19440")), ("Havelstrom GbR", Decimal("48000")),
                    ("Arbeitnehmerforderungen", Decimal("236000")), ("Würtl-Leasing GmbH", Decimal("11200"))]
    workbook(HAVEL / "34_abschlusskontrolle_schlussrechnung_20-01-2027.xlsx", "Möbelwerk Havelberg GmbH", Decimal("289790"), havel_claims,
             [("Freie Massezuflüsse", Decimal("777830")), ("Sicherheitenzuflüsse Havelbank", Decimal("343500"))],
             [("Freie Masseausgaben", Decimal("488040")), ("Auskehrung Sicherheiten Havelbank", Decimal("343500"))],
             [("Absonderung", [["Gläubiger", "Festgestellte Gesamtforderung", "Gesicherte Auszahlung", "Ausfall § 38"], ["Havelbank eG", 480000.00, 343500.00, 136500.00]]),
              ("Nachtrag", [["Prüffeld", "Status", "Betrag EUR", "Nächster Schritt"], ["Versicherungsprämie", "nur Hinweis", "", "Unterlagen anfordern; keine Buchung"]])])


def write_eml(path: Path, sender: str, recipient: str, subject: str, date: str, body: str) -> None:
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg["Date"] = date
    msg["Message-ID"] = f"<{path.stem}@testakte.example>"
    msg.set_content(body)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(msg.as_bytes())


def build_emails() -> None:
    write_eml(NORD / "eml" / "07_gericht_rueckfrage_schlussrechnung.eml", "insolvenzgericht.kiel@testakte.example", "kanzlei.hartmann@testakte.example", "10 IN 127/13 – Rückfrage zur Steuererstattung und Schlussrechnung", "Wed, 20 Mar 2024 10:18:00 +0100", "Sehr geehrter Herr Dr. Hartmann,\n\nbitte bestätigen Sie, ob der am 28. Juni 2023 eingegangene Betrag von 18.420,00 EUR vollständig in der vorgelegten Schlussrechnung und in der Teilungsmasse enthalten ist. Bitte erläutern Sie ferner die in einer älteren Arbeitsfassung verwendete Bezeichnung Nachtragsverteilung.\n\nMit freundlichen Grüßen\nAmtsgericht Kiel – Insolvenzabteilung\n")
    write_eml(NORD / "eml" / "08_antwort_steuererstattung_und_begriff.eml", "kanzlei.hartmann@testakte.example", "insolvenzgericht.kiel@testakte.example", "AW: 10 IN 127/13 – Steuererstattung und Schlussrechnung", "Wed, 20 Mar 2024 15:42:00 +0100", "Sehr geehrte Damen und Herren,\n\nder Betrag von 18.420,00 EUR ist als Einnahme in der Schlussrechnung enthalten und Bestandteil der Teilungsmasse von 120.462,00 EUR. Die Bezeichnung Nachtragsverteilung in der früheren Arbeitsfassung war unzutreffend, weil das Verfahren noch nicht aufgehoben war. Die führende Fassung vom 15. März 2024 bezeichnet den Vorgang als späten Massezufluss.\n\nMit freundlichen Grüßen\nDr. Jens-Peter Hartmann\n")
    write_eml(NORD / "eml" / "09_bank_bestaetigung_zahlungslauf.eml", "insolvenzservice@kieler-volksbank.testakte.example", "m.clausen@hartmann.testakte.example", "Nordlicht Handels GmbH – Ausführung Sammelüberweisung", "Tue, 23 Apr 2024 09:12:00 +0200", "Guten Morgen Frau Clausen,\n\ndie gestern freigegebene Sammelüberweisung über insgesamt 120.462,00 EUR wurde vollständig ausgeführt. Bis heute 09:00 Uhr liegt kein Rückläufer vor. Den Kontoauszug finden Sie im elektronischen Postfach.\n\nFreundliche Grüße\nKieler Volksbank eG\n")

    write_eml(HAVEL / "eml" / "26_rueckfrage_gericht_sicherheitenfluss.eml", "insolvenzgericht.stendal@testakte.example", "kanzlei.westphal@testakte.example", "7 IN 41/26 – Darstellung des Sicherheitenkontos", "Mon, 25 Jan 2027 11:02:00 +0100", "Sehr geehrte Frau Dr. Westphal,\n\nbitte reichen Sie eine Kontenabstimmung ein, aus der der Zufluss und die Auskehrung von 343.500,00 EUR an die Havelbank eG getrennt von der freien Masse hervorgehen. Der bisherige Erläuterungstext genügt für den Geldflussabgleich nicht.\n\nMit freundlichen Grüßen\nAmtsgericht Stendal – Insolvenzgericht\n")
    write_eml(HAVEL / "eml" / "27_antwort_sicherheitenkonto.eml", "kanzlei.westphal@testakte.example", "insolvenzgericht.stendal@testakte.example", "AW: 7 IN 41/26 – Sicherheitenkonto", "Tue, 26 Jan 2027 14:35:00 +0100", "Sehr geehrte Damen und Herren,\n\ndie beigefügte Kontrollarbeitsmappe weist 343.500,00 EUR als Zugang und als Auskehrung auf dem Sicherheitenkonto aus. Der Saldo beträgt 0,00 EUR. Die freie Teilungsmasse bleibt mit 289.790,00 EUR unverändert. Die Ausfallforderung der Havelbank beträgt bei einer Gesamtforderung von 480.000,00 EUR folgerichtig 136.500,00 EUR.\n\nMit freundlichen Grüßen\nDr. Nora Westphal\n")
    write_eml(HAVEL / "eml" / "28_bank_bestaetigung_schlussverteilung.eml", "firmenkunden@havelbank.testakte.example", "sana.yildiz@westphal.testakte.example", "Möbelwerk Havelberg – Zahlungslauf 10.03.2027", "Thu, 11 Mar 2027 10:21:00 +0100", "Sehr geehrte Frau Yildiz,\n\nder freigegebene Zahlungslauf über 289.790,00 EUR wurde vollständig ausgeführt. Die Gesamtsumme stimmt mit der übermittelten Kontrollsumme überein. Rückläufer sind bis heute nicht eingegangen.\n\nMit freundlichen Grüßen\nHavelbank eG\n")


def update_havel_csv() -> None:
    claims = [("Furnier Nord GmbH", Decimal("186420")), ("Havelbank eG (Ausfallforderung)", Decimal("136500")),
              ("Finanzamt Stendal", Decimal("92340")), ("AOK Sachsen-Anhalt", Decimal("61200")),
              ("Prignitz Forst KG", Decimal("43700")), ("Holzbauer GmbH und Co KG", Decimal("28100")),
              ("Beschlagwerk Elbe AG", Decimal("19440")), ("Havelstrom GbR", Decimal("48000")),
              ("Arbeitnehmer gesamt (38 Personen)", Decimal("236000")), ("Wuertl-Leasing GmbH", Decimal("11200"))]
    payouts = allocate(Decimal("289790"), claims)
    path = HAVEL / "18_verteilungsvorschlag.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["rang_insO", "lfd_nr", "glaeubiger", "festgestellt_eur", "absonderung_vorab_eur", "netto_teilnahme_eur", "quote_pct_ungerundet", "auszahlung_eur", "zahlungsdatum", "bemerkung"])
        writer.writerow(["§ 50 InsO (Absonderung)", 0, "Havelbank eG", "480000.00", "343500.00", "136500.00", "", "343500.00", "2026-09-01", "Sicherheitenzahlung; Ausfall separat in § 38-Basis"])
        quote = Decimal("289790") / Decimal("862900") * Decimal("100")
        for index, (name, amount, payout) in enumerate(payouts, 1):
            writer.writerow(["§ 38 InsO", index, name, f"{amount:.2f}", "0.00", f"{amount:.2f}", f"{quote:.10f}", f"{payout:.2f}", "2027-03-10", "Schlussverteilung; centgenauer Restausgleich"])
        writer.writerow(["§ 38 InsO", 11, "M. Kordes", "0.00", "0.00", "0.00", "0.0000000000", "0.00", "", "Vollständig bestritten; kein fristgerechter Nachweis"])
        writer.writerow(["§ 39 Abs. 1 Nr. 5 InsO", 12, "Tim Brauer", "120000.00", "0.00", "120000.00", "0.0000000000", "0.00", "", "Nachrangig; keine verbleibende Masse"])


def update_nord_csv() -> None:
    claims = [("Kieler Volksbank eG", Decimal("214302")), ("Fashion Forward KG", Decimal("23960")),
              ("DAK-Gesundheit", Decimal("12320")), ("IKK Nord", Decimal("9610")),
              ("Bundesagentur für Arbeit", Decimal("84220")),
              ("Übrige Lieferanten und sonstige Gläubiger", Decimal("165430"))]
    payouts = allocate(Decimal("120462"), claims)
    quote = Decimal("120462") / Decimal("509842") * Decimal("100")
    path = NORD / "csv" / "forderungstabelle_auszug.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter=";")
        writer.writerow(["Glaeubiger", "Festgestellt_EUR", "Status", "Quote_Prozent_ungerundet", "Auszahlung_EUR"])
        for name, amount, payout in payouts:
            writer.writerow([name, f"{amount:.2f}", "festgestellt", f"{quote:.10f}", f"{payout:.2f}"])
        writer.writerow(["Summe", "509842.00", "Kontrollsumme", "", "120462.00"])


def main() -> None:
    nord_interim()
    nord_final_report()
    nord_closing_docs()
    havel_interim()
    havel_final_report()
    havel_closing_docs()
    build_workbooks()
    build_emails()
    update_nord_csv()
    update_havel_csv()
    print("Abschlussakten Nordlicht und Havelberg erzeugt.")


if __name__ == "__main__":
    main()
