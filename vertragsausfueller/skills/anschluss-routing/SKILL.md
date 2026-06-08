---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Vertragsausfueller** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `changes-beweislast-docx-erkennen` — Changes Beweislast Docx Erkennen
- `erzeugen-red-fassungen-sonderfall-felder` — Erzeugen Red Fassungen Sonderfall Felder
- `fuehren-interessen-mappen-nachfrage` — Fuehren Interessen Mappen Nachfrage
- `term-track-vertraege` — Term Track Vertraege
- `vaf-batch-vaf-docx-vaf-einfuehrung` — Vaf Batch Vaf Docx Vaf Einfuehrung
- `vaf-bsag-vaf-klauselentscheidung-vaf-konzern` — Vaf Bsag Vaf Klauselentscheidung Vaf Konzern
- `vaf-clean-output` — Vaf Clean Output
- `vaf-feldinventar-vaf-fragebogen-vaf-fremdsprachige` — Vaf Feldinventar Vaf Fragebogen Vaf Fremdsprachige
- `vaf-plausibilitaetscheck-vaf-termsheet-altvertraege` — Vaf Plausibilitaetscheck Vaf Termsheet Altvertraege
- `vaf-quality-vaf-redline-vaf-rueckfrageninterview` — Vaf Quality Vaf Redline Vaf Rueckfrageninterview
- `vaf-template-vaf-template-vaf-track` — Vaf Template Vaf Template Vaf Track
- `vaf-vaf-mehrsprachige-vaf-platzhalterlogik` — Vaf Vaf Mehrsprachige Vaf Platzhalterlogik
- `vaf-versionierung` — Vaf Versionierung

## Arbeitsweg

- Ergebnis sichten: Welche Vertragsausfüller (Lückenschluss in Verträgen)-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (Vertragsspezifisch; § 195 BGB Regelverjährung 3 Jahre, § 14 BGB-InfoV Widerrufsfrist 14 Tage), notwendige Dokumente (Mustervertrag, Termsheet, Klauselkatalog, Altvertrag, Vertragsentwurf mit Track Changes), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Vertragspartner, Rechtsabteilung, Notar bei Formerfordernis oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Vertragsausfüller.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 9 UStG
- § 2 NachwG
- § 3a RVG
- § 29 VwVfG

### Leitentscheidungen

- BGH VI ZR 394/12
- BGH I ZR 169/12
- BGH VII ZR 213/07
- BGH VII ZR 37/17

