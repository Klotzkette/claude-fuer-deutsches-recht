---
name: fachanwalt-erbrecht-pflichtteilsberechnung
description: "Pflichtteilsanspruch berechnen wenn Erblasser nahe Angehoerige vom Erbe ausgeschlossen hat. §§ 2303 2311 2314 BGB Pflichtteil. Prüfraster: Pflichtteilsberechtigter Nachlasswert Bewertung Auskunftsanspruch Ergaenzungsanspruch Abzuege. Output: Pflichtteilsberechnung Auskunftsklage-Entwurf. Abgrenzung: nicht für Pflichtteilsergaenzungsanspruch (fachanwalt-erbrecht-pflichtteilsergaenzung-2325)."
---

# Pflichtteilsberechnung — Auskunft und Stufenklage

## Mandantenfragen beim Kaltstart

1. Wer ist der Erblasser, wann ist der Erbfall eingetreten und wo war der letzte gewöhnliche Aufenthalt?
2. In welchem Verhältnis steht der Mandant zum Erblasser (Abkömmling, Ehegatte, Elternteil)? Wurde er durch Testament oder Erbvertrag enterbt oder mit weniger als der Hälfte des gesetzlichen Erbteils bedacht?
3. Wer sind die übrigen pflichtteilsberechtigten und erbenden Personen? Gibt es Adoptivkinder, Stiefkinder, Halbgeschwister?
4. Hat der Erblasser in den letzten zehn Jahren vor dem Erbfall Schenkungen oder gemischte Schenkungen getätigt (Pflichtteilsergänzung § 2325 BGB)?
5. Liegt das Bestandsverzeichnis nach § 2314 BGB schon vor oder muss es erst eingefordert werden?
6. Haben die Erben die Auskunft verweigert, unvollständig erteilt oder die Bewertung blockiert?
7. Ist Verjährung drohend — Erbfall + 3 Jahre Jahresende § 2332 BGB?
8. Bestehen Anzeichen für verschleierte Schenkungen (Übertragungen unter Nießbrauch, Schenkungen an Lebensgefährten)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| § 2303 BGB | Pflichtteil als Geldanspruch — Hälfte des gesetzlichen Erbteils; Pflichtteilsberechtigte |
| § 2305 BGB | Ergänzungsanspruch bei zu geringer Bedachtung |
| § 2311 BGB | Bewertungsstichtag — Todestag; maßgeblicher Verkehrswert |
| § 2314 BGB | Auskunftsanspruch — Bestandsverzeichnis; SV-Bewertung auf Verlangen; Kosten trägt Nachlass |
| § 2315 BGB | Anrechnung von Vorausempfängen mit Anrechnungsbestimmung |
| § 2316 BGB | Ausgleichung unter Abkömmlingen |
| § 2325 BGB | Pflichtteilsergänzung — Schenkungen letzter 10 Jahre; 10 %-Abschmelzung je Jahr |
| § 2327 BGB | Anrechnung Eigengeschenke des Pflichtteilsberechtigten |
| § 2329 BGB | Direktanspruch gegen Beschenkte wenn Nachlass insufficient |
| § 2332 BGB | Verjährung — 3 Jahre ab Kenntnis; 30 Jahre absolut § 199 Abs. 3a BGB |

## Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---------|-------------|-------|-------------|
| BGH IV. Zivilsenat | IV ZR 88/24 | 12.03.2025 | Für die Entstehung des Pflichtteilsanspruchs nach § 199 Abs. 1 Nr. 1 BGB ist § 2317 Abs. 1 BGB auch dann maßgebend, wenn der Berechtigte zum Zeitpunkt des Erbfalls aufgrund der gesetzlichen Ausübungssperre in § 1600d Abs. 5 BGB an einer erfolgreichen Anspruchsdurchsetzung gehindert ist (nichteheliches Kind, Vaterschaftsfeststellung). Quelle: bundesgerichtshof.de bzw. dejure.org. |
| BGH IV. Zivilsenat | IV ZR 93/24 | 02.07.2025 | Eine Zuwendung von Todes wegen an den behandelnden Arzt des Erblassers ist nicht deshalb unwirksam, weil sie gegen ein berufsständisches Zuwendungsverbot der ärztlichen Berufsordnung (§ 32 Abs. 1 S. 1 BO) verstößt. Berufsrecht ist kein Verbotsgesetz i.S.d. § 134 BGB; Testierfreiheit (Art. 14 GG) überwiegt. Sittenwidrigkeit (§ 138 BGB) bleibt Einzelfallprüfung. Quelle: bundesgerichtshof.de Pressemitteilung 122/2025. |
| Weitere Rechtsprechung | Live-Verifikation erforderlich | - | keine weitere Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema — Stufenweise Durchsetzung

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.


