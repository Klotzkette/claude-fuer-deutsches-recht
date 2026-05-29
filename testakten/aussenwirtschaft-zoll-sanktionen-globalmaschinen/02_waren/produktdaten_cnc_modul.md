# Produktdaten und Klassifizierungsbegründung: CNC-Steuermodul GX-900

**Dokumenttyp:** Technisches Datenblatt / Klassifizierungsmemo  
**Erstellt:** 14. April 2026  
**Verfasser:** Dipl.-Ing. Rainer Hofstädter, Exportkontrollbeauftragter  
**Aktenzeichen:** GM-EK-2026-041  
**Vertraulichkeit:** Intern / Für Behörden freigegeben

---

## 1. Produktbezeichnung und Identifikation

| Merkmal | Wert |
|---|---|
| Handelsname | CNC-Steuermodul GX-900 |
| Interne Artikelnummer | 8000-GX900-EU |
| Hersteller | Globalmaschinen GmbH, Rotebühlplatz 18, 70178 Stuttgart |
| Entwicklungsstand | Revision 3.2 (Stand: 01/2026) |
| Seriennummernformat | GX9-JJJJ-XXXXXX |
| EAN | 4012345678901 |
| Herstellungsort | Stuttgart-Zuffenhausen (Montage), Prozessorkern: USA |

Das CNC-Steuermodul GX-900 ist ein hochintegriertes Steuerungssystem für numerisch gesteuerte Werkzeugmaschinen (Computer Numerical Control). Es wird von der Globalmaschinen GmbH sowohl in eigene Maschinen eingebaut (OEM-Variante) als auch als Ersatzteil für Bestandsmaschinen anderer Hersteller angeboten (Aftermarket-Variante).

---

## 2. Technische Spezifikationen

### 2.1 Kerndaten

| Parameter | Spezifikation |
|---|---|
| Prozessorkern | Quad-Core ARM Cortex-A72, 1,8 GHz, US-Ursprung (Chip-Design: Sunnyvale/CA) |
| Betriebssystem | RTOS LinuxCNC 2.9 (Open Source, angepasst) |
| Achssteuerung | bis zu 9 simultane CNC-Achsen (3+3+3 Konfiguration) |
| Positioniergenauigkeit | ≤ 0,001 mm (1 μm) bei Vollausbau |
| Schnittstellen | EtherCAT (IEC 61158), Profinet, RS-232/RS-485, USB 3.0, Ethernet 1 GbE |
| Firmware-Update | Over-the-Air (OTA) über gesichertes Cloud-Portal (TLS 1.3, AES-256) |
| Verschlüsselungsmodul | integrierter Hardware Security Module (HSM) Atmel ATECC608A |
| Schutzart | IP54 |
| Betriebstemperatur | -10 °C bis +55 °C |
| Versorgungsspannung | 24 V DC ±10 % |
| Abmessungen (LxBxH) | 385 × 290 × 72 mm |
| Gewicht | 2,4 kg |
| Konformität | CE, RoHS 2, REACH |

### 2.2 Servoantrieb-Schnittstelle

Das Modul steuert Servoantriebe über den EtherCAT-Bus mit einer Zykluszeit von 250 μs. Die Servoschnittstelle unterstützt die Profile CiA 402 und SoE. Maximale Ausgangssignalfrequenz an den Encoder-Eingängen: 4 MHz (Quadratur). Die Achsinterpolation ist linear und zirkulär (G01/G02/G03 konform nach DIN 66025).

### 2.3 Cloud-Konnektivität und Fernwartung

Die OTA-Updatefunktion nutzt ein herstellereigenes Cloud-Backend (Server: AWS Frankfurt, Region eu-central-1). Der Zugang ist zertifikatsbasiert (X.509), Geräteidentifikation über eindeutige Seriennummer. Der Export von Maschinendaten (Fertigungsparameter, Fehlerprotokolle) ist konfigurierbar und kann im Offline-Modus vollständig deaktiviert werden. Eine Fernsteuerung des Moduls über die Cloud ist technisch nicht implementiert; das Portal beschränkt sich auf Firmware-Distribution und Diagnosedaten.

### 2.4 Verschlüsselung

