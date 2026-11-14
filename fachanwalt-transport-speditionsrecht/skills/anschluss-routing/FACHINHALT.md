---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Fachanwalt Transport Speditionsrecht."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Transport Speditionsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `transport-autonome-lkw-konvois-haftung-1d-stvg` — Autonome LKW CMR Schadensregulierung
- `cmr-haftung-art-17-cmr` — CMR Haftung ART 17 CMR
- `cmr-haftung` — CMR Haftung Ladungsschaden
- `cotif-schriftsatz-brief-und-memo-bausteine` — Cotif Fachanwalt Haager
- `workflow-mandantenkommunikation` — FA Transport Spedition Mandant Redteam
- `einstieg-schnelltriage-fallrouting` — FA Transport Spedition Start Chronologie Fristen
- `frachtfuehrerhaftung-paragraf-425-hgb` — Frachtfuehrerhaftung Paragraf 425 HGB
- `gefahrgut-adr-paragraf-9-gefstoffvo` — Gefahrgut ADR Paragraf 9 Gefstoffvo
- `hgb-dokumentenmatrix-und-lueckenliste` — HGB Kabotage Beweislast Kanzlei RED Team Korrektur
- `ladungsschaden-art-23-cmr` — Ladungsschaden ART 23 CMR
- `lieferverzug` — Lieferverzug Orientierung Mandat Triage
- `luftfracht-monteral-uebereinkommen` — Luftfracht Monteral Uebereinkommen
- `marktzugang-sonderfall-edge-case` — Marktzugang Sonderfall Montrealer
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Transport Speditionsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
