---
name: statusrechte-einsatz-trennungsgeld
description: "Statusrechte Einsatz Trennungsgeld: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Statusrechte Einsatz Trennungsgeld

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Statusrechte Einsatz Trennungsgeld** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `statusrechte-im-einsatz-urlaub-betreuung` | Statusrechte im Einsatz, Urlaub, Betreuung: prüft Urlaubsansprüche, Betreuungsleistungen, Fürsorge im Auslandseinsatz und Rechtsbehelfe. Norm-/Quellenanker: SG § 30, EinsatzWVG, SVG. |
| `trennungsgeld-umzugskosten-reisekosten` | Trennungsgeld, Umzugskosten, Reisekosten: prüft TGV, BUKG, BRKG im Bundeswehr-Kontext. Norm-/Quellenanker: TGV, BUKG, BRKG. |
| `unterhaltssicherung-reservisten` | Unterhaltssicherung Reservisten: prüft UhSiG, Anspruchsberechtigte, Berechnung, Verfahren und Rechtsbehelfe. Norm-/Quellenanker: UhSiG. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Statusrechte Einsatz Trennungsgeld**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `statusrechte-im-einsatz-urlaub-betreuung`

**Fokus:** Statusrechte im Einsatz, Urlaub, Betreuung: prüft Urlaubsansprüche, Betreuungsleistungen, Fürsorge im Auslandseinsatz und Rechtsbehelfe. Norm-/Quellenanker: SG § 30, EinsatzWVG, SVG.

# Statusrechte im Einsatz: Urlaub, Betreuung und Fürsorge

## Fachkern: Statusrechte im Einsatz: Urlaub, Betreuung und Fürsorge
- **Spezialgegenstand:** Statusrechte im Einsatz: Urlaub, Betreuung und Fürsorge. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Im Auslandseinsatz haben Soldaten besondere Schutzrechte: Urlaub, Heimflüge, psychosoziale Betreuung, Fürsorge für Familie. Verletzungen der Fürsorge durch den Dienstherrn sind mit WBO anfechtbar.

Einsatz-bedingte Sonderregelungen: Verlängerung des Einsatzes, ungeplante Verwendungen und ihre Folgen.

## Einschlägige Normen und Quellen

- SG § 30 — Fürsorge (Einsatz)
- SG §§ 28–30 — Urlaubsanspruch
- EinsatzWVG — Weiterverwendung
- SVG §§ 63a ff. — Einsatzversorgung
- ZDv A-1402/1 — Betreuungsvorschrift

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- In welchem Einsatz und für welchen Zeitraum?
- Wurden Urlaubs- und Heimflugansprüche erfüllt?
- Gibt es psychosoziale Belastungen ohne Betreuungsangebot?
- Familie in Not während Einsatz — Sonderurlaub?
- Ungeplante Einsatzverlängerung?

## Prüf- und Arbeitslogik

### Schritt 1 — Urlaub und Heimflüge im Einsatz

Urlaubsanspruch: nach BUrlG (24 Werktage) zuzüglich Einsatz-Sonderurlaub.
Heimflug: i.d.R. bei Einsatzdauer > 4 Monate ein Heimflug genehmigt.
Familiäre Notlage: Sonderurlaub, kurzfristige Genehmigung.
Ablehnung: WBO-Beschwerde.

### Schritt 2 — Psychosoziale Betreuung

Einsatz belastet: Bundeswehr stellt Psychosoziale Betreuung (PSBw).
Inanspruchnahme: freiwillig, keine Disziplinarrelevanz.
PTBS-Prävention: Vorsorgeuntersuchungen.
Nachsorge: SanZ und BwKrhs nach Rückkehr.

### Schritt 3 — Fürsorge für Familie

SG § 30: Dienstherr hat Fürsorge für Angehörige im Einsatz.
Familienunterstützung: soziale Beratung durch Bundeswehr-Sozialdienst.
Notlagen: Sonderurlaub, finanzielle Soforthilfe.
Ansprechpartner: Sozialoffizier/Sozialbearbeiter.

### Schritt 4 — Einsatzverlängerung und Rechte

Verlängerung: Einwilligung des Soldaten erforderlich (über die geplante Einsatzzeit).
WBO-Beschwerde bei unzumutbarer Verlängerung.
Versorgungsfolgen: AVZ für gesamte Einsatzdauer.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Urlaubsansprüche im Auslandseinsatz
- Checkliste: Sonderurlaub bei familiärer Notlage
- Kontakte: PSBw, Sozialdienst Bundeswehr

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/sg/ — SG §§ 28–30
- https://www.gesetze-im-internet.de/bburlg/ — BUrlG
- https://www.bundeswehr.de/de/organisation/streitkraefte/sanitaetsdienst/psychosoziale-betreuung
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 2. `trennungsgeld-umzugskosten-reisekosten`

**Fokus:** Trennungsgeld, Umzugskosten, Reisekosten: prüft TGV, BUKG, BRKG im Bundeswehr-Kontext. Norm-/Quellenanker: TGV, BUKG, BRKG.

# Trennungsgeld, Umzugskosten und Reisekosten

## Fachkern: Trennungsgeld, Umzugskosten und Reisekosten
- **Spezialgegenstand:** Trennungsgeld, Umzugskosten und Reisekosten. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Versetzungen lösen ein komplexes System von Folgeansprüchen aus. Der Soldat muss aktiv Anträge stellen — die Ansprüche entstehen nicht automatisch.

