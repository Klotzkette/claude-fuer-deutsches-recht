---
name: fachanwalt-it-recht-software-mangel
description: "Pruefung von Softwaremangelanspruechen nach Kauf-Werk- oder Dienstvertragsrecht. Anwendungsfall Software funktioniert nicht wie vereinbart und Mandant will Nachbesserung Minderung Ruecktritt oder Schadensersatz. Normen §§ 433 ff. BGB Kaufrecht §§ 631 ff. BGB Werkvertragsrecht § 634 Nr. 1-4 BGB Gewaehlmaengel §§ 438 634a BGB Verjaehrung. Pruefraster Vertragstyp Mangelbegriff Spezifikation Nachbesserungsfrist Selbstvornahme Minderung Ruecktritt Schadensersatz Open-Source-Compliance. Output Mangelanalyse-Protokoll mit Vertragstyp-Einordnung Gewaehlmaengelauswahl und Klageschrift-Baustein. Abgrenzung zu fachanwalt-it-recht-saas-vertrag-verhandlung und softwarefehler-mangelhaftung-pruefen."
---

# Software-Mangel

## Kaltstart-Rückfragen

1. Handelt es sich um Standardsoftware (Kaufrecht), Individualentwicklung (Werkvertrag) oder SaaS/Cloud-Bereitstellung (Mietvertrag § 535 BGB)?
2. Wurde das Werk bzw. die Software bereits abgenommen oder geliefert? Liegt ein Übergabeprotokoll vor?
3. Welche konkreten Funktionen fehlen oder funktionieren nicht wie zugesagt? Liegt ein Lasten-/Pflichtenheft vor?
4. Wurde dem Lieferanten bereits eine Nacherfüllungsfrist gesetzt und welche Reaktion erfolgte?
5. Ist der Mandant Verbraucher oder Unternehmer? Welche AGB-Klauseln gelten?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Anspruchsgrundlagen

- Standardsoftware: Kaufrecht — Sachmangel § 434 BGB (objektive und subjektive Anforderungen), Rechtsmangel § 435 BGB.
- Individualsoftware: Werkvertrag — Mangel § 633 BGB, Werk frei von Sach- und Rechtsmängeln bei Abnahme.
- SaaS/Cloud: Mietrecht § 535 BGB — fortlaufende Gebrauchsgewährung, Mangel § 536 BGB führt zu Minderung kraft Gesetzes.
- Nacherfüllungspflicht: § 439 BGB (Kauf) bzw. § 635 BGB (Werk) — Nachbesserung oder Neulieferung.
- Sekundäre Rechte nach erfolglosem Fristablauf: Rücktritt § 437 Nr. 2 i.V.m. § 323 BGB, Minderung § 441 BGB, Schadensersatz § 437 Nr. 3 i.V.m. §§ 280, 281 BGB.
- BGH zu Standardsoftware als Sache: BGH VIII ZR 219/06, Urt. v. 15.11.2006, Rn. 12 ff.

## Beweislast und Frist

- Käufer/Besteller trägt nach Gefahrübergang bzw. Abnahme die Beweislast für den Mangel.
- Verbrauchsgüterkauf: Beweislastumkehr § 477 BGB für ein Jahr ab Gefahrübergang (vor 01.01.2022: sechs Monate).
- Verjährung Kaufrecht: zwei Jahre § 438 Abs. 1 Nr. 3 BGB; Werkvertrag bei nicht-Bauleistung: zwei Jahre § 634a Abs. 1 Nr. 1 BGB.
- Bei arglistig verschwiegenem Mangel: Regelverjährung § 438 Abs. 3 BGB bzw. § 634a Abs. 3 BGB.

## Prüfschema

```
1. Vertragstyp bestimmen (Kauf / Werk / Miete-SaaS)
2. Sollbeschaffenheit aus Lasten/Pflichtenheft und Vertrag ableiten
3. Istbeschaffenheit aus Tests und Logs dokumentieren
4. Soll/Ist-Abweichung = Mangel
5. Nacherfuellungsfrist setzen (zwei bis vier Wochen je nach Komplexitaet)
6. Bei Fristablauf: Ruecktritt oder Minderung oder Schadensersatz
7. Verjaehrung im Kalender notieren
```

Standardliteratur: Grüneberg BGB §§ 434, 633; Schneider IT-Vertragsrecht; MüKo-BGB / Westermann § 434.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Software-Mangel geltend machen | Mangelruege; Template unten |
| Variante A — Mandant will weiter mit Anbieter arbeiten | Nacherfuellung § 439 BGB bevorzugen; Klage als letztes Mittel |
| Variante B — SLA-Verletzung statt Mangel | Vertragsstrafe pruefen; anderes Skill |
| Variante C — Open-Source-Komponenten betroffen | Lizenz-Compliance pruefen; Schadensersatz nach allg. Delikt |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schreibvorlage Mängelrüge mit Fristsetzung

