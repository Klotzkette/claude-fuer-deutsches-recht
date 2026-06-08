---
name: karteikarten-lernplan-lernsitzung
description: "Karteikarten für Jurastudium und Examensvorbereitung erstellen: Anwendungsfall Student will Definitionen Tatbestaende Normen und Klausurrelevante Faelle als Lernkarten strukturieren. Lösungsschemata, Tatbestaende, Definitionen Buergerliches Recht Strafrecht öffentliches Recht. Prüfraster Karteikarten-Format Vorderseite Begriff/Norm Rückseite Definition/Schema, Schwierigkeitsgrad einordnen, prüfungsrelevant markieren. Output Karteikarten-Sammlung nach Fachgebiet strukturiert für Spaced-Repetition. Abgrenzung zu Lernplan für Zeitmanagement und zu Tatbestaende-Lernen im Jurastudium."
---

# Karteikarten-Drill

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DRiG § 5a Studiendauer 9 Semester (Regelstudienzeit), Freischuss-Frist (i.d.R. 8 Semester nach JAG), Wiederholungsfrist, Hausarbeit 4-6 Wochen.
- Tragende Normen verifizieren: DRiG §§ 5, 5a, 5b (Erste Prüfung), JAG der Länder, JAPO Bayern, JAG NRW, BBesG (Referendariat), Hochschulgesetze, Studienordnungen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Studierende, Justizprüfungsamt (Landesjustizverwaltung), Universität, Repetitorium, Klausurleiter, Mündliche-Prüfungs-Kommission.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Klausurgutachten (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis), Hausarbeit, Aktenvortrag (Referendar), Probeklausur, Prüfungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- **Rechtsgebiet oder Thema** (z. B. "BGB AT Willenserklärung", "§ 242 StGB", "Allgemeines Verwaltungsrecht Ermessen")
- **Quelle** (Skript, Lernblatt, eigene Notizen — optional, aber für genaue Karten erforderlich)
- **Kartenanzahl** (Standard: 10–20 pro Einheit)
- **Prüfungsziel** (Erstes Staatsexamen, Zweites Staatsexamen, Klausur, Hausarbeit)

## Rechtlicher Rahmen

Karteikarten aus bereitgestellten Materialien sind vorrangig. Definitionen oder Streitstände ohne zuverlässige Quelle werden mit `[PRÜFEN]` markiert.

**Quellenregel und Rechtsprechung:**

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

**Leitentscheidungen (Beispiele für Kartenkontexte):**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Quellenregel:**

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ablauf

### Schritt 1: Modus bestimmen

- `--erstellen`: Karten aus bereitgestellter Quelle generieren
- `--üben` (Standard): Fällige Karten + neue Karten üben; Frage zeigen → antworten → Antwort zeigen → Selbsteinschätzung → Bucket aktualisieren
- `--durchsehen`: Gesamte Kartei nach Bucket anzeigen
- `--statistik`: Fortschritt je Rechtsgebiet; hängen gebliebene Karten für mündlichen Drill markieren
- `--einheit <n>`: Fokussierte Einheit mit n Karten, priorisiert nach früheren Fehlern

### Schritt 2: Kartenerstellung (`--erstellen`)

**Kartenformat:**

```markdown
### Karte [N]
**F:** [Frage — ein Begriff, ein Tatbestandsmerkmal]
**A:** [Definition oder Regel — ein bis zwei Sätze, exakte Formulierung]
**Norm:** [§ / Art. — z. B. § 119 BGB]
**Quelle:** [Skript-Seite, Literatur, Urteil]
**Bucket:** neu
**Zuletzt geübt:** —
**Nächste Wiederholung:** [heutiges Datum]
**Hinweise:** [Abgrenzungen, Ausnahmen, Klausurfallen]
```

**Kartenregeln:**
1. Ein Begriff, ein Tatbestandsmerkmal = eine Karte. Nie mehrere Definitionen auf einer Karte.
2. Die Forderseite stellt eine Frage, kein Stichwort. Nicht "Vorsatz" — sondern "Was ist Vorsatz im Sinne des § 15 StGB?"
3. Die Rückseite enthält die Definition in Examensqualität — so wie sie in der Klausur gefordert wird.
4. Paragraphenangabe immer mit §-Zeichen: `§ 242 StGB`, `§ 812 Abs. 1 S. 1 Alt. 1 BGB`.
5. Karten aus eigenen Quellen sind zuverlässig. Karten aus meinem Wissen ohne Quelle erhalten `[PRÜFEN: Definition bestätigen]`.

