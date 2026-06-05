---
name: versorgung-ruhegehalt-versorgungsabschlag
description: "Versorgung Ruhegehalt Versorgungsabschlag: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Versorgung Ruhegehalt Versorgungsabschlag

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Versorgung Ruhegehalt Versorgungsabschlag** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `versorgung-ruhegehalt-beamtvg` | Versorgung und Ruhegehalt: ruhegehaltfähige Dienstzeit, Versorgungsabschlag, Mindestversorgung, Hinterbliebenenversorgung. |
| `versorgungsabschlag-14-beamtvg` | Skill zum Versorgungsabschlag bei vorzeitigem Eintritt in den Ruhestand nach § 14 Abs. 3 BeamtVG. Klaert die Hoehe des Abschlags die Konstellationen Antragsruhestand vor Erreichen der Regelaltersgrenze und Ruhestand wegen Dienstunfaehigkeit sowie die Ausnahmen fuer schwerbehinderte Beamte und fuer Dienstunfall. Behandelt das Verhaeltnis zum Mindestversorgungsschutz und die Berechnung im Wechselspiel mit Altersteilzeitmodellen. Liefert Berechnungstabelle und Beratungsraster. |
| `versorgungslastenteilung-107b-beamtvg` | Skill zur Versorgungslastenteilung bei Dienstherrenwechsel nach § 107b BeamtVG bzw. dem Versorgungslastenteilungs-Staatsvertrag. Klaert die Berechnung der Abfindung den Wechsel zwischen Bund und Land und zwischen Bundeslaendern die Hoehe des Erstattungssatzes nach Diensteinheiten Diensttagen oder Versorgungseinheiten und die Faelle in denen der neue Dienstherr keine Abfindung erhaelt. Behandelt Konstellationen Wechsel aus Hochschule in Ministerium Wechsel zwischen Bundeslaendern und Wechsel in den oeffentlichen Dienst der EU. Liefert Pruefraster und Berechnungstabelle. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Versorgung Ruhegehalt Versorgungsabschlag**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `versorgung-ruhegehalt-beamtvg`

**Fokus:** Versorgung und Ruhegehalt: ruhegehaltfähige Dienstzeit, Versorgungsabschlag, Mindestversorgung, Hinterbliebenenversorgung.


# Versorgung Ruhegehalt Beamtvg

## Aufgabe

Versorgung und Ruhegehalt: ruhegehaltfähige Dienstzeit, Versorgungsabschlag, Mindestversorgung, Hinterbliebenenversorgung.

## Arbeitsweise

Berechne nur mit belegten Daten. Prüfe Dienstzeiten, Teilzeit, Beurlaubung, Versorgungsauskunft und Anrechnung.

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

## 2. `versorgungsabschlag-14-beamtvg`

**Fokus:** Skill zum Versorgungsabschlag bei vorzeitigem Eintritt in den Ruhestand nach § 14 Abs. 3 BeamtVG. Klaert die Hoehe des Abschlags die Konstellationen Antragsruhestand vor Erreichen der Regelaltersgrenze und Ruhestand wegen Dienstunfaehigkeit sowie die Ausnahmen fuer schwerbehinderte Beamte und fuer Dienstunfall. Behandelt das Verhaeltnis zum Mindestversorgungsschutz und die Berechnung im Wechselspiel mit Altersteilzeitmodellen. Liefert Berechnungstabelle und Beratungsraster.


# Versorgungsabschlag § 14 Abs. 3 BeamtVG

## 1. Zweck und Anwendungsfall

Skill fuer Beamte, die einen Antragsruhestand vor Erreichen der Regelaltersgrenze pruefen oder die nach Ruhestandsversetzung den Versorgungsabschlag rechtlich angreifen wollen.

## 2. Eingaben

