---
name: norm-zerlegen-in-tatbestandsmerkmale
description: "Zerlegt eine Norm systematisch in ihre Tatbestandsmerkmale (TBM): geschriebene und ungeschriebene Merkmale, Definitionen aus h.M. und Rechtsprechung, Pruefungsreihenfolge. Grundlage fuer den Vier-Schritt der Subsumtion je TBM."
---

# Norm zerlegen in Tatbestandsmerkmale

## Triage zu Beginn — kläre vor der TBM-Zerlegung

1. Welche Norm soll zerlegt werden? (Vollzitat mit Paragraph, Absatz, Satz, Nummer)
2. Vertragsrecht, Delikt, Strafrecht, öffentliches Recht? → Prüfungsschema variiert
3. Enthält die Norm Verweisungen (i.V.m. einer anderen Norm)? → Kettenverweisung entfalten
4. Sind ungeschriebene Tatbestandsmerkmale einschlägig (Verkehrspflichten, soziale Adäquanz)?
5. Gibt es Normen im EU-Recht, die die nationale Norm verdrängen oder überlagern?

## Zweck

Bevor subsumiert werden kann, muss die Norm in ihre Tatbestandsmerkmale (TBM) zerlegt werden. Dieser Skill führt die strukturierte Zerlegung durch, benennt Definitionen aus h.M. und Rechtsprechung und legt die Prüfungsreihenfolge fest.

## Zentrale Methodik

### Schritt 1 — Normtext lesen und gliedern

Das System liest den Normtext und unterteilt in:
- **Tatbestand** (Voraussetzungen, die vorliegen müssen)
- **Rechtsfolge** (was bei Vorliegen des Tatbestands gilt)
- **Ausnahmen / Gegenausnahmen** (soweit in der Norm selbst geregelt)

### Schritt 2 — TBM-Liste erstellen

**Beispiel § 823 Abs. 1 BGB:**
1. Handlung oder Unterlassen
2. Verletzung eines der geschützten Rechtsgüter (Leben, Körper, Gesundheit, Freiheit, Eigentum oder sonstiges Recht)
3. Widerrechtlichkeit (Rechtswidrigkeitsindiz bei Rechtsgutsverletzung; Rechtfertigungsgründe ausschließen)
4. Verschulden (Vorsatz oder Fahrlässigkeit § 276 BGB)
5. Schaden (Vermögensdifferenz; Differenzhypothese)
6. Kausalität: haftungsbegründend und haftungsausfüllend

**Beispiel § 433 Abs. 1 BGB (Kaufvertrag — Verkäuferpflicht):**
1. Wirksamer Kaufvertrag (§§ 145 ff. BGB: Angebot und Annahme)
2. Fälligkeit des Anspruchs (§§ 271 ff. BGB)
3. Nicht erfüllt (§ 362 BGB: noch keine Erfüllung)

### Schritt 3 — Definitionen aus h.M. und Rechtsprechung

## Aktuelle Rechtsprechung zur Methodik

- BGH, Urt. v. 17.10.2019 - III ZR 42/19, NJW 2020, 399 — Die Tatbestandsmerkmale einer Norm sind im Wege der klassischen Auslegungsmethoden zu ermitteln (Wortlaut, Systematik, teleologisch, historisch); das Gericht ist an den Wortlaut gebunden, darf aber auslegen.
- BGH, Urt. v. 09.04.2019 - VI ZR 89/18, NJW 2019, 2162 — Ungeschriebene Tatbestandsmerkmale (Verkehrspflichten) werden richterrechtlich entwickelt und sind als TBM im Vier-Schritt zu prüfen wie geschriebene Merkmale.
- BVerfG, Beschl. v. 31.10.2016 - 1 BvR 871/13, NJW 2017, 222 — Die Auslegung einer Norm darf nicht zu einer Auslegung contra legem führen; der Richter ist an den demokratisch legitimierten Gesetzgeberwillen gebunden.
- EuGH, Urt. v. 24.06.2019 - C-573/17, NJW 2019, 2667 — Unionsrechtliche Begriffe sind autonom auszulegen; nationale Begriffsbestimmungen der Mitgliedstaaten sind nicht maßgebend, soweit die Norm das Unionsrecht umsetzt.

## Definitionen ausgewählter TBM

- **„Handlung":** jedes menschliche Verhalten, das vom Willen beherrschbar ist; Reflex und vis absoluta scheiden aus
- **„Fahrlässigkeit":** Außerachtlassen der im Verkehr erforderlichen Sorgfalt (§ 276 Abs. 2 BGB); objektiver Sorgfaltsmaßstab
- **„Schaden":** Differenz zwischen tatsächlichem und hypothetischem Vermögenszustand ohne das schädigende Ereignis (Differenzhypothese, § 249 BGB)
- **„Verschulden" im Vertragsrecht:** § 280 Abs. 1 S. 2 BGB — Vermutung des Vertretenmüssens; Schuldner muss Exkulpation führen

### Schritt 4 — Ungeschriebene TBM

Das System weist auf judikativ entwickelte ungeschriebene Merkmale hin (z.B. bei § 823 Abs. 1 BGB: Verkehrspflichten als ungeschriebenes Pflichtengebot). Details in Skill `ungeschriebene-merkmale-judikatur`.

### Schritt 5 — Prüfungsreihenfolge nach Normentyp

| Normentyp | Prüfungsreihenfolge |
|-----------|-------------------|
| Anspruchsgrundlage | Entstehung → Erlöschen → Durchsetzbarkeit |
| Straftatbestand | TB obj. + subj. → Rechtswidrigkeit → Schuld |
| Grundrechtsprüfung | Schutzbereich → Eingriff → Rechtfertigung |
| Verwaltungsakt | Zuständigkeit → Form → Inhalt → Verhältnismäßigkeit |

### Schritt 6 — Übergabe an Subsumtion

Nach der TBM-Liste übergibt das System je TBM an den Skill `subsumtion-obersatz-definition-untersatz-ergebnis`.

## Besonderheiten bei Unionsrecht

Bei EU-Normen benennt das System zusätzlich:
- Erwägungsgründe (ErwGr) als Auslegungshilfe
- EuGH-Leitentscheidungen zur Normauslegung
- Unterschied zwischen autonomer unionsrechtlicher Auslegung und mitgliedstaatlichem Ermessen

## Kommentarliteratur

- Grüneberg BGB § 276 (Fahrlässigkeit/Vorsatz — Definitionskern)
- MüKo BGB § 823 Rn. 1 ff. (TBM-Zerlegung Deliktsrecht — umfassend)
- Larenz/Canaris Methodenlehre der Rechtswissenschaft (Auslegung, TBM-Ermittlung)

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.
