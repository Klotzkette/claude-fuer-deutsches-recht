---
name: lease-datenschutz-telematik-esg-leasing-start
description: "Lease Datenschutz Telematik ESG Leasing Start: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lease Datenschutz Telematik ESG Leasing Start

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lease Datenschutz Telematik ESG Leasing Start** im Plugin Leasingrecht Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lease-033-datenschutz-telematik-im-fahrzeugleasing` | Datenschutz und Telematik im Fahrzeugleasing: DSGVO, Verarbeitungszwecke, Beschäftigtendatenschutz § 26 BDSG, Nutzungsprofile und Betriebsvereinbarung. |
| `lease-034-esg-leasing-taxonomie-und-green-lease` | ESG und Green Lease: EU-Taxonomie, SFDR, Nachhaltigkeitsklauseln, CO2-Reporting, Green-Finance-Strukturen und ESG-Anforderungen für Leasingportfolios. |
| `lease-037-start-up-equipment-leasing-covenants` | Start-up Equipment-Leasing: Kreditwürdigkeitsprüfung, Financial Covenants, persönliche Bürgschaft, Anlaufrisikoklauseln und typische Verhandlungspunkte. |

## Arbeitsweg

Im Plugin Leasingrecht Praxis gilt für **Lease Datenschutz Telematik ESG Leasing Start**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lease-033-datenschutz-telematik-im-fahrzeugleasing`

**Fokus:** Datenschutz und Telematik im Fahrzeugleasing: DSGVO, Verarbeitungszwecke, Beschäftigtendatenschutz § 26 BDSG, Nutzungsprofile und Betriebsvereinbarung.

# Datenschutz und Telematik im Fahrzeugleasing

## Zweck

Moderne Leasingfahrzeuge sind mit Telematik ausgestattet: GPS, Fahrstilüberwachung, Ferndiagnose. Die Verarbeitung dieser Daten berührt DSGVO, § 26 BDSG (Beschäftigtendatenschutz) und erfordert klare Regelungen im Leasingvertrag und in Betriebsvereinbarungen.

## DSGVO-Grundlagen

### Personenbezogene Daten
- GPS-Position + Uhrzeit + Fahrzeug-ID = personenbezogene Daten (identifizierbar über Fahrer)
- Fahrstildaten (Beschleunigung, Bremsung, Tempo): Personenbezug bei fester Fahrerzuordnung
- Telematik: Verarbeitung nach Art. 6 DSGVO erlaubnispflichtig

### Erlaubnistatbestände
- Art. 6 I b DSGVO: Vertragserfüllung (Flottenmanagement, Versicherungskalkulation)
- Art. 6 I f DSGVO: Berechtigte Interessen (Diebstahlschutz, Wartungsplanung)
- Art. 6 I a DSGVO: Einwilligung (für weitergehende Auswertung)

### Art. 6 I f: Interessenabwägung
Berechtigtes Interesse vs. Grundrechte des Betroffenen (Fahrer):
- Flottenmanagement: Berechtigtes Interesse bejaht
- Leistungsüberwachung einzelner Fahrer: Problematisch ohne BV oder Einwilligung
- Standortdaten in Echtzeit permanent: Sehr eingriffsintensiv; besonders zu rechtfertigen

## Beschäftigtendatenschutz (§ 26 BDSG)

### Anwendungsbereich
§ 26 BDSG gilt für die Datenverarbeitung im Beschäftigungsverhältnis.

- Firmenwagen mit Telematik: Fahrer = Beschäftigter → § 26 BDSG
- Zweck: Überwachung des Arbeitsverhältnisses erlaubt nur nach Verhältnismäßigkeitsprüfung

### Zulässige Verarbeitungszwecke (§ 26 I BDSG)
- Begründung, Durchführung und Beendigung des Beschäftigungsverhältnisses
- Straftaten im Beschäftigungsverhältnis aufdecken (§ 26 I 2 BDSG): Hohe Hürden (konkreter Anfangsverdacht)

