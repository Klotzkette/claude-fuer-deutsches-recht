---
name: beschwerde-sofortcheck-bwbes
description: "Beschwerde Sofortcheck Bwbes: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Beschwerde Sofortcheck Bwbes

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Beschwerde Sofortcheck Bwbes** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `beschwerde-fristen-sofortcheck` | Beschwerde-Fristen Sofortcheck WBO: prüft Fristbeginn, Berechnung, Form, Wiedereinsetzung und Vollzugsaussetzung. Norm-/Quellenanker: §§ 6–11 und 23a WBO. |
| `bwbes-neu-010-besoldungswiderspruch-soldat-und-fristen` | Besoldungswiderspruch Soldat: prüft VwGO-Fristen, Form, aufschiebende Wirkung und Klagewege. Norm-/Quellenanker: §§ 68–73 VwGO, BBesG. |
| `disziplinarverfahren-intake` | Disziplinarverfahren Intake: strukturierte Aufnahme, Priorisierung, Ausgabe im Thema Disziplinarverfahren. Norm-/Quellenanker: WDO, SG, BVerwG Wehrdienstsenat. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Beschwerde Sofortcheck Bwbes**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `beschwerde-fristen-sofortcheck`

**Fokus:** Beschwerde-Fristen Sofortcheck WBO: prüft Fristbeginn, Berechnung, Form, Wiedereinsetzung und Vollzugsaussetzung. Norm-/Quellenanker: §§ 6–11 und 23a WBO.

# Beschwerde-Fristen Sofortcheck (WBO)

## Fachkern: Beschwerde-Fristen Sofortcheck (WBO)
- **Spezialgegenstand:** Beschwerde-Fristen Sofortcheck (WBO). Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Die WBO-1-Monats-Frist beginnt mit Bekanntgabe der Maßnahme — häufig früher als der Soldat denkt. Mündliche Mitteilung durch den Vorgesetzten reicht für Fristbeginn aus.

Fristversäumnis führt zur Unzulässigkeit. Wiedereinsetzung (§ 23a WBO) ist nur bei unverschuldetem Hindernis möglich. In der Praxis läuft der Soldat Gefahr, bei informellen Dienstgesprächen bereits die Frist in Gang zu setzen.

## Einschlägige Normen und Quellen

- § 6 WBO — Beschwerdefrist (1 Monat)
- § 7 WBO — Form der Beschwerde
- § 8 WBO — Zuständigkeit und Einreichung
- § 9 WBO — Aussetzung des Vollzugs
- § 10 WBO — Entscheidung
- § 17a WBO — Antrag auf gerichtliche Entscheidung (TDG)
- § 23a WBO — Wiedereinsetzung

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Was ist die angefochtene Maßnahme (Befehl, Versetzung, Beurteilung, Entlassung)?
- Wann wurde die Maßnahme bekannt gegeben (Datum, Form)?
- Ist die 1-Monats-Frist noch offen?
- Wurden Fristen versäumt — Hindernisse für Wiedereinsetzung?
- An wen und in welcher Form wurde Beschwerde eingereicht?
- Soll gleichzeitig Vollzugsaussetzung (§ 9 WBO) beantragt werden?

## Prüf- und Arbeitslogik

### Schritt 1 — Fristbeginn ermitteln

§ 6 WBO: Kenntnis der Maßnahme = Fristbeginn.
Mündliche Bekanntgabe: Beginn am selben Tag.
Schriftliche Zustellung: Beginn am Tag des Zugangs.
Fristende: entsprechendes Datum des Folgemonats.

### Schritt 2 — Fristberechnung

§§ 187 ff. BGB analog: Beginn am Folgetag nach Kenntnistag.
Fällt Fristende auf Sa/So/Feiertag → nächster Werktag.
Datum der Kenntnisnahme sichern (Zeugen, Schriftstücke, Protokoll).

### Schritt 3 — Form der Beschwerde § 7 WBO

