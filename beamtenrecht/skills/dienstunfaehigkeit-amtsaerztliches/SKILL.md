---
name: dienstunfaehigkeit-amtsaerztliches
description: "Dienstunfaehigkeit Amtsaerztliches: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Dienstunfaehigkeit Amtsaerztliches

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Dienstunfaehigkeit Amtsaerztliches** im Plugin Beamtenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `dienstunfaehigkeit-amtsaerztliches-gutachten` | Skill zum amtsaerztlichen Gutachten im Verfahren der Dienstunfaehigkeit. Klaert die Mitwirkungspflicht des Beamten an der Untersuchung den Vorrang des amtsaerztlichen Gutachtens vor dem Privatgutachten die Anforderungen an Begruendung und Nachvollziehbarkeit den Anspruch auf Kenntnisnahme des Gutachtens den Schutzbereich des Personlichkeitsrechts und die Folgen der Verweigerung der Untersuchung. Liefert Pruefraster und Schriftsatzbausteine fuer Widerspruch und Klage. |
| `dienstunfaehigkeit-zurruhesetzung` | Dienstunfähigkeit und Zurruhesetzung: Prognose, amtsärztliches Gutachten, anderweitige Verwendung, Beteiligung und Rechtsschutz. |
| `dienstunfall-anerkennung` | Dienstunfall, Wegeunfall, psychische Dienstunfallfolgen und Unfallfürsorge. |
| `dienstunfall-anerkennung-45-beamtvg` | Skill zur Anerkennung von Dienstunfaellen nach § 31 BeamtVG und zur Einhaltung der Meldefristen nach § 45 BeamtVG. Klaert den Begriff des Dienstunfalls die Konstellation Wegeunfall die Behandlung von Spaetfolgen die Zwei-Jahres-Frist und die zehn-Jahres-Ausschlussfrist sowie die Glaubhaftmachung der Dienstunfallursaechlichkeit bei Vorerkrankungen. Liefert Pruefraster Antragsschriftbausteine und Hinweise zum amtsaerztlichen Gutachten und zur Beweislage. |

## Arbeitsweg

Im Plugin Beamten- und Richterdienstrecht gilt für **Dienstunfaehigkeit Amtsaerztliches**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `dienstunfaehigkeit-amtsaerztliches-gutachten`

**Fokus:** Skill zum amtsaerztlichen Gutachten im Verfahren der Dienstunfaehigkeit. Klaert die Mitwirkungspflicht des Beamten an der Untersuchung den Vorrang des amtsaerztlichen Gutachtens vor dem Privatgutachten die Anforderungen an Begruendung und Nachvollziehbarkeit den Anspruch auf Kenntnisnahme des Gutachtens den Schutzbereich des Personlichkeitsrechts und die Folgen der Verweigerung der Untersuchung. Liefert Pruefraster und Schriftsatzbausteine fuer Widerspruch und Klage.


# Amtsaerztliches Gutachten Dienstunfaehigkeit

## 1. Zweck und Anwendungsfall

Skill fuer Beamte im Verfahren zur Feststellung der Dienstunfaehigkeit, insbesondere im Streit ueber Auswahl, Reichweite und Verwertbarkeit des amtsaerztlichen Gutachtens.

## 2. Eingaben

- Untersuchungsaufforderung des Dienstherrn
- Amtsaerztliches Gutachten (falls vorliegend)
- Eigenes Privatgutachten
- Mandantenmitteilung zur Mitwirkung

## 3. Ablauf / Checkliste

### a) Untersuchungsaufforderung
- Schriftliche, hinreichend bestimmte Aufforderung mit Angabe des konkreten Anlasses, der Untersuchungsstelle, des Umfangs der Untersuchung und der Folgen unterlassener Mitwirkung.
- Pauschale oder unbestimmte Aufforderungen sind rechtswidrig (BVerwG-Rechtsprechung, konkret vor Zitat frei prüfen).

### b) Mitwirkungspflicht
- Beamter ist verpflichtet, sich der amtsaerztlichen Untersuchung zu unterziehen (§ 44 BBG).
- Verweigerung kann zu Ruhestandsversetzung gemaess Vermutungsregelung fuehren.

