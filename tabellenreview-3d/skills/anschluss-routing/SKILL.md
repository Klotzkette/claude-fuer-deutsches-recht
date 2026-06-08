---
name: anschluss-routing
description: "Anschluss-Routing für Tabellenreview (Excel/CSV): wählt den nächsten Spezial-Skill nach Engpass (keine harten Fristen, Excel-/CSV-Datei, Formelreview, Datenqualitätsbericht), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Tabellenreview 3d** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `aggregation-spaltenprompts-definieren` — Aggregation Spaltenprompts Definieren
- `arbeitsblatt-perspektiven-definieren` — Arbeitsblatt Perspektiven Definieren
- `arbeitsblatt-schriftsatz-brief-memo-bausteine` — Arbeitsblatt Schriftsatz Brief Memo Bausteine
- `arbeitsblatt-schriftsatz-brief-und-memo-bausteine` — Arbeitsblatt Schriftsatz Brief und Memo Bausteine
- `audit-trail-protokoll` — Audit Trail Protokoll
- `belegkette-rueckverfolgung` — Belegkette Rueckverfolgung
- `belegkette-rueckverfolgung-caching-rerun` — Belegkette Rueckverfolgung Caching Rerun
- `caching-und-teil-rerun` — Caching und Teil Rerun
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `datenpunkt-dokument-excel-beweislast` — Datenpunkt Dokument Excel Beweislast
- `datenpunkt-dokumentenmatrix-lueckenliste` — Datenpunkt Dokumentenmatrix Lueckenliste
- `dokument-behoerden-gericht-und-registerweg` — Dokument Behoerden Gericht und Registerweg
- `dokumentstapel-aufnehmen` — Dokumentstapel Aufnehmen
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Tabellenreview 3D-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Tabellenreview (Excel/CSV).

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 2 JVEG
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG
- § 16 HRG
- § 70 VwG
- § 123 VwG
- § 29 VwVfG
- § 1 KSchG
- § 7 KSchG
- § 102 BetrVG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

