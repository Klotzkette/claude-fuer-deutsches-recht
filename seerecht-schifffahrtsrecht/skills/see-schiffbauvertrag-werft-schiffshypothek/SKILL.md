---
name: see-schiffbauvertrag-werft-schiffshypothek
description: "SEE Schiffbauvertrag Werft Schiffshypothek: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# SEE Schiffbauvertrag Werft Schiffshypothek

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **SEE Schiffbauvertrag Werft Schiffshypothek** im Plugin Seerecht Schifffahrtsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `see-005-schiffbauvertrag-werft` | Reeder beauftragt Werft mit Neubau: Pruefung des Schiffbauvertrags auf Lieferpflichten; Gewaehrleistung; Verzoegerungsstrafen; Abnahme und Finanzierungssicherheiten. BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104 Schiffbauwerkshypothek; Refund Guarantee; SAJ/AWES-Muster. Output: Vertragsrisiko-Matrix und Verhandlungsempfehlung. |
| `see-023-schiffshypothek-kaufvertrag-scopen` | Schiffshypothek: Schiffsfinanzierungsbank oder Hypothekenglaeubigerbank scopet Kaufvertrag fuer hypothekenbelastetes Seeschiff: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. SchRG §§ 8-75; HGB §§ 596-601 Schiffsglaeubigerrechte. Output: Kaufvertrag-Review-Matrix und Closing-Conditions. |
| `see-033-schiffbauwerk-kaufvertrag-scopen` | Schiffbauwerk: Werft; Auftraggeber-Reeder; finanzierende Bank scopet Kaufvertrag fuer Schiff im Bau (Schiffbauwerk): Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. SchRG §§ 76-104 Schiffbauwerkshypothek; BGB §§ 631-651 Werkvertrag. Output: Kaufvertrag-Review-Matrix und Closing-Conditions. |
| `see-041-werftvertrag-register-pruefen` | Werftvertrag: Reeder oder Werft; Streit um Lieferung; Preisanpassung; Maengel prueft Schiffbauwerksregister ab Kiellegung auf Eigentumsstand, Hypotheken, Arreste und gesetzliche Vorrechte. BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104; CISG wenn nicht ausgeschlossen. Klaert Lastenfreiheit vor Closing oder Kreditvergabe. Output: Registerpruefprotokoll und Rangkarte. |
| `see-042-werftvertrag-hypothek-bestellen` | Werftvertrag: Reeder oder Werft; Streit um Lieferung; Preisanpassung; Maengel bestellt Schiffshypothek als Sicherheit fuer Finanzierung eines Neubauprojekt unter Werftvertrag. BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104; CISG wenn nicht ausgeschlossen. Notarielle Bestellungsurkunde, Rangstelle, Sicherungsabrede, Zubehoer-Mithaftung (SchRG § 31). Output: Bestellungs-Checkliste. |

## Arbeitsweg

Im Plugin Seerecht Schifffahrtsrecht gilt für **SEE Schiffbauvertrag Werft Schiffshypothek**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `see-005-schiffbauvertrag-werft`

**Fokus:** Reeder beauftragt Werft mit Neubau: Pruefung des Schiffbauvertrags auf Lieferpflichten; Gewaehrleistung; Verzoegerungsstrafen; Abnahme und Finanzierungssicherheiten. BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104 Schiffbauwerkshypothek; Refund Guarantee; SAJ/AWES-Muster. Output: Vertragsrisiko-Matrix und Verhandlungsempfehlung.

# Schiffbauvertrag Werft – Risikoprüfung

## Mandantenfall
Ein Reeder schließt mit einer polnischen Werft einen Vertrag über drei Mehrzweckfrachter; Lieferung in 24 Monaten; die Finanzierungsbank besteht auf Sicherheiten für die Anzahlung. Eine chinesische Werft verlangt nach Stahlpreisanstieg eine Preisanpassung; der Reeder lehnt ab. Ein Reeder nimmt ein Schiff mit erheblichen Mängelrügen ab; Werft beansprucht vollständige Zahlung.

## Erste Schritte
1. Vertragswerk sichten: Hauptvertrag (SAJ/AWES-Muster oder individuell); Spezifikationen; technische Anhänge; Zahlungsplan.
2. Anzahlungssicherheiten prüfen: Bankgarantie der Werftbank oder Refund Guarantee; Abrufbedingungen.
3. Schiffbauwerkshypothek aufnehmen: SchRG §§ 76-104 – Hypothek am Schiff im Bau; Baufinanzierung sichert Rohbau.
4. Lieferverzug-Regime analysieren: Strafklauseln (Liquidated Damages); Kündigungsrecht bei Verzug; Force-Majeure-Definition.
5. Abnahmeverfahren klären: Probefahrt; Klasseabnahme (GL/DNV); IMO-Zertifikate.
6. Gewährleistungsfristen und Nachbesserungsrechte (BGB § 634) abgleichen.

