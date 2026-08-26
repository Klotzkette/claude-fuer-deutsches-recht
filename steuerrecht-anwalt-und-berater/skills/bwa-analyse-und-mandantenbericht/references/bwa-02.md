# BWA-Analyse und Mandantenbericht: BWA, Kennzahlen und Mandantenbericht

Diese Datei wird nur geladen, wenn der konkrete Vorgang in diese Fallgruppe fällt.

## Betriebsuebersicht erstellen — Ergaenzung zur BWA

Auswahlsignal: Wenn es um Betriebsuebersicht erstellen — Ergaenzung zur BWA in Steuerrecht – Steuerberater und Anwälte geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen.

### Betriebsuebersicht erstellen — Ergaenzung zur BWA

#### Fachlicher Anker

- **Normen:** § 6a, § 238 HGB, § 252 HGB.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

#### Kernsachverhalt

Die Standard-BWA fasst Konten in funf Bloecken zusammen. Für detaillierte Analysen reicht das nicht — der Mandant will wissen, woraus sich "sonstige betriebliche Aufwendungen" zusammensetzen oder welche Erloeskonten beigetragen haben. Die Betriebsuebersicht ist die Kontenliste mit Salden, Vorjahresvergleich und ggf. Plan-Werten. Sie ergaenzt die BWA und ist Standard bei groesseren Mandanten und im Steuerberater-Buero zur internen Analyse.

#### Kaltstart-Rueckfragen

1. Welche Detailtiefe — alle Konten oder nur die wesentlichen?
2. Mandantenwunsch Layout — Konten in der Reihenfolge des Kontenrahmens oder strukturiert nach Funktionsbereichen?
3. Welche Vergleichsspalten — Vormonat, Vorjahres-Monat, kumulierter Jahresvergleich, Plan?
4. Welche Sortierung — Saldenhoehe, Kontenrahmen, alphabetisch?
5. Welche Schwellenwerte — Konten mit Saldo unter X EUR ausblenden?
6. Liegen Sachkontenbezeichnungen aktuell vor (Stammdaten aktualisieren)?
7. Wird die Übersicht intern oder extern (Mandant, Bank, Investor) genutzt?
8. Welche Konten müssen vertraulich gefuehrt werden (z.B. GF-Bezuege)?

#### Rechtlicher Rahmen

##### Primaernormen

**§ 238 HGB** — Buchfuehrungspflicht.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 33 StBerG** — Aufgabenkreis StB.

##### Standards

- DATEV BWA-Form 21 (Branchen-BWA) und Kontenuebersicht.
- IDW PS 480 (Erstellungsgrundsaetze).

#### Workflow

##### Phase 1 — Konfigurations-Wahl

| Form | Verwendung |
|---|---|
| Reine Kontenliste | Interne Stichprobe, Sachbearbeiter-Prüfung |
| Strukturierte Betriebsuebersicht | Mandant, Berufstraeger-Prüfung |
| Branchen-Betriebsuebersicht | Branchen-Vergleich (BBE) |
| Erweiterte Betriebsuebersicht | Bank-/Investor-Reporting |

##### Phase 2 — Aufbau strukturierte Betriebsuebersicht

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

##### Phase 3 — Vergleichsspalten

| Spalte | Inhalt | Quelle |
|---|---|---|
| Monat aktuell | Ist-Saldo der Periode | BWA-Buchungen |
| Monat Vorjahres-Periode | Saldo gleicher Monat Vorjahr | Vorjahres-DATEV |
| Kumuliert Jahr | Saldo seit Jahresbeginn | Year-to-Date |
| Kumuliert Vorjahres-Jahr | Vorjahres-YTD | Vorjahres-DATEV |
| Plan-Wert | Aus Stammdaten | Plan-Eingabe |
| Abweichung absolut | Ist minus Vorjahr / Plan | Berechnung |
| Abweichung in Prozent | absolute Abweichung / Vergleichswert | Berechnung |

##### Phase 4 — Filter und Sortierung

- Konten ohne Saldo ausblenden (Default).
- Konten mit Saldo < 100 EUR ggf. ausblenden (oder als "Sonstige" zusammenfassen).
- Sortierung nach Kontenrahmen (SKR 03 oder SKR 04).
- Innerhalb der Bloecke nach Saldenhoehe absteigend (optional).

##### Phase 5 — Vertrauliche Konten

- GF-Bezuege, Tantiemen: Mandantenwunsch beachten (oft separat behandeln).
- Privatentnahmen Einzelunternehmer: nicht in BWA, sondern Kapitalkonto.
- Sondergesellschafterdarlehen: separat ausweisen.

##### Phase 6 — Versand und Ablage

- Als PDF gemeinsam mit BWA.
- Ablage in Mandantenakte mit Versanddatum.
- Mandanten-Portal-Download möglich.

