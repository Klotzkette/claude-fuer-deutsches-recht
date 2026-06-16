---
name: softwarefehler-mangelhaftung-pruefen
description: "Strukturierte Prüfung bei mangelhafter Software mit Vertragstyp-Einordnung: Anwendungsfall Software versagt und Mandant braucht Einordnung ob Kauf- Werk- oder Dienstvertragsrecht gi..."
---

# Strukturierte Prüfung bei mangelhafter Software mit Vertragstyp-Einordnung


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierte Prüfung bei mangelhafter Software mit Vertragstyp-Einordnung. Anwendungsfall Software versagt und Mandant braucht Einordnung ob Kauf- Werk- oder Dienstvertragsrecht gilt. Normen §§ 433 ff. BGB Kauf §§ 631 ff. BGB Werkvertrag §§ 535 ff. BGB Miete SaaS §§ 611 ff. BGB Dienst § 438 BGB Verjährung zwei Jahre Kauf § 634a BGB fuenf Jahre Werk. Prüfraster Vertragstyp Mangelbegriff Pflichtenhefte Spezifikation Nachbesserung Minderung Rücktritt Open-Source-GPL-Compliance. Output Mangel-Prüfprotokoll mit Vertragstyp-Einordnung Anspruchskette und Klagestrategie. Abgrenzung zu fachanwalt-it-recht-software-mangel und fachanwalt-it-recht-saas-vertrag-verhandlung.

### Softwarefehler — Mangelhaftung prüfen

## Kaltstart-Rückfragen

1. Was ist Gegenstand des Vertrages — Standardsoftware (ERP, Office, Antivirussoftware), Individualsoftware (Eigenentwicklung, Customizing), SaaS (cloud-basiert, Abonnement) oder Beratungsleistung? Begründung: Vertragstyp bestimmt Mängelregime.
2. Wann wurde geliefert / in Betrieb genommen / abgenommen (§ 640 BGB bei Werkvertrag)? Verjährungsbeginn?
3. Was ist der konkrete Mangel — Bug (Fehlfunktion), Performance-Problem, Schnittstellen-Defekt, Sicherheitslücke, fehlende Dokumentation, Datenmigrations-Fehler?
4. Gibt es ein Pflichtenheft, eine Spezifikation oder ein SLA, das die geschuldete Funktionalität beschreibt?
5. Wurden Mangelrügen erhoben (§ 377 HGB bei beidseitig kaufmännischem Geschäft: unverzüglich nach Entdeckung)?
6. Welche Nachbesserungsversuche wurden unternommen — wie viele, in welcher Frist?
7. Handelt es sich um ein B2C-Vertragsverhältnis (§§ 327 ff. BGB Digitale-Produkte-Regime)?
8. Liegt Open-Source-Komponente vor — welche Lizenz (GPL, AGPL, MIT, Apache)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Vertragstypen und anwendbare Mängelregeln

| Konstellation | Vertragstyp | Mangelnorm | Verjährung |
|---|---|---|---|
| Standardsoftware auf Datenträger (Kauf) | Kaufrecht §§ 433 ff. BGB | § 434 BGB | 2 Jahre § 438 BGB ab Übergabe |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Individualsoftware-Erstellung | Werkvertrag §§ 631 ff. BGB | § 633 BGB | 2 Jahre § 634a BGB ab Abnahme; 5 Jahre bei Bauwerk-Bezug |
| Customizing / Anpassung | Werkvertrag §§ 631 ff. BGB | § 633 BGB | 2 Jahre § 634a BGB |
| B2C digitale Inhalte / SaaS | §§ 327–327u BGB (seit 01.01.2022) | § 327e BGB | § 327j BGB |
| Wartungsvertrag mit Erfolgspflicht | Werkvertrag § 631 BGB | § 633 BGB | 2 Jahre ab Abnahme |
| Beratung / Implementierung | Dienstvertrag § 611 BGB | § 280 Abs. 1 BGB | 3 Jahre §§ 195, 199 BGB |

