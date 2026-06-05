---
name: waehlen-rechtsprechung-recherche-europarecht
description: "Waehlen Rechtsprechung Recherche Europarecht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Waehlen Rechtsprechung Recherche Europarecht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Waehlen Rechtsprechung Recherche Europarecht** im Plugin Subsumtions-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-output-waehlen` | Output wählen im Plugin subsumtions-pruefer: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `rechtsprechung-recherche-strategie` | Gibt eine Strategie für die Rechtsprechungsrecherche: wann systeminternes Wissen genuegt, wann Web-Suche bei BVerfG/BGH/BAG/BSG/BVerwG/OLG/EuGH noetig ist. Nennt Fundstellen: curia.europa.eu, dejure.org, openjur, rechtsprechung-im-internet, bundesgerichtshof.de. |
| `spezial-europarecht-fristen-form-und-zustaendigkeit` | Europarecht: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Subsumtions-Prüfer gilt für **Waehlen Rechtsprechung Recherche Europarecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-output-waehlen`

**Fokus:** Output wählen im Plugin subsumtions-pruefer: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung.

# Output wählen

## Aufgabe

Dieser Prüffeld wählt den richtigen Output-Typ für die Arbeitsaufgabe. Er unterscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline und Mandantenübersetzung und gibt Stil- und Formatierungsanweisungen.

## Output-Typen und wann sie passen

| Output-Typ | Wann | Ton | Struktur |
|---|---|---|---|
| Klausurgutachten | Klausur, Hausarbeit, Lernmaterial | Gutachtenstil (Konjunktiv im Obersatz) | Vier-Schritt je TBM; Zwischenergebnis |
| Kurzgutachten / Memo | Interne Prüfung; erste Einschätzung | Sachlich, juristisch | Kurzlage, Prüfpfad, Ergebnis, offene Punkte |
| Klageschrift / Schriftsatz | Einreichung beim Gericht | Urteilsstil (Ergebnis zuerst) | Rubrum, Antrag, Begründung, Beweisangebote |
| Mandantenbrief | Kommunikation mit Mandant | Alltagssprache (→ output-alltagssprache-de) | Kurzzusammenfassung, Handlungsaufforderung, Hinweis |
| Subsumtionstabelle | Mehrere TBM oder mehrere Parteien | Tabellarisch | TBM, Definition, Tatsache, Subsumtion, Ergebnis |
| Checkliste | Vorbereitung, Intake, Mandatsziel | Knappe Aufzählung | Abhakbar; Fristen; Zuständigkeiten |
| Vermerk / Aktenvermerk | Interne Dokumentation | Sachlich, komprimiert | Datum, Sachverhalt, Prüfung, Ergebnis, nächste Schritte |
| Redline / Änderungsmarkierung | Vertragsprüfung, Entwurfsüberarbeitung | Kommentar-Ton | Track-Changes-Stil; Begründung je Änderung |
| Fremdsprachig | Internationale Mandanten | Englisch / Französisch | → output-fremdsprachig-en-fr |

## Entscheidungsbaum Output-Wahl

```
Wer liest den Output?
├─ Gericht → Schriftsatz (Urteilsstil; § 253 ZPO-Konformität)
├─ Mandant ohne Jurastudium → Mandantenbrief (Alltagssprache)
├─ Anwalt intern → Memo oder Vermerk (Gutachtenstil kurz)
├─ Klausurbetreuer → Gutachten (Vollgutachtenstil)
├─ Mehrere TBM / Parteien → Tabelle
└─ Checkliste für Intake/Routing → Checkliste
```

## Subsumtion — Output-Stil-Regeln

**Voller Gutachtenstil:**
- Memo, Hausarbeit, Klausur, gerichtliches Gutachten.
- Vier-Schritt-Schema (Obersatz, Definition, Subsumtion, Ergebnis) pro TBM.
- Konjunktiv im Obersatz; Indikativ in Subsumtion und Zwischenergebnis.

**Urteilsstil (Kurzgutachten / Schriftsatz):**
- Deduktiver Stil: "Die Klage ist begründet, weil ..."
- Kein Konjunktiv im Einstieg.
- Begründung folgt, nicht vorangehend.

**Subsumtionstabelle:**
- Mehrstöckige Anspruchsgrundlagen oder mehrere Anspruchsteller/-gegner.
- Spalten: TBM, Definition, Tatsache, Subsumtion, Ergebnis.

**Anti-Pattern:**
- "Hier liegt ein Vertrag vor, weil die Parteien einen Vertrag geschlossen haben" → Zirkelschluss.
- Statt dessen: "Hier liegt ein Vertrag iSd § 145 BGB vor, weil A am TT.MM.JJJJ ein Angebot iSd § 145 BGB abgegeben hat (Tatsachen) und B am TT.MM.JJJJ durch Erklärung Y angenommen hat (§ 147 BGB)."

## Einstieg

Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow

1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Output-Typ anhand der Entscheidungsmatrix bestimmen.
3. Stil- und Strukturanweisungen für den gewählten Output-Typ anwenden.
4. Passende Fachmodule vorschlagen.
5. Ein sofort nutzbares Ergebnis erzeugen.

## Output-Standard

- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Output-Typ-Empfehlung mit Begründung.
- Fertiger Entwurf im gewählten Format.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.

## Quellenregel

- Normen live prüfen: gesetze-im-internet.de.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine Blindzitate. Paywall-Literatur nur mit Nutzerquelle.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
- Im Memo-Format immer Zwischenergebnis je Tatbestandsmerkmal — leichter zu prüfen und besser zu lesen.

## 2. `rechtsprechung-recherche-strategie`

**Fokus:** Gibt eine Strategie für die Rechtsprechungsrecherche: wann systeminternes Wissen genuegt, wann Web-Suche bei BVerfG/BGH/BAG/BSG/BVerwG/OLG/EuGH noetig ist. Nennt Fundstellen: curia.europa.eu, dejure.org, openjur, rechtsprechung-im-internet, bundesgerichtshof.de.

# Rechtsprechung-Recherche-Strategie

## Zweck

Subsumtion ohne Rechtsprechung ist unvollständig. Dieser Skill vermittelt, wie und wo Rechtsprechung zu einer geprüften Norm recherchiert werden sollte. Er unterscheidet, wann das Wissen des Systems ausreichend ist und wann eine eigenständige Webrecherche unbedingt empfohlen wird. Grundregel: Keine Entscheidung aus Modellwissen zitieren ohne Live-Verifikation.

## Triage: Wann Live-Recherche zwingend?

1. Enthält das Ergebnis ein konkretes Aktenzeichen oder Datum? → immer live prüfen
2. Liegt die Entscheidung nach dem Wissensende des Systems? → immer live prüfen
3. Divergierende Rechtsprechung zwischen OLG-Bezirken? → live prüfen
4. Frische EuGH-Rechtsprechung (Vorabentscheidungen)? → curia.europa.eu
5. Bundesgerichtliche Grundsatzentscheidung älter als 3 Jahre? → kann mit Einschränkungen aus Systemwissen benannt, aber muss verifiziert werden

## Fundstellen nach Gericht

| Gericht | Kostenlose Fundstelle | Suchfunktion | Besonderheit |
|---------|----------------------|--------------|--------------|
| BGH | bgh.de / dejure.org / openjur.de | Aktenzeichen, Stichwort, Norm | Volltext; dejure.org mit Querverweisen zu Kommentaren |
| BVerfG | bverfg.de | Suchmaske; BVerfGE-Band | Volltext; leitsätze frei |
| BAG | bag.bund.de / dejure.org | Aktenzeichen, Stichwort | Nicht alle Entscheidungen veröffentlicht |
| BVerwG | bverwg.de | Aktenzeichen | Volltext für ausgewählte Entscheidungen |
| BSG | bsg.bund.de | Aktenzeichen | Volltext für ausgewählte Entscheidungen |
| BFH | bundesfinanzhof.de | Stichwort, Datum | Volltext; BFHE-Verweise |
| OLG / LG | openjur.de / dejure.org (je nach Land) | Gericht, Aktenzeichen, Norm | Nicht alle Urteile veröffentlicht |
| EuGH / EuG | curia.europa.eu | Rechtssache, Datum, Norm | Volltext in allen Amtssprachen; ECLI-Nummern |

## Recherchestrategie

### Schritt 1 — Norm identifizieren
Welche Norm soll durch Rechtsprechung ausgefüllt werden? Genaue Normbezeichnung (§, Absatz, Satz, Nummer) für die Suche verwenden.

### Schritt 2 — Gericht und Instanz bestimmen
BGH-Entscheidungen haben grundsätzlich Vorrang; OLG-Rechtsprechung nur relevant, wenn BGH-Rechtsprechung fehlt oder divergiert. Bei EU-Bezug immer EuGH prüfen.

### Schritt 3 — Suchbegriffe wählen
- Norm + Tatbestandsmerkmal (z. B. "§ 280 BGB Pflichtverletzung Unterlassen")
- Obersatz-Schlagwort (z. B. "Anscheinsbeweis Auffahrunfall BGH")
- Negativabgrenzung: "Wann greift X NICHT?"

### Schritt 4 — Entscheidung prüfen
- Datum: Ist die Entscheidung aktuell? Zwischenzeitlich aufgegeben?
- Tragender Rechtssatz vs. Obiter dictum: Nur tragender Rechtssatz bindet
- Instanz: BGH-Grundsatz vs. OLG-Abweichung dokumentieren

### Schritt 5 — Zitierweise
- Gericht + Entscheidungsform + Datum + Aktenzeichen + Fundstelle
- Beispiel: BGH, Urteil v. TT.MM.JJJJ, Az. X ZR 123/45, dejure.org [Prüfpunkt: live verifiziert?]

## Wann reicht das Systemwissen?

Das System kann Leitentscheidungen nennen als **Prüfpunkte**, nicht als Zitate, bei:
- Grundlegenden EuGH-Leitentscheidungen (Costa/ENEL, Simmenthal, Francovich, CILFIT — live zu prüfen unter curia.europa.eu)
- BVerfG-Grundsatzurteilen (Lüth, Apothekenurteil, Solange I und II — live zu prüfen unter bverfg.de)
- BGH-Grundsatzlinien zu bekannten Rechtsgebieten

**Immer:** Das System weist auf sein Wissensende-Datum hin und empfiehlt manuelle Überprüfung, wenn Entscheidungen neuer als 12–18 Monate sein könnten.

## Zitierverbot

- Keine BeckRS-, juris-Nummern aus Modellwissen zitieren
- Keine Randnummern aus Kommentaren, die nicht live geprüft wurden
- Keine NJW-Fundstellen ohne Verifikation in dejure.org oder Originalheft

## Ausgabe

Recherche-Protokoll: Norm → Such-Strategie → Gefundene Entscheidungen (mit Live-Prüfvermerk) → Tragender Rechtssatz → Relevanz für die konkrete Subsumtion.

---

Hinweis: Keine Rechtsberatung. Systemwissen ersetzt keine Live-Recherche.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
- Normtext live prüfen: gesetze-im-internet.de (Bund), eur-lex.europa.eu (EU), dejure.org (Querverweise).

## 3. `spezial-europarecht-fristen-form-und-zustaendigkeit`

**Fokus:** Europarecht: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Europarecht: Fristen, Form, Zuständigkeit und Rechtsweg

## Aufgabe

Dieser Skill prüft die verfahrensrechtlichen Dimensionen europarechtlicher Sachverhalte: Fristen vor EU-Gerichten und deutschen Gerichten bei EU-Bezug, Formvorschriften, sachliche und örtliche Zuständigkeit und den richtigen Rechtsweg.

## Zuständigkeit im EU-Rechtsrahmen

### Sachliche Zuständigkeit: EU-Gerichte vs. nationale Gerichte

| Streitgegenstand | Zuständiges Gericht |
|---|---|
| Klage gegen EU-Organ (Nichtigkeitsklage) | EuGH / EuG (Art. 263 AEUV) |
| Vorabentscheidung (Auslegungsfrage) | EuGH auf Vorlage nationaler Gerichte (Art. 267 AEUV) |
| Vertragsverletzungsverfahren gegen Mitgliedstaat | EuGH (Art. 258–260 AEUV) |
| Privatrechtliche Streitigkeit mit EU-Bezug | Nationale Gerichte (EuGVVO VO 1215/2012) |
| Arbeitnehmerrechte, DSGVO-Durchsetzung | Nationale Gerichte; Aufsichtsbehörden |

### Örtliche Zuständigkeit: EuGVVO (VO 1215/2012)

- **Allgemeiner Gerichtsstand:** Wohnsitz des Beklagten (Art. 4 EuGVVO)
- **Besonderer Gerichtsstand Vertrag:** Erfüllungsort (Art. 7 Nr. 1 EuGVVO); bei Kauf: Lieferort; bei Dienstleistung: Erbringungsort
- **Besonderer Gerichtsstand Delikt:** Schadensort (Art. 7 Nr. 2 EuGVVO); EuGH: Handlungs- oder Erfolgsort
- **Verbrauchergerichtsstand:** Art. 17–19 EuGVVO; Verbraucher kann am Wohnsitz klagen
- **Ausschließliche Zuständigkeit:** Grundstücke (Art. 24 Nr. 1), Gesellschaften (Art. 24 Nr. 2), Handelsregister (Art. 24 Nr. 3)

## Fristen im EU-Rechtsrahmen

### Vor dem EuGH (Verfahrensordnung EuGH)

| Verfahren | Frist | Grundlage |
|---|---|---|
| Nichtigkeitsklage | 2 Monate ab Bekanntgabe (Art. 263 Abs. 6 AEUV) | Ausschlussfrist |
| Untätigkeitsklage | 2 Monate nach Aufforderung und fehlendem Handeln (Art. 265 AEUV) | Ausschlussfrist |
| Schadenersatzklage | 5 Jahre (Art. 46 EuGH-Satzung) | Verjährung |
| Vorabentscheidung | Keine Frist; Dauer ca. 15–24 Monate | Verfahrensdauer |

### Deutsche Gerichte bei EU-Bezug

- DSGVO-Klage (Art. 79 DSGVO): Nationale Verjährungsfristen gelten (§§ 195 ff. BGB); Frist beginnt mit Kenntnis
- EuGVVO-Klage: Zustellung nach EuZVO (VO 1393/2007) beachten; Fristbeginn ab ordnungsgemäßer Zustellung
- Bußgeld nach EU-Wettbewerbsrecht: Verjährungsfrist nach Art. 25 VO 1/2003 (5 Jahre für Verstöße)

## Formvorschriften

### Klageschrift vor EuGH/EuG
- Einreichung über das e-Curia-System (curia.europa.eu)
- Anwaltszwang (Art. 19 EuGH-Satzung) außer bei Mitgliedstaaten und EU-Institutionen
- Sprache: beliebige EU-Amtssprache (Verfahrenssprache muss gewählt werden)

### Vorabentscheidungsersuchen durch nationales Gericht
- Kein Formzwang, aber Empfehlung der ausführlichen Begründung (EuGH-Leitlinien für nationale Gerichte)
- Elektronische Einreichung empfohlen; postalisch möglich
- Aussetzung des Ausgangsverfahrens § 148 ZPO analog oder spezieller Aussetzungsgrund

## Einstieg

Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow

1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** EU-Zuständigkeit, Fristen, Formfragen und Verfahrensstand prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills vorschlagen (z. B. eu-vorabentscheidung-pruefen, de-eu-recht-abgrenzung).

## Output-Standard

- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel

- Aktuelle Normen, EU-Rechtsakte, Behördenhinweise und Gerichtsseiten live prüfen (eur-lex.europa.eu, curia.europa.eu, gesetze-im-internet.de).
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn der Nutzer den Volltext bereitstellt.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe absichern.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
