---
name: energierecht-netz-speicher-zugang
description: "Netzanschluss und Netzzugang für Erzeugungsanlagen und Speicher prüfen. Normen: §§ 17 ff. 20 ff. EnWG, NAV. Prüfraster: Netzanschlussrecht, Anschlussbegehren, Kapazitaetsprüfung, Diskriminierungsfreiheit. Output: Netzanschluss-Rechtsgutachten. Abgrenzung: nicht EEG-Verguetungsrecht."
---

# Netz- und Speicher-Zugang

## Zweck

Behandelt Konflikte rund um Netzanschluss, Engpass-Management, Netzentgelte und Speicher-Sonderregelungen. Mandant typisch Erzeuger, Industriekunde, Speicher-Betreiber oder Netzbetreiber.

## Eingaben

- Anlagen-Typ und Leistung
- Standort (Netzgebiet, Verteilnetz vs. Übertragungsnetz)
- Aktueller Status (Antrag, Bestätigung, Ablehnung, Streit)
- Anschluss-Kosten geltend gemacht
- Netzentgelt-Festsetzung BNetzA für relevantes Jahr
- Bilanzkreis und Marktrollen

## Schritt 1 — Netzanschluss-Anspruch

### § 17 EnWG / § 8 EEG

- Anschluss-Pflicht Verteilnetzbetreiber für EE-Anlagen vorrangig § 8 EEG
- Sonstige Anlagen § 17 EnWG, Verhältnismäßigkeits-Prüfung
- Pflichtbestätigung mit Kosten-Schätzung binnen 8 Wochen

### Anschluss-Punkt

- Wirtschaftlich günstigster Punkt im technisch geeigneten Netzabschnitt
- Bei Streit Sachverständigen-Verfahren
- BNetzA-Festlegungen zu Anschluss-Standardisierung

### Anschluss-Kosten und Baukostenzuschuss

- Erzeugungs-Anlagen: Anschluss-Kosten typisch Anschluss-Begehrender (Anlage); ab Anschluss-Punkt Netzbetreiber
- Verbrauchs-Anlagen: Baukostenzuschuss nach NDAV / NAV
- BGH-Linie zu Baukostenzuschuss-Höhe

### Anschluss-Verweigerung

- Nur bei wirtschaftlicher Unzumutbarkeit Netzbetreiber
- "Wirtschaftliche Unzumutbarkeit" eng auszulegen — BNetzA-Maßstab
- Bei Verweigerung: Beschwerde BNetzA § 31 EnWG, danach OLG-Beschwerde § 75 EnWG

## Schritt 2 — Engpass-Management § 13 EnWG

### Drei Stufen

1. **Netzbezogene Maßnahmen** (Topologie-Wechsel, Spannungs-Anpassung)
2. **Marktbezogene Maßnahmen** (Redispatch, Bilanzkreis-Intervention)
3. **Notfall-Maßnahmen** (Abschaltungen)

### Redispatch 2.0 (seit 01.10.2021)

- **Alle Anlagen ab 100 kW** in Redispatch-Pflicht (auch EE-Anlagen!)
- Einspeise-Management durch Netzbetreiber bei Engpass
- Entschädigungs-Anspruch des Anlagen-Betreibers nach § 13a EnWG / § 15 EEG
- Daten-Übermittlungspflicht (Netzbetreiber-Vorgabe)

### Spitzenkappung § 11 Abs. 2 EnWG

- Verteilnetzbetreiber darf bis 3 % der jährlichen Energiemenge wegkappen
- Ohne Entschädigung
- BNetzA-Festlegung BK6-21-301

### Streitige Sachverhalte

- Falsche Engpass-Berechnung
- Diskriminierende Reihenfolge der Anlagen-Auswahl
- Entschädigungs-Höhe

## Schritt 3 — Netzentgelte und Anreizregulierung

### ARegV (Anreizregulierungsverordnung)

- Erlös-Obergrenze pro Netzbetreiber für 5-Jahres-Periode
- BNetzA-Festsetzung
- Effizienz-Werte als Vergleichsmaßstab
- Q-Faktor (Qualitätszuschlag/-abzug)

### StromNEV

- Berechnungs-Methodik Netzentgelte
- Netznutzungs-Entgelt für Endkunden
- Differenzierung Last-Profil, Spitzen-Last, Jahreshöchst-Last

