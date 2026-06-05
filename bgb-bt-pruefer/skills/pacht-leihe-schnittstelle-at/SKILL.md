---
name: pacht-leihe-schnittstelle-at
description: "Pacht Leihe Schnittstelle AT: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Pacht Leihe Schnittstelle AT

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Pacht Leihe Schnittstelle AT** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `pacht-leihe-und-verwahrung` | Pacht §§ 581 ff., Leihe §§ 598 ff. und Verwahrung §§ 688 ff. BGB: Pflichten, Haftung und Abgrenzung. |
| `schnittstelle-bgb-at-methodenlehre-agb` | Schnittstelle BGB-AT, Methodenlehre und AGB-Recht §§ 305-310 BGB: Einbeziehung, Inhaltskontrolle, Transparenz. |
| `schuldversprechen-schuldanerkenntnis` | Schuldversprechen § 780 BGB und Schuldanerkenntnis § 781 BGB: Form, Wirkung und Abgrenzung. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Pacht Leihe Schnittstelle AT**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `pacht-leihe-und-verwahrung`

**Fokus:** Pacht §§ 581 ff., Leihe §§ 598 ff. und Verwahrung §§ 688 ff. BGB: Pflichten, Haftung und Abgrenzung.

# Pacht, Leihe und Verwahrung BGB

## Fachkern: Pacht, Leihe und Verwahrung BGB
- **Spezialgegenstand:** Pacht, Leihe und Verwahrung BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Pachtverhältnisse (§§ 581 ff. BGB), Leihe (§§ 598 ff. BGB) und Verwahrung (§§ 688 ff. BGB) prüfen: Abgrenzung zur Miete, spezifische Pflichten und Haftungsregeln.

## Normanker

- §§ 581 ff. BGB: Pachtvertrag (Fruchtziehungsrecht)
- § 585 BGB: Landpacht als Sonderform
- §§ 598 ff. BGB: Leihe (unentgeltliche Gebrauchsüberlassung)
- § 600 BGB: Haftungsprivileg des Verleihers
- §§ 688 ff. BGB: Verwahrung (entgeltlich und unentgeltlich)
- § 690 BGB: Haftungsprivileg bei unentgeltlicher Verwahrung

## Intake

- Welcher Vertragstyp liegt vor (Pacht, Leihe, Verwahrung)?
- Ist Entgeltlichkeit oder Unentgeltlichkeit vereinbart?
- Besteht Fruchtziehungsrecht (dann Pacht statt Miete)?
- Welches Problem liegt vor (Haftung, Kündigung, Rückgabe, Beschädigung)?
- Gelten Sonderregeln für Landpacht?

## Prüfraster

1. Vertragstyp-Abgrenzung: Miete (nur Gebrauchsüberlassung) vs. Pacht (Gebrauchsüberlassung plus Fruchtziehungsrecht)
2. Pachtrecht: Anwendung der Mietrechtsregeln (§ 581 Abs. 2 BGB) soweit keine Sonderregeln
3. Landpacht nach §§ 585 ff. BGB: Schriftformerfordernis, Pachtzins, Pächterrechte
4. Leihe: unentgeltlich (§ 598 BGB); Abgrenzung zur Schenkung und Miete
5. Leihe-Haftung: Verleiher haftet nach § 600 BGB nur für arglistig verschwiegene Mängel
6. Leihe-Kündigung: § 604 BGB (Rückgabe nach Gebrauch oder nach vereinbarter Zeit)
7. Verwahrung: Pflichten des Verwahrers (Aufbewahrung, Herausgabe, § 688 BGB)
8. Haftungsprivileg bei unentgeltlicher Verwahrung: § 690 BGB (nur eigenübliche Sorgfalt)

## Fallstricke

- Fruchtziehungsrecht entscheidet über Pacht oder Miete; Abgrenzung hat Auswirkungen auf Mieterschutzrecht.
- Leihe ist stets unentgeltlich; auch nur nominale Gegenleistung kann zur Miete führen.
- Bei Verwahrung muss zwischen entgeltlicher (§ 688 BGB) und unentgeltlicher Verwahrung (§ 690 BGB) unterschieden werden.
- Landpacht unterliegt besonderen öffentlich-rechtlichen Beschränkungen.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Vertragstyp-Einordnung (Pacht, Miete, Leihe, Verwahrung)
- Pflichten-Matrix für beide Vertragsparteien
- Haftungsregeln je nach Vertragstyp
- Kündigung und Rückgabe-Schema

## Qualitätsregeln

- Fruchtziehungsrecht als Abgrenzungsmerkmal Pacht/Miete immer explizit prüfen.
- Haftungsprivilegien bei unentgeltlichen Verträgen (§§ 600 und 690 BGB) beachten.
- Landpacht-Sonderregeln nicht vergessen.

