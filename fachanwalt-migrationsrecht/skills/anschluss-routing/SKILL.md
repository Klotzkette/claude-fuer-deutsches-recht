---
name: anschluss-routing
description: "Anschluss-Routing für Fachanwalt Migrationsrecht: wählt den nächsten Spezial-Skill nach Engpass (§ 74 AsylG Klagefrist 2 Wochen / 1 Mon., Bescheid BAMF/ABH, Pass, Aufenthaltstitel), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Migrationsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `abschiebehaft-paragraf-62-aufenthg` — Abschiebehaft Paragraf 62 Aufenthg
- `abschiebungsabwehr-sofort-arbeitgeber` — Abschiebungsabwehr Sofort Arbeitgeber
- `arbeitgeberwechsel-asyl-anhoerung-asylg` — Arbeitgeberwechsel Asyl Anhoerung Asylg
- `asylantrag-folgeverfahren-paragraf-71-asylg` — Asylantrag Folgeverfahren Paragraf 71 Asylg
- `aufenthalt-paragraf-25a-aufenthg` — Aufenthalt Paragraf 25A Aufenthg
- `aufenthaltstitel` — Aufenthaltstitel
- `aufenthaltstitel-ausweisung-start` — Aufenthaltstitel Ausweisung Start
- `aufenthaltstitel-erstgespraech-mandatsannahme` — Aufenthaltstitel Erstgespraech Mandatsannahme
- `ausweisung-paragrafe-53-55-aufenthg` — Ausweisung Paragrafe 53 55 Aufenthg
- `ba-zustimmung-beschaeftigungsduldung` — BA Zustimmung Beschaeftigungsduldung
- `blaue-karte-bleiberecht-25a-chancenaufenthalt` — Blaue Karte Bleiberecht 25A Chancenaufenthalt
- `botschaft-visumtermin-dokumentenstapel` — Botschaft Visumtermin Dokumentenstapel
- `datenschutz-sicherheit-daueraufenthalt-eu` — Datenschutz Sicherheit Daueraufenthalt EU
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Migrationsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Migrationsrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 3 EMRK
- § 80 VwG
- § 36 AsylG
- § 71 AsylG
- § 74 AsylG
- Art. 6 GG
- Art. 8 EMRK
- § 81 AufenthG
- § 60a AufenthG
- § 123 VwG
- § 5 AufenthG
- § 10 StAG

### Leitentscheidungen

- EuGH C-490/16
- EuGH C-247/20

