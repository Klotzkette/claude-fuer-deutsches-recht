---
name: karteikarten
description: >
  Erstellt oder übt Karteikarten für die Gedächtnisleistung im Jurastudium — Leitner-System,
  fachspezifische Definitionen (§-genaue Formulierungen), Drill-Modus mit Selbsteinschätzung.
  Lädt, wenn der Nutzer „Karteikarten erstellen", „Definition üben", „Wiederholung starten"
  oder „Anki-Karten für [Rechtsgebiet]" sagt.
language: de
triggers:
  - "Karteikarten erstellen"
  - "Definition üben"
  - "Karteikarten Strafrecht"
  - "Definitionen Zivilrecht"
  - "Wiederholung starten"
  - "Anki Jura"
  - "Drill-Modus"
  - "Lernkartei"
  - "Definitionen wiederholen"
---

# Karteikarten-Drill

## Zweck

Definitionen, Tatbestandsmerkmale und Normstrukturen für das Staatsexamen müssen exakt und abrufbar sein — nicht „ungefähr bekannt". Diese Skill erzeugt Karteikarten aus eigenen Materialien (Skripten, Lernblättern, Definitionen-Sammlungen) oder aus eigenen Notizen, übt sie im Leitner-System und zeigt, welche Wissenslücken bestehen.

Nicht diese Skill: Anki selbst ersetzen. Wer Anki bereits nutzt, sollte es behalten. Diese Skill ist für den Direkteinstieg im Chat — ohne Programmwechsel.

Modi: `--erstellen` | `--üben` (Standard) | `--durchsehen` | `--statistik` | `--einheit <n>`

## Eingaben