#### Strategie und Praxis-Tipps

- Betriebsuebersicht ist Pflicht bei Mittelstand und Konzern-Reporting.
- Bei KMU: optional, mandantenabhaengig anbieten.
- Vertrauliche Konten klar markieren oder in geschuetzten Bereich auslagern.
- Bei Wechsel des Kontenrahmens Vorjahresvergleich nicht möglich ohne Brueckenposten.
- DATEV-Tipp: Standard-Betriebsuebersicht 21 oder individuelle Konfiguration über Berater-Stammdaten.
- StBVV: Standardform pauschaliert, individuelle Konfiguration als Zeithonorar.

#### Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 252.
- StBerG § 33.
- DATEV BWA-Form 21, Kontenuebersicht.
- IDW PS 480.
## Bewegungsbilanz aus BWA und SuSa

Auswahlsignal: Wenn es um Bewegungsbilanz aus BWA und SuSa in Steuerrecht – Steuerberater und Anwälte geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen.

### Bewegungsbilanz aus BWA und SuSa

#### Fachlicher Anker

- **Normen:** § 6a, § 264 HGB, § 297 HGB.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

#### Kernsachverhalt

Die Bewegungsbilanz stellt die Veraenderungen einzelner Bilanzposten zwischen zwei Stichtagen dar und macht damit deutlich, woher Mittel kamen (Mittelherkunft) und wohin sie geflossen sind (Mittelverwendung). Sie ist Vorstufe der Kapitalflussrechnung nach DRS 21 und IDW S 6 und wird besonders bei Bankgespraechen, Sanierungsmandaten und im Vorfeld der Fortbestehensprognose benoetigt. Der Steuerberater erstellt sie aus der SuSa zum Anfangs- und Endstichtag plus den BWA-Erfolgskonten.

#### Kaltstart-Rueckfragen

1. Welche Stichtage — Quartal, Halbjahr, Jahresende?
2. Liegt eine Stichtag-SuSa vor (Anfang und Ende der Periode)?
3. Welche Detailtiefe — Hauptposten oder einzelne Konten?
4. Sondereffekte in der Periode (Anlagenverkauf, Kapitalerhoehung, Gesellschafterdarlehen)?
5. Verwendungszweck — interne Steuerung, Bankgespraech, Sanierungskonzept?
6. Welche Vergleichsperiode — Vorjahresperiode parallel?
7. Welche Konsolidierung — Einzelgesellschaft oder Konzernblick?
8. Welche Abgrenzung — Geldfluss vs. nicht-zahlungswirksame Posten (Abschreibungen, Rueckstellungen)?

#### Rechtlicher Rahmen

##### Primaernormen

**§ 264 HGB** — Aufstellungspflicht Jahresabschluss; Anhang ggf. mit Kapitalflussrechnung.

**§ 297 HGB** — Konzernabschluss; Kapitalflussrechnung verpflichtend.

**§ 252 HGB** — Bewertungsgrundsaetze.

**§ 19 InsO** — Fortbestehensprognose; Bewegungsbilanz als analytische Grundlage.

##### Standards

- DRS 21 — Kapitalflussrechnung (verbindlich für Konzernabschluesse, empfohlen für Einzelabschluesse).
- IDW S 6 — Sanierungskonzept (Bewegungsbilanz als analytische Grundlage).
- IDW PS 305 — Risikofrueherkennung § 91 Abs. 2 AktG.

#### Workflow

##### Phase 1 — Datenbasis

- SuSa zum Anfangsstichtag (z.B. 31.12. Vorjahr).
- SuSa zum Endstichtag (z.B. 31.12. Berichtsjahr).
- BWA-Daten für die Periode (insbesondere Abschreibungen, Rueckstellungsveraenderung).
- Anlagenspiegel (Zugaenge, Abgaenge, AfA).

##### Phase 2 — Strukturierung Aktiva

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

##### Phase 3 — Strukturierung Passiva

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

##### Phase 4 — Mittelherkunft und Mittelverwendung

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

##### Phase 5 — Saldo und Prüfung

- Saldo Mittelherkunft minus Mittelverwendung = Veraenderung liquide Mittel.
- Gegencheck: Veraenderung Bank-Konten in SuSa muss matchen.
- Differenz zeigt Fehler in der Aufstellung — prüfen.

##### Phase 6 — Erläuterung und Versand

- Erläuterungstext für wesentliche Bewegungen.
- Bei Bank-/Investor-Reporting: zusammen mit Bilanz und BWA.
- Mandantenakte dokumentieren.

#### Strategie und Praxis-Tipps

