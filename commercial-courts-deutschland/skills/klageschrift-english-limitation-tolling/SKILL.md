---
name: klageschrift-english-limitation-tolling
description: "Klageschrift English Limitation Tolling: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Klageschrift English Limitation Tolling

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Klageschrift English Limitation Tolling** im Plugin Commercial Courts Deutschland. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `klageschrift-english-statement-of-claim` | Erstellt eine englische Commercial-Court-Klageschrift mit deutschem ZPO-Unterbau: parties, jurisdiction, facts, causes of action, relief sought, evidence und exhibits. |
| `limitation-and-tolling-check` | Prüft Verjährung, Hemmung, Standstill, Klageerhebung, Zustellung demnächst und internationale Limitation Issues. |

## Arbeitsweg

Im Plugin Commercial Courts Deutschland gilt für **Klageschrift English Limitation Tolling**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `klageschrift-english-statement-of-claim`

**Fokus:** Erstellt eine englische Commercial-Court-Klageschrift mit deutschem ZPO-Unterbau: parties, jurisdiction, facts, causes of action, relief sought, evidence und exhibits.

# Statement of Claim

## Fachkern: Statement of Claim
- **Spezialgegenstand:** Statement of Claim. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
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

## 2. `limitation-and-tolling-check`

**Fokus:** Prüft Verjährung, Hemmung, Standstill, Klageerhebung, Zustellung demnächst und internationale Limitation Issues.

# Limitation and Tolling

## Fachkern: Limitation and Tolling
- **Spezialgegenstand:** Limitation and Tolling. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
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

### Verjährungs- und Hemmungs-Karte

| Anspruchsart | Verjährung | Norm | Hinweis |
| --- | --- | --- | --- |
| Regelmäßige Verjährung | 3 Jahre | § 195 BGB | Beginn § 199 Abs. 1 BGB: Ende des Jahres, in dem Anspruch entstanden und Kenntnis (oder grob fahrlässige Unkenntnis) der anspruchsbegründenden Tatsachen |
| Schadensersatz wegen Verletzung des Lebens, Körpers, Gesundheit, Freiheit | 30 Jahre | § 199 Abs. 2 BGB | absolute Höchstgrenze |
| Andere Schadensersatzansprüche | 10 Jahre / 30 Jahre | § 199 Abs. 3 BGB | absolute Höchstgrenze; ab Begehung der Handlung |
| Kaufrechtliche Mängelansprüche bewegliche Sachen | 2 Jahre | § 438 BGB | ab Ablieferung |
| Bauwerk-Mängel | 5 Jahre | § 438 Abs. 1 Nr. 2 BGB / § 634a BGB | ab Abnahme |
| Werkvertrag Mängel | 2 Jahre / 5 Jahre | § 634a BGB | bewegliches Werk versus Bauwerk |
| Handelsrechtliche Mängelrüge | unverzüglich | § 377 HGB | Sonderregel, KEINE Verjährung sondern Ausschlussfrist |
| Anfechtungsklage AG-Beschluss | 1 Monat | § 246 AktG | absolute Frist, keine Hemmung |
| Anfechtungsklage GmbH-Beschluss | analoge Anwendung; angemessene Frist (BGH ständige Rechtsprechung) | analog § 246 AktG | grundsätzlich 1 Monat |
| Kündigungsschutzklage | 3 Wochen | § 4 KSchG | absolut |
| Befristungskontrollklage | 3 Wochen | § 17 TzBfG | absolut |
| Anspruch aus c.i.c. | 3 Jahre | § 195 BGB | mit Kenntnis |

### Hemmung der Verjährung (§§ 203 ff. BGB)

| Hemmungsgrund | Norm | Mechanik |
| --- | --- | --- |
| Verhandlungen | § 203 BGB | Hemmung solange Verhandlungen schweben; endet 3 Monate nach letzter Erklärung |
| Rechtsverfolgung (Klage, Mahnbescheid) | § 204 BGB | Klage rechtshängig oder Mahnbescheid zugestellt |
| Schiedsverfahren | § 204 Abs. 1 Nr. 11 BGB | mit Einleitung |
| Höhere Gewalt | § 206 BGB | letzte 6 Monate der Frist |
| Standstill Agreement | § 202 BGB analog | vertragliche Vereinbarung Verjährungshemmung |

### Zustellung "demnächst" § 167 ZPO

- Bei Klage- oder Mahnbescheidseinreichung am letzten Verjährungstag ist die Zustellung "demnächst" entscheidend für Rückwirkung.
- BGH ständige Rechtsprechung: "demnächst" wird großzügig ausgelegt; Verzögerungen bis ca. 14 Tage unschädlich, sofern nicht der Kläger sie zu vertreten hat (z.B. keine Vorschusszahlung GKG).
- Praxistipp: Gerichtskostenvorschuss SOFORT nach Klageeingang einzahlen, sonst keine "demnächst"-Wirkung.

### Trade-off und Praktiker-Tipp

- **Verjährungshemmung durch Verhandlungen § 203 BGB:** vorsicht — schweigt die Gegenseite mehrere Wochen, gilt § 203 Satz 1 BGB als beendet (Aufgabe der Verhandlungen). Lieber regelmäßig "Wir verhandeln noch"-Schreiben.
- **Standstill statt Klage:** bei drohendem Verjährungseintritt schriftliche Vereinbarung mit Gegnerseite über Verjährungsstreichung. Vorteil: Zeit für Aufklärung. Nachteil: Gegner kann jederzeit zurückspringen.
- **Internationale Verjährung:** Bei Rom I-VO Art. 4 anwendbares Recht; Verjährung folgt grundsätzlich materiellem Vertragsstatut. Bei deutsch-amerikanischen Verträgen oft Streit, weil US-Statute-of-Limitations sehr unterschiedlich.

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
