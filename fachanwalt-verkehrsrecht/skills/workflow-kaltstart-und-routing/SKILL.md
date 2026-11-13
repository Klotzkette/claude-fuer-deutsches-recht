---
name: workflow-kaltstart-und-routing
description: "Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Fachanwalt Verkehrsrecht."
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

## Verkehrsrechts-Kaltstart-Triage (Fachanwalt-Skill)
- **Stufe 1 - Saeule identifizieren:**
  - (a) Verkehrszivilrecht (Unfall, Schadenersatz, Mietwagen, Wertminderung, Nutzungsausfall, fiktive vs. konkrete Abrechnung, KH-Versicherer §§ 7, 17, 18 StVG, § 115 VVG).
  - (b) Verkehrs-OWi (Bussgeldbescheid §§ 24 ff. StVG, BKatV).
  - (c) Verkehrsstrafrecht (§§ 142 StGB, 222, 229, 315b, 315c, 315d, 316 StGB).
  - (d) Verkehrsverwaltungsrecht (FeV, MPU, Fuehrerschein-Entziehung, Punkte FAER § 4 StVG).
  - (e) Versicherungsrecht (Vollkasko, Teilkasko, Insassenunfallversicherung).
- **Stufe 2 - Mandantenrolle:** Geschaedigter, Schaediger, Halter, Fahrer, Versicherungsnehmer, Beschuldigter, Anwartschafts-/Wiedererteilungsantragsteller.
- **Stufe 3 - Haftungsquote bei Unfall:** § 17 StVG Betriebsgefahr-Abwaegung, § 7 StVG Halterhaftung; § 18 StVG Fahrerhaftung, § 823 BGB Verschulden, § 115 VVG Direktanspruch.
- **Stufe 4 - Kaskadenpruefung bei Trunkenheit:** § 24a StVG (0,5 Promille OWi), § 316 StGB (relative Fahruntuechtigkeit ab 0,3 Promille mit Ausfallerscheinungen; absolute ab 1,1), § 315c I Nr. 1a StGB (Gefaehrdung StraVerkehr), § 69 StGB (Entziehung Fahrerlaubnis).
- **Stufe 5 - Sofortmassnahmen:**
  - Akteneinsicht (§ 147 StPO bzw. § 49 OWiG, § 29 StVG Halterauskunft).
  - Versicherung: Schaden anzeigen, Werkstatt, SV-Gutachten beauftragen (Anspruch auf eigenen Sachverstaendigen).
  - Bei vorlaeufiger Entziehung Fuehrerschein § 111a StPO: Beschwerde § 304 StPO; Antrag auf Aufhebung.
- **Stufe 6 - Strategieentscheidungen** in Querverweisen auf Spezialskills.

<!-- BEGIN werkstatt-visualisierung -->
## 1. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für Straßenverkehrsrecht:** Welche Verfahrensfrage ist jetzt entscheidungsreif und welcher Beleg fehlt für die nächste Handlung?

**Erste Ansicht:** Zeige Verfahrensstand und Frist als kurze Zeitachse; ordne Streitpunkte in einer Tabelle nach Vortrag, Gegenposition, Beleg, Rechtsmaßstab und nächstem Arbeitsschritt.

**Sinnvolle Interaktion:** Eine Auswahl eines Streitpunkts zeigt die tragenden Belegstellen und den zugehörigen Entwurfsabschnitt. Alternative Tatsachenannahmen bleiben getrennt; ein Klick entscheidet keine streitige Rechtsfrage.

**Datengrundlage:** Verfahrensrolle, Antrag oder Ziel, Ereignis und Zugang, streitige Tatsache, Beleg, Rechtsquelle und offener Punkt. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** das verlangte ausformulierte Schreiben, der Schriftsatz, Bescheid, Entscheidungsentwurf oder Vermerk. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
