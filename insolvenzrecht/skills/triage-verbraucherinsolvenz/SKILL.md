---
name: triage-verbraucherinsolvenz
description: "Triage Verbraucherinsolvenz: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Triage Verbraucherinsolvenz

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Triage Verbraucherinsolvenz** im Plugin Insolvenzrecht (InsO). Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-triage-mandantenkommunikation-entscheidungsvorlage` | Triage: Mandantenkommunikation und Entscheidungsvorlage im Insolvenzrecht: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/GesR), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `spezial-verbraucherinsolvenz-mehrparteienkonflikt` | Verbraucherinsolvenz: Mehrparteienkonflikt und Interessenmatrix im Insolvenzrecht: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/GesR), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `spezial-zahlungsunfaehigkeit-tatbestand-beweis-und-belege` | Zahlungsunfaehigkeit: Tatbestandsmerkmale, Beweisfragen und Beleglage im Insolvenzrecht: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/GesR), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt. |
| `ueberschuldung-pruefung-19-inso` | Führt die zweistufige Überschuldungsprüfung gem. § 19 Abs. 2 InsO durch: Fortbestehensprognose (Stufe 1) und insolvenzrechtlicher Überschuldungsstatus auf Liquidationswertbasis (Stufe 2). Lädt, wenn Überschuldung geprüft, ein Überschuldungsstatus erstellt oder § 19 InsO ausgelegt werden soll. |

## Arbeitsweg

Im Plugin Insolvenzrecht (InsO) gilt für **Triage Verbraucherinsolvenz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-triage-mandantenkommunikation-entscheidungsvorlage`

**Fokus:** Triage: Mandantenkommunikation und Entscheidungsvorlage im Insolvenzrecht: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/GesR), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Triage: Mandantenkommunikation und Entscheidungsvorlage

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Triage: Mandantenkommunikation und Entscheidungsvorlage` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Triage: Mandantenkommunikation und Entscheidungsvorlage
- **Spezialgegenstand:** Triage: Mandantenkommunikation und Entscheidungsvorlage / triage mandantenkommunikation entscheidungsvorlage. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Triage** prüfen.
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

## 2. `spezial-verbraucherinsolvenz-mehrparteienkonflikt`

**Fokus:** Verbraucherinsolvenz: Mehrparteienkonflikt und Interessenmatrix im Insolvenzrecht: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/GesR), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Verbraucherinsolvenz: Mehrparteienkonflikt und Interessenmatrix

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Verbraucherinsolvenz: Mehrparteienkonflikt und Interessenmatrix` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Verbraucherinsolvenz: Mehrparteienkonflikt und Interessenmatrix
- **Spezialgegenstand:** Verbraucherinsolvenz: Mehrparteienkonflikt und Interessenmatrix / verbraucherinsolvenz mehrparteienkonflikt. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Verbraucherinsolvenz** prüfen.
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

## 3. `spezial-zahlungsunfaehigkeit-tatbestand-beweis-und-belege`

**Fokus:** Zahlungsunfaehigkeit: Tatbestandsmerkmale, Beweisfragen und Beleglage im Insolvenzrecht: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/GesR), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

# Zahlungsunfaehigkeit: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zahlungsunfaehigkeit: Tatbestandsmerkmale, Beweisfragen und Beleglage` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: Zahlungsunfaehigkeit: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Spezialgegenstand:** Zahlungsunfaehigkeit: Tatbestandsmerkmale, Beweisfragen und Beleglage / zahlungsunfaehigkeit tatbestand beweis und belege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** einschlägige Fachnormen, Behördenhinweise, Formulare, Verfahrensrecht und frei prüfbare Rechtsprechung live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Zahlungsunfaehigkeit** prüfen.
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

## Zahlungsunfähigkeit § 17 InsO — Tatbestandsmerkmale

