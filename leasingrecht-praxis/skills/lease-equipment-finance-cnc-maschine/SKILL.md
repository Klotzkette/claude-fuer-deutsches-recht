---
name: lease-equipment-finance-cnc-maschine
description: "Lease Equipment Finance CNC Maschine: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lease Equipment Finance CNC Maschine

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lease Equipment Finance CNC Maschine** im Plugin Leasingrecht Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lease-052-equipment-finance-term-sheet` | Equipment Finance Term Sheet: Strukturierung, Kernparameter, Verhandlungspunkte, Due-Diligence-Vorbedingungen und Abschluss. |
| `lease-053-cnc-maschine-abnahme-maengel` | CNC-Maschine Leasing: Technische Abnahme, Mängelrecht, Präzisionsanforderungen, Wartungsklauseln und Rückgabe. |
| `lease-054-fahrzeugflotte-telematik` | Fahrzeugflotte und Telematik: Datenstrategie, Telematik-Vertragsklauseln, Datenschutz-Compliance, Betriebsvereinbarung und Flottenauswertung. |

## Arbeitsweg

Im Plugin Leasingrecht Praxis gilt für **Lease Equipment Finance CNC Maschine**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lease-052-equipment-finance-term-sheet`

**Fokus:** Equipment Finance Term Sheet: Strukturierung, Kernparameter, Verhandlungspunkte, Due-Diligence-Vorbedingungen und Abschluss.

# Equipment Finance Term Sheet

## Zweck

Ein Term Sheet für Equipment Finance (Leasing oder Darlehen) definiert die Kernparameter der Transaktion vor dem formalen Vertragsschluss. Dieser Skill beschreibt die Struktur, typische Klauseln und Verhandlungspunkte.

## Struktur des Term Sheets

### 1. Parteien
- Leasinggeber / Finanzier: Name, Rechtsform, Sitz
- Leasingnehmer / Kreditnehmer: Name, Rechtsform, Sitz, USt-IdNr.
- Bürgen / Guarantors (falls vereinbart)

### 2. Transaktion
- Finanzierungsart: Finanzierungsleasing / Operating-Lease / Darlehen
- Leasingobjekt: Beschreibung, Hersteller, Modell, Anschaffungskosten
- Kaufvertrag: Lieferant, Datum, Preis inkl./exkl. USt

### 3. Finanzierungsparameter
| Parameter | Wert |
|---|---|
| Anschaffungskosten | EUR X |
| Eigenleistung/Anzahlung | X % |
| Finanzierungsbetrag | EUR Y |
| Laufzeit | X Monate |
| Rate (monatlich) | EUR Z |
| Zinssatz (p.a.) | X % fest/variabel |
| Restwert | EUR W |
| Effektiver Jahreszins | X % (§ 6 PAngV) |

### 4. Sicherheiten
- Eigentumsrecht (Standard beim Leasing)
- Bürgschaft: Gesellschafter, Konzernmutter?
- Abtretung: Forderungen, Rechte?
- Financial Covenants?

### 5. Aufschiebende Bedingungen (Conditions Precedent)
Vor Auszahlung/Aktivierung:
- Unterzeichneter Leasingvertrag
- Nachweis Eigenkapital / Anzahlung
- Bonitätsnachweise (Jahresabschlüsse, BWA)
- Versicherungsnachweis
- Ggf. Baugenehmigung (bei Immobilien)

### 6. Nebenabreden
- Informationspflichten: Jahresabschluss innerhalb X Monate nach Geschäftsjahresende
- Change of Control: Sonderkündigungsrecht LG?
- Pari-passu: Keine neuen vorrangigen Finanzierungen ohne LG-Zustimmung?
- Cross Default: Ausfall bei anderen Gläubigern = Ausfall hier?

### 7. Laufzeit des Term Sheets
- Bindungsdauer: Z.B. 30 Tage
- Exklusivität: LN darf in dieser Zeit keine anderen Finanzierungsangebote annehmen (optional)

## Verhandlungspunkte

### Für LN
- Effektivzins so niedrig wie möglich
- Keine übermäßigen Covenants
- Flexible Verlängerungs- oder Rückkaufoptionen
- Sicherheitenrückgabe nach Track Record

### Für LG
- Ausreichende Sicherheiten
- Informationsrechte für Monitoring
- Change-of-Control-Schutz
- Cross Default für Koordination bei Ausfall

## Due-Diligence vor Abschluss

### LN-Unterlagen
- Jahresabschlüsse letzte 3 Jahre (geprüft)
- Aktuelle BWA (nicht älter als 3 Monate)
- Gesellschaftsvertrag, Handelsregisterauszug
- Businessplan (bei Start-ups)
- Gesellschafterliste und Bonität der Gesellschafter

