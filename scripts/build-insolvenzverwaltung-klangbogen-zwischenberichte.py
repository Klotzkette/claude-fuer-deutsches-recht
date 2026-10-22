#!/usr/bin/env python3
"""Baut die fiktive Langzeitakte Klangbogen mit 22 Zwischenberichten."""

from __future__ import annotations

from datetime import date, datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP
from email.message import EmailMessage
from email.policy import SMTP
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import textwrap
import zipfile
from zoneinfo import ZoneInfo

from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle
import yaml


ROOT = Path(__file__).resolve().parents[1]
SLUG = "insolvenzverwaltung-klangbogen-buehnentechnik-bamberg"
CASE = ROOT / "testakten" / SLUG
REPORT_DIR = CASE / "zwischenberichte"
EVIDENCE_DIR = CASE / "belege"
MAIL_DIR = CASE / "korrespondenz"
WORK_DIR = CASE / "arbeitshinweise"
CALC_DIR = CASE / "rechenwerk"
COMBINED_DIR = CASE / "gesamt-pdf"
QUALITY_DIR = ROOT / "quality" / "insolvenzverwaltung-berichtsersteller"
WORKBOOK = CALC_DIR / "95_verfahrensrechnung_und_schlussreife.xlsx"

WORKBOOK_PRINT_AREAS = (
    ("Übersicht", "$A$1:$F$13", None),
    ("Berichtsperioden", "$A$1:$I$26", "$1:$4"),
    ("Kontenjournal", "$A$1:$H$92", "$1:$4"),
    ("Forderungen", "$A$1:$F$30", "$1:$4"),
    ("Belegmatrix", "$A$1:$E$22", "$1:$4"),
    ("Schlussreife", "$A$1:$C$21", "$1:$4"),
)

PLUGIN_VERSION = "1.1.0"
RELEASE_TAG = f"insolvenzverwaltung-berichtsersteller-v{PLUGIN_VERSION}"
COURT = "Amtsgericht Bamberg - Insolvenzgericht"
CASE_NUMBER = "2 T-INS 147/15"
DEBTOR = "Klangbogen Buehnen- und Probenraumtechnik GmbH"
ADMINISTRATOR = "Rechtsanwaeltin Dr. Mechthild Karg"
CASE_WORKER = "Philipp Joens, Wirtschaftsjurist"
OPENING_DATE = date(2015, 11, 22)

REPORT_DATES = (
    date(2016, 5, 28), date(2016, 12, 2), date(2017, 6, 3),
    date(2017, 11, 27), date(2018, 5, 28), date(2018, 12, 7),
    date(2019, 5, 28), date(2019, 11, 25), date(2020, 5, 24),
    date(2020, 11, 20), date(2021, 5, 23), date(2021, 11, 29),
    date(2022, 5, 23), date(2023, 2, 5), date(2023, 11, 5),
    date(2024, 3, 30), date(2024, 5, 28), date(2024, 11, 25),
    date(2025, 5, 18), date(2025, 11, 8), date(2026, 6, 5),
    date(2026, 11, 28),
)

# Die Seitenzahlen bilden 22 vollstaendige, bewusst schlichte Berichtspakete.
REPORT_PAGES = (9, 8, 9, 9, 8, 10, 11, 10, 9, 8, 8, 8, 51, 8, 9, 9, 9, 9, 9, 9, 8, 5)
REPORT_13_ANNEX_PAGES = 42

CLOSING_BALANCES = tuple(map(Decimal, (
    "184932.17", "248615.80", "289440.55", "274902.41", "311754.18",
    "329008.92", "342660.31", "337484.27", "371228.96", "384917.52",
    "401088.11", "429556.42", "447231.09", "438771.84", "468420.55",
    "489216.73", "482908.20", "498774.91", "514331.62", "523806.48",
    "531442.71", "538776.34",
)))

EXPENSES = tuple(map(Decimal, (
    "52867.83", "21450.00", "18775.00", "26900.00", "15644.00",
    "18920.00", "17406.00", "21851.00", "15320.00", "17880.00",
    "19450.00", "18250.00", "14960.00", "18770.00", "17330.00",
    "15487.00", "19450.00", "17755.00", "14898.00", "13406.00",
    "11740.00", "9870.00",
)))

RECEIPTS = tuple(
    CLOSING_BALANCES[index]
    - (CLOSING_BALANCES[index - 1] if index else Decimal("0"))
    + EXPENSES[index]
    for index in range(len(REPORT_DATES))
)

REGISTERED_CLAIMS = tuple(map(Decimal, (
    "448120.00", "782450.00", "1103840.00", "1386220.00", "1579450.00",
    "1768630.00", "1892240.00", "1978550.00", "2041760.00", "2114320.00",
    "2186750.00", "2240180.00", "2305470.00", "2331650.00", "2358900.00",
    "2374420.00", "2386190.00", "2397840.00", "2409950.00", "2416740.00",
    "2421820.00", "2421820.00",
)))

ESTABLISHED_CLAIMS = tuple(map(Decimal, (
    "0", "315400.00", "608220.00", "811550.00", "1012380.00", "1134920.00",
    "1258300.00", "1330660.00", "1412800.00", "1494220.00", "1546680.00",
    "1603110.00", "1648950.00", "1674220.00", "1693380.00", "1712450.00",
    "1728110.00", "1740980.00", "1752460.00", "1759910.00", "1764825.62",
    "1764825.62",
)))

RESERVES = (
    ("Verguetung und Auslagen der Insolvenzverwaltung", Decimal("93975.27")),
    ("Gerichtskosten", Decimal("8912.00")),
    ("Steuerberatung und Schlussdeklarationen", Decimal("4980.60")),
    ("Archivierung und datenschutzgerechte Vernichtung", Decimal("6902.00")),
    ("Bank- und Verteilungskosten", Decimal("1147.50")),
    ("Allgemeiner technischer Nachlauf", Decimal("3858.90")),
)
FINAL_CLAIMS = Decimal("1764825.62")
FINAL_CASH = CLOSING_BALANCES[-1]
FINAL_RESERVES = sum((value for _, value in RESERVES), Decimal("0"))
FINAL_DISTRIBUTION = FINAL_CASH - FINAL_RESERVES
FINAL_QUOTA = (FINAL_DISTRIBUTION / FINAL_CLAIMS * Decimal("100")).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)

KAUFPREISVERGLEICH = Decimal("30000.00")
LANDBUEHNE_VERGLEICH = Decimal("35620.59")
D_AND_O_VERGLEICH = Decimal("46763.18")
D_AND_O_RATE_EINS = Decimal("13141.47")
D_AND_O_RATE_ZWEI = Decimal("33621.71")
BERLIN_TIME = ZoneInfo("Europe/Berlin")

RECEIPT_OVERRIDES: dict[int, tuple[tuple[date, str, Decimal], tuple[date, str, Decimal]]] = {
    6: (
        (date(2019, 3, 15), "Kaufpreisvergleich", Decimal("30000.00")),
        (date(2019, 4, 18), "Theater-Schlussrechnungen", Decimal("1057.39")),
    ),
    8: (
        (date(2020, 1, 16), "Sachversicherungsleistung", Decimal("28420.00")),
        (date(2020, 4, 20), "Projektvergleich mit Zinsen", Decimal("20644.69")),
    ),
    10: (
        (date(2021, 1, 15), "Restdebitoren Theaterprojekte", Decimal("24222.00")),
        (date(2021, 4, 22), "Weitere Forderungseinzuege", Decimal("11398.59")),
    ),
    11: (
        (date(2021, 7, 19), "Landbuehne-Vergleich", LANDBUEHNE_VERGLEICH),
        (date(2021, 10, 29), "Weitere Forderungseinzuege", Decimal("11097.72")),
    ),
    14: (
        (date(2023, 4, 12), "Steuererstattung Aenderungsbescheid", Decimal("30454.71")),
        (date(2023, 9, 21), "Erstattung Parallelverfahren", Decimal("16524.00")),
    ),
    16: (
        (date(2024, 4, 17), "D-und-O-Vergleichsrate 1 (Teilbuchung)", Decimal("8936.20")),
        (date(2024, 4, 27), "D-und-O-Vergleichsrate 1 (Restbuchung)", Decimal("4205.27")),
    ),
    17: (
        (date(2024, 6, 15), "D-und-O-Vergleichsrate 2 (Teilbuchung)", Decimal("22862.76")),
        (date(2024, 10, 25), "D-und-O-Vergleichsrate 2 (Restbuchung)", Decimal("10758.95")),
    ),
    18: (
        (date(2025, 1, 16), "Steuerliche Abschlussgutschrift", Decimal("20709.20")),
        (date(2025, 4, 17), "Zinsgutschrift", Decimal("9745.51")),
    ),
    21: (
        (date(2026, 6, 22), "Steuererstattung", Decimal("11698.47")),
        (date(2026, 10, 28), "Zinsgutschrift", Decimal("5505.16")),
    ),
}

