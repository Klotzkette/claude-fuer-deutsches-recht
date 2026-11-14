---
name: einstieg-routing
description: "Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Insolvenzforderungsanmeldungsprüfung."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Insolvenzforderungsanmeldungspruefung** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `eingang-form-belege-bearbeiten` (Fachthema: aktenanlage-batchregister) — Aktenanlage Batchregister
- `eingang-form-belege-bearbeiten` (Fachthema: beleg-und-urkundencheck) — Beleg und Urkundencheck
- `bestreiten-schuldner-delikt-bearbeiten` (Fachthema: bestreiten-interessen-betrag) — Bestreiten Interessen Betrag
- `bestreiten-schuldner-delikt-bearbeiten` (Fachthema: bestreiten-mehrparteien-konflikt-und-interessen) — Bestreiten Mehrparteien Konflikt und Interessen
- `grund-betrag-rang-sicherheit-bearbeiten` (Fachthema: betrag-behoerden-gericht-und-registerweg) — Betrag Behoerden Gericht und Registerweg
- `eingang-form-belege-bearbeiten` (Fachthema: dubletten-serienforderungen) — Dubletten Serienforderungen
- `grund-betrag-rang-sicherheit-bearbeiten` (Fachthema: feststellung-forderungsgrund-rang-grund) — Feststellung Forderungsgrund Rang Grund
- `pruefakte-quellen-output-bearbeiten` (Fachthema: forderungsanmeldung-mandantenkommunikation-redteam-qualitygate) — Forderungsanmeldung Mandantenkommunikation Redteam Qualitygate
- `bestreiten-schuldner-delikt-bearbeiten` (Fachthema: vbuh-verhandlung-vergleich-und-eskalation) — Forderungsanmeldung Vbuh Verhandlung Vergleich Eskalation
- `grund-betrag-rang-sicherheit-bearbeiten` (Fachthema: forderungsgrund-rang-und-belegpruefung) — Forderungsgrund Rang und Belegpruefung
- `eingang-form-belege-bearbeiten` (Fachthema: formalpruefung-174) — Formalpruefung 174
- `grund-betrag-rang-sicherheit-bearbeiten` (Fachthema: grund-betrag-zinsen) — Grund Betrag Zinsen
- `grund-betrag-rang-sicherheit-bearbeiten` (Fachthema: grund-risikoampel-und-gegenargumente) — Grund Risikoampel und Gegenargumente
- `pruefakte-quellen-output-bearbeiten` (Fachthema: anschluss-routing) — Anschluss Routing
- `pruefakte-quellen-output-bearbeiten` (Fachthema: dokumente-intake) — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Insolvenzforderungsanmeldungspruefung sind § 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Pr. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

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
