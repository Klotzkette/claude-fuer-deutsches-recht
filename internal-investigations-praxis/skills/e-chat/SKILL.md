---
name: e-chat
description: "Strukturiert den E-Mail-Review in Internal Investigations – Keyword-Suche, TAR, Privilege-Log, DSGVO und Verwertbarkeit im Internal Investigations Praxis."
---

# E-Mail-Review in Internal Investigations

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; StPO §§ 53, 97, 102, 110, 136, 137, 152, 153a, BGB §§ 280, 626, BRAO § 43a, GwG, AntiDopG, HinSchG; StPO; HinSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

Die Auswertung von Geschäfts-E-Mails im Rahmen einer Internal Investigation ist zulässig, wenn eine Rechtsgrundlage nach § 26 BDSG oder Art. 6 Abs. 1 lit. f DSGVO vorliegt, Verhältnismäßigkeit gewahrt wird und die Betriebsratsmitbestimmung nach § 87 Abs. 1 Nr. 6 BetrVG beachtet wurde ([gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html)). Bei erlaubter privater E-Mail-Nutzung ist die Rechtslage komplizierter – das BAG hat wiederholt betont, dass der Schutz der privaten Kommunikation auch am Arbeitsplatz gilt. Die fehlerhafte Auswertung führt zu Beweisverwertungsverboten.

## Ziel dieses Skills

Dieser Skill steuert den E-Mail-Review von der Planung bis zur Produktion: Keyword-Entwicklung, Technology-Assisted Review (TAR), Privilege-Screening, DSGVO-Compliance und Verwertbarkeitsanalyse.

## Arbeitsprogramm

### 1. Rechtsgrundlage und Scope
- § 26 BDSG: Verarbeitung zur Aufdeckung von Straftaten – konkrete Verdachtsmomente erforderlich.
- Verhältnismäßigkeit: Zeitraum, Custodians, Postfächer eingrenzen.
- Private E-Mails: Filter einsetzen, wenn private Nutzung erlaubt; keine Auswertung ohne separate Rechtsgrundlage.
- Betriebsrat informieren (§ 80 BetrVG) und ggf. Zustimmung nach § 87 Abs. 1 Nr. 6 BetrVG einholen.

### 2. Keyword-Entwicklung
- Keyword-Liste mit Rechtsanwalt und Sachverständigen entwickeln; dokumentieren, warum jedes Keyword gewählt wurde.
- Iterativer Prozess: Ergebnisse der ersten Runde informieren verfeinerte Keywords.
- Custodian-spezifische Keywords (Spitznamen, interne Codes, Projektnamen).
- Negativliste: Keywords, die ausgeschlossen werden, und Begründung.
- Hit-Rate-Bericht: Anzahl der Treffer pro Keyword → Plausibilitätsprüfung.

### 3. Technology-Assisted Review (TAR)
- TAR/Predictive Coding: Machine-Learning-Klassifizierung von relevanten vs. nicht-relevanten Dokumenten.
- Seed-Set-Qualität: manuell überprüfte Beispieldokumente für das Training des Modells.
- Validation: Statistische Prüfung der Recall- und Precision-Werte (95 % Konfidenzintervall standard).
- Transparenz: TAR-für US-Discovery dokumentierbar; Gegenseite kann Methodik anfechten.

### 4. Privilege-Screening
- Alle Dokumente mit Anwaltskommunikation (To/From Anwalt, „privileged", „attorney-client") separat sichern.
- Privilege-Log erstellen (FRCP Rule 26(b)(5) Standard): Dokument, Datum, Autor, Empfänger, Basis des Privilege.
- Claw-Back-Vereinbarung (FRCP Rule 502(d)): Schutz vor unfreiwilligem Privilege-Waiver bei versehentlicher Produktion.
- Inadvertent Disclosure: sofortiger Claw-Back bei versehentlicher Herausgabe privilegierter Dokumente.

### 5. DSGVO-Konformität bei der Auswertung
- Reviewer dürfen nur Dokumente sehen, für die eine Rechtsgrundlage besteht.
- Drittbetroffene (Kunden, Lieferanten): personenbezogene Daten minimieren, bevor Reviewer Zugriff erhält.
- Drittstaatentransfer bei US-Review-Dienstleister: SCC, Art. 46 DSGVO.
- Review-Plattform: DSGVO-konformer Anbieter oder eigene Infrastructure.

### 6. Verwertbarkeit im Arbeits- und Strafverfahren
- E-Mail aus rechtswidrigem Zugriff (Passwortknacken, Admin-Backdoor ohne Erlaubnis): Beweisverwertungsverbot.
- Ordnungsgemäß aus Unternehmens-Server gesicherte E-Mail: grundsätzlich verwertbar, wenn DSGVO und BetrVG beachtet.
- Metadaten (Zeitstempel, IP-Adresse, E-Mail-Header): wichtige Korroboration; manipulierbar – immer prüfen.
- Hash-Wert der Original-E-Mail für Integritätsnachweis.

### 7. Dokumentation und Reporting
- Review-Log: welcher Reviewer hat wann welche Dokumente gesehen?
- Tag-Set: welche Tags wurden vergeben (relevant, privileged, hot doc, not relevant)?
- Hot-Documents-Liste: bedeutsame Dokumente mit Kurzzusammenfassung für den Anwalt.
- Produktions-Log: welche Dokumente wurden wem wann übergeben?

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| § 87 BetrVG | Mitbestimmung Überwachung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html) |
| Art. 5 DSGVO | Datenminimierung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 46 DSGVO | Drittstaatentransfer SCC | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |

## Ausgabeformate

- **Keyword-Liste-Vorlage** mit Hit-Rate-Spalte
- **TAR-Workflow-Dokumentation**
- **Privilege-Log-Vorlage** (FRCP Rule 26(b)(5))
- **DSGVO-Konformitätsprüfung** für E-Mail-Review
- **Hot-Documents-Zusammenfassung**

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

