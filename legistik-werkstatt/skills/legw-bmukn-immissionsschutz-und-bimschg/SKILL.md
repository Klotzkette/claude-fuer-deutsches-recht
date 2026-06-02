---
name: legw-bmukn-immissionsschutz-und-bimschg
description: "Sachbereich Immissionsschutz (BImSchG) im Geschaeftsbereich BMUKN: Normbestand (BImSchG; BImSchV (1-44; TA Luft; TA Laerm); BBodSchG; UVPG; UmwRG.); Akteure (UBA; BfS (Strahlen); Laender-Genehmigungsbehoerden; Bundesverwaltung Verkehr.); EU-Bezug (IED-RL; Luftqualitaets-RL; Umgebungslaerm-RL.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmukn (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmukn (Heranfuehrung)."
---

# Immissionsschutz (BImSchG) (BMUKN)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass fuer das Spezialthema Immissionsschutz (BImSchG) im Geschaeftsbereich BMUKN. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte fuer dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmukn`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmukn`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: BImSchG; BImSchV (1-44; TA Luft; TA Laerm); BBodSchG; UVPG; UmwRG.

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

UBA; BfS (Strahlen); Laender-Genehmigungsbehoerden; Bundesverwaltung Verkehr.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behoerden im Vollzug; betroffene Laenderbehoerden; Verbaende; wissenschaftliche Beiraete; zustaendige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

IED-RL; Luftqualitaets-RL; Umgebungslaerm-RL.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Genehmigungspflicht; Stand der Technik; Anlageklassen; Beteiligungsverfahren; Klagebefugnis von Umweltverbaenden.

Schrittfolge fuer den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

Akzeptanz im Verfahren; UVP-Pflicht; Verbandsklage; Stand-der-Technik-Streit.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Output

Sachfeld-Kompass:

```
Sachfeld:           Immissionsschutz (BImSchG)
Ressort:            BMUKN
Kernnormen:         BImSchG; BImSchV (1-44; TA Luft; TA Laerm); BBodSchG; UVPG; UmwRG.
Akteure/Aufsicht:   UBA; BfS (Strahlen); Laender-Genehmigungsbehoerden; Bundesverwaltung Verkehr.
EU/Voelkerrecht:    IED-RL; Luftqualitaets-RL; Umgebungslaerm-RL.
Pruefpunkte:        <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine:      <Sachfeld-spezifisch>
Naechste Skills:    legw-ressortaufgaben-bmukn; normhierarchie-routing; 
                    normenkartierung; verfassungsmaessigkeit-quercheck;
                    europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmukn` -> `legw-ressortaufgaben-bmukn` -> `legw-bmukn-immissionsschutz-und-bimschg` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.
