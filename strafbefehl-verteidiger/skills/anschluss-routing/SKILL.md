---
name: anschluss-routing
description: "Anschluss-Routing für Strafbefehl-Verteidigung: wählt den nächsten Spezial-Skill nach Engpass (§ 410 StPO Einspruch 2 Wochen, Strafbefehl, Ermittlungsakte, Einspruchsschrift), dokumentiert Router-Entscheidung mit Begründung."
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

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Strafbefehl-Verteidigung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 46 StGB
- § 69 StGB
- § 40 StGB
- § 44 StGB
- § 17 StGB
- § 69a StGB
- § 1 StGB
- § 15 StGB
- § 16 StGB
- § 42 StGB
- § 43 StGB
- § 201 StGB

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

