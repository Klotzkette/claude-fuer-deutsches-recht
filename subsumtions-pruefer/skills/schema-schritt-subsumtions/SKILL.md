---
name: schema-schritt-subsumtions
description: "Schema Schritt Subsumtions: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Schema Schritt Subsumtions

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Schema Schritt Subsumtions** im Plugin Subsumtions-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-schema-verhandlung-vergleich-und-eskalation` | Schema: Verhandlung, Vergleich und Eskalation im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-schritt-schriftsatz-brief-und-memo-bausteine` | Schritt: Schriftsatz-, Brief- und Memo-Bausteine im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-subsumtions-tatbestand-beweis-und-belege` | Subsumtions: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Subsumtions-Prüfer gilt für **Schema Schritt Subsumtions**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-schema-verhandlung-vergleich-und-eskalation`

**Fokus:** Schema: Verhandlung, Vergleich und Eskalation im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Schema: Verhandlung, Vergleich und Eskalation

## Aufgabe

Dieser Skill strukturiert Verhandlung, Vergleich und Eskalation im Subsumtions-Workflow. Er gibt ein Schema für Vergleichsverhandlungen, die Prüfung eines gerichtlichen Vergleichs (§ 779 BGB, § 794 Abs. 1 Nr. 1 ZPO) und die Eskalationsleiter vom außergerichtlichen Schreiben bis zur Klage oder zum einstweiligen Rechtsschutz.

## Verhandlungs-Schema

### Phase 1 — Außergerichtliche Verhandlung

**Zielsetzung festlegen:**
- Was ist die Minimalforderung (BATNA: Best Alternative to No Agreement)?
- Was ist das Maximalziel (Anker)?
- Welche Zugeständnisse können ohne Präzedenzwirkung gemacht werden?

**Verhandlungsrahmen:**
- Form: schriftlich (Anwaltschreiben), mündlich (Gespräch), per Mediator
- Fristen: Antwortfrist setzen (z. B. 14 Tage); Fristen zur Wahrung von Ansprüchen nicht versäumen
- Verjährungshemmung durch Verhandlungen (§ 203 BGB): Wann beginnt, wann endet sie?

### Phase 2 — Mediationsklausel / ADR

- Mediationsklausel im Vertrag? → MediationsG (BGBl. 2012 I S. 1577)
- Schlichtungsstelle: Verbraucherschlichtungsstellen (VSBG), Ombudsmann Versicherungen, Banken
- Europäische Online-Streitbeilegung (ODR): ec.europa.eu/consumers/odr (bei Online-Verbraucherverträgen)

### Phase 3 — Vergleich abschließen

**Gerichtlicher Vergleich (§ 794 Abs. 1 Nr. 1 ZPO; § 779 BGB):**

Voraussetzungen des Vergleichs nach § 779 BGB:
- Gegenseitiges Nachgeben beider Parteien
- Streit oder Ungewissheit über Rechtsverhältnis
- Einigung über die streitige Frage

**Vollstreckbarkeit:** Gerichtlicher Vergleich ist Vollstreckungstitel (§ 794 Abs. 1 Nr. 1 ZPO); keine Urteilsvollstreckung nötig.

**Notarieller Vergleich / Vollstreckungsunterwerfung:** § 794 Abs. 1 Nr. 5 ZPO; sofortige Zwangsvollstreckung ohne Klage.

**Widerrufsrecht beim Vergleich:**
- § 312g BGB (Fernabsatz / außerhalb Geschäftsräume): Widerrufsrecht in 14 Tagen, wenn Vergleich außerhalb Geschäftsräumen geschlossen
- Anwaltsvergleich: §§ 796a ff. ZPO; nach Abschluss für vollstreckbar erklärbar

### Phase 4 — Eskalation

**Eskalationsleiter:**

1. **Mahnung / Aufforderungsschreiben** (§ 286 Abs. 1 BGB für Verzugseintritt)
2. **Abmahnung** (Wettbewerbs-, Urheber-, Markenrecht; § 13 UWG; UrhG)
3. **Anwaltliches Schreiben** mit Fristsetzung und Klageandrohung
4. **Einstweilige Verfügung** (§§ 935/940 ZPO) bei Dringlichkeit und Eilbedürftigkeit
5. **Mahnverfahren** (§§ 688 ff. ZPO) bei unbestrittenen Geldforderungen
6. **Klage** (§§ 253 ff. ZPO)
7. **Pfändung** nach Urteil (§§ 803 ff. ZPO)

