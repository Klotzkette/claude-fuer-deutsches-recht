# 10 — Anspruchsanalyse: Unabhängige Ansprüche 1, 13, 21 (EP 3 218 922 B1)

AZ: SE-2026-FTO-0717 | Bearb.: Dr. Stadter-Birkenhain | Stand: 17.02.2026

---

## 1. Methodik der Anspruchsanalyse

Die Anspruchsanalyse folgt der im deutschen und europäischen Patentrecht anerkannten Methode der Merkmalsanalyse (Feature Analysis):

1. Vollständiger Anspruchswortlaut wird in einzelne Merkmale (Features) aufgegliedert.
2. Jedes Merkmal wird nach Wortlaut und Beschreibung interpretiert.
3. Technischer Bedeutungsgehalt jedes Merkmals wird aus Beschreibung und Zeichnungen ermittelt.
4. Schutzbereichsinterpretation nach Art. 69 EPÜ i.V.m. Protokoll: weder streng wörtlich (zentrale Definition) noch zu weit (peripheres Prinzip); „fairer Schutzumfang".

## 2. Anspruch 1 — Merkmalsanalyse (Vorrichtungsanspruch)

Wortlaut Anspruch 1 (aus Erteilungsschrift EP 3 218 922 B1, Seite 12):

> „Elektrothermisches Heizsystem (1) für Rotorblätter (2) einer Windkraftanlage, dadurch gekennzeichnet, dass das System umfasst:
> (a) mindestens drei entlang der Längsachse des Rotorblatts (2) angeordnete Heizzonen (Z1, Z2, Z3) mit jeweils unterschiedlichen maximal abrufbaren Heizleistungsdichten;
> (b) in die Schichtstruktur des Rotorblatts (2) integrierte elektrische Heizelemente (4) aus einem kohlenstoffbasierten Widerstandsmaterial;
> (c) eine kapazitive Sensoranordnung (5) zur Messung der Eisdicke an der Außenoberfläche des Rotorblatts (2);
> (d) eine Vorrichtung (6) zur kontaktlosen Übertragung elektrischer Energie von einem stationären Teil der Windkraftanlage auf einen rotierenden Teil der Windkraftanlage; und
> (e) eine Steuereinheit (7), die dazu eingerichtet ist, anhand der von der Sensoranordnung (5) ermittelten Eisdicke die Heizzonen (Z1, Z2, Z3) individuell zu aktivieren und zu deaktivieren."

### Merkmalsgliederung Anspruch 1

| Merkmal | Bezeichnung | Wortlaut (Kurzform) |
|---|---|---|
| M1 | Oberbegriff | Elektrothermisches Heizsystem für Rotorblätter einer WKA |
| M2 | Heizzonen | Mind. 3 Zonen entlang Längsachse, unterschiedliche Heizleistungsdichten |
| M3 | Heizelemente | Kohlenstoffbasiertes Widerstandsmaterial, in Schichtstruktur integriert |
| M4 | Sensor | Kapazitive Sensoranordnung zur Eisdicken-Messung |
| M5 | Energieübertragung | Kontaktlos, stationär → rotierend |
| M6 | Steuereinheit | Aktivierung/Deaktivierung der Zonen anhand Sensorwerte |

### Interpretation der Merkmale

**M2 (Heizzonen)**: „Mindestens drei" schließt 4, 5 oder mehr ein. IceFree v3 hat 4 Zonen (A–D) — erfüllt. „Unterschiedliche maximal abrufbare Heizleistungsdichten" bedeutet, dass die Zonen verschiedene Nennleistungen aufweisen (nicht notwendigerweise gleichzeitig verschieden betrieben). IceFree v3: Zone A 8 kW/m, B 6 kW/m, C 3 kW/m — erfüllt.

