# 11 — Merkmalsvergleich: Windsysteme IceFree v3 vs. Vellbruck EP 3 218 922 B1

AZ: SE-2026-FTO-0717 | Bearb.: Dr. Stadter-Birkenhain | Stand: 20.02.2026

---

## 1. Einleitung und Methodik

Der vorliegende Merkmalsvergleich stellt die Ausführungsform IceFree v3 des Mandanten (Windsysteme Norderhof AG) den Merkmalen der unabhängigen Ansprüche 1 und 13 des EP 3 218 922 B1 (Vellbruck Energietechnik GmbH) gegenüber. Die Prüfung umfasst:

- Identität: wörtliche Verwirklichung jedes Merkmals.
- Äquivalenz: Verwirklichung mit abgewandeltem Mittel, das die gleiche Wirkung mit dem gleichen Gedankengang erzielt (BGH X ZR 156/12 — Dreifrage-Test).
- Vorveröffentlichung: Ob das Merkmal bereits im Stand der Technik vor dem Prioritätstag 22.06.2017 bekannt war (Relevanz für Nichtigkeitsklage).

## 2. Merkmalsvergleich Anspruch 1

| Nr | Merkmal Anspruch 1 | IceFree v3 Ausführung | Identität | Äquivalenz | Anmerkung |
|---|---|---|---|---|---|
| M1 | Elektrothermisches Heizsystem für Rotorblätter einer WKA | Elektrothermisches Rotorblatt-Enteisungssystem | JA | — | Oberbegriff identisch |
| M2 | Mind. 3 Heizzonen entlang Längsachse, unterschiedliche Leistungsdichten | 4 Zonen (A–D), Leistung 8/6/3/0 kW/m | JA | — | 4 > 3, Merkmal vollständig erfüllt |
| M3 | Kohlenstoffbasiertes Widerstandsmaterial, in Schichtstruktur integriert | Kohlefaservlies, VARTM-laminiert in Epoxydharz | JA | — | Kohlefaservlies = kohlenstoffbasiert lt. EP-Beschreibung Abs. [0042] |
| M4 | Kapazitive Sensoranordnung zur Eisdicken-Messung | Kapazitive Sensoren (3/Zone), Messbereich 0–30 mm | JA | — | Wörtlich identisch |
| M5 | Kontaktlose Übertragung stationär → rotierend | Induktive Kopplung (induktiver Übertrager) | JA | — | Induktiv = kontaktlos, bevorzugte Ausf. im Patent |
| M6 | Steuereinheit: zonale Aktivierung/Deaktivierung anhand Sensorwerte | Edge-Computing-Box mit Zonen-Relais-Steuerung | JA | — | Wörtlich identisch |

**Ergebnis Anspruch 1: Alle 6 Merkmale wörtlich verwirklicht. Verletzung wahrscheinlich.**

## 3. Merkmalsvergleich Anspruch 13 (Verfahren)

| Nr | Merkmal Anspruch 13 | IceFree v3 Betriebsweise | Identität | Äquivalenz |
|---|---|---|---|---|
| V1 | Messen der Eisdicke mittels kapazitiver Sensoren | Kapazitive Messung 3×/Zone in Echtzeit | JA | — |
| V2 | Bestimmen zonenspezifischen Aktivierungssignals | Edge-AI: Eisbildungs-Score → Zonenentscheidung | JA | — |
| V3 | Kontaktlose Energieübertragung stationär → rotierend | Induktiver Übertrager, 50 Hz | JA | — |
| V4 | Aktivieren ermittelter Heizzonen | Zonenrelais aktivieren Heizmatten | JA | — |

**Ergebnis Anspruch 13: Alle 4 Verfahrensschritte verwirklicht. Verletzung des Verfahrensanspruchs wahrscheinlich.**

## 4. Mögliche Unterschiede und Gegenargumente

Die folgende Tabelle zeigt Argumente, die der Mandant möglicherweise zur Verteidigung (design-around oder Nichtverletzungsargument) vorbringen könnte, sowie deren vorläufige Bewertung:

| Argument | Bewertung |
|---|---|
| IceFree v3 hat 4 Zonen, Anspruch nennt „mind. 3" | Kein Unterschied — „mind. 3" schließt 4 ein. Kein Differenzierungsargument. |
| Induktive Kopplung ist spezifischer als „kontaktlos" | Nein — „kontaktlos" ist der Oberbegriff; induktiv ist eine Form. Keine Einschränkung. |
| ML-Algorithmus in Steuereinheit ist nicht in Anspruch 1 enthalten | Richtig — ML ist nur in Anspruch 14 (abhängig). Kein Differenzierungsargument für Anspruch 1. |
| Zonen-Heizleistung in IceFree v3 dynamisch (nicht nur statisch unterschiedlich) | Anspruch spricht von „maximal abrufbaren Heizleistungsdichten" — statische Maximalwerte. Dynamischer Betrieb ist Untermenge. Kein Differenzierungsargument. |
| Zone D (Blattwurzel) nicht beheizt → IceFree v3 hat effektiv 3 aktive Zonen | Zone D ist konstruktiv vorhanden aber inaktiv. Anspruch sagt „mindestens 3 Heizzonen" — ob aktiv oder potentiell aktiv, ist nicht spezifiziert. Schwaches Argument. |

Vorläufige Einschätzung: Kein valides Nichtverletzungsargument auf Basis reiner Wortlautanalyse erkennbar. Hauptansatz muss Nichtigkeitsklage oder Lizenz sein.

## 5. Identifizierte Redesign-Ansätze (vorläufig)

Für eine mögliche Design-Around-Strategie (Aktenstück 17) wurden folgende technische Eingriffspunkte identifiziert:

- **Sensor-Substitution**: Ersatz kapazitive Sensor durch optische Eisdetektion (Lidar oder Infrarot-Kamera) würde M4 nicht mehr erfüllen. Technisch möglich, aber erhöhter Aufwand und höhere Kosten.
- **Energieübertragung Schleifring**: Rückkehr zu Schleifring-Bürsten-System (wie IceFree v1/v2) würde M5 potenziell nicht unter Anspruch 1 fallen lassen — aber: Anspruch 8 der Vellbruck schützt auch Schleifring als Alternative. Kein FTO-Gewinn.
- **Material-Substitution**: Verwendung von nicht-kohlenstoffbasiertem Widerstandsmaterial (z.B. Metallfolie-Heizer). Würde M3 nicht erfüllen. Technisch rückschrittlich, aufwändig.

## 6. Fazit

Auf Basis der Merkmalsanalyse ist eine direkte Verletzung von Anspruch 1 und Anspruch 13 des EP 3 218 922 B1 durch IceFree v3 bei Herstellung, Anbieten, Inverkehrbringen oder Benutzen in den Validierungsstaaten (insb. DE) wahrscheinlich. Die Äquivalenzprüfung (Aktenstück 12) wird diese Analyse ergänzen.

Quellen: [dejure.org — § 9 PatG](https://dejure.org/gesetze/PatG/9.html) | [BGH X ZR 156/12](https://www.bundesgerichtshof.de) | [EPO — Art. 69 EPÜ Protokoll](https://www.epo.org/law-practice/legal-texts/epc/current-version-20130101/article/a69.html)
