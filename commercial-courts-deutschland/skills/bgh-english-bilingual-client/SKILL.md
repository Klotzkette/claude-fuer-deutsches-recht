---
name: bgh-english-bilingual-client
description: "BGH English Bilingual Client: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# BGH English Bilingual Client

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **BGH English Bilingual Client** im Plugin Commercial Courts Deutschland. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bgh-english-proceedings-184b-gvg` | Routet englischsprachige Fortführung vor dem Bundesgerichtshof: Voraussetzungen, Übersetzungen, Revisionsbegründung, Tenor und Mandantenkommunikation. |
| `bilingual-client-board-briefing` | Erstellt bilinguale Board- und Mandantenbriefings zu Commercial-Court-Verfahren: risk, timeline, budget, settlement range, next decisions. |

## Arbeitsweg

Im Plugin Commercial Courts Deutschland gilt für **BGH English Bilingual Client**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bgh-english-proceedings-184b-gvg`

**Fokus:** Routet englischsprachige Fortführung vor dem Bundesgerichtshof: Voraussetzungen, Übersetzungen, Revisionsbegründung, Tenor und Mandantenkommunikation.

# BGH in English

## Fachkern: BGH in English
- **Spezialgegenstand:** BGH in English. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Dieser Skill unterstützt Verfahren vor deutschen Commercial Courts oder Commercial Chambers mit internationalem Wirtschaftsbezug. Er liefert eine prozessuale Arbeitsstruktur und, wenn gewünscht, englischen Output. Deutsches Prozessrecht bleibt der Rahmen; englische Sprache bedeutet nicht Common-Law-Verfahren.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

### BGH-Revision auf Englisch nach § 184b GVG

Das Justizstandort-Stärkungsgesetz hat § 184b GVG eingeführt: Revision vor dem BGH kann in englischer Sprache geführt werden, wenn die Vorinstanz (Commercial Court oder Commercial Chamber) auf Englisch verhandelt hat und beide Parteien zustimmen.

| Verfahrensschritt | Praxishinweis | Norm |
| --- | --- | --- |
| Voraussetzung erstinstanzliches Verfahren | mündliche Verhandlung und Urteil in Englisch (§ 184a GVG) | § 184b Abs. 1 GVG |
| Antrag bei BGH | förmlicher Antrag, Zustimmung beider Parteien | § 184b Abs. 1 Satz 1 GVG |
| Anwalt für BGH | nur am BGH zugelassener Rechtsanwalt § 78 ZPO Abs. 1 Satz 3 ZPO i.V.m. §§ 162 ff. BRAO | Sprachkenntnisse zwingend; Liste BGH-Anwälte sehr begrenzt |
| Revisionsbegründung | innerhalb der Frist § 551 ZPO; in Englisch zulässig | nur Rechtsfragen, kein neuer Tatsachenvortrag (§ 559 ZPO) |
| Mündliche Verhandlung | sofern BGH zulässt; oft schriftliches Verfahren | Sprache Englisch |
| Tenor und Begründung | Englisch zulässig; für Vollstreckung Übersetzung nach § 110 ZPO bzw. Brüssel Ia-VO Art. 42 | praxisrelevant |
| Veröffentlichung | BGH-Datenbank meist deutsch; englische Originalfassung als Anlage | § 169 GVG |
| Streitwert | Revisionsbeschwer § 26 Nr. 8 EGZPO (z.Zt. 20.000 EUR Mindestbeschwer für Nichtzulassungsbeschwerde) | live aktuelle Schwelle prüfen |

### Trade-off Englisch versus Übersetzung

- **Englisch bis BGH:** spart Übersetzungskosten und Brüche; aber sehr enger Anwaltskreis (BGH-Anwälte mit Englisch-Praxis).
- **Schwächen:** Anlagen aus früheren Verfahren oft Deutsch; nicht alle BGH-Senate haben Spracherfahrung; bei Aufhebung und Zurückverweisung muss Tatsacheninstanz die Sprache fortführen können.
- **Praktiker-Tipp:** Bereits in Klage und Berufung BGH-Anwalt einbinden, der später Revision führen kann.

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Output-Standard

- **Executive Snapshot:** forum, language, next deadline, procedural risk.
- **Procedural Action:** konkreter nächster Antrag/Schriftsatz/Briefing in der gewünschten Sprache.
- **Evidence and Exhibits:** welche Anlagen tragen welchen Punkt, welche Übersetzung fehlt.
- **Risk Flags:** Zuständigkeit, Sprache, Frist, Geheimnis, Kosten, Rechtsmittel.
- **Follow-up Skills:** passende Skills aus diesem Plugin vorschlagen.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

