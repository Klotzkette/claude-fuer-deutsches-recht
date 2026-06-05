---
name: marktabgrenzung-kontextanalyse-mehrseitige
description: "Kontextanalyse Mehrseitige: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kontextanalyse Mehrseitige

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Kontextanalyse Mehrseitige** im Plugin Kartellrecht-Marktabgrenzung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `marktabgrenzung-kontextanalyse` | Verfahren beginnt und Verfahrensart und Parteistellung muessen bestimmt werden bevor die Marktabgrenzung-Analyse starten kann. Identifiziert Verfahrensart Fusionskontrolle Kartellverbot Missbrauchsverfahren und Zielrichtung der Marktabgrenzung. Normen FKVO 139/2004 Art. 101 102 AEUV §§ 1 18 19 35 GWB. Prüfraster ergebnisgetriebene Argumentation Parteistellung methodische Vorentscheidungen prozessualer Kontext. Output Kontext-Analysememo mit Verfahrensart Parteiposition und Routing-Empfehlung für Folge-Skills. Abgrenzung: gesamtbewertung-tragfähigkeit für Gesamturteil nach der Analyse. |
| `mehrseitige-maerkte-plattformen` | Prüffeld für mehrseitige maerkte plattformen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `merger-remedies-global` | Merger Remedies global: Fachmodul für großes Kartellrecht mit BKartA, DG Competition, FTC/DOJ und internationalen Behörden; prüft Divestiture, Behavioural Remedies, Monitoring Trustee und Hold-Separate planen, Evidenz, Fristen, Strategie und Quellen. |
| `ministererlaubnis-42-gwb` | Ministererlaubnis § 42 GWB: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizontal-GVO, DMA. |
| `minority-shareholdings-competition` | Minderheitsbeteiligungen und Competition: Fachmodul für großes Kartellrecht mit BKartA, DG Competition, FTC/DOJ und internationalen Behörden; prüft Kontrolle, Einfluss, Informationsrechte, Common Ownership und Fusionskontrolle prüfen, Evidenz, Fristen, Strategie und Quellen. |

## Arbeitsweg

Im Plugin Kartellrecht-Marktabgrenzung gilt für **Kontextanalyse Mehrseitige**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `marktabgrenzung-kontextanalyse`

**Fokus:** Verfahren beginnt und Verfahrensart und Parteistellung muessen bestimmt werden bevor die Marktabgrenzung-Analyse starten kann. Identifiziert Verfahrensart Fusionskontrolle Kartellverbot Missbrauchsverfahren und Zielrichtung der Marktabgrenzung. Normen FKVO 139/2004 Art. 101 102 AEUV §§ 1 18 19 35 GWB. Prüfraster ergebnisgetriebene Argumentation Parteistellung methodische Vorentscheidungen prozessualer Kontext. Output Kontext-Analysememo mit Verfahrensart Parteiposition und Routing-Empfehlung für Folge-Skills. Abgrenzung: gesamtbewertung-tragfähigkeit für Gesamturteil nach der Analyse.

# Marktabgrenzung — Kontextanalyse

## Fachkern: Marktabgrenzung — Kontextanalyse
- **Spezialgegenstand:** Marktabgrenzung — Kontextanalyse. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** Art. 101/102 AEUV, VO 1/2003, FKVO, GWB, Vertikal-GVO, DMA/DSA-Schnittstellen, private damages und Behördenpraxis.
- **Entscheidende Weiche:** Markt, Verhalten, Beteiligte, Schwelle, Effekt, Effizienzrechtfertigung, Verfahren, Dawn Raid/Leniency und Schadensersatz getrennt ordnen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Zweck

Bevor die sachliche und räumliche Marktabgrenzung inhaltlich geprüft werden kann, muss ihr Entstehungskontext verstanden werden. Marktdefinitionen sind selten neutral: Sie werden von Parteien strategisch eingesetzt, um Marktanteile zu verkleinern (wenn Marktbeherrschung droht) oder zu vergrößern (wenn Effizienzgründe vorgebracht werden).

## Analyse-Schritte

### 1. Verfahrensart bestimmen

| Verfahren | Relevante Norm | Primärziel der Marktabgrenzung |
|-----------|---------------|-------------------------------|
| Fusionskontrolle | FKVO 139/2004 / §§ 35 ff. GWB | Marktanteilsschwellen und SIEC-Test |
| Kartellverbot | Art. 101 AEUV / § 1 GWB | Wettbewerbsbeschränkung bewirkt/bezweckt |
| Missbrauchsverbot | Art. 102 AEUV / §§ 19–20 GWB | Marktbeherrschungsnachweis |
| BKartA-Sektoruntersuchung | § 32e GWB | Strukturanalyse ohne konkretes Verfahren |

