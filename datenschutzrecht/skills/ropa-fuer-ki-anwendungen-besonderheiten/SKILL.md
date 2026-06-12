---
name: ropa-fuer-ki-anwendungen-besonderheiten
description: "Besonderheiten des Verzeichnisses von Verarbeitungstaetigkeiten bei KI-Anwendungen: Trainingsdatensaetze, Inferenz, RAG, Prompt-Logs, Fine-Tuning, Vector Stores, automatisierte Entscheidungen (Art. 22 DSGVO), Bezug zur KI-Verordnung. Mit Spaltenerweiterungen und Beispielen für LLM-API-Nutzung, Co..."
---

# RoPA für KI-Anwendungen – Besonderheiten

## Zweck

Behandelt die zusaetzlichen Pflichtinhalte und Risiko-Markierungen, die das Verzeichnis von Verarbeitungstaetigkeiten bei KI-Anwendungen abbilden muss. Die DSGVO-Vorgaben in Art. 30 DSGVO werden nicht ersetzt, aber durch KI-spezifische Fragestellungen erweitert: Trainingsdaten, Modellzweck, Vector Stores, Prompt- und Output-Logs, Drittlandtransfer über LLM-Anbieter, automatisierte Entscheidungsfindung nach Art. 22 DSGVO, sowie das Zusammenspiel mit der KI-Verordnung (KI-VO, VO (EU) 2024/1689).

## Wann dieses Modul hilft

- Mandant fuehrt LLM-API (z. B. für interne Assistenten, Chatbots, Code-Generierung) ein.
- HR setzt KI-Tools zur Vorauswahl ein.
- Fachabteilung nutzt RAG-Architektur mit unternehmenseigenen Daten.
- KI-Modelle werden auf personenbezogenen Daten **trainiert oder feinabgestimmt**.
- Vector-Datenbank mit Embeddings personenbezogener Dokumente.
- Prüfung: greift Art. 22 DSGVO (automatisierte Entscheidung)?

## Rechtlicher Rahmen

### DSGVO

- Art. 30 DSGVO bleibt Pflicht; zusaetzliche Inhalte ergeben sich aus DSFA und Transparenzpflichten.
- Art. 22 DSGVO: Verbot ausschließlich automatisierter Einzelentscheidungen mit rechtlicher Wirkung; Ausnahmen Abs. 2; Schutzmassnahmen Abs. 3.
- Art. 35 DSGVO: DSFA-Pflicht bei systematischer und umfassender Bewertung (Profiling), bei neuen Technologien.
- Art. 13/14 DSGVO: Informationspflichten zu Logik, Tragweite und Auswirkungen automatisierter Entscheidungen.
- Art. 32 DSGVO: TOMs an KI-Risiken anpassen (Model Theft, Prompt Injection, Data Leakage).
- Art. 5 DSGVO: Datenminimierung, Speicherbegrenzung – besonders kritisch bei Trainingsdaten.

### KI-Verordnung (VO (EU) 2024/1689)

- Gilt seit 02.08.2024 stufenweise. Verbote ab 02.02.2025, GPAI-Pflichten ab 02.08.2025, Hochrisiko-Systeme ab 02.08.2026 (Annex III).
- HR-KI (Bewerberauswahl, Leistungsbewertung) ist nach Annex III Nr. 4 hochrisikobehaftet.
- Anbieter und Betreiber müssen Dokumentationspflichten (Art. 11, Art. 26 KI-VO) erfuellen – das ergaenzt das DSGVO-RoPA.

### EDSA-Leitlinien und EU-AI-Office

- EDPB Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models (verabschiedet 17.12.2024) – referenzieren, nicht aus Modellwissen zitieren.

## Ablauf / Checkliste

1. **KI-Inventur:** Welche KI-Funktionen sind im Einsatz? Anbieter, Modell, Hostingort.
2. **Datentyp-Mapping:** Sind personenbezogene Daten in Eingaben, Trainingsdaten, Embeddings, Logs oder Outputs?
3. **Rolle prüfen:** Verantwortlicher für welche Daten? Auftragsverarbeiter? Joint Controllership mit KI-Anbieter?
4. **Rechtsgrundlage:** Art. 6 DSGVO; bei besonderen Datenkategorien Art. 9; bei Beschäftigten § 26 BDSG; bei Web-Scraping kritisch zu prüfen.
5. **Drittlandtransfer:** Hosting in USA/UK? DPF-Listing, SCC, TIA.
6. **Art. 22 DSGVO:** Trifft das System Entscheidungen mit rechtlicher Wirkung?
7. **DSFA:** typischerweise Pflicht; in RoPA verlinken.
8. **TOM-Erweiterung:** Prompt-Filterung, Output-Filter, Logging-Limits, Model-Isolation, kein Training auf Mandantendaten.
9. **KI-VO-Bezug:** Falls Hochrisiko, KI-VO-Dokumentation referenzieren.
10. **Loeschfristen:** insbesondere für Prompt-Logs und Vector-Embeddings.

