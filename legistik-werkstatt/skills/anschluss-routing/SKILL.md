---
name: anschluss-routing
description: "Anschluss-Routing für Legistik-Werkstatt (Gesetzgebung): wählt den nächsten Spezial-Skill nach Engpass (Beteiligungsfristen, Referentenentwurf, Kabinettvorlage, BR-Drucksache), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Legistik Werkstatt** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `aa-ausfuhrkontrolle` — AA Ausfuhrkontrolle
- `aa-ausfuhrkontrolle-und-aussenwirtschaftsdimension` — AA Ausfuhrkontrolle und Aussenwirtschaftsdimension
- `aa-eu-bmi-verwaltungsverfahren` — AA EU BMI Verwaltungsverfahren
- `aa-eu-grundlagen-und-ratsverfahren` — AA EU Grundlagen und Ratsverfahren
- `aa-konsular-bmas-arbeitsrecht` — AA Konsular Bmas Arbeitsrecht
- `aa-konsular-und-passrecht` — AA Konsular und Passrecht
- `aa-sanktionsumsetzung-internationale` — AA Sanktionsumsetzung Internationale
- `aa-sanktionsumsetzung-und-internationale-abkommen` — AA Sanktionsumsetzung und Internationale Abkommen
- `aa-voelkerrecht-und-vertragsgesetzgebung` — AA Voelkerrecht und Vertragsgesetzgebung
- `aenderungs-formular-portal-einreichungslogik` — Aenderungs Formular Portal Einreichungslogik
- `aenderungs-formular-portal-und-einreichung` — Aenderungs Formular Portal und Einreichung
- `baut-quellenkarte` — Baut Quellenkarte
- `begruendung-allgemein-und-besonders` — Begruendung Allgemein und Besonders
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Normenanker

Arbeitsfokus: **Anschluss-Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 20 Abs. 3 GG` — Gesetzesbindung.
- `Art. 76 Abs. 1 GG` — Gesetzesinitiative.
- `Art. 77 Abs. 1 GG` — Gesetzesbeschluss.
- `Art. 80 Abs. 1 GG` — Verordnungsermächtigung.
- `Art. 84 Abs. 1 GG` — Verwaltungsvollzug.
- `§ 42 Abs. 1 GGO` — Gesetzgebungsvorhaben.
- `§ 43 Abs. 1 GGO` — Ressortabstimmung.
- `§ 44 Abs. 1 GGO` — Gesetzesfolgen.
- `§ 45 GGO` — Beteiligung.
- `§ 46 GGO` — Rechtsförmlichkeit.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Ergebnis sichten: Welche Legistik Werkstatt-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Legistik-Werkstatt (Gesetzgebung).

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
