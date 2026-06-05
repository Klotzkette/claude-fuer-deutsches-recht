---
name: steuer-bwa-aufbau-grundlagen-mandantengespraech-uebergabe
description: "Steuer BWA Aufbau Grundlagen Mandantengespraech Uebergabe: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Steuer BWA Aufbau Grundlagen Mandantengespraech Uebergabe

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **Steuer BWA Aufbau Grundlagen Mandantengespraech Uebergabe** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stb-bwa-aufbau-grundlagen` | Aufbau der Standard-BWA für Steuerberater erlaeutern und konfigurieren. Anwendungsfall monatliche oder quartalsweise BWA-Erstellung für GmbH oder Personenunternehmen mit SKR 03 oder SKR 04. Struktur Umsatzerlöse Material Personal sonstige betriebliche Aufwendungen Abschreibungen Zinsergebnis Steuern. Output strukturierter BWA-Bericht mit Erlaeuterung der einzelnen Positionen Querverweis stb-bwa-kontenrahmen-skr03-skr04 und stb-bwa-erlaeuterungstext-mandant. |
| `stb-bwa-mandantengespraech-uebergabe` | BWA-Übergabegespraech mit dem Mandanten. Anwendungsfall persoenliche oder telefonische Besprechung der monatlichen oder quartalsweisen BWA mit dem GF Klaerung der Abweichungen Steuerungsempfehlungen Risikoeskalation. Methodik Vorbereitung Agenda Gespraechsleitfaden Dokumentation. Output Gespraechsnotiz mit Massnahmen-Liste. |
| `stb-bwa-monatsabschluss-routine` | Routine für den Monatsabschluss in der Steuerberater-Kanzlei. Anwendungsfall monatliche BWA-Erstellung in einem standardisierten 30-Tage-Zyklus mit Belegabgabe Buchung Abstimmung BWA-Versand. Schritte Belegannahme Buchung GoBD-konform OPOS-Pflege Lohnbuchung-Integration Bestand-Schaetzung Periodenabgrenzung Auswertung. Output Monatsendreport Termincontrolling Querverweis stb-routine-monatsabschluss-30-tage-zyklus. |
| `stb-bwa-soll-ist-vergleich` | Soll-Ist-Vergleich in der BWA. Anwendungsfall Monats- oder Quartals-BWA mit Plan-Werten aus Wirtschaftsplan Unternehmensplanung Forecast. Methodik Planeingabe Abweichungsanalyse Steuerungsempfehlung. Output BWA mit Spalte Plan Ist Abweichung Erlaeuterungstext für Mandant Querverweis stb-bwa-mandantenreport-monatlich. |
| `stb-drv-sozialversicherungspruefung` | Steuerberater-Begleitung der DRV-Sozialversicherungsprüfung nach § 28p SGB IV. Anwendungsfall Mandant-GmbH erhaelt DRV-Prüfankündigung oder Prüfung laeuft bereits. Prüfungsschwerpunkte Statusfeststellung GF Scheinselbstständigkeit Mini- und Midijobs Phantomlohn Mindestlohn BAGB. Strafbarkeit § 266a StGB vorenthaltene Arbeitnehmer-Beitraege Haftungsrisiko GF § 69 AO Lohnsteuer-Aussenprüfung Verknuepfung. Output Mitwirkungsdokumentation Anhoerungsschreiben Widerspruchsvorlage. Abgrenzung zu anw-gf-haftung-69-ao-nicht-abgeführte-steuern GF-Haftung Steuer. |
| `stb-jahresabschluss-abgrenzungen-rap-rai` | Rechnungsabgrenzungsposten RAP aktiv und passiv. Anwendungsfall Jahresabschluss-Buchung Versicherung Miete Kfz-Steuer Vorauszahlungen periodengerechte Zuordnung. Methodik Identifikation Berechnung Buchung. Output Periodengerechte JA-Bestaende. |
| `stb-jahresabschluss-elektronische-uebermittlung-ebilanz` | E-Bilanz § 5b EStG elektronische Übermittlung. Anwendungsfall Bilanzierer Pflicht zur elektronischen Übermittlung der Steuerbilanz an FA Taxonomie-Standard. Methodik DATEV-E-Bilanz Modul. Output E-Bilanz uebermittelt. |
| `stb-jahresabschluss-handels-vs-steuerbilanz` | Handelsbilanz vs Steuerbilanz Massgeblichkeit § 5 EStG. Anwendungsfall Prüfung Abweichungen Handels- und Steuerbilanz Massgeblichkeitsprinzip umgekehrte Massgeblichkeit Wahlrechte. Methodik Differenz-Tabelle Bewertungs-Unterschiede. Output Steuerbilanz oder Überleitungsrechnung. |
| `stb-jahresabschluss-rueckstellungen-bewertung` | Rückstellungen Bewertung § 249 HGB. Anwendungsfall Jahresabschluss Bildung Rückstellungen Garantie drohende Verluste Tantieme Urlaub Steuern Prozesskosten. Methodik Prüfung Anlass Quantifizierung Auflösung. Output Rückstellungs-Aufstellung. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **Steuer BWA Aufbau Grundlagen Mandantengespraech Uebergabe**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stb-bwa-aufbau-grundlagen`

**Fokus:** Aufbau der Standard-BWA für Steuerberater erlaeutern und konfigurieren. Anwendungsfall monatliche oder quartalsweise BWA-Erstellung für GmbH oder Personenunternehmen mit SKR 03 oder SKR 04. Struktur Umsatzerlöse Material Personal sonstige betriebliche Aufwendungen Abschreibungen Zinsergebnis Steuern. Output strukturierter BWA-Bericht mit Erlaeuterung der einzelnen Positionen Querverweis stb-bwa-kontenrahmen-skr03-skr04 und stb-bwa-erlaeuterungstext-mandant.

