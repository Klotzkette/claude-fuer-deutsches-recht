---
name: fachanwalt-gewrechts-geschgehg-kollisionen-nda-hinschg-urhg
description: "Kollisionen zwischen gewerblichem Rechtsschutz NDA-Recht HinSchG und Urheberrecht prüfen wenn mehrere Schutzrechtsregime sich ueberschneiden. §§ 1 ff. GeschmMG § 14 MarkenG §§ 1 ff. HinSchG §§ 97 ff. UrhG. Prüfraster: Anwendungsbereich Vorrangfragen Schutzbereich Kollisionsauflösung Hinweisgeberschutz. Output: Kollisionsprüfmemo Handlungsempfehlung. Abgrenzung: Querschnitts-Skill für Kollisionsfragen."
---

## Mandantenfragen beim Kaltstart

1. Um welche Art von Information geht es (Quellcode, Kundenliste, Rezeptur, technisches Verfahren, Algorithmus, Finanzdaten)?
2. Welche konkreten Geheimhaltungsmaßnahmen hat das Unternehmen bisher getroffen (NDA, Zugriffskontrolle, Verschlüsselung, Schulungen)?
3. Wer hat die Information erlangt oder offenbart — ehemaliger Mitarbeiter, Lieferant, Wettbewerber, Journalist?
4. Besteht der Verdacht, dass die Information über einen Whistleblowing-Kanal (intern, BfJ, Öffentlichkeit) weitergegeben wurde?
5. Liegt ein NDA vor — wann geschlossen, welche Klauseln zur Geheimhaltungsdauer und Vertragsstrafe?
6. Welches Ziel verfolgt die Mandantschaft — einstweilige Verfügung, Schadensersatz, Strafanzeige oder Verteidigung gegen Vorwürfe?
7. Ist die Information möglicherweise auch urheberrechtlich oder patentrechtlich geschützt (Softwarecode, technische Erfindung)?
8. Handelt es sich um einen Sachverhalt mit Auslandsbezug (Wirtschaftsspionage, ausländischer Wettbewerber, grenzüberschreitende M&A)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| § 2 Nr. 1 GeschGehG | Legaldefinition Geschäftsgeheimnis: nicht allgemein bekannt, wirtschaftlicher Wert, angemessene Geheimhaltungsmaßnahmen, berechtigtes Interesse |
| § 3 GeschGehG | Erlaubte Handlungen: eigenständige Entwicklung, Reverse Engineering, Whistleblowing, Arbeitnehmer-Mitbestimmung |
| § 4 GeschGehG | Verbotene Handlungen: unbefugte Erlangung, Nutzung, Offenlegung |
| § 5 Nr. 2 GeschGehG | Whistleblower-Privileg: Geheimnisverletzung gerechtfertigt zur Aufdeckung rechtswidriger Handlungen im allgemeinen öffentlichen Interesse |
| §§ 6–8 GeschGehG | Zivilrechtliche Ansprüche: Unterlassung, Beseitigung, Vernichtung, Auskunft, Schadensersatz (drei Methoden) |
| §§ 9–14 GeschGehG | Prozessuale Sondervorschriften: Geheimhaltungsanordnung, beschränkter Personenkreis, Geheimnisklage |
| § 16 GeschGehG | Geheimhaltungsanordnung durch Gericht; Personenkreisbeschränkung |
| § 23 GeschGehG | Strafbarkeit Geheimnisverrat: bis 3 Jahre Freiheitsstrafe; bei Wirtschaftsspionage bis 5 Jahre |
| § 6 HinSchG | Verhältnis HinSchG zu anderen Vorschriften: GeschGehG-Schweigegebot tritt zurück |
| §§ 32, 36 HinSchG | Offenlegung als Ultima Ratio; Repressalienverbot mit Beweislastumkehr |
| § 40 HinSchG | Bußgeld bei Repressalie gegen Hinweisgeber bis EUR 50.000 |
| § 203 StGB | Verletzung von Privatgeheimnissen; Berufsgeheimnisträger inkl. Rechtsanwälte |
| §§ 43a BRAO, 2 BORA | Anwaltliche Verschwiegenheitspflicht |
| § 69a UrhG | Urheberrechtsschutz Software (Quellcode); Parallelschutz zu GeschGehG möglich |
| §§ 87a ff. UrhG | Datenbankschutz sui generis (15 Jahre, verlängerbar) |
| § 69e UrhG | Decompilation nur zur Herstellung von Interoperabilität erlaubt |
| Art. 6, 9, 35 DSGVO | Datenschutz bei Personalakten, Compliance-Untersuchungen, Datenschutz-Folgenabschätzung |
| § 26 BDSG | Beschäftigtendatenschutz bei internen Untersuchungen |

## Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---------|-------------|-------|-------------|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Vier-Stufen-Test § 2 Nr. 1 GeschGehG

| Stufe | Prüfpunkt | Praxis-Indikator | Rechtsfolge bei Fehlen |
|-------|-----------|-----------------|----------------------|
| 1 | Nicht allgemein bekannt / nicht ohne weiteres zugänglich | Branchenkenntnis, Fachliteratur, öffentliches Internet recherchiert? | Kein Geheimnisschutz |
| 2 | Wirtschaftlicher Wert wegen Geheimnischarakter | Negativwissen einbeziehen; Lizenzwert schätzen | Selten fehlend; Negativwissen reicht |
| 3 | Angemessene Geheimhaltungsmaßnahmen | Drei-Ebenen-Modell (organisatorisch, vertraglich, technisch) vollständig? | Häufigster Scheiterpunkt in der Rechtsprechung |
| 4 | Berechtigtes Geheimhaltungsinteresse | Illegal? Sittenwidrig? | Nur bei ausnahmsweise rechtswidrigem Inhalt fehlend |

## Prüfschema Geheimhaltungsmaßnahmen (Drei-Ebenen-Modell)

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.


| Ebene | Mindestanforderungen | Dokumentationspflicht |
|-------|--------------------|-----------------------|
| Organisatorisch | Need-to-Know-Prinzip; Besucherregelung; Offboarding-Protokoll (Rückgabe Geräte, Sperrung Zugänge am letzten Arbeitstag); Schulungsnachweis | GHS-Policy schriftlich; Schulungsregister |
| Vertraglich | NDA mit Lieferanten, Beratern, Bewerbern, Praktikanten vor Datenzugang; Geheimhaltungsklausel Arbeitsvertrag; nachvertragliches Wettbewerbsverbot § 74 HGB mit Karenzentschädigung | NDA-Archiv; Unterschriften vollständig |
| Technisch | RBAC-Zugriffsrechte; Multi-Faktor-Authentifizierung; AES-256-Verschlüsselung at-rest/in-transit; DLP-Systeme; Endpoint-Logging; Klassifizierungsschema (öffentlich/intern/vertraulich/streng vertraulich) | Audit-Logs; Patch-Protokolle; SIEM-Exports |

## Prüfschema Ansprüche bei Verletzung

| Schritt | Prüfpunkt | Norm | Rechtsfolge |
|---------|-----------|------|-------------|
| 1 | Geschäftsgeheimnis-Status positiv (§ 2 Nr. 1)? | § 2 Nr. 1 GeschGehG | Anspruchsvoraussetzung |
| 2 | Verbotene Handlung (Erlangung, Nutzung, Offenlegung)? | § 4 GeschGehG | Anspruchsgrundlage |
| 3 | Rechtfertigungsgrund? | § 3, § 5 GeschGehG | Whistleblower-Privileg; Reverse Engineering; Meinungsfreiheit |
| 4 | Unterlassung und Beseitigung | § 6 GeschGehG | Kein Verschuldenserfordernis |
| 5 | Vernichtung / Rückruf / Herausgabe | § 7 GeschGehG | Verhältnismäßigkeit prüfen |
| 6 | Auskunft und Rechnungslegung | § 8 GeschGehG | Vorbereitung Schadensersatz |
| 7 | Schadensersatz: Methode wählen | § 10 GeschGehG | Konkreter Schaden / Verletzergewinn / fiktive Lizenzgebühr |
| 8 | Strafanzeige | § 23 GeschGehG | Freiheitsstrafe bis 5 Jahre bei Wirtschaftsspionage |
| 9 | Einstweilige Verfügung | §§ 935, 940 ZPO | Dringlichkeit binnen 1 Monat ab Kenntnis |

## Kollisionsfeld: GeschGehG vs. Urheberrecht

| Aspekt | GeschGehG | UrhG |
|--------|-----------|------|
| Schutzgegenstand | Information mit wirtschaftlichem Wert | Persönliche geistige Schöpfung |
| Entstehung | Mit Geheimhaltungsmaßnahmen | Automatisch mit Schöpfung |
| Dauer | Solange geheim | 70 Jahre nach Tod des Urhebers |
| Bei Veröffentlichung | Schutzverlust GeschGehG | UrhG bleibt bestehen |
| Software (§ 69a UrhG) | GeschGehG + UrhG parallel vor Open-Source-Release | Quellcode = Sprachwerk; Schutz ab Schöpfung |
| Datenbankrecht | §§ 87a ff. UrhG parallel zu GeschGehG | 15 Jahre Investitionsschutz sui generis |

