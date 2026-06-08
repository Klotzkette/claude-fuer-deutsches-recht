---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Mandantenanfragen Assistent** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `anrede-anwaltskanzleien-bittet` — Anrede Anwaltskanzleien Bittet
- `dankt-dsgvo-sonderfall-e-mail` — Dankt Dsgvo Sonderfall E Mail
- `dringlichkeitsmarker-einwilligung-hinweis-erstantwort-generator` — Dringlichkeitsmarker Einwilligung Hinweis Erstantwort Generator
- `erstantwort-foermlich-mail` — Erstantwort Foermlich Mail
- `folgekorrespondenz-vorbereiten-konfliktcheck-vorab-ma` — Folgekorrespondenz Vorbereiten Konfliktcheck Vorab Ma
- `ma-einfuehrung-ma-erstvermerk-ma-konfliktcheck` — Ma Einfuehrung Ma Erstvermerk Ma Konfliktcheck
- `ma-mandant-manda-erstgespraechsleitfaden-manda-erstkontakt` — Ma Mandant Manda Erstgespraechsleitfaden Manda Erstkontakt
- `manda-mandatsablehnung-rechtsschutz-eintrittsanfrage` — Manda Mandatsablehnung Rechtsschutz Eintrittsanfrage
- `mandantenanfragen-anfrage-eingang-anrede-uebernehmen` — Mandantenanfragen Anfrage Eingang Anrede Uebernehmen
- `mehrsprachige-antwort-muster-erstantwort-spam-massen` — Mehrsprachige Antwort Muster Erstantwort Spam Massen
- `nennt-sachverhalt-telefon` — Nennt Sachverhalt Telefon
- `telefonische-terminvergabe-interessen-transkription-beweislast` — Telefonische Terminvergabe Interessen Transkription Beweislast
- `uebernimmt-telefon-konfiguration-transkriptionsdienst-erklaerung` — Uebernimmt Telefon Konfiguration Transkriptionsdienst Erklaerung

## Arbeitsweg

- Ergebnis sichten: Welche Mandantenanfragen Assistent-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Mandantenanfragen-Assistent.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 13 DSGVO
- Art. 28 DSGVO
- Art. 9 DSGVO
- § 203 StGB
- § 4 KSchG
- § 356 StGB
- § 29 VwVfG
- Art. 6 DSGVO
- § 5 TMG
- § 263 StGB
- Art. 32 DSGVO
- Art. 15 DSGVO

### Leitentscheidungen

- BGH VI ZR 7/20
- BGH VI ZR 246/19