# Aufbau der Standard-BWA — Grundlagen fuer Steuerberater

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Aufbau der Standard-BWA — Grundlagen fuer Steuerberater` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die Betriebswirtschaftliche Auswertung (BWA) ist das zentrale unterjaehrige Steuerungsinstrument. Steuerberater erstellen sie monatlich oder quartalsweise aus der Finanzbuchhaltung. Die Standard-BWA (DATEV-BWA-Form 01) liefert in fuenf Bloecken einen periodengerechten Erfolgsausweis: Umsatzerloese, Material- und Wareneinsatz, Personalkosten, sonstige betriebliche Aufwendungen, Abschreibungen sowie Zinsergebnis und Steuern. Der Skill leitet die Konfiguration und die korrekte Befuellung der Standard-BWA an und stellt sicher, dass die wirtschaftlich relevanten Aussagen sauber ablesbar sind.

## Kaltstart-Rueckfragen

1. Welcher Kontenrahmen liegt vor — SKR 03 oder SKR 04? Welche Standard-BWA-Form (BWA 01 kurz, BWA 01 lang, kumuliert)?
2. Welche Branche und Rechtsform — Industrie, Handel, Dienstleistung, Freiberufler, GmbH, Einzelunternehmen?
3. Welcher Auswertungszeitraum — Monat, Quartal, kumuliert seit Jahresbeginn?
4. Soll ein Vorjahresvergleich, Vormonatsvergleich oder Soll-Ist-Vergleich integriert werden?
5. Welche Periodenabgrenzungen sind vorgesehen — laufende Abgrenzungen (RAP) monatlich, vereinfacht jaehrlich oder gar nicht?
6. Sind die Personalkosten brutto oder mit Arbeitgeberanteilen erfasst? Liegen Daten aus dem Lohnprogramm zeitnah vor?
7. Ist eine kalkulatorische Position vorgesehen (kalkulatorischer Unternehmerlohn, kalkulatorischer Mietzins)?
8. Welche Empfaengerformatierung wuenscht der Mandant — knappe Uebersicht, ausfuehrliche BWA, mit Grafiken?

## Rechtlicher Rahmen

### Primaernormen

**§ 238 HGB** — Buchfuehrungspflicht des Kaufmanns; Grundlage der BWA als unterjaehrige Auswertung der laufenden Buchfuehrung.

**§ 240 HGB** — Inventarpflicht; periodische Bestandsaufnahme fliesst in BWA-Aufwand "Bestandsveraenderung" ein.

**§ 252 HGB** — Allgemeine Bewertungsgrundsaetze (Going-concern, Stichtagsprinzip, Vorsicht); auch unterjaehrig zu beachten.

**§ 5b EStG** — E-Bilanz fuer Bilanzierer; BWA ist nicht direkt taxonomiepflichtig, soll aber die Brueckenposten zur E-Bilanz abbilden.

**§ 90 AO** — Mitwirkungspflicht des Steuerpflichtigen; betrifft die fuer die BWA noetige Belegabgabe.

**§ 33 StBerG** — Aufgaben des Steuerberaters; Erstellung der BWA ist Hilfeleistung in Steuersachen i.S.d. § 1 StBerG bzw. vereinbare Taetigkeit § 57 Abs. 3 StBerG.

### Leitentscheidungen und Verwaltungsanweisungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BFH-Rechtsprechung zur periodengerechten Zuordnung von Aufwand und Ertrag: massgeblich sind die allgemeinen Grundsaetze des § 252 HGB und die EStG-Periodenregelungen; konkrete BFH-Aktenzeichen zur Periodenabgrenzung in amtliche/freie Quellen oder lizenzierte Datenbanken unter den Suchbegriffen "Periodenabgrenzung Betriebsausgaben" abrufbar.
- BMF-Schreiben zu GoBD: massgeblich ist das BMF-Schreiben v. 28.11.2019, BStBl I 2019, 1269; etwaige Aktualisierungen ueber bundesfinanzministerium.de pruefen.
- IDW PS 480 — Grundsaetze fuer die Erstellung von Jahresabschluessen (analog fuer hochwertige BWA-Erstellung).

Aktenzeichen und Fundstellen vor Uebernahme in amtliche/freie Quellen oder lizenzierte Datenbanken gegenpruefen.

## Workflow

### Phase 1 — Datenbasis pruefen

- Vollstaendigkeit der Buchungen pruefen: Bank-Kontoauszuege bis zum Stichtag verbucht, Kassenbuch abgestimmt, OPOS-Listen Debitor und Kreditor aktualisiert.
- Vorlaeufige Sachkontenverteilung im Verrechnungskonto (z. B. SKR 03 Konto 1590/1599 bzw. SKR 04 Konto 1370/1379 — DATEV-Kontenrahmen aktuelle Fassung heranziehen) auf Null stellen oder klar dokumentieren.
- Lohnbuchungen aus dem Lohnprogramm uebernommen? Sozialversicherungs-Beitragsschulden zum Auswertungsstichtag erfasst (Konto SKR 03 1742 bzw. SKR 04 3740 fuer Verbindlichkeiten SV)?
- Belege chronologisch und vollstaendig verbucht; Cut-off-Datum festlegen (z. B. 5. Werktag des Folgemonats).
- DATEV-Klickpfad zur Pruefung: Rechnungswesen → Stammdaten → Buchungsstapel → Stapelverarbeitung → noch nicht festgeschriebene Buchungen vor BWA festschreiben.

### Phase 2 — Periodenabgrenzungen

- Aktive Rechnungsabgrenzungsposten (Versicherung, Miete, Kfz-Steuer) anteilig auf Monate verteilen.
- Rueckstellungen monatlich anteilig: Urlaubsrueckstellung, Tantiemen, Berufsgenossenschaft.
- Bestandsveraenderung Roh- Hilfs- Betriebsstoffe und unfertige Erzeugnisse — wenigstens quartalsweise schaetzen.
- Abschreibungen monatlich oder jahresanteilig (1/12-Methode) buchen.

### Phase 3 — BWA-Struktur befuellen

Die Standardgliederung in fuenf Bloecken (Kontennummern typische SKR-Bereiche, im Einzelfall mit aktueller DATEV-Kontenrahmenfassung abgleichen):

1. **Umsatzerloese und sonstige betriebliche Ertraege** — Erloesbereich SKR 03 8000-8999 bzw. SKR 04 4000-4999.
2. **Material- und Wareneinsatz** — Wareneingang, Roh-, Hilfs- und Betriebsstoffe, Fremdleistungen (SKR 03 ab 3000 bzw. SKR 04 ab 5000).
3. **Personalkosten** — Loehne und Gehaelter, Sozialversicherungsanteile AG, Berufsgenossenschaft, sonstige Personalnebenkosten (SKR 03 ab 4100 bzw. SKR 04 ab 6000).
4. **Sonstige betriebliche Aufwendungen** — Raumkosten, Betriebsbedarf, Kfz-Kosten, Werbe- und Reisekosten; Abschreibungen werden meist separat als eigene Position ausgewiesen.
5. **Zinsergebnis und Steuern** — Zinsaufwand, Zinsertrag, Gewerbesteuer-Rueckstellungen, Koerperschaftsteuer-Vorauszahlungen.

### Phase 4 — Plausibilisierung

- Umsatzerloese gegen Vorjahres-Monatsumsatz pruefen: Abweichung mehr als 20 Prozent (Daumenregel) inhaltlich klaeren.
- Materialquote (Materialeinsatz im Verhaeltnis zum Umsatz): branchentypisch ca. 30-50 Prozent in der Industrie, ca. 60-80 Prozent im Handel, ca. 0-20 Prozent bei Dienstleistung. Konkrete Branchenwerte aus DATEV-BBE-Branchenvergleich abrufen (BBE-Datenstand typischerweise 1-2 Jahre Zeitverzug).
- Personalquote (Personalkosten zu Umsatz): bei Dienstleistung typisch ca. 35-55 Prozent (Branchenrichtwert, Verifikation in BBE Branchenkennzahlen empfohlen).
- Ergebnis vor Steuern auf Konsistenz zur Summen- und Saldenliste pruefen — Endsaldo der Erfolgskonten muss mit BWA uebereinstimmen.

### Phase 5 — BWA-Ausgabe und Erlaeuterung

- BWA als PDF mit Mandantenkopf und Zeitstempel ausgeben.
- Kurz-Erlaeuterung unter die BWA setzen (max. 5-7 Saetze): wesentliche Abweichungen, Verfahrensschritte (z.B. Schaetzung Bestand), Hinweis auf offene Punkte.
- Mandantenbezogene Hinweise zu Steuervorauszahlungen und Liquiditaet.

### Phase 6 — Archivierung GoBD-konform

- BWA elektronisch im Mandanten-Ordner gesichert ablegen (revisionssicher, unveraenderbar).
- Aufbewahrungsfrist 10 Jahre nach § 257 HGB / § 147 AO beachten.

## Output

- Standard-BWA als strukturierter Bericht mit funf Blocken, Vorjahresvergleich und kumuliertem Jahresblock.
- Erlaeuterungstext fuer den Mandanten (1-2 Seiten).
- Hinweise zur Liquiditaetslage und zu offenen Buchungsfragen.

## Strategie und Praxis-Tipps

- Auswertungsstichtag spaetestens 30 Tage nach Ablauf des Auswertungsmonats vereinbaren — sonst verliert die BWA Steuerungswirkung.
- BWA monatlich konsistent strukturieren; Wechsel der Auswertungslogik verwirrt den Mandanten und macht Vergleiche unmoeglich.
- Mandant fruehzeitig auf typische Sondereffekte hinweisen (Sonderabschreibung, Investitionsabzugsbetrag § 7g EStG, Sonderzahlungen).
- Honorar nach StBVV § 33 (Buchfuehrung) und § 35 (Lohnbuchfuehrung) abrechnen, Zusatzleistung BWA-Auswertung gesondert.
- Bei wiederholten Buchungsfehlern Mandanten-Belegabgabe disziplinieren — Checkliste an Mandanten verteilen.
- Bei Krisensignalen aus BWA: Querverweis zu stb-bwa-sus-bilanz-pruefung und Hinweispflicht § 102 StaRUG pruefen.

## Querverweise

- `stb-bwa-kontenrahmen-skr03-skr04` — Wahl SKR 03 oder SKR 04.
- `stb-bwa-monatsabschluss-routine` — Routine fuer die Monats-BWA.
- `stb-bwa-erlaeuterungstext-mandant` — Erlaeuterungstexte unter der BWA.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung mit BWA SuSa und Bilanz.
- `stb-bwa-fehlerquellen-haeufig` — typische Fehler beim BWA-Aufbau.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 240, 252, 257.
- EStG § 5b (E-Bilanz).
- AO § 147 (Aufbewahrung).
- BMF-Schreiben zu GoBD (massgeblich: BMF v. 28.11.2019, BStBl I 2019, 1269; etwaige Folgeschreiben ueber bundesfinanzministerium.de abrufen).
- DATEV Standard-BWA Form 01.
- StBerG §§ 1, 33, 57 Abs. 3.
- Verifikations-Hinweis: Bei Reformen des Kontenrahmens (DATEV-Updates jaehrlich) Aktualisierung der BWA-Konfiguration pruefen. Aktenzeichen vor Mandantenversand in amtliche/freie Quellen oder lizenzierte Datenbanken gegenpruefen.

<!-- AUDIT 27.05.2026 | welle 6 | 5 Marker aufgeloest: 1 bestaetigt (GoBD-Fundstelle BMF 28.11.2019 bestaetigt), 4 ersetzt (Formulierungen ohne Marker neu gefasst) -->

## 2. `stb-bwa-mandantengespraech-uebergabe`

**Fokus:** BWA-Übergabegespraech mit dem Mandanten. Anwendungsfall persoenliche oder telefonische Besprechung der monatlichen oder quartalsweisen BWA mit dem GF Klaerung der Abweichungen Steuerungsempfehlungen Risikoeskalation. Methodik Vorbereitung Agenda Gespraechsleitfaden Dokumentation. Output Gespraechsnotiz mit Massnahmen-Liste.

# BWA-Uebergabegespraech mit dem Mandanten

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `BWA-Uebergabegespraech mit dem Mandanten` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die schriftliche BWA mit Erlaeuterungstext ist das eine; das Gespraech mit dem Mandanten das andere. Bei wesentlichen Abweichungen, bei Krisensignalen und bei strategischen Entscheidungen ist das persoenliche oder zumindest telefonische Gespraech der Standard. Der Steuerberater bereitet sich vor, fuehrt das Gespraech strukturiert, dokumentiert die Ergebnisse und vereinbart Folgemassnahmen. Das Gespraech ist auch Haftungsschutz: was muendlich besprochen wurde, ist in der Gespraechsnotiz festzuhalten.

## Kaltstart-Rueckfragen

1. Welcher Anlass — Standardquartalsgespraech, Sondergespraech wegen Auffaelligkeit, Krisengespraech?
2. Wer nimmt teil — GF allein, mit kfm. Leitung, mit Aufsichtsrat oder Gesellschafter?
3. Welche Themenliste — nur BWA-Besprechung oder auch USt-, Lohn-, Investitionsfragen?
4. Welcher Zeitrahmen — 30 Minuten, 1 Stunde, ganztaegig?
5. Welche Unterlagen liegen vor — BWA, SuSa, OPOS, Lohn-Auswertung, Liquiditaetsplan?
6. Welche Beschluesse muessen herbeigefuehrt werden (Investition, Personal, Bankgespraech)?
7. Welche Eskalations-Themen sind vorbereitet (Krisensignale, Insolvenzgrund)?
8. Welche Anschluss-Schritte sind vereinbart (Folgetermin, Schriftverkehr)?

## Rechtlicher Rahmen

### Primaernormen

**§ 33 StBerG** — Aufgabenkreis StB.

**§ 57 Abs. 1 StBerG** — Gewissenhaftigkeit; auch in der Beratung.

**§ 102 StaRUG** — Hinweispflicht bei Krisensignalen; im Gespraech persoenlich auszusprechen.

**§ 31 StBerG** — Selbstaendigkeit; eigenverantwortliche Beurteilung.

**§ 5 RDG** — Abgrenzung Rechtsberatung; bei rechtlichen Themen Verweis auf Anwalt.

### Standards

- IDW PS 480 (Erstellungsgrundsaetze).
- BStBK Berufsrichtlinien.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Workflow

### Phase 1 — Vorbereitung

- BWA und Erlaeuterungstext durchsehen, wesentliche Abweichungen markieren.
- SuSa und OPOS-Liste vorbereiten.
- Bei groesseren Mandanten: Liquiditaetsplan (3-Wochen oder 3-6-12 Monate).
- Krisensignale identifizieren (Eigenkapital, SV-Rueckstaende, Liquiditaetsluecke).
- Agenda schriftlich vorbereiten und 1-2 Tage vor Termin an Mandant senden.

### Phase 2 — Agenda-Struktur

```
AGENDA QUARTALSGESPRAECH
Mandant: [Firma] GmbH
Termin: [Datum, Uhrzeit]
Teilnehmer: [GF Mandant, StB, ggf. Sachbearbeiter]

