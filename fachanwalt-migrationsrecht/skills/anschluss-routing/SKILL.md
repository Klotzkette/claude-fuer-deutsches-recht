---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Migrationsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-abschiebungsabwehr-sofort-arbeitgeber-arbeitsrecht` — Allgemein Abschiebungsabwehr Sofort Arbeitgeber Arbeitsrecht
- `arbeitgeberwechsel-asyl-anhoerung-asylg-ausbildungsduldung` — Arbeitgeberwechsel Asyl Anhörung Asylg Ausbildungsduldung
- `aufenthaltstitel-ausweisung-start-behoerdenkommunikation-blaue` — Aufenthaltstitel Ausweisung Start Behördenkommunikation Blaue
- `aufenthaltstitel-erstgespraech-mandatsannahme-fachanwalt-asyl` — Aufenthaltstitel Erstgespraech Mandatsannahme Fachanwalt Asyl
- `ba-zustimmung-beschaeftigungsduldung` — Ba Zustimmung Beschaeftigungsduldung
- `blaue-karte-blaue-karte-bleiberecht-25a-chancenaufenthalt` — Blaue Karte Blaue Karte Bleiberecht 25a Chancenaufenthalt
- `botschaft-visumtermin-workflow-chronologie-dokumentenstapel` — Botschaft Visumtermin Chronologie Dokumentenstapel
- `datenschutz-sicherheit-daueraufenthalt-eu-digitalbeweise-flucht` — Datenschutz Sicherheit Daueraufenthalt Eu Digitalbeweise Flucht
- `dublin-ueberstellung` — Dublin Ueberstellung
- `einbuergerung-lebensunterhalt-mehrstaatigkeit-strafen-einreise` — Einbuergerung Lebensunterhalt Mehrstaatigkeit Strafen Einreise
- `einbuergerung-start-fachkraefte-start` — Einbuergerung Start Fachkraefte Start
- `eurodac-treffer-fachanwalt` — Eurodac Treffer Fachanwalt
- `fachanwalt-migrationsrecht-aufenthaltstitel-ausweisung-bamf` — Fachanwalt Migrationsrecht Aufenthaltstitel Ausweisung Bamf
- `familiennachzug-ehegatte-kind-forscher-ict-freizuegigkeit-eu` — Familiennachzug Ehegatte Kind Forscher Ict Freizuegigkeit Eu

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

