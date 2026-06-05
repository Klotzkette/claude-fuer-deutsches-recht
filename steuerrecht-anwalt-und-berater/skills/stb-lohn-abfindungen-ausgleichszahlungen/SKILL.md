---
name: stb-lohn-abfindungen-ausgleichszahlungen
description: "STB Lohn Abfindungen Ausgleichszahlungen: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# STB Lohn Abfindungen Ausgleichszahlungen

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **STB Lohn Abfindungen Ausgleichszahlungen** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stb-lohn-abfindungen-besteuerung-funftel-regel` | Abfindungen Besteuerung Fuenftel-Regelung § 34 EStG. Anwendungsfall Aufhebungsvertrag Kündigung mit Abfindung Prüfung Voraussetzungen Fuenftel-Regel Berechnung Vorteilsvergleich. Methodik Berechnung mit DATEV LODAS. Output Lohn-Abrechnung Abfindung mit ermäßigter Besteuerung. |
| `stb-lohn-ausgleichszahlungen-altersteilzeit` | Altersteilzeit Block-Modell Gleichverteilungsmodell Aufstockungsbetrag. Anwendungsfall AN-Antrag Altersteilzeit ab 55 Block-/Gleichverteilungs-Variante AG-Aufstockung 20 Prozent steuerfrei. Methodik Prüfung AltTZG Berechnung. Output Altersteilzeit-Vereinbarung Lohn-Abrechnung. |
| `stb-lohn-betriebliche-altersversorgung-grundlagen` | Betriebliche Altersversorgung bAV Grundlagen Durchführungswege. Anwendungsfall Beratung Mandant zu bAV Direktversicherung Pensionskasse Pensionsfonds Direktzusage Unterstuetzungskasse steuerliche und SV-rechtliche Behandlung. Methodik Vergleich Wege Foerderung. Output bAV-Beratungs-Notiz. |
| `stb-lohn-dienstwagen-1-prozent-fahrtenbuch` | Dienstwagen 1-Prozent-Methode oder Fahrtenbuch. Anwendungsfall geldwerter Vorteil Privatnutzung Dienstwagen E-Auto Hybrid Listenpreis Brutto-Methode. Methodik Prüfung Methode Vergleich Steuerklasse. Output Lohn-Abrechnung mit korrektem Sachbezug Dienstwagen. |
| `stb-lohn-direktversicherung-3-nr-63-estg` | Direktversicherung Steuerfreiheit § 3 Nr 63 EStG bis 8 Prozent BBG SV-frei bis 4 Prozent BBG. Anwendungsfall Entgeltumwandlung Direktversicherung Konfiguration Mandant AG-Zuschuss 15 Prozent. Methodik Beitragsberechnung Beitragsbemessung Auswirkung Netto. Output Lohn-Konfiguration mit Direktversicherung. |
| `stb-lohn-elternzeit-mutterschutz` | Elternzeit Mutterschutz Mutterschaftsgeld Elterngeld lohnrelevant. Anwendungsfall AN-Schwangerschaft Geburt Antrag Mutterschutz Elternzeit Auswirkung auf Lohn SV-Status Steuerprogression. Methodik Prüfung MuschG Beschaeftigungsverbot BEEG. Output Lohn-Abrechnung Elternzeit Bescheinigung. |
| `stb-lohn-firmenrad-leasing-jobrad` | JobRad Dienstrad Leasingmodell steuerliche Behandlung. Anwendungsfall AG-Leasing eines Fahrrads oder E-Bikes Überlassung an AN durch Gehaltsumwandlung Sachbezug von einem Viertel Prozent. Methodik Prüfung Konfiguration Leasingvertrag. Output Lohn-Abrechnung mit JobRad. |
| `stb-lohn-jahresmeldungen-ahn-asn-besondere` | Jahresmeldungen DEUEV Jahreslohnsumme Abmelde- und Sondermeldungen. Anwendungsfall Jahresende-Meldungen 15. Februar Folgejahr AN-Jahresarbeitsentgelt-Meldung Sondermeldungen Lohnsteuerbescheinigung. Methodik Standardablauf. Output Jahresmeldungen Bescheinigungen. |
| `stb-lohn-jobticket-mobilitaet-deutschlandticket` | Jobticket Deutschlandticket steuerliche Behandlung. Anwendungsfall AG erstattet AN Mobilitaetsticket OePNV oder bietet Jobticket steuerfrei nach § 3 Nr 15 EStG Auswirkung auf Entfernungspauschale. Methodik Prüfung Konfiguration. Output Lohn-Abrechnung mit Jobticket. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **STB Lohn Abfindungen Ausgleichszahlungen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stb-lohn-abfindungen-besteuerung-funftel-regel`

**Fokus:** Abfindungen Besteuerung Fuenftel-Regelung § 34 EStG. Anwendungsfall Aufhebungsvertrag Kündigung mit Abfindung Prüfung Voraussetzungen Fuenftel-Regel Berechnung Vorteilsvergleich. Methodik Berechnung mit DATEV LODAS. Output Lohn-Abrechnung Abfindung mit ermäßigter Besteuerung.

# Abfindungen — Besteuerung mit Fuenftel-Regelung § 34 EStG

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Abfindungen — Besteuerung mit Fuenftel-Regelung § 34 EStG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Abfindungen aus Anlass der Beendigung des Arbeitsverhaeltnisses sind aussergewoehnliche Einkuenfte (§ 24 Nr. 1 EStG) und unterliegen der ermaessigten Besteuerung nach § 34 EStG (Fuenftel-Regelung). Voraussetzungen: Zusammenballung der Einkuenfte in einem Veranlagungszeitraum, gesetzlich oder vertraglich vereinbart. SV-rechtlich sind Abfindungen aus echtem Schadensersatz-Charakter SV-frei.

## Kaltstart-Rueckfragen

1. Liegt Aufhebungsvertrag, Kuendigung oder gerichtlicher Vergleich vor?
2. Welche Abfindungshoehe?
3. Wird die Abfindung in einem Jahr ausgezahlt (Zusammenballung)?
4. Welcher Bruttolohn des AN im Vorjahr und im Jahr der Auszahlung?
5. Welches Alter des AN, welche Beschaeftigungsdauer (Aufstockungs-Pauschale)?
6. Erfolgt die Abfindung ausschliesslich oder mit weiteren Komponenten (offene Loehne, Urlaubsabgeltung)?
7. Wird die Abfindung als Zahlungsersatz fuer entgangene Loehne gestaltet (SV-Pflicht-Risiko)?
8. AG-Wunsch — Auszahlung im Folgejahr (Steueroptimierung)?

## Rechtlicher Rahmen

### Primaernormen

**§ 24 Nr. 1 EStG** — aussergewoehnliche Einkuenfte Entschaedigungen.

**§ 34 Abs. 1, 2 EStG** — Fuenftel-Regelung.

**§ 19 EStG** — Einkuenfte nichtselbstaendige Arbeit.

**§ 14 SGB IV** — Arbeitsentgelt.

**SvEV § 1 Abs. 1 Nr. 16** — SV-Behandlung Abfindungen.

### Leitentscheidungen (Aktenzeichen vor Uebernahme in amtliche/freie Quellen oder lizenzierte Datenbanken pruefen)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BSG-Linie zu echter vs. unechter Abfindung im SV-Recht: vor Uebernahme aktuelle Entscheidungen in freier amtlicher Quelle pruefen.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Workflow

### Phase 1 — Voraussetzungen Fuenftel-Regelung

| Voraussetzung | Pruefung |
|---|---|
| Aussergewoehnliche Einkuenfte (Entschaedigung) | Aus Vertrag/Vergleich erkennbar |
| Zusammenballung in einem Veranlagungszeitraum | Auszahlung in einem Jahr |
| Steuerlich kann Auszahlung in einem Veranlagungsjahr erfolgen | ggf. Verschiebung in Folgejahr besser |

### Phase 2 — Berechnung Fuenftel-Regelung

```
Schritt 1: Jahres-Steuer mit Abfindung berechnen
Schritt 2: Jahres-Steuer ohne Abfindung berechnen
Schritt 3: Differenz aus Schritt 1 minus Schritt 2 = Steuer auf Abfindung mit Standardtabelle
Schritt 4: Differenz x 5 = ermaessigte Steuer auf Abfindung
```

Die Fuenftel-Regelung mindert die Steuerprogression — bei vollstaendiger Wirkung Steuerersparnis 15-30 Prozent.

### Phase 3 — SV-Behandlung

- Echte Abfindung (Schadensersatz fuer Verlust des Arbeitsplatzes): SV-frei.
- Unechte Abfindung (Lohnnachzahlung): SV-pflichtig.
- Pruefung Vereinbarung — wenn als "Entschaedigung wegen Verlust des Arbeitsplatzes" formuliert: SV-frei.

### Phase 4 — Steuerklassenoptimierung

- Bei Auszahlung im selben Jahr wie Kuendigung: Steuerklasse beachten.
- Bei Wechsel im Jahr (z.B. EhepartnerIn-Wahl 3/5 vs. 4/4): rechtzeitig pruefen.
- Vorausschau auf zu versteuerndes Einkommen.

### Phase 5 — Auszahlung im Folgejahr

