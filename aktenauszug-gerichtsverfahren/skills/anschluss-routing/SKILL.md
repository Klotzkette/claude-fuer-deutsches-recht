---
name: anschluss-routing
description: "Anschluss-Routing für Aktenauszüge zivilgerichtlicher Verfahren: wählt den nächsten Spezial-Skill nach Engpass (Akteneinsicht im laufenden Verfahren jederzeit, Klageschrift, Klageerwiderung, Schriftsätze), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Aktenauszug Gerichtsverfahren** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `akten-mandantenkommunikation-entscheidungsvorlage` — Akten Mandantenkommunikation Entscheidungsvorlage
- `aktenauszug-erstellen` — Aktenauszug Erstellen
- `aktenauszug-strukturpruefung-akzg-bauleiter` — Aktenauszug Strukturpruefung Akzg Bauleiter
- `aktenauszug-tatbestand-beweis-und-belege` — Aktenauszug Tatbestand Beweis und Belege
- `aktenauszug-verfahrensidentifikation-gericht` — Aktenauszug Verfahrensidentifikation Gericht
- `akzg-aktenauszug-bauleiter` — Akzg Aktenauszug Bauleiter
- `akzg-multiparteienverfahren-konsolidierung-spezial` — Akzg Multiparteienverfahren Konsolidierung Spezial
- `akzg-vertraulichkeit-redaction-spezial` — Akzg Vertraulichkeit Redaction Spezial
- `akzg-zeitstrahl-anlagenverzeichnis-extrakt` — Akzg Zeitstrahl Anlagenverzeichnis Extrakt
- `anlagenverzeichnis-extrakt` — Anlagenverzeichnis Extrakt
- `anwaltsschriftsatz-beweislast-beweismittel` — Anwaltsschriftsatz Beweislast Beweismittel
- `anwaltsschriftsatz-stilrichtlinie` — Anwaltsschriftsatz Stilrichtlinie
- `arbeitsgerichtsverfahren-modus-terminkalender` — Arbeitsgerichtsverfahren Modus Terminkalender
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Aktenauszug Gerichtsverfahren-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Aktenauszüge zivilgerichtlicher Verfahren.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
