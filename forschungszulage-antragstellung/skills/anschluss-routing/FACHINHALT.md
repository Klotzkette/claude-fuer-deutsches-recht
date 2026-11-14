---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Forschungszulage-Antragstellung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Forschungszulage Antragstellung** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `abgrenzung-adaptiver-antrag` — Abgrenzung Adaptiver Antrag
- `abgrenzung-compliance` — Abgrenzung Compliance
- `ablehnung-nachbesserung-einspruch` — Ablehnung Nachbesserung Einspruch
- `adaptiver-dokumentenmatrix` — Adaptiver Dokumentenmatrix
- `adaptiver-dokumentenmatrix-und-lueckenliste` — Adaptiver Dokumentenmatrix und Lueckenliste
- `antrag-zahlen-schwellen-und-berechnung` — Antrag Zahlen Schwellen und Berechnung
- `antrag-zahlen-schwellenwerte` — Antrag Zahlen Schwellenwerte
- `antragstellung-auszahlung-beihilfen` — Antragstellung Auszahlung Beihilfen
- `auftragsforschung-vertragsgestaltung` — Auftragsforschung Vertragsgestaltung
- `auszahlung-internationaler-bezug` — Auszahlung Internationaler Bezug
- `auszahlung-internationaler-bezug-und-schnittstellen` — Auszahlung Internationaler Bezug und Schnittstellen
- `beihilfen-beweislast-darlegungslast` — Beihilfen Beweislast Darlegungslast
- `beihilfen-beweislast-und-darlegungslast` — Beihilfen Beweislast und Darlegungslast
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Normenanker

Arbeitsfokus: **Anschluss-Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 1 FZulG` — Anspruchsberechtigung.
- `§ 2 Abs. 1 FZulG` — begünstigtes F&E-Vorhaben.
- `§ 3 FZulG` — förderfähige Aufwendungen.
- `§ 4 FZulG` — Höhe der Zulage.
- `§ 5 FZulG` — Antrag.
- `§ 6 FZulG` — Bescheinigung.
- `§ 10 FZulG` — Festsetzung/Auszahlung.
- `§ 90 Abs. 1 AO` — Mitwirkung und Belege.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Ergebnis sichten: Welche Forschungszulage Antragstellung-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