## Kollisionsfeld: GeschGehG vs. HinSchG

| Prüfschritt | Inhalt | Norm |
|------------|--------|------|
| 1 | Verstößt der Hinweis-Gegenstand gegen Strafrecht / OWi / EU-Recht? | § 2 HinSchG |
| 2 | Whistleblower-Privileg greift ein | § 5 Nr. 2 GeschGehG |
| 3 | Interne oder externe Meldestelle (gleichberechtigt) | § 7 HinSchG |
| 4 | Öffentliche Offenlegung nur als Ultima Ratio | § 32 HinSchG |
| 5 | Repressalienverbot; Beweislastumkehr | § 36 HinSchG |
| 6 | Schadensersatz bei vorsätzlich falscher Meldung | § 38 HinSchG |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — GeschGehG-Kollision mit NDA / HinSchG / UrhG pruefen | Vier-Stufen-Test und Kollisionsfelder unten |
| Variante A — nur NDA ohne GeschGehG-Schutzmassnamen | NDA-Schutz schwaecher; GeschGehG nicht automatisch anwendbar |
| Variante B — Whistleblower-Situation nach HinSchG | GeschGehG tritt zurueck; HinSchG-Schutz pruefen |
| Variante C — Softwarecode als Geschaeftsgeheimnis | Urheberrecht und GeschGehG parallel; Schutzsystem definieren |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatz-Bausteine

### Antrag auf Geheimhaltungsanordnung § 16 GeschGehG

```
An das Landgericht [Ort] – [zuständige Kammer] –

In dem Verfahren [Az.] beantragen wir namens der Klägerin:

1. Das Gericht ordnet gemäß § 16 GeschGehG an, dass folgende in der Klageschrift
   und ihren Anlagen enthaltene Informationen als geheimhaltungsbedürftig einzustufen
   sind: [Konkrete Bezeichnung der Geschäftsgeheimnisse, z. B. Kundenliste
   Anlage K 3; Rezeptur Anlage K 5].

2. Zugang zu den als geheimhaltungsbedürftig eingestuften Informationen ist auf
   folgenden Personenkreis zu beschränken:
   a) die Prozessbevollmächtigten der Parteien,
   b) je eine benannte Parteivertretung,
   c) bestellte Sachverständige mit schriftlicher Vertraulichkeitspflicht.

Begründung:
Die bezeichneten Informationen erfüllen die Voraussetzungen des § 2 Nr. 1 GeschGehG
[Ausführung der vier Stufen]. Eine Offenlegung gegenüber der Öffentlichkeit oder
einem unbeschränkten Personenkreis würde den wirtschaftlichen Wert der Informationen
unwiederbringlich vernichten.

[Ort, Datum]
Rechtsanwalt/Rechtsanwältin [Name]
```

### Einstweilige Verfügung wegen Geheimnisverrat

```
An das Landgericht [Ort]

ANTRAG AUF ERLASS EINER EINSTWEILIGEN VERFÜGUNG
gemäß §§ 935, 940 ZPO iVm § 6 GeschGehG

Verfügungsklägerin: [Unternehmensname]
Verfügungsbeklagter: [Ehemaliger Mitarbeiter / Wettbewerber]

Es wird beantragt:

1. Der Verfügungsbeklagten wird es bei Meidung eines Ordnungsgeldes bis zu
   EUR 250.000, ersatzweise Ordnungshaft, untersagt, die in Anlage AS 1
   bezeichneten Informationen zu nutzen oder offenzulegen.

2. Der Verfügungsbeklagten wird aufgegeben, alle Kopien und Vervielfältigungen
   der Informationen gemäß Anlage AS 1 unverzüglich herauszugeben.

Dringlichkeit:
Die Verfügungsklägerin erlangte am [Datum] durch [Umstand] Kenntnis vom
Informationsabfluss. Der Antrag wird binnen [Tage] gestellt; eine
Selbstwiderlegung liegt nicht vor.

Glaubhaftmachung:
Eidesstattliche Versicherung [Name] (Anlage EV 1); Endpoint-Log-Auszug
(Anlage EV 2); E-Mail-Verkehr (Anlage EV 3).

[Ort, Datum]
Rechtsanwalt/Rechtsanwältin [Name]
```

### NDA-Klausel (HinSchG-Vorbehalt und Reverse-Engineering-Freigabe)