## Mustertext / Template

### Erweiterte RoPA-Zeilen für KI-Anwendungen

| Nr. | KI-Anwendung | Zweck | Rechtsgrundlage | Datenkategorien (Input/Training/Output) | Anbieter / Hosting | Drittland / Garantie | Art. 22 DSGVO einschlaegig? | DSFA-Verweis | KI-VO-Status | Spezifische TOMs | Loeschfristen Logs |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Interner Chat-Assistent (LLM-API) | Mitarbeitersupport, Wissensabfragen | Art. 6 Abs. 1 lit. f DSGVO | Input: Prompts (kann pers. Daten enthalten); Training: keines; Output: Antworten | [Anbieter] US-Region | USA – DPF aktiv (Anhang); zusaetzlich SCC Modul 2 + TIA | nein | DSFA-Ziff. 4 | nicht Hochrisiko | Prompt-Filter, kein Training-Opt-in, Logging 30 Tage | 30 Tage |
| 2 | RAG-System Mandantendokumente | Anwaltliche Recherche | Art. 6 Abs. 1 lit. b und f DSGVO; § 50 BRAO | Input: Mandantenakten (Vector-DB); Output: Zitatpassagen | On-Premises / private Cloud DE | nein | nein | DSFA-Ziff. 5 | nicht Hochrisiko | Mandanten-Mandant-Trennung, Verschluesselung, Berufsgeheimnis-Schutz | Loeschung mit Mandatsende |
| 3 | HR-Vorauswahl Bewerber | Sichtung Bewerbungsdokumente | Art. 6 Abs. 1 lit. b + § 26 BDSG; **menschliche Letztentscheidung** | Input: Bewerbungsunterlagen; Output: Empfehlung | [Anbieter] DE | nein | Ja **mit menschlicher Letztentscheidung** (Art. 22 Abs. 2 lit. b) | DSFA-Ziff. 8 | Hochrisiko (Annex III Nr. 4) | Bias-Tests, Logging, Erklaerbarkeit, Beschwerdeweg | Loeschung 6 Monate nach Absage |
| 4 | Feinabstimmung Modell auf Branchendaten | Verbesserung Produktantworten | Art. 6 Abs. 1 lit. f DSGVO | Training: pseudonymisierte Branchendaten | DE | nein | nein | DSFA-Ziff. 9 | GPAI-Bezug | Pseudonymisierung vor Training, Loeschanfragen-Prozess | Modellversion 2 Jahre |

### Anhang: KI-spezifische TOMs

- Prompt-Klassifikation (PII-Erkennung) vor Versand an LLM.
- Output-Filter gegen Re-Identifizierung.
- Verbot Training-Opt-out durchsetzen (Auswahl entsprechender Tarife).
- Modell-Isolation (kein Cross-Tenant-Training).
- Logging-Limit; rollenbasierter Zugriff auf Logs.
- Vector-Store-Verschluesselung at-rest; Loeschmechanismus für Embeddings.
- Schulung Mitarbeiter zu Prompt-Hygiene.

## Typische Fehler

- "KI-Nutzung" als eine Zeile pauschal eingetragen – fehlende Differenzierung Input / Training / Output.
- Drittlandtransfer über LLM-Anbieter uebersehen, weil "kein Datenexport" gedacht wurde.
- Art. 22 DSGVO uebersehen, weil "der Mensch entscheidet final" behauptet wird, ohne dass dies tatsaechlich nachweisbar ist (Stichwort: rubber stamp).
- DSFA fehlt; nur Art. 30 RoPA gepflegt.
- Prompt-Logs unbegrenzt aufbewahrt.
- KI-VO-Hochrisiko-Status nicht festgehalten.
- Trainingsdaten aus Mandantenakten – Berufsgeheimnis (§ 43a Abs. 2 BRAO, § 203 StGB) verletzt.
- Webscraping-Trainingsdaten ohne Rechtsgrundlage.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 5, 6, 9, 13, 14, 22, 30, 32, 35.
- VO (EU) 2024/1689 (KI-VO / AI Act).
- BDSG, § 26.
- BRAO § 43a Abs. 2; § 50; StGB § 203.
- EDPB Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models (verabschiedet 17.12.2024).
- DSK: Hambacher Erklaerung zur Kuenstlichen Intelligenz (03.04.2019) und Folgepapiere.
