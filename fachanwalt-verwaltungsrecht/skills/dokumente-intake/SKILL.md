---
name: dokumente-intake
description: "Dokumentenintake für Fachanwalt Verwaltungsrecht: sortiert Verwaltungsakt, Widerspruchsbescheid, Klageschrift, prüft Datum, Absender, Frist und Beweiswert (Verwaltungsakte, Anhörung); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Verwaltungsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.


## Fachlandkarte dieses Plugins

- `amtshaftung-paragraf-839-bgb-art-34-gg` — Amtshaftung Paragraf 839 BGB ART 34 GG
- `anfechtungs-eilrechtsschutz-abs` — Anfechtungs Eilrechtsschutz ABS
- `anhoerung-paragraf-28-vwvfg` — Anhoerung Paragraf 28 Vwvfg
- `anordnung-quellenkarte` — Anordnung Quellenkarte
- `drittanfechtung` — Drittanfechtung
- `eilrechtsschutz-paragraf-80-vwgo` — Eilrechtsschutz Paragraf 80 Vwgo
- `einstweilige-fachanwalt-kanzlei` — Einstweilige Fachanwalt Kanzlei
- `ermessen-paragraf-40-vwvfg` — Ermessen Paragraf 40 Vwvfg
- `erstgespraech-mandatsannahme-fa-vwgo` — Erstgespraech Mandatsannahme FA Vwgo
- `fa-verwaltungsrecht-mandant-redteam-gate` — FA Verwaltungsrecht Mandant Redteam Gate
- `fa-verwaltungsrecht-start-chronologie-fristen` — FA Verwaltungsrecht Start Chronologie Fristen
- `klagefrist-paragraf-58-vwgo-bverwg-4-c-1-19` — Klagefrist Paragraf 58 Vwgo Bverwg 4 C 1 19
- `kommunalrecht-paragraf-2-go` — Kommunalrecht Paragraf 2 GO
- `anschluss-routing` — Anschluss Routing
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt Verwaltungsrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: VwGO, VwVfG, § 80 Abs 5 VwGO einstweilige Anordnung Normenkontrolle Polizei — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Bürger/Antragsteller.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
