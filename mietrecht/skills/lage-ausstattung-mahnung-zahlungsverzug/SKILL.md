---
name: lage-ausstattung-mahnung-zahlungsverzug
description: "Lage Ausstattung Mahnung Zahlungsverzug: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lage Ausstattung Mahnung Zahlungsverzug

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Lage Ausstattung Mahnung Zahlungsverzug** im Plugin Mietrecht (Wohnraum/Gewerbe). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lage-und-ausstattung-erheben` | Strukturierte Datenerhebung für die Einordnung in den Mietspiegel — Adresse Baujahr Wohnflaeche Bad Kueche Heizung Wohnungsausstattung Gebaeudeausstattung. Erfasst alle Merkmale die in qualifizierten Mietspiegeln als Sondermerkmale bewertet werden (Bodenbelag Fenster Balkon Terrasse Aufzug Stellplatz Energieeffizienz). Erzeugt eine Checkliste und ein strukturiertes Erhebungsprotokoll als Grundlage für ortsuebliche Vergleichsmiete Mieterhoehung Mietsenkungsverlangen oder Klage. |
| `mahnung-zahlungsverzug-mieter` | Vermietersicht — verfasse Mahnung und ggf. fristlose Kündigung bei Zahlungsverzug des Mieters. Prüfroutine deckt Verzug nach § 286 BGB Fälligkeit der Miete (§ 556b Abs. 1 BGB) Mahnschreiben Aufrechnungsverbot fristlose Kündigung nach § 543 Abs. 2 Nr. 3 BGB (eine Monatsmiete plus zwei aufeinanderfolgende Termine oder Rückstand von zwei Monatsmieten über zwei Termine) hilfsweise ordentliche Kündigung nach § 573 Abs. 2 Nr. 1 BGB und Schonfristzahlung des Mieters nach § 569 Abs. 3 BGB (Nachholung innerhalb von zwei Monaten nach Zustellung der Räumungsklage). Erzeugt gestuftes Schreibenpaket mit Disclaimer. |
| `mandat-triage-mietrecht` | Strukturierte Eingangs-Abfrage für mietrechtliche Mandate. Klaert Mandantenrolle (Vermieter Mieter WEG-Eigentuemer Verwalter) Gegenstandsart (Wohnraum Gewerbe WEG) Sachgebiet (Kündigung Mieterhoehung Mietminderung Modernisierung Nebenkostenabrechnung Mietkaution-Rückforderung Eigenbedarf Sanierung Räumung WEG-Beschluss WEG-Hausgeld-Klage). Fristen-Sofort-Check Kündigungs-Frist nach § 573c BGB Räumungs-Frist § 721 ZPO WEG-Klage ein Monat § 45 WEG Modernisierung-Ankündigung drei Monate vorher Mieterhoehung Zustimmungs-Frist zwei Monate § 558b BGB. Eskalation Telefon-Sofort bei Räumungstermin laufender Kündigungs-Frist. |

## Arbeitsweg

Im Plugin Mietrecht (Wohnraum/Gewerbe) gilt für **Lage Ausstattung Mahnung Zahlungsverzug**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `lage-und-ausstattung-erheben`

**Fokus:** Strukturierte Datenerhebung für die Einordnung in den Mietspiegel — Adresse Baujahr Wohnflaeche Bad Kueche Heizung Wohnungsausstattung Gebaeudeausstattung. Erfasst alle Merkmale die in qualifizierten Mietspiegeln als Sondermerkmale bewertet werden (Bodenbelag Fenster Balkon Terrasse Aufzug Stellplatz Energieeffizienz). Erzeugt eine Checkliste und ein strukturiertes Erhebungsprotokoll als Grundlage für ortsuebliche Vergleichsmiete Mieterhoehung Mietsenkungsverlangen oder Klage.

# Lage und Ausstattung erheben

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Lage und Ausstattung erheben` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


Dieser Skill leitet eine vollständige Datenerhebung an. Ergebnis ist ein strukturiertes Protokoll, das in jeden anderen Skill dieses Plugins einfliesst.

## Disclaimer