Schriftlich oder zur Niederschrift.
Einreichung: nächster Disziplinarvorgesetzter (§ 8 WBO).
Pflichtinhalt: Maßnahme benennen, Antrag (Aufhebung/Änderung), Beschwerdeführer.
Fax/E-Mail: Schriftformerfordernis prüfen!

### Schritt 4 — Wiedereinsetzung § 23a WBO

Unverschuldetes Hindernis erforderlich.
Antrag: unverzüglich nach Wegfall, max. 2 Wochen.
Versäumte Handlung nachholen.
Gründe: Krankheit, Fehlberatung, höhere Gewalt.

### Schritt 5 — Vollzugsaussetzung § 9 WBO

Antrag bei Disziplinarvorgesetzten oder Beschwerdestelle.
Ermessen: Erfolgsaussichten und Vollzugsinteresse.
Bei drohender Versetzung/Entlassung: sofort beantragen.
Einstweiliger Rechtsschutz TDG: § 17a WBO analog.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Fristenkalender: WBO-Beschwerdefrist berechnen
- Muster-Beschwerde §§ 6–8 WBO
- Checkliste: Vollständigkeit Beschwerde
- Entscheidungsbaum: Frist abgelaufen → Wiedereinsetzung?

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/wbo/ — WBO
- https://dejure.org/gesetze/WBO/6.html
- https://www.bverwg.de
- https://openjur.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 2. `bwbes-neu-010-besoldungswiderspruch-soldat-und-fristen`

**Fokus:** Besoldungswiderspruch Soldat: prüft VwGO-Fristen, Form, aufschiebende Wirkung und Klagewege. Norm-/Quellenanker: §§ 68–73 VwGO, BBesG.

# Besoldungswiderspruch Soldat und Fristen

## Fachkern: Besoldungswiderspruch Soldat und Fristen
- **Spezialgegenstand:** Besoldungswiderspruch Soldat und Fristen. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Besoldungsstreitigkeiten folgen dem VwGO-Weg, nicht der WBO. Der Widerspruch ist Voraussetzung für die Klage (1-Monats-Frist nach Bescheidzustellung).

Wichtig: Unterscheidung dienstrechtliche Maßnahme (WBO) vs. Geldzahlungsanspruch (VwGO/VG).

## Einschlägige Normen und Quellen

- §§ 68–73 VwGO — Widerspruchsverfahren
- § 74 VwGO — Klagefrist
- § 80 VwGO — Aufschiebende Wirkung
- § 9a BBesG — Rückforderung
- § 6 WBO — Beschwerde (dienstrechtliche Maßnahmen)

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Was ist Streitgegenstand (Grundgehalt, Zulage, Rückforderung)?
- Schriftlicher Bescheid vorhanden? Wann zugestellt?
- Läuft 1-Monats-Frist noch?
- Aufschiebende Wirkung bei Rückforderung beantragen?
- Widerspruchsbescheid schon erteilt?

## Prüf- und Arbeitslogik

### Schritt 1 — Widerspruchsfrist und Form

§ 70 VwGO: 1 Monat ab Zustellung.
Schriftlich oder zur Niederschrift bei der Behörde.
Adressat: BAPersBw oder zuständiges Personalamt.
Eingang maßgeblich! Wiedereinsetzung § 60 VwGO möglich.

### Schritt 2 — Inhalt des Widerspruchs

Bezeichnung des Bescheides (Datum, Az).
Anfechtungsbegehren.
Begründung: Rechtsfehler, Rechenfehler, Ermessensfehler.
Belege beifügen.

### Schritt 3 — Aufschiebende Wirkung § 80 VwGO

Widerspruch hat grundsätzlich aufschiebende Wirkung.
Sofortige Vollziehung: Antrag § 80 Abs. 5 VwGO beim VG.
Ratenzahlung oder Sicherheitsleistung als Alternative.

### Schritt 4 — Klage nach Widerspruchsbescheid

