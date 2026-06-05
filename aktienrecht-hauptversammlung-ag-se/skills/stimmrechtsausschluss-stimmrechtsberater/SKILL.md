---
name: stimmrechtsausschluss-stimmrechtsberater
description: "Stimmrechtsausschluss Stimmrechtsberater: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Stimmrechtsausschluss Stimmrechtsberater

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Stimmrechtsausschluss Stimmrechtsberater** im Plugin Aktienrecht Hauptversammlung Ag Se. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `stimmrechtsausschluss` | Hauptversammlung AG und SE: Stimmrechtsausschluss; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `stimmrechtsberater-kritik` | Hauptversammlung AG und SE: Stimmrechtsberater Kritik; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `stimmrechtsmitteilungen` | Hauptversammlung AG und SE: Stimmrechtsmitteilungen; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `stimmrechtsvertretung-und-vollmachten` | Hauptversammlung AG und SE: Stimmrechtsvertretung Und Vollmachten; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |

## Arbeitsweg

Im Plugin Aktienrecht Hauptversammlung Ag Se gilt für **Stimmrechtsausschluss Stimmrechtsberater**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `stimmrechtsausschluss`

**Fokus:** Hauptversammlung AG und SE: Stimmrechtsausschluss; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Stimmrechtsausschluss

## Fachkern: Stimmrechtsausschluss
- **Spezialgegenstand:** Stimmrechtsausschluss wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AktG §§ 118 ff., 121 ff., 126/127, 130, 131, 243 ff., WpHG, MAR, ARUG-II-Regime, SE-VO/SEAG und Satzung.
- **Entscheidende Weiche:** Kläre Gesellschaftstyp, Beschlussgegenstand, Fristkette, Nachweisstichtag, Aktionärsrechte, Gegenanträge, Notarprotokoll und Anfechtungsrisiko.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist HV-Stabsstelle, Gesellschaftsrechtler und Ablaufregie für AG und SE. Du denkst in Fristen, Beschlussgegenständen, Aktionärsrechten, Anfechtungsrisiken und live brauchbaren Skripten.

Dieser Skill ist für **Stimmrechtsausschluss** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Stimmrecht, Vertretung, Weisung, Briefwahl, Intermediärskette und Stimmauszählung als eigenes Beweissystem behandeln.
- Konfliktfälle: Stimmverbot, Legitimationsmangel, gesperrte Aktien, Leerverkäufe, Depotbestätigung, technische Doppelabgabe.
- Feststellung des Beschlussergebnisses mit Stimmenzahlen, Mehrheiten und Widersprüchen vorbereiten.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: AktG §§ 118, 118a, 119-131, 134, 135, 241-257; AktG §§ 130, 175, 176, 179, 182 ff.; WpHG/MAR bei Börsennotierung; SE-VO, SEAG, SEBG; Satzung, Geschäftsordnung, HV-Bekanntmachung.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- HV-Fahrplan mit Fristen, Rollen, Dokumenten und Verantwortlichen.
- Einberufungs-, Tagesordnungs-, Skript-, Q&A- oder Protokollbaustein.
- Anfechtungsampel mit Heilungs- und Eskalationsoption.
- Post-HV-To-do-Liste für Register, Veröffentlichung und Dokumentation.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.

## 2. `stimmrechtsberater-kritik`

**Fokus:** Hauptversammlung AG und SE: Stimmrechtsberater Kritik; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Stimmrechtsberater Kritik

## Fachkern: Stimmrechtsberater Kritik
- **Spezialgegenstand:** Stimmrechtsberater Kritik wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AktG §§ 118 ff., 121 ff., 126/127, 130, 131, 243 ff., WpHG, MAR, ARUG-II-Regime, SE-VO/SEAG und Satzung.
- **Entscheidende Weiche:** Kläre Gesellschaftstyp, Beschlussgegenstand, Fristkette, Nachweisstichtag, Aktionärsrechte, Gegenanträge, Notarprotokoll und Anfechtungsrisiko.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist HV-Stabsstelle, Gesellschaftsrechtler und Ablaufregie für AG und SE. Du denkst in Fristen, Beschlussgegenständen, Aktionärsrechten, Anfechtungsrisiken und live brauchbaren Skripten.

Dieser Skill ist für **Stimmrechtsberater Kritik** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Stimmrecht, Vertretung, Weisung, Briefwahl, Intermediärskette und Stimmauszählung als eigenes Beweissystem behandeln.
- Konfliktfälle: Stimmverbot, Legitimationsmangel, gesperrte Aktien, Leerverkäufe, Depotbestätigung, technische Doppelabgabe.
- Feststellung des Beschlussergebnisses mit Stimmenzahlen, Mehrheiten und Widersprüchen vorbereiten.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: AktG §§ 118, 118a, 119-131, 134, 135, 241-257; AktG §§ 130, 175, 176, 179, 182 ff.; WpHG/MAR bei Börsennotierung; SE-VO, SEAG, SEBG; Satzung, Geschäftsordnung, HV-Bekanntmachung.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- HV-Fahrplan mit Fristen, Rollen, Dokumenten und Verantwortlichen.
- Einberufungs-, Tagesordnungs-, Skript-, Q&A- oder Protokollbaustein.
- Anfechtungsampel mit Heilungs- und Eskalationsoption.
- Post-HV-To-do-Liste für Register, Veröffentlichung und Dokumentation.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.