- Die Bewegungsbilanz ist bei Kleinunternehmen keine Pflicht, gehoert bei mittelstaendischer Bilanzanalyse jedoch zum Standard.
- Banken erwarten bei groesseren Kreditengagements regelmaessig eine Bewegungsbilanz oder direkt eine Kapitalflussrechnung.
- Bei Sanierungsmandaten ist die Bewegungsbilanz Pflichtbestandteil neben dem Liquiditaetsplan.
- Praxis-Tipp: Die Bewegungsbilanz wird ueblicherweise halbjaehrlich erstellt und nicht monatlich, da der Aufstellungsaufwand bei kuerzerem Intervall den Steuerungsnutzen uebersteigt.
- StBVV: Diese Sonderauswertung wird über Zeithonorar oder Pauschalvereinbarung gesondert abgerechnet.
- DATEV-Tipp: Das DATEV-Bilanzbericht-/BAB-Modul automatisiert die Bewegungsbilanz aus zwei SuSa-Stichtagen (Klickpfad: Rechnungswesen → Auswertungen → Bewegungsbilanz oder Bilanzanalyse-Auswertungspaket).

#### Quellen und Updates

Stand: 05/2026.

- HGB §§ 264, 297.
- DRS 21.
- IDW S 6, IDW PS 305.
- InsO § 19.
- DATEV BAB-Modul.
## Branchenvergleich BBE / DATEV in der BWA

Auswahlsignal: Wenn es um Branchenvergleich BBE / DATEV in der BWA in Steuerrecht – Steuerberater und Anwälte geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen.

### Branchenvergleich BBE / DATEV in der BWA

#### Fachlicher Anker

- **Normen:** § 6a, § 33, § 57.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

#### Kernsachverhalt

Die DATEV BBE-Datenbank (Betriebswirtschaftliche Beratung) liefert anonymisierte Vergleichsdaten von Mandanten gleicher Branche. Der Mandant kann sich so im Branchen-Mittelwert, Median und Top-Quartil verorten. Der Branchenvergleich ist starkes Beratungs-Instrument bei Quartals- und Jahresgespraechen, weil er den Mandanten nicht mit blanken Zahlen, sondern mit der Wettbewerbssituation konfrontiert. Voraussetzung: SKR 03 mit Standard-Konten, klare Branchen-Klassifikation (WZ-Code).

#### Kaltstart-Rueckfragen

1. Welche Branche — WZ-Code 2008 (Statistisches Bundesamt) bzw. Branchenschluessel?
2. Welche Mandantengroesse (Umsatz, Mitarbeiterzahl)?
3. Welche Vergleichsbasis — Branchen-Median, -Mittelwert, Top-Quartil?
4. Welche Periode — Berichtsjahr abgeschlossen oder unterjaehrig vergleichend?
5. Welche Datentiefe — gesamte GuV oder einzelne Kennzahlen?
6. Welches BBE-Modul ist abonniert — Standard, erweitert?
7. Wie aktuell sind die Branchen-Daten (BBE liefert mit 1-2 Jahren Verzug)?
8. Welche Sondereffekte sind herauszurechnen (Saison, Einmaleffekte)?

#### Rechtlicher Rahmen

##### Primaernormen

**§ 33 StBerG** — StB-Aufgabenkreis.

**§ 57 StBerG** — Gewissenhaftigkeit (Datenqualitaet).

Paragraf 102 StaRUG: Ein Branchenvergleich kann ein Signal erläutern, ersetzt aber weder den Jahresabschlussauftrag noch die Prüfung von Offenkundigkeit und vermuteter Unkenntnis.

**§ 4 BDSG / DSGVO** — Datenschutz; BBE-Daten sind anonymisiert.

##### Standards

- DATEV BBE-Branchenbericht (Standard).
- BVR-Branchenanalysen (Volks- und Raiffeisenbanken).
- Sparkassen-Branchenbarometer.
- IDW PS 480.

#### Workflow

##### Phase 1 — Branchenklassifikation

- WZ-Code des Mandanten ermitteln (aktuelle Klassifikation der Wirtschaftszweige des Statistischen Bundesamtes; bisher WZ 2008, Aktualisierung prüfen).
- Beispiele typischer WZ-Codes: Restaurants mit Bedienung, Lebensmittel-Einzelhandel, Bau von Wohngebaeuden (konkrete Schlüssel im Mandantenstamm gegen die aktuelle WZ-Fassung prüfen).
- Im DATEV-Stammblatt erfassen — Voraussetzung für BBE-Auswertung (Klickpfad: Mandantendaten → Allgemeines → Branchenschluessel).
- Bei Mischbetrieb: Hauptbranche festlegen und Nebenbranche dokumentieren.

##### Phase 2 — BBE-Datenabruf

