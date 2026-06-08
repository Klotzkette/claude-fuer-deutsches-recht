---
name: anschluss-routing
description: "Anschluss-Routing für Strafrechtliche Aktenaufbereitung: wählt den nächsten Spezial-Skill nach Engpass (Anklage-Erwiderungsfrist, Ermittlungsakte, Anklageschrift, Hauptverhandlungsprotokoll), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Aktenaufbereiter Strafrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `aktenaufbereiter-erstpruefung-und-mandatsziel` — Aktenaufbereiter Erstpruefung und Mandatsziel
- `aktenaufbereiter-strafrecht` — Aktenaufbereiter Strafrecht
- `akteneinsicht-uebersicht-aktenvorblatt` — Akteneinsicht Uebersicht Aktenvorblatt
- `aktenlektuere-fristennotiz-und-naechster-schritt` — Aktenlektuere Fristennotiz und Naechster Schritt
- `aktenvorblatt-erstellen` — Aktenvorblatt Erstellen
- `aktenvorblatt-schriftsatz-brief-und-memo-bausteine` — Aktenvorblatt Schriftsatz Brief und Memo Bausteine
- `anklageschrift-zerlegen` — Anklageschrift Zerlegen
- `aussageanalyse-aussagepsychologie` — Aussageanalyse Aussagepsychologie
- `beweismittel-katalog-beweisverwertungsverbote` — Beweismittel Katalog Beweisverwertungsverbote
- `beweisverwertungsverbote-pruefen` — Beweisverwertungsverbote Pruefen
- `beziehungen-spezial-chronologie-ergaenzbar` — Beziehungen Spezial Chronologie Ergaenzbar
- `beziehungsmatrix-personen-taten` — Beziehungsmatrix Personen Taten
- `chronologie-compliance-dokumentation-und-akte` — Chronologie Compliance Dokumentation und Akte
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

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
