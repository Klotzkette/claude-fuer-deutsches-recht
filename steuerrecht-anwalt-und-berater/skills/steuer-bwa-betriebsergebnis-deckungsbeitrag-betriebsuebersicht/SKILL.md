---
name: steuer-bwa-betriebsergebnis-deckungsbeitrag-betriebsuebersicht
description: "Steuer BWA Betriebsergebnis Deckungsbeitrag Betriebsuebersicht: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Steuer BWA Betriebsergebnis Deckungsbeitrag Betriebsuebersicht

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **Steuer BWA Betriebsergebnis Deckungsbeitrag Betriebsuebersicht** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stb-bwa-betriebsergebnis-deckungsbeitrag` | Ausweis Betriebsergebnis vor und nach Zinsen Deckungsbeitragsstruktur in der BWA. Anwendungsfall analytische BWA mit Stufendeckungsbeitrag EBITDA EBIT EBT Mandant aus Industrie Handel Dienstleistung. Methodik fixe und variable Kosten Identifikation Branchenkennzahl. Output BWA mit Ergebnis-Pyramide Stufendeckung. |
| `stb-bwa-betriebsuebersicht-erstellen` | Betriebsuebersicht als ergaenzende Auswertung zur BWA. Anwendungsfall ausführliche Monats- oder Quartalsauswertung mit allen Sachkonten-Salden ergaenzend zur kompakten BWA. Methodik Konfiguration in DATEV oder Addison als Kontenliste mit Vorjahres- und Plan-Spalten. Output Betriebsuebersicht als PDF Anhang zur BWA. |
| `stb-bwa-bewegungsbilanz-erstellen` | Bewegungsbilanz aus BWA und SuSa erstellen. Anwendungsfall Veranschaulichung Geld- und Mittelfluss zwischen zwei Stichtagen Vermögens- und Kapitalbewegung. Methodik Aktiva und Passiva Vergleich Mittelherkunft Mittelverwendung. Output Bewegungsbilanz als Anhang zur BWA. Querverweis stb-bwa-cashflow-laienverstaendlich. |
| `stb-bwa-branchenvergleich-bbe-datev` | Branchenvergleich BWA auf Basis BBE-Datenbank über DATEV. Anwendungsfall Quartals- oder Jahres-BWA mit anonymisierten Branchen-Mittelwerten Median Top-Quartil. Methodik Branche identifizieren Vergleichsperiode waehlen Kennzahlenprüfung. Output BWA mit Branchenvergleichs-Spalte Erlaeuterung. |
| `stb-bwa-cashflow-laienverstaendlich` | Cashflow-Darstellung für Mandant in laienverstaendlicher Form. Anwendungsfall Quartals-BWA mit vereinfachter Cashflow-Aufstellung für GF ohne Finanz-Hintergrund. Methodik einfache Mittelfluss-Tabelle Brutto-Netto-Cashflow Trennung zahlungswirksam vs nicht-zahlungswirksam. Output 1-seitige Cashflow-Übersicht. |
| `stb-bwa-erlaeuterungstext-mandant` | Erlaeuterungstext unter der BWA für den Mandanten. Anwendungsfall Monats- oder Quartals-BWA mit kurzem fachlichem Begleittext der die wesentlichen Abweichungen und Risiken benennt. Aufbau Sachverhalt Erlaeuterung Ausblick Empfehlung. Output strukturierter Erlaeuterungstext 1 bis 2 Seiten als Anhang zur BWA Querverweis stb-bwa-mandantengespraech-uebergabe. |
| `stb-bwa-fehlerquellen-haeufig` | Typische Fehlerquellen in der BWA. Anwendungsfall Qualitaetsprüfung BWA durch Berufstraeger interne Stichprobe Fehler in Periodenabgrenzung Buchungsfehler Bestandsveraenderung Lohnbuchungen. Methodik Checkliste Plausibilitaetsprüfung. Output Fehlerprotokoll Korrekturmassnahmen Schulungsbedarf Querverweis stb-bwa-aufbau-grundlagen. |
| `stb-bwa-jahres-bwa-erstellen` | Jahres-BWA als Ergaenzung zum Jahresabschluss. Anwendungsfall Jahresabschluss-Begleitung mit BWA für das Gesamtjahr inkl Vorjahresvergleich Mehrjahrestrend und Mandantenpraesentation. Methodik kumulierte BWA mit Korrekturen Sondereffekten Mehrjahresvergleich. Output Jahres-BWA als Praesentations-PDF. |
| `stb-bwa-kapitalflussrechnung-iduk` | Kapitalflussrechnung nach indirekter Methode aus BWA und Bilanz. Anwendungsfall Jahresabschluss Bankreporting Sanierungskonzept Konzernabschluss. Methodik DRS 21 indirekte Ableitung aus Jahresueberschuss Mittelfluss laufende Geschäftstätigkeit Investitionstätigkeit Finanzierungstätigkeit. Output Kapitalflussrechnung als Standalone-Anhang. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **Steuer BWA Betriebsergebnis Deckungsbeitrag Betriebsuebersicht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stb-bwa-betriebsergebnis-deckungsbeitrag`

**Fokus:** Ausweis Betriebsergebnis vor und nach Zinsen Deckungsbeitragsstruktur in der BWA. Anwendungsfall analytische BWA mit Stufendeckungsbeitrag EBITDA EBIT EBT Mandant aus Industrie Handel Dienstleistung. Methodik fixe und variable Kosten Identifikation Branchenkennzahl. Output BWA mit Ergebnis-Pyramide Stufendeckung.

# Betriebsergebnis und Deckungsbeitrag in der BWA

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Betriebsergebnis und Deckungsbeitrag in der BWA` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


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
Umsatzerloese [Umsatz]
- Variable Kosten (Material, FL, var. Lohn) [Var. K]
= DECKUNGSBEITRAG I (Rohgewinn) [DB I]
- Fixkosten der Kostenstelle / des Produkts [Fix-KSt]
= DECKUNGSBEITRAG II [DB II]
- Allgemeine Fixkosten Unternehmen [Allg. Fix]
= BETRIEBSERGEBNIS / EBITDA [BE]
- Abschreibungen [AfA]
= EBIT
- Zinsergebnis [Zins]
= EBT (Ergebnis vor Steuern)
- Ertragsteuern [Steuern]
= JAHRESUEBERSCHUSS
```

### Phase 3 — DATEV/Addison-Konfiguration

- DATEV: BWA-Form 21 (Branchen-BWA) oder individuelle BWA-Form ueber Berater-Konfiguration. Klickpfad: Rechnungswesen → Stammdaten → Auswertungspakete → Eigene BWA-Form definieren.
- Addison: BWA-Definition mit eigenen Bloecken im Auswertungsmanager.
- Kostenstellen-Zuordnung ueber DATEV-Kostenrechnung (Modul Kostenrechnung Classic/Comfort) oder Sachkontenmasken mit Kostenstellen-Feld.

### Phase 4 — Break-even-Analyse

- Break-even-Umsatz = Fixkosten geteilt durch Deckungsbeitragsrate.
- Deckungsbeitragsrate = DB I geteilt durch Umsatz.
- Sicherheitsmarge = (Ist-Umsatz minus Break-even-Umsatz) geteilt durch Ist-Umsatz.
- Rechenbeispiel: Fixkosten 100.000 EUR, DB-Rate 40 Prozent ergibt einen Break-even-Umsatz von 250.000 EUR. Liegt der Ist-Umsatz bei 300.000 EUR, betraegt die Sicherheitsmarge rund 17 Prozent.

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
- `stb-bwa-statische-liquiditaet-kennzahlen` — Liquiditaetskennzahlen ergaenzend zur DB-Rechnung.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 252, 275.
- IDW PS 480.
- DATEV BWA-Form 01, 11, 21.
- Schweitzer/Kuepper, Systeme der Kostenrechnung (Standardlehrbuch).
- Coenenberg, Kostenrechnung und Kostenanalyse.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `stb-bwa-betriebsuebersicht-erstellen`

**Fokus:** Betriebsuebersicht als ergaenzende Auswertung zur BWA. Anwendungsfall ausführliche Monats- oder Quartalsauswertung mit allen Sachkonten-Salden ergaenzend zur kompakten BWA. Methodik Konfiguration in DATEV oder Addison als Kontenliste mit Vorjahres- und Plan-Spalten. Output Betriebsuebersicht als PDF Anhang zur BWA.

