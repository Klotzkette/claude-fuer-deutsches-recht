---
name: ptbs-polizei-reaktivierung-bbg-remonstration
description: "Ptbs Polizei Reaktivierung BBG Remonstration: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ptbs Polizei Reaktivierung BBG Remonstration

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Ptbs Polizei Reaktivierung BBG Remonstration** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ptbs-polizei-anerkennung-dienstunfall` | Skill zur Anerkennung der posttraumatischen Belastungsstoerung als Dienstunfall bei Polizei Justizvollzug Feuerwehr und Soldaten. Klaert die Anforderungen an die Glaubhaftmachung eines auslosenden Ereignisses die Anforderungen an den Kausalitaetsnachweis bei psychiatrischer Diagnose nach ICD-10 oder DSM-5 sowie die Konstellation Mehrfachbelastung durch wiederkehrende Einsaetze. Behandelt das Verhaeltnis zur Berufskrankheit nach § 31 BeamtVG und den Sonderfall Einsatzunfall bei Auslandsverwendung. Liefert Pruefraster und Antragsbausteine. |
| `reaktivierung-29-bbg-rechtsanspruch` | Skill zur Reaktivierung eines Ruhestandsbeamten nach § 29 BBG bzw. § 29 BeamtStG i.V.m. Landesrecht. Klaert die Voraussetzungen der wiedererlangten Dienstfaehigkeit Rechtsanspruch auf Reaktivierung Spielraum des Dienstherrn dienstliche Belange und Altersgrenze. Behandelt die Konstellation Ruhestand wegen Dienstunfaehigkeit bei amtsaerztlich attestierter Wiederherstellung sowie Reaktivierung gegen Antrag des Dienstherrn. Liefert Pruefraster und Schriftsatzbausteine. |
| `remonstration-rechtswidrige-weisung` | Remonstration bei rechtswidriger Weisung: Pflichten, Ablauf, Dokumentation und Schutz des Beamten. |
| `richter-praesidium-und-geschaeftsverteilung` | Präsidium, Geschäftsverteilungsplan, Abordnung und Besetzung mit Proberichtern. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Ptbs Polizei Reaktivierung BBG Remonstration**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ptbs-polizei-anerkennung-dienstunfall`

**Fokus:** Skill zur Anerkennung der posttraumatischen Belastungsstoerung als Dienstunfall bei Polizei Justizvollzug Feuerwehr und Soldaten. Klaert die Anforderungen an die Glaubhaftmachung eines auslosenden Ereignisses die Anforderungen an den Kausalitaetsnachweis bei psychiatrischer Diagnose nach ICD-10 oder DSM-5 sowie die Konstellation Mehrfachbelastung durch wiederkehrende Einsaetze. Behandelt das Verhaeltnis zur Berufskrankheit nach § 31 BeamtVG und den Sonderfall Einsatzunfall bei Auslandsverwendung. Liefert Pruefraster und Antragsbausteine.


# PTBS und Dienstunfall im Vollzugsdienst

## 1. Zweck und Anwendungsfall

Skill fuer Polizei- und Justizvollzugsbeamte, Feuerwehrleute und Soldaten, die wegen einer posttraumatischen Belastungsstoerung Dienstunfallfuersorge beanspruchen. Anwendung neben dem Schwester-Skill `dienstunfall-anerkennung-45-beamtvg`.

## 2. Eingaben

- Schilderung des oder der traumatischen Ereignisse
- Psychiatrisches Gutachten oder Befund (ICD-10 F43.1 oder DSM-5)
- Einsatzberichte
- Datum erster Krankheits- oder Behandlungsschritt
- Datum der ersten Meldung an den Dienstherrn

## 3. Ablauf / Checkliste

### a) Anerkennung als Dienstunfall
- Erforderlich: konkretes, ploetzliches Ereignis, das die Anforderungen eines aeusseren Einwirkungsvorgangs erfuellt. Mehrere "kleine" Belastungen koennen nach Rechtsprechung nicht als Dienstunfall gewertet werden, sondern moeglicherweise als Berufskrankheit.
- Bei klar identifizierbarem Ereignis (Schiesserei, Geiselsituation, Fund einer Leiche, Suizidassistenz) anerkennungsfaehig.

