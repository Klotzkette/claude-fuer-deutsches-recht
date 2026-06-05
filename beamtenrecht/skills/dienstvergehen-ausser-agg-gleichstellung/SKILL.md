---
name: dienstvergehen-ausser-agg-gleichstellung
description: "Dienstvergehen Ausser AGG Gleichstellung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Dienstvergehen Ausser AGG Gleichstellung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Dienstvergehen Ausser AGG Gleichstellung** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dienstvergehen-ausser-dienst-47-beamtstg` | Skill zur disziplinarrechtlichen Beurteilung von Verhalten ausserhalb des Dienstes nach § 47 BeamtStG bzw. § 77 BBG. Klaert die Voraussetzung der Eignung zur Beeintraechtigung des Vertrauens den Bezug zur Statusrelevanz und das Verhaeltnis zwischen privatem Verhalten und dienstlichen Anforderungen. Behandelt typische Konstellationen wie Trunkenheitsfahrt Steuerstraftaten Internetkommentare Mitgliedschaft in Vereinigungen sowie Sexualstraftaten ausserhalb des Dienstes. Liefert Verteidigungsbausteine und Pruefraster fuer die Disziplinarklage. |
| `agg-gleichstellung-und-frauenvertretung` | AGG, Gleichstellung, Frauenvertretung, Diversität und diskriminierungsfreie Auswahl im öffentlichen Dienst. |
| `altersteilzeit-93-bbg-blockmodell` | Skill zur Altersteilzeit der Beamten nach § 93 BBG bzw. § 9 BeamtStG i.V.m. den Landesregelungen. Klaert die zwei Modelle Teilzeitmodell und Blockmodell die Bezuegehoehe waehrend Aktiv- und Freistellungsphase die Auswirkungen auf das Ruhegehalt und auf den Versorgungsabschlag nach § 14 BeamtVG. Behandelt die Konstellation Hinausschiebung der Altersgrenze parallele Schwerbehinderung und teilweise Dienstunfaehigkeit waehrend der Altersteilzeit. Liefert Berechnungstabelle und Beratungsraster. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Dienstvergehen Ausser AGG Gleichstellung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dienstvergehen-ausser-dienst-47-beamtstg`

**Fokus:** Skill zur disziplinarrechtlichen Beurteilung von Verhalten ausserhalb des Dienstes nach § 47 BeamtStG bzw. § 77 BBG. Klaert die Voraussetzung der Eignung zur Beeintraechtigung des Vertrauens den Bezug zur Statusrelevanz und das Verhaeltnis zwischen privatem Verhalten und dienstlichen Anforderungen. Behandelt typische Konstellationen wie Trunkenheitsfahrt Steuerstraftaten Internetkommentare Mitgliedschaft in Vereinigungen sowie Sexualstraftaten ausserhalb des Dienstes. Liefert Verteidigungsbausteine und Pruefraster fuer die Disziplinarklage.


# Dienstvergehen ausser Dienst nach § 47 BeamtStG

## 1. Zweck und Anwendungsfall

Skill fuer Beamte, denen Verhalten ausserhalb des Dienstes als Dienstvergehen vorgeworfen wird (typisch: Steuerstraftaten, Trunkenheitsfahrt, ehrenrührige Aeusserungen im Internet, problematische Vereinszugehoerigkeit).

## 2. Eingaben

- Vorwurf in tatsaechlicher Hinsicht
- Strafurteil oder Strafbefehl (falls einschlaegig)
- Statusamt und Dienststellung
- Vorgeschichte und Beurteilungen
- Persoenliche Umstaende

## 3. Ablauf / Checkliste

### a) Voraussetzung
- § 47 Abs. 1 Satz 2 BeamtStG bzw. § 77 Abs. 1 Satz 2 BBG: Verhalten ausserhalb des Dienstes ist Dienstvergehen nur, wenn es nach den Umstaenden des Einzelfalls in besonderem Masse geeignet ist, das Vertrauen in einer fuer das Amt bedeutsamen Weise zu beeintraechtigen.

### b) Statusrelevanz
- Massgebliche Sichtweise: Wuerde der konkrete Sachverhalt das Vertrauen der Allgemeinheit in die Amtsfuehrung gerade dieses Beamten erschuettern?
- Statusbezogene Wertung: Bei Polizei- und Justizbeamten strengere Massstaebe als bei rein verwaltenden Taetigkeiten.

### c) Bewertungsmuster
- Trunkenheitsfahrt: in der Regel Dienstvergehen bei Polizei und Justizvollzug, sonst regelmaessig nur bei besonderen Umstaenden.
- Steuerstraftaten: Dienstvergehen, insbesondere bei Finanzbeamten oder Beamten in herausgehobener Position.
- Internetaeusserungen: Verstoss gegen Maessigungspflicht (§ 60 BBG), siehe Skill `politische-maessigung-60-bbg`.

### d) Verfassungstreue
- Mitgliedschaft in verfassungsfeindlichen Organisationen oder vergleichbare Sympathiebekundungen: Skill `verfassungstreue-7-bbg-reichsbuerger`.

### e) Bemessung
- Bemessung nach § 13 BDG; Skill `disziplinarmassnahmebemessung-13-bdg`.

## 4. Quellenpflicht

- Normen: § 47 BeamtStG; § 77 BBG; § 13 BDG.
- Rspr.: BVerwG zur ausserdienstlichen Pflichtverletzung — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Verteidigungs-Memo mit Pruefraster.
- Schriftsatz Disziplinarverteidigung.

## 6. Verifizierte Quellenanker

- BDG §§ 13, 17, 22, 23, 38, 63 als Kernnormen für Maßnahmebemessung, Einleitung, Strafverfahren, Bindungswirkung, Suspendierung und Aussetzung.
- BDG-Novelle 2024: Vollzugsmodell/Disziplinarverfügung auch für Höchstmaßnahmen im Bundesrecht; Länderrecht gesondert prüfen.
- BVerfG, 14.01.2020 - 2 BvR 2055/16: kein verfassungsrechtlicher Richtervorbehalt für disziplinarische Höchstmaßnahme, wenn Verfahren und volle gerichtliche Kontrolle gesichert sind.
- BVerwG, 02.12.2021 - 2 A 7.21: Reichsbürger-/Verfassungstreue-Fall im Bundesdienst.
- BVerwG, 10.10.2024 - 2 C 15.23: Verfassungstreueanforderungen im juristischen Vorbereitungsdienst.
- Bei Chatgruppen, außerdienstlichen Äußerungen und politischen Grenzfällen immer Kontext, Amtsbezug, Beweisqualität und Grundrechte getrennt würdigen.

## 7. Beispiel (Kurzfassung)

Mandant Lehrer, Verurteilung wegen Steuerhinterziehung 28.000 Euro im Strafbefehlsverfahren. Skill liefert Pruefraster: Bezug zum Lehramt, Statusrelevanz, Bemessung der Disziplinarmassnahme.

## 2. `agg-gleichstellung-und-frauenvertretung`

**Fokus:** AGG, Gleichstellung, Frauenvertretung, Diversität und diskriminierungsfreie Auswahl im öffentlichen Dienst.


# Agg Gleichstellung Und Frauenvertretung

## Aufgabe

AGG, Gleichstellung, Frauenvertretung, Diversität und diskriminierungsfreie Auswahl im öffentlichen Dienst.

## Arbeitsweise

Prüfe Benachteiligungsmerkmal, Indizien, Beteiligung, Auswahlvermerk und Fristen. Output: Risikoanalyse und Beweislastmatrix.

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

## 3. `altersteilzeit-93-bbg-blockmodell`

**Fokus:** Skill zur Altersteilzeit der Beamten nach § 93 BBG bzw. § 9 BeamtStG i.V.m. den Landesregelungen. Klaert die zwei Modelle Teilzeitmodell und Blockmodell die Bezuegehoehe waehrend Aktiv- und Freistellungsphase die Auswirkungen auf das Ruhegehalt und auf den Versorgungsabschlag nach § 14 BeamtVG. Behandelt die Konstellation Hinausschiebung der Altersgrenze parallele Schwerbehinderung und teilweise Dienstunfaehigkeit waehrend der Altersteilzeit. Liefert Berechnungstabelle und Beratungsraster.


# Altersteilzeit § 93 BBG — Blockmodell und Teilzeitmodell

## 1. Zweck und Anwendungsfall

Skill fuer Beamte ab dem 55. Lebensjahr, die ueber Altersteilzeit den gleitenden Uebergang in den Ruhestand wuenschen.

## 2. Eingaben

- Geburtsdatum
- Statusamt und Besoldungsgruppe
- Vorgesehene Modellwahl
- Restdienstzeit bis Regelaltersgrenze
- Schwerbehindertenstatus

## 3. Ablauf / Checkliste

### a) Voraussetzungen
- § 93 BBG (Bund); fuer Laender entsprechende Vorschriften.
- Mindestalter und Mindestbeschaeftigungsdauer, dienstliche Belange nicht entgegenstehend.

### b) Modelle
- Teilzeitmodell: gleichmaessige Reduzierung der Arbeitszeit ueber die gesamte Altersteilzeit.
- Blockmodell: Arbeitsphase mit voller Arbeitszeit und anschliessende Freistellungsphase.

### c) Bezuege
- Bezuege betragen in der Regel 80 v. H. der Bezuege der entsprechenden Vollzeitbeschaeftigung (Altersteilzeitzuschlag).
- Auswirkungen auf Beihilfe und Heilfuersorge pruefen.

### d) Ruhegehaltfaehigkeit
- Altersteilzeit ist anteilig ruhegehaltfaehig.

### e) Versorgungsabschlag
- Beim Eintritt in den Ruhestand nach Altersteilzeit kein Versorgungsabschlag, soweit die Altersteilzeit bis zur Regelaltersgrenze laeuft. Bei vorzeitigem Antragsruhestand greift Skill `versorgungsabschlag-14-beamtvg`.

### f) Aenderungen waehrend der Altersteilzeit
- Bei eintretender Dienstunfaehigkeit gelten Sondervorschriften zur Beendigung der Altersteilzeit; Restbezuege und Versorgung sind zu bemessen.

## 4. Quellenpflicht

- Normen: § 93 BBG; § 9 BeamtStG i.V.m. Landesrecht; § 6 BeamtVG; § 14 BeamtVG.
- Rspr.: BVerwG zu Altersteilzeit — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Berechnungstabelle Bezuege und Versorgung mit und ohne Altersteilzeit.
- Antrag auf Altersteilzeit.

## 6. Verifizierte Quellenanker

- § 93 BBG (Altersteilzeit Bund) i.V.m. § 9 ArbZV (Arbeitszeitverordnung); landesrechtliche Altersteilzeitvorschriften (BeamtStG enthaelt keine Altersteilzeitnorm; die Laender regeln Altersteilzeit eigenstaendig in ihren Landesbeamtengesetzen).
- § 6 BeamtVG (ruhegehaltfaehige Dienstzeit Altersteilzeit); § 14 BeamtVG (Versorgungsabschlag).
- Altersteilzeitzuschlagsverordnung Bund und landesrechtliche Aequivalente.
- BVerwG zur Altersteilzeit der Beamten — Datum und Az vor Zitat live verifizieren.

## 7. Beispiel (Kurzfassung)

Mandant 57 Jahre, will sechs Jahre Altersteilzeit im Blockmodell (drei Jahre Aktiv, drei Jahre Freistellung). Skill liefert Berechnung Bezuege und Versorgung.
