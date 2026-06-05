---
name: familienzuschlag-drittes-kinder
description: "Familienzuschlag Drittes Kinder: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Familienzuschlag Drittes Kinder

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Familienzuschlag Drittes Kinder** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `familienzuschlag-drittes-kind-bverfg` | Skill zum verfassungsrechtlichen Mindeststandard des Familienzuschlags fuer das dritte und jedes weitere Kind nach Art. 33 Abs. 5 GG. Klaert das BVerfG-Pruefschema fuer den Mehrkinderzuschlag mit Vergleich zur sozialhilferechtlichen Bedarfsdeckung und zum kinderbezogenen Existenzminimum. Behandelt die Konstellation alleinverdienender Beamter mit drei und mehr unterhaltsberechtigten Kindern. Liefert Widerspruch und Berechnungsmodell zur Geltendmachung der Differenz zwischen tatsaechlichem und verfassungsrechtlich gebotenem Mehrkinderzuschlag. |
| `familienzuschlag-kinder-und-rueckforderung` | Familienzuschlag, Kinderanteile, Konkurrenzen, Teilzeit, Trennung, Rückforderung und Mitteilungspflichten. |
| `foederalismusreform-kompetenzmatrix-beamtenrecht` | Kompetenzmatrix seit der Föderalismusreform 2006: Bund, Länder, Art. 70/73/74 Abs. 1 Nr. 27, Art. 125a GG, BeamtStG, BBG, Besoldung, Versorgung, Laufbahn und Richterrecht sauber trennen. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Familienzuschlag Drittes Kinder**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `familienzuschlag-drittes-kind-bverfg`

**Fokus:** Skill zum verfassungsrechtlichen Mindeststandard des Familienzuschlags fuer das dritte und jedes weitere Kind nach Art. 33 Abs. 5 GG. Klaert das BVerfG-Pruefschema fuer den Mehrkinderzuschlag mit Vergleich zur sozialhilferechtlichen Bedarfsdeckung und zum kinderbezogenen Existenzminimum. Behandelt die Konstellation alleinverdienender Beamter mit drei und mehr unterhaltsberechtigten Kindern. Liefert Widerspruch und Berechnungsmodell zur Geltendmachung der Differenz zwischen tatsaechlichem und verfassungsrechtlich gebotenem Mehrkinderzuschlag.


# Familienzuschlag dritte und weitere Kinder — verfassungsrechtliches Minimum

## 1. Zweck und Anwendungsfall

Skill fuer Beamte und Richter mit drei oder mehr unterhaltsberechtigten Kindern, die geltend machen, dass der Familienzuschlag und das Kindergeld die kindbezogenen Mehrbedarfe nicht in der vom BVerfG geforderten Hoehe abdecken.

## 2. Eingaben

- Besoldungsgruppe, Stufe, Stand der Bezuegemitteilung
- Anzahl der Kinder und Geburtsdaten
- Kindergeld bezogen ja/nein
- Wohnsitz (Bundesland)
- Datum der zeitnahen Geltendmachung

## 3. Ablauf / Checkliste

### a) BVerfG-Massstab
- Der Mehrkinderzuschlag muss die kindbezogenen Mehrbedarfe so abdecken, dass jedes Mehrkind nicht zur Belastung der Familie wird, die das amtsangemessene Lebenshaltungsniveau gefaehrden wuerde. Vergleich erfolgt mit dem sozialhilferechtlichen Mindestbedarf eines Kindes (Regelbedarf, anteilige Unterkunft, Bildungs- und Teilhabepaket, anteiliges Heizen).

### b) Berechnungsmodell
- Berechnung des sozialhilferechtlich notwendigen Bedarfs eines dritten Kindes pro Monat.
- Vergleich mit Familienzuschlag plus Kindergeld minus steuerliche Belastung der zusaetzlichen Bezuege.
- Differenz = verfassungsrechtlich gebotene Mindestnachforderung.

### c) Zeitnahe Geltendmachung
- Widerspruch im laufenden Haushaltsjahr ist Bedingung. Vorjahresanspruechen droht der Verfall.

### d) Verfahrenslage
- Widerspruch -> Bescheid -> Klage VG -> Aussetzung und Vorlage Art. 100 Abs. 1 GG.

## 4. Quellenpflicht

- Normen: Art. 33 Abs. 5 GG; §§ 39, 40 BBesG; landesrechtliche Aequivalente; SGB II / SGB XII (Bedarfsberechnung).
- Rspr.: BVerfG zur Familienzuschlagsproblematik — Quellenanker unten; konkrete Entscheidung in amtlicher oder freier Quelle prüfen.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Widerspruchsschrift mit konkreten Bedarfszahlen.
- Tabelle "Kindbezogener Bedarf — Bezuge — Differenz".

## 6. Verifizierte Quellenanker

