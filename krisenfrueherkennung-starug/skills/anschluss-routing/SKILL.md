---
name: anschluss-routing
description: "Anschluss-Routing für Krisenfrüherkennung StaRUG: wählt den nächsten Spezial-Skill nach Engpass (Frühzeitige Indikatoren, Liquiditätsplan, Frühwarn-Indikatoren, Sanierungskonzept IDW S 6), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Krisenfrueherkennung Starug** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `ampelsystem-beweislast-und-darlegungslast` — Ampelsystem Beweislast und Darlegungslast
- `berater-drohende-fruehwarnsystem` — Berater Drohende Fruehwarnsystem
- `cross-class-cram-down-und-absolute-priority` — Cross Class Cram Down und Absolute Priority
- `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` — Dokumentationspflicht und Protokollierung Geschaeftsfuehrung
- `drohende-zahlen-schwellen-und-berechnung` — Drohende Zahlen Schwellen und Berechnung
- `drohende-zahlungsunfaehigkeit` — Drohende Zahlungsunfaehigkeit
- `fortbestehensprognose-zweistufig` — Fortbestehensprognose Zweistufig
- `fruehwarnsystem-architektur-zwei-jahres-horizont` — Fruehwarnsystem Architektur Zwei Jahres Horizont
- `fruehwarnsystem-behoerden-gericht-und-registerweg` — Fruehwarnsystem Behoerden Gericht und Registerweg
- `geschaeftsfuehrerhaftung-quellenkarte-check` — Geschaeftsfuehrerhaftung Quellenkarte Check
- `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` — GF Haftung Paragraph 43 GMBHG und Paragraph 93 AKTG
- `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` — Insolvenzantragspflicht Paragraph 15A Inso und Drei Wochen Frist
- `integrierte-interessen-kennzahlenset` — Integrierte Interessen Kennzahlenset
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

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

