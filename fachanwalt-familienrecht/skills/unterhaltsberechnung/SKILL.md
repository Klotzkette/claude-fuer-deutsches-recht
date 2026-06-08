---
name: unterhaltsberechnung
description: "Unterhaltsberechnung im Plugin Fachanwalt Familienrecht: prüft konkret Kindes- und Ehegattenunterhalt vollständig berechnen, Versorgungsausgleich im Scheidungsverbund durchführen, Zugewinnausgleich nach §§ 1372-1390 BGB berechnen, Familienrecht einfuehrend. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Unterhaltsberechnung

## Arbeitsbereich

**Unterhaltsberechnung** ordnet den Fall über die tragenden Prüfungslinien: Kindes- und Ehegattenunterhalt vollständig berechnen, Versorgungsausgleich im Scheidungsverbund durchführen, Zugewinnausgleich nach §§ 1372-1390 BGB berechnen. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `fachanwalt-familienrecht-unterhaltsberechnung` | Kindes- und Ehegattenunterhalt vollständig berechnen: Mandant trennt sich oder wurde getrennt und will Unterhaltshoehe festlegen. Normen: §§ 1601 ff. BGB (Kindesunterhalt), § 1361 BGB (Trennungsunterhalt), §§ 1569 ff. BGB (nachehelicher Unterhalt), § 1574 BGB (Erwerbsobliegenheit). Prüfraster: Bereinigtes Nettoeinkommen, Halbteilungsgrundsatz, Selbstbehalt, Mangelfall, fiktives Einkommen bei Obliegenheitsverletzung. Output Unterhalts-Berechnung mit Rechenschritten. Abgrenzung: Duesseldorfer-Tabelle Übersicht siehe unterhalt-duesseldorfer-tabelle; Versorgungsausgleich siehe fachanwalt-familienrecht-versorgungsausgleich. |
| `fachanwalt-familienrecht-versorgungsausgleich` | Versorgungsausgleich im Scheidungsverbund durchführen: Rentenanrechte aus Ehe aufteilen. Normen: VersAusglG (seit 2009), §§ 1 und 10 VersAusglG (Hin- und Herrechnung), § 17 VersAusglG (externe Teilung), § 18 VersAusglG (Geringfuegigkeit). Prüfraster: Anrechte (gesetzl. Rente, Riester, Ruerup, bAV, Beamtenversorgung), externe vs. interne Teilung, Ausgleichswert, Abweichungsvereinbarung. Output Versorgungsausgleichs-Berechnungs-Memo, Verfahrensstrategie. Abgrenzung: Scheidungsantrag siehe fachanwalt-familienrecht-scheidungsantrag-stellen; Zugewinnausgleich siehe fachanwalt-familienrecht-zugewinnausgleich-berechnen. |
| `fachanwalt-familienrecht-zugewinnausgleich-berechnen` | Zugewinnausgleich nach §§ 1372-1390 BGB berechnen: Trennung oder Scheidung erfordert Aufstellung von Anfangs- und Endvermögen. Normen: § 1373 BGB (Zugewinn), § 1374 BGB (Anfangsvermögen inkl. Privilegierungen Abs. 2), § 1376 BGB (Bewertungsstichtag Endvermögen), § 1379 BGB (Auskunftsanspruch), § 254 ZPO (Stufenklage). Prüfraster: Anfangsvermögen/Endvermögen, Erbschaft-/Schenkungsprivileg, negatives Anfangsvermögen seit 2009, Verfuegungsbeschraenkungen § 1365 BGB, Verjährung 3 Jahre. Output Berechnungs-Schema, Auskunftsstufe. Abgrenzung: Versorgungsausgleich siehe fachanwalt-familienrecht-versorgungsausgleich; Scheidungsantrag siehe fachanwalt-familienrecht-scheidungsantrag-stellen. |
| `famr-einfuehrung-themen` | Familienrecht einfuehrend: Ehe, Scheidung, Zugewinn, Versorgungsausgleich, Unterhalt (Trennungs-, Ehegatten-, Kindes-, Volljaehrigen-), Sorgerecht, Umgangsrecht, Vaterschaft, Adoption. Entscheidungstabelle für Mandantenanfragen und Verweis auf Detail-Skills. |
| `famr-kindeswohlgefaehrdung-eilantrag-spezial` | Spezialfall Kindeswohlgefaehrdung und Eilantrag: § 1666 BGB, Anordnungen Familiengericht, einstweilige Anordnung § 49 FamFG, Inobhutnahme Jugendamt § 42 SGB VIII. Pruefraster und Mustertexte für Eilantrag. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: FamFG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `fachanwalt-familienrecht-unterhaltsberechnung`