### Zentrale Normen

- **§ 433 BGB** — Kaufvertrag; Übergabe und Verschaffung mangelfreier Sache Pflicht.
- **§ 434 BGB (n. F. seit 01.01.2022)** — Sachmangel: Abs. 1 subjektive Anforderungen (vereinbarte Beschaffenheit); Abs. 2 objektive Anforderungen (übliche Beschaffenheit vergleichbarer Software).
- **§ 439 BGB** — Nacherfüllung; Verkäufer Wahlrecht Neulieferung oder Nachbesserung; Ausnahme wenn beide Arten unmöglich oder nur mit unverhältnismäßigen Kosten möglich.
- **§ 440 BGB** — Fehlschlagen der Nachbesserung nach Zweiversuchsregel (§ 440 Satz 2 BGB).
- **§ 633 BGB** — Werkvertrag Mangelbegriff; Abs. 2 analog zu § 434 BGB.
- **§ 635 BGB** — Werkvertrag Nacherfüllung; Unternehmer Wahlrecht.
- **§ 637 BGB** — Selbstvornahme Werkvertrag; Vorschussanspruch.
- **§ 536 BGB** — Mietvertrag Mangelbegriff: Tauglichkeit zum vertragsgemäßen Gebrauch aufgehoben oder erheblich gemindert.
- **§§ 327–327u BGB** — Digitale-Produkte-Richtlinie B2C: Aktualisierungspflicht § 327f BGB, Sachmangel § 327e BGB, Beweislastumkehr § 327k BGB ein Jahr.
- **§ 377 HGB** — Untersuchungs- und Rügeobliegenheit bei beidseitig kaufmännischem Handelsgeschäft: unverzüglich nach Lieferung bei offensichtlichem Mangel, nach Entdeckung bei verborgenem Mangel; Verlust Mängelrechte bei Versäumnis.

### BGH-Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfschema

| Nr. | Prüfschritt | Norm | Kernfrage |
|---|---|---|---|
| 1 | Vertragstyp bestimmen | §§ 433, 535, 631, 611, 327 BGB | Kauf, Miete, Werk, Dienst, Digitale Produkte? |
| 2 | B2C-Regime Digitale Produkte | §§ 327 ff. BGB | Verbraucher? Digitaler Inhalt oder digitale Dienstleistung? |
| 3 | Mangelbegriff prüfen | §§ 434, 536, 633 BGB | Vereinbarte / übliche Beschaffenheit; konkret nachweisbarer Fehler |
| 4 | Pflichtenhefte und SLA auswerten | § 434 Abs. 1 BGB | Vereinbarte Beschaffenheit dokumentiert? |
| 5 | Rügeobliegenheit HGB | § 377 HGB | Beidseitig kaufmännisch? Unverzüglich gerügt? |
| 6 | Abnahme (bei Werkvertrag) | § 640 BGB | Abnahme ausdrücklich oder konkludent erfolgt? Vorbehalt erklärt? |
| 7 | Nacherfüllung und Fehlschlagen | §§ 439, 635, 440 BGB | Wie viele Versuche? Unzumutbarkeit? |
| 8 | Sekundärrechte prüfen | §§ 437, 636, 636, 638 BGB | Minderung, Rücktritt, Schadensersatz, Selbstvornahme |
| 9 | Verjährung | §§ 438, 634a BGB | 2 Jahre (Kauf/Werk) ab Übergabe/Abnahme; 5 Jahre Bauwerk; 3 Jahre SaaS |
| 10 | AGB-Kontrolle | §§ 305 ff., 309 BGB | Haftungsfreizeichnung, verkürzte Verjährung, Pauschalschadensersatz wirksam? |
| 11 | Open-Source-Compliance | GPL, AGPL, MIT | Lizenzbedingungen eingehalten? Copyleft ausgelöst? |
| 12 | DSGVO-Sicherheitsmangel | Art. 32 DSGVO | Sicherheitslücke = Mangel + DSGVO-Pflicht? |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu prüfen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Software-Mangel geltend machen | Mangelruege; Template unten |
| Variante A — Mandant will weiter mit Anbieter arbeiten | Nacherfuellung § 439 BGB bevorzugen; Klage als letztes Mittel |
| Variante B — SLA-Verletzung statt Mangel | Vertragsstrafe prüfen; anderes Skill |
| Variante C — Open-Source-Komponenten betroffen | Lizenz-Compliance prüfen; Schadensersatz nach allg. Delikt |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Mangelrüge mit Fristsetzung (Käufer / Besteller)

