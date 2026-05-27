---
name: liquiditaetsvorschau-insolvenzrechtlich
description: "Erstellt und bewertet die rollierende Liquiditätsvorschau als strukturierte Arbeitsgrundlage für insolvenzrechtliche Tatbestände nach § 17 InsO (Zahlungsunfähigkeit) und § 19 Abs. 2 InsO (Fortbestehensprognose). Lädt, wenn geprüft werden soll, ob/wann Zahlungsunfähigkeit eingetreten ist, eine Liquiditätsbilanz für Gericht oder Insolvenzverwalter erstellt werden soll, oder die 13-Wochen- bzw. 24-Monats-Vorschau nach IDW S 11 zu konstruieren ist."
---

# Liquiditätsvorschau als insolvenzrechtliches Beweismittel

## Powerplugin-Hinweis

**Die fachlich aktualisierte und autarke Version dieses Skills lebt im Plugin Liquiditätsplanung (`liquiditaetsplanung`)** (Power-Plugin Liquiditätsvorschau) — mit dem strikten BGH-Schema (Passiva II zwingend, BGHZ 217, 129; 10-%-Schwelle BGHZ 163, 134; Bugwellenrspr. BGH II ZR 112/21; titulierte Forderungen BGH IX ZR 229/22; objektive Beurteilung BGH II ZR 139/23), Excel-Vorlage, optionalem HTML-Padlet oder Markdown-Artefakt und Banking-Wahl. PDFs liegen im Plugin unter `references/rechtsprechung/`. Wenn `liquiditaetsplanung` installiert ist, dorthin übergeben oder dessen Belege beim Erstellen der gerichtsfesten Liquiditätsbilanz beiziehen.

## Zweck

Dieser Skill strukturiert die Erstellung und Bewertung einer rollierenden Liquiditätsvorschau
ausschließlich aus insolvenzrechtlicher Perspektive. Im Mittelpunkt steht nicht die
steuerberaterliche Mandantenberatung, sondern die **insolvenzrechtliche Liquiditätsbilanz** als
Beweismittel: Wann ist der Schuldner zahlungsunfähig nach § 17 InsO geworden? Trägt die
Fortbestehensprognose nach § 19 Abs. 2 S. 1 InsO? Die Liquiditätsvorschau dient damit
dem Insolvenzverwalter, dem vorläufigen Insolvenzverwalter, dem Sachverständigen im
Eröffnungsverfahren sowie dem beratenden Anwalt bei der Haftungsrekonstruktion gegenüber
Geschäftsführern (§§ 15a, 15b InsO).

Die Abgrenzung zur steuerberaterlichen Sicht ist methodisch zwingend: Steuerliche
Liquiditätsplanungen verfolgen Planungszwecke, während die insolvenzrechtliche Liquiditätsbilanz
retrograd (für Stichtage in der Vergangenheit) oder prospektiv (für den Eröffnungsantragszeitpunkt)
einen **normativen Tatbestand** belegt oder widerlegt.

## Eingaben

| Eingabe | Erläuterung |
|---|---|
| Referenzstichtag | Datum, für den Zahlungsunfähigkeit geprüft wird (retrograd) oder voraussichtlicher Antragszeitpunkt |
| Kontoauszüge | Alle Bankkonten und Kassenbestände des Schuldners, mindestens 13 Wochen vor Stichtag |
| Offene-Posten-Liste (OPOS) | Fällige und binnen 3 Wochen fällig werdende Verbindlichkeiten (Gläubiger) und Forderungen (Schuldner) |
| Betriebswirtschaftliche Auswertungen (BWA) | Monatliche BWA inkl. Summen- und Saldenlisten, ggf. betriebsinterne Kostenstellenauswertungen |
| Kontokorrentrahmen | Bestätigte KK-Linie, aktueller Ausnutzungsgrad, etwaige Kündigung oder Reduzierung |
| SV-Bescheide / Finanzamt | Rückstände Sozialversicherung (Einzugsstellen), Umsatzsteuer-Vorauszahlungen, Lohnsteuer |
| Auftragsbestand / Verträge | Bestehende Dauerschuldverhältnisse, Auftragsrückstand, Abrechnungsmodalitäten (relevant für 24-Monate-Vorschau) |
| Planungsprämissen | Dokumentierte Annahmen zu Umsatzverlauf, Kostenbasis, geplanter Kapitalmaßnahmen (für Fortbestehensprognose) |

