---
name: settlement-court-shareholder-board
description: "Settlement Court Shareholder Board: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Settlement Court Shareholder Board

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Settlement Court Shareholder Board** im Plugin Commercial Courts Deutschland. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `settlement-court-recorded-settlement` | Bereitet gerichtlichen Vergleich, settlement agreement, consent order, Vollstreckbarkeit und mehrsprachige Vergleichsdokumentation vor. |
| `shareholder-board-dispute` | Bearbeitet Gesellschafter-, Organ- und Joint-Venture-Streitigkeiten mit englischen Vertragsunterlagen vor deutschen Commercial Courts. |

## Arbeitsweg

Im Plugin Commercial Courts Deutschland gilt für **Settlement Court Shareholder Board**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `settlement-court-recorded-settlement`

**Fokus:** Bereitet gerichtlichen Vergleich, settlement agreement, consent order, Vollstreckbarkeit und mehrsprachige Vergleichsdokumentation vor.

# Settlement

## Fachkern: Settlement
- **Spezialgegenstand:** Settlement. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
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

## 2. `shareholder-board-dispute`

**Fokus:** Bearbeitet Gesellschafter-, Organ- und Joint-Venture-Streitigkeiten mit englischen Vertragsunterlagen vor deutschen Commercial Courts.

# Shareholder and Board Disputes

## Fachkern: Shareholder and Board Disputes
- **Spezialgegenstand:** Shareholder and Board Disputes. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
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

### Streitarten Gesellschafter-/Organstreitigkeiten

| Streittyp | Norm | Forum | Frist |
| --- | --- | --- | --- |
| Anfechtungsklage AG-Hauptversammlung | § 246 AktG | LG/OLG | 1 Monat |
| Nichtigkeitsklage AG-Beschluss | § 249 AktG | LG/OLG | grds. unbefristet, Verwirkung möglich |
| Anfechtungsklage GmbH-Gesellschafterversammlung | analog §§ 241 ff. AktG (BGH ständige Rechtsprechung) | LG am Sitz der GmbH | grds. 1 Monat, im Einzelfall angemessene Frist |
| Beschlussfeststellungsklage | § 256 ZPO | dito | innerhalb angemessener Frist |
| Verlust-/Schadensersatzklage gegen Vorstand/Geschäftsführer | § 93 AktG / § 43 GmbHG | LG/OLG | 5 Jahre § 93 Abs. 6 AktG / § 195 BGB |
| Auflösungsklage | § 61 GmbHG / § 117 BGB | LG am Sitz | grds. unbefristet |
| Einziehungsklage / Klage auf Hinausweisung | § 34 GmbHG | LG | wichtiger Grund nötig |
| Joint-Venture-Streit (vertraglich) | §§ 280, 311 BGB | Commercial Court / Schieds | Vertragsbasis |
| Geschäftsführerabberufung gerichtlich | § 38 GmbHG, § 84 AktG | LG | bei wichtigem Grund jederzeit |

### Eilrechtsschutz Optionen

| Maßnahme | Norm | Beispielfälle |
| --- | --- | --- |
| Einstweilige Verfügung | § 935 ZPO | Untersagung Hauptversammlungsbeschluss-Vollzug, Veröffentlichung im HR |
| Arrest | § 916 ZPO | Sicherung Geldforderung (z.B. § 93 AktG Schadensersatz) |
| Einstweilige Verfügung Geschäftsführer-Sperre | § 935 ZPO | Verfügungsbeschränkung |
| Vorläufige Bestellung Geschäftsführer | § 29 BGB analog / § 85 AktG | bei Führungslosigkeit |

### Trade-off Klage vs. Schiedsgericht in Gesellschafterstreitigkeiten

- **Klage vor LG:** öffentlich, Berufungsmöglichkeit, BGH-Rechtsprechung beruft sich auf bestehende Linie.
- **Schiedsgericht (DIS, ICC):** vertraulich, eine Instanz, schnellere Verfahren.
- **"Schiedsfähigkeit II"-Anforderungen:** BGH ständige Rechtsprechung verlangt für Schiedsklauseln in Gesellschaftsverträgen GmbH besondere Anforderungen (alle Gesellschafter müssen Klagebeteiligungsrechte haben, Veröffentlichung des Spruchs etc.). Bei Verstoß: Schiedsabrede unwirksam.

### Praktiker-Tipp

- **Sofortmaßnahmen bei drohendem Beschlussvollzug:** Klage UND einstweilige Verfügung parallel; die Klage hält die Monatsfrist § 246 AktG ein, die eV verhindert vorläufigen Vollzug.
- **Beweissicherung:** Tonbandaufnahmen von Versammlungen nur mit Einverständnis aller Teilnehmer (§ 201 StGB Strafbarkeit ohne Einverständnis!). Lieber Protokoll vom Notar.
- **D&O-Versicherung beachten:** Bei Klage gegen Geschäftsführer/Vorstand schnell D&O-Versicherer informieren; Deckungsfrist oft kurz (28 Tage).

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
