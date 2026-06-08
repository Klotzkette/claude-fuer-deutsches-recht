---
name: dokumente-intake
description: "Dokumentenintake für Strafzumessung: sortiert Anklageschrift, Urteilsentwurf, Vorverurteilungen BZR, prüft Datum, Absender, Frist und Beweiswert (BZR-Auszug, Persönlichkeitsgutachten); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Strafzumessung** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `153a-stpo-iii-bewaehrung-stgb` — 153a STPO III Bewaehrung STGB
- `besonders-formular-portal-und-einreichung` — Besonders Formular Portal und Einreichung
- `bewaehrung-56-stgb-positive-sozialprognose` — Bewaehrung 56 STGB Positive Sozialprognose
- `bewaehrung-auflagen-bewaehrungswiderruf-56f` — Bewaehrung Auflagen Bewaehrungswiderruf 56F
- `bewaehrung-interessen-deutschem` — Bewaehrung Interessen Deutschem
- `bewaehrungswiderruf-56f-stgb` — Bewaehrungswiderruf 56F STGB
- `deutschem-tatbestand-beweis-und-belege` — Deutschem Tatbestand Beweis und Belege
- `freiheitsstrafe-compliance-dokumentation-und-akte` — Freiheitsstrafe Compliance Dokumentation und Akte
- `freiheitsstrafe-ohne-bewaehrung-vollstreckung` — Freiheitsstrafe Ohne Bewaehrung Vollstreckung
- `freiheitsstrafe-strafmass-geldstrafe` — Freiheitsstrafe Strafmass Geldstrafe
- `geldstrafe-grossen-rechtsmittel` — Geldstrafe Grossen Rechtsmittel
- `geldstrafe-tagessatzanzahl-bestimmen` — Geldstrafe Tagessatzanzahl Bestimmen
- `geldstrafe-vs-freiheitsstrafe-47-stgb` — Geldstrafe VS Freiheitsstrafe 47 STGB
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Bewährungsauflage, Tatumstandskatalog, Vorstrafenregisterauszug, Sachverständigengutachten, Schuldfähigkeitsbeurteilung.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Strafzumessung-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: StGB §§ 46, 46a, 46b, 47, 49, 56, 57, 57a, 64, JGG §§ 17, 18, 21, BtMG § 31 — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Tatrichter, Verteidiger, Staatsanwaltschaft, Bewährungshelfer, Vollstreckungsbehörde prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Angeklagter.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
