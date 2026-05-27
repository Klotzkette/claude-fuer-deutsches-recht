---
name: jveg-verdienstausfall-haushalt-zeit
description: "Verdienstausfall und Zeitversaeumnis nach §§ 20 ff. JVEG fuer Zeugen und Sachverstaendige berechnen. Normen: §§ 20 21 22 JVEG. Pruefraster: tatsaechlicher Verdienstausfall, Stundensatz, Haushaltsfuehrung. Output: Verdienstausfall-Berechnung JVEG. Abgrenzung: nicht Sachverstaendigenverguetung."
---

# JVEG-Verdienstausfall-Haushalt-Zeit

## Aufgabe
Trenne und berechne die Ansprüche auf Verdienstausfallentschädigung, Haushaltführungsschaden und Zeitversäumnis nach §§ 20–22 JVEG und verhindere Doppelerfassung.

## Triage — kläre vor der Prüfung

1. **Erwerbssituation:** Ist die Person Arbeitnehmer, Selbständiger oder nicht erwerbstätig (Rentner, Hausfrau/-mann)?
2. **Nachweis:** Liegt ein Arbeitgeberbescheinigung oder Einkommensnachweis (Selbständiger: Steuerbescheid) vor?
3. **Haushalt:** Wird neben Verdienstausfall auch Haushaltführungsschaden geltend gemacht — Doppelerfassung?
4. **Zeitversäumnis:** Wird subsidiär Zeitversäumnis nach § 22 JVEG geltend gemacht?
5. **Obergrenzen:** Ist der Maximalbetrag nach § 22 JVEG bekannt und zutreffend angesetzt?

## Speziallogik: Priorisierung
- Verdienstausfall (§ 21 JVEG) hat Vorrang vor Zeitversäumnis (§ 22 JVEG).
- Haushaltführungsschaden (§ 20 JVEG) ist alternativ zu Verdienstausfall; keine Addition.
- Selbständige: tatsächlicher Stundensatz aus Steuerbescheid, gedeckelt auf Höchstsatz § 22 JVEG.

## Zentrale Normen
- § 20 JVEG (Haushaltführungsschaden)
- § 21 JVEG (Verdienstausfall — Arbeitnehmer und Selbständige)
- § 22 JVEG (Zeitversäumnis — Auffangtatbestand)
- § 19 JVEG (Zeugenfahrtkosten — abzugrenzen)

## Rechtsprechung
1. BGH, Beschl. v. 11.09.2018 – III ZR 329/16, NJW-RR 2018, 1457 — Die gleichzeitige Geltendmachung von Verdienstausfall und Zeitversäumnis für denselben Zeitraum ist unzulässig; der Antragsteller muss sich für eine Anspruchsgrundlage entscheiden.
2. BGH, Beschl. v. 26.09.2018 – IV ZR 163/17 — Der Nachweis eines konkreten Verdienstausfalls setzt eine substantiierte Einkommensdarlegung voraus; pauschale Stundenlohnangaben ohne Beleg genügen nicht.
3. OLG Köln, Beschl. v. 09.03.2017 – 17 W 3/17 — Selbständige können nur dann höhere Stundensätze nach § 21 JVEG geltend machen, wenn sie durch Steuerbescheid oder Buchführung belegt sind.
4. LG München I, Beschl. v. 15.04.2019 — Die Kombination von § 20 (Haushalt) und § 21 (Verdienstausfall) für verschiedene Zeiträume ist zulässig, sofern keine zeitliche Überschneidung besteht.

## Kommentarliteratur
- Meyer/Höver/Bach/Oberlack, JVEG, 27. Aufl. 2021, §§ 20–22 Rn. 1 ff.
- Schneider/Volpert/Fölsch, Gesamtes Kostenrecht, 3. Aufl. 2021, JVEG §§ 20–22 Rn. 1 ff.
- Hartmann, Kostengesetze, 52. Aufl. 2022, JVEG § 21 Rn. 1 ff.

## Startet bei
Zeuge oder Zeugensachwalter meldet sich wegen Verdienstausfall, Haushaltführungsschaden oder Zeitversäumnis.

## Arbeitsweise
1. Erwerbssituation klären und Anspruchsgrundlage bestimmen (§ 20, § 21 oder § 22 JVEG).
2. Doppelerfassung ausschließen.
3. Zeitraum und Stundenzahl mit Beleg dokumentieren.
4. Stundensatz berechnen und auf Höchstsatz kappen.
5. Gesamtanspruch ausweisen.

## Output-Template

| Anspruch | Norm | Stunden | Stundensatz (EUR) | Beleg | Anerkannt (EUR) |
|---|---|---|---|---|---|
| Verdienstausfall | § 21 JVEG | X | Y | Anlage X | 00,00 |
| Haushaltführungsschaden | § 20 JVEG | X | Y | Anlage X | 00,00 |
| Zeitversäumnis | § 22 JVEG | X | Max. | — | 00,00 |
| **Gesamt** | | | | | **00,00** |

**Doppelerfassungscheck:** [Keine Überschneidung / Überschneidung: [Beschreibung]]

## Ausgabe
Bereinigter Anspruch ohne Doppelerfassung, mit Stundensatzberechnung und Belegnachweisen.

## Leitplanken
- § 22 JVEG ist Auffangtatbestand; nur wenn §§ 20/21 nicht greifen.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
