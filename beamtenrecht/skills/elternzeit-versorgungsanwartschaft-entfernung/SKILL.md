---
name: elternzeit-versorgungsanwartschaft-entfernung
description: "Elternzeit Versorgungsanwartschaft Entfernung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Elternzeit Versorgungsanwartschaft Entfernung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Elternzeit Versorgungsanwartschaft Entfernung** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `elternzeit-versorgungsanwartschaft` | Skill zur Elternzeit der Beamten und ihren Auswirkungen auf Versorgungsanwartschaft Stufenaufstieg und Beihilfeberechtigung. Klaert die Beruecksichtigung der Kindererziehungszeiten im Ruhegehalt die Frage des ruhegehaltfaehigen Charakters der Elternzeit das Verhaeltnis zu Teilzeit-Elternzeit und dem Erziehungsurlaub bei Versorgungsausgleich nach Scheidung. Behandelt typische Konstellationen lange Elternzeit gestaffelt nach Kindern Teilzeitruckkehr Wiederaufnahme. Liefert Pruefraster und Antragsbausteine. |
| `entfernung-aus-dem-beamtenverhaeltnis-unterhalt` | Skill zur Entfernung aus dem Beamtenverhaeltnis als schaerfster Disziplinarmassnahme und zum Anspruch auf Unterhaltsbeitrag. Klaert das Verhaeltnis von Statusverlust und Versorgungsverlust den Anspruch auf Unterhaltsbeitrag nach § 10 BDG die Bemessung des Unterhaltsbeitrags und die Folgen fuer Krankenversicherung Beihilfe und Rentenversicherung. Behandelt die Konstellation Nachversicherung in der gesetzlichen Rentenversicherung sowie das Verhaeltnis zur Ruhestandsversetzung. Liefert Pruefraster und Antragsbausteine. |
| `entlassung-und-statusbeendigung` | Entlassung, Verlust der Beamtenrechte, Altersgrenze, einstweiliger Ruhestand und Statusbeendigung. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Elternzeit Versorgungsanwartschaft Entfernung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `elternzeit-versorgungsanwartschaft`

**Fokus:** Skill zur Elternzeit der Beamten und ihren Auswirkungen auf Versorgungsanwartschaft Stufenaufstieg und Beihilfeberechtigung. Klaert die Beruecksichtigung der Kindererziehungszeiten im Ruhegehalt die Frage des ruhegehaltfaehigen Charakters der Elternzeit das Verhaeltnis zu Teilzeit-Elternzeit und dem Erziehungsurlaub bei Versorgungsausgleich nach Scheidung. Behandelt typische Konstellationen lange Elternzeit gestaffelt nach Kindern Teilzeitruckkehr Wiederaufnahme. Liefert Pruefraster und Antragsbausteine.


# Elternzeit — Auswirkungen auf Versorgungsanwartschaft

## 1. Zweck und Anwendungsfall

Skill fuer Beamte, die Elternzeit nehmen oder genommen haben und die Auswirkungen auf Besoldung Stufenaufstieg Versorgungsbezuege und Beihilfe pruefen wollen.

## 2. Eingaben

- Geburtsdaten der Kinder
- Zeitraeume Elternzeit Voll- und Teilzeit
- Stufenfeststellung
- Versorgungsauskunft

## 3. Ablauf / Checkliste

### a) Ruhegehaltfaehigkeit
- Elternzeit ohne Bezuege ist grundsaetzlich nicht ruhegehaltfaehig (§ 6 BeamtVG i.V.m. § 6 BEEG).
- Kindererziehungszeiten werden in der Versorgung nach Massgabe gesonderter Regelungen beruecksichtigt (Kindererziehungszuschlag und vergleichbare Leistungen).

### b) Stufenaufstieg
- Elternzeit hemmt grundsaetzlich den Stufenaufstieg; spezifische Verzoegerungstatbestaende pruefen.

### c) Teilzeit waehrend Elternzeit
- Teilzeit nach § 92 BBG / § 43 BeamtStG i.V.m. Landesrecht ermoeglicht Beruecksichtigung pro rata.

### d) Beihilfe
- Beihilfeberechtigung waehrend Elternzeit bleibt regelmaessig erhalten.

### e) Versorgungsausgleich
- Bei Scheidung waehrend oder nach Elternzeit sind Versorgungsanwartschaften des Beamten zu uebertragen; Skill `versorgungslastenteilung-107b-beamtvg` ist nicht einschlaegig.

## 4. Quellenpflicht

- Normen: § 6 BeamtVG; § 6 BEEG; § 80 BBG; § 92 BBG; § 43 BeamtStG i.V.m. Landesrecht.
- Rspr.: BVerwG zur Beruecksichtigung der Elternzeit in der Versorgung — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Versorgungsausblick mit und ohne Beruecksichtigung der Elternzeit.
- Beratungsschreiben Mandantin.

## 6. Verifizierte Quellenanker

- § 6 BeamtVG (ruhegehaltfaehige Dienstzeiten); § 50a, § 50b BeamtVG (Kindererziehungszuschlag und Kindererziehungsergaenzungszuschlag).
- § 15 BEEG (Anspruch auf Elternzeit); § 79 BBG (Mutterschutz und Elternzeit Bundesbeamte); § 92 BBG (Teilzeit aus familiaeren Gruenden); § 43 BeamtStG i.V.m. Landesrecht (Teilzeit waehrend Elternzeit).
- BVerfG zur Beruecksichtigung von Kindererziehungszeiten in der Beamtenversorgung — Datum und Az vor Zitat in amtlicher Quelle live pruefen.
- Versorgungsausgleichsgesetz bei Scheidung waehrend oder nach Elternzeit; § 12 VersAusglG (Beamtenversorgung als Anrecht).

