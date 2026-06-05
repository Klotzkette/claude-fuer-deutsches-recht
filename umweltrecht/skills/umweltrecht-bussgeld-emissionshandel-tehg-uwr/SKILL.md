---
name: umweltrecht-bussgeld-emissionshandel-tehg-uwr
description: "Bussgeld Emissionshandel Tehg UWR: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bussgeld Emissionshandel Tehg UWR

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bussgeld Emissionshandel Tehg UWR** im Plugin Umweltrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `umweltrecht-bussgeld-sanktionen` | Unternehmen erhaelt Anhoerung oder Bußgeld-Bescheid wegen Umwelt-Ordnungswidrigkeit und will sich verteidigen. Normen OWiG §§ 55 67 68 BImSchG §§ 62 64 KrWG §§ 69 70 WHG § 103 BNatSchG §§ 69 71a Bußgeld bis 100000 EUR. Prüfraster Tatbestandsprüfung Verjährung Verwertungsverbote Verteidigungsargumente. Output Verteidigungsschrift Widerspruch Akteneinsicht-Antrag. Abgrenzung zu umweltrecht-verfahren (Verwaltungsklage) und umweltrecht-immissionsschutz-bimschg (Genehmigung). |
| `umweltrecht-emissionshandel-tehg` | Anlagenbetreiber begutachtet Zuteilungsantrag Monitoring Abgabepflicht oder wehrt DEHSt-Sanktion ab. TEHG §§ 4 5 7 8 9 26 ZuV 2020 BEHG. Abgabe bis 30. April Sanktion 100 EUR je fehlende Tonne CO2. Prüfraster Zuteilungs-Berechnung Monitoring-Pflichten Abgabe-Frist DEHSt-Anordnung. Output Zuteilungsantrag-Entwurf Monitoring-Konzept Klagestrategie. Abgrenzung zu umweltrecht-verfahren (allg. Verwaltungsklage) und esg-greenwashing-csrd (ESG-Berichtspflicht). |
| `uwr-emissionshandel-ets-spezial` | Spezialfall EU-Emissionshandel ETS: Anwendungsbereich, Zuteilung kostenloser Zertifikate, Berichts- und Abgabepflicht, CBAM seit 2026 fuer Importe. Pruefraster fuer Industriebetriebe und Sanktionen bei Verstoss. |

## Arbeitsweg

Im Plugin Umweltrecht gilt für **Bussgeld Emissionshandel Tehg UWR**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `umweltrecht-bussgeld-sanktionen`

**Fokus:** Unternehmen erhaelt Anhoerung oder Bußgeld-Bescheid wegen Umwelt-Ordnungswidrigkeit und will sich verteidigen. Normen OWiG §§ 55 67 68 BImSchG §§ 62 64 KrWG §§ 69 70 WHG § 103 BNatSchG §§ 69 71a Bußgeld bis 100000 EUR. Prüfraster Tatbestandsprüfung Verjährung Verwertungsverbote Verteidigungsargumente. Output Verteidigungsschrift Widerspruch Akteneinsicht-Antrag. Abgrenzung zu umweltrecht-verfahren (Verwaltungsklage) und umweltrecht-immissionsschutz-bimschg (Genehmigung).

# Bussgeld, Sanktionen und Anhoerung im Umweltrecht

## Triage — klaere vor Reaktion auf Anhoerung

1. Welches Umweltgesetz ist Grundlage (BImSchG § 62, KrWG § 69, WHG § 103, BNatSchG § 69)?
2. Welcher Vorwurf genau — vorsaetzlich oder fahrlassig (OWiG § 10)?
3. Welche Behoerde fuehrt das Verfahren (Gewerbeaufsicht, Umweltbehoerde, Staatsanwaltschaft)?
4. Wurde bereits Akteneinsicht beantragt (§ 49 OWiG)?
5. Ist der Mandant die juristische oder die natuerliche Person (GF-Haftung §§ 9, 30 OWiG)?
6. Bestehen Verjaehjrungsfristen (§ 31 OWiG: 3 Jahre bei Bussgeld bis 100.000 EUR)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen und Paragrafenkette

- **§ 62 BImSchG** — Bussgeldbewehrte Pflichtverletzungen Betreiber (Betrieb ohne Genehmigung, Verstoss Nebenbestimmungen)
- **§ 64 BImSchG** — Strafbewehrte Verstoesze (Schadstoffe in der Luft wissentlich)
- **§ 69 KrWG** — Ordnungswidrigkeiten (illegale Entsorgung, Nachweispflichtverletzung)
- **§ 70 KrWG** — Straftatbestaende Abfallrecht (§ 326 StGB Verweis)
- **§ 103 WHG** — Ordnungswidrigkeiten Wasserrecht
- **§ 69 BNatSchG** — Ordnungswidrigkeiten Naturschutz
- **§ 55 OWiG** — Anhoerungsrecht Betroffener
- **§ 67 OWiG** — Einspruch gegen Bussgeld-Bescheid (2 Wochen)
- **§ 68 OWiG** — Hauptverhandlung beim Amtsgericht
- **§ 30 OWiG** — Verbandsgeldbuse gegen jur. Person
- **§ 31 OWiG** — Verjaeahrung (3 Jahre bei max. Bussgeld > 1.000 EUR)

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow


**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Anhoerungsschreiben analysieren**: Vorwurf, Norm, Tatzeit, Beweismittel, gesetzte Frist.
2. **Akteneinsicht beantragen** (§ 49 OWiG): Vollstaendige Akte — Messberichte, Kontrolle-Protokolle, Zeugenaussagen.
3. **Schuld pruefen**: Vorsatz / Fahrlassigkeit, Zurechnung auf Mandant, Delegationskette.
4. **Verjaeahrung pruefen**: § 31 OWiG; Unterbrechung durch Anhoerung (§ 33 OWiG).
5. **Verteidigungsschrift einreichen**: Tatsachen und Recht; Antrag auf Einstellung oder Bussgeld-Reduzierung.
6. **Einspruch bei Bescheid**: § 67 OWiG — 2 Wochen-Frist ab Bekanntgabe; Einspruch hemmt Rechtskraft.
7. **Amtsgericht**: Hauptverhandlung § 68 OWiG — Zeugenbefragung, Sachverstaendige; Strafverfahren § 70 KrWG / § 326 StGB separat.

### Entscheidungsbaum nach Anhoerungsschreiben

```
Anhoerungsschreiben erhalten
 → Frist noch offen?
 JA → Akteneinsicht sofort beantragen
 → Schuld-Pruefung: War Pflichtverletzung schuldhaft?
 JA → Minderungsgruende? → Verteidigungsschrift mit Minderungsargumentation
 NEIN → Einstellungsantrag wegen fehlendem Vorsatz/Fahrlassigkeit
 NEIN → Einspruch (§ 67 OWiG, 2 Wochen ab Bescheid)
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Einlassung im Umwelt-Bussgeldbescheid-Anhoerungsverfahren | Einlassung nach Schema; Template unten |
| Variante A — Behoerde will Besprechung vor Bescheid | Vorgespräch annehmen; Einlassung dann muendlich |
| Variante B — Mandant will Bussgeldbescheid akzeptieren | Keine Einlassung noetig; Bussgeldbescheid abwarten |
| Variante C — Strafrecht parallel ermittelt | Strafverteidigung-Skill parallel; vorsichtige Einlassung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template: Einlassung im Anhoerungsverfahren

**Adressat:** Zustaendige Behoerde — Tonfall: sachlich-juristisch

```
An die [BEHOERDE]

Stellungnahme im Anhoerungsverfahren gemaess § 55 OWiG

Betroffene/r: [NAME MANDANT], [ADRESSE]
Ihr Zeichen: [AZ BEHOERDE]
Vorwurf: [KURZBESCHREIBUNG]

I. Wir zeigen die anwaltliche Vertretung von [MANDANT] an.
 Akteneinsicht beantragen wir hiermit ausdruecklich gemaess § 49 OWiG.
 Wir bitten um Verlaengerung der Stellungnahme-Frist bis [DATUM].

II. Sachverhalt
[MANDANT] ist Betreiber der Anlage [NAME] in [ORT].
[Objektiver Sachverhalt aus Mandantensicht].

III. Rechtliche Einlassung
a) Tatbestand: § [X] [Gesetz] ist nicht erfuellt, weil [Argumentation].
b) Schuld: Ein schuldhaftes Handeln liegt nicht vor. [MANDANT] hat alle
 zumutbaren Vorkehrungen getroffen (Nachweise Anlage [X]).
c) Verjaeahrung: Die Tat soll sich am [DATUM] ereignet haben. Gemaess
 § 31 OWiG verjaeahrte die Ordnungswidrigkeit am [DATUM].

IV. Antrag
Wir beantragen, das Verfahren einzustellen.

Anlagen: Betriebsprotokoll, Wartungsnachweise, Vollmacht
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Vertiefung: Verbandsbussgeld § 30 OWiG

- Behoerde kann gegen jur. Person Bussgeld festsetzen, wenn GF/Organ Pflicht verletzt.
- Bussgeld bis 10 Mio. EUR (§ 30 Abs. 2 OWiG) bei Vorsatz; bei Fahrlassigkeit Haelfte.
- Selbststaendiges Verfahren gegen jur. Person neben Verfahren gegen natuerliche Person moeglich.
- Verteidigung: Mangelnde Zurechnung der Handlung, fehlende Aufsichtspflichtverletzung § 130 OWiG.

