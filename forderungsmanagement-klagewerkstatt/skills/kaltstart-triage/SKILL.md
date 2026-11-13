---
name: kaltstart-triage
description: "Für Kaltstart-Triage Forderungssache: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Kaltstart-Triage Forderungssache

Eingangsroutine für jede neue Forderungsakte. Ziel ist nicht ein Formularinterview, sondern eine belastbare Aktenhypothese mit moeglichst wenigen Rueckfragen.

## Grundsatz: Akte zuerst, Fragen danach

Wenn ein Ordner, eine ZIP-Datei oder mehrere Dokumente vorhanden sind, wird zuerst `aktenordner-erstlekture` ausgefuehrt. Aus Dateinamen, Briefkoepfen, Vollmacht, Rechnung, Mahnung, Kontoauszug, Mahnbescheid, Widerspruch, Klageentwurf und gerichtlichen Schreiben werden Mandant, Gegner, Forderungsart, Betrag, Zahlungslage, Mahnstand und Fristen rekonstruiert.

Der erste Output lautet nicht "Bitte beantworten Sie sieben Fragen", sondern:

```text
Ich sehe in der Akte vorlaeufig Folgendes:
- mutmasslicher Mandant:
- mutmasslicher Schuldner:
- Forderung / Restforderung:
- Stand Mahnung, Mahnbescheid, Klage oder Vollstreckung:
- auffaellige Risiken:
Ich frage jetzt nur noch die Punkte ab, die aus den Unterlagen nicht sicher folgen.
```

## Nur noch echte Luecken fragen

| Luecke | Frage | Nur stellen, wenn |
|---|---|---|
| Rolle unklar | "Ich vermute, du bist auf Seite [Gläubiger/Schuldner]. Stimmt das?" | Vollmacht, Briefkopf oder Anschreiben widerspruechlich |
| Ziel unklar | "Soll ich eintreiben, abwehren, vergleichen oder nur sortieren?" | kein Mandatsziel aus Mail/Anschreiben erkennbar |
| Frist unklar | "Gibt es eine Frist ausserhalb der Akte?" | gerichtliche Frist oder Verjaehrungsdruck nicht sicher |
| Zahlung unklar | "Ist nach dem letzten Kontoauszug noch etwas bezahlt worden?" | Kontoauszug endet vor aktueller Aktenlage |
| Gegner unklar | "Ist diese Anschrift noch aktuell?" | Zustellung, Umzug, HR-Auszug oder Insolvenzfund unsicher |

Mehr als drei Startfragen sind nur erlaubt, wenn Fristversaeumnis oder falsche Partei droht.

## Routing in drei Spuren

| Befund | Spur | Folgeskill |
|---|---|---|
| Akte ungeordnet oder Dokumentenlage unklar | Akteninventar | aktenordner-erstlekture oder dokumente-intake |
| Forderung schluessig, faellig, Schuldner bekannt, kein ernstliches Bestreiten | Mahnbescheid | mahnbescheid-online |
| Bestreiten wahrscheinlich oder Anspruch muss begruendet werden | Zahlungsklage | zahlungsklage-erstellen |
| Hauptforderung bezahlt, nur Kosten/Zinsen offen | Klageblocker | klagefreigabe-belegte-forderung |
| Forderung wackelig, Belege unklar, Vergleich wirtschaftlich sinnvoll | aussergerichtliche Mahnung oder Vergleich | mahnung-aussergerichtlich-stufenmodell |
| Titel liegt bereits vor | Vollstreckung | zwangsvollstreckung-überblick |

## Risikoampel Erstbewertung

| Ampel | Auslöser |
|---|---|
| gruen | Forderung dokumentiert Schuldner solvent Verjährung in weiter Ferne Zustellung gesichert |
| gelb | Belege luckenhaft Verjährung im laufenden Jahr Schuldner zahlungssaeumig |
| rot | Verjährung tritt in den naechsten sechzig Tagen ein Schuldner verzogen oder insolvent Belegstand schwach |

Rote Ampel triggert sofort Skill verjaehrung-prüfen und gegebenenfalls Mahnbescheid noch am gleichen Werktag.

## Startprodukt

Die Triage endet immer mit einem knappen Arbeitsplan:

| Punkt | Inhalt |
|---|---|
| Aktenbefund | Was liegt vor, was fehlt |
| Parteienhypothese | Mandant, Gegner, Vertreter, Anschriften, Beleg |
| Forderungsmatrix | Hauptforderung, Nebenforderung, Zinsen, Zahlungen, Rest |
| Chronologie | Vertrag, Leistung, Rechnung, Mahnung, Zahlung, Verfahren |
| Fristenampel | Verjaehrung, Widerspruch, Einspruch, gerichtliche Verfuegung |
| Naechster Skill | genau ein Hauptskill und maximal zwei Alternativen |

## Norm-Pinpoints

- ZPO 253 Abs. 2 Klage Pflichtbestandteile
- ZPO 688 ff. Mahnverfahren
- ZPO 690 Mahnbescheidsantrag
- ZPO 696 Abgabe nach Widerspruch
- ZPO 699 700 Vollstreckungsbescheid
- BGB 271 Faelligkeit
- BGB 286 Verzug
- BGB 288 Verzugszinsen
- BGB 362 Erfuellung
- BGB 195 199 Verjährung
- Paragraf 23 Nummer 1 GVG ab 2026 allgemeine Amtsgerichtsgrenze zehntausend Euro; Paragraf 23 Nummer 2a GVG hält Wohnraummietsachen streitwertunabhängig beim Amtsgericht.

## Quellen

- [ZPO 253](https://www.gesetze-im-internet.de/zpo/__253.html)
- [BGB 286](https://www.gesetze-im-internet.de/bgb/__286.html)
- [BGB 195](https://www.gesetze-im-internet.de/bgb/__195.html)
- [GVG 23](https://www.gesetze-im-internet.de/gvg/__23.html)

<!-- BEGIN werkstatt-visualisierung -->
## 1. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für Forderungsmanagement:** Welche belegten Beträge tragen das Ergebnis und welche Annahme verändert es?

**Erste Ansicht:** Zeige Ausgangswerte, Zu- und Abgänge oder Forderungsbestand in einer nachvollziehbaren Tabelle und bei Zeitreihen als Verlauf. Trenne Stichtag, Zeitraum, Fälligkeit und tatsächlichen Geldfluss.

**Sinnvolle Interaktion:** Erlaube bei geeigneter Oberfläche einen Stichtags- oder Szenariowechsel. Nur belegte oder ausdrücklich angenommene Positionen lassen sich ein- oder ausblenden; Rechenergebnis und Begründung zeigen gemeinsam die Differenz zum Ausgangsstand.

**Datengrundlage:** Betrag, Währung, Vorzeichen, Datum, Zuordnungsgrund, Berechnungsregel und Originalfundstelle. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** nachrechenbare Berechnung mit begründetem Befund und dem bestellten Bericht oder Anspruchsschreiben. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
