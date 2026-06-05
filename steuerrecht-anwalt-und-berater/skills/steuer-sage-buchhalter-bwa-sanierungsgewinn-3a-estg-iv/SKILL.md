---
name: steuer-sage-buchhalter-bwa-sanierungsgewinn-3a-estg-iv
description: "Steuer Sage Buchhalter BWA Sanierungsgewinn 3A Estg IV: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Steuer Sage Buchhalter BWA Sanierungsgewinn 3A Estg IV

## Arbeitsbereich

Dieser Skill bündelt 9 sachlich verwandte Arbeitsschritte rund um **Steuer Sage Buchhalter BWA Sanierungsgewinn 3A Estg IV** im Plugin Steuerrecht-Anwalt und -Berater. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stb-sage-buchhalter-bwa-konfiguration` | Sage Buchhalter BWA-Konfiguration. Anwendungsfall Mandanten oder Kanzleien mit Sage-Software statt DATEV/Addison. Methodik Unterschiede Konten BWA-Forms. Output BWA in Sage. |
| `stb-sanierungsgewinn-3a-estg-grundtatbestand` | Tatbestandsmerkmale des § 3a EStG: Sanierungsertrag, unternehmensbezogene Sanierung und die vier Voraussetzungen Sanierungsbedürftigkeit, Sanierungsfähigkeit, Sanierungsabsicht der Gläubiger und Sanierungseignung. |
| `stb-sanierungsgewinn-3a-estg-unternehmens-vs-person` | Abgrenzung unternehmensbezogene Sanierung gegen personenbezogene Sanierung im Sinne § 3a EStG. § 3a EStG schützt nur die unternehmensbezogene Variante; Restschuldbefreiung Privatperson fällt unter § 3a Absatz 5. |
| `stb-sanierungsgewinn-3a-iv-estg-antrag-und-bindungswirkung` | Antrag nach § 3a Absatz 4 EStG: Form, Frist, Inhalt und Bindungswirkung. Nach Feststellung des Sanierungserfolgs ist der Antrag nicht mehr zurücknehmbar; strategische Konsequenzen sind vor Antragstellung abzuwägen. |
| `stb-sanierungsgewinn-bmf-2017-sanierungserlass-nachfolge` | BMF-Schreiben vom 27.04.2017 als Verwaltungsanweisung zur Nachfolge des Sanierungserlasses. Konkretisiert die vier Voraussetzungen des § 3a EStG aus Verwaltungssicht; vor Verwendung aktuellen BMF-Stand prüfen. |
| `stb-sanierungsgewinn-forderungsverzicht-bilanzielle-darstellung` | Bilanzielle Darstellung des Forderungsverzichts beim Schuldner und beim Gläubiger. Werthaltigkeit, außerordentlicher Ertrag, Ausweis in der GuV; Plan-Bilanz vor und nach Sanierung. |
| `stb-sanierungsgewinn-fruehwarnung-monat-zwoelf-vor-plan` | Frühwarn-Skill Sanierungsgewinn nach Paragraf 3a EStG. Rechnet 12 Monate vor Insolvenzantrag oder StaRUG-Anzeige rückwärts und zeigt Mandant und Berater wann welche Weiche zu stellen ist damit der Antrag nach Paragraf 3a Absatz 4 EStG nicht im letzten Moment platzt. |
| `stb-sanierungsgewinn-personengesellschaft-und-mitunternehmer` | Besonderheiten der Sanierungsertragsbehandlung bei Personengesellschaften und Mitunternehmern. Anteilige Zurechnung Sanierungsertrag; getrennter Antrag § 3a Absatz 4 EStG je Mitunternehmer; Sonderbetriebsvermögen. |
| `stb-sanierungsgewinn-rangruecktritt-und-5-abs-2a-estg` | Rangrücktritt im Kontext § 5 Absatz 2a EStG: Passivierungsverbot bei Tilgung ausschließlich aus zukünftigen Gewinnen führt zum Ertrag in voller Höhe und damit zum Sanierungsgewinn. BFH-Linie streng - keine Az aus Modellwissen. |

## Arbeitsweg

Im Plugin Steuerrecht-Anwalt und -Berater gilt für **Steuer Sage Buchhalter BWA Sanierungsgewinn 3A Estg IV**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stb-sage-buchhalter-bwa-konfiguration`

**Fokus:** Sage Buchhalter BWA-Konfiguration. Anwendungsfall Mandanten oder Kanzleien mit Sage-Software statt DATEV/Addison. Methodik Unterschiede Konten BWA-Forms. Output BWA in Sage.

# Sage Buchhalter BWA

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sage Buchhalter BWA` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Kernsachverhalt

Sage ist eine internationale ERP- und Buchhaltungsplattform, in Deutschland mit Sage 100, Sage 50 fuer KMU. Insbesondere bei mittelstaendischen Mandanten haeufig im Einsatz. BWA-Module sind aequivalent zu DATEV/Addison, aber mit anderer Bedienlogik. Steuerberater, die mit Sage-Mandanten arbeiten, brauchen Schnittstellen oder Datenuebernahme.

## Kaltstart-Rueckfragen

1. Welche Sage-Version (Sage 100, Sage 50, Sage Office Line)?
2. Wer betreibt Sage — Mandant selbst oder StB?
3. Welche BWA-Form ist konfiguriert?
4. Welcher Kontenrahmen (SKR 03, SKR 04, individuell)?
5. Welche Schnittstellen zu DATEV (falls vorhanden)?
6. Welche Module aktiv?
7. Welche Mandantenbeguenstigung?
8. Welcher Updates-Stand?

## Workflow

### Phase 1 — System-Setup

- Variante A: Mandant betreibt Sage selbst (Sage 50 Cloud, Sage 100, Sage Office Line); StB erhaelt Lese-Zugriff oder Monats-Export.
- Variante B: StB betreibt Sage als Service-Provider (selten; in der Regel DATEV-Bevorzugung in Kanzleien).
- Konten-Konfiguration: Sage unterstuetzt SKR 03/04 sowie eigene Kontenrahmen; Branchenkontenrahmen ueber Sage-Vorlagen.

### Phase 2 — BWA-Konfiguration

- Sage-Standard-BWA gliedert ueblicherweise nach Erloesen, variable Kosten, Deckungsbeitrag, Fixkosten, Betriebsergebnis (vergleichbar mit DATEV BWA 01).
- Vorjahresvergleich automatisch bei vorhandener Historie; Planwerte ueber das Sage-Planungsmodul.
- Anpassung der BWA-Zeilen ueber `Auswertungen → BWA → Konfiguration` (konkreter Programmpfad variiert je Sage-Version — im Zweifelsfall in der Sage-Onlinehilfe unter "BWA-Konfiguration" nachschlagen).

### Phase 3 — Schnittstellen

- Sage-eRechnung-Modul fuer XRechnung/ZUGFeRD-Empfang und -Versand (§ 14 UStG; siehe Skill `stb-erechnung-pflicht-b2b-2025-2026`).
- Bank-Anbindung ueber PSD2-Schnittstelle (HBCI/FinTS) oder Sage Banking.
- Export im DATEV-CSV-Format (DATEV ASCII-Format) ueber `Stammdaten → Datenexport → DATEV` (Programmpfad version-abhaengig).

### Phase 4 — Datenaustausch mit StB

- Standardisierter Monats-Export aus Sage; Termin- und Format-Vereinbarung schriftlich.
- StB-Seite: Import in DATEV Kanzlei-Rechnungswesen ueber `Datei → Datenuebernahme → Buchungsstapel`.
- Mapping-Tabelle Sage-Konten zu SKR 03/04 vorab abstimmen — Differenzen sonst pro Monat zu klaeren.

### Phase 5 — Lohn

- Sage HR / Sage Lohn als separate Module bzw. externes Lohnprogramm (DATEV LODAS, eGecko, etc.).
- Buchungssatz-Schnittstelle zum Hauptbuch (typischerweise monatlicher Buchungsbeleg).
- Bei Mandantenwechsel zu DATEV: Lohn meist parallel migriert (siehe `stb-lohn-mandantenaufnahme-onboarding`).

### Phase 6 — Updates

- Jaehrliche Programm-Updates zum 1. Januar (LSt/SV-Tabellen, USt-Aenderungen, AfA-Tabellen).
- Sage Cloud-Versionen: automatische Updates ueber den Cloud-Anbieter.
- Update-Pflicht aus § 146 AO (Programm muss aktuelle Tabellen abbilden).

## Output

- Konfigurierte Sage-BWA.

## Strategie und Praxis-Tipps

- Bei Sage-Mandanten Datenaustausch standardisieren — CSV-Export ist Standard.
- Datenuebernahme Sage zu DATEV ist Aufwand — Mandantenwechsel sorgfaeltig planen.
- Sage-Schulung ueber Sage-Akademie.

## Querverweise

- `stb-bwa-aufbau-grundlagen` — BWA.
- `stb-datev-bwa-modul-bedienen-tipps` — DATEV.
- `stb-addison-bwa-konfiguration-tipps` — Addison.

## Quellen und Updates

Stand: 05/2026.

- Sage Programm- und Bedienungsdokumentation (aktuelle Version pruefen).
- AO § 146 (Update-Pflicht der Buchfuehrungsprogramme).
- Hinweis: konkrete Programmpfade und Modulbezeichnungen koennen je Sage-Version abweichen; aktuelle Informationen in der Sage-Onlinehilfe pruefen.

<!-- AUDIT 27.05.2026 | welle 6 | 1 Marker aufgeloest: 1 ersetzt (Sage-Programmpfad nicht versionsspezifisch belegbar, Verweis auf Sage-Onlinehilfe) -->


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `stb-sanierungsgewinn-3a-estg-grundtatbestand`

**Fokus:** Tatbestandsmerkmale des § 3a EStG: Sanierungsertrag, unternehmensbezogene Sanierung und die vier Voraussetzungen Sanierungsbedürftigkeit, Sanierungsfähigkeit, Sanierungsabsicht der Gläubiger und Sanierungseignung.

# § 3a EStG — Grundtatbestand der Sanierungsertragsbefreiung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `§ 3a EStG — Grundtatbestand der Sanierungsertragsbefreiung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

§ 3a EStG befreit Erträge aus einer unternehmensbezogenen Sanierung von der Einkommensteuer (und über § 8 Abs. 1 KStG von der Körperschaftsteuer). Voraussetzung ist, dass die Sanierung kumulativ vier Merkmale erfüllt. Dieser Skill zerlegt die Norm in ihre Tatbestandsmerkmale und arbeitet Subsumtionspunkte heraus.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Liegt eine Sanierung (Schuldenerlass / Verzicht) tatsächlich vor — oder nur Forderungsausfall?
2. Hat das Unternehmen einen begünstigten Sanierungsertrag im Sinne § 3a EStG?
3. Sind die vier Voraussetzungen schriftlich dokumentiert?
4. Welche Steuerart ist betroffen — ESt, KSt, GewSt?
5. Ist die Sanierung unternehmensbezogen oder personenbezogen (siehe Folge-Skill)?

## Rechtlicher Rahmen

- **§ 3a Abs. 1 EStG** — Sanierungserträge sind steuerfrei, wenn sie durch eine unternehmensbezogene Sanierung anfallen.
- **§ 3a Abs. 2 EStG** — Definition unternehmensbezogene Sanierung: Maßnahmen zur Wiederherstellung der Zahlungsfähigkeit und Rentabilität eines Unternehmens.
- **§ 3a Abs. 3 EStG** — Berechnung des Sanierungsertrags (außerordentlicher Ertrag, mindernde Aufwendungen).
- **§ 3a Abs. 4 EStG** — Antragsmodalitäten und Bindungswirkung.
- **§ 8 Abs. 1 KStG** — Anwendung über die Körperschaftsteuer.
- **§ 7b GewStG** — Gewerbesteuer-Befreiung parallel.
- **§ 3c Abs. 4 EStG** — Verlustreihenfolge.

## / Schritt für Schritt

### Die vier Voraussetzungen kumulativ

