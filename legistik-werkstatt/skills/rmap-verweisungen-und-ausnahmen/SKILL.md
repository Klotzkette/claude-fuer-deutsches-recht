---
name: rmap-verweisungen-und-ausnahmen
description: "Verweisungen (statisch; dynamisch; Rueckverweisung) und Ausnahmen in der Rulemap sauber modellieren. Verkettung von Normen ueber Subrulemaps; Verweisungsketten dokumentieren; Ausnahmen als eigenstaendige Pfade. Output Verweisungs- und Ausnahmenkarte mit IDs und Pfadtiefen. Anschluss legw-rmap-entscheidungsbaum-validierung für die Pfadpruefung. Abgrenzung zur reinen Texterfassung; Verweisungen werden ausgerollt."
---

# Verweisungen und Ausnahmen in der Rulemap

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Knotenmodell aus legw-rmap-tatbestand-und-rechtsfolge
- Liste der Verweisungen und Ausnahmen aus der Norm

## Kern der Methode

Statische Verweisungen werden direkt aufgeloest. Dynamische Verweisungen (auf jeweils gueltige Fassung) sind als Verweisknoten mit Versionspflege umzusetzen. Rueckverweisungen sind als Schleifenpfade explizit zu markieren und auf Endlichkeit zu pruefen. Ausnahmen sind eigene Pfade; keine versteckten Negationen in Tatbestandsknoten.

## Vorgehen

1. Alle Verweisungen aus dem Normtext extrahieren
2. Statisch vs. dynamisch klassifizieren
3. Subrulemaps für aufgeloeste Verweisungen anlegen
4. Ausnahmen als eigene Pfade modellieren
5. Verweisungs- und Ausnahmenkarte dokumentieren

## Pruefpunkte

Pruefen: gibt es zirkulaere Verweisungen? Welche EU-Vorgaben sind zu verlinken? Sind Ausnahmen verhaeltnismaessig zugeschnitten? Stehen Ausnahmen im Einklang mit Gleichheitssatz und Bestimmtheitsgebot?

## Normenanker

Arbeitsfokus: **Verweisungen und Ausnahmen in der Rulemap**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

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

## Output

```
Skill: legw-rmap-verweisungen-und-ausnahmen
Thema: Verweisungen und Ausnahmen in der Rulemap
Ergebnis: <Artefakt gemaess Kern und Vorgehen>
Naechste Skills: siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur für Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.
