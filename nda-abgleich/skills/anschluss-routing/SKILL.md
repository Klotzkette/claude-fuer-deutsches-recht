---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Nda Abgleich** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `ausgabe-changes-docx-beweislast` — Ausgabe Changes Docx Beweislast
- `durch-interessen-echten-sonderfall-eigenen` — Durch Interessen Echten Sonderfall Eigenen
- `gegen-gelb-gleicht` — Gegen Gelb Gleicht
- `gegenseite-tracked-fristennotiz-nda-definitionsklausel` — Gegenseite Tracked Fristennotiz Nda Definitionsklausel
- `geschaeftsgeheimnis-geschgehg-kartellsensitiven-daten` — Geschaeftsgeheimnis Geschgehg Kartellsensitiven Daten
- `haltelinien-setzt-standard` — Haltelinien Setzt Standard
- `it-saas-laufzeit-survival-m-a` — It Saas Laufzeit Survival M A
- `m-a-aenderungsmodus-ampelmatrix` — M A Aenderungsmodus Ampelmatrix
- `mitarbeiter-need-non-solicit-permitted-disclosure` — Mitarbeiter Need Non Solicit Permitted Disclosure
- `nda-abgleich` — Nda Abgleich
- `nda-abgleich-arbeitnehmer-kuendigung-bewerbungen-pitches` — Nda Abgleich Arbeitnehmer Kündigung Bewerbungen Pitches
- `nda-anwendbares-recht-gerichtsstand` — Nda Anwendbares Recht Gerichtsstand
- `nda-bei-arbeitnehmer-kuendigung` — Nda Bei Arbeitnehmer Kündigung

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
## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von NDA-Abgleich.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
