---
name: datenminimierung-edge-datensatzqualitaet-bias
description: "Datenminimierung Edge Datensatzqualitaet Bias: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Datenminimierung Edge Datensatzqualitaet Bias

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Datenminimierung Edge Datensatzqualitaet Bias** im Plugin Robotik-Recht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `datenminimierung-edge-cloud` | Prüft lokale Verarbeitung, Edge/Cloud-Aufteilung, Telemetrie, Anonymisierung, Zugriffskontrolle und Retention. |
| `datensatzqualitaet-und-bias-hri` | Prüft Datenqualität und Bias bei Robotern, die Menschen erkennen, unterstützen, bewerten oder priorisieren. |

## Arbeitsweg

Im Plugin Robotik-Recht gilt für **Datenminimierung Edge Datensatzqualitaet Bias**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `datenminimierung-edge-cloud`

**Fokus:** Prüft lokale Verarbeitung, Edge/Cloud-Aufteilung, Telemetrie, Anonymisierung, Zugriffskontrolle und Retention.


# Datenminimierung in der Edge/Cloud-Architektur

## Fachkern: Datenminimierung in der Edge/Cloud-Architektur
- **Spezialgegenstand:** Datenminimierung in der Edge/Cloud-Architektur wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum geht es konkret

Robotik-Architekturen verteilen Datenverarbeitung typischerweise auf Edge (im Roboter), Fog (lokales Netzwerk, Steuerstand) und Cloud (Telemetrie, KI-Training, Predictive Maintenance). Datenminimierung (Art. 5 Abs. 1 lit. c DSGVO) und Privacy-by-Design (Art. 25 DSGVO) verlangen, dass möglichst wenige Daten möglichst spät und möglichst kurz fließen. Dieser Skill prüft das Datenflussmodell, identifiziert vermeidbare Übertragungen, schlägt Aggregations- und Anonymisierungsschritte vor und liefert Klauseln für Drittanbieter und Mitarbeiter.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller, Betreiber, DSB, CISO, Cloud-Anbieter.
2. **Architektur:** Edge-only, Edge+Cloud, Federated, Cloud-only? Welche Verarbeitungen jeweils?
3. **Datenkategorien:** Sensorrohdaten, Bewegungsmuster, Audio, Video, biometrische Templates, Telemetrie?
4. **Zwecke:** Sicherheit, Wartung, Performance, KI-Training, Marketing?
5. **Anlass:** DSFA, Audit, Aufsichtsanfrage, Architekturentscheidung, Vertragsverhandlung mit Cloud-Anbieter.

## Rechtlicher Rahmen

- **DSGVO** Art. 5 (Grundsätze), Art. 25 (Privacy by Design/Default), Art. 28 (Auftragsverarbeitung), Art. 32 (Sicherheit), Art. 35 (DSFA), Art. 44 ff. (Drittlandtransfer); EDPB-Leitlinien zu Drittlandtransfer und Anonymisierung.
- **KI-VO** Art. 10 Datenqualität; Art. 15 Cybersecurity.
- **CRA** VO (EU) 2024/2847 für vernetzte Komponenten.
- **Data Act** VO (EU) 2023/2854 zu Datenfluss und Cloud-Switching.
- **TTDSG** (in D ab 01.12.2021) bei Endgeräte-Zugriff (z. B. App).
- **BSI Cloud Security Cloud Computing Compliance Criteria Catalogue (C5)**, ISO/IEC 27001/27017/27018.

## Schritt für Schritt

1. **Datenfluss-Diagramm.** Quellen, Verarbeitung, Speicherorte, Übertragungen, Empfänger.
2. **Klassifizierung.** Personenbezogen / besondere Kategorie / nicht-personenbezogen.
3. **Edge-First.** Welche Daten können im Roboter aggregiert/anonymisiert/verworfen werden, bevor sie ihn verlassen?
4. **Zweckbindung.** Pro Datenkategorie konkreten Zweck; nicht Allzweck-Telemetrie.
5. **Rechtsgrundlage.** Art. 6/9 DSGVO; bei Beschäftigten § 26 BDSG bzw. BV.
6. **Anonymisierung vs. Pseudonymisierung.** EDPB-Test: Re-Identifikationsrisiko sachgerecht.
7. **Retention.** Maximale Speicherdauer je Kategorie; automatische Löschroutinen.
8. **Drittlandtransfer.** Art. 44 ff. DSGVO; SCC, TIA, ergänzende Maßnahmen.
9. **AVV** Art. 28 mit Cloud-Anbieter; Sub-Auftragsverarbeiter dokumentieren.
10. **Sicherheit.** Verschlüsselung in transit/at rest, IAM, Logging, Schlüssel-Management.

