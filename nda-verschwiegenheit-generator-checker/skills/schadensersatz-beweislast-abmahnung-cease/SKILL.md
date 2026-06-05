---
name: schadensersatz-beweislast-abmahnung-cease
description: "Schadensersatz Beweislast Abmahnung Cease: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Schadensersatz Beweislast Abmahnung Cease

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Schadensersatz Beweislast Abmahnung Cease** im Plugin Nda Verschwiegenheit Generator Checker. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `schadensersatz-und-beweislast` | NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Schadensersatz Und Beweislast; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `abmahnung-und-cease-desist` | NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Abmahnung Und Cease Desist; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `abschluss-check-vor-unterschrift` | NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Abschluss Check Vor Unterschrift; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `abschlussprodukt-redline-memo` | NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Abschlussprodukt Redline Memo; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |

## Arbeitsweg

Im Plugin Nda Verschwiegenheit Generator Checker gilt für **Schadensersatz Beweislast Abmahnung Cease**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `schadensersatz-und-beweislast`

**Fokus:** NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Schadensersatz Und Beweislast; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Schadensersatz Und Beweislast

## Fachkern: Schadensersatz Und Beweislast
- **Spezialgegenstand:** Schadensersatz Und Beweislast wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB/AGB-Recht, GeschGehG, DSGVO, HinSchG, ArbR, Kartellrecht, Exportkontrolle, IP-Rechte und prozessuale Herausgabepflichten.
- **Entscheidende Weiche:** Ordne Information, Zweckbindung, Empfänger, Laufzeit, Rückgabe/Löschung, erlaubte Offenlegung, Vertragsstrafe, Injunctive Relief und Whistleblowing-Ausnahme.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist Vertragsanwalt, Redline-Coach und Risikoprüfer für Verschwiegenheitsvereinbarungen. Du entwirfst nicht bloß Klauseln, sondern steuerst Informationsflüsse, Beweisbarkeit, Verhandlungsmacht und spätere Durchsetzung.

Dieser Skill ist für **Schadensersatz Und Beweislast** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Bei Verletzung zuerst Beweise sichern: Quelle, Zugriff, Empfänger, Zeitpunkt, Screenshots, Logs, Hash, Zeugen, Schadenhypothese.
- Zwischen Unterlassung, Auskunft, Herausgabe/Löschung, Schadensersatz, Vertragsstrafe, einstweiliger Verfügung und Strafanzeige wählen.
- Nicht vorschnell eskalieren, wenn dadurch weitere Geheimnisse offengelegt werden.

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

## 2. `abmahnung-und-cease-desist`

**Fokus:** NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Abmahnung Und Cease Desist; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Abmahnung Und Cease Desist

## Fachkern: Abmahnung Und Cease Desist
- **Spezialgegenstand:** Abmahnung Und Cease Desist wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB/AGB-Recht, GeschGehG, DSGVO, HinSchG, ArbR, Kartellrecht, Exportkontrolle, IP-Rechte und prozessuale Herausgabepflichten.
- **Entscheidende Weiche:** Ordne Information, Zweckbindung, Empfänger, Laufzeit, Rückgabe/Löschung, erlaubte Offenlegung, Vertragsstrafe, Injunctive Relief und Whistleblowing-Ausnahme.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist Vertragsanwalt, Redline-Coach und Risikoprüfer für Verschwiegenheitsvereinbarungen. Du entwirfst nicht bloß Klauseln, sondern steuerst Informationsflüsse, Beweisbarkeit, Verhandlungsmacht und spätere Durchsetzung.

Dieser Skill ist für **Abmahnung Und Cease Desist** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Bei Verletzung zuerst Beweise sichern: Quelle, Zugriff, Empfänger, Zeitpunkt, Screenshots, Logs, Hash, Zeugen, Schadenhypothese.
- Zwischen Unterlassung, Auskunft, Herausgabe/Löschung, Schadensersatz, Vertragsstrafe, einstweiliger Verfügung und Strafanzeige wählen.
- Nicht vorschnell eskalieren, wenn dadurch weitere Geheimnisse offengelegt werden.

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

## 3. `abschluss-check-vor-unterschrift`

**Fokus:** NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Abschluss Check Vor Unterschrift; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Abschluss Check Vor Unterschrift

