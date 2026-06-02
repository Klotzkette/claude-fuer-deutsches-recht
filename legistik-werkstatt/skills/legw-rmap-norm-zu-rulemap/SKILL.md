---
name: legw-rmap-norm-zu-rulemap
description: "Praxisleitfaden Norm in Rulemap ueberfuehren: Capture (Norm erfassen); Model (Logikmodell zeichnen); Simulate (Workflow durchspielen); Verify (Entscheidungen pruefen); Integrate (in System einbinden); Improve (weiterentwickeln). Liefert ein iteratives Vorgehensmodell mit Eingaben; Ausgaben und Pruefpunkten je Schritt. Anschluss legw-rmap-tatbestand-und-rechtsfolge fuer die feine Knotenmodellierung. Abgrenzung zur Textentwurfsarbeit; die Rulemap ist die parallel gepflegte Logikfassung."
---

# Von der Norm zur Rulemap - Vorgehensmodell

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Konkrete Norm oder Normentwurf
- Sachfeld-Kompass aus legw-<ressort>-<thema>
- Begriffsglossar aus legw-rmap-grundlagen

## Kern der Methode

Sechs Schritte des Rulemap Builders nach dem Modell der Rulemapping-Group: Capture; Model; Simulate; Verify; Integrate; Improve. Jeder Schritt produziert ein eigenes Artefakt; alle Artefakte sind versionierbar und im Builder ohne Programmierung pflegbar.

## Vorgehen

1. Capture: Normtext erfassen; Strukturparser anwerfen; Tatbestaende; Rechtsfolgen; Ausnahmen markieren
2. Model: Knoten und Kanten der Rulemap zeichnen; Entscheidungspfade abbilden
3. Simulate: realistische Faelle durchspielen; Pfaddeckung pruefen
4. Verify: automatisierte Entscheidungen gegen juristische Soll-Vorgabe pruefen
5. Integrate: Schnittstelle zur Vollzugs-IT der Verwaltung; ohne Programmierung
6. Improve: Feedback aus Vollzug und Gerichtsbarkeit zurueckspielen; Rulemap iterieren

## Pruefpunkte

Pruefen: ist jede Entscheidungspfad-Variante abgedeckt? Sind Ausnahmen explizit modelliert und nicht implizit? Liegt die Verantwortung fuer die Logik beim Normgeber oder beim IT-Dienstleister?

## Output

```
Skill:              legw-rmap-norm-zu-rulemap
Thema:              Von der Norm zur Rulemap - Vorgehensmodell
Ergebnis:           <Artefakt gemaess Kern und Vorgehen>
Naechste Skills:    siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur fuer Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.
