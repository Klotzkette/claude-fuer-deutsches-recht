---
name: norm-zerlegen-mandantenbrief
description: "Norm Zerlegen Mandantenbrief: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Norm Zerlegen Mandantenbrief

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Norm Zerlegen Mandantenbrief** im Plugin Subsumtions-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `norm-zerlegen-in-tatbestandsmerkmale` | Zerlegt eine Norm systematisch in ihre Tatbestandsmerkmale (TBM): geschriebene und ungeschriebene Merkmale, Definitionen aus h.M. und Rechtsprechung, Prüfungsreihenfolge. Grundlage für den Vier-Schritt der Subsumtion je TBM. |
| `output-memo-und-mandantenbrief` | Erzeugt interne Aktennotiz (Rechtsmemo) oder externen Mandantenbrief als Ausgabe der Subsumtion. Klarer Unterschied: Memo für interne Nutzung mit juristischer Tiefe; Mandantenbrief für Betroffene in verstaendlicher Sprache. Beide mit Pflicht-Haftungshinweis. |
| `output-pruefungsdokument-mit-warnhinweisen` | Erzeugt das vollständige Prüfungsdokument mit Pflicht-Kopfhinweis: kein Rechtsgutachten, kein Rechtsrat, nur mechanische Prüfung anhand Nutzerangaben. Enthaelt alle Warnhinweise an markanten Stellen des Dokuments und Abschluss-Disclaimer. |

## Arbeitsweg

Im Plugin Subsumtions-Prüfer gilt für **Norm Zerlegen Mandantenbrief**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `norm-zerlegen-in-tatbestandsmerkmale`

**Fokus:** Zerlegt eine Norm systematisch in ihre Tatbestandsmerkmale (TBM): geschriebene und ungeschriebene Merkmale, Definitionen aus h.M. und Rechtsprechung, Prüfungsreihenfolge. Grundlage für den Vier-Schritt der Subsumtion je TBM.

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

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `output-memo-und-mandantenbrief`

**Fokus:** Erzeugt interne Aktennotiz (Rechtsmemo) oder externen Mandantenbrief als Ausgabe der Subsumtion. Klarer Unterschied: Memo für interne Nutzung mit juristischer Tiefe; Mandantenbrief für Betroffene in verstaendlicher Sprache. Beide mit Pflicht-Haftungshinweis.

# Output: Memo und Mandantenbrief

## Triage zu Beginn

1. Ist ein internes Memo oder ein externer Brief gewünscht?
2. Gibt es ein Aktenzeichen für das Memo?
3. Soll der Mandantenbrief eine Fristsetzung enthalten?
4. In welcher Sprache? (Deutsch / Englisch / Zweisprachig → Skill output-fremdsprachig-en-fr)

## Rechtsprechung und berufsrechtliche Grundlage

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zweck

Dieser Skill erzeugt zwei verschiedene Ausgabeformate auf Basis des Subsumtionsergebnisses: eine interne Aktennotiz (Rechtsmemo) für die Verwendung im juristischen Kontext und einen externen Mandantenbrief für die Kommunikation mit dem Betroffenen. Beide Formate tragen unterschiedliche Sprache, unterschiedliche Tiefe und zwingend denselben Haftungshinweis.

## Format 1: Interne Aktennotiz (Rechtsmemo)

### Zweck des Memos

Das Memo dokumentiert die Subsumtion intern, dient als Arbeitsgrundlage und als Grundlage für das weitere Vorgehen. Es ist kein Schriftsatz und kein anwaltliches Beratungsschreiben.

### Aufbau

