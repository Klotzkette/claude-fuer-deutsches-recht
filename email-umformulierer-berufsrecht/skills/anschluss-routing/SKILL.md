---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Email Umformulierer Berufsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `email-berufsrecht-berufliche-korrespondenz` — Allgemeine Berufliche Korrespondenz
- `allgemeine-sonderfall-berufsrechtskonform-bora` — Allgemeine Sonderfall Berufsrechtskonform Bora
- `anrede-und-grussformeln` — Anrede Und Grussformeln
- `berufliche-fristennotiz-emotionale-steuerberater` — Berufliche Fristennotiz Emotionale Steuerberater
- `bora-konformitaetspruefung` — Bora Konformitaetspruefung
- `bora-konformitaetspruefung-brao-email-eingangsanalyse` — Bora Konformitaetspruefung Brao Email Eingangsanalyse
- `brao-interessen-fokus-formuliert` — Brao Interessen Fokus Formuliert
- `brao-konformitaetspruefung` — Brao Konformitaetspruefung
- `email-eingangsanalyse` — Email Eingangsanalyse
- `emotionale-trigger-ironie-sarkasmus-klare-bitte` — Emotionale Trigger Ironie Sarkasmus Klare Bitte
- `emotionale-trigger-katalog` — Emotionale Trigger Katalog
- `frist-und-mahnung-hoeflich` — Frist Und Mahnung Hoeflich
- `hoefliche-konformitaet-mails` — Hoefliche Konformitaet Mails

## Arbeitsweg

- Ergebnis sichten: Welche Email Umformulierer Berufsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von E-Mail-Umformulierung im Berufsrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 4 RVG
- § 10 RVG
- § 57 StBerG
- § 185 StGB
- § 57a StBerG
- Art. 5 GG
- § 240 StGB
- § 186 StGB
- § 203 StGB
- § 4a RVG
- § 261 StGB
- Art. 32 DSGVO

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

