#!/usr/bin/env python3
"""Erstellt die individuellen Bank- und Sachbelege der Familie Bergmann."""

from __future__ import annotations

import calendar
import csv
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
import json
from pathlib import Path
import sys
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfgen.canvas import Canvas

ROOT = Path(__file__).resolve().parent.parent
SLUG = "zugewinnausgleich-familie-bergmann-potsdam"
D = Decimal
CENT = D("0.01")
BANK = "Havelbogen Bank eG"
BANK_ADDRESS = "Privatkunden Potsdam · Berliner Straße 46 · 14467 Potsdam"
CONTACT = "Eike Sander · Telefon 0331 555 0148 · Servicezeichen HB-P-4426"
ACCOUNTS = {
    "Mara": {"owner": "Mara Bergmann", "number": "Privatkonto 4401", "opening": "15180.45"},
    "Jonas": {"owner": "Jonas Bergmann", "number": "Privatkonto 4402", "opening": "9240.18"},
    "Haushalt": {"owner": "Mara und Jonas Bergmann", "number": "Gemeinschaftskonto 4410", "opening": "6275.80"},
}
INK = colors.HexColor("#253A4A")
PALE = colors.HexColor("#EEF3F6")
BODY = ParagraphStyle("Text", fontName="Helvetica", fontSize=10, leading=14, spaceAfter=9)
SMALL = ParagraphStyle("Tabelle", parent=BODY, fontSize=8.5, leading=11, spaceAfter=0)
TITLE = ParagraphStyle("Titel", parent=BODY, fontName="Helvetica-Bold", fontSize=17, leading=21, spaceAfter=13)
HEAD = ParagraphStyle("Absender", parent=BODY, fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=INK)


def money(value):
    return f"{D(str(value)):,.2f}".replace(",", "x").replace(".", ",").replace("x", ".")


def rounded(value):
    return D(value).quantize(CENT, rounding=ROUND_HALF_UP)


def p(text, style=BODY):
    return Paragraph(escape(str(text)).replace("\n", "<br/>"), style)


def table(rows, widths, numeric=()):
    cells = [[p(value, SMALL) for value in row] for row in rows]
    t = Table(cells, colWidths=widths, repeatRows=1, hAlign="LEFT")
    commands = [("BACKGROUND", (0, 0), (-1, 0), PALE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("LINEBELOW", (0, 0), (-1, 0), .5, colors.HexColor("#9CACB7"))]
    for column in numeric:
        for row in range(1, len(cells)):
            cells[row][column] = p(rows[row][column], ParagraphStyle("Zahl", parent=SMALL, alignment=2))
    for row in range(2, len(rows), 2):
        commands.append(("BACKGROUND", (0, row), (-1, row), colors.HexColor("#F7F9FA")))
    t.setStyle(TableStyle(commands))
    return t


def pdf(path, sender, address, title, meta, parts):
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(path), pagesize=A4, rightMargin=46, leftMargin=46,
                            topMargin=42, bottomMargin=48, title=title, author=sender)
    story = [p(sender, HEAD), p(address, SMALL), Spacer(1, 20), p(title, TITLE), p(meta)]
    for part in parts:
        story.append(part if not isinstance(part, str) else p(part))
        if not isinstance(part, str):
            story.append(Spacer(1, 12))

    def footer(canvas, _):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#61717B"))
        canvas.drawString(46, 27, sender)
        canvas.drawRightString(A4[0] - 46, 27, f"Seite {canvas.getPageNumber()}")
        canvas.restoreState()

    doc.build(story, onFirstPage=footer, onLaterPages=footer,
              canvasmaker=lambda *a, **kw: Canvas(*a, **dict(kw, invariant=1)))


def csv_file(path, headers, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream, delimiter=";")
        writer.writerow(headers)
        writer.writerows(rows)


def transactions():
    result = {name: [] for name in ACCOUNTS}
    holidays = {"2025-04-18", "2025-04-21", "2025-05-01", "2025-05-29", "2025-06-09", "2025-10-03", "2025-12-25", "2025-12-26",
                "2026-01-01", "2026-04-03", "2026-04-06", "2026-05-01", "2026-05-14", "2026-05-25"}

    def add(who, when, partner, text, amount, reference):
        booked = date.fromisoformat(when)
        while booked.weekday() >= 5 or booked.isoformat() in holidays:
            booked += timedelta(days=1)
        when = booked.isoformat()
        if when <= "2026-07-08":
            result[who].append({"date": when, "partner": partner, "text": text,
                                "amount": D(str(amount)), "reference": reference})

    months = [(year, month) for year in (2025, 2026) for month in range(1, 13)
              if (2025, 4) <= (year, month) <= (2026, 7)]
    for year, month in months:
        ym = f"{year}-{month:02}"
        key = f"{year}{month:02}"
        # Gegenbuchungen eigener Überträge behalten denselben Referenzschlüssel.
        add("Mara", ym + "-02", "Mara und Jonas Bergmann", "Haushaltskonto / laufende Ausgaben", -2300, key + "-M-H")
        add("Haushalt", ym + "-02", "Mara Bergmann", "Übertrag Privatkonto 4401", 2300, key + "-M-H")
        add("Jonas", ym + "-03", "Mara und Jonas Bergmann", "Haus und Kinder / Dauerauftrag", -950, key + "-J-H")
        add("Haushalt", ym + "-03", "Jonas Bergmann", "Übertrag Privatkonto 4402", 950, key + "-J-H")
        if (year, month) >= (2025, 6):
            add("Jonas", ym + "-04", "Mara Bergmann", "Für Jule und Oskar / vereinbarter Abschlag", -780, key + "-J-M")
            add("Mara", ym + "-04", "Jonas Bergmann", "Für Jule und Oskar / vereinbarter Abschlag", 780, key + "-J-M")
        add("Mara", ym + "-05", "Havelbogen Bank eG", "Sparübertrag Tagesgeld 4421", -600, key + "-TG")
        add("Mara", ym + "-09", "Depotservice Havelbogen", "Fondssparplan D-8821 / Monatsrate", -300, key + "-DEP")
        add("Mara", ym + "-11", "Familienkasse", "Kindergeld Jule und Oskar", 510 if year == 2025 else 518, key + "-KG")
        add("Mara", ym + "-16", "HavelCard Abrechnung", f"Kartenabrechnung {month:02}/{year} / Mara", -(D(215) + D(month * 7) + D(".38")), key + "-KARTE")
        add("Mara", ym + "-21", "Waldsee Versicherung", "Pkw P-MB 418 / Monatsbeitrag", "-74.80", key + "-KFZ")
        add("Mara", ym + "-28", "Land Brandenburg", "Entgelt Personalnummer 048216", "4385.62", key + "-ENTGELT")
        add("Jonas", ym + "-02", "Bergmann Licht & Planung", "Privatentnahme Geschäftskonto 7712", 4700 + (month % 4) * 175, key + "-ENTNAHME")
        add("Jonas", ym + "-03", "Sven Hagedorn", "Miete Feuerbachstraße 9", -890, key + "-MIETE")
        add("Jonas", ym + "-06", "Ursula Bergmann", "Hilfe Haushalt und Pflege / Dauerauftrag", -380, key + "-OMA")
        add("Jonas", ym + "-12", "Krankenkasse", "Freiwillige Kranken- und Pflegeversicherung", "-612.44", key + "-KV")
        add("Jonas", ym + "-14", "Versorgungskasse", "Altersvorsorge Vertrag RV-62241", -260, key + "-RV")
        add("Jonas", ym + "-19", "HavelCard Abrechnung", f"Kartenabrechnung {month:02}/{year} / Jonas", -(D(195) + D(month * 11) + D(".72")), key + "-KARTE")
        add("Jonas", ym + "-24", "Geldautomat Potsdam", "Bargeldauszahlung / Karte endet 2208", -180, key + "-BAR")
        add("Haushalt", ym + "-05", BANK, "Annuität HD-2014-731", -1380, key + "-HD")
        add("Haushalt", ym + "-08", "Stadtwerke Potsdam", "Strom und Wärme / Abschlag 7318", -310, key + "-ENERGIE")
        add("Haushalt", ym + "-10", "Schulcatering Havelküche", "Jule / Oskar / Monatsabrechnung", "-124.60", key + "-ESSEN")
        add("Haushalt", ym + "-12", "Turnverein Bornim", "Beiträge Jule und Oskar", -48, key + "-SPORT")
        add("Haushalt", ym + "-15", "Telekommunikation", "Internet Kastanienweg 18", "-44.90", key + "-NETZ")
        add("Haushalt", ym + "-18", "Markt am Bornstedter Feld", "Kartenzahlung Haushalt", -(D(186) + D(month * 3) + D(".43")), key + "-MARKT1")
        add("Haushalt", ym + "-22", "Lebensmittelmarkt Potsdam", "Kartenzahlung Haushalt", -(D(149) + D(month * 4) + D(".16")), key + "-MARKT2")
        add("Haushalt", ym + "-26", "Waldsee Versicherung", "Wohngebäude / Monatsrate", "-39.80", key + "-GEB")
        add("Haushalt", ym + "-28", "Drogerie am Park", "Kartenzahlung / Haushalt und Schulbedarf", -(D(68) + D(month * 2) + D(".35")), key + "-DROGERIE")
        for who in ACCOUNTS:
            add(who, f"{ym}-{calendar.monthrange(year, month)[1]:02}", BANK, "Kontoführung / Monatsentgelt", "-6.90", key + "-GEB-" + who.upper())
    add("Haushalt", "2025-06-09", "Ferienhof Achterwasser", "Restzahlung Urlaub 12.07.-19.07.2025 / Buchung 25182", -1260, "REISE-25182")
    add("Haushalt", "2025-10-16", "Havel Sanitär", "Rechnung HS-251012 / Zirkulationspumpe", "-487.90", "HS-251012")
    add("Haushalt", "2026-05-12", "Jugendfahrt Sonnental", "Feriencamp Jule / Buchung 26-417", -420, "CAMP-26-417")
    add("Mara", "2026-05-18", "Mara und Jonas Bergmann", "Sondertilgung Haus / Übertrag aus Rücklage", -3500, "SONDER-202605")
    add("Haushalt", "2026-05-18", "Mara Bergmann", "Übertrag für Sondertilgung", 3500, "SONDER-202605")
    add("Haushalt", "2026-05-20", BANK, "Sondertilgung HD-2014-731", -3500, "HD-SONDER-202605")
    add("Jonas", "2026-06-10", "Havelmetall Edelmetalle", "Ankauf KM-26-610 / eine Münze", 3120, "KM-26-610")
    add("Jonas", "2026-06-16", "KontoKontor Digital GmbH", "Auszahlung Verkauf KK-260615-204", "1874.36", "KK-260615-204")
    for who, rows in result.items():
        balance = D(ACCOUNTS[who]["opening"])
        for row in sorted(rows, key=lambda row: (row["date"], row["reference"])):
            balance += row["amount"]
            row["balance"] = balance
            row["source"] = f"kontoauszuege/{who}_{row['date'][:7]}.pdf"
        rows.sort(key=lambda row: (row["date"], row["reference"]))
    return result


