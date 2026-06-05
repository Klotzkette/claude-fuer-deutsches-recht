---
name: steuer-bwa-kennzahlen-rentabilitaet-kontenrahmen-skr03
description: "Steuer BWA Kennzahlen Rentabilitaet Kontenrahmen Skr03: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Steuer BWA Kennzahlen Rentabilitaet Kontenrahmen Skr03

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **Steuer BWA Kennzahlen Rentabilitaet Kontenrahmen Skr03** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stb-bwa-kennzahlen-rentabilitaet-eigenkapital` | Rentabilitaetskennzahlen Eigenkapitalrendite Gesamtkapitalrendite ROI Umsatzrentabilitaet. Anwendungsfall Quartals- oder Jahresauswertung Beratungsgespraech Investor-Update. Methodik Berechnung Bewertung Branchenvergleich Praktische Aussage. Output Rentabilitaets-Kennzahlenblatt mit Erlaeuterung. |
| `stb-bwa-kontenrahmen-skr03-skr04` | Vergleich Kontenrahmen SKR 03 versus SKR 04 für BWA-Erstellung. Anwendungsfall Mandantenneuaufnahme oder Wechsel des Kontenrahmens Entscheidungsgrundlage Industrie Handel Dienstleistung. Aufbau Bilanz vs Prozess Gliederung GKV vs UKV. Output Empfehlung welcher Kontenrahmen Migrationsanleitung Querverweis stb-bwa-aufbau-grundlagen. |
| `stb-bwa-mandantenreport-monatlich` | Monatlicher Mandantenreport zusammenführend aus BWA SuSa OPOS Lohn Liquiditaet. Anwendungsfall standardisierter Monatsreport an Mandant per Mail oder Portal. Methodik 4-Seiten-Vorlage Cover BWA Kennzahlen Empfehlung. Output Mandantenreport als PDF Querverweis stb-routine-monatsabschluss-30-tage-zyklus. |
| `stb-bwa-statische-liquiditaet-kennzahlen` | Statische Liquiditaetskennzahlen Liquiditaet 1 2 3 Grades aus BWA und Bilanz. Anwendungsfall Quartalsauswertung Bankreporting Krisenfrueherkennung. Methodik Working Capital Aufstellung Anlagendeckung Kennzahlen. Output Liquiditaets-Kennzahlenblatt Bewertung Ampel. |
| `stb-bwa-vorlaeufiges-ergebnis-darstellung` | Darstellung vorlaeufiges Ergebnis in Quartals- und Halbjahres-BWA. Anwendungsfall unterjaehrige BWA mit Vorlaeufigkeitsvermerk Bestand-Schaetzung noch nicht abgeschlossene Periodenabgrenzung. Methodik klare Trennung gebuchte versus geschaetzte Posten Hinweis-Pflichten gegenüber Mandant. Output BWA mit Vorlaeufigkeitsvermerk Erlaeuterung. |
| `stb-bwa-zeitlicher-vergleich-jahresvergleich` | Zeitvergleich Vorjahr und Vormonat in der BWA. Anwendungsfall Monats- oder Quartals-BWA mit Gegenüberstellung Vorjahres-Periode kumulierter Jahresvergleich Abweichungs-Analyse Trendaussage. Methodik gleicher Zeitraum gleiches Geschäftsmodell Bereinigung Sondereffekte. Output Tabelle mit Soll Ist Vorjahr Abweichung absolut Prozent Erlaeuterungstext. |
| `stb-bwa-zeitvergleich-vorjahr-darstellung` | Zeitvergleich Vorjahr in der BWA grafisch und tabellarisch. Anwendungsfall optische Aufbereitung der Vorjahresvergleichsdaten für Mandantengespraech mit Liniendiagrammen Balkengrafik. Methodik Standard-Tabelle plus Visualisierung. Output BWA mit zusaetzlicher Grafik-Seite. |
| `stb-datentransfer-mandant-cloud-dsgvo` | Datentransfer Mandant zu Cloud DSGVO-Aspekte. Anwendungsfall Prüfung der DSGVO-Konformität beim Cloud-Datentransfer AVV Auftragsverarbeitung TOM technisch-organisatorische Massnahmen Drittlandtransfer. Methodik Prüfliste. Output DSGVO-Compliance-Dokument. |
| `stb-datev-bwa-modul-bedienen-tipps` | DATEV Kanzlei-Rechnungswesen BWA-Modul Bedienung. Anwendungsfall Erstellung BWA in DATEV Auswahl Form Konfiguration Periodenvergleich Branchenvergleich. Methodik Workflow-Tipps. Output BWA-konfiguriert. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **Steuer BWA Kennzahlen Rentabilitaet Kontenrahmen Skr03**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stb-bwa-kennzahlen-rentabilitaet-eigenkapital`

**Fokus:** Rentabilitaetskennzahlen Eigenkapitalrendite Gesamtkapitalrendite ROI Umsatzrentabilitaet. Anwendungsfall Quartals- oder Jahresauswertung Beratungsgespraech Investor-Update. Methodik Berechnung Bewertung Branchenvergleich Praktische Aussage. Output Rentabilitaets-Kennzahlenblatt mit Erlaeuterung.

# Rentabilitaetskennzahlen — Eigenkapital- Gesamtkapital-Rendite ROI

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rentabilitaetskennzahlen — Eigenkapital- Gesamtkapital-Rendite ROI` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Rentabilitaetskennzahlen zeigen, wie effizient ein Unternehmen Kapital einsetzt. Die wichtigsten: Eigenkapital-Rendite (Return on Equity), Gesamtkapital-Rendite (Return on Investment), Umsatzrentabilitaet (Return on Sales). Der Steuerberater nutzt sie fuer Mandantenbewertung, Investor-Update und Vergleich mit Marktstandards. Bei haftungsbeschraenkten Gesellschaften besonders relevant: ueber 5-Jahres-Durchschnitt nachhaltige Rentabilitaet ist Indikator fuer Going-concern (§ 252 HGB).

## Kaltstart-Rueckfragen

1. Welcher Berichtszeitraum — Jahresende, Quartal, kumuliert?
2. Welche Bezugsgroesse — gezeichnetes Kapital, bilanzielles Eigenkapital, durchschnittliches EK?
3. Sind kalkulatorische Positionen einzubeziehen (kalk. Unternehmerlohn, kalk. Zinsen)?
4. Welche Branchenvergleichsbasis?
5. Sondereffekte zu bereinigen (Anlagenverkauf, Sonderabschreibung)?
6. Welche Bezugsperiode fuer Durchschnitts-EK (Jahresanfang/Ende, Quartals-Mittel)?
7. Welche Steuerquote ist anzusetzen (bei mehrjaehrigen Vergleichen)?
8. Welcher Verwendungszweck — interne Steuerung, Investor-Update, Konzern-Reporting?

## Rechtlicher Rahmen

### Primaernormen

**§ 252 HGB** — Going-concern; Rentabilitaet ist Indikator.

**§ 33 StBerG** — StB-Aufgabenkreis.

**§ 91 Abs. 2 AktG / analog GmbH** — Risikofrueherkennung; ueber 5-Jahres-Trend ablesbar.

### Standards

- IDW S 1 — Grundsaetze zur Durchfuehrung von Unternehmensbewertungen (DCF-/Multiplikator-Verfahren).
- DRS 17 — Berichterstattung Lage-Bericht.
- BBE-Branchenkennzahlen.

## Workflow

### Phase 1 — Datenbasis

- Bilanz Anfang und Ende des Berichtszeitraums.
- GuV/BWA der Periode.
- Detail-Daten Eigenkapital (gezeichnet, Ruecklagen, Bilanzgewinn).
- Bei Personenunternehmen: Kapitalkonto-Bewegungen.

### Phase 2 — Berechnung Standard-Kennzahlen

```
EIGENKAPITALRENDITE vor Steuern:
 Jahresergebnis vor Steuern / Durchschnittliches Eigenkapital * 100

EIGENKAPITALRENDITE nach Steuern:
 Jahresueberschuss / Durchschnittliches Eigenkapital * 100

GESAMTKAPITALRENDITE (ROA, Return on Assets):
 (Jahresergebnis vor Steuern + Zinsaufwand) / Durchschnittliche Bilanzsumme * 100

RETURN ON INVESTMENT (ROI, DuPont):
 Umsatzrentabilitaet * Kapitalumschlag
 = (Gewinn/Umsatz) * (Umsatz/Bilanzsumme)

UMSATZRENTABILITAET:
 Jahresergebnis / Umsatz * 100

EBIT-MARGE:
 EBIT / Umsatz * 100

