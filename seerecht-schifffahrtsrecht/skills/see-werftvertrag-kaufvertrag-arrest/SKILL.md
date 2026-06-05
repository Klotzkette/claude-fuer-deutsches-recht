---
name: see-werftvertrag-kaufvertrag-arrest
description: "SEE Werftvertrag Kaufvertrag Arrest: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# SEE Werftvertrag Kaufvertrag Arrest

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **SEE Werftvertrag Kaufvertrag Arrest** im Plugin Seerecht Schifffahrtsrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `see-043-werftvertrag-kaufvertrag-scopen` | Werftvertrag: Reeder oder Werft; Streit um Lieferung; Preisanpassung; Maengel scopet Kaufvertrag fuer Neubauprojekt unter Werftvertrag: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104; CISG wenn nicht ausgeschlossen. Output: Kaufvertrag-Review-Matrix und Closing-Conditions. |
| `see-044-werftvertrag-arrest-vorbereiten` | Werftvertrag: Glaeubiger sichert Anspruch an Neubauprojekt unter Werftvertrag durch dinglichen Arrest (ZPO §§ 916-945); Registervermerk (SchRegO § 67); Vollziehungsfrist 1 Monat. ISAC 1952 Seeforderungen; P&I Letter of Undertaking als Alternative. Output: Arrestantrags-Baustein und Vollziehungs-Zeitplan. |
| `see-045-werftvertrag-wrackpflicht-pruefen` | Werftvertrag: Reeder oder Werft; Streit um Lieferung; Preisanpassung; Maengel analysiert Wrackbeseitigungspflicht nach WRC 2007 / WSG §§ 1-12 fuer gesunkenes Neubauprojekt unter Werftvertrag. Versicherungspflicht ab 300 BRZ; Behoerdenkoordination; Haftungsfolge. BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104; CISG wenn nicht ausgeschlossen. Output: WRC-Pflichtenanalyse und Kostenrisiko-Vermerk. |
| `see-046-werftvertrag-versicherung-melden` | Werftvertrag: Schadensereignis an Neubauprojekt unter Werftvertrag melden: P&I-Club-Meldepflicht; H&M-Police-Meldung; Mortgagee Interest Insurance (MII) aktivieren. VVG §§ 28-30 Obliegenheiten; DTV-Klauseln Kasko; IGP&I Club Rules. Output: Meldecheckliste und Fristenuebersicht. |
| `see-047-werftvertrag-local-counsel-instruieren` | Werftvertrag: Auslaendischen Anwalt fuer Arrest; Vollstreckung oder Registerfragen bei Neubauprojekt unter Werftvertrag im Ausland instruieren. ISAC 1952; EuGVVO 2012; lokales Seepfandrecht; P&I-Korrespondenten. Output: Local-Counsel-Briefing und Prioritaetenliste. |

## Arbeitsweg

Im Plugin Seerecht Schifffahrtsrecht gilt für **SEE Werftvertrag Kaufvertrag Arrest**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `see-043-werftvertrag-kaufvertrag-scopen`

**Fokus:** Werftvertrag: Reeder oder Werft; Streit um Lieferung; Preisanpassung; Maengel scopet Kaufvertrag fuer Neubauprojekt unter Werftvertrag: Gewaehrleistung; Lastenfreistellung; Eigentumsuebergang (SchRG § 2); Zertifikatsstatus; Escrow-Mechanismus. BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104; CISG wenn nicht ausgeschlossen. Output: Kaufvertrag-Review-Matrix und Closing-Conditions.

# Werftvertrag – Kaufvertrag scopen

## Mandantenfall
Ein Investor kauft ein Neubauprojekt unter Werftvertrag; Risiken aus Altlasten und Zertifikatsmängeln sind zu identifizieren. Ein Reeder veräußert ein Neubauprojekt unter Werftvertrag unter Zeitdruck; Gewährleistungsausschlüsse sind zu prüfen. Eine Bank finanziert den Kauf und möchte Vertragsrisiken kennen.

## Erste Schritte
1. Kaufvertrag sichten: Kaufpreis, Zahlungsplan, Lieferbedingungen fuer Neubauprojekt unter Werftvertrag.
2. Lastenuebergang pruefen: werden alle Hypotheken vor Eigentumsuebergang geloescht?
3. SchRG § 2 Eigentumsuebergang: erst Einigung und Eintragung; Zeitplan pruefen.
4. Zertifikatsstatus klaeren: Klasse; ISM; MLC; ISPS; Uebergabe oder Neuausstellung?
5. Gewaehrleistungsklauseln: BGB §§ 433-479 oder as-is-Ausschluss?
6. Escrow-Mechanismus fuer simultane Zahlung und Eigentumsuebergang aufsetzen.

