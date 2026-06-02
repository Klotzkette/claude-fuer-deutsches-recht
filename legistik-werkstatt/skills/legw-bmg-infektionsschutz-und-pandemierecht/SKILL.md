---
name: legw-bmg-infektionsschutz-und-pandemierecht
description: "Sachbereich Infektionsschutz und Pandemierecht im Geschaeftsbereich BMG: Normbestand (IfSG; IGV-AusfG; ImpfschadenAnerkennung; SGB V (Tests und Impfen).); Akteure (RKI; PEI; BMG; Laender-Gesundheitsbehoerden; Gesundheitsaemter; STIKO.); EU-Bezug (ECDC; HERA; EU-Health Union; IGV der WHO.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmg (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmg (Heranfuehrung)."
---

# Infektionsschutz und Pandemierecht (BMG)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass fuer das Spezialthema Infektionsschutz und Pandemierecht im Geschaeftsbereich BMG. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte fuer dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmg`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmg`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: IfSG; IGV-AusfG; ImpfschadenAnerkennung; SGB V (Tests und Impfen).

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

RKI; PEI; BMG; Laender-Gesundheitsbehoerden; Gesundheitsaemter; STIKO.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behoerden im Vollzug; betroffene Laenderbehoerden; Verbaende; wissenschaftliche Beiraete; zustaendige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

ECDC; HERA; EU-Health Union; IGV der WHO.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Meldepflichten; Schutzmassnahmen; Impfempfehlungen; epidemische Lage; Bevoelkerungsschutz.

Schrittfolge fuer den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

Verhaeltnismaessigkeit; Foederalismus; Parlamentsvorbehalt; gerichtliche Kontrolle.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Output

Sachfeld-Kompass:

```
Sachfeld:           Infektionsschutz und Pandemierecht
Ressort:            BMG
Kernnormen:         IfSG; IGV-AusfG; ImpfschadenAnerkennung; SGB V (Tests und Impfen).
Akteure/Aufsicht:   RKI; PEI; BMG; Laender-Gesundheitsbehoerden; Gesundheitsaemter; STIKO.
EU/Voelkerrecht:    ECDC; HERA; EU-Health Union; IGV der WHO.
Pruefpunkte:        <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine:      <Sachfeld-spezifisch>
Naechste Skills:    legw-ressortaufgaben-bmg; normhierarchie-routing; 
                    normenkartierung; verfassungsmaessigkeit-quercheck;
                    europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmg` -> `legw-ressortaufgaben-bmg` -> `legw-bmg-infektionsschutz-und-pandemierecht` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.
