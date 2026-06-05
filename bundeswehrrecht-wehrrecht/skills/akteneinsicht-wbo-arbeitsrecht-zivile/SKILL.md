---
name: akteneinsicht-wbo-arbeitsrecht-zivile
description: "Akteneinsicht WBO Arbeitsrecht Zivile: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Akteneinsicht WBO Arbeitsrecht Zivile

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Akteneinsicht WBO Arbeitsrecht Zivile** im Plugin Bundeswehrrecht Wehrrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `akteneinsicht-wbo-wdo` | Akteneinsicht WBO und WDO: prüft Einsichtsrechte, Umfang, Verweigerungsgründe und Rechtsbehelfe. Norm-/Quellenanker: §§ 4–5 WBO, §§ 18–21 WDO, § 17 SG. |
| `arbeitsrecht-zivile-bundeswehrbeschaeftigte` | Arbeitsrecht zivile Bundeswehrbeschäftigte: prüft TVöD-Anwendung, Personalrat BPersVG, Kündigung, Versetzung und Rechtsweg. Norm-/Quellenanker: TVöD Bund, BPersVG, KSchG. |
| `ausbildung-studium-bundeswehr-rueckforderung-ausbildungskosten` | Rückforderung Ausbildungskosten Bundeswehr: prüft § 56 SG, Zeitstaffelung, Verhältnismäßigkeit und Billigkeitserlass. Norm-/Quellenanker: § 56 SG, Art. 12 GG, BVerwG. |

## Arbeitsweg

Im Plugin Bundeswehrrecht Wehrrecht gilt für **Akteneinsicht WBO Arbeitsrecht Zivile**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `akteneinsicht-wbo-wdo`

**Fokus:** Akteneinsicht WBO und WDO: prüft Einsichtsrechte, Umfang, Verweigerungsgründe und Rechtsbehelfe. Norm-/Quellenanker: §§ 4–5 WBO, §§ 18–21 WDO, § 17 SG.

# Akteneinsicht nach WBO und WDO

## Fachkern: Akteneinsicht nach WBO und WDO
- **Spezialgegenstand:** Akteneinsicht nach WBO und WDO. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Das Akteneinsichtsrecht ist eine zentrale Verfahrensgarantie im Wehr- und Disziplinarrecht. Im WBO-Beschwerdeverfahren sichert § 4 WBO das Recht, alle entscheidungsrelevanten Unterlagen einzusehen. Im WDO-gerichtlichen Disziplinarverfahren hat der Soldat umfassende Einsichtsrechte (ähnlich StPO).

Verweigerungsgründe sind eng: VS-Einstufung, laufende Drittermittlungen, Schutz unbeteiligter Personen. Eine pauschale Verweigerung ist rechtswidrig und mit WBO anfechtbar.

## Einschlägige Normen und Quellen

- § 4 WBO — Akteneinsicht im Beschwerdeverfahren
- § 5 WBO — Unterlagen und Beweismittel
- §§ 18–21 WDO — Akteneinsicht im Disziplinarverfahren
- § 17 SG — Personalaktenrecht Soldaten
- Art. 15 DSGVO — Auskunftsrecht
- § 56 SG — Disziplinaraktenrecht

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- In welchem Verfahren wird Akteneinsicht beantragt (WBO, WDO, Personalakte § 17 SG)?
- Wurde Einsicht bereits beantragt und (teilweise) verweigert?
- Welche Unterlagen werden konkret benötigt (Bescheide, Gutachten, Zeugenaussagen)?
- Liegt eine VS-Einstufung vor?
- Ist ein Verteidiger oder Bevollmächtigter bestellt?
- Welche Fristen laufen (WBO: 1 Monat)?

## Prüf- und Arbeitslogik

### Schritt 1 — Verfahrensart und Rechtsgrundlage

WBO § 4: Einsicht in Akten, die Gegenstand der Beschwerde sind.
WDO §§ 18–21: Verteidiger ab Einleitungsverfügung umfassendes Einsichtsrecht.
SG § 17: Soldat hat Recht auf vollständige Personalakte.
DSGVO Art. 15: Auskunft über personenbezogene Daten (ergänzend).

### Schritt 2 — Umfang der Einsicht

WBO: alle entscheidungsrelevanten Unterlagen.
WDO: Anklage, Untersuchungsergebnis, Beweismittel, Disziplinarakte.
§ 17 SG: vollständige Personalakte inkl. Beurteilungen, Verwarnungen, Vermerke.
Keine Einsicht: VS-Dokumente ohne Freigabe, Unterlagen zu anderen Verfahren.

