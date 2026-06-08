---
name: ropa-processor-template-ki-anwendungen
description: "Ropa Processor Template KI Anwendungen im Datenschutzrecht: prüft konkret Full English-language template for the Records of, Besonderheiten des Verzeichnisses von, Verzeichnis von Verarbeitungstaetigkeiten in Konzern- und, Auskunft."
---

# Ropa Processor Template KI Anwendungen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachliche Module

## 1. `ropa-en-processor-template`

**Fokus:** Full English-language template for the Records of Processing Activities (RoPA) of the processor under Article 30(2) GDPR. Four mandatory contents, controller list, processing categories, third-country transfers, sub-processor annex. For hosting providers, payroll, IT outsourcing, and cloud vendors with German clients.

### Records of Processing Activities (RoPA) – Processor Template (English)

## Purpose

This skill provides a ready-to-use English-language template for the Records of Processing Activities of a processor pursuant to Article 30(2) GDPR. Unlike the controller record, only four mandatory contents apply. Intended for cloud providers, IT outsourcing companies, payroll bureaus, hosting providers, printing services, external DPOs, and law firms acting in a processor role.

## When you need this skill

- An English-speaking processor builds its first RoPA.
- A multinational client requests a copy of the processor's records.
- Audit (SOC 2, ISO 27001, supervisory authority) requires English-language documentation.
- A law firm performs processor functions for a client (e.g. payroll, document management, eDiscovery hosting).

## Legal framework

Article 30(2) GDPR requires each processor and, where applicable, the processor's representative, to maintain a record containing:

a) the name and contact details of the processor or processors and of each controller on behalf of which the processor is acting, and, where applicable, of the controller's or the processor's representative, and the Data Protection Officer;
b) the categories of processing carried out on behalf of each controller;
c) where applicable, transfers of personal data to a third country or an international organisation, including the identification of that third country or international organisation and, in the case of transfers referred to in the second subparagraph of Article 49(1), the documentation of suitable safeguards;
d) where possible, a general description of the technical and organisational measures referred to in Article 32(1) GDPR.

One row per controller. Multiple processing categories can be grouped where TOMs are identical.

## / Checklist

1. Cover sheet with processor details.
2. Maintain a controller list (each customer relationship).
3. Per controller, describe processing categories (not individual activities).
4. Identify third-country transfers and the applicable transfer instrument.
5. Reference a TOM annex; do not repeat Art. 32 wording.
6. Maintain a separate sub-processor annex (Art. 28(4) GDPR) showing transfer chains.
7. Add versioning footer.

## Template

### Cover Sheet

```
Processor: [Company name]
Address: [...]
Representative (Art. 27): [if applicable]
Data Protection Officer: [Name, contact]
Created: [date]
Last amended: [date]
Version: [v1.0]
```

### Table (mandatory columns)

| No. | Controller | Categories of processing | Third country / safeguards | TOM reference |
|---|---|---|---|---|
| 1 | [Client A GmbH] | Hosting of accounting software, backups, patch management | none | TOM Annex A |
| 2 | [Client B AG] | Payroll processing, wage tax filings, social security filings | none | TOM Annex A |
| 3 | [Client C KG] | Email hosting, spam filtering | USA – sub-processor (SCCs + TIA in Annex B) | TOM Annex A |
| 4 | [Client D e.V.] | Membership administration, direct debit collection | none | TOM Annex A |

### Sub-processor annex

| Sub-processor | Location | Service | Transfer tool |
|---|---|---|---|
| [Hyperscaler Cloud] | USA | Infrastructure as a Service | EU-US DPF (active listing on file in Annex B) |
| [Email filter service] | Ireland | Spam filtering | EU/EEA – no transfer safeguards required |
| [Backup provider] | Germany | Offsite backup | EU/EEA – no transfer safeguards required |

### Versioning footer

```
Version 1.0 – Initial draft – [date, author]
Version 1.1 – [change] – [date, author]
```

## Common mistakes

- Confusing "categories of processing" (processor view) with "purpose" (controller responsibility).
- Omitting sub-processors that introduce third-country transfers.
- Maintaining redundant TOM descriptions per controller where the operational baseline is uniform.
- Missing the controller's DPO contact.
- Copying the full text of Article 32 into the TOM column instead of referencing a TOM annex.
- Overlooking second-tier sub-processor transfers (e.g. when a sub-processor uses a sub-sub-processor in the USA).

