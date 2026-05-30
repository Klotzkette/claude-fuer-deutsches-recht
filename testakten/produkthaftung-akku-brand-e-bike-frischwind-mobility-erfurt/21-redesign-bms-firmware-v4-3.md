# 21 — Technisches Redesign BMS-Firmware V4.3 — Freigabe-Roadmap

**Dokument-Typ:** Technisches Strategiepapier
**AZ Kanzlei:** MR-2026-0822
**Technische Verantwortung:** CTO Dr. Ilse Pohlmann-Wittfeldt / externer Berater: Dipl.-Ing. Klaus Nähring, FH Erfurt

---

## 1. Zielsetzung des Redesigns

Das technische Redesign des BMS-Systems verfolgt drei Ziele:
1. Behebung des kritischen Firmware-Bugs (Integer-Overflow im Temperatur-Interrupt-Handler)
2. Anpassung des BMS an die tatsächlich verwendeten NMC-622-Zellen (statt LiFePO4)
3. Vorbereitung einer erneuten CE-Konformitätsbewertung für den Neumarktstart mit Wind-X8

---

## 2. Firmware V4.3 — Technische Änderungen

### 2.1 Bug-Fix Temperatur-Interrupt-Handler

```c
// Firmware V4.3 — Korrigierter Temperatur-Interrupt-Handler
void TEMP_IRQ_Handler(void) {
    // Explizite Typcastung vermeidet Integer-Overflow
    uint32_t temp_raw = (uint32_t)temp_sensor_raw;
    uint32_t threshold = (uint32_t)TEMP_THRESHOLD_BASE 
                       + (uint32_t)temp_compensation_factor;
    
    // Overflow-Schutz: threshold niemals > TEMP_THRESHOLD_MAX
    if (threshold > TEMP_THRESHOLD_MAX) {
        threshold = TEMP_THRESHOLD_MAX;
    }
    
    if (temp_raw > threshold) {
        charge_enable = 0;
        overheat_flag = 1;
        trigger_emergency_shutdown();
    }
}
```

### 2.2 NMC-622-Anpassungen

- Maximale Ladespannung: von 4,20 V/Zelle auf 4,15 V/Zelle reduziert (Sicherheitspuffer für NMC-622)
- Thermischer Abschaltpunkt: von 68 °C auf 55 °C Zelltemperatur gesenkt (NMC-622-spezifisch)
- Temperaturkompensation: Neue Kennlinie für NMC-622-Wärmekoeffizienten hinterlegt

### 2.3 Zusätzliche Sicherheitsfunktionen

- Watchdog-Timer: Unabhängiger Hardware-Watchdog überwacht BMS-Hauptschleife (neu)
- Redundante Temperatursensoren: Zwei statt einem Sensor; bei Sensorausfall → Abschaltung (neu)
- Ladestrom-Begrenzung bei Umgebungstemperatur > 30 °C: automatisch auf 2 A reduziert (neu)
- Over-the-Air-Firmware-Update: Ermöglicht zukünftige Bug-Fixes ohne physischen Serviceeinsatz (neu)

---

## 3. Freigabe-Roadmap

| Meilenstein | Datum | Status |
|---|---|---|
| Firmware V4.3 Entwicklungsabschluss | 28. Februar 2026 | Abgeschlossen |
| Interne Unit-Tests (MISRA C) | 10. März 2026 | Abgeschlossen |
| Externe Firmware-Verifikation (TÜV Rheinland) | 31. März 2026 | In Arbeit |
| Zellanalyse und Charakterisierung NMC-622 (Prof. Schellberg) | 15. April 2026 | Geplant |
| Baumusterprüfung Wind-X8 (neue Konformitätsbewertung, NB 0035) | 30. Juni 2026 | Geplant |
| CE-Konformitätserklärung Wind-X8 | 15. Juli 2026 | Geplant |
| Produktionsbeginn Wind-X8 | August 2026 | Geplant |
| Markteinführung Wind-X8 | Oktober 2026 | Geplant |

---

## 4. Rechtliche Voraussetzungen für Marktreintritt

- Vollständige neue Baumusterprüfung durch TÜV Rheinland (NB 0035).
- Neue Konformitätserklärung auf Basis NMC-622-Zellen und Firmware V4.3.
- BNetzA-Information über neues Produkt und Abgrenzung zum Rückruf-Produkt.
- Neue Betriebsanleitung mit expliziten Temperaturwarnungen und Ladehinweisen.
- Liefervertrag mit ChinaTech: ausdrückliche Vereinbarung der Zellchemie NMC-622 (Änderungsvertrag).