```
An [Verkäufer / Auftragnehmer]

Mangelrüge und Fristsetzung zur Nacherfüllung

Wir ruegen nachfolgende Maengel an der Softwarelieferung / dem
Softwarewerk vom [Datum]:

1. [Bug-Beschreibung: System stuerzt bei Ausfuehren von Funktion X
 ab; Fehlermeldung: [Code]; reproduzierbar bei: [Umgebung]]
2. [Performance: Antwortzeit bei 10 parallelen Nutzern > 30 Sekunden;
 vereinbart laut Pflichtenheft Punkt 4.2: < 3 Sekunden]
3. [Schnittstelle Y funktioniert nicht: Schnittstellendokumentation
 laut Spezifikation vom [Datum] nicht erfullt]

Die Maengel unterschreiten die vereinbarte Beschaffenheit gemaess
Pflichtenheft vom [Datum] sowie die objektive Beschaffenheit
vergleichbarer Software am Markt.

Wir fordern Sie auf, die vorgenannten Maengel zu beseitigen
(Nacherfuellung gemaess § 635 BGB / § 439 BGB) bis spaetestens
[Datum, Frist: 3–6 Wochen je nach Schwere].

Nach fruchtlosem Ablauf der Frist behalten wir uns vor:
- Minderung des Werklohns / Kaufpreises
- Ruecktritt vom Vertrag
- Schadensersatz statt der Leistung §§ 437 Nr. 3, 281 BGB /
 §§ 636, 281 BGB
- Selbstvornahme und Vorschussklage § 637 BGB (Werkvertrag)

[Unterschrift]
Anlagen: Fehlerprotokoll, Screenshots, Log-Auszuge
```

### Klage auf Vorschuss für Selbstvornahme § 637 BGB

```
Klageschrift

Klager: [Auftraggeber]
Beklagter: [Auftragnehmer]

I. Antrag
Der Beklagte wird verurteilt, an den Klager EUR ____ nebst Zinsen
in Hoehe von 5 Prozentpunkten uber dem Basiszinssatz seit
Klagehangigkeit zu zahlen (Vorschuss Selbstvornahme § 637 BGB).

II. Sachverhalt
[Vertragsschluss, Lieferung, Maengel, Fristsetzung, Fehlschlagen]

III. Rechtliche Wuerdigung
Der Beklagte hat den Werkvertrag vom [Datum] erfullt; die abge-
nommene Software weist nachfolgende Maengel auf: [Auflistung].
Nach zweimaliger erfolgsloser Nachbesserung [Datum 1, Datum 2] ist
die Nacherfuellung gemaess § 637 BGB i.V.m. § 440 Satz 2 BGB als
endgueltig fehlgeschlagen anzusehen.

Die Kosten der Fremdfirma [X] zur Mängelbehebung betragen
gemaess Kostenvoranschlag (Anlage K4) EUR ____.

[Unterschrift]
```

--- vor Versand klären ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Beweislast und Darlegungslast

