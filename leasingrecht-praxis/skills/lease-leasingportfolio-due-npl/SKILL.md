---
name: lease-leasingportfolio-due-npl
description: "Lease Leasingportfolio DUE NPL: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lease Leasingportfolio DUE NPL

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lease Leasingportfolio DUE NPL** im Plugin Leasingrecht Praxis. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lease-029-leasingportfolio-due-diligence` | Leasingportfolio Due Diligence: Vertragsanalyse, Risikoklassifizierung, Konzentrations- und Restwertrisikoanalyse, Bewertung für Kauf/Verkauf. |
| `lease-030-npl-leasingforderungen-verkauf` | NPL-Leasingforderungen: Definition, Bewertung, Verkaufsprozess, Inkasso, regulatorische Anforderungen und Restrukturierung. |
| `lease-031-versicherung-objekt-untergang-und-ersatz` | Versicherung im Leasingrecht: Gefahrtragung, Pflichtversicherung, Totalschaden, Versicherungsleistung und Abrechnung nach Untergang. |

## Arbeitsweg

Im Plugin Leasingrecht Praxis gilt für **Lease Leasingportfolio DUE NPL**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lease-029-leasingportfolio-due-diligence`

**Fokus:** Leasingportfolio Due Diligence: Vertragsanalyse, Risikoklassifizierung, Konzentrations- und Restwertrisikoanalyse, Bewertung für Kauf/Verkauf.

# Leasingportfolio Due Diligence

## Zweck

Beim Kauf oder Verkauf eines Leasingportfolios ist eine strukturierte Due Diligence unabdingbar. Sie deckt rechtliche Risiken (AGB, Mängel, Insolvenz) ebenso auf wie finanzielle (Restwert, Konzentration) und regulatorische (KWG, DSGVO). Dieser Skill beschreibt den vollständigen DD-Prozess.

## Struktur der Due Diligence

### 1. Legal Due Diligence

#### Vertragsstruktur
- Gibt es Rahmenvertrag + Einzelverträge oder nur Einzelverträge?
- Standard-AGB verwendet? AGB-geprüft und AGB-konform?
- Vertragssprache, anwendbares Recht, Gerichtsstand

#### Eigentumsklarheit
- Für jedes Objekt: Wer ist Eigentümer?
- Sicherungsübereignung: An Refinanzierer; Rang?
- Eigentumsvorbehalte des Lieferanten noch aktiv?

#### Gewährleistungs- und Abtretungsklauseln
- Abtretungsklausel vorhanden und vollzogen?
- Offene Mängelrügen?

#### Kündigungen und Streitigkeiten
- Offene Rechtsstreitigkeiten?
- Verträge mit laufenden Mahnverfahren oder Insolvenz des LN?

### 2. Financial Due Diligence

#### Cashflow-Modell
- Aktuelle und künftige Leasingraten
- Restlaufzeiten, Fälligkeiten
- Variabel verzinsliche vs. festverzinsliche Raten
- Sonderzahlungen, Restwerte

#### Restwertrisiko
- Portfoliogewichteter Restwert
- Marktentwicklung der Objekte (Kfz, Maschinen, IT): Wertkurven
- Klumpenrisiko in einer Objektklasse

#### Ausfall- und Überfälligkeitsrate
- NPL-Quote (Non-Performing Loans/Leases)
- Rückstandstage: 0–30 / 31–60 / 61–90 / >90 Tage
- Risikoklassifizierung der LN

### 3. Regulatory Due Diligence

#### KWG
- Ist der LG als Finanzdienstleistungsinstitut nach KWG § 32 erlaubt?
- Finanzierungsleasing = erlaubnispflichtiges Finanzdienstleistungsgeschäft (KWG § 1 II Nr. 10)
- BaFin-Erlaubnis vorhanden? Kapitalanforderungen (CRR)?

#### DSGVO
- Datenschutzkonformität der Leasingakten
- AVV mit Servicern, IT-Dienstleistern vorhanden?
- Datentransfers ins Ausland?

## Bewertungsparameter

### Portfoliokaufpreis
- Par Value (Nominalwert der offenen Raten) als Ausgangspunkt
- Abzüge für: Überfälligkeiten, Restwertrisiken, Schlechtverträge, Konzentration
- Aufschläge für: Kurze Restlaufzeit (gut besicherte Kurzfrist-Forderungen), Objektqualität

### Rendite (Yield)
- Interner Zinsfuß (IRR) des Portfolios
- Spread über Refinanzierungskosten = Ertragskennzahl

## Prüfprogramm