- DATEV-Klickpfad: Kanzlei-Rechnungswesen → Auswertungen → BBE-Branchenvergleich.
- Berichtsjahr und Vergleichsperiode auswaehlen.
- Datenstand prüfen — BBE-Daten weisen typischerweise einen Zeitverzug von ein bis zwei Jahren auf.
- Filter nach Mandantengroesse (Umsatzklasse) setzen, damit Vergleich zur Peer-Gruppe sauber ist.

##### Phase 3 — Standard-Kennzahlen

| Kennzahl | Mandant | Branchen-Median | Top-Quartil |
|---|---|---|---|
| Materialquote | [X] Prozent | [Y] Prozent | [Z] Prozent |
| Personalquote | [X] Prozent | [Y] Prozent | [Z] Prozent |
| Umsatz je Mitarbeiter | [X] EUR | [Y] EUR | [Z] EUR |
| EBITDA-Marge | [X] Prozent | [Y] Prozent | [Z] Prozent |
| EBIT-Marge | [X] Prozent | [Y] Prozent | [Z] Prozent |
| Eigenkapitalquote | [X] Prozent | [Y] Prozent | [Z] Prozent |
| Anlagendeckung | [X] Prozent | [Y] Prozent | [Z] Prozent |

##### Phase 4 — Verortung und Bewertung

- Mandant im Branchen-Quartil verorten (1. Quartil = bestes, 4. Quartil = schlechtestes Viertel).
- Auffaellige Abweichungen identifizieren (mehr als 20 Prozent vom Median).
- Plausibilitaet prüfen — extreme Abweichungen können auch auf Datenfehler hinweisen.

##### Phase 5 — Beratungsansatz

- Bei unterdurchschnittlicher Materialquote: Einkaufsvorteil — staerken.
- Bei ueberdurchschnittlicher Personalquote: Produktivitaet prüfen, ggf. Personalentwicklung diskutieren.
- Bei niedriger EBITDA-Marge: Preisgestaltung, Sortimentsbereinigung prüfen.
- Bei niedriger Eigenkapitalquote: Bilanzpolitik (Thesaurierung), Finanzierungsstruktur.

##### Phase 6 — Erläuterung im Quartalsgespraech

- Branchenvergleich Praesentation an Mandant.
- Stellen heraus: was ist Ueberdurchschnitt, was Unterdurchschnitt.
- Handlungsoptionen ableiten.
- Maßnahmen-Plan zur naechsten Quartals-Prüfung.

#### Strategie und Praxis-Tipps

- BBE-Daten sind nicht ideal aktuell — bei schnellen Marktveraenderungen ggf. mit zusaetzlichen Quellen ergaenzen (Bundesverbaende, Bafa-Studien).
- Bei spezialisierten Branchen ist BBE manchmal duenn — alternative Datenbasis (Statistik der DStV, IfM-Bonn) prüfen.
- Mandant nicht ueberfordern — 3-5 Kennzahlen reichen, mehr verwirrt.
- Branchenvergleich nicht moralisieren — Mandant darf in einer Branche auch unterdurchschnittlich sein, wenn er bewusst Nische besetzt.
- StBVV: BBE-Bericht als Zusatzleistung, über Pauschal oder Zeithonorar.
- Datenschutz: BBE-Berichte enthalten anonymisierte Daten; nicht weitergeben an Dritte ohne Mandantenzustimmung.

#### Quellen und Updates

Stand: 05/2026.

- StBerG §§ 33, 57.
- DSGVO / BDSG.
- DATEV BBE-Branchenbericht.
- Klassifikation der Wirtschaftszweige (WZ 2008, Statistisches Bundesamt; aktuelle Fassung unter destatis.de abrufbar).
- IDW PS 480.
- Hinweis: BBE-Datenstand vor Mandanteneinsatz prüfen (Zeitverzug von ein bis zwei Jahren ueblich); Branchenrichtwerte aus aktuellem DATEV-BBE-Bericht oder Branchenverbands-Daten entnehmen.
## Cashflow laienverstaendlich darstellen

Auswahlsignal: Wenn es um Cashflow laienverstaendlich darstellen in Steuerrecht – Steuerberater und Anwälte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten.

### Cashflow laienverstaendlich darstellen

#### Fachlicher Anker

- **Normen:** § 6a, § 33, § 57.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

#### Kernsachverhalt

Die DRS-21-Kapitalflussrechnung ist methodisch korrekt, aber für den nicht-finanzaffinen Mandanten zu komplex. Für das Mandantengespraech braucht es eine einfachere Darstellung: Wie viel Cash kam laufend rein? Was wurde investiert? Was wurde an Bank/Gesellschafter zurueckgezahlt? Was bleibt am Monatsende? Der Steuerberater erstellt eine 1-seitige Brutto-Cashflow-Übersicht, die dem Mandanten die Geldfluesse zeigt — ohne ihn zu ueberfordern.

#### Kaltstart-Rueckfragen

