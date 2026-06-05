---
name: arbeitsnaher-dienstvertrag-bauvertrag
description: "Arbeitsnaher Dienstvertrag Bauvertrag: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Arbeitsnaher Dienstvertrag Bauvertrag

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Arbeitsnaher Dienstvertrag Bauvertrag** im Plugin Bgb Bt Pruefer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `arbeitsnaher-dienstvertrag-bgb` | Prüft zivilrechtliche Dienstleistungsverhältnisse mit Arbeitsrechtsnähe, Scheinselbstständigkeit und Vergütungsfragen nach §§ 611 ff. BGB. |
| `bauvertrag-und-verbraucherbauvertrag` | Prüft Bauvertrag §§ 650a ff. BGB, Verbraucherbauvertrag, Abnahme, Mängel und Vergütung. |
| `bt-vertragsentwurf-modellvertrag` | Erstellt und prüft Vertragsentwürfe im Schuldrecht BT: Kaufvertrag, Mietvertrag, Werkvertrag, Auftrag und AGB-Schnittstelle. |

## Arbeitsweg

Im Plugin Bgb Bt Pruefer gilt für **Arbeitsnaher Dienstvertrag Bauvertrag**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `arbeitsnaher-dienstvertrag-bgb`

**Fokus:** Prüft zivilrechtliche Dienstleistungsverhältnisse mit Arbeitsrechtsnähe, Scheinselbstständigkeit und Vergütungsfragen nach §§ 611 ff. BGB.

# Arbeitsnaher Dienstvertrag im BGB

## Fachkern: Arbeitsnaher Dienstvertrag im BGB
- **Spezialgegenstand:** Arbeitsnaher Dienstvertrag im BGB; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Zivilrechtliche Dienstverträge mit Nähe zum Arbeitsrecht systematisch prüfen: Abgrenzung Arbeitsverhältnis/freier Mitarbeiter, Vergütung, Kündigung und Scheinselbstständigkeit.

## Normanker

- §§ 611–630h BGB: Dienstvertrag, Vergütung, Kündigung, Behandlungsvertrag
- § 611a BGB: Arbeitnehmer-Definition, Weisungsgebundenheit
- § 612 BGB: Vergütung ohne ausdrückliche Abrede
- § 621 BGB: Kündigungsfristen bei Dienstverhältnissen
- §§ 157 und 242 BGB: Auslegung und Treu und Glauben
- Sozialversicherungsrecht: § 7 SGB IV (Beschäftigung und Scheinselbstständigkeit)
- BAG-Rechtsprechung zu Arbeitnehmereigenschaft: nur nach Live-Prüfung mit Aktenzeichen zitieren

## Intake

- Welche Parteien und welche Leistungspflichten sind vereinbart?
- Liegt ein schriftlicher Vertrag vor; welche Bezeichnung wurde gewählt?
- Wie ist die tatsächliche Durchführung: Weisungen, Arbeitszeit, Arbeitsort, Eingliederung?
- Welche Vergütung wurde vereinbart und wie wird abgerechnet?
- Ist eine Kündigung ausgesprochen oder beabsichtigt; welche Fristen gelten?
- Gibt es Hinweise auf Scheinselbstständigkeit oder laufende Statusfeststellungsverfahren?

## Prüfraster

1. Vertragstyp bestimmen: Dienst-, Arbeits-, Werk- oder Auftragsverhältnis?
2. Abgrenzungskriterien nach § 611a BGB prüfen: persönliche Abhängigkeit, Weisungsgebundenheit, Eingliederung
3. Tatsächliche Durchführung der Leistung mit Vertragslage vergleichen (substance over form)
4. Vergütungsanspruch nach § 612 BGB prüfen, wenn keine ausdrückliche Vereinbarung besteht
5. Kündigungsfristen nach § 621 BGB berechnen; bei Arbeitsverhältnis § 622 BGB anwenden
6. Scheinselbstständigkeit: sozialversicherungsrechtliche Folgen nach § 7 SGB IV berücksichtigen
7. Haftungsfragen bei fehlerhafter Leistung prüfen: §§ 280 und 241 Abs. 2 BGB
8. Verjährung der Vergütungsansprüche nach §§ 195 und 199 BGB

## Fallstricke

- Vertragliche Bezeichnung als „freier Mitarbeiter" schützt nicht vor Umqualifizierung durch Gerichte.
- Faktische Weisungsgebundenheit begründet Arbeitnehmereigenschaft unabhängig vom Vertragstext.
- Vergütungsansprüche können nach § 612 BGB entstehen, auch wenn kein Betrag vereinbart wurde.
- Sozialversicherungsrechtliche Nachforderungen können rückwirkend vier Jahre betragen.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Einordnungsmemo (Dienstvertrag/Arbeitsvertrag/Werkvertrag) mit Risikoampel
- Abgrenzungsmatrix tatsächliche Durchführung vs. Vertragslage
- Fristenkalender für Kündigung und Verjährung
- Handlungsempfehlung und Lückenliste

