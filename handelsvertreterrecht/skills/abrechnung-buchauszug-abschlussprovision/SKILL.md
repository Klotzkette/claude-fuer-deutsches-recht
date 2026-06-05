---
name: abrechnung-buchauszug-abschlussprovision
description: "Abrechnung Buchauszug Abschlussprovision: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Abrechnung Buchauszug Abschlussprovision

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Abrechnung Buchauszug Abschlussprovision** im Plugin Handelsvertreterrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `abrechnung-und-buchauszug` | Unterstützt Handelsvertreter und Unternehmer bei Streitigkeiten über Provisionsabrechnungen und den Buchauszug nach § 87c HGB: Prüfung von Vollständigkeit und Richtigkeit der Abrechnung, Formulierung von Buchauszugsverlangen, Klageerhebung bei Verweigerung sowie Auswertung übergebener Daten auf Lücken und Stornoreserven. |
| `abschlussprovision` | Prüft den Provisionsanspruch des Abschlussvertreters nach §§ 87 und 87a HGB: Kausalität zwischen Vermittlungstätigkeit und Vertragsabschluss, Fälligkeit mit Ausführung durch den Unternehmer, Ansprüche bei vorzeitiger Vertragsauflösung sowie Abgrenzung von Abschluss- und Vermittlungsprovision. |
| `abschlussvertreter` | Klärt Rechtsstellung und Haftungsrahmen des Abschlussvertreters mit Abschlussvollmacht nach §§ 84 und 54 HGB: Vollmachtsumfang, Wirksamkeit abgeschlossener Verträge, Haftung bei Überschreitung der Vollmacht sowie Abgrenzung zum Vermittlungsvertreter ohne Abschlussbefugnis. |
| `agb-kontrolle` | Prüft AGB-Klauseln in Handelsvertreterverträgen auf Wirksamkeit nach §§ 305 ff. BGB und § 92c HGB: unangemessene Benachteiligung bei Provisionsregelungen, Ausgleichsausschlüssen, Wettbewerbsverboten sowie unzulässige Abweichungen vom zwingenden Handelsvertreterrecht nach §§ 84-92c HGB. |

## Arbeitsweg

Im Plugin Handelsvertreterrecht gilt für **Abrechnung Buchauszug Abschlussprovision**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `abrechnung-und-buchauszug`

**Fokus:** Unterstützt Handelsvertreter und Unternehmer bei Streitigkeiten über Provisionsabrechnungen und den Buchauszug nach § 87c HGB: Prüfung von Vollständigkeit und Richtigkeit der Abrechnung, Formulierung von Buchauszugsverlangen, Klageerhebung bei Verweigerung sowie Auswertung übergebener Daten auf Lücken und Stornoreserven.

# Provisionsabrechnung und Buchauszug nach § 87c HGB

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Provisionsabrechnung und Buchauszug nach § 87c HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie einschlägige BGH- und EuGH-Rechtsprechung ein.
Der Skill zielt auf konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X stellt fest, dass Unternehmer Y seit 18 Monaten keine vollständige Provisionsabrechnung übermittelt; X verlangt Buchauszug über alle vermittelten und abgeschlossenen Geschäfte nach § 87c Abs. 2 HGB.
- Unternehmer Y bestreitet, dass bestimmte Kunden vom Bezirk des X umfasst waren; X klagt auf Erteilung des Buchauszugs und ergänzende Auskunft.
- Handelsvertreterin Z prüft, ob die vom Unternehmer vorgelegte Abrechnung alle provisionspflichtigen Geschäfte enthält, insbesondere Direktabschlüsse und Folgegeschäfte.

## Erste Schritte

1. Vertrag und Provisionsvereinbarungen sichten; Abrechnungszeitraum und Rückstände bestimmen.
2. Schriftliches Buchauszugsverlangen nach § 87c Abs. 2 HGB formulieren und per Einschreiben übersenden.
3. Gelieferte Buchauszüge auf Vollständigkeit prüfen: alle Kunden, Aufträge, Umsätze, Rabatte, Stornos.
4. Fehlende Positionen in Differenzaufstellung erfassen und Nachforderung beziffern.
5. Bei Verweigerung: Klage auf Erteilung des Buchauszugs (Stufenklage nach § 254 ZPO) vorbereiten.
6. Verjährungsfristen nach § 195 BGB (3 Jahre) und Beginn nach § 199 BGB prüfen.

