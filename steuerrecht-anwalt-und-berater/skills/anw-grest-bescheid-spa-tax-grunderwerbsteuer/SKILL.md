---
name: anw-grest-bescheid-spa-tax-grunderwerbsteuer
description: "ANW Grest Bescheid SPA TAX Grunderwerbsteuer: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ANW Grest Bescheid SPA TAX Grunderwerbsteuer

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **ANW Grest Bescheid SPA TAX Grunderwerbsteuer** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anw-grest-bescheid-einspruch-adv-16` | GrESt-Bescheid prüfen und angreifen: Einspruch, Aussetzung der Vollziehung, § 16 GrEStG Rueckgaengigmachung/Korrektur, doppelte Festsetzung, falsche Bemessungsgrundlage, falscher Steuersatz, Verfahrensfehler und FG-Strategie. |
| `anw-grest-spa-tax-clause-indemnity` | GrESt im SPA vertraglich absichern: Tax Covenant, GrESt-Indemnity, Käufer-/Verkäufertragung, Signing-Closing-Doppelrisiko, Escrow, Mitwirkungspflichten, Anzeigen, Grundbesitzliste und Post-Closing-Steuerklauseln. |
| `anw-grunderwerbsteuer-share-deal-90-prozent` | Grunderwerbsteuer GrEStG bei Share-Deal-Transaktionen mit grundbesitzhaltenden Gesellschaften berechnen und gestalten. Anwendungsfall M-und-A-Transaktion mit Immobilien-Hintergrund Anteilsuebertragung droht GrESt-Pflicht. 90-Prozent-Schwelle ab 01.07.2021 statt zuvor 95 Prozent. § 1 Abs. 2a GrEStG Personengesellschaft § 1 Abs. 2b GrEStG Kapitalgesellschaft § 1 Abs. 3 GrEStG unmittelbare Vereinigung § 1 Abs. 3a wirtschaftliche Beteiligung. 10-Jahres-Frist RETT-Blocker-Strukturen Anzeigepflicht § 19 GrEStG. Output GrESt-Prüfprotokoll Strukturierungs-Empfehlung Anzeige-Vorlage. |
| `anw-grundsteuer-einspruch-adv-bfh` | Grundsteuer-Einspruch und Aussetzung der Vollziehung: Frist, Bekanntgabe, BFH-AdV-Linie II B 78/23 und II B 79/23, BFH-Hauptsache 12.11.2025, Belegstrategie, Einspruchsbegründung und AdV-Antrag formulieren. |
| `anw-grundsteuer-ermittlungsbasis-flaeche-nutzung` | Grundsteuer-Ermittlungsbasis prüfen: Wohnfläche, Nutzfläche, Grundstücksfläche, wirtschaftliche Einheit, Baujahr, Nutzung, Garagen, Stellplätze, Erbbaurecht, Teileigentum, Leerstand, Denkmalschutz und Schätzungen aus der Grundsteuererklärung herausarbeiten. |
| `anw-grundsteuer-gutachten-gemeiner-wert` | Grundsteuer-Gegenbeweis mit gemeinem Wert vorbereiten: Kaufpreis, Verkehrswertgutachten, Maklerbewertung, Gutachterausschuss, Sonderfaktoren und BFH-AdV-Linie zu deutlich niedrigerem gemeinem Wert dokumentieren. |
| `anw-grundsteuer-hebesatz-zahlungsplan` | Kommunalen Grundsteuerbescheid prüfen: Hebesatz, Satzung, Fälligkeiten, Zahlungsplan, Stundung, Erlass, Vollstreckungsaufschub, Abgrenzung Finanzamt/Gemeinde und Kommunikation mit Hausverwaltung oder Kommune. |
| `anw-grundsteuer-landesmodell-routing` | Grundsteuer-Landesmodell-Routing: Bundesmodell von Baden-Wuerttemberg, Bayern, Hamburg, Hessen, Niedersachsen und punktuellen Abweichungen trennen; richtige Rechtsquelle, Bescheidart, BFH-/FG-Stand und Argumentationslinie bestimmen. |
| `anw-grundsteuer-verfassungscheck-bundesmodell` | Verfassungsrechtlicher Grundsteuer-Check nach der Reform: BVerfG 10.04.2018 zur alten Einheitsbewertung, BFH 27.05.2024 AdV, BFH 12.11.2025 zum Bundesmodell, Art. 3 GG, Typisierung, gemeiner Wert, Landesmodelle und offene Verfahren sauber einordnen. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **ANW Grest Bescheid SPA TAX Grunderwerbsteuer**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `anw-grest-bescheid-einspruch-adv-16`

**Fokus:** GrESt-Bescheid prüfen und angreifen: Einspruch, Aussetzung der Vollziehung, § 16 GrEStG Rueckgaengigmachung/Korrektur, doppelte Festsetzung, falsche Bemessungsgrundlage, falscher Steuersatz, Verfahrensfehler und FG-Strategie.

# GrESt: Bescheid, Einspruch, AdV und § 16

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `GrESt: Bescheid, Einspruch, AdV und § 16` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Prüfe GrESt-Bescheide nach Asset Deal, Share Deal oder Umstrukturierung. Erstelle Einspruchs- und AdV-Strategie, wenn Bemessung, Tatbestand oder Doppelbelastung streitig sind.

## Bescheidanalyse

1. Bescheidadressat und Steuerschuldner.
2. Tatbestand: § 1 Abs. 1, 2a, 2b, 3, 3a oder anderer.
3. Grundstücke und Bundesland.
4. Bemessungsgrundlage.
5. Steuersatz.
6. Vorbehalt der Nachprüfung, Nebenbestimmungen.
7. Bekanntgabe, Einspruchsfrist, Zahlungsfrist.

## Angriffspunkte

- falscher Tatbestand,
- doppelte Festsetzung Signing/Closing,
- falscher Steuerschuldner,
- falscher Grundbesitzwert oder falsche Gegenleistung,
- falscher Bundesland-Steuersatz,
- § 16 GrEStG nicht geprüft,
- § 6a GrEStG übergangen,
- Anzeige- oder Anhörungsfehler.

## § 16-GrEStG-Route

Prüfe Rückgängigmachung, Aufhebung, Nichtdurchführung, Herabsetzung und besondere Share-Deal-Korrekturen getrennt. Nie pauschal versprechen, § 16 lösche jede Doppelbelastung; Fristen, Anzeigepflichten und Bescheidstand sind entscheidend.

## Output

- Bescheidprüfvermerk.
- Einspruchsentwurf.
- AdV-Antrag.
- § 16-Antrag oder Hilfsantrag.
- Fristen- und Zahlungsplan.
- Belegliste für Finanzamt und FG.

## Quellen

GrEStG, AO, FGO und BFH-Volltexte öffnen. BFH-AdV-Beschlüsse als Eilverfahren kennzeichnen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `anw-grest-spa-tax-clause-indemnity`

**Fokus:** GrESt im SPA vertraglich absichern: Tax Covenant, GrESt-Indemnity, Käufer-/Verkäufertragung, Signing-Closing-Doppelrisiko, Escrow, Mitwirkungspflichten, Anzeigen, Grundbesitzliste und Post-Closing-Steuerklauseln.

# GrESt: SPA-Klauseln, Indemnity und Escrow

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `GrESt: SPA-Klauseln, Indemnity und Escrow` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Hilf beim Entwurf oder Review von GrESt-Klauseln in Unternehmenskaufverträgen. Der Skill ist für deutsche oder deutsch-englische M&A-Praxis gedacht.

## Klauselthemen

- Wer trägt GrESt aus der Transaktion?
- Wer trägt GrESt aus Altvorgängen?
- Wer trägt doppelte GrESt bei Signing/Closing-Streit?
- Wer kontrolliert Anzeige und Korrespondenz?
- Wer führt Einspruch/AdV/Klage?
- Darf ein Vergleich geschlossen werden?
- Wird ein Escrow für GrESt gebildet?
- Welche Garantien gelten zur Grundstücksliste?

## Review-Raster

| Klausel | Risiko |
|---|---|
| "Buyer bears all transfer taxes" | zu breit; Alt-GrESt und Verkäuferverstöße erfassen? |
| keine Anzeigepflicht | § 19-Risiko bleibt unverteilt |
| keine Grundbesitzliste | Bemessung und Zuständigkeit unklar |
| keine Streitkontrolle | Einspruchsfrist läuft beim falschen Team |
| keine Doppelbesteuerungsklausel | Signing/Closing-Liquiditätsrisiko offen |

## Output

- Klauselkommentar in Deal-Sprache.
- Tax Covenant-Vorschlag auf Deutsch oder Englisch.
- Indemnity-Matrix.
- Closing Deliverables.
- Escrow- und Cooperation-Baustein.

## Stil

Kurz, deal-tauglich, nicht lehrbuchhaft. Bei englischen Klauseln Begriffe erklären, aber deutsches GrESt-Recht als maßgeblich markieren.

## Praktischer Tipp

- "Transfer Taxes" in englischen SPAs ist ein loser Begriff; deutsche GrESt immer mit "real estate transfer tax (Grunderwerbsteuer)" definieren und das anwendbare deutsche Recht ausdrücklich vorsehen, auch wenn der SPA englischem Recht unterliegt.
- Streitkontrolle (control of tax proceedings) muss den Käufer mindestens als Joinder vorsehen, weil das Finanzamt sich an den Käufer als Steuerschuldner halten kann (§ 13 GrEStG, gesamtschuldnerische Haftung). Wenn der Verkäufer den Einspruch allein führt, kommt der Käufer ohne Mitwirkungsrecht in die Haftung.
- Escrow-Höhe bei Signing/Closing-Doppelfestsetzungsrisiko: typisch 150 bis 200 % der berechneten GrESt der jeweils zweifelhaften Festsetzung, weil Zinsen nach § 233a AO (6 % bis 2018, danach 1,8 % p.a. nach Neuregelung) hinzukommen können.

## Trade-off: Indemnity vs. Garantie

| Pfad | Vorteil | Nachteil |
|---|---|---|
| Tax Indemnity (verschuldensunabhängig) | klare Allokation, einfache Durchsetzung | breite Haftungsschulter Verkäufer |
| Tax Warranty (Garantie) | passt in W&I-Versicherung | Kausalität und Schadenhöhe streitig |
| Specific Indemnity nur für identifiziertes Risiko | gezielt, deal-freundlich | nur für DD-bekannte Themen |

Empfehlung: Allgemeine Tax Indemnity für unbekannte Altrisiken + Specific Indemnity für DD-Findings + Escrow für streitige laufende Festsetzungen.

## Beispiel-Mustertext (Indemnity-Kern)

> Der Verkäufer stellt den Käufer von sämtlicher Grunderwerbsteuer einschließlich Säumniszuschlägen, Zinsen und Nebenleistungen frei, die auf Erwerbsvorgänge vor dem Closing zurückgeht oder bei der die Tatbestandsverwirklichung vor dem Closing eingetreten ist. Die Freistellung umfasst auch Doppelfestsetzungen aufgrund auseinanderfallender Signing-/Closing-Stichtage. Der Käufer informiert den Verkäufer unverzüglich, spätestens binnen [10] Werktagen, über Anzeigen, Auskunftsersuchen, Bescheide oder Klagen; der Verkäufer ist berechtigt, die Verteidigung auf eigene Kosten zu übernehmen, der Käufer wirkt loyal mit.

## Typische Fehler

- "Käufer trägt alle Steuern aus der Transaktion" deckt Alt-GrESt nicht (keine "Transaktionssteuer"). Klare Cut-off-Klausel mit Datum nötig.
- Grundbesitzliste fehlt oder ist nicht aktuell zum Closing-Datum; spätere Streitigkeiten über Bemessungsgrundlage und Belegenheitsfinanzamt.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `anw-grunderwerbsteuer-share-deal-90-prozent`

**Fokus:** Grunderwerbsteuer GrEStG bei Share-Deal-Transaktionen mit grundbesitzhaltenden Gesellschaften berechnen und gestalten. Anwendungsfall M-und-A-Transaktion mit Immobilien-Hintergrund Anteilsuebertragung droht GrESt-Pflicht. 90-Prozent-Schwelle ab 01.07.2021 statt zuvor 95 Prozent. § 1 Abs. 2a GrEStG Personengesellschaft § 1 Abs. 2b GrEStG Kapitalgesellschaft § 1 Abs. 3 GrEStG unmittelbare Vereinigung § 1 Abs. 3a wirtschaftliche Beteiligung. 10-Jahres-Frist RETT-Blocker-Strukturen Anzeigepflicht § 19 GrEStG. Output GrESt-Prüfprotokoll Strukturierungs-Empfehlung Anzeige-Vorlage.

# Grunderwerbsteuer bei Share Deals — 90-%-Schwelle, Anzeigepflicht, Gestaltung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Grunderwerbsteuer bei Share Deals — 90-%-Schwelle, Anzeigepflicht, Gestaltung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Anwaltliche Beratung bei Erwerb von Anteilen an Gesellschaften mit inländischem Grundbesitz. Seit der GrEStG-Reform vom 1.7.2021 ist die Schwelle für die GrESt-Pflicht beim Share Deal von 95 % auf **90 %** abgesenkt; die Behaltefrist wurde auf **10 Jahre** verlängert. Praxisrelevant in nahezu jedem M&A-Mandat mit Immobilien-Hintergrund.

## Kaltstart-Rückfragen

1. Welcher Anteilserwerb wird geplant (unmittelbar / mittelbar; Quote)?
2. Rechtsform Zielgesellschaft (KapGes oder PersGes)?
3. Welche Grundstücke besitzt die Zielgesellschaft (inländisch, Verkehrswert)?
4. Bestand bisher Konzern-Beteiligung > 0 % (Vorbeteiligungs-Anrechnung)?
5. Zeitachse Erwerbsphasen (mehrere Tranchen?)?
6. Erwerber bereits beteiligt? RETT-Blocker-Struktur vorhanden?
7. Welcher Stichtag (Signing / Closing — GrESt-Tatbestand?)?

## Rechtlicher Rahmen

### Primärnormen

- **§ 1 Abs. 1 GrEStG** — Grundstückskauf direkt (Asset Deal) — Tatbestand 1.
- **§ 1 Abs. 2a GrEStG** — Wechsel im Gesellschafterbestand einer **grundbesitzhaltenden Personengesellschaft** zu mindestens **90 %** innerhalb von **10 Jahren**.
- **§ 1 Abs. 2b GrEStG** — Wechsel im Gesellschafterbestand einer **grundbesitzhaltenden Kapitalgesellschaft** zu mindestens **90 %** innerhalb von **10 Jahren** (eingeführt durch StAGeRefG 1.7.2021).
- **§ 1 Abs. 3 GrEStG** — Unmittelbare **Anteilsvereinigung** zu mindestens **90 %** durch eine Person.
- **§ 1 Abs. 3a GrEStG** — Wirtschaftliche Beteiligung **mindestens 90 %** durch mehrstufige Beteiligungsketten.
- **§ 5 / § 6 GrEStG** — Befreiungen bei Anteilsübertragungen zwischen Gesamthand/PersGes-Gesellschaftern (eingeschränkt).
- **§ 6a GrEStG** — **Konzernklausel** (Steuervergünstigung bei Umstrukturierungen im Konzern): Befreiung für Erwerbsvorgänge nach § 1 Abs. 1 Nr. 3, Abs. 2, 2a, 2b, 3 oder 3a GrEStG aufgrund einer Umwandlung (§ 1 Abs. 1 Nr. 1-3 UmwG) oder Einbringung im Konzern. Voraussetzungen: **herrschendes Unternehmen** hält am abhängigen Unternehmen mindestens **95 %** ununterbrochen während der **Vor- und Nachbehaltensfrist von je 5 Jahren**. § 7 GrEStG regelt dagegen die Steuermessung beim Übergang von Gesamthandsvermögen in Bruchteilseigentum, nicht Konzernsachverhalte.
- **§ 8 GrEStG** — Bemessungsgrundlage: **Grundbesitzwert** § 138 BewG (nicht Kaufpreis Anteile; Sonderbewertung).
- **§ 11 GrEStG** — Steuersatz: Ländersteuer, **zwischen 3.5 % und 6.5 %** je Bundesland.
- **§ 19 GrEStG** — Anzeigepflicht: **2 Wochen** ab Tatbestandsverwirklichung; Verstoß bewehrt mit Säumniszuschlägen und ggf. Strafverfahren.

### Leitentscheidungen und Folgeskills

- **BFH, Beschluss vom 09.07.2025 — II B 13/25 (AdV)**: Ernstliche Zweifel an der Rechtmaessigkeit einer doppelten GrESt-Festsetzung nach § 1 Abs. 2b und § 1 Abs. 3 GrEStG bei zeitlich getrenntem Signing und Closing eines GmbH-Anteilserwerbs. Volltext ueber BFH-Datenbank (STRE202520204).
- **BFH, Beschluss vom 16.09.2025 — II B 23/25 (AdV)**: Keine automatische AdV gegen die Closing-Festsetzung selbst, wenn die rechtlichen Zweifel nur die zusätzliche Signing-Festsetzung betreffen. Zielbescheid sauber trennen.
- **BFH, Beschluss vom 27.10.2025 — II B 47/25 (AdV)** (sog. dritter Signing-Closing-Beschluss): Bestaetigt die Linie aus II B 13/25; doppelte GrESt-Festsetzung auf einheitlichen Lebenssachverhalt verstoesst gegen den Verhaeltnismaessigkeitsgrundsatz; gilt auch ohne Nachpruefungsvorbehalt nach § 164 AO. Volltext ueber BFH-Datenbank (STRE202520313).
- **BFH, Urteil vom 21.05.2025 — II R 31/22**: Volltext ueber BFH-Datenbank (Pruefung im Einzelfall).
- **BFH, Urteil vom 25.09.2024 — II R 2/22** und **II R 46/22** (Konzernklausel § 6a GrEStG): Volltext ueber BFH-Datenbank.
- Gleich lautende Erlasse der obersten Finanzbehörden der Länder vom 20.02.2026 zur Anwendung der Share-Deal-Regeln nach §§ 1 Abs. 2a und 2b GrEStG; sie ersetzen die Erlasse vom 10.05.2022 und sind als Verwaltungsauffassung zu kennzeichnen, nicht als Ersatz für BFH-Rechtsprechung.
- Weitere Rechtsprechung: vor Zitierung ueber dejure.org / BFH-Datenbank verifizieren.

Bei Detailfragen danach gezielt laden:

- `anw-grest-kaltstart-asset-share-deal`
- `anw-grest-share-deal-90-prozent-10-jahre`
- `anw-grest-signing-closing-doppelfestsetzung`
- `anw-grest-anzeige-19-closing-check`
- `anw-grest-spa-tax-clause-indemnity`
- `anw-grest-bescheid-einspruch-adv-16`

## Tatbestände im Überblick

### Tatbestand A — Asset Deal (§ 1 Abs. 1 GrEStG)

Klassischer Grundstückskauf — voller Steuersatz (3.5 %–6.5 %) auf Kaufpreis. **Kein Share Deal**, daher hier nur Bezugsmarke.

### Tatbestand B — Wechsel Gesellschafterbestand PersGes (§ 1 Abs. 2a GrEStG)

- Anwendung: Personengesellschaft mit inländischem Grundbesitz
- Schwelle: 90 % Anteils- oder Stimmrechtswechsel innerhalb 10 Jahren
- Steuerschuldner: Personengesellschaft selbst
- Bemessung: Grundbesitzwert § 138 BewG

### Tatbestand C — Wechsel Gesellschafterbestand KapGes (§ 1 Abs. 2b GrEStG, **Reform 2021**)

- Anwendung: Kapitalgesellschaft (GmbH, AG, KGaA) mit inländischem Grundbesitz
- Schwelle: 90 % Anteilswechsel innerhalb 10 Jahren
- Steuerschuldner: Kapitalgesellschaft selbst
- **Achtung**: Tatbestand neu seit 1.7.2021 — vor diesem Datum nur § 1 Abs. 3 GrEStG erfasst

### Tatbestand D — Anteilsvereinigung 90 % bei einer Person (§ 1 Abs. 3 GrEStG)

- Anwendung: Eine Erwerberin vereinigt ≥ 90 % der Anteile auf sich (KapGes oder PersGes)
- Steuerschuldner: Erwerberin
- Vereinigung kann unmittelbar oder mittelbar erfolgen

### Tatbestand E — Wirtschaftliche Beteiligung 90 % (§ 1 Abs. 3a GrEStG)

- Anwendung: mehrstufige Beteiligungsketten — wirtschaftlich entsprechen ≥ 90 %
- RETT-Blocker (Real Estate Transfer Tax-Blocker) zielen darauf, mehrere unter 90 %-Beteiligungen aufzuteilen, um GrESt zu vermeiden
- Reform-Risiko: Gesetzgeber will weitere Verschärfung

## Berechnungsbeispiel

```
Zielgesellschaft GmbH (KapGes) mit drei inländischen Grundstücken
Grundbesitzwert § 138 BewG: EUR 12 000 000

