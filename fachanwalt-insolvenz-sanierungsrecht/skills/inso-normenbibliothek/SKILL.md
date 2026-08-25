---
name: inso-normenbibliothek
description: "Erschließt eine konkret bezeichnete Vorschrift der Insolvenzordnung mit aktuellem Wortlaut, Systemstelle, Tatbestandsmerkmalen, Rechtsfolge, Fristen, Belegen und Verfahrensbezug. Verwenden für eine Einzelnorm oder Normsuche; lädt nur den einschlägigen Bereich und verweist bei vertiefter Fallbearbeitung auf den passenden Fachworkflow."
---

# 1. Vorschriften der Insolvenzordnung gezielt erschließen

## 1.1 Zweck und Anwendungsfall

Dieser Skill liefert den normbezogenen Einstieg, wenn eine Vorschrift der Insolvenzordnung genannt ist oder aus dem Sachverhalt ermittelt werden muss. Vertiefte Prüfungen wie Zahlungsunfähigkeit, Überschuldung, Anfechtung, Eigenverwaltung oder Insolvenzplan bleiben Aufgabe der hierfür vorhandenen Fachworkflows.

## 1.2 Eingaben

Benötigt werden Norm oder Fallfrage, Beteiligtenrolle, Verfahrensstadium, Fristlage und gewünschter Output. Aus der Akte sind nur diejenigen Unterlagen heranzuziehen, welche Tatbestand, Beweis oder Rechtsfolge der konkreten Vorschrift tragen.

## 1.3 Ablauf

1. Öffne den [Bereichsindex](references/index.md) und wähle genau die Datei mit der gesuchten Vorschrift.
2. Suche in dieser Bereichsdatei nach dem exakten `Suchbegriff` und lies nur den einschlägigen Normabschnitt bis zur nächsten Überschrift. Weitere Bereiche werden erst bei einer ausdrücklichen Verweisung oder notwendigen Schnittstelle geöffnet.
3. Prüfe den aktuellen Gesetzeswortlaut und ordne die Vorschrift in Verfahrensabschnitt, Beteiligtenrolle und Rechtsfolge ein.
4. Trenne Zulässigkeit, Tatbestand, Beweismaß, Darlegungs- und Beweislast, Frist, Zuständigkeit und Rechtsmittel.
5. Wenn der Fall eine eigenständige wirtschaftliche oder prozessuale Vollprüfung verlangt, wechsle anschließend zu genau einem passenden Fachskill und übergib ihm das Normergebnis samt Aktenfundstellen.

## 1.4 Quellenpflicht

Gesetzesstand und tragende Rechtsprechung sind aktuell und aus überprüfbaren Quellen zu verifizieren. Eine hinterlegte Arbeitskarte darf weder veralteten Wortlaut noch eine ungesicherte Fundstelle ersetzen.

## 1.5 Ausgabeformat

Liefere eine knappe Normkarte mit Tatbestand, Rechtsfolge, Verfahrensposition, Belegbedarf, Frist, stärkster Gegenposition und nächstem Arbeitsschritt. Bei einem Schriftsatzauftrag wird daraus unmittelbar ein ausformulierter Baustein mit konkreten Aktenfundstellen.

## 1.6 Beispiel

Bei einer Frage zu Paragraf 17 InsO wird zunächst nur der Bereich mit dieser Vorschrift geöffnet. Ergibt sich daraus eine vollständige Insolvenzreifeprüfung, wird das Normergebnis an den spezialisierten Zahlungsunfähigkeits-Workflow übergeben, ohne weitere Normskills parallel zu laden.
