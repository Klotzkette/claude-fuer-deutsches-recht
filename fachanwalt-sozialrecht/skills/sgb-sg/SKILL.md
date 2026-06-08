---
name: sgb-sg
description: "SGB SG im Plugin Fachanwalt Sozialrecht: prüft konkrete Prüfungslinie für fachanwalt sozialrecht sgb ii bescheid, Vergleich vor Sozialgericht § 101 SGG, Mandant hat Sozialleistungsbescheid erhalten und Anwalt, Mandant benoetigt Hilfsmittel (Rollstuhl Hoerhilfe Prothese. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# SGB SG

## Arbeitsbereich

**SGB SG** ordnet den Fall über die tragenden Prüfungslinien: Prüfungslinie für fachanwalt sozialrecht sgb ii bescheid, Vergleich vor Sozialgericht § 101 SGG, Mandant hat Sozialleistungsbescheid erhalten und Anwalt. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `fachanwalt-sozialrecht-sgb-ii-bescheid` | Prüfungslinie für fachanwalt sozialrecht sgb ii bescheid: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `fachanwalt-sozialrecht-vergleich-sg-widerspruchsverhandlung` | Vergleich vor Sozialgericht § 101 SGG. Widerspruchsverhandlung Behörde § 84 SGG. Mediation in Sozialleistungs-Streit zunehmend. Anhörung GdB-Verfahren Vergleich Schwerbehinderung. Korrespondenz Behörde Klagebegründung Vergleichsbereitschaft Gericht. |
| `fachanwalt-sozialrecht-widerspruch-sozialleistung` | Mandant hat Sozialleistungsbescheid erhalten und Anwalt formuliert Widerspruch. § 84 SGG Widerspruchsfrist ein Monat. Prüfraster: Frist (Bekanntgabe Vier-Tage-Fiktion § 37 Abs. 2 SGB X seit 1.1.2025 PostModG) aufschiebende Wirkung § 86a SGG Antrag § 86b SGG Tatsachen und Rechtsgrundlagen Beweisangebote. Output: Widerspruchsschriftsatz mit Begründung. Abgrenzung zu bescheid-frist-quick-check (Fristkontrolle vorab) und klage-sozialgericht (nach Widerspruchsbescheid). |
| `hilfsmittelantrag-pruefen` | Mandant benoetigt Hilfsmittel (Rollstuhl Hoerhilfe Prothese Pflegebett Treppenlift) und fragt welcher Kostentraeger zuständig ist und wie Antrag und Widerspruch aussehen. § 33 SGB V Hilfsmittelverzeichnis § 139 SGB V § 40 SGB XI § 47 SGB IX. Prüfraster: Zuständigkeit Krankenkasse/Pflegekasse/Eingliederungstraeger/Sozialhilfe Festbetraege Mehrkostenregelung typische Ablehnungsgründe. Output: Antragsentwurf oder Widerspruchsentwurf Hilfsmittel. Abgrenzung zu eingliederungshilfe-schule (Schule) und pflegegrad-widerspruch (Pflegegrad). |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGG §§ 51, 78, 87, 90, 130a, 144, 160, 183, 193, SGB I, II, III, V, VI, IX, X; § 11. SGB I-XII und Sozialgerichtsbarkeit SGG. Widerspruch; § 84 SGG Klage; § 87 SGG Eilantrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `fachanwalt-sozialrecht-sgb-ii-bescheid`

**Fokus:** Prüfungslinie für fachanwalt sozialrecht sgb ii bescheid: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