# Betriebsuebersicht erstellen — Ergaenzung zur BWA

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Betriebsuebersicht erstellen — Ergaenzung zur BWA` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die Standard-BWA fasst Konten in funf Bloecken zusammen. Fuer detaillierte Analysen reicht das nicht — der Mandant will wissen, woraus sich "sonstige betriebliche Aufwendungen" zusammensetzen oder welche Erloeskonten beigetragen haben. Die Betriebsuebersicht ist die Kontenliste mit Salden, Vorjahresvergleich und ggf. Plan-Werten. Sie ergaenzt die BWA und ist Standard bei groesseren Mandanten und im Steuerberater-Buero zur internen Analyse.

## Kaltstart-Rueckfragen

1. Welche Detailtiefe — alle Konten oder nur die wesentlichen?
2. Mandantenwunsch Layout — Konten in der Reihenfolge des Kontenrahmens oder strukturiert nach Funktionsbereichen?
3. Welche Vergleichsspalten — Vormonat, Vorjahres-Monat, kumulierter Jahresvergleich, Plan?
4. Welche Sortierung — Saldenhoehe, Kontenrahmen, alphabetisch?
5. Welche Schwellenwerte — Konten mit Saldo unter X EUR ausblenden?
6. Liegen Sachkontenbezeichnungen aktuell vor (Stammdaten aktualisieren)?
7. Wird die Uebersicht intern oder extern (Mandant, Bank, Investor) genutzt?
8. Welche Konten muessen vertraulich gefuehrt werden (z.B. GF-Bezuege)?

## Rechtlicher Rahmen

### Primaernormen

**§ 238 HGB** — Buchfuehrungspflicht.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 33 StBerG** — Aufgabenkreis StB.

### Standards

- DATEV BWA-Form 21 (Branchen-BWA) und Kontenuebersicht.
- IDW PS 480 (Erstellungsgrundsaetze).

## Workflow

### Phase 1 — Konfigurations-Wahl

| Form | Verwendung |
|---|---|
| Reine Kontenliste | Interne Stichprobe, Sachbearbeiter-Pruefung |
| Strukturierte Betriebsuebersicht | Mandant, Berufstraeger-Pruefung |
| Branchen-Betriebsuebersicht | Branchen-Vergleich (BBE) |
| Erweiterte Betriebsuebersicht | Bank-/Investor-Reporting |

### Phase 2 — Aufbau strukturierte Betriebsuebersicht

Beispiel-Aufbau (Kontennummern typische SKR 03-Beispiele; konkrete Nummern mit aktueller DATEV-Kontenrahmenfassung abgleichen):

```
BETRIEBSUEBERSICHT
Mandant: [Firma]
Zeitraum: [Monat / kumuliert]

I. UMSATZ UND BETRIEBLICHE ERTRAEGE
 8400 Erloese 19 Prozent USt [X]
 8300 Erloese 7 Prozent USt [X]
 8125 Erloese steuerfreie innergem. Lieferung [X]
 8200 Sonstige betriebliche Ertraege [X]

II. MATERIAL- UND WARENEINSATZ
 3400 Wareneingang 19 Prozent VSt [X]
 3300 Wareneingang 7 Prozent VSt [X]
 3100 Fremdleistungen [X]

III. PERSONALKOSTEN
 4120 Loehne [X]
 4130 Gehaelter [X]
 4138 Beitraege zur Berufsgenossenschaft [X]
 4140 Krankenkassen-AG-Anteil [X]

IV. SONSTIGE BETRIEBLICHE AUFWENDUNGEN
 4210 Miete [X]
 4240 Gas Strom Wasser [X]
 4500 Kfz-Kosten [X]
 4600 Werbe- und Reisekosten [X]
 4900 Sonstige betriebliche Aufwendungen [X]

V. ABSCHREIBUNGEN
 4830 Absetzungen auf Sachanlagen [X]

VI. ZINSERGEBNIS UND STEUERN
 7300 Zinsen und aehnliche Aufwendungen [X]
 7100 Zinsertraege [X]
 7600 Steuern vom Einkommen und Ertrag [X]

ERGEBNIS NACH STEUERN [X]
```

### Phase 3 — Vergleichsspalten

| Spalte | Inhalt | Quelle |
|---|---|---|
| Monat aktuell | Ist-Saldo der Periode | BWA-Buchungen |
| Monat Vorjahres-Periode | Saldo gleicher Monat Vorjahr | Vorjahres-DATEV |
| Kumuliert Jahr | Saldo seit Jahresbeginn | Year-to-Date |
| Kumuliert Vorjahres-Jahr | Vorjahres-YTD | Vorjahres-DATEV |
| Plan-Wert | Aus Stammdaten | Plan-Eingabe |
| Abweichung absolut | Ist minus Vorjahr / Plan | Berechnung |
| Abweichung in Prozent | absolute Abweichung / Vergleichswert | Berechnung |

### Phase 4 — Filter und Sortierung

- Konten ohne Saldo ausblenden (Default).
- Konten mit Saldo < 100 EUR ggf. ausblenden (oder als "Sonstige" zusammenfassen).
- Sortierung nach Kontenrahmen (SKR 03 oder SKR 04).
- Innerhalb der Bloecke nach Saldenhoehe absteigend (optional).

### Phase 5 — Vertrauliche Konten

- GF-Bezuege, Tantiemen: Mandantenwunsch beachten (oft separat behandeln).
- Privatentnahmen Einzelunternehmer: nicht in BWA, sondern Kapitalkonto.
- Sondergesellschafterdarlehen: separat ausweisen.

### Phase 6 — Versand und Ablage

- Als PDF gemeinsam mit BWA.
- Ablage in Mandantenakte mit Versanddatum.
- Mandanten-Portal-Download moeglich.

## Output

- Betriebsuebersicht als strukturiertes PDF.
- Anhang zur BWA.
- Interne Auswertungs-Datei (Excel-Export aus DATEV).

## Strategie und Praxis-Tipps

- Betriebsuebersicht ist Pflicht bei Mittelstand und Konzern-Reporting.
- Bei KMU: optional, mandantenabhaengig anbieten.
- Vertrauliche Konten klar markieren oder in geschuetzten Bereich auslagern.
- Bei Wechsel des Kontenrahmens Vorjahresvergleich nicht moeglich ohne Brueckenposten.
- DATEV-Tipp: Standard-Betriebsuebersicht 21 oder individuelle Konfiguration ueber Berater-Stammdaten.
- StBVV: Standardform pauschaliert, individuelle Konfiguration als Zeithonorar.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-susa-erstellen-grundlagen` — Summen- und Saldenliste als Grundlage.
- `stb-bwa-zeitlicher-vergleich-jahresvergleich` — Vorjahresvergleich.
- `stb-bwa-kontenrahmen-skr03-skr04` — Kontenrahmenwahl und Mapping.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 252.
- StBerG § 33.
- DATEV BWA-Form 21, Kontenuebersicht.
- IDW PS 480.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `stb-bwa-bewegungsbilanz-erstellen`

**Fokus:** Bewegungsbilanz aus BWA und SuSa erstellen. Anwendungsfall Veranschaulichung Geld- und Mittelfluss zwischen zwei Stichtagen Vermögens- und Kapitalbewegung. Methodik Aktiva und Passiva Vergleich Mittelherkunft Mittelverwendung. Output Bewegungsbilanz als Anhang zur BWA. Querverweis stb-bwa-cashflow-laienverstaendlich.

# Bewegungsbilanz aus BWA und SuSa

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Bewegungsbilanz aus BWA und SuSa` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die Bewegungsbilanz stellt die Veraenderungen einzelner Bilanzposten zwischen zwei Stichtagen dar und macht damit deutlich, woher Mittel kamen (Mittelherkunft) und wohin sie geflossen sind (Mittelverwendung). Sie ist Vorstufe der Kapitalflussrechnung nach DRS 21 und IDW S 6 und wird besonders bei Bankgespraechen, Sanierungsmandaten und im Vorfeld der Fortbestehensprognose benoetigt. Der Steuerberater erstellt sie aus der SuSa zum Anfangs- und Endstichtag plus den BWA-Erfolgskonten.

## Kaltstart-Rueckfragen

1. Welche Stichtage — Quartal, Halbjahr, Jahresende?
2. Liegt eine Stichtag-SuSa vor (Anfang und Ende der Periode)?
3. Welche Detailtiefe — Hauptposten oder einzelne Konten?
4. Sondereffekte in der Periode (Anlagenverkauf, Kapitalerhoehung, Gesellschafterdarlehen)?
5. Verwendungszweck — interne Steuerung, Bankgespraech, Sanierungskonzept?
6. Welche Vergleichsperiode — Vorjahresperiode parallel?
7. Welche Konsolidierung — Einzelgesellschaft oder Konzernblick?
8. Welche Abgrenzung — Geldfluss vs. nicht-zahlungswirksame Posten (Abschreibungen, Rueckstellungen)?

## Rechtlicher Rahmen

### Primaernormen

**§ 264 HGB** — Aufstellungspflicht Jahresabschluss; Anhang ggf. mit Kapitalflussrechnung.

**§ 297 HGB** — Konzernabschluss; Kapitalflussrechnung verpflichtend.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 19 InsO** — Fortbestehensprognose; Bewegungsbilanz als analytische Grundlage.

### Standards

- DRS 21 — Kapitalflussrechnung (verbindlich fuer Konzernabschluesse, empfohlen fuer Einzelabschluesse).
- IDW S 6 — Sanierungskonzept (Bewegungsbilanz als analytische Grundlage).
- IDW PS 305 — Risikofrueherkennung § 91 Abs. 2 AktG.

## Workflow

### Phase 1 — Datenbasis

- SuSa zum Anfangsstichtag (z.B. 31.12. Vorjahr).
- SuSa zum Endstichtag (z.B. 31.12. Berichtsjahr).
- BWA-Daten fuer die Periode (insbesondere Abschreibungen, Rueckstellungsveraenderung).
- Anlagenspiegel (Zugaenge, Abgaenge, AfA).

### Phase 2 — Strukturierung Aktiva

```
AKTIVA-VERAENDERUNG:
Position Anfang Ende Veraenderung
Anlagevermoegen
 Sachanlagen [X] [Y] [+/-Z]
 Immaterielle WG [X] [Y] [+/-Z]
 Finanzanlagen [X] [Y] [+/-Z]
