---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Wandeldarlehen Lebenszyklus** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `bilingual-einsprachig` — Bilingual Einsprachig
- `cap-table-darlehenshoehe-konditionen` — Cap Table Darlehenshoehe Konditionen
- `dokumenten-upload-formfehler-heilungs` — Dokumenten Upload Formfehler Heilungs
- `einsprachige-vertragsfassung-vertragserstellung` — Einsprachige Vertragsfassung Vertragserstellung
- `gesellschafterbeschluss-kapitalerhoehung-vorbereiten` — Gesellschafterbeschluss Kapitalerhoehung Vorbereiten
- `gesellschafterliste-aktualisieren-gesellschafterversammlung` — Gesellschafterliste Aktualisieren Gesellschafterversammlung
- `gmbh-vollstaendigen` — Gmbh Vollstaendigen
- `handelsregisteranmeldung-kapitalerhoehung-kyc-aml` — Handelsregisteranmeldung Kapitalerhoehung Kyc Aml
- `lebenszyklus-bilinguale-vertragserstellung` — Lebenszyklus Bilinguale Vertragserstellung
- `mandat-triage-mehrere-parallel` — Mandat Triage Mehrere Parallel
- `notar-paket-parteien-erfassen` — Notar Paket Parteien Erfassen
- `post-eintragung-rangruecktritt-formulieren` — Post Eintragung Rangruecktritt Formulieren
- `sacheinlagebericht-werthaltigkeit-begleitet` — Sacheinlagebericht Werthaltigkeit Begleitet
- `unterzeichnung-elektronisch-wandelereignis-eingang` — Unterzeichnung Elektronisch Wandelereignis Eingang

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Wandeldarlehen Lebenszyklus-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Investor.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