### SGB-II-Bescheid (Bürgergeld)

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `SGB-II-Bescheid (Bürgergeld)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage — kläre vor SGB-II-Bearbeitung
1. Welcher Bescheid genau (Bewilligungs-, Aufhebungs-, Erstattungsbescheid)? § 40 SGB II i.V.m. §§ 45, 48 SGB X: Unterschied materiell-rechtlich entscheidend.
2. Widerspruchsfrist 1 Monat ab Bekanntgabe (§ 84 SGG) — noch offen? Bei abgelaufenem Bescheid: § 44 SGB X-Überprüfungsantrag.
3. Aufschiebende Wirkung: SGB-II-Bescheide haben grundsätzlich KEINE aufschiebende Wirkung (§ 39 SGB II) — Eilantrag § 86b SGG notwendig wenn laufende Versorgung gefährdet.
4. Hat der Bescheid eine ordnungsgemäße Anhörung nach § 24 SGB X durchlaufen? Bei Aufhebung/Erstattung pruefen. BSG-Linie B 7 AS / B 4 AS — vor Ausgabe Aktenzeichen live in dejure.org pruefen.
5. Ist Mandant im Karenzjahr (§ 12 Abs. 3 SGB II)? Dann erweiterte Vermögensschonung.

## Aktuelle Rechtsprechung (Stand Mai 2026)

- BSG, Urteil vom 02.12.2025 — B 7 AS 20/24 R (verbunden mit B 7 AS 30/24 R und B 7 AS 6/25 R): Die Regelbedarfe für 2022 sind nicht verfassungswidrig zu niedrig festgesetzt; keine Verletzung des Grundrechts auf Gewährleistung eines menschenwürdigen Existenzminimums. Die Einmalzahlung von 200 Euro im Juli 2022 hat den durch den Ukraine-Krieg ausgelösten Kaufkraftverlust hinreichend kompensiert. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BSG&Datum=02.12.2025&Aktenzeichen=B+7+AS+20/24+R sowie Pressemitteilung Nr. 30/2025: https://www.bsg.bund.de/SharedDocs/Pressemitteilungen/DE/2025/2025_30.html
- BSG, Urteil vom 12.03.2025 — B 7 AS 5/24 R: Abgeschlossene Ausbildung mit Bewilligung von BAföG-Leistungen schließt den Leistungsausschluss nach SGB II nicht zwingend aus. Offene Fundstelle: https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2025/2025_03_12_B_07_AS_05_24_R.html
- BSG, Urteil vom 26.03.2025 — B 4 AS 4/24 R: Bundeserstattung an Kommunen für SGB-II-Verwaltungskosten nach § 6b SGB II. Offene Fundstelle: https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2025/2025_03_26_B_04_AS_04_24_R.html
- BSG, Urteil vom 04.06.2025 — B 7 AS 17/24 R: Vollstreckung von Erstattungsforderungen durch BA im SGB II. Offene Fundstelle: https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2025/2025_06_04_B_07_AS_17_24_R.html
- BSG, Urteil vom 16.07.2025 — B 7 AS 19/24 R: Durchschnittseinkommens-Berechnung bei vorläufiger Bewilligung nach § 41a SGB II. Offene Fundstelle: https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2025/2025_07_16_B_07_AS_19_24_R.html

Weitere Rechtsprechung vor Ausgabe live in dejure.org / bsg.bund.de mit Gericht, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Kaltstart-Rückfragen

1. Wer gehört zur Bedarfsgemeinschaft (§ 7 Abs. 3 SGB II) — Ehepartner, Kinder unter 25, Lebenspartner?
2. Welcher konkrete Punkt des Bescheids wird angegriffen (Regelbedarf-Stufe, Kosten der Unterkunft, Einkommensanrechnung, Vermögenszurechnung, Sanktion, Aufhebungs- und Erstattungsbescheid)?
3. Wurde eine Anhörung nach § 24 SGB X vor Erlass des belastenden Bescheids durchgeführt?
4. Droht eine Versorgungslücke — laufende Leistungen gefährdet (einstweiliger Rechtsschutz § 86b SGG notwendig)?
5. Wie hoch ist die geltend gemachte Erstattung (§ 50 SGB X), und ist der Zeitraum bekannt?
6. Gibt es atypische Mehrbedarfe (z.B. dezentrale Warmwasserbereitung, kostenaufwändige Ernährung, Behinderung)?
7. Bei Sanktion: Liegt eine schriftliche Rechtsfolgenbelehrung vor — und ist die Pflichtverletzung tatbestandlich eindeutig?
8. Ist der Mandant im Karenzjahr (§ 12 Abs. 3 SGB II — erste zwölf Monate SGB-II-Bezug, Vermögen nur bei Erheblichkeit)?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 7 SGB II | Anspruchsberechtigte; Bedarfsgemeinschaft Abs. 3 |
| § 11 SGB II | Einkommensbegriff (alles außer explizit Ausgenommenes) |
| § 11a SGB II | Nicht als Einkommen zu berücksichtigende Einnahmen |
| § 11b SGB II | Einkommensbereinigung: Werbungskosten, Versicherungspauschalen, Erwerbstätigenfreibetrag |
| § 12 SGB II | Vermögensberücksichtigung; Freibetrag EUR 15000 pro Person Abs. 2; Karenzjahr Abs. 3 |
| § 20 SGB II | Regelbedarf; Regelbedarfsstufen 1–6 (Regelbedarfs-Ermittlungsgesetz) |
| § 21 SGB II | Mehrbedarfe: Schwangerschaft, Alleinerziehung, Behinderung, Ernährung, Warmwasser |
| § 22 SGB II | Kosten der Unterkunft (tatsächlich bis zur Angemessenheitsgrenze; Heizkosten separat) |
| § 31 SGB II | Pflichtverletzung; Leistungsminderung |
| § 31a SGB II | Höhe der Leistungsminderung nach Pflichtverletzung — Sanktionen nach BVerfG 5.11.2019 — 1 BvL 7/16 in Schwere begrenzt |
| § 39 SGB II | Kein Suspensiveffekt bei Widerspruch; Ausnahme bei drohender Unzumutbarkeit |
| § 41a SGB II | Vorläufige Leistungserbringung bei ungeklärtem Sachverhalt |
| § 43 SGB II | Aufrechnung von Erstattungsansprüchen (max. 30 % des Regelbedarfs) |
| § 44 SGB X | Rücknahme rechtswidriger Ablehnungen zugunsten des Betroffenen |
| § 45 SGB X | Rücknahme rechtswidriger begünstigender Verwaltungsakte (Vertrauensschutz) |
| § 48 SGB X | Aufhebung bei wesentlicher Änderung der Verhältnisse |

### Leitentscheidungen (Stand Mai 2026)

| Aktenzeichen | Gericht/Datum | Tragende Aussage | Offene Fundstelle |
|---|---|---|---|
| B 7 AS 20/24 R (verbunden mit B 7 AS 30/24 R, B 7 AS 6/25 R) | BSG 02.12.2025 | Regelbedarfe 2022 verfassungsgemäß; 200-Euro-Einmalzahlung hat Kaufkraftverlust kompensiert | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BSG&Datum=02.12.2025&Aktenzeichen=B+7+AS+20/24+R |
| B 7 AS 5/24 R | BSG 12.03.2025 | Leistungsausschluss bei BAföG-Anspruch — gestützte Abgrenzung | https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2025/2025_03_12_B_07_AS_05_24_R.html |
| B 4 AS 4/24 R | BSG 26.03.2025 | § 6b SGB II — Bundeserstattung Verwaltungskosten | https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2025/2025_03_26_B_04_AS_04_24_R.html |
| B 7 AS 17/24 R | BSG 04.06.2025 | Vollstreckung von Erstattungsforderungen durch BA | https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2025/2025_06_04_B_07_AS_17_24_R.html |
| B 7 AS 19/24 R | BSG 16.07.2025 | Durchschnittseinkommens-Berechnung § 41a SGB II | https://www.bsg.bund.de/SharedDocs/Entscheidungen/DE/2025/2025_07_16_B_07_AS_19_24_R.html |
| 1 BvL 7/16 | BVerfG 05.11.2019 | Sanktionen § 31a SGB II in Höhe begrenzt | https://dejure.org/dienste/vernetzung/rechtsprechung?Text=1+BvL+7/16 |

Weitere Entscheidungen vor Ausgabe in dejure.org / bsg.bund.de live verifizieren.

---

## Prüfschema (15 Schritte)

| Schritt | Inhalt | Norm |
|---|---|---|
| 1 | Bedarfsgemeinschaft korrekt abgegrenzt? | § 7 Abs. 3 SGB II |
| 2 | Regelbedarfsstufe richtig zugeordnet (1–6)? | § 20, Anlage RBEG |
| 3 | Mehrbedarfe vollständig berücksichtigt? | § 21 SGB II |
| 4 | Kosten der Unterkunft tatsächlich angesetzt? | § 22 Abs. 1 SGB II |
| 5 | Angemessenheits-Grenze KdU mit aktueller örtlicher Rechtsprechung pruefen | § 22 Abs. 1 S. 1 SGB II — schlüssiges Konzept; BSG-Linie B 7 AS / B 14 AS, Aktenzeichen vor Ausgabe in dejure.org pruefen |
| 6 | Heizkosten separat und angemessen? | § 22 Abs. 1 Satz 3 SGB II |
| 7 | Einkommensbereinigung § 11b korrekt? | § 11b SGB II |
| 8 | Freibetrag Erwerbstätigkeit korrekt berechnet? | § 11b Abs. 2, 3 SGB II |
| 9 | Vermögensfreibetrag EUR 15000 pro Person beachtet? | § 12 Abs. 2 SGB II |
| 10 | Karenzjahr-Schutz greift (erste 12 Monate)? | § 12 Abs. 3 SGB II |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 12 | Verfahrensfehler: Anhörung § 24 SGB X, Begründung § 35 SGB X? | §§ 24, 35 SGB X |
| 13 | Aufhebungsbescheid: Rechtsgrundlage § 45, 48 SGB X korrekt? | §§ 45, 48 SGB X |
| 14 | Erstattungsbetrag zutreffend und Aufrechnungsgrenze § 43 beachtet? | § 43 SGB II |
| 15 | Eilantrag § 86b SGG nötig (kein Suspensiveffekt § 39 SGB II)? | § 86b SGG |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — SGB-II-Bescheid pruefen und anfechten | Widerspruch; Template unten |
| Variante A — Mandant will sofortige Zahlung | Eilantrag § 86b SGG parallel zum Widerspruch |
| Variante B — Rueckforderungsbescheid | § 45 vs. § 48 SGB X unterscheiden; Vertrauensschutz |
| Variante C — Sanktionsbescheid | Verfassungswidrigkeit BVerfGE 1 BvL 7/16 pruefen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 — Vollständiger Widerspruch mit KdU-Rüge

```
An das Jobcenter [Ort]

Az. Jobcenter: [BehAz]
BG-Nummer: [BG]
betr. [Name, Geburtsdatum] und Bedarfsgemeinschaft

Widerspruch gegen den [Bewilligungs-/Aufhebungs-/Erstattungs-]
bescheid vom [Datum], zugegangen am [Datum]

Sehr geehrte Damen und Herren,

namens und in Vollmacht legen wir

 W i d e r s p r u c h

ein.

I. Bedarfsgemeinschaft (§ 7 Abs. 3 SGB II)
[Korrekte Abgrenzung darstellen; ggf. Person zu Unrecht ein-
oder ausgeklammert]

II. Regelbedarf (§ 20 SGB II)
Unsere Mandantschaft wird der Regelbedarfsstufe [X] zugeordnet.
[Richtig / Falsch, weil: Begründung]

III. Mehrbedarfe (§ 21 SGB II)
Folgende Mehrbedarfe wurden zu Unrecht nicht berücksichtigt:
- Alleinerziehung § 21 Abs. 3 SGB II (Anlage W1)
- Kostenaufwändige Ernährung § 21 Abs. 5 SGB II wegen [Diagnose]
 (Anlage W2: ärztliches Attest)

IV. Kosten der Unterkunft (§ 22 SGB II)
Tatsächliche monatliche Kaltmiete: EUR [Betrag]
Angesetzt: EUR [Betrag]

Das vom Jobcenter zugrundeliegende Schlüssige Konzept ist
angreifbar, weil [Argumentation, z.B. veraltete Daten, keine
Differenzierung nach Wohnungsgrößen, keine Verfügbarkeitsanalyse]
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Betrag unterhalb der tatsächlichen Kosten ist unzulässig.

V. Einkommensbereinigung (§ 11b SGB II)
Einkommen aus Erwerbstätigkeit EUR [Betrag] brutto.
Bereinigung: Versicherungspauschale EUR 30, Werbungskosten
EUR [Betrag], Erwerbstätigenfreibetrag § 11b Abs. 2, 3 SGB II.
Fehler: [Konkrete Rechenfehler des Jobcenters].