## 7. Beispiel (Kurzfassung)

Mandantin Beamtin A12, drei Kinder, je drei Jahre Elternzeit. Skill liefert Berechnung der ruhegehaltfaehigen Zeiten und Hinweise auf Kindererziehungszuschlag.

## 2. `entfernung-aus-dem-beamtenverhaeltnis-unterhalt`

**Fokus:** Skill zur Entfernung aus dem Beamtenverhaeltnis als schaerfster Disziplinarmassnahme und zum Anspruch auf Unterhaltsbeitrag. Klaert das Verhaeltnis von Statusverlust und Versorgungsverlust den Anspruch auf Unterhaltsbeitrag nach § 10 BDG die Bemessung des Unterhaltsbeitrags und die Folgen fuer Krankenversicherung Beihilfe und Rentenversicherung. Behandelt die Konstellation Nachversicherung in der gesetzlichen Rentenversicherung sowie das Verhaeltnis zur Ruhestandsversetzung. Liefert Pruefraster und Antragsbausteine.


# Entfernung aus dem Beamtenverhaeltnis und Unterhaltsbeitrag

## 1. Zweck und Anwendungsfall

Skill fuer Beamte, denen die Entfernung aus dem Beamtenverhaeltnis droht oder verfuegt ist. Hilft bei der Pruefung der Unterhaltsbeitragsfrage und der Anschlussversorgung.

## 2. Eingaben

- Disziplinarurteil oder -bescheid
- Familienstand und Unterhaltspflichten
- Dauer der Beamtenzeit
- Krankheits- und Beihilfestatus

## 3. Ablauf / Checkliste

### a) Folgen der Entfernung
- § 10 BDG: Verlust der Bezuege, des Statusamtes und der Versorgungsansprueche aus dem Beamtenverhaeltnis.
- Nachversicherung in der gesetzlichen Rentenversicherung (§ 8 SGB VI).

### b) Unterhaltsbeitrag
- § 10 Abs. 3 BDG: auf Antrag Unterhaltsbeitrag fuer eine bestimmte Zeit (in der Regel bis zu sechs Monate), wenn der ehemalige Beamte unverschuldet bedürftig ist.
- Bemessung in Anlehnung an die zuletzt bezogenen Dienstbezuege.

### c) Krankenversicherung
- Bei Entfernung erlischt regelmaessig die Beihilfeberechtigung. PKV-Versicherte muessen Tarif anpassen.
- Anwartschaftsversicherung pruefen.

### d) Verhaeltnis zur Ruhestandsversetzung
- Bei laufender Erkrankung ist zu pruefen, ob alternativ Ruhestandsversetzung wegen Dienstunfaehigkeit moeglich ist; die Disziplinarklage wuerde dann grundsaetzlich zur Aberkennung des Ruhegehalts fuehren (anderer Tatbestand).

### e) Verfahren
- Disziplinarverfuegung anfechten; Disziplinarklage abwehren.
- Antrag auf Unterhaltsbeitrag binnen Frist nach Eintritt der Entfernung.

## 4. Quellenpflicht

- Normen: §§ 10, 11 BDG; § 8 SGB VI; landesrechtliche Aequivalente.
- Rspr.: BVerwG zur Entfernung und zum Unterhaltsbeitrag — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Antrag auf Unterhaltsbeitrag.
- Beratungsschreiben Nachversicherung und PKV.

## 6. Verifizierte Quellenanker

- BDG §§ 13, 17, 22, 23, 38, 63 als Kernnormen für Maßnahmebemessung, Einleitung, Strafverfahren, Bindungswirkung, Suspendierung und Aussetzung.
- BDG-Novelle 2024: Vollzugsmodell/Disziplinarverfügung auch für Höchstmaßnahmen im Bundesrecht; Länderrecht gesondert prüfen.
- BVerfG, 14.01.2020 - 2 BvR 2055/16: kein verfassungsrechtlicher Richtervorbehalt für disziplinarische Höchstmaßnahme, wenn Verfahren und volle gerichtliche Kontrolle gesichert sind.
- BVerwG, 02.12.2021 - 2 A 7.21: Reichsbürger-/Verfassungstreue-Fall im Bundesdienst.
- BVerwG, 10.10.2024 - 2 C 15.23: Verfassungstreueanforderungen im juristischen Vorbereitungsdienst.
- Bei Chatgruppen, außerdienstlichen Äußerungen und politischen Grenzfällen immer Kontext, Amtsbezug, Beweisqualität und Grundrechte getrennt würdigen.

## 7. Beispiel (Kurzfassung)

Mandant Studiendirektor entfernt wegen Veruntreuung von 35.000 Euro Schulgeld. Skill liefert Antrag auf Unterhaltsbeitrag und Hinweise auf Nachversicherung in der gesetzlichen Rentenversicherung.

## 3. `entlassung-und-statusbeendigung`

**Fokus:** Entlassung, Verlust der Beamtenrechte, Altersgrenze, einstweiliger Ruhestand und Statusbeendigung.


# Entlassung Und Statusbeendigung

## Aufgabe

Entlassung, Verlust der Beamtenrechte, Altersgrenze, einstweiliger Ruhestand und Statusbeendigung.

## Arbeitsweise

Prüfe Beendigungsgrund, Anhörung, Zuständigkeit, Versorgung und Rechtsschutz. Unterscheide Entlassung kraft Gesetzes, Verwaltungsakt und Disziplinarfolge.

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