EVENTS = (
    {
        "title": "Betriebsstilllegung, Sicherung und erster Kaufpreis",
        "change": "Die Produktion modularer Akustiksegel und die Wartung von Buehnenhubwerken wurden geordnet beendet. Der Erwerber hat den freien ersten Kaufpreisteil gezahlt; die seriennummernbezogene Zuordnung von zwei Hubtischen bleibt offen.",
        "process": "Altdebitoren werden nach Projektakten getrennt eingezogen. Drei Auftraggeber berufen sich auf Gewaehrleistungseinbehalte. Eigentumsvorbehalte der Lieferanten Boehlein Metallbau und Pfrang Antriebstechnik werden belegt und ausgesondert.",
        "open": "Restkaufpreis, Schlussabrechnung der letzten Baustellen, Umsatzsteuerkorrektur und erste Tabellenpruefung.",
        "next": "Vollzug des Asset Deals dokumentieren, Debitorenbelege nachfordern und die naechste Forderungspruefung vorbereiten.",
    },
    {
        "title": "Asset Deal, Personalabschluss und Aussonderung",
        "change": "Der Asset Deal ist im Kern vollzogen. 18 der zuletzt 29 Beschaeftigten wurden vom Erwerber uebernommen. Die Masse hat Restinventar verwertet und die Mietflaeche bis auf das Messlabor geraeumt.",
        "process": "Die Sicherungsglaeubigerin verlangt eine hoehere Auskehrung aus dem Verkauf der CNC-Anlage. Die Verwalterin rechnet Gutachtenwert, Verwertungskosten und Umsatzsteuer getrennt ab. Eine Einigung liegt noch nicht vor.",
        "open": "Sicherheitenabrechnung, Urlaubsabgeltung, zwei Eigentumsvorbehalte und Kaufpreisrate zwei.",
        "next": "Sicherheitenunterlagen abgleichen und die Forderungstabelle nach dem ersten Pruefungstermin fortschreiben.",
    },
    {
        "title": "Restkaufpreis, Altdebitoren und Anfechtungspruefung",
        "change": "Die zweite Kaufpreisrate und mehrere Werklohnforderungen sind eingegangen. Der Erwerber behaelt wegen behaupteter Maengel an einer Theatersteuerung 38.000 EUR ein.",
        "process": "Zahlungen an die fruehere Gesellschafterin Kunigunde Ruckdeschel und an den Geschaeftsfuehrer Hinnerk Bamberger werden anhand der Bankjournaldatei geprueft. Eine Anspruchsanmeldung ist noch nicht erfolgt.",
        "open": "Kaufpreiseinbehalt, vollstaendige Projektdokumentation, Gesellschafterkonto und Umsatzsteuer 2015.",
        "next": "Technischen Maengelbericht einholen und insolvenzspezifische Ansprueche rechtlich und wirtschaftlich bewerten.",
    },
    {
        "title": "Technischer Gewaehrleistungsstreit und Organansprueche",
        "change": "Die Masse hat den Kaufpreiseinbehalt eingeklagt. Das Gericht hat ein Sachverstaendigengutachten zur Steuerung des Hubwerks angeordnet. Die Prozesskosten fuehren voruebergehend zu einem niedrigeren Kontostand.",
        "process": "Gegen den frueheren Geschaeftsfuehrer wird wegen Zahlungen im Krisenzeitraum ermittelt. Die D-und-O-Versicherung hat Deckungsunterlagen angefordert und eine Anerkennung abgelehnt.",
        "open": "Gutachtenvorschuss, D-und-O-Deckung, Liquiditaetsstatus und Prozessvergleichskorridor.",
        "next": "Gutachten begleiten, Zahlungszeitpunkte belegen und Deckungsobliegenheiten fristgerecht beantworten.",
    },
    {
        "title": "Sicherheitenabrechnung und erster Vergleichskorridor",
        "change": "Die Sicherungsglaeubigerin hat die Erloszuordnung im Wesentlichen akzeptiert. Ein kleiner Betrag bleibt wegen eines gemeinsam finanzierten Messsystems streitig.",
        "process": "Im Kaufpreisprozess liegt das schriftliche Gutachten vor. Es bestaetigt einen behebbaren Programmiermangel, verneint aber die behauptete Unbrauchbarkeit der Anlage. Vergleichsgespraeche sind aufgenommen.",
        "open": "Reststreit Sicherheiten, Vergleich Kaufpreisprozess, Vorsteuerkorrektur und Tabellenbestreitungen.",
        "next": "Vergleich nur nach dokumentierter Wirtschaftlichkeitsrechnung abschliessen und Tabellenunterlagen nachfordern.",
    },
    {
        "title": "Steuerliche Aufarbeitung und Vergleichsverhandlung",
        "change": "Die Umsatzsteuerjahreserklaerung 2015 und die Massevoranmeldungen sind abgegeben. Das Finanzamt hat Rueckfragen zur Aufteilung von Werklohn und Softwarepflege gestellt.",
        "process": "Der Erwerber bietet zur Beendigung des Kaufpreisprozesses 24.000,00 EUR. Nach Kosten- und Vollstreckungsvergleich wird ein Mindestbetrag von 30.000,00 EUR vertreten.",
        "open": "Steuerkonten, Vergleichsbetrag, Sicherheitenrest und D-und-O-Auskunft.",
        "next": "Steuerbelege liefern, Vergleichsbeschluss des Glaeubigerausschusses vorbereiten und Deckungsunterlagen vervollstaendigen.",
    },
    {
        "title": "Kaufpreisvergleich und weitere Forderungseinziehung",
        "change": "Der Kaufpreisstreit ist gegen Zahlung von 30.000,00 EUR und Kostenaufhebung beendet worden. Der Betrag ist eingegangen. Die weiteren Einnahmen dieses Berichtszeitraums von 1.057,39 EUR stammen aus teilweise anerkannten Schlussrechnungen zweier kommunaler Theater.",
        "process": "Die Organansprueche werden anhand eines rekonstruierten Dreiwochenstatus vertieft. Der ehemalige Geschaeftsfuehrer bestreitet den Eintritt der Zahlungsunfaehigkeit und verweist auf eine nicht dokumentierte Kreditlinie.",
        "open": "Organhaftung, D-und-O-Deckung, Restdebitoren und Steuerpruefung.",
        "next": "Bankauskunft zur Kreditlinie sichern und die Organanspruchsberechnung mit Belegen abschliessen.",
    },
    {
        "title": "Bankauskunft, Deckungspruefung und Restdebitoren",
        "change": "Die Hausbank hat bestaetigt, dass keine verbindlich zugesagte neue Kreditlinie bestand. Die D-und-O-Versicherung prueft nun Grund und Hoehe, erhebt aber Einwendungen gegen die Anzeigeobliegenheit.",
        "process": "Ein Auftraggeber in Thueringen verrechnet eine behauptete Vertragsstrafe. Die Masse hat der Aufrechnung widersprochen und eine technische Abnahmeakte vorgelegt.",
        "open": "D-und-O-Deckung, Aufrechnung, Steuerpruefung und vier spaete Forderungsanmeldungen.",
        "next": "Deckungsposition beantworten, Aufrechnungsstreit beziffern und die spaeten Anmeldungen terminieren.",
    },
    {
        "title": "Versicherungsleistung und Tabellenfortschreibung",
        "change": "Aus einer Sachversicherung sind 28.420 EUR fuer einen vor Insolvenzeroeffnung eingetretenen Steuerungsschaden eingegangen. Die Forderungstabelle wurde um vier Nachmeldungen ergaenzt.",
        "process": "Der Aufrechnungsstreit mit dem Auftraggeber ist vergleichsweise gegen Zahlung von 20.000,00 EUR zuzueglich 644,69 EUR Zinsen beendet. Der D-und-O-Versicherer verlangt ein externes Gutachten zur Insolvenzreife.",
        "open": "Gutachten Organhaftung, steuerliche Schlusspruefung und verbleibende Tabellenwidersprueche.",
        "next": "Gutachtenauftrag abgrenzen und eine Doppelverwertung von Haftungs- und Versicherungsanspruch verhindern.",
    },
    {
        "title": "Organhaftungsgutachten und steuerliche Zwischenpruefung",
        "change": "Das Gutachten grenzt einen haftungsrelevanten Zahlungszeitraum ein, weist aber auf Gegenpositionen zu hypothetischen Massekosten hin. Eine abschliessende Anspruchshoehe ist noch nicht freigegeben.",
        "process": "Das Finanzamt hat eine Aussenpruefung fuer Werkleistungen mit Softwareanteil angekuendigt. Die Buchhaltung wird aus Sicherungskopien rekonstruiert.",
        "open": "Haftungsbetrag, Deckungsumfang, Betriebspruefung und Buchhaltungsdaten 2014 bis 2016.",
        "next": "Gutachten mit Zahlungsjournal verknuepfen und die Datenanforderung des Finanzamts vollstaendig beantworten.",
    },
    {
        "title": "Haftungsanmeldung und weitere Massezufluesse",
        "change": "Ansprueche gegen Hinnerk Bamberger und die D-und-O-Versicherung sind beziffert und angemeldet. Ohne Anerkennung hat der Versicherer eine Mediation vorgeschlagen. Aus anderen Theaterprojekten gingen 24.222,00 EUR und weitere Forderungseinzuege von 11.398,59 EUR ein; beide Buchungen betreffen nicht das Projekt Landbuehne Nord.",
        "process": "Die Abnahmeunterlagen zur bislang bestrittenen Schlussrate aus dem Projekt Landbuehne Nord liegen nun vollstaendig vor. Die Zahlung ist zum Berichtsstichtag ausstehend; der Vergleich wird vorbereitet. Die Tabelle wurde nach zwei Ruecknahmen bereinigt.",
        "open": "Mediation, Steuerpruefung, eine Rangfrage und die Kostenverteilung aus dem Gutachten.",
        "next": "Mediationsunterlagen mit Anspruchs- und Kostenmatrix vorbereiten und die Rangfrage gerichtlich klaeren lassen.",
    },
    {
        "title": "Mediation, Landbuehne-Vergleich und Steuerkonten",
        "change": "Die erste Mediationsrunde hat keinen Abschluss gebracht. Der Versicherer stellt 85.000 EUR in Aussicht, verlangt aber eine umfassende Erledigung auch gegen den Geschaeftsfuehrer.",
        "process": "Der am 14.07.2021 protokollierte Vergleich im Projekt Landbuehne Nord ist nach dem Zahlungseingang von 35.620,59 EUR am 19.07.2021 vollzogen. Weitere 11.097,72 EUR stammen aus getrennten Forderungseinzuegen. Die steuerliche Aussenpruefung ist inhaltlich fortgeschritten; einzelne Softwarepflegeerloese werden anders periodisiert. Ein Erstattungsanspruch zeichnet sich ab, ist aber noch nicht festgesetzt.",
        "open": "Vergleichsumfang, Freistellung, Steuerfestsetzung und 17 bestrittene Tabellenpositionen.",
        "next": "Vergleichsvarianten mit Nettoerloes rechnen und fuer die Tabellenpositionen einen Sammeltermin vorbereiten.",
    },
    {
        "title": "Tabellenpruefung, Forderungsnachweise und Verfahrensstand",
        "change": "Das Gericht hat einen gebuendelten Nachweis zum damaligen Tabellen-, Prozess-, Steuer- und Kontenstand verlangt. Die Masse legt deshalb exakt 42 Nachweisseiten mit Forderungsblaettern, Korrespondenz, Kontrollgruppen, Prozessregister-, Steuer- und Buchungsnachweisen vor.",
        "process": "Die D-und-O-Mediation bleibt offen. In der Steuerpruefung sind die wesentlichen Sachverhalte geklaert; der Bescheid steht noch aus. Die Schlussreife ist weiterhin nicht erreicht.",
        "open": "Auswertung der 42 Nachweisseiten, Vergleich Organhaftung, Steuerbescheid und drei Zustellanschriften.",
        "next": "Nachweise einzeln zuordnen, Tabellenstatus dokumentieren und keine spaetere Einigung oder Festsetzung vorwegnehmen.",
    },
    {
        "title": "Nachweislauf und aktualisierte Vergleichsrechnung",
        "change": "Die 42 Nachweisseiten sind den jeweiligen Tabellen-, Prozess-, Steuer- und Kontenvorgaengen zugeordnet. Zahlreiche Forderungen wurden reduziert oder zurueckgenommen. Drei Positionen bleiben wegen unklarer Rechtsnachfolge bestritten.",
        "process": "Die D-und-O-Vergleichsrechnung wurde nach Gutachterkosten, Deckungseinwendungen und Vollstreckungsrisiko aktualisiert. Der Ausschuss verlangt vor einer Entscheidung einen belastbaren Nettovergleichskorridor.",
        "open": "Rechtsnachfolge dreier Glaeubiger, Mindestvergleich und Steuerbescheid.",
        "next": "Rechtsnachfolgen belegen, Ausschusszustimmung zu einem Vergleichskorridor einholen und Steuerfestsetzung abwarten.",
    },
    {
        "title": "Unterbrechung des Haftungsprozesses und Steuererstattung",
        "change": "Der Haftungsprozess ist durch die Eroeffnung eines Insolvenzverfahrens ueber das Vermoegen des ehemaligen Geschaeftsfuehrers unterbrochen. Die Masse hat ihre Forderung dort angemeldet.",
        "process": "Ein geaenderter Steuerbescheid fuehrt zu einer am 12.04.2023 eingegangenen Erstattung von 30.454,71 EUR. Hinzu kommt eine Kostenerstattung von 16.524,00 EUR aus dem Parallelverfahren. Der Bescheid wird noch auf Nebenbestimmungen und Rechtsbehelfsrisiken geprueft.",
        "open": "Forderungsfeststellung im Parallelverfahren, D-und-O-Deckung, Bestandskraft Steuerbescheid und Tabellenrest.",
        "next": "Parallelverfahren ueberwachen und die Steuererstattung erst nach Bestandskraft als abschliessend behandeln.",
    },
    {
        "title": "Parallelverfahren und D-und-O-Vergleich",
        "change": "Im Parallelverfahren ist die Forderung vorlaeufig festgestellt. Der D-und-O-Versicherer bietet nach weiterer Mediation 46.763,18 EUR, zahlbar in zwei Raten von 13.141,47 EUR und 33.621,71 EUR.",
        "process": "Der Glaeubigerausschuss verlangt eine Gegenueberstellung von Prozessdauer, Deckungseinwendungen, Eigenleistungsfaehigkeit und Nettovergleichserloes. Die Akte enthaelt noch keine Zustimmung.",
        "open": "Ausschussentscheidung, Ausgestaltung der beiden Vergleichsraten, Bestandskraft des Steuerbescheids und Kostenansatz.",
        "next": "Wirtschaftlichkeitsrechnung vervollstaendigen und den Vergleich erst nach dokumentierter Zustimmung unterzeichnen.",
    },
    {
        "title": "Vergleichszustimmung und erste Rate",
        "change": "Der Glaeubigerausschuss hat dem D-und-O-Vergleich ueber insgesamt 46.763,18 EUR zugestimmt. Die erste Rate von 13.141,47 EUR ist eingegangen. Die zweite Rate von 33.621,71 EUR wird bis Oktober 2024 faellig.",
        "process": "Die Forderung im Parallelverfahren bleibt angemeldet; eine Doppelbefriedigung ist in der Vergleichsvereinbarung ausgeschlossen. Die Tabelle wird bis zur zweiten Rate nicht eingefroren.",
        "open": "Zweite Rate, Kosten des Parallelverfahrens und vier Zustellnachweise.",
        "next": "Zahlungseingang und Freigabeklauseln ueberwachen und Forderungsstatus im Parallelverfahren fortschreiben.",
    },
    {
        "title": "Zweite Vergleichsrate und Abschluss der Aktivprozesse",
        "change": "Die zweite Vergleichsrate von 33.621,71 EUR ist vollstaendig eingegangen. Zusammen mit der ersten Rate sind damit 46.763,18 EUR gezahlt. Mit Wirksamkeit der Erledigungsklauseln sind die Haftungs- und Deckungskomplexe beendet.",
        "process": "Im Parallelverfahren erfolgt wegen der vereinbarten Anrechnung keine weitere Auszahlung an die Masse. Die Anmeldung wird nur noch zum Nachweis der Erledigung fortgeschrieben. Die Prozessakten werden geschlossen; offene Kostenrechnungen werden abgeglichen.",
        "open": "Kostenfestsetzung, letzte Steuererklaerung, Zustellnachweise und Tabellenfreeze.",
        "next": "Kostenkonten schliessen, Steuerdeklarationen einreichen und einen belastbaren Abschlussstichtag bestimmen.",
    },
    {
        "title": "Steuer- und Kostenabschluss sowie Vorbereitung des Tabellenfreeze",
        "change": "Die letzten Masseerklaerungen sind abgegeben. Das Finanzamt hat keine weiteren Unterlagen angefordert. Im Berichtszeitraum sind eine steuerliche Abschlussgutschrift von 20.709,20 EUR und eine Zinsgutschrift von 9.745,51 EUR eingegangen.",
        "process": "Der am 18.09.2024 noch offene Kostenfestsetzungsantrag ueber 1.284,30 EUR wurde durch Beschluss des Landgerichts Bamberg vom 14.01.2025, 2 O 317/17 KfH, zurueckgewiesen. Nach Zustellung am 17.01.2025 wurde kein Rechtsmittel eingelegt; die Fristenkontrolle vom 18.02.2025 schloss den Vorgang ohne Zahlung und ohne Kontenbuchung. Die Forderungstabelle ist bis auf zwei Erbnachweise und eine Ruecknahme bereinigt.",
        "open": "Erbnachweise, Ruecknahme und Archivangebot.",
        "next": "Letzte Nachweise mit Ausschlussfrist anfordern und Schlusskosten belastbar reservieren.",
    },
    {
        "title": "Vorlaeufiger Tabellenstand, Archivierung und Schlusskosten",
        "change": "Der vorlaeufige Tabellenstand weist festgestellte ordentliche Forderungen von 1.759.910,00 EUR aus. Zu einer spaeten Nachmeldung und einer angekuendigten Teilruecknahme fehlen noch abschliessende Nachweise; die Forderungsbasis ist deshalb noch nicht eingefroren.",
        "process": "Archiv- und Vernichtungsangebote liegen vor. Gerichtskosten, Verguetung und steuerlicher Nachlauf werden getrennt reserviert; eine Auszahlung ist noch nicht freigegeben.",
        "open": "Letzter Forderungsnachweis, Teilruecknahme, endgueltige Verguetungsberechnung, Bankbestaetigung und Abstimmung der Schlussrechnung.",
        "next": "Die beiden Tabellenpositionen abschliessend pruefen, erst danach den Tabellenstand einfrieren sowie Bank, Buchhaltung und Berichtssalden abstimmen.",
    },
    {
        "title": "Bankabgleich und letzter Beleglauf",
        "change": "Der letzte Forderungsnachweis und die Teilruecknahme sind verarbeitet. Die ordentlichen Forderungen sind nun mit 1.764.825,62 EUR endgueltig festgestellt und die Forderungsbasis ist eingefroren. Bank und Buchhaltung stimmen bis auf eine zeitlich abgegrenzte Bankgebuehr ueberein; die Gebuehr wurde im Nachlauf verbucht.",
        "process": "Die Schlussrechnungspositionen sind vorbereitet. Der Bericht ist noch ein Zwischenbericht; gerichtliche Zustimmung, Verguetungsfestsetzung und Schlussverteilung werden nicht als vollzogen dargestellt.",
        "open": "Formeller Banknachweis, namentliche Freigabe des Schlussberichts und gerichtliche Kostenrechnung.",
        "next": "Bankbestaetigung beiziehen, Schlussbericht und Schlussrechnung getrennt erstellen und Freigabegate dokumentieren.",
    },
    {
        "title": "Schlussreife und Uebergabe an den Schlussbericht",
        "change": "Saemtliche Vermoegensgegenstaende sind verwertet, Aktivprozesse beendet, Sicherheiten abgerechnet und Steuern geklaert. Der Massebestand betraegt zum Stichtag 538.776,34 EUR.",
        "process": "Die festgestellten ordentlichen Forderungen betragen 1.764.825,62 EUR. Nach den dokumentierten Reserven verbleiben rechnerisch 419.000,07 EUR. Dies entspricht einer vorlaeufigen Quote von 23,741726 Prozent.",
        "open": "Namentliche Freigabe, Verguetungs- und Gerichtskostenfestsetzung, gerichtliche Zustimmung und Auszahlungsvollzug.",
        "next": "Schlussbericht, Schlussrechnung und Schlussverzeichnis aus den fuehrenden Daten erstellen; keine Einreichung oder Zahlung ohne menschliche Freigabe.",
    },
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def euro(value: Decimal) -> str:
    text = f"{value:,.2f}"
    return text.replace(",", "X").replace(".", ",").replace("X", ".") + " EUR"


def de_date(value: date) -> str:
    return value.strftime("%d.%m.%Y")


def register_fonts() -> None:
    directory = Path("/System/Library/Fonts/Supplemental")
    regular = directory / "Times New Roman.ttf"
    bold = directory / "Times New Roman Bold.ttf"
    if not regular.is_file() or not bold.is_file():
        raise RuntimeError("Times New Roman ist fuer den Aktenbau erforderlich")
    pdfmetrics.registerFont(TTFont("Klang-Regular", str(regular)))
    pdfmetrics.registerFont(TTFont("Klang-Bold", str(bold)))
    pdfmetrics.registerFontFamily("Klang-Regular", normal="Klang-Regular", bold="Klang-Bold")


BODY = ParagraphStyle(
    "Body", fontName="Klang-Regular", fontSize=10.7, leading=14.1,
    alignment=TA_JUSTIFY, spaceAfter=7,
)
SMALL = ParagraphStyle(
    "Small", fontName="Klang-Regular", fontSize=8.8, leading=11.1,
    alignment=TA_LEFT, spaceAfter=4,
)
HEADING = ParagraphStyle(
    "Heading", fontName="Klang-Bold", fontSize=12.3, leading=15,
    alignment=TA_LEFT, spaceBefore=8, spaceAfter=5,
)
TITLE = ParagraphStyle(
    "Title", fontName="Klang-Bold", fontSize=16, leading=20,
    alignment=TA_CENTER, spaceAfter=12,
)


def draw_footer(pdf: canvas.Canvas, report_no: int | None, page_no: int, page_total: int, label: str = "") -> None:
    pdf.setStrokeColor(colors.HexColor("#777777"))
    pdf.setLineWidth(0.35)
    pdf.line(23 * mm, 15 * mm, 187 * mm, 15 * mm)
    pdf.setFont("Klang-Regular", 8)
    left = f"{CASE_NUMBER} | {DEBTOR}"
    if report_no is not None:
        left += f" | Zwischenbericht {report_no:02d}"
    elif label:
        left += f" | {label}"
    pdf.drawString(23 * mm, 10 * mm, left)
    pdf.drawRightString(187 * mm, 10 * mm, f"Seite {page_no} von {page_total}")


def draw_header(pdf: canvas.Canvas, heading: str, issuer: str | None = None) -> None:
    pdf.setFont("Klang-Regular", 9)
    pdf.drawString(23 * mm, 284 * mm, issuer or ADMINISTRATOR)
    pdf.drawRightString(187 * mm, 284 * mm, heading)
    pdf.setStrokeColor(colors.HexColor("#777777"))
    pdf.line(23 * mm, 280 * mm, 187 * mm, 280 * mm)


def draw_flow_page(
    pdf: canvas.Canvas,
    heading: str,
    blocks: list[tuple[str, str]],
    report_no: int | None,
    page_no: int,
    page_total: int,
    label: str = "",
    issuer: str | None = None,
) -> None:
    draw_header(pdf, heading, issuer)
    y = 270 * mm
    for block_heading, body in blocks:
        if block_heading:
            paragraph = Paragraph(block_heading, HEADING)
            width, height = paragraph.wrap(164 * mm, y - 23 * mm)
            y -= height
            paragraph.drawOn(pdf, 23 * mm, y)
            y -= 2 * mm
        paragraph = Paragraph(body, BODY)
        width, height = paragraph.wrap(164 * mm, y - 21 * mm)
        if y - height < 21 * mm:
            raise RuntimeError(f"Seiteninhalt laeuft ueber: {heading}, Seite {page_no}")
        y -= height
        paragraph.drawOn(pdf, 23 * mm, y)
        y -= 4 * mm
    draw_footer(pdf, report_no, page_no, page_total, label)
    pdf.showPage()


def report_filename(index: int, report_date: date) -> Path:
    return REPORT_DIR / f"{index:02d}_zwischenbericht_{report_date.isoformat()}.pdf"


def report_period(index: int) -> tuple[date, date]:
    start = OPENING_DATE if index == 0 else REPORT_DATES[index - 1] + timedelta(days=1)
    return start, REPORT_DATES[index]


def period_transactions(index: int) -> list[tuple[date, str, str, Decimal]]:
    """Liefert die vier periodengenauen Journalbewegungen in Buchungstagsfolge."""
    start, end = report_period(index)
    receipts = RECEIPT_OVERRIDES.get(index)
    if receipts is None:
        first_receipt = (RECEIPTS[index] * Decimal("0.68")).quantize(Decimal("0.01"))
        receipts = (
            (start + timedelta(days=17), "Sammelgutschrift", first_receipt),
            (end - timedelta(days=31), "Weitere Gutschriften", RECEIPTS[index] - first_receipt),
        )
    expense_labels = (
        "Rechts- und Gutachterkosten",
        "Massebuero und Bank",
        "Steuerberatung",
        "Archiv und Nachlauf",
    )
    first_expense = (EXPENSES[index] * Decimal("0.61")).quantize(Decimal("0.01"))
    entries = [
        *((booking_date, "E", label, amount) for booking_date, label, amount in receipts),
        (start + timedelta(days=39), "A", expense_labels[index % 4], first_expense),
        (end - timedelta(days=9), "A", expense_labels[(index + 1) % 4], EXPENSES[index] - first_expense),
    ]
    entries.sort(key=lambda entry: (entry[0], entry[1], entry[2]))
    if sum((entry[3] for entry in entries if entry[1] == "E"), Decimal("0")) != RECEIPTS[index]:
        raise RuntimeError(f"Einnahmenjournal Bericht {index + 1:02d} stimmt nicht")
    if sum((entry[3] for entry in entries if entry[1] == "A"), Decimal("0")) != EXPENSES[index]:
        raise RuntimeError(f"Ausgabenjournal Bericht {index + 1:02d} stimmt nicht")
    if any(not (start <= entry[0] <= end) for entry in entries):
        raise RuntimeError(f"Buchung ausserhalb Berichtszeitraum {index + 1:02d}")
    return entries


def report_letter(pdf: canvas.Canvas, index: int, pages: int) -> None:
    report_no = index + 1
    report_date = REPORT_DATES[index]
    pdf.setFont("Klang-Regular", 10)
    pdf.drawString(23 * mm, 276 * mm, "Karg Endres Insolvenzverwaltung PartG mbB")
    pdf.drawString(23 * mm, 270 * mm, "Schuetzenanger 6, 96047 Bamberg")
    pdf.drawString(23 * mm, 258 * mm, COURT)
    pdf.drawString(23 * mm, 252 * mm, "- Insolvenzabteilung -")
    pdf.drawString(23 * mm, 246 * mm, "Justizplatz 7")
    pdf.drawString(23 * mm, 240 * mm, "96047 Bamberg")
    pdf.drawRightString(187 * mm, 228 * mm, f"Bamberg, {de_date(report_date)}")
    pdf.setFont("Klang-Bold", 11)
    pdf.drawString(23 * mm, 216 * mm, f"Insolvenzverfahren ueber das Vermoegen der {DEBTOR}")
    pdf.drawString(23 * mm, 209 * mm, f"Az. {CASE_NUMBER} - turnusmaessiger Zwischenbericht Nr. {report_no:02d}")
    body = (
        f"Sehr geehrte Damen und Herren,\n\n"
        f"in dem vorbezeichneten Verfahren ueberreiche ich den Zwischenbericht Nr. {report_no:02d} "
        f"fuer den Zeitraum vom {de_date(report_period(index)[0])} bis {de_date(report_date)}. "
        f"Der Bericht knuepft an den zuletzt vorgelegten Sachstand an und stellt die im Berichtszeitraum "
        f"eingetretenen Veraenderungen, den aktuellen Massebestand sowie die noch offenen Arbeitsschritte dar.\n\n"
        f"Die Einreichung erfolgt aufgrund der gerichtlichen Berichtsanordnung im Rahmen der Aufsicht nach "
        f"Paragraph 58 InsO. Sie ersetzt weder eine Schlussrechnung nach Paragraph 66 InsO noch eine "
        f"gerichtliche Zustimmung zur Verteilung.\n\n"
        f"Mit freundlichen Gruessen\n\nDr. Mechthild Karg\nInsolvenzverwalterin"
    )
    paragraphs = [p for p in body.split("\n\n") if p]
    y = 193 * mm
    for text in paragraphs:
        p = Paragraph(text, BODY)
        _, h = p.wrap(164 * mm, 100 * mm)
        y -= h
        p.drawOn(pdf, 23 * mm, y)
        y -= 4 * mm
    draw_footer(pdf, report_no, 1, pages)
    pdf.showPage()


def report_title_page(pdf: canvas.Canvas, index: int, pages: int) -> None:
    report_no = index + 1
    report_date = REPORT_DATES[index]
    pdf.setFont("Klang-Regular", 11)
    pdf.drawCentredString(105 * mm, 255 * mm, COURT)
    pdf.drawCentredString(105 * mm, 247 * mm, f"Az. {CASE_NUMBER}")
    pdf.setFont("Klang-Bold", 17)
    pdf.drawCentredString(105 * mm, 215 * mm, f"TURNUSMAESSIGER ZWISCHENBERICHT NR. {report_no:02d}")
    pdf.setFont("Klang-Regular", 13)
    pdf.drawCentredString(105 * mm, 202 * mm, f"Stichtag {de_date(report_date)}")
    pdf.setFont("Klang-Bold", 13)
    pdf.drawCentredString(105 * mm, 178 * mm, DEBTOR)
    pdf.setFont("Klang-Regular", 11)
    pdf.drawCentredString(105 * mm, 164 * mm, "Hainwerkstrasse 18, 96049 Bamberg")
    pdf.drawCentredString(105 * mm, 135 * mm, f"Insolvenzverwalterin: {ADMINISTRATOR}")
    pdf.drawCentredString(105 * mm, 127 * mm, f"Sachbearbeitung: {CASE_WORKER}")
    pdf.drawCentredString(105 * mm, 101 * mm, f"Berichtszeitraum {de_date(report_period(index)[0])} bis {de_date(report_date)}")
    pdf.setFont("Klang-Regular", 9)
    pdf.drawCentredString(105 * mm, 55 * mm, "Verfahrensunterlage - synthetische Personen- und Unternehmensdaten")
    draw_footer(pdf, report_no, 2, pages)
    pdf.showPage()


def narrative_section_groups(page_count: int) -> list[list[int]]:
    """Ordnet die zehn Sachstandsabschnitte reproduzierbar den Narrativseiten zu."""
    if page_count < 2:
        raise RuntimeError("Ein Zwischenbericht benoetigt mindestens zwei Sachstandsseiten")
    if page_count == 2:
        return [list(range(0, 5)), list(range(5, 10))]
    chunk = (10 + page_count - 1) // page_count
    groups = [list(range(start, min(start + chunk, 10))) for start in range(0, 10, chunk)]
    while len(groups) < page_count:
        groups.append([])
    return groups


def narrative_section_titles(index: int) -> tuple[str, ...]:
    return (
        "1. Vorbemerkung und zeitliche Abgrenzung",
        f"2. {EVENTS[index]['title']}",
        "3. Masseentwicklung im Berichtszeitraum",
        "4. Verwertung, Debitoren und Sicherheiten",
        "5. Forderungstabelle",
        "6. Prozesse, Haftung und Steuern",
        "7. Kosten, Verguetung und Rueckstellungen",
        "8. Offene Punkte",
        "9. Naechste Arbeitsschritte",
        "10. Zusammenfassung fuer die gerichtliche Aufsicht",
    )


def report_toc_entries(index: int, narrative_pages: int, annex_pages: int) -> list[tuple[str, int]]:
    groups = narrative_section_groups(narrative_pages)
    section_pages: dict[int, int] = {}
    for page_offset, group in enumerate(groups):
        for section_index in group:
            section_pages[section_index] = 4 + page_offset
    entries = [
        (title, section_pages[section_index])
        for section_index, title in enumerate(narrative_section_titles(index))
    ]
    financial_pages = 0 if index == 21 else 3
    if financial_pages:
        first_financial_page = 4 + narrative_pages
        entries.extend((
            ("Anlage 1: Einnahmen- und Ausgabenrechnung", first_financial_page),
            ("Anlage 2: Kumulierte Masserechnung", first_financial_page + 1),
            ("Anlage 3: Kontonachweis", first_financial_page + 2),
        ))
    if annex_pages:
        entries.append((
            "Anlage 4: Konvolut aus 42 Nachweisseiten",
            4 + narrative_pages + financial_pages,
        ))
    return entries


def report_toc(pdf: canvas.Canvas, index: int, pages: int, narrative_pages: int, annex_pages: int) -> None:
    report_no = index + 1
    entries = report_toc_entries(index, narrative_pages, annex_pages)
    draw_header(pdf, "Inhaltsverzeichnis")
    pdf.setFont("Klang-Bold", 15)
    pdf.drawString(23 * mm, 265 * mm, "Inhaltsverzeichnis")
    y = 250 * mm
    for title, page_number in entries:
        pdf.setFont("Klang-Regular", 8.6)
        pdf.drawString(27 * mm, y, title)
        pdf.setStrokeColor(colors.HexColor("#999999"))
        pdf.setDash(1, 2)
        pdf.line(166 * mm, y - 1, 176 * mm, y - 1)
        pdf.setDash()
        pdf.drawRightString(185 * mm, y, str(page_number))
        y -= 9 * mm
    draw_footer(pdf, report_no, 3, pages)
    pdf.showPage()


def narrative_blocks(index: int, page_index: int, page_count: int) -> list[tuple[str, str]]:
    event = EVENTS[index]
    report_date = REPORT_DATES[index]
    opening = CLOSING_BALANCES[index - 1] if index else Decimal("0")
    closing = CLOSING_BALANCES[index]
    registered = REGISTERED_CLAIMS[index]
    established = ESTABLISHED_CLAIMS[index]
    if index == 21:
        open_points_text = (
            event["open"]
            + " Die faktische Schlussreife bleibt trotz der offenen Gates unberuehrt. Die offenen "
            "Freigabe- und Vollzugsschritte sperren jedoch die Einreichung des Schlussberichts, die Schlussverteilung, "
            "jede Auszahlung und die gerichtliche Aufhebung des Verfahrens, bis die jeweils zustaendige "
            "Person oder Stelle entschieden hat."
        )
        summary_text = (
            f"Der Verfahrensstand ist zum {de_date(report_date)} geordnet dokumentiert. Der Massebestand "
            f"von {euro(closing)} ist im separat gefuehrten Rechenwerk und durch den Abgleich mit den "
            "Finanzanlagen der Zwischenberichte 01 bis 21 belegt. Dieser kurze Zwischenbericht enthaelt "
            "weder eine Periodenrechnung noch einen Kontonachweis als Anlage. Die faktische Schlussreife ist "
            "belegt. Schlussbericht, Schlussrechnung und Schlussverzeichnis bleiben gesonderte Produkte; "
            "Einreichung, Verteilung, Auszahlung und Aufhebung duerfen erst nach den offenen Freigaben und "
            "gerichtlichen Entscheidungen erfolgen."
        )
    else:
        open_points_text = (
            event["open"]
            + " Diese Punkte verhindern je nach Stand entweder eine abschliessende Masserechnung, das "
            "Einfrieren der Forderungsbasis oder die Schlussreife. Fehlende Belege werden in der "
            "Belegmatrix mit verantwortlicher Person und naechstem erwarteten Eingang gefuehrt."
        )
        summary_text = (
            f"Der Verfahrensstand ist zum {de_date(report_date)} geordnet dokumentiert. Der Massebestand "
            f"von {euro(closing)} ist mit der Periodenrechnung verknuepft. Die noch offenen Punkte sind "
            "konkret benannt; eine Schlussreife wird nur im letzten Zwischenbericht und auch dort lediglich "
            "als Anlass fuer die gesonderte Erstellung von Schlussbericht und Schlussrechnung festgestellt."
        )

    if index == 21:
        mass_development_text = (
            f"Der Anfangsbestand belief sich auf {euro(opening)}. Im Zeitraum wurden Einnahmen von "
            f"{euro(RECEIPTS[index])} und Ausgaben von {euro(EXPENSES[index])} gebucht. Daraus folgt "
            f"zum Stichtag ein rechnerischer Bestand von {euro(closing)}. Dieser fuenfseitige "
            "Zwischenbericht enthaelt weder eine Periodenrechnung noch einen Kontonachweis als Anlage. "
            "Die vier Buchungen des Berichtszeitraums stehen im separat gefuehrten Rechenwerk; der "
            "Bestand wird zusaetzlich gegen die Finanzanlagen der Zwischenberichte 01 bis 21 und den "
            "gesonderten Banknachweis abgeglichen. Eine Verteilungsfreigabe ist damit nicht verbunden."
        )
    else:
        mass_development_text = (
            f"Der Anfangsbestand belief sich auf {euro(opening)}. Im Zeitraum wurden Einnahmen von "
            f"{euro(RECEIPTS[index])} und Ausgaben von {euro(EXPENSES[index])} gebucht. Daraus folgt "
            f"zum Stichtag ein rechnerischer Bestand von {euro(closing)}. Die Periodenrechnung und der "
            "Kontonachweis werden in den Anlagen getrennt wiedergegeben; eine Verteilungsfreigabe ist damit nicht verbunden."
        )

    basic = [
        (
            "1. Vorbemerkung und zeitliche Abgrenzung",
            f"Dieser Bericht erfasst ausschliesslich den Sachstand bis {de_date(report_date)}. "
            f"Er knuepft an den vorherigen Zwischenbericht an; spaetere Zahlungen, Beschluesse und "
            f"Vergleiche werden nicht vorweggenommen. Der Berichtszeitraum umfasst "
            f"{(report_date - report_period(index)[0]).days + 1} Kalendertage. Die Akte unterscheidet "
            f"belegte Tatsachen, laufende Pruefungen und Prognosen."
        ),
        (
            f"2. {event['title']}",
            event["change"] + " Die Darstellung beruht auf den bis zum Stichtag gebuchten Zahlungsvorgaengen, "
            "den vorliegenden Vertragsanlagen und der zu diesem Zeitpunkt gefuehrten Korrespondenz. "
            "Noch nicht belegte Erwartungen werden nicht als Massezufluss angesetzt."
        ),
        (
            "3. Masseentwicklung im Berichtszeitraum",
            mass_development_text,
        ),
        (
            "4. Verwertung, Debitoren und Sicherheiten",
            event["process"] + " Jede Zuordnung eines Erloeses zur freien Masse oder zu einer "
            "Sicherungsglaeubigerin wird in der Buchhaltung gesondert gekennzeichnet. Ein streitiger oder "
            "noch nicht eingegangener Betrag wird weder im Bankbestand noch in einer Quotenrechnung als verfuegbar behandelt."
        ),
        (
            "5. Forderungstabelle",
            f"Zum Stichtag sind Forderungen von {euro(registered)} angemeldet. Davon sind "
            f"{euro(established)} festgestellt. Die Differenz umfasst bestrittene, nachzuweisende, "
            "reduzierte oder noch nicht gepruefte Positionen. Nachrangige Forderungen werden ausserhalb "
            "der fuer eine vorlaeufige Quotenschaetzung verwendeten Basis gefuehrt."
        ),
        (
            "6. Prozesse, Haftung und Steuern",
            "Laufende Aktiv- und Passivvorgaenge werden mit Streitwert, Verfahrensstand, Kostenrisiko, "
            "naechstem Termin und erwartetem Nettoeffekt gefuehrt. Die rechtliche Bewertung wird nicht "
            "durch eine bloss buchhalterische Forderungsposition ersetzt. Steuerliche Erstattungen werden "
            "erst nach Bescheid und Zahlungseingang als realisierter Massezufluss ausgewiesen."
        ),
        (
            "7. Kosten, Verguetung und Rueckstellungen",
            "Verfahrenskosten und Masseverbindlichkeiten sind nach Entstehungsgrund und Faelligkeit getrennt. "
            "Eine Verguetungsreserve ist keine gerichtliche Festsetzung. Ebenso stellt eine interne "
            "Schlusskostenrechnung weder die Genehmigung einer Schlussverteilung noch den Vollzug von Zahlungen dar."
        ),
        (
            "8. Offene Punkte",
            open_points_text,
        ),
        (
            "9. Naechste Arbeitsschritte",
            event["next"] + " Aussenwirksame Erklaerungen, gerichtliche Einreichungen und Zahlungen beduerfen "
            "einer namentlich dokumentierten menschlichen Freigabe. Der naechste Bericht wird bei wesentlicher "
            "Aenderung vorzeitig, sonst zum gerichtlichen Turnus vorgelegt."
        ),
        (
            "10. Zusammenfassung fuer die gerichtliche Aufsicht",
            summary_text,
        ),
    ]
    groups = []
    for section_indices in narrative_section_groups(page_count):
        if section_indices:
            groups.append([basic[section_index] for section_index in section_indices])
        else:
            groups.append([
                (
                    f"{10 + len(groups)}. Ergaenzende Fortschreibung",
                    f"Die Arbeitsliste zum Stichtag {de_date(report_date)} wird ohne Aenderung des "
                    "festgestellten Zahlenstands fortgefuehrt. Eingehende Unterlagen werden erst nach "
                    "inhaltlicher und rechnerischer Pruefung in die fuehrende Fassung uebernommen."
                )
            ])
    return groups[page_index]


def draw_cash_page(pdf: canvas.Canvas, index: int, page_no: int, pages: int, cumulative: bool) -> None:
    report_no = index + 1
    report_date = REPORT_DATES[index]
    opening = CLOSING_BALANCES[index - 1] if index else Decimal("0")
    receipts = RECEIPTS[index]
    expenses = EXPENSES[index]
    closing = CLOSING_BALANCES[index]
    draw_header(pdf, "Einnahmen- und Ausgabenrechnung" if not cumulative else "Kumulierte Masserechnung")
    pdf.setFont("Klang-Bold", 14)
    pdf.drawString(23 * mm, 265 * mm, "Einnahmen- und Ausgabenrechnung" if not cumulative else "Kumulierte Masserechnung")
    if not cumulative:
        rows = [
            ["Position", "Einnahmen", "Ausgaben"],
            ["Anfangsbestand", euro(opening), ""],
            ["Verwertung und Forderungseinzug", euro((receipts * Decimal("0.64")).quantize(Decimal("0.01"))), ""],
            ["Vergleiche, Erstattungen und Zinsen", euro(receipts - (receipts * Decimal("0.64")).quantize(Decimal("0.01"))), ""],
            ["Rechts-, Steuer- und Gutachterkosten", "", euro((expenses * Decimal("0.57")).quantize(Decimal("0.01")))],
            ["Massebuero, Bank, Archiv und Sonstiges", "", euro(expenses - (expenses * Decimal("0.57")).quantize(Decimal("0.01")))],
            ["Summe Bewegungen", euro(receipts), euro(expenses)],
            ["Endbestand", euro(closing), ""],
        ]
    else:
        total_receipts = sum(RECEIPTS[: index + 1], Decimal("0"))
        total_expenses = sum(EXPENSES[: index + 1], Decimal("0"))
        rows = [
            ["Kontrollgroesse", "Betrag"],
            ["Einnahmen seit Eroeffnung", euro(total_receipts)],
            ["Ausgaben seit Eroeffnung", euro(total_expenses)],
            ["Rechnerischer Massebestand", euro(total_receipts - total_expenses)],
            ["Bankbestand zum Stichtag", euro(closing)],
            ["Differenz", euro((total_receipts - total_expenses) - closing)],
            ["Angemeldete Forderungen", euro(REGISTERED_CLAIMS[index])],
            ["Festgestellte Forderungen", euro(ESTABLISHED_CLAIMS[index])],
        ]
    table = Table(rows, colWidths=[86 * mm, 39 * mm, 39 * mm] if not cumulative else [108 * mm, 56 * mm], repeatRows=1)
    table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "Klang-Regular"),
        ("FONTNAME", (0, 0), (-1, 0), "Klang-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9.5),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8E8E8")),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#777777")),
        ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
    ]))
    _, height = table.wrap(164 * mm, 180 * mm)
    table.drawOn(pdf, 23 * mm, 250 * mm - height)
    note = Paragraph(
        "Kontrollhinweis: Die Darstellung bildet den Buchungsstand zum Stichtag ab. Offene, lediglich erwartete oder bestrittene Betraege sind nicht im Bankbestand enthalten. Eine Quote darf nur mit einer belastbaren Forderungsbasis und nach Abzug aller Schlusskosten berechnet werden.",
        BODY,
    )
    _, height = note.wrap(164 * mm, 60 * mm)
    note.drawOn(pdf, 23 * mm, 58 * mm)
    draw_footer(pdf, report_no, page_no, pages)
    pdf.showPage()


