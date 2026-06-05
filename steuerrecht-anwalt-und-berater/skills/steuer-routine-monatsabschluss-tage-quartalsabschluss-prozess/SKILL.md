---
name: steuer-routine-monatsabschluss-tage-quartalsabschluss-prozess
description: "Steuer Routine Monatsabschluss Tage Quartalsabschluss Prozess: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Steuer Routine Monatsabschluss Tage Quartalsabschluss Prozess

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **Steuer Routine Monatsabschluss Tage Quartalsabschluss Prozess** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stb-routine-monatsabschluss-30-tage-zyklus` | Routine Monatsabschluss im 30-Tage-Zyklus. Anwendungsfall systematische Steuerung der Monatsabschluss-Routine in der Kanzlei mit klaren Deadlines Belegabgabe Buchung BWA-Versand USt-VA. Methodik Termin-Controlling. Output 30-Tage-Plan. |
| `stb-routine-quartalsabschluss-prozess` | Routine Quartalsabschluss-Prozess. Anwendungsfall vierteljaehrlicher Quartalsabschluss mit Periodenabgrenzung Quartals-BWA Mandantengespraech und Steuerthemen. Methodik strukturierter Quartals-Plan. Output Quartals-BWA Quartalsbericht Gespraech. |
| `stb-sanierungsgewinn-3c-iv-estg-verlustreihenfolge` | § 3c Absatz 4 EStG Verlustreihenfolge: bestehende Verlustvorträge mindern den Sanierungsertrag, bevor die Steuerbefreiung nach § 3a EStG greift. Folge: Verlustvortrag wird verbraucht, mindestens aber bis Mindestbesteuerung. |
| `stb-sanierungsgewinn-7b-gewstg-gewerbesteuer-parallel` | § 7b GewStG befreit den Sanierungsertrag parallel zur ESt/KSt von der Gewerbesteuer. Eigener Antrag mit Gewerbesteuererklärung erforderlich; nicht automatisch aus § 3a EStG-Antrag mit zu erstrecken. |
| `stb-sanierungsgewinn-10a-s-1-gewstg-gewerbeverlust` | § 10a Satz 1 GewStG Gewerbeverlust-Verbrauch im Sanierungskontext. Reihenfolge und Mindestbesteuerung bei der Gewerbesteuer; Parallele zu § 3c Absatz 4 EStG. |
| `stb-sanierungsgewinn-betriebsstaette-und-international` | Internationale Aspekte des Sanierungsertrags: Betriebsstätten-Zuordnung, DBA-Behandlung, Sanierungsforderungsverzicht durch ausländische Gläubiger. § 3a EStG gilt nur für die deutsche Besteuerung. |
| `stb-sanierungsgewinn-debt-equity-swap-statt-verzicht` | Debt-Equity-Swap als Alternative zum Forderungsverzicht: Umwandlung der Forderung in Eigenkapital. Sanierungssteuerlich oft günstiger; aber gesellschaftsrechtliche Hürden und Werthaltigkeits-Problem zu beachten. |
| `stb-sanierungsgewinn-koerperschaftsteuer-vs-einkommensteuer` | Unterschiede in der Sanierungsertragsbehandlung zwischen Körperschaftsteuer und Einkommensteuer. KSt geht über § 8 Absatz 1 KStG auf § 3a EStG; ESt direkt; unterschiedliche Verlustverrechnung und Antragsstruktur. |
| `stb-sanierungsgewinn-liquidation-nachrang-fg-koeln` | Solvente GmbH-Liquidation mit nachrangigem Gesellschafterdarlehen. Klaert mit der verifizierten FG-Koeln-Linie (Urteil v. 06.03.2012 — 13 K 3006/11, GmbHR 2012 Seite 977; vorgehend zu BFH I R 34/12) und mit BFH II R 19/01 die Frage, wann die Verbindlichkeit ausgebucht werden muss und ob ein etwaiger Sanierungsgewinn mangels Koerperschaftsteuersubjekt noch festsetzbar ist. Adressat ist der Steuerberater oder Rechtsanwalt, der eine GmbH ohne Insolvenz nur per Liquidation abwickeln will und ein hohes Gesellschafterdarlehen mit qualifiziertem Rangruecktritt im Bestand hat. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **Steuer Routine Monatsabschluss Tage Quartalsabschluss Prozess**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stb-routine-monatsabschluss-30-tage-zyklus`

**Fokus:** Routine Monatsabschluss im 30-Tage-Zyklus. Anwendungsfall systematische Steuerung der Monatsabschluss-Routine in der Kanzlei mit klaren Deadlines Belegabgabe Buchung BWA-Versand USt-VA. Methodik Termin-Controlling. Output 30-Tage-Plan.

# 30-Tage-Zyklus Monatsabschluss

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `30-Tage-Zyklus Monatsabschluss` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Der Monatsabschluss laeuft in einem standardisierten 30-Tage-Zyklus ab. Ohne klare Deadlines verzoegern sich Auswertungen, Belegabgabe schleppt sich, USt-VA wird verspaetet. Der 30-Tage-Plan strukturiert die Arbeit der Kanzlei und definiert Pflichten Mandant / Sachbearbeiter / Berufstraeger.

## Kaltstart-Rueckfragen

1. Mandantengroesse und Belegvolumen?
2. Welche Monatsabschluss-Termine sind vereinbart?
3. Welche Sachbearbeiter haben welchen Mandantenstamm?
4. Welche Sondertermine (LSt 10., SV drittletzter Bankarbeitstag)?
5. Welche Eskalations-Routine?
6. Welche Mandantengruppen mit Sonderbehandlung (Krise, Sanierung)?
7. Welches Termin-Controlling-Tool (DATEV-Kanzleiplaner, externes)?
8. Welche Urlaubsvertretung im Team?

## Rechtlicher Rahmen

### Primaernormen

**§ 146 AO** — Zeitgerechtigkeit.

**§ 18 UStG** — USt-VA-Fristen.

**§ 41a EStG** — LSt-Anmeldung 10. Folgemonat.

**§ 23 SGB IV** — SV-Beitragsfrist drittletzter Bankarbeitstag.

## Workflow

### Phase 1 — 30-Tage-Plan (Standard)

```
TAG 1-5: BELEGEINGANG
- Mandant uebermittelt Belege
- Sachbearbeiter prueft Vollstaendigkeit
- Bei Verzoegerung: Mahnung Stufe 1

TAG 6-15: BUCHUNG
- Bank, Kasse, Eingangs- und Ausgangsrechnungen
- Lohnbuchung aus Lohnprogramm
- OPOS-Pflege

TAG 16-22: ABSTIMMUNG UND PERIODENABGRENZUNG
- Kontenabstimmung
- Verrechnungskonten auf null
- RAP, Rueckstellungen anteilig
- AfA monatlich

TAG 23-25: SUSA UND BWA
- SuSa-Pruefung
- BWA-Erstellung
- Berufstraeger-Pruefung
- Erlaeuterungstext

TAG 26-28: AUSWERTUNG VERSAND
- USt-Voranmeldung
- BWA und SuSa an Mandant
- Mandanten-Notiz mit Erlaeuterung

TAG 29-30: ABSCHLUSS UND ARCHIVIERUNG
- Mandantenakte aktualisieren
- Wiedervorlage Folgemonat
- Honoraranknuepfung pruefen
```

### Phase 2 — Sondertermine

| Tag | Pflicht |
|---|---|
| 10. des Folgemonats | LSt-Anmeldung |
| Drittletzter Bankarbeitstag | SV-Beitragsnachweis und -Zahlung |
| 10. des Folgemonats | USt-VA (sofern monatlich) |
| 15. Februar Folgejahr | Jahresmeldung DEUEV, BG-Lohnnachweis |
| 28. Februar Folgejahr | LSt-Bescheinigungen |
| 31. Juli Folgejahr | Steuererklaerungen Standardfrist § 149 Abs. 2 AO (ohne Beratervorbehalt) |
| Letzter Tag Februar des **zweiten** Folgejahres | Steuererklaerungen mit Beratervorbehalt § 149 Abs. 3 AO (StB-Mandat); fuer Veranlagungszeitraeume mit verlaengerten Fristen Stand pruefen |

### Phase 3 — Mandantengruppen

- A-Mandanten (Mittelstand, vollservice): 30-Tage-Plan strict.
- B-Mandanten (KMU, monatlich): 30-Tage-Plan moderately strict.
- C-Mandanten (Kleinmandanten, vierteljaehrlich): Quartalsplan.

### Phase 4 — Eskalation

- Bei Belegabgabe-Verzoegerung: 1./2./3. Mahnung.
- Bei wiederholten Verspaetungen: Honorar-Aufschlag, Mandatsgespraech.
- Bei dauerhafter Verspaetung: Mandatsniederlegung pruefen.

### Phase 5 — Sachbearbeiter-Zuordnung

- Klare Zustaendigkeit pro Mandant.
- Urlaubsvertretung dokumentiert.
- Berufstraeger-Pruefung mindestens beim Versand.

### Phase 6 — Controlling

- DATEV-Kanzleiplaner mit Termin-Erinnerungen.
- Monats-Statistik: Wie viele Mandanten p termingerecht?
- KPIs: Tage zwischen Belegannahme und BWA-Versand.

## Output

- 30-Tage-Plan mit Termin-Sicherheit.
- BWA, USt-VA, SV-Meldung pflichtgemaess.
- Mandantenkommunikation strukturiert.

## Strategie und Praxis-Tipps

- 30-Tage-Plan ist Standard fuer professionelle Kanzleien — staerkstes Qualitaetsmerkmal.
- Bei Krisen-Mandanten 2-Wochen-Zyklus (Liquiditaetsplan).
- Bei Saisonbetrieb angepasste Planung (z.B. Saison-Spitzen).
- Sachbearbeiter-Schulung in der Kanzlei zu klaren Prozessen.
- StBVV: in Buchfuehrungspauschale.

## Querverweise

- `stb-bwa-monatsabschluss-routine` — Monatsabschluss.
- `stb-pruefliste-belegabgabe-monatlich` — Belegabgabe.
- `stb-routine-quartalsabschluss-prozess` — Quartalsabschluss.
- `stb-lohn-monatsende-meldepflichten-checkliste` — Lohn-Meldepflichten.
- `stb-mandantenanfrage-reaktion-frist-laufend` — Reaktionsfristen.

## Quellen und Updates

Stand: 05/2026.

- AO § 146.
- UStG § 18.
- EStG § 41a.
- SGB IV § 23.
- DStV-Praxisleitfaden Kanzleiorganisation.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `stb-routine-quartalsabschluss-prozess`

**Fokus:** Routine Quartalsabschluss-Prozess. Anwendungsfall vierteljaehrlicher Quartalsabschluss mit Periodenabgrenzung Quartals-BWA Mandantengespraech und Steuerthemen. Methodik strukturierter Quartals-Plan. Output Quartals-BWA Quartalsbericht Gespraech.