Präklusionsfristen: TGV 6 Monate, BUKG 2 Jahre — unbedingt einhalten.

## Einschlägige Normen und Quellen

- TGV — Trennungsgeldverordnung
- BUKG — Bundesumzugskostengesetz
- BRKG — Bundesreisekostengesetz
- BBesG §§ 12–13 — Reisekostenvergütung
- SG § 22 — Versetzung

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Versetzungsverfügung und Datum?
- Umzugszusage § 3 BUKG vorhanden?
- TGV oder BUKG beansprucht?
- Reisekosten Dienstreise oder Familienheimfahrt?
- Rückforderungsbescheid?

## Prüf- und Arbeitslogik

### Schritt 1 — TGV im Detail

Trennungstagegeld: Betrag pro Tag der Trennung.
Trennungsübernachtungsgeld: bei Unterkunft am neuen Dienstort.
Reisegeld: Familienheimfahrten (Höhe nach Entfernung).
Antrag: spätestens 6 Monate nach Versetzung!

### Schritt 2 — BUKG im Detail

Umzugszusage: vor Umzug, ohne Zusage kein Anspruch!
Erstattungsfähige Kosten: Transportkosten, Mietentschädigungen, Maklerkosten, Reisekosten Familie.
Antrag: 2 Jahre nach Umzug.
Umzugspauschale: anstatt Einzelnachweise möglich.

### Schritt 3 — Reisekosten BRKG

Dienstreisen: Tagegeld (vollständig/gekürzt je nach Abwesenheitsdauer), Übernachtungsgeld, Fahrtkosten.
Kilometer-Pauschale für Pkw.
Bahncard: wenn wirtschaftlicher als Volltarif.
Abgrenzung Dienstreise vs. Familienheimfahrt.

### Schritt 4 — Rückforderung und Rechtsbehelfe

Rückforderung bei Falschangaben: keine Gutgläubigkeit möglich bei wissentlicher Fehlingabe.
Irrtum: Billigkeitserlass möglich.
Widerspruch: 1 Monat.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Fristenübersicht: TGV, BUKG, BRKG
- Berechnungsbeispiel Trennungsgeld-Antrag
- Checkliste: Umzugszusage BUKG

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/tgv/ — TGV
- https://www.gesetze-im-internet.de/bukg/ — BUKG
- https://www.gesetze-im-internet.de/brkg/ — BRKG

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `unterhaltssicherung-reservisten`

**Fokus:** Unterhaltssicherung Reservisten: prüft UhSiG, Anspruchsberechtigte, Berechnung, Verfahren und Rechtsbehelfe. Norm-/Quellenanker: UhSiG.

# Unterhaltssicherung für Reservisten

## Fachkern: Unterhaltssicherung für Reservisten
- **Spezialgegenstand:** Unterhaltssicherung für Reservisten. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Das UhSiG sichert den Lebensunterhalt von Arbeitnehmern und Selbstständigen während der Wehrübung. Anspruch: Verdienstausfallausgleich (Netto-Monatseinkommen abzüglich Wehrsold).

Selbstständige müssen Einkommen der letzten 3 Jahre nachweisen; dies ist oft die schwierigste Praxis-Hürde.

## Einschlägige Normen und Quellen

- UhSiG — Unterhaltssicherungsgesetz
- WSG — Wehrsoldgesetz (Abzug)
- ArbPlSchG — Arbeitgebererstattung
- SGB II/III — Schnittstellen
- SG §§ 60–69 — Dienstleistungspflicht

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Arbeitnehmer oder Selbstständiger?
- Welche Wehrübung (freiwillig/Pflicht)?
- Höhe des bisherigen Einkommens?
- Wurde UhSiG bereits beantragt?
- Streit über Berechnungsgrundlage?

## Prüf- und Arbeitslogik

### Schritt 1 — Anspruchsvoraussetzungen

Arbeitnehmer: laufendes Arbeitsverhältnis, Einkommensausfall durch Wehrübung.
Selbstständige: Einkommenseinbuße durch Abwesenheit.
FWD: kein UhSiG, aber WSG.
Pflicht-Heranziehung: UhSiG gilt.

### Schritt 2 — Berechnung Arbeitnehmer

Basis: Netto-Monatseinkommen aus Lohn/Gehalt.
Abzug: erhaltener Wehrsold.
Leistung: Differenz.
Nachweis: Lohnnachweis, letzter Monat vor Einberufung.

### Schritt 3 — Berechnung Selbstständiger

Basis: Durchschnittseinkommen der letzten 3 Jahre (steuerliche Nachweise).
Besonderheit: nicht der tatsächliche Ausfall, sondern Durchschnitt.
Streit: Berechnungsjahre, Einkommensart.

### Schritt 4 — Verfahren und Rechtsbehelfe

Antrag: Karrierecenter oder BAPersBw.
Fristen: Antrag möglichst vor Beginn der Übung.
Widerspruch gegen ablehnenden Bescheid: 1 Monat.
Klage: VG.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Berechnungsschema UhSiG Arbeitnehmer
- Berechnungsschema UhSiG Selbstständiger
- Checkliste: Unterlagen für UhSiG-Antrag

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/uhsig/ — UhSiG
- https://www.gesetze-im-internet.de/wsg/ — WSG
- https://www.gesetze-im-internet.de/arb-plschg/ — ArbPlSchG
- https://www.bundeswehr.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?
