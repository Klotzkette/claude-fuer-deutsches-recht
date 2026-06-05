---
name: vermoegensauskunft-vollstreckungsbescheid
description: "Vermoegensauskunft Vollstreckungsbescheid: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vermoegensauskunft Vollstreckungsbescheid

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Vermoegensauskunft Vollstreckungsbescheid** im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-vermoegensauskunft-zahlen-schwellen-und-berechnung` | Vermoegensauskunft: Zahlen, Schwellenwerte und Berechnung im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-vollstreckungsbescheid-dokumentenmatrix-und-lueckenliste` | Vollstreckungsbescheid: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-vollstreckungstitel-sonderfall-und-edge-case` | Vollstreckungstitel: Sonderfall und Edge-Case-Prüfung im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.) gilt für **Vermoegensauskunft Vollstreckungsbescheid**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-vermoegensauskunft-zahlen-schwellen-und-berechnung`

**Fokus:** Vermoegensauskunft: Zahlen, Schwellenwerte und Berechnung im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Vermoegensauskunft: Zahlen, Schwellenwerte und Berechnung

## Spezialwissen: Vermoegensauskunft: Zahlen, Schwellenwerte und Berechnung
- **Spezialgegenstand:** Vermoegensauskunft: Zahlen, Schwellenwerte und Berechnung / vermoegensauskunft zahlen schwellen und berechnung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ZPO, InsO, ZVG, EU, VO.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Vermoegensauskunft** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Materielle Weichen Vermögensauskunft (§ 802c ZPO)
- **Rechtsgrundlage:** § 802c ZPO i.V.m. §§ 802a, 802d ZPO. Pflicht des Schuldners zur Abgabe einer Vermögensauskunft im Vermögensverzeichnis vor dem Gerichtsvollzieher (früher: eidesstattliche Versicherung).
- **Voraussetzung:** Gläubiger benötigt vollstreckbaren Titel; keine eigenständige Schwelle (anders als früher 500-Euro-Grenze).
- **Verfahren:** Gerichtsvollzieher fordert Schuldner zur Abgabe; Schuldner muss persönlich erscheinen, alle Vermögensgegenstände, Forderungen, Beschäftigungsverhältnisse und Zahlungen der letzten zwei Jahre offenlegen.
- **Verzeichnis-Inhalt (§ 802c Abs. 2 ZPO):** Forderungen aus Lohn, Bankguthaben, Wertpapiere, Lebensversicherungen, Grundstücke, Sicherungseigentum, GmbH-Anteile, Fahrzeuge, Wertsachen, Schenkungen letzte 4 Jahre (an nahestehende Personen), übertragenes Vermögen.
- **Eintragung im Schuldnerverzeichnis (§ 882b ZPO):** Bei Nichtabgabe oder erfolgloser Vollstreckung Eintragung von Amts wegen ins Schuldnerverzeichnis - online abrufbar (für Gläubiger gegen Gebühr). Dauer: drei Jahre nach Eintragung.
- **Haftbefehl (§ 802g ZPO):** Bei unentschuldigter Nichtabgabe Erzwingungshaft bis sechs Monate. Beantragung beim Gerichtsvollzieher; Haftbefehl wird durch Amtsgericht erlassen.
- **Wiederholung (§ 802d Abs. 1 ZPO):** Erneute Vermögensauskunft erst nach Ablauf von 2 Jahren erforderlich; Ausnahme bei plausibler Begründung erheblicher Änderungen (§ 802d Abs. 1 S. 2 ZPO).
- **Schutzschriften / Korrekturen:** Schuldner kann unrichtige Angaben durch Berichtigung korrigieren (§ 802c Abs. 3 ZPO); falsche Angaben sind als Straftat (§ 156 StGB - falsche Versicherung an Eides statt) strafbar.
- **Praktiker-Tipp:** Vor Antrag: § 802l ZPO Kontensuche bei Bundeszentralamt für Steuern parallel beauftragen. Vermögensauskunft schafft die Voraussetzung für gezielte PfÜBs.

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