### Gas: GasNEV

- Analog Strom, mit Sonder-Mechanismen für Speicher / Saisonale Schwankungen

### Streit BNetzA-Beschluss

- Beschluss BK4/BK6/BK8/BK9 — verschiedene Beschlusskammern
- Anhörungs-Beschluss → Festlegungs-Beschluss → Beschwerde OLG Düsseldorf § 75 EnWG
- Frist ein Monat

## Schritt 4 — Sondernetzentgelte Industrie § 19 StromNEV

### § 19 Abs. 1 StromNEV

- "Atypisches" Nutzungsverhalten
- Reduzierte Netzentgelte für Last-Profile außerhalb der Last-Spitze

### § 19 Abs. 2 Satz 1 StromNEV

- "Stromintensive Verbraucher" — bestimmte Verbrauchsstunden
- Reduzierung bis auf 20 % Standard-Entgelt

### § 19 Abs. 2 Satz 2 StromNEV

- "Bandlast-Privileg"
- Verbrauch ≥ 7.000 Vollbenutzungs-Stunden + ≥ 10 GWh/Jahr
- Ab 7.000 h: 20 % Entgelt; ab 7.500 h: 15 %; ab 8.000 h: 10 %
- **Antragsfrist: 30.09. für Folgejahr** beim Netzbetreiber

### Verfassungsrechtliche Probleme

- EuGH 02.09.2021, C-718/18: Unabhaengigkeit BNetzA als Regulierungsbehoerde; nationaler Gesetzgeber darf die Tarif-Festlegungskompetenz nicht beschraenken (curia.europa.eu).
- BNetzA-Festlegungen zu Anwendungs-Modalitaeten: aktuelle Festlegungs-Aktenzeichen vor Ausgabe ueber bundesnetzagentur.de pruefen

### Streit-Konstellation

- Antrag Sondernetzentgelt zurückgewiesen
- Beschwerde BNetzA → OLG Düsseldorf
- Skill `energierecht-industriekunden` für Detail

## Schritt 5 — Speicher

### Speicher-Doppelnutzungs-Privileg

- Speicher ist gleichzeitig Verbraucher (Lade-Phase) und Erzeuger (Entlade-Phase)
- **Vermeidungs-Vorschrift** § 118 EnWG: keine doppelte Netzentgelt-Belastung
- Stand 2024: zeitlich befristete Privilegierung bis 2029 (in Reform)

### Großspeicher

- Anschluss an Übertragungsnetz möglich
- Vermarktung als Regelenergie-Anbieter (Sekundärregelreserve, Minutenreserve, FCR)
- Netzentgelt-Befreiung gemäß § 118 Abs. 6 EnWG

### Heim-Speicher

- Verteilnetz-Anschluss
- Nutzung für Eigenverbrauch + Netzeinspeisung
- Marktstammdatenregister-Eintrag

### Wasserstoff-Speicher

- Sondernormen Wasserstoff-Netz-Verordnung
- Übergangsregelung Gasnetz-Mit-Nutzung
- Förderung KfW BEW / Klimaschutzverträge

## Schritt 6 — Bilanzkreis und Marktrollen

### Bilanzkreis-Verantwortlicher (BKV)

- Übernimmt Bilanzierung-Pflicht
- ÜNB Bilanzkreis-Vertrag
- Ausgleichsenergie bei Abweichungen

### GPKE / GeLi-Gas-Prozesse

- Standardisierte Marktrollen-Prozesse
- BNetzA-Festlegung MaBiS / WiM

### Marktstammdatenregister

- Zentrale BNetzA-Datenbank
- Eintragungs-Pflicht Anlagen / Marktakteure
- § 5 MaStRV

## Schritt 7 — EU-Bezug

### EU-Strommarktordnung 1227/2011 (REMIT)

- Markt-Transparenz, Insiderhandel-Verbot
- Bilanzkreis-Daten-Übermittlung
- BNetzA-Sanktionen bei REMIT-Verstoß

### EU-Strommarkt-Reform 2024

- Flexibilitäts-Mechanismen verstärken
- Capacity-Markt-Optionen für Mitgliedstaaten

### EuGH-Linie (verifiziert curia.europa.eu)

