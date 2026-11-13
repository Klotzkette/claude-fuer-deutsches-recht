---
name: einstieg-routing
description: "Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Fluggastrechte."
---

# Einstieg und Routing

## Einsatzlage

Bearbeite die Fluggastforderung anhand von Buchung, Flugverlauf und vorhandener Korrespondenz bis zum bestellten Schreiben oder Beratungsergebnis. Ordne dafür Ereignis, ausführendes Unternehmen, Fristen und die einschlägige Fachprüfung zu.

## Fachlandkarte dieses Plugins

- `abtretung-an-fluggastportal-spezial` — Abtretung AN Fluggastportal Spezial
- `airline-bonitaet-und-vollstreckung` — Airline Bonitaet und Vollstreckung
- `airline-standardausreden-annullierung` — Airline Standardausreden Annullierung
- `airline-standardausreden-pruefen` — Airline Standardausreden Prüfen
- `anlagen-bauen` — Anlagen Bauen
- `annullierung-oder-verspaetung-einordnen` — Annullierung Oder Verspaetung Einordnen
- `annullierung-schriftsatz-brief-memo-bausteine` — Annullierung Schriftsatz Brief Memo Bausteine
- `annullierung-schriftsatz-brief-und-memo-bausteine` — Annullierung Schriftsatz Brief und Memo Bausteine
- `anschluss-router` — Anschluss Router
- `anschlussflug-und-reiseplan` — Anschlussflug und Reiseplan
- `ausgleich-internationaler-bezug-schnittstellen` — Ausgleich Internationaler Bezug Schnittstellen
- `ausgleich-internationaler-bezug-und-schnittstellen` — Ausgleich Internationaler Bezug und Schnittstellen
- `ausnahmen-aussergewoehnliche-umstaende` — Ausnahmen Aussergewoehnliche Umstaende
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Buchung, Bordkarten, Störungsmitteilung und Antworten des Unternehmens zuerst lesen. Rolle und gewünschtes Ergebnis nur klären, soweit sie nicht bereits feststehen; kein ungefragter Klageentwurf bei einem Beratungsauftrag.
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fluggastrechte sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.
- Fehlt die Ankunftszeit oder das Ersatzangebot, den konkreten Nachweis anfordern und den bereits begründbaren Teil vorläufig bearbeiten. Nach Eingang Zeitverlust, Betrag und betroffene Argumentation aktualisieren und das bestellte Dokument fertigstellen. Weitere gezielte Fragen sind bei neuen entscheidenden Lücken möglich, bereits beantwortete Fragen entfallen.

## Normen & Rechtsprechung

Konkret zu prüfen:

- VO (EG) Nr. 261/2004 (Fluggastrechte)
- Art. 5 VO 261/2004 (Annullierung)
- Art. 6 VO 261/2004 (Verspätung)
- Art. 7 VO 261/2004 (Ausgleichszahlung 250/400/600 EUR)
- EuGH C-402/07 (Sturgeon)

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Einen passenden Spezialskill optional nutzen; sein Aufruf oder seine Benennung ersetzt nicht die Bearbeitung. Kein weiterer Dateizugriff ist Voraussetzung für die Fortsetzung mit den vorliegenden Angaben.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
- Interne Quellen- und Zugriffshinweise getrennt vom Empfängertext halten. Vollständige Sätze und dezimale Gliederung; für formatierte Dokumente Times New Roman 11 pt, sonst entsprechender Exporthinweis. Versand, Abtretung oder Klageeinreichung nicht eigenmächtig veranlassen.

<!-- BEGIN werkstatt-visualisierung -->
## 1. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für Fluggastrechte:** Welche Verfahrensfrage ist jetzt entscheidungsreif und welcher Beleg fehlt für die nächste Handlung?

**Erste Ansicht:** Zeige Verfahrensstand und Frist als kurze Zeitachse; ordne Streitpunkte in einer Tabelle nach Vortrag, Gegenposition, Beleg, Rechtsmaßstab und nächstem Arbeitsschritt.

**Sinnvolle Interaktion:** Eine Auswahl eines Streitpunkts zeigt die tragenden Belegstellen und den zugehörigen Entwurfsabschnitt. Alternative Tatsachenannahmen bleiben getrennt; ein Klick entscheidet keine streitige Rechtsfrage.

**Datengrundlage:** Verfahrensrolle, Antrag oder Ziel, Ereignis und Zugang, streitige Tatsache, Beleg, Rechtsquelle und offener Punkt. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** das verlangte ausformulierte Schreiben, der Schriftsatz, Bescheid, Entscheidungsentwurf oder Vermerk. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