## Rechtsrahmen
- BGB §§ 631-651: Werkvertragsrecht; Abnahme (§ 640); Mängelrechte (§ 634); Verjährung (§ 634a 5 Jahre für Schiffbau).
- SchRG §§ 76-104: Schiffbauwerkshypothek; Bestellung und Rang während der Bauphase.
- HGB §§ 480-482: Hintergrund für Lieferverpflichtungen.
- CISG (UN-Kaufrecht): bei internationalen Werftverträgen oft ausgeschlossen; Ausschlussklausel prüfen.
- ZPO §§ 864-871: Vollstreckung in Schiffbauwerkshypothek bei Werftinsolvenz.

## Prüfraster
- Ist die Refund Guarantee abrufbar und unwiderruflich?
- Welche Ereignisse gelten als Bauverzug; wie hoch ist die LD-Rate?
- Kann der Reeder bei Werftinsolvenz das Schiff aus dem Bau herauslösen (SchRG § 76)?
- Decken die Mängelklauseln auch latente Mängel nach Abnahme ab?
- Ist der Gerichtsstand klar vereinbart; welches Recht gilt?

## Typische Fallstricke
- Pauschalschadenersatz (LD) begrenzt den Schadensanspruch; echter Schaden kann höher liegen.
- CISG nicht ausgeschlossen: UN-Kaufrecht kann auf Schiffbauverträge anwendbar sein.
- Schiffbauwerkshypothek erlischt mit Eintragung als fertiges Schiff; Übergang auf Seeschiffshypothek muss aktiv beantragt werden.
- Force-Majeure-Klauseln schließen Stahlpreiserhöhungen nicht automatisch ein.

## Output
- Vertragsrisiko-Matrix: Lieferung; Zahlung; Mängel; Insolvenz; Gewährleistung
- Verhandlungsempfehlung: Klauseln nachbessern
- Checkliste Schiffbauhypothek und Sicherheitenpaket


## Erweiterte Normengrundlage

### Werkvertragsrecht
- BGB §§ 631-650: Werkvertrag; Abnahme; Mängelhaftung; Vergütung; Kündigung.
- BGB § 640: Abnahme des Werkes; Fälligkeit der Vergütung; Abnahmefiktion.
- BGB § 641: Fälligkeit der Vergütung; Zahlung Zug-um-Zug gegen Abnahme.

### Schiffbauwerkshypothek
- SchRG §§ 76-104: Schiffbauwerkshypothek; Entstehung; Eintragungsvoraussetzungen; Ausübung.
- SchRG § 76: Belastbarkeit eines im Bau befindlichen Schiffes als Schiffsbauwerk.
- SchRG § 78: Eintragung im Schiffsbauregister beim zuständigen Amtsgericht am Bauort.

## Checkliste Werftvertrag-Prüfung
- [ ] Bauvertrag (Shipbuilding Contract) vollständig analysiert
- [ ] Spezifikationen (Technical Specifications) geprüft; Keel-Laying-Datum; Liefertermin
- [ ] Abschlagszahlungen (Installment Schedule) und Zahlungsplan dokumentiert
- [ ] Refund Guarantee der Werftbank angefordert und geprüft
- [ ] Schiffbauwerkshypothek eingetragen; Rang bestätigt
- [ ] Abnahmeprotokoll (Protocol of Delivery and Acceptance) Muster bereit

## Relevante Rechtsprechung
- BGH zur Haftung des Werftunternehmers für Konstruktionsfehler; BGB §§ 633-634.
- OLG Hamburg zur Auslegung von Force-Majeure-Klauseln in Schiffbauverträgen.
- BGH zur Sicherungszession der Refund-Guarantee durch den Kreditgeber.


## Praxishinweis

Die oben genannten Normen bilden den Mindest-Recherche-Kanon. Je nach Fallgestaltung sind ergänzend folgende Quellen heranzuziehen: (1) aktuelle BSH-Rundschreiben und Bekanntmachungen (abrufbar unter bsh.de); (2) Verwaltungsvorschriften der zuständigen Wasser- und Schifffahrtsverwaltung; (3) aktuelle Entscheidungen des LG und OLG Hamburg zu seerechtlichen Fragen (openjur.de); (4) ITLOS-Rechtsprechungsdatenbank (itlos.org). Bei internationalem Bezug ist stets zu prüfen, ob der betreffende Staat UNCLOS-, MLC- oder MARPOL-Vertragsstaat ist und ob ISAC 1952 gilt.

## Quellen
- BGB § 634a Verjährung: https://www.gesetze-im-internet.de/bgb/__634a.html
- SchRG §§ 76-104: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- HGB § 480: https://dejure.org/gesetze/HGB/480.html
- BGH Werkvertragsrecht Schiffbau: https://www.bgh.de
- dejure BGB § 631: https://dejure.org/gesetze/BGB/631.html