| Voraussetzung | Inhalt | Nachweis |
|---|---|---|
| Sanierungsbedürftigkeit | Unternehmen in der Krise; ohne Sanierung Insolvenzgefahr | BWA mit Verlustreihe, Liquiditätsplan, Sanierungsgutachten |
| Sanierungsfähigkeit | Mit Sanierung tragfähig fortführbar | Fortbestehensprognose, IDW S 6-Konzept |
| Sanierungsabsicht der Gläubiger | Verzicht erfolgt zum Zweck der Sanierung — nicht aus anderen Gründen | Schriftliche Erklärungen der Gläubiger |
| Sanierungseignung | Die Maßnahme ist objektiv geeignet, das Unternehmen zu retten | Sanierungsplan; Maßnahmenkatalog; Quote |

### Subsumtions-Reihenfolge

| Schritt | Prüfung |
|---|---|
| 1 | Liegt ein Ertrag aus Schuldenerlass / Verzicht vor? |
| 2 | Ist die Sanierung unternehmensbezogen (§ 3a Abs. 2 EStG)? |
| 3 | Sanierungsbedürftigkeit: Krise dokumentiert? |
| 4 | Sanierungsfähigkeit: Konzept mit Fortbestehensprognose? |
| 5 | Sanierungsabsicht: schriftlich von Gläubigern? |
| 6 | Sanierungseignung: objektiv geeignete Maßnahme? |
| 7 | Antrag nach § 3a Abs. 4 EStG gestellt? |
| 8 | Verlustreihenfolge § 3c Abs. 4 EStG beachtet? |

## Trade-off-Matrix

| Konstellation | § 3a EStG einschlägig? |
|---|---|
| Verzicht durch Lieferanten in laufendem Geschäft ohne Krise | Nein — keine Sanierungsbedürftigkeit |
| Verzicht im Rahmen von Vergleich vor Liquidation | Nein — Sanierungseignung fehlt |
| Verzicht im StaRUG-Plan | Ja, wenn Konzept tragfähig |
| Verzicht im Insolvenzplan | Ja, mit IDW S 6-Konzept regelmäßig erfüllt |
| Schuldenerlass durch Gesellschafter zu Eigenkapitalstärkung | Häufig nicht § 3a, sondern verdeckte Einlage |
| Vergleich mit einzelnen Gläubigern, ohne Konzept | Schwierig — Sanierungsfähigkeit muss nachweisbar sein |

## Praxistipps der alten Hasen

- **Die "Sanierungsabsicht" ist die Innenseite des Gläubigers.** Sie ist die häufigste Bruchstelle. Lassen Sie Gläubiger schriftlich erklären: "Ich verzichte zum Zweck der Sanierung der [Firma]". Eine schlichte Verzichtserklärung ohne Bezug reicht oft nicht.
- **Sanierungsbedürftigkeit ist objektiv.** BWA, Bilanz, Liquiditätsplan müssen die Krise zeigen. Ein "es läuft schlecht" reicht nicht.
- **Sanierungsfähigkeit erfordert ein Konzept.** IDW S 6 ist der Goldstandard. Bei kleineren Sanierungen reicht ein strukturiertes Kurzkonzept, das dieselben Bausteine enthält.
- **Sanierungseignung ist Plausibilitätskontrolle.** Die Maßnahme muss objektiv geeignet sein. Wenn der Verzicht 10 % der Verbindlichkeiten reduziert und das Konzept fordert eine Reduktion von 80 %, ist die Eignung zu verneinen.
- **§ 3a EStG begünstigt Erträge, nicht Maßnahmen.** Nur der durch den Verzicht entstehende Ertrag ist betroffen — andere Erträge (z. B. aus operativem Geschäft) bleiben voll steuerpflichtig.

## Mustertexte / Berechnungsbeispiele

### Mustererklärung Gläubiger zu Sanierungsabsicht

```
[Briefkopf Gläubiger]

Verzichtserklärung zum Zweck der Sanierung

Hiermit verzichten wir, [Gläubiger], gegenüber [Schuldnerin]
auf Forderungen in Höhe von EUR [Betrag] aus [Rechnung,
Darlehen, Bürgschaft etc.].

Dieser Verzicht erfolgt ausdrücklich zum Zweck der Sanierung
der Schuldnerin im Sinne des § 3a Abs. 1 EStG. Wir gehen davon
aus, dass die Schuldnerin durch dieses und parallele Verzichte
ihre Zahlungsfähigkeit und Rentabilität wiederherstellt.

Diese Erklärung dient auch dem Nachweis der Sanierungsabsicht
gegenüber dem Finanzamt.

[Ort], [Datum]
[Unterschrift Gläubiger]
```

### Berechnungsschema § 3a Abs. 3 EStG

```
Sanierungsertrag brutto (Verzichtsbetrag) EUR [A]
abzgl. mit dem Sanierungsertrag wirtschaftlich
 zusammenhängende Aufwendungen (Berater,
 Rechtskosten — § 3c Abs. 1, Abs. 4 EStG) EUR [B]
Sanierungsertrag netto EUR [A-B]
abzgl. zu verrechnender Verlustvortrag § 3c IV EStG EUR [C]
verbleibender Sanierungsertrag (steuerbefreit gem.
§ 3a Abs. 1 EStG bei Antrag § 3a Abs. 4 EStG) EUR [A-B-C]
```

### Subsumtionsmuster Vier Voraussetzungen — Gutachtenformat

```
A. Sanierungsbedürftigkeit
Die Sanierungsbedürftigkeit setzt voraus, dass das
Unternehmen ohne Sanierungsmaßnahmen mit hoher Wahr-
scheinlichkeit insolvent würde. Hier liegen folgende
Indikatoren vor:
- Eigenkapital negativ in Höhe von EUR [...]
- Liquiditätslücke binnen [Frist] absehbar
- Verlustreihe Wj X-3 bis X-1: EUR [...]
► Sanierungsbedürftigkeit liegt vor.

B. Sanierungsfähigkeit
Mit den geplanten Maßnahmen — siehe IDW-S-6-Konzept vom
[Datum] (Anlage [...]) — ist eine Fortführung des
Unternehmens überwiegend wahrscheinlich. Die integrierte
Planung 24 Monate weist [...].
► Sanierungsfähigkeit liegt vor.

C. Sanierungsabsicht der Gläubiger
Die Gläubiger haben mit Schreiben vom [Datum] aus-
drücklich erklärt, dass der Verzicht zum Zweck der
Sanierung erfolgt. Die Erklärungen entsprechen den
Anforderungen des BMF-Schreibens vom 27.04.2017.
► Sanierungsabsicht liegt vor.

D. Sanierungseignung
Die Maßnahmen sind quantitativ und qualitativ geeignet,
die Krise der Mandantin nachhaltig zu beseitigen. Im
Maßnahmenkatalog (Anlage [...]) sind [...].
► Sanierungseignung liegt vor.

E. Ergebnis
§ 3a Abs. 1 EStG ist anwendbar. Antrag § 3a Abs. 4 EStG
wird gestellt; § 3c Abs. 4 EStG-Verlustreihenfolge wird
beachtet; parallel § 7b GewStG-Antrag.
```

## Typische Fehler

- Sanierungsabsicht nur mündlich; FA lehnt ab.
- Sanierungsbedürftigkeit nicht ausreichend belegt; nur "Eindruck" statt Zahlen.
- IDW S 6-Konzept fehlt; Sanierungsfähigkeit nicht objektivierbar.
- Sanierungseignung nicht plausibilisiert; Maßnahme zu klein.
- § 3a Abs. 2 EStG (unternehmensbezogen) mit personenbezogen verwechselt.

## Querverweise

- `stb-sanierungsgewinn-3a-estg-unternehmens-vs-person`
- `stb-sanierungsgewinn-3a-iv-estg-antrag-und-bindungswirkung`
- `stb-sanierungsgewinn-3c-iv-estg-verlustreihenfolge`
- `stb-sanierungsgewinn-bmf-2017-sanierungserlass-nachfolge`
- `stb-sanierungsgewinn-vorbereitungs-checkliste`

## Quellen Stand 06/2026

### Normen

- § 3a Abs. 1, 2, 3, 4 EStG.
- § 8 Abs. 1 KStG.
- § 3c Abs. 4 EStG.
- § 5 Abs. 2a EStG.
- § 7b GewStG.
- § 11 KStG (Liquidationsbesteuerung).
- BMF-Schreiben vom 27.04.2017 — vor Verwendung Stand prüfen.
- IDW S 6 (Sanierungskonzept).

### Rechtsprechung (verifiziert)

- **BFH, Urt. v. 19.08.2020 — XI R 32/18, BStBl. II 2021, 279** — § 5 Abs. 2a EStG bei Rangrücktritt.
- **BFH, Urt. v. 30.11.2011 — I R 100/10, DStR 2012, 450** — Passivierungsvoraussetzungen.
- **FG Köln, Urt. v. 06.03.2012 — 13 K 3006/11, GmbHR 2012, 977** (vorgehend zu BFH I R 34/12) — Liquidations-Kernentscheidung Os. 7.
- **BFH, Beschl. v. 05.02.2014 — I R 34/12, BFH/NV 2014, 1014** — Ls. 3: Streitstand nicht evident rechtsfehlerhaft.
- **FG Düsseldorf, Urt. v. 18.09.2018 — 6 K 454/15 K, DStRE 2019** — Mindestbesteuerung Definitiveffekt; Rev. anh. BFH I R 36/18 (ausgesetzt wegen BVerfG 2 BvL 19/14, Vorlage BFH I R 59/12).

### Verwaltungsauffassung

- **OFD Frankfurt a. M., Rundverfügung v. 26.07.2021 — S 2743 A-12-St 523, BeckVerw 556782** und **v. 03.08.2018 — S 2743 A-12-St 525, DStR 2019, 560**.
- **OFD Frankfurt, Verfügung v. 27.12.2018, BeckVerw 447487** — Einsprüche zur Mindestbesteuerung ruhend zu stellen.
- **OFD Nordrhein-Westfalen, Kurzinformation ESt Nr. 46/2014, akt. 22.09.2017, DB 2017, 2580**.

### Querverweis Liquidations-Fachmodul

- `stb-sanierungsgewinn-stehengelassene-verbindlichkeiten` — Drei-Phasen-Analyse zur Behandlung stehen gelassener Verbindlichkeiten in der Liquidation.

## 3. `stb-sanierungsgewinn-3a-estg-unternehmens-vs-person`

**Fokus:** Abgrenzung unternehmensbezogene Sanierung gegen personenbezogene Sanierung im Sinne § 3a EStG. § 3a EStG schützt nur die unternehmensbezogene Variante; Restschuldbefreiung Privatperson fällt unter § 3a Absatz 5.

