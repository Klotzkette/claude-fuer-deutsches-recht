---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Fachanwalt Erbrecht."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Erbrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `berater-mehrparteien-konflikt-und-interessen` — Berater Interessen Beweislast Darlegungslast
- `workflow-mandantenkommunikation` — BGB
- `digitaler-nachlass-facebook-bgh-iii-zr-183-17` — Digitaler Nachlass Facebook BGH III ZR 183 17
- `ehegattentestament-bindungswirkung` — Ehegattentestament Bindungswirkung
- `erb-einfuehrung-erbfolge-system` — ERB Einfuehrung Erbfolge Erstgespraech
- `erb-nachlassinventar-erstellung` — ERB Nachlassinventar Pflichtteilsanspruch
- `erbengemeinschaft-blockade-auseinandersetzung` — Erbengemeinschaft Blockade Erstgespraech
- `internationaler-erbfall-eu-erbvo` — Erbfall EU Mandat Triage Pflichtteil Auskunft
- `erbfall-intake-und-nachlassordnung` — Erbfall Intake Erbrecht Erbschein
- `pflichtteilsergaenzung-2325` — Erbrecht Pflichtteilsergaenzung Schenkung
- `erbschein-antrag` — Erbschein Antrag Orientierung
- `erbschein-einziehung-paragraf-2361-bgb-olg-muenchen-31-wx-275-19` — Erbschein Einziehung Paragraf 2361 BGB OLG Muenchen 31 WX 275 19
- `erbverzicht-pflichtteilsverzicht` — Erbverzicht Pflichtteilsverzicht
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Erbrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
