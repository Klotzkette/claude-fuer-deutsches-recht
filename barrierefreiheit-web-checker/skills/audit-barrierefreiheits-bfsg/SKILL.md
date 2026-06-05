---
name: audit-barrierefreiheits-bfsg
description: "Audit Barrierefreiheits BFSG: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Audit Barrierefreiheits BFSG

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Audit Barrierefreiheits BFSG** im Plugin Barrierefreiheit Web (BFSG/WCAG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-audit-schriftsatz-brief-und-memo-bausteine` | Audit: Schriftsatz-, Brief- und Memo-Bausteine im Plugin barrierefreiheit web checker; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-barrierefreiheits-erstpruefung-und-mandatsziel` | Barrierefreiheits: Erstprüfung, Rollenklärung und Mandatsziel im Plugin barrierefreiheit web checker; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-bfsg-tatbestand-beweis-und-belege` | BFSG: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin barrierefreiheit web checker; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Barrierefreiheit Web (BFSG/WCAG) gilt für **Audit Barrierefreiheits BFSG**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-audit-schriftsatz-brief-und-memo-bausteine`

**Fokus:** Audit: Schriftsatz-, Brief- und Memo-Bausteine im Plugin barrierefreiheit web checker; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Audit: Schriftsatz-, Brief- und Memo-Bausteine

## Spezialwissen: Audit: Schriftsatz-, Brief- und Memo-Bausteine
- **Spezialgegenstand:** Audit: Schriftsatz-, Brief- und Memo-Bausteine / audit schriftsatz brief und memo bausteine. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BFSG, BFSGV, BITV, EN, WCAG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Audit** prüfen.
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

## 2. `spezial-barrierefreiheits-erstpruefung-und-mandatsziel`

**Fokus:** Barrierefreiheits: Erstprüfung, Rollenklärung und Mandatsziel im Plugin barrierefreiheit web checker; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Barrierefreiheits: Erstprüfung, Rollenklärung und Mandatsziel

## Spezialwissen: Barrierefreiheits: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Barrierefreiheits: Erstprüfung, Rollenklärung und Mandatsziel / barrierefreiheits erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BFSG, BFSGV, BITV, EN, WCAG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Barrierefreiheit** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Erstprüfung Barrierefreiheit: 5-Schritte-Diagnose
1. **Rolle bestimmen:** Hersteller (§ 3 Nr. 1 BFSG), Importeur (§ 3 Nr. 2), Händler (§ 3 Nr. 3), Dienstleistungserbringer (§ 3 Nr. 4) — Pflichtenkanon je nach Rolle.
2. **Anwendungsbereich BFSG (§ 1):** Liegt das konkrete Produkt/Dienst im abschließenden Katalog (Computerhardware, Selbstbedienungsterminals, Verbraucherendgeräte für elektronische Kommunikation, audiovisuelle Mediendienste, Personenverkehr, Bankendienstleistungen, E-Books, elektronischer Geschäftsverkehr)?
3. **Kleinstunternehmens-Ausnahme (§ 3 Abs. 3 BFSG):** Beschäftigte < 10 und Jahresumsatz/Bilanzsumme < 2 Mio. EUR?
4. **Zeitlich:** Inverkehrbringen vor oder nach 28.06.2025? Übergang § 38 BFSG für Selbstbedienungsterminals bis 27.06.2040.
5. **Mandatsziel:** Erst-Audit? Konformitätserklärung? Klagedrohung abwehren? Mängelbeseitigung gegen Behörde verteidigen? Schlichtung initiieren?

## Trade-off
Vollumfängliches Audit aller Seiten/Funktionen vs. risikobasiertes Stichprobenaudit: bei großen Plattformen wirtschaftlich nur risikobasiert möglich. Aber: Konformitätserklärung muss den geprüften Geltungsbereich klar benennen — sonst trägt sie nicht die Generalaussage.

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

## 3. `spezial-bfsg-tatbestand-beweis-und-belege`

**Fokus:** BFSG: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin barrierefreiheit web checker; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# BFSG: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Spezialwissen: BFSG: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Spezialgegenstand:** BFSG: Tatbestandsmerkmale, Beweisfragen und Beleglage / bfsg tatbestand beweis und belege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BFSG, BFSGV, BITV, EN, WCAG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **BFSG** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Tatbestandsstruktur BFSG-Verstoß
Wirtschaftsakteur-Pflicht ist verletzt, wenn:
- **Produkt / Dienstleistung im Anwendungsbereich** (§ 1 Abs. 2/3 BFSG)
- **Inverkehrbringen / Erbringen nach 28.06.2025** (§ 38 BFSG; Übergangsregelungen beachten)
- **Anforderungen Anhang 1 BFSGV nicht erfüllt** und keine Ausnahme nach § 16 (grundlegende Veränderung), § 17 (unverhältnismäßige Belastung) oder § 3 Nr. 17 (Kleinstunternehmen für Dienstleistung) greift
- **Konformitätsvermutung nach harmonisierter Norm EN 301 549** nicht in Anspruch genommen

## Beweisthemen
- **Konformitätsvermutung**: Wer die Vermutung in Anspruch nimmt, muss die Anwendung der harmonisierten Norm und das Ergebnis dokumentieren (technische Dokumentation § 6 BFSG, Anhang 2 BFSGV).
- **Unverhältnismäßige Belastung (§ 17)**: Bewertung in Anlehnung an Anhang 4 BFSGV — Verhältnis Kosten/Nutzen, Größe des Unternehmens, geschätzte Inanspruchnahme durch Menschen mit Behinderung. Dokumentationspflicht **vor** dem Inverkehrbringen.
- **Wesentliche Veränderung (§ 16)**: dokumentieren, welches Wesensmerkmal betroffen wäre.

## Beleglage in Audit-Berichten
- Screenshot mit URL, Datum und Uhrzeit
- DOM-Auszug der betroffenen Stelle
- WCAG-Erfolgskriterium und EN-301-549-Klausel
- Reproduktionsschritt (Browser, Hilfstechnologie, Version)
- Erwartetes Verhalten und Soll-Zustand

## Trade-off
"Unverhältnismäßige Belastung" wird von Marktüberwachungsbehörden eng ausgelegt; pauschale Berufung ohne dokumentierte Bewertung ist im Klage- und Bußgeldverfahren nicht tragfähig. Die Bewertung ist alle 5 Jahre, bei wesentlichen Änderungen oder auf Verlangen der Marktüberwachung zu überprüfen.

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
