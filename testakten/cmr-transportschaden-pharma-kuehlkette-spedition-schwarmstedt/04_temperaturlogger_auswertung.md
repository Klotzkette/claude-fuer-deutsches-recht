# Temperaturlogger-Auswertung — DataTrack 4000

Akte: LG Hannover 9 O 244/26
Fahrzeug: Scania R 450, Kennzeichen B-44-PTT / Auflieger B-88-RKL
Loggernr.: DT4-2025-7783
Auswertung: RAin Dr. Antonia Hammerschmidt / Sachverständigenbüro Prof. Dr. H. Kretschmann (TU Hamburg)
Stand: 25. März 2026

---

## 1. Gerät und Technische Spezifikation

Das DataTrack 4000 ist ein zertifizierter Temperaturlogger für pharmazeutische Kühlkettentransporte. Der Logger erfüllt die Anforderungen der EU-GMP-Leitlinien (Kapitel 3, Qualifizierung) und der WHO PQS-Spezifikation E 06/TR03. Aufzeichnung alle 5 Minuten, interner Speicher 2.000 Datenpunkte, GSM-Echtzeit-Übertragung an Petrescu Transport SRL Dispatcher-Software sowie an die Schwarmstedt-Leitstelle (Softrack 7, Soltau).

**Technischer Hinweis:** Die DataTrack 4000 Betriebsanleitung (Rev. 2024-3) schreibt vor, dass bei Überschreitung der eingestellten Grenzwerte (hier: +8°C obere Alarmschwelle) ein akustischer Alarm im Fahrerhaus ertönt und eine SMS an die hinterlegten Nummern gesendet wird. Im vorliegenden Fall wurde nach bisheriger Feststellung weder eine SMS-Meldung empfangen noch ist dokumentiert, dass der Fahrerhaus-Alarm ausgelöst hat. Dies ist aufklärungsbedürftig.

---

## 2. Rohdaten — Kritische Phase (13./14. Januar 2026)

| Uhrzeit (UTC+1) | Temp. [°C] | Status | Bemerkungen |
|---|---|---|---|
| 23:00 | +7,1 | Normal | Letzte manuelle Fahrerüberprüfung laut Protokoll |
| 23:05 | +7,2 | Normal | — |
| 23:30 | +7,4 | Normal | — |
| 00:00 | +7,6 | Normal | Fahrzeugstopp A6, Raststätte Bourg-en-Bresse Ost |
| 00:30 | +7,7 | Normal | — |
| 01:00 | +7,8 | Normal | — |
| 01:30 | +7,9 | Normal | — |
| 02:00 | +7,8 | Normal | — |
| 02:30 | +7,7 | Normal | — |
| 03:00 | +7,9 | Normal | — |
| 03:05 | +7,8 | Normal | — |
| 03:10 | +7,9 | Normal | — |
| 03:15 | +8,0 | Grenzwert | Exakt obere Grenze, noch kein Alarm |
| **03:18** | **+8,3** | **ALARM** | **Obere Alarmgrenze überschritten** |
| 03:23 | +9,1 | ALARM | Anstieg kontinuierlich |
| 03:28 | +10,4 | ALARM | — |
| 03:33 | +11,8 | ALARM | — |
| 03:38 | +13,2 | ALARM | — |
| **03:41** | **+14,3** | **ALARM** | **Peak-Temperatur** |
| 03:46 | +13,7 | ALARM | Beginn Abkühlung |
| 03:51 | +11,1 | ALARM | — |
| **03:54** | **+7,9** | **Normal** | **Ende Überschreitung (36 Minuten)** |
| 03:59 | +7,6 | Normal | — |
| 04:30 | +7,2 | Normal | — |
| 05:00 | +7,1 | Normal | — |
| 05:45 | +6,8 | Normal | Fahrzeug verlässt Raststätte (Weiterfahrt nach Lyon) |
| 08:22 | +7,0 | Normal | Ankunft Empfangsrampe HCL Lyon |

---

## 3. Beurteilung durch Sachverständigen Prof. Dr. Kretschmann

Prof. Dr. Horst Kretschmann (Institut für Kühltechnik und Thermodynamik, TU Hamburg-Harburg) hat am 22. März 2026 ein vorläufiges Gutachten (Ref. TUH-KT-2026-0088) erstattet. Kernaussagen:

### 3.1 Ursache des Temperaturanstiegs

"Der Temperaturverlauf ab ca. 03:15 Uhr ist charakteristisch für einen kombinierten Effekt: (a) Aufwärmung des Laderaums durch Wärmeeinleitung von außen (Nachttemperatur Bourg-en-Bresse ca. +3°C, also kein starker externer Wärmeeintrag) und (b) vorübergehende Unterbrechung der aktiven Kühlung. Der steile Anstieg auf +14,3°C innerhalb von 23 Minuten ist mit einem bloßen Wärmeeintrag durch Laderaumöffnung nicht vollständig erklärbar; wahrscheinlicher ist eine kurzzeitige Abschaltung des Kühlaggregats oder ein elektronischer Reset des Carrier-Systems."

"Die Abkühlung ab 03:41 Uhr erfolgt ebenfalls steil, was auf eine Wiederaufnahme der aktiven Kühlung hindeutet. Ein 'natürliches' Abkühlen bei +3°C Außentemperatur wäre deutlich langsamer."

