---
name: richteranklage-art-richterbeurteilung
description: "Richteranklage ART Richterbeurteilung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Richteranklage ART Richterbeurteilung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Richteranklage ART Richterbeurteilung** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `richteranklage-art-98-gg` | Skill zur Richteranklage nach Art. 98 Abs. 2 und Abs. 5 GG i.V.m. den landesrechtlichen Vorschriften. Klaert die Voraussetzungen fuer ein Verfahren beim Bundesverfassungsgericht gegen einen Bundesrichter den verfassungsrechtlichen Tatbestand der Amtsverletzung das Antragsverfahren auf Versetzung in den Ruhestand oder Entlassung und das Verhaeltnis zur disziplinarrechtlichen Sanktion. Behandelt die Konstellationen Verstoesse gegen die richterliche Unabhaengigkeit politische Aeusserungen und schwerwiegende Pflichtverstoesse. Liefert Pruefraster. |
| `richterbeurteilung-praesidialrat` | Richterbeurteilung, Präsidialrat, Richterwahlausschuss und Beteiligung vor Ernennung. |
| `richterdienst-drig-grundlagen` | Richterdienst nach DRiG: Rechtsformen, Voraussetzungen, Richter auf Probe, Lebenszeit und Unvereinbarkeiten. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Richteranklage ART Richterbeurteilung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `richteranklage-art-98-gg`

**Fokus:** Skill zur Richteranklage nach Art. 98 Abs. 2 und Abs. 5 GG i.V.m. den landesrechtlichen Vorschriften. Klaert die Voraussetzungen fuer ein Verfahren beim Bundesverfassungsgericht gegen einen Bundesrichter den verfassungsrechtlichen Tatbestand der Amtsverletzung das Antragsverfahren auf Versetzung in den Ruhestand oder Entlassung und das Verhaeltnis zur disziplinarrechtlichen Sanktion. Behandelt die Konstellationen Verstoesse gegen die richterliche Unabhaengigkeit politische Aeusserungen und schwerwiegende Pflichtverstoesse. Liefert Pruefraster.


# Richteranklage Art. 98 GG

## 1. Zweck und Anwendungsfall

Skill zur Pruefung der Voraussetzungen einer Richteranklage. Anwendung sehr selten, aber relevant fuer Verfahrensbeteiligte, die einen Bundesrichter wegen schwerwiegender Pflichtverstoesse aus dem Amt entfernt sehen wollen, oder fuer den betroffenen Richter zur Verteidigung.

## 2. Eingaben

- Beschwerdegegenstand (konkretes Verhalten)
- Statusamt des Betroffenen (Bundesrichter oder Landesrichter)
- Stand der disziplinarrechtlichen Vorgaenge
- Antrag des Bundestags oder der Landesregierung

## 3. Ablauf / Checkliste

### a) Tatbestand
- Art. 98 Abs. 2 GG: Wenn ein Bundesrichter im Amt oder ausser Amts gegen die Grundsaetze des Grundgesetzes oder gegen die verfassungsmaessige Ordnung verstoesst, kann das Bundesverfassungsgericht auf Antrag des Bundestages mit Zweidrittelmehrheit anordnen, dass der Richter in ein anderes Amt versetzt oder in den Ruhestand zu versetzen ist. Bei vorsaetzlichem Verstoss Entlassung.

### b) Anwendung auf Landesrichter
- Art. 98 Abs. 5 GG ermoeglicht analoge Vorschriften in den Laendern; landesrechtliche Vorschriften unterschiedlich.

### c) Antragsverfahren
- Antrag durch den Bundestag (Bundesrichter).
- Verfahren vor dem BVerfG (Senatsentscheidung).

### d) Bewertung
- Die Hoehe der Schwelle ist hoch; in der Praxis selten erfuellt. Disziplinarmassnahmen treten daneben.

### e) Verteidigung
- Geltendmachung der Garantie der richterlichen Unabhaengigkeit Art. 97 GG.
- Pruefung des Tatbestands der Amtsverletzung.

## 4. Quellenpflicht

- Normen: Art. 97, 98 GG; §§ 13 Nr. 9, 58 ff. BVerfGG; Landesrichtergesetze.
- Rspr.: BVerfG zu Richteranklage — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle; sehr seltene Verfahren.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Pruefraster Tatbestand und Verfahrensgang.
- Verteidigungs-Memo bei drohender Anklage.

## 6. Verifizierte Quellenanker

- Art. 97 GG, Art. 98 GG, Art. 101 GG, § 21e GVG sowie DRiG §§ 25, 26, 39, 61 ff. als Kernnormen.
- BVerfG, 20.09.2016 - 2 BvR 2453/15: Bundesrichterwahl, Art. 95 Abs. 2 GG und Bindung an Art. 33 Abs. 2 GG.
- BVerfG, 11.11.2021 - 2 BvR 1473/20: Dienstaufsicht, Erledigungsdruck und Grenze bei objektiv nicht bewältigbarem Pensum.
- BVerfG, 22.03.2018 - 2 BvR 780/16: Richter auf Zeit und richterliche Unabhängigkeit im organisationsrechtlichen Kontext.
- EuGH, 24.06.2019 - C-619/18 und EuGH, 19.11.2019 - C-585/18, C-624/18, C-625/18 als EU-rechtliche Anker der Justizunabhängigkeit.
- Landesrichterrecht, Dienstgerichte der Länder und Präsidialratsrecht immer landesrechtlich live prüfen.