Umlaufvermoegen
 Vorraete [X] [Y] [+/-Z]
 Forderungen LuL [X] [Y] [+/-Z]
 Sonstige Forderungen [X] [Y] [+/-Z]
 Liquide Mittel [X] [Y] [+/-Z]
Aktive Rechnungsabgrenzung [X] [Y] [+/-Z]
```

### Phase 3 — Strukturierung Passiva

```
PASSIVA-VERAENDERUNG:
Eigenkapital
 Gezeichnetes Kapital [X] [Y] [+/-Z]
 Kapitalruecklagen [X] [Y] [+/-Z]
 Gewinn-/Verlustruecklage [X] [Y] [+/-Z]
 Jahresergebnis [X] [Y] [+/-Z]
Rueckstellungen [X] [Y] [+/-Z]
Verbindlichkeiten
 Kreditinstitute [X] [Y] [+/-Z]
 Lieferanten [X] [Y] [+/-Z]
 Sonstige Verbindlichkeiten [X] [Y] [+/-Z]
Passive Rechnungsabgrenzung [X] [Y] [+/-Z]
```

### Phase 4 — Mittelherkunft und Mittelverwendung

```
MITTELHERKUNFT:
- Jahresueberschuss
- Abschreibungen (zahlungsunwirksam)
- Erhoehung Rueckstellungen
- Erhoehung Verbindlichkeiten
- Verringerung Vorraete
- Verringerung Forderungen
- Anlagenabgang (Veraeusserung)
- Kapitalerhoehung Gesellschafter

MITTELVERWENDUNG:
- Jahresfehlbetrag
- Verringerung Rueckstellungen
- Verringerung Verbindlichkeiten
- Erhoehung Vorraete
- Erhoehung Forderungen
- Anlagenzugang (Investition)
- Ausschuettung an Gesellschafter
```

### Phase 5 — Saldo und Pruefung

- Saldo Mittelherkunft minus Mittelverwendung = Veraenderung liquide Mittel.
- Gegencheck: Veraenderung Bank-Konten in SuSa muss matchen.
- Differenz zeigt Fehler in der Aufstellung — pruefen.

### Phase 6 — Erlaeuterung und Versand

- Erlaeuterungstext fuer wesentliche Bewegungen.
- Bei Bank-/Investor-Reporting: zusammen mit Bilanz und BWA.
- Mandantenakte dokumentieren.

## Output

- Bewegungsbilanz als strukturiertes PDF.
- Erlaeuterungstext zu wesentlichen Veraenderungen.
- Vorstufe fuer Kapitalflussrechnung.

## Strategie und Praxis-Tipps

- Die Bewegungsbilanz ist bei Kleinunternehmen keine Pflicht, gehoert bei mittelstaendischer Bilanzanalyse jedoch zum Standard.
- Banken erwarten bei groesseren Kreditengagements regelmaessig eine Bewegungsbilanz oder direkt eine Kapitalflussrechnung.
- Bei Sanierungsmandaten ist die Bewegungsbilanz Pflichtbestandteil neben dem Liquiditaetsplan.
- Praxis-Tipp: Die Bewegungsbilanz wird ueblicherweise halbjaehrlich erstellt und nicht monatlich, da der Aufstellungsaufwand bei kuerzerem Intervall den Steuerungsnutzen uebersteigt.
- StBVV: Diese Sonderauswertung wird ueber Zeithonorar oder Pauschalvereinbarung gesondert abgerechnet.
- DATEV-Tipp: Das DATEV-Bilanzbericht-/BAB-Modul automatisiert die Bewegungsbilanz aus zwei SuSa-Stichtagen (Klickpfad: Rechnungswesen → Auswertungen → Bewegungsbilanz oder Bilanzanalyse-Auswertungspaket).

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-bwa-kapitalflussrechnung-iduk` — Kapitalflussrechnung.
- `stb-bwa-cashflow-laienverstaendlich` — Cashflow.
- `stb-liquiditaetsvorschau-3-6-12-monate` — Liquiditaetsplan.
- `stb-bwa-sus-bilanz-pruefung` — Krisensignale.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 264, 297.
- DRS 21.
- IDW S 6, IDW PS 305.
- InsO § 19.
- DATEV BAB-Modul.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `stb-bwa-branchenvergleich-bbe-datev`

**Fokus:** Branchenvergleich BWA auf Basis BBE-Datenbank über DATEV. Anwendungsfall Quartals- oder Jahres-BWA mit anonymisierten Branchen-Mittelwerten Median Top-Quartil. Methodik Branche identifizieren Vergleichsperiode waehlen Kennzahlenprüfung. Output BWA mit Branchenvergleichs-Spalte Erlaeuterung.

