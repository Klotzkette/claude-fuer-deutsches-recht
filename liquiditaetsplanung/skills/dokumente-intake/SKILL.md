---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Liquiditaetsplanung** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `deutschem-dokumentationspaket-excel` — Deutschem Dokumentationspaket Excel
- `export-forecast-fortbestehensprognose-international` — Export Forecast Fortbestehensprognose International
- `idw-s6-integrierte-sanierungsplanung` — Idw S6 Integrierte Sanierungsplanung
- `insolvenzrecht-liqui-sonderfall-liquiditaetsplanung` — Insolvenzrecht Liqui Sonderfall Liquiditaetsplanung
- `interessen-verifikation-beweislast-vorschau` — Interessen Verifikation Beweislast Vorschau
- `liqp-bankenreporting-leitfaden` — Liqp Bankenreporting Leitfaden
- `liqp-liquiditaetspool-cash-pooling-spezial` — Liqp Liquiditaetspool Cash Pooling Spezial
- `liqp-liquiditaetspool-cash-rollende-13wochen-warenkredit-skonto` — Liqp Liquiditaetspool Cash Rollende 13wochen Warenkredit Skonto
- `liqp-rollende-13wochen-bauleiter` — Liqp Rollende 13wochen Bauleiter
- `liqp-warenkredit-skonto-szenarien-spezial` — Liqp Warenkredit Skonto Szenarien Spezial
- `liqui-ausgabengruppen-systematik` — Liqui Ausgabengruppen Systematik
- `liqui-bei-drohender-zahlungsunfaehigkeit` — Liqui Bei Drohender Zahlungsunfaehigkeit
- `liqui-bei-eingetretener-zahlungsunfaehigkeit` — Liqui Bei Eingetretener Zahlungsunfaehigkeit

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Liquiditätsstatus, Finanzplan, Liquiditätsvorschau 3 Wochen / 3–6–12 Monate, Fortbestehensprognose, Sanierungsgutachten IDW S 6.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Liquiditätsplanung und Insolvenzrecht-Schnittstelle-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: InsO §§ 17, 18, 19, 15a, IDW S 11, IDW PS 800, HGB § 252 Abs. 1 Nr. 2 (Going Concern), StaRUG §§ 1, 29, 102 — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Bank, IV/Restrukturierungsbeauftragter prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Geschäftsführung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