1. Vertragsliste (Tape): Alle Verträge mit Metadaten (LN, Objekt, Rate, Laufzeit, Restwert)
2. Sample-Review: 10–20 % Stichprobe für tiefere Analyse
3. Eigentumsnachweis: Stichprobenweise Kaufverträge prüfen
4. Ausfall-Analyse: NPL-Quote, Rückstandsalter, Verwertungserlöse historisch
5. Regulatorisches: KWG-Erlaubnis, BaFin-Korrespondenz
6. Vertragliche Risiken: AGB-Mängel, fehlende Abtretungsklauseln

## Typische Fallen

- Tape enthält falsche Daten: Restwert-Annahmen zu optimistisch
- Eigentumsnachweis fehlt für Objekte → LG ist gar nicht Eigentümer
- NPL-Quoten nach "optimistischer" Definition → tatsächliche Ausfallrate höher
- KWG-Erlaubnis fehlt oder Bedingungen verletzt → Kaufer übernimmt regulatorisches Risiko

## Normen und Quellen

- KWG § 1 II Nr. 10 (Finanzierungsleasing): https://www.gesetze-im-internet.de/kredwg/__1.html
- KWG § 32 (Erlaubnispflicht): https://www.gesetze-im-internet.de/kredwg/__32.html
- Art. 28 DSGVO: https://eur-lex.europa.eu
- §§ 398 ff. BGB (Abtretung): https://dejure.org/gesetze/BGB/398.html
- CRR (EU 575/2013): https://eur-lex.europa.eu
- BGH, Urteil vom 13.11.2013 - VIII ZR 257/12 (Abtretungskonstruktion): https://www.bgh.de

## Output-Formate

- **DD-Checkliste**: Legal, Financial, Regulatory – dreispaltig
- **Tape-Analyse-Vorlage**: Excel-Format für Portfolio-Überblick
- **Sample-Review-Protokoll**: Einzelvertrag – 20 Prüfpunkte
- **Bewertungs-Memo**: Par Value, Abzüge, Kaufpreisrange

## 2. `lease-030-npl-leasingforderungen-verkauf`

**Fokus:** NPL-Leasingforderungen: Definition, Bewertung, Verkaufsprozess, Inkasso, regulatorische Anforderungen und Restrukturierung.

# NPL-Leasingforderungen: Verkauf und Restrukturierung

## Zweck

Non-Performing Leases (NPL) sind ausgefallene oder überfällige Leasingverträge. LG müssen diese aktiv managen: Inkasso, Restrukturierung oder Portfolio-Verkauf sind die Optionen. Dieser Skill beschreibt Definitionen, Bewertung und Verkaufsprozess.

## NPL-Definition im Leasing

### Klassifikation
- **Performing**: Aktuell, ≤ 30 Tage Rückstand
- **Watch List**: 31–60 Tage
- **Sub-Standard**: 61–90 Tage
- **Doubtful**: 91–180 Tage
- **Loss (NPL)**: > 180 Tage oder wertberichtigtes Engagement

EBA-Definition (Leitlinien EBA/GL/2018/06): Non-Performing Exposure bei > 90 Tage Rückstand oder Hinweisen auf Uneinbringlichkeit.

### Leasing-spezifische NPL-Merkmale
- Objekt noch beim LN: Besicherungsposition erhalten
- Objekt bereits herausgegeben/verwertet: Residualforderung
- Insolvenz LN: Insolvenzforderung (oft 5–30 % Quote)

## Bewertung von NPL-Leasingforderungen

### Factored Value
- Barwert der erwarteten Einzahlungen (inkl. Verwertungserlös des Objekts)
- Diskontiert mit Risikozuschlag-Zinssatz
- Rückforderungsrate (Recovery Rate): historische Daten wichtig

### Objektwert als Sicherheitspolster
- Physisches Objekt vorhanden: LG kann Objekt zurückholen und verwerten
- Marktwert des Objekts vs. Restwert im Vertrag → Sicherheitspolster
- Objekt nicht auffindbar oder zerstört → Nur unbesicherte Forderung

## NPL-Verkaufsprozess

### 1. Portfoliobereinigung
- Zusammenstellung homogener NPL-Tranchen (Kfz, Maschinen, Verbraucher, B2B)
- Data Tape: Überfälligkeitstage, Objektwert, LN-Typ, Gerichtsstand

### 2. Investoransprache
- Distressed Debt Fonds, Spezialinvestoren (z.B. Intrum, Hoist, Waterfall AM)
- Non-Disclosure Agreement (NDA) → Datenraum-Zugang

### 3. Bewertungsphase
- Investoren erstellen Bid (Kaufpreisangebot)
- LG kann Reserve Price (Mindestpreis) setzen

