---
name: einstieg-routing
description: "Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Fachanwalt Vergaberecht."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Fachanwalt Vergaberecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `schadensersatz-181-gwb` — Aufklaerung
- `ausschluss-bieter-paragraf-124-gwb` — Ausschluss Bieter Paragraf 124 GWB
- `bieterstrategie-go-no-go` — Bieterstrategie GO Eforms TED Eignung
- `eignungskriterien-paragraf-122-gwb` — Eignungskriterien Paragraf 122 GWB
- `eu-schwelle-vergabeordnung-richtlinie-2014-24` — EU Schwelle Vergabeordnung Richtlinie 2014 24
- `de-facto-vergabe-klage` — Facto
- `workflow-chronologie-und-belegmatrix` — Facto Vergabe
- `it-sicherheits-vergabe-bsi-it-sig-2` — IT Sicherheits Konzessionsvergabe Konzvgv
- `kaltstart-triage` — Kaltstart Triage
- `konzvgv-risikoampel-und-gegenargumente` — Konzvgv Rahmenvereinbarung International
- `mandantenpadlet-vergabe-canvas` — Mandantenpadlet Vergabe Triage Vergaberecht
- `nachpruefungsverfahren-paragraf-160-gwb` — Nachpruefungsverfahren Paragraf 160 GWB
- `vergabekammer-sachverhalt-abstellungsantraege` — Vergabekammer-Sachverhalt, Rügehistorie und konkrete Abstellungsanträge: Zurückversetzung, Neuwertung, Änderung der Vergabeunterlagen, Aufhebung, Akteneinsicht und Zuschlagsverbot.
- `vergabekammer-verhandlung-vergleich-und-eskalation` — Mündliche Verhandlung, Aufklärungsrunde, Vergleichskorridor und OLG-Eskalation im laufenden VK-Verfahren.
- `nebenabrede-paragraf-58-vgv` — Nebenabrede Paragraf 58 VGV
- `dokumente-intake` — Dokumente Intake
- `output-waehlen` — Output Waehlen

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fachanwalt Vergaberecht sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Bei Bieterangriffen immer das **konkrete Ziel** erfragen oder aus der Akte ableiten: bloße Rüge, vorgerichtliche Abhilfe, Änderung der Vergabeunterlagen, Fristverlängerung, Wiederaufnahme des Angebots, Neuwertung, Zurückversetzung, Untersagung des Zuschlags, Unwirksamkeitsfeststellung oder Schadensersatz. Wenn dieses Ziel auf eine VK-Entscheidung oder VK-Verhandlung zuläuft, direkt zu `vergabekammer-sachverhalt-abstellungsantraege` oder `vergabekammer-verhandlung-vergleich-und-eskalation` routen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