# Quartalsabschluss-Prozess

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Quartalsabschluss-Prozess` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Der Quartalsabschluss ist ein vertiefter Monatsabschluss: ueblicherweise mit vollstaendigeren Periodenabgrenzungen, Quartals-BWA, Bilanzentwurf-Vorlauf, Quartalsgespraech mit dem Mandanten. Standard fuer Mittelstand und groessere KMU. Bei Konzern-Mandanten Pflicht (Konsolidierungs-Anforderung).

## Kaltstart-Rueckfragen

1. Welche Mandantengroesse — Quartalsabschluss Standard oder ausnahmsweise?
2. Welche Periodenabgrenzung-Tiefe (Bestand, RAP, Rueckstellungen)?
3. Liegt Inventur vor (Quartals-Zwischeninventur)?
4. Welche Konsolidierungs-Anforderung Konzern?
5. Welche Bank- oder Investor-Reporting?
6. Welches Quartals-Gespraech (Termin, Teilnehmer)?
7. Welche Steuerthemen anstehend (Vorauszahlungs-Anpassung)?
8. Welche Sondervorgaenge (Anlagenkauf, Personalveraenderung)?

## Rechtlicher Rahmen

### Primaernormen

**§§ 238, 252 HGB** — Buchfuehrungs- und Bewertungsgrundsaetze.

**§ 18 UStG** — USt-VA (vierteljaehrlich moeglich bei kleineren Mandanten).

**§ 33 StBerG** — StB-Aufgabenkreis.

## Workflow

### Phase 1 — Quartals-Plan

```
WOCHE 1-2 NACH QUARTALSENDE: BELEGE UND BUCHUNG
- Letzte Belege Quartal komplett
- Buchung abschliessen
- OPOS-Pflege

WOCHE 3: PERIODENABGRENZUNG VERTIEFT
- Bestandsfortschreibung (Schaetzung bei Industrie)
- Rueckstellungen quartalsweise
- AfA aktualisieren
- Bestandsveraenderungen erfassen

WOCHE 4: ABSTIMMUNG UND BWA
- Hauptbuch-Nebenbuch
- Anlagen-Konten
- USt-Quartals-VA
- BWA mit Vorjahresvergleich kumuliert

WOCHE 5: REPORTING UND GESPRAECH
- Quartalsbericht
- Mandantengespraech
- Strategiethemen
```

### Phase 2 — Quartals-BWA-Inhalte

- Kumulierter Jahresblock seit Jahresbeginn.
- Vorjahresvergleich Quartal.
- Plan-Ist-Vergleich.
- Kennzahlen aktualisiert.

### Phase 3 — Quartalsgespraech

- 1-2 Stunden mit GF.
- Standard-Agenda (siehe stb-mandantenkommunikation-bwa-uebergabe-quartal).
- Dokumentation.

### Phase 4 — Steuerthemen

- USt-Voranmeldung quartalsweise.
- Steuervorauszahlungen anpassen (Antrag § 37 EStG).
- Investitionsabzugsbetrag § 7g EStG.
- Sonderabschreibung pruefen.

### Phase 5 — Sonderfall Konzern

- Konsolidierungs-Daten an Mutter.
- IFRS-Reporting separat moeglich.
- Konzernbericht zeitnah.

### Phase 6 — Wiedervorlage Folgequartal

- Naechster Termin im Kalender.
- Massnahmen-Liste aus Gespraech.
- Strategie-Themen kontrollieren.

## Output

- Quartals-BWA mit allen Kennzahlen.
- Quartalsbericht.
- Gespraechs-Protokoll.

## Strategie und Praxis-Tipps

- Bei A-Mandanten Quartalsabschluss Standard, nicht nur Monatsabschluss.
- Quartal-Periodenabgrenzung tiefer als Monat (Bestand-Schaetzung sorgfaeltiger).
- Bei Konzern-Mandanten Termincontrolling kritisch (Konzern-Frist meist eng).
- StBVV: Quartalsabschluss als gesonderter Auftrag oder in Pauschalvereinbarung.
- DATEV-Tipp: DATEV Quartals-BWA mit kumuliertem Vergleich.

## Querverweise

- `stb-routine-monatsabschluss-30-tage-zyklus` — Monatsabschluss.
- `stb-mandantenkommunikation-bwa-uebergabe-quartal` — Quartalsgespraech.
- `stb-bwa-aufbau-grundlagen` — BWA.
- `stb-susa-monatlich-quartalsweise` — SuSa.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 252.
- UStG § 18.
- StBerG § 33.
- EStG § 37.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `stb-sanierungsgewinn-3c-iv-estg-verlustreihenfolge`

**Fokus:** § 3c Absatz 4 EStG Verlustreihenfolge: bestehende Verlustvorträge mindern den Sanierungsertrag, bevor die Steuerbefreiung nach § 3a EStG greift. Folge: Verlustvortrag wird verbraucht, mindestens aber bis Mindestbesteuerung.

# § 3c Abs. 4 EStG — Verlustreihenfolge bei Sanierung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `§ 3c Abs. 4 EStG — Verlustreihenfolge bei Sanierung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

§ 3c Abs. 4 EStG ist die "stille" Norm, die regelmäßig übersehen wird. Sie ordnet an, dass vor der Steuerbefreiung des Sanierungsertrags nach § 3a EStG zunächst alle vorhandenen Verlustvorträge zu verrechnen sind. Erst der danach verbleibende Sanierungsertrag wird steuerfrei. Konsequenz: Der Verlustvortrag wird durch die Sanierung aufgezehrt, auch wenn er für andere Zwecke (Folgejahre) noch von Wert gewesen wäre.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Wie hoch ist der Sanierungsertrag (vor Verlustverrechnung)?
2. Welche Verlustvorträge bestehen — laufender Verlust, Vortrag § 10d EStG, Gewerbeverlust § 10a S. 1 GewStG?
3. Ist die Mindestbesteuerung § 10d Abs. 2 EStG / § 10a Sätze 2-3 GewStG zu beachten?
4. Welche Reihenfolge der Verrechnung sieht das Gesetz vor?
5. Welche Aufwendungen sind nach § 3c Abs. 1 EStG mit dem Sanierungsertrag wirtschaftlich verknüpft (sanierungsbezogen)?

## Rechtlicher Rahmen

- **§ 3c Abs. 4 EStG** — Sonderregel Verlustreihenfolge bei Sanierung.
- **§ 3c Abs. 1 EStG** — Allgemeines Aufwandsabzugsverbot bei steuerfreien Einnahmen.
- **§ 10d EStG** — Verlustabzug ESt.
- **§ 10d Abs. 2 EStG** — Mindestbesteuerung: Sockelbetrag 1 Mio. EUR + 60 %.
- **§ 10a Satz 1 GewStG** — Gewerbeverlust.
- **§ 10a Sätze 2-3 GewStG** — Mindestbesteuerung GewSt.
- **§ 3a Abs. 1, 4 EStG** — Steuerbefreiung Sanierungsertrag.

## / Schritt für Schritt

### Verrechnungsreihenfolge nach § 3c Abs. 4 EStG

| Stufe | Inhalt |
|---|---|
| 1 | Sanierungsertrag ermitteln (Verzichtsbetrag minus zugehörige Aufwendungen § 3c Abs. 1 EStG) |
| 2 | Laufender Verlust des Sanierungsjahres mindert Sanierungsertrag (§ 3c Abs. 4 S. 1 EStG) |
| 3 | Verlustrücktrag (§ 10d Abs. 1 EStG) — sofern in Anspruch genommen — mindert Sanierungsertrag |
| 4 | Verlustvortrag (§ 10d Abs. 2 EStG) mindert Sanierungsertrag — Mindestbesteuerungsgrenze beachten |
| 5 | Nicht-Sanierungsgewinne anderer Einkunftsquellen mindern den nutzbaren Verlust |
| 6 | Verbleibender Sanierungsertrag wird gem. § 3a Abs. 1 EStG steuerfrei gestellt — auf Antrag |
| 7 | Folge: Verlustvortrag in der Höhe der Verrechnung dauerhaft verbraucht |

### Parallele Logik im Gewerbesteuerrecht

| Stufe | Inhalt |
|---|---|
| 1 | Gewerbeertrag = handelsrechtlicher Gewinn + GewSt-spezifische Hinzurechnungen/Kürzungen |
| 2 | Gewerbeverlust (§ 10a S. 1 GewStG) mindert Gewerbeertrag — Mindestbesteuerung beachten |
| 3 | Sanierungsertrag-Anteil des Gewerbeertrags wird gem. § 7b GewStG steuerfrei gestellt — eigener Antrag |
| 4 | Verbleibender Sanierungsertrag im GewSt: 0 EUR (bei Antrag) |
| 5 | Gewerbeverlust durch Verrechnung aufgezehrt |

## Trade-off-Matrix

| Konstellation | Wirkung § 3c Abs. 4 EStG | Empfehlung |
|---|---|---|
| Kleiner Sanierungsertrag, großer Verlustvortrag | Voll verrechenbar | Antrag § 3a IV ggf. entbehrlich |
| Großer Sanierungsertrag, kleiner Verlustvortrag | Teilverrechnung; Rest steuerfrei | Antrag § 3a IV zwingend |
| Sanierungsertrag genau in Höhe Verlustvortrag | Voll verrechnet; kein steuerfreier Rest | Antrag § 3a IV taktisch erwägen |
| Mehrere Geschäftsbereiche mit eigenen Verlusten | § 3c IV ordnet pro Steuerpflichtigem zu | Einzelfallprüfung |
| Mehrjährige Sanierung mit Verzichten in mehreren Jahren | Verrechnung pro Jahr neu | Strategische Aufteilung |

## Praxistipps der alten Hasen

- **Die Mindestbesteuerung greift auch bei Sanierung.** § 3c Abs. 4 EStG ordnet die Verrechnung nach § 10d Abs. 2 EStG-Regeln an. Bei großen Sanierungserträgen (> 1 Mio. EUR) bleibt also auch bei reichlich Verlustvortrag ein Restbetrag von 40 % zu versteuern — ohne Antrag § 3a Abs. 4 EStG voll steuerpflichtig.
- **§ 3c Abs. 1 EStG (Aufwandsabzugsverbot) gilt auch hier.** Aufwendungen, die in unmittelbarem wirtschaftlichen Zusammenhang mit dem Sanierungsertrag stehen (z. B. Beraterkosten Sanierung, Rechtskosten Vergleich), dürfen den Gewinn nicht mindern. Sie werden vom Sanierungsertrag abgezogen (= mindern die steuerfreie Größe), nicht vom übrigen Ergebnis.
- **Laufender Verlust vor Vortrag.** Das Gesetz ordnet die Verrechnung in einer bestimmten Reihenfolge an: erst laufender Verlust, dann Rücktrag, dann Vortrag.
- **Reihenfolge erspart Streit.** Die Berechnung ist transparent und nachvollziehbar — sie muss in der Steuererklärung in Anlage Sanierungsertrag dargestellt werden.

## Mustertexte / Berechnungsbeispiele

### Berechnungsbeispiel mit Mindestbesteuerung