## Vergleichsrechnung

Entscheidungsbaum: Lohnt sich der Rechtsstreit?

```
Klageforderung: EUR X
Prozesskostenrisiko: EUR Y (RVG-Gebühren beider Seiten + Gerichtskosten)
Erfolgswahrscheinlichkeit: p (%)
Erwarteter Wert Klage: X × p - Y × (1-p)
Vergleichsangebot: EUR Z
Entscheidung: Vergleich wenn Z > Erwarteter Wert Klage
```

## Einstieg

Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. In welcher Phase befindet sich der Sachverhalt (außergerichtlich, Verhandlung, Klage)?
2. Was ist das Minimalziel und das Maximalziel der fragenden Partei?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Entwürfe, Schreiben oder Angebote belegen den Stand?
5. Welcher Output wird gebraucht: Verhandlungsschreiben, Vergleichsentwurf, Eskalationsplan, Memo?

## Arbeitsworkflow

1. **Fallbild bilden:** Phase, Parteien, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen für Vergleich, Vollstreckbarkeit, Verjährungshemmung und Eskalation prüfen.
3. **Prüfpunkte abarbeiten:** Verhandlungsposition, Risiken, Gegenargumente und Alternativwege trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen und Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills vorschlagen.

## Output-Standard

- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Verhandlungsmatrix:** Position, Zugeständnis, Untergrenze, Risiko, nächster Schritt.
- **Arbeitsprodukt:** Vergleichsentwurf, Verhandlungsschreiben oder Eskalationsplan.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf markieren.

## Quellenregel

- Normen live prüfen: gesetze-im-internet.de (BGB §§ 779, 203, 286; ZPO §§ 688 ff., 794, 935, 940; UWG § 13; MediationsG).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine Blindzitate. Paywall-Literatur nur mit Nutzerquelle.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `spezial-schritt-schriftsatz-brief-und-memo-bausteine`

**Fokus:** Schritt: Schriftsatz-, Brief- und Memo-Bausteine im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Schriftsatz-, Brief- und Memo-Bausteine

## Aufgabe

Dieser Skill erzeugt sofort verwendbare Bausteine für Schriftsätze, Mandantenbriefe und interne Memos. Er stellt sicher, dass alle Bausteine subsumtionsfest sind: Obersatz, Definition, Subsumtion und Ergebnis sind klar getrennt; Quellen sind entweder live verifiziert oder als Prüfpunkte markiert.

## Baustein 1 — Anspruchseinleitung (Klage / Schriftsatz)

**Muster:**
```
[Kläger] macht gegen [Beklagten] einen Anspruch auf [Leistung] aus § [Norm] geltend.

Sachverhalt: [knappe Tatsachendarstellung; jede Tatsache mit Anlage belegen]

Rechtliche Würdigung:
1. [Tatbestandsmerkmal 1]: [Definition + Subsumtion + Zwischenergebnis]
2. [Tatbestandsmerkmal 2]: [Definition + Subsumtion + Zwischenergebnis]
[...]

Ergebnis: Der Anspruch ist begründet / nicht begründet, weil [Zusammenfassung].
```

## Baustein 2 — Einredeblock (Klageerwiderung / Verteidigungsschriftsatz)

**Muster:**
```
Die Klage ist abzuweisen. [Beklagter] erhebt folgende Einreden und Einwendungen:

1. [Einrede Verjährung]: Die Forderung ist gemäß §§ 195, 199 BGB verjährt. Fristbeginn: [Datum].
 Frist: 3 Jahre; Ablauf: [Datum]. Verjährung nicht gehemmt, weil [Begründung].

2. [Einrede § 320 BGB]: [Beklagter] verweigert Leistung, bis [Kläger] [Gegenleistung] erbringt (Zug-um-Zug).

3. [Einwendung Nichtigkeit § 134 BGB]: Der Vertrag ist nichtig, weil [Norm/Sachverhalt].
```

## Baustein 3 — Mandantenbrief (Alltagssprache)

**Muster:**
```
Betreff: Ihre Angelegenheit [Kurzbeschreibung]

Sehr geehrte/r [Mandant],

ich habe Ihre Unterlagen geprüft. Ergebnis: [klare Aussage in 2–3 Sätzen].

Was das für Sie bedeutet: [konkrete Handlungsaufforderung].

Was Sie jetzt tun sollten: [nummerierte Liste mit Fristen].

Ich stehe für Rückfragen zur Verfügung.

Wichtiger Hinweis: Dieses Schreiben ist kein abschließender Rechtsrat ...
```