Der integrierte HSM (ATECC608A) implementiert:
- AES-128/256 (symmetrisch)
- SHA-256/384 (Hashfunktionen)
- ECDSA P-256/P-384 (Signatur)
- ECDH P-256 (Schlüsselvereinbarung)

Die maximale Schlüssellänge beträgt 256 Bit (symmetrisch) bzw. 384 Bit (asymmetrisch ECC). Das Modul ist **nicht** für militärische Verschlüsselung ausgelegt und erfüllt nicht FIPS 140-3 Level 3.

---

## 3. Typische Endverwendung

Das GX-900 wird primär eingesetzt in:
- Dreh- und Fräsmaschinen (zivile Fertigung, Metallbearbeitung)
- Holzbearbeitungszentren
- Laserschneidanlagen (Einbindung als Interpolationsmodul)
- Retrofit-Vorhaben: Modernisierung älterer CNC-Maschinenparks

Kundenbranchen: Maschinenbau, Automobilindustrie, Werkzeugbau, Luft- und Raumfahrtzulieferer (Strukturbauteile, keine Waffensysteme), Medizintechnik (Fräsen von Implantaten).

---

## 4. Klassifizierungsanalyse nach EU-Dual-Use-Verordnung (VO EU 2021/821)

### 4.1 Vorgehensweise

Die Klassifizierung erfolgt anhand der Anhänge I (Güterliste) der EU-Dual-Use-Verordnung (EU) 2021/821, ergänzt durch den Vergleich mit der US-amerikanischen Export Administration Regulations (EAR), Commerce Control List (CCL).

### 4.2 Prüfungsschritt 1: Numerische Steuerungen – Kategorie 2B

**Einstiegspunkt:** Kategorie 2 (Materialbearbeitung), Untergruppe B (Ausrüstung).

Gemäß Position **2B001.b.1** der EU-Dual-Use-Güterliste sind numerische Steuerungssysteme für Werkzeugmaschinen zu prüfen, wenn sie für mehr als 5 simultane, interpolierend gesteuerte Achsen ausgelegt sind.

**Befund:** Das GX-900 steuert bis zu **9 simultane Achsen** mit Interpolation – dies überschreitet den Schwellenwert von 5 Achsen nach 2B001.b.1. Das Modul ist daher **grundsätzlich listenpflichtig** als Steuerungssystem für Werkzeugmaschinen i.S.v. 2B001.

### 4.3 Prüfungsschritt 2: Positioniergenauigkeit

Position 2B001 setzt voraus, dass die Positioniergenauigkeit besser als:
- ≤ 6 μm bei linearen Achsen (nach VDI/DGQ 3441 oder ISO 230-2)

Das GX-900 erreicht ≤ 1 μm – unterschreitet damit die Schwelle erheblich.

**Befund:** Der Genauigkeitsparameter liegt innerhalb des kontrollierten Bereichs.

### 4.4 Prüfungsschritt 3: Informationssicherheitsfunktionen – Kategorie 5 Teil 2

Das integrierte HSM mit AES-256 und ECC-384 ist auf Tauglichkeit für Position **5E002** (Software für die Entwicklung oder Produktion von Gütern der Pos. 5A002) zu prüfen. Pos. 5A002.a umfasst Systeme zur Sicherung von Informationen mittels kryptographischer Methoden.

**Ausnahme:** Note 3 zu Kategorie 5 Teil 2 (Cryptography Note / "CN") sieht eine Freistellung vor, wenn die kryptographischen Funktionen nicht das primäre Element der Ware sind und die Ware für einen allgemeinen, kommerziellen Zweck (ohne selektive Kontrollmöglichkeit) entwickelt wurde. Das GX-900 nutzt den HSM ausschließlich zur Integritätssicherung von Firmware-Updates und Gerätezertifikaten, nicht zur Verschlüsselung von Kommunikationsinhalten im Sinne einer Vertraulichkeitslösung.

**Befund:** Die CN (Cryptography Note) greift mit hoher Wahrscheinlichkeit; eine Einstufung unter 5A002/5E002 ist nicht indiziert. Eine formelle BAFA-Anfrage zur Bestätigung wird empfohlen.

### 4.5 Prüfungsschritt 4: US-EAR-Bezug (ECCN)

