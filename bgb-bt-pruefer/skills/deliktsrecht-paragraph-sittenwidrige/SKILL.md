---
name: deliktsrecht-paragraph-sittenwidrige
description: "Deliktsrecht Paragraph Sittenwidrige: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Deliktsrecht Paragraph Sittenwidrige

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Deliktsrecht Paragraph Sittenwidrige** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `deliktsrecht-paragraph-823-1` | Prüft Rechtsgutsverletzung, Handlung, Kausalität, Rechtswidrigkeit, Verschulden und Schaden nach § 823 Abs. 1 BGB. |
| `deliktsrecht-paragraph-826-sittenwidrige-schaedigung` | Prüft sittenwidrige vorsätzliche Schädigung § 826 BGB: Sittenwidrigkeit, Vorsatz und Vermögensschaden. |
| `deliktsrecht-schutzgesetz-paragraph-823-2` | Prüft Schutzgesetzverletzung § 823 Abs. 2 BGB: Schutzgesetz-Eigenschaft, Tatbestand und Schutzzweck. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Deliktsrecht Paragraph Sittenwidrige**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `deliktsrecht-paragraph-823-1`

**Fokus:** Prüft Rechtsgutsverletzung, Handlung, Kausalität, Rechtswidrigkeit, Verschulden und Schaden nach § 823 Abs. 1 BGB.

# Deliktsrecht § 823 Abs. 1 BGB

## Fachkern: Deliktsrecht § 823 Abs. 1 BGB
- **Spezialgegenstand:** Deliktsrecht § 823 Abs. 1 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Den Grundtatbestand des Deliktsrechts nach § 823 Abs. 1 BGB vollständig prüfen: geschützte Rechtsgüter, Tatbestand, Rechtswidrigkeit, Verschulden und Schaden.

## Normanker

- § 823 Abs. 1 BGB: Leben, Körper, Gesundheit, Freiheit, Eigentum und sonstige Rechte
- § 249 BGB: Naturalrestitution als Primärform des Schadensersatzes
- § 253 BGB: immaterieller Schadensersatz (Schmerzensgeld)
- §§ 827 und 828 BGB: Verschuldensfähigkeit
- § 254 BGB: Mitverschulden des Geschädigten
- § 840 BGB: Gesamtschuld bei mehreren Schädigern
- §§ 195 und 199 BGB: Verjährungsfrist (drei Jahre ab Kenntnis)

## Intake

- Welches Rechtsgut ist verletzt: Körper, Gesundheit, Eigentum, allgemeines Persönlichkeitsrecht?
- Wer hat die verletzende Handlung begangen und wann?
- Ist die Kausalität zwischen Handlung und Schaden nachweisbar?
- Ist der Schädiger verschuldensfähig (§§ 827 und 828 BGB)?
- Liegt ein Mitverschulden des Geschädigten vor?

## Prüfraster

1. Rechtsgutsverletzung: Körper, Gesundheit, Freiheit, Eigentum, sonstiges Recht bestimmen
2. Handlung: aktives Tun oder Unterlassen (Unterlassen nur wenn Garantenpflicht bestand)
3. Haftungsbegründende Kausalität: äquivalente Kausalität (conditio sine qua non)
4. Rechtswidrigkeit: Indikationsfunktion der Rechtsgutsverletzung; Rechtfertigungsgründe prüfen
5. Verschulden: Vorsatz oder Fahrlässigkeit nach § 276 BGB; Verschuldensfähigkeit (§§ 827 und 828 BGB)
6. Haftungsausfüllende Kausalität: konkreter Schaden und Zurechnung
7. Schaden nach §§ 249 ff. BGB: Naturalrestitution, Schadensersatz in Geld, Schmerzensgeld
8. Mitverschulden nach § 254 BGB und Verjährung nach §§ 195 und 199 BGB

## Fallstricke

- Sonstige Rechte nach § 823 Abs. 1 BGB (z.B. Recht am Gewerbebetrieb) werden restriktiv ausgelegt.
- Reines Vermögensschaden ist nicht durch § 823 Abs. 1 BGB geschützt (kein sonstiges Recht).
- Unterlassen als Handlung setzt Garantenpflicht voraus.
- Rechtswidrigkeit wird bei Rechtsgutsverletzung indiziert; Rechtfertigungsgründe müssen der Schuldner beweisen.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Tatbestandsprüfung § 823 Abs. 1 BGB im Gutachtenstil
- Kausalitätslinie mit Belegen
- Schadensberechnung (materiell und immateriell)
- Mitverschuldensprüfung

