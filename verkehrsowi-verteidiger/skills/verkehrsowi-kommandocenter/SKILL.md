---
name: verkehrsowi-kommandocenter
description: "Zentrales Steuerungsmodul VerkehrsOWi-Verteidiger: Mandant stellt OWi-Mandat vor und benoetigt schnelle Orientierung. Normen: §§ 24 StVG, 67 OWiG, 25 StVG, 4 StVG (FAER). Prüfraster: Ampel-Schnelldiagnose (Tatvorwurf, Frist, Fahrverbot-Risiko, Punkte), Routing auf Subskills. Output Deal-Karte OWi mit Fristen-Ampel und Routing-Empfehlung. Abgrenzung: Alkohol/Drogen siehe verkehrsowi-alkohol-drogen-24a; Rotlicht/Abstand/Handy siehe verkehrsowi-rotlicht-abstand-handy im Verkehrsowi Verteidiger: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# VerkehrsOWi-Verteidiger — Kommandocenter

## Arbeitsbereich

Zentrales Steuerungsmodul VerkehrsOWi-Verteidiger: Mandant stellt OWi-Mandat vor und benoetigt schnelle Orientierung. Normen: §§ 24 StVG, 67 OWiG, 25 StVG, 4 StVG (FAER). Prüfraster: Ampel-Schnelldiagnose (Tatvorwurf, Frist, Fahrverbot-Risiko, Punkte), Routing auf Subskills. Output Deal-Karte OWi mit Fristen-Ampel und Routing-Empfehlung. Abgrenzung: Alkohol/Drogen siehe verkehrsowi-alkohol-drogen-24a; Rotlicht/Abstand/Handy siehe verkehrsowi-rotlicht-abstand-handy. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: § 67 OWiG Einspruch 2 Wochen, § 31 OWiG Verjährung 3/6 Monate, § 26 StVG Fahrverbot 4 Monate, § 79 OWiG Rechtsbeschwerde 1 Woche.
- Tragende Normen verifizieren: StVG §§ 24, 24a, 25, 26, OWiG §§ 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Betroffener, Verteidiger, Bußgeldstelle (Polizei/Verwaltungsbehörde), Amtsgericht (Bußgeldrichter), OLG-Senat, PTB (Eichbehörde).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zeugenfragebogen, Anhörungsbogen, Bußgeldbescheid, Einspruchsschrift, Messprotokoll, Eichschein, Hauptverhandlungsprotokoll — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Einstiegspunkt fuer alle OWi-Mandate im Verkehrsrecht. Erfasst Kontext, bewertet Dringlichkeit und routet zur richtigen Subskill-Anleitung.

## Sofort-Triage bei Mandatsaufnahme

**Drei kritische Fragen zuerst:**

1. **Fristlage:** Wann wurde der Bussgeldbescheid zugestellt? Einspruchsfrist § 67 Abs. 1 OWiG: 2 Wochen ab Zustellung.
 - Frist offen → Einspruch sofort, dann vertiefen
 - Frist abgelaufen → Wiedereinsetzung § 52 OWiG pruefen

2. **OWi oder Strafrecht?** — Grenzwert: § 24a Abs. 1 StVG (0,5 Promille OWi) vs. § 316 StGB (ab 1,1 Promille oder Ausfallerscheinung = Strafrecht!); Geschwindigkeit: OWi immer.

3. **Fahrverbot oder Fahrerlaubnis-Entzug?** — § 25 StVG (OWi: 1-3 Monate, bleibt Fahrerlaubnis) vs. § 69 StGB (Strafrecht: Entziehung mit Sperrfrist).

## Ampel-Schnelldiagnose

| Situation | Ampel | Massnahme |
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
| Messverfahren-Angriffspunkte pruefen | `verkehrsowi-messverfahren-geschwindigkeit` |
| Beweisverwertung standardisiert | `verkehrsowi-beweisverwertung-standardisiert` |
| Alkohol / Drogen § 24a StVG | `verkehrsowi-alkohol-drogen-24a` |
| Fahreridentifizierung | `verkehrsowi-fahreridentifizierung` |
| Anhoerung / Bussgeldbescheid-Pruefung | `verkehrsowi-anhoerung-bussgeldbescheid` |
| Haertefall Fahrverbot | `verkehrsowi-haertefall-fahrverbot` |
| Punkte in Flensburg | `verkehrsowi-punkte-fahrverbot-flensburg` |
| Hauptverhandlung Amtsgericht | `verkehrsowi-hauptverhandlung-amtsgericht` |
| Rechtsbeschwerde | `verkehrsowi-rechtsbeschwerde` |
| Zeugen Polizei Strategie | `verkehrsowi-zeugen-polizei-strategie` |
| Rotlicht Abstand Handy | `verkehrsowi-rotlicht-abstand-handy` |
| Verjaehrung Zustellung | `verkehrsowi-verjaehrung-zustellung` |
| Mandantenkommunikation | `verkehrsowi-mandantenkommunikation` |
| Quality Gate | `verkehrsowi-quality-gate` |

## Zentrale OWi-Normen im Ueberblick

- **§ 24 StVG** — Ordnungswidrigkeiten im Strassenverkehr allgemein
- **§ 24a StVG** — Alkohol (0,5 Promille) und Drogen
- **§ 25 StVG** — Fahrverbot 1-3 Monate
- **§ 26 StVG** — Zustaendigkeit Bussgeldbehoerde
- **§ 67 OWiG** — Einspruch 2-Wochen-Frist
- **§ 77 OWiG** — Beweisaufnahme, Sachverstaendige
- **§ 79 OWiG** — Rechtsbeschwerde
- **§ 4 BKatV** — Regelfahrverbot und Abweichung bei Haertefall
- **Art. 103 Abs. 1 GG** — Rechtliches Gehoer, Rohmessdaten-Recht

## Querschnitts-Rechtsprechung

- BGH BGHSt 43, 277 — Standardisiertes Messverfahren befreit von Detailbegruendung, aber konkrete Einwaende sind aufzuklaeren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- OLG Bamberg NZV 2017, 494 — Sachverstaendigenantrag bei konkreten Messfehler-Angriffspunkten zwingend zu bescheiden.

## Harte Leitplanken

- OWi vs. Strafrecht immer zuerst klaeren — falsche Qualifikation ist schwerer Fehler.
- Frist immer zuerst sichern — kein Schritt vor Einspruch.
- Rohmessdaten grundsaetzlich anfordern.
- Anwaltliche Endkontrolle bei allen Fristen und Antraegen.
