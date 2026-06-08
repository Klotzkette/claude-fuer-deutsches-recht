---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Verwaltungsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `anfechtungs-eilrechtsschutz-abs-eilrechtsschutz` — Anfechtungs Eilrechtsschutz Abs Eilrechtsschutz
- `einstweilige-fachanwalt-kanzlei` — Einstweilige Fachanwalt Kanzlei
- `erstgespraech-mandatsannahme-fa-vwgo-anfechtungsklage` — Erstgespraech Mandatsannahme Fa Vwgo Anfechtungsklage
- `fachanwalt-verwaltungsrecht-drittanfechtung-einstweiliger` — Fachanwalt Verwaltungsrecht Drittanfechtung Einstweiliger
- `fachanwalt-verwaltungsrecht-verwaltungsakt-rechtsbehelf-vwgo` — Fachanwalt Verwaltungsrecht Verwaltungsakt Rechtsbehelf Vwgo
- `normenkontrolle-ordnungsrecht-interessen-orientierung-sonderfall` — Normenkontrolle Ordnungsrecht Interessen Orientierung Sonderfall
- `normenkontrolle-vwgo-orientierung-vwgo-behoerde` — Normenkontrolle Vwgo Orientierung Vwgo Behörde
- `polizei-polizei-filmen-rechtsschutz-beweislast` — Polizei Polizei Filmen Rechtsschutz Beweislast
- `schnittstelle-verpflichtungsklage-verwaltungsrecht` — Schnittstelle Verpflichtungsklage Verwaltungsrecht
- `verwr-folgenbeseitigung-planfeststellung-grossvorhaben` — Verwr Folgenbeseitigung Planfeststellung Grossvorhaben
- `verwr-verwaltungsverfahren-eilantrag-abs-energietrassen` — Verwr Verwaltungsverfahren Eilantrag Abs Energietrassen
- `vorläufiger-vwvfg-vergleichsverhandlung-strategie` — Vorlaeufiger Vwvfg Vergleichsverhandlung Strategie
- `vwr-eilrechtsschutz-widerspruch-klage` — Vwr Eilrechtsschutz Widerspruch Klage

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
