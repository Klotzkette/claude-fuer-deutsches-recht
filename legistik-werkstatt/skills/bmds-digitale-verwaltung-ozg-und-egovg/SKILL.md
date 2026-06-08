---
name: bmds-digitale-verwaltung-ozg-und-egovg
description: "Sachbereich Digitale Verwaltung (OZG; EGovG) im Geschaeftsbereich BMDS: Normbestand (OZG; OZG-AeG; EGovG; EGovG-Länder; eIDAS-DurchG; XOeV.); Akteure (BMDS; ITZBund; FITKO; Länder-CIOs; Bundesdruckerei.); EU-Bezug (Single Digital Gateway; eIDAS 2.0; EU Digital Wallet.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmds (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmds (Heranfuehrung)."
---

# Digitale Verwaltung (OZG; EGovG) (BMDS)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass für das Spezialthema Digitale Verwaltung (OZG; EGovG) im Geschaeftsbereich BMDS. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte für dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmds`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmds`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: OZG; OZG-AeG; EGovG; EGovG-Länder; eIDAS-DurchG; XOeV.

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

BMDS; ITZBund; FITKO; Länder-CIOs; Bundesdruckerei.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behörden im Vollzug; betroffene Länderbehoerden; Verbaende; wissenschaftliche Beiraete; zuständige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

Single Digital Gateway; eIDAS 2.0; EU Digital Wallet.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Online-Faehigkeit; Once-Only-Prinzip; Identifizierungsdienste; Registeranbindung.

Schrittfolge für den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

Foederale Vollzugskette; Registerharmonisierung; Datenschutz; Akzeptanz.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Normenanker

Arbeitsfokus: **Digitale Verwaltung (OZG; EGovG) (BMDS)**. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

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
Sachfeld: Digitale Verwaltung (OZG; EGovG)
Ressort: BMDS
Kernnormen: OZG; OZG-AeG; EGovG; EGovG-Länder; eIDAS-DurchG; XOeV.
Akteure/Aufsicht: BMDS; ITZBund; FITKO; Länder-CIOs; Bundesdruckerei.
EU/Voelkerrecht: Single Digital Gateway; eIDAS 2.0; EU Digital Wallet.
Pruefpunkte: <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine: <Sachfeld-spezifisch>
Naechste Skills: legw-ressortaufgaben-bmds; normhierarchie-routing;
 normenkartierung; verfassungsmaessigkeit-quercheck;
 europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmds` -> `legw-ressortaufgaben-bmds` -> `legw-bmds-digitale-verwaltung-ozg-und-egovg` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis für den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.
