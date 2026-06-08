---
name: anschluss-routing
description: "Anschluss-Routing für DFG-Förderantrag: wählt den nächsten Spezial-Skill nach Engpass (Antragsfrist Ausschreibungstermin, Projektbeschreibung, Finanzierungsplan, Lebenslauf), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Dfg Foerderantrag** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `adaptive-dokumentenmatrix-lueckenliste` — Adaptive Dokumentenmatrix Lueckenliste
- `adaptive-dokumentenmatrix-und-lueckenliste` — Adaptive Dokumentenmatrix und Lueckenliste
- `anfaenger-antraege-dfg` — Anfaenger Antraege DFG
- `anfaenger-risikoampel-gegenargumente` — Anfaenger Risikoampel Gegenargumente
- `antraege-zahlen-schwellen-und-berechnung` — Antraege Zahlen Schwellen und Berechnung
- `antraege-zahlen-schwellenwerte-berechnung` — Antraege Zahlen Schwellenwerte Berechnung
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `dfg-bis-200k-begutachtung-light` — DFG BIS 200k Begutachtung Light
- `dfg-eigenanteil-und-grundausstattung` — DFG Eigenanteil und Grundausstattung
- `dfg-eigene-vorarbeiten-darstellen` — DFG Eigene Vorarbeiten Darstellen
- `dfg-erstantragsteller-besondere-checks` — DFG Erstantragsteller Besondere Checks
- `dfg-erstpruefung-und-mandatsziel` — DFG Erstpruefung und Mandatsziel
- `dfg-finanzplan-module-personal-geraete` — DFG Finanzplan Module Personal Geraete
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Regelungs- und Quellenanker

Arbeitsfokus: **Anschluss-Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 91b Abs. 1 GG` — Forschungsförderung im Bund-Länder-System.
- `§ 23 BHO` — Zuwendungsvoraussetzungen.
- `§ 44 Abs. 1 BHO` — Bewilligung, Nachweis und Prüfung.
- `§ 7 Abs. 1 BHO` — Wirtschaftlichkeit und Sparsamkeit.
- `§ 48 Abs. 1 VwVfG` — Rücknahme rechtswidriger Bewilligungen.
- `§ 49 Abs. 1 VwVfG` — Widerruf rechtmäßiger Bewilligungen.
- `DFG-Kodex Leitlinie 1` — Redlichkeit.
- `DFG-Kodex Leitlinie 7` — Qualitätssicherung.
- `DFG-Kodex Leitlinie 14` — Autorschaft.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Ergebnis sichten: Welche Dfg Foerderantrag-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von DFG-Förderantrag.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 48 VwVfG
- § 49 VwVfG
- § 27 BDSG
- § 7 TierSchG
- § 8 TierSchG
- § 69a UrhG
- § 28 VwVfG
- § 39 VwVfG
- § 4 AWG
- § 5 AWG
- § 18 AWG
- Art. 44 DSGVO

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