- **§ 17 Abs. 2 S. 1 InsO:** Zahlungsunfähigkeit liegt vor, wenn der Schuldner nicht in der Lage ist, die fälligen Zahlungspflichten zu erfüllen.
- **§ 17 Abs. 2 S. 2 InsO Vermutung:** Zahlungsunfähigkeit wird in der Regel angenommen bei **Zahlungseinstellung** (objektives Verhalten — Nichtzahlung an mehrere Gläubiger, Lohn, Steuer, Sozialversicherung).
- **BGH-Linie zur 10-Prozent-Schwelle / 3-Wochen-Liquiditätslücke (verifizierungspflichtig):**
 - Schuldner ist zahlungsfähig, wenn er die Liquiditätslücke binnen 3 Wochen schließen kann.
 - Liquiditätslücke < 10 Prozent regelmäßig unbedenklich (Zahlungsstockung).
 - Liquiditätslücke ≥ 10 Prozent über 3 Wochen → Indiz für Zahlungsunfähigkeit.
 - Beweislast: Schuldner muss zeigen, dass er die Lücke schließen kann (Substantiierungslast).

## Liquiditätsstatus zum Stichtag — Methodik

| Position | Betrag | Anmerkung |
|---|---|---|
| Liquide Mittel (Kasse, Bank, Tagesgeld) | + | Stichtag |
| Innerhalb 3 Wochen verfügbar (eingehende Forderungen) | + | OPOS-Liste mit Fälligkeit |
| Verfügbare Kreditlinien | + | nur, wenn nicht ausgeschöpft und ungekündigt |
| **Aktiva I (verfügbare Mittel)** | **= A** | |
| Fällige Verbindlichkeiten zum Stichtag | + | OPOS-Liste mit Fälligkeit |
| Innerhalb 3 Wochen fällig | + | Lohn, Steuer, SV, Lieferanten |
| **Passiva I (fällige Verbindlichkeiten)** | **= P** | |
| **Liquiditätslücke = P − A** | | Quote = (P − A) / P |

- Quote ≥ 10 Prozent und nicht schließbar → Zahlungsunfähigkeit.
- Quote < 10 Prozent oder Lücke binnen 3 Wochen schließbar → Zahlungsstockung.

## Beweisfragen und Belegbedarf

- **Schuldner / Geschäftsführer (haftungsabschirmend):** Liquiditätsstatus zum konkreten Stichtag mit Datum, Annahmen, Berechnung.
- **Insolvenzverwalter / Gläubiger (zur Antragstellung):** Belege für Zahlungseinstellung — Mahnungen, Vollstreckungsbescheide, Wechselproteste, Eidesstattliche Versicherung des Schuldners.
- **Indizien für Zahlungseinstellung:**
 - Stundungsverhandlungen mit mehreren Gläubigern.
 - Nichtabführen Sozialversicherungsbeiträge (§ 266a StGB!).
 - Vorinsolvenzliche Pfändungs- und Überweisungsbeschlüsse.
 - Kreditkündigungen.

## Risikoampel
- **ROT:** Lücke ≥ 10 Prozent über 3 Wochen, keine substantiierte Schließungsperspektive → ZU § 17 InsO + Antragspflicht § 15a InsO (3 Wochen ab Eintritt).
- **GELB:** Lücke < 10 Prozent oder kurzfristig schließbar → Zahlungsstockung, Frühwarnsystem aktivieren.
- **GRÜN:** Liquidität gedeckt mit Reserve, Kovenanten eingehalten.

## 4. `ueberschuldung-pruefung-19-inso`

**Fokus:** Führt die zweistufige Überschuldungsprüfung gem. § 19 Abs. 2 InsO durch: Fortbestehensprognose (Stufe 1) und insolvenzrechtlicher Überschuldungsstatus auf Liquidationswertbasis (Stufe 2). Lädt, wenn Überschuldung geprüft, ein Überschuldungsstatus erstellt oder § 19 InsO ausgelegt werden soll.