## 2. `see-023-schiffshypothek-kaufvertrag-scopen`

**Fokus:** Schiffshypothek: Schiffsfinanzierungsbank oder Hypothekenglaeubigerbank scopet Kaufvertrag fuer hypothekenbelastetes Seeschiff: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. SchRG §§ 8-75; HGB §§ 596-601 Schiffsglaeubigerrechte. Output: Kaufvertrag-Review-Matrix und Closing-Conditions.

# Schiffshypothek – Kaufvertrag scopen

## Mandantenfall
Ein Investor kauft ein hypothekenbelastetes Seeschiff; Risiken aus Altlasten und Zertifikatsmängeln sind zu identifizieren. Ein Reeder veräußert ein hypothekenbelastetes Seeschiff unter Zeitdruck; Gewährleistungsausschlüsse sind zu prüfen. Eine Bank finanziert den Kauf und möchte Vertragsrisiken kennen.

## Erste Schritte
1. Kaufvertrag sichten: Kaufpreis, Zahlungsplan, Lieferbedingungen fuer hypothekenbelastetes Seeschiff.
2. Lastenuebergang pruefen: werden alle Hypotheken vor Eigentumsuebergang geloescht?
3. SchRG § 2 Eigentumsuebergang: erst Einigung und Eintragung; Zeitplan pruefen.
4. Zertifikatsstatus klaeren: Klasse; ISM; MLC; ISPS; Uebergabe oder Neuausstellung?
5. Gewaehrleistungsklauseln: BGB §§ 433-479 oder as-is-Ausschluss?
6. Escrow-Mechanismus fuer simultane Zahlung und Eigentumsuebergang aufsetzen.

## Rechtsrahmen
- SchRG §§ 8-75; HGB §§ 596-601 Schiffsglaeubigerrechte; BGB §§ 433-479 Kaufgewaehrleistung; SchRG § 2 Eigentumsuebergang; SchRegO. Rangfolge Hypotheken; Absonderung InsO §§ 49-51.

## Prüfraster
- Sind alle Hypotheken und Lasten vor Eigentumsuebergang abzuloesen?
- Enthaelt der Kaufvertrag eine umfassende Freistellungsklausel?
- Sind Zertifikate (Klasse/ISM/MLC) als Closing-Bedingungen definiert?
- Ist der Gewaehrleistungsausschluss rechtswirksam?
- Ist Escrow-Mechanismus fuer simultane Transaktion vorgesehen?

## Typische Fallstricke
- Kaeufer haftet mit hypothekenbelastetes Seeschiff fuer Altschulden bis zur Loeschung.
- Gewaehrleistungsausschluss (as-is) deckt keine versteckten Konstruktionsmaengel.
- Zertifikatslücke zwischen Closing und Neuausstellung gefaehrdet Betrieb.

## Output
Kaufvertrag-Review-Matrix und Closing-Conditions-Checkliste fuer hypothekenbelastetes Seeschiff.


## Vertiefung: Wesentliche Kaufvertragsklauseln im Schiffskauf
International dominieren MOA-Standardformulare (Norwegian Saleform 2012; Norwegian Saleform 1993; Nipponsale 1999). Für deutsche Seeschiffe mit HGB-Bezug gelten ergänzend die deutschen Kaufrechtsregeln (BGB §§ 433-479). Bei internationalem Schiffskauf empfiehlt sich die ausdrückliche Rechtswahl (z.B. englisches Recht) im Vertrag, um CISG-Anwendung zu vermeiden.

## Wesentliche Klauseln prüfen
- **Deposit Clause**: Anzahlung (typisch 10%) als Sicherheit; bei Closing verrechenbar; bei Buyer-Default einbehalten.
- **Delivery Condition**: clean class; no outstanding class recommendations; free of encumbrances.
- **Bunker Provision**: aktuelle Bunker werden zum Tagesmarktpreis übernommen; gemessen bei Übergabe.
- **Vessel Documents**: welche Originalzertifikate werden übergeben; welche müssen neu ausgestellt werden?
- **Governing Law and Arbitration**: English Law und LMAA-Schiedsverfahren London ist Marktstandard.

## Risiken und Gegenmaßnahmen
Wesentliche Risiken beim Schiffskauf: Verborgene Hypotheken; ausstehende Klassemängelempfehlungen; unbekannte Schiffsgläubigerrechte; laufende PSC-Banning; auslaufende ISM-/MLC-Zertifikate. Gegenmaßnahmen: umfassende Freistellungsklausel; Kaufpreiseinbehalt als Escrow; Closing-Conditions präzise definieren.