1. Ergebnisuebersicht Quartal [X]
2. Wesentliche Abweichungen vs. Plan und Vorjahr
3. Liquiditaetslage und OPOS
4. Steuerliche Themen (USt, vorausgezahlte Steuern)
5. Lohn- und Personalkosten
6. Investitions- und Finanzierungsfragen
7. Ausblick und Massnahmen-Plan
8. Anschluss-Termin und naechste Schritte
```

### Phase 3 — Gespraechsfuehrung

- Top-down: zuerst Gesamtergebnis, dann Einzelpositionen.
- Mandant aktiv einbinden: "Sehen Sie das auch so?", "Welche Ursachen vermuten Sie?".
- Bei Krisensignalen direkt ansprechen: "Ich muss Sie auf folgendes ausdruecklich hinweisen ..." (§ 102 StaRUG).
- Empfehlungen klar formulieren, mit Verantwortlichkeit und Zeitleiste.
- Keine Rechtsberatung — bei rechtlichen Fragen Verweis auf Anwalt.

### Phase 4 — Krisengespraech (Sonderfall)

- Bei Hinweispflicht-Auslosung (§ 102 StaRUG): Persoenliches Gespraech mit GF.
- Klare Aussage zu Krisenursachen: Eigenkapital, Liquiditaet, SV-Rueckstaende.
- Empfehlung zur Anwaltskonsultation (Insolvenzrecht, Sanierungsrecht).
- Mandant moeglichen Wegfall der Mandatsbasis (§ 627 BGB) signalisieren.
- Gespraechsergebnis schriftlich bestaetigen (Warnschreiben).

### Phase 5 — Dokumentation

```
GESPRAECHSNOTIZ
Datum / Uhrzeit: [Datum, 14:00-15:30 Uhr]
Teilnehmer: [Namen und Funktionen]
Anlass: Quartalsgespraech [Q1/2026]

KERNTHEMEN:
1. [Thema A] — Aussage / Vereinbarung
2. [Thema B] — Aussage / Vereinbarung
...

VEREINBARTE MASSNAHMEN:
| Massnahme | Verantwortlich | Termin |
|---|---|---|
| ... | ... | ... |

OFFENE PUNKTE:
- [...]

ANSCHLUSS-TERMIN: [Datum]
```

### Phase 6 — Nachgang

- Gespraechsnotiz binnen 3 Tagen an Mandant senden mit Bitte um Bestaetigung.
- Massnahmen in DATEV-Wiedervorlage oder Tasksystem eintragen.
- Bei Krisengespraech: Warnschreiben separat per Einschreiben.

## Output

- Gespraechsnotiz mit Massnahmenliste.
- Wiedervorlage-Eintrag fuer Folgetermin.
- Ggf. Warnschreiben § 102 StaRUG.

## Strategie und Praxis-Tipps

- Quartalsgespraech als Standard mit allen wichtigen Mandanten — staerkste Mandantenbindung.
- Bei Krisensignalen: persoenliches Gespraech nicht durch E-Mail ersetzen.
- Gespraechsnotiz ist Haftungsschutz — was schriftlich dokumentiert ist, gilt.
- StBVV: Gespraech als Zusatzleistung; Pauschalvereinbarung mit Gespraechs-Kontingent moeglich.
- Bei wiederholten Krisensignalen ohne Reaktion: Mandatsniederlegung § 627 BGB pruefen, mit anwaltlicher Begleitung.

## Querverweise

- `stb-bwa-erlaeuterungstext-mandant` — Erlaeuterungstext.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung.
- `stb-warnschreiben-krisensignale` — Warnschreiben.
- `stb-mandantenkommunikation-bwa-uebergabe-quartal` — Quartalsgespraech.
- `stb-jahresgespraech-mandant-bwa-basis` — Jahresgespraech.

## Quellen und Updates

Stand: 05/2026.

- StBerG §§ 31, 33, 57.
- StaRUG § 102.
- RDG § 5.
- BGB § 627.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BStBK Berufsrichtlinien.

## 3. `stb-bwa-monatsabschluss-routine`

**Fokus:** Routine für den Monatsabschluss in der Steuerberater-Kanzlei. Anwendungsfall monatliche BWA-Erstellung in einem standardisierten 30-Tage-Zyklus mit Belegabgabe Buchung Abstimmung BWA-Versand. Schritte Belegannahme Buchung GoBD-konform OPOS-Pflege Lohnbuchung-Integration Bestand-Schaetzung Periodenabgrenzung Auswertung. Output Monatsendreport Termincontrolling Querverweis stb-routine-monatsabschluss-30-tage-zyklus.

# Monatsabschluss-Routine fuer den Steuerberater

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Monatsabschluss-Routine fuer den Steuerberater` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Die wirtschaftliche Aussagekraft einer BWA haengt entscheidend von der Disziplin des Monatsabschluss-Zyklus ab. Ohne klaren Prozess verzoegert sich die BWA, der Mandant verliert das Vertrauen, Krisensignale werden zu spaet erkannt. Dieser Skill etabliert eine reproduzierbare 30-Tage-Routine, die in DATEV oder Addison genauso funktioniert wie in Sage oder BuchhaltungsButler — mit klar zugeordneten Verantwortlichkeiten zwischen Mandant, Sachbearbeiter und Berufstraeger.

## Kaltstart-Rueckfragen

1. Welcher Mandant — Belegvolumen, Komplexitaet, Kontenrahmen?
2. Welche Belegabgabe-Form ist vereinbart — Papier, DATEV Unternehmen Online, BuchhaltungsButler, scan-zentrum?
3. Welcher Auswertungstermin ist mit dem Mandanten verbindlich vereinbart — bis zum 15., 20., 25. des Folgemonats?
4. Wer bucht (Sachbearbeiter), wer prueft (Berufstraeger), wer versendet?
5. Liegen Lohnbuchungen aus dem Lohnprogramm rechtzeitig vor (in der Regel Monatsmitte des Folgemonats)?
6. Welche Periodenabgrenzungen werden routinemaessig gebucht (RAP, Rueckstellungen, Abschreibungen)?
7. Gibt es Sonderpflichten — Konzernanforderung, Bankreporting, fortlaufender Liquiditaetsplan?
8. Welche Eskalation bei verspaeteter Belegabgabe (Mahnung, Honorar-Aufschlag, BWA-Verschiebung)?

## Rechtlicher Rahmen

### Primaernormen

**§§ 238, 239 HGB** — Buchfuehrungspflicht und ordnungsgemaesse Buchfuehrung.

**§§ 140, 141, 146 AO** — Aufzeichnungs- und Buchfuehrungspflichten; § 146 Abs. 1 AO Zeitgerechtigkeit der Buchungen.

**§ 90 AO** — Mitwirkungspflicht des Mandanten (Belegabgabe).

**§ 147 AO / § 257 HGB** — Aufbewahrungsfristen 6 bzw. 10 Jahre.

**§ 33 StBerG** — Aufgaben des Steuerberaters (Buchfuehrung als Hilfeleistung in Steuersachen).

**§ 35 StBVV** — Honorar fuer Buchfuehrung; Anhang 5 zur StBVV.

### Verwaltungsanweisungen

- BMF v. 28.11.2019 (BStBl I 2019, 1269) — GoBD; Anforderungen an zeitgerechte Buchungen (regelmaessig binnen 10 Tagen; spaetestens Monatsende).
- BMF v. 25.08.2020 (DSGVO im Steuerberater-Verhaeltnis).

## Workflow

### Phase 1 — Tag 1-5 des Folgemonats: Belegabgabe und Wareneingang

- Mandant uebermittelt Belege bis spaetestens 5. des Folgemonats (digital ueber DATEV Unternehmen Online).
- Belegannahme-Kontrolle: Vollstaendigkeit Eingangsrechnungen, Ausgangsrechnungen, Bankauszuege, Kassenauszuege, Lohnauswertungen.
- Pruefung Kassenfuehrung GoBD-konform (taegliche Aufzeichnungen, Z-Bons).
- OP-Listen vom Vormonat anfordern: noch nicht bezahlte Eingangsrechnungen, ueberfaellige Ausgangsrechnungen.

### Phase 2 — Tag 5-15: Buchung Tagesarbeit

