---
name: grosskanzlei-ma-tabellenreview
description: "Freistehender Tabellenreview für Corporate M&A-Dokumente Datenpunkte und Perspektiven: Anwendungsfall Tabellen Formeln Excel-Modelle oder Dokumentenmatrizen in Transaktionen muessen auf Formelbrueche widersprüchliche Zahlen und Inkonsistenzen geprüft werden. SPA Financial Statements, DD-Modelle...."
---

# Freistehender Tabellenreview

## Fachlicher Anker

- **Normen:** §§ 3, §§ 76, §§ 105.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Freistehender Tabellenreview
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, UmwG, WpHG/MAR, GWB/FKVO, AWG/AWV, LMA-Finanzierung, Beirats-/Organregeln, SPA/SHA/Term-Sheet-Praxis.
- **Entscheidende Weiche:** Dealphase, Mandantenrolle, CP/Consent, Haftung, Disclosure, Signing/Closing, Notar/Register, Beirat/Organ und Verhandlungstaktik trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Kernsachverhalt

Tabellen, Datenräume und Dokumentenmatrizen in M&A-Transaktionen sind fehleranfällig: Formelbrüche in Excel-Modellen, widersprüchliche Umsatzzahlen in Finance vs. Commercial Workstreams, fehlende Anlagen zu Verträgen, inkonsistente Währungsangaben und veraltete Stichtage. Der Tabellenreview bringt Struktur in die Massendatenprüfung, indem er einen dreidimensionalen Review-Würfel aufbaut: Zeilen (Dokumente oder Datenpunkte), Spalten (Prüfungsfragen und Kriterien), Blätter (Workstream-Perspektiven). Er schützt vor teuren Post-Closing-Überraschungen und ist Grundlage für Q&A-Listen und Disclosure Schedules.

## Kaltstart-Rückfragen

1. Was sind die Eingabedaten — Excel-Dateien, CSV, Markdown-Tabellen, Datenraumlisten, Vertragslisten?
2. Welcher Dealtyp und welcher DD-Scope gelten — Buy-Side DD, Sell-Side DD, Vendor DD, Fairness Opinion?
3. Welche Workstreams sind bereits aktiv und sollen im Review-Würfel berücksichtigt werden?
4. Welche Materiality-Schwelle gilt für den Deal (z.B. EUR 100.000 einzeln, EUR 500.000 kumuliert)?
5. Sind Cross-Check-Anforderungen definiert — Umsatz in Finance vs. Kundenvertragsliste in Commercial?
6. Welche bekannten Problempunkte sollen gezielt geprüft werden (z.B. Change-of-Control-Klauseln, auslaufende Lizenzen)?
7. Wer erhält den Review-Output — intern, Mandant, Gegenseite, Gericht?
8. Welches Ausgabeformat ist bevorzugt — Markdown, Excel-Export, Word-Bericht?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Relevante Normen für den Tabellenreview

| Norm / Standard | Regelungsinhalt |
|---|---|
| §§ 242 ff. HGB | Grundsätze ordnungsmäßiger Buchführung (GoB); Vollständigkeitsgebot, Wahrheitsgebot, Klarheitsgebot |
| IDW S 1 | Grundsätze zur Durchführung von Unternehmensbewertungen; Plausibilisierungsanforderungen an Finanzmodelle |
| § 264 HGB | Jahresabschluss muss ein den tatsächlichen Verhältnissen entsprechendes Bild der Vermögens-, Finanz- und Ertragslage vermitteln |
| § 256a HGB | Wechselkursumrechnung bei Fremdwährungsposten; Stichtagskurs |
| SPA-Kaufpreisklauseln | Completion Accounts, Locked Box, Leakage, Net Debt-Definition; Zahlengrundlage für Kaufpreisanpassung |
| §§ 249, 252 HGB | Rückstellungspflicht und Stetigkeitsgrundsatz; Bilanzierungswahlrechte |

### Leitentscheidungen

