---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: hausarbeitenmacher — Didaktisches Plugin für juristische."
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
- `fachgebiet-routing-zivil-oeffentlich-straf` — Fachgebiet Routing Zivil Öffentlich Straf
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

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