- **Rechtsgebiet oder Thema** (z. B. „BGB AT Willenserklärung", „§ 242 StGB", „Allgemeines Verwaltungsrecht Ermessen")
- **Quelle** (Skript, Lernblatt, eigene Notizen — optional, aber für genaue Karten erforderlich)
- **Kartenanzahl** (Standard: 10–20 pro Einheit)
- **Prüfungsziel** (Erstes Staatsexamen, Zweites Staatsexamen, Klausur, Hausarbeit)

## Rechtlicher Rahmen

Die Karteikarten folgen der kanonischen Definitionsliteratur des deutschen Rechts. Definitionen ohne zuverlässige Quellenangabe werden mit `[PRÜFEN]` markiert.

**Maßgebliche Literatur und Rechtsprechung:**

- Larenz/Wolf, BGB Allgemeiner Teil, 9. Aufl. 2004 — Grundlagendefinitionen BGB AT
- Medicus/Lorenz, Schuldrecht I Allgemeiner Teil, 22. Aufl. 2021 — Schuldrecht
- Roxin/Greco, Strafrecht Allgemeiner Teil, Bd. I, 5. Aufl. 2020 — StGB AT
- Maurer/Waldhoff, Allgemeines Verwaltungsrecht, 20. Aufl. 2020 — VerwR
- Brox/Walker, Allgemeines Schuldrecht, 46. Aufl. 2022
- Wessels/Beulke/Satzger, Strafrecht AT, 53. Aufl. 2023
- Grüneberg, BGB, 84. Aufl. 2025 (vormals Palandt) — maßgeblich für Kurzformeln

**Leitentscheidungen (Beispiele für Kartenkontexte):**

- BGH, Urt. v. 07.06.1984 – IX ZR 66/83, BGHZ 91, 324 — Schweigen als Willenserklärung
- BGH, Urt. v. 08.03.2005 – XI ZR 170/04, NJW 2005, 1579 Rn. 14 — Anfechtung § 119 BGB
- BGH, Urt. v. 26.11.2015 – I ZR 174/14, NJW 2016, 1575 — Bestimmtheitsgrundsatz
- BGH BGHZ 213, 374 Rn. 26 ff. — Vorsatz und dolus eventualis im Zivilrecht

**Kommentare:**

- Ellenberger, in: Grüneberg, BGB, 84. Aufl. 2025, § 119 Rn. 4
- Armbrüster, in: MüKoBGB, 9. Aufl. 2021, § 123 Rn. 12
- Wendtland, in: BeckOK BGB, 70. Ed. (Stand 01.08.2024), § 133 Rn. 5

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
2. Die Forderseite stellt eine Frage, kein Stichwort. Nicht „Vorsatz" — sondern „Was ist Vorsatz im Sinne des § 15 StGB?"
3. Die Rückseite enthält die Definition in Examensqualität — so wie sie in der Klausur gefordert wird.
4. Paragraphenangabe immer mit §-Zeichen: `§ 242 StGB`, `§ 812 Abs. 1 S. 1 Alt. 1 BGB`.
5. Karten aus eigenen Quellen sind zuverlässig. Karten aus meinem Wissen ohne Quelle erhalten `[PRÜFEN: Definition bestätigen]`.

**Beispiel-Karte:**

```
F: Was ist Beleidigung im Sinne des § 185 StGB?
A: Beleidigung ist die Kundgabe der Miss- oder Nichtachtung gegenüber einer bestimmten Person
   durch Erklärung oder tätliches Verhalten.
Norm: § 185 StGB
Quelle: Wessels/Hettinger/Engländer, Strafrecht BT 1, 46. Aufl. 2023, Rn. 401
```

### Schritt 3: Drill-Modus (`--üben`)

**Priorisierung:**
1. Karten mit `nächste_wiederholung <= heute` und Bucket ≠ gekonnt
2. Neue, noch nicht versuchte Karten
3. Kein Fälliges mehr: Fragen, ob gekonnte Karten zur Verfallsprävention wiederholt werden sollen

**Drill-Ablauf je Karte:**
1. Frage zeigen. Auf Antwort warten.
2. Nutzer antwortet (oder: „weiß nicht" / „überspringen")
3. Antwort und Norm zeigen
4. Selbsteinschätzung: `gewusst` / `teilweise` / `nicht gewusst` / `weiß nicht`
5. Bucket und Wiederholungstermin aktualisieren:

| Einschätzung | Bucket | Nächste Wiederholung |
|---|---|---|
| gewusst | aufsteigen (neu → lernend → überprüfend → gekonnt) | +1 Tag neu, +3 lernend, +7 überprüfend, +21 gekonnt |
| teilweise | gleich | +1 Tag |
| nicht gewusst | absteigen | heute +4 Stunden |
| weiß nicht | absteigen | heute +4 Stunden |

## Ausgabeformat

- Karten im Markdown-Format, ein Block je Karte
- Statistik als Tabelle: Rechtsgebiet / Gesamt / Bucket-Verteilung / Heute fällig
- Sitzungsbericht am Ende einer `--einheit`:

```yaml
sitzungs_verlauf:
  - datum: 2026-05-08
    rechtsgebiet: Schuldrecht BT
    typ: karteikarten
    karten_anzahl: 10
    gewusst: 7
    teilweise: 2
    nicht_gewusst: 1
    problemthemen: [§ 823 Abs. 2 BGB Schutzgesetze]
```

## Beispiel

**Einheit BGB AT — 5 Karten:**

> F: Wann liegt eine Willenserklärung vor?
> A: Eine Willenserklärung ist eine private Willensäußerung, die unmittelbar auf die Herbeiführung einer Rechtsfolge gerichtet ist (Handlungswille, Erklärungsbewusstsein [str.], Geschäftswille).
> Norm: §§ 116 ff. BGB; Ellenberger, in: Grüneberg, BGB, 84. Aufl. 2025, Vor § 116 Rn. 1.

> F: Was ist der Unterschied zwischen Anfechtung nach § 119 und § 123 BGB?
> A: § 119 BGB: Irrtum über Inhalt oder Erklärungsinhalt (ohne Verschulden des Anfechtungsgegners); § 123 BGB: arglistige Täuschung oder widerrechtliche Drohung (Verschulden des Täuschenden erforderlich). Ausschlussfrist: § 119 „unverzüglich", § 123 Abs. 1 i.V.m. § 124 BGB ein Jahr.
> Norm: §§ 119, 123, 124 BGB.

## Risiken und typische Fehler

- **Ungenaue Definitionen lernen**: Eine Karte mit einer im Wesentlichen richtigen, aber examensuntauglichen Definition ist schlimmer als keine Karte. Definitionen aus Skripten sind oft schärfer als solche aus meinem Wissen — Skripte bevorzugen.
- **Zu viel auf eine Karte**: Tatbestandsmerkmale sind einzeln zu üben, nicht als Block. Wer „Betrug § 263 StGB: alle Merkmale" auf eine Karte schreibt, hat sechs Karten in eine gepresst.
- **Karte als Lernersatz**: Karteikarten sind Abruftraining für bereits Verstandenes. Eine Karte, die regelmäßig falsch beantwortet wird, zeigt ein Verständnisproblem — dann ist mündliches Durcharbeiten mit `sokratisches-drillen` angezeigt.
- **Wiederholungstermine ignorieren**: Das Leitner-System funktioniert nur, wenn die Abstände eingehalten werden. Ausgefallene Tage akkumulieren Rückstand.
- **Keine Normangabe**: Jede Karte muss die einschlägige Norm nennen. Definitionen ohne Norm sind im Examen wertlos.

## Quellenpflicht

Jede Karte, die aus eigenen Unterlagen generiert wurde, trägt die Quellangabe dieser Unterlagen. Karten, die aus meinem Wissen ohne bereitgestellte Quelle generiert werden, erhalten `[PRÜFEN]` — vor dem Einlernen gegen Skript, Lehrbuch oder Kommentar abgleichen. Falsch eingeübte Definitionen schaden mehr als Lücken.

**Kanonische Definitionen-Quellen:**
- Skripten: Alpmann Schmidt, Hemmer/Wüst, Jura Intensiv, Kaiser-Skripten
- Lehrbücher: s. Rechtlicher Rahmen
- Kommentare: Grüneberg (vormals Palandt), MüKoBGB, BeckOK BGB

Hinweis: Diese Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.