## Cross-references

- `ropa-art-30-dsgvo-grundlagen` for the German framework.
- `ropa-en-controller-template` for the controller counterpart.
- `dpa-en-template-controller-processor` for English DPA template.
- `dpa-en-tom-annex-template` for the TOM annex.
- `tia-en-template-full` for the English Transfer Impact Assessment.

## Sources as of 06/2026

- Regulation (EU) 2016/679 (GDPR), Article 30(2), Article 28.
- DSK Short Paper No. 1 "Records of Processing Activities" (Status 17 December 2018).
- DSK Short Paper No. 13 "Processor Agreements" (Status 16 January 2018).
- EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR (adopted 7 July 2021).

## 2. `ropa-für-ki-anwendungen-besonderheiten`

**Fokus:** Besonderheiten des Verzeichnisses von Verarbeitungstaetigkeiten bei KI-Anwendungen: Trainingsdatensaetze, Inferenz, RAG, Prompt-Logs, Fine-Tuning, Vector Stores, automatisierte Entscheidungen (Art. 22 DSGVO), Bezug zur KI-Verordnung. Mit Spaltenerweiterungen und Beispielen für LLM-API-Nutzung, Co-Pilot-Tools und KI-gestuetzte Bewerberauswahl.

### RoPA für KI-Anwendungen – Besonderheiten

## Zweck

Dieser Skill behandelt die zusaetzlichen Pflichtinhalte und Risiko-Markierungen, die das Verzeichnis von Verarbeitungstaetigkeiten bei KI-Anwendungen abbilden muss. Die DSGVO-Vorgaben in Art. 30 DSGVO werden nicht ersetzt, aber durch KI-spezifische Fragestellungen erweitert: Trainingsdaten, Modellzweck, Vector Stores, Prompt- und Output-Logs, Drittlandtransfer ueber LLM-Anbieter, automatisierte Entscheidungsfindung nach Art. 22 DSGVO, sowie das Zusammenspiel mit der KI-Verordnung (KI-VO, VO (EU) 2024/1689).

## Wann dieses Modul hilft

- Mandant fuehrt LLM-API (z. B. für interne Assistenten, Chatbots, Code-Generierung) ein.
- HR setzt KI-Tools zur Vorauswahl ein.
- Fachabteilung nutzt RAG-Architektur mit unternehmenseigenen Daten.
- KI-Modelle werden auf personenbezogenen Daten **trainiert oder feinabgestimmt**.
- Vector-Datenbank mit Embeddings personenbezogener Dokumente.
- Pruefung: greift Art. 22 DSGVO (automatisierte Entscheidung)?

## Rechtlicher Rahmen

### DSGVO

- Art. 30 DSGVO bleibt Pflicht; zusaetzliche Inhalte ergeben sich aus DSFA und Transparenzpflichten.
- Art. 22 DSGVO: Verbot ausschliesslich automatisierter Einzelentscheidungen mit rechtlicher Wirkung; Ausnahmen Abs. 2; Schutzmassnahmen Abs. 3.
- Art. 35 DSGVO: DSFA-Pflicht bei systematischer und umfassender Bewertung (Profiling), bei neuen Technologien.
- Art. 13/14 DSGVO: Informationspflichten zu Logik, Tragweite und Auswirkungen automatisierter Entscheidungen.
- Art. 32 DSGVO: TOMs an KI-Risiken anpassen (Model Theft, Prompt Injection, Data Leakage).
- Art. 5 DSGVO: Datenminimierung, Speicherbegrenzung – besonders kritisch bei Trainingsdaten.

### KI-Verordnung (VO (EU) 2024/1689)

- Gilt seit 02.08.2024 stufenweise. Verbote ab 02.02.2025, GPAI-Pflichten ab 02.08.2025, Hochrisiko-Systeme ab 02.08.2026 (Annex III).
- HR-KI (Bewerberauswahl, Leistungsbewertung) ist nach Annex III Nr. 4 hochrisikobehaftet.
- Anbieter und Betreiber muessen Dokumentationspflichten (Art. 11, Art. 26 KI-VO) erfuellen – das ergaenzt das DSGVO-RoPA.

### EDSA-Leitlinien und EU-AI-Office

- EDPB Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models (verabschiedet 17.12.2024) – referenzieren, nicht aus Modellwissen zitieren.

