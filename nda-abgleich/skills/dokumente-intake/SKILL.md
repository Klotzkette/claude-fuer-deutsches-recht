---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Nda Abgleich** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

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

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Nda Abgleich-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: GehG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.


## Normen & Rechtsprechung

Konkret zu prüfen:

- § 305 BGB (AGB-Begriff)
- § 305c BGB (überraschende Klauseln)
- § 307 BGB (Inhaltskontrolle)
- § 90 HGB (Geschäftsgeheimnisse)
- GeschGehG (Geschäftsgeheimnisgesetz)
## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Vertragspartner.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
