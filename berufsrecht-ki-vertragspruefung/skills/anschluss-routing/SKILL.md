---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Berufsrecht Ki Vertragspruefung** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `ai-act-rollen-kanzlei-provider-deployer-api` — Ai Act Rollen Kanzlei Provider Deployer Api
- `br-ki-vertragspruefung-brki-rollout-chronologie` — Allgemein Brki Rollout Chronologie
- `anbietern-belehrung-sonderfall-edge` — Anbietern Belehrung Sonderfall Edge
- `art-50-ki-vo-schriftsatz-marketing-chatbot` — Art 50 Ki Vo Schriftsatz Marketing Chatbot
- `avv-grenzpruefung-brki-anbieter-brki-eu` — Avv Grenzpruefung Brki Anbieter Brki Eu
- `avv-grenzpruefung-datenschutz` — Avv Grenzpruefung Datenschutz
- `berufsrecht-ki-vertragspruefung-kaltstart-interview` — Berufsrecht Ki Vertragspruefung Kaltstart Interview
- `berufsrechtliche-bnoto-interessen-brao` — Berufsrechtliche Bnoto Interessen Brao
- `brki-anbieter-due-diligence` — Brki Anbieter Due Diligence
- `brki-eu-us-dpf-transferpruefung` — Brki Eu Us Dpf Transferpruefung
- `brki-rag-bro-grundlagen-cloud-act` — Brki Rag Bro Grundlagen Cloud Act
- `brki-rag-vertraulichkeit-spezial` — Brki Rag Vertraulichkeit Spezial
- `brki-rollout-trainings-workflow` — Brki Rollout Trainings Workflow
- `bro-grundlagen-ki-einsatz` — Bro Grundlagen Ki Einsatz

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