- BVerfG, 05.05.2015 - 2 BvL 17/09 u.a.: R-Besoldung Sachsen-Anhalt; Parameterprüfung zur amtsangemessenen Alimentation.
- BVerfG, 04.05.2020 - 2 BvL 4/18: R-Besoldung Berlin; Mindestabstand und Alimentation.
- BVerfG, 04.05.2020 - 2 BvL 6/17 u.a.: kinderreiche Richterfamilien und Familienzuschlag.
- BVerfG, 17.09.2025 - 2 BvL 20/17 u.a.: Berliner A-Besoldung; Prekaritätsschwelle und Dreischritt.
- Seit der Föderalismusreform 2006 ist Landesbesoldung landesrechtlich zu prüfen; BBesG nur für Bund/Soldaten und fortgeltende Sonderlagen.
- Für Stufen, Auslandsdienstbezüge, Erschwerniszulagen und Mehrarbeit zusätzlich aktuelle Spezialnormen live prüfen; die BVerfG-Linie ersetzt keine Fachnormprüfung.

## 7. Beispiel (Kurzfassung)

Justizvollzugshauptsekretaer A8 Stufe 6, drei Kinder in einer Bedarfsgemeinschaft. Skill liefert Bedarfsberechnung und Widerspruchsentwurf wegen unzureichender Mehrkinderzuschlaege.

## 2. `familienzuschlag-kinder-und-rueckforderung`

**Fokus:** Familienzuschlag, Kinderanteile, Konkurrenzen, Teilzeit, Trennung, Rückforderung und Mitteilungspflichten.


# Familienzuschlag Kinder Und Rueckforderung

## Aufgabe

Familienzuschlag, Kinderanteile, Konkurrenzen, Teilzeit, Trennung, Rückforderung und Mitteilungspflichten.

## Arbeitsweise

Erhebe Familienstand, Kindergeld, andere beihilfeberechtigte Person, Dienstherr des Partners und Änderungsdatum.

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

## 3. `foederalismusreform-kompetenzmatrix-beamtenrecht`

**Fokus:** Kompetenzmatrix seit der Föderalismusreform 2006: Bund, Länder, Art. 70/73/74 Abs. 1 Nr. 27, Art. 125a GG, BeamtStG, BBG, Besoldung, Versorgung, Laufbahn und Richterrecht sauber trennen.


# Föderalismusreform - Kompetenzmatrix Beamtenrecht

## Problem

Beamtenrecht wirkt einheitlich, ist es aber nicht. Seit der Föderalismusreform 2006 sind Status, Laufbahn, Besoldung und Versorgung auf Bund und Länder unterschiedlich verteilt. Dieser Skill verhindert den Standardfehler, Bundesrecht auf Landesbeamte oder ein Landesbesoldungsgesetz auf Bundesbeamte anzuwenden.

## Matrix

| Bereich | Bundesbeamte | Landesbeamte / Kommunalbeamte | Richter |
| --- | --- | --- | --- |
| Statusrechte | BBG | BeamtStG plus Landesbeamtengesetz | DRiG, Landesrichtergesetz, BeamtStG-Verweise |
| Laufbahn | Bundeslaufbahnrecht | Landeslaufbahnrecht | DRiG, Landesrichterrecht, Laufbahnelemente landesrechtlich |
| Besoldung | BBesG | Landesbesoldungsgesetz | Bund/Land je nach Gericht und Dienstherr |
| Versorgung | BeamtVG | Landesversorgungsgesetz | Bund/Land je nach Status |
| Disziplinarrecht | BDG | Landesdisziplinargesetz | Richterdienstrecht plus Disziplinarrecht, abhängig von Gericht und Status |

## Verfassungsanker

- Art. 73 Abs. 1 Nr. 8 GG: Rechtsverhältnisse der Bundesbediensteten.
- Art. 74 Abs. 1 Nr. 27 GG: Statusrechte und -pflichten der Landesbeamten, Richter in den Ländern eingeschlossen, mit Ausnahmen für Laufbahn, Besoldung und Versorgung.
- Art. 70 GG: Länderkompetenz, soweit keine Bundeskompetenz.
- Art. 125a GG: Fortgeltung alter Bundesregelungen, bis sie ersetzt werden.
- Art. 33 Abs. 2 und 5 GG: bundesweite verfassungsrechtliche Leitplanken.

## Arbeitsablauf

1. Dienstherr und Status feststellen.
2. Betroffene Materie auswählen: Status, Laufbahn, Besoldung, Versorgung, Disziplinar, Beihilfe, Richterdienst.
3. Kompetenzquelle benennen.
4. Normportal auswählen: gesetze-im-internet.de oder amtliches Landesportal.
5. Nur dann konkrete Norm zitieren.

## Typische Fehler

- BeamtStG als vollständiges Beamtenrecht missverstehen.
- § 17 BeamtStG als allgemeine Laufbahnwechselnorm verwenden; die Norm betrifft Umstrukturierungsfälle, nicht jeden freiwilligen Wechsel.
- BBesG für Landesbeamte nach 2006 ungeprüft verwenden.
- Landesrichter mit Bundesrichtern gleichsetzen.
- Kommunalbeamte ohne Landeskommunalrecht prüfen.

## Output

Der Skill liefert eine kurze „Rechtsquellenlandkarte" mit Trefferquote:

- sicher einschlägige Normen;
- noch live zu prüfende Landesnormen;
- falsche Normen, die ausdrücklich ausgeschlossen werden;
- nächster Fachmodul.
