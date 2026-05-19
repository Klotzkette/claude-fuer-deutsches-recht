---
name: liquiditaetsvorschau-3-6-12-monate
description: Erstellt für eine GmbH/UG aus unstrukturierten Eingaben (Rechnungen, Bankauszüge, BWA, SuSa, Zahlungserwartungen, Daueraufträge) eine robuste rollierende Liquiditätsvorschau mit Wochenraster über 3, 6 und 12 Monate. Prüft fortlaufend, ob Zahlungsunfähigkeit nach § 17 InsO (10-%-Lücke / 3-Wochen-Horizont) droht oder bereits eingetreten ist, und liefert eine insolvenzrechtliche Fortführungsprognose unter Beachtung der Abgrenzung zwischen handelsbilanzieller und insolvenzrechtlicher Überschuldung (§ 19 InsO). Methodik nach IDW S 6 (Sanierungskonzept) und IDW S 11 (Insolvenzeröffnungsgründe). Exportiert die Tabelle nach Excel.
language: de
triggers:
  - "Liquiditätsvorschau"
  - "Liquiditätsplanung"
  - "Cashflow-Planung"
  - "Zahlungsunfähigkeit § 17 InsO"
  - "10-Prozent-Lücke"
  - "Drei-Wochen-Frist"
  - "Fortführungsprognose"
  - "Fortbestehensprognose § 19 InsO"
  - "IDW S 6"
  - "IDW S 11"
  - "13-Wochen-Forecast"
  - "rollierende Liquidität"
  - "insolvenzfähige Überschuldung"
---

# Rollierende Liquiditätsvorschau 3/6/12 Monate mit Fortführungsprognose (§§ 17, 19 InsO)

## Zweck

Dieser Skill erzeugt aus dem typischerweise vorhandenen, oft unstrukturierten Material einer kleinen Kapitalgesellschaft (offene Rechnungen, Bankauszüge, BWA, SuSa, Zahlungserwartungen, Kreditverträge, Daueraufträge, Sozialversicherungs- und Steuerbescheide) eine **rollierende Liquiditätsvorschau** mit folgenden Funktionen:

1. **Wochenraster (Mo–So)** über drei Horizonte:
   - **Kurzfristhorizont 13 Wochen (3 Monate)** – primär für § 17 InsO (Zahlungsunfähigkeit).
   - **Mittelfristhorizont 26 Wochen (6 Monate)** – Brücke zwischen Zahlungsfähigkeit und Fortführungsprognose.
   - **Langfristhorizont 52 Wochen (12 Monate)** – Grundlage Fortbestehensprognose nach § 19 Abs. 2 InsO und Fortführungsprognose nach IDW S 6.

2. **Automatische Insolvenzreife-Ampel** für jede Woche:
   - **Grün**: Liquide Mittel > 110 % der in der Folgewoche fällig werdenden Verbindlichkeiten.
   - **Gelb (Zahlungsstockung)**: Lücke < 10 % oder Lücke ≥ 10 %, aber innerhalb von 3 Wochen schließbar.
   - **Rot (Zahlungsunfähigkeit § 17 InsO)**: Lücke ≥ 10 % und nicht innerhalb von 3 Wochen schließbar (st. Rspr. BGH BGHZ 163, 134 Rn. 12 ff.).

3. **Fortführungsprognose**: 12-Monats-Auswertung mit den **Kernelementen des IDW S 6** (siehe unten), abgegrenzt von einer reinen handelsbilanziellen Überschuldungsprognose. Liefert ein Ergebnis „positive Fortführungsprognose" / „negative Fortführungsprognose" mit Begründung.

4. **Excel-Export**: Die Tabelle wird über `werkzeuge/build_liquiditaetsplan.py` als `liquiditaetsplan.xlsx` exportiert. Cloud-Bedienung über interaktive Tabelle möglich; Werte mit Excel-Formeln, nicht hartcodiert.

Anwendungsfälle: Krisen-GmbH/UG, Mittelstand mit Bugwellen-Liquidität, Vorbereitung Sanierungsgespräch mit Hausbank, Dokumentation Fortbestehensprognose für § 19 InsO, Vorbereitung StaRUG-Restrukturierungsverfahren, regelmäßige wöchentliche Geschäftsführer-Sitzung.

## Eingaben

Strukturiert oder unstrukturiert; das Modell soll robust extrahieren:

