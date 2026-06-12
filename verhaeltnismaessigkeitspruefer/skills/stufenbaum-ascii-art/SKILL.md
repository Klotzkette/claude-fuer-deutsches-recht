---
name: stufenbaum-ascii-art
description: "ASCII-Stufenbaum der Verhältnismäßigkeitspruefung zum Ausdrucken und Mitschreiben. Visualisiert die Vorpruefung Schutzbereich-Eingriff-Schranke, die vier Stufen Zweck/Geeignet/Erforderlich/Angemessen und die absoluten Grenzen Wuerde, Wesensgehalt, Existenzminimum."
---

# Stufenbaum als ASCII-Visualisierung

> Komprimierte Sichtbarmachung des gesamten Prüfungsaufbaus. Druckbar, in Schriftsaetze einklebbar, zur Tafelarbeit verwendbar.

## Vollbaum

```
                  +-----------------------------------+
                  |  GRUNDRECHTSPRUEFUNG               |
                  +-----------------------------------+
                                |
                                v
 +-----------------------------+------------------------------+
 |  Vorpruefung                                               |
 |   1. Schutzbereich eroeffnet? (persoenlich + sachlich)      |
 |   2. Eingriff (klassisch oder modern)?                     |
 |   3. Schranke vorhanden (Vorbehalt oder verfassungsimm.)?  |
 +-----------------------------+------------------------------+
                                |
                                v
 +-----------------------------+------------------------------+
 |  Formelle Verfassungsmaessigkeit                            |
 |   - Kompetenz, Verfahren, Form                              |
 |   - Bestimmtheit / Normklarheit                             |
 |   - Wesentlichkeitstheorie / Parlamentsvorbehalt            |
 |   - Zitiergebot Art 19 I 2 GG                               |
 +-----------------------------+------------------------------+
                                |
                                v
 +-----------------------------+------------------------------+
 |  Materielle Verfassungsmaessigkeit: Schranken-Schranke      |
 +-----------------------------+------------------------------+
                                |
                                v
            +-------------------+-------------------+
            |                                       |
   +--------+--------+                     +--------+--------+
   | Stufe 1         |                     | Stufe 2         |
   | Legitimer Zweck |                     | Geeignetheit    |
   +--------+--------+                     +--------+--------+
            |                                       |
            +-------------------+-------------------+
                                |
                                v
            +-------------------+-------------------+
            |                                       |
   +--------+--------+                     +--------+--------+
   | Stufe 3         |                     | Stufe 4         |
   | Erforderlichkeit|                     | Angemessenheit  |
   +--------+--------+                     +--------+--------+
            |                                       |
            +-------------------+-------------------+
                                |
                                v
 +-----------------------------+------------------------------+
 |  Absolute Grenzen (Pruefung endet hier, wenn verletzt)      |
 |   * Menschenwuerde Art 1 I GG (Objektformel)                |
 |   * Wesensgehalt Art 19 II GG (Kernbereich)                 |
 |   * Existenzminimum Art 1 I iVm Art 20 I GG                 |
 +-----------------------------+------------------------------+
                                |
                                v
                  +-----------------------------------+
                  |  Ergebnis: verfassungsmaessig?     |
                  +-----------------------------------+
```

## Kurzbaum für Schriftsaetze

```
[Schutzbereich] -> [Eingriff] -> [Schranke]
    -> [Bestimmtheit/Wesentlichkeit/Zitiergebot]
    -> [Zweck] -> [Geeignet] -> [Erforderlich] -> [Angemessen]
    -> [Absolute Grenzen]
    -> [Ergebnis]
```

## Pfeilbaum für Tafelarbeit

```
+ Eingriffsmassnahme ?
|
+--- Schutzbereich beruehrt ?
|       +--- nein  -> Pruefung endet
|       +--- ja    -> weiter
|
+--- Eingriff ?
|       +--- nein  -> Pruefung endet
|       +--- ja    -> weiter
|
+--- Schranke einschlaegig ?
|       +--- vorbehaltlos -> verfassungsimmanente Schranke ?
|       +--- einfach      -> jedes verf.maessige Gesetz
|       +--- qualifiziert -> nur fuer genannte Zwecke
|
+--- Bestimmtheit / Wesentlichkeit / Zitiergebot ?
|       +--- nein -> verfassungswidrig
|       +--- ja   -> weiter
|
+--- Stufen 1-4 ?
|       +--- Zweck            -> legitim ?
|       +--- Geeignet         -> foerdert Zweck ?
|       +--- Erforderlich     -> milderes Mittel ?
|       +--- Angemessen       -> Abwaegung ?
|
+--- Absolute Grenzen ?
|       +--- Wuerde / Wesensgehalt / Existenzminimum
+--- Ergebnis
```

## Verwendung

- In Schriftsaetzen vor dem Prüfungsteil als Leitfaden einklappen.
- In Klausuren als interne Gliederungshilfe (nicht in den Prüfungsteil kopieren).
- In Schulungen als Tafelbild mit ergaenzenden Fall-Notizen.

## Verwandt

- `mermaid-flowchart-pruefung` für die Mermaid-Version.
- `ascii-pruefungsschema` für die kompakte Tabellenvariante.
- `padlet-vier-stufen-tafel` für kollaborative Tafelarbeit.