- Wenn AN im Folgejahr arbeitslos: niedrigeres ZvE; Fuenftel-Wirkung staerker.
- Bei Verschiebung Vereinbarungsbasis: Aufhebungsvertrag mit Auszahlungstermin Januar Folgejahr.
- AG-Risiko: Insolvenz vor Auszahlung — Mandant pruefen.

### Phase 6 — Lohnabrechnung

- DATEV LODAS: Abfindung mit Lohnart "Sonstige Bezuege ermaessigt" buchen.
- Achtung Reform: Mit dem Wachstumschancengesetz wurde der Lohnsteuer-Abzug der Fuenftel-Regelung im Lohnsteuer-Verfahren ab 2025 gestrichen (Verifikation 2026 ueber aktuelles BMF-Schreiben zur Lohnsteuer-Ermittlung); seither erfolgt die Fuenftel-Anwendung nur noch in der Veranlagung beim AN. AG sollte AN zur Einkommensteuererklaerung anhalten.
- LSt-Bescheinigung in Zeile 10 ("Ermaessigt besteuerter Arbeitslohn fuer mehrere Jahre") — gilt fuer die Zuordnung zur Kennzahl; konkretes Feld bei jedem LSt-Update pruefen (Bescheinigungsmuster BMF).

## Output

- Lohn-Abrechnung mit ermaessigter Besteuerung.
- LSt-Bescheinigung Zeile 10.
- Beratungsnotiz zu Auszahlungs-Optimierung.

## Strategie und Praxis-Tipps

- Verschiebung in Folgejahr fast immer steuerlich vorteilhaft, wenn AN im Folgejahr weniger verdient.
- Aufstockungs-Abfindung: AG zahlt mehr aus, um Netto zu erhoehen — Beratung sinnvoll.
- Bei laufendem Lohn bis Beendigung + Abfindung: Aufteilung pruefen (laufender Lohn keine Fuenftel-Regelung).
- SV-Frei nur bei echter Entschaedigung — schon im Aufhebungsvertrag korrekt formulieren.
- StBVV: Sonderlohn-Berechnung Zeithonorar oder Pauschale.
- DATEV-Tipp: DATEV LODAS Lohnart "Ermaessigte Besteuerung" mit automatischer Fuenftel-Berechnung.

## Querverweise

- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.
- `stb-lohn-lohnsteuer-monatsabschluss` — Monatsabschluss.
- `stb-lohn-sv-beitraege-grundlagen` — SV.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 19, 24 Nr. 1, 34.
- SGB IV § 14.
- SvEV § 1.
- BFH-Linie zur Zusammenballung der Einkuenfte (stetige Rechtsprechung, vgl. Schmidt/EStG, Blumich/EStG zu § 34 EStG; konkrete Aktenzeichen vor Uebernahme in amtliche/freie Quellen oder lizenzierte Datenbanken pruefen).
- BSG-Linie zur SV-Einordnung echter vs. unechter Abfindungen (aktuelle Entscheidungen vor Uebernahme in freier amtlicher Quelle pruefen).
- Wachstumschancengesetz vom 27.03.2024 (BGBl. 2024 I Nr. 108): Streichung der Fuenftel-Regelung im Lohnsteuer-Abzugsverfahren ab dem Veranlagungszeitraum 2025; Anwendung der Fuenftel-Regelung nur noch in der Veranlagung beim AN.

<!-- AUDIT 27.05.2026 | welle 6 | 4 Marker aufgeloest: 0 bestaetigt (Fundstelle/Datum), 4 ersetzt (Hinweis auf Pruefung in amtliche/freie Quellen oder lizenzierte Datenbanken neu formuliert) -->

## 2. `stb-lohn-ausgleichszahlungen-altersteilzeit`

**Fokus:** Altersteilzeit Block-Modell Gleichverteilungsmodell Aufstockungsbetrag. Anwendungsfall AN-Antrag Altersteilzeit ab 55 Block-/Gleichverteilungs-Variante AG-Aufstockung 20 Prozent steuerfrei. Methodik Prüfung AltTZG Berechnung. Output Altersteilzeit-Vereinbarung Lohn-Abrechnung.

# Altersteilzeit — Block- und Gleichverteilungsmodell

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Altersteilzeit — Block- und Gleichverteilungsmodell` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die Altersteilzeit ermoeglicht AN ab 55 Jahren eine Reduzierung der Arbeitszeit auf die Haelfte. Zwei Modelle: Gleichverteilungsmodell (halftige Stunden ueber die gesamte Laufzeit) oder Blockmodell (Vollzeit-Arbeitsphase + Vollzeit-Freistellungsphase). AG zahlt halftiges Gehalt plus Aufstockungsbetrag (mind. 20 Prozent des Regelgehalts; insgesamt ca. 70 Prozent des frueheren Nettos). Steuerlich teilweise gefoerdert (§ 3 Nr. 28 EStG), SV-rechtlich besondere Behandlung. Hinweis: Die BA-Foerderung der Altersteilzeit (§ 4 AltTZG) ist seit 31.12.2009 ausgelaufen; Altersteilzeit existiert aber als tarifvertragliche oder einzelvertragliche Gestaltung weiter. AltTZG bleibt als steuerlich-sozialversicherungsrechtlicher Rahmen wirksam.

## Kaltstart-Rueckfragen

1. Erfuellt der AN das Alter (mind. 55 Jahre)?
2. Welches Modell — Blockmodell oder Gleichverteilungsmodell?
3. Welche Laufzeit?
4. Liegt schriftliche Altersteilzeit-Vereinbarung vor?
5. Welche Aufstockungsbetraege (mind. AltTZG, ggf. tariflich mehr)?
6. Welche Wertguthaben-Vereinbarung im Blockmodell (Insolvenzsicherung)?
7. Wird das Wertguthaben in der Arbeitsphase angesammelt und in der Freistellungsphase abgebaut?
8. Plant AN nach Altersteilzeit Renteneintritt?

## Rechtlicher Rahmen

### Primaernormen

**AltTZG** — Altersteilzeitgesetz.

**§ 2 AltTZG** — Voraussetzungen.

**§ 3 AltTZG** — Aufstockungsbetrag.

**§ 3 Nr. 28 EStG** — Steuerfreiheit Aufstockungsbetrag.

**§ 1 SvEV** — SV-Behandlung Aufstockungsbetrag.

**§ 7c, 7d SGB IV** — Wertguthabenvereinbarungen.

**§ 8a SGB IV** — Insolvenzsicherung Wertguthaben.

### Verwaltungsanweisungen

- BMAS Rundschreiben zur Altersteilzeit.
- BFH zur Steuerbehandlung.

## Workflow

### Phase 1 — Voraussetzungen

| Voraussetzung | Pruefung |
|---|---|
| Alter mind. 55 Jahre | Geburtsdatum |
| Beschaeftigungsdauer im Betrieb | Arbeitsvertrag |
| Reduzierung auf 50 Prozent | Vereinbarung |
| Vereinbarung schriftlich | Vertrag liegt vor |
| Insolvenzsicherung Wertguthaben | Bei Blockmodell zwingend |

### Phase 2 — Berechnung Aufstockungsbetrag

- Mindestaufstockung: 20 Prozent des Brutto-Regelarbeitsentgelts (vom Stand vor Altersteilzeit).
- Optionale tarifliche Aufstockung hoeher.
- Aufstockung steuerfrei (§ 3 Nr. 28 EStG) bis Hoechstbetrag.
- Aufstockung SV-pflichtig nur in bestimmten Grenzen.

### Phase 3 — Blockmodell

- Arbeitsphase (z.B. 5 Jahre Vollzeit): halbe Bezahlung; andere Haelfte wandert in Wertguthaben.
- Freistellungsphase (z.B. 5 Jahre Freistellung): Auszahlung aus Wertguthaben + Aufstockungsbetrag.
- Wertguthaben muss insolvenzgesichert sein (§ 8a SGB IV).

### Phase 4 — Gleichverteilungsmodell

- Halbtags-Arbeit ueber gesamte Laufzeit.
- Halbtags-Lohn + Aufstockungsbetrag laufend.
- Keine Wertguthaben-Bildung.

### Phase 5 — Lohnabrechnung

- Reduziertes Brutto: halbtags.
- Aufstockungsbetrag: in DATEV LODAS als Lohnart "Altersteilzeit-Aufstockung".
- LSt-frei nach § 3 Nr. 28 EStG.
- SV-Behandlung: Sondervorschriften AltTZG; Beitrag wird ggf. zur RV-Anwartschaft aufgestockt (AG-Sonderbeitrag).

### Phase 6 — Renteneintritt

- Nach Altersteilzeit oft direkter Renteneintritt mit 63 (vorgezogene Altersrente).
- Pruefung Rentenabschlag.
- DRV-Beratung empfehlen.

## Output

- Altersteilzeit-Vereinbarung.
- Wertguthaben-Konto im DATEV LODAS.
- Lohn-Abrechnung mit Aufstockungsbetrag.

## Strategie und Praxis-Tipps

- Blockmodell ist haeufiger — AN arbeitet voll, dann frei.
- Wertguthaben-Insolvenzsicherung ist KRITISCH — § 8a SGB IV.
- Aufstockungsbetrag steuerfrei, aber Progressionsvorbehalt § 32b EStG einbeziehen.
- AG-Sonderbeitrag zur RV-Anwartschaft (zusaetzlich): in vielen Faellen Pflicht (Mindestaufstockung).
- StBVV: Altersteilzeit-Beratung Zusatzauftrag (Komplex, einmalig).
- DATEV-Tipp: DATEV LODAS Altersteilzeit-Modul mit Wertguthaben-Konto.

## Querverweise

- `stb-lohn-ueberstunden-abbau-arbeitszeitkonto` — Arbeitszeitkonto.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-betriebliche-altersversorgung-grundlagen` — bAV.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.