# Branchenvergleich BBE / DATEV in der BWA

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Branchenvergleich BBE / DATEV in der BWA` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die DATEV BBE-Datenbank (Betriebswirtschaftliche Beratung) liefert anonymisierte Vergleichsdaten von Mandanten gleicher Branche. Der Mandant kann sich so im Branchen-Mittelwert, Median und Top-Quartil verorten. Der Branchenvergleich ist starkes Beratungs-Instrument bei Quartals- und Jahresgespraechen, weil er den Mandanten nicht mit blanken Zahlen, sondern mit der Wettbewerbssituation konfrontiert. Voraussetzung: SKR 03 mit Standard-Konten, klare Branchen-Klassifikation (WZ-Code).

## Kaltstart-Rueckfragen

1. Welche Branche — WZ-Code 2008 (Statistisches Bundesamt) bzw. Branchenschluessel?
2. Welche Mandantengroesse (Umsatz, Mitarbeiterzahl)?
3. Welche Vergleichsbasis — Branchen-Median, -Mittelwert, Top-Quartil?
4. Welche Periode — Berichtsjahr abgeschlossen oder unterjaehrig vergleichend?
5. Welche Datentiefe — gesamte GuV oder einzelne Kennzahlen?
6. Welches BBE-Modul ist abonniert — Standard, erweitert?
7. Wie aktuell sind die Branchen-Daten (BBE liefert mit 1-2 Jahren Verzug)?
8. Welche Sondereffekte sind herauszurechnen (Saison, Einmaleffekte)?

## Rechtlicher Rahmen

### Primaernormen

**§ 33 StBerG** — StB-Aufgabenkreis.

**§ 57 StBerG** — Gewissenhaftigkeit (Datenqualitaet).

**§ 102 StaRUG** — Hinweispflicht; Branchenvergleich kann Krisensignal verstaerken oder relativieren.

**§ 4 BDSG / DSGVO** — Datenschutz; BBE-Daten sind anonymisiert.

### Standards

- DATEV BBE-Branchenbericht (Standard).
- BVR-Branchenanalysen (Volks- und Raiffeisenbanken).
- Sparkassen-Branchenbarometer.
- IDW PS 480.

## Workflow

### Phase 1 — Branchenklassifikation

- WZ-Code des Mandanten ermitteln (aktuelle Klassifikation der Wirtschaftszweige des Statistischen Bundesamtes; bisher WZ 2008, Aktualisierung pruefen).
- Beispiele typischer WZ-Codes: Restaurants mit Bedienung, Lebensmittel-Einzelhandel, Bau von Wohngebaeuden (konkrete Schluessel im Mandantenstamm gegen die aktuelle WZ-Fassung pruefen).
- Im DATEV-Stammblatt erfassen — Voraussetzung fuer BBE-Auswertung (Klickpfad: Mandantendaten → Allgemeines → Branchenschluessel).
- Bei Mischbetrieb: Hauptbranche festlegen und Nebenbranche dokumentieren.

### Phase 2 — BBE-Datenabruf

- DATEV-Klickpfad: Kanzlei-Rechnungswesen → Auswertungen → BBE-Branchenvergleich.
- Berichtsjahr und Vergleichsperiode auswaehlen.
- Datenstand pruefen — BBE-Daten weisen typischerweise einen Zeitverzug von ein bis zwei Jahren auf.
- Filter nach Mandantengroesse (Umsatzklasse) setzen, damit Vergleich zur Peer-Gruppe sauber ist.

### Phase 3 — Standard-Kennzahlen

| Kennzahl | Mandant | Branchen-Median | Top-Quartil |
|---|---|---|---|
| Materialquote | [X] Prozent | [Y] Prozent | [Z] Prozent |
| Personalquote | [X] Prozent | [Y] Prozent | [Z] Prozent |
| Umsatz je Mitarbeiter | [X] EUR | [Y] EUR | [Z] EUR |
| EBITDA-Marge | [X] Prozent | [Y] Prozent | [Z] Prozent |
| EBIT-Marge | [X] Prozent | [Y] Prozent | [Z] Prozent |
| Eigenkapitalquote | [X] Prozent | [Y] Prozent | [Z] Prozent |
| Anlagendeckung | [X] Prozent | [Y] Prozent | [Z] Prozent |

### Phase 4 — Verortung und Bewertung

- Mandant im Branchen-Quartil verorten (1. Quartil = bestes, 4. Quartil = schlechtestes Viertel).
- Auffaellige Abweichungen identifizieren (mehr als 20 Prozent vom Median).
- Plausibilitaet pruefen — extreme Abweichungen koennen auch auf Datenfehler hinweisen.

### Phase 5 — Beratungsansatz

- Bei unterdurchschnittlicher Materialquote: Einkaufsvorteil — staerken.
- Bei ueberdurchschnittlicher Personalquote: Produktivitaet pruefen, ggf. Personalentwicklung diskutieren.
- Bei niedriger EBITDA-Marge: Preisgestaltung, Sortimentsbereinigung pruefen.
- Bei niedriger Eigenkapitalquote: Bilanzpolitik (Thesaurierung), Finanzierungsstruktur.

### Phase 6 — Erlaeuterung im Quartalsgespraech

- Branchenvergleich Praesentation an Mandant.
- Stellen heraus: was ist Ueberdurchschnitt, was Unterdurchschnitt.
- Handlungsoptionen ableiten.
- Massnahmen-Plan zur naechsten Quartals-Pruefung.

## Output

- BWA mit Branchenvergleichs-Spalte oder Anhang.
- Verortungsbericht mit Top-Quartil-Vergleich.
- Massnahmen-Plan.

## Strategie und Praxis-Tipps

- BBE-Daten sind nicht ideal aktuell — bei schnellen Marktveraenderungen ggf. mit zusaetzlichen Quellen ergaenzen (Bundesverbaende, Bafa-Studien).
- Bei spezialisierten Branchen ist BBE manchmal duenn — alternative Datenbasis (Statistik der DStV, IfM-Bonn) pruefen.
- Mandant nicht ueberfordern — 3-5 Kennzahlen reichen, mehr verwirrt.
- Branchenvergleich nicht moralisieren — Mandant darf in einer Branche auch unterdurchschnittlich sein, wenn er bewusst Nische besetzt.
- StBVV: BBE-Bericht als Zusatzleistung, ueber Pauschal oder Zeithonorar.
- Datenschutz: BBE-Berichte enthalten anonymisierte Daten; nicht weitergeben an Dritte ohne Mandantenzustimmung.

## Querverweise

- `stb-bwa-zeitlicher-vergleich-jahresvergleich` — Vorjahresvergleich.
- `stb-bwa-kennzahlen-rentabilitaet-eigenkapital` — Rentabilitaetskennzahlen.
- `stb-bwa-mandantengespraech-uebergabe` — Quartalsgespraech.
- `stb-bwa-mandantenreport-monatlich` — Monatsreport.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- StBerG §§ 33, 57.
- DSGVO / BDSG.
- DATEV BBE-Branchenbericht.
- Klassifikation der Wirtschaftszweige (WZ 2008, Statistisches Bundesamt; aktuelle Fassung unter destatis.de abrufbar).
- IDW PS 480.
- Hinweis: BBE-Datenstand vor Mandanteneinsatz pruefen (Zeitverzug von ein bis zwei Jahren ueblich); Branchenrichtwerte aus aktuellem DATEV-BBE-Bericht oder Branchenverbands-Daten entnehmen.

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 1 bestaetigt (WZ 2008 Statistisches Bundesamt bestaetigt), 1 ersetzt (Hinweis ohne Marker neu formuliert) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `stb-bwa-cashflow-laienverstaendlich`

**Fokus:** Cashflow-Darstellung für Mandant in laienverstaendlicher Form. Anwendungsfall Quartals-BWA mit vereinfachter Cashflow-Aufstellung für GF ohne Finanz-Hintergrund. Methodik einfache Mittelfluss-Tabelle Brutto-Netto-Cashflow Trennung zahlungswirksam vs nicht-zahlungswirksam. Output 1-seitige Cashflow-Übersicht.

# Cashflow laienverstaendlich darstellen

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Cashflow laienverstaendlich darstellen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die DRS-21-Kapitalflussrechnung ist methodisch korrekt, aber fuer den nicht-finanzaffinen Mandanten zu komplex. Fuer das Mandantengespraech braucht es eine einfachere Darstellung: Wie viel Cash kam laufend rein? Was wurde investiert? Was wurde an Bank/Gesellschafter zurueckgezahlt? Was bleibt am Monatsende? Der Steuerberater erstellt eine 1-seitige Brutto-Cashflow-Uebersicht, die dem Mandanten die Geldfluesse zeigt — ohne ihn zu ueberfordern.

## Kaltstart-Rueckfragen

1. Welcher Mandantentyp — Solo, Familien-GmbH, Mittelstand?
2. Welcher Verstaendnisgrad — Bilanz-affin oder GF ohne Finanzhintergrund?
3. Welcher Zeitraum — Monat, Quartal, Jahr?
4. Welche Detailtiefe — nur Hauptposten oder mit Einzeladern?
5. Welche Vergleichsperiode — Vorjahres-Quartal, Vorjahr?
6. Welche Investitionen sind separat darzustellen?
7. Welche Gesellschafter-Bewegungen (Ausschuettung, Privateinlage)?
8. Welcher Verwendungszweck — interne Steuerung, Bankgespraech?

## Rechtlicher Rahmen

### Primaernormen

**§ 33 StBerG** — StB-Aufgabenkreis; mandantengerechte Aufbereitung.

**§ 57 StBerG** — Gewissenhaftigkeit.

**§ 252 HGB** — Going-concern.

**§ 19 InsO** — Fortbestehensprognose; Cashflow-Betrachtung Pflicht.

### Standards

- DRS 21 (methodische Grundlage).
- IDW S 6 (Sanierungskonzept).
- DStV-Praxisleitfaden Mandantenkommunikation.

## Workflow

### Phase 1 — Vereinfachte Cashflow-Struktur

```
CASHFLOW-UEBERSICHT (vereinfacht)
Mandant: [Firma]
Zeitraum: [Quartal X / 2026]

WAS WURDE LAUFEND VERDIENT?
+ Jahresueberschuss/-fehlbetrag [X]
+ Abschreibungen (kein Cash-Ausfluss) [X]
+/- Veraenderung Vorraete und Forderungen [X]
+/- Veraenderung Lieferantenverbindlichkeiten [X]
= LAUFENDER CASHFLOW [Y]

WAS WURDE INVESTIERT?
- Neue Maschinen, Fahrzeuge, IT [X]
- Beteiligungen [X]
+ Verkauf Alt-Anlagen [X]
= INVESTITIONS-CASHFLOW [-Z]

WIE HAT SICH DIE FINANZIERUNG VERAENDERT?
+ Neue Bankdarlehen [X]
- Tilgung Bankdarlehen [X]
- Ausschuettung Gesellschafter [X]
+ Privateinlage Gesellschafter [X]
= FINANZIERUNGS-CASHFLOW [+/- A]

NETTO-CASH-VERAENDERUNG [Y - Z +/- A]

