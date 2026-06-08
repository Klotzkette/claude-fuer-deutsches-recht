---
name: anschluss-routing
description: "Anschluss-Routing für Berufsrechts-KI bei Vertragsprüfung: wählt den nächsten Spezial-Skill nach Engpass (Rechtzeitige Mandatsannahme, AVV-Vertrag, Mandatsvertrag, Datenschutzfolgeabschätzung), dokumentiert Router-Entscheidung mit Begründung."
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
- `belehrung-abschlussprodukt-uebergabe` — Belehrung Abschlussprodukt Uebergabe
- `belehrung-abschlussprodukt-und-uebergabe` — Belehrung Abschlussprodukt und Uebergabe
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

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Berufsrechts-KI bei Vertragsprüfung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 203 StGB
- Art. 28 DSGVO
- § 204 StGB
- § 62a StBerG
- § 2 HRG
- § 4 HRG
- § 7 HRG
- § 15 HRG
- § 16 HRG
- § 70 VwG
- § 123 VwG
- Art. 32 DSGVO

### Leitentscheidungen

- BGH VI ZR 36/20
- BGH VIII ZR 78/20