1. Welcher Mandantentyp — Solo, Familien-GmbH, Mittelstand?
2. Welcher Verstaendnisgrad — Bilanz-affin oder GF ohne Finanzhintergrund?
3. Welcher Zeitraum — Monat, Quartal, Jahr?
4. Welche Detailtiefe — nur Hauptposten oder mit Einzeladern?
5. Welche Vergleichsperiode — Vorjahres-Quartal, Vorjahr?
6. Welche Investitionen sind separat darzustellen?
7. Welche Gesellschafter-Bewegungen (Ausschuettung, Privateinlage)?
8. Welcher Verwendungszweck — interne Steuerung, Bankgespraech?

#### Rechtlicher Rahmen

##### Primaernormen

**§ 33 StBerG** — StB-Aufgabenkreis; mandantengerechte Aufbereitung.

**§ 57 StBerG** — Gewissenhaftigkeit.

**§ 252 HGB** — Going-concern.

**§ 19 InsO** — Fortbestehensprognose; Cashflow-Betrachtung Pflicht.

##### Standards

- DRS 21 (methodische Grundlage).
- IDW S 6 (Sanierungskonzept).
- DStV-Praxisleitfaden Mandantenkommunikation.

#### Workflow

##### Phase 1 — Vereinfachte Cashflow-Struktur

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

##### Phase 2 — Erklaerung für den Mandanten

- "Laufender Cashflow" = Geld, das aus dem normalen Geschäft hineinkommt (ohne Investitionen, ohne Bankgeschaefte).
- "Investitions-Cashflow" = Geld, das in neue Anlagen geflossen oder aus Verkauf alter zurueckgeflossen ist.
- "Finanzierungs-Cashflow" = Geld, das mit Bank und Gesellschaftern ausgetauscht wurde.
- Summe ergibt Veraenderung Bank-/Kasse-Bestand.

##### Phase 3 — Visualisierung Wasserfall

- Wasserfall-Grafik: Startbestand Bank, dann farbig Plus/Minus, dann Endbestand.
- Mandant sieht visuell, woher das Geld kam und wohin es ging.
- DATEV Praesentation-Modul oder Excel-Wasserfalldiagramm.

##### Phase 4 — Kennzahlen für Mandant

- Free Cashflow (FCF) = laufender Cashflow minus Investitions-Cashflow.
- Bedeutung: was bleibt nach Bedienung der laufenden Investitionen?
- FCF > 0 nachhaltig = Unternehmen kann Schulden tilgen und ausschuetten.
- FCF < 0 nachhaltig = Unternehmen finanziert Verzehr.

##### Phase 5 — Beratungsempfehlung

- Bei negativem laufendem Cashflow: Working-Capital-Diskussion (Vorraete, Forderungen, Lieferanten).
- Bei negativem FCF über mehrere Perioden: Liquiditaets-Engpass droht; Liquiditaetsplanung erforderlich.
- Bei Sondereinmaleffekten (Anlagenverkauf): klar als einmalig kennzeichnen.

##### Phase 6 — Mandantenkommunikation

- Cashflow-Übersicht zusammen mit BWA versenden.
- Im Quartalsgespraech 5 Minuten erklaeren.
- Bei Krisensignalen: Sondergespraech mit Liquiditaetsplanung.

#### Strategie und Praxis-Tipps

- Bei Familien-GmbH ist Cashflow oft wichtigeres Steuerungsmass als Bilanzgewinn — direkter Bezug zur Bankliquiditaet.
- "Gewinn vs. Cash"-Erklaerung: Gewinn kann positiv sein und Bank-Bestand sinken, wenn Forderungen steigen.
- Bei Bankgespraech: Cashflow-Übersicht oft entscheidender als reine GuV.
- StBVV: Cashflow-Übersicht als Bestandteil der Quartals-BWA oder als Zusatzauftrag.
- DATEV-Tipp: Der DATEV-Bilanzbericht beinhaltet eine automatisierte Kapitalflussrechnung (Klickpfad: Rechnungswesen → Bilanzbericht → Bestandteile waehlen → Kapitalflussrechnung). Die vereinfachte Mandantendarstellung erfolgt in Excel oder im DATEV-Praesentationsmodul manuell.

#### Quellen und Updates

Stand: 05/2026.

- HGB §§ 264, 297.
- DRS 21.
- IDW S 6.
- StBerG §§ 33, 57.
- DStV-Praxisleitfaden Mandantenkommunikation.
## Erläuterungstext zur BWA für den Mandanten

Auswahlsignal: Wenn es um Erläuterungstext zur BWA für den Mandanten in Steuerrecht – Steuerberater und Anwälte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten.

### Erläuterungstext zur BWA für den Mandanten

#### Fachlicher Anker

