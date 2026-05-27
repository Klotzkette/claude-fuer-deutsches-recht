---
name: lernsitzung
description: "Lernsitzung fuer Jurastudium interaktiv durchfuehren: Anwendungsfall Student will aktive Lernsitzung zu bestimmtem Thema absolvieren mit Erklaerungen Uebungsaufgaben und sofortigem Feedback. Tatbestaende, Subsumtion, Loesungsschemata Zivilrecht Strafrecht oeffentliches Recht. Pruefraster Thema und Lernziel festlegen, Erklaerung Kontrollfragen Uebungsfall Feedback, Wissenslücken identifizieren. Output strukturierte Lernsitzung mit Erklaerungen und Zwischentest. Abgrenzung zu Karteikarten fuer Memorierung und zu Gutachten-Uebung fuer Klausurtraining."
---

# Lerneinheit

## Zweck

Eine strukturierte Lerneinheit mit einer festen Anzahl an Fragen — Karteikarten-Drill, Klausurfrage im Gutachtenstil oder Mündlichkeitssimulation. Die Ergebnisse fließen in den Lernplan ein, sodass die nächste Einheit auf dem aufsetzt, was in dieser Einheit schwierig war.

## Eingaben

- **Rechtsgebiet** (z. B. „Schuldrecht AT", „§§ 242, 243 StGB", „Verwaltungsrecht Ermessen")
- **Anzahl der Fragen** (N)
- **Modus** (`--karteikarten` | `--klausurfrage` | `--mündlich`, Standard: Nachfrage)
- Optional: **Schwerpunkt** (z. B. „Schwerpunkt: Kausalität", „nur Definitionen")

## Rechtlicher Rahmen

Die Fragen folgen dem Examensrelevanzkanon für das Erste und Zweite Staatsexamen nach JAG/JAPrO der Bundesländer. Inhaltlicher Maßstab:

**Leitentscheidungen (Beispiele je Modus):**

Karteikarten-Drill (Definitionen):
- BGH, Urt. v. 07.06.1984 – IX ZR 66/83, BGHZ 91, 324 — Willenserklärung, Definition Schweigen
- BGH BGHZ 213, 374 Rn. 26 ff. — dolus eventualis im Zivilrecht

Gutachtenstil-Klausurfragen:
- BGH, Urt. v. 25.11.2009 – VIII ZR 318/08, NJW 2010, 610 Rn. 12 — Leistungsstörungsrecht § 280 BGB
- BGH, Urt. v. 22.09.1995 – 2 StR 310/95, BGHSt 41, 292 — Mittäterschaft § 25 Abs. 2 StGB

**Literatur:**
- Grüneberg, BGB, 84. Aufl. 2025 (vormals Palandt) — Kurzkommentar-Standard
- Roxin/Greco, Strafrecht AT I, 5. Aufl. 2020 — Deliktsaufbau (Lehrbuch)
- Maurer/Waldhoff, Allgemeines Verwaltungsrecht, 20. Aufl. 2020 — VerwR-Standard (Lehrbuch)
- Armbrüster, in: MüKoBGB, 9. Aufl. 2021, § 116 Rn. 1 ff. — BGB AT vertiefte Definitionen

## Ablauf

### Schritt 1: Eingaben prüfen

Wenn Rechtsgebiet oder Anzahl fehlen, einmalig fragen:

> „Welches Rechtsgebiet, und wie viele Fragen? (z. B. ‚Schuldrecht AT, 10 Fragen' oder ‚StGB BT Eigentumsdelikte 5 — Gutachtenstil')"

### Schritt 2: Modus bestimmen und Inhaltsquelle laden

- `--karteikarten`: `karteikarten`-Skill laden, N Karten im Drill-Modus, priorisiert nach früheren Fehlern + fälligen Karten
- `--klausurfrage`: `gutachten-uebung`-Skill laden, N Kurzklausurfragen im Gutachtenstil generieren, Nutzer schreibt Lösung, Feedback pro Frage
- `--mündlich` (Standard): `pruefungsgespraech-ag`-Skill laden, N Fragen im sokratischen Frage-Antwort-Format, Pushback nach jeder Antwort

Jurisdiktion/Prüfungsordnung aus Nutzerprofil laden, falls vorhanden (z. B. Examensvorbereitung NRW → JAG NRW-Prüfungsstoff priorisieren).

### Schritt 3: N Fragen — eine nach der anderen

Nie mehrere Fragen auf einmal. Erst Antwort abwarten, dann nächste Frage.

Nach jeder Frage: kurze Rückmeldung (richtig / teilweise / falsch + Korrektur). Falsche Antworten mit Normangabe erläutern — nie nur „falsch".

### Schritt 4: Sitzungsabschluss

Am Ende der N Fragen:
- Ergebnis: X/N richtig (Prozentwert)
- Nicht gewusste Themen: Liste mit Unterthema-Tags
- Schwache Unterthemen dieser Sitzung
- Vergleich mit früheren Sitzungen zu diesem Rechtsgebiet (falls Verlauf existiert)
- Empfehlung für die nächste Sitzung

Sitzungsbericht schreiben:

```yaml
sitzungs_verlauf:
  - datum: 2026-05-08
    rechtsgebiet: Schuldrecht AT
    typ: karteikarten          # oder klausurfrage / mündlich
    fragen_anzahl: 10
    richtig: 7
    teilweise: 1
    falsch: 2
    schwache_themen: [§ 275 Abs. 1 BGB Unmöglichkeit, § 286 Abs. 2 BGB Verzug ohne Mahnung]
```

Falls Lernplan vorhanden: Sitzungsbericht an `lernplan.yaml` → `sitzungs_verlauf` anhängen.
Falls kein Lernplan: in `sitzungs_verlauf.yaml` schreiben.

### Schritt 5: Anschlussempfehlung

> „Auf Basis dieser Sitzung empfiehlt sich als nächster Schritt: [konkrete Empfehlung — z. B. ‚Definitionen § 275 BGB mit karteikarten vertiefen' oder ‚gutachtenstil-übung: Klausurfall zu § 286 BGB']."

## Ausgabeformat

- Fragen einzeln, eine nach der anderen
- Rückmeldung je Frage: kurz und normgenau
- Sitzungsabschluss: tabellarische Auswertung + Verlaufsmuster (ab 2+ Sitzungen zu demselben Rechtsgebiet)
- YAML-Sitzungsbericht für den Lernplan

## Beispiel

**Eingabe:** „10 Fragen Strafrecht BT Eigentumsdelikte, Modus mündlich"

**Verlauf (Auszug):**

> Frage 1: A nimmt heimlich das Fahrrad des B mit, um es dauerhaft zu behalten. Welche Straftatbestände kommen in Betracht, und wie lautet der Obersatz für den ersten Anspruch?

Nutzer antwortet. Skill prüft: Ist § 242 Abs. 1 StGB (Diebstahl) benannt? Obersatz vorhanden? Fremdheit der Sache, Wegnahme, Zueignungsabsicht als Prüfungspunkte erwähnt?

Pushback falls unvollständig: „Sie haben § 242 StGB benannt — gut. Was ist Wegnahme? Definition, bitte."

**Sitzungsabschluss:** 7/10 richtig. Schwache Themen: Abgrenzung § 242/246 StGB (Diebstahl/Unterschlagung), Gewahrsamsbruch-Definition. Empfehlung: Karteikarten § 242–248c StGB + eine Klausurfrage zur Abgrenzung.

## Risiken und typische Fehler

- **Rechtsgebiet zu weit gewählt**: „BGB" als Rechtsgebiet für eine 10-Fragen-Einheit ist sinnlos breit. Auf Unterthemen eingrenzen (z. B. „BGB AT Stellvertretung §§ 164 ff.").
- **Modus nicht zur Lernphase passend**: Karteikarten sind für Definitionen-Memorierung. Gutachtenstil-Klausurfragen für Strukturtraining. Mündlich für Verständnis-Tiefe. Den richtigen Modus zur richtigen Lernphase wählen.
- **Sitzungsergebnisse nicht verwerten**: Der Wert der Sitzungshistorie liegt darin, dass schwache Themen bei der nächsten Sitzung priorisiert werden. Sitzungen ohne Auswertung sind verlorenes Feedback.
- **Lernplan-Abweichungen ignorieren**: Wenn die Sitzungshistorie zeigt, dass ein Thema in drei Sitzungen hintereinander schlecht abgeschnitten hat, muss es im Lernplan hochgestuft werden — nicht nur in der nächsten Sitzung wiederholt.

## Quellenpflicht

Normangaben und Definitionen in Fragen und Korrekturen folgen gefestigter Rechtsprechung und kanonischer Literatur. Werden Fragen aus meinem Wissen generiert (nicht aus bereitgestellten Quellen), gilt: inhaltliche Korrektheit ist mit `[PRÜFEN]` markiert, wenn keine sichere Verifikation möglich ist. Vor dem Einlernen gegen Skript oder Kommentar abgleichen.

Hinweis: Diese Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
