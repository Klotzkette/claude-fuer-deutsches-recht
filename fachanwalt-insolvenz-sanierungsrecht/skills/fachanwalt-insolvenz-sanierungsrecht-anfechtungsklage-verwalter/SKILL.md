---
name: fachanwalt-insolvenz-sanierungsrecht-anfechtungsklage-verwalter
description: "Anfechtungsklage des Insolvenzverwalters nach §§ 129-147 InsO vorbereiten: Tatbestand je Rechtshandlung, § 130/131/133/134/135, Bargeschäft § 142, Rückgewähr § 143, Gegenleistung § 144, Verjährung § 146, Beweislast, KI-Kandidatenmatrix und Gegnerverteidigung. Output: Klagegerüst mit Beleg- und Risikoplan."
---

# Anfechtungsklage des Insolvenzverwalters

## Kaltstart

1. Welche Rechtshandlungen sollen eingeklagt werden, einzeln mit Datum, Betrag und Empfänger?
2. Ist der Zeitpunkt nach § 140 InsO geklärt oder nur das Buchungsdatum bekannt?
3. Welche Norm trägt jede einzelne Handlung: § 130, § 131, § 132, § 133, § 134 oder § 135 InsO?
4. Welche Belege gibt es zu Zahlungsunfähigkeit, Kenntnis, Gegenleistung und Gläubigerbenachteiligung?
5. Ist § 142 InsO als Verteidigung zu erwarten?
6. Gibt es eine Gegenleistung nach § 144 InsO?
7. Sind Verjährung und Hemmung nach § 146 InsO und BGB geprüft?
8. Ist die Klage wirtschaftlich sinnvoll oder ist ein Vergleich besser?

## Klagefähigkeitsgate

Keine Klage ohne:

- Eröffnungsbeschluss und Verwalterstellung.
- Insolvenzantrag und Eröffnungsdatum.
- transaktionsscharfe Darstellung.
- Tatbestand je Zahlung oder Sicherheit.
- Beleg für Zahlungsunfähigkeit und Kenntnis, soweit erforderlich.
- Zinsgrund nach § 143 Abs. 1 S. 3 InsO.
- Prüfung von § 142 und § 144 InsO.

## Tatbestandstabelle

| Norm | Schwerpunkt | Frist oder Zeitraum | Kenntnis |
|---|---|---|---|
| § 130 InsO | kongruente Deckung | drei Monate vor Antrag oder nach Antrag | Kenntnis der Zahlungsunfähigkeit oder des Antrags |
| § 131 InsO | inkongruente Deckung | letzter Monat, zweiter/dritter Monat | bei Nr. 1 keine; bei Nr. 2 Zahlungsunfähigkeit; bei Nr. 3 Kenntnis der Benachteiligung |
| § 132 InsO | unmittelbar nachteilige Handlung | drei Monate | je nach Fallgruppe |
| § 133 Abs. 1 InsO | Vorsatz | zehn Jahre | Kenntnis des Vorsatzes |
| § 133 Abs. 2 InsO | Deckungshandlung bei Vorsatz | vier Jahre | Kenntnis des Vorsatzes |
| § 133 Abs. 4 InsO | entgeltlicher Vertrag mit nahestehender Person | zwei Jahre | Vorsatzkenntnis oder Ausschluss prüfen |
| § 134 InsO | unentgeltliche Leistung | vier Jahre | keine Kenntnis nötig |
| § 135 InsO | Gesellschafterdarlehen | Sicherheit zehn Jahre, Befriedigung ein Jahr | keine Kenntnis nötig |
| § 142 InsO | Bargeschäft | Verteidigung | bei § 133 zusätzlich erkannte Unlauterkeit |

## KI-Vorarbeit

KI darf vor der Klage:

- Kandidaten aus Kontoauszügen, OPOS und E-Mails extrahieren.
- Zahlungsvorgänge nach Datum, Empfänger, Betrag und Quelle normalisieren.
- mögliche Normen vorschlagen.
- Beleglücken und Human-Review-Punkte markieren.

KI darf nicht:

- § 133-Vorsatz oder Kenntnis als bewiesen behaupten.
- Dreiecksverhältnisse final rechtlich auflösen.
- fehlende Belege durch Plausibilität ersetzen.

## Klagegerüst

```text
An das Landgericht [Ort]

Klage

des [Name], Insolvenzverwalter über das Vermögen der [Schuldnerin],
Kläger,

gegen

[Name und Anschrift],
Beklagte.

Anträge:
1. Die Beklagte wird verurteilt, an den Kläger EUR [Betrag] nebst Zinsen seit [Datum] zu zahlen.
2. Die Beklagte trägt die Kosten des Rechtsstreits.
3. Das Urteil ist vorläufig vollstreckbar.

Begründung:

I. Verfahren und Anfechtungsbefugnis
[Eröffnung, Verwalterbestellung, Massebezug]

II. Rechtshandlungen
| Datum | Betrag | Vorgang | Quelle | Tatbestand |
| ... |

III. Zahlungsunfähigkeit und Kenntnis
[Liquiditätsstatus, Zahlungseinstellung, Empfängerwissen, Gegenindizien]

IV. Rechtliche Würdigung je Tatbestand
[§ 130/131/133/134/135 getrennt]

V. Rechtsfolge
[§ 143 Rückgewähr, Zinsen nur Verzug oder § 291 BGB, § 144 Gegenleistung]
```

## Gegnerverteidigung antizipieren

| Einwand | Reaktion |
|---|---|
| Bargeschäft | Gleichwertigkeit, Unmittelbarkeit, § 133-Unlauterkeit prüfen |
| keine Kenntnis | konkrete Kenntnisbelege oder zwingende Umstände darlegen |
| Sanierungsversuch | bei § 133 Untauglichkeit und Kenntnis beweisen |
| Liquiditätsstatus unsubstantiiert | Einzelposten, Kontoauszüge und Fälligkeiten belegen |
| Verjährung | Ermittlungszeitraum und Kenntnisstand des Verwalters dokumentieren |
| Gegenleistung | § 144 InsO sauber behandeln |

## Leitlinien

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Output

| Abschnitt | Status |
|---|---|
| Klageantrag | [...] |
| Sachverhaltstabelle | [...] |
| Beweismittel | [...] |
| stärkster Tatbestand | [...] |
| größtes Prozessrisiko | [...] |
| Vergleichskorridor | [...] |

---

Hinweis: Keine Rechtsberatung. Klageentwurf nur nach Originalprüfung von Gesetz, Akte und aktueller Rechtsprechung verwenden.
