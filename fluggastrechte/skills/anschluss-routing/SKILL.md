---
name: anschluss-routing
description: "Anschluss-Routing für Fluggastrechte VO 261/2004: wählt den nächsten Spezial-Skill nach Engpass (Verjährung 3 Jahre § 195 BGB, Buchungsbestätigung, Boardingpass, Verspätungsbestätigung), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fluggastrechte** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `abtretung-an-fluggastportal-spezial` — Abtretung AN Fluggastportal Spezial
- `airline-bonitaet-und-vollstreckung` — Airline Bonitaet und Vollstreckung
- `airline-standardausreden-annullierung` — Airline Standardausreden Annullierung
- `airline-standardausreden-pruefen` — Airline Standardausreden Pruefen
- `anlagen-bauen` — Anlagen Bauen
- `annullierung-oder-verspaetung-einordnen` — Annullierung Oder Verspaetung Einordnen
- `annullierung-schriftsatz-brief-memo-bausteine` — Annullierung Schriftsatz Brief Memo Bausteine
- `annullierung-schriftsatz-brief-und-memo-bausteine` — Annullierung Schriftsatz Brief und Memo Bausteine
- `anschluss-router` — Anschluss Router
- `anschlussflug-und-reiseplan` — Anschlussflug und Reiseplan
- `ausgleich-internationaler-bezug-schnittstellen` — Ausgleich Internationaler Bezug Schnittstellen
- `ausgleich-internationaler-bezug-und-schnittstellen` — Ausgleich Internationaler Bezug und Schnittstellen
- `ausnahmen-aussergewoehnliche-umstaende` — Ausnahmen Aussergewoehnliche Umstaende
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fluggastrechte-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?


## Normen & Rechtsprechung

Konkret zu prüfen:

- VO (EG) Nr. 261/2004 (Fluggastrechte)
- Art. 5 VO 261/2004 (Annullierung)
- Art. 6 VO 261/2004 (Verspätung)
- Art. 7 VO 261/2004 (Ausgleichszahlung 250/400/600 EUR)
- EuGH C-402/07 (Sturgeon)
## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fluggastrechte VO 261/2004.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
