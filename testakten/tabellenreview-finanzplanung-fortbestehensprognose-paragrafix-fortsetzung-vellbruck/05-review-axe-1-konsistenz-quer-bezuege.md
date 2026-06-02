# 05 — Review-Achse 1: Konsistenz / Querbezüge

**Aktenzeichen:** TR-WF-2026-PFX-0712
**Datum:** 10./11. Januar 2026
**Prüfer:** Karsten Federkamp (unter Aufsicht Dr. Wittfeldt-Steinheim)

---

## Prüfgegenstand

Die Konsistenzprüfung untersucht, ob alle blattübergreifenden Verknüpfungen korrekt, vollständig und nachvollziehbar sind. Insbesondere:

- Stimmen Zellbezüge zwischen Eingangsblättern und Rechenblättern?
- Sind alle Aggregationen (Summen, Verweise) korrekt?
- Werden Korrekturen in PARAM automatisch in alle nachgelagerten Blätter übertragen?
- Gibt es Blattbrüche (Blätter mit veralteten, manuell überschriebenen Werten)?

---

## Methodik

Der Reviewer hat folgende Konsistenzprüfmethodik angewendet:

1. **Formel-Audit-Tool:** Excel-interne Formelüberwachung (Spurpfeile, Formelprüfung) systematisch für alle Rechenblätter durchgeführt.
2. **Benchmark-Check:** Saldenbilanz-Abstimmung: IST-GuV-Summen gegen IST-Bilanz-Eigenkapitalveränderung (Eigenkapitalspiegel).
3. **Kreuztabelle Blattübergänge:** Alle 84 Named Ranges auf korrekte Adressierung geprüft.
4. **Konsistenz PARAM → Nachgelagerte Blätter:** 23 Parameter aus PARAM einzeln verändert und Auswirkung in allen 18 Blättern nachverfolgt.

---

## Ergebnisse der Konsistenzprüfung

### Befunde ohne Finding-Status (korrekt)

| Prüfpunkt | Befund |
|---|---|
| IST-GuV → PLAN-GuV Basisjahr-Übernahme | Korrekt verknüpft |
| PERSONAL → PLAN-GuV Personalaufwand | Korrekt, Named Range "PersonalAufwand2026" stimmt |
| INVESTITIONEN → PLAN-BILANZ Sachanlagen | Korrekt; AfA-Plan konsistent |
| LIQUIDITÄT → ZUSAMMENFASSUNG Liquiditätskennzahlen | Korrekt |
| PARAM Wachstumsraten → PLAN-GuV | Korrekt übernommen (PARAM!B5–B8) |

### Befunde mit Finding-Status

| Finding-Nr. | Betroffene Blätter | Zellen | Kurzbeschreibung |
|---|---|---|---|
| F-01 | PLAN-CF ↔ ZINS-SCHULDEN | CF!E14, ZS!D9 | Zirkulärer Bezug |
| F-02 | PLAN-GuV, PLAN-BILANZ | div. | 47 Hardcoded-Werte |
| F-03 | PLAN-BILANZ | PB!B44 | Falsche SUM-Formel Bilanzsumme |
| F-04 | ZINS-SCHULDEN | ZS!C5 | Formel durch Hardcoded ersetzt |

### Blattbrüche (inkonsistente manuelle Überschreibungen)

Folgende Blätter weisen Zellen auf, in denen Formelbezüge zu PARAM durch Hardcoded-Werte ersetzt wurden, ohne dass dies im Änderungsprotokoll dokumentiert ist:

- `ZINS-SCHULDEN!C5` (Zinssatz, siehe Finding 4)
- `PLAN-GuV!F22` (Umsatzwachstum Q3 2026: statt =PARAM!B5 wurde 0,072 eingetragen)
- `PLAN-CF!H8` (Forderungslaufzeit: statt =PARAM!B19 wurde 42 eingetragen)

---

## Gesamtbewertung Konsistenz

Die Grundarchitektur des Modells ist konsistent aufgebaut. Die identifizierten Blattbrüche und der zirkuläre Bezug (Finding 1) sind jedoch schwerwiegende Mängel, die die Belastbarkeit des Modells als Grundlage für eine IDW-S-11-konforme Fortbestehensprognose infrage stellen.

**Quellen:** IDW S 11 Tz. 22–31 (Modellkonsistenz und Parametersteuerung), [https://www.idw.de](https://www.idw.de); HGB § 252: [https://dejure.org/gesetze/HGB/252.html](https://dejure.org/gesetze/HGB/252.html).