| Phase | Schritt | Maßnahme | Norm |
|-------|---------|---------|------|
| Vorbereitung | 1 | Pflichtteilsberechtigung feststellen | § 2303 BGB |
| Vorbereitung | 2 | Erbquote + Pflichtteilsquote berechnen | §§ 1924 ff., 2303 BGB |
| Auskunft | 3 | Auskunftsschreiben § 2314 BGB senden | § 2314 Abs. 1 BGB |
| Auskunft | 4 | Frist setzen: 4 Wochen; notarielles Verzeichnis fordern | § 2314 Abs. 1 Satz 3 BGB |
| Auskunft | 5 | SV-Bewertung fordern für Immobilien/Unternehmen | § 2314 Abs. 1 Satz 2 BGB |
| Klage | 6 | Stufenklage erheben wenn Auskunft verweigert/unvollständig | § 254 ZPO |
| Klage | 7 | Auskunftsstufe — Verzeichnis vollständig einholen | Stufe 1 |
| Klage | 8 | Versicherungsstufe — eidesstattliche Versicherung | Stufe 2 |
| Klage | 9 | Zahlungsstufe — Pflichtteilsbetrag beziffern und einklagen | Stufe 3 |
| Sicherung | 10 | Direktanspruch § 2329 BGB gegen Beschenkte | § 2329 BGB |

## Bestandsverzeichnis § 2314 BGB — Auskunftsinhalt

Das Bestandsverzeichnis muss enthalten:

**Aktiva:**
- Alle Bankkonten und Wertpapierdepots (Saldo Todestag)
- Immobilien (Grundstücksbezeichnung, Grundbuchauszug, Wertangabe)
- Unternehmensbeteiligungen mit Gesellschaftsvertrag und Bewertung
- Krypto-Assets und digitale Vermögenswerte
- Hausrat, Fahrzeuge, Schmuck
- Lebensversicherungen (Rückkaufswert, Bezugsberechtigte)
- Offene Forderungen, Darlehen an Dritte

**Passiva:**
- Verbindlichkeiten Kreditinstitute
- Steuerschulden (Einkommensteuer, Grundsteuer)
- Unterhaltsverpflichtungen
- Beerdigungskosten § 1968 BGB
- Sonstige Verbindlichkeiten

**Schenkungen:**
- Alle Schenkungen letzter 10 Jahre § 2325 BGB
- Gemischte Schenkungen (Kaufpreis erheblich unter Verkehrswert)
- Schenkungen unter Nießbrauchsvorbehalt
- Schenkungen an Ehegatten (unbegrenzte Frist!)

**Ausgleichungen:**
- Vorausempfänge mit Anrechnungsbestimmung § 2315 BGB
- Ausgleichungspflichtige Zuwendungen § 2316 BGB

## Berechnungsschema

```
PFLICHTTEILSBERECHNUNG

Schritt 1: Nettonachlass
   Aktiva zum Todestag:              EUR [A]
 - Erblasserschulden:                EUR [B]
 - Beerdigungskosten:                EUR [C]
 = Nettonachlass:                    EUR [D]

Schritt 2: Ergänzungsmasse § 2325 BGB
   Schenkung 1 [Datum]:
   Nominalwert / bereinigter Wert:   EUR [X]
   Abschmelzung [Y]%:                EUR [Z] (= Ansatz)
   
   Schenkung 2 [Datum]:
   Niederstwertvergleich:
     Bereinigter Schenkungswert:     EUR [X1]
     Erbfall-Wert:                   EUR [X2]
     Anzusetzender Wert:             EUR [min(X1,X2)]
   Abschmelzung [Y]%:                EUR [Z2]
   
   Summe Ergänzungsmasse:            EUR [E]

Schritt 3: Pflichtteilsquote
   Gesetzlicher Erbteil:             [X/Y]
   Pflichtteilsquote:                [X/2Y]

Schritt 4: Pflichtteil
   Nettonachlass × Quote:            EUR [F]

Schritt 5: Pflichtteilsergänzung
   Ergänzungsmasse × Quote:          EUR [G]

Schritt 6: Anrechnung § 2315 BGB
   Vorausempfang mit Anrechnung:   - EUR [H]

Schritt 7: Anrechnung Eigengeschenk § 2327 BGB
   Erhaltene Schenkung vom Erblasser:- EUR [I]

GESAMT-PFLICHTTEILSANSPRUCH:         EUR [F+G-H-I]
Zinsen § 291 BGB ab Klagezustellung:  Basiszins + 5 %
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Pflichtteil berechnen und durchsetzen | Stufenklage-Bausteine unten; Auskunft zuerst |
| Variante A — Erbe zahlt freiwillig wenn Berechnung klar | Aussergerichtliche Geltendmachung zuerst; Klage als Backup |
| Variante B — Erblasser hat viel verschenkt | Pflichtteilsergaenzung § 2325 BGB pruefen; 10-Jahres-Frist |
| Variante C — Stufenklage zu aufwaendig | Direktklage auf Zahlung wenn Grundlage klar; Auskunft nachfassen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatz-Bausteine

### Auskunftsanforderung § 2314 BGB

```
An die Erben nach [Name Erblasser]
[Adresse]