## Checkliste Kaufvertrag-Prüfung
- [ ] Kaufvertrag vollständig vorliegend (Hauptvertrag; Anhänge; Spezifikationen)
- [ ] Kaufpreis und Zahlungsmodalitäten klar geregelt
- [ ] Closing-Bedingungen (Delivery Conditions) präzise definiert
- [ ] Lastenfreistellungsklausel des Verkäufers vollständig
- [ ] Escrow-Mechanismus für simultane Zahlung und Eigentumsübergang geregelt
- [ ] Gewährleistung (BGB §§ 433-479) oder Ausschluss (as-is) klar vereinbart
- [ ] Zertifikate (Klasse; ISM; MLC; ISPS) als Closing-Conditions definiert
- [ ] Rücktrittsrechte und Vertragsstrafen bei Verzögerung geregelt
- [ ] Rechtswahl und Gerichtsstand/Schiedsklausel vereinbart

## Relevante Rechtsprechung
- BGH zur Gewährleistung beim Schiffskauf; arglistiges Verschweigen von Mängeln.
- BGH zur Wirksamkeit von as-is-Klauseln in Kaufverträgen; Grenzen des Haftungsausschlusses.
- LG Hamburg zu Closing-Bedingungen bei Schiffskäufen; Auslegung von Saleform-Vertragsklauseln.

## Normen im Überblick
- BGB § 433: Kaufvertrag; Pflichten des Verkäufers.
- BGB §§ 434-442: Sachmangel; Rechtsmangel; Haftungsausschluss.
- BGB §§ 437-441: Mängelrechte des Käufers; Nacherfüllung; Rücktritt; Minderung.
- SchRG § 2: Eigentumsübergang nur durch Einigung und Eintragung; nicht durch Kaufvertrag allein.
- SchRG § 19: Löschung der Hypothek durch Löschungsbewilligung des Gläubigers.
- HGB §§ 480-482: Schiffslieferung im Kontext des Handelsrechts.

## Quellen
- SchRG § 2: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- BGB §§ 433-479: https://dejure.org/gesetze/BGB/433.html
- HGB §§ 480 ff.: https://dejure.org/gesetze/HGB/480.html
- openjur Schiffskaufstreit: https://www.openjur.de

## 3. `see-033-schiffbauwerk-kaufvertrag-scopen`

**Fokus:** Schiffbauwerk: Werft; Auftraggeber-Reeder; finanzierende Bank scopet Kaufvertrag fuer Schiff im Bau (Schiffbauwerk): Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. SchRG §§ 76-104 Schiffbauwerkshypothek; BGB §§ 631-651 Werkvertrag. Output: Kaufvertrag-Review-Matrix und Closing-Conditions.

# Schiffbauwerk – Kaufvertrag scopen

## Mandantenfall
Ein Investor kauft ein Schiff im Bau (Schiffbauwerk); Risiken aus Altlasten und Zertifikatsmängeln sind zu identifizieren. Ein Reeder veräußert ein Schiff im Bau (Schiffbauwerk) unter Zeitdruck; Gewährleistungsausschlüsse sind zu prüfen. Eine Bank finanziert den Kauf und möchte Vertragsrisiken kennen.

## Erste Schritte
1. Kaufvertrag sichten: Kaufpreis, Zahlungsplan, Lieferbedingungen fuer Schiff im Bau (Schiffbauwerk).
2. Lastenuebergang pruefen: werden alle Hypotheken vor Eigentumsuebergang geloescht?
3. SchRG § 2 Eigentumsuebergang: erst Einigung und Eintragung; Zeitplan pruefen.
4. Zertifikatsstatus klaeren: Klasse; ISM; MLC; ISPS; Uebergabe oder Neuausstellung?
5. Gewaehrleistungsklauseln: BGB §§ 433-479 oder as-is-Ausschluss?
6. Escrow-Mechanismus fuer simultane Zahlung und Eigentumsuebergang aufsetzen.

## Rechtsrahmen
- SchRG §§ 76-104 Schiffbauwerkshypothek; BGB §§ 631-651 Werkvertrag; BGB §§ 433-479 Kaufgewaehrleistung; SchRG § 2 Eigentumsuebergang; SchRegO. Baufortschritt; Refund Guarantee; Bauabnahme.

## Prüfraster
- Sind alle Hypotheken und Lasten vor Eigentumsuebergang abzuloesen?
- Enthaelt der Kaufvertrag eine umfassende Freistellungsklausel?
- Sind Zertifikate (Klasse/ISM/MLC) als Closing-Bedingungen definiert?
- Ist der Gewaehrleistungsausschluss rechtswirksam?
- Ist Escrow-Mechanismus fuer simultane Transaktion vorgesehen?

## Typische Fallstricke
- Kaeufer haftet mit Schiff im Bau (Schiffbauwerk) fuer Altschulden bis zur Loeschung.
- Gewaehrleistungsausschluss (as-is) deckt keine versteckten Konstruktionsmaengel.
- Zertifikatslücke zwischen Closing und Neuausstellung gefaehrdet Betrieb.

