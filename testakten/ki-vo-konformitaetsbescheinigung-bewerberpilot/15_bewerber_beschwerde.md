# Bewerber-Beschwerde COMP-2026-0411

**Beschwerde-ID:** COMP-2026-0411
**Eingang:** Sonntag, 16.05.2026, 21:18 Uhr über das Bewerberbeschwerdeformular auf der Internetseite der BewerberPilot Score GmbH
**Eingangsbestätigung:** automatisch um 21:18 Uhr; menschliche Erstantwort durch Customer Success Team (Hannah Erdmann) am Montag 17.05.2026, 09:42 Uhr
**Beschwerdeführerin:** Bewerberin Frau Sahra Damou (Pseudonym wegen Vertraulichkeit; tatsächlicher Name in der Akte hinterlegt)
**Bezug zu Bewerbung:** APP-2026-04-1118 (Pflege-Stelle Cluster B, Elbtal Klinikservice gGmbH)
**Datum Bewerbung:** 04.04.2026
**Datum Ablehnung:** 12.05.2026 (Recruiter-23, Reasontext: "trotz fachlicher Eignung kein freier Slot im Cluster Pflege ab 1.8.")

---

## 1. Inhalt der Beschwerde (wörtlich, anonymisiert)

> "Sehr geehrte Damen und Herren,
>
> ich habe mich am 4. April 2026 bei der Elbtal Klinikservice gGmbH über Ihre Plattform für eine Pflegestelle beworben. Am 12. Mai habe ich eine Ablehnungs-E-Mail bekommen. In der Mail steht, mein Profil sei mit Hilfe eines KI-Systems geprüft worden. Bitte teilen Sie mir mit:
>
> 1. Auf welcher Datengrundlage hat das KI-System mich bewertet?
> 2. Welche Note (Score) habe ich bekommen?
> 3. Welche Merkmale meiner Bewerbung haben dazu geführt, dass ich abgelehnt wurde?
> 4. Hat die Tatsache, dass ich in den letzten drei Jahren in einer Klinik in Beirut gearbeitet habe und nicht in einer deutschen Klinik, eine Rolle gespielt?
> 5. Hat die Tatsache, dass mein Anschreiben in Deutsch geschrieben ist, aber mit dem Stil einer Person, die Deutsch als Fremdsprache erlernt hat, eine Rolle gespielt?
> 6. Würde meine Bewerbung anders bewertet, wenn das KI-System nicht zum Einsatz gekommen wäre?
>
> Ich bin in Deutschland qualifiziert (Anerkennungsbescheid des Sozialministeriums Sachsen vom 14.10.2024). Ich habe alle Sprachzeugnisse vorgelegt (DSH-2, Pflegefachsprache C1). Ich wurde abgelehnt mit der Begründung, es gebe 'keinen freien Slot'. Das ist seltsam, weil dieselbe Stelle eine Woche später erneut ausgeschrieben war.
>
> Ich bitte Sie um eine Antwort innerhalb eines Monats nach Art. 15 DSGVO und um eine Erklärung nach den Vorschriften der KI-Verordnung. Wenn meine Bewerbung wegen meiner Auslandserfahrung oder meines Sprachstils nachteilig behandelt wurde, behalte ich mir vor, eine Beschwerde bei der Landesdatenschutzbeauftragten Sachsen und bei der Antidiskriminierungsstelle des Bundes einzulegen.
>
> Mit freundlichen Gruessen
> Sahra Damou (Name pseudonymisiert)"

## 2. Erstantwort an die Bewerberin (versandt am 17.05.2026, 09:42 Uhr)

> "Sehr geehrte Frau Damou,
>
> vielen Dank für Ihre Anfrage. Wir bestätigen den Eingang Ihrer Beschwerde unter der Vorgangsnummer COMP-2026-0411. Wir werden Ihre Anfrage gemaess Art. 15 DSGVO und Art. 19 KI-VO innerhalb eines Monats nach Eingang beantworten, das ist bis spätestens 16.06.2026.
>
> Bitte beachten Sie, dass:
>
> 1. Die BewerberPilot Score GmbH ist Anbieterin des KI-Systems. Die Bewerbungsentscheidung in Ihrem Fall hat die Elbtal Klinikservice gGmbH getroffen. Wir werden Ihre Anfrage gemeinsam mit der Elbtal Klinikservice gGmbH bearbeiten.
> 2. Die Antwort umfasst Score, Erklaermerkmale und (soweit verfügbar) die menschliche Begründung des Recruiters.
> 3. Sie können unter folgendem Link eine Anonymisierung Ihres Falls für die Nutzung in unserer Bias-Pruefung beantragen.
>
> Mit freundlichen Gruessen
> Hannah Erdmann
> Customer Success Manager
> BewerberPilot Score GmbH"

## 3. Interne Pruefung des Vorgangs (vorläufig)

### 3.1 Score und Erklaermerkmale (laut Logfile-Auszug)

| Feld | Wert | Bemerkung |
|---|---|---|
| Score | 41 | Mittelfeld, nicht in Top-20 |
| Muss-Kriterium-Flag | PASS | qualifikatorisch erfüllt |
| Reason Codes | career_continuity, language_proficient_b2 | nicht: "Auslandserfahrung negativ" |

Die "career_continuity" wird als Erklaermerkmal angezeigt. Die Bewerberin hat einen nicht-linearen Verlauf (zwei Jahre Beirut-Klinik, davor Aachen) — das ist im Kontext des Bias-Audits (vgl. 13_bias_audit_bericht.md) als **kritisches Merkmal** markiert.

Die Reason-Codes "language_proficient_b2" statt "language_german_native" weist auf die Sprachmuster-Erkennung hin. Frau Damou hat einen Sprachstil, der von der Mustermenge "Muttersprache Deutsch" abweicht.