# Zweistufige Überschuldungsprüfung gem. § 19 Abs. 2 InsO

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Zweistufige Überschuldungsprüfung gem. § 19 Abs. 2 InsO` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Zweck

Dieser Skill leitet die strukturierte Prüfung durch, ob bei einer Kapitalgesellschaft
(insb. GmbH, UG, AG) Überschuldung i.S.d. § 19 Abs. 2 InsO als Insolvenzantragspflicht-
auslösender Eröffnungsgrund vorliegt. Er klärt den modifizierten zweistufigen
Überschuldungsbegriff, benennt die Prüfungsschritte, stellt Hinweise zur Dokumentation
bereit und warnt vor den häufigsten Bewertungsfehlern.

Wichtig: Die Fortbestehensprognose ist nicht dasselbe wie volle Sanierungsfähigkeit. Sie
prüft für § 19 InsO, ob die Zahlungsfähigkeit im Prognosezeitraum überwiegend wahrscheinlich
erhalten bleibt. Ein Sanierungskonzept geht weiter und muss Krisenursachen, Leitbild,
Maßnahmen, integrierte GuV-/Bilanz-/Liquiditätsplanung, Szenarien und Dokumentation
zusammenführen.

## Eingaben

- Jahresabschluss oder aktuelle BWA (Bilanz, GuV) des Unternehmens
- Liquiditätsplanung (Plan-GuV, Plan-Bilanz, Liquiditätsplan) — zumindest als Entwurf
- Liste der Verbindlichkeiten inkl. Rangangaben (insb. Gesellschafterdarlehen)
- Angaben zu Eventualverbindlichkeiten (Bürgschaften, Haftungsrisiken)
- Unternehmenskonzept / Sanierungsplan (sofern vorhanden)
- Stichtag der Prüfung

## Rechtlicher Rahmen

### Gesetzliche Grundlage

§ 19 Abs. 2 Satz 1 InsO definiert Überschuldung: Das Vermögen des Schuldners deckt die
bestehenden Verbindlichkeiten nicht mehr, es sei denn, die Fortführung des Unternehmens
ist nach den Umständen überwiegend wahrscheinlich. Antragspflicht gem. § 15a Abs. 1 InsO
tritt bei Überschuldung grundsätzlich innerhalb von sechs Wochen ein.

### Historische Entwicklung und aktueller Stand

Der modifizierte zweistufige Überschuldungsbegriff wurde durch das MoMiG 2008 eingeführt
und durch das SanInsFoG / StaRUG (2021) sowie das SanInsKG (2022/2023) weiterentwickelt.
Das SanInsKG verkürzte den Prognosezeitraum krisenbedingt auf vier Monate (befristete
Sonderregel, galt bis 31.12.2023). Seit 01.01.2024 gilt wieder der Regelzeitraum von
zwölf Monaten. Zum Stichtag 18.05.2026 beträgt der Prognosezeitraum zwölf Monate.

### Rechtsprechung (Pflichtpinpoints; Az. und Datum vor Ausgabe über dejure.org / openjur.de verifizieren)

**Fortbestehensprognose:** Anforderungen an die Prognoseentscheidung (st. BGH-Linie): plausibler Liquiditätsplan mit nachvollziehbaren Planungsannahmen erforderlich; bloße Hoffnung auf künftige Kapitalzuführungen genügt nicht; maßgeblich ist überwiegende Wahrscheinlichkeit der Zahlungsfähigkeitserhaltung im Prognosezeitraum (12 Monate seit 01.01.2024). Unrealistische Annahmen entwerten die Prognose insgesamt.

**Insolvenzrechtliche Überschuldung:** Im Überschuldungsstatus sind nicht handelsbilanzielle Buchwerte, sondern Liquidations- bzw. Zerschlagungswerte anzusetzen; bei negativer Fortbestehensprognose auch stille Reserven und immaterielle Vermögensgegenstände zu Zerschlagungswerten.

**Abgrenzung handelsbilanzieller vs. insolvenzrechtlicher Überschuldung:** Negative Handelsbilanz indiziert mögliche insolvenzrechtliche Überschuldung, begründet sie aber nicht zwingend. Positives HGB-Eigenkapital schließt umgekehrt eine insolvenzrechtliche Überschuldung nicht aus, wenn Vermögensgegenstände zu Fortführungswerten überhöht aktiviert sind.

**Qualifizierter Rangrücktritt:** Nur ein qualifizierter Rangrücktritt (Erfüllung beschränkt auf das freie, die sonstigen Verbindlichkeiten übersteigende Vermögen) bewirkt das Ausscheiden aus dem Überschuldungsstatus iSd § 19 Abs. 2 S. 2 InsO. Einfacher Rangrücktritt genügt nicht.

Hinweis: Aktenzeichen und Randnummern der einschlägigen BGH-Entscheidungen (zur Fortbestehensprognose, Liquidationswerten, Rangrücktritt) vor Ausgabe in offener Quelle (dejure.org, openjur.de, bundesgerichtshof.de) prüfen.

### Quellen (nur verifiziert)

- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
 (umfassend zur Prüfungsreihenfolge, zum modifizierten Überschuldungsbegriff und zur
 Behandlung nachrangiger Verbindlichkeiten)
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
 (Bewertungsmethodik Liquidationswerte, Gesellschafterdarlehen, Pensionsrückstellungen)
### Berufsständische Methodenlogik

Für Überschuldungsstatus und Fortbestehensprognose ist ein integrierter Finanzplan
erforderlich: Plan-GuV, Plan-Bilanz und Liquiditätsplan müssen zusammenpassen. Wenn
die Prüfung zugleich eine Sanierungsaussage tragen soll, sind zusätzlich die Bausteine
eines Sanierungskonzepts zu prüfen: Ausgangslage, Krisenstadium, Krisenursachen, Leitbild,
Maßnahmen, integrierte Planung, Szenarien, Sanierungsfähigkeit und Dokumentation.

## Ablauf

### Schritt 1 — Fortbestehensprognose (Stufe 1)

**1.1 Unternehmenskonzept prüfen**
Ist ein schlüssiges Unternehmenskonzept (Fortführungsstrategie, Geschäftsmodell,
Absatzplanung) vorhanden und plausibel? Ohne Konzept kann keine positive Prognose
gestellt werden.

Wenn Sanierungsfähigkeit behauptet wird, zusätzlich prüfen: Sind die wesentlichen
Krisenursachen nach Maßnahmen beseitigt oder beherrschbar? Ist das Unternehmen nach
Umsetzung wieder wettbewerbs-, rendite- und finanzierungsfähig? Eine bloße
Liquiditätsverlängerung genügt dafür nicht.

**1.2 Integrierten Finanzplan erstellen**
- Plan-GuV für die kommenden zwölf Monate (Regelzeitraum ab 01.01.2024)
- Plan-Bilanz zu den relevanten Stichtagen
- monatlicher Liquiditätsplan (Mittelzuflüsse, Mittelabflüsse, Saldo)
- Maßnahmenlog mit Kosten, Timing, Verantwortlichen, Bilanz-/GuV-/Liquiditätseffekt und Belegstatus, sofern Sanierungsfähigkeit beurteilt wird.

**1.3 Prognoseurteil**
Maßgebliches Kriterium: überwiegende Wahrscheinlichkeit (> 50 %) der Aufrechterhaltung
der Zahlungsfähigkeit im Prognosezeitraum. Die Planungsannahmen sind zu plausibilisieren
(Marktdaten, Auftragsbestand, gesicherte Finanzierungszusagen). Externe Gutachter
(Wirtschaftsprüfer, Unternehmensberater) sind hinzuzuziehen, wenn interne Kompetenz fehlt
(vgl. IDW S 11 Tz. 56 ff.).

→ **Positive Prognose**: Keine Überschuldung i.S.d. § 19 Abs. 2 InsO — Prüfung endet hier.
→ **Negative Prognose** (oder Prognose nicht mit überwiegender Wahrscheinlichkeit positiv):
 Weiter mit Schritt 2.

### Schritt 2 — Insolvenzrechtlicher Überschuldungsstatus (Stufe 2)

**2.1 Aktivseite zu Liquidationswerten bewerten**
Sämtliche Vermögensgegenstände sind zu Zerschlagungswerten (Liquidationswerten) zu
erfassen — nicht zu HGB-Buchwerten oder Fortführungswerten. Typische Abweichungen:
- Immobilien: Verkehrswert abzgl. Verwertungskosten und Zeitdruck-Abschlag
- Maschinen/Anlagen: Gebrauchtmarktwert, ggf. erheblich unter Buchwert
- Forderungen: unter Berücksichtigung von Ausfallwahrscheinlichkeiten
- Immaterielle Werte (Patente, Kundenstamm): oft stark gemindert oder null
- Latente Steueransprüche: nur ansetzen, soweit bei Liquidation realisierbar

**2.2 Passivseite vollständig erfassen**
- Sämtliche Verbindlichkeiten inkl. nachrangiger Forderungen gem. § 39 InsO
 (insb. Gesellschafterdarlehen)
- Eventualverbindlichkeiten (Bürgschaften, Garantien) nach Wahrscheinlichkeitsbewertung
- Pensionsrückstellungen: versicherungsmathematisch ermittelt, nicht HGB-Abzinsung
- Latente Steuerschulden aus stillen Reserven
- **Ausnahme § 19 Abs. 2 Satz 2 InsO**: Verbindlichkeiten mit qualifiziertem Rangrücktritt
 (Erfüllung ausdrücklich nur aus freiem, die übrigen Verbindlichkeiten übersteigendem
 Vermögen zugesagt) sind aus der Passivseite herauszulassen.

**2.3 Saldierung und Ergebnis**
Übersteigen die Passiva die Aktiva (Liquidationswerte), liegt rechnerische Überschuldung vor.
Dokumentation im Überschuldungsstatus (tabellarische Gegenüberstellung).

**2.4 Gesamtergebnis und Handlungspflichten**
Bei Überschuldung: Antragspflicht gem. § 15a Abs. 1 InsO — Frist grundsätzlich sechs Wochen.
Parallel prüfen: Zahlungsunfähigkeit gem. § 17 InsO und drohende Zahlungsunfähigkeit
gem. § 18 InsO.

## Ausgabeformat

Erstelle ein strukturiertes Gutachten mit folgenden Abschnitten:

```
I. Sachverhalt und Prüfungsanlass
II. Fortbestehensprognose
 1. Unternehmenskonzept
 2. Finanzplanung (tabellarisch: Monat 1–12, Liquiditätssaldo)
 3. Prognoseergebnis mit Begründung
