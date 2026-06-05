---
name: mandantenentscheidung-einspruch-sonderfall
description: "Mandantenentscheidung Einspruch Sonderfall: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Mandantenentscheidung Einspruch Sonderfall

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Mandantenentscheidung Einspruch Sonderfall** im Plugin Forschungszulage (FZulG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-dokumentation-mandantenentscheidung` | Dokumentation: Mandantenkommunikation und Entscheidungsvorlage im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-einspruch-sonderfall-und-edge-case` | Einspruch: Sonderfall und Edge-Case-Prüfung im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-foerdercheck-risikoampel-und-gegenargumente` | Foerdercheck: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Forschungszulage (FZulG) gilt für **Mandantenentscheidung Einspruch Sonderfall**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-dokumentation-mandantenentscheidung`

**Fokus:** Dokumentation: Mandantenkommunikation und Entscheidungsvorlage im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Dokumentation: Mandantenkommunikation und Entscheidungsvorlage

## Spezialwissen: Dokumentation: Mandantenkommunikation und Entscheidungsvorlage
- **Spezialgegenstand:** Dokumentation: Mandantenkommunikation und Entscheidungsvorlage / dokumentation mandantenentscheidung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** FZulG, BSFZ.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Dokumentation** prüfen.
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

## 2. `spezial-einspruch-sonderfall-und-edge-case`

**Fokus:** Einspruch: Sonderfall und Edge-Case-Prüfung im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Einspruch: Sonderfall und Edge-Case-Prüfung

## Spezialwissen: Einspruch: Sonderfall und Edge-Case-Prüfung
- **Spezialgegenstand:** Einspruch: Sonderfall und Edge-Case-Prüfung / einspruch sonderfall und edge case. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** FZulG, BSFZ.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Einspruch** prüfen.
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

## Zwei verschiedene Einspruchswege

| Bescheidart | Rechtsbehelf | Frist | Stelle |
|---|---|---|---|
| BSFZ-Bescheinigungsbescheid | Widerspruch / Klage VG | 1 Monat (§ 70 VwGO) | direkt BSFZ |
| Festsetzungsbescheid Finanzamt | Einspruch (§ 347 AO) | 1 Monat (§ 355 AO) | Finanzamt |
| Klage gegen Festsetzungsbescheid | Anfechtungsklage FG | 1 Monat (§ 47 FGO) | Finanzgericht |
| Klage gegen BSFZ-Widerspruchsbescheid | Anfechtungsklage VG | 1 Monat (§ 74 VwGO) | Verwaltungsgericht |

## Typische Einspruchsgründe (BSFZ-Ebene)

- "Vorhaben hat kein FuE-Risiko" - Gegenargument: konkretes Risiko mit Literatur belegen, Iterationen nachweisen.
- "Routine-Entwicklung, kein Neuheitsgrad" - Gegenargument: Stand der Technik in der Antragsbegründung konkreter darstellen.
- "Vorhaben gehört zur Grundausstattung" - Gegenargument: Projekt-Charakter mit definierten Meilensteinen, nicht Daueraufgabe.

## Typische Einspruchsgründe (Finanzamt-Ebene)

- Personalzeit-Kürzung durch Außenprüfung - Gegenargument: Stundennachweise vorlegen.
- Auftragsforschung an Nicht-EWR-Dienstleister abgelehnt - regelmäßig keine Heilung möglich.
- KMU-Status verneint, weil Konzernzugehörigkeit übersehen - Gegenargument: Aufschlüsselung der Beteiligungsstruktur.
- Eigenleistung Einzelunternehmer gekürzt - Gegenargument: Stundennachweis vorlegen, Pauschalsatz nicht streitbar.

## Norm-Bezug konkret

- § 5 FZulG, § 6 FZulG: BSFZ-Bescheinigung als Grundlagenbescheid.
- § 9, § 10 FZulG: Festsetzung Forschungszulage.
- § 347 AO, § 355 AO: Einspruch und Frist.
- § 361 AO: AdV beim Finanzamt.
- § 69 FGO: AdV durch Finanzgericht.
- § 70 VwGO, § 74 VwGO: Widerspruch und Klage gegen BSFZ-VA.
- AGVO (EU) 651/2014 Art. 25: beihilferechtliche Rückausnahme bei Kumulierungs-Überschreitung.

## Praktischer Tipp

- **Einspruchsfrist niemals mit "Auf den Tag genau einreichen"-Strategie schmälern**: BSFZ und Finanzamt haben unterschiedliche Bekanntgabe-Wege (postalisch bzw. elektronisch ELSTER); bei elektronischer Bekanntgabe gilt § 122 Abs. 2a AO mit Dreitagesvermutung.
- **AdV-Antrag parallel stellen**: Bei Festsetzungsbescheid mit Verrechnungs- oder Auszahlungsfolge AdV nach § 361 AO beantragen, sonst Liquiditätsproblem.
- **Bei reiner BSFZ-Ablehnung**: zuerst BSFZ-Widerspruch durchziehen, nicht parallel das Finanzamt anrufen - letzteres ist gebundene Folge des BSFZ-Bescheids.

## Beispiel-Mustertext (Einspruchsbegründung Finanzamt - Personalzeit)

> Gegen den Festsetzungsbescheid Forschungszulage vom [Datum, AZ] lege ich namens der Mandantschaft form- und fristgerecht Einspruch ein. Begründung:
>
> Das Finanzamt hat die im Antrag ausgewiesene Personalzeit von [X] Std. für FuE-Aktivitäten im Rahmen des bescheinigten Vorhabens [BSFZ-AZ] auf [Y] Std. gekürzt. Diese Kürzung entbehrt einer Grundlage. Die Stundenaufzeichnungen (Anlage 1) weisen die FuE-Zuordnung der einzelnen Mitarbeiter [...] nach Tag, Vorhaben-Nummer und Tätigkeit lückenlos aus. Eine Kürzung allein wegen pauschalen Zweifeln des Prüfers an der Plausibilität ist verfahrensrechtlich nicht zulässig (Beweislast Finanzamt für die Kürzung, vgl. § 88 AO Untersuchungsgrundsatz).
>
> Antrag: Festsetzung der Forschungszulage in Höhe von EUR [...] entsprechend der ursprünglich beantragten Bemessungsgrundlage. Zusätzlich Antrag auf Aussetzung der Vollziehung gemäß § 361 AO bis zur Entscheidung über den Einspruch.

## Typische Fehler

- Widerspruch gegen BSFZ-Bescheid ans Finanzamt geschickt - falsche Zuständigkeit, kein Fristwirkung.
- Klage gegen Festsetzungsbescheid beim Verwaltungsgericht erhoben - Rechtsweg verfehlt, FGO einschlägig.
- AdV-Antrag vergessen, obwohl Liquiditätsdruck besteht.

## 3. `spezial-foerdercheck-risikoampel-und-gegenargumente`

**Fokus:** Foerdercheck: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Foerdercheck: Risikoampel, Gegenargumente und Verteidigungslinien

## Spezialwissen: Foerdercheck: Risikoampel, Gegenargumente und Verteidigungslinien
- **Spezialgegenstand:** Foerdercheck: Risikoampel, Gegenargumente und Verteidigungslinien / foerdercheck risikoampel und gegenargumente. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** FZulG, BSFZ.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Foerdercheck** prüfen.
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
