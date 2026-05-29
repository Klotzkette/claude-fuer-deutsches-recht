---
name: energierecht-eeg-kwkg-erzeugung
description: "EEG- und KWKG-Verguetungen für Stromerzeugungsanlagen prüfen: Einspeiseverguetung, Marktpraemie, KWK-Zuschlag. Normen: §§ 19 ff. EEG, §§ 6 ff. KWKG. Prüfraster: Anlagenanschluss, Verguetungsmodalitaeten, Direktvermarktung, Ausschreibungspflicht. Output: Verguetungsberechnung EEG und KWKG. Abgrenzung: nicht Netzanschlussrecht."
---

# EEG, KWKG und Erzeugung erneuerbarer Energien

## Zweck

Zentrale Skill-Norm für Erzeugungs-Anlagen (Wind, Solar, Biomasse, KWK, Wasser, Geothermie). Behandelt Vergütungs-Mechanismen, Ausschreibungs-Verfahren, Anlagen-Zulassung und typische Streit-Konstellationen.

## Eingaben

- Anlagen-Typ (Wind, Photovoltaik, KWK, Biomasse, Wasserkraft, Geothermie)
- Installierte Leistung kW / MW
- Inbetriebnahme-Datum oder geplantes Datum
- Ausschreibungs-Teilnahme (Zuschlag, Höchst-Wert)
- Marktstammdatenregister-Eintrag (MaStR-Nummer)
- Förder-Bezug (EEG-Vergütung, KWKG-Zuschlag, BImSchG-Genehmigung, Investitions-Förderung)
- Netzbetreiber und Bilanzkreis

## Schritt 1 — Förder-Architektur EEG 2023

### Marktprämie + Direktvermarktung § 19, § 20 EEG

Standard-Fall: Anlagen ab 100 kW (Solar 100 kWp ab 2025, schrittweise reduziert). Vermarktung über Direktvermarkter; EEG zahlt Marktprämie als Differenz zwischen anzulegendem Wert und Marktpreis.

### Feste Einspeise-Vergütung § 21 EEG

Kleinanlagen unter 100 kW (Solar). Vergütung direkt vom Netzbetreiber.

### Anzulegender Wert

Aus Ausschreibung (Wind, Solar > 1 MW) oder gesetzlich festgelegt (Kleinanlagen, Biomasse Bestand). Inflations-Anpassung nach § 51a EEG (seit 2024 stärker eingeführt).

### Ausschreibungs-Verfahren

- **Wind onshore**: jährlich vier Termine, anzulegender Wert je MWh, Höchstwert 7,35 ct/kWh (Stand 2024, jährliche Anpassung BNetzA)
- **PV-Freifläche > 1 MW**: vier Termine pro Jahr
- **PV-Dach > 1 MW**: separate Ausschreibung
- **Biomasse**: zweimal pro Jahr
- **Wind offshore**: Bundesfachplan-Ausschreibung BSH

### Innovationsausschreibung § 39o EEG

Speicher-Kombinationen, KWK-Hybride, besondere Anlagenkonzepte. Zuschlag in MWh-Vergütung statt Cent/kWh.

## Schritt 2 — KWKG 2023

### Zuschlag-Berechtigte Anlagen § 5 KWKG

- Neuanlagen, modernisierte Anlagen, Bestandsanlagen
- Brennstoffe: Erdgas, biogene Brennstoffe, Wasserstoff (ab 2025 mit gestaffelter Quote)
- Leistungs-Klassen: < 50 kW, 50 — 100 kW, 100 — 250 kW, 250 — 2 MW, > 2 MW

### Zuschlags-Höhen

Gestaffelt nach Leistung und Inbetriebnahme. Zuschlags-Dauer typisch 30.000 — 45.000 Vollbenutzungs-Stunden.

### Wasserstoff-Quote

Seit 2024 Pflicht zu schrittweisem H2-Ready-Standard für Anlagen > 10 MW (KWKG-Reform 2023).

### Förderfähigkeits-Antrag § 10 KWKG

- BAFA als zuständige Behörde (für Standard-Anlagen)
- BNetzA für Ausschreibungs-KWK
- Frist-genau prüfen

## Schritt 3 — Anlagen-Zulassung und Genehmigung

### Marktstammdatenregister § 33 EEG

- **Eintragungs-Pflicht** binnen ein Monat nach Inbetriebnahme
- BNetzA-Webportal
- Bei Versäumnis: **anzulegender Wert auf null** § 33 Abs. 6 EEG bis zur Eintragung
- Strenge Verwaltungspraxis BNetzA

### BImSchG-Genehmigung

- Windkraftanlagen > 50 m Gesamthöhe: § 4 BImSchG förmliches Verfahren
- Biogas-Anlage > 1,2 MW: Standard-Verfahren
- Sammlung Antrags-Unterlagen: Schallgutachten, Schattenwurfprognose, artenschutzrechtliche Prüfung (saP), Bauantrag

