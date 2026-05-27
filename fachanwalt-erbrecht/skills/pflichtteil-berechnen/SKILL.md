---
name: pflichtteil-berechnen
description: "Pflichtteilsanspruch und Pflichtteilsergaenzungsanspruch berechnen. §§ 2303 2311 2325 BGB Pflichtteil. Pruefraster: Pflichtteilsquote Nachlasswert Bewertungsstichtag Abzuege Ergaenzungsanspruch Auskunft. Output: Pflichtteilsberechnung mit Rechenweg. Abgrenzung: nicht fuer Auskunftsklage oder Pflichtteilsklage (schriftsatzkern-substantiierung)."
---

# Pflichtteil und Pflichtteilsergänzung berechnen

## Mandantenfragen beim Kaltstart

1. Wer ist der Erblasser und wann ist der Erbfall eingetreten? Letzter gewöhnlicher Aufenthalt (Gerichtsstand)?
2. In welchem Verhältnis steht der Mandant zum Erblasser — Abkömmling, Ehegatte, Elternteil? Durch Testament oder Erbvertrag enterbt oder zu wenig bedacht?
3. Wer sind die übrigen Pflichtteilsberechtigten und die eingesetzten Erben?
4. Hat der Erblasser Schenkungen in den letzten 10 Jahren getätigt (§ 2325 BGB)? An wen und in welcher Höhe?
5. Liegt ein Bestandsverzeichnis nach § 2314 BGB vor oder muss es erst eingefordert werden?
6. Gibt es Vorausempfänge des Pflichtteilsberechtigten mit Anrechnungsbestimmung (§ 2315 BGB)?
7. Hat der Pflichtteilsberechtigte einen Pflichtteilsverzicht erklärt (§ 2346 BGB)?
8. Besteht ein Pflichtteilsentzugsgrund nach § 2333 BGB (Straftat gegen Erblasser, Erblasser-nahe Personen)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

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
| BGH | IV ZR 132/13 | 23.07.2014 | Schenkung an Ehegatten — 10-Jahres-Frist beginnt nicht vor Auflösung der Ehe (nicht Todestag) |
| BGH | IV ZR 138/14 | 29.04.2015 | Schenkung unter Nießbrauchsvorbehalt — Frist beginnt nicht vor tatsächlichem Erlöschen des Nießbrauchs |
| BGH | IVa ZR 85/88 | 19.04.1989 | Niederstwertprinzip § 2325 Abs. 2 BGB bei nicht verbrauchbaren Sachen (insb. Immobilien) |
| BGH | IV ZR 259/92 | 02.06.1993 | Bewertung nicht verbrauchbarer Sachen: Inflationsbereinigung des Schenkungswerts vs. Wert zum Erbfall |
| BGH | IV ZR 232/12 | 16.01.2013 | Verjährung § 2332 BGB — einheitlicher Anspruch; keine neue Verjährung für erst später bekannte Nachlassgegenstände |
| BGH | IV ZR 211/00 | 07.03.2001 | Pflichtteilsentzug § 2333 BGB — enge Auslegung; nur schwere Verfehlungen; Beweislast beim Erben |
| OLG Frankfurt | 20 W 350/14 | 21.08.2015 | Unternehmensbewertung als Nachlassgegenstand — IDW S1 oder vereinfachtes Ertragswertverfahren |

## Prüfschema — Stufenweise Pflichtteilsberechnung

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.


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
| Krypto-Assets | Börsenkurs Todestag (FG Köln 14 K 1212/20) |
| Hausrat | Zeitwert (geschätzt) |
| Lebensversicherung | Rückkaufswert (soweit keine Drittbegünstigung) |

### Passiva

| Verbindlichkeit | Abzugsfähig |
|----------------|------------|
| Erblasser-Schulden (Kredit, Steuern, Unterhalt) | Ja |
| Beerdigungskosten § 1968 BGB | Ja |
| Pflegekosten letzte Lebensjahre | Ja (soweit nicht bereits bezahlt) |
| Erbschaftsteuer | Nein (BGH IV ZR 132/76) |
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

