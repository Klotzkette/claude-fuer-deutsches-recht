---
name: forschungszulage-insolvenzlage-red
description: "Insolvenzlage RED: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Insolvenzlage RED

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Insolvenzlage RED** im Plugin Forschungszulage (FZulG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-forschungszulage-erstpruefung-und-mandatsziel` | Forschungszulage: Erstprüfung, Rollenklärung und Mandatsziel im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-insolvenzlage-red-team-und-qualitaetskontrolle` | Insolvenzlage: Red-Team und Qualitätskontrolle im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-portaltexte-schriftsatz-brief-und-memo-bausteine` | Portaltexte: Schriftsatz-, Brief- und Memo-Bausteine im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Forschungszulage (FZulG) gilt für **Insolvenzlage RED**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-forschungszulage-erstpruefung-und-mandatsziel`

**Fokus:** Forschungszulage: Erstprüfung, Rollenklärung und Mandatsziel im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Forschungszulage: Erstprüfung, Rollenklärung und Mandatsziel

## Spezialwissen: Forschungszulage: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Forschungszulage: Erstprüfung, Rollenklärung und Mandatsziel / forschungszulage erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Forschungszulage** prüfen.
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

## FZulG-Anspruchsvoraussetzungen (Erstprüfung)

| Tatbestandsmerkmal | Norm | Prüffrage |
|---|---|---|
| Anspruchsberechtigter | § 1 FZulG | Steuerpflichtige nach EStG / KStG mit FuE-Aktivität in DE; auch Personengesellschaften, mit Sonderregeln für nicht-steuerpflichtige Mitunternehmer |
| FuE-Vorhaben | § 2 FZulG i.V.m. Frascati-Manual | Grundlagenforschung, industrielle Forschung oder experimentelle Entwicklung |
| Begünstigte Aufwendungen | § 3 FZulG | Lohnaufwendungen FuE-Personal + 25 % Pauschale für Personalnebenkosten + Auftragsforschungs-Anteil + bestimmte Einzelunternehmer-Eigenleistung |
| Bemessungsgrundlage | § 3 FZulG | maximal förderfähig pro Jahr (Höchstgrenze vor Ausgabe verifizieren - ab 2024/2025 erhöht) |
| Zulagensatz | § 4 FZulG | regelmäßig 25 %, für KMU + 10 % (auf Antrag) |

## Norm-Bezug konkret

- § 1 FZulG: Anspruchsvoraussetzung.
- § 2 FZulG: begünstigte FuE-Tätigkeiten.
- § 3 FZulG: förderfähige Aufwendungen und Bemessungsgrundlage.
- § 4 FZulG: Höhe der Forschungszulage.
- §§ 5, 6 FZulG: Bescheinigungsverfahren BSFZ.
- §§ 9, 10 FZulG: Festsetzung beim Finanzamt.
- BMF-Schreiben zum FZulG (Datum und AZ vor Ausgabe verifizieren auf bundesfinanzministerium.de).
- AGVO (EU) 651/2014: beihilferechtliche Grundlage; Art. 25 Forschungs- und Entwicklungsvorhaben.

## Praktischer Tipp

- Forschungszulage ist eine **steuerliche Förderung mit Verrechnung gegen die Einkommen-/Körperschaftsteuerschuld**; bei Verlusten oder zu niedriger Steuerschuld erfolgt **Auszahlung des überschießenden Betrags** (§ 10 Abs. 1 Satz 4 FZulG). Das ist der zentrale Liquiditätsvorteil gegenüber klassischen Sonderabschreibungen.
- BSFZ-Bescheinigung ist **rückwirkend möglich** für vier Jahre nach Ende des Wirtschaftsjahres (Antrag bei BSFZ); die Festsetzung beim Finanzamt erfolgt **mit der Einkommen-/Körperschaftsteuererklärung** des jeweiligen Wirtschaftsjahres.
- Forschungszulage ist beihilferechtlich vereinbar mit anderen Beihilfen, aber **bei kumulativer Anwendung Höchstintensitäten der AGVO Art. 25 prüfen** (Grundlagenforschung 100 %, industrielle Forschung 50 %, experimentelle Entwicklung 25 %; KMU-Aufschläge).

## Trade-off: FZulG vs. andere Förderinstrumente

| Pfad | Vorteil | Nachteil |
|---|---|---|
| FZulG | rechtssicherer Anspruch (kein Antragsglück), auch in Verlustlage liquiditätswirksam | engerer FuE-Begriff, Verfahren in zwei Stufen |
| ZIM, Horizon Europe | höhere Förderquoten bei Zuschuss | konkurrenzbasiert, Antragsaufwand hoch |
| Investitionsabzugsbetrag § 7g EStG | breit anwendbar | nur Stundung, kein "echter" Zuschuss |

Empfehlung: FZulG immer prüfen, weil rechtssicher; nicht alternativ, sondern **kumulativ** zu klassischen Projektförderungen denken.

## Typische Fehler (Erstprüfung)

- Antragsteller hält Routinetätigkeiten (Software-Wartung, marginale Produktverbesserung) für FuE - Bescheinigung wird abgelehnt.
- Eigenleistung des Einzelunternehmers wird nicht angesetzt, obwohl nach § 3 Abs. 3 FZulG erlaubt (pauschal 70 EUR/Std., maximal 40 Std./Woche, vor Ausgabe verifizieren).
- Antrag beim Finanzamt ohne vorherige BSFZ-Bescheinigung - das Finanzamt setzt nicht fest, bis die Bescheinigung vorliegt.

## 2. `spezial-insolvenzlage-red-team-und-qualitaetskontrolle`

**Fokus:** Insolvenzlage: Red-Team und Qualitätskontrolle im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Insolvenzlage: Red-Team und Qualitätskontrolle

## Spezialwissen: Insolvenzlage: Red-Team und Qualitätskontrolle
- **Spezialgegenstand:** Insolvenzlage: Red-Team und Qualitätskontrolle / insolvenzlage red team und qualitaetskontrolle. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Insolvenzlage** prüfen.
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

## 3. `spezial-portaltexte-schriftsatz-brief-und-memo-bausteine`

**Fokus:** Portaltexte: Schriftsatz-, Brief- und Memo-Bausteine im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Portaltexte: Schriftsatz-, Brief-, Memo- und Plädoyer-Bausteine

## Spezialwissen: Portaltexte: Schriftsatz-, Brief-, Memo- und Plädoyer-Bausteine
- **Spezialgegenstand:** Portaltexte: Schriftsatz-, Brief-, Memo- und Plädoyer-Bausteine / portaltexte schriftsatz brief und memo bausteine. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Portaltexte** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Plädoyer-Kern:** ein Satz, der FuE-Kern, Beleganker und Antrag zusammenbindet; bei Bedarf als Kurzfassung, Langfassung und Behördenfassung.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
