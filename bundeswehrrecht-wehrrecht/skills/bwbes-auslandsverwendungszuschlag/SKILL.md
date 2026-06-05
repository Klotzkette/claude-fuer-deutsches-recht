---
name: bwbes-auslandsverwendungszuschlag
description: "Bwbes Auslandsverwendungszuschlag: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Bwbes Auslandsverwendungszuschlag

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Bwbes Auslandsverwendungszuschlag** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `bwbes-neu-003-auslandsverwendungszuschlag-und-einsatzversorgung` | AVZ und Einsatzversorgung: prüft §§ 56–58 BBesG, Gefährdungsstufen, EinsatzWVG, SVG §§ 63a ff. und PTBS-Anerkennung. Norm-/Quellenanker: BBesG, EinsatzWVG, SVG. |
| `bwbes-neu-004-trennungsgeld-umzugskosten-reisebeihilfe` | Trennungsgeld, Umzugskosten, Reisebeihilfe: prüft TGV, BUKG, Anspruchsvoraussetzungen, Präklusionsfristen und Rückforderungen. Norm-/Quellenanker: TGV, BUKG, BRKG. |
| `bwbes-neu-005-erschwerniszulagen-militaerischer-dienst` | Erschwerniszulagen militärischer Dienst: prüft EZulV, Anspruchsvoraussetzungen, Wegfall und Rückforderung. Norm-/Quellenanker: BBesG §§ 47–50, EZulV. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Bwbes Auslandsverwendungszuschlag**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `bwbes-neu-003-auslandsverwendungszuschlag-und-einsatzversorgung`

**Fokus:** AVZ und Einsatzversorgung: prüft §§ 56–58 BBesG, Gefährdungsstufen, EinsatzWVG, SVG §§ 63a ff. und PTBS-Anerkennung. Norm-/Quellenanker: BBesG, EinsatzWVG, SVG.

# Auslandsverwendungszuschlag und Einsatzversorgung

## Fachkern: Auslandsverwendungszuschlag und Einsatzversorgung
- **Spezialgegenstand:** Auslandsverwendungszuschlag und Einsatzversorgung. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Auslandseinsätze lösen besondere Besoldungs- und Versorgungsansprüche aus. AVZ tageweise nach Gefährdungsstufen; SVG §§ 63a ff. regeln Einsatzversorgung bei einsatzbedingten Schäden.

PTBS und psychische Einsatzfolgen sind anerkannte Wehrdienstbeschädigungen. Das EinsatzWVG sichert Weiterverwendung bei einsatzbedingten Schäden.

## Einschlägige Normen und Quellen

- §§ 56–58 BBesG — AVZ
- AuslVZV — Auslandsverwendungszulagenverordnung
- SVG §§ 63a–63h — Einsatzversorgung
- EinsatzWVG — Einsatzweiterverwendungsgesetz
- § 27 SVG — Wehrdienstbeschädigung
- SGB XIV — Soziales Entschädigungsrecht

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- In welchem Einsatz und welchem Zeitraum?
- Welche Gefährdungsstufe galt?
- Wurde der volle AVZ korrekt ausgezahlt?
- Einsatzbedingte Erkrankung oder Verletzung?
- Wurden Nachversorgungsansprüche geltend gemacht?
- Streit über Kausalität (Einsatz → Schaden)?

## Prüf- und Arbeitslogik

### Schritt 1 — AVZ Berechnung §§ 56–58 BBesG

Stufen 1–7 AuslVZV: Gefahrenlage und Region.
Tageweise Berechnung inkl. An-/Abreisetage.
Abgrenzung: AVZ (Kampfeinsatz) vs. Auslandsdienstbezüge § 52 BBesG (stationäre NATO-Verwendung).
Fehler: Stufenzuordnung korrekt? Alle Einsatztage erfasst?

### Schritt 2 — Einsatzversorgung SVG §§ 63a ff.

