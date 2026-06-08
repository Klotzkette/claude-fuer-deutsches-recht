---
name: pflichtteil-berechnen-schriftsatzkern
description: "Pflichtteil Berechnen Schriftsatzkern im Plugin Fachanwalt Erbrecht: prüft konkret Pflichtteilsanspruch und Pflichtteilsergaenzungsanspruch, Erbrechtsklage oder erbrechtlichen Antrag substantiiert, Belegmatrix. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Pflichtteil Berechnen Schriftsatzkern

## Arbeitsbereich

**Pflichtteil Berechnen Schriftsatzkern** ordnet den Fall über die tragenden Prüfungslinien: Pflichtteilsanspruch und Pflichtteilsergaenzungsanspruch, Erbrechtsklage oder erbrechtlichen Antrag substantiiert, Belegmatrix. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüfungslinien

| Prüfungslinie | Fokus |
| --- | --- |
| `pflichtteil-berechnen` | Pflichtteilsanspruch und Pflichtteilsergaenzungsanspruch berechnen. §§ 2303 2311 2325 BGB Pflichtteil. Prüfraster: Pflichtteilsquote Nachlasswert Bewertungsstichtag Abzuege Ergaenzungsanspruch Auskunft. Output: Pflichtteilsberechnung mit Rechenweg. Abgrenzung: nicht für Auskunftsklage oder Pflichtteilsklage (schriftsatzkern-substantiierung). |
| `schriftsatzkern-substantiierung` | Erbrechtsklage oder erbrechtlichen Antrag substantiiert formulieren. §§ 2303 2353 BGB §§ 253 286 ZPO. Prüfraster: Anspruchsgrundlage Sachverhalt Beweisangebot Antrag Streitwert Fristen. Output: Schriftsatzkern Klagentwurf oder Antrag. Abgrenzung: nicht für außergerichtliche Korrespondenz oder Berechnungen. |
| `spezial-belegmatrix-sonderfall-und-edge-case` | Belegmatrix: Sonderfall und Edge-Case-Prüfung im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüfungslinien im Detail

## 1. `pflichtteil-berechnen`

**Fokus:** Pflichtteilsanspruch und Pflichtteilsergaenzungsanspruch berechnen. §§ 2303 2311 2325 BGB Pflichtteil. Prüfraster: Pflichtteilsquote Nachlasswert Bewertungsstichtag Abzuege Ergaenzungsanspruch Auskunft. Output: Pflichtteilsberechnung mit Rechenweg. Abgrenzung: nicht für Auskunftsklage oder Pflichtteilsklage (schriftsatzkern-substantiierung).

### Pflichtteil und Pflichtteilsergänzung berechnen

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Pflichtteil und Pflichtteilsergänzung berechnen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Mandantenfragen beim Kaltstart

1. Wer ist der Erblasser und wann ist der Erbfall eingetreten? Letzter gewöhnlicher Aufenthalt (Gerichtsstand)?
2. In welchem Verhältnis steht der Mandant zum Erblasser — Abkömmling, Ehegatte, Elternteil? Durch Testament oder Erbvertrag enterbt oder zu wenig bedacht?
3. Wer sind die übrigen Pflichtteilsberechtigten und die eingesetzten Erben?
4. Hat der Erblasser Schenkungen in den letzten 10 Jahren getätigt (§ 2325 BGB)? An wen und in welcher Höhe?
5. Liegt ein Bestandsverzeichnis nach § 2314 BGB vor oder muss es erst eingefordert werden?
6. Gibt es Vorausempfänge des Pflichtteilsberechtigten mit Anrechnungsbestimmung (§ 2315 BGB)?
7. Hat der Pflichtteilsberechtigte einen Pflichtteilsverzicht erklärt (§ 2346 BGB)?
8. Besteht ein Pflichtteilsentzugsgrund nach § 2333 BGB (Straftat gegen Erblasser, Erblasser-nahe Personen)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| § 2303 BGB | Pflichtteilsrecht — Geldanspruch in Höhe der Hälfte des gesetzlichen Erbteils |
| § 2304 BGB | Ausschluss des Pflichtteils bei Zuwendung unter Auflage oder Bedingung |
| § 2305 BGB | Pflichtteil bei Bedachtheit mit weniger als Pflichtteil — Ergänzungsanspruch |
| § 2309 BGB | Ausschluss durch nähere Verwandte — Enkel nur bei Vorversterben der Kinder |
| § 2311 BGB | Bewertungsstichtag — Wert des Nachlasses zum Zeitpunkt des Erbfalls |
| § 2314 BGB | Auskunftsanspruch — Bestandsverzeichnis; SV-Bewertung auf Nachlasskosten |
| § 2315 BGB | Anrechnung auf Pflichtteil — Vorausempfänge mit Anrechnungsbestimmung |
| § 2316 BGB | Ausgleichung unter Abkömmlingen — gleichmäßige Behandlung |
| § 2325 BGB | Pflichtteilsergänzung — Schenkungen letzter 10 Jahre; Abschmelzung 10 % je Jahr |
| § 2326 BGB | Pflichtteilsergänzung bei Bedachtsein — Ergänzung bis zur vollen Hälfte |
| § 2327 BGB | Anrechnung Eigengeschenke auf Ergänzungsanspruch |
| § 2329 BGB | Direktanspruch gegen Beschenkte wenn Nachlass nicht ausreicht |
| § 2332 BGB | Verjährung — 3 Jahre ab Kenntnis; 30 Jahre absolut |
| § 2333 BGB | Pflichtteilsentzug — abschließende Gründe |
| § 2346 BGB | Pflichtteilsverzicht — notariell beurkundeter Verzicht |

## Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---------|-------------|-------|-------------|
| BGH IV. Zivilsenat | IV ZR 88/24 | 12.03.2025 | Für die Entstehung des Pflichtteilsanspruchs (§ 199 Abs. 1 Nr. 1 BGB) ist § 2317 Abs. 1 BGB auch dann maßgebend, wenn der Berechtigte zum Zeitpunkt des Erbfalls aufgrund der gesetzlichen Ausübungssperre in § 1600d Abs. 5 BGB an einer Anspruchsdurchsetzung gehindert ist. Für den Pflichtteilsanspruch des nichtehelichen Kindes ist Kenntnis von der wirksamen Vaterschaftsanerkennung oder -feststellung erforderlich. Quelle: bundesgerichtshof.de / dejure.org. |
| BGH IV. Zivilsenat | IV ZR 93/24 | 02.07.2025 | Zuwendung von Todes wegen an behandelnden Arzt nicht wegen Verstoß gegen § 32 (M)BO-Ä unwirksam; Berufsordnung kein § 134 BGB-Verbot; Testierfreiheit (Art. 14 GG) überwiegt. Quelle: bundesgerichtshof.de PM 2025/2025122.html. |
| Weitere Rechtsprechung | Live-Verifikation erforderlich | - | keine weitere Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema — Stufenweise Pflichtteilsberechnung

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfpunkt | Norm | Ergebnis |
|---------|-----------|------|---------|
| 1 | Pflichtteilsberechtigung prüfen | § 2303 BGB | Wer ist berechtigt? Abkömmlinge / Ehegatte / Eltern |
| 2 | Gesetzliche Erbquote ermitteln | §§ 1924 ff. BGB | Quote je Berechtigtem |
| 3 | Pflichtteilsquote berechnen | § 2303 Abs. 1 Satz 2 | Hälfte der gesetzlichen Erbquote |
| 4 | Nachlasswert ermitteln | § 2311 BGB | Aktiva minus Passiva am Todestag |
| 5 | Schenkungen letzter 10 Jahre hinzurechnen | § 2325 BGB | Abschmelzung 10 % je Jahr |
| 6 | Pflichtteil berechnen | §§ 2303, 2311 BGB | Quote × Nachlasswert |
| 7 | Pflichtteilsergänzung berechnen | § 2325 BGB | Quote × Schenkungswert |
| 8 | Anrechnung Vorausempfänge | § 2315 BGB | Minderung Pflichtteil |
| 9 | Anrechnung Eigengeschenke | § 2327 BGB | Minderung Pflichtteilsergänzung |
| 10 | Direktanspruch gegen Beschenkte prüfen | § 2329 BGB | Wenn Nachlass insufficient |
| 11 | Verjährung prüfen | § 2332 BGB | 3 Jahre ab Kenntnis |

## Schritt 1 — Pflichtteilsberechtigte § 2303 BGB

**Pflichtteilsberechtigt:**
- Abkömmlinge des Erblassers (Kinder, Enkel wenn Kinder vorverstorben — § 2309 BGB)
- Ehegatte / eingetragener Lebenspartner (LPartG)
- Eltern des Erblassers — nur wenn keine Abkömmlinge vorhanden

**Nicht pflichtteilsberechtigt:** Geschwister, Großeltern, Stiefeltern, Stiefkinder (ohne Adoption)