### Solar-Freiflächen / Wind: Bauleitplanung-Bezug

- Wind: ab 1.000 m zu nächster Wohnbebauung (Bundesland-Regelung Bayern 10H abgeschafft 2023)
- Solar: Acker- und Grünland-Standorte mit eingeschränkten Möglichkeiten
- Beschleunigungs-Gebiete EU-RED III: Pflicht ab 21.02.2026 zu deren Ausweisung

### WindBG / SolarBG

- Windflächenbedarfsgesetz 2022: Länder-Quote Mindestflächen
- Solarpaket I 2024: vereinfachte Anlagenzulassung Mieterstrom, Direktversorgung

## Schritt 4 — Repowering und Modernisierung

### Repowering Wind § 23b EEG

- Ersatz Bestandsanlage durch leistungsstärkere Neuanlage am gleichen Standort
- Anrechnungs-Mechanismus
- Bevorzugte Behandlung in Ausschreibungen

### Modernisierung KWK § 5 Abs. 2 KWKG

- Mindest-Wert-Erhaltung von Bestandsanlagen
- Neuer Zuschlag bei wesentlicher Modernisierung

### Speicher-Hybridisierung

- Innovationsausschreibung
- Doppelvermarktungs-Verbot beachten

## Schritt 5 — Streit-Konstellationen

### Vergütungs-Streit mit Netzbetreiber

- Anlagenzulassung erfolgt aber Vergütung verweigert
- BGH-EnVR-Senat: laufende Rechtsprechung zum Anlagenbegriff und zur Verguetung — vor Ausgabe Aktenzeichen ueber bundesgerichtshof.de verifizieren
- Klärung Streit ueber Schiedsverfahren bei der BNetzA (§ 81 EEG) oder Klage Zivilgericht

### Bei nicht-rechtzeitiger MaStR-Eintragung

- Anlage in Betrieb, Eintrag fehlt
- Korrektur möglich, aber Vergütungs-Sperre für Zwischen-Zeitraum
- BNetzA-Verwaltungspraxis prüfen

### Ausschreibungs-Zuschlag versäumt

- Anlage gebaut, Zuschlag verfehlt
- Alternative: feste Einspeise-Vergütung bei Kleinanlagen / Sonder-Konstellationen
- Wenn kein Förderanspruch: Marktvermarktung über Direktvermarkter, PPA

### Bei Bürgerwindprojekten

- Bürgerenergiegesellschaft § 3 Nr. 15 EEG
- Privilegierungen in Ausschreibung
- Mitglieder-Anteils-Mindestanforderungen

## Schritt 6 — PPA als Alternative zur EEG-Förderung

### Corporate PPA

- Direkter Vertrag Anlage — Endkunde (Industrie)
- Vermeidet Marktrisiko
- Skill `energierecht-projektfinanzierung` für Strukturierung

### On-Site PPA

- Anlage auf Kundengelände
- Direktversorgung ohne Netzdurchleitung
- Mess- und Eichrecht beachten

## Schritt 7 — Strafzahlung BNetzA / Pönale

### Pönalen bei Nicht-Realisierung Ausschreibungs-Zuschlag

- Zuschlag erteilt aber nicht rechtzeitig umgesetzt
- Pönale je nach Volumen
- Wiederaufnahme-Sperre

### Nachträglicher Ausschluss

- Bei wesentlichen Verstößen Förderfähigkeit
- BNetzA-Anordnung, klagebar VG

## Schritt 8 — Erdgas / Biogas / Biomethan

- Biomasse-Spezial-Regelungen § 39f-h EEG
- Nachhaltigkeits-Anforderungen RED II/III
- Biomethan-Einspeisung Gasnetz
- HRG-Verfahren Wasserstoff-Hochlauf (Erdgas-Vorgriff)

## Schritt 9 — EU-Bezug

### RED III (Renewable Energy Directive III, 2024)

- Beschleunigungs-Gebiete Pflicht
- Vereinfachung Genehmigung
- Nationale Umsetzung läuft

### EU-Strommarkt-Reform 2024

- Differenzverträge (Contracts for Difference)
- PPA-Erleichterungen
- Capacity-Markt-Mechanismen

## Schritt 10 — Mandanten-Strategie

### Bei Erzeugungs-Investor (Neuanlage)

1. Anlagentyp und Standort prüfen
2. Genehmigungs-Weg klar (BImSchG / Bau)
3. Förderpfad (Ausschreibung vs. PPA vs. Eigenverbrauch)
4. MaStR-Eintragung sicherstellen
5. Vergütungs-Direktvermarkter wählen
6. Begleit-Verträge (PPA, Wartungs-Vertrag, Versicherungs-Schutz)

