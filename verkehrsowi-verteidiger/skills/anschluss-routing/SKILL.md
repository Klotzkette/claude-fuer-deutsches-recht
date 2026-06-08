---
name: anschluss-routing
description: "Anschluss-Routing für Verkehrs-OWi-Verteidigung: wählt den nächsten Spezial-Skill nach Engpass (Einspruch 2 Wochen § 67 OWiG, Bußgeldbescheid, Anhörungsbogen, Messprotokoll), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Verkehrsowi Verteidiger** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `abstand-quellenkarte` — Abstand Quellenkarte
- `akteneinsicht-internationaler-bezug-und-schnittstellen` — Akteneinsicht Internationaler Bezug und Schnittstellen
- `alkohol-compliance-dokumentation-und-akte` — Alkohol Compliance Dokumentation und Akte
- `alkohol-drogen-beweisverwertung` — Alkohol Drogen Beweisverwertung
- `amtsgericht-drogen-interessen-einspruch` — Amtsgericht Drogen Interessen Einspruch
- `anhoerung-verkehrsowi-einspruch-messverfahren` — Anhoerung Verkehrsowi Einspruch Messverfahren
- `bussgeldbescheid-tatbestand-beweis-und-belege` — Bussgeldbescheid Tatbestand Beweis und Belege
- `drogen-mehrparteien-konflikt-und-interessen` — Drogen Mehrparteien Konflikt und Interessen
- `einspruch-dokumentenmatrix-und-lueckenliste` — Einspruch Dokumentenmatrix und Lueckenliste
- `fahrverbot-geschwindigkeit-handy` — Fahrverbot Geschwindigkeit Handy
- `geschwindigkeit-verhandlung-vergleich-und-eskalation` — Geschwindigkeit Verhandlung Vergleich und Eskalation
- `handy-zahlen-schwellen-und-berechnung` — Handy Zahlen Schwellen und Berechnung
- `hauptverhandlung-sonderfall-messakte-messung` — Hauptverhandlung Sonderfall Messakte Messung
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Verkehrsowi Verteidiger-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Verkehrs-OWi-Verteidigung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
