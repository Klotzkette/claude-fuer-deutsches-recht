---
name: aggregation-spaltenprompts-definieren
description: "Aggregation Spaltenprompts Definieren: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Aggregation Spaltenprompts Definieren

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Aggregation Spaltenprompts Definieren** im Plugin Tabellenreview 3D. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `risikoampel-aggregation` | Risikoampeln für alle geprüften Positionen aggregieren: rot/gelb/gruen je Dimension. Normen: §§ 174 ff. InsO. Prüfraster: Ampellogik, Schwellenwerte, Gesamtrisikoeinschaetzung. Output: Risikoampel-Aggregationsbericht. Abgrenzung: nicht Kreuzblatt-Konsistenzprüfung. |
| `spaltenprompts-definieren` | Spaltenprompts für die drei Prüfperspektiven des 3D-Tabellenreviews definieren. Normen: §§ 174 ff. InsO. Prüfraster: Prompt-Formulierung je Spalte, Normverankerung, Eindeutigkeit. Output: Spaltenprompts-Dokument. Abgrenzung: nicht Zeilenprompts. |
| `spezial-arbeitsblatt-schriftsatz-brief-und-memo-bausteine` | Arbeitsblatt: Schriftsatz-, Brief- und Memo-Bausteine im Plugin tabellenreview 3d; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin Tabellenreview 3D gilt für **Aggregation Spaltenprompts Definieren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `risikoampel-aggregation`

**Fokus:** Risikoampeln für alle geprüften Positionen aggregieren: rot/gelb/gruen je Dimension. Normen: §§ 174 ff. InsO. Prüfraster: Ampellogik, Schwellenwerte, Gesamtrisikoeinschaetzung. Output: Risikoampel-Aggregationsbericht. Abgrenzung: nicht Kreuzblatt-Konsistenzprüfung.

# /tabellenreview-3d:risikoampel-aggregation


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Zweck

4000 Zellen einzeln zu sichten ist nicht praktikabel. Diese Aggregation reduziert die Sicht ohne Information zu verlieren — wer reinzoomen will klickt durch.

## Aggregationsstufen

### Zellen-Ampel (atomisch)

Aus `review-durchfuehren`. Vier Werte: grün / gelb / rot / prüfer-flag.

### Zeilen-Ampel (Dokument)

Konsolidierung über alle Zellen einer Zeile (also über alle Spalten aller Arbeitsblätter):
- mindestens 1 rote Zelle = Zeile **rot**
- keine rote aber mindestens 2 gelbe = Zeile **gelb**
- nur grün = Zeile **grün**
- mindestens 1 Prüfer-Flag = `prüfer-flag` zusätzlich

### Spalten-Ampel (Datenpunkt-Hotspot)

Anzahl roter Zellen über alle Zeilen über alle Arbeitsblätter pro Spalte. Top-5-Spalten mit höchstem Rot-Anteil = Hotspot-Spalten. Beispiel: 'Change of Control' rot in 42 von 87 Verträgen = Hotspot.

### Arbeitsblatt-Ampel (Perspektive)

Anteil roter Zeilen je Arbeitsblatt. Erlaubt Aussage: 'aus Datenschutzsicht ist das Portfolio kritisch, aus Wirtschaftssicht passabel'.

### Würfel-Ampel (Gesamtprojekt)

Worst-of-Worst-Konsolidierung: wenn irgendein Arbeitsblatt rot ist und irgendeine Zeile rot ist und Prüfer noch nicht abgenommen hat = **rot blockierend**.

## Schweregrad-Boden

Wenn ein Skill ein Finding mit einem Schweregrad produziert und ein anderer Skill (z. B. `kreuzblatt-konsistenzpruefung`) ihn ändern will, gilt der vorgelagerte Schweregrad als BODEN — eine rote Zelle kann nicht still nach gelb verschoben werden, nur dokumentiert überschrieben.

## Ausgabe

- `ampel-aggregat.md` mit:
 - Würfel-Ampel (gesamt)
 - Arbeitsblatt-Ampeln (eine je Perspektive)
 - Spalten-Hotspots (Top-N)
 - Zeilen-Ampel-Liste (sortiert nach Schwere)
- `heatmap.json` mit Daten für Excel-Heatmap-Visualisierung

## Hinweis zur Prüfer-Abnahme

Vor Mandatsabnahme müssen ALLE Zellen mit `prüfer-flag` durch den Prüfer abgehakt sein. Ohne Prüfer-Abnahme darf das Aggregat nicht an Mandanten gehen.

## 2. `spaltenprompts-definieren`

**Fokus:** Spaltenprompts für die drei Prüfperspektiven des 3D-Tabellenreviews definieren. Normen: §§ 174 ff. InsO. Prüfraster: Prompt-Formulierung je Spalte, Normverankerung, Eindeutigkeit. Output: Spaltenprompts-Dokument. Abgrenzung: nicht Zeilenprompts.

# /tabellenreview-3d:spaltenprompts-definieren


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Zweck

