---
name: kennzahlenset-und-ampelsystem-starug-konform
description: "StaRUG-konformes KPI-Set und Ampelsystem fuer Krisenfrueherkennung definieren: Berater oder GF braucht messbare Schwellenwerte fuer Krisen-Monitoring. Normen: § 1 StaRUG (Frueherkennungspflicht), IDW PS 340 n.F. Pruefraster: Liquiditaetsreichweite, EBITDA-Coverage, Net-Debt-EBITDA, Covenant-Headroom, DSCR — numerische Schwellen gruen/gelb/rot, Berechnungsformeln, Eskalationslogik. Output KPI-Dashboard-Template, Ampelsystem-Beschreibung, Schwellenwert-Dokumentation. Abgrenzung: Fruehwarnsystem-Architektur siehe fruehwarnsystem-architektur-zwei-jahres-horizont; Liquiditaetsplanung siehe rollierende-liquiditaetsplanung-24-monate-template."
---

# Kennzahlenset und Ampelsystem — StaRUG-konform

Ein Ampelsystem ohne kalibrierte Schwellenwerte ist eine Farbenspielerei ohne Steuerungsnutzen. Das StaRUG-konforme KPI-Set verbindet betriebswirtschaftliche Standardkennzahlen mit klaren, numerisch definierten Auslösern — so dass jeder Geschäftsführer und jeder Berater sofort erkennt: Grün ist alles in Ordnung, Gelb ist Handlungsbedarf, Rot ist Krisenalarm. Die Schwellen sind nicht willkürlich, sondern aus der Rechtsprechung, IDW-Standards und Bankpraxis abgeleitet.

---

## Rechtsgrundlagen

- § 1 StaRUG (Früherkennungspflicht mit KPI-basierter Überwachung)
- § 18 InsO (drohende Zahlungsunfähigkeit — Liquiditätsreichweite als Schlüsselindikator)
- IDW PS 340 n.F. (Risikobewertung, Schwellenwerte, Eskalationsstufen)
- IDW S 6 Tz. 40 ff. (Leistungsfähigkeitsanalyse, Kennzahlen)
- IDW S 11 (Beurteilung Insolvenzeröffnungsgründe — Liquiditätstest)
- BGH IX ZR 285/14 (Sanierungsberater-Pflicht: frühzeitige KPI-Auswertung)

---

## Pflichten

### 1. Warum quantitative Schwellen unverzichtbar sind

Qualitative Urteile wie „die Liquidität ist angespannt" genügen nicht. § 1 StaRUG verlangt rechtzeitiges Erkennen und Handeln — das setzt messbare Auslöser voraus. Ohne definierte Schwellen:

- Keine objektive Eskalationspflicht auslösbar
- Keine Beweissicherung für „rechtzeitig erkannt"
- Kein Nachweis gegenüber Insolvenzverwalter oder Gericht

### 2. Das KPI-Set — Sieben Kern-Indikatoren

Die folgenden sieben KPIs bilden das Rückgrat des Ampelsystems:

**KPI 1: Liquiditätsreichweite**
```
Definition:  Verfügbare Liquidität (Kasse + freie Kreditlinien) ÷ durchschnittl. monatl. Auszahlungen
Einheit:     Monate
Grün:        ≥ 6 Monate
Gelb:        3 bis < 6 Monate
Rot:         < 3 Monate
Bedeutung:   Überleben-Indikator Nr. 1 — wie lange kann das Unternehmen ohne neue Einnahmen zahlen?
```

**KPI 2: EBITDA-Coverage (Zinsdeckungsgrad)**
```
Definition:  EBITDA ÷ Zinsaufwand (rolling 12 Monate)
Einheit:     Faktor (x)
Grün:        ≥ 3,0x
Gelb:        1,5x bis < 3,0x
Rot:         < 1,5x
Bedeutung:   Kann das Unternehmen aus dem operativen Ergebnis seine Zinsen bedienen?
```

**KPI 3: Net-Debt/EBITDA**
```
Definition:  Nettofinanzverbindlichkeiten ÷ EBITDA (rolling 12 Monate)
             Nettoverschuldung = Bankschulden + Anleihen - flüssige Mittel
Einheit:     Faktor (x)
Grün:        ≤ 3,0x
Gelb:        3,0x bis 4,5x
Rot:         > 4,5x
Bedeutung:   Wie viele Jahre EBITDA braucht das Unternehmen, um schuldenfrei zu werden?
```

**KPI 4: Covenant-Headroom**
```
Definition:  Prozentualer Abstand der tatsächlichen Finanzkennzahl zur vertraglich vereinbarten
             Covenant-Grenze
             Headroom (%) = (Ist-Wert - Covenant-Grenze) ÷ |Covenant-Grenze| × 100
Einheit:     Prozent (%)
Grün:        ≥ 25 %
Gelb:        10 % bis < 25 %
Rot:         < 10 % (oder Covenant bereits verletzt)
Bedeutung:   Verletzung eines Financial Covenants löst typischerweise Kündigungsrecht der Bank aus
```