## Schritt 2 — Gesetzliche Erbquoten §§ 1924 ff. BGB

| Konstellation | Gesetzliche Erbquoten |
|--------------|----------------------|
| Ehegatte + 2 Kinder (Zugewinngemeinschaft) | Ehegatte 1/2 (1/4 nach § 1931 + 1/4 pauschalierter Zugewinn § 1371); jedes Kind 1/4 |
| Ehegatte + 1 Kind (Zugewinngemeinschaft) | Ehegatte 1/2; Kind 1/2 |
| Ehegatte + keine Kinder, Eltern leben | Ehegatte 3/4; Eltern 1/4 |
| Nur 3 Kinder, kein Ehegatte | Jedes Kind 1/3 |
| Keine Kinder + Eltern | Jeder Elternteil 1/2 |
| Ehegatte + keine Kinder + keine Eltern | Ehegatte allein 100 % |

**Zugewinngemeinschaft Hinweis:** § 1371 BGB pauschaliert den Zugewinn durch Erhöhung der Erbquote um 1/4 ("erbrechtliche Lösung"). Alternativ: bei Ausschlagung güterrechtliche Lösung + kleiner Pflichtteil § 1371 Abs. 3 BGB.

## Schritt 3 — Pflichtteilsquote

```
Pflichtteilsquote = 1/2 × gesetzlicher Erbteil
```

| Beispiel | Gesetzlicher Erbteil | Pflichtteilsquote |
|---------|---------------------|------------------|
| Einziges Kind enterbt; kein Ehegatte | 1/2 | 1/4 des Nachlasses |
| Kind 1 enterbt; Ehegatte + Kind 2 (Zugewinn) | 1/4 | 1/8 des Nachlasses |
| Ehegatte enterbt; 2 Kinder | 1/2 (inkl. Zugewinnzuschlag) | 1/4 des Nachlasses |
| Kind enterbt bei Zugewinngemeinschaft Ehegatte + 1 Kind | 1/2 | 1/4 des Nachlasses |

## Schritt 4 — Nachlassbewertung § 2311 BGB

### Aktiva (Stichtag = Todestag)

| Vermögensgegenstand | Bewertungsmethode |
|--------------------|------------------|
| Bankguthaben, Barvermögen | Nennwert |
| Wertpapiere (börsennotiert) | Schlusskurs Todestag |
| Wertpapiere (nicht börsennotiert) | Ertragswertverfahren |
| Immobilien | Verkehrswert-Gutachten (SV § 2314 Abs. 1 Satz 2 BGB) |
| Unternehmensbeteiligungen | IDW S1 oder vereinfachtes Ertragswertverfahren |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Hausrat | Zeitwert (geschätzt) |
| Lebensversicherung | Rückkaufswert (soweit keine Drittbegünstigung) |

### Passiva

| Verbindlichkeit | Abzugsfähig |
|----------------|------------|
| Erblasser-Schulden (Kredit, Steuern, Unterhalt) | Ja |
| Beerdigungskosten § 1968 BGB | Ja |
| Pflegekosten letzte Lebensjahre | Ja (soweit nicht bereits bezahlt) |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Pflichtteils-Verbindlichkeiten anderer | Ja (als Erbfallschuld) |

## Schritt 5 — Pflichtteilsergänzung § 2325 BGB

### Abschmelzungsregel

| Schenkungsjahr vor Erbfall | Anrechnungsquote |
|---------------------------|-----------------|
| 1. Jahr (0–12 Monate vor Tod) | 100 % |
| 2. Jahr | 90 % |
| 3. Jahr | 80 % |
| 4. Jahr | 70 % |
| 5. Jahr | 60 % |
| 6. Jahr | 50 % |
| 7. Jahr | 40 % |
| 8. Jahr | 30 % |
| 9. Jahr | 20 % |
| 10. Jahr | 10 % |
| > 10 Jahre | 0 % — keine Anrechnung |

### Ausnahme: Ehegatte-Schenkungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Schenkung an Ehegatte vor 30 Jahren ist relevant wenn Ehe bei Tod noch bestand

### Ausnahme: Schenkung unter Nießbrauchsvorbehalt

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Erblasser verschenkt Immobilie aber behält lebenslangen Nießbrauch → Frist ab Tod/Aufgabe Nießbrauch

### Bewertung der Schenkung § 2325 Abs. 2 BGB

| Sachtyp | Bewertungsregel |
|---------|----------------|
| Geld, Wertpapiere (verbrauchbar) | Wert zum Schenkungszeitpunkt |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

