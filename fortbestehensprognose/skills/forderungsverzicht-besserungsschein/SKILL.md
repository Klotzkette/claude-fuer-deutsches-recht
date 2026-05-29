---
name: forderungsverzicht-besserungsschein
description: "Erzeugt eine Forderungsverzichtsvereinbarung mit Besserungsschein. Gläubiger verzichtet auf Forderung — bei Wiedererstarken der Zahlungsfähigkeit der Schuldnerin lebt die Forderung wieder auf. Effekt im insolvenzrechtlichen Status die verzichtete Forderung wird nicht passiviert. Steuerliche Folge beim Schuldner Ertragsbuchung (Sanierungserlös Sanierungsgewinn § 3a EStG bei Sanierungsbedarf). Beim Gläubiger Forderungsausfall ggf abzugsfähig."
---

# Forderungsverzicht mit Besserungsschein

## Wirkung

Gläubiger verzichtet auf eine Forderung. Effekt:

- **Im Status**: Forderung entfaellt aus den Passiva. Bilanzbild verbessert sich.
- **Liquidität**: keine direkte Liquiditätszuflussverbesserung (die Forderung war ggf ohnehin nicht in den nächsten 12 Monaten zur Zahlung fällig).
- **Bilanz**: Ertrag (Sanierungserloes).

Mit **Besserungsschein**: Wenn die Schuldnerin später wieder zahlungsfähig wird lebt die Forderung wieder auf. Der Verzicht ist also bedingt.

## Anwendungsfall

- Bank verzichtet auf Teil-Tilgung eines Darlehens.
- Lieferant verzichtet auf Forderung mit Besserungsschein als Sanierungsbeitrag.
- Hauptgesellschafter verzichtet auf Forderung (statt Rangrücktritt).

## Steuerliche Folgen

### Beim Schuldner

Ertragsbuchung Sanierungserloes. **Sanierungsgewinn § 3a EStG** kann steuerbefreit sein wenn die Voraussetzungen (Sanierungsabsicht Sanierungsfähigkeit Sanierungseignung Gläubigergleichbehandlung) erfüllt sind.

Vor Unterzeichnung **steuerliche Beratung** zwingend.

### Beim Gläubiger

Forderungsausfall regelmäßig als Betriebsausgabe abzugsfähig. Bei Banken Wertberichtigung. Steuerlich vor Verzicht prüfen lassen.

## Mustervorlage

