---
name: ag-vorbereitung
description: >
  Vorbereitung auf das Aufrufen in der Arbeitsgemeinschaft (AG) oder im
  Seminar. Lade diesen Skill bei Anfragen wie „AG-Vorbereitung",
  „Seminar vorbereiten", „was fragt der Dozent", „Cold Call" oder
  „ich werde morgen drangenommen".
language: de
argument-hint: "[Fall oder Thema nennen]"
triggers:
  - "ag-vorbereitung"
  - "seminar vorbereiten"
  - "aufgerufen werden"
  - "cold call"
  - "drangenommen"
  - "arbeitsgemeinschaft"
---

# AG/Seminar-Vorbereitung (Cold-Call-Prep)

## Zweck

Dieser Skill bereitet dich auf das **Aufrufen in der Arbeitsgemeinschaft (AG)** oder im **Seminar** vor. Die AG ist im deutschen Jurastudium ein zentrales Lernformat: ein Dozent (oft Referendar oder wissenschaftlicher Mitarbeiter) bespricht Übungsfälle mit kleinen Gruppen von Studierenden. Wer nicht vorbereitet ist, verliert wertvolle Übungszeit.

Schwerpunkte:
- Fallbesprechungs-AGs im Grundstudium (BGB, StGB, ÖffR)
- Übungsklausur-AGs in der Examensvorbereitung
- Seminargespräche mit sokratischen Dozentenbohrern
- Lehrveranstaltungen, in denen aktive Teilnahme benotet wird (Große Übung, BGB-Übung)

Das Plugin sagt **nicht**, was der Dozent fragen wird – es bohrt die Fragen, die ein erfahrener AG-Leiter wahrscheinlich stellen wird, und lässt dich antworten.

## Eingaben

1. **Fall oder Thema** – als Text oder Stichworte
2. **AG-Typ** – Grundstudium / Fortgeschrittenenübung / Examens-AG / Seminar
3. **Lernprofil** (`~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md`) → Fachsemester, Schwächen, Lernstil
4. Optional: **bisherige Musterlösung** oder eigene Antwort zur Besprechung

## Ablauf

### Schritt 1: Fallanalyse

Das Plugin analysiert den vorliegenden Fall / das Thema und:
- Identifiziert die **3–5 klassischen Bohrerpunkte**, an denen ein AG-Leiter einhaken wird
- Bewertet, welche Streitstände für die AG-Besprechung typisch sind
- Markiert Punkte, die erfahrungsgemäß unterschätzt werden

### Schritt 2: Simuliertes Aufrufen

Das Plugin nimmt die Rolle des AG-Leiters ein und **bohrt dich**:

> „Du bist A und behauptest einen Anspruch auf Rückzahlung. Welche Anspruchsgrundlage prüfst du zuerst, und warum nicht § 812 BGB?"

Es gibt nicht die Antwort. Es wartet auf deine Antwort und hakt nach.

Typische AG-Leiter-Fragen, die das Plugin simuliert:
- „Was ist der Obersatz?"
- „Wie definierst du [Tatbestandsmerkmal]?"
- „Was sagt der Grüneberg dazu?"
- „Was ist die Mindermeinung, und warum folgt die h.M. nicht ihr?"
- „Kannst du den Unterschied zwischen § 280 Abs. 1 und § 280 Abs. 3 BGB erklären?"
- „Was ändert sich, wenn [Sachverhaltsmodifikation]?"

Im **Drill-Modus**: Das Plugin stellt die Fragen, ohne Hinweise zu geben.
Im **Erklärungs-Modus**: Das Plugin gibt nach der Frage einen Kontext-Hinweis.

### Schritt 3: Sachverhaltsmodifikationen

Nach der Grundbesprechung gibt das Plugin typische AG-Variationen:
- „Was ändert sich, wenn A weiß, dass B ein Minderjähriger ist?"
- „Wie wäre es, wenn A die Frist nicht gesetzt hätte?"
- „Gilt das auch, wenn es sich um Dienst- statt Kaufvertrag handelt?"

### Schritt 4: Zusammenfassung

Nach der Simulationssitzung:
- Liste der beantworteten und offenen Fragen
- Schwachstellen mit gezielten Verweisen (Norm, Kommentar, Lernplan)
- Empfehlung, welche Abschnitte vor der AG nochmals durchzuarbeiten sind

## Quellen und Zitierweise

→ `../references/zitierweise.md`

In der AG wird das **mündliche Zitieren** erwartet – kein vollständiges Literaturverzeichnis, aber:
- Kommentar benennen: „Im Grüneberg, § 280 Rn. X steht …"
- BGH nennen: „Der BGH hat in der Entscheidung NJW [Jahr], [Seite] entschieden, dass …"
- Streitstand anzeigen: „Nach h.M. – so der Grüneberg und der MüKo – gilt X. Die Gegenauffassung bei Brox/Walker argumentiert …"