## Quellen und Updates

Stand: 05/2026.

- AltTZG §§ 2, 3.
- EStG §§ 3 Nr. 28, 32b.
- SGB IV §§ 7c, 7d, 8a.
- SvEV § 1.
- BMAS Rundschreiben.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `stb-lohn-betriebliche-altersversorgung-grundlagen`

**Fokus:** Betriebliche Altersversorgung bAV Grundlagen Durchführungswege. Anwendungsfall Beratung Mandant zu bAV Direktversicherung Pensionskasse Pensionsfonds Direktzusage Unterstuetzungskasse steuerliche und SV-rechtliche Behandlung. Methodik Vergleich Wege Foerderung. Output bAV-Beratungs-Notiz.

# Betriebliche Altersversorgung (bAV) — Grundlagen

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Betriebliche Altersversorgung (bAV) — Grundlagen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die betriebliche Altersversorgung (bAV) ist eine vom AG zugesagte Versorgungsleistung zugunsten des AN, die zusaetzlich zur gesetzlichen RV traegt. Funf Durchfuehrungswege (BetrAVG): Direktzusage, Unterstuetzungskasse, Direktversicherung, Pensionskasse, Pensionsfonds. Steuerliche Foerderung ueber § 3 Nr. 63 EStG (bis 8 Prozent BBG steuerfrei, bis 4 Prozent BBG SV-frei) sowie § 100 EStG (Foerderung Geringverdiener). Pflicht: AG-Zuschuss zur Entgeltumwandlung 15 Prozent nach BRSG.

## Kaltstart-Rueckfragen

1. Welcher Durchfuehrungsweg ist gewuenscht oder bereits eingerichtet?
2. Erfolgt die bAV durch Entgeltumwandlung (AN-finanziert) oder AG-finanziert?
3. Welche Beitragshoehe pro Monat?
4. Liegt eine Versorgungszusage vor (Vertragstext)?
5. Welche Steuerklasse hat der AN? (Geringverdiener-Foerderung § 100 EStG bei Niedriglohn)
6. Wann erfolgt der Renteneintritt des AN (Pruefung Vertragslaufzeit)?
7. Welche Mitarbeiterzahl im Betrieb (BAVAG-Beratungspflichten)?
8. Welche bAV-Tarifvertraege (z.B. Metall- und Elektroindustrie) sind anwendbar?

## Rechtlicher Rahmen

### Primaernormen

**BetrAVG** — Betriebsrentengesetz.

**§ 1 BetrAVG** — Zusagearten.

**§ 1a BetrAVG** — Anspruch Entgeltumwandlung; 15-Prozent-Zuschuss-Pflicht AG.

**§ 3 Nr. 63 EStG** — Steuerfreiheit Direktversicherung/Pensionskasse/Pensionsfonds bis 8 Prozent BBG.

**§ 100 EStG** — Foerderung Geringverdiener (Hochstgehalt ueber bAV-Beitrag).

**§ 19 EStG** — Versorgungsbezuege in Auszahlungsphase.

**§ 1 Abs. 1 Nr. 9 SvEV** — SV-Freiheit bAV-Beitraege bis 4 Prozent BBG-West RV (kumuliert).

**BRSG (Betriebsrentenstaerkungsgesetz)** — Reform 2018, weitere Anpassungen.

### Verwaltungsanweisungen

- BMF v. 06.12.2017 zur bAV-Reform.
- BMF v. 18.03.2022.
- DSV Rundschreiben.

## Workflow

### Phase 1 — Durchfuehrungsweg-Wahl

| Weg | Charakter | Steuer (Ansparphase) | SV (Ansparphase) | Auszahlung |
|---|---|---|---|---|
| Direktversicherung | Versicherungsvertrag AG zu Versicherer | Bis 8 Prozent BBG steuerfrei (§ 3 Nr. 63 EStG) | Bis 4 Prozent BBG SV-frei | Voll lohnsteuerpflichtig in Auszahlung |
| Pensionskasse | Sondervermoegen ueber Pensionskasse | Wie Direktversicherung | Wie Direktversicherung | Wie Direktversicherung |
| Pensionsfonds | Kapitalmarktorientiert | Wie Direktversicherung | Wie Direktversicherung | Wie Direktversicherung |
| Direktzusage | AG-eigene Versorgungszusage | Bei Auszahlung lohnsteuerpflichtig | SV-frei (bis BBG bei Auszahlung) | Voll lohnsteuerpflichtig |
| Unterstuetzungskasse | Eigene rechtsfaehige Kasse | Wie Direktzusage | Wie Direktzusage | Wie Direktzusage |

### Phase 2 — Steuerliche Foerderung § 3 Nr. 63 EStG

- Bis 8 Prozent der RV-BBG (West) steuerfrei.
- Davon bis 4 Prozent BBG zusaetzlich SV-frei.
- BBG-West RV 2025: 96.600 EUR/Jahr; 8 Prozent = 7.728 EUR steuerfrei, 4 Prozent = 3.864 EUR SV-frei (Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen).
- AN-Vorteil: niedrigeres Brutto in Ansparphase, hoehere Rente.

### Phase 3 — § 100 EStG Geringverdiener-Foerderung

- AG kann fuer AN mit Bruttolohn unter Schwellenwert (§ 100 Abs. 3 Nr. 3 EStG: 2.575 EUR/Monat seit dem Grundrentengesetz 2020; Schwellenwert wird nicht automatisch angepasst, bei Gesetzesaenderung pruefen) BAV-Foerderbetrag erhalten.
- Foerderbetrag: 30 Prozent des AG-Beitrags (max. 288 EUR/Jahr je AN — Stand 2025, § 100 Abs. 1 EStG; BMF-Schreiben zu § 100 EStG pruefen).
- AG verrechnet Foerderung mit abzufuehrender LSt in der LSt-Anmeldung.

### Phase 4 — § 1a BetrAVG 15-Prozent-Zuschuss

- Bei Entgeltumwandlung in Direktversicherung/Pensionskasse/Pensionsfonds: AG-Zuschuss-Pflicht 15 Prozent.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Geltung: fuer ab 2019 abgeschlossene Vereinbarungen (Bestand seit 2022).

### Phase 5 — Auszahlungsphase

- bAV-Renten lohnsteuerpflichtig in voller Hoehe (nachgelagerte Besteuerung).
- KV/PV-Pflicht in der Auszahlungsphase (Freibetrag fuer Pflichtversicherte Rentner nach § 226 Abs. 2 SGB V; aktueller Freibetrag ueber GKV-Spitzenverband pruefen).
- Sondersituation pauschal versteuerte Direktversicherung (§ 40b EStG a.F.): Auszahlung ggf. nicht voll steuerpflichtig (Altvertraege bis 2004).

### Phase 6 — Beratung Mandant

- Vergleich Durchfuehrungswege mit Mandant.
- Bei kleinen Mandanten oft Direktversicherung praktisch (kein eigener Pensionsverwaltungs-Aufwand).
- Bei Konzernen Pensionsfonds oder Direktzusage moeglich.
- Vertragstext mit Rechtsanwalt pruefen lassen.

## Output

- Beratungsnotiz zu bAV-Durchfuehrungsweg.
- Konfiguration in DATEV LODAS / Lohn und Gehalt.
- Versorgungszusage-Vertrag.

## Strategie und Praxis-Tipps

- Direktversicherung ist Standard fuer kleine Mandanten — wenig Aufwand, klare Foerderung.
- 4-Prozent-Grenze SV-Frei genau pruefen — daruber hinaus SV-pflichtig.
- AG-Zuschuss 15 Prozent ist Pflicht — wer das nicht zahlt, riskiert AN-Klagen.
- Bei Direktzusagen: bilanzielle Behandlung (Rueckstellung) zu beachten — § 6a EStG.
- StBVV: bAV-Beratung als Zusatzauftrag (Komplex).
- DATEV-Tipp: DATEV LODAS bAV-Konfiguration mit Versicherer-Schnittstelle.

## Querverweise

- `stb-lohn-direktversicherung-3-nr-63-estg` — Direktversicherung.
- `stb-lohn-vermoegenswirksame-leistungen` — VL.
- `stb-lohn-bav-doppelversorgung-foerderung` — Mehrere bAV-Wege.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.

## Quellen und Updates

Stand: 05/2026.

- BetrAVG §§ 1, 1a.
- EStG §§ 3 Nr. 63, 19, 100; § 6a (Direktzusage-Rueckstellung).
- SGB IV; SvEV.
- BMF v. 06.12.2017, v. 18.03.2022.
- BRSG.
- BBG-West RV 2025: 96.600 EUR; § 100 EStG Schwellenwert 2.575 EUR/Monat, Foerderbetrag max. 288 EUR/Jahr (Stand 2025; Sozialversicherungs-Rechengroessenverordnung 2026 und BMF-Schreiben pruefen).

