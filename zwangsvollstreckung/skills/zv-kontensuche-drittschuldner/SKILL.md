---
name: zv-kontensuche-drittschuldner
description: "Glaeubiger hat Urteil aber kein bekanntes Konto oder Arbeitgeber des Schuldners. § 802l ZPO Drittauskunfte. Pruefraster: Rentenversicherung Bund Bundeszentralamt fuer Steuern Kontenabruf Kraftfahrt-Bundesamt Schuldnerverzeichnis § 882b ZPO. Output: Drittsauskunfts-Antrag und Auswertungs-Protokoll. Abgrenzung zu zv-vermoegensauskunft-gv (Glaeubigerantrag auf EV durch GV) und zv-pfueb-bank (nach Kontoermittlung)."
---

# Kontensuche und Drittschuldnerermittlung


## Triage zu Beginn

1. Liegt ein vollstreckbarer Titel vor und ist die Forderung mindestens 500 EUR (§ 802l Abs. 1 ZPO)?
2. War eine Vermögensauskunft des Schuldners bereits unergiebig oder ist der Aufenthalt unbekannt?
3. Sollen alle drei Auskunftsstellen abgefragt werden (DRV, BZSt, KBA) oder nur eine?
4. Ist der Schuldner ein Unternehmen — dann Handelsregistereintrag als Informationsquelle?

## Aktuelle Rechtsprechung

- BGH, Beschl. v. 22.10.2015 - I ZB 70/14, NJW 2016, 466 — § 802l ZPO: Drittauskünfte sind subsidiär gegenüber der Vermögensauskunft; aber bei unbekanntem Aufenthalt sofort zulässig.
- BGH, Beschl. v. 26.01.2017 - I ZB 38/16, NJW 2017, 1540 — § 802l ZPO: Gläubiger kann alle drei Auskunftsquellen gleichzeitig beantragen; Reihenfolge steht in seinem Ermessen.
- BGH, Beschl. v. 20.04.2017 - I ZB 88/16, NJW 2017, 1897 — Kontenabruf über BZSt auch nach bereits erfolgter Vermögensauskunft zulässig, wenn neue Erkenntnisse erwartet werden.
- BGH, Beschl. v. 15.07.2021 - VII ZB 14/20, NJW 2021, 3046 — § 802c ZPO: Schuldner muss in der Vermögensauskunft alle Konten und Forderungen vollständig angeben; Verschweigen kann Strafverfolgung auslösen.

## Zentrale Normen

- § 802l ZPO — Drittauskünfte (DRV Bund, BZSt/§ 24c KWG, KBA)
- § 802c ZPO — Vermögensauskunft (primäre Quelle)
- § 802d ZPO — Sperrfrist 2 Jahre für erneute Vermögensauskunft
- § 882b ZPO — Schuldnerverzeichnis
- § 93 Abs. 7 AO — Kontenabrufverfahren BZSt
- § 24c KWG — Kontenevidenzzentrale BaFin/BZSt

## Kommentarliteratur

- Zöller/Herget, ZPO, 35. Aufl. 2024, § 802l Rn. 1-20 (Drittauskünfte Voraussetzungen)
- MüKo-ZPO/Gruber, 6. Aufl. 2022, § 802c Rn. 1-30 (Vermögensauskunft)
- Thomas/Putzo, ZPO, 45. Aufl. 2024, § 882b Rn. 1-10 (Schuldnerverzeichnis)

## Aufgabe

Bevor eine Forderungspfändung Sinn ergibt, muss der Drittschuldner bekannt sein. Dieser Skill beschafft die Daten, ohne unnötige PfÜB ins Leere zu werfen.

## Startet bei

- Titel vorhanden, aber kein Konto, kein Arbeitgeber, keine sonstige Forderung des Schuldners bekannt
- Frühere Versuche ergebnislos
- Vermögensauskunft des Schuldners liegt vor oder Sperrfrist hindert sie nicht