Diese Erhebung ersetzt keine Rechtsberatung. Sie ist ein Vorbereitungsschritt für eine spätere rechtliche Prüfung. Bei strittigen Punkten amtliche Quellen heranziehen oder Rechtsrat einholen.

## Workflow

### 1. Adresse und Lage

- Vollständige Adresse (Straße, Hausnummer, PLZ, Ort).
- Stadt-/Stadtteil/Quartier.
- Wohnlagen-Zuordnung nach dem amtlichen Straßenverzeichnis oder Geoportal der Stadt (einfach / mittel / gut). Wenn unklar: Link auf das amtliche Verzeichnis aus references/mietspiegel-quellen.md.

### 2. Gebäude

- Baujahr (laut Mietvertrag, Grundbuchauszug oder Bauakte).
- Letzte umfassende Modernisierung (Jahr, Umfang).
- Anzahl Wohneinheiten.
- Aufzug ja/nein.
- Stellplatz/Garage zur Wohnung gehoerig.
- Energieausweis (Verbrauch oder Bedarf, kWh/(m² · a)).

### 3. Wohnung

- Wohnfläche in m² nach Wohnflächenverordnung (WoFlV).
- Anzahl Zimmer.
- Stockwerk.
- Bodenbelaege je Raum (Parkett, Laminat, Fliesen, Teppich).
- Fenster (Doppel- oder Dreifachverglasung, Holz/Kunststoff).
- Balkon / Loggia / Terrasse (Größe, Ausrichtung).
- Keller / Abstellraum außerhalb der Wohnung.

### 4. Bad

- Anzahl Baeder/WCs.
- Wanne und/oder Dusche.
- Fenster im Bad.
- Bodenheizung.

### 5. Küche

- Einbauküche mitvermietet ja/nein.
- Geräte (Herd, Backofen, Kuehlschrank, Geschirrspueler).

### 6. Heizung und Warmwasser

- Heizungsart (Gas, Fernwaerme, Oel, Waermepumpe).
- Zentral oder Etagenheizung.
- Warmwasserbereitung (zentral, dezentral, über Heizung).

### 7. Mietvertrag

- Vertragsdatum.
- Aktuelle Nettokaltmiete und Vorauszahlungen.
- Indexmiete, Staffelmiete oder Festmiete.
- Schönheitsreparaturklausel (im Original-Wortlaut zitieren).
- Schlüsselgeld, Kaution.

## Ausgabe

Protokoll als Markdown mit den oben genannten Abschnitten plus Quellenangabe (woher stammt jede Information: Mietvertrag, Augenschein, Energieausweis, Straßenverzeichnis). Dieses Protokoll ist Input für alle weiteren Skills.

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette

- Ortsueblliche Vergleichsmiete: § 558 BGB
- Begruendungsmittel: § 558a BGB
- Kappungsgrenze: § 558 Abs. 3 BGB

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `mahnung-zahlungsverzug-mieter`

**Fokus:** Vermietersicht — verfasse Mahnung und ggf. fristlose Kündigung bei Zahlungsverzug des Mieters. Prüfroutine deckt Verzug nach § 286 BGB Fälligkeit der Miete (§ 556b Abs. 1 BGB) Mahnschreiben Aufrechnungsverbot fristlose Kündigung nach § 543 Abs. 2 Nr. 3 BGB (eine Monatsmiete plus zwei aufeinanderfolgende Termine oder Rückstand von zwei Monatsmieten über zwei Termine) hilfsweise ordentliche Kündigung nach § 573 Abs. 2 Nr. 1 BGB und Schonfristzahlung des Mieters nach § 569 Abs. 3 BGB (Nachholung innerhalb von zwei Monaten nach Zustellung der Räumungsklage). Erzeugt gestuftes Schreibenpaket mit Disclaimer.

# Mahnung und Kündigung bei Zahlungsverzug (Vermieter / Hausverwaltung)

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mahnung und Kündigung bei Zahlungsverzug (Vermieter / Hausverwaltung)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Disclaimer (Schlüsselstelle, mehrfach)

