---
name: personalakte-einsicht-pflege-beihilfe
description: "Personalakte Einsicht Pflege Beihilfe: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Personalakte Einsicht Pflege Beihilfe

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Personalakte Einsicht Pflege Beihilfe** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `personalakte-einsicht-datenschutz` | Personalakte, Einsicht, Datenschutz, Berichtigung und Entfernung belastender Unterlagen. |
| `pflege-beihilfe-pflegeversicherung-beamte` | Pflege im Beamtenrecht: Beihilfe, private oder soziale Pflegeversicherung, Pflegegrad, stationäre Pflege, Angehörige und Eigenanteile. |
| `plausibilisierung-gleicher-gesamtnoten` | Skill zur rechtlich sauberen Aufloesung von Notengleichstand bei der beamtenrechtlichen Auswahlentscheidung. Klaert die Stufenfolge ausschoepfender Beurteilungswert Binnendifferenzierung Einzelmerkmale Reihenfolge und Gewichtung sowie das Recht zum Rueckgriff auf Vorbeurteilung Hilfskriterien und Auswahlgespraech. Liefert Pruefraster und Schriftsatzbausteine zur Anfechtung der Auswahlentscheidung wenn der Auswahlvermerk diese Stufenfolge nicht oder nicht nachvollziehbar abarbeitet. |
| `politische-maessigung-60-bbg` | Skill zur politischen Maessigungspflicht nach § 60 BBG bzw. § 33 BeamtStG. Klaert die Pflicht zur Maessigung und Zurueckhaltung im politischen Bereich die Reichweite bei privater Aeusserung in sozialen Medien die Grenze zur Verfassungstreue und das Verhaeltnis zur Meinungs- und Wissenschaftsfreiheit. Behandelt typische Konstellationen Twitter-Aeusserung kommunalpolitisches Engagement Lehrerinnen und Lehrer in der Klassendiskussion sowie Wahlkampfauftritte. Liefert Pruefraster und Verteidigungsbausteine. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Personalakte Einsicht Pflege Beihilfe**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `personalakte-einsicht-datenschutz`

**Fokus:** Personalakte, Einsicht, Datenschutz, Berichtigung und Entfernung belastender Unterlagen.


# Personalakte Einsicht Datenschutz

## Aufgabe

Personalakte, Einsicht, Datenschutz, Berichtigung und Entfernung belastender Unterlagen.

## Arbeitsweise

Prüfe Aktenbestandteile, Einsichtsrecht, Bevollmächtigte, Kopien, Löschung/Berichtigung und DSGVO-Schnittstellen. Output: Akteneinsichtsantrag.

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

## 2. `pflege-beihilfe-pflegeversicherung-beamte`

**Fokus:** Pflege im Beamtenrecht: Beihilfe, private oder soziale Pflegeversicherung, Pflegegrad, stationäre Pflege, Angehörige und Eigenanteile.


# pflege-beihilfe-pflegeversicherung-beamte

## Aufgabe

Ordnet Pflegekosten bei Beamten und Pensionären ohne GKV-SGB-XI-Scheuklappen.

## Pflichtfragen

- Bund oder welches Bundesland, welcher Dienstherr und welcher Status: Beamter, Richter, Versorgungsempfänger, Bewerber oder Ruhestandsfall?
- Welcher Bescheid, welche Verfügung, welche Auswahlmitteilung, welche Versorgungsauskunft oder welcher Beihilfebescheid liegt vor?
- Datum, Zugang, Frist, Rechtsbehelf und gewünschtes Ziel?
- Welche Aktenbestandteile fehlen: Personalakte, Auswahlvermerk, Beurteilungen, Berechnungsblatt, amtsärztliches Gutachten, Beihilfeakte, PKV-Schreiben?

## Prüfprogramm

1. **Rechtsquelle trennen:** Bundesrecht, Landesrecht, Richterrecht und Satzungs-/Versorgungsrecht sauber auseinanderhalten.
2. **Eilbedürftigkeit prüfen:** Konkurrentenschutz, Widerspruchsfrist, Klagefrist, Beihilfefrist, Dienstunfallmeldung oder Ruhestandsdatum sichern.
3. **Materiellen Kern prüfen:** Art. 33 Abs. 2 oder Abs. 5 GG, BeamtVG, BBhV/landesrechtliche Beihilfe, BBesG/Landesbesoldung, BeamtStG/BBG und VwGO.
4. **Akte auswerten:** Nicht nur Normen, sondern Dokumentation, Ermessen, Beteiligung, Begründung, Plausibilität und Beweiswert bewerten.
5. **Output bauen:** Sofortmaßnahme, Antrag, Widerspruch, Eilantrag, Akteneinsicht, Mandantenbrief oder Berechnungsmatrix.

