---
name: forumwahl-court-glossary
description: "Forumwahl Commercial Court Vs Schiedsgericht, Glossary Commercial Court De En: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Forumwahl Commercial Court Vs Schiedsgericht, Glossary Commercial Court De En

## Arbeitsbereich

Dieser Skill bündelt **Forumwahl Commercial Court Vs Schiedsgericht, Glossary Commercial Court De En** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `forumwahl-commercial-court-vs-schiedsgericht` | Vergleicht Commercial Court, ordentliche Kammer, Schiedsgericht, DIS/ICC/LCIA und Gerichtsstandsvereinbarung; Output ist eine Vorstandsvorlage mit Empfehlung. |
| `glossary-commercial-court-de-en` | Erstellt ein DE/EN-Glossar für Commercial-Court-Mandate: ZPO-Begriffe, Anträge, Beweis, Tenor, Vergleich, Rechtsmittel und falsche Freunde. |

## Arbeitsweg

Für **Forumwahl Commercial Court Vs Schiedsgericht, Glossary Commercial Court De En** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `commercial-courts-deutschland` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `forumwahl-commercial-court-vs-schiedsgericht`

**Fokus:** Vergleicht Commercial Court, ordentliche Kammer, Schiedsgericht, DIS/ICC/LCIA und Gerichtsstandsvereinbarung; Output ist eine Vorstandsvorlage mit Empfehlung.

# Forumwahl gegenüber Schiedsgericht

## Fachkern: Forumwahl gegenüber Schiedsgericht
- **Spezialgegenstand:** Forumwahl gegenüber Schiedsgericht; dieser Skill beginnt mit der Sachfrage und liefert eine konkrete Lösung statt bloßer Orientierung.
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

### Forum-Vergleich (Vorstandsvorlage)

| Kriterium | Commercial Court (OLG) | Commercial Chamber (LG) | Schiedsgericht (DIS, ICC, LCIA) | Ordentliches LG (KfH) |
| --- | --- | --- | --- | --- |
| Rechtsgrundlage | § 119b GVG | §§ 95, 184a GVG | §§ 1029 ff. ZPO | §§ 95 ff. GVG |
| Streitwert | regelmäßig ab 500.000 EUR | ohne harte Schwelle | ohne | nach GVG-Schwellen |
| Sprache | DE/EN | DE/EN | frei wählbar | DE |
| Vertraulichkeit | § 273a ZPO Anordnung möglich | dito | grundsätzlich gegeben | öffentliche Verhandlung |
| Beweisaufnahme | richterliche Prozessleitung | dito | flexibler; nahe Common Law möglich | dito |
| Dauer (erste Instanz) | ca. 12-18 Monate | ca. 18-30 Monate | ca. 12-24 Monate (Institut) | ca. 18-30 Monate |
| Berufung / Rechtsmittel | nur Revision § 184b GVG zum BGH | Berufung OLG, Revision BGH | nur Aufhebung § 1059 ZPO | dito ordentliche Wege |
| Vollstreckung Ausland | EuGVVO/Brüssel Ia EU; sonst Anerkennungsverfahren | dito | New York Convention 1958 weltweit | dito |
| Kosten | GKG + RVG | dito | Schiedsrichterhonorare + Institut + Anwälte | GKG + RVG |
| Anwaltszwang | ja | ja | abhängig von Schiedsordnung | ja |
| Wahl der Richter | nein | nein | ja (party-appointed) | nein |
| Eilrechtsschutz | §§ 916, 935 ZPO Arrest/eV | dito | sehr eingeschränkt; staatliche Gerichte daneben § 1033 ZPO | dito |

### Trade-off Argumente