**Fokus:** Kindes- und Ehegattenunterhalt vollständig berechnen: Mandant trennt sich oder wurde getrennt und will Unterhaltshoehe festlegen. Normen: §§ 1601 ff. BGB (Kindesunterhalt), § 1361 BGB (Trennungsunterhalt), §§ 1569 ff. BGB (nachehelicher Unterhalt), § 1574 BGB (Erwerbsobliegenheit). Prüfraster: Bereinigtes Nettoeinkommen, Halbteilungsgrundsatz, Selbstbehalt, Mangelfall, fiktives Einkommen bei Obliegenheitsverletzung. Output Unterhalts-Berechnung mit Rechenschritten. Abgrenzung: Duesseldorfer-Tabelle Übersicht siehe unterhalt-duesseldorfer-tabelle; Versorgungsausgleich siehe fachanwalt-familienrecht-versorgungsausgleich.

# Unterhaltsberechnung

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Unterhaltsberechnung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Unterhaltsberechnung
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Aktuelle Rechtsprechung (verifiziert, Stand 05/2026)

- BGH, Beschluss vom 22.01.2025 - XII ZB 148/24: Bemessung des angemessenen Selbstbehalts des unterhaltspflichtigen Kindes beim Elternunterhalt; Familienselbstbehalt bei verheirateten Unterhaltspflichtigen (§ 1603 Abs. 1 BGB, § 94 Abs. 1a SGB XII). Quelle: bundesgerichtshof.de bzw. dejure.org vor Verwendung verifizieren.
- Düsseldorfer Tabelle 2026 in Kraft seit 01.01.2026 (Pressemitteilung OLG Düsseldorf vom 01.12.2025); Mindestunterhalt § 1612a BGB: EUR 486 / EUR 558 / EUR 653 (Altersstufen 1-3).
- Weitere Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesgerichtshof.de, dejure.org, openjur.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Kaltstart-Rückfragen

1. Welche Art von Unterhalt — Kindesunterhalt, Trennungsunterhalt (§ 1361 BGB) oder Nachehelicher Unterhalt (§§ 1569 ff. BGB)?
2. Wie ist die Einkommenssituation beider Beteiligter — Arbeitnehmer, Selbständig, Arbeitslos? Letzte 12 Monate Einkommen erforderlich, bei Selbständigen drei Jahre.
3. Wie viele Unterhaltsberechtigte und in welcher Rangfolge (§ 1609 BGB) — minderjährige Kinder, Mutter eines nichtehelichen Kindes, Ehegatte?
4. Trennungszeitpunkt, Rechtshängigkeit Scheidungsantrag, Rechtskraft Scheidung — Stichtage für Trennungs- bzw. Nachehelichen Unterhalt?
5. Liegt eine Ehe von kurzer Dauer (§ 1579 Nr. 1 BGB) oder Verwirkungstatbestand (§ 1579 BGB) vor?

## Anspruchsgrundlagen

