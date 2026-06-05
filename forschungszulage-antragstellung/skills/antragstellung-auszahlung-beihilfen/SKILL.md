---
name: antragstellung-auszahlung-beihilfen
description: "Auszahlung Beihilfen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Auszahlung Beihilfen

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Auszahlung Beihilfen** im Plugin Forschungszulage (FZulG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-antragstellung-tatbestand-beweis-und-belege` | Antragstellung: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-auszahlung-internationaler-bezug-und-schnittstellen` | Auszahlung: Internationaler Bezug und Schnittstellen im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-beihilfen-beweislast-und-darlegungslast` | Beihilfen: Beweislast, Darlegungslast und Substantiierung im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Forschungszulage (FZulG) gilt für **Auszahlung Beihilfen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-antragstellung-tatbestand-beweis-und-belege`

**Fokus:** Antragstellung: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Antragstellung: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Spezialwissen: Antragstellung: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Spezialgegenstand:** Antragstellung: Tatbestandsmerkmale, Beweisfragen und Beleglage / antragstellung tatbestand beweis und belege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Antragstellung** prüfen.
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

## 2. `spezial-auszahlung-internationaler-bezug-und-schnittstellen`

**Fokus:** Auszahlung: Internationaler Bezug und Schnittstellen im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Auszahlung: Internationaler Bezug und Schnittstellen

## Spezialwissen: Auszahlung: Internationaler Bezug und Schnittstellen
- **Spezialgegenstand:** Auszahlung: Internationaler Bezug und Schnittstellen / auszahlung internationaler bezug und schnittstellen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Auszahlung** prüfen.
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

## 3. `spezial-beihilfen-beweislast-und-darlegungslast`

**Fokus:** Beihilfen: Beweislast, Darlegungslast und Substantiierung im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Beihilfen: Beweislast, Darlegungslast und Substantiierung

## Spezialwissen: Beihilfen: Beweislast, Darlegungslast und Substantiierung
- **Spezialgegenstand:** Beihilfen: Beweislast, Darlegungslast und Substantiierung / beihilfen beweislast und darlegungslast. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Beihilfen** prüfen.
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

## Beihilferechtlicher Rahmen FZulG

- Die Forschungszulage ist eine staatliche Beihilfe nach Art. 107 AEUV, die unter die Allgemeine Gruppenfreistellungsverordnung (EU) 651/2014 (AGVO), Artikel 25 fällt: "Beihilfen für Forschungs- und Entwicklungsvorhaben".
- Bei Kumulierung mit anderen staatlichen Beihilfen (Bundes-/Landes-Förderungen, EU-Mittel) sind die Höchstintensitäten nach AGVO Art. 25 Abs. 5-7 einzuhalten:

| FuE-Phase | Höchstintensität (AGVO Art. 25 Abs. 5) | KMU-Bonus |
|---|---|---|
| Grundlagenforschung | 100 % | - |
| Industrielle Forschung | 50 % | + 10 % mittlere Unternehmen, + 20 % Kleinunternehmen |
| Experimentelle Entwicklung | 25 % | + 10 % mittlere, + 20 % Kleinunternehmen |
| Durchführbarkeitsstudien | 50 % | + 10 % mittlere, + 20 % Kleinunternehmen |

## Norm-Bezug konkret

- Art. 107, 108 AEUV: Beihilferahmen.
- AGVO (EU) 651/2014, Art. 25, 28: Vereinbarkeit FuE-Beihilfen / Beihilfen für KMU.
- § 1 Abs. 1 FZulG: Vereinbarkeit mit AGVO als Grundvoraussetzung.
- De-minimis-Verordnung (EU) 2023/2831: irrelevant für FZulG (FZulG fällt unter AGVO, nicht unter De-minimis).
- VO (EU) 1407/2013 (alt) bzw. neue De-minimis-VO: nur für Kumulierung mit De-minimis-Beihilfen relevant.

## Darlegungslast bei Kumulierung

| Punkt | Wer trägt Darlegungslast |
|---|---|
| Höchstintensität eingehalten | Steuerpflichtiger (Antragsteller) |
| KMU-Status | Steuerpflichtiger |
| Konzernzugehörigkeit / verbundene Unternehmen | Steuerpflichtiger |
| Andere Förderungen für dasselbe Vorhaben | Steuerpflichtiger |
| Abgrenzung Förder-fähig / nicht förder-fähig | Steuerpflichtiger; Finanzamt prüft |

## Praktischer Tipp

- **Kumulierungstabelle führen**: pro Vorhaben alle staatlichen Beihilfen mit Quellangabe, Betrag, Förderintensität. Spätestens bei Außenprüfung wird das verlangt.
- **Pflichtangaben im FZulG-Antrag** zu anderweitigen Förderungen: § 9 FZulG verlangt vollständige Offenlegung; Verschweigen führt nicht nur zur Rückforderung der FZulG, sondern kann beihilferechtliche Konsequenzen nach Art. 108 AEUV haben (Rückforderung mit Zinsen).
- **Konzernsicht**: AGVO-Höchstintensitäten gelten konzernweit für verbundene Unternehmen i.S.v. Anhang I AGVO. Mutter und FuE-Tochter sind regelmäßig zusammen zu betrachten.

## Beispiel-Kumulierungsrechnung

> FuE-Vorhaben "X" (experimentelle Entwicklung, Höchstintensität 25 % + 10 % mittlere Unternehmen = 35 %)
> Gesamte förderfähige Kosten: 1.000.000 EUR
> Maximale Beihilfe: 350.000 EUR
>
> Bereits bewilligt:
> - ZIM-Zuschuss BMWK: 200.000 EUR (20 %)
> - FZulG (geplant) bei BMG 800.000 EUR × 35 % KMU: 280.000 EUR (28 %)
>
> Summe: 480.000 EUR / 1.000.000 EUR = 48 % - Überschreitung!
>
> Maßnahme: FZulG-Bemessungsgrundlage reduzieren auf BMG (350.000 - 200.000) / 0,35 = 428.571 EUR, sodass Kumulierung bei 350.000 EUR und damit Höchstintensität 35 % bleibt.

## Typische Fehler

- Anderweitige Förderung im FZulG-Antrag nicht angegeben - Verstoß gegen § 9 FZulG, Rückforderungsrisiko.
- AGVO-Höchstintensität konzernweit nicht aggregiert; bei Tochter-Förderung Mutter-Förderung übersehen.
- "De-minimis" mit AGVO-Förderung verwechselt; FZulG fällt grundsätzlich nicht unter De-minimis.
