---
name: stb-lohn-kurzarbeit-lohnsteuer-anmeldung
description: "STB Lohn Kurzarbeit Lohnsteuer Anmeldung: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# STB Lohn Kurzarbeit Lohnsteuer Anmeldung

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **STB Lohn Kurzarbeit Lohnsteuer Anmeldung** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stb-lohn-kurzarbeit-kug-progression` | Kurzarbeitergeld KUG Anmeldung Berechnung Progressionsvorbehalt. Anwendungsfall Kurzarbeit-Antrag bei der Bundesagentur Lohnabrechnung mit anteiligem Lohn und KUG Steuerprogressionsvorbehalt für AN. Methodik Prüfung Voraussetzungen Berechnung Soll- und Ist-Entgelt. Output Kurzarbeit-Lohnabrechnung Bescheinigung. |
| `stb-lohn-lohnsteuer-anmeldung-elster` | Elektronische Lohnsteuer-Anmeldung über ELSTER. Anwendungsfall monatliche oder vierteljaehrliche LSt-Anmeldung KiSt SolZ Pauschalierung Anmeldungs-Schema technische Übermittlung. Methodik Daten aus Lohnabrechnung ELSTER-Formular Prüfen Senden. Output ELSTER-Quittung. |
| `stb-lohn-lohnsteuer-monatsabschluss` | Monatlicher Lohnsteuer-Monatsabschluss. Anwendungsfall regulaere Lohnabrechnung Bruttolohn LSt KiSt SolZ pauschalierte Loehne SV-Abrechnung Auszahlung Anmeldung. Methodik Standard-Abrechnungsschritte 39e Tabelle. Output Lohnabrechnungen LSt-Anmeldung Bankueberweisung. |
| `stb-lohn-minijob-538-euro-2024-anpassung` | Minijob 538 EUR-Grenze dynamisch an Mindestlohn gekoppelt seit 1.10.2022. Anwendungsfall geringfuegige Beschaeftigung pauschale Abgaben Beitragsbefreiung Steuerklassen-Frage Mehrfachbeschaeftigung. Methodik Prüfung 538 EUR-Grenze Aufzeichnungspflicht MiLoG. Output Minijob-Abrechnung Anmeldung Knappschaft. |
| `stb-lohn-sachbezuege-50-euro-freigrenze` | Sachbezuege 50 EUR Freigrenze § 8 Abs 2 EStG. Anwendungsfall geldwerte Vorteile Gutscheine Sachgeschenke Aufmerksamkeiten Begründung steuerfrei wenn unter 50 EUR/Monat. Methodik Prüfung Sachbezugs-Typ Geldzuwendung-Abgrenzung Loyalitaetsprogramme. Output Sachbezugs-Abrechnung Dokumentation. |
| `stb-mandanten-onboarding-checkliste-vollservice` | Onboarding-Checkliste Neumandant Vollservice. Anwendungsfall Mandatsannahme Standardablauf Mandantenvereinbarung Vollmachten DSGVO-Information Buchführung Lohn Steuererklärung. Methodik strukturierter Checkliste. Output Mandantenakte komplett startklar. |
| `stb-mandantenkommunikation-bwa-uebergabe-quartal` | Quartalsgespraech BWA-Übergabe. Anwendungsfall systematische Quartalskommunikation mit Mandant Ergebnisbesprechung Steuerthemen Investitionsplanung. Methodik Termin-Vorbereitung Agenda Dokumentation. Output Quartalsgespraechs-Protokoll Massnahmen-Liste. |
| `stb-mandantenrechnung-honorar-stbvv` | Mandantenrechnung Honorar StBVV. Anwendungsfall Honorarabrechnung Pauschal- Zeit- und Gegenstandswert-Honorar Steuerberatergebührenverordnung. Methodik Rechnungsschreibung Gebührensaetze § 33 35 35a. Output Mandantenrechnung. |
| `stb-pruefliste-belegabgabe-monatlich` | Prüfliste monatliche Belegabgabe. Anwendungsfall standardisierte Belegabgabe-Kontrolle Mandant Vollständigkeit Bankauszuege Kasse Eingangsrechnungen Ausgangsrechnungen Lohnauswertung. Methodik Prüfliste Eingangskontrolle Mahnung. Output Prüfprotokoll Belegmahnung. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **STB Lohn Kurzarbeit Lohnsteuer Anmeldung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stb-lohn-kurzarbeit-kug-progression`

**Fokus:** Kurzarbeitergeld KUG Anmeldung Berechnung Progressionsvorbehalt. Anwendungsfall Kurzarbeit-Antrag bei der Bundesagentur Lohnabrechnung mit anteiligem Lohn und KUG Steuerprogressionsvorbehalt für AN. Methodik Prüfung Voraussetzungen Berechnung Soll- und Ist-Entgelt. Output Kurzarbeit-Lohnabrechnung Bescheinigung.

# Kurzarbeitergeld (KUG) — Anmeldung, Berechnung, Progression

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Kurzarbeitergeld (KUG) — Anmeldung, Berechnung, Progression` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Kurzarbeit ist die voruebergehende Reduzierung der regelmäßigen Arbeitszeit aus wirtschaftlichen Gruenden. Der AG meldet Kurzarbeit bei der Bundesagentur fuer Arbeit (BA) an; der AN erhaelt anteilig den Lohn vom AG plus KUG von der BA. KUG wird ueber AG abgerechnet (Erstattungsverfahren). Das KUG selbst ist steuerfrei, unterliegt aber dem Progressionsvorbehalt (§ 32b EStG) — wirkt also auf den Steuersatz der uebrigen Einkuenfte.

## Kaltstart-Rueckfragen

1. Vorliegt erheblicher Arbeitsausfall mit Entgeltausfall fuer mindestens 10 Prozent der AN-Belegschaft?
2. Ist der Arbeitsausfall voruebergehend und unabwendbar?
3. Hat der AG Anzeige beim BA-Arbeitgeberservice eingereicht?
4. Liegt Zustimmung Betriebsrat oder AN-Vereinbarung vor?
5. Wie hoch ist der Arbeitsausfall pro AN (Prozentsatz)?
6. Welche Sollentgelte sind zugrunde zu legen?
7. Welche AN-Kinder (KUG-Erhoehung mit Kind)?
8. Welche Dauer ist beantragt?

## Rechtlicher Rahmen

### Primaernormen

**§§ 95-109 SGB III** — Kurzarbeitergeld.

**§ 96 SGB III** — Anspruchsvoraussetzungen.

**§ 99 SGB III** — Anzeige des Arbeitsausfalls.

**§ 32b EStG** — Progressionsvorbehalt.

**§ 14 SGB IV** — Arbeitsentgelt.

### Verwaltungsanweisungen

- BA-Merkblatt KUG.
- BMF zu Progressionsvorbehalt.

## Workflow

### Phase 1 — Voraussetzungen

| Voraussetzung | Pruefung |
|---|---|
| Erheblicher Arbeitsausfall | Mind. 10 Prozent der AN mit > 10 Prozent Entgeltausfall |
| Voruebergehender Charakter | Erwartung Erholung |
| Unabwendbarkeit | Wirtschaftliche/technische Gruende, nicht selbst verschuldet |
| Sozialvertraegliche Loesung | Urlaubsabbau, Arbeitszeitkonten zuerst aufbrauchen |

### Phase 2 — Anzeige BA

- Form ueber BA-Arbeitgeberservice.
- Spaetestens Ende des Anspruchsmonats.
- BA-Pruefung der Voraussetzungen; Bescheid.

### Phase 3 — Berechnung KUG

- Sollentgelt = pauschaliertes Brutto-Lohn ohne Arbeitsausfall (auf BBG RV begrenzt).
- Istentgelt = tatsaechliches Brutto im Anspruchsmonat.
- Pauschalierte Nettoentgeltdifferenz = Differenz fiktives Netto-Sollentgelt minus Netto-Istentgelt nach KUG-Tabelle der BA.
- KUG ohne Kind: 60 Prozent der Nettoentgeltdifferenz.
- KUG mit Kind (mindestens ein Kind nach ELStAM oder zumindest aus Kinderfreibetrag erkennbar): 67 Prozent der Nettoentgeltdifferenz.
- BBG-Grenze: Sollentgelt nur bis BBG RV; ab 2025 bundeseinheitlich 8.050 EUR/Monat (96.600 EUR/Jahr; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen).
- Pandemie-Sonderaufstockungen (auf 70/77 Prozent ab 4. Monat, 80/87 Prozent ab 7. Monat) sind regulaer ausgelaufen — Anwendung nur bei Sonderverordnung; Stand 2026 pruefen.

### Phase 4 — Lohnabrechnung

- AN-Lohn anteilig (Istentgelt): regulaere LSt und SV.
- KUG: steuerfrei, SV-frei.
- AG zahlt KUG aus eigener Kasse aus, beantragt Erstattung bei BA.
- AG-Erstattung von BA in der Regel im Folgemonat.

### Phase 5 — Progressionsvorbehalt

- KUG wird im AN-Steuerbescheid in den Progressionsvorbehalt § 32b Abs. 1 Satz 1 Nr. 1 lit. a EStG einbezogen.
- Hoehere Steuerklassifikation auf die uebrigen Einkuenfte.
- AN bekommt LSt-Bescheinigung mit "KUG" (in der Regel Zeile 15 — bei LSt-Bescheinigungsmuster-Aenderungen BMF-Schreiben pruefen).
- Bei Bezug von Lohnersatzleistungen ueber 410 EUR im Kalenderjahr: Veranlagungspflicht des AN gemaess § 46 Abs. 2 Nr. 1 EStG; Steuererklaerung zwingend.

### Phase 6 — Pflichten AG

- Monatliche Abrechnung KUG je AN.
- Antrag an BA bis Ende dritter Folgemonat nach Anspruchsmonat.
- Aufzeichnung KUG-Stunden je AN.
- LSt-Bescheinigung jaehrlich mit KUG-Angabe.

## Output

- Kurzarbeits-Lohnabrechnung.
- Antrag an BA mit Berechnung.
- LSt-Bescheinigung mit KUG-Angabe.

## Strategie und Praxis-Tipps

- Anzeige fristgerecht (Ende Anspruchsmonat) — Verspaetung schliesst Anspruch aus.
- Urlaubsabbau und Arbeitszeitkonto-Abbau zuerst sind grundsaetzlich Pflicht.
- AN-Information ueber Progressionsvorbehalt — Steuernachzahlung in der Veranlagung moeglich.
- SV-Beitraege wurden in Pandemiezeit teilweise vom AG erlassen — Sonderregelungen 2020-2022 abgelaufen.
- StBVV: Kurzarbeit-Abrechnung Sondertaetigkeit, Zeithonorar.
- DATEV-Tipp: DATEV LODAS KUG-Modul mit BA-Schnittstelle.

## Querverweise

- `stb-lohn-lohnsteuer-monatsabschluss` — Monatsabschluss.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.

## Quellen und Updates

Stand: 05/2026.

- SGB III §§ 95-109.
- EStG § 32b.
- BA-Merkblatt KUG.

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 1 bestaetigt (BBG RV 2025 96.600 EUR eingesetzt), 1 ersetzt (LSt-Bescheinigungszeile Pruefhinweis ohne Marker) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `stb-lohn-lohnsteuer-anmeldung-elster`

**Fokus:** Elektronische Lohnsteuer-Anmeldung über ELSTER. Anwendungsfall monatliche oder vierteljaehrliche LSt-Anmeldung KiSt SolZ Pauschalierung Anmeldungs-Schema technische Übermittlung. Methodik Daten aus Lohnabrechnung ELSTER-Formular Prüfen Senden. Output ELSTER-Quittung.

# Lohnsteuer-Anmeldung ueber ELSTER

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Lohnsteuer-Anmeldung ueber ELSTER` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die Lohnsteuer-Anmeldung wird elektronisch ueber ELSTER an das Finanzamt uebermittelt — Pflicht seit Jahren. Der Steuerberater nutzt entweder DATEV-ELSTER-Modul oder ELSTER-Online direkt. Die Anmeldung enthaelt: LSt, KiSt, SolZ, ggf. pauschalierte Loehne. Frist: 10. des Folgemonats (monatlich) bzw. 10. des dem Quartal folgenden Monats (vierteljaehrlich).

