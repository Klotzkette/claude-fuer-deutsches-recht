---
name: beschlagnahme-oeffentliche-lasten
description: "Beschlagnahme Oeffentliche Lasten: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Beschlagnahme Oeffentliche Lasten

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Beschlagnahme Oeffentliche Lasten** im Plugin Zwangsverwaltung (ZVG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin zwangsverwaltung-zvg: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `spezial-beschlagnahme-fristen-form-und-zustaendigkeit` | Beschlagnahme: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin zwangsverwaltung zvg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `zvg-oeffentliche-lasten` | Öffentliche Lasten und grundstuecksbezogene Abgaben in der Zwangsverwaltung. Anwendungsfall Grundsteuer Erschließungsgebuhren oder Beitraege werden fällig und Zwangsverwalter muss prüfen ob und in welchem Rang zu zahlen ist. Normen § 10 ZVG Rangklassen § 12 GrStG Grundsteuerschuldner § 155 ZVG Ausgaben. Prüfraster Grundsteuer Abgaben Rang Fälligkeiten Zahlung Nachweis Belegpflicht. Output Lasten-Übersicht mit Rangfolge Zahlungsplan und Nachweis für Gerichtsbericht. Abgrenzung zu zvg-konten-kassenführung und zvg-rechnungslegung. |

## Arbeitsweg

Im Plugin Zwangsverwaltung (ZVG) gilt für **Beschlagnahme Oeffentliche Lasten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin zwangsverwaltung-zvg: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin zwangsverwaltung-zvg: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

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

## 2. `spezial-beschlagnahme-fristen-form-und-zustaendigkeit`

**Fokus:** Beschlagnahme: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin zwangsverwaltung zvg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Beschlagnahme: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Beschlagnahme: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Beschlagnahme: Fristen, Form, Zuständigkeit und Rechtsweg / beschlagnahme fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** ZVG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Beschlagnahme** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Materielle Weichen Beschlagnahme im ZVG
- **Wirkung der Beschlagnahme (§ 20 ZVG):** Mit der Beschlagnahme erfasst werden Grundstück mit Bestandteilen und Zubehör (§ 21 ZVG), Mietzinsen/Pachtzinsen und sonstige Nutzungen (§ 21 Abs. 2 ZVG). Verfügungsverbot zugunsten der Gläubiger (§ 23 ZVG): Eigentümer darf nicht mehr veräußern oder belasten; Verfügungen sind relativ unwirksam.
- **Beginn der Beschlagnahme (§ 22 ZVG):** Mit Zustellung des Anordnungsbeschlusses an den Schuldner; bei Anordnung der Zwangsverwaltung mit Inbesitznahme durch den Verwalter.
- **Eintragung im Grundbuch (§ 19 Abs. 2 ZVG):** Versteigerungsvermerk wird als Sicherungseintragung von Amts wegen im Grundbuch eingetragen; macht die Beschlagnahme öffentlich.
- **Schutzwirkung Beschlagnahme:** Vor der Beschlagnahme bestehende Rechte bleiben in der Rangfolge unverändert; nach Beschlagnahme erworbene Rechte sind gegenüber dem Versteigerungserlös in der Rangfolge nachrangig (§ 23 ZVG).
- **Mieter und neue Mietverträge (§ 57b ZVG):** Vor Beschlagnahme abgeschlossene Mietverträge bestehen fort. Nach Beschlagnahme abgeschlossene Verträge dürfen nicht zu Lasten der Berechtigten gehen (§ 57b ZVG); Wirkungslosigkeit gegenüber Gläubigern, soweit nachteilig.
- **Vereinbarungen über Miete:** Vorausverfügungen des Schuldners über Miete (z. B. Abtretung) sind nur in den Schranken des § 1124 BGB i.V.m. § 21 Abs. 2 ZVG zulässig - max. für den laufenden Mietzeitraum.
- **Aufhebung (§ 28 ZVG):** Der Schuldner kann durch Antrag die einstweilige Einstellung erreichen, wenn er glaubhaft macht, dass die Versteigerung eine unbillige Härte bedeuten würde (§ 30a ZVG - sechsmonatige Schutzfrist möglich).
- **Verhältnis zu anderen Vollstreckungen:** Pfändung von Mietzinsen ist nach Beschlagnahme grundsätzlich überholt (§ 21 Abs. 2 ZVG); andere Vollstreckungsmaßnahmen wirken nicht auf die beschlagnahmten Gegenstände.
- **Praktiker-Tipp:** Zustellung des Anordnungsbeschlusses ist die zentrale Datumsgrenze; alle danach erfolgten Verfügungen sind risikobehaftet. Im Schuldner-Beraterkontext: Anfechtungsverfahren prüfen und Antrag auf einstweilige Einstellung (§ 30a ZVG) frühzeitig stellen.

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

## 3. `zvg-oeffentliche-lasten`

**Fokus:** Öffentliche Lasten und grundstuecksbezogene Abgaben in der Zwangsverwaltung. Anwendungsfall Grundsteuer Erschließungsgebuhren oder Beitraege werden fällig und Zwangsverwalter muss prüfen ob und in welchem Rang zu zahlen ist. Normen § 10 ZVG Rangklassen § 12 GrStG Grundsteuerschuldner § 155 ZVG Ausgaben. Prüfraster Grundsteuer Abgaben Rang Fälligkeiten Zahlung Nachweis Belegpflicht. Output Lasten-Übersicht mit Rangfolge Zahlungsplan und Nachweis für Gerichtsbericht. Abgrenzung zu zvg-konten-kassenführung und zvg-rechnungslegung.

# Öffentliche Lasten und grundstücksbezogene Abgaben

## Aufgabe

Ordnet Grundsteuer, Gebühren, Beiträge und sonstige objektbezogene Lasten in der Zwangsverwaltung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Grundsteuer, Gebühren oder Beitragsbescheide eingehen
- Lasten im Besitzerlangungsbericht fehlen
- Verteilung oder Rechnungslegung vorbereitet wird

## Eingaben

- Bescheide, Lastenregister, Kontoauszüge
- Objektdaten, Grundsteuer, Gebühren, WEG-Unterlagen
- Fälligkeiten und Zahlungsnachweise

## Workflow

1. **Lasten erfassen** - Art, Zeitraum, Betrag, Fälligkeit und Behörde aufnehmen.
2. **Rang und Zweck** - öffentliche Last, Betriebskosten, Verwaltungsausgabe oder Schuldneraltlast trennen.
3. **Zahlungsplan** - Liquidität, Vorschussbedarf und Verteilungsauswirkung prüfen.
4. **Nachhalten** - Bescheide, Widerspruchsfristen und Belege ablegen.

## Ausgabe

- Lastenregister
- Zahlungsplan
- Berichtsbaustein

## Qualitätsgates

- Zeitraum sauber abgegrenzt
- Fälligkeit belegt
- Zahlung buchhalterisch zugeordnet

## Rote Schwellen

- Zwangsmaßnahmen der Kommune
- Doppelzahlung
- Beitragsbescheid mit kurzer Frist

## Interne Vorlagen

- assets/templates/versicherung-und-lasten.md
- assets/templates/konto-kassenbuch.md

## Amtliche Erstquellen

- § 3 Abs. 1 Nr. 5 ZwVwV
- § 15 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Öffentliche Lasten

§ 10 Abs. 1 Nr. 3 ZVG (Vorrang öffentlicher Lasten) → § 12 GrStG (Grundsteuerpflicht) → §§ 10-12 ZwVwV (Ausgaben und Rangfolge) → § 155 ZVG (Verteilungsplan) → § 80 AO (Steuerpflichten bei Vermögensverwaltung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Öffentliche Lasten

1. Ist die laufende Grundsteuer erfasst und im Zahlungsplan aufgenommen?
2. Bestehen Rückstände bei öffentlichen Lasten aus der Zeit vor Beschlagnahme?
3. Liegen weitere öffentliche Lasten vor (Anliegerbeiträge Erschließungskosten)?
4. Ist eine Umsatzsteueroption für das Grundstück vorhanden? (Auswirkung auf Vorsteuer)

## Ausgaben-Checkliste Öffentliche Lasten

| Posten | Fälligkeit | Betrag | Bezahlt |
|---|---|---|---|
| Grundsteuer Q1 | 15.02. | [...] | [ ] |
| Grundsteuer Q2 | 15.05. | [...] | [ ] |
| Grundsteuer Q3 | 15.08. | [...] | [ ] |
| Grundsteuer Q4 | 15.11. | [...] | [ ] |
| Erschließungs-/Anliegerbeiträge | gem. Bescheid | [...] | [ ] |
| Müllgebühren/Straßenreinigung | gem. Bescheid | [...] | [ ] |
| Kanalgebühren/Wasserversorgung | gem. Bescheid | [...] | [ ] |
