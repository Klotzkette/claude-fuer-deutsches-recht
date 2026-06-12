---
name: bwa-zeitlicher-vergleich-jahresvergleich
description: "Zeitvergleich Vorjahr und Vormonat in der BWA. Anwendungsfall Monats- oder Quartals-BWA mit Gegenüberstellung Vorjahres-Periode kumulierter Jahresvergleich Abweichungs-Analyse Trendaussage. Methodik gleicher Zeitraum gleiches Geschäftsmodell Bereinigung Sondereffekte. Output Tabelle mit Soll Ist..."
---

# Zeitlicher Vergleich in der BWA — Vorjahr und Vormonat

## Fachlicher Anker

- **Normen:** § 6a, § 252 Abs. 1 Nr. 6 HGB, § 265 Abs. 2 HGB.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Eine BWA ohne zeitlichen Vergleich ist eine reine Momentaufnahme ohne Steuerungswert. Erst durch die Gegenueberstellung mit der Vorjahres-Periode (Monat oder Quartal) und dem kumulierten Jahresvergleich entsteht Trendaussage. Der Steuerberater muss dabei methodisch sauber vorgehen: Sondereffekte herausrechnen, Periodenabgrenzungen vergleichbar machen und qualifizierte Aussagen über Abweichungen treffen.

## Kaltstart-Rueckfragen

1. Welche Auswertungsform — Monats-BWA mit Vorjahresvergleich oder kumulierter Vergleich seit Jahresbeginn?
2. Hat das Unternehmen Sondereffekte im Vorjahr (Einmal-Erloese, Sonderabschreibungen, Sonder-Tantieme)?
3. Änderungen im Geschäftsmodell, Sortiment, Vertriebsgebiet seit Vorjahr?
4. Hat sich die Buchhaltungs-Routine geaendert (Periodenabgrenzung, Bestand-Schaetzung)?
5. Liegen Vorjahres-BWA-Daten konsistent vor, oder wurde der Vorberater gewechselt?
6. Aussagekraft des Vergleichs: Ist gleicher Saisonzyklus vorhanden (z.B. Tourismus)?
7. Mandantenwunsch — Tabelle oder zusaetzlich Grafik?
8. Reportingzweck — interne Steuerung, Bankberichterstattung, Investoren-Update?

## Rechtlicher Rahmen

### Primaernormen

**§ 252 Abs. 1 Nr. 6 HGB** — Bewertungsstetigkeit; zeitlicher Vergleich setzt konsistente Methoden voraus.

**§ 265 Abs. 2 HGB** — Vergleichbarkeit der Vorjahreszahlen im Jahresabschluss; analog für unterjaehrige BWA.

**§ 238 HGB** — Buchfuehrungspflicht; Grundlage für den Datenbestand.

**§ 5 EStG / § 4 EStG** — Massgeblichkeit für Vergleichszeitraeume.

### Verwaltungsanweisungen

- BMF v. 28.11.2019 zu GoBD — laufende Buchfuehrung.
- IDW PS 250 — Berichterstattung über Prüfergebnisse (sinngemäß auf BWA-Berichterstattung anwendbar).

## Workflow

### Phase 1 — Datenbasis sichern

- Vorjahres-BWA-Daten aus Vorperiode bestaendig in DATEV/Addison verfuegbar machen.
- Bei Mandantenuebernahme: Vorjahres-BWA des Vorberaters anfordern (Mandantenakte).
- Kontenrahmen-Änderungen prüfen (SKR 03 → SKR 04 erfordert Brueckenposten).

### Phase 2 — Sondereffekte identifizieren

| Typische Sondereffekte | Behandlung |
|---|---|
| Einmal-Erloese (Anlagenverkauf, Versicherungsleistung) | Sondereffekt-Spalte in BWA; Bereinigtes Ergebnis separat ausweisen |
| Sonderabschreibungen § 7g EStG / § 7b EStG | Ausweis separat; Vorjahresvergleich darum bereinigen |
| Sonder-Tantieme oder Sonderzahlungen Personal | Personalkostenquote bereinigen |
| Aufholeffekt nach Krise / Aufholmonat | Trendanalyse glaetten (3-Monats-Schnitt) |
| Investitionsabzugsbetrag § 7g EStG | Ausweis im Jahresblock, nicht Monats-BWA |