- **Stammdaten Gesellschaft**: Rechtsform, Branche, Mitarbeiterzahl, Jahresumsatz, Hausbank, Stichtag.
- **Eröffnungsbestand liquider Mittel**: Kontostände, Kasse, Tagesgeld, ungenutzte Kreditlinien (mit Laufzeit und Konditionen).
- **Offene Verbindlichkeiten** (Kreditorenliste): Lieferant, Fälligkeitsdatum, Betrag, Mahnstufe, Stundungen.
- **Offene Forderungen** (Debitorenliste): Kunde, Rechnungsdatum, Fälligkeit, voraussichtlicher Zahlungseingang, Ausfallrisiko.
- **Dauerverpflichtungen**: Miete, Pacht, Leasing, Personal (Lohn, Gehalt, AG-Anteil SV), Krankenkassenbeiträge (monatliche Drittellast), Lohnsteuer, Strom/Gas, Versicherungen.
- **Steuern**: Umsatzsteuer-Vorauszahlung/-Erstattung (mit Voranmeldungsturnus, ggf. Dauerfristverlängerung), Körperschaftsteuer-Vorauszahlung, Gewerbesteuer-Vorauszahlung, Rückstände beim Finanzamt.
- **Kreditverträge**: Tilgung, Zins, Sondertilgung, Covenants (z.B. EK-Quote, Leverage), Avalrahmen.
- **Geplante Investitionen/Desinvestitionen**: CapEx, Maschinenverkauf, Sale-and-Lease-back.
- **Auftragsbestand**: zugesagte Aufträge mit Lieferzeitpunkt, voraussichtlichem Zahlungsziel, Abschlagszahlungen.
- **Bankauszüge** der letzten 3–6 Monate (für saisonale Muster und Plausibilität).
- **BWA und SuSa** (siehe Schwester-Skill `bwa-sus-bilanz-pruefung`).

Wenn Daten lückenhaft sind: Annahmen explizit dokumentieren, sensitivitätsanalysieren (Best/Base/Worst).

## Rechtlicher Rahmen

### Primärnormen

- **§ 17 InsO – Zahlungsunfähigkeit**: Der Schuldner ist zahlungsunfähig, wenn er nicht in der Lage ist, die fälligen Zahlungspflichten zu erfüllen; in der Regel anzunehmen, wenn er seine Zahlungen eingestellt hat.
- **§ 18 InsO – Drohende Zahlungsunfähigkeit**: Voraussichtliche Unfähigkeit zur Erfüllung im Zeitraum **24 Monate** (Prognose).
- **§ 19 InsO – Überschuldung**: Vermögen deckt Verbindlichkeiten nicht, **es sei denn** Fortführung des Unternehmens ist nach den Umständen überwiegend wahrscheinlich (positive Fortbestehensprognose; Prognosehorizont aktuell 12 Monate, ggf. nach SanInsKG geändert – Stichtag prüfen).
- **§ 15a InsO – Insolvenzantragspflicht**: 3 Wochen ab Eintritt der Zahlungsunfähigkeit, 6 Wochen ab Eintritt der Überschuldung.
- **§ 15b InsO – Zahlungsverbote nach Insolvenzreife**.
- **§ 1 StaRUG – Krisenfrüherkennung**: Pflicht der Geschäftsleitung zur fortlaufenden Krisenüberwachung.

### Leitentscheidungen

1. BGH, Urt. v. 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 Rn. 12–19: Definition Zahlungsunfähigkeit; Liquiditätslücke ≥ 10 % und nicht binnen 3 Wochen schließbar; Abgrenzung zur Zahlungsstockung.

2. BGH, Urt. v. 12.10.2006 – IX ZR 228/03, NJW 2007, 78 Rn. 16–22: Indizienkatalog der Zahlungsunfähigkeit; eingestellte SV-Beiträge, Stundungen, Mahnverfahren, Lastschriftrückläufer.

3. BGH, Urt. v. 19.11.2019 – II ZR 233/18, NJW 2020, 1809 Rn. 17 ff.: Fortbestehensprognose nach § 19 Abs. 2 InsO – tragfähiges Unternehmenskonzept und Finanzplan; Maßstab überwiegende Wahrscheinlichkeit.

