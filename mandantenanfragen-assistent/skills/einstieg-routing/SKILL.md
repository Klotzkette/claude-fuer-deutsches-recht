---
name: einstieg-routing
description: "Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: mandantenanfragen-assistent."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Mandantenanfragen Assistent** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `anfrage-eingang-parser` — Anfrage Eingang Parser
- `anrede-anwaltskanzleien-bittet` — Anrede Anwaltskanzleien Bittet
- `anrede-uebernehmen` — Anrede Uebernehmen
- `anwaltskanzleien-erstpruefung-und-mandatsziel` — Anwaltskanzleien Erstpruefung und Mandatsziel
- `bietet-fehlerkatalog` — Bietet Fehlerkatalog
- `bittet-internationaler-bezug-und-schnittstellen` — Bittet Internationaler Bezug und Schnittstellen
- `dankt-dsgvo-sonderfall-e-mail` — Dankt DSGVO Sonderfall E Mail
- `dringlichkeitsmarker-einwilligung-hinweis` — Dringlichkeitsmarker Einwilligung Hinweis
- `dsgvo-sonderfall-und-edge-case` — DSGVO Sonderfall und Edge Case
- `e-mail-erstantwort-und-terminrouting` — E Mail Erstantwort und Terminrouting
- `eingehenden-quellenkarte` — Eingehenden Quellenkarte
- `einwilligung-hinweis-datenschutz` — Einwilligung Hinweis Datenschutz
- `einwilligungshinweis-fristennotiz-und-naechster-schritt` — Einwilligungshinweis Fristennotiz und Naechster Schritt
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Mandantenanfragen Assistent sind DSGVO. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

<!-- BEGIN werkstatt-visualisierung -->
## 1. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für Juristische Methodik und Arbeitstechnik:** Welche Quelle trägt welche Aussage und wo beginnt eine eigene Folgerung?

**Erste Ansicht:** Zeige eine Quellenkarte mit Originalaussage, genauer Fundstelle, zeitlichem und sachlichem Kontext sowie abgeleiteter Aussage. Eine Rezeptions- oder Argumentationslinie braucht belegte Verbindungen.

**Sinnvolle Interaktion:** Eine Auswahl kann Originaltext, Übersetzung und eigene Einordnung gegenüberstellen. Nicht verifizierte Zitate bleiben offen; weder fehlende Textstellen noch historische Übergänge ergänzen.

**Datengrundlage:** Quelle, Fassung, Datum, genaue Textstelle, Aussage, Übertragungsschritt und Aussagegrenze. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** quellengebundene Analyse, Überprüfung oder ausformulierter Argumentationsabschnitt. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