VI. Verfahrensfehler
Eine Anhörung nach § 24 SGB X wurde vor Erlass des belastenden
Bescheids nicht durchgeführt. Dies ist heilbar (§ 41 SGB X),
aber im Widerspruchsverfahren zu korrigieren.

Wir beantragen:
1. Den Bescheid aufzuheben / zu korrigieren.
2. Die vollen tatsächlichen Kosten der Unterkunft anzuerkennen.
3. Akteneinsicht (§ 25 SGB X).

Mit freundlichen Grüßen
[Fachanwalt/-anwältin für Sozialrecht]
```

### Baustein 2 — Eilantrag § 86b SGG bei Leistungslücke

```
An das Sozialgericht [Ort] [Datum]

Antrag auf einstweilige Anordnung
gem. § 86b Abs. 2 SGG

[Mandant] ./. Jobcenter [Ort]

beantragen wir:

Der Antragsgegner wird im Wege der einstweiligen Anordnung
verpflichtet, dem Antragsteller / der Antragstellerin
vorläufig Leistungen nach SGB II in Höhe von monatlich
EUR [Betrag] (Regelbedarf + KdU) zu gewähren.

Anordnungsanspruch:
Alle Voraussetzungen des SGB II sind erfüllt (Anlage A1:
Meldebestätigung Jobcenter; Anlage A2: Einkommensnachweis;
Anlage A3: Mietvertrag). Der Widerspruch vom [Datum] ist
fristgerecht eingelegt.

Anordnungsgrund:
Ohne sofortige Leistungen drohen Mietrückstand und
Versorgungsausfall. Der Lebensunterhalt ist nicht
anderweitig gesichert. Kein Suspensiveffekt nach
§ 39 SGB II.

Mit freundlichen Grüßen
[Fachanwalt/-anwältin]
```

### Baustein 3 — Widerspruch gegen Sanktionsbescheid

```
An das Jobcenter [Ort]

Widerspruch gegen Sanktionsbescheid vom [Datum]

Sehr geehrte Damen und Herren,

der Sanktionsbescheid ist rechtswidrig, weil:

1. Rechtsfolgenbelehrung fehlerhaft: Die Belehrung enthielt
 keine hinreichend konkrete Benennung der verletzten Pflicht
 und der genauen Rechtsfolge (BSG-Linie zu § 31 SGB II).