- Bankbuchungen: GVC-Kontierung (DATEV) oder Banking-Kontierung.
- Eingangsrechnungen: gegen OPOS abgleichen, USt-Behandlung (Vorsteuer, Reverse-Charge, innergemeinschaftlicher Erwerb).
- Ausgangsrechnungen: aus Faktura-Modul oder manuelle Buchung; USt-Schluessel pruefen.
- Kassenbuchung: tageweise mit Z-Bon-Verprobung.
- Lohnbuchungen aus Lohnprogramm integrieren (Loehne, Sozialabgaben, Pauschalsteuer).

### Phase 3 — Tag 15-20: Abstimmung und Periodenabgrenzung

- Kontenabstimmung: Bank gegen Bankauszug, Kasse gegen Kassenbericht, Verrechnungskonten 1590/1599 (SKR 03) bzw. entsprechende SKR-04-Konten auf null.
- Rueckstellungen monatlich anteilig: Urlaub, Tantiemen, Berufsgenossenschaft, Pruefungskosten.
- Abschreibungen monatlich oder kumuliert (1/12-Methode aus Anlagenbuchhaltung).
- Aktive und passive Rechnungsabgrenzung (Versicherung, Miete, Kfz-Steuer) auf den Monat zerlegt.
- Bestandsveraenderung: bei Handel monatliche Schaetzung (Warenroll), bei Industrie Zwischeninventur quartalsweise.

### Phase 4 — Tag 20-25: Plausibilisierung

- Pruefung Umsatzentwicklung vs. Vormonat und Vorjahres-Monat.
- Vorsteuer-Pruefung: VAT-Konten sauber, Innergemeinschaftliche Lieferungen mit Bestaetigung der USt-Id.
- USt-Voranmeldung erstellen (§ 18 UStG) — bis zum 10. des Folgemonats (ggf. Dauerfristverlaengerung).
- BWA-Vorabauswertung pruefen: Ist das Ergebnis plausibel? Materialquote, Personalquote, Sondereffekte?

### Phase 5 — Tag 25-30: BWA-Erstellung und Versand

- BWA aus DATEV/Addison/Sage erstellen mit Vorjahresvergleich und kumuliertem Jahresblock.
- Erlaeuterungstext (1-2 Seiten) ergaenzen.
- Berufstraeger-Pruefung (4-Augen-Prinzip) — Stichproben, Plausibilitaet, Krisensignale.
- BWA an Mandant versenden (DATEV Unternehmen Online, E-Mail mit verschluesseltem Anhang).
- Monatsabschluss in Mandantenakte dokumentieren mit Zeitstempel und Bearbeiter.

### Phase 6 — Nachgang: Mandantenkommunikation

- Bei Auffaelligkeiten Mandant telefonisch oder im Meeting kontaktieren.
- Termin fuer Quartalsgespraech ankuendigen (alle 3 Monate).
- Bei wiederholten Belegabgabe-Verzoegerungen Mahnschreiben mit Honoraranknuepfung (Zuschlag fuer Eilfall).

## Output

- BWA mit Vorjahresvergleich und Erlaeuterungstext.
- USt-Voranmeldung uebermittelt.
- OPOS-Listen aktualisiert.
- Mandantenakte mit Monatsabschluss-Eintrag dokumentiert.

## Strategie und Praxis-Tipps

- 30-Tage-Zyklus mit klaren Deadlines (Tag 5 Belegannahme, Tag 15 Buchungsende, Tag 25 BWA fertig) durchhalten.
- Schwellenmandant: bei mehr als 200 Belegen monatlich automatische Belegeingangs-Erkennung (DATEV DUO) sinnvoll.
- Personalkosten brauchen vorgezogene Datenuebernahme — Lohnabteilung muss BWA-relevante Buchungen bis Tag 12 liefern.
- Honoraranknuepfung StBVV § 33: Buchfuehrungspauschale pro Monat, BWA-Erstellung separat als Vereinbarung.
- Bei Krisensignalen (negative BWA, Eigenkapitalerosion) automatische Eskalation an Berufstraeger (Querverweis stb-bwa-sus-bilanz-pruefung).

## Querverweise

- `stb-routine-monatsabschluss-30-tage-zyklus` — vertiefte Prozessbeschreibung.
- `stb-bwa-aufbau-grundlagen` — BWA-Struktur.
- `stb-pruefliste-belegabgabe-monatlich` — Belegabgabe-Checkliste.
- `stb-bwa-fehlerquellen-haeufig` — typische Fehler im Monatsabschluss.
- `stb-bwa-sus-bilanz-pruefung` — Krisensignal-Check.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 238, 239, 257.
- AO §§ 140, 141, 146, 147.
- StBerG § 33.
- StBVV § 33 (Buchfuehrung), Anhang 5.
- BMF v. 28.11.2019, BStBl I 2019, 1269 (GoBD).
- Verifikations-Hinweis: GoBD-Update bei BMF-Anpassungen jaehrlich pruefen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `stb-bwa-soll-ist-vergleich`

**Fokus:** Soll-Ist-Vergleich in der BWA. Anwendungsfall Monats- oder Quartals-BWA mit Plan-Werten aus Wirtschaftsplan Unternehmensplanung Forecast. Methodik Planeingabe Abweichungsanalyse Steuerungsempfehlung. Output BWA mit Spalte Plan Ist Abweichung Erlaeuterungstext für Mandant Querverweis stb-bwa-mandantenreport-monatlich.