### Objekt-DD
- Kaufvertrag mit Lieferant
- Technische Spezifikation
- Wertgutachten (wenn Restwert wesentlich)

## Prüfprogramm

1. Alle Kernparameter vollständig und konsistent?
2. Sicherheiten angemessen für Risiko?
3. Conditions Precedent realistisch erfüllbar?
4. Term-Sheet-Laufzeit ausreichend für Due Diligence?
5. Binding oder Non-Binding? (Term Sheet = meist non-binding, außer Exklusivität)
6. Steuerliche Behandlung: Leasing vs. Darlehen klar entschieden?

## Typische Fallen

- Term Sheet als binding interpretiert → LN/LG an Konditionen gebunden ohne endgültige Due Diligence
- Conditions Precedent zu eng formuliert → Transaktion scheitert an Formalitäten
- Fehlende Cross-Default-Klausel → LG erfährt Ausfall bei anderen Gläubigern nicht rechtzeitig
- Effektivzins nicht korrekt angegeben → § 494 BGB-Risiken

## Normen und Quellen

- §§ 506–509 BGB (Verbraucherleasing): https://dejure.org/gesetze/BGB/506.html
- § 6 PAngV (effektiver Jahreszins): https://www.gesetze-im-internet.de/pangv/__6.html
- §§ 765–778 BGB (Bürgschaft): https://dejure.org/gesetze/BGB/765.html
- HGB §§ 238 ff. (Jahresabschluss): https://www.gesetze-im-internet.de/hgb/__238.html
- IFRS 16 (Bilanzierung): https://eur-lex.europa.eu

## Output-Formate

- **Term-Sheet-Vorlage**: Vollständige Vorlage mit allen Parametern
- **Verhandlungsprotokoll**: Änderungen im Term Sheet dokumentiert
- **Conditions-Precedent-Checkliste**: Alle Bedingungen vor Aktivierung
- **Due-Diligence-Liste**: LN-Unterlagen für LG

## 2. `lease-053-cnc-maschine-abnahme-maengel`

**Fokus:** CNC-Maschine Leasing: Technische Abnahme, Mängelrecht, Präzisionsanforderungen, Wartungsklauseln und Rückgabe.

# CNC-Maschinen-Leasing: Abnahme, Mängel und Wartung

## Zweck

CNC-Maschinen (Computer Numerical Control) sind hochpräzise Fertigungsanlagen mit spezifischen Anforderungen an Abnahme, Präzision, Wartung und Rückgabe. Dieser Skill analysiert die besonderen rechtlichen Aspekte dieses Segments.

## Technische Besonderheiten

### CNC-Maschinen als Leasingobjekte
- Hoher Anschaffungswert (50.000 € bis mehrere Millionen €)
- Langer Lebenszyklus (10–20+ Jahre)
- Präzisionsanforderungen: Toleranzen im Mikrometerbereich
- Steuerungssoftware: Siemens SINUMERIK, Fanuc, Heidenhain – lizenzpflichtig
- Spezialwerkzeuge und Zubehör: Teuer; teils mitgeleast

### Wirtschaftliches Eigentum (BMF-Erlass)
- Leasinglaufzeit: Typisch 5–7 Jahre; betriebsgewöhnliche Nutzungsdauer oft 10 Jahre
- Prüfung: Laufzeit zwischen 40–90 % der ND → LG bleibt wirtschaftlicher Eigentümer

## Abnahme: Kritische Punkte

### Abnahmetest (FAT – Factory Acceptance Test)
- Vor Lieferung: Abnahme beim Lieferant (FAT)
- Nach Lieferung: Abnahme beim LN (SAT – Site Acceptance Test)
- Prüfumfang: Geometrische Genauigkeit, Positioniergenauigkeit, Wiederholgenauigkeit, Oberflächenqualität
- Normen: DIN ISO 230 (Maschinengenauigkeit), VDI 3441 (Statistik)

### Abnahmeprotokoll bei CNC
- Messprotokolle: Geometriemessungen, Kreistest, Probebearbeitung mit Messergebnissen
- Werkzeug- und Aufnahme-Lieferumfang dokumentieren
- Steuerungsversion und Softwarelizenz festhalten
- Typenschild-Foto und Seriennummer

### Abnahmeverweigerung
- Bei Unterschreitung vereinbarter Genauigkeitstoleranzen: Berechtigt
- Maschine muss nachgerüstet werden; Fristsetzung an Lieferant

## Mängelrecht

