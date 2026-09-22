#!/usr/bin/env python3
"""Einzeln ausgearbeitete Nachtragsbelege der Schöneberger Verwaltungsvorgänge."""

from __future__ import annotations

import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parent.parent
A = "betriebskosten-2025-weg-schoeneberg"
B = "betriebskosten-2025-mietshaus-schoeneberg"
WEG = "Gemeinschaft der Wohnungseigentümer Ebersstraße 84\nc/o Hofbogen Immobilienverwaltung GmbH\nHauptstraße 118, 10827 Berlin"
GMBH = "Südquadrat Wohnen GmbH\nAnne Kroll, Objektverwaltung\nDominicusstraße 28, 10827 Berlin"
VENDORS = {
    "freiweg": ("FREIWEG Räumdienst GmbH", "Ordensmeisterstraße 34, 12099 Berlin", "Sven Mertens | disposition@freiweg-raeumdienst.de", "USt-IdNr. DE318427965", "#415568"),
    "labor": ("Spreequell Wasseranalytik GmbH", "Lorenzstraße 46, 12209 Berlin", "Dr. Birgit Teich | befund@spreequell-wasseranalytik.de", "USt-IdNr. DE307582416", "#23645E"),
    "waerme": ("Wärmekreis Berlin GmbH", "Bessemerstraße 72, 12103 Berlin", "Annette Grewe | service@waermekreis-berlin.de", "USt-IdNr. DE296713842", "#4C5966"),
    "dach": ("Dachtechnik Rösner GmbH", "Ringstraße 21, 12105 Berlin", "Erik Rösner | service@roesner-dachtechnik.de", "USt-IdNr. DE287631954", "#4F6251"),
    "elektro": ("Elektro Klinker GmbH", "Alboinstraße 23, 12103 Berlin", "Tobias Klinker | buero@elektro-klinker-berlin.de", "USt-IdNr. DE309647218", "#345B72"),
    "kanal": ("Kanalwerk Lüftungstechnik GmbH", "Gottlieb-Dunkel-Straße 43, 12099 Berlin", "Petra Voss | rechnung@kanalwerk-lueftung.de", "USt-IdNr. DE321765498", "#6A5044"),
}


def amount(value):
    return Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def euro(value):
    return f"{amount(value):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def invoice(case, number, day, vendor, recipient, site, period, items, text, payment, paid=""):
    net = amount(sum(Decimal(str(q)) * Decimal(str(p)) for _, q, p in items))
    vat = amount(net * Decimal("0.19"))
    return dict(case=case, number=number, day=day, vendor=vendor, recipient=recipient,
                site=site, period=period, items=items, text=text, payment=payment,
                paid=paid, net=net, vat=vat, gross=net + vat,
                file=f"belege/{number}.pdf")