# Soll-Ist-Vergleich in der BWA

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Soll-Ist-Vergleich in der BWA` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Der Soll-Ist-Vergleich legt unterjaehrige Planwerte des Mandanten neben die tatsaechlich gebuchten Werte und zeigt Abweichungen. Er ist Voraussetzung fuer professionelles Controlling und wird besonders bei groesseren Mandanten, Bankreporting und Sanierungsmandaten erwartet. Der Steuerberater leitet den Mandanten beim Aufstellen des Plans an und integriert die Werte in das DATEV/Addison-System.

## Kaltstart-Rueckfragen

1. Liegt ein Wirtschaftsplan / Budget des Mandanten vor, oder muss er erst erstellt werden?
2. Detailgrad des Plans — Jahres-Plan, Quartals-Plan, Monats-Plan?
3. Welche Position muss geplant werden — nur Umsatz und EBIT, oder gesamte GuV?
4. Welche Annahmen gelten — Preise, Mengen, Tarife, Personalentwicklung?
5. Liegen historische Daten fuer Plausibilitaet vor (mindestens 12 Monate)?
6. Reportingzweck — interne Steuerung, Bankgespraech, Investorenreport, Konzernreporting?
7. Wie oft wird der Plan ueberarbeitet (rollierend, Quartal, Jahr)?
8. Wer ist Plan-Verantwortlicher beim Mandanten (GF, kfm. Leitung, externer Berater)?

## Rechtlicher Rahmen

### Primaernormen

**§ 1 StaRUG** — Krisenfrueherkennung der Geschaeftsleitung; Planung ist Pflichtbestandteil.

**§ 91 Abs. 2 AktG / analog GmbH** — Ueberwachungs- und Risikomanagementsystem.

**§ 252 HGB** — Going-concern; positive Fortbestehensprognose setzt belastbaren Plan voraus.

**§ 19 Abs. 2 InsO** — Fortbestehensprognose; Prognosezeitraum (regulaer 12 Monate; durch SanInsKG zeitweise auf vier Monate verkuerzt). Aktuelle Geltungsdauer der SanInsKG-Verkuerzung in freier amtlicher Quelle pruefen.

### Standards

- IDW S 6 — Anforderungen an Sanierungskonzepte (integrierter Finanzplan).
- IDW S 11 — Beurteilung Insolvenzeroeffnungsgruende.
- IDW PS 305 — Pruefung Risikofrueherkennungssystem § 91 Abs. 2 AktG.

## Workflow

### Phase 1 — Planbasis bereitstellen

- Wenn kein Plan vorhanden: Mandant zur Erstellung anleiten oder eigenstaendig erstellen lassen (StBVV-Zusatzauftrag § 35).
- Datengrundlage: Historische Werte (12-36 Monate) als Ausgangsbasis.
- Annahmen schriftlich dokumentieren: Umsatzwachstum, Preisentwicklung, Personalplanung, Investitionsplanung.
- Plan auf Jahres-, Quartals- und Monatsebene herunterbrechen (Top-down oder Bottom-up).

### Phase 2 — Planeingabe in DATEV/Addison

- DATEV: Plan-Werte ueber DATEV Kanzlei-Rechnungswesen → Plan-Stammdaten erfassen.
- Addison: Budget-Modul aktivieren, Werte einlesen.
- Saisonalitaet abbilden: Jahresplan auf 12 Monate verteilen mit branchentypischen Schwankungsmustern.
- Plausibilitaetspruefung: Plan-Werte mit Vorjahres-Ist abgleichen.

### Phase 3 — Monatliche Soll-Ist-Auswertung

- BWA-Form mit Spalten konfigurieren: Plan, Ist, Abweichung absolut, Abweichung in Prozent.
- Kumulierter Year-to-Date-Vergleich Plan vs. Ist parallel.
- Periodengerecht abgrenzen — auch der Plan muss saisonbereinigt sein.

### Phase 4 — Abweichungsanalyse

| Abweichung | Bewertung | Handlungsbedarf |
|---|---|---|
| < 5 Prozent | Normaler Streubereich | Beobachten |
| 5-15 Prozent | Signifikante Abweichung | Ursache klaeren, Mandant ansprechen |
| > 15 Prozent | Wesentliche Abweichung | Bericht an GF, ggf. Planrevision |
| > 25 Prozent ueber mehrere Monate | Krisensignal | stb-bwa-sus-bilanz-pruefung pruefen |

### Phase 5 — Planrevision

- Bei groesseren Abweichungen ueber 2-3 Monate: Plan-Revision erforderlich.
- Mandant in Entscheidung einbinden — keine eigenmaechtige Planaenderung ohne Mandantenfreigabe.
- Dokumentation der Planaenderungen in Mandantenakte mit Datum und Begruendung.

### Phase 6 — Reporting an externe Stakeholder

- Bei Banken-Reporting: Plan-Ist-Bericht mit Erlaeuterung und Gegenmassnahmen.
- Bei Konzernreporting: Konzern-Reporting-Form (oft UKV-Format, internationale Lesart).
- Sanierungsmandate: Plan-Ist als Teil des IDW-S-6-Reports.

## Output

- BWA mit Plan-Ist-Vergleich (Monat und kumuliert).
- Abweichungsanalyse mit Erlaeuterungen.
- Planrevisions-Vorschlag bei wesentlichen Abweichungen.
- Bericht an externe Stakeholder (Bank, Investor, Konzern).

## Strategie und Praxis-Tipps

- Plan-Ist macht nur Sinn, wenn der Plan ernsthaft erarbeitet wurde — sonst wird der Vergleich Spielerei.
- Mindestens Quartalsweise Planrevision; rollierende Forecasts (Quartal + 4-Quartals-Horizont) sind heute Standard.
- Bei sanierungsbeduerftigen Mandanten: Plan ist Pflichtbestandteil der Fortbestehensprognose nach § 19 InsO und IDW S 6.
- Honorar fuer Plan-Erstellung gesondert vereinbaren — die Buchfuehrungspauschale deckt das nicht ab.
- Bei wesentlichen Abweichungen: Mandantengespraech terminieren, nicht nur per E-Mail kommunizieren.
- DATEV-Tipp: Plan-Stammdaten zentral pflegen, damit die BWA automatisch Plan-Spalten ausweist.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA-Grundlagen.
- `stb-bwa-zeitlicher-vergleich-jahresvergleich` — Vorjahresvergleich.
- `stb-bwa-mandantenreport-monatlich` — Mandantenreport.
- `stb-liquiditaetsvorschau-3-6-12-monate` — Liquiditaetsplanung.
- `stb-bwa-sus-bilanz-pruefung` — Krisenfrueherkennung.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 252, 265.
- StaRUG § 1.
- InsO § 19 (Prognosezeitraum 12 Monate; die SanInsKG-Sonderregelung mit verkuerztem 4-Monats-Zeitraum galt befristet vom 09.11.2022 bis 31.12.2023 und ist ausgelaufen; es gilt wieder der gesetzliche Standard-Prognosezeitraum von 12 Monaten).
- IDW S 6, IDW S 11, IDW PS 305.
- DATEV Kanzlei-Rechnungswesen Plan-Modul.
- Addison Budget-Modul.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 bestaetigt (SanInsKG-Sonderregelung ausgelaufen 31.12.2023, Standardzeitraum 12 Monate bestaetigt) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `stb-drv-sozialversicherungspruefung`

**Fokus:** Steuerberater-Begleitung der DRV-Sozialversicherungsprüfung nach § 28p SGB IV. Anwendungsfall Mandant-GmbH erhaelt DRV-Prüfankündigung oder Prüfung laeuft bereits. Prüfungsschwerpunkte Statusfeststellung GF Scheinselbstständigkeit Mini- und Midijobs Phantomlohn Mindestlohn BAGB. Strafbarkeit § 266a StGB vorenthaltene Arbeitnehmer-Beitraege Haftungsrisiko GF § 69 AO Lohnsteuer-Aussenprüfung Verknuepfung. Output Mitwirkungsdokumentation Anhoerungsschreiben Widerspruchsvorlage. Abgrenzung zu anw-gf-haftung-69-ao-nicht-abgeführte-steuern GF-Haftung Steuer.

# DRV-Sozialversicherungsprüfung — Steuerberater-Begleitung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DRV-Sozialversicherungsprüfung — Steuerberater-Begleitung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Steuerberater-Begleitung der **Sozialversicherungsprüfung** durch die Deutsche Rentenversicherung (DRV) — turnusmäßig alle vier Jahre nach § 28p SGB IV. Im Unterschied zur Lohnsteuer-Außenprüfung (Finanzamt) prüft die DRV die Sozialversicherungsbeiträge (Renten-, Kranken-, Pflege-, Arbeitslosen-, Unfallversicherung). Häufige Risiken: Statusfeststellung (Scheinselbständigkeit), Phantomlohn (Mindestlohn-Differenz), § 266a StGB-Strafbarkeit bei vorenthaltenem AN-Anteil.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Kaltstart-Rückfragen

1. Prüfung angekündigt (Datum, Prüfer, Vorlage-Anforderung)?
2. Prüfzeitraum (typisch 4 Jahre, ggf. erweitert)?
3. Lohnabrechnungssystem (DATEV LODAS, SAP, Sage)?
4. Anzahl Beschäftigte (AN, Mini/Midijob, freie Mitarbeiter)?
5. Geschäftsführer mit SV-Status klärungsbedürftig (GmbH-GF; ggf. Statusfeststellung erforderlich)?
6. Phantomlohn-Risiken (Mindestlohn-Differenzen, Schwarzarbeit-Indikatoren)?
7. Vorprüfung damals: Beanstandungen ja/nein? Welche Themen offen?

## Rechtlicher Rahmen

### Primärnormen

- **§ 28p SGB IV** — Turnusmäßige Prüfung mindestens alle 4 Jahre durch DRV.
- **§ 28a SGB IV** — Meldepflichten Arbeitgeber.
- **§ 28d SGB IV** — Beitragsschuldner (regelmäßig AG für AG- und AN-Anteil).
- **§ 28e SGB IV** — Beitragsforderung.
- **§ 7 SGB IV** — Beschäftigung; Abgrenzung Selbständigkeit/Beschäftigung.
- **§ 7a SGB IV** — Statusfeststellungsverfahren (Clearingstelle DRV).
- **§ 266a StGB** — Vorenthalten und Veruntreuen von Arbeitsentgelt; **Arbeitnehmeranteil** SV-Beiträge **strikt** unabhängig von Liquidität.
- **§ 14 Abs. 2 SGB IV** — Phantomlohn: tatsächlich gezahlt = Mindestlohn × Stunden, auch wenn vertraglich weniger; Differenzbeitragspflicht.
- **MiLoG** — Mindestlohngesetz; Anpassung Mindestlohn jährlich (12.82 EUR seit 1.1.2025; 13.90 EUR ab 1.1.2026).
- **§ 8 Abs. 1 Nr. 1 SGB IV** — Mini-Job-Grenze (538 EUR seit 1.10.2022; dynamisch an Mindestlohn).
- **§ 22 SGB IV** — Verjährung Beitragsforderung: vier Jahre (regelmäßig); 30 Jahre bei Vorsatz.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfungs-Schwerpunkte 2026

### Schwerpunkt 1 — Statusfeststellung

DRV prüft, ob als "freie Mitarbeiter" beschäftigte Personen tatsächlich abhängig beschäftigt sind. Kriterien (BSG-Linie):

- Eingliederung in betrieblichen Ablauf
- Weisungsabhängigkeit
- Unternehmerrisiko fehlend
- Keine eigene Betriebsstätte
- Exklusivität für einen Auftraggeber

Folge bei Umqualifizierung: Nachzahlung Beiträge **rückwirkend bis 4 Jahre** (bei Vorsatz 30 Jahre).

### Schwerpunkt 2 — GmbH-Geschäftsführer (SV-Status)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Gesellschafter-GF** mit Mehrheit oder Sperrminorität: regelmäßig **selbständig** → SV-frei.
- Bei Unklarheit: **Statusfeststellungsverfahren** § 7a SGB IV bei DRV-Clearingstelle (verbindliche Klärung).

### Schwerpunkt 3 — Mini-/Midijob und Mindestlohn-Differenz

- Mini-Job-Grenze 538 EUR (dynamisch); Überschreitung → reguläre SV-Pflicht ab Stunde 1.
- Mindestlohn-Differenz: tatsächliche Auszahlung muss ≥ Mindestlohn × Arbeitsstunden sein; sonst Phantomlohn-Nachzahlung.
- DRV-Praxis: Stichproben Lohnabrechnung + Stundenaufzeichnungen.

### Schwerpunkt 4 — Mindestlohn-Dokumentation

- **§ 17 MiLoG** Aufzeichnungspflicht: Arbeitsbeginn, -ende, -dauer **täglich** bei Geringverdienern (< Schwellenwert ca. 2 958 EUR).
- Bei fehlenden Aufzeichnungen: DRV schätzt zu Ungunsten AG.

### Schwerpunkt 5 — Schwarzgeld-Indikatoren

- Auffallende Cash-Abhebungen, fehlende Auszahlungsbelege, unplausible Lohnverhältnisse.
- DRV meldet bei Verdacht an Hauptzollamt (Schwarzarbeit) und FA (Steufa).

## Workflow

### Phase 1 — Ankündigung (Vor Prüfung)

- Prüfungsanordnung erhält AG i.d.R. 2-3 Wochen vorher.
- StB sammelt: Lohnjournale, Stundenaufzeichnungen, Arbeitsverträge freier Mitarbeiter, GmbH-Anstellungsverträge GF.
- **Voranalyse** durch StB: typische Risiken identifizieren.
- Bei kritischen Punkten: anwaltliche Beratung empfehlen (`anw-mandat-triage-steuerrecht`).

### Phase 2 — Während Prüfung

- DRV-Prüfer hat Zugang zu Lohnabrechnungssystem.
- StB begleitet als Berater; **kein Schweigerecht** wie im FA-Strafverfahren (DRV ist nicht-strafrechtlich).
- Fragen sachlich beantworten; bei strittigen Punkten **Mitwirkung dokumentieren** (was wurde wann übergeben).

### Phase 3 — Anhörung § 28r SGB IV

- DRV erlässt vor Bescheid eine Anhörung mit beabsichtigten Nachforderungen.
- Frist regelmäßig ein Monat zur Stellungnahme.
- StB prüft mit Mandant: Plausibilität, Verteidigungslinien.

### Phase 4 — Bescheid + Widerspruch

- DRV erlässt Beitragsbescheid mit Nachforderung.
- **Widerspruchsfrist ein Monat** § 84 SGG.
- Bei strittigen Sachverhalten **Klage zum Sozialgericht** möglich.

### Phase 5 — Parallelverfahren § 266a StGB

- Bei Vorenthaltungs-Verdacht ggf. parallele Strafanzeige durch DRV.
- **Anwaltlich beraten lassen** — StB darf nicht selbst Strafverteidigung leisten (§ 5 RDG).

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Freie Mitarbeiter ohne Statusfeststellung | Umqualifizierung; Nachforderung 4 Jahre | Statusfeststellung läuft | klare § 7a SGB IV-Bestätigung |
| GmbH-GF ohne klaren SV-Status | Nachforderung bei nachträglicher Umqualifizierung | Klärung beauftragt | Statusfeststellung vorhanden |
| Mindestlohn unterschritten | Phantomlohn + § 266a StGB | Differenz nachbezahlt | Mindestlohn-Compliance |
| § 17 MiLoG-Aufzeichnungen fehlen | Schätzung zu Ungunsten + Bußgeld | Stichproben | vollständige Aufzeichnungen |
| Schwarzgeld-Verdacht | DRV meldet an Zoll + FA; Strafverfahren | Aufklärung läuft | sauber dokumentiert |

## StB-Eigene Haftungsvermeidung

- StB ist **kein anwaltlicher Berater** zu § 266a StGB — bei Vorenthaltungs-Verdacht **anwaltliche Beratung empfehlen**.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Dokumentation** aller Hinweise an Mandantenleitung.

## Querverweise

- `stb-bwa-sus-bilanz-pruefung` — Pre-Check für SV-Themen
- `stb-warnschreiben-krisensignale` — Warnschreiben bei SV-Rückständen
- `anw-aussenpruefung-strategien` — Parallele LSt-AP (FA) kann ergänzen
- `anw-gf-haftung-69-ao-nicht-abgefuehrte-steuern` — bei GmbH-Insolvenz und LSt/SV-Rückständen
- `anw-steuerstrafverteidigung-verstaendigung` — bei § 266a StGB-Anklage
- `fachanwalt-arbeitsrecht` — bei arbeitsrechtlichen Statusfragen

## Quellen und Updates

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026 bundle_044
 → Leitsatz korrigiert zu echtem Inhalt (Scheinselbständigkeit Physiotherapeutin)
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
-->

## 6. `stb-jahresabschluss-abgrenzungen-rap-rai`

**Fokus:** Rechnungsabgrenzungsposten RAP aktiv und passiv. Anwendungsfall Jahresabschluss-Buchung Versicherung Miete Kfz-Steuer Vorauszahlungen periodengerechte Zuordnung. Methodik Identifikation Berechnung Buchung. Output Periodengerechte JA-Bestaende.

# Rechnungsabgrenzungsposten (RAP) aktiv und passiv

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rechnungsabgrenzungsposten (RAP) aktiv und passiv` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Rechnungsabgrenzungsposten (RAP) sind die bilanzielle Zuordnung von Aufwand und Ertrag zur richtigen Periode. Aktive RAP: Vorauszahlungen, die der Mandant gemacht hat und die in das Folgejahr gehoeren (z.B. Versicherungspraemie fuer 12 Monate, gezahlt im Dezember). Passive RAP: Einzahlungen, die im aktuellen Jahr empfangen wurden, aber Leistungen fuer das Folgejahr betreffen.