def bank_documents(folder, records):
    for who, rows in records.items():
        account = ACCOUNTS[who]
        csv_rows = [["2025-03-31", "2025-03-31", "VORTRAG", BANK, "Saldovortrag 31.03.2025", "0.00", account["opening"], f"belege/Saldenbestaetigung_2025-04-01.pdf"]]
        for row in rows:
            csv_rows.append([row["date"], row["date"], row["reference"], row["partner"], row["text"], row["amount"], row["balance"], row["source"]])
        csv_file(folder / "zahlenwerk" / f"Konto_{who}_2025_2026.csv",
                 ["Buchungstag", "Valuta", "Referenz", "Auftraggeber_Empfänger", "Buchungstext", "Betrag_EUR", "Saldo_EUR", "Belegdatei"], csv_rows)
        previous = D(account["opening"])
        for month in sorted({r["date"][:7] for r in rows}):
            items = [r for r in rows if r["date"].startswith(month)]
            year, m = map(int, month.split("-"))
            end = "08.07.2026" if month == "2026-07" else f"{calendar.monthrange(year, m)[1]:02}.{m:02}.{year}"
            grid = [["Buchung / Valuta", "Geschäftspartner / Referenz", "Buchungstext", "Betrag EUR", "Saldo EUR"]]
            grid += [[date.fromisoformat(r["date"]).strftime("%d.%m.%Y"), r["partner"] + "\n" + r["reference"], r["text"], money(r["amount"]), money(r["balance"])] for r in items]
            pdf(folder / "kontoauszuege" / f"{who}_{month}.pdf", BANK, BANK_ADDRESS,
                "Kontoumsätze" if month == "2026-07" else "Kontoauszug",
                f"{account['owner']} · {account['number']}\nZeitraum 01.{m:02}.{year} bis {end} · Auszug {m:02}/{year}\nAnfangssaldo: {money(previous)} EUR",
                [table(grid, [68, 118, 168, 72, 77], (3, 4)),
                 f"Endsaldo zum {end}: {money(items[-1]['balance'])} EUR. Summe Gutschriften: {money(sum((r['amount'] for r in items if r['amount'] > 0), D(0)))} EUR. Summe Belastungen: {money(-sum((r['amount'] for r in items if r['amount'] < 0), D(0)))} EUR.",
                 "Valuta entspricht bei den hier aufgeführten Buchungen dem Buchungstag. Der Auszug enthält gebuchte Umsätze, keine vorgemerkten Kartenreservierungen. Die Kontobezeichnung gibt die Inhaber laut Stammdaten wieder; Verwendungszwecke stammen vom jeweiligen Auftraggeber.", CONTACT])
            previous = items[-1]["balance"]
    # Am Trennungstag liegen keine Buchungen vor. Spätere Vorgänge bleiben getrennt.
    for day, balances in [("01.04.2025", [D(ACCOUNTS[w]["opening"]) for w in ACCOUNTS]),
                          ("08.07.2026", [records[w][-1]["balance"] for w in ACCOUNTS])]:
        pdf(folder / "belege" / f"Saldenbestaetigung_{'-'.join(reversed(day.split('.')))}.pdf", BANK, BANK_ADDRESS,
            "Bestätigung gebuchter Kontostände", f"Auskunft vom 18.08.2026 · angefragter Tag {day}\nAn Mara und Jonas Bergmann / Versand jeweils an die hinterlegte Anschrift",
            ["Sehr geehrte Frau Bergmann, sehr geehrter Herr Bergmann, auf Ihre gemeinsame Anfrage vom 12. August bestätigen wir aus dem Buchungsarchiv folgende Bestände. Am 1. April 2025 wurden auf den drei Konten keine Umsätze gebucht; der Tagesendstand entspricht daher dem Übertrag des Vortags. Die Auskunft zum 8. Juli 2026 betrifft den Tagesendbestand.",
             table([["Konto", "Inhaber", "Bestand EUR"]] + [[ACCOUNTS[w]["number"], ACCOUNTS[w]["owner"], money(value)] for w, value in zip(ACCOUNTS, balances)], [150, 250, 103], (2,)),
             "Tagesgeld, Depot, Geschäftskonto und Darlehenskonten sind nicht in diesen drei Kontosalden enthalten. Für diese Produkte erhalten Sie gesonderte Auskünfte. Eine Kontovollmacht verändert die hier angegebenen Inhaber nicht. Auf eine wirtschaftliche Zuordnung einzelner Überweisungen erstreckt sich diese Bankauskunft nicht.", "Mit freundlichen Grüßen\nEike Sander\nPrivatkundenbetreuung"])


def loan_documents(folder):
    balance = D("207860.00")
    rows = []
    for year, month in [(y, m) for y in (2025, 2026) for m in range(1, 13) if (2025, 4) <= (y, m) <= (2026, 7)]:
        when = f"{year}-{month:02}-05"
        interest = rounded(balance * D("0.0215") / 12)
        opening = balance
        extra = D(3500) if (year, month) == (2026, 5) else D(0)
        balance = balance + interest - 1380 - extra
        rows.append([when, opening, interest, D(1380), extra, balance, "belege/Darlehenskonto_HD-2014-731.pdf"])
    csv_file(folder / "zahlenwerk/Darlehensbewegungen_2025_2026.csv",
             ["Fälligkeit", "Anfang_EUR", "Zinsen_EUR", "Rate_EUR", "Sondertilgung_EUR", "Restkapital_EUR", "Belegdatei"], rows)
    pdf(folder / "belege/Darlehenskonto_HD-2014-731.pdf", BANK, BANK_ADDRESS, "Darlehenskonto HD-2014-731",
        "Mara und Jonas Bergmann · Kastanienweg 18, 14476 Potsdam\nKontoauskunft vom 18.08.2026 · Beide Kreditnehmer haften laut Vertrag gesamtschuldnerisch.",
        ["Ausgangskapital nach Buchung des 31. März 2025: 207.860,00 EUR. Gebundener Sollzins 2,15 Prozent jährlich; monatliche Annuität 1.380,00 EUR, jeweils zum 5. des Monats. Die nachstehende Kontenliste enthält die gebuchten Zins- und Tilgungsanteile. Die Sondertilgung von 3.500,00 EUR wurde am 20. Mai 2026 gesondert vereinnahmt; sie ist hier in der Mai-Zeile enthalten.",
         table([["Fälligkeit", "Vortrag EUR", "Zins EUR", "Rate EUR", "Zusätzlich EUR", "Rest EUR"]] + [[r[0]] + [money(v) for v in r[1:6]] for r in rows], [66, 93, 78, 78, 88, 100], (1, 2, 3, 4, 5)),
         f"Restkapital am 8. Juli 2026: {money(balance)} EUR. Die am 6. Juli gebuchte Rate zum Fälligkeitstag 5. Juli ist bereits berücksichtigt. Bis zum 8. Juli ist keine weitere Zahlung eingegangen. Das Restkapital ist kein Ablöseangebot; bei einer Ablösung wären taggenaue Zinsen und gegebenenfalls vertragliche Kosten gesondert zu ermitteln.",
         "Die eingetragene Grundschuld von 280.000,00 EUR zuzüglich dinglicher Nebenleistungen bleibt unverändert. Sie bildet nicht den aktuellen Rückzahlungsbetrag ab. Eine Entlassung eines Kreditnehmers aus der persönlichen Haftung wurde weder beantragt noch zugesagt. Für Fragen zum Konto steht Ihnen Eike Sander zur Verfügung."])
    return rows


