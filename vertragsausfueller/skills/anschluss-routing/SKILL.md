---
name: anschluss-routing
description: "Anschluss-Routing für Vertragsausfüller: wählt den nächsten Spezial-Skill nach Engpass (Schriftform/Textform-Fristen, Vertragsentwurf, Mustervertrag, Anlagen), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Vertragsausfueller** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `altvertraege-dokumentenmatrix-und-lueckenliste` — Altvertraege Dokumentenmatrix und Lueckenliste
- `altvertrag-nachziehen` — Altvertrag Nachziehen
- `ausdruecklicher-fristennotiz-und-naechster-schritt` — Ausdruecklicher Fristennotiz und Naechster Schritt
- `batch-modus-docx-stripper-einfuehrung` — Batch Modus Docx Stripper Einfuehrung
- `bsag-mietvertrag-klauselentscheidung` — Bsag Mietvertrag Klauselentscheidung
- `changes-beweislast-docx-erkennen` — Changes Beweislast Docx Erkennen
- `clean-output` — Clean Output
- `docx-stripper` — Docx Stripper
- `docx-tatbestand-beweis-und-belege` — Docx Tatbestand Beweis und Belege
- `einfuehrung-prozess` — Einfuehrung Prozess
- `erkennen-schriftsatz-brief-und-memo-bausteine` — Erkennen Schriftsatz Brief und Memo Bausteine
- `erzeugen-red-fassungen-sonderfall-felder` — Erzeugen RED Fassungen Sonderfall Felder
- `fassungen-sonderfall-und-edge-case` — Fassungen Sonderfall und Edge Case
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

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

