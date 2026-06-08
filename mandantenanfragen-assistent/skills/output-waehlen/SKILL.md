---
name: output-waehlen
description: "Output-Wahl für Mandantenanfragen-Assistent: stimmt Adressat (Mandant, Anwalt, Sekretariat), Frist (Unverzügliche Antwort) und Form auf den Zweck ab — typische Outputs: Antwortentwurf, Empfangsbestätigung, Rückfrage-Vorschlag."
---

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Mandantenanfragen Assistent** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.


## Fachlandkarte dieses Plugins

- `anfrage-eingang-parser` — Anfrage Eingang Parser
- `anrede-anwaltskanzleien-bittet` — Anrede Anwaltskanzleien Bittet
- `anrede-uebernehmen` — Anrede Uebernehmen
- `anwaltskanzleien-erstpruefung-und-mandatsziel` — Anwaltskanzleien Erstpruefung und Mandatsziel
- `bietet-fehlerkatalog` — Bietet Fehlerkatalog
- `bittet-internationaler-bezug-und-schnittstellen` — Bittet Internationaler Bezug und Schnittstellen
- `dankt-dsgvo-sonderfall-e-mail` — Dankt DSGVO Sonderfall E Mail
- `dringlichkeitsmarker-einwilligung-hinweis` — Dringlichkeitsmarker Einwilligung Hinweis
- `dsgvo-sonderfall-und-edge-case` — DSGVO Sonderfall und Edge Case
- `e-mail-erstantwort-und-terminrouting` — E Mail Erstantwort und Terminrouting
- `eingehenden-quellenkarte` — Eingehenden Quellenkarte
- `einwilligung-hinweis-datenschutz` — Einwilligung Hinweis Datenschutz
- `einwilligungshinweis-fristennotiz-und-naechster-schritt` — Einwilligungshinweis Fristennotiz und Naechster Schritt
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

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
