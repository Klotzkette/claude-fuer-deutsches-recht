---
name: anschluss-routing
description: "Anschluss-Routing für Memorandum-Ersteller: wählt den nächsten Spezial-Skill nach Engpass (Mandantenbericht-Fristen, Sachverhalt, Quellen, Vorergebnisse), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Memorandums Ersteller** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `antworten-interessen-ausfuehrungen-fragen` — Antworten Interessen Ausfuehrungen Fragen
- `ausfuehrungen-formular-portal-und-einreichung` — Ausfuehrungen Formular Portal und Einreichung
- `due-diligence-ergebnis-handlungsempfehlung` — DUE Diligence Ergebnis Handlungsempfehlung
- `fragen-compliance-dokumentation-und-akte` — Fragen Compliance Dokumentation und Akte
- `gliederung-mandantenunterlagen-memorandum` — Gliederung Mandantenunterlagen Memorandum
- `haftungsrisiko-rechtsanwalt-board-pack` — Haftungsrisiko Rechtsanwalt Board Pack
- `juristisches-questions-fristennotiz` — Juristisches Questions Fristennotiz
- `laenge-formate-mandantenfreundliche-fassung` — Laenge Formate Mandantenfreundliche Fassung
- `mandantenanfrage-schnell` — Mandantenanfrage Schnell
- `mandantenkommunikation-redteam` — Mandantenkommunikation Redteam
- `mandantenunterlagen-tatbestand-beweis-und-belege` — Mandantenunterlagen Tatbestand Beweis und Belege
- `memo-board-pack-besondere-anlaesse-spezial` — Memo Board Pack Besondere Anlaesse Spezial
- `memo-compliance-vorfall-intern` — Memo Compliance Vorfall Intern
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Memorandums Ersteller-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Memorandum-Ersteller.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 203 StGB
- § 31 VVG
- § 29 VwVfG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