## Rechtsrahmen
- BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104; CISG wenn nicht ausgeschlossen; BGB §§ 433-479 Kaufgewaehrleistung; SchRG § 2 Eigentumsuebergang; SchRegO. Liquidated Damages; Force Majeure; Klasse-Abnahme SAJ/AWES-Muster.

## Prüfraster
- Sind alle Hypotheken und Lasten vor Eigentumsuebergang abzuloesen?
- Enthaelt der Kaufvertrag eine umfassende Freistellungsklausel?
- Sind Zertifikate (Klasse/ISM/MLC) als Closing-Bedingungen definiert?
- Ist der Gewaehrleistungsausschluss rechtswirksam?
- Ist Escrow-Mechanismus fuer simultane Transaktion vorgesehen?

## Typische Fallstricke
- Kaeufer haftet mit Neubauprojekt unter Werftvertrag fuer Altschulden bis zur Loeschung.
- Gewaehrleistungsausschluss (as-is) deckt keine versteckten Konstruktionsmaengel.
- Zertifikatslücke zwischen Closing und Neuausstellung gefaehrdet Betrieb.

## Output
Kaufvertrag-Review-Matrix und Closing-Conditions-Checkliste fuer Neubauprojekt unter Werftvertrag.


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

## 2. `see-044-werftvertrag-arrest-vorbereiten`

**Fokus:** Werftvertrag: Glaeubiger sichert Anspruch an Neubauprojekt unter Werftvertrag durch dinglichen Arrest (ZPO §§ 916-945); Registervermerk (SchRegO § 67); Vollziehungsfrist 1 Monat. ISAC 1952 Seeforderungen; P&I Letter of Undertaking als Alternative. Output: Arrestantrags-Baustein und Vollziehungs-Zeitplan.

# Werftvertrag – Arrest vorbereiten

## Mandantenfall
Ein Hypothekengläubiger will ein Neubauprojekt unter Werftvertrag arrestieren; Kredit ist ausgefallen. Ein Konnossementsinhaber hat Schadensansprüche und arretiert das Neubauprojekt unter Werftvertrag im Hafen. Ein Bergungsunternehmen sichert seinen Bergungslohnanspruch durch Arrest.

## Erste Schritte
1. Seeforderung nach ISAC 1952 Art. 1 gegenueber Eigentuemer des Neubauprojekt unter Werftvertrag konkretisieren.
2. Arrestgrund glaublhaft machen: {vessel} wird Hafen verlassen; Reeder insolvent.
3. LG am Liegeplatz (ZPO § 919) als zustaendiges Gericht bestimmen.
4. Arrestbeschluss beantragen; ohne Anhoerung des Gegners moeglich.
5. Vollziehung: Eintragung im Register (SchRegO § 67) binnen einem Monat.
6. Freigabestrategie: LOU des P&I-Clubs oder Barzahlung als Alternative vorbereiten.

## Rechtsrahmen
- ZPO §§ 916-945 Arrest; ZPO § 929 Vollziehungsfrist; SchRegO § 67; ISAC 1952 Art. 1.

## Prüfraster
- Ist die Forderung eine Seeforderung nach ISAC 1952 Art. 1?
- Liegt das Neubauprojekt unter Werftvertrag im Hafen und kann es noch abgefangen werden?
- Ist der Arrestgrund (Fluchtgefahr) konkret dargelegt?
- Ist die Vollziehungsfrist von 1 Monat realistisch einzuhalten?
- Besteht Risiko des ZPO § 945-Schadensersatzes bei unberechtigtem Arrest?

## Typische Fallstricke
- Arrest ohne Registereintragung (SchRegO § 67) ist wirkungslos.
- LOU des P&I-Clubs beendet Arrest, nicht die Forderung; Klage geht weiter.
- ZPO § 945-Schadensersatz bei unberechtigtem Arrest kann erheblich sein.

## Output
Arrestantrags-Baustein (ZPO § 920) und Vollziehungs-Zeitplan für Neubauprojekt unter Werftvertrag.


## Vertiefung: Internationale Seearrestpraxis
International koordinieren sich Gläubiger häufig über die 1952 Brüsseler Seearrest-Konvention (ISAC 1952) und über P&I-Club-Korrespondenten. In der EU gilt ergänzend die EuGVVO 2012 (Brüssel Ia-VO) für Vollstreckung und gegenseitige Anerkennung von Arrestbeschlüssen. In Drittstaaten gelten nationaler Seearrest-Regeln; Koordination mit Local Counsel ist unverzichtbar.