4. BGH, Urt. v. 09.10.2012 – II ZR 298/11, BGHZ 195, 42 Rn. 12–18: Maßgeblich ist nicht die handelsbilanzielle Überschuldung, sondern die **insolvenzrechtliche** Überschuldung; Fortführungs- vs. Liquidationswerte je nach Prognose.

### Kommentarliteratur und berufsständische Verlautbarungen

1. K. Schmidt/Herchen, in: K. Schmidt, Insolvenzordnung, 20. Aufl. 2023, § 17 InsO Rn. 5–35: Liquiditätsbilanz nach BGH-Konzept; 10-%-Grenze; 3-Wochen-Horizont; Behandlung von Stundungen und Kreditlinien.

2. Uhlenbruck/Mock, Insolvenzordnung, 16. Aufl. 2024, § 19 InsO Rn. 47–95: Zweistufige Überschuldungsprüfung; Fortbestehensprognose als Kernsanierungselement; Anforderung integrierte Planung (Ertrag/Bilanz/Liquidität).

3. **IDW S 6 (i.d.F. 2018)**: Anforderungen an die Erstellung von Sanierungskonzepten – Kernelemente: (i) Auftrag und Auftragsdurchführung, (ii) Basisinformationen, (iii) Analyse Krisenstadium und Ursachen, (iv) Leitbild des sanierten Unternehmens, (v) Maßnahmen zur Krisenbewältigung, (vi) integrierter Unternehmensplan und Fortführungsprognose.

4. **IDW S 11 (Stand 22.08.2016 + Updates)**: Beurteilung des Vorliegens von Insolvenzeröffnungsgründen – Liquiditätsstatus, 3-Wochen-Finanzplan, Fortbestehensprognose, Abgrenzung handelsbilanzielle vs. insolvenzrechtliche Überschuldung.

5. Pape/Schaltke, in: Pape/Uhländer, StaRUG, 1. Aufl. 2021, § 1 StaRUG Rn. 10–30: Geschäftsleiterpflichten zur Krisenfrüherkennung; integrierte Planung als Pflichtprogramm.

## Ablauf

**Schritt 1 – Datenaufnahme**
- Nutzer-Input parsen: PDFs (Bankauszüge, Rechnungen), CSV (Buchhaltungsexport), freier Text.
- Strukturieren in: (a) Anfangsbestand, (b) Einzahlungs-Buckets (Kundenforderungen, USt-Erstattungen, sonstige), (c) Auszahlungs-Buckets (Personal, SV, Lohnsteuer, USt-Zahlung, KSt/GewSt, Lieferanten, Miete, Leasing, Zins+Tilgung, sonstiges).
- Ausfallrisiko-Score für Debitoren (Top-Kunden, Mahnstand, Branche).

**Schritt 2 – Wochenraster bauen**
- Spalten: KW (Mo–So) ab KW Stichtag, Anfangsbestand Bank, + Einzahlungen je Bucket, − Auszahlungen je Bucket, **Endbestand**, **fällige Verbindlichkeiten in Folgewoche**, **3-Wochen-Lücke (kumuliert)**, **Lücken-Quote in %**, **Ampel**.
- Drei Sheets: `13-Wochen`, `26-Wochen`, `52-Wochen`. Letzteres monatlich aggregiert ab Monat 4.

**Schritt 3 – 3-Wochen-Test (§ 17 InsO)**
- Pro Woche: berechne `Lücke = max(0, fällige Verbindlichkeiten − verfügbare Mittel)`.
- Berechne `Lücke_3W = Summe der ungedeckten fälligen Verbindlichkeiten in t, t+1, t+2 minus erwartete Zugänge in t+1, t+2`.
- Berechne `Quote = Lücke_3W / fällige Verbindlichkeiten in t`.
- `Ampel = rot` wenn Quote ≥ 10 % und Lücke_3W am Ende der Periode nicht null; `gelb` wenn Quote ≥ 10 %, aber binnen 3 Wochen schließbar; sonst `grün`.

**Schritt 4 – Sensitivität (Best/Base/Worst)**
- Drei Spalten parallel: Zahlungseingang 100 %, 80 %, 60 % der Forderungen.
- Drei Spalten parallel: Auftragsausführung wie geplant, −10 %, −25 %.
- Ergebnis: Ampel je Szenario.