Die erste Würfel-Achse — Spalten — ist die wichtigste. Ein schlechter Spaltenprompt erzeugt schlechte Zellen über den gesamten Stapel. Dieser Skill kuratiert Spaltenprompts: aus Bibliothek wählen, anpassen, neu schreiben.

## Bibliothek (Auszug)

### M&A-Due-Diligence

- **Change-of-Control:** "Enthält der Vertrag eine Klausel die bei Kontrollwechsel beim Vertragspartner Kündigung Zustimmungspflicht oder Anpassung ausloest? Wenn ja wörtliches Zitat mit Fundstelle und Ausloeseschwelle (z. B. mehr als 50 Prozent Anteile / 25 Prozent / Sperrminorität)."
- **Abtretungsverbot:** "Ist die Abtretung von Rechten aus dem Vertrag ausgeschlossen oder zustimmungspflichtig? Wenn ja: nur Anspruch oder Vertragsübernahme? Woertliches Zitat und Norm-Bezug (BGB Paragraph 399 / HGB Paragraph 354a)."
- **MAC-Klausel:** "Enthält der Vertrag eine Material-Adverse-Change-Klausel? Wenn ja Definition der Wesentlichkeit und Rechtsfolge."
- **Haftungsbegrenzung:** "Wie ist die Haftung beschraenkt? Pro Schadensfall und pro Vertragsjahr? Aussnahmen (Vorsatz grobe Fahrlaessigkeit Personenschäden)?"

### Immobilien-Portfolio

- **Abteilung II:** "Welche Lasten und Beschraenkungen sind in Abteilung II eingetragen? Pro Eintrag: Art Begünstigter Rang und Löschungserleichterung."
- **Abteilung III:** "Welche Grundpfandrechte sind in Abteilung III eingetragen? Pro Eintrag: Betrag Gläubiger Rang Brieftyp und Löschungsbewilligung vorhanden ja oder nein."
- **Baulast:** "Ist im Baulastenverzeichnis eine Baulast verzeichnet? Inhalt und gegen wen wirksam (Baulasten existieren NICHT im Grundbuch)."

### Arbeitsvertrag

- **Tarifbindung:** "Wird auf einen Tarifvertrag Bezug genommen? Wenn ja welcher Tarifvertrag in welcher Fassung statisch oder dynamisch?"
- **Probezeit:** "Wie lange ist die Probezeit? Maximal 6 Monate nach BGB Paragraph 622 Absatz 3 zulässig."
- **Befristung:** "Ist der Vertrag befristet? Mit oder ohne Sachgrund? Falls ohne Sachgrund: Höchstdauer 2 Jahre nach TzBfG Paragraph 14."

### Vendor-Onboarding

- **AVV-Pflicht:** "Verarbeitet der Vendor personenbezogene Daten im Auftrag? Wenn ja liegt eine AVV nach DSGVO Artikel 28 vor und ist sie aktuell?"
- **Exit-Klausel:** "Welche Pflichten treffen den Vendor bei Vertragsende (Datenherausgabe Löschung Transition-Services)?"

## Pflichtfelder pro Spalte

```yaml
- id: change-of-control
 titel: "Change of Control"
 prompt: |
 Enthält der Vertrag eine Klausel die bei Kontrollwechsel ...
 antworttyp: zitat-mit-fundstelle
 pflichtfeld: true
 ampel-regel:
 rot: "Klausel vorhanden + harte Kündigungsfolge ohne Heilung"
 gelb: "Zustimmungsvorbehalt mit unklarer Schwelle"
 gruen: "Keine Klausel oder branchenüblicher Standard"
```

## Ausgabe

- `spaltenprompts.yaml` — fertige Spaltenprompts mit allen Pflichtfeldern
- Optional: `spaltenprompt-bibliothek.yaml` als wiederverwendbare Bibliothek

## Grenzen

Spaltenprompts ersetzen nicht das Lesen des Dokuments. Sie machen das Lesen reproduzierbar und vergleichbar.

## 3. `spezial-arbeitsblatt-schriftsatz-brief-und-memo-bausteine`

**Fokus:** Arbeitsblatt: Schriftsatz-, Brief- und Memo-Bausteine im Plugin tabellenreview 3d; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Arbeitsblatt: Schriftsatz-, Brief- und Memo-Bausteine

## Spezialwissen: Arbeitsblatt: Schriftsatz-, Brief- und Memo-Bausteine
- **Spezialgegenstand:** Arbeitsblatt: Schriftsatz-, Brief- und Memo-Bausteine / arbeitsblatt schriftsatz brief und memo bausteine. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** Aufgabenbezogen statt Platzhalter: HGB §§ 238, 257; AO § 147; ZPO §§ 371 ff. bei Urkunden/elektronischen Dokumenten; DSGVO Art. 5, 6, 32; GoBD; Mandats-/Datenraumvorgaben. Bei rein wirtschaftlicher Tabellenprüfung keine Scheinnorm erfinden.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Arbeitsblatt** prüfen.
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
