---
name: richterdienstgericht-rechtswegabgrenzung
description: "Richterdienstgericht Rechtswegabgrenzung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Richterdienstgericht Rechtswegabgrenzung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Richterdienstgericht Rechtswegabgrenzung** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `richterdienstgericht-und-rechtswegabgrenzung` | Richterdienstgerichte und Rechtsweg: DRiG, Landesrichterrecht, Dienstaufsichtsmaßnahme, Statusstreit, Beurteilung, Beihilfe, Versorgung, Präsidium und Verwaltungsgerichtsbarkeit trennen. |
| `richterliche-unabhaengigkeit-dienstaufsicht` | Richterliche Unabhängigkeit, Dienstaufsicht, Ermahnung, Geschäftsprüfung und unzulässige Einflussnahme. |
| `richterwahl-art-33-ii-und-praesidialrat` | Richterwahl, Art. 33 Abs. 2 GG, Richterwahlausschuss, Präsidialrat, Bundesrichterwahl, Begründungspflichten, Konkurrentenstreit und politische Wahlspielräume. |
| `ruhensregelung-53-beamtvg` | Skill zur Ruhensregelung von Versorgungsbezuegen bei Erwerbseinkommen nach § 53 BeamtVG. Klaert Hinzuverdienstgrenze fuer Ruhestandsbeamte unterschiedliche Grenzen vor und nach Erreichen der Regelaltersgrenze Anrechnung von Verwendungseinkommen aus dem oeffentlichen Dienst und Erwerbsersatzeinkommen wie Krankengeld oder Arbeitslosengeld. Behandelt Sonderfaelle wie Tantiemen Aktienoptionen Honorare als Sachverstaendiger und Beratungseinkommen. Liefert Pruefraster und Antragsbausteine. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Richterdienstgericht Rechtswegabgrenzung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `richterdienstgericht-und-rechtswegabgrenzung`

**Fokus:** Richterdienstgerichte und Rechtsweg: DRiG, Landesrichterrecht, Dienstaufsichtsmaßnahme, Statusstreit, Beurteilung, Beihilfe, Versorgung, Präsidium und Verwaltungsgerichtsbarkeit trennen.


# Richterdienstgericht oder Verwaltungsgericht?

## Problem

Nicht jeder Streit eines Richters gehört zum Richterdienstgericht. Nicht jeder Streit über Dienstaufsicht gehört zur Verwaltungsgerichtsbarkeit. Dieser Skill klärt den Rechtsweg, bevor ein Schriftsatz entsteht.

## Entscheidungsbaum

1. Geht es um einen Eingriff in richterliche Unabhängigkeit?
 - Dann Richterdienstgericht prüfen.
2. Geht es um Status, Ernennung, Versetzung, Entlassung, Disziplinarrecht?
 - Spezialzuständigkeiten nach DRiG/Landesrichtergesetz prüfen.
3. Geht es um Beihilfe, Besoldung, Versorgung, Reisekosten?
 - Häufig Verwaltungsgerichtsbarkeit, aber Landesrecht prüfen.
4. Geht es um Geschäftsverteilung?
 - Präsidialverfassung, gesetzlicher Richter, konkretes Verfahren und Rechtsschutzlage trennen.
5. Geht es um Beurteilung/Beförderung?
 - Art. 33 Abs. 2 GG, Präsidialrat/Richterwahlausschuss und Rechtsweg prüfen.

## Intake

- Bundesrichter oder Landesrichter?
- Gerichtsbarkeit und Bundesland.
- Maßnahme und Datum.
- Gibt es Rechtsbehelfsbelehrung?
- Wurde Präsidium, Präsidialrat oder Richterrat beteiligt?
- Ziel: Aufhebung, Feststellung, Unterlassung, Beförderung, Akteneinsicht?

## Output

Der Skill erstellt:

- Rechtsweg-Memo;
- Fristenzettel;
- Klage-/Antragsskizze;
- Risiko „falsches Gericht";
- Liste fehlender Unterlagen.

