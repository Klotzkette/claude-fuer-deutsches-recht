---
name: document-cost
description: "Definiert Dokumentenaufbewahrungs- und -vernichtungsstrategien für Internal Investigation – HGB-Fristen, DSGVO-Löschpflichten, Legal Hold im Internal Investigations Praxis."
---

# Dokumentenaufbewahrung und -vernichtung nach Internal Investigations

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; StPO §§ 53, 97, 102, 110, 136, 137, 152, 153a, BGB §§ 280, 626, BRAO § 43a, GwG, AntiDopG, HinSchG; StPO; HinSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

Dokumentenaufbewahrung unterliegt einem komplexen Spannungsfeld: Handelsrechtliche Aufbewahrungspflichten (§ 257 HGB: 10 Jahre für Buchführung, 6 Jahre für Handelsbriefe, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__257.html)) und steuerrechtliche Pflichten (§ 147 AO) stehen im Konflikt mit dem DSGVO-Löschungsgebot (Art. 17 DSGVO). Im Rahmen einer Internal Investigation wird dieser Konflikt durch den Legal Hold verschärft: Dokumente müssen trotz DSGVO-Löschpflicht aufbewahrt werden, bis die Untersuchung abgeschlossen ist.

## Ziel dieses Skills

Dieser Skill definiert für alle relevanten Dokumentenkategorien klare Aufbewahrungs- und Löschregeln, die sowohl handelsrechtliche Pflichten als auch DSGVO-Anforderungen erfüllen.

## Arbeitsprogramm

### 1. Aufbewahrungspflichten-Übersicht
| Dokumentenart | Frist | Norm |
|---|---|---|
| Buchführungsunterlagen, Jahresabschlüsse | 10 Jahre | § 257 Abs. 4 HGB |
| Handelsbriefe (inkl. E-Mail) | 6 Jahre | § 257 Abs. 4 HGB |
| Steuerunterlagen | 10 Jahre | § 147 AO |
| Lohnunterlagen | 6–10 Jahre | § 147 AO |
| Personalakten (nach Austritt) | 3–5 Jahre | § 195 BGB |
| Verträge | 10 Jahre nach Vertragsende | § 195 BGB |

### 2. Legal Hold – Vorrang vor Löschpflicht
- Art. 17 Abs. 3 lit. e DSGVO: Löschungsrecht entfällt, wenn Verarbeitung zur Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen erforderlich ist.
- Automatische Löschroutinen für Legal-Hold-Dokumente deaktivieren.
- Legal-Hold-Register führen: welche Dokumente stehen unter Hold, seit wann, weshalb?
- Aufhebung des Legal Hold: nach Abschluss aller Verfahren (Untersuchung, Behördenverfahren, Gerichtsverfahren).

### 3. Untersuchungsspezifische Aufbewahrung
- Interviewprotokolle: solange verfahrensrelevant; danach DSGVO-konforme Löschung.
- Forensic Images: bis zur Beendigung aller Verfahren; danach sicheres Löschen (NIST SP 800-88).
- Untersuchungsbericht (Vollbericht): strategische Entscheidung; kann dauerhaft archiviert werden, wenn er keine personenbezogenen Daten enthält; Pseudonymisierung möglich.
- Korrespondenz mit Behörden: 10 Jahre nach Abschluss des Verfahrens.

### 4. DSGVO-konforme Löschung
- Art. 17 DSGVO: Recht auf Löschung muss nach Wegfall des Legal Hold beachtet werden.
- Technisches Löschen: sichere Überschreibung oder Zerstörung von Datenträgern (NIST SP 800-88).
- Löschprotokoll: Dokumentation, was wann wie gelöscht wurde.
- Backups: Löschung muss sich auch auf Backup-Systeme erstrecken (Art. 5 Abs. 1 lit. c DSGVO).

### 5. Aufbewahrung für US-Discovery
- Dokumente unter US-Litigation-Hold: bis zum Abschluss des US-Verfahrens.
- Spoliation-Risiko: vorzeitige Vernichtung kann Sanktionen auslösen (FRCP 37(e)).
- Koordination zwischen deutschem Handelsrecht (Aufbewahrungspflicht) und DSGVO-Löschpflicht und US-Litigation-Hold.

### 6. Aufbewahrung in der Praxis
- Dokumentenmanagement-System: automatische Fristen und Erinnerungen.
- Records-Management-Policy: welche Dokumente werden wie lange aufbewahrt?
- Jährliche Aufbewahrungs-Reviews: abgelaufene Dokumente identifizieren und vernichten.
- Ausnahmen dokumentieren: warum wird ein Dokument über die Standardfrist hinaus aufbewahrt?

### 7. Vernichtungsstrategie nach Untersuchungsabschluss
- Nach Aufhebung des Legal Hold: Überprüfung jedes Dokuments auf verbleibende Aufbewahrungspflichten.
- Priorisierung: personenbezogene Daten zuerst löschen (DSGVO-Sensibilität).
- Keine selektive Vernichtung: alle Kopien (lokal, Cloud, Backup) müssen erfasst sein.
- Zeuge der Vernichtung: Protokollierung der sicheren Löschung durch IT-Abteilung.

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 257 HGB | Aufbewahrungspflichten | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__257.html) |
| § 147 AO | Steuerrechtliche Aufbewahrung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/ao_1977/__147.html) |
| Art. 17 DSGVO | Recht auf Löschung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 5 DSGVO | Datensparsamkeit | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| FRCP Rule 37(e) | Spoliation Sanctions | US Federal Courts |

## Ausgabeformate

- **Aufbewahrungsfristen-Matrix** (Dokumententyp × Norm × Frist)
- **Legal-Hold-Register-Vorlage**
- **Löschprotokoll-Vorlage**
- **Records-Management-Policy-Template**
- **Aufbewahrungskonzept** für Untersuchungsunterlagen

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