### b) Kausalitaet
- Verlangt wird die rechtlich wesentliche Mitursache. Vorerkrankungen oder seelische Pradisposition schliessen Anerkennung nicht aus, soweit das Ereignis als wesentliche Mitursache zu werten ist.
- Beweismittel: psychiatrisches Gutachten, idealerweise mit Diagnose nach ICD-10 / DSM-5, Symptomverlauf und Verbindung zum Ereignis.

### c) Meldefrist
- § 45 BeamtVG: zwei Jahre ab Kenntnis, absolute Frist zehn Jahre. Bei PTBS oft verzoegerte Meldung; rechtzeitige Spaetfolgenmeldung beachten.

### d) Abgrenzung zur Berufskrankheit
- Wiederkehrende Belastungen ohne identifizierbares Einzelereignis werden moeglicherweise nur als Berufskrankheit (§ 31 Abs. 3 BeamtVG) anerkannt, sofern in der BKV gelistet.

### e) Folgen
- Anerkennung fuehrt zu Heilverfahrenskosten, Unfallfuersorge, ggf. Unfallruhegehalt; siehe `unfallruhegehalt-36-beamtvg`.

## 4. Quellenpflicht

- Normen: §§ 30, 31, 45 BeamtVG; ICD-10 F43.1; BKV.
- Rspr.: BVerwG zur Anerkennung psychischer Erkrankungen als Dienstunfall — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Dienstunfallmeldung mit psychiatrischem Gutachten.
- Hilfsantrag auf Anerkennung als Berufskrankheit.

## 6. Verifizierte Quellenanker

- §§ 30, 31, 45 BeamtVG; § 31 Abs. 3 BeamtVG i.V.m. der Berufskrankheitenverordnung (BKV) fuer den Hilfsantrag Berufskrankheit.
- ICD-10 F43.1 als Diagnosegrundlage; DSM-5 als ergaenzendes Diagnosesystem.
- Anforderung an psychiatrisches Gutachten: Diagnose, Symptomverlauf, Verbindung zum auslosenden Ereignis, Differentialdiagnose.
- BVerwG zur Anerkennung psychischer Erkrankungen als Dienstunfall und zur Abgrenzung Berufskrankheit — Datum und Az vor Zitat live verifizieren.
- Bei Auslandsverwendung Soldaten und Bundespolizei Auslandsverwendungsgesetz und Einsatzversorgungsgesetz ergaenzend pruefen.

## 7. Beispiel (Kurzfassung)

Polizeihauptmeister entdeckt erhaengten Vermissten; entwickelt PTBS. Skill liefert Dienstunfallmeldung und Kausalitaetsdarstellung.

## 2. `reaktivierung-29-bbg-rechtsanspruch`

**Fokus:** Skill zur Reaktivierung eines Ruhestandsbeamten nach § 29 BBG bzw. § 29 BeamtStG i.V.m. Landesrecht. Klaert die Voraussetzungen der wiedererlangten Dienstfaehigkeit Rechtsanspruch auf Reaktivierung Spielraum des Dienstherrn dienstliche Belange und Altersgrenze. Behandelt die Konstellation Ruhestand wegen Dienstunfaehigkeit bei amtsaerztlich attestierter Wiederherstellung sowie Reaktivierung gegen Antrag des Dienstherrn. Liefert Pruefraster und Schriftsatzbausteine.


# Reaktivierung nach § 29 BBG — Rueckkehr aus dem Ruhestand

## 1. Zweck und Anwendungsfall

Skill fuer ehemals wegen Dienstunfaehigkeit in den Ruhestand versetzte Beamte, die ihre Dienstfaehigkeit wiedererlangt haben und Reaktivierung anstreben — oder die gegen eine Reaktivierung durch den Dienstherrn Rechtsschutz suchen.