2. Kein Verschulden: Die Pflichtverletzung war nicht ver-
 schuldet, weil [konkreter Grund: Krankheit, Irrtum,
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Sanktionen sind nur bei Verschulden verfassungskonform.

3. Verhältnismäßigkeit: Die festgesetzte Minderung von [X %]
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 muss ein Härteparagraph greifen.

Wir beantragen: Aufhebung des Sanktionsbescheids.

Mit freundlichen Grüßen
[Fachanwalt/-anwältin]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Position | Träger | Beweismittel |
|---|---|---|
| Bedarfsgemeinschaft korrekt | Jobcenter (Nachweis) | Melderegister, Behördenauskunft |
| Einkommen korrekt angerechnet | Jobcenter | Lohnnachweis, Steuerbescheid |
| Angemessenheitsgrenze KdU | Jobcenter | Schlüssiges Konzept; Verfügbarkeitsanalyse |
| Mehrbedarfe (Atypischer Bedarf) | Kläger | Ärztliches Attest, Nachweise |
| Pflichtverletzung (Sanktion) | Jobcenter | Aktenlage; Rechtsfolgenbelehrung vorhanden |
| Kein Verschulden (Gegenargument) | Kläger | Krankheitsattest, Schriftverkehr |
| Vertrauensschutz § 45 SGB X | Kläger | Bescheid, Handeln in gutem Glauben |

---

## Fristen und Verjährung

| Frist | Grundlage | Inhalt |
|---|---|---|
| Ein Monat | § 84 Abs. 1 SGG | Widerspruchsfrist nach Bekanntgabe |
| Vier-Tage-Fiktion | § 37 Abs. 2 SGB X (seit 01.01.2025) | Bekanntgabe: vierter Tag nach Aufgabe zur Post |
| Drei-Tage-Fiktion | § 37 Abs. 2 SGB X a.F. | Für Bescheide vor dem 01.01.2025 |
| Ein Monat | § 87 Abs. 1 SGG | Klagefrist nach Widerspruchsbescheid |
| Vier Jahre | § 44 SGB X | Rücknahme rechtswidriger Ablehnungen zugunsten |
| Zehn Jahre | § 45 Abs. 3 SGB X | Rücknahme rechtswidrig begünstigender VA (Betrug) |

---

## Typische Gegenargumente des Jobcenters

| Jobcenter-Argument | Rechtliche Gegenstrategie |
|---|---|
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Einnahmen als Einkommen angerechnet" | § 11a SGB II: Ausnahmen prüfen (Aufwandsentschädigungen, Wohngeld, Kindergeld-Teile) |
| "Vermögen vorhanden" | § 12 Abs. 2: Freibetrag EUR 15000 pro Person; Karenzjahr § 12 Abs. 3; Schonvermögen (Hausrat, Altersvorsorge) |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Aufhebung § 48 SGB X korrekt" | Handlungs-/Kenntnis-Verschulden nicht vorhanden; Vertrauensschutz § 45 SGB X |
| "Vorläufige Leistung § 41a wird endabgerechnet" | Höhe der Nachforderung begrenzt; Billigkeitslösung § 43 SGB II |
| "Keine Anhörung nötig" | § 24 SGB X gilt bei allen belastenden VA; Heilung nur im Widerspruch, nicht im Bescheid |

---

## Streitwert / Kosten

| Position | Richtwert |
|---|---|
| Streitwert Bürgergeld-Klage | Strittiger Nachzahlungsbetrag oder Jahreswert monatlicher Mehrleistungen |
| Gerichtskosten SG | Kostenfrei § 183 SGG (Betroffene) |
| Anwaltsgebühren | PKH regelmäßig bewilligbar; Wahlanwalt EUR 400 bis 800 (erste Instanz) |
| Eilverfahren § 86b SGG | Hälfte Hauptsache-Streitwert; PKH beantragen |
| Akteneinsicht | Gebührenfrei § 25 SGB X |

---

## Strategische Empfehlung

| Fallkonstellation | Empfehlung |
|---|---|
| KdU-Kürzung | Schlüssiges Konzept des Jobcenters prüfen; Mietspiegel / Marktatlas gegenüberstellen |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Aufhebungs-/Erstattungsbescheid | § 45 oder § 48 SGB X Rechtsgrundlage? Vertrauensschutz und Jahresfristen prüfen |
| Eilschutz nötig | § 86b Abs. 2 SGG sofort stellen; kein Suspensiveffekt § 39 SGB II beachten |
| Mehrfach-Bescheide | Jeden Bescheid einzeln anfechten; Sammelwiderspruch vermeiden |
| § 44 SGB X-Rücknahme | Für zurückliegende Zeiträume (max. 4 Jahre) effektiv nutzen |

---

## Ausgabe — Berechnungsprüfung

- Berechnungstabelle Soll vs. Bescheid pro Position (Regelbedarf, Mehrbedarfe, KdU, Einkommen, Vermögen).
- Differenzberechnung pro Monat; bei Abweichung Übergabe an `fachanwalt-sozialrecht-widerspruch-sozialleistung`.

---

## Anschluss-Skills

- `fachanwalt-sozialrecht-widerspruch-sozialleistung` — allgemeine Widerspruchslogik
- `fachanwalt-sozialrecht-erwerbsminderungsrente` — wenn Bürgergeld wegen EM-Rentenprozess läuft
- `fachanwalt-sozialrecht-vergleich-sg-widerspruchsverhandlung` — Vergleichsstrategie

## Quellen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 2. `fachanwalt-sozialrecht-vergleich-sg-widerspruchsverhandlung`

**Fokus:** Vergleich vor Sozialgericht § 101 SGG. Widerspruchsverhandlung Behörde § 84 SGG. Mediation in Sozialleistungs-Streit zunehmend. Anhörung GdB-Verfahren Vergleich Schwerbehinderung. Korrespondenz Behörde Klagebegründung Vergleichsbereitschaft Gericht.

### Sozialrecht — Vergleich vor SG / Widerspruchsverhandlung

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sozialrecht — Vergleich vor SG / Widerspruchsverhandlung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage — kläre vor SG-Verhandlung
1. Verfahrensstand: Widerspruchsverfahren, Klage beim SG, mündliche Verhandlung oder Gütetermin?
2. Ist die Klage fristgerecht nach § 87 SGG (1 Monat ab Widerspruchsbescheid) eingereicht?
3. Beweislage: Liegen aktuelle Gutachten/Atteste vor oder muss Gutachten nach § 109 SGG beantragt werden?
4. Vergleichsbereitschaft der Behörde: Hat sie Abhilfe-Signal gesetzt, Teilabhilfe in Aussicht gestellt?
5. Bei Unterlaufen der Monatsfrist: Wiedereinsetzung (§ 67 SGG) möglich?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Kaltstart-Rückfragen

1. In welchem Verfahrensstand befindet sich das Mandat (Widerspruchsverfahren, Klage anhängig, Termin beim SG schon anberaumt)?
2. Was ist der Streitgegenstand — und wie groß ist der Unterschied zwischen Behörden-Position und Mandanten-Forderung?
3. Liegen aktuelle Sachverständigengutachten vor, oder muss der Beweisstand erst aufgebaut werden?
4. Besteht Vergleichsbereitschaft beim Mandanten — und sind die Minimalziele klar definiert?
5. Hat die Behörde im Widerspruchsverfahren bereits Abhilfe-Signale gesetzt?
6. Ist die Klage innerhalb der Monatsfrist (§ 87 SGG) eingereicht worden?
7. Ist eine Untätigkeitsklage nach § 88 SGG erforderlich (kein Widerspruchsbescheid nach drei Monaten)?
8. Gibt es Beizuladdende (§ 75 SGG) — z.B. Krankenversicherung bei Rentenstreit?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 84 SGG | Widerspruchsverfahren; Frist ein Monat |
| § 85 SGG | Widerspruchsbescheid nach drei Monaten |
| § 87 SGG | Klagefrist: ein Monat nach Widerspruchsbescheid |
| § 88 SGG | Untätigkeitsklage: drei Monate Untätigkeit der Behörde |
| § 101 SGG | Vergleich vor dem Sozialgericht; auch außergerichtlich durch Vergleichs-Protokoll |
| § 109 SGG | Gutachten durch Arzt des Vertrauens auf Antrag des Klägers |
| § 75 SGG | Beiladung notwendiger Beteiligter |
| § 86b SGG | Einstweiliger Rechtsschutz parallel zum Hauptverfahren |
| § 183 SGG | Kostenfreiheit des Verfahrens für Versicherte |
| § 193 SGG | Kostentragung bei Mutwilligkeit; faktisch selten |

### Leitentscheidungen

| Aktenzeichen | Gericht/Datum | Leitsatz |
|---|---|---|
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |

---

## Verfahrenspfade und Strategien

### Pfad 1 — Widerspruchs-Abhilfe durch Behörde

Die günstigste Variante: Behörde überprüft internen Bescheid und erlässt Abhilfebescheid. Voraussetzungen:
- Widerspruchsbegründung mit klaren Rechts- und Tatsachenfehlern
- Neue Beweismittel (aktuelle Atteste, Gutachten)
- Frühzeitige Kontaktaufnahme mit Sachbearbeiter

Taktik: Im Widerspruch explizit auf Fehler hinweisen (§ 35 SGB X-Begründungsmangel, § 24 SGB X-Anhörungsfehler) — erleichtert Behörde die Abhilfe ohne Gesichtsverlust.

### Pfad 2 — Klage und Schriftverkehr vor SG-Termin

Zwischen Klageerhebung und dem ersten Verhandlungstermin liegt oft ein Jahr. In dieser Phase:
- Klagebegründung mit vollständigem Sachvortrag
- Akteneinsicht beim Gericht beantragen
- Vergleichsbereitschaft in Schriftsatz signalisieren
- § 109 SGG-Antrag für eigenes Gutachten stellen (frühzeitig, weil Gutachten Zeit braucht)

### Pfad 3 — Erörterungs- und Verhandlungstermin

Das SG lädt zu einem Erörterungs- oder Verhandlungstermin. Der Vorsitzende unterbreitet oft einen Vergleichsvorschlag:

Taktik im Termin:
- Mandant gut vorbereiten (keine Überraschungen)
- Minimalziel und Maximalziel intern festlegen
- Vergleichsvorschlag nicht sofort annehmen: Bedenkzeit erbitten
- Bei GdB-Vergleich: Zeitliche Bindung und Abänderungsklausel klären

### Pfad 4 — Mediation im Sozialrecht (zunehmend)

Besonders bei langwierigen Bürgergeld-Sanktions- und Pflegegrad-Fällen bieten einige Gerichte Mediation an. Die DGFM bildet Mediatoren für Sozialleistungs-Streit aus. Vorteil: Kreative Lösungen außerhalb der formalen Leistungsgrenzen.

### Pfad 5 — GKV-Ombudsmann (KK-spezifisch)

Bei GKV-Streitigkeiten: Ombudsmann nach § 66 SGB V als Vorab-Klärung. Kein Rechtsmittel, aber Beschleunigung der GKV-Entscheidung.

---

## Prüfschema Vergleichs-Vorbereitung (12 Schritte)

| Schritt | Inhalt | Grundlage |
|---|---|---|
| 1 | Verfahrensstand ermitteln (Widerspruch/Klage/Berufung) | Aktenstatus |
| 2 | Stärken und Schwächen der eigenen Position analysieren | Sachverhalt, Gutachten |
| 3 | Vergleichsziel des Mandanten klären (Minimum, Optimum) | Mandantengespräch |
| 4 | Behördenposition kennen: Spielräume? Ermessen? | Widerspruchsbescheid |
| 5 | Gutachten-Lage: eigene Gutachten vorhanden? Günstig? | § 109 SGG |
| 6 | Verfahrensdauer und Prozesskostenrisiko abwägen | § 183 SGG; PKH |
| 7 | Vergleichsvorschlag formulieren (konkret: GdB X, Rentensatz Y %, Leistung Z EUR) | § 101 SGG |
| 8 | Abänderungsklausel / Befristung im Vergleich sichern | § 101 SGG; § 48 SGB X |
| 9 | Im Termin: Vorsitzenden-Vorschlag kritisch prüfen | SG-Termin |
| 10 | Vergleich schriftlich zu Protokoll nehmen | § 101 Abs. 1 SGG |
| 11 | Vergleichs-Ratifikation durch Mandant vor Unterzeichnung | Vollmacht prüfen |
| 12 | Vollstreckbarkeit des Vergleichs sichern | § 199 SGG |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Vergleich SG / Widerspruchsverhandlung | Vergleichsvorschlag; Template unten |
| Variante A — Mandant will keinen Vergleich | Urteil anstreben; Beweislage einschaetzen |
| Variante B — Teilvergleich moeglich | Streitpunkte aufteilen; Teilerfolg sichern |
| Variante C — Grundsatzfrage offen | Revision zum BSG anstreben; Vergleich vermeiden |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 — Klageerhebung mit Vergleichssignal

```
An das Sozialgericht [Ort] [Datum]

Klage

In dem Rechtsstreit
[Name, Anschrift] ./. [Behörde]

erhebe ich / erheben wir namens und in Vollmacht von [Name]

 K l a g e

gegen den Widerspruchsbescheid der [Behörde] vom [Datum],
Az. [...].

Antrag:
Der Beklagte wird verpflichtet, [konkreter Leistungsantrag,
z.B. EM-Rente, GdB-Feststellung, Bürgergeld-Nachzahlung].

Begründung:
[Kurze Sachdarstellung; ausführliche Begründung erfolgt
nach Ladung]

Unsere Mandantschaft ist grundsätzlich zu einer vergleichs-
weisen Einigung bereit, sofern [Mindestbedingung konkret].

Beweisangebote:
- Anlage K1: Ärztliches Attest
- Anlage K2: Gutachten

Zugleich beantragen wir gemäß § 109 SGG die Einholung eines
Sachverständigengutachtens durch [Gutachter].

Mit freundlichen Grüßen
[Fachanwalt/-anwältin für Sozialrecht]
```

### Baustein 2 — Vergleichsangebot außergerichtlich (Widerspruchsphase)

```
An die [Behörde]

Az. [BehAz]
betr. [Name] — Vergleichsangebot im Widerspruchsverfahren

Sehr geehrte Damen und Herren,

um das Widerspruchsverfahren zu beschleunigen, unterbreiten
wir folgendes Vergleichsangebot:

Unsere Mandantschaft verzichtet auf [Teil der Forderung /
Rückwirkung], wenn die Behörde bereit ist, [konkrete
Gegenleistung: GdB von X, Leistungsgewährung ab Datum Y,
Teilzahlung EUR Z].

Ein solcher Vergleich würde das Verfahren ohne kostenintensive
Klage beenden. Wir bitten um Rückmeldung binnen zwei Wochen.

Mit freundlichen Grüßen
[Fachanwalt/-anwältin]
```

### Baustein 3 — § 109 SGG-Antrag für Vertrauensgutachten

```
An das Sozialgericht [Ort]

Az. S [X] [SGB-Bereich] [Az]

In dem Rechtsstreit [Name] ./. [Behörde]

beantragen wir:

Gemäß § 109 SGG wird ein Gutachten durch folgende Sachver-
ständige / folgenden Sachverständigen eingeholt:

[Gutachter-Name, Fachrichtung, Adresse]

Beweisfrage: [konkret, z.B. Grad der Behinderung; quantitatives
Leistungsvermögen; MdE-Grad]

Die Kläger-Seite beantragt die Einholung auf eigene Kosten.
PKH-Antrag ist gestellt (Anlage: PKH-Antrag).

Mit freundlichen Grüßen
[Fachanwalt/-anwältin]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast und Beweisführung

| Beweisthema | Träger | Standard | Mittel |
|---|---|---|---|
| Medizinische Tatsachen | Kläger | Vollbeweis | Fachärztliche Atteste, Gutachten § 109 SGG |
| Verfahrensfehler (fehlende Anhörung) | Kläger | Vollbeweis | Akte zeigt keine Anhörung |
| Ermessensfehler | Kläger (Rüge) | Begründung im Bescheid | § 35 SGB X |
| Vergleichs-Bindungswirkung | Keine Beweisfrage | Vertrag zu Protokoll | § 101 SGG |
| Abänderbarkeit Vergleich | Neue Tatsachen | Wesentliche Änderung | § 48 SGB X analog |

---

## Fristen und Verjährung

| Frist | Grundlage | Inhalt |
|---|---|---|
| Ein Monat | § 84 SGG | Widerspruchsfrist |
| Drei Monate | § 88 SGG | Untätigkeitsklage wenn kein Widerspruchsbescheid |
| Ein Monat | § 87 SGG | Klagefrist nach Widerspruchsbescheid |
| Nicht limitiert | § 101 SGG | Vergleich kann jederzeit im Verfahren geschlossen werden |
| Vier Jahre | § 44 SGB X | Rücknahme rechtswidriger Bescheide |

---

## Typische Stolpersteine bei Vergleichen

| Stolperstein | Folge | Gegenstrategie |
|---|---|---|
| Vergleich ohne Abänderungsklausel | GdB/Leistung nicht anpassbar bei Verschlechterung | Abänderungsklausel für Folgeanträge einfügen |
| Vergleich unter Wert | Mandant erhält weniger als bei Urteil | Gutachten abwarten; Risikoabwägung mit Mandant |
| Vergleich nicht zu Protokoll | Keine Vollstreckbarkeit | § 101 Abs. 1 SGG: Vergleich immer zu Protokoll |
| Verjährung Nachzahlung nicht vereinbart | Offene Forderung bleibt unklar | Nachzahlungszeitraum im Vergleich konkret benennen |
| Behörde zieht Vergleichsangebot zurück | Verfahren geht weiter | Vergleichsangebot schriftlich festhalten; Vertrauensschutz |
| § 109 SGG-Gutachten zu spät beantragt | Termin ohne eigenes Gutachten | Antrag frühzeitig nach Klagezustellung stellen |

---

## Streitwert / Kosten

| Position | Richtwert |
|---|---|
| Gerichtskosten | Kostenfrei § 183 SGG (Versicherte) |
| Anwaltskosten | PKH regelmäßig; Wahlanwalt nach RVG |
| § 109-Gutachten | EUR 800 bis 5000; Kläger-Vorschuss; PKH möglich |
| LSG-Berufung | Streitwert > EUR 750 (§ 144 Abs. 1 SGG) |
| Untätigkeitsklage | Keine Mehrkosten |

---

## Strategische Empfehlung

| Fallkonstellation | Empfehlung |
|---|---|
| Gutachten-Lage günstig | Klage und Termin abwarten; Vergleich erst wenn Verhandlung läuft |
| Gutachten-Lage unklar | § 109 SGG frühzeitig beantragen; Vergleich erst nach Gutachten |
| Behörde signalisiert Kompromissbereitschaft | Vergleichsangebot im Widerspruch mit konkretem Angebot |
| Untätigkeit der Behörde > 3 Monate | Untätigkeitsklage § 88 SGG; Druck durch Klage |
| GdB-Vergleich | Abänderungsklausel und Befristung sichern |
| Mandant will schnelle Lösung | Aktives Vergleichsangebot; Vollmacht für Vergleichs-Abschluss einholen |

---

## Anschluss-Skills

- `fachanwalt-sozialrecht-widerspruch-sozialleistung` — Widerspruchsprozess
- `fachanwalt-sozialrecht-erwerbsminderungsrente` — EM-Rente Strategie
- `fachanwalt-sozialrecht-sgb-ii-bescheid` — Bürgergeld-Verfahren
- `fachanwalt-sozialrecht-long-covid-bk-anerkennung-bg` — BK-Vergleich

## Quellen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 3. `fachanwalt-sozialrecht-widerspruch-sozialleistung`

**Fokus:** Mandant hat Sozialleistungsbescheid erhalten und Anwalt formuliert Widerspruch. § 84 SGG Widerspruchsfrist ein Monat. Prüfraster: Frist (Bekanntgabe Vier-Tage-Fiktion § 37 Abs. 2 SGB X seit 1.1.2025 PostModG) aufschiebende Wirkung § 86a SGG Antrag § 86b SGG Tatsachen und Rechtsgrundlagen Beweisangebote. Output: Widerspruchsschriftsatz mit Begründung. Abgrenzung zu bescheid-frist-quick-check (Fristkontrolle vorab) und klage-sozialgericht (nach Widerspruchsbescheid).

### Widerspruch gegen Sozialleistungsbescheid (§ 84 SGG)

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Widerspruch gegen Sozialleistungsbescheid (§ 84 SGG)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Triage — kläre zuerst
1. Widerspruchsfrist 1 Monat (§ 84 SGG) ab Bekanntgabe (Vier-Tage-Fiktion § 37 Abs. 2 SGB X n.F.) — läuft sie noch?
2. Aufschiebende Wirkung (§ 86a SGG) oder sofortige Vollziehung (SGB II § 39, SGB V § 86a Abs. 2)? Bei Wegfall: Eilantrag § 86b SGG.
3. Verfahrensmangel (§ 24 SGB X Anhörung, § 35 SGB X Begründung) — führt zur Aufhebung unabhängig von materieller Rechtslage.
4. Bei bestandskräftigem Bescheid: Überprüfungsantrag § 44 SGB X möglich (4 Jahre rückwirkend)?
5. Folgeantrag oder Widerspruch? Einige Leistungen müssen neu beantragt werden.

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Kaltstart-Rückfragen

1. Welche Behörde hat den Bescheid erlassen (Jobcenter, Deutsche Rentenversicherung, Krankenkasse, Versorgungsamt, Pflegekasse, Sozialamt)?
2. Wann wurde der Bescheid zugestellt — und wann läuft die Widerspruchsfrist ab (Vier-Tage-Fiktion § 37 Abs. 2 SGB X seit 01.01.2025)?
3. Welche konkrete Leistung wird abgelehnt, gekürzt oder zurückgefordert (Bürgergeld, EM-Rente, GdB, Pflegegrad, Krankengeld, Verletztengeld)?
4. Hat der Bescheid keine oder beschränkte aufschiebende Wirkung (z.B. SGB II § 39, SGB V § 86a Abs. 2) — ist Eilantrag § 86b SGG nötig?
5. Wurden alle relevanten Unterlagen (Atteste, Gutachten, Einkommensnachweise) der Behörde bereits vorgelegt?
6. Liegt ein Verfahrensmangel vor (fehlende Anhörung § 24 SGB X, unzureichende Begründung § 35 SGB X)?
7. Für bestandskräftige Bescheide: Rücknahme nach § 44 SGB X möglich (Vierjahresfrist)?
8. Hat die Behörde einen Aufhebungs-/Erstattungsbescheid erlassen — auf welche Rechtsgrundlage (§ 45 oder § 48 SGB X)?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 78 Abs. 1 SGG | Widerspruchsverfahren als Zulässigkeitsvoraussetzung vor Klage (bei Bundesbehörden ggf. entbehrlich) |
| § 84 Abs. 1 SGG | Widerspruch: schriftlich, elektronisch nach § 36a SGB I oder zur Niederschrift; Frist ein Monat |
| § 86a SGG | Aufschiebende Wirkung des Widerspruchs (Grundsatz); Ausnahmen Abs. 2 |
| § 86b SGG | Einstweiliger Rechtsschutz: Anordnung aufschiebende Wirkung Abs. 1; einstweilige Anordnung Abs. 2 |
| § 87 SGG | Klagefrist: ein Monat nach Widerspruchsbescheid |
| § 88 SGG | Untätigkeitsklage: drei Monate nach Widerspruchseinlegung ohne Bescheid |
| § 24 SGB X | Anhörung vor belastenden Verwaltungsakten |
| § 35 SGB X | Begründungspflicht von Verwaltungsakten |
| § 37 Abs. 2 SGB X | Bekanntgabefiktion: vierter Tag nach Aufgabe zur Post (seit 01.01.2025 PostModG) |
| § 41 SGB X | Heilung von Verfahrensfehlern (Anhörung kann nachgeholt werden) |
| § 44 SGB X | Rücknahme rechtswidriger Verwaltungsakte zugunsten des Betroffenen (vier Jahre) |
| § 45 SGB X | Rücknahme rechtswidrig begünstigender Verwaltungsakte (Vertrauensschutz) |
| § 48 SGB X | Aufhebung bei wesentlicher Änderung der Verhältnisse |

### Bekanntgabe-Fiktion: Neue Regelung seit 01.01.2025

Das Postmodernisierungsgesetz (PostModG) hat die Bekanntgabefiktion von drei auf vier Tage verlängert:
- **Ab 01.01.2025:** § 37 Abs. 2 SGB X n.F. — Bekanntgabe am vierten Tag nach Aufgabe zur Post
- **Vor 01.01.2025:** § 37 Abs. 2 SGB X a.F. — Bekanntgabe am dritten Tag nach Aufgabe zur Post
- Bei Wochenende oder Feiertag: Verschiebung auf den nächsten Werktag

### Leitentscheidungen

| Aktenzeichen | Gericht/Datum | Leitsatz |
|---|---|---|
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |

---

## Prüfschema (14 Schritte)

| Schritt | Inhalt | Norm |
|---|---|---|
| 1 | Statthaftigkeit: Widerspruchsverfahren erforderlich? | § 78 SGG |
| 2 | Widerspruchsfrist berechnen (Zustelldatum + 4 Tage Fiktion + 1 Monat) | § 84, § 37 SGB X |
| 3 | Form gewahrt (schriftlich, elektronisch, Niederschrift)? | § 84 Abs. 1 SGG |
| 4 | Beschwer konkret benennen (Verletzung der Mandantschaft) | § 84 SGG |
| 5 | Tatsächliche Grundlage des Bescheids prüfen | Sachverhaltsermittlung |
| 6 | Rechtsgrundlage des Bescheids identifizieren (§ 45 oder § 48 SGB X?) | §§ 45, 48 SGB X |
| 7 | Verfahrensmängel (Anhörung § 24, Begründung § 35 SGB X)? | §§ 24, 35, 41 SGB X |
| 8 | Aufschiebende Wirkung kraft Gesetz oder Wegfall? | § 86a, § 39 SGB II |
| 9 | Bei Wegfall aufschiebende Wirkung: Eilantrag § 86b parallel? | § 86b SGG |
| 10 | Beweismittel zusammenstellen (Atteste, Gutachten, Bescheinigungen) | § 84 SGG |
| 11 | Akteneinsicht § 25 SGB X beantragen | § 25 SGB X |
| 12 | Begründung schriftlich ausführen oder Nachholfrist setzen | § 84 SGG |
| 13 | Widerspruchsbescheid abwarten (max. 3 Monate, dann § 88 SGG) | § 88 SGG |
| 14 | Klagefrist § 87 SGG nach Widerspruchsbescheid eintragen | § 87 SGG |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Widerspruch gegen Sozialleistungsbescheid | Widerspruchsschreiben mit Begruendungsankuendigung; Template unten |
| Variante A — Mandant will sofortige Zahlung (kein langer Widerspruch) | Eilantrag § 86b SGG statt oder neben Widerspruch |
| Variante B — Bestandskraeftiger Bescheid | § 44 SGB X Rücknahmeantrag statt Widerspruch |
| Variante C — Verfahrensmangel (Anhörung fehlte) | Formeller Widerspruch wegen § 24 SGB X; materiell pruefen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 — Vollständiges Widerspruchsschreiben mit Begründungsankündigung

```
[Briefkopf Kanzlei]

[Behörde, Anschrift] [Ort, Datum]

Az. [BehAz]
betr. [Name, Geburtsdatum]
[ggf. Versicherungsnummer / BG-Nummer / Kundennummer]

Widerspruch gegen den Bescheid vom [Datum],
zugegangen am [Datum]

Sehr geehrte Damen und Herren,

namens und in Vollmacht von [Name] legen wir gegen den oben
bezeichneten Bescheid fristwahrend

 W i d e r s p r u c h

ein.

Der Bescheid ist rechtswidrig und verletzt unsere Mandantschaft
in ihren Rechten.

Vorläufige Begründung:

1. Tatsächliche Grundlage
 [Kurzdarstellung des Sachverhalts und der strittigen Leistung]

2. Rechtliche Grundlage
 Die Ablehnung / Kürzung / Aufhebung verletzt [§ XX SGB X/II/V/VI]
 weil [Kurzbegründung].

3. Verfahrensfehler
 [Sofern vorhanden: Anhörung fehlt § 24 SGB X; Begründung
 unzureichend § 35 SGB X]

Die ausführliche Widerspruchsbegründung wird nach Akteneinsicht
innerhalb von vier Wochen nachgereicht.

Wir beantragen:
a) Den Bescheid aufzuheben / abzuändern.
b) Akteneinsicht in die vollständige Verwaltungsakte (§ 25 SGB X).
c) [Bei fehlendem Suspensiveffekt:] Zugleich stellen wir beim
 zuständigen Sozialgericht [Ort] Antrag nach § 86b SGG auf
 [Anordnung der aufschiebenden Wirkung / einstweilige Anordnung].

