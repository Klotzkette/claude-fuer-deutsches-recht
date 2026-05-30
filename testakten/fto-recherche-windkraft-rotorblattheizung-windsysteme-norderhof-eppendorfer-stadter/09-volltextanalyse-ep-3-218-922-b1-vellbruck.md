# 09 — Volltextanalyse EP 3 218 922 B1 (Vellbruck Energietechnik GmbH)

AZ: SE-2026-FTO-0717 | Bearb.: Dr. Stadter-Birkenhain | Stand: 14.02.2026

---

## 1. Bibliographische Daten

| Feld | Inhalt |
|---|---|
| Dokumentnummer | EP 3 218 922 B1 |
| Titel | Elektrothermisches Heizsystem für Rotorblätter einer Windkraftanlage |
| Anmelder | Vellbruck Energietechnik GmbH, Ammerländer Heerstr. 114–118, 26129 Oldenburg |
| Erfinder | Rolf-Dieter Vellbruck, Dipl.-Ing. Karsten Mehrtens, Dr. Britta Schumann-Ostergaard |
| Priorität | DE 10 2017 210 413.4, 22.06.2017 |
| Anmeldetag EP | 25.05.2018 |
| Veröffentlichung | 20.09.2023 (Erteilungsblatt) |
| Erteilungsdatum | 14.03.2023 |
| IPC | F03D 80/40, H05B 3/84, H05B 2203/016 |
| CPC | F03D 80/40, H05B 2203/016, H05B 3/84, Y02E 10/723 |
| Ansprüche | 21 (1 unabhängige Vorrichtung, 1 unabhängiges Verfahren, 1 unabhängiges Computerprogramm) |
| Validierungsstaaten | DE, FR, GB, NL, DK, SE, NO, FI, AT, ES, IT, PL, BE, CZ |
| Einspruch | Nordex Energy GmbH, 12.01.2024 — zurückgezogen 18.11.2024 |
| Entgegenhaltungen EPO | EP 2 462 344 A1, US 2016/0195073 A1, CN 106 121 921 A |

## 2. Kurzbeschreibung Erfindung (aus Abs. [0001]–[0012])

Die Erfindung betrifft ein elektrothermisches Heizsystem zur Verhinderung und Beseitigung von Eisansatz an Rotorblättern von Windkraftanlagen. Als technische Aufgabe wird in Absatz [0007] angegeben: die Bereitstellung eines Rotorblatt-Heizsystems, das (1) eine differentielle Heizleistung in verschiedenen Blattzonen ermöglicht, (2) eine präzise Eisdetektion ohne Beeinträchtigung der aerodynamischen Oberfläche gewährleistet, und (3) eine wartungsarme, kontaktlose Energieübertragung realisiert.

Als Stand der Technik werden in Abs. [0003]–[0006] folgende Systeme beschrieben und abgegrenzt: metallfolienbasierte Schleifringheizung (EP 2 462 344), thermische Heizung ohne Zonierung (DE 10 2014 223 614 A1), Druckimpulsenteisung (Siemens-Patente).

## 3. Beschreibung der bevorzugten Ausführungsform

Laut Beschreibung (Abs. [0040]–[0085]) umfasst die bevorzugte Ausführungsform:

**Heizmatten**: Gewebte Kohlenstofffaser-Matten mit definiertem elektrischen Widerstand, laminiert in die Glasfaser-Verbundstruktur des Rotorblatts. Widerstand je Zone einstellbar durch Vlies-Fasergewicht. Anschluss über integrierte Kupfersammelschienen.

**Heizzonen**: Mindestens drei Zonen (Z1: 0–3 m Blattspitze, Z2: 3–8 m, Z3: 8–25 m), jede mit eigenem Leistungsregler. In Abs. [0055] wird explizit ausgeführt, dass auch 4 oder mehr Zonen von der Erfindung umfasst sind.

**Kapazitive Sensorik**: Pro Zone min. 2 kapazitive Flächensensoren zur Bestimmung der lokalen dielektrischen Konstante, aus der auf die Eisdicke zurückgerechnet wird (Abs. [0060]–[0068]).

**Induktive Energieübertragung**: Primärspule stationär am Gondel-Rotorübergang; Sekundärspule auf Rotornabe. Ausführungsform mit einer Betriebsfrequenz von 20–100 kHz beschrieben. Übertragungsleistung bis 200 kW.

**Steuereinheit**: Mikrokontroller-basierter Regler, der Sensorwerte auswertet und Heizzonen-Relais steuert. Abs. [0078] beschreibt optional einen „lernenden Algorithmus" auf Basis historischer Betriebsdaten — Maschinenlernen explizit erwähnt aber als fakultativ (nicht in Anspruch 1 enthalten).