### Schritt 3 — Verweigerungsgründe prüfen

Geheimschutz: nur VS-eingestufter Teil, nicht gesamte Akte.
Drittermittlungen: nur insoweit Einschränkung zulässig.
Schutz Dritter: Schwärzung personenbezogener Daten möglich.
Pauschale Verweigerung = rechtswidrig → WBO-Beschwerde.

### Schritt 4 — Rechtsbehelfe bei Verweigerung

WBO-Beschwerde gegen Aktenvorenthaltung als dienstliche Maßnahme.
Antrag gerichtliche Entscheidung § 17a WBO beim TDG.
WDO-Verfahren: Befangenheitsantrag gegen Untersuchungsführer.
DSGVO Art. 15: Auskunftsverlangen an BfDI oder DSB Bundeswehr.

### Schritt 5 — Praktische Umsetzung

Schriftlicher Antrag mit konkreter Nennung gewünschter Unterlagen.
Empfangsbestätigung verlangen.
Wichtig: WBO-Beschwerdefrist läuft weiter — kein Hemmungstatbestand durch Akteneinsichtsantrag!
Notfalls WBO-Beschwerde vorsorglich einlegen, Akteneinsicht parallel verfolgen.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Muster-Akteneinsichtsantrag (WBO / WDO / § 17 SG)
- Tabelle: Rechtsgrundlagen Akteneinsicht in verschiedenen Verfahren
- Checkliste: Unterlagen im Disziplinarverfahren einfordern

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/wbo/ — WBO
- https://www.gesetze-im-internet.de/wdo_2002/ — WDO
- https://www.gesetze-im-internet.de/sg/ — § 17 SG
- https://www.bverwg.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 2. `arbeitsrecht-zivile-bundeswehrbeschaeftigte`

**Fokus:** Arbeitsrecht zivile Bundeswehrbeschäftigte: prüft TVöD-Anwendung, Personalrat BPersVG, Kündigung, Versetzung und Rechtsweg. Norm-/Quellenanker: TVöD Bund, BPersVG, KSchG.

# Arbeitsrecht für zivile Bundeswehrbeschäftigte

## Fachkern: Arbeitsrecht für zivile Bundeswehrbeschäftigte
- **Spezialgegenstand:** Arbeitsrecht für zivile Bundeswehrbeschäftigte. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Die Bundeswehr beschäftigt neben Soldaten eine große Zahl ziviler Arbeitnehmerinnen und Arbeitnehmer. Deren Arbeitsverhältnisse richten sich nach TVöD Bund und allgemeinem Arbeitsrecht; Mitbestimmung durch Personalrat (BPersVG, nicht BetrVG).

Besonderheiten entstehen durch militärische Organisationsstruktur, häufige Versetzungen, Sicherheitsüberprüfungen (SÜG) als Beschäftigungsvoraussetzung und ggf. Auslandsverwendungen.

## Einschlägige Normen und Quellen

- TVöD Bund — Tarifvertrag öffentlicher Dienst Bund
- BPersVG — Bundespersonalvertretungsgesetz
- § 1 KSchG — Kündigungsschutz
- § 613a BGB — Betriebsübergang
- ArbGG — Arbeitsgerichtsgesetz
- NATO-Truppenstatut — bei ausländischen Truppen mit zivilem Personal
- SÜG — Sicherheitsüberprüfung als Beschäftigungsvoraussetzung

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Welcher Tarifvertrag gilt (TVöD Bund, TV-L, sonstiger)?
- Geht es um Kündigung, Versetzung, Abmahnung, Eingruppierung oder Sicherheitsüberprüfung?
- Hat der Personalrat zugestimmt, oder wurde seine Beteiligung unterlassen?
- Liegt ein Versetzungsfall unter NATO-Truppenstatut vor?
- Sind Fristen nach KSchG (3 Wochen) oder BPersVG abgelaufen?
- Besteht Sonderkündigungsschutz (Schwerbehinderung, Schwangerschaft, Personalrat)?

## Prüf- und Arbeitslogik

### Schritt 1 — Arbeitsverhältnis einordnen

TVöD Bund: Entgeltgruppen E1–E15.
Abgrenzung: Beamte der Bundeswehrverwaltung → BBG (anderer Rechtsweg!).
Befristung: TzBfG prüfen.
Leiharbeit: AÜG, höchstens 18 Monate.

### Schritt 2 — Personalratsbeteiligung BPersVG

