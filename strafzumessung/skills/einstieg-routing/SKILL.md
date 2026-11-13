---
name: einstieg-routing
description: "Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Strafzumessung."
---

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Strafzumessung** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `153a-stpo-iii-bewaehrung-stgb` — 153a STPO III Bewaehrung STGB
- `besonders-formular-portal-und-einreichung` — Besonders Formular Portal und Einreichung
- `bewaehrung-56-stgb-positive-sozialprognose` — Bewaehrung 56 STGB Positive Sozialprognose
- `bewaehrung-auflagen-bewaehrungswiderruf-56f` — Bewaehrung Auflagen Bewaehrungswiderruf 56F
- `bewaehrung-interessen-deutschem` — Bewaehrung Interessen Deutschem
- `bewaehrungswiderruf-56f-stgb` — Bewaehrungswiderruf 56F STGB
- `deutschem-tatbestand-beweis-und-belege` — Deutschem Tatbestand Beweis und Belege
- `freiheitsstrafe-compliance-dokumentation-und-akte` — Freiheitsstrafe Compliance Dokumentation und Akte
- `freiheitsstrafe-ohne-bewaehrung-vollstreckung` — Freiheitsstrafe Ohne Bewaehrung Vollstreckung
- `freiheitsstrafe-strafmass-geldstrafe` — Freiheitsstrafe Strafmass Geldstrafe
- `geldstrafe-grossen-rechtsmittel` — Geldstrafe Großen Rechtsmittel
- `geldstrafe-tagessatzanzahl-bestimmen` — Geldstrafe Tagessatzanzahl Bestimmen
- `geldstrafe-vs-freiheitsstrafe-47-stgb` — Geldstrafe VS Freiheitsstrafe 47 STGB
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Vorhandene Feststellungen, Vorurteile und Vollstreckungsunterlagen zuerst lesen. Rolle und Auftrag übernehmen: Verteidigung, Staatsanwaltschaft oder Gericht; benötigt werden etwa Strafzumessungsvermerk, Plädoyer oder Urteilsgründe, nicht automatisch ein Anklagesatz.
- Echte Rechtsmittel- und Verfahrensfristen aus Zustellung und Verfahrensstand bestimmen. Die Prüfung der Bewährung nach Paragraf 56 StGB sowie der Reststrafenaussetzung nach Paragrafen 57 und 57a StGB davon trennen; Straf- und Bewährungszeiträume sind keine allgemeinen Eilfristen.
- Fachpfad wählen: zentrale Anker im Strafzumessung sind StGB §§ 46, 46a, 46b, 47, 49, 56, 57, 57a, 64, JGG §§ 17, 18, 21, BtMG § 31. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Tatrichter, Verteidiger, Staatsanwaltschaft, Bewährungshelfer, Vollstreckungsbehörde.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

Fehlt bei einer Vorverurteilung der Vollstreckungsstand, den betreffenden Nachweis gezielt anfordern. Nach Eingang Zäsur und Einbeziehbarkeit für die Gesamtstrafe neu prüfen und die Begründung ändern. Bei Geldstrafe fehlende Einkommensangaben erfragen und die Tagessatzhöhe neu berechnen, ohne daraus automatisch die Tagessatzanzahl zu ändern.

Neue entscheidende Lücken in kurzen Anschlussfragen klären, beantwortete Fragen nicht wiederholen. Unabhängig tragfähige Teile vorläufig liefern und nach Antwort bis zum bestellten Dokument fortsetzen. Vollständige Sätze, dezimale Gliederung und soweit möglich Times New Roman 11 pt verwenden; Nutzerdateiname vor ergebnis.md als bloßem Standard. Keine Strafentscheidung, Verständigung oder externe Erklärung selbst auslösen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Fachskills und Referenzen sind optionale Vertiefungen; ihre Empfehlung ersetzt nicht das bestellte Ergebnis. Quellenstatus und Recherchegrenzen getrennt vom Empfängertext notieren.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

<!-- BEGIN werkstatt-visualisierung -->
## 1. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für Strafjustiz: Anklage, Hauptverhandlung und Rechtsfolgen:** Welche Verfahrensfrage ist jetzt entscheidungsreif und welcher Beleg fehlt für die nächste Handlung?

**Erste Ansicht:** Zeige Verfahrensstand und Frist als kurze Zeitachse; ordne Streitpunkte in einer Tabelle nach Vortrag, Gegenposition, Beleg, Rechtsmaßstab und nächstem Arbeitsschritt.

**Sinnvolle Interaktion:** Eine Auswahl eines Streitpunkts zeigt die tragenden Belegstellen und den zugehörigen Entwurfsabschnitt. Alternative Tatsachenannahmen bleiben getrennt; ein Klick entscheidet keine streitige Rechtsfrage.

**Datengrundlage:** Verfahrensrolle, Antrag oder Ziel, Ereignis und Zugang, streitige Tatsache, Beleg, Rechtsquelle und offener Punkt. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** das verlangte ausformulierte Schreiben, der Schriftsatz, Bescheid, Entscheidungsentwurf oder Vermerk. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
