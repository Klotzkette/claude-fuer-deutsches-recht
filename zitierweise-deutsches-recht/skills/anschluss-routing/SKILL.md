---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Zitierweise deutsches Recht."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Zitierweise Deutsches Recht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `aktenzeichen-schriftsatz-brief-und-memo-bausteine` — Aktenzeichen Schriftsatz Brief und Memo Bausteine
- `aufsatz-interessen` — Aufsatz Interessen
- `aufsatz-interessen-beckrs-blindzitate` — Aufsatz Interessen Beckrs Blindzitate
- `beckrs-zahlen-schwellen-und-berechnung` — Beckrs Zahlen Schwellen und Berechnung
- `blindzitate-internationaler-bezug-und-schnittstellen` — Blindzitate Internationaler Bezug und Schnittstellen
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `datum-entscheidungsform-spezial-gericht` — Datum Entscheidungsform Spezial Gericht
- `entscheidungsform-risikoampel-und-gegenargumente` — Entscheidungsform Risikoampel und Gegenargumente
- `fristen-und-risikoampel` — Fristen und Risikoampel
- `gericht-dokumentenmatrix-und-lueckenliste` — Gericht Dokumentenmatrix und Lueckenliste
- `hauszitierweise-juristische-kommentar` — Hauszitierweise Juristische Kommentar
- `juristische-erstpruefung-und-mandatsziel` — Juristische Erstpruefung und Mandatsziel
- `kaltstart-triage` — Kaltstart Triage
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Regelungs- und Quellenanker

Arbeitsfokus: **Anschluss-Routing**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `§ 130 Nr. 6 ZPO` — verantworteter Schriftsatz.
- `§ 138 Abs. 1 ZPO` — Wahrheit und Vollständigkeit.
- `§ 253 Abs. 2 ZPO` — bestimmter Klagegrund.
- `§ 313 Abs. 3 ZPO` — Entscheidungsgründe.
- `§ 540 Abs. 1 ZPO` — Berufungsurteil.
- `§ 267 Abs. 1 StPO` — strafgerichtliche Urteilsgründe.
- `§ 117 Abs. 2 VwGO` — verwaltungsgerichtliche Urteilsgründe.
- `§ 51 UrhG` — zulässiges Zitieren fremder Texte.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Ergebnis sichten: Welche Zitierweise Deutsches Recht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
