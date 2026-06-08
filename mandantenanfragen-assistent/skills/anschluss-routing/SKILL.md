---
name: anschluss-routing
description: "Anschluss-Routing für Mandantenanfragen-Assistent: wählt den nächsten Spezial-Skill nach Engpass (Unverzügliche Antwort, Mandantenmail, Kanzleiprofil, Honorarinfo), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Mandantenanfragen Assistent** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `anfrage-eingang-parser` — Anfrage Eingang Parser
- `anrede-anwaltskanzleien-bittet` — Anrede Anwaltskanzleien Bittet
- `anrede-uebernehmen` — Anrede Uebernehmen
- `anwaltskanzleien-erstpruefung-und-mandatsziel` — Anwaltskanzleien Erstpruefung und Mandatsziel
- `bietet-fehlerkatalog` — Bietet Fehlerkatalog
- `bittet-internationaler-bezug-und-schnittstellen` — Bittet Internationaler Bezug und Schnittstellen
- `dankt-dsgvo-sonderfall-e-mail` — Dankt DSGVO Sonderfall E Mail
- `dringlichkeitsmarker-einwilligung-hinweis` — Dringlichkeitsmarker Einwilligung Hinweis
- `dsgvo-sonderfall-und-edge-case` — DSGVO Sonderfall und Edge Case
- `e-mail-erstantwort-und-terminrouting` — E Mail Erstantwort und Terminrouting
- `eingehenden-quellenkarte` — Eingehenden Quellenkarte
- `einwilligung-hinweis-datenschutz` — Einwilligung Hinweis Datenschutz
- `einwilligungshinweis-fristennotiz-und-naechster-schritt` — Einwilligungshinweis Fristennotiz und Naechster Schritt
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Mandantenanfragen Assistent-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Mandantenanfragen-Assistent.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 13 DSGVO
- Art. 28 DSGVO
- Art. 9 DSGVO
- § 203 StGB
- § 4 KSchG
- § 356 StGB
- § 29 VwVfG
- Art. 6 DSGVO
- § 5 TMG
- § 263 StGB
- Art. 32 DSGVO
- Art. 15 DSGVO

### Leitentscheidungen

- BGH VI ZR 7/20
- BGH VI ZR 246/19