```
Sanierungsertrag brutto EUR 2.000.000
abzgl. zugehörige Aufwendungen
 § 3c Abs. 1 EStG EUR -150.000
Sanierungsertrag netto EUR 1.850.000

Laufender Verlust Sanierungsjahr EUR -200.000
Sanierungsertrag nach lauf. Verlust EUR 1.650.000

Verlustvortrag § 10d EStG verfügbar EUR 1.300.000
Mindestbesteuerung:
 Sockel EUR 1.000.000
 + 60 % von (1.650.000 - 1.000.000) EUR 390.000
 = maximal nutzbarer Vortrag EUR 1.390.000
 begrenzt durch Vortrag EUR 1.300.000

Sanierungsertrag nach Vortrag EUR 350.000
► steuerfrei § 3a Abs. 1 EStG bei Antrag § 3a Abs. 4 EStG
► Verlustvortrag voll verbraucht (EUR 1.300.000 weg)
► laufender Verlust (EUR 200.000) verbraucht
```

### Berechnungsbeispiel ohne Antrag

```
Wenn KEIN Antrag § 3a Abs. 4 EStG gestellt:
► § 3a EStG nicht anwendbar
► aber § 3c Abs. 4 EStG bleibt Spezialregel?
► Lex: ohne Antrag tritt § 3a-Steuerbefreiung nicht ein;
 Sanierungsertrag voll steuerpflichtig
► Mindestbesteuerung § 10d Abs. 2 EStG greift wie üblich
► Verlustverbrauch wie sonst auch
```

### Berechnungsbeispiel Verlustrücktrag

```
Sanierungsjahr Wj X mit Sanierungsertrag EUR 800.000
Verlustrücktrag aus Wj X+1 möglich EUR 200.000
 (Verlust in X+1 entstanden; § 10d Abs. 1 EStG-Wahlrecht)

Reihenfolge § 3c Abs. 4 EStG:
1. Laufender Verlust Wj X (sofern vorhanden)
2. Verlustrücktrag Wj X+1 nach Wj X (Wahlrecht ausgeübt)
3. Verlustvortrag § 10d Abs. 2 EStG

Verbleibender Sanierungsertrag nach Rücktrag EUR 600.000
abzgl. Verlustvortrag § 10d Abs. 2 EStG EUR 600.000
Restbetrag EUR 0

► Sanierungsertrag voll verrechnet
► Antrag § 3a IV EStG möglicherweise entbehrlich
► Aber: Verlustrücktrag-Wahlrecht prüfen (Folgejahre)
```

### Praxis-Hinweis Verrechnungsdokumentation

```
Anlage zur Steuererklärung Sanierungsjahr:
- Berechnungsschema § 3c Abs. 4 EStG mit:
 - Sanierungsertrag brutto
 - § 3c Abs. 1 EStG-Aufwendungen
 - Sanierungsertrag netto
 - Verrechnung laufender Verlust
 - Verrechnung Rücktrag (falls beantragt)
 - Verrechnung Vortrag mit Mindestbesteuerung
 - Steuerfrei zu stellender Restbetrag
- Vortragsrest zum Jahresende
- Gewerbeverlust separat (analog § 10a S. 1 GewStG)
```

## Typische Fehler

- Mindestbesteuerung übersehen; Sanierungsertrag voll mit Verlustvortrag verrechnet ohne Sockel-Logik.
- Aufwendungen § 3c Abs. 1 EStG nicht abgezogen; Sanierungsertrag falsch zu hoch ausgewiesen.
- Reihenfolge laufender Verlust / Rücktrag / Vortrag nicht eingehalten.
- Gewerbesteuer-Parallele § 10a S. 1 GewStG vergessen.
- Verlustvortrag nach Antrag bzw. Sanierung im Folgejahr noch angesetzt — ist aber verbraucht.

## Querverweise

- `stb-sanierungsgewinn-verlustvortrag-sanity-check`
- `stb-sanierungsgewinn-3a-iv-estg-antrag-und-bindungswirkung`
- `stb-sanierungsgewinn-10a-s-1-gewstg-gewerbeverlust`
- `stb-sanierungsgewinn-7b-gewstg-gewerbesteuer-parallel`
- `stb-sanierungsgewinn-koerperschaftsteuer-vs-einkommensteuer`

## Quellen Stand 06/2026

- § 3c Abs. 1, 4 EStG.
- § 3a Abs. 1, 4 EStG.
- § 10d Abs. 1, 2, 4 EStG.
- § 10a S. 1-3, 6 GewStG.
- § 7b GewStG.
- BMF-Schreiben vom 27.04.2017 — vor Verwendung Stand prüfen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; Quelle vor Ausgabe protokollieren.

## 4. `stb-sanierungsgewinn-7b-gewstg-gewerbesteuer-parallel`

**Fokus:** § 7b GewStG befreit den Sanierungsertrag parallel zur ESt/KSt von der Gewerbesteuer. Eigener Antrag mit Gewerbesteuererklärung erforderlich; nicht automatisch aus § 3a EStG-Antrag mit zu erstrecken.

# § 7b GewStG — Gewerbesteuer-Befreiung Sanierung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `§ 7b GewStG — Gewerbesteuer-Befreiung Sanierung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

§ 7b GewStG ist die gewerbesteuerliche Schwesternorm zu § 3a EStG. Der Sanierungsertrag wird auch von der Gewerbesteuer befreit — aber nur, wenn ein eigener Antrag mit der Gewerbesteuererklärung gestellt wird. Wer nur § 3a Abs. 4 EStG beantragt, bleibt auf der Gewerbesteuer sitzen. Die GewSt-Belastung des Sanierungsertrags ist bei einem Hebesatz von 400 % rund 14 % — das ist nicht unerheblich.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Ist die Mandantin gewerbesteuerpflichtig (Gewerbebetrieb)?
2. Welcher Hebesatz gilt am Sitz / der Betriebsstätte?
3. Welcher Gewerbeverlust-Vortrag (§ 10a S. 1 GewStG) ist vorhanden?
4. Ist der § 3a EStG / § 8 KStG-Antrag bereits gestellt?
5. Mehrere Betriebsstätten — Zerlegung erforderlich?

## Rechtlicher Rahmen

- **§ 7b Abs. 1 GewStG** — Sanierungsertrag bleibt bei der Ermittlung des Gewerbeertrags außer Ansatz.
- **§ 7b Abs. 2 GewStG** — Verweis auf § 3a EStG-Voraussetzungen.
- **§ 7b Abs. 3 GewStG** — eigener Antrag.
- **§ 10a Sätze 1-3, 6 GewStG** — Gewerbeverlust und Mindestbesteuerung.
- **§ 7 GewStG** — Gewerbeertrag.
- **§ 16 GewStG** — Steuermesszahl und Hebesatz.

## / Schritt für Schritt

| Schritt | Inhalt | Output |
|---|---|---|
| 1 | Gewerbeertrag ohne Sanierungswirkung berechnen | Basisgrößen |
| 2 | Sanierungsertrag identifizieren — gleicher Betrag wie bei § 3a EStG | Sanierungsertrag-Komponente |
| 3 | Verlust-Verrechnung nach § 10a S. 1 GewStG (Mindestbesteuerung) | Reduzierter Sanierungsertrag |
| 4 | Antrag § 7b GewStG mit Gewerbesteuererklärung | Antragseingang |
| 5 | Nachweis vier Voraussetzungen § 3a Abs. 1 EStG (Verweis auf § 3a-Antrag) | Verweisanlage |
| 6 | Bei mehreren Betriebsstätten: Zerlegung beachten | Anteilige Befreiung pro Betriebsstätte |
| 7 | Steuermesszahl nach Verrechnung anwenden | Steuermessbetrag |
| 8 | Hebesatz Gemeinde anwenden | GewSt |

## Trade-off-Matrix

| Konstellation | Auswirkung | Empfehlung |
|---|---|---|
| § 3a EStG-Antrag gestellt, § 7b GewStG vergessen | Volle GewSt auf Sanierungsertrag | Antrag nachholen — fristgerecht möglich? |
| Gewerbeverlust deckt Sanierungsertrag | Mindestbesteuerung bedenken | § 7b GewStG ggf. unnötig |
| Mehrere Betriebsstätten | Zerlegung; § 7b GewStG je Gemeinde | Beachten — pro Betriebsstätte |
| Personengesellschaft mit Gewerbeertrag | Antrag pro Steuersubjekt | Einzelfallprüfung |
| Hohe Hebesatzgemeinde | Hohe Ersparnis durch § 7b GewStG | Antrag besonders wichtig |

## Praxistipps der alten Hasen

- **§ 7b GewStG ist eigenständig.** Der § 3a Abs. 4 EStG-Antrag erstreckt sich NICHT automatisch auf die Gewerbesteuer. Eigener Antrag in der Gewerbesteuererklärung — sonst Steuerlast trotz Sanierung.
- **Mindestbesteuerung im Gewerbesteuerrecht** funktioniert parallel zur ESt/KSt: Sockel 1 Mio. EUR + 60 % des übersteigenden Sanierungsertrags. Bei kleinen Sanierungsbeträgen bis 1 Mio. EUR voll mit Verlust verrechenbar — § 7b GewStG-Antrag dann häufig entbehrlich (wenn Verlust deckt).
- **Hebesatz prüfen.** Bei Großstädten mit Hebesatz 470-490 % entspricht die GewSt-Belastung 16-17 % — das ist mehr als die KSt-Belastung des Sanierungsertrags ohne Vorabzug.
- **Zerlegungsmasse bei mehreren Betriebsstätten** ist § 28 GewStG. Der Sanierungsertrag wird auf die Betriebsstätten verteilt — § 7b GewStG wirkt pro Betriebsstätte.

## Mustertexte / Berechnungsbeispiele

### Muster Antrag § 7b GewStG

```
[Briefkopf]
An das Finanzamt [Ort]
- Gewerbesteuerstelle -

Anlage zur Gewerbesteuererklärung [Erhebungszeitraum]
der [Firma]

Betreff: Antrag nach § 7b Abs. 3 GewStG — Befreiung des
 Sanierungsertrags von der Gewerbesteuer

Sehr geehrte Damen und Herren,

namens und in Vollmacht unserer Mandantin beantragen wir
die Befreiung des im Wirtschaftsjahr [...] entstandenen
Sanierungsertrags in Höhe von EUR [Betrag] von der Gewerbe-
steuer gem. § 7b Abs. 1 GewStG.

Die Voraussetzungen des § 3a Abs. 1 EStG sind erfüllt; wir
verweisen auf den Antrag nach § 3a Abs. 4 EStG vom [Datum]
(Anlage zur KSt-/ESt-Erklärung [Jahr]) und die dortigen
Anlagen 1 bis 5 (IDW S 6-Konzept, Verzichtserklärungen
der Gläubiger, Krisendokumentation).

Berechnung Gewerbeertrag:

Gewerbeertrag vor Sanierungswirkung EUR [G]
+ Sanierungsertrag EUR [S]
Gewerbeertrag brutto EUR [G+S]

- Gewerbeverlust § 10a S. 1 GewStG verbraucht EUR [V]
 (Mindestbesteuerung beachtet)

Gewerbeertrag nach Verlustverrechnung EUR [G+S-V]
- Sanierungsertrag-Befreiung § 7b GewStG EUR [S-(verrechnet)]
zu versteuernder Gewerbeertrag EUR [G-V_übrig]

Mit freundlichen Grüßen
[Berater]
```

### Berechnungsbeispiel ohne § 7b-Antrag

