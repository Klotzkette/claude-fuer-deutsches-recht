---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Fachanwalt Insolvenz- und Sanierungsrecht."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Insolvenz Sanierungsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `absonderungsrecht-paragraf-50-inso` — Absonderungsrecht Paragraf 50 Inso
- `anfechtung-vorsatz-paragraf-133-inso-bgh-ix-zr-65-16` — Anfechtung Vorsatz Paragraf 133 Inso BGH IX ZR 65 16
- `eigenverwaltung-schutzschirm-paragraf-270b-inso` — Eigenverwaltung Paragraf 270b und Schutzschirm Paragraf 270d InsO
- `eroeffnung-behoerden-gericht-und-registerweg` — Eroeffnung Fachanwalt FAO Gläubigerantrag
- `fa-inso-sanierung-quellen-edge-case` — FA Inso Sanierung Quellen Edge Case
- `fa-insolvenz-schuldschein-und-lma` — FA Schuldschein
- `glaeubigerantrag` — Gläubigerantrag Insolvenzanfechtung
- `insolvenz-glaeubigerverhandlung-sanierung` — Gläubigerverhandlung Sanierung IDW S6 Krypto
- `insanw-eigenverwaltung-schutzschirm-spezial` — Insanw Eigenverwaltung Konzerninsolvenz
- `einstieg-schnelltriage-fallrouting` — Insanw Fortbestehensprognose
- `insolvenz-tatbestand-beweis-und-belege` — Insolvenz Insolvenzanfechtung Insolvenzrecht
- `insolvenzgeld-paragraf-165-sgb-iii` — Insolvenzgeld Paragraf 165 SGB III
- `insolvenzplan-paragraf-217-inso-bgh-ix-zb-66-19` — Insolvenzplan Paragraf 217 Inso BGH IX ZB 66 19
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Insolvenz Sanierungsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