### 4. Kaufvertrag (Forderungskaufvertrag)
- Abtretung der Forderungen (§ 398 BGB)
- Gewährleistungsausschlüsse für Bonität des LN (keine Haftung für Einbringlichkeit)
- Representations & Warranties: Eigentumsrecht, keine Vorababtretung, korrekte Salden

### 5. Schuldnerbenachrichtigung
- Nach Abtretung: Benachrichtigung des LN über neuen Gläubiger (§ 409 BGB)
- Inkassounternehmen tritt als neuer Gläubiger auf

## Regulatorik

### KWG und Inkasso
- Inkassounternehmen: Erlaubnispflicht nach RDG (Rechtsdienstleistungsgesetz)
- § 10 I Nr. 1 RDG: Inkasso als Rechtsdienstleistung erlaubt, wenn Unternehmen registriert
- ECSP / EBA-Leitlinien: Regulatorische Anforderungen für NPL-Käufer

### NPL-Richtlinie (EU 2021/2167)
EU-Richtlinie 2021/2167 über Kreditdienstleister und Kreditkäufer:
- Registrierungspflicht für Kreditdienstleister in EU
- Transparenz- und Verbraucherschutzpflichten
- Deutsches Umsetzungsgesetz: Kreditzweitmarktgesetz (KrZwMG, 2023)

## Prüfprogramm

1. NPL-Definition: Nach welcher Klassifizierung (intern, EBA)?
2. Objektlage: Objekt beim LN vorhanden, bereits verwertet oder unbekannt?
3. Forderungsbetrag: Kapital + Zinsen + Kosten korrekt berechnet?
4. Verkaufsprozess: Homogene Tranchen, Data Tape vollständig?
5. Kaufvertrag: Representations & Warranties, Gewährleistungsausschlüsse?
6. Regulatorik: Käufer nach KrZwMG registriert?

## Typische Fallen

- Objekt nicht lokalisierbar → Sicherheitspolster fehlt → niedrigerer Kaufpreis
- Doppelt abgetretene Forderung (Vorrang-Problem) → Käufer erwirbt keine Forderung
- LN bereits insolvenzantrag gestellt → InsO-Verfahren läuft; Käufer übernimmt InsO-Forderung
- KrZwMG: Käufer ohne Registrierung → Bußgeld, Kaufvertrag ggf. unwirksam

## Normen und Quellen

- EBA/GL/2018/06 (NPL-Leitlinien): https://eur-lex.europa.eu
- EU-Richtlinie 2021/2167 (NPL): https://eur-lex.europa.eu
- KrZwMG (Kreditzweitmarktgesetz): https://www.gesetze-im-internet.de
- §§ 398–413 BGB: https://dejure.org/gesetze/BGB/398.html
- RDG § 10 (Inkasso): https://www.gesetze-im-internet.de/rdg/__10.html
- § 409 BGB (Abtretungsanzeige): https://dejure.org/gesetze/BGB/409.html

## Output-Formate

- **NPL-Klassifikationstabelle**: Rückstandstage – Kategorie – Risikoeinschätzung
- **Data-Tape-Vorlage**: Excel-Format für NPL-Portfolio-Verkauf
- **Forderungskaufvertrag-Checkliste**: R&W, Gewährleistung, Abtretung
- **KrZwMG-Compliance-Memo**: Registrierungsvoraussetzungen

## 3. `lease-031-versicherung-objekt-untergang-und-ersatz`

**Fokus:** Versicherung im Leasingrecht: Gefahrtragung, Pflichtversicherung, Totalschaden, Versicherungsleistung und Abrechnung nach Untergang.

# Versicherung im Leasingrecht: Untergang und Ersatz

## Zweck

Der Untergang, Diebstahl oder Totalschaden am Leasingobjekt ist ein kritisches Ereignis: Wer trägt den Schaden? Wer bekommt die Versicherungsleistung? Wie rechnet sich der Leasingvertrag ab? Dieser Skill analysiert Versicherungspflichten, Gefahrtragung und Abrechnungslogik.

## Gefahrtragung im Finanzierungsleasing

### Grundsatz: LN trägt die Gefahr
BGH VIII ZR 71/93: Im Finanzierungsleasing trägt der Leasingnehmer das Risiko des zufälligen Untergangs und der zufälligen Verschlechterung. Dies gilt als wirksame AGB-Klausel für das Finanzierungsleasing, da LN wirtschaftlicher Eigentümer ist.

Folge: Bei Untergang durch Zufall (Brand, Diebstahl, Naturkatastrophe) schuldet LN weiterhin die Leasingraten – es sei denn, die Versicherung deckt den Schaden.