### Typische Mängel bei CNC-Maschinen
- Geometriefehler (Geradlinigkeit, Rechtwinkligkeit)
- Positionierungsfehler > Toleranz
- Thermische Drift bei Erwärmung
- Steuerungssoftware-Bugs
- Hydraulik- oder Pneumatikleckagen

### Abtretungskonstruktion
- LG tritt Mängelansprüche gegen Lieferant an LN ab (§ 398 BGB)
- LN klagt direkt gegen Maschinenbauer/Importeur

### Verjährung § 438 BGB
- Sachmängelansprüche: 2 Jahre ab Abnahme (§ 438 I Nr. 3 BGB)
- Bei Arglist: 3 Jahre ab Kenntnis (§ 195 BGB)

## Wartung und Instandhaltung

### Wartungsvertrag
- Hersteller-Wartungsvertrag: Empfohlen für CNC; regelmäßige Kalibrierung
- Im Leasingvertrag: LN verpflichtet zur Wartung nach Herstellervorgabe
- Wartungsprotokoll: Nachzuweisen bei Rückgabe (Minderwert-Schutz)

### Ersatzteile
- Originale Ersatzteile vs. Nicht-OEM: Im Leasingvertrag regeln
- Gewährleistung des Lieferanten erlischt bei nicht-OEM-Ersatzteilen?

## Rückgabe der CNC-Maschine

### Zustandsprüfung
- Wiederholungsmessung Geometrie: Noch innerhalb Toleranz?
- Verschleiß an Führungen, Spindeln, Kugelgewindetrieben
- Steuerungssoftware: Werkseinstellung oder LN-spezifische Konfiguration?

### Rückbau und Transport
- CNC: Spezialisten für Demontage und Transport erforderlich
- Transportschäden: Wer trägt? Im Leasingvertrag regeln

## Prüfprogramm

1. FAT und SAT durchgeführt? Messprotokolle archiviert?
2. Abtretungsklausel: Kann LN direkt gegen Lieferant klagen?
3. Wartungsprotokoll vollständig? Wartungsvertrag vorhanden?
4. Mängel innerhalb 2-Jahresfrist gerügt?
5. Rückgabe: Geometrietest, Verschleiß, Software-Reset?
6. Rückbaukosten: Im Vertrag klar geregelt?

## Normen und Quellen

- § 438 BGB (Verjährung Sachmängel): https://dejure.org/gesetze/BGB/438.html
- § 398 BGB (Abtretung): https://dejure.org/gesetze/BGB/398.html
- DIN ISO 230 (Maschinengenauigkeit): https://www.din.de
- VDI 3441 (Statistische Genauigkeitsprüfung): https://www.vdi.de
- EU-Maschinenverordnung VO 2023/1230: https://eur-lex.europa.eu
- BGH, Urteil vom 13.11.2013 - VIII ZR 257/12: https://www.bgh.de

## Output-Formate

- **SAT-Abnahmeprotokoll-Vorlage**: CNC – Geometrie, Software, Zubehör
- **Mängelrüge-Vorlage**: LN an CNC-Hersteller (abgetretenes Recht)
- **Wartungsnachweis-Formular**: Kalibrier- und Serviceprotokoll
- **Rückgabe-Checkliste CNC**: Geometrie, Verschleiß, Transport

## 3. `lease-054-fahrzeugflotte-telematik`

**Fokus:** Fahrzeugflotte und Telematik: Datenstrategie, Telematik-Vertragsklauseln, Datenschutz-Compliance, Betriebsvereinbarung und Flottenauswertung.

# Fahrzeugflotte und Telematik: Datenstrategie und Compliance

## Zweck

Flottentelematik liefert wertvolle Daten für Kostenoptimierung, Sicherheit und Wartungsplanung – aber sie birgt erhebliche Datenschutzrisiken. Dieser Skill bearbeitet technische Telematikstrategie mit rechtlicher Compliance.

## Telematikdaten: Kategorien und Verwendung

### Datentypen
| Datentyp | Zweck | Personenbezug |
|---|---|---|
| GPS-Position + Timestamp | Tourenplanung, Diebstahl | Hoch (Fahrerprofil) |
| Geschwindigkeit + Beschleunigung | Fahrstilanalyse, Versicherung | Mittel–Hoch |
| Kraftstoffverbrauch | Kostenoptimierung | Gering |
| Motor-Diagnosedaten (OBD) | Wartungsplanung | Gering |
| Fahrerzuordnung (Schlüssel-ID) | Regresspflichten | Hoch |

