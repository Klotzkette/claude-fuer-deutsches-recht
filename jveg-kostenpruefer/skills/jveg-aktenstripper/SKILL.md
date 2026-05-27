---
name: jveg-aktenstripper
description: "JVEG-relevante Daten aus Gerichtsakten und Gutachterunterlagen extrahieren: Termine, Stunden, Auslagen. Normen: §§ 2 ff. JVEG. Pruefraster: Terminsprotokoll, Stundennachweis, Belegstruktur. Output: Extrahierter Datensatz fuer Kostenpruefung. Abgrenzung: nicht Kostenberechnung."
---

# JVEG-Aktenstripper

## Aufgabe
Extrahiere alle vergütungsrelevanten Daten aus Gerichtsschreiben, Anträgen, Rechnungen und Belegen und überführe sie in eine strukturierte, prüfbare JVEG-Datenmatrix.

## Triage — kläre vor dem Ausstreifen

1. **Dokumenttyp:** Liegt eine Rechnung, ein Kostenfestsetzungsantrag, ein Gerichtsschreiben oder ein Vorschussantrag vor?
2. **Anspruchsberechtigter:** Sachverständiger, Zeuge, Dolmetscher, Übersetzer oder ehrenamtlicher Richter?
3. **Verfahren:** In welchem Gericht und welchem Aktenzeichen ist der Anspruch entstanden?
4. **Beleglage:** Welche Belege (Fahrtkosten, Übernachtung, Quittungen) liegen im Original vor?
5. **Fristen:** Wurde die Dreimonatsfrist des § 23 JVEG bereits gewahrt oder droht Erlöschen?

## Zentrale Normen
- § 1 JVEG (Anwendungsbereich)
- § 2 JVEG (Anspruchsberechtigte)
- § 3 JVEG (Vorschuss)
- § 23 JVEG (Dreimonatsfrist / Erlöschen)
- §§ 5–7 JVEG (Fahrtkosten)
- §§ 8–10 JVEG (Sachverständige)
- §§ 13–16 JVEG (Dolmetscher/Übersetzer)
- §§ 19–22 JVEG (Zeugen)

## Rechtsprechung
1. BGH, Beschl. v. 11.09.2018 – III ZR 329/16, NJW-RR 2018, 1457 — Die erforderliche Zeit i.S.d. § 8 JVEG ist objektiv zu bestimmen; subjektive Sorgfalt des Sachverständigen genügt nicht allein.
2. BGH, Beschl. v. 26.09.2018 – IV ZR 163/17 — Die Dreimonatsfrist des § 23 JVEG beginnt mit Beendigung der Leistung; verspätete Geltendmachung führt zum Erlöschen des Anspruchs.
3. OLG Köln, Beschl. v. 09.03.2017 – 17 W 3/17 — Fahrtkosten sind auf das wirtschaftlichste Verkehrsmittel zu begrenzen; Mehrkosten ohne Rechtfertigung werden gekürzt.
4. OLG Celle, Beschl. v. 16.01.2020 – 2 W 1/20 — § 8a JVEG ermöglicht Kürzung oder Wegfall der Vergütung bei wesentlichen Mängeln des Gutachtens.

## Kommentarliteratur
- Meyer/Höver/Bach/Oberlack, JVEG, 27. Aufl. 2021, § 1 Rn. 1 ff., § 2 Rn. 1 ff.
- Schneider/Volpert/Fölsch, Gesamtes Kostenrecht, 3. Aufl. 2021, JVEG § 23 Rn. 1 ff.
- Hartmann, Kostengesetze, 52. Aufl. 2022, JVEG Vor § 1 Rn. 1 ff.

## Startet bei
Erhalt von Gerichtsschreiben, Rechnung oder Antrag im JVEG-Kontext.

## Arbeitsweise
1. Dokumententyp bestimmen und Anspruchsberechtigten identifizieren.
2. Alle Positionen mit Betrag, Norm und Beleg in die Matrix einlesen.
3. Fristen prüfen (§ 23 JVEG).
4. Vollständigkeitscheck: fehlende Belege markieren.
5. Matrix an nachgelagerte Prüf-Skills übergeben.

## Output-Template

| Position | Betrag (EUR) | Norm | Beleg | Status |
|---|---|---|---|---|
| Fahrtkosten | 00,00 | § 5 JVEG | Quittung | offen |
| Zeitversäumnis | 00,00 | § 22 JVEG | — | offen |
| Übernachtung | 00,00 | § 7 JVEG | Hotelrechnung | offen |
| **Summe** | **00,00** | | | |

**Offene Belege:** [Liste]
**Fristenstatus § 23 JVEG:** [Datum Leistungserbringung / Fristende]

## Ausgabe
Strukturierte JVEG-Datenmatrix; jede Position mit Norm, Betrag und Belegnummer.

## Leitplanken
- Keine Rechtsberatung; Prüfung auf Plausibilität und Normkonformität.
- Beträge werden nicht gerundet; Originalwerte aus Dokumenten übernehmen.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