### Phase 3 — Vergleichstabelle erstellen

```
| Position | Monat aktuell | Monat Vorjahr | Abweichung EUR | Abweichung in Prozent |
|--------------------|---------------|---------------|----------------|------------------------|
| Umsatzerloese | 125.000 | 110.000 | +15.000 | +13,6 |
| Materialeinsatz | 45.000 | 42.000 | +3.000 | +7,1 |
| Personalkosten | 38.000 | 35.500 | +2.500 | +7,0 |
| Sonstige Aufw. | 18.000 | 17.500 | +500 | +2,9 |
| Abschreibungen | 4.500 | 4.300 | +200 | +4,7 |
| Betriebsergebnis | 19.500 | 10.700 | +8.800 | +82,2 |
```

Vorsicht: Im obigen Beispiel ist `13,6` nur in der Tabelle akzeptabel; in der Frontmatter-Description waere das verboten (Cowork-Validator-Bug). In Erläuterungstexten ausserhalb der Tabelle "13 Prozent" oder "rund 14 Prozent" formulieren.

### Phase 4 — Abweichungsanalyse

- Absolute Abweichung in EUR: ab welchem Schwellenwert ist Klärung noetig? Mandantenabhaengig (kleine Mandanten ab 500 EUR, große ab 5.000 EUR).
- Prozentuale Abweichung: ab 10-20 Prozent ist Erläuterung im BWA-Text Pflicht.
- Kreuzpruefung: Umsatzplus von 13 Prozent rechtfertigt Materialeinsatzplus von 7 Prozent nicht — Materialquote sinkt, Marge waechst. Ursache klären (Preiserhoehung, Mix-Effekt, Einkaufsvorteile)?

### Phase 5 — Kumuliert seit Jahresbeginn

- Jahresblock (Year-to-Date) parallel zum Monatsblock.
- Vergleichszeitraum identisch wie Mandantenkalender (Wirtschaftsjahr vom 1. Januar bis 31. Dezember; bei abweichendem Wirtschaftsjahr entsprechend anpassen).
- Trend: Erwartung Jahresende hochrechnen (Annualisierung), aber mit Vorsicht (Saisonzyklus beachten).

### Phase 6 — Erläuterungstext und Mandantenkommunikation

- 3-5 Saetze unter der BWA: wichtigste Abweichungen benennen, Ursachen vermuten oder klärend fragen.
- Bei Krisensignalen (Umsatz minus 20 Prozent, Eigenkapitalerosion): Eskalation an Berufstraeger und ggf. Querverweis stb-bwa-sus-bilanz-pruefung.

## Strategie und Praxis-Tipps

- Bei Mandantenuebernahme klare Erwartung kommunizieren: Vorjahresvergleich ist erst sinnvoll, wenn ein volles Wirtschaftsjahr Daten vorliegt.
- Saisonale Branchen (Tourismus, Bau, Einzelhandel) immer mit Vorjahres-Monatsvergleich, nicht Vormonatsvergleich.
- Bei abweichendem Wirtschaftsjahr Mandant darauf hinweisen, dass Standard-BWA-Form ggf. anzupassen ist.
- DATEV BWA 11 (Bewegungs-BWA) gibt Vormonatsvergleich detailliert aus; DATEV BWA 01 mit Vorjahresvergleich konfigurieren.
- Honorar für aufwendige Sondereffekt-Bereinigung als Zusatzauftrag StBVV § 35 / Zeithonorar.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 252, 265.
- EStG §§ 4, 5, 7g.
- BMF v. 28.11.2019, BStBl I 2019, 1269 (GoBD).
- DATEV BWA-Form 01 mit Vorjahresvergleich (Standard).
- IDW PS 250 (sinngemäß).
