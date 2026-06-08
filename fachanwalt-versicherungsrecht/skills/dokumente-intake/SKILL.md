---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt Versicherungsrecht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `cyber-loesegeld-versr-cyber-deckungsanfrage` — Cyber Loesegeld Versr Cyber Deckungsanfrage
- `deckungsklage-interessen-deckungspruefung-obliegenheiten` — Deckungsklage Interessen Deckungspruefung Obliegenheiten
- `do-deckungsabwehr-lebensversicherung-rueckkauf` — Do Deckungsabwehr Lebensversicherung Rueckkauf
- `erstgespraech-mandatsannahme-berufsunfaehigkeit-klage` — Erstgespraech Mandatsannahme Berufsunfaehigkeit Klage
- `fachanwalt-kanzlei-krankenversicherung` — Fachanwalt Kanzlei Krankenversicherung
- `klage-versicherer-triage-versicherungsrecht-schriftsatzkern` — Klage Versicherer Triage Versicherungsrecht Schriftsatzkern
- `lebens-leistungsablehnung-international-obliegenheitsverletzung` — Lebens Leistungsablehnung International Obliegenheitsverletzung
- `ombudsmann-gdv-orientierung-regress-abwehr` — Ombudsmann Gdv Orientierung Regress Abwehr
- `private-spezial-pruefen-rechtsschutz-beweislast` — Private Prüfen Rechtsschutz Beweislast
- `rentenversicherung-sachversicherung-schnittstelle` — Rentenversicherung Sachversicherung Schnittstelle
- `themen-fristennotiz-versr-rechtsschutz-versr` — Themen Fristennotiz Versr Rechtsschutz Versr
- `versicherungsrecht-vergleichsverhandlung-strategie-versr-bafin` — Versicherungsrecht Vergleichsverhandlung Strategie Versr Bafin
- `versr-bu-anerkennt-leistungspruefung-nachpruefung-anerkenntnis` — Versr Bu Anerkennt Leistungspruefung Nachpruefung Anerkenntnis

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt Versicherungsrecht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: VAG, VVG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Versicherungsnehmer.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