INVOICES = [
    invoice(A, "FR-250618-084", "2025-06-18", "freiweg", WEG, "Ebersstraße 84, Fahrradkeller und Hof", "16.06.2025, 08:20 bis 11:20 Uhr", [
        ("Acht gekennzeichnete Fahrräder zum Zwischenlager verbringen", 8, 32),
        ("Tragen, Etikettenabgleich und Übergabeliste", 3, 48),
        ("Fahrzeugpauschale Berlin einschließlich Anfahrt", 1, 60)],
        "Auftrag EB84-FR-06 von Frau Wendt. Von dreizehn am 6. Mai gekennzeichneten Rädern waren fünf vor unserem Termin entfernt worden. Die übrigen acht wurden nummeriert und in das Lager Lankwitz übernommen. Keine Verschrottung und kein Auftrennen angeschlossener, unmarkierter Fahrräder. Die Lagerliste trägt die Nummern EB84-01 bis EB84-08. Herr Albrecht hat die Übergabe um 11:20 Uhr gegengezeichnet.",
        "Zahlbar bis 02.07.2025 auf die im Lieferantenstamm geführte Bankverbindung. Lagerentgelt ist nicht in dieser Transportrechnung enthalten. Bei Rückfragen bitte FR-250618-084 nennen.", "2025-06-27"),
    invoice(A, "FR-250804-084", "2025-08-04", "freiweg", WEG, "Lager Lankwitz, Zugang EB84", "16.06.2025 bis 03.08.2025", [
        ("Stellplatzwochen: acht Räder für sieben volle Wochen", 56, 4)],
        "Die Lagerplätze beziehen sich auf die Übergabeliste vom 16. Juni. Alle acht Räder standen während des abgerechneten Zeitraums im abgegrenzten Lagerabschnitt. Das blaue Rad EB84-03 wurde am 30. Juli telefonisch von Herrn Rabe beansprucht; die Abholung war bei Rechnungserstellung für den 5. August vereinbart. Die telefonische Zuordnung hat die tatsächliche Lagerdauer nicht verkürzt. Für keines der Räder liegt bislang ein Verwertungsauftrag vor.",
        "Zahlbar bis 18.08.2025. Bezug zur Transportrechnung FR-250618-084, jedoch eigenständiger Leistungszeitraum. Nach Abholung wird der Stellplatz im nächsten Abrechnungslauf nicht weitergeführt.", "2025-08-15"),
    invoice(A, "SP-250919-084", "2025-09-19", "labor", WEG, "Ebersstraße 84, zentrale Trinkwassererwärmung", "Probenahme 09.09.2025, Untersuchung 09.09. bis 19.09.2025", [
        ("Untersuchung auf Legionella spec., drei Wasserproben", 3, 54),
        ("Probenahme und Temperaturdokumentation vor Ort", 1, 99),
        ("Anfahrt und gekühlter Probentransport", 1, 35)],
        "Auftragsnummer SQ-084-25. Die untersuchten Entnahmestellen und Ergebnisse stehen im gesonderten Bericht SP-L250919-084. Der Zugang zur Wohnung 12 wurde durch die Verwaltung ermöglicht. Die Rechnung enthält keine Armaturenreparatur, keine Anlagenreinigung und keine Maßnahme am Wärmeerzeuger. Der versiegelte Probensatz ging am 9. September um 12:35 Uhr im Labor ein; die Rechnung wird gemeinsam mit der freigegebenen Berichtsfassung versandt.",
        "Zahlbar bis 03.10.2025. Bitte Rechnungsnummer und Kundenkonto EB84 angeben. Eine zusätzliche Anfahrt wurde nicht berechnet.", "2025-09-30"),
    invoice(A, "WK-250925-PV84", "2025-09-25", "waerme", WEG, "Ebersstraße 84, Heizraum", "24.09.2025, 12:40 bis 14:10 Uhr", [
        ("Undichte Probenahmearmatur im Zirkulationsrücklauf ersetzen", 1, 96),
        ("Montage, Dichtheitskontrolle und Dokumentation, Stunden", 1.5, 68)],
        "Nach dem Labortermin wurde Tropfwasser an der vorhandenen Probenahmearmatur gemeldet. Die Spindelabdichtung ließ sich nicht nachstellen. Armatur gewechselt, Anschluss abgedichtet und auf Dichtheit kontrolliert. Monteur Deniz Acar meldete den Abschluss Frau Wendt. Die Arbeiten wurden nach der ohnehin am selben Tag ausgeführten Kesselwartung erledigt. Deshalb keine weitere Anfahrt. Die Wartungsrechnung EB84-HW-2025 enthält diese Armatur und diese Arbeitszeit nicht.",
        "Zahlbar bis 09.10.2025 unter Angabe WK-250925-PV84. Der ausgetauschte Altteil wurde dem Hausservice gezeigt und anschließend als Metallschrott mitgenommen.", "2025-10-06"),
    invoice(A, "DR-251118-084", "2025-11-18", "dach", WEG, "Ebersstraße 84, hofseitige Dachrinne", "17.11.2025, 09:00 bis 12:00 Uhr", [
        ("Laub und Ablagerungen aus 34 Metern Dachrinne entfernen, Stunden", 3, 65),
        ("Zugangssicherung und Abtransport des Reinigungsguts", 1, 70)],
        "Ausführung nach Herbstterminplan. Gereinigt wurden Rinne und vorhandene Einlaufkörbe; anschließend erfolgte eine Wasserdurchlaufkontrolle. Keine neuen Rohrstücke, keine Lötarbeiten und kein Ersatz von Haltern. Der im August erneuerte Kupferrohrabschnitt blieb unberührt. Das Laub wurde in fünf Säcken aufgenommen und abgefahren. Herr Albrecht öffnete den Dachzugang und nahm den verschlossenen Schlüsselumschlag um 12:10 Uhr zurück.",
        "Zahlbar bis 02.12.2025. Der Bezug zur früheren Rechnung EB84-KU-2025 dient nur der Bauteilzuordnung; diese wird weder erneut berechnet noch gutgeschrieben.", "2025-11-28"),
    invoice(A, "EK-EB84-TG-26-041", "2026-05-08", "elektro", WEG, "Ebersstraße 84, gemeinsame Tiefgaragen-Grundinstallation", "20.04.2026 bis 06.05.2026", [
        ("Leitungswege und Kabeltrassen gemäß Angebot vom 08.12.2025", 1, 6000),
        ("Unterverteilung und dynamisches Lastmanagement", 1, 7000),
        ("Planung, Messkonzept und Inbetriebnahme", 1, 2000)],
        "Schlussrechnung zum schriftlichen Auftrag vom 2. März 2026. Frau Wendt und Herr Rabe nahmen die gemeinsame Anlage am 6. Mai um 14:30 Uhr ab. Der Schrank trägt die Kennzeichnung EB84-LM01. Die Verlegung verläuft bis zu den vorbereiteten Abzweigpunkten; einzelne Ladegeräte und deren Anschlusskabel sind nicht enthalten. Das Prüfprotokoll wurde mit der technischen Dokumentation übergeben. Keine Abschläge gestellt und keine Beträge aus 2025 vereinnahmt.",
        "Zahlbar bis 22.05.2026. Auftraggeber ist ausschließlich die Gemeinschaft. Die private Rechnung EK-EB84-LP-26-042 an Herrn Rabe wird gesondert versandt.", "2026-05-20"),
    invoice(A, "EK-EB84-LP-26-042", "2026-05-08", "elektro", "Herrn Jens Rabe\nc/o Hofbogen Immobilienverwaltung GmbH\nHauptstraße 118, 10827 Berlin", "Ebersstraße 84, Stellplätze 3 und 4", "05.05.2026 bis 06.05.2026", [
        ("Ladepunkt mit Messung und Zugangskarte", 2, 780),
        ("Private Zuleitungen ab vorbereitetem Abzweigpunkt", 2, 180),
        ("Montage und Einbindung beider Geräte", 1, 240)],
        "Auftrag von Herrn Rabe vom 12. März 2026. Zwei Ladepunkte an den von ihm bezeichneten Stellplätzen installiert und mit den Zugangskarten R03 und R04 übergeben. Die Geräte sind dem gemeinsamen Lastmanagement untergeordnet. Die gemeinsame Grundinstallation wird in dieser Rechnung nicht nochmals angesetzt. Die Geräteseriennummern und die Zugangskarten sind auf dem Herrn Rabe übergebenen Inbetriebnahmeblatt verzeichnet. Die Rechnung wird auf seinen Wunsch über das Objektbüro zugestellt.",
        "Zahlbar bis 22.05.2026 durch den Rechnungsempfänger. Bitte die private Auftragsnummer EK-EB84-LP-26-042 angeben. Die Rechnung der Gemeinschaft trägt eine andere Nummer."),
    invoice(B, "FR-250327-073", "2025-03-27", "freiweg", GMBH, "Gotenstraße 73, Hofdurchgang", "25.03.2025, 07:45 bis 10:15 Uhr", [
        ("Fünf mit Objektanhänger versehene Fahrräder auslagern", 5, 29),
        ("Tragearbeiten und Aufnahme der Rahmennummern, Stunden", 2.5, 48),
        ("Transportfahrzeug und Anfahrt", 1, 55)],
        "Auftrag von Frau Kroll nach Ablauf der im Aushang genannten Rückmeldefrist vom 21. März. Die fünf Räder verengten den Hofdurchgang. Die Nummern GO73-M01 bis M05 wurden bei der Übernahme mit der Liste des Hausdienstes verglichen. Ein angekettetes Lastenrad ohne Anhänger blieb stehen. Übernommen wurde zur Verwahrung, nicht zur sofortigen Verwertung. Einlagerungsbestätigung am selben Tag per E-Mail an das Objektbüro; Abholung gegen Zuordnungsnachweis möglich.",
        "Zahlbar bis 10.04.2025. Rechnung betrifft allein den Einsatz vom 25. März. Keine Dauerpauschale für spätere Hofräumungen.", "2025-04-07"),
    invoice(B, "FR-251106-073", "2025-11-06", "freiweg", GMBH, "Gotenstraße 73, Fahrradständer vor dem Hofeingang", "04.11.2025, 08:10 bis 10:10 Uhr", [
        ("Drei erneut zurückgelassene, gekennzeichnete Fahrräder auslagern", 3, 29),
        ("Tragen, Liste und Ladungssicherung, Stunden", 2, 54),
        ("Anfahrt mit Transportfahrzeug", 1, 50)],
        "Die Gegenstände tragen die neuen Kennzeichen GO73-N01 bis N03. Es handelt sich nicht um einen zweiten Transport der im März erfassten Räder. Frau Martens war bei der Übergabe anwesend. Zu N02 fehlt ein Hinterrad, N03 hat einen gerissenen Sattel; diese Merkmale wurden auf dem Übernahmezettel vermerkt. Die Stellfläche wurde leer übergeben. Ob die Gegenstände später herausgegeben oder verwertet werden, ist mit diesem Räumauftrag nicht entschieden.",
        "Zahlbar bis 20.11.2025. Bei Rückfragen Rechnung FR-251106-073 und Kennzeichen des einzelnen Fahrrads nennen.", "2025-11-17"),
    invoice(B, "SP-251024-073", "2025-10-24", "labor", GMBH, "Gotenstraße 73, zentrale Trinkwassererwärmung", "Probenahme 14.10.2025, Untersuchung 14.10. bis 24.10.2025", [
        ("Untersuchung auf Legionella spec., drei Wasserproben", 3, 52),
        ("Probenahme und Temperaturaufnahme", 1, 96),
        ("Anfahrt und Probentransport", 1, 30)],
        "Kundenauftrag SQ-073-25. Proben am Speicherabgang, Zirkulationsrücklauf und an der entfernten Entnahmestelle in Wohnung 08. Die Nummern, Zeiten und Messergebnisse enthält Bericht SP-L251024-073. Frau Martens begleitete den Heizraumtermin; der Wohnungszugang war vorab vereinbart. Keine Wasserproben aus dem Nachbarhaus Gotenstraße 71 und keine Lebensmitteluntersuchung. Es wurden weder neue Messgeräte eingebaut noch Leitungen instand gesetzt.",
        "Zahlbar bis 07.11.2025. Die Befundübermittlung an das Objektbüro ist im Untersuchungspreis enthalten.", "2025-11-04"),
    invoice(B, "KL-250811-071", "2025-08-11", "kanal", "Tafelgut Gastronomie GmbH\nz. Hd. Lukas Ahrendt\nGotenstraße 71, 10829 Berlin", "Gotenstraße 71, Restaurant TAFELGUT im Erdgeschoss", "08.08.2025, 06:30 bis 10:00 Uhr", [
        ("Fettfilter ausbauen und reinigen, Stunden", 3.5, 72),
        ("Reinigungsmittel und Auffangmaterial", 1, 68),
        ("Ventilatorprüfung und Messung am Auslass", 1, 100)],
        "Serviceauftrag des Restaurantbetreibers vom 6. August. Filter gereinigt und wieder eingesetzt, Motorlager kontrolliert. Die vorhandene seitliche Ausblasöffnung blieb unverändert. Der Kochbetrieb begann nach Abschluss wieder um 11:30 Uhr. Bei geringer Windbewegung gelangte weiterhin Küchenluft in den Hof; eine neue Rohrführung war nicht beauftragt. Ein Messblatt wurde Herrn Ahrendt übergeben. Das Wohngebäude Nummer 73 hat keinen Anschluss an diesen Küchenabluftstrang.",
        "Zahlbar bis 25.08.2025 durch die Gastronomiegesellschaft. Die Objektverwaltung erhält auf Wunsch des Auftraggebers eine Kopie; ein zweites Rechnungsexemplar ist keine weitere Forderung.", "2025-08-22"),
    invoice(B, "KL-250905-073", "2025-09-05", "kanal", GMBH, "Gotenstraße 73, Restaurant TAFELGUT, Objekt GO73", "01.09.2025 bis 03.09.2025", [
        ("Edelstahl-Küchenabluftleitung über Dach, 11 Meter", 11, 280),
        ("Dachkonsole und Befestigungssatz", 1, 980),
        ("Montage und Abdichtung, Stunden", 24, 95),
        ("Gerüstzugang und Luftmengenmessung", 1, 460)],
        "Schlussrechnung zum Auftrag von Herrn Brenner vom 20. August. Die Baustellenmappe führt den Auftrag KW-71-0820, Restaurant TAFELGUT. Die neue Leitung wurde vom bisherigen seitlichen Austritt bis zum Dachabschluss geführt. Abnahme am 3. September durch Herrn Brenner und Herrn Ahrendt. Filterreinigung vom August nicht erneut enthalten. Der Montagebericht ist unter der Baustellennummer abgelegt. Die Ausführung wurde nach dem vereinbarten Ortstermin abgerechnet; Nachtragsleistungen sind nicht hinzugekommen.",
        "Zahlbar bis 19.09.2025. Bei Rückfragen zur Objektanschrift oder zur Zuordnung des Montageberichts bitte vor Zahlung Nachricht an Petra Voss."),
    invoice(B, "KL-G250917-073", "2025-09-17", "kanal", GMBH, "Storno zum Rechnungskopf Gotenstraße 73", "Bezug: Rechnung KL-250905-073 vom 05.09.2025", [
        ("Vollständige Stornierung der ursprünglichen Schlussrechnung", 1, -6800)],
        "Sehr geehrte Frau Kroll, wir stornieren die Rechnung KL-250905-073 in voller Höhe. Die dort genannte Objektanschrift entsprach nicht dem Montageauftrag. Leistungsempfänger bleibt die Südquadrat Wohnen GmbH. Die berichtigte Rechnung KL-250917-071 mit der Baustellenanschrift Gotenstraße 71 wird gesondert übermittelt. Die Montage ist einmal ausgeführt worden. Bitte bewahren Sie Original, Storno und neue Rechnung als zusammenhängenden Vorgang auf.",
        "Auf die stornierte Rechnung ging keine Zahlung ein. Deshalb erfolgt aus diesem Dokument keine Auszahlung oder Verrechnung mit anderen Aufträgen. Bitte nur die berichtigte Rechnung zur Zahlung verwenden."),
    invoice(B, "KL-250917-071", "2025-09-17", "kanal", GMBH, "Gotenstraße 71, Restaurant TAFELGUT, Objekt GO71", "01.09.2025 bis 03.09.2025", [
        ("Edelstahl-Küchenabluftleitung über Dach, 11 Meter", 11, 280),
        ("Dachkonsole und Befestigungssatz", 1, 980),
        ("Montage und Abdichtung, Stunden", 24, 95),
        ("Gerüstzugang und Luftmengenmessung", 1, 460)],
        "Berichtigte Rechnung zum Auftrag KW-71-0820. Sie ersetzt ausschließlich die mit KL-G250917-073 stornierte Rechnung KL-250905-073. Leistungsumfang, Ausführungszeitraum und Rechnungsempfänger sind unverändert. Richtiggestellt sind Baustellenanschrift und Objektkennzeichen. Die Montage erfolgte auf dem Dach und an der Hofseite des Nachbargebäudes Gotenstraße 71, nicht an der Heizung oder an Wohnungsentlüftungen der Nummer 73. Abnahme am 3. September; Unterlagen liegen dem Objektbüro vor.",
        "Zahlbar bis 01.10.2025. Zahlungsreferenz KL-250917-071. Keine weitere Forderung aus der ursprünglichen Rechnung.", "2025-10-01"),
    invoice(B, "EK-GO73-TG-26-056", "2026-06-12", "elektro", GMBH, "Gotenstraße 73, Tiefgarage, gemeinsame Grundinstallation", "01.06.2026 bis 10.06.2026", [
        ("Leitungswege und Kabeltrassen", 1, 4000),
        ("Verteilung und Lastmanagement", 1, 5000),
        ("Planung, Messkonzept und Inbetriebnahme", 1, 1500)],
        "Schlussrechnung auf Grundlage des Angebots EK-GO73-TG-25 und des Auftrags vom 3. März 2026. Die Anlage wurde am 10. Juni um 09:40 Uhr mit Frau Kroll in Betrieb genommen. Endpunkte für sechs Stellplätze vorbereitet, noch keine privaten Ladegeräte montiert. Zählerfeld GO73-LM01 bleibt vom Treppenhauszähler A01 getrennt. Der Baustellenzugang wurde am 1. Juni durch Frau Martens geöffnet; die letzten Kabeldurchführungen wurden am 9. Juni verschlossen. Abschläge wurden nicht angefordert.",
        "Zahlbar bis 26.06.2026 unter Angabe EK-GO73-TG-26-056. Abnahme und Prüfprotokoll wurden der Objektverwaltung ausgehändigt.", "2026-06-24"),
]