### Betriebsvereinbarung (§ 26 IV BDSG)
- Kollektivrechtliche Regelung möglich: Betriebsrat + Arbeitgeber schließen BV über Telematik
- BV muss DSGVO-Anforderungen erfüllen (Art. 88 DSGVO)
- Inhalt: Zwecke, Datenkategorien, Auskunftsrechte, Löschfristen

## Telematik-Klauseln im Leasingvertrag

### LG-seitig
- LG darf Telematikdaten für: Fahrzeugdiagnose, Wartungsplanung, Diebstahlschutz
- Keine Übermittlung an Dritte ohne Rechtsgrundlage (Art. 28 DSGVO: AVV wenn Subunternehmer)

### LN-seitig (Flottenleasing)
- LN verarbeitet Daten der Fahrer für eigenes Flottenmanagement
- LN ist Verantwortlicher (Art. 4 Nr. 7 DSGVO) gegenüber Fahrern
- Informationspflicht gegenüber Fahrern (Art. 13 DSGVO)

## Auftragsverarbeitung (Art. 28 DSGVO)

Wenn LG oder Telematik-Dienstleister Daten im Auftrag des LN verarbeitet:
- Auftragsverarbeitungsvertrag (AVV) erforderlich
- Inhalt: Zweck, Kategorien, technisch-organisatorische Maßnahmen, Löschung

## Prüfprogramm

1. Welche Telematikdaten werden erhoben? GPS, Fahrstil, Diagnose?
2. Rechtsgrundlage für Verarbeitung: Art. 6 I b/f/a DSGVO?
3. Fahrer = Beschäftigter? § 26 BDSG und Betriebsvereinbarung?
4. AVV mit LG/Telematik-Dienstleister vorhanden?
5. Informationspflicht gegenüber Fahrern (Art. 13 DSGVO) erfüllt?
6. Löschkonzept: Telematikdaten nach welcher Frist gelöscht?

## Typische Fallen

- Telematik ohne Information der Fahrer → Verstoß Art. 13 DSGVO; Bußgeld
- BV fehlt → Betriebsrat kann Unterlassung der Telematikauswertung verlangen
- Leistungsüberwachung über Telematik ohne Rechtsgrundlage → Art. 83 IV DSGVO: bis 10 Mio. € Bußgeld
- AVV mit Telematik-Dienstleister fehlt → Bußgeldrisiko Art. 28 DSGVO

## Normen und Quellen

- DSGVO Art. 6, 13, 28: https://eur-lex.europa.eu
- § 26 BDSG (Beschäftigtendatenschutz): https://www.gesetze-im-internet.de/bdsg_2018/__26.html
- Art. 88 DSGVO (Beschäftigtendaten): https://eur-lex.europa.eu
- DSK (Datenschutzkonferenz) Kurzpapier Fahrzeugdaten: https://www.datenschutzkonferenz-online.de
- BAG 27.07.2017 – 2 AZR 681/16 (Überwachung, Beweisverwertungsverbot): https://openjur.de

## Output-Formate

- **Datenschutzfolgenabschätzung (DSFA)**: Telematik im Flottenleasing
- **Betriebsvereinbarungs-Muster**: Telematik-Nutzung Fahrzeuge
- **Informationsschreiben**: Art. 13 DSGVO für Fahrer
- **AVV-Klausel-Muster**: LN mit Telematik-Dienstleister

## 2. `lease-034-esg-leasing-taxonomie-und-green-lease`

**Fokus:** ESG und Green Lease: EU-Taxonomie, SFDR, Nachhaltigkeitsklauseln, CO2-Reporting, Green-Finance-Strukturen und ESG-Anforderungen für Leasingportfolios.

# ESG und Green Lease: Taxonomie und Nachhaltigkeit

## Zweck

ESG-Anforderungen (Environmental, Social, Governance) durchdringen zunehmend das Leasinggeschäft. EU-Taxonomie, SFDR und Green-Bond-Standards bestimmen, welche Leasingverträge als nachhaltig gelten. „Green Lease" ist ein Konzept, das ESG-Pflichten vertraglich verankert. Dieser Skill erklärt den Rahmen und gibt Vertragsbausteine.