## Rechtlicher Rahmen

### § 17 InsO — Zahlungsunfähigkeit: Das 10-%/3-Wochen-Schema

Zahlungsunfähigkeit liegt vor, wenn der Schuldner nicht in der Lage ist, die fälligen
Zahlungspflichten zu erfüllen (§ 17 Abs. 2 S. 1 InsO). Bloße Zahlungsstockung — also eine
vorübergehende Illiquidität — ist kein Insolvenzgrund; entscheidend ist die **Unfähigkeit**,
nicht nur der vorübergehende Mangel.

Der BGH hat das operative Prüfschema entwickelt:

**BGH, Urt. v. 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 Rn. 17–18:**
Eine Liquiditätslücke von **weniger als 10 %** der fälligen Verbindlichkeiten begründet noch
keine Zahlungsunfähigkeit, sofern mit überwiegender Wahrscheinlichkeit innerhalb von **drei
Wochen** Deckung zu erwarten ist. Übersteigt die Lücke 10 %, ist Zahlungsunfähigkeit zu
vermuten, es sei denn, der Schuldner weist nach, dass die Lücke in drei Wochen vollständig
beseitigt werden kann. Diese Vermutung ist widerlegbar.

**BGH, Urt. v. 19.07.2007 – IX ZR 81/06, NJW 2007, 78 Rn. 36:**
Indizien für Zahlungsunfähigkeit sind u. a.: Nichtabführung von Sozialversicherungsbeiträgen,
Nichtzahlung von Löhnen und Gehältern, Einstellung der Zahlungen gegenüber wesentlichen
Gläubigern, Nichtbedienung von Bankkrediten, Überziehung des Kontokorrentrahmens ohne
Verlängerungsperspektive. Der Indizienkatalog ersetzt keine Liquiditätsbilanz, dient aber
deren Plausibilisierung im Gutachtenstil.

**BGH, Urt. v. 12.10.2006 – IX ZR 228/03, NZI 2007, 36:**
Forderungen, die der Gläubiger nachweislich gestundet hat oder für die eine ernsthafte
Stundungsvereinbarung — keine bloße Duldung — vorliegt, sind aus der Passivseite der
3-Wochen-Liquiditätsbilanz herauszunehmen. Bloßes Stillhalten oder Nichtgeltendmachen genügt
nicht; erforderlich ist eine klare, zumindest konkludente Stundungsabrede. In der Praxis ist
diese Abgrenzung besonders fehlerträchtig und zwingt zur sorgfältigen Einzelbewertung jeder
gestundeten Position.

### § 19 Abs. 2 InsO — Fortbestehensprognose (Überschuldung)

Überschuldung liegt vor, wenn das Vermögen des Schuldners die bestehenden
Verbindlichkeiten nicht mehr deckt, **es sei denn**, die Fortführung des Unternehmens ist
nach den Umständen überwiegend wahrscheinlich (§ 19 Abs. 2 S. 1 InsO). Die
Fortbestehensprognose ist damit negativer Tatbestand: Bei positiver Prognose entfällt der
Insolvenztatbestand der Überschuldung.

