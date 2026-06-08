---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fluggastrechte** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `abtretung-an-fluggastportal-spezial` — Abtretung An Fluggastportal Spezial
- `airline-bonitaet-und-vollstreckung` — Airline Bonitaet Und Vollstreckung
- `airline-standardausreden-annullierung-verspaetung-anschlussflug` — Airline Standardausreden Annullierung Verspaetung Anschlussflug
- `airline-standardausreden-pruefen` — Airline Standardausreden Prüfen
- `allgemein-anschluss-router-workflow-chronologie` — Allgemein Anschluss Router Chronologie
- `annullierung-oder-verspaetung-einordnen` — Annullierung Oder Verspaetung Einordnen
- `anschlussflug-und-reiseplan` — Anschlussflug Und Reiseplan
- `ausnahmen-aussergewoehnliche-aussergewoehnliche-umstaende` — Ausnahmen Aussergewoehnliche Aussergewoehnliche Umstaende
- `ausnahmen-aussergewoehnliche-umstaende-pruefen` — Ausnahmen Aussergewoehnliche Umstaende Prüfen
- `aussergewoehnliche-distanz-interessen-erfassen` — Aussergewoehnliche Distanz Interessen Erfassen
- `aussergewoehnliche-umstaende-strikt` — Aussergewoehnliche Umstaende Strikt
- `distanz-und-ausgleich-berechnen` — Distanz Und Ausgleich Berechnen
- `flug-anschlussflug-codeshare-anspruch-uebersicht` — Flug Anschlussflug Codeshare Anspruch Uebersicht
- `flug-anschlussflug-codeshare-spezial` — Flug Anschlussflug Codeshare Spezial

## Arbeitsweg

- Ergebnis sichten: Welche Fluggastrechte-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?


## Normen & Rechtsprechung

Konkret zu prüfen:

- VO (EG) Nr. 261/2004 (Fluggastrechte)
- Art. 5 VO 261/2004 (Annullierung)
- Art. 6 VO 261/2004 (Verspätung)
- Art. 7 VO 261/2004 (Ausgleichszahlung 250/400/600 EUR)
- EuGH C-402/07 (Sturgeon)
## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fluggastrechte VO 261/2004.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
