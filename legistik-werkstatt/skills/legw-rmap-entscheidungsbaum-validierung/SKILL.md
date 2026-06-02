---
name: legw-rmap-entscheidungsbaum-validierung
description: "Simulation und Verifikation der Rulemap: Faelle generieren; Pfadabdeckung messen; Soll-Ist-Vergleich gegen juristische Erwartung. Werkzeuge im Rulemap Builder: Capture; Simulate; Verify. Output Validierungsprotokoll mit Pfaddeckung; Trefferquote; offenen Punkten. Anschluss legw-rmap-bestimmtheit-und-justitiabilitaet fuer rechtliche Bewertung der Pfade. Abgrenzung zur klassischen Beweiswuerdigung im Einzelfall."
---

# Entscheidungsbaum-Simulation und Verifikation

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Vollstaendige Rulemap (Knoten; Verweisungen; Ausnahmen)
- Fallkatalog (realistische Sachverhalte und Grenzfaelle)

## Kern der Methode

Validierung ueber drei Achsen: Vollstaendigkeit (jeder Pfad erreichbar); Konsistenz (keine widerspruechlichen Pfade); Korrektheit (juristisch korrekte Ergebnisse). Im Builder werden Faelle simuliert und Entscheidungen automatisch verifiziert.

## Vorgehen

1. Fallkatalog mit realistischen und Grenzfallszenarien aufbauen
2. Simulation laufen lassen; Pfadabdeckung messen
3. Verifikation: jeden Pfad gegen juristische Soll-Antwort spiegeln
4. Abweichungen aufnehmen; in legw-rmap-tatbestand-und-rechtsfolge zurueckspielen
5. Validierungsprotokoll fuer Akte und NKR ablegen

## Pruefpunkte

Pruefen: ist jeder Pfad mindestens einmal gepruefte? Sind systematisch Grenz- und Ausnahmefaelle erfasst? Sind die juristischen Soll-Antworten autorisiert (durch Fachreferat oder externe Begutachtung)?

## Output

```
Skill:              legw-rmap-entscheidungsbaum-validierung
Thema:              Entscheidungsbaum-Simulation und Verifikation
Ergebnis:           <Artefakt gemaess Kern und Vorgehen>
Naechste Skills:    siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur fuer Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.
