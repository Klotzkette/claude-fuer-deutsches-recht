---
name: vertragstypen-mischvertrag-werkvertrag
description: "Vertragstypen Mischvertrag Werkvertrag: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Vertragstypen Mischvertrag Werkvertrag

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Vertragstypen Mischvertrag Werkvertrag** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vertragstypen-mischvertrag-router` | Vertragstypen-Router: Mischvertrag, gemischter Vertrag, Abgrenzung und Normauswahl im BGB BT. |
| `werkvertrag-abnahme-und-faelligkeit` | Werkvertrag: Abnahme § 640 BGB, Fälligkeit der Vergütung, fingierte Abnahme und Abnahmeverweigerung. |
| `werkvertrag-grundschema-paragraph-631` | Werkvertrag § 631 BGB: Grundschema, Vergütung, Abnahme, Mängelrechte und Kündigung. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Vertragstypen Mischvertrag Werkvertrag**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vertragstypen-mischvertrag-router`

**Fokus:** Vertragstypen-Router: Mischvertrag, gemischter Vertrag, Abgrenzung und Normauswahl im BGB BT.

# Vertragstypen und Mischvertrag Router

## Fachkern: Vertragstypen und Mischvertrag Router
- **Spezialgegenstand:** Vertragstypen und Mischvertrag Router; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Vertragstypen im BGB BT einordnen und bei Misch- oder atypischen Verträgen die anwendbaren Normen bestimmen: Absorptionstheorie, Kombinationstheorie und Typenzwang-Fragen.

## Normanker

- §§ 433 ff. BGB: Kaufvertrag
- §§ 535 ff. BGB: Mietvertrag
- §§ 611 ff. BGB: Dienstvertrag
- §§ 631 ff. BGB: Werkvertrag
- § 651a ff. BGB: Reisevertrag
- §§ 662 ff. BGB: Auftrag
- § 675 BGB: Geschäftsbesorgung
- Amtliches BGB: https://www.gesetze-im-internet.de/bgb/

## Intake

- Welche Leistungen schuldet die Partei (Übereignung, Gebrauchsüberlassung, Erfolg, Tätigkeit, Vermittlung)?
- Liegt ein reiner Vertragstyp vor oder mehrere Elemente in einem Vertrag?
- Welches Vertragsrecht soll für Mängelrechte, Kündigung oder Haftung gelten?
- Gibt es einen Schwerpunkt der vertraglichen Pflichten?
- Sind spezielle Formvorschriften zu beachten?

## Prüfraster

1. Vertragsinhalt analysieren: Was sind die Hauptleistungspflichten beider Seiten?
2. Typenkatalogs-Prüfung: Welche gesetzlichen Vertragstypen passen (Kauf, Miete, Werk, Dienst, Auftrag)?
3. Rein typischer Vertrag oder Mischvertrag?
4. Bei Mischverträgen: Absorptionstheorie (überwiegt ein Typ?) oder Kombinationstheorie (je nach Pflicht)?
5. Werk-Dienst-Abgrenzung: Erfolgsschuldnerschaft (Werk) vs. Tätigkeitsschuldnerschaft (Dienst)
6. Kauf-Werk-Abgrenzung: bereits fertige Sache (Kauf) vs. erst herzustellende Sache (Werklieferung § 650 BGB)
7. Miet-Pacht-Abgrenzung: Fruchtziehung (Pacht) vs. bloße Gebrauchsüberlassung (Miete)
8. Atypische Verträge (z.B. Franchising, Factoring, Leasing): Analogie oder allgemeines Schuldrecht

## Fallstricke

- Falsche Vertragstyp-Einordnung führt zu falschen Mängelrechten, Kündigungsfristen und Haftungsregeln.
- Bei Werklieferungsvertrag (§ 650 BGB) gilt Kaufrecht, nicht Werkrecht.
- Franchising, Factoring, Leasing haben kein kodifiziertes Sonderrecht; analogische Anwendung erforderlich.
- Schwerpunktbestimmung bei Mischverträgen ist Wertungsfrage; Argumentation klar machen.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Vertragstyp-Einordnung mit Begründung
- Anwendbare Normen-Matrix (je nach Pflicht oder Schwerpunkt)
- Mischvertrag-Behandlungsempfehlung
- Risikoampel für fehlerhafte Einordnung

## Qualitätsregeln

