---
name: fachanwalt-it-recht-software-mangel
description: "Prüfung von Softwaremangelansprüchen nach Kauf-Werk- oder Dienstvertragsrecht. Anwendungsfall Software funktioniert nicht wie vereinbart und Mandant will Nachbesserung Minderung Rücktritt oder Schadensersatz. Normen §§ 433 ff. BGB Kaufrecht §§ 631 ff. BGB Werkvertragsrecht § 634 Nr. 1-4 BGB Gewaehlmaengel §§ 438 634a BGB Verjährung. Prüfraster Vertragstyp Mangelbegriff Spezifikation Nachbesserungsfrist Selbstvornahme Minderung Rücktritt Schadensersatz Open-Source-Compliance. Output Mangelanalyse-Protokoll mit Vertragstyp-Einordnung Gewaehlmaengelauswahl und Klageschrift-Baustein. Abgrenzung zu fachanwalt-it-recht-saas-vertrag-verhandlung und softwarefehler-mangelhaftung-prüfen."
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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

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

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

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

---
<!-- AUDIT 27.05.2026: Bundle 010 Halluzinations-Reparatur -->
<!-- VII ZR 124/18 (behauptet 06.06.2019, NJW 2019, 2867): NOT_FOUND auf dejure.org — geloescht -->
<!-- VII ZR 190/20 (behauptet NJW 2021, 3438, Thema: Software-Mangel): WRONG_TOPIC — real: Kfz-Thermofenster delikthaftung, NJW 2021, 3721, verifiziert auf dejure.org/2021,37448 — geloescht -->

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