## EU-Taxonomie-Verordnung (EU 2020/852)

### Grundkonzept
Die Taxonomie-VO definiert, welche wirtschaftlichen Aktivitäten als ökologisch nachhaltig gelten:
- Sechs Umweltziele (Klimaschutz, Klimaanpassung, Wasser, Kreislaufwirtschaft, Biodiversität, Schadstoffvermeidung)
- „Do No Significant Harm" (DNSH): Keine erhebliche Beeinträchtigung anderer Ziele
- Mindest-Sozialstandards (OECD, UN-Leitprinzipien)

### Leasing und Taxonomie
- Wenn LG Finanzprodukte anbietet oder investiert: Offenlegungspflicht (SFDR)
- Leasingobjekte können taxonomiefähig sein: PV-Anlagen, E-Fahrzeuge, effiziente Gebäude
- LG muss anteiligen Taxonomie-Anteil seines Portfolios offenlegen (Art. 8 Taxonomie-VO für Finanzunternehmen)

## SFDR (Sustainable Finance Disclosure Regulation, EU 2019/2088)

### Anwendungsbereich
- Finanzmarktteilnehmer und Finanzberater
- Leasinggesellschaften: Sofern Finanzdienstleistungsinstitut (KWG) → SFDR-Scope prüfen

### Offenlegungspflichten
- Art. 3 SFDR: Grundlegende ESG-Informationen auf Webseite
- Art. 7 SFDR: Adverse Sustainability Impacts (PAI) – Negative Nachhaltigkeitsauswirkungen
- Art. 8/9 SFDR: Produktklassifizierung (hellgrün/dunkelgrün)

## Green Lease: Vertragsklauseln

### Typische Green-Lease-Klauseln

**1. CO2-Monitoring-Klausel**
LN ist verpflichtet, Energieverbrauch und CO2-Ausstoß des Leasingobjekts jährlich zu berichten. LG kann Daten für ESG-Reporting verwenden.

**2. Instandhaltungsstandard**
LN hält das Objekt auf einem energetischen Standard X (z.B. Kfz: mind. Euro 6; Gebäude: Energieklasse A).

**3. Upgrade-Klausel**
LG bietet LN bei technischen Verbesserungen (effizientere Maschine, E-Fahrzeug) ein Upgrade-Angebot an.

**4. ESG-Kündigung**
Wenn LN dokumentierte ESG-Verstöße begeht (z.B. unrechtmäßige Entsorgung), kann LG außerordentlich kündigen.

**5. Green-Bond-Eligible**
Wenn LG Green Bonds emittiert: Leasingobjekte müssen Taxonomie-Kriterien erfüllen; LN kooperiert bei Nachweis-Erbringung.

## CO2-Flottenregulierung

### Kfz-Flottenleasing und CO2-Ziele
- EU-VO 2019/631: CO2-Flottengrenzwerte für Kfz-Hersteller
- PKW: 95 g CO2/km (2021), 0 g (Verbrenner-Neuzulassungsverbot ab 2035)
- Auswirkung auf Leasingportfolios: E-Fahrzeuge werden Pflicht; Restwert konventioneller Fahrzeuge sinkt

## Soziale und Governance-Anforderungen (S und G)

- Lieferkettensorgfaltspflichtengesetz (LkSG, ab 2023): Unternehmen mit > 1.000 MA
- Wenn Leasingobjekte aus Lieferketten mit Menschenrechtsverstößen: LkSG-Pflicht des LN
- Governance: Transparenz des LG in ESG-Berichterstattung (nfRB = nichtfinanzielle Berichterstattung, CSR-RUG)

## Prüfprogramm

1. Taxonomie-Konformität: Ist das Leasingobjekt taxonomiefähig? DNSH-Prüfung?
2. SFDR: Ist LG als Finanzmarktteilnehmer einzustufen?
3. Green-Lease-Klauseln: CO2-Monitoring, Upgrade, ESG-Kündigung vereinbart?
4. CO2-Flottenregulierung: E-Fahrzeuge im Portfolio? Restwert-Entwicklung?
5. LkSG: LN oder LG betroffen? Lieferkettencompliance?
6. ESG-Reporting: Welche Kennzahlen müssen ausgewiesen werden?