## Ablauf / Checkliste

1. **KI-Inventur:** Welche KI-Funktionen sind im Einsatz? Anbieter, Modell, Hostingort.
2. **Datentyp-Mapping:** Sind personenbezogene Daten in Eingaben, Trainingsdaten, Embeddings, Logs oder Outputs?
3. **Rolle pruefen:** Verantwortlicher für welche Daten? Auftragsverarbeiter? Joint Controllership mit KI-Anbieter?
4. **Rechtsgrundlage:** Art. 6 DSGVO; bei besonderen Datenkategorien Art. 9; bei Beschaeftigten § 26 BDSG; bei Web-Scraping kritisch zu pruefen.
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
- Drittlandtransfer ueber LLM-Anbieter uebersehen, weil "kein Datenexport" gedacht wurde.
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

## 3. `ropa-konzernumlauf-und-multi-entity`

**Fokus:** Verzeichnis von Verarbeitungstaetigkeiten in Konzern- und Multi-Entity-Strukturen. Konzernklausel-Mythos, Rollenverteilung (Verantwortlicher gemeinsam Verantwortlich Auftragsverarbeiter), zentrale vs. dezentrale Pflege, Intercompany-Datenfluesse, BCR-Verweis. Mit Strukturskizze und Vorlage für Master-RoPA und Entity-Anhaenge.

### RoPA im Konzern und in Multi-Entity-Strukturen

## Wann dieses Modul hilft

- Konzernweiter RoPA-Roll-out (Mutter- und Tochtergesellschaften).
- Shared-Service-Center für HR, IT, Buchhaltung, Recht (typischerweise Processor-Konstellation).
- Intercompany Data Transfer Agreements (IDTA, hier deutscher Begriff: konzerninterne Datentransfer-Vereinbarung).
- Binding Corporate Rules (BCR) im Aufbau.
- M&A-Due-Diligence (Datenschutz-DD).
- Pruefung durch Aufsichtsbehoerde mit Bezug zu mehreren Konzernunternehmen.

## Rechtlicher Rahmen

### Kein Konzernprivileg

Die DSGVO kennt **kein Konzernprivileg** (Erwaegungsgrund 48 erlaubt nur ein **berechtigtes Interesse** an konzerninterner Datenuebermittlung im Rahmen von Art. 6 Abs. 1 lit. f DSGVO; keine pauschale Freistellung). Jede Datenuebermittlung zwischen rechtlich selbststaendigen Konzernunternehmen ist eine Uebermittlung im Sinne der DSGVO und braucht eine Rechtsgrundlage.

### Rollenverteilung

- **Verantwortlicher (Art. 4 Nr. 7 DSGVO):** entscheidet ueber Zwecke und Mittel.
- **Gemeinsam Verantwortliche (Art. 26 DSGVO):** gemeinsame Festlegung; Joint-Controllership-Vereinbarung erforderlich.
- **Auftragsverarbeiter (Art. 28 DSGVO):** im Auftrag, weisungsgebunden; AVV erforderlich.

Konzerninterne Shared-Service-Center sind typischerweise Auftragsverarbeiter (z. B. IT-Service-GmbH). HR-Daten an Mutter zur Karriereplanung koennen Joint-Controllership begruenden.

### Drittlandtransfer im Konzern

Konzerninterne Uebermittlungen in Drittlaender unterliegen Art. 44 ff. DSGVO. Loesungen:

- BCR (Art. 47 DSGVO) – aufwendig, aber genehmigungsfaehig.
- SCC (Beschluss (EU) 2021/914) zwischen den konzernzugehoerigen Stellen.
- Angemessenheitsbeschluss (z. B. EU-US DPF für US-Tochter im DPF).

### EDSA-Leitlinien

EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR (verabschiedet 07.07.2021) – grundlegend zur Rollenklaerung.

## Ablauf / Checkliste

1. **Strukturkarte:** Liste aller Konzerngesellschaften mit Sitz, Rechtsform, taetigem Personal, Datenkategorien.
2. **Rollen-Mapping:** Wer ist für welchen Datenfluss Controller, Joint Controller oder Processor?
3. **Master-RoPA:** zentrales Dokument für gruppenuebergreifende Prozesse (Konzern-HR, Konzern-CRM, Konzern-Compliance).
4. **Entity-Anhaenge:** pro Gesellschaft eigene Tabelle mit Spezifika.
5. **Intercompany-Vertraege:** AVV oder Joint-Controllership-Vereinbarung verlinken.
6. **BCR-Status:** wenn vorhanden, in jedem Entity-RoPA als Garantie referenzieren; sonst SCC.
7. **Pflegemodell:** zentraler Datenschutzkoordinator oder dezentrale DSB?

