---
name: krankheitsbedingte-urlaubsuebertragung
description: "Krankheitsbedingte Urlaubsuebertragung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Krankheitsbedingte Urlaubsuebertragung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Krankheitsbedingte Urlaubsuebertragung** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `krankheitsbedingte-urlaubsuebertragung` | Skill zur Uebertragung und Abgeltung des Erholungsurlaubs bei laenger andauernder Erkrankung im Beamtenverhaeltnis. Klaert die 15-Monats-Frist nach EuGH-Rechtsprechung den unionsrechtlichen Mindesturlaub die Unterscheidung zwischen unionsrechtlich gewaehrtem Urlaub und nationalem Zusatzurlaub den Verzicht auf Verfall mangels Mitwirkungsobliegenheit sowie das Verhaeltnis zur Abgeltung bei Eintritt in den Ruhestand. Liefert Berechnungstabelle und Pruefraster. |
| `krankheitskosten-beihilfe-pkv-widerspruch` | Krankheitskosten im Beamtenrecht: Beihilfe, PKV, ablehnender Beihilfebescheid, medizinische Notwendigkeit, Voranerkennung, Frist und Widerspruch. |
| `landesrecht-16-laender-routenplan` | Routenplan für Landesbeamtenrecht aller 16 Länder: Landesbeamtengesetz, Laufbahn, Besoldung, Versorgung, Beihilfe, Disziplinarrecht und Landesrichterrecht ohne falsches Bundesrechts-Autopilotieren. |
| `laufbahnrecht-bund` | Laufbahnrecht Bund: Laufbahngruppen, Vorbereitungsdienst, Aufstieg, Laufbahnwechsel, Anerkennung von Zeiten und Qualifikation. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Krankheitsbedingte Urlaubsuebertragung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `krankheitsbedingte-urlaubsuebertragung`

**Fokus:** Skill zur Uebertragung und Abgeltung des Erholungsurlaubs bei laenger andauernder Erkrankung im Beamtenverhaeltnis. Klaert die 15-Monats-Frist nach EuGH-Rechtsprechung den unionsrechtlichen Mindesturlaub die Unterscheidung zwischen unionsrechtlich gewaehrtem Urlaub und nationalem Zusatzurlaub den Verzicht auf Verfall mangels Mitwirkungsobliegenheit sowie das Verhaeltnis zur Abgeltung bei Eintritt in den Ruhestand. Liefert Berechnungstabelle und Pruefraster.


# Krankheitsbedingte Urlaubsuebertragung

## 1. Zweck und Anwendungsfall

Skill fuer Beamte mit langjaehriger Erkrankung und entstehenden Resturlaubsanspruechen. Klaert, wie viel Urlaub noch besteht und wann er endgueltig verfaellt.

## 2. Eingaben

- Urlaubskonto
- Krankheitszeitraeume mit Daten
- Schwerbehindertenstatus (ggf. Zusatzurlaub)
- Wechselschicht- und Nachtdienste (ggf. Zusatzurlaub)
- Datum Wiederaufnahme oder Eintritt in den Ruhestand

## 3. Ablauf / Checkliste

### a) Unionsrechtlicher Mindesturlaub
- Vier Wochen pro Jahr.
- Verfaellt nicht automatisch bei Krankheit; nach EuGH Schultz-Hoff erst 15 Monate nach Ende des Urlaubsjahres.

### b) Zusatzurlaub
- Schwerbehindertenzusatzurlaub (§ 208 SGB IX) und Schichturlaub: getrennt zu betrachten, Verfall nach den jeweils einschlaegigen Vorschriften.

### c) Mitwirkungsobliegenheit
- Auch bei langer Krankheit greift die Mitwirkungsobliegenheit; Dienstherr muss spaetestens bei Wiederaufnahme klare Hinweise zum Resturlaub geben.

### d) Abgeltung
- Bei Eintritt in den Ruhestand oder anderen Beendigungstatbestaenden ist nicht verfallener Urlaub finanziell abzugelten.

### e) Berechnung
- Tabelle "Urlaubsjahr — Anspruch — genommen — uebertragen — verfallen — Stand".

## 4. Quellenpflicht

- Normen: Richtlinie 2003/88/EG; § 89 BBG; Erholungsurlaubsverordnung; § 208 SGB IX.
- Rspr.: EuGH Schultz-Hoff und Folgesachen, BVerwG zur Uebertragung bei Krankheit — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Berechnungstabelle Resturlaub.
- Antrag auf Gewaehrung oder Abgeltung.

## 6. Verifizierte Quellenanker