**Schritt 5 – Fortführungsprognose (12 Monate)**
- Aggregation auf Monatsebene; Übergang zu Ertrags- und Bilanzplanung (verzahnt).
- Prüfe die **IDW-S-6-Kernelemente**:
  1. **Krisenstadium** (Stakeholder-/Strategie-/Produkt-/Absatz-/Erfolgs-/Liquiditäts-/Insolvenzkrise nach Hauschka-Schema).
  2. **Krisenursachen** (intern/extern).
  3. **Leitbild** des sanierten Unternehmens (Geschäftsmodell, Markt, Positionierung).
  4. **Maßnahmen** (Innenfinanzierung, Außenfinanzierung, leistungswirtschaftlich, finanzwirtschaftlich).
  5. **Integrierte Planung** (Ertrag/Bilanz/Liquidität) 24+ Monate.
  6. **Ergebnis**: positive vs. negative Fortführungsprognose mit Begründung.
- Maßstab nach BGH NJW 2020, 1809 Rn. 18: überwiegende Wahrscheinlichkeit.

**Schritt 6 – Abgrenzung handelsbilanzielle vs. insolvenzrechtliche Überschuldung**
- Handelsbilanzielles negatives EK ist **kein** Insolvenzgrund. Maßgeblich ist der **Überschuldungsstatus** mit Fortführungswerten bei positiver Prognose, mit Liquidationswerten bei negativer Prognose (BGH BGHZ 195, 42 Rn. 12 ff.).
- Qualifizierter Rangrücktritt (§ 39 Abs. 2 InsO) eliminiert Verbindlichkeit aus dem Status.
- Stille Reserven (insb. Sachanlagen, selbst erstellte immaterielle WG) sind zu aktivieren.
- Stille Lasten (Rückstellungsbedarf, Prozessrisiken, Bürgschaften) sind anzusetzen.
- Ergebnis: **Insolvenzfähige Überschuldung** nur, wenn rechnerische Unterdeckung **und** negative Fortführungsprognose.

**Schritt 7 – Excel-Export**
- Aufruf `python werkzeuge/build_liquiditaetsplan.py --eingabe <mandant>.yaml --ausgabe liquiditaetsplan.xlsx`.
- Drei Sheets (13W/26W/52W), Ampel via bedingter Formatierung, Lückenquote in Prozentformat, Formeln (`=SUMME(...)`, `=B5-C5`, kein Hartcoding).
- Ergänzungssheet `Fortfuehrungsprognose` mit IDW-S-6-Matrix.
- Ergänzungssheet `Annahmen` (alle Inputs nachvollziehbar).

## Ausgabeformat

1. **Liquiditätsplan Excel** (`liquiditaetsplan.xlsx`) mit Sheets:
   - `13-Wochen` (Wochenraster, Ampel, 3-Wochen-Test)
   - `26-Wochen`
   - `52-Wochen` (ab Monat 4 monatlich aggregiert)
   - `Fortfuehrungsprognose` (IDW-S-6-Matrix)
   - `Annahmen` (Inputs und Sensitivitäten)
2. **Lage-Memo** im Gutachtenstil mit
   - Ergebnis § 17 InsO (zahlungsunfähig / drohend / zahlungsfähig) mit Wochenangabe des frühesten Roteintritts.
   - Ergebnis § 19 InsO (positive/negative Fortführungsprognose, insolvenzrechtliche Überschuldung indiziert ja/nein).
   - Handlungsempfehlungen: Antragspflicht §§ 15a, 15b InsO oder StaRUG-Restrukturierungsrahmen (§§ 29 ff. StaRUG).
3. **Hinweis auf Hinweispflicht** (§ 102 StaRUG) wenn nicht-Geschäftsleiter beauftragt (z.B. Steuerberater nutzt Skill für Mandanten).

## Beispiel

**Sachverhalt**: Edelholz Manufaktur Berlin GmbH, 20 Mitarbeiter, Jahresumsatz 2,1 Mio. EUR, Stichtag 18.05.2026, Kontostand 18.500 EUR, Kontokorrent 150.000 EUR zu 92 % ausgeschöpft, offene LuL 187.000 EUR (davon 64.000 EUR überfällig), SV-Rückstand 38.000 EUR, USt-Vorauszahlung 14.200 EUR fällig 10.06.2026, Großauftrag 145.000 EUR mit Lieferung KW 28 und Zahlungsziel 30 Tage netto.

**Gutachtenstil**:

