---
name: lage-und-ausstattung-erheben
description: Strukturierte Datenerhebung fuer die Einordnung in den Mietspiegel — Adresse Baujahr Wohnflaeche Bad Kueche Heizung Wohnungsausstattung Gebaeudeausstattung. Erfasst alle Merkmale die in qualifizierten Mietspiegeln als Sondermerkmale bewertet werden (Bodenbelag Fenster Balkon Terrasse Aufzug Stellplatz Energieeffizienz). Erzeugt eine Checkliste und ein strukturiertes Erhebungsprotokoll als Grundlage fuer ortsuebliche Vergleichsmiete Mieterhoehung Mietsenkungsverlangen oder Klage.
---

# Lage und Ausstattung erheben

Dieser Skill leitet eine vollständige Datenerhebung an. Ergebnis ist ein strukturiertes Protokoll, das in jeden anderen Skill dieses Plugins einfliesst.

## Disclaimer

Diese Erhebung ersetzt keine Rechtsberatung. Sie ist ein Vorbereitungsschritt für eine spätere rechtliche Prüfung. Bei strittigen Punkten amtliche Quellen heranziehen oder Rechtsrat einholen.

## Workflow

### 1. Adresse und Lage

- Vollständige Adresse (Straße, Hausnummer, PLZ, Ort).
- Stadt-/Stadtteil/Quartier.
- Wohnlagen-Zuordnung nach dem amtlichen Straßenverzeichnis oder Geoportal der Stadt (einfach / mittel / gut). Wenn unklar: Link auf das amtliche Verzeichnis aus references/mietspiegel-quellen.md.

### 2. Gebäude

- Baujahr (laut Mietvertrag, Grundbuchauszug oder Bauakte).
- Letzte umfassende Modernisierung (Jahr, Umfang).
- Anzahl Wohneinheiten.
- Aufzug ja/nein.
- Stellplatz/Garage zur Wohnung gehoerig.
- Energieausweis (Verbrauch oder Bedarf, kWh/(m² · a)).

### 3. Wohnung

- Wohnfläche in m² nach Wohnflächenverordnung (WoFlV).
- Anzahl Zimmer.
- Stockwerk.
- Bodenbelaege je Raum (Parkett, Laminat, Fliesen, Teppich).
- Fenster (Doppel- oder Dreifachverglasung, Holz/Kunststoff).
- Balkon / Loggia / Terrasse (Größe, Ausrichtung).
- Keller / Abstellraum außerhalb der Wohnung.

### 4. Bad

- Anzahl Baeder/WCs.
- Wanne und/oder Dusche.
- Fenster im Bad.
- Bodenheizung.

### 5. Küche

- Einbauküche mitvermietet ja/nein.
- Geräte (Herd, Backofen, Kuehlschrank, Geschirrspueler).

### 6. Heizung und Warmwasser

- Heizungsart (Gas, Fernwaerme, Oel, Waermepumpe).
- Zentral oder Etagenheizung.
- Warmwasserbereitung (zentral, dezentral, über Heizung).

### 7. Mietvertrag

- Vertragsdatum.
- Aktuelle Nettokaltmiete und Vorauszahlungen.
- Indexmiete, Staffelmiete oder Festmiete.
- Schönheitsreparaturklausel (im Original-Wortlaut zitieren).
- Schlüsselgeld, Kaution.

## Ausgabe

Protokoll als Markdown mit den oben genannten Abschnitten plus Quellenangabe (woher stammt jede Information: Mietvertrag, Augenschein, Energieausweis, Straßenverzeichnis). Dieses Protokoll ist Input für alle weiteren Skills.

## Aktuelle Rechtsprechung — Leitsaetze

- BGH, Urt. v. 14.12.2022 — VIII ZR 304/21, NJW 2023, 1289 Rn. 28: Ein qualifizierter Mietspiegel ist Sachverstaendigenzeugnis im Sinne von § 558a BGB; das Gericht darf ihn nicht ohne nachvollziehbare Begruendung beiseitelassen.
- BGH, Urt. v. 21.09.2022 — VIII ZR 188/21, NJW 2022, 3580 Rn. 18: Wohnlage ist nach dem jeweils geltenden Mietspiegel zu bestimmen; fehlerhafte Einordnung durch den Vermieter macht das Mieterhoehungsverlangen formell unwirksam, wenn die Wohnlage unrichtig angegeben ist.
- BGH, Urt. v. 19.04.2023 — VIII ZR 201/22, NJW 2023, 2059 Rn. 22: Modernes Bad bedeutet im Mietspiegel-Kontext: Wannenbad oder Dusche mit Fliesenboden; fehlende Fliesen koennen zu Wohnwertabzug fuehren.

## Paragrafenkette

- Ortsueblliche Vergleichsmiete: § 558 BGB
- Begruendungsmittel: § 558a BGB
- Kappungsgrenze: § 558 Abs. 3 BGB

## Kommentarliteratur

- Schmidt-Futterer, Mietrecht, 15. Aufl. — § 558a BGB Rn. 1 ff. Mietspiegel
- BeckOK Mietrecht — § 558 BGB Mietspiegelrecht