### Bei Bestandsanlage

1. Vergütungs-Anspruch prüfen
2. Modernisierungs-Optionen
3. Repowering-Strategie
4. Vermarktungs-Optimierung

### Bei Streit mit Netzbetreiber

1. BNetzA-Beschwerde erwägen
2. Klage VG / Bundesgerichtshof bei EnWG-Linien
3. Skill `energierecht-verfahren`

## Aktuelle Rechtsprechung & Leitsätze (Stand 05/2026)

- **EuGH 28.03.2019, C-405/16 P (PreussenElektra-Nachfolge / EEG 2012)**: EEG-Umlage stellt keine staatliche Beihilfe i.S.v. Art. 107 AEUV dar (in Vorlaeufer-Konstellation); Aenderung gegenueber Kommissions-Auffassung. Quelle: curia.europa.eu (CELEX 62016CJ0405).
- **BGH 05.07.2022, EnVR 41/20**: Anlagenbegriff EEG; Abgrenzung zwischen mehreren Anlagen am selben Standort. Quelle: bundesgerichtshof.de — Pressemitteilung BGH 99/2022. Vor Zitieren der Detailfragen Aktenzeichen ueber bundesgerichtshof.de verifizieren.
- **BVerwG 17.12.2020, 4 C 5.19**: BImSchG-Genehmigung Windkraftanlage; Anforderungen an artenschutzrechtliche Pruefung (saP). Quelle: bverwg.de.
- **EuGH 27.04.2023, C-217/22 (Aktiengesellschaft Yarpa)**: Auslegung der EE-Richtlinie 2018/2001 (RED II) — Foerderfaehigkeit. Quelle: curia.europa.eu.
- **Gesetzeslage 05/2026:**
  - EEG 2023 (BGBl. I 2022 S. 1237, mehrfach geaendert)
  - Solarpaket I — BGBl. I 2024 S. 151 (Inkraftsetzung 16.05.2024)
  - WindBG 2022 (BGBl. I S. 1353) — 2-Prozent-Flaechenziel Laender
  - KWKG 2023 — Verlaengerung Foerderung bis 2030 (Wasserstoff-Pflicht ab 10 MW)
  - GEG 2024 (BGBl. I 2023 S. 280) — Heizungsgesetz, 65-Prozent-EE-Pflicht ab 2024 in Neubaugebieten
  - RED III — RL (EU) 2023/2413; Frist Umsetzung 21.05.2025; Beschleunigungsgebiete ab 21.02.2026 verpflichtend
  - BNetzA-Festlegungen Ausschreibungs-Hoechstwerte 2025/2026 ueber bundesnetzagentur.de aktuell pruefen

Konkrete Aktenzeichen vor Ausgabe ueber bundesgerichtshof.de / bverwg.de / curia.europa.eu mit Datum verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 19 EEG (Marktpraemie) — § 20 EEG (Direktvermarktung) — § 21 EEG (feste Einspeise-Verguetung) — § 23b EEG (Repowering) — § 33 EEG (MaStR-Eintragungspflicht) — § 4 BImSchG (Genehmigungspflicht) — § 35 BauGB (Privilegierung Aussenbereich) — § 44 BNatSchG (Zugriffsverbote Artenschutz)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Verzahnung

- `energierecht-netz-speicher-zugang` — Netzanschluss
- `energierecht-vertrieb-marktrollen` — Direktvermarktung
- `energierecht-projektfinanzierung` — PPA
- `energierecht-transaktionen-dd` — bei Anlagen-Verkauf
- `umweltrecht-immissionsschutz-bimschg` — BImSchG-Genehmigung
- `klimaklagen-verbandsklage-umwrg` — bei Verbands-Klagen Wind
- `normenkontrolle-bauleitplanung` — bei Bauleit-Streit

## Quellen

- EEG 2023 + Solarpaket I 2024 §§ 19, 20, 21, 23b, 33, 39f-o, 51a
- KWKG 2023 §§ 5, 10, 25
- BImSchG §§ 4, 10
- BauGB §§ 35, 249
- WindBG, SolarBG, GEG, EnEfG
- BNetzA-Festlegungen zu Ausschreibungs-Höchstwerten
- BAFA-Merkblätter
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BVerwG 17.12.2020, 4 C 5.19 — BImSchG-Windkraft saP (bverwg.de)
- EU-RED III (Richtlinie (EU) 2023/2413, ABl. L 2413 vom 31.10.2023; eur-lex.europa.eu/eli/dir/2023/2413/oj)
- EU-Strommarkt-Verordnung (EU) 2024/1747; sowie VO (EU) 2019/943 (Grundverordnung)
- EuGH 02.09.2021, C-718/18 — Unabhaengigkeit BNetzA als Regulierungsbehoerde