Mitbestimmung bei Kündigung (§ 79 BPersVG), Versetzung (§ 76), Eingruppierung (§ 75).
Fehlende Beteiligung → Kündigung unwirksam!
Frist: Personalrat hat 10 Arbeitstage für Stellungnahme.
Einigungsstellenverfahren bei Blockade.

### Schritt 3 — Kündigung prüfen

KSchG ab 6 Monaten, Betrieb > 10 MA (hier: Dienststelle zählt).
Gründe: personenbedingt (Sicherheitsüberprüfung entzogen!), verhaltensbedingt, betriebsbedingt.
Sonderkündigungsschutz: SGB IX, MuSchG, BEEG, Personalrat-Mitglieder.
Klage ArbG: 3-Wochen-Frist.

### Schritt 4 — Versetzung und Direktionsrecht

§ 106 GewO Direktionsrecht, aber Grenzen TVöD und BPersVG.
Versetzung andere Dienststelle: Personalratsbeteiligung, ggf. Zustimmungsverweigerung.
Sicherheitsüberprüfung entzogen: Versetzung nicht-VS-Dienstposten oder Kündigung prüfen.

### Schritt 5 — Rechtsweg

Arbeitsgerichte (ArbG/LAG/BAG) für alle TVöD-Streitigkeiten.
NICHT Verwaltungsgericht!
Kündigungsschutzklage: 3-Wochen-Frist unbedingt wahren.
BPersVG-Streitigkeiten: VG möglich bei Statusfragen des Personalrats.

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Tabelle: Personalrat (BPersVG) vs. Betriebsrat (BetrVG) — Unterschiede in der Bundeswehr
- Checkliste: Kündigung ziviler Bundeswehrbeschäftigter — häufige Fehler
- Muster: Widerspruch gegen Versetzungsverfügung

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/tvod/ — TVöD
- https://www.gesetze-im-internet.de/bpersvg/ — BPersVG
- https://www.gesetze-im-internet.de/kschg/ — KSchG
- https://www.bundesarbeitsgericht.de

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?

## 3. `ausbildung-studium-bundeswehr-rueckforderung-ausbildungskosten`

**Fokus:** Rückforderung Ausbildungskosten Bundeswehr: prüft § 56 SG, Zeitstaffelung, Verhältnismäßigkeit und Billigkeitserlass. Norm-/Quellenanker: § 56 SG, Art. 12 GG, BVerwG.

# Ausbildung, Studium und Rückforderung von Ausbildungskosten

## Fachkern: Ausbildung, Studium und Rückforderung von Ausbildungskosten
- **Spezialgegenstand:** Ausbildung, Studium und Rückforderung von Ausbildungskosten. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** SG, WSG, WPflG, KDVG, WDO, SVG, BBesG, VwGO, truppendienstgerichtliche Zuständigkeiten und Grundrechte.
- **Entscheidende Weiche:** Status, Befehl/Dienstpflicht, Gewissen/KDV, Besoldung/Versorgung, Disziplinarweg, Eilrechtsschutz und Nachweisführung trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Fachlicher Kontext

Wer als Soldat auf Bundeswehrkosten studiert oder eine teure Ausbildung absolviert (Offizier, Pilot, Sanitätsoffizier, UniBw), geht eine Dienstzeitverpflichtung ein. Vorzeitige Entlassung löst Rückforderungsanspruch aus (§ 56 SG).

BVerfG und BVerwG betonen Verhältnismäßigkeit: Erstattung ist Vorteilsausgleich, keine Vertragsstrafe. Härteregelungen und Billigkeitserlass sind ausdrücklich vorgesehen.

## Einschlägige Normen und Quellen

- § 56 SG — Rückforderung Ausbildungskosten
- § 46 SG — Entlassung auf eigenen Antrag
- § 55 SG — Entlassung Soldat auf Zeit
- Art. 12 GG — Berufsfreiheit (Verhältnismäßigkeit)
- BVerwGE 95, 262 — Verhältnismäßigkeit Rückforderung
- SVG §§ 39–48 — Berufsförderungsdienst

## Einsatz

Dieser Abschnitt bearbeitet **Einschlägige Normen und Quellen** im Bereich **Bundeswehrrecht und Wehrrecht**. Er ordnet die konkrete Lage, sichere Tatsachen, offene Fragen, Risiken, Quellen und den nächsten verwertbaren Schritt.
sichtbar wird oder der Allgemein-Skill dorthin routet. Arbeite praktisch, schnell und
verwertbar: keine Vorlesung, sondern ein geordneter Arbeitsweg mit Ergebnis.