## Output
Kaufvertrag-Review-Matrix und Closing-Conditions-Checkliste fuer Schiff im Bau (Schiffbauwerk).


## Vertiefung: Wesentliche Kaufvertragsklauseln im Schiffskauf
International dominieren MOA-Standardformulare (Norwegian Saleform 2012; Norwegian Saleform 1993; Nipponsale 1999). Für deutsche Seeschiffe mit HGB-Bezug gelten ergänzend die deutschen Kaufrechtsregeln (BGB §§ 433-479). Bei internationalem Schiffskauf empfiehlt sich die ausdrückliche Rechtswahl (z.B. englisches Recht) im Vertrag, um CISG-Anwendung zu vermeiden.

## Wesentliche Klauseln prüfen
- **Deposit Clause**: Anzahlung (typisch 10%) als Sicherheit; bei Closing verrechenbar; bei Buyer-Default einbehalten.
- **Delivery Condition**: clean class; no outstanding class recommendations; free of encumbrances.
- **Bunker Provision**: aktuelle Bunker werden zum Tagesmarktpreis übernommen; gemessen bei Übergabe.
- **Vessel Documents**: welche Originalzertifikate werden übergeben; welche müssen neu ausgestellt werden?
- **Governing Law and Arbitration**: English Law und LMAA-Schiedsverfahren London ist Marktstandard.

## Risiken und Gegenmaßnahmen
Wesentliche Risiken beim Schiffskauf: Verborgene Hypotheken; ausstehende Klassemängelempfehlungen; unbekannte Schiffsgläubigerrechte; laufende PSC-Banning; auslaufende ISM-/MLC-Zertifikate. Gegenmaßnahmen: umfassende Freistellungsklausel; Kaufpreiseinbehalt als Escrow; Closing-Conditions präzise definieren.


## Checkliste Kaufvertrag-Prüfung
- [ ] Kaufvertrag vollständig vorliegend (Hauptvertrag; Anhänge; Spezifikationen)
- [ ] Kaufpreis und Zahlungsmodalitäten klar geregelt
- [ ] Closing-Bedingungen (Delivery Conditions) präzise definiert
- [ ] Lastenfreistellungsklausel des Verkäufers vollständig
- [ ] Escrow-Mechanismus für simultane Zahlung und Eigentumsübergang geregelt
- [ ] Gewährleistung (BGB §§ 433-479) oder Ausschluss (as-is) klar vereinbart
- [ ] Zertifikate (Klasse; ISM; MLC; ISPS) als Closing-Conditions definiert
- [ ] Rücktrittsrechte und Vertragsstrafen bei Verzögerung geregelt
- [ ] Rechtswahl und Gerichtsstand/Schiedsklausel vereinbart

## Relevante Rechtsprechung
- BGH zur Gewährleistung beim Schiffskauf; arglistiges Verschweigen von Mängeln.
- BGH zur Wirksamkeit von as-is-Klauseln in Kaufverträgen; Grenzen des Haftungsausschlusses.
- LG Hamburg zu Closing-Bedingungen bei Schiffskäufen; Auslegung von Saleform-Vertragsklauseln.

## Normen im Überblick
- BGB § 433: Kaufvertrag; Pflichten des Verkäufers.
- BGB §§ 434-442: Sachmangel; Rechtsmangel; Haftungsausschluss.
- BGB §§ 437-441: Mängelrechte des Käufers; Nacherfüllung; Rücktritt; Minderung.
- SchRG § 2: Eigentumsübergang nur durch Einigung und Eintragung; nicht durch Kaufvertrag allein.
- SchRG § 19: Löschung der Hypothek durch Löschungsbewilligung des Gläubigers.
- HGB §§ 480-482: Schiffslieferung im Kontext des Handelsrechts.

## Quellen
- SchRG § 2: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- BGB §§ 433-479: https://dejure.org/gesetze/BGB/433.html
- HGB §§ 480 ff.: https://dejure.org/gesetze/HGB/480.html
- openjur Schiffskaufstreit: https://www.openjur.de

## 4. `see-041-werftvertrag-register-pruefen`

**Fokus:** Werftvertrag: Reeder oder Werft; Streit um Lieferung; Preisanpassung; Maengel prueft Schiffbauwerksregister ab Kiellegung auf Eigentumsstand, Hypotheken, Arreste und gesetzliche Vorrechte. BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104; CISG wenn nicht ausgeschlossen. Klaert Lastenfreiheit vor Closing oder Kreditvergabe. Output: Registerpruefprotokoll und Rangkarte.

# Werftvertrag – Registerprüfung

