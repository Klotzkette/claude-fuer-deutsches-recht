---
name: zv-pfueb-802l-arbeit
description: "ZV Pfueb 802l Arbeit: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# ZV Pfueb 802l Arbeit

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **ZV Pfueb 802l Arbeit** im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zv-pfueb-mieter-finanzamt` | Gläubiger will Mietforderung Steuererstattung oder Forderung gegen sonstigen Drittschuldner pfaenden. §§ 829 835 851 850b ZPO sonstige Drittschuldner. Prüfraster: Mieter Mietzinsforderung Finanzamt Steuererstattung Kranken-kasse Krankengeld Versicherung Rückkaufswert Geschäftspartner Rechnungen. § 851 ZPO Unuebertragbarkeit § 850b ZPO bedingt pfaendbar. Output: PfUeB-Antrag sonstiger Drittschuldner. Abgrenzung zu zv-pfueb-bank (Bank) und zv-pfueb-arbeitsentgelt (Lohn). |
| `spezial-802l-verhandlung-vergleich-und-eskalation` | 802L: Verhandlung, Vergleich und Eskalation im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-arbeit-schriftsatz-brief-und-memo-bausteine` | Arbeit: Schriftsatz-, Brief- und Memo-Bausteine im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Zwangsvollstreckung (ZPO §§ 704 ff.) gilt für **ZV Pfueb 802l Arbeit**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `zv-pfueb-mieter-finanzamt`

**Fokus:** Gläubiger will Mietforderung Steuererstattung oder Forderung gegen sonstigen Drittschuldner pfaenden. §§ 829 835 851 850b ZPO sonstige Drittschuldner. Prüfraster: Mieter Mietzinsforderung Finanzamt Steuererstattung Kranken-kasse Krankengeld Versicherung Rückkaufswert Geschäftspartner Rechnungen. § 851 ZPO Unuebertragbarkeit § 850b ZPO bedingt pfaendbar. Output: PfUeB-Antrag sonstiger Drittschuldner. Abgrenzung zu zv-pfueb-bank (Bank) und zv-pfueb-arbeitsentgelt (Lohn).

# PfÜB Mieter, Finanzamt, sonstige Drittschuldner

## Aufgabe

Pfändung beweglicher Forderungen jenseits von Bank und Arbeitgeber. Häufigste Fälle: Mietzins (Vermieter ist Schuldner, Mieter ist Drittschuldner), Steuererstattung gegen Finanzamt, Versicherungsleistungen, B2B-Forderungen.

## Startet bei

- Titel + Klausel + Zustellung grün
- Drittschuldner identifizierbar (Person, Sitz)
- Forderung nicht nach § 851 ZPO unpfändbar

## Rechtsgrundlagen

- §§ 829, 835 ZPO – allgemeine Forderungspfändung
- § 851 ZPO – unpfändbare Forderungen
- § 851a ZPO – Pfändungsschutz Landwirt
- § 851b ZPO – Pfändungsschutz Miete (Mieterperspektive – hier umgekehrt)
- § 850b ZPO – bedingt pfändbare Bezüge (Renten aus Versicherung, Schmerzensgeld)
- § 46 AO – Steueranspruchsabtretung und -pfändung
- § 54 SGB I – Pfändbarkeit Sozialleistungen
- §§ 21, 22 EStG mittelbar (Mietzins als Forderung)

## Workflow

1. **Drei-Säulen-Prüfung**.
2. **Drittschuldner exakt bezeichnen**: Mieter (Vor- und Nachname), Finanzamt mit zuständiger Behörde, Versicherungs-AG mit Sitz.
3. **Forderung definieren**:
 - Mietzins: laufender Anspruch des Vermieters gegen den Mieter aus Mietvertrag vom DD.MM.JJJJ, einschließlich Nebenkostennachzahlungen, einschließlich künftiger Mieten.
 - Finanzamt: alle Einkommensteuer-Erstattungsansprüche des Schuldners für VZ x ff., einschließlich Solidaritätszuschlag.
 - Versicherung: Rückkaufswert oder fällige Leistungen aus Police Nr. x.
4. **Pfändungsverbote prüfen**:
 - § 851 ZPO: unübertragbare Forderungen
 - § 850b ZPO: Sterbegeld, Schmerzensgeld – nur eingeschränkt pfändbar
 - § 54 SGB I: Kindergeld nur für Unterhalt des Kindes pfändbar