```
Sehr geehrte Damen und Herren,

namens und in Vollmacht unserer Mandantschaft ruegen wir die nachfolgend
beschriebenen Maengel der gelieferten Software [Produktbezeichnung,
Versionsnummer]:

1. [Mangel 1 — Soll laut Pflichtenheft Ziff. X / Ist laut Test-Protokoll vom ...]
2. [Mangel 2 — ...]
3. [Mangel 3 — ...]

Wir fordern Sie auf bis spaetestens [Datum, mindestens zwei Wochen] die
Maengel im Wege der Nacherfuellung gemaess § 439 BGB / § 635 BGB zu
beseitigen.

Nach fruchtlosem Fristablauf werden wir vom Vertrag zuruecktreten den
Kaufpreis zurueckverlangen sowie Schadensersatz statt der Leistung
geltend machen (§§ 437 Nr. 2 und Nr. 3 BGB i.V.m. §§ 323 280 281 BGB).

Mit freundlichen Gruessen
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Übergabe

- Bei Fristablauf ohne Nacherfüllung: Übergang in `forderungsmanagement-klagewerkstatt` zur Klageerhebung.
- Bei laufendem SaaS: parallel Minderungsmitteilung an Vermieter nach § 536 BGB.
- Verjährungsfrist im Aktenkalender notieren.

## Aktuelle Rechtsprechung (v14.2)

- BGH, Urt. v. 06.06.2019 — VII ZR 124/18, NJW 2019, 2867 Rn. 28: Zur Abgrenzung Kauf- und Werkvertrag bei Software; Individualsoftware ist werkvertraglich (§ 633 BGB); Standardsoftware auf körperlichem Datenträger als Kauf (§ 434 BGB); SaaS/Cloud-Software als Miet- oder Dienstvertrag.
- BGH, Urt. v. 16.09.2021 — VII ZR 190/20, NJW 2021, 3438 Rn. 38: Zum Mangelbegriff bei Software; fehlende Interoperabilität mit vertraglich vorausgesetzter Systemumgebung ist Sachmangel nach § 434 Abs. 1 BGB (a.F.) / § 434 Abs. 2 BGB (n.F. ab 2022).
- OLG Frankfurt, Urt. v. 15.04.2021 — 6 U 152/20, NJW-RR 2021, 912 Rn. 22: Fristsetzung nach § 439 BGB muss konkrete Mangelbeseitigung benennen; pauschale "Nachbesserungsaufforderung" setzt Frist nicht wirksam.
- LG Berlin, Urt. v. 28.09.2021 — 52 O 83/20, CR 2022, 145 Rn. 18: Zur Mängelrüge bei SaaS; SLA-Unterschreitung als Sachmangel; Schlechtleistung begründet Minderungsrecht nach §§ 536, 536a BGB analog.

## Triage zu Beginn

1. Vertragstyp: Kauf / Werk / Miete / Dienst / Kombination?
2. Standard- oder Individualsoftware?
3. Liegt ein Sachmangel (§ 434 BGB) oder Rechtsmangel (§ 435 BGB) vor?
4. Fristsetzung zur Nacherfüllung bereits erfolgt? Frist abgelaufen?

## Output-Template — Software-Mangel-Memo

**Adressat:** Gericht / Gegenseite — Tonfall: sachlich-juristisch

```
Software-Mangel-Memo [DATUM]
Parteien: [AUFTRAGGEBER] vs. [AUFTRAGNEHMER/ANBIETER]
Vertragstyp: Kauf § 433 BGB / Werkvertrag § 631 BGB / Miete § 535 BGB
Software: [BEZEICHNUNG, VERSION]

Mangel:
Beschreibung: [KONKRETE BESCHREIBUNG]
Rechtsgrundlage: § 434 Abs. [X] BGB / § 633 Abs. [X] BGB / § 536 BGB

Ansprüche:
1. Nacherfüllung (§ 439 / § 635 BGB): Frist gesetzt am [DATUM]; Ablauf [DATUM]
2. Bei Fristablauf: Rücktritt § 437 Nr. 2 / § 634 Nr. 3 BGB / Minderung / Schadensersatz

Streitwert: [BETRAG EUR]
Verjährung: § 438 BGB 2 Jahre ab Ablieferung / § 195 BGB 3 Jahre (§ 634a BGB)
```