## Kaltstart-Rueckfragen

1. Welcher Anmeldungszeitraum — monatlich, vierteljaehrlich, jaehrlich?
2. Liegen alle Lohnabrechnungen vor?
3. Sind pauschalierte Loehne (Minijob, § 37b, § 40a) zu beruecksichtigen?
4. Welches Finanzamt ist zustaendig?
5. Steuer-Nr des AG aktuell?
6. Liegen Sondervergueteungen mit eigener Steuerklasse vor?
7. Welche Korrekturen aus Vormonat (Berichtigung § 153 AO)?
8. ELSTER-Zugang funktioniert (Zertifikat, Passwort)?

## Rechtlicher Rahmen

### Primaernormen

**§ 41a EStG** — Anmeldung Lohnsteuer.

**§ 41b EStG** — Lohnsteuerbescheinigung.

**§ 40 EStG, § 40a EStG, § 37b EStG** — Pauschalierungen.

**§ 240 AO** — Saeumniszuschlag.

**§ 152 AO** — Verspaetungszuschlag.

**§ 39e EStG** — ELStAM.

### Verwaltungsanweisungen

- BMF zu ELSTER-Verfahren.
- LStR.

## Workflow

### Phase 1 — Daten zusammenstellen

- Bruttoloehne aller AN.
- LSt insgesamt.
- KiSt insgesamt (Konfession der einzelnen AN).
- SolZ insgesamt (SolZ entfaellt fuer Lohnsteuerpflichtige unterhalb der Freigrenze § 3 Abs. 3 SolZG seit 01.01.2021; ab 2025 Freigrenze 18.130 EUR ESt (Einzel) / 36.260 EUR (Zusammenveranlagung); Milderungszone bis Voll-SolZ; aktuelle Grenzen ueber SolZG-Fassung pruefen).
- Pauschal versteuerte Betraege (§ 40 Abs. 1 / Abs. 2 EStG, § 40a EStG, § 37b EStG).
- KSt-Pauschalierung Aushilfen (§ 40a EStG): 25 Prozent (kurzfristig) oder 2 Prozent (Minijob, geht direkt an Knappschaft, nicht ueber LSt-Anmeldung).

### Phase 2 — ELSTER-Formular

| Feld | Inhalt |
|---|---|
| Steuer-Nr | AG-Steuer-Nr |
| Anmeldungszeitraum | Monat/Quartal |
| Bruttoloehne insgesamt | Summe aller Brutto |
| Einbehaltene LSt | Summe LSt |
| KiSt evang/kath | Konfession |
| SolZ | Stand 2026 ggf. 0 |
| Pauschal versteuerte Betraege | § 40, § 40a, § 37b |
| Erstattungsantraege | Lohnsteuer-Ueberzahlung |

### Phase 3 — Pruefung vor Senden

- Plausibilitaet Bruttolohnsumme mit BWA/SuSa (Konto 4120/4130 SKR 03).
- LSt-Summe plausibel zur Bruttolohnsumme (ca. 15-25 Prozent je nach Steuerklassen-Mix).
- SV-Beitraege im Mandantenbericht separat dokumentiert.

### Phase 4 — Sendung und Quittung

- ELSTER-Senden ueber DATEV LODAS Schnittstelle oder ELSTER-Online.
- Sendebestaetigung mit Transaktions-Nummer archivieren.
- FA-Bescheid abwarten (in der Regel automatische Verarbeitung, kein gesonderter Bescheid).

### Phase 5 — Zahlung

- LSt-Faelligkeit: 10. des Folgemonats.
- Ueberweisung an FA-Konto.
- Verspaetungszuschlag § 152 AO: bis 10 Prozent der Anmeldung, max. 25.000 EUR.
- Saeumniszuschlag § 240 AO: 1 Prozent pro Monat.

### Phase 6 — Korrekturen

- Bei spaeter erkanntem Fehler: Berichtigung § 153 AO.
- Berichtigte Anmeldung mit Vermerk "Berichtigung".
- Bei wesentlicher Steuerverkuerzung: ggf. Selbstanzeige § 371 AO.

## Output

- ELSTER-Quittung mit Transaktions-Nummer.
- Lohnsteuer-Anmeldung-Dokumentation in Mandantenakte.
- Buchungssatz (Konto LSt-Verbindlichkeit).

## Strategie und Praxis-Tipps

- Frist 10. des Folgemonats hart — bei wiederholten Verspaetungen Verspaetungszuschlag.
- Pauschalierungs-Optionen pruefen (Minijob 2 Prozent vs. reguläre Lohnsteuer).
- Bei Sondervergueteungen Fuenftel-Regelung § 34 EStG pruefen.
- Bei Mehrfachbeschaeftigung des AN: Steuerklasse 6 fuer Folge-AG.
- StBVV: ELSTER-Anmeldung in Lohnpauschale.
- DATEV-Tipp: DATEV LODAS hat direkte ELSTER-Schnittstelle; bei Sicherheits-Zertifikaten regelmäßige Erneuerung.

## Querverweise

- `stb-lohn-lohnsteuer-monatsabschluss` — Monatsabschluss.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-monatsende-meldepflichten-checkliste` — Meldepflichten.
- `stb-datev-lohn-modul-lodas-luh` — DATEV LODAS.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 37b, 39e, 40, 40a, 41a, 41b.
- AO §§ 152, 153, 240, 371.
- BMF zu ELSTER-Verfahren.
- LStR.
- SolZ-Freigrenze 2025: 18.130 EUR ESt (Einzel); Milderungszone § 3 Abs. 3 SolZG; aktuelle Freigrenze jaehrlich pruefen (SolZG).

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 bestaetigt (SolZ-Freigrenze 2025 eingesetzt) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `stb-lohn-lohnsteuer-monatsabschluss`

**Fokus:** Monatlicher Lohnsteuer-Monatsabschluss. Anwendungsfall regulaere Lohnabrechnung Bruttolohn LSt KiSt SolZ pauschalierte Loehne SV-Abrechnung Auszahlung Anmeldung. Methodik Standard-Abrechnungsschritte 39e Tabelle. Output Lohnabrechnungen LSt-Anmeldung Bankueberweisung.

# Lohnsteuer-Monatsabschluss

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Lohnsteuer-Monatsabschluss` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Der monatliche Lohnsteuer-Abschluss ist die Hauptarbeit der Lohnbuchhaltung: Bruttolohnermittlung, LSt-Berechnung (Steuerklasse, KiFB, KKB), KiSt, SolZ, pauschalierte Loehne, SV-Beitraege, Auszahlung netto, Buchung im Hauptbuch, Anmeldung LSt beim FA. Der Steuerberater erledigt das mit DATEV LODAS oder Lohn und Gehalt — aber die fachliche Pruefung bleibt seine Verantwortung.

## Kaltstart-Rueckfragen

