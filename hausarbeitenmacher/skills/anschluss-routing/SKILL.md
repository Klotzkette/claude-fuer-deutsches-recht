---
name: anschluss-routing
description: "Anschluss-Routing für Jura-Hausarbeiten: wählt den nächsten Spezial-Skill nach Engpass (Hausarbeits-Abgabefrist, Sachverhalt, Literaturverzeichnis, Gliederung), dokumentiert Router-Entscheidung mit Begründung."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Hausarbeitenmacher** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.


## Fachlandkarte dieses Plugins

- `adressaten-formular-portal-und-einreichung` — Adressaten Formular Portal und Einreichung
- `aufgabenstellung-erfassen-fachgebiet` — Aufgabenstellung Erfassen Fachgebiet
- `ausfluegen-didaktisches-durch` — Ausfluegen Didaktisches Durch
- `bearbeitungsplan-erstellen` — Bearbeitungsplan Erstellen
- `behutsame-frech-haeufige-fehler` — Behutsame Frech Haeufige Fehler
- `didaktisches-erstpruefung-und-mandatsziel` — Didaktisches Erstpruefung und Mandatsziel
- `durch-schriftsatz-brief-und-memo-bausteine` — Durch Schriftsatz Brief und Memo Bausteine
- `europarecht-anwendbarkeit-hausarbeiten` — Europarecht Anwendbarkeit Hausarbeiten
- `europarecht-interessen-fertigen-sonderfall` — Europarecht Interessen Fertigen Sonderfall
- `fachgebiet-routing-zivil-oeffentlich-straf` — Fachgebiet Routing Zivil Oeffentlich Straf
- `fertigen-sonderfall-und-edge-case` — Fertigen Sonderfall und Edge Case
- `fuehrt-risikoampel-und-gegenargumente` — Fuehrt Risikoampel und Gegenargumente
- `gliederung-mit-tiefenstruktur` — Gliederung mit Tiefenstruktur
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Hausarbeitenmacher-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Jura-Hausarbeiten.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 267 AEUV
- § 242 StGB
- § 24 StGB
- § 263 StGB
- § 40 VwG
- Art. 20 GG
- § 22 StGB
- Art. 5 GG
- § 74 VwG
- § 15 StGB
- § 211 StGB
- § 70 VwG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