## Quellenregel

Vor echter Verwendung aktuelle Primärquellen prüfen: GVG, ZPO, einschlägige Landesverordnungen und die Gerichtsseite des zuständigen Landes. Keine erfundenen Gerichtslisten, keine erfundenen Formularpflichten, keine Paywall-Fundstellen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `bilingual-client-board-briefing`

**Fokus:** Erstellt bilinguale Board- und Mandantenbriefings zu Commercial-Court-Verfahren: risk, timeline, budget, settlement range, next decisions.

# Bilingual Board Briefing

## Fachkern: Bilingual Board Briefing
- **Spezialgegenstand:** Bilingual Board Briefing. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Dieser Skill unterstützt Verfahren vor deutschen Commercial Courts oder Commercial Chambers mit internationalem Wirtschaftsbezug. Er liefert eine prozessuale Arbeitsstruktur und, wenn gewünscht, englischen Output. Deutsches Prozessrecht bleibt der Rahmen; englische Sprache bedeutet nicht Common-Law-Verfahren.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

### Bilinguales Board Briefing — Strukturmuster

#### Executive Summary (Deckblatt)

| Punkt | Inhalt | Maximal |
| --- | --- | --- |
| Status | Verfahrensstand in 1-2 Sätzen | 50 Wörter |
| Nächste Frist | Datum, Akt, Verantwortlicher | 1 Zeile |
| Risiko Ampel | Grün/Gelb/Rot mit Begründung | 1 Zeile |
| Budget update | Forecast vs. Actual, Abweichung | 1 Zeile |
| Settlement range | Likelihood + Range (z.B. 50-65 % Wahrscheinlichkeit, 2-3 Mio. EUR) | 2 Zeilen |
| Board decision needed | Y/N + Frist | 1 Zeile |

#### Detail-Sektionen (DE/EN paralleler Aufbau)

1. **Sachverhalt / Background.** Was ist passiert, in 3-5 Sätzen.
2. **Rechtsfragen / Legal Issues.** 3-5 Bullet Points, Sprache angemessen für Vorstand (kein juristischer Jargon).
3. **Verfahrensgang / Procedural Timeline.** Bisherige Schritte, anstehende Termine.
4. **Budget und Kostenrisiko / Budget and Cost Risk.** Eigenes Honorar, Gegnerkosten, GKG, Sachverständige, Übersetzungen.
5. **Vergleichsoptionen / Settlement Options.** Range, Reputationsfolgen, Präzedenzwirkung.
6. **Board Decision Items.** Konkrete Entscheidungspunkte (z.B. "Soll Vorstand Vergleichsmandat bis 3,5 Mio. EUR autorisieren?").

### Trade-off Sprache des Briefings

| Modus | Pro | Contra |
| --- | --- | --- |
| Nur Englisch | spart Übersetzung, internationaler Vorstand | deutsche Spezifika werden flach |
| Nur Deutsch | präzise rechtliche Begriffe | ausländische Vorstandsmitglieder verstehen weniger |
| Bilingual parallel | beide Welten | aufwendig, doppelte Pflege |
| Englisch mit deutschen Fachbegriffen in Klammern | guter Kompromiss | längerer Text |

### Berufsrechtliche Hinweise

- **Mandantengeheimnis § 43a Abs. 2 BRAO, § 203 StGB:** Board-Briefing nur an befugte Empfänger (Vorstand, Aufsichtsrat); Verteiler-Liste pflegen.
- **Insiderrecht Art. 17 MAR:** Bei börsennotierter Gesellschaft Briefing kann insiderrelevante Information enthalten. Compliance-Stelle einbinden.
- **D&O-Versicherung:** Briefing kann später als Beweis für ordnungsgemäße Information des Boards in D&O-Haftungsprozess dienen. Versionierung und Archivierung.

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Output-Standard

- **Executive Snapshot:** forum, language, next deadline, procedural risk.
- **Procedural Action:** konkreter nächster Antrag/Schriftsatz/Briefing in der gewünschten Sprache.
- **Evidence and Exhibits:** welche Anlagen tragen welchen Punkt, welche Übersetzung fehlt.
- **Risk Flags:** Zuständigkeit, Sprache, Frist, Geheimnis, Kosten, Rechtsmittel.
- **Follow-up Skills:** passende Skills aus diesem Plugin vorschlagen.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

## Quellenregel

Vor echter Verwendung aktuelle Primärquellen prüfen: GVG, ZPO, einschlägige Landesverordnungen und die Gerichtsseite des zuständigen Landes. Keine erfundenen Gerichtslisten, keine erfundenen Formularpflichten, keine Paywall-Fundstellen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