<!-- AUDIT 27.05.2026 | welle 6 | 5 Marker aufgeloest: 4 bestaetigt (Werte 2025 eingesetzt), 1 ersetzt (Rentner-Freibetrag Pruefhinweis ohne Marker) -->

## 4. `stb-lohn-dienstwagen-1-prozent-fahrtenbuch`

**Fokus:** Dienstwagen 1-Prozent-Methode oder Fahrtenbuch. Anwendungsfall geldwerter Vorteil Privatnutzung Dienstwagen E-Auto Hybrid Listenpreis Brutto-Methode. Methodik Prüfung Methode Vergleich Steuerklasse. Output Lohn-Abrechnung mit korrektem Sachbezug Dienstwagen.

# Dienstwagen — 1-Prozent-Methode oder Fahrtenbuch

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Dienstwagen — 1-Prozent-Methode oder Fahrtenbuch` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Stellt der AG dem AN einen Dienstwagen zur privaten Nutzung zur Verfuegung, entsteht geldwerter Vorteil (Sachbezug). Zwei Berechnungsmethoden: 1-Prozent-Methode (pauschal 1 Prozent vom Bruttolistenpreis pro Monat) oder Fahrtenbuch (anteilig nach tatsaechlicher Privatnutzung). E-Autos und Hybride haben reduzierte Bemessungsgrundlage. Zusaetzlich gilt 0,03 Prozent fuer Fahrten Wohnung-Arbeit pro Entfernungskilometer.

## Kaltstart-Rueckfragen

1. Welches Fahrzeug — Verbrenner, Plug-in-Hybrid, Elektro?
2. Bruttolistenpreis bei Erstzulassung?
3. Wird der Dienstwagen privat genutzt? In welchem Umfang?
4. Liegt Fahrtenbuch vor (mind. 6 Monate korrekt gefuehrt)?
5. Wohnung-Arbeit-Entfernung in km?
6. Wie viele Tage pro Monat Fahrten zur Arbeit?
7. Wird AN am Erwerb beteiligt (Eigenbeteiligung)?
8. Welche Sondersituationen (Garagengeld, Tankkarte, Pflege)?

## Rechtlicher Rahmen

### Primaernormen

**§ 6 Abs. 1 Nr. 4 Satz 2 EStG** — 1-Prozent-Methode.

**§ 6 Abs. 1 Nr. 4 Satz 3 EStG** — Fahrtenbuch-Methode.

**§ 6 Abs. 1 Nr. 4 Satz 2 EStG** — Reduzierte Bemessungsgrundlage E-Auto / Hybrid.

**§ 8 Abs. 2 EStG** — Sachbezug.

**§ 9 Abs. 1 Nr. 4a EStG** — Entfernungspauschale beim AN.

### Verwaltungsanweisungen

- BMF v. 03.03.2022 — E-Auto / Hybrid Sonderregeln.
- LStR R 8.1.
- BMF v. 18.11.2009 — Dienstwagen allgemein.

## Workflow

### Phase 1 — Methode waehlen

| Kriterium | 1-Prozent-Methode | Fahrtenbuch |
|---|---|---|
| Aufwand | Gering | Hoch (taeglich) |
| Pauschalierung | Ja | Nein, einzelfallgenau |
| Vorteil bei niedriger Privatnutzung | Nein, hoher Sachbezug | Ja, niedriger Sachbezug |
| Vorteil bei teurem Auto | Nein | Ja, anteilig |
| Vorteil bei Vielfahrer | Ja | Nein |

### Phase 2 — 1-Prozent-Methode

- 1 Prozent des Bruttolistenpreises (auf volle 100 EUR abgerundet) pro Monat = Sachbezug Privatnutzung.
- Plus 0,03 Prozent x Bruttolistenpreis x Entfernungskilometer fuer Fahrten Wohnung-Arbeit (oder 0,002 Prozent je tatsaechlich gefahrenem Arbeitsweg-Tag bei Einzelnachweis).
- E-Auto (rein elektrisch, Bruttolistenpreis bis 70.000 EUR — Anhebung von 60.000 auf 70.000 EUR fuer Anschaffungen ab 01.01.2024 durch Wachstumschancengesetz, BGBl. 2024 I Nr. 108; aktuelles BMF-Schreiben pruefen): nur ein Viertel der Bemessungsgrundlage (0,25 Prozent statt 1 Prozent), entsprechend 0,0075 Prozent statt 0,03 Prozent fuer Wohnung-Arbeit.
- E-Auto ueber Listenpreis-Grenze: halbe Bemessungsgrundlage (0,5 Prozent statt 1 Prozent).
- Plug-in-Hybrid: 0,5 Prozent bei Mindest-Reichweite oder CO2-Bedingungen (Voraussetzungen § 6 Abs. 1 Nr. 4 Satz 2 Nr. 3 ff. EStG; aktuelle Anforderungen in BMF-Schreiben pruefen).

**Zahlenbeispiel:** Verbrenner-Dienstwagen Bruttolistenpreis 45.000 EUR; Wohnung-Arbeit 15 km. Monatlicher Sachbezug: 1 Prozent x 45.000 EUR = 450 EUR + 0,03 Prozent x 45.000 EUR x 15 km = 202,50 EUR; gesamt 652,50 EUR Sachbezug. Bei E-Auto 45.000 EUR Listenpreis (in Foerderbereich): nur 0,25 Prozent x 45.000 EUR = 112,50 EUR Privatanteil + 0,0075 Prozent x 45.000 EUR x 15 km = 50,625 EUR; gesamt 163,125 EUR.

### Phase 3 — Fahrtenbuch-Methode

- Voraussetzungen Fahrtenbuch (BMF-Anforderungen):
 - Zeitnah gefuehrt (taeglich).
 - Lueckenlos.
 - Datum, Zweck, Start- und Ziel-Kilometer, gefahrene Strecke.
 - Trennung privat/dienstlich.
 - Unveraenderbar (kein Excel-Sheet, sondern Buch oder zertifizierte Software).
- Aufteilung: Privatfahrten anteilig zur Jahres-Kilometer.
- Anteil x Gesamt-Kfz-Kosten = Sachbezug.

### Phase 4 — E-Auto / Plug-in-Hybrid

- E-Auto Erstzulassung 2019-2030 mit Listenpreis bis 60.000 EUR (Anschaffung bis 31.12.2023) bzw. bis 70.000 EUR (Anschaffung ab 01.01.2024, Wachstumschancengesetz BGBl. 2024 I Nr. 108; aktuelles BMF-Schreiben pruefen): 0,25 Prozent.
- E-Auto Listenpreis ueber der jeweiligen Grenze: 0,5 Prozent.
- Plug-in-Hybrid: 0,5 Prozent bei Mindestreichweite elektrisch 80 km oder CO2-Wert max. 50 g/km (§ 6 Abs. 1 Nr. 4 EStG i.V.m. § 3 Abs. 2 EmoG; Stand 2025; aktuelle Anforderungen ueber BMF-Schreiben pruefen, da Grenzwerte politisch angepasst werden koennen).

### Phase 5 — Eigenbeteiligung

- AN zahlt monatlich an AG (z.B. 100 EUR): mindert Sachbezug 1:1.
- Eigenbeteiligung an Anschaffungskosten: mindert Bemessungsgrundlage gleichmaessig.
- AN-Eigenanteil Garagengeld: nicht ueberlagernd.

### Phase 6 — Lohnabrechnung

- Sachbezug 1-Prozent + 0,03 Prozent als Lohnzuschlag.
- LSt-pflichtig nach Steuerklasse.
- SV-pflichtig bis BBG.
- Buchung im Lohnkonto.

## Output

- Lohn-Abrechnung mit Sachbezug Dienstwagen.
- Fahrtenbuch oder Erklaerung 1-Prozent-Methode.
- Dokumentation Bruttolistenpreis.

## Strategie und Praxis-Tipps

- Fahrtenbuch nur sinnvoll bei geringer Privatnutzung — Aufwand erheblich.
- E-Auto bis 60.000 EUR (Anschaffung bis 31.12.2023) bzw. bis 70.000 EUR (Anschaffung ab 01.01.2024, Wachstumschancengesetz): massive Steuerersparnis (0,25 vs. 1 Prozent).
- 0,03-Prozent-Pauschale Wohnung-Arbeit auch bei seltenen Fahrten — bei wenigen Fahrten 0,002-Prozent-Tagesmethode (gueltig: Einzelnachweis).
- Bei Familien-GmbH mit GGF: Dienstwagen kritisch — verdeckte Gewinnausschuettung bei Privatnutzung Familienangehoeriger ueber Vereinbarung.
- StBVV: in Lohnpauschale; Fahrtenbuch-Pruefung Zeithonorar.
- DATEV-Tipp: DATEV LODAS Dienstwagen-Modul mit Listenpreis und Konfiguration; bei E-Auto/Hybrid Sonderschluessel.

## Querverweise

- `stb-lohn-sachbezuege-50-euro-freigrenze` — Sachbezug.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.
- `stb-lohn-firmenrad-leasing-jobrad` — JobRad.
- `stb-lohn-jobticket-mobilitaet-deutschlandticket` — Jobticket.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 6, 8, 9.
- LStR R 8.1.
- BMF v. 03.03.2022 (E-Auto / Hybrid).
- BMF v. 18.11.2009 (Dienstwagen).
- E-Auto-Listenpreisgrenze: bis 70.000 EUR (Anschaffung ab 01.01.2024); Plug-in-Hybrid: 80 km elektrische Mindestreichweite oder max. 50 g/km CO2 (Stand 2025; BMF-Schreiben E-Auto/Hybrid pruefen).

<!-- AUDIT 27.05.2026 | welle 6 | 7 Marker aufgeloest: 4 bestaetigt (Wachstumschancengesetz BGBl. 2024 I Nr. 108, Grenzwerte eingesetzt), 3 ersetzt (Pruefhinweise ohne Marker) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `stb-lohn-direktversicherung-3-nr-63-estg`

**Fokus:** Direktversicherung Steuerfreiheit § 3 Nr 63 EStG bis 8 Prozent BBG SV-frei bis 4 Prozent BBG. Anwendungsfall Entgeltumwandlung Direktversicherung Konfiguration Mandant AG-Zuschuss 15 Prozent. Methodik Beitragsberechnung Beitragsbemessung Auswirkung Netto. Output Lohn-Konfiguration mit Direktversicherung.

# Direktversicherung — § 3 Nr. 63 EStG

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Direktversicherung — § 3 Nr. 63 EStG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die Direktversicherung ist der haeufigste bAV-Durchfuehrungsweg: AG schliesst einen Versicherungsvertrag fuer den AN ab. Beitraege bis 8 Prozent der RV-BBG (West) sind steuerfrei (§ 3 Nr. 63 EStG), bis 4 Prozent BBG SV-frei. Beim AN reduziert sich das Bruttolohn um den Beitrag, in der Auszahlungsphase ist die Rente lohnsteuerpflichtig (nachgelagerte Besteuerung). Der Steuerberater konfiguriert die Direktversicherung in DATEV LODAS und prueft die Schwellen.

## Kaltstart-Rueckfragen

1. Welche Versicherungsgesellschaft? Liegt Vertrag vor?
2. Welcher monatliche Beitrag?
3. Erfolgt durch Entgeltumwandlung (AN-Beitrag aus Brutto) oder AG-Finanzierung (zusaetzlich)?
4. AG-Zuschuss 15 Prozent nach § 1a BetrAVG vorgesehen?
5. Welcher Bruttolohn des AN (BBG-Pruefung)?
6. Sind bereits Vorvertraege ueber bAV vorhanden (kumulierte 8-Prozent-Pruefung)?
7. Wann erfolgt voraussichtlicher Renteneintritt?
8. Welche Sondersituation (Pensionsfonds-Wechsel, Beitragsfreistellung)?

## Rechtlicher Rahmen

### Primaernormen

**§ 3 Nr. 63 EStG** — Steuerfreiheit Beitraege bAV bis 8 Prozent BBG.

**§ 1a BetrAVG** — Entgeltumwandlungs-Anspruch und 15-Prozent-Zuschuss.

**§ 1 Abs. 1 Nr. 9 SvEV** — SV-Freiheit bAV-Beitraege bis 4 Prozent BBG-West RV (kumuliert).

**§ 19 EStG** — Versorgungsbezuege Auszahlung.

**§ 40b EStG a.F.** — Pauschalbesteuerung (Altvertraege bis 31.12.2004).

### Verwaltungsanweisungen

- BMF v. 06.12.2017.
- BMF v. 18.03.2022 (BRSG-Reform).
- LStR.

## Workflow

### Phase 1 — Foerderungs-Grenzen

| Grenze | Wert (Stand 2025) | Wirkung |
|---|---|---|
| 8 Prozent BBG-West RV | 7.728 EUR/Jahr (BBG-West RV 2025: 96.600 EUR; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen) | LSt-frei |
| 4 Prozent BBG-West RV | ca. 3.864 EUR/Jahr (2024) | SV-frei (zusaetzlich zur LSt-Freiheit) |
| Darueber hinaus | Vollversteuerung; SV-Pflicht | Wie regulaerer Lohn |

**Zahlenbeispiel (Stand 2024-Werte):** AN mit Entgeltumwandlung 200 EUR/Monat in Direktversicherung = 2.400 EUR/Jahr. Liegt unter 4-Prozent-BBG (3.864 EUR) — voll LSt- UND SV-frei. AG erspart SV-AG-Anteil und muss daher 15 Prozent Pflichtzuschuss nach § 1a BetrAVG leisten (= 30 EUR/Monat).

(BBG-Werte 2025: West RV 96.600 EUR/Jahr; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen.)

### Phase 2 — Vergleich Entgeltumwandlung vs. AG-Finanzierung

- Entgeltumwandlung: AN-Beitrag aus Brutto; AG spart SV-Beitraege; § 1a BetrAVG 15-Prozent-Zuschuss-Pflicht.
- AG-Finanzierung: zusaetzlich zum Lohn; volle Foerderung § 3 Nr. 63 EStG; § 100 EStG fuer Geringverdiener.

### Phase 3 — § 1a BetrAVG 15-Prozent-Zuschuss

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Geltung Direktversicherung/Pensionskasse/Pensionsfonds (nicht Direktzusage).
- Seit 2019; fuer Altvertraege bis Ende 2021 noch Uebergangsregelung; seit 2022 voll wirksam.

### Phase 4 — Lohnabrechnung-Konfiguration

- DATEV LODAS: Konto fuer Direktversicherung anlegen.
- Beitrag aus Brutto reduzieren (Entgeltumwandlung) oder zusaetzlich (AG-Finanzierung).
- LSt-frei bis 8 Prozent BBG.
- SV-frei bis 4 Prozent BBG.
- Buchung im Hauptbuch (Konto 4380 oder 6380 SKR 03).

### Phase 5 — Auszahlungsphase

- Rente lohnsteuerpflichtig (nachgelagerte Besteuerung) nach § 22 Nr. 5 EStG (Vertrag der bAV) bzw. § 19 EStG (bei Direktzusage / Unterstuetzungskasse).
- KV/PV-Beitragspflicht in der KVdR (Freibetrag fuer Pflichtversicherte Rentner nach § 226 Abs. 2 SGB V; aktuellen Freibetrag ueber GKV-Spitzenverband pruefen).
- Bei Kapitalauszahlung Sondertarif § 34 Abs. 2 Nr. 4 i.V.m. § 24 Nr. 1 EStG Fuenftel-Regel pruefen — Voraussetzung: Zusammenballung in einem Veranlagungszeitraum.

### Phase 6 — Bei Insolvenz

- Direktversicherung mit Sicherungsmechanismus durch Versicherungsaufsicht.
- Bei Insolvenz des AG: AN-Anspruch bleibt (Vertragsuebertragung an AN moeglich).
- PSVaG (Pensions-Sicherungs-Verein) bei Direktzusage relevant, NICHT bei Direktversicherung.

## Output

- Konfigurierte Direktversicherung in DATEV LODAS.
- Lohnabrechnung mit korrektem Sachbezug.
- AG-Zuschuss 15 Prozent dokumentiert.

## Strategie und Praxis-Tipps

- 4-Prozent-SV-Grenze pruefen — daruber LSt-frei, aber SV-pflichtig.
- AG-Zuschuss 15 Prozent ist GESETZLICHE PFLICHT — bei Entgeltumwandlung nicht verhandelbar.
- Bei Altvertraegen (vor 2005) § 40b EStG a.F. pauschal versteuert; in Auszahlung anders behandelt.
- Bei Wechsel des AG: Vertrag uebertragen lassen, sonst Beitragsfreistellung.
- StBVV: in Lohnpauschale; Beratung Direktversicherungs-Wahl Zusatzauftrag.
- DATEV-Tipp: DATEV LODAS Direktversicherungs-Modul mit Versicherer-Schnittstelle (z.B. Allianz, R+V).

## Querverweise

- `stb-lohn-betriebliche-altersversorgung-grundlagen` — bAV-Grundlagen.
- `stb-lohn-bav-doppelversorgung-foerderung` — Doppelfoerderung.
- `stb-lohn-vermoegenswirksame-leistungen` — VL.
- `stb-lohn-sv-beitraege-grundlagen` — SV.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 3 Nr. 63, 19, 22 Nr. 5, 34, 40b a.F.
- BetrAVG §§ 1, 1a.
- SvEV § 1 Abs. 1 Nr. 9.
- BMF v. 06.12.2017 (IV C 5 - S 2333/17/10002), v. 18.03.2022 (IV C 5 - S 2333/19/10005).
- BBG-West RV 2025: 96.600 EUR; 8 Prozent = 7.728 EUR LSt-frei; 4 Prozent = 3.864 EUR SV-frei (Sozialversicherungs-Rechengroessenverordnung 2026 pruefen).

<!-- AUDIT 27.05.2026 | welle 6 | 6 Marker aufgeloest: 4 bestaetigt (BBG 2025 eingesetzt, BMF-GZ recherchiert), 2 ersetzt (Pruefhinweise ohne Marker) -->

## 6. `stb-lohn-elternzeit-mutterschutz`

**Fokus:** Elternzeit Mutterschutz Mutterschaftsgeld Elterngeld lohnrelevant. Anwendungsfall AN-Schwangerschaft Geburt Antrag Mutterschutz Elternzeit Auswirkung auf Lohn SV-Status Steuerprogression. Methodik Prüfung MuschG Beschaeftigungsverbot BEEG. Output Lohn-Abrechnung Elternzeit Bescheinigung.

# Elternzeit, Mutterschutz, Mutterschaftsgeld, Elterngeld

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Elternzeit, Mutterschutz, Mutterschaftsgeld, Elterngeld` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Bei Schwangerschaft und Elternschaft gelten besondere lohnrechtliche Regelungen: Mutterschutz nach MuschG (Beschaeftigungsverbot 6 Wochen vor und 8 Wochen nach Geburt), Mutterschaftsgeld nach SGB V, Elternzeit nach BEEG (bis 3 Jahre), Elterngeld nach BEEG (Bundeselterngeld- und Elternzeitgesetz). Der Steuerberater begleitet die Lohnabrechnung in dieser Phase, prueft AG-Zuschuss-Pflichten und die SV-Behandlung.

