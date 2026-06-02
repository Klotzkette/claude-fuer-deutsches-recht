---
name: legw-bmftr-forschungsfoerderung-und-ressortforschung
description: "Sachbereich Forschungsfoerderung und Ressortforschung im Geschaeftsbereich BMFTR: Normbestand (BHO; ANBest-P; SubvG; AGVO (Forschung); AGVO; Rahmenprogramm.); Akteure (BMFTR; Projekttraeger (PT; PT-DLR; PT Juelich); Ressortforschungseinrichtungen.); EU-Bezug (Horizon Europe; ERC; EIC; AGVO.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmftr (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmftr (Heranfuehrung)."
---

# Forschungsfoerderung und Ressortforschung (BMFTR)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass fuer das Spezialthema Forschungsfoerderung und Ressortforschung im Geschaeftsbereich BMFTR. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte fuer dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmftr`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmftr`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: BHO; ANBest-P; SubvG; AGVO (Forschung); AGVO; Rahmenprogramm.

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

BMFTR; Projekttraeger (PT; PT-DLR; PT Juelich); Ressortforschungseinrichtungen.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behoerden im Vollzug; betroffene Laenderbehoerden; Verbaende; wissenschaftliche Beiraete; zustaendige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

Horizon Europe; ERC; EIC; AGVO.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Foerderbekanntmachung; Antragsbearbeitung; Auswahlverfahren; Erfolgskontrolle; Verwertungsregeln; Open-Access.

Schrittfolge fuer den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

Doppelfoerderung; Auslegung des Forschungsbegriffs; Auswertung; IP-Rechte.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Output

Sachfeld-Kompass:

```
Sachfeld:           Forschungsfoerderung und Ressortforschung
Ressort:            BMFTR
Kernnormen:         BHO; ANBest-P; SubvG; AGVO (Forschung); AGVO; Rahmenprogramm.
Akteure/Aufsicht:   BMFTR; Projekttraeger (PT; PT-DLR; PT Juelich); Ressortforschungseinrichtungen.
EU/Voelkerrecht:    Horizon Europe; ERC; EIC; AGVO.
Pruefpunkte:        <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine:      <Sachfeld-spezifisch>
Naechste Skills:    legw-ressortaufgaben-bmftr; normhierarchie-routing; 
                    normenkartierung; verfassungsmaessigkeit-quercheck;
                    europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmftr` -> `legw-ressortaufgaben-bmftr` -> `legw-bmftr-forschungsfoerderung-und-ressortforschung` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.
