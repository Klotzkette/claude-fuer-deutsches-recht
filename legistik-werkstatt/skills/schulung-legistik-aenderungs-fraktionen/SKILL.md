---
name: schulung-legistik-aenderungs-fraktionen
description: "Schulung Legistik Aenderungs Fraktionen: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Schulung Legistik Aenderungs Fraktionen

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Schulung Legistik Aenderungs Fraktionen** im Plugin Legistik Werkstatt. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `schulung-legistik` | Trainerleitfaden für Legistik-Schulung mit der Arbeitsakte elektronisches Pflichtpostfach. Anwendungsfall Referenten oder Mitarbeiter von Verbanden sollen legistische Kernkompetenz in zwei Tagen Inhouse-Schulung oder einer Woche Fortbildung erwerben. Lernziele Auftragsaufnahme Normebenen-Routing Verfassungsrecht- und Europarechts-Quercheck Referentenentwurf Begründung Synopse XML Folgenabschaetzung. Sechs Stationen mit Lernziel Aufgabe Stolperfallen Erwartungshorizont. Output Trainerleitfaden Aufgabenhefte Erwartungshorizonten je Station. Kompatibel mit der Arbeitsakte legistik-pflichtpostfach. |
| `spezial-aenderungs-formular-portal-und-einreichung` | Aenderungs: Formular, Portal und Einreichungslogik im Plugin legistik werkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-fraktionen-dokumentenmatrix-und-lueckenliste` | Fraktionen: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin legistik werkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-kabinettsentwuerfe-compliance-dokumentation-und-akte` | Kabinettsentwuerfe: Compliance-Dokumentation und Aktenvermerk im Plugin legistik werkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Legistik-Werkstatt gilt für **Schulung Legistik Aenderungs Fraktionen**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `schulung-legistik`

**Fokus:** Trainerleitfaden für Legistik-Schulung mit der Arbeitsakte elektronisches Pflichtpostfach. Anwendungsfall Referenten oder Mitarbeiter von Verbanden sollen legistische Kernkompetenz in zwei Tagen Inhouse-Schulung oder einer Woche Fortbildung erwerben. Lernziele Auftragsaufnahme Normebenen-Routing Verfassungsrecht- und Europarechts-Quercheck Referentenentwurf Begründung Synopse XML Folgenabschaetzung. Sechs Stationen mit Lernziel Aufgabe Stolperfallen Erwartungshorizont. Output Trainerleitfaden Aufgabenhefte Erwartungshorizonten je Station. Kompatibel mit der Arbeitsakte legistik-pflichtpostfach.


# Trainerleitfaden Schulung Legistik

> Arbeitsakte "Elektronisches Pflichtpostfach". Zwei Tage Inhouse-Schulung oder Aufteilung auf eine Fortbildungswoche.

## Lernziele

Nach Abschluss der Schulung koennen die Teilnehmenden:

1. **Auftragsaufnahme** - eine politische Vorgabe in operationalisierbare Regelungsziele übersetzen
2. **Norm-Routing** - die richtige Norm-Ebene wählen
3. **Verfassung quer prüfen** - Grundrechte, Kompetenzen, Wesentlichkeit
4. **Europarecht quer prüfen** - Primärrecht, Sekundärrecht, Notifizierung
5. **Referentenentwurf bauen** - Format, Änderungsbefehle, Inkrafttreten
6. **Begründung schreiben** - allgemeiner und besonderer Teil
7. **Synopse erstellen** - dreispaltig
8. **Folgenabschätzung** - Erfüllungsaufwand und Nachhaltigkeit
9. **NKR-Vorlage** - Erstellung
10. **Goldplating erkennen und vermeiden**

## Arbeitsakte

Politische Vorgabe: "Jede im Handelsregister eingetragene Gesellschaft sowie alle nach DSA als VLOP oder VLOSE eingestuften Unternehmen müssen ein elektronisches Pflichtpostfach vorhalten."

Akte enthält:
- Auftragsblatt aus Koalitionsvertrag-Auszug
- Bestehende Normen-Sammlung (HGB, ZPO, FamFG, DSA, eIDAS)
- Synopsen-Vorlage
- Begründungs-Vorlage
- XML-Beispiel
- NKR-Vorlage

## Stationen

### Station 1 - Auftragsaufnahme (60 Min)

Skill `legistik-auftragsaufnahme`. Teilnehmende fuellen Auftragsblatt aus.

### Station 2 - Norm-Routing (45 Min)

Skill `normhierarchie-routing`. Entscheidung: HGB-Änderung als Hauptort, plus FamFG und ZPO als Folge.

### Station 3 - Kompetenz / Verordnung (45 Min)

