---
name: buergschaft-verbraucherbuerge-grundschema
description: "Buergschaft Verbraucherbuerge Grundschema: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Buergschaft Verbraucherbuerge Grundschema

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Buergschaft Verbraucherbuerge Grundschema** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `buergschaft-form-und-verbraucherbuerge` | Prüft Schriftform der Bürgschaft § 766 BGB, Verbraucherbürgschaft, sittenwidrige Bürgschaft und AGB-Bürgschaftsklauseln. |
| `buergschaft-grundschema-paragraph-765` | Prüft Bürgschaft §§ 765 ff. BGB: Tatbestand, Akzessorietät, Inanspruchnahme und Regressanspruch des Bürgen. |
| `darlehen-und-finanzierung` | Prüft Darlehensvertrag §§ 488 ff. BGB, Verbraucherdarlehen §§ 491 ff. BGB, Zinsen, Kündigung und Widerruf. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Buergschaft Verbraucherbuerge Grundschema**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `buergschaft-form-und-verbraucherbuerge`

**Fokus:** Prüft Schriftform der Bürgschaft § 766 BGB, Verbraucherbürgschaft, sittenwidrige Bürgschaft und AGB-Bürgschaftsklauseln.

# Bürgschaft: Form und Verbraucherbürge

## Fachkern: Bürgschaft: Form und Verbraucherbürge
- **Spezialgegenstand:** Bürgschaft: Form und Verbraucherbürge; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Formvorschrift des § 766 BGB, Verbraucherschutz bei Bürgschaften und Sittenwidrigkeit nach § 138 BGB prüfen: insbesondere Bürgschaften von Privatpersonen für Unternehmensschulden.

## Normanker

- § 766 BGB: Schriftform der Bürgschaftserklärung
- § 350 HGB: Formfreiheit für Kaufleute (einseitig)
- § 138 BGB: Sittenwidrigkeit übermäßiger Bürgschaften
- §§ 305–310 BGB: AGB-Kontrolle für Bürgschaftsklauseln in Allgemeinen Kreditbedingungen
- Art. 247 EGBGB: vorvertragliche Informationspflichten bei Verbraucherverträgen
- BGH-Rechtsprechung zur Sittenwidrigkeit bei finanziell überfordertem Bürgen: nur nach Live-Prüfung zitieren

## Intake

- Ist die Bürgschaftserklärung schriftlich erteilt worden; fehlt Unterschrift oder Text?
- Handelt es sich um einen Verbraucher oder Kaufmann als Bürgen?
- Steht das Bürgschaftsrisiko in einem krassen Missverhältnis zum Einkommen des Bürgen?
- Besteht eine enge persönliche Verbindung zwischen Bürgen und Hauptschuldner?
- Liegt eine AGB-Bürgschaftsklausel vor?

## Prüfraster

1. Schriftform nach § 766 BGB: eigenhändige Unterzeichnung, vollständiger Urkundentext
2. Ausnahme für Kaufleute: § 350 HGB prüfen (einseitig, wenn Bürgschaft für Bürgen Handelsgeschäft)
3. Verbraucherbürgschaft: Informationspflichten nach Art. 247 EGBGB?
4. Sittenwidrigkeit nach § 138 BGB: krasses Missverhältnis zwischen Bürgschaftsumfang und wirtschaftlicher Leistungsfähigkeit
5. Emotionale Nähe als Indiz für Sittenwidrigkeit (Ehegatten, Kinder als Bürgen für Unternehmensschulden)
6. AGB-Bürgschaftsklauseln: Inhaltskontrolle nach § 307 BGB
7. Folgen der Sittenwidrigkeit: Gesamtnichtigkeit nach § 138 Abs. 1 BGB
8. Verjährung des Bürgschaftsanspruchs: § 195 BGB

## Fallstricke

- Mündliche oder telegrafische Bürgschaft ist nach § 766 BGB nichtig (Ausnahme § 350 HGB).
- Sittenwidrigkeitsprüfung ist einzelfallabhängig; allgemeine Faustformeln unzuverlässig.
- AGB-Bürgschaftsklauseln in Bankverträgen werden oft als überraschend (§ 305c BGB) oder unangemessen (§ 307 BGB) eingestuft.
- Bürgschaftserweiterungen für zukünftige Verbindlichkeiten müssen ausdrücklich vereinbart sein.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Formprüfung mit Ergebnis (wirksam/nichtig)
- Sittenwidrigkeitsprüfung mit Einkommensvergleich
- AGB-Risikoliste
- Handlungsempfehlung und Risikoampel