§ 74 VwGO: 1 Monat nach Zustellung Widerspruchsbescheid.
VG: allgemeine Leistungsklage.
Kostentragung: §§ 161 ff. VwGO.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Muster-Widerspruch gegen Besoldungsbescheid
- Fristenplan: Widerspruch → Widerspruchsbescheid → Klage
- Entscheidungsbaum: WBO oder VwGO-Widerspruch?

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/vwgo/ — VwGO
- https://www.gesetze-im-internet.de/bbesg/ — BBesG
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `disziplinarverfahren-intake`

**Fokus:** Disziplinarverfahren Intake: strukturierte Aufnahme, Priorisierung, Ausgabe im Thema Disziplinarverfahren. Norm-/Quellenanker: WDO, SG, BVerwG Wehrdienstsenat.

# Disziplinarverfahren Intake

## Fachkern: Disziplinarverfahren Intake
- **Spezialgegenstand:** Disziplinarverfahren Intake. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Das Disziplinarverfahren nach WDO beginnt mit einer Pflichtverletzung und kann bis zur Entfernung aus dem Dienst führen. Einfache Maßnahmen liegen beim Disziplinarvorgesetzten; schwere Maßnahmen beim Truppendienstgericht.

Zentral ist die sorgfältige Sachverhaltsaufnahme zu Beginn: Status, Vorwurf, Verfahrensstand, Fristen, Rechtsbeistände.

## Einschlägige Normen und Quellen

- §§ 22–30 WDO — Einfache Disziplinarmaßnahmen
- §§ 58–77 WDO — Gerichtliches Disziplinarverfahren
- §§ 46–57 WDO — Untersuchungsverfahren
- §§ 1–17 WDO — Allgemeine Vorschriften, Fristen
- § 17 SG — Personalakte

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Was ist der Pflichtverletzungsvorwurf?
- Welches Verfahrensstadium liegt vor (Vorermittlung, förmliches Verfahren, Hauptverhandlung)?
- Welche Maßnahme droht?
- Hat der Soldat einen Rechtsbeistand?
- Welche Fristen laufen?
- Welche Dokumente liegen vor?

## Prüf- und Arbeitslogik

### Schritt 1 — Sofort-Triage

Verfahrensstadium: einfaches Verfahren (Disziplinarvorgesetzter) oder gerichtliches Verfahren (TDG)?
Vorwurf: konkreter Tatvorwurf festhalten.
Fristen: Einleitungsverfügung, Einspruchsfristen, Verhandlungstermin.
Risikobewertung: Maßnahmenschwere grün/gelb/rot.

### Schritt 2 — Verfahrensrechte des Soldaten

Rechtsbeistand: § 91 WDO, Wahlverteidiger.
Akteneinsicht: §§ 18–21 WDO.
Aussageverweigerungsrecht: analog StPO.
Anwesenheitsrecht bei Beweisaufnahme.

### Schritt 3 — Verteidigungsstrategie

Tatbestandsprüfung: Pflichtnorm, Tatbestand, Rechtswidrigkeit, Schuld.
Beweislast: WDO § 42: Dienstherr trägt Beweislast.
Milderungsgründe: WDO § 38.
Zeitliche Grenzen: Ausschlussfrist § 17 WDO.

### Schritt 4 — Einfache vs. gerichtliche Maßnahmen

Einfache Maßnahmen: Disziplinarvorgesetzter entscheidet (§§ 22–30 WDO).
Gerichtliche Maßnahmen: TDG entscheidet (§§ 58 ff. WDO).
Schwelle: gerichtliches Verfahren bei Degradierung, Entfernung.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Risikoampel: Verfahrensstand und Maßnahmenschwere
- Fragenliste für Mandantengespräch (Disziplinarverfahren)
- Tabelle: Einfache vs. gerichtliche Disziplinarmaßnahmen

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/wdo_2002/ — WDO
- https://www.bverwg.de — BVerwG Wehrdienstsenat
- https://openjur.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?