# § 3a EStG — unternehmensbezogen vs. personenbezogen

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `§ 3a EStG — unternehmensbezogen vs. personenbezogen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

§ 3a EStG unterscheidet zwischen unternehmensbezogener Sanierung (§ 3a Abs. 1, 2 EStG) und personenbezogener Sanierung (§ 3a Abs. 5 EStG — Restschuldbefreiung). Wer die Variante falsch zuordnet, stellt entweder den falschen Antrag oder gar keinen. Dieser Skill arbeitet die Abgrenzung systematisch heraus.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Ist Schuldner eine Kapitalgesellschaft (regelmäßig unternehmensbezogen) oder eine natürliche Person?
2. Bei Personengesellschaft / Einzelunternehmen: Betrifft der Verzicht das Betriebs- oder das Privatvermögen?
3. Liegt ein Restschuldbefreiungsverfahren (§§ 286 ff. InsO) vor?
4. Welches Wirtschaftsgut wird verzichtet — Betriebsdarlehen, Lieferantenforderung, Privatdarlehen?
5. Hat der Schuldner ein Unternehmen, das fortgeführt werden soll?

## Rechtlicher Rahmen

- **§ 3a Abs. 1, 2 EStG** — unternehmensbezogene Sanierung; Anwendungsbereich Betrieb.
- **§ 3a Abs. 5 EStG** — Schuldenerlass durch Restschuldbefreiung; eigenständiger Befreiungstatbestand für natürliche Personen.
- **§ 3a Abs. 4 EStG** — Antrag in beiden Varianten.
- **§ 4 EStG, § 5 EStG** — Betriebsvermögensvergleich; Abgrenzung Betrieb / Privat.
- **§§ 286 ff. InsO** — Restschuldbefreiungsverfahren.

## / Schritt für Schritt

### Variante A: unternehmensbezogene Sanierung (§ 3a Abs. 1, 2 EStG)

| Kriterium | Inhalt |
|---|---|
| Schuldner | Unternehmen, das fortgeführt werden soll |
| Anwendungsbereich | Betriebs-/Unternehmensvermögen |
| Ziel | Wiederherstellung Zahlungsfähigkeit und Rentabilität |
| Vier Voraussetzungen | Bedürftigkeit, Fähigkeit, Absicht, Eignung — kumulativ |
| Antragspflicht | § 3a Abs. 4 EStG |
| Wirkung | Steuerbefreiung des Sanierungsertrags |

### Variante B: personenbezogene Sanierung (§ 3a Abs. 5 EStG — Restschuldbefreiung)

| Kriterium | Inhalt |
|---|---|
| Schuldner | Natürliche Person im Restschuldbefreiungsverfahren |
| Anwendungsbereich | Auch Privatvermögen / private Schulden |
| Ziel | Wirtschaftlicher Neuanfang nach Verbraucherinsolvenz |
| Voraussetzung | Restschuldbefreiung gem. §§ 286 ff. InsO erteilt |
| Antrag | § 3a Abs. 4 EStG analog |
| Wirkung | Steuerbefreiung der Erträge aus erlassenen Schulden |

### Subsumtions-Reihenfolge

| Schritt | Frage |
|---|---|
| 1 | Ist der Schuldner natürliche oder juristische Person? |
| 2 | Bei natürlicher Person: läuft Restschuldbefreiungsverfahren? |
| 3 | Wenn ja: § 3a Abs. 5 EStG |
| 4 | Wenn nein, aber Einzelunternehmen mit Sanierungslage: § 3a Abs. 1 EStG (unternehmensbezogen) |
| 5 | Bei juristischer Person: stets § 3a Abs. 1 EStG |
| 6 | Bei Personengesellschaft: prüfen, ob Verzicht das Betriebs- oder das Privatvermögen der Mitunternehmer betrifft (siehe Folge-Skill) |

## Trade-off-Matrix

| Konstellation | § 3a EStG-Variante | Bemerkung |
|---|---|---|
| GmbH mit StaRUG-Plan | Abs. 1, 2 (unternehmensbezogen) | Standard |
| Einzelunternehmen, Betrieb saniert | Abs. 1, 2 | Betrieb wird fortgeführt |
| Einzelunternehmen, Betrieb aufgegeben | Möglich nur Abs. 5 wenn Privatinsolvenz | Sonst voll steuerpflichtig |
| Natürliche Person mit Restschuldbefreiung | Abs. 5 | Andere Voraussetzungen |
| GbR / KG: Verzicht im Betriebsvermögen | Abs. 1, 2 | Anteilig je Mitunternehmer |
| Gesellschafter verzichtet auf Darlehen an seine GmbH | Häufig nicht § 3a; verdeckte Einlage | Eigene Prüfung |

## Praxistipps der alten Hasen

- **"Unternehmensbezogen" verlangt eine echte Fortführung.** Wer den Betrieb aufgibt und nur einzelne Vermögensgegenstände verwertet, fällt nicht unter § 3a Abs. 1 EStG. Hier hilft ggf. nur die Liquidations-Konstellation (siehe Sonder-Skill FG Köln).
- **§ 3a Abs. 5 EStG (Restschuldbefreiung) ist eigenständig.** Die vier Voraussetzungen des Abs. 1 müssen hier nicht in derselben Form vorliegen — Voraussetzung ist die Erteilung der Restschuldbefreiung.
- **Personengesellschaft: gemischte Lage möglich.** Verzicht auf Gesellschafterdarlehen im Sonderbetriebsvermögen wird einkommensteuerlich beim Mitunternehmer; Verzicht auf Bankdarlehen im Gesamthandsvermögen wird auf alle Mitunternehmer verteilt.
- **Bei verdeckter Einlage durch Gesellschafter** ist § 3a EStG nicht das richtige Instrument. Der Verzicht des Gesellschafters auf eine werthaltige Forderung ist Einlage (§ 4 Abs. 1 S. 1 EStG / § 27 KStG); nicht werthaltige Forderung führt zum vollen Ertrag bei der Gesellschaft.

## Mustertexte / Berechnungsbeispiele

### Memo-Bausteine zur Variantenwahl

```
Memo: Variantenwahl § 3a EStG

I. Sachverhalt
[Schuldner X plant Forderungsverzicht von Y EUR ...]

II. Rechtsfrage
Ist der Verzicht unternehmensbezogen (§ 3a Abs. 1 EStG)
oder personenbezogen (§ 3a Abs. 5 EStG)?

III. Subsumtion
1. Schuldner ist [natürliche/juristische Person ...]
2. Verzicht betrifft [Betriebs-/Privatvermögen ...]
3. [Restschuldbefreiungsverfahren läuft / läuft nicht ...]
4. Unternehmensfortführung [beabsichtigt / nicht beabsichtigt ...]

IV. Ergebnis
§ 3a Abs. [1 / 5] EStG anwendbar.

V. Folge: Antrag § 3a Abs. 4 EStG mit Berücksichtigung
 der spezifischen Voraussetzungen.
```

### Berechnungsbeispiel Personengesellschaft mit gemischtem Verzicht

```
KG mit zwei Kommanditisten 50/50:

Verzicht Bankdarlehen Gesamthandsvermögen EUR 800.000
 ► je Mitunternehmer EUR 400.000 Sanierungsertrag
 ► je Mitunternehmer Antrag § 3a Abs. 4 EStG

Verzicht Gesellschafterdarlehen Kommanditist A
 Sonderbetriebsvermögen EUR 200.000
 ► nur Kommanditist A betroffen
 ► getrennte Prüfung in dessen Steuererklärung
```

## Typische Fehler

- Falsche Variante (Abs. 1 statt Abs. 5) bei natürlicher Person mit Restschuldbefreiung.
- Bei Personengesellschaft alle Mitunternehmer pauschal behandelt; Sonderbetriebsvermögen übersehen.
- Verzicht des Gesellschafters fälschlich als § 3a EStG-Sachverhalt; in Wirklichkeit verdeckte Einlage.
- Aufgabe Betrieb und § 3a Abs. 1 EStG-Antrag — fehlende Unternehmensfortführung.

## Querverweise

- `stb-sanierungsgewinn-3a-estg-grundtatbestand`
- `stb-sanierungsgewinn-personengesellschaft-und-mitunternehmer`
- `stb-sanierungsgewinn-koerperschaftsteuer-vs-einkommensteuer`
- `stb-sanierungsgewinn-liquidation-nachrang-fg-koeln`
- `stb-sanierungsgewinn-debt-equity-swap-statt-verzicht`

## Quellen Stand 06/2026

- § 3a Abs. 1, 2, 4, 5 EStG.
- § 4 Abs. 1 S. 1 EStG (verdeckte Einlage).
- § 5 EStG.
- § 27 KStG.
- §§ 286 ff. InsO (Restschuldbefreiung).
- BMF-Schreiben vom 27.04.2017 — vor Verwendung Stand prüfen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; Quelle vor Ausgabe protokollieren.

## 4. `stb-sanierungsgewinn-3a-iv-estg-antrag-und-bindungswirkung`

**Fokus:** Antrag nach § 3a Absatz 4 EStG: Form, Frist, Inhalt und Bindungswirkung. Nach Feststellung des Sanierungserfolgs ist der Antrag nicht mehr zurücknehmbar; strategische Konsequenzen sind vor Antragstellung abzuwägen.

# § 3a Abs. 4 EStG — Antrag und Bindungswirkung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `§ 3a Abs. 4 EStG — Antrag und Bindungswirkung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

§ 3a Abs. 4 EStG macht die Steuerbefreiung vom ausdrücklichen Antrag abhängig. Der Antrag wirkt bindend: Nach Feststellung des Sanierungserfolgs kann er nicht mehr zurückgenommen werden. Die Folge ist endgültig — alle steuerlichen Wahlrechte zu Verlustverbrauch und Aufwandsabzug sind dann gesetzt.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Soll der Antrag tatsächlich gestellt werden — oder reicht der Verlustvortrag (Sanity-Check)?
2. Wann ist der späteste Zeitpunkt für den Antrag?
3. Was sind die Folgen der Bindungswirkung für den Verlustvortrag?
4. Sind alle vier Voraussetzungen (§ 3a Abs. 1 EStG) dokumentiert?
5. Ist parallel § 7b GewStG zu beantragen?

## Rechtlicher Rahmen

- **§ 3a Abs. 4 EStG** — Antrag erforderlich; Bindungswirkung nach Sanierungserfolg.
- **§ 3a Abs. 1 EStG** — Materielle Voraussetzungen.
- **§ 3c Abs. 4 EStG** — Verlustverbrauch als zwingende Folge.
- **§ 7b GewStG** — paralleler Antrag.
- **§ 149 AO** — Steuererklärung.
- **§ 164 AO** — Festsetzung unter Vorbehalt; eventuelle Rücknahme der Steuerfestsetzung im Vorbehaltsverfahren.

## / Schritt für Schritt

| Schritt | Inhalt | Output |
|---|---|---|
| 1 | Sanity-Check: Verlustvortrag deckt Ertrag? | Wenn ja: kein Antrag |
| 2 | Vier Voraussetzungen § 3a Abs. 1 EStG dokumentiert? | Beweispaket |
| 3 | Sanierungsjahr identifizieren — Geschäftsjahr des Verzichts | Wirtschaftsjahr |
| 4 | Antrag formuliert — siehe Mustertext | Antragsentwurf |
| 5 | Antrag mit Steuererklärung für Sanierungsjahr einreichen (KSt-/ESt-Erklärung) | Eingegangen FA |
| 6 | Parallel § 7b GewStG-Antrag mit Gewerbesteuererklärung | Eingegangen FA |
| 7 | FA-Bearbeitung; ggf. Nachfragen, Steuerakten-Einsicht | Bescheid |
| 8 | Steuerbescheid Sanierungsjahr unter Vorbehalt § 164 AO? | Spätere Korrektur möglich |
| 9 | Bei Streit: Einspruch § 347 AO | Verfahren |
| 10 | Nach Sanierungserfolg: Bindungswirkung eingetreten | Keine Rücknahme |

## Trade-off-Matrix

| Antrag stellen? | Verlustvortrag? | Empfehlung |
|---|---|---|
| Ja | Niedrig vs. Sanierungsertrag | Ja zwingend |
| Ja | Hoch, deckt vollständig | Nein, entbehrlich (Sanity-Check) |
| Ja | Mittel, deckt teilweise | Ja für übersteigenden Teil |
| Ja | Bei Streit Bedürftigkeit/Eignung | Verbindliche Auskunft § 89 AO vorab |
| Ja | International | Vorher Betriebsstätten klären |
| Ja | Personengesellschaft | Antrag je Mitunternehmer prüfen |

## Praxistipps der alten Hasen

- **Bindungswirkung ist die Falle.** Stellen Sie nicht "vorsorglich" Antrag. Wenn sich später herausstellt, dass die Sanierung schwächer ist oder ein Verlustvortrag verfügbar wäre, sind Sie gebunden.
- **Steuerbescheid unter Vorbehalt § 164 AO sichern.** Im Sanierungsjahr kann der Sachverhalt sich noch entwickeln (z. B. weitere Verzichtsangebote). Vorbehalt lässt nachträgliche Anpassung zu — die Antragsbindungswirkung greift erst mit Erfolgsfeststellung.
- **§ 7b GewStG nicht vergessen.** Der Sanierungsantrag § 3a EStG / § 8 Abs. 1 KStG schließt die Gewerbesteuer-Befreiung NICHT automatisch ein. Eigener Antrag mit Gewerbesteuererklärung.
- **Form: keine bestimmte vorgeschrieben.** In der Praxis: ausdrücklicher Antragstext in der Steuererklärung oder beigefügtes Schreiben. Wichtig: Bezug auf § 3a Abs. 4 EStG und Sanierungsjahr.
- **Frist: praktisch mit Steuererklärung.** Eine spätere Antragstellung im Einspruchsverfahren ist umstritten; verlassen Sie sich nicht darauf.