```
Sanierungsertrag EUR 1.500.000
Gewerbeverlust EUR 0
Hebesatz 410 %
Steuermesszahl 3,5 %

Ohne § 7b GewStG-Antrag:
Gewerbesteuer = 1.500.000 × 3,5 % × 4,10 = EUR 215.250

Mit § 7b GewStG-Antrag:
Gewerbesteuer auf Sanierungsertrag = EUR 0

► Ersparnis EUR 215.250 durch eigenen Antrag
```

### Berechnungsbeispiel mit Gewerbeverlust

```
Sanierungsertrag EUR 800.000
Gewerbeverlust-Vortrag EUR 600.000
Hebesatz 410 %

Mindestbesteuerung:
 Sockel 1.000.000 + 60 % (800.000 - 1.000.000) → nicht relevant,
 da Sanierungsertrag < Sockel; voll verrechenbar

Verrechnung: 600.000 vom Sanierungsertrag
verbleibender Sanierungsertrag EUR 200.000

§ 7b GewStG: EUR 200.000 steuerfrei
Effektive GewSt auf Sanierungsertrag: EUR 0
Gewerbeverlust verbraucht
```

## Typische Fehler

- § 7b GewStG-Antrag vergessen — volle GewSt-Last auf Sanierungsertrag.
- Vier Voraussetzungen nicht erneut in GewSt-Anlage dokumentiert (kann Verwaltung kritisieren).
- Mindestbesteuerung übersehen.
- Zerlegung bei mehreren Betriebsstätten nicht beachtet.
- § 10a S. 1 GewStG-Vortrag mit § 10d EStG-Vortrag verwechselt.

## Querverweise

- `stb-sanierungsgewinn-3a-iv-estg-antrag-und-bindungswirkung`
- `stb-sanierungsgewinn-10a-s-1-gewstg-gewerbeverlust`
- `stb-sanierungsgewinn-3c-iv-estg-verlustreihenfolge`
- `stb-sanierungsgewinn-betriebsstaette-und-international`
- `stb-sanierungsgewinn-zustaendigkeiten-fa-betriebspruefung`

## Quellen Stand 06/2026

- § 7b Abs. 1, 2, 3 GewStG.
- § 10a S. 1-3, 6 GewStG.
- § 7 GewStG.
- § 16, § 28 GewStG.
- § 3a Abs. 1, 4 EStG (Verweis).
- BMF-Schreiben vom 27.04.2017 — Stand prüfen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; Quelle vor Ausgabe protokollieren.

## 5. `stb-sanierungsgewinn-10a-s-1-gewstg-gewerbeverlust`

**Fokus:** § 10a Satz 1 GewStG Gewerbeverlust-Verbrauch im Sanierungskontext. Reihenfolge und Mindestbesteuerung bei der Gewerbesteuer; Parallele zu § 3c Absatz 4 EStG.

# § 10a Satz 1 GewStG — Gewerbeverlust bei Sanierung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `§ 10a Satz 1 GewStG — Gewerbeverlust bei Sanierung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

§ 10a Satz 1 GewStG regelt die Verlustverrechnung im Gewerbesteuerrecht. Im Sanierungskontext steht er parallel zu § 3c Abs. 4 EStG: Bevor § 7b GewStG den Sanierungsertrag freistellt, wird der Gewerbeverlust verrechnet. Auch hier gilt die Mindestbesteuerung (§ 10a Sätze 2-3 GewStG).

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Wie hoch ist der vortragsfähige Gewerbeverlust (gesonderter Feststellungsbescheid § 10a S. 6 GewStG)?
2. Ist ein Unternehmer- oder Unternehmenswechsel erfolgt (§ 10a S. 8 GewStG)?
3. Welche Konsequenzen hat § 8c KStG-analog im Gewerbesteuerrecht (Verlust-Untergang bei Anteilseignerwechsel)?
4. Sanierungsklausel im Gewerbesteuerrecht: § 8c Abs. 1a KStG analog anwendbar (umstritten — Stand prüfen)?
5. Mindestbesteuerung greift?

## Rechtlicher Rahmen

- **§ 10a Satz 1 GewStG** — Gewerbeverlust-Vortrag bis zu 1 Mio. EUR voll, darüber 60 % des übersteigenden positiven Gewerbeertrags.
- **§ 10a Satz 2 GewStG** — Sockelbetrag und Quote (Mindestbesteuerung).
- **§ 10a Satz 6 GewStG** — gesonderte Feststellung des Vortrags.
- **§ 10a Satz 8 GewStG** — Unternehmer- bzw. Unternehmenswechsel; Wegfall bei Verlust der Unternehmensidentität.
- **§ 7b GewStG** — Sanierungsertragsbefreiung.
- **§ 7 GewStG** — Ermittlung Gewerbeertrag.

## / Schritt für Schritt

| Schritt | Inhalt |
|---|---|
| 1 | Gewerbeverlust-Vortrag aus letztem Feststellungsbescheid § 10a S. 6 GewStG abrufen |
| 2 | Unternehmer-/Unternehmensidentität geprüft (§ 10a S. 8 GewStG, BFH-Rspr. — keine Entscheidung aus Modellwissen) |
| 3 | Gewerbeertrag des Sanierungsjahres ermitteln (mit Sanierungsertrag) |
| 4 | Mindestbesteuerung anwenden: Sockel 1 Mio. EUR + 60 % Übersteigend |
| 5 | Gewerbeverlust gegen Sanierungsertrag verrechnen |
| 6 | Verbleibender Sanierungsertrag-Anteil → § 7b GewStG freistellen (Antrag) |
| 7 | Verbleibender Gewerbeertrag → Steuermessbetrag und Hebesatz |

## Trade-off-Matrix

| Konstellation | Wirkung | Empfehlung |
|---|---|---|
| Gewerbeverlust deckt Sanierungsertrag voll | Sanierungsertrag vor § 7b GewStG aufgezehrt | § 7b GewStG-Antrag entbehrlich |
| Großer Sanierungsertrag, kleiner Vortrag | Teilverrechnung; Rest § 7b GewStG | § 7b GewStG-Antrag zwingend |
| Sanierungsertrag knapp über Sockel | Mindestbesteuerung relevant | Berechnung sauber dokumentieren |
| Anteilseignerwechsel vor Sanierung | § 10a S. 8 GewStG-Risiko | Sanierungsklauseln analog prüfen |
| Mehrere Mitunternehmer | Anteilig je Mitunternehmer | Einzelfallprüfung |

## Praxistipps der alten Hasen

- **§ 10a S. 8 GewStG ist die GewSt-Falle parallel zu § 8c KStG.** Bei wesentlichem Unternehmer- oder Unternehmenswechsel kann der Gewerbeverlust untergehen. Im Sanierungskontext oft kritisch: Wenn die Sanierung von einem Anteilseignerwechsel begleitet wird, kann der Vortrag weg sein, bevor § 7b GewStG zur Anwendung kommt.
- **Sanierungsklausel im Gewerbesteuerrecht** ist nicht direkt im GewStG verankert; die analoge Anwendung von § 8c Abs. 1a KStG ist umstritten und höchstrichterlich nicht eindeutig geklärt — vor Verwendung Rechtsstand prüfen.
- **Mindestbesteuerung in Sanierungssituationen** wirkt besonders hart, weil der Sanierungsertrag häufig ein einmaliger Ausschlag ist. Bei Erträgen über 1 Mio. EUR bleibt 40 % steuerpflichtig — § 7b GewStG-Antrag ist dann unverzichtbar.
- **Feststellungsbescheid abrufen.** Verlassen Sie sich nicht auf Buchhaltungs-Stand; nur der Bescheid § 10a S. 6 GewStG ist verbindlich.

## Mustertexte / Berechnungsbeispiele

### Berechnungsbeispiel Mindestbesteuerung GewSt

```
Gewerbeertrag vor Sanierung EUR -100.000
Sanierungsertrag EUR 2.300.000
Gewerbeertrag des Jahres EUR 2.200.000

Gewerbeverlust-Vortrag § 10a S.1 GewStG EUR 1.600.000

Mindestbesteuerung:
 Sockel EUR 1.000.000
 + 60 % (2.200.000 - 1.000.000) EUR 720.000
 maximal nutzbarer Vortrag EUR 1.720.000
 begrenzt durch Vortrag EUR 1.600.000

Gewerbeertrag nach Verlustverrechnung EUR 600.000
Davon Sanierungsertrag-Anteil (max.) EUR 600.000
► § 7b GewStG-Antrag stellen, um diesen Anteil freizustellen
► Gewerbeverlust voll verbraucht
```

### Berechnungsbeispiel ohne Anteilseignerwechsel-Problematik

```
Sanierungsertrag EUR 500.000
Gewerbeertrag laufendes Geschäft EUR -100.000
Gewerbeertrag des Jahres EUR 400.000

Gewerbeverlust-Vortrag EUR 450.000

Mindestbesteuerung: Sockel 1 Mio. > 400.000 ► voll nutzbar
Verrechnung: 400.000 vom Gewerbeertrag
verbleibender Gewerbeertrag EUR 0
► § 7b GewStG-Antrag dennoch erwägen (Bindungswirkung minimal,
 da Ertrag bereits durch Verlust verbraucht)
```

### Memo-Baustein zur Identitätsprüfung § 10a S. 8 GewStG

```
Memo: § 10a S. 8 GewStG — Unternehmer-/Unternehmensidentität

I. Sachverhalt
[Anteilseignerwechsel von ... zu ... am ...; Branche
unverändert; Personal teils übernommen ...]

II. Rechtsfrage
Bleibt der Gewerbeverlust-Vortrag erhalten?

III. Subsumtion
- Unternehmensidentität (Branche, Betriebsstätte, ...)
- Unternehmeridentität (juristische Person bleibt)
- BFH-Linie zur Wesentlichkeit nicht aus Modellwissen
 zitieren; vor Ausgabe Quelle prüfen

IV. Folge
[Wenn untergegangen: kein Verbrauch durch Sanierungsertrag möglich;
 wenn erhalten: Verbrauch gem. § 10a S. 1 GewStG]
```

## Typische Fehler

- Feststellungsbescheid nicht abgerufen; Vortragsbetrag aus Erinnerung.
- § 10a S. 8 GewStG-Untergang übersehen — Anteilseignerwechsel ignoriert.
- Mindestbesteuerung übergangen; FA korrigiert Bescheid.
- Reihenfolge: § 10a S. 1 GewStG vor § 7b GewStG nicht beachtet.
- Verwechslung mit § 10d EStG.

## Querverweise

- `stb-sanierungsgewinn-3c-iv-estg-verlustreihenfolge`
- `stb-sanierungsgewinn-7b-gewstg-gewerbesteuer-parallel`
- `stb-sanierungsgewinn-verlustvortrag-sanity-check`
- `stb-sanierungsgewinn-koerperschaftsteuer-vs-einkommensteuer`

## Quellen Stand 06/2026

- § 10a S. 1, 2, 3, 6, 8 GewStG.
- § 7b GewStG.
- § 7, § 16, § 28 GewStG.
- § 8c, § 8d KStG (analog).
- BMF-Schreiben vom 27.04.2017 — Stand prüfen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; Quelle vor Ausgabe protokollieren.

## 6. `stb-sanierungsgewinn-betriebsstaette-und-international`

**Fokus:** Internationale Aspekte des Sanierungsertrags: Betriebsstätten-Zuordnung, DBA-Behandlung, Sanierungsforderungsverzicht durch ausländische Gläubiger. § 3a EStG gilt nur für die deutsche Besteuerung.