1. Welcher Abrechnungsmonat?
2. Welche Aenderungen gegenueber Vormonat (Eintritte, Austritte, Gehaltsaenderungen, Sonderzahlungen)?
3. Liegen alle ELStAM-Daten aktuell vor?
4. Liegen Krankheitstage / Urlaubstage vor?
5. Sind Sondervergueteungen (Tantieme, Boni) abzurechnen?
6. Liegen Sachbezuege oder geldwerte Vorteile vor?
7. Sind pauschal versteuerte Loehne (Minijob, Aushilfen) abzurechnen?
8. Welcher LSt-Anmeldungs-Zeitraum (monatlich, vierteljaehrlich, jaehrlich)?

## Rechtlicher Rahmen

### Primaernormen

**§ 38 EStG** — Lohnsteuer-Abzug Pflicht AG.

**§ 39b EStG** — Einbehaltung Lohnsteuer.

**§ 40 EStG** — Pauschalierung in besonderen Faellen.

**§ 40a EStG** — Pauschalierung Aushilfskraefte.

**§ 41a EStG** — Anmeldung Lohnsteuer.

**§ 3 EStG** — steuerfreie Einnahmen (Kataloge); insbesondere § 3 Nr. 16, 24, 26, 33, 39, 51, 63.

**§ 3b EStG** — Zuschlaege Sonntag, Feiertag, Nacht.

**§ 8 Abs. 2 EStG** — Sachbezuege.

**§ 19 EStG** — Einkuenfte aus nichtselbstaendiger Arbeit.

**SGB IV §§ 14, 28d, 28e** — SV-Beitraege.

### Verwaltungsanweisungen

- LStR (Lohnsteuer-Richtlinien).
- LStDV.
- BMF-Schreiben zu Reisekosten, Sachbezuegen.

## Workflow

### Phase 1 — Datenuebernahme

- Stammdaten aus DATEV LODAS/Lohn und Gehalt.
- Aenderungsdaten aus Mandant (Eintritte, Krankheitstage, Sonderzahlungen).
- ELStAM aktuell abrufen.

### Phase 2 — Bruttolohnermittlung

- Grundgehalt aus Stammdatum.
- Stundenlohn bei Stunden-AN.
- Mehrarbeit, Ueberstunden, Schichtzuschlaege.
- Sonn-/Feiertag-/Nachtzuschlaege § 3b EStG (LSt-frei und SV-frei in bestimmten Grenzen).
- Sondervergueteungen: 13. Monatsgehalt, Tantieme, Sonderzahlung.
- Sachbezuege (Verpflegung, Unterkunft mit SvEV-Werten; jaehrlich ueber BMAS-SvEV-Verordnung aktualisiert; Stand 2025: Verpflegung frei 313 EUR/Monat, Unterkunft 278 EUR/Monat).

### Phase 3 — Lohnsteuer-Berechnung

- LSt-Tabelle automatisch in DATEV LODAS.
- Steuerklasse, KiFB, KKB aus ELStAM.
- Pauschalierung Aushilfen (§ 40a EStG): 2 Prozent (Minijob) oder 25 Prozent (kurzfristig).
- Pauschalierung Sachzuwendungen (§ 37b EStG): 30 Prozent (mit Zuschlag).
- KiSt nach AN-Konfession.
- SolZ (Stand 2025): entfaellt fuer den Grossteil der AN seit 01.01.2021 (Freigrenze § 3 SolZG; ab 2025 18.130 EUR ESt Einzel); Milderungszone bis Voll-SolZ; aktuelle Grenzen ueber SolZG-Fassung pruefen.

### Phase 4 — SV-Beitraege

- Beitragsbemessungsgrenzen (BBG) Stand 2025 (Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen):
 - RV/AV: ab 2025 bundeseinheitlich 8.050 EUR/Monat (96.600 EUR/Jahr; West-Ost-Angleichung zum 01.01.2025 abgeschlossen).
 - KV/PV (bundeseinheitlich): 5.512,50 EUR/Monat (66.150 EUR/Jahr); JAEG abweichend.
- Beitragssaetze Stand 2025: RV 18,6 Prozent, AV 2,6 Prozent, KV allgemein 14,6 Prozent + KK-Zusatzbeitrag (durchschnittlich 2,5 Prozent), PV 3,6 Prozent + Kinderlosenzuschlag 0,6 Prozent; Sozialversicherungs-Rechengroessenverordnung 2026 zum Jahreswechsel pruefen.
- Zusatzbeitrag KV individuell je Kasse.
- Beitragsverteilung AG-/AN-Anteile (jeweils ca. halftig; Ausnahmen PV-Kinderlose, Insolvenzgeld-Umlage).

### Phase 5 — Auszahlung und Buchung

- Nettolohn = Brutto minus LSt/KiSt/SolZ minus SV-AN-Anteile (- Pfaendung, - VL, - Sonderabzug).
- Ueberweisung an AN-Konto.
- Typische Buchungssaetze SKR04 (SKR03 entsprechend):
 - Loehne und Gehaelter: 6020 SKR04 (4120 SKR03) "Loehne" an 3740 SKR04 (1742 SKR03) "Verbindlichkeiten aus Lohn- und Kirchensteuer", 3760 SKR04 (1741 SKR03) "Verbindlichkeiten im Rahmen der sozialen Sicherheit", 3790 SKR04 (1755 SKR03) "Sonstige Verbindlichkeiten gegenueber Mitarbeitern".
 - AG-SV-Anteil: 6110 SKR04 (4130 SKR03) "Gesetzliche soziale Aufwendungen" an 3760 SKR04 (1741 SKR03).
 - Bei Auszahlung Netto: 3790 SKR04 an Bank (1800 SKR04 / 1200 SKR03).
 - Abfuehrung LSt: 3740 SKR04 an Bank.
 - Abfuehrung SV: 3760 SKR04 an Bank.
- Konten-Nr je nach Kontenplan und DATEV-Mandantenkonfiguration; bei Abweichungen Mandantenstammdaten pruefen.

### Phase 6 — Anmeldung Lohnsteuer

- LSt-Anmeldung beim FA ueber ELSTER bis 10. des Folgemonats.
- LSt-Faelligkeit: 10. des Folgemonats; Sofortverfuegung Saeumniszuschlag § 240 AO.
- KiSt parallel angemeldet.
- SolZ ggf. parallel.

## Output

- Lohnabrechnungen aller AN.
- LSt-Anmeldung an FA.
- SV-Beitragsabrechnung an Krankenkassen.
- Buchungssatz fuer Hauptbuch.

## Strategie und Praxis-Tipps

- Frist 10. des Folgemonats fuer LSt-Anmeldung — bei Verspaetung Verspaetungszuschlag.
- BBG und Beitragssaetze: Stand 2025 (RV-BBG 96.600 EUR, KV-BBG 66.150 EUR; Beitragssaetze RV 18,6%, AV 2,6%, KV 14,6%+Zusatz, PV 3,6%+Kinderlos); Sozialversicherungs-Rechengroessenverordnung 2026 jaehrlich pruefen.
- Bei pauschal versteuerten Loehnen (Minijob 2 Prozent): Buchung separat.
- Sonn-/Feiertag-/Nacht-Zuschlaege § 3b EStG nur LSt- und SV-frei in bestimmten Grenzen; ueber die Grenze normal versteuert/verbeitragt.
- StBVV: Monatsabschluss in Lohnpauschale; Sondertaetigkeiten (Mehrarbeit-Berechnung mit komplexer Schichten-Logik) Zeithonorar.
- DATEV-Tipp: DATEV LODAS Monatsabschluss-Pruefliste vor Anmeldung; Plausibilitaetspruefung Bruttolohnsumme.

## Querverweise

- `stb-lohn-mandantenaufnahme-onboarding` — Onboarding.
- `stb-lohn-meldungen-sv-elstam-zugang` — ELStAM/SV-Meldungen.
- `stb-lohn-lohnsteuer-anmeldung-elster` — ELSTER-Anmeldung.
- `stb-lohn-sv-beitraege-grundlagen` — SV-Beitraege.
- `stb-lohn-monatsende-meldepflichten-checkliste` — Meldepflichten.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 3, 3b, 8, 19, 38, 39b, 40, 40a, 41a; LStR.
- SGB IV §§ 14, 28d, 28e.
- LStDV.
- BBG 2025: RV 96.600 EUR, KV/PV 66.150 EUR; Beitragssaetze 2025: RV 18,6%, AV 2,6%, KV 14,6%+Zusatz, PV 3,6%+Kinderlos 0,6% (Sozialversicherungs-Rechengroessenverordnung 2026 pruefen).
- SvEV-Sachbezugswerte 2025: Verpflegung 313 EUR/Monat, Unterkunft 278 EUR/Monat (jaehrlich durch BMAS angepasst).

<!-- AUDIT 27.05.2026 | welle 6 | 8 Marker aufgeloest: 6 bestaetigt (BBG/Beitragssaetze 2025 eingesetzt), 2 ersetzt (Pruefhinweise ohne Marker) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `stb-lohn-minijob-538-euro-2024-anpassung`

**Fokus:** Minijob 538 EUR-Grenze dynamisch an Mindestlohn gekoppelt seit 1.10.2022. Anwendungsfall geringfuegige Beschaeftigung pauschale Abgaben Beitragsbefreiung Steuerklassen-Frage Mehrfachbeschaeftigung. Methodik Prüfung 538 EUR-Grenze Aufzeichnungspflicht MiLoG. Output Minijob-Abrechnung Anmeldung Knappschaft.

