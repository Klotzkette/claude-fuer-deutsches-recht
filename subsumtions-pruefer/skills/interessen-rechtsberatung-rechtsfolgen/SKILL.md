---
name: interessen-rechtsberatung-rechtsfolgen
description: "Interessen Rechtsberatung Rechtsfolgen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Interessen Rechtsberatung Rechtsfolgen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Interessen Rechtsberatung Rechtsfolgen** im Plugin Subsumtions-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-pruefen-mehrparteien-konflikt-und-interessen` | Pruefen: Mehrparteienkonflikt und Interessenmatrix im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-rechtsberatung-internationaler-bezug-und-schnittstellen` | Rechtsberatung: Internationaler Bezug und Schnittstellen im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-rechtsfolgen-zahlen-schwellen-und-berechnung` | Rechtsfolgen: Zahlen, Schwellenwerte und Berechnung im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Subsumtions-Prüfer gilt für **Interessen Rechtsberatung Rechtsfolgen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-pruefen-mehrparteien-konflikt-und-interessen`

**Fokus:** Pruefen: Mehrparteienkonflikt und Interessenmatrix im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Mehrparteienkonflikt und Interessenmatrix

## Aufgabe

Dieser Skill strukturiert Sachverhalte mit mehr als zwei Parteien oder mehreren widerstreitenden Interessen. Er erstellt eine Interessenmatrix und prüft Ansprüche, Einreden und Risiken für jede Partei getrennt.

## Warum Mehrparteien besonders anspruchsvoll?

- Unterschiedliche Anspruchsgrundlagen für jede Partei
- Beweislast je Partei separat zu beurteilen
- Kollusionsgefahr zwischen Parteien (z. B. Gesamtschuldner §§ 421 ff. BGB)
- Mögliche Interessenkonflikte für den beratenden Anwalt (§ 43a Abs. 4 BRAO)
- Prozesstaktik: Wer wird zuerst verklagt? Streitverkündung? Beiladung?

## Schritt 1 — Parteienidentifikation

Alle Beteiligten auflisten:
- Hauptparteien (Kläger, Beklagte)
- Nebenintervenientenpotenzial (§§ 66–77 ZPO)
- Streitverkündete (§§ 72–77 ZPO)
- Mögliche Gesamtschuldner oder Gesamtgläubiger (§§ 421 ff. BGB)
- Dritte mit möglichen eigenen Ansprüchen (z. B. § 328 BGB, echter Vertrag zugunsten Dritter)

## Schritt 2 — Interessenmatrix erstellen

| Partei | Interesse | Anspruchsgrundlage / Einrede | Beweislage | Risiko |
|---|---|---|---|---|
| A | Zahlung von X | § 433 Abs. 2 BGB | Vertrag vorhanden; Zahlung streitig | Mittel |
| B | Abwehr; Mängel | § 437 BGB; § 320 BGB | Mängelbeleg fehlt | Hoch |
| C | Regress gegen B | § 426 BGB (Gesamtschuldner) | Innenausgleich unklar | Niedrig |

## Schritt 3 — Anspruchskette prüfen

Bei mehrstöckigen Sachverhalten (z. B. Haupt- und Subunternehmer, Konzerngesellschaften):
- Welche Partei hat einen Anspruch gegen welche andere?
- Ist Drittschadensliquidation relevant?
- Durchgriffshaftung (§§ 826 BGB, faktisches Konzernrecht)?
- AEUV Art. 101 / 102 bei vertikalen Vertragsketten?

## Schritt 4 — Prozesstaktik und Verfahrensstruktur

- **Streitverkündung § 72 ZPO:** Wenn Partei bei Unterliegen Regress nehmen möchte; Interventionswirkung § 68 ZPO
- **Nebenintervention § 66 ZPO:** Dritter hat rechtliches Interesse am Obsiegen einer Partei
- **Klagerweiterung § 264 ZPO:** Zusätzliche Beklagte einbeziehen?
- **Aufrechnung und Widerklage:** Gegenansprüche der Beklagten gegen Kläger (§ 387 BGB; §§ 145 ZPO)

## Interessenkonflikt-Check für Anwalt

- § 43a Abs. 4 BRAO: Verbot der Vertretung widerstreitender Interessen
- BRAO § 356: Parteiverrat (Strafrecht)
- Checkliste: Ist die fragende Person Anwalt einer bestimmten Partei? Gibt es Mandate auf der Gegenseite?