## 2. `spezial-vollstreckungsbescheid-dokumentenmatrix-und-lueckenliste`

**Fokus:** Vollstreckungsbescheid: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Vollstreckungsbescheid: Dokumentenmatrix, Lückenliste und Nachforderung

## Spezialwissen: Vollstreckungsbescheid: Dokumentenmatrix, Lückenliste und Nachforderung
- **Spezialgegenstand:** Vollstreckungsbescheid: Dokumentenmatrix, Lückenliste und Nachforderung / vollstreckungsbescheid dokumentenmatrix und lueckenliste. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ZPO, InsO, ZVG, EU, VO.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Vollstreckungsbescheid** prüfen.
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

## 3. `spezial-vollstreckungstitel-sonderfall-und-edge-case`

**Fokus:** Vollstreckungstitel: Sonderfall und Edge-Case-Prüfung im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Vollstreckungstitel: Sonderfall und Edge-Case-Prüfung

## Spezialwissen: Vollstreckungstitel: Sonderfall und Edge-Case-Prüfung
- **Spezialgegenstand:** Vollstreckungstitel: Sonderfall und Edge-Case-Prüfung / vollstreckungstitel sonderfall und edge case. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ZPO, InsO, ZVG, EU, VO.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Vollstreckungstitel** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Materielle Weichen Vollstreckungstitel (§§ 704, 794 ZPO)
- **Katalog (§ 794 Abs. 1 ZPO):** (1) Urteile rechtskräftig oder vorläufig vollstreckbar, (2) Vollstreckungsbescheide, (3) gerichtliche Vergleiche, (4) Kostenfestsetzungsbeschlüsse, (5) vollstreckbare notarielle Urkunden, (6) Schiedssprüche nach § 1060 ZPO, (7) anwaltliche Vergleiche nach § 796a ZPO, (8) europäische Vollstreckungstitel etc.
- **Vollstreckungsklausel (§ 724 ZPO):** Erforderlich auf jeder Ausfertigung des Titels (Ausnahme: Vollstreckungsbescheid - mit Erlass vollstreckbar). Klauselantrag beim Gericht/Notar; Klauselgegenklage § 768 ZPO bei Einwendungen.
- **Notarielle Urkunde (§ 794 Abs. 1 Nr. 5 ZPO):** Bedarf ausdrücklicher Vollstreckungsunterwerfung; Schuldner muss sich der sofortigen Zwangsvollstreckung unterwerfen. Wirksam bei klaren, bestimmbaren Forderungen.
- **Vorläufige Vollstreckbarkeit:** Mit Sicherheitsleistung (§§ 708 Abs. 11 ZPO i.V.m. 709 ZPO) bei Geldforderungen aus erstinstanzlichem Urteil; ohne Sicherheitsleistung in Spezialfällen (§ 708 ZPO).
- **Voraussetzungen für jede Vollstreckung (§ 750 ZPO):** (1) Titel mit Vollstreckungsklausel (außer Vollstreckungsbescheid), (2) Zustellung an den Schuldner, (3) keine Vollstreckungssperre (Eilanträge, Insolvenzeröffnung, § 89 InsO).
- **Vollstreckungsabwehrklage (§ 767 ZPO):** Schuldner kann materielle Einwendungen (Erfüllung, Stundung, Verjährung), die nach Schluss der mündlichen Verhandlung entstanden sind, im Wege der Vollstreckungsabwehrklage geltend machen.
- **Verjährung (§§ 197 Abs. 1 Nr. 3, 4 BGB):** Vollstreckungstitel verjähren in 30 Jahren ab Rechtskraft. Wiederholtes Anhängigmachen / Wiederaufnahme des Vollstreckungsverfahrens unterbricht die Verjährung.
- **EuG-Titel:** Europäischer Vollstreckungstitel (VO 805/2004), Europäischer Zahlungsbefehl (VO 1896/2006), Europäischer Geringfügigkeitsverfahren (VO 861/2007) - länderübergreifende Vollstreckung ohne Exequatur.

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