# Minijob — 538-EUR-Grenze und Anpassungen

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Minijob — 538-EUR-Grenze und Anpassungen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die geringfuegige Beschaeftigung ("Minijob") ist seit 01.10.2022 dynamisch an den Mindestlohn gekoppelt: 10 Wochenstunden bei 12 EUR Mindestlohn = 480 EUR; bei 12,41 EUR (Stand 01.01.2024) ergab das 538 EUR. Bei MiLo-Anhebungen steigt die Grenze entsprechend. Pauschalabgaben des AG: 30 Prozent (15 RV + 13 KV + 2 LSt) bzw. 12 Prozent bei Privathaushalt. AN ist SV-frei (Ausnahme: RV-Pflicht mit Opt-out).

## Kaltstart-Rueckfragen

1. Welcher AN — neu eingestellt oder bestehend?
2. Aktueller Bruttolohn pro Monat und im Jahresdurchschnitt?
3. Ist die 538-EUR-Grenze (Stand 01.01.2024) eingehalten?
4. Aktuell (Stand 2026): Mindestlohn 13,90 EUR/h, Minijob-Grenze 603 EUR/Monat (= 13,90 × 130 / 3 = 602,33, kfm. gerundet 603; MiLoV5 v. 05.11.2025, BGBl. 2025 I Nr. 268; Minijob-Zentrale). Ab 2027: MiLo 14,60 EUR/h, Grenze voraussichtlich 633 EUR/Monat (MiLoV5).
5. Hat der AN bereits andere Minijobs (Mehrfachbeschaeftigung verboten ueber Grenze)?
6. Hat der AN eine Hauptbeschaeftigung mit SV-Pflicht? (Dann zweiter Minijob noch moeglich.)
7. Hat der AN RV-Befreiung beantragt (Opt-out)?
8. Welcher Pauschalsatz greift — 30 Prozent (gewerblich) oder 12 Prozent (Privathaushalt)?

## Rechtlicher Rahmen

### Primaernormen

**§ 8 SGB IV** — geringfuegige Beschaeftigung; aktuelle Grenze dynamisch an MiLo gekoppelt (538 EUR Stand 01.01.2024; bei MiLo-Anhebung dynamisch).

**§ 8a SGB IV** — Privathaushalts-Minijob.

**§ 40a EStG** — Pauschalierung Aushilfen.

**§ 14 SGB IV** — Arbeitsentgelt.

**§ 17 MiLoG** — Aufzeichnungspflicht.

**§ 6 SGB VI** — Befreiung Rentenversicherungspflicht.

### Verwaltungsanweisungen

- Gemeinsame Rundschreiben Spitzenverbaende KK.
- Knappschaft Bahn-See als Minijob-Zentrale.

## Workflow

### Phase 1 — Grenzpruefung

- Bruttolohn pro Monat <= 538 EUR (Stand 01.01.2024).
- Stand 01.01.2025: 556 EUR/Monat (MiLo 12,82 EUR; § 8 Abs. 1a SGB IV).
- Stand 01.01.2026: 603 EUR/Monat (MiLo 13,90 EUR; MiLoV5 vom 05.11.2025, BGBl. 2025 I Nr. 268; bestaetigt durch Minijob-Zentrale, Jahresgrenze 7.236 EUR).
- Voraussichtlich 01.01.2027: 633 EUR/Monat (MiLo 14,60 EUR; MiLoV5).
- Sonderzahlungen (Weihnachts-, Urlaubsgeld): bei regelmäßigem Anspruch JAHRES-Durchschnitt bilden, sonst Grenzverletzung.
- Mehrfacher Minijob mehrerer AG: Summe pruefen.

### Phase 2 — Pauschalabgaben AG

| Abgabe | Gewerblicher Minijob | Privathaushalts-Minijob |
|---|---|---|
| Pauschale RV | 15 Prozent | 5 Prozent |
| Pauschale KV | 13 Prozent | 5 Prozent |
| Pauschalsteuer (LSt+KiSt+SolZ) | 2 Prozent | 2 Prozent |
| U1 (Krankheit) | Satz je KK (Stand 2025 typisch 1,0-1,1 Prozent) | wie links |
| U2 (Mutterschaft) | Satz je KK (Stand 2025 typisch 0,24 Prozent) | wie links |
| Insolvenzgeld-Umlage | 0,06 Prozent (Stand 2024; Insolvenzgeldumlageverordnung pruefen) | — (Privathaushalt) |
| Berufsgenossenschaft | Branchen-spezifisch | Haftpflichtversicherung Privathaushalt |

(Saetze U1/U2 jaehrlich neu festgelegt; Krankenkassen-Satzungen pruefen.)

**Zahlenbeispiel gewerblicher Minijob (Stand 01.01.2024, MiLo 12,41 EUR, Grenze 538 EUR):** Bruttolohn 500 EUR. AG-Pauschalabgaben ca. 30 Prozent + Umlagen — 15 Prozent RV (75 EUR) + 13 Prozent KV (65 EUR) + 2 Prozent LSt-Pauschale (10 EUR) + U1 + U2 + Insolvenzgeld-Umlage = rund 150-160 EUR. AN-Auszahlung 500 EUR netto, sofern AN von der RV-Pflicht befreit ist; sonst minus AN-RV-Differenzbetrag ca. 18 EUR (3,6 Prozent).

**Typischer Buchungssatz (SKR03/SKR04):** Lohnaufwand Minijob (4128 SKR03 / 6028 SKR04) an Verbindlichkeiten Lohn/Knappschaft (1741 SKR03 / 3760 SKR04). AG-Pauschalabgaben als gesetzliche soziale Aufwendungen (4138 SKR03 / 6128 SKR04). Konkrete Kontennummern je Mandant pruefen.

### Phase 3 — RV-Pflicht und Opt-out

- Grundsatz: Minijob ist RV-pflichtig.
- AN-Beitrag: Differenz zwischen 15 Prozent AG-Pauschale und vollem RV-Beitragssatz (Differenz ca. 3,6 Prozent).
- Opt-out moeglich: AN beantragt schriftlich Befreiung von RV-Pflicht.
- Antrag wirkt ab Beginn des Folgemonats; nicht ruecknahmemoeglich fuer den Minijob.

### Phase 4 — Anmeldung Minijob-Zentrale

- Knappschaft Bahn-See als zentrale Stelle.
- Anmeldung bei Beginn (Sofort wie SV-pflichtige Beschaeftigung).
- Beitragsnachweis spaetestens drittletzter Bankarbeitstag.

### Phase 5 — Aufzeichnungspflicht MiLoG

- § 17 MiLoG: Beginn, Ende und Dauer der taeglichen Arbeitszeit aufzeichnen.
- Bei Minijob Pflicht zur Aufzeichnung; spaetestens am 7. Folgetag.
- Aufbewahrungspflicht 2 Jahre.
- Verstoesse: Bussgeld bis 30.000 EUR.

### Phase 6 — Schwellen-Risiko

- Aushilfen mit jahresweise variierendem Lohn: Jahresdurchschnitt pruefen.
- Bei voraussichtlicher Grenzueberschreitung: rechtzeitig SV-pflichtige Beschaeftigung statt Minijob.
- Bei Grenzueberschreitung rueckwirkend: Nachforderung SV-Beitraege (AG- und AN-Anteil), § 28e SGB IV.

## Output

- Minijob-Abrechnung mit Pauschalabgaben.
- Anmeldung Knappschaft.
- MiLoG-Aufzeichnung dokumentiert.

## Strategie und Praxis-Tipps

- 538 EUR (Stand 01.01.2024) ist nicht statisch — bei MiLo-Erhoehung neue Grenze; jeweils zum Stichtag pruefen.
- Bei wesentlichen Sonderzahlungen Auslegung als regelmaessig im Jahresdurchschnitt — sonst Grenzverletzung.
- Opt-out RV nur bei verstanden vom AN — Nachteil: keine Anrechnung auf RV-Anwartschaft.
- Mehrfache Minijobs: AG haftet nur fuer eigenen Minijob; AN-Pruefpflicht aber.
- StBVV: Minijob in Lohnpauschale; komplexe Sonderfaelle (Sonderzahlungen) Zeithonorar.
- DATEV-Tipp: DATEV LODAS Minijob-Konfiguration prueft automatisch Grenze; bei MiLo-Update jaehrlich anpassen.

## Querverweise

- `stb-lohn-mini-midi-grenzen-2026-stand` — aktuelle Grenzen.
- `stb-lohn-midi-job-uebergangsbereich-2000-euro` — Uebergangsbereich.
- `stb-lohn-sv-beitraege-grundlagen` — SV.
- `stb-lohn-mindestlohn-aktuell-2026-anpassung` — Mindestlohn.
- `stb-lohn-aufzeichnungspflichten-milog` — MiLoG.

## Quellen und Updates

Stand: 05/2026.

- SGB IV §§ 8, 8a, 14.
- SGB VI § 6.
- EStG § 40a.
- MiLoG § 17.
- Gemeinsame Rundschreiben Spitzenverbaende KK.
- Minijob-Grenze 2025: 556 EUR/Monat (MiLo 12,82 EUR). Minijob-Grenze 2026: 603 EUR/Monat (MiLo 13,90 EUR, MiLoV5 v. 05.11.2025, BGBl. 2025 I Nr. 268; Berichtigung Nr. 312). 2027 voraussichtlich 633 EUR/Monat (MiLo 14,60 EUR, MiLoV5).

<!-- AUDIT 27.05.2026 | welle 6 | 5 Marker aufgeloest: 4 bestaetigt (Grenze 556 EUR 2025 eingesetzt), 1 ersetzt (Umlage-Pruefhinweis ohne Marker) -->
<!-- UPDATE 29.05.2026 | MiLoV5: Minijob-Grenze 603 EUR (2026) / voraussichtlich 633 EUR (2027) ergaenzt -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `stb-lohn-sachbezuege-50-euro-freigrenze`