| Unterhaltsart | Anspruchsgrundlage | Besonderheiten |
|---|---|---|
| Kindesunterhalt minderjährig | §§ 1601, 1612a BGB Düsseldorfer Tabelle | Privilegierter Mindestunterhalt § 1612a BGB |
| Volljährigenunterhalt | §§ 1601, 1610 BGB | Bedürftigkeitsprüfung Ausbildung |
| Trennungsunterhalt | § 1361 BGB | Bis Rechtskraft Scheidung |
| Betreuungsunterhalt nach Scheidung | § 1570 BGB | Mindestens bis 3. Lebensjahr Kind |
| Aufstockungsunterhalt | § 1573 Abs. 2 BGB | Differenz zum eheangepassten Lebensbedarf |
| Krankheitsunterhalt | § 1572 BGB | Krankheitsbedingt erwerbsunfähig |

- Bereinigtes Nettoeinkommen: Brutto − Steuern − Sozialabgaben − berufsbedingte Aufwendungen (5 % pauschal, mindestens 50 EUR höchstens 150 EUR — st. Rspr.) − Vorsorgeaufwendungen (bis 4 % Bruttoeinkommen Altersvorsorge).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Erwerbsobliegenheit § 1574 BGB — fiktives Einkommen bei vorwerfbarer Untätigkeit.
- Selbstbehalt nach Duesseldorfer Tabelle Anmerkung A — die konkreten Sätze (notwendiger Selbstbehalt gegenüber minderjaehrigen Kindern, angemessener Selbstbehalt gegenüber Ehegatten und volljaehrigen Kindern) werden in der Duesseldorfer Tabelle jaehrlich neu festgelegt; immer aktuelle Fassung des laufenden Jahres heranziehen, z.B. über OLG Duesseldorf Pressestelle oder unterhalt.net.
- Rangfolge § 1609 BGB: 1. minderjährige unverheiratete Kinder + privilegierte Volljährige, 2. Elternteile betreuender Kinder, 3. Ehegatten ab Ehe über kurze Zeit, 4. nicht privilegierte Volljährige, 5. andere Verwandte.
- Bei Mangelfall (Einkommen reicht nicht für alle Berechtigten): Mangelverteilung nach Quoten innerhalb desselben Rangs.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Beweislast

- Unterhaltsberechtigter trägt Beweislast für Bedürftigkeit und Anspruchsvoraussetzungen.
- Unterhaltspflichtiger trägt Beweislast für Leistungsfähigkeit und für negative Anspruchsvoraussetzungen (Verwirkung § 1579 BGB).
- Auskunftsanspruch nach § 1605 BGB — wechselseitig alle zwei Jahre, mit Belegen Steuerbescheid Gehaltsnachweise.

## Berechnungsschema Kindesunterhalt

```
1. Bruttoeinkommen des Barunterhaltspflichtigen letzte 12 Monate
2. - Steuern - SV-Beitraege - berufsbedingte Aufwendungen 5 %
3. = bereinigtes Nettoeinkommen
4. Einkommensgruppe aus Duesseldorfer Tabelle ablesen
5. Tabellenwert nach Altersstufe (0-5 / 6-11 / 12-17 / volljaehrig)
6. - haelftiges Kindergeld bei minderjaehrigen § 1612b BGB
7. = Zahlbetrag
```

## Schreibvorlage Auskunftsanforderung § 1605 BGB

```
Sehr geehrte Frau Kollegin sehr geehrter Herr Kollege

namens und in Vollmacht unseres Mandanten fordern wir Ihren Mandanten
auf binnen vier Wochen Auskunft nach § 1605 BGB ueber seine
Einkommens- und Vermoegensverhaeltnisse zu erteilen mit Belegen

1. Einkommensteuerbescheide letzte drei Jahre
2. Gehaltsabrechnungen letzte 12 Monate
3. bei Selbstaendigkeit BWA der letzten drei Jahre
4. Aufstellung der Vermoegenswerte und Verbindlichkeiten

Andernfalls werden wir Stufenklage § 254 ZPO erheben.

Mit kollegialen Gruessen
```

## Übergabe