EBITDA-MARGE:
 EBITDA / Umsatz * 100
```

### Phase 3 — Schwellenwerte und Bewertung (Daumenregeln, branchenabhaengig)

| Kennzahl | Gruen (typisch) | Gelb (typisch) | Rot (typisch) |
|---|---|---|---|
| Eigenkapitalrendite (nach Steuern) | ueber ca. 15 Prozent | ca. 5-15 Prozent | unter ca. 5 Prozent |
| Gesamtkapitalrendite | ueber ca. 10 Prozent | ca. 5-10 Prozent | unter ca. 5 Prozent |
| Umsatzrentabilitaet | ueber ca. 8 Prozent | ca. 3-8 Prozent | unter ca. 3 Prozent |
| EBITDA-Marge | ueber ca. 15 Prozent | ca. 8-15 Prozent | unter ca. 8 Prozent |

Die Schwellenwerte sind Branchen-Daumenregeln und vor dem Mandantengespraech mit aktuellen BBE-Branchendaten abzugleichen. Industriebetriebe weisen typischerweise hoehere EK-Renditen aus; Handel hat oft geringe Umsatzrentabilitaet bei hohem Kapitalumschlag.

### Phase 4 — DuPont-Analyse

Zerlegung ROI in zwei Hebel:
- Umsatzrentabilitaet (Margenhebel)
- Kapitalumschlag (Effizienzhebel)

Beispiel: ROI 8 Prozent kann sich aus Umsatzrentabilitaet 4 Prozent x Kapitalumschlag 2 ergeben (Handel) oder Umsatzrentabilitaet 8 Prozent x Kapitalumschlag 1 (Industrie).

### Phase 5 — Mehrjahres-Trend

- 5-Jahres-Trend EK-Rendite ist Indikator fuer Going-concern.
- Bei nachhaltig fallender EK-Rendite: Krisenfrueherkennung.
- Bei stark schwankender Rendite: Volatilitaets-Risiko.

### Phase 6 — Erlaeuterung und Beratungsempfehlung

- Mandant in Branchenkontext einordnen.
- Bei unterdurchschnittlicher EK-Rendite: Massnahmen (Preisgestaltung, Kostenstruktur, Bilanzpolitik).
- Bei langfristig negativen Renditen: Hinweispflicht § 102 StaRUG aufgrund Eigenkapitalverzehr.

## Output

- Rentabilitaets-Kennzahlenblatt.
- 5-Jahres-Trend-Grafik.
- DuPont-Analyse.
- Erlaeuterungstext mit Branchenvergleich.

## Strategie und Praxis-Tipps

- Bei haftungsbeschraenkten Gesellschaften EK-Rendite vor und nach Steuern parallel ausweisen.
- Bei Personenunternehmen: EK-Rendite ohne kalkulatorischen Unternehmerlohn ist irrefuehrend.
- Bei Holding-Strukturen: bereinigte Renditen ohne reine Beteiligungs-Ergebnisse.
- Bei Konzern: ROCE (Return on Capital Employed) statt ROI.
- StBVV: Standardkennzahlen pauschaliert, Mehrjahres-Trend als Zusatzauftrag.
- DATEV-Tipp: Kennzahlen-Modul mit Standard-Formeln; individuelle Anpassung ueber Berater-Stammdaten.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-bwa-statische-liquiditaet-kennzahlen` — Liquiditaetskennzahlen.
- `stb-bwa-cashflow-laienverstaendlich` — Cashflow.
- `stb-bwa-branchenvergleich-bbe-datev` — Branchenvergleich.
- `stb-bwa-mandantenreport-monatlich` — Monatsreport.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 252, 264.
- StBerG § 33.
- StaRUG § 102.
- IDW S 1, DRS 17.
- BBE-Branchenkennzahlen.
- Coenenberg, Jahresabschluss und Jahresabschlussanalyse.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 ersetzt (Daumenregel-Hinweis ohne Marker neu formuliert) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `stb-bwa-kontenrahmen-skr03-skr04`

**Fokus:** Vergleich Kontenrahmen SKR 03 versus SKR 04 für BWA-Erstellung. Anwendungsfall Mandantenneuaufnahme oder Wechsel des Kontenrahmens Entscheidungsgrundlage Industrie Handel Dienstleistung. Aufbau Bilanz vs Prozess Gliederung GKV vs UKV. Output Empfehlung welcher Kontenrahmen Migrationsanleitung Querverweis stb-bwa-aufbau-grundlagen.