**Fokus:** Sachbezuege 50 EUR Freigrenze § 8 Abs 2 EStG. Anwendungsfall geldwerte Vorteile Gutscheine Sachgeschenke Aufmerksamkeiten Begründung steuerfrei wenn unter 50 EUR/Monat. Methodik Prüfung Sachbezugs-Typ Geldzuwendung-Abgrenzung Loyalitaetsprogramme. Output Sachbezugs-Abrechnung Dokumentation.

# Sachbezuege — 50-EUR-Freigrenze § 8 Abs. 2 EStG

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sachbezuege — 50-EUR-Freigrenze § 8 Abs. 2 EStG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Sachbezuege (geldwerte Vorteile, die nicht in Geld bestehen) sind nach § 8 Abs. 2 Satz 11 EStG steuerfrei, wenn sie monatlich 50 EUR nicht uebersteigen (Anhebung von 44 auf 50 EUR zum 01.01.2022). Voraussetzung: Sachzuwendung, nicht Geldzuwendung. Abgrenzung wichtig — Geldgutscheine sind oft kein Sachbezug. Bei Ueberschreitung der 50-EUR-Grenze ist die GESAMTE Zuwendung steuer- und SV-pflichtig (Freigrenze, nicht Freibetrag).

## Kaltstart-Rueckfragen

1. Welche Art Sachbezug — Warengutschein, Bonusprogramm, Sachzuwendung physisch?
2. Liegt eine Geldzuwendung verkleidet als Sachbezug vor?
3. Hoehe der Sachbezuege im Monat?
4. Werden Sachbezuege mehrfach im Monat oder einmalig gewaehrt?
5. Erfolgt Anrechnung auf den Lohn (Lohnumwandlung)?
6. Wer waehlt die Sachzuwendung (AG oder AN)?
7. Welche Belege liegen vor?
8. Wurde Pauschalierung § 37b EStG gewaehlt (30 Prozent ohne Freigrenze)?

## Rechtlicher Rahmen

### Primaernormen

**§ 8 Abs. 2 Satz 11 EStG** — 50-EUR-Freigrenze fuer Sachbezuege.

**§ 8 Abs. 1 EStG** — Geldzufluss vs. Sachzufluss.

**§ 37b EStG** — Pauschalierung 30 Prozent Sachzuwendungen.

**§ 19 EStG** — Einkuenfte aus nichtselbstaendiger Arbeit.

**ZAG (Zahlungsdiensteaufsichtsgesetz)** — Definition Geld vs. Sachgutschein.

### Verwaltungsanweisungen

- BMF v. 13.04.2021 — Sachbezugs-Definitions-Klarstellung (Gutscheine).
- LStR R 8.1.
- BMF v. 15.03.2022 zu Inflationsausgleichspraemie (Sonderregelung 2022-2024).

## Workflow

### Phase 1 — Sachbezugs-Definition

| Form | Sachbezug? |
|---|---|
| Gutschein/Karte fuer konkretes Geschaeft (z.B. nur Tankstelle) | Ja (Sachbezug) |
| Gutschein nur online einlosbar (Amazon-Gutschein) | Ja bei ZAG-Konformitaet |
| Geldkarte (allgemeine Akzeptanzstelle) | Nein (Geldzuwendung) |
| Kreditkartenguthaben | Nein |
| Mahlzeitenscheck (Pluxee, Edenred) | Ja (Sachbezug) |
| Mitarbeiterrabatt | Spezialregelung § 8 Abs. 3 EStG |
| Firmenwagen | Sachbezug, aber Sonderregelung 1-Prozent |
| Jobticket | Steuerfrei bei AG-Pauschalerstattung |
| Sachgeschenk physisch | Sachbezug |

### Phase 2 — 50-EUR-Pruefung

- Monatlich Summe Sachbezuege je AN.
- Ueberschreitung 50 EUR: die GESAMTE monatliche Zuwendung ist lohnsteuer- und SV-pflichtig — nicht nur der ueberschreitende Teil (Freigrenze, nicht Freibetrag).
- Aufmerksamkeiten zu persoenlichen Anlaessen (Geburtstag, Hochzeit) bis 60 EUR LSt-frei (gesonderte Regelung R 19.6 LStR, nicht Sachbezugs-Freigrenze; vgl. `stb-lohn-betriebsausfluege-aufmerksamkeiten-60-euro`).
- Sachbezugswerte SvEV (Verpflegung, Unterkunft) jaehrlich angepasst (Stand 2025: Verpflegung frei 313 EUR/Monat, Fruehstueck 2,17 EUR, Mittag/Abend je 4,13 EUR; Werte 2026 ueber BMAS/SvEV-VO pruefen).
- Zahlenbeispiel: Tankgutschein 49 EUR + Sachgeschenk 5 EUR im selben Monat = 54 EUR; Folge — vollstaendige Versteuerung der 54 EUR, weil 50-EUR-Grenze ueberschritten.

### Phase 3 — Inflationsausgleichspraemie (2022-2024 — fuer 2026 NICHT mehr anwendbar)

- § 3 Nr. 11c EStG: Bis 3.000 EUR Inflationsausgleichspraemie LSt- und SV-frei, gueltig vom 26.10.2022 bis 31.12.2024.
- Voraussetzung: zusaetzlich zum Lohn; nicht auf bestehende Verguetung umgestellt.
- Bei laufenden Abrechnungen 2026 nicht mehr nutzbar; nur fuer rueckblickende DRV- oder Lohnsteuer-Aussenpruefungen Pruefzeitraum 2022-2024 relevant.

### Phase 4 — Pauschalierung § 37b EStG

- AG kann Sachzuwendungen pauschal mit 30 Prozent (zzgl. KiSt und SolZ) versteuern.
- Wahlrecht; einheitlich fuer alle Empfaenger.
- Vorteil: AN-netto.
- Nachteil: Beitragspflichtig in SV (PE-Pflicht).

### Phase 5 — Dokumentation

- Bezugsbelege im Lohnordner.
- Bei Gutscheinen: Aussteller-Bestaetigung ueber Sachzuwendungs-Charakter.
- Aufzeichnung pro AN-Monat.

### Phase 6 — Lohnabrechnung

- Sachbezug als Sachzuwendung in DATEV LODAS einpflegen.
- Bei Freigrenz-Einhaltung: LSt-frei und SV-frei.
- Bei Ueberschreitung: voll versteuern und verbeitragen.

## Output

- Lohn-Abrechnung mit Sachbezugs-Aufstellung.
- Dokumentation 50-EUR-Pruefung pro AN.
- Belege im Lohnordner.

## Strategie und Praxis-Tipps

- 50-EUR-Freigrenze ist beliebter Gestaltungshebel — bei sorgfaeltiger Dokumentation problemlos.
- Gutscheine streng abgrenzen: BMF v. 13.04.2021 wichtig — nur ZAG-Sachgutscheine zaehlen.
- Aufmerksamkeiten 60 EUR pro persoenlichem Anlass NICHT in 50 EUR-Grenze eingerechnet (eigene Regelung).
- Bei Hochzeitsgeschenk + Geburtstagsgeschenk im selben Monat: beide Aufmerksamkeiten getrennt zu pruefen.
- Pauschalierung § 37b EStG bei groesseren Streuwerbeartikel-Verteilungen sinnvoll.
- StBVV: in Lohnpauschale; Sondergestaltungen Zeithonorar.
- DATEV-Tipp: DATEV LODAS hat eigene Sachbezugs-Konten; bei Mandanten mit Gutscheinprogrammen sorgfaeltige Konfiguration.

## Querverweise

- `stb-lohn-arbeitsvertrag-pruefung-lohn-relevant` — Vertragspruefung.
- `stb-lohn-betriebsausfluege-aufmerksamkeiten-60-euro` — 60-EUR-Aufmerksamkeit.
- `stb-lohn-dienstwagen-1-prozent-fahrtenbuch` — Dienstwagen.
- `stb-lohn-jobticket-mobilitaet-deutschlandticket` — Jobticket.
- `stb-lohn-firmenrad-leasing-jobrad` — JobRad.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 3 Nr. 11c (Inflationsausgleichspraemie 2022-2024), 8, 19, 37b.
- ZAG.
- BMF v. 13.04.2021 (Gutscheine).
- LStR R 8.1.
- Sachbezugsfreigrenze: 50 EUR/Monat (seit 01.01.2022, § 8 Abs. 2 Satz 11 EStG; vorher 44 EUR). SvEV-Sachbezugswerte 2025: Verpflegung frei 313 EUR/Monat; Werte jaehrlich pruefen.

<!-- AUDIT 27.05.2026 | welle 6 | 2 Marker aufgeloest: 2 bestaetigt (50-EUR-Freigrenze seit 2022 und SvEV-Werte 2025 eingesetzt) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 6. `stb-mandanten-onboarding-checkliste-vollservice`

**Fokus:** Onboarding-Checkliste Neumandant Vollservice. Anwendungsfall Mandatsannahme Standardablauf Mandantenvereinbarung Vollmachten DSGVO-Information Buchführung Lohn Steuererklärung. Methodik strukturierter Checkliste. Output Mandantenakte komplett startklar.

