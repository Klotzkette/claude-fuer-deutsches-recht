---
name: cross-border-default-judgment
description: "Cross Border Default Judgment: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Cross Border Default Judgment

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Cross Border Default Judgment** im Plugin Commercial Courts Deutschland. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `cross-border-jurisdiction-brussels-ia` | Prüft internationale Zuständigkeit, Gerichtsstandsvereinbarung, Brüssel Ia, Lugano-Bezug, Drittstaaten und Anti-suit-/lis-pendens-Risiken. |
| `default-judgment-and-nonappearance` | Prüft Versäumnis, Anerkenntnis, Säumnisfolgen, Einspruch und taktische Nichtteilnahme in Commercial-Court-Verfahren. |

## Arbeitsweg

Im Plugin Commercial Courts Deutschland gilt für **Cross Border Default Judgment**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `cross-border-jurisdiction-brussels-ia`

**Fokus:** Prüft internationale Zuständigkeit, Gerichtsstandsvereinbarung, Brüssel Ia, Lugano-Bezug, Drittstaaten und Anti-suit-/lis-pendens-Risiken.

# Cross-Border Jurisdiction

## Fachkern: Cross-Border Jurisdiction
- **Spezialgegenstand:** Cross-Border Jurisdiction. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
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
2. **Anwendungsbereich prüfen:** Brüssel Ia (VO Nr. 1215/2012) für EU-Beklagte mit Sitz in Mitgliedstaat (Art. 4 Brüssel Ia); Haager Übereinkommen über Gerichtsstandsvereinbarungen (HGÜ 2005) im Verhältnis zu UK seit 1.1.2021 sowie Singapur und Mexiko; Lugano-Übereinkommen (2007) im Verhältnis Schweiz, Norwegen, Island; in allen übrigen Fällen autonomes deutsches Recht (§§ 12 ff. ZPO i.V.m. §§ 38, 40 ZPO Gerichtsstandsvereinbarung).
3. **Gerichtsstandsvereinbarung Art. 25 Brüssel Ia:** Schriftform oder elektronische Aufzeichnung, eindeutige Bezeichnung des Gerichts; bei Verbrauchern, Versicherten oder Arbeitnehmern sind Vereinbarungen nur eingeschränkt möglich (Art. 15, 19, 23 Brüssel Ia). Bei nicht-ausschließlichen Klauseln aufpassen: Erstanrufung sichert Forum, sonst lis pendens-Regel Art. 29 Brüssel Ia (Italian Torpedo).
4. **Lis pendens und Anti-suit:** Art. 29 Brüssel Ia Erstanrufungsprinzip; bei ausschließlicher Gerichtsstandsvereinbarung Art. 31 Abs. 2 Brüssel Ia Vorrang des vereinbarten Gerichts. EuGH: Anti-suit-Injunctions gegen EU-Gerichte unzulässig (West Tankers-Doktrin); im Verhältnis zu Drittstaaten möglich, aber von deutschen Gerichten nicht anerkannt.
5. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären. Nächsten Schritt: Zuständigkeitsrüge § 39 ZPO oder positive Anrufung Commercial Court mit Forum-Klausel als Anlage; Vollstreckbarerklärung-Frage frühzeitig mitdenken (§§ 1110 ff. ZPO, Verordnungen).

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

## 2. `default-judgment-and-nonappearance`

**Fokus:** Prüft Versäumnis, Anerkenntnis, Säumnisfolgen, Einspruch und taktische Nichtteilnahme in Commercial-Court-Verfahren.

# Default and Nonappearance

## Fachkern: Default and Nonappearance
- **Spezialgegenstand:** Default and Nonappearance. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
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
2. **Säumnistatbestände (§§ 330-347 ZPO):** Säumnis des Klägers § 330 ZPO (Klageabweisung), Säumnis des Beklagten § 331 ZPO (Vorbringen des Klägers gilt als zugestanden, Versäumnisurteil bei Schlüssigkeit); Säumnis im schriftlichen Vorverfahren § 276 i.V.m. § 331 Abs. 3 ZPO. Bei Commercial Court mit englischer Sprache: Säumnisurteil kann in englischer Sprache ergehen, Vollstreckung im Ausland setzt aber deutschen Vollstreckungstitel voraus (Art. 53 Brüssel Ia Bescheinigung).
3. **Einspruch und Wiedereinsetzung (§§ 338-345, 233 ZPO):** Einspruchsfrist 2 Wochen ab Zustellung (§ 339 ZPO); Wiedereinsetzung in den vorigen Stand bei unverschuldeter Versäumung (§ 233 ZPO, Antrag binnen 2 Wochen ab Wegfall des Hindernisses). Bei zulässigem Einspruch wird das Verfahren in die Lage zurückversetzt, in der es vor der Säumnis war (§ 342 ZPO).
4. **Anerkenntnisurteil (§ 307 ZPO) und taktische Nichtteilnahme:** Anerkenntnis hat unmittelbar Urteilsfolge; Trade-off: schnelles, vollstreckbares Urteil ohne Kostenrisiko der Beweisaufnahme, aber materielle Kostenfolge je Tatbestand (§ 93 ZPO: bei sofortigem Anerkenntnis ohne Anlass zur Klage trägt der Kläger die Kosten). Taktische Säumnis (z.B. um Versäumnisurteil mit Einspruchsoption als Verzögerungsstrategie) wird von deutschen Gerichten zunehmend rechtsmissbräuchlich gewertet, Vorsicht bei Wiederholung.
5. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären. Nächsten Schritt: Säumnisantrag, Einspruchsfrist im Fristenbuch, Vollstreckungstitel zur Bescheinigung Art. 53 Brüssel Ia.

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
