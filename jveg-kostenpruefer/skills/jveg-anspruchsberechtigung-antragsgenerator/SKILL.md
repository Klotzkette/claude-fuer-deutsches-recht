---
name: jveg-anspruchsberechtigung-antragsgenerator
description: "Anspruchsberechtigung Antragsgenerator: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Anspruchsberechtigung Antragsgenerator

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Anspruchsberechtigung Antragsgenerator** im Plugin JVEG-Kostenprüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `jveg-anspruchsberechtigung` | Anspruchsberechtigung nach JVEG prüfen: Sachverständiger, Zeuge, Dolmetscher, Anwalt. Normen: §§ 1 2 JVEG. Prüfraster: Personenkategorie, Beauftragung durch Gericht, Verfahrensart. Output: Prüfergebnis Anspruchsberechtigung JVEG. Abgrenzung: nicht Verguetungsberechnung. |
| `jveg-antragsgenerator` | Antrag auf gerichtliche Kostenfestsetzung nach JVEG erstellen: Verguetungsantrag, Anlagen, Fristen. Normen: §§ 2 4 JVEG. Prüfraster: Antragsfrist, Formerfordernis, Anlagenliste. Output: Kostenfestsetzungsantrag nach JVEG. Abgrenzung: nicht Beschwerde gegen Festsetzung. |
| `jveg-dolmetscher-uebersetzer` | Verguetung für gerichtliche Dolmetscher und Übersetzer nach JVEG berechnen. Normen: §§ 9 11 JVEG, Anlage 1 JVEG. Prüfraster: Stundenverguetung, Mindestwartezeit, Anfahrt, schriftliche Übersetzung je Seite. Output: Verguetungsberechnung Dolmetscher und Übersetzer. Abgrenzung: nicht Sachverständigenverguetung. |

## Arbeitsweg

Im Plugin JVEG-Kostenprüfer gilt für **Anspruchsberechtigung Antragsgenerator**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `jveg-anspruchsberechtigung`

**Fokus:** Anspruchsberechtigung nach JVEG prüfen: Sachverständiger, Zeuge, Dolmetscher, Anwalt. Normen: §§ 1 2 JVEG. Prüfraster: Personenkategorie, Beauftragung durch Gericht, Verfahrensart. Output: Prüfergebnis Anspruchsberechtigung JVEG. Abgrenzung: nicht Verguetungsberechnung.

# JVEG-Anspruchsberechtigung

## Fachkern: JVEG-Anspruchsberechtigung
- **Spezialgegenstand:** JVEG-Anspruchsberechtigung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Kläre, welche Person nach § 2 JVEG anspruchsberechtigt ist, und ordne die Vergütungsgrundlage (Sachverständiger, Zeuge, Dolmetscher usw.) der richtigen Normengruppe zu.

## Triage — kläre vor der Prüfung

1. **Rolle der Person:** Sachverständiger, Zeuge, Dritter, Dolmetscher, Übersetzer, Protokollperson oder ehrenamtlicher Richter?
2. **Beauftragung:** Liegt eine gerichtliche Beauftragung oder Ladung vor (§ 1 JVEG)?
3. **Verfahrensart:** Zivilverfahren, Strafverfahren, Verwaltungsverfahren?
4. **Mehrfachrollen:** Hat die Person mehrere Funktionen in einem Verfahren (z.B. Sachverständiger und Zeuge)?
5. **Dritterstattung:** Soll eine Dritte Person (§ 2 Abs. 2 JVEG) geltend machen?

## Zentrale Normen
- § 1 JVEG (Anwendungsbereich)
- § 2 JVEG (Anspruchsberechtigte: Sachverständige, Dolmetscher, Übersetzer, Protokollpersonen, ehrenamtliche Richter, Zeugen, Dritte)
- § 19 JVEG (Zeugenfahrtkosten)
- § 22 JVEG (Zeitversäumnis des Zeugen)
- § 13 JVEG (Dolmetscher)
- § 8 JVEG (Sachverständigenvergütung)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Eingang eines JVEG-Antrags oder einer Rechnung, wenn die Rolle der anspruchsberechtigten Person unklar ist.

