---
name: rmap-tatbestand-und-rechtsfolge
description: "Knotenmodellierung in der Rulemap: jeden Tatbestand als prüfbare Bedingung; jede Rechtsfolge als Aktionsknoten. Konjunktion; Disjunktion; Negation; Schwellenwerte sauber abbilden. Output Tatbestands-Rechtsfolge-Liste mit Knoten-IDs; Datentypen und Prüfnotizen. Anschluss legw-rmap-verweisungen-u..."
---

# Tatbestand und Rechtsfolge als Knoten modellieren

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Konkrete Normfassung
- Ergebnis aus legw-rmap-norm-zu-rulemap (Capture)

## Kern der Methode

Jeder Tatbestand wird zum prüfbaren Bedingungsknoten mit klarem Datentyp (boolean; Schwellenwert; Datum; Aufzaehlung). Jede Rechtsfolge wird zum Aktionsknoten mit eindeutigem Effekt (Bewilligung; Versagung; Auflage; Frist setzen). Konjunktion (und); Disjunktion (oder); Negation; Vergleichsoperator werden explizit gemacht; nicht durch Sprache verschleiert.

## Prüfpunkte

Prüfen: ist jede Voraussetzung als eigener Knoten modelliert? Sind unbestimmte Rechtsbegriffe (zumutbar; angemessen; ueberwiegendes Interesse) entweder konkretisiert oder als gesonderter Beurteilungsknoten markiert?

## Normenanker

Arbeitsfokus: **Tatbestand und Rechtsfolge als Knoten modellieren**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 20 Abs. 3 GG` — Gesetzesbindung.
- `Art. 76 Abs. 1 GG` — Gesetzesinitiative.
- `Art. 77 Abs. 1 GG` — Gesetzesbeschluss.
- `Art. 80 Abs. 1 GG` — Verordnungsermächtigung.
- `Art. 84 Abs. 1 GG` — Verwaltungsvollzug.
- `§ 42 Abs. 1 GGO` — Gesetzgebungsvorhaben.
- `§ 43 Abs. 1 GGO` — Ressortabstimmung.
- `§ 44 Abs. 1 GGO` — Gesetzesfolgen.
- `§ 45 GGO` — Beteiligung.
- `§ 46 GGO` — Rechtsförmlichkeit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Prüfung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur für Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.
