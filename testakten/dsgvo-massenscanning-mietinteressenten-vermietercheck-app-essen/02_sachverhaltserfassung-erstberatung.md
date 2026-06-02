# 02 — Sachverhaltserfassung und Erstberatung

**Aktenzeichen:** DSB-NW-44/26
**Datum:** 14.–15. Januar 2026
**Bearbeiter:** RA Dr. Cornelius Specht, RAin Miriam Beckenbauer

---

## 1. Hintergrund der Mandantin

### 1.1 Unternehmensdarstellung

Die VermieterCheck Solutions GmbH (nachfolgend „VCS") wurde 2019 in Essen gegründet und betreibt eine B2B-SaaS-Plattform, über die Privatvermieter Bonitätsauskünfte über Mietinteressenten einholen können. Zum Stichdatum 14.01.2026 sind 12.400 Privatvermieter angeschlossen. Die Daten der Mietinteressenten werden durch das proprietäre KI-Profiling-Modul „ProspectScore Pro" verarbeitet.

**Verarbeitete Datenkategorien (lt. Erstauskunft GF):**
- Bonitätsauskunft (Schufa-Score, Negativmerkmale)
- Voreigentum / frühere Mietverhältnisse
- Beruf und Einkommenssituation
- Familienstatus und Haushaltsgroesse
- Automatisch ermittelter Risiko-Score (0–100) durch ProspectScore Pro

### 1.2 Technische Systemarchitektur

Das Modul ProspectScore Pro ist als Microservice in einer AWS-Infrastruktur (Frankfurt, eu-central-1) betrieben. Die Entwicklung und der Second-Level-Support erfolgen durch den indischen Dienstleister Sundara Tech Pvt. Ltd. (Bengaluru, Karnataka). Nach Aussage des DevOps-Leiters (Herr Tarkan Bilgic) besteht seit Oktober 2022 ein Datenaustausch mit Sundara Tech ohne abgeschlossene Standarddatenschutzklauseln (SCC) gemaess Art. 46 Abs. 2 lit. c DSGVO.

### 1.3 Betriebsdauer und Verarbeitungsumfang

ProspectScore Pro wurde laut Mandantin im März 2023 in den Produktivbetrieb übernommen. Bis Januar 2026 wurden die personenbezogenen Daten von ca. 142.300 Mietinteressenten verarbeitet. Davon haben schriftlich Einwilligung erteilt: nach Angaben der Mandantin ca. 88.000 Personen; bei den verbleibenden ca. 54.300 Personen fehlen nachweisbare Einwilligungserklärungen.

---

## 2. Chronologie der Ereignisse

| Datum | Ereignis |
|-------|----------|
| Mrz 2023 | Produktivbetrieb ProspectScore Pro startet |
| Okt 2022 | Beginn Datentransfer an Sundara Tech Pvt. Ltd. ohne SCC |
| 08. Nov 2025 | Anonyme HinSchG-Meldung bei interner Meldestelle (unbearbeitet) |
| 17. Nov 2025 | Penetrationstest-Bericht SecureProof GmbH: SQL-Injection CVE-2026-0188 identifiziert |
| 22. Nov 2025 | Erstbestaetigter Datenleak: 142.300 Datensätze exfiltriert |
| 29. Nov 2025 | 72h-Frist gemaess Art. 33 DSGVO läuft ab — keine Meldung bei LDI NRW |
| 03. Dez 2025 | LDI NRW erhält anonymen Hinweis; leitet Vorprüfung ein |
| 12. Dez 2025 | LDI NRW eröffnet formales Aufsichtsverfahren, AZ DSB-NW-44/26 |
| 15. Dez 2025 | Sammelklage VDuG eingereicht: LG Essen 18 Mass 4/26 |
| 22. Dez 2025 | Einzelklage Tannenbruck: LG Essen 4 O 244/26 |
| 07. Jan 2026 | StA Essen eröffnet Ermittlungen § 42 BDSG: 12 Js 11.422/26 |
| 14. Jan 2026 | Mandatsuebernahme durch SBD |

---

## 3. Erstberatungsgespräche (Protokoll)

### 3.1 Gespräch mit GF Schimmelpfennig-Drosthager (14.01.2026, 14:00–17:30 Uhr)

**Themen:**
1. Aufklärung über Zeugnisverweigerungsrecht § 52 StPO im Strafverfahren
2. Belehrung über Schweigerecht § 136 StPO als Beschuldigter
3. Erläuterung der zivilrechtlichen Haftungsrisiken Art. 82 DSGVO
4. Besprechung des Sachverhalts zur privaten Nutzung der Plattform (Wohnungen Essen-Bredeney)

**Ergebnis:** GF Schimmelpfennig-Drosthager bestreitet vorsätzliches Handeln, raumt aber ein, die Plattform zur eigenen Mieterauswahl genutzt zu haben. Die strafrechtliche Beurteilung wird gesondert geprüft (s. Akte 15).

### 3.2 Gespräch mit Datenschutzbeauftragter Frau Hannelore Kessler-Brandt (15.01.2026, 09:00–11:00 Uhr)

**Themen:**
1. Stand der internen DSFA-Dokumentation (Art. 35 DSGVO) — Ergebnis: keine DSFA durchgeführt
2. Verarbeitungsverzeichnis (Art. 30 DSGVO) — Ergebnis: vorhanden, jedoch nicht aktuell
3. Einwilligungsmanagement — Ergebnis: keine dokumentierten Einwilligungserklärungen für ca. 54.300 Betroffene
4. Meldepflicht Art. 33 DSGVO — Ergebnis: Versäumnis bestätigt, keine interne Eskalation erfolgt

### 3.3 Gespräch mit DevOps-Leiter Herr Tarkan Bilgic (15.01.2026, 11:30–13:00 Uhr)

**Themen:**
1. Architektur des Datentransfers zu Sundara Tech
2. API-Authentifizierungsverfahren
3. CVE-2026-0188 — SQL-Injection in der Suchanfrage-Schnittstelle des Scoring-Backends

**Ergebnis:** Seit Oktober 2022 werden Rohdaten der Mietinteressenten für Modelltraining und Support-Zwecke an Sundara Tech übertragen. Ein AVV-Vertrag existiert seit Dezember 2023 (also nachträglich), SCC wurde jedoch nie unterzeichnet.

---

## 4. Einschätzung des Gesamtrisikos

### 4.1 Risikomatrix (Ersteinschätzung)

| Risiko | Eintrittswahrscheinlichkeit | Finanzielles Exposure | Priorität |
|--------|----------------------------|-----------------------|------------|
| LDI-Bussgeld Art. 83 | Hoch (75%) | bis 20.000.000 EUR | KRITISCH |
| VDuG-Sammelklage Art. 82 | Mittel-Hoch (60%) | bis 12.300.000 EUR | KRITISCH |
| Strafverfahren § 42 BDSG | Mittel (45%) | Freiheitsstrafe GF | HOCH |
| Einzelklage Tannenbruck | Mittel (55%) | bis 1.500 EUR + Kosten | MITTEL |
| Drittlandhaftung Art. 44 | Hoch (70%) | Bussgeld (kumulativ) | HOCH |
| Reputationsschaden NDR | Sehr hoch (90%) | Umsatzrückgang | HOCH |

### 4.2 Strategische Empfehlung

Die Kanzlei SBD empfiehlt eine Dreisäulenstrategie:

**Säule 1 — Compliance-Offensive:** Sofortige Nachholung der DSFA, Sanierung des AVV mit Sundara Tech, Nachmeldung der Datenpanne an LDI NRW mit Schadensbegrenzungs-Narrative.

**Säule 2 — Verfahrensverteidigung:** Aktive Vertretung in allen Verfahren mit dem Ziel der Strafminderung (Art. 83 Abs. 2 DSGVO-Milderungsgründe) und Abweisung der Sammelklage mangels individueller Kausalität.

**Säule 3 — Kommunikationsmanagement:** Koordination mit PR-Beratung zur Steuerung der Berichterstattung NDR Panorama; kein öffentliches Eingeständnis ohne anwaltliche Freigabe.

---

## 5. Nächste Schritte

1. DSFA-Kickoff-Workshop mit Datenschutzbeauftragter Kessler-Brandt: 20.01.2026
2. Beauftragung eines unabhängigen Datenschutz-Gutachters für Art. 22 DSGVO: bis 22.01.2026
3. Anwaltsschreiben an LDI NRW zur Fristverlängerung: 17.01.2026
4. Koordination mit Strafverteidiger Dr. Robert Ankermann (StA-Verfahren): 16.01.2026
5. Pruefung Insolvenzrisiko bei Maximalhaftung: Gespräch Steuerberater Münster & Partner

---

## Quellen

- DSGVO Art. 6, 22, 30, 33, 35, 44, 46, 82, 83 — [dejure.org/gesetze/DSGVO](https://dejure.org/gesetze/DSGVO)
- BDSG § 42 — [dejure.org/gesetze/BDSG](https://dejure.org/gesetze/BDSG)
- HinSchG — [dejure.org/gesetze/HinSchG](https://dejure.org/gesetze/HinSchG)
- StPO §§ 52, 136 — [dejure.org/gesetze/StPO](https://dejure.org/gesetze/StPO)
- BGH VI ZR 10/24 (DSGVO-Schadensersatz) — [bundesgerichtshof.de](https://www.bundesgerichtshof.de)
