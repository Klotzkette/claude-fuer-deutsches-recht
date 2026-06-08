---
name: bmg-arzneimittel-medizinprodukterecht
description: "Sachbereich Arzneimittel- und Medizinprodukterecht im Geschaeftsbereich BMG: Normbestand (AMG; MPG; MPDG; ApBetrO; AMNOG; MedBVSV.); Akteure (BfArM; PEI; G-BA; DIMDI/BfArM; Länder-Aufsichten.); EU-Bezug (VO 726/2004; MDR; IVDR; EMA.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmg (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmg (Heranfuehrung)."
---

# Arzneimittel- und Medizinprodukterecht (BMG)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass für das Spezialthema Arzneimittel- und Medizinprodukterecht im Geschaeftsbereich BMG. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte für dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmg`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmg`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: AMG; MPG; MPDG; ApBetrO; AMNOG; MedBVSV.

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

BfArM; PEI; G-BA; DIMDI/BfArM; Länder-Aufsichten.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behörden im Vollzug; betroffene Länderbehoerden; Verbaende; wissenschaftliche Beiraete; zuständige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

VO 726/2004; MDR; IVDR; EMA.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Zulassungsverfahren; Pharmakovigilanz; klinische Pruefungen; Medizinprodukte-Konformitaet; Preisbildung (AMNOG).

Schrittfolge für den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

EU-Konformitaet; Notified Bodies; Versorgungsengpaesse; Off-label-Use.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Normenanker

Arbeitsfokus: **Arzneimittel- und Medizinprodukterecht (BMG)**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 5 Abs. 1 DSGVO` — Datenschutzgrundsätze.
- `Art. 6 Abs. 1 DSGVO` — Rechtsgrundlage.
- `Art. 22 DSGVO` — automatisierte Entscheidungen.
- `Art. 35 DSGVO` — Datenschutz-Folgenabschätzung.
- `§ 3 OZG` — Nutzerkonten/Portalverbund live prüfen.
- `§ 5 EGovG` — elektronische Aktenführung live prüfen.
- `Art. 3 KI-VO` — Begriffe.
- `Art. 6 KI-VO` — Hochrisiko-Systeme.


Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Output

Sachfeld-Kompass:

```
Sachfeld: Arzneimittel- und Medizinprodukterecht
Ressort: BMG
Kernnormen: AMG; MPG; MPDG; ApBetrO; AMNOG; MedBVSV.
Akteure/Aufsicht: BfArM; PEI; G-BA; DIMDI/BfArM; Länder-Aufsichten.
EU/Voelkerrecht: VO 726/2004; MDR; IVDR; EMA.
Pruefpunkte: <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine: <Sachfeld-spezifisch>
Naechste Skills: legw-ressortaufgaben-bmg; normhierarchie-routing;
 normenkartierung; verfassungsmaessigkeit-quercheck;
 europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmg` -> `legw-ressortaufgaben-bmg` -> `legw-bmg-arzneimittel-und-medizinprodukterecht` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis für den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.