### c) Vorrang des amtsaerztlichen Gutachtens
- Im Konfliktfall zwischen amtsaerztlichem Gutachten und Privatgutachten genuesst das amtsaerztliche Gutachten regelmaessig groesseres Gewicht; Vorrang aber nicht absolut, sondern nur bei methodisch gleichwertiger Erstellung.

### d) Inhaltliche Anforderungen
- Nachvollziehbare Begruendung, ausdifferenzierte Stellungnahme zur Restdienstfaehigkeit, anderweitige Verwendung, Reaktivierungschance.
- Bloss formelhaftes Ergebnis genuegt nicht.

### e) Akteneinsicht
- Beamter hat Anspruch auf Akteneinsicht und Mitteilung des Gutachteninhalts (§ 110 BBG; landesrechtliche Aequivalente).
- Persoenlichkeitsrechte sind durch geeignete Aufbereitung zu wahren.

## 4. Quellenpflicht

- Normen: §§ 26, 44, 110 BBG; § 26 BeamtStG i.V.m. Landesrecht; Art. 2 Abs. 1, Art. 1 Abs. 1 GG.
- Rspr.: BVerwG zur Untersuchungsaufforderung und zum Vorrang des amtsaerztlichen Gutachtens — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Widerspruch gegen Untersuchungsaufforderung.
- Schriftsatz gegen Ruhestandsbescheid.

## 6. Verifizierte Quellenanker

- §§ 44 bis 48 BBG (Dienstunfaehigkeit, begrenzte Dienstfaehigkeit, Wiederherstellung, Verfahren, aerztliche Untersuchung); § 110 BBG (Akteneinsicht); § 26 BeamtStG i.V.m. Landesrecht.
- Art. 2 Abs. 1, Art. 1 Abs. 1 GG (Persoenlichkeitsrecht) als Schranke der Untersuchungsanordnung.
- Anforderung an Bestimmtheit der Untersuchungsaufforderung: konkreter Anlass, Untersuchungsstelle, Umfang, Folgen unterlassener Mitwirkung.
- BVerwG zur Bestimmtheit der Untersuchungsaufforderung und zum Vorrang des amtsaerztlichen Gutachtens — Datum und Az vor Zitat live verifizieren.
- Akteneinsicht und Kenntnisnahme des Gutachtens nach § 110 BBG sowie landesrechtlichen Aequivalenten.

## 7. Beispiel (Kurzfassung)

Mandant erhaelt pauschale Aufforderung zur Untersuchung "wegen wiederholter Erkrankung". Skill liefert Widerspruch gegen Aufforderung wegen mangelnder Bestimmtheit und Pruefraster.

## 2. `dienstunfaehigkeit-zurruhesetzung`

**Fokus:** Dienstunfähigkeit und Zurruhesetzung: Prognose, amtsärztliches Gutachten, anderweitige Verwendung, Beteiligung und Rechtsschutz.


# Dienstunfaehigkeit Zurruhesetzung

## Aufgabe

Dienstunfähigkeit und Zurruhesetzung: Prognose, amtsärztliches Gutachten, anderweitige Verwendung, Beteiligung und Rechtsschutz.

## Arbeitsweise

Prüfe Gesundheitsstatus, Gutachtenqualität, Prognose, Rehabilitationspflicht, anderweitige Verwendung und Verfahrensbeteiligte.

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

## 3. `dienstunfall-anerkennung`

**Fokus:** Dienstunfall, Wegeunfall, psychische Dienstunfallfolgen und Unfallfürsorge.


# Dienstunfall Anerkennung

## Aufgabe

Dienstunfall, Wegeunfall, psychische Dienstunfallfolgen und Unfallfürsorge.

## Arbeitsweise

Erhebe Ereignis, Ort, Zeit, dienstliche Verrichtung, Kausalität, Meldedatum, ärztliche Unterlagen. Output: Anerkennungsantrag oder Widerspruch.

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

## 4. `dienstunfall-anerkennung-45-beamtvg`

