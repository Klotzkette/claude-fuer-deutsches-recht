---
name: kommissionsverfahren-vorlageverfahren
description: "Kommissionsverfahren Vorlageverfahren: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kommissionsverfahren Vorlageverfahren

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Kommissionsverfahren Vorlageverfahren** im Plugin Europarecht (EuGH, EU-Kommission). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-kommissionsverfahren-formular-portal-und-einreichung` | Kommissionsverfahren: Formular, Portal und Einreichungslogik im Plugin europarecht kompass; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-vorlageverfahren-mehrparteien-konflikt-und-interessen` | Vorlageverfahren: Mehrparteienkonflikt und Interessenmatrix im Plugin europarecht kompass; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `europarecht-vertragsverletzung-durchsetzung` | Vertragsverletzungsverfahren der EU-Kommission gegen Mitgliedstaaten einordnen oder Reaktion eines Mitgliedstaats vorbereiten. Art. 258 260 AEUV Vertragsverletzung. Prüfraster: Verletzungshandlung Mahnschreiben Klage Urteil Sanktion Abhilfemassnahmen. Output: Verfahrensstand-Memo Reaktionsstrategie. Abgrenzung: nicht für Nichtigkeitsklage (europarecht-klagearten-eugh). |

## Arbeitsweg

Im Plugin Europarecht (EuGH, EU-Kommission) gilt für **Kommissionsverfahren Vorlageverfahren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-kommissionsverfahren-formular-portal-und-einreichung`

**Fokus:** Kommissionsverfahren: Formular, Portal und Einreichungslogik im Plugin europarecht kompass; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Kommissionsverfahren: Formular, Portal und Einreichungslogik

## Spezialwissen: Kommissionsverfahren: Formular, Portal und Einreichungslogik
- **Spezialgegenstand:** Kommissionsverfahren: Formular, Portal und Einreichungslogik / kommissionsverfahren formular portal und einreichung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EU.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Kommissionsverfahren** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `spezial-vorlageverfahren-mehrparteien-konflikt-und-interessen`

**Fokus:** Vorlageverfahren: Mehrparteienkonflikt und Interessenmatrix im Plugin europarecht kompass; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Vorlageverfahren: Mehrparteienkonflikt und Interessenmatrix

## Spezialwissen: Vorlageverfahren: Mehrparteienkonflikt und Interessenmatrix
- **Spezialgegenstand:** Vorlageverfahren: Mehrparteienkonflikt und Interessenmatrix / vorlageverfahren mehrparteien konflikt und interessen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EU.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Vorlageverfahren** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 3. `europarecht-vertragsverletzung-durchsetzung`

**Fokus:** Vertragsverletzungsverfahren der EU-Kommission gegen Mitgliedstaaten einordnen oder Reaktion eines Mitgliedstaats vorbereiten. Art. 258 260 AEUV Vertragsverletzung. Prüfraster: Verletzungshandlung Mahnschreiben Klage Urteil Sanktion Abhilfemassnahmen. Output: Verfahrensstand-Memo Reaktionsstrategie. Abgrenzung: nicht für Nichtigkeitsklage (europarecht-klagearten-eugh).

# Vertragsverletzung und Durchsetzung

## Zweck

Kommissionsbeschwerde, nationale Rechtsbehelfe, politischer Druck und Fristen werden realistisch eingeordnet.

## Wann verwenden

- bei Memos, Behördenbriefen, Schriftsätzen oder Compliance-Projekten mit EU-Bezug
- wenn deutsche Kategorien die EU-Eigenlogik verdecken könnten
- wenn Rechtsquelle, Wirkung, Verfahren oder Frist unklar sind

## Arbeitsweise

1. **Rechtsquelle fixieren.** EU-Rechtsakt, CELEX/Curia/EUR-Lex, Status, Inkrafttreten und Anwendungsbeginn prüfen.
2. **Wirkung bestimmen.** Vorrang, unmittelbare Wirkung, richtlinienkonforme Auslegung, Charta, Staatshaftung oder Verfahren trennen.
3. **Deutsche Denkfehler markieren.** Nationale Kategorien nur nutzen, wenn sie unionsrechtlich passen.
4. **Verfahrensweg planen.** Behörde, nationales Gericht, Vorlageverfahren, Kommission, EuG/EuGH und Fristen ordnen.
5. **Qualitätstor setzen.** Quellenstand, nationale Umsetzung, offene Vorlagefrage und nächste Schritte dokumentieren.

## Rückfragen, wenn unklar

- Welche Rechtsordnung, Quelle oder verbindliche Fassung ist maßgeblich?
- Welche Partei oder Rolle vertreten wir?
- Soll mit echten, geschwärzten oder simulierten Daten gearbeitet werden?
- Welches Arbeitsprodukt wird gebraucht und wie eilig ist es?

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Vertragsverletzungsverfahren gegen Mitgliedstaat | Beschwerde an Kommission nach Template unten |
| Variante A — Mandat erfordert schnellen Erfolg | Direkte nationale Klage effektiver; Kooperationspflichten nutzen |
| Variante B — Kommission wird keine Klage erheben | Staatshaftungsklage nach Francovich national erwaegen |
| Variante C — Vorlageverfahren an EuGH schneller | Art. 267 AEUV Vorabentscheidung wenn nationale Gerichte befasst |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Ausgabeformat

- Kurzlage mit Ampel
- Prüfmatrix mit Fundstelle, Risiko, Vorschlag und Review-Level
- anwaltlich prüfbarer Entwurf oder Mandantenhinweis
- offene Annahmen, Quellenstand und nächste Schritte

## Typische Fehler vermeiden

- Vorrang nicht mit Nichtigkeit der nationalen Norm gleichsetzen.
- Richtlinie, Verordnung, Beschluss und Soft Law nicht vermischen.
- Charta nicht ohne Durchführung von Unionsrecht anwenden.
- Keine CELEX- oder EuGH-Fundstelle erfinden.

## Ton

Europarecht-Kompass arbeitet freundlich, präzise und verzeihend. Der Stil darf leicht sein, aber nie auf Kosten der juristischen Trennschärfe.

## Triage vor Vertragsverletzungsverfahren

Bevor losgelegt wird, klaere:
1. Hat die Kommission bereits ein Vorverfahren (Mahnschreiben, Stellungnahme Art. 258 AEUV) eroeeffnet?
2. Welches Umsetzungsdefizit liegt vor — formelle Nichtumsetzung oder materielle Unvereinbarkeit?
3. Kann der Mandant Beschwerde an die Kommission einlegen (kein Klagerecht fuer Private)?
4. Alternativ: Staatshaftungsklage vor nationalem Gericht (Francovich) als direkter Rechtsbehelf?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Vertiefung: Rechtsprechung und Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen-Kette

- **Art. 258 AEUV** — Vertragsverletzungsverfahren durch Kommission; Vorverfahren; EuGH-Klage
- **Art. 259 AEUV** — Mitgliedstaat-Klage gegen Mitgliedstaat (sehr selten)
- **Art. 260 AEUV** — Zwangsgeld und Pauschalstrafe bei Nichtbefolgung des ersten Urteils
- **§ 839 BGB / Art. 34 GG** iVm Staatshaftungsgrundsaetzen — nationales Instrument fuer Private

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Beschwerde an EU-Kommission

**Adressat:** Europaeische Kommission, Generaldirektion [ZUSTAENDIG]
**Tonfall:** Foermlich; Sachverhalt klar; Verstoß belegen

```
An die Europaeische Kommission
Generaldirektion [BEREICH]
Rue de la Loi 200, B-1049 Bruessel

BESCHWERDE (Art. 258 AEUV Anregung)
Datum: [DATUM]

Beschwerdefuehrender Mandant: [NAME / KANZLEI]
(Kein eigenes Klagerecht; Anregung an Kommission zur Einleitung VVV)

I. BETROFFENER MITGLIEDSTAAT
Bundesrepublik Deutschland

II. BEANSTANDETER VERSTOESSUNG
[Beschreibung: Nicht-/Fehlumgesetzung [Richtlinie X] in [§ Y Gesetz Z]]

III. BEGRUENDUNG
Die [RL X] verpflichtet die MS bis [DATUM] zu [Maßnahme]. Deutschland hat
[keine / unvollstaendige] Umsetzung vorgenommen: [DETAILS].
Dies beeintraechtigt den Mandanten wie folgt: [SCHADEN / NACHTEIL].

IV. BEILAGE
[Umsetzungsgesetz / fehlende Norm / EU-Text im Vergleich]

Wir bitten die Kommission, ein Vorverfahren nach Art. 258 AEUV zu eroeeffnen.

[KANZLEI], [ORT], [DATUM]
[RA-NAME]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]
