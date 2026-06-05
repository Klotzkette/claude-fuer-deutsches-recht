---
name: interim-relief-issues-list
description: "Interim Relief Issues List: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Interim Relief Issues List

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Interim Relief Issues List** im Plugin Commercial Courts Deutschland. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `interim-relief-arrest-injunction` | Prüft einstweilige Verfügung, Arrest und interim relief im Commercial-Court-Umfeld, einschließlich Eilbedürftigkeit, Sicherheitsleistung und Vollziehung. |
| `issues-list-and-roadmap` | Formuliert eine Issues List für Commercial-Court-Verfahren: legal issues, factual issues, evidence issues, quantum, jurisdiction and language. |

## Arbeitsweg

Im Plugin Commercial Courts Deutschland gilt für **Interim Relief Issues List**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `interim-relief-arrest-injunction`

**Fokus:** Prüft einstweilige Verfügung, Arrest und interim relief im Commercial-Court-Umfeld, einschließlich Eilbedürftigkeit, Sicherheitsleistung und Vollziehung.

# Interim Relief

## Fachkern: Interim Relief
- **Spezialgegenstand:** Interim Relief. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
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

### Einstweiliger Rechtsschutz — Übersicht

| Maßnahme | Norm | Schutzobjekt | Voraussetzungen | Zuständig |
| --- | --- | --- | --- | --- |
| Arrest | § 916 ZPO | Geldforderung | Arrestanspruch + Arrestgrund (Vereitelungsgefahr) | LG/AG je nach Streitwert; bei Commercial Court Streit i.V.m. § 119b GVG |
| Einstweilige Verfügung — Sicherungsverfügung | § 935 ZPO | Anspruch außer Geld (Sicherung des Streitgegenstands) | Verfügungsanspruch + Verfügungsgrund | dito |
| Einstweilige Verfügung — Regelungsverfügung | § 940 ZPO | vorläufige Regelung eines Rechtsverhältnisses | Verfügungsanspruch + Verfügungsgrund | dito |
| Einstweilige Verfügung — Leistungsverfügung | gewohnheitsrechtlich (BGH ständige Rechtsprechung); § 935 ZPO analog | vorübergehende Befriedigung (z.B. Wettbewerbsverstoß) | strenge Anforderungen | dito |
| ARRest auf Patentstreit, Pre-Trial | § 916 ZPO i.V.m. ZPO Spezialnormen | Geldforderung | strenge Anforderungen Geheimhaltung | LG-Patentkammer |

### Verfügungsgrund / Eilbedürftigkeit

| Argument | Inhalt | Praxis |
| --- | --- | --- |
| Vermögenswerteflucht | Vermögensentzug, Verschiebung ins Ausland | bei Auslandsbezug stark |
| Drohende Verkaufshandlung | irreversibler Verlust des Schutzguts | typisch IP-Verletzung |
| Insolvenznähe der Gegenseite | Schutzbedürfnis vor anderen Gläubigern | Insolvenzantragspflicht § 15a InsO |
| Verstreichen einer Klage- oder Verjährungsfrist | Anspruch verfällt | für Eilbedürftigkeit relevant |
| Vorgreifliche Tatsachen | Beweismittel würden verloren gehen | § 485 ZPO selbständiges Beweisverfahren parallel |

### Trade-off und Praxistipp

- **Sicherheitsleistung § 921 ZPO:** Bei eV regelmäßig Sicherheitsleistung verlangt; Bürgschaft einer deutschen Großbank typisch (5-25 % der Forderungssumme).
- **Schadensersatzrisiko § 945 ZPO:** Bei nachträglicher Aufhebung der eV trägt Antragsteller verschuldensunabhängige Schadenshaftung. Daher: vorher gründlich prüfen.
- **Mündliche Verhandlung oder Beschluss:** Bei Antrag ohne mündliche Verhandlung schneller; Gegner kann jedoch Widerspruch nach § 924 ZPO einlegen, dann doch Verhandlung.
- **Internationale Wirkung:** Brüssel Ia-VO Art. 36 ermöglicht Anerkennung in EU. Für USA/Asien: dort eigenes Eilverfahren notwendig.
- **Vollziehungsfrist § 929 Abs. 2 ZPO:** Beschluss muss binnen einem Monat ab Erlass dem Gegner zugestellt sein, sonst Wirkungsverlust. KRITISCH bei Auslandsstoff (Haager Zustellungsübereinkommen, mehrere Wochen).

### Schutzschrift § 945a ZPO

Wer Eilanträge gegen sich erwartet (z.B. nach Abmahnung), kann eine Schutzschrift einreichen: Vorabverteidigung, die das Gericht vor Erlass des eV-Beschlusses berücksichtigen muss. Hinterlegt zentral beim Schutzschriftenregister.

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

## 2. `issues-list-and-roadmap`

**Fokus:** Formuliert eine Issues List für Commercial-Court-Verfahren: legal issues, factual issues, evidence issues, quantum, jurisdiction and language.

# Issues List

## Fachkern: Issues List
- **Spezialgegenstand:** Issues List. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
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