## Kaltstart-Rueckfragen

1. Welche Vorauszahlungen wurden geleistet (Versicherung, Miete, Leasing, Kfz-Steuer)?
2. Welche Einnahmen wurden empfangen, die Folgejahr betreffen (Mietvorauszahlungen, Service-Vertraege)?
3. Welcher Vertragszeitraum?
4. Welche Belege liegen vor?
5. Welche Standard-RAP wiederkehrend (Versicherung, Miete)?
6. Welche Sonderzahlungen?
7. Welcher Konten-Plan (RAP-Konten SKR 03)?
8. Welche steuerliche Behandlung (Massgeblichkeit § 5 EStG)?

## Rechtlicher Rahmen

### Primaernormen

**§ 250 HGB** — Rechnungsabgrenzungsposten.

**§ 252 Abs. 1 Nr. 5 HGB** — Periodenabgrenzung.

**§ 5 Abs. 5 EStG** — Steuerliche Massgeblichkeit RAP.

**§ 6 EStG** — Bewertung.

### Standards

- IDW PS 480.

## Workflow

### Phase 1 — Aktive RAP-Identifikation

| Beispiel | Vorauszahlung | RAP-Berechnung |
|---|---|---|
| Versicherungspraemie 12 Monate fuer Folgejahr | 1.200 EUR im Dezember | RAP aktiv 1.200 EUR |
| Miete Januar des Folgejahres in Dezember | 1.000 EUR | RAP aktiv 1.000 EUR |
| Leasing-Vorauszahlung | 5.000 EUR fuer 24 Monate | RAP aktiv 5.000 EUR (5.000 / 24 x 24 Monate) |
| Kfz-Steuer Folgejahr | 800 EUR | RAP aktiv 800 EUR |
| GEZ-Beitrag Folgejahr | 70 EUR | RAP aktiv 70 EUR |

### Phase 2 — Passive RAP-Identifikation

| Beispiel | Einzahlung | RAP-Berechnung |
|---|---|---|
| Mietvorauszahlung fuer Folgejahr | 5.000 EUR | RAP passiv 5.000 EUR |
| Service-Vertrag Vorauszahlung | 2.400 EUR fuer 24 Monate | RAP passiv 2.400 EUR x 12/24 = 1.200 EUR |
| Jahresvorauszahlung Wartungsvertrag | 600 EUR | RAP passiv 600 EUR |

### Phase 3 — Berechnung

- Anteil des Vorgangs, der in das Folgejahr gehoert.
- Bei 12-Monats-Vorauszahlung im Dezember: 11/12 RAP, 1/12 Aufwand/Ertrag.
- Bei kuerzeren Perioden anteilig genau.

### Phase 4 — Buchung

- Aktive RAP: Konto 980 SKR 03 (1900 SKR 04).
- Buchung: Aktive RAP an Aufwand (z.B. 4360 Versicherung).
- Passive RAP: Konto 990 SKR 03 (3900 SKR 04).
- Buchung: Ertrag (z.B. 8500) an Passive RAP.

### Phase 5 — Aufloesung im Folgejahr

- Eroeffnungsbilanz hat RAP-Bestaende.
- Im Folgejahr: Aufloesung anteilig.
- Buchung: Aufwand an Aktive RAP / Passive RAP an Ertrag.

### Phase 6 — Steuerliche Behandlung

- § 5 Abs. 5 EStG: aktive RAP sind in der Steuerbilanz zwingend.
- Steuerbilanz und Handelsbilanz oft identisch in RAP.

## Output

- RAP-Liste mit Berechnungsbasis.
- Buchungen im Hauptbuch.
- Bilanz mit RAP-Posten.

## Strategie und Praxis-Tipps

- Standard-RAP (Versicherung, Miete, Kfz-Steuer) sind wiederkehrend — Routine.
- Bei Mehrjahresvertraegen (z.B. 5-Jahres-Wartung): RAP gestaffelt.
- Bei kleinen RAP-Betraegen unter Wesentlichkeitsschwelle: ggf. nicht abgrenzen (vgl. BMF zu RAP-Bagatelle).
- Bei Pruefungspflicht: WP prueft RAP detailliert.
- DATEV-Tipp: DATEV-AfA-Modul kann RAP-Aufloesung monatlich automatisch.

## Querverweise

- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-jahresabschluss-rueckstellungen-bewertung` — Rueckstellungen.
- `stb-bwa-aufbau-grundlagen` — BWA mit Periodenabgrenzung.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 250, 252.
- EStG §§ 5, 6.
- IDW PS 480.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 7. `stb-jahresabschluss-elektronische-uebermittlung-ebilanz`

**Fokus:** E-Bilanz § 5b EStG elektronische Übermittlung. Anwendungsfall Bilanzierer Pflicht zur elektronischen Übermittlung der Steuerbilanz an FA Taxonomie-Standard. Methodik DATEV-E-Bilanz Modul. Output E-Bilanz uebermittelt.

# E-Bilanz — § 5b EStG elektronische Uebermittlung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `E-Bilanz — § 5b EStG elektronische Uebermittlung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

§ 5b EStG verpflichtet alle Bilanzierer zur elektronischen Uebermittlung der Steuerbilanz an das Finanzamt (E-Bilanz). Die Uebermittlung erfolgt im XBRL-Format auf Basis der jaehrlich vom BMF veroeffentlichten Kerntaxonomie (BMF-Taxonomie, abrufbar ueber esteuer.de) und wird ueber das ERiC-Modul der Finanzverwaltung uebertragen (in DATEV: integrierte ERiC-Schnittstelle, in Addison/Sage separates ERiC-Plugin). Frist: parallel zur Steuererklaerung (Festsetzungsverjaehrung beachten, ggf. § 109 AO Verlaengerung). Bei Mandanten mit Handelsbilanz und Steuerbilanz uebermittelt der StB regelmaessig die Handelsbilanz nebst Ueberleitungsrechnung; die "Echte-Steuerbilanz"-Uebermittlung ist Wahlrecht.

## Kaltstart-Rueckfragen