## Kaltstart-Rueckfragen

1. Schwangerschaftsbescheinigung mit Geburtstermin?
2. Wann beginnt der Mutterschutz?
3. Welcher Bruttolohn der letzten 3 Monate (Bemessungsbasis)?
4. Welche Krankenkasse zustaendig?
5. Plant AN Elternzeit — wie lange?
6. Plant Vater/Partner ebenfalls Elternzeit?
7. Wird Elterngeld Basis oder Plus gewaehlt?
8. Welche Beschaeftigungsverbote vor Geburt (z.B. schwere Arbeiten, Schichtdienst)?

## Rechtlicher Rahmen

### Primaernormen

**MuschG** — Mutterschutzgesetz.

**§§ 3, 6 MuschG** — Beschaeftigungsverbote.

**§ 24 SGB V** — Mutterschaftsgeld.

**§ 24i SGB V** — Mutterschaftsgeld-Auszahlung.

**BEEG** — Bundeselterngeld- und Elternzeitgesetz.

**§§ 1-14 BEEG** — Elterngeld (Basis, Plus, Partnerschaftsbonus).

**§§ 15-22 BEEG** — Elternzeit (Anspruch, Anmeldung, Teilzeit).

**§ 32b EStG** — Progressionsvorbehalt fuer Mutterschaftsgeld und Elterngeld.

