---
name: zulassungsgrenzen-check-amtsgericht
description: "Zulässigkeits-, Zuständigkeits- und Rechtsmittelgrenzen für Selbstvertreter vor dem Amtsgericht: § 23 GVG 10.000 EUR, Sonderzuständigkeiten, § 495a ZPO 1.000 EUR, § 511 ZPO Berufungsbeschwer 1.000 EUR, Übergangsfälle, Anwaltszwang und rote Flaggen."
---

# Zulassungsgrenzen-Check Amtsgericht

## Zweck

Dieser Skill prüft, ob ein Bürger seinen Fall wirklich vor dem Amtsgericht selbst führen kann und welche Wert- oder Zulassungsgrenzen später wichtig werden. Er verbindet Zuständigkeit, Verfahrensart und Rechtsmittel in einer klaren Ampel.

## Kernwerte Stand Mai 2026

| Thema | Grenze | Norm |
|---|---:|---|
| Amtsgericht allgemeine Zivilsache | bis einschließlich 10.000 EUR | § 23 Nr. 1 GVG |
| Landgericht allgemeine Zivilsache | über 10.000 EUR | § 71 GVG |
| Vereinfachtes Verfahren | bis einschließlich 1.000 EUR | § 495a ZPO |
| Berufung ohne Zulassung | Beschwer über 1.000 EUR | § 511 Abs. 2 Nr. 1 ZPO |
| Berufung mit Zulassung | Beschwer bis 1.000 EUR, wenn AG zulässt | § 511 Abs. 2 Nr. 2, Abs. 4 ZPO |

## Stichtag und Übergang

Prüfen Sie bei alten Verfahren immer die Übergangslage:

- Für neue Verfahren im Jahr 2026 gilt die AG-Grenze von 10.000 EUR.
- Für die Berufung gilt seit 2026 die Beschwerdegrenze von 1.000 EUR.
- Bei Urteilen oder mündlichen Verhandlungen aus 2025 kann Übergangsrecht relevant sein. In solchen Fällen alte 600-EUR-Berufungsgrenze nicht vorschnell verwerfen.

## Prüfablauf

### 1. Was ist der Streitgegenstand?

| Fall | Was zählt? |
|---|---|
| Geldforderung | Forderung ohne Zinsen und Nebenforderungen |
| Mehrere Forderungen | Zusammenrechnung nach § 5 ZPO prüfen |
| Herausgabe | Wert der Sache |
| Räumung | besondere mietrechtliche Streitwertregeln prüfen |
| Feststellung | wirtschaftliches Interesse, oft Abschlag |

### 2. Gibt es Sonderzuständigkeit?

Amtsgericht unabhängig vom Wert kann insbesondere relevant sein bei:

- Wohnraummietsachen;
- bestimmten Nachbarrechtssachen;
- Wildschaden;
- Familiensachen, Betreuung, Nachlass;
- weiteren gesetzlichen Zuweisungen.

Bei Familiensachen gesondert prüfen: Amtsgericht bedeutet nicht automatisch "ohne Anwalt".

### 3. Anwaltszwang prüfen

- Normale Zivilsache vor dem Amtsgericht: kein Anwaltszwang.
- Landgericht und höher: grundsätzlich Anwaltszwang nach § 78 ZPO.
- Familiengericht: § 114 FamFG prüfen.
- Berufung zum Landgericht: spätestens für die Berufungsbegründung Anwalt erforderlich.

### 4. Rechtsmittelgrenze prüfen

Nach Urteil:

| Beschwer | Folge |
|---:|---|
| über 1.000 EUR | Berufung grundsätzlich statthaft |
| bis 1.000 EUR und Berufung zugelassen | Berufung statthaft |
| bis 1.000 EUR und nicht zugelassen | Berufung grundsätzlich nicht statthaft |

## Ausgabeformat

**Grenzen-Check**
| Frage | Ergebnis | Ampel |
|---|---|---|
| Streitwert | | |
| Amtsgericht zuständig? | | |
| Selbstvertretung möglich? | | |
| Vereinfachtes Verfahren möglich? | | |
| Berufung später realistisch? | | |

**Konsequenz**
[Klare Handlungsempfehlung: AG, LG/Anwalt, Rechtsantragsstelle, PKH, Streitwert nacharbeiten.]

**Nächste Skills**
- `sachliche-zuständigkeit-amtsgericht-23-gvg`
- `anwaltszwang-pruefen-78-zpo`
- `klage-streitwert-angabe-3-zpo`
- `berufung-amtsgericht-511-zpo`

## Qualitätsregeln

- Werte immer mit "mehr als", "bis einschließlich" und konkretem Betrag formulieren.
- Bei knappem Streitwert nicht kreativ kleinrechnen. Teilklage nur mit deutlichem Hinweis auf Risiken.
- Bei Berufung nie verschweigen, dass vor dem Landgericht Anwaltszwang besteht.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
