---
name: werkvertrag-maengelrechte-deliktsrecht
description: "Werkvertrag Maengelrechte Deliktsrecht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Werkvertrag Maengelrechte Deliktsrecht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Werkvertrag Maengelrechte Deliktsrecht** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `werkvertrag-maengelrechte` | Werkvertrag-Mängelrechte §§ 633-638 BGB: Nacherfüllung, Selbstvornahme, Minderung, Schadensersatz. |
| `deliktsrecht-haftung-fuer-verrichtungen-paragraph-831` | Prüft Haftung für Verrichtungsgehilfen § 831 BGB: Verrichtungsgehilfe, Exkulpation und Schaden. |
| `kaufrecht-schadensersatz-aufwendungsersatz` | Prüft Schadensersatz §§ 437 Nr. 3 und 280 ff. BGB sowie Aufwendungsersatz § 284 BGB beim Kaufrecht. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Werkvertrag Maengelrechte Deliktsrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `werkvertrag-maengelrechte`

**Fokus:** Werkvertrag-Mängelrechte §§ 633-638 BGB: Nacherfüllung, Selbstvornahme, Minderung, Schadensersatz.

# Werkvertrag Mängelrechte §§ 633-638 BGB

## Fachkern: Werkvertrag Mängelrechte §§ 633-638 BGB
- **Spezialgegenstand:** Werkvertrag Mängelrechte §§ 633-638 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Werkvertragliche Mängelrechte nach §§ 633-638 BGB vollständig prüfen: Mangeldefinition, Nacherfüllungsrecht, Selbstvornahme, Minderung, Rücktritt und Schadensersatz.

## Normanker

- § 633 BGB: Sach- und Rechtsmangel beim Werkvertrag
- § 634 BGB: Rechte des Bestellers (Stufenverhältnis)
- § 635 BGB: Nacherfüllung (Nachbesserung oder Neuherstellung)
- § 636 BGB: Besondere Bestimmungen für Rücktritt und Schadensersatz ohne Fristsetzung
- § 637 BGB: Selbstvornahme und Aufwendungsersatz
- § 638 BGB: Minderung der Vergütung
- § 634a BGB: Verjährung der Mängelansprüche

## Intake

- Welcher Mangel liegt vor (Sachmangel: subjektiv, objektiv; Rechtsmangel)?
- Wann wurde der Mangel entdeckt und angezeigt?
- Wurde Nacherfüllung verlangt und eine Frist gesetzt?
- Wurde Nacherfüllung abgelehnt oder ist sie fehlgeschlagen?
- Ist Verjährung eingetreten?

## Prüfraster

1. Mangelbegriff nach § 633 BGB: subjektive Anforderungen (Vereinbarung), objektive Anforderungen (Üblichkeit), Montage
2. Mangel bei Abnahme vorhanden: Beweislastregel und Abnahme-Zeitpunkt
3. Fristsetzung zur Nacherfüllung: Grundvoraussetzung für Rücktritt, Minderung, Schadensersatz
4. Nacherfüllung nach § 635 BGB: Anspruch des Bestellers; Wahlrecht Nachbesserung oder Neuherstellung
5. Ausnahmen von der Fristsetzung nach § 636 BGB: ernsthafte und endgültige Verweigerung, besondere Umstände
6. Selbstvornahme nach § 637 BGB: Fristsetzung fehlgeschlagen oder entbehrlich; Aufwendungsersatz
7. Minderung nach § 638 BGB: verhältnismäßige Herabsetzung der Vergütung
8. Schadensersatz: §§ 280 und 281 BGB (Pflichtverletzung und Verschulden); statt Leistung oder neben Leistung
9. Verjährung: § 634a Abs. 1 BGB (2 Jahre für bewegliche Sachen; 5 Jahre für Bauwerke)

## Fallstricke

- Fristsetzung fehlt: kein Rücktritt, keine Minderung, kein Schadensersatz statt Leistung.
- Nacherfüllungsrecht des Unternehmers ist subjektives Recht; Besteller muss es einräumen.
- Selbstvornahme nur nach fehlgeschlagener oder endgültig abgelehnter Nacherfüllung.
- Verjährung beginnt mit Abnahme (§ 634a Abs. 2 BGB), nicht mit Mangelentdeckung.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Mängel-Beschreibung und Zuordnung (subjektiv, objektiv, Montage)
- Mängelrecht-Stufenschema (Nacherfüllung → Minderung/Rücktritt → Schadensersatz)
- Fristsetzungs-Dokumentation
- Verjährungs-Berechnung