def paragraph(text, size=10, color="#222222", bold=False):
    return Paragraph(escape(str(text)).replace("\n", "<br/>"), ParagraphStyle(
        "body", fontName="Helvetica-Bold" if bold else "Helvetica", fontSize=size,
        leading=size * 1.32, textColor=colors.HexColor(color), spaceAfter=7))


def document(path, vendor, recipient, title, metadata, sections):
    name, address, contact, taxid, tone = VENDORS[vendor]
    path.parent.mkdir(parents=True, exist_ok=True)
    flow = [paragraph(name, 17, tone, True), paragraph(f"{address}\n{contact}", 9),
            Spacer(1, 15), paragraph(recipient, 10), Spacer(1, 9),
            paragraph(title, 14, tone, True)]
    flow.extend(paragraph(f"{key}: {value}", 9) for key, value in metadata)
    flow.append(Spacer(1, 7))
    for section in sections:
        if isinstance(section, str):
            flow.append(paragraph(section))
        else:
            rows, widths = section
            table = Table([[paragraph(c, 9, "#FFFFFF" if r == 0 else "#222222", r == 0)
                            for c in row] for r, row in enumerate(rows)], colWidths=widths,
                          repeatRows=1, hAlign="LEFT")
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(tone)),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F1F3F4")]),
            ]))
            flow.extend([table, Spacer(1, 9)])

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(colors.HexColor("#555555"))
        canvas.drawString(46, 34, f"{name} | {taxid}")
        canvas.drawString(46, 23, path.stem)
        canvas.drawRightString(A4[0] - 46, 23, f"Seite {doc.page}")
        canvas.restoreState()

    SimpleDocTemplate(str(path), pagesize=A4, leftMargin=46, rightMargin=46,
                      topMargin=34, bottomMargin=50, title=title, author=name).build(
        flow, onFirstPage=footer, onLaterPages=footer,
        canvasmaker=lambda *a, **kw: Canvas(*a, **dict(kw, invariant=1)))


