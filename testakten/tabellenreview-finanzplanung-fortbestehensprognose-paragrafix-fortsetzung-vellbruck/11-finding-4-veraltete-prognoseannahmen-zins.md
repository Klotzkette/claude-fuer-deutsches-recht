# 11 — Finding 4: Veraltete Prognoseannahmen Zinsen

**Aktenzeichen:** TR-WF-2026-PFX-0712
**Finding-ID:** F-04
**Schwere:** Kritisch (Manipulationsverdacht)
**Entdeckt:** 12. Januar 2026

---

## Sachverhalt

Zwischen den Modellversionen v22 und v23 wurde der Zinssatz für den Kontokorrentkredit in Zelle `ZINS-SCHULDEN!C5` von 6,2 % auf 4,9 % p.a. reduziert. Diese Änderung erfolgte:
- Durch direktes Überschreiben der Formel `=PARAM!B12` mit dem Hardcoded-Wert `0,049`.
- Ohne Anpassung des zentralen Parameterwertes in `PARAM!B12` (bleibt bei 6,2 %).
- Ohne Dokumentation im internen Änderungsprotokoll des Modells.
- Ohne Quellenbeleg für den neuen Zinssatz.

---

## Marktlage Zinsen Januar 2026

| Referenz | Wert (Jan 2026) |
|---|---|
| EZB Hauptrefinanzierungssatz | 3,15 % |
| 3M-Euribor | 2,88 % |
| Marktüblicher KK-Zins, Investment Grade | 4,5–5,5 % |
| Marktüblicher KK-Zins, erhöhtes Kreditrisiko | 6,0–7,5 % |

Paragrafix GmbH weist eine deutlich erhöhte Kreditrisikoeinschätzung auf (Umsatzrückgang –17,6 % 2025, ausgeschöpfte Kreditlinie). Ein Zinssatz von 4,9 % entspricht einer Investment-Grade-Bewertung, die für Paragrafix nicht zutreffend ist.

---

## Auswirkung der Zinssatz-Absenkung

| Szenario | Zinssatz | Zinsaufwand 2026 (TEUR) | Zinsaufwand 2027 (TEUR) | Delta kumuliert |
|---|---|---|---|---|
| v23 (Modell) | 4,9 % | 122 | 64 | — |
| v22-Niveau | 6,2 % | 154 | 81 | +49 TEUR |
| Marktkonform (7,0 %) | 7,0 % | 175 | 92 | +81 TEUR |
| Marktkonform (7,5 %) | 7,5 % | 187 | 98 | +99 TEUR |

---

## Rechtliche Einordnung

Die nicht dokumentierte, parameterentkoppelte Absenkung einer wesentlichen Annahme, die das Prognose-Gesamtergebnis maßgeblich beeinflusst, begründet den Verdacht einer bewussten Ergebnismanipulation:

- **§ 283b StGB** (Verletzung der Buchführungspflicht durch ungenaue Darstellung): Der geschäftsführende GF haftet persönlich, wenn er ein Modell zur Grundlage von Geschäftsentscheidungen macht, das er kennt oder kennen musste als fehlerhaft.
- **§ 15a InsO** (Insolvenzantragspflicht): Wenn nach Korrektur des Zinssatzes das Modell in den negativen Bereich kippt, könnte die Antragspflicht des GF ausgelöst sein.
- **AktG § 91** (analog über GmbH-Recht): Pflicht zur ordnungsgemäßen Risikofrüherkennnung.

**Quellen:** StGB § 283b: [https://dejure.org/gesetze/StGB/283b.html](https://dejure.org/gesetze/StGB/283b.html); InsO § 15a: [https://dejure.org/gesetze/InsO/15a.html](https://dejure.org/gesetze/InsO/15a.html); AktG § 91: [https://dejure.org/gesetze/AktG/91.html](https://dejure.org/gesetze/AktG/91.html).

---

## Empfehlung

Sofortige Korrektur auf marktkonformen Zinssatz (Reviewer-Empfehlung: 6,5 % als konservative Mitte). Dokumentation der Quellengrundlage (Bankschreiben oder Marktzinsreferenz). Strafrechtliche Beratung durch externen Strafrechtsexperten für GF Dr. Vellbruck-Steinheim unverzüglich einholen.