| Pro Commercial Court / Chamber | Pro Schiedsgericht |
| --- | --- |
| Günstiger Streitwert ab 5-10 Mio. EUR (gedeckelte GKG) | Vertraulichkeit zentral (kein Filing, keine Pressepräsenz) |
| BGH-Revision als Rechtssicherheit | freie Schiedsrichterwahl, Branchen-Expertise |
| Schnellere mündliche Verhandlung | weltweite Vollstreckung New York Convention |
| Staatliche Autorität bei renitentem Gegner | bei Cross-Border-Fällen ohne EU-Bezug oft schneller |
| Wortprotokoll § 613 ZPO neu | Sprachwahl ohne § 184a GVG-Beschluss |
| Klare Anwendung deutschen materiellen Rechts | Verfahrensautonomie (UNCITRAL-Model) |

### Empfehlung je Fallkonstellation

| Konstellation | Empfehlung |
| --- | --- |
| Inhouse-Streit, Beschlussmängelklage GmbH | Commercial Chamber LG (BGH-Rspr. "Schiedsfähigkeit II" zu Schiedsklauseln im Gesellschaftsvertrag beachten) |
| Post-M&A Warranty Claim 5-50 Mio. EUR | Commercial Court OLG oder Schiedsgericht (W&I-Versicherer hat Mitspracherecht) |
| Cross-Border-Lieferkette, Vollstreckung in USA/Asien | Schiedsgericht (NYC Convention) |
| Massive Geheimhaltung (Patente, Trade Secrets) | Schiedsgericht oder Commercial Court mit § 273a ZPO |
| Schnelles Urteil mit hoher Reputationswirkung | Commercial Court OLG (Publicity) |
| Lieferantenstreit unter 5 Mio. EUR | KfH LG (kosten- und schnellgerecht) |

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

## 2. `glossary-commercial-court-de-en`

**Fokus:** Erstellt ein DE/EN-Glossar für Commercial-Court-Mandate: ZPO-Begriffe, Anträge, Beweis, Tenor, Vergleich, Rechtsmittel und falsche Freunde.

# Commercial Court Glossary

## Fachkern: Commercial Court Glossary
- **Spezialgegenstand:** Commercial Court Glossary; dieser Skill beginnt mit der Sachfrage und liefert eine konkrete Lösung statt bloßer Orientierung.
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

## Glossar (Kernbegriffe DE/EN, mit falschen Freunden)

| Deutsch | Englisch | Hinweis / Falscher Freund |
| --- | --- | --- |
| Klageschrift | statement of claim | nicht "complaint" (US), nicht "pleading" allgemein |
| Klageerwiderung | statement of defence | nicht "answer" (US-Stil) |
| Antrag (im Schriftsatz) | request / motion | "motion" eher US; in DE: Antrag im Sinne von § 308 ZPO Bindung |
| Tenor | operative part of the judgment | "Tenor" nicht wörtlich übernehmen |
| Tatbestand | summary of facts / statement of facts | nicht "tatbestand" (clipping unverständlich) |
| Entscheidungsgründe | reasons / grounds of the decision | "decision" nicht ausreichend |
| Beweisangebot | offer of evidence / evidence proffered | nicht "discovery"; deutscher Prozess kennt keine Discovery |
| Substantiierungspflicht | duty of substantiation / specificity requirement | enge Anforderung, nicht "notice pleading" |
| Streitwert | amount in dispute / value of the claim | wichtig für Zuständigkeit und Gebühren |
| Vergleich (gerichtlich) | court settlement | nicht "comparison" |
| Aufrechnung | set-off | spezifisch § 388 BGB, nicht "offset" |
| Widerklage | counterclaim | § 33 ZPO, mit Konnexität |
| Mündliche Verhandlung | oral hearing | nicht "trial" (Common-Law-Begriff impliziert Jury) |
| Sachverständigengutachten | expert opinion / court-appointed expert | Gericht bestellt, keine Parteigutachter im Sinne der CPR |
| Vollstreckungstitel | enforceable title | Art. 53 Brüssel Ia bei Auslandsvollstreckung |

## Arbeitsworkflow

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Glossar einsetzen:** Begriff im Kontext belegen, falsche Freunde vermeiden (besonders "complaint", "motion", "discovery", "trial"), bei Erstnennung eines Begriffs deutschen Originalbegriff in Klammern führen.
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