BANK-/KASSE-BESTAND ANFANG [X]
BANK-/KASSE-BESTAND ENDE [X]
```

### Phase 2 — Erklaerung fuer den Mandanten

- "Laufender Cashflow" = Geld, das aus dem normalen Geschaeft hineinkommt (ohne Investitionen, ohne Bankgeschaefte).
- "Investitions-Cashflow" = Geld, das in neue Anlagen geflossen oder aus Verkauf alter zurueckgeflossen ist.
- "Finanzierungs-Cashflow" = Geld, das mit Bank und Gesellschaftern ausgetauscht wurde.
- Summe ergibt Veraenderung Bank-/Kasse-Bestand.

### Phase 3 — Visualisierung Wasserfall

- Wasserfall-Grafik: Startbestand Bank, dann farbig Plus/Minus, dann Endbestand.
- Mandant sieht visuell, woher das Geld kam und wohin es ging.
- DATEV Praesentation-Modul oder Excel-Wasserfalldiagramm.

### Phase 4 — Kennzahlen fuer Mandant

- Free Cashflow (FCF) = laufender Cashflow minus Investitions-Cashflow.
- Bedeutung: was bleibt nach Bedienung der laufenden Investitionen?
- FCF > 0 nachhaltig = Unternehmen kann Schulden tilgen und ausschuetten.
- FCF < 0 nachhaltig = Unternehmen finanziert Verzehr.

### Phase 5 — Beratungsempfehlung

- Bei negativem laufendem Cashflow: Working-Capital-Diskussion (Vorraete, Forderungen, Lieferanten).
- Bei negativem FCF ueber mehrere Perioden: Liquiditaets-Engpass droht; Liquiditaetsplanung erforderlich.
- Bei Sondereinmaleffekten (Anlagenverkauf): klar als einmalig kennzeichnen.

### Phase 6 — Mandantenkommunikation

- Cashflow-Uebersicht zusammen mit BWA versenden.
- Im Quartalsgespraech 5 Minuten erklaeren.
- Bei Krisensignalen: Sondergespraech mit Liquiditaetsplanung.

## Output

- 1-seitige Cashflow-Uebersicht laienverstaendlich.
- Wasserfall-Grafik.
- Erlaeuterungstext.

## Strategie und Praxis-Tipps

- Bei Familien-GmbH ist Cashflow oft wichtigeres Steuerungsmass als Bilanzgewinn — direkter Bezug zur Bankliquiditaet.
- "Gewinn vs. Cash"-Erklaerung: Gewinn kann positiv sein und Bank-Bestand sinken, wenn Forderungen steigen.
- Bei Bankgespraech: Cashflow-Uebersicht oft entscheidender als reine GuV.
- StBVV: Cashflow-Uebersicht als Bestandteil der Quartals-BWA oder als Zusatzauftrag.
- DATEV-Tipp: Der DATEV-Bilanzbericht beinhaltet eine automatisierte Kapitalflussrechnung (Klickpfad: Rechnungswesen → Bilanzbericht → Bestandteile waehlen → Kapitalflussrechnung). Die vereinfachte Mandantendarstellung erfolgt in Excel oder im DATEV-Praesentationsmodul manuell.

## Querverweise

- `stb-bwa-kapitalflussrechnung-iduk` — methodisch DRS 21.
- `stb-bwa-bewegungsbilanz-erstellen` — Bewegungsbilanz.
- `stb-liquiditaetsvorschau-3-6-12-monate` — Liquiditaetsplanung.
- `stb-bwa-mandantengespraech-uebergabe` — Quartalsgespraech.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 264, 297.
- DRS 21.
- IDW S 6.
- StBerG §§ 33, 57.
- DStV-Praxisleitfaden Mandantenkommunikation.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 6. `stb-bwa-erlaeuterungstext-mandant`

**Fokus:** Erlaeuterungstext unter der BWA für den Mandanten. Anwendungsfall Monats- oder Quartals-BWA mit kurzem fachlichem Begleittext der die wesentlichen Abweichungen und Risiken benennt. Aufbau Sachverhalt Erlaeuterung Ausblick Empfehlung. Output strukturierter Erlaeuterungstext 1 bis 2 Seiten als Anhang zur BWA Querverweis stb-bwa-mandantengespraech-uebergabe.

# Erlaeuterungstext zur BWA fuer den Mandanten

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erlaeuterungstext zur BWA fuer den Mandanten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die BWA ohne Erlaeuterung ist ein Zahlenfriedhof. Der Mandant — meist kein Bilanzbuchhalter — liest sie nicht oder falsch. Erst der Erlaeuterungstext macht aus Tabellen Steuerungsinformation. Der Steuerberater liefert auf 1-2 Seiten die wesentlichen Aussagen: Was ist passiert, welche Abweichungen sind erklaerungsbeduerftig, welche Handlungsempfehlungen ergeben sich? Ein guter Erlaeuterungstext erhoeht die Mandantenbindung und schuetzt vor Krisenuebersehen.

## Kaltstart-Rueckfragen

1. Welcher Mandantentyp — Solo-Unternehmer, Familien-GmbH, Mittelstand mit eigener Buchhaltung?
2. Wie tief soll der Text gehen — kurze Zusammenfassung (1/2 Seite) oder ausfuehrliche Analyse (2 Seiten)?
3. Welche Abweichungen sind wesentlich (Schwellenwert absolut/prozentual)?
4. Welche Sondereffekte muessen erklaert werden (Sonderzahlung, Sonderabschreibung, Einmalumsatz)?
5. Liegen Krisensignale vor (Eigenkapital negativ, SV-Rueckstaende, Umsatzeinbruch)?
6. Welche Empfehlungen sind angebracht (Investition, Personalkosten, Lieferanten)?
7. Adressat — GF (operativer Fokus), Aufsichtsrat (strategisch), Bank (Schuldendienst)?
8. Welcher Stil — kurz und sachlich, ausfuehrlich erklaerend, mit Grafiken?

## Rechtlicher Rahmen

### Primaernormen

**§ 33 StBerG** — Aufgabenkreis des StB; Erlaeuterung ist Bestandteil der Hilfeleistung in Steuersachen.

**§ 57 Abs. 1 StBerG** — Gewissenhaftigkeit; auch in der Mandantenkommunikation.

**§ 102 StaRUG** — Hinweis- und Warnpflicht bei Krisensignalen; im Erlaeuterungstext zu beruecksichtigen.

**§ 5 RDG** — Abgrenzung Rechts- vs. Wirtschaftsberatung; rein wirtschaftliche Erlaeuterung ist StB-Aufgabe.

### Standards

- IDW PS 480 (Erstellungsgrundsaetze).
- DStV-Praxisleitfaden Mandantenkommunikation.
- Berufsregeln BStBK § 13 Berufspflichten.

## Workflow

### Phase 1 — Schwellenwerte definieren

| Mandantengroesse | Absolute Schwelle | Prozentuale Schwelle |
|---|---|---|
| Kleinunternehmer < 500.000 EUR Umsatz | ab 500 EUR Abweichung | ab 10 Prozent |
| KMU 500.000-5 Mio EUR Umsatz | ab 2.000 EUR | ab 5 Prozent |
| Mittelstand 5-50 Mio EUR | ab 10.000 EUR | ab 3 Prozent |
| Grosser Mittelstand > 50 Mio EUR | ab 50.000 EUR | ab 2 Prozent |

### Phase 2 — Erlaeuterungs-Struktur

```
ERLAEUTERUNGEN ZUR BWA
Mandant: [Firma] GmbH
Zeitraum: [Monat / Quartal / kumuliert]
Stichtag: [Datum]

1. ZUSAMMENFASSUNG (3 Saetze)
[Wie war der Monat insgesamt? Auf einen Blick.]

2. UMSATZ UND ERTRAGSLAGE
[Umsatzentwicklung, Margenentwicklung, Sondereffekte.]

3. KOSTENSTRUKTUR
[Material- und Personalkostenquote, sonstige Aufwendungen.]

4. WESENTLICHE ABWEICHUNGEN
[Positionen ueber Schwellenwert, mit vermuteten Ursachen.]

5. RISIKEN / HINWEISE
[Liquiditaet, OPOS, Steuer- oder SV-Rueckstaende, Krisensignale.]

6. EMPFEHLUNGEN
[Konkrete Massnahmen oder Klaerungsbedarf.]