## Ausgabe

- Kurzbild mit Frist und Ziel.
- Prüfmatrix mit Normgruppe, Tatsachen, Unterlagen und Risiken.
- Konkreter nächster Schritt mit Entwurf oder Anlagenliste.

## Quellen-Hardening

Keine Rechtsprechung aus Modellwissen zitieren. Entscheidungen nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und amtlicher/frei prüfbarer Quelle. Landesrecht und Beihilferecht live prüfen.

## 3. `plausibilisierung-gleicher-gesamtnoten`

**Fokus:** Skill zur rechtlich sauberen Aufloesung von Notengleichstand bei der beamtenrechtlichen Auswahlentscheidung. Klaert die Stufenfolge ausschoepfender Beurteilungswert Binnendifferenzierung Einzelmerkmale Reihenfolge und Gewichtung sowie das Recht zum Rueckgriff auf Vorbeurteilung Hilfskriterien und Auswahlgespraech. Liefert Pruefraster und Schriftsatzbausteine zur Anfechtung der Auswahlentscheidung wenn der Auswahlvermerk diese Stufenfolge nicht oder nicht nachvollziehbar abarbeitet.


# Plausibilisierung gleicher Gesamtnoten

## 1. Zweck und Anwendungsfall

Skill fuer Konstellationen, in denen mehrere Bewerber dieselbe Gesamtnote in der dienstlichen Beurteilung erreichen. Die Auswahlentscheidung muss in diesem Fall in einer bestimmten Reihenfolge differenzieren; ein Auswahlvermerk, der diese Reihenfolge nicht abarbeitet, ist regelmaessig rechtswidrig.

## 2. Eingaben

- Beurteilung Mandant und Konkurrent mit Einzelmerkmalen
- Auswahlvermerk
- Hinweise zu Hilfskriterien (Vorbeurteilung, Schwerbehinderung, Frauenfoerderung, Auslandsverwendung)
- Stellenanforderungsprofil

## 3. Ablauf / Checkliste

### a) Stufenfolge der Differenzierung
1. Binnendifferenzierung der Gesamtnote durch ausschoepfende Wuerdigung des Beurteilungstextes (Spezifizierung der Note, Bewertungstendenz "oberer Bereich" oder "unterer Bereich").
2. Vergleich der Einzelmerkmale, insbesondere derjenigen, die fuer den konkret zu besetzenden Dienstposten relevant sind.
3. Vergleich auf der Grundlage der vorhergehenden Regelbeurteilungen ("Vorbeurteilungen").
4. Hilfskriterien (Schwerbehinderung, Frauenfoerderplan, Auslandsverwendung, Dienstalter).
5. Letztrangig Auswahlgespraech oder Assessment Center.

### b) Reihenfolge ist verbindlich
- Diese Reihenfolge ist nach staendiger Rechtsprechung des BVerwG einzuhalten; das Ueberspringen einzelner Stufen ist Verfahrensfehler.

### c) Auswahlvermerk
- Muss erkennbar machen, welche Stufen mit welchem Ergebnis abgearbeitet wurden.
- Bloss formelhafte Begruendung ("der Konkurrent ueberzeugte im Gespraech mehr") genuegt nicht.

### d) Gewichtung der Einzelmerkmale
- Die Auswahl muss aufzeigen, welche Einzelmerkmale fuer den konkreten Dienstposten besonders gewichtet wurden und warum.

## 4. Quellenpflicht

- Normen: Art. 33 Abs. 2 GG; § 9 BBG; §§ 22, 32 ff. BLV; einschlaegige Beurteilungsrichtlinien.
- Rspr.: BVerwG zur Stufenfolge der Differenzierung — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Tabellenraster: "Stufe — Inhalt — Auswahlvermerk Ja/Nein — Defizit".
- Schriftsatzbaustein "Anordnungsanspruch — Stufenfolgenverstoss".

## 6. Verifizierte Quellenanker

- Art. 33 Abs. 2 GG: Bestenauslese nach Eignung, Befähigung und fachlicher Leistung.
- Art. 74 Abs. 1 Nr. 27 GG und Art. 70 GG: Statusrechtliche Bundeskompetenz, Laufbahn/Besoldung/Versorgung der Länder grundsätzlich Landesrecht.
- BeamtStG und BBG immer nach Dienstherr trennen; Landesbeamtengesetz und Beurteilungsrichtlinien live prüfen.
- BVerwG, 11.10.2016 - 2 C 11.15 als verifizierter Anker zu Art. 33 Abs. 2 GG und Eignungsanforderungen bei Höchstaltersgrenzen.
- Für Spezialfragen der dienstlichen Beurteilung, Anlassbeurteilung, Binnendifferenzierung und Auswahlgespräch keine privaten Datenbankzitate verwenden; konkrete Rechtsprechung nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.