## Seeforderungen nach ISAC 1952 Art. 1
Zum Arrest berechtigende Seeforderungen umfassen: Schiffsbau- und -reparaturkosten; Schiffsausrüstung; Schifffahrtsabgaben; Frachtzahlungen; Charterzahlungen; Bergungskosten; Schiffsgläubigerrechte; Konnossementsansprüche; Kollisionshaftung; Hypothekenansprüche. Nicht erfasst sind Ansprüche aus reinem Landtransport ohne Seebezug.

## Verteidigungsstrategien des Schiffseigentümers
- **Letter of Undertaking (LOU)**: P&I-Club stellt ein formelles Versprechen aus das Schiff zu stellen; Arrest wird aufgehoben; Rechtsstreit geht weiter.
- **Gegenklage nach § 945 ZPO**: bei unberechtigtem Arrest; Schadensersatz für Liegekosten; entgangene Fracht; Reparaturkosten.
- **Sofortige Sicherheitsleistung**: Zahlung unter Vorbehalt; Bankbürgschaft; Schuldschein.


## Checkliste Arrest-Vorbereitung
- [ ] Seeforderung nach ISAC 1952 Art. 1 identifiziert und dokumentiert
- [ ] Schiff im Hafen bestätigt; Liegeplatz ermittelt
- [ ] Zuständiges Gericht bestimmt (LG am Liegeplatz; ZPO § 919)
- [ ] Arrestanspruch und Arrestgrund glaubhaft gemacht (Eidesstattliche Versicherung)
- [ ] Arrestantrag (ZPO § 920) vollständig vorbereitet
- [ ] Vollziehungsstrategie: Registereintragung (SchRegO § 67) plus physische Bewachung
- [ ] Freigabe-Optionen identifiziert: LOU des P&I-Clubs; Bankbürgschaft
- [ ] § 945-Schadensersatzrisiko bewertet

## Relevante Rechtsprechung
- LG Hamburg; OLG Hamburg zu Seearrest; Anforderungen an Arrestanspruch und -grund.
- BGH zur Haftung aus ungerechtfertigtem Arrest nach ZPO § 945.
- ITLOS Juno Trader Case No. 13 (Saint Vincent v. Guinea-Bissau 2004): Prompt Release; Verhältnismäßigkeit der Sicherheitsleistung.

## Normen im Überblick
- ZPO § 916: dinglicher Arrest; Voraussetzungen; Arrestanspruch; Arrestgrund.
- ZPO §§ 917-919: besondere Arrestgründe; örtliche Zuständigkeit (Liegeplatz).
- ZPO § 920: Arrestantrag; Form; Glaubhaftmachung.
- ZPO § 929: Vollziehungsfrist 1 Monat; Wirkungsverlust bei Nichtvollziehung.
- ZPO § 945: Schadensersatz bei unberechtigtem oder wirkungslos gewordenem Arrest.
- SchRegO § 67: Eintragung von Pfändungs- und Arrestvermerken im Schiffsregister.
- ISAC 1952 Art. 1-8: Seeforderungen; Arrest an Schwesterschiffen; Verfahren.


## Vertiefung Arrest

### Seeforderungen und ISAC 1952
Das ISAC 1952 definiert abschließend, für welche Forderungen ein Schiffsarrest zulässig ist (Art. 1). Deutschland ist Vertragsstaat; die meisten EU-Häfen ebenfalls. Im Nicht-Vertragsstaat gilt nationales Recht; die Anforderungen können abweichen.

### Arrest vs. LOU des P&I-Clubs
In der Praxis wird der Arrest häufig durch eine Letter of Undertaking (LOU) des P&I-Clubs abgewandt. Die LOU ist ein abstraktes Schuldversprechen des Clubs; sie wird nur ausgestellt, wenn die zugrundeliegende Forderung club-covered ist.

## Normen-Synopse Arrest
| Norm | Inhalt |
|------|--------|
| ZPO § 916 | Dinglicher Arrest |
| ZPO § 920 | Arrestantrag |
| ZPO § 929 | Vollziehungsfrist |
| ZPO § 945 | Schadensersatz |
| ISAC 1952 Art. 1 | Seeforderungen |

## Quellen
- ZPO §§ 916-945: https://dejure.org/gesetze/ZPO/916.html
- SchRegO § 67: https://dejure.org/gesetze/SchRegO/67.html
- ISAC 1952: https://www.admin.ch/opc/de/classified-compilation/19520172/index.html
- openjur LG Hamburg Arrest: https://www.openjur.de

