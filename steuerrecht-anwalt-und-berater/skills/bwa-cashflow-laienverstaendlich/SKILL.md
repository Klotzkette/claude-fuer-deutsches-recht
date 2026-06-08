---
name: bwa-cashflow-laienverstaendlich
description: "Cashflow-Darstellung für Mandant in laienverstaendlicher Form. Anwendungsfall Quartals-BWA mit vereinfachter Cashflow-Aufstellung für GF ohne Finanz-Hintergrund. Methodik einfache Mittelfluss-Tabelle Brutto-Netto-Cashflow Trennung zahlungswirksam vs nicht-zahlungswirksam. Output 1-seitige Cashflow-Übersicht."
---

# Cashflow laienverstaendlich darstellen

## Fachlicher Anker

- **Normen:** § 6a, § 33, § 57.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Kernsachverhalt

Die DRS-21-Kapitalflussrechnung ist methodisch korrekt, aber für den nicht-finanzaffinen Mandanten zu komplex. Fuer das Mandantengespraech braucht es eine einfachere Darstellung: Wie viel Cash kam laufend rein? Was wurde investiert? Was wurde an Bank/Gesellschafter zurueckgezahlt? Was bleibt am Monatsende? Der Steuerberater erstellt eine 1-seitige Brutto-Cashflow-Uebersicht, die dem Mandanten die Geldfluesse zeigt — ohne ihn zu ueberfordern.

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

### Phase 2 — Erklaerung für den Mandanten

- "Laufender Cashflow" = Geld, das aus dem normalen Geschaeft hineinkommt (ohne Investitionen, ohne Bankgeschaefte).
- "Investitions-Cashflow" = Geld, das in neue Anlagen geflossen oder aus Verkauf alter zurueckgeflossen ist.
- "Finanzierungs-Cashflow" = Geld, das mit Bank und Gesellschaftern ausgetauscht wurde.
- Summe ergibt Veraenderung Bank-/Kasse-Bestand.

### Phase 3 — Visualisierung Wasserfall

- Wasserfall-Grafik: Startbestand Bank, dann farbig Plus/Minus, dann Endbestand.
- Mandant sieht visuell, woher das Geld kam und wohin es ging.
- DATEV Praesentation-Modul oder Excel-Wasserfalldiagramm.

### Phase 4 — Kennzahlen für Mandant

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

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 8 AO (Wohnsitz, Aufenthalt)
- §§ 33, 34 AO (Steuerpflichtiger, gesetzliche Vertreter)
- § 42 AO (Gestaltungsmissbrauch)
- §§ 169-171 AO (Festsetzungsverjährung)
- §§ 233a, 235 AO (Verzinsung, Hinterziehungszinsen)
- § 370 AO (Steuerhinterziehung)
- §§ 153, 371 AO (Berichtigungserklärung, Selbstanzeige)
- §§ 15, 32a EStG (Einkünfte aus Gewerbebetrieb, Tarif)
- § 8 KStG, § 7 GewStG (Einkommen, Gewerbeertrag)
- §§ 1, 15 UStG (Steuerbare Umsätze, Vorsteuerabzug)

### Leitentscheidungen

- BFH I R 36/18 (Hinzurechnungsbesteuerung AStG)
- BFH XI R 11/22 (Reverse-Charge-Verfahren)
- BFH IX R 49/13 (Liebhaberei vs. Einkunftserzielungsabsicht)
- BVerfG 2 BvL 1/03 (Steuerfreistellung Existenzminimum)
- EuGH C-280/10 (Vorsteuerabzug bei wirtschaftlicher Tätigkeit)

### Anwendung im Skill

- Beraterhaftung gegen Mandantenpflicht (§§ 153, 154 AO) klar trennen; Selbstanzeige nach § 371 AO ist eine Strafnorm, kein Steueroptimierungs-Tool.
- Festsetzungsverjaehrung nach §§ 169-171 AO im Zweifel zugunsten des Steuerpflichtigen; Hemmung durch Aussenpruefung beachten.
- Bei Gestaltungsmissbrauch § 42 AO immer alternative Wirtschaftsgruende dokumentieren.
