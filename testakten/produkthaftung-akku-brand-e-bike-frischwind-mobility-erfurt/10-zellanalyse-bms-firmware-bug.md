# 10 — Zellanalyse und BMS-Firmware-Bug V3.9.1 — Sachverständigengutachten

**Dokument-Typ:** Zusammenfassung Sachverständigengutachten
**AZ Kanzlei:** MR-2026-0822
**Sachverständiger:** Prof. Dr.-Ing. Hartmut Schellberg, Institut für Elektrochemische Energiespeicher, TU Braunschweig
**Gutachten-Nr.:** TUB-ESS-2026-0034
**Datum Gutachten:** 14. Februar 2026

---

## 1. Auftrag

Frischwind Mobility GmbH beauftragte Prof. Dr.-Ing. Schellberg mit der Analyse von:
1. Zellchemie der CT-LI-45-X-Akkus (Ist vs. Soll laut Datenblatt)
2. BMS-Firmware-Verhalten Version 3.9.1 unter Grenztemperaturbedingungen
3. Kausalzusammenhang zwischen BMS-Bug und den drei dokumentierten Brandvorfällen

---

## 2. Zellanalyse

**Methodik:** REM-EDX-Analyse (Rasterelektronenmikroskopie + energiedispersive Röntgenspektroskopie) an Zellen aus zwei unbeschadigten Akkus (Charge 2023-CH-441 und 2024-CH-088); ICP-OES (Massenspektrometrie) zur Elementanalyse Kathodenmaterial.

**Ergebnis:**
- Datenblatt ChinaTech: LiFePO4 (Lithiumeisenphosphat) — Kathodenformel LiFePO4
- Tatsächliche Zusammensetzung (EDX): NMC (Nickel-Mangan-Kobalt-Oxid) — Kathodenformel LiNi0.6Mn0.2Co0.2O2 (NMC-622)
- Abweichung: **Signifikant** — NMC-622 weist einen deutlich niedrigeren Onset-Punkt für thermisches Durchgehen auf (ca. 150 °C vs. LiFePO4 > 270 °C)

**Schlussfolgerung Sachverständiger:** „ChinaTech ShenZhen hat in den Serienakkus eine andere Zellchemie verbaut als im Datenblatt angegeben. Dies stellt eine wesentliche und sicherheitsrelevante Abweichung von der vertraglichen Spezifikation dar."

---

## 3. BMS-Firmware-Analyse

**Methodik:** Firmware-Reverse-Engineering der Version 3.9.1 (Binär-Dump aus zwei Serienakkus); Vergleich mit dem Quellcode-Auszug, den CTO Dr. Pohlmann-Wittfeldt bereitgestellt hat; Simulation unter Temperaturbedingungen 35–45 °C.

**Identifizierter Bug:**

```
// Temperatur-Interrupt-Handler (BMS V3.9.1)
void TEMP_IRQ_Handler(void) {
    if (temp_sensor_raw > TEMP_THRESHOLD_HIGH) {
        charge_enable = 0;   // Ladung stoppen
        overheat_flag = 1;
    }
    // BUG: TEMP_THRESHOLD_HIGH wird bei hoher Umgebungstemperatur
    // durch Integer-Overflow in temp_compensation_factor falsch berechnet.
    // Ergebnis: Bei Umgebung > 38°C wird TEMP_THRESHOLD_HIGH zu 0xFF überlaufen
    // und der Handler niemals ausgelöst.
}
```

**Wirkung:** Bei Umgebungstemperatur > 38 °C und Ladestrom > 3 A wird der Temperatur-Interrupt-Handler aufgrund eines Integer-Overflows im Kompensationsfaktor niemals ausgelöst. Die Zellen werden nicht abgeschaltet und laden weiter bis 4,35 V/Zelle — 7,1 % über dem Sicherheitsgrenzwert.

---

## 4. Kausalzusammenhang

**Vorfall 1 (Köpenick):** Außentemperatur 39 °C, Schnellladung 3,5 A → BMS-Handler inaktiv → Überladung bis 4,35 V → thermisches Durchgehen. **Kausal: Ja (sehr hohe Wahrscheinlichkeit).**

**Vorfall 2 (Leipzig):** Außentemperatur 41 °C, Ladung abgeschlossen, Fahrt in voller Sonne → Zelltemperatur akkumuliert → thermisches Durchgehen. **Kausal: Ja (hohe Wahrscheinlichkeit).**

**Vorfall 3 (Stuttgart):** Kellertemperatur 36 °C (Heizungsnähe), Ladung über Nacht → Grenzfall, Temperatur knapp über 38 °C-Schwelle. **Kausal: Wahrscheinlich.**

---

## 5. Verantwortlichkeit ChinaTech vs. Frischwind

| Ebene | ChinaTech | Frischwind |
|---|---|---|
| Falsche Zellchemie im Datenblatt | Primär verantwortlich | Hätte durch Eingangsqualitätsprüfung entdeckt werden können |
| BMS-Firmware-Bug | Primär verantwortlich (Firmware-Hersteller) | Hätte in Eingangsvalidierung der Firmware geprüft werden müssen |
| Unterlassene RAPEX-Meldung | Keine Pflicht | Primär verantwortlich — ProdSG-Verstoß |
| Unterlassener Rückruf nach Vorfall 1 | Keine Pflicht | Primär verantwortlich — § 26 ProdSG |
