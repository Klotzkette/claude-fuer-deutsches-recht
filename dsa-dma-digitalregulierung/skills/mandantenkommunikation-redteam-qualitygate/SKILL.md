---
name: mandantenkommunikation-redteam-qualitygate
description: "Mandantenkommunikation, Redteam Qualitygate, Dma Fristen Form Und Zustaendigkeit: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Mandantenkommunikation, Redteam Qualitygate, Dma Fristen Form Und Zustaendigkeit

## Arbeitsbereich

Dieser Skill bündelt **Mandantenkommunikation, Redteam Qualitygate, Dma Fristen Form Und Zustaendigkeit** zu einem konkreten Arbeitsgang. Starte mit dem Modul, das die Tatsachen der Akte trägt; weitere Module nur hinzunehmen, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output betreffen.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin dsa-dma-digitalregulierung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin dsa-dma-digitalregulierung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `spezial-dma-fristen-form-und-zustaendigkeit` | DMA: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin dsa dma digitalregulierung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Für **Mandantenkommunikation, Redteam Qualitygate, Dma Fristen Form Und Zustaendigkeit** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `dsa-dma-digitalregulierung` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin dsa-dma-digitalregulierung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin dsa-dma-digitalregulierung: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

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

## Mandantenkommunikation DSA/DMA
- **Anrede + Bezug:** "In Sachen [Mandant] / Ihre DSA-/DMA-Compliance"
- **Sachstand kurz:** Plattform-Kategorisierung (Vermittlungsdienst, Hosting, Online-Plattform, VLOP), Pflichtenkanon, Status Compliance.
- **Empfehlung:** zentraler nächster Schritt (z. B. "AGB Art. 14-DSA-konform anpassen, Statement-of-Reasons-Prozess implementieren, Single Point of Contact benennen").
- **Risikoampel** mit Bezug auf Bußgeldrahmen (DSA 6 %, DMA 10 % bzw. 20 %).
- **Frist** klar benennen: Compliance-Berichte jährlich, Risikobewertung VLOP jährlich, Statement of Reasons unverzüglich.
- **Kostenhinweis:** RVG/Honorarvereinbarung.
- **Zuständigkeitshinweis:** DSA via BNetzA (deutscher DSC); DMA ausschließlich Kommission — Doppelverfahren vermeiden.

## Praxis-Tipp
Vermeiden Sie pauschale Aussagen wie "Sie sind nicht betroffen". DSA gilt für alle Vermittlungsdienste mit gestuftem Pflichtenkanon; auch Kleinst- und Kleinunternehmen sind betroffen, lediglich mit Erleichterungen (Art. 19, 24, 29 DSA). Lassen Sie diese Differenzierung sichtbar werden.

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

**Fokus:** Red-Team Qualitygate im Plugin dsa-dma-digitalregulierung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin dsa-dma-digitalregulierung: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

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

## Red-Team-Prüfpunkte DSA/DMA
1. **Rollenklarheit:** Vermittlungsdienst (Art. 6 DSA), Hosting (Art. 6 DSA), Online-Plattform (Art. 19 ff. DSA) oder VLOP/VLOSE (Art. 33 ff. DSA)? Pflichtenkanon variiert erheblich.
2. **Anwendungsbereich:** Anbieter mit Sitz in EU (Art. 2 DSA) oder Drittlandsanbieter mit EU-Nutzern (dann Art. 13 DSA Rechtsvertreter Pflicht)?
3. **Notice-and-Action:** Wurde der Mechanismus nach Art. 16 DSA implementiert? Mit den Pflichtinformationen?
4. **Statement of Reasons (SoR):** Art. 17 DSA — wird vollständig gegenüber Nutzer und Transparenzdatenbank erfüllt?
5. **AGB:** Erfüllen die Nutzungsbedingungen Art. 14 DSA-Anforderungen?
6. **DMA-Gatekeeper-Verwechslung:** Kein DMA-Argument bei einem Anbieter, der nicht als Gatekeeper benannt ist; und umgekehrt — DMA-Pflichten gelten erst nach Benennung.
7. **Nationaler vs. EU-Rahmen:** DSA-Aufsicht national bei DSC (BNetzA für DE), DMA-Aufsicht ausschließlich EU-Kommission.
8. **Halluzinations-Check:** Keine erfundenen Erwägungsgründe; keine Vermischung Erwägung — Norm — Leitlinie.

## Praxis-Tipp
Häufiger Fehler: DSA und DMA werden vermischt. Die Pflichtenwirkung ist eine andere — DSA gilt für alle Vermittlungsdienste mit gestuftem Pflichtenkanon, DMA nur für ausdrücklich benannte Gatekeeper. Bei Beratung stets zuerst klären: "Ist Ihr Mandant von der EU-Kommission als Gatekeeper benannt?" Wenn nein: kein DMA-Argument.

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

## 3. `spezial-dma-fristen-form-und-zustaendigkeit`

**Fokus:** DMA: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin dsa dma digitalregulierung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# DMA: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: DMA: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** DMA: Fristen, Form, Zuständigkeit und Rechtsweg / dma fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DMA, EU, DSA, VO, DGA, AI, NIS, DORA, CRA, DDG, GWB, VLOP.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **DMA** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## DMA-typische Fristen und Zuständigkeit
- **Art. 3 DMA Gatekeeper-Benennung:** Mitteilung an Kommission binnen 2 Monaten nach Schwellenerreichung; Benennungsbeschluss der Kommission binnen 45 Arbeitstagen.
- **Art. 5-7 DMA Pflichten:** 6 Monate nach Benennung wirksam.
- **Art. 11 DMA Compliance-Bericht:** jährlich an Kommission.
- **Art. 14 DMA Zusammenschlüsse:** Informationspflicht an Kommission.
- **Art. 30 DMA Bußgeld:** bis 10 % Jahresumsatz, bei Wiederholung bis 20 %, Zwangsgeld täglich bis 5 %.
- **Zuständig**: ausschließlich EU-Kommission (Art. 39 DMA), keine nationalen Doppelverfahren — anders als bei DSA (dort nationale DSC nach Art. 49 DSA).
- **Rechtsweg:** Klage zum Gericht der Europäischen Union (EuG) gemäß Art. 263 AEUV gegen Kommissionsbeschlüsse; Revision zum EuGH.

## Praxis-Tipp
DMA-Verfahren laufen ausschließlich europäisch — nationale Wettbewerbsbehörden bleiben außen vor (Art. 1 Abs. 6 DMA). Wer als Gatekeeper-Adressat parallel ein nationales Kartellverfahren (z. B. § 19a GWB) führt, sollte das Verhältnis ne bis in idem prüfen. § 19a GWB ergänzt DMA punktuell — keine Verdrängung.

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
