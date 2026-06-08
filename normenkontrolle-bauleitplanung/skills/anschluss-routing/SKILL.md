---
name: anschluss-routing
description: "Anschluss-Routing für Normenkontrolle Bauleitplanung: wählt den nächsten Spezial-Skill nach Engpass (§ 47 II VwGO 1 Jahr ab Bekanntmachung, Bebauungsplan, Begründung, Abwägungsmaterial), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Normenkontrolle Bauleitplanung** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `abwaegung-formular-portal` — Abwaegung Formular Portal
- `abwaegung-formular-portal-und-einreichung` — Abwaegung Formular Portal und Einreichung
- `abwaegungsgebot-1-abs-7-baugb` — Abwaegungsgebot 1 ABS 7 Baugb
- `anfechtung-antragsbefugnis-red-team-korrektur` — Anfechtung Antragsbefugnis RED Team Korrektur
- `anfechtung-tatbestandsmerkmale` — Anfechtung Tatbestandsmerkmale
- `anpassungsgebot-flaechennutzungsplan` — Anpassungsgebot Flaechennutzungsplan
- `antragsbefugnis-eigentuemer-nachbar` — Antragsbefugnis Eigentuemer Nachbar
- `antragsbefugnis-fehlerkatalog` — Antragsbefugnis Fehlerkatalog
- `antragsbefugnis-red-team-und-qualitaetskontrolle` — Antragsbefugnis RED Team und Qualitaetskontrolle
- `antragstellervertretung-zahlen-schwellen-und-berechnung` — Antragstellervertretung Zahlen Schwellen und Berechnung
- `artenschutz-naturschutz-aufstellungsbeschluss` — Artenschutz Naturschutz Aufstellungsbeschluss
- `artenschutz-naturschutz-planung` — Artenschutz Naturschutz Planung
- `aufstellungsbeschluss-bekanntmachung` — Aufstellungsbeschluss Bekanntmachung
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Normenkontrolle Bauleitplanung-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Normenkontrolle Bauleitplanung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