def build(root=ROOT):
    for row in INVOICES:
        items = [["Leistung", "Menge", "Netto / EUR", "Gesamt / EUR"]]
        items += [[label, str(quantity).replace(".", ","), euro(price), euro(Decimal(str(quantity)) * Decimal(str(price)))]
                  for label, quantity, price in row["items"]]
        items += [["Nettobetrag", "", "", euro(row["net"])],
                  ["Umsatzsteuer 19 Prozent", "", "", euro(row["vat"])],
                  ["Rechnungsbetrag", "", "", euro(row["gross"])]]
        document(root / "testakten" / row["case"] / row["file"], row["vendor"], row["recipient"],
                 "Stornorechnung" if row["net"] < 0 else "Rechnung",
                 [("Nummer", row["number"]), ("Rechnungsdatum", row["day"]),
                  ("Leistungsort", row["site"]), ("Leistungszeitraum", row["period"])],
                 [(items, [258, 45, 94, 106]), row["text"], row["payment"],
                  "Mit freundlichen Grüßen\n" + VENDORS[row["vendor"]][2].split(" | ")[0]])

    for slug, code, recipient, taken, report, temps, results in [
        (A, "084", WEG, "09.09.2025", "19.09.2025", [61.4, 56.2, 55.8], ["<2", "<2", "12"]),
        (B, "073", GMBH, "14.10.2025", "24.10.2025", [62.0, 57.1, 55.3], ["<2", "<2", "<2"]),
    ]:
        ident = "SP-L250919-084" if slug == A else "SP-L251024-073"
        terminal = "WE12" if slug == A else "WE08"
        rows = [["Proben-ID / Entnahmestelle", "Zeit", "Temperatur °C", "Legionella spec. KBE/100 ml"]]
        rows += [[f"SQ{code}-{i:02d}: {site}", time, str(temp).replace(".", ","), result]
                 for i, (site, time, temp, result) in enumerate(zip(
                     ["Speicherabgang", "Zirkulationsrücklauf", f"Dusche {terminal}"],
                     ["09:10", "09:25", "10:05"], temps, results), 1)]
        document(root / "testakten" / slug / "belege" / f"{ident}.pdf", "labor", recipient,
                 "Untersuchungsbericht Trinkwasser warm",
                 [("Bericht", ident), ("Probenahme", taken), ("Befundfreigabe", report)],
                 ["Auftraggeber und Probenstellen entsprechen dem beigefügten Probenahmeauftrag. Untersuchungsparameter: Legionella spec. Die Probenahme führte Kerstin Sommer durch. Die Messung erfolgte nach Abnahme vorhandener Strahlregler beziehungsweise am vorgesehenen Probenahmehahn. Temperaturen wurden an der Entnahmestelle erfasst. Die gekühlten, verschlossenen Proben trafen am selben Tag im Labor ein.",
                  (rows, [219, 49, 92, 143]),
                  "Verfahren: Kulturverfahren nach DIN EN ISO 11731; Ergebnisangabe bezogen auf 100 ml. Das Zeichen <2 bezeichnet ein Ergebnis unterhalb der für diese Probe erreichten Bestimmungsgrenze. Ergebnisse gelten für die bezeichneten Proben zum Entnahmezeitpunkt; andere Leitungsabschnitte wurden nicht untersucht. Der Bericht ersetzt weder einen Bauzustandsbericht noch eine Messung sämtlicher Wohnungsanschlüsse.",
                  "Probenzustand bei Eingang: Gefäße dicht, Kennzeichnungen lesbar, keine Transportschäden vermerkt. Probeneingang und Geräteprotokoll sind unter dem Laborauftrag hinterlegt. Bericht geprüft und freigegeben am oben genannten Datum. Ansprechpartner für Rückfragen zur Analytik ist Dr. Birgit Teich.",
                  "Dr. Birgit Teich\nLaborleitung Wasseranalytik"])

    document(root / "testakten" / A / "belege/FR-250616-084_Uebernahme.pdf", "freiweg", WEG,
             "Übernahme zur Zwischenlagerung",
             [("Datum", "16.06.2025"), ("Objekt", "Ebersstraße 84"), ("Auftrag", "EB84-FR-06")],
             ["Bei Beginn des Einsatzes waren acht der dreizehn markierten Räder vorhanden. Fünf Stellplätze waren nach Rückmeldung des Hausservice vor dem Termin freigemacht worden. Die Kennzeichnungen der übrigen Gegenstände wurden am Verladeort nochmals mit der Liste abgeglichen. Herr Tom Albrecht öffnete um 08:20 Uhr Keller und Hoftor. Ein unmarkiertes Lastenrad und der Kinderroller an der Kellertreppe wurden nicht angefasst.",
              ([["Kennzeichen", "Merkmale bei Übernahme"], ["EB84-01", "Schwarzes Herrenrad, vorderer Reifen ohne Luft"], ["EB84-02", "Silbernes Cityrad, Korb lose"], ["EB84-03", "Blaues Tourenrad, brauner Sattel, Schloss am Rahmen"], ["EB84-04", "Rotes Jugendrad, Kette abgesprungen"], ["EB84-05", "Grünes Damenrad, Rücklicht fehlt"], ["EB84-06", "Graues Rad, Vorderrad ausgebaut beigebunden"], ["EB84-07", "Weißes Klapprad, rechter Griff beschädigt"], ["EB84-08", "Dunkles Trekkingrad, Gepäckträger mit gelbem Band"]], [85, 418]),
              "Eingelagert im Abschnitt L2 in Lankwitz. Keine Aussage über Eigentumsaufgabe; dies wurde vor Ort nicht geprüft. Herausgabe nur nach Zuordnung über die Verwaltung und Übergabevermerk. Die Gegenstände bleiben einzeln gekennzeichnet. Übernahme beendet um 11:20 Uhr. Unterschriften auf dem Transportblatt: Sven Mertens für den Räumdienst und Tom Albrecht für den Hausservice."])

    document(root / "testakten" / B / "belege/KW-71-0820_Montagebericht.pdf", "kanal", GMBH,
             "Montage- und Übergabebericht Küchenabluft",
             [("Baustelle", "Gotenstraße 71, Restaurant TAFELGUT"), ("Auftrag", "KW-71-0820 vom 20.08.2025"), ("Übergabe", "03.09.2025, 15:20 Uhr")],
             ["Nach den Beschwerden über Küchenluft im gemeinsamen Hofbereich wurde eine neue, elf Meter lange Edelstahlleitung bis über Dach geführt. Die bisherige seitliche Ausblasöffnung wurde geschlossen. Das Gerüst stand auf der Hofseite der Nummer 71. Zugang über die Restaurantküche, Dachzugang durch den Hausmeister. Im Wohnhaus Nummer 73 wurden keine Leitungen verlegt, keine Wandöffnungen hergestellt und keine Wohnungsgeräte angeschlossen.",
              ([["Ausführung", "Feststellung"], ["01.09.2025", "Konsolen gesetzt und Leitungstrasse montiert; Küche bis 16 Uhr geschlossen"], ["02.09.2025", "Rohrsegmente und Dachabschluss gesetzt; vorhandener Ventilator weiterverwendet"], ["03.09.2025", "Durchführung abgedichtet, Luftmenge geprüft, seitliche Altöffnung geschlossen"], ["Übergabe", "Elias Brenner und Lukas Ahrendt anwesend; Restpunkt: kleine Putzstelle im Hof"]], [105, 398]),
              "Die Filterreinigung vom 8. August ist eine frühere Leistung und nicht Teil dieses Montageauftrags. Bei der Übergabe war im Erdgeschosshof kein auffälliger Küchenluftgeruch wahrnehmbar; eine Beobachtung bei jeder Windrichtung fand nicht statt. Herr Ahrendt will die nächsten Abenddienste abwarten. Kein Austausch des Küchenventilators, kein Umbau des Fettabscheiders und keine Arbeiten an der Gebäudeheizung.",
              "Technische Unterlagen übergeben an das Objektbüro. Empfang bestätigt: Elias Brenner, 03.09.2025. Montageleitung: Pascal Rehberg. Nachtrag am 5. September: Frau Kroll bittet um Kontrolle der Objektanschrift im Rechnungskopf; Rechnungserstellung erfolgt zentral bei Frau Voss."])

    for slug in (A, B):
        path = root / "testakten" / slug / "zahlenwerk/Belegnachtrag_2025_2026.csv"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream, delimiter=";")
            writer.writerow(["Belegnummer", "Datum", "Leistungszeitraum", "Aussteller", "Rechnungsempfänger", "Leistungsort", "Netto_EUR", "USt_EUR", "Brutto_EUR", "Zahlungsdatum_laut_Unterlagen", "Datei"])
            for row in INVOICES:
                if row["case"] == slug:
                    writer.writerow([row["number"], row["day"], row["period"], VENDORS[row["vendor"]][0],
                                     row["recipient"].split("\n")[0], row["site"], row["net"], row["vat"],
                                     row["gross"], row["paid"], row["file"]])
        payments = [row for row in INVOICES if row["case"] == slug and row["paid"]
                    and row["recipient"] in (WEG, GMBH)]
        with (path.parent / "Zahlungsdetails_Nachtraege.csv").open("w", encoding="utf-8", newline="") as stream:
            writer = csv.writer(stream, delimiter=";")
            writer.writerow(["Buchungsdatum", "Objektkonto", "Empfänger", "Verwendungszweck", "Belastung_EUR", "Buchungsreferenz"])
            for row in sorted(payments, key=lambda item: item["paid"]):
                account = "GO71" if row["number"] == "KL-250917-071" else ("EB84" if slug == A else "GO73")
                writer.writerow([row["paid"], account, VENDORS[row["vendor"]][0], row["number"],
                                 row["gross"], f"SEPA-{account}-{row['number']}"])


if __name__ == "__main__":
    build()
    print(f"{len(INVOICES)} Rechnungen/Stornos, vier Nachweise und vier Beleg-/Zahlungsregister erstellt.")