Eine Zahlungsverzugskündigung ist die mietrechtlich folgenreichste Erklärung. Eine formale oder materielle Fehlkündigung ist unwirksam und kann zu Schadensersatzanspruechen des Mieters führen. Vor Versand einer fristlosen Kündigung ist eine fachanwaltliche Prüfung dringend empfohlen. Diese Auto-Erstellung ersetzt nicht die anwaltliche Vertretung.

## Workflow

### Schritt 1 — Fälligkeit und Verzug prüfen

- **Fälligkeit** der Miete: spätestens am dritten Werktag eines jeden Monats (§ 556b Abs. 1 BGB) — soweit vertraglich nichts anderes vereinbart ist.
- **Verzug** ohne Mahnung tritt nach § 286 Abs. 2 Nr. 1 BGB ein wenn die Miete kalendermaessig bestimmt ist (was bei § 556b BGB der Fall ist).
- Eine Mahnung ist also rechtlich nicht zwingend — als Vorstufe zur Kündigung aber dringend empfohlen (Beweisbarkeit gutes Verhältnis Schonfristoption).

### Schritt 2 — Mahnschreiben

- Sachliche knappe Aufforderung zur Zahlung des konkreten Rückstands.
- Frist zur Zahlung (eine bis zwei Wochen genügen wegen Verzugs).
- Hinweis auf drohende Kündigung wenn nicht gezahlt wird.
- Hinweis auf laufende Verzugszinsen (§ 288 BGB).

### Schritt 3 — Voraussetzungen der fristlosen Kündigung (§ 543 Abs. 2 Nr. 3 BGB)

Die fristlose Kündigung wegen Zahlungsverzugs ist zulässig wenn:

- **Variante a**: der Mieter für **zwei aufeinanderfolgende Termine** mit der Entrichtung der Miete oder eines nicht unerheblichen Teils der Miete im Verzug ist. "Nicht unerheblich" = mehr als eine Monatsmiete.
- **Variante b**: in einem Zeitraum der sich über **mehr als zwei Termine** erstreckt mit einem Betrag in Verzug ist der **zwei Monatsmieten** erreicht.

Was zur Miete zählt: Grundmiete plus Nebenkostenvorauszahlungen plus etwaige Heizkostenvorauszahlungen.

### Schritt 4 — Ordentliche Kündigung als Hilfsantrag (§ 573 Abs. 2 Nr. 1 BGB)

- Hilfsweise zur fristlosen Kündigung ist die ordentliche Kündigung wegen erheblicher schuldhafter Pflichtverletzung zulässig.
- Frist nach § 573c BGB (drei sechs oder neun Monate je nach Mietdauer).
- Empfehlung: in einem Schreiben fristlos hilfsweise ordentlich kündigen.

### Schritt 5 — Formale Anforderungen (§ 568 Abs. 1 BGB)

- **Schriftform** zwingend mit eigenhändiger Unterschrift aller Vermieter.
- **Begründung** im Schreiben — konkrete Aufstellung der rückständigen Monate und Betraege (§ 569 Abs. 4 BGB).
- **Hinweis** auf das Recht des Mieters die Wohnung durch Nachzahlung zu erhalten (§ 569 Abs. 3 Nr. 2 BGB) — Schonfristzahlung innerhalb von **zwei Monaten** nach Zustellung der Raeumungsklage.

### Schritt 6 — Schonfristzahlung des Mieters (§ 569 Abs. 3 Nr. 2 BGB)

- Wenn der Mieter nach Zugang der fristlosen Kündigung aber spätestens bis zum Ablauf von zwei Monaten nach Zustellung der **Raeumungsklage** den gesamten Rückstand begleicht oder eine öffentliche Stelle die Zahlung verbindlich zusagt: **fristlose Kündigung wird unwirksam**.
- Wichtig: die Schonfristzahlung wirkt nur für die fristlose Kündigung — eine hilfsweise erklärte **ordentliche** Kündigung bleibt nach BGH-Rspr. wirksam.
- Schonfristzahlung kann nicht mehrfach in Anspruch genommen werden (§ 569 Abs. 3 Nr. 2 Satz 2 BGB) — bei wiederholtem Zahlungsverzug ist sie ausgeschlossen wenn binnen zwei Jahren bereits einmal angewendet.

### Schritt 7 — Prüfroutine vor Versand

