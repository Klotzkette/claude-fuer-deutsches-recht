---
name: workflow-kaltstart-und-routing
description: "Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Insolvenzrecht."
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

## Insolvenzrecht-spezifische Routing-Weichen
- **Antragspflicht (§ 15a InsO)?** Geschäftsführer/Vorstand bei GmbH/AG → Drei-Wochen-Frist bei Zahlungsunfähigkeit (§ 17 InsO), Sechs-Wochen-Frist bei Überschuldung (§ 19 InsO). Sofort prüfen, ob Frist läuft. Bei Haftungsfrage: Skill für Geschäftsführerhaftung.
- **Eröffnungsgrund?** Zahlungsunfähigkeit § 17 InsO (Liquiditätslücke ≥ 10 Prozent über drei Wochen, BGH-Linie), drohende Zahlungsunfähigkeit § 18 InsO (Prognosezeitraum 24 Monate seit SanInsFoG), Überschuldung § 19 InsO (rechnerische Überschuldung plus negative Fortbestehensprognose, Prognosezeitraum 12 Monate).
- **Verfahrensart?** Regelverfahren, Eigenverwaltung nach Paragraf 270 InsO (Antrag und Eigenverwaltungsplanung nach Paragraf 270a InsO, vorläufige Anordnung nach Paragraf 270b InsO) oder Schutzschirm nach Paragraf 270d InsO. Für den Schutzschirm braucht es drohende Zahlungsunfähigkeit oder Überschuldung ohne eingetretene Zahlungsunfähigkeit und die begründete Bescheinigung einer in Insolvenzsachen erfahrenen, gesetzlich qualifizierten Person; IDW S 11 kann methodisch helfen, ist aber keine eigenständige gesetzliche Zulässigkeitsvoraussetzung. Den StaRUG-Weg nach den aktuellen Zugangsvoraussetzungen gesondert prüfen.
- **Rolle des Mandanten?** Schuldner, Geschäftsführer (persönliche Haftung), Insolvenzverwalter, Gläubiger (Anmeldung, Aus-/Absonderung), Anfechtungsgegner, Sicherungsnehmer.
- **Eilige Trigger:** Insolvenzgeldvorfinanzierung läuft, Lohnzahlung steht an, Energieversorger droht Sperre, Vermieter kündigt § 112 InsO, Pfändung droht, Strafanzeige § 15a Abs. 4 InsO im Raum.

## Anti-Halluzinations-Hinweise
- Keine erfundenen BGH-Aktenzeichen. Wenn Datum/Az. nicht sicher: "BGH-Linie zu § 17 InsO, Az. bitte verifizieren".
- IDW S6 ist Standard für Sanierungskonzept, IDW S11 für Insolvenzgründe — Stand stets prüfen.
- Drei-Wochen-Frist § 15a InsO ist Höchstfrist, keine Mindestfrist. Verkürzung möglich, wenn Sanierung aussichtslos.

<!-- BEGIN werkstatt-visualisierung -->
## 1. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für Insolvenz- und Sanierungsrecht:** Welche belegten Beträge tragen das Ergebnis und welche Annahme verändert es?

**Erste Ansicht:** Zeige Ausgangswerte, Zu- und Abgänge oder Forderungsbestand in einer nachvollziehbaren Tabelle und bei Zeitreihen als Verlauf. Trenne Stichtag, Zeitraum, Fälligkeit und tatsächlichen Geldfluss.

**Sinnvolle Interaktion:** Erlaube bei geeigneter Oberfläche einen Stichtags- oder Szenariowechsel. Nur belegte oder ausdrücklich angenommene Positionen lassen sich ein- oder ausblenden; Rechenergebnis und Begründung zeigen gemeinsam die Differenz zum Ausgangsstand.

**Datengrundlage:** Betrag, Währung, Vorzeichen, Datum, Zuordnungsgrund, Berechnungsregel und Originalfundstelle. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** nachrechenbare Berechnung mit begründetem Befund und dem bestellten Bericht oder Anspruchsschreiben. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