**Zeitraum der Prognose:** Durch das SanInsKG (in Kraft ab 09.11.2022) wurde der
Prognosezeitraum von 12 auf **4 Monate** verkürzt. Nach Auslaufen der SanInsKG-Verlängerung
gilt seit **01.01.2024 wieder der 12-Monats-Zeitraum** (§ 19 Abs. 2 S. 1 InsO a.F./n.F.
i.V.m. Art. 103l EGInsO). IDW S 11 empfiehlt für eine belastbare Prognose einen
Planungshorizont von **24 Monaten**, da kürze Zeiträume bei Sanierungssachverhalten
systematisch zu optimistisch sind.

### Kommentarliteratur

**Mock, in: Uhlenbruck, InsO, 16. Aufl. 2024, § 17 Rn. 5 und Rn. 44:**
Mock betont, dass für die Liquiditätsbilanz nach § 17 InsO ausschließlich fällige und
im Drei-Wochen-Zeitraum fällig werdende Verbindlichkeiten einzustellen sind; künftige,
noch nicht fällige Verbindlichkeiten bleiben außer Ansatz. Die Aktivseite beschränkt sich
auf sofort verfügbare Mittel (Kasse, Bankguthaben, realisierbare Forderungen im
Drei-Wochen-Fenster); stille Reserven oder unkündbare Anlagen zählen nicht.

**Schmerbach, in: K. Schmidt, InsO, 20. Aufl. 2023, § 17 Rn. 11 und Rn. 28:**
Schmerbach hebt hervor, dass die Drei-Wochen-Frist des § 17 Abs. 2 S. 1 InsO
keine Karenzzeit für den Schuldner, sondern ein Abgrenzungsmerkmal zwischen
Zahlungsunfähigkeit und Zahlungsstockung darstellt. Der Nachweis, dass innerhalb dieses
Zeitraums hinreichend Deckungsmittel zur Verfügung stehen werden, obliegt dem Schuldner
bzw. ist durch den Sachverständigen anhand konkreter Tatsachen zu belegen; bloße
Erwartungen oder Hoffnungen genügen nicht.

### IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen)

Der IDW S 11 (Stand: 25.01.2017) liefert den methodischen Rahmen für die gutachterliche
Beurteilung von Zahlungsunfähigkeit und Überschuldung. Er schreibt vor:

- **Stichtagsbezogene Liquiditätsbilanz** für § 17 InsO: Gegenüberstellung der liquiden
  Mittel (Zahlungsmittel I. Stufe) und der fälligen sowie innerhalb von 21 Tagen fällig
  werdenden Verbindlichkeiten (Zahlungsmittel II. Stufe für Mittelzuflüsse).
- **Integrierte Finanzplanung** für § 19 InsO: Ertrags-, Vermögens- und
  Liquiditätsplanung für mindestens 12 Monate (IDW S 11 empfiehlt 24 Monate).
- **Prüfungspflichten des Gutachters**: Plausibilisierung aller Planungsprämissen,
  Sensitivitätsanalyse, Dokumentation abweichender Szenarien.
- **Drei-Stufen-Ampel** (methodisch abgeleitet aus IDW S 11 Tz. 15–21 i.V.m. BGH
  IX ZR 123/04): Klassifizierung der Liquiditätslage als GRÜN, GELB oder ROT
  (siehe Ablauf-Abschnitt).

## Ablauf

Die Rekonstruktion der Liquiditätsvorschau durch Insolvenzverwalter oder Anwalt erfolgt
in folgenden Schritten:

**Schritt 1 — Datenbeschaffung**
Anforderung aller Kontoauszüge (Girokonto, Festgeld, Kreditlinie) für den relevanten
Zeitraum direkt von der Bank (§§ 97, 101 InsO im eröffneten Verfahren; im vorläufigen
Verfahren über Mitwirkungspflicht des Schuldners). Beschaffung aller OPOS-Listen
(Kreditorenbuchhaltung + Debitorenbuchhaltung), BWA mit Summen-/Saldenlisten sowie
Gehaltsabrechnungen und SV-Nachweise. Erhebung aller Stundungsvereinbarungen,
Ratenzahlungsvereinbarungen und Fälligkeitsverschiebungen schriftlich (E-Mails, Briefe).

