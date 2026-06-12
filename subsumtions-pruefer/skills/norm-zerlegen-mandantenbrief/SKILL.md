---
name: norm-zerlegen-mandantenbrief
description: "Zerlegt eine Norm systematisch in ihre Tatbestandsmerkmale (TBM): geschriebene und ungeschriebene Merkmale, Definitionen aus h.M. und Rechtsprechung, Prüfungsreihenfolge. Grundlage für den Vier-Schritt der Subsumtion je TBM im Subsumtions Prüfer."
---

# Norm zerlegen in Tatbestandsmerkmale

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn — kläre vor der TBM-Zerlegung

1. Welche Norm soll zerlegt werden? (Vollzitat mit Paragraph, Absatz, Satz, Nummer)
2. Vertragsrecht, Delikt, Strafrecht, öffentliches Recht? → Prüfungsschema variiert
3. Enthält die Norm Verweisungen (i.V.m. einer anderen Norm)? → Kettenverweisung entfalten
4. Sind ungeschriebene Tatbestandsmerkmale einschlägig (Verkehrspflichten, soziale Adäquanz)?
5. Gibt es Normen im EU-Recht, die die nationale Norm verdrängen oder überlagern?

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

## Quellen für Definitionen und Methodik

- **Normtext zuerst:** Wortlaut, Satzstruktur, Verweisungen, Ausnahmen und Rechtsfolge sichtbar zerlegen.
- **Gesetzesmaterialien und Systematik:** Bei offenen Begriffen fachliche Einordnung, Stellung im Gesetz und Zweck der Norm heranziehen.
- **Kommentare und Lehrbücher:** Definitionen nur mit Fundstelle übernehmen; abweichende Ansichten als solche kennzeichnen.
- **Rechtsprechung zur konkreten Norm:** Nur Entscheidungen zitieren, die das jeweilige Tatbestandsmerkmal wirklich behandeln. Keine abstrakten Methodenzitate erfinden.
- **EU-Recht:** Bei unionsrechtlich geprägten Begriffen prüfen, ob autonome Auslegung des Unionsrechts Vorrang vor nationalen Definitionen hat.

## Definitionen ausgewählter TBM

- **"Handlung":** jedes menschliche Verhalten, das vom Willen beherrschbar ist; Reflex und vis absoluta scheiden aus
- **"Fahrlässigkeit":** Außerachtlassen der im Verkehr erforderlichen Sorgfalt (§ 276 Abs. 2 BGB); objektiver Sorgfaltsmaßstab
- **"Schaden":** Differenz zwischen tatsächlichem und hypothetischem Vermögenszustand ohne das schädigende Ereignis (Differenzhypothese, § 249 BGB)
- **"Verschulden" im Vertragsrecht:** § 280 Abs. 1 S. 2 BGB — Vermutung des Vertretenmüssens; Schuldner muss Exkulpation führen

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