**Häufig nachgefragte Quellen in AGs:**
- Grüneberg, BGB (Studienstandard, fast immer vorhanden)
- Brox/Walker, *Allg. Schuldrecht*, 47. Aufl. 2023 – häufig für Schuldrecht-AGs
- Medicus/Petersen, *Bürgerliches Recht*, 27. Aufl. 2019 – breite Schuldrechtsdarstellung
- Wertenbruch, *BGB AT*, 5. Aufl. 2023 – AT-AGs
- Fischer, StGB – Strafrecht-AGs

## Ausgabeformat

### AG-Vorbereitung (Steckbrief)

```
**Fall / Thema:** [Kurzzusammenfassung]
**AG-Typ:** [Grundstudium / Fortgeschrittene / Examens-AG]
**Schwerpunktnormen:** [§§]
**Kernstreitstand:** [1–2 Sätze]

**Die 5 wahrscheinlichsten AG-Fragen:**
1. [Frage] → [Hinweis auf relevanten Kommentarabschnitt]
2. [Frage] → [Normbezug]
3. [Frage] → [Streitstand mit Belegen]
4. [Frage] → [Sachverhaltsmodifikation]
5. [Frage] → [Vertiefungsfrage]

**Sachverhaltsmodifikationen:**
- Was ändert sich, wenn …?
- Wie ist es, wenn …?

**Vorbereiten bis:** [gezielte Seiten/Randnummern aus dem Kommentar]
```

### Simulierte AG-Sitzung

```
[AG-Leiter-Modus]
Frage: „[Konkrete Frage im AG-Stil]"

[Nutzerantwort]

Nachbohren: „[Präzisierungsfrage oder Sachverhaltsmodifikation]"
```

## Beispiel

**Fall:** A und B schließen einen Kaufvertrag über ein Notebook (800 €). Das Notebook ist bei Übergabe defekt (Bildschirm flimmert). B verlangt Nacherfüllung. A verweigert. B setzt eine Frist von 14 Tagen, die fruchtlos verstreicht.

**AG-Vorbereitung:**

Schwerpunktnormen: §§ 433, 434, 437, 439, 280, 281 BGB

Die 5 wahrscheinlichsten AG-Fragen:
1. „Was ist der Obersatz für den Schadensersatzanspruch?" → §§ 437 Nr. 3, 280 Abs. 1, 3, 281 BGB; Grüneberg/Weidenkaff, § 437 Rn. 1
2. „Wann liegt ein Sachmangel vor?" → § 434 Abs. 1 BGB; Grüneberg/Weidenkaff, § 434 Rn. 5
3. „War die Fristsetzung wirksam?" → § 281 Abs. 1 S. 1 BGB; Frist muss angemessen sein
4. „Was ändert sich, wenn der Mangel erst nach 6 Monaten auftritt?" → Beweislastumkehr § 477 BGB; BGH, NJW 2021, 1006
5. „Wie verhält sich § 280 Abs. 1 BGB zu §§ 280 Abs. 3, 281 BGB?" → Subsidiarität des Schadensersatzes statt der Leistung; Ernst, in: MüKoBGB, § 280 Rn. 60

**Simulierte AG-Frage:**
„Wir sind bei dem Schadensersatzanspruch. Du sagst, § 437 Nr. 3 BGB. Gut. Aber was ist mit dem Vertretenmüssen? Hat B das zu beweisen, oder A?"

*[Deine Antwort]*

Nachbohren: „Und wenn A beweist, dass der Defekt durch unsachgemäße Behandlung nach Übergabe entstanden ist – was passiert dann mit § 477 BGB?"

## Risiken / typische Fehler

- **Unpräziser Obersatz:** In der AG erwartet der Dozent den hypothetisch formulierten Obersatz, nicht eine Zusammenfassung des Sachverhalts.
- **Streitstände nicht kennen:** AG-Leiter bohren gezielt auf bekannte Diskussionspunkte. § 434 BGB n. F. (2022) hat den Mangelbegriff verändert – vor jeder AG auf aktuelle Gesetzeslage prüfen.
- **Sachverhaltsmodifikationen nicht antizipieren:** Fast jede AG endet mit Modifikationsfragen. Diese üben und im Lernprofil protokollieren.
- **Quellen nicht benennen können:** „Ich glaube, das steht irgendwo im Kommentar" ist keine AG-Antwort. Mindestens Grüneberg + eine BGH-Entscheidung zu jedem Kernanspruch kennen.
- **Defensives Schweigen:** Lieber eine strukturierte Antwort auf falschem Fundament als gar keine Antwort – der AG-Leiter kann nur korrigieren, was er hört.