## 3. `see-045-werftvertrag-wrackpflicht-pruefen`

**Fokus:** Werftvertrag: Reeder oder Werft; Streit um Lieferung; Preisanpassung; Maengel analysiert Wrackbeseitigungspflicht nach WRC 2007 / WSG §§ 1-12 fuer gesunkenes Neubauprojekt unter Werftvertrag. Versicherungspflicht ab 300 BRZ; Behoerdenkoordination; Haftungsfolge. BGB §§ 631-651 Werkvertragsrecht; SchRG §§ 76-104; CISG wenn nicht ausgeschlossen. Output: WRC-Pflichtenanalyse und Kostenrisiko-Vermerk.

# Werftvertrag – Wrackbeseitigungspflicht prüfen

## Mandantenfall
Ein Neubauprojekt unter Werftvertrag sinkt in deutschen Gewässern; WSA ordnet Beseitigung an; Eigentümer fragt nach Haftung. Die finanzierende Bank fragt, ob sie als Hypothekengläubigerin haftet. Ein Reeder ist insolvent; Behörde will Kosten beim letzten Eigentümer eintreiben.

## Erste Schritte
1. WRC 2007 / WSG Anwendbarkeit pruefen: Neubauprojekt unter Werftvertrag ab 300 BRZ in deutschen Gewaessern.
2. Verantwortlichen identifizieren: WSG § 2 - Eigentuemer des {vessel} haftet primaer.
3. Behoerdliche Meldepflicht (WRC Art. 5 / WSG § 4): unverzuegliche Meldung beim WSA.
4. Versicherungsnachweis (WRC Art. 12): Pflicht ab 300 BRZ; P&I-Club-Zertifikat vorlegen.
5. Kostenschaetzung einholen: Bergungsunternehmen; Umweltschadensrisiko bewerten.
6. Notfallmassnahmen koordinieren: BSH-Schadstoffabwehr; Buenker-Oelbergung.

## Rechtsrahmen
- WSG §§ 1-12 Wrackbeseitigungsgesetz; WRC 2007 Nairobi Art. 1-12; MARPOL Annex I Reg. 26.

## Prüfraster
- Ist der Eigentuemer des Neubauprojekt unter Werftvertrag bekannt und zahlungsfaehig?
- Greift WRC 2007 (Schiff ab 300 BRZ; Gewaesser eines Vertragsstaats)?
- Ist Wrackbeseitigungs-Versicherung vorhanden (WRC Art. 12)?
- Ueberschreiten Wrackkosten den Schiffswert?
- Bestehen Umweltschadensrisiken (Bunkeröl/Chemikalien) beim Neubauprojekt unter Werftvertrag?

## Typische Fallstricke
- WRC gilt auch fuer Freizeitjachten ab 14 Meter Laenge.
- Behoerdliche Ersatzvornahme begründet Kostenerstattungsanspruch mit Vorrang.
- Bei Neubauprojekt unter Werftvertrag unter Auslandsflagge kommen Flaggenstaat-Pflichten hinzu.

## Output
WRC-Pflichtenanalyse und Kostenrisiko-Vermerk für Neubauprojekt unter Werftvertrag.


## Vertiefung: Nairobi WRC 2007 im Überblick
Das Nairobi Wrack-Übereinkommen (WRC 2007) trat international 2015 in Kraft; Deutschland hat es 2013 ratifiziert und durch das Wrackbeseitigungsgesetz (WSG) umgesetzt. Es gilt für Wracks in der AWZ und dem Küstenmeer von Vertragsstaaten; für Wracks auf der Hohen See gelten nur nationale Normen. Kernpflicht: Eigentümer muss das Wrack melden; markieren; und beseitigen oder beseitigen lassen.

## Haftungsstruktur
Primär haftet der eingetragene Eigentümer; sekundär können Hypothekengläubiger oder faktische Betreiber herangezogen werden. Die Haftung ist nicht automatisch durch Schiffswert begrenzt; das Haftungsbeschränkungsrecht nach HGB §§ 611-617 oder LLMC 1976/1996 kann aber Obergrenzen setzen. P&I-Clubs decken Wrackbeseitigungskosten typischerweise im Rahmen der Pollution-Deckung ab.

