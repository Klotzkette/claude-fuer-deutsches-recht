# Bias-Audit-Bericht BewerberPilot TalentRank 2.4

**Auftraggeberin:** BewerberPilot Score GmbH, Koeln
**Auftragnehmerin:** FairnessLab GmbH (externe Prüfstelle), Berlin
**Auftragsnummer:** FL-2026-088
**Berichtsstand:** v0.4 vom 20.05.2026 (Zwischenbericht)
**Bearbeitende:** Dr. Hanna Bock-Mertens (Lead), Tom Wilberforce (Statistik), Naomi Wallenstein (Auditmanagement)
**Prüfumfang:** Score-Modell, Ranking-Modell, GPAI-Zusammenfassung (LexiCore Coordinator v3.1)
**Prüfzeitraum:** 06.04.2026 bis 18.05.2026

---

## 1. Auftragsumfang

FairnessLab GmbH wurde mit der unabhängigen Auditpruefung des KI-Systems BewerberPilot TalentRank 2.4 auf mögliche diskriminierende Effekte beauftragt. Prüfkriterium ist die Vereinbarkeit mit Art. 10 KI-VO (Daten-Governance) und Art. 15 KI-VO (Robustheit), erweitert um den Diskriminierungsschutz nach §§ 1, 7 AGG sowie Art. 21 GRCh.

## 2. Methodik

### 2.1 Datensätze

| Datensatz | Umfang | Zweck im Audit | Quelle |
|---|---|---|---|
| D-Train-2024-HR | 48.200 Profile | Bias-Identifikation Trainingsdaten | Anbieterin |
| D-Val-2025-General | 12.000 Profile | Validierungsbias | Anbieterin |
| D-Test-2026-Care | 4.800 Profile | Domänenspezifischer Bias (Klinikbereich) | Anbieterin |
| D-Adverse-Set | 1.200 Profile | Robustheit gegenüber Randfällen | FairnessLab |
| D-Synth-Counterfactual | 5.000 Profile | Kontrafaktische Analyse (Surrogatvariablen) | FairnessLab |

### 2.2 Fairnessmetriken

Verwendete Metriken:

1. **Demographic Parity** (gleiche Selektionsraten je Gruppe)
2. **Equal Opportunity** (gleiche True-Positive-Rate je Gruppe)
3. **Predictive Parity** (gleicher positiver Vorhersagewert je Gruppe)
4. **Calibration within Groups** (Kalibrierung der Score-Verteilung je Gruppe)
5. **Counterfactual Fairness** (Score-Stabilität bei Surrogatwechsel)

### 2.3 Vergleichsgruppen (Surrogat-Identifikation)

Geschlechtsangabe, Religion, Herkunft etc. werden im Modell nicht verarbeitet. Untersuchte **Surrogate**:

- Geschlechtsnahe Vornamen (Distribution nach Statistischem Bundesamt 2020)
- Nicht-lineare Karriereverläufe (Lückenmuster, Wechsel-Quoten, Restart-Phase)
- Sprachmuster (Nicht-Muttersprachlichkeit über stilometrische Marker)
- Pflegeauslandserfahrung (Klinikabschnitte ausserhalb DACH)
- Ausbildungsweg (klassisch akademisch vs. Quereinstieg)

## 3. Ergebnisse

### 3.1 Quantitative Ergebnisse (Kernzahlen)

| Test | Metrik | Ergebnis | Schwelle | Bewertung |
|---|---|---|---|---|
| Geschlechtsnahe Vornamen (Frauen vs. Männer) | Demographic Parity Difference | 0.028 (2.8 Pp.) | <0.05 | Beobachten |
| Geschlechtsnahe Vornamen | Equal Opportunity Difference | 0.024 | <0.05 | Beobachten |
| Nicht-lineare Karriereverläufe (Brüche >18 Monate) | Selektionsrate -7.4 Pp. | -0.074 | <0.05 | Massnahme erforderlich |
| Sprachliche Nicht-Muttersprachlichkeit | Selektionsrate -5.1 Pp. | -0.051 | <0.05 | Massnahme erforderlich |
| Pflegeauslandserfahrung | Selektionsrate -3.2 Pp. | -0.032 | <0.05 | Beobachten |
| Ausbildungsweg Quereinstieg | Selektionsrate -2.7 Pp. | -0.027 | <0.05 | Beobachten |

### 3.2 Qualitative Ergebnisse (Erklaermerkmale)

Die Erklaermerkmale des Score-Modells betonen "Berufserfahrung kontinuierlich", "Abschluss klassisch" und "muttersprachliches Anschreiben". Diese Erklaermerkmale sind **unmittelbar Ursache** der quantitativen Effekte bei nicht-linearen Karriereverläufen und Sprachmustern.