- Bei Verweigerung Auskunft: Stufenklage Familiengericht; Unterhaltssache § 231 FamFG; oertliche Zuständigkeit § 232 FamFG; sachliche Zuständigkeit §§ 23a Abs. 1 Nr. 1, 23b GVG.
- Bei einstweiligem Regelungsbedarf einstweilige Anordnung § 246 FamFG (Trennungsunterhalt).
- Bei Verfahrenskostenhilfe Anlage § 117 ZPO ausfüllen.
- Anschluss bei Trennung: Skill `fachanwalt-familienrecht-scheidungsantrag-stellen`.

## 2. `fachanwalt-familienrecht-versorgungsausgleich`

**Fokus:** Versorgungsausgleich im Scheidungsverbund durchführen: Rentenanrechte aus Ehe aufteilen. Normen: VersAusglG (seit 2009), §§ 1 und 10 VersAusglG (Hin- und Herrechnung), § 17 VersAusglG (externe Teilung), § 18 VersAusglG (Geringfuegigkeit). Prüfraster: Anrechte (gesetzl. Rente, Riester, Ruerup, bAV, Beamtenversorgung), externe vs. interne Teilung, Ausgleichswert, Abweichungsvereinbarung. Output Versorgungsausgleichs-Berechnungs-Memo, Verfahrensstrategie. Abgrenzung: Scheidungsantrag siehe fachanwalt-familienrecht-scheidungsantrag-stellen; Zugewinnausgleich siehe fachanwalt-familienrecht-zugewinnausgleich-berechnen.

