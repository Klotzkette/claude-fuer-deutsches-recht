---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Verkehrsowi Verteidiger** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `alkohol-drogen-beweisverwertung-standardisiert-verkehrsowi` — Alkohol Drogen Beweisverwertung Standardisiert Verkehrsowi
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `amtsgericht-drogen-interessen-einspruch` — Amtsgericht Drogen Interessen Einspruch
- `anhoerung-verkehrsowi-einspruch-messverfahren-geschwindigkeit` — Anhörung Verkehrsowi Einspruch Messverfahren Geschwindigkeit
- `fahrverbot-geschwindigkeit-handy` — Fahrverbot Geschwindigkeit Handy
- `hauptverhandlung-sonderfall-messakte-messung-fahrverbot` — Hauptverhandlung Sonderfall Messakte Messung Fahrverbot
- `punkte-rotlicht-verkehrsowi` — Punkte Rotlicht Verkehrsowi
- `simulation-training-verjaehrung-zustellung-zeugen-polizei` — Simulation Training Verjährung Zustellung Zeugen Polizei
- `verkehrsowi-haertefall-fahrverbot-hauptverhandlung-amtsgericht` — Verkehrsowi Haertefall Fahrverbot Hauptverhandlung Amtsgericht
- `verkehrsowi-punkte-fahrverbot-rechtsbeschwerde-rotlicht-abstand` — Verkehrsowi Punkte Fahrverbot Rechtsbeschwerde Rotlicht Abstand
- `verteidiger-beweislast-verkehrsowi-aktenanlage-akteneinsicht` — Verteidiger Beweislast Verkehrsowi Aktenanlage Akteneinsicht
- `vowi-akteneinsicht` — Vowi Akteneinsicht
- `vowi-bussgeldbescheid-verkehrsowi-quality-gate` — Vowi Bussgeldbescheid Verkehrsowi Quality Gate
- `vowi-handyverstoss-akteneinsicht-alkohol` — Vowi Handyverstoss Akteneinsicht Alkohol

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