## Qualitätsregeln

- Tatsächliche Durchführung immer über formelle Vertragsbezeichnung stellen.
- Scheinselbstständigkeitsrisiken frühzeitig aufzeigen.
- Sozialversicherungsrechtliche und steuerliche Parallelrisiken benennen.
- Keine BAG-Entscheidung ohne Aktenzeichen und frei prüfbare Quelle verwenden.

## Anschluss-Skills

- dienstvertrag-und-behandlungsvertrag
- werk-dienst-abgrenzung-erfolg
- geschaeftsbesorgung-auftrag-mandat
- workflow-anfangercoach-schuldrecht-bt

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `bauvertrag-und-verbraucherbauvertrag`

**Fokus:** Prüft Bauvertrag §§ 650a ff. BGB, Verbraucherbauvertrag, Abnahme, Mängel und Vergütung.

# Bauvertrag und Verbraucherbauvertrag

## Fachkern: Bauvertrag und Verbraucherbauvertrag
- **Spezialgegenstand:** Bauvertrag und Verbraucherbauvertrag; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Bauvertragsrecht nach §§ 650a–650v BGB und VOB/B-Parallelrecht prüfen: Leistungspflichten, Abnahme, Mängelrechte, Vergütungsanpassung und Sonderkündigungsrecht.

## Normanker

- §§ 650a–650v BGB: Bauvertrag, Verbraucherbauvertrag, Architekten- und Ingenieurvertrag
- §§ 631–650 BGB: allgemeines Werkvertragsrecht als Basis
- § 640 BGB: Abnahme und Abnahmepflicht
- § 641 BGB: Fälligkeit der Vergütung
- § 650b BGB: Anordnungsrecht des Bestellers
- § 650c BGB: Vergütungsanpassung bei Anordnungen
- § 650e BGB: Sicherungshypothek des Unternehmers
- § 650f BGB: Bauhandwerkersicherheit
- §§ 650i–650n BGB: Verbraucherbauvertrag (Informationspflichten, Widerrufsrecht)
- VOB/B als ergänzendes Regelwerk (nur wenn vereinbart)

## Intake

- Handelt es sich um einen einfachen Bauvertrag oder einen Verbraucherbauvertrag?
- Ist die VOB/B wirksam in den Vertrag einbezogen worden?
- Welche Leistungspflichten wurden vereinbart und welche Abweichungen sind eingetreten?
- Wurde die Abnahme erklärt oder verweigert; liegen Mängel vor?
- Gibt es Anordnungen des Bestellers nach § 650b BGB und wie wurde die Vergütung angepasst?
- Welche Sicherheiten wurden gestellt oder gefordert?
- Bestehen Kündigungsrechte nach § 648 oder § 648a BGB?

## Prüfraster

1. Vertragstyp: Bauvertrag (§ 650a BGB), Verbraucherbauvertrag (§ 650i BGB) oder allgemeiner Werkvertrag?
2. VOB/B-Einbeziehung und AGB-Wirksamkeit nach §§ 305 ff. BGB prüfen
3. Abnahme: ordnungsgemäße Erklärung, fiktive Abnahme, verweigerte Abnahme mit Mängelrüge
4. Mängel: Sachmangel nach § 633 BGB, Nacherfüllungspflicht, Fristsetzung
5. Vergütungsanpassung bei Anordnungen nach § 650c BGB
6. Sicherungshypothek (§ 650e BGB) und Bauhandwerkersicherheit (§ 650f BGB) prüfen
7. Kündigung: freie Kündigung (§ 648 BGB), außerordentliche Kündigung (§ 648a BGB)
8. Verjährung der Mängelrechte: § 634a BGB (5 Jahre bei Bauwerken)

## Fallstricke

- Beim Verbraucherbauvertrag gelten strenge Informationspflichten und ein Widerrufsrecht nach § 650l BGB.
- Die fiktive Abnahme setzt eine ordnungsgemäße Fristsetzung voraus.
- Vergütungsanpassung nach § 650c BGB muss rechtzeitig geltend gemacht werden.
- VOB/B-Klauseln können gegenüber Verbrauchern als AGB unwirksam sein.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Vertragstyp-Einordnung mit Risikoampel
- Abnahme- und Mängelrechtsprüfung
- Vergütungsmatrix mit Anordnungsfolgen
- Kündigungsfolgenabschätzung und Lückenliste