**Schritt 2 — Plausibilisierung der Eingangsdaten**
Abgleich OPOS-Kreditoren gegen Buchführungsdaten und Kontoauszüge: Stimmen
gebuchte Verbindlichkeiten mit Kontoabflüssen überein? Sind Verbindlichkeiten gebucht,
die faktisch gestundet sind (Abgrenzung nach BGH IX ZR 228/03)? Abgleich
Forderungsbestände gegen Kontozuflüsse (Forderungsausfallquote schätzen).

**Schritt 3 — Wochenweise Aggregation (13-Wochen-Modell)**
Für jede der 13 Kalenderwochen wird eine eigene Zeile der Liquiditätsvorschau erstellt:

```
Woche N:
  (+) Anfangsbestand Kasse + Bank (verfügbar)
  (+) Erwartete Forderungseingänge (dokumentiert, konkret)
  (+) Freie KK-Linie (soweit nicht gekündigt)
  (-) Fällige Verbindlichkeiten der Woche N
  (-) Bis Ende Woche N+2 fällig werdende Verbindlichkeiten (3-Wochen-Fenster)
  (=) Netto-Liquiditätsposition der Woche N
  (%) Liquiditätslücke = Defizit / Summe fällige Verbindlichkeiten
```

Für die 13-Wochen-Vorschau werden wochen- und tagesgenaue Fälligkeiten
benötigt; späteste Verfalldaten aus Rechnungen, Mahnungen und Verträgen sind
zu dokumentieren.

**Schritt 4 — Drei-Stufen-Ampel-Bewertung**

| Ampel | Kriterium | Rechtliche Konsequenz |
|---|---|---|
| GRÜN | Liquiditätslücke < 10 % der fälligen Verbindlichkeiten | Keine Zahlungsunfähigkeit; Zahlungsstockung möglich |
| GELB | Lücke ≥ 10 %, aber Beseitigung binnen 3 Wochen überwiegend wahrscheinlich | Zahlungsstockung; Überwachungspflicht; Maßnahmen dokumentieren |
| ROT | Lücke ≥ 10 % und keine Beseitigung binnen 3 Wochen | Zahlungsunfähigkeit nach § 17 InsO; Antragspflicht § 15a InsO ausgelöst |

**Schritt 5 — 24-Monats-Vorschau (Fortbestehensprognose)**
Aufbauend auf der 13-Wochen-Vorschau wird die integrierte Finanzplanung auf 24 Monate
verlängert. Die Prämissen sind schriftlich zu fixieren und durch unabhängige Belege
(Auftragsbestand, Vertragskonditionen, Finanzierungszusagen) zu unterlegen. Das Ergebnis
ist ein monatlicher Cashflow-Plan mit expliziter Darstellung der
Mindestliquiditätsreserve. Für die Fortbestehensprognose nach § 19 Abs. 2 InsO muss
die Liquiditätsplanung zeigen, dass der Schuldner mit überwiegender Wahrscheinlichkeit
in der Lage sein wird, seine Verbindlichkeiten laufend zu erfüllen.

**Schritt 6 — Gerichtsfeste Dokumentation**
Das Ergebnis wird als Gutachten oder gutachtenähnliche Stellungnahme dokumentiert:
Darstellung der Methodik, Auflistung aller Quellen, Sensitivitätsanalyse (Best/Base/Worst
Case), explizite Ampel-Bewertung mit Datumsangabe. Im Gerichtsverfahren muss die
Dokumentation geeignet sein, als Anlage zum Insolvenzantrag oder als
Sachverständigengutachten (§ 22 InsO) zu dienen.

## Ausgabeformat

Das Ausgabedokument ist eine **juristische Stellungnahme im Gutachtenstil** und umfasst:

