---
name: kv-familienversicherung-kv-statusfeststellung
description: "KV Familienversicherung KV Statusfeststellung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# KV Familienversicherung KV Statusfeststellung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **KV Familienversicherung KV Statusfeststellung** im Plugin Krankenkassenrecht Krankenversicherung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kv-062-familienversicherung-einkommensgrenze-minijob` | Familienversicherung nach § 10 SGB V: Einkommensgrenzen, Minijob als Ausschlussgrund, Überprüfung und Nachzahlungsrisiken bei Grenzüberschreitung. |
| `kv-063-statusfeststellung-und-krankenversicherung` | Statusfeststellungsverfahren nach § 7a SGB IV: Scheinselbstständigkeit, sozialversicherungsrechtliche Folgen für die Krankenversicherung und Nachzahlungsrisiken. |
| `kv-064-sperrzeit-arbeitslosengeld-und-krankenversicherung` | Krankenversicherung bei Arbeitslosigkeit und Sperrzeit nach SGB III: Pflichtversicherung, Beitragsübernahme durch Bundesagentur, Lückenproblem und Optionen. |

## Arbeitsweg

Im Plugin Krankenkassenrecht Krankenversicherung gilt für **KV Familienversicherung KV Statusfeststellung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kv-062-familienversicherung-einkommensgrenze-minijob`

**Fokus:** Familienversicherung nach § 10 SGB V: Einkommensgrenzen, Minijob als Ausschlussgrund, Überprüfung und Nachzahlungsrisiken bei Grenzüberschreitung.

# Familienversicherung: Einkommensgrenze und Minijob

## Skill-Zweck

Die Familienversicherung erlaubt beitragsfreie Mitversicherung von Angehörigen. Dieser Skill klärt **Einkommensgrenzen, Auswirkungen des Minijobs und Risiken bei Grenzüberschreitung**.

## Rechtlicher Rahmen

- **§ 10 SGB V** – Familienversicherung: Voraussetzungen, Einkommensgrenzen
- **§ 10 Abs. 1 Nr. 5 SGB V** – Einkommensgrenze: 1/7 der monatlichen Bezugsgröße
- **§ 10 Abs. 1 Nr. 5 Satz 2** – Erhöhte Grenze für geringfügig Beschäftigte: bis Geringfügigkeitsgrenze (520 €/Monat)
- **§ 8 SGB IV** – Geringfügige Beschäftigung (Minijob): bis 520 €/Monat
- **§ 16 SGB IV** – Gesamteinkommen: alle Einkunftsarten
- BSG B 12 KR 4/15 R (Familienversicherung und Einkommensgrenze)

## Einkommensgrenzen 2025

| Grundregel | Grenze |
|------------|--------|
| Einkommensgrenze allgemein | 505 €/Monat (1/7 der Bezugsgröße) |
| Minijob-Ausnahme | Bis 520 €/Monat (Geringfügigkeitsgrenze) |
| Gesamteinkommen | Alle Einkünfte i.S.d. EStG (§ 16 SGB IV) |

## Prüfprogramm

### Schritt 1 – Grundvoraussetzungen prüfen
- Familienmitglied GKV-versichert beim Hauptmitglied?
- Kein eigener KV-Schutz (keine eigene Pflichtversicherung, keine PKV)?
- Wohnort Deutschland oder EU (bei EU-Koordinierungsrecht)?

### Schritt 2 – Einkommensgrenze
- Gesamteinkommen des Familienmitglieds: alle steuerpflichtigen Einkünfte
- § 16 SGB IV: Einkünfte aus Kapital, Vermietung, Honorar – alles einbeziehen
- Kindergeld, Rente (des Familienmitglieds): grundsätzlich nicht als Arbeitseinkommen, aber prüfen

### Schritt 3 – Minijob und Familienversicherung
- Familienmitglied jobbt als Minijobber (≤ 520 €/Monat): Familienversicherung bleibt
- Ausnahme: Minijob-Einkommen allein überschreitet Einkommensgrenze → Familienversicherung endet
- 2 Minijobs: Summe zählt; kann Einkommensgrenze überschreiten

### Schritt 4 – Überprüfung durch Kasse
- Kasse prüft regelmäßig (jährlich): Einkommensnachweise, Steuererklärung
- Rückwirkende Aberkennung: wenn Grenze überschritten wurde → Nachzahlung ab Überschreitung
- Verjährung: 4 Jahre (§ 25 SGB IV)

### Schritt 5 – Übergang zu eigener Mitgliedschaft
- Einkommensgrenze überschritten: freiwillige GKV (§ 9 SGB V) innerhalb 3 Monate
- Pflichtmitgliedschaft bei Überschreitung der JAEG-Grenzen und Arbeitnehmerstatus
- Keine Lücke entstehen lassen

## Typische Fallen

- **Zwei Minijobs eines Partners**: Jeder Minijob unter 520 €, aber zusammen 650 € → Einkommensgrenze überschritten.
- **Kapitalerträge vergessen**: Abgeltungssteuer befreit nicht von GKV-Beitragspflicht bei freiwillig Versicherten; Einkommensgrenze Familienversicherung umfasst Kapitalerträge.
- **Sonderzahlungen**: Einmalzahlungen (Urlaubsgeld, Weihnachtsgeld) können Monatsgrenze überschreiten; Jahresgrenze maßgeblich (Monatsdurchschnitt).
- **Auslandseinkünfte**: Auch Einkünfte aus dem Ausland zählen zum Gesamteinkommen.

## Output-Formate

- Einkommens-Familienversicherungs-Prüfschema
- Überprüfungs-Antrag Kasse
- Übergangsplanung (Einkommensgrenze überschritten)
- Widerspruch gegen Nachzahlungsbescheid
- Familienversicherungs-Checkliste (Jährliche Überprüfung)

## Quellen

- [§ 10 SGB V – Familienversicherung](https://www.gesetze-im-internet.de/sgb_5/__10.html)
- [§ 8 SGB IV – Geringfügige Beschäftigung](https://www.gesetze-im-internet.de/sgb_4/__8.html)
- [§ 16 SGB IV – Gesamteinkommen](https://www.gesetze-im-internet.de/sgb_4/__16.html)
- [BSG B 12 KR 4/15 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [GKV-Spitzenverband Familienversicherung](https://www.gkv-spitzenverband.de)
- [dejure.org § 10 SGB V](https://dejure.org/gesetze/SGB_V/10.html)
## Hinweis: Änderungsmeldepflicht und rückwirkende Beiträge

- Überschreiten der Einkommensgrenze ist der Kasse unverzüglich zu melden
- Rückwirkende Auflösung der Familienversicherung → Beitragsnachforderung ab Überschreitungsmonat
- Minijob-Arbeitgeber zahlt Pauschalbeitrag zur GKV (§ 249b SGB V); dies ist kein Versicherungsschutz des Arbeitnehmers
- Bei Zweifel über Einkommensgrenzen: jährliche Prüfung empfohlen

## Weiterführende Quellen

- [§ 10 SGB V – Familienversicherung](https://www.gesetze-im-internet.de/sgb_5/__10.html)
- [§ 6 Abs. 1 Nr. 1 SGB V – Versicherungsfreiheit Minijob](https://www.gesetze-im-internet.de/sgb_5/__6.html)
- [§ 249b SGB V – Pauschalbeitrag Minijob](https://www.gesetze-im-internet.de/sgb_5/__249b.html)
- [BSG-Rechtsprechung Familienversicherung](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)

## 2. `kv-063-statusfeststellung-und-krankenversicherung`

**Fokus:** Statusfeststellungsverfahren nach § 7a SGB IV: Scheinselbstständigkeit, sozialversicherungsrechtliche Folgen für die Krankenversicherung und Nachzahlungsrisiken.

# Statusfeststellung und Krankenversicherung

## Skill-Zweck

Wer als selbstständig gilt, muss sich selbst krankenversichern. Wenn der Status als scheinselbstständig festgestellt wird, drohen erhebliche Nachzahlungen. Dieser Skill klärt **Statusfeststellung, Krankenversicherungsfolgen und Abwehrstrategien**.

## Rechtlicher Rahmen

- **§ 7 SGB IV** – Beschäftigungsbegriff: persönliche Abhängigkeit, Weisungsgebundenheit
- **§ 7a SGB IV** – Anfrageverfahren bei der Deutschen Rentenversicherung (DRV)
- **§ 5 Abs. 1 Nr. 1 SGB V** – Pflichtversicherung bei Beschäftigung
- **§ 25 SGB IV** – Verjährung von Beitragsansprüchen: 4 Jahre (vorsätzlich: 30 Jahre)
- **§ 28p SGB IV** – Betriebsprüfung durch DRV
- BSG B 12 KR 14/14 R (Statusfeststellung Honorarärzte), BSG B 12 R 11/18 R (Kriterien Selbstständigkeit)

## Statuskriterien (BSG-Maßstäbe)

| Merkmal Selbstständigkeit | Merkmal Beschäftigung |
|--------------------------|----------------------|
| Eigene Betriebsstätte | Arbeitsort vorgegeben |
| Eigenes unternehmerisches Risiko | Festes Entgelt, kein Risiko |
| Mehrere Auftraggeber | Nur ein Auftraggeber |
| Eigene Mitarbeiter | Allein tätig im fremden Betrieb |
| Freie Zeiteinteilung | Arbeitszeitvorgaben |

## Prüfprogramm

### Schritt 1 – Statusfeststellungsverfahren (§ 7a SGB IV)
- Freiwilliges Anfrageverfahren bei DRV Bund
- Antragsteller: Auftraggeber oder Auftragnehmer
- DRV prüft Einzelfall: Gesamtbild der Tätigkeit entscheidend
- Bindende Entscheidung für alle Sozialversicherungsträger

### Schritt 2 – Scheinselbstständigkeit und KV-Folgen
- Feststellung Beschäftigungsverhältnis: rückwirkende KV-Pflichtversicherung
- Nachzahlung: KV-Beiträge für gesamten Zeitraum der Beschäftigung
- AN-Anteil (7,3 %): zahlt Beschäftigter; AG-Anteil (7,3 %): zahlt Auftraggeber
- Wenn private KV während falscher Selbstständigkeit: PKV-Beiträge keine Anrechnung; GKV-Nachzahlung trotzdem

### Schritt 3 – Verjährung und Schutz
- 4 Jahre ab Ende des Jahres der Beitragsfälligkeit (§ 25 SGB IV)
- Bei Vorsatz: 30 Jahre; schwierige Abgrenzung
- Betriebsprüfung durch DRV: bis 4 Jahre rückwirkend; bei Verstößen auch länger

### Schritt 4 – Widerspruch gegen Statusfeststellungsbescheid
- Widerspruch bei DRV möglich; dann Klage beim SG
- Argumente: Gesamtbild zeigt Selbstständigkeit; Einzelmerkmale unzureichend gewichtet
- Einstweiliger Rechtsschutz: bei hohen Nachzahlungen

### Schritt 5 – Honorarärzte und Sonderfälle
- BSG B 12 KR 14/14 R: Honorarärzte in Klinik häufig als Beschäftigte eingestuft
- Hebammen, Rettungsdienstpersonal: zunehmend als abhängig Beschäftigte bewertet
- Plattformarbeit: BSG prüft zunehmend App-Fahrer etc.

## Typische Fallen

- **Ein-Auftraggeber-Falle**: Ausschließliche Tätigkeit für einen Auftraggeber ist starkes Indiz für Abhängigkeit.
- **Frühzeitige Anfrage vergessen**: Ohne Anfrageverfahren kein Vertrauensschutz; DRV kann rückwirkend feststellen.
- **PKV-Versichert als Scheinselbstständiger**: PKV-Beiträge laufen weiter; GKV-Nachzahlung kommt zusätzlich; keine Erstattung der PKV-Beiträge.
- **Arbeitgeberhaftung**: Auftraggeber muss AG-Anteil nachzahlen; strafrechtliche Konsequenzen bei Vorsatz.

## Output-Formate

- Statusfeststellungsantrag DRV
- Selbstständigkeitsmerkmale-Dokumentation
- Widerspruch gegen Statusfeststellungsbescheid
- Nachzahlungs-Ratenantrag
- Statusrisiko-Bewertungsmatrix

## Quellen

- [§ 7 SGB IV – Beschäftigungsbegriff](https://www.gesetze-im-internet.de/sgb_4/__7.html)
- [§ 7a SGB IV – Anfrageverfahren](https://www.gesetze-im-internet.de/sgb_4/__7a.html)
- [BSG B 12 KR 14/14 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [DRV Statusfeststellung](https://www.deutsche-rentenversicherung.de)
- [§ 25 SGB IV – Verjährung](https://www.gesetze-im-internet.de/sgb_4/__25.html)
- [dejure.org § 7 SGB IV](https://dejure.org/gesetze/SGB_IV/7.html)

## 3. `kv-064-sperrzeit-arbeitslosengeld-und-krankenversicherung`

**Fokus:** Krankenversicherung bei Arbeitslosigkeit und Sperrzeit nach SGB III: Pflichtversicherung, Beitragsübernahme durch Bundesagentur, Lückenproblem und Optionen.

# Sperrzeit, Arbeitslosengeld und Krankenversicherung

## Skill-Zweck

Arbeitslose sind in der GKV pflichtversichert. Bei Sperrzeit entfällt jedoch das ALG – aber bleibt der Krankenversicherungsschutz? Dieser Skill klärt **KV-Status während Sperrzeit, Beitragsübernahme und Überbrückungsoptionen**.

## Rechtlicher Rahmen

- **§ 5 Abs. 1 Nr. 2 SGB V** – Pflichtversicherung ALG-Bezieher
- **§ 5 Abs. 1 Nr. 2a SGB V** – Pflichtversicherung Bürgergeld-Bezieher
- **§ 251 Abs. 4a SGB V** – Beitragstragung: Bundesagentur für Arbeit bei ALG-Bezug
- **§ 159 SGB III** – Sperrzeit: Ruhen des ALG-Anspruchs
- **§ 192 Abs. 1 Nr. 2 SGB V** – Mitgliedschaftserhaltung durch Krankengeldanspruch
- **§ 157 SGB III** – Dauer der Sperrzeit (12 Wochen in der Regel)
- BSG B 12 KR 3/10 R (KV während Sperrzeit)

## Sperrzeit und KV-Schutz

| Zeitraum | KV-Status |
|----------|-----------|
| ALG-Bezug regulär | Pflichtversicherung; BA zahlt Beiträge |
| Sperrzeit (ruhendes ALG) | KV bleibt erhalten; ABER kein Beitragszuschuss mehr |
| Bürgergeld-Bezug | Pflichtversicherung; Jobcenter zahlt Beiträge |
| Keine Leistungen mehr | Freiwillige Versicherung (3 Monate Frist) oder Pflichtversicherung wenn Voraussetzungen |

## Prüfprogramm

### Schritt 1 – KV-Status während Sperrzeit
- Sperrzeit = Ruhen des ALG; keine Zahlungen der BA
- GKV-Mitgliedschaft bleibt weiterhin durch § 5 Abs. 1 Nr. 2 SGB V erhalten solange ALG grundsätzlich besteht
- ABER: Beiträge ruhen auch; Kasse fordert Beitrag selbst? → klären

### Schritt 2 – Beitragspflicht während Sperrzeit
- Kein ALG = kein Arbeitsentgelt als Beitragsgrundlage
- Kasse berechnet Beitrag aus Eigenanteil des Arbeitslosen (Mindestbeitrag für Nichtpflichtversicherte?)
- Faktisch: Sperrzeit oft nur 12 Wochen; danach wieder ALG-Bezug; Beitragsrückstände entstehen

### Schritt 3 – Bürgergeld als Auffang
- Nach ALG-Anspruchserschöpfung: Bürgergeld (SGB II) → neue Pflichtversicherung
- Jobcenter zahlt Beiträge (§ 251 Abs. 4 SGB V)
- Kein Versicherungsschutz-Lücke wenn Bürgergeld nahtlos folgt

### Schritt 4 – Freiwillige Versicherung
- Wenn kein ALG und kein Bürgergeld: 3-Monats-Frist für freiwillige GKV (§ 9 SGB V)
- Beitrag: Mindestbemessungsgrundlage; oft erheblich
- Alternative: Partnerkasse (Familienversicherung) prüfen

### Schritt 5 – Sperrzeit-Widerspruch
- Sperrzeit-Bescheid durch Arbeitsamt anfechten (nicht GKV-Zuständigkeit)
- Widerspruch beim Jobcenter/Arbeitsagentur
- Aufschiebende Wirkung: ALG läuft weiter bis Entscheidung über Widerspruch (§ 86a SGG)

## Typische Fallen

- **Sperrzeit und KV-Ruhen**: Manche meinen KV ruht auch während Sperrzeit; das ist FALSCH – KV-Mitgliedschaft bleibt.
- **Eigeninitiative-Kündigung und Sperrzeit**: Selbst kündigen löst Sperrzeit aus; ALG wird für 12 Wochen gesperrt.
- **ALG erschöpft ohne Bürgergeld-Antrag**: Lücke entsteht; sofort Bürgergeld beantragen.
- **Hartz-IV/Bürgergeld und KV**: Neues Bürgergeld-Recht (seit 2023) hat gleiche GKV-Regelungen wie früheres ALG II.

## Output-Formate

- Sperrzeit-KV-Informationsblatt
- Freiwillige GKV-Antrag bei Sperrzeit
- Bürgergeld-Antrag-Checkliste
- Widerspruch Sperrzeit-Bescheid (an Arbeitsverwaltung)
- Beitragsschuldvermeidungs-Plan

## Quellen

- [§ 5 SGB V Nr. 2 – KV Arbeitslose](https://www.gesetze-im-internet.de/sgb_5/__5.html)
- [§ 159 SGB III – Sperrzeit](https://www.gesetze-im-internet.de/sgb_3/__159.html)
- [§ 251 SGB V – Beitragstragung](https://www.gesetze-im-internet.de/sgb_5/__251.html)
- [BSG B 12 KR 3/10 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [Bundesagentur für Arbeit – KV](https://www.arbeitsagentur.de)
- [dejure.org § 5 SGB V](https://dejure.org/gesetze/SGB_V/5.html)