**Beispiel-Karte:**

```
F: Was ist Beleidigung im Sinne des § 185 StGB?
A: Beleidigung ist die Kundgabe der Miss- oder Nichtachtung gegenüber einer bestimmten Person
 durch Erklärung oder tätliches Verhalten.
Norm: § 185 StGB
```

### Schritt 3: Drill-Modus (`--üben`)

**Priorisierung:**
1. Karten mit `nächste_wiederholung <= heute` und Bucket ≠ gekonnt
2. Neue, noch nicht versuchte Karten
3. Kein Fälliges mehr: Fragen, ob gekonnte Karten zur Verfallsprävention wiederholt werden sollen

**Drill-Ablauf je Karte:**
1. Frage zeigen. Auf Antwort warten.
2. Nutzer antwortet (oder: "weiß nicht" / "überspringen")
3. Antwort und Norm zeigen
4. Selbsteinschätzung: `gewusst` / `teilweise` / `nicht gewusst` / `weiß nicht`
5. Bucket und Wiederholungstermin aktualisieren:

| Einschätzung | Bucket | Nächste Wiederholung |
|---|---|---|
| gewusst | aufsteigen (neu → lernend → überprüfend → gekonnt) | +1 Tag neu, +3 lernend, +7 überprüfend, +21 gekonnt |
| teilweise | gleich | +1 Tag |
| nicht gewusst | absteigen | heute +4 Stunden |
| weiß nicht | absteigen | heute +4 Stunden |

## Beispiel

**Einheit BGB AT — 5 Karten:**

> F: Wann liegt eine Willenserklärung vor?
> A: Eine Willenserklärung ist eine private Willensäußerung, die unmittelbar auf die Herbeiführung einer Rechtsfolge gerichtet ist (Handlungswille, Erklärungsbewusstsein [str.], Geschäftswille).
> Norm: §§ 116 ff. BGB; Ellenberger, in: lizenzpflichtige Literaturquelle, BGB, 84. Aufl. 2025, Vor § 116 Rn. 1.

> F: Was ist der Unterschied zwischen Anfechtung nach § 119 und § 123 BGB?
> A: § 119 BGB: Irrtum über Inhalt oder Erklärungsinhalt (ohne Verschulden des Anfechtungsgegners); § 123 BGB: arglistige Täuschung oder widerrechtliche Drohung (Verschulden des Täuschenden erforderlich). Ausschlussfrist: § 119 "unverzüglich", § 123 Abs. 1 i.V.m. § 124 BGB ein Jahr.
> Norm: §§ 119, 123, 124 BGB.

## Risiken und typische Fehler

- **Ungenaue Definitionen lernen**: Eine Karte mit einer im Wesentlichen richtigen, aber examensuntauglichen Definition ist schlimmer als keine Karte. Definitionen aus Skripten sind oft schärfer als solche aus meinem Wissen — Skripte bevorzugen.
- **Zu viel auf eine Karte**: Tatbestandsmerkmale sind einzeln zu üben, nicht als Block. Wer "Betrug § 263 StGB: alle Merkmale" auf eine Karte schreibt, hat sechs Karten in eine gepresst.
- **Karte als Lernersatz**: Karteikarten sind Abruftraining für bereits Verstandenes. Eine Karte, die regelmäßig falsch beantwortet wird, zeigt ein Verständnisproblem — dann ist mündliches Durcharbeiten mit `pruefungsgespraech-ag` angezeigt.
- **Wiederholungstermine ignorieren**: Das Leitner-System funktioniert nur, wenn die Abstände eingehalten werden. Ausgefallene Tage akkumulieren Rückstand.
- **Keine Normangabe**: Jede Karte muss die einschlägige Norm nennen. Definitionen ohne Norm sind im Examen wertlos.

## Quellenpflicht

Jede Karte, die aus eigenen Unterlagen generiert wurde, trägt die Quellangabe dieser Unterlagen. Karten, die aus meinem Wissen ohne bereitgestellte Quelle generiert werden, erhalten `[PRÜFEN]` — vor dem Einlernen gegen Skript, Lehrbuch oder Kommentar abgleichen. Falsch eingeübte Definitionen schaden mehr als Lücken.

**Kanonische Definitionen-Quellen:**
- Skripten: Alpmann Schmidt, Hemmer/Wüst, Jura Intensiv, Kaiser-Skripten
- Lehrbücher: s. Rechtlicher Rahmen
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Diese Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

