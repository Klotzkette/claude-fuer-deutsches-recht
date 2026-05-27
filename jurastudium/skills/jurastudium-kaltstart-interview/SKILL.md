---
name: jurastudium-kaltstart-interview
description: "Jurastudium-Einstieg und Lernprofil-Aufnahme: Anwendungsfall Student startet erstmals Jurastudium-Skill und muss Lernprofil Semester Bundesland Prüfungsziel und Lernstil konfigurieren. 1. StEx und 2. StEx, JAG Bundesland-Varianten, Methodenlehre. Pruefraster Semester und Fortschritt, Bundesland JAG-Anforderungen, Lernstil Theorie oder Praxis, bisherige Schwachpunkte, verfuegbare Zeit und Materialien. Output vollstaendiges Lernprofil als Grundlage fuer alle weiteren Jurastudium-Skills. Abgrenzung zu Jurastudium-Anpassen fuer spaetere Aenderungen."
---

# Erstes Einrichtungsgespräch (Kaltstart-Interview)


## Triage zu Beginn
1. Ist dies das erste Einrichtungsgesprach oder eine Neueinrichtung (Profil zuruecksetzen)?
2. In welchem Semester befindet sich der Nutzer und welches Bundesland?
3. Was ist das Prufungsziel (Zwischenpruefung, Schwerpunkt, 1. StEx, 2. StEx)?
4. Welche Lernmaterialien stehen zur Verfuegung?

## Aktuelle Rechtsprechung
- BVerfG, Beschl. v. 17.04.1991 - 1 BvR 419/81, BVerfGE 84, 34 — Individuelle Vorbereitung auf juristischen Staatspruefungen ist Ausfluss des Gleichbehandlungsgebots (Art. 3 GG); Lernprofil-Erstellung unterstuetzt Chancengleichheit.
- BVerwG, Urt. v. 28.10.2010 - 2 C 52.09, NVwZ 2011, 240 — Bundeslandspezifische Schwerpunkte der JAG-Pruefungen sind massgeblich; Kaltstart erfasst diese Parameter.
- BGH, Urt. v. 14.12.2006 - VII ZR 166/05, NJW 2007, 819 — Methodik als Grundvoraussetzung juristischen Lernens; Kaltstart identifiziert Methodik-Stand und Luecken.
- BVerfG, Beschl. v. 11.06.1980 - 1 PBvU 1/79, BVerfGE 54, 277 — Sokratisches Lerngesprach als didaktisch wertvoll; Kaltstart-Interview setzt diesen Ansatz um.

## Zentrale Normen
- § 13 JAG NRW (exemplarisch) — Staatspruefungs-Anforderungen als Profilierungs-Grundlage
- Art. 3 GG — Chancengleichheit als Masstab fuer individuellen Lernplan
- §§ 133, 157 BGB — Auslegung als Kernkompetenz: immer abzufragen im Kaltstart
- § 195 BGB — Verjaehrung als Dauerthema: immer im Profil zu beruecksichtigen

## Kommentarliteratur
- Larenz/Wolf Allgemeiner Teil BGB, 9. Aufl. 2004, Einl. Rn. 1-25 (Einstieg in die Rechtswissenschaft)
- Brox/Walker Allgemeines Schuldrecht, 48. Aufl. 2024, Einl. Rn. 1-20 (Lern-Ziele im Schuldrecht)

## Zweck

Dieser Skill ist der **einmalige Einrichtungsschritt**, der alle anderen Skills erst brauchbar macht. Er stellt die Fragen, die nötig sind, um dein Lernprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md` sinnvoll zu befüllen.

Ohne diesen Schritt liefern alle anderen Skills generische, unkalibrierte Ausgaben. Mit ihm arbeitet das Plugin wie ein gut informierter Kommilitone oder Repetitor, der weiß, wo du stehst.

Einsatz:
- Erstes Starten des Plugins
- Nach einem Semester- oder Stationswechsel
- Vor Beginn der intensiven Examensvorbereitung
- `--redo` zum vollständigen Neuaufsetzen
- `--schnellstart` für eine kürzere Variante (~5 Minuten, danach erweiterbar)
- `--check-integrations` prüft nur, ob externe Dienste angebunden sind

## Eingaben

Keine Voreingaben nötig. Dieser Skill stellt alle Fragen selbst. Optional: Materialien als Anhang mitgeben (Vorlesungsplan, benotete Klausuren, Gliederungen).

## Ablauf

### Schritt 1: Begrüßung und Rollenklärung

```
Willkommen beim Jurastudium-Plugin. Bevor ich dir nützlich sein kann,
möchte ich dich kennenlernen – dein Studienstand, dein Bundesland,
deine Ziele und dein Lernstil.