## Baustein 4 — Internes Memo (juristisches Gutachten-Kurzformat)

**Struktur:**
```
MEMO
An: [Empfänger] Von: [Autor] Datum: [TT.MM.JJJJ]
Betr.: [Kurzbezeichnung]

KURZLAGE:
[2–3 Sätze: Sachverhalt, Kernfrage, Ergebnis]

PRÜFUNG:
1. [Norm]: [Definition] → [Subsumtion] → [Zwischenergebnis]
2. [Weitere TBM] ...

ERGEBNIS:
[Klarer Satz; Risikoampel; offene Punkte]

NÄCHSTE SCHRITTE:
[Sofortmaßnahme + Frist + Zuständigkeit]

QUELLEN:
[Nur live verifiziertere Quellen oder Prüfpunkte; keine Blindzitate]
```

## Baustein 5 — Beweisangebot (Schriftsatz)

**Muster:**
```
Beweis: [Tatsachenbehauptung]

Beweismittel:
- Zeuge [Name, Anschrift] (§§ 373 ff. ZPO)
- Urkunde [Anlage K-Nr.] (§§ 415 ff. ZPO)
- Sachverständigengutachten zu [Beweisfrage] (§§ 402 ff. ZPO)

Hinweis: Beweislast liegt beim [Kläger/Beklagten] gemäß [Grundregel / Umkehr].
```

## Formale Mindestanforderungen Schriftsatz (§ 253 ZPO)

- Rubrum (Bezeichnung der Parteien und Prozessbevollmächtigten)
- Bestimmter Antrag (§ 253 Abs. 2 Nr. 2 ZPO): was genau? wie viel? bis wann?
- Sachverhaltsschilderung mit Belegen (Anlagen)
- Rechtliche Begründung (Anspruchsgrundlage, Subsumtion)
- Beweisangebote für streitige Tatsachen
- Unterschrift / qualifizierte elektronische Signatur (§ 130a ZPO bei elektronischer Übermittlung)

## Einstieg

Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welcher Baustein wird gebraucht (Schriftsatz, Brief, Memo)?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welche Tonalität: formal-juristisch (Gericht) oder verständlich (Mandant)?

## Arbeitsworkflow

1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Baustein auswählen:** Schriftsatz, Brief, Memo, Beweisangebot oder gemischtes Dokument.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, Gegenargumente trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen und Alternativwegen.
5. **Anschluss bauen:** Passende weitere Skills vorschlagen.

## Output-Standard

- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** vollständiger Baustein in der gewählten Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf markieren.

## Quellenregel

- Normen live prüfen: gesetze-im-internet.de (ZPO §§ 130a, 253, 373 ff., 402 ff., 415 ff.; BGB §§ 195, 320, 387 ff.).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine Blindzitate. Paywall-Literatur nur mit Nutzerquelle.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `spezial-subsumtions-tatbestand-beweis-und-belege`

**Fokus:** Subsumtions: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Subsumtion: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Aufgabe

Dieser Skill führt den vollständigen Subsumtions-Durchgang durch: Tatbestandsmerkmale identifizieren, Beweisfragen zuordnen und Beleglage prüfen. Er integriert das Vier-Schritt-Schema (Obersatz, Definition, Subsumtion, Ergebnis) mit der Beweislastverteilung und der Dokumentenprüfung.

## Vier-Schritt-Schema

**Schritt 1 — Obersatz**
- Formulierung im Konjunktiv: "A könnte gegen B einen Anspruch auf X aus § Y haben."
- Enthält: Anspruchsteller, Anspruchsgegner, Anspruchsinhalt, Anspruchsgrundlage
- Anti-Muster: "A hat einen Anspruch" (Indikativ im Obersatz = Urteilsstil-Fehler)

**Schritt 2 — Definition**
- Jedes streitige Tatbestandsmerkmal mit einer abstrakt-allgemeinen Definition belegen
- Quelle: BGH-Linie (live zu prüfen), h.M. in der Literatur (nur mit Nutzerquelle), Legaldefinition im Gesetz
- Anti-Muster: Definition stammt aus dem Sachverhalt selbst (Zirkelschluss)

