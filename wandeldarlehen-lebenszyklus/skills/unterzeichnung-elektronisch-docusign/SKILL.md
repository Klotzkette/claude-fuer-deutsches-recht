---
name: unterzeichnung-elektronisch-docusign
description: "Praxis DocuSign und Adobe Sign fuer Wandeldarlehen: Authentifizierung der Unterzeichner (E-Mail-OTP, SMS-OTP, eID), Pruefspur und Audit Trail, Aufbewahrung zehn Jahre (§ 147 AO), Vorhalten der PDF mit Zertifikatsblock. Versandreihenfolge und Erinnerungsmanagement bei mehrseitiger Unterschriftsrunde."
---

# Elektronische Unterzeichnung (DocuSign / Adobe Sign)

## Zweck

Dieser Skill begleitet die elektronische Unterzeichnung des Wandeldarlehensvertrags über DocuSign oder Adobe Sign. Er stellt sicher, dass die Textform (§ 126b BGB) gewahrt ist, alle Parteien authentifiziert sind und der Audit Trail revisionssicher archiviert wird. Phase B des Lebenszyklus.

## Eingaben

- Unterzeichner (Name, E-Mail-Adresse, Mobilnummer für SMS-OTP)
- Gewünschte Authentifizierungsstufe (E-Mail-OTP, SMS-OTP, QES nach eIDAS)
- Unterzeichnungsreihenfolge (z. B. erst Gesellschaft, dann Gesellschafterinnen, zuletzt Lender)
- Frist für Unterzeichnung (z. B. sieben Bankarbeitstage)
- Archivierungspflicht: zehn Jahre für steuerrelevante Dokumente (§ 147 AO)

## Rechtlicher Rahmen

### Primärnormen
- § 126b BGB (Textform ausreichend; DocuSign erfüllt dies)
- § 126a BGB (Elektronische Form mit QES – höhere Stufe, nicht erforderlich für Wandeldarlehen)
- Art. 26 ff. eIDAS-VO 910/2014 (Anforderungen an elektronische Signaturen)
- § 147 AO (Aufbewahrungspflicht steuerrelevanter Unterlagen zehn Jahre)
- § 257 HGB (Aufbewahrungspflicht handelsrelevanter Unterlagen sechs Jahre)

### Rechtsprechung
- BGH, Urt. v. 24. Januar 2006 – XI ZR 384/03 (E-Mail als Textform nach § 126b BGB)
- OLG Frankfurt, Urt. v. 2. Dezember 2020 – 4 U 269/19 (DocuSign-Signatur als Textform anerkannt)

## Vorgehen

### 1. Dokument vorbereiten
Endgültige PDF des Wandeldarlehensvertrags erstellen (kein DOCX an Unterzeichner senden). Alle Felder ausgefüllt, keine Platzhalter. Unterschriftsfelder positionieren (am Signaturblock).

### 2. DocuSign-Envelope erstellen
Empfängerreihenfolge: 1. Gesellschaft (Geschäftsführerin), 2. Gesellschafterin 1, 3. Gesellschafterin 2, 4. Darlehensgeber. Authentifizierung: SMS-OTP (Standard) oder eID. Ablaufdatum: sieben Bankarbeitstage.

### 3. Authentifizierungsstufen
| Stufe | Methode | Für Wandeldarlehen |
|---|---|---|
| E-Mail-OTP | Code per E-Mail | Ausreichend (Textform § 126b BGB) |
| SMS-OTP | Code per SMS | Empfohlen |
| QES (eIDAS) | Personalausweis-Online-Funktion | Nicht erforderlich, höchste Sicherheit |

### 4. Erinnerungsmanagement
Automatische Erinnerungen nach drei Tagen, nach fünf Tagen. Persönliche Nachfrage nach sieben Tagen. Ablauf-Eskalation an alle Parteien kommunizieren.

### 5. Audit Trail sichern
Nach Abschluss: Certificate of Completion (PDF mit Audit Trail) herunterladen. Zeitstempel, IP-Adressen, Authentifizierungsnachweis, Unterzeichnungschronologie. Archivieren: zehn Jahre revisionssicher (§ 147 AO).

### 6. Archivierung und Verteilung
Jede Partei erhält signiertes PDF per E-Mail (automatisch durch DocuSign). Zusätzlich: Ablage in Kanzleidokumentenmanagementsystem. Backup: mindestens zwei unabhängige Speicherorte.

## Checkliste Unterzeichnungsrunde

| Schritt | Erledigt |
|---|---|
| PDF final, keine Platzhalter | [ ] |
| Alle E-Mail-Adressen geprüft | [ ] |
| Mobilnummern für SMS-OTP vorhanden | [ ] |
| Reihenfolge korrekt konfiguriert | [ ] |
| Ablaufdatum gesetzt | [ ] |
| Erinnerungsintervalle konfiguriert | [ ] |
| Audit Trail archiviert | [ ] |
| Alle Parteien haben signiertes PDF | [ ] |

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Unterzeichner nicht authentifiziert | Identitätszweifel, Anfechtungsrisiko | Nur E-Mail-OTP | SMS-OTP oder QES |
| Kein Audit Trail gespeichert | Beweisnot bei Streit | Audit Trail unvollständig | Vollständiger Trail archiviert |
| Aufbewahrung unter zehn Jahre | § 147 AO-Verstoß | Sechs Jahre | Zehn Jahre |
| Falsches Dokument (Entwurf) unterzeichnet | Streit über Vertragsinhalt | Versionsverwechslung möglich | Nur finale PDF |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/textform-vs-schriftform-vs-notariell/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/beurkundungserfordernis-pruefung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/wandelereignis-eingang/SKILL.md`

## Quellen und Updates

Stand: 05/2026. eIDAS-VO 910/2014; § 147 AO. Bei Änderung eIDAS 2.0 (VO 2024/1183) aktualisieren.
