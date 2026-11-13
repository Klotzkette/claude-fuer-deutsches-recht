---
name: workflow-kaltstart-und-routing
description: "Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Krisenfrüherkennung und StaRUG-Management."
---

# Kaltstart und Routing

## Aufgabe
Nutze diesen Workflow-Skill für Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
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

## Routing-Weichen Krisenfrüherkennung
- **Rechtspflicht:** Paragraf 1 StaRUG verpflichtet die Geschäftsleiter der dort erfassten Rechtsträger, fortlaufend über bestandsgefährdende Entwicklungen zu wachen, geeignete Gegenmaßnahmen zu ergreifen und das Überwachungsorgan unverzüglich zu unterrichten.
- **Beobachtungszeitraum:** Paragraf 1 StaRUG nennt keinen festen Zeitraum. Für die drohende Zahlungsunfähigkeit ist nach Paragraf 18 Absatz 2 InsO in aller Regel eine gesonderte 24-Monats-Prognose zu rechnen. Eine Lücke in dieser Prognose ist ein Krisensignal, ersetzt aber weder Tatbestandsprüfung noch Stichtagsabgrenzung.
- **Mandantenrolle?**
  - Geschäftsleitung selbst (haftungsrelevant): eigene Pflicht nach Paragraf 1 StaRUG; Aufgabenverteilung und Delegation entlasten nur bei ordnungsgemäßer Auswahl, Instruktion und Überwachung.
  - Berater (RA, StB, Sanierungsberater): Plausibilisieren des Frühwarnsystems.
  - Aufsichtsrat oder Beirat: konkrete Organstellung und Überwachungspflicht nach Paragraf 111 AktG, Paragraf 52 GmbHG, Satzung und Geschäftsordnung prüfen.
- **Welcher Skill als Nächstes?**
  - Liquiditätsplanung (13-Wochen oder 24-Monate) → liquiditaetsplanung-Plugin.
  - Fortbestehensprognose → fortbestehensprognose-Plugin.
  - StaRUG-Plan oder Insolvenzplan → insolvenzplan-starug-planwerkstatt-Plugin.

## Eilige Trigger
- Hinweise auf drohende Zahlungsunfähigkeit: Prognose nach Paragraf 18 InsO erstellen, Eignung der StaRUG-Instrumente gesondert prüfen und eine beabsichtigte Inanspruchnahme nach Paragraf 31 StaRUG anzeigen.
- Eingetretene Zahlungsunfähigkeit oder Überschuldung: Antragspflicht nach Paragraf 15a InsO ohne schuldhaftes Zögern prüfen; die StaRUG-Route nicht ungeprüft fortsetzen.
- Ab Eintritt materieller Insolvenz Zahlungen anhand Paragraf 15b InsO einzeln prüfen und dokumentieren.

<!-- BEGIN werkstatt-visualisierung -->
## 1. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für Sanierung, StaRUG und Krisenfrüherkennung:** Welche belegten Beträge tragen das Ergebnis und welche Annahme verändert es?

**Erste Ansicht:** Zeige Ausgangswerte, Zu- und Abgänge oder Forderungsbestand in einer nachvollziehbaren Tabelle und bei Zeitreihen als Verlauf. Trenne Stichtag, Zeitraum, Fälligkeit und tatsächlichen Geldfluss.

**Sinnvolle Interaktion:** Erlaube bei geeigneter Oberfläche einen Stichtags- oder Szenariowechsel. Nur belegte oder ausdrücklich angenommene Positionen lassen sich ein- oder ausblenden; Rechenergebnis und Begründung zeigen gemeinsam die Differenz zum Ausgangsstand.

**Datengrundlage:** Betrag, Währung, Vorzeichen, Datum, Zuordnungsgrund, Berechnungsregel und Originalfundstelle. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** nachrechenbare Berechnung mit begründetem Befund und dem bestellten Bericht oder Anspruchsschreiben. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