```
§ [X] Vertraulichkeit

(1) Die Parteien verpflichten sich, Vertrauliche Informationen gemäß § 2 Nr. 1
GeschGehG streng vertraulich zu behandeln und Dritten nicht ohne vorherige
schriftliche Zustimmung der offenbarenden Partei zugänglich zu machen.

(2) Diese Vereinbarung berührt nicht die Rechte nach dem Hinweisgeberschutzgesetz
(HinSchG). Meldungen über Rechtsverstöße an interne, externe oder — in den
Grenzen des § 32 HinSchG — öffentliche Meldestellen stellen keine Verletzung
dieser Vereinbarung dar.

(3) Erlaubt bleiben die in § 3 GeschGehG bezeichneten Handlungen, insbesondere
die eigenständige Entwicklung und das Reverse Engineering nach § 3 Abs. 1 Nr. 2
GeschGehG, soweit gesetzlich zulässig.

(4) Bei Verletzung dieser Vereinbarung ist eine Vertragsstrafe von EUR [Betrag]
je Verstoß zu zahlen, unbeschadet weitergehender Schadensersatzansprüche.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Beweislast

| Beweisthema | Beweislast | Beweismittel |
|------------|-----------|--------------|
| Geheimnischarakter (§ 2 Nr. 1 GeschGehG) | Kläger | GHS-Policy, Klassifizierungsregister, Schulungsnachweise |
| Angemessene Geheimhaltungsmaßnahmen | Kläger | RBAC-Protokolle, NDA-Archiv, IT-Audit-Berichte |
| Verbotene Handlung (§ 4 GeschGehG) | Kläger | Endpoint-Logs, E-Mail-Metadaten, Zeugen, forensische Auswertung |
| Rechtfertigungsgrund (§ 3, § 5 GeschGehG) | Beklagter | Nachweis Reverse Engineering, Whistleblowing-Meldung, Meinungsfreiheit |
| Schaden / Verletzergewinn | Kläger (nach Auskunft) | Buchhaltungsunterlagen Beklagter, Sachverständigengutachten |
| Repressalie gegen Hinweisgeber | Arbeitgeber bei Klage nach § 36 HinSchG | Beweislastumkehr: Arbeitgeber muss rechtmäßige Kündigung belegen |

## Fristen

| Frist | Inhalt | Norm |
|-------|--------|------|
| 1 Monat (ca.) | Dringlichkeit bei einstweiliger Verfügung; Selbstwiderlegungsrisiko | §§ 935, 940 ZPO |
| 3 Jahre | Regelverjährung Schadensersatzanspruch ab Kenntnis | §§ 195, 199 BGB |
| 1 Woche | Interne Meldestelle muss Eingang bestätigen | § 17 HinSchG |
| 3 Monate | Rückmeldung interne Meldestelle über ergriffene Maßnahmen | § 17 Abs. 2 HinSchG |
| 5 Jahre | Aufbewahrungsfrist für Meldungen und Dokumentation durch Meldestelle | § 11 HinSchG |
| Laufend | Jahresprotokoll Geheimhaltungsmaßnahmen empfohlen | § 2 Nr. 1 lit. c GeschGehG |

## Gegenargumente und Reaktion

| Gegenargument | Herkunft | Reaktion |
|--------------|---------|----------|
| "Die Information ist allgemein bekannt / im Internet abrufbar" | Beklagter | Konkrete Quellenrecherche; Unterschied zwischen teilweise bekannter Struktur und spezifischer Detailkombination |
| "Keine angemessenen Geheimhaltungsmaßnahmen — Klage scheitert" | Beklagter | Drei-Ebenen-Nachweis (org/vertragl/techn); ex-post-Dokumentation schadet nicht, wenn Maßnahmen tatsächlich bestanden |
| "Ich bin Hinweisgeber — § 5 Nr. 2 GeschGehG / HinSchG schützt mich" | Beklagter | Prüfen: Deckt HinSchG § 2 den Sachverhalt ab? War Meldung nur zu eigenem Vorteil oder tatsächlich öffentliches Interesse? |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Reverse Engineering nach § 3 GeschGehG erlaubt" | Beklagter | Prüfen: Produkt rechtmäßig erlangt? Keine AGB-Beschränkung (§ 307 BGB)? Keine Urheberrechtsverletzung (§ 69e UrhG)? |
| "NDA-Klausel ist nach § 307 BGB unwirksam" | Beklagter | Individualvertrag vs. AGB unterscheiden; bei Kaufmann § 310 BGB; Inhaltskontrolle trotzdem durchführen |

## Streitwert und Kosten

**Streitwert Unterlassung:** Orientierung am wirtschaftlichen Interesse der Klägerin; bei Kundenlisten EUR 50.000–500.000 je nach Umsatzrelevanz; bei technischen Verfahren bis in den Millionenbereich.

**Einstweilige Verfügung:** Streitwert i. d. R. 1/3 bis 1/2 des Hauptsachestreitwerts.

**Sachliche Zuständigkeit:** Landgericht ohne Streitwertgrenze (§ 15 GeschGehG); ggf. Konzentrationsgericht nach Landesrecht.

**Schadensberechnung (§ 10 GeschGehG, drei Methoden):**
1. Konkreter Schaden: entgangener Gewinn + Rechtsverteidigungskosten.
2. Verletzergewinn: vollständiger Abschöpfung des Gewinns des Verletzers.
3. Fiktive Lizenzgebühr: branchenübliche Lizenzrate auf den relevanten Umsatz (typisch 3–10 %).

**Strafbarkeit § 23 GeschGehG:**
- Abs. 1 (Erlangung): Freiheitsstrafe bis 3 Jahre oder Geldstrafe.
- Abs. 4 (Wirtschaftsspionage / Auslandsbezug): Freiheitsstrafe bis 5 Jahre.

## Strategische Empfehlung

| Situation | Empfehlung | Begründung |
|-----------|------------|-----------|
| Mitarbeiterabwanderung mit Datenmitnahme | Sofortiger eV-Antrag auf Unterlassung + Herausgabe; Strafanzeige § 23 GeschGehG parallel | Beweissicherung vor Datenlöschung; Abschreckungswirkung |
| Unternehmen will Schutz aufbauen | Drei-Ebenen-Maßnahmenkatalog; GHS-Policy; NDA-Update mit HinSchG-Vorbehalt | OLG Köln: fehlende IT-Kontrollen vernichten Schutz |
| Whistleblower verteidigen | § 5 Nr. 2 GeschGehG + § 36 HinSchG kombinieren; Beweislastumkehr nutzen | Arbeitgeber muss rechtmäßige Kündigung beweisen |
| M&A-NDA-Verhandlung | Pflichtklauseln: HinSchG-Vorbehalt, Reverse-Engineering-Freigabe, beidseitige Vertragsstrafe, Schiedsklausel DIS/ICC | Einseitige AG-NDA enthält regelmäßig HinSchG-Aushebelungen |
| Geheimnisklage LG | Sofort Geheimhaltungsanordnung § 16 GeschGehG beantragen; Personenkreis präzise benennen | Schutz vor weiterer Offenbarung im laufenden Verfahren |

## Anschluss-Skills

- `fachanwalt-arbeitsrecht-hinschg-whistleblower-repressalie` — HinSchG-Verteidigung im Arbeitsverhältnis
- `fachanwalt-gewerblicher-rechtsschutz-abmahnung-uwg` — UWG-Abmahnung bei unlauterem Geheimnisverrat
- `fachanwalt-gewerblicher-rechtsschutz-markenanmeldung` — Ergänzender Markenschutz für Produktnamen
- `fachanwalt-internationales-wirtschaftsrecht-cisg-pruefung` — Grenzüberschreitende NDA-Fragen

## Quellen

- GeschGehG: https://www.gesetze-im-internet.de/geschgehg/
- HinSchG: https://www.gesetze-im-internet.de/hinschg/
- BGH I ZR 136/17: https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&az=I%20ZR%20136/17
- BAG 2 AZR 547/05: https://juris.bundesarbeitsgericht.de/cgi-bin/rechtsprechung/document.py?Gericht=bag&Art=en&az=2%20AZR%20547/05
- Know-how-RL (EU) 2016/943: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32016L0943

## Triage-Fragen bei Geschäftsgeheimnis-Mandat

Bevor die Schutzstrategie entwickelt wird, klaere:
1. Liegen "angemessene Geheimhaltungsmassnahmen" nach § 2 Nr. 1 lit. b GeschGehG vor (technisch UND organisatorisch)?
2. Ist die verletzte Information wirklich ein Geschaeftsgeheimnis oder bereits bekannte Branchen-Praxis?
3. Kommt § 5 GeschGehG (Whistleblowing-Ausnahme) oder § 36 HinSchG in Betracht?
4. Ist eine sofortige Sicherungsanordnung nach § 16 GeschGehG (Offenbarungsschutz im Verfahren) erforderlich?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
