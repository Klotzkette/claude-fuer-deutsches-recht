---
name: paragraph-verjaehrung-werk-dienst
description: "Paragraph Verjaehrung Werk Dienst: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Paragraph Verjaehrung Werk Dienst

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Paragraph Verjaehrung Werk Dienst** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vergleich-paragraph-779` | Vergleich § 779 BGB: gegenseitiges Nachgeben, Irrtum über Grundlage, Widerruf und Abgrenzung. |
| `verjaehrung-bgb-bt-spezial` | Verjährung im BGB BT: Sonderfristen für Kauf §438, Miet §548, Werk §634a, Delikt §852 BGB. |
| `werk-dienst-abgrenzung-erfolg` | Werk-Dienst-Abgrenzung: Erfolgsschuldnerschaft § 631 BGB vs. Tätigkeitsschuldnerschaft § 611 BGB. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Paragraph Verjaehrung Werk Dienst**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vergleich-paragraph-779`

**Fokus:** Vergleich § 779 BGB: gegenseitiges Nachgeben, Irrtum über Grundlage, Widerruf und Abgrenzung.

# Vergleich § 779 BGB

## Fachkern: Vergleich § 779 BGB
- **Spezialgegenstand:** Vergleich § 779 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Vergleichsvertrag nach § 779 BGB prüfen: Voraussetzungen des gegenseitigen Nachgebens, Fehler über die Vergleichsgrundlage, Nichtigkeitsfolgen und Abgrenzung zum Erlass und zur Anerkenntnis.

## Normanker

- § 779 BGB: Vergleich (gegenseitiges Nachgeben zur Beilegung eines streitigen Rechtsverhältnisses)
- § 779 Abs. 1 Hs. 2 BGB: Nichtigkeit bei Irrtum über den als feststehend angesehenen Sachverhalt
- §§ 119 ff. BGB: Allgemeine Anfechtungsregeln ergänzend
- § 397 BGB: Erlass als Alternative zum Vergleich
- §§ 145 ff. BGB: Vertragsschluss-Allgemeinregeln

## Intake

- Liegt ein Vergleich vor (gegenseitiges Nachgeben, streitiges oder ungewisses Rechtsverhältnis)?
- Oder handelt es sich um einen einseitigen Erlass (§ 397 BGB) oder eine Anerkenntnis?
- Bestand ein Irrtum über den gemeinsamen Sachverhalt, den die Parteien als feststehend angenommen haben?
- Welches Recht des Vergleichs soll geprüft werden (Wirksamkeit, Anfechtung, Leistungsklage)?
- Wurde der Vergleich in einer prozessualen Form geschlossen (gerichtlicher Vergleich)?

## Prüfraster

1. Vergleichsbegriff: Beilegung eines Streits oder einer Ungewissheit durch gegenseitiges Nachgeben
2. Streitiges oder ungewisses Rechtsverhältnis: objektive Ungewissheit reicht; subjektiver Streit genügt
3. Gegenseitiges Nachgeben: beide Parteien müssen etwas aufgeben (nicht nur eine Seite)
4. Wirksamkeit: §§ 145 ff. BGB (Vertragsschluss); mögliche Formerfordernisse (z.B. Notarform bei Immobilien)
5. Nichtigkeit nach § 779 Abs. 1 Hs. 2 BGB: gemeinschaftlicher Irrtum über gemeinsam als feststehend angesehene Tatsachen
6. Abgrenzung zu Erlass (§ 397 BGB): einseitiger Verzicht auf Forderung; kein gegenseitiges Nachgeben nötig
7. Gerichtlicher Vergleich: zusätzliche prozessuale Wirkungen (Vollstreckungstitel, § 794 ZPO)
8. Widerrufsvorbehalt: im Anwaltsvergleich üblich; Folgen für Wirksamkeit

## Fallstricke

- Gegenseitiges Nachgeben fehlt wenn nur eine Seite verzichtet; dann Erlass oder Anerkenntnis.
- § 779 Abs. 1 Hs. 2 BGB: Irrtum muss die Vergleichsgrundlage betreffen; späterer Irrtum genügt nicht.
- Gerichtlicher Vergleich hat zusätzliche Wirkungen als Vollstreckungstitel; Widerruf beachten.
- Vorsorgevorbehalt (z.B. Steuervorbehalt) kann Endgültigkeit des Vergleichs einschränken.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Vergleichs-Wirksamkeits-Prüfung
- Irrtum-über-Vergleichsgrundlage-Analyse
- Abgrenzungsmatrix (Vergleich, Erlass, Anerkenntnis)
- Vollstreckungs-Optionen bei gerichtlichem Vergleich

## Qualitätsregeln