Einsatzbedingte Gesundheitsschäden: erleichterte Kausalitätsvermutung § 63c SVG.
Einsatz-Versorgungskrankengeld, Übergangsgeld.
Antrag beim BAPersBw, Versorgungsreferat.
Schäden unverzüglich melden — Beweissicherung!

### Schritt 3 — EinsatzWVG

Zweck: Weiterverwendung einsatzgeschädigter Soldaten.
Anspruch auf erneute Einstellung zur Rehabilitation.
Subsidiarität: erst SVG-Ansprüche, dann EinsatzWVG.

### Schritt 4 — PTBS und psychische Folgen

PTBS: anerkannte Wehrdienstbeschädigung.
Kausalität: 'hinreichende Wahrscheinlichkeit'.
Eigene Fachärzte einschalten, Gegengutachten.
Verwaltungsstreit: VG + Sozialgericht für Versorgungsleistungen.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: AVZ-Gefährdungsstufen und Tagessätze
- Prüfschema: Einsatzversorgungsansprüche SVG
- Checkliste: Einsatzbedingte Schäden dokumentieren

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/bbesg/ — §§ 56–58 BBesG
- https://www.gesetze-im-internet.de/einsatzwvg/ — EinsatzWVG
- https://www.gesetze-im-internet.de/svg/ — SVG §§ 63a ff.
- https://www.gesetze-im-internet.de/auslvzv/ — AuslVZV

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 2. `bwbes-neu-004-trennungsgeld-umzugskosten-reisebeihilfe`

**Fokus:** Trennungsgeld, Umzugskosten, Reisebeihilfe: prüft TGV, BUKG, Anspruchsvoraussetzungen, Präklusionsfristen und Rückforderungen. Norm-/Quellenanker: TGV, BUKG, BRKG.

# Trennungsgeld, Umzugskosten und Reisebeihilfe

## Fachkern: Trennungsgeld, Umzugskosten und Reisebeihilfe
- **Spezialgegenstand:** Trennungsgeld, Umzugskosten und Reisebeihilfe. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Versetzungen lösen Ansprüche auf Trennungsgeld (TGV), Umzugskostenvergütung (BUKG) und Reisebeihilfe aus. Typische Fehler: zu späte Beantragung, fehlende Umzugszusage (BUKG), fehlerhafte Berechnung des Trennungsgeldes.

Präklusionsfristen sind strikt: TGV-Antrag spätestens 6 Monate nach Versetzung; BUKG-Antrag 2 Jahre nach Umzug.

## Einschlägige Normen und Quellen

- TGV — Trennungsgeldverordnung
- BUKG — Bundesumzugskostengesetz
- BRKG — Bundesreisekostengesetz
- BBesG §§ 12–13 — Reisekostenvergütung
- SG § 22 — Versetzung (Auslöser)

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Liegt Versetzungsverfügung vor? Wann wirksam?
- Hat der Soldat Umzugszusage § 3 BUKG erhalten?
- Trennungsgeld oder Umzugskostenvergütung?
- Wie lange dauert Trennung vom Familienwohnsitz?
- Familienheimfahrten beansprucht?
- Droht Rückforderung?

## Prüf- und Arbeitslogik

### Schritt 1 — Trennungsgeld TGV

Anspruch: Soldat versetzt, Familienwohnsitz nicht aufgegeben, wohnt am neuen Dienstort.
Trennungstagegeld, Übernachtungsgeld, Reisegeld (Familienheimfahrten).
Präklusionsfrist: Antrag spätestens 6 Monate nach Versetzung!
Dauer: i.d.R. max. 3 Jahre, Verlängerung ausnahmsweise.

### Schritt 2 — Umzugskostenvergütung BUKG

Umzugszusage § 3 BUKG vor dem Umzug — zwingend!
Erstattungsfähig: Beförderungskosten, Mietentschädigungen, Maklerkosten.
Antrag: innerhalb 2 Jahre nach Umzug.
Familie mitgezogen: erhöhte Pauschalen.

