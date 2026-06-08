---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Hausarbeitenmacher** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-hausarbeit-start-workflow-chronologie` — Allgemein Hausarbeit Start Chronologie
- `aufgabenstellung-erfassen-fachgebiet-routing-gliederung` — Aufgabenstellung Erfassen Fachgebiet Routing Gliederung
- `ausfluegen-didaktisches-durch` — Ausfluegen Didaktisches Durch
- `behutsame-frech-haeufige-fehler-selbstkontrolle-abgabe` — Behutsame Frech Haeufige Fehler Selbstkontrolle Abgabe
- `europarecht-anwendbarkeit-hausarbeiten-bearbeitungsplan` — Europarecht Anwendbarkeit Hausarbeiten Bearbeitungsplan
- `europarecht-interessen-fertigen-sonderfall-fuehrt` — Europarecht Interessen Fertigen Sonderfall Fuehrt
- `gutachtenstil-vs-haus-fussnotenstil-literaturrecherche-leitfaden` — Gutachtenstil Vs Haus Fussnotenstil Literaturrecherche Leitfaden
- `haus-plagiatscheck-haus-themaeingrenzung-meinungsstreit` — Haus Plagiatscheck Haus Themaeingrenzung Meinungsstreit
- `juristische-liefert-beweislast-rechtstheorie` — Juristische Liefert Beweislast Rechtstheorie
- `methodenlehre-auslegung-öffentliches-statthaft-professor` — Methodenlehre Auslegung Oeffentliches Statthaft Professor
- `rechtstheorie-rechtsphilosophie-seminararbeit-modus-adressaten` — Rechtstheorie Rechtsphilosophie Seminararbeit Modus Adressaten
- `schleimerei-seminararbeiten-sokratisch` — Schleimerei Seminararbeiten Sokratisch
- `strafrecht-zivilrecht-strafrecht-rechtswidrigkeit` — Strafrecht Zivilrecht Strafrecht Rechtswidrigkeit
- `subsumtion-schritt-verfassungsrecht-grundrechtspruefung` — Subsumtion Schritt Verfassungsrecht Grundrechtspruefung

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