- Sachverhalt-Schwerpunkt für Absorptionstheorie klar herausarbeiten.
- § 650 BGB (Werklieferung) immer als Alternative zu § 631 BGB prüfen.
- Atypische Verträge mit allgemeinem Schuldrecht lösen, wenn kein kodifizierter Typ passt.

## Anschluss-Skills

- werk-dienst-abgrenzung-erfolg
- kaufvertrag-grundschema-paragraph-433
- werkvertrag-grundschema-paragraph-631
- dienstvertrag-und-behandlungsvertrag

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `werkvertrag-abnahme-und-faelligkeit`

**Fokus:** Werkvertrag: Abnahme § 640 BGB, Fälligkeit der Vergütung, fingierte Abnahme und Abnahmeverweigerung.

# Werkvertrag: Abnahme und Fälligkeit §§ 640 und 641 BGB

## Fachkern: Werkvertrag: Abnahme und Fälligkeit §§ 640 und 641 BGB
- **Spezialgegenstand:** Werkvertrag: Abnahme und Fälligkeit §§ 640 und 641 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Abnahme beim Werkvertrag nach §§ 640 und 641 BGB prüfen: Abnahmepflicht des Bestellers, Rechtsfolgen der Abnahme (Fälligkeit, Gefahrübergang, Verjährungsbeginn), fingierte Abnahme und Abnahmeverweigerung.

## Normanker

- § 640 BGB: Abnahmepflicht des Bestellers und fingierte Abnahme
- § 641 BGB: Fälligkeit der Vergütung (nach Abnahme)
- § 641a BGB: Fertigstellungsbescheinigung
- § 644 BGB: Gefahrtragung beim Werkvertrag
- § 634a BGB: Verjährungsbeginn (Abnahme)
- § 648a BGB: Kündigung aus wichtigem Grund

## Intake

- Wurde das Werk abgenommen oder ist die Abnahme verweigert worden?
- Liegt ein Grund zur Abnahmeverweigerung (wesentlicher Mangel) vor?
- Gibt es eine fingierte Abnahme nach § 640 Abs. 2 BGB?
- Wann beginnt die Verjährung (Abnahmezeitpunkt)?
- Ist die Vergütung fällig (§ 641 BGB)?

## Prüfraster

1. Abnahme-Tatbestand: körperliche Übernahme und Billigung des Werks als im Wesentlichen vertragsgemäß
2. Abnahmepflicht des Bestellers nach § 640 Abs. 1 BGB: Pflicht zur Abnahme nach Fertigstellung
3. Abnahmeverweigerungsrecht: berechtigt nur bei wesentlichen Mängeln; unwesentliche berechtigen nicht zur Verweigerung
4. Fingierte Abnahme nach § 640 Abs. 2 BGB: Fristsetzung durch Unternehmer; Ablauf ohne Reaktion oder ohne Mängelangabe
5. Rechtsfolgen der Abnahme: Fälligkeit der Vergütung (§ 641 BGB); Gefahrübergang (§ 644 BGB); Verjährungsbeginn (§ 634a BGB)
6. Mängelrüge bei Abnahme: Kenntnis eines Mangels bei Abnahme schließt Mängelrechte aus (§ 640 Abs. 3 BGB)
7. Schlussrechnung und Prüfungspflichten bei VOB/B-Verträgen (Besonderheiten)

## Fallstricke

- Unwesentliche Mängel berechtigen nicht zur Abnahmeverweigerung; sonst gerät Besteller in Annahmeverzug.
- Fingierte Abnahme (§ 640 Abs. 2 BGB): Frist muss nach Fertigstellung gesetzt werden; pauschale Fristsetzung vorab genügt nicht.
- Vorbehaltlose Abnahme in Kenntnis eines Mangels schließt Mängelansprüche aus (§ 640 Abs. 3 BGB).
- Bei VOB/B-Verträgen gelten ergänzende Regeln zur Abnahme; diese gehen BGB vor.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Abnahme-Status-Analyse (erteilt, verweigert, fingiert)
- Rechtsfolgen-Matrix (Fälligkeit, Gefahrübergang, Verjährungsbeginn)
- Handlungsempfehlung (Nachfristsetzung, Mängelrüge, Klage)
- Risikoampel

## Qualitätsregeln

- Wesentlichkeit eines Mangels als Schwelle zur Abnahmeverweigerung immer prüfen.
- § 640 Abs. 3 BGB-Kenntnisausschluss aktiv in Prüfung einbauen.
- Fingierte Abnahme nur nach korrekter Fristsetzung annehmen.

## Anschluss-Skills