## Behördliche Zuständigkeit
In Deutschland ist das Wasserstraßen- und Schifffahrtsamt (WSA) die zuständige Behörde (§ 4 WSG). Bei Gefahr für Menschenleben oder Umwelt kann das WSA sofortige Maßnahmen anordnen und auf Kosten des Eigentümers durchführen. Das BSH koordiniert Schadstoffabwehrmaßnahmen auf See.


## Checkliste Wrackpflicht-Prüfung
- [ ] Lage des Wracks bestimmt: AWZ; Küstenmeer; Binnengewässer
- [ ] Anwendbarkeit WRC 2007 / WSG geprüft: Schiff ab 300 BRZ; Vertragsstaaten-Gewässer
- [ ] Eigentümer identifiziert; Kontakt aufgenommen
- [ ] Meldung beim WSA erfolgt (WSG § 4 / WRC Art. 5)
- [ ] Wrackbeseitigungs-Versicherungsnachweis angefordert (WRC Art. 12)
- [ ] Kostenschätzung für Bergung eingeholt
- [ ] Umweltgefährdung durch Bunkeröl oder Schadstoffe bewertet
- [ ] BSH Schadstoffabwehr informiert
- [ ] Haftungsstruktur analysiert: Eigentümer; Hypothekengläubiger; Versicherer

## Relevante Rechtsprechung
- BGH zur Ersatzvornahme bei Wrackbeseitigung; Kostenerstattungsanspruch der Behörde gegen Eigentümer.
- VG Hamburg und VG Stade zur Behördenzuständigkeit für Wrackbeseitigung in der AWZ.
- ITLOS Advisory Opinion No. 17 (Seabed Disputes Chamber 2011): Pflichten der Sponsoring States für Tätigkeiten im Meeresgebiet.

## Normen im Überblick
- WSG §§ 1-12: Wrackbeseitigungsgesetz; Pflichten des Eigentümers; Behördenzuständigkeit; Kosten.
- WRC 2007 Art. 1-16: Definitionen; Anwendungsbereich; Meldepflichten; Versicherungspflicht; Haftung.
- MARPOL Annex I Reg. 26: Bunkeröl-Sicherheitsmaßnahmen bei Schiffskatastrophen.
- HGB § 611: Haftungsbeschränkung des Schiffseigentümers nach LLMC 1976/1996.
- InsO §§ 49-51: Absonderungsrecht des Hypothekengläubigers; Haftungsfreistellung.


## Vertiefung Wrackbeseitigung

### Behördliche Struktur
In der AWZ ist das BSH (Bundesamt für Seeschifffahrt und Hydrographie) zuständig; im Küstenmeer und den Seewasserstraßen die WSA (Wasserstraßen- und Schifffahrtsämter). Die Zuständigkeit ist für die Einschätzung des Vollzugsrisikos entscheidend.

### Versicherungspflicht nach WRC 2007
Ab 300 BRZ besteht eine Pflichtversicherung für Wrackbeseitigungskosten (WRC Art. 12); der Nachweis muss an Bord mitgeführt werden. Deutschland hat das WRC 2007 ratifiziert (BGBl. 2013 II Nr. 22).

## Normen-Synopse Wrackbeseitigung
| Norm | Inhalt |
|------|--------|
| WSG § 1 | Anwendungsbereich |
| WSG § 4 | Meldepflicht |
| WRC Art. 12 | Versicherungspflicht |
| MARPOL Annex I | Bunkerölsicherheit |

## Quellen
- WSG: https://www.gesetze-im-internet.de/wsg/
- WRC 2007 IMO: https://www.imo.org/en/About/Conventions/Pages/Nairobi-International-Convention-on-the-Removal-of-Wrecks.aspx
- BSH: https://www.bsh.de
- MARPOL IMO: https://www.imo.org/en/About/Conventions/Pages/International-Convention-for-the-Prevention-of-Pollution-from-Ships-(MARPOL).aspx

## 4. `see-046-werftvertrag-versicherung-melden`

**Fokus:** Werftvertrag: Schadensereignis an Neubauprojekt unter Werftvertrag melden: P&I-Club-Meldepflicht; H&M-Police-Meldung; Mortgagee Interest Insurance (MII) aktivieren. VVG §§ 28-30 Obliegenheiten; DTV-Klauseln Kasko; IGP&I Club Rules. Output: Meldecheckliste und Fristenuebersicht.

# Werftvertrag – Schadensfall bei Versicherung melden

## Mandantenfall
Ein Neubauprojekt unter Werftvertrag erleidet Kollisionsschäden; P&I-Club und H&M-Versicherer werden koordiniert informiert. Ein Reeder verzögert die Schadensmeldung; Versicherer beruft sich auf VVG § 28 Obliegenheitsverletzung. Eine Bank aktiviert MII-Police nach Totalverlust eines hypothekenbelasteten Neubauprojekt unter Werftvertrag.

