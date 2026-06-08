---
name: einstieg-routing
description: "Einstieg, Triage und Routing für Energierecht (EnWG, EEG): ordnet Rolle (Erzeuger, Netzbetreiber, BNetzA), markiert Frist (Beschwerde BNetzA-Beschluss 1 Monat § 75 EnWG), wählt Norm (EnWG, EEG, KWKG) und Zuständigkeit (BNetzA), leitet zum passenden Spezial-Skill."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Energierecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.


## Fachlandkarte dieses Plugins

- `anfrage-mehrparteien-konflikt-und-interessen` — Anfrage Mehrparteien Konflikt und Interessen
- `anschluss` — Anschluss
- `bess-abfall-recycling-rueckbau` — Bess Abfall Recycling Rueckbau
- `bess-abstandsflaechen-baurecht-brandenburg` — Bess Abstandsflaechen Baurecht Brandenburg
- `bess-baurecht-brandenburg` — Bess Baurecht Brandenburg
- `bess-behoerdenstrategie` — Bess Behoerdenstrategie
- `bess-bimschg-und-4-bimschv` — Bess Bimschg und 4 Bimschv
- `bess-brandschutz-co-location-datenschutz` — Bess Brandschutz CO Location Datenschutz
- `bess-co-location-pv-wind` — Bess CO Location PV Wind
- `bess-datenschutz-video-leitwarte` — Bess Datenschutz Video Leitwarte
- `bess-dieselgenerator-notstrom` — Bess Dieselgenerator Notstrom
- `bess-epc-fca-agnes-finanzierung` — Bess EPC FCA Agnes Finanzierung
- `bess-fca-agnes-bnetza` — Bess FCA Agnes BNETZA
- `dokumente-intake` — Dokumente Intake
- `quellen-livecheck` — Quellen Livecheck

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Energierecht sind EEG, KWKG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Output

Triage-Notiz mit Frist, Norm, Zuständigkeit, Anschluss-Skill-Vorschlag und konkret nächstem Schritt. Bei Energierecht (EnWG, EEG) typische Eskalationsstufen: EnWG-Stellungnahme, Beschwerde BNetzA, Vergütungsantrag.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