## Typische Fallen

- Taxonomie-Fähigkeit ohne DNSH-Prüfung deklariert → Greenwashing-Vorwurf
- SFDR-Offenlegungen fehlen → BaFin-Rüge
- Restwert konventioneller Fahrzeuge im Portfolio sinkt durch Verbrennerverbot schneller als kalkuliert
- Fehlende CO2-Daten vom LN → ESG-Reporting lückenhaft

## Normen und Quellen

- EU-Taxonomie-VO 2020/852: https://eur-lex.europa.eu
- SFDR 2019/2088: https://eur-lex.europa.eu
- EU-VO 2019/631 (CO2-Flottengrenzwerte): https://eur-lex.europa.eu
- LkSG (Lieferkettensorgfaltspflichtengesetz): https://www.gesetze-im-internet.de/lksg/
- CSR-RUG (nichtfinanzielle Berichterstattung): https://www.gesetze-im-internet.de/hgb/__289b.html

## Output-Formate

- **Green-Lease-Klauseln-Muster**: Fertige Textbausteine für Leasingvertrag
- **Taxonomie-Check**: Leasingobjekt taxonomiefähig ja/nein mit Begründung
- **CO2-Reporting-Vorlage**: Jährliches Monitoring-Formular für LN
- **SFDR-Disclosure-Muster**: Art. 3/7 SFDR für Leasinggesellschaft

## 3. `lease-037-start-up-equipment-leasing-covenants`

**Fokus:** Start-up Equipment-Leasing: Kreditwürdigkeitsprüfung, Financial Covenants, persönliche Bürgschaft, Anlaufrisikoklauseln und typische Verhandlungspunkte.

# Start-up Equipment-Leasing: Covenants und Risikoabsicherung

## Zweck

Start-ups haben oft keinen Track Record und schwache Bonität. Leasinggeber setzen deshalb auf zusätzliche Sicherheiten: Financial Covenants, persönliche Bürgschaft der Gründer, Anzahlungen und spezielle Risikoklauseln. Dieser Skill analysiert typische Anforderungen und Verhandlungspositionen.

## Bonitätsprüfung bei Start-ups

### Herausforderungen
- Keine Unternehmenshistorie → keine historischen Finanzberichte
- Negativer oder kein Cashflow → klassische Kreditwürdigkeitsprüfung scheitert
- Hohe Unsicherheit → LG kalkuliert hohes Ausfallrisiko ein

### Unterlagen, die LG verlangt
- Businessplan mit Finanzplanung (mind. 3 Jahre)
- Gesellschaftsvertrag und Handelsregisterauszug
- Gesellschafterstruktur und Gesellschafter-Bonität
- Ggf. Investoren-Letters (VC-Commitment)
- Kontoauszüge der letzten 3 Monate

## Sicherungsmechanismen des LG

### 1. Anzahlung / Sonderzahlung
- LG verlangt erhöhte Anzahlung (z.B. 3 Monatsraten voraus)
- Reduziert das Ausfallrisiko in der kritischen Anlaufphase

### 2. Bürgschaft der Gesellschafter/Gründer
- Persönliche Bürgschaft (§§ 765 ff. BGB): Gründer bürgen für Leasingverpflichtungen
- Selbstschuldnerische Bürgschaft (§ 773 BGB): LG kann sofort gegen Bürgen vorgehen
- AGB-Wirksamkeit: Bürgschaft in AGB? Gegenüber Verbrauchern/Gründern strenge Anforderungen

### 3. Financial Covenants
Typische Covenants:
- Mindesteigenkapital (z.B. Eigenkapital > 0 oder > definierter Betrag)
- Maximalverschuldung (Debt/Equity Ratio)
- Mindest-Cashflow (EBITDA > X)
- Jahresabschluss fristgerecht vorzulegen

