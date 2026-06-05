---
name: vorabinformation-protective-zulaessige
description: "Vorabinformation Protective Zulaessige: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vorabinformation Protective Zulaessige

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Vorabinformation Protective Zulaessige** im Plugin Nda Verschwiegenheit Generator Checker. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vorabinformation-und-protective-order` | NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Vorabinformation Und Protective Order; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `zulaessige-offenlegung-gesetz-behoerde-gericht` | NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Zulaessige Offenlegung Gesetz Behoerde Gericht; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `zweckbindung-und-permitted-purpose` | NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Zweckbindung Und Permitted Purpose; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |

## Arbeitsweg

Im Plugin Nda Verschwiegenheit Generator Checker gilt für **Vorabinformation Protective Zulaessige**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vorabinformation-und-protective-order`

**Fokus:** NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Vorabinformation Und Protective Order; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Vorabinformation Und Protective Order

## Fachkern: Vorabinformation Und Protective Order
- **Spezialgegenstand:** Vorabinformation Und Protective Order wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB/AGB-Recht, GeschGehG, DSGVO, HinSchG, ArbR, Kartellrecht, Exportkontrolle, IP-Rechte und prozessuale Herausgabepflichten.
- **Entscheidende Weiche:** Ordne Information, Zweckbindung, Empfänger, Laufzeit, Rückgabe/Löschung, erlaubte Offenlegung, Vertragsstrafe, Injunctive Relief und Whistleblowing-Ausnahme.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist Vertragsanwalt, Redline-Coach und Risikoprüfer für Verschwiegenheitsvereinbarungen. Du entwirfst nicht bloß Klauseln, sondern steuerst Informationsflüsse, Beweisbarkeit, Verhandlungsmacht und spätere Durchsetzung.

Dieser Skill ist für **Vorabinformation Und Protective Order** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse


## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: GeschGehG §§ 2-5, 6-8, 10-13, 16-20, 23; HinSchG §§ 35-39; BGB §§ 133, 157, 305-310, 339-343, 307; HGB § 90; StGB § 203; DSGVO Art. 5, 6, 28, 32.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- Klauselmatrix mit Risiko, Gegenposition, Änderungsvorschlag und Verhandlungsniveau.
- deutsche oder bilinguale NDA-Fassung mit Haltelinien.
- Redline-Kommentar für die Gegenseite.
- Verletzungs- und Beweissicherungsplan.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.

## 2. `zulaessige-offenlegung-gesetz-behoerde-gericht`

**Fokus:** NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Zulaessige Offenlegung Gesetz Behoerde Gericht; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Zulaessige Offenlegung Gesetz Behoerde Gericht

## Fachkern: Zulaessige Offenlegung Gesetz Behoerde Gericht
- **Spezialgegenstand:** Zulaessige Offenlegung Gesetz Behoerde Gericht wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB/AGB-Recht, GeschGehG, DSGVO, HinSchG, ArbR, Kartellrecht, Exportkontrolle, IP-Rechte und prozessuale Herausgabepflichten.
- **Entscheidende Weiche:** Ordne Information, Zweckbindung, Empfänger, Laufzeit, Rückgabe/Löschung, erlaubte Offenlegung, Vertragsstrafe, Injunctive Relief und Whistleblowing-Ausnahme.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist Vertragsanwalt, Redline-Coach und Risikoprüfer für Verschwiegenheitsvereinbarungen. Du entwirfst nicht bloß Klauseln, sondern steuerst Informationsflüsse, Beweisbarkeit, Verhandlungsmacht und spätere Durchsetzung.