# Kontenrahmen SKR 03 vs SKR 04 — Wahl und Bedeutung fuer BWA

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Kontenrahmen SKR 03 vs SKR 04 — Wahl und Bedeutung fuer BWA` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

DATEV bietet zwei Standardkontenrahmen an. SKR 03 ist prozessorientiert (Wareneinkauf 3000er, Aufwand 4000er, Erloese 8000er). SKR 04 ist abschlussorientiert (Aktiva 0xxx-2xxx, Passiva 3xxx, Ertrag 4xxx, Aufwand 5xxx-7xxx). Die Wahl beeinflusst die BWA-Struktur, die Schnittstellen zur E-Bilanz und die Mandantenkommunikation. Bei Neuaufnahme eines Mandanten muss der Steuerberater bewusst waehlen; ein Wechsel des Kontenrahmens im laufenden Geschaeftsjahr ist nur ausnahmsweise sinnvoll.

## Kaltstart-Rueckfragen

1. Welche Mandantenstruktur — Industrie, Handel, Dienstleistung, Freiberufler, Holding?
2. Welche Rechtsform und Groessenklasse (§ 267 HGB) — Kleinst-, Klein-, mittelgrosse oder grosse Kapitalgesellschaft?
3. Welche Mandanten in der Kanzlei nutzen bereits welchen SKR? (Konsistenz im Kanzleibetrieb.)
4. Wird der Mandant bilanziert oder erfolgt EUER nach § 4 Abs. 3 EStG?
5. Welche Schnittstellen sind vorgesehen — DATEV Unternehmen Online, BuchhaltungsButler, sevDesk, Lexware?
6. Welches Lohnprogramm liefert Personalkosten-Buchungen — DATEV LODAS, Lohn und Gehalt, externer Provider?
7. Welche Berichts- und Reporting-Anforderungen — Konzernanforderung, internationale Eigentuemer mit UKV-Wunsch?
8. Plant der Mandant einen Branchenvergleich (DATEV Branchenbericht) — Vergleichbarkeit setzt Kontenrahmen voraus.

## Rechtlicher Rahmen

### Primaernormen

**§ 238 HGB** — Buchfuehrungspflicht; Kontenrahmen ist Wahlrecht, muss aber stetig sein (§ 252 Abs. 1 Nr. 6 HGB).

**§ 252 Abs. 1 Nr. 6 HGB** — Bewertungsstetigkeit; gilt analog fuer Kontenrahmen-Wechsel.

**§ 5b EStG** — E-Bilanz-Taxonomie; SKR 03 und SKR 04 sind beide kompatibel, aber die Brueckenkonten unterscheiden sich.

**§ 275 HGB** — Gliederung GuV; GKV nach § 275 Abs. 2 HGB / UKV nach § 275 Abs. 3 HGB. SKR 03 unterstuetzt traditionell GKV, SKR 04 ist offener fuer UKV.

### Verwaltungsanweisungen und Standards

- DATEV-Kontenrahmen-Dokumentation (jaehrliche Updates).
- IDW RS HFA 38 — Gliederungsgrundsaetze nach HGB.
- BMF v. 28.09.2011 (BStBl I 2011, 855) — E-Bilanz-Taxonomie; jaehrliche Anpassung durch BMF-Schreiben. Aktuelle Version ist die Taxonomie 6.9 (BMF-Schreiben April 2025, verpflichtend fuer WJ ab 01.01.2026); aktuelle Fassung ueber esteuer.de abrufbar.

## Workflow

### Phase 1 — Bestandsaufnahme

- Aktuelle Buchhaltung des Mandanten sichten — welcher Kontenrahmen wird derzeit genutzt? Bei Mandantenwechsel: Vorberaterkontenrahmen pruefen.
- Branche und Geschaeftsmodell erfassen; bei produzierendem Gewerbe SKR 03 ueblich, bei dienstleistenden GmbH zunehmend SKR 04.
- Anforderungen externer Stakeholder pruefen (Banken, Konzern-Mutter, Wirtschaftspruefer).

### Phase 2 — Entscheidung treffen

| Kriterium | SKR 03 | SKR 04 |
|---|---|---|
| Sortierung | Prozessorientiert (Beschaffung, Produktion, Absatz) | Abschlussorientiert (Bilanz und GuV nach HGB-Gliederung) |
| Branche | Industrie, Handwerk, traditioneller Handel | Dienstleistung, Holding, freie Berufe, kapitalmarkt-naher Mittelstand |
| GuV-Form | GKV (typisch) | UKV (typisch), aber auch GKV moeglich |
| E-Bilanz | Voll unterstuetzt | Voll unterstuetzt (Brueckenkonten differierend) |
| Internationale Vergleichbarkeit | Geringer | Hoeher (Naehe zu IFRS-Strukturen) |

### Phase 3 — Umsetzung

- Neue Mandanten: Kontenrahmen im DATEV-Stammdaten/Addison-Stammdaten festlegen; Bestaetigung im Mandantenstammblatt.
- Wechsel bestehender Mandanten: Nur zum Jahreswechsel, mit Eroeffnungsbilanz-Umbuchung. Wechsel waehrend des Jahres vermeidet § 252 Abs. 1 Nr. 6 HGB.
- Stammkontenliste mit individuellen Konten ergaenzen (Branchen-Sachkonten, Gesellschafterkonten).

### Phase 4 — Schnittstellen pruefen

- Lohnbuchhaltungs-Schnittstelle (DATEV-Buchungsbelege) — Kontenrahmen muss matchen.
- BWA-Konfiguration (Form 01, 11, 21) — die Standard-Forms sind fuer beide SKR vorbereitet, aber individualisierte Forms muessen angepasst werden.
- Branchenvergleich DATEV BBE — nur fuer Standard-SKR und Standard-Konten zuverlaessig.

### Phase 5 — Kommunikation an Mandanten

- Bei Wechsel: Mandant ueber Periode der Umstellung informieren; Auswirkungen auf BWA-Vorjahresvergleich erklaeren.
- Bei Erst-Einrichtung: kurze schriftliche Begruendung der Wahl in Mandantenakte.

## Output

- Empfehlung SKR 03 oder SKR 04 mit kurzer Begruendung (1-2 Absaetze).
- Konfigurierter Kontenrahmen in DATEV/Addison/Sage.
- Konsistenz-Pruefung BWA-Form passend zum Kontenrahmen.

## Strategie und Praxis-Tipps

- Mandanten mit Wachstumsabsicht und kapitalmarkt-naher Ausrichtung tendieren zu SKR 04; mittelstaendische Industriebetriebe bleiben oft bei SKR 03.
- Innerhalb der Kanzlei moeglichst konsistent — Mandantensachbearbeiter koennen sonst nicht effizient wechseln.
- DATEV-BBE-Branchenvergleich liefert die besten Daten fuer SKR 03 mit Standardkonten; bei SKR 04 ist die Datenbasis duenner.
- Honorar fuer Kontenrahmen-Wechsel separat im Zusatzauftrag aufnehmen (StBVV §§ 33, 35), nicht in der laufenden Buchhaltung.
- Bei Holding-Strukturen mit verschiedenen Tochtergesellschaften: gleicher Kontenrahmen in allen Einheiten erleichtert Konsolidierung.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — Standard-BWA-Struktur.
- `stb-jahresabschluss-elektronische-uebermittlung-ebilanz` — E-Bilanz-Taxonomie.
- `stb-susa-erstellen-grundlagen` — SuSa-Struktur abhaengig vom Kontenrahmen.
- `stb-datev-bwa-modul-bedienen-tipps` — DATEV-spezifische Konfiguration.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 252, 275.
- EStG § 5b.
- DATEV-Kontenrahmen SKR 03 und SKR 04 (Stand 2026).
- BMF v. 28.09.2011, BStBl I 2011, 855 (E-Bilanz-Grundsaetze); jaehrliche Taxonomie-Aktualisierung: aktuelle Version 6.9 (WJ ab 01.01.2026), abrufbar unter esteuer.de.
- IDW RS HFA 38.

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 2 bestaetigt (E-Bilanz Taxonomie 6.9 fuer WJ 2026 bestaetigt, esteuer.de-Quelle angegeben) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `stb-bwa-mandantenreport-monatlich`

**Fokus:** Monatlicher Mandantenreport zusammenführend aus BWA SuSa OPOS Lohn Liquiditaet. Anwendungsfall standardisierter Monatsreport an Mandant per Mail oder Portal. Methodik 4-Seiten-Vorlage Cover BWA Kennzahlen Empfehlung. Output Mandantenreport als PDF Querverweis stb-routine-monatsabschluss-30-tage-zyklus.

# Monatlicher Mandantenreport

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Monatlicher Mandantenreport` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Ein Mandantenreport ist die kuratierte Aufbereitung aller Auswertungen eines Monats: BWA, Kennzahlen, OPOS-Status, Lohnsumme, Liquiditaetsstand. Statt 5 einzelne PDFs erhaelt der Mandant ein 4-Seiten-Dokument: Cover mit Hauptaussagen, BWA-Block, Kennzahlen-Block, Empfehlungsblock. Der Report standardisiert die Kanzlei-Kommunikation, erhoeht die Mandantenbindung und reduziert Rueckfragen.

## Kaltstart-Rueckfragen

1. Welcher Mandant — Solo, KMU, Mittelstand?
2. Welche Detailtiefe — Standard (4 Seiten) oder erweitert (10 Seiten)?
3. Welche Kennzahlen sind dem Mandanten wichtig?
4. Welche Zusatzthemen einmonatlich (USt, Lohn, Investition)?
5. Liegt eine Mandanten-CI vor (Logo, Farbe)?
6. Welche Anrede (Sie/Du; gendergerecht)?
7. Welcher Versandkanal — E-Mail mit PDF-Anhang, DATEV Unternehmen Online, gedruckt per Post?
8. Welche Eskalation bei Krisensignalen (markiert, Anschreiben)?

## Rechtlicher Rahmen

### Primaernormen

**§ 33 StBerG** — StB-Aufgabenkreis.

**§ 57 StBerG** — Gewissenhaftigkeit.

**§ 102 StaRUG** — Hinweispflicht; im Monatsreport zu kommunizieren.

**§ 90 AO** — Mitwirkungspflicht Mandant; im Report Massnahmen-Plan.

**DSGVO Art. 32** — Sicherheit der Verarbeitung; verschluesselte Uebertragung.

### Standards

- DStV-Praxisleitfaden Mandantenkommunikation.
- BStBK Berufsrichtlinien.
- IDW PS 480.

## Workflow

### Phase 1 — Standard-Struktur

```
SEITE 1: COVER
- Mandantenlogo (links oben)
- Berichtsperiode (Monat / Jahr)
- 3 Hauptaussagen ("Auf einen Blick")
- Ampel-Status (Gruen/Gelb/Rot)
- Inhaltsverzeichnis

SEITE 2: BWA-BLOCK
- BWA-Hauptzahlen (5 Bloecke + Ergebnis)
- Vorjahresvergleich
- Kumulierter Jahresvergleich
- Erlaeuterung wesentliche Abweichungen

SEITE 3: KENNZAHLEN-BLOCK
- Liquiditaet 1./2./3. Grades
- EBIT-/EBITDA-Marge
- Eigenkapitalquote
- Branchenvergleich (falls verfuegbar)
- OPOS-Uebersicht (Top-Forderungen, Top-Verbindlichkeiten)

SEITE 4: EMPFEHLUNGSBLOCK
- 3-5 Handlungsempfehlungen
- Massnahmen-Tabelle mit Verantwortlich/Termin
- Eskalationen (Krisensignale, Hinweise)
- Anschluss-Termine (naechste Auswertung, Quartalsgespraech)
- Kontaktdaten Steuerberater
```

### Phase 2 — Datenintegration

- BWA aus DATEV/Addison ueber Export.
- Kennzahlen aus Kennzahlen-Modul.
- OPOS aus OP-Verwaltung.
- Lohn aus Lohnprogramm.
- Liquiditaet aus Liquiditaetsplanung.

### Phase 3 — Cover-Aussagen formulieren

- 3 Hauptaussagen pro Monat (z.B. "Umsatz plus 12 Prozent gegenueber Vorjahr", "Personalkostenquote stabil bei 38 Prozent", "Liquiditaet 1. Grades stabil bei 18 Prozent").
- Klar, kurz, nicht ueber-positiv (Vertrauensbildung durch Realismus).
- Bei Krisensignalen: Hauptaussage rot markiert.

### Phase 4 — Empfehlungsblock

- Konkret und umsetzbar.
- Mit Verantwortlichkeit (Mandant, StB, Bank).
- Mit Termin (z.B. "bis 15. Folgemonat klaeren").
- Keine Rechtsberatung (§ 5 RDG).

