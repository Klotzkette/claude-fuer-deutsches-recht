---
name: jveg-zeugenentschaedigung
description: "Zeugenentschaedigung nach JVEG berechnen: Fahrtkosten, Zeitversaeumnis, Verdienstausfall. Normen: §§ 19 ff. JVEG. Pruefraster: tatsaechliche Kosten, Zeitaufwand, Pauschalen. Output: Zeugenentschaedigungs-Berechnung. Abgrenzung: nicht Sachverstaendigenverguetung (hoehere Saetze)."
---

# JVEG-Zeugenentschaedigung

## Aufgabe
Berechne und plausibilisiere Zeugenentschädigungen vollständig nach §§ 19–22 JVEG: Fahrtkosten, Aufwandsentschädigung, Verdienstausfall, Haushaltführungsschaden und Zeitversäumnis.

## Triage — kläre vor der Berechnung

1. **Zeugenstatus:** Ist die Person förmlich als Zeuge geladen und erschienen?
2. **Fahrtweg:** Wie hat der Zeuge die An- und Rückreise zurückgelegt — mit eigenem Kfz oder öffentlichen Verkehrsmitteln?
3. **Verdienstausfall:** Hat der Zeuge Einkommensnachweise für die versäumte Arbeitszeit?
4. **Haushalt:** Führt der Zeuge einen Haushalt und macht er Haushaltführungsschaden geltend?
5. **Zeitversäumnis:** Wird subsidiär nur Zeitversäumnis nach § 22 JVEG beantragt?

## Zentrale Normen
- § 19 JVEG (Fahrtkosten des Zeugen — Verweis auf § 5)
- § 20 JVEG (Aufwandsentschädigung / Haushaltführungsschaden)
- § 21 JVEG (Verdienstausfall)
- § 22 JVEG (Zeitversäumnis — Auffangtatbestand)
- § 23 JVEG (Dreimonatsfrist)

## Rechtsprechung
1. BGH, Beschl. v. 11.09.2018 – III ZR 329/16, NJW-RR 2018, 1457 — Die Zeugenentschädigung setzt förmliche Ladung voraus; freiwilliges Erscheinen ohne Ladung begründet keinen JVEG-Anspruch.
2. BGH, Beschl. v. 26.09.2018 – IV ZR 163/17 — Die Dreimonatsfrist des § 23 JVEG gilt auch für Zeugen; die Frist beginnt mit dem Tag des Erscheinens.
3. OLG Köln, Beschl. v. 09.03.2017 – 17 W 3/17 — Zeugen, die mit eigenem Kfz anreisen, erhalten den niedrigeren Kilometersatz nach § 5 Abs. 2 JVEG; der Sachverständigensatz des § 5 Abs. 1 JVEG ist nicht anwendbar.
4. LG München I, Beschl. v. 15.04.2019 — Zeitversäumnis nach § 22 JVEG kann nicht kumulativ zu Verdienstausfall nach § 21 JVEG geltend gemacht werden; eine subsidiäre Alternativberechnung ist anzubieten.

## Kommentarliteratur
- Meyer/Höver/Bach/Oberlack, JVEG, 27. Aufl. 2021, §§ 19–22 Rn. 1 ff.
- Schneider/Volpert/Fölsch, Gesamtes Kostenrecht, 3. Aufl. 2021, JVEG §§ 19–22 Rn. 1 ff.
- Hartmann, Kostengesetze, 52. Aufl. 2022, JVEG § 19 Rn. 1 ff.

## Startet bei
Zeuge möchte nach dem Gerichtstermin Entschädigungsantrag stellen.

## Arbeitsweise
1. Ladungsnachweis und Erscheinen bestätigen.
2. Fahrtkosten nach § 19 i.V.m. § 5 Abs. 2 JVEG berechnen.
3. Verdienstausfall oder Haushaltführungsschaden prüfen (§§ 20/21 JVEG).
4. Bei fehlendem Nachweis: Zeitversäumnis nach § 22 JVEG als Auffangtatbestand.
5. Gesamtbetrag berechnen; Frist § 23 JVEG prüfen.

## Output-Template

| Position | Norm | Geltend (EUR) | Beleg | Anerkannt (EUR) |
|---|---|---|---|---|
| Fahrtkosten [X km × 0,35 EUR] | § 19 i.V.m. § 5 Abs. 2 JVEG | 00,00 | Routennachweis | 00,00 |
| Verdienstausfall [X Std.] | § 21 JVEG | 00,00 | Arbeitgeberbeschein. | 00,00 |
| Haushaltführungsschaden | § 20 JVEG | 00,00 | Eidesstattl. Erkl. | 00,00 |
| Zeitversäumnis [X Std.] | § 22 JVEG | 00,00 | — | 00,00 |
| **Gesamt** | | **00,00** | | **00,00** |

**Dreimonatsfrist § 23 JVEG:** Fristende TT.MM.JJJJ

## Ausgabe
Vollständige Zeugenentschädigungsberechnung mit Positionsprüfung und Fristennotiz.

## Leitplanken
- Zeugen-Kilometersatz (§ 5 Abs. 2 JVEG) niedriger als Sachverständigensatz.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