## Fristen im Ueberblick

| Verfahrensschritt | Frist | Grundlage |
|---|---|---|
| Einspruch gegen Bussgeld-Bescheid | 2 Wochen ab Bekanntgabe | § 67 Abs. 1 OWiG |
| Akteneinsicht-Antrag | Unverzueglich nach Anhoerung | § 49 OWiG |
| Verjaeahrung OWi (Bussgeld > 1000 EUR) | 3 Jahre | § 31 Abs. 2 Nr. 1 OWiG |
| Strafverfolgungsverjaehrung (§ 326 StGB) | 5 Jahre | § 78 Abs. 3 Nr. 4 StGB |

## Anschluss-Skills

- `umweltrecht-verfahren` — Gerichtsverfahren nach Einspruch
- `umweltrecht-immissionsschutz-bimschg` — Nachtraegliche Auflagen als Busjgeld-Alternative
- `umweltrecht-kommandocenter` — Intake und Mandats-Triage

## 2. `umweltrecht-emissionshandel-tehg`

**Fokus:** Anlagenbetreiber begutachtet Zuteilungsantrag Monitoring Abgabepflicht oder wehrt DEHSt-Sanktion ab. TEHG §§ 4 5 7 8 9 26 ZuV 2020 BEHG. Abgabe bis 30. April Sanktion 100 EUR je fehlende Tonne CO2. Prüfraster Zuteilungs-Berechnung Monitoring-Pflichten Abgabe-Frist DEHSt-Anordnung. Output Zuteilungsantrag-Entwurf Monitoring-Konzept Klagestrategie. Abgrenzung zu umweltrecht-verfahren (allg. Verwaltungsklage) und esg-greenwashing-csrd (ESG-Berichtspflicht).

# Emissionshandel und TEHG

## Triage — klaere zuerst

1. Welcher EU-ETS-Handelszeitraum (Phase 4: 2021-2030)?
2. Ist die Anlage TEHG-pflichtig (§ 2 TEHG i.V.m. Anlage 1 TEHG)?
3. Kostenlose Zuteilung oder Auktion — Grundlage ZuV 2020?
4. Monitoring-Plan DEHSt genehmigt?
5. Abgabe-Frist 30. April eingehalten?
6. Welche Art von Streit — Zuteilungsbescheid, Monitoring-Anordnung, Bussgeld?

## Zentrale Normen und Paragrafenkette

- **§ 2 TEHG i.V.m. Anlage 1** — Anwendungsbereich; Taetigkeitsliste (Energieumwandlung, Industrie, Luftverkehr)
- **§ 4 TEHG** — Genehmigungspflicht Anlagenbetreiber
- **§ 5 TEHG** — Monitoring-Pflicht (akkreditierter Pruefstelle)
- **§ 7 TEHG** — Jaehrliche Berichtspflicht (verifizierter Emissionsbericht)
- **§ 8 TEHG** — Abgabepflicht 30. April (Anzahl Berechtigungen entspricht verifizierten Emissionen)
- **§ 9 TEHG** — Kostenlose Zuteilung (ZuV 2020, Produktbenchmarks)
- **§ 26 TEHG** — Sanktion 100 EUR/t CO2 bei Abgaberueckstand; keine Befreiung durch Zahlung
- **ZuV 2020** — Zuteilungsverordnung 2020 — Benchmarks, Benchmark-Kurven, Cross-Sektoral-Correction-Faktor (CSCF)
- **BEHG** — Brennstoffemissionshandelsgesetz (nationaler ETS); § 10 BEHG Berichts- und Abgabepflicht

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schritt-fuer-Schritt-Workflow

1. **TEHG-Pflicht pruefen**: Anlage 1 TEHG — Taetigkeitskategorie, Schwellenwert (z.B. Feuerungsanlage > 20 MW thermisch).
2. **Genehmigungs-/Monitoring-Antrag**: § 4 TEHG-Genehmigung + Monitoring-Plan gemaess MVO/DEHSt.
3. **Zuteilungsantrag** (Phase 4: bis 31.05.2019 gestellt; laufende Anpassung bei Kapazitaetsaenderung): ZuV 2020-Benchmarks bestimmen; Baseline-Daten (2014-2018) einreichen.
4. **Jaehrliches Monitoring**: Emissionen messen/berechnen, von akkreditiertem Pruefstelle verifizieren lassen.
5. **Emissionsbericht 31. Maerz**: DEHSt-Einreichung.
6. **Abgabe 30. April**: Berechtigungen (EUAs) im EUTL-Konto abbuchen; fehlende Berechtigungen zukaufen (Spot oder Forward).
7. **Bei Zuteilungsbescheid-Angriff**: Widerspruch DEHSt, Klageverwaltungsgericht Berlin (§ 88 VwGO, auschliessliche Zustaendigkeit VG Berlin).

