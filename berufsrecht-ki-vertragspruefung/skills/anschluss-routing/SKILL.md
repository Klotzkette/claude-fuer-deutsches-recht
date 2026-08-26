---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: anwaltlichem Berufsrecht und Vertragsprüfung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Berufsrecht Ki Vertragspruefung** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `ai-act-rollen-kanzlei-provider-deployer-api` — AI ACT Rollen Kanzlei Provider Deployer API
- `anbietern-belehrung-sonderfall-edge` — Anbietern Belehrung Sonderfall Edge
- `anbietern-schriftsatz-brief-memo-bausteine` — Anbietern Schriftsatz Brief Memo Bausteine
- `art-50-ki-vo-schriftsatz-marketing-chatbot` — ART 50 KI VO Schriftsatz Marketing Chatbot
- `avv-grenzpruefung-brki-anbieter-eu` — AVV Grenzpruefung Brki Anbieter EU
- `avv-grenzpruefung-datenschutz` — AVV Grenzpruefung Datenschutz
- `belehrung-abschlussprodukt-uebergabe` — Belehrung Abschlussprodukt Übergabe
- `belehrung-abschlussprodukt-und-uebergabe` — Belehrung Abschlussprodukt und Übergabe
- `berufsrecht-sonderfall-edge-case` — Berufsrecht Sonderfall Edge Case
- `berufsrecht-sonderfall-und-edge-case` — Berufsrecht Sonderfall und Edge Case
- `berufsrechtliche-bnoto-interessen-brao` — Berufsrechtliche Bnoto Interessen BRAO
- `bnoto-interessen` — Bnoto Interessen
- `bnoto-mehrparteien-konflikt-und-interessen` — Bnoto Mehrparteien Konflikt und Interessen
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Berufsrecht Ki Vertragspruefung-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.


## Quellenkontrolle

Berufsrecht, Geheimnisschutz und Datenschutz getrennt prüfen: Paragraf 43a Absatz 2 und Paragraf 43e BRAO, Paragraf 2 BORA, Paragraf 203 StGB sowie Artikel 28 und 32 DSGVO. Eine Gerichtsentscheidung nur einsetzen, wenn ihr Sachverhalt die konkrete Vertrags-, Verschwiegenheits- oder Sicherheitsfrage trägt; ein nicht erläutertes Aktenzeichen ist kein Rechtsanker.