# Mandanten-Onboarding-Checkliste Vollservice

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandanten-Onboarding-Checkliste Vollservice` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Bei der Mandatsannahme sind zahlreiche Dokumente, Vollmachten, Vereinbarungen und Stammdaten zu erfassen. Eine standardisierte Checkliste sichert, dass nichts vergessen wird — und schuetzt den Steuerberater vor Haftungsrisiken (z.B. unklare Auftragsumfang).

## Kaltstart-Rueckfragen

1. Welcher Mandantentyp — Einzelunternehmer, Personengesellschaft, GmbH, Konzern?
2. Welcher Leistungsumfang — Buchfuehrung, Lohn, Jahresabschluss, Steuererklaerungen, Beratung?
3. Welcher Vorberater (Datenuebernahme)?
4. Welche Software-Schnittstellen (DATEV Unternehmen Online)?
5. Welche Vollmachten brauchen es (Finanzamt, DRV, Krankenkasse, BG)?
6. Welche AVV / DSGVO-Vereinbarungen?
7. Welche Mandatsvereinbarung (Pauschal, Zeithonorar, Mischmodell)?
8. Welche Mandantenkontakte (Buchhaltung, GF, Personalleitung)?

## Rechtlicher Rahmen

### Primaernormen

**§ 33 StBerG** — StB-Aufgabenkreis.

**§ 57 StBerG** — Gewissenhaftigkeit.

**§ 4 StBVV** — Auftrag erteilt.

**§ 80 AO** — Vollmacht.

**DSGVO Art. 28** — Auftragsverarbeitung (AVV).

**§ 67 StBerG** — Berufshaftpflicht.

## Workflow

### Phase 1 — Mandatsannahme

```
ONBOARDING-CHECKLISTE
Mandant: [Firma / Person]
Mandatsbeginn: [Datum]

A. MANDATSDOKUMENTE
[ ] Mandatsvereinbarung unterzeichnet
[ ] Honorarvereinbarung (Pauschal, Zeit, Gegenstandswert)
[ ] Allgemeine Auftragsbedingungen mitgegeben
[ ] AVV nach DSGVO Art. 28
[ ] Datenschutzhinweise gem. Art. 13 DSGVO ausgehaendigt

B. VOLLMACHTEN
[ ] Vollmacht Finanzamt (§ 80 AO) - alle relevanten Steuerarten
[ ] Vollmacht DRV (SV-Pruefung)
[ ] Vollmacht Krankenkassen
[ ] Vollmacht BG
[ ] Vollmacht IHK/lizenzpflichtige Literaturquelle (Veroeffentlichung)
[ ] Bestellung Empfangsbevollmaechtigter beim FA

C. STAMMDATEN
[ ] Handelsregister-Auszug
[ ] Gesellschaftsvertrag (GmbH)
[ ] Eintrittsdatum aller Gesellschafter
[ ] Steuer-Nr und Steuer-Id
[ ] Bankkonten-Liste
[ ] Adressen, Telefonnummern, Mailadressen
[ ] Ansprechpartner Funktionen

D. SCHNITTSTELLEN
[ ] DATEV Unternehmen Online Konto eingerichtet
[ ] Bank-Online-Banking-Schnittstelle
[ ] eRechnungsempfang konfiguriert
[ ] Lohnprogramm-Schnittstelle (LODAS, externes Lohn)
[ ] BG/Krankenkasse-Zertifikate

E. BUCHFUEHRUNG
[ ] Kontenrahmen festgelegt (SKR 03 / SKR 04)
[ ] BWA-Form ausgewaehlt
[ ] Belegtransfer-Verfahren vereinbart
[ ] Zustaendigkeiten Sachbearbeiter

F. LOHN (falls vereinbart)
[ ] AN-Liste komplett
[ ] ELStAM-Abruf erfolgreich
[ ] SV-Anmeldungen
[ ] Lohnsteuer-Anmelde-Zeitraum
[ ] Berufsgenossenschaft

G. STEUERN
[ ] USt-Voranmelde-Zeitraum
[ ] Steuervorauszahlungen
[ ] Belegabgabe-Routine
[ ] Fristenkalender

H. ESKALATION
[ ] Krisenmandat-Status?
[ ] Hinweispflichten § 102 StaRUG
[ ] BHV-Anzeige falls relevant
```

### Phase 2 — Vorberater-Wechsel

- Vorberater um Datenuebernahme bitten.
- Mandantenakte vom Vorberater erhalten.
- Vorperioden-Daten in DATEV uebernehmen.

### Phase 3 — Risikoanalyse

- Krisensignale-Pruefung (Eigenkapital, SV-Rueckstaende).
- Steuerliche Auffaelligkeiten (laufende BP, anhaengige Einspruchsverfahren).
- Vor-Pruefung der Stammdaten.

### Phase 4 — Mandanten-Information

- Erstgespraech mit Mandant ueber Prozesse.
- DATEV Unternehmen Online Einfuehrung.
- Belegabgabe-Routine erlaeutern.

### Phase 5 — DSGVO-Compliance

- Datenschutzhinweise gemaess Art. 13 DSGVO.
- AVV mit allen Auftragsverarbeitern.
- Sicherheits-Vorkehrungen (verschluesselte Datenuebertragung).

### Phase 6 — Mandantenakte aufbauen

- Papier-Akte (falls noch verwendet) oder digital.
- Strukturierte Ordner (Vertrag, Vollmachten, Stamm, Korrespondenz).
- Wiedervorlage fuer Folgejahr.

## Output

- Vollstaendige Mandantenakte.
- DATEV Unternehmen Online Konto eingerichtet.
- Erste Auswertung erfolgreich.

## Strategie und Praxis-Tipps

- Standardisierte Onboarding-Checkliste reduziert die Fehlerquote erheblich und schuetzt vor Haftungsfaellen (§ 67 StBerG).
- Bei Mandanten mit Konzernstruktur: zentrale Datenkonsolidierung, Konzern-Vollmachten gebearbeitet erfassen.
- Mandatsvereinbarung klar formulieren — definierter Leistungsumfang schuetzt beide Seiten und ist Voraussetzung fuer eine rechtssichere Honorarabrechnung nach StBVV.
- BHV-Anzeige bei erkennbaren Risiken zeitnah (Haftungs-Praeventiv).
- StBVV: Onboarding wahlweise als separater Auftrag nach § 13 StBVV (Beratungstaetigkeit), Pauschalvereinbarung nach § 14 StBVV oder als Teil der laufenden Buchfuehrungspauschale.
- DATEV-Tipp: DATEV Mandanten-Onboarding-Modul mit Checklistensystem; alternative kanzleieigene Checkliste im DMS.

## Querverweise

- `stb-lohn-mandantenaufnahme-onboarding` — Lohn-Onboarding.
- `stb-pruefliste-belegabgabe-monatlich` — Belegabgabe.
- `stb-online-portal-datev-mandantenshop` — DATEV Unternehmen Online.
- `stb-datentransfer-mandant-cloud-dsgvo` — DSGVO im Datenverkehr.

## Quellen und Updates

Stand: 05/2026.

- StBerG §§ 33, 57, 67.
- StBVV § 4.
- AO § 80.
- DSGVO Art. 13, 28.
- DStV-Praxisleitfaden Mandantenaufnahme.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 7. `stb-mandantenkommunikation-bwa-uebergabe-quartal`

**Fokus:** Quartalsgespraech BWA-Übergabe. Anwendungsfall systematische Quartalskommunikation mit Mandant Ergebnisbesprechung Steuerthemen Investitionsplanung. Methodik Termin-Vorbereitung Agenda Dokumentation. Output Quartalsgespraechs-Protokoll Massnahmen-Liste.

# Quartalsgespraech — BWA-Uebergabe mit dem Mandanten

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Quartalsgespraech — BWA-Uebergabe mit dem Mandanten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Das Quartalsgespraech ist Standard fuer mittelstaendische Mandanten: BWA-Besprechung, steuerliche Themen, Investitionsplanung, Personalfragen, Liquiditaet. 1-2 Stunden pro Quartal. Bestaerkt die Mandantenbindung und reduziert spaetere Konflikte. Der Steuerberater bereitet sich systematisch vor, fuehrt das Gespraech strukturiert und dokumentiert die Ergebnisse.

## Kaltstart-Rueckfragen

1. Welche Themen sind im aktuellen Quartal relevant?
2. Welche BWA-Auffaelligkeiten?
3. Welche Steuerthemen anstehend (Vorauszahlungen, USt-Sonderpruefung)?
4. Welche Personalthemen (Eintritte, Austritte, Pruefungen)?
5. Welche Investitionsplaene des Mandanten?
6. Welche Liquiditaet aktuell?
7. Welche Eskalationsthemen (Krisensignale)?
8. Welche externen Stakeholder (Bank, Beirat)?

## Rechtlicher Rahmen

### Primaernormen

**§ 33 StBerG** — StB-Aufgabenkreis.

**§ 57 StBerG** — Gewissenhaftigkeit.

**§ 102 StaRUG** — Hinweispflicht.

**§ 5 RDG** — Abgrenzung Rechtsberatung.

## Workflow

### Phase 1 — Vorbereitung (1 Woche vorher)

- BWA, SuSa, OPOS-Listen durchsehen.
- Vorquartal-Vergleich aufbereiten.
- Steuerliche Themen sammeln (vorausgezahlte Steuern, Investitionsabzugsbetrag § 7g EStG, Sonder-AfA).
- Personalfragen erfassen (Lohnkostenquote, geplante Neueinstellungen, anstehende Tarifaenderungen).
- Agenda an Mandanten ca. 5 Werktage vor Termin per E-Mail senden.

Muster-E-Mail Terminvereinbarung:

```
Sehr geehrte Frau / Herr [Name],

zur Vorbereitung unseres Quartalsgespraechs am [Datum, Uhrzeit] in
[Ort: Ihre Geschaeftsraeume / unsere Kanzlei] erhalten Sie anbei:

- BWA Q[1-4]/[Jahr] mit Vorjahresvergleich
- Aktuelle SuSa und OPOS-Listen
- Vorlaeufige Steuerprognose [Jahr]