## Einstieg

Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer sind die Gegenüber (alle Parteien)?
2. Welches konkrete Ziel soll für welche Partei erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Interessenmatrix, Memo, Checkliste, Tabelle, Entwurf oder Schriftsatzbaustein?

## Arbeitsworkflow

1. **Fallbild bilden:** Alle Parteien, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand je Partei prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, Gegenargumente und Wertungsfragen je Partei trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot pro Partei mit Begründung, Annahmen und Alternativwegen.
5. **Anschluss bauen:** Passende weitere Skills vorschlagen.

## Output-Standard

- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Interessenmatrix:** Partei, Anspruch/Einrede, Norm, Beweislage, Risiko.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf markieren.

## Quellenregel

- Aktuelle Normen live prüfen: gesetze-im-internet.de (BGB §§ 421 ff., ZPO §§ 66 ff., 72 ff., BRAO).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine Blindzitate. Paywall-Literatur nur mit Nutzerquelle.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `spezial-rechtsberatung-internationaler-bezug-und-schnittstellen`

**Fokus:** Rechtsberatung: Internationaler Bezug und Schnittstellen im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Rechtsberatung: Internationaler Bezug und Schnittstellen

## Aufgabe

Dieser Skill strukturiert Sachverhalte mit internationalem Bezug: anwendbares Recht (IPR), internationale Zuständigkeit, Schnittstellen zwischen deutschem Recht, EU-Recht und Drittstaatenrecht sowie Anerkennungs- und Vollstreckungsfragen.

## Abgrenzung: Welches Recht gilt?

### Kollisionsrecht — Schritt für Schritt

**Schritt 1 — EU-Kollisionsrecht prüfen (Vorrang vor EGBGB)**

| Sachverhalt | Anwendbares Kollisionsrecht |
|---|---|
| Vertragliche Schuldverhältnisse | Rom I-VO (VO 593/2008) |
| Außervertragliche Schuldverhältnisse (Delikt, Bereicherung) | Rom II-VO (VO 864/2007) |
| Unterhalt | EuUntVO (VO 4/2009) |
| Erbrecht | EuErbVO (VO 650/2012) |
| Ehegüterrecht | EuGüVO (VO 2016/1103) |
| Insolvenz | EuInsVO (VO 2015/848) |

**Schritt 2 — EGBGB subsidiär**

Wenn kein EU-Kollisionsrecht greift: EGBGB (Art. 3 ff.) für Personen- und Familienrecht, Sachenrecht, ggf. Deliktsrecht außerhalb Rom II-VO.

### Anwendbares Recht nach Rom I-VO (Verträge)

- Freie Rechtswahl (Art. 3 Rom I-VO): Parteien können anwendbares Recht wählen; Grenzen: zwingendes Recht des Aufenthaltsstaates (Art. 6 Rom I-VO für Verbraucher)
- Ohne Rechtswahl (Art. 4 Rom I-VO): Recht des charakteristischen Leistungserbringers (z. B. Verkäufer, Dienstleister)
- Verbraucherverträge (Art. 6 Rom I-VO): Recht des gewöhnlichen Aufenthalts des Verbrauchers; zwingende Mindeststandards

## Internationale Zuständigkeit

### EuGVVO (VO 1215/2012) — innerhalb EU/EWR

- Allgemeiner Gerichtsstand: Wohnsitz des Beklagten (Art. 4)
- Besonderer Gerichtsstand Vertragserfüllung (Art. 7 Nr. 1): Erfüllungsort
- Verbraucherschutz (Art. 17–19): Verbraucher klagt am Wohnsitz
- Ausschließliche Zuständigkeit (Art. 24): Grundstücke, Gesellschaften, Register

### Drittstaaten (außerhalb EU)

- Brüssel I nicht anwendbar; nationale ZPO-Regeln (§§ 12 ff. ZPO) oder Staatsverträge
- Haager Übereinkommensrecht: HZÜ, HGÜ (Gerichtsstandsübereinkommen von 2005)
- Schiedsgerichtsbarkeit: New Yorker Übereinkommen 1958 (Vollstreckung ausländischer Schiedssprüche)

## Anerkennung und Vollstreckung ausländischer Urteile

