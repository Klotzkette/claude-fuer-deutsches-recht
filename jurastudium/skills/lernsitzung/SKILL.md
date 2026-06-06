---
name: lernsitzung
description: "Lernsitzung für Jurastudium interaktiv durchführen: Anwendungsfall Student will aktive Lernsitzung zu bestimmtem Thema absolvieren mit Erklärungen Uebungsaufgaben und sofortigem Feedback. Tatbestaende, Subsumtion, Lösungsschemata Zivilrecht Strafrecht öffentliches Recht. Prüfraster Thema und Lernziel festlegen, Erklärung Kontrollfragen Uebungsfall Feedback, Wissenslücken identifizieren. Output strukturierte Lernsitzung mit Erklärungen und Zwischentest. Abgrenzung zu Karteikarten für Memorierung und zu Gutachten-Uebung für Klausurtraining im Jurastudium: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Lerneinheit

## Arbeitsbereich

Lernsitzung für Jurastudium interaktiv durchführen: Anwendungsfall Student will aktive Lernsitzung zu bestimmtem Thema absolvieren mit Erklärungen Uebungsaufgaben und sofortigem Feedback. Tatbestaende, Subsumtion, Lösungsschemata Zivilrecht Strafrecht öffentliches Recht. Prüfraster Thema und Lernziel festlegen, Erklärung Kontrollfragen Uebungsfall Feedback, Wissenslücken identifizieren. Output strukturierte Lernsitzung mit Erklärungen und Zwischentest. Abgrenzung zu Karteikarten für Memorierung und zu Gutachten-Uebung für Klausurtraining. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DRiG § 5a Studiendauer 9 Semester (Regelstudienzeit), Freischuss-Frist (i.d.R. 8 Semester nach JAG), Wiederholungsfrist, Hausarbeit 4-6 Wochen.
- Tragende Normen verifizieren: DRiG §§ 5, 5a, 5b (Erste Prüfung), JAG der Länder, JAPO Bayern, JAG NRW, BBesG (Referendariat), Hochschulgesetze, Studienordnungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Studierende, Justizprüfungsamt (Landesjustizverwaltung), Universität, Repetitorium, Klausurleiter, Mündliche-Prüfungs-Kommission.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Klausurgutachten (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis), Hausarbeit, Aktenvortrag (Referendar), Probeklausur, Prüfungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Eine strukturierte Lerneinheit mit einer festen Anzahl an Fragen — Karteikarten-Drill, Klausurfrage im Gutachtenstil oder Mündlichkeitssimulation. Die Ergebnisse fließen in den Lernplan ein, sodass die nächste Einheit auf dem aufsetzt, was in dieser Einheit schwierig war.

## Eingaben

- **Rechtsgebiet** (z. B. "Schuldrecht AT", "§§ 242, 243 StGB", "Verwaltungsrecht Ermessen")
- **Anzahl der Fragen** (N)
- **Modus** (`--karteikarten` | `--klausurfrage` | `--mündlich`, Standard: Nachfrage)
- Optional: **Schwerpunkt** (z. B. "Schwerpunkt: Kausalität", "nur Definitionen")

## Rechtlicher Rahmen

Die Fragen folgen dem Examensrelevanzkanon für das Erste und Zweite Staatsexamen nach JAG/JAPrO der Bundesländer. Inhaltlicher Maßstab:

**Leitentscheidungen (Beispiele je Modus):**

Karteikarten-Drill (Definitionen):
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Gutachtenstil-Klausurfragen:
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Literatur:**
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ablauf

### Schritt 1: Eingaben prüfen

Wenn Rechtsgebiet oder Anzahl fehlen, einmalig fragen:

> "Welches Rechtsgebiet, und wie viele Fragen? (z. B. 'Schuldrecht AT, 10 Fragen' oder 'StGB BT Eigentumsdelikte 5 — Gutachtenstil')"

### Schritt 2: Modus bestimmen und Inhaltsquelle laden

- `--karteikarten`: `karteikarten`-Skill laden, N Karten im Drill-Modus, priorisiert nach früheren Fehlern + fälligen Karten
- `--klausurfrage`: `gutachten-uebung`-Skill laden, N Kurzklausurfragen im Gutachtenstil generieren, Nutzer schreibt Lösung, Feedback pro Frage
- `--mündlich` (Standard): `pruefungsgespraech-ag`-Skill laden, N Fragen im sokratischen Frage-Antwort-Format, Pushback nach jeder Antwort