## Mustertexte / Berechnungsbeispiele

### Muster Antrag § 3a Abs. 4 EStG (Anlage zur Steuererklärung)

```
[Briefkopf Steuerberater / Anwalt]
An das Finanzamt [Ort]
- Steuernummer [Nr.] / Sachgebiet [Nr.] -

Anlage zur [Körperschaft-/Einkommen-]Steuererklärung
[Wirtschaftsjahr] der [Firma]

Betreff: Antrag nach § 3a Abs. 4 EStG —
 Sanierungsertrag in Höhe von EUR [Betrag]

Sehr geehrte Damen und Herren,

namens und in Vollmacht unserer Mandantin beantragen wir die
Steuerbefreiung des im Wirtschaftsjahr [...] entstandenen
Sanierungsertrags in Höhe von EUR [Betrag] nach § 3a Abs. 1 EStG.

I. Sachverhalt
Die [Firma] befand sich im Wirtschaftsjahr [...] in einer
existenzbedrohenden Krise. Die in Anlage 1 beigefügte
Liquiditätsplanung und die in Anlage 2 beigefügte Krisen-
ursachenanalyse belegen die Sanierungsbedürftigkeit.

Durch im Anlagenkonvolut 3 beigefügte schriftliche Verzichts-
erklärungen der Gläubiger [...] verzichteten diese auf
Forderungen in Höhe von insgesamt EUR [Betrag]. Hieraus
ergibt sich ein außerordentlicher Ertrag (Sanierungsertrag)
in entsprechender Höhe.

II. Vier Voraussetzungen § 3a Abs. 1 EStG
1. Sanierungsbedürftigkeit: Anlagen 1 und 2.
2. Sanierungsfähigkeit: IDW S 6-Konzept vom [Datum] —
 Anlage 4.
3. Sanierungsabsicht der Gläubiger: Schriftliche
 Erklärungen — Anlagen 3.
4. Sanierungseignung: Maßnahmenkatalog und Quote —
 Anlage 5.

III. Berechnung Sanierungsertrag nach § 3a Abs. 3 EStG
Sanierungsertrag brutto EUR [A]
abzgl. zusammenhängende Aufwendungen EUR [B]
Sanierungsertrag netto EUR [A-B]
abzgl. Verlustvortrag § 3c Abs. 4 EStG EUR [C]
verbleibender steuerbefreiter Ertrag EUR [A-B-C]

IV. Anträge
1. Steuerbefreiung in Höhe von EUR [A-B-C] gem.
 § 3a Abs. 1 EStG.
2. Festsetzung unter Vorbehalt der Nachprüfung
 gem. § 164 AO bis Abschluss des Sanierungsverfahrens.

Mit freundlichen Grüßen
[Berater]
```

### Berechnungsschema mit Bindungswirkungs-Folge

```
Schritt 1: Antrag § 3a Abs. 4 EStG ► gestellt
Schritt 2: FA prüft vier Voraussetzungen
Schritt 3: FA stellt Sanierungserfolg fest
Schritt 4: Bindungswirkung greift ► Rücknahme ausgeschlossen
Schritt 5: Verlustvortrag wurde verbraucht ► dauerhaft weg
Schritt 6: Bei späterer Streit: nur noch Steuerbescheid-
 Korrektur, kein neuer Wahlrechtsweg
```

## Typische Fehler

- Antrag gestellt, obwohl Verlustvortrag voll deckt — Bindungswirkung greift dennoch.
- § 7b GewStG-Antrag vergessen; Gewerbesteuer voll steuerpflichtig.
- Antrag im Einspruchsverfahren nachgereicht; FA bestreitet Zulässigkeit.
- Vier Voraussetzungen nicht vollständig dokumentiert; FA lehnt ab.
- Sanierungsjahr falsch zugeordnet (Verzicht im Vorjahr, Antrag im Folgejahr).

## Querverweise

- `stb-sanierungsgewinn-3a-estg-grundtatbestand`
- `stb-sanierungsgewinn-verlustvortrag-sanity-check`
- `stb-sanierungsgewinn-3c-iv-estg-verlustreihenfolge`
- `stb-sanierungsgewinn-7b-gewstg-gewerbesteuer-parallel`
- `stb-sanierungsgewinn-bmf-2017-sanierungserlass-nachfolge`

## Quellen Stand 06/2026

- § 3a Abs. 1, 3, 4 EStG.
- § 8 Abs. 1 KStG (Verweis aus KSt).
- § 7b GewStG.
- § 3c Abs. 4 EStG.
- § 149 AO (Steuererklärung).
- § 164 AO (Vorbehalt der Nachprüfung).
- § 89 AO (verbindliche Auskunft).
- § 347 AO (Einspruch).
- BMF-Schreiben vom 27.04.2017 — vor Verwendung Stand prüfen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; Quelle vor Ausgabe protokollieren.

## 5. `stb-sanierungsgewinn-bmf-2017-sanierungserlass-nachfolge`

**Fokus:** BMF-Schreiben vom 27.04.2017 als Verwaltungsanweisung zur Nachfolge des Sanierungserlasses. Konkretisiert die vier Voraussetzungen des § 3a EStG aus Verwaltungssicht; vor Verwendung aktuellen BMF-Stand prüfen.

# BMF-Schreiben 27.04.2017 — Sanierungserlass-Nachfolge

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `BMF-Schreiben 27.04.2017 — Sanierungserlass-Nachfolge` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Das BMF-Schreiben vom 27.04.2017 ist die Verwaltungsanweisung, die den früheren Sanierungserlass (BMF 27.03.2003) nach der Entscheidung des Großen Senats des BFH (Modellwissen — vor Verwendung Quelle prüfen) ersetzt hat. Es konkretisiert, wie die Finanzverwaltung die vier Voraussetzungen des § 3a EStG (gesetzliche Verankerung durch Wachstumschancengesetz, BGBl. I 2024 — Stand prüfen) prüft und welche Nachweise im Antragsverfahren erforderlich sind.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Welcher Bearbeitungsstand des BMF-Schreibens ist im konkreten Mandat aktuell?
2. Gibt es Übergangsregelungen für Altfälle (Verzichte vor Inkrafttreten der gesetzlichen Verankerung)?
3. Soll auf BMF 27.04.2017 oder direkt auf § 3a EStG abgestellt werden?
4. Wie sieht die FA-Praxis im konkreten Veranlagungsbezirk aus (Regionalisierungs-Tendenzen)?
5. Ist eine verbindliche Auskunft § 89 AO ausreichend für die FA-Bindung an die Verwaltungsanweisung?

## Rechtlicher Rahmen

- **BMF-Schreiben vom 27.04.2017** — Verwaltungsanweisung; Nachfolger des Sanierungserlasses 27.03.2003.
- **§ 3a EStG** — gesetzliche Verankerung; Wachstumschancengesetz BGBl. I 2024 (Stand prüfen).
- **§ 3a Abs. 1, 2, 3, 4 EStG** — materielle Voraussetzungen.
- **§ 3c Abs. 4 EStG** — Verlustreihenfolge.
- **§ 7b GewStG** — Gewerbesteuer.
- **§ 89 AO** — verbindliche Auskunft.

## / Schritt für Schritt

### Vier Voraussetzungen im BMF-Schreiben konkretisiert

| Voraussetzung | BMF-Konkretisierung (Indizien) |
|---|---|
| Sanierungsbedürftigkeit | Verlustreihe; negative Liquiditätsplanung; Insolvenzgefahr binnen kurzer Zeit |
| Sanierungsfähigkeit | Tragfähiges Konzept; integrierte Planung 24 Monate; Maßnahmen quantifiziert |
| Sanierungsabsicht der Gläubiger | Schriftlich; ausdrücklich auf Sanierungszweck bezogen |
| Sanierungseignung | Plausibilität der Maßnahmen; ausreichende Quote |

### Anwendungs-Workflow

| Schritt | Inhalt |
|---|---|
| 1 | Aktuellen Stand des BMF-Schreibens beim BMF / im BStBl. abrufen |
| 2 | Konkrete Sanierungssituation auf BMF-Kriterien spiegeln |
| 3 | Für jede Voraussetzung: Nachweisbündel zusammenstellen |
| 4 | Verbindliche Auskunft § 89 AO erwägen, wenn FA-Praxis unklar |
| 5 | Antrag § 3a Abs. 4 EStG mit Hinweis auf BMF-Schreiben |
| 6 | Bei Ablehnung: Einspruch unter Bezugnahme auf BMF und § 3a EStG |

## Trade-off-Matrix

| Konstellation | BMF-Bezug? |
|---|---|
| Standard-Sanierungsantrag | BMF zusätzlich zu § 3a EStG referenzieren |
| Streitige Voraussetzung | BMF-Konkretisierung zitieren als FA-Bindung |
| Altfall (Verzicht vor gesetzlicher Verankerung) | Übergangsregelung BMF prüfen |
| Internationaler Sachverhalt | BMF nur eingeschränkt einschlägig — § 3a EStG primär |
| Verwaltungsänderung im laufenden Verfahren | Vertrauensschutz prüfen |

## Praxistipps der alten Hasen

- **Verwaltungsanweisungen binden die Verwaltung.** Wenn das BMF-Schreiben einen Punkt konkretisiert und das FA daraus abweicht, ist das ein Argument für den Einspruch.
- **Stand prüfen.** Das BMF-Schreiben kann durch Ergänzungen oder Neufassungen geändert sein. Verlassen Sie sich nicht auf Modellwissen, sondern rufen Sie den aktuellen Stand im BStBl. oder beim BMF ab.
- **Verbindliche Auskunft als Sicherheit.** Wenn das BMF-Schreiben Spielräume lässt, ist eine verbindliche Auskunft § 89 AO sinnvoll. Sie bindet das konkrete FA — und führt zu einer Gebühr nach § 89 Abs. 5 AO.
- **BMF-Schreiben ist nicht für das Gericht verbindlich.** Im Streit vor dem Finanzgericht ist das Gericht an § 3a EStG, nicht an die Verwaltungsanweisung gebunden. Der BMF-Bezug ist trotzdem nützlich, weil das Gericht häufig die Verwaltungspraxis als Auslegungshilfe heranzieht.

## Mustertexte / Berechnungsbeispiele

### Antragsbaustein mit BMF-Bezug

```
[Antrag § 3a Abs. 4 EStG — Auszug]

Die Voraussetzungen einer unternehmensbezogenen Sanierung
im Sinne § 3a Abs. 1 EStG sind nach Maßgabe des BMF-Schreibens
vom 27.04.2017 (BStBl. I [..., Seite ...]) erfüllt:

1. Sanierungsbedürftigkeit
 Die Mandantin wies in den Jahren [X-3] bis [X-1] eine
 Verlustreihe von kumuliert EUR [Betrag] aus. Die
 integrierte Liquiditätsplanung zeigt einen Liquiditäts-
 Bedarf von EUR [...] bis [Stichtag], der ohne Sanierung
 nicht gedeckt werden konnte (Anlage 1).

2. Sanierungsfähigkeit
 Das IDW S 6-Konzept des Sanierungsberaters
 [Name] vom [Datum] (Anlage 4) weist die Fortführung
 bei Durchführung der vorgeschlagenen Maßnahmen aus.
 Die integrierte Planung für [24 Monate ab Stichtag]
 ist Teil des Konzepts.

3. Sanierungsabsicht der Gläubiger
 Die Gläubiger [...] haben mit Schreiben vom [Datum]
 ausdrücklich erklärt, dass der jeweilige Verzicht
 "zum Zweck der Sanierung der Mandantin" erfolgt
 (Anlagen 3.1 bis 3.n). Diese Formulierung entspricht
 der Konkretisierung in Abschnitt [...] des BMF-
 Schreibens 27.04.2017.

4. Sanierungseignung
 Die im Maßnahmenkatalog (Anlage 5) quantifizierten
 Maßnahmen führen nach den Planungen zu einer
 Verbesserung der Eigenkapitalquote von [X] % auf
 [Y] %; die Liquiditätsdeckungslücke wird geschlossen.

Wir bitten um steuerbefreite Festsetzung in Höhe von
EUR [Betrag] gem. § 3a Abs. 1 EStG.
```