1. **Stichtagsbestimmung** — welcher Stichtag wird untersucht und warum
2. **Datenbasis** — tabellarische Auflistung aller verwendeten Unterlagen mit Datum und
   Herkunft
3. **13-Wochen-Liquiditätsbilanz** — Tabelle mit Wochen-Spalten, Einzelpositionen
   (Aktiv/Passiv), Netto-Liquiditätsposition und prozentualer Lücke
4. **Ampel-Ergebnis** je Woche mit rechtlicher Bewertung (GRÜN/GELB/ROT + Begründung)
5. **Stundungsabzüge** — Einzelauflistung aller herausgerechneten Verbindlichkeiten mit
   Nachweisbeschreibung (BGH IX ZR 228/03)
6. **24-Monats-Vorschau** (sofern Fortbestehensprognose zu beurteilen) — monatlicher
   Cashflow, Prämissenblatt, Szenarioanalyse
7. **Rechtliche Subsumtion** — Abschließende Einordnung: liegt § 17 InsO vor, wenn ja
   seit wann?; liegt § 19 InsO vor?
8. **Hinweis auf Antragspflicht** — soweit Tatbestand des § 15a InsO ausgelöst

Alle Tabellen enthalten Quellenverweise auf die zugrunde liegenden Belegpositionen
(Kontoauszug, OPOS-Zeile, Rechnung).

## Beispiel

**Sachverhalt: Muster-Bauservice GmbH**

Die Muster-Bauservice GmbH (20 Mitarbeiter, Jahresumsatz ca. 2 Mio. EUR, Sitz
Hannover) stellt am 15. März 2025 beim Insolvenzgericht einen Eigenantrag. Der
Geschäftsführer behauptet, Zahlungsunfähigkeit sei erst am 10. März 2025 eingetreten.
Der vorläufige Insolvenzverwalter hat folgende Eckdaten ermittelt:

- Kassebestand 15.03.2025: 3.200 EUR
- Bankguthaben (laufendes Konto): 8.500 EUR
- Kontokorrentlinie: 150.000 EUR, zu **92 %** ausgenutzt (freie Linie: 12.000 EUR,
  nicht erweiterungsfähig; Hausbank hat mit Schreiben vom 08.03.2025 eine
  Kreditlinienerweiterung abgelehnt)
- Fällige Verbindlichkeiten zum 15.03.2025: 87.400 EUR (davon SV-Rückstand
  Februar 2025: 18.300 EUR; USt-Vorauszahlung Januar 2025: 11.200 EUR;
  Lieferantenverbindlichkeiten > 30 Tage: 57.900 EUR)
- Binnen 3 Wochen (bis 05.04.2025) fällig werdende Verbindlichkeiten: 34.600 EUR
  (Löhne März 2025: 28.400 EUR; Mietfälligkeit 01.04.2025: 6.200 EUR)
- Dokumentierte Forderungseingänge binnen 3 Wochen: 14.300 EUR (zwei
  Abschlagsrechnungen mit Zahlungsziel 31.03.2025, Bonität der Auftraggeber geprüft)
- Eine Stundungsvereinbarung liegt nur für einen Lieferanten (Fischer Baustoffe GmbH,
  4.200 EUR) vor — schriftlich bestätigt bis 30.04.2025.

**Gutachtenstil-Subsumtion:**

*I. Liquide Mittel I. Stufe (sofort verfügbar):*
Kasse 3.200 EUR + Bank 8.500 EUR + freie KK-Linie 12.000 EUR = **23.700 EUR**.

*II. Erwartete Zuflüsse binnen 3 Wochen (Liquiditätsmittel II. Stufe):*
Forderungseingänge 14.300 EUR. Summe verfügbarer Mittel: 23.700 + 14.300 = **38.000 EUR**.