**KPI 5: DSCR (Debt Service Coverage Ratio)**
```
Definition:  (EBITDA - CAPEX Erhaltung) ÷ (Zinsen + Tilgung, fällig im Planungszeitraum)
Einheit:     Faktor (x)
Grün:        ≥ 1,20x
Gelb:        1,00x bis < 1,20x
Rot:         < 1,00x (Schuldendienstunfähigkeit)
Bedeutung:   Kann das Unternehmen Zinsen UND Tilgung aus dem operativen Cashflow bedienen?
```

**KPI 6: Eigenkapitalquote**
```
Definition:  Eigenkapital ÷ Bilanzsumme × 100
Einheit:     Prozent (%)
Grün:        ≥ 20 %
Gelb:        10 % bis < 20 %
Rot:         < 10 % (oder negatives Eigenkapital → Überschuldungsrisiko)
Bedeutung:   Struktureller Schutzpuffer, insbes. relevant für § 19 InsO Überschuldung
```

**KPI 7: Cash-Conversion-Rate (CCR)**
```
Definition:  Operativer Cashflow ÷ EBITDA × 100
Einheit:     Prozent (%)
Grün:        ≥ 70 %
Gelb:        40 % bis < 70 %
Rot:         < 40 %
Bedeutung:   Wie viel des Ergebnisses wird tatsächlich als Cash realisiert?
             Niedrige CCR signalisiert Working-Capital-Probleme oder Bilanzrisiken
```

---

## Vorgehen

### Schritt 1: Ampeltabelle monatlich aktualisieren

```
AMPELTABELLE — [Firma GmbH] — Stand: [MM/JJJJ]

KPI                     | Ist-Wert | Grün       | Gelb           | Rot        | Ampel | Trend
------------------------|----------|------------|----------------|------------|-------|------
Liquiditätsreichweite   | [x] Mon. | ≥ 6 Mon.   | 3 bis < 6 Mon. | < 3 Mon.   | [🔴/🟡/🟢] | [↑↓→]
EBITDA-Coverage         | [x,xx]x  | ≥ 3,0x     | 1,5x bis < 3x  | < 1,5x     | [Amp] | [↑↓→]
Net-Debt/EBITDA         | [x,xx]x  | ≤ 3,0x     | 3,0x bis 4,5x  | > 4,5x     | [Amp] | [↑↓→]
Covenant-Headroom       | [x] %    | ≥ 25 %     | 10 % bis < 25% | < 10 %     | [Amp] | [↑↓→]
DSCR                    | [x,xx]x  | ≥ 1,20x    | 1,0x bis 1,2x  | < 1,0x     | [Amp] | [↑↓→]
Eigenkapitalquote       | [x] %    | ≥ 20 %     | 10 % bis < 20% | < 10 %     | [Amp] | [↑↓→]
Cash-Conversion-Rate    | [x] %    | ≥ 70 %     | 40 % bis < 70% | < 40 %     | [Amp] | [↑↓→]

Gesamtampel: [ROT / GELB / GRÜN]
Eskalationsstufe: [1 / 2 / 3]
Kommentar: [___]
```

### Schritt 2: Eskalationslogik anwenden

```
GESAMTAMPEL-LOGIK:
  GRÜN:   Alle KPIs im grünen Bereich
  GELB:   Mind. 1 KPI im gelben Bereich, kein KPI im roten Bereich
  ROT:    Mind. 1 KPI im roten Bereich

ESKALATION:
  GRÜN:  Routinereporting, monatlich
  GELB:  Sofortanalyse (5 Werktage), Maßnahmenplan (10 Werktage), Info Gesellschafter (15 Werktage)
  ROT:   Sofortmaßnahmen (72 Stunden), Berater einschalten, StaRUG prüfen
```

### Schritt 3: Trendanalyse und Prognostik

Nicht nur der Ist-Wert, auch der Trend ist entscheidend:

- **Verschlechterung über drei Monate** bei einem grünen KPI → präventiver Gelb-Status setzen
- **Gleichbleibend Gelb über zwei Monate ohne Maßnahmen** → automatisch Rot
- **Verbesserung** dokumentieren und in Protokoll aufnehmen (Enthaftung)

---

## Templates

### Muster: KPI-Datenblatt für Monatsreporting