### Operating-Lease
Beim Operating-Lease verbleibt das Verwertungsrisiko beim LG. Gefahrtragungsklausel zulasten des LN ist hier problematischer (§ 307 BGB).

## Versicherungspflichten

### Vertragliche Verpflichtung des LN
Leasingverträge enthalten typischerweise:
- Pflicht zur Kaskoversicherung (Vollkasko) auf Kosten des LN
- LN muss Versicherungspolice dem LG vorlegen
- LG als Begünstigter (Versicherungsnehmer bleibt LN, aber LG bezieht Leistung)

### Wer ist Versicherungsnehmer?
- Variante 1: LN ist Versicherungsnehmer; LG als Begünstigter
- Variante 2: LG ist Versicherungsnehmer; Prämien auf LN umgelegt
- Variante 3: LG schließt Gruppenversicherung ab; LN zahlt Prämienanteil

## Totalschaden: Abrechnungslogik

### Ablauf bei Totalschaden
1. Ereignis: Totalschaden oder Diebstahl
2. Schadenmeldung: LN meldet an Versicherung und LG
3. Gutachten: Versicherung bestimmt Wiederbeschaffungswert oder Restwert
4. Auszahlung: Versicherungsleistung an LG (als Begünstigter)
5. Vertragsende: Leasingvertrag endet; verbleibende Forderung des LG

### Abrechnung
```
Versicherungsleistung (Schaden-Entschädigung)
- Ausstehende Leasingraten (abgezinst, bis Vertragsende)
- Evtl. Vertragsabschlusskosten
= Differenz (positiv: LN erhält zurück; negativ: LN schuldet Differenz)
```

**Gap-Versicherung** (GAP = Guaranteed Asset Protection):
- Deckt die Differenz zwischen Versicherungsleistung und ausstehenden Raten
- Besonders wichtig bei Kfz: Fahrzeugwert sinkt schneller als Ratenhöhe
- BGH: GAP-Versicherungsklauseln zulässig, wenn transparent

## AGB-Kontrolle: Versicherungsklauseln

### Prämienübernahme durch LN
- Zulässig als Nebenleistungspflicht
- Transparenzgebot: Prämie muss im Leasingvertrag oder separat ausgewiesen sein

### Untergang ohne Versicherungsleistung (z.B. Krieg, Terrorismus, ausgeschlossene Schäden)
- Wer trägt den Schaden?
- AGB-Klausel: LN trägt Restschuld auch bei nicht gedecktem Untergang → umstritten nach § 307 BGB
- Verbraucher: Solche Klauseln können unangemessen sein

## Prüfprogramm

1. Welche Versicherung ist vertraglich vereinbart? (Vollkasko, Teilkasko, Haftpflicht)
2. Wer ist Versicherungsnehmer, wer Begünstigter?
3. GAP-Versicherung vorhanden? Deckt sie die Restschuld?
4. Schadenmeldung rechtzeitig (Obliegenheitsverletzung prüfen)?
5. Versicherungsleistung: An LG ausgezahlt? Abrechnung mit LN?
6. AGB-Klausel zu nicht gedecktem Schaden: AGB-konform?

## Typische Fallen

- Keine Vollkaskoversicherung trotz Vertragspflicht → LN haftet für Schaden ohne Deckung
- GAP-Versicherung fehlt → LN zahlt aus eigener Tasche die Differenz
- Obliegenheitsverletzung (z.B. Schadensmeldung zu spät) → Versicherung kürzt Leistung
- LG nicht als Begünstigter eingetragen → Versicherungsleistung geht an LN, nicht an LG

## Normen und Quellen

- BGH VIII ZR 71/93 (Gefahrtragung Finanzierungsleasing): https://www.bgh.de
- § 307 BGB (AGB-Inhaltskontrolle): https://dejure.org/gesetze/BGB/307.html
- VVG §§ 43 ff. (Versicherung für fremde Rechnung): https://www.gesetze-im-internet.de/vvg_2008/__43.html
- VVG §§ 81 ff. (Obliegenheiten): https://www.gesetze-im-internet.de/vvg_2008/__81.html
- openjur.de GAP-Versicherung Leasing: https://openjur.de

## Output-Formate

- **Versicherungs-Checkliste**: Pflichten des LN, Begünstigter, GAP
- **Totalschaden-Abrechnungsvorlage**: Versicherungsleistung vs. ausstehende Raten
- **Obliegenheits-Protokoll**: Schadenmeldung, Aufklärungspflicht, Fristen
- **GAP-Analyse**: Wertentwicklung vs. Ratenprofil – Deckungslücke