## Mandantenfall
Eine finanzierende Bank prueft den Schiffbauwerksregister ab Kiellegung vor Auszahlung eines Kredits fuer ein Neubauprojekt unter Werftvertrag. Ein Investor will Eigentuemerstellung und Lastenfreiheit bestaetigt haben. Ein Insolvenzverwalter erstellt die Glaeubigerliste fuer die Masse.

## Erste Schritte
1. Aktuellen Registerauszug (Schiffbauwerksregister ab Kiellegung) beim zustaendigen Gericht beschaffen.
2. Eigentuemerstellung (Abt. I) pruefen; Verkaeufereigenschaft bestaetigen.
3. Hypothekenabteilung (Abt. II): Betrag, Rang, Glaeubiger und Faelligkeit.
4. Gesetzliche Vorrechte identifizieren (HGB §§ 596-601 oder BinSchG §§ 102-116).
5. Arrest- und Pfaendungsvermerke sichten; Zeitpunkt der Eintragung beachten.
6. Registerpruefprotokoll erstellen; Rangkarte und Risikoampel ausgeben.

## Rechtsrahmen
- BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104; CISG wenn nicht ausgeschlossen; SchRegO §§ 3-19 Registerführung; BGB §§ 892-893 Gutglaubensschutz im Register. Liquidated Damages; Force Majeure; Klasse-Abnahme SAJ/AWES-Muster.

## Prüfraster
- Stimmt eingetragener Eigentümer mit dem Verkäufer des Neubauprojekt unter Werftvertrags überein?
- Sind alle Hypotheken mit aktuellem Valutierungsstand bei Gläubigern abgeglichen?
- Bestehen gesetzliche Vorrechte, die Hypotheken im Rang verdrängen?
- Gibt es Arrest- oder Pfändungsvermerke im Register?
- Sind Löschungsvoraussetzungen für alle Altlasten erfüllt?

## Typische Fallstricke
- Gesetzliche Vorrechte (Crew-Löhne, Hafengebühren) entstehen ohne Registereintragung.
- Voreintragungspflicht: Veräußerer muss im Schiffbauwerksregister ab Kiellegung eingetragen sein.
- Bei Neubauprojekt unter Werftvertrag unter Auslandsflagge gilt Lex registri des Flaggenstaats.

## Output
Registerprüfprotokoll mit Abteilungsübersicht und Rangkarte für Neubauprojekt unter Werftvertrag.


## Vertiefung: Registerrechtliche Besonderheiten
Das Schiffsregister ist ein öffentliches Register im Sinne des SchRG § 3; es gilt das Prinzip der positiven und negativen Publizität (BGB §§ 892-893 analog). Ein gutgläubiger Erwerber kann sich auf den Registerinhalt verlassen, soweit keine Eintragungsvoraussetzungen fehlen. Bei internationalen Transaktionen ist die Anerkennung ausländischer Schiffshypotheken nach dem Recht des Registerstaats (Lex registri) zu prüfen; dies gilt insbesondere für Schiffe unter Panama-, Marshall-Islands- oder Liberia-Flagge.

## Verfahrensablauf Registerprüfung
Die Registerprüfung erfolgt in drei Phasen:
1. **Formelle Prüfung**: Ist das Schiff eingetragen; ist die Eintragungsnummer korrekt; liegt das Schiffsregisterblatt vollständig vor?
2. **Materielle Prüfung**: Inhalt der Abteilungen I bis III; Rangfolge der Einträge; Zeitstempel.
3. **Risikoanalyse**: Bewertung der Restrisiken; gesetzliche Schiffsgläubigerrechte die außerhalb des Registers entstehen; Fristen für Löschungsanträge.

## Praktische Hinweise
Registerauszüge sind nur tagesaktuell belastbar; kurzfristige Nachtragsanfragen sicherstellen. Bei komplexen Portfolien ist ein automatisiertes Monitoring sinnvoll. Die Kosten für den Registerauszug betragen je nach Registergericht wenige Euro; Notargebühren für beglaubigte Ausfertigungen fallen zusätzlich an.


## Checkliste Registerprüfung
- [ ] Registerauszug Abteilung I: Schiffsname; IMO-Nummer; Flagge; Eigentümer; Datum der Eintragung
- [ ] Registerauszug Abteilung II: alle Hypotheken; Rangstellen; Gläubiger; Nennbeträge; Eintragungsdaten
- [ ] Registerauszug Abteilung III: Arreste; Pfändungen; sonstige Verfügungsbeschränkungen
- [ ] Gesetzliche Schiffsgläubigerrechte (HGB §§ 596-601) abgefragt: Crew-Löhne; Hafengebühren; Bergungskosten
- [ ] Valutierungsauszüge aller Hypothekengläubiger vorliegend
- [ ] Löschungsbewilligungen für alle abzulösenden Lasten gesichert
- [ ] Negativattest: keine weiteren Lasten oder Verfügungsbeschränkungen bekannt

