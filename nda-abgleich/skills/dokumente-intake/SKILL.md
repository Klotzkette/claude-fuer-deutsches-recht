---
name: dokumente-intake
description: "Dokumentenintake für NDA-Abgleich: sortiert NDA-Entwurf, Mustervorlage, Vorvertrags-Korrespondenz, prüft Datum, Absender, Frist und Beweiswert (Versionsverlauf, Mailverkehr); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Nda Abgleich** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `aenderungsmodus-compliance-dokumentation` — Aenderungsmodus Compliance Dokumentation
- `aenderungsmodus-compliance-dokumentation-und-akte` — Aenderungsmodus Compliance Dokumentation und Akte
- `ampelmatrix-internationaler-bezug-schnittstellen` — Ampelmatrix Internationaler Bezug Schnittstellen
- `ampelmatrix-internationaler-bezug-und-schnittstellen` — Ampelmatrix Internationaler Bezug und Schnittstellen
- `arbeitnehmer-kuendigung` — Arbeitnehmer Kuendigung
- `ausgabe-changes-docx-beweislast` — Ausgabe Changes Docx Beweislast
- `ausgabe-mandantenkommunikation-entscheidungsvorlage` — Ausgabe Mandantenkommunikation Entscheidungsvorlage
- `changes-abschlussprodukt-uebergabe` — Changes Abschlussprodukt Uebergabe
- `changes-abschlussprodukt-und-uebergabe` — Changes Abschlussprodukt und Uebergabe
- `chirurgisch-quellenkarte` — Chirurgisch Quellenkarte
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `docx-beweislast-darlegungslast` — Docx Beweislast Darlegungslast
- `docx-beweislast-und-darlegungslast` — Docx Beweislast und Darlegungslast
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

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
