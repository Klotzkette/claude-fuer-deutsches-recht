# 12 — Finding 5: Doppelte Buchungen Rückstellung Pensionen

**Aktenzeichen:** TR-WF-2026-PFX-0712
**Finding-ID:** F-05
**Schwere:** Mittel–Hoch
**Entdeckt:** 12. Januar 2026

---

## Sachverhalt

Im Blatt `PLAN-BILANZ` und korrespondierend in `PLAN-GuV` wurden Pensionsrückstellungen für das Jahr 2026 doppelt erfasst:

- `PLAN-BILANZ!D55`: Pensionsrückstellung 2026 = 480 TEUR
- `PLAN-BILANZ!D56`: Pensionsverpflichtungen (langfristig) 2026 = 480 TEUR
- `PLAN-GuV!D38`: Zuführung Pensionsrückstellung 2026 = 480 TEUR (einmalig)

Beim Abgleich mit der IST-Bilanz 2025 (Pensionsrückstellungen 2025: 460 TEUR, erwartet: ca. +15–20 TEUR Zuführung 2026) wird deutlich, dass sowohl eine kurzfristige als auch eine langfristige Position denselben Betrag ausweisen, obwohl es sich um dieselbe Rückstellung handelt. Die Zuführung in der GuV (480 TEUR) entspricht zudem nicht dem planmäßigen Anstieg, sondern der Gesamtposition.

---

## Auswirkung

| Position | Modell v23 (TEUR) | Korrekt (TEUR) | Fehler (TEUR) |
|---|---|---|---|
| Pensionsrückstellung Bilanz Passiva | 960 | 480 | +480 |
| Personalaufwand / Zuführung GuV | 480 | 19 | +461 |
| Bilanzsumme Passiva | Überhöht um 480 | — | — |
| EBITDA 2026 | Um 461 TEUR zu niedrig | — | — |

Paradoxerweise bewirkt dieser Fehler, dass die GuV das EBITDA 2026 zu niedrig ausweist (konservativ), während die Bilanz überhöhte Passiva zeigt. Das Nettoliquiditätsergebnis ist von diesem Fehler kaum betroffen, da die Zuführung nicht zahlungswirksam ist — jedoch verzerrte Bilanzdarstellung ist aus HGB-Sicht unzulässig.

---

## Empfehlung

Korrektur der Bilanzposition auf einfache Erfassung Pensionsrückstellung (ca. 479 TEUR = 460 TEUR + 19 TEUR planmäßige Zuführung). Abstimmung mit Jahresabschlussprüfer Birkholz & Partner über aktuarielle Bestätigung.

**Verantwortlich:** CFO Pellbach-Roosendaal.
**Frist:** 3 Arbeitstage.

**Quellen:** HGB § 249 (Rückstellungen): [https://dejure.org/gesetze/HGB/249.html](https://dejure.org/gesetze/HGB/249.html); IDW S 11 Tz. 29 (Bilanzpositionen in Fortbestehensprognose), [https://www.idw.de](https://www.idw.de).
