---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Erbrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `berater-interessen-beweislast-darlegungslast` — Berater Interessen Beweislast Darlegungslast
- `erb-einfuehrung-erb-erstgespraech-erb-internationales` — Erb Einfuehrung Erb Erstgespraech Erb Internationales
- `erb-nachlassinventar-erb-pflichtteilsanspruch-erb` — Erb Nachlassinventar Erb Pflichtteilsanspruch Erb
- `erbengemeinschaft-blockade-erstgespraech-mandatsannahme` — Erbengemeinschaft Blockade Erstgespraech Mandatsannahme
- `erbfall-eu-mandat-triage-pflichtteil-auskunft` — Erbfall Eu Mandat Triage Pflichtteil Auskunft
- `erbfall-intake-erbrecht-erbschein` — Erbfall Intake Erbrecht Erbschein
- `erbschein-antrag-orientierung-pflichtteilsberechnung` — Erbschein Antrag Orientierung Pflichtteilsberechnung
- `fachanwalt-kanzlei-livecheck` — Fachanwalt Kanzlei Livecheck
- `krypto-wallet-erbschaftsteuer-steuerrecht` — Krypto Wallet Erbschaftsteuer Steuerrecht
- `pflichtteil-berechnen-schriftsatzkern-substantiierung-sonderfall` — Pflichtteil Berechnen Schriftsatzkern Substantiierung Sonderfall
- `pflichtteil-progressionsoptimierung-spezial-schnittstellen` — Pflichtteil Progressionsoptimierung Schnittstellen
- `pflichtteilsergaenzung-frist-fachanwalt-erbrecht` — Pflichtteilsergaenzung Frist Fachanwalt Erbrecht
- `pflichtteilsergaenzung-testamentsvollstreckung-mediation` — Pflichtteilsergaenzung Testamentsvollstreckung Mediation

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt Erbrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: BGB, §§ 1922 ff — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Erblasser (Beratung).

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