### 3.3 GPAI-Komponente LexiCore Coordinator v3.1

Stichprobenprüfung von 200 Zusammenfassungen (100 deutsch, 100 englisch):

- 84 % der Zusammenfassungen sind sachlich korrekt.
- 11 % enthalten leichte Verzerrungen ("der Kandidat" wo "die Bewerberin" angemessen wäre).
- 5 % enthalten Halluzinationen (z.B. erfundene Studiengänge, falsche Zertifikatsbezeichnungen).
- Quellenanker (Wortlaut-Zitat aus Bewerbungsunterlagen) ist in 73 % der Fälle korrekt zugeordnet.

Eine Modellversion-Spezifikation ("Coordinator v3.1.0" vs. "v3.1.2" vs. "v3.2") wurde von LexiCore Systems Inc. trotz Nachfrage nicht präzisiert. Die Bias-Bewertung der GPAI-Komponente ist daher mit einer Unsicherheit von einer Stufe (vor/nach Modellupdate) zu lesen.

## 4. Massnahmen

### 4.1 Sofortige Massnahmen (vor Pilotstart)

| Massnahme | Verantwortlich | Frist | Erwartete Wirkung |
|---|---|---|---|
| Featuregewichtung "Karriere-Linearität" reduzieren | ML Lead | 21.06.2026 | -50 % Effekt bei nicht-linearen Verläufen |
| Featuregewichtung "Sprachmuster" reduzieren | ML Lead | 21.06.2026 | -50 % Effekt bei Nicht-Muttersprachlichkeit |
| Review-Set um 1.500 Profile mit nicht-linearen Verläufen erweitern | Data Governance | 14.06.2026 | bessere Kalibrierung |
| LexiCore-Modellversion präzisieren | Vendor Management | 07.06.2026 | Nachvollziehbarkeit |
| Quellenanker-Anzeige im UI stärken | UX Team | 30.06.2026 | weniger Halluzinationswirkung |
| Halluzinationen-Limit (Modellguardrails) verschärfen | ML Lead | 30.06.2026 | weniger Falschangaben |
| Recruiter-Schulung mit Bias-Sensibilisierung | Product Compliance | 30.06.2026 | menschliche Korrektur |

### 4.2 Begleitende Massnahmen (Pilot)

| Massnahme | Verantwortlich | Frist | Erwartete Wirkung |
|---|---|---|---|
| Monatlicher Bias-Bericht Pilot | FairnessLab | erstmals 31.08.2026 | Früherkennung |
| Recruiter-Override-Quote im Pilot | Product Compliance | laufend | Indikator Vertrauen/Misstrauen |
| Bewerber-Beschwerden auswerten | Customer Success | laufend | Realfeedback |

## 5. Empfehlung

Der Bias-Auditbericht empfiehlt, die EU-Konformitätserklärung **erst nach Umsetzung** der unter 4.1 genannten sofortigen Massnahmen **und nach Nachweis der Wirkung** in einem Folgeaudit zu unterzeichnen. Eine Pilotfreigabe ist mit den oben genannten begleitenden Massnahmen verantwortbar.

## 6. Restrisiko und Auditgrenze

- Der Auditbericht stützt sich auf die von der Anbieterin bereitgestellten Datensätze. Eine Eigenermittlung von Diskriminierung in der realen Welt ist nicht möglich.
- Die LexiCore-Modellversion ist nicht abschliessend geklärt; ein zukünftiges Modellupdate kann die Befunde ändern.
- Die Surrogate sind überlappend (z.B. korreliert "Sprachmuster" mit "Pflegeauslandserfahrung"). Eine vollständige Entkopplung ist nicht möglich.

## 7. Unterzeichnung

Berlin, 20.05.2026

Dr. Hanna Bock-Mertens
Lead Auditor, FairnessLab GmbH

Naomi Wallenstein
Audit Manager, FairnessLab GmbH

Honorar Zwischenbericht: 18.500 EUR netto. Schlussbericht nach Wirkungsprüfung voraussichtlich 14.07.2026; Honorar: 12.000 EUR netto.

---

## Anmerkung der BewerberPilot Score GmbH (Caspar Lintorf, 23.05.2026)

Die Befunde sind in 10_lueckenliste_massnahmenplan.md übernommen (Nr. 2, 3 und 4). Die Pilotfreigabe wird **nur** ausgesprochen, wenn die Wirkungsprüfung bis 06.07.2026 erfolgreich abgeschlossen ist. Eine "Notpilot"-Variante ist nicht vorgesehen.