Anteilserwerb 95 % in einer Tranche
-> Tatbestand C § 1 Abs. 2b GrEStG (KapGes-Wechsel ≥ 90 %)
-> Steuersatz Bundesland (z. B. Berlin 6 %)
-> GrESt: 6 % × 12 000 000 = EUR 720 000

Hinweis: GrESt fällt auf Grundbesitzwert (nicht Kaufpreis der Anteile)
und wird zusätzlich zum Kaufpreis fällig.
```

## Gestaltungs-Optionen

### Option 1 — Unter 90 %-Schwelle bleiben

- Erwerb von z. B. 89.9 % der Anteile durch Erwerberin
- Restanteil bleibt bei Verkäufer oder bei externem Investor
- **Risiko**: bei späterer Aufstockung greift § 1 Abs. 3 GrEStG; **Vorbeteiligungs-Anrechnung** über 10 Jahre

### Option 2 — RETT-Blocker

- Erwerb durch verbundene Gesellschaften: Erwerber A 89 % + Erwerber B (verbundener Investor) 11 %
- **Risiko**: § 1 Abs. 3a GrEStG (wirtschaftliche Beteiligung) kann durchgreifen, wenn beide Erwerber wirtschaftlich identisch sind
- Praxis: Strukturen unterschiedlich wirksam je nach Bundesland und Auslegung

### Option 3 — Asset Deal statt Share Deal

- Grundstücke einzeln aus der Zielgesellschaft erwerben
- GrESt auf Kaufpreis (regelmäßig höher als Grundbesitzwert)
- Aber: Möglicherweise andere Steuerfolgen günstiger (KSt, GewSt)

### Option 4 — Befreiungstatbestände nutzen

- § 5/§ 6 GrEStG bei Anteilsübertragung in PersGes (Gesamthand)
- § 6a GrEStG bei konzerninternen Umstrukturierungen (Umwandlung/Einbringung; 95 %-Beteiligung + 5 Jahre Vor- und Nachbehaltensfrist)
- Vorsicht: Behaltefristen!

## Anzeigepflicht § 19 GrEStG

- **Frist 2 Wochen** ab Tatbestandsverwirklichung (= regelmäßig Closing)
- Form: schriftliche Anzeige beim **Finanzamt am Belegenheitsort** des Grundbesitzes
- Inhalt: Beteiligte, Anteilsquoten, Zeitpunkt, Beschreibung Grundstücke
- Bei Verstoß: Säumniszuschläge nach § 240 AO + ggf. Steuerstrafverfahren (Steuerhinterziehung § 370 AO durch Unterlassen)

## Workflow

### Phase 1 — Strukturplanung Pre-Signing

- Grundstücksinventar Zielgesellschaft
- Beteiligungsanalyse Erwerber-Konzern (bestehende Vorbeteiligungen)
- Bemessungsgrundlagen-Berechnung (Grundbesitzwert)
- Steuermodellrechnung Asset vs. Share Deal
- Gestaltungsoption (unter Schwelle / RETT / Asset)

### Phase 2 — Vertragsgestaltung

- Tax Indemnity Clause (Verkäufer trägt GrESt bei Verstoß)
- Tax Reps and Warranties zu Grundbesitz
- Closing-Mechanik (Anzeige-Verpflichtung)

### Phase 3 — Closing + Anzeige

- Anzeige § 19 GrEStG **binnen 2 Wochen** beim FA
- Verbindliche Auskunft § 89 Abs. 2 AO **vorab** empfehlenswert
- Dokumentation Beteiligungsänderung mit Gesellschaftervertrag, Notar, HR

### Phase 4 — Post-Closing

- GrESt-Bescheid prüfen (Bemessungsgrundlage)
- Bei Streit: Einspruch (`anw-einspruch-finanzamt`)
- 10-Jahres-Tracking (für spätere Anteilsänderungen)

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Vorbeteiligung 10 % + Erwerb 80 % | § 1 Abs. 3 + Anrechnung; GrESt fällig | Genaue Prüfung 10-Jahres-Frist | unter Schwelle |
| Anzeige § 19 versäumt | Säumniszuschlag + Strafverfahren | Frist knapp eingehalten | sofort angezeigt |
| Bemessung über Kaufpreis statt Grundbesitzwert | falscher Bescheid → Einspruch | Bewertungsgutachten beibringen | korrekter Wert §138 BewG |
| RETT-Blocker schwach gestaltet | wirtschaftliche Identität → § 1 Abs. 3a | Strukturüberprüfung | wirtschaftlich unabhängige Erwerber |
| Bundesland-Steuersatz übersehen | Falsche Steuerprognose | Korrektur möglich | richtiger Hebesatz |
| Signing/Closing-Trennung + Doppel-Festsetzung § 1 Abs. 2b + Abs. 3 | Doppelbesteuerung — AdV unter Berufung auf BFH II B 13/25, II B 47/25 sofort beantragen | Pruefung Verhaeltnismaessigkeit; Verzicht auf eine Festsetzung verhandeln | Einheitliche Festsetzung |

## Querverweise

- `anw-verbindliche-auskunft` — Pre-Signing-Klärung
- `anw-mandat-triage-steuerrecht` — bei Mandatsanfang
- `anw-organschaft-konzern-grundlagen` — bei Konzern-Restrukturierung
- `fachanwalt-handels-gesellschaftsrecht-ma-due-diligence-findings` — DD im M&A
- `fachanwalt-handels-gesellschaftsrecht-holding-strukturplanung` — Holding-Setup
- `immobilienrechtspraxis` — bei vorgelagertem Grundstücksgeschäft

## Quellen und Updates

Stand: 05/2026. StAGeRefG (Reform 1.7.2021): 95→90 %, 5→10 Jahre. Gleich lautende Ländererlasse vom 20.02.2026 als Verwaltungsauffassung einordnen und den BStBl-/Landesvolltext vor Ausgabe öffnen. Bundesland-Steuersätze 3.5 %–6.5 % vor Ausgabe aktuell prüfen. Bei Verschärfung RETT-Blocker oder weiterer Schwellenabsenkung aktualisieren.

## 4. `anw-grundsteuer-einspruch-adv-bfh`

**Fokus:** Grundsteuer-Einspruch und Aussetzung der Vollziehung: Frist, Bekanntgabe, BFH-AdV-Linie II B 78/23 und II B 79/23, BFH-Hauptsache 12.11.2025, Belegstrategie, Einspruchsbegründung und AdV-Antrag formulieren.

# Grundsteuer: Einspruch, AdV und BFH-Linie

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Grundsteuer: Einspruch, AdV und BFH-Linie` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Erstelle einen belastbaren Verfahrensplan für Einspruch, Aussetzung der Vollziehung und Klage in Grundsteuerfällen. Der Skill nutzt die BFH-Linie, aber verkauft AdV-Beschlüsse nicht als sichere Hauptsache.

