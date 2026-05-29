---
name: fachanwalt-handels-gesellschaftsrecht-handelsvertreterausgleich
description: "Workflow-Skill zu fachanwalt handels gesellschaftsrecht handelsvertreterausgleich. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen."
---

## Mandantenfragen beim Kaltstart

1. Wann endete das Handelsvertreterverhältnis, und wer hat es beendet (Eigenkündigung des Handelsvertreters, Kündigung des Unternehmens, einvernehmliche Aufhebung, Tod)?
2. Hat der Handelsvertreter neue Kunden geworben oder bestehende Geschäftsverbindungen wesentlich erweitert, und erzielen diese Kunden nach Vertragsende weiterhin Umsätze beim Unternehmer?
3. Wie hoch waren die Provisionen der letzten 5 Vertragsjahre (Jahresvergütungen für § 89b Abs. 2 HGB-Höchstgrenze)?
4. Wurde der Ausgleichsanspruch innerhalb eines Jahres nach Vertragsende schriftlich geltend gemacht (§ 89b Abs. 4 S. 2 HGB)?
5. Liegt ein schriftlicher Handelsvertretervertrag mit Ausgleichs-, Wettbewerbs- oder Karenzklauseln vor?
6. Liegt ein Ausschlussgrund vor — Eigenkündigung ohne wichtigen Grund, Kündigung des Unternehmers aus schuldhaftem Verhalten des Handelsvertreters, Übernahme durch Dritten mit Vereinbarung?
7. Handelt es sich ggf. um einen Vertragshändler oder Franchisenehmer (analoge Anwendung § 89b HGB)?
8. Welche Sogwirkung hat die Marke des Unternehmers gehabt — stark oder schwach — relevant für Billigkeitskorrektur?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| § 89b Abs. 1 HGB | Ausgleichsanspruch: (1) Unternehmervorteile aus neuen Kunden, (2) Provisionsverluste des HV, (3) Billigkeit |
| § 89b Abs. 2 HGB | Höchstgrenze: Durchschnitt der letzten 5 Jahresvergütungen; bei kürzerer Vertragsdauer: Gesamtdurchschnitt |
| § 89b Abs. 3 HGB | Ausschluss: Eigenkündigung ohne wichtigen Grund; Kündigung durch Unternehmer aus schuldhaftem Verhalten; Übernahme durch Dritten |
| § 89b Abs. 4 HGB | Verzicht im Voraus unwirksam; Geltendmachung binnen 1 Jahr nach Beendigung |
| § 89b Abs. 5 HGB | Modifizierte Anwendung auf Versicherungs- und Bausparkassenvertreter |
| § 89a HGB | Kündigung aus wichtigem Grund; fristlose Kündigung |
| §§ 84 ff. HGB | Begriffsbestimmung Handelsvertreter; ständiger Betrauung; selbständiger Gewerbetreibender |
| § 92 HGB | Versicherungsvertreter; Sonderregeln |
| Richtlinie 86/653/EWG | Handelsvertreter-RL; europarechtskonforme Auslegung § 89b HGB zwingend (EuGH Semen) |
| § 288 Abs. 2 BGB | Verzugszinsen 9 Prozentpunkte über Basiszinssatz bei Unternehmern |

## Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---------|-------------|-------|-------------|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Berechnungsschema Münchener Modell

| Schritt | Berechnung | Erläuterung |
|---------|-----------|-------------|
| 1 | Bruttoprovision aus Neukunden letztes Vertragsjahr | Basis für Prognose |
| 2 | Multiplikation Prognosezeitraum (3–5 Jahre) unter Berücksichtigung Abwanderungsquote (typisch 15–25 % p. a.) | Gibt Bruttoprovisionsverlust |
| 3 | Abzug verwaltende Tätigkeit (Bestandspflege, ohne Neuwerbung): 15–25 % | BGH: nur Neuwerbungsanteile maßgeblich |
| 4 | Abzinsung auf Vertragsendezeitpunkt (Basiszinssatz zzgl. Risikoaufschlag) | Barwertberechnung |
| 5 | Billigkeitskorrektur: Sogwirkung der Marke (Abschlag); Wettbewerbsverbot, Karenzentschädigung, Alter, Krankheit | Kann Ergebnis erhöhen oder senken |
| 6 | Vergleich mit Höchstgrenze § 89b Abs. 2 HGB (Durchschnitt 5-Jahres-Vergütung) | Niedrigerer Wert gilt |

### Rechenbeispiel

