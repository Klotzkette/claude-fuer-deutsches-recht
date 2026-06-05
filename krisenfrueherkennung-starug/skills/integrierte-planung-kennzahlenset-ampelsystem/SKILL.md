---
name: integrierte-planung-kennzahlenset-ampelsystem
description: "Integrierte Planung Kennzahlenset Ampelsystem: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Integrierte Planung Kennzahlenset Ampelsystem

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Integrierte Planung Kennzahlenset Ampelsystem** im Plugin Krisenfrüherkennung (StaRUG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `integrierte-planung-guv-bilanz-cashflow` | Integriertes Drei-Statement-Modell (GuV/Bilanz/Cashflow) für StaRUG-Planung erstellen: Sanierungsberater braucht konsistentes Planungsmodell. Normen: IDW S 6 (Sanierungsstandard), IDW S 11 (Fortbestehensprognose), HGB §§ 242 ff. (Jahresabschluss), § 1 StaRUG. Prüfraster: GuV-Plan, Bilanzplan, Cash-Flow-Statement, Working-Capital-Modell, Investitions-/Finanzierungsplan, Brucke Ergebnis-Liquiditaet. Output Excel-Modell-Template, Planungsannahmen-Memo. Abgrenzung: Liquiditaetsplanung rolling siehe rollierende-liquiditaetsplanung-24-monate-template; Kennzahlen-Ampel siehe kennzahlenset-und-ampelsystem-starug-konform. |
| `kennzahlenset-und-ampelsystem-starug-konform` | StaRUG-konformes KPI-Set und Ampelsystem für Krisenfrueherkennung definieren: Berater oder GF braucht messbare Schwellenwerte für Krisen-Monitoring. Normen: § 1 StaRUG (Frueherkennungspflicht), IDW PS 340 n.F. Prüfraster: Liquiditaetsreichweite, EBITDA-Coverage, Net-Debt-EBITDA, Covenant-Headroom, DSCR — numerische Schwellen gruen/gelb/rot, Berechnungsformeln, Eskalationslogik. Output KPI-Dashboard-Template, Ampelsystem-Beschreibung, Schwellenwert-Dokumentation. Abgrenzung: Fruehwarnsystem-Architektur siehe fruehwarnsystem-architektur-zwei-jahres-horizont; Liquiditaetsplanung siehe rollierende-liquiditaetsplanung-24-monate-template. |
| `kfe-fruherkennungssystem-bauleiter` | Bauleiter Frueherkennungssystem § 1 StaRUG: Risikolandkarte, Indikatoren, Eskalationsstufen, Berichtswege an Geschaeftsleitung und Aufsichtsorgan. Pruefraster fuer mittelstaendische GmbH. |

## Arbeitsweg

Im Plugin Krisenfrüherkennung (StaRUG) gilt für **Integrierte Planung Kennzahlenset Ampelsystem**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `integrierte-planung-guv-bilanz-cashflow`

**Fokus:** Integriertes Drei-Statement-Modell (GuV/Bilanz/Cashflow) für StaRUG-Planung erstellen: Sanierungsberater braucht konsistentes Planungsmodell. Normen: IDW S 6 (Sanierungsstandard), IDW S 11 (Fortbestehensprognose), HGB §§ 242 ff. (Jahresabschluss), § 1 StaRUG. Prüfraster: GuV-Plan, Bilanzplan, Cash-Flow-Statement, Working-Capital-Modell, Investitions-/Finanzierungsplan, Brucke Ergebnis-Liquiditaet. Output Excel-Modell-Template, Planungsannahmen-Memo. Abgrenzung: Liquiditaetsplanung rolling siehe rollierende-liquiditaetsplanung-24-monate-template; Kennzahlen-Ampel siehe kennzahlenset-und-ampelsystem-starug-konform.

# Integrierte Planung — GuV, Bilanz und Cashflow

Wer nur eine GuV-Planung vorlegt, hat keinen Finanzplan. Wer nur eine Liquiditätsplanung vorlegt, hat kein Steuerungsinstrument. Das Drei-Statement-Modell verknüpft Gewinn- und Verlustrechnung, Bilanz und Kapitalflussrechnung zu einer konsistenten Planung, die jedem Anspruch — ob IDW S 6, IDW S 11 oder § 1 StaRUG — standhält. Ohne diese Verknüpfung sind Restrukturierungskonzepte nicht belastbar und Fortführungsprognosen nicht fundiert.

---

## Rechtsgrundlagen

- § 1 StaRUG (Krisenfrüherkennungspflicht, integrierte Planung als Standard)
- IDW S 6 in aktueller Fassung als methodischer Rahmen für Sanierungskonzepte
- IDW S 11 als methodischer Rahmen für Insolvenzeröffnungsgründe und Fortbestehensprognose
- § 18 InsO (drohende Zahlungsunfähigkeit — integrierte Sicht nötig)
- § 252 Abs. 1 Nr. 2 HGB (Going-Concern-Prinzip in der Rechnungslegung)
- DRS 21 (Kapitalflussrechnung nach DRSC-Standard)

---

## Pflichten

### 1. Warum alle drei Statements zwingend sind

Jede der drei Planungsebenen beantwortet andere Fragen:

| Statement | Kernfrage | Relevanz im StaRUG-Kontext |
|---|---|---|
| GuV | Ist das Geschäftsmodell profitabel? | Ertragslage, EBITDA-Coverage |
| Bilanz | Ist das Unternehmen solvent? | Eigenkapital, Überschuldungsstatus |
| Cashflow | Kann das Unternehmen zahlen? | Zahlungsunfähigkeit, Liquidität |

Ein Unternehmen kann bilanziell positives Eigenkapital haben und trotzdem zahlungsunfähig sein (Ergebnis vs. Cash). Ein anderes kann Verluste schreiben, aber noch Liquidität haben (Abschreibungen). Nur die integrierte Sicht zeigt die volle Wahrheit.

### 2. Interlinkage — Die drei Aussagen müssen sich rechnerisch schließen

```
GuV → Jahresergebnis fließt ins Eigenkapital der Bilanz
Bilanz → Veränderung Working Capital ist Cashflow-Treiber
Cashflow → Endbestand ist Kassenposition in der Bilanz

KONTROLLFORMEL:
 Kassenbestand (Bilanz) = Kassenbestand Vorjahr + Cashflow aus lfd. Geschäft
 + Cashflow aus Investitionstätigkeit
 + Cashflow aus Finanzierungstätigkeit
```

---

## Vorgehen

### Schritt 1: GuV-Planung erstellen

**Mindeststruktur:**

```
Umsatzerlöse
- Material-/Wareneinsatz
= Rohertrag / Bruttoergebnis
- Personalkosten
- Sonstige betriebliche Aufwendungen (Miete, Marketing, IT, ...)
= EBITDA (Earnings before Interest, Taxes, Depreciation, Amortization)
- Abschreibungen (AfA)
= EBIT
- Zinsaufwand
+ Zinsertrag
= EBT (Ergebnis vor Steuern)
- Ertragsteuern (Körperschaftsteuer, Solidaritätszuschlag, Gewerbesteuer)
= Jahresergebnis
```

**Planprämissen je Zeile dokumentieren** (Wachstumsrate, Kostensteigerung, etc.)

### Schritt 2: Working-Capital-Modellierung

Das Working Capital ist die kritische Brücke zwischen GuV und Cashflow:

```
WORKING CAPITAL = Vorräte + Forderungen L&L - Verbindlichkeiten L&L

Modellierung über Umschlagstage:
 Vorräte (DIO) = (Vorräte / Umsatz) × 365 Tage
 Forderungen (DSO) = (Forderungen L&L / Umsatz) × 365 Tage
 Verbindlichkeiten (DPO) = (Verb. L&L / Wareneinsatz) × 365 Tage

 Net Working Capital Days = DIO + DSO - DPO

 Veränderung Working Capital = WC(t) - WC(t-1)
 → Zunahme WC: Cashflow negativ (Liquiditätsbindung)
 → Abnahme WC: Cashflow positiv (Liquiditätsfreisetzung)
```

### Schritt 3: Bilanzplanung

Bilanzpositionen aus GuV und Working-Capital-Modell ableiten:

**Aktiva:**
- Anlagevermögen: Vorjahr + Investitionen - Abschreibungen
- Vorräte: über DIO-Formel
- Forderungen L&L: über DSO-Formel
- Kassenbestand: aus Cashflow-Statement

**Passiva:**
- Eigenkapital: Vorjahr + Jahresergebnis - Ausschüttungen
- Verbindlichkeiten L&L: über DPO-Formel
- Bankverbindlichkeiten: Plan-Tilgungen und -Ziehungen
- Steuerrückstellungen: aus GuV

### Schritt 4: Cashflow-Statement ableiten (indirekte Methode)

```
CASHFLOW AUS LAUFENDER GESCHÄFTSTÄTIGKEIT
 Jahresergebnis
 + Abschreibungen
 +/- Veränderung Vorräte
 +/- Veränderung Forderungen L&L
 +/- Veränderung Verbindlichkeiten L&L
 +/- Veränderung sonstige Aktiva/Passiva
 = CFO (Cash Flow from Operations)

CASHFLOW AUS INVESTITIONSTÄTIGKEIT
 - Investitionen in Sachanlagen (CAPEX)
 + Erlöse aus Anlagenverkäufen
 = CFI (Cash Flow from Investing)

CASHFLOW AUS FINANZIERUNGSTÄTIGKEIT
 + Kreditaufnahmen
 - Kredittilgungen
 - Zinszahlungen (alternativ: unter CFO)
 - Dividenden/Ausschüttungen
 = CFF (Cash Flow from Financing)

FREE CASH FLOW = CFO + CFI
NETTO-CASH-CHANGE = CFO + CFI + CFF
ENDBESTAND KASSE = Anfangsbestand + Netto-Cash-Change
```

### Schritt 5: Investitions- und Finanzierungsplan

Separates Modul für größere Investitionsvorhaben:

- CAPEX-Planung (Erhaltungsinvestition vs. Wachstumsinvestition)
- Finanzierungsstruktur je Investition (Eigen-/Fremdfinanzierung, Förderung)
- Tilgungsplan bestehender Verbindlichkeiten
- Fälligkeiten und Verlängerungsoptionen bestehender Kredite

### Schritt 6: Sanierungskonzept-Brücke

Wenn die integrierte Planung ein Sanierungskonzept tragen soll, ergänze zwingend:

- **Krisenursachen:** Welche Planposition adressiert welche Ursache?
- **Leitbild:** Welche Zielstruktur erklärt die Planwerte nach Sanierung?
- **Maßnahmenlog:** Maßnahme, Verantwortlicher, Zeitpunkt, Kosten, GuV-/Bilanz-/Liquiditätseffekt, Nachweis.
- **Szenarien:** Base Case und plausible Downside; bei kritischen Annahmen zusätzlich Einzelsensitivität.
- **Dokumentation:** Datenstand, Planversion, Quellen, Annahmen, offene Punkte.
- **Monitoring:** Kennzahlen, Covenants, Mindestliquidität, Reporting-Takt.

Eine reine Drei-Statement-Mechanik reicht nicht, wenn die wirtschaftliche Sanierungslogik fehlt.

---

## Templates

### Muster: Planprämissen-Tabelle (Drei-Statement-Modell)

```
PLANPRÄMISSEN — DREI-STATEMENT-MODELL
Gesellschaft: [Firma]
Basisjahr: [JJJJ]
Planperiode: [JJJJ+1] bis [JJJJ+2]

GuV-TREIBER
 Umsatzwachstum p.a.: Base [x%] / Bear [-x%]
 Materialkostenquote: [x%] des Umsatzes
 Personalkostensteigerung: [x%] p.a. (Tariferhöhung + Headcount)
 Abschreibungsquote: [x% auf Anlagevermögen Ø]
 Effektivzinssatz: [x%] auf Ø Bankverbindlichkeiten

WORKING CAPITAL
 DIO (Vorräte): [x] Tage
 DSO (Forderungen): [x] Tage
 DPO (Verbindlichkeiten): [x] Tage

INVESTITIONEN
 Erhaltungs-CAPEX: EUR [x] p.a.
 Wachstums-CAPEX: EUR [x] (einmalig in [JJJJ])

FINANZIERUNG
 Tilgung Bankkredit: EUR [x] p.a.
 Neue Kreditaufnahme: EUR [x] in [JJJJ]
 Ausschüttung: EUR [x] (oder: keine Ausschüttung in der Planperiode)
```

---

## Fallstricke

1. **GuV-Planung ohne Cashflow** — in der Praxis verbreitet und gefährlich: profitables Unternehmen kann illiquid werden, wenn Working Capital wächst (z.B. Vorratsaufbau bei Umsatzwachstum).

2. **Planbilanzen werden vergessen** — viele Restrukturierungspläne haben GuV und Cash, aber keine Bilanz. IDW S 6 und IDW S 11 verlangen aber explizit die Planbilanz, um Überschuldungsstatus zu beurteilen.

3. **Stichtagsbezogene statt periodengerechte Abgrenzung** — Rückstellungen und Abgrenzungen in der Bilanzplanung vergessen → rechnerische Lücken zwischen GuV und Cashflow.

4. **Investitionsplanungen ohne Finanzierungsquelle** — CAPEX-Pläne, die nicht mit konkreter Finanzierungsstruktur unterlegt sind, sind Wunschlisten, keine valide Planung.

5. **Steuerlast unterschätzen** — Ertragsteuern, Umsatzsteuer, Lohnsteuer, Sozialversicherung und steuerliche Effekte von Sanierungsmaßnahmen müssen bei Wesentlichkeit in Cash und Ergebnis abgebildet werden.

6. **Krisenursachen nicht verknüpfen** — Planung verbessert sich, ohne dass eine Maßnahme die Ursache erklärt. Dann ist es keine Sanierungsplanung, sondern eine Wunschrechnung.

7. **Kleine Unternehmen unterprüfen** — bei geringerer Komplexität darf die Darstellung schlanker sein, aber GuV, Bilanz, Liquidität, Maßnahmen und Belege müssen trotzdem zusammenpassen.

---

## Querverweise

- → `rollierende-liquiditaetsplanung-24-monate-template` — detaillierter Cashflow-Plan
- → `fruehwarnsystem-architektur-zwei-jahres-horizont` — Einbettung in Frühwarnsystem
- → `kennzahlenset-und-ampelsystem-starug-konform` — KPI-Ableitung aus der Planung
- → `fortbestehensprognose-zweistufig` — Nutzung der integrierten Planung für IDW S 11
- → `krisenstadien-stakeholder-strategie-ergebnis-liquiditaet` — Diagnostik auf Basis der Planung


## Aktuelle Leitentscheidungen — Integrierte Planung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- IDW S 6 — Anforderungen an Sanierungskonzepte, aktuelle Fassung 2023; integrierte Unternehmensplanung als Kernbaustein jedes belastbaren Sanierungskonzepts.

## Paragrafenkette Integrierte Planung

§ 19 Abs. 2 InsO (Fortbestehensprognose auf Basis integrierter Planung) → IDW S 6 (Sanierungskonzept-Standard) → IDW S 11 (Beurteilung Insolvenzgruende) → § 1 StaRUG (24-Monats-Horizont) → § 43 GmbHG (Sorgfaltspflicht bei Planung)

## Triage — Integrierte Planung

1. **Drei-Sicht-Verknuepfung?** Guv-Planung → Cashflow (direkte Methode) → Bilanz-Planung konsistent?
2. **Annahmen dokumentiert?** Umsatz-Wachstumsraten, Kostenentwicklung, Working-Capital-Annahmen transparent?
3. **Szenarien?** Base-Case, Best-Case, Worst-Case durchgerechnet?
4. **Saldo-Check?** Integrierte Planung muss bilanziell schliessen (Bilanzsumme immer ausgeglichen).
5. **Sanierungsbezug?** Jede tragende Planverbesserung muss auf Ursache, Maßnahme, Timing und Beleg zurückgeführt werden.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `kennzahlenset-und-ampelsystem-starug-konform`

**Fokus:** StaRUG-konformes KPI-Set und Ampelsystem für Krisenfrueherkennung definieren: Berater oder GF braucht messbare Schwellenwerte für Krisen-Monitoring. Normen: § 1 StaRUG (Frueherkennungspflicht), IDW PS 340 n.F. Prüfraster: Liquiditaetsreichweite, EBITDA-Coverage, Net-Debt-EBITDA, Covenant-Headroom, DSCR — numerische Schwellen gruen/gelb/rot, Berechnungsformeln, Eskalationslogik. Output KPI-Dashboard-Template, Ampelsystem-Beschreibung, Schwellenwert-Dokumentation. Abgrenzung: Fruehwarnsystem-Architektur siehe fruehwarnsystem-architektur-zwei-jahres-horizont; Liquiditaetsplanung siehe rollierende-liquiditaetsplanung-24-monate-template.

# Kennzahlenset und Ampelsystem — StaRUG-konform

Ein Ampelsystem ohne kalibrierte Schwellenwerte ist eine Farbenspielerei ohne Steuerungsnutzen. Das StaRUG-konforme KPI-Set verbindet betriebswirtschaftliche Standardkennzahlen mit klaren, numerisch definierten Auslösern — so dass jeder Geschäftsführer und jeder Berater sofort erkennt: Grün ist alles in Ordnung, Gelb ist Handlungsbedarf, Rot ist Krisenalarm. Die Schwellen sind nicht willkürlich, sondern aus der Rechtsprechung, IDW-Standards und Bankpraxis abgeleitet.

---

## Rechtsgrundlagen

- § 1 StaRUG (Früherkennungspflicht mit KPI-basierter Überwachung)
- § 18 InsO (drohende Zahlungsunfähigkeit — Liquiditätsreichweite als Schlüsselindikator)
- IDW PS 340 n.F. (Risikobewertung, Schwellenwerte, Eskalationsstufen)
- IDW S 6 Tz. 40 ff. (Leistungsfähigkeitsanalyse, Kennzahlen)
- IDW S 11 (Beurteilung Insolvenzeröffnungsgründe — Liquiditätstest)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Pflichten

### 1. Warum quantitative Schwellen unverzichtbar sind

Qualitative Urteile wie "die Liquidität ist angespannt" genügen nicht. § 1 StaRUG verlangt rechtzeitiges Erkennen und Handeln — das setzt messbare Auslöser voraus. Ohne definierte Schwellen:

- Keine objektive Eskalationspflicht auslösbar
- Keine Beweissicherung für "rechtzeitig erkannt"
- Kein Nachweis gegenüber Insolvenzverwalter oder Gericht

### 2. Das KPI-Set — Sieben Kern-Indikatoren

Die folgenden sieben KPIs bilden das Rückgrat des Ampelsystems:

**KPI 1: Liquiditätsreichweite**
```
Definition: Verfügbare Liquidität (Kasse + freie Kreditlinien) ÷ durchschnittl. monatl. Auszahlungen
Einheit: Monate
Grün: ≥ 6 Monate
Gelb: 3 bis < 6 Monate
Rot: < 3 Monate
Bedeutung: Überleben-Indikator Nr. 1 — wie lange kann das Unternehmen ohne neue Einnahmen zahlen?
```

**KPI 2: EBITDA-Coverage (Zinsdeckungsgrad)**
```
Definition: EBITDA ÷ Zinsaufwand (rolling 12 Monate)
Einheit: Faktor (x)
Grün: ≥ 3,0x
Gelb: 1,5x bis < 3,0x
Rot: < 1,5x
Bedeutung: Kann das Unternehmen aus dem operativen Ergebnis seine Zinsen bedienen?
```

**KPI 3: Net-Debt/EBITDA**
```
Definition: Nettofinanzverbindlichkeiten ÷ EBITDA (rolling 12 Monate)
 Nettoverschuldung = Bankschulden + Anleihen - flüssige Mittel
Einheit: Faktor (x)
Grün: ≤ 3,0x
Gelb: 3,0x bis 4,5x
Rot: > 4,5x
Bedeutung: Wie viele Jahre EBITDA braucht das Unternehmen, um schuldenfrei zu werden?
```

**KPI 4: Covenant-Headroom**
```
Definition: Prozentualer Abstand der tatsächlichen Finanzkennzahl zur vertraglich vereinbarten
 Covenant-Grenze
 Headroom (%) = (Ist-Wert - Covenant-Grenze) ÷ |Covenant-Grenze| × 100
Einheit: Prozent (%)
Grün: ≥ 25 %
Gelb: 10 % bis < 25 %
Rot: < 10 % (oder Covenant bereits verletzt)
Bedeutung: Verletzung eines Financial Covenants löst typischerweise Kündigungsrecht der Bank aus
```

**KPI 5: DSCR (Debt Service Coverage Ratio)**
```
Definition: (EBITDA - CAPEX Erhaltung) ÷ (Zinsen + Tilgung, fällig im Planungszeitraum)
Einheit: Faktor (x)
Grün: ≥ 1,20x
Gelb: 1,00x bis < 1,20x
Rot: < 1,00x (Schuldendienstunfähigkeit)
Bedeutung: Kann das Unternehmen Zinsen UND Tilgung aus dem operativen Cashflow bedienen?
```

**KPI 6: Eigenkapitalquote**
```
Definition: Eigenkapital ÷ Bilanzsumme × 100
Einheit: Prozent (%)
Grün: ≥ 20 %
Gelb: 10 % bis < 20 %
Rot: < 10 % (oder negatives Eigenkapital → Überschuldungsrisiko)
Bedeutung: Struktureller Schutzpuffer, insbes. relevant für § 19 InsO Überschuldung
```

**KPI 7: Cash-Conversion-Rate (CCR)**
```
Definition: Operativer Cashflow ÷ EBITDA × 100
Einheit: Prozent (%)
Grün: ≥ 70 %
Gelb: 40 % bis < 70 %
Rot: < 40 %
Bedeutung: Wie viel des Ergebnisses wird tatsächlich als Cash realisiert?
 Niedrige CCR signalisiert Working-Capital-Probleme oder Bilanzrisiken
```

---

## Vorgehen

### Schritt 1: Ampeltabelle monatlich aktualisieren

```
AMPELTABELLE — [Firma GmbH] — Stand: [MM/JJJJ]

KPI | Ist-Wert | Grün | Gelb | Rot | Ampel | Trend
------------------------|----------|------------|----------------|------------|-------|------
Liquiditätsreichweite | [x] Mon. | ≥ 6 Mon. | 3 bis < 6 Mon. | < 3 Mon. | [🔴/🟡/🟢] | [↑↓→]
EBITDA-Coverage | [x,xx]x | ≥ 3,0x | 1,5x bis < 3x | < 1,5x | [Amp] | [↑↓→]
Net-Debt/EBITDA | [x,xx]x | ≤ 3,0x | 3,0x bis 4,5x | > 4,5x | [Amp] | [↑↓→]
Covenant-Headroom | [x] % | ≥ 25 % | 10 % bis < 25% | < 10 % | [Amp] | [↑↓→]
DSCR | [x,xx]x | ≥ 1,20x | 1,0x bis 1,2x | < 1,0x | [Amp] | [↑↓→]
Eigenkapitalquote | [x] % | ≥ 20 % | 10 % bis < 20% | < 10 % | [Amp] | [↑↓→]
Cash-Conversion-Rate | [x] % | ≥ 70 % | 40 % bis < 70% | < 40 % | [Amp] | [↑↓→]

Gesamtampel: [ROT / GELB / GRÜN]
Eskalationsstufe: [1 / 2 / 3]
Kommentar: [___]
```

### Schritt 2: Eskalationslogik anwenden

```
GESAMTAMPEL-LOGIK:
 GRÜN: Alle KPIs im grünen Bereich
 GELB: Mind. 1 KPI im gelben Bereich, kein KPI im roten Bereich
 ROT: Mind. 1 KPI im roten Bereich

ESKALATION:
 GRÜN: Routinereporting, monatlich
 GELB: Sofortanalyse (5 Werktage), Maßnahmenplan (10 Werktage), Info Gesellschafter (15 Werktage)
 ROT: Sofortmaßnahmen (72 Stunden), Berater einschalten, StaRUG prüfen
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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Triage — Erste Einordnung

Bevor losgelegt wird, klaere:
1. **Krisenstadium?** Ertragskrise (EBIT negativ), Liquiditaetskrise (Cashflow negativ) oder akute Insolvenznaehe (ZU/Ueberschuldung)?
2. **Insolvenzgrund?** § 17 InsO (ZU), § 18 InsO (drohende ZU), § 19 InsO (Ueberschuldung)?
3. **Fristen?** Antragspflicht § 15a InsO: 3 Wochen (ZU), 6 Wochen (Ueberschuldung).
4. **Sanierungs-Pfad?** StaRUG (drohende ZU), Schutzschirm, Eigenverwaltung oder Regelverfahren?

## 3. `kfe-fruherkennungssystem-bauleiter`

**Fokus:** Bauleiter Frueherkennungssystem § 1 StaRUG: Risikolandkarte, Indikatoren, Eskalationsstufen, Berichtswege an Geschaeftsleitung und Aufsichtsorgan. Pruefraster fuer mittelstaendische GmbH.

# KFE: Frueherkennungssystem

## Spezialwissen: KFE: Frueherkennungssystem
- **Spezialgegenstand:** KFE: Frueherkennungssystem / kfe fruherkennungssystem bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StaRUG, KFE.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