## Qualitätsregeln

- Haftungsbegründende und haftungsausfüllende Kausalität trennen.
- Reines Vermögensschaden immer über § 823 Abs. 2 BGB oder § 826 BGB prüfen.
- Verschuldensfähigkeit bei Minderjährigen und psychisch Erkrankten immer prüfen.

## Anschluss-Skills

- deliktsrecht-paragraph-826-sittenwidrige-schaedigung
- deliktsrecht-schutzgesetz-paragraph-823-2
- schadensrecht-paragraphen-249-253
- delikt-vertrag-konkurrenz


## Quellen

- https://www.gesetze-im-internet.de/bgb/__823.html
- https://www.gesetze-im-internet.de/bgb/__249.html
- https://www.gesetze-im-internet.de/bgb/__253.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `deliktsrecht-paragraph-826-sittenwidrige-schaedigung`

**Fokus:** Prüft sittenwidrige vorsätzliche Schädigung § 826 BGB: Sittenwidrigkeit, Vorsatz und Vermögensschaden.

# Deliktsrecht § 826 BGB: Sittenwidrige Schädigung

## Fachkern: Deliktsrecht § 826 BGB: Sittenwidrige Schädigung
- **Spezialgegenstand:** Deliktsrecht § 826 BGB: Sittenwidrige Schädigung; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

§ 826 BGB als Auffangtatbestand für vorsätzliche sittenwidrige Schädigungen prüfen: Sittenwidrigkeit des Verhaltens, bedingter Vorsatz und reiner Vermögensschaden.

## Normanker

- § 826 BGB: vorsätzliche sittenwidrige Schädigung
- § 138 BGB: Sittenwidrigkeit als Parallelwertung
- § 823 Abs. 2 BGB: Schutzgesetzverletzung (Abgrenzung)
- BGH-Rechtsprechung zu § 826 BGB (z.B. Dieselskandal): nur nach Live-Prüfung zitieren
- § 31 BGB: Organverantwortlichkeit für juristische Personen

## Intake

- Welches Verhalten wird als sittenwidrig bewertet?
- Hatte der Schädiger Vorsatz bezüglich der Schädigung (auch bedingter Vorsatz)?
- Ist ein Vermögensschaden entstanden?
- Ist der Schädiger eine natürliche Person oder eine juristische Person (§ 31 BGB)?
- Gibt es eine BGH-Linie, die dieses Verhalten erfasst (z.B. arglistige Täuschung, Marktmanipulation)?

## Prüfraster

1. Objektive Sittenwidrigkeit: Verstoß gegen das Anstandsgefühl aller billig und gerecht Denkenden
2. Schaden: reiner Vermögensschaden oder Verletzung eines nach § 823 Abs. 1 BGB geschützten Guts
3. Kausalität: sittenwidrige Handlung hat Schaden verursacht
4. Vorsatz: mindestens bedingter Vorsatz (dolus eventualis); bloße Fahrlässigkeit genügt nicht
5. Vorsatz auf Schädigungserfolg: Schädiger muss den Schaden als möglich vorausgesehen und in Kauf genommen haben
6. Bei juristischen Personen: Organzurechnung nach § 31 BGB
7. Schaden nach §§ 249 ff. BGB: auch entgangener Gewinn (§ 252 BGB)
8. Verjährung: §§ 195 und 199 BGB

## Fallstricke

- Fahrlässigkeit genügt nicht; mindestens bedingter Vorsatz auf Schädigungserfolg notwendig.
- Sittenwidrigkeit ist nicht dasselbe wie Rechtswidrigkeit; eigenständige Wertung erforderlich.
- § 826 BGB schützt auch reinen Vermögensschaden, § 823 Abs. 1 BGB tut das nicht.
- BGH-Rechtsprechung zum Dieselskandal ist fallbezogen; keine pauschale Übertragung.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Sittenwidrigkeits-Analyse mit Fallwertung
- Vorsatz-Dokumentation
- Schadensberechnung
- Risikoampel und Handlungsempfehlung

## Qualitätsregeln

- Sittenwidrigkeitswertung immer mit konkreten Tatsachen belegen.
- Vorsatz und Fahrlässigkeit klar abgrenzen.
- BGH-Entscheidungen nur nach Live-Prüfung mit Aktenzeichen verwenden.