## Qualitätsregeln

- Fristsetzung und Entbehrlichkeitsalternativen immer vollständig prüfen.
- Verjährungsbeginn (Abnahme) von Mangelentdeckung strikt trennen.
- § 637 BGB-Selbstvornahme nur nach korrekter Fristsetzung annehmen.

## Anschluss-Skills

- werkvertrag-abnahme-und-faelligkeit
- werkvertrag-grundschema-paragraph-631
- verjaehrung-bgb-bt-spezial
- schadensrecht-paragraphen-249-253

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `deliktsrecht-haftung-fuer-verrichtungen-paragraph-831`

**Fokus:** Prüft Haftung für Verrichtungsgehilfen § 831 BGB: Verrichtungsgehilfe, Exkulpation und Schaden.

# Deliktsrecht: Haftung für Verrichtungen § 831 BGB

## Fachkern: Deliktsrecht: Haftung für Verrichtungen § 831 BGB
- **Spezialgegenstand:** Deliktsrecht: Haftung für Verrichtungen § 831 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Gehilfenhaftung nach § 831 BGB vollständig prüfen: Gehilfeneigenschaft, Schaden bei Ausführung der Verrichtung und Entlastungsbeweis des Geschäftsherrn.

## Normanker

- § 831 BGB: Haftung des Geschäftsherrn für Verrichtungsgehilfen
- § 278 BGB: Haftung des Schuldners für Erfüllungsgehilfen (Abgrenzung)
- § 823 BGB: deliktische Eigenhaftung des Verrichtungsgehilfen
- § 840 BGB: gesamtschuldnerische Haftung von Geschäftsherrn und Verrichtungsgehilfen
- § 31 BGB: Haftung für Organe (kein Exkulpationsmöglichkeit)

## Intake

- Wer ist der Geschäftsherr und wer ist der Verrichtungsgehilfe?
- Hat der Verrichtungsgehilfe eine unerlaubte Handlung begangen?
- Bestand ein Weisungsverhältnis und wurde die Handlung in Ausführung der Verrichtung begangen?
- Kann der Geschäftsherr darlegen, dass er sorgfältig ausgewählt, angeleitet und überwacht hat?
- Liegt eine Schadensersatzpflicht nach § 823 BGB auch des Verrichtungsgehilfen vor?

## Prüfraster

1. Verrichtungsgehilfe: weisungsgebundene Tätigkeit in Abhängigkeit vom Geschäftsherrn
2. Unerlaubte Handlung des Verrichtungsgehilfen nach §§ 823 ff. BGB
3. Zusammenhang mit der Verrichtung: Handlung in Ausführung (nicht nur bei Gelegenheit)
4. Kausalität und Schaden beim Geschädigten
5. Exkulpation nach § 831 Abs. 1 Satz 2 BGB: sorgfältige Auswahl, Instruktion und Überwachung
6. Dezentralisierte Unternehmen: Auswahl eines Leitungsverantwortlichen kann genügen
7. Gesamtschuld: Geschäftsherr und Verrichtungsgehilfe haften nach § 840 BGB als Gesamtschuldner
8. Regress des Geschäftsherrn gegen Verrichtungsgehilfen nach § 840 Abs. 2 BGB

## Fallstricke

- Handlung bei Gelegenheit der Verrichtung (nicht in Ausführung) löst keine § 831 BGB-Haftung aus.
- Exkulpationsbeweis ist schwierig; bloße formale Richtlinien reichen nicht aus.
- Bei juristischen Personen gilt § 31 BGB für Organe ohne Exkulpationsmöglichkeit.
- Verrichtungsgehilfe haftet daneben persönlich nach § 823 BGB.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Gehilfenhaftungs-Schema (Geschäftsherr, Gehilfe, Schaden, Zusammenhang)
- Exkulpations-Checkliste
- Gesamtschuldnerische Haftungsmatrix
- Risikoampel und Handlungsempfehlungen

## Qualitätsregeln

- In-Ausführung vs. bei-Gelegenheit immer klar abgrenzen.
- Exkulpationsbeweis vollständig aufnehmen und würdigen.
- § 31 BGB und § 831 BGB nicht verwechseln.

## Anschluss-Skills

