"""Geschäftsunterlagen der Autohaus Schönbuchring GmbH. Beträge in Euro."""
from datetime import date, timedelta

STICHTAG = date(2026, 9, 25)
FIRMA = "Autohaus Schönbuchring GmbH"
HAUS = "Hulbsteig 18 · 71034 Böblingen"
BANK = "Würmquell Gewerbebank eG"
D = "Grundakte/"
N = "Nachlieferung/"
# Objekt, interner Beleg, Vertragspartner, Grund, Fälligkeit, Betrag, Bezug
KREDITOREN = [
    ("K01","EA-971","Lackzentrum Böblinger Tal","Lack- und Karosserieaufträge","2026-09-18",19000,"Aufmaß 158 bis 173"),
    ("K02","EA-988","Radsatz Heckengäu KG","Herbstbevorratung","2026-09-21",12000,"Wareneingang 41"),
    ("K03","M-2609","Gewerbehof Hulbsteig KG","Septemberpacht","2026-09-22",11500,"Pachtkonto 18"),
    ("K04","EA-1004","Prüftechnik Calw GmbH","Hebebühnenservice","2026-09-25",9500,"Abnahme WB-26"),
    ("K05","EA-1011","Fahrzeugtransporte Birk","Hoftransport Juli/August","2026-09-29",9400,"Touren 81–96"),
    ("K06","EA-1013","Teilekontor Schönrain","Bremssätze und Kleinmaterial","2026-10-02",12600,"Wareneingang 52"),
    ("K07","EA-9882","Aufbereitung Schiltach","Rahmenlos Vorführwagen","2026-10-06",15400,"Sammelrechnung 09"),
    ("K08","EA-9917","Serviceverbund Gäu","Garantiearbeiten August","2026-10-09",15600,"Satzliste G-08"),
    ("K09","EA-1044","Energiepark Hulb","Ladesäulen und Werkstattstrom","2026-10-13",14200,"Ablesung August"),
    ("K10","EA-1050","Diagnosepool Glems","Diagnosegeräte und Lizenzen","2026-10-16",10800,"Jahresabrechnung"),
]
DEBITOREN = [
    ("F01","AR-482","Flieder Kurierdienst KG","Fuhrparkinspektion","2026-09-29",18000,"Avis FK-42"),
    ("F02","AR-489","Pflegedienst Höhenrain","Wartung und Ersatzwagen","2026-09-30",11000,"Avis PH-91"),
    ("F03","AR-493","Karosseriehaus Deufringen","Lackierarbeiten","2026-10-02",7500,"Avis KD-16"),
    ("F04","AR-497","Wohnmobile Glashütte KG","Werkstattlos Ausbau","2026-10-06",16000,"Avis WG-7"),
    ("F05","AR-500","Taxizentrale Mönchhalde","Achsreparatur und Teile","2026-10-09",8500,"Avis TM-34"),
    ("F06","AR-505","Getriebepool Nagold","Überholte Getriebe","2026-10-14",15000,"Avis GN-22"),
    ("F07","AR-511","Lerchenweg Sozialmobil","Wartungsrahmen","2026-10-16",10000,"Avis LS-55"),
    ("F08","AR-130","Schwanenflug Mobilität GmbH","Unfallschaden, Abnahme strittig","2026-08-03",22000,"Anwaltsschreiben S-18"),
]
# Bestands- und Kommissionsfahrzeuge. Freihanderlös nach Kosten und Steuerabrechnung.
AUTOS = [
 ("SB-071","Kombi S1 · graublau","Erwerb / Lagerfinanzierung",36000,31000,26000),
 ("SB-083","Kompaktvan H2 · silber","Erwerb / Lagerfinanzierung",32000,28000,24000),
 ("SB-094","Kastenwagen V4 · achat","Erwerb / Lagerfinanzierung",41000,35000,32000),
 ("SB-107","Elektrolimousine E6 · grün","Erwerb / Lagerfinanzierung",37000,30000,27000),
 ("SB-116","Hochdachkombi T3 · weiß","Erwerb / Lagerfinanzierung",28000,24000,21000),
 ("SB-121","Crossover W2 · braun","Erwerb / Lagerfinanzierung",32000,26000,10000),
 ("KO-017","Oldtimer C · rot","Kommission Marquardt",0,0,0),
 ("KO-020","Camper R · sand","Kommission Renz",0,0,0),
]
AKTIVA = [
 ("A01","Hausbank und Barkasse",52000,52000,"B01–B03, N01; Bank brutto inkl. Sicherungsguthaben"),
 ("A02","Lieferforderungen",108000,94000,"O02, N04; sieben Avis und Vergleichsofferte"),
 ("A03","Fahrzeuge im Eigenbestand",206000,174000,"V01, N02; sechs Lagerfahrzeuge"),
 ("A04","Werkstattausstattung",78000,41000,"N02; Hebebühnen, Diagnose und Kabine"),
 ("A05","Ersatzteile und Räder",30000,17000,"N02; Rücknahmeangebot nach Sortierung"),
 ("A06","Aktive Rechnungsabgrenzung",12000,0,"F01, N02; nicht abtretbares Wartungspaket"),
]
PASSIVA = [
 ("P01","Lieferanten und Vermieter",130000,130000,"O01 K01–K10; zehn bestehende Verpflichtungen"),
 ("P02","Einkaufsfinanzierung",140000,140000,"V01, V02; Summe sechs Ablösebeträge"),
 ("P03","Investitionsdarlehen",50000,50000,"F01, B04, N01; Betriebskonto getrennt"),
 ("P04","Gesellschafterdarlehen",115000,115000,"F02; Endfälligkeit 31.03.2027"),
 ("P05","Gewährleistungsrückstellung",20000,20000,"F01, N02; noch offene Einzelvorgänge"),
]
VERKEHR = [
 ("2026-08-31","Übertrag vom Vormonat",106000),
 ("2026-09-02","W-562 / Kundensammelabrechnung",18000),
 ("2026-09-04","Löhne Vorperiode / Sammelauftrag",-29500),
 ("2026-09-08","Ablöse SB-058 / Einkaufslinie",-27500),
 ("2026-09-10","Gebrauchtwagen / Kaufpreis SB-058",33000),
 ("2026-09-14","USt August und betriebliche Abgaben",-19000),
 ("2026-09-16","Gebäude und Versicherung / Lastschrift",-7200),
 ("2026-09-18","Teileauftrag EA-928",-10800),
 ("2026-09-21","Kartenabrechnung Werkstatt W-320",12500),
 ("2026-09-22","Werkstattlöhne / Abschlag September",-20900),
 ("2026-09-23","Ablöse SB-066 / Einkaufslinie",-30600),
 ("2026-09-24","Fahrzeugzahlung SB-066 / Freigabe 24.09.",32000),
 ("2026-09-25","Sozialversicherung und Lohnrest / Sammelauftrag",-6000),
]
# Planungsdatei der Geschäftsführung. Erstes 21-Tage-Fenster basiert allein auf OP.
WOCHEN_EIN = [36500,24500,25000,46000,51000,38500,48500,52000,40500,61000,37500,45000,35000]
WOCHEN_AUS = [74000,31000,25000,39000,54500,44500,45500,50000,43000,53500,42500,47000,41500]
MONAT_EIN = [145000,156000,148000,162500,171000,148000,160000,147000,155000]
MONAT_AUS = [152000,151000,146000,272500,166000,147000,155000,149000,153000]
def wochen():
    return [(STICHTAG+timedelta(days=1+i*7), STICHTAG+timedelta(days=7+i*7),
             e,a) for i,(e,a) in enumerate(zip(WOCHEN_EIN, WOCHEN_AUS))]
