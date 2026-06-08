---
name: anschluss-routing
description: "Anschluss-Routing für Einfache/Leichte Sprache Jura: wählt den nächsten Spezial-Skill nach Engpass (keine harten Fristen, Originalbescheid, Vereinfachte Fassung, Lese-Test), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Einfache Leichte Sprache Jura** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `annaeherung-quellenkarte` — Annaeherung Quellenkarte
- `aufenthaltsrecht-mandant` — Aufenthaltsrecht Mandant
- `aufenthaltsrecht-mandant-betreuung` — Aufenthaltsrecht Mandant Betreuung
- `bauen-fristennotiz-naechster-schritt` — Bauen Fristennotiz Naechster Schritt
- `bauen-fristennotiz-und-naechster-schritt` — Bauen Fristennotiz und Naechster Schritt
- `bescheidmodus` — Bescheidmodus
- `bescheidmodus-02` — Bescheidmodus 02
- `betreuung-vormundschaft` — Betreuung Vormundschaft
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `einfache-sprache` — Einfache Sprache
- `experimentelle-glossar-sonderfall-jura` — Experimentelle Glossar Sonderfall Jura
- `experimentelle-schriftsatz-brief-memo-bausteine` — Experimentelle Schriftsatz Brief Memo Bausteine
- `familienrecht-erstgespraech` — Familienrecht Erstgespraech
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Einfache Leichte Sprache Jura-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?


## Normen & Rechtsprechung

Konkret zu prüfen:

- § 11 SGB I (Verständlichkeit)
- BGG (Behindertengleichstellungsgesetz) § 11
- BITV 2.0 (Barrierefreie Informationstechnik-Verordnung)
- UN-BRK Art. 9, 21
## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Einfache/Leichte Sprache Jura.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