| Frage | Beweislast | Hinweis |
|---|---|---|
| Vorliegen des Mangels | Käufer / Besteller | Pflichtenheft; Sachverständiger; Fehlerprotokoll |
| Mangel bei Übergabe vorhanden | Käufer; Ausnahme § 477 BGB (B2C: Beweislastumkehr 1 Jahr); § 327k BGB (Digitale Produkte: 1 Jahr) | Zeitnähe zur Übergabe wichtig |
| Fristsetzung + Fehlschlagen | Käufer / Besteller | Schriftnachweis Rüge + Nachbesserungsversuche |
| Unzumutbarkeit Fristsetzung | Käufer | Gravierende Mängel, Unzuverlässigkeit |
| AGB-Inhaltskontrolle | Gericht von Amts wegen | § 306 BGB |
| Open-Source-Lizenzverletzung | Kläger (Lizenzgeber) | Auskunftsanspruch § 242 BGB vorgelagert |

## Fristen und Verjährung

| Frist | Dauer | Anker |
|---|---|---|
| Mangelrüge HGB (kaufmänn.) | Unverzüglich nach Entdeckung | § 377 HGB |
| Verjährung Kaufrecht | 2 Jahre ab Übergabe | § 438 Abs. 1 Nr. 3 BGB |
| Verjährung Werkvertrag | 2 Jahre ab Abnahme | § 634a Abs. 1 Nr. 1 BGB |
| Verjährung Werk-Bauwerk | 5 Jahre ab Abnahme | § 634a Abs. 1 Nr. 2 BGB |
| Verjährung SaaS Miete | 3 Jahre § 195 BGB (Regelverjährung) | §§ 195, 199 BGB |
| Verjährung Digitale Produkte | 2 Jahre (Kauf-analog) | § 327j BGB |
| Beweislastumkehr § 477 BGB B2C | 1 Jahr ab Übergabe | § 477 Abs. 1 BGB |
| Fristsetzung Nacherfüllung | Angemessen: typisch 3–8 Wochen | § 323 Abs. 1 BGB |

## Typische Gegenargumente und Reaktion

| Einwand | Reaktion |
|---|---|
| Rüge zu spät § 377 HGB | Prüfen ob Mangel erst nach Produktivbetrieb erkennbar (verborgener Mangel); dann Rügefrist nach Entdeckung |
| Keine Abnahme erklärt — Verjährung noch nicht begonnen | Konkludente Abnahme bei Ingebrauchnahme ohne wesentliche Rüge (§ 640 Abs. 1 S. 3 BGB) kann Verjährung starten |
| Pflichtenheft deckt Mangel nicht | Objektive Beschaffenheit § 434 Abs. 2 BGB: übliche Beschaffenheit vergleichbarer Software als Auffangtatbestand |
| Zweiversuchsregel nicht erfüllt | § 440 Satz 2 BGB — zwei Nachbesserungsversuche grundsätzlich ausreichend; auch einseitiger Wechsel auf Lieferung möglich § 439 Abs. 1 BGB |
| Pauschalschadensersatz im Vertrag | § 309 Nr. 5 BGB — unwirksam wenn überhöht; Angemessenheit durch Interessenabwägung |

## Streitwert und Kosten

- Streitwert: Kaufpreis / Werklohn (Rücktritt oder Schadensersatz statt der Leistung); bei Minderung Differenz.
- Vorschuss Selbstvornahme § 637 BGB: Höhe des Kostenvoranschlags.
- Gerichtskosten: GKG-Anlage 1 Tabelle 1200 (Zivilsache erste Instanz); bei 50.000 EUR = ca. 1.638 EUR.
- RVG Anwalt: 1,3-fache Verfahrensgebühr + 1,2-fache Terminsgebühr; bei 50.000 EUR ca. 3.500 EUR netto.
- Sachverständigenkosten IT: 150–350 EUR/h; Gesamtgutachten 5.000–30.000 EUR.
- Prozesskostenhilfe: für natürliche Personen ohne Vermögen §§ 114 ff. ZPO; Streitwertklausel prüfen.

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Frischer Mangel — Nachbesserung offen | Schriftliche Mangelrüge + angemessene Frist; Frist im Kalender |
| Verjährung droht in 3 Monaten | Sofort Klage oder Güteantrag § 204 BGB zur Hemmung |
| Sicherheitslücke | Parallel DSGVO-Pflichten prüfen; Mangelrüge + sofortige Gefahrenabwehr |
| Open-Source-Lizenzverletzung | Abmahnverfahren (GPL = GNU GPL Enforcement Coalition); Auskunft vor Schadensersatz |
| SaaS-Ausfall | Minderung Miete § 536 BGB; bei dauerhafter Unterschreitung SLA Sonderkündigungsrecht |

