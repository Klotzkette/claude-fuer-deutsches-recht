# 02 — Produktbeschreibung E-Bike Wind-X7

**Dokument-Typ:** Technische Produktbeschreibung (kanzleiinterne Arbeitsunterlage)
**AZ Kanzlei:** MR-2026-0822
**Erstellungsdatum:** 22. Januar 2026

---

## 1. Produktidentifikation

| Merkmal | Wert |
|---|---|
| Produktname | Frischwind Wind-X7 |
| Produktkategorie | Pedelec (EPAC) nach EN 15194:2017 |
| EAN | 4 012 345 678 901 |
| Modellnummer | FW-WX7-2023-EU |
| Erstinverkehrbringen | 15. März 2023 |
| Produktionsstandort | Erfurt (Rahmen/Montage); ShenZhen, China (Akku-Zellen) |
| Marktregionen | Deutschland, Österreich, Schweiz, Niederlande, Belgien |
| Umsatzvolumen (kumuliert bis Jan. 2026) | ca. 4.200 Einheiten |

---

## 2. Technische Spezifikation

### 2.1 Rahmen und Antrieb

- **Rahmen:** Aluminium 6061-T6, Größen S / M / L / XL
- **Motor:** Brose Drive S (250 W Nennleistung, max. 25 km/h Unterstützung)
- **Gewicht:** 23,4 kg (Größe M, ohne Akku: 17,8 kg)
- **Zugelassene Traglast:** 120 kg (Fahrer + Gepäck)

### 2.2 Akku-System (kritisch)

| Parameter | Wert |
|---|---|
| Akkumodell | CT-LI-45-X |
| Hersteller | ChinaTech ShenZhen Co. Ltd. |
| Zellchemie | Lithium-Eisenphosphat (LiFePO4) — lt. Datenblatt; tatsächlich NMC (Li-NiMnCoO2) lt. Zellanalyse |
| Nennspannung | 45 V |
| Kapazität | 17,5 Ah (787,5 Wh) |
| Ladezeit (0–100 %) | ca. 5,5 Stunden |
| BMS-Firmware | Version 3.9.1 (fehlerbehaftet); aktuell in Entwicklung: V4.3 |
| Schutzklasse | IP65 |
| Betriebstemperatur | -10 °C bis +40 °C (lt. Datenblatt) |

**Kritischer Befund:** Entgegen dem Datenblatt von ChinaTech sind die Zellen nicht LiFePO4 (Lithiumeisenphosphat, niedrigeres thermisches Risiko), sondern NMC (Nickel-Mangan-Kobalt-Oxid, höheres thermisches Risiko). Dieser Widerspruch wurde bei der Eingangsqualitätskontrolle Frischwind nicht festgestellt.

### 2.3 BMS (Battery Management System)

Das BMS CT-BMS-3.9 kontrolliert Lade-/Entladezyklen, Temperaturmanagement und Überladeschutz. In Firmware-Version 3.9.1 besteht ein kritischer Bug im Temperatur-Interrupts-Handler:

Bei Umgebungstemperaturen > 38 °C und gleichzeitiger Schnellladung (> 3 A) wird der Überladeschutz nicht korrekt aktiviert. Die Zellen werden bis zu 4,35 V/Zelle überladen (Sollwert: 4,20 V/Zelle), was bei NMC-Zellen zum thermischen Durchgehen führen kann (Exotherme Reaktion, selbstverstärkend).

---

## 3. CE-Kennzeichnung

| Anforderung | Details |
|---|---|
| CE-Richtlinien | 2006/42/EG (Maschinenrichtlinie), 2014/30/EU (EMV), 2014/35/EU (Niederspannung) |
| Harmonisierte Norm | EN 15194:2017 (EPAC Pedelec) |
| Konformitätserklärung | Ausgestellt 10.02.2023, Frischwind Mobility GmbH |
| Benannte Stelle (Baumusterprüfung) | TÜV Rheinland, Köln, NB 0035 |
| Baumusterprüfbescheinigung | TR-2022-LF-4412 (gültig bis 09.02.2028) |

**Kritisch:** Die Baumusterprüfung erfolgte mit Prototyp-Akkus, die tatsächlich LiFePO4-Zellen enthielten. Die Serienproduktion mit NMC-Zellen wurde nicht nachgemeldet — mögliche Verletzung der Konformitätspflicht.

---

## 4. Lieferkette und Verträge

- **Rahmenliefervertrag ChinaTech ShenZhen Co. Ltd.:** Laufzeit 2022–2027; Garantie: 24 Monate; Haftungsbeschränkung auf Warenwert; keine Produkthaftungsfreistellung.
- **Montagepartner:** Eigenmontage Erfurt (Qualitätssicherungsprotokoll QS-FW-2022-003).
- **Logistik:** Direktlieferung ab Werk ChinaTech → Seefracht → Hamburg → Erfurt.