## 2. Eingaben

- Ruhestandsbescheid und Datum
- Aktuelles amtsaerztliches Gutachten
- Dienstherr
- Lebensalter und Regelaltersgrenze
- Dienstposten in Aussicht

## 3. Ablauf / Checkliste

### a) Voraussetzung
- § 29 BBG bzw. § 29 BeamtStG i.V.m. Landesrecht.
- Wiederhergestellte Dienstfaehigkeit muss amtsaerztlich attestiert sein.
- Reaktivierung scheidet aus, wenn das 67. Lebensjahr (bzw. die Regelaltersgrenze) erreicht ist.

### b) Antragsanspruch
- Reaktivierung auf Antrag des Beamten: Anspruch besteht, wenn Dienstfaehigkeit wieder vorliegt und keine zwingenden dienstlichen Belange entgegenstehen.

### c) Anordnung durch Dienstherrn
- Reaktivierung von Amts wegen unter den gleichen Voraussetzungen moeglich; insbesondere bei wiederhergestellter Dienstfaehigkeit innerhalb von zehn Jahren nach Ruhestandsversetzung.

### d) Folgen
- Wiederherstellung des aktiven Beamtenverhaeltnisses; Bezuege statt Versorgungsbezuege.
- Statusamt grundsaetzlich unveraendert.

### e) Rechtsschutz
- Widerspruch gegen Bescheid; Klage zum VG; ggf. einstweilige Anordnung.

## 4. Quellenpflicht

- Normen: § 29 BBG; § 29 BeamtStG i.V.m. Landesrecht.
- Rspr.: BVerwG zur Reaktivierung und zum Anspruch auf Wiedereingliederung — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Antrag auf Reaktivierung.
- Widerspruchsschrift gegen Reaktivierungsanordnung.

## 6. Verifizierte Quellenanker

- § 46 BBG (Wiederherstellung der Dienstfaehigkeit, Reaktivierung Bund); § 29 BeamtStG i.V.m. Landesrecht.
- Voraussetzung amtsaerztlich attestierte Wiederherstellung der Dienstfaehigkeit; Zehn-Jahres-Frist nach Ruhestandsversetzung als Regelgrenze.
- BVerwG zum Reaktivierungsanspruch und zu dienstlichen Belangen — Datum und Az vor Zitat live verifizieren.
- Altersgrenze Regelaltersgrenze als absolute Schranke; nach Erreichen keine Reaktivierung mehr.

## 7. Beispiel (Kurzfassung)

Mandant wurde 2019 wegen depressiver Episode in den Ruhestand versetzt; nunmehr stabilisiert. Skill liefert Reaktivierungsantrag mit amtsaerztlichem Gutachten und Hinweis auf Anspruch.

## 3. `remonstration-rechtswidrige-weisung`

**Fokus:** Remonstration bei rechtswidriger Weisung: Pflichten, Ablauf, Dokumentation und Schutz des Beamten.


# Remonstration Rechtswidrige Weisung

## Aufgabe

Remonstration bei rechtswidriger Weisung: Pflichten, Ablauf, Dokumentation und Schutz des Beamten.

## Arbeitsweise

Prüfe Weisungsart, offensichtliche Rechtswidrigkeit, Dienstweg, Dringlichkeit und Dokumentation. Erzeuge Remonstrationsvermerk mit nüchternem Ton.

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

## 4. `richter-praesidium-und-geschaeftsverteilung`

**Fokus:** Präsidium, Geschäftsverteilungsplan, Abordnung und Besetzung mit Proberichtern.


# Richter Praesidium Und Geschaeftsverteilung

## Aufgabe

Präsidium, Geschäftsverteilungsplan, Abordnung und Besetzung mit Proberichtern.

## Arbeitsweise

Prüfe GVP, Präsidiumsentscheidung, Abordnungsdauer, DRiG-Sonderregeln und mögliche Besetzungsrüge-Schnittstellen.

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