5. **Vollstreckungsgericht**: Wohnsitz Schuldner (§ 828 Abs. 2 ZPO).
6. **Antrag** auf ZVFV-Formular, ab 1.10.2026 XML-Antrag.
7. **Zustellung** an Drittschuldner durch GV oder ab 1.10.2027 elektronisch (sofern Behörde/Unternehmen Postfach eröffnet).
8. **Drittschuldnererklärung § 840 ZPO** abwarten.
9. **Bei Finanzamt-Pfändung**: parallele Abtretungsanzeige nach § 46 AO ist verfahrensmäßig oft schneller, aber rechtlich anders zu bewerten – Mandanten beraten.

## Sonderfall Mieter als Drittschuldner

Pfändung der Mietforderung. Wichtige Punkte:

- Der Mieter darf nach Pfändung nur noch an den Gläubiger zahlen.
- Der Mieter kann mit eigenen Gegenforderungen gegen den Vermieter aufrechnen, soweit § 392 BGB nichts entgegensteht.
- Mietminderung bleibt möglich, Pfändung erfasst nur den tatsächlich geschuldeten Betrag.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Sonderfall Steuererstattung

- § 46 AO regelt Abtretung und Pfändung. Anzeige beim Finanzamt zwingend.
- Erfasst werden Erstattungsansprüche für laufenden VZ und künftige – soweit hinreichend bestimmt.
- Vorauszahlungen sind keine Erstattung, sondern Vorleistung.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Leitentscheidungen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ausgabeformat

```
PFÜB SONSTIGER DRITTSCHULDNER [Mandant] / [Schuldner]

Titel: [Art, Datum, Aussteller]
Forderung Schuldner: EUR Haupt + EUR Zinsen + EUR Kosten
Drittschuldner: [Mieter / Finanzamt / Versicherung / Geschäftspartner]
Gepfändete Forderung: [genaue Bezeichnung mit Rechtsgrund und Zeitraum]
Pfändungsverbote: [§ 851 / § 850b / § 54 SGB I geprüft]
Zustellungsweg: GV Papier / eBO / ab 1.10.2027 ggf. elektronisch

NÄCHSTER SCHRITT: Drittschuldnererklärung
WIEDERVORLAGE: DD.MM.JJJJ
```

## Qualitätsgates

- Niemals unpfändbare Forderungen pfänden (§ 851 ZPO – Sozialhilfe nicht abgrenzbar).
- Niemals Kindergeld pfänden, außer für privilegierte Unterhaltsforderung.
- Bei Steuererstattung: Zeitraum konkret nennen, sonst Pfändung zu unbestimmt.
- Bei Mietzins: Mieter darf nicht doppelt zahlen – schriftliche Aufforderung an Mieter zur Zahlung an Gläubiger.

## Querverweise

- `zv-titel-klausel-zustellung`
- `zv-pfueb-bank`, `zv-pfueb-arbeitsentgelt`
- `zv-elektronische-zustellung-2027`
- `zv-vermoegensauskunft-gv` – wenn Forderungen unbekannt
- `zv-kontensuche-drittschuldner`

## 2. `spezial-802l-verhandlung-vergleich-und-eskalation`

**Fokus:** 802L: Verhandlung, Vergleich und Eskalation im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# 802L: Verhandlung, Vergleich und Eskalation

## Spezialwissen: 802L: Verhandlung, Vergleich und Eskalation
- **Spezialgegenstand:** 802L: Verhandlung, Vergleich und Eskalation / 802l verhandlung vergleich und eskalation. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **802L** prüfen.
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

## 3. `spezial-arbeit-schriftsatz-brief-und-memo-bausteine`

**Fokus:** Arbeit: Schriftsatz-, Brief- und Memo-Bausteine im Plugin zwangsvollstreckung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Arbeit: Schriftsatz-, Brief- und Memo-Bausteine

## Spezialwissen: Arbeit: Schriftsatz-, Brief- und Memo-Bausteine
- **Spezialgegenstand:** Arbeit: Schriftsatz-, Brief- und Memo-Bausteine / arbeit schriftsatz brief und memo bausteine. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Arbeit** prüfen.
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