## Anschluss-Skills

- mietvertrag-grundschema-paragraph-535
- auftrag-und-unentgeltliche-taetigkeit
- vertragstypen-mischvertrag-router


## Quellen

- https://www.gesetze-im-internet.de/bgb/__581.html
- https://www.gesetze-im-internet.de/bgb/__598.html
- https://www.gesetze-im-internet.de/bgb/__688.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `schnittstelle-bgb-at-methodenlehre-agb`

**Fokus:** Schnittstelle BGB-AT, Methodenlehre und AGB-Recht §§ 305-310 BGB: Einbeziehung, Inhaltskontrolle, Transparenz.

# Schnittstelle BGB-AT, Methodenlehre und AGB §§ 305-310 BGB

## Fachkern: Schnittstelle BGB-AT, Methodenlehre und AGB §§ 305-310 BGB
- **Spezialgegenstand:** Schnittstelle BGB-AT, Methodenlehre und AGB §§ 305-310 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

AGB-Recht nach §§ 305-310 BGB mit BGB-AT-Methodenlehre verknüpfen: Einbeziehungskontrolle, Auslegung (§ 305c Abs. 2 BGB), Inhaltskontrolle und Rechtsfolgen bei Unwirksamkeit.

## Normanker

- §§ 305 ff. BGB: Allgemeine Geschäftsbedingungen
- § 305 BGB: AGB-Begriff (vorformuliert, für Vielzahl von Verträgen, gestellt)
- § 305c BGB: Überraschende und mehrdeutige Klauseln
- § 307 BGB: Inhaltskontrolle, unangemessene Benachteiligung
- § 308 BGB: Klauselverbote mit Wertungsmöglichkeit
- § 309 BGB: Klauselverbote ohne Wertungsmöglichkeit
- § 310 BGB: Anwendungsbereich (B2B vs. B2C)

## Intake

- Liegt eine AGB-Situation vor (vorformuliert, für viele Verträge, eine Seite hat gestellt)?
- In welchem Vertragstyp kommen die AGB vor (Kauf, Miete, Werkvertrag, Dienstleistung)?
- Welche konkrete Klausel ist problematisch?
- B2B oder B2C (unterschiedliche Kontrolldichte)?
- Wurde die AGB wirksam einbezogen (Hinweis, Möglichkeit zur Kenntnisnahme, Einverständnis)?

## Prüfraster

1. AGB-Tatbestand nach § 305 BGB: vorformuliert, für Vielzahl von Verträgen bestimmt, von einer Partei gestellt
2. Einbeziehungskontrolle: ausdrücklicher Hinweis, Möglichkeit der Kenntnisnahme, Einverständnis (§ 305 Abs. 2 BGB)
3. Überraschende Klauseln nach § 305c Abs. 1 BGB: nicht Vertragsinhalt geworden
4. Auslegung nach § 305c Abs. 2 BGB: Unklarheiten gehen zu Lasten des Verwenders
5. Inhaltskontrolle nach § 307 BGB: wesentliche Grundgedanken des dispositiven Rechts; Generalklausel
6. Klauselverbote nach §§ 308 und 309 BGB: Liste typischer unwirksamer Klauseln
7. B2B vs. B2C: § 310 Abs. 1 BGB schränkt Anwendungsbereich für kaufmännische Verträge ein
8. Rechtsfolge der Unwirksamkeit: § 306 BGB (Vertrag im Übrigen wirksam; gesetzliche Regelung tritt ein)

## Fallstricke

- Individuelle Vereinbarung ist keine AGB; auch wenn vorformuliert und für ein Massengeschäft bestimmt.
- § 307 BGB gilt auch im B2B-Bereich; Kontrolldichte ist aber geringer als gegenüber Verbrauchern.
- Transparenzgebot des § 307 Abs. 1 S. 2 BGB: Klausel muss verständlich und klar sein.
- Kumulation von Klauseln: einzelne wirksame Klauseln können zusammen unwirksam sein.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- AGB-Klausel-Prüfprotokoll (Einbeziehung, Überraschungsklausel, Inhaltskontrolle)
- Wirksamkeitsmatrix nach §§ 307-309 BGB
- B2B/B2C-Unterscheidungsübersicht
- Vertragsgestaltungsempfehlungen

## Qualitätsregeln

- AGB-Tatbestand und individuelle Vereinbarung immer als erste Weiche prüfen.
- Rechtsfolge des § 306 BGB (gesetzliche Ersatzregelung) bei unwirksamen Klauseln stets mitdenken.
- B2B-Situation schließt AGB-Kontrolle nicht aus.