## Sofortcheck

1. Bekanntgabe und Einspruchsfrist.
2. Richtiger Bescheid: Grundsteuerwert, Messbetrag oder Grundsteuerbescheid.
3. Vollziehbarkeit: Zahlungstermin, Höhe, Liquiditätsbelastung.
4. Belege für erheblich niedrigeren gemeinen Wert oder falsche Datenbasis.
5. Stand: Einspruch eingelegt, AdV beim Finanzamt beantragt, Ablehnung, FG-Antrag.

## BFH-Anker

- **BFH, Beschlüsse vom 27.05.2024 - II B 78/23 (AdV), II B 79/23 (AdV)**: Bei summarischer Prüfung kann AdV in Betracht kommen, wenn ein deutlich niedrigerer gemeiner Wert plausibel gemacht wird.
- **BFH, Urteile vom 12.11.2025 - II R 25/24, II R 31/24, II R 3/25**: Bundesmodell in den entschiedenen Verfahren verfassungsgemäß; Einzelfallnachweis bleibt gesondert zu prüfen.
- **BFH-Fokusseite Grundsteuer, Stand Mai 2026**: vor jeder Ausgabe prüfen, ob zu Landesmodellen oder neuen Verfahren weiterer Stand veröffentlicht ist.

## AdV-Argumentation