### 3.2 Recruiter-Entscheidung

Recruiter-23 hat die Ablehnung mit dem Text "trotz fachlicher Eignung kein freier Slot im Cluster Pflege ab 1.8." begründet. Diese Begründung ist:

- Sachlich auf "kein freier Slot" gestützt.
- Aber: Dieselbe Stelle ist eine Woche später (19.05.2026) erneut ausgeschrieben worden. Das ist im Logfile **nicht** ersichtlich, aber durch externe Recherche nachprüfbar.

### 3.3 Bias-Bezug

Frau Damou fällt in **zwei** Cluster mit erhöhter Bias-Wahrscheinlichkeit nach dem Bias-Auditbericht:

- "nicht-lineare Karriereverläufe" (-7.4 Pp. Selektionsrate)
- "sprachliche Nicht-Muttersprachlichkeit" (-5.1 Pp.)

Eine Korrektur des Featuregewichts in diesen Bereichen ist im Massnahmenplan vorgesehen (Lückenliste Nr. 2 und 3, Frist 21.06.2026). Zum Zeitpunkt der Ablehnung (12.05.2026) waren die Massnahmen noch nicht umgesetzt.

### 3.4 Verfahrensrechtliche Pruefung

- **Art. 15 DSGVO (Auskunftsrecht):** Antwort innerhalb eines Monats vorgesehen.
- **Art. 22 DSGVO (Verbot ausschliesslich automatisierter Entscheidung):** Hier nicht berührt, weil die Entscheidung durch einen Menschen (Recruiter-23) getroffen wurde. Allerdings ist der Einfluss des KI-Vorschlags auf den Recruiter zu untersuchen ("Soft Automation").
- **Art. 19 KI-VO (Beschwerdemöglichkeit):** Das System hat ein Beschwerdeformular, das genutzt wurde. Die Frist nach KI-VO ist gewahrt.
- **AGG:** Pruefung, ob ein Vergleichsmoment besteht (andere Bewerbende mit ähnlicher Qualifikation, aber linearem Karriereweg und deutscher Muttersprache, sind eingeladen worden). Bei Indizien (§ 22 AGG) verschiebt sich die Beweislast.

## 4. Empfehlung (Customer Success + Compliance)

1. **Innerhalb von zwei Wochen** ausführliche Antwort an Frau Damou mit den in 3.1 genannten Daten, einer Erklärung des Reason-Codes-Konzepts und einem Hinweis auf das laufende Bias-Audit.
2. **Klärung mit Elbtal Klinikservice gGmbH:**
   - Warum wurde die Stelle erneut ausgeschrieben?
   - Wurde Frau Damou aus einem anderen Grund abgelehnt, als der Recruiter angegeben hat?
   - Wer hat die Ablehnung intern freigegeben?
3. **Anbieterseitige Reaktion:**
   - Bewerbung als Use-Case in das Bias-Reviewset aufnehmen (mit Einwilligung Frau Damous).
   - Featuregewichte vor Pilotbeginn anpassen (Lückenliste Nr. 2 und 3, Frist 21.06.2026).
   - Recruiter-23 in der Schulung 31.05.2026 über den Vorfall briefen.
4. **Beobachtung:** Wenn Frau Damou Beschwerde bei der Landesdatenschutzbeauftragten Sachsen einlegt, ist der Vorgang eskalationspflichtig im Sinne von Art. 73 KI-VO (Meldung schwerwiegender Vorfälle, sofern qualifizierter Vorfall vorliegt).

## 5. Akten- und Datenflusshinweis

- Frau Damous Bewerbungsunterlagen sind im Pilotsystem in pseudonymisierter Form gespeichert; Aufbewahrung 24 Monate, Löschung 12.05.2028.
- Der Beschwerdevorgang COMP-2026-0411 ist Bestandteil des Compliance-Registers.
- Eine Kopie der Beschwerde wird an die Betreiberin (Elbtal Klinikservice gGmbH) über den Compliance-Channel weitergeleitet.
- Die Anbieterin koordiniert die Antwort an Frau Damou nur, soweit Auskunft zu Score und Erklaermerkmalen gebeten wird; die "Warum-nicht-eingestellt-Antwort" trifft die Betreiberin.

## 6. Vorläufige Wertung Compliance

Die Beschwerde Frau Damous ist **berechtigt** in dem Sinn, dass sie ein laufendes Bias-Problem im System sichtbar macht. Eine gerichtsfeste Diskriminierung ist daraus noch nicht ableitbar; die Wahrscheinlichkeit, dass das KI-System den Score negativ beeinflusst hat, ist aber konkret und sollte zu einer (a) reaktiven Korrektur für Frau Damou (nochmalige Pruefung der Bewerbung durch einen anderen Recruiter ohne KI-Score) und (b) proaktiven Massnahme im Pilotbetrieb führen.

## 7. Zeitlinie

- 16.05.2026 21:18 Uhr: Beschwerde eingegangen.
- 17.05.2026 09:42 Uhr: Erstantwort versendet.
- 21.05.2026: Coordinatorgespraech mit Elbtal Klinikservice gGmbH (Frau Yann, Personalleitung).
- 23.05.2026: Bias-Auditbericht v0.4 als Bezugsdokument geprüft.
- 26.05.2026: Compliance-Vorgangsnotiz in die Akte aufgenommen.
- **Bis 16.06.2026:** Ausführliche Antwort an Frau Damou (Art. 15 DSGVO-Frist).
- **Bis 21.06.2026:** Featuregewichts-Anpassungen umgesetzt (Lückenliste).
- **Bis 06.07.2026:** Bias-Wirkungsbestätigung FairnessLab.
