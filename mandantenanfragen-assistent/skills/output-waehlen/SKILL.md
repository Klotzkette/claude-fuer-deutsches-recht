---
name: output-waehlen
description: "Output wählen im Mandantenanfragen-Triage: Diese Output-Weiche für Mandantenanfragen Assistent entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist."
---

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Mandantenanfragen Assistent** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

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

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Mandantenanfragen Assistent (DSGVO) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Output

Format-Wahl mit kurzer Begründung, einer Alternative und fertigem Bausteinen; bei Mandantenanfragen-Assistent sofort: Antwortentwurf oder Empfangsbestätigung.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
