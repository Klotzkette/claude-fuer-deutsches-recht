---
name: mandanten-intake
description: "Erstgespräch oder Telefon-Intake in einer Sozialrechtskanzlei — Stammdaten Mandant erfassen Fristen identifizieren und Akte anlegen. Sozialrechtliches Mandats-Intake. Pruefraster: Geburtsdatum Versichertennummer zustaendige Behoerden Verfahrensstand laufende Fristen Bevollmaechtigungssituation Familien- und Bedarfsgemeinschaft Schwerbehinderten- oder Pflegestatus. Output: Mandatsblatt Vollmacht Datenschutzhinweis Aktenanlage mit sofortigen Fristen markiert. Abgrenzung zu mandat-triage-sozialrecht (Routing) und erstgespraech-mandatsannahme (Gebuehren und GwG-Check)."
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

## Triage — kläre beim allerersten Kontakt

1. Läuft eine Frist (Widerspruch oder Klage) heute oder in den nächsten drei Tagen? — sofort Skill `fristenbuch-sozialrecht`, Eskalation an Anwalt
2. Eilbedarf (Wegfall existenzsichernder Leistungen, Wohnungsverlust, Hilfsmittel lebensnotwendig)? — parallel `eilantrag-sozialrecht`
3. Wirtschaftliche Bedürftigkeit für PKH? — bereits beim Intake Einkommenssituation notieren
4. Bevollmächtigungssituation: liegt bereits eine Vollmacht anderer Beratungsstelle vor? — Konfliktcheck
5. Sozialdaten (§ 67 SGB X): Mandant über vertraulichen Umgang mit Sozialdaten nach Art. 13 DSGVO belehren

## Aktuelle Rechtsprechung

- BSG, Urt. v. 26.04.1994 - 1 RK 16/93, SozR 3-2500 § 13 Nr. 10 Rn. 14 — Der Beratungsanspruch nach § 14 SGB I ist umfassend; die Behörde muss von sich aus auf alle Leistungen hinweisen, die nach der Aktenlage in Betracht kommen (sozialrechtlicher Herstellungsanspruch).
- BSG, Urt. v. 11.03.2004 - B 13 RJ 16/03 R, SozR 4-1200 § 14 Nr. 5 Rn. 19 — Der sozialrechtliche Herstellungsanspruch setzt voraus, dass die Behörde eine ihr obliegende Pflicht verletzt hat und diese Pflichtverletzung kausal für den Nachteil des Versicherten war; der Mandant ist so zu stellen, als hätte die Behörde richtig beraten.
- BSG, Urt. v. 24.01.2013 - B 14 AS 158/12 R, SozR 4-4200 § 37 Nr. 5 Rn. 15 — Die Antragstellung ist im Sozialrecht konstitutiv; ohne wirksamen Antrag entsteht kein Anspruch auf Leistungen, auch wenn ein Bedarf tatsächlich bestand. Das Datum des Eingangs des Antrags ist für die Wirkung entscheidend.
- BSG, Urt. v. 29.11.2018 - B 14 AS 31/17 R, SozR 4-4200 § 36 Nr. 5 Rn. 12 — Sozialdaten (§ 67 SGB X) unterliegen besonderem Schutz; Offenbarungen dürfen nur auf gesetzlicher Grundlage oder mit ausdrücklicher Einwilligung des Betroffenen erfolgen.

## Kommentarliteratur

- Kasseler Kommentar Sozialversicherungsrecht, Mrozynski § 14 SGB I Rn. 1 ff. (Beratungspflicht)
- Hauck/Noftz SGB X, § 67 Rn. 1 ff. (Sozialdatenschutz)