Jurisdiktion/Prüfungsordnung aus Nutzerprofil laden, falls vorhanden (z. B. Examensvorbereitung NRW → JAG NRW-Prüfungsstoff priorisieren).

### Schritt 3: N Fragen — eine nach der anderen

Nie mehrere Fragen auf einmal. Erst Antwort abwarten, dann nächste Frage.

Nach jeder Frage: kurze Rückmeldung (richtig / teilweise / falsch + Korrektur). Falsche Antworten mit Normangabe erläutern — nie nur "falsch".

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
 typ: karteikarten # oder klausurfrage / mündlich
 fragen_anzahl: 10
 richtig: 7
 teilweise: 1
 falsch: 2
 schwache_themen: [§ 275 Abs. 1 BGB Unmöglichkeit, § 286 Abs. 2 BGB Verzug ohne Mahnung]
```

Falls Lernplan vorhanden: Sitzungsbericht an `lernplan.yaml` → `sitzungs_verlauf` anhängen.
Falls kein Lernplan: in `sitzungs_verlauf.yaml` schreiben.

### Schritt 5: Anschlussempfehlung

> "Auf Basis dieser Sitzung empfiehlt sich als nächster Schritt: [konkrete Empfehlung — z. B. 'Definitionen § 275 BGB mit karteikarten vertiefen' oder 'gutachtenstil-übung: Klausurfall zu § 286 BGB']."

## Ausgabeformat

- Fragen einzeln, eine nach der anderen
- Rückmeldung je Frage: kurz und normgenau
- Sitzungsabschluss: tabellarische Auswertung + Verlaufsmuster (ab 2+ Sitzungen zu demselben Rechtsgebiet)
- YAML-Sitzungsbericht für den Lernplan

## Beispiel

**Eingabe:** "10 Fragen Strafrecht BT Eigentumsdelikte, Modus mündlich"

**Verlauf (Auszug):**

> Frage 1: A nimmt heimlich das Fahrrad des B mit, um es dauerhaft zu behalten. Welche Straftatbestände kommen in Betracht, und wie lautet der Obersatz für den ersten Anspruch?

Nutzer antwortet. Skill prüft: Ist § 242 Abs. 1 StGB (Diebstahl) benannt? Obersatz vorhanden? Fremdheit der Sache, Wegnahme, Zueignungsabsicht als Prüfungspunkte erwähnt?

Pushback falls unvollständig: "Sie haben § 242 StGB benannt — gut. Was ist Wegnahme? Definition, bitte."

**Sitzungsabschluss:** 7/10 richtig. Schwache Themen: Abgrenzung § 242/246 StGB (Diebstahl/Unterschlagung), Gewahrsamsbruch-Definition. Empfehlung: Karteikarten § 242–248c StGB + eine Klausurfrage zur Abgrenzung.

## Risiken und typische Fehler

- **Rechtsgebiet zu weit gewählt**: "BGB" als Rechtsgebiet für eine 10-Fragen-Einheit ist sinnlos breit. Auf Unterthemen eingrenzen (z. B. "BGB AT Stellvertretung §§ 164 ff.").
- **Modus nicht zur Lernphase passend**: Karteikarten sind für Definitionen-Memorierung. Gutachtenstil-Klausurfragen für Strukturtraining. Mündlich für Verständnis-Tiefe. Den richtigen Modus zur richtigen Lernphase wählen.
- **Sitzungsergebnisse nicht verwerten**: Der Wert der Sitzungshistorie liegt darin, dass schwache Themen bei der nächsten Sitzung priorisiert werden. Sitzungen ohne Auswertung sind verlorenes Feedback.
- **Lernplan-Abweichungen ignorieren**: Wenn die Sitzungshistorie zeigt, dass ein Thema in drei Sitzungen hintereinander schlecht abgeschnitten hat, muss es im Lernplan hochgestuft werden — nicht nur in der nächsten Sitzung wiederholt.

## Quellenpflicht

Normangaben und Definitionen in Fragen und Korrekturen folgen gefestigter Rechtsprechung und kanonischer Literatur. Werden Fragen aus meinem Wissen generiert (nicht aus bereitgestellten Quellen), gilt: inhaltliche Korrektheit ist mit `[PRÜFEN]` markiert, wenn keine sichere Verifikation möglich ist. Vor dem Einlernen gegen Skript oder Kommentar abgleichen.

Hinweis: Diese Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
