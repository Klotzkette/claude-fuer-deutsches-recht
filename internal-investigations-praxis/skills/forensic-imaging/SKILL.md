---
name: forensic-imaging
description: "Leitet forensische Sicherung von IT-Systemen an – Imaging-Standards, Chain of Custody, Hash-Werte, Zulässigkeit und DSGVO-Konformität im Internal Investigations Praxis."
---

# Forensic Imaging und IT-Datensicherung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; StPO §§ 53, 97, 102, 110, 136, 137, 152, 153a, BGB §§ 280, 626, BRAO § 43a, GwG, AntiDopG, HinSchG; StPO; HinSchG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

Forensic Imaging ist die Erstellung einer bit-genauen Kopie eines digitalen Datenträgers, um Beweise integer zu sichern. Es unterliegt keiner spezifischen deutschen Gesetzesnorm, muss aber DSGVO-konform sein (§ 26 BDSG, Art. 5 Abs. 1 lit. c DSGVO – Datenminimierung) und den technischen Standard ISO/IEC 27037 (Guidelines for identification, collection, acquisition and preservation of digital evidence) einhalten. Bei fehlerhafter Durchführung drohen Beweisverwertungsverbote, und die Integrität des gesamten Ermittlungsergebnisses kann in Frage gestellt werden.

## Ziel dieses Skills

Dieser Skill stellt sicher, dass forensische Sicherungsmaßnahmen technisch korrekt, rechtlich zulässig und beweissicher durchgeführt werden.

## Arbeitsprogramm

### 1. Vorbereitung und Rechtsgrundlage
- DSGVO-Rechtsgrundlage für die Verarbeitung der gesicherten Daten (§ 26 BDSG bei Beschäftigtendaten; Art. 6 Abs. 1 lit. f DSGVO).
- Verhältnismäßigkeit: Ist ein vollständiges Disk-Image erforderlich, oder reicht Selective Collection?
- Betriebsratszustimmung (§ 87 Abs. 1 Nr. 6 BetrVG) bei systematischer Überwachung prüfen.
- Auftragserteilung an externen IT-Forensiker: NDA und Auftragsverarbeitungsvertrag (Art. 28 DSGVO) abschließen.

### 2. Forensic-Imaging-Standard
- **Write-Blocker**: Hardware-Write-Blocker verwenden, um keine Spuren auf dem Original zu hinterlassen.
- **Hash-Werte**: SHA-256-Hash von Originalmedium und Image berechnen; Übereinstimmung dokumentiert Integrität.
- **Image-Format**: EnCase (E01), FTK-Image, DD-Format – dokumentieren, welches Format und welche Software verwendet wurde.
- **Dokumentation**: Gerätebeschreibung (Seriennummer, Hersteller, Modell), Zeitstempel, Name des Forensikers, Zeuge.
- ISO/IEC 27037: Identifikation → Sicherung → Dokumentation → Übergabe.

### 3. Chain of Custody
- Jeder Zugriff auf das Originalmedium und das Image wird protokolliert (wer, wann, warum).
- Physische Sicherung: Image auf verschlüsseltem Datenträger in versiegeltem Behälter.
- Keine Auswertung des Originals – nur des Images.
- Für gerichtliche Verwertung: Chain-of-Custody-Protokoll als Anlage zum Ermittlungsbericht.

### 4. Scope: Vollbild vs. gezielte Sicherung
- Vollständiges Disk-Image: höchste Beweissicherung, aber datenschutzrechtlich eingriffsintensiver.
- Selective Collection (z. B. nur bestimmte Ordner, Dateitypen, Zeiträume): datenschutzfreundlicher, aber Beweislücken möglich.
- Keyword-Suche auf Image: erstes Selektionsmittel; Liste der Keywords dokumentieren und begründen.
- Responsive vs. non-responsive Dokumente trennen (für US-Discovery relevant).

### 5. Besondere Datenträger
- **Mobile Devices**: Chip-off, JTAG oder forensische Software (Cellebrite, Oxygen Forensics) – Passwortschutz und Verschlüsselung beachten (vgl. inv-018-mobile-devices).
- **Cloud-Dienste**: Exportfunktionen nutzen (Google Workspace, M365 eDiscovery); Drittstaatentransfer prüfen.
- **Encrypted Devices**: BitLocker/FileVault – Schlüssel bei IT sichern oder Entschlüsselungshilfe vom Gerätehersteller anfordern.
- **Collaboration Tools**: Teams-Compliance-Center, Slack eDiscovery API.

### 6. DSGVO-Anforderungen bei der Auswertung
- Keine Auswertung privater Kommunikation, wenn private Nutzung erlaubt oder unklar ist.
- Filter für private E-Mails/Dokumente vor Übergabe an Rechtsanwalt einsetzen.
- Drittbetroffene (Kunden, Geschäftspartner): personenbezogene Daten minimieren.
- Löschkonzept: wann werden forensische Images vernichtet?

### 7. Dokumentation für den Bericht
- Forensik-Summary: welche Systeme, welche Zeiträume, welche Keywords, Treffer-Übersicht.
- Nicht verwertbare Dateien dokumentieren (defekte Sektoren, verschlüsselte Bereiche).
- Expert Witness Report für US-Discovery oder Strafverfahren.

## Normenregister

| Norm | Inhalt | Quelle |
|---|---|---|
| § 26 BDSG | Beschäftigtendatenschutz | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/bdsg_2018/__26.html) |
| Art. 5 DSGVO | Datenminimierung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| Art. 28 DSGVO | Auftragsverarbeitung | [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016R0679) |
| § 87 BetrVG | Mitbestimmung Überwachung | [gesetze-im-internet.de](https://www.gesetze-im-internet.de/betrvg/__87.html) |

## Ausgabeformate

- **Forensik-Auftragsvorlage** (Scope, Standards, NDA, Art. 28 DSGVO)
- **Chain-of-Custody-Protokoll**
- **Forensik-Summary-Vorlage**
- **DSGVO-Konformitätsprüfung** für Forensic Imaging
- **Expert Witness Report** (Vorlage für US-Discovery)

Rechtsprechungszitate nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