### Innerhalb EU: EuGVVO
- Art. 36 ff. EuGVVO: Automatische Anerkennung; keine gesonderte Anerkennung nötig
- Art. 39 ff. EuGVVO: Vollstreckbarerklärung nach nationalem Recht

### Außerhalb EU
- §§ 328, 722, 723 ZPO: Anerkennung ausländischer Urteile; Verbürgung der Gegenseitigkeit; Ordre-public-Kontrolle
- Vollstreckungsklage (§ 722 ZPO) vor deutschem Gericht

## DSGVO-Schnittstellen (international)

- Art. 3 DSGVO: Anwendungsbereich bei Niederlassung in der EU oder Angebot/Monitoring von EU-Bürgern
- Art. 44 ff. DSGVO: Drittstaatenübermittlung; Angemessenheitsbeschluss, SCC (Standardvertragsklauseln)
- Live-Check: Aktuellen Angemessenheitsbeschluss für das Zielland prüfen (edpb.europa.eu; datenschutz.de)

## Einstieg

Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Staatsangehörigkeiten, Wohnsitze oder Niederlassungen der Parteien sind beteiligt?
2. Wo wurde der Vertrag abgeschlossen? Wo soll Leistung erbracht werden?
3. Gibt es eine Rechtswahlklausel oder Schiedsklausel?
4. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein oder Mandantenbrief?

## Arbeitsworkflow

1. **Fallbild bilden:** Parteien, Staatsangehörigkeiten, Wohnsitze, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Kollisionsrecht, Zuständigkeit, Fristen, Formfragen prüfen.
3. **Prüfpunkte abarbeiten:** Anwendbares Recht, Gerichtsstand, Vollstreckung, Drittstaatenproblematik trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und Alternativwegen.
5. **Anschluss bauen:** Passende weitere Skills vorschlagen (z. B. eu-vorabentscheidung-pruefen, spezial-europarecht-fristen-form-und-zustaendigkeit).

## Output-Standard

- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf markieren.

## Quellenregel

- EU-Kollisionsrecht live prüfen: eur-lex.europa.eu (Rom I, Rom II, EuGVVO, EuErbVO etc.).
- Nationale Normen: gesetze-im-internet.de (EGBGB, ZPO §§ 12 ff., 328, 722 f.).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine Blindzitate. Paywall-Literatur nur mit Nutzerquelle.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `spezial-rechtsfolgen-zahlen-schwellen-und-berechnung`

**Fokus:** Rechtsfolgen: Zahlen, Schwellenwerte und Berechnung im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Rechtsfolgen: Zahlen, Schwellenwerte und Berechnung

## Aufgabe

Dieser Skill quantifiziert die Rechtsfolgen einer Subsumtion: Schadensersatz, Vertragsstrafen, gesetzliche Zinsen, Bußgelder, Streitwert, RVG-Gebühren und sonstige geldwerte Rechtsfolgen. Er gibt Berechnungsschemata und Prüfpunkte für Zahlen, die live zu verifizieren sind.

## Wichtige Schwellenwerte und gesetzliche Beträge (Stand: Modellwissen; live prüfen)

| Bereich | Schwelle / Betrag | Norm | Quelle |
|---|---|---|---|
| Zuständigkeit AG / LG | bis EUR 5.000 AG; ab EUR 5.000 LG | §§ 23, 71 GVG | gesetze-im-internet.de |
| Berufungssumme | EUR 600 | § 511 Abs. 2 Nr. 1 ZPO | gesetze-im-internet.de |
| Kleinstunternehmer USt | EUR 22.000 (ab 2025: EUR 25.000) | § 19 UStG | live prüfen; gesetze-im-internet.de |
| DSGVO-Bußgeld max. | EUR 20 Mio. oder EUR 4% Jahresumsatz | Art. 83 Abs. 5 DSGVO | eur-lex.europa.eu |
| Verzugszins | Basiszinssatz + 5 PP (§ 288 Abs. 1 BGB); + 9 PP bei B2B (§ 288 Abs. 2 BGB) | §§ 288, 247 BGB | gesetze-im-internet.de; Bundesbank.de (Basiszinssatz) |
| Mietkaution max. | 3 Nettokaltmieten | § 551 BGB | gesetze-im-internet.de |
| Abfindung | Kein gesetzlicher Betrag; § 1a KSchG: 0,5 Monatsverdienst/Jahr | § 1a KSchG | live prüfen |
| Schmerzensgeld | Kein Schematismus; nach Billigkeitsgesichtspunkten | § 253 Abs. 2 BGB | BGH-Rechtsprechung live prüfen |