### Verwendungszwecke (Rechtsgrundlagen)
- Flottenmanagement (Route, Auslastung): Art. 6 I b/f DSGVO
- Wartungsplanung (Motor-Diagnose): Art. 6 I f DSGVO
- Fahrtstilüberwachung einzelner Fahrer: § 26 BDSG + Betriebsvereinbarung
- Regresszwecke (wer hatte Fahrzeug bei Unfall): § 26 BDSG, Verhältnismäßigkeit

## Betriebsvereinbarung Telematik

### Notwendigkeit
- Wenn Telematik Arbeitnehmer überwacht: Betriebsrat mitbestimmungspflichtig (§ 87 I Nr. 6 BetrVG)
- Ohne Betriebsrat-Zustimmung: Daten nicht verwertbar
- Betriebsvereinbarung (BV) + Zustimmung Betriebsrat: Erlaubnis für Datenverarbeitung

### Inhalt der Betriebsvereinbarung
1. Zweck der Telematik (klar definiert: nur Flottenoptimierung, nicht Leistungsüberwachung)
2. Datenkategorien: GPS ja, Fahrstil nein / nur aggregiert
3. Aufbewahrungsfristen: GPS-Daten max. 30 Tage; Ausnahme bei Unfallbezug bis Abschluss
4. Zugriffsberechtigte: Flottenmanager, nicht Vorgesetzte
5. Rechte der Arbeitnehmer: Auskunft, Berichtigung, Widerspruch
6. Keine Verhaltenskontrolle: Daten nicht für Abmahnungen verwenden

## Telematik-Klauseln im Leasingvertrag

### Pflichten des LG
- Datenverarbeitung durch LG: Nur für vertragsgemäße Zwecke (Fahrzeugdiagnose, Standort bei Diebstahl)
- AVV (Art. 28 DSGVO): Wenn Telematik-Dienstleister im Auftrag des LN
- Weitergabe an Dritte: Nur mit Erlaubnis des LN

### Pflichten des LN
- Fahrer informieren (Art. 13 DSGVO)
- Betriebsvereinbarung umsetzen
- Keine unautorisierten Tracking-Modifikationen

## Datenstrategie und Flottenoptimierung

### Auswertungsszenarien
1. **Kraftstoffoptimierung**: Schlechte Fahrgewohnheiten identifizieren → Schulungspotenzial
2. **Geofencing**: Alarm wenn Fahrzeug außerhalb erlaubter Zone
3. **Predictive Maintenance**: OBD-Daten analysieren → Wartung vor Ausfall
4. **Diebstahlrückverfolgung**: GPS-Echtzeitposition für Polizei

### Kennzahlen (KPIs) für Flottenmanager
- Durchschnittlicher Kraftstoffverbrauch/100 km
- Anzahl Harsh Events (Vollbremsungen, Beschleunigung)
- Stillstandzeiten
- Gesamtkm vs. geplante km

## Prüfprogramm

1. Betriebsvereinbarung Telematik: Abgeschlossen und DSGVO-konform?
2. Art. 13 DSGVO: Fahrer über Telematik informiert?
3. AVV mit Telematik-Dienstleister vorhanden?
4. Daten-Löschkonzept: GPS max. 30 Tage?
5. LG-Telematik-Klausel: Nur vertragsgemäße Verwendung?
6. Regresszwecke: Fahrerzuordnung DSGVO-konform?

## Typische Fallen

- Keine Betriebsvereinbarung → Telematikdaten nicht verwertbar; Betriebsrat kann Unterlassung verlangen
- Fahrer nicht informiert (Art. 13 DSGVO) → Bußgeld bis 20 Mio. € oder 4 % Jahresumsatz
- Daten länger als nötig gespeichert → DSGVO-Verstoß
- Fahrtstil-Auswertung für Abmahnungen verwendet → § 87 I Nr. 6 BetrVG verletzt

## Normen und Quellen

- DSGVO Art. 6, 13, 28: https://eur-lex.europa.eu
- § 26 BDSG: https://www.gesetze-im-internet.de/bdsg_2018/__26.html
- § 87 I Nr. 6 BetrVG (Mitbestimmung Überwachung): https://www.gesetze-im-internet.de/betrvg/__87.html
- Art. 83 DSGVO (Bußgelder): https://eur-lex.europa.eu
- BAG 29.06.2004 – 1 ABR 21/03 (Mitbestimmung IT-Kontrolle): https://openjur.de

## Output-Formate

- **Betriebsvereinbarung Telematik**: Mustertext mit DSGVO-Anforderungen
- **Datenschutzinformation Fahrer**: Art. 13 DSGVO für Flottenleasing
- **AVV-Telematik**: Muster für LN mit Telematik-Dienstleister
- **Telematik-KPI-Dashboard**: Excel-Vorlage mit Flottenauswertung