**Inflationsbereinigung:** Schenkungswert × (Verbraucherpreisindex Todestag / Verbraucherpreisindex Schenkungstag)

## Berechnungsformel (Gesamtübersicht)

```
PFLICHTTEILSBERECHNUNG

I. Nettonachlass
 Aktiva zum Todestag: EUR [A]
 - Passiva: EUR [B]
 = Nettonachlass: EUR [C]

II. Pflichtteilsergänzung (Schenkungen)
 Schenkung Nr. 1 vom [Datum]:
 Wert (nicht verbrauchbar — Niederstwert): EUR [X]
 Abschmelzung [X]%: EUR [Y]
 Schenkung Nr. 2 vom [Datum]:
 Wert (verbrauchbar — Nominalbetrag): EUR [X]
 Abschmelzung [X]%: EUR [Y]
 Summe Ergänzungsmasse: EUR [D]

III. Berechnungsbasis
 Nettonachlass + Ergänzungsmasse: EUR [C+D]

IV. Pflichtteilsquote: [X/Y] (z.B. 1/8)

V. Pflichtteilsanspruch:
 Nettonachlass × Quote: EUR [P1]
 Ergänzungsanspruch:
 Ergänzungsmasse × Quote: EUR [P2]
 Gesamt (vor Anrechnung): EUR [P1+P2]

VI. Anrechnung § 2315 BGB (Vorausempfang): EUR [minus A]
 Gesamt-Pflichtteilsanspruch: EUR [Summe]
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Pflichtteil berechnen | Neunstufiges Schema; Schriftsatzbausteine unten |
| Variante A — Erbe zahlt freiwillig wenn Betrag klar | Aussergerichtliche Geltendmachung; Klage nur als Backup |
| Variante B — viele Schenkungen innerhalb von 10 Jahren | Pflichtteilsergaenzung § 2325 BGB Hauptfokus |
| Variante C — Immobilienwert streitig | Sachverstaendigengutachten einplanen; Stufenklage als Sicherheit |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatz-Bausteine

### Auskunftsanforderung § 2314 BGB

```
An die Erben nach [Erblasser]
[Adresse]

Auskunfts- und Wertermittlungsanspruch nach § 2314 BGB

Sehr geehrte Damen und Herren,

namens und in Vollmacht unseres Mandanten — [Name] als
Pflichtteilsberechtigter nach dem am [Datum] verstorbenen
[Erblasser] — fordern wir Sie auf, binnen vier Wochen ein
notarielles Nachlassverzeichnis nach § 2314 Abs. 1 Satz 3
BGB vorzulegen.

Das Verzeichnis muss enthalten:
1. Sämtliche Aktiva und Passiva des Nachlasses zum Todestag
 [Datum], bewertet nach §§ 2311, 2311a BGB
2. Sämtliche Schenkungen des Erblassers der letzten 10 Jahre
 nach § 2325 BGB (auch gemischte Schenkungen und
 Schenkungen unter Nießbrauchsvorbehalt)
3. Ausgleichungspflichtige Zuwendungen nach §§ 2315, 2316 BGB

Hinsichtlich der Bewertung von Immobilien und Unternehmen
verlangen wir bereits jetzt die Hinzuziehung eines vereidigten
Sachverständigen nach § 2314 Abs. 1 Satz 2 BGB. Die Kosten
trägt der Nachlass (§ 2314 Abs. 2 BGB).

Nach fruchtlosem Fristablauf werden wir Stufenklage nach
§ 254 ZPO erheben.

Mit freundlichen Grüßen
[Kanzlei]
```

### Stufenklage § 254 ZPO (Antragsformulierung)

```
Klage

In der Sache [Pflichtteilsberechtigter] ./. [Erben]

beantragen wir:

I. Auskunftsstufe:
 Die Beklagten werden verurteilt, Auskunft über den Bestand
 des Nachlasses nach [Erblasser] zu erteilen durch Vorlage
 eines vollständigen Bestandsverzeichnisses einschließlich
 aller Schenkungen der letzten 10 Jahre.

II. Versicherungsstufe:
 Die Beklagten werden verurteilt, die Richtigkeit des
 vorgelegten Verzeichnisses an Eides statt zu versichern.

III. Zahlungsstufe:
 Die Beklagten werden verurteilt, an den Kläger den sich
 aus der Auskunft ergebenden Pflichtteilsanspruch nebst
 Zinsen in Höhe von 5 Prozentpunkten über dem
 Basiszinssatz seit Klagezustellung zu zahlen.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Beweislast

