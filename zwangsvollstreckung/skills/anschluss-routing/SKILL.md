---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Zwangsvollstreckung** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `bank-haertefall-inso` — Bank Haertefall Inso
- `kontenpfaendung-notar-interessen-online` — Kontenpfaendung Notar Interessen Online
- `mahnbescheid-fristennotiz-zv-titel-zv-kontensuche` — Mahnbescheid Fristennotiz Zv Titel Zv Kontensuche
- `pfueb-raeumung-schuldnerschutz-beweislast` — Pfueb Raeumung Schuldnerschutz Beweislast
- `vermoegensauskunft-vollstreckungsbescheid-vollstreckungstitel` — Vermoegensauskunft Vollstreckungsbescheid Vollstreckungstitel
- `zpo-zwangsvollstreckung-zv-abwehr` — Zpo Zwangsvollstreckung Zv Abwehr
- `zv-elektronische-zv-eu-zv` — Zv Elektronische Zv Eu Zv
- `zv-mahnbescheid-zv-mobiliar-zv-notarielle` — Zv Mahnbescheid Zv Mobiliar Zv Notarielle
- `zv-pfaendungstabelle-zv-pfueb-zv-pfueb` — Zv Pfaendungstabelle Zv Pfueb Zv Pfueb
- `zv-pfueb-802l-arbeit` — Zv Pfueb 802l Arbeit
- `zv-raeumung-zv-tabellenauszug-zv-vermoegensauskunft` — Zv Raeumung Zv Tabellenauszug Zv Vermoegensauskunft
- `zv-vollstreckungsbescheid-zv-vollstreckungsschutz-zv-zvg` — Zv Vollstreckungsbescheid Zv Vollstreckungsschutz Zv Zvg
- `zwv-pfaendung-konto-vollstreckungsschutz-billigkeit` — Zwv Pfaendung Konto Vollstreckungsschutz Billigkeit

## Arbeitsweg

- Ergebnis sichten: Welche Zwangsvollstreckung-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Zwangsvollstreckung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