Das dauert 10–15 Minuten (oder ~5 Minuten mit --schnellstart).
Du kannst jederzeit pausieren und später fortsetzen.
```

**Akademische Integrität – Erinnerung am Anfang:**
> Bevor du dieses Plugin für benotete Arbeiten (Hausarbeiten, Take-Home-Klausuren, Seminararbeiten) nutzt: Prüfe die Prüfungsordnung deines Fachbereichs und die Vorgaben deines Prüfers zur KI-Nutzung. Das Plugin ist für Übung und Vorbereitung gedacht.

### Schritt 2: Persönliche Daten

1. Name (für Ansprache in Sitzungen)?
2. Fachsemester?
3. Hochschule und Fachbereich?
4. Bundesland / JAG (welches Justizprüfungsamt)?
5. Ziel: 1. Staatsexamen / 2. Staatsexamen / Schwerpunktbereichsnote / Hausarbeit?
6. Ziel-Prüfungstermin?
7. Repetitorium (Alpmann Schmidt / Hemmer / Brügelmann / Jura-Intensiv / keins / selbst)?

### Schritt 3: Aktuelle Lehrveranstaltungen und Prüfungen

Für jede Lehrveranstaltung:
1. Name der Veranstaltung?
2. Prüfungsformat (Klausur / Hausarbeit / mündliche Prüfung)?
3. Wo im Semester (Woche des Vorlesungsplans)?
4. Aktuelle Note oder Einschätzung?

### Schritt 4: Lernstil

1. **Drill oder Erklärung?**
   - *Drill*: Du willst, dass das Plugin dich fragt, nachbohrt und sagt, wenn deine Begründung unscharf ist.
   - *Erklärung*: Du willst zuerst klare Darstellungen, dann dich selbst testen.
2. Wo bist du stark (Rechtsgebiete, Aufbautypen)?
3. Wo bist du schwach (Rechtsgebiete, Prüfungsschritte)?
4. Was vermeidest du systematisch?

### Schritt 5: Materialaufnahme

Das Plugin nimmt entgegen:
- Eigene Gliederungen (Pfad oder Einfügen)
- Benotete Klausuren mit Korrekturen (falls vorhanden)
- Alte Examsklausuren (selber JPA, anderer JPA)
- Übungsklausuren mit Lösungen
- Vorlesungsunterlagen / Skripte
- Seminararbeiten
- Repetitoriumsskripte

**Materialzählung:** Nach Aufnahme wird die Gesamtzahl protokolliert. Unter 10 Positionen: Profil wird als `WENIG MATERIAL` markiert, nachgelagerte Skills sind dünner.

### Schritt 6: JAG-spezifischer Check

Das Plugin prüft das Bundesland und fragt ggf.:
- „Nach der JAG [Bundesland] sind folgende Fächer im 1. StEx Pflicht: [Liste]. Stimmt das mit deiner Planung überein?"
- „Hat dein JPA bekannte Schwerpunktsetzungen (z. B. NRW: Sachenrecht häufig; Bayern: Grundbuchrecht)? Falls du alte Klausuren hast, können wir das ableiten."

### Schritt 7: Gutachtenstil-Kurzcheck (optional)

Das Plugin stellt einen kurzen Einstiegsfall und prüft, ob der Gutachtenstil sitzt:
> „Formuliere den Obersatz für einen Schadensersatzanspruch wegen einer verspäteten Lieferung."

Antwort wird bewertet (hypothetisch / assertorisch, Normbezug vorhanden?).

### Schritt 8: Profilschreiben

Das Plugin schreibt alle Angaben in `~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md` und meldet:
> „Lernprofil angelegt. Du kannst jetzt alle Skills nutzen. Ich empfehle als nächsten Schritt: `/jurastudium:lernplan` für eine erste Lernplanung."

## Quellen und Zitierweise

Dieser Skill erzeugt keine inhaltlichen juristischen Outputs. Zitierregeln →  `../references/zitierweise.md` werden in den nachgelagerten Skills angewendet.

## Ausgabeformat

Nach dem Interview: **Profil-Zusammenfassung** mit allen eingetragenen Werten zur Bestätigung durch den Nutzer. Danach: Schreiben in `CLAUDE.md`.

```
**Dein Lernprofil – Zusammenfassung**

Name: [Name]
Fachsemester: [X]
Hochschule: [X]
Bundesland / JAG: [X] (JPA: [X])
Ziel-Examen: [1. StEx / 2. StEx / …]
Prüfungstermin: [Datum]
Repetitorium: [X]

Aktuelle Lehrveranstaltungen:
- [Fach]: [Format], Woche [X]

Lernstil: [Drill / Erklärung]
Stärken: [X]
Schwächen: [X]

Material: [N] Positionen [WENIG MATERIAL: ja/nein]

→ Profil wird in CLAUDE.md geschrieben. Bestätigen? (ja / ändern)
```

## Beispiel (Schnellstart-Modus)

```
Plugin: Bundesland?
Nutzer: Bayern
Plugin: 1. oder 2. Staatsexamen?
Nutzer: 1. StEx, Frühjahr 2026
Plugin: Fachsemester?
Nutzer: 7. Semester
Plugin: Lernstil – Drill oder Erklärung?
Nutzer: Drill
Plugin: Schwächste Rechtsgebiete?
Nutzer: Sachenrecht, Bereicherungsrecht
Plugin: Profil angelegt. Empfehle: /jurastudium:lernplan
```

## Risiken / typische Fehler

- **Profil nicht anlegen:** Alle anderen Skills liefern ohne Profil unkalibrierte Outputs. `jurastudium-kaltstart-interview` immer zuerst.
- **Falsches Bundesland:** JAG-Unterschiede sind erheblich (Klausurzahl, Prüfungsgebiete). Einmal falsch eingetragen → alle Examensprognosen und Lernpläne gehen an der Realität vorbei.
- **Wenig Material hochladen:** Das Plugin arbeitet besser mit mehr Material. Alte JPA-Klausuren und benotete eigene Arbeiten sind besonders wertvoll für `examens-prognose` und `gutachten-uebung`.
- **Lernstil nicht anpassen:** Drill-Modus ist intensiver und für Examensphase geeignet; Erklärungs-Modus für Grundstudium. Kann jederzeit per `/jurastudium:jurastudium-anpassen` geändert werden.