```
FORDERUNGSVERZICHTSVEREINBARUNG MIT BESSERUNGSSCHEIN

zwischen

  [Vor- und Nachname Gläubiger]
  [Anschrift]
  - im Folgenden "der Gläubiger" -

und

  [Firma der Schuldnerin]
  vertreten durch [Geschäftsführer]
  [Anschrift]
  HRB [...] AG [...]
  - im Folgenden "die Schuldnerin" -

1. Praeambel

Der Gläubiger ist Inhaber folgender Forderung gegen die Schuldnerin:

  [Bezeichnung der Forderung]
  Hauptforderung [Betrag] EUR
  zuzueglich Zinsen
  zum [Stichtag] insgesamt [Gesamtbetrag] EUR

Die Schuldnerin befindet sich in einer angespannten wirtschaftlichen Lage 
und hat eine Fortbestehensprognose nach § 19 Abs. 2 InsO erstellt. Mit
Sanierungsbeitrag durch den Gläubiger ist die Prognose positiv.

2. Verzicht

2.1 Der Gläubiger verzichtet hiermit gegenüber der Schuldnerin auf die 
oben bezeichnete Forderung in voller Höhe einschließlich Zinsen und 
Nebenforderungen.

2.2 Die Forderung erlischt im Status der Schuldnerin und ist in der 
insolvenzrechtlichen Status-Aufstellung nicht mehr zu passivieren.

3. Besserungsschein

3.1 Der Verzicht ist bedingt durch das Wiedererstarken der Zahlungsfähigkeit 
der Schuldnerin.

3.2 Die Forderung lebt wieder auf wenn

  a) die Schuldnerin im Jahresabschluss ein positives Eigenkapital aufweist 
     oder
  b) die Schuldnerin in einem Geschäftsjahr einen Jahresueberschuss von mehr 
     als [X] EUR erwirtschaftet oder
  c) der Gläubiger bei nachhaltiger Verbesserung der wirtschaftlichen Lage 
     in Textform die Wiederaufnahme verlangt.

3.3 Der Rückzahlungsbetrag betraegt im Fall des Wiederauflebens

  - höchstens den urspruenglichen Forderungsbetrag,
  - mindestens [X] Prozent des verfügbaren Eigenkapitals des Folgejahres,
  - wird in Raten über [N] Monate getilgt.

3.4 Die Besserungsklausel laeuft für [N] Jahre ab Unterzeichnung. Nach 
Ablauf entfaellt die Wiederauflebensmöglichkeit endgültig.

4. Steuerliche Hinweise

Die Parteien sind sich bewusst dass dieser Verzicht beim Schuldner Ertrag 
ausloest. Vor Unterzeichnung wurde steuerlicher Rat eingeholt.

5. Form und Wirksamkeit

5.1 Diese Vereinbarung ist beidseitig unterzeichnet wirksam.

5.2 Änderungen und Ergänzungen bedürfen der Schriftform.

5.3 Gerichtsstand: [Sitz der Schuldnerin].

[Ort], [Datum]

___________________________
[Gläubiger]


___________________________
[Geschäftsführer]
für die Schuldnerin
```

## Hinweise

### Echtheit der Sanierungsabsicht

Wird der Forderungsverzicht später als Scheingeschäft angesehen (z. B. weil keine ernsthafte Sanierungsabsicht vorlag) kann er anfechtbar sein.

### Gläubigergleichbehandlung

Bei Sanierungsverzicht ist auf Gläubigergleichbehandlung zu achten. Wenn nur einzelne Gläubiger verzichten und andere nicht ist das in Ordnung — solange der Vorgang nicht als Begueneten-Bezugnahme zu Lasten der nicht-verzichtenden Gläubiger zu werten ist.

### Besserungsschein-Trigger genau definieren

Der Trigger für das Wiederaufleben muss objektiv und nachprüfbar sein. Klauseln wie "wenn es uns wieder besser geht" sind ungeeignet.

## Ausgabe

- `forderungsverzicht-besserungsschein-<glaeubiger>.docx`.
- Steuerliche Prüfer-Flag — Steuerberater einbinden.
- Statusupdate (Skill `bilanzieller-status-aufnehmen`): Forderung entfaellt aus den Passiva.
- Eintrag im Sanierungsbausteine-Tracker.


## Aktuelle Leitentscheidungen — Forderungsverzicht und Besserungsschein

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Forderungsverzicht

§ 19 Abs. 2 InsO (Ueberschuldungsbereinigung) → § 3a EStG (steuerfreier Sanierungsgewinn) → § 397 BGB (Erlass/Verzicht) → § 158 BGB (haengende Bedingung Besserungsschein) → § 133 InsO (Anfechtungsrisiko bei selektivem Verzicht)

## Triage — Forderungsverzicht Check

1. **Glaeubiger und Betrag?** Wer verzichtet auf wie viel?
2. **Steuerliche Folge?** Sanierungsgewinn § 3a EStG: Nachweise Sanierungsplan, Sanierungsabsicht, Sanierungseignung vorbereiten.
3. **Besserungsschein-Formulierung?** Bedingung klar definiert (Wiederherstellung ZF anhand konkreter Liquiditaets-Schwelle).
4. **Anfechtungsschutz?** Verzicht muss Teil eines Gesamtsanierungskonzepts sein (IDW S 6 Qualitaet) um Vorsatzanfechtung § 133 InsO auszuschliessen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.