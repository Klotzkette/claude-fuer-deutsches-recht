---
name: verkehrsowi-kommandocenter
description: "Für VerkehrsOWi-Verteidiger — Kommandocenter: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# VerkehrsOWi-Verteidiger — Kommandocenter

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen; Verjährung nach Delikt und anwendbarer Fassung (aktuell § 26 Abs. 3 StVG grundsätzlich 6 Monate bei § 24 Abs. 1, §§ 31–33 OWiG); Fahrverbot § 25 Abs. 2, 3 und 6 StVG (grundsätzlich spätestens 1 Monat nach Rechtskraft wirksam, Viermonatsprivileg nur bei erfüllten Voraussetzungen; Verbotsfrist gesondert); § 79 OWiG Rechtsbeschwerde 1 Woche. Historische Fassung und Übergang prüfen; [amtlich belegte Einzelheiten](../../references/verkehrsowi-leitplanken.md).
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Sofort-Triage bei Mandatsaufnahme

**Drei kritische Fragen zuerst:**

1. **Fristlage:** Wann wurde der Bussgeldbescheid zugestellt? Einspruchsfrist § 67 Abs. 1 OWiG: 2 Wochen ab Zustellung.
 - Frist offen → Einspruch sofort, dann vertiefen
 - Frist abgelaufen → Wiedereinsetzung § 52 OWiG prüfen

2. **OWi oder Strafrecht?** — Grenzwert: § 24a Abs. 1 StVG (0,5 Promille OWi) vs. § 316 StGB (ab 1,1 Promille oder Ausfallerscheinung = Strafrecht!); Geschwindigkeit: OWi immer.

3. **Fahrverbot oder Fahrerlaubnis-Entzug?** — § 25 StVG (OWi: 1-3 Monate, bleibt Fahrerlaubnis) vs. § 69 StGB (Strafrecht: Entziehung mit Sperrfrist).

## Ampel-Schnelldiagnose

| Situation | Ampel | Maßnahme |
|-----------|-------|-----------|
| Frist laeuft in < 3 Tagen | ROT | Einspruch SOFORT, dann vertiefen |
| Frist laeuft in 4-7 Tagen | GELB | Einspruch und Akteneinsicht parallel |
| Frist > 7 Tage | GRUEN | Strukturierte Bearbeitung |
| Frist abgelaufen, Wiedereinsetzungsgrund | GELB | § 52 OWiG Antrag |
| Strafrecht (§ 316 StGB) statt OWi | ROT | Subskill Strafrecht wechseln! |

## Routing-Matrix

| Aufgabe | Subskill |
|---------|---------|
| Einspruchsfrist berechnen + einlegen | `verkehrsowi-fristen-einspruch` |
| Akteneinsicht Messakte anfordern | `verkehrsowi-akteneinsicht-messakte` |
| Messverfahren-Angriffspunkte prüfen | `verkehrsowi-messverfahren-geschwindigkeit` |
| Beweisverwertung standardisiert | `verkehrsowi-beweisverwertung-standardisiert` |
| Alkohol / Drogen § 24a StVG | `verkehrsowi-alkohol-drogen-24a` |
| Fahreridentifizierung | `verkehrsowi-fahreridentifizierung` |
| Anhörung / Bussgeldbescheid-Prüfung | `verkehrsowi-anhoerung-bussgeldbescheid` |
| Haertefall Fahrverbot | `verkehrsowi-haertefall-fahrverbot` |
| Punkte in Flensburg | `verkehrsowi-punkte-fahrverbot-flensburg` |
| Hauptverhandlung Amtsgericht | `verkehrsowi-hauptverhandlung-amtsgericht` |
| Rechtsbeschwerde | `verkehrsowi-rechtsbeschwerde` |
| Zeugen Polizei Strategie | `verkehrsowi-zeugen-polizei-strategie` |
| Rotlicht Abstand Handy | `verkehrsowi-rotlicht-abstand-handy` |
| Verjährung Zustellung | `verkehrsowi-verjaehrung-zustellung` |
| Mandantenkommunikation | `verkehrsowi-mandantenkommunikation` |
| Quality Gate | `verkehrsowi-quality-gate` |

## Zentrale OWi-Normen im Überblick

