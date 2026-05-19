---
name: anpassen
description: >
  Lernprofil anpassen: Lernstil wechseln, Fächer aktualisieren, Material
  hinzufügen, Bundesland oder Prüfungsziel ändern. Lade diesen Skill bei
  Anfragen wie „Profil ändern", „Lernstil wechseln", „neues Fach hinzufügen",
  „Bundesland aktualisieren" oder „anpassen".
language: de
argument-hint: "[--lernstil | --bundesland | --fach | --material | --reset]"
triggers:
  - "profil ändern"
  - "lernstil wechseln"
  - "fach hinzufügen"
  - "bundesland aktualisieren"
  - "anpassen"
  - "einstellungen"
---

# Lernprofil anpassen

## Zweck

Dieser Skill ändert einzelne oder mehrere Einträge im Lernprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md`, ohne das gesamte Kaltstart-Interview erneut zu durchlaufen.

Einsatzbereiche:
- Semesterwechsel (neue Lehrveranstaltungen, neues Prüfungsziel)
- Lernstil wechseln (Drill → Erklärung oder umgekehrt)
- Bundesland / JAG aktualisieren (z. B. nach Hochschulwechsel)
- Neues Material hinzufügen (Klausuren, Gliederungen)
- Schwächen- und Stärkenprofil nach Prüfungsergebnissen anpassen
- `--reset`: vollständiges Löschen des Profils (vor neuem Kaltstart)

## Eingaben

1. **Flag** (optional): `--lernstil`, `--bundesland`, `--fach`, `--material`, `--examen`, `--reset`
2. Ohne Flag: interaktives Menü mit allen anpassbaren Feldern
3. Lernprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md`

## Ablauf

### Ohne Flag: Interaktives Menü

```
Was möchtest du anpassen?
1. Lernstil (aktuell: [Drill / Erklärung])
2. Bundesland / JAG (aktuell: [X])
3. Ziel-Examen und Prüfungstermin (aktuell: [X])
4. Aktuelle Lehrveranstaltungen
5. Schwächen / Stärken
6. Material hinzufügen
7. Repetitorium wechseln
8. Profil vollständig zurücksetzen (--reset)
```

### `--lernstil`

Wechsel zwischen:
- **Drill-Modus:** Sokratisch, kein Vorwegnehmen der Antwort, Nachbohren
- **Erklärungs-Modus:** Erst Erklärung, dann Selbsttest, mehr Gerüst

Gilt sofort für alle nachfolgenden Skills in dieser Sitzung und wird in `CLAUDE.md` gespeichert.

### `--bundesland`

Fragt nach neuem Bundesland und JAG, prüft Konsistenz:
> „Nach dem Wechsel von NRW nach Bayern unterscheiden sich die Prüfungsfächer im 1. StEx. Ich aktualisiere das Profil. Bitte bestätige: [neue Fächerliste nach JAG Bayern]."

### `--fach`

Fügt eine Lehrveranstaltung hinzu oder entfernt sie:
- Name der Veranstaltung
- Prüfungsformat (Klausur / Hausarbeit / mündlich)
- Semesterwoche

### `--material`

Nimmt neues Lernmaterial auf:
- Dateipfad oder Textinhalt (benotete Klausur, Gliederung, JPA-Klausur)
- Aktualisiert den Materialzähler im Profil
- Entfernt `WENIG MATERIAL`-Flag, sobald ≥ 10 Positionen vorhanden

### `--examen`

Aktualisiert Prüfungsziel, Prüfungstermin und Repetitorium.

### `--reset`

Sicherheitsabfrage:
> „Du löschst das gesamte Lernprofil. Diese Aktion ist nicht rückgängig zu machen. Danach musst du kaltstart-interview erneut durchlaufen. Fortfahren? (ja / nein)"

## Quellen und Zitierweise

Dieser Skill ändert nur Konfigurationsdaten. Keine juristischen Inhalte. Zitierregeln → `../references/zitierweise.md` gelten in den inhaltlichen Skills.

## Ausgabeformat

Nach jeder Änderung:

```
**Profil aktualisiert**

Geändert:
- [Feld]: [alter Wert] → [neuer Wert]

Nicht geändert:
- [Feld]: [aktueller Wert] (unverändert)

Gespeichert in: ~/.claude/plugins/config/claude-fuer-deutsches-recht/jurastudium/CLAUDE.md

**Auswirkungen auf laufende Skills:**
- lernplan: [wird beim nächsten Aufruf mit neuen Daten neu berechnet]
- examens-prognose: [aktualisiert Prüfungsgebietsliste nach neuer JAG]
- examensvorbereitung-fragen: [neue Bundesland-Filterung aktiv]
```

## Beispiel

**Anfrage:** „Ich habe jetzt auch VwGO als Pflichtfach und möchte auf Drill-Modus wechseln."

**Ausgabe:**

```
Profil aktualisiert:
- Lernstil: Erklärung → Drill
- Lehrveranstaltungen: VwGO-Klausur (Klausur, Woche 1) hinzugefügt

Auswirkungen:
- sokratisches-drillen, ag-vorbereitung, gutachten-uebung: ab sofort Drill-Modus
- examensvorbereitung-fragen: VwGO jetzt in der Fächerliste
- lernplan: wird beim nächsten Aufruf mit VwGO ergänzt
```

## Risiken / typische Fehler

- **Falsches Bundesland nach Hochschulwechsel nicht aktualisieren:** Alle Examensprognosen und Lernpläne arbeiten mit dem gespeicherten Bundesland. Bei Wechsel immer sofort `--bundesland` ausführen.
- **Veraltete Lehrveranstaltungen nicht entfernen:** Beendete Fächer im Profil lassen laufen, führt zu Studienplan-Verzerrungen.
- **`--reset` versehentlich ausführen:** Das Plugin fragt zur Sicherheit nach. Antwort „nein" bricht ab. Vor dem Reset eigene Gliederungen sichern.
- **Material nicht hochladen nach neuen Klausurergebnissen:** `examens-prognose` und `gutachten-uebung` werden genauer, wenn benotete Klausuren im Profil sind. Nach jeder Prüfungsrückgabe `--material` ausführen.