# Versorgungsausgleich

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Versorgungsausgleich` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Versorgungsausgleich
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Zweck

Bei Scheidung: Hin- und Herteilung der während der Ehezeit erworbenen Versorgungs-Anrechte. Standard im Scheidungsverbund.

## 1) Eingangs-Abfrage

1. Ehezeit (Eheschliessung bis Rechtshaengigkeit Scheidung)?
2. Beide Eheleute Versorgungs-Anrechte (DRV, betriebliche, private)?
3. Beamten-Status?
4. Eheschliessung im Ausland?
5. Ausgleichs-Anspruch Verzicht in Ehevertrag?
6. Höhe Anrechte (Renten-Punkte)?

## 2) Rechtsgrundlagen

- **VersAusglG 2009** (Versorgungsausgleichsgesetz seit 1.9.2009)
- Vorher: Splitting / Quasi-Splitting -> heute Halbteilung
- **§ 1 VersAusglG**: Pflicht zur Halbteilung
- **§ 6 VersAusglG**: Vertragliche Modifikationen (Ehevertrag)
- **§ 27 VersAusglG**: Härteklausel

## 3) Ehezeit-Begriff § 3 VersAusglG

- **Beginn**: 1. des Monats der Eheschliessung
- **Ende**: letzter Tag des Monats der Rechtshaengigkeit Scheidung
- Beispiel: Ehe 12.5.2010, Scheidung rechtshaengig 7.3.2025
- Ehezeit: 1.5.2010 - 31.2.2025

## 4) Anrechte-Arten

### Gesetzliche Rentenversicherung

- Auskunft DRV mit Renten-Punkten
- Halbteilung der während Ehezeit erworbenen Punkte

### Beamten-Versorgung

- Berechnung nach BeamtVG
- Quasi-interne Teilung

### Betriebliche Altersversorgung

- Direktzusage: typisch interne Teilung
- Pensionskasse / Pensionsfonds: extern möglich
- Direktversicherung: typisch externe Teilung

### Private Renten (Riester, Ruerup, klassische LV)

- Auskunft Versicherer
- Interne oder externe Teilung

## 5) Interne vs. externe Teilung

### Interne Teilung § 10 VersAusglG

- Im selben Versorgungs-System
- Ausgleichs-Berechtigter erhaelt eigenen Anspruch
- Standardform

### Externe Teilung § 14 VersAusglG

- Bei kleinem Wert (< 84 EUR/Monat Rente, Stand 2024)
- Auf Antrag des Versorgungs-Trägers
- Ausgleichswert wird in Ziel-Versorgung übertragen (DRV oder eigene Wahl)
- BGH-Linie 2020 zur Verzinsung bei externer Teilung

## 6) Berechnung

### Ausgleichswert

- Pro Anrecht: Halftung des während Ehezeit erworbenen Wertes
- Korrespondierender Kapitalwert nach Bewertungsregeln

### Mehrwert-Faktor

- Bei externer Teilung: Verzinsung des Ausgleichswerts
- Korrigiert Inflations-Verluste

## 7) Verzicht / Modifikation

### Ehevertrag § 6 VersAusglG

- Notarielle Form
- Kontrolle § 138 BGB (Sittenwidrigkeit)
- BGH-Linie zur Wirksamkeitsprüfung bei Inkompetenz / Druck

### Härteklausel § 27 VersAusglG

- Grobe Unbilligkeit bei kurzer Ehe (< 3 Jahre)
- Bei wesentlicher Wert-Disproportion
- Bei Mitschuldigkeit

## 8) Workflow

### Phase 1 — Auskunfts-Verfahren

- FamG fordert von beiden Eheleuten Versorgungs-Auskunft
- Eheleute reichen Formular V10 ein
- Versorgungs-Träger antwortet binnen 3-6 Monaten

### Phase 2 — Berechnung

- FamG erstellt VA-Beschluss-Entwurf
- Beide Anwälte überprüfen Auskuenfte
- Bei Streit: Sachverständiger

### Phase 3 — Beschluss

- FamG beschließt Aufteilung
- Im Scheidungsverbund Teil des Endbeschlusses

### Phase 4 — Vollzug

- Mitteilung an Versorgungs-Träger
- Eintragung der Anrechte beim Ausgleichs-Berechtigten

## 9) Anwalts-Strategie

### Bei vermeintlich kurzem Ehe-Verlauf

- Prüfen ob VA-Ausschluss durch § 27 sinnvoll
- Bei höheren Anrechten: VA-Ausschluss bringt Verlust

### Bei selbstständigem Mandanten

- Versicherungs-Verträge identifizieren
- Bei DRV: minimale Anrechte ggf. nicht ausgleichs-relevant

### Bei Auslandsbezug

- Versorgungen aus EU oder Drittstaaten
- Bei EU: VO (EU) 883/2004 Sozialversicherungs-Abkommen

## 10) Typische Fehler

1. **Versorgungs-Auskunft übersehen** -> falsche Berechnung
2. **Ehezeit falsch berechnet** -> Falschberechnung
3. **Interne vs. externe Teilung nicht optimiert** -> wirtschaftlicher Verlust
4. **Härte-Antrag § 27 versäumt** -> ungewollte Aufteilung
5. **Ehevertrag-Prüfung übersprungen** -> § 138 BGB-Streit später

## 11) BGH-Linien

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anschluss

- `fachanwalt-familienrecht-duesseldorfer-tabelle-unterhalt` — bei Unterhalts-Frage
- `fachanwalt-familienrecht-kindeswohlgefaehrdung-eilantrag` — bei Konflikt
- `bav-strategie-konzern` — bei komplexer betrieblicher AV

<!-- AUDIT 27.05.2026 | Bundle 022 | Task 2
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Status: WRONG_TOPIC
Kindesunterhalt und Immobilienfinanzierung (Tilgungsraten bis Wohnwert berücksichtigbar,
§ 1603 Abs. 2 BGB) – nicht den Mehrwert-Faktor im Versorgungsausgleich.
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Maßnahme: Zeile aus BGH-Linien (Abschnitt 11) gelöscht.
-->

## 3. `fachanwalt-familienrecht-zugewinnausgleich-berechnen`

**Fokus:** Zugewinnausgleich nach §§ 1372-1390 BGB berechnen: Trennung oder Scheidung erfordert Aufstellung von Anfangs- und Endvermögen. Normen: § 1373 BGB (Zugewinn), § 1374 BGB (Anfangsvermögen inkl. Privilegierungen Abs. 2), § 1376 BGB (Bewertungsstichtag Endvermögen), § 1379 BGB (Auskunftsanspruch), § 254 ZPO (Stufenklage). Prüfraster: Anfangsvermögen/Endvermögen, Erbschaft-/Schenkungsprivileg, negatives Anfangsvermögen seit 2009, Verfuegungsbeschraenkungen § 1365 BGB, Verjährung 3 Jahre. Output Berechnungs-Schema, Auskunftsstufe. Abgrenzung: Versorgungsausgleich siehe fachanwalt-familienrecht-versorgungsausgleich; Scheidungsantrag siehe fachanwalt-familienrecht-scheidungsantrag-stellen.

# Zugewinnausgleich berechnen

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zugewinnausgleich berechnen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Zugewinnausgleich berechnen
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Kaltstart-Rückfragen

1. Wann wurde die Ehe geschlossen, wann wurde Trennung erklärt, wann Zustellung des Scheidungsantrags (Stichtag § 1384 BGB für Endvermögen)?
2. Welchen Güterstand hatten die Eheleute — gesetzlicher Güterstand der Zugewinngemeinschaft oder ehevertraglich modifiziert?
3. Welches Vermögen hatte jeder Ehegatte bei Eheschließung (Anfangsvermögen § 1374 BGB) — Belege, Bewertungen?
4. Welches Vermögen besteht zum Stichtag (Konten, Immobilien, Unternehmen, Lebensversicherungen, Kfz, Schulden)?
5. Gab es Erbschaften, Schenkungen, Schmerzensgeld während der Ehe? Diese sind privilegiert (§ 1374 Abs. 2 BGB) und werden dem Anfangsvermögen hinzugerechnet.

## Anspruchsgrundlagen und Berechnung

- Gesetzlicher Güterstand: Zugewinngemeinschaft (§ 1363 BGB), Vermögensmassen bleiben getrennt, Ausgleich erst bei Beendigung.
- Beendigung durch Tod, Scheidung oder Vereinbarung; Ausgleichsforderung als Geldanspruch (§ 1378 Abs. 1 BGB).
- Anfangsvermögen (§ 1374 BGB) = Aktiva − Passiva bei Eheschließung; Erbschaften, Schenkungen, Ausstattung nach § 1374 Abs. 2 BGB werden hinzugerechnet (privilegierter Erwerb).
- Endvermögen (§ 1375 BGB) = Aktiva − Passiva am Stichtag § 1384 BGB (Rechtshängigkeit des Scheidungsantrags). Illoyale Vermögensminderungen werden hinzugerechnet (§ 1375 Abs. 2 BGB).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Zugewinn = Endvermögen − Anfangsvermögen (nicht negativ — § 1373 BGB).
- Ausgleichsforderung = (Zugewinn des Höhergewinnenden − Zugewinn des Wenigergewinnenden) ÷ 2 (§ 1378 Abs. 1 BGB).
- Begrenzung: Ausgleichsforderung wird durch Vermögen des Schuldners am Stichtag begrenzt (§ 1378 Abs. 2 BGB).
- Auskunftsanspruch zu drei Stichtagen Trennung, Beendigung und ergänzend Anfangsvermögen (§ 1379 BGB seit 2009) — Stufenklage § 254 ZPO.
- Verjährung Ausgleichsforderung: drei Jahre § 195 BGB ab Kenntnis der Beendigung des Güterstands (§ 199 BGB).

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Beweislast

- Jeder Ehegatte trägt Beweislast für sein Anfangsvermögen und für anspruchsmindernde Tatsachen.
- Vermutung gegen Anfangsvermögen widerlegbar (§ 1377 Abs. 3 BGB): Wenn kein Verzeichnis erstellt wurde gilt das Endvermögen als Zugewinn — Vermutung kann widerlegt werden.
- Illoyale Vermögensminderungen § 1375 Abs. 2 BGB: Beweislast trägt der Ausgleichsberechtigte (Schenkung ohne Anstandspflicht, Vermögensvergeudung, Benachteiligung).

## Berechnungsschema

```
 Ehegatte A Ehegatte B