### Phase 5 — Layout und Versand

- Einheitliche Vorlage (PowerPoint oder Word-Template).
- Mandantenlogo eingebunden.
- PDF-Export verschluesselt.
- Versand via DATEV Unternehmen Online oder E-Mail mit Passwort.

### Phase 6 — Feedback und Iteration

- Monatlich Mandanten-Feedback einsammeln.
- Iteratives Verbessern des Reports.
- Standardisierung in der Kanzlei (Template-Library).

## Output

- 4-seitiger Mandantenreport als PDF.
- Versandprotokoll im Mandantenakte.
- Wiedervorlage fuer Folgemonat.

## Strategie und Praxis-Tipps

- Standardisierter Report ist Kanzlei-Differenzierungsmerkmal — viele Steuerberater versenden noch nackte BWA, der Report hebt sich ab.
- Template-Library pflegen: 3-5 Varianten je nach Mandantentyp (Solo, KMU, Mittelstand).
- Bei wesentlichen Aenderungen Mandant per Telefon kurz vorabinformieren.
- StBVV: Reportgestaltung Zusatzauftrag oder Pauschalvereinbarung; nicht in Standard-Buchfuehrungspauschale.
- DATEV-Tipp: DATEV Praesentation-Modul mit Vorlagen; bei Vollindividualisierung Excel/PowerPoint.
- Mandantenwunsch in Erstgespraech klaeren: Detailtiefe, Frequenz, Versandkanal.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-bwa-erlaeuterungstext-mandant` — Erlaeuterungstext.
- `stb-routine-monatsabschluss-30-tage-zyklus` — Monatsabschluss-Routine.
- `stb-bwa-mandantengespraech-uebergabe` — Quartalsgespraech.
- `stb-mandantenkommunikation-bwa-uebergabe-quartal` — Quartalsbesprechung.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- StBerG §§ 33, 57.
- StaRUG § 102.
- DSGVO Art. 32.
- DStV-Praxisleitfaden Mandantenkommunikation.
- IDW PS 480.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `stb-bwa-statische-liquiditaet-kennzahlen`

**Fokus:** Statische Liquiditaetskennzahlen Liquiditaet 1 2 3 Grades aus BWA und Bilanz. Anwendungsfall Quartalsauswertung Bankreporting Krisenfrueherkennung. Methodik Working Capital Aufstellung Anlagendeckung Kennzahlen. Output Liquiditaets-Kennzahlenblatt Bewertung Ampel.

# Statische Liquiditaetskennzahlen — 1. 2. 3. Grades

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Statische Liquiditaetskennzahlen — 1. 2. 3. Grades` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Statische Liquiditaetskennzahlen geben einen Schnappschuss der Zahlungsfaehigkeit zum Stichtag. Sie sind keine vollwertige Liquiditaetsplanung (dynamisch), aber Standardinstrument fuer Bank-Reporting, Quartals-Pruefung und erste Krisenfrueherkennung. Der Steuerberater berechnet sie aus Bilanz und SuSa und bewertet sie nach branchenueblichen Schwellenwerten. Bei Krisenmandanten ist die Liquiditaet 1. Grades unter 100 Prozent oft erster Indikator fuer § 17 InsO-Risiko.

## Kaltstart-Rueckfragen

1. Welche Stichtag — Monats-, Quartals- oder Jahresstichtag?
2. Liegt aktuelle SuSa und Bilanz vor?
3. Welche Kreditlinien (Kontokorrent, langfristig)?
4. Welche Verbindlichkeiten kurzfristig (< 1 Jahr) vs. langfristig?
5. Sind Forderungen werthaltig (keine grossen Einzelrisiken)?
6. Welche Vorraete (Umschlaghaeufigkeit)?
7. Welche Branche — branchentypische Schwellenwerte differieren?
8. Welcher Verwendungszweck — interne Steuerung, Bank, Sanierungsgutachten?

## Rechtlicher Rahmen

### Primaernormen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**§ 19 InsO** — Ueberschuldung mit Fortbestehensprognose.

**§ 252 HGB** — Going-concern.

**§ 102 StaRUG** — Hinweispflicht.

**§ 91 Abs. 2 AktG / analog GmbH** — Risikofrueherkennung.

### Standards

- IDW S 11 — Beurteilung Insolvenzeroeffnungsgruende.
- IDW S 6 — Sanierungskonzept.
- BBE-Branchenkennzahlen.

## Workflow

### Phase 1 — Datenbasis

- Bilanz zum Stichtag.
- SuSa mit Saldenstand kurzfristig vs. langfristig.
- OPOS-Listen Debitoren und Kreditoren.
- Kreditvertraege mit Linien-Limit und ausnutzungen.

### Phase 2 — Berechnung Kennzahlen

```
LIQUIDITAET 1. GRADES (Barliquiditaet, Cash Ratio):
 Liquide Mittel (Bank+Kasse) / kurzfristige Verbindlichkeiten

LIQUIDITAET 2. GRADES (einbeziehbare Liquiditaet, Quick Ratio):
 (Liquide Mittel + kurzfristige Forderungen) / kurzfristige Verbindlichkeiten

LIQUIDITAET 3. GRADES (gesamte kurzfristige Liquiditaet, Current Ratio):
 Umlaufvermoegen / kurzfristige Verbindlichkeiten

WORKING CAPITAL:
 Umlaufvermoegen minus kurzfristige Verbindlichkeiten
 (sollte positiv sein; bei negativ = kritisches Signal)

ANLAGENDECKUNG I:
 Eigenkapital / Anlagevermoegen

ANLAGENDECKUNG II:
 (Eigenkapital + langfristiges Fremdkapital) / Anlagevermoegen
 (sollte ueber 100 Prozent sein, sonst Fristenkongruenz verletzt)
```

### Phase 3 — Schwellenwerte und Ampel (typische Daumenregeln, branchenabhaengig)

| Kennzahl | Gruen (typisch) | Gelb (typisch) | Rot (typisch) |
|---|---|---|---|
| Liquiditaet 1. Grades | ueber ca. 20 Prozent | ca. 10-20 Prozent | unter ca. 10 Prozent |
| Liquiditaet 2. Grades | ueber ca. 100 Prozent | ca. 80-100 Prozent | unter ca. 80 Prozent |
| Liquiditaet 3. Grades | ueber ca. 200 Prozent | ca. 120-200 Prozent | unter ca. 120 Prozent |
| Working Capital | Positiv mit Reserve | Knapp positiv | Negativ |
| Anlagendeckung II | ueber ca. 110 Prozent | ca. 100-110 Prozent | unter ca. 100 Prozent |

Die Schwellenwerte sind Branchenrichtwerte und vor dem Mandantengespraech mit aktuellen BBE-Daten abzugleichen. Handel weist oft niedrigere Liquiditaet 3. Grades wegen schnellem Lagerumschlag aus.

### Phase 4 — Interpretation

- Liquiditaet 1. Grades < 10 Prozent: Achtung — bei ueber 3 Wochen anhaltend, § 17 InsO-Pruefung erforderlich.
- Working Capital negativ: Umlaufvermoegen finanziert teils Anlagevermoegen — Fristenkongruenz verletzt, akute Liquiditaets-Spannung.
- Anlagendeckung II < 100 Prozent: Anlagevermoegen wird teils mit kurzfristigem Kapital finanziert — strukturelles Risiko.
- Kreditlinien einbeziehen: ungenutzte Linien erhoehen "verfuegbare Mittel" der Liquiditaet 1. Grades.

### Phase 5 — Beratungsempfehlung

- Bei roter Ampel Liquiditaet 1. Grades: dynamische Liquiditaetsplanung (3-Wochen) sofort.
- Bei roter Ampel Anlagendeckung II: Umfinanzierung pruefen (kurzfristige in langfristige Schulden umwidmen).
- Bei negativem Working Capital: Sondergespraech mit Bank.

### Phase 6 — Reporting

- Liquiditaets-Kennzahlenblatt im Quartalsbericht.
- Bei Krisensignalen Querverweis stb-liquiditaetsvorschau-3wochen und stb-bwa-sus-bilanz-pruefung.

## Output

- Liquiditaets-Kennzahlenblatt mit Ampel.
- Erlaeuterungstext.
- Empfehlungen zur Liquiditaetssteuerung.

## Strategie und Praxis-Tipps

