---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Meinungspruefer** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `abwaegung-art-arbeitgeber-betrieb` — Abwaegung Art Arbeitgeber Betrieb
- `beleglage-tatsachenbehauptung-beweissicherung-screenshots` — Beleglage Tatsachenbehauptung Beweissicherung Screenshots
- `beleidigung-meinungspruefer` — Beleidigung Meinungspruefer
- `egmr-art-eugh-grch` — Egmr Art Eugh Grch
- `europarecht-emrk-gegendarstellung-entschuldigung` — Europarecht Emrk Gegendarstellung Entschuldigung
- `kommunalrecht-buergermeister-machtkritik-amtstraeger` — Kommunalrecht Buergermeister Machtkritik Amtstraeger
- `mehrdeutigkeit-sinnermittlung-meinung-tatsache` — Mehrdeutigkeit Sinnermittlung Meinung Tatsache
- `meinung-strafantrag-verfahren` — Meinung Strafantrag Verfahren
- `nachrede-tatsache` — Nachrede Tatsache
- `olg-kg-rechtsprechungsbank-verifiziert` — Olg Kg Rechtsprechungsbank Verifiziert
- `output-memo-pruefvermerk` — Output Memo Pruefvermerk
- `personen-politisches-presserecht-plattformen` — Personen Politisches Presserecht Plattformen
- `rechtsvergleich-usa-risikomatrix-ampel` — Rechtsvergleich Usa Risikomatrix Ampel
- `satire-ironisierung-schimpfwort-lackaffe` — Satire Ironisierung Schimpfwort Lackaffe

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Meinungspruefer-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: Art. 10, Art. 11, EMRK, GG, OLG, § 188 StGB, Art — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Betroffener.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