- Geburtsdatum
- Eintritt in das Beamtenverhaeltnis
- Datum des Eintritts in den Ruhestand (geplant oder erfolgt)
- Grund (Antragsruhestand, Dienstunfaehigkeit, Schwerbehinderung)
- Versorgungsbescheid

## 3. Ablauf / Checkliste

### a) Anwendungsbereich
- § 14 Abs. 3 BeamtVG: 3,6 v. H. Versorgungsabschlag fuer jedes Jahr des vorzeitigen Eintritts in den Ruhestand, maximal 10,8 v. H. der Versorgungsbezuege.

### b) Konstellationen
- Antragsruhestand auf Antrag nach Vollendung des 63. (bzw. 62.) Lebensjahres: Abschlag greift.
- Ruhestand wegen Dienstunfaehigkeit ohne Dienstunfall: Abschlag greift unter Voraussetzungen; Ausnahme bei langer Dienstzeit (z. B. ab 40 Jahre).
- Ruhestand wegen Dienstunfaehigkeit infolge Dienstunfall: kein Abschlag.

### c) Ausnahmen
- Schwerbehindertenstatus mit Grad der Behinderung mindestens 50 ermoeglicht den abschlagsfreien Antragsruhestand mit Vollendung des 60. Lebensjahres (geltende Altersgrenzen pruefen).

### d) Verhaeltnis zur Altersteilzeit
- Bei Blockmodellen der Altersteilzeit ist die Berechnung im Hinblick auf den Versorgungsabschlag besonders zu pruefen.

### e) Rechtsschutz
- Widerspruch gegen Versorgungsbescheid; Klage vor dem VG.

## 4. Quellenpflicht

- Normen: § 14 BeamtVG; § 4 BeamtVG; § 8 BBG, § 51 BBG; landesrechtliche Aequivalente.
- Rspr.: BVerwG zum Versorgungsabschlag — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Berechnungstabelle: Bezuege ohne Abschlag, Abschlagsfaktor, Bezuege mit Abschlag.
- Beratungsschreiben mit Vor- und Nachteilen Antragsruhestand.

## 6. Verifizierte Quellenanker

- BeamtVG und jeweiliges Landesversorgungsrecht sauber trennen; Versorgung ist bei Landesbeamten seit der Föderalismusreform grundsätzlich Landesrecht.
- BVerfG, 27.09.2005 - 2 BvR 1387/02: Versorgungsänderungsrecht und Alimentationsprinzip als verfassungsrechtlicher Anker.
- BVerfG, 20.03.2007 - 2 BvL 11/04: Versorgung aus dem letzten Amt und Wartefrist.
- BVerwG, 25.10.2018 - 2 C 33.17 sowie BVerwG, 30.10.2018 - 2 C 32.17 als verifizierte Anker für Besoldungs-/Versorgungsvorlagen; Reichweite auf konkrete Versorgungsfrage jeweils prüfen.
- Konkrete Berechnung nie aus Modellwissen: Bescheid, Dienstzeiten, Ruhensnormen, Rentenbescheide und Landesrecht in Tabelle nachziehen.

## 7. Beispiel (Kurzfassung)

Mandantin 62 Jahre, Antragsruhestand zum Jahresende. Skill liefert Berechnung des Versorgungsabschlags und Hinweise auf Alternativen (Altersteilzeit Blockmodell, Pruefung Schwerbehinderung).

## 3. `versorgungslastenteilung-107b-beamtvg`

**Fokus:** Skill zur Versorgungslastenteilung bei Dienstherrenwechsel nach § 107b BeamtVG bzw. dem Versorgungslastenteilungs-Staatsvertrag. Klaert die Berechnung der Abfindung den Wechsel zwischen Bund und Land und zwischen Bundeslaendern die Hoehe des Erstattungssatzes nach Diensteinheiten Diensttagen oder Versorgungseinheiten und die Faelle in denen der neue Dienstherr keine Abfindung erhaelt. Behandelt Konstellationen Wechsel aus Hochschule in Ministerium Wechsel zwischen Bundeslaendern und Wechsel in den oeffentlichen Dienst der EU. Liefert Pruefraster und Berechnungstabelle.