## Relevante Rechtsprechung
- BGH zur Rangfolge von Schiffsgläubigerrechten und Hypotheken; Absonderung in der Insolvenz des Reeders.
- ITLOS M/V Saiga Case No. 2 (Saint Vincent and the Grenadines v. Guinea 1999): Flaggenstaat-Verantwortung; genuine link UNCLOS Art. 91.
- Landgericht Hamburg; Beschlüsse zu Schiffsarrest und Registervormerkung; abrufbar über openjur.de.

## Normen im Überblick
- SchRG §§ 1-7: Anwendungsbereich; Eintragungsfähigkeit; Definition Schiff.
- SchRG §§ 8-30: Schiffshypothek; Entstehung; Bestellung; Übertragung.
- SchRG §§ 31-58: Inhalt; Umfang; Erstreckung auf Zubehör und Forderungen.
- SchRG §§ 59-74: Rang und Konkurrenz mehrerer Hypotheken.
- SchRG § 75: Höchstbetragshypothek.
- SchRG §§ 76-104: Schiffbauwerkshypothek.
- HGB §§ 596-601: gesetzliche Schiffsgläubigerrechte mit gesetzlichem Pfandrecht.


## Vertiefung Registerrecht

### Schiffsregister und Grundbuchrecht im Vergleich
Das Schiffsregister folgt dem Grundbuchrecht (BGB §§ 873; 925) mit schiffsspezifischen Modifikationen durch das SchRG. Die Eintragung ist konstitutiv für die Entstehung von Schiffshypotheken. Gutgläubiger Erwerb ist möglich, wenn der Erwerber auf den Registerinhalt vertraut (SchRG § 3). Die öffentliche Urkunde (Registerauszug) gilt als Beweis für den eingetragenen Inhalt.

### Internationaler Bezug
Ausländische Schiffsregisterauszüge sind im deutschen Rechtsverkehr anerkannt, wenn sie von der zuständigen Auslandsbehörde ausgestellt und beglaubigt sind. Bei Flaggenwechsel ist die Löschung im alten Register und Neueintragung im neuen Register erforderlich (FlaggRG § 9).

## Normen-Synopse Register
| Norm | Inhalt |
|------|--------|
| SchRG § 1 | Eintragungsfähige Schiffe |
| SchRG § 8 | Entstehung der Hypothek |
| SchRegO § 8 | Eintragungsverfahren |
| HGB § 596 | Gesetzliche Vorrechte |

## Quellen
- SchRG: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- HGB §§ 596-601: https://dejure.org/gesetze/HGB/596.html
- BSH Register: https://www.bsh.de/DE/THEMEN/Schifffahrt/Schiffsregister/schiffsregister_node.html
- SchRegO: https://dejure.org/gesetze/SchRegO

## 5. `see-042-werftvertrag-hypothek-bestellen`

**Fokus:** Werftvertrag: Reeder oder Werft; Streit um Lieferung; Preisanpassung; Maengel bestellt Schiffshypothek als Sicherheit fuer Finanzierung eines Neubauprojekt unter Werftvertrag. BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104; CISG wenn nicht ausgeschlossen. Notarielle Bestellungsurkunde, Rangstelle, Sicherungsabrede, Zubehoer-Mithaftung (SchRG § 31). Output: Bestellungs-Checkliste.

# Werftvertrag – Schiffshypothek bestellen

## Mandantenfall
Eine Bank bestellt eine Hypothek auf ein Neubauprojekt unter Werftvertrag als Sicherheit fuer einen Schiffskredit. Ein Reeder sucht Zwischenfinanzierung und bietet sein Neubauprojekt unter Werftvertrag als Sicherheit an. Eine Bestandshypothek soll auf eine neue Kredittranche erstreckt werden.

## Erste Schritte
1. Eintragungsfaehigkeit des Neubauprojekt unter Werftvertrags pruefen; Eintragung im Schiffbauwerksregister ab Kiellegung bestaetigen.
2. Sicherungsabrede aufsetzen: gesicherte Forderungen, Kuendigungsrechte, Cross-Default.
3. Notarielle Hypothekenbestellungsurkunde nach SchRG §§ 8-18 erstellen.
4. Vertretungsbefugnis des Eigentuemers pruefen; ggf. Handelsregisterauszug.
5. Eintragungsantrag beim {reg_type}-Gericht stellen; Rangstelle fruehzeitig reservieren.
6. Eintragungsbestaetigung und ggf. Hypothekenbrief sichern; Sicherungsvertrag archivieren.

## Rechtsrahmen
- BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104; CISG wenn nicht ausgeschlossen; SchRG § 31 Zubehoer-Mithaftung; SchRG § 75 Hoechstbetragshypothek; SchRegO §§ 13-19. Liquidated Damages; Force Majeure; Klasse-Abnahme SAJ/AWES-Muster.