## Qualitätsregeln

- Sittenwidrigkeitsprüfung immer auf konkrete Zahlen stützen.
- AGB-Bürgschaftsklauseln im Zweifelsfall gesondert prüfen.
- BGH-Rechtsprechung zu Angehörigenbürgschaften nur nach Live-Prüfung zitieren.

## Anschluss-Skills

- buergschaft-grundschema-paragraph-765
- buergschaft-einreden-und-akzessorietaet
- schnittstelle-bgb-at-methodenlehre-agb
- workflow-red-team-gegenseite


## Quellen

- https://www.gesetze-im-internet.de/bgb/__766.html
- https://www.gesetze-im-internet.de/bgb/__765.html
- https://www.gesetze-im-internet.de/bgb/__307.html
## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `buergschaft-grundschema-paragraph-765`

**Fokus:** Prüft Bürgschaft §§ 765 ff. BGB: Tatbestand, Akzessorietät, Inanspruchnahme und Regressanspruch des Bürgen.

# Bürgschaft Grundschema § 765 BGB

## Fachkern: Bürgschaft Grundschema § 765 BGB
- **Spezialgegenstand:** Bürgschaft Grundschema § 765 BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Bürgschaft als personale Sicherheit nach § 765 BGB vollständig prüfen: Tatbestand, Akzessorietät, Inanspruchnahme des Bürgen und Regressanspruch.

## Normanker

- § 765 BGB: Bürgschaftsvertrag (Definition)
- § 766 BGB: Schriftform
- § 767 BGB: Akzessorietät
- §§ 768–770 BGB: Einreden des Bürgen
- § 771 BGB: Einrede der Vorausklage
- § 774 BGB: Legalzession und Übergang der Forderung auf den Bürgen
- § 776 BGB: Aufgabe von Sicherheiten
- § 778 BGB: Kreditauftrag

## Intake

- Wer sind Gläubiger, Hauptschuldner und Bürge?
- Liegt eine wirksame Hauptforderung vor?
- Ist die Bürgschaftserklärung formwirksam nach § 766 BGB?
- Wurde auf die Einrede der Vorausklage verzichtet?
- Welche Einreden stehen dem Bürgen zu?
- Ist die Hauptschuld fällig und durchsetzbar?

## Prüfraster

1. Bürgschaftsvertrag nach § 765 BGB: Angebot und Annahme, Form nach § 766 BGB
2. Wirksame Hauptforderung: Entstehung, Fälligkeit, keine Einreden
3. Akzessorietät nach § 767 BGB: Bürgschaftsschuld folgt Hauptschuld
4. Einreden des Bürgen: §§ 768–770 BGB (eigene und übernommene Einreden)
5. Einrede der Vorausklage nach § 771 BGB; Verzicht bei selbstschuldnerischer Bürgschaft
6. Inanspruchnahme: Fälligkeit, Mahnung, Klage gegen Bürgen
7. Legalzession nach § 774 BGB: Übergang der Hauptforderung auf den Bürgen nach Zahlung
8. Regressansprüche: § 774 BGB sowie §§ 670 und 683 BGB (analoge Auftragsregeln)

## Fallstricke

- Bürgschaft ohne schriftliche Erklärung des Bürgen ist nichtig (§ 766 BGB).
- Selbstschuldnerische Bürgschaft schließt § 771 BGB aus; Bürge kann sofort in Anspruch genommen werden.
- Legalzession nach § 774 BGB setzt vollständige Zahlung der Hauptschuld durch den Bürgen voraus.
- Bürgschaft erlischt mit Erlöschen der Hauptschuld (Akzessorietät).
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Anspruchsmatrix (Gläubiger gegen Bürge, Bürge gegen Hauptschuldner)
- Einreden-Checkliste
- Legalzession und Regressprüfung
- Risikoampel und Handlungsempfehlung

## Qualitätsregeln

- Bürgschaftsprüfung immer mit Hauptschuld-Prüfung verknüpfen.
- Selbstschuldnerische Bürgschaft klar von subsidiärer Bürgschaft abgrenzen.
- Regresswege vollständig aufzeigen.

