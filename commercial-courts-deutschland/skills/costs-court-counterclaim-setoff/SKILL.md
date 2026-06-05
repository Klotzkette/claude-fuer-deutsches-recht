---
name: costs-court-counterclaim-setoff
description: "Costs Court Counterclaim Setoff: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Costs Court Counterclaim Setoff

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Costs Court Counterclaim Setoff** im Plugin Commercial Courts Deutschland. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `costs-court-fees-risk-budget` | Erstellt Kosten- und Risikobudget: Gerichtskosten, Anwaltskosten, Übersetzung, Transcript, Sachverständige, Security, Settlement und Enforcement. |
| `counterclaim-setoff-claim-amendment` | Plant Widerklage, Hilfswiderklage, Aufrechnung, Klageänderung und amendment strategy in englischsprachigen Wirtschaftsprozessen. |

## Arbeitsweg

Im Plugin Commercial Courts Deutschland gilt für **Costs Court Counterclaim Setoff**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `costs-court-fees-risk-budget`

**Fokus:** Erstellt Kosten- und Risikobudget: Gerichtskosten, Anwaltskosten, Übersetzung, Transcript, Sachverständige, Security, Settlement und Enforcement.

# Costs and Budget

## Fachkern: Costs and Budget
- **Spezialgegenstand:** Costs and Budget. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
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

### Kosten-Modell deutsches Verfahren (auch Commercial Court)

| Kostenart | Norm | Berechnungsgrundlage |
| --- | --- | --- |
| Gerichtskosten | GKG (Gerichtskostengesetz), insbesondere Anlage 1 KV | Streitwert-degressiv; 3,0-Gebühr bei LG-Klage erste Instanz, ermäßigt auf 1,0 bei frühem Vergleich |
| Anwaltskosten Inland | RVG, insbesondere VV 3100 (Verfahrens-1,3), 3104 (Termins-1,2), 3200 (Berufung) | Streitwertabhängige Gebühren oder Vergütungsvereinbarung § 3a RVG |
| Vergütungsvereinbarung | § 3a RVG | Stundensätze grosskanzlei-typisch 350-700 EUR; Mandatsbedarf bei internationalen Streitigkeiten |
| Übersetzungen | JVEG | 1,55 EUR pro angefangene 55 Zeichen Standardtext; bei Anlagen oft erhebliche Posten |
| Wortprotokoll § 613 ZPO Justizstandort-Stärkungsgesetz | JVEG | Stenografie/Tonprotokoll kostenpflichtig, vorher Antrag |
| Sachverständige | § 8 ff. JVEG | nach Honorargruppen; bei IT/Finanz oft hoch (Honorargruppe M3) |
| Sicherheitsleistung Ausländer | § 110 ZPO Prozesskostensicherheit | Kläger ohne Wohnsitz/Sitz in EU/EWR |
| Streitwert Zwischenfeststellung | § 256 ZPO | für Sicherungsverfahren oft niedriger als Hauptsacheverfahren |
| Vollstreckungskosten | GvKostG, § 788 ZPO | trägt Schuldner |

### Schwellen-Beispiele Streitwert/Gerichtsgebühren (orientativ; live aktuelle KV-Werte prüfen)

| Streitwert | Verfahrensgebühr 3,0 (KV 1210) | Berufungsgebühr 4,0 (KV 1220) |
| --- | --- | --- |
| 100.000 EUR | ca. 3.273 EUR | ca. 4.364 EUR |
| 500.000 EUR | ca. 10.041 EUR | ca. 13.388 EUR |
| 5.000.000 EUR | ca. 49.143 EUR (Höchstsatz erreichbar) | dito |

(Stand vor letzter GKG-Novelle, vor Verwendung im Mandat aktuelle Gebührentabelle bestätigen.)

### Trade-off Kostenmodell

- **Streitwertdeckelung GKG:** ab ca. 30 Mio. EUR Streitwert Höchstgebühr; bei Mega-Mandaten Gericht "billig" gegenüber Schiedsgericht.
- **Erstattungsfähigkeit:** Vergütungsvereinbarung übersteigt RVG nicht erstattbar gegenüber Gegner (§ 3a Abs. 1 RVG, § 91 ZPO Grenzen). Bei W&I-Verfahren regelmäßiger Streitpunkt.
- **Cost Cap mit Mandant:** §§ 49b BRAO, § 4 RVG: keine Erfolgshonorare grundsätzlich (Ausnahmen § 4a RVG nur bei wirtschaftlicher Notwendigkeit).

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

## 2. `counterclaim-setoff-claim-amendment`

**Fokus:** Plant Widerklage, Hilfswiderklage, Aufrechnung, Klageänderung und amendment strategy in englischsprachigen Wirtschaftsprozessen.

# Counterclaim and Set-off

## Fachkern: Counterclaim and Set-off
- **Spezialgegenstand:** Counterclaim and Set-off. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
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
2. **Widerklage-Voraussetzungen (§ 33 ZPO):** Konnexität (rechtlicher Zusammenhang mit Klagegegenstand oder Verteidigungsmitteln); sachliche Zuständigkeit muss gegeben sein (bei Commercial Court Streitwert mindestens 500.000 EUR nach Justizstandort-Stärkungsgesetz, bei Anrufung Commercial Chamber regelmäßig herabgesetzte Schwellen je Landesrecht). Englische Sprache der Widerklage folgt der Hauptklage, wenn § 184 GVG i.V.m. Landesverordnung greift.
3. **Aufrechnung (§ 388 BGB / § 145 Abs. 3 ZPO):** Materielle Aufrechnungserklärung Gegenseitigkeit, Gleichartigkeit, Wirksamkeit, Fälligkeit der aktiven Forderung. Prozessual Hilfsaufrechnung als hilfsweise vorgetragene Verteidigung; Trennung in vorrangige Hauptverteidigung und Eventualaufrechnung dokumentieren.
4. **Klageänderung (§ 263 ZPO):** Zustimmung des Beklagten oder Sachdienlichkeit; Sachdienlichkeit liegt vor, wenn der bisherige Prozessstoff verwertet werden kann und kein neues Sachverhaltsfundament aufzubauen ist. Bei Klageerweiterung um Streitwert: erneute Prüfung Zuständigkeit, ggf. Verweisung.
5. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären. Nächsten Schritt mit Frist, Owner, Anlagen festlegen.

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