```
KPI-DATENBLATT — MONATLICHES REPORTING
Gesellschaft: [Firma GmbH]
Berichtsmonat: [MM/JJJJ]
Erstellt: [Name, Funktion]
Freigegeben GF: [Name, Datum]

1. LIQUIDITÄTSREICHWEITE
   Kassenbestand per Monatsende: EUR [___]
   Freie Kreditlinien: EUR [___]
   Verfügbare Liquidität gesamt: EUR [___]
   Monatl. Ø Auszahlungen (letzte 3 Monate): EUR [___]
   Reichweite: [x,x] Monate → AMPEL: [GRÜN/GELB/ROT]

2. EBITDA-COVERAGE
   EBITDA rolling 12 Monate: EUR [___]
   Zinsaufwand rolling 12 Monate: EUR [___]
   EBITDA-Coverage: [x,xx]x → AMPEL: [GRÜN/GELB/ROT]

3. NET-DEBT/EBITDA
   Bankschulden + Anleihen: EUR [___]
   ./. Liquide Mittel: EUR [___]
   Nettoverschuldung: EUR [___]
   EBITDA rolling 12 Monate: EUR [___]
   Net-Debt/EBITDA: [x,xx]x → AMPEL: [GRÜN/GELB/ROT]

4. COVENANT-HEADROOM
   Vereinbarter Covenant: [KPI] ≤ [Wert]
   Ist-Wert: [Wert]
   Headroom: [x] % → AMPEL: [GRÜN/GELB/ROT]

5. DSCR
   EBITDA: EUR [___]
   ./. Erhaltungs-CAPEX: EUR [___]
   Zinsen fällig: EUR [___]
   Tilgung fällig: EUR [___]
   DSCR: [x,xx]x → AMPEL: [GRÜN/GELB/ROT]

KOMMENTAR ZU ABWEICHUNGEN:
[___]

MAßNAHMEN BEI GELB/ROT:
[___]
```

---

## Fallstricke

1. **KPI-Definitionen nicht abgestimmt** — EBITDA (vor/nach Sondereffekten?), Nettoverschuldung (mit/ohne Pensionen?) — unklare Definitionen machen den Vergleich mit Vorperioden oder mit Covenants wertlos.

2. **Schwellenwerte nicht branchenspezifisch kalibriert** — die oben genannten Schwellen sind Orientierungswerte. Kapitalintensive Branchen (z.B. Industrie) tolerieren höheres Net-Debt/EBITDA als servicebasierte Modelle.

3. **Covenant-Berechnung nicht mit Bankdefinition abgestimmt** — Banken haben oft modifizierte EBITDA-Definitionen (z.B. bereinigt um Sondereffekte). Abweichende interne Berechnung führt zu falscher Headroom-Einschätzung.

4. **DSCR ohne Erhaltungs-CAPEX** — wer Tilgung aus dem EBITDA bedienen will, aber keine laufenden Investitionen einrechnet, überzeichnet die Tragfähigkeit.

5. **Ampelsystem ohne Eskalationsprotokoll** — Gelb-Status, der nicht protokolliert und eskaliert wird, ist eine versäumte Haftungsentlastung.

---

## Querverweise

- → `fruehwarnsystem-architektur-zwei-jahres-horizont` — Systemarchitektur und Reporting-Zyklus
- → `rollierende-liquiditaetsplanung-24-monate-template` — Datenbasis für KPIs
- → `integrierte-planung-guv-bilanz-cashflow` — Planungsbasis für Forecast-KPIs
- → `drohende-zahlungsunfaehigkeit-paragraph-18-inso` — Liquiditätsreichweite als Tatbestandsmerkmal
- → `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` — Protokollierung der Ampelwerte


## Weitere Leitentscheidungen

- BGH, Urt. v. 19.12.2017 — IX ZR 285/14, BGHZ 217, 1 — Fortbestehensprognose § 19 Abs. 2 InsO und Handlungspflichten: positive Prognose heilt Ueberschuldung; negative Prognose loest Antragspflicht aus; Dokumentation ist Haftungsschutz.
- BGH, Urt. v. 15.03.2016 — II ZR 119/14, NJW 2016, 2493 — § 43 GmbHG / § 15b InsO: Geschaeftsfuehrer haftet persoenlich; ordnungsgemaesse Krisenfrueherkennung und Dokumentation als Entlastungsbeweis.
- BGH, Urt. v. 26.01.2017 — IX ZR 285/14 — Antragspflicht § 15a InsO: Fristbeginn mit Kenntnis; spaeteres Handeln erhoht Haftungsrisiko erheblich.
- BGH, Urt. v. 06.05.2021 — IX ZR 72/20, NZI 2021, 631 — Sanierungs-Konzept-Pflicht: echter Sanierungsversuch mit dokumentiertem Konzept schutzt vor Strafbarkeit und Anfechtung.


## Triage — Erste Einordnung

Bevor losgelegt wird, klaere:
1. **Krisenstadium?** Ertragskrise (EBIT negativ), Liquiditaetskrise (Cashflow negativ) oder akute Insolvenznaehe (ZU/Ueberschuldung)?
2. **Insolvenzgrund?** § 17 InsO (ZU), § 18 InsO (drohende ZU), § 19 InsO (Ueberschuldung)?
3. **Fristen?** Antragspflicht § 15a InsO: 3 Wochen (ZU), 6 Wochen (Ueberschuldung).
4. **Sanierungs-Pfad?** StaRUG (drohende ZU), Schutzschirm, Eigenverwaltung oder Regelverfahren?