Stark ist:

- konkrete Abweichung zwischen Grundsteuerwert und plausibel belegtem gemeinen Wert,
- objektbezogene Sonderlage: Hinterliegergrundstück, Hanglage, Erschließung, Altlast, Denkmalschutz, massive Baumängel,
- falsche Datenbasis im Bescheid.

Schwach ist:

- nur "neue Grundsteuer ist zu teuer",
- nur pauschale Verfassungsrüge,
- Angriff gegen Gemeindehebesatz im falschen Verfahren.

## Output-Module

### 1. Einspruch

Formuliere knapp:

- Bescheid, Datum, Aktenzeichen,
- Antrag auf Aufhebung/Änderung,
- konkrete Fehler,
- Belege,
- Antrag auf Ruhen nur, wenn ein passendes Muster- oder BFH-Verfahren wirklich einschlägig ist.

### 2. AdV beim Finanzamt

Zusätzlich:

- ernstliche Zweifel,
- Abweichung vom gemeinen Wert,
- Zahlungsbelastung,
- Antrag auf Aussetzung in konkret bezifferter Höhe.

### 3. FG-AdV

Nur wenn FA ablehnt oder nicht rechtzeitig entscheidet. Dann Ablehnung, Einspruch, Bescheide und Belege als Anlagenliste aufbereiten.