Endvermoegen (Stichtag § 1384) X1 X2
+ illoyale Minderungen § 1375 +a1 +a2
- Schulden -b1 -b2
= Endvermoegen bereinigt E_A E_B

Anfangsvermoegen indexiert Y1 Y2
+ privilegierter Erwerb § 1374 +p1 +p2
= Anfangsvermoegen bereinigt A_A A_B

Zugewinn = max(E - A; 0) Z_A Z_B

Ausgleichsforderung = (Z_max - Z_min) / 2
Schuldner ist der Ehegatte mit groesserem Zugewinn
```

## Schreibvorlage Auskunftsanforderung § 1379 BGB

```
Sehr geehrte Frau Kollegin sehr geehrter Herr Kollege

namens und in Vollmacht unserer Mandantin fordern wir Ihren Mandanten
auf binnen vier Wochen Auskunft ueber sein Vermoegen § 1379 BGB zu
erteilen und zwar zu folgenden Stichtagen
1. Trennung [Datum]
2. Anfangsvermoegen Eheschliessung [Datum]
3. Endvermoegen Rechtshaengigkeit Scheidungsantrag [Datum]

Die Auskunft hat saemtliche Aktiva und Passiva mit Belegen zu
enthalten Konten Immobilien Beteiligungen Lebensversicherungen
Kfz Schmuck Kunst. Auf Verlangen ist eidesstattliche Versicherung
nach § 260 Abs. 2 BGB abzugeben.