### Memo-Baustein "Aktualität des BMF-Schreibens"

```
Memo: Aktualität BMF-Schreiben 27.04.2017

Stand der Recherche [Datum]:
- BMF-Schreiben 27.04.2017 abgerufen über [Quelle]
- Letzte Änderung: [Datum/aufzulisten]
- Übergangsregelung Altfälle: [vorhanden / nicht vorhanden]
- Aktuelle Verwaltungs-Praxis lt. Erlass: [...]

Hinweis: Der Stand ist mandatsbezogen zu prüfen. Modell-
wissen darf nicht zur Datierung der letzten Änderung
herangezogen werden.
```

## Typische Fehler

- BMF-Schreiben in der Fassung von 2017 zitiert, ohne aktuellen Stand zu prüfen.
- Vier Voraussetzungen ohne BMF-Konkretisierung dokumentiert; FA verlangt mehr.
- Verbindliche Auskunft nicht erbeten, obwohl konkretes FA streitig.
- Argument im Einspruch: BMF-Bindung nicht herausgearbeitet.

## Querverweise

- `stb-sanierungsgewinn-3a-estg-grundtatbestand`
- `stb-sanierungsgewinn-3a-iv-estg-antrag-und-bindungswirkung`
- `stb-sanierungsgewinn-vorbereitungs-checkliste`
- `stb-sanierungsgewinn-zustaendigkeiten-fa-betriebspruefung`
- `anw-verbindliche-auskunft`

## Quellen Stand 06/2026

- BMF-Schreiben vom 27.04.2017 — vor Verwendung aktuellen Stand im BStBl. abrufen.
- § 3a EStG (Wachstumschancengesetz BGBl. I 2024 — Stand prüfen).
- § 3a Abs. 1, 2, 3, 4 EStG.
- § 3c Abs. 4 EStG.
- § 7b GewStG.
- § 89 AO.
- Rechtsprechung (insb. Großer Senat BFH zum alten Sanierungserlass): keine Entscheidung aus Modellwissen zitieren; Quelle vor Ausgabe protokollieren.

## 6. `stb-sanierungsgewinn-forderungsverzicht-bilanzielle-darstellung`

**Fokus:** Bilanzielle Darstellung des Forderungsverzichts beim Schuldner und beim Gläubiger. Werthaltigkeit, außerordentlicher Ertrag, Ausweis in der GuV; Plan-Bilanz vor und nach Sanierung.

# Forderungsverzicht — bilanzielle Darstellung

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Forderungsverzicht — bilanzielle Darstellung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Der Forderungsverzicht durch Gläubiger ist beim Schuldner ein Buchgewinn. Wie er handelsrechtlich und steuerlich darzustellen ist, beeinflusst sowohl die Höhe des Sanierungsertrags als auch die Sichtbarkeit gegenüber dem FA. Dieser Skill stellt die Buchungslogik und die Plan-Bilanz-Erstellung dar.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Wer verzichtet — Bank, Lieferant, Gesellschafter?
2. Auf welche Verbindlichkeit wird verzichtet — Darlehen, Lieferantenforderung, Gesellschafterdarlehen?
3. Ist die Forderung werthaltig oder unverwerthaltig?
4. Soll der Verzicht handelsrechtlich (HGB) anders als steuerrechtlich gebucht werden?
5. Gibt es Besserungsabrede / Rangrücktritt?

## Rechtlicher Rahmen

- **§ 246 HGB** — Vollständigkeitsgrundsatz.
- **§ 252 HGB** — Allgemeine Bewertungsgrundsätze.
- **§ 247 Abs. 1, § 266 HGB** — Bilanzgliederung.
- **§ 275 HGB** — GuV-Gliederung; außerordentliche Erträge wurden mit BilRUG (2015) gestrichen, ggf. heute "sonstige betriebliche Erträge".
- **§ 5 Abs. 1 EStG** — Maßgeblichkeit.
- **§ 5 Abs. 2a EStG** — Passivierungsverbot bei Tilgung nur aus zukünftigen Gewinnen (Rangrücktritt-Falle).
- **§ 8 Abs. 3 KStG** — Verdeckte Einlage durch Gesellschafter.
- **§ 3a Abs. 3 EStG** — Berechnung Sanierungsertrag.

## / Schritt für Schritt

### Buchungslogik beim Schuldner

| Variante | Buchung |
|---|---|
| Verzicht durch Drittgläubiger (Bank, Lieferant) | Verbindlichkeit an außerordentlichen / sonstigen betrieblichen Ertrag |
| Verzicht durch Gesellschafter — werthaltige Forderung | Verbindlichkeit an Kapitalrücklage (verdeckte Einlage) |
| Verzicht durch Gesellschafter — nicht werthaltige Forderung | Verbindlichkeit an Kapitalrücklage in Höhe Teilwert; Restbetrag an Ertrag |
| Verzicht mit Besserungsabrede | Verbindlichkeit weiterhin passiviert mit Vermerk; bei Eintritt Wegfall an Ertrag |

### Werthaltigkeit prüfen

| Indikator | Werthaltig? |
|---|---|
| Schuldnerin solvent, Verbindlichkeit termingerecht bedient | Ja |
| Schuldnerin in Krise; aber Vermögen deckt Forderung | Teilweise — Teilwert |
| Schuldnerin überschuldet, keine Aussicht auf Rückzahlung | Nicht werthaltig |
| Verbindlichkeit nachrangig | Werthaltigkeit unsicher |

## Trade-off-Matrix

| Variante Verzicht | Bilanzielle Wirkung Schuldner | Steuerliche Wirkung |
|---|---|---|
| Drittgläubiger voll | Außerordentlicher Ertrag in voller Höhe | Sanierungsertrag § 3a EStG (mit Antrag steuerfrei) |
| Gesellschafter werthaltig | Erhöhung Kapitalrücklage; kein Ertrag | § 8 Abs. 3 KStG verdeckte Einlage; nicht § 3a EStG |
| Gesellschafter nicht werthaltig | Teilweise Einlage, teilweise Ertrag | Ertragsteil ggf. § 3a EStG |
| Verzicht mit Besserungsschein | Verbindlichkeit bleibt; spätere Buchung Ertrag bei Eintritt | Spätere Sanierungsertrags-Würdigung |
| Rangrücktritt qualifiziert | Verbindlichkeit bleibt (oder § 5 Abs. 2a EStG-Problem) | siehe Folge-Skill |

## Praxistipps der alten Hasen

- **Werthaltigkeit ist entscheidend.** Bei Gesellschafter-Verzicht muss die Werthaltigkeit der Forderung im Zeitpunkt des Verzichts bestimmt werden. Werthaltig = Einlage, nicht werthaltig = Ertrag. Die Einstufung ist häufig FA-streitig — vorher dokumentieren (Bonitätsanalyse, Vermögensaufstellung der Schuldnerin).
- **GuV-Ausweis seit BilRUG.** Außerordentliche Erträge gibt es im HGB-Schema nicht mehr (BilRUG 2015). Sanierungsertrag wird heute typischerweise unter "sonstige betriebliche Erträge" ausgewiesen — mit Erläuterung im Anhang.
- **Steuerbilanz vs. Handelsbilanz.** § 5 Abs. 1 EStG ordnet Maßgeblichkeit an; aber bei Sanierungsertrag kann die steuerliche Würdigung abweichen (z. B. § 8 Abs. 3 KStG verdeckte Einlage). Beachten Sie die Abweichung in der Mehr-Weniger-Rechnung.
- **Besserungsabrede ist ein Spezialfall.** Sie verschiebt den Ertrag in spätere Jahre, in denen die Schuldnerin wieder Gewinne erzielt. Steuerlich greift § 3a EStG erst bei tatsächlichem Wegfall — Antrag erst dann.
- **Plan-Bilanz vor und nach Sanierung** sind die wichtigsten Dokumente für das Mandat. Sie zeigen FA und Gläubigern den Effekt; sie sind aber auch das interne Steuerungsinstrument.

## Mustertexte / Berechnungsbeispiele

### Plan-Bilanz vor und nach Verzicht

```
Aktiva vor Sanierung nach Sanierung
Anlagevermögen EUR 2.500.000 EUR 2.500.000
Umlaufvermögen EUR 1.200.000 EUR 1.200.000
Summe Aktiva EUR 3.700.000 EUR 3.700.000

Passiva vor Sanierung nach Sanierung
Eigenkapital EUR -800.000 EUR -300.000
 davon Bilanzverlust EUR -2.500.000 EUR -2.000.000
Rückstellungen EUR 400.000 EUR 400.000
Verbindlichkeiten ggü. Kreditinst. EUR 2.500.000 EUR 1.700.000
 (Bankverzicht 800.000)
Verbindlichkeiten ggü. Lieferanten EUR 1.600.000 EUR 1.400.000
 (Lieferantenverzicht 200.000)
Summe Passiva EUR 3.700.000 EUR 3.200.000

Sanierungsertrag GuV EUR 0 EUR 1.000.000
```

### Buchungssätze (Beispiel)

```
Variante A — Drittgläubiger (Bank) verzichtet auf 800.000:
 Verbindlichkeiten Kreditinstitut 800.000
 an sonstiger betrieblicher Ertrag 800.000

Variante B — Gesellschafter verzichtet auf werthaltige 200.000:
 Verbindlichkeiten Gesellschafter 200.000
 an Kapitalrücklage 200.000

Variante C — Gesellschafter verzichtet auf nicht werthaltige
500.000 (Teilwert 100.000, Restbetrag 400.000 zum Ertrag):
 Verbindlichkeiten Gesellschafter 500.000
 an Kapitalrücklage 100.000
 an sonstiger betrieblicher Ertrag 400.000

Variante D — Verzicht mit Besserungsabrede:
 bei Eintritt der Besserung (z. B. Gewinn 300.000 in
 Folgejahr):
 Verbindlichkeit / Wegfall 300.000
 an sonstiger betrieblicher Ertrag 300.000
```

### Anhangs-Erläuterung

```
Anhang [Geschäftsjahr]:

Im Berichtsjahr wurde die Gesellschaft im Rahmen einer
unternehmensbezogenen Sanierung saniert. Die Gläubiger
[...] verzichteten auf Forderungen in Höhe von insgesamt
EUR 1.000.000. Der entstandene außerordentliche Ertrag
ist in der GuV unter "sonstige betriebliche Erträge"
ausgewiesen. Steuerlich wurde ein Antrag nach § 3a Abs. 4
EStG gestellt. Die vier Voraussetzungen einer unternehmens-
bezogenen Sanierung sind nach Auffassung der Geschäfts-
führung erfüllt.
```

## Typische Fehler

- Werthaltigkeit des Gesellschafter-Darlehens nicht dokumentiert; FA bestreitet.
- Außerordentlicher Ertrag in alter GuV-Position ausgewiesen (vor BilRUG); nach BilRUG nicht mehr zulässig.
- Plan-Bilanz vor und nach Sanierung nicht erstellt; Beweismittel fehlt.
- Buchungssatz fehlerhaft — z. B. Verbindlichkeit nicht ausgebucht.
- Besserungsabrede bilanziell nicht erkannt; Ertrag zu früh gebucht.

## Querverweise

- `stb-sanierungsgewinn-debt-equity-swap-statt-verzicht`
- `stb-sanierungsgewinn-rangruecktritt-und-5-abs-2a-estg`
- `stb-sanierungsgewinn-3a-estg-grundtatbestand`
- `stb-sanierungsgewinn-3a-iv-estg-antrag-und-bindungswirkung`
- `stb-sanierungsgewinn-3c-iv-estg-verlustreihenfolge`

## Quellen Stand 06/2026

### Normen

