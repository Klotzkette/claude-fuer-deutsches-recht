#!/usr/bin/env python3
"""Reproduzierbare Rechnungen und Buchungsdaten der beiden Schöneberger Akten."""

from __future__ import annotations

import calendar
import csv
import json
import sys
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.pdfgen.canvas import Canvas

ROOT = Path(__file__).resolve().parent.parent
CASES = [
    dict(slug="betriebskosten-2025-weg-schoeneberg", code="EB84", address="Ebersstraße 84, 10827 Berlin", area=1200, unit="07", owner="Katrin Schütte", tenant="Yasin und Nora Seidel", recipient="Gemeinschaft der Wohnungseigentümer Ebersstraße 84", manager="Hofbogen Immobilienverwaltung GmbH", clerk="Lea Wendt", manager_address="Hauptstraße 118, 10827 Berlin", units=12, hm=900, power=140, tax_value=320000, tax=466.24, water=3680, waste=2950, street=620, insurance=2460, lift=1785, chimney=357, heat_service=714, meter=1190, pump=480, rebate=119, repair=1249.50, light=416.50, paint=1785, theft=2165.80, recovery=940, opening=3000, opening_price=1.10, closing=2500, oils=[(5000,1.05),(2000,.98),(5000,1.02)], opening_co2=430.54, pv=18, draft_date="2026-08-12", tenant_date="2026-08-18", cold=190, heat=110, rent=1620),
    dict(slug="betriebskosten-2025-mietshaus-schoeneberg", code="GO73", address="Gotenstraße 73, 10829 Berlin", area=800, unit="04", owner="Südquadrat Wohnen GmbH", tenant="Fabian und Miriam Öztürk", recipient="Südquadrat Wohnen GmbH", manager="Südquadrat Wohnen GmbH", clerk="Anne Kroll", manager_address="Dominicusstraße 28, 10827 Berlin", units=8, hm=800, power=115, tax_value=2600000, tax=3788.20, water=2840, waste=2360, street=480, insurance=1980, lift=1428, chimney=297.50, heat_service=595, meter=952, pump=360, rebate=95.20, repair=892.50, light=595, paint=1428, theft=0, recovery=0, opening=2000, opening_price=1.08, closing=1500, oils=[(3500,1.05),(1500,.98),(3000,1.02)], opening_co2=287.03, pv=12, draft_date="2026-08-26", tenant_date="2026-08-26", cold=180, heat=120, rent=1450),
]
MONTHS = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
SUPPLIER_ADDRESSES = {
    "Kiezwerk Hausservice GmbH": "Feurigstraße 18, 10827 Berlin | Objektleitung Tom Albrecht | tom.albrecht@kiezwerk-hausservice.de",
    "Ringhof Hausdienst GmbH": "Naumannstraße 32, 10829 Berlin | Objektleitung Jule Martens | jule.martens@ringhof-hausdienst.de",
    "Lichtbogen Energie GmbH": "Tempelhofer Damm 92, 12101 Berlin | Kundenbetreuung Ronja Frank | service@lichtbogen-energie.de",
    "Berliner Wasserbetriebe": "Neue Jüdenstraße 1, 10179 Berlin | Kundenkonto Objektversorgung",
    "Berliner Stadtreinigungsbetriebe": "Ringbahnstraße 96, 12103 Berlin | Gebührenstelle Grundstücksservice",
    "Berolina Sachversicherung AG": "Bundesallee 181, 10717 Berlin | Vertragsservice Merle Simon | vertrag@berolina-sach.de",
    "Aufzugswerk Berlin GmbH": "Nonnendammallee 18, 13599 Berlin | Abrechnung Jens Reuter | service@aufzugswerk-berlin.de",
    "Schornsteinfegerbetrieb R. Pohl": "Friedrich-Wilhelm-Straße 19, 12103 Berlin | Ralf Pohl | buero@schornsteinfeger-pohl-berlin.de",
    "Wärmekreis Berlin GmbH": "Bessemerstraße 72, 12103 Berlin | Annette Grewe | service@waermekreis-berlin.de",
    "Messpunkt Berlin GmbH": "Manteuffelstraße 47, 12103 Berlin | Sonja Kranz | service@messpunkt-berlin.de",
    "Schließtechnik Ahrens GmbH": "Kolonnenstraße 53, 10829 Berlin | Thorsten Ahrens | buero@schliesstechnik-ahrens.de",
    "Elektro Klinker GmbH": "Alboinstraße 23, 12103 Berlin | Tobias Klinker | buero@elektro-klinker-berlin.de",
    "Malerbetrieb Weiß & Sohn": "Vorarlberger Damm 14, 12157 Berlin | Rainer Weiß | buero@weiss-maler-berlin.de",
    "Dachtechnik Rösner GmbH": "Ringstraße 21, 12105 Berlin | Erik Rösner | service@roesner-dachtechnik.de",
    "Havel Brennstoffe GmbH": "Hafenstraße 17, 13597 Berlin | Disposition Brigitte Arndt | lieferung@havel-brennstoffe.de",
}


def money(n):
    return f"{Decimal(str(n)).quantize(Decimal('.01'), rounding=ROUND_HALF_UP):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def rounded(n):
    return float(Decimal(str(n)).quantize(Decimal('.01'), rounding=ROUND_HALF_UP))