## Abschluss

Gib immer eine "nächste 7 Tage"-Liste: Frist, Beleg, Antrag, Zahlung, Rückfrage an Gemeinde/Finanzamt.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `anw-grundsteuer-ermittlungsbasis-flaeche-nutzung`

**Fokus:** Grundsteuer-Ermittlungsbasis prüfen: Wohnfläche, Nutzfläche, Grundstücksfläche, wirtschaftliche Einheit, Baujahr, Nutzung, Garagen, Stellplätze, Erbbaurecht, Teileigentum, Leerstand, Denkmalschutz und Schätzungen aus der Grundsteuererklärung herausarbeiten.

# Grundsteuer: Ermittlungsbasis Fläche, Nutzung und wirtschaftliche Einheit

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Grundsteuer: Ermittlungsbasis Fläche, Nutzung und wirtschaftliche Einheit` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Dieser Skill zerlegt die tatsächliche Grundlage der Grundsteuerbewertung. Er eignet sich für Hausverwaltungen, Eigentümer und Berater, wenn Bescheide aus ELSTER-Erklärungen, Altunterlagen oder Schätzungen nicht nachvollziehbar sind.

## Dokumente anfordern

- Grundsteuererklärung und Übermittlungsprotokoll.
- Grundbuchauszug, Teilungserklärung, Aufteilungsplan.
- Wohnflächenberechnung, Mietflächenaufstellung, Bauakte.
- Flurkarte, Katasterauszug, Bodenrichtwertauskunft.
- Mietvertrag / Nutzungsliste / Leerstandsnachweise.
- Denkmalschutzbescheid, Baulasten, Erbbaurechtsvertrag.
- Fotos, Skizzen, Scan der Bescheide.

## Prüfraster

| Feld | Typischer Fehler | Beleg |
|---|---|---|
| Grundstücksfläche | Flurstücke zusammengezogen oder getrennt | Kataster, Grundbuch |
| Wohnfläche | Keller, Dachboden, Balkon, Gewerbe falsch | Wohnflächenberechnung |
| Nutzfläche | Laden, Lager, Werkstatt falsch eingeordnet | Mietvertrag, Bauplan |
| Baujahr | Kernsanierung als Neubau missverstanden | Bauakte, Sanierungsnachweis |
| Grundstücksart | Wohn-/Geschäftshaus, Teileigentum, gemischte Nutzung | Teilungserklärung |
| Bodenrichtwert | Zone oder Stichtag falsch | Gutachterausschuss |
| wirtschaftliche Einheit | mehrere Objekte zusammen oder getrennt | Grundbuch, Nutzung |
| Denkmalschutz / Ermäßigung | nicht berücksichtigt | Bescheid Denkmalschutz |

## Arbeitsweise

1. Bescheiddaten in eine Tabelle übernehmen.
2. Mandantenangaben danebenstellen.
3. Jede Abweichung als "belegt", "plausibel offen" oder "unbelegt" markieren.
4. Fehler nach Bescheidzuständigkeit sortieren: Finanzamt oder Gemeinde.
5. Bei Schätzungsbescheid sofort prüfen, ob eine vollständige Erklärung nachgereicht werden muss.

## Output

Erstelle:

- Datenabgleichstabelle.
- Belegliste mit Verantwortlichkeit.
- Änderungsantrag oder Einspruchsbaustein.
- Fristenhinweis.
- Folgeempfehlung: `anw-grundsteuerwert-bewertung-bewg-218ff` oder `anw-grundsteuer-einspruch-adv-bfh`.

## Grenzen

Keine "gefühlten" Flächenwerte als feststehend ausgeben. Bei streitiger Wohnfläche immer Belege oder Messung verlangen. Rechtsprechung nur aus geöffneten freien Quellen zitieren.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 6. `anw-grundsteuer-gutachten-gemeiner-wert`

**Fokus:** Grundsteuer-Gegenbeweis mit gemeinem Wert vorbereiten: Kaufpreis, Verkehrswertgutachten, Maklerbewertung, Gutachterausschuss, Sonderfaktoren und BFH-AdV-Linie zu deutlich niedrigerem gemeinem Wert dokumentieren.

# Grundsteuer: Gemeiner Wert und Gutachtenstrategie

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Grundsteuer: Gemeiner Wert und Gutachtenstrategie` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Bereite den Nachweis vor, dass der festgestellte Grundsteuerwert im Einzelfall erheblich über dem gemeinen Wert liegt. Der Skill hilft, ohne voreilige Gutachtenkosten eine belastbare Belegstrategie zu bauen.

