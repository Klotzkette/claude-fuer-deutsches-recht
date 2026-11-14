---
name: redteam
description: "Für Red-Team-Analyse in Internal Investigations: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Red-Team-Analyse in Internal Investigations

## Rechtlicher Rahmen

Die Red-Team-Analyse ist keine gesetzlich normierte Pflicht, sondern ein Instrument zur Qualitätssicherung. Sie prüft Untersuchungshypothese, Gegenhypothese, Beweiswert, Verwertbarkeit, Interessenkonflikte und offene Ermittlungsansätze, ohne aus einer unternehmerischen Zweckmäßigkeit eine angebliche höchstrichterliche Einzelpflicht abzuleiten.

## Ziel dieses Skills

Dieser Skill nimmt die gegnerische Perspektive ein: Welche Gegenargumente gibt es zu jedem Tatbestandsmerkmal? Welche Beweise fehlen? Welche Verwertungsprobleme bestehen? Ziel ist nicht die Vernichtung der Untersuchung, sondern ihre Härtung.

## Arbeitsprogramm

### 1. Hypothesenprüfung
- Haupthypothese vs. Alternativhypothese: Welche anderen Erklärungen des Sachverhalts sind möglich?
- Ockhams Rasiermesser: Welche Erklärung ist am einfachsten?
- Confirmation Bias-Check: Wurde aktiv nach widerlegenden Beweisen gesucht, oder nur nach bestätigenden?
- Reihenfolge der Hypothesenprüfung: erst entlastende, dann belastende Indizien gewichten.

### 2. Tatbestandsmerkmale-Prüfung
- Jedes Tatbestandsmerkmal einzeln prüfen: Fehlt ein Element, scheitert die Subsumtion.
- Beispiel Untreue (§ 266 StGB): Vermögensbetreuer (Pflicht?), Pflichtverletzung (rechtwidrig?), Vermögensschaden (messbar?), Vorsatz (direkter oder bedingter?).
- Gegenargumente zu jedem Merkmal dokumentieren – auch wenn sie schwach sind.

### 3. Beweiswürdigung und -lücken
- Welche Beweise fehlen (missing witnesses, deleted documents, encrypted communications)?
- Welche Zeugen wurden nicht befragt, und warum nicht?
- Wurden belastende Dokumente gefunden, aber auch entlastende gesucht?
- Chain of Custody: Ist die Integrität jedes Beweisstücks belegbar?
- Sachverständige: War ein IT-Forensiker nach ISO/IEC 27037-Standard tätig?

### 4. Verwertbarkeitsprobleme
- Beweisverwertungsverbot bei rechtswidrig erlangten Beweisen (DSGVO-Verstoß, fehlende Betriebsratszustimmung, erpresste Aussage).
- Fruit-of-the-poisonous-tree-Doktrin (US-Analogie): Folgebeweise aus einem unverwertbaren Ausgangsbeweis.
- Zeugenpflicht vs. Schweigerecht: Wurde ein Beschuldigter wie ein Zeuge befragt?
- Protokollfehler: Fehlt Datum, Unterschrift, Belehrung – was macht das Protokoll?

### 5. Interessenkollisionen
- Wer hat den Untersuchungsauftrag erteilt, und hat er ein Interesse am Ergebnis?
- Kann das Ergebnis zugunsten des Auftraggebers manipuliert worden sein (Scope-Beschränkung, selektive Interviews)?
- Hat der ermittelnde Anwalt frühere Beziehungen zu Beschuldigten?
- Würde ein US-Monitor oder ein unabhängiger Sachverständiger die Untersuchung als objektiv bewerten?

### 6. Normative Schwachstellen
- Welche Normen wurden im Bericht angewandt, und sind diese zutreffend?
- Wurden neuere Rechtsprechungen berücksichtigt oder ignoriert?
- Werden BGH-Entscheidungen korrekt zitiert, und sind sie frei prüfbar?
- Gibt es widerstreitende Rechtsprechung, die im Bericht nicht erwähnt wird?

### 7. Szenarien-Analyse
- Best Case: Alle Beweise werden verwertet, Subsumtion gelingt, Sanktionen minimal.
- Base Case: Einige Beweise unverwertbar, Kooperation mit Behörden senkt Bußgeld.
- Worst Case: Wesentliche Beweise unverwertbar, Interessenkollision des Ermittlers bekannt, Behörde leitet eigene Untersuchung ein.

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 266 StGB | Untreue | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__266.html) |
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| § 87 BetrVG | Mitbestimmung Überwachung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html) |

## Ausgabeformate

- **Red-Team-Memo** (Gegenhypothesen, Beweislücken, Verwertungsprobleme)
- **Tatbestandsmerkmal-Matrix** (Merkmal × Beweis × Gegenargument)
- **Szenarioanalyse** (Best/Base/Worst Case)
- **Interessenkollisions-Analyse**
- **Qualitätssicherungs-Checkliste** für den Abschlussbericht

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