## Prüfraster
- Ist das Neubauprojekt unter Werftvertrag im Schiffbauwerksregister ab Kiellegung eingetragen und eintragungsfaehig?
- Ist die Sicherungsabrede vollstaendig und rechtswirksam?
- Ist Zubehoer-Mithaftung (SchRG § 31) vertraglich gesichert?
- Ist die notarielle Form eingehalten (SchRG § 17)?
- Ist der Rangstellen-Antrag fruehzeitig gestellt?

## Typische Fallstricke
- Fehlende notarielle Form fuehrt zur Nichtigkeit der Hypothek (SchRG § 17).
- Rang entsteht mit Antragstellung; fruehzeitig beim Schiffbauwerksregister ab Kiellegung-Gericht stellen.
- Briefhypothek verliert Vollstreckungswert bei Verlust des Hypothekenbriefs.

## Output
Checkliste Hypothekenbestellung und Unterlagen-Übersicht für Neubauprojekt unter Werftvertrag.


## Vertiefung: Hypothekenarten im deutschen Schiffsrecht
Das SchRG kennt die Verkehrshypothek (§§ 8-30) und die Höchstbetragshypothek (§ 75). Die Verkehrshypothek ist an eine bestimmte Forderung gebunden; die Höchstbetragshypothek sichert variable Forderungen bis zu einem eingetragenen Maximalbetrag und eignet sich für revolvierende Kreditlinien. In der Praxis der Schiffsfinanzierung dominiert die Hypothekenbestellung als erstrangige Höchstbetragshypothek zugunsten der Konsortialführerbank.

## Verfahrensablauf Hypothekenbestellung
1. **Vor der Bestellung**: Eintragungsfähigkeit prüfen; Rangstelle reservieren (SchRegO § 13); Sicherungsabrede verhandeln.
2. **Bestellung**: Notarielle Bestellungsurkunde; Unterschriften des Eigentümers; Vollmachten (ggf. notariell beglaubigt).
3. **Eintragung**: Antrag beim Registergericht; Vorlage der Bestellungsurkunde; Eintragungsgebühr.
4. **Nach der Eintragung**: Registerauszug beschaffen; Sicherungsvertrag und Registerauszug archivieren; Mortgagee's Interest Insurance prüfen.

## Praktische Hinweise
In Konsortialkrediten hält eine Sicherheitentreuhänderin (Security Trustee) die Hypothek für alle Konsortialmitglieder. Die Hypothek kann jederzeit abgetreten werden (SchRG §§ 35-58); für die Abtretung ist Briefübergabe oder Eintragung erforderlich je nach Hypothekenart.


## Checkliste Hypothekenbestellung
- [ ] Eintragungsfähigkeit des Schiffes bestätigt (SchRG § 1)
- [ ] Eigentümer mit Vollmacht zur Hypothekenbestellung legitimiert
- [ ] Sicherungsabrede (Security Agreement / Credit Agreement) unterzeichnet
- [ ] Notarielle Hypothekenbestellungsurkunde erstellt und unterzeichnet
- [ ] Eintragungsantrag beim Registergericht gestellt; Rangstelle reserviert
- [ ] Mithaftung des Zubehörs (SchRG § 31) vertraglich vereinbart
- [ ] Eintragungsbestätigung und ggf. Hypothekenbrief gesichert
- [ ] Mortgagee's Interest Insurance (MII) beantragt

## Relevante Rechtsprechung
- BGH zur Wirksamkeit der notariellen Hypothekenbestellungsurkunde; Formerfordernisse SchRG § 17.
- BGH zur Mithaftung des Zubehörs nach SchRG § 31; Abgrenzung Schiffszubehör von persönlichem Eigentum des Kapitäns.
- OLG Hamburg zur Rangfolge bei gleichzeitig beantragten Hypotheken; Zeitpunkt der Antragstellung maßgeblich.

## Normen im Überblick
- SchRG § 8: Begründung der Schiffshypothek durch Einigung und Eintragung.
- SchRG §§ 9-14: Inhalt der Eintragungsurkunde; Form; Unterschriften.
- SchRG §§ 15-18: Eintragungsvoraussetzungen; notarielle Form.
- SchRG §§ 35-58: Übertragung der Hypothek; Abtretung; Pfändung.
- SchRG § 59: Rangfolge; ältere Hypothek geht jüngerer vor.
- SchRG § 75: Höchstbetragshypothek für revolvierende Kredite.
- InsO § 49: Absonderungsrecht des Hypothekengläubigers in der Insolvenz des Reeders.

## Quellen
- SchRG §§ 8-18: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- SchRegO §§ 13-19: https://dejure.org/gesetze/SchRegO
- BSH: https://www.bsh.de/DE/THEMEN/Schifffahrt/Schiffsregister/schiffsregister_node.html
- dejure SchRG § 75: https://dejure.org/gesetze/SchRG/75.html
