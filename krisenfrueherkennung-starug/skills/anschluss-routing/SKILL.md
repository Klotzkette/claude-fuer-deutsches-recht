---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Krisenfrueherkennung Starug** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `berater-drohende-fruehwarnsystem` — Berater Drohende Fruehwarnsystem
- `drohende-zahlungsunfaehigkeit-fortbestehensprognose-zweistufig` — Drohende Zahlungsunfaehigkeit Fortbestehensprognose Zweistufig
- `integrierte-interessen-kennzahlenset-mandantenentscheidung` — Integrierte Interessen Kennzahlenset Mandantenentscheidung
- `integrierte-planung-kennzahlenset-ampelsystem-kfe` — Integrierte Planung Kennzahlenset Ampelsystem Kfe
- `kfe-krisenstab-cross-class-dokumentationspflicht-protokollierung` — Kfe Krisenstab Cross Class Dokumentationspflicht Protokollierung
- `kfe-restrukturierungsbeauftragter-stabilisierungsanordnung` — Kfe Restrukturierungsbeauftragter Stabilisierungsanordnung
- `krisenfrueherkennung-krisenmanagement-monats` — Krisenfrueherkennung Krisenmanagement Monats
- `krisenstadien-fristennotiz-starug-gf-haftung` — Krisenstadien Fristennotiz Starug Gf Haftung
- `mandantenbrief-warnung-paragraph-starug-warnpflicht` — Mandantenbrief Warnung Paragraph Starug Warnpflicht
- `pflicht-planung-restrukturierungsplan` — Pflicht Planung Restrukturierungsplan
- `pflichtenkollision-shift-restructuring-lounge` — Pflichtenkollision Shift Restructuring Lounge
- `restrukturierungsplan-architektur-rollierende` — Restrukturierungsplan Architektur Rollierende
- `stabilisierungsanordnung-vollstreckungssperre` — Stabilisierungsanordnung Vollstreckungssperre

## Arbeitsweg

- Ergebnis sichten: Welche Krisenfrüherkennung und StaRUG-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (§ 1 StaRUG fortlaufend, § 15a InsO 3 Wochen / 6 Wochen, § 102 StaRUG Hinweispflicht Steuerberater 14 Tage), notwendige Dokumente (Frühwarnsystem-Bericht, Restrukturierungsanzeige, Restrukturierungsplan, Sanierungsmoderation-Antrag, Stabilisierungsanordnung), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Geschäftsführer, Aufsichtsrat, Restrukturierungsbeauftragter, Restrukturierungsgericht (LG) oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Krisenfrüherkennung StaRUG.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 1 StaRUG
- § 102 StaRUG
- § 93 AktG
- § 43 GmbHG
- § 73 StaRUG
- § 26 StaRUG
- § 29 StaRUG
- § 31 StaRUG
- § 30 StaRUG
- § 49-59 StaRUG
- § 9 StaRUG
- § 76 StaRUG

### Leitentscheidungen

- BGH IX ZR 285/14
- BGH IX ZR 56/22
- BGH II ZR 206/22
- BGH IV ZR 66/25

