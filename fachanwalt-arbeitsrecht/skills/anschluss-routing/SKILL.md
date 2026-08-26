---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Fachanwalt Arbeitsrecht."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Arbeitsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `abmahnung-loeschung-personalakte-bag-2-azr-782-11` — Abmahnung Loeschung Personalakte BAG 2 AZR 782 11
- `aktenzeichen-fehlerkatalog` — Aktenzeichen Fehlerkatalog
- `ar-aufhebungsvertrag-praxis` — AR Aufhebungsvertrag Konkurrenzklausel
- `ar-betriebsuebergang-spezial` — AR Betriebsuebergang Spezial Einfuehrung
- `einstieg-schnelltriage-fallrouting` — AR Kuendigungspruefung Fazugang Arbeitgeber
- `vergleich-arbeitsgericht-abrechnung` — Arbeitsgericht Abrechnung
- `aufhebungsvertrag-faires-verhandeln-bag-6-azr-333-21` — Aufhebungsvertrag Faires Verhandeln BAG 6 AZR 333 21
- `bag-mindesturlaub-kein-verzicht` — BAG
- `befristung-compliance-dokumentation-und-akte` — Befristung FAO Unwirksam Fristennotiz
- `befristung-tzbfg` — Befristung Tzbfg BEM Verfahren Fazugang
- `beteiligung-betriebsrat-102-betrvg` — Beteiligung Betriebsrat Erstgespraech
- `betriebsrat-zahlen-schwellen-und-berechnung` — Betriebsrat BETRVG Datum
- `betriebsratswahl-anfechtung-leiharbeit-bag-7-abr-4-21` — Betriebsratswahl Anfechtung Leiharbeit BAG 7 ABR 4 21
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Arbeitsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
