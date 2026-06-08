---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Ki Richtlinie Kanzleien** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

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

- Ergebnis sichten: Welche Ki Richtlinie Kanzleien-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von KI-Richtlinie für Kanzleien.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 28 DSGVO
- § 203 StGB
- Art. 22 DSGVO
- Art. 9 DSGVO
- Art. 6 DSGVO
- § 2 UrhG
- Art. 30 DSGVO
- Art. 46 DSGVO
- Art. 13 DSGVO
- § 44b UrhG
- Art. 35 DSGVO
- § 5 UrhG

### Leitentscheidungen

- BGH VI ZR 273/16

