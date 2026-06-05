---
name: dsa-eidas-einordnung
description: "Eidas Einordnung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Eidas Einordnung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Eidas Einordnung** im Plugin DSA/DMA Digitalregulierung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-dsa-tatbestand-beweis-und-belege` | DSA: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin dsa dma digitalregulierung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-eidas-behoerden-gericht-und-registerweg` | Eidas: Behörden-, Gerichts- oder Registerweg im Plugin dsa dma digitalregulierung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-einordnung-zahlen-schwellen-und-berechnung` | Einordnung: Zahlen, Schwellenwerte und Berechnung im Plugin dsa dma digitalregulierung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin DSA/DMA Digitalregulierung gilt für **Eidas Einordnung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-dsa-tatbestand-beweis-und-belege`

**Fokus:** DSA: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin dsa dma digitalregulierung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# DSA: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Spezialwissen: DSA: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Spezialgegenstand:** DSA: Tatbestandsmerkmale, Beweisfragen und Beleglage / dsa tatbestand beweis und belege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DSA, EU, VO, DMA, DGA, AI, NIS, DORA, CRA, DDG, GWB, VLOP.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **DSA** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## DSA-Pflichtenkaskade (VO (EU) 2022/2065, gilt seit 17.02.2024)
- **Vermittlungsdienste**: Allgemeine Pflichten Art. 11-15 (Kontaktstelle, Vertreter, AGB-Transparenz, Transparenzbericht).
- **Hostingdienste**: zusätzlich Art. 16 (Notice-and-Action), Art. 17 (Begründung Moderationsmaßnahmen), Art. 18 (Strafverfolgungsmeldung bei Lebensgefahr).
- **Online-Plattformen**: zusätzlich Art. 19-28 (internes Beschwerdesystem, außergerichtliche Streitbeilegung, vertrauenswürdige Hinweisgeber, Maßnahmen gegen Missbrauch, Transparenzbericht erweitert, Online-Werbung, Schutz Minderjähriger, Designtransparenz).
- **VLOP/VLOSE** (Art. 33: 45 Mio. aktive Nutzer mtl.): zusätzlich Art. 34 Risikobewertung, Art. 35 Risikominderung, Art. 36 Krisenreaktion, Art. 37 unabhängiges Audit, Art. 39 Werbearchiv, Art. 40 Datenzugang für Forscher.

## Tatbestand Art. 16 DSA (Notice-and-Action)
Voraussetzungen für eine wirksame Meldung:
- Begründung mit Erläuterung des Rechtsverstoßes
- Genauer elektronischer Standort (URL)
- Name und Kontakt des Hinweisgebers (außer bei Inhalten zu Art. 3-7 RL 2011/93/EU)
- Erklärung des guten Glaubens

**Rechtsfolge**: ab Eingang einer hinreichend präzisen Meldung besteht "tatsächliche Kenntnis" i. S. v. Art. 6 DSA — Haftungsprivileg entfällt für den Inhalt. Zeitliche Tracking-Pflicht beweisen.

## Beweisbausteine
- Vollständige Eingangsbestätigung mit Zeitstempel (Art. 16 Abs. 4).
- Begründungspflicht jeder Maßnahme nach Art. 17 (Statement of Reasons) — auch beim DSA-Transparenzdatenbank-Eintrag.
- Audit-Trail interner Beschwerden Art. 20.

## Trade-off
Schnelle Entfernung mindert Haftungsrisiko, kann aber gegen Art. 17 (Begründungspflicht, ne bis in idem) und Art. 14 (AGB-Transparenz) verstoßen. Übermoderation steht unter unionsgrundrechtlicher Beobachtung (Art. 11 GRCh Meinungsfreiheit).

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

## 2. `spezial-eidas-behoerden-gericht-und-registerweg`

**Fokus:** Eidas: Behörden-, Gerichts- oder Registerweg im Plugin dsa dma digitalregulierung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Eidas: Behörden-, Gerichts- oder Registerweg

## Spezialwissen: Eidas: Behörden-, Gerichts- oder Registerweg
- **Spezialgegenstand:** Eidas: Behörden-, Gerichts- oder Registerweg / eidas behoerden gericht und registerweg. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EU, DSA, VO, DMA, DGA, AI, NIS, DORA, CRA, DDG, GWB, VLOP.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **eIDAS 2.0** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## eIDAS 2.0 Behörden- und Registerwege
- **VO (EU) 910/2014 (eIDAS)** geändert durch **VO (EU) 2024/1183 (eIDAS 2.0)**: rechtsgültige eID, qualifizierte elektronische Signatur (QES), elektronische Siegel, Zeitstempel, qualifizierte Webseitenzertifikate, Einschreiben.
- **EU Digital Identity Wallet (EUDI Wallet)**: Mitgliedstaaten müssen Wallet bereitstellen.
- **Zuständige Aufsicht in DE:**
 - **BNetzA** als Aufsicht über qualifizierte Vertrauensdiensteanbieter (§ 9 VDG).
 - **BSI** für Sicherheitsanforderungen, Standards, Zertifizierungen.
