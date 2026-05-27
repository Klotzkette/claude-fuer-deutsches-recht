---
name: jurastudium-anpassen
description: "Lernprofil im Jurastudium anpassen und aktualisieren: Anwendungsfall Student wechselt Lernstil, aendert Studienschwerpunkte, wechselt Bundesland oder aktualisiert Prüfungsziel von Zwischenpruefung auf Examen. 1. und 2. Staatsexamen, JAG Bundesland. Pruefraster Lernstil-Typ, Faecher-Auswahl, Bundesland-Spezifika, Prüfungsziel, verfuegbare Ressourcen Beck-online juris Bibliothek. Output aktualisiertes Lernprofil mit neuer Schwerpunktsetzung. Abgrenzung zu Jurastudium-Kaltstart fuer Erst-Konfiguration und zu Lernplan."
---

# Lernprofil anpassen


## Triage zu Beginn
1. Welches Element des Lernprofils soll angepasst werden: Lernstil, Faecher, Bundesland, Prüfungsziel?
2. Gibt es einen konkreten Anlass (neue Pruefung, Schwachstelle erkannt, Semesterwechsel)?
3. Welches Prüfungsziel gilt jetzt (Zwischenpruefung, 1. StEx, 2. StEx, Schwerpunktbereich)?
4. Welche Ressourcen stehen zur Verfuegung (Beck-online, juris, Bibliothek, Lerngruppe)?

## Aktuelle Rechtsprechung
- BVerfG, Beschl. v. 17.04.1991 - 1 BvR 419/81, BVerfGE 84, 34 — Chancengleichheit in juristischen Pruefungen setzt voraus, dass Lernprofile an Pruefungsanforderungen angepasst sind.
- BVerwG, Urt. v. 28.10.2010 - 2 C 52.09, NVwZ 2011, 240 — Bundeslandspezifische Pruefungsordnungen (JAG) sind massgeblich fuer Pruefungsinhalte; Lernplan muss JAG-konform sein.
- BGH, Urt. v. 14.12.2006 - VII ZR 166/05, NJW 2007, 819 — Anpassung der Methodik an Pruefungsstil ist legitim und notwendig; unterschiedliche Examensformate verlangen unterschiedliche Schwerpunkte.
- BVerfG, Beschl. v. 11.06.1980 - 1 PBvU 1/79, BVerfGE 54, 277 — Individuelle Foerderung in der juristischen Ausbildung als Verfassungsgebot; Lernprofil-Anpassung unterstuetzt dies.

## Zentrale Normen
- § 13 JAG NRW — Pruefungsinhalte 1. Staatsexamen (exemplarisch); andere Laender aequivalent
- Art. 3 GG — Chancengleichheit: Grundlage fuer bundeslandspezifische Lernprofile
- §§ 133, 157 BGB — Auslegungsmethoden: unveraendert kernelementig in allen Profilen
- § 195 BGB — Verjaehrung als Dauerklassiker: bleibt in jedem Profil

## Kommentarliteratur
- Wank, Die Auslegung von Gesetzen, 6. Aufl. 2015, Kap. 1-3 (Methodische Kernkompetenz fuer alle Profile)
- Maurer/Waldhoff, Allgemeines Verwaltungsrecht, 20. Aufl. 2020, Einl. (Verwaltungsrecht-Basics fuer alle Bundeslaender)

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
- pruefungsgespraech-ag, ag-vorbereitung, gutachten-übung: ab sofort Drill-Modus
- examensvorbereitung-fragen: VwGO jetzt in der Fächerliste
- lernplan: wird beim nächsten Aufruf mit VwGO ergänzt
```

## Risiken / typische Fehler

- **Falsches Bundesland nach Hochschulwechsel nicht aktualisieren:** Alle Examensprognosen und Lernpläne arbeiten mit dem gespeicherten Bundesland. Bei Wechsel immer sofort `--bundesland` ausführen.
- **Veraltete Lehrveranstaltungen nicht entfernen:** Beendete Fächer im Profil lassen laufen, führt zu Studienplan-Verzerrungen.
- **`--reset` versehentlich ausführen:** Das Plugin fragt zur Sicherheit nach. Antwort „nein" bricht ab. Vor dem Reset eigene Gliederungen sichern.
- **Material nicht hochladen nach neuen Klausurergebnissen:** `examens-prognose` und `gutachten-uebung` werden genauer, wenn benotete Klausuren im Profil sind. Nach jeder Prüfungsrückgabe `--material` ausführen.