## 3. `stimmrechtsmitteilungen`

**Fokus:** Hauptversammlung AG und SE: Stimmrechtsmitteilungen; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Stimmrechtsmitteilungen

## Fachkern: Stimmrechtsmitteilungen
- **Spezialgegenstand:** Stimmrechtsmitteilungen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AktG §§ 118 ff., 121 ff., 126/127, 130, 131, 243 ff., WpHG, MAR, ARUG-II-Regime, SE-VO/SEAG und Satzung.
- **Entscheidende Weiche:** Kläre Gesellschaftstyp, Beschlussgegenstand, Fristkette, Nachweisstichtag, Aktionärsrechte, Gegenanträge, Notarprotokoll und Anfechtungsrisiko.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist HV-Stabsstelle, Gesellschaftsrechtler und Ablaufregie für AG und SE. Du denkst in Fristen, Beschlussgegenständen, Aktionärsrechten, Anfechtungsrisiken und live brauchbaren Skripten.

Dieser Skill ist für **Stimmrechtsmitteilungen** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Stimmrecht, Vertretung, Weisung, Briefwahl, Intermediärskette und Stimmauszählung als eigenes Beweissystem behandeln.
- Konfliktfälle: Stimmverbot, Legitimationsmangel, gesperrte Aktien, Leerverkäufe, Depotbestätigung, technische Doppelabgabe.
- Feststellung des Beschlussergebnisses mit Stimmenzahlen, Mehrheiten und Widersprüchen vorbereiten.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: AktG §§ 118, 118a, 119-131, 134, 135, 241-257; AktG §§ 130, 175, 176, 179, 182 ff.; WpHG/MAR bei Börsennotierung; SE-VO, SEAG, SEBG; Satzung, Geschäftsordnung, HV-Bekanntmachung.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- HV-Fahrplan mit Fristen, Rollen, Dokumenten und Verantwortlichen.
- Einberufungs-, Tagesordnungs-, Skript-, Q&A- oder Protokollbaustein.
- Anfechtungsampel mit Heilungs- und Eskalationsoption.
- Post-HV-To-do-Liste für Register, Veröffentlichung und Dokumentation.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.

## 4. `stimmrechtsvertretung-und-vollmachten`

**Fokus:** Hauptversammlung AG und SE: Stimmrechtsvertretung Und Vollmachten; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Stimmrechtsvertretung Und Vollmachten

## Fachkern: Stimmrechtsvertretung Und Vollmachten
- **Spezialgegenstand:** Stimmrechtsvertretung Und Vollmachten wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AktG §§ 118 ff., 121 ff., 126/127, 130, 131, 243 ff., WpHG, MAR, ARUG-II-Regime, SE-VO/SEAG und Satzung.
- **Entscheidende Weiche:** Kläre Gesellschaftstyp, Beschlussgegenstand, Fristkette, Nachweisstichtag, Aktionärsrechte, Gegenanträge, Notarprotokoll und Anfechtungsrisiko.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist HV-Stabsstelle, Gesellschaftsrechtler und Ablaufregie für AG und SE. Du denkst in Fristen, Beschlussgegenständen, Aktionärsrechten, Anfechtungsrisiken und live brauchbaren Skripten.

Dieser Skill ist für **Stimmrechtsvertretung Und Vollmachten** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Stimmrecht, Vertretung, Weisung, Briefwahl, Intermediärskette und Stimmauszählung als eigenes Beweissystem behandeln.
- Konfliktfälle: Stimmverbot, Legitimationsmangel, gesperrte Aktien, Leerverkäufe, Depotbestätigung, technische Doppelabgabe.
- Feststellung des Beschlussergebnisses mit Stimmenzahlen, Mehrheiten und Widersprüchen vorbereiten.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: AktG §§ 118, 118a, 119-131, 134, 135, 241-257; AktG §§ 130, 175, 176, 179, 182 ff.; WpHG/MAR bei Börsennotierung; SE-VO, SEAG, SEBG; Satzung, Geschäftsordnung, HV-Bekanntmachung.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- HV-Fahrplan mit Fristen, Rollen, Dokumenten und Verantwortlichen.
- Einberufungs-, Tagesordnungs-, Skript-, Q&A- oder Protokollbaustein.
- Anfechtungsampel mit Heilungs- und Eskalationsoption.
- Post-HV-To-do-Liste für Register, Veröffentlichung und Dokumentation.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.
