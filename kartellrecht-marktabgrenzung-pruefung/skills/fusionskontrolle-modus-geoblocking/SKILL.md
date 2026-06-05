---
name: fusionskontrolle-modus-geoblocking
description: "Fusionskontrolle Modus Geoblocking: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Fusionskontrolle Modus Geoblocking

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Fusionskontrolle Modus Geoblocking** im Plugin Kartellrecht-Marktabgrenzung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fusionskontrolle-modus` | Prüft Marktabgrenzung im Kontext der EU-Fusionskontrolle (FKVO 139/2004): Phase I und Phase II SIEC-Test (Significant Impediment to Effective Competition) horizontale und nicht-horizontale Fusionen Effizienzeinrede und Koordinierungseffekte. Schwellenwerte und nationale Zuständigkeit BKartA. |
| `geoblocking-und-kartellrecht-schnittstelle` | Geoblocking und Kartellrecht Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizontal-GVO, DMA. |
| `gesamtbewertung-tragfaehigkeit` | Gesamturteil zur Tragfähigkeit einer Marktabgrenzung: hoch mittel oder gering. Fasst zentrale Schwachstellen in 3 bis 5 scharfen Punkten zusammen. Bewertet Angreifbarkeit vor Gericht oder Behoerde und empfiehlt prozesstaktische Konsequenzen für das eigene Team. |
| `gun-jumping-global` | Gun Jumping und Closing Control: Fachmodul für großes Kartellrecht mit BKartA, DG Competition, FTC/DOJ und internationalen Behörden; prüft Vollzugsverbot, Clean Teams, Integration Planning und Informationsaustausch vor Closing prüfen, Evidenz, Fristen, Strategie und Quellen. |
| `handelsvertreterprivileg-echtes-unechtes-agenturmodell` | Handelsvertreterprivileg echtes unechtes Agenturmodell: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizontal-GVO, DMA. |

## Arbeitsweg

Im Plugin Kartellrecht-Marktabgrenzung gilt für **Fusionskontrolle Modus Geoblocking**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `fusionskontrolle-modus`

**Fokus:** Prüft Marktabgrenzung im Kontext der EU-Fusionskontrolle (FKVO 139/2004): Phase I und Phase II SIEC-Test (Significant Impediment to Effective Competition) horizontale und nicht-horizontale Fusionen Effizienzeinrede und Koordinierungseffekte. Schwellenwerte und nationale Zuständigkeit BKartA.

# Fusionskontrolle — Modus

## Fachkern: Fusionskontrolle — Modus
- **Spezialgegenstand:** Fusionskontrolle — Modus. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** Art. 101/102 AEUV, VO 1/2003, FKVO, GWB, Vertikal-GVO, DMA/DSA-Schnittstellen, private damages und Behördenpraxis.
- **Entscheidende Weiche:** Markt, Verhalten, Beteiligte, Schwelle, Effekt, Effizienzrechtfertigung, Verfahren, Dawn Raid/Leniency und Schadensersatz getrennt ordnen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Rechtsrahmen

- FKVO 139/2004 (EU): Für Zusammenschlüsse mit gemeinschaftsweiter Bedeutung (Umsatzschwellen Art. 1 FKVO).
- §§ 35–43 GWB (national): Für Zusammenschlüsse unterhalb der FKVO-Schwellen.

## Verfahrensphasen

### Phase I (Art. 6 FKVO)
25 Arbeitstage. Endet mit Freigabe, Freigabe mit Auflagen oder Verweis auf Phase II.

### Phase II (Art. 8 FKVO)
90 Arbeitstage (+ Verlängerung). Vertiefte Prüfung. Endet mit Freigabe, Freigabe mit Auflagen oder Untersagung.

## SIEC-Test

**Significant Impediment to Effective Competition** — Seit FKVO 2004 Ablösung des früheren Marktbeherrschungstests. Weiter als reine Marktbeherrschungsprüfung:

Zwei Szenarien:
1. **Dominanz**: Fusion schafft oder stärkt eine beherrschende Stellung.
2. **Koordinierte Effekte**: Fusion erhöht Wahrscheinlichkeit wettbewerbsschädlicher Koordinierung (ohne Dominanz).

## Marktdefinition im Fusionskontext

Besonderheiten:
- Marktdefinition auf Basis des Status vor Fusion (Ist-Zustand).
- Counterfactual-Analyse: Wie würde Wettbewerb ohne Fusion aussehen? (Relevant für Failing-Firm-Defence).
- Prospektive Betrachtung: Zukünftige Marktentwicklungen (Innovationsmärkte) einbeziehen.

## Horizontale Fusionen

Direkte Eliminierung von Wettbewerbsdruck zwischen den Fusionspartnern.

Marktanteilsschwellen (Soft Law HM-Leitlinien 2004):
- Kombinierter Marktanteil < 25 Prozent: In der Regel keine Bedenken.
- Kombinierter Marktanteil > 50 Prozent: Starke Bedenken (Marktbeherrschungsvermutung).
- HHI-Analyse: Herfindahl-Hirschman-Index zur Konzentrationsberechnung.

## Nicht-horizontale Fusionen

Vertikale und Konglomeratsfusionen (EU-Leitlinien 2008):
- Abschottungseffekte (Input Foreclosure, Customer Foreclosure).
- Leveraging (Marktmacht auf einem Markt genutzt für anderen Markt).
- Portfolio-Effekte bei Konglomeratsfusionen.

## Effizienzeinrede

Fusionsbedingte Effizienzgewinne können wettbewerbsschädliche Effekte aufwiegen, wenn:
1. Effizienzgewinne fusionsspezifisch (nicht ohne Fusion erreichbar).
2. Effizienzgewinne nachgewiesen und quantifizierbar.
3. Verbraucher profitieren (pass-through zum Kunden).

## Leitentscheidungen Fusionskontrolle

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- EK, Beschl. v. 04.09.2019 — COMP/M.9064 (Google/Fitbit) — Fusionspraxisfaelle Digitalmärkte; Datenzugang als Wettbewerbsfaktor.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Prüfprotokoll Fusionskontrolle

```
Anmeldepflicht: [FKVO / GWB / keine]
Phase: [Phase I / Phase II]
Marktanteil kombiniert: [%]
HHI vor Fusion: [Wert]
HHI nach Fusion: [Wert]
Delta HHI: [Wert]
SIEC-Bedenken: [Dominanz / Koordinierung / keine]
Effizienzeinrede: [ja / nein]
Ergebnis: [freigabefähig / mit Auflagen / kritisch]
```

## 2. `geoblocking-und-kartellrecht-schnittstelle`

**Fokus:** Geoblocking und Kartellrecht Schnittstelle: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizontal-GVO, DMA.

# Geoblocking und Kartellrecht Schnittstelle

## Fachkern: Geoblocking und Kartellrecht Schnittstelle
- **Spezialgegenstand:** Geoblocking und Kartellrecht Schnittstelle. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** Art. 101/102 AEUV, VO 1/2003, FKVO, GWB, Vertikal-GVO, DMA/DSA-Schnittstellen, private damages und Behördenpraxis.
- **Entscheidende Weiche:** Markt, Verhalten, Beteiligte, Schwelle, Effekt, Effizienzrechtfertigung, Verfahren, Dawn Raid/Leniency und Schadensersatz getrennt ordnen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Geoblocking und Kartellrecht Schnittstelle** im Bereich **Kartellrecht — Marktabgrenzung und Wettbewerb**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Kartellrecht deutsch/europäisch: Kartellverbot, Missbrauch, Fusionskontrolle, Private Enforcement, Compliance und Digital Markets.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfmatrix, Argumentationslinie, Risikoampel, Quellencheck und verwertbarer Entwurfsbaustein. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?

## 3. `gesamtbewertung-tragfaehigkeit`

**Fokus:** Gesamturteil zur Tragfähigkeit einer Marktabgrenzung: hoch mittel oder gering. Fasst zentrale Schwachstellen in 3 bis 5 scharfen Punkten zusammen. Bewertet Angreifbarkeit vor Gericht oder Behoerde und empfiehlt prozesstaktische Konsequenzen für das eigene Team.

# Gesamtbewertung — Tragfähigkeit der Marktabgrenzung

## Fachkern: Gesamtbewertung — Tragfähigkeit der Marktabgrenzung
- **Spezialgegenstand:** Gesamtbewertung — Tragfähigkeit der Marktabgrenzung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** Art. 101/102 AEUV, VO 1/2003, FKVO, GWB, Vertikal-GVO, DMA/DSA-Schnittstellen, private damages und Behördenpraxis.
- **Entscheidende Weiche:** Markt, Verhalten, Beteiligte, Schwelle, Effekt, Effizienzrechtfertigung, Verfahren, Dawn Raid/Leniency und Schadensersatz getrennt ordnen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Bewertungsrahmen

Die Gesamtbewertung erfolgt nach Abschluss aller Einzel-Prüfungsschritte. Sie verdichtet die Erkenntnisse zu einem klaren Urteil mit prozesstaktischen Konsequenzen.

## Tragfähigkeitsskala

### HOCH
Marktabgrenzung ist juristisch und ökonomisch gut fundiert. Methodik transparent und nachvollziehbar. Evidenz trianguliert. Konsistent mit Behördenpraxis und Rechtsprechung.

**Prozesstaktik:** Abgrenzung kann offensiv vertreten werden. Risiko einer erfolgreichen Anfechtung gering.

### MITTEL
Marktabgrenzung ist vertretbar, aber angreifbar. Methodische oder Evidenz-Schwächen bestehen. Unter Verteidigungsdruck könnten einzelne Argumente nicht standhalten.

**Prozesstaktik:** Nachbesserung bestimmter Argumente empfohlen. Alternativdefinitionen als Rückfallposition vorbereiten.

### GERING
Marktabgrenzung hat fundamentale Schwächen. Ergebnisgetriebene Argumentation erkennbar. SSNIP-Test fehlt oder ist fehlerhaft angewendet. Evidenz einseitig oder unvollständig.

**Prozesstaktik:** Abgrenzung ist hochriskant. Entweder grundlegende Überarbeitung oder Alternativstrategie erforderlich.

## Standardformat der Gesamtbewertung

```
GESAMTURTEIL: [HOCH / MITTEL / GERING]