- werkvertrag-grundschema-paragraph-631
- werkvertrag-maengelrechte
- verjaehrung-bgb-bt-spezial
- workflow-fristen-ruecktritt-kuendigung


## Quellen

- https://www.gesetze-im-internet.de/bgb/__640.html
- https://www.gesetze-im-internet.de/bgb/__641.html
- https://www.gesetze-im-internet.de/bgb/__634a.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `werkvertrag-grundschema-paragraph-631`

**Fokus:** Werkvertrag § 631 BGB: Grundschema, Vergütung, Abnahme, Mängelrechte und Kündigung.

# Werkvertrag Grundschema § 631 BGB

## Fachkern: Werkvertrag Grundschema § 631 BGB
- **Spezialgegenstand:** Werkvertrag Grundschema § 631 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Werkvertrag nach § 631 BGB vollständig prüfen: Vertragstypische Pflichten, Vergütungsfälligkeit, Abnahme, Mängelrecht-Katalog, VOB/B-Besonderheiten und Kündigung.

## Normanker

- § 631 BGB: Vertragstypische Pflichten beim Werkvertrag
- § 633 BGB: Sach- und Rechtsmangel beim Werkvertrag
- § 634 BGB: Rechte des Bestellers bei Mängeln
- § 635 BGB: Nacherfüllung beim Werkvertrag
- § 636 BGB: Besondere Bestimmungen für Rücktritt und Schadensersatz
- § 640 BGB: Abnahme
- § 641 BGB: Fälligkeit der Vergütung
- § 648 BGB: Kündigung durch den Besteller
- § 648a BGB: Kündigung aus wichtigem Grund

## Intake

- Was ist der Vertragsgegenstand (Bauleistung, Reparatur, IT-Leistung, Gutachten)?
- Wurde ein Werk-Erfolg definiert und ist er eingetreten?
- Welche Mängel werden gerügt?
- Ist das Werk abgenommen?
- Gilt VOB/B oder AGB des Unternehmers?

## Prüfraster

1. Vertragsschluss: Parteien, Werkgegenstand, Vergütung, Fälligkeit
2. Pflichten des Unternehmers: mangelfreie Herstellung des Werks; Eigenverantwortung für Ausführung
3. Pflichten des Bestellers: Abnahme (§ 640 BGB), Vergütungszahlung (§ 641 BGB), Mitwirkung
4. Sachmangel nach § 633 BGB: subjektive, objektive Anforderungen, Montagemangel
5. Rechte des Bestellers nach § 634 BGB: Nacherfüllung, Selbstvornahme, Rücktritt, Minderung, Schadensersatz
6. Nacherfüllung nach § 635 BGB: Vorrang; Besteller muss Frist setzen
7. Abnahme: Voraussetzungen, Rechtsfolgen, Abnahmeverweigerungsrecht
8. Verjährung: § 634a BGB (2 Jahre beweglich; 5 Jahre Bauleistungen)
9. Kündigung: § 648 BGB (jederzeitiges Recht des Bestellers; Vergütungsfolge) oder § 648a BGB (wichtiger Grund)

## Fallstricke

- Vergütung wird erst fällig nach Abnahme (§ 641 BGB); ohne Abnahme kein Anspruch auf volle Vergütung.
- Nacherfüllungsrecht des Unternehmers vor Rücktritt und Schadensersatz beachten.
- Kündigung nach § 648 BGB jederzeit möglich, aber Besteller muss vereinbarte Vergütung abzüglich ersparter Aufwendungen zahlen.
- VOB/B-Verträge haben eigene Abnahme- und Mängelregelungen die BGB ergänzen oder ersetzen.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Werkvertragsstruktur-Übersicht (Parteien, Gegenstand, Vergütung)
- Mangelprüfungs-Schema (Istbeschaffenheit vs. Sollbeschaffenheit)
- Besteller-Rechte-Matrix nach § 634 BGB
- Kündigung und Vergütungsfolgen

## Qualitätsregeln

- Abnahme als Schlüsselereignis für Fälligkeit und Verjährung immer prüfen.
- Nacherfüllungsrecht des Unternehmers vor Sekundäransprüchen einräumen.
- VOB/B-Verträge gesondert auf Abweichungen vom BGB prüfen.

## Anschluss-Skills

- werkvertrag-abnahme-und-faelligkeit
- werkvertrag-maengelrechte
- werk-dienst-abgrenzung-erfolg
- bauvertrag-und-verbraucherbauvertrag

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
