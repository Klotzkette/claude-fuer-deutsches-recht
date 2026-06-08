---
name: dokumente-intake
description: "Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen."
---

# Dokumentenintake

## Einsatzlage

Dieser Dokumenten-Intake für **Ki Richtlinie Kanzleien** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `anonymisierung-pseudonymisierung-automatisierte-entscheidungen` — Anonymisierung Pseudonymisierung Automatisierte Entscheidungen
- `anwaelten-berufsrechtskonforme-beruht` — Anwaelten Berufsrechtskonforme Beruht
- `bias-diskriminierung-regelsatz-erstellen-dienstleister-due` — Bias Diskriminierung Regelsatz Erstellen Dienstleister Due
- `bora-brak-dsgvo` — Bora Brak Dsgvo
- `dokumentationspflichten-protokoll-dsgvo-executive-summary` — Dokumentationspflichten Protokoll Dsgvo Executive Summary
- `geschgehg-halluzinations-handhabung-kanzlei-kontext` — Geschgehg Halluzinations Handhabung Kanzlei Kontext
- `hinweisen-kanzleien-pflegt` — Hinweisen Kanzleien Pflegt
- `kennzeichnungspflichten-veroeffentlichungen-ki-kompetenz-vo` — Kennzeichnungspflichten Veroeffentlichungen Ki Kompetenz Vo
- `kirk-leitfaden-kirk-prompts-kr-executive` — Kirk Leitfaden Kirk Prompts Kr Executive
- `literatur-quellen-prompting-leitfaden-rdg-chatbot` — Literatur Quellen Prompting Leitfaden Rdg Chatbot
- `nutzungsrichtlinie-auftragsverarbeitungsvertrag-musterklauseln` — Nutzungsrichtlinie Auftragsverarbeitungsvertrag Musterklauseln
- `rechtsabteilungen-syndikus-verordnung-interessen` — Rechtsabteilungen Syndikus Verordnung Interessen
- `richtlinien-skelett-richtlinien-update-schatten-aufdeckung` — Richtlinien Skelett Richtlinien Update Schatten Aufdeckung

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Ki Richtlinie Kanzleien-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: DSGVO — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Output

Dokumentenregister mit K/B-Nummerierung, Chronologie, Beweiswerttabelle und Rückfrageliste an Kanzlei.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
