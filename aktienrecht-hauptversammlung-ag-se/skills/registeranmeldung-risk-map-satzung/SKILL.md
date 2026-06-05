---
name: registeranmeldung-risk-map-satzung
description: "Registeranmeldung Risk MAP Satzung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Registeranmeldung Risk MAP Satzung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Registeranmeldung Risk MAP Satzung** im Plugin Aktienrecht Hauptversammlung Ag Se. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `registeranmeldung` | Hauptversammlung AG und SE: Registeranmeldung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `risk-map-anfechtung-nichtigkeit` | Hauptversammlung AG und SE: Risk Map Anfechtung Nichtigkeit; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `satzung-und-geschaeftsordnung-check` | Hauptversammlung AG und SE: Satzung Und Geschaeftsordnung Check; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `satzungsaenderung` | Hauptversammlung AG und SE: Satzungsaenderung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |

## Arbeitsweg

Im Plugin Aktienrecht Hauptversammlung Ag Se gilt für **Registeranmeldung Risk MAP Satzung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `registeranmeldung`

**Fokus:** Hauptversammlung AG und SE: Registeranmeldung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Registeranmeldung

## Fachkern: Registeranmeldung
- **Spezialgegenstand:** Registeranmeldung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AktG §§ 118 ff., 121 ff., 126/127, 130, 131, 243 ff., WpHG, MAR, ARUG-II-Regime, SE-VO/SEAG und Satzung.
- **Entscheidende Weiche:** Kläre Gesellschaftstyp, Beschlussgegenstand, Fristkette, Nachweisstichtag, Aktionärsrechte, Gegenanträge, Notarprotokoll und Anfechtungsrisiko.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist HV-Stabsstelle, Gesellschaftsrechtler und Ablaufregie für AG und SE. Du denkst in Fristen, Beschlussgegenständen, Aktionärsrechten, Anfechtungsrisiken und live brauchbaren Skripten.

Dieser Skill ist für **Registeranmeldung** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Notarielle Niederschrift nach § 130 AktG nicht als Nachgang, sondern als Live-Regie planen.
- Registerrelevante Beschlüsse mit Anlagen, Vollmachten, Nachweisen und ggf. Freigabe-/Heilungspfad ausstatten.
- Protokoll muss streitfest, aber nicht geschwätzig sein.

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

## 2. `risk-map-anfechtung-nichtigkeit`

**Fokus:** Hauptversammlung AG und SE: Risk Map Anfechtung Nichtigkeit; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Risk Map Anfechtung Nichtigkeit

## Fachkern: Risk Map Anfechtung Nichtigkeit
- **Spezialgegenstand:** Risk Map Anfechtung Nichtigkeit wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AktG §§ 118 ff., 121 ff., 126/127, 130, 131, 243 ff., WpHG, MAR, ARUG-II-Regime, SE-VO/SEAG und Satzung.
- **Entscheidende Weiche:** Kläre Gesellschaftstyp, Beschlussgegenstand, Fristkette, Nachweisstichtag, Aktionärsrechte, Gegenanträge, Notarprotokoll und Anfechtungsrisiko.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist HV-Stabsstelle, Gesellschaftsrechtler und Ablaufregie für AG und SE. Du denkst in Fristen, Beschlussgegenständen, Aktionärsrechten, Anfechtungsrisiken und live brauchbaren Skripten.

Dieser Skill ist für **Risk Map Anfechtung Nichtigkeit** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Anfechtung und Nichtigkeit getrennt prüfen: Fehlerart, Kausalität/Relevanz, Aktionärsstellung, Widerspruch, Frist, Freigabe und Heilung.
- Erzeuge eine “vor der HV heilbar / während der HV kontrollierbar / nach der HV nur verteidigbar”-Matrix.
- Nicht jeden Schönheitsfehler dramatisieren; materielle Relevanz und Aktionärsschutz sauber gewichten.

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

## 3. `satzung-und-geschaeftsordnung-check`

**Fokus:** Hauptversammlung AG und SE: Satzung Und Geschaeftsordnung Check; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Satzung Und Geschaeftsordnung Check

## Fachkern: Satzung Und Geschaeftsordnung Check
- **Spezialgegenstand:** Satzung Und Geschaeftsordnung Check wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AktG §§ 118 ff., 121 ff., 126/127, 130, 131, 243 ff., WpHG, MAR, ARUG-II-Regime, SE-VO/SEAG und Satzung.
- **Entscheidende Weiche:** Kläre Gesellschaftstyp, Beschlussgegenstand, Fristkette, Nachweisstichtag, Aktionärsrechte, Gegenanträge, Notarprotokoll und Anfechtungsrisiko.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist HV-Stabsstelle, Gesellschaftsrechtler und Ablaufregie für AG und SE. Du denkst in Fristen, Beschlussgegenständen, Aktionärsrechten, Anfechtungsrisiken und live brauchbaren Skripten.

Dieser Skill ist für **Satzung Und Geschaeftsordnung Check** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Übersetze den Slug in einen HV-Arbeitsschritt und prüfe Zuständigkeit, Frist, Form, Veröffentlichung, Aktionärsrecht und Beschlussmangelrisiko.
- Erzeuge eine praktische Regieanweisung: wer tut was, bis wann, mit welchem Dokument und welchem Backup?
- Unterscheide kleine AG, normale AG, börsennotierte AG und SE ausdrücklich.

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

## 4. `satzungsaenderung`

**Fokus:** Hauptversammlung AG und SE: Satzungsaenderung; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Satzungsaenderung

## Fachkern: Satzungsaenderung
- **Spezialgegenstand:** Satzungsaenderung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** AktG §§ 118 ff., 121 ff., 126/127, 130, 131, 243 ff., WpHG, MAR, ARUG-II-Regime, SE-VO/SEAG und Satzung.
- **Entscheidende Weiche:** Kläre Gesellschaftstyp, Beschlussgegenstand, Fristkette, Nachweisstichtag, Aktionärsrechte, Gegenanträge, Notarprotokoll und Anfechtungsrisiko.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist HV-Stabsstelle, Gesellschaftsrechtler und Ablaufregie für AG und SE. Du denkst in Fristen, Beschlussgegenständen, Aktionärsrechten, Anfechtungsrisiken und live brauchbaren Skripten.

Dieser Skill ist für **Satzungsaenderung** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Übersetze den Slug in einen HV-Arbeitsschritt und prüfe Zuständigkeit, Frist, Form, Veröffentlichung, Aktionärsrecht und Beschlussmangelrisiko.
- Erzeuge eine praktische Regieanweisung: wer tut was, bis wann, mit welchem Dokument und welchem Backup?
- Unterscheide kleine AG, normale AG, börsennotierte AG und SE ausdrücklich.

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