## Arbeitsweise
1. Ladungs- oder Bestellungsdokument auswerten.
2. Rolle nach § 2 JVEG zuordnen.
3. Bei Mehrfachrolle: Abgrenzung prüfen, keine Doppelerstattung.
4. Zutreffende Normenkette für nachgelagerte Prüfung benennen.

## Output-Template

| Kriterium | Befund |
|---|---|
| Person | [Name/Bezeichnung] |
| Rolle nach § 2 JVEG | [Sachverständiger / Zeuge / Dolmetscher / …] |
| Beauftragungsdokument | [Aktenzeichen, Datum] |
| Maßgebliche Normen | [§§ …] |
| Mehrfachrolle | [Ja / Nein — Begründung] |
| Ergebnis | [Anspruchsberechtigung bejaht / verneint] |

## Ausgabe
Rollenzuordnung mit Normenbegründung; Weiterleitung an spezifische Vergütungsprüf-Skills.

## Leitplanken
- Rollenzuordnung ist abschließend nach § 2 JVEG; keine analoge Ausweitung.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.

## 2. `jveg-antragsgenerator`

**Fokus:** Antrag auf gerichtliche Kostenfestsetzung nach JVEG erstellen: Verguetungsantrag, Anlagen, Fristen. Normen: §§ 2 4 JVEG. Prüfraster: Antragsfrist, Formerfordernis, Anlagenliste. Output: Kostenfestsetzungsantrag nach JVEG. Abgrenzung: nicht Beschwerde gegen Festsetzung.

# JVEG-Antragsgenerator

## Fachkern: JVEG-Antragsgenerator
- **Spezialgegenstand:** JVEG-Antragsgenerator wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Erstelle druckfertige JVEG-Antragsschreiben (Vorschuss, Nachzahlung, Festsetzung, Ergänzung) mit vollständiger Anlagen- und Belegliste.

## Triage — kläre vor der Erstellung

1. **Antragsart:** Vorschuss (§ 3 JVEG), Nachzahlung, Festsetzungsantrag (§ 4 JVEG) oder Ergänzungsantrag?
2. **Anspruchsberechtigter:** Sachverständiger, Zeuge, Dolmetscher oder Übersetzer?
3. **Fristen:** Ist die Dreimonatsfrist des § 23 JVEG noch nicht abgelaufen?
4. **Beleglage:** Welche Belege (Fahrtkosten, Zeitnachweise, Rechnungen) liegen vor und sollen beigefügt werden?
5. **Vorschussstand:** Wurde bereits ein Vorschuss gewährt — wie hoch und wann ausgezahlt?

## Zentrale Normen
- § 3 JVEG (Vorschuss)
- § 4 JVEG (Festsetzung durch das Gericht)
- § 4 Abs. 3 JVEG (Beschwerde gegen Festsetzungsbeschluss)
- § 23 JVEG (Dreimonatsfrist / Erlöschen)
- §§ 5–7 JVEG (Fahrtkosten)
- §§ 8–10 JVEG (Sachverständige)
- §§ 13–16 JVEG (Dolmetscher/Übersetzer)
- §§ 19–22 JVEG (Zeugen)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Mandant oder Sachverständiger möchte JVEG-Vergütung gerichtlich festsetzen lassen oder Vorschuss beantragen.

## Arbeitsweise
1. Antragsart und Anspruchsgrundlage bestimmen.
2. Alle Positionen mit Normbezug und Belegverweis auflisten.
3. Frist § 23 JVEG prüfen und im Schreiben dokumentieren.
4. Anlagenliste mit Belegnummern erstellen.
5. Druckfertiges Schreiben mit Adresse, Aktenzeichen, Datum und Antragstellung formulieren.

## Output-Template

**[Gericht / Kostenbeamter]**
**Az.:** [Aktenzeichen]
**Datum:** [TT.MM.JJJJ]

**Antrag auf [Festsetzung / Vorschuss / Nachzahlung] nach JVEG**

