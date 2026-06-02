---
name: legw-bmf-finanzmarktaufsicht-bafin-kwg-wpig
description: "Sachbereich Finanzmarktaufsicht (BaFin; KWG; WpIG) im Geschaeftsbereich BMF: Normbestand (KWG; ZAG; WpIG; WpHG; KAGB; VAG; FinDAG; FinStabG; SAG; BörsG.); Akteure (BaFin; Deutsche Bundesbank; ESMA; EBA; EIOPA; FSB.); EU-Bezug (CRR; CRD; MiFID II; AIFMD; UCITS; PSD2 und PSD3; DORA; MiCA.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmf (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmf (Heranfuehrung)."
---

# Finanzmarktaufsicht (BaFin; KWG; WpIG) (BMF)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass fuer das Spezialthema Finanzmarktaufsicht (BaFin; KWG; WpIG) im Geschaeftsbereich BMF. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte fuer dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmf`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmf`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: KWG; ZAG; WpIG; WpHG; KAGB; VAG; FinDAG; FinStabG; SAG; BörsG.

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

BaFin; Deutsche Bundesbank; ESMA; EBA; EIOPA; FSB.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behoerden im Vollzug; betroffene Laenderbehoerden; Verbaende; wissenschaftliche Beiraete; zustaendige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

CRR; CRD; MiFID II; AIFMD; UCITS; PSD2 und PSD3; DORA; MiCA.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Erlaubnistatbestand klar formulieren; Aufsichtsbefugnisse zuweisen; Konzern- und Beaufsichtigungsbruecke zur Bundesbank; Sanktionsrahmen; Verbraucherschutz im Finanzmarkt.

Schrittfolge fuer den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

Doppelregulierung EU plus national; Aufsichtsarbitrage; Insolvenzfaehigkeit von Banken; Crypto-Sektor; Wechselwirkung mit Geldwaeschegesetz.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Output

Sachfeld-Kompass:

```
Sachfeld:           Finanzmarktaufsicht (BaFin; KWG; WpIG)
Ressort:            BMF
Kernnormen:         KWG; ZAG; WpIG; WpHG; KAGB; VAG; FinDAG; FinStabG; SAG; BörsG.
Akteure/Aufsicht:   BaFin; Deutsche Bundesbank; ESMA; EBA; EIOPA; FSB.
EU/Voelkerrecht:    CRR; CRD; MiFID II; AIFMD; UCITS; PSD2 und PSD3; DORA; MiCA.
Pruefpunkte:        <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine:      <Sachfeld-spezifisch>
Naechste Skills:    legw-ressortaufgaben-bmf; normhierarchie-routing; 
                    normenkartierung; verfassungsmaessigkeit-quercheck;
                    europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmf` -> `legw-ressortaufgaben-bmf` -> `legw-bmf-finanzmarktaufsicht-bafin-kwg-wpig` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.