## Belegtreppe

1. **Schnellbelege**: aktueller Kaufpreis, nicht nur Wunschpreis; Exposé; Maklerbewertung; Vergleichsangebote.
2. **Objektbelege**: Fotos, Baumängel, Denkmalschutz, Erschließung, Lageeinschränkungen, Altlasten, Leerstand.
3. **Marktbelege**: Bodenrichtwertzone, Gutachterausschuss, Vergleichspreise.
4. **Sachverständigengutachten**: wenn Streitwert und Erfolgsaussicht es tragen.

## Prüffragen

- Ist der Kaufpreis nahe am Hauptfeststellungszeitpunkt oder muss zeitlich angepasst werden?
- War der Kaufpreis fremdüblich?
- Gibt es Sonderrechte, Belastungen oder Nutzungsbeschränkungen?
- Sind Mängel objektiv dokumentiert?
- Wird nur der Bodenwert angegriffen oder auch Gebäude-/Ertragswert?

## BFH-Linie

Die BFH-AdV-Beschlüsse vom 27.05.2024 ermöglichen im Eilverfahren eine Argumentation über den niedrigeren gemeinen Wert. Das ersetzt nicht den Nachweis. Formuliere daher nie "wegen BFH automatisch auszusetzen", sondern "ernstliche Zweifel bei plausibel belegter erheblicher Abweichung".

## Output

- Belegtreppe mit Kosten-Nutzen-Einschätzung.
- Gutachter-Briefing mit konkreter Bewertungsfrage.
- AdV-Begründungsbaustein.
- Anlageverzeichnis.
- Risikoabschnitt: Kosten, Beweislast, Zeit, Hauptsache.

## Praktischer Tipp

- "Erhebliche Abweichung" nach BFH-AdV-Linie heißt: in den entschiedenen Fällen lagen festgestellter Grundsteuerwert und plausibler gemeiner Wert um deutlich mehr als 40 % auseinander. Bei kleineren Abweichungen besser auf konkrete Bewertungsfehler stützen, nicht auf den gemeinen Wert.
- Kosten-Nutzen-Schwelle für Sachverständigengutachten: erst sinnvoll, wenn die jährliche Mehrbelastung über die nächsten fünf Jahre die Gutachterkosten (typisch 1.500 bis 4.000 EUR für ein Wohnobjekt) übersteigt. Sonst Belegtreppe-Stufe 1 bis 3 ausschöpfen.
- Verkehrswertgutachten muss die konkrete Bewertungsfrage adressieren: nicht "Verkehrswert", sondern "gemeiner Wert zum Hauptfeststellungszeitpunkt 01.01.2022 nach den allgemeinen Bewertungsgrundsätzen des § 9 BewG".

## Beispiel-Mustertext (AdV-Antrag)

> Die Aussetzung der Vollziehung ist gemäß § 361 Abs. 2 Satz 2 AO zu gewähren. Es bestehen ernstliche Zweifel an der Rechtmäßigkeit des Grundsteuerwertbescheids vom [Datum, AZ], weil der festgestellte Grundsteuerwert von EUR [...] den nach beigefügten Belegen (Anlagen 1 bis [n]) plausibilisierten gemeinen Wert von EUR [...] um [...] % übersteigt. Diese erhebliche Abweichung begründet im Lichte von BFH, Beschluss vom 27.05.2024 - II B 78/23 und II B 79/23, ernstliche Zweifel im Sinne des § 69 Abs. 2 Satz 2 FGO.

## Typische Fehler

- Maklerbewertung ohne Datumsangabe und ohne Marktbezug einreichen; das Finanzamt verlangt nachvollziehbare Vergleichsobjekte.
- Kaufpreis aus 2020 für den Stichtag 01.01.2022 ohne Zeitanpassung verwenden.
- AdV-Antrag ohne ausdrücklichen Hilfsantrag auf Sicherheitsleistung; bei hohen Beträgen riskant.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 7. `anw-grundsteuer-hebesatz-zahlungsplan`

**Fokus:** Kommunalen Grundsteuerbescheid prüfen: Hebesatz, Satzung, Fälligkeiten, Zahlungsplan, Stundung, Erlass, Vollstreckungsaufschub, Abgrenzung Finanzamt/Gemeinde und Kommunikation mit Hausverwaltung oder Kommune.