def historic_and_property(folder):
    pdf(folder / "belege/Bankarchiv_2011_Mara.pdf", BANK, BANK_ADDRESS, "Auskunft aus dem Kontenarchiv",
        "Mara Bergmann, vormals Mara Kreuter · Anforderung 12.08.2026\nHistorischer Auskunftstag: 18.06.2011 · Ausfertigung 18.08.2026",
        ["Sehr geehrte Frau Bergmann, die am 18. Juni 2011 geführten Konten waren ausschließlich auf Ihren damaligen Namen Mara Kreuter eröffnet. Herr Bergmann war nicht Mitinhaber. Der 18. Juni war ein Samstag. Zwischen Abschluss des 17. Juni und Beginn des folgenden Bankarbeitstages sind keine weiteren Buchungen dokumentiert.",
         table([["Produkt", "Kontonummer", "Guthaben EUR"], ["Girokonto", "4401", "3.275,40"], ["Sparbuch", "4421", "18.450,00"]], [230, 150, 123], (2,)),
         "Für das Girokonto weisen die letzten Buchungen im Juni eine Entgeltzahlung von 2.140,85 EUR am 15. Juni und eine Kartenzahlung von 84,60 EUR am 16. Juni aus. Der Sparbuchstand stammt aus dem am 31. Mai nachgetragenen Guthaben; im Juni gab es weder Einzahlung noch Abhebung. Ein Depot bestand bei unserem Haus im Juni 2011 nicht.",
         "Die spätere Umstellung des Sparbuchs in Tagesgeld änderte die interne Produktnummer nicht. Fremdbankprodukte, Fahrzeuge oder private Verbindlichkeiten sind von dieser Archivauskunft nicht erfasst. Mit freundlichen Grüßen\nEike Sander"])
    pdf(folder / "belege/Bankarchiv_2011_Jonas.pdf", BANK, BANK_ADDRESS, "Auskunft aus dem Kontenarchiv",
        "Jonas Bergmann · Auskunftstag 18.06.2011 · erstellt am 18.08.2026",
        ["Sehr geehrter Herr Bergmann, nach Ihren Kontostammdaten waren Sie am genannten Tag alleiniger Inhaber des Privatkontos 4402 und des Geschäftskontos 7712. Das Geschäftskonto trug den Zusatz Bergmann Licht & Planung. Es wird für ein Einzelunternehmen geführt. Die Beträge sind keine Bilanz und enthalten keine Bewertung des Betriebs.",
         table([["Produkt", "Kontonummer", "Stand EUR"], ["Privatkonto", "4402", "5.480,20"], ["Geschäftskonto", "7712", "16.820,00"], ["Betriebsmitteldarlehen", "BD-2009-14", "-14.800,00"]], [230, 150, 123], (2,)),
         "Der Darlehenssaldo ist separat aufgeführt und nicht vom Geschäftskontoguthaben abgezogen. Die letzte Ratenbuchung erfolgte am 15. Juni. Das Kreditkonto wies am 18. Juni keine offenen Raten aus. Die für das Geschäftskonto eingeräumte Linie von 10.000,00 EUR war nicht in Anspruch genommen und ist kein vorhandenes Guthaben.",
         "Die beigefügten Kontoinformationen ersetzen keine Auskunft über Forderungen aus erbrachten Planungsleistungen. Auf frühere private Darlehen mit Angehörigen erstreckt sich unser Archiv nicht. Mit freundlichen Grüßen\nEike Sander"])
    pdf(folder / "belege/Studienkredit_Mara_2011.pdf", "Bildungsfinanzierung Nord", "Kreditservice · Sophienstraße 18 · 30159 Hannover", "Darlehenskonto SK-2004-418",
        "Mara Kreuter · Kontoauskunft zum 18.06.2011 · Nachdruck 19.08.2026",
        ["Der Darlehensvertrag vom 4. Oktober 2004 wurde mit Frau Mara Kreuter geschlossen. Zum angefragten Stichtag beträgt das ausstehende Darlehenskapital 12.400,00 EUR. Ein Mitschuldner ist nicht verzeichnet. Die nächste planmäßige Rate von 180,00 EUR war am 1. Juli 2011 fällig.",
         table([["Datum", "Buchung", "Kapital EUR"], ["01.04.2011", "Stand nach Monatsrate", "12.858,20"], ["01.05.2011", "Stand nach Monatsrate", "12.705,91"], ["01.06.2011", "Stand nach Monatsrate", "12.552,88"], ["17.06.2011", "Zusätzliche Tilgung 152,88 EUR", "12.400,00"]], [93, 310, 100], (2,)),
         "Das Darlehen ist später am 2. Mai 2018 vollständig zurückgeführt worden. Die Bestätigung wird nach Archivdaten erteilt; sie enthält keine Kosten für den Abruf. Bei Rückfragen geben Sie bitte das Kontozeichen an.\nMit freundlichen Grüßen\nBeate König\nKreditverwaltung"])
    pdf(folder / "belege/Kaufvertrag_Haus_2014_Abschrift.pdf", "Notariat Dr. Sebastian Rahl", "Friedrich-Ebert-Straße 27 · 14467 Potsdam", "Kaufvertrag vom 16. Mai 2014",
        "Urkundenrolle 417/2014 · Textliche Abschrift der Vertragsbestimmungen\nVerkäufer: Henrik und Doris Stein · Käufer: Mara und Jonas Bergmann",
        ["1. Vertragsgegenstand\nVerkauft wird das Grundstück Kastanienweg 18, 14476 Potsdam, verzeichnet im Grundbuch von Bornim Blatt 2841, Flur 6, Flurstück 218/11, Gebäude- und Freifläche 486 Quadratmeter. Das Grundstück ist mit einem Einfamilienhaus bebaut. Die Käufer erwerben je einen hälftigen Miteigentumsanteil. Bewegliche Gegenstände werden nicht gesondert verkauft.",
         "2. Kaufpreis und Fälligkeit\nDer Kaufpreis beträgt 326.000,00 EUR. Er ist innerhalb von vierzehn Tagen nach Zugang der notariellen Fälligkeitsmitteilung zu zahlen, jedoch nicht vor dem 1. Juli 2014. Die Mitteilung setzt insbesondere die Eintragung der Auflassungsvormerkung und die Sicherstellung der Löschung nicht übernommener Belastungen voraus. Die Käufer schulden den Kaufpreis als Gesamtschuldner.",
         "3. Besitz und Lasten\nBesitz, Nutzungen und Lasten gehen nach vollständiger Kaufpreiszahlung über. Die Verkäufer bestätigen, dass keine Miet- oder Pachtverhältnisse bestehen. Der Übergabetermin wird unmittelbar zwischen den Beteiligten abgestimmt. Schlüssel und vorhandene Bauunterlagen sind bei der Übergabe auszuhändigen.",
         "4. Finanzierung und Grundpfandrechte\nZur Kaufpreisfinanzierung darf eine Grundschuld bis 280.000,00 EUR für die finanzierende Bank bestellt werden. Vor Eigentumsumschreibung darf sie nur insoweit verwertet werden, wie die Bank Zahlungen mit Tilgungswirkung auf den Kaufpreis erbracht hat. Persönliche Verbindlichkeiten der Verkäufer werden dadurch nicht übernommen.",
         "5. Kosten\nDie Kosten dieser Urkunde und ihres Vollzugs sowie die Grunderwerbsteuer tragen die Käufer. Kosten der Löschung nicht übernommener Verkäuferbelastungen tragen die Verkäufer. Die Beteiligten haben den vorgelesenen Text genehmigt. In der Urschrift sind die Unterschriften der vier Beteiligten und des Notars vermerkt. Diese Textabschrift gibt keine Unterschriften oder Siegel wieder."])
    pdf(folder / "belege/Immobilienbegehung_2026.pdf", "Havelraum Immobilienbewertung", "Ansprechpartnerin: Annika Seifert · Gutenbergstraße 21 · 14467 Potsdam", "Objektbesichtigung Kastanienweg 18",
        "Ortstermin 19.08.2026, 14:00 bis 15:35 Uhr · Bericht vom 25.08.2026\nAuftraggeber: Mara Bergmann · Auftrag HR-26-184",
        ["Besichtigt wurden Erdgeschoss, Obergeschoss, Keller und Garten. Das Haus wurde 1997 errichtet und 2014 von den heutigen Eigentümern übernommen. Wohnfläche nach vorgelegter Bauakte 142 Quadratmeter; Grundstück 486 Quadratmeter. Eine eigene Flächenvermessung ist nicht durchgeführt worden. Herr Jonas Bergmann war nicht anwesend, hatte aber vorab zwei Fotos aus März 2025 übersandt.",
         "Die Fenster stammen überwiegend aus dem Baujahr. Im Kellervorraum zeigt sich unterhalb des Lichtschachts eine Feuchtigkeitsspur. Frau Bergmann berichtet von Starkregen im Juni 2026. Ob Abdichtung, Lichtschacht oder Leitungsführung betroffen sind, ließ sich bei der Besichtigung nicht feststellen. Die Heizung ist aus 2011. Ein 2025 angekündigter Dachausbau wurde nach den vorgelegten Unterlagen nicht ausgeführt.",
         "Unter Berücksichtigung der am 8. Juli 2026 dokumentierten Objektmerkmale ergibt die vorläufige Marktpreisindikation eine Spanne von 495.000,00 bis 525.000,00 EUR. Die Spannweite hängt insbesondere von den nicht geöffneten Kellerabdichtungen und den energetischen Modernisierungskosten ab. Sie ist kein Verkehrswertgutachten. Fremdfinanzierungen werden nicht abgezogen.",
         "Die Maklernotiz aus April 2025 nannte nach Außenbesichtigung 470.000,00 bis 495.000,00 EUR. Ein rechnerischer Mittelwert dieser Spannen ist nicht Gegenstand des Auftrags. Für eine förmliche rückwirkende Wertermittlung werden die Bauakte, der Auszug aus der Kaufpreissammlung und die Unterlagen zur Kellerreparatur benötigt. Die zwei Angebote zur Abdichtung sind bislang nicht eingegangen.\nAnnika Seifert\nImmobilienökonomin"])
    pdf(folder / "belege/Erbschaft_Horst_Bank_2019.pdf", BANK, BANK_ADDRESS, "Nachlasskonto Horst Bergmann",
        "Erblasser: Horst Bergmann, Am Mühlenberg 7, 14547 Beelitz\nTodestag 12.02.2019 · Nachlasszeichen HB-N-19-083 · Auskunft 29.03.2019",
        ["Sehr geehrter Herr Bergmann, nach Vorlage des Erbscheins vom 7. März 2019, Amtsgericht Potsdam 52 VI 184/19, sind Sie als alleiniger Erbe in unseren Unterlagen erfasst. Wir bestätigen folgende Salden zum Todestag Ihres Vaters.",
         table([["Produkt", "Kennung", "Stand EUR"], ["Girokonto", "Nachlasskonto 5903", "4.200,00"], ["Grundstücksdarlehen", "GD-2012-118", "-8.500,00"]], [230, 160, 113], (2,)),
         "Das Darlehen war durch eine Grundschuld auf dem unbebauten Grundstück in Wittbrietzen gesichert. Am 25. März wurden 4.200,00 EUR aus dem Guthaben sowie 4.300,00 EUR aus Ihrer Überweisung eingesetzt und das Darlehen vollständig abgelöst. Weitere Darlehenszinsen für diesen Zeitraum wurden im vereinbarten Ablösebetrag nicht zusätzlich berechnet. Die Löschungsbewilligung wurde dem Notariat übersandt.",
         "Das Konto wurde anschließend geschlossen. Andere Vermögenswerte des Nachlasses sind bei uns nicht hinterlegt. Mit freundlichen Grüßen\nEike Sander"])
    pdf(folder / "belege/Grundstueck_Wittbrietzen_2019.pdf", "Landwert Märkische Zauche", "Sabine Lindau · Berliner Straße 24 · 14547 Beelitz", "Werteinschätzung unbebautes Grundstück",
        "12.04.2019 · Herr Jonas Bergmann · Objekt LW-19-118\nGemarkung Wittbrietzen, Flur 3, Flurstück 118/7, 612 Quadratmeter",
        ["Sehr geehrter Herr Bergmann, nach Ihrem Auftrag vom 19. März haben wir das Grundstück von der öffentlichen Straße aus besichtigt und die Katasterunterlagen eingesehen. Für den von Ihnen erfragten Zeitpunkt 12. Februar 2019 schätzen wir den erzielbaren Kaufpreis auf 31.000,00 EUR. Eine Bebauung war nicht vorhanden. Der Zaun ist beschädigt; im hinteren Bereich stehen mehrere verwilderte Obstbäume.",
         "Die Einschätzung setzt lastenfreies Eigentum voraus. Ein gesichertes Baurecht wird nicht zugesagt. Ein Hausanschluss auf dem Flurstück ist nicht nachgewiesen. Die vorhandene Zufahrt vom Wirtschaftsweg ist etwa drei Meter breit. Katastergröße und tatsächliche Grenzlage wurden nicht neu vermessen. Vor einem Verkauf sollte die Gemeinde zum Planungsstand befragt werden.",
         "Der Betrag enthält weder eine Bewertung persönlicher Darlehen noch Kosten des Erbfalls. Die Angaben sind eine Maklereinschätzung, keine förmliche Verkehrswertermittlung. Eine spätere Entwicklung des Grundstücksmarkts ist nicht eingerechnet.\nMit freundlichen Grüßen\nSabine Lindau"])
    pdf(folder / "belege/Grundstueck_Wittbrietzen_2026.pdf", "Landwert Märkische Zauche", "Sabine Lindau · Berliner Straße 24 · 14547 Beelitz", "Erneute Objektbesichtigung",
        "21.08.2026 · Objekt LW-26-118 · Bezug: Auskunft vom 12.04.2019\nAn Jonas Bergmann, Feuerbachstraße 9, 14471 Potsdam",
        ["Bei der Besichtigung am 17. August zeigte sich das Grundstück weiterhin unbebaut. Der alte Zaun ist teilweise entfernt. Eine schriftliche Baugenehmigung liegt uns nicht vor; nach telefonischer Auskunft der Gemeinde ist ein konkretes Vorhaben bisher nicht beantragt. Auf dem Grundstück befinden sich keine Solarmodule, Lagercontainer oder dauerhaft abgestellten Fahrzeuge.",
         "Für einen Verkauf unter den vorgefundenen Umständen sehen wir eine Preisspanne von 47.000,00 bis 53.000,00 EUR. Eine stichtagsbezogene Marktpreisindikation für den 8. Juli 2026 liegt bei 50.000,00 EUR. Die alte Grundschuld ist nach dem vorgelegten Löschungsvermerk seit dem 20. Mai 2019 gelöscht; auch die Ablösebestätigung der Bank lag in Kopie vor. Ein Verkauf hat nach Ihren Angaben nicht stattgefunden.",
         "Die Wertangabe vom 12. April 2019 und diese erneute Indikation beruhen auf unterschiedlichen Marktzeitpunkten. Erschließungskosten oder eine spätere Bauplanung sind nicht zugesagt. Falls eine verbindliche Bewertung erforderlich wird, können die vorhandenen Unterlagen an einen öffentlich bestellten Sachverständigen weitergegeben werden.\nMit freundlichen Grüßen\nSabine Lindau"])
    pdf(folder / "belege/Bestattung_Horst_2019.pdf", "Bestattungen am Mühlenberg", "Claudia Teichert · Poststraße 14 · 14547 Beelitz", "Rechnung B-190228-17",
        "Rechnungsdatum 28.02.2019 · an Jonas Bergmann\nBestattung Horst Bergmann, verstorben am 12.02.2019\nNachdruck mit Zahlungsvermerk vom 11.03.2019",
        ["Sehr geehrter Herr Bergmann, wir rechnen die von Ihnen am 14. Februar beauftragten Leistungen für die Beisetzung Ihres Vaters ab. Die Zeremonie fand am 25. Februar um 11:00 Uhr auf dem Friedhof Wittbrietzen statt. Die Grabstelle wurde nach Rücksprache mit Ihnen ausgewählt.",
         table([["Leistung", "Betrag EUR"], ["Abholung, Versorgung und Überführung", "1.180,00"], ["Sarg, Ausstattung und Trägerdienst", "1.390,00"], ["Organisation und Trauerfeier", "860,00"], ["Auslagen Friedhof und Grabstelle", "1.040,00"], ["Blumen und Drucksachen", "350,00"], ["Gesamtbetrag einschließlich enthaltener Umsatzsteuer", "4.820,00"]], [383, 120], (1,)),
         "Die genannten Beträge sind Endpreise; durchlaufende Friedhofsauslagen sind darin gesondert ausgewiesen. Zahlungseingang von Ihrem Privatkonto am 8. März 2019: 4.820,00 EUR. Der Rechnungsbetrag ist vollständig ausgeglichen. Eine laufende Grabpflege ist mit dieser Rechnung nicht vereinbart.\nMit freundlichen Grüßen\nClaudia Teichert"])


