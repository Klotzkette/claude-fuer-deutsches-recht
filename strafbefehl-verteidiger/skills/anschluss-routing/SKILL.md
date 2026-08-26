---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Strafbefehl-Verteidiger."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Strafbefehl Verteidiger** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `aktenanlage-fehlerkatalog` — Aktenanlage Fehlerkatalog
- `akteneinsicht-behoerden-gericht-und-registerweg` — Akteneinsicht Behoerden Gericht und Registerweg
- `deal-beweislast-einspruch` — Deal Beweislast Einspruch
- `einspruch-risikoampel-und-gegenargumente` — Einspruch Risikoampel und Gegenargumente
- `einspruchsentscheidung-und-folgen` — Einspruchsentscheidung und Folgen
- `einstellung-153a-hauptverhandlung` — Einstellung 153a Hauptverhandlung
- `einstellung-fahrerlaubnis` — Einstellung Fahrerlaubnis
- `fahrerlaubnis-mandantenentscheidung` — Fahrerlaubnis Mandantenentscheidung
- `hauptverhandlung-international-schnittstellen` — Hauptverhandlung International Schnittstellen
- `mandantenkommunikation-redteam-qualitygate` — Mandantenkommunikation Redteam Qualitygate
- `nebenfolgen-fahrerlaubnis-strafbefehl` — Nebenfolgen Fahrerlaubnis Strafbefehl
- `nebenfolgen-strafbefehl-strafbefehls` — Nebenfolgen Strafbefehl Strafbefehls
- `pflichtverteidigung-quellenkarte` — Pflichtverteidigung Quellenkarte
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Strafbefehl Verteidiger-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