Anlagen:
- Vollmacht
- [Bescheid-Kopie sofern erforderlich]

Mit freundlichen Grüßen
[Fachanwalt/-anwältin für Sozialrecht]
```

### Baustein 2 — Ausführliche Widerspruchsbegründung nach Akteneinsicht

```
[Briefkopf]

An [Behörde, Widerspruchsstelle]

Az. [BehAz]
betr. [Name] — Widerspruchsbegründung

Sehr geehrte Damen und Herren,

wir nehmen auf unseren Widerspruch vom [Datum] Bezug und
begründen diesen nach Akteneinsicht wie folgt:

I. Sachverhaltsergänzung

[Ergänzung der Tatsachen, die dem Bescheid zugrunde gelegt
wurden; Korrekturen gegenüber dem Bescheid; neue Beweismittel]

II. Rechtliche Bewertung

1. Rechtsgrundlage falsch angewendet
 Der Bescheid stützt sich auf § [XX], obwohl [Begründung
 warum die Norm nicht greift oder falsch ausgelegt wurde].

2. Tatbestandsvoraussetzungen nicht erfüllt
 [Konkrete Tatbestandsmerkmale fehlen; BSG-Rechtsprechung zitieren]

3. Ermessensfehler
 [Wenn Ermessen eingeräumt ist: Ermessen nicht ausgeübt /
 Ermessensüberschreitung / -unterschreitung]