### Verwaltungsanweisungen

- BMFSFJ-Merkblaetter.
- BMF zu Progressionsvorbehalt.

## Workflow

### Phase 1 — Mutterschutz und Beschaeftigungsverbot

- 6 Wochen vor Geburt: Beschaeftigungsverbot ohne Antrag (kann AN auf eigenen Wunsch arbeiten).
- 8 Wochen nach Geburt (12 bei Mehrlingen/Behinderung): absolutes Beschaeftigungsverbot.
- AG zahlt Mutterschutzlohn 100 Prozent fortgesetzt (basis fuer Mutterschaftsgeld + AG-Zuschuss).

### Phase 2 — Mutterschaftsgeld

- Krankenkasse zahlt Mutterschaftsgeld (Hoechstsatz 13 EUR/Tag, § 24i Abs. 2 SGB V — seit 01.01.1992 unveraendert; bei Gesetzesaenderung GKV-Spitzenverband pruefen).
- AG zahlt Zuschuss zum Mutterschaftsgeld bis zum durchschnittlichen Nettolohn der letzten 3 Monate (§ 20 Abs. 1 MuSchG).
- Beide zusammen ergeben Nettolohn der Schwangeren waehrend Mutterschutz.
- AG-Erstattung der gesamten Aufwendungen ueber U2-Umlage (100 Prozent) — vgl. `stb-lohn-umlage-u1-u2-insogeld-umlage`.

### Phase 3 — Elternzeit und Elterngeld

- Elternzeit: bis zu 3 Jahre Anspruch, bis 8. Geburtstag.
- Anmeldung: spaetestens 7 Wochen vor Beginn.
- Waehrend Elternzeit: kein Anspruch auf Lohn vom AG.
- Elterngeld vom Staat: 65 Prozent vom durchschnittlichen Nettolohn vor Geburt (max. 1.800 EUR/Monat; Einkommensgrenze fuer Ehepartner-Gesamteinkommen ab 01.04.2024 abgesenkt auf 175.000 EUR, § 1 Abs. 8 BEEG; bei Gesetzesaenderung BMFSFJ pruefen).
- Elterngeld Basis: 12 Monate; 14 Monate bei Partnermonaten.
- Elterngeld Plus: doppelte Laufzeit bei halber monatlicher Hoehe (kombiniert mit Teilzeit, bis 32 Wochenstunden).

### Phase 4 — Teilzeit waehrend Elternzeit

- Bis 32 Stunden/Woche moeglich (BEEG-Reform 2021).
- AN beantragt Teilzeit beim AG.
- AG kann nur aus betrieblichen Gruenden ablehnen.

### Phase 5 — SV-Status waehrend Elternzeit

- Mitgliedschaft KV bleibt erhalten (beitragsfrei).
- RV-Pflicht eingeschraenkt (wenn keine Beschaeftigung).
- AV: Anwartschaftsanrechnung Erziehungszeiten (3 Jahre).
- Pruefung Krankenkasse: ggf. freiwillige Versicherung.

### Phase 6 — Progressionsvorbehalt

- Mutterschaftsgeld und Elterngeld sind steuerfrei.
- Werden aber in den Progressionsvorbehalt einbezogen (§ 32b EStG).
- AN-Steuerbescheid: hoeherer Steuersatz auf uebrige Einkuenfte.
- Bei Veranlagung: ggf. Nachzahlung.

## Output

- Mutterschutz-Lohnabrechnung mit AG-Zuschuss.
- Elternzeit-Status in DATEV LODAS.
- Bescheinigung fuer Elterngeld-Antrag.

## Strategie und Praxis-Tipps

- AG-Zuschuss zum Mutterschaftsgeld ist gesetzliche Pflicht — verbindlich.
- Bei Teilzeit waehrend Elternzeit: lohnsteuer- und SV-rechtlich wie regulaere Teilzeit.
- AN sollte Elterngeld Basis vs. Plus mit Steuerberater oder Familienberatung pruefen.
- Wegen Progressionsvorbehalt im Folgejahr kann Steuernachzahlung anfallen.
- StBVV: Mutterschutz/Elternzeit-Abrechnung Zusatzauftrag (Komplex).
- DATEV-Tipp: DATEV LODAS Mutterschutz-Modul; Elternzeit als "Unterbrechung" markieren.

## Querverweise

- `stb-lohn-krankheit-entgeltfortzahlung-efzg` — Krankheit.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-lohnsteuer-monatsabschluss` — Monatsabschluss.

## Quellen und Updates

Stand: 05/2026.

- MuschG.
- SGB V §§ 24, 24i.
- BEEG.
- EStG § 32b.
- BMFSFJ-Merkblaetter.

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 1 bestaetigt (Mutterschaftsgeld 13 EUR/Tag seit 1992 stabil), 1 ersetzt (BEEG-Einkommensgrenze 175.000 EUR ab 01.04.2024 eingesetzt) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 7. `stb-lohn-firmenrad-leasing-jobrad`

**Fokus:** JobRad Dienstrad Leasingmodell steuerliche Behandlung. Anwendungsfall AG-Leasing eines Fahrrads oder E-Bikes Überlassung an AN durch Gehaltsumwandlung Sachbezug von einem Viertel Prozent. Methodik Prüfung Konfiguration Leasingvertrag. Output Lohn-Abrechnung mit JobRad.

# JobRad / Dienstrad — Steuerliche Behandlung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `JobRad / Dienstrad — Steuerliche Behandlung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Das JobRad / Dienstrad ist ein vom AG geleastes Fahrrad oder E-Bike, das dem AN auch privat ueberlassen wird. Bei Gehaltsumwandlung gilt seit 2020 die 0,25-Prozent-Sachbezug-Regelung (1 Prozent von einem Viertel des Bruttolistenpreises). Bei voller AG-Finanzierung (zusaetzlich zum Lohn) ist das JobRad sogar steuerfrei (§ 3 Nr. 37 EStG). Die Regelung gilt bis 31.12.2030.

## Kaltstart-Rueckfragen

1. Welche Form — AG-finanziert (steuerfrei) oder Gehaltsumwandlung (0,25-Prozent)?
2. Bruttolistenpreis des Rades?
3. Welcher Leasing-Vertragspartner (JobRad, Lease-a-bike, Eurorad)?
4. Welche Vertragslaufzeit (typisch 36 Monate)?
5. Liegt Uebernahme-Option am Vertragsende vor (Restwert-Auswirkung)?
6. Ist das Rad ein E-Bike (S-Pedelec ueber 25 km/h = Kraftfahrzeug-Behandlung)?
7. Liegt Vereinbarung der Privatnutzung schriftlich vor?
8. Welche Pruefung im Konzern bzgl. Lohnumwandlung-Pflicht?

## Rechtlicher Rahmen

### Primaernormen

**§ 3 Nr. 37 EStG** — Steuerfreiheit AG-finanziertes Dienstrad (Geltung bis 31.12.2030).

**§ 6 Abs. 1 Nr. 4 EStG** — Bemessungsgrundlage Sachbezug.

