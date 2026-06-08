---
name: data-board
description: "Richtet einen sicheren virtuellen Data Room für externe Counsel, Behörden und US-Discovery ein – Zugang, Privilegierung, Protokollierung im Internal Investigations Praxis."
---

# Sicherer Data Room für Counsel und Behörden

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; StPO §§ 53, 97, 102, 110, 136, 137, 152, 153a, BGB §§ 280, 626, BRAO § 43a, GwG, AntiDopG, HinSchG; StPO; HinSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

Der virtuelle Data Room (VDR) ist das zentrale Instrument für die kontrollierte Weitergabe von Untersuchungsdokumenten an externe Anwälte, Behörden, US-Counsel oder DOJ/SEC. Die Nutzung eines VDR ermöglicht Need-to-know-Zugangskontrolle, Zugriffsprotokollierung und Wasserzeichnung – alles kritisch für Privilegeschutz, DSGVO-Konformität und Beweiskettensicherheit. Die DSGVO verlangt für den Datentransfer in Drittstaaten nach Art. 46 eine geeignete Garantie (SCC, [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679)). Beschlagnahme von VDR-Inhalten ist möglich (§ 94 StPO), wenn der Anbieter oder seine Server in Deutschland oder der EU ansässig sind.

## Ziel dieses Skills

Dieser Skill stellt den technisch und rechtlich korrekten Aufbau und Betrieb eines VDR für Internal Investigations sicher.

## Arbeitsprogramm

### 1. Auswahl des VDR-Anbieters
- EU-basierter Anbieter bevorzugen (kein US-CLOUD-Act-Risiko bei EU-only-Hosting).
- Zertifizierungen: ISO 27001, SOC 2 Type II.
- Funktionen: Wasserzeichen, View-only-Modus (kein Download), granulare Zugangskontrolle, Audit Trail.
- DSGVO-Konformität: Auftragsverarbeitungsvertrag (Art. 28 DSGVO) abschließen.
- Drittstaatentransfer: wenn US-Anwälte oder DOJ Zugang erhalten, SCC oder anderes Schutzinstrument.

### 2. Zugangskontrolle und Benutzergruppen
- Benutzergruppen definieren: Interne Anwälte, Externe Anwälte, Forensiker, Behörden (nur Faktenbericht), US-Counsel.
- Jede Gruppe sieht nur die Dokumente, die für ihre Rolle bestimmt sind.
- Einzelpersonen-Zugang mit Audit Trail: wer hat wann welches Dokument wie lange geöffnet?
- Zeitlich befristeter Zugang: VDR-Zugang nach Abschluss der Untersuchung automatisch deaktivieren.

### 3. Dokumentenstruktur im VDR
- **Privilegiert – nur interne Anwälte**: Vollbericht, Interviewprotokolle, Rechtsgutachten.
- **Faktenbericht**: für Behörden und externe Berater ohne volles Privilege.
- **Forensik-Ergebnisse**: für IT-Forensiker und technische Berater.
- **Board Materials**: für Aufsichtsrat und Audit Committee.
- **Correspondence**: E-Mail-Verkehr mit Behörden.
- Klare Ordnerstruktur mit Versionsverwaltung; keine Dokumente in falsche Ordner hochladen.

### 4. Wasserzeichen und DRM
- Dynamische Wasserzeichen (Benutzername + Datum + IP) auf allen angezeigten Dokumenten.
- View-only-Modus: kein Download, kein Drucken ohne Genehmigung.
- Screenshot-Schutz: technisch schwer vollständig, aber dokumentiert, dass Schutzmaßnahmen ergriffen wurden.
- Print-Tracking: jeder Druckauftrag wird protokolliert.

### 5. Herausgabe an Behörden
- Vor Herausgabe: Privilegierungsanalyse aller Dokumente in dem für die Behörde freigegebenen Ordner.
- Privilege-Log für alle zurückgehaltenen Dokumente.
- Keine Herausgabe von Dokumenten, die Inhouse-Counsel-Kommunikation enthalten (kein EU-Privilege nach Akzo Nobel, aber deutsches Recht schützt ggf. weitere Kategorien).
- Drittstaaten-Herausgabe (DOJ, SEC): DSGVO Art. 49 Abs. 1 lit. e (Strafverfolgungsausnahme) nur eng; vorher Rechtsberatung.

### 6. DSGVO-Konformität
- Personenbezogene Daten im VDR: Verzeichnis der Verarbeitungstätigkeiten (Art. 30 DSGVO) aktualisieren.
- Betroffenenrechte: Auskunftsrecht (Art. 15 DSGVO) – kann Betroffener VDR-Dokumente anfordern? § 29 BDSG ermöglicht Einschränkung während laufender Untersuchung.
- Löschplan: nach Abschluss der Untersuchung VDR-Daten nach DSGVO-Grundsätzen löschen.

### 7. Sicherheitsvorfälle
- VDR-Datenpanne: Art. 33 DSGVO – Meldung binnen 72 Stunden an Datenschutzbehörde.
- Verdacht auf unberechtigten Zugriff: sofortige Sperrung des verdächtigen Accounts; Forensik-Log prüfen.
- Backup: tägliches automatisches Backup; Wiederherstellungsplan dokumentieren.

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| Art. 28 DSGVO | Auftragsverarbeitung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 46 DSGVO | Drittstaatentransfer | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 33 DSGVO | Datenpannenmeldung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| § 94 StPO | Beschlagnahme | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/stpo/__94.html) |
| EuGH C-550/07 P | Akzo Nobel Privilege | [curia.europa.eu](https://curia.europa.eu/juris/document/document.jsf?docid=83458&doclang=DE) |

## Ausgabeformate

- **VDR-Setup-Checkliste** (Anbieterauswahl, Zugangskontrolle, Wasserzeichen)
- **Benutzergruppen-Matrix** (Rolle × Zugangsberechtigung × Dokumente)
- **Ordnerstruktur-Vorlage** für Untersuchungs-VDR
- **Art. 28-DSGVO-Checkliste** für VDR-Anbieter
- **Herausgabe-Protokoll** für Behörden

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