*§ 17 InsO*: 13-Wochen-Test zeigt in KW 22 eine Lücke von 41.000 EUR (Quote 22 %); selbst inkl. erwarteter Eingänge aus dem Großauftrag wäre die Lücke erst in KW 32 vollständig schließbar – damit **nicht innerhalb von 3 Wochen** ab KW 22. **Zahlungsunfähigkeit liegt voraussichtlich ab KW 22 vor** (BGH BGHZ 163, 134 Rn. 14). Ampel rot.

*§ 19 InsO*: Handelsbilanzielles EK negativ. Überschuldungsstatus mit Fortführungswerten unter Berücksichtigung stiller Reserven der CNC-Anlage (Verkehrswert 180.000 EUR, Buchwert 95.000 EUR) ergibt rechnerische Unterdeckung von ca. 60.000 EUR. Fortführungsprognose negativ, weil integrierte 12-Monats-Planung keinen positiven operativen Cashflow bei realistischen Annahmen erbringt (IDW S 6, Tz. 5 ff.; BGH NJW 2020, 1809 Rn. 18). **Insolvenzrechtliche Überschuldung indiziert**.

*Handlungsempfehlung*: Antragspflicht 3 Wochen ab Eintritt § 17 InsO (KW 22) bzw. 6 Wochen ab § 19 InsO. Parallel Prüfung StaRUG-Restrukturierungsrahmen nur möglich bei rein **drohender** Zahlungsunfähigkeit – nicht mehr eröffnet, wenn § 17 InsO bereits eingetreten ist. Hinweis nach § 102 StaRUG durch beauftragten Steuerberater zu erteilen.

## Risiken und typische Fehler

- **Handelsbilanzielle vs. insolvenzrechtliche Überschuldung verwechseln**: Negatives EK in HGB-Bilanz allein begründet keinen Antragsgrund (BGH BGHZ 195, 42 Rn. 12); maßgeblich ist Überschuldungsstatus.
- **3-Wochen-Frist statisch rechnen**: Die Frist läuft ab dem **Eintritt** der Zahlungsunfähigkeit, nicht ab Erstellung des Liquiditätsplans.
- **Stundungen als Liquidität werten**: Stundungen verschieben die Fälligkeit, sind aber Indiz für Zahlungsunfähigkeit (BGH NJW 2007, 78 Rn. 18) – nicht beruhigen lassen.
- **Kreditlinien unkritisch ansetzen**: Nur **zugesagte und ziehungsfähige** Linien zählen; gekündigte oder ausgeschöpfte Linien nicht.
- **Großaufträge ohne Zahlungseingangsrisiko ansetzen**: Realistische Annahmen mit Ausfall- und Skonto-Quoten; immer Sensitivität (Worst Case).
- **Fortführungsprognose ohne IDW-S-6-Struktur**: Eine nicht strukturierte „Prognose" trägt vor Gericht nicht; BGH NJW 2020, 1809 verlangt tragfähiges Konzept.
- **USt- und LSt-Rückstände kleinreden**: Diese sind starke Insolvenzindizien und führen oft zur Anzeige durch Finanzamt/Krankenkasse (§ 15a Abs. 4 InsO).
- **Personalkosten unterschätzen**: Lohn + AG-Anteil SV + KK-Beiträge = ca. 1,28× Bruttolohn; monatliche Drittellast SV-Beiträge.
- **SanInsKG-Stand übersehen**: Prognosehorizont § 19 InsO wurde temporär verkürzt; aktuelle Fassung am Bewertungsstichtag prüfen.

## Quellenpflicht

Alle Aussagen sind nach `references/zitierweise.md` zu belegen. Mindestens zwei Rspr.-Belege im BGH-Stil (BGHZ 163, 134; BGH NJW 2007, 78; BGH NJW 2020, 1809; BGHZ 195, 42) und zwei Kommentarbelege im Bearbeiter-Stil (K. Schmidt/Herchen; Uhlenbruck/Mock; Pape/Schaltke). Berufsständische Verlautbarungen (IDW S 6, IDW S 11) sind gesondert zu zitieren und nicht als „Rechtsprechung" zu kennzeichnen.

Siehe ergänzend:
- `references/idw-s6-kernelemente.md` – Strukturmatrix Sanierungskonzept
- `references/wochenraster-anleitung.md` – Aufbau und Buckets der Wochenplanung
- `werkzeuge/build_liquiditaetsplan.py` – Excel-Generator (mit Beispiel-YAML)