- §§ 246, 252, 247 Abs. 1, 266, 275 HGB.
- § 5 Abs. 1 EStG.
- § 5 Abs. 2a EStG.
- § 3a Abs. 1, 3, 4 EStG.
- § 8 Abs. 3 KStG.
- BilRUG (Bilanzrichtlinie-Umsetzungsgesetz).
- BMF-Schreiben vom 27.04.2017 — Stand prüfen.

### Rechtsprechung (verifiziert)

- **BFH, Urt. v. 30.11.2011 — I R 100/10, DStR 2012, 450** — Voraussetzungen der Passivierung von Verbindlichkeiten: bestimmter Verpflichtungsinhalt, durchsetzbar, wirtschaftliche Belastung.
- **BFH, Urt. v. 19.08.2020 — XI R 32/18, BStBl. II 2021, 279** — Anwendung des § 5 Abs. 2a EStG bei Rangruecktritt mit Tilgungsvorbehalt aus zukünftigen Gewinnen.
- **FG Köln, Urt. v. 06.03.2012 — 13 K 3006/11, GmbHR 2012, 977** — Liquidations-Kernentscheidung Os. 7 (Wegfall mit Erlöschen mangels Steuersubjekt).
- **BFH, Beschl. v. 05.02.2014 — I R 34/12, BFH/NV 2014, 1014** — nachgehend zu FG Köln 13 K 3006/11.
- **BFH, Urt. v. 16.05.2015 — IX R 28/14, BFH/NV 2015, 1679** — umgekehrter Fall: Forderung der Gesellschaft gegen Gesellschafter.

### Verwaltungsauffassung

- **OFD Frankfurt a. M., Rundverfügung v. 26.07.2021 — S 2743 A-12-St 523, BeckVerw 556782** — ertragsteuerliche Beurteilung von Darlehensverbindlichkeiten der Muttergesellschaft im Abwicklungsendvermögen der Tochter.
- **OFD Frankfurt a. M., Rundverfügung v. 03.08.2018 — S 2743 A-12-St 525, DStR 2019, 560** — Vorgängerverfügung.
- **OFD Nordrhein-Westfalen, Kurzinformation ESt Nr. 46/2014, akt. 22.09.2017, DB 2017, 2580**.

### Literatur

- Bergmann, Liquidationsbesteuerung von Kapitalgesellschaften, Diss., 2012, S. 145 ff.
- Dietrich/Weber, DStR 2019, 966, 970.
- Hageböke, in: Rödder/Herlinghaus/Neumann, KStG, 1. Aufl. 2015, § 11 Rn. 78.
- Stalbold, in: Gosch, KStG, § 11 Rn. 72.
- Micker, in: Herrmann/Heuer/Raupach, EStG/KStG, § 11 KStG Rn. 44.

### Querverweis Fachmodul

- `stb-sanierungsgewinn-stehengelassene-verbindlichkeiten` — Drei-Phasen-Analyse für stehen gelassene Verbindlichkeiten in der Liquidation.

## 7. `stb-sanierungsgewinn-fruehwarnung-monat-zwoelf-vor-plan`

**Fokus:** Frühwarn-Skill Sanierungsgewinn nach Paragraf 3a EStG. Rechnet 12 Monate vor Insolvenzantrag oder StaRUG-Anzeige rückwärts und zeigt Mandant und Berater wann welche Weiche zu stellen ist damit der Antrag nach Paragraf 3a Absatz 4 EStG nicht im letzten Moment platzt.

# Sanierungsgewinn — Frühwarnung 12 Monate vor Plan

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Frühwarnung 12 Monate vor Plan` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Der Sanierungsgewinn nach § 3a EStG ist der häufigste Stolperstein in der späten Sanierungsphase. Erfahrungsgemäß realisieren Mandantinnen und Mandanten erst dann, dass aus dem Forderungsverzicht der Gläubiger ein steuerpflichtiger Buchgewinn entsteht, wenn der Insolvenzplan oder das StaRUG-Restrukturierungsverfahren bereits bei Gericht eingereicht ist. Dann ist es regelmäßig zu spät, um die "vier Voraussetzungen" (Sanierungsbedürftigkeit, Sanierungsfähigkeit, Sanierungsabsicht der Gläubiger, Sanierungseignung) sauber zu dokumentieren.

Dieser Skill stellt die Zeitachse 12 Monate vor dem geplanten Antrag dar und zeigt monatlich, welche Weiche zu stellen ist.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Ist eine außergerichtliche Sanierung, ein StaRUG-Verfahren oder ein Insolvenzplan ernsthaft in Planung?
2. Welches Antragsdatum ist realistisch — in Monaten ab heute?
3. Wer ist Schuldnerin (Personengesellschaft, GmbH, Einzelunternehmen) und welches Wirtschaftsjahr läuft?
4. Liegen Verlustvorträge zur Körperschaft- oder Einkommensteuer vor und in welcher Höhe?
5. Welches Gewerbesteuer-Hebesatz-Niveau und welcher Gewerbeverlustvortrag bestehen?
6. Gibt es Drittgläubiger (Banken, Lieferanten) und welches Verzichtsvolumen ist im Gespräch?
7. Wer ist Steuerberater und ist er bereits eingebunden?

## Rechtlicher Rahmen

- **§ 3a EStG** — Steuerfreiheit des Sanierungsertrags bei unternehmensbezogener Sanierung; vier Voraussetzungen kumulativ.
- **§ 3a Abs. 4 EStG** — Antrag erforderlich; nach Sanierungserfolg keine Rücknahme.
- **§ 3c Abs. 4 EStG** — Verlustreihenfolge: Verlustvorträge mindern den Sanierungsertrag, bevor Steuerfreiheit greift.
- **§ 7b GewStG** — Parallel-Befreiung der Gewerbesteuer.
- **§ 10a Satz 1 GewStG** — Gewerbeverlust-Verbrauch entsprechend.
- **BMF-Schreiben vom 27.04.2017** (Sanierungserlass-Nachfolge) — verwaltungsseitige Konkretisierung der vier Voraussetzungen.
- Inkrafttreten der gesetzlichen Verankerung in § 3a EStG: Verifikation des aktuellen Standes (Wachstumschancengesetz, BGBl. I 2024) vor jedem Mandat.

## / Schritt für Schritt — die Zeitachse

| Monat vor Plan | Aufgabe | Verantwortlich | Output |
|---|---|---|---|
| M-12 | Erkennung Sanierungsfall; Mandantenwarnung versenden (siehe Skill `stb-sanierungsgewinn-mandantenwarnung-rechtzeitig`) | Anwalt/StB | Mandantenbrief |
| M-11 | Verlustvortrag-Sanity-Check ESt/KSt/GewSt (siehe Skill `stb-sanierungsgewinn-verlustvortrag-sanity-check`) | StB | Verlustvortrags-Tabelle |
| M-10 | Erstdiagnose: unternehmensbezogene vs. personenbezogene Sanierung (siehe Skill `stb-sanierungsgewinn-3a-estg-unternehmens-vs-person`) | Anwalt | Memo |
| M-9 | Sanierungsbedürftigkeit dokumentieren — BWA, Liquiditätsplan, Krisenursachenanalyse | StB + Anwalt | Sanierungskonzept Entwurf |
| M-8 | Sanierungsfähigkeit dokumentieren — Fortbestehensprognose, integrierte Planung 24 Monate | Sanierungsberater + StB | IDW S 6 / S 11 Entwurf |
| M-7 | Sanierungseignung dokumentieren — Maßnahmenkatalog, Quote, Realisierbarkeit | Anwalt + Sanierungsberater | Maßnahmenplan |
| M-6 | Sanierungsabsicht der Gläubiger dokumentieren — schriftliche Verzichtsangebote einholen | Anwalt | Gläubigerverhandlungs-Protokoll |
| M-5 | Bilanzielle Vorbereitung — Auswirkungen Forderungsverzicht modellieren (siehe Skill `stb-sanierungsgewinn-forderungsverzicht-bilanzielle-darstellung`) | StB | Plan-Bilanz |
| M-4 | Alternative debt-equity-swap prüfen (siehe Skill `stb-sanierungsgewinn-debt-equity-swap-statt-verzicht`) | Anwalt + StB | Optionsvergleich |
| M-3 | Verbindliche Auskunft FA erwägen — Sanierungsbedürftigkeit absichern lassen | Anwalt | Antrag § 89 AO |
| M-2 | Vermeidungsstrategien finalisieren (siehe Skill `stb-sanierungsgewinn-vermeidungsstrategien-praxis`) | Anwalt + StB | Strategievermerk |
| M-1 | Antragsentwurf § 3a Abs. 4 EStG (siehe Skill `stb-sanierungsgewinn-3a-iv-estg-antrag-und-bindungswirkung`) | StB | Antragsentwurf |
| M-0 | Insolvenz-/StaRUG-Antrag stellen; Sanierungsantrag § 3a EStG mit nächster Steuererklärung | Anwalt + StB | Antrag eingereicht |

## Trade-off-Matrix

| Konstellation | Frühwarnung sinnvoll? | Schwerpunkt |
|---|---|---|
| Verlustvortrag deckt potentiellen Sanierungsertrag | Ja, aber Sanity-Check vorrangig | Verbrauchsreihenfolge § 3c IV |
| Verlustvortrag deutlich kleiner als Ertrag | Ja, kritischer Pfad | Vier-Voraussetzungen-Doku |
| Gläubigerstruktur klein und kooperativ | Ja, aber leichter | Schriftliche Verzichtszusagen |
| Komplexe Gläubigerstruktur (Banken, Lieferanten, Anleihen) | Sehr dringend | Sanierungsabsicht je Gläubiger |
| Personengesellschaft / Mitunternehmer | Sehr dringend | Personenbezogene Komponenten |
| Internationale Komponente | Sehr dringend | Betriebsstätten-Zuordnung |

## Praxistipps der alten Hasen

- **Die "vier Voraussetzungen" werden im Streit vom FA Punkt für Punkt zerlegt.** Wer erst im Monat M-2 anfängt zu dokumentieren, verliert. Beginnen Sie spätestens in M-9 mit der schriftlichen Sammlung — Maßnahmenpläne, Konzeptentwürfe, Liquiditätsdaten.
- **Die Sanierungsabsicht der Gläubiger ist eine Innenseite.** Sie müssen sie im Außenverhältnis nachweisen. Lassen Sie sich von jedem verzichtenden Gläubiger schriftlich bestätigen, dass der Verzicht der Sanierung des Unternehmens dient.
- **Vermeiden Sie einen Forderungsverzicht "ins Blaue".** Wenn die Bedingungen des § 3a EStG nicht erfüllt werden können, entsteht ein voll steuerpflichtiger Gewinn, der die Liquidität sofort wieder belastet — und mit ihm Vorauszahlungen.
- **Der Verlustvortrag ist Ihr stiller Hebel.** Wenn er den Sanierungsertrag aufzehrt, brauchen Sie den Antrag nach § 3a Abs. 4 EStG gar nicht — Sie sparen sich den Streit mit dem FA über die vier Voraussetzungen.
- **Die Bindungswirkung des Antrags ist scharf.** Einmal gestellt und Sanierungserfolg festgestellt, ist die Rücknahme nicht mehr möglich. Strukturieren Sie vorher — nicht hinterher.

## Mustertexte / Berechnungsbeispiele

### Beispiel-Zeitachse (sequentielle Darstellung)

```
M-12 ► Mandantenbrief Warnung Sanierungsgewinn
M-11 ► Verlustvortrag-Check (EStG/KStG/GewStG)
M-10 ► Memo "unternehmensbezogen vs. personenbezogen"
M-9 ► Sanierungskonzept Entwurf
M-8 ► IDW-S6-Bericht Entwurf
M-7 ► Maßnahmenkatalog mit Quote
M-6 ► Gläubigeransprache schriftlich
M-5 ► Plan-Bilanz mit Verzichtswirkung
M-4 ► Optionsvergleich Verzicht vs. d/e-swap
M-3 ► Verbindliche Auskunft (optional)
M-2 ► Strategievermerk Vermeidung
M-1 ► Antragsentwurf 3a IV EStG
M-0 ► Antrag eingereicht
```

### Berechnungsbeispiel Wirkungsweise § 3c Abs. 4 EStG

```
Schritt 1 Vor Sanierung
 Verlustvortrag KSt zum 31.12. EUR 800.000
 Gewerbeverlust zum 31.12. EUR 600.000