- Statische Kennzahlen sind Schnappschuss — bei Krisensignalen IMMER dynamische Liquiditaetsplanung ergaenzen.
- Bei Banken: Liquiditaet 1. Grades und Working Capital sind Standard-Pruefungsfelder.
- Kreditlinien-Ausnutzung mit dokumentieren — "verfuegbare Reserve" ist Steuerungsgroesse.
- StBVV: Standardkennzahlen pauschaliert, dynamische Liquiditaetsplanung als Zusatzauftrag.
- DATEV-Tipp: Kennzahlen-Modul mit Standard-Liquiditaetsformeln; bei individuellen Branchen-Schwellen Anpassung.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-bwa-kennzahlen-rentabilitaet-eigenkapital` — Rentabilitaet.
- `stb-liquiditaetsvorschau-3-6-12-monate` — dynamische Liquiditaetsplanung.
- `stb-liquiditaetsvorschau-3wochen` — § 17 InsO-Pruefung.
- `stb-bwa-sus-bilanz-pruefung` — Krisensignale.

## Quellen und Updates

Stand: 05/2026.

- InsO §§ 17, 19.
- HGB §§ 252, 268.
- StaRUG § 102.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- IDW S 6, IDW S 11.
- BBE-Branchenkennzahlen.

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 1 bestaetigt (BGH IX ZR 123/04, BGHZ 163, 134 bestaetigt), 1 ersetzt (Daumenregel-Hinweis ohne Marker neu formuliert) -->

## 5. `stb-bwa-vorlaeufiges-ergebnis-darstellung`

**Fokus:** Darstellung vorlaeufiges Ergebnis in Quartals- und Halbjahres-BWA. Anwendungsfall unterjaehrige BWA mit Vorlaeufigkeitsvermerk Bestand-Schaetzung noch nicht abgeschlossene Periodenabgrenzung. Methodik klare Trennung gebuchte versus geschaetzte Posten Hinweis-Pflichten gegenüber Mandant. Output BWA mit Vorlaeufigkeitsvermerk Erlaeuterung.

# Vorlaeufiges Ergebnis in der unterjaehrigen BWA

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Vorlaeufiges Ergebnis in der unterjaehrigen BWA` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Unterjaehrige BWA sind per Definition vorlaeufig: Periodenabgrenzungen sind noch nicht final, Bestaende werden geschaetzt, Abschreibungen ggf. erst zum Jahresende angepasst. Der Steuerberater muss diese Vorlaeufigkeit explizit kennzeichnen, damit der Mandant das Ergebnis nicht ueberbewertet. Anders als der Jahresabschluss enthaelt die BWA Schaetzwerte, die spaeter korrigiert werden. Ein Quartals- oder Halbjahres-Ergebnis braucht einen Vorlaeufigkeitsvermerk, eine Aufstellung der Schaetzungen und ggf. ein Confidence Interval.

## Kaltstart-Rueckfragen

1. Welche Periode wird ausgewertet — Quartal, Halbjahr, kumuliert seit Jahresbeginn?
2. Welche Posten sind geschaetzt (Bestand, Rueckstellungen, Abschreibungen)?
3. Sind alle Eingangsrechnungen erfasst, oder gibt es eine "fehlende Rechnungs"-Schaetzung?
4. Liegt eine Zwischeninventur vor (insbesondere bei Industrie und Handel)?
5. Sind Personalkosten vollstaendig erfasst (laufender Monat und Sonderzahlungen)?
6. Welcher Verwendungszweck — interne Steuerung, Bankgespraech, Investor-Update?
7. Welche Eskalation bei Krisensignalen — direkte Information an GF oder Aufsichtsrat?
8. Ist eine Hochrechnung auf Jahresende gewuenscht (Annualisierung)?

## Rechtlicher Rahmen

### Primaernormen

**§ 252 Abs. 1 Nr. 4 HGB** — Vorsichtsprinzip; auch unterjaehrig zu beachten.

**§ 252 Abs. 1 Nr. 5 HGB** — Periodenabgrenzung.

**§ 252 Abs. 1 Nr. 6 HGB** — Bewertungsstetigkeit.

**§ 240 HGB** — Inventar; jaehrliche Bestandsaufnahme.

**§ 33 StBerG** — Erstellungsauftrag des Steuerberaters; Vorlaeufigkeitshinweis ist Standard.

### Standards

- IDW PS 480 — Erstellung von Jahresabschluessen (Vorlaeufigkeitsvermerke analog).
- IDW S 7 — Begutachtungen (analog Hinweise auf Vorlaeufigkeit).
- BMF v. 28.11.2019 zu GoBD.

## Workflow

### Phase 1 — Schaetzungspositionen identifizieren

| Position | Schaetzungsgrundlage | Genauigkeit |
|---|---|---|
| Warenbestand | Letzte Inventur + Roll auf Basis Umsatz/Wareneinsatz | Mittel |
| Unfertige Erzeugnisse | Auftragsstatus, Stundenanteile | Niedrig bis mittel |
| Urlaubsrueckstellung | 1/12 der Jahresrueckstellung | Hoch |
| Tantieme/Gratifikation | Anteilig zum Jahresziel | Niedrig |
| Berufsgenossenschaft | Vorjahresbescheid + Lohnsumme | Mittel |
| Abschreibungen | 1/12 Jahresabschreibung aus Anlagenverzeichnis | Hoch |
| Vorsteuer-/USt-Abgrenzung | Aus USt-Voranmeldung | Hoch |
| Drohende Verluste | Einzelfallschaetzung | Niedrig |

### Phase 2 — Schaetzungsdokumentation

- Jede Schaetzungsposition mit Methode, Quelle und Zeitstempel dokumentieren.
- Bei wesentlichen Schaetzungen (Bestand) interne Stichprobe (Auswertung Lagerverwaltung).
- Schaetzungen muessen periodisch konsistent sein (keine Glaettung "nach Bedarf").

### Phase 3 — BWA-Ausgabe mit Vorlaeufigkeitsvermerk

Standard-Vermerk:

```
HINWEIS: Diese BWA gibt das vorlaeufige Ergebnis fuer den Zeitraum
[von - bis] wieder. Folgende Posten enthalten Schaetzwerte:
- Warenbestand: gerollt aus Inventur [Datum] auf Basis Wareneinsatz.
- Urlaubsrueckstellung: anteilig 1/12 der Jahresrueckstellung.
- Abschreibungen: 1/12 der Jahresabschreibung aus Anlagenverzeichnis.
Diese Schaetzungen werden zum Jahresabschluss durch tatsaechliche
Werte ersetzt; das vorlaeufige Ergebnis kann sich entsprechend
veraendern. Die BWA ist nicht testiert.

Erstellt: [Datum]
Bearbeiter: [Sachbearbeiter]
Freigegeben: [Berufstraeger]
```

### Phase 4 — Hochrechnung Jahresende

- Annualisierung: Quartals-Ist mal 4, mit Saisonbereinigung.
- Bandbreite angeben: optimistisches/realistisches/pessimistisches Szenario.
- Vorsicht bei Saisonbranchen — lineare Hochrechnung verzerrt.

### Phase 5 — Kommunikation an Mandant

- BWA mit explizitem Vorlaeufigkeitsvermerk an Mandant.
- Bei Bankgespraech: Mandant darauf hinweisen, dass BWA nicht testiert ist; ggf. Sondergutachten WP/StB beauftragen.
- Bei Investor-Update: Vorlaeufigkeitsvermerk in Praesentation einarbeiten.

### Phase 6 — Krisen-Eskalation

- Bei drohenden Verlusten oder negativem Eigenkapital: Eskalation an Berufstraeger.
- Querverweis stb-bwa-sus-bilanz-pruefung und § 102 StaRUG-Pruefung.

## Output

- Vorlaeufige BWA mit klar gekennzeichnetem Vermerk.
- Schaetzungsliste in Mandantenakte.
- Hochrechnung Jahresende mit Szenarien.

## Strategie und Praxis-Tipps