- 10-Jahres-Frist beginnt **nicht** vor Auflösung der Ehe (BGH IV ZR 132/13)
- Schenkung an Ehegatte vor 30 Jahren ist relevant wenn Ehe bei Tod noch bestand

### Ausnahme: Schenkung unter Nießbrauchsvorbehalt

- 10-Jahres-Frist beginnt **nicht** vor tatsächlichem Erlöschen des Nießbrauchs (BGH IV ZR 138/14)
- Erblasser verschenkt Immobilie aber behält lebenslangen Nießbrauch → Frist ab Tod/Aufgabe Nießbrauch

### Bewertung der Schenkung § 2325 Abs. 2 BGB

| Sachtyp | Bewertungsregel |
|---------|----------------|
| Geld, Wertpapiere (verbrauchbar) | Wert zum Schenkungszeitpunkt |
| Immobilien, Unternehmen (nicht verbrauchbar) | **Niederstwertprinzip** — niedrigerer Wert von inflationsbereinigtem Schenkungswert vs. Wert zum Erbfall (BGH IVa ZR 85/88) |

**Inflationsbereinigung:** Schenkungswert × (Verbraucherpreisindex Todestag / Verbraucherpreisindex Schenkungstag)

## Berechnungsformel (Gesamtübersicht)

```
PFLICHTTEILSBERECHNUNG

I. Nettonachlass
   Aktiva zum Todestag:                    EUR [A]
 - Passiva:                                EUR [B]
 = Nettonachlass:                          EUR [C]

II. Pflichtteilsergänzung (Schenkungen)
   Schenkung Nr. 1 vom [Datum]:
     Wert (nicht verbrauchbar — Niederstwert): EUR [X]
     Abschmelzung [X]%:                     EUR [Y]
   Schenkung Nr. 2 vom [Datum]:
     Wert (verbrauchbar — Nominalbetrag):    EUR [X]
     Abschmelzung [X]%:                     EUR [Y]
   Summe Ergänzungsmasse:                   EUR [D]

III. Berechnungsbasis
   Nettonachlass + Ergänzungsmasse:         EUR [C+D]

IV. Pflichtteilsquote: [X/Y] (z.B. 1/8)

V. Pflichtteilsanspruch:
   Nettonachlass × Quote:                  EUR [P1]
   Ergänzungsanspruch:
   Ergänzungsmasse × Quote:                EUR [P2]
   Gesamt (vor Anrechnung):                EUR [P1+P2]

VI. Anrechnung § 2315 BGB (Vorausempfang):  EUR [minus A]
   Gesamt-Pflichtteilsanspruch:            EUR [Summe]
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
| „Schenkung älter als 10 Jahre" | Ehegattenschenkung-Sonderregel § 2325 Abs. 3 BGB; Nießbrauch-Vorbehalt (BGH IV ZR 138/14); genaue Fristberechnung |
| „Pflichtteilsverzicht liegt vor" | Prüfen ob notarielle Form § 2346 BGB gewahrt; Anfechtung wegen Irrtum/Täuschung § 2351 BGB |
| „Pflichtteilsentzug angeordnet" | Enge Auslegung § 2333 BGB; Beweislast beim Erben (BGH IV ZR 211/00) |
| „Vorausempfang anzurechnen" | Anrechnungsbestimmung schriftlich vereinbart? § 2315 BGB; nur bei ausdrücklicher Anrechnung |
| „Nachlasswert überhöht bewertet" | Eigene SV-Bewertung; Niederstwertprinzip bei nicht verbrauchbaren Sachen |

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
- BGH IV ZR 132/13 (23.07.2014); IV ZR 138/14 (29.04.2015)
- BGH IVa ZR 85/88 (19.04.1989); IV ZR 259/92 (02.06.1993)
- BGH IV ZR 232/12 (16.01.2013)
- MüKoBGB / Lange § 2303 ff.
- BeckOK BGB Erbrecht
- Burandt/Rojahn Erbrecht
- Stand: 05/2026