III. Verfahrensfehler

[Anhörung § 24 SGB X fehlt; Begründung § 35 SGB X unzureichend;
Sachverhaltsermittlung mangelhaft § 20 SGB X]

Wir halten den Widerspruch aufrecht und beantragen
Abhilfe durch:
[Konkrete Abhilfeforderung]

Beweisangebote:
- Anlage W1: [Beschreibung]
- Anlage W2: [Beschreibung]

Mit freundlichen Grüßen
[Fachanwalt/-anwältin]
```

### Baustein 3 — § 44 SGB X Rücknahme-Antrag für bestandskräftigen Bescheid

```
An [Behörde]

Az. [Alter Bescheid-Az]

Antrag auf Rücknahme nach § 44 SGB X

Sehr geehrte Damen und Herren,

hiermit beantragen wir gemäß § 44 SGB X die Rücknahme des
bestandskräftigen Bescheids vom [Datum] und Nachzahlung der
vorenthaltenen Leistungen.

Begründung:

Der genannte Bescheid war zum Zeitpunkt seines Erlasses
rechtswidrig, weil [Begründung: Norm falsch angewendet,
Sachverhalt falsch ermittelt, Rechtslage falsch bewertet].

Die Vierjahresfrist des § 44 Abs. 4 SGB X ist gewahrt
(Bescheid vom [Datum]; Antrag am [Datum]).