# Versorgungslastenteilung bei Dienstherrenwechsel

## 1. Zweck und Anwendungsfall

Skill fuer Konstellationen, in denen ein Beamter den Dienstherrn wechselt (Bund nach Land, Land nach Land, Hochschule nach Ministerium, Wechsel in den EU-Dienst) und die Frage zu klaeren ist, wie die spaeteren Versorgungsleistungen zwischen den beteiligten Dienstherren aufzuteilen sind.

## 2. Eingaben

- Vorgeschichte des Dienstverhaeltnisses (Anfang, Dienstherrenwechsel, Statusverwendungen)
- Datum jedes Wechsels
- Statusamt zum Zeitpunkt des Wechsels
- Beruecksichtigungsfaehige Vordienstzeiten
- Bei Wechsel in EU- oder zwischenstaatliche Verwendung: einschlaegige Regelungen

## 3. Ablauf / Checkliste

### a) Anwendungsbereich
- Versorgungslastenteilungs-Staatsvertrag fuer Wechsel zwischen Bund und Land und zwischen Bundeslaendern.
- § 107b BeamtVG fuer Faelle, die nicht vom Staatsvertrag erfasst sind (z. B. mittelbare Verwaltung).

### b) Berechnung
- Abfindung in Hoehe eines Vielfachen der Bezuege im Zeitpunkt des Wechsels, multipliziert mit den Dienstjahren beim abgebenden Dienstherrn.
- Faktor und Bemessungsgrundlage nach dem Staatsvertrag oder § 107b BeamtVG.

### c) Konstellation Hochschule -> Ministerium
- Wechsel in mittelbare Verwaltung oft komplexer; pruefen, ob Hochschule eigener Dienstherr ist.

### d) Auslandsverwendung und EU
- Bei Wechsel in den EU-Dienst gilt das EU-Beamtenstatut; Vordienstzeiten werden in der Regel als Pensionskapital transferiert.

### e) Folgenwirkung
- Die Versorgung wird beim letzten Dienstherrn berechnet; Versorgungslastenteilung wirkt im Innenverhaeltnis der Dienstherren.

## 4. Quellenpflicht

- Normen: § 107b BeamtVG; Versorgungslastenteilungs-Staatsvertrag; EU-Beamtenstatut.
- Rspr.: BVerwG zur Versorgungslastenteilung — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Tabellarische Berechnung der Versorgungslastenteilung.
- Hinweisschreiben an alle beteiligten Dienstherren.

## 6. Verifizierte Quellenanker

- BeamtVG und jeweiliges Landesversorgungsrecht sauber trennen; Versorgung ist bei Landesbeamten seit der Föderalismusreform grundsätzlich Landesrecht.
- BVerfG, 27.09.2005 - 2 BvR 1387/02: Versorgungsänderungsrecht und Alimentationsprinzip als verfassungsrechtlicher Anker.
- BVerfG, 20.03.2007 - 2 BvL 11/04: Versorgung aus dem letzten Amt und Wartefrist.
- BVerwG, 25.10.2018 - 2 C 33.17 sowie BVerwG, 30.10.2018 - 2 C 32.17 als verifizierte Anker für Besoldungs-/Versorgungsvorlagen; Reichweite auf konkrete Versorgungsfrage jeweils prüfen.
- Konkrete Berechnung nie aus Modellwissen: Bescheid, Dienstzeiten, Ruhensnormen, Rentenbescheide und Landesrecht in Tabelle nachziehen.

## 7. Beispiel (Kurzfassung)

Mandantin wechselt nach 18 Jahren als Professorin in Hessen in das Bundesministerium fuer Bildung. Skill liefert Berechnung der von Hessen an den Bund zu zahlenden Abfindung nach dem Staatsvertrag.