```
Provisionsverlust-Berechnung (Prognosezeitraum 4 Jahre, Abwanderung 20 % p. a.):

Bruttoprovision Neukunden letztes Jahr:   EUR 50.000
Jahr 1 (×80 %):                           EUR 40.000
Jahr 2 (×64 %):                           EUR 32.000
Jahr 3 (×51,2 %):                         EUR 25.600
Jahr 4 (×40,96 %):                        EUR 20.480
Bruttoprovisionsverlust gesamt:           EUR 118.080

Abzug Bestandspflege 20 %:              ./. EUR  23.616
Zwischensumme:                            EUR  94.464

Abzinsung Barwert (Faktor 0,93):          EUR  87.852

Billigkeitsabschlag Sogwirkung 15 %:    ./. EUR  13.178
Berechnetes Ergebnis:                     EUR  74.674

Höchstgrenze § 89b Abs. 2 HGB
(Ø 5 Jahresvergütungen je EUR 60.000):    EUR  60.000

Ausgleichsanspruch:                       EUR  60.000 zzgl. 19 % USt
```

## Prüfschema § 89b HGB

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.


| Schritt | Prüfpunkt | Norm | Rechtsfolge |
|---------|-----------|------|-------------|
| 1 | Handelsvertretervertrag i. S. §§ 84 ff. HGB? | § 84 HGB | Analoge Anwendung bei Vertragshändler/Franchisenehmer prüfen |
| 2 | Beendigung des Vertragsverhältnisses? | § 89b Abs. 1 HGB | Frist läuft erst ab Vertragsende |
| 3 | Neukunden geworben oder Geschäftsverbindungen wesentlich erweitert? | § 89b Abs. 1 Nr. 1 HGB | Nachweis durch Kundenlisten, Provisionsabrechnungen |
| 4 | Nachvertragliche Unternehmervorteile aus diesen Kunden? | § 89b Abs. 1 Nr. 1 HGB | Prognostische Schätzung zulässig (§ 287 ZPO) |
| 5 | Provisionsverluste des Handelsvertreters? | § 89b Abs. 1 Nr. 2 HGB | Prognose nach Abwanderungsquote; EuGH Semen: Untergrenze beachten |
| 6 | Billigkeit? | § 89b Abs. 1 Nr. 3 HGB | Sogwirkung, Wettbewerbsverbot, persönliche Umstände |
| 7 | Höchstgrenze § 89b Abs. 2 HGB? | § 89b Abs. 2 HGB | Durchschnitt letzte 5 Jahre; kürzer = Gesamtdurchschnitt |
| 8 | Ausschlussgründe § 89b Abs. 3 HGB? | § 89b Abs. 3 HGB | Eigenkündigung ohne wichtigen Grund schließt Anspruch aus |
| 9 | Jahresfrist § 89b Abs. 4 S. 2 HGB eingehalten? | § 89b Abs. 4 HGB | Versäumnis = Anspruchsverlust (materiell-rechtliche Ausschlussfrist) |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Handelsvertreterausgleich § 89b HGB berechnen und fordern | Muenchener Modell-Berechnung; Schriftsatzbausteine unten |
| Variante A — Ausgleich offensichtlich gering | Aussergerichtliche Geltendmachung; Klage bei Verweigerung |
| Variante B — Unternehmer behauptet Ausschlussgruende | Ausschlussgruende § 89b Abs. 3 HGB gegenprueefen |
| Variante C — Verjährung Jahresfrist laeuft ab | Geltendmachung unverzueglich; Frist § 89b Abs. 4 HGB wahren |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatz-Bausteine

### Geltendmachung (außergerichtlich, Jahresfrist wahrend)

```
[Briefkopf Kanzlei]                                          [Ort, Datum]

An [Unternehmensname]                             - Einschreiben/Rückschein -

Beendigung Handelsvertretervertrag vom [Datum]
Geltendmachung Ausgleichsanspruch § 89b HGB — Wahrung Jahresfrist

Sehr geehrte Damen und Herren,

unter Bezugnahme auf die anliegende Vollmacht (Anlage 1) zeige ich die
anwaltliche Vertretung des Handelsvertreters [Name] an.

Das Handelsvertreterverhältnis endete zum [Datum]. Der Ausgleichsanspruch
nach § 89b HGB ist entstanden und wird hiermit innerhalb der Jahresfrist
des § 89b Abs. 4 S. 2 HGB schriftlich geltend gemacht.

Vorläufige Berechnung (Detailberechnung folgt nach Belegübermittlung):

Bruttoprovisionen Neukunden letztes Jahr:   EUR [X]
Provisionen Ø 5 Jahre:                     EUR [X/Jahr]
Höchstgrenze § 89b Abs. 2 HGB:             EUR [X]
Vorläufiger Ausgleichsanspruch:             EUR [X] zzgl. 19 % USt

Zur Ermittlung des Ausgleichs sind wir auf die Provisionsabrechnungen und
Kundendaten der letzten 5 Vertragsjahre angewiesen. Wir bitten um deren
Übermittlung bis zum [Datum].

Nach Vorlage der Unterlagen werden wir den Anspruch beziffert geltend machen.

[Kanzlei, Fachanwalt/Fachanwältin für Handels- und Gesellschaftsrecht]
```