**Schritt 3 — Subsumtion**
- Konkrete Tatsachen aus dem Sachverhalt werden unter die abstrakte Definition gehalten
- Jede Tatsachenbehauptung mit Beleg (Anlage, Zeuge, Urkunde) versehen
- Anti-Muster: Definition wird wiederholt statt Tatsachen unter sie subsumiert

**Schritt 4 — Ergebnis**
- Zwischenergebnis je Tatbestandsmerkmal im Indikativ
- Gesamtergebnis im Indikativ: "Die Voraussetzungen des § Y liegen vor / nicht vor."

## Beweisfragen-Matrix

| Tatbestandsmerkmal | Definition (Quelle) | Tatsache aus Sachverhalt | Beleg | Beweislast | Beweismittel |
|---|---|---|---|---|---|
| TBM 1 | [...] | [...] | Anlage K1 | Kläger | Urkunde § 415 ZPO |
| TBM 2 | [...] | [...] | Zeuge Müller | Kläger | Zeuge §§ 373 ff. ZPO |
| TBM 3 (Einrede) | [...] | [...] | fehlend | Beklagter | SV-Gutachten §§ 402 ff. ZPO |

## Beleglage-Check

Für jede Tatsachenbehauptung im Schriftsatz oder Gutachten:

1. **Liegt ein Beleg vor?** (Urkunde, Zeuge, Sachverständigengutachten, Augenschein)
2. **Ist der Beleg ausreichend?** (Echtheit, Inhalt, Relevanz für das TBM)
3. **Ist die Beweislast korrekt?** (Grundregel: wer Tatsache behauptet, trägt Beweislast)
4. **Gibt es Beweislastumkehr?** (§ 630h BGB Arzthaftung; § 22 AGG Diskriminierung; Art. 82 Abs. 3 DSGVO)
5. **Ist Anscheinsbeweis möglich?** (§ 286 ZPO + Erfahrungssatz)
6. **Fehlender Beleg:** Sekundäre Darlegungslast der Gegenseite prüfen

## Typische Subsumtionsfehler

| Fehlertyp | Beschreibung | Heilung |
|---|---|---|
| Sprung-Subsumtion | Tatsache direkt unter Norm ohne Definition | Definition mit Quelle einsetzen |
| Zirkelschluss | Definition stammt aus dem Sachverhalt | Definition aus externer Quelle |
| Scheinsubsumtion | Definition wiederholt; keine konkreten Tatsachen | Tatsachen aus Akte zitieren |
| Fehlendes Zwischenergebnis | Merkmal offen gelassen | Klares Ja/Nein mit Begründung |
| Konjunktiv im Schluss | "könnte vorliegen" | Indikativ: "liegt vor" |

## Einstieg

Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Norm und welches Tatbestandsmerkmal soll geprüft werden?
2. Welche Tatsachen sind unstreitig, welche streitig?
3. Welche Belege liegen vor (Anlagen, Zeugen, Gutachten)?
4. Wer trägt die Beweislast (Grundregel oder Umkehr)?
5. Welcher Output wird gebraucht: Prüfmatrix, Schriftsatzbaustein, Klausurgutachten?

## Arbeitsworkflow

1. **Fallbild bilden:** Norm, Parteien, Tatbestandsmerkmale, Beleglage und offene Beweisfragen.
2. **Vier-Schritt-Schema anwenden:** Obersatz → Definition → Subsumtion → Ergebnis je TBM.
3. **Beweisfragen-Matrix füllen:** Pro TBM: Tatsache, Beleg, Beweislast, Beweismittel.
4. **Risiko bewerten:** Grün/Gelb/Rot je TBM; offene Beweisfragen als Prüfpunkte.
5. **Anschluss bauen:** Passende weitere Skills vorschlagen.

## Output-Standard

- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Beweisfragen-Matrix:** TBM, Definition, Tatsache, Beleg, Beweislast, Beweismittel.
- **Arbeitsprodukt:** Vier-Schritt-Subsumtion je TBM mit Zwischenergebnis.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf markieren.

## Quellenregel

- Normen live prüfen: gesetze-im-internet.de (ZPO §§ 286, 294, 373 ff., 402 ff., 415 ff.; BGB §§ 630h; AGG § 22).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle (dejure.org, bgh.de).
- Keine Blindzitate. Paywall-Literatur nur mit Nutzerquelle.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