## 4. Anspruchsübersicht (alle 21 Ansprüche)

| Nr | Typ | Inhalt (Kurzform) |
|---|---|---|
| 1 | Unabhängig (Vorrichtung) | Gesamtsystem: Heizzonen + Kohlenstoffmaterial + kapazitive Sensorik + kontaktlose Übertragung + Steuereinheit |
| 2 | Abhängig v. 1 | Mindestens 3 Heizzonen |
| 3 | Abhängig v. 1 | Heizelement aus Kohlenstofffaservlies oder -gewebe |
| 4 | Abhängig v. 1 | Kapazitiver Sensor als Flächensensor |
| 5 | Abhängig v. 1 | Kapazitiver Sensor an Druck- und Saugseite |
| 6 | Abhängig v. 1 | Energieübertragung induktiv mit Frequenz 20–200 kHz |
| 7 | Abhängig v. 1 | Energieübertragung induktiv mit Wirkungsgrad > 90 % |
| 8 | Abhängig v. 1 | Schleifring als Alternative zu induktiver Übertragung (Alternativausf.) |
| 9 | Abhängig v. 1 | Steuereinheit mit Außentemperaturmessung |
| 10 | Abhängig v. 1 | Steuereinheit mit Wetterdaten-Anbindung |
| 11 | Abhängig v. 1 | Vorheizbetrieb bei Prognose-Schwellwert |
| 12 | Abhängig v. 1 | Alarmfunktion bei Eiswurf-Risiko |
| 13 | Unabhängig (Verfahren) | Verfahren zur Rotorblatt-Beheizung: Eisdetekt. kapazitiv → zonale Aktivierung |
| 14 | Abhängig v. 13 | Verfahren mit ML-basierter Prognose |
| 15 | Abhängig v. 13 | Verfahren mit Wetterdaten-Integration |
| 16 | Abhängig v. 13 | Verfahren mit prädiktivem Vorheizbetrieb |
| 17 | Abhängig v. 13 | Verfahren mit zonenindividueller Leistungsregelung |
| 18 | Abhängig v. 13 | Verfahren mit Energieoptimierung |
| 19 | Abhängig v. 13 | Verfahren mit Eiswurf-Warnsystem |
| 20 | Abhängig v. 13 | Verfahren mit Selbstdiagnose der Heizelemente |
| 21 | Unabhängig (SW/CRP) | Computerprogrammprodukt zur Durchführung des Verfahrens gem. Anspruch 13 |

## 5. Zeichnungen (Figuren 1–8)

- Fig. 1: Gesamtansicht Windkraftanlage mit eingezeichnetem Heizsystem
- Fig. 2: Rotorblatt-Querschnitt mit integrierten Heizmatten und Sammelschienen
- Fig. 3: Schematischer Aufbau Zonensteuerung (3 Zonen)
- Fig. 4: Kapazitiver Sensor-Aufbau (Flächensensor)
- Fig. 5: Induktiver Übertrager (Primär- und Sekundärspule)
- Fig. 6: Steueralgorithmus (Flussdiagramm) mit Eisdetektion und Zonenaktivierung
- Fig. 7: Diagramm Eisdicke vs. Kapazitätsmesswert (Kalibrierungskurve)
- Fig. 8: Systemarchitektur SCADA-Integration

## 6. Erste Einschätzung Schutzbereich

Der Schutzbereich von Anspruch 1 erstreckt sich nach dem Wortlaut und dem Protokoll zu Art. 69 EPÜ (Schutzumfang) auf alle Vorrichtungen, die die Merkmale (a)–(e) des Anspruchs 1 verwirklichen. Die Beschreibung zeigt, dass der Erfinder eine breite Technologieklasse schützen wollte (Abs. [0004]: „Die Erfindung ist nicht auf die in den Figuren dargestellten Ausführungsformen beschränkt").

Für IceFree v3 gilt vorläufig: Sämtliche 5 Merkmale des unabhängigen Anspruchs 1 erscheinen verwirklicht. → Verletzungsgefahr hoch. Vertiefung in Aktenstücken 10–12.

Quellen: [Espacenet — EP 3 218 922 B1](https://worldwide.espacenet.com/patent/search?q=EP3218922B1) | [EPO — Art. 69 EPÜ](https://www.epo.org/law-practice/legal-texts/epc/current-version-20130101/article/a69.html) | [dejure.org — § 14 PatG](https://dejure.org/gesetze/PatG/14.html)