ZENTRALE SCHWACHSTELLEN:

1. [Schwachstelle — konkret und scharf formuliert, z.B.:
 "SSNIP-Test-Ergebnis beruht auf veralteten Daten aus 2019 und
 wurde nicht auf Cellophane-Fallacy-Risiko geprüft."]

2. [Schwachstelle — z.B.:
 "Angebotsseitige Substitution durch Anbieter Z wird behauptet,
 aber der Umstellungszeitraum von 18 Monaten überschreitet
 den EU-Standard von 12 Monaten."]

3. [Schwachstelle — z.B.:
 "Interne Marktberichte des Unternehmens aus 2022 bezeichnen
 Produkt X als 'direkten Konkurrenten', der in der vorgelegten
 Abgrenzung aber ausgeschlossen wird."]

4. [optional]

5. [optional]

ANGREIFBARKEIT VOR GERICHT/BEHÖRDE:
[sehr hoch / hoch / mittel / gering]

PROZESSTAKTISCHE KONSEQUENZ:
[konkrete Empfehlung in 2–4 Sätzen]
```

## Checkliste für die Gesamtbewertung

| Prüfungsbereich | Bewertung | Gewichtung |
|-----------------|-----------|------------|
| SSNIP-Test | | Hoch |
| Nachfragesubstitution | | Hoch |
| Angebotsseitige Substitution | | Mittel |
| Räumlicher Markt | | Mittel |
| Evidenzqualität | | Hoch |
| Konsistenz | | Hoch |
| Behördenpraxis-Abgleich | | Mittel |
| Alternativdefinitionen geprüft | | Mittel |

## Hinweis

Das Gesamturteil ersetzt keine anwaltliche Würdigung im Einzelfall. Es ist eine strukturierte Einschätzung auf Basis der dokumentierten Prüfungsschritte.

## Leitentscheidungen Gesamtbewertung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 4. `gun-jumping-global`

**Fokus:** Gun Jumping und Closing Control: Fachmodul für großes Kartellrecht mit BKartA, DG Competition, FTC/DOJ und internationalen Behörden; prüft Vollzugsverbot, Clean Teams, Integration Planning und Informationsaustausch vor Closing prüfen, Evidenz, Fristen, Strategie und Quellen.

# Gun Jumping und Closing Control

## Fachkern: Gun Jumping und Closing Control
- **Spezialgegenstand:** Gun Jumping und Closing Control. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** Art. 101/102 AEUV, VO 1/2003, FKVO, GWB, Vertikal-GVO, DMA/DSA-Schnittstellen, private damages und Behördenpraxis.
- **Entscheidende Weiche:** Markt, Verhalten, Beteiligte, Schwelle, Effekt, Effizienzrechtfertigung, Verfahren, Dawn Raid/Leniency und Schadensersatz getrennt ordnen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Gun Jumping und Closing Control** im Bereich **Kartellrecht Global Competition Law**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Vollzugsverbot, Clean Teams, Integration Planning und Informationsaustausch vor Closing prüfen

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** GWB, Art. 101/102 AEUV, FKVO, VO 1/2003, Vertikal-GVO, DMA, Sherman Act, Clayton Act, FTC Act und lokale Regeln live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.


## Spezielle Leitplanken

- Bei Mehrjurisdiktionsfällen lokale Counsel-Fragen ausdrücklich ausgeben.
- Behördenpraxis und Formulare live prüfen.
- Keine nicht verifizierten Bußgeld- oder Rechtsprechungszitate.

## Output

Erzeuge je nach Auftrag: Jurisdiktionsmatrix, Verfahrensplan, Behördenstrategie, Memo, Dawn-Raid-Plan, Fusionskontrollcheck oder Schriftsatzbaustein. Am Ende immer: Risikoampel, offene Punkte, Quellencheck und nächster Schritt.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei aktuellem Behörden-, Kammer-, Berufs- oder Wettbewerbsrecht zuerst die amtliche Normfassung und die zuständige Behörden- oder Kammerseite prüfen.

## 5. `handelsvertreterprivileg-echtes-unechtes-agenturmodell`

**Fokus:** Handelsvertreterprivileg echtes unechtes Agenturmodell: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizontal-GVO, DMA.

# Handelsvertreterprivileg echtes unechtes Agenturmodell

## Fachkern: Handelsvertreterprivileg echtes unechtes Agenturmodell
- **Spezialgegenstand:** Handelsvertreterprivileg echtes unechtes Agenturmodell. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** Art. 101/102 AEUV, VO 1/2003, FKVO, GWB, Vertikal-GVO, DMA/DSA-Schnittstellen, private damages und Behördenpraxis.
- **Entscheidende Weiche:** Markt, Verhalten, Beteiligte, Schwelle, Effekt, Effizienzrechtfertigung, Verfahren, Dawn Raid/Leniency und Schadensersatz getrennt ordnen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Handelsvertreterprivileg echtes unechtes Agenturmodell** im Bereich **Kartellrecht — Marktabgrenzung und Wettbewerb**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

**Fachlicher Fokus:** Kartellrecht deutsch/europäisch: Kartellverbot, Missbrauch, Fusionskontrolle, Private Enforcement, Compliance und Digital Markets.

## Startfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfmatrix, Argumentationslinie, Risikoampel, Quellencheck und verwertbarer Entwurfsbaustein. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?