## Berechnungsschemata

### Schema 1 — Verzugszinsen

```
Hauptforderung: EUR X
Fälligkeit: TT.MM.JJJJ (bei Mahnung oder vertraglicher Bestimmung)
Verzugsbeginn: Mahnung (§ 286 Abs. 1 BGB) oder 30 Tage nach Fälligkeit (§ 286 Abs. 3 BGB)
Zinssatz: Basiszinssatz (Bundesbank.de, aktuell prüfen) + 5 PP (B2C) / + 9 PP (B2B)
Zinsen pro Tag: Hauptforderung × Zinssatz / 365
Gesamtzinsen: Zinsen pro Tag × Anzahl Tage Verzug
```

### Schema 2 — Schadensersatz § 249 BGB

```
Naturalrestitution (§ 249 Abs. 1 BGB): Zustand wie ohne schädigendes Ereignis
Differenzschaden: Vermögen mit schädigendem Ereignis vs. ohne
Positiver Schaden (damnum emergens): tatsächlich entstandene Kosten
Entgangener Gewinn (lucrum cessans): § 252 BGB; üblicher Gewinn oder wahrscheinliche Entwicklung
Abzug: Mitverschulden § 254 BGB; Vorteilsausgleichung
```

### Schema 3 — RVG-Gebühren (Anwalt; live prüfen)

```
Streitwert (§ 2 RVG) → Gebührentabelle (Anlage 2 RVG)
Geschäftsgebühr (Nr. 2300 RVG VV): 0,5–2,5; Regelgebühr 1,3
Verfahrensgebühr (Nr. 3100 RVG VV): 1,3
Terminsgebühr (Nr. 3104 RVG VV): 1,2
Einigungsgebühr (Nr. 1000, 1003 RVG VV): 1,5
Hinweis: RVG-Tabellen und Gebührensätze live prüfen unter gesetze-im-internet.de (RVG Anlage 2)
```

## Streitwertberechnung

- Leistungsklage: Streitwert = Klageforderung
- Feststellungsklage: Abschlag (BGH: ca. 20–80% des bezifferbaren Hauptanspruchs; live prüfen)
- Räumungsklage: Jahresmiete (§ 9 ZPO)
- Unterlassungsklage: Gesamtinteresse des Klägers; kein starrer Schematismus

## Einstieg

Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rechtsfolge soll berechnet werden (Schadensersatz, Zinsen, Bußgeld, Gebühren)?
2. Welche Zahlen und Daten liegen vor (Hauptforderung, Frist, Basiszinssatz)?
3. Gibt es behördliche Festsetzungen oder Schätzgrundlagen?
4. Welche Dokumente, Rechnungen oder Tabellen belegen die Zahlen?
5. Welcher Output wird gebraucht: Berechnung im Schriftsatz, Mandanteninfo, Tabelle?

## Arbeitsworkflow

1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Zahlen-Grundlage in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen für Rechtsfolge und Berechnung prüfen.
3. **Prüfpunkte abarbeiten:** Welche Beträge sind gesichert? Welche müssen live geprüft werden?
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen und Alternativwegen.
5. **Anschluss bauen:** Passende weitere Skills vorschlagen.

## Output-Standard

- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Berechnungstabelle:** Posten, Norm, Betrag, Annahme/Unsicherheit, Quelle.
- **Arbeitsprodukt:** Berechnungsschema für Schriftsatz oder Mandantenbrief.
- **Qualitätsgate:** keine Scheingenauigkeit; alle Zahlenwerte als Prüfpunkte markieren, wenn sie nicht live verifiziert sind.

## Quellenregel

- Aktuelle Beträge, Schwellenwerte und Gebührentabellen immer live prüfen: gesetze-im-internet.de, Bundesbank.de (Basiszinssatz), eur-lex.europa.eu (EU-Bußgelder).
- Rechtsprechung zu Schmerzensgeld und Schadensersatz nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle (dejure.org, bgh.de).
- Keine Blindzitate. Paywall-Literatur nur mit Nutzerquelle.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis, Frist oder Zahl nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