# Sanierungsgewinn — Betriebsstätte und international

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Betriebsstätte und international` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Bei grenzüberschreitenden Sachverhalten wirft die Sanierungsertragsbefreiung Fragen auf: Welche Betriebsstätte trägt den Ertrag? Wie wirkt das anwendbare Doppelbesteuerungsabkommen? Kann ein ausländischer Gläubiger die Voraussetzungen nach § 3a EStG erfüllen? § 3a EStG ist eine rein deutsche Norm; ausländische Steuersysteme behandeln Sanierungserträge oft anders.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Hat die Schuldnerin Betriebsstätten im Ausland?
2. Sind ausländische Gläubiger beteiligt?
3. Welche DBA sind anwendbar (insb. Großbritannien, USA, Niederlande, Schweiz, Österreich)?
4. Wird über § 3a EStG-Antrag deutsche Besteuerung vermieden — was passiert mit der ausländischen Steuer?
5. Verrechnungspreis-Aspekte bei konzerninternem Schuldenerlass?

## Rechtlicher Rahmen

- **§ 3a Abs. 1, 4 EStG** — Befreiung Sanierungsertrag.
- **§ 49 EStG** — Beschränkte Steuerpflicht.
- **§ 12 AO** — Betriebsstätte.
- **§ 1 AStG** — Verrechnungspreise.
- **§ 8b KStG** — Beteiligungserträge / Gesellschafter im Ausland.
- **DBA** — typischerweise Art. 5 (Betriebsstätte), Art. 7 (Unternehmensgewinne), Art. 11 (Zinsen).
- **§ 50d Abs. 8, 9 EStG** — Subject-to-tax-Klauseln.

## / Schritt für Schritt

### Schuldner ist deutsche Gesellschaft mit Auslandsbetriebsstätte

| Schritt | Inhalt |
|---|---|
| 1 | Sanierungsertrag entsteht handelsbilanziell auf Gesellschaftsebene |
| 2 | Steuerlich: Zuordnung des Ertrags zur Betriebsstätte / Stammhaus nach Funktions- und Risikoanalyse |
| 3 | Welcher Verzicht ist welcher Betriebsstätte zuzuordnen (Verzicht auf Forderung einer Auslandsbetriebsstätte vs. Stammhaus)? |
| 4 | § 3a EStG befreit nur den Anteil, der der deutschen Steuerpflicht unterliegt |
| 5 | DBA: Auslandsbetriebsstätte i. d. R. mit Freistellungsmethode (Art. 7 DBA-typisch); deutsche Steuerbefreiung greift ohnehin nicht |
| 6 | Antrag § 3a Abs. 4 EStG nur für deutschen Teil |

### Schuldner ist deutsche Gesellschaft, ausländischer Gläubiger

| Schritt | Inhalt |
|---|---|
| 1 | Sanierungsertrag auf Ebene der deutschen Gesellschaft |
| 2 | § 3a EStG-Voraussetzungen (vier Punkte) müssen erfüllt sein — auf deutschen Sachverhalt bezogen |
| 3 | Sanierungsabsicht des ausländischen Gläubigers — schriftliche Bestätigung, ggf. in englischer Sprache mit deutscher Übersetzung |
| 4 | Verrechnungspreise: § 1 AStG bei konzerninternem Verzicht prüfen — Werthaltigkeitsbewertung |
| 5 | Antrag § 3a Abs. 4 EStG — deutsche Steuer |
| 6 | Wirkung in der Heimatjurisdiktion des Gläubigers: ggf. Forderungsausfall steuerlich abzugsfähig |

### Schuldner ist ausländische Gesellschaft mit deutscher Betriebsstätte

| Schritt | Inhalt |
|---|---|
| 1 | Beschränkte Steuerpflicht in Deutschland (§ 49 EStG) — nur für deutsche Betriebsstätte |
| 2 | Sanierungsertrag der deutschen Betriebsstätte: § 3a EStG anwendbar |
| 3 | Stammhaus im Ausland — kein deutsches Besteuerungsrecht (außer Sonderfall) |
| 4 | Vier Voraussetzungen für die Betriebsstätte zu dokumentieren |

## Trade-off-Matrix

| Konstellation | Wirkung § 3a EStG | Hinweis |
|---|---|---|
| Deutsche GmbH, Auslandsverbindlichkeit | Bei deutschem Steuersubstrat anwendbar | DBA-Freistellung für Auslandsteil prüfen |
| Deutsche GmbH, ausländischer Verzichter | § 3a EStG anwendbar wenn Voraussetzungen erfüllt | Sanierungsabsicht-Bestätigung in DE bekommen |
| Auslands-GmbH mit DE-Betriebsstätte | Anwendbar für Betriebsstätten-Ertrag | Stammhaus außen vor |
| Konzerninterner Verzicht | § 1 AStG-Risiko (verdeckte Gewinnausschüttung / Einlage) | Vorher Prüfung |
| Hybride Instrumente (Genussrecht etc.) | Sonderfälle | Einzelfallprüfung |

## Praxistipps der alten Hasen

- **§ 3a EStG ist deutsch.** Andere Jurisdiktionen kennen keine analoge Regel oder anderslautende. Bei internationalen Sanierungen muss in jeder Jurisdiktion separat geprüft werden.
- **DBA-Freistellung kann § 3a EStG erübrigen.** Wenn das DBA dem Stammhaus-Staat das Besteuerungsrecht zuweist und Deutschland nur freistellt, ist § 3a EStG für diesen Teil ohnehin nicht relevant.
- **Sanierungsabsicht ausländischer Gläubiger.** Eine schriftliche Erklärung in englischer Sprache mit ausdrücklichem Bezug "for purposes of restructuring / sanierung of [Firma]" und beglaubigter deutscher Übersetzung sichert die Beweislage.
- **§ 1 AStG-Verrechnungspreise.** Bei konzerninternem Verzicht prüft das FA, ob ein fremder Dritter ebenso verzichtet hätte. Wenn nein, droht eine verdeckte Gewinnausschüttung / Einlage statt § 3a EStG.
- **Hinzurechnungsbesteuerung § 7 AStG** kann bei Zwischengesellschaften wirken — der Sanierungsertrag der Zwischengesellschaft wird in Deutschland zugerechnet, § 3a EStG wirkt dort nicht analog (umstritten — Stand prüfen).

## Mustertexte / Berechnungsbeispiele

### Beispiel: Deutsche GmbH mit britischer Betriebsstätte

```
Verbindlichkeit gegenüber dt. Bank EUR 1.000.000
Verbindlichkeit gegenüber brit. Bank EUR 500.000

Verzicht beide Banken voll:
► Gesamt-Sanierungsertrag EUR 1.500.000

Zuordnung:
► Stammhaus DE: EUR 1.000.000 ► § 3a EStG-Antrag
► Betriebsstätte UK: EUR 500.000 ► DBA-Freistellung greift,
 deutsche Steuerbefreiung nicht erforderlich
► UK behandelt Ertrag nach UK-Recht (separat zu prüfen)
```

### Mustererklärung Sanierungsabsicht ausländischer Gläubiger

```
Confirmation of restructuring intent / Bestätigung der
Sanierungsabsicht

We, [Foreign Creditor], hereby waive our claims against
[Debtor GmbH] in the amount of EUR [...] arising from
[loan agreement / invoice / etc.] dated [...].

This waiver is expressly granted for the purposes of
restructuring (Sanierung) of the Debtor's business
within the meaning of section 3a of the German Income
Tax Act (Einkommensteuergesetz). We acknowledge that
this confirmation may be used as evidence vis-à-vis
the German tax authorities.

[Place], [Date]
[Authorized signature]

