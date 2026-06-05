---
name: forschungszulage-antragstellung-workflow-mandantenkommunikation
description: "Workflow Mandantenkommunikation: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Workflow Mandantenkommunikation

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Workflow Mandantenkommunikation** im Plugin Forschungszulage (FZulG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin forschungszulage-antragstellung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin forschungszulage-antragstellung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `spezial-fzulg-fristen-form-und-zustaendigkeit` | FZulG: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Forschungszulage (FZulG) gilt für **Workflow Mandantenkommunikation**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin forschungszulage-antragstellung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin forschungszulage-antragstellung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin forschungszulage-antragstellung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin forschungszulage-antragstellung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 3. `spezial-fzulg-fristen-form-und-zustaendigkeit`

**Fokus:** FZulG: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin forschungszulage antragstellung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# FZulG: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: FZulG: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** FZulG: Fristen, Form, Zuständigkeit und Rechtsweg / fzulg fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **FZulG** prüfen.
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

## FZulG-Fristen und Zuständigkeiten

| Aktion | Frist | Stelle |
|---|---|---|
| BSFZ-Bescheinigungsantrag | jederzeit, rückwirkend für vier Jahre nach Ende des Wirtschaftsjahres (vor Ausgabe verifizieren) | BSFZ (bescheinigung-forschungszulage.de) |
| Antrag auf Festsetzung Forschungszulage | mit der ESt-/KSt-Erklärung des Wirtschaftsjahres | zuständiges Finanzamt des Betriebs |
| Einspruch BSFZ-Bescheid | 1 Monat nach Bekanntgabe (§ 70 VwGO) | direkt bei BSFZ |
| Einspruch Festsetzungsbescheid Finanzamt | 1 Monat nach Bekanntgabe (§ 355 AO) | Finanzamt |
| Klage gegen BSFZ-Bescheid | nach erfolglosem Einspruch | Verwaltungsgericht (Sitz BSFZ - Berlin oder zuständig laut RBB) |
| Klage gegen Festsetzungsbescheid | nach erfolglosem Einspruch | Finanzgericht |

## Norm-Bezug konkret

- § 5 Abs. 1 FZulG: Bescheinigungsantrag bei BSFZ.
- § 9 Abs. 1 FZulG: Antrag auf Festsetzung beim Finanzamt nach Ablauf des Wirtschaftsjahres.
- § 10 FZulG: Festsetzung, Verrechnung mit ESt/KSt, ggf. Auszahlung des überschießenden Betrags.
- § 169 Abs. 2 AO: Festsetzungsfrist 4 Jahre.
- § 355 AO: Einspruchsfrist Steuerbescheid 1 Monat.
- § 70 VwGO: Widerspruchsfrist Verwaltungsakt 1 Monat (für BSFZ-Bescheinigung als VA).
- § 42 FGO: Klagefrist Finanzgericht 1 Monat.

## Praktischer Tipp

- **Zweigleisigkeit beachten**: BSFZ-Bescheid ist Verwaltungsakt nach VwVfG (Bundesrecht), Festsetzungsbescheid Finanzamt ist Steuerverwaltungsakt nach AO. Zwei separate Rechtsbehelfssysteme.
- BSFZ-Bescheinigung wirkt als **Grundlagenbescheid** für das Finanzamt; bei abgelehnter BSFZ-Bescheinigung Finanzamt nicht erst anrufen, sondern BSFZ-Bescheid zuerst angreifen.
- Vier-Jahres-Rückwirkung gibt Spielraum: bei knapper Liquidität auch noch zurückliegende Wirtschaftsjahre antragsfähig. Voraussetzung: Festsetzungsfrist § 169 AO für die jeweilige ESt-/KSt-Veranlagung noch offen.

## Beispiel-Mustertext (Antrag auf Festsetzung Forschungszulage)

> An das Finanzamt [...]
>
> Antrag auf Festsetzung der Forschungszulage gemäß § 9 FZulG für das Wirtschaftsjahr [Jahr]
>
> Sehr geehrte Damen und Herren,
> namens und mit Vollmacht der [Mandant], Steuernummer [...], beantrage ich die Festsetzung der Forschungszulage gemäß § 9 FZulG für das Wirtschaftsjahr [Datum bis Datum]. Beigefügt ist:
>
> 1. BSFZ-Bescheinigung vom [Datum, AZ] (Anlage 1).
> 2. Aufstellung der förderfähigen Aufwendungen nach § 3 FZulG (Anlage 2): Lohnaufwendungen für FuE-Personal EUR [...], 25 % Personalnebenkosten EUR [...], begünstigte Auftragsforschung EUR [...] x [...] %, [ggf.] Eigenleistung Einzelunternehmer EUR [...].
> 3. Bemessungsgrundlage EUR [...]; bei Zulagensatz [25 %/35 % KMU] beläuft sich die Forschungszulage auf EUR [...].
> 4. Belege zur Personalzuordnung FuE (Stundenaufzeichnungen, Anlage 3).
>
> Eine Festsetzung mit Verrechnung gegen die festgesetzte ESt/KSt des Wirtschaftsjahres und Auszahlung des überschießenden Betrags gemäß § 10 Abs. 1 Satz 4 FZulG wird beantragt.

## Typische Fehler

- Einspruch gegen BSFZ-Bescheid wird ans Finanzamt geschickt - Zuständigkeit verfehlt, Frist tickt weiter.
- Festsetzungsantrag ohne BSFZ-Bescheinigung - Bearbeitung ruht.
- Eigenleistung Einzelunternehmer nicht aufgeschlüsselt (Std., Wochen, Begründung); pauschale Beantragung wird gekürzt.