**M3 (Heizelemente)**: „Kohlenstoffbasiertes Widerstandsmaterial" — Kohlefaservlies von IceFree v3 ist eindeutig kohlenstoffbasiert. „In die Schichtstruktur des Rotorblatts integriert" — IceFree v3: Lamination in Epoxydharz-Matrix — erfüllt. Entscheidende Frage: Fällt Kohlefaservlies unter „kohlenstoffbasiertes Widerstandsmaterial"? Nach Beschreibung Abs. [0042]: „Vorzugsweise wird als kohlenstoffbasiertes Widerstandsmaterial ein Kohlenstofffaservlies oder ein Kohlenstofffasergewebe verwendet." → Kohlefaservlies ist bevorzugte Ausführungsform — M3 durch IceFree v3 verwirklicht.

**M4 (Sensor)**: „Kapazitive Sensoranordnung zur Messung der Eisdicke" — IceFree v3 hat kapazitive Eisdickensensoren (3 pro Zone). Merkmal wörtlich erfüllt.

**M5 (Energieübertragung)**: „Kontaktlos" — IceFree v3 verwendet induktive Kopplung. Beschreibung EP 3 218 922 Abs. [0065]: Bevorzugte Ausführungsform ist induktive Kopplung. Wortlaut „kontaktlos" ist weiter als „induktiv" — auch andere kontaktlose Methoden wären erfasst. IceFree v3 erfüllt M5 wörtlich.

**M6 (Steuereinheit)**: „Aktivierung und Deaktivierung der Zonen anhand Sensorwerte" — Edge-Computing-Box von IceFree v3 macht genau das. Merkmal erfüllt.

## 3. Anspruch 13 — Merkmalsanalyse (Verfahrensanspruch)

Wortlaut Anspruch 13 (vereinfacht):

> „Verfahren zur Beheizung von Rotorblättern einer Windkraftanlage mittels eines elektrothermischen Heizsystems, umfassend die Schritte:
> (i) Messen der Eisdicke an der Rotorblattoberfläche mittels kapazitiver Sensoren;
> (ii) Bestimmen eines zonenspezifischen Aktivierungssignals für mindestens 3 Heizzonen anhand der gemessenen Eisdicke;
> (iii) Kontaktloses Übertragen elektrischer Energie von stationär auf rotierend;
> (iv) Aktivieren der ermittelten Heizzonen."

IceFree v3 führt alle 4 Verfahrensschritte aus. Eine Verletzung von Anspruch 13 ist wahrscheinlich, wenn das System in Betrieb genommen wird (§ 9 Nr. 1 PatG: „Benutzen").

## 4. Anspruch 21 — Computerprogrammanspruch

Anspruch 21 schützt ein Computerprogrammprodukt, das bei Ausführung auf einem Prozessor das Verfahren nach Anspruch 13 durchführt. Die Software-Steuerungslogik von IceFree v3 würde bei Ausführung auf der Edge-Computing-Box des Systems die Schritte i–iv ausführen. → Anspruch 21 verletzt, wenn das Programm in Deutschland vertrieben oder angeboten wird.

## 5. Gesamtergebnis Anspruchsanalyse

| Anspruch | Art | IceFree v3 verwirklicht? | Verletzungsmodus |
|---|---|---|---|
| 1 | Vorrichtung | Ja — alle 6 Merkmale | Herstellung, Anbieten, Inverkehrbringen, § 9 Nr. 1 PatG |
| 13 | Verfahren | Ja — alle 4 Schritte | Benutzen, § 9 Nr. 3 PatG |
| 21 | Software | Ja | Anbieten der Software, § 9 Nr. 1 PatG analog |
| 2–12 | Abhängig v. 1 | Teils ja (M2–M7) | Keine eigenständige Verletzung nötig |
| 14–20 | Abhängig v. 13 | Teils ja | Benutzen mit erweiterten Merkmalen |

Ergebnis: FTO-Status **ROT** für alle drei unabhängigen Ansprüche.

Quellen: [dejure.org — § 9 PatG](https://dejure.org/gesetze/PatG/9.html) | [dejure.org — § 14 PatG](https://dejure.org/gesetze/PatG/14.html) | [EPO — Protokoll Art. 69 EPÜ](https://www.epo.org/law-practice/legal-texts/epc/current-version-20130101/article/a69.html) | [BGH X ZR 156/12 Äquivalenz](https://www.bundesgerichtshof.de)
