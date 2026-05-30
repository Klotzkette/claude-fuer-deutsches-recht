# 02 — Technologiebeschreibung Rotorblattheizung IceFree v3

AZ: SE-2026-FTO-0717 | Bearb.: Dr. Eppendorfer | Stand: 21.01.2026

---

## 1. Überblick IceFree v3

IceFree v3 ist das dritte Produktionssystem der Windsysteme Norderhof AG zur Rotorblattheizung (Vorgänger: IceFree v1 2018, v2 2021). Das System adressiert die Vereisung von Rotorblättern bei Windkraftanlagen unter Umgebungstemperaturen von −15 °C bis +2 °C bei gleichzeitigem Auftreten von unterkühltem Regen, Nebel oder Schnee (IEC 61400-1 Klimaklasse Ice Zone T).

Eisbildung an Rotorblättern führt zu:

- Aerodynamischen Verlusten (bis −20 % Energieertrag je Eisbildungsereignis)
- Unwucht und erhöhter mechanischer Belastung (Lager, Getriebe)
- Eiswurf-Risiko (Sicherheitsrelevanz, Haftung des Betreibers)
- Abschaltpflichten nach TA Lärm und Betreibergenehmigung

## 2. Systemarchitektur IceFree v3

### 2.1 Heizelemente (Heizmatten)

Material: Kohlefaservlies-Widerstandsheizer (spez. Widerstand ca. 12 Ω·cm), eingebettet in Epoxydharz-Matrix. Fertigungsverfahren: Infusionstechnologie (VARTM). Positionierung: Im Bereich 0–5 m Rotorblattspitze (Hochrisikozone) und 5–20 m (Mittelzone), jeweils auf Druckseite und Saugseite.

Heizzonen (zonales Heizmanagement):
- Zone A: 0–2 m (Spitze), max. 8 kW/m, dauerhafter Betrieb bei Eiserkennung
- Zone B: 2–5 m (äußerer Bereich), 6 kW/m, pulsgesteuerter Betrieb
- Zone C: 5–20 m (Mittelzone), 3 kW/m, Intervallbetrieb
- Zone D: 20 m – Blattwurzel, nicht beheizt (thermisch unkritisch)

### 2.2 Schleifringstromübertrager

Typ: Kontaktloser induktiver Übertragung (IceFree v3 NEU gegenüber v1/v2: v1/v2 nutzten Schleifring-Bürstensysteme). Leistungsübertragungskapazität: bis 120 kW pro Rotorblatt. Frequenz: 50 Hz. Übertragungseffizienz: > 96 %.

Hinweis für FTO: Der Wechsel von Schleifring auf induktive Kopplung ist ein potenzieller Differenzierungspunkt gegenüber älteren Patenten, aber EP 3 218 922 B1 deckt nach Erstlektüre beide Varianten über Unteranspruch 8 ab.

### 2.3 Eisdetektion und Sensorik

Primärsensorik: Kapazitive Eisdickensensoren (Messbereich 0–30 mm Eis, Genauigkeit ±0,5 mm), integriert in die Blattoberfläche, je 3 Sensoren pro Zone. Sekundärsensorik: PT100-Temperatursensoren (Blattoberfläche und Luft), Vibrationssensoren (MEMS-Beschleunigungssensor).

Algorithmus: Machine-Learning-Modell (Random Forest + physikalisches Modell), trainiert auf 4 Jahre Betriebsdaten (2021–2024) von 12 Windparks in Norddeutschland und Skandinavien. Entscheidungslogik: Eisbildungs-Score (0–100), Schwellwert 35 für Vorheizbetrieb, Schwellwert 65 für Volllastbetrieb.

### 2.4 Steuereinheit (Edge-Computing-Box)

Hardware: Intel Atom-basiertes Embedded System, IP67, Temperaturbereich −40°C bis +70°C. Software: Linux RTOS, Python 3.11 Steuerungslogik, MQTT-Datenprotokoll zur Windpark-SCADA. Kommunikation: CAN-Bus intern, Ethernet extern.

Wetterdaten-Integration: API-Anbindung an DWD (Deutscher Wetterdienst) und ECMWF-Ensemble-Prognosen für predictive anti-icing (Vorheizstrategie).

## 3. Abgrenzung IceFree v3 zu Vorprodukten

| Merkmal | IceFree v1 (2018) | IceFree v2 (2021) | IceFree v3 (2026) |
|---|---|---|---|
| Heizelement | Metallfolie-Heizer | Glasfaser-Heizer | Kohlefaservlies |
| Stromübertragung | Schleifring-Bürste | Schleifring-Bürste | Induktiv (kontaktlos) |
| Zonierung | 2 Zonen | 4 Zonen | 4 Zonen + prädiktiv |
| Eisdetektion | Vibrationssensor | Vibr. + Temp. | Kapazitiv + ML |
| Steuerung | Einfach-SPS | PLC + Wetterdaten | Edge-AI + ECMWF |
| Leistung | 60 kW | 90 kW | 120 kW |

## 4. Patentstatus eigene Anmeldungen Windsysteme Norderhof AG

| Dokument | Anmeldetag | Status | Kernmerkmal |
|---|---|---|---|
| DE 10 2022 134 511 A1 | 22.12.2022 | Anhängig, kein Bescheid | Kohlefaservlies-Heizer |
| EP 22 834 190.2 | 22.12.2022 (PCT) | Recherchebericht 14.11.2024 | Gesamtsystem |
| US 18/723,441 | 20.06.2024 (national phase) | Ausstehend | Gesamtsystem |
| CN 202380012741.X | 20.06.2024 (national phase) | Ausstehend | Gesamtsystem |

Hinweis: Eigene anhängige Anmeldungen des Mandanten schaffen keine FTO — nur erteilte Patente begründen Ausschließungsrechte. Der Mandant hat derzeit keine erteilten Patente auf IceFree v3.

## 5. Anspruchsrelevante Kernmerkmale für FTO

Folgende Merkmale sind für den Merkmalsvergleich mit Hindernispatenten prioritär zu untersuchen:

1. Kohlefaservlies als Widerstandsheizelement, integriert in Rotorblattstruktur
2. Zonales Heizmanagement (mindestens 3 Zonen mit unterschiedlichen Leistungsdichten)
3. Induktive (kontaktlose) Energieübertragung auf rotierende Komponente
4. Kapazitive Eisdetektion an Rotorblattoberfläche
5. ML-basiertes Eisbildungsmodell zur prädiktiven Heizsteuerung
6. Integration von Außenwetterdaten (Wetterdienst-API) in Steueralgorithmus
7. Steuereinheit als Edge-Computing-System mit Echtzeit-Sensorauswertung

Quellen: [DPMA Patentdatenbank](https://www.dpma.de) | [EPO Espacenet](https://www.epo.org/en/searching-for-patents/technical/espacenet.html) | IEC 61400-1 Ed. 4 (2019)