def investment_documents(folder):
    pdf(folder / "belege/Tagesgeld_Depot_Mara_2026.pdf", BANK, BANK_ADDRESS, "Tagesgeld- und Depotauskunft",
        "Mara Bergmann · Produkte 4421 und D-8821 · Auskunft vom 18.08.2026",
        ["Wir bestätigen die nachstehenden Bestände jeweils zum Tagesabschluss. Das Tagesgeldkonto und das Wertpapierdepot werden auf Ihren Namen allein geführt. Die monatlichen Sparüberträge aus dem Privatkonto 4401 sind im Kontoauszug als Umbuchung erkennbar.",
         table([["Produkt", "01.04.2025 EUR", "08.07.2026 EUR"], ["Tagesgeld 4421", "34.600,00", "44.562,48"], ["Depot D-8821 / Kurswert", "17.460,00", "23.480,00"]], [230, 136, 137], (1, 2)),
         "Zwischen den beiden Tagen wurden sechzehn Sparüberträge zu je 600,00 EUR auf das Tagesgeld gebucht. Zinsgutschriften: 30.06.2025 84,60 EUR, 30.09.2025 88,30 EUR, 31.12.2025 90,80 EUR, 31.03.2026 47,32 EUR und 30.06.2026 51,46 EUR. Es gab in diesem Zeitraum keine Abhebung vom Tagesgeldkonto. Ein einbehaltener Steuerbetrag ist in diesen Nettogutschriften bereits berücksichtigt.",
         "Im Depot wurden von April 2025 bis Juni 2026 fünfzehn Sparraten zu je 300,00 EUR investiert. Die Juli-Rate war am 8. Juli noch nicht ausgeführt. Der Depotausweis umfasst 226,815 Anteile des Mischfonds HavelWert Ausgewogen zum bankseitigen Bewertungskurs. Anschaffungskosten und aktueller Kurswert sind unterschiedliche Größen. Die Bewertung ist keine Verkaufsgarantie. Eine Altersvorsorgebindung besteht bei diesem frei verfügbaren Depot nach den hinterlegten Vertragsdaten nicht.\nMit freundlichen Grüßen\nEike Sander"])
    pdf(folder / "belege/Gold_Kauf_2022.pdf", "Havelmetall Edelmetalle", "Tobias Lenz · Breite Straße 34 · 14467 Potsdam", "Kaufabrechnung KM-22-119",
        "Jonas Bergmann · Kaufdatum 14.11.2022 · Zahlung unbar am 15.11.2022",
        ["Auf Ihren Auftrag wurden vier Anlagemünzen Krügerrand, jeweils eine Feinunze Gold, aus unserem Handelsbestand geliefert. Jahrgänge gemischt, bankhandelsfähiger Zustand. Die Münzen sind nach Stückzahl dokumentiert; individuelle Seriennummern tragen sie nicht. Die Übergabe erfolgte im Ladengeschäft gegen Abholschein.",
         table([["Position", "Stück", "Preis je Stück EUR", "Gesamt EUR"], ["Krügerrand 1 oz / Gold", "4", "1.750,00", "7.000,00"]], [248, 45, 105, 105], (1, 2, 3)),
         "Rechnungsbetrag 7.000,00 EUR. Es wird keine Umsatzsteuer gesondert ausgewiesen. Zahlung vom Privatkonto Jonas Bergmann, Ende 4402, eingegangen am 15. November 2022. Eine Verwahrung durch unser Haus wurde nicht beauftragt. Der Kunde nahm die Münzen in vier Kapseln und einer Transporthülle mit.\nTobias Lenz\nEdelmetallhandel"])
    pdf(folder / "belege/Gold_Ankauf_2026.pdf", "Havelmetall Edelmetalle", "Tobias Lenz · Breite Straße 34 · 14467 Potsdam", "Ankaufabrechnung KM-26-610",
        "Jonas Bergmann · 10.06.2026 · Prüfung und Übergabe 12:15 Uhr",
        ["Angekauft wurde eine Goldmünze Krügerrand, eine Feinunze, aus Privatbesitz. Gewicht, Abmessungen und Leitfähigkeit wurden im Laden geprüft. Die Münze wies keine die Handelsfähigkeit beeinträchtigende Beschädigung auf. Die im Kaufbeleg von 2022 bezeichneten übrigen drei Münzen wurden nicht eingeliefert.",
         table([["Stück", "Gegenstand", "Ankaufspreis EUR"], ["1", "Krügerrand 1 oz / Gold", "3.120,00"]], [50, 335, 118], (2,)),
         "Der vereinbarte Betrag von 3.120,00 EUR wurde am gleichen Tag auf das vom Verkäufer benannte Privatkonto Ende 4402 überwiesen. Keine Barzahlung, kein Tauschgeschäft und kein Verwahrvertrag. Mit der Gutschrift ist diese einzelne Ankaufposition abgerechnet.\nTobias Lenz"])
    pdf(folder / "belege/Gold_Angebot_2026-07-08.pdf", "Havelmetall Edelmetalle", "Tobias Lenz · Breite Straße 34 · 14467 Potsdam", "Unverbindliche Ankaufskondition",
        "08.07.2026, 15:20 Uhr · Anfrage Jonas Bergmann telefonisch\nBezug auf Kauf KM-22-119 und Ankauf KM-26-610",
        ["Für drei weitere Krügerrand-Münzen zu jeweils einer Feinunze haben wir Ihnen heute einen indikativen Ankaufspreis von 3.035,00 EUR pro Stück genannt. Bei drei bankhandelsfähigen Münzen entspräche dies 9.105,00 EUR. Die Stücke lagen bei der telefonischen Anfrage nicht vor. Vor einer Auszahlung wäre die Prüfung im Geschäft erforderlich.",
         "Das Angebot galt nur am genannten Handelstag und war keine Zusage für spätere Kurse. Nach Ihrer Angabe befinden sich die drei Münzen weiterhin in Ihrem Besitz. Eine Buchung, Übergabe oder Kaufpreiszahlung ist am 8. Juli nicht erfolgt. Der bereits im Juni abgerechnete Ankauf einer Münze ist nicht Bestandteil dieser Kondition.",
         "Diese Nachricht wurde auf Ihre Bitte am 19. August aus unserem Anfragebuch ausgedruckt. Sie dokumentiert eine Händlerkondition, keinen amtlichen Börsenkurs.\nMit freundlichen Grüßen\nTobias Lenz"])
    crypto = [
        ["2025-01-20", "KK-250120-081", "Kauf", "0.06000000", "5100.00", "0.00", "0.06000000", "belege/Krypto_Transaktionsauskunft.pdf"],
        ["2025-04-01", "KK-S-250401", "Bestandsauskunft", "0.00000000", "0.00", "0.00", "0.06000000", "belege/Krypto_Transaktionsauskunft.pdf"],
        ["2026-06-15", "KK-260615-204", "Verkauf", "-0.02000000", "1880.00", "5.64", "0.04000000", "belege/Krypto_Transaktionsauskunft.pdf"],
        ["2026-06-16", "KK-A-260616", "EUR-Auszahlung", "0.00000000", "1874.36", "0.00", "0.04000000", "kontoauszuege/Jonas_2026-06.pdf"],
        ["2026-07-08", "KK-S-260708", "Bestandsauskunft", "0.00000000", "0.00", "0.00", "0.04000000", "belege/Krypto_Transaktionsauskunft.pdf"],
    ]
    csv_file(folder / "zahlenwerk/Krypto_Transaktionen.csv", ["Datum", "Referenz", "Vorgang", "BTC_Veränderung", "EUR_Betrag", "Gebühr_EUR", "BTC_Bestand", "Belegdatei"], crypto)
    pdf(folder / "belege/Krypto_Transaktionsauskunft.pdf", "KontoKontor Digital GmbH", "Kundenservice · Friedrichstraße 71 · 10117 Berlin", "Transaktions- und Bestandsauskunft",
        "Kunde Jonas Bergmann · Kundenkonto KK-41872 · erstellt am 19.08.2026\nAngefragter Zeitraum 20.01.2025 bis 08.07.2026",
        ["Das Kundenkonto wurde am 17. Januar 2025 auf Jonas Bergmann eröffnet. Ein zweiter Inhaber ist nicht hinterlegt. Die Einzahlung vom 20. Januar betrug 5.100,00 EUR. Dieser Betrag wurde einschließlich der im Kaufpreis enthaltenen Gebühr vollständig zum Erwerb von 0,06000000 BTC verwendet. Die Verwahrung erfolgt innerhalb des Kundenkontos. Externe Übertragungen sind im angefragten Zeitraum nicht verzeichnet.",
         table([["Datum", "Vorgang", "BTC", "EUR"], ["20.01.2025", "Kauf KK-250120-081", "+0,06000000", "5.100,00"], ["01.04.2025", "Bestand / Indikationswert", "0,06000000", "4.620,00"], ["15.06.2026", "Verkauf KK-260615-204", "-0,02000000", "1.880,00"], ["16.06.2026", "Auszahlung nach Gebühr 5,64 EUR", "0,00000000", "1.874,36"], ["08.07.2026", "Bestand / Indikationswert", "0,04000000", "3.800,00"]], [72, 239, 96, 96], (2, 3)),
         "Der letzte Bestand entspricht 0,04000000 BTC. Das EUR-Verrechnungskonto weist am 8. Juli 2026 nach der Juni-Auszahlung 0,00 EUR aus. Der EUR-Indikationswert beruht auf dem intern verwendeten Kurs von 95.000,00 EUR je BTC am 8. Juli um 19:15 Uhr; er ist nicht der Erlös einer ausgeführten Order. Gebühren eines künftigen Verkaufs sind nicht abgezogen.",
         "Der Eintrag Verkauf bezeichnet ausschließlich die ausgeführte Teilmenge von 0,02000000 BTC. Eine Schließung des Kontos ist nicht verzeichnet. Zugangsdaten und private Schlüssel werden mit dieser Auskunft nicht mitgeteilt.\nFreundliche Grüße\nMiriam Groß\nKundenservice"])