| Partei | Beweislastgegenstand | Beweismittel |
|--------|---------------------|--------------|
| Pflichtteilsberechtigter | Berechtigung (Verwandtschaft, Ehegatten-Status) | Geburtsurkunde, Heiratsurkunde, Scheidungsurteil |
| Pflichtteilsberechtigter | Schenkungen § 2325 BGB | Schenkungsvertrag, notarielles Protokoll, Kontobewegungen |
| Pflichtteilsberechtigter | Wert der Schenkung | SV-Gutachten, Börsenkurs, Kaufpreisnachweis |
| Erbe | Anrechnungsbestimmung § 2315 BGB | Schriftliche Vereinbarung mit Anrechnungsvorbehalt |
| Erbe | Pflichtteilsentzug § 2333 BGB | Strafurteil, Beweise für Verfehlung |
| Erbe | Pflichtteilsverzicht § 2346 BGB | Notarielle Urkunde |

## Fristen

| Frist | Auslöser | Dauer | Folge |
|-------|---------|-------|-------|
| Verjährung Pflichtteil § 2332 BGB | Kenntnis von Erbfall + letztwilliger Verfügung | 3 Jahre ab Jahresende | Anspruchsverlust |
| Absolute Verjährung | Erbfall (unabhängig von Kenntnis) | 30 Jahre § 199 Abs. 3a BGB | Anspruchsverlust |
| Auskunftsfrist § 2314 BGB | Setzung im Schreiben | Üblich 4 Wochen | Stufenklage |
| Direktanspruch § 2329 BGB | Schenkungsdatum | 3 Jahre ab Kenntnis | Verjährung gegen Beschenkten |

## Gegenargumente und Reaktion

| Gegenargument Erbe | Reaktion |
|-------------------|---------|
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Pflichtteilsverzicht liegt vor" | Prüfen ob notarielle Form § 2346 BGB gewahrt; Anfechtung wegen Irrtum/Täuschung § 2351 BGB |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Vorausempfang anzurechnen" | Anrechnungsbestimmung schriftlich vereinbart? § 2315 BGB; nur bei ausdrücklicher Anrechnung |
| "Nachlasswert überhöht bewertet" | Eigene SV-Bewertung; Niederstwertprinzip bei nicht verbrauchbaren Sachen |

## Streitwert und Kosten

**Streitwert Pflichtteilsklage:** Bezifferter Pflichtteilsanspruch

**Gerichtsgebühren Beispiel EUR 80.000:**
- Stufe 1 (Auskunft): Streitwert 25 % der Hauptsache = EUR 20.000 → GKG ca. EUR 588
- Stufe 3 (Zahlung): EUR 80.000 → GKG ca. EUR 1.962 (3.0)
- RA-Gebühren gesamt je Partei: ca. EUR 5.000–7.000

**SV-Gutachten Immobilie:** EUR 2.000–6.000 (Nachlasskosten § 2314 Abs. 2 BGB)

## Strategische Empfehlung

| Strategie | Empfehlung | Begründung |
|-----------|-----------|------------|
| Verjährung sichern | Sofort nach Erbfall Auskunftsschreiben senden | § 2332 BGB Frist läuft ab Jahresende; keine Fristverlängerung |
| Stufenklage | Bei Auskunftsverweigerung unverzüglich Stufe 1 erheben | Einheitliches Verfahren; effizient |
| SV frühzeitig | Sachverständigen für Immobilien-/Unternehmens-Bewertung benennen | Basis für Pflichtteilshöhe; auf Nachlasskosten § 2314 Abs. 2 BGB |
| Schenkungsrecherche | Kontoauszüge Erblasser letzter 10 Jahre vollständig durchsuchen | Häufig unbekannte Schenkungen |
| Direktanspruch § 2329 | Bei insolventen Erben gegen Beschenkte vorgehen | Sicherungsmechanismus wenn Nachlass aufgebraucht |

## Anschluss-Skills

- `fachanwalt-erbrecht-pflichtteilsberechnung` — vertiefte Pflichtteilsberechnung mit Auskunftsstufe
- `nachlassinsolvenz-erbenhaftung-begrenzen` — wenn Nachlass überschuldet
- `fachanwalt-erbrecht-testamentsvollstreckung` — TV-Abwicklung in Pflichtteilskonstellationen

## Quellen

- BGB §§ 2303–2338, 2346, 1924 ff., 1371
- ZPO § 254
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Burandt/Rojahn Erbrecht
- Stand: 05/2026

## 2. `schriftsatzkern-substantiierung`

