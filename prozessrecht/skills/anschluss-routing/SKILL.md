---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Prozessrecht."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Prozessrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `amtlicher-zpo-proz-bauleiter-eilverfahren` — Amtlicher ZPO Proz Bauleiter Eilverfahren
- `anspruchstabelle-beweislast` — Anspruchstabelle Beweislast
- `anspruchstabelle-gegenseite-interessen` — Anspruchstabelle Gegenseite Interessen
- `anwaltsgeheimnis-pruefung` — Anwaltsgeheimnis Prüfung
- `argumentationsverbesserung-red-team` — Argumentationsverbesserung RED Team
- `beweissicherung-einstweilige-verfuegung` — Beweissicherung Einstweilige Verfuegung
- `chronologie` — Chronologie
- `eilverfahren-risikoampel-und-gegenargumente` — Eilverfahren Risikoampel und Gegenargumente
- `einstweilige-verfuegung` — Einstweilige Verfuegung
- `gegenseite-mehrparteien-konflikt-und-interessen` — Gegenseite Mehrparteien Konflikt und Interessen
- `gegenseite-status-mahnbescheid-mahnschreiben` — Gegenseite Status Mahnbescheid Mahnschreiben
- `kaltstart-interview` — Kaltstart Interview
- `mahnbescheid` — Mahnbescheid
- `kostenfeststellungsklage-verzugsschaden-erledigung` — Zahlung, Aufrechnung, dauernde Einrede, Unmöglichkeit oder Wegfall des Rechtsschutzbedürfnisses nach Klageeinreichung; prüft Paragraf 91a ZPO, Paragraf 269 Abs. 3 Satz 3 ZPO und materiellen Kostenerstattungsanspruch als Verzugsschaden.
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Prozessrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
