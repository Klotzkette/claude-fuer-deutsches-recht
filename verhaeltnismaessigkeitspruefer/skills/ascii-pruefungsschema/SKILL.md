---
name: ascii-pruefungsschema
description: ASCII-Pruefungsschema fuer die vierstufige Verhaeltnismaessigkeitspruefung mit Box-Drawing fuer Sequenzen Abzweige und Ampelstatus. Mit Vorlage fuer Schriftsatzanlage Klausurausarbeitung und Mandatsmemo.
---

## Aufgabe

Eine reine Text-Visualisierung der vier Pruefungsstufen mit Ampelstatus.
Brauchbar fuer Schriftsatzanlagen, Klausuren und Mandatsmemos.

## Schema 1: Sequenz

```
+----------------------------------------+
| 1 Legitimer Zweck                      |
| Frage: Welcher Zweck wird verfolgt?    |
| Schrankentyp:                          |
| Status:  [+]  Erfuellt                 |
+--------------------+-------------------+
                     v
+----------------------------------------+
| 2 Geeignetheit                         |
| Frage: Foerdert Mittel den Zweck?      |
| Kontrolldichte:                        |
| Status:  [+]  Erfuellt                 |
+--------------------+-------------------+
                     v
+----------------------------------------+
| 3 Erforderlichkeit                     |
| Frage: Gibt es milderes gleich         |
|        effektives Mittel?              |
| Alternativen geprueft: 3               |
| Status:  [~]  Wertungsoffen            |
+--------------------+-------------------+
                     v
+----------------------------------------+
| 4 Angemessenheit                       |
| Eingriff vs Zweck                      |
| Absolute Grenzen geprueft              |
| Status:  [-]  Eingriff zu schwer       |
+----------------------------------------+
                     v
            ERGEBNIS: Verstoss
```

## Schema 2: Abzweige bei verfassungsimmanenter Schranke

```
+----------------+----------------------+
| Grundrecht     | vorbehaltlos?        |
+----------------+----------------------+
                       v Ja
+----------------------------------------+
| Verfassungsgut mit Rang als Schranke?  |
+----------------------------------------+
                       v
+----------------------------------------+
| Praktische Konkordanz pruefen          |
+----------------------------------------+
```

## Statussymbole

- [+]  Stufe ohne Probleme erfuellt
- [~]  Wertungsoffen mit Argumenten
- [-]  Stufe scheitert
- [!]  Absolute Grenze beruehrt (Wuerde, Wesensgehalt, Existenzminimum)

## Anwendung

- Anlage zum Schriftsatz, eingerueckt mit Monospace-Schrift.
- Klausurbeilage bei Fortgeschrittenenpruefung.
- Mandatsmemo als Quick-Overview.

## Output

Reines ASCII; keine Bilder, keine Mermaid-Syntax. Direkt einsetzbar
in jeder Textdatei.