```
AKTENNOTIZ / RECHTSMEMO
Erstellt: [Datum]
Betreff: [Rechtsfrage / Norm / Sachverhalt kurz]
Aktenzeichen (intern): [optional]
---

I. SACHVERHALT (NUTZEREINGABE)
[Zusammenfassung des Sachverhalts aus Nutzereingaben — keine eigenen Ergänzungen]

II. GEPRÜFTE NORM(EN)
[Liste der geprüften Normen]

III. SUBSUMTION
[Vier-Schritt-Schema je TBM; Ergebnis je TBM]

IV. EINWENDUNGEN / EINREDEN
[Geprüfte Gegenrechte; Ergebnis]

V. RECHTSFOLGE
[Bestimmte Rechtsfolge, Höhe, Nebenansprüche]

VI. BEWEISBEDARF
[Offene TBM; fehlende Belege; Risikohinweis]

VII. EMPFEHLUNG
[Nächste Schritte: Schriftsatz / Widerspruch / Anwalt / Abbruch]

VIII. WARNHINWEIS
Dieses Memo ist ein mechanisch erzeugtes Arbeitsdokument auf Basis der Nutzerangaben.
Es ist keine Rechtsberatung und keine anwaltliche Stellungnahme.
```

### Sprachstil Memo

Juristisch präzise; Paragrafenangaben vollständig; Zitate im BGH-Format; Abkürzungen bei einmaliger Ausschreibung zulässig.

## Format 2: Mandantenbrief

### Zweck des Mandantenbriefs

Der Mandantenbrief richtet sich an den Betroffenen (nicht-juristischen Leser). Er erklärt das Ergebnis in verständlicher Sprache und gibt klare Handlungsempfehlungen.

### Aufbau

```
[Ort, Datum]
Betreff: Ihre Anfrage zu [Sachverhalt kurz]
Sehr geehrte/r [Name],

[Einleitung: kurze Zusammenfassung des Anliegens]
[Ergebnis in Alltagssprache: Was haben wir geprüft? Was hat sich ergeben?]
[Was bedeutet das für Sie? Mögliche nächste Schritte.]
[Was Sie noch brauchen: Belege, Fristen, Ansprechpartner]

Mit freundlichen Grüßen
[Absender — ggf. Kanzlei / Beratungsstelle]
```

### Pflicht-Haftungshinweis im Mandantenbrief

> **Wichtiger Hinweis:** Dieses Schreiben ist das Ergebnis einer mechanischen Prüfung auf Basis der von Ihnen genannten Tatsachen und der von Ihnen gewählten Norm. Es ist keine Rechtsberatung und keine anwaltliche Stellungnahme. Es ersetzt nicht die Prüfung durch einen zugelassenen Rechtsanwalt. Wenn Sie rechtliche Schritte einleiten oder auf dieses Ergebnis vertrauen möchten, wenden Sie sich bitte zuerst an einen Fachanwalt.

### Sprachstil Mandantenbrief

Verständlich, direkt, ohne Fachbegriffe (oder mit sofortiger Erklärung). Details in Skill `output-alltagssprache-de`.

## Auswahl durch Nutzer

Das System fragt: Welches Format benötigen Sie?
- (A) Interne Aktennotiz (Rechtsmemo)
- (B) Mandantenbrief (externer Brief an Betroffene)
- (C) Beides

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.

## 3. `output-pruefungsdokument-mit-warnhinweisen`

**Fokus:** Erzeugt das vollständige Prüfungsdokument mit Pflicht-Kopfhinweis: kein Rechtsgutachten, kein Rechtsrat, nur mechanische Prüfung anhand Nutzerangaben. Enthaelt alle Warnhinweise an markanten Stellen des Dokuments und Abschluss-Disclaimer.

# Output: Prüfungsdokument mit Warnhinweisen

## Zweck

Dieses Ausgabe-Format ist das vollständigste und transparenteste Format des Subsumtions-Prüfers. Es enthält an jedem kritischen Punkt des Dokuments einen Warnhinweis, der dem Leser klar macht, was das Dokument ist — und was es ausdrücklich nicht ist.

## Triage zu Beginn

1. Wird das Dokument von juristisch nicht vorgebildeten Personen gelesen?
2. Besteht besonderes Haftungsrisiko (Fristen, Vollstreckungshandlungen, Strafrecht)?
3. Soll das Dokument als Grundlage für eine Klageschrift / einen Widerspruch dienen?
4. Sind Generalklauseln oder unbestimmte Rechtsbegriffe einschlägig? → Warnhinweis verschärfen

## Rechtsprechung zur Dokumentationspflicht

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Pflicht-Kopf (jedes Prüfungsdokument beginnt damit)