*III. Fällige und binnen 3 Wochen fällig werdende Verbindlichkeiten (Passivseite):*
Fällige Verbindlichkeiten 87.400 EUR abzüglich dokumentierte Stundung Fischer
Baustoffe GmbH 4.200 EUR (BGH IX ZR 228/03 (NZI 2007, 36)) = 83.200 EUR. Hinzu kommen
binnen-3-Wochen-Verbindlichkeiten 34.600 EUR. Passivseite gesamt: **117.800 EUR**.

*IV. Liquiditätslücke:*
117.800 EUR − 38.000 EUR = **79.800 EUR**. Quotient: 79.800 / 117.800 = **67,7 %**.

*V. Ampel-Bewertung:*
Die Liquiditätslücke beträgt 67,7 % und liegt damit weit über dem Schwellenwert von
10 % (BGH IX ZR 123/04, BGHZ 163, 134 Rn. 17). Eine Beseitigung der Lücke
binnen drei Wochen ist angesichts der abgelehnten Kreditlinienerweiterung, des hohen
SV-Rückstands und des begrenzten Auftragsbestands nicht überwiegend wahrscheinlich.
**Ergebnis: ROT — Zahlungsunfähigkeit nach § 17 InsO liegt vor.**

*VI. Zeitpunkt der Zahlungsunfähigkeit:*
Unter Berücksichtigung der Indizien nach BGH IX ZR 81/06 Rn. 36 (Nichtabführung
SV-Beiträge Februar 2025, die am 28.02.2025 fällig waren; Überziehung der KK-Linie
auf 92 % bereits seit Januar 2025 laut Kontoauszügen) ist Zahlungsunfähigkeit nicht
erst am 10.03.2025, sondern spätestens **Ende Februar 2025** eingetreten. Die
13-Wochen-Rückschau bestätigt, dass die Liquiditätslücke zum 28.02.2025 bereits
ca. 55 % betragen hat. Die Behauptung des Geschäftsführers, Zahlungsunfähigkeit sei
erst am 10.03.2025 eingetreten, ist durch die Liquiditätsbilanz widerlegt.

## Risiken und typische Fehler

**1. Verwechslung von Zahlungsunfähigkeit und Zahlungsstockung**
Die 10-%-Grenze ist eine widerlegliche Vermutung, kein starrer Schwellenwert. Wer
mechanisch auf die Quote abstellt, ohne die 3-Wochen-Beseitigungsmöglichkeit zu prüfen,
begeht einen methodischen Fehler.

**2. Unkritische Übernahme von Stundungsbehauptungen**
Die bloße Duldung durch einen Gläubiger (kein Mahn-, kein Vollstreckungsschreiben)
begründet keine Stundung im Sinne von BGH IX ZR 228/03 (NZI 2007, 36). Fehlendes Stundungs-
nachweis führt zur Aufnahme der Position in die Passivseite.

**2a. Aussetzung der Vollziehung (§ 361 AO / § 69 FGO) fälschlich als Stundung werten**
AdV-Verfügungen hemmen nur die Vollziehung; die Fälligkeit der Steuerforderung bleibt
unberührt. AdV-Beträge sind weiter **Passiva I**, soweit nicht zusätzlich eine schriftliche
§ 222 AO-Stundung mit Fälligkeitsverschiebung über den Stichtag hinaus vorliegt. Eine
Herausnahme von AdV-Beträgen aus den Passiva I führt zu einer methodisch falschen
"nicht zahlungsunfähig"-Feststellung.

**3. Einbeziehung nicht fälliger Verbindlichkeiten**
Verbindlichkeiten mit Fälligkeit außerhalb des 3-Wochen-Fensters dürfen nach
Mock, in: Uhlenbruck, InsO, 16. Aufl. 2024, § 17 Rn. 44 nicht in die Liquiditätsbilanz
eingestellt werden. Dies verwechselt die § 17-Bilanz mit einer Überschuldungsbilanz.

