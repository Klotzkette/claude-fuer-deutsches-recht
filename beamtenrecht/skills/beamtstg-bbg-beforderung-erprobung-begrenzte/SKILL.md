---
name: beamtstg-bbg-beforderung-erprobung-begrenzte
description: "Beamtstg BBG Beforderung Erprobung Begrenzte: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Beamtstg BBG Beforderung Erprobung Begrenzte

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Beamtstg BBG Beforderung Erprobung Begrenzte** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `beamtstg-bbg-landesrecht-abgrenzung` | Trennt BeamtStG, BBG, Landesbeamtengesetze und kommunale Sonderregeln; verhindert falsche Normenwahl bei Status, Pflichten, Versetzung, Entlassung und Dienstvergehen. |
| `beforderung-und-erprobung` | Beförderung, Erprobung, Sperrzeiten, Wartezeiten und Beförderungsdienstposten. |
| `begrenzte-dienstfaehigkeit-27-bbg` | Skill zur begrenzten Dienstfaehigkeit nach § 27 BBG bzw. § 27 BeamtStG. Klaert die Voraussetzungen fuer die Reduzierung der Arbeitszeit anstatt Versetzung in den Ruhestand das Verhaeltnis zu § 26 BBG Dienstunfaehigkeit die Bezuegehoehe bei begrenzter Dienstfaehigkeit und die Auswirkungen auf die Versorgungsanwartschaft. Behandelt das praktische Vorgehen amtsaerztliches Gutachten Pruefung anderweitiger Verwendung Beruecksichtigung der Belange des Beamten. Liefert Pruefraster und Schriftsatzbausteine. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Beamtstg BBG Beforderung Erprobung Begrenzte**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `beamtstg-bbg-landesrecht-abgrenzung`

**Fokus:** Trennt BeamtStG, BBG, Landesbeamtengesetze und kommunale Sonderregeln; verhindert falsche Normenwahl bei Status, Pflichten, Versetzung, Entlassung und Dienstvergehen.


# BeamtStG, BBG und Landesrecht richtig abgrenzen

## Einstieg

Der Skill fragt zuerst:

- Wer ist Dienstherr?
- Handelt die Bundesbehörde, ein Land, eine Kommune, Universität, Kammer, Rundfunkanstalt oder sonstige Körperschaft?
- Geht es um Statusrechte oder um Laufbahn/Besoldung/Versorgung?
- Gibt es eine Speziallaufbahn: Polizei, Schule, Justizvollzug, Feuerwehr, Steuerverwaltung, Hochschule?

## Grundsätze

Das BeamtStG ist kein vollständiges Beamtenhandbuch. Es setzt gemeinsame statusrechtliche Eckpunkte für Landes- und Kommunalbeamte. Details der Laufbahn, Besoldung, Versorgung und des Verfahrens stehen in Landesgesetzen. Für Bundesbeamte ist das BBG Ausgangspunkt; daneben stehen BBesG, BeamtVG, BDG und Laufbahnverordnungen.

## Abgrenzungsfragen

### Status

- Ernennung, Beamtenverhältnis auf Widerruf/Probe/Lebenszeit/Zeit.
- Pflichten, Treue, Mäßigung, Dienstvergehen.
- Entlassung, Verlust der Beamtenrechte, Ruhestand.

### Laufbahn

- Vorbildung, Laufbahngruppe, Fachrichtung.
- Aufstieg, Anerkennung, Probezeit.
- Landesrechtliche Öffnungen.

### Besoldung und Versorgung

- Seit 2006 bei Landesbeamten überwiegend Landesrecht.
- Bundesrecht nur beim Bund und für fortgeltende Übergangslagen.

## Praktische Ausgabe

Der Skill erzeugt eine Normenampel:

| Farbe | Bedeutung |
| --- | --- |
| Grün | Norm ist sehr wahrscheinlich einschlägig, muss aber in aktueller Fassung geprüft werden. |
| Gelb | Norm kann einschlägig sein, hängt an Status/Bundesland/Sonderlaufbahn. |
| Rot | Norm gehört zu anderem Dienstherrn oder falscher Materie. |

## Mini-Check gegen Halluzination

Wenn der Nutzer ein Aktenzeichen, eine Behördennorm oder eine Verwaltungsvorschrift nennt, prüft der Skill:

- Passt die Norm zum Bundesland?
- Gibt es eine amtliche Quelle?
- Ist das Zitat nur aus einer privaten Datenbank?
- Wird eine Verwaltungsvorschrift fälschlich wie ein Gesetz behandelt?

