---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Strafzumessung** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `153a-stpo-iii-stpo-bewaehrung-stgb` — 153a Stpo Iii Stpo Bewaehrung Stgb
- `bewaehrung-auflagen-bewaehrungswiderruf-56f-freiheitsstrafe-ohne` — Bewaehrung Auflagen Bewaehrungswiderruf 56f Freiheitsstrafe Ohne
- `bewaehrung-interessen-deutschem-freiheitsstrafe` — Bewaehrung Interessen Deutschem Freiheitsstrafe
- `freiheitsstrafe-strafmass-geldstrafe-tagessatzanzahl-vs-stgb` — Freiheitsstrafe Strafmass Geldstrafe Tagessatzanzahl Vs Stgb
- `geldstrafe-grossen-rechtsmittel-gesamtstrafenfolgen` — Geldstrafe Grossen Rechtsmittel Gesamtstrafenfolgen
- `gesamtstrafenbildung-stgb-gestaendnis-strafmilderung` — Gesamtstrafenbildung Stgb Gestaendnis Strafmilderung
- `jgg-jugendstrafe-minder-schwerer-nachtraegliche` — Jgg Jugendstrafe Minder Schwerer Nachtraegliche
- `orientierung-triage-paragraph-stgb-besonders` — Orientierung Triage Paragraph Stgb Besonders
- `regelbeispiele-stgb-strafbefehl` — Regelbeispiele Stgb Strafbefehl
- `strafbefehl-stpo-strafmilderung-stgb-strafrahmen` — Strafbefehl Stpo Strafmilderung Stgb Strafrahmen
- `strafkammer-strafzumessung-strafzumessungstatsachen` — Strafkammer Strafzumessung Strafzumessungstatsachen
- `strafrecht-verfahrensstadium-strafbefehl-taeter-opfer` — Strafrecht Verfahrensstadium Strafbefehl Taeter Opfer
- `strafz-aufklaerungshilfe-kronzeuge-sicherungsverwahrung` — Strafz Aufklaerungshilfe Kronzeuge Sicherungsverwahrung
- `strafz-strafzumessungstatsachen-strafzumessungs-tatsachen` — Strafz Strafzumessungstatsachen Strafzumessungs Tatsachen

## Arbeitsweg

- Ergebnis sichten: Welche Strafzumessung-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (§ 56 StGB Bewährungszeit 2–5 Jahre, § 57 StGB 2/3-Reststrafenaussetzung, § 57a StGB lebenslange Freiheitsstrafe nach 15 Jahren), notwendige Dokumente (Bewährungsauflage, Tatumstandskatalog, Vorstrafenregisterauszug, Sachverständigengutachten, Schuldfähigkeitsbeurteilung), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Tatrichter, Verteidiger, Staatsanwaltschaft, Bewährungshelfer, Vollstreckungsbehörde oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Strafzumessung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 46 StGB
- § 49 StGB
- § 55 JGG
- § 55 StGB
- § 56 StGB
- § 46a StGB
- § 40 StGB
- § 47 StGB
- § 56f StGB
- § 54 StGB
- § 57 StGB
- § 105 JGG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