- Gegenseitiges Nachgeben als Kernmerkmal immer sachverhaltsnah belegen.
- Irrtum nach § 779 Abs. 1 Hs. 2 BGB nur bei gemeinsamem und vorherigem Sachverhaltsmerkmal anwenden.
- Prozessuale Wirkungen des gerichtlichen Vergleichs gesondert prüfen.

## Anschluss-Skills

- workflow-vergleich-und-verhandlungsplan
- schuldversprechen-schuldanerkenntnis
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

## 2. `verjaehrung-bgb-bt-spezial`

**Fokus:** Verjährung im BGB BT: Sonderfristen für Kauf §438, Miet §548, Werk §634a, Delikt §852 BGB.

# Verjährung BGB-BT Spezial

## Fachkern: Verjährung BGB-BT Spezial
- **Spezialgegenstand:** Verjährung BGB-BT Spezial; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Verjährungsfristen im BGB Besonderer Teil prüfen: Sonderfristen für Kaufrecht (§ 438 BGB), Mietrecht (§ 548 BGB), Werkvertragsrecht (§ 634a BGB), Deliktsrecht (§ 852 BGB) und deren Verhältnis zur Regelverjährung.

## Normanker

- § 438 BGB: Verjährung beim Kaufvertrag (2 Jahre; 5 Jahre für Bauwerke; 30 Jahre bei arglistigem Verschweigen)
- § 548 BGB: Verjährung bei Miet- und Pachtrecht (6 Monate nach Rückgabe)
- § 634a BGB: Verjährung beim Werkvertrag (2 Jahre; 5 Jahre für Bauwerke; 10 Jahre bei Arglist)
- § 852 BGB: Verjährung deliktischer Bereicherungsansprüche (10 Jahre)
- §§ 195 und 199 BGB: Regelverjährung (3 Jahre; Beginn mit Kenntnis oder grob fahrlässiger Unkenntnis)
- §§ 203 ff. BGB: Hemmung und Neubeginn der Verjährung

## Intake

- Welcher Vertragstyp oder Anspruchsgrundlage liegt vor?
- Wann begann die Verjährungsfrist (Lieferung, Abnahme, Rückgabe, Kenntnis)?
- Gibt es Hemmungstatbestände (Verhandlungen, Klage, Güteantrag)?
- Wurden Arglisttatbestände mitgeprüft?
- Ist die Frist möglicherweise bereits abgelaufen?

## Prüfraster

1. Anspruchsgrundlage und Sonderfristen-Norm bestimmen
2. Kaufrecht: § 438 Abs. 1 BGB (2 Jahre ab Übergabe; 5 Jahre für Bauwerke; 30 Jahre bei Arglist)
3. Mietrecht: § 548 Abs. 1 BGB (6 Monate nach Rückgabe) für Vermieterersatzansprüche
4. Werkvertragsrecht: § 634a BGB (2 Jahre bei Bewegungssachen; 5 Jahre für Bauwerke)
5. Deliktsrecht: §§ 195 und 199 BGB (3 Jahre ab Kenntnis); § 852 BGB für Bereicherungsanspruch (10 Jahre)
6. Hemmungstatbestände: §§ 203-213 BGB (Verhandlungen, gerichtliche Geltendmachung)
7. Neubeginn nach § 212 BGB: Anerkenntnis, Abschlagszahlung, Sicherheitsleistung
8. Arglist-Verlängerungen: § 438 Abs. 3 und § 634a Abs. 3 BGB

## Fallstricke

- § 548 BGB (Miet) beginnt mit Rückgabe der Mietsache, nicht mit Kenntnis des Vermieters.
- Arglist verlängert Verjährung bei Kauf auf 30 Jahre; bei Werkvertrag auf 10 Jahre.
- Hemmung durch Verhandlungen (§ 203 BGB) setzt echten Austausch voraus; bloße Ablehnung genügt nicht.
- Verjährung des Bereicherungsanspruchs nach § 852 BGB (10 Jahre) als 'Restschaden' neben § 823 BGB.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Verjährungs-Kalender (Fristbeginn, Fristende, Hemmungszeiträume)
- Sonderfrist-Matrix (Kauf, Miete, Werk, Delikt)
- Arglist-Verlängerungs-Prüfung
- Handlungsempfehlung (Klageerhebung, Anerkenntniseinholung)

## Qualitätsregeln

- Anspruchsgrundlage und Sonderverjährung immer als erste Weiche setzen.
- Arglist immer aktiv mitprüfen; kann Verjährung entscheidend verlängern.
- Hemmungsberechnung dokumentieren.

## Anschluss-Skills

- kaufrecht-beweislast-verjaehrung-digitale-elemente
- werkvertrag-maengelrechte
- bt-fristen-erklaerungen-zugang
- workflow-fristen-ruecktritt-kuendigung


## Quellen