**Zwischenergebnis Ursache:** Wahrscheinlich technische Unterbrechung des Kühlaggregats, nicht primär Fahrerfehler. Dies ist für Art. 29 CMR bedeutsam.

### 3.2 Schadensbeurteilung Pharmazeutika

"Monoklonale Antikörper (mAb) sind thermolabile Proteinverbindungen. Bei Temperaturexposition >8°C für mehr als 30 Minuten ist eine irreversible Denaturierung oder Aggregatbildung wahrscheinlich. Der QS-Bericht HCL-QA-2026-0011 ist in seiner Schlussfolgerung (95 von 144 Vials unbrauchbar) plausibel, obwohl eine zerstörungsfreie Überprüfung nicht möglich ist. Zu prüfen ist, ob alle 12 Isotherm-Boxen gleichmäßig betroffen waren oder ob aufgrund der Lagestabilität innerhalb des Laderaums einzelne Bereiche weniger exponiert waren."

### 3.3 Alarmversagen DataTrack 4000

"Das Nichtauslösen des akustischen Alarms und der SMS-Benachrichtigung trotz nachgewiesener Temperaturüberschreitung ist technisch erklärungsbedürftig. Mögliche Ursachen: (a) Fehler in der Alarmkonfiguration des Geräts, (b) GSM-Funkloch im Bereich der Raststätte A6 (zu prüfen mit Netzbetreiberdaten), (c) defekte interne Alarmfunktion. Ich empfehle die physische Begutachtung des DataTrack 4000 Geräts."

---

## 4. Rechtliche Folgewirkung der Sachverständigenaussage

### 4.1 Für Art. 29 CMR

Wenn die Ursache ein technischer Kühlaggregat-Defekt war:
- Kein leichtfertiges Handeln des Fahrers im Sinne von Art. 29 CMR
- Möglicherweise Produkthaftung des Kühlaggregat-Herstellers (Carrier Transicold, ggf. Garantieansprüche)
- Schwarmstedt hat Kühlaggregat-Wartungspflichten zu erfüllen (§ 3 Abs. 1 StVZO, ADR Abs. 9.2); zu prüfen: War das Aggregat ordnungsgemäß gewartet?

Wenn der Fahrer das Kühlaggregat bewusst oder fahrlässig abgeschaltet hat:
- Einfache Fahrlässigkeit: Art. 23 Abs. 3 CMR anwendbar
- Leichtfertigkeit: Nur wenn Bewusstsein der Wahrscheinlichkeit, dann Art. 29 CMR

### 4.2 Für Wartungsprotokoll

Petrescu Transport SRL ist nach Art. 3 CMR für Wartungszustand verantwortlich. Schwarmstedt muss darüber hinaus nach § 7a Abs. 1 GüKG und GDP-Anforderungen die Eignung des Subunternehmers nachgewiesen haben. Zu klären: Hat Schwarmstedt das Kühlfahrzeug der Petrescu Transport SRL vor Auftragsvergabe auf GDP-Konformität geprüft?

---

## 5. Wartungsprotokoll Kühlaggregat (Auszug, Petrescu Transport SRL)

| Datum | Wartungsart | Werkstatt | Befund | Unterschrift |
|---|---|---|---|---|
| 15.09.2025 | Jahreswartung Carrier | Frigosped SRL, Bukarest | Keine Mängel | B. Petrescu |
| 05.11.2025 | Ölwechsel Aggregat | Frigosped SRL, Bukarest | Ölstand ok | C. Petrescu |
| 10.01.2026 | Kurzinspektion vor Fahrtantritt | — (Eigeninspektion) | Ok, Kühlkette geprüft | C. Petrescu |

Das Wartungsprotokoll liegt in rumänischer Sprache vor; eine notariell beglaubigte Übersetzung ist anzufertigen.

---

## 6. Zusammenfassung kritische Punkte

1. **Ursache ungeklärt:** Technisches Versagen vs. Fahrerfehler — entscheidend für Art. 29 CMR
2. **Alarm-Versagen:** DataTrack 4000 hat trotz Überschreitung nicht ausgelöst; mögliche Produkthaftung
3. **Exposition:** 36 Minuten über +8°C, Peak +14,3°C — medizinisch-fachlich reicht das für Denaturierung
4. **Schadensbegutachtung MediVita:** 95 von 144 Vials vernichtet; sachverständige Gegenprüfung notwendig
5. **Überprüfungslücke:** Keine Fahrerüberprüfung über 6 Stunden (23:00 bis 05:00 Uhr) — möglicherweise Obliegenheitsverletzung, aber kein Art. 29 CMR-Sachverhalt ohne Bewusstsein des Schadens

---

## 7. Maßnahmen

- [ ] Physische Begutachtung DataTrack 4000 durch Kretschmann (Termin 10. April 2026)
- [ ] Netzbetreiberabfrage GSM-Abdeckung A6 / Bourg-en-Bresse (03:00 bis 04:00 Uhr, 14.01.2026)
- [ ] Carrier Transicold Deutschland GmbH: Wartungshistorie Aggregat anfordern
- [ ] Notariell beglaubigte Übersetzung Wartungsprotokoll Petrescu
- [ ] Gegengutachten QS-Bericht HCL-QA-2026-0011 (Ladungsverteilung in Isotherm-Boxen)