## 2. `beforderung-und-erprobung`

**Fokus:** Beförderung, Erprobung, Sperrzeiten, Wartezeiten und Beförderungsdienstposten.


# Beforderung Und Erprobung

## Aufgabe

Beförderung, Erprobung, Sperrzeiten, Wartezeiten und Beförderungsdienstposten.

## Arbeitsweise

Trenne Statusverleihung von Dienstpostenübertragung. Prüfe laufbahnrechtliche Wartezeiten, Erprobung, Haushaltstelle und Beteiligung von Personalrat/Gleichstellung/Schwerbehindertenvertretung.

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

## 3. `begrenzte-dienstfaehigkeit-27-bbg`

**Fokus:** Skill zur begrenzten Dienstfaehigkeit nach § 27 BBG bzw. § 27 BeamtStG. Klaert die Voraussetzungen fuer die Reduzierung der Arbeitszeit anstatt Versetzung in den Ruhestand das Verhaeltnis zu § 26 BBG Dienstunfaehigkeit die Bezuegehoehe bei begrenzter Dienstfaehigkeit und die Auswirkungen auf die Versorgungsanwartschaft. Behandelt das praktische Vorgehen amtsaerztliches Gutachten Pruefung anderweitiger Verwendung Beruecksichtigung der Belange des Beamten. Liefert Pruefraster und Schriftsatzbausteine.


# Begrenzte Dienstfaehigkeit nach § 27 BBG

## 1. Zweck und Anwendungsfall

Skill fuer Beamte, deren Dienstfaehigkeit eingeschraenkt, aber nicht vollstaendig verloren ist. Anwendung als milderer Eingriff im Verhaeltnis zur Versetzung in den Ruhestand nach § 26 BBG.

## 2. Eingaben

- Amtsaerztliches Gutachten
- Dienstpostenbeschreibung
- Vorgesehene Verwendung (anderer Dienstposten?)
- Stellungnahme des Mandanten

## 3. Ablauf / Checkliste

### a) Voraussetzungen § 27 BBG
- Beamter ist nicht vollstaendig dienstunfaehig.
- Restliche Dienstleistung ist mit mindestens 50 v. H. der Arbeitszeit moeglich.
- Andersweitige Verwendung im Sinne § 26 Abs. 2 BBG ist zu pruefen.

### b) Verhaeltnis zu § 26 BBG
- § 27 BBG ist die mildere Maszahme; Vorrang vor Versetzung in den Ruhestand.
- Dienstherr ist verpflichtet, die Moeglichkeit der begrenzten Dienstfaehigkeit zu pruefen.

### c) Bezuege
- Bezuege werden anteilig der herabgesetzten Arbeitszeit gezahlt; ggf. Ausgleichszahlung nach den landesrechtlichen Vorschriften.

### d) Versorgungsanwartschaft
- Die Zeit der begrenzten Dienstfaehigkeit ist anteilig ruhegehaltfaehig.
- Sondervorschriften zur Hochrechnung bei spaeterer Versetzung in den Ruhestand.

### e) Verfahrensschritte
- Amtsaerztliches Gutachten.
- Anhoerung Mandant.
- Bescheid; Rechtsschutz Widerspruch und Klage.

## 4. Quellenpflicht

- Normen: § 27 BBG; § 27 BeamtStG i.V.m. Landesrecht; § 26 BBG.
- Rspr.: BVerwG zur begrenzten Dienstfaehigkeit — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Antrag oder Widerspruch.
- Berechnung der reduzierten Bezuege und Versorgungsfolgen.

## 6. Verifizierte Quellenanker

- § 45 BBG (begrenzte Dienstfaehigkeit Bund); § 27 BeamtStG i.V.m. Landesrecht.
- § 44 BBG (Dienstunfaehigkeit) als Vergleichsmassstab; § 6 BeamtVG (anteilige Ruhegehaltfaehigkeit).
- Vorrang der milderen Massnahme: anderweitige Verwendung und begrenzte Dienstfaehigkeit vor Ruhestandsversetzung.
- BVerwG zur begrenzten Dienstfaehigkeit und zur Pruefungspflicht anderweitiger Verwendung — Datum und Az vor Zitat live verifizieren.

## 7. Beispiel (Kurzfassung)

Mandantin Polizeikommissarin mit Bandscheibenleiden, Innen- statt Streifendienst denkbar. Dienstherr will Ruhestand verfuegen. Skill liefert Antrag auf begrenzte Dienstfaehigkeit und Pruefraster anderweitiger Verwendung.
