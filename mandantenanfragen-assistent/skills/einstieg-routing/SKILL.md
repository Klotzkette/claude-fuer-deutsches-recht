---
name: einstieg-routing
description: "Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Mandantenanfragen Assistent** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

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

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Mandantenanfragen Assistent sind DSGVO. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Mandantenanfragen-Assistent typische Eskalationsstufen: Antwortentwurf, Empfangsbestätigung, Rückfrage-Vorschlag.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
