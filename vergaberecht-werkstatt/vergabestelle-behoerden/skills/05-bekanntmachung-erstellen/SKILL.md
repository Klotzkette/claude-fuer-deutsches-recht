---
name: 05-bekanntmachung-erstellen
description: "Auftragsbekanntmachung, Berichtigung oder Portalveröffentlichung für TED und eForms (oberhalb) oder Bekanntmachungsplattform des Bundes bzw Landesportal und DVAL (unterhalb) vorbereiten. Reihenfolge nach Paragraf 40 VgV erst EU dann national. Pflichtinhalt, Fristen, CPV, Unterlagenlinks und Uploadfreigabe prüfen. Output Bekanntmachungstext, Feldliste und Veröffentlichungsnachweis."
---

# Bekanntmachung erstellen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## In Klartext

Die Bekanntmachung ist die öffentliche Ankündigung des Auftrags. Sie entscheidet, wer von dem Auftrag erfährt und welches Ereignis den Fristlauf auslöst. Der Auftrag muss inhaltlich bestimmt sein und die Veröffentlichung auf dem richtigen Kanal in der gesetzlichen Reihenfolge erfolgen. Oberhalb des EU-Schwellenwerts gilt: zuerst Veröffentlichung im EU-Amtsblatt oder Ablauf der 48-Stunden-Regel nach § 40 Abs. 3 VgV, danach national.

## Rechtsgrundlage

§ 37 VgV (Inhalt und Versand) und § 40 VgV (Veröffentlichung, keine nationale Vorab-Veröffentlichung) iVm Durchführungsverordnung (EU) 2019/1780 (eForms). Unterhalb der Schwelle § 28 UVgO bzw. Landesrecht. Bauleistungen § 12 EU VOB/A (oberhalb) bzw. § 12 VOB/A (unterhalb).

## Veröffentlichungsweg wählen

1. Oberhalb EU-Schwellenwert: Supplement zum Amtsblatt der EU (TED) mit eForms über das angebundene Vergabeportal.
2. Nationale oder regionale Zweitveröffentlichung erst nach der EU-Veröffentlichung oder 48 Stunden nach Eingangsbestätigung durch das EU-Amt (§ 40 VgV) und ohne zusätzliche Angaben.
3. Unterhalb EU-Schwellenwert beim Bund: zentrale Bekanntmachungsplattform des Bundes (§ 28 UVgO).
4. Unterhalb bei Land und Kommune: Landesvergabeportal und nach Landesrecht gegebenenfalls regionales Amtsblatt; welche Kanaele Pflicht sind, im Landesvergabegesetz live prüfen.

## Fristanker ab 1. Juli 2026

1. Nach § 187 Abs. 2 GWB zuerst feststellen, ob das Verfahren vor dem 1. Juli 2026 begonnen hat.
2. In Neuverfahren grundsätzlich das jeweilige Absendeereignis nach §§ 15 bis 17 VgV dokumentieren.
3. Wurde bei der Übermittlung an das EU-Amt ein späterer Veröffentlichungstag angegeben, ist nach § 40 Abs. 1 Satz 2 VgV dieser angegebene Tag statt Absendung oder Eingangsbestätigung für die Fristberechnung maßgeblich.
4. Absendung, angegebener Veröffentlichungstag und tatsächliche TED-Veröffentlichung als drei getrennte Datenfelder führen. Eine bloß später erfolgte TED-Veröffentlichung verschiebt den Fristbeginn nicht automatisch.

Ausführlicher Wegweiser in der Repo-Referenz Veröffentlichungswege.

## Pflichtschritte Inhalt

1. Auftragsgegenstand und CPV-Code
2. Schätzwert (sofern bekannt) oder Wertspanne
3. Eignungs- und Ausschlussgründe
4. Zuschlagskriterien mit Gewichtung
5. Angebots- oder Teilnahmefrist (Mindestfristen § 15 VgV: offenes Verfahren 35 Tage; nichtoffenes Verfahren oder Verhandlungsverfahren mit TNWB 30 Tage Teilnahme und 30 Tage Angebot; bei Vorinformation oder beschleunigtem Verfahren Verkürzung möglich)
6. Verwendetes eForm-Formular
7. Übermittlungsbestätigung, gegebenenfalls angegebener späterer Veröffentlichungstag und tatsächlicher Veröffentlichungsnachweis mit TED-Nummer oder Portallink
8. Fristberechnungsblatt mit eindeutig benanntem Rechtsanker
9. Upload- oder Veröffentlichungsweg mit Freigabe dokumentieren

## Anker-Rechtsprechung

- EuGH C-454/06 'pressetext' zu wesentlichen Änderungen
- EuGH C-27/15 'Pizzo' zu nicht ankündigbaren Anforderungen

## Output

Bekanntmachungstext und Veröffentlichungsnachweis. Reihenfolge EU vor national dokumentieren. Bei verspäteter Veröffentlichung Fristenkette neu berechnen.

## Upload-Workflow

Bei Berichtigung, Fristverlängerung, geänderten Unterlagen oder Portalveröffentlichung den Skill `bekanntmachung-berichtigung-und-upload-routing` nutzen. Kein Senden an TED, DVAL, bund.de oder Landesportal ohne Freigabecheck.

## Wann Vergaberechtler einschalten

Bei Zweifeln an der Verfahrensart oder der Loslimitierung und immer dann, wenn eine bereits veröffentlichte Bekanntmachung korrigiert oder zurückgezogen werden muss; eine fehlerhafte Bekanntmachung kann das ganze Verfahren angreifbar machen.