**Fokus:** Skill zur Anerkennung von Dienstunfaellen nach § 31 BeamtVG und zur Einhaltung der Meldefristen nach § 45 BeamtVG. Klaert den Begriff des Dienstunfalls die Konstellation Wegeunfall die Behandlung von Spaetfolgen die Zwei-Jahres-Frist und die zehn-Jahres-Ausschlussfrist sowie die Glaubhaftmachung der Dienstunfallursaechlichkeit bei Vorerkrankungen. Liefert Pruefraster Antragsschriftbausteine und Hinweise zum amtsaerztlichen Gutachten und zur Beweislage.


# Dienstunfall — Anerkennung und Meldefristen

## 1. Zweck und Anwendungsfall

Skill fuer Beamte mit Dienstunfaellen oder dem Verdacht, dass eine gesundheitliche Beeintraechtigung dienstunfallbedingt ist. Hilft bei rechtzeitiger Meldung und bei Streit um die Anerkennung.

## 2. Eingaben

- Datum des Vorfalls
- Ort und genaue Schilderung des Ereignisses
- Zeugen
- Aerztliche Unterlagen
- Datum der ersten Meldung an den Dienstherrn

## 3. Ablauf / Checkliste

### a) Dienstunfallbegriff
- § 31 BeamtVG: ein auf aeussere Einwirkung beruhendes, ploetzliches, oertlich und zeitlich bestimmtes, einen Koerperschaden verursachendes Ereignis in Ausuebung oder infolge des Dienstes.
- Wegeunfaelle nach § 31 Abs. 2 BeamtVG (Hin- und Rueckweg).

### b) Meldefristen § 45 BeamtVG
- Schriftliche Meldung innerhalb von zwei Jahren ab dem Unfall.
- Bei Spaetfolgen oder verspaeteter Erkennbarkeit: Frist beginnt mit Kenntnis; absolute Ausschlussfrist zehn Jahre.

### c) Vorerkrankungen
- Vorerkrankungen schliessen Anerkennung nicht aus, soweit der Unfall mit Wahrscheinlichkeit eine wesentliche Mitursache fuer die Verschlechterung war.
- Massgeblich ist die "rechtlich wesentliche Mitursache" (BVerwG-Rechtsprechung, konkret vor Zitat frei prüfen).

### d) Beweislast
- Grundsaetzlich Beweislast beim Beamten; an die Glaubhaftmachung des Unfallhergangs sind im Eilrechtsschutz keine ueberhoehten Anforderungen zu stellen.

### e) Folgen der Anerkennung
- Unfallfuersorge: Unfallruhegehalt, Heilverfahrenskosten, Pflegezulage, Unterhaltsbeitrag, einmalige Unfallentschaedigung — Skill `unfallruhegehalt-36-beamtvg`.

## 4. Quellenpflicht

- Normen: §§ 30 bis 47 BeamtVG; landesrechtliche Aequivalente.
- Rspr.: BVerwG zum Dienstunfallbegriff und zur Kausalitaet — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 5. Ausgabeformat

- Schriftliche Dienstunfallmeldung.
- Pruefraster fuer Spaetfolgenmeldungen.

## 6. Verifizierte Quellenanker

- § 31 BeamtVG (Dienstunfallbegriff); § 31 Abs. 2 BeamtVG (Wegeunfall); § 45 BeamtVG (Meldefristen zwei Jahre / zehn Jahre).
- §§ 30 bis 47 BeamtVG (Unfallfuersorge insgesamt).
- Massgeblich Lehre der rechtlich wesentlichen Mitursache; konstante Linie des BVerwG zur Kausalitaetspruefung.
- BVerwG zum Dienstunfallbegriff und zur Kausalitaetsfrage — Datum und Az vor Zitat live verifizieren.

## 7. Beispiel (Kurzfassung)

Mandantin Lehrerin stuerzt im Klassenzimmer; zunaechst nur Hautabschuerfung, drei Jahre spaeter Bandscheibenschaden mit gutachterlich nachgewiesener Mitursache. Skill liefert Spaetfolgenmeldung innerhalb der Zehn-Jahres-Frist mit Kausalitaetsbegruendung.
