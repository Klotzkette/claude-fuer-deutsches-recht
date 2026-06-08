---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Transport Speditionsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `autonome-lkw-cmr-schadensregulierung-speditionshaftung-hgb` — Autonome Lkw Cmr Schadensregulierung Speditionshaftung Hgb
- `cmr-haftung-ladungsschaden-frachtfuehrerhaftung` — Cmr Haftung Ladungsschaden Frachtfuehrerhaftung
- `cotif-fachanwalt-haager` — Cotif Fachanwalt Haager
- `hgb-kabotage-beweislast-kanzlei-red` — Hgb Kabotage Beweislast Kanzlei Red
- `lieferverzug-orientierung-mandat-triage` — Lieferverzug Orientierung Mandat Triage
- `marktzugang-sonderfall-montrealer-spezial-pruefen` — Marktzugang Sonderfall Montrealer Prüfen
- `regeln-interessen-schnittstelle-spedition` — Regeln Interessen Schnittstelle Spedition
- `reklamationsschreiben-cmr-schriftsatzkern-substantiierung-adsp` — Reklamationsschreiben Cmr Schriftsatzkern Substantiierung Adsp
- `speditionsrecht-tio-schiedsgericht-frachtvertrag` — Speditionsrecht Tio Schiedsgericht Frachtvertrag
- `trans-cmr-frachtbrief-hgb-spedition-kabotage-marktzugang` — Trans Cmr Frachtbrief Hgb Spedition Kabotage Marktzugang
- `trans-multimodaler-transr-cmr-transr-multimodaler` — Trans Multimodaler Transr Cmr Transr Multimodaler
- `trans-transport-visby` — Trans Transport Visby
- `transr-einfuehrung-rechtsquellen` — Transr Einfuehrung Rechtsquellen

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt Transport Speditionsrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: HGB, §§ 407 ff, §§ 453 ff — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Absender.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
