---
name: legw-rmap-tatbestand-und-rechtsfolge
description: "Knotenmodellierung in der Rulemap: jeden Tatbestand als pruefbare Bedingung; jede Rechtsfolge als Aktionsknoten. Konjunktion; Disjunktion; Negation; Schwellenwerte sauber abbilden. Output Tatbestands-Rechtsfolge-Liste mit Knoten-IDs; Datentypen und Pruefnotizen. Anschluss legw-rmap-verweisungen-und-ausnahmen fuer Sonderkonstellationen und legw-rmap-entscheidungsbaum-validierung fuer die Pruefung der Pfade."
---

# Tatbestand und Rechtsfolge als Knoten modellieren

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Konkrete Normfassung
- Ergebnis aus legw-rmap-norm-zu-rulemap (Capture)

## Kern der Methode

Jeder Tatbestand wird zum pruefbaren Bedingungsknoten mit klarem Datentyp (boolean; Schwellenwert; Datum; Aufzaehlung). Jede Rechtsfolge wird zum Aktionsknoten mit eindeutigem Effekt (Bewilligung; Versagung; Auflage; Frist setzen). Konjunktion (und); Disjunktion (oder); Negation; Vergleichsoperator werden explizit gemacht; nicht durch Sprache verschleiert.

## Vorgehen

1. Tatbestand 1 bis n extrahieren und als Knoten anlegen
2. Rechtsfolgen extrahieren und mit Tatbestaenden verbinden
3. Konjunktionen und Disjunktionen explizit kennzeichnen
4. Datentypen je Knoten festlegen
5. Konfliktfreiheit pruefen; widerspruechliche Pfade ausschliessen

## Pruefpunkte

Pruefen: ist jede Voraussetzung als eigener Knoten modelliert? Sind unbestimmte Rechtsbegriffe (zumutbar; angemessen; ueberwiegendes Interesse) entweder konkretisiert oder als gesonderter Beurteilungsknoten markiert?

## Output

```
Skill:              legw-rmap-tatbestand-und-rechtsfolge
Thema:              Tatbestand und Rechtsfolge als Knoten modellieren
Ergebnis:           <Artefakt gemaess Kern und Vorgehen>
Naechste Skills:    siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur fuer Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.