def business_documents(folder):
    source = "belege/Betriebszahlen_2023_2025.pdf"
    euer = [
        ["Honorare Projektplanung", "186420.00", "199860.00", "176480.00", source],
        ["Erlöse Schulungen", "12400.00", "16600.00", "14750.00", source],
        ["Fremdleistungen", "-34280.00", "-39540.00", "-31260.00", source],
        ["Büromiete", "-12600.00", "-13200.00", "-13800.00", source],
        ["Personal Aushilfe", "-15640.00", "-17280.00", "-18480.00", source],
        ["Software und Daten", "-6840.00", "-7440.00", "-8520.00", source],
        ["Fahrten und Reisen", "-7940.00", "-8610.00", "-6260.00", source],
        ["Versicherung und Beiträge", "-3180.00", "-3240.00", "-3390.00", source],
        ["Abschreibungen", "-10400.00", "-11600.00", "-9850.00", source],
        ["Finanzierungskosten", "-1820.00", "-1660.00", "-1420.00", source],
        ["Sonstiger Aufwand", "-8760.00", "-9190.00", "-8930.00", source],
    ]
    csv_file(folder / "zahlenwerk/Euer_Jonas_2023_2025.csv", ["Position", "2023_EUR", "2024_EUR", "2025_EUR", "Belegdatei"], euer)
    pdf(folder / source, "Steuerbüro Weigel", "Matthias Weigel · Dortustraße 31 · 14467 Potsdam", "Betriebszahlen nach Jahresaufzeichnungen",
        "Bergmann Licht & Planung · Jonas Bergmann · Mandant 2187\nAuskunft vom 21.08.2026 · Jahre 2023 bis 2025",
        ["Die Aufstellung übernimmt die nach den Jahresaufzeichnungen abgegrenzten Nettoerlöse und Nettoaufwendungen. Umsatzsteuerzahlungen und Umsatzsteuererstattungen sind in dieser Übersicht nicht als eigene Positionen enthalten. Es handelt sich um eine betriebswirtschaftliche Mehrjahresübersicht, nicht um die vollständigen amtlichen EÜR-Formulare. Private Entnahmen und private Einkommensteuerzahlungen sind nicht als Betriebsaufwand abgesetzt.",
         table([["Position", "2023 EUR", "2024 EUR", "2025 EUR"]] + [[r[0]] + [money(v) for v in r[1:4]] for r in euer], [239, 88, 88, 88], (1, 2, 3)),
         "Die Leistungserbringung erfolgt überwiegend durch Herrn Bergmann persönlich. Die Aushilfe übernimmt Zeichnungsablage, Dokumentation und Terminverwaltung. In den Zahlen ist kein fiktiver Unternehmerlohn abgezogen. Eine Kunden- oder Unternehmensbewertung haben wir nicht vorgenommen. Für das laufende Jahr 2026 liegen bislang Buchungsunterlagen und offene Posten, aber noch kein Jahresabschluss vor.",
         "Kaufangebote, ein Unternehmenskaufvertrag oder eine Übertragungsvereinbarung liegen uns nicht vor. Aus den Gewinnen darf deshalb nicht ohne weitere Annahmen auf einen Verkaufspreis geschlossen werden. Die Unterlagen können nach Freigabe des Mandanten an einen gesondert beauftragten Bewerter übergeben werden.\nMatthias Weigel\nSteuerberater"])
    op_source = "belege/Offene_Posten_2026-07-08.pdf"
    ops = [
        ["BLP-26-031", "2026-05-20", "2026-06-03", "Havelhallen GmbH", "7140.00", "3570.00", "3570.00", "Rest nach Teilzahlung 10.06. / Rückfrage zu Aufmaß", op_source],
        ["BLP-26-036", "2026-06-04", "2026-06-18", "Nordbogen Werkstätten", "4284.00", "0.00", "4284.00", "Zahlung für 15.07. angekündigt", op_source],
        ["BLP-26-038", "2026-06-10", "2026-06-24", "Kulturhof West", "2380.00", "1190.00", "1190.00", "Einbehalt wegen fehlender Dokumentation", op_source],
        ["BLP-26-041", "2026-06-19", "2026-07-03", "Schulcampus Teltow", "5950.00", "0.00", "5950.00", "Prüflauf beim Auftraggeber", op_source],
        ["BLP-26-044", "2026-06-25", "2026-07-09", "Riedel Ladenbau", "3213.00", "0.00", "3213.00", "Noch nicht fällig am Auskunftstag", op_source],
        ["BLP-26-047", "2026-07-01", "2026-07-15", "Havelhallen GmbH", "1785.00", "0.00", "1785.00", "Zweite Halle / gesonderte Beauftragung", op_source],
        ["BLP-26-048", "2026-07-02", "2026-07-16", "Dahlmann Haustechnik", "1428.00", "0.00", "1428.00", "Rechnung per E-Mail bestätigt", op_source],
        ["BLP-26-049", "2026-07-03", "2026-07-17", "Parkterrassen Gastronomie", "952.00", "0.00", "952.00", "Kontoverbindung nochmals angefragt", op_source],
    ]
    csv_file(folder / "zahlenwerk/Offene_Posten_2026-07-08.csv", ["Rechnungsnummer", "Rechnungsdatum", "Fälligkeit", "Auftraggeber", "Brutto_EUR", "Bezahlt_EUR", "Rest_EUR", "Bemerkung", "Belegdatei"], ops)
    pdf(folder / op_source, "Bergmann Licht & Planung", "Jonas Bergmann · Büro: Behlertstraße 18 · 14469 Potsdam", "Offene Kundenrechnungen",
        "Stand 08.07.2026 nach Bankabgleich · exportiert von Leonie Franke am 11.08.2026",
        ["Die Liste enthält den am 8. Juli gebuchten Stand. Nach diesem Tag eingegangene Zahlungen sind nicht vorgezogen. Die Notizen stammen aus der Debitorenablage; sie ersetzen keine Bestätigung des Auftraggebers. Beträge einschließlich 19 Prozent Umsatzsteuer.",
         table([["Rechnung / Datum", "Kunde / Notiz", "Brutto EUR", "Bezahlt EUR", "Rest EUR"]] + [[r[0] + "\n" + r[1], r[3] + "\n" + r[7], money(r[4]), money(r[5]), money(r[6])] for r in ops], [91, 196, 72, 72, 72], (2, 3, 4)),
         "Nicht enthalten sind noch nicht abgerechnete Entwürfe für das Projekt Am Kanal. Für diese Arbeiten liegt ein Stundenblatt, aber noch keine Freigabe des Auftraggebers vor. Die Auftragsunterlagen werden getrennt aufbewahrt. Ein Inkassoverfahren war für keine der oben genannten Rechnungen beauftragt.\nLeonie Franke\nBüroorganisation"])
    inv_source = "belege/Inventar_Haendlerangebot_2026.pdf"
    inventory = [
        ["IT-2019-01", "CAD-Arbeitsstation", "2019-10-14", "3800.00", "1.00", "380.00", "Tastatur ersetzt / ohne Datenplatten", inv_source],
        ["IT-2023-02", "Notebook Projektarbeit", "2023-02-06", "2450.00", "1.00", "620.00", "Akku 76 Prozent / Netzteil vorhanden", inv_source],
        ["ME-2021-03", "Lichtmessgerät", "2021-04-12", "5200.00", "1300.00", "2150.00", "Kalibrierung 2025", inv_source],
        ["ME-2024-04", "Laser-Distanzmessgerät", "2024-06-18", "1680.00", "784.00", "920.00", "Koffer fehlt", inv_source],
        ["BU-2018-05", "Planablage und Schränke", "2018-09-03", "3100.00", "1.00", "250.00", "Abholung durch Käufer", inv_source],
        ["IT-2025-06", "Großformatdrucker", "2025-01-20", "2850.00", "2137.50", "1550.00", "Wartung Juni 2026", inv_source],
        ["ME-2020-07", "Leuchten-Prüfstand", "2020-11-09", "4600.00", "920.00", "1800.00", "Sonderanfertigung ohne Gewähr", inv_source],
        ["BU-2022-08", "Büromöbel Nebenraum", "2022-03-07", "2180.00", "908.33", "450.00", "Vier Tische und sechs Stühle", inv_source],
    ]
    csv_file(folder / "zahlenwerk/Inventar_Jonas_2026-07-08.csv", ["Inventarnummer", "Gegenstand", "Anschaffung", "Anschaffungskosten_EUR", "Buchwert_EUR", "Angebot_Haendler_EUR", "Bemerkung", "Belegdatei"], inventory)
    pdf(folder / inv_source, "Werkraum Gebrauchttechnik", "Felix Groß · Gewerbering 14 · 14532 Stahnsdorf", "Ankaufsvoranfrage Büro- und Messtechnik",
        "22.08.2026 · Bezug auf Inventarstand 08.07.2026 · Angebot WG-26-283",
        ["Sehr geehrter Herr Bergmann, nach Besichtigung am 20. August nennen wir Ihnen nachfolgend die unverbindlichen Netto-Ankaufsangebote für die vorgelegten Gegenstände. Die von Ihrem Steuerbüro zugelieferte Buchwertspalte geben wir nur zur Zuordnung wieder. Sie war für unsere Angebote nicht maßgeblich. Gegenüber dem 8. Juli sind nach Ihrer Erklärung keine Gegenstände hinzugekommen oder abgegeben worden.",
         table([["Inventar", "Gegenstand / Zustand", "Buchwert EUR", "Angebot EUR"]] + [[r[0], r[1] + "\n" + r[6], money(r[4]), money(r[5])] for r in inventory], [80, 223, 100, 100], (2, 3)),
         "Softwarelizenzen, Kundendaten, laufende Aufträge und der Name des Büros sind nicht Bestandteil dieser Voranfrage. Ein Fahrzeug wurde nicht angeboten. Das Angebot setzt Funktionsfähigkeit bei Übergabe voraus und beinhaltet keine Verbindlichkeit zur Übernahme des gesamten Betriebs. Es fand keine Übergabe statt.\nMit freundlichen Grüßen\nFelix Groß"])
    pdf(folder / "belege/Betrieb_Stichtagsunterlagen.pdf", "Steuerbüro Weigel", "Matthias Weigel · Dortustraße 31 · 14467 Potsdam", "Auszüge aus Anlagen- und Kontenunterlagen",
        "Bergmann Licht & Planung / Jonas Bergmann · Schreiben vom 21.08.2026",
        ["Sehr geehrter Herr Bergmann, die alten Unterlagen aus 2011 liegen teilweise nur als Ausdruck vor. Am 18. Juni 2011 sind folgende Einzelwerte dokumentiert: Geschäftskonto 16.820,00 EUR, offene Kundenforderungen 12.400,00 EUR, offene Lieferantenrechnungen 7.200,00 EUR und Betriebsmitteldarlehen 14.800,00 EUR. Die damalige Aufstellung zur Versicherung der Büroausstattung nennt einen Zeitwert von 17.500,00 EUR. Einen übertragbaren Kundenstamm oder persönlichen Geschäftswert haben wir damals nicht bewertet.",
         table([["Posten", "01.04.2025 EUR", "08.07.2026 EUR"], ["Geschäftskonto 7712", "24.180,50", "28.460,20"], ["Betriebsmitteldarlehen BD-2021-08", "11.300,00", "8.240,00"], ["Lieferantenrechnungen offen", "6.800,00", "9.760,00"], ["Umsatzsteuer laufendes Konto", "2.160,00", "3.480,00"]], [267, 118, 118], (1, 2)),
         "Die Privatentnahmen von April 2025 bis Juli 2026 sind im privaten Kontoauszug als solche bezeichnet; sie werden nicht nochmals als Betriebsausgaben abgezogen. Die Einkommensteuervorauszahlungen betreffen private Steuern und sind in den genannten Lieferantenverbindlichkeiten nicht enthalten. Bankkonten und Einzelwerte dürfen bei einer späteren Gesamtbewertung nicht ohne Abgrenzung zusätzlich angesetzt werden.",
         "Die Übersicht ist kein Unternehmenswertgutachten. Auf welche Weise Ertragskraft, persönliche Tätigkeit, betriebsnotwendige Ausstattung und Forderungsausfall in einer Bewertung berücksichtigt werden, war nicht Gegenstand unseres Auftrags. Bitte teilen Sie mit, ob ein gesonderter Bewerter direkt Einsicht in die Buchungsunterlagen erhalten soll.\nMatthias Weigel\nSteuerberater"])
    pdf(folder / "belege/Geschaeftskonto_Bankauskunft.pdf", BANK, BANK_ADDRESS, "Geschäftskonto und Betriebsmitteldarlehen",
        "Bergmann Licht & Planung / Jonas Bergmann · Auskunft 18.08.2026",
        ["Sehr geehrter Herr Bergmann, auf Ihre Anfrage bestätigen wir die Bestände des auf Sie allein geführten Geschäftskontos 7712 und des Betriebsmitteldarlehens BD-2021-08. Die Firmierung bezeichnet Ihr Einzelunternehmen und keinen weiteren Kontoinhaber.",
         table([["Stichtag", "Geschäftskonto EUR", "Darlehensrest EUR"], ["01.04.2025", "24.180,50", "11.300,00"], ["08.07.2026", "28.460,20", "8.240,00"]], [133, 185, 185], (1, 2)),
         "Für die Kontokorrentlinie von 15.000,00 EUR bestand an beiden Tagen keine Inanspruchnahme. Frau Bergmann ist für diese Geschäftsverbindung weder Mitdarlehensnehmer noch Bürge. Der Hausfinanzierungsvertrag HD-2014-731 ist eine getrennte Vertragsbeziehung. Die ausgewiesenen Guthaben sind nicht mit den Darlehensständen verrechnet.",
         "Die Zahlung auf Ihr Privatkonto 4402 am 2. Juli 2026 in Höhe von 5.225,00 EUR trägt den von Ihnen angegebenen Verwendungszweck Privatentnahme. Aus dieser Buchung allein ergibt sich weder ein Arbeitgeberverhältnis noch eine Aussage zum Wert des Unternehmens.\nMit freundlichen Grüßen\nEike Sander"])
    return euer, ops, inventory


