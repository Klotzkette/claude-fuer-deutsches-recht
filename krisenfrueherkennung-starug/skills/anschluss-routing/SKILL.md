---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Krisenfrüherkennung und StaRUG-Management."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Krisenfrueherkennung Starug** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `ampelsystem-beweislast-und-darlegungslast` — Ampelsystem Beweislast und Darlegungslast
- `berater-drohende-fruehwarnsystem` — Berater Drohende Fruehwarnsystem
- `cross-class-cram-down-und-absolute-priority` — Cross Class Cram Down und Absolute Priority
- `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` — Dokumentationspflicht und Protokollierung Geschäftsführung
- `drohende-zahlen-schwellen-und-berechnung` — Drohende Zahlen Schwellen und Berechnung
- `drohende-zahlungsunfaehigkeit` — Drohende Zahlungsunfaehigkeit
- `fortbestehensprognose-zweistufig` — Fortbestehensprognose Zweistufig
- `fruehwarnsystem-architektur-zwei-jahres-horizont` — Fruehwarnsystem Architektur Zwei Jahres Horizont
- `fruehwarnsystem-behoerden-gericht-und-registerweg` — Fruehwarnsystem Behoerden Gericht und Registerweg
- `geschaeftsfuehrerhaftung-quellenkarte-check` — Geschäftsführerhaftung Quellenkarte Check
- `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` — GF Haftung Paragraph 43 GMBHG und Paragraph 93 AKTG
- `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` — Insolvenzantragspflicht Paragraph 15A Inso und Drei Wochen Frist
- `integrierte-interessen-kennzahlenset` — Integrierte Interessen Kennzahlenset
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Krisenfrüherkennung und StaRUG-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: Paragraf 1 StaRUG gilt fortlaufend; ein Antrag nach Paragraf 15a InsO ist ohne schuldhaftes Zögern zu stellen, höchstens binnen drei Wochen bei Zahlungsunfähigkeit und sechs Wochen bei Überschuldung. Paragraf 102 StaRUG enthält keine feste 14-Tage-Frist und setzt einen Auftrag zur Jahresabschlusserstellung sowie die weiteren Tatbestandsmerkmale voraus. Danach notwendige Dokumente, gerichtliches Instrument und nächsten Fachpfad bestimmen.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Geschäftsführer, Aufsichtsrat, Restrukturierungsbeauftragten, das nach Paragrafen 34 und 35 StaRUG zuständige Restrukturierungsgericht oder einen Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