### Schritt 3 — Reisekostenvergütung BRKG

Dienstreisen: Tagegeld, Übernachtung, Fahrtkosten.
Familienheimfahrten im Trennungsgeld: TGV geht vor.
Auslandseinsatz: AVZ hat Vorrang (lex specialis).

### Schritt 4 — Rückforderung und Rechtsbehelfe

Rückforderung bei Falschangaben oder vorzeitiger Rückkehr.
Gutglaubensschutz analog BBesG.
Billigkeitserlass möglich.
Widerspruch: 1 Monat nach Bescheid.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Checkliste: Unterlagen BUKG-Antrag
- Fristen-Übersicht: TGV vs. BUKG
- Muster-Antrag Trennungsgeld

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
- https://dejure.org/gesetze/TGV

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `bwbes-neu-005-erschwerniszulagen-militaerischer-dienst`

**Fokus:** Erschwerniszulagen militärischer Dienst: prüft EZulV, Anspruchsvoraussetzungen, Wegfall und Rückforderung. Norm-/Quellenanker: BBesG §§ 47–50, EZulV.

# Erschwerniszulagen für militärischen Dienst

## Fachkern: Erschwerniszulagen für militärischen Dienst
- **Spezialgegenstand:** Erschwerniszulagen für militärischen Dienst. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Soldaten in bestimmten Verwendungen erhalten Erschwerniszulagen: Fallschirmspringer, Kampfschwimmer, Minenräumer, ABC-Schutz, Heeresfliegerpersonal. Voraussetzung: aktive Ausübung der qualifizierten Tätigkeit.

Wegfall der Verwendung führt oft zum sofortigen Wegfall der Zulage — Rückforderung nur bei Bösgläubigkeit.

## Einschlägige Normen und Quellen

- §§ 47–50 BBesG — Zulagen für Erschwernisse
- EZulV — Erschwerniszulagenverordnung
- § 9a BBesG — Rückforderung Bezüge
- ZDv — Verwendungsbestimmungen für besondere Tätigkeiten

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Welche Erschwerniszulage beansprucht oder weggefallen?
- Welche Tätigkeit liegt vor (Fallschirmjäger, ABC, Taucher)?
- Liegen Voraussetzungen der EZulV vor?
- Rückforderungsbescheid erlassen?
- War Soldat gutgläubig?

## Prüf- und Arbeitslogik

### Schritt 1 — Anspruchsvoraussetzungen EZulV

EZulV § 2 ff.: Zulage nur bei aktiver Ausübung.
Fallschirmspringen: Mindestanzahl Sprünge/Jahr.
Kampfschwimmer: Tauchschein und aktive Einsätze.
Heeresflugzeugführer: aktive Flugverwendung.
Erfüllungsnachweise prüfen.

### Schritt 2 — Wegfall der Zulage

Verwendungswechsel → Zulage entfällt mit Monatsende.
Keine auslaufende Zahlung ohne Rechtsgrundlage.
Mitteilungspflicht des Dienstherrn; ohne Mitteilung: Gutglaubensschutz.
Übergangsregelungen EZulV beachten.

### Schritt 3 — Rückforderung § 9a BBesG

Überzahlte Zulagen grundsätzlich rückforderbar.
Gutgläubiger Empfang und Verbrauch: kein Rückforderungsanspruch.
Bösgläubigkeit: Soldat wusste oder hätte wissen müssen.
Billigkeitserlass möglich.

### Schritt 4 — Rechtsbehelfe

Widerspruch 1 Monat.
Klage: VG.
Parallel: Billigkeitserlass beantragen.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Erschwerniszulagen nach EZulV (Typen, Voraussetzungen, Höhe)
- Checkliste: Nachweise für Erschwerniszulage
- Muster-Widerspruch gegen Rückforderungsbescheid

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/ezulv/ — EZulV
- https://www.gesetze-im-internet.de/bbesg/ — §§ 47–50 BBesG

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?
