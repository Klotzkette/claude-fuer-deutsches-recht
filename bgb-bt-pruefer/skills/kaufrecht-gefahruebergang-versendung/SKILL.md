---
name: kaufrecht-gefahruebergang-versendung
description: "Kaufrecht Gefahruebergang Versendung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Kaufrecht Gefahruebergang Versendung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Kaufrecht Gefahruebergang Versendung** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kaufrecht-gefahruebergang-und-versendung` | Prüft Gefahrübergang § 446 BGB, Versendungskauf § 447 BGB und Ausnahmen beim Verbrauchsgüterkauf. |
| `kaufrecht-nacherfuellung-ruecktritt-minderung` | Prüft Nacherfüllung § 439 BGB, Rücktritt § 437 Nr. 2 BGB, Minderung und Schadensersatz bei Sachmangel. |
| `kaufrecht-rechtsmangel-paragraph-435` | Prüft Rechtsmangel § 435 BGB: Rechte Dritter, beschränkt dingliche Rechte, öffentlich-rechtliche Lasten und Rechtsfolgen. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Kaufrecht Gefahruebergang Versendung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kaufrecht-gefahruebergang-und-versendung`

**Fokus:** Prüft Gefahrübergang § 446 BGB, Versendungskauf § 447 BGB und Ausnahmen beim Verbrauchsgüterkauf.

# Kaufrecht: Gefahrübergang und Versendung

## Fachkern: Kaufrecht: Gefahrübergang und Versendung
- **Spezialgegenstand:** Kaufrecht: Gefahrübergang und Versendung; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Gefahrübergang nach §§ 446 und 447 BGB prüfen: Zeitpunkt, Übergabe, Versendung, Verbrauchsgüterkaufausnahme und Rechtsfolgen bei Untergang der Sache.

## Normanker

- § 446 BGB: Gefahrübergang bei Übergabe der Sache
- § 447 BGB: Versendungskauf, Gefahrübergang bei Übergabe an Transportperson
- § 475 Abs. 2 BGB: Ausnahme beim Verbrauchsgüterkauf (Gefahrübergang erst bei Übergabe)
- § 300 Abs. 2 BGB: Gefahrübergang bei Gläubigerverzug
- §§ 243 und 244 BGB: Gattungsschuld und Konkretisierung

## Intake

- Handelt es sich um einen Versendungskauf nach § 447 BGB?
- Hat der Käufer die Versendung veranlasst oder hat der Verkäufer auf Wunsch des Käufers versandt?
- Liegt ein Verbrauchsgüterkauf vor; gilt § 475 Abs. 2 BGB?
- Ist die Sache auf dem Transportweg beschädigt oder untergegangen?
- War die Sache bereits konkretisiert (bei Gattungsschuld nach § 243 BGB)?

## Prüfraster

1. Gefahrübergang bei Übergabe nach § 446 BGB: Zeitpunkt und Ort der Übergabe
2. Versendungskauf nach § 447 BGB: Käufer hat Versendung veranlasst oder Ort ist kein Erfüllungsort
3. Gefahrübergang beim Versendungskauf: Übergabe an Transportperson, nicht beim Empfänger
4. Verbrauchsgüterkaufausnahme nach § 475 Abs. 2 BGB: Gefahrübergang erst bei Übergabe an Verbraucher
5. Gläubigerverzug: § 300 Abs. 2 BGB kann Gefahrübergang vorziehen
6. Gattungsschuld: Konkretisierung nach § 243 BGB Voraussetzung für Gefahrübergang
7. Folgen des Gefahrübergangs: Käufer trägt Gefahr des zufälligen Untergangs (Preisgefahr und Leistungsgefahr)
8. Beweislast: wer beweist den Zustand bei Gefahrübergang?

## Fallstricke

- Bei Verbrauchsgüterkauf geht Gefahr nicht auf den Verbraucher über, solange Ware nicht übergeben wurde.
- § 447 BGB gilt im Verbrauchsgüterkauf nicht zu Lasten des Käufers.
- Gefahrübergang und Eigentumsverschaffung können zeitlich auseinanderfallen.
- Gläubigerverzug des Käufers (Annahmeverzug) verschiebt Gefahrübergang nach § 300 Abs. 2 BGB.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Gefahrübergangs-Zeitlinie
- Versendungskauf-Analyse
- Verbraucherschutzausnahme-Prüfung
- Beweislastverteilung

## Qualitätsregeln

- § 447 BGB und § 475 Abs. 2 BGB immer im selben Atemzug prüfen.
- Gattungsschuld immer auf Konkretisierung prüfen.
- Gefahrübergang und Eigentumsverschaffung nicht verwechseln.

## Anschluss-Skills

- kaufvertrag-grundschema-paragraph-433
- kaufrecht-sachmangel-paragraph-434
- kaufrecht-nacherfuellung-ruecktritt-minderung
- bt-fristen-erklaerungen-zugang


## Quellen

- https://www.gesetze-im-internet.de/bgb/__446.html
- https://www.gesetze-im-internet.de/bgb/__447.html
- https://www.gesetze-im-internet.de/bgb/__474.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `kaufrecht-nacherfuellung-ruecktritt-minderung`

**Fokus:** Prüft Nacherfüllung § 439 BGB, Rücktritt § 437 Nr. 2 BGB, Minderung und Schadensersatz bei Sachmangel.

# Kaufrecht: Nacherfüllung, Rücktritt und Minderung

## Fachkern: Kaufrecht: Nacherfüllung, Rücktritt und Minderung
- **Spezialgegenstand:** Kaufrecht: Nacherfüllung, Rücktritt und Minderung; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Käuferrechte bei Sachmangel nach § 437 BGB vollständig prüfen: Nacherfüllung, Fristsetzung, Rücktritt, Minderung und Schadensersatz.

## Normanker

- § 437 BGB: Rechte des Käufers bei Sachmangel
- § 439 BGB: Nacherfüllung (Nachbesserung oder Nachlieferung)
- §§ 440 und 441 BGB: Rücktritt und Minderung
- § 323 BGB: Voraussetzungen des Rücktritts
- § 441 BGB: Minderung
- § 442 BGB: Kenntnis des Käufers vom Mangel
- § 443 BGB: Garantie
- § 475 BGB: Verbrauchsgüterkauf

## Intake

- Liegt ein Sachmangel nach § 434 BGB vor?
- Wurde eine angemessene Nachfrist zur Nacherfüllung gesetzt?
- Hat der Verkäufer Nacherfüllung verweigert oder ist sie fehlgeschlagen?
- Wählt der Käufer Rücktritt oder Minderung?
- Besteht zusätzlich ein Schadensersatzanspruch?

## Prüfraster

1. Sachmangel nach § 434 BGB: subjektive, objektive und Montageanforderungen
2. Nacherfüllungsanspruch nach § 439 BGB: Wahl zwischen Nachbesserung und Nachlieferung
3. Fristsetzung: angemessene Frist mit Ablehnungsandrohung nach § 323 BGB
4. Unmöglichkeit oder Verweigerung der Nacherfüllung: § 440 BGB
5. Rücktritt nach §§ 437 Nr. 2 und 323 BGB: Voraussetzungen, Ausnahmen bei erheblichem Mangel
6. Minderung nach § 441 BGB: Verhältnisrechnung, Rückforderung bei bereits gezahltem Kaufpreis
7. Schadensersatz nach §§ 437 Nr. 3 und 280 BGB: neben oder statt der Leistung
8. Verjährung: § 438 BGB; Beweislastumkehr § 477 BGB

## Fallstricke

- Rücktritt setzt erheblichen Mangel voraus (§ 323 Abs. 5 Satz 2 BGB); unerheblicher Mangel berechtigt nur zur Minderung.
- Bei Verbrauchsgüterkauf zwei Nachbesserungsversuche sind nicht gesetzlich vorgeschrieben; Einzelfallbeurteilung.
- Minderungsberechnung: Verhältnis mängelfreier Kaufpreis zum tatsächlichen Kaufpreis.
- § 442 BGB schließt Mängelansprüche aus, wenn Käufer Mangel bei Vertragsschluss kannte.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Mängelrechte-Stufenleiter (Nacherfüllung, Rücktritt/Minderung, Schadensersatz)
- Fristsetzungs-Dokumentation
- Rücktritts-/Minderungs-Berechnung
- Risikoampel und Handlungsempfehlung

## Qualitätsregeln

- Nacherfüllung immer vor Rücktritt und Minderung prüfen.
- Erheblichkeit des Mangels ausdrücklich beurteilen.
- Minderungsberechnung immer zahlenmäßig darstellen.

## Anschluss-Skills

- kaufrecht-sachmangel-paragraph-434
- kaufrecht-gefahruebergang-und-versendung
- kaufrecht-schadensersatz-aufwendungsersatz
- bt-fristen-erklaerungen-zugang

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `kaufrecht-rechtsmangel-paragraph-435`

**Fokus:** Prüft Rechtsmangel § 435 BGB: Rechte Dritter, beschränkt dingliche Rechte, öffentlich-rechtliche Lasten und Rechtsfolgen.

# Kaufrecht: Rechtsmangel § 435 BGB

## Fachkern: Kaufrecht: Rechtsmangel § 435 BGB
- **Spezialgegenstand:** Kaufrecht: Rechtsmangel § 435 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Rechtsmängel nach § 435 BGB prüfen: Rechte Dritter, Belastungen und öffentlich-rechtliche Lasten, die den Käufer beeinträchtigen; Rechtsfolgen und Abgrenzung zum Sachmangel.

## Normanker

- § 435 BGB: Rechtsmangel (Rechte Dritter und öffentlich-rechtliche Lasten)
- § 437 BGB: Käuferrechte (gelten auch bei Rechtsmangel)
- §§ 986 ff. BGB: Einreden des Besitzers (Besitzrecht Dritter)
- GBO: Grundbucheintragungen als Indiz für Rechtsmängel (bei Grundstückskäufen)
- § 311b BGB: Beurkundungspflicht beim Grundstückskauf

## Intake

- Haben Dritte Rechte an der verkauften Sache, die den Käufer beeinträchtigen (Pfandrecht, Nießbrauch, Miete)?
- Bestehen öffentlich-rechtliche Lasten (Erschließungsbeiträge, Denkmalschutz, Baulasten)?
- Wurde der Käufer über die Rechte Dritter informiert?
- Welche Käuferrechte sollen geltend gemacht werden?

## Prüfraster

1. Rechtsmangel-Einordnung nach § 435 BGB: Recht eines Dritten oder sonstige Last
2. Sachmangel vs. Rechtsmangel: klare Abgrenzung (Sachmangel betrifft Beschaffenheit, Rechtsmangel betrifft Rechtsstellung)
3. Beeinträchtigung des Käufers: muss der Käufer das Recht des Dritten dulden?
4. Öffentlich-rechtliche Lasten: Benutzungseinschränkungen, Erschließungsbeiträge
5. Käuferrechte nach § 437 BGB: Nacherfüllung (Beseitigung des Rechtsmangels), Rücktritt, Minderung, Schadensersatz
6. Fristsetzung zur Beseitigung des Rechtsmangels
7. Kenntnis des Käufers nach § 442 BGB: bekannte Rechtsmängel können Ansprüche ausschließen
8. Verjährung nach § 438 BGB

## Fallstricke

- Öffentlich-rechtliche Lasten können Rechtsmangel sein, auch wenn keine privaten Rechte Dritter bestehen.
- Mieter hat aus Kaufvertrag kein Klagerecht gegen Käufer (kein Vertragsverhältnis), aber es kann Vollstreckungsschutz für Mieter bestehen.
- Kauf bricht nicht Miete nach § 566 BGB: Mieter bleibt berechtigt trotz Eigentümerwechsel.
- Aufgedeckte Rechtsmängel müssen zeitnah gerügt werden.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Rechtsmangel-Analyse (Art und Umfang des Rechts Dritter)
- Käuferrechte-Stufenleiter
- Öffentlich-rechtliche Lasten-Checkliste
- Risikoampel

## Qualitätsregeln

- Sachmangel und Rechtsmangel immer klar trennen.
- Öffentlich-rechtliche Lasten immer einschließen.
- § 566 BGB bei Immobilienkaufrecht stets beachten.

## Anschluss-Skills

- kaufrecht-sachmangel-paragraph-434
- kaufrecht-nacherfuellung-ruecktritt-minderung
- mietvertrag-grundschema-paragraph-535
- workflow-anspruchslandkarte


## Quellen

- https://www.gesetze-im-internet.de/bgb/__435.html
- https://www.gesetze-im-internet.de/bgb/__437.html
- https://www.gesetze-im-internet.de/bgb/__433.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
