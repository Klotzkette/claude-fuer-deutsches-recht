---
name: dba-all-country-memo-generator
description: "Generiert ein länderspezifisches DBA-Memo für jeden deutschen DBA-Staat aus Matrix, DBA-Text und Sachverhalt. Für Länder ohne eigenen Detail-Skill: Artikelroute, Einkunftsart, Methode, Quellensteuer, Beweise, Edge-Cases und offene Live-Prüfungen."
---

# DBA-All-Country-Memo-Generator

## Fachlicher Kern — Steuerrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DBA-All-Country-Memo-Generator` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** AO, EStG, KStG, GewStG, UStG, GrEStG, UmwStG, AStG, FZulG, MinStG; BMF-Schreiben nur mit Datum, Titel und offizieller BMF-URL verwenden.
- **Verifizierte Anker:** BMF-Schreiben vom 15.10.2025 zur obligatorischen E-Rechnung und UStAE-Anpassung; BMF-Seite Forschungszulage mit Hinweis zu Antrags-/Festsetzungslogik und BMF-Schreiben vom 07.02.2023; BMF/BZSt-Datensatzbeschreibung vom 05.08.2025 für Mindeststeuer-Berichte; BMF-Schreiben vom 25.05.2023 zu § 6a GrEStG; BMF-Schreiben vom 02.01.2025/01.08.2025 zum Umwandlungssteuer-Anwendungserlass live prüfen.
- **Arbeitsmodus:** Erst Steuerart, Zeitraum, Verwaltungsstand, Frist/Festsetzung, Zuständigkeit, Form/Portal und Beleglage klären; dann BMF-Verwaltungslinie von BFH-Rechtsprechung und Gesetz trennen.
- **Outputpflicht:** Steuerartenmatrix, BMF-Radar, Einspruchsbaustein, ELSTER-/Portal-To-do, Risikoampel, DBA-/GrESt-/USt-Tabelle oder Mandantenmemo.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Aufgabe

Dieser Skill erzeugt aus jedem realistischen DBA-Sachverhalt ein verwendbares Memo, auch wenn das Land noch keinen Einzel-Skill hat.

## Pflichtaufbau

1. **Sachverhalt:** Beteiligte, Staaten, Zeitraum, Beträge, Zahlungsflüsse.
2. **DBA-Status:** Matrix und live geprüfter DBA-Text.
3. **Ansässigkeit:** nationales Recht, Art. 4, Tie-Breaker.
4. **Einkunftsart:** Artikel 6 bis 21 oder Alt-DBA-Sonderartikel.
5. **Verteilung:** Besteuerungsrecht, Quellensteuerhöchstsatz, Verfahren.
6. **Methode Deutschland:** Freistellung/Anrechnung/Progressionsvorbehalt/Switch-over.
7. **Anti-Missbrauch:** § 50d EStG, Beneficial Ownership, PPT/LOB, Substanz.
8. **Belege:** konkret.
9. **Ergebnis:** Kurzantwort plus offene Prüfmarker.

## Realistische Varianten

Baue bei Bedarf Varianten:

- Arbeitnehmer mit 47 Home-Office-Tagen und Bonus für Vorjahr.
- GmbH zahlt Softwarelizenz an ausländische Schwester.
- Deutsche KG mit ausländischer Betriebsstätte und lokalen Verlusten.
- Verkauf einer Immobilien-Holding.
- Pensionär mit gesetzlicher und betrieblicher Rente.
- US-LLC mit deutschen Gesellschaftern.
- Grenzgänger mit Dienstreisen in Drittstaaten.

## Quellenregel

Wenn der DBA-Text nicht vorliegt, keine abschließenden Sätze behaupten. Ausgabe dann ausdrücklich als "Arbeitsmemo mit Live-Prüfmarkern" kennzeichnen.

## Praktiker-Tipps "Schnell zum Bescheid"

