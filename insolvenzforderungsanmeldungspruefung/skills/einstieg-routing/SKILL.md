---
name: einstieg-routing
description: "Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Insolvenzforderungsanmeldungsprüfung."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Insolvenzforderungsanmeldungspruefung** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `aktenanlage-batchregister` — Aktenanlage Batchregister
- `beleg-und-urkundencheck` — Beleg und Urkundencheck
- `bestreiten-interessen-betrag` — Bestreiten Interessen Betrag
- `bestreiten-mehrparteien-konflikt-und-interessen` — Bestreiten Mehrparteien Konflikt und Interessen
- `betrag-behoerden-gericht-und-registerweg` — Betrag Behoerden Gericht und Registerweg
- `dubletten-serienforderungen` — Dubletten Serienforderungen
- `feststellung-forderungsgrund-rang-grund` — Feststellung Forderungsgrund Rang Grund
- `forderungsanmeldung-mandantenkommunikation-redteam-qualitygate` — Forderungsanmeldung Mandantenkommunikation Redteam Qualitygate
- `vbuh-verhandlung-vergleich-und-eskalation` — Forderungsanmeldung Vbuh Verhandlung Vergleich Eskalation
- `forderungsgrund-rang-und-belegpruefung` — Forderungsgrund Rang und Belegpruefung
- `formalpruefung-174` — Formalpruefung 174
- `grund-betrag-zinsen` — Grund Betrag Zinsen
- `grund-risikoampel-und-gegenargumente` — Grund Risikoampel und Gegenargumente
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Insolvenzforderungsanmeldungspruefung sind § 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Pr. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