7. AUSBLICK
[Erwartung Jahresende oder naechstes Quartal.]
```

### Phase 3 — Sondereffekte erlaeutern

- Einmaleffekte (Anlagenverkauf, Versicherungsleistung): Hinweis auf "ohne Sondereffekt waere das Ergebnis ...".
- Sonderabschreibungen (§ 7b, § 7g EStG): kurz erklaeren, dass es sich um steuerliche Foerderung handelt.
- Sonderzahlungen Personal (Tantieme, Weihnachtsgeld): Hinweis auf Periodicitaet.

### Phase 4 — Risiko- und Hinweis-Block

- Bei OPOS-Listen mit ueberfaelligen Forderungen > 60 Tage: Hinweis auf Forderungsausfall-Risiko.
- Bei Steuerrueckstaenden: Hinweis auf Saeumniszuschlaege § 240 AO und ggf. Stundung § 222 AO.
- Bei SV-Rueckstaenden: dringender Hinweis (§ 266a StGB-Risiko fuer GF).
- Bei Eigenkapitalerosion: Verweis auf Pruefung § 19 InsO und stb-bwa-sus-bilanz-pruefung.

### Phase 5 — Empfehlungen formulieren

- Konkret und umsetzbar: "Bitte pruefen Sie Mahnungen fuer OP > 60 Tage" statt "OP-Management verbessern".
- Bei wesentlichen Massnahmen: Termin zur Besprechung anbieten.
- Keine Rechtsberatung (§ 5 RDG); bei Rechtsfragen Verweis auf Anwalt.

### Phase 6 — Freigabe und Versand

- 4-Augen-Prinzip: Sachbearbeiter schreibt, Berufstraeger gibt frei.
- Versand zusammen mit der BWA als PDF im verschluesselten Mandantenportal.

## Output

- Erlaeuterungstext 1-2 Seiten DIN A4 als PDF.
- Beigeheftet zur BWA.
- Mandantenakte mit Versanddatum dokumentiert.

## Strategie und Praxis-Tipps

- Erlaeuterungstexte standardisieren: Bausteinbibliothek pflegen, individualisieren je Mandant.
- Erlaeuterungstexte sind Haftungsschutz — bei spaeterem Streit kann der StB nachweisen, dass er hingewiesen hat.
- Nicht ausufernd: Mandant liest 2 Seiten, nicht 10. Was nicht in 2 Seiten passt, gehoert ins Quartalsgespraech.
- Wiederkehrende Posten in den Folgemonaten nur kurz erwaehnen, neuartige Effekte ausfuehrlich.
- StBVV: Erlaeuterungstext als Teil der BWA-Erstellung pauschalisiert; bei Sondererlaeuterung Zeithonorar.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-bwa-mandantengespraech-uebergabe` — Quartalsgespraech.
- `stb-bwa-zeitlicher-vergleich-jahresvergleich` — Abweichungsanalyse.
- `stb-bwa-sus-bilanz-pruefung` — Krisensignale.
- `stb-warnschreiben-krisensignale` — formelles Warnschreiben.

## Quellen und Updates

Stand: 05/2026.

- StBerG §§ 33, 57.
- StaRUG § 102.
- RDG § 5.
- AO §§ 222, 240.
- StGB § 266a.
- IDW PS 480.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 7. `stb-bwa-fehlerquellen-haeufig`

**Fokus:** Typische Fehlerquellen in der BWA. Anwendungsfall Qualitaetsprüfung BWA durch Berufstraeger interne Stichprobe Fehler in Periodenabgrenzung Buchungsfehler Bestandsveraenderung Lohnbuchungen. Methodik Checkliste Plausibilitaetsprüfung. Output Fehlerprotokoll Korrekturmassnahmen Schulungsbedarf Querverweis stb-bwa-aufbau-grundlagen.

# Typische BWA-Fehlerquellen und Plausibilitaetspruefung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Typische BWA-Fehlerquellen und Plausibilitaetspruefung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

BWA-Fehler sind nicht nur Schoenheitsmaengel — sie verfaelschen die Steuerung, koennen Krisensignale verdecken und im Streit mit dem Mandanten haftungsrelevant werden. Der Steuerberater muss systematisch die typischen Fehlerquellen abpruefen, bevor die BWA versendet wird. Dieser Skill ist Pflicht-Checkliste fuer Sachbearbeiter und Berufstraeger.

## Kaltstart-Rueckfragen

1. Wer hat die BWA erstellt — interner Sachbearbeiter, ausgelagerte Buchhaltung, automatisch?
2. Welches Buchhaltungs-System — DATEV, Addison, Sage, BuchhaltungsButler?
3. Sind Lohnbuchungen aus separatem Lohnprogramm integriert?
4. Wurde eine OPOS-Pflege vor BWA-Erstellung durchgefuehrt?
5. Liegt eine Zwischeninventur oder Warenroll vor?
6. Hat sich am Kontenrahmen oder an der BWA-Konfiguration etwas geaendert?
7. Welche Periode wird ausgewertet — Monat, Quartal, kumuliert?
8. Gibt es Sondereffekte, die separat ausgewiesen werden sollten?

## Rechtlicher Rahmen

### Primaernormen

**§ 238 HGB** — ordnungsgemaesse Buchfuehrung.

**§ 146 AO** — Zeitgerechtigkeit, Vollstaendigkeit, Richtigkeit.

**§ 257 HGB / § 147 AO** — Aufbewahrung.

**§ 33 StBerG** — StB-Aufgabenkreis; Sorgfaltspflicht.

**§ 57 StBerG** — Gewissenhaftigkeit.

### Standards

- BMF v. 28.11.2019 zu GoBD.
- IDW PS 480 (Erstellung).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Workflow

### Phase 1 — Konsistenzpruefung BWA gegen SuSa

- BWA-Endsalden Erfolgskonten = SuSa-Salden? (Differenz = Fehler.)
- BWA-Block-Summen = Kontensummen? (Konfigurationsfehler bei BWA-Form?)
- Bestaendsveraenderung in BWA = Anfangs-/Endbestand-Differenz aus SuSa?

### Phase 2 — Typische Fehlerklassen

| Fehlerklasse | Symptom | Ursache | Korrektur |
|---|---|---|---|
| Periodenabgrenzung fehlt | Sprunghafte Aufwendungen | RAP nicht gebucht | RAP nachbuchen |
| Bestandsveraenderung falsch | Wareneinsatz unplausibel | Inventur fehlt, Schaetzung schlecht | Zwischeninventur oder Warenroll |
| Lohnbuchungen verzoegert | Personalkosten zu niedrig | Lohnprogramm nicht synchron | Buchung aus Lohnprogramm uebernehmen |
| Verrechnungskonto offen | Saldo nicht null im Verrechnungs-/Geldtransit-Konto (z. B. SKR 03 1590/1599) | Buchung nicht zugeordnet | Klaerung mit Mandant; Kontonummer in DATEV-Kontenrahmen SKR 03/04 pruefen (DATEV-Kontenrahmen jaehrlich aktualisiert) |
| USt-Voranmeldung uneinheitlich | USt-Konto-Saldo passt nicht | USt-Schluessel falsch | Buchung pruefen |
| Sonderzahlungen Personal | Monatsausschlag Lohn | Tantieme einmalig | Im Erlaeuterungstext erwaehnen |
| Abschreibungen nicht aktualisiert | AfA monatlich konstant trotz Investition | Anlagenbuchhaltung nicht synchron | AfA aktualisieren |
| Skonti-Buchung | Erloese zu hoch | Skonti nicht erloesschmaelernd gebucht | Erloesschmaelerung im richtigen Erloeskontenbereich (vgl. DATEV-Kontenrahmen aktuelle Fassung, SKR 03 typisch 8730er bzw. SKR 04 4730er-Bereich) |
| Provisionserloese | DB falsch | Aufwand statt Erloesschmaelerung | Buchung umstellen |

### Phase 3 — Plausibilitaetsquoten

| Quote | Branchentypisch | Auffaellig wenn |
|---|---|---|
| Materialquote Industrie | 30-50 Prozent | < 25 oder > 60 Prozent |
| Materialquote Handel | 60-80 Prozent | < 50 oder > 90 Prozent |
| Personalkostenquote DL | 35-55 Prozent | < 25 oder > 70 Prozent |
| Mietquote | 3-10 Prozent | > 15 Prozent |
| Kfz-Kosten | 1-5 Prozent | > 10 Prozent (Privatanteil pruefen) |
| Versicherungen | 0,5-2 Prozent | > 3 Prozent (Doppelbuchung) |

### Phase 4 — Lohnbuchungs-Konsistenz

- Lohnsumme BWA muss mit dem Bruttolohn aus dem Lohnprogramm uebereinstimmen (Konten Loehne/Gehaelter SKR 03 4120/4130 bzw. SKR 04 6020/6030 — DATEV-Kontenrahmen aktuelle Fassung).
- SV-AG-Anteil-Konto-Saldo gegen den AG-Anteil aus der Lohnabrechnung pruefen (Daumenregel: ca. 20-21 Prozent vom Bruttolohn; massgebliche Beitragssaetze KV 14,6 Prozent allgemein (Stand 2025), RV 18,6 Prozent, PV 3,6 Prozent, AV 2,6 Prozent — aktuelle Werte aus der Sozialversicherungs-Rechengroessenverordnung abrufen).
- Berufsgenossenschaft monatlich anteilig gebucht (Konto SKR 03 4140 bzw. SKR 04 6140 — Konkretisierung im aktuellen DATEV-Kontenrahmen pruefen).
- Pauschalsteuer fuer Aushilfen ueber das jeweils passende Steueraufwandskonto buchen (z. B. SKR 03 4148 fuer Lohnsteuer 2 Prozent Pauschal — konkrete Kontonummer in der aktuellen DATEV-Kontenrahmen-Dokumentation nachschlagen).

### Phase 5 — Spezial-Pruefungen

- Bei GmbH: Geschaeftsfuehrer-Gehalt vollstaendig erfasst? Verdeckte Gewinnausschuettung-Risiko?
- Bei Holding: Erloese aus Beteiligung sauber erfasst (steuerfrei nach § 8b KStG)?
- Bei Personenunternehmen: Privatentnahmen nicht in BWA, sondern in Kapitalkonto.
- USt-konsistenz mit USt-Voranmeldung.