Auskunfts- und Wertermittlungsanspruch nach § 2314 BGB

Sehr geehrte Damen und Herren,

namens und in Vollmacht unseres Mandanten — [Name] als
Pflichtteilsberechtigter nach dem am [Datum] verstorbenen
[Erblasser] — fordern wir Sie auf, binnen vier Wochen
ein notarielles Nachlassverzeichnis nach § 2314 Abs. 1
Satz 3 BGB vorzulegen.

Das Verzeichnis muss enthalten:
1. Sämtliche Aktiva und Passiva des Nachlasses zum Todestag
   [Datum], bewertet nach §§ 2311, 2311a BGB
2. Sämtliche Schenkungen des Erblassers der letzten zehn
   Jahre nach § 2325 BGB (auch gemischte Schenkungen,
   Schenkungen unter Nießbrauchsvorbehalt, Schenkungen
   an den Ehegatten ohne zeitliche Begrenzung)
3. Ausgleichungspflichtige Zuwendungen nach §§ 2315,
   2316 BGB

Hinsichtlich der Bewertung von Immobilien und
Unternehmensbeteiligungen verlangen wir bereits jetzt
die Hinzuziehung eines vereidigten Sachverständigen
nach § 2314 Abs. 1 Satz 2 BGB.
Die Kosten trägt der Nachlass (§ 2314 Abs. 2 BGB).

Nach fruchtlosem Fristablauf werden wir Stufenklage
nach § 254 ZPO erheben.

Mit freundlichen Grüßen
[Kanzlei]
```

### Stufenklage § 254 ZPO

```
[Landgericht / Amtsgericht]
Abteilung: [Kammer]

Klage

Kläger: [Name, Adresse] — Pflichtteilsberechtigter
Beklagte: [Namen, Adressen] — Erben

wegen: Pflichtteil (Stufenklage § 254 ZPO)

I. AUSKUNFTSSTUFE
   Die Beklagten werden als Gesamtschuldner verurteilt,
   durch Vorlage eines notariellen Nachlassverzeichnisses
   Auskunft über den Bestand des Nachlasses nach
   [Erblasser] zum Todestag [Datum] zu erteilen,
   einschließlich aller Schenkungen der letzten zehn Jahre
   nach § 2325 BGB.

II. VERSICHERUNGSSTUFE
   Die Beklagten werden als Gesamtschuldner verurteilt,
   die Richtigkeit des vorgelegten Verzeichnisses
   an Eides statt zu versichern.

III. ZAHLUNGSSTUFE
   Die Beklagten werden als Gesamtschuldner verurteilt,
   an den Kläger den sich aus der Auskunft ergebenden
   Pflichtteilsanspruch nebst Zinsen in Höhe von fünf
   Prozentpunkten über dem Basiszinssatz ab
   Klagezustellung zu zahlen.

IV. STREITWERT AUSKUNFTSSTUFE
   25 % des voraussichtlichen Hauptanspruchs.
   Vorläufiger Streitwert: EUR [Betrag].
```

### Direktanspruch gegen Beschenkte § 2329 BGB

```
An [Beschenkter]
[Adresse]

Pflichtteilsergänzungsanspruch nach § 2329 BGB

Sehr geehrte Damen und Herren,

unser Mandant ist Pflichtteilsberechtigter nach dem
am [Datum] verstorbenen [Erblasser].

Der Erblasser hat Ihnen am [Datum] folgende Schenkung
gemacht: [Beschreibung, Wert].

Der Nachlass reicht zur Erfüllung des Pflichtteilsergänzungs-
anspruchs unseres Mandanten nicht aus. Nach § 2329 BGB
kann unser Mandant von Ihnen als Beschenktem Ergänzung
bis zum Wert der Schenkung verlangen.

Betrag: EUR [Pflichtteilsergänzungsanspruch], begrenzt auf
Schenkungswert EUR [Betrag].