- Vorlaeufigkeitsvermerk ist nicht nur Haftungsschutz, sondern auch Mandanten-Erziehung — der Mandant lernt, dass das Quartal nicht der Jahresabschluss ist.
- Bei wesentlichen Schaetzungen Stichprobenbericht: kurze Beschreibung, woher die Zahl kommt.
- Bei wiederkehrenden Bankgespraechen Vorlaeufigkeit nicht jedes Mal neu erklaeren — einmaliger Schulungstermin mit dem Bankberater.
- Honoraranknuepfung: Quartals-BWA als Zusatzauftrag StBVV § 35 oder Pauschalvereinbarung.
- Bei wesentlichen Korrekturen zwischen Quartal und Jahresabschluss Mandanten proaktiv informieren — Vertrauensschutz.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-bwa-zeitlicher-vergleich-jahresvergleich` — Vorjahresvergleich.
- `stb-jahresabschluss-vorbereitung-stichtag` — Jahresabschluss.
- `stb-bwa-fehlerquellen-haeufig` — Fehlerquellen.
- `stb-bwa-sus-bilanz-pruefung` — Krisensignale.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 240, 252, 257.
- AO § 147.
- StBerG § 33.
- IDW PS 480, IDW S 7.
- BMF v. 28.11.2019 zu GoBD.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 6. `stb-bwa-zeitlicher-vergleich-jahresvergleich`

**Fokus:** Zeitvergleich Vorjahr und Vormonat in der BWA. Anwendungsfall Monats- oder Quartals-BWA mit Gegenüberstellung Vorjahres-Periode kumulierter Jahresvergleich Abweichungs-Analyse Trendaussage. Methodik gleicher Zeitraum gleiches Geschäftsmodell Bereinigung Sondereffekte. Output Tabelle mit Soll Ist Vorjahr Abweichung absolut Prozent Erlaeuterungstext.

# Zeitlicher Vergleich in der BWA — Vorjahr und Vormonat

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zeitlicher Vergleich in der BWA — Vorjahr und Vormonat` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Eine BWA ohne zeitlichen Vergleich ist eine reine Momentaufnahme ohne Steuerungswert. Erst durch die Gegenueberstellung mit der Vorjahres-Periode (Monat oder Quartal) und dem kumulierten Jahresvergleich entsteht Trendaussage. Der Steuerberater muss dabei methodisch sauber vorgehen: Sondereffekte herausrechnen, Periodenabgrenzungen vergleichbar machen und qualifizierte Aussagen ueber Abweichungen treffen.

## Kaltstart-Rueckfragen

1. Welche Auswertungsform — Monats-BWA mit Vorjahresvergleich oder kumulierter Vergleich seit Jahresbeginn?
2. Hat das Unternehmen Sondereffekte im Vorjahr (Einmal-Erloese, Sonderabschreibungen, Sonder-Tantieme)?
3. Aenderungen im Geschaeftsmodell, Sortiment, Vertriebsgebiet seit Vorjahr?
4. Hat sich die Buchhaltungs-Routine geaendert (Periodenabgrenzung, Bestand-Schaetzung)?
5. Liegen Vorjahres-BWA-Daten konsistent vor, oder wurde der Vorberater gewechselt?
6. Aussagekraft des Vergleichs: Ist gleicher Saisonzyklus vorhanden (z.B. Tourismus)?
7. Mandantenwunsch — Tabelle oder zusaetzlich Grafik?
8. Reportingzweck — interne Steuerung, Bankberichterstattung, Investoren-Update?

## Rechtlicher Rahmen

### Primaernormen

**§ 252 Abs. 1 Nr. 6 HGB** — Bewertungsstetigkeit; zeitlicher Vergleich setzt konsistente Methoden voraus.

**§ 265 Abs. 2 HGB** — Vergleichbarkeit der Vorjahreszahlen im Jahresabschluss; analog fuer unterjaehrige BWA.

**§ 238 HGB** — Buchfuehrungspflicht; Grundlage fuer den Datenbestand.

**§ 5 EStG / § 4 EStG** — Massgeblichkeit fuer Vergleichszeitraeume.

### Verwaltungsanweisungen

- BMF v. 28.11.2019 zu GoBD — laufende Buchfuehrung.
- IDW PS 250 — Berichterstattung ueber Pruefergebnisse (sinngemaess auf BWA-Berichterstattung anwendbar).

## Workflow

### Phase 1 — Datenbasis sichern

- Vorjahres-BWA-Daten aus Vorperiode bestaendig in DATEV/Addison verfuegbar machen.
- Bei Mandantenuebernahme: Vorjahres-BWA des Vorberaters anfordern (Mandantenakte).
- Kontenrahmen-Aenderungen pruefen (SKR 03 → SKR 04 erfordert Brueckenposten).

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

Vorsicht: Im obigen Beispiel ist `13,6` nur in der Tabelle akzeptabel; in der Frontmatter-Description waere das verboten (Cowork-Validator-Bug). In Erlaeuterungstexten ausserhalb der Tabelle "13 Prozent" oder "rund 14 Prozent" formulieren.

### Phase 4 — Abweichungsanalyse

- Absolute Abweichung in EUR: ab welchem Schwellenwert ist Klaerung noetig? Mandantenabhaengig (kleine Mandanten ab 500 EUR, grosse ab 5.000 EUR).
- Prozentuale Abweichung: ab 10-20 Prozent ist Erlaeuterung im BWA-Text Pflicht.
- Kreuzpruefung: Umsatzplus von 13 Prozent rechtfertigt Materialeinsatzplus von 7 Prozent nicht — Materialquote sinkt, Marge waechst. Ursache klaeren (Preiserhoehung, Mix-Effekt, Einkaufsvorteile)?

### Phase 5 — Kumuliert seit Jahresbeginn

- Jahresblock (Year-to-Date) parallel zum Monatsblock.
- Vergleichszeitraum identisch wie Mandantenkalender (Wirtschaftsjahr vom 1. Januar bis 31. Dezember; bei abweichendem Wirtschaftsjahr entsprechend anpassen).
- Trend: Erwartung Jahresende hochrechnen (Annualisierung), aber mit Vorsicht (Saisonzyklus beachten).

### Phase 6 — Erlaeuterungstext und Mandantenkommunikation

- 3-5 Saetze unter der BWA: wichtigste Abweichungen benennen, Ursachen vermuten oder klaerend fragen.
- Bei Krisensignalen (Umsatz minus 20 Prozent, Eigenkapitalerosion): Eskalation an Berufstraeger und ggf. Querverweis stb-bwa-sus-bilanz-pruefung.

## Output

- BWA mit Monats-Vorjahresvergleich und kumuliertem Jahresvergleich.
- Bereinigte Vergleichszahlen bei Sondereffekten.
- Erlaeuterungstext mit Abweichungsanalyse.

## Strategie und Praxis-Tipps

- Bei Mandantenuebernahme klare Erwartung kommunizieren: Vorjahresvergleich ist erst sinnvoll, wenn ein volles Wirtschaftsjahr Daten vorliegt.
- Saisonale Branchen (Tourismus, Bau, Einzelhandel) immer mit Vorjahres-Monatsvergleich, nicht Vormonatsvergleich.
- Bei abweichendem Wirtschaftsjahr Mandant darauf hinweisen, dass Standard-BWA-Form ggf. anzupassen ist.
- DATEV BWA 11 (Bewegungs-BWA) gibt Vormonatsvergleich detailliert aus; DATEV BWA 01 mit Vorjahresvergleich konfigurieren.
- Honorar fuer aufwendige Sondereffekt-Bereinigung als Zusatzauftrag StBVV § 35 / Zeithonorar.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Struktur.
- `stb-bwa-soll-ist-vergleich` — Plan-Ist-Vergleich.
- `stb-bwa-erlaeuterungstext-mandant` — Erlaeuterungstexte.
- `stb-bwa-branchenvergleich-bbe-datev` — Branchenvergleich.
- `stb-bwa-mandantengespraech-uebergabe` — Mandantengespraech.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 252, 265.
- EStG §§ 4, 5, 7g.
- BMF v. 28.11.2019, BStBl I 2019, 1269 (GoBD).
- DATEV BWA-Form 01 mit Vorjahresvergleich (Standard).
- IDW PS 250 (sinngemaess).


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 7. `stb-bwa-zeitvergleich-vorjahr-darstellung`

**Fokus:** Zeitvergleich Vorjahr in der BWA grafisch und tabellarisch. Anwendungsfall optische Aufbereitung der Vorjahresvergleichsdaten für Mandantengespraech mit Liniendiagrammen Balkengrafik. Methodik Standard-Tabelle plus Visualisierung. Output BWA mit zusaetzlicher Grafik-Seite.

