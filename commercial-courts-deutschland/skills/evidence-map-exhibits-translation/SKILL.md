---
name: evidence-map-exhibits-translation
description: "Evidence MAP Exhibits Translation: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Evidence MAP Exhibits Translation

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Evidence MAP Exhibits Translation** im Plugin Commercial Courts Deutschland. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `evidence-map-zpo-vs-common-law` | Erklärt Mandanten den Unterschied zwischen deutscher Beweisaufnahme und Common-Law-Erwartungen; erstellt Evidence Map ohne Discovery-Fantasien. |
| `exhibits-translation-608-zpo` | Plant Anlagen, Übersetzungen und Sprache: welche Dokumente englisch bleiben können, wann Übersetzung nötig ist, wie Exhibit Index und Bundle aussehen. |

## Arbeitsweg

Im Plugin Commercial Courts Deutschland gilt für **Evidence MAP Exhibits Translation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `evidence-map-zpo-vs-common-law`

**Fokus:** Erklärt Mandanten den Unterschied zwischen deutscher Beweisaufnahme und Common-Law-Erwartungen; erstellt Evidence Map ohne Discovery-Fantasien.

# Evidence Map ZPO/Common Law

## Fachkern: Evidence Map ZPO/Common Law
- **Spezialgegenstand:** Evidence Map ZPO/Common Law. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
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

### Beweismittel-Vergleich ZPO versus Common Law

| Punkt | Deutsche ZPO | US/UK Common Law |
| --- | --- | --- |
| Beweiserhebungsumfang | beschränkt; § 138 ZPO Wahrheitspflicht, kein "fishing expedition" | breite Discovery; broad relevance |
| Dokumentenvorlage | § 142 ZPO (Anordnung Vorlage Urkunde der Partei oder Dritten); § 421 ZPO (Pflicht zur Vorlage bei Anspruch) | Document Production / Disclosure, Privilege Log |
| Zeugen | benannte Zeugen § 373 ZPO, Vernehmung durch Richter (§ 397 Abs. 1 ZPO) | Deposition, Cross-Examination, Witness Statement |
| Sachverständige | gerichtlich bestellt § 404 ZPO, neutral | Party-Appointed Expert, Battle of Experts |
| Akteneinsicht | § 299 ZPO, beschränkt | Public Filings, PACER |
| Privileged Documents | § 383 ZPO Zeugnisverweigerung Anwalt; nur Mandatsverhältnis | Attorney-Client Privilege, Work Product |
| Verspätungspräklusion | § 296 ZPO; verspäteter Vortrag wird zurückgewiesen | flexibel; "trial by ambush" zulässig im Mandat |
| Beweismaß | volle Überzeugung § 286 ZPO; ausnahmsweise § 287 ZPO Schätzung | Preponderance of evidence (Zivilrecht), Beyond reasonable doubt (Strafrecht) |
| Wahrheitspflicht | § 138 Abs. 1 ZPO | nicht direkt; Sanctions for perjury |

### Was Mandant aus dem Common Law mitbringt — und was nicht funktioniert

| Wunsch des Mandanten (Common Law-Erwartung) | ZPO-Antwort |
| --- | --- |
| "Discovery vom Gegner" | nicht möglich; nur § 142 ZPO Einzelanordnung mit konkreter Bezeichnung |
| "Cross-Examination" | beschränkt; Richter befragt zuerst, Anwälte ergänzen § 397 ZPO |
| "Witness Statement statt Aussage" | nicht prozessgemäß; nur gerichtliche Vernehmung zählt |
| "Subpoena to Third Party" | § 142 ZPO mit Beschränkungen; bei Auslandsbezug Haager Beweisaufnahme |
| "Privilege Log" | nicht erforderlich; deutsche Anwälte können einzelne Dokumente zurückhalten |
| "E-Discovery" | nicht standardisiert; aber Geschäftsleitungs-Bevollmächtigte können Daten kontextbezogen vorlegen |
| "Disclosure of Documents" | nicht generell; § 142 ZPO und § 810 BGB nur einzelfallbezogen |
| "Self-Disclosure (Rule 26 USA)" | nicht; deutsche Beweismittel müssen angeboten und vom Richter beigezogen werden |

### Trade-off

- **Mehrwert ZPO:** kostengünstiger, schneller, Geheimhaltung höher (kein US-Style-Public-Filing).
- **Mehrwert Common Law:** Document Production zwingt Gegner zur Offenlegung; deutsche Partei "fischt" oft im Dunkeln.
- **Praktiker-Tipp Mandantenkommunikation:** Vor jedem Termin Erwartungs-Management; klares Memo "Was in Deutschland prozessual geht und was nicht" für US-/UK-Inhouse-Counsel.

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

## 2. `exhibits-translation-608-zpo`

**Fokus:** Plant Anlagen, Übersetzungen und Sprache: welche Dokumente englisch bleiben können, wann Übersetzung nötig ist, wie Exhibit Index und Bundle aussehen.

# Exhibits und Übersetzung

## Fachkern: Exhibits und Übersetzung
- **Spezialgegenstand:** Exhibits und Übersetzung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
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

Besondere Anker: § 184a GVG und §§ 606 ff. ZPO. Übersetzungslogik gehört in den Anlagenindex: Originalsprache, benötigte Übersetzung, zitierte Passagen, Kosten, Frist und Zustellungsrisiko.

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