Wir fordern Sie auf, bis [Datum] zu zahlen.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Beweislast

| Partei | Beweislastgegenstand | Beweismittel |
|--------|---------------------|--------------|
| Pflichtteilsberechtigter | Berechtigung | Geburtsurkunde, Heiratsurkunde, ggf. Adoptionsurkunde |
| Pflichtteilsberechtigter | Enterbung oder Unterbedachtung | Testament, Erbschein |
| Pflichtteilsberechtigter | Schenkungen § 2325 BGB | Notarverträge, Kontobewegungen, Grundbuchauszüge |
| Erbe | Anrechnungsbestimmung § 2315 BGB | Schriftliche Vereinbarung mit Anrechnungsvorbehalt |
| Erbe | Pflichtteilsverzicht § 2346 BGB | Notarielle Urkunde |
| Erbe | Vollständigkeit und Richtigkeit Bestandsverzeichnis | Eidesstattliche Versicherung Stufe 2 |

## Fristen

| Frist | Auslöser | Dauer | Folge |
|-------|---------|-------|-------|
| Auskunftsanforderung | Möglichst bald nach Erbfall | Praxis: 4 Wochen setzen | Bei Ablehnung: Stufenklage |
| Verjährung Pflichtteil § 2332 BGB | Kenntnis von Erbfall + Verfügung | 3 Jahre ab Jahresende | Anspruchsverlust |
| Absolute Verjährung | Erbfall | 30 Jahre § 199 Abs. 3a BGB | Anspruchsverlust |
| Direktanspruch § 2329 BGB | Schenkungsdatum | 3 Jahre ab Kenntnis | Verjährung gegen Beschenkten |

## Gegenargumente und Reaktion

| Gegenargument Erbe | Reaktion |
|-------------------|---------|
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Nachlass wertlos, kein Pflichtteil" | Ergänzungsanspruch gegen Beschenkte § 2329 BGB; Nachlasswert ≠ Ergänzungsbasis |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Privatverzeichnis reicht" | § 2314 Abs. 1 Satz 3 BGB: auf Verlangen notarielles Verzeichnis; kein Ermessen |

## Streitwert und Kosten

**Streitwert Auskunftsstufe:** 25 % des voraussichtlichen Hauptanspruchs (Praxis der meisten Gerichte)

**Streitwert Zahlungsstufe:** Bezifferter Pflichtteilsanspruch

**Gerichtsgebühren Beispiel EUR 50.000:**
- Auskunftsstufe EUR 12.500 → GKG 3.0 Gebühr ca. EUR 618
- Zahlungsstufe EUR 50.000 → GKG ca. EUR 1.638
- RA-Gebühren: je Partei ca. EUR 3.500–5.500

**SV-Gutachten:** Auf Nachlasskosten § 2314 Abs. 2 BGB — typisch EUR 2.000–6.000 je Immobilie

## Strategische Empfehlung

| Strategie | Empfehlung | Begründung |
|-----------|-----------|------------|
| Verjährungssicherung | Auskunftsschreiben noch vor Ablauf von 2.5 Jahren nach Erbfall | Verjährung droht; Stufenklage hemmt § 204 BGB |
| Notarielles Verzeichnis | Konsequent fordern | Beweiskraft höher; Erbe haftet für Vollständigkeit |
| SV direkt benennen | Bereits im Auskunftsschreiben | Verhindert Verzögerung durch Erben |
| Schenkungsrecherche | Kontoauszüge 10+ Jahre rückwärts | Verschleierte Schenkungen häufig |
| Direktanspruch § 2329 | Beschenkte frühzeitig in Haftung nehmen | Schutz bei Nachlass-Insolvenz |

## Anschluss-Skills

- `pflichtteil-berechnen` — vollständiges Berechnungsraster mit allen Schritten
- `nachlassinsolvenz-erbenhaftung-begrenzen` — wenn Nachlass überschuldet
- `fachanwalt-erbrecht-testamentsvollstreckung` — TV-Auskunftspflicht § 2218 BGB

## Quellen

- BGB §§ 2303–2332, 2314, 2325, 2329, 2332
- ZPO § 254
- BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteilsanspruch nichteheliches Kind; Verjährung): dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=12.03.2025&Aktenzeichen=IV+ZR+88/24
- BGH, Urteil vom 02.07.2025 - IV ZR 93/24 (Zuwendung an Hausarzt; Berufsordnung kein § 134 BGB-Verbot): bundesgerichtshof.de Pressemitteilung 2025/2025122.html
- Weitere Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesgerichtshof.de, dejure.org, openjur.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Stand: 05/2026