### 2. Wer hat die Marktabgrenzung vorgelegt?

- **Eigenes Team**: Welches Ergebnis soll gestützt werden? Fusionszulässigkeit (weiter Markt gewünscht) oder Missbrauchsabwehr (enger Markt zu vermeiden)?
- **Gegnerische Partei**: Gegensätzliche Interessenlage identifizieren.
- **Wettbewerbsbehörde** (BKartA, Kommission, NCA): Prüfung auf methodische Konsistenz und Abweichungen von Präzedenzfällen.

### 3. Prüfung auf ergebnisgetriebene Argumentation

Indizien für Ergebnisorientierung:
- Markt wird ohne ökonomische Begründung sehr eng/weit definiert.
- Kundendaten und Elastizitäten fehlen, stattdessen nur funktionale Beschreibungen.
- Präzedenzfälle werden selektiv zitiert oder ohne Kontext übertragen.
- SSNIP-Test wird übergangen oder die Preissteigerung wird außerhalb des Rahmens 5–10 Prozent gewählt.
- Angebotsseitige Substitution wird als Argument für breiten Markt eingesetzt, ohne Kurzfristigkeitscheck.

### 4. Dokumentation

```
Verfahrensart: [Fusionskontrolle / Kartell / Missbrauch]
Vorleger der Abgrenzung: [Eigenes Team / Gegner / Behörde]
Erkennbare Zielrichtung: [Markt enger / weiter als plausibel]
Ergebnisorientierungs-Score: [gering / mittel / hoch]
Begründung: [...]
```

### 5. Überleitung

Der Output dieser Kontextanalyse fließt in alle nachfolgenden Prüfungsschritte ein. Er bestimmt die Prüfungsintensität und die Richtung der Alternativdefinitionen (Skills `alternative-marktdefinition-eng` und `alternative-marktdefinition-weit`).

## Leitentscheidungen Kontextanalyse

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- EK, Marktdefinitionsbekanntmachung 2024 Rn. 10-30 — Kontextfaktoren: Regulierung, Substitution, Technologie, Verhalten.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `mehrseitige-maerkte-plattformen`

**Fokus:** Prüffeld für mehrseitige maerkte plattformen: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

# Mehrseitige Märkte und Plattformen

## Fachkern: Mehrseitige Märkte und Plattformen
- **Spezialgegenstand:** Mehrseitige Märkte und Plattformen. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** Art. 101/102 AEUV, VO 1/2003, FKVO, GWB, Vertikal-GVO, DMA/DSA-Schnittstellen, private damages und Behördenpraxis.
- **Entscheidende Weiche:** Markt, Verhalten, Beteiligte, Schwelle, Effekt, Effizienzrechtfertigung, Verfahren, Dawn Raid/Leniency und Schadensersatz getrennt ordnen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Grundproblem

Klassische Marktdefinition setzt einen Preis voraus. Plattformmärkte sind häufig zweiseitig: Eine Seite erhält Dienste kostenlos (Nutzer), die andere Seite zahlt (Werbetreibende, Entwickler). Keine der klassischen Marktdefinitionsmethoden greift ohne Anpassung.

## Rechtliche Einordnung

### Getrennte Märkte

Der EuGH tendiert dazu, die Marktseiten als getrennte Märkte zu definieren:
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Integrierte Betrachtung

Alternativ: Plattform als Gesamtprodukt, Preis = Summe der Preise beider Seiten (Rochet/Tirole, 2003).

## Prüfungsschritte

### 1. Identifikation der Marktseiten

- Welche Nutzergruppen interagieren über die Plattform?
- Welche Seite zahlt, welche erhält kostenlose Dienste?
- Asymmetrie: Wer profitiert von Netzwerkeffekten der anderen Seite?

### 2. Direkte vs. indirekte Netzwerkeffekte

| Typ | Beschreibung | Marktdefinitionsrelevanz |
|-----|-------------|--------------------------|
| Direkt | Mehr Nutzer → Mehrwert für alle Nutzer | Gleiche Seite |
| Indirekt | Mehr Nutzer (Seite A) → Mehrwert für Seite B | Kreuzeffekt |

### 3. SSNIP-Test auf Plattformen

Probleme:
- Preiserhöhung auf Seite A kann durch Erhöhung der Attraktivität auf Seite B ausgeglichen werden.
- Plattform kann Preiserhöhung für Werbetreibende profitabel halten, auch wenn Nutzerabwanderung einsetzt.
- Lösung: Beidseitiger SSNIP-Test (Kommission 2024 Rn. 93 ff.).

### 4. Relevante Märkte auf Plattformen (Praxis)