Der Prozessorkern (ARM Cortex-A72 basierend auf US-IP, Chip-Design Sunnyvale/CA) unterliegt potenziell der US-Exportkontrolle (EAR, 15 CFR Part 774, CCL). Relevante ECCN-Kandidaten:

| ECCN | Beschreibung | Treffer? |
|---|---|---|
| 3A991 | Prozessoren, nicht unter 3A001 | Wahrscheinlich Ja |
| 3E001 | Technologie für Güter nach 3A001 | Nein (kein Transfer von Technologie) |
| 2B001 | Werkzeugmaschinen-Steuerungen | Parallel-Klassifizierung möglich |
| EAR99 | Nicht kontrolliert, Freirestkategorie | Ausschluss prüfen |

Der ARM Cortex-A72 als Commodity-Prozessor fällt nach aktueller BIS-Praxis regelmäßig unter **ECCN 3A991** (weniger sensibel, ATF-Liste), sofern er die Performance-Schwellen von 3A001.a nicht überschreitet. Die De-minimis-Regel (15 CFR § 734.4) könnte bei weniger als 25 % US-Wertanteil am Endprodukt eingreifen; der Wertanteil ist zu ermitteln.

**Handlungsempfehlung:** US-amerikanischen Hersteller des Chips (voraussichtlich: Broadcom-Lizenzpartner) anfragen, ob ein ECCN-Klassifizierungsschreiben vorliegt.

### 4.6 Ergebnis Klassifizierung

| Aspekt | Ergebnis |
|---|---|
| EU-Dual-Use-Listenpflicht | **Ja, 2B001.b.1** (CNC-Steuerung, >5 Achsen, hohe Genauigkeit) |
| Kryptographie (5A002) | Wahrscheinlich freigestellt (Cryptography Note) |
| US-EAR-Berührung | Prüfung De-minimis-Regel erforderlich |
| Endprodukt-HS-Code | **8537.10** (Schalttafeln und -schränke, ≤ 1000 V) – bestätigt |
| KN-Unterposition | 8537 10 99 (sonstige, ≤ 1000 V) |
| TARIC | 8537 10 99 10 (soweit anwendbar, DE-Praxis) |

---

## 5. Identifikation besonderer Exportkontrollrisiken

1. **Mehrachsigkeit:** Die 9-Achsen-Interpolation überschreitet die Listenschwelle – eine Genehmigungspflicht für Exporte in Drittstaaten (insbesondere in Länder des Anhangs II der EU-Dual-Use-VO) ist wahrscheinlich.
2. **US-Prozessorkern:** Re-Export-Beschränkungen nach EAR könnten unabhängig vom deutschen/EU-Recht gelten (Extraterritorialitätsprinzip). Exporte aus der EU in sanktionierte Länder (Russland, Weißrussland, Iran) sind nach Art. 12g VO (EU) 833/2014 verboten; der Hersteller haftet für Umgehungshandlungen Dritter.
3. **Cloud-OTA:** Das Cloud-Update-Feature macht das Modul zu einem vernetzten System; Sicherheitsüberprüfungen können nach Cyber-Security-Gesichtspunkten zusätzlich relevant werden (NIS2).
4. **Endverwendungsrisiko:** Angegebene Endverwendung (zivile Maschinenwartung) deckt sich nicht mit der Weiterleitungsstruktur (TR → KZ); Catch-All-Prüfung nach Art. 4 EU 2021/821 ist obligatorisch.

---

## 6. Empfohlene nächste Schritte

- [ ] Vollständige Güterlistenprüfung nach 2B001 mit BAFA-Verbindlichkeitsbescheid
- [ ] ECCN-Bestätigung beim US-Komponentenlieferanten einholen
- [ ] De-minimis-Berechnung (US-Wertanteil)
- [ ] Endverwendungserklärung (EUC) des türkischen Händlers für jede Sendung
- [ ] Weiterverkaufsverbot in die Russische Föderation, Weißrussland und Iran vertraglich sicherstellen
- [ ] Catch-All-Prüfung für die konkrete Kasachstan-Transaktion dokumentieren

---

*Erstellt von: Dipl.-Ing. Rainer Hofstädter | Exportkontrollbeauftragter | Globalmaschinen GmbH | Version 1.0 | 14.04.2026*