- Rückstandsberechnung dokumentiert (Monat für Monat mit Sollstellung und Zahlung).
- Schwelle eine Monatsmiete plus zwei Termine oder zwei Monatsmieten über zwei Termine erreicht.
- Konkrete Bezifferung des Rückstands im Kündigungsschreiben.
- Alle Vermieter unterzeichnen die Kündigung.
- Zustellung mit Nachweis (Einschreiben mit Rückschein oder Bote).
- Hinweis auf Schonfristzahlung im Schreiben (nicht zwingend aber empfohlen).

## Schreibenpaket

### A. Mahnschreiben

Sachlich kurz. Anrede mit Namen. Bezugnahme auf den Mietvertrag. Konkrete Aufstellung des Rückstands. Frist zur Zahlung. Hinweis auf Verzugszinsen und drohende Kündigung. Höflichkeitsformel.

### B. Fristlose Kündigung mit hilfsweiser ordentlicher Kündigung

1. Absender Vermieter mit Anschrift.
2. Adresse aller Mieter namentlich.
3. Bezugnahme auf den Mietvertrag.
4. Kündigungserklärung — fristlos nach § 543 Abs. 2 Nr. 3 BGB.
5. Hilfsweise ordentliche Kündigung nach § 573 Abs. 2 Nr. 1 BGB mit konkretem Endtermin nach § 573c BGB.
6. Begründung mit konkreter Aufstellung der rückständigen Monate und Betraege.
7. Hinweis auf Schonfristzahlung nach § 569 Abs. 3 Nr. 2 BGB.
8. Hinweis auf Widerspruchsrecht nach § 574 BGB für die hilfsweise ordentliche Kündigung.
9. Eigenhaendige Unterschrift aller Vermieter.

## Hinweis zur Raeumungsklage

Wenn der Mieter nach Ablauf der Kündigungsfrist nicht raeumt: **Raeumungsklage** zum Amtsgericht am Belegenheitsort (§ 29a ZPO). Siehe Skill `klageentwurf-amtsgericht`. **Disclaimer** — die Raeumungsklage ist anwaltliche Praxis; Selbstvertretung ist beim Amtsgericht zwar möglich aber nicht empfohlen.

## Vor Versand (Disclaimer wiederholt)

Vor Versand der fristlosen Kündigung: fachanwaltliche Prüfung der Rückstandsberechnung der Schwellenwerte und der Schonfristregelung. Risiko: Unwirksamkeit Schadensersatz Verzug auf eigener Seite. Die Schonfristzahlung kann das gesamte Verfahren wieder neutralisieren — der Vermieter muss dann ordentlich gekündigt haben um den Mieter langfristig loszuwerden.

## Aktuelle Rechtsprechung — Leitsaetze

- BGH, Urt. v. 09.07.2025 – Az. VIII ZR 287/23 — Schonfristzahlung nach § 569 Abs. 3 Nr. 2 BGB heilt nur die fristlose, nicht die ordentliche Kuendigung wegen Zahlungsverzugs. Klarstellung des Streits mit dem LG Berlin II. Folge: Doppelkuendigung (fristlos hilfsweise ordentlich) bleibt die strategisch sichere Loesung fuer den Vermieter. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=09.07.2025&Aktenzeichen=VIII+ZR+287/23
- BGH, Urt. v. 01.07.2020 – Az. VIII ZR 323/18 — Schonfristzahlung (§ 569 Abs. 3 Nr. 2 BGB) beseitigt nur die fristlose Kuendigung wegen Zahlungsverzugs; eine hilfsweise erklaerte ordentliche Kuendigung nach § 573 Abs. 2 Nr. 1 BGB bleibt wirksam. Ein Ausschluss der Sozialklausel § 574 Abs. 1 Satz 2 BGB greift, weil ein Grund vorliegt, der den Vermieter zur fristlosen Kuendigung berechtigt hätte. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=01.07.2020&Aktenzeichen=VIII+ZR+323/18
- BGH, Beschl. v. 08.12.2021 – Az. VIII ZR 32/20 — Erheblichkeit des Mietrueckstands im Sinne von § 573 Abs. 2 Nr. 1 BGB; massgeblich ist die Gesamthoehe des Rueckstands, nicht die Aufgliederung in einzelne Monatsbetraege. Bestaetigt die Wertungslinie zur ordentlichen Kuendigung neben der fristlosen. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=08.12.2021&Aktenzeichen=VIII+ZR+32/20
- Weitere Rechtsprechungslinien des VIII. ZS zu § 543, § 569 BGB vor Ausgabe ueber https://www.bundesgerichtshof.de und https://dejure.org verifizieren.