## Anschluss-Skills

- `fachanwalt-it-recht-saas-vertrag-verhandlung` — SLA und AVV-Prüfung
- `cyber-incident-response-72h` — bei Sicherheitslücke und Datenpanne
- `fachanwalt-it-recht-ki-vo-hochrisiko-konformitaetsbewertung` — bei KI-Software

## Quellen

- BGB §§ 280, 327–327u, 433–453, 535–548, 631–650
- HGB § 377
- DSGVO Art. 32
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Marly Praxishandbuch Softwarerecht, 8. Aufl.
- Schneider IT-Recht, 5. Aufl.

## Triage zu Beginn
1. Welcher Vertragstyp liegt vor — Kauf, Werkvertrag, SaaS-Miete, Digitale Produkte B2C (§§ 327 ff. BGB)?
2. Wann war Lieferung / Abnahme — laeuft Verjährungsfrist (2 Jahre Kauf/Werk, 3 Jahre SaaS)?
3. Wurde eine Mangelruege erhoben — bei kaufmaennischem Geschäft § 377 HGB unverzueglich?
4. Wie viele Nachbesserungsversuche gab es — Zweiversuchsregel § 440 Satz 2 BGB erfuellt?
5. Liegt eine Open-Source-Komponente vor — welche Lizenz (GPL, AGPL, MIT, Apache)?
6. Ist die Sicherheitsluecke datenschutzrelevant — parallel DSGVO-Meldepflicht Art. 33 prüfen?

## Output-Template — Mangelruege mit Fristsetzung
**Adressat:** Verkaeuer / Auftragnehmer — Tonfall: sachlich-juristisch
```
[KANZLEI]
[ADRESSE]
[DATUM]

[NAME MANDANT] ./. [GEGNER]
[AKTENZEICHEN]

Betreff: Mangelruege und Fristsetzung zur Nacherfuellung

Sehr geehrte Damen und Herren,

wir vertreten [NAME MANDANT]. Die am [DATUM LIEFERUNG] geleistete
Software / das am [DATUM ABNAHME] abgenommene Softwarewerk weist
nachfolgende Maengel auf:

1. [MANGELBESCHREIBUNG 1: Funktion, Fehlermeldung, Reproduzierbarkeit]
2. [MANGELBESCHREIBUNG 2: Performance-Wert IST vs. SOLL laut Pflichtenheft Pkt. X]
3. [MANGELBESCHREIBUNG 3: Sicherheitsluecke — CVE-Nummer falls bekannt]

Die Maengel unterschreiten die vereinbarte Beschaffenheit gemaess
Pflichtenheft / Spezifikation vom [DATUM] sowie die objektive
Beschaffenheit vergleichbarer Software (§ 434 Abs. 2 BGB / § 633 Abs. 2 BGB).

Wir setzen Frist zur Nacherfuellung bis [DATUM] (Frist: [ZEITRAUM]).

Nach Fristablauf behalten wir vor: Minderung, Ruecktritt, Schadensersatz
(§§ 437, 636 BGB) sowie Selbstvornahme mit Vorschussklage (§ 637 BGB).

[KANZLEI], [DATUM]

Anlagen: Fehlerprotokoll, Screenshots, Log-Auszuege (Anlage K1–K3)
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