1. Liegt Bilanzierungspflicht vor (§§ 140-141 AO)?
2. Welches Wirtschaftsjahr?
3. Welche aktuelle Taxonomie-Version (jaehrlich angepasst)?
4. Welche Mandantenstammdaten (Steuer-Nr, FA)?
5. Welche Sondersituation (Sonderbilanz, Ergaenzungsbilanz Personengesellschaft)?
6. Welche Konten-Zuordnung zu Taxonomie?
7. Liegen alle Stammdaten vor?
8. Welche DATEV-Schnittstelle aktiv?

## Rechtlicher Rahmen

### Primaernormen

**§ 5b EStG** — Pflicht elektronische Uebermittlung.

**§ 5 EStG** — Massgeblichkeit.

**§§ 140-141 AO** — Bilanzierungspflicht.

**§ 25 EStG** — Veranlagung.

### Verwaltungsanweisungen

- BMF-Schreiben vom 28.09.2011, IV C 6 - S 2133-b/11/10009 zur erstmaligen E-Bilanz-Einfuehrung (Anwendungszeitpunkte und Mindestumfang).
- BMF-Schreiben zur jaehrlichen Aktualisierung der Taxonomie (zuletzt veroeffentlichte Fassung ueber esteuer.de bzw. BMF-Newsletter pruefen).
- Anwendungsfragen siehe AEAO zu § 5b EStG (Anwendungserlass zur Abgabenordnung in jeweils gueltiger Fassung).

## Workflow

### Phase 1 — Pflicht-Pruefung

- Bilanzierer nach § 5 EStG: E-Bilanz Pflicht.
- EUER-Steuerpflichtige (§ 4 Abs. 3 EStG): keine E-Bilanz, Anlage EUER.
- Personengesellschaften mit Bilanzierungspflicht.

### Phase 2 — Taxonomie

- BMF-Kerntaxonomie in der jeweils gueltigen Jahresfassung (Veroeffentlichung typisch im 2. Quartal, Anwendungspflicht ab Folgejahr). Bezugsquelle: www.esteuer.de.
- Pflichtfelder ("Mussfelder") sind zwingend zu fuellen; bei nicht verfuegbarem Datum dokumentierter "NIL"-Wert (Auffangregel siehe BMF-Taxonomie-Begleitdokumentation).
- Optionale Felder ("Kannfelder") nach Bedarf; "Mussfelder, soweit vorhanden" sind bei tatsaechlichem Vorliegen verpflichtend.

### Phase 3 — Konten-Zuordnung

- Standardkontenrahmen SKR 03 / SKR 04 (DATEV) bzw. IKR sind mit Standard-Mapping zur Kerntaxonomie ausgestattet; konkrete Mapping-Pflege siehe SKR-aktuelle Fassung.
- Individuelle Konten erfordern manuelle Zuordnung zur Taxonomie-Position; Pruefen vor Versand zwingend.
- In DATEV Kanzlei-Rechnungswesen erfolgt die E-Bilanz-Erstellung typischerweise ueber das Modul "E-Bilanz" mit eigenem Pruefprotokoll (genaue Programmpfade in der aktuellen DATEV-Programmversion ggf. abweichend).

### Phase 4 — Uebermittlung

- Auswertung im StB-Programm generiert eine XBRL-Datei (Endung .xbrl bzw. eingebettet in das XBRL-Paket).
- Versand an die Finanzverwaltung erfolgt ueber das ERiC-Modul (ELSTER Rich Client) mit Authentifizierungszertifikat (in der Regel das Berater-/Organisations-Zertifikat im ELSTER-Online-Portal).
- Vor Echt-Versand: Plausibilitaetspruefung im ERiC durchlaufen; Pruefprotokoll dokumentieren.
- Nach Versand: Uebermittlungsprotokoll (Transferticket-ID) speichern; Ablage in der Mandantenakte (Pflicht zur Aufbewahrung der Versandquittung).

### Phase 5 — Steuerbilanz-Anteil

- Bei Mandanten mit Handelsbilanz und separater Steuerbilanz: beide moeglich.
- Standardfall: Handelsbilanz mit Ueberleitungsrechnung.
- Steuerliche Wahlrechte hier ausgeuebt.

### Phase 6 — Wiedervorlage

- Folgejahr-E-Bilanz vorbereiten.
- Taxonomie-Updates jaehrlich.
- DATEV-Updates einspielen.

## Output

- E-Bilanz uebermittelt.
- ELSTER-Quittung.
- Steuererklaerung mit E-Bilanz-Bezug.

## Strategie und Praxis-Tipps

- E-Bilanz ist Standard fuer alle Bilanzierer.
- Bei groesseren Mandanten DATEV-E-Bilanz-Modul mit automatischer Taxonomie-Zuordnung.
- Pflicht-Felder strikt einhalten — Sendung wird sonst abgelehnt.
- Taxonomie-Updates zum 1. Januar jeden Jahres einspielen.

## Querverweise

- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-jahresabschluss-handels-vs-steuerbilanz` — Massgeblichkeit.
- `stb-bwa-kontenrahmen-skr03-skr04` — Kontenrahmen.

## Quellen und Updates

Stand: 05/2026.

- EStG §§ 5, 5b, 25.
- AO §§ 140, 141.
- BMF-Schreiben vom 28.09.2011 (IV C 6 - S 2133-b/11/10009) sowie Folgeschreiben.
- AEAO zu § 5b EStG.
- Verifikations-Hinweis: aktuelle Taxonomie-Version 2026 und Folgejahre ueber www.esteuer.de bzw. BMF-Newsletter pruefen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 8. `stb-jahresabschluss-handels-vs-steuerbilanz`

**Fokus:** Handelsbilanz vs Steuerbilanz Massgeblichkeit § 5 EStG. Anwendungsfall Prüfung Abweichungen Handels- und Steuerbilanz Massgeblichkeitsprinzip umgekehrte Massgeblichkeit Wahlrechte. Methodik Differenz-Tabelle Bewertungs-Unterschiede. Output Steuerbilanz oder Überleitungsrechnung.

# Handelsbilanz vs. Steuerbilanz — Massgeblichkeit § 5 EStG

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Handelsbilanz vs. Steuerbilanz — Massgeblichkeit § 5 EStG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Das Massgeblichkeitsprinzip (§ 5 EStG) verbindet Handels- und Steuerbilanz: die Handelsbilanz ist Ausgangsbasis fuer die Steuerbilanz. Aber es gibt zahlreiche Abweichungen — teils Pflicht (z.B. § 5 Abs. 4a EStG drohende Verluste), teils Wahlrecht (z.B. Sonder-AfA). Der Steuerberater erstellt entweder zwei separate Bilanzen oder eine Handelsbilanz mit Ueberleitungsrechnung zur Steuerbilanz.

## Kaltstart-Rueckfragen

1. Wird Steuerbilanz separat oder als Ueberleitung erstellt?
2. Welche Abweichungen sind erkennbar?
3. Welche Wahlrechte will Mandant nutzen?
4. Welche Sonder-AfA-Optionen pruefen?
5. Welche Rueckstellungen-Differenzen?
6. Welche IAB-Bilanzierung (§ 7g EStG)?
7. Welche Anpassungen E-Bilanz erforderlich?
8. Welche steuerliche Beratung gewuenscht?

## Rechtlicher Rahmen

### Primaernormen

**§ 5 Abs. 1 EStG** — Massgeblichkeit.

**§ 5 Abs. 1a EStG** — Wahlrechte.

**§ 5 Abs. 4a EStG** — Drohende-Verluste-Rueckstellungen ausgeschlossen.

**§ 5b EStG** — E-Bilanz.

**§ 6 EStG** — Bewertung Steuerbilanz.

**§ 7 EStG** — AfA-Methoden.

**§ 7g EStG** — IAB.

### Verwaltungsanweisungen

- BMF v. 12.03.2010 zu § 5 EStG.
- BMF zu E-Bilanz.

## Workflow

### Phase 1 — Massgeblichkeits-Pruefung

| Bewertung | Handelsbilanz (HGB) | Steuerbilanz (EStG) |
|---|---|---|
| Anschaffungskosten | § 253 HGB | § 6 EStG (gleich) |
| AfA-Methode | § 253 HGB | § 7 EStG (degressiv eingeschraenkt) |
| Rueckstellungen | § 249 HGB | § 5 Abs. 4a EStG (eingeschraenkt) |
| Drohende Verluste | Pflicht | Verboten |
| IAB | Keine handelsrechtliche Position | § 7g EStG Ruecklage Eigenkapital |
| Sonder-AfA § 7g, § 7b | Nicht zwingend | Wahlrecht |
| LIFO-Bewertung | Wahlrecht | § 6 Abs. 1 Nr. 2a EStG |

### Phase 2 — Wahlrechte nutzen

- Sonder-AfA § 7g Abs. 5 EStG (KMU): bis zu **40 %** der Anschaffungs- oder Herstellungskosten, frei verteilbar auf das Anschaffungsjahr und die folgenden vier Jahre (durch JStG 2020 von 20 % auf 40 % angehoben fuer Anschaffungen ab 01.01.2024; stabile Rechtslage).
- IAB § 7g Abs. 1-4 EStG: vorab bis zu **50 %** der voraussichtlichen Anschaffungs-/Herstellungskosten ausserbilanziell gewinnmindernd; Hoechstbetrag 200.000 EUR pro Wirtschaftsjahr; Gewinngrenze 200.000 EUR (stabile Rechtslage seit JStG 2020, § 7g Abs. 1 S. 2 Nr. 1 EStG).
- Bewertungsvereinfachungen (LIFO § 6 Abs. 1 Nr. 2a EStG; nur bei dauerhaft eingesetzten gleichartigen WG).
- Pensionsrueckstellungen § 6a EStG (fester Rechnungszinsfuss 6 %).

### Phase 3 — Pflicht-Abweichungen

- Drohende-Verluste-Rueckstellungen: HGB-Pflicht, EStG-Verbot.
- Pensionsrueckstellungen: § 6a EStG-Bewertung mit festem Zinsfuss 6 Prozent.
- Riester- und Direktzusagen.

### Phase 4 — Ueberleitungsrechnung

```
JAHRESERGEBNIS HANDELSBILANZ [X]
+ Drohende-Verluste-Rueckstellungen [+Y]
+ Steuerliche Sonder-AfA Mehrabschreibung [-Z]
+ Anpassung Pensionsrueckstellung [+/-]
+ IAB (Ruecklage) [-Y]
- Andere Wahlrechte [+/-]
= JAHRESERGEBNIS STEUERBILANZ [W]
```

### Phase 5 — E-Bilanz-Uebermittlung

- § 5b EStG: elektronische Uebermittlung an FA.
- Taxonomie-Standard: aktuelle Version 6.9 (BMF-Schreiben April 2025, verpflichtend fuer WJ ab 01.01.2026), abrufbar unter esteuer.de.
- Ueber DATEV-E-Bilanz-Modul.

### Phase 6 — Mandantenkommunikation

- Differenzen erlaeutern.
- Steueroptimierung diskutieren.
- Bei wesentlichen Wahlrechten Mandantenwahl dokumentieren.

## Output

- Handelsbilanz und Steuerbilanz (oder Ueberleitungsrechnung).
- E-Bilanz uebermittelt.
- Mandantengespraech ueber Wahlrechte.

## Strategie und Praxis-Tipps

- Bei kleinen Mandanten oft Einheitsbilanz (Steuerbilanz = Handelsbilanz mit Wahlrechten gleichgesetzt).
- Bei groesseren Mandanten zunehmend separate Steuerbilanz.
- IAB § 7g EStG ist gestaltungsstark — bei Investitionen pruefen.
- Bei Pensionsrueckstellungen erhebliche Differenzen — Mandant erklaeren.
- E-Bilanz-Taxonomie jaehrlich anpassen.

## Querverweise

- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-jahresabschluss-rueckstellungen-bewertung` — Rueckstellungen.
- `stb-jahresabschluss-anlagenverzeichnis-afa` — AfA.
- `stb-jahresabschluss-elektronische-uebermittlung-ebilanz` — E-Bilanz.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 249, 253.
- EStG §§ 5, 5b, 6, 6a, 7, 7b, 7g.
- BMF v. 12.03.2010 zu § 5 EStG.
- BMF zur E-Bilanz.
- Hinweis: E-Bilanz-Taxonomie jaehrlich anpassen; Version 6.9 fuer WJ 2026 massgeblich (esteuer.de).

