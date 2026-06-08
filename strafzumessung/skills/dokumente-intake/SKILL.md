---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Strafzumessung** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `153a-stpo-iii-stpo-bewaehrung-stgb` — 153a Stpo Iii Stpo Bewaehrung Stgb
- `bewaehrung-auflagen-bewaehrungswiderruf-56f-freiheitsstrafe-ohne` — Bewaehrung Auflagen Bewaehrungswiderruf 56f Freiheitsstrafe Ohne
- `bewaehrung-interessen-deutschem-freiheitsstrafe` — Bewaehrung Interessen Deutschem Freiheitsstrafe
- `freiheitsstrafe-strafmass-geldstrafe-tagessatzanzahl-vs-stgb` — Freiheitsstrafe Strafmass Geldstrafe Tagessatzanzahl Vs Stgb
- `geldstrafe-grossen-rechtsmittel-gesamtstrafenfolgen` — Geldstrafe Grossen Rechtsmittel Gesamtstrafenfolgen
- `gesamtstrafenbildung-stgb-gestaendnis-strafmilderung` — Gesamtstrafenbildung Stgb Gestaendnis Strafmilderung
- `jgg-jugendstrafe-minder-schwerer-nachtraegliche` — Jgg Jugendstrafe Minder Schwerer Nachtraegliche
- `orientierung-triage-paragraph-stgb-besonders` — Orientierung Triage Paragraph Stgb Besonders
- `regelbeispiele-stgb-strafbefehl` — Regelbeispiele Stgb Strafbefehl
- `strafbefehl-stpo-strafmilderung-stgb-strafrahmen` — Strafbefehl Stpo Strafmilderung Stgb Strafrahmen
- `strafkammer-strafzumessung-strafzumessungstatsachen` — Strafkammer Strafzumessung Strafzumessungstatsachen
- `strafrecht-verfahrensstadium-strafbefehl-taeter-opfer` — Strafrecht Verfahrensstadium Strafbefehl Taeter Opfer
- `strafz-aufklaerungshilfe-kronzeuge-sicherungsverwahrung` — Strafz Aufklaerungshilfe Kronzeuge Sicherungsverwahrung
- `strafz-strafzumessungstatsachen-strafzumessungs-tatsachen` — Strafz Strafzumessungstatsachen Strafzumessungs Tatsachen

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