## Warnung

Der Skill darf keine pauschalen Aussagen wie „Richter gehen immer zum Richterdienstgericht" ausgeben. Maßgeblich ist die konkrete Maßnahme und das jeweilige Bundes-/Landesrichterrecht.

## 2. `richterliche-unabhaengigkeit-dienstaufsicht`

**Fokus:** Richterliche Unabhängigkeit, Dienstaufsicht, Ermahnung, Geschäftsprüfung und unzulässige Einflussnahme.


# Richterliche Unabhaengigkeit Dienstaufsicht

## Aufgabe

Richterliche Unabhängigkeit, Dienstaufsicht, Ermahnung, Geschäftsprüfung und unzulässige Einflussnahme.

## Arbeitsweise

Trenne sachliche Unabhängigkeit von Dienstaufsicht. Prüfe, ob Kritik Organisation/Verhalten oder Spruchinhalt betrifft. Output: Gegenvorstellung oder Dienstaufsichtsmemo.

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

## 3. `richterwahl-art-33-ii-und-praesidialrat`

**Fokus:** Richterwahl, Art. 33 Abs. 2 GG, Richterwahlausschuss, Präsidialrat, Bundesrichterwahl, Begründungspflichten, Konkurrentenstreit und politische Wahlspielräume.


# Richterwahl, Bestenauslese und Präsidialrat

## Zweck

Richterwahlen verbinden Bestenauslese, demokratische Legitimation und institutionelle Unabhängigkeit. Dieser Skill verhindert zwei Fehler: reine Politik ohne Art. 33 Abs. 2 GG und schematische Bestenauslese ohne Wahlspielraum.

## Intake

- Bundesrichter oder Landesrichter?
- Welches Gericht und welche Besoldungsgruppe?
- Ausschreibung, Vorschlagsliste, Beurteilungen, Präsidialratsvotum vorhanden?
- Auswahlentscheidung schriftlich begründet?
- Unterlegener Bewerber will Eilrechtsschutz?

## Prüfroute

1. Anforderungsprofil und Auswahlmaßstab.
2. Aktuelle Beurteilungen und Anlassbeurteilungen.
3. Präsidialrat/Richterwahlausschuss: Zusammensetzung, Beteiligung, Votum.
4. Art. 33 Abs. 2 GG: Eignung, Befähigung, fachliche Leistung.
5. Politische Wahlentscheidung: Raum, Grenze, Begründung.
6. Rechtsschutz: Konkurrentenmitteilung, Wartefrist, Eilantrag.

## Bundesrichterwahl

Bei Bundesrichtern wirken Richterwahlausschuss und zuständiger Bundesminister zusammen. Der Skill prüft, ob Art. 33 Abs. 2 GG sichtbar verarbeitet wurde und ob eine Ablehnung nachvollziehbar begründet ist.

## Output

- Auswahlvermerk-Check.
- Eilantrag gegen Ernennung.
- Behörden-/Ministeriumsvermerk.
- Mandantenbrief für Bewerber.
- Fragenkatalog an Präsidialrat/Richterwahlausschuss.

## Rechtsprechungsanker

BVerfG 20.09.2016 - 2 BvR 2453/15 zur Bundesrichterwahl. Bei Konkurrentenstreit zusätzlich einschlägige verwaltungsgerichtliche Rechtsprechung live prüfen.

## 4. `ruhensregelung-53-beamtvg`

**Fokus:** Skill zur Ruhensregelung von Versorgungsbezuegen bei Erwerbseinkommen nach § 53 BeamtVG. Klaert Hinzuverdienstgrenze fuer Ruhestandsbeamte unterschiedliche Grenzen vor und nach Erreichen der Regelaltersgrenze Anrechnung von Verwendungseinkommen aus dem oeffentlichen Dienst und Erwerbsersatzeinkommen wie Krankengeld oder Arbeitslosengeld. Behandelt Sonderfaelle wie Tantiemen Aktienoptionen Honorare als Sachverstaendiger und Beratungseinkommen. Liefert Pruefraster und Antragsbausteine.


