---
name: anschluss-routing
description: "Für Anschluss-Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Urteilsbauer und Relationsmacher."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Urteilsbauer Relationsmacher** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `aktenintake-schriftsatz-brief-und-memo-bausteine` — Aktenintake Schriftsatz Brief und Memo Bausteine
- `aktenintake-zivil` — Aktenintake Zivil
- `amts-aktenintake-zivil-anspruchsgrundlagen` — Amts Aktenintake Zivil Anspruchsgrundlagen
- `amts-fristen-form-zustaendigkeit` — Amts Fristen Form Zustaendigkeit
- `anspruchsgrundlagen-pruefen` — Anspruchsgrundlagen Prüfen
- `berufungsfest-beschluss-bauen-beweisbeschluss` — Berufungsfest Beschluss Bauen Beweisbeschluss
- `berufungsfest-pruefen` — Berufungsfest Prüfen
- `beschluss-bauen-zpo` — Beschluss Bauen ZPO
- `beschluss-tatbestand-beweis-und-belege` — Beschluss Tatbestand Beweis und Belege
- `beschluss-tatbestandsmerkmale` — Beschluss Tatbestandsmerkmale
- `beweisbeschluss-vorbereiten` — Beweisbeschluss Vorbereiten
- `beweiswuerdigung-mit-richter-input` — Beweiswuerdigung mit Richter Input
- `beweiswuerdigung-quellenkarte` — Beweiswuerdigung Quellenkarte
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Urteilsbauer Relationsmacher-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.


## Quellenkontrolle

Für die Relation gelten keine universellen materiell-rechtlichen Leitentscheidungen. Zuerst Anspruchsgrundlage und Einwendungen des konkreten Streitstoffs bestimmen; pro Rechtssatz nur eine Entscheidung mit Gericht, Datum, Aktenzeichen, tragender Aussage und Quelle verwenden. Verfahrensrechtlich insbesondere Paragraf 138, Paragraf 139, Paragraf 253 Absatz 2 Nummer 2, Paragraf 286, Paragraf 296 und Paragraf 308 ZPO fallbezogen prüfen.
