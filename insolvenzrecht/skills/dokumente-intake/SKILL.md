---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Insolvenzrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `anfechtungsrechte-antragspflicht-15a-auslaendischer` — Anfechtungsrechte Antragspflicht 15a Auslaendischer
- `antragspflicht-spezial-belegmatrix-spezial-chronologie` — Antragspflicht Belegmatrix Chronologie
- `feststellung-sonderfall-glaeubigerantrag-inso-insolvenzrecht` — Feststellung Sonderfall Glaeubigerantrag Inso Insolvenzrecht
- `glaeubigerantrag-glaeubigerausschuss-mitwirkung-inso-dsgvo` — Glaeubigerantrag Glaeubigerausschuss Mitwirkung Inso Dsgvo
- `glaeubigerausschuss-fristennotiz-ueberschuldung-do-versicherung` — Glaeubigerausschuss Fristennotiz Ueberschuldung Do Versicherung
- `inso-gerichtliche-aufsichtswege-glaeubigerausschuss-praxis` — Inso Gerichtliche Aufsichtswege Glaeubigerausschuss Praxis
- `inso-lma-facility-massearmut-massekostenmangel-negativeintrag` — Inso Lma Facility Massearmut Massekostenmangel Negativeintrag
- `inso-npl-kreditkauf-restschuldbefreiung-versagungsgruende-schufa` — Inso Npl Kreditkauf Restschuldbefreiung Versagungsgruende Schufa
- `inso-tabelle-verbraucherinsolvenz-leitfaden-insol-insolvenzgeld` — Inso Tabelle Verbraucherinsolvenz Leitfaden Insol Insolvenzgeld
- `insol-sanierungsgewinn-7b-debt-equity-eigenverwaltung-cra-fruehe` — Insol Sanierungsgewinn 7b Debt Equity Eigenverwaltung Cra Fruehe
- `insol-sanierungsgewinn-insolvenzreife-antragspflicht-insol` — Insol Sanierungsgewinn Insolvenzreife Antragspflicht Insol
- `insol-sanierungsgewinn-liquidation-mandantenwarnung-iv` — Insol Sanierungsgewinn Liquidation Mandantenwarnung Iv
- `insol-sanierungsgewinn-uebertragende-finanzamt-stundung-verzicht` — Insol Sanierungsgewinn Uebertragende Finanzamt Stundung Verzicht
- `insolvenzrecht-kaltstart-interview` — Insolvenzrecht Kaltstart Interview

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Insolvenzantrag, Gläubigerverzeichnis, Forderungsanmeldung, Insolvenztabelle, Berichts- und Schlusstermin, Insolvenzplan, Restrukturierungsplan (StaRUG).
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Insolvenzrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: InsO §§ 1, 13, 14, 15a, 17, 18, 19, 20, 21, 22, 27, 35, 39, 47, 55, 56, 60, 64, 80, 87, 97, 129, 133, 142, 174, 175, 179, 187, 199, 270, 270a-d, 286, 287, 295, 300, StaRUG §§ 1, 29, 31, 39, 49–55, 84, 100, 102 — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Schuldner, IV/SV/Restrukturierungsbeauftragter, Gläubigerausschuss, Insolvenzgericht, Gläubiger, Geschäftsführer (§ 15a-Adressat) prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Schuldner GmbH/Person.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
