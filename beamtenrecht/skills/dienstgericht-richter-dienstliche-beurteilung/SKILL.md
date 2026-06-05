---
name: dienstgericht-richter-dienstliche-beurteilung
description: "Dienstgericht Richter Dienstliche Beurteilung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Dienstgericht Richter Dienstliche Beurteilung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Dienstgericht Richter Dienstliche Beurteilung** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dienstgericht-richter-disziplinar-63-drig` | Skill zum Dienstgericht fuer Richter nach §§ 61 ff. DRiG und den Landesrichtergesetzen. Klaert die Zustaendigkeit des Dienstgerichts in Statussachen Disziplinarsachen und Versetzungs- und Pruefverfahren die Besetzung des Spruchkoerpers mit beruflichen und ehrenamtlichen Richtern und das Verfahrensrecht in Anlehnung an das BDG. Behandelt die Konstellationen Verfahren gegen Disziplinarmassnahmen Pruefung der richterlichen Unabhaengigkeit nach § 26 DRiG und Antrag auf Aufhebung der Geschaeftsverteilung. Liefert Pruefraster und Schriftsatzbausteine. |
| `dienstliche-beurteilung-angriff` | Dienstliche Beurteilung angreifen: Beurteilungsmaßstab, Beurteilerzuständigkeit, Beiträge, Plausibilität, Quoten und Nachzeichnung. |
| `dienstpflichten-treue-maessigung-neutralitaet` | Dienstpflichten: Treuepflicht, Mäßigung, Neutralität, Wahrheitspflicht, Amtsverschwiegenheit und Social Media. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Dienstgericht Richter Dienstliche Beurteilung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dienstgericht-richter-disziplinar-63-drig`

**Fokus:** Skill zum Dienstgericht fuer Richter nach §§ 61 ff. DRiG und den Landesrichtergesetzen. Klaert die Zustaendigkeit des Dienstgerichts in Statussachen Disziplinarsachen und Versetzungs- und Pruefverfahren die Besetzung des Spruchkoerpers mit beruflichen und ehrenamtlichen Richtern und das Verfahrensrecht in Anlehnung an das BDG. Behandelt die Konstellationen Verfahren gegen Disziplinarmassnahmen Pruefung der richterlichen Unabhaengigkeit nach § 26 DRiG und Antrag auf Aufhebung der Geschaeftsverteilung. Liefert Pruefraster und Schriftsatzbausteine.


# Dienstgericht fuer Richter

## 1. Zweck und Anwendungsfall

Skill fuer Richter, die ein Verfahren beim Dienstgericht fuehren oder verteidigen wollen. Anwendung typisch bei Disziplinarsachen, Pruefverfahren wegen Eingriffen in die richterliche Unabhaengigkeit (§ 26 DRiG) oder Streit um die Geschaeftsverteilung.

## 2. Eingaben

- Beanstandeter Vorgang (Disziplinarverfuegung, Massnahme der Dienstaufsicht, Geschaeftsverteilungsbeschluss)
- Statusamt (Bundes- oder Landesrichter)
- Spruchkoerper-Besetzung
- Antrag im Detail

## 3. Ablauf / Checkliste

### a) Zustaendigkeit
- § 62 DRiG: Dienstgericht des Bundes fuer Bundesrichter, Dienstgerichte der Laender fuer Landesrichter.
- § 78 DRiG: Disziplinarsachen, Statussachen, Pruefung nach § 26 DRiG.

### b) Besetzung
- Dienstgericht: Drei Berufsrichter, zwei ehrenamtliche Richter (in Disziplinarsachen) bzw. spezifische Besetzung in Statussachen.

### c) Pruefung nach § 26 DRiG
- Pruefung von Massnahmen der Dienstaufsicht, ob die richterliche Unabhaengigkeit beruehrt wird; Pruefraster: Massnahme, Beruehrung der Unabhaengigkeit, Folgen.
- Antrag auf Pruefung in Frist (regelmaessig 3 Monate nach Massnahme).

### d) Disziplinarverfahren
- Verfahren nach BDG in Anlehnung; spezifische Besonderheiten in DRiG und Landesrichtergesetzen.

### e) Geschaeftsverteilung
- Antrag auf Pruefung der Geschaeftsverteilung beim Dienstgericht — siehe Schwester-Skill `geschaeftsverteilung-richter-21e-gvg`.

## 4. Quellenpflicht

- Normen: §§ 26, 61 bis 78 DRiG; Landesrichtergesetze; BDG (entsprechend).
- Rspr.: BGH zum Dienstgericht des Bundes; OLG-Dienstgerichte der Laender — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Antrag an das Dienstgericht.
- Pruefraster nach § 26 DRiG.

## 6. Verifizierte Quellenanker

- Art. 97 GG, Art. 98 GG, Art. 101 GG, § 21e GVG sowie DRiG §§ 25, 26, 39, 61 ff. als Kernnormen.
- BVerfG, 20.09.2016 - 2 BvR 2453/15: Bundesrichterwahl, Art. 95 Abs. 2 GG und Bindung an Art. 33 Abs. 2 GG.
- BVerfG, 11.11.2021 - 2 BvR 1473/20: Dienstaufsicht, Erledigungsdruck und Grenze bei objektiv nicht bewältigbarem Pensum.
- BVerfG, 22.03.2018 - 2 BvR 780/16: Richter auf Zeit und richterliche Unabhängigkeit im organisationsrechtlichen Kontext.
- EuGH, 24.06.2019 - C-619/18 und EuGH, 19.11.2019 - C-585/18, C-624/18, C-625/18 als EU-rechtliche Anker der Justizunabhängigkeit.
- Landesrichterrecht, Dienstgerichte der Länder und Präsidialratsrecht immer landesrechtlich live prüfen.

## 7. Beispiel (Kurzfassung)

Mandant Vorsitzender Richter, Praesidium hat ihm anhaengiges Verfahren entzogen mit Hinweis auf Belastungssituation. Skill liefert Pruefung nach § 26 DRiG und Antrag beim Dienstgericht.

## 2. `dienstliche-beurteilung-angriff`

**Fokus:** Dienstliche Beurteilung angreifen: Beurteilungsmaßstab, Beurteilerzuständigkeit, Beiträge, Plausibilität, Quoten und Nachzeichnung.


# Dienstliche Beurteilung Angriff

## Aufgabe

Dienstliche Beurteilung angreifen: Beurteilungsmaßstab, Beurteilerzuständigkeit, Beiträge, Plausibilität, Quoten und Nachzeichnung.

## Arbeitsweise

Prüfe Eröffnung, Einwendungen, Beurteilungsbeiträge, Gesamturteil, Plausibilisierung und Vergleichsgruppe. Formuliere Einwendungsschreiben.

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

## 3. `dienstpflichten-treue-maessigung-neutralitaet`

**Fokus:** Dienstpflichten: Treuepflicht, Mäßigung, Neutralität, Wahrheitspflicht, Amtsverschwiegenheit und Social Media.


# Dienstpflichten Treue Maessigung Neutralitaet

## Aufgabe

Dienstpflichten: Treuepflicht, Mäßigung, Neutralität, Wahrheitspflicht, Amtsverschwiegenheit und Social Media.

## Arbeitsweise

Ordne Verhalten nach Dienstbezug, Öffentlichkeit, Amt, Funktionsnähe und Grundrechtsbezug. Formuliere risikobewusste Beratung ohne pauschale Einschüchterung.

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