## Erste Schritte
1. P&I-Club sofort informieren; Korrespondenten vor Ort aktivieren.
2. H&M-Versicherer (Kasko) unverzueglich benachrichtigen; DTV-Fristen beachten.
3. MII-Police der Bank aktivieren, sofern Hypothekenglaeubigerbank betroffen.
4. Schadensdokumentation: Fotos; Sachverstaendige; Logbuecher; Klassenachricht sichern.
5. Schadensminderungspflicht (VVG § 82): Notmassnahmen veranlassen und dokumentieren.
6. Alle Beteiligten koordinieren: P&I; H&M; MII; Klassifikator; Versicherungsmakler.

## Rechtsrahmen
- VVG §§ 28-30 Obliegenheiten; VVG § 82 Schadensminderung; DTV-Klauseln Kasko 2009; IGP&I Club Rules.

## Prüfraster
- Ist Meldung fristgerecht an alle Versicherer erfolgt?
- Sind Schadensminderungsmassnahmen dokumentiert?
- Greift MII-Police der Bank; sind alle Voraussetzungen erfuellt?
- Liegt ein Deckungswiderspruch zwischen H&M und P&I vor?
- Ist der Klassifikator informiert; droht Klasse-Suspension?

## Typische Fallstricke
- Verspaetete P&I-Meldung fuehrt zu Deckungsverlust (Club Rule: prompt notification).
- MII greift nur wenn Bank nicht als Mitversicherter in H&M-Police steht.
- H&M deckt nur 3/4 der Kollisionshaftung; P&I nimmt 1/4.

## Output
Meldecheckliste (P&I/H&M/MII) und Fristenübersicht für Neubauprojekt unter Werftvertrag.


## Vertiefung: P&I-Club-Meldesystem
P&I-Clubs arbeiten nach dem Mutual-Insurance-Prinzip: Mitglieder (Reeder) sichern sich gegenseitig ab; Prämien werden nachträglich angepasst. Für die Deckungsauslösung entscheidend ist die prompte Meldung an den zuständigen Club-Korrespondenten im Hafenstaat. Alle 13 IG-Clubs haben weltweite Korrespondentennetzwerke; im Schadenfall sofort aktivieren.

## Koordination mehrerer Versicherer
Bei einem Schiffsunfall sind typischerweise beteiligt: H&M-Versicherer (Schaden am eigenen Schiff); P&I-Club (Drittschäden; Personenschäden; Umwelt); ggf. War-Risk-Versicherer (politische Risiken); Cargo-Versicherer der Ladung (vom Befrachter beauftragt). Koordination ist essenziell um Deckungslücken und Doppelerstattungen zu vermeiden.

## Beweissicherung nach Schadensereignis
Unmittelbare Maßnahmen: Unfallstelle fotografieren; beschädigte Teile sichern; Zeugenaussagen protokollieren; Logbücher und Stundenbücher sofort sichern und beglaubigen lassen. Externe Gutachter (Havariekommissar; Klasseninspektor; P&I-Club-Surveyor) sind unverzüglich zu bestellen. Digitale Daten (AIS; VDR; ECDIS) sichern und auf Backup-Medien kopieren.


## Checkliste Schadensmeldung
- [ ] P&I-Club-Korrespondent am Schadensort informiert (innerhalb 24 Stunden)
- [ ] H&M-Versicherer unverzüglich benachrichtigt; DTV-Fristen eingehalten
- [ ] MII-Police der Bank aktiviert (wenn Hypothekengläubiger betroffen)
- [ ] Schadensdokumentation vollständig: Fotos; Gutachter; Logbücher; Zeugenaussagen
- [ ] Schadensminderungsmaßnahmen veranlasst und dokumentiert (VVG § 82)
- [ ] Klasseninspektor bestellt; ggf. Klasse-Suspension akzeptiert
- [ ] Alle Versicherer koordiniert; Deckungsüberschneidungen geklärt
- [ ] Aufräumungskosten aus P&I-Pollution-Deckung angemeldet

## Relevante Rechtsprechung
- BGH zur Obliegenheitsverletzung (VVG § 28) bei Schiffsversicherung; Kausalitätsgegenbeweis.
- OLG Hamburg zu P&I-Deckungsversagung bei verspäteter Meldung; Club-Rule-Auslegung.
- BGH zu Mortgagee's Interest Insurance; Verhältnis zur H&M-Police; Schutzbereich.