def side_documents(folder):
    pdf(folder / "belege/Privatkonto_Jonas_Archiv_2019.pdf", BANK, BANK_ADDRESS, "Archivumsätze Privatkonto 4402",
        "Jonas Bergmann · Zeitraum 01.03.2019 bis 31.03.2019\nAngeforderter Auszug vom 18.08.2026 · Auszugsnummer 03/2019",
        ["Anfangssaldo am 1. März 2019: 16.520,00 EUR. Die nachstehenden Buchungen geben den vollständigen Monatsbestand des Privatkontos wieder. Die alltäglichen Familienzahlungen liefen in diesem Monat über das Gemeinschaftskonto. Der Auftraggebertext wurde unverändert übernommen.",
         table([["Buchungstag", "Vorgang / Gegenkonto", "Betrag EUR", "Saldo EUR"], ["04.03.2019", "Privatentnahme / Geschäftskonto 7712", "3.100,00", "19.620,00"], ["05.03.2019", "Übertrag Haushalt / Gemeinschaftskonto 4410", "-2.800,00", "16.820,00"], ["08.03.2019", "Bestattungen am Mühlenberg / B-190228-17", "-4.820,00", "12.000,00"], ["25.03.2019", "Ablösung Nachlassdarlehen GD-2012-118", "-4.300,00", "7.700,00"], ["29.03.2019", "Entgelt Kontoführung", "-5,90", "7.694,10"]], [76, 247, 90, 90], (2, 3)),
         "Endsaldo: 7.694,10 EUR. Der weitere Ablöseanteil von 4.200,00 EUR wurde unmittelbar vom Nachlasskonto gebucht und ist keine zusätzliche Gutschrift auf diesem Privatkonto. Ein Grundstückskauf oder Verkauf ist im Auszug nicht gebucht. Valuta entspricht dem jeweiligen Buchungstag.\nEike Sander\nKontenservice"])
    pdf(folder / "belege/Basisrente_Jonas_Vertragsauskunft.pdf", "Havelvorsorge Lebensversicherung", "Kundenservice · Schiffbauergasse 6 · 14467 Potsdam", "Vertragsauskunft RV-62241",
        "Jonas Bergmann · Versicherungsbeginn 01.02.2012\nAuskunft vom 24.08.2026 zum Vertragsstand 08.07.2026",
        ["Sehr geehrter Herr Bergmann, für Ihre Basisrentenversicherung führen wir Sie als Versicherungsnehmer und versicherte Person. Der monatliche Beitrag beträgt 260,00 EUR. Die Beiträge bis einschließlich Juni 2026 sind bezahlt. Die Juli-Lastschrift war zum angefragten Zeitpunkt noch nicht erfolgt. Eine Beleihung ist nicht verzeichnet.",
         "Vereinbart ist eine lebenslange monatliche Altersrente ab dem 1. März 2045. Der Vertrag räumt kein Kapitalwahlrecht ein. Die Ansprüche sind nach den Vertragsbedingungen weder vererblich, übertragbar, beleihbar noch veräußerbar. Bei Einstellung der Beitragszahlung kann der Vertrag unter den vereinbarten Voraussetzungen beitragsfrei fortgeführt werden; eine Auszahlung eines Rückkaufswerts ist nicht vorgesehen.",
         "Der technische Vertragswert aus dem Jahresnachweis zum 31. Dezember 2025 beträgt 39.840,00 EUR. Dieser Wert ist kein verfügbarer Bankbestand und kein Auszahlungsangebot. Eine gerichtliche Auskunft über ein in der Ehezeit erworbenes Anrecht wird bei entsprechender Anfrage gesondert erstellt. Dieses Schreiben ersetzt diese Auskunft nicht.\nMit freundlichen Grüßen\nDaniela Büttner\nVertragsservice"])
    pdf(folder / "belege/Privatdarlehen_Ursula_Abschluss.pdf", "Ursula Bergmann", "Brandenburger Straße 22 · 14542 Werder (Havel)", "Bestätigung zur Rückzahlung",
        "Werder, 09.08.2026 · an Jonas Bergmann, Feuerbachstraße 9, 14471 Potsdam",
        ["Lieber Jonas, ich habe die Mappe mit den alten Kontoauszügen gefunden. Das Geld hatte ich Dir 2010 für den gebrauchten Wagen und die neue Büroeinrichtung geliehen. Am 18. Juni 2011 waren davon noch 5.000,00 EUR offen. Wir hatten keine Zinsen ausgemacht. Mara hatte die Abrede nicht mit unterschrieben.",
         "Nach meinem Haushaltsbuch kamen am 2. Juli 2012 1.500,00 EUR, am 4. September 2013 weitere 1.500,00 EUR und am 14. März 2014 die letzten 2.000,00 EUR zurück. Seitdem fordere ich dafür nichts mehr von Dir. Ich hatte die letzte Zahlung auf der alten Karte mit dem grünen Stift vermerkt. Es ging damals nicht um das später gekaufte Haus.",
         "Die 380,00 EUR im Monat, die Du mir jetzt schickst, sind etwas anderes. Davon bezahle ich Fahrten zum Arzt, die Haushaltshilfe und das, was bei den Pflegeleistungen übrig bleibt. Ich möchte Dir dafür weder die Wohnung noch etwas aus einem späteren Nachlass versprechen. Eine Rückzahlung dieser laufenden Hilfe haben wir nicht vereinbart. Danke, dass Du die Unterlagen wieder zurückbringst.\nDeine Mutter\nUrsula Bergmann"])
    pdf(folder / "belege/Fahrzeuge_2011_2026.pdf", "Autohaus Bornstedter Feld", "Jens Thiel · Am Schragen 12 · 14469 Potsdam", "Auskunft zu Fahrzeugankäufen und Anfragen",
        "20.08.2026 · An Mara und Jonas Bergmann · Vorgang ABF-26-388",
        ["Sehr geehrte Frau Bergmann, sehr geehrter Herr Bergmann, aus den vorgelegten früheren Ankaufsangeboten ergeben sich für den 17. Juni 2011 folgende Werte: Frau Kreuter, VW Polo Baujahr 2008, damaliger Ankaufspreis 9.600,00 EUR; Herr Bergmann, Ford Focus Baujahr 2005, damaliger Ankaufspreis 6.800,00 EUR. Beide Angebote waren ohne offenen Fahrzeugkredit abgegeben worden. Für den 18. Juni ist keine Veränderung des Fahrzeugzustands dokumentiert.",
         "Die heute genutzten Fahrzeuge sind andere. Nach Besichtigung am 18. August 2026 und unter Zugrundelegung der Kilometerstände aus den Werkstattaufträgen vom 6. Juli nennen wir für den 8. Juli folgende Ankaufskonditionen: Skoda Octavia, Kennzeichen P-MB 418, Halterin Mara Bergmann, 91.420 Kilometer, 12.800,00 EUR; VW Caddy, Kennzeichen P-JB 278, Halter Jonas Bergmann, 138.700 Kilometer, 8.400,00 EUR. Ein Kauf wurde nicht abgeschlossen.",
         "Für den Octavia besteht nach Ihrer Angabe kein Kredit. Zum Caddy wurde die Ablöseauskunft des finanzierenden Instituts über 2.960,00 EUR zum 8. Juli vorgelegt. Eigentums- und Sicherungsrechte werden durch unsere Preisangabe nicht geprüft. Der Caddy ist nach Auskunft des Herrn Bergmann nicht im betrieblichen Anlagenverzeichnis erfasst. Die Angebote setzen die Übergabe mit den vorgelegten Rädern und Schlüsseln voraus.\nJens Thiel\nGebrauchtwagenankauf"])
    pdf(folder / "belege/Caddy_Kredit_2026.pdf", "Mobilkredit Nord GmbH", "Vertragsservice · Königstraße 17 · 30175 Hannover", "Kreditstand Fahrzeugvertrag MK-2019-278",
        "Jonas Bergmann · Fahrzeug VW Caddy / P-JB 278\nAuskunft 17.08.2026 zum 08.07.2026",
        ["Sehr geehrter Herr Bergmann, der am 8. Juli 2026 gebuchte Restkapitalbetrag beträgt 2.960,00 EUR. Die Juli-Rate von 240,00 EUR ist bereits berücksichtigt. Der Vertrag wurde mit Ihnen persönlich geschlossen. Frau Bergmann ist nicht Kreditnehmerin.",
         "Die Rate wird auf Ihren Wunsch seit Januar 2025 vom Geschäftskonto 7712 eingezogen. Die Wahl des Zahlkontos ändert den Kreditnehmer nicht. Das Steuerbüro erhält die Belastung als privaten Vorgang. Zum 1. April 2025 betrug das Restkapital 6.310,00 EUR. Rückstände oder Mahnkosten sind zu keinem der beiden Zeitpunkte ausgewiesen.",
         "Die Zulassungsbescheinigung Teil II wird bis zur Erledigung der gesicherten Forderungen von uns verwahrt. Die Auskunft enthält kein verbindliches Ablöseangebot für einen anderen Zahlungstag. Bitte nennen Sie bei einem Verkaufswunsch den geplanten Zahlungstermin.\nMit freundlichen Grüßen\nTanja Weller\nVertragsservice"])
    pdf(folder / "belege/Ferienhof_Rechnung_2025.pdf", "Ferienhof Achterwasser", "Hanna Völz · Dorfstraße 6 · 17459 Loddin", "Buchung 25182 / Zahlungsbestätigung",
        "10.06.2025 · Mara Bergmann · Reisezeit 12.07. bis 19.07.2025",
        ["Guten Tag Frau Bergmann, Ihre Restzahlung von 1.260,00 EUR ist heute auf unserem Konto eingegangen. Die Anzahlung von 240,00 EUR wurde bereits am 4. Februar 2025 gebucht. Der Gesamtpreis für die Ferienwohnung beträgt damit 1.500,00 EUR einschließlich Endreinigung und Wäsche. Die örtliche Kurabgabe wird erst bei Anreise abgerechnet.",
         "Angemeldet sind Sie und Ihre beiden Kinder Jule und Oskar. Die Änderung vom 9. Mai, wonach Herr Bergmann nicht mitreist, haben wir übernommen. Die Wohnung ist für vier Personen zum gleichen Wochenpreis vermietet; wegen der geringeren Personenzahl ergibt sich daher keine Erstattung. Fahrradverleih und Ausflüge sind nicht im Mietpreis enthalten.",
         "Die Schlüssel erhalten Sie am Anreisetag ab 15:00 Uhr im Hofbüro. Bitte rufen Sie an, falls Sie später als 18:00 Uhr eintreffen. Die Rückgabe erfolgt am 19. Juli bis 10:00 Uhr.\nFreundliche Grüße\nHanna Völz"])
    pdf(folder / "belege/Pflegedienst_Ursula_2026.pdf", "Pflegedienst Havelnah", "Büro Werder · Auf dem Strengfeld 9 · 14542 Werder (Havel)", "Abrechnung Eigenanteil Juni 2026",
        "Rechnung PH-2606-044 · 03.07.2026 · Ursula Bergmann\nLeistungsort Brandenburger Straße 22, 14542 Werder (Havel)",
        ["Sehr geehrte Frau Bergmann, wir berechnen die im Juni vereinbarten, nicht von der Pflegekasse übernommenen Leistungen. Der direkt mit der Pflegekasse abgerechnete Sachleistungsanteil wird mit dieser Rechnung nicht erneut verlangt. Die Besuchsnachweise liegen im Haushaltsordner und wurden wöchentlich abgezeichnet.",
         table([["Leistung", "Umfang", "Betrag EUR"], ["Haushaltshilfe zusätzlich", "8 Stunden zu 24,00 EUR", "192,00"], ["Begleitung Arzt und Apotheke", "4 Termine zu 18,00 EUR", "72,00"], ["Fahrtkosten Eigenanteil", "4 Fahrten zu 9,50 EUR", "38,00"], ["Eigenanteil gesamt", "", "302,00"]], [228, 175, 100], (2,)),
         "Der Betrag von 302,00 EUR wird am 10. Juli vom vereinbarten Konto abgebucht. Medikamente, private Taxifahrten und Einkäufe sind nicht Bestandteil dieser Rechnung. Bei Änderungen der Unterstützung durch Angehörige informieren Sie bitte die Einsatzplanung, damit Besuchszeiten abgestimmt werden können.\nMit freundlichen Grüßen\nKatrin Mohr\nVerwaltung"])


def build(root=ROOT, dataset=None):
    folder = root / "testakten" / SLUG
    records = transactions()
    bank_documents(folder, records)
    loans = loan_documents(folder)
    historic_and_property(folder)
    investment_documents(folder)
    business_documents(folder)
    side_documents(folder)
    data = {"slug": SLUG, "accounts": {who: {**ACCOUNTS[who], "closing": str(rows[-1]["balance"])} for who, rows in records.items()},
            "loan_closing": str(loans[-1][5]), "bank_rows": sum(len(rows) for rows in records.values())}
    if dataset:
        Path(dataset).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return data


if __name__ == "__main__":
    print(json.dumps(build(dataset=sys.argv[1] if len(sys.argv) > 1 else None), ensure_ascii=False, indent=2))