### Klage auf Handelsvertreterausgleich

```
An das Landgericht [Sitz des Unternehmens]
— Kammer für Handelssachen —                                 [Ort, Datum]

Klage

des [Handelsvertreter], [Anschrift]              – Kläger –
gegen
die [Unternehmensname], [Anschrift]              – Beklagte –

wegen Handelsvertreterausgleich § 89b HGB

Anträge:

1. Die Beklagte wird verurteilt, an den Kläger EUR [Betrag] nebst Zinsen
   in Höhe von neun Prozentpunkten über dem Basiszinssatz seit [Datum]
   zu zahlen.
2. Die Beklagte trägt die Kosten des Rechtsstreits.

Streitwert: EUR [Betrag].

Begründung:

I. Sachverhalt
Der Kläger war seit [Datum] als selbständiger Handelsvertreter (§ 84 HGB) für
die Beklagte tätig (Handelsvertretervertrag vom [Datum], Anlage K 1). Das
Vertragsverhältnis endete durch Kündigung der Beklagten zum [Datum] (Anlage K 2).

II. Unternehmervorteile § 89b Abs. 1 Nr. 1 HGB
Der Kläger hat [Anzahl] Neukunden akquiriert (Kundenliste Anlage K 3). Diese
Kunden erzielen mit der Beklagten nach Vertragsende erhebliche Umsätze. Die
Provisionen aus Neukundengeschäften betrugen im letzten Vertragsjahr [Jahr]
EUR [Betrag] (Provisionsabrechnungen Anlage K 4).

III. Provisionsverluste § 89b Abs. 1 Nr. 2 HGB
Berechnungsgrundlage nach Münchener Modell (Anlage K 5, Detailberechnung):
[Prognose 4 Jahre, Abwanderungsquote 20 %, Barwert, Billigkeitskorrektur].
Ergebnis: EUR [Betrag].

IV. Billigkeit § 89b Abs. 1 Nr. 3 HGB
Eine überragende Sogwirkung der Marke der Beklagten ist nicht nachweisbar.
Eine Karenzentschädigung wurde nicht gezahlt.

V. Höchstgrenze § 89b Abs. 2 HGB
Ø Jahresvergütung der letzten 5 Jahre: EUR [Betrag]/Jahr. Höchstgrenze: EUR [Betrag].
Der berechnete Ausgleich liegt [unter/über] der Höchstgrenze. Geltend gemacht
wird: EUR [Betrag].

VI. Kein Ausschlussgrund § 89b Abs. 3 HGB
Das Vertragsverhältnis wurde durch die Beklagte ordentlich gekündigt.

VII. Jahresfrist § 89b Abs. 4 S. 2 HGB
Schreiben vom [Datum] (Anlage K 6) wahrt die Jahresfrist.

[Kanzlei, Fachanwalt/Fachanwältin für Handels- und Gesellschaftsrecht]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Beweislast

| Beweisthema | Beweislast | Beweismittel |
|------------|-----------|--------------|
| Handelsvertreterstellung (§ 84 HGB) | Kläger | Handelsvertretervertrag; Gewerbeanmeldung; Provisionsabrechnungen |
| Neukunden geworben | Kläger | Kundenliste mit Erstakquise-Datum; Provisionsabrechnungen |
| Nachvertragliche Unternehmervorteile | Kläger (Prognose, § 287 ZPO) | Fortlaufende Umsätze der Neukunden nach Vertragsende |
| Eigenkündigung ohne wichtigen Grund (Ausschluss § 89b Abs. 3 Nr. 1) | Unternehmer | Kündigungsschreiben; Ursache der Kündigung |
| Schuldhaftes Verhalten des HV (§ 89b Abs. 3 Nr. 2) | Unternehmer | Abmahnungen; Protokolle; Zeugen |
| Höhe Jahresvergütung (Höchstgrenze § 89b Abs. 2) | Beide / Auskunftspflicht Unternehmer | Provisionsabrechnungen der letzten 5 Jahre |
| Sogwirkung Marke (Billigkeit) | Unternehmer (Abschlag) | Marktforschungsdaten; Markenstärkeindex |

## Fristen

| Frist | Inhalt | Norm |
|-------|--------|------|
| 1 Jahr | Geltendmachung Ausgleichsanspruch nach Vertragsende (Ausschlussfrist) | § 89b Abs. 4 S. 2 HGB |
| 6 Monate | Außerordentliche Kündigung nach § 89a HGB nach Kenntnis des wichtigen Grundes | § 89a HGB; BGH-Rspr. |
| 3 Jahre | Verjährung des bezifferten Ausgleichsanspruchs ab Fälligkeit | §§ 195, 199 BGB |
| 5 Jahre | Aufbewahrungspflicht Provisionsabrechnungen (§ 257 HGB) | § 257 HGB |

## Gegenargumente und Reaktion

| Gegenargument | Herkunft | Reaktion |
|--------------|---------|----------|
| "Eigenkündigung des HV — § 89b Abs. 3 Nr. 1 HGB" | Unternehmer | Nachweis wichtiger Grund (unzumutbares Verhalten des Unternehmers); oder Alter/Krankheit des HV |
| "Keine Neukunden geworben — nur Bestandspflege" | Unternehmer | Provisionsabrechnungen detailliert aufschlüsseln; Anteil Neukunden- vs. Bestandsprovisionen |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| "Jahresfrist versäumt" | Unternehmer | Fristenwahrung durch anwaltliches Schreiben belegen; Datum des Poststempels |
| "Kein Handelsvertreter sondern Arbeitnehmer" | Unternehmer | Selbständigkeit nach § 84 HGB: kein Weisungsrecht des Unternehmers über Arbeitszeit und -ort; Beweise für unternehmerische Freiheit |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Streitwert und Kosten

**Streitwert:** Bezifferter Ausgleichsanspruch; vor Bezifferung: Antrag auf vorläufigen Streitwert nach § 61 GKG.

**Beispiel: Ausgleich EUR 60.000:**
- Gerichtsgebühren (3.0 LG-Verfahren aus EUR 60.000): ca. EUR 1.638.
- Anwaltsgebühren (1.3 + 1.2 + Auslagen): ca. EUR 3.800 netto je Seite.

**Umsatzsteuer:** Ausgleichsanspruch ist umsatzsteuerpflichtig (§ 1 Abs. 1 Nr. 1 UStG); daher zzgl. 19 % USt auf Nettobetrag.

**Steuerliche Behandlung beim Handelsvertreter:** § 34 EStG ermäßigter Steuersatz möglich bei Vertragsbeendigung als außerordentliche Einkunft.

## Strategische Empfehlung

| Situation | Empfehlung | Begründung |
|-----------|------------|-----------|
| Jahresfrist droht zu verstreichen | Sofort Geltendmachungsschreiben mit vorläufiger Berechnung | § 89b Abs. 4: Frist ist materiell-rechtlich; Versäumnis = endgültiger Verlust |
| Unternehmer verweigert Provisionsauskünfte | Auskunftsklage vorbereiten; § 87c HGB Provisionsauskunftspflicht | Ohne Zahlen keine Hauptsacheklage bezifferbar |
| Starke Marke des Unternehmers | EuGH Semen einsetzen; Provisionsverluste als Mindestuntergrenze verteidigen | Reine Billigkeitskürzung unzulässig |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Anschluss-Skills

- `fachanwalt-handels-gesellschaftsrecht-gesellschafterstreit` — Bei parallelem Gesellschafterstreit nach Ende des HV-Verhältnisses in Gesellschaft
- `fachanwalt-handels-gesellschaftsrecht-holding-strukturplanung` — Steuerplanung für Ausgleichszahlung
- `fachanwalt-handels-gesellschaftsrecht-geschaeftsfuehrerhaftung` — Wenn GF des Unternehmens Ausgleich verhindert

## Quellen

- § 89b HGB: https://www.gesetze-im-internet.de/hgb/__89b.html
- RL 86/653/EWG: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653
- EuGH C-348/07 (Semen): https://curia.europa.eu/juris/liste.jsf?num=C-348/07
- BGH VIII ZR 209/07: https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&az=VIII%20ZR%20209/07
- BGH VIII ZR 249/08: https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&az=VIII%20ZR%20249/08