- Richtlinie 2003/88/EG Art. 7; EuGH C-350/06 (Schultz-Hoff), C-214/10 (KHS), C-684/16 (Max-Planck), C-518/20 (Fraport / Stadt Wuppertal).
- 15-Monats-Frist als zulaessige Uebertragungsobergrenze fuer den unionsrechtlichen Mindesturlaub.
- § 89 BBG; § 208 SGB IX; Erholungsurlaubsverordnung und landesrechtliche Aequivalente.
- Abgeltungspflicht bei Beendigung des Beamtenverhaeltnisses fuer den unionsrechtlich nicht verfallenen Mindesturlaub.
- BVerwG zur Uebertragung der Schultz-Hoff-Linie ins Beamtenverhaeltnis — Az vor Zitat live verifizieren.

## 7. Beispiel (Kurzfassung)

Mandantin 28 Monate Krankheit, in 2022 zehn Tage Urlaub genommen. Skill liefert Berechnung des unionsrechtlichen Mindesturlaubs fuer 2022, 2023 und 2024 unter Beruecksichtigung des Verfalls 15 Monate nach Urlaubsjahr.

## 2. `krankheitskosten-beihilfe-pkv-widerspruch`

**Fokus:** Krankheitskosten im Beamtenrecht: Beihilfe, PKV, ablehnender Beihilfebescheid, medizinische Notwendigkeit, Voranerkennung, Frist und Widerspruch.


# krankheitskosten-beihilfe-pkv-widerspruch

## Aufgabe

Führt Beamte und Versorgungsempfänger durch den Streit um konkrete Krankheitskosten.

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

## 3. `landesrecht-16-laender-routenplan`

**Fokus:** Routenplan für Landesbeamtenrecht aller 16 Länder: Landesbeamtengesetz, Laufbahn, Besoldung, Versorgung, Beihilfe, Disziplinarrecht und Landesrichterrecht ohne falsches Bundesrechts-Autopilotieren.


# Landesrecht - 16-Länder-Routenplan

## Ziel

Dieser Skill macht keine Scheinpräzision. Er führt durch die 16 Länder, fragt den Dienstherrn sauber ab und zwingt zur aktuellen Landesrechtsprüfung, bevor eine Norm oder Frist ausgegeben wird.

## Intake

- Bundesland.
- Dienstherr: Land, Kommune, Universität, Schule, Polizei, Justiz, Feuerwehr, Körperschaft.
- Status: Beamter, Richter, Professor, Anwärter, Wahlbeamter, Ruhestand.
- Thema: Laufbahn, Besoldung, Versorgung, Beihilfe, Disziplinarrecht, Personalvertretung.
- Existiert ein Bescheid mit Rechtsbehelfsbelehrung?

## Routenlogik

1. Landesbeamtengesetz für Statusdetails.
2. Landeslaufbahnverordnung / Laufbahngesetz für Qualifikation und Aufstieg.
3. Landesbesoldungsgesetz für Grundgehalt, Stufen, Zuschläge.
4. Landesversorgungsgesetz für Ruhegehalt und Hinterbliebene.
5. Landesdisziplinargesetz für Maßnahmen und Verfahren.
6. Landesrichtergesetz für Richterdienst, Präsidium, Dienstgericht und Beteiligungen.
7. Spezialrecht für Polizei, Schule, Hochschule, Kommunalwahlbeamte.

## Outputformen

- Landesrecht-Fundstellenliste mit Prüflinks.
- Fristenzettel nach Bescheiddatum.
- Mandantenbrief „Warum wir zuerst das Bundesland klären müssen".
- Behördenanschreiben zur Akteneinsicht oder Fristverlängerung.

## Gute Praxis

Bei jedem Land wird ausdrücklich offengelegt:

- „gesichert aus Bundesrecht";
- „landesrechtlich zu prüfen";
- „nur Verwaltungspraxis, keine Norm";
- „aktuelle Rechtsprechung nötig".

## Fehlervermeidung

Der Skill stoppt Ausgaben, wenn:

- Bundesland fehlt;
- nur „öffentlicher Dienst" genannt wird;
- Beamter und Tarifbeschäftigter vermischt werden;
- die Akte aus einem Stadtstaat stammt und Kommunal-/Landesebene unklar ist;
- altes BRRG/BBesG ohne Übergangsgrundlage benutzt werden soll.

## 4. `laufbahnrecht-bund`

**Fokus:** Laufbahnrecht Bund: Laufbahngruppen, Vorbereitungsdienst, Aufstieg, Laufbahnwechsel, Anerkennung von Zeiten und Qualifikation.


# Laufbahnrecht Bund

## Aufgabe

Laufbahnrecht Bund: Laufbahngruppen, Vorbereitungsdienst, Aufstieg, Laufbahnwechsel, Anerkennung von Zeiten und Qualifikation.

## Arbeitsweise

Arbeite mit Laufbahnverordnung und Ressortvorgaben. Prüfe Eingangsvoraussetzungen, Laufbahnbefähigung, Erprobung, Fortbildung und Auswahlentscheidung.

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