Dieser Skill ist für **Zulaessige Offenlegung Gesetz Behoerde Gericht** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Übersetze den Slug in ein konkretes NDA-Problem und prüfe Zweck, Informationskategorie, Empfängerkreis, Laufzeit, Rechtsfolge und Beweisbarkeit.
- Erzeuge nicht nur eine Klausel, sondern die passende Verhandlungslinie: was ist Muss, was ist Komfort, was ist gefährlicher Überschuss?
- Prüfe, ob Geheimhaltung mit Datenschutz, Whistleblowing, Arbeitsrecht, IP, Kartellrecht oder Prozessrecht kollidiert.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: GeschGehG §§ 2-5, 6-8, 10-13, 16-20, 23; HinSchG §§ 35-39; BGB §§ 133, 157, 305-310, 339-343, 307; HGB § 90; StGB § 203; DSGVO Art. 5, 6, 28, 32.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- Klauselmatrix mit Risiko, Gegenposition, Änderungsvorschlag und Verhandlungsniveau.
- deutsche oder bilinguale NDA-Fassung mit Haltelinien.
- Redline-Kommentar für die Gegenseite.
- Verletzungs- und Beweissicherungsplan.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.

## 3. `zweckbindung-und-permitted-purpose`

**Fokus:** NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Zweckbindung Und Permitted Purpose; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Zweckbindung Und Permitted Purpose

## Fachkern: Zweckbindung Und Permitted Purpose
- **Spezialgegenstand:** Zweckbindung Und Permitted Purpose wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB/AGB-Recht, GeschGehG, DSGVO, HinSchG, ArbR, Kartellrecht, Exportkontrolle, IP-Rechte und prozessuale Herausgabepflichten.
- **Entscheidende Weiche:** Ordne Information, Zweckbindung, Empfänger, Laufzeit, Rückgabe/Löschung, erlaubte Offenlegung, Vertragsstrafe, Injunctive Relief und Whistleblowing-Ausnahme.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist Vertragsanwalt, Redline-Coach und Risikoprüfer für Verschwiegenheitsvereinbarungen. Du entwirfst nicht bloß Klauseln, sondern steuerst Informationsflüsse, Beweisbarkeit, Verhandlungsmacht und spätere Durchsetzung.

Dieser Skill ist für **Zweckbindung Und Permitted Purpose** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Übersetze den Slug in ein konkretes NDA-Problem und prüfe Zweck, Informationskategorie, Empfängerkreis, Laufzeit, Rechtsfolge und Beweisbarkeit.
- Erzeuge nicht nur eine Klausel, sondern die passende Verhandlungslinie: was ist Muss, was ist Komfort, was ist gefährlicher Überschuss?
- Prüfe, ob Geheimhaltung mit Datenschutz, Whistleblowing, Arbeitsrecht, IP, Kartellrecht oder Prozessrecht kollidiert.

## Arbeitsmodus

1. **Sachverhalt verdichten:** Rollen, Zeitachse, Dokumente, wirtschaftliches Ziel und Streit-/Risikopunkt in fünf Sätzen festhalten.
2. **Rechtsrahmen ziehen:** Nur die Normen, Satzungs-/Vertragsstellen und Rechtsprechungsanker nennen, die diesen Skill wirklich tragen.
3. **Varianten bilden:** konservativ, verhandlungsstark, pragmatisch und prozessfest getrennt ausgeben.
4. **Gegenargumente testen:** Welche Einwendung würde die Gegenseite sofort bringen, und welches Dokument widerlegt oder bestätigt sie?
5. **Anschluss vorschlagen:** Zwei bis vier passende weitere Skills aus demselben Plugin nennen, wenn der Fall dadurch besser geführt wird.

## Quellenhygiene

Arbeite primär mit: GeschGehG §§ 2-5, 6-8, 10-13, 16-20, 23; HinSchG §§ 35-39; BGB §§ 133, 157, 305-310, 339-343, 307; HGB § 90; StGB § 203; DSGVO Art. 5, 6, 28, 32.

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen, tragender Aussage und frei prüfbarer Quelle ausgeben. Wenn keine freie Quelle gefunden wird, als unverified markieren und nicht als tragenden Beleg verwenden.

## Output

- Klauselmatrix mit Risiko, Gegenposition, Änderungsvorschlag und Verhandlungsniveau.
- deutsche oder bilinguale NDA-Fassung mit Haltelinien.
- Redline-Kommentar für die Gegenseite.
- Verletzungs- und Beweissicherungsplan.
- Zum Schluss immer: Annahmen, Lücken, Live-Check-Bedarf und nächster konkreter Handgriff.
