---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Schriftform Und Textform Bgb** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `anspruchsformulierungen-formverstoss-buergschaft` — Anspruchsformulierungen Formverstoss Buergschaft
- `arbeitsrecht-befristung-schriftform-checker-vertrag` — Arbeitsrecht Befristung Schriftform Checker Vertrag
- `elektronische-paragraph-formerfordernisse-ueberblick` — Elektronische Paragraph Formerfordernisse Ueberblick
- `formwahl-zugang-live-prozessablauf-mandantenentscheidung` — Formwahl Zugang Live Prozessablauf Mandantenentscheidung
- `klauselgenerator-formvorbehalt-maklervertrag-paragraph-amtlicher` — Klauselgenerator Formvorbehalt Maklervertrag Paragraph Amtlicher
- `kuendigung-per-mandantenkorrespondenz-zugang-mandantenwarnung` — Kündigung Per Mandantenkorrespondenz Zugang Mandantenwarnung
- `notarielle-beurkundung-prozessablauf-papier-paragraph` — Notarielle Beurkundung Prozessablauf Papier Paragraph
- `prozessordnungen-textform-verifikation` — Prozessordnungen Textform Verifikation
- `sftf-arbeitsvertraege-nachweisgesetz-doppelschriftform-aufhebung` — Sftf Arbeitsvertraege Nachweisgesetz Doppelschriftform Aufhebung
- `sftf-formvorgaben-bgb-interessen-checklisten` — Sftf Formvorgaben Bgb Interessen Checklisten
- `textform-paragraph-verteidigungsstrategie-formangriff` — Textform Paragraph Verteidigungsstrategie Formangriff
- `willenserklaerung-zivilrecht-zugang` — Willenserklaerung Zivilrecht Zugang
- `zugang-empfangsbeduerftiger-zugang-formgerechter` — Zugang Empfangsbeduerftiger Zugang Formgerechter

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