III. Überschuldungsstatus (bei negativer Prognose)
 Aktiva (Liquidationswerte) EUR
 ─────────────────────────────────────────
 Anlagevermögen ...
 Umlaufvermögen ...
 Sonstige Aktiva ...
 Summe Aktiva ...
 ─────────────────────────────────────────
 Passiva
 Verbindlichkeiten (gesamt) ...
 ./. qualif. Rangrücktritt ...
 Summe Passiva (maßgeblich) ...
 ─────────────────────────────────────────
 Saldo (Unter-/Überdeckung) ...
IV. Rechtliches Ergebnis
V. Handlungsempfehlung (Antragspflicht, Sanierungsoptionen)
```

Quellenangaben in Fußnoten oder am Ende des Gutachtens.

## Beispiel

**Sachverhalt:** Die XY GmbH, Maschinenbau, weist zum 30.04.2026 in der Handelsbilanz
ein negatives Eigenkapital von –180.000 EUR aus. Der Geschäftsführer beauftragt eine
Überschuldungsprüfung nach § 19 Abs. 2 InsO.

---

**Gutachten (Auszug)**

**I. Sachverhalt**
Die XY GmbH (Stammkapital 25.000 EUR) erwirtschaftete im Geschäftsjahr 2025 einen
Jahresfehlbetrag von 230.000 EUR. Der Auftragsbestand ist rückläufig; Hauptkunde (40 %
Umsatz) hat Vertrag zum 30.06.2026 gekündigt.

**II. Fortbestehensprognose (Stufe 1)**

Unternehmenskonzept: Kein schlüssiges Restrukturierungskonzept vorhanden. Kostensenkungsmaßnahmen
erst in Planung, keine gesicherten Alternativaufträge. Gesellschafter hat keine verbindliche
Finanzierungszusage abgegeben.

Plan-Cashflow (12 Monate, stark vereinfacht):

| Monat | Einzahlungen | Auszahlungen | Saldo monatl. | Kumuliert |
|-------|-------------|--------------|---------------|-----------|
| Mai 26 | 85.000 | 110.000 | –25.000 | –25.000 |
| Jun 26 | 60.000 | 108.000 | –48.000 | –73.000 |
| … | … | … | … | … |
| Apr 27 | 55.000 | 105.000 | –50.000 | –420.000 |

→ Kumulierter Liquiditätssaldo nach 12 Monaten: **–420.000 EUR**
→ Ergebnis Stufe 1: **Negative Fortbestehensprognose.** Die Zahlungsfähigkeit kann im
 Prognosezeitraum (12 Monate) nicht mit überwiegender Wahrscheinlichkeit aufrechterhalten
 werden. Prüfung Stufe 2 ist durchzuführen.

**III. Überschuldungsstatus zu Liquidationswerten (Stufe 2)**

| Aktiva (Liquidationswerte) | EUR |
|------------------------------------------------|------------|
| Grundstück/Gebäude (Verkehrswert –15 %) | 320.000 |
| Maschinen/Anlagen (Gebrauchtmarktwert) | 180.000 |
| Vorräte (Liquidationsabschlag 40 %) | 90.000 |
| Forderungen (Ausfallabschlag 25 %) | 180.000 |
| Kassenbestand / Bankguthaben | 80.000 |
| **Summe Aktiva** |**850.000** |

| Passiva | EUR |
|------------------------------------------------|------------|
| Bankverbindlichkeiten | 600.000 |
| Lieferantenverbindlichkeiten | 150.000 |
| Steuerverbindlichkeiten | 80.000 |
| Pensionsrückstellungen (versicherungsmath.) | 120.000 |
| Gesellschafterdarlehen (§ 39 InsO-Nachrang, | |
| OHNE qualifizierten Rangrücktritt) | 200.000 |
| **Summe Passiva** |**1.150.000**|

| **Saldo (Unterdeckung)** |**–300.000**|

→ Ergebnis Stufe 2: **Rechnerische Überschuldung** i.H.v. 300.000 EUR.

**IV. Rechtliches Ergebnis**
Die XY GmbH ist überschuldet i.S.d. § 19 Abs. 2 InsO. Der Insolvenzantragspflicht
nach § 15a Abs. 1 InsO ist innerhalb von sechs Wochen nachzukommen, sofern keine
Beseitigung der Überschuldung (z.B. Kapitalzuführung, Rangrücktritt mit qualifizierter
Ausgestaltung) erfolgt.

## Risiken und typische Fehler

**Fehler 1 — HGB-Buchwerte statt Liquidationswerte**
Der häufigste Fehler: Der Überschuldungsstatus wird mit handelsbilanziellen Buchwerten
erstellt. Das ist unzulässig. Bei negativer Fortbestehensprognose sind ausnahmslos
Liquidations- bzw. Zerschlagungswerte anzusetzen (st. BGH-Linie; Az. vor Ausgabe verifizieren). Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle.

**Fehler 2 — Einfacher statt qualifizierter Rangrücktritt bei Gesellschafterdarlehen**
Ein Gesellschafterdarlehen mit einfachem Rangrücktritt bleibt Passivposten im
Überschuldungsstatus. Nur der qualifizierte Rangrücktritt (Erfüllung ausschließlich
aus freiem, die übrigen Verbindlichkeiten übersteigendem Vermögen) führt gem.
§ 19 Abs. 2 S. 2 InsO zum Ausscheiden aus dem Status (st. BGH-Linie; konkretes Az. vor Ausgabe verifizieren).

**Fehler 3 — Mangelhafte Fortbestehensprognose ohne Plausibilisierung**
Eine Fortbestehensprognose, die sich auf pauschale Hoffnungen oder ungesicherte
Finanzierungsabsichten stützt, ist rechtlich wertlos. Erforderlich sind integrierte
Finanzplanungen mit nachvollziehbaren Annahmen, die einer Plausibilitätsprüfung
standhalten (st. BGH-Linie; Az. vor Ausgabe verifizieren).

**Fehler 4 — Pensionsrückstellungen und latente Steuern falsch angesetzt**
Pensionsrückstellungen sind versicherungsmathematisch (nicht nach HGB-Abzinsung) zu
bewerten. Latente Steueransprüche sind nur insoweit aktivierbar, als sie bei Liquidation
tatsächlich realisierbar sind; latente Steuerschulden aus stillen Reserven müssen passiviert
Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.

**Fehler 5 — Eventualverbindlichkeiten vergessen**
Bürgschaften, Haftungsübernahmen und sonstige Eventualverbindlichkeiten müssen nach
Inanspruchnahmewahrscheinlichkeit bewertet und passiviert werden. Ihr Fehlen im Status
führt zu systematischer Untererfassung der Passiva.

**Fehler 6 — Prognosezeitraum verwechselt**
Seit 01.01.2024 gilt wieder der 12-Monats-Zeitraum. Die SanInsKG-Verkürzung auf
vier Monate ist ausgelaufen. Prognosezeitraum-Fehler infizieren die gesamte Prüfung.

**Fehler 7 — Fortbestehensprognose mit Sanierungskonzept verwechseln**
Eine positive Liquiditätsprognose beseitigt den Überschuldungsgrund, beweist aber noch
nicht, dass das Geschäftsmodell dauerhaft saniert ist. Für Sanierungsfähigkeit sind
Krisenursachen, Leitbild, Maßnahmen, integrierte Planung, Sensitivitäten und Nachweise
gesondert zu dokumentieren.

## Quellenpflicht

Jede Aussage zu Prüfungsmaßstäben, Bewertungsmethoden oder Rechtsfolgen ist zu belegen.
Mindeststandard:

- Grundlegende BGH-Linie zu Anforderungen an die Fortbestehensprognose (Plausibilität, Liquiditätsplanung): Aktenzeichen und Datum vor Ausgabe über dejure.org / openjur.de verifizieren.
- BGH-Linie zur Bewertung im Überschuldungsstatus (Liquidationswerte, stille Reserven): Az. vor Ausgabe verifizieren.
- BGH-Linie zur Abgrenzung handels- vs. insolvenzrechtliche Überschuldung: Az. vor Ausgabe verifizieren.
- Grundlegende BGH-Linie zum qualifizierten Rangrücktritt nach § 19 Abs. 2 S. 2 InsO: Az. vor Ausgabe verifizieren.
- **BGH IX ZR 285/14 vom 26.01.2017** (Steuerberater-Hinweispflicht) und **BGH IX ZR 56/22 vom 29.06.2023** (Drittschutz) relevant für die Berater-Position bei Erstellung der Prognose.
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=26.01.2017&Aktenzeichen=IX+ZR+285/14>
 <https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=29.06.2023&Aktenzeichen=IX+ZR+56/22>
- Quellenregel: Keine Kommentar-, Handbuch-, Aufsatz- oder Tabellenfundstellen aus Modellwissen; nur Nutzerquelle, amtliche/freie Quelle oder lizenzierte Live-Verifikation verwenden.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Berufsständischer Methodenrahmen zu Insolvenzeröffnungsgründen und Sanierungskonzepten nur als Arbeitsmaßstab; keine Literaturfundstellen ohne Nutzerquelle oder lizenzierten Live-Zugriff.

---
*Dieser Skill ersetzt keine konkrete anwaltliche Beratung im Einzelfall.*


## Triage — Ueberschuldungs-Pruefung § 19 InsO

Bevor losgelegt wird, klaere:

1. **Bilanzieller Status?** Aktiva kleiner als Passiva auf Basis von Fortfuehrungswerten (erste Stufe)?
2. **Stille Reserven?** Grundstuecke, Beteiligungen, Patente zum Verkehrswert hoeher als Buchwert?
3. **Sanierungsmassnahmen einbezogen?** Rangruecktritt, Patronatserklaerung, Kapitalzufuhr — bereits wirksam oder nur geplant?
4. **Fortbestehensprognose positiv?** Dann keine Ueberschuldung trotz negativem Reinvermoegen (§ 19 Abs. 2 S. 1 InsO).
5. **Frist?** Ueberschuldung erkannt → Antragspflicht § 15a InsO: 6 Wochen.

## Output-Template Ueberschuldungs-Memo

**Adressat:** Geschaeftsfuehrung / Insolvenzgericht — Tonfall: sachlich-betriebswirtschaftlich

```
UEBERSCHULDUNGSSTATUS nach § 19 InsO
Gesellschaft: [FIRMA] Stichtag: [DATUM]

STUFE 1 — BILANZIELLER STATUS (Fortfuehrungswerte)
Aktiva (Verkehrswerte): EUR [BETRAG]
- Sachanlagen: EUR [...]
- Forderungen: EUR [...]
- Liquide Mittel: EUR [...]
Passiva: EUR [BETRAG]
- Eigenkapital: EUR [...]
- Fremdkapital: EUR [...]
BILANZIELLES REINVERMOEGEN: EUR [positiv / negativ]

STUFE 2 — FORTBESTEHENSPROGNOSE
Ergebnis Prognose: [POSITIV / NEGATIV]
Grundlage: [IDW S 11 / Eigenprognose / Liquiditaetsplanung]

ERGEBNIS:
[Ueberschuldung i.S.d. § 19 InsO: JA / NEIN]
[Antragspflicht: JA ab [DATUM] / NEIN]
```
