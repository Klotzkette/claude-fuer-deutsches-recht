---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fortbestehensprognose** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `annahmen-sammeln-bilanzieller-status-comfortletter-weich` — Annahmen Sammeln Bilanzieller Status Comfortletter Weich
- `comfortletter-sonderfall-edge-forderungsverzicht` — Comfortletter Sonderfall Edge Forderungsverzicht
- `fbp-bankenkommunikation-fbp-integrierte-fbp-stresstest` — Fbp Bankenkommunikation Fbp Integrierte Fbp Stresstest
- `fbp-zahlungsunfaehigkeit-fortbestehensprognose-zusammenfuehren` — Fbp Zahlungsunfaehigkeit Fortbestehensprognose Zusammenfuehren
- `fortbestehensdokumentation-insolvenzrecht-fortbestehensprognose` — Fortbestehensdokumentation Insolvenzrecht Fortbestehensprognose
- `fortbestehensprognose-kaltstart-interview` — Fortbestehensprognose Kaltstart Interview
- `fp-gerichtsfaehigkeit-fp-einfuehrung-fp-zeitraum` — Fp Gerichtsfaehigkeit Fp Einfuehrung Fp Zeitraum
- `gesellschafterdarlehen-rangruecktritt-liquiditaet-monate` — Gesellschafterdarlehen Rangruecktritt Liquiditaet Monate
- `liquiditaet-patronatserklaerung-interessen-plausibilisierung` — Liquiditaet Patronatserklaerung Interessen Plausibilisierung
- `negativer-fristennotiz-ausloesendes-ereignis-forderungsverzicht` — Negativer Fristennotiz Ausloesendes Ereignis Forderungsverzicht
- `prognose-stichtag-stundungsanfrage-glaeubiger-annahmen` — Prognose Stichtag Stundungsanfrage Glaeubiger Annahmen
- `rangruecktritt-sanierungsbausteine-selbstdokumentation` — Rangruecktritt Sanierungsbausteine Selbstdokumentation
- `sanierungsbausteine-vorschlagen-annahmen-bilanzstatus` — Sanierungsbausteine Vorschlagen Annahmen Bilanzstatus

## Arbeitsweg

- Ergebnis sichten: Welche Fortbestehensprognose-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fortbestehensprognose StaRUG/InsO.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 43 GmbHG
- § 3a EStG
- § 102 StaRUG
- § 266a StGB
- § 1 StaRUG
- § 93 AktG
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG
- § 16 HRG
- § 70 VwG

### Leitentscheidungen

- BGH II ZR 296/05
- BGH IX ZR 285/14
- BGH IX ZR 56/22
- BGH II ZR 206/22
- BGH IV ZR 66/25

