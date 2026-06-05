---
name: inv-insurance-press
description: "Inv 050 Insurance Notification, Inv 051 Press Strategy: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Inv 050 Insurance Notification, Inv 051 Press Strategy

## Arbeitsbereich

Dieser Skill bündelt **Inv 050 Insurance Notification, Inv 051 Press Strategy** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `inv-050-insurance-notification` | Koordiniert die Versicherungsmeldung bei Internal Investigations – D&O, Crime-Versicherung, Cyber-Versicherung, Meldepflichten und Deckungsstrategien. |
| `inv-051-press-strategy` | Entwickelt die Pressestrategie bei Internal Investigations – Ad-hoc-Pflicht, Reputationsmanagement, Medienanfragen und Krisenkommunikation. |

## Arbeitsweg

Für **Inv 050 Insurance Notification, Inv 051 Press Strategy** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `internal-investigations-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `inv-050-insurance-notification`

**Fokus:** Koordiniert die Versicherungsmeldung bei Internal Investigations – D&O, Crime-Versicherung, Cyber-Versicherung, Meldepflichten und Deckungsstrategien.

# Versicherungsmeldung bei Internal Investigations

## Rechtlicher Rahmen

Versicherungsmeldungen bei Internal Investigations betreffen vor allem die D&O-Versicherung (Directors & Officers), die Crime-/Vertrauensschadensversicherung und ggf. die Cyber-Versicherung. Meldepflichten sind im Versicherungsvertrag geregelt und nach § 23 VVG (Anzeigepflicht bei Gefahrerhöhung) und §§ 82, 83 VVG (Schadenminderungspflicht, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/vvg_2008/__82.html)) gesetzlich unterlegt. Verspätete Meldung kann zur Leistungsfreiheit des Versicherers führen. Claims-Made-Policen verlangen, dass sowohl das schädigende Ereignis als auch die Meldung in der Versicherungsperiode liegen.

## Ziel dieses Skills

Dieser Skill stellt sicher, dass alle relevanten Versicherungsmeldungen rechtzeitig, vollständig und so formuliert werden, dass der Deckungsschutz maximiert und nicht durch fehlerhafte Kommunikation gefährdet wird.

## Arbeitsprogramm

### 1. Relevante Versicherungsarten
- **D&O-Versicherung**: Deckung für Schadensersatzansprüche gegen Organmitglieder (Vorstand, Aufsichtsrat, Geschäftsführer).
- **Crime-/Vertrauensschadensversicherung** (VSV): Deckung für Schäden durch Mitarbeiter-Betrug, Diebstahl, Unterschlagung.
- **Cyber-Versicherung**: Deckung für Cyberangriffe, Datenlecks, Betriebsunterbrechungen.
- **Professional-Indemnity (PI)**: Deckung für Berufsfehler; relevant bei Beratungsunternehmen.
- **General Liability**: prüfen, ob der Schaden erfasst ist.

### 2. D&O-Versicherung – Meldung und Deckungsvoraussetzungen
- **Claims-Made-Prinzip**: Anspruch und Meldung müssen in der Versicherungsperiode liegen.
- **Meldepflicht**: sofortige Meldung nach Kenntnis eines möglichen Deckungsanspruchs; kein Abwarten bis zum Untersuchungsabschluss.
- **Selbstbehalt** (Retention): gemäß § 25 VVG 2009 (Änderungen 2020): Vorstandsmitglieder müssen einen Selbstbehalt von 10 % des Schadens, höchstens 1,5-faches Jahresfixgehalt tragen.
- **Ausschluss vorsätzliches Handeln**: wenn Pflichtverletzung vorsätzlich war, greift die D&O häufig nicht; ggf. erst nach Freispruch oder Verfahrenseinstellung.

### 3. Crime-Versicherung (VSV)
- Deckung: Vermögensschäden durch unehrliche oder betrügerische Handlungen von Mitarbeitern.
- Meldepflicht: unverzüglich nach Entdeckung; Verzögerung kann zur teilweisen oder vollständigen Leistungsfreiheit führen.
- Nachweisanforderungen: vollständige Dokumentation des Schadens; Name des Täters und Handlungsbeschreibung.
- Sublimits: prüfen, ob für bestimmte Schadensarten (z. B. Social Engineering, Cyberbetrug) gesonderte Limits gelten.

### 4. Cyber-Versicherung
- Deckungsanlass: Datenpanne, Ransomware, Betriebsunterbrechung.
- Sofortige Meldung nach Entdeckung; keine eigenständigen Maßnahmen vor Rücksprache mit Versicherer.
- Incident-Response-Kosten: in der Regel vorab genehmigungspflichtig (IT-Forensiker, Krisenkommunikation).
- DSGVO-Bußgelder: regelmäßig nicht versicherbar (Ordre-public-Vorbehalt); aber Verteidigungskosten oft gedeckt.

### 5. Verhältnis zu behördlichen Ermittlungen
- Defense Costs Coverage: Kosten für externe Anwälte im Rahmen behördlicher Untersuchungen häufig gedeckt.
- Policentext prüfen: sind Compliance-Untersuchungen (Internal Investigations) explizit erfasst?
- Versicherer hat Mitspracherecht bei Verteidigungsstrategie (in manchen Policen); keine Aussagen ohne Abstimmung.
- Regressansprüche: wenn Versicherer zahlt und Täter identifiziert wurde, kann Versicherer Regress nehmen (§ 86 VVG).

### 6. Kommunikation mit Versicherer
- Keine überschießende Offenbarung von Untersuchungsergebnissen an Versicherer.
- Keine falschen Aussagen gegenüber Versicherer (§ 31 VVG: arglistige Täuschung führt zu Leistungsfreiheit).
- Vorläufige Meldung: Deckungsanspruch anzeigen, ohne alle Einzelheiten preiszugeben; Detailmeldung folgt nach Untersuchungsabschluss.
- Anwalt für Versicherungsrecht hinzuziehen: bei komplexen Deckungsfragen.

### 7. Deckungsstreitigkeiten
- Versicherer lehnt Deckung ab (z. B. wegen angeblichem Vorsatz): Widerspruch und ggf. Schiedsverfahren oder Klage.
- § 115 VVG: Direktklage gegen Versicherer bei Pflichtversicherungen.
- Musterfeststellungsklage bei gleichartigen Deckungsstreitigkeiten (z. B. nach COVID-19-Betriebsunterbrechungsfällen).

## Red-Team-Fragen

- Wurden alle relevanten Versicherer (D&O, Crime, Cyber) unverzüglich nach Entdeckung des Schadens informiert?
- Sind die Meldepflichten aus dem Versicherungsvertrag vollständig erfüllt?
- Hat der Versicherer Mitspracherecht bei der Verteidigungsstrategie, und wurde er in strategische Entscheidungen eingebunden?
- Könnte die D&O-Versicherung wegen Vorsatz der Täter leistungsfrei sein?
- Wurden Incident-Response-Kosten (Forensiker, Krisenkommunikation) vorab mit dem Cyber-Versicherer abgestimmt?
- Ist der Selbstbehalt der Organmitglieder korrekt berechnet und berücksichtigt?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| §§ 82, 83 VVG | Schadenminderungspflicht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/vvg_2008/__82.html) |
| § 23 VVG | Anzeigepflicht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/vvg_2008/__23.html) |
| § 86 VVG | Regressanspruch Versicherer | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/vvg_2008/__86.html) |
| § 31 VVG | Arglistige Täuschung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/vvg_2008/__31.html) |

## Ausgabeformate

- **Versicherungsmeldungs-Template** (D&O, Crime, Cyber)
- **Meldepflichten-Checkliste** pro Versicherungsart
- **Deckungsanalyse-Matrix** (Schaden × Versicherung × Deckungsumfang)
- **Selbstbehalt-Berechnungs-Vorlage**
- **Deckungsstreit-Eskalationsplan**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `inv-051-press-strategy`

**Fokus:** Entwickelt die Pressestrategie bei Internal Investigations – Ad-hoc-Pflicht, Reputationsmanagement, Medienanfragen und Krisenkommunikation.

# Pressestrategie und Krisenkommunikation

## Rechtlicher Rahmen

Die Kommunikation nach außen während einer Internal Investigation unterliegt kapitalmarktrechtlichen Pflichten (Art. 17 MAR: Ad-hoc-Meldepflicht bei kursrelevanten Informationen, [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014R0596)), dem Strafrecht (§ 353b StGB: Verletzung von Dienstgeheimnissen ist irrelevant für Private, aber § 17 UWG a. F./GeschGehG schützt Unternehmensgeheimnisse) und dem allgemeinen Persönlichkeitsrecht der Betroffenen. Falsche oder irreführende Aussagen gegenüber der Presse können Strafbarkeit (§ 186 StGB: üble Nachrede) oder Schadensersatzpflichten begründen.

## Ziel dieses Skills

Dieser Skill entwickelt eine kontrollierte Kommunikationsstrategie, die Reputationsschäden minimiert, gesetzliche Pflichten erfüllt und die Untersuchung nicht gefährdet.

## Arbeitsprogramm

### 1. Ad-hoc-Meldepflicht – Prüfung
- Art. 17 MAR: Insider-Information, die direkt das Unternehmen betrifft und kursrelevant ist, muss unverzüglich veröffentlicht werden.
- Liegt eine kursrelevante Information vor? Ist der Verstoß so wesentlich, dass ein verständiger Investor die Information bei seiner Anlageentscheidung berücksichtigen würde?
- Self-Befreiung (Art. 17 Abs. 4 MAR): temporäre Verzögerung möglich, wenn sofortige Offenlegung die Untersuchung gefährdet; strenge Voraussetzungen.
- BaFin: Self-Befreiung muss BaFin nachgemeldet werden.

### 2. Kommunikationsstrategie-Optionen
- **No comment**: sinnvoll, wenn Ermittlungen noch nicht abgeschlossen sind; signalisiert aber Schweigen.
- **Reaktive Stellungnahme**: nur auf konkrete Anfragen reagieren; kein proaktives Herausgehen.
- **Proaktive Pressemitteilung**: nach Abschluss der Untersuchung oder bei unvermeidlichem Bekanntwerden; Kontrolle über das Narrativ.
- **Board Statement**: bei schwerwiegenden Fällen mit öffentlichem Interesse.

### 3. Kernbotschaften
- Das Unternehmen nimmt Compliance-Verstöße ernst.
- Es wurden sofortige Untersuchungsmaßnahmen eingeleitet.
- Das Unternehmen kooperiert vollständig mit den Behörden.
- Maßnahmen zur Verhinderung künftiger Vorfälle wurden eingeleitet.
- **Nicht**: Schuldeingeständnisse, Nennung von Tätern (Unschuldsvermutung), Details der laufenden Untersuchung.

### 4. Persönlichkeitsrechte der Betroffenen
- Namentliche Nennung von Beschuldigten vor rechtskräftiger Verurteilung: hohes Haftungsrisiko (§ 823 Abs. 1 BGB, Allgemeines Persönlichkeitsrecht; Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG).
- Unschuldsvermutung (Art. 6 Abs. 2 EMRK): keine öffentliche Verurteilung vor Gerichtsurteil.
- DSGVO Art. 85: Medienfreiheit vs. Datenschutz; schwieriger Balanceakt.

### 5. Medienanfragen-Management
- Alle Medienanfragen werden zentral durch die Pressestelle geleitet; keine direkte Kommunikation von Mitarbeitern oder Anwälten mit Medien.
- Response-Time: bei kapitalmarktorientierten Unternehmen innerhalb weniger Stunden.
- Off-the-record-Gespräche: nur durch erfahrene PR-Berater; immer mit Anwalt abgestimmt.
- Background Briefings für ausgewählte Journalisten: nur zur Kontextualisierung, nie zur Enthüllung von Untersuchungsdetails.

### 6. Social Media
- Falsche Information in sozialen Netzwerken über den Vorfall: Gegendarstellungsrecht nach § 56 MStV (Medienstaatsvertrag).
- Mitarbeiter-Social-Media: Policy, die unkontrollierten Kommentaren vorbeugt.
- Darknet/Leak-Sites: wenn Hacker Untersuchungsunterlagen leaken, sofort Reaktion (Löschungsanspruch, Behördeneinschaltung).

### 7. Interne Kommunikation
- Mitarbeiter erfahren Pressemitteilungen idealerweise nicht zuerst aus den Medien.
- Interne Kommunikation vor externer Veröffentlichung: CEO-Statement an alle Mitarbeiter.
- Q&A-Dokument für Manager: wie antworten auf Mitarbeiterfragen?
- Verbot, intern Details der Untersuchung zu diskutieren (DSGVO, Unschuldsvermutung, Beweissicherung).

## Red-Team-Fragen

- Besteht eine Ad-hoc-Meldepflicht, und wurde die Self-Befreiungsentscheidung dokumentiert?
- Enthält die Pressemitteilung Aussagen, die als Schuldeingeständnis interpretiert werden könnten?
- Wurden Beschuldigte in der Öffentlichkeit namentlich genannt, obwohl die Unschuldsvermutung gilt?
- Sind alle Mitarbeiter angewiesen, keine Medienkommentare abzugeben, und wird dies kontrolliert?
- Ist die interne Kommunikation vor der externen Kommunikation erfolgt?
- Gibt es Lücken zwischen dem, was der Presse mitgeteilt wurde, und dem, was den Behörden mitgeteilt wurde?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| Art. 17 MAR | Ad-hoc-Meldepflicht | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32014R0596) |
| § 823 BGB | Persönlichkeitsrecht | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__823.html) |
| Art. 6 Abs. 2 EMRK | Unschuldsvermutung | Europarat |
| Art. 85 DSGVO | Medienfreiheit vs. Datenschutz | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |

## Ausgabeformate

- **Krisen-Pressemitteilung** (Template mit Kernbotschaften)
- **CEO-Statement** (intern, vor externer Kommunikation)
- **Q&A-Dokument** für Manager und Mitarbeiter
- **Ad-hoc-Meldungs-Entscheidungsbaum**
- **Media-Handling-Protokoll** für Journalisten-Anfragen

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