| Gericht | Az. | Datum | Leitsatz (kurz) |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema / Review-Würfel

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Status |
|---|---|---|---|
| 1 | Eingaben erfassen und inventarisieren | Dateiname, Typ, Stichtag, Version, Ersteller, Datenraumort | Inventar erstellt |
| 2 | Zeilendefinition (Dokument-Inventory) | Dokumente, Vertragscluster, Gesellschaften, Assets, Kunden, Lieferanten, Lizenzen | Zeilen definiert |
| 3 | Spaltendefinition (Prüfungsfragen) | Datenpunkte, Klauseln, Zahlenfelder, Risiken, Materiality, Belegstellen, Owner, SPA-Relevanz | Spalten definiert |
| 4 | Blattdefinition (Workstreams) | Legal, Tax, Finance, Commercial, ESG/Compliance, Employment, IP/IT, Regulatory, PMI | Blätter definiert |
| 5 | Zellenstatus vergeben | `leer`, `belegt`, `widersprüchlich`, `prüfen`, `nicht anwendbar` | Grid-Status |
| 6 | Formeln und Rechenlogik prüfen | Summen nachrechnen; SVERWEIS/XVERWEIS auf Quellen prüfen; Prozentsätze mit Nenner und Stichtag verifizieren | Formelprüfung |
| 7 | Währung und Stichtag prüfen | Konsistente Währung (EUR, USD); einheitlicher Stichtag (Abschluss-Stichtag, Signing-Stichtag); § 256a HGB | Stichtag klar |
| 8 | Kreuzblatt-Widersprüche | Umsatz Finance vs. Commercial; Headcount HR vs. Lohnliste; IP-Portfolio Legal vs. Patentregister | Widersprüche markiert |
| 9 | Material-Schwellen-Filter | Alle Posten über Materiality-Schwelle (EUR [X]) hervorheben; Cluster-Analyse für kumulative Werte | Material Items Liste |
| 10 | Change-of-Control-Screening | Alle Verträge mit CoC-Klausel identifizieren; Zustimmungspflicht, Kündigungsrecht, Kaufrecht | CoC-Liste |
| 11 | Laufzeit und Kündigungsfristen | Auslaufende Verträge (< 12 Monate), ordentliche / außerordentliche Kündigungsrechte | Laufzeit-Matrix |
| 12 | Cap Table und Anteilsstruktur | Vollständigkeit, Runde-Übereinstimmung, Verwässerungsschutz, Optionen und Wandelrechte | Cap Table geprüft |
| 13 | Net Debt- und Working Capital-Brücke | Net Debt-Definition laut SPA; Cash-like Items, Debt-like Items, Normalisierung Working Capital | Brückenrechnung |
| 14 | Fehlerliste und Q&A ableiten | Dubletten, Lücken, widersprüchliche Zahlen, fehlende Anlagen, unplausible Formeln → Q&A-Liste | Fehlerliste fertig |
| 15 | Output und Übergabe | Review Grid als Markdown/CSV; Findings-Tabelle; Übergabe an DD-Reporting, Disclosure Schedules | Output bereit |

## Beweislast / Qualitätssicherung

| Anforderung | Norm / Standard | Konsequenz bei Fehler |
|---|---|---|
| Vollständigkeit der Datengrundlage | IDW S 1; SPA (Rep & Warranties) | Garantieverletzung; Kaufpreisminderung |
| Korrekte Formellogik | GoB (§§ 242 ff. HGB) | Haftung für fehlerhafte Entscheidungen |
| Konsistente Stichtage | § 256a HGB; SPA-Closing Accounts | Kaufpreisanpassungsanspruch |
| Vollständige Vertragsanlage | Disclosure Obligation (SPA) | Garantieverletzung, Schadensersatz |

## Fristen und zeitliche Aspekte

| Zeitpunkt | Maßnahme | Hinweis |
|---|---|---|
| Nach Datenraum-Öffnung | Erster Tabellenreview innerhalb 3–5 Werktage | Q&A-Frist der Gegenseite nutzen |
| Nach Q&A-Antworten | Aktualisierter Review mit geschlossenen Lücken | Neue Widersprüche durch Antworten möglich |
| Vor Signing | Finaler Review: alle offenen TODOs geschlossen | SPA-Anlage: Disclosure Schedule |
| Nach Completion Accounts (Closing) | Zahlen-Abgleich mit vorläufigen und finalen Accounts | Kaufpreisanpassungsfrist lt. SPA (typisch 45–90 Tage) |

## Typische Fehlerarten und Gegenmaßnahmen

| Fehlertyp | Häufigkeit | Gegenmaßnahme |
|---|---|---|
| Formelbruch in Excel-Finanzmodell | Hoch | Jeden Zellbezug prüfen; Summen manuell nachrechnen |
| Inkonsistente Umsatzdaten | Mittel | Cross-Check Finance vs. Commercial; Top-10-Kunden-Umsatz reconcilieren |
| Fehlende Vertragsanlagen | Hoch | Indexabgleich; Q&A-Frage stellen; Materiality-Filter anwenden |
| Veralteter Jahresabschluss | Mittel | Stichtag prüfen; ggf. Interim Financials anfordern |
| Währungsfehler | Niedrig | Einheitliche Währung und Wechselkurs-Stichtag definieren |
| Change-of-Control übersehen | Mittel | Alle Verträge screenen; CoC-Schlüsselbegriffe als Suchfiler |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu prüfen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Tabellen aus M-and-A-Unterlagen reviewen | Tabellenreview nach Schema; Prüfbericht unten |
| Variante A — Nur bestimmte Tabellenspalten relevant | Selektive Prüfung der relevanten Spalten |
| Variante B — Tabellen aus Auslandsrecht andere Formate | Formatkonvertierung zuerst; dann Prüfung nach Schema |
| Variante C — Eilbedarf Tabelle muss sofort freigegeben werden | Kurzcheck ohne Vollpruefung; Vorbehalt in Freigabe vermerken |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 — Review Grid (Standardstruktur)