## Mustertext / Template

### Master-RoPA-Deckblatt

```
Konzern: [Mutter AG]
Konzernweite DSB: [Name, Kontakt]
Geltungsbereich: [Liste der Tochtergesellschaften, EU/EWR + Drittlaender]
Konzerninterne Garantie: [BCR genehmigt YYYY-MM-DD durch Lead-Behörde XY] oder [SCC-Rahmenvertrag YYYY]
Erstellt: [Datum]
Letzte Aenderung: [Datum]
Version: [v1.0]
```

### Master-Tabelle (gruppenuebergreifende Prozesse)

| Nr. | Prozess | Verantwortlicher | Gemeinsam Verantwortliche | Auftragsverarbeiter im Konzern | Datenfluss | Garantie |
|---|---|---|---|---|---|---|
| 1 | Konzern-Identity-Provider | Mutter AG (DE) | – | IT-Service-GmbH (DE) | Mitarbeiter aller Entities -> IdP | AVV |
| 2 | Konzernweite Compliance-Hotline | Mutter AG (DE) und Tochter Inc. (US) | Joint-Controllership Vereinbarung vom YYYY | Hotline-Provider (Dritter) | Hinweise aus allen Standorten | SCC + TIA; US-Tochter im EU-US DPF |
| 3 | Talent-Pool / Karriereplattform | Mutter AG | Toechter EU/EWR | – | HR-Daten weltweit | BCR (genehmigt YYYY) |
| 4 | Konzern-CRM | Mutter AG | – | Vertriebs-GmbH (DE) | Kundendaten EU -> Konzernzentrale | AVV |

### Entity-Anhang (pro Tochter)

```
Tochter: [Name, Sitz, Rechtsform]
Lokal Verantwortlicher: [...]
Lokal DSB: [...]
Lokale Aufsichtsbehoerde: [...]
Lokale Prozesse: [Tabelle entsprechend Controller-Vorlage]
Bezug zu Master-RoPA: [Prozessnummern oben]
```

### Datenflussdiagramm (textuell)

```
DE (Mutter) <--AVV--> IT-Service-GmbH (DE)
DE (Mutter) <--Joint Controllership--> US (Tochter im DPF)
DE (Mutter) <--BCR--> IN (Tochter)
DE (Mutter) <--SCC--> BR (Tochter, kein Angemessenheitsbeschluss)
```

## Typische Fehler

- "Konzernprivileg" angenommen; keine eigene Rechtsgrundlage dokumentiert.
- Shared-Service-Center als Controller behandelt, obwohl weisungsgebunden -> Joint Controllership statt AVV unzutreffend gewaehlt.
- BCR vorhanden, aber im RoPA nicht referenziert.
- Intercompany-Datenfluesse nicht erfasst; nur lokale Prozesse dokumentiert.
- US-Konzerntochter als "EU-nahe" behandelt – DPF-Status nicht geprueft.
- M&A: Datenschutz-DD ohne Sichtung des RoPA der Target-Gesellschaft.
- Doppelte Pflege: Master-RoPA und Entity-RoPA divergieren; kein Versionsabgleich.

## Quellen Stand 06/2026

- VO (EU) 2016/679 (DSGVO), Art. 4 Nr. 7, Art. 26, Art. 28, Art. 30, Art. 44–47, Erwaegungsgrund 48.
- Durchfuehrungsbeschluss (EU) 2021/914 der Kommission vom 04.06.2021 (SCC).
- EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR (verabschiedet 07.07.2021).
- EDPB Working Document on Approval Procedure for BCR (zuletzt aktualisiert 2022).
- DSK-Kurzpapier Nr. 1 "Verzeichnis von Verarbeitungstaetigkeiten" (Stand 17.12.2018).

## 4. `spezial-auskunft-behoerden-gericht-und-registerweg`

**Fokus:** Auskunft: Behörden-, Gerichts- oder Registerweg im Plugin datenschutzrecht.

### Auskunft: Behörden-, Gerichts- oder Registerweg