# Ruhensregelung Versorgungsbezuege § 53 BeamtVG

## 1. Zweck und Anwendungsfall

Skill fuer Ruhestandsbeamte mit Nebenerwerbseinkommen. Klaert, ob und in welcher Hoehe Versorgungsbezuege gekuerzt werden, wenn der Versorgungsempfaenger Einkommen aus selbststaendiger oder nichtselbststaendiger Erwerbstaetigkeit erzielt.

## 2. Eingaben

- Ruhestandsbescheid und Versorgungsbezuegemitteilung
- Datum Eintritt in den Ruhestand (regulaerer Ruhestand vor Regelaltersgrenze, Ruhestand wegen Dienstunfaehigkeit)
- Art und Hoehe des Erwerbseinkommens
- Datum des Beginns des Erwerbseinkommens
- Arbeitgeber im oeffentlichen Dienst oder Privatwirtschaft

## 3. Ablauf / Checkliste

### a) Grundprinzip
- Versorgungsbezuege werden bis zur Hoehe einer Hoechstgrenze geschmaelert, wenn der Versorgungsempfaenger Erwerbs- oder Erwerbsersatzeinkommen bezieht.

### b) Hoechstgrenze
- Hoechstgrenze typischerweise die ruhegehaltfaehigen Dienstbezuege zum Zeitpunkt des Eintritts in den Ruhestand. Bei Dienstunfaehigkeitsruhestand vor Regelaltersgrenze gelten besondere Grenzen.

### c) Anrechnungsfreies Einkommen
- Bestimmte Einkommen wie Aufwandsentschaedigungen, ehrenamtliche Taetigkeiten und teilweise wissenschaftliche Lehrtaetigkeiten sind nicht anrechenbar.

### d) Verwendungseinkommen
- Einkommen aus Beschaeftigung im oeffentlichen Dienst wird in vollem Umfang angerechnet (§ 53 BeamtVG zusammen mit § 56).

### e) Endgueltige Berechnung
- Nach Erreichen der Regelaltersgrenze entfaellt die Anrechnung weitgehend (Ausnahmen pruefen).
- Beginn und Ende der Hinzuverdienstphase exakt dokumentieren.

## 4. Quellenpflicht

- Normen: § 53 BeamtVG; § 56 BeamtVG; landesrechtliche Aequivalente.
- Rspr.: BVerwG zur Ruhensregelung — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Tabelle "Monat — Bezuege Brutto — Erwerbseinkommen — Hoechstgrenze — Ruhensbetrag — Auszahlung".
- Beratungsschreiben fuer Mandanten zur Entscheidung ueber Aufnahme einer Erwerbstaetigkeit.

## 6. Verifizierte Quellenanker

- BeamtVG und jeweiliges Landesversorgungsrecht sauber trennen; Versorgung ist bei Landesbeamten seit der Föderalismusreform grundsätzlich Landesrecht.
- BVerfG, 27.09.2005 - 2 BvR 1387/02: Versorgungsänderungsrecht und Alimentationsprinzip als verfassungsrechtlicher Anker.
- BVerfG, 20.03.2007 - 2 BvL 11/04: Versorgung aus dem letzten Amt und Wartefrist.
- BVerwG, 25.10.2018 - 2 C 33.17 sowie BVerwG, 30.10.2018 - 2 C 32.17 als verifizierte Anker für Besoldungs-/Versorgungsvorlagen; Reichweite auf konkrete Versorgungsfrage jeweils prüfen.
- Konkrete Berechnung nie aus Modellwissen: Bescheid, Dienstzeiten, Ruhensnormen, Rentenbescheide und Landesrecht in Tabelle nachziehen.

## 7. Beispiel (Kurzfassung)

Ruhestandsbeamter A14 mit 60 Jahren wegen Dienstunfaehigkeit, beraten Honorarvertrag fuer Beratung beim Wirtschaftspruefer. Skill liefert Ruhensberechnung und Gestaltungshinweise.
