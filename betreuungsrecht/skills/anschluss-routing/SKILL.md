---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Betreuungsrecht."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Betreuungsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `anschluss-router` — Anschluss Router
- `aufgabenkreise-festlegen` — Aufgabenkreise Festlegen
- `bericht-betreuer-betreuerpflichten` — Bericht Betreuer Betreuerpflichten
- `bericht-mandantenkommunikation` — Bericht Mandantenkommunikation
- `betreuer-als-erbe` — Betreuer ALS Erbe
- `betreuer-registrierung` — Betreuer Registrierung
- `betreuer-registrierung-betreuung` — Betreuer Registrierung Betreuung
- `betreuer-zahlen-schwellen-und-berechnung` — Betreuer Zahlen Schwellen und Berechnung
- `betreuer-zahlen-schwellenwerte-berechnung` — Betreuer Zahlen Schwellenwerte Berechnung
- `betreuerpflichten-alltag` — Betreuerpflichten Alltag
- `betreuerpflichten-formular-portal-und-einreichung` — Betreuerpflichten Formular Portal und Einreichung
- `betreuerpflichten-genehmigung-bericht` — Betreuerpflichten Genehmigung Bericht
- `betreuerpflichten-genehmigung-betreuung` — Betreuerpflichten Genehmigung Betreuung
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Normenanker

Arbeitsfokus: **Anschluss-Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 1814 Abs. 1 BGB` — Betreuungsvoraussetzungen.
- `§ 1815 Abs. 1 BGB` — Aufgabenkreis.
- `§ 1816 BGB` — Betreuerauswahl.
- `§ 1821 Abs. 1 BGB` — Wunschbefolgung.
- `§ 1823 BGB` — Vertretungsmacht.
- `§ 274 FamFG` — Beteiligte.
- `§ 278 FamFG` — Anhörung.
- `§ 280 FamFG` — Gutachten.
- `§ 5 BtOG` — Beratung.
- `§ 8 BtOG` — Betreuungsvermeidung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Ergebnis sichten: Welche Betreuungsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