Ich beantrage die Festsetzung folgender Vergütung:

| Position | Betrag (EUR) | Norm | Anlage |
|---|---|---|---|
| [Position] | 00,00 | § X JVEG | Anlage [Nr.] |
| **Gesamtbetrag** | **00,00** | | |

Belege: [Liste der Anlagen]
Fristwahrung § 23 JVEG: Leistung erbracht am [Datum]; Antrag fristgerecht.

## Ausgabe
Druckfertiges Antragsschreiben mit Positionsliste, Normenbezug und Anlagenliste.

## Leitplanken
- Kein Schreiben ohne geprüfte Fristen (§ 23 JVEG).
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.

## 3. `jveg-dolmetscher-uebersetzer`

**Fokus:** Verguetung für gerichtliche Dolmetscher und Übersetzer nach JVEG berechnen. Normen: §§ 9 11 JVEG, Anlage 1 JVEG. Prüfraster: Stundenverguetung, Mindestwartezeit, Anfahrt, schriftliche Übersetzung je Seite. Output: Verguetungsberechnung Dolmetscher und Übersetzer. Abgrenzung: nicht Sachverständigenverguetung.

# JVEG-Dolmetscher-Uebersetzer

## Fachkern: JVEG-Dolmetscher-Uebersetzer
- **Spezialgegenstand:** JVEG-Dolmetscher-Uebersetzer wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Prüfe die Vergütungsansprüche von Dolmetschern und Übersetzern nach §§ 13–16 JVEG auf Stundensatz, Textumfang, Reisezeiten und Terminlogik.

## Triage — kläre vor der Prüfung

1. **Tätigkeit:** Dolmetschen (mündlich, § 13 JVEG) oder Übersetzen (schriftlich, § 16 JVEG)?
2. **Sprachkombination:** Welche Sprache — liegt eine Sonderregelung für seltene Sprachen vor?
3. **Umfang:** Stunden (Dolmetscher) oder Zeilen/Normseiten (Übersetzer) — wie belegt?
4. **Reisezeit und Fahrtkosten:** Sind Reisezeiten als Wartezeit oder als Dolmetschzeit abgerechnet?
5. **Fristen:** Dreimonatsfrist § 23 JVEG gewahrt?

## Zentrale Normen
- § 13 JVEG (Dolmetscher — Stundensatz, Mindestdauer)
- § 14 JVEG (Zuschlag für besondere Leistungen)
- § 15 JVEG (Kürzung bei unvollständiger Tätigkeit)
- § 16 JVEG (Übersetzer — Vergütung nach Zeilen)
- §§ 5–7 JVEG (Fahrtkosten)
- § 23 JVEG (Dreimonatsfrist)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Eingang einer Rechnung eines Dolmetschers oder Übersetzers im gerichtlichen Verfahren.

## Arbeitsweise
1. Tätigkeitsart abgrenzen (mündlich/schriftlich).
2. Ansatz auf Normkonformität prüfen (Stundensatz/Zeilenpreis).
3. Zeitnachweis oder Zeilennachweis prüfen.
4. Reisezeiten und Fahrtkosten separat prüfen.
5. Frist § 23 JVEG notieren.

## Output-Template

| Position | Geltend (EUR) | Norm | Prüfbefund | Anerkannt (EUR) |
|---|---|---|---|---|
| Dolmetschzeit [X Std.] | 00,00 | § 13 JVEG | [Befund] | 00,00 |
| Übersetzungszeilen [X] | 00,00 | § 16 JVEG | [Befund] | 00,00 |
| Fahrtkosten | 00,00 | § 5 JVEG | [Befund] | 00,00 |
| **Gesamt** | **00,00** | | | **00,00** |

**Fristenstatus § 23 JVEG:** [Fristende]

## Ausgabe
Positionsgenaues Prüfergebnis mit anerkanntem Betrag und Kürzungsbegründung.

## Leitplanken
- Wartezeiten ohne Dolmetschleistung nicht vergütungsfähig.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
