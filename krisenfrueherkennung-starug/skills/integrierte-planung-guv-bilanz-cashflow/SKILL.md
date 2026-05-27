---
name: integrierte-planung-guv-bilanz-cashflow
description: "Integriertes Drei-Statement-Modell (GuV/Bilanz/Cashflow) fuer StaRUG-Planung erstellen: Sanierungsberater braucht konsistentes Planungsmodell. Normen: IDW S 6 (Sanierungsstandard), IDW S 11 (Fortbestehensprognose), HGB §§ 242 ff. (Jahresabschluss), § 1 StaRUG. Pruefraster: GuV-Plan, Bilanzplan, Cash-Flow-Statement, Working-Capital-Modell, Investitions-/Finanzierungsplan, Brucke Ergebnis-Liquiditaet. Output Excel-Modell-Template, Planungsannahmen-Memo. Abgrenzung: Liquiditaetsplanung rolling siehe rollierende-liquiditaetsplanung-24-monate-template; Kennzahlen-Ampel siehe kennzahlenset-und-ampelsystem-starug-konform."
---

# Integrierte Planung — GuV, Bilanz und Cashflow

Wer nur eine GuV-Planung vorlegt, hat keinen Finanzplan. Wer nur eine Liquiditätsplanung vorlegt, hat kein Steuerungsinstrument. Das Drei-Statement-Modell verknüpft Gewinn- und Verlustrechnung, Bilanz und Kapitalflussrechnung zu einer konsistenten Planung, die jedem Anspruch — ob IDW S 6, IDW S 11 oder § 1 StaRUG — standhält. Ohne diese Verknüpfung sind Restrukturierungskonzepte nicht belastbar und Fortführungsprognosen nicht fundiert.

---

## Rechtsgrundlagen

- § 1 StaRUG (Krisenfrüherkennungspflicht, integrierte Planung als Standard)
- IDW S 6 Tz. 85 ff. (integrierte Planungsrechnung als Kern des Sanierungskonzepts)
- IDW S 11 Tz. 23 ff. (Liquiditätsstatus und integrierte Planung)
- IDW S 11 Tz. 30 ff. (Fortführungsprognose — Planungsgrundlage)
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
  Vorräte (DIO)       = (Vorräte / Umsatz) × 365 Tage
  Forderungen (DSO)   = (Forderungen L&L / Umsatz) × 365 Tage
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

---

## Templates

### Muster: Planprämissen-Tabelle (Drei-Statement-Modell)

```
PLANPRÄMISSEN — DREI-STATEMENT-MODELL
Gesellschaft: [Firma]
Basisjahr: [JJJJ]
Planperiode: [JJJJ+1] bis [JJJJ+2]

GuV-TREIBER
  Umsatzwachstum p.a.:       Base [x%] / Bear [-x%]
  Materialkostenquote:        [x%] des Umsatzes
  Personalkostensteigerung:   [x%] p.a. (Tariferhöhung + Headcount)
  Abschreibungsquote:         [x% auf Anlagevermögen Ø]
  Effektivzinssatz:           [x%] auf Ø Bankverbindlichkeiten

WORKING CAPITAL
  DIO (Vorräte):              [x] Tage
  DSO (Forderungen):          [x] Tage
  DPO (Verbindlichkeiten):    [x] Tage

INVESTITIONEN
  Erhaltungs-CAPEX:           EUR [x] p.a.
  Wachstums-CAPEX:            EUR [x] (einmalig in [JJJJ])

FINANZIERUNG
  Tilgung Bankkredit:         EUR [x] p.a.
  Neue Kreditaufnahme:        EUR [x] in [JJJJ]
  Ausschüttung:               EUR [x] (oder: keine Ausschüttung in der Planperiode)
```

---

## Fallstricke

1. **GuV-Planung ohne Cashflow** — in der Praxis verbreitet und gefährlich: profitables Unternehmen kann illiquid werden, wenn Working Capital wächst (z.B. Vorratsaufbau bei Umsatzwachstum).