## Qualitätsregeln

- Abnahme immer als Zäsur für Gewährleistungsfrist und Beweislastumkehr markieren.
- Bei Verbraucherbauvertrag Informationspflichten und Widerrufsrecht gesondert prüfen.
- VOB/B nur anwenden, wenn wirksam einbezogen.

## Anschluss-Skills

- werkvertrag-grundschema-paragraph-631
- werkvertrag-abnahme-und-faelligkeit
- werkvertrag-maengelrechte
- workflow-fristen-ruecktritt-kuendigung

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `bt-vertragsentwurf-modellvertrag`

**Fokus:** Erstellt und prüft Vertragsentwürfe im Schuldrecht BT: Kaufvertrag, Mietvertrag, Werkvertrag, Auftrag und AGB-Schnittstelle.

# BT-Vertragsentwurf und Modellvertrag

## Fachkern: BT-Vertragsentwurf und Modellvertrag
- **Spezialgegenstand:** BT-Vertragsentwurf und Modellvertrag; der Skill muss die konkrete Fachfrage tragen und nicht nur in einen allgemeinen Startdialog zurückfallen.
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.


## Zweck

Vertragsentwürfe im BGB Schuldrecht BT erstellen, prüfen und roten Fäden zuordnen: Kaufvertrag, Mietvertrag, Werkvertrag, Auftrag und Geschäftsbesorgung mit AGB-Konformität.

## Normanker

- §§ 241 ff. BGB: Schuldverhältnis und Nebenpflichten
- §§ 305–310 BGB: AGB-Recht, Einbeziehung, Inhaltskontrolle
- §§ 433 ff. BGB: Kaufvertrag
- §§ 535 ff. BGB: Mietvertrag
- §§ 631 ff. BGB: Werkvertrag
- §§ 662 ff. BGB: Auftrag
- § 675 BGB: Geschäftsbesorgungsvertrag
- §§ 312 ff. BGB: Verbrauchervertragsrecht, Fernabsatz, Widerruf

## Intake

- Welcher Vertragstyp soll entworfen oder geprüft werden?
- Handelt es sich um ein B2B- oder B2C-Verhältnis (AGB-Kontrolle relevant)?
- Welche Hauptleistungspflichten und Nebenpflichten sollen geregelt werden?
- Bestehen gesetzliche Formvorgaben (§ 311b BGB, § 550 BGB, § 578 BGB)?
- Welche Haftungsbeschränkungen und Gewährleistungsausschlüsse sind gewünscht?
- Gibt es Fernabsatz- oder Haustürgeschäftselemente?

## Prüfraster

1. Vertragstyp-Identifikation und anwendbare Normen bestimmen
2. Vertragsschluss: Angebot, Annahme, Form, AGB-Einbeziehung nach § 305 Abs. 2 BGB
3. Hauptleistungspflichten vollständig und eindeutig formulieren
4. Nebenpflichten nach § 241 Abs. 2 BGB: Informations-, Schutz- und Aufklärungspflichten
5. Gewährleistungsregelungen: gesetzliche Ansprüche, Verkürzungen, § 309 Nr. 8 BGB
6. Haftungsbeschränkungen: § 309 Nr. 7 BGB, § 307 BGB Generalklausel
7. Laufzeit, Kündigung und Verlängerungsklauseln
8. Fernabsatz- und Widerrufsrecht nach §§ 312 ff. BGB bei Verbraucherverträgen

## Fallstricke

- Gewährleistungsausschlüsse gegenüber Verbrauchern sind nach § 309 Nr. 8 BGB weitgehend unwirksam.
- Überraschende Klauseln nach § 305c BGB werden nicht Vertragsbestandteil.
- Zu kurze Mängelrügefristen können bei Bauwerken gegen § 309 Nr. 8 BGB verstoßen.
- Formvorschriften (Schriftform, notarielle Beurkundung) müssen explizit geprüft werden.
## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Output

- Vertragsentwurf mit kommentierten Klauseln
- AGB-Risikoliste (unwirksame Klauseln markiert)
- Formcheckliste
- Empfehlungen zur Überarbeitung

## Qualitätsregeln

- Jede Klausel auf AGB-Wirksamkeit und Transparenzgebot prüfen.
- B2C-Verträge immer gesondert auf Verbraucherschutzrecht prüfen.
- Formvorgaben nicht durch Checkliste pauschal abhaken; individuell prüfen.

## Anschluss-Skills

- schnittstelle-bgb-at-methodenlehre-agb
- vertragstypen-mischvertrag-router
- kaufvertrag-grundschema-paragraph-433
- bt-fristen-erklaerungen-zugang

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