# Grafische Aufbereitung des Vorjahresvergleichs in der BWA

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Grafische Aufbereitung des Vorjahresvergleichs in der BWA` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Tabellen sind sachlich richtig, aber visuell muehsam. Fuer das Mandantengespraech und das Bankreporting empfiehlt sich die grafische Aufbereitung des Vorjahresvergleichs: Liniendiagramme fuer Umsatz und Ergebnis ueber 12 Monate, Balkengrafik fuer kumulierte Werte, Heatmap fuer monatliche Abweichungen. Der Steuerberater nutzt die DATEV-/Addison-Grafik-Module oder exportiert die Daten in eine Excel-/PowerPoint-Vorlage.

## Kaltstart-Rueckfragen

1. Welcher Verwendungszweck — internes Quartalsgespraech, Bankgespraech, Investor-Update?
2. Welche Detailtiefe — nur Umsatz/Ergebnis oder auch Kosten-Komponenten?
3. Welche Zeitachse — letzte 12 Monate rollierend, Kalenderjahr, mehrere Jahre?
4. Welche Grafik-Form — Liniendiagramm, Balken, kombiniert, Heatmap?
5. Welche Tool-Wahl — DATEV-Grafik-Modul, Excel, PowerPoint, Power BI?
6. Welches Layout — A4-Format, A3 fuer Praesentation, Bildschirm-Praesentation?
7. Welche Hervorhebungen — Trendlinien, gleitende Durchschnitte, Krisen-Markierungen?
8. Welche Mandanten-Identitaet (Logo, Farben)?

## Rechtlicher Rahmen

### Primaernormen

**§ 33 StBerG** — Aufgabenkreis StB.

**§ 57 StBerG** — Gewissenhaftigkeit.

**§ 102 StaRUG** — Hinweispflicht (auch grafisch erkennbare Krisensignale).

### Standards

- DATEV-Grafik-Modul (DATEV Praesentation).
- BBE Branchengrafiken.
- IDW PS 480 (Erstellung).

## Workflow

### Phase 1 — Datenexport

- BWA-Daten aus DATEV/Addison in Excel exportieren.
- 12 Monate Vorjahr und 12 Monate Berichtsjahr.
- Kumulierte Werte separat berechnen.

### Phase 2 — Grafik-Auswahl

| Information | Geeignete Grafik |
|---|---|
| Umsatzentwicklung Monatsverlauf | Liniendiagramm 12 Monate Vorjahr/Jahr |
| Kumulierter Vergleich | Flaechendiagramm oder Balken |
| Kostenstruktur (Material/Personal/Sonstige) | Stapelbalken oder Tortendiagramm |
| Abweichungen vs. Vorjahr je Monat | Balken mit Plus/Minus-Differenz |
| Branchen-Heatmap | Heatmap mit Farbcodierung |
| Trend-Glaettung | Gleitender Durchschnitt 3-/12-Monate |

### Phase 3 — Visualisierung Beispiele

**Beispiel 1 — Umsatzverlauf Liniendiagramm:**
- X-Achse: Monate Januar bis Dezember.
- Y-Achse: Umsatzhoehe in EUR.
- Zwei Linien: Vorjahres-Umsatz (gestrichelt) und Berichtsjahr (durchgezogen).
- Markierung Sondereffekte.

**Beispiel 2 — Kumulierter Vergleich:**
- X-Achse: Monate (kumuliert YTD).
- Y-Achse: Kumulierte Position.
- Vergleich Vorjahres-Kumuliert vs. Berichtsjahr-Kumuliert.
- Anstieg/Abfall direkt ablesbar.

**Beispiel 3 — Kostenstruktur Stapelbalken:**
- 12 Monatsbalken nebeneinander.
- Jeder Balken: Material/Personal/Sonstige/Abschreibung gestapelt.
- Vorjahresvergleich darunter.

### Phase 4 — Erlaeuterungstext zur Grafik

- Jede Grafik mit 2-3 Saetzen erlaeutern.
- Auf wesentliche Auffaelligkeiten hinweisen.
- Klar formulieren: "Im Marz Berichtsjahr lag der Umsatz rund 15 Prozent ueber Vorjahresmonat, im April rund 8 Prozent unter Vorjahresmonat."

### Phase 5 — Layout-Standardisierung

- Mandantenlogo oben links, Stichtag oben rechts.
- Maximal 2 Grafiken pro A4-Seite.
- Standard-Schriftgroesse 10pt mit Achsenbeschriftung 8pt.
- Farbpalette einheitlich (z.B. Blau fuer Vorjahr, Grun fuer Berichtsjahr, Rot fuer Sondereffekte).

### Phase 6 — Versand

- BWA mit Grafik-Anhang (PDF).
- Bei Praesentation: PowerPoint mit gleichen Grafiken.
- Mandantenakte dokumentieren.

## Output

- BWA-Grafik-Anhang mit 3-5 Standardgrafiken.
- Erlaeuterungstext zu jeder Grafik.
- Praesentationsvorlage fuer Quartalsgespraech.

## Strategie und Praxis-Tipps

- Grafische Aufbereitung ist Mandantenbindungs-Instrument; mit Abstand wirkungsvoller als reine Tabelle.
- Standardisierung in der Kanzlei — gleiches Layout, gleiche Farbcodierung fuer alle Mandanten.
- Achtung: Skalen-Manipulation vermeiden (Y-Achse nicht bei Null, sondern bei realer Bandbreite — gilt als unredlich nur bei boswilliger Verzerrung).
- Bei Krisensignalen Grafik mit roter Markierung; visuelle Verstaerkung der Warnung.
- StBVV: Standard-Grafik pauschaliert, Sonderformate mit Zeithonorar.
- Datenschutz: bei Cloud-basierten Tools (Power BI Online) DSGVO-konforme Konfiguration.

## Querverweise

- `stb-bwa-zeitlicher-vergleich-jahresvergleich` — Zahlentabelle.
- `stb-bwa-mandantenreport-monatlich` — Monatsreport.
- `stb-bwa-mandantengespraech-uebergabe` — Quartalsgespraech.
- `stb-bwa-branchenvergleich-bbe-datev` — Branchenvergleich.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung BWA/SuSa/Bilanz.

## Quellen und Updates

Stand: 05/2026.

- StBerG §§ 33, 57.
- DATEV Praesentations-Modul.
- IDW PS 480.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 8. `stb-datentransfer-mandant-cloud-dsgvo`

**Fokus:** Datentransfer Mandant zu Cloud DSGVO-Aspekte. Anwendungsfall Prüfung der DSGVO-Konformität beim Cloud-Datentransfer AVV Auftragsverarbeitung TOM technisch-organisatorische Massnahmen Drittlandtransfer. Methodik Prüfliste. Output DSGVO-Compliance-Dokument.

# Datentransfer Mandant-Cloud — DSGVO-Aspekte

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Datentransfer Mandant-Cloud — DSGVO-Aspekte` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Beim Datentransfer zwischen Mandant, StB und Cloud-Dienstleistern muss DSGVO-Konformitaet sichergestellt sein. Wesentliche Aspekte: AVV nach Art. 28 DSGVO mit jedem Auftragsverarbeiter, TOM (technisch-organisatorische Massnahmen), Drittlandtransfer-Pruefung (USA-Server problematisch), Einhaltung der Daten-Minimierung. Bei Verstoss: Bussgeld bis 4 Prozent Jahresumsatz.

## Kaltstart-Rueckfragen

1. Welche Cloud-Dienstleister sind im Einsatz (DATEV, BuchhaltungsButler, sevDesk, Microsoft, Google)?
2. Liegen AVV mit allen Auftragsverarbeitern vor?
3. Welche Daten werden gespeichert (Mandantendaten, Lohndaten, Mitarbeiterdaten)?
4. Welcher Server-Standort (EU, Drittland)?
5. Welche TOM-Massnahmen?
6. Welche Mandantenkommunikation Datenschutzhinweise?
7. Welche Sicherheits-Vorfaelle in der Vergangenheit?
8. Welche Berufsverschwiegenheit (§ 57 StBerG)?

## Rechtlicher Rahmen

### Primaernormen

**DSGVO Art. 5** — Grundsaetze.

**DSGVO Art. 28** — Auftragsverarbeiter.

**DSGVO Art. 32** — Sicherheit der Verarbeitung.

**DSGVO Art. 44-50** — Drittlandtransfer.

**§ 57 Abs. 1 StBerG** — Verschwiegenheit.

**§ 203 StGB** — Verletzung Berufsgeheimnis.

### Verwaltungsanweisungen

- Aufsichtsbehoerden DSK-Beschluesse.
- Schrems II-Urteil EuGH (Drittlandtransfer USA).

## Workflow

### Phase 1 — Auftragsverarbeitungs-Inventar

| Dienstleister | Datenart | EU-Server | AVV |
|---|---|---|---|
| DATEV | Mandantendaten | Ja | Ja |
| Microsoft 365 | E-Mail, Office | Teilweise EU | Ja, mit Standardvertragsklauseln |
| Google Workspace | E-Mail, Storage | EU/USA | Ja |
| BuchhaltungsButler | Mandanten-Buchhaltung | EU | Ja |
| Zoom | Videokonferenz | Mix | Ja |

### Phase 2 — AVV-Pruefung Art. 28 DSGVO