Andernfalls werden wir Stufenklage § 254 ZPO erheben.

Mit kollegialen Gruessen
```

## Übergabe

- Bei Verweigerung: Stufenklage Auskunft + eidesstattliche Versicherung + Zahlung beim Familiengericht (Gueterrechtssache § 261 FamFG; Zuständigkeit § 262 FamFG i.V.m. §§ 23a, 23b GVG).
- Bei Auslandsvermögen Auskunftsanspruch erstreckt sich auch auf ausländisches Vermögen.
- Bei Unternehmenswerten Sachverständigengutachten zur Bewertung notwendig — Kosten regelmäßig vorzustrecken.
- Anschluss: Skill `fachanwalt-familienrecht-scheidungsantrag-stellen` bei Verbund nach § 137 FamFG.

## 4. `famr-einfuehrung-themen`

**Fokus:** Familienrecht einfuehrend: Ehe, Scheidung, Zugewinn, Versorgungsausgleich, Unterhalt (Trennungs-, Ehegatten-, Kindes-, Volljaehrigen-), Sorgerecht, Umgangsrecht, Vaterschaft, Adoption. Entscheidungstabelle für Mandantenanfragen und Verweis auf Detail-Skills.

# Familienrecht: Themen-Map

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Familienrecht: Themen-Map` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: Familienrecht: Themen-Map
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zuständige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behördenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 5. `famr-kindeswohlgefaehrdung-eilantrag-spezial`

**Fokus:** Spezialfall Kindeswohlgefaehrdung und Eilantrag: § 1666 BGB, Anordnungen Familiengericht, einstweilige Anordnung § 49 FamFG, Inobhutnahme Jugendamt § 42 SGB VIII. Pruefraster und Mustertexte für Eilantrag.

# FamR: Kindeswohl-Eilantrag

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `FamR: Kindeswohl-Eilantrag` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: FamR: Kindeswohl-Eilantrag
- **Normen-/Quellenanker:** BGB, FamFG, SGB, VIII.

## Fallweichen
Frage zu Beginn nur ab, was für den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, für wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz für eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