- **Vertrauensliste der EU**: ec.europa.eu/digital-building-blocks/sites/display/EUDIGITALIDENTITYWALLET — Liste qualifizierter Vertrauensdiensteanbieter.
- **Klagewege:**
 - **Vor BNetzA**: Anhörung, Anordnung, Widerruf der Zulassung; gegen Anordnungen VG-Klage.
 - **Zivilrecht**: §§ 6, 8 VDG (Vertrauensdienstegesetz) — Schadensersatzansprüche.
 - **Strafrecht**: § 269 StGB Fälschung beweiserheblicher Daten, § 268 StGB Fälschung technischer Aufzeichnungen.

## Praxis-Tipp
QES (qualifizierte elektronische Signatur) hat nach § 126a BGB die Funktion der Schriftform. Bei Streit über die Beweiskraft elektronischer Signaturen sind das Vertrauensdienste-Zertifikat (mit gültigem Zeitstempel zur Signaturzeit), die Sperrlistenprüfung (OCSP/CRL) und die Vertrauensliste der EU die Beweisgrundlage.

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

## 3. `spezial-einordnung-zahlen-schwellen-und-berechnung`

**Fokus:** Einordnung: Zahlen, Schwellenwerte und Berechnung im Plugin dsa dma digitalregulierung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Einordnung: Zahlen, Schwellenwerte und Berechnung

## Spezialwissen: Einordnung: Zahlen, Schwellenwerte und Berechnung
- **Spezialgegenstand:** Einordnung: Zahlen, Schwellenwerte und Berechnung / einordnung zahlen schwellen und berechnung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EU, DSA, VO, DMA, DGA, AI, NIS, DORA, CRA, DDG, GWB, VLOP.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Einordnung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Schwellen DSA (VO (EU) 2022/2065)
- **VLOP / VLOSE** (Art. 33 Abs. 1): durchschnittlich **mindestens 45 Mio. monatlich aktive Nutzer** in der Union — berechnet nach Methodik der Durchführungsverordnung (EU) 2023/1322.
- **Online-Plattformen, Kleinst- und Kleinunternehmen** sind nach Art. 19 von einem Teil der Pflichten befreit (Anlehnung an Empfehlung 2003/361/EG: < 50 Beschäftigte und ≤ 10 Mio. EUR Jahresumsatz/-bilanzsumme).
- **Bußgeld DSA** (Art. 52): bis 6 % des weltweiten Jahresumsatzes; Zwangsgeld bis 5 % des durchschnittlichen täglichen Umsatzes.

## Schwellen DMA (VO (EU) 2022/1925, gilt seit 02.05.2023)
Vermutung Gatekeeper-Status nach Art. 3 Abs. 2 DMA, wenn alle drei Schwellen erfüllt:
- **Größe Union**: Jahresumsatz im EWR ≥ 7,5 Mrd. EUR (in jedem der letzten drei Geschäftsjahre) **oder** durchschnittliche Marktkapitalisierung / fairer Marktwert ≥ 75 Mrd. EUR im letzten Geschäftsjahr **und** zentraler Plattformdienst in mindestens 3 Mitgliedstaaten.
- **Nutzerzahl**: mindestens 45 Mio. monatlich aktive Endnutzer in der Union und mindestens 10.000 jährlich aktive gewerbliche Nutzer (jeweils im letzten Geschäftsjahr).
- **Verfestigt**: Nutzer-Schwellen in den letzten drei Geschäftsjahren erreicht.

Gegenbeweis: Art. 3 Abs. 5 DMA — Marktbedingungen widerlegen die Gatekeeper-Stellung.

## Bußgeldrahmen DMA
- Bis **10 % des weltweiten Jahresumsatzes** (Art. 30); Wiederholung bis **20 %**. Zwangsgeld bis 5 % des durchschnittlichen täglichen Umsatzes.

## Trade-off
Schwellen sind Brutto-Größen — gerichtliche Überprüfung der Methodik (Definition aktiver Nutzer, Konsolidierungsgrenze) ist offen; Designated-Beschlüsse der Kommission werden vor dem EuG angegriffen. Die Marktkapitalisierungs-Schwelle macht auch wachstumsstarke Anbieter ohne hohen Umsatz erfassbar.

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