## 7. Beispiel (Kurzfassung)

Hypothetisch: Bundesrichter aeussert sich oeffentlich gegen die Geltung des Grundgesetzes. Skill liefert Pruefraster der Voraussetzungen einer Richteranklage und der parallelen disziplinarrechtlichen Schritte.

## 2. `richterbeurteilung-praesidialrat`

**Fokus:** Richterbeurteilung, Präsidialrat, Richterwahlausschuss und Beteiligung vor Ernennung.


# Richterbeurteilung Praesidialrat

## Aufgabe

Richterbeurteilung, Präsidialrat, Richterwahlausschuss und Beteiligung vor Ernennung.

## Arbeitsweise

Prüfe Beurteilung, Präsidialratsbeteiligung nach DRiG/Landesrecht, Auswahlvermerk und Rechtsschutz. Beachte richterliche Besonderheiten.

## Pflichtfragen

- Welcher Status liegt vor: Beamter, Richter, Bewerber, Anwärter, Tarifbeschäftigter, Wahlbeamter oder Mischfall?
- Welcher Dienstherr und welches Bundesland sind betroffen?
- Gibt es einen Bescheid, eine Beurteilung, eine Ausschreibung, einen Auswahlvermerk oder eine Verfügung mit Datum und Zugang?
- Welche Frist läuft und welches Ergebnis soll erreicht werden?
- Welche Unterlagen fehlen noch: Personalakte, Beurteilungsbeiträge, amtsärztliches Gutachten, Berechnungsblatt, Beteiligungsvermerk?

## Prüfprogramm

1. **Status und Rechtsquelle:** Bundesrecht, Landesrecht oder Richterrecht trennen; Normen live gegen amtliche Quellen prüfen.
2. **Eingriff und Ziel:** Verwaltungsakt, dienstliche Weisung, Auswahlentscheidung, Realakt oder bloße Kommunikation einordnen.
3. **Materielle Prüfung:** Tatbestand, Ermessen, Beteiligung, Begründung, Gleichbehandlung, Fürsorge und Verhältnismäßigkeit prüfen.
4. **Verfahren:** Anhörung, Akteneinsicht, Frist, Widerspruch, Klageart, Eilrechtsschutz und Glaubhaftmachung klären.
5. **Output:** Eine klare Handlungsempfehlung, einen Entwurf oder eine Risikomatrix erzeugen.

## Ausgabeformat

- Kurzantwort in drei Sätzen.
- Checkliste der fehlenden Tatsachen.
- Rechtliche Einordnung mit passenden Normgruppen.
- Nächste Schritte mit Fristen und Anlagen.
- Quellenhygiene: keine nicht überprüfbaren Fundstellen, keine Kommentar- oder Aufsatzblindzitate.

## 3. `richterdienst-drig-grundlagen`

**Fokus:** Richterdienst nach DRiG: Rechtsformen, Voraussetzungen, Richter auf Probe, Lebenszeit und Unvereinbarkeiten.


# Richterdienst Drig Grundlagen

## Aufgabe

Richterdienst nach DRiG: Rechtsformen, Voraussetzungen, Richter auf Probe, Lebenszeit und Unvereinbarkeiten.

## Arbeitsweise

Prüfe DRiG §§ 1 ff., Status, Probezeit, Lebenszeit, Deutscher im Sinne Art. 116 GG, Befähigung zum Richteramt und soziale Kompetenz.

## Pflichtfragen

- Welcher Status liegt vor: Beamter, Richter, Bewerber, Anwärter, Tarifbeschäftigter, Wahlbeamter oder Mischfall?
- Welcher Dienstherr und welches Bundesland sind betroffen?
- Gibt es einen Bescheid, eine Beurteilung, eine Ausschreibung, einen Auswahlvermerk oder eine Verfügung mit Datum und Zugang?
- Welche Frist läuft und welches Ergebnis soll erreicht werden?
- Welche Unterlagen fehlen noch: Personalakte, Beurteilungsbeiträge, amtsärztliches Gutachten, Berechnungsblatt, Beteiligungsvermerk?

## Prüfprogramm

1. **Status und Rechtsquelle:** Bundesrecht, Landesrecht oder Richterrecht trennen; Normen live gegen amtliche Quellen prüfen.
2. **Eingriff und Ziel:** Verwaltungsakt, dienstliche Weisung, Auswahlentscheidung, Realakt oder bloße Kommunikation einordnen.
3. **Materielle Prüfung:** Tatbestand, Ermessen, Beteiligung, Begründung, Gleichbehandlung, Fürsorge und Verhältnismäßigkeit prüfen.
4. **Verfahren:** Anhörung, Akteneinsicht, Frist, Widerspruch, Klageart, Eilrechtsschutz und Glaubhaftmachung klären.
5. **Output:** Eine klare Handlungsempfehlung, einen Entwurf oder eine Risikomatrix erzeugen.

## Ausgabeformat

- Kurzantwort in drei Sätzen.
- Checkliste der fehlenden Tatsachen.
- Rechtliche Einordnung mit passenden Normgruppen.
- Nächste Schritte mit Fristen und Anlagen.
- Quellenhygiene: keine nicht überprüfbaren Fundstellen, keine Kommentar- oder Aufsatzblindzitate.