- **Normen:** § 6a, § 33, § 57 Abs. 1.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

#### Kernsachverhalt

Die BWA ohne Erläuterung ist ein Zahlenfriedhof. Der Mandant — meist kein Bilanzbuchhalter — liest sie nicht oder falsch. Erst der Erläuterungstext macht aus Tabellen Steuerungsinformation. Der Steuerberater liefert auf 1-2 Seiten die wesentlichen Aussagen: Was ist passiert, welche Abweichungen sind erklaerungsbeduerftig, welche Handlungsempfehlungen ergeben sich? Ein guter Erläuterungstext erhoeht die Mandantenbindung und schuetzt vor Krisenuebersehen.

#### Kaltstart-Rueckfragen

1. Welcher Mandantentyp — Solo-Unternehmer, Familien-GmbH, Mittelstand mit eigener Buchhaltung?
2. Wie tief soll der Text gehen — kurze Zusammenfassung (1/2 Seite) oder ausfuehrliche Analyse (2 Seiten)?
3. Welche Abweichungen sind wesentlich (Schwellenwert absolut/prozentual)?
4. Welche Sondereffekte müssen erklaert werden (Sonderzahlung, Sonderabschreibung, Einmalumsatz)?
5. Liegen Krisensignale vor (Eigenkapital negativ, SV-Rueckstaende, Umsatzeinbruch)?
6. Welche Empfehlungen sind angebracht (Investition, Personalkosten, Lieferanten)?
7. Adressat — GF (operativer Fokus), Aufsichtsrat (strategisch), Bank (Schuldendienst)?
8. Welcher Stil — kurz und sachlich, ausfuehrlich erklaerend, mit Grafiken?

#### Rechtlicher Rahmen

##### Primaernormen

**§ 33 StBerG** — Aufgabenkreis des StB; Erläuterung ist Bestandteil der Hilfeleistung in Steuersachen.

**§ 57 Abs. 1 StBerG** — Gewissenhaftigkeit; auch in der Mandantenkommunikation.

Paragraf 102 StaRUG: Krisensignale aus der BWA nur dann als gesetzlichen Hinweis behandeln, wenn daneben ein Jahresabschlussauftrag besteht und Offenkundigkeit sowie vermutete Unkenntnis des Mandanten belegt sind.

**§ 5 RDG** — Abgrenzung Rechts- vs. Wirtschaftsberatung; rein wirtschaftliche Erläuterung ist StB-Aufgabe.

##### Standards

- IDW PS 480 (Erstellungsgrundsaetze).
- DStV-Praxisleitfaden Mandantenkommunikation.
- Berufsregeln BStBK § 13 Berufspflichten.

#### Workflow

##### Phase 1 — Schwellenwerte definieren

| Mandantengroesse | Absolute Schwelle | Prozentuale Schwelle |
|---|---|---|
| Kleinunternehmer < 500.000 EUR Umsatz | ab 500 EUR Abweichung | ab 10 Prozent |
| KMU 500.000-5 Mio EUR Umsatz | ab 2.000 EUR | ab 5 Prozent |
| Mittelstand 5-50 Mio EUR | ab 10.000 EUR | ab 3 Prozent |
| Großer Mittelstand > 50 Mio EUR | ab 50.000 EUR | ab 2 Prozent |

##### Phase 2 — Erläuterungs-Struktur

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

##### Phase 3 — Sondereffekte erläutern

- Einmaleffekte (Anlagenverkauf, Versicherungsleistung): Hinweis auf "ohne Sondereffekt waere das Ergebnis ...".
- Sonderabschreibungen (§ 7b, § 7g EStG): kurz erklaeren, dass es sich um steuerliche Förderung handelt.
- Sonderzahlungen Personal (Tantieme, Weihnachtsgeld): Hinweis auf Periodicitaet.

##### Phase 4 — Risiko- und Hinweis-Block

- Bei OPOS-Listen mit ueberfaelligen Forderungen > 60 Tage: Hinweis auf Forderungsausfall-Risiko.
- Bei Steuerrueckstaenden: Hinweis auf Saeumniszuschlaege § 240 AO und ggf. Stundung § 222 AO.
- Bei SV-Rueckstaenden: dringender Hinweis (§ 266a StGB-Risiko für GF).
- Bei Eigenkapitalerosion: Verweis auf Prüfung § 19 InsO und stb-bwa-sus-bilanz-pruefung.

##### Phase 5 — Empfehlungen formulieren

- Konkret und umsetzbar: "Bitte prüfen Sie Mahnungen für OP > 60 Tage" statt "OP-Management verbessern".
- Bei wesentlichen Maßnahmen: Termin zur Besprechung anbieten.
- Keine Rechtsberatung (§ 5 RDG); bei Rechtsfragen Verweis auf Anwalt.