**Fokus:** Erbrechtsklage oder erbrechtlichen Antrag substantiiert formulieren. §§ 2303 2353 BGB §§ 253 286 ZPO. Prüfraster: Anspruchsgrundlage Sachverhalt Beweisangebot Antrag Streitwert Fristen. Output: Schriftsatzkern Klagentwurf oder Antrag. Abgrenzung: nicht für außergerichtliche Korrespondenz oder Berechnungen.

### Schriftsatzkern und Substantiierung im Erb- und Pflichtteilsrecht

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Schriftsatzkern und Substantiierung im Erb- und Pflichtteilsrecht` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Schriftsatzkern und Substantiierung im Erb- und Pflichtteilsrecht

- **Spezialfrage (Schriftsatzkern und Substantiierung im Erb- und Pflichtteilsrecht):** Anspruchsgrundlage Sachverhalt Beweisangebot Antrag Streitwert Fristen. Output: Schriftsatzkern Klagentwurf oder Antrag. Abgrenzung: nicht für außergerichtliche Korrespondenz oder Berechnungen.
- **Arbeitsweise:** Erst Sachverhalt, Norm, Frist, Zuständigkeit und Beweis klären; Rechtsprechung nur verifiziert als tragenden Beleg einsetzen.

## Aktuelle Rechtsprechung (Substantiierung Erbrecht)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Wann dieser Arbeitsgang greift

- Es soll ein vollwertiger Schriftsatz im Bereich Erb- und Pflichtteilsrecht erstellt werden, typischerweise: Pflichtteilsklage, Erbschein-Antrag/Beschwerde, Erbenfeststellungsklage.
- Die Mandatsannahme und ggf. Vergleichsverhandlung sind abgeschlossen oder gescheitert.
- Klage-, Widerspruchs-, Einspruchs-, Rechtsmittel-Frist ist bekannt und im Kalender eingetragen.

## Aufbauschema

### A. Rubrum

- Parteien (Bezeichnung wie im Vorprozess oder Bescheid, exakte Schreibweise!).
- Zustellungsanschrift Bevollmaechtigte.
- Gericht/Behörde (Zuständigkeit pruefen und im Schriftsatz darstellen, wenn streitig).
- Aktenzeichen (Bezugs-Az., neues Az. nach Eingang).
- Streitwert/Gegenstandswert.

### B. Antraege

Klassischer Antrag-Block; je nach Verfahrenstyp:

- Leistungsantrag (zu zahlen, zu unterlassen, zu beseitigen, herauszugeben).
- Feststellungsantrag (Feststellungsinteresse darlegen).
- Gestaltungsantrag (Aufhebung, Anfechtung, Scheidung).
- Hilfsantraege staffeln (von eng nach weit oder von hoch nach niedrig).

### C. Tatsachenvortrag

Der Substantiierungs-Kern; pro Anspruchsgrundlage in §§ 1922 ff. BGB, FamFG, ErbStG, BeurkG eine eigene Tatsachen-Sequenz:

1. **Sachverhalts-Chronologie** mit konkreten Daten (Tag, Uhrzeit, Ort, Personen).
2. **Mandantenseitige Tatsachenbehauptungen** mit Beweisangeboten.
3. **Gegnerisches Verhalten** mit Belegen (Schreiben, Aussage, Verhalten).
4. **Schaden/Folgen** bezifferbar (Hauptforderung, Nebenforderung, Zinsen, Folgekosten).

### D. Rechtliche Wuerdigung

Anspruchsaufbau klassisch:

1. **Anspruchsgrundlage** nennen (z.B. § X iVm § Y).
2. **Tatbestandsmerkmale** durchgehen; jedes Merkmal wird gegen den Tatsachenvortrag gespiegelt.
3. **Einwendungen** der Gegenseite vorwegnehmen und entkraeften.
4. **Rechtsprechungs-Verweise:** BAG/BGH/BVerfG/EuGH/BFH je nach Fachgebiet; bei Erb- und Pflichtteilsrecht typischerweise die letzte hoechstrichterliche Linie zitieren.
5. **Subsumtion-Ergebnis** klar formulieren.

### E. Beweisangebote

Pflichtbestandteil, ohne den Substantiierung nicht ausreicht:

- Urkundenbeweis: konkrete Anlage Kxx benennen, Inhalt nicht nur "Vertrag" sondern "Vertrag vom TT.MM.JJJJ, dort § X Abs. Y, Anlage K1".
- Zeugenbeweis: Name, ladungsfaehige Anschrift, Beweisthema in einem Satz.
- Sachverstaendigenbeweis: ggf. Privatgutachten mit anfuegen, gerichtliches Gutachten beantragen.
- Parteivernehmung als letzte Stufe, mit Antrag § 448 ZPO und Indiziengeruest.
- Inaugenscheinnahme: bei Sache vor Ort (Mietraum, Baustelle, Fahrzeug, Hardware).

### F. Anlagenverzeichnis

- K1, K2 ... durchnummeriert (Antragstellerin/Klaegerin).
- Bei Beklagten B1, B2 ...
- Jede Anlage mit Datum, Absender, Empfaenger, Inhaltsbeschreibung in einem Satz.
- Pflicht-Erwaehnung im Tatsachenvortrag.

## Substantiierungs-Fallen im Erb- und Pflichtteilsrecht

- **Pauschaltatsachen** ohne konkrete Daten ("seit Jahren", "regelmaessig", "in mehreren Faellen") werden vom Gericht uebergangen.
- **Beweisangebot zur falschen Tatsache:** Beweisthema deckt nur Teilaussage ab.
- **Selbst-widersprueche** zwischen Schriftsatz und Anlage ("Im Vertrag steht doch was anderes").
- **Verspaeteter Vortrag** § 296 ZPO/§ 87b VwGO: Rueglich-Fristen beachten, Verschulden vermeiden.
- **Anspruchskonkurrenz** zwischen mehreren Grundlagen: nicht eine wegfallen lassen.

## Pruefkette vor Versand

1. Antragsformulierung tenoriert (urteilstauglich, vollstreckbar)?
2. Jede Tatbestandsmerkmal-Subsumtion mit eigener Tatsache + Beweis hinterlegt?
3. Frist eingehalten (Eingangsstempel/elektronische Uebermittlung)?
4. Zuständigkeit positiv festgestellt?
5. Streitwert plausibel, ggf. mit Anlage Streitwert-Berechnung?
6. Anlagenverzeichnis vollstaendig und nummerisch konsistent?
7. beA-/EGVP-/EBO-Konformitaet (PDF/A, ERVV-Signatur)?
8. Vier-Augen-Pruefung durch Sozius oder Senior-Anwaeltin?

## Rechtsprechungs-Werkzeugkasten

- BVerfG, BGH, BAG, BFH, BVerwG, EuGH und die jeweils massgeblichen Fachsenate für Erb- und Pflichtteilsrecht.
- §§ 1922 ff. BGB, FamFG, ErbStG, BeurkG sowie Verordnungen/Richtlinien dazu.
- Aktuelle Reform- und Gesetzgebungslage einbeziehen.

## Pflicht-Output

1. **Schriftsatz** mit Rubrum, Antraegen, Tatsachenvortrag, Rechtsausfuehrung, Beweisangeboten, Anlagenverzeichnis.
2. **Anlagen-Konvolut** numerisch geordnet, jede Anlage einzeln benannt.
3. **Frist-Doku** mit Eingangsbestaetigung (beA-Eingangsnachricht, EB).
4. **Streitwertskizze** (eigenes Memo, falls > 1 Anspruch).
5. **Mandanten-Erinnerung** mit Naechster-Schritt-Aufgaben (Zeuginnen vorbereiten, Sachverstaendiger?).

## Beispiel-Anspruchsgrundlagen im Erb- und Pflichtteilsrecht

Drei haeufig gebrauchte Anspruchsgrundlagen aus §§ 1922 ff. BGB, FamFG, ErbStG, BeurkG und ihre Substantiierungs-Anforderungen:

### Grundlage 1

- Tatbestandsmerkmal 1: konkrete Tatsache + Beweis.
- Tatbestandsmerkmal 2: konkrete Tatsache + Beweis.
- Tatbestandsmerkmal 3: konkrete Tatsache + Beweis.
- Rechtsfolge: konkreter Antrag.

### Grundlage 2

Analog - jede Tatsache braucht ein Beweisangebot.

### Grundlage 3 (Auffanggrundlage / Sekundaeranspruch)

Hilfsweise vortragen, klar als Hilfsantrag/Hilfsvortrag kennzeichnen.

## Antrags-Muster nach Verfahrenstyp

Typische Antraege in Erb- und Pflichtteilsrecht (Pflichtteilsklage, Erbschein-Antrag/Beschwerde, Erbenfeststellungsklage):

- Hauptantrag (Leistung/Feststellung/Gestaltung).
- Hilfsantrag (z.B. für den Fall, dass Hauptforderung verjaehrt ist).
- Annex-Antraege (Zinsen, Nebenforderungen, Kosten).
- Streitwert-Antrag (falls Streitwert streitig).

## Beweisaufnahme - was das Gericht sehen will

### Urkundenbeweis

- Anlage K1: Bezeichnung, Datum, kurze Inhaltsbeschreibung.
- Im Tatsachenvortrag: "Diese Behauptung beruht auf dem als Anlage K1 vorgelegten Schreiben der Beklagten vom TT.MM.JJJJ, dort Seite Y, Absatz Z."

### Zeugenbeweis

- Form: "Beweis: Aussage der Zeugin Name, ladungsfaehige Anschrift, zum Beweisthema (konkret in einem Satz)."
- Mehrere Zeuginnen zum gleichen Thema: Indiziengeruest staerken.
- Keine Beweisermittlung ueber Zeugnis - das Beweisthema muss konkret sein.

### Sachverstaendigenbeweis

- Bei Erb- und Pflichtteilsrecht-typischen Streitfaellen oft notwendig (Bauwerk, IT-System, Anlagebewertung, medizinische Frage).
- Privatgutachten als Anlage K vorlegen + zugleich gerichtliches Gutachten beantragen.
- Verfahrensoekonomie: Sachverstaendigen-Kosten frueh mit Mandantin besprechen.

### Parteivernehmung (§ 448 ZPO)

- Letzte Stufe, nur wenn andere Beweismittel ausgeschoepft.
- Indiziengeruest vortragen, das eine gewisse Wahrscheinlichkeit der Behauptung tragt.

## Replik-/Duplik-Vorausschau

Schon im Klageschriftsatz die wahrscheinlichen Einwaende der Gegenseite vorwegnehmen:

- Verjährung -> Hemmungstatbestand vortragen.
- Erfuellung/Aufrechnung -> rechtzeitige Tatsachenbasis schaffen.
- Formmangel -> Heilung/Schutz-Argument bereit halten.
- Treuwidrigkeit -> Indiziengeruest gegen Treuwidrigkeits-Vorwurf.

## Elektronische Einreichung (beA, EGVP, EBO, ELSTER)

- PDF/A-2 oder PDF/A-3, mit eingebetteten Schriften.
- Strukturdatensatz nach ERVV pflicht-konform (Sender, Empfaenger, Az., Versanddatum).
- Qualifizierte elektronische Signatur (qeS) der einreichenden RA-Person oder einfacher elektronischer Versand ueber beA (sicherer Uebermittlungsweg).
- Eingangsbestaetigung aufbewahren - Datum der Einreichung ist Fristwahrungs-Beweis.
- 1.10.2026 / 1.10.2027 - ZVollstrDigitG-Aenderungen im Vollstreckungsbereich; in Erb- und Pflichtteilsrecht ggf. spezifische ERV-Pflichten beachten.

## Schriftsatz-Stil

- Aktiv, kurze Saetze, klare Subsumtion.
- Keine Floskeln ("Die Klage ist zulaessig und begruendet" als Ueberschrift, aber dann substantiieren).
- Mandanten- und Beweismittel-Zitate woertlich, in Anfuehrungszeichen, mit Anlage-Verweis.
- Keine Gefuehlsausbrueche - sachlich auch bei provokanter Gegenseite.

## Vier-Augen-Check

Vor Versand:

- [ ] Antrag tenorierungsfaehig
- [ ] Frist gewahrt mit Reserve
- [ ] Jede Tatsache hat Beweis
- [ ] Anlagen vollstaendig und nummeriert
- [ ] Rechtsprechungs-Zitat aktuell
- [ ] Streitwert plausibel
- [ ] beA/EGVP-konform
- [ ] Senior-/Sozius-Freigabe

## Cross-Refs

- `erstgespraech-mandatsannahme` (im selben Plugin) für die Tatsachen-Grundlage und Streitwertskizze.
- `vergleichsverhandlung-strategie` (im selben Plugin) für parallelen Vergleichsversuch (Gueteverhandlung, Mediation).

## 3. `spezial-belegmatrix-sonderfall-und-edge-case`

**Fokus:** Belegmatrix: Sonderfall und Edge-Case-Prüfung im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

### Belegmatrix: Sonderfall und Edge-Case-Prüfung

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Belegmatrix: Sonderfall und Edge-Case-Prüfung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: Belegmatrix: Sonderfall und Edge-Case-Prüfung
- **Normen-/Quellenanker:** BGB, EU, ErbVO.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Belegmatrix** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