## Anschluss-Skills

- bt-vertragsentwurf-modellvertrag
- kaufvertrag-grundschema-paragraph-433
- mietvertrag-grundschema-paragraph-535
- werkvertrag-grundschema-paragraph-631


## Quellen

- https://www.gesetze-im-internet.de/bgb/__305.html
- https://www.gesetze-im-internet.de/bgb/__307.html
- https://www.gesetze-im-internet.de/bgb/__309.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `schuldversprechen-schuldanerkenntnis`

**Fokus:** Schuldversprechen § 780 BGB und Schuldanerkenntnis § 781 BGB: Form, Wirkung und Abgrenzung.

# Schuldversprechen und Schuldanerkenntnis §§ 780 und 781 BGB

## Fachkern: Schuldversprechen und Schuldanerkenntnis §§ 780 und 781 BGB
- **Spezialgegenstand:** Schuldversprechen und Schuldanerkenntnis §§ 780 und 781 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Schuldversprechen (§ 780 BGB) und Schuldanerkenntnis (§ 781 BGB) prüfen: Formerfordernisse, rechtliche Wirkungen, Abgrenzung zum abstrakten Schuldversprechen und zu Beweiszwecken dienenden Erklärungen.

## Normanker

- § 780 BGB: Schuldversprechen (abstrakt, formgebunden)
- § 781 BGB: Schuldanerkenntnis (abstrakt, formgebunden)
- § 782 BGB: Erlass der Formvorschriften bei Schuldversprechen und Schuldanerkenntnis
- § 812 BGB: Bereicherungsrecht als Rückabwicklungsgrundlage
- § 821 BGB: Einrede der ungerechtfertigten Bereicherung

## Intake

- Liegt ein abstraktes Schuldversprechen (§ 780 BGB) oder ein Schuldanerkenntnis (§ 781 BGB) vor?
- Wurde die Schriftform (§§ 780 und 781 BGB) eingehalten?
- Zu welchem Zweck wurde die Erklärung abgegeben (Beweis, Novation, Sicherheit)?
- Besteht ein kausaler Bezug zur Grundschuld oder zum ursprünglichen Schuldverhältnis?
- Gibt es Einwendungen aus dem Kausalverhältnis?

## Prüfraster

1. Qualifikation: abstraktes Schuldversprechen (§ 780 BGB) oder Schuldanerkenntnis (§ 781 BGB)?
2. Abgrenzung zum kausalen (deklaratorischen) Anerkenntnis: kein Formzwang, nur Beweisfunktion
3. Formerfordernis der Schriftform: §§ 780 und 781 BGB i.V.m. § 126 BGB; Ausnahme § 782 BGB
4. Wirkung des abstrakten Schuldversprechens: eigenständige Verbindlichkeit losgelöst vom Grundverhältnis
5. Einrede der Bereicherung nach § 821 BGB: wenn Kausalverhältnis nicht besteht oder wegfällt
6. Bereicherungsrückforderung nach § 812 BGB falls abstraktes Schuldversprechen ohne Rechtsgrund
7. Unterschied zu Bürgschaft (§ 765 BGB) und Garantie (keine Formvorschrift im BGB)

## Fallstricke

- Kausales (deklaratorisches) Anerkenntnis hat keine Formvorschrift; Verwechslung mit § 781 BGB führt zu Fehlern.
- Ohne Schriftform ist abstraktes Schuldversprechen nach § 780 BGB nichtig (§ 125 BGB).
- § 782 BGB: Im kaufmännischen Bereich kann Formerfordernis durch Handelsbräuche abdingbar sein.
- Einrede der Bereicherung (§ 821 BGB) verhindert nicht die wirksame Entstehung der abstrakten Schuld.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Einordnungsmatrix (abstrakt vs. kausal, Schuldversprechen vs. Anerkenntnis)
- Formwirksamkeits-Check
- Einwendungs-Analyse (§ 821 BGB, Kausalverhältnis)
- Gestaltungsempfehlung

## Qualitätsregeln

- Abstraktes und kausales Anerkenntnis immer getrennt behandeln.
- Schriftformerfordernis bei §§ 780 und 781 BGB immer prüfen.
- § 821 BGB als Einrede, nicht als Unwirksamkeitsgrund, einordnen.

## Anschluss-Skills

- buergschaft-grundschema-paragraph-765
- bereicherungsrecht-leistungskondiktion
- bt-fristen-erklaerungen-zugang


## Quellen

- https://www.gesetze-im-internet.de/bgb/__780.html
- https://www.gesetze-im-internet.de/bgb/__781.html
- https://www.gesetze-im-internet.de/bgb/__812.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