Wir beantragen:
1. Rücknahme des Bescheids vom [Datum].
2. Nachzahlung der zu Unrecht vorenthaltenen Leistungen
 ab [Zeitraum] in Höhe von EUR [Betrag] (hilfsweise
 gerichtlich zu klären).

Mit freundlichen Grüßen
[Fachanwalt/-anwältin]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Position | Träger | Beweismittel |
|---|---|---|
| Rechtzeitigkeit des Widerspruchs | Kläger | Eingangsnachweis, Faxprotokoll, Postnachweis |
| Fristbeginn: Bekanntgabe | Behörde (muss Aufgabedatum nachweisen) | Postaufgabe-Buch |
| Verfahrensmangel (fehlende Anhörung) | Kläger | Abwesenheit eines Anhörungsschreibens in der Akte |
| Sachverhaltsgrundlage des Bescheids | Behörde (im Widerspruchsverfahren darzulegen) | Verwaltungsakte |
| Tatbestandsvoraussetzungen § 44 SGB X | Kläger | Nachweis ursprünglicher Rechtswidrigkeit |
| Vertrauensschutz § 45 SGB X | Kläger | Guter Glaube; keine Kenntnis der Rechtswidrigkeit |

---

## Fristen und Verjährung

| Frist | Grundlage | Inhalt |
|---|---|---|
| Ein Monat | § 84 Abs. 1 SGG | Widerspruchsfrist ab Bekanntgabe |
| Vier Tage | § 37 Abs. 2 SGB X (ab 01.01.2025) | Bekanntgabefiktion nach Aufgabe zur Post |
| Drei Tage | § 37 Abs. 2 SGB X a.F. | Für Bescheide vor 01.01.2025 |
| Drei Monate | § 88 Abs. 1 SGG | Untätigkeitsklage wenn kein Widerspruchsbescheid |
| Ein Monat | § 87 Abs. 1 SGG | Klagefrist nach Widerspruchsbescheid |
| Vier Jahre | § 44 Abs. 4 SGB X | Rücknahme rechtswidriger VA zugunsten; rückwirkende Leistung |
| Ein Jahr | § 45 Abs. 4 SGB X | Jahresfrist bei Aufhebung begünstigender VA |
| Zehn Jahre | § 45 Abs. 3 SGB X | Absolute Frist (Betrug, Täuschung) |

---

## Typische Fehler und Gegenstrategien

| Fehler | Folge | Gegenstrategie |
|---|---|---|
| Widerspruchsfrist verpasst | Bestandskraft des Bescheids | § 44 SGB X-Rücknahme; Wiedereinsetzung in vorigen Stand § 27 SGB X |
| Widerspruch ohne Begründung | Wird möglicherweise ohne Sachprüfung abgewiesen | Begründung binnen vier Wochen nachliefern; Akteneinsicht beantragen |
| Kein Eilantrag bei § 39 SGB II | Leistungen laufen aus | Sofortige § 86b SGG-Klage beim SG |
| § 48 SGB X statt § 45 SGB X | Vertrauensschutz wird umgangen | Rechtsgrundlage im Bescheid prüfen; Jahresfrist § 45 Abs. 4 |
| Widerspruch zu Klage verwechselt | Falsche Behörde | Widerspruch an Ausgangsbehörde; Klage erst nach Widerspruchsbescheid |
| § 44 SGB X-Antrag zu spät | Nur letzte vier Jahre erstattbar | Frühzeitig berechnen; Antrag stellen |

---

## Streitwert / Kosten

| Position | Richtwert |
|---|---|
| Streitwert Widerspruch | Kein Streitwert (Verwaltungsverfahren, gebührenfrei für Betroffene) |
| Gerichtskosten SG | Kostenfrei § 183 SGG |
| Anwaltskosten | PKH regelmäßig; Wahlanwalt nach RVG (Streitwert) |
| Akteneinsicht § 25 SGB X | Gebührenfrei |
| Eilantrag § 86b SGG | Kostenfrei; PKH beantragen |

---

## Strategische Empfehlung

| Fallkonstellation | Empfehlung |
|---|---|
| Frist läuft in wenigen Tagen ab | Frist-wahrender Widerspruch sofort ohne Begründung; Begründung folgt nach Akteneinsicht |
| Keine aufschiebende Wirkung | § 86b SGG parallel zum Widerspruch beim SG stellen |
| Bestandskräftiger Bescheid | § 44 SGB X prüfen; Vierjahresfrist beachten |
| Aufhebungs-/Erstattungsbescheid | § 45 vs. § 48 SGB X korrekt identifizieren; Jahresfrist vs. Vertrauensschutz |
| Untätigkeit der Behörde | Nach drei Monaten Untätigkeitsklage § 88 SGG |
| Klage anhängig | Klagerücknahme und Nachverhandlung kann günstiger sein |

---

## Ausgabe

- `widerspruch-<az>-<datum>.docx` und Markdown-Spiegel.
- Eintrag im Fristenbuch (`fristenbuch-sozialrecht`).
- Eintrag im Postausgang.

## Versand-Check

Vor Versand Skill `bescheid-frist-quick-check` konsultieren. Prüft Inhalt, Signatur, Empfängeradresse und Anlagenständigkeit.

## Hinweis Aussetzung der Vollziehung

Bei Bescheiden über Aufhebung, Rückforderung oder Sanktion: Widerspruch hat keine aufschiebende Wirkung wenn die Behörde die sofortige Vollziehung angeordnet hat oder das Gesetz sie vorsieht (§ 86a Abs. 2 SGG). Hilfsantrag auf Aussetzung der Vollziehung an die Behörde — bei Ablehnung Eilantrag § 86b SGG ans Sozialgericht (Skill `eilantrag-sozialrecht`).

---

## Anschluss-Skills

- `fachanwalt-sozialrecht-sgb-ii-bescheid` — SGB II spezifisch
- `fachanwalt-sozialrecht-erwerbsminderungsrente` — EM-Rente Widerspruch
- `fachanwalt-sozialrecht-vergleich-sg-widerspruchsverhandlung` — nach Widerspruchsablehnung
- `fachanwalt-sozialrecht-long-covid-bk-anerkennung-bg` — BG-Widerspruch
- `eilantrag-sozialrecht` — bei Wegfall aufschiebende Wirkung
- `fristenbuch-sozialrecht` — Vorfrist einplanen

