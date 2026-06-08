---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Fachanwalt It Recht** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `dma-dsa-dsgvo-fachanwalt-governance` — Dma Dsa Dsgvo Fachanwalt Governance
- `dsv-aufnahme-dsv-benachrichtigung-dsv-benachrichtigung-dsv` — Dsv Aufnahme Dsv Benachrichtigung Dsv Benachrichtigung Dsv
- `dsv-dsfa-update-erstgespraech-vorfallmeldung-eskalationsmatrix` — Dsv Dsfa Update Erstgespraech Vorfallmeldung Eskalationsmatrix
- `dsv-kinderdaten-besondere-kommunikationssperre-lead-authority` — Dsv Kinderdaten Besondere Kommunikationssperre Lead Authority
- `dsv-massenbenachrichtigung-dsv-meldekette-dsv-meldung-dsv` — Dsv Massenbenachrichtigung Dsv Meldekette Dsv Meldung Dsv
- `dsv-meldung-baylda-bfdi-bln-bdi-hbdi-hmbbfdi` — Dsv Meldung Baylda Bfdi Bln Bdi Hbdi Hmbbfdi
- `dsv-meldung-lda-ldi-nrw-lfd-niedersachsen-sachsen-anhalt-lfdi` — Dsv Meldung Lda Ldi Nrw Lfd Niedersachsen Sachsen Anhalt Lfdi
- `dsv-meldung-lfdi-mv-rlp-saarland-saechsdsb` — Dsv Meldung Lfdi Mv Rlp Saarland Saechsdsb
- `dsv-meldung-tlfdi-uld-sh-nachmeldung-aktualisierung-enisa` — Dsv Meldung Tlfdi Uld Sh Nachmeldung Aktualisierung Enisa
- `dsv-pressemitteilung-krisenkommunikation-sammelklagen-vvt-update` — Dsv Pressemitteilung Krisenkommunikation Sammelklagen Vvt Update
- `dsv-rechtsprechung-saas-vertrag-fristennotiz-fachanwalt-it` — Dsv Rechtsprechung Saas Vertrag Fristennotiz Fachanwalt It
- `dsv-risikobewertung-art-schnelltriage-risiko-sofortmassnahmen` — Dsv Risikobewertung Art Schnelltriage Risiko Sofortmassnahmen
- `dsv-stakeholder-dsv-tonfall-dsv-verdacht-dsv-zeitleiste` — Dsv Stakeholder Dsv Tonfall Dsv Verdacht Dsv Zeitleiste
- `fachanwalt-it-cloud-vertrag-datenschutz-itr-ki-saas-bauleiter` — Fachanwalt It Cloud Vertrag Datenschutz Itr Ki Saas Bauleiter

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Fachanwalt It Recht-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: BDSG, DDG, DSGVO, TKG, TTDSG — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Auftraggeber.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
