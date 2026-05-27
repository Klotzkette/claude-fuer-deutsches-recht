---
name: stb-bwa-betriebsergebnis-deckungsbeitrag
description: "Ausweis Betriebsergebnis vor und nach Zinsen Deckungsbeitragsstruktur in der BWA. Anwendungsfall analytische BWA mit Stufendeckungsbeitrag EBITDA EBIT EBT Mandant aus Industrie Handel Dienstleistung. Methodik fixe und variable Kosten Identifikation Branchenkennzahl. Output BWA mit Ergebnis-Pyramide Stufendeckung."
---

# Betriebsergebnis und Deckungsbeitrag in der BWA

## Kernsachverhalt

Die Standard-BWA weist ein Betriebsergebnis nach Block-Logik aus. Fuer Steuerungszwecke ist aber die Deckungsbeitragsrechnung mit Stufenkonzept ergiebiger: Sie trennt variable von fixen Kosten und zeigt, ab welcher Umsatzhoehe das Unternehmen profitabel arbeitet. Der Steuerberater muss die Standard-BWA so umkonfigurieren oder ergaenzen, dass DB I, DB II und EBITDA/EBIT/EBT klar ablesbar sind. Insbesondere bei Industrie- und Handelsmandanten ist die Deckungsbeitragsstruktur Standard.

## Kaltstart-Rueckfragen

1. Welche Branche und welches Geschaeftsmodell — Industrie mit Fertigung, Handel mit Lagerumschlag, Dienstleistung mit Stundensaetzen?
2. Welche Kosten sind variabel (mit Umsatz schwankend), welche fix (unabhaengig vom Umsatz)?
3. Ist eine Stufendeckungsbeitragsrechnung gewuenscht (DB I, DB II, DB III)?
4. Welche Ergebniskennzahlen benoetigt der Mandant — EBITDA fuer Banken, EBIT fuer interne Steuerung?
5. Werden kalkulatorische Positionen ausgewiesen (kalk. Unternehmerlohn, kalk. Miete)?
6. Internationale Stakeholder vorhanden (Mutter, Investor), die UKV-Format bevorzugen?
7. Welche Kostenstellenstruktur ist hinterlegt (Profit Center, Cost Center)?
8. Wird eine Produktdeckungsbeitrags-Auswertung benoetigt (Auftragskalkulation)?

## Rechtlicher Rahmen

### Primaernormen

**§ 275 HGB** — GuV-Gliederung GKV (Abs. 2) oder UKV (Abs. 3); Wahlrecht. Deckungsbeitragsrechnung ist mit UKV besser abbildbar.

**§ 238 HGB** — Buchfuehrungspflicht.

**§ 252 HGB** — Bewertungsstetigkeit; Wechsel der BWA-Form muss begruendet werden.

### Standards

- IDW PS 480 — Erstellungsgrundsaetze (analog auf BWA).
- DATEV BWA-Formen 01 (Standard), 11 (Bewegungs-BWA), 21 (Branchen-BWA).

## Workflow

### Phase 1 — Kostenstruktur analysieren

| Kostenart | Typische Zuordnung |
|---|---|
| Wareneinsatz/Materialeinsatz | Variable Kosten (mit Umsatz schwankend) |
| Fremdleistungen | Variable Kosten (auftragsabhaengig) |
| Akkord-/Stueck-Lohn | Variable Kosten |
| Zeitlohn/Festgehalt | Fixe Kosten |
| Miete/Pacht | Fixe Kosten |
| Versicherungen | Fixe Kosten |
| Werbung Standard | Fixe Kosten |
| Provisionen | Variable Kosten |
| Abschreibungen | Fixe Kosten (Strukturkosten) |
| Zinsen | Finanzkosten (separat) |

### Phase 2 — Stufendeckungsbeitrag konfigurieren

```
Umsatzerloese                          [Umsatz]
- Variable Kosten (Material, FL, var. Lohn) [Var. K]
= DECKUNGSBEITRAG I (Rohgewinn)        [DB I]
- Fixkosten der Kostenstelle / des Produkts [Fix-KSt]
= DECKUNGSBEITRAG II                   [DB II]
- Allgemeine Fixkosten Unternehmen     [Allg. Fix]
= BETRIEBSERGEBNIS / EBITDA            [BE]
- Abschreibungen                       [AfA]
= EBIT
- Zinsergebnis                         [Zins]
= EBT (Ergebnis vor Steuern)
- Ertragsteuern                        [Steuern]
= JAHRESUEBERSCHUSS
```

### Phase 3 — DATEV/Addison-Konfiguration

- DATEV: BWA-Form 21 (Branchen) oder individuelle BWA-Form ueber Berater-Konfiguration.
- Addison: BWA-Definition mit eigenen Bloecken.
- Kostenstellen-Zuordnung ueber DATEV-Kostenrechnung oder Sachkontenmasken.

### Phase 4 — Break-even-Analyse

- Break-even-Umsatz = Fixkosten / Deckungsbeitragsrate.
- Deckungsbeitragsrate = DB I / Umsatz.
- Sicherheitsmarge = (Ist-Umsatz minus Break-even) / Ist-Umsatz.
- Beispiel: Fixkosten 100.000 EUR, DB-Rate 40 Prozent → Break-even 250.000 EUR Umsatz.

### Phase 5 — Reporting und Erlaeuterung

- BWA mit Stufendeckung auf einer Seite.
- Erlaeuterung Schwellenwerte: Break-even, Sicherheitsmarge.
- Bei sinkendem DB I: Pruefung Wareneinsatz, Lieferantenkonditionen.
- Bei steigenden Fixkosten ohne Umsatzaequivalent: Fixkostenstruktur hinterfragen.

### Phase 6 — Quartalsgespraech mit Mandant

- DB-Struktur erlaeutern, Mandant fuer die Stellschrauben sensibilisieren.
- Massnahmen-Plan bei kritischer Marge: Preiserhoehung, Sortimentsbereinigung, Fixkostensenkung.

## Output

- BWA mit Deckungsbeitragsstruktur (DB I, DB II, EBITDA, EBIT, EBT).
- Break-even-Analyse und Sicherheitsmarge.
- Erlaeuterungstext fuer Mandant.

## Strategie und Praxis-Tipps

- Stufendeckungsbeitrag ist bei Handel und Industrie Pflicht; bei Dienstleistung haeufig Stunden-DB sinnvoller.
- EBITDA ist Bank-Standard fuer Schuldendienstpruefung (EBITDA-Multiple).
- Bei kalkulatorischen Positionen Mandant darauf hinweisen, dass es sich um Sicht der Betriebswirtschaft handelt, nicht um steuerliche Behandlung.
- DB-Rate als Kennzahl monatlich tracken — sinkende DB-Rate bei steigendem Umsatz ist Alarmsignal (Preisdruck).
- StBVV: Individuelle BWA-Konfiguration als Zusatzauftrag mit Zeithonorar abrechnen.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-bwa-kennzahlen-rentabilitaet-eigenkapital` — Rentabilitaetskennzahlen.
- `stb-bwa-cashflow-laienverstaendlich` — Cashflow-Darstellung.
- `stb-bwa-branchenvergleich-bbe-datev` — Branchenvergleich.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 252, 275.
- IDW PS 480.
- DATEV BWA-Form 01, 11, 21.
- Schweitzer/Kuepper, Systeme der Kostenrechnung (Standardlehrbuch).
- Coenenberg, Kostenrechnung und Kostenanalyse.
