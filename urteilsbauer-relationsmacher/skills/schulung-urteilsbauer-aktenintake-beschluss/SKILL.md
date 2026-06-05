---
name: schulung-urteilsbauer-aktenintake-beschluss
description: "Schulung Urteilsbauer Aktenintake Beschluss: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Schulung Urteilsbauer Aktenintake Beschluss

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Schulung Urteilsbauer Aktenintake Beschluss** im Plugin Urteilsbauer / Relationsmacher. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `schulung-urteilsbauer` | Schulungs-Trainerleitfaden für Plugin urteilsbauer-relationsmacher: Ausbilder plant Schulungstag für Proberichter, Assessoren oder Rechtspfleger. Normen: §§ 313 und 286 und 529 ZPO (Lernziele). Prüfraster: Lernziele, Stundenplan (1 Tag oder 2 Tage), praktische Übungen anhand einer Arbeitsakte, Erwartungshorizont. Output Seminarplan, Arbeitsaufgaben, Bewertungsraster. Abgrenzung: Inhaltliche Arbeit mit Akten siehe relation-zivil, aktenintake-zivil; Prüfungsvorbereitung siehe vollrelation-langfassung. |
| `spezial-aktenintake-schriftsatz-brief-und-memo-bausteine` | Aktenintake: Schriftsatz-, Brief- und Memo-Bausteine im Plugin urteilsbauer relationsmacher; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-beschluss-tatbestand-beweis-und-belege` | Beschluss: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin urteilsbauer relationsmacher; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Urteilsbauer / Relationsmacher gilt für **Schulung Urteilsbauer Aktenintake Beschluss**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `schulung-urteilsbauer`

**Fokus:** Schulungs-Trainerleitfaden für Plugin urteilsbauer-relationsmacher: Ausbilder plant Schulungstag für Proberichter, Assessoren oder Rechtspfleger. Normen: §§ 313 und 286 und 529 ZPO (Lernziele). Prüfraster: Lernziele, Stundenplan (1 Tag oder 2 Tage), praktische Übungen anhand einer Arbeitsakte, Erwartungshorizont. Output Seminarplan, Arbeitsaufgaben, Bewertungsraster. Abgrenzung: Inhaltliche Arbeit mit Akten siehe relation-zivil, aktenintake-zivil; Prüfungsvorbereitung siehe vollrelation-langfassung.

# Trainer-Leitfaden Schulung Urteilsbauer

Zielgruppe: Proberichter/-innen, Assessoren/-innen, Rechtspfleger/-innen.


## Triage zu Beginn (für Trainer)

1. Wie groß ist die Gruppe und welche Vorkenntnisse haben die Teilnehmenden (Proberichter, Assessoren, Rechtspfleger)?
2. Wird die Arbeitsakte `testakten/solis-vision-x-smartglasses/` verwendet oder eine andere Testakte?
3. Wird ein-tägig oder zwei-tägig geschult — welche Themenblöcke können gestrichen werden?
4. Sollen DOCX-Rendern und PDF-Export live vorgeführt werden (technische Voraussetzungen prüfen)?

## Aktuelle Rechtsprechung (für Schulungsunterlagen)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (für Schulungsunterlagen)

- § 139 ZPO — Hinweis- und Aufklärungspflicht
- § 313 ZPO — Inhalt und Form des Urteils (Tatbestand + Entscheidungsgründe)
- § 286 ZPO — Beweiswürdigung
- § 358, 359 ZPO — Beweisbeschluss
- § 38 FamFG — Beschluss (bei Familiensachen)
- §§ 708, 709 ZPO — vorläufige Vollstreckbarkeit

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Erweiterter Stundenplan Zweitagesschulung

### Tag 1

| Block | Dauer | Skills | Lernziel |
|---|---|---|---|
| Aktenintake | 90 Min | `aktenintake-zivil` | Akte strukturieren, Tabellen-Template ausfüllen |
| Relation | 90 Min | `relation-zivil`, `vollrelation-langfassung` | Vollrelation vs. Kurzrelation |
| Zulässigkeit + AG | 60 Min | `zulaessigkeit-pruefen`, `anspruchsgrundlagen-pruefen` | Prüfschema sicher anwenden |
| International | 60 Min | `internationales-privatrecht`, `cisg-pruefen` | CISG-Anwendbarkeit, Knock-out |
| Beweis | 60 Min | `beweisbeschluss-vorbereiten`, `beweiswuerdigung-mit-richter-input` | Beweiswürdigung schreiben |

### Tag 2

| Block | Dauer | Skills | Lernziel |
|---|---|---|---|
| Urteil schreiben | 90 Min | `tenor-bauen-zivil`, `tatbestand-zivil-schreiben`, `entscheidungsgruende-zivil-schreiben` | Vollständiges Urteil im Urteilsstil |
| Nebenentscheidungen | 60 Min | `kostenentscheidung-bauen`, `vorlaeufige-vollstreckbarkeit`, `rechtsmittelbelehrung-zivil` | Tenor-Ziff. 2-4 korrekt |
| Selbstkontrolle | 45 Min | `berufungsfest-pruefen`, `revisionsfest-pruefen` | Fehler selbst erkennen |
| Render | 45 Min | `dokumente-rendern-urteil-docx` | DOCX live erstellen |

## Hinweis zur Prüfungstäuschung

Am Beginn jeder Schulung: **Ausgegebene Relationen und Urteilsentwürfe dürfen nicht in Klausuren des Vorbereitungsdienstes als eigene Arbeit eingereicht werden.** Eigenleistung der Teilnehmenden ist nicht verzichtbar.

## Lernziele

Die Teilnehmenden koennen am Ende

1. eine Zivilakte strukturiert intaken,
2. eine Relation aufbauen,
3. die einschlaegigen Anspruchsgrundlagen identifizieren,
4. CISG- und IPR-Probleme erkennen,
5. einen Beweisbeschluss vorbereiten,
6. eine Beweiswürdigung schreiben (mit Eigenanteil),
7. Tenor, Tatbestand und Entscheidungsgründe formulieren,
8. ein vollständiges Urteil im offiziellen Layout ausgeben.

## Eintagesschulung

| Block | Skills |
| --- | --- |
| Akteintake und Relation | `aktenintake-zivil`, `relation-zivil`, optional `vollrelation-langfassung` |
| Zulässigkeit und Anspruchsgrundlagen | `zulaessigkeit-pruefen`, `anspruchsgrundlagen-pruefen` |
| Internationales | `internationales-privatrecht`, `cisg-pruefen`, `kollidierende-agb-pruefen`, `incoterms-und-gefahruebergang` |
| Beweis | `beweisbeschluss-vorbereiten`, `beweiswuerdigung-mit-richter-input` |
| Urteil schreiben | `tenor-bauen-zivil`, `tatbestand-zivil-schreiben`, `entscheidungsgruende-zivil-schreiben` |
| Nebenentscheidungen | `kostenentscheidung-bauen`, `vorlaeufige-vollstreckbarkeit`, `rechtsmittelbelehrung-zivil` |
| Selbstkontrolle | `berufungsfest-pruefen`, `revisionsfest-pruefen` |
| Ausgabe | `dokumente-rendern-urteil-docx` |

## Zweitagesschulung

Tag 1 wie oben. Tag 2 vertieft die Arbeitsakte `testakten/solis-vision-x-smartglasses/`:
- Vormittag: kollidierende AGB Schweizer Recht und EU-Recht; CISG-Anwendbarkeit ohne und mit ordnungsgemäßem Ausschluss
- Mittag: DSGVO als Eingriffsnorm und Auswirkung auf den Sachmangel
- Nachmittag: Beweiswürdigung des Gutachtens; Schreiben des Urteilstenors und der Entscheidungsgründe; Render des DOCX

## Hinweis zur Prüfungstaeuschung

Im Trainerleitfaden zu Beginn jeder Schulung den Hinweis mitgeben: **Die hier ausgegebenen Relationen und Urteilsentwuerfe duerfen nicht in Klausuren des Vorbereitungsdienstes als eigene Arbeit eingereicht werden.** Es handelt sich um Schulungs- und Praxismaterial; die Eigenleistung der Teilnehmer/-innen ist nicht verzichtbar.

## Workflow-Entscheidungspunkte

Am Anfang **immer** vier Wahlfragen stellen:

1. **Relations-Stil**: Vollrelation Schulstandard (mit `vollrelation-langfassung`) oder Kurzrelation Praxisstandard (nur `relation-zivil`)?
2. **Dokumenttyp**: Urteil Versäumnisurteil oder Beschluss?
3. **Ausgabeformat**: nur DOCX oder DOCX und PDF?
4. **Tenor-Variante**: Soll die wahrscheinliche Variante (A B oder C aus der Tenorierungsstation) gerendert werden oder eine bestimmte Variante?

Die Antworten werden im Akten-Workspace gespeichert (Datei `workflow-entscheidungen.yaml`) damit nachvollziehbar bleibt was geliefert wurde.

## Stolperstellen in der Arbeitsakte

1. Kläger glaubt, deutsches Recht gelte - die AGB der Beklagten verweisen aber auf Schweizer Recht.
2. Beide AGB kollidieren - Knock-out Doktrin greift.
3. CISG ist anwendbar, auch ohne ausdrücklichen Ausschluss in beiden AGB.
4. Incoterm FOB Galway - Gefahrübergang dort, also vor Eintritt in die EU - aber DSGVO greift trotzdem nach Art. 3 II DSGVO.
5. Streitwert 1577 EUR - sachlich zustaendig AG nach Paragraf 23 Nr. 1 GVG.
6. Berufung waere ohne Zulassung nicht statthaft (Beschwer unter 600 EUR für Beklagte) - der Kläger hat aber Beschwer über 600 EUR, also Berufung statthaft.


---

<!-- AUDIT 27.05.2026 -->
## Audit-Hinweis (27.05.2026)

Dieser Skill wurde im Rahmen von Bundle 046 auf halluzinierte Rechtsprechungsnachweise geprüft und korrigiert.

## 2. `spezial-aktenintake-schriftsatz-brief-und-memo-bausteine`

**Fokus:** Aktenintake: Schriftsatz-, Brief- und Memo-Bausteine im Plugin urteilsbauer relationsmacher; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Aktenintake: Schriftsatz-, Brief- und Memo-Bausteine

## Spezialwissen: Aktenintake: Schriftsatz-, Brief- und Memo-Bausteine
- **Spezialgegenstand:** Aktenintake: Schriftsatz-, Brief- und Memo-Bausteine / aktenintake schriftsatz brief und memo bausteine. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DOCX und PDF sind Dateiformate, keine Rechtsquellen. Je nach Modul ZPO §§ 313 (Tatbestand/Entscheidungsgründe), 308, 322 (Tenor und Rechtskraft), 139 (richterlicher Hinweis), 78a (Rechtspfleger), 495a (vereinfachtes Verfahren), 511 ff. (Berufung) sowie GVG §§ 23, 71 (Zuständigkeit AG/LG), Aktenordnung des Landes und einschlägiges materielles Recht live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Aktenintake** prüfen.
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

## 3. `spezial-beschluss-tatbestand-beweis-und-belege`

**Fokus:** Beschluss: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin urteilsbauer relationsmacher; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Beschluss: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Spezialwissen: Beschluss: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Spezialgegenstand:** Beschluss: Tatbestandsmerkmale, Beweisfragen und Beleglage / beschluss tatbestand beweis und belege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DOCX und PDF sind Dateiformate, keine Rechtsquellen. Je nach Modul ZPO §§ 313 (Tatbestand/Entscheidungsgründe), 308, 322 (Tenor und Rechtskraft), 139 (richterlicher Hinweis), 78a (Rechtspfleger), 495a (vereinfachtes Verfahren), 511 ff. (Berufung) sowie GVG §§ 23, 71 (Zuständigkeit AG/LG), Aktenordnung des Landes und einschlägiges materielles Recht live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Beschluss** prüfen.
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