**§ 8 Abs. 2 EStG** — Sachbezug.

### Verwaltungsanweisungen

- BMF v. 17.11.2017 — Dienstrad.
- BMF v. 09.01.2020 — Aktualisierung 0,25-Prozent-Regelung.

## Workflow

### Phase 1 — Variante waehlen

| Variante | LSt | SV | Voraussetzung |
|---|---|---|---|
| AG-finanziert zusaetzlich (§ 3 Nr. 37) | Steuerfrei | SV-frei | "Zusaetzlich zum Lohn" |
| Gehaltsumwandlung 0,25-Prozent | 0,25 Prozent vom Bruttolistenpreis als Sachbezug | SV-pflichtig wie regulaerer Lohn | Vereinbarung |

### Phase 2 — Sachbezug 0,25-Prozent-Regelung

- Konstruktion: 1 Prozent von einem Viertel des Bruttolistenpreises (= 0,25 Prozent vom Bruttolistenpreis) als monatlicher Sachbezug Privatnutzung.
- Bruttolistenpreis vorher auf volle 100 EUR abgerundet.
- Im Unterschied zum Dienstwagen: keine zusaetzlichen 0,03 Prozent fuer Fahrten Wohnung-Arbeit beim Fahrrad/E-Bike (nicht S-Pedelec).
- **Zahlenbeispiel:** Bruttolistenpreis 3.000 EUR — 0,25 Prozent = 7,50 EUR/Monat Sachbezug. Bei E-Bike 4.500 EUR Listenpreis — 0,25 Prozent x 4.500 EUR = 11,25 EUR/Monat.

### Phase 3 — Leasingvertrag

- Vertragspartner: Bank/Leasinggesellschaft.
- AG-Leasingrate aus Brutto-Gehalt umgewandelt (typisch 50-100 EUR/Monat).
- AN-Vorteil: Brutto-Reduktion mit Steuerersparnis.
- Vertragsende: AN-Uebernahme moeglich; Restwert (typisch 10 Prozent) muss als Vorteil versteuert werden.

### Phase 4 — Sonderfall S-Pedelec

- S-Pedelec mit Tretunterstuetzung bis 45 km/h: zulassungs-, versicherungs- und fuehrerscheinpflichtiges Kraftfahrzeug.
- Sachbezugs-Berechnung wie Dienstwagen: 1 Prozent vom Bruttolistenpreis (bei rein elektrisch und Listenpreis bis 70.000 EUR ggf. 0,25 Prozent — vgl. `stb-lohn-dienstwagen-1-prozent-fahrtenbuch`).
- Plus 0,03 Prozent Wohnung-Arbeit pro Entfernungskilometer (anders als bei klassischem JobRad/Pedelec bis 25 km/h).

### Phase 5 — Pruefung Gehaltsumwandlung

- Verzicht auf laufende Vergueteung schriftlich vereinbart.
- Auswirkung auf Mindestlohn-Pflicht: Brutto-Lohn nach Umwandlung muss MiLo erreichen.
- Auswirkung auf bAV-Foerderung: BBG-Grenzen bleiben.
- Auswirkung auf Sondervergueteungen (z.B. Tantieme): in der Regel keine Reduktion.

### Phase 6 — Lohnabrechnung

- DATEV LODAS: Lohnart "JobRad-Sachbezug 0,25 Prozent".
- Buchung im Hauptbuch.
- LSt-Bescheinigung mit Sachbezugs-Vermerk.

## Output

- Lohn-Abrechnung mit JobRad-Sachbezug.
- Leasingvertrag-Beleg.
- Vereinbarung Gehaltsumwandlung.

## Strategie und Praxis-Tipps

- JobRad ist beliebter Lohnumwandlungs-Hebel mit hoher AN-Akzeptanz.
- 0,25-Prozent-Regelung ist generoes — bei 3.000 EUR-Rad nur 7,50 EUR/Monat Sachbezug.
- Bei AG-Finanzierung zusaetzlich: voll steuerfrei nach § 3 Nr. 37 EStG — beste Variante fuer AG mit gutem Imagewunsch.
- Restwert-Versteuerung am Ende des Leasings nicht vergessen (Wert minus 10 Prozent Restwert = Versteuerungs-Pflicht).
- S-Pedelec ungleich JobRad — Dienstwagen-Behandlung 1 Prozent.
- StBVV: in Lohnpauschale; Konfiguration einmalig.
- DATEV-Tipp: DATEV LODAS JobRad-Lohnart konfigurieren; Leasingvertrag verlinken.

## Querverweise

- `stb-lohn-sachbezuege-50-euro-freigrenze` — Sachbezug.
- `stb-lohn-dienstwagen-1-prozent-fahrtenbuch` — Dienstwagen.
- `stb-lohn-jobticket-mobilitaet-deutschlandticket` — Jobticket.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.
- `stb-lohn-mindestlohn-aktuell-2026-anpassung` — Mindestlohn (bei Gehaltsumwandlung MiLo-Pruefung).

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 3 Nr. 37, 6, 8.
- BMF v. 17.11.2017, v. 09.01.2020.
- Verifikations-Hinweis: § 3 Nr. 37 EStG gueltig bis 31.12.2030.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 8. `stb-lohn-jahresmeldungen-ahn-asn-besondere`

**Fokus:** Jahresmeldungen DEUEV Jahreslohnsumme Abmelde- und Sondermeldungen. Anwendungsfall Jahresende-Meldungen 15. Februar Folgejahr AN-Jahresarbeitsentgelt-Meldung Sondermeldungen Lohnsteuerbescheinigung. Methodik Standardablauf. Output Jahresmeldungen Bescheinigungen.

# Jahresmeldungen — Lohnsumme, Sondermeldungen, LSt-Bescheinigung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Jahresmeldungen — Lohnsumme, Sondermeldungen, LSt-Bescheinigung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Zum Jahresende sind verschiedene Jahresmeldungen Pflicht: Jahresmeldung DEUEV (Lohnsumme je AN bis 15. Februar Folgejahr), Lohnsteuerbescheinigung an FA (bis 28. Februar Folgejahr), BG-Lohnnachweis (15. Februar Folgejahr), Statistik-Meldungen, Berichtigungs-Meldungen. Der Steuerberater erledigt diese systematisch im Januar/Februar Folgejahr.

## Kaltstart-Rueckfragen

1. Welches Berichtsjahr abzurechnen?
2. Wie viele AN-Bewegungen im Jahr (Anmeldung, Abmeldung)?
3. Liegen alle DEUEV-Jahresmeldungen automatisch in DATEV LODAS?
4. Welche Lohnsteuerbescheinigungen sind elektronisch zu uebermitteln (alle)?
5. BG-Lohnnachweis vorbereitet?
6. Welche Statistik-Meldungen anstehen?
7. Welche Korrekturen aus dem Vorjahr (Berichtigungs-Meldungen)?
8. Welcher Mandantenkommunikationsplan fuer LSt-Bescheinigungen?

## Rechtlicher Rahmen

### Primaernormen

**§ 28a SGB IV** — DEUEV-Meldungen.

**§ 41b EStG** — Elektronische Lohnsteuerbescheinigung.

**§ 165 SGB VII** — BG-Lohnnachweis.

**§ 28f SGB IV** — Aufzeichnungspflicht 10 Jahre.

### Verwaltungsanweisungen

- DEUEV-Verfahrensanweisung.
- BMF zur Lohnsteuerbescheinigung.

## Workflow

### Phase 1 — Jahresmeldung DEUEV

- § 10 DEUEV: Frist 15. Februar des Folgejahres (gesetzlich; bei Verschiebung auf naechsten Werktag).
- Inhalt: SV-pflichtige Lohnsumme je AN ueber das ganze Jahr.
- Form: elektronisch ueber sv.net (online / comfort) oder DATEV DAKOTA.
- Abgabegrund: 50 (Jahresmeldung).
- Eigene Meldung pro AN, der im Jahr beschaeftigt war (auch ausgeschiedene).

### Phase 2 — Lohnsteuerbescheinigung

- Frist: bis 28. Februar Folgejahr.
- Empfaenger: ELStAM-System (Finanzamt).
- Inhalt: Jahres-Brutto, einbehaltene LSt/KiSt/SolZ, SV-Beitraege, geldwerte Vorteile, Steuerklasse, Aufmerksamkeiten, KUG, Mutterschaftsgeld, Elterngeld.
- AN bekommt Ausdruck (Papier oder elektronisch zur Steuererklaerung).

### Phase 3 — BG-Lohnnachweis

- Frist: bis 15. Februar Folgejahr.
- Inhalt: Jahres-Lohnsumme nach Gefahrenklassen.
- Form: elektronisch ueber sv.net oder BG-Portal.

### Phase 4 — Statistik-Meldungen

- Sofern Mandant in Statistik-Stichprobe: Jahresmeldung an Destatis.
- Frist nach Aufforderung.
- Inhalt: Bruttolohnsumme, Mitarbeiterzahl, Stunden.

### Phase 5 — Berichtigungs-Meldungen

- Bei nachtraeglich erkannten Fehlern: Berichtigungs-Meldung mit korrigierten Werten.
- Bei wesentlicher LSt-Differenz: ggf. § 41c EStG Lohnsteuer-Berichtigung beim FA.
- Bei SV-Differenzen: SV-Berichtigung und Nachzahlung oder Erstattung.