- **DBA-Text vor Memo-Endfassung beschaffen**: ueber bundesfinanzministerium.de (Bereich Internationales Steuerrecht / Liste der DBA) — jede DBA-Seite enthaelt PDF-Link zum Gesetzes-Text inklusive Protokolle. Ohne Originaltext kein finalisiertes Memo.
- **MLI-Status pro Vertragsstaat pruefen**: OECD-MLI-Matching-Database (oecd.org) zeigt, ob beide Staaten kongruent notifiziert/reserviert haben. Wirksamkeitsdatum pro Norm separat.
- **BZSt-Formularkatalog**: für das Verfahren ueber bzst.de / BOP — Antragsformulare nach Einkunftsart strukturiert (vom Anwender mit aktuellem BZSt-Formularverzeichnis abzugleichen, KEINE erfundenen Formularnummern).
- **Ansaessigkeitsbescheinigung des betroffenen Heimatstaats** im Memo als Pflicht-Anlage benennen.
- **Q1-Antragsfenster** beim BZSt nutzen (Januar bis Maerz) — kuerzere Bearbeitungszeiten.
- **Apostille oder Konsularbeglaubigung** bei Drittstaaten (USA, VAE, Singapur, Australien) — Vorlaufzeit 6-10 Wochen einplanen.

## Trade-off-Tabelle (generisch)

| Trade-off | Pfad A | Pfad B | Empfehlung |
|---|---|---|---|
| Freistellung vs. Anrechnung | Freistellung mit Progressionsvorbehalt | Anrechnung § 34c EStG | bei aktiven Einkuenften Freistellung; bei passiven Anrechnung |
| Freistellungsbescheinigung vorab vs. Erstattung nachher | vor Zahlung — schnellerer Cashflow | nach Einbehalt — Vier-Jahres-Frist | bei regelmäßigen Zahlungen Pfad A; bei einmaligen Pfad B |
| MAP vs. EU-Streitbeilegung | bilateral, flexibler | EU-DBA-SBG mit Schiedszwang | bei EU-Sachverhalten beide parallel |
| EU-RL (MTRL/ZinsLizenzRL) vs. DBA | EU-RL 0 Prozent bei Verbundenheit | DBA-Hoechstsatz | EU-RL vorrangig, wenn Voraussetzungen erfuellt |
| Substanz aufbauen vs. Direktbezug | Holding mit Substanz aufbauen | direkter Bezug | § 50d Abs. 3 EStG bedenken; Substanz nur bei wirtschaftlicher Notwendigkeit |

## Was Reviewer/Pruefer triggert (generisch)

- **DBA-Fundstelle nicht zitiert** oder falsche BGBl-Stelle.
- **MLI-Status nicht erwaehnt** — auch bei US-DBA (USA haben MLI nicht ratifiziert) gehoert das ins Memo.
- **Ansaessigkeitsbescheinigung fehlt** als Anlage.
- **Substanztest § 50d Abs. 3 EStG nicht durchgeprueft** bei Holding-Konstellationen.
- **Subject-to-Tax (§ 50d Abs. 9 EStG) ignoriert** bei Niedrigsteuer-Wegzug.
- **Aktivitaetsklausel uebersehen** bei Holding-Einkuenften.
- **Personengesellschafts-Qualifikationskonflikt** nicht behandelt (BMF 26.09.2014).
- **Zeitlicher Anwendungsbereich** falsch — DBA-Fassung passt nicht zum Veranlagungszeitraum.

## Mustertabelle DBA-Memo (jedes Land)

