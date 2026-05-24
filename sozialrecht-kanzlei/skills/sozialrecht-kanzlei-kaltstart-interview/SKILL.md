---
name: sozialrecht-kanzlei-kaltstart-interview
description: "Kaltstart-Interview fuer die sozialrechtliche Kanzlei. Erfragt Schwerpunktbereiche (Buergergeld SGB II / SGB IX Schwerbehinderung / SGB V Krankenversicherung / SGB XI Pflege / Asylbewerberleistungsgesetz) zustaendige Sozialgerichte typische Mandate (Bescheid-Widerspruch / Klage / Eilrechtsschutz) Prozesskostenhilfe-Quote Sekretariatslast Aktenstruktur-Konvention Versandwege (beA / Post / ePostfach Behoerde) Eskalation. Schreibt Profil nach ~/.claude/plugins/config/claude-fuer-deutsches-recht/sozialrecht-kanzlei/CLAUDE.md. Mit --redo neu interviewen."
---

# /sozialrecht-kanzlei:sozialrecht-kanzlei-kaltstart-interview

## Ablauf

1. Konfigurationsdatei `~/.claude/plugins/config/claude-fuer-deutsches-recht/sozialrecht-kanzlei/CLAUDE.md` prüfen.
2. Falls vorhanden ohne Platzhalter: bestätigen.
3. Andernfalls Interview unten durchführen.
4. Datei schreiben.
5. Zusammenfassung anzeigen mit nächsten Skill-Empfehlungen.

## Kaltstart-Interview

### 1. Rolle und Kanzlei

- **Rolle:** Fachanwalt für Sozialrecht / Rechtsanwalt mit sozialrechtlichem Schwerpunkt / Syndikus eines Sozialverbands / Beratungsstelle?
- **Kanzleigroesse:** Einzelkanzlei / Sozietät / mittelstaendisch / Verband
- **Sekretariat:** ja / nein (entscheidet ob Sekretariats-Workflows aktiv)
- **Mandantenklientel:** Privatpersonen / Verbände / Eingliederungsträger / gemischt

### 2. Schwerpunktbereiche

- **SGB II** Bürgergeld (Regelbedarfe Kosten der Unterkunft Sanktionen): ja / nein
- **SGB III** Arbeitsförderung Arbeitslosengeld I: ja / nein
- **SGB V** Krankenversicherung (Leistungsanträge Krankengeld): ja / nein
- **SGB VI** Rente: ja / nein
- **SGB VII** Unfallversicherung BG: ja / nein
- **SGB VIII** Kinder- und Jugendhilfe (Hilfe zur Erziehung Schulbegleitung): ja / nein
- **SGB IX** Rehabilitation und Teilhabe (Schwerbehinderung Hilfsmittel): ja / nein
- **SGB XI** Pflegeversicherung (Pflegegrade): ja / nein
- **SGB XII** Sozialhilfe (Grundsicherung im Alter Eingliederungshilfe): ja / nein
- **AsylbLG** Asylbewerberleistungen: ja / nein

### 3. Zuständige Gerichte

- **Hauptsozialgericht** mit Adresse und beA-/EGVP-Postfach
- **LSG** des Bundeslandes
- Bundessozialgericht Kassel (Revision)

### 4. Versandwege

- **beA** vorhanden (Pflicht für RA seit 01.01.2022)
- **EGVP** Behörden- und Gerichtsversand
- **Post** Restfälle (Mandanten ohne digitalen Zugang)
- **ePostfach** Mandanten-eAkte

### 5. Prozesskostenhilfe

- **PKH-Quote** geschätzt im Mandantenstamm
- **Vorlagen** für PKH-Antrag und ZP1a vorhanden
- **Belege** Standardliste für Einkommens- und Vermögensnachweis

### 6. Sekretariat und Aktenführung

- **Aktenstruktur-Konvention:** Mandat-Nummer + Mandantenname + Rechtsbereich
- **Postausgangsbuch:** digital / papier / hybrid
- **Fristenbuch:** zentral / je Anwalt
- **Vorfristen:** typischer Vorlauf vor Fristablauf

### 7. Standort und Eskalation

- **Bundesland** (entscheidet über LSG und LSG-Praxis)
- **Eskalationspartner** bei verfahrensrechtlichen Sonderfällen

## Ausgabe

Profil wird geschrieben. Nächste sinnvolle Skills:

- `/sozialrecht-kanzlei:mandanten-intake` — für neue Mandanten
- `/sozialrecht-kanzlei:bescheidanalyse` — wenn Bescheid auf dem Tisch liegt
- `/sozialrecht-kanzlei:fristenbuch-sozialrecht` — Fristen-Check

## Rechtlicher Rahmen

- **SGG** Sozialgerichtsgesetz: § 78 Vorverfahren / § 84 Widerspruchsfrist / § 87 Klagefrist / § 86b Eilrechtsschutz
- **SGB X** Sozialverwaltungsverfahren: §§ 41 ff. Heilung / § 25 Akteneinsicht / § 44 Überprüfung
- **BRAO** § 31a beA-Pflicht
- **RVG** + RVG-VV für Sozialrechtsverfahren (Sondergebuehren) und PKH

## Hinweise

Dieses Plugin ist Werkzeug der zugelassenen Anwaltschaft. Mandantenkommunikation bleibt anwaltliche Verantwortung. Anlagen vor Versand sichten. Vor jedem Versand der `versand-vor-check` aus dem Plugin `kanzlei-cowork`.