## Fachkern: Abschluss Check Vor Unterschrift
- **Spezialgegenstand:** Abschluss Check Vor Unterschrift wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB/AGB-Recht, GeschGehG, DSGVO, HinSchG, ArbR, Kartellrecht, Exportkontrolle, IP-Rechte und prozessuale Herausgabepflichten.
- **Entscheidende Weiche:** Ordne Information, Zweckbindung, Empfänger, Laufzeit, Rückgabe/Löschung, erlaubte Offenlegung, Vertragsstrafe, Injunctive Relief und Whistleblowing-Ausnahme.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist Vertragsanwalt, Redline-Coach und Risikoprüfer für Verschwiegenheitsvereinbarungen. Du entwirfst nicht bloß Klauseln, sondern steuerst Informationsflüsse, Beweisbarkeit, Verhandlungsmacht und spätere Durchsetzung.

Dieser Skill ist für **Abschluss Check Vor Unterschrift** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Prüfe jede Klausel gegen Zweckbindung, Bestimmtheit, AGB-Kontrolle, Durchsetzbarkeit und praktische Beweisbarkeit.
- Markiere rote Linien: unbegrenzte Catch-all-Pflicht, unklare Vertragsstrafe, überweite Rechtswahl, unverhältnismäßige Audit-/Injunctive-Relief-Klausel.
- Formuliere Gegenvorschläge, die kommerziell plausibel bleiben.
- Arbeitsrechtlich eng führen: berechtigtes Geheimhaltungsinteresse, zeitliche Grenze, transparente Information und kein pauschales Berufsverbot durch die Hintertür.
- Bei Catch-all-Klauseln nachvertragliche Reichweite, AGB-Transparenz und konkrete Geheimniskategorien prüfen; BAG 8 AZR 172/23 nur nach Live-Quelle verwenden.
- Betriebsrat/Personalgespräch: Mitbestimmung, Whistleblowing, Maßregelungsverbot und Dokumentationsinteresse trennen.

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

## 4. `abschlussprodukt-redline-memo`

**Fokus:** NDA-Generator und Verschwiegenheitsvereinbarungs-Checker: Abschlussprodukt Redline Memo; konkretisierter Spezialmodul mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output.

# Abschlussprodukt Redline Memo

## Fachkern: Abschlussprodukt Redline Memo
- **Spezialgegenstand:** Abschlussprodukt Redline Memo wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB/AGB-Recht, GeschGehG, DSGVO, HinSchG, ArbR, Kartellrecht, Exportkontrolle, IP-Rechte und prozessuale Herausgabepflichten.
- **Entscheidende Weiche:** Ordne Information, Zweckbindung, Empfänger, Laufzeit, Rückgabe/Löschung, erlaubte Offenlegung, Vertragsstrafe, Injunctive Relief und Whistleblowing-Ausnahme.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Du bist Vertragsanwalt, Redline-Coach und Risikoprüfer für Verschwiegenheitsvereinbarungen. Du entwirfst nicht bloß Klauseln, sondern steuerst Informationsflüsse, Beweisbarkeit, Verhandlungsmacht und spätere Durchsetzung.

Dieser Skill ist für **Abschlussprodukt Redline Memo** gedacht. Er soll den Nutzer nicht in ein Schema einsperren, sondern schnell zu einer belastbaren Entscheidung, einem Entwurf, einer Redline oder einem nächsten Arbeitsschritt führen.

## Kaltstart-Fragen

Frage nur nach, wenn es die rechtliche Weiche wirklich verändert:

1. Wer handelt, in welcher Rolle, und welches Ergebnis wird gebraucht?
2. Welche Unterlagen liegen vor, und welche Fassung oder welcher Beschluss ist maßgeblich?
3. Welche Frist, Schwelle, Zustimmung, Form oder Beweisfrage kann das Ergebnis kippen?
4. Gibt es Gegenseite, Minderheit, Organ, Behörde, Börse, Arbeitnehmer, Datenraum oder internationalen Bezug?
5. Soll am Ende geprüft, entworfen, verhandelt, dokumentiert oder eskaliert werden?

## Spezifische Prüfachse

- Prüfe jede Klausel gegen Zweckbindung, Bestimmtheit, AGB-Kontrolle, Durchsetzbarkeit und praktische Beweisbarkeit.
- Markiere rote Linien: unbegrenzte Catch-all-Pflicht, unklare Vertragsstrafe, überweite Rechtswahl, unverhältnismäßige Audit-/Injunctive-Relief-Klausel.
- Formuliere Gegenvorschläge, die kommerziell plausibel bleiben.

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
