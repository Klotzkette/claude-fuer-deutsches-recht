---
name: einstieg-routing
description: "Einstieg, Triage und Routing für DFG-Förderantrag: ordnet Rolle (Antragsteller, DFG-Gutachter, Universitätsleitung), markiert Frist (Antragsfrist Ausschreibungstermin), wählt Norm (DFG-Verwendungsrichtlinien, Wissenschaftsfreiheit Art. 5 III GG) und Zuständigkeit (Deutsche Forschungsgemeinschaft), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Dfg Foerderantrag** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `adaptive-dokumentenmatrix-lueckenliste` — Adaptive Dokumentenmatrix Lueckenliste
- `adaptive-dokumentenmatrix-und-lueckenliste` — Adaptive Dokumentenmatrix und Lueckenliste
- `anfaenger-antraege-dfg` — Anfaenger Antraege DFG
- `anfaenger-risikoampel-gegenargumente` — Anfaenger Risikoampel Gegenargumente
- `antraege-zahlen-schwellen-und-berechnung` — Antraege Zahlen Schwellen und Berechnung
- `antraege-zahlen-schwellenwerte-berechnung` — Antraege Zahlen Schwellenwerte Berechnung
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `dfg-bis-200k-begutachtung-light` — DFG BIS 200k Begutachtung Light
- `dfg-eigenanteil-und-grundausstattung` — DFG Eigenanteil und Grundausstattung
- `dfg-eigene-vorarbeiten-darstellen` — DFG Eigene Vorarbeiten Darstellen
- `dfg-erstantragsteller-besondere-checks` — DFG Erstantragsteller Besondere Checks
- `dfg-erstpruefung-und-mandatsziel` — DFG Erstpruefung und Mandatsziel
- `dfg-finanzplan-module-personal-geraete` — DFG Finanzplan Module Personal Geraete
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Regelungs- und Quellenanker

Arbeitsfokus: **Einstieg und Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 91b Abs. 1 GG` — Forschungsförderung im Bund-Länder-System.
- `§ 23 BHO` — Zuwendungsvoraussetzungen.
- `§ 44 Abs. 1 BHO` — Bewilligung, Nachweis und Prüfung.
- `§ 7 Abs. 1 BHO` — Wirtschaftlichkeit und Sparsamkeit.
- `§ 48 Abs. 1 VwVfG` — Rücknahme rechtswidriger Bewilligungen.
- `§ 49 Abs. 1 VwVfG` — Widerruf rechtmäßiger Bewilligungen.
- `DFG-Kodex Leitlinie 1` — Redlichkeit.
- `DFG-Kodex Leitlinie 7` — Qualitätssicherung.
- `DFG-Kodex Leitlinie 14` — Autorschaft.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Dfg Foerderantrag sind DFG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei DFG-Förderantrag typische Eskalationsstufen: Projektbeschreibung, Finanzierungsplan, Begründung Personalbedarf.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