| Pruefphase | Norm / Fundstelle | Befund Mandant | Ergebnis | Verifikationsquelle |
|---|---|---|---|---|
| Anwendungsbereich | Art. 1, 2 DBA-[Land] (BGBl. II [Jahr] S. [...]) | [Mandant erfasst?] | [erfasst / nicht erfasst] | bundesfinanzministerium.de |
| Ansaessigkeit | Art. 4 DBA + §§ 8, 9 AO | Tie-Breaker | [Wohnsitzstaat] | Ansaessigkeitsbescheinigung |
| Einkunftsart | Art. [6-21] DBA | Qualifikation [...] | [Art. x] | OECD-Kommentar |
| Verteilung | Art. [x] DBA | [Hoechstsatz / Belegenheit / Auftrittsstaat / ...] | [Quellenstaat darf ...] | DBA-Text |
| Methode | Art. 23A/B DBA + § 34c EStG | [Freistellung / Anrechnung] | [Methode] | DBA-Methodenartikel |
| Treaty Override | § 50d Abs. 3/8/9 EStG | [Substanz / Subject-to-Tax] | [greift / greift nicht] | BMF-Schreiben |
| Verfahren | § 50a, § 50c EStG | [Antragsweg] | [BZSt / FA Heimatstaat] | BOP-Portal |

## Beispiel-Varianten und Live-Marker

- **Arbeitnehmer 47 Home-Office-Tage + Bonus Vorjahr**: pruefe Konsultationsvereinbarung Home-Office; pruefe 183-Tage-Regel mit Aufenthaltskalender; Bonus aufteilen nach Vesting-Zeitraum.
- **GmbH-Softwarelizenz an auslaendische Schwester**: pruefe § 50a EStG-Einbehalt; Freistellungsbescheinigung BZSt; § 4j EStG-Lizenzschranke.
- **Deutsche KG mit auslaendischer BS und Verlusten**: pruefe Freistellung-Aktivitaetsklausel; § 2a EStG-Verlustberuecksichtigung.
- **Verkauf Immobilien-Holding**: pruefe Art. 13 DBA (grundstuecksreiche Gesellschaft); Belegenheitsstaat.
- **Pensionaer mit DRV + Betriebsrente Wegzug Portugal**: pruefe Art. 18 DBA-PT; NHR; § 50d Abs. 9 EStG.
- **US-LLC mit DE-Gesellschaftern**: pruefe Qualifikationskonflikt (LLC transparent vs. intransparent); BMF 26.09.2014; Subject-to-Tax.
- **Grenzgaenger mit Dienstreisen Drittstaaten**: pruefe Grenzgaenger-Status (CH/FR/AT); 183-Tage-Regel im Drittstaat.

## Konkrete Subsumtionsschema-Vorlage

Bei jeder Variante folgendes Schema durcharbeiten:

| Phase | Sachverhalt | DBA-Artikel + nat. Recht | Subsumtion | Ergebnis | Live-Markierung |
|---|---|---|---|---|---|
| Ansaessigkeit | [...] | Art. 4 + §§ 8, 9 AO | Tie-Breaker | [Wohnsitzstaat] | Ansaessigkeitsbescheinigung |
| Einkunftsart | [...] | Art. [6-21] | [Qualifikation] | [Art. x DBA] | OECD-Kommentar |
| Verteilung | [...] | Art. [x] DBA | [Hoechstsatz/Belegenheit] | [Recht Quellenstaat: ...] | DBA-Text |
| Methode | [...] | Art. 23 + § 34c EStG | [Freistellung/Anrechnung] | [Methode] | Methodenartikel |
| Treaty Override | [...] | § 50d Abs. 3/8/9 EStG | [Substanz/Subject-to-Tax] | [greift/greift nicht] | BMF-Schreiben |
| Verfahren | [...] | § 50a, § 50c EStG | [Vorab/Nachher] | [Antragsweg] | BOP |

## Querverweise

- `stb-dba-grundprinzip-oecd-musterabkommen` — Pruefkette.
- `stb-dba-ansaessigkeit-tie-breaker-rules` — Ansaessigkeit.
- `stb-dba-betriebsstaette-art-5-musterabkommen` — BS.
- `stb-dba-methodenartikel-anrechnung-vs-freistellung` — Methode.
- `stb-dba-quellensteuer-erstattung-bzst-50c-estg` — BZSt-Verfahren.
- `stb-dba-edge-cases-playbook` — Edge-Cases.
- `stb-dba-quellensteuer-atlas-weltweit` — Quellensteuer drei Ebenen.
- `stb-dba-map-eu-streitbeilegung` — bei Doppelbesteuerung.