- delikt-organisationspflicht
- deliktsrecht-paragraph-823-1
- delikt-vertrag-konkurrenz
- produzentenhaftung-und-verkehrssicherung


## Quellen

- https://www.gesetze-im-internet.de/bgb/__831.html
- https://www.gesetze-im-internet.de/bgb/__823.html
- https://www.gesetze-im-internet.de/bgb/__276.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `kaufrecht-schadensersatz-aufwendungsersatz`

**Fokus:** Prüft Schadensersatz §§ 437 Nr. 3 und 280 ff. BGB sowie Aufwendungsersatz § 284 BGB beim Kaufrecht.

# Kaufrecht: Schadensersatz und Aufwendungsersatz

## Fachkern: Kaufrecht: Schadensersatz und Aufwendungsersatz
- **Spezialgegenstand:** Kaufrecht: Schadensersatz und Aufwendungsersatz; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Schadensersatzansprüche des Käufers bei Sachmangel nach §§ 437 Nr. 3 und 280 BGB sowie Aufwendungsersatz nach § 284 BGB prüfen.

## Normanker

- § 437 Nr. 3 BGB: Schadensersatz und Aufwendungsersatz als Käuferrecht
- § 280 Abs. 1 BGB: Schadensersatz wegen Pflichtverletzung
- § 281 BGB: Schadensersatz statt der Leistung nach Fristsetzung
- § 283 BGB: Schadensersatz bei Unmöglichkeit
- § 284 BGB: Aufwendungsersatz statt Schadensersatz
- § 311a BGB: anfängliche Unmöglichkeit
- § 249 BGB: Naturalrestitution; § 252 BGB: entgangener Gewinn

## Intake

- Liegt ein Sachmangel vor, der zum Schadensersatz berechtigt?
- Wurde eine Nachfrist gesetzt und ist sie erfolglos abgelaufen?
- Welche Schäden sind entstanden: Mangelfolgeschäden, entgangener Gewinn, nutzlose Aufwendungen?
- Kommt Aufwendungsersatz nach § 284 BGB in Betracht?
- Liegt anfängliche Unmöglichkeit oder nachträgliche Pflichtverletzung vor?

## Prüfraster

1. Pflichtverletzung: Sachmangel bei Gefahrübergang (§ 434 BGB)
2. Vertretenmüssen des Verkäufers: Verschulden nach § 276 BGB
3. Schadensersatz neben der Leistung: § 280 Abs. 1 BGB (Mangelfolgeschäden ohne Fristsetzung)
4. Schadensersatz statt der Leistung: § 281 BGB (Fristsetzung erforderlich, außer § 281 Abs. 2 BGB)
5. Kleiner vs. großer Schadensersatz: kleiner (Verbleib Sache) vs. großer (Rückgabe Sache)
6. Aufwendungsersatz nach § 284 BGB: statt Schadensersatz; vergebliche Aufwendungen im Vertrauen auf Leistungserhalt
7. Differenzhypothese für Schadensberechnung
8. Verjährung: § 438 BGB; Beweislastumkehr § 477 BGB

## Fallstricke

- Schadensersatz neben der Leistung und statt der Leistung müssen klar getrennt werden.
- Aufwendungsersatz nach § 284 BGB ist kein Schadensersatz; andere Voraussetzungen.
- Mangelfolgeschäden können ohne Fristsetzung geltend gemacht werden.
- § 284 BGB und § 281 BGB schließen sich gegenseitig aus (kein gleichzeitiger Antrag).
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Schadensersatz-Auswahl (neben/statt Leistung)
- Schadenspositionen-Liste
- Aufwendungsersatz-Berechnung
- Risikoampel und Handlungsempfehlung

## Qualitätsregeln

- Kleinen und großen Schadensersatz immer explizit unterscheiden.
- § 284 BGB als Alternative zu § 281 BGB in Betracht ziehen.
- Vertretenmüssen des Verkäufers nie pauschal annehmen.

## Anschluss-Skills

- kaufrecht-nacherfuellung-ruecktritt-minderung
- schadensrecht-paragraphen-249-253
- kaufrecht-sachmangel-paragraph-434
- workflow-output-gutachten-klage-brief


## Quellen

- https://www.gesetze-im-internet.de/bgb/__437.html
- https://www.gesetze-im-internet.de/bgb/__280.html
- https://www.gesetze-im-internet.de/bgb/__284.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