##### Phase 6 — Freigabe und Versand

- 4-Augen-Prinzip: Sachbearbeiter schreibt, Berufstraeger gibt frei.
- Versand zusammen mit der BWA als PDF im verschluesselten Mandantenportal.

#### Strategie und Praxis-Tipps

- Erläuterungstexte standardisieren: Bausteinbibliothek pflegen, individualisieren je Mandant.
- Erläuterungstexte sind Haftungsschutz — bei spaeterem Streit kann der StB nachweisen, dass er hingewiesen hat.
- Nicht ausufernd: Mandant liest 2 Seiten, nicht 10. Was nicht in 2 Seiten passt, gehoert ins Quartalsgespraech.
- Wiederkehrende Posten in den Folgemonaten nur kurz erwaehnen, neuartige Effekte ausfuehrlich.
- StBVV: Erläuterungstext als Teil der BWA-Erstellung pauschalisiert; bei Sondererlaeuterung Zeithonorar.

#### Quellen und Updates

Stand: 05/2026.

- StBerG §§ 33, 57.
- StaRUG § 102.
- RDG § 5.
- AO §§ 222, 240.
- StGB § 266a.
- IDW PS 480.
## Typische BWA-Fehlerquellen und Plausibilitaetspruefung

Auswahlsignal: Wenn es um Typische BWA-Fehlerquellen und Plausibilitaetspruefung in Steuerrecht – Steuerberater und Anwälte geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten.

### Typische BWA-Fehlerquellen und Plausibilitaetspruefung

#### Fachlicher Anker

- **Normen:** § 6a, § 238 HGB, § 146 AO.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

#### Kernsachverhalt

BWA-Fehler sind nicht nur Schoenheitsmaengel — sie verfaelschen die Steuerung, können Krisensignale verdecken und im Streit mit dem Mandanten haftungsrelevant werden. Der Steuerberater muss systematisch die typischen Fehlerquellen abpruefen, bevor die BWA versendet wird. Dieser Skill ist Pflicht-Checkliste für Sachbearbeiter und Berufstraeger.

#### Kaltstart-Rueckfragen

1. Wer hat die BWA erstellt — interner Sachbearbeiter, ausgelagerte Buchhaltung, automatisch?
2. Welches Buchhaltungs-System — DATEV, Addison, Sage, BuchhaltungsButler?
3. Sind Lohnbuchungen aus separatem Lohnprogramm integriert?
4. Wurde eine OPOS-Pflege vor BWA-Erstellung durchgefuehrt?
5. Liegt eine Zwischeninventur oder Warenroll vor?
6. Hat sich am Kontenrahmen oder an der BWA-Konfiguration etwas geaendert?
7. Welche Periode wird ausgewertet — Monat, Quartal, kumuliert?
8. Gibt es Sondereffekte, die separat ausgewiesen werden sollten?

#### Rechtlicher Rahmen

##### Primaernormen

**§ 238 HGB** — ordnungsgemaesse Buchfuehrung.

**§ 146 AO** — Zeitgerechtigkeit, Vollstaendigkeit, Richtigkeit.

**§ 257 HGB / § 147 AO** — Aufbewahrung.

**§ 33 StBerG** — StB-Aufgabenkreis; Sorgfaltspflicht.

**§ 57 StBerG** — Gewissenhaftigkeit.

##### Standards

- BMF v. 28.11.2019 zu GoBD.
- IDW PS 480 (Erstellung).

#### Workflow

##### Phase 1 — Konsistenzpruefung BWA gegen SuSa

- BWA-Endsalden Erfolgskonten = SuSa-Salden? (Differenz = Fehler.)
- BWA-Block-Summen = Kontensummen? (Konfigurationsfehler bei BWA-Form?)
- Bestaendsveraenderung in BWA = Anfangs-/Endbestand-Differenz aus SuSa?

##### Phase 2 — Typische Fehlerklassen