## Basiszinssatz § 247 BGB und Verzug

- Basiszinssatz zum 01.01.2026: 1,27 Prozent (Bundesbank-Bekanntmachung); B2C-Verzugszinssatz 6,27 Prozent. Quelle: https://www.bundesbank.de/de/presse/pressenotizen/bekanntgabe-des-basiszinssatzes-zum-1-januar-2026-basiszinssatz-bleibt-unveraendert-bei-1-27--973974
- Halbjaehrliche Pruefung am 01.01. und 01.07. erforderlich.

## Paragrafenkette

§§ 543, 569, 573 BGB — Kuendigungsvoraussetzungen Zahlungsverzug; § 286 BGB — Verzug; § 569 Abs. 3 BGB — Schonfrist; § 247 BGB — Basiszinssatz; § 288 BGB — Verzugszinsen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 3. `mandat-triage-mietrecht`

**Fokus:** Strukturierte Eingangs-Abfrage für mietrechtliche Mandate. Klaert Mandantenrolle (Vermieter Mieter WEG-Eigentuemer Verwalter) Gegenstandsart (Wohnraum Gewerbe WEG) Sachgebiet (Kündigung Mieterhoehung Mietminderung Modernisierung Nebenkostenabrechnung Mietkaution-Rückforderung Eigenbedarf Sanierung Räumung WEG-Beschluss WEG-Hausgeld-Klage). Fristen-Sofort-Check Kündigungs-Frist nach § 573c BGB Räumungs-Frist § 721 ZPO WEG-Klage ein Monat § 45 WEG Modernisierung-Ankündigung drei Monate vorher Mieterhoehung Zustimmungs-Frist zwei Monate § 558b BGB. Eskalation Telefon-Sofort bei Räumungstermin laufender Kündigungs-Frist.

# Mandat-Triage Mietrecht

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandat-Triage Mietrecht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Mietrechts-Mandate sind heterogen — Wohnraummietrecht (sozial geschützt) Gewerbemietrecht (vertragsdominiert) WEG (eigene Logik). Triage stellt richtige Spur sicher.

## Ablauf — sieben Fragen

### Frage 1 — Mandantenrolle?

- Vermieter (Privat / Wohnungsunternehmen)
- Mieter
- WEG-Eigentümer (in eigener Sache)
- WEG-Verwalter / Hausverwaltung
- Sondereigentums-Verwalter
- Untermieter

### Frage 2 — Gegenstandsart?

- Wohnraum
- Gewerbe
- Garage / Stellplatz (separat oder im Mietvertrag enthalten)
- WEG (Sondereigentum + Gemeinschaftseigentum)
- Pacht
- Mischmietvertrag

### Frage 3 — Sachgebiet?

- **Kündigung** (ordentlich außerordentlich Eigenbedarf Zahlungsverzug)
- Räumung
- **Mieterhöhung** (Vergleichsmiete Modernisierung)
- **Überhöhte Ausgangsmiete / Mietwucher** (Mietpreisbremse, § 5 WiStrG 1954, § 291 StGB)
- **Mietminderung** (Mangel)
- Modernisierung
- **Nebenkostenabrechnung** (Erstellung Prüfung)
- **Mietkaution** Rückforderung
- **Schönheitsreparaturen** Anspruch
- Mietmangel-Anspruch
- WEG-Beschluss-Anfechtung
- WEG-Hausgeld-Klage / Forderung
- Räumungsfrist
- Anschlussraum (Garage Stellplatz)
- Untermiete

### Frage 4 — Akute Eilbedürftigkeit?