```
============================================================
PRÜFUNGSDOKUMENT — KEINE RECHTSBERATUNG
============================================================

Dieses Dokument ist keine Rechtsberatung und keine
Rechtsanwendung. Es prüft mechanisch eine vom Nutzer
behauptete Norm anhand vom Nutzer behaupteter Tatsachen.

Das System kann nicht prüfen:
• ob der Nutzer die richtige Norm gewählt hat
• ob der Sachverhalt vollständig oder korrekt geschildert ist
• ob es eine vorrangige, speziellere oder günstigere Norm gibt
• ob die Gegenseite andere Tatsachen behauptet oder belegt
• ob Generalklauseln und unbestimmte Rechtsbegriffe im
 Einzelfall wie ausgelegt zugunsten oder zulasten des Nutzers
 ausgelegt werden
• ob das Prüfungsergebnis vor Gericht standhält

Erstellt: [Datum]
Betreff: Mechanische Subsumtionsprüfung
Norm: [geprüfte Norm]
Sachverhalt: [kurze Zusammenfassung Nutzerangabe]
============================================================
```

## Struktur des Gesamtdokuments

### Abschnitt 1 — Eingabe (Nutzereingaben dokumentiert)

Alle Nutzerangaben werden wortwörtlich wiedergegeben. Keine Ergänzungen durch das System. Damit ist für den Leser klar, worauf das Prüfungsergebnis beruht.

### Abschnitt 2 — Normwahl (mit Warnhinweis)

> **Normwahl-Warnung:** Die nachfolgende Prüfung bezieht sich ausschließlich auf die vom Nutzer genannte Norm. Das System hat keine unabhängige Prüfung vorgenommen, ob diese Norm die einschlägige, vollständige oder richtige Grundlage ist. Die "falsche-Wiese-Warnung" (Skill `falsche-wiese-warnung`) empfiehlt, die Normwahl vorab zu validieren.

### Abschnitt 3 — Tatbestandsmerkmale (je TBM mit Warnhinweis)

Bei jedem Tatbestandsmerkmal, das mit "fraglich" oder "offen" endet:

> **TBM-Warnhinweis:** Dieses Tatbestandsmerkmal konnte nicht abschließend beurteilt werden. Das Gesamtergebnis ist entsprechend unsicher.

### Abschnitt 4 — Generalklauseln und unbestimmte Rechtsbegriffe (mit Warnhinweis)

> **Generalklausel-Warnung:** Das Prüfungsergebnis zu diesem Merkmal ist eine Indiziensammlung, kein Subsumtionsergebnis. Generalklauseln und unbestimmte Rechtsbegriffe können mechanisch nicht abschließend beurteilt werden.

### Abschnitt 5 — Subsumtionsergebnis (mit Warnhinweis)

> **Ergebnis-Warnung:** Das nachfolgende Ergebnis gilt nur unter der Prämisse, dass alle Nutzerangaben vollständig und korrekt sind und die gewählte Norm die einschlägige Grundlage ist. Abweichende Tatsachen oder eine andere Normwahl würden zu einem anderen Ergebnis führen.

### Abschnitt 6 — Abschluss-Disclaimer (Pflicht)

```
============================================================
ABSCHLUSS-DISCLAIMER
============================================================

Dieses Prüfungsdokument wurde automatisch auf Basis der
Eingaben des Nutzers erstellt. Es ist kein Rechtsgutachten,
keine anwaltliche Stellungnahme und keine Rechtsberatung.

Für alle rechtlich relevanten Entscheidungen — insbesondere
Klageerhebung, Widerspruch, Strafanzeige, Vertragsschluss
oder -kündigung — ist die Prüfung durch einen zugelassenen
Rechtsanwalt (ggf. Fachanwalt) unerlässlich.

Falsche Normwahl oder falsche Sachverhaltsdarstellung kann
das gesamte Ergebnis entwerten.
============================================================
```

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen und der vom Nutzer gewählten Norm. Falsche Normwahl oder falsche Sachverhaltsdarstellung kann das gesamte Ergebnis entwerten.