Bei Verletzung: Kündigungsrecht des LG oder Sonderkündigungsrecht.

### 4. Abtretung von Forderungen / Rechten
- Start-up tritt Kundenverträge oder Fördergelder als Sicherheit ab
- § 398 BGB: Abtretung möglich, wenn Forderungen bestimmt oder bestimmbar

### 5. Verpfändung von Gesellschaftsanteilen
- GmbH-Anteile können verpfändet werden (§ 1274 BGB i.V.m. § 15 IV GmbHG: notarielle Form)
- LG erhält Stimmrechte bei Pfandfall (ggf. in Pfandvertrag)

## Anlaufrisikoklauseln

### Verlängerter Rücktritt
- Wenn Start-up erste Kundenzahlung nicht erhält: LG kann von Vertrag zurücktreten
- Selten; eher: Anpassungsklausel

### Change of Control
- Wenn Gründer das Unternehmen verlassen oder verkaufen: LG hat Sonderkündigungsrecht oder Nachbesicherungspflicht tritt ein

### Reporting-Pflichten
- Quartalsberichte (P&L, Cashflow)
- Sofortige Mitteilung von Covenant-Verletzungen
- Benachrichtigung bei wesentlichen Änderungen (Geschäftsführer, Investoren, Haftungsumfang)

## Verhandlungspositionen des Start-ups

### Gründer-Bürgschaft begrenzen
- Höchstbetrag vereinbaren
- Akzessorietät erhalten (Bürgschaft erlischt mit Hauptforderung)
- Nachhaftung ausschließen: Bürgschaft endet mit Vertragsbeendigung

### Covenants anpassen
- An realistische Unternehmensplanung (nicht an Erwachsenen-Unternehmen-Standards)
- Cure Period: Zeit zur Heilung einer Covenant-Verletzung

### Sicherheitenrückgabe
- Sicherheiten werden freigegeben wenn Track Record aufgebaut (z.B. nach 12 Monaten ohne Rückstand)

## Prüfprogramm

1. Bonitätslage: Businessplan, Finanzplanung, Gesellschafterstruktur?
2. Sicherheiten: Anzahlung, Bürgschaft, Covenants, Forderungsabtretung?
3. Bürgschaft: Selbstschuldnerisch, Höchstbetrag, Privatperson?
4. Covenants: Realistisch für Start-up? Cure Period?
5. Change of Control: Klausel vorhanden? Wann ausgelöst?
6. Verhandlung: Sicherheitenrückgabe vereinbart?

## Typische Fallen

- Bürgschaft ohne Höchstbetrag → unbegrenzte persönliche Haftung der Gründer
- Covenants zu streng → Verletzung bei erster Schwankung → sofortige Kündigung
- Keine Cure Period → sofortige Kündigung bei technischer Covenant-Verletzung
- Forderungsabtretung zu weit gefasst → Start-up kann eigene Forderungen nicht mehr einziehen

## Normen und Quellen

- §§ 765–778 BGB (Bürgschaft): https://dejure.org/gesetze/BGB/765.html
- § 773 BGB (selbstschuldnerische Bürgschaft): https://dejure.org/gesetze/BGB/773.html
- § 398 BGB (Abtretung): https://dejure.org/gesetze/BGB/398.html
- § 15 IV GmbHG (Verpfändung GmbH-Anteile): https://www.gesetze-im-internet.de/gmbhg/__15.html
- § 307 BGB (AGB-Inhaltskontrolle Bürgschaft): https://dejure.org/gesetze/BGB/307.html
- BGH IX ZR 48/15 (Bürgschaft AGB): https://www.bgh.de

## Output-Formate

- **Covenant-Template**: Financial Covenants für Start-up-Leasingvertrag
- **Bürgschafts-Vorlage**: Selbstschuldnerische Bürgschaft mit Höchstbetrag
- **Reporting-Pflichten-Anlage**: Quartalsbericht-Format
- **Verhandlungsmatrix**: LG-Anforderungen vs. Start-up-Gegenvorschläge