| Fehlerklasse | Symptom | Ursache | Korrektur |
|---|---|---|---|
| Periodenabgrenzung fehlt | Sprunghafte Aufwendungen | RAP nicht gebucht | RAP nachbuchen |
| Bestandsveraenderung falsch | Wareneinsatz unplausibel | Inventur fehlt, Schaetzung schlecht | Zwischeninventur oder Warenroll |
| Lohnbuchungen verzoegert | Personalkosten zu niedrig | Lohnprogramm nicht synchron | Buchung aus Lohnprogramm uebernehmen |
| Verrechnungskonto offen | Saldo nicht null im Verrechnungs-/Geldtransit-Konto (z. B. SKR 03 1590/1599) | Buchung nicht zugeordnet | Klärung mit Mandant; Kontonummer in DATEV-Kontenrahmen SKR 03/04 prüfen (DATEV-Kontenrahmen jaehrlich aktualisiert) |
| USt-Voranmeldung uneinheitlich | USt-Konto-Saldo passt nicht | USt-Schlüssel falsch | Buchung prüfen |
| Sonderzahlungen Personal | Monatsausschlag Lohn | Tantieme einmalig | Im Erläuterungstext erwaehnen |
| Abschreibungen nicht aktualisiert | AfA monatlich konstant trotz Investition | Anlagenbuchhaltung nicht synchron | AfA aktualisieren |
| Skonti-Buchung | Erloese zu hoch | Skonti nicht erloesschmaelernd gebucht | Erloesschmaelerung im richtigen Erloeskontenbereich (vgl. DATEV-Kontenrahmen aktuelle Fassung, SKR 03 typisch 8730er bzw. SKR 04 4730er-Bereich) |
| Provisionserloese | DB falsch | Aufwand statt Erloesschmaelerung | Buchung umstellen |

##### Phase 3 — Plausibilitaetsquoten

| Quote | Branchentypisch | Auffaellig wenn |
|---|---|---|
| Materialquote Industrie | 30-50 Prozent | < 25 oder > 60 Prozent |
| Materialquote Handel | 60-80 Prozent | < 50 oder > 90 Prozent |
| Personalkostenquote DL | 35-55 Prozent | < 25 oder > 70 Prozent |
| Mietquote | 3-10 Prozent | > 15 Prozent |
| Kfz-Kosten | 1-5 Prozent | > 10 Prozent (Privatanteil prüfen) |
| Versicherungen | 0,5-2 Prozent | > 3 Prozent (Doppelbuchung) |

##### Phase 4 — Lohnbuchungs-Konsistenz

- Lohnsumme BWA muss mit dem Bruttolohn aus dem Lohnprogramm uebereinstimmen (Konten Loehne/Gehaelter SKR 03 4120/4130 bzw. SKR 04 6020/6030 — DATEV-Kontenrahmen aktuelle Fassung).
- SV-AG-Anteil-Konto-Saldo gegen den AG-Anteil aus der Lohnabrechnung prüfen (Daumenregel: ca. 20-21 Prozent vom Bruttolohn; massgebliche Beitragssaetze KV 14,6 Prozent allgemein (Stand 2025), RV 18,6 Prozent, PV 3,6 Prozent, AV 2,6 Prozent — aktuelle Werte aus der Sozialversicherungs-Rechengroessenverordnung abrufen).
- Berufsgenossenschaft monatlich anteilig gebucht (Konto SKR 03 4140 bzw. SKR 04 6140 — Konkretisierung im aktuellen DATEV-Kontenrahmen prüfen).
- Pauschalsteuer für Aushilfen über das jeweils passende Steueraufwandskonto buchen (z. B. SKR 03 4148 für Lohnsteuer 2 Prozent Pauschal — konkrete Kontonummer in der aktuellen DATEV-Kontenrahmen-Dokumentation nachschlagen).

##### Phase 5 — Spezial-Prüfungen

- Bei GmbH: Geschäftsführer-Gehalt vollstaendig erfasst? Verdeckte Gewinnausschuettung-Risiko?
- Bei Holding: Erloese aus Beteiligung sauber erfasst (steuerfrei nach § 8b KStG)?
- Bei Personenunternehmen: Privatentnahmen nicht in BWA, sondern in Kapitalkonto.
- USt-konsistenz mit USt-Voranmeldung.

##### Phase 6 — Fehlerprotokoll und Korrektur

- Fehlerliste mit Datum, Konto, Buchungssatz, Korrektur.
- Korrektur-Buchung mit Verweis im Buchungstext (z.B. "Korrektur BWA-Prüfung Q2/2026").
- Bei wesentlichen Fehlern: BWA neu erstellen und versenden.
- Mandant informieren bei Auswirkungen auf vorgelegte Reports.

#### Strategie und Praxis-Tipps

- Standardisierte Prüfliste vor jedem BWA-Versand abarbeiten — auch bei Routine-Mandanten.
- 4-Augen-Prinzip: Sachbearbeiter prüft selbst, Berufstraeger stichprobenartig.
- Bei wiederholten Fehlern beim gleichen Sachbearbeiter: Schulung erforderlich.
- DATEV-Tipp: Auswertung "Konten mit ungewoehnlichem Saldo" als monatliche Pflichtpruefung.
- Honoraranknuepfung: Fehlerprotokoll als Teil der Qualitaetssicherung, kein Extra-Honorar.
- Bei Buchungsfehlern aus Vorperiode: Vorperiode korrigieren oder Erläuterungstext mit Hinweis.

#### Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 257.
- AO §§ 146, 147.
- StBerG §§ 33, 57.
- BMF v. 28.11.2019 zu GoBD.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
