---
name: strafbefehl-tagessaetze-geldstrafe
description: "Berechnung Tagessaetze und Geldstrafe nach §§ 40 41 StGB. Tagessatzanzahl nach Schuld. Tagessatzhoehe nach Nettoeinkommen Dreissigstel. Mindest-Tagessatz 1 EUR. Schaetzungsrecht des Gerichts § 40 Abs. 3 StGB. Einkommensnachweise. Ratenzahlungsantrag § 42 StGB. Ersatzfreiheitsstrafe § 43 StGB."
---

# Tagessaetze und Geldstrafe — §§ 40 bis 43 StGB

## Triage zu Beginn

1. **Wie viele Tagessaetze sind im Strafbefehl festgesetzt?** — Anzahl bestimmt Schuldgewicht, Hoehe das Nettoeinkommen.
2. **Tagessatzhoehe korrekt?** — Nettoeinkommen / 30 = Tagessatz (§ 40 Abs. 2 StGB); zu hoch wenn Einkommen ueberschaetzt.
3. **Liegt Einkommensnachweis vor?** — Lohnabrechnung, Steuerbescheid, BWA bei Selbststaendigen.
4. **Ratenzahlung noetig?** — § 42 StGB: Gericht kann Ratenzahlung gestatten; Antrag bei Zahlungsunfaehigkeit.
5. **Kann Geldstrafe nicht bezahlt werden?** — Ersatzfreiheitsstrafe droht (§ 43 StGB: 1 Tag Freiheitsstrafe pro uneinbringlichem Tagessatz).

## Zentrale Normen

- **§ 40 Abs. 1 StGB** — Geldstrafe: 5 bis 360 Tagessaetze (bei Mehrfachverstoss bis 720)
- **§ 40 Abs. 2 StGB** — Tagessatz: Dreissigstel des monatlichen Nettoeinkommens; Mindest 1 EUR
- **§ 40 Abs. 2 Satz 3 StGB** — Schaetzungsrecht des Gerichts wenn genaues Einkommen nicht feststellbar
- **§ 41 StGB** — Geldstrafe neben Freiheitsstrafe moeglich
- **§ 42 StGB** — Zahlungserleichterungen, Ratenzahlung
- **§ 43 StGB** — Ersatzfreiheitsstrafe: 1 Tag pro Tagessatz, mind. 1 Tag
- **§ 459d StPO** — Uneinbringlichkeit der Geldstrafe: Vollstreckungsgericht entscheidet

## Aktuelle Rechtsprechung

- BGH, Beschl. v. 17.09.2020 - 4 StR 134/20, NStZ 2021, 108 — Tagessatzhoehe richtet sich nach dem Nettoeinkommen zur Tatzeit; bei Einkommensveraenderungen zwischen Tat und Urteil ist regelmaessig das Urteilszeitpunkt-Einkommen massgeblich.
- BGH, Urt. v. 12.01.2021 - 6 StR 372/20, NStZ 2021, 354 — Schaetzung nach § 40 Abs. 2 Satz 3 StGB ist nur zulaessig wenn Gericht die Einkommensermittlung ausgeschoepft hat; reine Nichtangabe des Einkommens genuegt allein nicht.
- OLG Hamm, Beschl. v. 20.04.2021 - 4 RVs 40/21, NStZ-RR 2021, 305 — Ratenzahlungsantrag nach § 42 StGB hat keinen Suspensiveffekt; Vollstreckung kann trotz Antrag eingeleitet werden.
- BGH, Beschl. v. 03.09.2019 - 4 StR 247/19, NStZ 2020, 45 — § 41 StGB (Geldstrafe neben Freiheitsstrafe) setzt voraus, dass Verurteiler aus der Tat wirtschaftliche Vorteile gezogen hat oder besondere Begleitumstaende vorliegen.

## Kommentarliteratur

- Fischer StGB § 40 Rn. 1-35 (Tagessatzsystem, Nettoeinkommen, Schaetzung)
- Fischer StGB § 42 Rn. 1-15 (Ratenzahlung, Zahlungserleichterung)
- Fischer StGB § 43 Rn. 1-10 (Ersatzfreiheitsstrafe)
- MueKo StGB / Radtke § 40 Rn. 1-50 (vollstaendige Kommentierung)
- Schoenke/Schroeder/Kinzig StGB § 40 Rn. 1-25

## Berechnungsschema Tagessatz

```
1. Bruttoeinkommen monatlich:          [BETRAG] EUR
2. Abzuege (Lohnsteuer, SV-Beitraege): [BETRAG] EUR
3. Nettoeinkommen:                     [BETRAG] EUR
4. Tagessatz (Netto / 30):             [BETRAG] EUR

Besonderheiten:
- Fahrtkosten / Werbungskosten: koennen abgezogen werden
- Unterhaltspflichten: mindern verfuegbares Einkommen (§ 40 Abs. 2 Satz 2)
- Schulden / Verbindlichkeiten: einzelfallabhaengig, kein automatischer Abzug
- Selbststaendige: Gewinn lt. Steuerbescheid / 12 als Monats-"Netto"
```

## Einkommensnachweise-Checkliste

```
□ Lohnabrechnung letzter 3 Monate
□ Steuerbescheid letztes Jahr
□ Rentennachweis (bei Rentnern)
□ Buchfuehrungs-Zusammenfassung / BWA (bei Selbststaendigen)
□ ALG-II-/Buergergeld-Bescheid (bei ALG-II-Empfaengern: ca. 1-2 EUR Tagessatz)
□ Unterhaltsnachweis (belegt Verbindlichkeiten)
□ Kreditvertraege (monatliche Belastungen)
```

## Antrag auf Ratenzahlung — Template

**Adressat:** Vollstreckungsgericht / Staatsanwaltschaft — Tonfall: sachlich, Daten belegt

```
In der Strafsache gegen [NAME]
Az.: [AKTENZEICHEN]

Antrag auf Zahlungserleichterung nach § 42 StGB

Mein Mandant ist verurteilt zu [X] Tagessaetzen a [Y] EUR,
gesamt [X*Y] EUR Geldstrafe.

Er ist aufgrund [Einkommensverhaeltnisse beschreiben] derzeit nicht in
der Lage, den Gesamtbetrag in einer Summe zu zahlen.

Wir beantragen Ratenzahlung von [RATE] EUR monatlich beginnend
ab [DATUM].

Anlage: Einkommensnachweis / Kontoauszug
```

## Harte Leitplanken

- Tagessatz nie ohne Einkommensnachweis bestimmen — Schaetzung zu Mandantenungunsten moglich.
- Ratenzahlungsantrag fruehzeitig stellen — vor Vollstreckungsbeginn.
- Ersatzfreiheitsstrafe (§ 43 StGB) dem Mandanten klar erklaeren.
- Anwaltliche Endkontrolle bei Berechnungen.
