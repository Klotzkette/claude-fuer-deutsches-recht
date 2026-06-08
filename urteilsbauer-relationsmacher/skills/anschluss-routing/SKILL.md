---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Urteilsbauer Relationsmacher** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `aktenintake-zivil` — Aktenintake Zivil
- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `amts-aktenintake-zivil-anspruchsgrundlagen` — Amts Aktenintake Zivil Anspruchsgrundlagen
- `anspruchsgrundlagen-pruefen` — Anspruchsgrundlagen Prüfen
- `berufungsfest-beschluss-bauen-beweisbeschluss-vorbereiten` — Berufungsfest Beschluss Bauen Beweisbeschluss Vorbereiten
- `berufungsfest-pruefen` — Berufungsfest Prüfen
- `beschluss-bauen-zpo` — Beschluss Bauen Zpo
- `beweisbeschluss-vorbereiten` — Beweisbeschluss Vorbereiten
- `beweiswuerdigung-mit-richter-input` — Beweiswuerdigung Mit Richter Input
- `beweiswuerdigung-richter-cisg-dsgvo-rechtswidriges` — Beweiswuerdigung Richter Cisg Dsgvo Rechtswidriges
- `cisg-pruefen` — Cisg Prüfen
- `dokumente-rendern-urteil-docx` — Dokumente Rendern Urteil Docx
- `dsgvo-rechtswidriges-produkt` — Dsgvo Rechtswidriges Produkt
- `entscheidungsgruende-redaktion-familienrichter-input` — Entscheidungsgruende Redaktion Familienrichter Input

## Arbeitsweg

- Ergebnis sichten: Welche Urteilsbauer Relationsmacher-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Urteilsbauer/Relationsmacher.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 38 FamFG
- § 13 GVG
- § 137 FamFG
- Art. 3 DSGVO
- Art. 9 DSGVO
- Art. 6 DSGVO
- § 70 VwG
- § 123 VwG
- § 71 GVG
- § 63 GKG
- Art. 103 GG
- § 111 FamFG

### Leitentscheidungen

- BGH VI ZR 96/11
- BGH VI ZR 113/17
- BGH VII ZR 213/10
- BGH VI ZR 39/20
- BGH VI ZR 40/20