**4. Prognosezeitraum der Fortbestehensprognose verwechseln**
Seit 01.01.2024 gilt wieder der 12-Monats-Zeitraum für § 19 InsO. Das SanInsKG-Regime
mit 4 Monaten ist ausgelaufen. IDW S 11 empfiehlt weiterhin 24 Monate.

**5. Fehlende Sensitivitätsanalyse**
Eine Liquiditätsvorschau ohne Best/Base/Worst-Case-Szenarien ist für Gerichtszwecke
unzureichend; sie ermöglicht keine Einschätzung der Planungsrobustheit.

**6. Datierungsfehler bei der Fälligkeitsbestimmung**
Verzugsbeginn (§ 286 BGB) und Fälligkeitsberechnung (§ 271 BGB) sind voneinander
zu trennen. Für die Liquiditätsbilanz zählt die **Fälligkeit**, nicht der Zahlungsverzug.

**7. Kontokorrentlinie ohne Kündigungsprüfung**
Eine bereits faktisch gekündigte oder nicht mehr verlängerungsfähige KK-Linie darf
nicht als freie Liquiditätsreserve angesetzt werden. Schmerbach, in: K. Schmidt, InsO,
20. Aufl. 2023, § 17 Rn. 28, betont, dass nur tatsächlich verfügbare Mittel einzustellen
sind.

## Quellenpflicht

Folgende Belege sind in jeder Liquiditätsvorschau mit insolvenzrechtlichem Zweck
zwingend zu zitieren und zu berücksichtigen:

**BGH-Rechtsprechung (Mindest-Pinpoints):**
- BGH, Urt. v. 24.05.2005 – IX ZR 123/04, BGHZ 163, 134 Rn. 17–18
  (10-%-/3-Wochen-Schema; Abgrenzung Zahlungsunfähigkeit/Zahlungsstockung)
- BGH, Urt. v. 19.07.2007 – IX ZR 81/06, NJW 2007, 78 Rn. 36
  (Indizienkatalog Zahlungsunfähigkeit)
- BGH, Urt. v. 12.10.2006 – IX ZR 228/03, NZI 2007, 36(Stundungen in der Liquiditätsbilanz)

**Kommentarliteratur:**
- Mock, in: Uhlenbruck, InsO, 16. Aufl. 2024, § 17 Rn. 5, 44
- Schmerbach, in: K. Schmidt, InsO, 20. Aufl. 2023, § 17 Rn. 11, 28

**IDW-Standard:**
- IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen), Stand 25.01.2017,
  insb. Tz. 15–21 (Liquiditätsbilanz) und Tz. 40–55 (Fortbestehensprognose)

**Ergänzend empfohlen:**
- MüKoInsO/Drukarczyk/Schüler, 4. Aufl. 2019, § 19 Rn. 66 ff.
  (integrierte Finanzplanung für Fortbestehensprognose)
- Karsten Schmidt/Uhlenbruck (Hrsg.), Die GmbH in Krise, Sanierung, Insolvenz,
  6. Aufl. 2024, Kap. 5 Rn. 5.23 ff.

---
*Dieser Skill ersetzt keine konkrete anwaltliche Beratung im Einzelfall.*


## Triage — Liquiditaetsvorschau insolvenzrechtlich

Bevor losgelegt wird, klaere:

1. **Zweck?** ZU-Test § 17 InsO (3-Wochen-Fenster) oder Fortbestehensprognose § 19 Abs. 2 InsO (12 Monate)?
2. **Methode?** Direkte Methode (Cash In / Cash Out) bevorzugt fuer InsO-Beurteilung.
3. **Zeitraum?** 3 Wochen (akute ZU-Pruefung), 13 Wochen (operativer Forecast), 12-24 Monate (Fortbestehensprognose).
4. **Eingabedaten?** Offene Posten (OPOS), Bankkontoauszuege, Steuer- und SV-Verbindlichkeiten.
5. **Stichtag?** Fuer InsO-Verfahren muss Stichtag tag-genau sein.