# Grundsteuer: Hebesatz, Zahlung und Gemeindeebene

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Grundsteuer: Hebesatz, Zahlung und Gemeindeebene` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Prüfe den Grundsteuerbescheid der Gemeinde und organisiere Zahlung, Stundung, Erlass oder kommunale Rechtsbehelfe. Dieser Skill ist nicht für Bewertungsfehler im Grundsteuerwertbescheid gedacht.

## Prüfen

1. Messbetrag aus dem Finanzamtsbescheid übernommen?
2. Hebesatz durch kommunale Satzung gedeckt?
3. Fälligkeiten korrekt?
4. Aufteilung auf Eigentümer, WEG, Hausverwaltung oder Erbbauberechtigte zutreffend?
5. Zahlung trotz Einspruch nötig?
6. Stundung, Ratenzahlung oder Erlass wegen unbilliger Härte realistisch?

## Typische Fehler

- falscher Messbetrag übernommen,
- altes Kassenzeichen oder falsches Objekt,
- falscher Eigentümer nach Verkauf,
- Hebesatzjahr verwechselt,
- Vorauszahlungen ohne neuen Bescheid fortgeschrieben,
- Hausverwaltung legt Kosten falsch auf Mieter oder WEG-Einheiten um.

## Output

Erstelle:

- Zahlungsplan mit Fälligkeiten und Vorfristen.
- Gemeindeschreiben bei Übernahmefehler.
- Stundungs-/Ratenzahlungsantrag, wenn nötig.
- Hinweis auf parallelen Einspruch beim Finanzamt, wenn die Bewertung falsch ist.
- Betriebskosten-/WEG-Hinweis nur als Nebensatz; vertiefte Prüfung an Miet-/WEG-Plugin abgeben.

## Abgrenzung

Wenn der Wert falsch ist, nicht bei der Gemeinde "korrigieren" wollen. Dann `anw-grundsteuer-kaltstart-bescheidkette` und `anw-grundsteuer-einspruch-adv-bfh` nutzen.

## Norm-Bezug konkret

- § 25 GrStG: Hebesatzrecht der Gemeinde.
- § 28 GrStG: Fälligkeit zu je einem Viertel zum 15.02., 15.05., 15.08., 15.11.
- § 27 GrStG: Jahresbescheid, Vorauszahlungen.
- § 33 GrStG: Erlass bei wesentlicher Ertragsminderung (insb. bei bebauten Grundstücken, Kulturgut).
- § 222 AO: Stundung wegen erheblicher Härte und Sicherheitsleistung.
- § 227 AO: Billigkeitserlass im Einzelfall.

## Praktischer Tipp

- Gegen den Gemeindegrundsteuerbescheid ist regelmäßig **Widerspruch nach VwGO** (nicht Einspruch nach AO) statthaft, weil es ein landesrechtlicher Verwaltungsakt ist. Frist und Form aus der Rechtsbehelfsbelehrung lesen; in einigen Bundesländern (z. B. NRW, Niedersachsen) ist das Vorverfahren abgeschafft, dann direkt Anfechtungsklage zum Verwaltungsgericht.
- § 33 GrStG-Erlass ist ein Antrag bis zum 31.03. des Folgejahres; Versäumung schließt den Erlass für das betreffende Jahr aus. Voraussetzung: Ertragsminderung über 50 % bei normaler Bewirtschaftung, nicht selbst verschuldet.
- Bei Eigentümerwechsel zum Jahreswechsel: Käufer schuldet erst ab Folgejahr (§ 10 Abs. 1 GrStG zum Stichtag); im Kaufvertrag aber häufig wirtschaftliche Übernahme pro rata temporis vereinbart - das ist nur schuldrechtlich, nicht gegenüber der Gemeinde wirksam.

## Beispiel-Mustertext (Stundungsantrag)

> Sehr geehrte Damen und Herren, hiermit beantrage ich für die mit Bescheid vom [Datum, AZ] festgesetzte Grundsteuer von EUR [...] Stundung gemäß § 222 AO. Die sofortige Einziehung würde eine erhebliche Härte bedeuten, weil [konkrete Lebenslage / Liquiditätsengpass mit Belegen]. Ich biete Ratenzahlung in monatlichen Teilbeträgen von EUR [...] ab dem [Datum] an. Auf eine Sicherheitsleistung wird verzichtet, weil [Begründung].

## Typische Fehler

- Rechtsbehelf gegen Hebesatzbescheid wird als Angriff auf den Grundsteuerwert geführt; die Gemeinde verweist auf den Grundlagenbescheid nach § 351 Abs. 2 AO - dort muss der Einspruch laufen.
- Zahlung "unter Vorbehalt" eingestellt, ohne förmliche AdV beim Finanzamt; Folge: Mahn- und Vollstreckungsverfahren der Gemeinde.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 8. `anw-grundsteuer-landesmodell-routing`

**Fokus:** Grundsteuer-Landesmodell-Routing: Bundesmodell von Baden-Wuerttemberg, Bayern, Hamburg, Hessen, Niedersachsen und punktuellen Abweichungen trennen; richtige Rechtsquelle, Bescheidart, BFH-/FG-Stand und Argumentationslinie bestimmen.

# Grundsteuer: Landesmodell-Routing

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Grundsteuer: Landesmodell-Routing` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Bestimme das richtige Grundsteuermodell und verhindere Modellvermischung. Dieser Skill ist besonders wichtig, wenn Mandanten mit Immobilien in mehreren Bundesländern arbeiten.

## Modellkarte

| Modellgruppe | Typische Route |
|---|---|
| Bundesmodell | BewG §§ 218 ff., GrStG, BFH-Bundesmodell-Linie |
| Baden-Württemberg | Landesgrundsteuergesetz, Bodenwertmodell, BFH-Stand 2026 gesondert prüfen |
| Bayern | wertunabhängiges Flächenmodell, landesrechtliche Normen prüfen |
| Hamburg | Flächen-/Wohnlagenmodell |
| Hessen | Flächen-Faktor-Modell |
| Niedersachsen | Flächen-Lage-Modell |
| punktuelle Abweichungen | Bundesmodell plus landesspezifische Messzahlen/Hebesatzrecht |

## Prüfschritte

1. Belegenheitsland je Grundstück erfassen.
2. Bescheidkette je Land trennen.
3. Landesgesetz und Verwaltungshinweise öffnen.
4. BFH-/FG-Stand für genau dieses Modell prüfen.
5. Nur dann verfassungsrechtlich argumentieren.

## Output

- Bundesland-Matrix.
- Zuständigkeitsliste Finanzamt/Gemeinde.
- Modellbedingte Angriffspunkte.
- Warnung, wenn eine Bundesmodell-Entscheidung nicht auf das Landesmodell passt.
- Vorschlag, welche Folgeskills geladen werden.

## Quellenregel

Aktuelle BFH-Fokusseite zur Grundsteuer und Landesgesetze prüfen. Keine pauschalen Aussagen wie "die Grundsteuer ist überall gleich" oder "BFH hat alles entschieden".

## Praktischer Tipp

