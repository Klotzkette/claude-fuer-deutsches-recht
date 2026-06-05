---
name: belegte-faellige-fmkw
description: "Belegte Faellige Fmkw: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Belegte Faellige Fmkw

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Belegte Faellige Fmkw** im Plugin Forderungsmanagement / Klagewerkstatt. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-belegte-compliance-dokumentation-und-akte` | Belegte: Compliance-Dokumentation und Aktenvermerk im Plugin forderungsmanagement klagewerkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-faellige-zahlen-schwellen-und-berechnung` | Faellige: Zahlen, Schwellenwerte und Berechnung im Plugin forderungsmanagement klagewerkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-fmkw-mandantenkommunikation-entscheidungsvorlage` | Fmkw: Mandantenkommunikation und Entscheidungsvorlage im Plugin forderungsmanagement klagewerkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Forderungsmanagement / Klagewerkstatt gilt für **Belegte Faellige Fmkw**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-belegte-compliance-dokumentation-und-akte`

**Fokus:** Belegte: Compliance-Dokumentation und Aktenvermerk im Plugin forderungsmanagement klagewerkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Belegte: Compliance-Dokumentation und Aktenvermerk

## Fachkern: Belegte: Compliance-Dokumentation und Aktenvermerk
- **Spezialgegenstand:** Belegte: Compliance-Dokumentation und Aktenvermerk wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB Anspruch/Fälligkeit/Verzug, ZPO Mahn-/Klageverfahren, HGB kaufmännische Belege, Inkassorecht, Verjährung und Zuständigkeit.
- **Entscheidende Weiche:** Nur klare, fällige, beweisbare Forderungen weitergeben; Vertrag, Leistung, Rechnung, Mahnung, Einwendungen, Verjährung und Kosten getrennt prüfen.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Belegte** prüfen.
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

## 2. `spezial-faellige-zahlen-schwellen-und-berechnung`

**Fokus:** Faellige: Zahlen, Schwellenwerte und Berechnung im Plugin forderungsmanagement klagewerkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Faellige: Zahlen, Schwellenwerte und Berechnung

## Fachkern: Faellige: Zahlen, Schwellenwerte und Berechnung
- **Spezialgegenstand:** Faellige: Zahlen, Schwellenwerte und Berechnung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB Anspruch/Fälligkeit/Verzug, ZPO Mahn-/Klageverfahren, HGB kaufmännische Belege, Inkassorecht, Verjährung und Zuständigkeit.
- **Entscheidende Weiche:** Nur klare, fällige, beweisbare Forderungen weitergeben; Vertrag, Leistung, Rechnung, Mahnung, Einwendungen, Verjährung und Kosten getrennt prüfen.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Faellige** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Materielle Weichen Fälligkeit
- **Fälligkeit (§ 271 BGB):** Im Zweifel sofort fällig (§ 271 Abs. 1 BGB). Konkret bestimmte Leistungszeit durch Vertrag, Verkehrssitte, gesetzliche Regelung. Bei Rechnung: typischerweise Fälligkeit gemäß Zahlungsbedingungen (z. B. "binnen 14 Tagen").
- **B2B-Zahlungsfristen (§ 271a BGB):** Vereinbarte Zahlungsfrist darf grundsätzlich 60 Tage nicht überschreiten (§ 271a Abs. 1 S. 1 BGB); bei Verbraucher als Schuldner sogar 30 Tage (§ 271a Abs. 1 S. 2 BGB). Überschreitung führt zur Reduktion auf das gesetzliche Maß.
- **Verzug ohne Mahnung (§ 286 Abs. 2 BGB):** Wenn (1) Leistungszeit kalendermäßig bestimmt, (2) Mahnung ist entbehrlich, (3) Schuldner ernsthaft verweigert, (4) 30 Tage nach Fälligkeit und Zugang Rechnung bei Verbrauchern bzw. ab Rechnungsdatum bei B2B (§ 286 Abs. 3 BGB).
- **Verzugszinsen:**
 - B2C: 5 Prozentpunkte über Basiszinssatz (§ 288 Abs. 1 BGB).
 - B2B: 9 Prozentpunkte über Basiszinssatz (§ 288 Abs. 2 BGB).
 - Aktuelle Werte halbjährlich (1. Januar / 1. Juli) auf bundesbank.de prüfen.
- **40-Euro-Pauschale (§ 288 Abs. 5 BGB):** Bei B2B-Geldforderungen ohne Verbraucher als Gläubiger: 40 Euro je Forderung pauschal als Verzugsschaden, anrechenbar auf weitergehende Schadensersatzkosten (z. B. Inkasso/Anwalt). Greift bei jeder verzögerten Zahlung neu.
- **Rechnungs-Anforderungen (§ 14 UStG bei B2B):** Vollständige Rechnung mit Pflichtangaben (Anschriften, Steuernummer/USt-IdNr., Datum, Leistungsbeschreibung, Entgelt, Steuersatz, Steuerbetrag). Bei Mängeln häufig Berufung auf fehlende Fälligkeit; gerichtlich aber strikt zu trennen: Mängel der Rechnung berühren in der Regel nicht die Fälligkeit der zugrundeliegenden Forderung.
- **Verjährung (§ 195 BGB):** Regelmäßig 3 Jahre, Beginn mit Schluss des Jahres, in dem Anspruch entstanden und Kenntnis besteht (§ 199 BGB). Bei Mietzinsen: 3 Jahre. Bei Werklohn: 3 Jahre ab Abnahme.
- **Praktiker-Tipp:** Klare Zahlungsbedingungen vereinbaren ("netto Kasse innerhalb von 14 Tagen ohne Abzug ab Rechnungsdatum"); damit ist Fälligkeit kalendermäßig bestimmt und Verzug tritt ohne Mahnung ein. Verspätete Rechnungsstellung verzögert nur den B2C-Verzug (§ 286 Abs. 3 BGB), nicht den B2B-Verzug (zwischen Unternehmern stets ab kalendarisch bestimmtem Termin).

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

## 3. `spezial-fmkw-mandantenkommunikation-entscheidungsvorlage`

**Fokus:** Fmkw: Mandantenkommunikation und Entscheidungsvorlage im Plugin forderungsmanagement klagewerkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Fmkw: Mandantenkommunikation und Entscheidungsvorlage

## Fachkern: Fmkw: Mandantenkommunikation und Entscheidungsvorlage
- **Spezialgegenstand:** Fmkw: Mandantenkommunikation und Entscheidungsvorlage wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB Anspruch/Fälligkeit/Verzug, ZPO Mahn-/Klageverfahren, HGB kaufmännische Belege, Inkassorecht, Verjährung und Zuständigkeit.
- **Entscheidende Weiche:** Nur klare, fällige, beweisbare Forderungen weitergeben; Vertrag, Leistung, Rechnung, Mahnung, Einwendungen, Verjährung und Kosten getrennt prüfen.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Fmkw** prüfen.
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
