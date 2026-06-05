---
name: verteilung-zwangsverwaltung-aktenanlage
description: "Verteilung Zwangsverwaltung Aktenanlage: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Verteilung Zwangsverwaltung Aktenanlage

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Verteilung Zwangsverwaltung Aktenanlage** im Plugin Zwangsverwaltung (ZVG). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-verteilung-verhandlung-vergleich-und-eskalation` | Verteilung: Verhandlung, Vergleich und Eskalation im Plugin zwangsverwaltung zvg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-zwangsverwaltung-erstpruefung-und-mandatsziel` | Zwangsverwaltung: Erstprüfung, Rollenklärung und Mandatsziel im Plugin zwangsverwaltung zvg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `zvg-aktenanlage-objektcockpit` | Aktenanlage und Objektcockpit für den Zwangsverwalter nach §§ 146 ff. ZVG. Anwendungsfall Zwangsverwaltungsauftrag geht ein und Objekt muss komplett erfasst werden. Normen §§ 146 152 ZVG Bestellung § 154 ZVG Pflichten § 155 ZVG Einnahmen Ausgaben. Prüfraster Objektkarte Beteiligtenregister Mieterliste Lasten Treuhandkonto Fristen Berichte Wiedervorlagen. Output Vollständiges Objektcockpit als Arbeitsbasis für alle Folge-Skills der Zwangsverwaltung. Abgrenzung zu zvg-bestellung-beschlagnahme (rechtlicher Bestellvorgang) und zvg-miet-und-pachtverwaltung. |

## Arbeitsweg

Im Plugin Zwangsverwaltung (ZVG) gilt für **Verteilung Zwangsverwaltung Aktenanlage**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-verteilung-verhandlung-vergleich-und-eskalation`

**Fokus:** Verteilung: Verhandlung, Vergleich und Eskalation im Plugin zwangsverwaltung zvg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Verteilung: Verhandlung, Vergleich und Eskalation

## Spezialwissen: Verteilung: Verhandlung, Vergleich und Eskalation
- **Spezialgegenstand:** Verteilung: Verhandlung, Vergleich und Eskalation / verteilung verhandlung vergleich und eskalation. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Verteilung** prüfen.
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

## 2. `spezial-zwangsverwaltung-erstpruefung-und-mandatsziel`

**Fokus:** Zwangsverwaltung: Erstprüfung, Rollenklärung und Mandatsziel im Plugin zwangsverwaltung zvg; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Zwangsverwaltung: Erstprüfung, Rollenklärung und Mandatsziel

## Spezialwissen: Zwangsverwaltung: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Zwangsverwaltung: Erstprüfung, Rollenklärung und Mandatsziel / zwangsverwaltung erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Zwangsverwaltung** prüfen.
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

## 3. `zvg-aktenanlage-objektcockpit`

**Fokus:** Aktenanlage und Objektcockpit für den Zwangsverwalter nach §§ 146 ff. ZVG. Anwendungsfall Zwangsverwaltungsauftrag geht ein und Objekt muss komplett erfasst werden. Normen §§ 146 152 ZVG Bestellung § 154 ZVG Pflichten § 155 ZVG Einnahmen Ausgaben. Prüfraster Objektkarte Beteiligtenregister Mieterliste Lasten Treuhandkonto Fristen Berichte Wiedervorlagen. Output Vollständiges Objektcockpit als Arbeitsbasis für alle Folge-Skills der Zwangsverwaltung. Abgrenzung zu zvg-bestellung-beschlagnahme (rechtlicher Bestellvorgang) und zvg-miet-und-pachtverwaltung.

# Aktenanlage und Objektcockpit

## Aufgabe

Eröffnet eine vollständige Zwangsverwaltungsakte mit Objektkarte, Beteiligten, Rent Roll, Lasten, Konto und Berichtsterminen.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- eine neue Zwangsverwaltung übernommen wird
- Bestandsakten unvollständig sind
- Berichte und Rechnungslegung aufgebaut werden müssen

## Eingaben

- Bestellungsurkunde, Grundbuchdaten, Objektunterlagen
- Mietverträge, Betriebskosten, Versicherungen, öffentliche Lasten
- Kontodaten und Gerichtsvorgaben

## Workflow

1. **Akte aufsetzen** - Objekt, Beteiligte, Aktenzeichen, Bestallung und Zuständigkeiten erfassen.
2. **Register bauen** - Mieter/Pächter, Lasten, Verträge, Versicherungen, Dienstleister und Schlüssel erfassen.
3. **Finanzen** - Treuhandkonto, Sollmieten, Istmieten, Ausgaben und Vorschusslogik anlegen.
4. **Berichte** - Besitzerlangungsbericht, Monats- und Jahresrechnung vormerken.

## Ausgabe

- Objektkarte
- Rent Roll
- Lasten- und Versicherungsregister
- Wiedervorlagen

## Qualitätsgates

- jede Nutzungseinheit mit Sollmiete
- öffentliche Lasten separat
- Buchführung getrennt

## Rote Schwellen

- fehlende Bestallungsurkunde
- Objektzugang ungeklärt
- kein Treuhandkonto

## Interne Vorlagen

- assets/templates/zvg-objektkarte.md
- assets/templates/mieterliste-rent-roll.md

## Amtliche Erstquellen

- § 2 ZwVwV
- § 13 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Aktenanlage/Objektcockpit

§ 152 ZVG (Pflichten Zwangsverwalter) → § 153 ZVG (Nutzungen) → §§ 2-5 ZwVwV (Aufgaben Verwalter) → § 13 ZwVwV (Buchführung) → § 14 ZwVwV (Rechnungslegung) → § 154 ZVG (Gerichtliche Aufsicht) → § 159 ZVG (Aufhebung Zwangsverwaltung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Aktenanlage

Kläre bei Übernahme:
1. Liegt die vollständige Bestellungsurkunde vor? (Pflichtdokument — ohne keine Legitimation)
2. Grundbuchauszug aktuell (max. 3 Monate alt)?
3. Alle Nutzungseinheiten mit Mietverträgen erfasst?
4. Treuhandkonto bei einer Bank eröffnet und dem Gericht benannt?
5. Etwaige Vorlasten (Grundschulden Grundpfandrechte) aus Abt. III Grundbuch erfasst?

## Output-Template Objektkarte (Auszug)

```
OBJEKTKARTE — ZWANGSVERWALTUNG
Aktenzeichen Vollstreckungsgericht: [AZ]
Bestellungsurkunde vom: [DATUM]

Objekt: [ADRESSE, GRUNDBUCHBEZEICHNUNG]
Gemarkung / Flurstück: [...]
Grundbuch: Amtsgericht [X], Blatt [Y]

BETEILIGTE
Schuldner: [NAME, ADRESSE]
Gläubiger: [NAME, ADRESSE, FORDERUNG]
Vollstreckungsgericht: AG [ORT], Richter/Rechtspfleger: [NAME]
Zwangsverwalter: [NAME, BÜRO, TELEFON]

NUTZUNGSEINHEITEN
Nr. | Lage | Mieter | Nettomiete | NK-Vorauszahlung | Vertrag vom
1 | ... | ... | ... | ... | ...

TREUHANDKONTO: [BANK, IBAN]
LETZTER GERICHT-BERICHT: [DATUM]
NÄCHSTER BERICHT FÄLLIG: [DATUM]
```