## Normen im Überblick
- VVG § 28: Verletzung vertraglicher Obliegenheiten; Leistungsfreiheit bei Vorsatz; Leistungskürzung bei grober Fahrlässigkeit.
- VVG § 78: Mehrfachversicherung; Gesamtschuldner der Versicherer; Ausgleich.
- VVG § 82: Schadensminderungsobliegenheit; Aufwendungsersatz für Rettungskosten.
- VVG §§ 130-136: Haftpflichtversicherung; Direktklagerecht des Geschädigten.
- DTV-Klauseln Kasko 2009 § 2: versicherte Gefahren und Schäden; Selbstbehalte.


## Vertiefung Schadensmeldung

### Koordination der Versicherer
Bei einem Kaskoschaden sind in der Regel mehrere Versicherer betroffen: H&M-Versicherer für den Sachschaden; P&I-Club für die Haftpflicht gegenüber Dritten; MII für den Hypothekengläubiger. Die Koordination ist Aufgabe des Schiffsanwalts.

### Subrogation
Der H&M-Versicherer, der den Schaden reguliert hat, tritt in die Forderungen des Reeders gegen den Schädiger ein (VVG § 86). Der P&I-Club zahlt nur nach dem Pay-to-be-Paid-Prinzip; der Reeder muss den Schaden erst selbst zahlen und wird dann vom Club erstattet.

## Normen-Synopse Versicherung
| Norm | Inhalt |
|------|--------|
| VVG § 28 | Obliegenheitsverletzung |
| VVG § 82 | Schadensminderung |
| VVG § 86 | Forderungsübergang |
| DTV-Kasko 2009 | Versicherte Gefahren |

## Quellen
- VVG §§ 28-30: https://www.gesetze-im-internet.de/vvg/__28.html
- DTV-Klauseln Kasko: https://www.deutscher-transport-versicherungsverband.de
- IGP&I: https://www.igpandi.org
- openjur P&I-Streit: https://www.openjur.de

## 5. `see-047-werftvertrag-local-counsel-instruieren`

**Fokus:** Werftvertrag: Auslaendischen Anwalt fuer Arrest; Vollstreckung oder Registerfragen bei Neubauprojekt unter Werftvertrag im Ausland instruieren. ISAC 1952; EuGVVO 2012; lokales Seepfandrecht; P&I-Korrespondenten. Output: Local-Counsel-Briefing und Prioritaetenliste.

# Werftvertrag – Local Counsel instruieren

## Mandantenfall
Ein Neubauprojekt unter Werftvertrag liegt in einem ausländischen Hafen; lokaler Arrest ist erforderlich. Eine Hypothekenbank braucht Auskunft zur Vollstreckbarkeit ihrer deutschen Sicherheit im Ausland. Ein P&I-Club braucht nach Unfall lokale Rechtsvertretung für das Neubauprojekt unter Werftvertrag.

## Erste Schritte
1. Local Counsel auswaehlen: Empfehlung durch P&I-Club-Korrespondenten oder Netzwerk.
2. Briefing erstellen: Neubauprojekt unter Werftvertrag-Daten (IMO-Nummer; Flagge); Sachverhalt; deutsches Recht.
3. Lokale Rechtslage abfragen: Vollstreckungsanforderungen; Anerkennung deutscher Titel.
4. ISAC-1952-Pruefung: Ist Hafenstaat Vertragsstaat?
5. Letter of Instruction verfassen: Weisungen; Budget; Berichtspflichten.
6. P&I-Club koordinieren: liegt LOU-Angebot vor; macht es Arrest entbehrlich?

## Rechtsrahmen
- ISAC 1952 Art. 1; EuGVVO 2012 Recast EU-Vollstreckung; UNCLOS Art. 292 Prompt Release; SchRG §§ 8-74.

## Prüfraster
- Ist der Hafenstaat ISAC-1952-Vertragsstaat?
- Sind deutsche Urteile im Hafenstaat anerkennungsfaehig?
- Hat Local Counsel Erfahrung mit Seerecht und Werftvertrag?
- Liegt ein LOU des P&I-Clubs vor?
- Ist der Kostenrahmen fuer das Auslandsverfahren freigegeben?

## Typische Fallstricke
- Lokale Seepfandrechte koennen deutsche Hypothek im Rang ueberbieten.
- Kostenunterschaetzung: Auslandsverfahren dauern laenger und kosten mehr.
- LOU-Verhandlungen erfordern erfahrenen Local Counsel.