### Phase 6 — Mandantenkommunikation

- Lohnsteuerbescheinigungen an AN versenden (Standard: Anfang Februar).
- Mandant ueber Beitragsentwicklung informieren (Jahres-Bruttolohnsumme).
- Wiedervorlage fuer Folgejahr.

## Output

- Jahresmeldungen DEUEV.
- Lohnsteuerbescheinigungen.
- BG-Lohnnachweis.
- Statistik-Meldungen (falls Stichprobe).

## Strategie und Praxis-Tipps

- 15. Februar und 28. Februar sind harte Fristen — Termincontrolling Pflicht.
- Bei vielen Mandanten Lohn-Block-Bearbeitung im Januar/Februar.
- LSt-Bescheinigungen automatisch aus DATEV LODAS; bei Korrektur Sonderaufwand.
- Bei AN-Wechsel im Jahr: Jahresmeldung beim alten AG; neuen AG ueber Lohnzeitraum informieren.
- StBVV: Jahresmeldungen in Lohnpauschale oder gesonderter Auftrag.
- DATEV-Tipp: DATEV LODAS Jahresende-Lauf mit automatischer Erstellung aller Meldungen.

## Querverweise

- `stb-lohn-monatsende-meldepflichten-checkliste` — Meldepflichten.
- `stb-lohn-sv-meldungen-dakota-svnet` — sv.net.
- `stb-lohn-berufsgenossenschaft-bg-meldung-jahresende` — BG.
- `stb-lohn-lohnsteuer-anmeldung-elster` — ELSTER.
- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.

## Quellen und Updates

Stand: 05/2026.

- SGB IV §§ 28a, 28f.
- SGB VII § 165.
- EStG §§ 41b, 41c.
- DEUEV.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 9. `stb-lohn-jobticket-mobilitaet-deutschlandticket`

**Fokus:** Jobticket Deutschlandticket steuerliche Behandlung. Anwendungsfall AG erstattet AN Mobilitaetsticket OePNV oder bietet Jobticket steuerfrei nach § 3 Nr 15 EStG Auswirkung auf Entfernungspauschale. Methodik Prüfung Konfiguration. Output Lohn-Abrechnung mit Jobticket.

# Jobticket und Deutschlandticket — Steuerliche Behandlung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Jobticket und Deutschlandticket — Steuerliche Behandlung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Der AG kann AN ein Jobticket fuer OePNV steuerfrei zur Verfuegung stellen, wenn dieses zusaetzlich zum geschuldeten Arbeitslohn gewaehrt wird (§ 3 Nr. 15 EStG). Seit 2023 ist das Deutschlandticket (49 EUR/Monat ab 01.05.2023, ab 01.01.2025 58 EUR; Preis wird politisch jaehrlich festgelegt — aktuellen Wert ueber Verkehrsministerkonferenz pruefen) ebenso behandelbar. Bei voller AG-Finanzierung ist das Ticket steuer- und SV-frei. Bei AN-Eigenanteil wird der AG-Zuschuss steuerfrei behandelt. Die Entfernungspauschale wird beim AN um die steuerfreien AG-Leistungen gekuerzt.

## Kaltstart-Rueckfragen

1. Welches Ticket — Jobticket, Deutschlandticket, anderes OePNV-Ticket?
2. Wer zahlt — AG voll, AG-Zuschuss + AN-Eigenanteil?
3. Wird zusaetzlich zum Lohn gewaehrt oder durch Gehaltsumwandlung?
4. Welche Entfernung Wohnung-Arbeit hat der AN (Auswirkung auf Entfernungspauschale)?
5. Liegt nur OePNV-Nutzung vor, oder auch privat?
6. Pauschalierung § 40 Abs. 2 EStG 25 Prozent gewuenscht (AG-finanzierte Sachzuwendung)?
7. Welche Versorger (DB, Verkehrsverbund, Deutschlandticket-Vertrieb)?
8. Anwendung im DATEV LODAS bereits konfiguriert?

## Rechtlicher Rahmen

### Primaernormen

**§ 3 Nr. 15 EStG** — Steuerfreiheit Jobticket fuer OePNV.

**§ 9 Abs. 1 Nr. 4 EStG** — Entfernungspauschale.

**§ 40 Abs. 2 Satz 2 EStG** — Pauschalbesteuerung 25 Prozent.

**§ 8 Abs. 2 EStG** — Sachbezug.

### Verwaltungsanweisungen

- BMF v. 15.08.2019 zu Jobticket.
- BMF zu Deutschlandticket 2023/2024.
- LStR R 3.15.

## Workflow

### Phase 1 — Voraussetzungen Steuerfreiheit § 3 Nr. 15 EStG

- Sachbezug fuer Fahrten Wohnung-Arbeit oder im OePNV.
- "Zusaetzlich zum ohnehin geschuldeten Arbeitslohn" (kein Gehaltsumwandlung).
- Ticket ist auch privat nutzbar (z.B. Deutschlandticket).

### Phase 2 — Steuerfreiheit oder Pauschalierung

| Variante | Lohnsteuer | SV |
|---|---|---|
| AG-finanziertes Jobticket zusaetzlich zum Lohn | Steuerfrei (§ 3 Nr. 15 EStG) | SV-frei |
| Jobticket durch Gehaltsumwandlung (kein "zusaetzlich") | Steuerpflichtig | SV-pflichtig (alternativ Pauschal § 40 Abs. 2) |
| Pauschal versteuert 25 Prozent (§ 40 Abs. 2) | Pauschal 25 Prozent | Pauschal beitragsfrei |

### Phase 3 — Entfernungspauschale-Kuerzung

- Steuerfreier AG-Zuschuss zum Jobticket wird beim AN von der Entfernungspauschale abgezogen.
- AN-Werbungskostenabzug entsprechend gemindert.
- Bei Pauschalierung § 40 Abs. 2 EStG: keine Kuerzung.

### Phase 4 — Deutschlandticket-Sondersituation

- 01.05.2023: Einfuehrung Deutschlandticket 49 EUR/Monat.
- Ab 01.01.2025: 58 EUR/Monat; Preis wird politisch jaehrlich festgelegt — aktuellen Wert ueber Verkehrsministerkonferenz (VMK) pruefen.
- Behandlung wie Jobticket nach § 3 Nr. 15 EStG.
- Bei AG-Zuschuss zum Deutschlandticket des AN: steuerfrei, wenn ueber Job-Karte erworben.
- **Zahlenbeispiel:** AG zahlt fuer AN das Deutschlandticket voll (58 EUR/Monat Stand 2025; Preis pruefen), zusaetzlich zum Lohn → 696 EUR/Jahr LSt- und SV-frei nach § 3 Nr. 15 EStG; allerdings beim AN Kuerzung der Entfernungspauschale (§ 9 Abs. 1 Nr. 4 Satz 6 EStG) — der AN gibt in der Anlage N die AG-Leistung an, das FA mindert den Werbungskostenabzug. Alternative Pauschalierung 25 Prozent (§ 40 Abs. 2 Satz 2 EStG): keine Kuerzung der Entfernungspauschale.

### Phase 5 — Lohnabrechnung

- DATEV LODAS: Lohnart "Jobticket steuerfrei".
- Buchung im Hauptbuch (Lohnnebenkosten).
- AN-LSt-Bescheinigung mit Jobticket-Vermerk Zeile 17.

### Phase 6 — Dokumentation

- Bestellnachweis Ticket.
- AG-Erstattungsbeleg.
- Vertrag mit Verkehrsverbund.

## Output

- Lohn-Abrechnung mit Jobticket steuerfrei.
- LSt-Bescheinigung Zeile 17.
- Beleg im Lohnordner.

## Strategie und Praxis-Tipps

- Deutschlandticket ist guenstig fuer AG — minimale Buchung, hohe AN-Bindung.
- "Zusaetzlich zum Lohn" streng pruefen — bei Gehaltsumwandlung kein § 3 Nr. 15.
- Bei Pauschalierung 25 Prozent: keine Entfernungspauschalen-Kuerzung beim AN; attraktiv.
- Bei vollstaendiger AG-Erstattung: AN profitiert ueber Werbungskosten-Differenz.
- StBVV: in Lohnpauschale; Konfiguration einmalig.
- DATEV-Tipp: DATEV LODAS Jobticket-Konfiguration mit eigenem Lohnart.

## Querverweise

- `stb-lohn-sachbezuege-50-euro-freigrenze` — Sachbezug.
- `stb-lohn-dienstwagen-1-prozent-fahrtenbuch` — Dienstwagen.
- `stb-lohn-firmenrad-leasing-jobrad` — JobRad.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 3 Nr. 15, 8, 9 Abs. 1 Nr. 4, 40 Abs. 2.
- BMF v. 15.08.2019 (Jobticket).
- LStR R 3.15.
- Deutschlandticket-Preis: 58 EUR/Monat ab 01.01.2025 (jaehrlich durch VMK festgelegt; pruefen).

<!-- AUDIT 27.05.2026 | welle 6 | 4 Marker aufgeloest: 2 bestaetigt (Deutschlandticket 58 EUR ab 01.01.2025), 2 ersetzt (Pruefhinweise ohne Marker) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