- **Räumungstermin** binnen Tagen — Räumungsschutz
- **Kündigung gestern erhalten** Klage-Frist nach Vorbemerkung
- **Eigenbedarfsräumung droht** Räumungsklage zugestellt
- **Modernisierung morgen** unzumutbar
- **Mietminderungs-Stopp** Vermieter klagt Mietrückstand
- **Schimmelbefall lebensbedrohlich**
- **WEG-Beschluss-Anfechtung** ein-Monats-Frist

### Frage 5 — Vertragsbasis?

- Schriftlicher Mietvertrag (Datum)
- Mündlicher Mietvertrag
- Wohnraum-Mietvertrag mit gestaffelten Mieten / Indexmiete
- Gewerbemietvertrag
- WEG-Gemeinschaftsordnung
- Teilungserklärung

### Frage 6 — Frist?

- **Kündigungs-Frist Vermieter** § 573c BGB drei Monate (bei langer Mietdauer länger)
- **Kündigungs-Frist Mieter** drei Monate (nicht abhängig von Mietdauer)
- **Räumungsfrist Vollstreckung** § 721 ZPO Gewährung
- **Mieterhöhungs-Zustimmungsfrist § 558b BGB** zwei Monate
- **Mietminderungs-Anzeige** § 536c BGB unverzüglich
- **Betriebskostenabrechnung** § 556 Abs. 3 BGB zwölf Monate
- **WEG-Beschluss-Anfechtung** § 45 WEG ein Monat

### Frage 7 — Wirtschaftliche Verhältnisse?

- Miete-Volumen
- Eigenkapital (Mietkaution Selbstbeteiligung)
- Rechtsschutz Mieter Vermieter
- PKH bei Mieter

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Eigenbedarfskündigung erstellen | `eigenbedarfskuendigung-erstellen` |
| Mieterhöhung — Vermieter | `mieterhoehungsverlangen-erstellen` |
| Mieterhöhung — Mieter | `mieterhoehung-pruefen-widersprechen` |
| Mietsenkungsverlangen | `mietsenkungsverlangen` |
| Mietpreisüberhöhung / Mietwucher | `mietpreisueberhoehung-wistrg-1954-mietwucher` |
| Nebenkosten erstellen | `nebenkostenabrechnung-erstellen` |
| Nebenkosten prüfen | `nebenkostenabrechnung-pruefen` |
| Klage am AG | `klageentwurf-amtsgericht` |
| Mahnung Zahlungsverzug | `mahnung-zahlungsverzug-mieter` |
| Mieteranfragen beantworten | `mieteranfragen-beantworten` |
| Lage und Ausstattung erheben | `lage-und-ausstattung-erheben` |
| WEG-Beschluss-Anfechtung | `weg-beschluss-anfechten` |
| Mietkaution-Rückforderung | (Skill mietkaution-rueckforderung — perspektivisch) |
| Mietminderung wegen Mangel | (Skill mietminderung-prüfen — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** — keine Doppelmandate Mieter/Vermieter
- **Streitwert** Wohnraum Jahresmiete EUR (KSchG-Streitwert vergleichbar)
- **AG-Zuständigkeit** Mietrecht-Streit über Wohnraum § 23 Nr. 2 a) GVG ausschließlich AG
- **Versicherungs-Deckung** Mietrechtsschutz häufig

## Eskalation

- **Telefon-Sofort** Räumungstermin Räumungsklage Schimmel
- **Binnen einer Stunde** WEG-Beschluss-Anfechtung Frist läuft heute
- **Heute** Kündigungs-Widerspruch Mieterhöhungs-Antwort
- **Diese Woche** Klageschrift Räumungsschutz

## Ausgabe

- `triage-protokoll-mietrecht.md`
- Aktenanlage
- Frist im Fristenbuch
- Mandatsvereinbarung mit Honorar
- Empfehlung Folge-Skill

## Quellen

- BGB §§ 535 ff. 558 558b 573c 556
- WEG §§ 14 19 20 44 45
- ZPO § 721 (Räumungsfrist)
- BGH VIII. Zivilsenat und V. Zivilsenat nur mit Datum, Aktenzeichen und frei prüfbarer Quelle

## Aktuelle Rechtsprechung — Leitsaetze (Triage-Relevant)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