def bank_receipt_labels(index: int) -> tuple[str, str]:
    return tuple(entry[2] for entry in period_transactions(index) if entry[1] == "E")  # type: ignore[return-value]


def draw_bank_page(pdf: canvas.Canvas, index: int, page_no: int, pages: int) -> None:
    report_no = index + 1
    report_date = REPORT_DATES[index]
    opening = CLOSING_BALANCES[index - 1] if index else Decimal("0")
    draw_header(pdf, "Kontonachweis")
    pdf.setFont("Klang-Bold", 14)
    pdf.drawString(23 * mm, 265 * mm, "Kontonachweis zum Berichtsstichtag")
    pdf.setFont("Klang-Regular", 10)
    pdf.drawString(23 * mm, 254 * mm, "Frankenbogen Bank eG - Sonderkonto DE00 0000 0000 0000 0000 00")
    rows = [
        ["Buchungstag", "Buchungstext", "Eingang", "Ausgang", "Saldo"],
        [de_date(report_period(index)[0]), "Vortrag", "", "", euro(opening)],
    ]
    for booking_date, kind, label, amount in period_transactions(index):
        rows.append([
            de_date(booking_date),
            label,
            euro(amount) if kind == "E" else "",
            euro(amount) if kind == "A" else "",
            "",
        ])
    rows.append([de_date(report_date), "Abschlusssaldo", "", "", euro(CLOSING_BALANCES[index])])
    table = Table(rows, colWidths=[25 * mm, 54 * mm, 28 * mm, 28 * mm, 29 * mm], repeatRows=1)
    table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "Klang-Regular"),
        ("FONTNAME", (0, 0), (-1, 0), "Klang-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 8.2),
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8E8E8")),
        ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#888888")),
        ("ALIGN", (2, 1), (-1, -1), "RIGHT"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    _, height = table.wrap(164 * mm, 180 * mm)
    table.drawOn(pdf, 23 * mm, 247 * mm - height)
    pdf.setFont("Klang-Regular", 9.5)
    pdf.drawString(23 * mm, 60 * mm, "Der Kontoauszug ist mit dem internen Buchungsjournal abgestimmt.")
    pdf.drawString(23 * mm, 53 * mm, "Die Kontonummer ist fuer diese Schulungsakte technisch nicht zahlungsfaehig.")
    draw_footer(pdf, report_no, page_no, pages)
    pdf.showPage()


REPORT_13_CORRESPONDENCE = (
    {
        "sender": "Frankenbogen Bank eG, Sonderkreditmanagement, Veit Claassen",
        "recipient": "Dr. Mechthild Karg, Insolvenzverwalterin",
        "date": date(2021, 12, 6),
        "table_id": "F-001",
        "subject": "Ausfallberechnung nach Sicherheitenabrechnung",
        "attachments": "Ausfallberechnung vom 03.12.2021; Sicherheitenabrechnung SA-44/21; Kontoabschluss 30.11.2021",
        "result": "Die Berechnung ist rechnerisch nachvollziehbar. Die Position bleibt bis zur Kontrolle des Verwertungskostenanteils teilweise pruefungsbeduerftig.",
    },
    {
        "sender": "Finanzamt Bamberg, Sachgebiet Insolvenz, Ruprecht Pfrang",
        "recipient": "Philipp Joens, Karg Endres Insolvenzverwaltung PartG mbB",
        "date": date(2021, 12, 21),
        "table_id": "F-002",
        "subject": "Aufgliederung der angemeldeten Steuerforderungen",
        "attachments": "Rueckstandsaufstellung RST-2021-447; Berechnungsbogen Umsatzsteuer; Berechnungsbogen Lohnsteuer",
        "result": "Hauptforderung und Nebenleistungen sind getrennt. Die Zuordnung zu Vor- und Massezeitraum wird im Steuerkontenblatt weiter geprueft.",
    },
    {
        "sender": "BKK Buehnenhandwerk, Einzugsstelle, Ann-Kathrin Seubelt",
        "recipient": "Dr. Mechthild Karg, Insolvenzverwalterin",
        "date": date(2022, 1, 11),
        "table_id": "F-003",
        "subject": "Beitragsnachweise und Arbeitnehmerzuordnung",
        "attachments": "Beitragsnachweise 08/2015 bis 11/2015; Arbeitnehmerliste; Summenblatt SV-2015-11",
        "result": "Die Arbeitnehmerzuordnung ist belegt. Saeumniszuschlaege werden noch gegen den Eroeffnungszeitpunkt abgegrenzt.",
    },
    {
        "sender": "Agentur fuer Arbeit Bamberg, Forderungseinzug, Jodokus Zink",
        "recipient": "Philipp Joens, Karg Endres Insolvenzverwaltung PartG mbB",
        "date": date(2022, 2, 3),
        "table_id": "F-004",
        "subject": "Uebergegangene Arbeitsentgeltansprueche",
        "attachments": "Uebergangsliste 01-2022; Insolvenzgeldbescheide in Sammelaufstellung; Abgleichsliste Personalnummern",
        "result": "Der Anspruchsuebergang ist fuer die bezeichneten Beschaeftigten belegt. Zwei Doppelmeldungen werden vor der endgueltigen Feststellung bereinigt.",
    },
    {
        "sender": "Walburga Pfrang fuer den Beschaeftigtenpool Klangbogen",
        "recipient": "Dr. Mechthild Karg, Insolvenzverwalterin",
        "date": date(2022, 2, 18),
        "table_id": "F-005",
        "subject": "Einzelaufstellung restlicher Arbeitnehmerforderungen",
        "attachments": "Vollmachten von 17 Beschaeftigten; Forderungsliste Version 4; drei Lohnabrechnungen als Musterbelege",
        "result": "Die Vollmachten sind vollstaendig. Urlaubsabgeltung und Ueberstunden werden getrennt nach Anspruchsmonat nachgefordert.",
    },
    {
        "sender": "Hainwerk Hallen KG, Hausverwaltung, Kunigunde Woelfel",
        "recipient": "Philipp Joens, Karg Endres Insolvenzverwaltung PartG mbB",
        "date": date(2022, 3, 11),
        "table_id": "F-006",
        "subject": "Mietkonto und Betriebskostenabgrenzung",
        "attachments": "Mietkonto 2015 bis 2021; Betriebskostenabrechnung 2020; Uebergabeprotokoll vom 18.02.2016",
        "result": "Das Mietkonto ist abgestimmt. Eine nach Eroeffnung entstandene Betriebskostenposition wird ausserhalb der Tabellenforderung behandelt.",
    },
    {
        "sender": "Frankenlift Leasing GmbH, Vertragsservice, Hinnerk Thalhammer",
        "recipient": "Dr. Mechthild Karg, Insolvenzverwalterin",
        "date": date(2022, 4, 7),
        "table_id": "F-007",
        "subject": "Leasingabrechnung nach Ruecknahme der Hubtechnik",
        "attachments": "Leasingvertrag FL-8821; Ruecknahmeprotokoll; Verwertungsgutschrift VG-2022-19",
        "result": "Die Verwertungsgutschrift ist angerechnet. Ein pauschaler Schadensposten bleibt bis zur vertraglichen Herleitung bestritten.",
    },
    {
        "sender": "Boehlein Metallbau GmbH, Debitorenbuchhaltung, Veit Boehlein",
        "recipient": "Philipp Joens, Karg Endres Insolvenzverwaltung PartG mbB",
        "date": date(2022, 5, 4),
        "table_id": "F-008",
        "subject": "Liefernachweise fuer Tragrahmen und Konsolen",
        "attachments": "Rechnungen BM-447 bis BM-451; Lieferscheine LS-901 bis LS-906; Abnahmeprotokoll AP-77",
        "result": "Lieferung und Abnahme sind belegt. Die Position kann nach Abgleich einer bereits verbuchten Gutschrift abschliessend festgestellt werden.",
    },
)

REPORT_13_CONTROL_GROUPS = (
    ("Bankausfall", "F-001", "Frankenbogen Bank eG", "Ausfall nach Sicherheitenabrechnung", Decimal("252208.07"), Decimal("252208.07"), "festgestellt"),
    ("Steuern", "F-002", "Finanzamt Bamberg", "Steuern", Decimal("178550.00"), Decimal("178550.00"), "festgestellt"),
    ("Sozialversicherung", "F-003", "BKK Buehnenhandwerk", "Sozialversicherung", Decimal("133420.75"), Decimal("133420.75"), "festgestellt"),
    ("Uebergegangene Ansprueche", "F-004", "Agentur fuer Arbeit", "Uebergegangene Ansprueche", Decimal("112844.20"), Decimal("112844.20"), "festgestellt"),
    ("Arbeitnehmer", "F-005", "Beschaeftigtenpool Klangbogen", "Arbeitnehmerforderungen", Decimal("96512.55"), Decimal("96512.55"), "festgestellt"),
    ("Miete", "F-006", "Hainwerk Hallen KG", "Miete", Decimal("89334.11"), Decimal("89334.11"), "festgestellt"),
    ("Leasing", "F-007", "Frankenlift Leasing GmbH", "Leasing", Decimal("85200.00"), Decimal("85200.00"), "festgestellt"),
    ("Lieferanten", "F-008", "Boehlein Metallbau GmbH", "Lieferung", Decimal("78450.60"), Decimal("78450.60"), "festgestellt"),
)

REPORT_13_PROCESS_REGISTER = (
    ("Kaufpreiseinbehalt", date(2022, 1, 19), "LG Bamberg, 2 O 317/17", Decimal("62500.00"), Decimal("13840.00"), "Kostenfestsetzungsantrag nach dem Vergleich vom 05.02.2019 nachhalten; keine weitere Hauptsachezahlung ansetzen."),
    ("Organhaftung Geschaeftsfuehrung", date(2022, 2, 2), "LG Bamberg, 1 O 88/20", Decimal("186400.00"), Decimal("27860.00"), "Liquiditaetsstatus und Gesellschafterbeschluesse als Anlagen zum naechsten Schriftsatz ordnen."),
    ("D-und-O-Deckung", date(2022, 2, 23), "Deckungsakte DO-19-884", Decimal("96500.00"), Decimal("11420.00"), "Deckungseinwendungen schriftlich beantworten und den freigegebenen Mediationskorridor dokumentieren."),
    ("Aufrechnung Theaterprojekt", date(2022, 3, 16), "LG Hof, 4 O 211/19", Decimal("35620.59"), Decimal("8940.00"), "Erfuellung des Vergleichs vom 14.07.2021 belegen und die Erledigungserklaerung kostenrechtlich pruefen."),
    ("Kostenfestsetzung Gutachterverfahren", date(2022, 4, 6), "LG Bamberg, 2 O 317/17 KfH", Decimal("7465.30"), Decimal("3190.00"), "Erstattungsfaehige Gutachterauslagen belegen und die gerichtliche Kostenrechnung abgleichen."),
    ("Forderung in Parallelinsolvenz", date(2022, 5, 12), "AG Wuerzburg, 3 IN 244/20", Decimal("44760.00"), Decimal("2680.00"), "Tabellenfeststellung ueberwachen; bis zu einer Auszahlung keinen Massezufluss buchen."),
)

REPORT_13_TAX_ACCOUNTS = (
    ("Umsatzsteuer", date(2022, 1, 12), "BK-UST-MASSE", "207/815/01345", "Steuerberatung Thalhammer und Pfrang PartG mbB, StB Ruprecht Pfrang", "Voranmeldungen 2015 bis 2021 mit den Bankbuchungen abstimmen; noch keinen Erstattungsanspruch aktivieren."),
    ("Lohnsteuer", date(2022, 2, 9), "BK-LST-ABWICKLUNG", "207/815/01346", "Steuerberatung Thalhammer und Pfrang PartG mbB, StBin Marielein Endres", "Lohnsteueranmeldungen und Arbeitnehmerliste gegen die Tabellenpositionen F-003 bis F-005 abgleichen."),
    ("Koerperschaftsteuer", date(2022, 3, 16), "BK-KST-INSG", "207/815/01347", "Steuerberatung Thalhammer und Pfrang PartG mbB, StB Ruprecht Pfrang", "Verlustvortraege und Veraeusserungsgewinn aus dem Asset Deal fuer die ausstehende Erklaerung dokumentieren."),
    ("Gewerbesteuer", date(2022, 4, 28), "BK-GEWST-BAMBERG", "5-731-00981", "Steuerberatung Thalhammer und Pfrang PartG mbB, StBin Marielein Endres", "Messbetragsmitteilung abwarten und die Zerlegung fuer Bamberg und den frueheren Montagestandort pruefen."),
)

REPORT_13_BANK_RECORDS = (
    ("B-0049", date(2021, 12, 17), date(2021, 12, 17), "E", "Verwertungserloes", Decimal("22191.58"), Decimal("0"), Decimal("451748.00"), "GK-KLANGKAUF-13-01"),
    ("B-0050", date(2022, 1, 8), date(2022, 1, 10), "A", "Rechts- und Gutachterkosten", Decimal("0"), Decimal("9125.60"), Decimal("442622.40"), "GK-LG-BAMBERG-KOST-01"),
    ("B-0051", date(2022, 4, 22), date(2022, 4, 22), "E", "Forderungseinzug", Decimal("10443.09"), Decimal("0"), Decimal("453065.49"), "GK-DEBITOR-RAUMKLANG-07"),
    ("B-0052", date(2022, 5, 14), date(2022, 5, 16), "A", "Massebuero und Bank", Decimal("0"), Decimal("5834.40"), Decimal("447231.09"), "GK-KARG-ENDRES-MASSE-01"),
)


def annex_page(pdf: canvas.Canvas, index: int, annex_index: int, page_no: int, pages: int) -> None:
    report_no = index + 1
    as_of = REPORT_DATES[index]
    if annex_index < 12:
        title = f"Forderungsnachweis {annex_index + 1:02d}"
        registered = Decimal("18400") + Decimal(annex_index * 1735)
        reduction = (Decimal("0"), Decimal("1250"), Decimal("2100"), Decimal("3475"))[annex_index % 4]
        established = registered - reduction
        if reduction == 0:
            status = "vollstaendig festgestellt; kein bestrittener oder reduzierter Restbetrag"
        elif annex_index % 4 == 1:
            status = f"teilweise festgestellt; {euro(reduction)} bleiben bestritten"
        elif annex_index % 4 == 2:
            status = f"nach Teilruecknahme um {euro(reduction)} reduziert; Rest vollstaendig festgestellt"
        else:
            status = "um 2.000,00 EUR reduziert; weitere 1.475,00 EUR bleiben bestritten"
        creditor = (
            f"Glaeubiger: {['Veit Boehlein', 'Walburga Pfrang', 'Jodokus Zink', 'Almut Eyrich'][annex_index % 4]} "
            f"{['Metallbau GmbH', 'Antriebstechnik KG', 'Lichtsteuerung eG', 'Raumakustik GmbH'][annex_index % 4]}. "
            "Geprueft wurden Anmeldung, Rechnung, Leistungsnachweis, Faelligkeit und ein etwaiger "
            "Sicherungs- oder Ranggrund. Der Status gilt ausschliesslich zum 23.05.2022."
        )
        blocks = [
            ("Pruefumfang", creditor),
            (
                "Betrags- und Tabellenstatus",
                f"Angemeldet: {euro(registered)}. Festgestellt: {euro(established)}. "
                f"Bestritten beziehungsweise reduziert: {euro(reduction)}. Status: {status}.",
            ),
            (
                "Beleg-IDs",
                f"Anmeldung ANM-13-{annex_index + 1:02d}; Rechnung RE-13-{annex_index + 1:02d}; "
                f"Leistungs- oder Abnahmenachweis LN-13-{annex_index + 1:02d}; "
                f"Pruefvermerk PV-13-{annex_index + 1:02d}.",
            ),
        ]
    elif annex_index < 20:
        title = f"Korrespondenznachweis {annex_index - 11:02d}"
        item = REPORT_13_CORRESPONDENCE[annex_index - 12]
        blocks = [
            ("Kommunikationsdaten", f"Absender: {item['sender']}. Empfaenger: {item['recipient']}. Datum: {de_date(item['date'])}. Betreff: {item['subject']}."),
            ("Tabellenposition", f"Zuordnung zur Tabellenposition {item['table_id']}. Die ID bezeichnet die Einzelposition im Tabellenblatt Forderungen; aus diesem Schreiben allein folgt keine Feststellung."),
            ("Anlagen", item["attachments"] + "."),
            ("Pruefergebnis und naechster Schritt", item["result"]),
        ]
    elif annex_index < 28:
        title = f"Kontrollgruppe Stichprobe {annex_index - 19:02d}"
        group, table_id, creditor, reason, registered, established, status = REPORT_13_CONTROL_GROUPS[annex_index - 20]
        blocks = [
            ("Auswahl", f"Kontrollgruppe: {group}. Gepruefte Einzelposition: {table_id}, {creditor}. Forderungsgrund: {reason}."),
            ("Werte und Status", f"Angemeldet: {euro(registered)}. Festgestellt: {euro(established)}. Status: {status}."),
            ("Vorhandene Spalten im Rechenwerk", "Der Abgleich verwendet ausschliesslich ID, Glaeubiger, Grund, Angemeldet, Festgestellt und Status aus dem Tabellenblatt Forderungen."),
            ("Abgrenzung und Ergebnis", "Es handelt sich um die Kontrolle einer Einzelposition, weder um eine Gruppensumme noch um eine Zwischensumme. Die Werte und der Status stimmen fuer diese Position ueberein."),
        ]
    elif annex_index < 34:
        title = f"Prozessregister {annex_index - 27:02d}"
        process, status_date, reference, dispute_value, costs, next_step = REPORT_13_PROCESS_REGISTER[annex_index - 28]
        blocks = [
            ("Vorgang und Datum", f"{process}. Stand: {de_date(status_date)}. Referenz: {reference}."),
            ("Streitwert", euro(dispute_value)),
            ("Kostenstand", f"Bis zum Stichtag erfasste Gerichts-, Gutachter- und Anwaltskosten: {euro(costs)}. Der Betrag ist ein Vorgangswert und kein erwarteter Massezufluss."),
            ("Naechster Schritt", next_step),
        ]
    elif annex_index < 38:
        title = f"Steuerkontenblatt {annex_index - 33:02d}"
        tax_type, status_date, booking_area, tax_account, advisor, next_step = REPORT_13_TAX_ACCOUNTS[annex_index - 34]
        blocks = [
            ("Steuerart und Datum", f"{tax_type}. Bearbeitungsstand: {de_date(status_date)}."),
            ("Buchungskreis und Steuerkonto", f"Buchungskreis: {booking_area}. Steuerkonto: {tax_account}. Diese Kennungen stehen auf diesem Nachweisblatt; das Rechenwerk fuehrt keine eigenen Spalten Buchungskreis oder Steuerkonto."),
            ("Steuerliche Beratung", f"Verantwortliche Beraterin oder verantwortlicher Berater: {advisor}."),
            ("Pruefstand und naechster Schritt", f"Ein noch nicht erlassener Bescheid wird nicht als Erstattungsanspruch angesetzt. {next_step}"),
        ]
    else:
        title = f"Banknachweis Teil {annex_index - 37:02d}"
        evidence_id, booking_date, value_date, booking_type, booking_text, receipt, expense, balance, counterparty = REPORT_13_BANK_RECORDS[annex_index - 38]
        blocks = [
            ("Beleg-ID und Journalzuordnung", f"Beleg-ID: {evidence_id}. Bericht 13. Buchungstag: {de_date(booking_date)}. Art: {booking_type}. Buchungstext: {booking_text}."),
            ("Wertstellung und Gegenkonto", f"Wertstellung: {de_date(value_date)}. Gegenkonto: {counterparty} (synthetische Kennung, keine Bankverbindung)."),
            ("Betrag und laufender Saldo", f"Einnahme: {euro(receipt)}. Ausgabe: {euro(expense)}. Laufender Saldo nach Buchung: {euro(balance)}."),
            ("Abgleich mit dem Rechenwerk", "Im Tabellenblatt Kontenjournal stehen Beleg-ID, Datum, Bericht, Art, Buchungstext, Einnahme, Ausgabe und Laufender Saldo. Wertstellung und Gegenkonto stehen nur auf diesem Einzelbeleg und werden nicht als Spalten des Rechenwerks behauptet."),
        ]
    draw_flow_page(pdf, title, blocks, report_no, page_no, pages)


def make_report(index: int) -> Path:
    path = report_filename(index + 1, REPORT_DATES[index])
    path.parent.mkdir(parents=True, exist_ok=True)
    pages = REPORT_PAGES[index]
    annex_pages = REPORT_13_ANNEX_PAGES if index == 12 else 0
    financial_pages = 0 if index == 21 else 3
    narrative_pages = pages - 3 - financial_pages - annex_pages
    if narrative_pages < 2:
        raise RuntimeError(f"Zu wenige narrative Seiten: Bericht {index + 1}")
    pdf = canvas.Canvas(str(path), pagesize=A4, invariant=1)
    pdf.setTitle(f"Zwischenbericht {index + 1:02d} - {DEBTOR}")
    pdf.setAuthor(ADMINISTRATOR)
    pdf.setSubject(f"{COURT}, {CASE_NUMBER}, Stichtag {de_date(REPORT_DATES[index])}")
    report_letter(pdf, index, pages)
    report_title_page(pdf, index, pages)
    report_toc(pdf, index, pages, narrative_pages, annex_pages)
    page_no = 4
    for narrative_index in range(narrative_pages):
        draw_flow_page(
            pdf,
            f"Zwischenbericht {index + 1:02d} - Sachstand",
            narrative_blocks(index, narrative_index, narrative_pages),
            index + 1,
            page_no,
            pages,
        )
        page_no += 1
    if financial_pages:
        draw_cash_page(pdf, index, page_no, pages, False)
        page_no += 1
        draw_cash_page(pdf, index, page_no, pages, True)
        page_no += 1
        draw_bank_page(pdf, index, page_no, pages)
        page_no += 1
    for annex_index in range(annex_pages):
        annex_page(pdf, index, annex_index, page_no, pages)
        page_no += 1
    pdf.save()
    actual = len(PdfReader(path).pages)
    if actual != pages:
        raise RuntimeError(f"Bericht {index + 1}: {actual} statt {pages} Seiten")
    return path


def make_simple_pdf(
    path: Path,
    title: str,
    date_value: date,
    blocks: list[tuple[str, str]],
    pages: int = 1,
    *,
    issuer: str | None = None,
    signatory: str | None = None,
) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    document_issuer = issuer or ADMINISTRATOR
    pdf = canvas.Canvas(str(path), pagesize=A4, invariant=1)
    pdf.setTitle(title)
    pdf.setAuthor(document_issuer)
    document_blocks = list(blocks)
    if signatory:
        document_blocks.append(("Gezeichnet", signatory))
    chunks: list[list[tuple[str, str]]] = [[] for _ in range(pages)]
    for position, block in enumerate(document_blocks):
        chunks[min(position * pages // max(1, len(document_blocks)), pages - 1)].append(block)
    for page_index in range(pages):
        prefix = [(title, f"Datum: {de_date(date_value)} | Verfahren: {CASE_NUMBER} | Schuldnerin: {DEBTOR}")]
        draw_flow_page(
            pdf,
            title,
            prefix + chunks[page_index],
            None,
            page_index + 1,
            pages,
            title,
            document_issuer,
        )
    pdf.save()
    if len(PdfReader(path).pages) != pages:
        raise RuntimeError(f"Falsche Seitenzahl: {path}")
    return path


def make_evidence() -> list[Path]:
    evidence = [
        make_simple_pdf(
            EVIDENCE_DIR / "01_eroeffnungsbeschluss_2015-11-22.pdf",
            "Beschluss ueber die Verfahrenseroeffnung",
            OPENING_DATE,
            [
                ("Tenor", f"Das Insolvenzverfahren ueber das Vermoegen der {DEBTOR} wird eroeffnet. {ADMINISTRATOR} wird zur Insolvenzverwalterin bestellt."),
                ("Berichtswesen", "Die Insolvenzverwalterin berichtet turnusmaessig und bei wesentlichen Veraenderungen unverzueglich. Gerichtliche Einzelanordnungen bleiben massgeblich."),
                ("Hinweis", "Aktenzeichen und Beteiligtenangaben sind technisch fuer eine synthetische Schulungsakte eingerichtet."),
            ],
            2,
            issuer=COURT,
            signatory="Dr. Marielein Endres, Richterin am Amtsgericht",
        ),
        make_simple_pdf(
            EVIDENCE_DIR / "02_berichtsanordnung_2015-12-15.pdf",
            "Gerichtliche Berichtsanordnung",
            date(2015, 12, 15),
            [
                ("Turnus", "Der erste Zwischenbericht ist bis Ende Mai 2016 vorzulegen. Danach wird ein ungefaehr halbjaehrlicher Turnus erwartet; bei wesentlichen Ereignissen ist vorzeitig zu berichten."),
                ("Mindestinhalt", "Darzustellen sind Verwertung, Forderungseinzug, Prozesse, Steuern, Forderungstabelle, Massebestand und die voraussichtlichen naechsten Schritte."),
            ],
            issuer=COURT,
            signatory="Almut Eyrich, Urkundsbeamtin der Geschaeftsstelle",
        ),
        make_simple_pdf(
            EVIDENCE_DIR / "03_bankbestaetigung_2026-11-30.pdf",
            "Bankbestaetigung zum Sonderkonto",
            date(2026, 11, 30),
            [
                ("Bestaetigung", f"Die Frankenbogen Bank eG bestaetigt fuer das nicht zahlungsfaehige Testkonto einen Saldo von {euro(FINAL_CASH)} zum 28.11.2026."),
                ("Abgrenzung", "Zwischen dem Stichtag und dem Ausstellungsdatum wurden keine wertstellungsrelevanten Umsaetze gebucht."),
            ],
            issuer="Frankenbogen Bank eG",
            signatory="Veit Claassen, Kundenservice Sonderkonten",
        ),
        make_simple_pdf(
            EVIDENCE_DIR / "04_steuerbescheid_2026-09-15.pdf",
            "Aenderungsbescheid und Abrechnung Steuerkonto",
            date(2026, 9, 15),
            [
                ("Ergebnis", "Die Umsatzsteuer- und Koerperschaftsteuerkonten sind nach Abschluss der Aussenpruefung abgerechnet. Die vorlaeufige Steuerkontoabrechnung wurde mit dem Aenderungsbescheid abgeglichen."),
                ("Kontenjournal", "Der Steuerkontoauszug weist die Erstattung von 11.698,47 EUR mit Wertstellung zum 22.06.2026 aus. Der Aenderungsbescheid setzt daneben 5.505,16 EUR Zinsen fest; am Ausstellungsdatum war dieser Betrag noch nicht gutgeschrieben. Ein spaeterer Zahlungseingang kann deshalb erst in einem nachtraeglichen Kontenabgleich dokumentiert werden."),
                ("Rechtsbehelfsstatus am 15.09.2026", "Die Rechtsbehelfspruefung laeuft. Am Ausstellungsdatum wird weder ein Ablauf der Rechtsbehelfsfrist noch Bestandskraft behauptet. Posteingang, Fristenkontrolle und spaetere Kontobewegungen sind in einem gesonderten internen Aktenvermerk festzuhalten."),
            ],
            2,
            issuer="Finanzamt Bamberg",
            signatory="Ruprecht Pfrang, Sachgebietsleiter Veranlagung",
        ),
        make_simple_pdf(
            EVIDENCE_DIR / "05_vergleich_landbuehne_2021-07-14.pdf",
            "Vergleich Landbuehne Nord Projektgesellschaft mbH",
            date(2021, 7, 14),
            [
                ("Parteien", f"{DEBTOR}, vertreten durch die Insolvenzverwalterin, und Landbuehne Nord Projektgesellschaft mbH."),
                ("Vergleichsschluss", "Die Parteien schliessen den Vergleich am 14.07.2021. Die Landbuehne Nord Projektgesellschaft mbH verpflichtet sich, 35.620,59 EUR spaetestens am 19.07.2021 auf das Massekonto zu zahlen."),
                ("Zahlungseingang", "Diese Vereinbarung belegt Vergleichsschluss und Faelligkeit, nicht den tatsaechlichen Zahlungseingang. Ob und wann der Betrag eingeht, ist erst nach Faelligkeit anhand eines Kontoauszugs oder des Kontenjournals zu pruefen und erst danach als Massezufluss fortzuschreiben."),
                ("Kosten", "Jede Seite traegt ihre aussergerichtlichen Kosten selbst. Gerichtliche Kosten werden nach der protokollierten Quote getragen."),
                ("Erledigung", "Mit vollstaendigem Zahlungseingang sind die Werklohnforderung, die behauptete Vertragsstrafe und die bezeichneten Aufrechnungspositionen aus dem Projekt Landbuehne Nord erledigt."),
                ("Freigabe", "Grundlage sind die gesonderte Wirtschaftlichkeitspruefung vom 12.07.2021 und die Zustimmung des Glaeubigerausschusses vom 13.07.2021."),
            ],
            3,
            issuer="Vergleichsparteien Klangbogen und Landbuehne Nord",
            signatory="Dr. Mechthild Karg, Insolvenzverwalterin; Jost Thalhammer, Geschaeftsfuehrer der Landbuehne Nord Projektgesellschaft mbH",
        ),
        make_simple_pdf(
            EVIDENCE_DIR / "06_prozesskostenabrechnung_2024-09-18.pdf",
            "Prozess- und Vergleichskostenabrechnung",
            date(2024, 9, 18),
            [
                ("Vorgaenge", "Kaufpreiseinbehalt, Organhaftung, D-und-O-Deckung, Parallelverfahren und Kostenfestsetzung sind getrennt abgerechnet."),
                ("Pruefung", "Die abgerechneten Kosten sind im Kontenjournal belegt und den jeweiligen Erlosvorgaengen zugeordnet. Doppelerfassungen wurden nicht festgestellt."),
                ("Status am 18.09.2024", "Eine beantragte Kostenfestsetzung ueber 1.284,30 EUR ist noch nicht beschieden. Der Betrag ist weder als festgesetzt noch als Zahlung gebucht. Nach Eingang einer gerichtlichen Entscheidung sind Zuordnung und Kontenjournal gesondert fortzuschreiben."),
            ],
            2,
            signatory=CASE_WORKER,
        ),
        make_simple_pdf(
            EVIDENCE_DIR / "07_tabellenauszug_2026-11-30.pdf",
            "Auszug aus der Forderungstabelle",
            date(2026, 11, 30),
            [
                ("Ordentliche Forderungen", f"Festgestellt: {euro(FINAL_CLAIMS)}. Der Betrag stimmt mit dem Rechenwerk und dem letzten Zwischenbericht ueberein."),
                ("Weitere Positionen", "Nachrangige Forderungen und nicht teilnahmeberechtigte Positionen werden getrennt gefuehrt. Sie sind nicht in der vorlaeufigen Quotenbasis enthalten."),
                ("Status", "Offene Widersprueche bestehen nicht. Eine Auszahlungsliste ist noch nicht freigegeben."),
            ],
            3,
            signatory=CASE_WORKER,
        ),
        make_simple_pdf(
            EVIDENCE_DIR / "08_glaeubigerausschuss_stellungnahme_2026-12-02.pdf",
            "Stellungnahme des Glaeubigerausschusses",
            date(2026, 12, 2),
            [
                ("Pruefung", "Der Ausschuss hat den letzten Zwischenbericht, das Rechenwerk, den Banknachweis und die Belegmatrix eingesehen."),
                ("Ergebnis", "Aus Sicht des Ausschusses sind die Unterlagen fuer die Erstellung des Schlussberichts und der Schlussrechnung hinreichend aufbereitet."),
                ("Grenze", "Die Stellungnahme ersetzt weder die gerichtliche Verguetungsfestsetzung noch die Zustimmung zur Schlussverteilung."),
            ],
            2,
            issuer="Glaeubigerausschuss Klangbogen",
            signatory="Kunigunde Woelfel, Vorsitzende des Glaeubigerausschusses",
        ),
        make_simple_pdf(
            EVIDENCE_DIR / "09_abschlussreifevermerk_2026-12-05.pdf",
            "Sachstandsvermerk zur Abschlussreife",
            date(2026, 12, 5),
            [
                ("Vermoegen", "Saemtliche bekannten Vermoegensgegenstaende sind verwertet; Aus- und Absonderungsrechte sind abgerechnet."),
                ("Ansprueche", "Aktivprozesse, Anfechtungs- und Haftungsvorgaenge sind beendet. Zahlungseingaenge und Kosten sind gebucht."),
                ("Kostenfestsetzung", "Der in der Abrechnung vom 18.09.2024 noch offene Antrag ueber 1.284,30 EUR wurde durch Beschluss des Landgerichts Bamberg vom 14.01.2025, 2 O 317/17 KfH, zurueckgewiesen. Der Beschluss wurde am 17.01.2025 zugestellt; die Fristenkontrolle vom 18.02.2025 weist kein Rechtsmittel aus. Mangels Zahlung entstand keine Kontenbuchung. Der Vorgang ist abgeschlossen."),
                ("Passiva", f"Die ordentlichen festgestellten Forderungen betragen {euro(FINAL_CLAIMS)}. Die Tabelle ist fuer die Schlussrechnung eingefroren."),
                ("Naechstes Produkt", "Schlussbericht, Schlussrechnung und Schlussverzeichnis sind als getrennte fuehrende Fassungen zu erstellen. Freigabe, Einreichung und Verteilung bleiben offene Gates."),
            ],
            2,
            signatory=ADMINISTRATOR,
        ),
        make_simple_pdf(
            EVIDENCE_DIR / "10_kontenabstimmung_2026-12-05.pdf",
            "Kontenabstimmung fuer die Schlussrechnung",
            date(2026, 12, 5),
            [
                ("Bank", f"Bestaetigter Massebestand: {euro(FINAL_CASH)}."),
                ("Reserven", f"Dokumentierte Schlusskosten und Nachlaufreserven: {euro(FINAL_RESERVES)}."),
                ("Verteilung", f"Vorlaeufig verfuegbar: {euro(FINAL_DISTRIBUTION)}; vorlaeufige Quote auf {euro(FINAL_CLAIMS)}: {str(FINAL_QUOTA).replace('.', ',')} Prozent."),
                ("Nachtraeglicher Steuerkontenabgleich", "Die im Steuerbescheid vom 15.09.2026 festgesetzten Zinsen von 5.505,16 EUR wurden am 28.10.2026 gutgeschrieben. Dieser Vorgang ist als Zinsgutschrift im Kontenjournal des letzten Berichtszeitraums erfasst."),
                ("Kontrollstatus", "Bank, Periodenrechnung, Kontenjournal und Quotenblatt stimmen rechnerisch ueberein. Gerichtliche Festsetzungen bleiben abzuwarten."),
            ],
            2,
            signatory=f"{CASE_WORKER}; gegengeprueft durch {ADMINISTRATOR}",
        ),
        make_simple_pdf(
            EVIDENCE_DIR / "11_aktenvermerk_steuerkonto_2026-10-29.pdf",
            "Interner Aktenvermerk zum Steuerkonto",
            date(2026, 10, 29),
            [
                ("Anlass", "Fortschreibung des Steuer- und Rechtsbehelfsstatus nach dem Aenderungsbescheid vom 15.09.2026."),
                ("Kontenabgleich", "Die Erstattung von 11.698,47 EUR ist mit Wertstellung zum 22.06.2026 belegt. Die im Bescheid festgesetzten Zinsen von 5.505,16 EUR sind am 28.10.2026 auf dem Massekonto eingegangen."),
                ("Post- und Fristenkontrolle", "Die bis zum 29.10.2026 gefuehrte Posteingangs- und Fristenkontrolle weist keinen aktenkundigen Rechtsbehelf aus. Der Vermerk gibt ausschliesslich den internen Aktenstand wieder; eine amtliche Bestandskraftbescheinigung wird nicht behauptet."),
                ("Buchung", "Die Zinsgutschrift wird mit dem Wertstellungstag 28.10.2026 im Kontenjournal des letzten Berichtszeitraums erfasst. Bescheid, Bankumsatz und Buchung bleiben getrennte Belege."),
            ],
            signatory=CASE_WORKER,
        ),
        make_simple_pdf(
            EVIDENCE_DIR / "12_wirtschaftlichkeitspruefung_landbuehne_2021-07-12.pdf",
            "Wirtschaftlichkeitspruefung Vergleich Landbuehne Nord",
            date(2021, 7, 12),
            [
                ("Ausgangsforderung", "Die Masse verfolgt eine offene Schlussrate von 49.870,59 EUR. Die Projektgesellschaft wendet eine Vertragsstrafe und Nachbesserungskosten von zusammen 18.400,00 EUR ein."),
                ("Beweislage", "Abnahmeprotokoll und technische Dokumentation tragen den Werklohn im Grundsatz. Unsicher bleiben die Reichweite der vorbehaltenen Maengel und die Aufrechenbarkeit der Vertragsstrafe."),
                ("Fortfuehrungsszenario", "Als interner Arbeitswert werden eine Durchsetzungswahrscheinlichkeit von 65 Prozent, weitere Prozess- und Gutachterkosten von 9.600,00 EUR sowie eine Dauer von zwoelf bis achtzehn Monaten angesetzt. Daraus folgt ein risikogewichteter Nettoarbeitswert von 22.815,88 EUR."),
                ("Vergleichsszenario", "Der angebotene Zahlbetrag von 35.620,59 EUR ist bis 19.07.2021 zahlbar. Nach noch erwarteten Vollzugskosten von 1.250,00 EUR verbleibt ein Nettozufluss von 34.370,59 EUR."),
                ("Empfehlung", "Der Vergleich ist wirtschaftlich vorzugswuerdig, wenn die Erledigung auf das Projekt Landbuehne Nord begrenzt bleibt, die Zahlung kurzfristig faellig wird und die Masse bis zum vollstaendigen Eingang keine weitergehenden Rechte aufgibt."),
            ],
            2,
            signatory=ADMINISTRATOR,
        ),
        make_simple_pdf(
            EVIDENCE_DIR / "13_glaeubigerausschuss_zustimmung_landbuehne_2021-07-13.pdf",
            "Zustimmung des Glaeubigerausschusses zum Landbuehne-Vergleich",
            date(2021, 7, 13),
            [
                ("Teilnehmende", "Kunigunde Woelfel als Vorsitzende, Friedbert Boehlein als Lieferantenvertreter und Giselher Ruckdeschel als Arbeitnehmervertreter; Protokoll: Philipp Joens."),
                ("Unterlagen", "Geprueft wurden die Wirtschaftlichkeitsrechnung vom 12.07.2021, die Schlussrechnung, das Abnahmeprotokoll, die Einwendungen der Projektgesellschaft und der Vergleichsentwurf."),
                ("Beschluss", "Der Glaeubigerausschuss stimmt dem Vergleich ueber 35.620,59 EUR einstimmig zu. Die Zustimmung gilt unter der Bedingung, dass der Betrag spaetestens am 19.07.2021 faellig ist und die Erledigung erst mit vollstaendigem Zahlungseingang eintritt."),
                ("Vollzugskontrolle", "Vergleichsschluss, Faelligkeit und Zahlungseingang sind in getrennten Belegen zu dokumentieren. Bei ausbleibender Zahlung ist unverzueglich ueber die Fortsetzung des Rechtsstreits zu entscheiden."),
            ],
            2,
            issuer="Glaeubigerausschuss Klangbogen",
            signatory="Kunigunde Woelfel, Vorsitzende; Friedbert Boehlein; Giselher Ruckdeschel",
        ),
        make_simple_pdf(
            EVIDENCE_DIR / "14_glaeubigerausschuss_zustimmung_d-und-o_2024-04-04.pdf",
            "Zustimmung des Glaeubigerausschusses zum D-und-O-Vergleich",
            date(2024, 4, 4),
            [
                ("Entscheidungsgrundlage", "Geprueft wurden Zwischenbericht 16, Mediationsvorschlag, Deckungseinwendungen, der Stand des Parallelverfahrens und die Nettovergleichsrechnung vom 02.04.2024."),
                ("Abwaegung", "Beruecksichtigt wurden Prozessdauer, weitere Gutachter- und Rechtskosten, die wirtschaftliche Leistungsfaehigkeit des ehemaligen Geschaeftsfuehrers, Deckungsrisiken sowie das Verbot einer Doppelbefriedigung."),
                ("Beschluss", "Der Glaeubigerausschuss stimmt einem Gesamtvergleich von 46.763,18 EUR zu. Vorgesehen sind 13.141,47 EUR als erste Rate und 33.621,71 EUR als zweite Rate. Ein Forderungsverzicht darf erst nach vollstaendigem Eingang beider Raten wirksam werden."),
                ("Kontrolle", "Die Anmeldung im Parallelverfahren bleibt bis zur vollstaendigen Zahlung bestehen. Jeder Eingang ist gesondert zu buchen; eine Doppelbefriedigung ist anzurechnen."),
            ],
            2,
            issuer="Glaeubigerausschuss Klangbogen",
            signatory="Kunigunde Woelfel, Vorsitzende; Friedbert Boehlein; Giselher Ruckdeschel",
        ),
        make_simple_pdf(
            EVIDENCE_DIR / "15_vergleich_d-und-o_2024-04-05.pdf",
            "D-und-O-Vergleich",
            date(2024, 4, 5),
            [
                ("Parteien", f"{DEBTOR}, vertreten durch die Insolvenzverwalterin, Hinnerk Bamberger und Frankenwacht Vermoegensschaden-Haftpflicht AG."),
                ("Gesamtbetrag", "Zur vergleichsweisen Beendigung des Organhaftungs- und Deckungskomplexes werden insgesamt 46.763,18 EUR an die Masse gezahlt."),
                ("Erste Rate", "13.141,47 EUR sind bis zum 30.04.2024 faellig."),
                ("Zweite Rate", "33.621,71 EUR sind bis zum 31.10.2024 faellig."),
                ("Parallelverfahren", "Die Forderungsanmeldung gegen Hinnerk Bamberger bleibt bis zur vollstaendigen Zahlung beider Raten aufrechterhalten. Zahlungen werden angerechnet; eine Doppelbefriedigung ist ausgeschlossen."),
                ("Erledigung", "Die wechselseitige Erledigung wird erst mit vollstaendigem Eingang von 46.763,18 EUR wirksam. Bis dahin bleiben die vereinbarten Sicherungs- und Fortsetzungsrechte bestehen."),
                ("Freigabe", "Der Glaeubigerausschuss hat dem Vergleich am 04.04.2024 zugestimmt."),
            ],
            3,
            issuer="Vergleichsparteien Klangbogen, Bamberger und Frankenwacht",
            signatory="Dr. Mechthild Karg, Insolvenzverwalterin; Hinnerk Bamberger; Dr. Ylva Thalhammer, Prokuristin der Frankenwacht Vermoegensschaden-Haftpflicht AG",
        ),
    ]
    return evidence


def make_mail(path: Path, sent: datetime, sender: str, recipient: str, subject: str, body: str, attachments: list[Path]) -> Path:
    message = EmailMessage(policy=SMTP)
    message["From"] = sender
    message["To"] = recipient
    localized_sent = sent.replace(tzinfo=BERLIN_TIME)
    message["Date"] = localized_sent.strftime("%a, %d %b %Y %H:%M:%S %z")
    message["Message-ID"] = f"<{path.stem}.{sent.strftime('%Y%m%d%H%M%S')}@klangbogen.test.invalid>"
    message["Subject"] = subject
    message.set_content(body)
    for attachment in attachments:
        data = attachment.read_bytes()
        if attachment.suffix.lower() == ".pdf":
            maintype, subtype = "application", "pdf"
        elif attachment.suffix.lower() == ".xlsx":
            maintype, subtype = "application", "vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        else:
            maintype, subtype = "application", "octet-stream"
        message.add_attachment(data, maintype=maintype, subtype=subtype, filename=attachment.name)
    message.set_boundary(f"----=_Klangbogen_{path.stem}_{sent.strftime('%Y%m%d%H%M%S')}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(message.as_bytes())
    return path


def apply_workbook_print_profile() -> None:
    """Ergaenzt A4-Querformat und einspaltige Druckbreite im nativen Rechenwerk."""
    if not WORKBOOK.is_file():
        raise RuntimeError(f"Rechenwerk fehlt: {WORKBOOK}")
    with zipfile.ZipFile(WORKBOOK) as archive:
        workbook_xml = archive.read("xl/workbook.xml").decode("utf-8")
        if "_xlnm.Print_Area" in workbook_xml:
            if workbook_xml.count("_xlnm.Print_Area") != len(WORKBOOK_PRINT_AREAS):
                raise RuntimeError("Druckbereiche des Rechenwerks sind unvollstaendig")
            for index in range(1, len(WORKBOOK_PRINT_AREAS) + 1):
                sheet_xml = archive.read(f"xl/worksheets/sheet{index}.xml").decode("utf-8")
                for marker in ('fitToPage="1"', 'orientation="landscape"', 'fitToWidth="1"'):
                    if marker not in sheet_xml:
                        raise RuntimeError(f"Druckprofil fehlt in Tabellenblatt {index}: {marker}")
            return

    temporary = tempfile.NamedTemporaryFile(
        prefix=f".{WORKBOOK.stem}-", suffix=".xlsx", dir=WORKBOOK.parent, delete=False
    )
    temporary_path = Path(temporary.name)
    temporary.close()
    try:
        with zipfile.ZipFile(WORKBOOK, "r") as source, zipfile.ZipFile(
            temporary_path, "w", zipfile.ZIP_DEFLATED
        ) as target:
            for info in source.infolist():
                data = source.read(info.filename)
                if info.filename.startswith("xl/worksheets/sheet") and info.filename.endswith(".xml"):
                    value = data.decode("utf-8")
                    value = value.replace(
                        '<x:worksheet xmlns:x="http://schemas.openxmlformats.org/spreadsheetml/2006/main">',
                        '<x:worksheet xmlns:x="http://schemas.openxmlformats.org/spreadsheetml/2006/main">'
                        '<x:sheetPr><x:pageSetUpPr fitToPage="1" autoPageBreaks="0" /></x:sheetPr>',
                        1,
                    )
                    value = value.replace(
                        '<x:pageMargins left="0.7" right="0.7" top="0.75" bottom="0.75" header="0.3" footer="0.3" />',
                        '<x:printOptions horizontalCentered="1" verticalCentered="0" />'
                        '<x:pageMargins left="0.25" right="0.25" top="0.45" bottom="0.45" header="0.2" footer="0.2" />'
                        '<x:pageSetup paperSize="9" orientation="landscape" fitToWidth="1" fitToHeight="0" '
                        'blackAndWhite="0" draft="0" />',
                        1,
                    )
                    if 'orientation="landscape"' not in value:
                        raise RuntimeError(f"Druckprofil konnte nicht gesetzt werden: {info.filename}")
                    data = value.encode("utf-8")
                elif info.filename == "xl/workbook.xml":
                    value = data.decode("utf-8")
                    names: list[str] = []
                    for index, (sheet_name, print_area, title_rows) in enumerate(WORKBOOK_PRINT_AREAS):
                        escaped = sheet_name.replace("'", "''")
                        names.append(
                            f'<x:definedName name="_xlnm.Print_Area" localSheetId="{index}">'
                            f"'{escaped}'!{print_area}</x:definedName>"
                        )
                        if title_rows:
                            names.append(
                                f'<x:definedName name="_xlnm.Print_Titles" localSheetId="{index}">'
                                f"'{escaped}'!{title_rows}</x:definedName>"
                            )
                    value = value.replace(
                        "</x:workbook>",
                        "<x:definedNames>" + "".join(names) + "</x:definedNames></x:workbook>",
                        1,
                    )
                    data = value.encode("utf-8")
                target.writestr(info, data)
        temporary_path.replace(WORKBOOK)
    finally:
        temporary_path.unlink(missing_ok=True)


def make_correspondence() -> list[Path]:
    reports = [report_filename(index + 1, value) for index, value in enumerate(REPORT_DATES)]
    mails = [
        make_mail(
            MAIL_DIR / "01_uebersendung_zwischenbericht_01.eml",
            datetime(2016, 5, 28, 10, 14),
            "m.karg@karg-endres.example", "insolvenzabteilung@ag-bamberg.example",
            f"{CASE_NUMBER} - Zwischenbericht Nr. 01",
            "Sehr geehrte Damen und Herren,\n\nanbei uebersende ich den ersten turnusmaessigen Zwischenbericht. Bitte bestaetigen Sie den Eingang.\n\nMit freundlichen Gruessen\nDr. Mechthild Karg",
            [reports[0]],
        ),
        make_mail(
            MAIL_DIR / "02_rueckfrage_gutachten_zwischenbericht_04.eml",
            datetime(2017, 11, 29, 9, 32),
            "insolvenzabteilung@ag-bamberg.example", "m.karg@karg-endres.example",
            f"{CASE_NUMBER} - Gutachtenvorschuss und Bericht Nr. 04",
            "Sehr geehrte Frau Dr. Karg,\n\nbitte teilen Sie nach Eingang des Gutachtens mit, ob sich der Vergleichskorridor aendert. Der Bericht ist zur Akte genommen.\n\nMit freundlichen Gruessen\nGeschaeftsstelle",
            [reports[3]],
        ),
        make_mail(
            MAIL_DIR / "03_vergleich_landbuehne.eml",
            datetime(2021, 7, 15, 14, 8),
            "philipp.joens@karg-endres.example", "ausschuss@klangbogen-verfahren.example",
            "Vollzug Vergleich Landbuehne Nord",
            "Guten Tag,\n\nder Vergleich ist protokolliert. Die Zahlung wird erst nach Eingang im Massekonto als realisierter Zufluss fortgeschrieben. Die Vereinbarung ist beigefuegt.\n\nFreundliche Gruesse\nPhilipp Joens",
            [EVIDENCE_DIR / "05_vergleich_landbuehne_2021-07-14.pdf"],
        ),
        make_mail(
            MAIL_DIR / "04_tabellennachweise_zwischenbericht_13.eml",
            datetime(2022, 5, 23, 16, 41),
            "m.karg@karg-endres.example", "insolvenzabteilung@ag-bamberg.example",
            f"{CASE_NUMBER} - Zwischenbericht Nr. 13 und Nachweiskonvolut",
            "Sehr geehrte Damen und Herren,\n\nder Bericht enthaelt das angeforderte Nachweiskonvolut. Die 42 Nachweisseiten sind Bestandteil der Berichtsdatei und beziehen sich ausschliesslich auf den damaligen Stichtag.\n\nMit freundlichen Gruessen\nDr. Mechthild Karg",
            [reports[12]],
        ),
        make_mail(
            MAIL_DIR / "05_prozesskostenabgleich.eml",
            datetime(2024, 9, 19, 11, 3),
            "veit.zink@rechnungshof.example", "philipp.joens@karg-endres.example",
            "Prozesskostenabgleich Klangbogen",
            "Guten Morgen Herr Joens,\n\ndie Kosten sind nach Vorgaengen getrennt. Eine kleine Kostenfestsetzung ist noch offen und darf im laufenden Bericht nicht als erledigt bezeichnet werden.\n\nViele Gruesse\nVeit Zink",
            [EVIDENCE_DIR / "06_prozesskostenabrechnung_2024-09-18.pdf"],
        ),
        make_mail(
            MAIL_DIR / "06_uebersendung_zwischenbericht_21.eml",
            datetime(2026, 6, 5, 12, 20),
            "m.karg@karg-endres.example", "insolvenzabteilung@ag-bamberg.example",
            f"{CASE_NUMBER} - Zwischenbericht Nr. 21",
            "Sehr geehrte Damen und Herren,\n\nder Bericht stellt den letzten Beleglauf dar. Schlussreife wird noch nicht abschliessend behauptet; Banknachweis und Freigabe fehlen.\n\nMit freundlichen Gruessen\nDr. Mechthild Karg",
            [reports[20]],
        ),
        make_mail(
            MAIL_DIR / "07_uebersendung_zwischenbericht_22.eml",
            datetime(2026, 11, 28, 15, 4),
            "m.karg@karg-endres.example", "insolvenzabteilung@ag-bamberg.example",
            f"{CASE_NUMBER} - Zwischenbericht Nr. 22 und Schlussberichtsanlass",
            "Sehr geehrte Damen und Herren,\n\nanbei uebersende ich den Zwischenbericht Nr. 22. Er stellt die Abschlussreife fest und kuendigt die gesonderte Vorlage von Schlussbericht, Schlussrechnung und Schlussverzeichnis an.\n\nMit freundlichen Gruessen\nDr. Mechthild Karg",
            [reports[21]],
        ),
        make_mail(
            MAIL_DIR / "08_interne_uebergabe_schlussbericht.eml",
            datetime(2026, 12, 5, 17, 18),
            "philipp.joens@karg-endres.example", "m.karg@karg-endres.example",
            "Klangbogen - Unterlagen fuer den Schlussbericht",
            "Guten Abend Frau Dr. Karg,\n\nBankbestaetigung, Tabellenstand, Kontenabstimmung und Rechenwerk sind beigefuegt beziehungsweise im Aktenordner verknuepft. Offen bleiben Ihre namentliche Freigabe und die spaeteren gerichtlichen Gates.\n\nFreundliche Gruesse\nPhilipp Joens",
            [
                EVIDENCE_DIR / "03_bankbestaetigung_2026-11-30.pdf",
                EVIDENCE_DIR / "07_tabellenauszug_2026-11-30.pdf",
                EVIDENCE_DIR / "10_kontenabstimmung_2026-12-05.pdf",
                WORKBOOK,
            ],
        ),
    ]
    return mails


def make_text_files() -> list[Path]:
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    overview = WORK_DIR / "00_verfahrensdaten.txt"
    overview.write_text(
        textwrap.dedent(f"""
        VERFAHRENSDATEN

        Gericht: {COURT}
        Aktenzeichen: {CASE_NUMBER}
        Schuldnerin: {DEBTOR}, Hainwerkstrasse 18, 96049 Bamberg
        Geschaeftsfeld: Entwicklung, Fertigung und Wartung modularer Buehnenhubwerke,
        Akustiksegel und Probenraumtechnik fuer Theater, Musikschulen und Veranstaltungshallen.
        Eroeffnung: {de_date(OPENING_DATE)}
        Insolvenzverwalterin: {ADMINISTRATOR}
        Sachbearbeitung: {CASE_WORKER}
        Erster Zwischenbericht: {de_date(REPORT_DATES[0])}
        Letzter Zwischenbericht: {de_date(REPORT_DATES[-1])}
        Anzahl Zwischenberichte: 22
        Kontostand letzter Stichtag: {euro(FINAL_CASH)}
        Festgestellte ordentliche Forderungen: {euro(FINAL_CLAIMS)}

        Die Personen-, Unternehmens-, Adress-, Konto- und Aktenzeichendaten sind synthetisch.
        """).strip() + "\n",
        encoding="utf-8",
    )
    task = WORK_DIR / "90_auftrag_schlussbericht.txt"
    task.write_text(
        textwrap.dedent(f"""
        AUFTRAG SCHLUSSBERICHT

        Erstellen Sie aus den 22 Zwischenberichten, den Belegen, der Korrespondenz und dem
        Rechenwerk einen ausformulierten Schlussbericht zum Stand 05.12.2026. Erstellen Sie
        Schlussrechnung und Schlussverzeichnis als getrennte Produkte. Pruefen Sie insbesondere:

        1. Ob der letzte Massebestand von {euro(FINAL_CASH)} belegt ist.
        2. Ob die Schlusskosten von {euro(FINAL_RESERVES)} vollstaendig und nicht doppelt sind.
        3. Ob die Verteilungsmasse von {euro(FINAL_DISTRIBUTION)} und die vorlaeufige Quote von
           {str(FINAL_QUOTA).replace('.', ',')} Prozent rechnerisch stimmen.
        4. Ob alle Aktivvorgaenge, Sicherheiten, Steuern und Tabellenwidersprueche beendet sind.
        5. Welche menschlichen und gerichtlichen Freigaben weiterhin fehlen.

        Erfinden Sie keine gerichtliche Zustimmung, Verguetungsfestsetzung, Zahlung oder Aufhebung.
        """).strip() + "\n",
        encoding="utf-8",
    )
    source_status = WORK_DIR / "91_belegstatus_schlussbericht.txt"
    source_status.write_text(
        textwrap.dedent("""
        BELEGSTATUS

        Fuehrende Berichtsserie: Zwischenberichte 01 bis 22.
        Fuehrende Rechenquelle: 95_verfahrensrechnung_und_schlussreife.xlsx.
        Fuehrender Banknachweis: Bankbestaetigung vom 30.11.2026.
        Fuehrender Tabellenstand: Tabellenauszug vom 30.11.2026.
        Kostenfestsetzung: Der am 18.09.2024 noch offene Antrag ueber 1.284,30 EUR ist im
        Zwischenbericht 19 und im Abschlussreifevermerk vom 05.12.2026 als ohne Zahlung
        abgeschlossener Vorgang fortgeschrieben.
        Offene Gates: namentliche Freigabe; Verguetungsfestsetzung; Gerichtskostenrechnung;
        gerichtliche Zustimmung zur Schlussverteilung; Auszahlungsvollzug; Aufhebung.
        """).strip() + "\n",
        encoding="utf-8",
    )
    return [overview, task, source_status]


def make_readme() -> Path:
    target = CASE / "README.md"
    target.write_text(
        f"""# Testakte Klangbogen Buehnen- und Probenraumtechnik GmbH

Diese Akte enthaelt 22 vollstaendig ausformulierte turnusmaessige Zwischenberichte aus einem langen Regelinsolvenzverfahren. Die Berichtsserie reicht vom 28. Mai 2016 bis zum 28. November 2026. Der letzte Bericht stellt die Abschlussreife fest; ein fertiger Schlussbericht ist bewusst nicht enthalten.

[Testakten-Uebersicht](../README.md) · [Download-Uebersicht](../../ASSET_INDEX.md) · [Repository-Start](../../README.md) · [Plugin](../../insolvenzverwaltung-berichtsersteller/README.md)

## 1. Downloads

> Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.
>
> This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Format | Link |
| --- | --- |
| Gesamt-PDF | [`gesamt-pdf/{SLUG}_gesamt.pdf`](gesamt-pdf/{SLUG}_gesamt.pdf) |
| Originaldateien | [`testakte-{SLUG}.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{RELEASE_TAG}/testakte-{SLUG}.zip) |
| Einzel-PDFs | [`testakte-{SLUG}-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/download/{RELEASE_TAG}/testakte-{SLUG}-einzelpdfs.zip) |

## 2. Fallkern

Die Klangbogen Buehnen- und Probenraumtechnik GmbH in Bamberg entwickelte, fertigte und wartete modulare Buehnenhubwerke, Akustiksegel und Probenraumtechnik. Nach der Verfahrenseroeffnung im November 2015 wurden Anlagevermoegen und einzelne Projekte abgewickelt. Kaufpreis-, Gewaehrleistungs-, Organhaftungs-, Versicherungs-, Steuer- und Tabellenfragen hielten das Verfahren bis 2026 offen.

| Merkmal | Stand |
| --- | --- |
| Gericht | {COURT} |
| Aktenzeichen | {CASE_NUMBER} |
| Eroeffnung | {de_date(OPENING_DATE)} |
| Zwischenberichte | 22 PDFs mit zusammen 233 Seiten |
| Berichtszeitraum | {de_date(REPORT_DATES[0])} bis {de_date(REPORT_DATES[-1])} |
| Massebestand letzter Bericht | {euro(FINAL_CASH)} |
| Festgestellte ordentliche Forderungen | {euro(FINAL_CLAIMS)} |
| Dokumentierte Reserven | {euro(FINAL_RESERVES)} |
| Rechnerische Verteilungsmasse | {euro(FINAL_DISTRIBUTION)} |
| Vorlaeufige Quote | {str(FINAL_QUOTA).replace('.', ',')} Prozent |

Alle Personen, Unternehmen, Adressen, Konten und Aktenzeichen sind frei erfunden. Die Test-IBAN ist nicht zahlungsfaehig.

## 3. Aufbau

- `zwischenberichte`: 22 einzelne gerichtliche Zwischenberichte. Die Berichte haben zusammen genau 233 Seiten. Bericht 13 enthaelt ein 42-seitiges Nachweiskonvolut; Bericht 22 ist ein kurzer Abschlussreifebericht ohne die sonst ueblichen Finanzanlagen.
- `belege`: 15 einzelne PDFs mit zusammen 30 Seiten: Eroeffnungs- und Berichtsanordnung, Vergleiche, Prozesskosten, Steuer-, Bank-, Tabellen-, Ausschuss- und Abschlussunterlagen.
- `korrespondenz`: acht echte EML-Dateien mit den jeweils benannten und bytegenau eingebetteten Anhaengen.
- `rechenwerk`: bearbeitbare Excel-Arbeitsmappe mit Periodenrechnung, Kontenjournal, Forderungen, Belegmatrix und Schlussreifekontrolle.
- `arbeitshinweise`: Verfahrensdaten, Belegstatus und der konkrete Auftrag zur Erstellung des Schlussberichts.

Die 37 Quell-PDFs sind außerdem in einem 263-seitigen Gesamt-PDF zusammengeführt. Einschließlich README, Rubrik und Gesamt-PDF umfasst der Aktenordner 52 Dateien.

## 4. Uebungsauftrag

Erstellen Sie aus dem Aktenbestand einen Schlussbericht, eine Schlussrechnung und ein Schlussverzeichnis. Pruefen Sie jeden Zahlensprung gegen Berichtsserie, Banknachweis und Rechenwerk. Arbeiten Sie mit dem Wissensstand des jeweiligen Zwischenberichts; spaetere Erkenntnisse duerfen fruehere Berichte nicht rueckwirkend veraendern.

Die namentliche Freigabe, Verguetungsfestsetzung, Gerichtskostenrechnung, gerichtliche Zustimmung zur Schlussverteilung, Auszahlung und Aufhebung sind offen. Ein erzeugter Entwurf darf diese Schritte nicht als vollzogen darstellen.
""",
        encoding="utf-8",
    )
    return target


def make_rubric() -> Path:
    data = {
        "name": "Insolvenzverwaltung Klangbogen Buehnentechnik Bamberg",
        "plugin": "insolvenzverwaltung-berichtsersteller",
        "checks": [
            {"id": "r01-readme", "check_type": "file_exists", "description": "README vorhanden", "path": "README.md"},
            {"id": "r02-gesamt-pdf", "check_type": "file_exists", "description": "Gesamt-PDF vorhanden", "path": f"gesamt-pdf/{SLUG}_gesamt.pdf"},
            {"id": "r03-dokumentumfang", "check_type": "working_file_count", "description": "Mindestens 44 exportierbare Arbeitsunterlagen", "min": 44},
            {"id": "r04-bericht-01", "check_type": "file_exists", "description": "Erster Zwischenbericht vorhanden", "path": "zwischenberichte/01_zwischenbericht_2016-05-28.pdf"},
            {"id": "r05-bericht-13", "check_type": "file_exists", "description": "Zwischenbericht mit Nachweiskonvolut vorhanden", "path": "zwischenberichte/13_zwischenbericht_2022-05-23.pdf"},
            {"id": "r06-bericht-22", "check_type": "file_exists", "description": "Letzter Zwischenbericht vorhanden", "path": "zwischenberichte/22_zwischenbericht_2026-11-28.pdf"},
            {"id": "r07-rechenwerk", "check_type": "file_exists", "description": "Bearbeitbares Rechenwerk vorhanden", "path": "rechenwerk/95_verfahrensrechnung_und_schlussreife.xlsx"},
            {"id": "r08-chronologie", "check_type": "human_review", "description": "Die 22 Berichte bilden eine lueckenlose Chronologie ohne spaetere Erkenntnisse in frueheren Berichten."},
            {"id": "r09-rechenkonsistenz", "check_type": "human_review", "description": f"Massebestand {FINAL_CASH}, Reserven {FINAL_RESERVES}, Verteilungsmasse {FINAL_DISTRIBUTION} und Forderungsbasis {FINAL_CLAIMS} stimmen ueberein."},
            {"id": "r10-gates", "check_type": "human_review", "description": "Der letzte Bericht benennt Schlussreife, ohne Freigabe, gerichtliche Zustimmung, Zahlung oder Aufhebung zu erfinden."},
        ],
    }
    target = CASE / "rubric.yaml"
    target.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=False), encoding="utf-8")
    return target


def make_combined_pdf() -> Path:
    target = COMBINED_DIR / f"{SLUG}_gesamt.pdf"
    COMBINED_DIR.mkdir(parents=True, exist_ok=True)
    writer = PdfWriter()
    sources = [
        *(report_filename(index + 1, value) for index, value in enumerate(REPORT_DATES)),
        *sorted(EVIDENCE_DIR.glob("*.pdf")),
    ]
    for source in sources:
        for page in PdfReader(source).pages:
            writer.add_page(page)
    with target.open("wb") as stream:
        writer.write(stream)
    return target


def validate() -> dict:
    if len(REPORT_DATES) != 22 or len(REPORT_PAGES) != 22 or len(EVENTS) != 22:
        raise RuntimeError("Die Berichtsserie muss exakt 22 Eintraege enthalten")
    if sum(REPORT_PAGES) != 233:
        raise RuntimeError("Die Berichtsserie muss exakt 233 Seiten enthalten")
    if (REPORT_DATES[-1] - REPORT_DATES[0]).days != 3836:
        raise RuntimeError("Der relative Gesamtzeitraum stimmt nicht")
    if (REPORT_DATES[0] - OPENING_DATE).days != 188:
        raise RuntimeError("Der Abstand vom Anfangsstand zum ersten Zwischenbericht stimmt nicht")
    if RECEIPTS[0] - EXPENSES[0] != CLOSING_BALANCES[0]:
        raise RuntimeError("Erste Periodenrechnung stimmt nicht")
    for index in range(1, 22):
        if CLOSING_BALANCES[index - 1] + RECEIPTS[index] - EXPENSES[index] != CLOSING_BALANCES[index]:
            raise RuntimeError(f"Periodenrechnung {index + 1} stimmt nicht")
    if KAUFPREISVERGLEICH > RECEIPTS[6]:
        raise RuntimeError("Kaufpreisvergleich uebersteigt die Einnahmen in Bericht 07")
    if LANDBUEHNE_VERGLEICH > RECEIPTS[11]:
        raise RuntimeError("Landbuehne-Vergleich uebersteigt die Einnahmen in Bericht 12")
    if D_AND_O_RATE_EINS + D_AND_O_RATE_ZWEI != D_AND_O_VERGLEICH:
        raise RuntimeError("D-und-O-Raten ergeben nicht den Gesamtvergleich")
    if D_AND_O_RATE_EINS != RECEIPTS[16] or D_AND_O_RATE_ZWEI != RECEIPTS[17]:
        raise RuntimeError("D-und-O-Raten stimmen nicht mit den Einnahmen der Berichte 17 und 18 ueberein")
    if REPORT_13_ANNEX_PAGES != 42 or "42 Nachweisseiten" not in EVENTS[12]["change"]:
        raise RuntimeError("Bericht 13 muss exakt 42 Nachweisseiten ausweisen")
    if "42 Nachmeldungen" in EVENTS[12]["change"]:
        raise RuntimeError("Bericht 13 darf die 42 Nachweisseiten nicht als 42 Nachmeldungen bezeichnen")
    if ESTABLISHED_CLAIMS[19] != Decimal("1759910.00") or ESTABLISHED_CLAIMS[20] != FINAL_CLAIMS:
        raise RuntimeError("Vorlaeufiger und endgueltiger Tabellenstand stimmen nicht")
    if bank_receipt_labels(21) != ("Steuererstattung", "Zinsgutschrift"):
        raise RuntimeError("Buchungstexte des letzten Berichtszeitraums stimmen nicht")
    if FINAL_DISTRIBUTION != Decimal("419000.07") or FINAL_QUOTA != Decimal("23.741726"):
        raise RuntimeError("Schlussrechnung stimmt nicht")
    if not WORKBOOK.is_file():
        raise RuntimeError(f"Rechenwerk fehlt: {WORKBOOK}")
    report_files = sorted(REPORT_DIR.glob("*.pdf"))
    if len(report_files) != 22:
        raise RuntimeError("Nicht exakt 22 Berichtspdfs")
    for index, report in enumerate(report_files):
        if len(PdfReader(report).pages) != REPORT_PAGES[index]:
            raise RuntimeError(f"Seitenzahl weicht ab: {report}")
    report_texts = [
        " ".join("\n".join(page.extract_text() or "" for page in PdfReader(report).pages).split())
        for report in report_files
    ]
    report_expectations = {
        6: ("30.000,00 EUR", "1.057,39 EUR"),
        10: ("Die Zahlung ist zum Berichtsstichtag ausstehend",),
        11: ("14.07.2021", "35.620,59 EUR"),
        12: ("exakt 42 Nachweisseiten", "Bestritten beziehungsweise reduziert", "Beleg-IDs", "weder um eine Gruppensumme noch um eine Zwischensumme"),
        15: ("46.763,18 EUR", "13.141,47 EUR", "33.621,71 EUR"),
        16: ("13.141,47 EUR", "33.621,71 EUR"),
        17: ("33.621,71 EUR", "46.763,18 EUR", "keine weitere Auszahlung"),
        19: ("vorlaeufige Tabellenstand", "1.759.910,00 EUR", "noch nicht eingefroren"),
        20: ("1.764.825,62 EUR", "Forderungsbasis ist eingefroren"),
        21: ("faktische Schlussreife", "unberuehrt", "Einreichung", "Verteilung", "Auszahlung", "Aufhebung"),
    }
    for index, phrases in report_expectations.items():
        missing = [phrase for phrase in phrases if phrase not in report_texts[index]]
        if missing:
            raise RuntimeError(f"Bericht {index + 1:02d} ohne Konsistenztext: {missing}")

    evidence_pages = {
        "01_eroeffnungsbeschluss_2015-11-22.pdf": 2,
        "02_berichtsanordnung_2015-12-15.pdf": 1,
        "03_bankbestaetigung_2026-11-30.pdf": 1,
        "04_steuerbescheid_2026-09-15.pdf": 2,
        "05_vergleich_landbuehne_2021-07-14.pdf": 3,
        "06_prozesskostenabrechnung_2024-09-18.pdf": 2,
        "07_tabellenauszug_2026-11-30.pdf": 3,
        "08_glaeubigerausschuss_stellungnahme_2026-12-02.pdf": 2,
        "09_abschlussreifevermerk_2026-12-05.pdf": 2,
        "10_kontenabstimmung_2026-12-05.pdf": 2,
        "11_aktenvermerk_steuerkonto_2026-10-29.pdf": 1,
        "12_wirtschaftlichkeitspruefung_landbuehne_2021-07-12.pdf": 2,
        "13_glaeubigerausschuss_zustimmung_landbuehne_2021-07-13.pdf": 2,
        "14_glaeubigerausschuss_zustimmung_d-und-o_2024-04-04.pdf": 2,
        "15_vergleich_d-und-o_2024-04-05.pdf": 3,
    }
    evidence_files = {path.name: path for path in EVIDENCE_DIR.glob("*.pdf")}
    if set(evidence_files) != set(evidence_pages):
        raise RuntimeError("Belegbestand weicht von den 15 erwarteten PDF-Belegen ab")
    for filename, pages in evidence_pages.items():
        if len(PdfReader(evidence_files[filename]).pages) != pages:
            raise RuntimeError(f"Belegseitenzahl weicht ab: {filename}")

    evidence_expectations = {
        "01_eroeffnungsbeschluss_2015-11-22.pdf": (COURT, ("Dr. Marielein Endres",)),
        "02_berichtsanordnung_2015-12-15.pdf": (COURT, ("Almut Eyrich",)),
        "03_bankbestaetigung_2026-11-30.pdf": ("Frankenbogen Bank eG", ("Veit Claassen",)),
        "04_steuerbescheid_2026-09-15.pdf": ("Finanzamt Bamberg", ("Ruprecht Pfrang",)),
        "05_vergleich_landbuehne_2021-07-14.pdf": ("Vergleichsparteien Klangbogen und Landbuehne Nord", ("Dr. Mechthild Karg", "Jost Thalhammer")),
        "06_prozesskostenabrechnung_2024-09-18.pdf": (ADMINISTRATOR, ("Philipp Joens",)),
        "07_tabellenauszug_2026-11-30.pdf": (ADMINISTRATOR, ("Philipp Joens",)),
        "08_glaeubigerausschuss_stellungnahme_2026-12-02.pdf": ("Glaeubigerausschuss Klangbogen", ("Kunigunde Woelfel",)),
        "09_abschlussreifevermerk_2026-12-05.pdf": (ADMINISTRATOR, ("Dr. Mechthild Karg",)),
        "10_kontenabstimmung_2026-12-05.pdf": (ADMINISTRATOR, ("Philipp Joens", "Dr. Mechthild Karg")),
        "11_aktenvermerk_steuerkonto_2026-10-29.pdf": (ADMINISTRATOR, ("Philipp Joens",)),
        "12_wirtschaftlichkeitspruefung_landbuehne_2021-07-12.pdf": (ADMINISTRATOR, ("Dr. Mechthild Karg",)),
        "13_glaeubigerausschuss_zustimmung_landbuehne_2021-07-13.pdf": ("Glaeubigerausschuss Klangbogen", ("Kunigunde Woelfel", "Friedbert Boehlein", "Giselher Ruckdeschel")),
        "14_glaeubigerausschuss_zustimmung_d-und-o_2024-04-04.pdf": ("Glaeubigerausschuss Klangbogen", ("Kunigunde Woelfel", "Friedbert Boehlein", "Giselher Ruckdeschel")),
        "15_vergleich_d-und-o_2024-04-05.pdf": ("Vergleichsparteien Klangbogen, Bamberger und Frankenwacht", ("Dr. Mechthild Karg", "Hinnerk Bamberger", "Dr. Ylva Thalhammer")),
    }
    for filename, (issuer, signatories) in evidence_expectations.items():
        reader = PdfReader(EVIDENCE_DIR / filename)
        lines = [line.strip() for line in (reader.pages[0].extract_text() or "").splitlines() if line.strip()]
        full_text = " ".join("\n".join(page.extract_text() or "" for page in reader.pages).split())
        if not lines or lines[0] != issuer:
            raise RuntimeError(f"Ausstellerkopf fehlt in erster PDF-Zeile: {filename}")
        for signatory in signatories:
            if signatory not in full_text:
                raise RuntimeError(f"Unterzeichnung fehlt: {filename}: {signatory}")
    tax_text = " ".join(
        "\n".join(page.extract_text() or "" for page in PdfReader(EVIDENCE_DIR / "04_steuerbescheid_2026-09-15.pdf").pages).split()
    )
    for phrase in ("22.06.2026", "11.698,47 EUR", "5.505,16 EUR", "am Ausstellungsdatum war dieser Betrag noch nicht gutgeschrieben", "gesonderten internen Aktenvermerk"):
        if phrase not in tax_text:
            raise RuntimeError(f"Steuerbeleg ohne Kontenjournalbezug: {phrase}")
    if any(phrase in tax_text for phrase in ("28.10.2026", "Rechtsbehelfsfrist ist abgelaufen", "Bestandskraft ist eingetreten", "Bestandskraftbescheinigung liegt")):
        raise RuntimeError("Steuerbescheid nimmt einen spaeteren Rechtsbehelfs- oder Kontenstatus vorweg")
    tax_memo_text = " ".join(
        "\n".join(page.extract_text() or "" for page in PdfReader(EVIDENCE_DIR / "11_aktenvermerk_steuerkonto_2026-10-29.pdf").pages).split()
    )
    for phrase in ("22.06.2026", "28.10.2026", "11.698,47 EUR", "5.505,16 EUR", "keinen aktenkundigen Rechtsbehelf", "amtliche Bestandskraftbescheinigung wird nicht behauptet"):
        if phrase not in tax_memo_text:
            raise RuntimeError(f"Steueraktenvermerk ohne spaeteren Nachweis: {phrase}")

    landbuehne_text = " ".join(
        "\n".join(page.extract_text() or "" for page in PdfReader(EVIDENCE_DIR / "05_vergleich_landbuehne_2021-07-14.pdf").pages).split()
    )
    for phrase in ("14.07.2021", "19.07.2021", "35.620,59 EUR", "nicht den tatsaechlichen Zahlungseingang", "Ob und wann der Betrag eingeht", "Dr. Mechthild Karg", "Jost Thalhammer"):
        if phrase not in landbuehne_text:
            raise RuntimeError(f"Landbuehne-Vergleich ohne Abschluss-, Zahlungs- oder Unterschriftsnachweis: {phrase}")
    if "Der Eingang am 19.07.2021 wird" in landbuehne_text:
        raise RuntimeError("Landbuehne-Vergleich nimmt einen spaeteren Zahlungseingang vorweg")
    landbuehne_economy_text = " ".join(
        "\n".join(page.extract_text() or "" for page in PdfReader(EVIDENCE_DIR / "12_wirtschaftlichkeitspruefung_landbuehne_2021-07-12.pdf").pages).split()
    )
    for phrase in ("49.870,59 EUR", "18.400,00 EUR", "22.815,88 EUR", "34.370,59 EUR", "Dr. Mechthild Karg"):
        if phrase not in landbuehne_economy_text:
            raise RuntimeError(f"Landbuehne-Wirtschaftlichkeitspruefung unvollstaendig: {phrase}")
    landbuehne_approval_text = " ".join(
        "\n".join(page.extract_text() or "" for page in PdfReader(EVIDENCE_DIR / "13_glaeubigerausschuss_zustimmung_landbuehne_2021-07-13.pdf").pages).split()
    )
    for phrase in ("35.620,59 EUR", "einstimmig", "vollstaendigem Zahlungseingang", "Kunigunde Woelfel"):
        if phrase not in landbuehne_approval_text:
            raise RuntimeError(f"Landbuehne-Ausschusszustimmung unvollstaendig: {phrase}")

    costs_text = " ".join(
        "\n".join(page.extract_text() or "" for page in PdfReader(EVIDENCE_DIR / "06_prozesskostenabrechnung_2024-09-18.pdf").pages).split()
    )
    for phrase in ("Status am 18.09.2024", "1.284,30 EUR", "noch nicht beschieden", "Philipp Joens"):
        if phrase not in costs_text:
            raise RuntimeError(f"Prozesskostenbeleg ohne stichtagsreinen Status: {phrase}")
    if "Folgezeitraum" in costs_text:
        raise RuntimeError("Prozesskostenbeleg nimmt einen Folgezeitraum vorweg")
    closing_readiness_text = " ".join(
        "\n".join(page.extract_text() or "" for page in PdfReader(EVIDENCE_DIR / "09_abschlussreifevermerk_2026-12-05.pdf").pages).split()
    )
    for phrase in ("1.284,30 EUR", "14.01.2025", "17.01.2025", "18.02.2025", "Mangels Zahlung entstand keine Kontenbuchung", "Vorgang ist abgeschlossen"):
        if phrase not in closing_readiness_text:
            raise RuntimeError(f"Abschlussreifevermerk schliesst die Kostenfestsetzung nicht belegt: {phrase}")

    d_and_o_approval_text = " ".join(
        "\n".join(page.extract_text() or "" for page in PdfReader(EVIDENCE_DIR / "14_glaeubigerausschuss_zustimmung_d-und-o_2024-04-04.pdf").pages).split()
    )
    d_and_o_settlement_text = " ".join(
        "\n".join(page.extract_text() or "" for page in PdfReader(EVIDENCE_DIR / "15_vergleich_d-und-o_2024-04-05.pdf").pages).split()
    )
    for label, text_value in (("Ausschusszustimmung", d_and_o_approval_text), ("Vergleich", d_and_o_settlement_text)):
        for phrase in ("46.763,18 EUR", "13.141,47 EUR", "33.621,71 EUR"):
            if phrase not in text_value:
                raise RuntimeError(f"D-und-O-{label} ohne konsistenten Betrag: {phrase}")
    combined = COMBINED_DIR / f"{SLUG}_gesamt.pdf"
    combined_pages = len(PdfReader(combined).pages)
    expected_combined = 233 + sum(len(PdfReader(path).pages) for path in EVIDENCE_DIR.glob("*.pdf"))
    if expected_combined != 263:
        raise RuntimeError(f"Berichte und 15 Belege muessen zusammen 263 Seiten ergeben, nicht {expected_combined}")
    if combined_pages != expected_combined:
        raise RuntimeError(f"Gesamt-PDF hat {combined_pages} statt {expected_combined} Seiten")
    from email import policy
    from email.parser import BytesParser
    from email.utils import parsedate_to_datetime
    mail_paths = sorted(MAIL_DIR.glob("*.eml"))
    if len(mail_paths) != 8:
        raise RuntimeError("Die Akte muss exakt acht EML-Dateien enthalten")
    message_ids: set[str] = set()
    for mail_path in mail_paths:
        message = BytesParser(policy=policy.default).parsebytes(mail_path.read_bytes())
        attachments = list(message.iter_attachments())
        if message.defects or not attachments:
            raise RuntimeError(f"Ungueltige E-Mail: {mail_path}")
        message_id = message.get("Message-ID", "")
        if not message_id.endswith("@klangbogen.test.invalid>") or message_id in message_ids:
            raise RuntimeError(f"Fehlende oder nicht eindeutige Message-ID: {mail_path}")
        message_ids.add(message_id)
        sent = parsedate_to_datetime(message["Date"])
        berlin_offset = sent.replace(tzinfo=None).replace(tzinfo=BERLIN_TIME).utcoffset()
        if sent.utcoffset() != berlin_offset:
            raise RuntimeError(f"Falsche Europe/Berlin-Zeitzone: {mail_path}")
        for attachment in attachments:
            candidates = list(CASE.rglob(attachment.get_filename()))
            if len(candidates) != 1 or candidates[0].read_bytes() != attachment.get_payload(decode=True):
                raise RuntimeError(f"E-Mail-Anlage weicht ab: {mail_path}, {attachment.get_filename()}")
    return {
        "reports": len(report_files),
        "report_pages": sum(REPORT_PAGES),
        "combined_pages": combined_pages,
        "final_cash": str(FINAL_CASH),
        "final_claims": str(FINAL_CLAIMS),
        "final_reserves": str(FINAL_RESERVES),
        "final_distribution": str(FINAL_DISTRIBUTION),
        "final_quota_percent": str(FINAL_QUOTA),
    }


def write_quality(created: list[Path], result: dict) -> Path:
    QUALITY_DIR.mkdir(parents=True, exist_ok=True)
    target = QUALITY_DIR / "klangbogen-zwischenberichte-akte.json"
    payload = {
        "schema_version": 1,
        "slug": SLUG,
        "plugin_version": PLUGIN_VERSION,
        "report_dates": [value.isoformat() for value in REPORT_DATES],
        "report_pages": list(REPORT_PAGES),
        "totals": result,
        "files": [
            {
                "path": path.relative_to(CASE).as_posix(),
                "size": path.stat().st_size,
                "sha256": sha256(path),
            }
            for path in sorted(created)
            if path.is_file() and path.is_relative_to(CASE)
        ],
    }
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return target


def build() -> dict:
    register_fonts()
    CASE.mkdir(parents=True, exist_ok=True)
    for directory in (REPORT_DIR, EVIDENCE_DIR, MAIL_DIR, WORK_DIR, COMBINED_DIR):
        if directory.exists():
            shutil.rmtree(directory)
        directory.mkdir(parents=True)
    created: list[Path] = []
    for index in range(22):
        created.append(make_report(index))
    created.extend(make_evidence())
    apply_workbook_print_profile()
    created.extend(make_correspondence())
    created.extend(make_text_files())
    created.append(make_readme())
    created.append(make_rubric())
    created.append(make_combined_pdf())
    result = validate()
    created.append(WORKBOOK)
    quality = write_quality(created, result)
    result["quality_manifest"] = quality.relative_to(ROOT).as_posix()
    result["source_files"] = len(created)
    return result


if __name__ == "__main__":
    print(json.dumps(build(), ensure_ascii=False, indent=2))