## Output
Local-Counsel-Briefing für Neubauprojekt unter Werftvertrag und Prioritätenliste.


## Vertiefung: Netzwerk-Aufbau und Koordination
P&I-Clubs unterhalten weltweit Netzwerke von Korrespondenten und Local Counsel (LoC). Bei Arrestsachen ist der LoC am Liegeplatz des Schiffes entscheidend; er kennt lokale Verfahrensvorschriften und Richter. Bei Vollstreckungsurteilen ist der LoC im Staat des zu vollstreckenden Urteils zuständig. Für EU-Staaten erleichtert die EuGVVO 2012 die Anerkennung.

## Briefing-Elemente
Ein effektives LoC-Briefing enthält: Kurzdarstellung des Sachverhalts (max. 2 Seiten); Kopien der relevanten Verträge; Registerauszug; Arrestbeschluss oder Urteil; Vollmacht; Budgetrahmen; Kommunikationsweg (verschlüsselte E-Mail). Zeitkritische Fragen sofort priorisieren; Arrest läuft schnell ab.

## Kostenkontrolle und Abrechnung
LoC-Anwälte rechnen nach nationalem Recht ab: in England nach Stundensätzen; in Deutschland nach RVG oder Stundensatz. Vorab Kostenvoranschlag und Budgetgenehmigung einholen. P&I-Club trägt die Anwaltskosten in der Regel; vorher Freigabe bestätigen lassen (Club Approval).


## Checkliste Local-Counsel-Beauftragung
- [ ] Local Counsel ausgewählt (Empfehlung P&I-Club-Korrespondent)
- [ ] Erfahrung des LoC mit Seerecht im Hafenstaat bestätigt
- [ ] Vollmacht ausgestellt und übermittelt
- [ ] Briefing-Dokument erstellt: Schiffsdaten; Sachverhalt; deutsches Recht
- [ ] Budgetrahmen genehmigt (P&I-Club-Approval)
- [ ] Berichtspflichten und Eskalationsweg definiert
- [ ] Prüfung ob LOU des P&I-Clubs den Arrest entbehrlich macht
- [ ] ISAC-1952-Status des Hafenstaats geprüft

## Relevante Rechtsprechung
- ITLOS Arctic Sunrise Case No. 22 (Netherlands v. Russia 2013): einstweilige Maßnahmen nach UNCLOS Art. 290; Freilassung des Schiffes.
- ITLOS Juno Trader Case No. 13 (Saint Vincent v. Guinea-Bissau 2004): Prompt Release nach Art. 292; angemessene Sicherheitsleistung.
- EuGH zur EuGVVO 2012; gegenseitige Anerkennung von Vollstreckungstiteln in der EU.

## Normen im Überblick
- ISAC 1952 Art. 1-8: Seeforderungen; Arrest; Verfahren; Vertragsstaat-Liste.
- EuGVVO 2012 Recast Art. 35-57: Vollstreckung ausländischer Titel in der EU.
- UNCLOS Art. 292: Prompt Release; Schiff und Crew freizulassen gegen angemessene Sicherheit.
- ZPO §§ 722-723: Vollstreckbarerklärung ausländischer Urteile in Deutschland.
- Anerkennungs- und Vollstreckungsausführungsgesetz (AVAG): nationale Umsetzung EuGVVO.


## Vertiefung Local Counsel

### Vollmacht und Briefing
Die Vollmacht für den Local Counsel sollte eine Generalvollmacht für alle prozessualen Handlungen enthalten. Das Briefing-Memorandum muss das Kernsachverhalt auf Englisch zusammenfassen; Local Counsel im Ausland arbeitet selten auf Basis deutschsprachiger Unterlagen.

### Koordination P&I-Club
Der P&I-Club hat eigene Netzwerke von Correspondenten und Local Counsel. Die Kosten sind i.d.R. durch die P&I-Deckung gedeckt; eine vorab Budgetfreigabe ist erforderlich.

## Normen-Synopse Local Counsel
| Norm | Inhalt |
|------|--------|
| ISAC 1952 Art. 1 | Seeforderungen |
| UNCLOS Art. 292 | Prompt Release |
| EuGVVO Art. 35 | EU-Vollstreckung |
| NYÜ 1958 | Schiedssprüche |

## Quellen
- ISAC 1952: https://www.admin.ch/opc/de/classified-compilation/19520172/index.html
- EuGVVO: https://dejure.org/gesetze/EuGVVO
- SchRG: https://www.gesetze-im-internet.de/schrg/BJNR014990940.html
- openjur Vollstreckung Ausland: https://www.openjur.de
