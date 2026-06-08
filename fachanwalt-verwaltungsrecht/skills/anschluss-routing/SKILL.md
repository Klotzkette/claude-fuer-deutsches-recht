---
name: anschluss-routing
description: "Anschluss-Routing für Fachanwalt Verwaltungsrecht: wählt den nächsten Spezial-Skill nach Engpass (§ 74 VwGO Klagefrist 1 Mon., Verwaltungsakt, Widerspruchsbescheid, Klageschrift), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Verwaltungsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `amtshaftung-paragraf-839-bgb-art-34-gg` — Amtshaftung Paragraf 839 BGB ART 34 GG
- `anfechtungs-eilrechtsschutz-abs` — Anfechtungs Eilrechtsschutz ABS
- `anhoerung-paragraf-28-vwvfg` — Anhoerung Paragraf 28 Vwvfg
- `anordnung-quellenkarte` — Anordnung Quellenkarte
- `drittanfechtung` — Drittanfechtung
- `eilrechtsschutz-paragraf-80-vwgo` — Eilrechtsschutz Paragraf 80 Vwgo
- `einstweilige-fachanwalt-kanzlei` — Einstweilige Fachanwalt Kanzlei
- `ermessen-paragraf-40-vwvfg` — Ermessen Paragraf 40 Vwvfg
- `erstgespraech-mandatsannahme-fa-vwgo` — Erstgespraech Mandatsannahme FA Vwgo
- `fa-verwaltungsrecht-mandant-redteam-gate` — FA Verwaltungsrecht Mandant Redteam Gate
- `fa-verwaltungsrecht-start-chronologie-fristen` — FA Verwaltungsrecht Start Chronologie Fristen
- `klagefrist-paragraf-58-vwgo-bverwg-4-c-1-19` — Klagefrist Paragraf 58 Vwgo Bverwg 4 C 1 19
- `kommunalrecht-paragraf-2-go` — Kommunalrecht Paragraf 2 GO
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Verwaltungsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Verwaltungsrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
