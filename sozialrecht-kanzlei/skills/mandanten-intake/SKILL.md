---
name: mandanten-intake
description: Strukturierter Erst-Intake in einer sozialrechtlichen Kanzlei. Erfasst Mandantenstammdaten Geburtsdatum Versichertennummer aktuell zustaendige Behoerden bisheriger Verfahrensstand laufende Fristen Bevollmaechtigungssituation Familien- und Bedarfsgemeinschaftssituation Schwerbehinderten- oder Pflegestatus. Erzeugt Mandatsblatt Vollmacht Datenschutzhinweis Aktenanlage in der Konvention. Markiert sofortige Fristen. Identifiziert Mehrfachmandate (Familie). Geeignet fuer Telefon- oder Praesenz-Intake.
---

# Mandanten-Intake (Sozialrecht)

## Zweck

Den ersten Kontakt strukturieren — alle Daten erfassen die das Mandat braucht; sofortige Fristen erkennen; Akte korrekt anlegen; Vollmacht und Datenschutzhinweis vorbereiten.

## Pflichtfelder

### 1. Stammdaten

- Name Vornamen Geburtsdatum Geburtsname
- Anschrift Telefon Mobil E-Mail
- Familienstand und Bedarfsgemeinschaftsmitglieder (Ehepartner Kinder)
- Geburtsdaten der Bedarfsgemeinschaftsmitglieder
- Staatsangehoerigkeit (Asylbewerberleistungsgesetz Abgrenzung)

### 2. Sozialrechtliche Bezugspunkte

- Versicherten-Nummer GKV
- Renten-Versicherungsnummer
- Schwerbehindertenstatus (GdB Merkzeichen Ausweisnummer)
- Pflegegrad (falls vorhanden)
- Laufende Sozialleistungen mit Höhe und Bewilligungszeitraum
- Zuständige Behörden mit Aktenzeichen

### 3. Aktueller Vorgang

- Worum geht es? (Bescheid Ablehnung Sanktion Rückforderung Erstantrag)
- Datum Bescheid und Zugangsdatum
- Frist (Widerspruchsfrist Klagefrist)
- Bisherige Schritte des Mandanten

### 4. Wirtschaftliche Situation

- Einkommen aktuell
- Vermögen Schonvermögen (für PKH-Prüfung)
- Belege aktuell vorhanden? (Bescheid Lohnabrechnungen Mietvertrag Kontoausuege)

### 5. Vollmachten und Mandatsumfang

- Anwaltsvollmacht Standardumfang
- Untervollmacht für Sozialgericht beA
- Datenschutzhinweis nach Art. 13 DSGVO
- Honorarvereinbarung / PKH-Antrag separat

## Sofort-Prüfraster

- **Frist heute oder in den nächsten drei Tagen?** Sofort eskalieren — Skill `fristenbuch-sozialrecht`.
- **Eilbedürfnis** Wohnungsverlust Wegfall existenzsichernder Leistungen? Skill `eilantrag-sozialrecht`.
- **PKH erforderlich?** Skill `prozesskostenhilfe-antrag`.
- **Akteneinsicht erforderlich?** Skill `akteneinsicht-anfordern`.

## Akte anlegen

- Aktenstruktur nach Plugin-Konvention: `~/.claude/plugins/config/claude-fuer-deutsches-recht/sozialrecht-kanzlei/mandate/<az>-<name>/`
- Unterordner: `01_stammdaten`, `02_bescheide`, `03_korrespondenz`, `04_akten`, `05_schriftsätze`, `06_anlagen`, `07_fristen`, `08_honorar`.

## Vollmachts- und Datenschutzdokumente

- **Anwaltsvollmacht** mit konkretem Mandatsumfang (Vorverfahren und Klage; ggf. Untervollmacht).
- **Datenschutzhinweis** nach Art. 13 DSGVO mit Verweis auf die Verarbeitung von Sozialdaten und Gesundheitsdaten (Art. 9 DSGVO).
- **Schweigepflichtsentbindung** für Behörden / Ärzte / Drittstellen — separat.

## Ausgabe

- Mandatsblatt `01_stammdaten/mandatsblatt.md`.
- Vollmachtsentwurf zur Unterschrift `01_stammdaten/vollmacht.docx`.
- Datenschutzhinweis `01_stammdaten/datenschutz.md`.
- Fristenbuch-Eintrag(e).
- Empfehlung nächster Skills.