### Phase 6 — Fehlerprotokoll und Korrektur

- Fehlerliste mit Datum, Konto, Buchungssatz, Korrektur.
- Korrektur-Buchung mit Verweis im Buchungstext (z.B. "Korrektur BWA-Pruefung Q2/2026").
- Bei wesentlichen Fehlern: BWA neu erstellen und versenden.
- Mandant informieren bei Auswirkungen auf vorgelegte Reports.

## Output

- Fehlerprotokoll mit Korrekturmassnahmen.
- Korrigierte BWA.
- Ggf. Schulungsmemo fuer Sachbearbeiter.

## Strategie und Praxis-Tipps

- Standardisierte Pruefliste vor jedem BWA-Versand abarbeiten — auch bei Routine-Mandanten.
- 4-Augen-Prinzip: Sachbearbeiter prueft selbst, Berufstraeger stichprobenartig.
- Bei wiederholten Fehlern beim gleichen Sachbearbeiter: Schulung erforderlich.
- DATEV-Tipp: Auswertung "Konten mit ungewoehnlichem Saldo" als monatliche Pflichtpruefung.
- Honoraranknuepfung: Fehlerprotokoll als Teil der Qualitaetssicherung, kein Extra-Honorar.
- Bei Buchungsfehlern aus Vorperiode: Vorperiode korrigieren oder Erlaeuterungstext mit Hinweis.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-bwa-monatsabschluss-routine` — Monatsabschluss.
- `stb-susa-formfehler-pruefen` — SuSa-Fehler.
- `stb-bwa-sus-bilanz-pruefung` — Krisensignale.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 257.
- AO §§ 146, 147.
- StBerG §§ 33, 57.
- BMF v. 28.11.2019 zu GoBD.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026 | welle 6 | 3 Marker aufgeloest: 1 bestaetigt (SV-Beitragssaetze Stand 2025 eingesetzt), 2 ersetzt (DATEV-Kontonummern-Hinweise ohne Marker neu formuliert) -->

## 8. `stb-bwa-jahres-bwa-erstellen`

**Fokus:** Jahres-BWA als Ergaenzung zum Jahresabschluss. Anwendungsfall Jahresabschluss-Begleitung mit BWA für das Gesamtjahr inkl Vorjahresvergleich Mehrjahrestrend und Mandantenpraesentation. Methodik kumulierte BWA mit Korrekturen Sondereffekten Mehrjahresvergleich. Output Jahres-BWA als Praesentations-PDF.

# Jahres-BWA — Ergaenzung zum Jahresabschluss

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Jahres-BWA — Ergaenzung zum Jahresabschluss` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Der formale Jahresabschluss (Bilanz + GuV + Anhang + ggf. Lagebericht) ist juristisches Pflichtdokument, aber fuer den Mandanten oft schwer lesbar. Die Jahres-BWA ist die kommunikative Ergaenzung: kumulierter BWA-Block fuer das Gesamtjahr mit Vorjahresvergleich, Mehrjahres-Trend (3-5 Jahre), Kennzahlen-Zusammenfassung. Der Steuerberater praesentiert dem Mandanten die wirtschaftliche Entwicklung in einer Form, die der GF tatsaechlich liest und versteht.

## Kaltstart-Rueckfragen

1. Welcher Stichtag — Kalender-Geschaeftsjahr oder abweichendes Wirtschaftsjahr?
2. Liegen Daten der letzten 3-5 Jahre vor (Mehrjahres-Trend)?
3. Welche Korrekturen ergeben sich aus dem Jahresabschluss (vs. vorlaeufiger Quartals-BWA)?
4. Sondereffekte im Geschaeftsjahr (Sondertilgung, Sonderausschuettung, Sonder-AfA)?
5. Welche Kennzahlen sind im Vordergrund?
6. Welche Mandantenidentitaet (Logo, Farben)?
7. Verwendungszweck — Mandantengespraech, Gesellschafterversammlung, Bankgespraech?
8. Welche Erlaeuterungstiefe — knapp (2-3 Seiten) oder ausfuehrlich (10 Seiten)?

## Rechtlicher Rahmen

### Primaernormen

**§§ 242, 264 HGB** — Aufstellungspflicht Jahresabschluss.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 33 StBerG** — StB-Aufgabenkreis.

**§ 5b EStG** — E-Bilanz (Pflicht zur elektronischen Uebermittlung).

**§ 102 StaRUG** — Hinweispflicht bei Krisensignalen, im Jahresgespraech zu praesentieren.

### Standards

- IDW PS 480 — Erstellungsgrundsaetze.
- IDW PS 305 — Pruefung Risikofrueherkennung.
- DRS 17 — Lage-Bericht-Standards.
- DStV-Praxisleitfaden Mandantenkommunikation.

## Workflow

### Phase 1 — Datenbasis

- Jahresabschluss-Daten endgueltig (Bilanz, GuV, Anhang).
- Mehrjahres-Daten BWA (3-5 Jahre).
- Anlagenspiegel.
- OPOS-Saldenliste zum Stichtag.

### Phase 2 — Jahres-BWA aufbauen

```
JAHRES-BWA [Geschaeftsjahr]
Mandant: [Firma]
Stichtag: [Datum]

I. ERGEBNIS-UEBERBLICK
 Umsatzerloese [Jahr] [Vorjahr] [Abweichung in Prozent]
 Materialeinsatz ...
 Personalkosten ...
 Sonstige Aufwendungen ...
 Abschreibungen ...
 Betriebsergebnis ...
 Zinsergebnis ...
 Ergebnis vor Steuern ...
 Steuern ...
 Jahresergebnis ...

II. STRUKTURKENNZAHLEN
 Materialquote [Prozent]
 Personalquote [Prozent]
 Umsatzrentabilitaet [Prozent]
 EBITDA-Marge [Prozent]

III. LIQUIDITAETSKENNZAHLEN
 Liquiditaet 1./2./3. Grades [Prozent]
 Eigenkapitalquote [Prozent]
 Anlagendeckung II [Prozent]

IV. RENTABILITAET
 Eigenkapitalrendite [Prozent]
 Gesamtkapitalrendite [Prozent]

V. MEHRJAHRES-TREND (3-5 Jahre)
 Umsatzentwicklung als Liniendiagramm
 Ergebnisentwicklung
 Eigenkapital-Entwicklung
```

### Phase 3 — Sondereffekte separat

- Sonder-AfA § 7g EStG, § 7b EStG separat ausweisen.
- Anlagenverkauf, Sondertilgung, Sonderausschuettung mit kurzem Erlaeuterungsblock.
- "Bereinigtes Ergebnis" zusaetzlich darstellen.

### Phase 4 — Mehrjahres-Visualisierung

- Liniendiagramm Umsatz und Ergebnis ueber 5 Jahre.
- Balken Eigenkapital-Entwicklung.
- Heatmap Quartals-Ergebnisse (16 Quartale).

### Phase 5 — Kommentierung

- 2-Seiten-Erlaeuterung der wesentlichen Entwicklung.
- Vergleich Plan vs. Ist (falls Plan vorlag).
- Vergleich Branche (BBE-Daten falls verfuegbar).
- Ausblick auf Folgejahr.

### Phase 6 — Mandantenpraesentation

- Jahresgespraech mit Mandant: 1 Stunde mit Jahres-BWA-Praesentation.
- Im Anschluss schriftliche Bestaetigung der besprochenen Punkte.
- Bei Krisensignalen: § 102 StaRUG-Eskalation in den Bericht aufnehmen.

## Output

- Jahres-BWA als Praesentations-PDF (5-10 Seiten).
- Mehrjahres-Trend-Grafik.
- Erlaeuterungs- und Empfehlungstext.

## Strategie und Praxis-Tipps

