---
name: legal-hold
description: "Implementiert Legal Hold – Sicherung, Sperrung und Dokumentation aller potenziell relevanten Beweismittel ab Verdachtsmoment im Internal Investigations Praxis."
---

# Legal Hold

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; StPO §§ 53, 97, 102, 110, 136, 137, 152, 153a, BGB §§ 280, 626, BRAO § 43a, GwG, AntiDopG, HinSchG; StPO; HinSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

Der Legal Hold (Beweismittelsicherungsanordnung) ist die erste operative Maßnahme nach Entstehung eines Verdachts. Die Pflicht zur Beweismittelsicherung folgt im deutschen Recht aus der allgemeinen Treuepflicht des Vorstands (§ 93 AktG, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html)) sowie aus der Beweislastumkehr in zivilrechtlichen Schadensersatzverfahren. Werden Beweismittel schuldhaft vernichtet, können Gerichte nach § 286 ZPO nachteilige Schlüsse ziehen; im US-Recht droht „Spoliation" mit Sanktionen nach FRCP 37(e). Strafrechtlich ist Beweismittelvernichtung nach § 274 StGB strafbar ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__274.html)). Datenschutzrechtlich kollidiert der Legal Hold mit dem Löschungsgebot nach Art. 17 DSGVO und § 35 BDSG – dieser Konflikt muss explizit gelöst werden.

## Ziel dieses Skills

Dieser Skill stellt sicher, dass relevante Daten und Dokumente ab dem Moment des Verdachts gesichert, unveränderlich aufbewahrt und so dokumentiert werden, dass die Integrität der Beweismittelkette (Chain of Custody) in jedem Verfahren belegbar ist.

## Arbeitsprogramm

### 1. Trigger-Ereignisse identifizieren
- Wann entstand der Verdacht? Erste interne Meldung, externe Anfrage, Whistleblower-Hinweis (HinSchG § 3, [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hinschg/))?
- Ab wann besteht Verfahrenswahrscheinlichkeit (US: „reasonable anticipation of litigation")?
- Dokumentation des Trigger-Zeitpunkts für spätere Fristberechnung.

### 2. Custodians und Datenquellen identifizieren
- Wer sind die relevanten Personen (Custodians)? Betroffene, Vorgesetzte, Buchhalter, IT-Admins?
- Welche Datenquellen existieren: E-Mail-Server, Sharepoint, Teams/Slack, Mobilgeräte, physische Dokumente, Buchhaltungssysteme, Cloud-Dienste?
- Drittparteien: Steuerberater, Wirtschaftsprüfer, externe Berater mit relevanten Unterlagen.

### 3. Sicherungsmaßnahmen
- IT-Snapshot und E-Mail-Archivierung: Archivierungsregel in Exchange/M365 oder Veritas aktivieren.
- Gelöschte E-Mails: Backup-Tapes, Exchange Recoverable Items (14-Tage-Fenster beachten).
- Automatische Löschroutinen deaktivieren (z. B. 30-Tage-Chat-Löschung in Teams).
- Physische Dokumente: Versiegelung von Büros, Aktenschränken bei Bedarf.
- Mobile Devices: MDM-Fernsperre, Cloud-Backup stoppen (vgl. inv-018-mobile-devices).

### 4. Legal-Hold-Benachrichtigung
- Schriftliche Hold-Notice an alle Custodians: was gesichert wird, warum, welche Handlungen verboten sind (Löschen, Verschieben, Verändern).
- Empfangsbestätigung dokumentieren.
- Keine Selbstjustiz: Mitarbeiter dürfen keine eigenen Selektionen vornehmen.
- Betriebsrat: Mitbestimmung nach § 87 Abs. 1 Nr. 6 BetrVG bei technischer Überwachungseinrichtung prüfen ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html)).

### 5. Datenschutzkonflikt auflösen
- DSGVO Art. 17 Abs. 3 lit. e: Löschpflicht entfällt, soweit Verarbeitung zur Geltendmachung, Ausübung oder Verteidigung von Rechtsansprüchen erforderlich ist.
- § 26 BDSG: Verarbeitung zur Aufdeckung von Straftaten zulässig, wenn tatsächliche Anhaltspunkte vorliegen und Verhältnismäßigkeit gewahrt ist ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html)).
- Verzeichnis der Verarbeitungstätigkeiten (Art. 30 DSGVO) aktualisieren.
- Datenschutzbeauftragter (DSB) einbinden.

### 6. Chain of Custody dokumentieren
- Hash-Werte (SHA-256) aller gesicherten Datensätze zum Sicherungszeitpunkt.
- Wer hat wann Zugriff gehabt – lückenlose Zugriffsprotokollierung.
- Forensik-Images nach ISO/IEC 27037 (Leitfaden für digitale Beweise).

### 7. Abgrenzung Legal Hold vs. Vollsicherung
- Legal Hold ≠ vollständige Forensik: Nur Sicherung, keine Auswertung durch Unternehmen selbst.
- Auswertung erst nach Rechtsgrundlagenklärung (Datenschutz, BetrVG, Strafrecht).

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 93 AktG | Sorgfaltspflicht Vorstand | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/aktg/__93.html) |
| § 274 StGB | Urkundenunterdrückung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__274.html) |
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| Art. 17 DSGVO | Recht auf Löschung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| § 87 BetrVG | Mitbestimmung Überwachung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html) |
| HinSchG | Hinweisgeberschutz 2023 | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/hinschg/) |

## Ausgabeformate

- **Legal-Hold-Notice** (Mustertext für Custodians)
- **Custodian-Liste** mit Bestätigungsmatrix
- **Chain-of-Custody-Protokoll**
- **Datenschutz-Abwägungsmemo** (Art. 17 Abs. 3 lit. e DSGVO vs. Löschpflicht)
- **IT-Anweisungsliste** für Systemadministratoren

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