## Spezialwissen: Auskunft: Behörden-, Gerichts- oder Registerweg
- **Normen-/Quellenanker:** DSGVO, BDSG, TDDDG, PIA, DPIA, AVV, Art. 15, Art. 33, Art. 44, US, DPF, SCC.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Auskunft DSGVO** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Auskunftsanspruch Art. 15 DSGVO — Behörden- und Gerichtswege
- **Erstantrag** direkt an Verantwortlichen — Frist 1 Monat (Art. 12 Abs. 3 DSGVO), Verlängerung um 2 Monate bei Komplexität.
- **Datenkopie** Art. 15 Abs. 3 DSGVO; erste Kopie kostenlos, weitere mit Verwaltungskosten zulässig (EuGH C-307/22 zur Reichweite).
- **Identitätsprüfung** Art. 12 Abs. 6 — bei begründeten Zweifeln; nicht überzogen handhaben.
- **Verweigerung:**
 - **Art. 12 Abs. 5 lit. b DSGVO:** offenkundig missbräuchlich.
 - **§ 34 BDSG:** Ausnahmen (z. B. Datenverbleib bei Berufsgeheimnisträgern, Strafverfolgung).
- **Beschwerdewege:**
 - **Beschwerde Aufsicht Art. 77 DSGVO:** zuständige Landesdatenschutzbehörde oder BfDI.
 - **Klage gegen Verantwortlichen Art. 79 DSGVO:** ZG mit Streitwert-Zuständigkeit; ggf. § 29c ZPO Verbraucher.
 - **Klage gegen Aufsicht Art. 78 DSGVO:** VG-Klage.
- **EuGH-Rechtsprechung:** C-487/21 (Österreichische Datenschutzbehörde): Auskunftsanspruch erstreckt sich auf konkrete Empfänger (nicht nur Empfängerkategorien), wenn diese identifiziert werden können.

## Praxis-Tipp
Bei unvollständiger Auskunft frühzeitig nachhaken und konkret benennen, was fehlt (Empfänger, Speicherdauer, Herkunft, Logik bei automatisierten Entscheidungen). Pauschale Beschwerde "Auskunft unvollständig" wird oft zurückgewiesen — präzise Nachforderung erhöht Erfolgsaussichten.

## 5. `spezial-bdsg-tatbestand-beweis-und-belege`

**Fokus:** Bdsg: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin datenschutzrecht.

### Bdsg: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Spezialwissen: Bdsg: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Normen-/Quellenanker:** DSGVO, BDSG, TDDDG, PIA, DPIA, AVV, Art. 15, Art. 33, Art. 44, US, DPF, SCC.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **BDSG** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## BDSG-relevante Tatbestände und Beweisfragen
- **§ 26 BDSG (Beschäftigtendaten):** Erforderlichkeit für Begründung/Durchführung/Beendigung Arbeitsverhältnis; Beweislast Arbeitgeber. Bei Aufdeckung von Straftaten Abs. 1 S. 2 — dokumentierter Verdacht erforderlich.
- **§ 22 BDSG (besondere Datenkategorien):** Verarbeitung Art. 9 DSGVO-Daten (Gesundheit, Religion etc.) nur mit zusätzlicher Rechtsgrundlage des BDSG; nationale Erlaubnis-Norm + DSGVO-Rechtsgrundlage erforderlich.
- **§ 24 BDSG (Verarbeitung zu anderen Zwecken):** Zweckänderung bei nichtöffentlichen Stellen — Abwägung Interessen.
- **§ 38 BDSG (DSB-Bestellungspflicht):** ab 20 Personen mit ständiger Personendatenverarbeitung; Verstoß: § 43 BDSG Bußgeld.
- **Beweismittel:** Verzeichnis Art. 30 DSGVO, AVV, Schulungsnachweise, Logfiles, E-Mail-Verkehr, Betriebsvereinbarungen.

## Praxis-Tipp
Bei Verstoß gegen § 26 BDSG ist die zentrale Beweisfrage immer: "Erforderlich für was genau?" Pauschale Verweise auf "Zwecke des Arbeitsverhältnisses" tragen nicht — der konkrete Anlass und die Geeignetheit der Mittel müssen dokumentierbar sein. BAG 27.07.2017, 2 AZR 681/16 zur Verwertbarkeit von Keylogger-Daten als Leitorientierung.