[Beglaubigte deutsche Übersetzung beifügen]
```

## Typische Fehler

- Zuordnung Sanierungsertrag zur falschen Betriebsstätte — Steuerlast unverhältnismäßig.
- Sanierungsabsicht-Bestätigung des ausländischen Gläubigers ohne Übersetzung; FA bestreitet.
- § 1 AStG-Verrechnungspreise nicht beachtet; verdeckte Gewinnausschüttung statt § 3a EStG.
- DBA-Anwendung übersehen; Doppelbesteuerung oder doppelter Verzicht.
- § 7 AStG-Hinzurechnung bei Zwischengesellschaft nicht geprüft.

## Querverweise

- `stb-sanierungsgewinn-3a-estg-grundtatbestand`
- `stb-sanierungsgewinn-3a-iv-estg-antrag-und-bindungswirkung`
- `stb-sanierungsgewinn-koerperschaftsteuer-vs-einkommensteuer`
- `stb-sanierungsgewinn-zustaendigkeiten-fa-betriebspruefung`

## Quellen Stand 06/2026

- § 3a Abs. 1, 4 EStG.
- § 49 EStG.
- § 12 AO.
- § 1, § 7 AStG.
- § 8b KStG.
- § 50d Abs. 8, 9 EStG.
- Doppelbesteuerungsabkommen — jeweils einschlägiges DBA.
- BMF-Schreiben vom 27.04.2017 — Stand prüfen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; Quelle vor Ausgabe protokollieren.

## 7. `stb-sanierungsgewinn-debt-equity-swap-statt-verzicht`

**Fokus:** Debt-Equity-Swap als Alternative zum Forderungsverzicht: Umwandlung der Forderung in Eigenkapital. Sanierungssteuerlich oft günstiger; aber gesellschaftsrechtliche Hürden und Werthaltigkeits-Problem zu beachten.

# Debt-Equity-Swap statt Forderungsverzicht

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Debt-Equity-Swap statt Forderungsverzicht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Der Debt-Equity-Swap ist die Umwandlung einer Forderung des Gläubigers in Anteile am Schuldner — typischerweise im Wege einer Kapitalerhöhung mit Sacheinlage (Forderung). Aus Sicht des Schuldners verschwindet die Verbindlichkeit, ohne dass ein Ertrag entsteht (im werthaltigen Bereich). Aus Sicht des Gläubigers werden Anteile geschaffen. Dieser Skill stellt den d/e-swap als Alternative zum Forderungsverzicht dar.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Ist der Gläubiger bereit, Anteile am Schuldner zu erwerben?
2. Hat der Schuldner die Rechtsform für eine Kapitalerhöhung (GmbH, AG)?
3. Wie hoch ist der Teilwert der Forderung (Werthaltigkeit)?
4. Gesellschaftsrechtliche Zustimmung der Altgesellschafter?
5. Bewertung der Forderung: extern (Wirtschaftsprüfer) oder intern?
6. Soll Insolvenzplan / StaRUG genutzt werden, um Mehrheits-Hürden zu überwinden?

## Rechtlicher Rahmen

- **§§ 55 ff. GmbHG** — Kapitalerhöhung GmbH.
- **§ 56 GmbHG** — Sacheinlage.
- **§§ 182 ff. AktG** — Kapitalerhöhung AG.
- **§ 9 InsO / §§ 217 ff. InsO** — Insolvenzplan; Debt-Equity-Swap als Planmaßnahme.
- **§ 7 StaRUG** — Eigenverwaltete Restrukturierung.
- **§ 5 EStG, § 8 Abs. 3 KStG** — Verdeckte Einlage / Einlagebewertung.
- **§ 3a EStG** — Sanierungsertrag.
- **§ 17 EStG** — Anteile am Kapital von Gesellschaften.
- **§ 8b KStG** — Beteiligungserträge.

## / Schritt für Schritt

### Variante 1: Außergerichtlicher d/e-swap

| Schritt | Inhalt |
|---|---|
| 1 | Verhandlung mit Gläubiger über Übernahme von Anteilen |
| 2 | Werthaltigkeitsprüfung der Forderung (Teilwert) |
| 3 | Gesellschafterversammlung: Zustimmung zur Kapitalerhöhung mit Sacheinlage |
| 4 | Sacheinlagebewertung (§ 56 GmbHG i. V. m. §§ 19-21 GmbHG) |
| 5 | Anmeldung Handelsregister |
| 6 | Buchhalterische Umsetzung beim Schuldner |
| 7 | Steuerliche Folge beim Schuldner: Einlage in Kapitalrücklage; kein Sanierungsertrag bei voller Werthaltigkeit |

### Variante 2: d/e-swap im Insolvenzplan / StaRUG

| Schritt | Inhalt |
|---|---|
| 1 | Plan vorbereiten — Gläubigergruppe Anteilseigner |
| 2 | Verzicht auf Bezugsrecht der Altgesellschafter im Plan (§ 225a InsO / § 9 StaRUG) |
| 3 | Plan-Annahme durch Gläubigerversammlung |
| 4 | Vollzug — Anteile entstehen, Forderung erlischt |
| 5 | Bilanzielle Umsetzung beim Schuldner |
| 6 | Steuerliche Folgen: i. d. R. keine Sanierungsertrags-Konstellation, da Einlage |

## Trade-off-Matrix

| Aspekt | Forderungsverzicht | Debt-Equity-Swap |
|---|---|---|
| Ertrag beim Schuldner | Ja, ggf. § 3a EStG erforderlich | Nein bei werthaltiger Forderung |
| Verlustvortrag verbrannt | Ja (§ 3c IV EStG) | Nein |
| Gläubiger erhält | Nichts | Anteile / Beteiligung |
| Gesellschaftsrechtliche Hürden | Keine | Hoch (Kapitalerhöhung, Zustimmung) |
| Buchhalterischer Aufwand | Gering | Hoch |
| FA-Streit | Ja, vier Voraussetzungen | Geringer, wenn Werthaltigkeit klar |
| Eignung bei vielen Gläubigern | Begrenzt | Hoch (im Plan) |
| Gewerbesteuerliche Folge | § 7b GewStG-Antrag | Keine — Einlage |
| § 8c KStG-Risiko | Gering | Anteilseignerwechsel ► Vorsicht |

## Praxistipps der alten Hasen

- **Werthaltigkeit ist der Schlüssel.** Wenn die Forderung nicht werthaltig ist, entsteht beim Schuldner trotz Sacheinlage ein Ertrag in Höhe der Differenz zwischen Nennwert und Teilwert. Dann ist die "Verzichts"-Logik wieder relevant.
- **Bewertung extern absichern.** Sacheinlagen werden vom Registergericht geprüft. Ein gutachterlicher Wertnachweis (WP, externer Sachverständiger) ist die sichere Variante.
- **§ 8c KStG-Falle.** Der d/e-swap erzeugt einen Anteilseignerwechsel — § 8c KStG-Verlustuntergang droht. § 8d KStG-Antrag prüfen.
- **Insolvenzplan als Hebel.** Im Plan können Bezugsrechte der Altgesellschafter ausgeschlossen werden (§ 225a InsO), was außergerichtlich nur mit deren Zustimmung geht. StaRUG erlaubt Ähnliches.
- **Kombination möglich.** Häufig werden d/e-swap und Verzicht kombiniert: Hauptgläubiger swappt, kleinere verzichten. Steuerlich getrennte Würdigung.
- **§ 8b KStG für den Gläubiger.** Wenn der Gläubiger Kapitalgesellschaft ist und die Beteiligung später veräußert, greift § 8b KStG (95 % Steuerfreiheit) — der d/e-swap ist also auch gläubigerseitig attraktiv.

## Mustertexte / Berechnungsbeispiele

### Vergleich Forderungsverzicht vs. d/e-swap

```
Ausgangslage:
 Forderung Gläubiger A EUR 1.500.000
 Forderung Gläubiger B EUR 500.000
 Forderung Gläubiger C EUR 300.000
 Verlustvortrag KSt EUR 400.000
 Hebesatz GewSt 410 %

Szenario 1: Vollständiger Forderungsverzicht
 Sanierungsertrag EUR 2.300.000
 Verlustvortrag verbraucht EUR -400.000
 steuerpflichtiger Ertrag ohne Antrag EUR 1.900.000
 KSt + SolZ ~ EUR 300.000
 GewSt ~ EUR 273.000
 Gesamtsteuer ohne § 3a/§ 7b ~ EUR 573.000
 Mit Antrag § 3a/§ 7b: EUR 0
 Aber: Bindungswirkung, Aufwand Vier-Voraussetzungen-Doku

Szenario 2: d/e-swap nur Gläubiger A, Rest Verzicht
 Sacheinlage A (werthaltig) EUR 1.500.000 ► Kapitalrücklage
 Verzicht B + C EUR 800.000
 Sanierungsertrag EUR 800.000
 Verlustvortrag verbraucht EUR -400.000
 Rest steuerpflichtig ohne Antrag EUR 400.000
 Steuerlast ohne Antrag ~ EUR 120.000
 Mit Antrag § 3a/§ 7b für 400.000: EUR 0 (Bindung nur kleinere Größe)
 Verlustvortrag geschont in Höhe d/e-swap-Teil

► d/e-swap erspart Verlustvortrag-Verbrauch
► reduziert Antrags-Bindungswirkung
```

### Muster Sacheinlageerklärung (Auszug)

```
Sacheinlageerklärung gem. § 56 GmbHG

Der Kreditgeber [Gläubiger] tritt sämtliche Ansprüche aus
dem Darlehensvertrag vom [Datum] in Höhe von EUR 1.500.000
an die [Schuldnerin] GmbH ab. Diese Forderung wird im
Rahmen der heute beschlossenen Kapitalerhöhung als Sach-
einlage auf einen neuen Geschäftsanteil von EUR [...]
eingebracht. Der Wert der Forderung ist im Werthaltigkeits-
gutachten der [WP] vom [Datum] (Anlage) mit EUR 1.500.000
festgestellt.

Mit der Eintragung der Kapitalerhöhung im Handelsregister
erlischt die Forderung des Gläubigers gegenüber der Schuld-
nerin gem. § 364 BGB durch Konfusion.
```

## Typische Fehler

- Werthaltigkeit der Forderung nicht extern bewertet; FA bestreitet später.
- § 8c KStG-Falle übersehen; Verlustvortrag geht durch Anteilseignerwechsel unter.
- Bezugsrechtsausschluss der Altgesellschafter außergerichtlich ohne Zustimmung versucht.
- Im Plan d/e-swap als Strukturelement vergessen; nur Verzichte beschlossen.
- Steuerliche Würdigung d/e-swap nicht von Verzicht abgegrenzt.

## Querverweise

- `stb-sanierungsgewinn-forderungsverzicht-bilanzielle-darstellung`
- `stb-sanierungsgewinn-rangruecktritt-und-5-abs-2a-estg`
- `stb-sanierungsgewinn-vermeidungsstrategien-praxis`
- `stb-sanierungsgewinn-verlustvortrag-sanity-check`
- `stb-sanierungsgewinn-koerperschaftsteuer-vs-einkommensteuer`

## Quellen Stand 06/2026

### Normen

- §§ 55, 56 GmbHG.
- §§ 182, 183 AktG.
- §§ 217, 225a InsO.
- § 9 StaRUG.
- § 5 EStG, § 5 Abs. 2a EStG.
- § 6 Abs. 1 Nr. 3 EStG i.V.m. § 12 Abs. 1 BewG.
- § 8 Abs. 3 KStG.
- § 8b KStG.
- § 8c, § 8d KStG.
- § 3a EStG.
- § 11 KStG (Liquidationsbesteuerung).
- BMF-Schreiben vom 27.04.2017 — Stand prüfen.

### Rechtsprechung (verifiziert)

- **BFH, Urt. v. 19.08.2020 — XI R 32/18, BStBl. II 2021, 279** — § 5 Abs. 2a EStG bei Rangruecktritt (relevant fuer Abgrenzung DES vs. Verzicht vs. Rangruecktritt).
- **BFH, Urt. v. 30.11.2011 — I R 100/10, DStR 2012, 450** — Voraussetzungen der Passivierung; wirtschaftliche Belastung.
- **BFH, Urt. v. 17.11.2020 — I R 2/18, BStBl. II 2021, 580** — kein § 42 AO bei Gewinn-auf-Verlust-Verschmelzung im Rueckwirkungszeitraum.
- **FG Koeln, Urt. v. 06.03.2012 — 13 K 3006/11, GmbHR 2012, 977** (vorgehend zu BFH I R 34/12) — Liquidations-Kernentscheidung.

### Verwaltungsauffassung

- **OFD Frankfurt a. M., Rundverfuegung v. 26.07.2021 — S 2743 A-12-St 523, BeckVerw 556782**.
- **OFD Frankfurt a. M., Rundverfuegung v. 03.08.2018 — S 2743 A-12-St 525, DStR 2019, 560**.

### Querverweis Fachmodul

- `stb-sanierungsgewinn-stehengelassene-verbindlichkeiten` — Liquidations-Alternative zum DES, wenn Restrukturierung scheitert.

## 8. `stb-sanierungsgewinn-koerperschaftsteuer-vs-einkommensteuer`

**Fokus:** Unterschiede in der Sanierungsertragsbehandlung zwischen Körperschaftsteuer und Einkommensteuer. KSt geht über § 8 Absatz 1 KStG auf § 3a EStG; ESt direkt; unterschiedliche Verlustverrechnung und Antragsstruktur.

# Sanierungsgewinn — KSt vs. ESt

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — KSt vs. ESt` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

§ 3a EStG ist eine Norm des Einkommensteuerrechts. Über § 8 Abs. 1 KStG findet sie auch im Körperschaftsteuerrecht Anwendung. Trotz dieser Brücke gibt es im Detail Unterschiede — etwa beim Verlustvortragsregime, bei der Mindestbesteuerung, bei § 8c KStG-Risiken und beim Antragsverfahren. Dieser Skill arbeitet die Unterschiede heraus.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Ist die Schuldnerin natürliche Person, Personengesellschaft oder Kapitalgesellschaft?
2. Wer ist Antragsteller — Steuerpflichtiger der ESt (Einzelunternehmer / Mitunternehmer) oder Körperschaft?
3. Welche Verlustvorträge bestehen?
4. Gab es Anteilseignerwechsel (§ 8c, § 8d KStG bei KSt)?
5. Mehrere Wirtschaftsjahre mit Verzichten?
6. Internationale Komponente?

## Rechtlicher Rahmen