<!-- AUDIT 27.05.2026 | welle 6 | 3 Marker aufgeloest: 3 bestaetigt (§ 7g 40% stabil, IAB 50% stabil, E-Bilanz Taxonomie 6.9 recherchiert) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 9. `stb-jahresabschluss-rueckstellungen-bewertung`

**Fokus:** Rückstellungen Bewertung § 249 HGB. Anwendungsfall Jahresabschluss Bildung Rückstellungen Garantie drohende Verluste Tantieme Urlaub Steuern Prozesskosten. Methodik Prüfung Anlass Quantifizierung Auflösung. Output Rückstellungs-Aufstellung.

# Rueckstellungen — Bildung und Bewertung § 249 HGB

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rueckstellungen — Bildung und Bewertung § 249 HGB` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Rueckstellungen sind Bilanzposten fuer ungewisse Verbindlichkeiten, drohende Verluste, Aufwendungen fuer abgrenzbare zukuenftige Leistungen. Sie sind Pflichtbestandteil des Jahresabschlusses (§ 249 HGB). Der Steuerberater identifiziert die relevanten Anlaesse, quantifiziert mit Vorsicht und bucht die Rueckstellungen. Steuerlich sind manche Rueckstellungen begrenzt (§ 5 Abs. 4a EStG).

## Kaltstart-Rueckfragen

1. Welche Verbindlichkeiten sind ungewiss zum Stichtag?
2. Liegen drohende Verluste aus schwebenden Geschaeften vor?
3. Welche Garantieverpflichtungen?
4. Welche Tantieme/Sondervergueteungen sind zugesagt?
5. Urlaubsanspruch der AN zum Stichtag (Urlaubsrueckstellung)?
6. Anhaengige Rechtsstreitigkeiten?
7. Steuer-Rueckstellungen (KSt, GewSt)?
8. Welche bisherigen Rueckstellungen sind aufzuloesen?

## Rechtlicher Rahmen

### Primaernormen

**§ 249 HGB** — Rueckstellungs-Pflichten.

**§ 253 HGB** — Bewertung; Hoehe und Diskontierung.

**§ 5 Abs. 4a EStG** — Steuerliche Einschraenkungen.

**§ 6 EStG** — Bewertung.

### Standards

- IDW PS 480.
- IDW RH HFA 1.009 (Rueckstellungen).
- BFH-Rechtsprechung zu Rueckstellungen.

## Workflow

### Phase 1 — Rueckstellungs-Anlaesse

| Anlass | Standard-Bewertung |
|---|---|
| Garantieverpflichtungen | Erfahrungswerte (in Prozent vom Umsatz) |
| Drohende Verluste schwebende Geschaefte | Hoehe des erwarteten Verlustes |
| Tantieme / Gratifikation | Vereinbarter Anteil |
| Urlaubsrueckstellung | (Brutto-Lohn + SV-AG) x Urlaubsanteil |
| Berufsgenossenschaft | Vorjahres-Beitrag + Anpassung |
| Pruefungskosten | Honorar fuer JA und USt-VA-Pruefung |
| Aufbewahrung GoBD | Pauschal 10-50 EUR pro AN |
| Anhaengige Prozesse | Anwaltliche Einschaetzung |
| Steuer-Rueckstellungen | KSt, GewSt nach Plan |
| Pensionsrueckstellungen | § 6a EStG-Bewertung |

### Phase 2 — Quantifizierung

- Bei Garantierueckstellungen: historisches Mittel der letzten 3 Jahre (in Prozent vom Umsatz).
- Bei Urlaubsrueckstellung: nicht genommene Urlaubstage x (Brutto + SV-AG) / 21 Arbeitstage.
- Bei Tantieme: vereinbarter Prozentsatz auf Jahresergebnis.

### Phase 3 — Steuerliche Einschraenkungen

- § 5 Abs. 4a EStG: Drohverlustrueckstellungen sind in der Steuerbilanz dem Grunde nach **nicht** zulaessig — handelsrechtliche Pflicht (§ 249 Abs. 1 S. 1 Alt. 2 HGB) und steuerliches Verbot fallen damit auseinander; in der Ueberleitungsrechnung zur Steuerbilanz zwingend zu korrigieren.
- Wahlrechte handelsrechtlicher Aufwandsrueckstellungen sind in der Steuerbilanz regelmaessig nicht abbildbar.
- Pensionsrueckstellungen sind nach § 6a EStG mit festem Rechnungszinsfuss von 6 % zu bewerten; daraus resultieren erhebliche Abweichungen zur HGB-Bewertung nach § 253 Abs. 2 HGB.

### Phase 4 — Diskontierung § 253 HGB

- Rueckstellungen mit Restlaufzeit > 1 Jahr sind nach § 253 Abs. 2 S. 1 HGB mit dem durchschnittlichen Marktzinssatz der vergangenen sieben Geschaeftsjahre abzuzinsen (Standardfall).
- **Altersversorgungsverpflichtungen und vergleichbare langfristige Verpflichtungen** sind nach § 253 Abs. 2 S. 2 HGB zwingend mit dem 10-Jahres-Durchschnittszinssatz abzuzinsen (kein 7-Jahres-Wahlrecht).
- Pauschalannahme einer Restlaufzeit von 15 Jahren bei Altersversorgungsverpflichtungen ist nach § 253 Abs. 2 S. 2 HGB zulaessig.
- Die Zinssaetze werden monatlich von der Deutschen Bundesbank veroeffentlicht; den zum Bilanzstichtag aktuellen Wert pflegen.

### Phase 5 — Aufloesung

- Bei Wegfall des Anlasses: erfolgswirksam aufloesen.
- Bei tatsaechlichem Eintritt: gegen Rueckstellung buchen.
- Bei abweichendem Aufwand: Erfolgs-Differenz.

### Phase 6 — Dokumentation

- Rueckstellungs-Liste mit Anlass, Berechnung, Hoehe.
- Mandantenakte mit Bewertungsgrundlagen.
- Bei Pruefungspflicht: WP-Pruefer-Vorbereitung.

## Output

- Rueckstellungs-Aufstellung.
- Buchungen im Hauptbuch.
- Bilanz-Position "Rueckstellungen".

## Strategie und Praxis-Tipps

- Rueckstellungen sind Vorsichtsprinzip-Werkzeug — bei Pruefungspflicht WP-erfasst.
- § 5 Abs. 4a EStG kann zur Differenz Handels-/Steuerbilanz fuehren — bei Massgeblichkeit beachten.
- Urlaubsrueckstellung ist Standardbestandteil — auch bei kleinen Mandanten zu bilden.
- Bei Pruefungspflicht WP-Erlaeuterung der Bewertungs-Grundlagen wichtig.

## Querverweise

- `stb-jahresabschluss-vorbereitung-stichtag` — JA-Vorbereitung.
- `stb-jahresabschluss-bestandskonten-abstimmung` — Bestandsabstimmung.
- `stb-jahresabschluss-handels-vs-steuerbilanz` — Massgeblichkeit.
- `stb-bwa-aufbau-grundlagen` — BWA.

## Quellen und Updates

Stand: 05/2026.

- HGB §§ 249, 253.
- EStG §§ 5 Abs. 4a, 6, 6a.
- IDW PS 480; IDW RH HFA 1.009.
- BFH-Rechtsprechung.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