```
TABELLENREVIEW — Projekt [Deal-Code] — Workstream [Finance]
Stand: [Datum]
Erstellt von: [Name]

| Dok.-Nr. | Dokument | Stichtag | Umsatz | EBITDA | Net Debt | Status | Kommentar |
|----------|-----------------|------------|----------|----------|----------|-------------|-----------|
| DR-001 | JA 2023 (HGB) | 31.12.2023 | EUR 50M | EUR 7M | EUR 12M | belegt | OK |
| DR-002 | Forecast 2024 | 31.12.2024 | EUR 55M | EUR 8M | n.v. | prüfen | Net Debt fehlt — TODO Finance bis [Datum] |
| DR-003 | Interim Q1 2024 | 31.03.2024 | EUR 13M | EUR 2M | EUR 11M | widersprüchl.| Umsatz Q1 2024 vs. Forecast-Ableitung: EUR 0,5M Differenz — Q&A stellen |
| DR-004 | Tax Return 2022 | 31.12.2022 | nicht v. | nicht v. | nicht v. | leer | Nicht in DR hochgeladen — Q&A: Steuerbescheid 2022 anfordern |
```

### Baustein 2 — Q&A-Fragen aus Tabellenreview

```
Q&A-LISTE — Projekt [Deal-Code] — Workstream Finance
Stand: [Datum]
Erstellt von: [Name]

Q1 (MATERIAL): Net Debt-Berechnung
Im Finanzmodell (DR-002) wird Net Debt zum 31.12.2024 nicht ausgewiesen. Bitte
definieren Sie Net Debt gemäß SPA-Entwurf Ziffer [X] und stellen Sie einen
Net Debt-Überleitungsplan zur Verfügung, der Cash-like Items und Debt-like Items
getrennt ausweist. Frist: [Datum].

Q2 (WIDERSPRUCH): Umsatz Q1 2024
Im Interim Report Q1 2024 (DR-003) wird ein Umsatz von EUR 13M ausgewiesen.
Die Ableitung aus dem Forecast 2024 (DR-002) ergibt für Q1 2024 einen Planumsatz
von EUR 13,5M. Die Differenz von EUR 0,5M (3,8 %) ist zu erläutern.

Q3 (LÜCKE): Steuerbescheid 2022
Der Steuerbescheid 2022 (Körperschaftsteuer, Gewerbesteuer) wurde nicht hochgeladen.
Bitte unverzüglich nachreichen.
```

### Baustein 3 — Kreuzblatt-Widerspruchs-Memo

```
KREUZBLATT-MEMO — Projekt [Deal-Code]
Stand: [Datum]
Von: Tabellenreview-Team

WIDERSPRUCH: Umsatz Finance vs. Commercial

Finance (DR-003, JA 2023): Gesamtumsatz EUR 50M
Commercial (DR-015, Kundenliste): Top-10-Kunden EUR 38M; Restanteile n.v.

Mögliche Erklärungen:
(a) Internes Umsatz-Splittig zwischen Segmenten nicht in Kundenliste abgebildet.
(b) Umsatz enthält Intercompany-Erlöse, die in Kundenliste nicht erscheinen.
(c) Datenfehler in einer der beiden Quellen.

TODO [Finance-Owner]: Segmentumsatz-Überleitung bis [Datum].
TODO [Commercial-Owner]: Kundenliste um Intercompany-Position ergänzen.
Eskalation: Bei Nichtbehebung bis [Datum] → Q&A an Verkäufer.
```

--- vor Versand klären ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klärenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Streitwert und Kosten

| Schadensfall | Ansatz | Hinweis |
|---|---|---|
| Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
| Garantieverletzung wegen fehlender Unterlagen | Differenz tatsächlicher vs. garantierter Wert | SPA Rep & Warranties |
| Schadensersatz wegen CoC-Verletzung | Vertragsstrafrisiko + Neuverhandlungskosten | Wichtigste CoC-Verträge priorisieren |

## Strategische Empfehlung

| Akteur | Empfehlung |
|---|---|
| DD-Team | Review Grid ab Tag 1 anlegen; Materiality-Schwelle vor Start festlegen; Kreuzblatt-Widersprüche sofort Q&A zuführen |
| Partner | Final Review vor Signing persönlich freigeben; alle TODOs müssen geschlossen oder als Disclosure offengelegt sein |
| Mandant | Vollständige Disclosure Schedule als Verhandlungsmasse; Fehler im Datenraum können Verhandlungsposition stärken |

## Anschluss-Skills

- `grosskanzlei-ma-aktenanlage` — Review-Outputs in Deal-Akte einpflegen
- `grosskanzlei-ma-liquiditaetsvorschau` — Finanzdaten aus Review mit Liquidität verknüpfen
- `grosskanzlei-ma-insolvenzreife` — Insolvenzreife-Indikatoren aus Review eskalieren
- `corporate-kanzlei-fair-disclosure-knowledge` — Disclosure-Klauseln mit Review-Findings verzahnen

## Quellen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- §§ 242, 249, 252, 256a, 264 HGB; IDW S 1
