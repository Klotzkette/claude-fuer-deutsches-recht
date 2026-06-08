---
name: datensatzqualitaet-und-bias-hri
description: "Prüft Datenqualität und Bias bei Robotern, die Menschen erkennen, unterstützen, bewerten oder priorisieren."
---

# Datenqualität und Bias in der Human-Robot Interaction (HRI)

## Fachkern: Datenqualität und Bias in der Human-Robot Interaction (HRI)
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

Roboter, die Menschen erkennen, klassifizieren, priorisieren oder unterstützen (Service-, Pflege-, Sicherheitsrobotik, Liefer- und autonome Mobilität, Recruiting-/Empfangsroboter) sind regelmäßig auf Trainingsdaten angewiesen, deren Qualität und Repräsentativität über Sicherheit und Diskriminierungsfreiheit entscheidet. Art. 10 KI-VO setzt für Hochrisiko-KI verbindliche Anforderungen an Daten-Governance, Repräsentativität, Bias-Behandlung und Annotationsprozesse. Dazu kommen DSGVO, AGG, BFSG und Grundrechte. Dieser Skill liefert Prüfschema, Test-Matrix und Vertragsklauseln.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Anbieter Hochrisiko-KI, Betreiber, Auditor, Aufsichtsbehörde, betroffene Person/Verband.
2. **Funktion:** Personenerkennung, Gestenerkennung, Spracherkennung, Verhaltensprädiktion, Risikoeinschätzung, Triage-Unterstützung.
3. **Trainingsdaten-Quelle:** öffentlich, lizenziert, synthetisch, betriebseigene Aufnahmen, gemischt.
4. **Anlass:** Konformitätsbewertung, Audit Notified Body, Bias-Beschwerde, AGG-Prozess, KI-VO-Inspektion.
5. **Unterlagen:** Data Sheets, Model Cards, Annotationsrichtlinien, Test-/Validierungsberichte, Demographic Statistics.

## Rechtlicher Rahmen

- **KI-VO Art. 10** Daten-Governance bei Hochrisiko-KI: relevante, repräsentative, fehlerfreie und vollständige Trainings-, Validierungs- und Testdaten; Verfahren zur Erkennung möglicher Verzerrungen ("biases") und ihrer Behebung; Art. 10 Abs. 5 erlaubt Verarbeitung besonderer Kategorien (Art. 9 DSGVO) zur Bias-Korrektur unter strikten Voraussetzungen.
- **KI-VO Art. 9** Risikomanagement.
- **KI-VO Art. 15** Genauigkeit, Robustheit, Cybersicherheit.
- **DSGVO** Art. 5, 9, 22, 25, 35.
- **AGG** §§ 1, 2, 7, 19, 20.
- **BFSG** für Verbraucherrobotik.
- **EU-Grundrechtecharta** Art. 21 Diskriminierungsverbot.

## Schritt für Schritt

