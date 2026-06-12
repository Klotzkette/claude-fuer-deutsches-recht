---
name: anschluss-routing
description: "Anschluss-Routing für NDA-Abgleich: wählt den nächsten Spezial-Skill nach Engpass (Geltungsdauer NDA (5-10 Jahre), NDA-Entwurf, Mustervorlage, Vorvertrags-Korrespondenz), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Nda Abgleich** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `aenderungsmodus-compliance-dokumentation` — Änderungsmodus Compliance Dokumentation
- `aenderungsmodus-compliance-dokumentation-und-akte` — Änderungsmodus Compliance Dokumentation und Akte
- `ampelmatrix-internationaler-bezug-schnittstellen` — Ampelmatrix Internationaler Bezug Schnittstellen
- `ampelmatrix-internationaler-bezug-und-schnittstellen` — Ampelmatrix Internationaler Bezug und Schnittstellen
- `arbeitnehmer-kuendigung` — Arbeitnehmer Kuendigung
- `ausgabe-changes-docx-beweislast` — Ausgabe Changes Docx Beweislast
- `ausgabe-mandantenkommunikation-entscheidungsvorlage` — Ausgabe Mandantenkommunikation Entscheidungsvorlage
- `changes-abschlussprodukt-uebergabe` — Changes Abschlussprodukt Übergabe
- `changes-abschlussprodukt-und-uebergabe` — Changes Abschlussprodukt und Übergabe
- `chirurgisch-quellenkarte` — Chirurgisch Quellenkarte
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `docx-beweislast-darlegungslast` — Docx Beweislast Darlegungslast
- `docx-beweislast-und-darlegungslast` — Docx Beweislast und Darlegungslast
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Nda Abgleich-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Normen & Rechtsprechung

Konkret zu prüfen:

- § 305 BGB (AGB-Begriff)
- § 305c BGB (überraschende Klauseln)
- § 307 BGB (Inhaltskontrolle)
- § 90 HGB (Geschäftsgeheimnisse)
- GeschGehG (Geschäftsgeheimnisgesetz)

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
