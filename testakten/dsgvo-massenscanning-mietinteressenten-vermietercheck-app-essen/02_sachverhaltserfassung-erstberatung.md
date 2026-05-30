# 02 — Sachverhaltserfassung und Erstberatung

**Aktenzeichen:** DSB-NW-44/26
**Datum:** 14.–15. Januar 2026
**Bearbeiter:** RA Dr. Cornelius Specht, RAin Miriam Beckenbauer

---

## 1. Hintergrund der Mandantin

### 1.1 Unternehmensdarstellung

Die VermieterCheck Solutions GmbH (nachfolgend „VCS") wurde 2019 in Essen gegruendet und betreibt eine B2B-SaaS-Plattform, ueber die Privatvermieter Bonitaetsauskuenfte ueber Mietinteressenten einholen koennen. Zum Stichdatum 14.01.2026 sind 12.400 Privatvermieter angeschlossen. Die Daten der Mietinteressenten werden durch das proprietaere KI-Profiling-Modul „ProspectScore Pro" verarbeitet.

**Verarbeitete Datenkategorien (lt. Erstauskunft GF):**
- Bonitaetsauskunft (Schufa-Score, Negativmerkmale)
- Voreigentum / fruehere Mietverhaeltnisse
- Beruf und Einkommenssituation
- Familienstatus und Haushaltsgroesse
- Automatisch ermittelter Risiko-Score (0–100) durch ProspectScore Pro

### 1.2 Technische Systemarchitektur

Das Modul ProspectScore Pro ist als Microservice in einer AWS-Infrastruktur (Frankfurt, eu-central-1) betrieben. Die Entwicklung und der Second-Level-Support erfolgen durch den indischen Dienstleister Sundara Tech Pvt. Ltd. (Bengaluru, Karnataka). Nach Aussage des DevOps-Leiters (Herr Tarkan Bilgic) besteht seit Oktober 2022 ein Datenaustausch mit Sundara Tech ohne abgeschlossene Standarddatenschutzklauseln (SCC) gemaess Art. 46 Abs. 2 lit. c DSGVO.

### 1.3 Betriebsdauer und Verarbeitungsumfang

ProspectScore Pro wurde laut Mandantin im Maerz 2023 in den Produktivbetrieb uebernommen. Bis Januar 2026 wurden die personenbezogenen Daten von ca. 142.300 Mietinteressenten verarbeitet. Davon haben schriftlich Einwilligung erteilt: nach Angaben der Mandantin ca. 88.000 Personen; bei den verbleibenden ca. 54.300 Personen fehlen nachweisbare Einwilligungserklaerungen.

---

## 2. Chronologie der Ereignisse

| Datum | Ereignis |
|-------|----------|
| Mrz 2023 | Produktivbetrieb ProspectScore Pro startet |
| Okt 2022 | Beginn Datentransfer an Sundara Tech Pvt. Ltd. ohne SCC |
| 08. Nov 2025 | Anonyme HinSchG-Meldung bei interner Meldestelle (unbearbeitet) |
| 17. Nov 2025 | Penetrationstest-Bericht SecureProof GmbH: SQL-Injection CVE-2026-0188 identifiziert |
| 22. Nov 2025 | Erstbestaetigter Datenleak: 142.300 Datensaetze exfiltriert |
| 29. Nov 2025 | 72h-Frist gemaess Art. 33 DSGVO laeuft ab — keine Meldung bei LDI NRW |
| 03. Dez 2025 | LDI NRW erhaelt anonymen Hinweis; leitet Vorpruefung ein |
| 12. Dez 2025 | LDI NRW eroeffnet formales Aufsichtsverfahren, AZ DSB-NW-44/26 |
| 15. Dez 2025 | Sammelklage VDuG eingereicht: LG Essen 18 Mass 4/26 |
| 22. Dez 2025 | Einzelklage Tannenbruck: LG Essen 4 O 244/26 |
| 07. Jan 2026 | StA Essen eroeffnet Ermittlungen § 42 BDSG: 12 Js 11.422/26 |
| 14. Jan 2026 | Mandatsuebernahme durch SBD |

---

## 3. Erstberatungsgespraeche (Protokoll)

### 3.1 Gespraech mit GF Schimmelpfennig-Drosthager (14.01.2026, 14:00–17:30 Uhr)

**Themen:**
1. Aufklaerung ueber Zeugnisverweigerungsrecht § 52 StPO im Strafverfahren
2. Belehrung ueber Schweigerecht § 136 StPO als Beschuldigter
3. Erlaeuterung der zivilrechtlichen Haftungsrisiken Art. 82 DSGVO
4. Besprechung des Sachverhalts zur privaten Nutzung der Plattform (Wohnungen Essen-Bredeney)

**Ergebnis:** GF Schimmelpfennig-Drosthager bestreitet vorsaetzliches Handeln, raumt aber ein, die Plattform zur eigenen Mieterauswahl genutzt zu haben. Die strafrechtliche Beurteilung wird gesondert geprueft (s. Akte 15).

### 3.2 Gespraech mit Datenschutzbeauftragter Frau Hannelore Kessler-Brandt (15.01.2026, 09:00–11:00 Uhr)

**Themen:**
1. Stand der internen DSFA-Dokumentation (Art. 35 DSGVO) — Ergebnis: keine DSFA durchgefuehrt
2. Verarbeitungsverzeichnis (Art. 30 DSGVO) — Ergebnis: vorhanden, jedoch nicht aktuell
3. Einwilligungsmanagement — Ergebnis: keine dokumentierten Einwilligungserklaerungen fuer ca. 54.300 Betroffene
4. Meldepflicht Art. 33 DSGVO — Ergebnis: Versaeumnis bestaetigt, keine interne Eskalation erfolgt

### 3.3 Gespraech mit DevOps-Leiter Herr Tarkan Bilgic (15.01.2026, 11:30–13:00 Uhr)

**Themen:**
1. Architektur des Datentransfers zu Sundara Tech
2. API-Authentifizierungsverfahren
3. CVE-2026-0188 — SQL-Injection in der Suchanfrage-Schnittstelle des Scoring-Backends

**Ergebnis:** Seit Oktober 2022 werden Rohdaten der Mietinteressenten fuer Modelltraining und Support-Zwecke an Sundara Tech uebertragen. Ein AVV-Vertrag existiert seit Dezember 2023 (also nachtraeglich), SCC wurde jedoch nie unterzeichnet.

---

## 4. Einschaetzung des Gesamtrisikos

### 4.1 Risikomatrix (Ersteinschaetzung)

| Risiko | Eintrittswahrscheinlichkeit | Finanzielles Exposure | Prioritaet |
|--------|----------------------------|-----------------------|------------|
| LDI-Bussgeld Art. 83 | Hoch (75%) | bis 20.000.000 EUR | KRITISCH |
| VDuG-Sammelklage Art. 82 | Mittel-Hoch (60%) | bis 12.300.000 EUR | KRITISCH |
| Strafverfahren § 42 BDSG | Mittel (45%) | Freiheitsstrafe GF | HOCH |
| Einzelklage Tannenbruck | Mittel (55%) | bis 1.500 EUR + Kosten | MITTEL |
| Drittlandhaftung Art. 44 | Hoch (70%) | Bussgeld (kumulativ) | HOCH |
| Reputationsschaden NDR | Sehr hoch (90%) | Umsatzrueckgang | HOCH |

### 4.2 Strategische Empfehlung

Die Kanzlei SBD empfiehlt eine Dreisaeulenstrategie:

**Saeule 1 — Compliance-Offensive:** Sofortige Nachholung der DSFA, Sanierung des AVV mit Sundara Tech, Nachmeldung der Datenpanne an LDI NRW mit Schadensbegrenzungs-Narrative.

**Saeule 2 — Verfahrensverteidigung:** Aktive Vertretung in allen Verfahren mit dem Ziel der Strafminderung (Art. 83 Abs. 2 DSGVO-Milderungsgruende) und Abweisung der Sammelklage mangels individueller Kausalitaet.

**Saeule 3 — Kommunikationsmanagement:** Koordination mit PR-Beratung zur Steuerung der Berichterstattung NDR Panorama; kein oeffentliches Eingestaendnis ohne anwaltliche Freigabe.

---

## 5. Naechste Schritte

1. DSFA-Kickoff-Workshop mit Datenschutzbeauftragter Kessler-Brandt: 20.01.2026
2. Beauftragung eines unabhaengigen Datenschutz-Gutachters fuer Art. 22 DSGVO: bis 22.01.2026
3. Anwaltsschreiben an LDI NRW zur Fristverlaengerung: 17.01.2026
4. Koordination mit Strafverteidiger Dr. Robert Ankermann (StA-Verfahren): 16.01.2026
5. Pruefung Insolvenzrisiko bei Maximalhaftung: Gespräch Steuerberater Muenster & Partner

---

## Quellen

- DSGVO Art. 6, 22, 30, 33, 35, 44, 46, 82, 83 — [dejure.org/gesetze/DSGVO](https://dejure.org/gesetze/DSGVO)
- BDSG § 42 — [dejure.org/gesetze/BDSG](https://dejure.org/gesetze/BDSG)
- HinSchG — [dejure.org/gesetze/HinSchG](https://dejure.org/gesetze/HinSchG)
- StPO §§ 52, 136 — [dejure.org/gesetze/StPO](https://dejure.org/gesetze/StPO)
- BGH VI ZR 10/24 (DSGVO-Schadensersatz) — [bundesgerichtshof.de](https://www.bundesgerichtshof.de)