- EuGH 02.09.2021, C-718/18 — Unabhaengigkeit der Regulierungsbehoerde BNetzA; Tarif-Festlegung Strom und Gas
- Weitere EuGH-Entscheidungen zur Diskriminierungsfreiheit beim Netzzugang vor Ausgabe konkret ueber curia.europa.eu verifizieren

## Schritt 8 — Streit-Strategie

### Bei Netzanschluss-Problem

1. Schriftverkehr mit Netzbetreiber sortieren
2. § 17 EnWG / § 8 EEG-Anspruch prüfen
3. Wirtschaftlichkeits-Argument einbringen
4. BNetzA-Beschwerde § 31 EnWG
5. Vor OLG-Beschwerde (Frist 1 Monat ab BNetzA-Bescheid)

### Bei Netzentgelt-Streit

1. BNetzA-Festlegung studieren
2. Maßstab Anreizregulierung
3. Beschwerde BNetzA
4. OLG-Beschwerde

### Bei Engpass-Entschädigung

1. Daten-Übermittlung verifizieren
2. Entschädigung berechnen nach § 13a EnWG
3. Klage VG bei strittig
4. Skill `energierecht-verfahren`

## Aktuelle Rechtsprechung & Leitsätze (Stand 05/2026)

- **EuGH 02.09.2021, C-718/18** (Kommission ./. Deutschland, Strom- und Gasmarkt): Deutschland hat gegen die Richtlinien 2009/72/EG und 2009/73/EG verstossen — die Bundesnetzagentur muss umfassende Entscheidungsbefugnisse zur Festlegung der Tarife und Netznutzungsbedingungen haben (Unabhaengigkeit der Regulierungsbehoerde). Quelle: curia.europa.eu (CELEX 62018CJ0718).
- **BVerwG 09.06.2010, 9 A 20.08** (Bahnstromleitung): Anforderungen an Planfeststellung; immissionsschutzrechtliche Massgaben. Quelle: bverwg.de.
- **BGH (EnVR-Senat)**: Laufende Senatsrspr. zur ARegV, StromNEV-Anwendung; konkrete Aktenzeichen vor Ausgabe per bundesgerichtshof.de / OLG Duesseldorf (3. Kartellsenat) verifizieren.
- **OLG Duesseldorf VI-3 Kart**: laufende Senatsrspr. zu BNetzA-Beschluessen; oeffentliche Entscheidungsdatenbank olg-duesseldorf.nrw.de.
- **EnWG-Reform 2023/2024** (BGBl. I 2023 S. 1565 — EnWG-Aenderung im Rahmen Solarpaket I; sowie BGBl. I 2024): Umsetzung der EU-Strommarkt-Reform 2024/1747.

Konkrete Beschwerdeentscheidungen vor Ausgabe per olg-duesseldorf.nrw.de / bundesgerichtshof.de verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 17 EnWG (Netzanschluss-Pflicht) — § 8 EEG (Anschluss EE-Anlagen vorrangig) — § 13 EnWG (Engpass-Management) — § 13a EnWG (Redispatch-Entschaedigung) — § 19 StromNEV (Sondernetzentgelte) — § 118 EnWG (Speicher-Privileg) — §§ 31, 75 EnWG (BNetzA-Beschwerde, OLG-Beschwerde)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verzahnung

- `energierecht-eeg-kwkg-erzeugung` — Erzeugungs-Anlagen
- `energierecht-industriekunden` — § 19 StromNEV-Detail
- `energierecht-verfahren` — BNetzA-Beschwerde
- `energierecht-projektfinanzierung` — Speicher-Finanzierung

## Quellen

- EnWG 2024 §§ 8, 11, 13, 13a, 17, 31, 65, 75, 118
- EEG 2023 § 8, § 15
- StromNEV § 19
- GasNEV
- ARegV
- NAV / NDAV
- MaStRV § 5
- BNetzA-Beschlüsse BK4 / BK6 / BK8 / BK9 — bundesnetzagentur.de
- BGH EnVR-Linien — vor Ausgabe konkretes Aktenzeichen ueber bundesgerichtshof.de verifizieren
- OLG Düsseldorf VI-3 Kart-Verfahren — olg-duesseldorf.nrw.de
- EuGH 02.09.2021, C-718/18 — Unabhaengigkeit BNetzA als Regulierungsbehoerde (curia.europa.eu)
- EU REMIT 1227/2011
- EU-Strommarktordnung 2019/943 + Reform VO (EU) 2024/1747
