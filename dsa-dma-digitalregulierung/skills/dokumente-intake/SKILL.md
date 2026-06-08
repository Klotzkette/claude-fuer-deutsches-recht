---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Dsa Dma Digitalregulierung** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `dark-patterns-internes-beschwerdesystem` — Dark Patterns Internes Beschwerdesystem
- `data-digitalregulierung-dora` — Data Digitalregulierung Dora
- `dma-business-user-gatekeeper-kernplattformdienste` — Dma Business User Gatekeeper Kernplattformdienste
- `dma-pflichten-dsa-art-forschungsdatenzugang-algorithmen` — Dma Pflichten Dsa Art Forschungsdatenzugang Algorithmen
- `dsa-eidas-einordnung` — Dsa Eidas Einordnung
- `erstellung-forschungsdatenzugang-mehrparteienkonflikt-gatekeeper` — Erstellung Forschungsdatenzugang Mehrparteienkonflikt Gatekeeper
- `kernplattformdienste-sonderfall-klagewege-risikobewertung` — Kernplattformdienste Sonderfall Klagewege Risikobewertung
- `out-court-pflichten-pyramide-systemic-risk` — Out Court Pflichten Pyramide Systemic Risk
- `pyramide-check-dsgvo-p2b-anti-steering` — Pyramide Check Dsgvo P2b Anti Steering
- `transparenzbericht-erstellung-trusted-flagger-vlop-vlose` — Transparenzbericht Erstellung Trusted Flagger Vlop Vlose
- `transparenzbericht-fristennotiz-dsa-dma-account-sperre` — Transparenzbericht Fristennotiz Dsa Dma Account Sperre
- `werbearchiv-aufbauen-klage-gegen-account` — Werbearchiv Aufbauen Klage Gegen Account
- `zustellung-vertreter` — Zustellung Vertreter

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Dsa Dma Digitalregulierung-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: Art. 13, Art. 20, Art. 34, Art. 40, DDG, § 19a GWB — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Plattform/VLOP.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
