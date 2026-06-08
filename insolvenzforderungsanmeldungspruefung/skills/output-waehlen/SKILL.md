---
name: output-waehlen
description: "Output-Wahl für Insolvenzforderungsanmeldung: stimmt Adressat (Gläubiger, Insolvenzverwalter, Schuldner), Frist (Anmeldefrist im Eröffnungsbeschluss) und Form auf den Zweck ab — typische Outputs: Forderungsanmeldung mit Rang, Widerspruchsschreiben, Klage auf Feststellung."
---

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Insolvenzforderungsanmeldungspruefung** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.


## Fachlandkarte dieses Plugins

- `aktenanlage-batchregister` — Aktenanlage Batchregister
- `beleg-und-urkundencheck` — Beleg und Urkundencheck
- `bestreiten-interessen-betrag` — Bestreiten Interessen Betrag
- `bestreiten-mehrparteien-konflikt-und-interessen` — Bestreiten Mehrparteien Konflikt und Interessen
- `betrag-behoerden-gericht-und-registerweg` — Betrag Behoerden Gericht und Registerweg
- `dubletten-serienforderungen` — Dubletten Serienforderungen
- `feststellung-forderungsgrund-rang-grund` — Feststellung Forderungsgrund Rang Grund
- `forderungsanmeldung-mandantenkommunikation-redteam-qualitygate` — Forderungsanmeldung Mandantenkommunikation Redteam Qualitygate
- `forderungsanmeldung-vbuh-verhandlung-vergleich-eskalation` — Forderungsanmeldung Vbuh Verhandlung Vergleich Eskalation
- `forderungsgrund-rang-und-belegpruefung` — Forderungsgrund Rang und Belegpruefung
- `formalpruefung-174` — Formalpruefung 174
- `grund-betrag-zinsen` — Grund Betrag Zinsen
- `grund-risikoampel-und-gegenargumente` — Grund Risikoampel und Gegenargumente
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Insolvenzforderungsanmeldungspruefung (§ 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Pr) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Output

Format-Wahl mit kurzer Begründung, einer Alternative und fertigem Bausteinen; bei Insolvenzforderungsanmeldung sofort: Forderungsanmeldung mit Rang oder Widerspruchsschreiben.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