Schritt 2 Forderungsverzicht 01.04.
 Verzichtsbetrag (Banken+Lieferanten) EUR 1.000.000
 ► entstehender Buchgewinn handelsrechtlich
 und steuerlich (vorläufig) gleich

Schritt 3 § 3c Abs. 4 EStG (Verbrauchsreihenfolge)
 KSt Sanierungsertrag EUR 1.000.000
 abzgl. Verlustvortrag EUR -800.000
 verbleibender Sanierungsertrag EUR 200.000
 steuerfrei nach § 3a Abs. 1 EStG EUR 200.000

Ergebnis: kein KSt-Cashflow durch Verzicht
 aber Verlustvortrag vollständig aufgezehrt
```

## Typische Fehler

- Mandant erfährt erst bei Plan-Einreichung vom Sanierungsgewinn — keine Dokumentation der vier Voraussetzungen vorhanden.
- Verlustvortrag nicht gegengerechnet; Antrag § 3a Abs. 4 EStG gestellt, obwohl unnötig.
- Gewerbesteuer-Parallelantrag § 7b GewStG vergessen.
- Sanierungsabsicht der Gläubiger nur mündlich vereinbart; FA verlangt Schriftform.
- Personenbezogene Sanierung mit unternehmensbezogenem Antrag verwechselt.

## Querverweise

- `stb-sanierungsgewinn-verlustvortrag-sanity-check`
- `stb-sanierungsgewinn-mandantenwarnung-rechtzeitig`
- `stb-sanierungsgewinn-vorbereitungs-checkliste`
- `stb-sanierungsgewinn-3a-iv-estg-antrag-und-bindungswirkung`
- `stb-sanierungsgewinn-vermeidungsstrategien-praxis`
- `anw-insolvenzreife-pruefung-17-19-inso` (vorgelagerte Insolvenzprüfung)

## Quellen Stand 06/2026

- § 3a EStG (Sanierungsertrag, Steuerbefreiung).
- § 3a Abs. 4 EStG (Antrag, Bindungswirkung).
- § 3c Abs. 4 EStG (Verlustreihenfolge).
- § 7b GewStG (Gewerbesteuer-Parallelregelung).
- § 10a Satz 1 GewStG (Gewerbeverlust).
- BMF-Schreiben vom 27.04.2017 (Sanierungserlass-Nachfolge) — vor Verwendung am aktuellen BMF-Stand verifizieren.
- Wachstumschancengesetz (BGBl. I 2024) — gesetzliche Verankerung; Stand prüfen.
- IDW S 6 (Sanierungskonzept), IDW S 11 (Insolvenzeröffnungsgründe).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren. Vor Ausgabe Quelle mit Gericht, Datum, Aktenzeichen, Fundstelle, Randnummer protokollieren.

## 8. `stb-sanierungsgewinn-personengesellschaft-und-mitunternehmer`

**Fokus:** Besonderheiten der Sanierungsertragsbehandlung bei Personengesellschaften und Mitunternehmern. Anteilige Zurechnung Sanierungsertrag; getrennter Antrag § 3a Absatz 4 EStG je Mitunternehmer; Sonderbetriebsvermögen.

# Sanierungsgewinn — Personengesellschaft und Mitunternehmer

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Sanierungsgewinn — Personengesellschaft und Mitunternehmer` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

Bei Personengesellschaften (GbR, OHG, KG, GmbH und Co. KG) ist der Sanierungsertrag nicht bei der Gesellschaft selbst, sondern anteilig bei den Mitunternehmern zu versteuern (Mitunternehmerschaft, § 15 Abs. 1 S. 1 Nr. 2 EStG). Jeder Mitunternehmer muss seinen Anteil am Sanierungsertrag in der eigenen Steuererklärung deklarieren und ggf. Antrag § 3a Abs. 4 EStG stellen. Sonderbetriebsvermögen wird separat behandelt.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Welche Rechtsform liegt vor — GbR, OHG, KG, GmbH und Co. KG?
2. Anzahl Mitunternehmer und Beteiligungsverhältnis?
3. Wird auf Verbindlichkeiten im Gesamthandsvermögen oder im Sonderbetriebsvermögen verzichtet?
4. Welche Verlustvorträge bestehen bei welchen Mitunternehmern (§ 10d EStG)?
5. Liegen Verluste nach § 15a EStG vor (beschränkte Verlustverrechnung Kommanditisten)?
6. Stille Reserven in der Gesellschaft?

## Rechtlicher Rahmen

- **§ 15 Abs. 1 S. 1 Nr. 2 EStG** — Mitunternehmer; Einkünfte einschließlich Sondervergütungen und Sonderbetriebsvermögen.
- **§ 15a EStG** — Verlustverrechnungsbeschränkung Kommanditist (negatives Kapitalkonto).
- **§ 16 EStG** — Veräußerung / Aufgabe Mitunternehmeranteil.
- **§ 3a Abs. 1, 4 EStG** — Sanierungsbefreiung; Antrag.
- **§ 3c Abs. 4 EStG** — Verlustreihenfolge.
- **§ 10d EStG** — Verlustabzug.
- **§ 7b GewStG** — Gewerbesteuer.
- **§ 10a S. 1 GewStG** — Gewerbeverlust (auf Gesellschafts-Ebene).
- **§ 180 Abs. 1 Nr. 2 AO** — gesonderte und einheitliche Feststellung.

## / Schritt für Schritt

### Verbindlichkeit im Gesamthandsvermögen

| Schritt | Inhalt |
|---|---|
| 1 | Sanierungsertrag entsteht auf Gesellschaftsebene |
| 2 | Sanierungsertrag wird in gesonderter und einheitlicher Feststellung § 180 AO auf Mitunternehmer verteilt |
| 3 | Jeder Mitunternehmer erhält anteiligen Sanierungsertrag (entsprechend Beteiligungsquote / Gewinnverteilungsschlüssel) |
| 4 | Jeder Mitunternehmer prüft individuell: § 10d EStG-Vortrag vorhanden? § 3a Abs. 4 EStG-Antrag erforderlich? |
| 5 | Gewerbeverlust und § 7b GewStG auf Gesellschaftsebene; gesonderte Feststellung |

### Verbindlichkeit im Sonderbetriebsvermögen

| Schritt | Inhalt |
|---|---|
| 1 | Gesellschafterdarlehen wird im Sonderbetriebsvermögen des betroffenen Mitunternehmers ausgewiesen |
| 2 | Verzicht trifft nur diesen Mitunternehmer |
| 3 | Sanierungsertrag wird in dessen Sonder-GuV ausgewiesen |
| 4 | Übrige Mitunternehmer nicht betroffen |
| 5 | Antrag § 3a Abs. 4 EStG nur dieser Mitunternehmer |

### § 15a EStG-Falle Kommanditist

| Schritt | Inhalt |
|---|---|
| 1 | Verluste aus KG-Beteiligung sind bei Kommanditisten verrechnungsbeschränkt (§ 15a EStG) |
| 2 | Nicht verrechenbare Verluste werden gesondert festgestellt |
| 3 | Sanierungsertrag erhöht das Kapitalkonto → Verlustverrechnung möglich |
| 4 | § 3a EStG-Antrag würde die Verrechnungsmasse mindern |
| 5 | Trade-off prüfen |

## Trade-off-Matrix

| Konstellation | Wirkung | Empfehlung |
|---|---|---|
| Verzicht Gesamthand, alle Mitunternehmer mit ESt-Verlustvortrag | Voll verrechenbar pro Person | Antrag § 3a IV ggf. teilweise entbehrlich |
| Verzicht Gesamthand, einige Mitunternehmer ohne Vortrag | Anteilige Steuerpflicht je Person | Individual-Antrag § 3a IV EStG |
| Verzicht Sonderbetriebsvermögen | Nur einer betroffen | Klar abgegrenzter Antrag |
| Kommanditist § 15a EStG-Verluste | Verrechnung mit Sanierungsertrag möglich | Bindungswirkung § 3a IV erst nach Sanity-Check |
| Mehrere Wirtschaftsjahre mit Verzichten | Komplexe Verteilung | Detail-Schema |

## Praxistipps der alten Hasen

- **Gesonderte und einheitliche Feststellung ist Pflicht.** Bei Personengesellschaften wird der Sanierungsertrag auf Gesellschaftsebene festgestellt und auf Mitunternehmer verteilt (§ 180 AO). Jeder Mitunternehmer erhält den anteiligen Ertrag in seiner ESt-Erklärung.
- **Antrag § 3a Abs. 4 EStG ist Sache des Mitunternehmers.** Der Antrag wird nicht von der Personengesellschaft, sondern jeweils vom Mitunternehmer mit dessen ESt-Erklärung gestellt. Bei mehreren Mitunternehmern: koordiniertes Vorgehen empfohlen, aber rechtlich unabhängig.
- **§ 15a EStG-Verluste sind ein Hebel.** Wenn Kommanditisten nicht ausgleichsfähige Verluste haben, können diese durch den Sanierungsertrag aktiviert werden — ohne Antrag § 3a EStG. Vorher rechnen, ob Antrag noch sinnvoll ist.
- **Sonderbetriebsvermögen sauber trennen.** Verzicht auf Gesellschafterdarlehen, das im Sonderbetriebsvermögen geführt war, ist nur dem Sondervermögens-Inhaber zuzurechnen — nicht auf alle Mitunternehmer zu verteilen.
- **§ 7b GewStG-Antrag liegt bei der Personengesellschaft.** Gewerbesteuer-Subjekt ist die Gesellschaft selbst (nicht die Mitunternehmer). Antrag wird mit GewSt-Erklärung der Gesellschaft gestellt.

## Mustertexte / Berechnungsbeispiele

### Berechnungsbeispiel KG mit 3 Kommanditisten

```
KG-Sanierungsertrag (Gesamthand) EUR 1.500.000
Gewinnverteilungsschlüssel: 50/30/20 %

Kommanditist A (50 %): EUR 750.000
 ESt-Verlustvortrag EUR 800.000
 Mindestbesteuerung: Sockel 1 Mio. > 750.000
 ► voll verrechenbar
 ► Antrag § 3a IV EStG entbehrlich
 ► Verlustvortrag verbraucht 750.000

Kommanditist B (30 %): EUR 450.000
 ESt-Verlustvortrag EUR 200.000
 Sanierungsertrag - Vortrag EUR 250.000
 ► Antrag § 3a IV EStG für 250.000 erforderlich
 ► ESt-Spitzensatz ohne Antrag: ~ 105.000

Kommanditist C (20 %): EUR 300.000
 Kein Verlustvortrag, aber § 15a EStG-Verluste EUR 400.000
 ► Sanierungsertrag aktiviert § 15a-Verluste
 ► nach § 15a-Verrechnung: 0 EUR steuerpflichtig
 ► Antrag § 3a IV EStG ggf. entbehrlich

Gewerbesteuer:
 Antrag § 7b GewStG durch KG mit GewSt-Erklärung
 Gewerbeverlust § 10a S. 1 GewStG vorher prüfen
```

### Berechnungsbeispiel Sonderbetriebsvermögen

```
KG, Gesellschafterdarlehen Kommanditist A
im Sonderbetriebsvermögen EUR 600.000

Gesellschafter A verzichtet:
► Sanierungsertrag NUR bei Mitunternehmer A
► Kommanditisten B und C nicht betroffen

A trägt allein:
 Sanierungsertrag EUR 600.000
 ESt-Verlustvortrag EUR 400.000
 Sanierungsertrag - Vortrag EUR 200.000
 ► Antrag § 3a IV EStG für 200.000

Übrige Mitunternehmer unverändert.
```

## Typische Fehler