- Schriftlicher AVV-Vertrag.
- Inhalte: Verarbeitungstaetigkeit, Daten-Kategorien, TOM-Bestimmungen, Sub-Verarbeiter, Pflichten beidseitig.
- Aktualitaet pruefen.

### Phase 3 — Drittlandtransfer Pruefung

- USA-Server: nach Schrems II zusaetzliche Massnahmen erforderlich.
- Standardvertragsklauseln (SCC).
- Transfer Impact Assessment (TIA).
- Bei sensiblen Daten (Mandantenidentifizier, Gesundheitsdaten): EU-Server bevorzugen.

### Phase 4 — TOM-Massnahmen

| Bereich | Massnahmen |
|---|---|
| Vertraulichkeit | Verschluesselung Transport (TLS), Verschluesselung at-rest |
| Integritaet | Hashverfahren, Audit-Logs |
| Verfuegbarkeit | Backup, Redundanz |
| Belastbarkeit | Disaster Recovery |
| Wiederherstellbarkeit | Backup-Restore |
| Pruefverfahren | Regelmaessige Audits |
| Pseudonymisierung | wo moeglich |

### Phase 5 — Mandantenkommunikation

- Datenschutzhinweise gem. Art. 13 DSGVO bei Mandatsaufnahme.
- Information bei wesentlichen Aenderungen.
- Mandantenanfragen Art. 15 DSGVO beantworten.

### Phase 6 — Datenschutz-Folgenabschaetzung (DSFA)

- Bei umfangreicher Verarbeitung personenbezogener Daten.
- Bei systematischer Profilbildung.
- Bei besonderen Datenkategorien.

## Output

- DSGVO-Compliance-Dokument.
- AVV-Mappe.
- TOM-Massnahmen-Liste.

## Strategie und Praxis-Tipps

- Die Berufsverschwiegenheit nach § 57 StBerG ist durch § 203 Abs. 1 Nr. 3 StGB strafrechtlich abgesichert; die Einbeziehung externer Dienstleister (Cloud-Anbieter) erfordert nach § 203 Abs. 3, 4 StGB die schriftliche Verpflichtung des Dienstleisters auf die Schweigepflicht — entsprechende Klauseln im AVV pruefen.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- DSGVO-Bussgelder bis 20 Mio. EUR oder 4 % des weltweiten Jahresumsatzes (Art. 83 Abs. 5 DSGVO) — Compliance unverzichtbar.
- Jaehrliche DSGVO-Pruefung im Kanzleiteam (Verzeichnis Verarbeitungstaetigkeiten, AVV-Mappe, TOM-Liste aktualisieren).
- StBVV: DSGVO-Compliance-Beratung fuer Mandanten als separater Auftrag nach § 13 StBVV (Beratung) oder als Bestandteil der Buchfuehrungspauschale.

## Querverweise

- `stb-online-portal-datev-mandantenshop` — DUO.
- `stb-buchhaltungsbutler-mandantencloud` — Cloud.
- `stb-ki-tools-im-stb-betrieb-grenzen-berufsrecht` — KI-Tools.

## Quellen und Updates

Stand: 05/2026.

- DSGVO Art. 5, 13, 28, 32, 44-50.
- StBerG § 57.
- StGB § 203.
- Schrems II-Urteil EuGH.
- DSK-Beschluesse.

## 9. `stb-datev-bwa-modul-bedienen-tipps`

**Fokus:** DATEV Kanzlei-Rechnungswesen BWA-Modul Bedienung. Anwendungsfall Erstellung BWA in DATEV Auswahl Form Konfiguration Periodenvergleich Branchenvergleich. Methodik Workflow-Tipps. Output BWA-konfiguriert.

# DATEV Kanzlei-Rechnungswesen BWA-Modul — Bedienung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DATEV Kanzlei-Rechnungswesen BWA-Modul — Bedienung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

DATEV Kanzlei-Rechnungswesen ist die zentrale Steuerberater-Software fuer Buchfuehrung, BWA, SuSa, Jahresabschluss. Das BWA-Modul bietet zahlreiche Standardforms (BWA 01, 11, 21), Branchenanpassungen und individuelle Konfigurations-Moeglichkeiten ueber Berater-Stammdaten. Der Steuerberater nutzt Standardformen, passt sie bei Bedarf an und integriert Branchenvergleich (BBE).

## Kaltstart-Rueckfragen

1. Welche DATEV-Version (jaehrliche Updates)?
2. Welche BWA-Form ist aktuell konfiguriert?
3. Welche Branche?
4. Welche Auswertungsfrequenz?
5. Welche individuellen Anpassungen vorgenommen?
6. Welche Berater-Sicht-Konfiguration?
7. Welche Mandanten-Sicht (Mandantensicht-Filter)?
8. Welche Exportformate (PDF, Excel)?

## Workflow

### Phase 1 — Standardformen kennen

| Form | Verwendung |
|---|---|
| BWA 01 | Standard-BWA fuer 90 Prozent aller Mandanten |
| BWA 11 | Bewegungs-BWA mit detailliertem Vormonatsvergleich |
| BWA 21 | Branchen-BWA mit Branchenvergleich |
| BWA 31 | Kostenstellen-BWA |
| BWA 41 | Liquiditaets-BWA |
| BWA 51 | Statistische BWA |

### Phase 2 — Konfiguration

- Berater-Stammdaten: Mandantengruppen und BWA-Stammvorlagen zentral pflegen (typischer Programmpfad `Bestand → Berater-Stammdaten → BWA-Konfiguration`; exakter Pfad in aktueller DATEV-Programmversion ggf. abweichend).
- Mandantenstammdaten: BWA-Form-Zuordnung pro Mandant unter `Mandantenstammdaten → Auswertungen → BWA`.
- Periodenvergleich: Vorjahresdaten automatisch bei vorhandener Historie; Planwerte ueber `Auswertungen → Plan-Erfassung`.

### Phase 3 — Branchenvergleich

- Branchenschluessel (WZ-Code 2008) im Mandantenstamm hinterlegen.
- BBE-Branchen-Abonnement der DATEV nutzen (Aktualisierung jaehrlich).
- BWA 21 zeigt direkt Branchenmittel; Branchenbericht separat als PDF/Excel.

### Phase 4 — Individualisierung

- Eigene BWA-Form ueber Berater-Stammdaten anlegen (Kopie einer Standard-Form als Ausgangsbasis empfohlen).
- Konten-Zuordnung manuell definieren — pro Konto bzw. Kontenintervall.
- Spalten frei konfigurieren: Plan, Ist, Vorjahr, Vorjahres-kumuliert, Abweichung absolut/prozentual.

### Phase 5 — Ausgabe

- PDF-Export mit Mandanten-Briefkopf ueber das Druckmodul.
- Excel-Export fuer Detailauswertung (Pivot-fhaeig).
- DUO-Versand: BWA wird direkt in das DUO-Postfach des Mandanten gestellt (`Auswertungen → BWA → Versand an DUO`).

### Phase 6 — Updates

- Jaehrliche DATEV-Programm-Updates zum 1. Januar (LSt/SV-Tabellen, USt-Saetze, AfA-Tabellen, neue gesetzliche Pflichtmeldungen).
- Bei groesseren Reformen unterjaehrige Updates (Wachstumschancengesetz, eRechnung-Verfahren).
- Berater-Funktion Updates manuell pruefen, da individuelle Formen nicht automatisch migriert werden.

## Output

- Konfigurierte DATEV-BWA.
- Standard-Vorlagen.
- Branchen-Vergleich.

## Strategie und Praxis-Tipps

- BWA 21 fuer alle BWA-Mandanten mit Branchen-Wunsch.
- Individuelle BWA nur bei besonderem Bedarf — Standard-Form deckt 90 Prozent ab.
- Berater-Stammdaten zentral pflegen — vereinheitlicht Kanzleibetrieb.
- DATEV-Schulungen empfehlenswert (DATEV-Akademie).

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA.
- `stb-bwa-branchenvergleich-bbe-datev` — Branchenvergleich.
- `stb-bwa-kontenrahmen-skr03-skr04` — Kontenrahmen.

## Quellen und Updates

Stand: 05/2026.

- DATEV Kanzlei-Rechnungswesen Bedienungs-Dokumentation (aktuelle Version pruefen).
- DATEV-Programm-Updates jaehrlich (Stand 01.01.) sowie unterjaehrige Reform-Updates.
- AO § 146 (Update-Pflicht der Buchfuehrungsprogramme).
- Verifikations-Hinweis: konkrete Programmpfade und Form-Nummern ggf. abweichend in aktueller DATEV-Version.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