## Trade-off-Matrix

| Architektur-Entscheidung | Pro | Contra | Empfehlung |
|---|---|---|---|
| Edge-only Inferenz | Datenschutz, Latenz | beschränkte Modelle | für Echtzeit-Steuerung Standard |
| Federated Learning | Daten bleiben lokal | Implementierungsaufwand | bei KI-Modellen mit Personendaten |
| Cloud Training Roh-Daten | beste Performance | DSGVO-/Trade-Secret-Risiko | nur synthetisch oder aggregiert |
| Audio in Cloud | Sprachsteuerung-Komfort | TTDSG, DSGVO | on-device ASR mit Wake-Word-Filter |

## Praxistipps

- **Roh-Video** verlässt den Roboter nie; nur Ereignis-Snippets.
- **Hash + Templates** statt Klartext-IDs.
- **Telemetrie-Schemata** versionieren; "kann ich auf das Feld verzichten?" bei jedem Release.
- **Logs**: Performance ≠ Personen; getrennte Pipelines.
- **AVV-Audit**: TIA aktualisieren bei jedem Cloud-Anbieter-Wechsel.

## Mustertexte

**AVV-Klausel zu Datenminimierung (Auszug):**

> Der Auftragsverarbeiter erhält ausschließlich die in Anlage 1 abschließend aufgeführten Datenkategorien zur Erfüllung der dort genannten Zwecke. Die Verarbeitung erfolgt im Geltungsbereich der DSGVO; ein Drittlandtransfer ist nur mit gesonderter schriftlicher Zustimmung des Verantwortlichen und nach Durchführung eines Transfer Impact Assessment (TIA) zulässig. Roh-Sensordaten verlassen das Edge-Gerät nur in aggregierter Form mit einer Latenz von mindestens 60 Sekunden. Die Speicherdauer beträgt 30 Tage für Telemetrie und 6 Monate für Sicherheitsereignisse.

**Mitarbeiterhinweis Telemetrie (Auszug):**

> Der Cobot überträgt zur Wartung Vibrations-, Strom- und Temperatur-Aggregate pro 5-Minuten-Fenster an den Hersteller-Cloud-Service. Eine Übertragung personenbezogener Daten findet nicht statt; das Modell der Aggregation und die Datenpunkte sind in Anlage 2 abschließend beschrieben. Die Übertragung erfolgt verschlüsselt (TLS 1.3) an einen Server in Frankfurt am Main.

## Typische Fehler

- **"Vorsorgliches" Logging** aller Daten – Datenminimierungs-Verstoß.
- **Cloud-Training auf Roh-Daten** ohne TIA und SCC.
- **Sprachsteuerung in Cloud** ohne TTDSG-Prüfung.
- **Anonymisierungs-Anspruch** ohne Re-ID-Test.
- **Keine Löschroutine** technisch implementiert.

## Querverweise

- `data-act-roboterdaten`
- `beschaeftigtendatenschutz-cobot`
- `cra-produkt-mit-digitalen-elementen`

## Quellen Stand 06/2026

- DSGVO Art. 5, 25, 28, 32, 35, 44 ff.
- BDSG § 26.
- TTDSG.
- VO (EU) 2024/1689 (KI-VO), Art. 10, 15.
- VO (EU) 2024/2847 (CRA).
- VO (EU) 2023/2854 (Data Act).
- BSI C5; ISO/IEC 27001/27017/27018.
- EDPB Guidelines on Anonymisation (in Bearbeitung 2024-2026); EDPB Recommendations 01/2020 Supplementary Measures.
- Live-Verifikation auf eur-lex.europa.eu, edpb.europa.eu, BfDI, bsi.bund.de; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.

## 2. `datensatzqualitaet-und-bias-hri`

**Fokus:** Prüft Datenqualität und Bias bei Robotern, die Menschen erkennen, unterstützen, bewerten oder priorisieren.


# Datenqualität und Bias in der Human-Robot Interaction (HRI)

## Fachkern: Datenqualität und Bias in der Human-Robot Interaction (HRI)
- **Spezialgegenstand:** Datenqualität und Bias in der Human-Robot Interaction (HRI) wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


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