- **§ 24 StVG** — Ordnungswidrigkeiten im Strassenverkehr allgemein
- **§ 24a StVG** — Alkohol (0,5 Promille) und Drogen
- **§ 25 StVG** — Fahrverbot 1-3 Monate
- **§ 26 StVG** — Zuständigkeit Bussgeldbehoerde
- **§ 67 OWiG** — Einspruch 2-Wochen-Frist
- **§ 77 OWiG** — Beweisaufnahme, Sachverstaendige
- **§ 79 OWiG** — Rechtsbeschwerde
- **§ 4 BKatV** — Regelfahrverbot und Abweichung bei Haertefall
- **Art. 103 Abs. 1 GG** — Rechtliches Gehoer, Rohmessdaten-Recht

## Querschnitts-Rechtsprechung

- BGH BGHSt 43, 277 — Standardisiertes Messverfahren befreit von Detailbegruendung, aber konkrete Einwaende sind aufzuklaeren.
- OLG Bamberg NZV 2017, 494 — Sachverstaendigenantrag bei konkreten Messfehler-Angriffspunkten zwingend zu bescheiden.

## Harte Leitplanken

- OWi vs. Strafrecht immer zuerst klären — falsche Qualifikation ist schwerer Fehler.
- Frist immer zuerst sichern — kein Schritt vor Einspruch.
- Rohmessdaten grundsätzlich anfordern.
- Anwaltliche Endkontrolle bei allen Fristen und Antraegen.

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.

<!-- BEGIN werkstatt-visualisierung -->
## 1. Verständlich arbeiten und sichtbar prüfen

Bei komplexem Material zuerst verständlich machen, wer beteiligt ist, was geschehen ist und welche Entscheidung ansteht. Vorhandene Unterlagen auswerten und Fachbegriffe beim ersten Gebrauch kurz erklären. Danach das erste nutzbare Arbeitsergebnis liefern. Die Fachansicht und ihre Beispiele an den konkreten Auftrag, Empfänger und Bearbeitungsstand anpassen; daraus entsteht kein Auftrag für ein zusätzliches Verfahren oder andere Unterlagen. Eine passende Visualisierung direkt erstellen, wenn sie Vergleich, Ablauf, Mengen oder Zusammenhänge verständlicher macht; nicht erst allgemein anbieten oder eine Auswahl aus Werkzeugnamen verlangen. Einfache Einzelfragen knapp beantworten. Anfangs eine zentrale Ansicht mit verständlichen Beschriftungen und kurzem Befund zeigen; weitere Details nach Bedarf öffnen.

**Leitfrage für Strafrecht und Strafverfahren:** Welche Verfahrensfrage ist jetzt entscheidungsreif und welcher Beleg fehlt für die nächste Handlung?

**Erste Ansicht:** Zeige Verfahrensstand und Frist als kurze Zeitachse; ordne Streitpunkte in einer Tabelle nach Vortrag, Gegenposition, Beleg, Rechtsmaßstab und nächstem Arbeitsschritt.

**Sinnvolle Interaktion:** Eine Auswahl eines Streitpunkts zeigt die tragenden Belegstellen und den zugehörigen Entwurfsabschnitt. Alternative Tatsachenannahmen bleiben getrennt; ein Klick entscheidet keine streitige Rechtsfrage.

**Datengrundlage:** Verfahrensrolle, Antrag oder Ziel, Ereignis und Zugang, streitige Tatsache, Beleg, Rechtsquelle und offener Punkt. Je tragendem Wert die Datei und Seite, Tabellenblatt/Zelle, Zeile oder Belegkennung mitführen.

**Weiter zum Ergebnis:** das verlangte ausformulierte Schreiben, der Schriftsatz, Bescheid, Entscheidungsentwurf oder Vermerk. Die Ansicht ist ein Arbeitsmittel auf diesem Weg.

Nutze eine tatsächlich verfügbare Visualisierung oder Fachanwendung; bei geeigneter interaktiver Oberfläche direkt ein Applet erstellen oder die vorhandene Anwendung verwenden. Ohne diese Fähigkeit eine verständliche Tabelle oder Skizze liefern. Belege und Annahmen trennen, fehlende Werte nicht als null behandeln. Auswahl und neue Angaben im selben Arbeitsprodukt fortschreiben und dieses ausformulieren. Keine Datenübermittlung, Speicherung oder erfolgreiche Funktion behaupten, die nicht stattfand.

Bei interaktiver Arbeit die [lokalen Regeln für Oberfläche, Belege und Fortsetzung](../../references/arbeitsoberflaeche-und-visualisierung.md) lesen.
<!-- END werkstatt-visualisierung -->