| Plattform | Typische Marktdefinition EU-Praxis |
|-----------|-----------------------------------|
| Google Search | Markt für allgemeine Suchdienste; Markt für Online-Suchwerbung |
| App Store | Markt für iOS App-Distribution; kein Android-Substitute |
| Facebook/Meta | Markt für soziale Netzwerke; Markt für Online-Werbung |
| Amazon Marketplace | Markt für Online-Marktplatzdienste; Markt für Onlineeinzelhandel |

### 5. Bewertung der vorgelegten Abgrenzung

- Wurden alle Marktseiten identifiziert?
- Wurde die Entscheidung für getrennte oder integrierte Betrachtung begründet?
- Netzwerkeffekte in der Abgrenzung berücksichtigt?
- DMA-Gatekeeper-Designierung als Referenzpunkt verwendet? (vgl. Skill `dma-und-gatekeeper-markt`)

## Leitentscheidungen Mehrseitige Maerkte

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BKartA, Beschl. v. 01.02.2022 — B6-22/21 (Facebook/Meta) — Plattformmacht; Social-Network-Markt; Nutzerdaten als Wechselkostenfaktor.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `merger-remedies-global`

**Fokus:** Merger Remedies global: Fachmodul für großes Kartellrecht mit BKartA, DG Competition, FTC/DOJ und internationalen Behörden; prüft Divestiture, Behavioural Remedies, Monitoring Trustee und Hold-Separate planen, Evidenz, Fristen, Strategie und Quellen.

# Merger Remedies global

## Fachkern: Merger Remedies global
- **Spezialgegenstand:** Merger Remedies global. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** Art. 101/102 AEUV, VO 1/2003, FKVO, GWB, Vertikal-GVO, DMA/DSA-Schnittstellen, private damages und Behördenpraxis.
- **Entscheidende Weiche:** Markt, Verhalten, Beteiligte, Schwelle, Effekt, Effizienzrechtfertigung, Verfahren, Dawn Raid/Leniency und Schadensersatz getrennt ordnen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Merger Remedies global** im Bereich **Kartellrecht Global Competition Law**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Divestiture, Behavioural Remedies, Monitoring Trustee und Hold-Separate planen

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

## 4. `ministererlaubnis-42-gwb`

**Fokus:** Ministererlaubnis § 42 GWB: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: Art. 101/102 AEUV, GWB §§ 1 und 18-20 und 19a und 32 ff., 33 ff., 35 ff., FKVO, Vertikal-GVO 2022/720, Horizontal-GVO, DMA.

# Ministererlaubnis § 42 GWB

## Fachkern: Ministererlaubnis § 42 GWB
- **Spezialgegenstand:** Ministererlaubnis § 42 GWB. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** Art. 101/102 AEUV, VO 1/2003, FKVO, GWB, Vertikal-GVO, DMA/DSA-Schnittstellen, private damages und Behördenpraxis.
- **Entscheidende Weiche:** Markt, Verhalten, Beteiligte, Schwelle, Effekt, Effizienzrechtfertigung, Verfahren, Dawn Raid/Leniency und Schadensersatz getrennt ordnen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz
Dieser Abschnitt bearbeitet **Fachkern: Ministererlaubnis § 42 GWB** im Bereich **Kartellrecht — Marktabgrenzung und Wettbewerb**. Arbeite praktisch, schnell und verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

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

## 5. `minority-shareholdings-competition`

**Fokus:** Minderheitsbeteiligungen und Competition: Fachmodul für großes Kartellrecht mit BKartA, DG Competition, FTC/DOJ und internationalen Behörden; prüft Kontrolle, Einfluss, Informationsrechte, Common Ownership und Fusionskontrolle prüfen, Evidenz, Fristen, Strategie und Quellen.

# Minderheitsbeteiligungen und Competition

## Fachkern: Minderheitsbeteiligungen und Competition
- **Spezialgegenstand:** Minderheitsbeteiligungen und Competition. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** Art. 101/102 AEUV, VO 1/2003, FKVO, GWB, Vertikal-GVO, DMA/DSA-Schnittstellen, private damages und Behördenpraxis.
- **Entscheidende Weiche:** Markt, Verhalten, Beteiligte, Schwelle, Effekt, Effizienzrechtfertigung, Verfahren, Dawn Raid/Leniency und Schadensersatz getrennt ordnen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Einsatz

Dieser Abschnitt bearbeitet **Fachkern: Minderheitsbeteiligungen und Competition** im Bereich **Kartellrecht Global Competition Law**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.

**Fokus:** Kontrolle, Einfluss, Informationsrechte, Common Ownership und Fusionskontrolle prüfen

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