## 7. Beispiel (Kurzfassung)

Beide Bewerber Note "uebertrifft die Anforderungen". Auswahlvermerk: "Aufgrund des Auswahlgespraechs wurde Bewerberin B vorgezogen." Skill liefert Argument: Ueberspringen der Stufen Binnendifferenzierung Einzelmerkmale Vorbeurteilung; Auswahl rechtswidrig, Anordnungsanspruch begruendet.

## 4. `politische-maessigung-60-bbg`

**Fokus:** Skill zur politischen Maessigungspflicht nach § 60 BBG bzw. § 33 BeamtStG. Klaert die Pflicht zur Maessigung und Zurueckhaltung im politischen Bereich die Reichweite bei privater Aeusserung in sozialen Medien die Grenze zur Verfassungstreue und das Verhaeltnis zur Meinungs- und Wissenschaftsfreiheit. Behandelt typische Konstellationen Twitter-Aeusserung kommunalpolitisches Engagement Lehrerinnen und Lehrer in der Klassendiskussion sowie Wahlkampfauftritte. Liefert Pruefraster und Verteidigungsbausteine.


# Politische Maessigungspflicht § 60 BBG

## 1. Zweck und Anwendungsfall

Skill fuer Beamte, denen die Verletzung der Maessigungspflicht vorgeworfen wird (Twitter-Posts, kommunalpolitisches Engagement, oeffentliche Statements), und fuer die rechtliche Pruefung der Aeusserungsgrenzen.

## 2. Eingaben

- Konkrete Aeusserung im Wortlaut und Kontext
- Plattform (oeffentlich, beruflich oder privat)
- Statusamt und Dienststellung
- Reaktion des Dienstherrn (Ermahnung, Disziplinarvorgang)

## 3. Ablauf / Checkliste

### a) Inhalt der Pflicht
- § 60 BBG bzw. § 33 BeamtStG: Pflicht zu Maessigung und Zurueckhaltung im politischen Bereich, in dem die persoenliche Anschauung dem ueberparteilichen Auftreten widerspraeche.

### b) Reichweite
- Sie gilt nicht nur im Dienst, sondern auch ausserhalb. Sie wird modifiziert durch Art. 5 Abs. 1 GG (Meinungsfreiheit) und Art. 5 Abs. 3 GG (Wissenschaftsfreiheit).

### c) Statusbezug
- Bei Lehrkraeften und Polizei strengere Massstaebe; bei wissenschaftlichen Beamten weitere Spielraeume durch Art. 5 Abs. 3 GG.

### d) Soziale Medien
- Auch Privataccounts ohne dienstliche Kennzeichnung koennen erfasst werden, wenn der Bezug zur Amtsstellung erkennbar ist.

### e) Grenze zur Verfassungstreue
- Aeusserungen, die die freiheitlich demokratische Grundordnung bekaempfen, werden unter dem strengeren Massstab des § 7 BBG / § 33 Abs. 1 BeamtStG bewertet — Skill `verfassungstreue-7-bbg-reichsbuerger`.

## 4. Quellenpflicht

- Normen: § 60 BBG; § 33 BeamtStG; Art. 5 Abs. 1 und 3 GG; Art. 33 Abs. 5 GG.
- Rspr.: BVerfG und BVerwG zur Maessigungspflicht — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Verteidigungs-Memo.
- Stellungnahme im Disziplinarverfahren.

## 6. Verifizierte Quellenanker

- § 60 BBG; § 33 BeamtStG (Pflicht zur Maessigung und Zurueckhaltung im politischen Bereich).
- Art. 5 Abs. 1 GG (Meinungsfreiheit) und Art. 5 Abs. 3 GG (Wissenschaftsfreiheit) als Schranken-Schranke der Maessigungspflicht.
- Art. 33 Abs. 5 GG (hergebrachte Grundsaetze des Berufsbeamtentums); Art. 21 GG (Parteienprivileg).
- BVerfG zur Meinungsfreiheit der Beamten und zur Maessigungspflicht — Datum und Az vor Zitat live verifizieren.
- Statusabhaengige Differenzierung in der Rechtsprechung: strengere Massstaebe fuer Polizei und Lehrkraefte, weitere Spielraeume fuer wissenschaftliches Personal.

## 7. Beispiel (Kurzfassung)

Mandant Studiendirektor postet politische Kommentare zu Migrationsfragen auf Twitter unter Realname und mit Hinweis auf Schulort. Skill liefert Pruefraster Statusbezug, Meinungsfreiheit und Verhaeltnismaessigkeit moeglicher Disziplinarmassnahmen.