Vorgesehene Agenda (Dauer 1-2 Stunden):
1. Quartal in Zahlen
2. BWA-Auffaelligkeiten
3. Steuerliche Themen (inkl. Vorauszahlungs-Anpassung)
4. Liquiditaet, Bank, OPOS-Status
5. Personalthemen
6. Investitionen / Strategie
7. Naechste Schritte

Bitte teilen Sie uns mit, falls Sie weitere Themen aufnehmen moechten.

Mit freundlichen Gruessen
[StB-Kanzlei]
```

### Phase 2 — Termin (1-2 Stunden)

- Teilnehmer: Geschaeftsfuehrung, ggf. kaufmaennische Leitung; auf StB-Seite Sachbearbeiter und Berufstraeger.
- Ort: bevorzugt beim Mandanten (Vor-Ort-Bezug staerkt die Beratungsbeziehung) oder StB-Buero.
- Bei Bewirtung im StB-Buero auf ordnungsgemaessen Bewirtungsbeleg (§ 4 Abs. 5 S. 1 Nr. 2 EStG) achten — geschaeftlicher Anlass, Bewirteten, Hoehe und Datum dokumentieren.
- Agenda-Punkte abarbeiten und Zeitfenster pro Punkt einhalten.

### Phase 3 — Standard-Agenda

```
QUARTALSGESPRAECH AGENDA
Mandant: [Firma]
Quartal: [Q1/2026]
Termin: [Datum, Uhrzeit]

1. Quartal in Zahlen (10 Min)
 - Umsatz, EBIT, Ergebnis
 - Vergleich Plan/Vorquartal/Vorjahresquartal

2. BWA-Auffaelligkeiten (15 Min)
 - Wesentliche Abweichungen
 - Sondereffekte
 - Empfehlungen

3. Steuerliche Themen (15 Min)
 - Steuervorauszahlungen
 - USt-Voranmeldung Quartalsergebnis
 - Investitionsabzugsbetrag § 7g EStG
 - Sonder-AfA Moeglichkeiten

4. Liquiditaet und Bank (10 Min)
 - Bankgespraeche
 - OPOS-Status
 - Liquiditaetsplan

5. Personal (10 Min)
 - Bestand
 - Anstehende Vertraegsaenderungen
 - Lohnerhoehungen, Sonderzahlungen
 - SV-Pruefung in Sicht?

6. Investitionen / Strategie (15 Min)
 - Geplante Investitionen
 - Steuerliche Optimierung
 - Bankfinanzierung

7. Naechste Schritte (5 Min)
 - Termine
 - Aktionspunkte
```

### Phase 4 — Krisengespraech (Sonderfall)

- Bei Krisensignalen: BWA mit Hervorhebung der negativen Kennzahlen vorbereiten (drohende Zahlungsunfaehigkeit, Ueberschuldung, sinkendes Eigenkapital).
- § 102 StaRUG-Hinweispflicht ausdruecklich ansprechen und schriftlich dokumentieren — der Mandant ist auf das Risiko der Insolvenzantragspflicht (§ 15a InsO) und auf die Notwendigkeit anwaltlicher / insolvenzrechtlicher Beratung hinzuweisen.
- Anwalt (Insolvenz- bzw. Sanierungsspezialist) empfehlen — die StB-Hinweispflicht erfuellt keine insolvenzrechtliche Beratung iSv § 5 RDG.
- Dokumentation: Aktenvermerk mit Datum, Inhalt des Hinweises, anwesende Personen; ggf. zusaetzliches Bestaetigungsschreiben an Mandant.

### Phase 5 — Dokumentation (1 Woche nach Termin)

```
GESPRAECHSPROTOKOLL
Datum: [Datum]
Teilnehmer: [Namen, Funktionen]

Behandelte Themen:
1. [Thema] - [Diskussion] - [Vereinbarung]
2. ...

Aktionspunkte:
| Punkt | Verantwortlich | Termin |
| ... | ... | ... |

Naechste Schritte:
- ...
```

### Phase 6 — Wiedervorlage

- DATEV-Kanzleiplaner mit Aktionspunkten.
- Naechster Termin Quartalsgespraech bereits in Kalender.
- Mandant-Verbindlichkeit der Protokoll-Bestaetigung.

## Output

- Gespraechs-Protokoll.
- Aktionspunkte-Liste.
- Wiedervorlage in DATEV-Kanzleiplaner.

## Strategie und Praxis-Tipps

- Quartalsgespraech ist Mandantenbindungs-Instrument — staerkstes verfuegbares Mittel.
- Bei Krisensignalen: Persoenliches Gespraech zwingend, nicht Telefon.
- Vor-Ort-Gespraech beim Mandanten staerker als StB-Buero.
- Bei Familienmandanten: einer der Familie zu jedem Quartal einbinden.
- StBVV: in Pauschalvereinbarung oder separater Auftrag (Beratungs-Honorar).
- Bei Mandanten ohne Quartalsgespraechs-Vereinbarung: anbieten.

## Querverweise

- `stb-bwa-mandantengespraech-uebergabe` — BWA-Uebergabe.
- `stb-jahresgespraech-mandant-bwa-basis` — Jahresgespraech.
- `stb-bwa-mandantenreport-monatlich` — Monatsreport.
- `stb-bwa-fehlerquellen-haeufig` — Krisensignale und Fehlerquellen.
- `stb-mandantenrechnung-honorar-stbvv` — StBVV-Honorar.

## Quellen und Updates

Stand: 05/2026.

- StBerG §§ 33, 57.
- StaRUG § 102.
- RDG § 5.
- DStV-Praxisleitfaden Mandantenkommunikation.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 8. `stb-mandantenrechnung-honorar-stbvv`

**Fokus:** Mandantenrechnung Honorar StBVV. Anwendungsfall Honorarabrechnung Pauschal- Zeit- und Gegenstandswert-Honorar Steuerberatergebührenverordnung. Methodik Rechnungsschreibung Gebührensaetze § 33 35 35a. Output Mandantenrechnung.

# Mandantenrechnung — Honorar nach StBVV

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandantenrechnung — Honorar nach StBVV` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Der Steuerberater rechnet sein Honorar nach der StBVV (Steuerberatervergutungsverordnung) ab. Drei Hauptformen: Pauschalverguetung (in Mandatsvereinbarung), Zeithonorar (bei nicht-routinemaessigen Auftraegen), Gegenstandswert-Gebuehr (bei Jahresabschluss, Steuererklaerungen). Der Steuerberater muss die StBVV strikt einhalten — Abweichungen ohne Mandantenvereinbarung sind rechtswidrig.

## Kaltstart-Rueckfragen

1. Welche Leistung ist abzurechnen — Buchfuehrung, Lohnbuchfuehrung, Jahresabschluss, Steuererklaerung, Beratung?
2. Welche Honorarform mit dem Mandanten vereinbart (Pauschal, Zeit, StBVV-Standard)?
3. Welcher Gegenstandswert ist relevant?
4. Welcher Schwierigkeitsgrad (10/10 unkompliziert, 10/10 schwierig)?
5. Welche Hoechstsatz wurde mit dem Mandanten vereinbart?
6. Liegt schriftliche Pauschalvereinbarung vor?
7. Welche Auslagen (Reisekosten, Portoauslagen)?
8. Welche USt-Saetze?

## Rechtlicher Rahmen

### Primaernormen

**StBVV** — Steuerberatervergutungsverordnung.

**§ 4 StBVV** — Honorarvereinbarung.

**§ 14 StBVV** — Pauschalverguetung.

**§ 33 StBVV** — Buchfuehrung.

**§ 35 StBVV** — Jahresabschluss.

**§ 24 StBVV** — Steuererklaerungen.

**§ 13 StBVV** — Beratungstaetigkeit.

**§ 1 Abs. 1 Nr. 1 UStG** — Steuerbarkeit der StB-Leistung; StB-Honorare sind grundsaetzlich umsatzsteuerpflichtig (Regelsteuersatz 19 %). Eine Steuerbefreiung nach § 4 UStG kommt regelmaessig nicht in Betracht.

### Verwaltungsanweisungen

- BStBK Honorartabellen.

## Workflow

### Phase 1 — Honorarform-Wahl

| Form | Anwendung |
|---|---|
| StBVV-Standard | Klare Rahmenleistung (Jahresabschluss, Steuererklaerung) |
| Pauschalvereinbarung | Laufende Buchfuehrung, Lohnbuchfuehrung, Mandantenpauschale |
| Zeithonorar | Beratung, Sondertaetigkeiten, Pruefungsbegleitung |
| Erfolgsabhaengig | Eingeschraenkt zulaessig (§ 9a StBVV) |

### Phase 2 — Gegenstandswert ermitteln

| Leistung | Gegenstandswert |
|---|---|
| Buchfuehrung | Jahresumsatz, alternativ Geschaeftsvorfaelle |
| Jahresabschluss | Bilanzsumme + Lohnsumme + 50 Prozent Umsatz |
| Steuererklaerung ESt | ZvE des Mandanten |
| Steuererklaerung KSt | Bemessungsgrundlage |
| USt-Voranmeldung | Brutto-Umsatz |
| Pruefungsbegleitung | Pruefungsergebnis |

### Phase 3 — Gebuehrensatz waehlen

- 10/10 = Mittelgebuehr (Standardfall).
- 4/10 bis 18/10 = Bandbreite je nach Schwierigkeit, Bedeutung, Umfang.
- 18/10 Hoechstsatz nur bei aussergewoehnlicher Schwierigkeit, Bedeutung oder Umfang (Begruendung in der Akte dokumentieren).