- Bei multi-Bundesland-Portfolios: tabellarische Modellzuordnung anlegen mit Spalten Bundesland, Modell, Rechtsgrundlage, zuständiges Finanzamt, Bescheidstand, Einspruchsfrist. Pro Bundesland separater Bearbeiter, weil Argumentation, Belegtypen und Verwaltungspraxis stark voneinander abweichen.
- Bundesmodell-Argumente gegen Landesmodell zu spielen ist eine der häufigsten Schwachstellen in Einspruchsbegründungen. Beispiel: Bayerisches Flächenmodell ist wertunabhängig, daher gemeiner-Wert-Argumentation nach BFH II B 78/23 / II B 79/23 strukturell nicht übertragbar.
- Baden-Württemberg (Bodenwertmodell): hier ist die Bodenrichtwertzone der zentrale Angriffspunkt, weil der Gebäudewert keine Rolle spielt.

## Trade-off: Modellangriff vs. Einzelfallangriff

| Pfad | Geeignet bei | Risiko |
|---|---|---|
| Verfassungsrechtlicher Modellangriff | grundsätzliche Bedenken, Pilotverfahren | nach BFH 12.11.2025 (II R 25/24, II R 31/24, II R 3/25) im Bundesmodell schwierig - vor Ausgabe verifizieren auf bundesfinanzhof.de |
| Einzelfallangriff (Fläche, Wert, Bodenrichtwert) | klare Bewertungsfehler | erfordert Belege, Stichtagsbezug, Plausibilisierung |
| Hebesatzangriff (Gemeinde) | exzessive Erhöhung, Satzungsfehler | landesrechtlicher Rechtsweg, separater Bescheid |

Empfehlung: Erst Einzelfall prüfen, dann ggf. zusätzlich verfassungsrechtlich argumentieren, niemals umgekehrt.

## Typische Fehler

- Mandant hat Immobilien in BY und BW, Einspruch wird mit BFH-Linie zum Bundesmodell begründet; das geht in beiden Ländern fehl.
- "Hauptfeststellungszeitpunkt 01.01.2022" wird auch auf Bayern übertragen; dort gilt der Stichtag der Erklärung (Flächenmodell hat keine Hauptfeststellung im klassischen Sinn).

## 9. `anw-grundsteuer-verfassungscheck-bundesmodell`

**Fokus:** Verfassungsrechtlicher Grundsteuer-Check nach der Reform: BVerfG 10.04.2018 zur alten Einheitsbewertung, BFH 27.05.2024 AdV, BFH 12.11.2025 zum Bundesmodell, Art. 3 GG, Typisierung, gemeiner Wert, Landesmodelle und offene Verfahren sauber einordnen.

# Grundsteuer: Verfassungscheck Bundesmodell und Reformstand

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Grundsteuer: Verfassungscheck Bundesmodell und Reformstand` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Prüfe, ob ein Grundsteuerfall sinnvoll verfassungsrechtlich angegriffen werden kann. Trenne dabei:

- alte Einheitsbewertung bis 2024,
- neues Bundesmodell ab 2025,
- eigenständige Landesmodelle,
- individuelle Bewertungsfehler,
- reine Belastungsverschiebung ohne Rechtsfehler.

## Gesicherte Eckpunkte

- Das Bundesverfassungsgericht hat mit Urteil vom **10.04.2018 - 1 BvL 11/14, 1 BvL 12/14, 1 BvL 1/15, 1 BvR 639/11, 1 BvR 889/12** die alte Einheitsbewertung wegen Art. 3 Abs. 1 GG beanstandet und eine Reform verlangt.
- Die Reform gilt für die Grundsteuer ab 2025; Hauptfeststellungszeitpunkt ist regelmäßig der 01.01.2022.
- Der BFH hat mit Beschlüssen vom **27.05.2024 - II B 78/23 (AdV)** und **II B 79/23 (AdV)** im Eilverfahren ernstliche Zweifel für möglich gehalten, wenn der festgestellte Grundsteuerwert erheblich über dem plausibel belegten gemeinen Wert liegt.
- Der BFH hat mit Urteilen vom **12.11.2025 - II R 25/24, II R 31/24, II R 3/25** das neue Bewertungsrecht im Bundesmodell in den entschiedenen Konstellationen für verfassungsgemäß gehalten. Diese Linie ersetzt nicht die Prüfung individueller Bewertungsfehler.
- Im Mai 2026 sind beziehungsweise waren mehrere Verfahren zu Bundes- und Landesmodellen beim BFH relevant; vor Ausgabe aktuellen Stand in der BFH-Fokus-Seite prüfen.

## Prüfschema

1. **Modell bestimmen**: Bundesmodell, Baden-Württemberg, Bayern, Hamburg, Hessen, Niedersachsen oder punktuelle Abweichung.
2. **Streitgegenstand klären**: Wertfeststellung, Messbetrag oder Hebesatzbescheid.
3. **Typisierungsangriff filtern**: Pauschale "Grundsteuer ist verfassungswidrig"-Rüge ist nach der BFH-Linie schwach, wenn kein Einzelfehler dargelegt wird.
4. **Einzelfall öffnen**: Erhebliche Abweichung vom gemeinen Wert, falsche Grundstücksart, falsche Fläche, falscher Bodenrichtwert, unzutreffende Miete, falsches Baujahr.
5. **Rechtsschutz wählen**: Einspruch gegen Grundlagenbescheid, AdV, Klage; bei Gemeindehebesatz kommunalrechtliche Route.

## Formulierungshilfe

> Die verfassungsrechtliche Rüge wird nicht abstrakt als Angriff gegen die Grundsteuerreform geführt. Der Schwerpunkt liegt auf der konkreten gleichheitswidrigen Überbewertung der wirtschaftlichen Einheit, weil der festgestellte Grundsteuerwert nach den beigefügten Belegen deutlich oberhalb des gemeinen Werts liegt.

## Warnungen

- Nicht behaupten, das Bundesmodell sei nach BFH-Stand 2025/2026 generell verfassungswidrig.
- BFH-AdV-Beschlüsse sind keine Hauptsacheentscheidung, aber sehr wichtig für Aussetzung und Belegstrategie.
- Landesmodelle nicht mit dem Bundesmodell vermischen.
- Hebesatzkritik gehört in die kommunale Ebene; Bewertungsfehler gehören zum Finanzamt.

## Output

Gib eine Ampel:

- **Grün**: nur Belastungsverschiebung, keine tragfähige Rüge erkennbar.
- **Gelb**: Bewertungsfehler plausibel, Belege fehlen.
- **Rot**: erhebliche Überbewertung oder falsche Datenbasis mit Frist- und AdV-Bedarf.

Immer mit Quellenblock: BVerfG/BFH/Gesetz/Modellseite, Datum, Aktenzeichen, Link.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