## Rechtsrahmen

- § 87c HGB — Provisionsabrechnung und Buchauszugsanspruch des Handelsvertreters
- § 87 HGB — Provisionsanspruch und provisionspflichtige Geschäfte
- § 87a HGB — Entstehung und Fälligkeit des Provisionsanspruchs
- § 254 ZPO — Stufenklage (Auskunft und Leistung)
- § 195 BGB — Regelmäßige Verjährungsfrist drei Jahre
- Art. 12 RL 86/653/EWG — Provisionsanspruch des Handelsvertreters

## Prüfraster

- Ist der Buchauszugsanspruch entstanden (Handelsvertretervertrag, provisionspflichtige Geschäfte)?
- Umfasst der vorgelegte Buchauszug alle vertragsrelevanten Geschäfte und Kunden?
- Wurden Stornoreserven oder Rückbuchungen korrekt und nachvollziehbar ausgewiesen?
- Ist der Abrechnungszeitraum vollständig abgedeckt, einschließlich Direktgeschäfte des Unternehmers?
- Besteht ein ergänzender Auskunftsanspruch nach § 87c Abs. 2 HGB bei unklaren Positionen?
- Sind Verjährungsfristen für einzelne Abrechnungsperioden bereits abgelaufen?
- Kommt eine Stufenklage auf Buchauszug, Abrechnung und Zahlung in Betracht?

## Typische Fallstricke

- Buchauszugsverlangen nicht schriftlich oder ohne genaue Periodenangabe gestellt — Beweisschwierigkeiten.
- Verjährung einzelner Provisionsforderungen übersehen, obwohl Buchauszugsanspruch noch offen ist.
- Unternehmer legt unvollständigen Buchauszug vor; Handelsvertreter akzeptiert ohne Gegenkontrolle.
- Stornoreserven ohne vertragliche Grundlage einbehalten — Prüfung der AGB-Konformität versäumt.

## Output

Buchauszugs-Anforderungsschreiben, Differenzaufstellung mit Nachforderungsberechnung, Entwurf Stufenklage nach § 254 ZPO.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien sind: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Praktisch relevant sind insbesondere: Provisionsabrechnungen und Buchauszug (§ 87c HGB),
nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Ausgleichsanspruch (§ 89b HGB).
Zwingende Vorschriften zum Schutz des Handelsvertreters nach § 92c HGB können vertraglich
nicht abgebedungen werden; entgegenstehende Klauseln sind nach § 134 BGB nichtig.

## Quellen