2. **Planbilanzen werden vergessen** — viele Restrukturierungspläne haben GuV und Cash, aber keine Bilanz. IDW S 6 und IDW S 11 verlangen aber explizit die Planbilanz, um Überschuldungsstatus zu beurteilen.

3. **Stichtagsbezogene statt periodengerechte Abgrenzung** — Rückstellungen und Abgrenzungen in der Bilanzplanung vergessen → rechnerische Lücken zwischen GuV und Cashflow.

4. **Investitionsplanungen ohne Finanzierungsquelle** — CAPEX-Pläne, die nicht mit konkreter Finanzierungsstruktur unterlegt sind, sind Wunschlisten, keine valide Planung.

5. **Steuerlast unterschätzen** — effektiver Steuersatz (Körperschaftsteuer + Solidaritätszuschlag + Gewerbesteuer) beträgt ca. 30 %; diese Position fehlt in vielen „schnellen" Plan-GuVs.

---

## Querverweise

- → `rollierende-liquiditaetsplanung-24-monate-template` — detaillierter Cashflow-Plan
- → `fruehwarnsystem-architektur-zwei-jahres-horizont` — Einbettung in Frühwarnsystem
- → `kennzahlenset-und-ampelsystem-starug-konform` — KPI-Ableitung aus der Planung
- → `fortbestehensprognose-zweistufig` — Nutzung der integrierten Planung für IDW S 11
- → `krisenstadien-stakeholder-strategie-ergebnis-liquiditaet` — Diagnostik auf Basis der Planung


## Aktuelle Leitentscheidungen — Integrierte Planung

- BGH, Urt. v. 07.03.2013 — IX ZR 64/12, NZI 2013, 477 — Integrierte Planung als IDW S 6 Kernbaustein: Sanierungskonzept muss integrierte Guv-Bilanz-Cashflow-Planung enthalten; isolierter Liquiditaetsplan ohne Verbindung zu Guv reicht nicht.
- BGH, Urt. v. 19.12.2017 — IX ZR 285/14, BGHZ 217, 1 — Fortbestehensprognose auf Basis integrierter Planung: Cashflow-Planung muss aus Guv-Annahmen abgeleitet sein; zirkulaere Planungen nicht akzeptiert.
- OLG Muenchen, Beschl. v. 23.05.2019 — 23 U 3003/18, NZI 2019, 694 — Planung und Bankenfinanzierung: Integrierte Planung mit Szenario-Analyse als Voraussetzung fuer Kreditentscheidung; Bank darf auf plausibilisierte Planung vertrauen.
- IDW S 6 — IDW Standard: Grundsaetze zur Erstellung von Sanierungskonzepten, Stand 06/2022 — integrierte Unternehmensplanung als Pflichtbaustein jedes Sanierungskonzepts.

## Paragrafenkette Integrierte Planung

§ 19 Abs. 2 InsO (Fortbestehensprognose auf Basis integrierter Planung) → IDW S 6 (Sanierungskonzept-Standard) → IDW S 11 (Beurteilung Insolvenzgruende) → § 1 StaRUG (24-Monats-Horizont) → § 43 GmbHG (Sorgfaltspflicht bei Planung)

## Triage — Integrierte Planung

1. **Drei-Sicht-Verknuepfung?** Guv-Planung → Cashflow (direkte Methode) → Bilanz-Planung konsistent?
2. **Annahmen dokumentiert?** Umsatz-Wachstumsraten, Kostenentwicklung, Working-Capital-Annahmen transparent?
3. **Szenarien?** Base-Case, Best-Case, Worst-Case durchgerechnet?
4. **Saldo-Check?** Integrierte Planung muss bilanziell schliessen (Bilanzsumme immer ausgeglichen).

## Kommentarliteratur

- IDW S 6, Stand 06/2022 — integrierte Unternehmensplanung.
- IDW S 11, Stand 11/2022 — Liquiditaetsplanung als Teil.
- K. Schmidt/Uhlenbruck, GmbH in Krise, § 5 Rn. 5.5 ff. — Planungsanforderungen Sanierungskonzept.
