---
name: datenminimierung-edge-datensatzqualitaet-bias
description: "Prüft lokale Verarbeitung, Edge/Cloud-Aufteilung, Telemetrie, Anonymisierung, Zugriffskontrolle und Retention im Robotik-Recht."
---

# Datenminimierung in der Edge/Cloud-Architektur

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Geltungsbeginn 02.08.2026 für Hochrisiko (Art. 6 Anhang III), Verbote ab 02.02.2025, Maschinen-VO 20.01.2027, ProdHaftRL-Umsetzung 09.12.2026, KI-VO Art. 73 schwerwiegender Vorfall innerhalb 15 Tagen.
- Tragende Normen verifizieren: EU KI-VO (VO 2024/1689) Art. 6, 8-15, 16, 26, 50, 73, 99, Maschinenverordnung 2023/1230, Produkthaftungs-Richtlinie 2024/2853, BGB §§ 823, 831, ProdHaftG, EU NIS2-RL 2022/2555, EU CRA — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Hersteller, Importeur, Händler, Betreiber, Endnutzer, Marktüberwachungsbehörde (BMAS/BNetzA/BMDV), benannte Stelle (Notified Body), KI-Aufsicht (BNetzA-Stelle).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Konformitätserklärung, technische Dokumentation Anhang IV KI-VO, Risikomanagement-System Art. 9, Datengovernance-Konzept Art. 10, FAT/SAT-Protokoll, Betriebsanleitung, CE-Kennzeichnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Datenminimierung in der Edge/Cloud-Architektur
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

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