### Entscheidungsbaum Abgabe-Ruckstand

```
Abgabe-Frist 30.04. versaeumt?
 JA → § 26 TEHG: Sanktion 100 EUR/t CO2 Rueckstand
 → Sofort fehlende EUAs kaufen (Markt oder Broker)
 → Abgabe nachholen
 → Sanktions-Bescheid DEHSt anfechten? → Nur Verjaeahrung oder Fehler Feststellungsbescheid pruefbar
 NEIN → Alles korrekt → Dokumentation sichern
```

## Output-Template: Widerspruch Zuteilungsbescheid

**Adressat:** DEHSt — Tonfall: sachlich-juristisch

```
An die Deutsche Emissionshandelsstelle (DEHSt)
Bismarckplatz 1, 14193 Berlin

Widerspruch gegen Zuteilungsbescheid

Anlagenbetreiber: [NAME MANDANT]
Anlage: [NAME], [ORT], TEHG-Genehmigung Nr. [NR.]
DEHSt-Az.: [AZ.]

I. Hiermit legen wir namens und in Vollmacht des Anlagenbetreibers
 Widerspruch gegen den Zuteilungsbescheid vom [DATUM] ein.

II. Sachverhalt
Die DEHSt hat fuer die Handelsperiode 2021-2030 eine kostenlose
Zuteilung von [X] EUAs/Jahr festgesetzt. Unsere Berechnung
auf Basis der ZuV 2020 und der Benchmark-Daten ergibt jedoch
[Y] EUAs/Jahr.

III. Begruendung
a) Falsche Benchmark-Anwendung: DEHSt hat Benchmark [BM-CODE]
 angewendet, richtig waere [ANDERER CODE] (vgl. ZuV 2020 Anhang 1).
b) Baseline-Daten fehlerhaft: Produktionsmenge [JAHR] betraegt
 [ZAHL] t (Nachweise Anlage), nicht [ZAHL t DEHSt].
c) CSCF-Korrektur unzulaessig hoch: Berechnung gem. Beschl. EU 2021/355.

IV. Antrag
Wir beantragen, den Zuteilungsbescheid aufzuheben und
[Y] EUAs/Jahr zuzuteilen.

Anlagen: Produktionsdaten, Pruefstellen-Bericht, Benchmark-Berechnung
```

## Vertiefung: BEHG Nationaler Emissionshandel

- Gilt fuer Brennstofflieferanten (Waerme, Verkehr, Gebaeude, Kleingewerbe nicht unter EU-ETS).
- Festpreis-Phase bis 2025: 25 EUR/t CO2 (2021), schrittweise auf 55 EUR/t (2025).
- Ab 2026: Mengenhandel im Preiskorridor 55-65 EUR/t.
- Abgabe-Pflicht: Berechtigungszertifikate (nEHS-Zertifikate) bis 31. Juli des Folgejahres.
- DEHSt fuer nEHS-Registerueberwachung zustaendig.

## Fristen-Ueberblick

| Schritt | Frist | Grundlage |
|---|---|---|
| Zuteilungsantrag Phase 4 (laufend) | Bei Neuanlage: 12 Monate vor Betrieb | ZuV 2020 § 4 |
| Emissionsbericht einreichen | 31. Maerz Folgejahr | § 7 TEHG |
| Abgabe Emissionsberechtigungen | 30. April Folgejahr | § 8 TEHG |
| Widerspruch Zuteilungsbescheid | 1 Monat | § 70 VwGO |
| Klage VG Berlin | 1 Monat nach Widerspruchsbescheid | § 74 VwGO |

## Anschluss-Skills

- `umweltrecht-verfahren` — Klageverfahren VG Berlin
- `esg-greenwashing-csrd` — CSRD-Berichtspflicht ETS-Kosten
- `energierecht-industriekunden` — Befreiung BES-Regelung CO2-Kompensation
- `umweltrecht-kommandocenter` — Mandat-Intake

## 3. `uwr-emissionshandel-ets-spezial`

**Fokus:** Spezialfall EU-Emissionshandel ETS: Anwendungsbereich, Zuteilung kostenloser Zertifikate, Berichts- und Abgabepflicht, CBAM seit 2026 fuer Importe. Pruefraster fuer Industriebetriebe und Sanktionen bei Verstoss.

# Umwelt: ETS und CBAM

## Spezialwissen: Umwelt: ETS und CBAM
- **Spezialgegenstand:** Umwelt: ETS und CBAM / uwr emissionshandel ets spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EU, ETS, CBAM.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
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
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