- [§ 87c HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__87c.html)
- [§ 87 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__87.html)
- [§ 254 ZPO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/zpo/__254.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 87c HGB](https://dejure.org/gesetze/HGB/87c.html)

## 2. `abschlussprovision`

**Fokus:** Prüft den Provisionsanspruch des Abschlussvertreters nach §§ 87 und 87a HGB: Kausalität zwischen Vermittlungstätigkeit und Vertragsabschluss, Fälligkeit mit Ausführung durch den Unternehmer, Ansprüche bei vorzeitiger Vertragsauflösung sowie Abgrenzung von Abschluss- und Vermittlungsprovision.

# Abschlussprovision des Abschlussvertreters nach §§ 87 und 87a HGB

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Abschlussprovision des Abschlussvertreters nach §§ 87 und 87a HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie einschlägige BGH- und EuGH-Rechtsprechung ein.
Der Skill zielt auf konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter A hat einen Kaufvertrag zwischen Kunde K und Unternehmer U abgeschlossen; U verweigert die Provisionszahlung mit Hinweis auf angeblich fehlende Kausalität der Vermittlung.
- Unternehmer U löst einen vom Vertreter A abgeschlossenen Vertrag einvernehmlich mit dem Kunden auf; A verlangt seine Provision nach § 87a Abs. 3 HGB.
- Handelsvertreter A streitet mit U darüber, ob ein bestimmter Auftrag im Rahmen der Abschlussvertretung oder außerhalb seiner Vollmacht zustande kam.

## Erste Schritte

1. Vertragsart klären: Abschlussvertreter mit Vollmacht oder Vermittlungsvertreter ohne Abschlussvollmacht?
2. Kausalzusammenhang zwischen Tätigkeit des Vertreters und Vertragsabschluss dokumentieren.
3. Fälligkeitszeitpunkt nach § 87a Abs. 1 HGB bestimmen: Ausführung des Geschäfts durch Unternehmer.
4. Provisionssatz und Bemessungsgrundlage aus dem Vertretervertrag ermitteln.
5. Bei vorzeitiger Aufhebung: Prüfung nach § 87a Abs. 3 HGB, ob Aufhebung dem Unternehmer zuzurechnen ist.
6. Verjährung prüfen: §§ 195, 199 BGB; Abschlusszeitpunkt festhalten.

## Rechtsrahmen

- § 87 HGB — Entstehung des Provisionsanspruchs, Kausalität
- § 87a HGB — Fälligkeit und Erlöschen der Provision
- § 87a Abs. 3 HGB — Provision bei nicht ausgeführtem Geschäft ohne Vertreterverschulden
- § 84 HGB — Begriff des Handelsvertreters und Selbständigkeit
- § 54 HGB — Handlungsvollmacht des Abschlussvertreters
- Art. 7 und 8 RL 86/653/EWG — Provisionsanspruch auf abgeschlossene und ausgeführte Geschäfte

## Prüfraster

- Hat der Handelsvertreter den Vertragsabschluss tatsächlich herbeigeführt oder wesentlich mitgewirkt?
- Ist das Geschäft wirksam zustande gekommen und liegt im Vertragsgebiet oder beim Kundenstamm des Vertreters?
- Hat der Unternehmer das Geschäft ausgeführt oder verweigert er dies ohne Verschulden des Vertreters?
- Liegt eine einvernehmliche Aufhebung vor, die dem Unternehmer nach § 87a Abs. 3 HGB zuzurechnen ist?
- Entspricht die berechnete Provision dem vereinbarten Satz und der richtigen Bemessungsgrundlage?
- Ist der Anspruch verjährt oder durch vertragliche Ausschlussfristen erloschen?

## Typische Fallstricke

- Kausalität nicht ausreichend dokumentiert — Unternehmer bestreitet Vermittlungsleistung.
- Fälligkeitszeitpunkt falsch bestimmt: Provision erst fällig, wenn Unternehmer das Geschäft ausführt.
- § 87a Abs. 3 HGB bei einvernehmlicher Vertragsaufhebung übersehen.
- Abschlussvertreter handelt ohne ausreichende Vollmacht — Provisionsanspruch gefährdet.
- Provisionssatz aus alten Vertragsversionen übernommen — aktuelle Fassung nicht geprüft.

## Output

Provisionsberechnung mit Kausalitätsnachweis, Klageschriftentwurf auf Provisionszahlung, Fristenübersicht.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien sind: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Praktisch relevant sind insbesondere: Provisionsabrechnungen und Buchauszug (§ 87c HGB),
nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Ausgleichsanspruch (§ 89b HGB).
Zwingende Vorschriften zum Schutz des Handelsvertreters nach § 92c HGB können vertraglich
nicht abgebedungen werden; entgegenstehende Klauseln sind nach § 134 BGB nichtig.

## Quellen

- [§ 87 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__87.html)
- [§ 87a HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__87a.html)
- [§ 84 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__84.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 87 HGB](https://dejure.org/gesetze/HGB/87.html)

## 3. `abschlussvertreter`

**Fokus:** Klärt Rechtsstellung und Haftungsrahmen des Abschlussvertreters mit Abschlussvollmacht nach §§ 84 und 54 HGB: Vollmachtsumfang, Wirksamkeit abgeschlossener Verträge, Haftung bei Überschreitung der Vollmacht sowie Abgrenzung zum Vermittlungsvertreter ohne Abschlussbefugnis.

# Rechtsstellung des Abschlussvertreters nach §§ 84 und 54 HGB

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um Rechtsstellung des Abschlussvertreters nach §§ 84 und 54 HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie einschlägige BGH- und EuGH-Rechtsprechung ein.
Der Skill zielt auf konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter B hat im Namen von Unternehmer U einen Großauftrag abgeschlossen; U bestreitet nachträglich die Wirksamkeit, weil B seine Vollmacht überschritten habe.
- Unternehmer U prüft, ob ein von seinem Abschlussvertreter B geschlossener Rabattvertrag ihn bindet oder ob B gegen Weisungen verstoßen hat.
- Handelsvertreter B will wissen, ob er für einen mangelhaften Kaufvertrag haftet, den er in Vollmacht von U abgeschlossen hat.

## Erste Schritte

1. Vollmachtsurkunde und Vertretervertrag auf Umfang und Einschränkungen der Abschlussvollmacht prüfen.
2. Vertretungshandlung auf Vollmachtskonformität prüfen: Gebiet, Warengruppe, Kundenstamm, Preisrahmen.
3. Wirksamkeit des abgeschlossenen Vertrags nach §§ 164 ff. BGB bestimmen.
4. Bei Überschreitung: Genehmigung durch den Unternehmer und Handelndenhaftung nach § 179 BGB prüfen.
5. Abgrenzung Abschlussvertreter vs. Vermittlungsvertreter anhand konkreter Vollmachtserteilung klären.
6. Dokumentation der Vollmachtsgrundlagen für spätere Streitigkeiten sichern.

## Rechtsrahmen

- § 84 HGB — Begriff des Handelsvertreters
- § 54 HGB — Handlungsvollmacht
- §§ 164–181 BGB — Stellvertretung, Vollmacht, Missbrauch
- § 179 BGB — Haftung des Vertreters ohne Vertretungsmacht
- § 91a HGB — Abschlussvertreter in Ausnahmefällen
- Art. 1 Abs. 2 RL 86/653/EWG — Handelsvertreter mit dauernder Vollmacht

## Prüfraster

- Bestand eine wirksame Abschlussvollmacht zum Zeitpunkt des Vertragsschlusses?
- Hat der Handelsvertreter die Grenzen der Vollmacht eingehalten (Betrag, Ware, Kundenstamm)?
- Ist der abgeschlossene Vertrag für den Unternehmer bindend oder ist Genehmigung erforderlich?
- Haftet der Handelsvertreter persönlich nach § 179 BGB bei Vollmachtsüberschreitung?
- Liegt eine Anscheinsvollmacht oder Duldungsvollmacht des Unternehmers vor?
- Hat der Handelsvertreter Informationspflichten gegenüber dem Unternehmer nach § 86 HGB erfüllt?

## Typische Fallstricke

- Vollmachtsüberschreitung nicht erkannt — Unternehmer bleibt gebunden, wenn er genehmigt.
- Fehlende schriftliche Vollmachtsurkunde erschwert Nachweis gegenüber Dritten.
- Anscheinsvollmacht durch jahrelange Duldung — Unternehmer kann Verträge nicht mehr anfechten.
- Abgrenzung zum Vermittlungsvertreter unklar — Provisionsstruktur und Haftung divergieren.

## Output

Vollmachtsprüfungsvermerk, Risikobewertung abgeschlossener Verträge, Empfehlung zur Vollmachtsgestaltung.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien sind: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Praktisch relevant sind insbesondere: Provisionsabrechnungen und Buchauszug (§ 87c HGB),
nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Ausgleichsanspruch (§ 89b HGB).
Zwingende Vorschriften zum Schutz des Handelsvertreters nach § 92c HGB können vertraglich
nicht abgebedungen werden; entgegenstehende Klauseln sind nach § 134 BGB nichtig.

## Quellen

- [§ 84 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__84.html)
- [§ 54 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__54.html)
- [§ 179 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__179.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 84 HGB](https://dejure.org/gesetze/HGB/84.html)

## 4. `agb-kontrolle`

**Fokus:** Prüft AGB-Klauseln in Handelsvertreterverträgen auf Wirksamkeit nach §§ 305 ff. BGB und § 92c HGB: unangemessene Benachteiligung bei Provisionsregelungen, Ausgleichsausschlüssen, Wettbewerbsverboten sowie unzulässige Abweichungen vom zwingenden Handelsvertreterrecht nach §§ 84-92c HGB.

# AGB-Kontrolle im Handelsvertretervertrag nach §§ 305 ff. BGB und § 92c HGB

## Überblick

Dieser Skill unterstützt bei rechtlichen Fragen rund um AGB-Kontrolle im Handelsvertretervertrag nach §§ 305 ff. BGB und § 92c HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie einschlägige BGH- und EuGH-Rechtsprechung ein.
Der Skill zielt auf konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X erhält vom Unternehmer Y vorformulierte Vertragsbedingungen mit einer Klausel, die den Ausgleichsanspruch vollständig ausschließt; X prüft die Wirksamkeit nach § 89b Abs. 4 HGB.
- Unternehmer Y verwendet eine AGB-Klausel, die Provisionen um 20 % kürzt, wenn der Jahresumsatz ein bestimmtes Ziel verfehlt; die Klausel wird auf Wirksamkeit nach § 307 BGB geprüft.
- Handelsvertreter X findet in seinem Vertrag eine AGB-Klausel, die das Wettbewerbsverbot auf fünf Jahre verlängert und keine Karenzentschädigung vorsieht; X lässt die Klausel auf Verstoß gegen § 90a HGB prüfen.

## Erste Schritte

1. Vertrag auf vorformulierte Klauseln i.S.v. § 305 BGB identifizieren.
2. Zwingende Normen des Handelsvertreterrechts (§§ 84-92c HGB) als Prüfmaßstab herausarbeiten.
3. Einzelne Klauseln auf unangemessene Benachteiligung nach § 307 BGB prüfen.
4. Klauselverbote nach §§ 308, 309 BGB auf handelsvertretertypische Klauseln anwenden.
5. Klauseln, die vom zwingenden Recht abweichen, nach § 92c HGB auf Zulässigkeit prüfen.
6. Nichtige Klauseln identifizieren und Rechtsfolgen (Wegfall, gesetzliche Regelung) bestimmen.

## Rechtsrahmen

- §§ 305–310 BGB — AGB-Recht, Einbeziehung, Inhaltskontrolle
- § 307 BGB — Unangemessene Benachteiligung
- § 92c HGB — Zwingende Vorschriften des Handelsvertreterrechts
- § 89b Abs. 4 HGB — Zwingende Natur des Ausgleichsanspruchs
- § 90a Abs. 1 S. 2 HGB — Mindestinhalt der Wettbewerbsabrede
- Art. 19 RL 86/653/EWG — Unabdingbare Rechte des Handelsvertreters

## Prüfraster

- Sind die streitigen Klauseln AGB i.S.v. § 305 Abs. 1 BGB oder individuell ausgehandelt?
- Weichen die Klauseln von zwingenden Vorschriften der §§ 84-92c HGB ab?
- Liegt eine unangemessene Benachteiligung nach § 307 BGB vor?
- Verstoßen einzelne Klauseln gegen konkrete Klauselverbote der §§ 308, 309 BGB?
- Was sind die Rechtsfolgen der Nichtigkeit — Gesamtnichtigkeit oder Teilwegfall?
- Ist die Klausel durch ergänzende Vertragsauslegung zu ersetzen oder gilt dispositives Recht?

## Typische Fallstricke

- Zwingendes Handelsvertreterrecht (§ 92c HGB) nicht als Maßstab berücksichtigt.
- Kaufmännische AGB-Kontrolle mit verbraucherrechtlichem Maßstab verwechselt.
- Ausgleichsausschlussklauseln als wirksam behandelt, obwohl § 89b Abs. 4 HGB diese verbietet.
- Nichtigkeit der Klausel führt nicht automatisch zur Gesamtnichtigkeit des Vertrags (§ 306 BGB).

## Output

AGB-Prüfvermerk mit Bewertung jeder Klausel, Empfehlung zur Vertragsanpassung, Formulierungsvorschläge für rechtssichere Klauseln.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien sind: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Praktisch relevant sind insbesondere: Provisionsabrechnungen und Buchauszug (§ 87c HGB),
nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Ausgleichsanspruch (§ 89b HGB).
Zwingende Vorschriften zum Schutz des Handelsvertreters nach § 92c HGB können vertraglich
nicht abgebedungen werden; entgegenstehende Klauseln sind nach § 134 BGB nichtig.

## Quellen

- [§ 307 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__307.html)
- [§ 92c HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__92c.html)
- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 307 BGB](https://dejure.org/gesetze/BGB/307.html)