## Quellen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## 4. `hilfsmittelantrag-pruefen`

**Fokus:** Mandant benoetigt Hilfsmittel (Rollstuhl Hoerhilfe Prothese Pflegebett Treppenlift) und fragt welcher Kostentraeger zuständig ist und wie Antrag und Widerspruch aussehen. § 33 SGB V Hilfsmittelverzeichnis § 139 SGB V § 40 SGB XI § 47 SGB IX. Prüfraster: Zuständigkeit Krankenkasse/Pflegekasse/Eingliederungstraeger/Sozialhilfe Festbetraege Mehrkostenregelung typische Ablehnungsgründe. Output: Antragsentwurf oder Widerspruchsentwurf Hilfsmittel. Abgrenzung zu eingliederungshilfe-schule (Schule) und pflegegrad-widerspruch (Pflegegrad).

### Hilfsmittelantrag prüfen

## Fachlicher Kern — Sozialrecht und Sozialversicherungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Hilfsmittelantrag prüfen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** SGB I, IV § 7 und § 7a, V, VI, VII, IX, X §§ 20, 24, 44, 45, 48, 50, 60 ff.; SGB II, XII; SGG §§ 54, 86a, 86b, 87, 90, 103, 109, 144, 151, 160; Pflegebegutachtung/MD-Richtlinien live prüfen.
- **Verifizierte Anker:** BSG, Urteil vom 05.11.2024 - B 12 BA 3/23 R (Lehrende/Dozenten: Status immer einzelfallabhängig); BSG, Urteil vom 23.04.2024 - B 12 BA 9/22 R (Pilot/Freelancer, Eingliederung und unternehmerisches Risiko); BSG, Urteil vom 01.02.2022 - B 12 KR 37/19 R und Urteil vom 20.02.2024 - B 12 KR 1/22 R (GmbH-Geschäftsführer, Sperrminorität/mittelbare Beteiligung).
- **Arbeitsmodus:** Immer Verwaltungsakt, Frist, Widerspruch/Klage/eA, Amtsermittlung, medizinische Tatsachen, Mitwirkungspflichten und Beweisgutachten trennen; bei Status § 7 SGB IV: tatsächliche Eingliederung, Weisung, Rechtsmacht und Unternehmerrisiko abgleichen.
- **Outputpflicht:** Bescheidanalyse in einfacher Sprache, Widerspruch, eA-Antrag, Statusmatrix, medizinische Beweisfragen, Belegliste, Fristenplan oder SG-Schriftsatz.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Anspruchsgrundlagen im Überblick

### Krankenversicherung (SGB V)

- **§ 33 SGB V** Hilfsmittel zur Sicherung des Erfolgs der Krankenbehandlung zur Vorbeugung Behinderung oder zum Behinderungsausgleich.
- **§ 139 SGB V** Hilfsmittelverzeichnis des GKV-Spitzenverbands — Voraussetzung für Standard-Hilfsmittel.
- **§ 33 Abs. 6 SGB V** Festbetraege.
- **§ 33 Abs. 1 Satz 4 SGB V** Mehrkostenübernahme bei medizinisch begründetem Sondermodell.

### Pflegeversicherung (SGB XI)

- **§ 40 SGB XI** Pflegehilfsmittel zur Erleichterung der Pflege (Pflegebett Rollstuhl mit Pflegemerkmalen) und zum Verbrauch bestimmte Pflegehilfsmittel.
- **§ 40 Abs. 4 SGB XI** Maßnahmen zur Verbesserung des individuellen Wohnumfelds (Treppenlift bis 4000 EUR pro Maßnahme im Regelfall).

### Eingliederungshilfe (SGB IX Teil 2)

- **§§ 102 ff. SGB IX** Leistungen zur sozialen Teilhabe einschließlich Hilfsmittel zur Teilhabe (z. B. Vorlesegerät für blinde Person Schulbegleitung Kommunikationshilfe).

### Sozialhilfe (SGB XII)

- **§§ 53 ff. SGB XII** Hilfen in besonderen Lebenslagen — subsidiaer.

## Prüfraster

### Bedarf

- Ärztliche Verordnung vorhanden?
- Eindeutige Indikation (medizinische Notwendigkeit Teilhabeziel Pflegeerleichterung)?
- Vergleich zwischen Standardversorgung und konkretem Wunschmodell.

### Zuständigkeit

- Welcher Träger ist primaer zuständig? Bei Streit § 14 SGB IX — Zuständigkeitsklärung binnen zwei Wochen sonst Vorleistungspflicht.
- Kommunikation mit der Kasse: Antrag immer schriftlich; Aktenzeichen vergeben; Frist § 18 SGB IX (zwei Monate für Rehabilitationsträger).

### Genehmigungsfiktion § 18 SGB IX / § 13 Abs. 3a SGB V

- **§ 13 Abs. 3a SGB V** — Krankenkasse muss innerhalb von drei Wochen über Antrag entscheiden (fünf Wochen bei MDK-Gutachten). Bei Untätigkeit gilt Antrag als genehmigt.
- **§ 18 SGB IX** — bei Teilhabe-Anträgen zwei Monate.
- Pflichtschritt: Frist im Fristenbuch (Skill `fristenbuch-sozialrecht`).

### Mehrkosten und Sondermodelle

- Versicherter darf Sondermodell auf eigene Kosten wählen (§ 33 Abs. 1 Satz 9 SGB V).
- Bei medizinischer Notwendigkeit der Mehrkosten Anspruch gegen die Kasse — Begründung mit Atteste und Vergleichsbewertung.

## Sondergeneralien

### Rollstuhl

- Elektrorollstuhl bei eingeschraenkter Bewegungsfähigkeit + Ausschluss handbetriebener Versorgung.
- Pflegerollstuhl bei stationärer Pflege über SGB XI möglich.

### Hörhilfe / Cochlea-Implantat

- Hörgeräteversorgung nach Hilfsmittelverzeichnis; Aufzahlung bei Sondermodellen.
- BSG-Rspr. zur Mehrkostenproblematik bei hochgradig Hörgeschädigten.

### Vorlesekraft / Hilfsmittel für blinde Personen

- Vorlesegerät als Hilfsmittel zur Teilhabe (SGB IX) oder bei Berufsausbildung beruflicher Teilhabe (Bundesagentur für Arbeit DRV SGB VI).
- Vorlesekraft als persönliche Assistenz nach SGB IX Teilhabe / Assistenz für Studium oder Beruf.

### Treppenlift / Wohnungsumbau

- Pflegekasse SGB XI § 40 bei pflegebedingtem Bedarf bis Höchstbetrag.
- Eingliederungshilfe oder Sozialhilfe ergänzend.

## Ausgabe

- Bei Ablehnung: Widerspruchsentwurf über Skill `widerspruch-formulieren` mit fachlichen Bausteinen.
- Bei Untätigkeit: Frist im Fristenbuch für Genehmigungsfiktion / Untätigkeitsklage § 88 SGG.

## Triage — kläre vor Antragsstellung oder Widerspruch

1. Welcher Träger ist primär zuständig — Krankenkasse (§ 33 SGB V), Pflegekasse (§ 40 SGB XI), Eingliederungshilfeträger (§§ 102 ff. SGB IX) oder Sozialhilfe (§§ 53 ff. SGB XII)?
2. Liegt ärztliche Verordnung vor, und entspricht das Hilfsmittel dem Hilfsmittelverzeichnis (§ 139 SGB V)?
3. Läuft Genehmigungsfiktion nach § 13 Abs. 3a SGB V (drei Wochen) oder § 18 SGB IX (zwei Monate) — Frist bereits abgelaufen?
4. Ist das Standardmodell medizinisch ausreichend, oder ist Mehrkosten-Übernahme für ein Sondermodell begründbar?
5. Eilbedürftigkeit: ist das Hilfsmittel lebensnotwendig oder schulisch/beruflich unabweisbar? (→ § 86b SGG)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
