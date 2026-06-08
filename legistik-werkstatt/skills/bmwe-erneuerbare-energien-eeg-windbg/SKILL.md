---
name: bmwe-erneuerbare-energien-eeg-windbg
description: "Sachbereich Erneuerbare Energien (EEG; WindBG) im Geschaeftsbereich BMWE: Normbestand (EEG; WindBG; KWKG; SolarSpitzenG; BImSchG-Bezuege; ROG.); Akteure (Bundesnetzagentur; Bafa; Länderbehoerden Genehmigung; Planungsbehoerden.); EU-Bezug (RED III; State Aid Guidelines for Energy and Environment.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmwe (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmwe (Heranfuehrung)."
---

# Erneuerbare Energien (EEG; WindBG) (BMWE)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass für das Spezialthema Erneuerbare Energien (EEG; WindBG) im Geschaeftsbereich BMWE. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte für dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmwe`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmwe`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: EEG; WindBG; KWKG; SolarSpitzenG; BImSchG-Bezuege; ROG.

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

Bundesnetzagentur; Bafa; Länderbehoerden Genehmigung; Planungsbehoerden.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behörden im Vollzug; betroffene Länderbehoerden; Verbaende; wissenschaftliche Beiraete; zuständige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

RED III; State Aid Guidelines for Energy and Environment.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Foerderhoehen und Ausschreibungen; Flaechenzielwerte; Planungsbeschleunigung; Buergerenergie.

Schrittfolge für den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

Beihilferechtliche Notifizierung; Planungsrecht; Akzeptanz vor Ort.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Normenanker

Arbeitsfokus: **Erneuerbare Energien (EEG; WindBG) (BMWE)**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 23 Abs. 1 GG` — Mitwirkung in EU-Angelegenheiten.
- `Art. 288 Abs. 3 AEUV` — Richtlinie und Umsetzungsspielraum.
- `Art. 4 Abs. 3 EUV` — Grundsatz loyaler Zusammenarbeit.
- `Art. 258 AEUV` — Vertragsverletzungsverfahren.
- `Art. 267 AEUV` — Vorabentscheidung.
- `§ 43 Abs. 1 GGO` — Ressortabstimmung.
- `§ 44 Abs. 1 GGO` — Folgenabschätzung.
- `§ 45 GGO` — Beteiligung.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Output

Sachfeld-Kompass:

```
Sachfeld: Erneuerbare Energien (EEG; WindBG)
Ressort: BMWE
Kernnormen: EEG; WindBG; KWKG; SolarSpitzenG; BImSchG-Bezuege; ROG.
Akteure/Aufsicht: Bundesnetzagentur; Bafa; Länderbehoerden Genehmigung; Planungsbehoerden.
EU/Voelkerrecht: RED III; State Aid Guidelines for Energy and Environment.
Pruefpunkte: <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine: <Sachfeld-spezifisch>
Naechste Skills: legw-ressortaufgaben-bmwe; normhierarchie-routing;
 normenkartierung; verfassungsmaessigkeit-quercheck;
 europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmwe` -> `legw-ressortaufgaben-bmwe` -> `legw-bmwe-erneuerbare-energien-eeg-windbg` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis für den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.