Skill `gesetzgebungskompetenz-pruefen`. Art. 74 Nr. 11 GG (Recht der Wirtschaft) plus Nr. 1 (Bürgerliches Recht).

### Station 4 - Verfassung-Quercheck (60 Min)

Skill `verfassungsmaessigkeit-quercheck`. Grundrechte: Art. 12 Berufsfreiheit (Unternehmen), Art. 14 Eigentum (Investitionsschutz), Art. 3 Gleichbehandlung (warum nur diese Unternehmen?).

### Station 5 - Europarecht-Quercheck (90 Min)

Skill `europarechtskonformitaet`. DSA, eIDAS 2.0, Notifizierung 2015/1535. Goldplating-Prüfung Skill `goldplating-vermeiden`.

### Station 6 - Entwurf und Begründung (120 Min)

Skills `referentenentwurf-bauen` und `begruendung-allgemein-und-besonders`. Teilnehmende formulieren Paragraf 33a HGB neu.

### Station 7 - Synopse und Lesefassung (45 Min)

Skills `synopse-erstellen` und `lesefassung-konsolidiert`.

### Station 8 - XML (30 Min)

Skill `xml-paralleldarstellung`. Optional - nur wenn Zielgruppe IT-affin.

### Station 9 - Folgenabschätzung (60 Min)

Skills `folgenabschaetzung-erfuellungsaufwand` und `folgenabschaetzung-nachhaltigkeit`.

### Station 10 - NKR und KMU (45 Min)

Skill `normenkontrollrat-kmu-check`.

### Station 11 - Goldplating-Sondersession (30 Min)

Diskussion: wann ist strenger als EU OK? Wann nicht?

### Station 12 - Plenum Abschluss (45 Min)

Skill `schulung-legistik`. Was würden Sie anders machen?

## Erwartungshorizonte

Siehe Arbeitsakte `legistik-pflichtpostfach`.

## Stolperfallen-Sammlung

- Norm-Ebene falsch gewählt (Wesentlichkeit übersehen)
- Notifizierung 2015/1535 übersehen
- Goldplating begangen ohne Bewusstsein
- Erfüllungsaufwand zu niedrig geschätzt
- Bestimmtheitsgebot bei Schwellenwerten verletzt ("ab einer gewissen Größe")
- Verweis-Schleifen erst spaet entdeckt

## Materialliste

- Drucker für Entwürfe
- Whiteboard / Flipchart
- ggf. Excel-Schulung für Synopsen-Tabellen
- HdR-PDF, GGO-PDF, NKRG-PDF
- Smartphone für Online-Recherche in BGBl und Bundesanzeiger
## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 38-42 GGO (Legistik-Grundregeln, Schulungspflicht für Referenten) — §§ 1-5 HdR (Handbuch der Rechtsförmlichkeit, Ausbildungsgrundlage) — Art. 20 Abs. 3 GG (Rechtsstaat: hinreichende Normenqualität) — § 33 BBG (Fortbildungspflicht Bundesbeamte)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `spezial-aenderungs-formular-portal-und-einreichung`

**Fokus:** Aenderungs: Formular, Portal und Einreichungslogik im Plugin legistik werkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.


# Aenderungs: Formular, Portal und Einreichungslogik

## Spezialwissen: Aenderungs: Formular, Portal und Einreichungslogik
- **Spezialgegenstand:** Aenderungs: Formular, Portal und Einreichungslogik / aenderungs formular portal und einreichung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** XML.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Aenderungs** prüfen.
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

## 3. `spezial-fraktionen-dokumentenmatrix-und-lueckenliste`

**Fokus:** Fraktionen: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin legistik werkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.


# Fraktionen: Dokumentenmatrix, Lückenliste und Nachforderung

## Spezialwissen: Fraktionen: Dokumentenmatrix, Lückenliste und Nachforderung
- **Spezialgegenstand:** Fraktionen: Dokumentenmatrix, Lückenliste und Nachforderung / fraktionen dokumentenmatrix und lueckenliste. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** XML.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Fraktionen** prüfen.
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

## 4. `spezial-kabinettsentwuerfe-compliance-dokumentation-und-akte`

**Fokus:** Kabinettsentwuerfe: Compliance-Dokumentation und Aktenvermerk im Plugin legistik werkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.


# Kabinettsentwuerfe: Compliance-Dokumentation und Aktenvermerk

## Spezialwissen: Kabinettsentwuerfe: Compliance-Dokumentation und Aktenvermerk
- **Spezialgegenstand:** Kabinettsentwuerfe: Compliance-Dokumentation und Aktenvermerk / kabinettsentwuerfe compliance dokumentation und akte. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** XML.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Kabinettsentwuerfe** prüfen.
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
