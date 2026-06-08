---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Aktenaufbereiter Strafrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `aktenaufbereiter-strafrecht` — Aktenaufbereiter Strafrecht
- `akteneinsicht-uebersicht-aktenvorblatt-erstellen-anklageschrift` — Akteneinsicht Uebersicht Aktenvorblatt Erstellen Anklageschrift
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `beweismittel-katalog-beweisverwertungsverbote-beziehungsmatrix` — Beweismittel Katalog Beweisverwertungsverbote Beziehungsmatrix
- `beziehungen-spezial-chronologie-ergaenzbar` — Beziehungen Chronologie Ergaenzbar
- `ersatz-sonderfall-excel-faehige` — Ersatz Sonderfall Excel Faehige
- `fortlaufend-luecken-personenverzeichnis` — Fortlaufend Luecken Personenverzeichnis
- `fristenliste-strafverfahren-aktenlektuere-fristennotiz` — Fristenliste Strafverfahren Aktenlektuere Fristennotiz
- `kronzeugen-regelung-opferzeugen-besondere-personenverzeichnis` — Kronzeugen Regelung Opferzeugen Besondere Personenverzeichnis
- `revision-rechtsfehler-aktenaufbereiter-aktenvorblatt` — Revision Rechtsfehler Aktenaufbereiter Aktenvorblatt
- `sechs-u-haft-aussageanalyse-aussagepsychologie` — Sechs U Haft Aussageanalyse Aussagepsychologie
- `strafbefehl-einspruchsstrategie-strafzumessung-deutsches` — Strafbefehl Einspruchsstrategie Strafzumessung Deutsches
- `strafrecht-strafverteidigung-uebersichten` — Strafrecht Strafverteidigung Uebersichten
- `vermoegensabschoepfung-dritt-einziehung-verstaendigung-deal` — Vermoegensabschoepfung Dritt Einziehung Verstaendigung Deal

## Arbeitsweg

- Ergebnis sichten: Welche Aktenaufbereiter Strafrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Strafrechtliche Aktenaufbereitung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
