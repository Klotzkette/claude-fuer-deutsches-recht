---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Aktenauszug Gerichtsverfahren** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `aktenauszug-strukturpruefung-akzg-bauleiter-vertraulichkeit` — Aktenauszug Strukturpruefung Akzg Bauleiter Vertraulichkeit
- `akzg-zeitstrahl-anlagenverzeichnis-extrakt-anwaltsschriftsatz` — Akzg Zeitstrahl Anlagenverzeichnis Extrakt Anwaltsschriftsatz
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `anwaltsschriftsatz-beweislast-beweismittel-interessen` — Anwaltsschriftsatz Beweislast Beweismittel Interessen
- `arbeitsgerichtsverfahren-modus-terminkalender` — Arbeitsgerichtsverfahren Modus Terminkalender
- `beweismittel-gegenueberstellung-einleitungssatz-generator` — Beweismittel Gegenueberstellung Einleitungssatz Generator
- `erstellen-fristennotiz-gerichtsverfahren-verfahrensgeschichte` — Erstellen Fristennotiz Gerichtsverfahren Verfahrensgeschichte
- `gegenueberstellung-parteivortraege-rechtsargumente` — Gegenueberstellung Parteivortraege Rechtsargumente
- `parteivortrag-gegenueberstellung-rechtsargumente` — Parteivortrag Gegenueberstellung Rechtsargumente
- `sachverhaltschronologie-textbausteine-schnelle-stilrichtlinie` — Sachverhaltschronologie Textbausteine Schnelle Stilrichtlinie
- `schwerpunktthemen-identifikation-akten-aktenauszug` — Schwerpunktthemen Identifikation Akten Aktenauszug
- `strukturierter-strafprozess-modus-verwaltungsprozess-modus` — Strukturierter Strafprozess Modus Verwaltungsprozess Modus
- `verfahrensidentifikation-verfahrenszusammenfassung-absatz` — Verfahrensidentifikation Verfahrenszusammenfassung Absatz
- `verfahrensidentifikation-verfahrenszusammenfassung-rechtsweg` — Verfahrensidentifikation Verfahrenszusammenfassung Rechtsweg

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