- **§ 3a EStG** — Befreiung Sanierungsertrag (ESt).
- **§ 8 Abs. 1 KStG** — Anwendung auf KSt; sinngemäße Übernahme.
- **§ 8c, § 8d KStG** — Verlustuntergang / Verschonungsregel KSt.
- **§ 10d EStG** — Verlustabzug ESt; analog für KSt.
- **§ 10a S. 1 GewStG** — Gewerbeverlust.
- **§ 7b GewStG** — Sanierungsertrag GewSt.
- **§ 11 KStG** — Liquidationsbesteuerung KSt.
- **§ 15 EStG** — Einkünfte aus Gewerbebetrieb (Personengesellschaft).
- **§ 17 EStG** — Anteile an Kapitalgesellschaften.

## / Schritt für Schritt

### KSt-Pfad

| Schritt | Inhalt |
|---|---|
| 1 | Sanierungsertrag in HB/StB der Körperschaft |
| 2 | § 3a EStG über § 8 Abs. 1 KStG anwendbar |
| 3 | Verlustvortrag § 10d EStG analog; Mindestbesteuerung |
| 4 | § 8c KStG-Risiko prüfen (Anteilseignerwechsel) |
| 5 | § 8d KStG-Verschonung bei Bedarf beantragen |
| 6 | Antrag § 3a Abs. 4 EStG mit KSt-Erklärung |
| 7 | § 7b GewStG parallel mit GewSt-Erklärung |

### ESt-Pfad (Einzelunternehmer, Mitunternehmer)

| Schritt | Inhalt |
|---|---|
| 1 | Sanierungsertrag im Betriebsvermögen des Steuerpflichtigen |
| 2 | § 3a EStG direkt anwendbar |
| 3 | Verlustvortrag § 10d EStG bei der natürlichen Person |
| 4 | Bei Personengesellschaft: Anteile je Mitunternehmer |
| 5 | Sonderbetriebsvermögen: Verzicht auf Gesellschafterdarlehen → beim Sondervermögen-Inhaber |
| 6 | Antrag § 3a Abs. 4 EStG mit ESt-Erklärung |
| 7 | § 7b GewStG mit GewSt-Erklärung der Personengesellschaft |

## Trade-off-Matrix

| Aspekt | KSt | ESt |
|---|---|---|
| Steuersatz | 15 % KSt + SolZ | progressiv bis 45 % + SolZ |
| Verlustvortrag | § 10d analog auf KSt | § 10d EStG direkt |
| Verlustuntergang Anteilseignerwechsel | § 8c KStG | bei Personengesellschaft: § 15a EStG, § 16 EStG |
| Mindestbesteuerung | § 10d Abs. 2 EStG analog | § 10d Abs. 2 EStG |
| Antrag § 3a Abs. 4 EStG | mit KSt-Erklärung | mit ESt-Erklärung |
| Bindungswirkung | gleichermaßen | gleichermaßen |
| § 7b GewStG | gleichermaßen | gleichermaßen |
| Verdeckte Einlage Gesellschafter | § 8 Abs. 3 KStG | § 4 Abs. 1 EStG |

## Praxistipps der alten Hasen

- **§ 8 Abs. 1 KStG ist die Brücke.** Die Norm § 3a EStG gilt sinngemäß für KSt; alle Voraussetzungen und Rechtsfolgen werden übernommen. Die FA-Praxis unterscheidet nicht.
- **§ 8c KStG ist die KSt-spezifische Falle.** Bei Anteilseignerwechsel kann der Verlustvortrag untergehen — vor dem Sanierungsertrag. Dann fehlt der Verbrauchsbuffer. § 8d KStG-Antrag schützt; ist aber strikt zu beantragen.
- **ESt-Progression macht Verzicht teurer.** Wenn die natürliche Person hohe Einkommen hat, ist die Steuerlast des Sanierungsertrags bei voller Steuerpflicht überproportional hoch. § 3a EStG-Antrag besonders wichtig.
- **Personengesellschaft: gemischtes Bild.** Sanierungsertrag wird auf Mitunternehmer verteilt; jeder beantragt § 3a Abs. 4 EStG individuell. Verlustverrechnung erfolgt auf Mitunternehmer-Ebene.
- **Sonderbetriebsvermögen separat.** Verzicht auf Gesellschafterdarlehen, das im Sonderbetriebsvermögen war, wird beim Mitunternehmer, nicht in der Gesamthand verbucht.

## Mustertexte / Berechnungsbeispiele

### Vergleich KSt vs. ESt — gleiche Sanierung

```
Sanierungsertrag in beiden Fällen EUR 1.500.000

Variante A: GmbH (KSt-Pfad)
 KSt-Verlustvortrag EUR 1.000.000
 Mindestbesteuerung: Sockel + 60 %
 voll nutzbar bis 1.000.000

 Sanierungsertrag - Vortrag EUR 500.000
 Antrag § 3a Abs. 4 EStG für 500.000 ► steuerfrei
 KSt + SolZ ohne Antrag: ~ EUR 79.000
 GewSt (410 % Hebesatz): ~ EUR 72.000

Variante B: Einzelunternehmer (ESt-Pfad)
 ESt-Verlustvortrag EUR 1.000.000
 Mindestbesteuerung gleich
 Sanierungsertrag - Vortrag EUR 500.000

 Antrag § 3a Abs. 4 EStG für 500.000 ► steuerfrei
 ESt-Spitzensteuersatz 42 % + SolZ
 ESt ohne Antrag: ~ EUR 220.000
 GewSt mit Anrechnung § 35 EStG: ~ EUR 72.000 (anrechenbar)

► ESt-Last ohne Antrag drastisch höher
► Antrag § 3a EStG bei ESt besonders wichtig
```

### Memo-Baustein "Variantenwahl KSt vs. ESt"

```
I. Rechtsform der Schuldnerin
[GmbH / Einzelunternehmen / KG ...]

II. Anwendbare Norm
[KSt: § 3a EStG über § 8 Abs. 1 KStG / ESt: § 3a EStG direkt]

III. Verlustvortrag
[§ 10d EStG-Vortrag EUR ...; § 8c KStG-Risiko geprüft]

IV. Antragsverfahren
Antrag mit [KSt-/ESt-]Erklärung; parallel § 7b GewStG.

V. Ergebnis
Erwartete Steuerlast nach Antrag: EUR ...
Bindungswirkung nach Feststellung: EUR ...
```

## Typische Fehler

- § 8c KStG-Untergang übersehen; Verlustvortrag schon weg, Antrag in falscher Höhe.
- Personengesellschaft pauschal behandelt; Mitunternehmer-Anteilsbetrachtung fehlt.
- ESt-Progression nicht beziffert; Mandant unterschätzt Belastung.
- § 7b GewStG vergessen — gleichgültig ob KSt oder ESt.
- Sonderbetriebsvermögen mit Gesamthand vermischt.

## Querverweise

- `stb-sanierungsgewinn-3a-estg-grundtatbestand`
- `stb-sanierungsgewinn-personengesellschaft-und-mitunternehmer`
- `stb-sanierungsgewinn-3a-estg-unternehmens-vs-person`
- `stb-sanierungsgewinn-verlustvortrag-sanity-check`
- `stb-sanierungsgewinn-3c-iv-estg-verlustreihenfolge`

## Quellen Stand 06/2026

- § 3a Abs. 1, 4 EStG.
- § 8 Abs. 1, 3 KStG.
- § 8c, § 8d KStG.
- § 10d EStG.
- § 10a S. 1 GewStG.
- § 7b GewStG.
- § 11 KStG.
- § 15, § 17 EStG.
- § 4 Abs. 1 EStG.
- BMF-Schreiben vom 27.04.2017 — Stand prüfen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; Quelle vor Ausgabe protokollieren.

## 9. `stb-sanierungsgewinn-liquidation-nachrang-fg-koeln`

**Fokus:** Solvente GmbH-Liquidation mit nachrangigem Gesellschafterdarlehen. Klaert mit der verifizierten FG-Koeln-Linie (Urteil v. 06.03.2012 — 13 K 3006/11, GmbHR 2012 Seite 977; vorgehend zu BFH I R 34/12) und mit BFH II R 19/01 die Frage, wann die Verbindlichkeit ausgebucht werden muss und ob ein etwaiger Sanierungsgewinn mangels Koerperschaftsteuersubjekt noch festsetzbar ist. Adressat ist der Steuerberater oder Rechtsanwalt, der eine GmbH ohne Insolvenz nur per Liquidation abwickeln will und ein hohes Gesellschafterdarlehen mit qualifiziertem Rangruecktritt im Bestand hat.