## Sachverhaltsaufnahme — Startfragen

- Wann wurde Ausbildung abgeschlossen, und welche Dienstzeitverpflichtung bestand?
- Wie lange hat der Soldat nach Ausbildungsende tatsächlich gedient?
- Welche Kosten macht die Bundeswehr geltend (Studium, Pilotenausbildung)?
- Liegt ein Rückforderungsbescheid vor?
- Warum wurde das Dienstverhältnis beendet (eigener Antrag, Gesundheit, Pflichtverletzung)?
- Wurde ein Härtefall oder Billigkeitserlass beantragt?

## Prüf- und Arbeitslogik

### Schritt 1 — Rückforderungsgrundlage § 56 SG

Tatbestand: Entlassung auf eigenen Antrag (§ 46 SG) oder nach § 55 Abs. 4 SG (Pflichtverletzung).
NICHT bei: krankheitsbedingter Entlassung § 55 Abs. 2 SG!
Kosten: tatsächlich entstandene Ausbildungskosten (Studium, Pilotenausbildung, Sold während Ausbildung).
Keine Rückforderung für allgemeine Grundausbildung.

### Schritt 2 — Zeitstaffelung und Berechnung

Rückforderungsbetrag vermindert sich linear pro abgeleistetes Dienstjahr nach Ausbildungsende.
Formel: Kosten × (verbleibende Verpflichtungszeit / Gesamtverpflichtungszeit).
Berechnung im Bescheid kontrollieren: Datum Ausbildungsende, Verpflichtungszeit, tatsächliche Dienstzeit.

### Schritt 3 — Verhältnismäßigkeit und Härte

Art. 12 GG: Rückforderung darf nicht prohibitiv auf Berufsfreiheit wirken.
BVerwG: Billigkeitserlass bei besonderer Härte (schwere Erkrankung, familiäre Ausnahmesituation, unzumutbare wirtschaftliche Belastung).
Ratenzahlungsvereinbarung und Stundungsantrag möglich.

### Schritt 4 — Entlassungsgrund ist entscheidend

Eigener Antrag § 46 SG → voller Rückforderungsanspruch.
Entlassung § 55 Abs. 4 Pflichtverletzung → Rückforderung möglich.
Gesundheit § 55 Abs. 2 → KEINE Rückforderung!
Elternzeit/Pflegezeit → BVerwG: eingeschränkte Rückforderung.

### Schritt 5 — Rechtsbehelfe

Widerspruch gegen Rückforderungsbescheid: 1 Monat.
Aufschiebende Wirkung beantragen (§ 80 VwGO).
Klage VG: sachlich zuständig.
Parallel: Billigkeitserlass beantragen (eigenständiger Verwaltungsakt).

## Arbeitsergebnisse

Erzeuge je nach Auftrag eines oder mehrere dieser Ergebnisse:

- Kurzvermerk mit Risikoampel (grün/gelb/rot)
- Prüfschema mit Tatbestandselementen und offenen Punkten
- Fragenliste für Mandanten/Sachverhaltsgespräch
- Entwurfsbausteine (Beschwerde, Antrag, Schriftsatz, Stellungnahme)
- Dokumentenanforderungsliste
- Nächster Schritt mit konkreter Frist

- Berechnungsschema: Rückforderungsbetrag nach § 56 SG
- Tabelle: Typische Ausbildungen, Verpflichtungszeiten und Kostengrößenordnungen
- Muster-Widerspruch gegen Rückforderungsbescheid
- Checkliste: Härtegründe für Billigkeitserlass

## Quellenhygiene

- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle nennen
 (openjur.de, bverwg.de, bverfg.de, bgh.de).
- Normtexte über gesetze-im-internet.de oder dejure.org live prüfen.
- Bei Behördenverfahren: aktuelle Formulare und Merkblätter der Bundeswehr / BAPersBw prüfen.

**Primärquellen:**

- https://www.gesetze-im-internet.de/sg/ — § 56 SG
- https://www.bverwg.de — BVerwG Wehrdienstsenat
- https://openjur.de — TDG-Entscheidungen
- https://dejure.org/gesetze/SG/56.html

## Qualitätsgate

Vor Ausgabe prüfen:

- Fristen, Zuständigkeit und Rechtsgrundlage vollständig?
- Offene Tatsachen als `[offen: ...]` markiert?
- Gegenargumente und Verteidigungslinien formuliert?
- Beweislastverteilung geklärt?
- Output entspricht dem gewünschten Arbeitsergebnis?