def para(text, size=10, heading=False, space=8):
    return Paragraph(escape(str(text)).replace("\n", "<br/>"), ParagraphStyle("body", fontName="Helvetica-Bold" if heading else "Helvetica", textColor=colors.white if heading else colors.black, fontSize=size, leading=size*1.4, spaceAfter=space))


def pdf(path, brand, address, recipient, heading, metadata, blocks, tone="#294a46"):
    path.parent.mkdir(parents=True, exist_ok=True)
    colour = colors.HexColor(tone)
    padding = 3 if heading in {"Betriebskostenabrechnung 2025", "Wärmekosten 2025: Übergebener Rechenbogen"} else 7
    story = [Paragraph(escape(brand), ParagraphStyle("brand", fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=colour)), para(address, 9), Spacer(1,22), para(recipient), Spacer(1,12)]
    for key, value in metadata:
        story.append(para(f"{key}: {value}",9))
    story += [Spacer(1,8), Paragraph(escape(heading), ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=15, leading=19, spaceAfter=15))]
    for block in blocks:
        if isinstance(block, str):
            story.append(para(block))
        else:
            rows, widths = block
            table = Table([[para(c,9,heading=index==0,space=0) for c in row] for index,row in enumerate(rows)],colWidths=widths,repeatRows=1,hAlign="LEFT")
            table.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,0),colour),("TEXTCOLOR",(0,0),(-1,0),colors.white),("VALIGN",(0,0),(-1,-1),"TOP"),("TOPPADDING",(0,0),(-1,-1),padding),("BOTTOMPADDING",(0,0),(-1,-1),padding),("ROWBACKGROUNDS",(0,1),(-1,-1),[colors.white,colors.HexColor("#f3f5f4")]),("LINEBELOW",(0,-1),(-1,-1),.5,colour)]))
            story += [table, Spacer(1,14)]
    def footer(c, d):
        c.saveState();c.setFont("Helvetica",8);c.setFillColor(colors.HexColor("#5e6467"))
        c.drawString(48,31,f"{brand} | {path.stem}");c.drawRightString(A4[0]-48,31,f"Seite {d.page}");c.restoreState()
    SimpleDocTemplate(str(path),pagesize=A4,leftMargin=48,rightMargin=48,topMargin=38,bottomMargin=54,title=heading,author=brand).build(story,onFirstPage=footer,onLaterPages=footer,canvasmaker=lambda *a,**kw:Canvas(*a,**dict(kw,invariant=1)))