# Sanierungsgewinn — Liquidation, Nachrang und die FG-Koeln-Linie

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Liquidation, Nachrang und die FG-Koeln-Linie` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Eine GmbH in solventer Liquidation mit einem hohen nachrangigen Gesellschafterdarlehen wirft eine Frage auf, die § 3a EStG **nicht** beantwortet: Ist beim Loeschungszeitpunkt ein steuerpflichtiger Gewinn aus dem Wegfall der Verbindlichkeit anzunehmen, oder nicht? Antwort: Wenn die FG-Koeln-Linie greift (siehe unten), entsteht der Gewinn rechentheoretisch zwar, ist aber **mangels Koerperschaftsteuersubjekt nicht mehr festsetzbar**. § 3a EStG ist im Liquidationsfall denklogisch ohnehin schwierig — die Sanierungseignung fehlt.

Dieser Skill behandelt die Konstellation systematisch.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Mandantin ist eine GmbH (oder UG, GmbH und Co. KG mit Komplementaer-GmbH) und steht vor der Liquidation — **nicht** Insolvenz.
2. Besteht ein Gesellschafterdarlehen mit qualifiziertem Rangruecktritt? Hoehe in EUR?
3. Hat die Gesellschafterin **ausdruecklich** erklaert, dass sie verzichtet, oder will sie das Darlehen bis zur Loeschung passiviert lassen?
4. Wie ist die Rangruecktrittsklausel formuliert (Tilgung aus „freiem Vermoegen" vs. „aus zukuenftigen Gewinnen oder Liquidationsueberschuss")?
5. Welche Aktiva, welche Drittglaeubiger, welches Sperrjahr-Datum?
6. Gibt es nennenswerte Verlustvortraege?

## Rechtlicher Rahmen

- **§ 60 Abs. 1 Nr. 2 GmbHG** — Aufloesungsbeschluss durch Gesellschafter.
- **§ 65 GmbHG** — Bekanntmachung und Glaeubigeraufruf.
- **§ 71 GmbHG** — Liquidations-Eroeffnungsbilanz, Schlussbilanz.
- **§ 73 GmbHG** — Sperrjahr und Verteilungsverbot.
- **§ 74 GmbHG** — Loeschung im Handelsregister und Vollbeendigung.
- **§ 1 KStG, § 11 KStG** — Liquidationsbesteuerung Koerperschaft.
- **§ 5 Abs. 2a EStG** — Passivierungsverbot bei „nur aus zukuenftigen Gewinnen oder einem etwaigen Liquidationsueberschuss" tilgbaren Verbindlichkeiten.
- **§ 3a EStG, § 3a Abs. 2 EStG** — Sanierungsbefreiung; Sanierungseignung bei Liquidation fraglich.
- **§ 17 EStG, § 17 Abs. 4 EStG** — Aufloesungsverlust und nachtraegliche Anschaffungskosten auf Gesellschafterebene.
- **§ 397 BGB** — Erlassvertrag.

### Verifizierte Rechtsprechung

- **FG Koeln, Urteil v. 06.03.2012 — 13 K 3006/11**, GmbHR 2012, 977 (vorgehend zu BFH I R 34/12 — Verpflichtungsklage auf verbindliche Auskunft, in Folge des FG-Urteils). Os. 7 woertlich:

> „Ist ausgeschlossen, dass ein GmbH-Gesellschafter die mit einer Rangruecktrittserklaerung verbundenen Darlehensforderungen gegenueber der GmbH erlassen wird, kann bei der Liquidation der GmbH der Verzicht nicht unterstellt und ein steuerpflichtiger Gewinn angenommen werden. Die Verbindlichkeit ist bis zum Abschluss der Liquidation, d.h. bis zur Loeschung im Handelsregister als Verbindlichkeit auszuweisen. Mit dem Erloeschen der GmbH erloeschen neben den Verbindlichkeiten auch eventuelle Verlustvortraege. Der dadurch rechtstheoretisch entstehende Gewinn ist mangels Koerperschaftsteuersubjekt nicht mehr steuerpflichtig."

- **BFH, Urteil v. 26.02.2003 — II R 19/01** — Verbindlichkeiten entfallen nicht allein durch Vermoegenslosigkeit oder Aufloesungsbeschluss.
- **BFH, Urteil v. 30.11.2011 — I R 100/10** — § 5 Abs. 2a EStG bei qualifiziertem Rangruecktritt (Abgrenzung).
- **OFD Frankfurt a. M.** — Verfuegung mit der Aussage, dass der blosse Liquidationsbeschluss kein konkludenter Forderungsverzicht ist (Aktualitaet vor Anwendung pruefen).

## / Schritt fuer Schritt

| Schritt | Inhalt | Output |
|---|---|---|
| 1 | Sachverhalt sauber erfassen: GmbH solvent? Drittglaeubiger gedeckt? Nachrangiges Darlehen? | Sachverhaltsblatt |
| 2 | Wortlaut der Rangruecktrittsklausel pruefen: „freies Vermoegen" oder „nur aus zukuenftigen Gewinnen"? | Klausel-Memo |
| 3 | § 5 Abs. 2a EStG-Falle pruefen: Bei „nur aus zukuenftigen Gewinnen"-Klauseln greift Passivierungsverbot — Ausbuchung waehrend der Liquidation noch bei fortbestehendem Steuersubjekt | Pruefvermerk |
| 4 | Wenn Klausel sauber (freies Vermoegen): FG-Koeln-Linie tragend | Memo Szenario A |
| 5 | Sanierungseignung § 3a EStG pruefen — fehlt regelmaessig bei Liquidation | Negativbefund |
| 6 | § 17 Abs. 4 EStG-Aufloesungsverlust auf Gesellschafterebene parallel pruefen | Spiegel-Memo |
| 7 | Verbindliche Auskunft § 89 Abs. 2 AO beim FA pruefen | Antragsentwurf |
| 8 | Liquidations-Eroeffnungsbilanz und Schlussbilanz vorbereiten | Bilanzentwurf |
| 9 | Loeschungsantrag beim Handelsregister nach Sperrjahr | Anmeldung HR |

## Trade-off-Matrix

| Strategie | Wirkung | Risiko |
|---|---|---|
| A — Darlehen bleibt passiviert bis Loeschung | Steuerausfall nach FG Koeln 13 K 3006/11 (mangels Subjekt) | § 5 Abs. 2a EStG-Falle bei unsauberer Klausel |
| B — Ausbuchung in Liquidations-Eroeffnungsbilanz | Sanierungsertrag entsteht bei fortbestehender GmbH | § 3a EStG kaum anwendbar — Sanierungseignung fehlt; voll steuerpflichtig |
| C — Ausdruecklicher Verzicht durch Gesellschafterin (§ 397 BGB) | Sofortige Ausbuchung, klare Verhaeltnisse | Sanierungsertrag voll steuerpflichtig; § 17 EStG-Spiegel wahrnehmen |
| D — Insolvenzverfahren statt Liquidation | § 3a EStG eher anwendbar | Insolvenzverfahrenkosten, Reputationsrisiko |

## Praxistipps der alten Hasen

- **Klauselwortlaut entscheidet ueber alles.** Eine reine „Tilgung-nur-aus-zukuenftigen-Gewinnen"-Klausel reisst die GmbH in § 5 Abs. 2a EStG hinein — Ausbuchung **vor** Loeschung mit voller Steuerlast bei der lebenden GmbH. Sauber formulieren: „Tilgung aus freiem Vermoegen" (BFH I R 100/10 zur Abgrenzung).
- **§ 3a EStG nicht reflexartig bemuehen.** Bei einer Liquidation fehlt die Sanierungseignung. Wer den Antrag § 3a Abs. 4 EStG dennoch stellt, riskiert ein Ablehnungsbescheid des FA und unnoetigen Streit. Lieber die FG-Koeln-Linie und § 17 Abs. 4 EStG-Spiegel argumentieren.
- **Aktualitaet der OFD-Frankfurt-Verfuegung pruefen.** Vor der Antragstellung beim FA klaeren, ob die Verfuegung noch gilt — manche Bundeslaender weichen ab.
- **Verbindliche Auskunft erspart Streit.** Bei Volumen ab ca. 1 Mio EUR Darlehensbestand lohnt der § 89 Abs. 2 AO-Antrag. Vorlaufzeit FA: drei bis sechs Monate; rechtzeitig vor Loeschungsantrag stellen.
- **§ 17 Abs. 4 EStG nicht vergessen.** Auf Ebene der Gesellschafterin ist der Aufloesungsverlust geltend zu machen, sofern Darlehensverlust als nachtraegliche Anschaffungskosten zu beruecksichtigen ist (zu den Grenzen siehe staend. Rspr. zu „eigenkapitalersetzenden Darlehen" / BMF-Schreiben).

## Quellenpflicht

Verbindliche Zitierweise: `references/zitierweise.md`. Die FG-Koeln-Fundstelle und die BFH-Linie sind in jedem Memo, Antrag und Mandantenbrief mit Gericht, Datum, Aktenzeichen, Fundstelle und ggf. Randnummer zu nennen. Os. 7 von 13 K 3006/11 ist woertlich zitierfaehig (s. oben).

## Ausgabeformat

- Memo im Gutachtenstil: Sachverhalt knapp; Frage; Kurzantwort; Subsumtion; Gesamtergebnis; Risiken; Quellenverzeichnis.
- Querverweise auf die Akten 05 (Rangruecktritt), 06 (§ 5 Abs. 2a EStG), 07 (BFH II R 19/01), 08 (Szenario A), 16 (FG Koeln) der Test-Akte Strassburger Handelshof — soweit das Mandat parallel laeuft.

## Beispiele

### Beispiel 1 — Klauselwortlaut sauber, Strategie A

GmbH solvent, Darlehen 2,4 Mio EUR mit Rangruecktritt „Tilgung aus freiem Vermoegen". Drittglaeubiger gedeckt. Strategie A: Passivierung bis Loeschung. Ergebnis: kein festsetzbarer Sanierungsgewinn nach FG Koeln 13 K 3006/11. § 17 Abs. 4 EStG-Aufloesungsverlust bei Gesellschafterin nach Massgabe der nachtraeglichen Anschaffungskosten-Linie.

### Beispiel 2 — Klauselwortlaut unsauber, § 5 Abs. 2a EStG greift

GmbH solvent, Darlehen 2,4 Mio EUR mit Rangruecktritt „Tilgung nur aus zukuenftigen Gewinnen". Folge: Passivierungsverbot greift in der Liquidations-Eroeffnungsbilanz. Sanierungsertrag entsteht bei fortbestehender GmbH. § 3a EStG nicht anwendbar (Sanierungseignung fehlt). Voll steuerpflichtig, KSt + GewSt. Mandantenwarnung erforderlich — Klausel haette frueh saniert werden muessen.

### Beispiel 3 — Ausdruecklicher Verzicht durch Gesellschafterin

GmbH solvent, Darlehen 2,4 Mio EUR, Gesellschafterin erklaert ausdruecklich Verzicht (§ 397 BGB). Folge: Sofortige Ausbuchung mit Sanierungsertrag in der Periode des Verzichts; § 3a EStG nicht anwendbar (Liquidation). Voll steuerpflichtig bei der GmbH; auf Gesellschafterebene § 17 Abs. 4 EStG-Spiegel.

## Typische Fehler

- Reflexartig § 3a EStG-Antrag gestellt — Sanierungseignung in Liquidation kaum darstellbar; Ablehnung erwartbar.
- Klauseltext nicht im Originalwortlaut geprueft; nur Etikett "qualifizierter Rangruecktritt" verwendet.
- BFH-Revisionsstand nicht aktualisiert; veraltete Argumentation.
- Liquidator versaeumt Steuererklaerung Abwicklungszeitraum (§ 11 KStG) — § 69 AO-Haftung.
- § 17 Abs. 4 EStG-Spiegel auf Gesellschafterebene nicht parallel geltend gemacht.

## Praxistipps der alten Hasen — Ergaenzung

- **Verbindliche Auskunft § 89 AO mit FG-Koeln-Bezug.** Wenn das FA der Linie folgt, wird der Antrag haeufig positiv beschieden; aktuelle OFD-Verfuegungen vorab pruefen.
- **Sperrjahr ausnutzen.** Das Sperrjahr nach § 73 GmbHG (mindestens 1 Jahr nach Bekanntmachung des Glaeubigeraufrufs) gibt Zeit, die Strategie zu finalisieren.
- **Loeschungsantrag erst nach Steuerakte.** Vor Loeschung sollten die FA-Verfahren abgeschlossen oder die Bescheide bestandskraeftig sein, um die Vollbeendigung nicht zu blockieren.

## Querverweise

- `stb-sanierungsgewinn-3a-estg-grundtatbestand`
- `stb-sanierungsgewinn-3a-estg-unternehmens-vs-person`
- `stb-sanierungsgewinn-rangruecktritt-und-5-abs-2a-estg`
- `stb-sanierungsgewinn-vermeidungsstrategien-praxis`
- `stb-sanierungsgewinn-forderungsverzicht-bilanzielle-darstellung`
- `insol-sanierungsgewinn-liquidation-statt-plan-folgen`
- `gk-sanierungsgewinn-forderungsverzicht-vs-mantelkauf-8c-kstg`

## Quellen Stand 06/2026

- **FG Koeln, Urteil v. 06.03.2012 — 13 K 3006/11, GmbHR 2012, 977** (vorgehend zu BFH I R 34/12). Os. 7 woertlich oben zitiert.
- BFH, Urteil v. 26.02.2003 — II R 19/01.
- BFH, Urteil v. 30.11.2011 — I R 100/10 (zu § 5 Abs. 2a EStG bei qualifiziertem Rangruecktritt).
- OFD Frankfurt a. M., Verfuegung (Aktualitaet vor Anwendung pruefen).
- §§ 60, 65, 71, 73, 74 GmbHG; § 1 KStG, § 11 KStG; § 5 Abs. 2a EStG; § 3a EStG; § 17 EStG; § 397 BGB.
- Verbindliche Zitierweise: `references/zitierweise.md`.
