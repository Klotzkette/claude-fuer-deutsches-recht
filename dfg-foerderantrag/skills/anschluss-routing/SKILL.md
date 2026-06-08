---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Dfg Foerderantrag** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `anfaenger-antraege-dfg` — Anfaenger Antraege Dfg
- `dfg-bis-200k-begutachtung-light` — Dfg Bis 200k Begutachtung Light
- `dfg-eigenanteil-und-grundausstattung` — Dfg Eigenanteil Und Grundausstattung
- `dfg-eigene-vorarbeiten-darstellen` — Dfg Eigene Vorarbeiten Darstellen
- `dfg-erstantragsteller-besondere-checks` — Dfg Erstantragsteller Besondere Checks
- `dfg-finanzplan-module-personal-geraete` — Dfg Finanzplan Module Personal Geraete
- `dfg-foerderstrategie-schnell-oder-gross` — Dfg Foerderstrategie Schnell Oder Gross
- `dfg-grossgeraete-und-cluster-antrag` — Dfg Grossgeraete Und Cluster Antrag
- `dfg-grundsystem-foerderlinien` — Dfg Grundsystem Foerderlinien
- `dfg-internationale-kooperation-aufbau` — Dfg Internationale Kooperation Aufbau
- `dfg-ki-ethik-forschungsdaten` — Dfg Ki Ethik Forschungsdaten
- `dfg-kollegen-review-organisieren` — Dfg Kollegen Review Organisieren
- `dfg-koselleck-500k-125m` — Dfg Koselleck 500k 125m

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