- Jahres-BWA ist KEIN Ersatz fuer den formalen Jahresabschluss, sondern ergaenzende Kommunikations-Schicht.
- Der formale JA folgt § 325 HGB (Bundesanzeiger-Veroeffentlichung); die Jahres-BWA ist intern.
- Bei Gesellschafterversammlung: Jahres-BWA als Tischvorlage statt blanker Bilanz.
- Mehrjahres-Trend ist Standard bei mittelstaendischer Bilanzanalyse — 5 Jahre ist guter Kompromiss.
- StBVV: Jahres-BWA als Zusatzauftrag neben Jahresabschluss-Erstellung; ggf. Pauschal.
- DATEV-Tipp: Klickpfad fuer Mehrjahres-Vergleich: Rechnungswesen → Auswertungen → BWA → BWA-Form mit Vorjahresspalten waehlen, Jahresvergleich aktivieren.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-bwa-mandantenreport-monatlich` — Monatsreport.
- `stb-bwa-kennzahlen-rentabilitaet-eigenkapital` — Rentabilitaet.
- `stb-jahresgespraech-mandant-bwa-basis` — Jahresgespraech.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 242, 252, 264, 325.
- EStG § 5b.
- StBerG § 33.
- StaRUG § 102.
- IDW PS 480, IDW PS 305, DRS 17.
- DStV-Praxisleitfaden.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 9. `stb-bwa-kapitalflussrechnung-iduk`

**Fokus:** Kapitalflussrechnung nach indirekter Methode aus BWA und Bilanz. Anwendungsfall Jahresabschluss Bankreporting Sanierungskonzept Konzernabschluss. Methodik DRS 21 indirekte Ableitung aus Jahresueberschuss Mittelfluss laufende Geschäftstätigkeit Investitionstätigkeit Finanzierungstätigkeit. Output Kapitalflussrechnung als Standalone-Anhang.

# Kapitalflussrechnung nach DRS 21 indirekte Methode

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Kapitalflussrechnung nach DRS 21 indirekte Methode` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die Kapitalflussrechnung ist nach DRS 21 Pflichtbestandteil des Konzernabschlusses (§ 297 HGB) und freiwillig fuer Einzelabschluesse. Die indirekte Methode leitet den Cashflow aus dem Jahresueberschuss durch Eliminierung nicht-zahlungswirksamer Posten und Beruecksichtigung von Bilanzveraenderungen ab. Sie ist Bank-Standard, Bestandteil von Sanierungskonzepten nach IDW S 6 und Grundlage der Fortbestehensprognose nach § 19 InsO.

## Kaltstart-Rueckfragen

1. Welcher Anlass — Jahresabschluss Konzern, Sanierungskonzept, Bank-Reporting, freiwillige Erstellung?
2. Liegen Bilanz Anfang und Ende sowie BWA/GuV vor?
3. Welche Methode — indirekt (Standard) oder direkt (selten)?
4. Welche Konsolidierung — Einzel oder Konzern?
5. Sondereffekte (Anlagenverkauf, Sondertilgung, Kapitalerhoehung)?
6. Welcher Fonds — Liquide Mittel (Bank+Kasse), Finanzmittel weiter (incl. Wertpapiere)?
7. Welche Vorperiode wird vergleichend dargestellt?
8. Adressat — interne Steuerung, externe Veroeffentlichung, Sanierungsgutachten?

## Rechtlicher Rahmen

### Primaernormen

**§ 297 HGB** — Konzernabschluss; Kapitalflussrechnung verpflichtend.

**§ 264 HGB** — Aufstellungspflicht Einzelabschluss; Kapitalflussrechnung freiwillig.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 19 Abs. 2 InsO** — Fortbestehensprognose mit Liquiditaetsbetrachtung.

### Standards

- DRS 21 — Kapitalflussrechnung (gilt fuer Konzernabschluss; analog fuer Einzelabschluss).
- IDW S 6 — Sanierungskonzept; Cashflow-Rechnung Pflicht.
- IDW PS 305 — Risikofrueherkennung.
- IAS 7 — Cashflow Statements (bei internationaler Konzern-Reporting).

## Workflow

### Phase 1 — Datenbasis

- Bilanz Anfang und Ende (zwei Stichtage).
- GuV/BWA der Periode.
- Anlagenspiegel mit Zugaengen, Abgaengen, AfA.
- Eigenkapitalveraenderungsrechnung.
- Detail-Konten fuer ausserordentliche Posten.

### Phase 2 — Struktur DRS 21

```
KAPITALFLUSSRECHNUNG nach DRS 21 (indirekte Methode)

I. CASHFLOW AUS LAUFENDER GESCHAEFTSTAETIGKEIT
 Jahresueberschuss/Fehlbetrag [X]
 +/- Abschreibungen/Zuschreibungen Anlagevermoegen [X]
 +/- Veraenderung Rueckstellungen [X]
 +/- Sonstige nicht-zahlungswirksame Aufwendungen/Ertraege [X]
 +/- Veraenderung Vorraete [X]
 +/- Veraenderung Forderungen LuL [X]
 +/- Veraenderung sonstige Aktiva [X]
 +/- Veraenderung Verbindlichkeiten LuL [X]
 +/- Veraenderung sonstige Passiva [X]
 +/- Gezahlte/Erstattete Ertragsteuern [X]
 = Cashflow aus laufender Geschaeftstaetigkeit [X]

II. CASHFLOW AUS INVESTITIONSTAETIGKEIT
 - Auszahlungen fuer Investitionen Sachanlagen [X]
 - Auszahlungen fuer Investitionen immat. WG [X]
 - Auszahlungen fuer Investitionen Finanzanlagen [X]
 + Einzahlungen aus Abgang Sachanlagen [X]
 + Einzahlungen aus Abgang Finanzanlagen [X]
 = Cashflow aus Investitionstaetigkeit [X]

III. CASHFLOW AUS FINANZIERUNGSTAETIGKEIT
 + Einzahlungen aus Kapitalerhoehung [X]
 + Aufnahme Darlehen Kreditinstitute [X]
 - Tilgung Darlehen Kreditinstitute [X]
 - Ausschuettungen an Gesellschafter [X]
 = Cashflow aus Finanzierungstaetigkeit [X]

IV. VERAENDERUNG FINANZMITTELFONDS [X]
 + Finanzmittelfonds zu Beginn der Periode [X]
 = Finanzmittelfonds am Ende der Periode [X]
```

### Phase 3 — Ableitung Bewegungen

| Posten | Ermittlung |
|---|---|
| Veraenderung Vorraete | Vorraete Ende minus Vorraete Anfang (Aktiva-Erhoehung mindert Cashflow) |
| Veraenderung Forderungen | Forderungen Ende minus Anfang (Erhoehung mindert Cashflow) |
| Veraenderung Verbindlichkeiten | Verbindlichkeiten Ende minus Anfang (Erhoehung erhoeht Cashflow) |
| Abschreibungen | Aus Anlagenspiegel; nicht-zahlungswirksam → wird zurueckaddiert |
| Veraenderung Rueckstellungen | Rueckstellungen Ende minus Anfang; nicht-zahlungswirksam |

### Phase 4 — Sondereffekte

- Anlagenverkauf: Differenz Buchwert/Verkaufserloes als Sonderposten; Buchgewinn aus laufendem Cashflow herausrechnen.
- Sondertilgung: in Finanzierungstaetigkeit, nicht in laufender Geschaeftstaetigkeit.
- Kapitalerhoehung: in Finanzierungstaetigkeit, nicht Ergebnis.
- Ausschuettungen: in Finanzierungstaetigkeit, kein Aufwand.

### Phase 5 — Plausibilitaetspruefung

- Endsaldo Finanzmittelfonds = Bilanzposten "Liquide Mittel" zum Endstichtag? (Mussmatch sein.)
- Vergleich Vorjahr: aussergewoehnliche Veraenderungen kenntlich machen.
- Zusammenwirken mit Bewegungsbilanz pruefen.

### Phase 6 — Erlaeuterung und Versand

- Erlaeuterung wesentlicher Posten in Anhang (insb. Investitionstaetigkeit).
- Bei Bank-/Investor-Reporting Praesentationsformat (eine Seite plus Erlaeuterung).
- Sanierungskonzept IDW S 6: integriert mit Plan-Cashflow 24 Monate.

## Output

- Kapitalflussrechnung nach DRS 21 indirekte Methode.
- Erlaeuterung wesentlicher Veraenderungen.
- Anhang im Jahresabschluss (freiwillig im Einzelabschluss).

## Strategie und Praxis-Tipps

- Bei Mittelstand: Kapitalflussrechnung auf Wunsch des Bank-Partners als Standard.
- Konzernabschluss: Pflicht nach DRS 21 — nicht verhandelbar.
- Bei IFRS-orientierten Konzernen: parallel IAS 7 darstellen.
- Praxis-Tipp: Cashflow aus laufender Geschaeftstaetigkeit ist Indikator fuer organische Ertragskraft; deutlich unter Jahresueberschuss = Working-Capital-Problem.
- StBVV: Kapitalflussrechnung als separater Auftrag (Anhang Jahresabschluss).
- DATEV-Tipp: DATEV Konzernabschluss/Jahresabschluss-Modul mit Kapitalflussrechnung; bei Einzelabschluss manuelle Erstellung.

## Querverweise

- `stb-bwa-bewegungsbilanz-erstellen` — Vorstufe.
- `stb-bwa-cashflow-laienverstaendlich` — vereinfachte Darstellung.
- `stb-jahresabschluss-vorbereitung-stichtag` — Jahresabschluss.
- `stb-liquiditaetsvorschau-3-6-12-monate` — Plan-Cashflow.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 264, 297.
- DRS 21.
- IDW S 6, IDW PS 305.
- IAS 7 (international).
- InsO § 19.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