### Phase 4 — Rechnungs-Inhalt

```
RECHNUNG
StB Steuerberater XYZ
Steuer-Nr: ...
USt-IdNr: ...

An: [Mandant]
Rechnungsnummer: ...
Rechnungsdatum: ...

Leistungsbeschreibung:
1. Jahresabschluss [Jahr]
 Gegenstandswert: [X]
 Gebuehrensatz nach § 35 StBVV: 25/10
 Mittelgebuehr: [Y]
 Faktor: ...
 Honorar netto: [Z]

2. Buchfuehrung Monate [von - bis]
 Gegenstandswert: [X]
 Gebuehrensatz nach § 33 StBVV: 5/10
 Honorar netto: [Z]

3. Auslagen
 Reisekosten EUR [X]
 Porto EUR [X]

Zwischensumme netto: [Z]
USt 19 Prozent: [Y]
Brutto: [Z]

Faellig: [Datum]
Bankverbindung: ...
```

### Phase 5 — Pauschalvereinbarung

- Schriftliche Vereinbarung mit Mandant.
- Pauschalbetrag pro Monat / Jahr.
- Was ist enthalten / was Zusatzauftrag.
- Anpassung jaehrlich oder bei wesentlicher Aenderung.

### Phase 6 — Rechnungsausgabe und Mahnung

- Rechnung mit GoBD-konformen Pflichtangaben.
- Faelligkeit ueblich 14 Tage.
- Bei Verspaetung Mahnung mit Mahnkosten.
- Bei dauerhafter Saeumigkeit: gerichtliches Mahnverfahren bzw. Klage durch Inkassoanwalt.

## Output

- Mandantenrechnung mit StBVV-konformer Berechnung.
- Pauschalvereinbarungen schriftlich.

## Strategie und Praxis-Tipps

- Die StBVV definiert den Mindestrahmen — eine Unterschreitung der Mindestgebuehr ist nur in begruendeten Ausnahmefaellen und unter Beachtung von § 4 StBVV (Hoehe der Verguetung) zulaessig.
- Pauschalvereinbarung ist Standard bei laufender Mandatsbetreuung — Planungssicherheit fuer beide Seiten; Schriftform nach § 14 StBVV beachten.
- Bei Beratungstaetigkeiten ist ein Zeithonorar oft sachgerecht (genaue Erfassung mit Stundenzettel, ggf. Stundensatz nach § 13 StBVV).
- Bei Mandatsende StBVV-Abrechnung konsequent durchsetzen; Transparenz vorab vermeidet Konflikte (Hinweis im Onboarding und Pauschalvertrag).
- USt-Pflicht beachten — StB-Leistungen sind grundsaetzlich USt-pflichtig (Regelsteuersatz 19 %).

## Querverweise

- `stb-mandanten-onboarding-checkliste-vollservice` — Onboarding.
- `stb-mandantenanfrage-reaktion-frist-laufend` — Reaktionsfristen.
- `stb-bwa-monatsabschluss-routine` — Buchfuehrungs-Routine.

## Quellen und Updates

Stand: 05/2026.

- StBVV §§ 4, 9a, 13, 14, 24, 33, 35.
- BStBK Honorartabellen.
- UStG.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 9. `stb-pruefliste-belegabgabe-monatlich`

**Fokus:** Prüfliste monatliche Belegabgabe. Anwendungsfall standardisierte Belegabgabe-Kontrolle Mandant Vollständigkeit Bankauszuege Kasse Eingangsrechnungen Ausgangsrechnungen Lohnauswertung. Methodik Prüfliste Eingangskontrolle Mahnung. Output Prüfprotokoll Belegmahnung.

# Pruefliste monatliche Belegabgabe

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Pruefliste monatliche Belegabgabe` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die Belegabgabe-Disziplin des Mandanten ist Erfolgsfaktor der Monatsabschluss-Routine. Fehlt ein Beleg, verzoegert sich die BWA, die USt-VA wird ungenau, der Jahresabschluss bekommt Probleme. Der Steuerberater fuehrt eine Pruefliste, prueft die Vollstaendigkeit eingegangener Belege und mahnt bei Verzoegerungen. Bei wiederholten Verspaetungen Honoraranknuepfung oder Eskalation.

## Kaltstart-Rueckfragen

1. Welche Belegart wird abgegeben (Papier, DUO, scan-zentrum)?
2. Welche Frequenz vereinbart (taeglich, woechentlich, monatlich)?
3. Welche Mandantenbranche und Belegvolumen?
4. Welche Sondervorgaenge in der Periode (Reisekosten, Geschenke)?
5. Welche Frist fuer Belegabgabe?
6. Welche Eskalation bei Verspaetung?
7. Welche Wiederkehrenden Belegart (Mieten, Versicherungen)?
8. Welcher Eskalationsstand?

## Rechtlicher Rahmen

### Primaernormen

**§ 146 AO** — Zeitgerechtigkeit, Vollstaendigkeit.

**§ 147 AO** — Aufbewahrung.

**§ 90 AO** — Mitwirkungspflicht Mandant.

**§ 33 StBerG** — StB-Aufgabenkreis.

**§ 4 StBVV** — Honorarvereinbarung.

## Workflow

### Phase 1 — Standard-Pruefliste

```
BELEGABGABE-PRUEFLISTE
Mandant: [Firma]
Monat: [Monat]

A. BANK
[ ] Alle Bankauszuege fuer den Monat
[ ] PSD2-Online-Banking-Anbindung funktioniert
[ ] Ueberweisungen mit Verwendungszweck

B. KASSE
[ ] Kassenbuch komplett
[ ] Z-Bons taeglich
[ ] Tageseinnahmen-Aufzeichnung GoBD-konform

C. EINGANGSRECHNUNGEN
[ ] Lieferantenrechnungen alle erfasst
[ ] eRechnungen empfangen
[ ] Beleg-Pruefung (USt-Pflichtangaben)

D. AUSGANGSRECHNUNGEN
[ ] Kundenrechnungen alle erfasst
[ ] eRechnungs-Versand (B2B Pflicht seit 01.01.2025)
[ ] Skonti-Belege

E. LOHN
[ ] Lohnauswertung aus Lohnprogramm
[ ] SV-Beitragsbescheide
[ ] Sondervergueteungen, Boni

F. SONSTIGE
[ ] Reisekosten-Belege
[ ] Bewirtungsbelege
[ ] Geschenk-Belege
[ ] Kfz-Belege
[ ] Versicherungs-Bescheide
[ ] FA-Bescheide

G. SONDERVORGAENGE
[ ] Anlagenkauf/-verkauf
[ ] Darlehensvereinbarungen
[ ] Gesellschaftervereinbarungen

H. STATUS
Belege vollstaendig: [Ja/Nein]
Fehlende Belege: [Liste]
Mahnstand: [keine / 1. / 2. Mahnung]
```

### Phase 2 — Eingangskontrolle

- Mandant uebermittelt Belege.
- Sachbearbeiter laed in DATEV.
- Vollstaendigkeit pruefen (Bank-Cut-off: alle Buchungen bis Monatsende erfasst; Lohnbuchungen aus dem Lohnprogramm mit gleicher Periode synchron).

### Phase 3 — Mahnung bei Verspaetung

- Stufe 1: telefonische Nachfrage.
- Stufe 2: schriftliche Erinnerung (E-Mail).
- Stufe 3: Mandantenakte mit Vermerk; ggf. Honorar-Aufschlag.
- Stufe 4: Mandantenniederlegung (§ 627 BGB) im Extremfall.

### Phase 4 — Belege fuer wiederkehrende Vorgaenge

- Miet-, Pacht-, Leasing-Vertraege als Stamm-Dokumente einmalig erfassen (jaehrliche Anpassung pruefen).
- Versicherungs-Bescheide jaehrlich (Pruefung Versicherungssumme, Beitragsanpassung).
- Dauerauftraege fuer Strom, Heizung, Wasser, Telekommunikation (Buchung als wiederkehrend); Jahresabrechnungen separat erfassen.

### Phase 5 — Bei Verlust eines Beleges

- Mandant um Ersatzbeleg bitten.
- Schaetzung (mit Vermerk) als letzte Option.
- Bei wiederholten Verlusten: GoBD-Risiko.

### Phase 6 — Reporting an Mandant

- Bei jedem Monatsabschluss: Pruefprotokoll mit Status.
- Bei wesentlichen Maengeln: Mandantengespraech.

## Output

- Pruefprotokoll Belegabgabe.
- Mahnung bei Verspaetung.
- Mandantenakte aktualisiert.

## Strategie und Praxis-Tipps

- Pruefliste konsequent durchgehen — fehlende Belege sind haeufige Ursache von Buchungsfehlern.
- Bei wiederholten Verzoegerungen: Honorar-Aufschlag (z.B. 25 Prozent Eilzuschlag) abrechnen.
- DATEV-DUO ist Effizienz-Hebel — Mandanten konsequent zur Nutzung ermutigen.
- StBVV: in Pauschal; Eilbearbeitung Sonderhonorar.
- DATEV-Tipp: DATEV DUO Belegfluss-Statistik nutzen.

## Querverweise

- `stb-bwa-monatsabschluss-routine` — Monatsabschluss.
- `stb-online-portal-datev-mandantenshop` — DUO.
- `stb-belegtransfer-datev-unternehmen-online` — Belegtransfer.
- `stb-mandantenanfrage-reaktion-frist-laufend` — Mandantenanfragen.

## Quellen und Updates

Stand: 05/2026.

- AO §§ 90, 146, 147.
- StBerG § 33.
- StBVV § 4.
- BMF v. 28.11.2019 zu GoBD.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
