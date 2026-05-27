---
name: jveg-antragsgenerator
description: "Antrag auf gerichtliche Kostenfestsetzung nach JVEG erstellen: Verguetungsantrag, Anlagen, Fristen. Normen: §§ 2 4 JVEG. Pruefraster: Antragsfrist, Formerfordernis, Anlagenliste. Output: Kostenfestsetzungsantrag nach JVEG. Abgrenzung: nicht Beschwerde gegen Festsetzung."
---

# JVEG-Antragsgenerator

## Aufgabe
Erstelle druckfertige JVEG-Antragsschreiben (Vorschuss, Nachzahlung, Festsetzung, Ergänzung) mit vollständiger Anlagen- und Belegliste.

## Triage — kläre vor der Erstellung

1. **Antragsart:** Vorschuss (§ 3 JVEG), Nachzahlung, Festsetzungsantrag (§ 4 JVEG) oder Ergänzungsantrag?
2. **Anspruchsberechtigter:** Sachverständiger, Zeuge, Dolmetscher oder Übersetzer?
3. **Fristen:** Ist die Dreimonatsfrist des § 23 JVEG noch nicht abgelaufen?
4. **Beleglage:** Welche Belege (Fahrtkosten, Zeitnachweise, Rechnungen) liegen vor und sollen beigefügt werden?
5. **Vorschussstand:** Wurde bereits ein Vorschuss gewährt — wie hoch und wann ausgezahlt?

## Zentrale Normen
- § 3 JVEG (Vorschuss)
- § 4 JVEG (Festsetzung durch das Gericht)
- § 4 Abs. 3 JVEG (Beschwerde gegen Festsetzungsbeschluss)
- § 23 JVEG (Dreimonatsfrist / Erlöschen)
- §§ 5–7 JVEG (Fahrtkosten)
- §§ 8–10 JVEG (Sachverständige)
- §§ 13–16 JVEG (Dolmetscher/Übersetzer)
- §§ 19–22 JVEG (Zeugen)

## Rechtsprechung
1. BGH, Beschl. v. 11.09.2018 – III ZR 329/16, NJW-RR 2018, 1457 — Vergütungsanträge müssen die tatsächlich erforderliche Zeit nachvollziehbar belegen; pauschale Schätzungen genügen nicht.
2. BGH, Beschl. v. 26.09.2018 – IV ZR 163/17 — Die Dreimonatsfrist des § 23 JVEG ist eine Ausschlussfrist; bei Versäumnis entfällt der Anspruch endgültig.
3. OLG Köln, Beschl. v. 09.03.2017 – 17 W 3/17 — Anträge müssen Fahrtkosten mit Streckennachweis und Wirtschaftlichkeitsprüfung belegen.
4. OLG Celle, Beschl. v. 16.01.2020 – 2 W 1/20 — Ein Ergänzungsantrag ist nur möglich, soweit der Ursprungsantrag die Position nicht erfasst hat; keine Nachbesserung bereits beschiedener Positionen.

## Kommentarliteratur
- Meyer/Höver/Bach/Oberlack, JVEG, 27. Aufl. 2021, § 3 Rn. 1 ff., § 4 Rn. 1 ff.
- Schneider/Volpert/Fölsch, Gesamtes Kostenrecht, 3. Aufl. 2021, JVEG § 23 Rn. 1 ff.
- Hartmann, Kostengesetze, 52. Aufl. 2022, JVEG § 4 Rn. 1 ff.

## Startet bei
Mandant oder Sachverständiger möchte JVEG-Vergütung gerichtlich festsetzen lassen oder Vorschuss beantragen.

## Arbeitsweise
1. Antragsart und Anspruchsgrundlage bestimmen.
2. Alle Positionen mit Normbezug und Belegverweis auflisten.
3. Frist § 23 JVEG prüfen und im Schreiben dokumentieren.
4. Anlagenliste mit Belegnummern erstellen.
5. Druckfertiges Schreiben mit Adresse, Aktenzeichen, Datum und Antragstellung formulieren.

## Output-Template

**[Gericht / Kostenbeamter]**
**Az.:** [Aktenzeichen]
**Datum:** [TT.MM.JJJJ]

**Antrag auf [Festsetzung / Vorschuss / Nachzahlung] nach JVEG**

Ich beantrage die Festsetzung folgender Vergütung:

| Position | Betrag (EUR) | Norm | Anlage |
|---|---|---|---|
| [Position] | 00,00 | § X JVEG | Anlage [Nr.] |
| **Gesamtbetrag** | **00,00** | | |

Belege: [Liste der Anlagen]
Fristwahrung § 23 JVEG: Leistung erbracht am [Datum]; Antrag fristgerecht.

## Ausgabe
Druckfertiges Antragsschreiben mit Positionsliste, Normenbezug und Anlagenliste.

## Leitplanken
- Kein Schreiben ohne geprüfte Fristen (§ 23 JVEG).
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