## Rechtsgrundlagen

- § 802l ZPO – Drittauskünfte des Gerichtsvollziehers
- § 93 Abs. 7 AO – Kontenabrufverfahren über das BZSt
- § 24c KWG – Kontenevidenzzentrale der BaFin
- § 802c ZPO – primäre Quelle: Vermögensauskunft
- § 882b ZPO – Schuldnerverzeichnis
- § 33 StVG – Halterauskunft KBA

## Workflow

1. **Schuldnerverzeichnis abfragen** über das zentrale Vollstreckungsportal der Länder (`vollstreckungsportal.de`). Kostenpflichtig.
2. **Vorhandene Vermögensauskunft einsehen**, falls noch nicht zwei Jahre alt.
3. **Drittauskunft § 802l ZPO** durch den Gerichtsvollzieher beantragen, sobald Forderung mindestens 500 EUR und Vermögensauskunft erfolglos oder Schuldner nicht erreichbar:
   - **Deutsche Rentenversicherung Bund**: aktueller Arbeitgeber oder Rentenzahlstelle
   - **Bundeszentralamt für Steuern (BZSt)**: Kontostammdaten nach § 24c KWG, alle deutschen Kreditinstitute mit Konten des Schuldners
   - **Kraftfahrt-Bundesamt**: KFZ-Halterauskunft
4. **Ausländische Konten**: nicht über § 802l erreichbar, aber EU-Kontenpfändungsbeschluss (EuKtPVO) ist Alternative über `zv-pfueb-bank`.
5. **Plausibilitätsprüfung**: Auskunft veraltet sich. Konten existieren ggf. nicht mehr, Arbeitgeber gewechselt.
6. **Anschluss**: bekannte Bank → `zv-pfueb-bank`, bekannter Arbeitgeber → `zv-pfueb-arbeitsentgelt`.

## Voraussetzungen § 802l ZPO im Einzelnen

- Forderung mindestens 500 EUR (§ 802l Abs. 1 ZPO).
- Schuldner hat seinen gewöhnlichen Aufenthalt unbekannt **oder** Vermögensauskunft hat keine Befriedigung erwarten lassen **oder** Vermögensauskunft wurde nicht abgegeben.
- Antrag stets über den Gerichtsvollzieher; der Gerichtsvollzieher leitet die Anfragen weiter und übermittelt das Ergebnis.

## Leitentscheidungen

- BGH 22.10.2015 – I ZB 70/14 (Voraussetzungen § 802l)
- BGH 26.1.2017 – I ZB 38/16 (Reihenfolge der Drittauskünfte)
- BGH 20.4.2017 – I ZB 88/16 (Kontenabruf trotz neuer Vermögensauskunft)

## Ausgabeformat

```
DRITTSCHULDNERSUCHE [Mandant] gegen [Schuldner]

Titel:                 [Art, Datum]
Forderungshöhe:        EUR x (≥ 500 EUR? ja/nein)
VA-Stand:              [vorhanden, Datum / fehlt / unergiebig]
Beantragte Auskünfte:  [DRV / BZSt / KBA]
Geschätzte Dauer:      4-8 Wochen ab GV-Antrag
Folgeskill:            [zv-pfueb-bank / -arbeitsentgelt / ...]

WIEDERVORLAGE:         DD.MM.JJJJ
```

## Qualitätsgates

- Niemals § 802l ZPO unterhalb der Bagatellgrenze 500 EUR beantragen.
- Niemals BZSt-Kontenabruf ohne erfolglose Vermögensauskunft oder unbekannten Aufenthalt.
- Daten sind sensibel – Datenschutz beachten, Auskunft nur für konkrete Vollstreckung.
- Doppelte Abfragen vermeiden (Kostenfalle).

## Querverweise

- `zv-vermoegensauskunft-gv` – Hauptquelle vor § 802l
- `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`
- `zv-kommandocenter`
- `zv-elektronische-zustellung-2027`
