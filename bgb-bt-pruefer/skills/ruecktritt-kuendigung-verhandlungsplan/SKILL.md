---
name: ruecktritt-kuendigung-verhandlungsplan
description: "Ruecktritt Kuendigung Verhandlungsplan: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Ruecktritt Kuendigung Verhandlungsplan

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Ruecktritt Kuendigung Verhandlungsplan** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-fristen-ruecktritt-kuendigung` | Fristen, Rücktritt und Kündigung im BGB BT: Fristsetzung, Rücktrittsrecht, Kündigungsrecht, Rechtsfolgen. |
| `workflow-vergleich-und-verhandlungsplan` | Vergleich und Verhandlungsplan im BGB BT: Vergleichskorridore, Verhandlungsführung, Dokumentation. |
| `bt-fristen-erklaerungen-zugang` | Prüft Fristen, Erklärungen und Zugang im Schuldrecht BT: Rücktritt, Kündigung, Mahnung, Mängelrüge und Nachfrist. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Ruecktritt Kuendigung Verhandlungsplan**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `workflow-fristen-ruecktritt-kuendigung`

**Fokus:** Fristen, Rücktritt und Kündigung im BGB BT: Fristsetzung, Rücktrittsrecht, Kündigungsrecht, Rechtsfolgen.

# Workflow: Fristen, Rücktritt und Kündigung

## Zweck

Fristsetzung, Rücktrittsrecht und Kündigung bei BGB-BT-Verträgen vollständig prüfen: wann ist eine Frist erforderlich, wann entbehrlich, Rechtsfolgen des Rücktritts nach §§ 346 ff. BGB und Kündigungsrecht.

## Normanker

- § 281 BGB: Schadensersatz statt Leistung (Fristsetzung als Grundvoraussetzung)
- § 323 BGB: Rücktritt wegen Nichtleistung oder Schlechtleistung
- § 324 BGB: Rücktritt bei Verletzung einer Pflicht nach § 241 Abs. 2 BGB
- §§ 346 ff. BGB: Rechtsfolgen des Rücktritts (Rückgewährkette)
- §§ 542 und 573 BGB: Kündigung von Mietverträgen
- §§ 621 und 627 BGB: Kündigung von Dienstverträgen
- §§ 648 und 648a BGB: Kündigung von Werkverträgen

## Intake

- Welche Pflichtverletzung liegt vor (Nichtleistung, Schlechtleistung, Nebenpflichtverletzung)?
- Wurde eine Frist gesetzt und ist sie abgelaufen?
- Ist die Fristsetzung entbehrlich (ernsthafte Verweigerung, Fixgeschäft)?
- Wird Rücktritt oder Kündigung angestrebt?
- Was ist das Vertragsverhältnis (Dauerschuldverhältnis → Kündigung; einmaliges Schuldverhältnis → Rücktritt)?

## Prüfraster

1. Pflichtverletzungs-Art bestimmen: Nicht- oder Schlechtleistung, Nebenpflichtverletzung
2. Fristsetzungserfordernis: § 323 und § 281 BGB (Grundregel: Frist erforderlich)
3. Entbehrlichkeit der Frist: ernsthafte und endgültige Weigerung, Fixgeschäft, besondere Umstände
4. Rücktritt (§ 323 BGB): bei Nichterfüllung nach Fristablauf; Gestaltungsrecht
5. Dauerschuldverhältnisse: statt Rücktritt Kündigung nach §§ 314 und 543 BGB
6. Rechtsfolgen des Rücktritts: §§ 346 ff. BGB (Rückgewähr, Wertersatz, Nutzungsherausgabe)
7. Kündigung-Typen: ordentlich vs. außerordentlich; Fristen je nach Vertragstyp
8. Form und Zugang: Rücktritt und Kündigung sind empfangsbedürftige Gestaltungsrechte

## Fallstricke

- Fristsetzung zu kurz: keine angemessene Zeit gewährt; Rücktritt unwirksam.
- Bei Dauerschuldverhältnissen ist Rücktritt oft ausgeschlossen; nur Kündigung möglich.
- Rücktritt macht Rückgewähr erforderlich (§§ 346 ff. BGB); Kosten und Wertersatz beachten.
- Widerruf von Gestaltungsrechten (Rücktritt, Kündigung) grundsätzlich nicht möglich.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Fristsetzungs-Prüfungsschema
- Rücktritts- vs. Kündigungsanalyse
- Rechtsfolgen-Matrix (Rückgewähr, Wertersatz)
- Handlungsempfehlung mit Formulierungsvorschlag

## Qualitätsregeln

- Angemessenheit der Frist immer sachverhaltsbezogen bestimmen.
- Dauerschuldverhältnis-Abgrenzung vor Rücktritt prüfen.
- Form und Zugang des Gestaltungsrechts dokumentieren.

## Anschluss-Skills

- workflow-output-gutachten-klage-brief
- bt-fristen-erklaerungen-zugang
- schadensrecht-paragraphen-249-253
- werkvertrag-abnahme-und-faelligkeit


## Quellen

- https://www.gesetze-im-internet.de/bgb/__323.html
- https://www.gesetze-im-internet.de/bgb/__346.html
- https://www.gesetze-im-internet.de/bgb/__314.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `workflow-vergleich-und-verhandlungsplan`

**Fokus:** Vergleich und Verhandlungsplan im BGB BT: Vergleichskorridore, Verhandlungsführung, Dokumentation.

# Workflow: Vergleich und Verhandlungsplan

## Zweck

Vergleichsverhandlungen im BGB-BT-Mandat vorbereiten und durchführen: Vergleichskorridore bestimmen, Verhandlungsstrategie festlegen, Vergleichsvertrag gestalten und rechtlich prüfen.

## Normanker

- § 779 BGB: Vergleichsvertrag (gegenseitiges Nachgeben)
- § 397 BGB: Erlass (einseitiger Verzicht)
- § 781 BGB: Schuldanerkenntnis
- § 254 BGB: Mitverschulden (beeinflusst Vergleichskorridor)
- § 794 ZPO: Vollstreckungstitel durch gerichtlichen Vergleich
- BRAO §§ 43a und 49 ff.: Anwaltliche Pflichten bei Vergleichsverhandlungen

## Intake

- Was ist das Verhandlungsziel des Mandanten (maximale Forderung, Minimalakzeptanz)?
- Wie hoch ist das Prozesskostenrisiko im Klagefall?
- Was sind die starken und schwachen Punkte der eigenen Position?
- Gibt es zeitlichen oder wirtschaftlichen Druck für den Mandanten?
- Soll der Vergleich als gerichtlicher Vergleich (Vollstreckungstitel) oder außergerichtlich geschlossen werden?

## Prüfraster

1. Verhandlungsziel definieren: Maximalforderung, Verhandlungsspielraum, Minimalakzeptanz
2. BATNA bestimmen: Best Alternative To Negotiated Agreement; was passiert ohne Vergleich?
3. Gegenseiten-BATNA abschätzen: welchen Druck hat die Gegenseite zum Vergleich?
4. Vergleichskorridor berechnen: zwischen eigenem Mindestbetrag und Gegenseiten-Maximum
5. Verhandlungsstrategie: Angebot-Abfolge, Zugeständnisse planen, Verhandlungsführung
6. Vergleichsvertrag: § 779 BGB-Anforderungen (gegenseitiges Nachgeben, schriftlich empfohlen)
7. Vollständigkeit des Vergleichs: alle Streitpunkte regeln; keine offenen Fragen lassen
8. Vollstreckungstitel: gerichtlicher Vergleich nach § 794 ZPO für sofortige Vollstreckbarkeit

## Fallstricke

- Vergleichsvertrag regelt nicht alle Streitpunkte; neuer Streit entsteht.
- Gegenseitiges Nachgeben fehlt: dann kein Vergleich nach § 779 BGB, sondern Erlass.
- Vollstreckungstitel-Option nicht genutzt: Vollstreckung erfordert später erneuten Klageweg.
- Mandant nicht ausreichend über Prozesskostenrisiko und Vergleichsalternative aufgeklärt.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Verhandlungsplan mit Zielen und Zugeständnisstrategie
- Vergleichskorridor-Berechnung
- Vergleichsvertrag-Entwurf
- Vollstreckungssicherungs-Empfehlung

## Qualitätsregeln

- BATNA immer vor Verhandlung bestimmen; ohne Alternative keine Verhandlungsmacht.
- Vergleichsvertrag auf § 779 BGB-Vollständigkeit prüfen.
- Vollstreckungstitel-Option aktiv ansprechen.

## Anschluss-Skills

- vergleich-paragraph-779
- workflow-red-team-gegenseite
- workflow-output-gutachten-klage-brief
- bt-fristen-erklaerungen-zugang


## Quellen

- https://www.gesetze-im-internet.de/bgb/__779.html
- https://www.gesetze-im-internet.de/bgb/__397.html
- https://www.gesetze-im-internet.de/zpo/__794.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `bt-fristen-erklaerungen-zugang`

**Fokus:** Prüft Fristen, Erklärungen und Zugang im Schuldrecht BT: Rücktritt, Kündigung, Mahnung, Mängelrüge und Nachfrist.

# BT-Fristen, Erklärungen und Zugang

## Fachkern: BT-Fristen, Erklärungen und Zugang
- **Spezialgegenstand:** BT-Fristen, Erklärungen und Zugang; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Fristen und empfangsbedürftige Willenserklärungen im Schuldrecht BT prüfen: Zugang, Wirksamkeit und Rechtsfolgen von Rücktritt, Kündigung, Mahnung und Nachfrist.

## Normanker

- § 130 BGB: Zugang empfangsbedürftiger Willenserklärungen
- § 132 BGB: Zugang durch Gerichtsvollzieher
- §§ 186–193 BGB: Fristberechnung
- § 281 BGB: Fristsetzung zur Nacherfüllung vor Schadensersatz
- § 323 BGB: Rücktrittsvoraussetzungen und Fristsetzung
- § 349 BGB: Rücktrittserklärung
- §§ 542 ff. BGB: außerordentliche Kündigung im Mietrecht
- § 626 BGB: außerordentliche Kündigung im Dienstverhältnis
- § 634 Nr. 1 und 2 BGB: Nacherfüllung und Fristsetzung im Werkvertragsrecht

## Intake

- Welche Erklärung wird geprüft: Rücktritt, Kündigung, Mahnung oder Mängelrüge?
- Wann und wie wurde die Erklärung abgesandt und dem Empfänger zugegangen?
- Welche Frist wurde gesetzt und ist sie angemessen?
- Liegt ein Fall vor, in dem es keiner Fristsetzung bedarf (§ 323 Abs. 2 BGB)?
- Wurden Fristen durch Hemmung oder Neubeginn der Verjährung beeinflusst?

## Prüfraster

1. Zugang der Erklärung nach § 130 BGB bestimmen: Zeitpunkt, Ort, Empfangsbotin
2. Fristberechnung nach §§ 186–193 BGB (Fristbeginn, Fristende, Sonntag/Feiertag)
3. Angemessenheit der Nachfrist nach § 281 oder § 323 BGB
4. Ausnahmen von der Fristsetzungspflicht: § 323 Abs. 2 BGB (ernsthafte Verweigerung, besonderer Termin)
5. Rechtsfolge bei abgelaufener Frist: Rücktrittsrecht, Schadensersatz statt der Leistung
6. Wirksamkeit der Rücktrittserklärung nach § 349 BGB: empfangsbedürftige Willenserklärung
7. Wirksamkeit der Kündigung: Form, Frist, Begründungspflicht je nach Vertragstyp
8. Beweissicherung: Einschreiben, Bote, Fax-Sendebericht, elektronische Zustellung

## Fallstricke

- Frist beginnt erst mit Zugang der Nachfristierungserklärung, nicht mit Abgabe.
- Zu kurze Nachfrist wird automatisch auf angemessene Frist verlängert (h.M.).
- Rücktritt per E-Mail ist zugegangen, wenn sie in den Machtbereich des Empfängers gelangt ist.
- Kündigung per Telefon oder WhatsApp kann formwidrig sein (z.B. § 568 BGB Schriftform).
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Fristkalender mit Berechnungsschritten
- Zugangsdokumentation
- Rücktritts-/Kündigungsvoraussetzungen-Checkliste
- Beweissicherungshinweise

## Qualitätsregeln

- Zugang immer von Abgabe und Absendung trennen.
- Nachfrist-Angemessenheit nach Art und Umfang der Leistung beurteilen.
- Bei elektronischen Erklärungen Zugangsfiktion und AGB-Klauseln prüfen.

## Anschluss-Skills

- werkvertrag-abnahme-und-faelligkeit
- mietrecht-mangel-minderung
- workflow-fristen-ruecktritt-kuendigung
- kaufrecht-nacherfuellung-ruecktritt-minderung

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