## Anschluss-Skills

- deliktsrecht-paragraph-823-1
- deliktsrecht-schutzgesetz-paragraph-823-2
- schadensrecht-paragraphen-249-253
- workflow-red-team-gegenseite


## Quellen

- https://www.gesetze-im-internet.de/bgb/__826.html
- https://www.gesetze-im-internet.de/bgb/__138.html
- https://www.gesetze-im-internet.de/bgb/__823.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `deliktsrecht-schutzgesetz-paragraph-823-2`

**Fokus:** Prüft Schutzgesetzverletzung § 823 Abs. 2 BGB: Schutzgesetz-Eigenschaft, Tatbestand und Schutzzweck.

# Deliktsrecht: Schutzgesetz § 823 Abs. 2 BGB

## Fachkern: Deliktsrecht: Schutzgesetz § 823 Abs. 2 BGB
- **Spezialgegenstand:** Deliktsrecht: Schutzgesetz § 823 Abs. 2 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Haftung nach § 823 Abs. 2 BGB bei Verletzung eines Schutzgesetzes prüfen: Schutzgesetz-Eigenschaft, Tatbestandsverwirklichung, Schutzzweck und Schaden.

## Normanker

- § 823 Abs. 2 BGB: Haftung bei Verletzung eines Schutzgesetzes
- § 134 BGB: Nichtigkeit bei Gesetzesverstoß (parallele Frage)
- StGB-Tatbestände als Schutzgesetze: §§ 242 (Diebstahl), 263 (Betrug), 266 (Untreue) StGB
- Art. 32 DSGVO als Schutzgesetz (umstritten; Tendenz BGH: ja)
- Straßenverkehrsgesetz und weitere Sicherheitsgesetze als Schutzgesetze

## Intake

- Welche gesetzliche Norm soll als Schutzgesetz herangezogen werden?
- Dient die Norm zumindest auch dem Schutz des individuellen Geschädigten?
- Hat der Schädiger den Tatbestand der Schutznorm erfüllt?
- Ist der eingetretene Schaden vom Schutzzweck der Norm erfasst?
- Liegt Verschulden bezüglich der Schutznormverletzung vor?

## Prüfraster

1. Schutzgesetz-Eigenschaft: Norm muss zumindest auch individuellen Schutz bezwecken
2. Tatbestand der Schutznorm verwirklicht: vollständige Subsumtion unter die Schutznorm
3. Verschulden: Vorsatz oder Fahrlässigkeit bezüglich der Schutznormverletzung
4. Schutzzweckzusammenhang: eingetretener Schaden muss im Schutzbereich der Norm liegen
5. Kausalität: Schutznormverletzung hat Schaden verursacht
6. Schaden nach §§ 249 ff. BGB
7. Mitverschulden nach § 254 BGB
8. Verjährung: §§ 195 und 199 BGB; strafrechtliche Verjährung getrennt prüfen

## Fallstricke

- Reine Ordnungsvorschriften ohne individuellen Schutzcharakter sind keine Schutzgesetze.
- Schutzzweckzusammenhang muss für jeden Schadensposten einzeln geprüft werden.
- DSGVO Art. 32 als Schutzgesetz ist höchstrichterlich noch nicht abschließend geklärt.
- Tatbestandsverwirklichung der Schutznorm muss vollständig geprüft werden (keine verkürzte Prüfung).
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Schutzgesetz-Analyse (Norm, individueller Schutzcharakter, Tatbestand)
- Schutzzweckzusammenhang-Prüfung
- Schadensberechnung
- Risikoampel

## Qualitätsregeln

- Schutzgesetz-Eigenschaft immer selbst begründen, nicht als selbstverständlich annehmen.
- Schutzzweckzusammenhang für jeden Schadensposten gesondert prüfen.
- Bei strafrechtlichen Schutzgesetzen zivilrechtliche und strafrechtliche Verjährung trennen.

## Anschluss-Skills

- deliktsrecht-paragraph-823-1
- deliktsrecht-paragraph-826-sittenwidrige-schaedigung
- delikt-verkehrspflicht-digital
- workflow-anspruchslandkarte


## Quellen

- https://www.gesetze-im-internet.de/bgb/__823.html
- https://www.gesetze-im-internet.de/stgb/__263.html
- https://www.gesetze-im-internet.de/bgb/__249.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