def write_csv(path, headers, rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",encoding="utf-8",newline="") as stream:
        writer=csv.writer(stream,delimiter=";");writer.writerow(headers);writer.writerows(rows)


def build(case):
    c=case; root=ROOT/"testakten"/c["slug"]; belege=[]
    hm_issuer="Kiezwerk Hausservice GmbH" if c["units"]==12 else "Ringhof Hausdienst GmbH"
    hm_clerk="Tom Albrecht" if c["units"]==12 else "Jule Martens"
    def invoice(number, day, issuer, label, items, category, note, vat=19, paid=None):
        filename=f"{number}_{category}.pdf"; amount=rounded(sum(q*p for _,q,p in items))
        net=rounded(amount/(1+vat/100)) if vat else amount
        rows=[["Leistung", "Menge", "Einzel EUR", "Brutto EUR"]]+[[text,str(q),money(p),money(q*p)] for text,q,p in items]
        rows += [["Gesamtbetrag", "", "", money(amount)]]
        paragraphs=[f"Sehr geehrte Damen und Herren, für das Objekt {c['address']} berechnen wir die nachstehenden Leistungen. Leistungsort und Auftraggeber sind der Objektakte {c['code']} zugeordnet.",(rows,[271,45,70,113]),note]
        if vat: paragraphs.append(f"Im Gesamtbetrag enthalten: Entgelt {money(net)} EUR und {vat} Prozent Umsatzsteuer {money(amount-net)} EUR. Die Einzelpreise in der Tabelle verstehen sich einschließlich Umsatzsteuer.")
        elif category=="Wasser":
            water_net=rounded(amount*.45/1.07)
            paragraphs.append(f"Im Gesamtbetrag enthalten: Trinkwasser einschließlich Grundpreis {money(amount*.45)} EUR, darin 7 Prozent Umsatzsteuer {money(amount*.45-water_net)} EUR; Entwässerungsgebühren {money(amount*.55)} EUR ohne Umsatzsteuer. Die Teilbeträge ergeben zusammen den Gesamtbetrag.")
        else: paragraphs.append("Die ausgewiesenen Beträge enthalten keine Umsatzsteuer. Maßgeblich ist der bezeichnete Gebühren- beziehungsweise Versicherungszeitraum.")
        paragraphs += [f"Zahlungsreferenz: {number}. {'Die Gutschrift wird auf dem bestehenden Kundenkonto verrechnet.' if amount<0 else 'Zahlbar binnen 14 Tagen auf das im Lieferantenstamm hinterlegte Konto. Bei Rückfragen nennen Sie bitte die Rechnungsnummer und das Objektkennzeichen.'}", "Mit freundlichen Grüßen\nRechnungsstelle / Kundenservice"]
        pdf(root/"belege"/filename,issuer,SUPPLIER_ADDRESSES[issuer],f"{c['recipient']}\nc/o {c['manager']}\n{c['manager_address']}",label,[("Rechnungsnummer",number),("Datum",day),("Objekt",c["address"])],paragraphs)
        tax=rounded(amount*.45-rounded(amount*.45/1.07)) if category=="Wasser" else rounded(amount-net)
        belege.append(dict(number=number,date=day,issuer=issuer,label=label,category=category,amount=amount,vat=tax,file=f"belege/{filename}",paid=paid or (date.fromisoformat(day)+timedelta(days=10)).isoformat()))
    for m in range(1,13):
        last=calendar.monthrange(2025,m)[1];day=f"2025-{m:02d}-{last}"
        parts=[420,180,210,90] if c["units"]==12 else [380,150,190,80]
        invoice(f"{c['code']}-HM-{m:02d}",day,hm_issuer,f"Hausservice {MONTHS[m-1]} 2025",list(zip(["Treppenhausreinigung nach Wochenplan","Hofpflege, Sichtkontrolle und Winterbereitschaft","Technische Rundgänge, Müllbehälter und Leuchtmittelkontrolle","Schlüsselverwaltung, Terminabstimmung und Ableseorganisation"],[1]*4,parts)),"Hausservice",f"Leistungszeitraum 01.{m:02d}.2025 bis {last:02d}.{m:02d}.2025. Grundlage ist der Hausservicevertrag. Gesonderte Handwerkeraufträge sind in dieser Monatspauschale nicht enthalten. Die Einsatzblätter führt das Objektbüro; eine Rechnungskopie ist keine erneute Zahlungsanforderung.")
        invoice(f"{c['code']}-EL-{m:02d}",day,"Lichtbogen Energie GmbH",f"Strom Hauszugang und Treppenhaus {MONTHS[m-1]} 2025",[("Arbeitspreis, gemessener Monatsverbrauch",400 if c["units"]==12 else 320,.30),("Grundpreis und Messstellenbetrieb",1,20 if c["units"]==12 else 19)],"Allgemeinstrom",f"Zähler {c['code']}-A01; Verbrauch {400 if c['units']==12 else 320} kWh. Keine Abschlagsrechnung. Heizungsstrom, Photovoltaikeinspeisung und Tiefgarage werden unter anderen Messstellen geführt. Es besteht kein Liefervertrag über Haushaltsstrom einzelner Wohnungen.")
    annual=[
        ("WA","2026-01-16","Berliner Wasserbetriebe","Wasser und Entwässerung 2025","Wasser",c["water"],"Hauptzähler und Abwassergebühren laut Jahresbescheid. Enthalten sind sämtliche im Kalenderjahr 2025 gebuchten Gebühren einschließlich der Grundgebühr.",0),
        ("MU","2025-01-15","Berliner Stadtreinigungsbetriebe","Gebühren Abfallentsorgung 2025","Abfall",c["waste"],"Restmüll, Biotonne und Sperrmüll-Grundleistung nach Behältervertrag. Keine Entsorgung von Bauabfällen. Vier Quartalslastschriften betreffen diesen einen Jahresbescheid.",0),
        ("ST","2025-01-15","Berliner Stadtreinigungsbetriebe","Straßenreinigungsgebühren 2025","Strassenreinigung",c["street"],"Straßenabschnitt vor dem Grundstück; öffentliche Straßenreinigung nach Gebührenbescheid. Winterdienst auf privaten Hofflächen ist nicht Bestandteil dieser Gebühren.",0),
        ("VS","2024-12-17","Berolina Sachversicherung AG","Beitragsrechnung Wohngebäude 2025","Versicherung",c["insurance"],"Versicherungszeitraum 01.01.2025 bis 31.12.2025. Wohngebäude einschließlich Glas und Haus- und Grundbesitzerhaftpflicht. Versicherungssteuer ist enthalten. Kein Rechtsschutzbaustein.",0),
        ("AU","2025-12-19","Aufzugswerk Berlin GmbH","Wartung Personenaufzug 2025","Aufzug",c["lift"],"Vier Wartungstermine am 18.02., 13.05., 19.08. und 18.11.2025. Prüfung von Sicherheitseinrichtungen und Schmierung. Ersatzteile und Störungsbeseitigung werden gesondert berechnet.",19),
        ("SF","2025-11-12","Schornsteinfegerbetrieb R. Pohl","Kehr- und Messarbeiten 2025","Schornstein",c["chimney"],"Abgasweg und Ölkessel im Heizraum; Messung am 11.11.2025. Der Betrag betrifft ausschließlich die Zentralheizung und ist noch nicht in einer Wartungsrechnung enthalten.",19),
        ("HW","2025-09-25","Wärmekreis Berlin GmbH","Ölkesselwartung und Brennereinstellung","Heizungswartung",c["heat_service"],"Arbeitsbericht vom 24.09.2025: Brenner gereinigt, Düse gereinigt, Regelung geprüft, Abgasverlust gemessen. Keine Ersatzinvestition und keine Reparatur außerhalb der turnusmäßigen Wartung.",19),
        ("MD","2026-02-10","Messpunkt Berlin GmbH","Messdienst und Gerätemiete 2025","Messdienst",c["meter"],"Funkablesung Heizwärme und Warmwasser, Abrechnungsservice, Gerätemiete. Ablesung zum 31.12.2025. Die Messwerte werden im gesonderten Datenexport übergeben.",19),
        ("HP","2026-01-13","Lichtbogen Energie GmbH","Betriebsstrom Heizzentrale 2025","Heizstrom",c["pump"],"Separate Messstelle H01 für Brenner und Umwälzpumpen. 01.01.2025 bis 31.12.2025. Nicht im Allgemeinstrom enthalten.",19),
        ("GU","2025-10-02" if c["units"]==12 else "2025-06-03",hm_issuer,"Gutschrift Reinigungseinsatz","Gutschrift",-c["rebate"],"Bezug: September-Rechnung HM-09. Ausfall der Treppenhausreinigung am 05.09.2025, keine Nachholung. Vereinbarte Kürzung nach Reklamation." if c["units"]==12 else "Bezug: Mai-Rechnung HM-05. Reinigung am 16.05.2025 und Ersatztermin am folgenden Montag ausgefallen. Nächster regulärer Termin 23.05.2025. Vereinbarte Kürzung nach Reklamation.",19),
        ("TU","2025-07-22" if c["units"]==12 else "2025-10-09","Schließtechnik Ahrens GmbH","Fahrradkeller: Tür und Schließzylinder","Schloss",c["repair"],"Beschädigte Tür nach Aufbruch gesichert, Zylinder und Schließblech erneuert, Funktion geprüft. Schlüsselbestand bei Übergabe abgeglichen. Der Einsatz wurde vom Objektbüro nach Schadenmeldung ausgelöst.",19),
        ("LI","2025-10-14" if c["units"]==12 else "2025-10-10","Elektro Klinker GmbH","Störung Beleuchtung Treppenhaus" if c["units"]==12 else "Stromkasten Kellerflur: Abdeckung ersetzen","Lichtreparatur",c["light"],"Defekten Bewegungsmelder im zweiten Obergeschoss ersetzt; Leitung und Schutzschalter geprüft. Störungsmeldung vom Vorabend. Material und Montage enthalten; keine laufende Stromlieferung." if c["units"]==12 else "Beschädigte Abdeckung am Stromkasten im Kellerflur erneuert und Befestigung hergestellt. Meldung vom 07.10.2025. Keine Arbeiten an Ladepunkten oder Photovoltaikanlage.",19),
        ("MA","2025-08-25" if c["units"]==12 else "2025-10-27","Malerbetrieb Weiß & Sohn","Kellerzugang: Ausbesserung und Anstrich","Maler",c["paint"],"Stoßstellen verspachtelt, Wandfeld neben der Fahrradkellertür und angrenzenden Flur neu gestrichen. Abdeckung und Reinigung nach Arbeitsende enthalten. Abnahme durch den Hausservice.",19),
    ]
    for suffix,day,issuer,label,cat,amount,note,vat in annual:
        invoice(f"{c['code']}-{suffix}-2025",day,issuer,label,[(label,1,amount)],cat,note,vat)
    if c["theft"]:
        invoice(f"{c['code']}-KU-2025","2025-08-01","Dachtechnik Rösner GmbH","Fallrohr nach Kupferdiebstahl ersetzen",[("Kupferfallrohr, Befestigung und Montage",1,c["theft"])],"Fallrohr","Im Hof fehlten 3.8 Meter Fallrohr. Ersatz montiert und Ablauf geprüft. Bezug: Feststellung am 18.07.2025.")
    for idx,((litres,price),day) in enumerate(zip(c["oils"],["2025-02-12","2025-05-14","2025-10-16"]),1):
        co2=rounded(litres*2.68/1000*55*1.19)
        invoice(f"{c['code']}-OE-{idx:02d}",day,"Havel Brennstoffe GmbH","Heizöl EL schwefelarm",[("Heizöl EL, Lieferung in Liter",litres,price)],"Heizoel",f"Lieferung {litres} Liter bei 15 Grad Celsius; Energiegehalt {litres*10} kWh, Emissionsfaktor laut Lieferant 0.268 kg CO2/kWh. Brennstoffemissionen {litres*2.68:.0f} kg CO2. Im Bruttopreis enthaltene Kohlendioxidkosten {money(co2)} EUR bei einem Zertifikatepreis von 55 EUR/t CO2 zuzüglich 19 Prozent Umsatzsteuer. Diese Kosten sind kein Zuschlag zum Rechnungsbetrag. Lieferschein am Tankstutzen durch den Hausservice gegengezeichnet.")
    # Separate Originalbelege für die Vorratsbewertung, nicht erneut als Jahresaufwand buchen.
    invoice(f"{c['code']}-OE-2024","2024-12-16","Havel Brennstoffe GmbH","Heizöllieferung Dezember 2024",[("Heizöl EL, Lieferung in Liter",c["opening"],c["opening_price"])],"Vorjahreslieferung",f"Energiegehalt {c['opening']*10} kWh; Emissionsfaktor 0.268 kg CO2/kWh. Enthaltene Kohlendioxidkosten {money(c['opening_co2'])} EUR; Zertifikatepreis 45 EUR/t zuzüglich 19 Prozent Umsatzsteuer. Bezug: Tankaufnahme zum Jahreswechsel. Rechnung am 23.12.2024 ausgeglichen.",paid="2024-12-23")
    # Zahlenwerk enthält Buchungsquellen, nicht das Ergebnis einer rechtlichen Prüfung.
    write_csv(root/"zahlenwerk"/"Belegeingang_2025.csv",["Belegnummer","Datum","Aussteller","Bezeichnung","Brutto_EUR","Datei","Zahlungsdatum"],[[b[k] for k in ["number","date","issuer","label","amount","file","paid"]] for b in belege])
    opening=[("2025-01-01",c["opening"],"Peilstab und Tanktabelle; Aufnahme 08:10 Uhr",hm_clerk),("2025-02-12",c["oils"][0][0],"Zugang laut Lieferschein OE-01","Havel Brennstoffe"),("2025-05-14",c["oils"][1][0],"Zugang laut Lieferschein OE-02","Havel Brennstoffe"),("2025-10-16",c["oils"][2][0],"Zugang laut Lieferschein OE-03","Havel Brennstoffe"),("2025-12-31",c["closing"],"Peilstab und Tanktabelle; Aufnahme 09:35 Uhr",hm_clerk)]
    write_csv(root/"zahlenwerk"/"Tankbuch_2025.csv",["Datum","Liter","Vorgang","Erfasst_durch"],opening)
    areas=[96,96,102,98,100,100,108,100,96,98,102,104] if c["units"]==12 else [96,104,100,108,92,100,98,102]
    assert sum(areas)==c["area"]
    write_csv(root/"zahlenwerk"/"Flaechen_und_Messwerte_2025.csv",["Einheit","Wohnfläche_m2","Heizkostenverteiler_Einheiten","Warmwasser_m3","Zeitraum","Messstelle"],[[f"WE{i:02d}",a,6400+i*315,rounded(23+i*1.7),"01.01.2025 bis 31.12.2025",f"{c['code']}-W{i:02d}"] for i,a in enumerate(areas,1)])
    write_csv(root/"zahlenwerk"/"Mietkonto_2025.csv",["Buchungstag","Einheit","Kaltmiete_EUR","Vorauszahlung_Betrieb_EUR","Vorauszahlung_Heizung_EUR","Buchungstext"],[[f"2025-{m:02d}-03",c["unit"],c["rent"],c["cold"],c["heat"],f"Dauerauftrag {c['tenant']} {MONTHS[m-1]} 2025"] for m in range(1,13)])
    pdf(root/"belege"/"Tankaufnahme_und_Waermemessung.pdf",c["manager"],c["manager_address"],f"Objektakte {c['code']}","Tankaufnahme und Wärmemengenzähler",[("Stand","31.12.2025"),("Anlage","Ölkessel und zentrale Warmwasserbereitung")],["Tankdaten wurden am 01.01.2025 und 31.12.2025 durch zwei Mitarbeiter abgelesen. Liefermengen und Tankpeilungen werden nicht gleichgesetzt. Das Tankbuch enthält die einzelnen Zugänge.",([["Messgröße","01.01.2025","31.12.2025"],["Tankinhalt Liter",str(c["opening"]),str(c["closing"])],["Warmwasser-Wärmemengenzähler kWh","148000",str(148000+(26000 if c["units"]==12 else 19000))],["Wärmeerzeugung gesamt kWh","620000",str(620000+(104000 if c["units"]==12 else 76000))]],[245,127,127]),"Warmwasserbereitung wird mit einem eigenen Wärmemengenzähler erfasst. Die Wohnungsablesung zum 31.12.2025 enthält dagegen bewertete Einheiten der Heizkostenverteiler an den Heizkörpern und Warmwasservolumen in Kubikmetern. Heizkostenverteilereinheiten sind keine Kilowattstunden. Kein dokumentierter Geräteausfall und kein Nutzerwechsel.","Die Vorratsbewertung wird im Objektbüro nach dem Verbrauch der ältesten Liefermenge fortgeführt. Am Jahresende verblieb ausschließlich ein Teil der Lieferung vom 16.10.2025 im Tank. Maßgeblich sind die Lieferpreise einschließlich ausgewiesener Preisbestandteile.",f"Aufgenommen: {hm_clerk} und Sven Böhme, Hausservice\nÜbernommen in die Objektakte am 05.01.2026."])
    unit_tax=c["units"]==12
    for kind,title,day in [("Grundsteuerwert","Bescheidabschrift über den Grundsteuerwert","2024-04-09"),("Grundsteuermessbetrag","Bescheidabschrift über den Grundsteuermessbetrag","2025-01-07"),("Grundsteuer_2025","Bescheidabschrift über die Grundsteuer 2025","2025-01-14")]:
        value=c["tax_value"];mess=rounded(value*.00031)
        body=[f"Für die wirtschaftliche Einheit {c['address']}{', Wohnungseigentum WE07' if unit_tax else ', Mietwohngrundstück'} wird der im Verfügungssatz bezeichnete Betrag festgestellt beziehungsweise festgesetzt. Steuerpflichtiger: {c['owner']}. Die Angaben zum Wohnungseigentum erfassen ausschließlich die wirtschaftliche Einheit WE07; andere Wohnungen sind nicht Bestandteil dieses Bescheids." if unit_tax else f"Steuerpflichtiger: {c['owner']}. Die wirtschaftliche Einheit umfasst das gesamte Mietwohngrundstück {c['address']}. Sie ist nicht in Wohnungseigentum aufgeteilt."]
        if kind=="Grundsteuerwert":body += [f"Der Grundsteuerwert auf den 01.01.2022 beträgt {money(value)} EUR. Grundstücksart: {'Wohnungseigentum' if unit_tax else 'Mietwohngrundstück'}. Die Feststellung erfolgt für Zwecke der Grundsteuer ab 2025. Der festgestellte Wert wird als Grundlage für den gesonderten Messbescheid verwendet. Dieser Bescheid setzt noch keinen zu zahlenden Jahressteuerbetrag fest."]
        elif kind=="Grundsteuermessbetrag":body += [f"Der Grundsteuermessbetrag ab dem 01.01.2025 wird auf {money(mess)} EUR festgesetzt. Berechnung: Grundsteuerwert {money(value)} EUR multipliziert mit der für Wohngrundstücke geltenden Messzahl von 0.31 Promille. Der Hebesatz ist in diesem Messbetrag nicht enthalten."]
        else:
            body += [([["Berechnungsgrundlage","Wert"],["Messbetrag EUR",money(mess)],["Hebesatz Grundsteuer B 2025","470 Prozent"],["Festgesetzte Jahressteuer EUR",money(c["tax"])],["Vierteljahresrate EUR",money(c["tax"]/4)]],[325,174]),"Die Jahressteuer ist zu je einem Viertel am 15. Februar, 15. Mai, 15. August und 15. November fällig. Eine bestehende Lastschriftermächtigung wird berücksichtigt. Änderungen des Grundlagenbescheids werden nach dessen Wirksamwerden gesondert verarbeitet."]
        body += ["Rechtsbehelfsbelehrung: Gegen diesen Bescheid kann innerhalb eines Monats nach Bekanntgabe Einspruch beim ausstellenden Finanzamt schriftlich, elektronisch oder zur Niederschrift eingelegt werden. Der Einspruch soll den angefochtenen Bescheid bezeichnen. Ein Einspruch hemmt die Zahlungspflicht nicht.","Diese Abschrift wurde der Verwaltung aus der Post des Eigentümers überlassen. Finanzamt Schöneberg, Grundstücksstelle."]
        pdf(root/"belege"/(kind+".pdf"),"Finanzamt Schöneberg","Potsdamer Straße 140, 10783 Berlin | Grundstücksstelle",f"{c['owner']}\nObjekt {c['address']}",title,[("Datum",day),("Aktenzeichen",f"18/{'117' if unit_tax else '118'}/0925/{c['unit']}")],body,tone="#3e444a")
    # Schriftlicher Stand der Verwaltung mit nachvollziehbaren, ungeprüften Ansätzen.
    costs=[("Hausservice",c["hm"]*12),("Wasser und Abwasser",c["water"]),("Abfall",c["waste"]),("Straßenreinigung",c["street"]),("Wohngebäudeversicherung",c["insurance"]),("Aufzug",c["lift"]),("Allgemeinstrom",c["power"]*12),("Tür und Schließanlage",c["repair"]),("Treppenhausarbeiten",c["paint"]),("Beleuchtung",c["light"])]
    share=108/c["area"]; coldsum=sum(rounded(amount*share) for _,amount in costs)
    ground=c["tax"] if unit_tax else rounded(c["tax"]*share)
    raw_heat=rounded(sum(q*p for q,p in c["oils"])+c["heat_service"]+c["chimney"]+c["pump"]+c["meter"])
    heat_volume=sum(6400+i*315 for i in range(1,c["units"]+1))
    warm_volume=rounded(sum(23+i*1.7 for i in range(1,c["units"]+1)))
    my_heat=6400+int(c["unit"])*315; my_warm=rounded(23+int(c["unit"])*1.7)
    heat_parts=[rounded(raw_heat*.75*.30*share),rounded(raw_heat*.75*.70*my_heat/heat_volume),rounded(raw_heat*.25*.30*share),rounded(raw_heat*.25*.70*my_warm/warm_volume)]
    heating=rounded(sum(heat_parts))
    rows=[["Kostenart","Objekt EUR","Ihr Anteil EUR"]]+[[name,money(amount),money(rounded(amount*share))] for name,amount in costs]
    rows += [["Grundsteuer",money(c["tax"]),money(ground)],["Heizung / Warmwasser","gesonderter Rechenbogen",money(heating)]]
    cost_total=rounded(coldsum+ground+heating); credited=3300 if unit_tax else 3600; balance=rounded(cost_total-credited)
    sender_address = "Ruhlsdorfer Straße 28, 14513 Teltow" if unit_tax else c["manager_address"]
    pdf(root/"belege"/"Betriebskostenabrechnung_2025_versandt.pdf",c["owner"],sender_address,f"{c['tenant']}\nWE{c['unit']}, {c['address']}","Betriebskostenabrechnung 2025",[("Datum",c["tenant_date"]),("Abrechnungszeitraum","01.01.2025 bis 31.12.2025"),("Wohnfläche",f"108 m² / {c['area']} m²")],[f"Sehr geehrte Familie {'Seidel' if unit_tax else 'Öztürk'},\nanbei erhalten Sie die Abrechnung für Ihre Wohnung. Für die aufgeführten Kosten wurde der Anteil von 108/{c['area']} angesetzt, soweit die Position keinen gesonderten Nachweis enthält.",(rows,[259,110,130]),([["Berechnung","EUR"],["Kostenanteile gesamt",money(cost_total)],["Angerechnete Vorauszahlungen",money(credited)],["Nachzahlung",money(balance)]],[359,140]),"Bitte überweisen Sie den ausgewiesenen Betrag innerhalb von vier Wochen nach Zugang unter Angabe der Wohnung und des Abrechnungsjahres. Die Belege können nach Terminabstimmung im Verwaltungsbüro eingesehen werden. Die Verwaltungsunterlagen und der Rechenbogen der Wärmekosten sind Bestandteil der Abrechnungsmappe.",f"Mit freundlichen Grüßen\n{c['owner']}"])
    heat_rows=[["Wohnungsberechnung","Bezugsgrößen","EUR"],["Raumwärme Grundkosten",f"75 % x 30 % x 108/{c['area']}",money(heat_parts[0])],["Raumwärme Verbrauch",f"75 % x 70 % x {my_heat}/{heat_volume}",money(heat_parts[1])],["Warmwasser Grundkosten",f"25 % x 30 % x 108/{c['area']}",money(heat_parts[2])],["Warmwasser Verbrauch",f"25 % x 70 % x {money(my_warm)}/{money(warm_volume)}",money(heat_parts[3])],["Wohnung insgesamt","",money(heating)]]
    pdf(root/"belege"/"Waermekosten_Rechenbogen_2025.pdf","Messpunkt Berlin GmbH",SUPPLIER_ADDRESSES["Messpunkt Berlin GmbH"],c["manager"],"Wärmekosten 2025: Übergebener Rechenbogen",[("Datum","30.07.2026"),("Objekt",c["code"])],["Sehr geehrte Damen und Herren, die nachstehende Berechnung wurde mit den von Ihrem Objektbüro übergebenen Kostensummen erstellt. Nachträgliche Kostenänderungen teilen Sie uns bitte unter Angabe der betroffenen Rechnungen mit.",([["Ansatz","Gesamt EUR"],["Brennstoff",money(sum(q*p for q,p in c["oils"]))],["Wartung",money(c["heat_service"])],["Schornsteinfeger",money(c["chimney"])],["Betriebsstrom",money(c["pump"])],["Messdienst",money(c["meter"])],["Kosten insgesamt",money(raw_heat)]],[330,169]),f"Die gemessene Warmwasserwärme beträgt 25 Prozent der gemessenen Wärmeerzeugung. Verteilvorgabe für beide Kostenblöcke: 30 Prozent Grundkosten und 70 Prozent Verbrauchskosten. Übergebene Wohnfläche {c['area']} m². Wohnung WE{c['unit']}: 108 m².",(heat_rows,[185,229,85]),"Die Prozentsätze der Wohnungsberechnung beziehen sich jeweils auf die Gesamtkosten. Eine gesonderte Eigentümerquote aus Kohlendioxidkosten wurde vom Objektbüro noch nicht mitgeteilt. Der Tankbestand zum 31.12.2025 ist in der Übergabedatei nicht enthalten. Die Messdatei bleibt von der Kostendatei getrennt; die Zählerstände werden durch eine Änderung der Kostensumme nicht überschrieben.","Mit freundlichen Grüßen\nSonja Kranz, Abrechnung"])
    if unit_tax:
        pdf(root/"belege"/"Eigentuemerabrechnung_WE07_2025.pdf",c["manager"],c["manager_address"],"Katrin Schütte\nSondereigentum WE07", "Eigentümerkonto und Jahresabrechnung 2025",[("Datum",c["draft_date"]),("Objekt",c["address"])],["Sehr geehrte Frau Schütte, wir übersenden Ihnen den Stand Ihres Eigentümerkontos. Die nachstehend aufgeführten Beträge sind die Buchungen zur Einheit WE07 und enthalten neben laufenden Objektkosten auch die nicht verbrauchten Zuführungen und Verwaltungsvorgänge.",([["Buchungsbereich","WE07 EUR"],["Laufende Objektkosten laut Anlage",money(coldsum)],["Heizung und Warmwasser",money(heating)],["Verwaltervergütung", "428,40"],["Zuführung Erhaltungsrücklage","1.080,00"],["Sonderumlage Dachprojekt","450,00"]],[330,169]),"Die Grundsteuerbescheide für das Sondereigentum gehen unmittelbar an die jeweiligen Eigentümer. In den vorstehenden Gemeinschaftsbuchungen ist die Grundsteuer Ihrer Wohnung nicht enthalten. Ihre direkte Steuerzahlung kann daher nur anhand Ihres eigenen Bescheids und Zahlungsnachweises bearbeitet werden.","Die tatsächlichen Ausgaben für die Erhaltung werden aus dem Gemeinschaftskonto gezahlt. Die Rücklagenzuführung ist eine gesonderte Kontobewegung. Das Jahreskonto ersetzt weder die Einzelrechnungen noch die Beschlussniederschrift. Bitte teilen Sie Abweichungen zu Ihren Vorauszahlungen schriftlich mit.","Mit freundlichen Grüßen\nLea Wendt"])
    # Zahlungsbewegungen außerhalb der Lieferantenliste bleiben als eigene Originaldaten sichtbar.
    events=[["2025-01-03",c["tax"]/4,"Grundsteuer 1. Quartal","Finanzamt"],["2025-05-15",c["tax"]/4,"Grundsteuer 2. Quartal","Finanzamt"],["2025-08-15",c["tax"]/4,"Grundsteuer 3. Quartal","Finanzamt"],["2025-11-17",c["tax"]/4,"Grundsteuer 4. Quartal","Finanzamt"],["2025-12-18",-(c["recovery"] or 420),"Entschädigung Gebäudeschaden","Berolina Sachversicherung"],["2026-02-18",-round(c["pv"]*85.5,2),"PV Einspeisevergütung Kalenderjahr 2025","Netzabrechnung"]]
    events[0][0]="2025-02-17"
    write_csv(root/"zahlenwerk"/"Kontoauszug_Sonderbuchungen.csv",["Valuta","Belastung_EUR","Buchungstext","Partner"],events)
    insurance_scope="Diese Abrechnung betrifft nur die bezeichnete Schadenmeldung. " + ("Zum später gemeldeten Fallrohrdiebstahl liegt noch keine vollständige Dokumentation vor. " if unit_tax else "Nicht zum Gebäude gehörende bewegliche Gegenstände sind nicht mit erfasst. ") + "Bitte verwenden Sie bei weiterem Schriftverkehr die jeweilige Schadennummer."
    pdf(root/"belege"/"Versicherung_Schadenabrechnung.pdf","Berolina Sachversicherung AG",SUPPLIER_ADDRESSES["Berolina Sachversicherung AG"] ,c["recipient"],"Abrechnung Gebäudeschaden",[("Datum","12.12.2025"),("Schadennummer",f"BG-25-{c['code']}-17")],[f"Sehr geehrte Damen und Herren, wir schließen die Bearbeitung der am {'18.07.2025' if unit_tax else '07.10.2025'} gemeldeten Beschädigung am Fahrradkeller ab. Grundlage waren die eingereichte Schließtechnikrechnung, die Fotodokumentation des Hausservice und Ihre Angaben zum Zugang.",f"Zur Auszahlung kommen {money(c['recovery'] or 420)} EUR. Die Differenz zur eingereichten Rechnung ergibt sich aus dem vereinbarten Selbstbehalt und den nicht bestätigten Nebenpositionen. Der Betrag wird am 18.12.2025 auf das bisherige Beitragskonto ausgezahlt. Die Ersatzbeschaffung entwendeter Fahrräder ist nicht Gegenstand dieser Regulierung.",insurance_scope,"Mit freundlichen Grüßen\nMerle Simon, Sachbearbeitung Gebäudeschäden"])
    pdf(root/"belege"/"Angebot_Tiefgarage_Ladeinfrastruktur.pdf","Elektro Klinker GmbH",SUPPLIER_ADDRESSES["Elektro Klinker GmbH"] ,c["recipient"],"Angebot Grundinstallation Ladeinfrastruktur",[("Datum","08.12.2025"),("Angebot",f"EK-{c['code']}-TG-25")],["Sehr geehrte Damen und Herren, nach der Begehung der Tiefgarage bieten wir eine gemeinsame Grundinstallation mit Leitungsführung, Lastmanagement und Zählerschrankerweiterung an. Einzelne Ladepunkte sind nicht Bestandteil dieses Angebots.",([["Leistungsbestandteil","Netto EUR"],["Leitungswege und Kabeltrassen","6.000,00" if unit_tax else "4.000,00"],["Verteilung und Lastmanagement","7.000,00" if unit_tax else "5.000,00"],["Planung, Messkonzept und Inbetriebnahme","2.000,00" if unit_tax else "1.500,00"],["Gesamt einschließlich 19 Prozent Umsatzsteuer","17.850,00" if unit_tax else "12.495,00"]],[359,140]),"Ausführung frühestens nach Netzfreigabe und schriftlichem Auftrag. Gültigkeit bis 31.01.2026. Zum Datum dieses Angebots wurde keine Leistung ausgeführt. Die verfügbare Anschlussleistung und die Zuordnung der Stellplätze sind vor Auftragserteilung schriftlich zu bestätigen.","Mit freundlichen Grüßen\nTobias Klinker"])
    result=dict(c,belege=belege,areas=areas,draft_costs=costs,draft_ground=ground,draft_heating=heating,draft_total=cost_total,draft_credited=credited,draft_balance=balance)
    return result


if __name__=="__main__":
    output=Path(sys.argv[1]) if len(sys.argv)>1 else Path("/tmp/betriebskosten-daten.json")
    results=[build(c) for c in CASES]
    output.write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding="utf-8")
    print(f"{sum(len(c['belege']) for c in results)} Rechnungen/Bescheide zuzüglich Grundsteuer, Abrechnung und Messunterlagen; Daten: {output}")
