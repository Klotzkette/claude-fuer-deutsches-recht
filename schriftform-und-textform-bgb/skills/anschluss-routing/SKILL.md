---
name: anschluss-routing
description: "Anschluss-Routing für Schriftform/Textform BGB: wählt den nächsten Spezial-Skill nach Engpass (Form vor Wirksamkeit, Vertrag, Unterschrift, qualifizierte e-Signatur), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Schriftform Und Textform Bgb** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `amtlicher-formkern-bgb-zpo-check` — Amtlicher Formkern BGB ZPO Check
- `anspruchsformulierungen-formverstoss` — Anspruchsformulierungen Formverstoss
- `arbeitsrecht-befristung-schriftform-checker` — Arbeitsrecht Befristung Schriftform Checker
- `befristungsabrede-qes-rechtsprechung` — Befristungsabrede QES Rechtsprechung
- `befristungsabrede-qes-rechtsprechung-stand-2026` — Befristungsabrede QES Rechtsprechung Stand 2026
- `bgb-mehrparteien-konflikt-und-interessen` — BGB Mehrparteien Konflikt und Interessen
- `buergschaft-verbraucherdarlehen-und-andere-strenge-formen` — Buergschaft Verbraucherdarlehen und Andere Strenge Formen
- `checklisten-schriftsatz-brief-und-memo-bausteine` — Checklisten Schriftsatz Brief und Memo Bausteine
- `dokumentations-und-beweisarchitektur` — Dokumentations und Beweisarchitektur
- `elektronische-paragraph-formerfordernisse` — Elektronische Paragraph Formerfordernisse
- `empfangsbeduerftiger-international` — Empfangsbeduerftiger International
- `empfangsbeduerftiger-international-schnittstellen` — Empfangsbeduerftiger International Schnittstellen
- `form-checker-fuer-vertrag-oder-willenserklaerung` — Form Checker Fuer Vertrag Oder Willenserklaerung
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Schriftform Und Textform Bgb-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Schriftform/Textform BGB.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 46h ArbGG
- § 14 TzBfG
- § 16 TzBfG
- § 15 GmbHG
- § 46c ArbGG
- § 17 TzBfG
- § 16a BeurkG
- § 23a GVG
- § 113 FamFG
- § 2 HRG
- § 4 HRG
- § 7 HRG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