1. **Use-Case-spezifische Datenanforderungen.** Was muss der Roboter erkennen, in welcher Umgebung, bei welcher Bevölkerung?
2. **Data Sheet** je Datensatz: Quelle, Sammelmethode, Annotatoren, Lizenzen, Verteilungsstatistiken nach geschützten Merkmalen (soweit zulässig erhebbar).
3. **Repräsentativitäts-Audit.** Vergleich Trainings-Demografie vs. Zielpopulation; Gap-Analyse.
4. **Annotationsqualität.** Inter-Annotator-Agreement (Cohen's Kappa), Quality Gates, Konfliktauflösung.
5. **Bias-Tests.** Disparate Performance je Subgruppe (Confusion-Matrix pro Subgruppe; Equal Opportunity / Demographic Parity / Calibration).
6. **Mitigations.** Re-Sampling, Re-Weighting, Data Augmentation, Synthese, Adversarial Debiasing; Folgen für Performance dokumentieren.
7. **Beschäftigtenkontext.** Im Recruiting-/HR-Kontext besondere Vorsicht; AGG-Audit; KI-VO Anhang III Nr. 4.
8. **Dokumentation Art. 10 KI-VO** im technischen Dossier.
9. **Post-Market-Monitoring** Art. 72 KI-VO: kontinuierliche Bias-Überwachung nach Inverkehrbringen.

## Trade-off-Matrix

| Ansatz | Pro | Contra | Empfehlung |
|---|---|---|---|
| Demographic Parity | klare Gleichheit | Performance-Einbuße | bei stark normativer Pflicht (z. B. Recruiting) |
| Equal Opportunity | TPR-Gleichheit | komplizierter | bei sicherheitsbezogenen Anwendungen |
| Synthese fehlende Subgruppen | Coverage erhöhen | Verteilungsverschiebung | nur wenn kontrolliert, mit Trennung Real vs. Synth |
| Subgruppen-Performance nicht messen | "blind" | KI-VO-Verstoß | Messung notwendig (Art. 10 Abs. 2 lit. f) |

## Praxistipps

- **Subgroup-Reports** pro Release.
- **Halbjährliches Real-World-Audit** mit unabhängiger Stelle.
- **Annotations-SLA** mit Sub-Anbietern; Cohen's Kappa min. 0,75.
- **Transparenz an Nutzer** über Performance-Grenzen (Art. 13 KI-VO).
- **Daten-Aufbewahrung** mit Wiederverwendbarkeit für Re-Audit.

## Mustertexte

**Klausel Trainingsdaten-Lieferant (Auszug):**

> Der Lieferant stellt Trainingsdatensätze mit einem detaillierten Data Sheet im Format Anhang B bereit. Der Lieferant garantiert: (a) rechtmäßige Erhebung (DSGVO/Lizenzen), (b) Repräsentativität bezogen auf die in Anlage C definierte Zielpopulation, (c) Annotationsqualität mit Cohen's Kappa nicht unter 0,80, (d) Subgruppen-Statistik nach Alter, Geschlecht, Hautfarbe (soweit zulässig erhebbar) inklusive Performance-Erwartung. Der Lieferant haftet für Vertragsverletzungen, die zu KI-VO-Konformitätsverlust führen, mit pauschalisiertem Schadensersatz von 250.000 EUR je Vorfall; weitergehende Schäden bleiben unberührt.

**Auszug Model Card (Bias-Sektion):**

> Bekannte Limitierungen: Die Erkennungsrate von Personen unter 1,40 m Körpergröße ist mit 92,1 % gegenüber dem Mittelwert von 97,5 % deutlich niedriger. Bei Rollstuhl-Nutzern liegt die Erkennungsrate bei 95,3 %. Empfehlung an den Betreiber: in Umgebungen mit Kindern oder Rollstuhl-Nutzern reduzierte Maximalgeschwindigkeit, redundante Sensorik aktivieren.

## Typische Fehler

- **Trainingsdaten nicht repräsentativ** für reale Bevölkerung – AGG-/KI-VO-Risiko.
- **Keine Subgruppen-Metriken** dokumentiert.
- **Annotationsrichtlinie informell**; keine Inter-Annotator-Tests.
- **Bias-Mitigation einmalig**, ohne Post-Market-Monitoring.
- **Drift** durch Modell-Updates nicht überwacht.

## Querverweise

- `accuracy-robustness-cybersecurity-ai`
- `biometrie-emotion-und-personenerkennung`
- `barrierefreiheit-und-inklusion-robotik`

## Quellen Stand 06/2026

- VO (EU) 2024/1689 (KI-VO), Art. 9, 10, 13, 15, 72.
- DSGVO Art. 5, 9, 22, 35.
- AGG §§ 1, 7, 19, 20.
- EU-Grundrechtecharta Art. 21.
- BFSG.
- NIST AI Risk Management Framework; ISO/IEC TR 24027 Bias.
- Live-Verifikation auf eur-lex.europa.eu, edpb.europa.eu, BAuA, antidiskriminierungsstelle.de; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