## Anschluss-Skills

- buergschaft-einreden-und-akzessorietaet
- buergschaft-form-und-verbraucherbuerge
- gesamtschuld-und-regress-bgb-bt
- workflow-anspruchslandkarte

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `darlehen-und-finanzierung`

**Fokus:** Prüft Darlehensvertrag §§ 488 ff. BGB, Verbraucherdarlehen §§ 491 ff. BGB, Zinsen, Kündigung und Widerruf.

# Darlehen und Finanzierung

## Fachkern: Darlehen und Finanzierung
- **Spezialgegenstand:** Darlehen und Finanzierung; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Darlehensverträge nach §§ 488 ff. BGB prüfen: Pflichten beider Seiten, Verbraucherdarlehensrecht, Widerrufsrecht und Kündigung bei Zahlungsverzug.

## Normanker

- §§ 488–490 BGB: Gelddarlehen, Verzinsung, Kündigung
- §§ 491–505e BGB: Verbraucherdarlehen, vorvertragliche Informationspflichten, ESIS
- § 491a BGB: vorvertragliche Informationen beim Verbraucherdarlehen
- § 495 BGB: Widerrufsrecht des Verbrauchers
- § 497 BGB: Verzug des Darlehensnehmers
- § 498 BGB: Kündigung bei Zahlungsverzug (Kreditwürdigkeitsprüfung)
- § 505 BGB: Immobiliar-Verbraucherdarlehensvertrag
- Art. 247 EGBGB: Pflichtangaben im Darlehensvertrag

## Intake

- Handelt es sich um ein Verbraucherdarlehen oder ein Darlehen zwischen Unternehmen?
- Wurden alle Pflichtinformationen nach Art. 247 EGBGB mitgeteilt?
- Hat der Verbraucher fristgerecht widerrufen?
- Liegt ein Zahlungsverzug vor; wurden die Kündigungsvoraussetzungen nach § 498 BGB erfüllt?
- Welche Zinsen und Nebenkosten wurden vereinbart?

## Prüfraster

1. Vertragsschluss: Angebot, Annahme, Form (§ 492 BGB: Schriftform bei Verbraucherdarlehen)
2. Pflichtangaben nach Art. 247 EGBGB: vollständig und rechtzeitig?
3. Widerrufsrecht nach § 495 BGB: Frist (14 Tage), Belehrung, Widerrufsfolgen
4. Auszahlungsanspruch des Darlehensnehmers; Anspruch auf Rückzahlung des Darlehensgebers
5. Zinsen: Zinsvereinbarung, gesetzlicher Zinssatz (§ 246 BGB), Verzugszinsen (§ 497 BGB)
6. Kündigung bei Zahlungsverzug: § 498 BGB (zwei aufeinanderfolgende Raten, Rückstandsquote)
7. Außerordentliche Kündigung nach § 490 BGB
8. Vorzeitige Rückzahlung und Vorfälligkeitsentschädigung

## Fallstricke

- Fehlerhafte Widerrufsbelehrung kann Widerrufsfrist auf ein Jahr und 14 Tage verlängern (§ 356b Abs. 2 BGB).
- Kündigungsvoraussetzungen nach § 498 BGB müssen exakt eingehalten werden; formelle Fehler schaden.
- Vorfälligkeitsentschädigung ist für Verbraucherdarlehen gesetzlich begrenzt.
- Zinsen über dem marktüblichen Niveau können auf Sittenwidrigkeit nach § 138 BGB hindeuten.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Vertragstyp-Prüfung (Verbraucherdarlehen/Unternehmensdarlehen)
- Widerrufsrecht-Zeitlinie
- Kündigungs-Checkliste nach § 498 BGB
- Zinsen- und Kostenmatrix

## Qualitätsregeln

- Verbraucherdarlehensrecht immer bei Kreditnehmern, die natürliche Personen sind, prüfen.
- Widerrufsbelehrung auf inhaltliche Richtigkeit und Vollständigkeit überprüfen.
- § 498 BGB-Kündigungsvoraussetzungen rechnerisch nachvollziehen.

## Anschluss-Skills

- leasing-bgb-bt-schnittstelle
- buergschaft-grundschema-paragraph-765
- schnittstelle-bgb-at-methodenlehre-agb
- workflow-livequellen-rechtsstand

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