- Sanierungsertrag auf Gesellschaft statt auf Mitunternehmer beantragt.
- Sonderbetriebsvermögen mit Gesamthand vermischt.
- § 15a EStG-Verluste nicht aktiviert; Antrag § 3a IV EStG entbehrlich gewesen.
- Antrag § 3a IV EStG für KG gestellt — Norm gilt aber für die Mitunternehmer-ESt.
- § 7b GewStG-Antrag durch Mitunternehmer statt durch Gesellschaft.
- Gewinnverteilungsschlüssel falsch angesetzt; Anteile fehlerhaft.

## Querverweise

- `stb-sanierungsgewinn-3a-estg-grundtatbestand`
- `stb-sanierungsgewinn-3a-estg-unternehmens-vs-person`
- `stb-sanierungsgewinn-koerperschaftsteuer-vs-einkommensteuer`
- `stb-sanierungsgewinn-3a-iv-estg-antrag-und-bindungswirkung`
- `stb-sanierungsgewinn-verlustvortrag-sanity-check`

## Quellen Stand 06/2026

- § 15 Abs. 1 S. 1 Nr. 2 EStG.
- § 15a EStG.
- § 16 EStG.
- § 3a Abs. 1, 4 EStG.
- § 3c Abs. 4 EStG.
- § 10d EStG.
- § 7b GewStG.
- § 10a S. 1 GewStG.
- § 180 Abs. 1 Nr. 2 AO.
- BMF-Schreiben vom 27.04.2017 — Stand prüfen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; Quelle vor Ausgabe protokollieren.

## 9. `stb-sanierungsgewinn-rangruecktritt-und-5-abs-2a-estg`

**Fokus:** Rangrücktritt im Kontext § 5 Absatz 2a EStG: Passivierungsverbot bei Tilgung ausschließlich aus zukünftigen Gewinnen führt zum Ertrag in voller Höhe und damit zum Sanierungsgewinn. BFH-Linie streng - keine Az aus Modellwissen.

# Rangrücktritt und § 5 Abs. 2a EStG

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Rangrücktritt und § 5 Abs. 2a EStG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Worum geht es

§ 5 Abs. 2a EStG enthält ein Passivierungsverbot für Verbindlichkeiten, die ausschließlich aus zukünftigen Gewinnen, Einnahmen oder Vermögenswerten zu tilgen sind. Klassisch trifft das den Rangrücktritt mit Tilgung "aus freiem Vermögen" — wenn der Rangrücktritt zu eng formuliert ist, entsteht ein Buchgewinn in Höhe der Verbindlichkeit. Dieser Buchgewinn ist im Sanierungskontext häufig der Sanierungsertrag, den § 3a EStG retten muss.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. Liegt eine Rangrücktrittserklärung vor — schriftlich, vor oder im Sanierungsverfahren?
2. Welche Tilgungsabrede ist im Rangrücktritt enthalten — "aus zukünftigen Gewinnen" oder "aus freiem Vermögen"?
3. Ist § 5 Abs. 2a EStG einschlägig (Passivierungsverbot)?
4. Wenn ja: Sanierungsertrag § 3a EStG vorbereitet?
5. Insolvenz- oder Überschuldungssituation der Schuldnerin?

## Rechtlicher Rahmen

- **§ 5 Abs. 2a EStG** — Passivierungsverbot bei Tilgung aus zukünftigen Gewinnen.
- **§ 5 Abs. 1 EStG** — Maßgeblichkeit.
- **§ 39 Abs. 2 InsO** — qualifizierter Rangrücktritt; Anforderungen.
- **§ 19 InsO** — Überschuldung; Behandlung Rangrücktritt im Überschuldungsstatus.
- **§ 3a EStG** — Sanierungsertrag.
- **§ 8 Abs. 3 KStG** — verdeckte Einlage.

## / Schritt für Schritt

| Schritt | Inhalt |
|---|---|
| 1 | Rangrücktrittstext einsehen und auf Tilgungsabrede prüfen |
| 2 | Klausel "aus zukünftigen Gewinnen" identifizieren — § 5 Abs. 2a EStG-Trigger |
| 3 | Wenn ja: Verbindlichkeit ist in Steuerbilanz auszubuchen ► Ertrag entsteht |
| 4 | Wirtschaftsjahr der Auflösung bestimmen — Zeitpunkt der Rangrücktrittsvereinbarung |
| 5 | Sanierungsertrag § 3a EStG-Antrag vorbereiten — falls vier Voraussetzungen erfüllt |
| 6 | Alternativ: Rangrücktrittsklausel anpassen (Tilgung aus freiem Vermögen / aus Gewinnen UND Liquidationserlös) — Passivierungsverbot vermeiden |
| 7 | Mit Gläubiger neu verhandeln und Vertrag ergänzen |

## Trade-off-Matrix

| Klauseltext | Passivierungsverbot § 5 Abs. 2a EStG? | Steuerliche Wirkung |
|---|---|---|
| "Tilgung nur aus zukünftigen Gewinnen" | Ja | Verbindlichkeit ausbuchen ► Ertrag |
| "Tilgung aus Gewinnen, Einnahmen, freiem Vermögen" | Nein (BFH-Linie streng — Stand prüfen) | Verbindlichkeit bleibt |
| "Qualifizierter Rangrücktritt § 39 Abs. 2 InsO" | Hängt vom Wortlaut ab | Einzelfallprüfung |
| "Insolvenzrechtlicher Rangrücktritt nur" | Üblicherweise nein | Bei sauberer Formulierung Verbindlichkeit bleibt |
| Rangrücktritt + Besserungsklausel | Kommt auf Wortlaut an | Mehrstufige Würdigung |

## Praxistipps der alten Hasen

- **Die Klauselfalle ist alltäglich.** Viele Rangrücktrittstexte sind handelsrechtlich-insolvenzrechtlich gedacht ("zur Vermeidung der Überschuldung") und enthalten zugleich eine zu enge Tilgungsabrede, die § 5 Abs. 2a EStG triggert.
- **Saubere Klausel: drei Tilgungsquellen.** Tilgung "aus künftigen Gewinnen, Einnahmen ODER aus dem die sonstigen Verbindlichkeiten übersteigenden freien Vermögen". Diese Formulierung wird in der Beraterpraxis als vergleichsweise sicher gehandelt — vor Verwendung aktuellen BFH-Stand prüfen.
- **Liquidationsklausel ist riskant.** Die Klausel "Tilgung aus Liquidationsüberschuss" allein reicht nach BFH-Linie nicht — sie macht die Schuld trotzdem zu einer aus zukünftigen Vermögenswerten zahlbaren. Stand prüfen — Aktenzeichen nicht aus Modellwissen.
- **Nachholbar nur bedingt.** Eine fehlerhafte Klausel kann durch Vertragsanpassung geheilt werden — aber die bilanzielle Auflösung im Streitjahr kann bleiben. Die Heilung wirkt regelmäßig erst pro futuro.
- **Bei drohender Überschuldung doppelt prüfen.** § 19 InsO verlangt für die Herausnahme aus Passiva einen Rangrücktritt mit insolvenzrechtlicher Wirkung. Steuerrechtlich gilt § 5 Abs. 2a EStG separat. Ein insolvenzrechtlich sicherer Rangrücktritt kann steuerrechtlich zur Auflösung führen — und umgekehrt.

## Mustertexte / Berechnungsbeispiele

### Musterklausel — sicherer Rangrücktritt

```
Rangrücktrittsvereinbarung

Der Gläubiger [Name] erklärt hiermit, dass seine Forderung
gegen die Schuldnerin [Firma] in Höhe von EUR [Betrag]
aus dem Darlehensvertrag vom [Datum] im Rang hinter alle
gegenwärtigen und zukünftigen Forderungen sämtlicher
anderer Gläubiger zurücktritt (qualifizierter Rangrücktritt
i.S.d. § 39 Abs. 2 InsO).

Die Forderung ist zu tilgen, sobald und soweit eine
Tilgung möglich ist aus:
 (i) künftigen Gewinnen oder Einnahmen der Schuldnerin,
 (ii) einem die sonstigen Verbindlichkeiten der Schuldnerin
 übersteigenden freien Vermögen, oder
 (iii) einem etwaigen Liquidationsüberschuss.

Diese Erklärung gilt unwiderruflich bis zur nachhaltigen
Beseitigung der Krise der Schuldnerin.
```

### Musterklausel — RISKANTE Formulierung (zu vermeiden)

```
[ZU VERMEIDEN]

Die Forderung ist nur aus künftigen Gewinnen zu tilgen.

► Triggert § 5 Abs. 2a EStG
► Verbindlichkeit muss steuerlich ausgebucht werden
► Sanierungsertrag entsteht in Höhe der Verbindlichkeit
```

### Berechnungsbeispiel mit § 3a EStG-Schutz

```
Verbindlichkeit Gesellschafter EUR 600.000
Rangrücktritt mit Klausel "nur aus zukünftigen Gewinnen"
► § 5 Abs. 2a EStG greift
► Verbindlichkeit wird ausgebucht ► Ertrag EUR 600.000

Wenn vier Voraussetzungen § 3a EStG erfüllt:
► Antrag § 3a Abs. 4 EStG stellen
► Sanierungsertrag steuerfrei (mit Verlustverrechnung)

Wenn vier Voraussetzungen NICHT erfüllt:
► EUR 600.000 voll steuerpflichtig
► KSt ~ 95.000, GewSt ~ 86.000 ► Liquiditätsbedarf 181.000

► Vorher Klausel ändern wäre besser gewesen.
```

### Memo-Baustein "Rangrücktritts-Klausel-Audit"

```
Memo: Audit Rangrücktrittsklausel — § 5 Abs. 2a EStG-Risiko

I. Sachverhalt
Die Mandantin hat im Wj X-Y einen Rangrücktritt
durch den Gesellschafter [Name] über EUR [Betrag]
vereinbart. Der Wortlaut ist:
"[Originalzitat aus dem Rangrücktrittsvertrag]"

II. Prüfung § 5 Abs. 2a EStG
Tilgungsabrede umfasst:
[ ] freies Vermögen (sicher)
[ ] zukünftige Gewinne (kritisch wenn allein)
[ ] zukünftige Einnahmen (kritisch wenn allein)
[ ] Liquidationsüberschuss (BFH-Linie streng — prüfen)

III. Ergebnis
[Wenn alle Quellen erfasst, insb. freies Vermögen:
 § 5 Abs. 2a EStG-Risiko gering — Verbindlichkeit bleibt]
[Wenn nur Gewinne/Einnahmen:
 § 5 Abs. 2a EStG-Risiko hoch — Auflösung droht]

IV. Empfehlung
[Klausel-Anpassung durch Nachtragsvereinbarung]
[Versand mit Empfangsbestätigung]
[Stichtag und Wirksamwerden dokumentieren]
```

## Typische Fehler

- Rangrücktrittsklausel "nur aus zukünftigen Gewinnen" gewählt; § 5 Abs. 2a EStG-Auflösung übersehen.
- Verbindlichkeit handelsrechtlich passiviert, steuerlich nicht ausgebucht — Mehr-Weniger-Rechnung fehlt.
- Anpassung der Klausel zu spät; Auflösung im falschen Wirtschaftsjahr nicht mehr heilbar.
- Insolvenzrechtliche und steuerrechtliche Wirkung verwechselt.
- BFH-Linie zur Liquidationsklausel überschätzt; Klausel zu schmal.

## Querverweise

- `stb-sanierungsgewinn-3a-estg-grundtatbestand`
- `stb-sanierungsgewinn-3a-iv-estg-antrag-und-bindungswirkung`
- `stb-sanierungsgewinn-forderungsverzicht-bilanzielle-darstellung`
- `stb-sanierungsgewinn-liquidation-nachrang-fg-koeln`
- `anw-insolvenzreife-pruefung-17-19-inso`

## Quellen Stand 06/2026

- § 5 Abs. 1, 2a EStG.
- § 39 Abs. 2 InsO.
- § 19 InsO.
- § 3a Abs. 1, 4 EStG.
- § 8 Abs. 3 KStG.
- BMF-Schreiben vom 27.04.2017 — Stand prüfen.
- Rechtsprechung des BFH zu § 5 Abs. 2a EStG (ständige Rspr.): keine Entscheidung aus Modellwissen zitieren; Quelle vor Ausgabe protokollieren.