- https://www.gesetze-im-internet.de/bgb/__438.html
- https://www.gesetze-im-internet.de/bgb/__548.html
- https://www.gesetze-im-internet.de/bgb/__634a.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `werk-dienst-abgrenzung-erfolg`

**Fokus:** Werk-Dienst-Abgrenzung: Erfolgsschuldnerschaft § 631 BGB vs. Tätigkeitsschuldnerschaft § 611 BGB.

# Werk-Dienst-Abgrenzung: Erfolg vs. Tätigkeit

## Fachkern: Werk-Dienst-Abgrenzung: Erfolg vs. Tätigkeit
- **Spezialgegenstand:** Werk-Dienst-Abgrenzung: Erfolg vs. Tätigkeit; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Abgrenzung zwischen Werkvertrag (Erfolgshaftung) und Dienstvertrag (Tätigkeitspflicht) vornehmen: Rechtsfolgen für Mängelhaftung, Kündigung, Vergütung und Abnahme.

## Normanker

- § 631 BGB: Werkvertrag (Herstellung oder Veränderung einer Sache oder ein anderer durch Arbeit herbeigeführter Erfolg)
- § 611 BGB: Dienstvertrag (Dienstleistung als solche geschuldet, nicht ein Erfolg)
- § 613a BGB: Betriebsübergang (nicht Thema, aber Abgrenzung zu Arbeitsverhältnis)
- § 650 BGB: Werklieferungsvertrag
- § 627 BGB: Kündigung von Dienstverträgen mit besonderem Vertrauen

## Intake

- Was schuldet der Auftragnehmer: eine Tätigkeit (Dienst) oder ein bestimmtes Ergebnis (Werk)?
- Wer trägt das Ausführungsrisiko?
- Ist Abnahme des Ergebnisses vereinbart oder erwartet?
- Welche Partei hat ein Interesse an dieser Abgrenzung (Mängelrechte, Kündigung, Vergütung)?
- Besteht Scheinselbstständigkeit (Abgrenzung zum Arbeitsvertrag)?

## Prüfraster

1. Sachverhalt-Analyse: Was ist der vertraglich geschuldete Kern — Tätigkeit oder Ergebnis?
2. Werkvertrag: Auftragnehmer schuldet einen bestimmten Erfolg (§ 631 BGB); Vergütung fällig erst mit Abnahme
3. Dienstvertrag: Auftragnehmer schuldet Tätigkeit (§ 611 BGB); Vergütung für geleistete Zeit
4. Bedeutung für Mängelhaftung: Werkvertrag hat §§ 633 ff. BGB; Dienstvertrag grundsätzlich keine Gewährleistung
5. Abnahme: beim Werkvertrag konstitutiv (§ 640 BGB); beim Dienstvertrag nicht vorgesehen
6. Kündigung: Dienstvertrag nach § 621 BGB (ordentlich) oder § 627 BGB (aus wichtigem Grund); Werkvertrag nach § 648 BGB
7. Behandlungsvertrag: Arzt schuldet keine Heilung (Dienstvertrag), aber Einhaltung des medizinischen Standards
8. IT-Projekte: Pflichtenheft und abnahmefähige Ergebnisse sprechen für Werkvertrag

## Fallstricke

- Behandlungsvertrag (§ 630a BGB) ist Dienstvertrag; kein Erfolg geschuldet, nur lege artis-Behandlung.
- IT-Dienstleistungsverträge: oft unklar ob Dienst oder Werk; Pflichtenheft-Analyse entscheidend.
- Bei Scheinselbstständigkeit droht Arbeitnehmerqualifikation mit Sozialversicherungspflicht.
- Vergütungsfolgen: Werkvertrag zahlt nach Abnahme; Dienstvertrag zahlt laufend oder nach Zeitperioden.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Einordnungsmatrix (Werk vs. Dienst vs. Arbeitsvertrag)
- Rechtsfolgen-Vergleich (Vergütung, Mängel, Kündigung, Abnahme)
- Risikobewertung bei Fehlqualifikation
- Gestaltungsempfehlung

## Qualitätsregeln

- Erfolgsdefinition im Vertrag immer wörtlich auswerten; keine Vermutungen.
- Behandlungsvertrag immer als Dienstvertrag einordnen.
- Bei IT-Projekten Meilensteine und Abnahmeregeln analysieren.

## Anschluss-Skills

- werkvertrag-grundschema-paragraph-631
- dienstvertrag-und-behandlungsvertrag
- vertragstypen-mischvertrag-router
- arbeitsnaher-dienstvertrag-bgb


## Quellen

- https://www.gesetze-im-internet.de/bgb/__631.html
- https://www.gesetze-im-internet.de/bgb/__611.html
- https://www.gesetze-im-internet.de/bgb/__630a.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
