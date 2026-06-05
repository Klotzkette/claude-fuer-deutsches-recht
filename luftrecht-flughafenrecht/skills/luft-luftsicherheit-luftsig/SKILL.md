---
name: luft-luftsicherheit-luftsig
description: "Luft Luftsicherheit Luftsig: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Luft Luftsicherheit Luftsig

## Arbeitsbereich

Dieser Skill bündelt 5 sachlich verwandte Arbeitsschritte rund um **Luft Luftsicherheit Luftsig** im Plugin Luftrecht Flughafenrecht. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `luft-012-luftsicherheit-luftsig` | Flughafen oder Airline klaert Sicherheitspflichten oder fechtet LuftSiG-Bescheid an. Prueft LuftSiG §§ 1-9 Sicherheitsplan Kontrollpflichten EU-DVO 2015/1998 Sicherheitsprogramm und Rechtsschutz gegen Auflagen und liefert Compliance-Check-Vermerk und Widerspruchs-Baustein. |
| `luft-013-zuverlaessigkeitsueberpruefung` | Person wurde Zuverlässigkeit nach LuftSiG § 7 versagt oder widerrufen. Prueft Versagungsgruende Vorstrafen Verfassungsschutz-Erkenntnisse Gesamtwürdigung Anhoerungspflicht Rechtsschutz vor VG und BVerfG 2 BvL 8/07 Grundrechtskonformitaet und liefert Widerspruchs-Schriftsatz-Baustein. |
| `luft-014-drohnen-uas-betrieb` | Drohnenbetreiber braucht Betriebsgenehmigung oder Mandant ist nach Drohnenflug-Unfall in Haftungsfragen verwickelt. Prueft EU-VO 2019/947 Betriebskategorien Open/Specific/Certified LuftVG § 21a Registrierungspflicht LBA Versicherungspflicht EU-VO 785/2004 und liefert Genehmigungs-Checkliste und Haftungs-Vermerk. |
| `luft-015-gefahrgut-luftfracht` | Absender Spedition oder Airline hat Gefahrgut-Luftfrachtproblem: fehlerhafte Deklaration Versand verbotener Gueter oder Behoerdenuntersuchung. Prueft ICAO TI Doc 9284 IATA DGR LuftVG § 27 Gefahrgutbeauftragter und Strafbarkeit nach LuftVG § 58 und liefert Compliance-Check und Stellungnahme-Baustein. |
| `luft-016-passagierrechte-schnittstelle` | Passagier fordert Entschaedigung nach Flugumsetzung Annullierung oder Verspaetung. Prueft EU-VO 261/2004 Art. 5-7 Entschaedigungshoehe 250-600 EUR aussergewoehnliche Umstaende EuGH Sturgeon C-402/07 und Nelson C-581/10 Verbindungsflug-Rechtsprechung und liefert Klageschriftsatz-Baustein. |

## Arbeitsweg

Im Plugin Luftrecht Flughafenrecht gilt für **Luft Luftsicherheit Luftsig**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `luft-012-luftsicherheit-luftsig`

**Fokus:** Flughafen oder Airline klaert Sicherheitspflichten oder fechtet LuftSiG-Bescheid an. Prueft LuftSiG §§ 1-9 Sicherheitsplan Kontrollpflichten EU-DVO 2015/1998 Sicherheitsprogramm und Rechtsschutz gegen Auflagen und liefert Compliance-Check-Vermerk und Widerspruchs-Baustein.

# Luftsicherheit nach LuftSiG – Compliance und Rechtsschutz

## Mandantenfall

- Flughafenbetreiber erhält Bescheid der Luftsicherheitsbehörde mit Auflagen zur Verschärfung der Zugangskontrollen; Kosten unzumutbar Widerspruch geplant.
- Catering-Unternehmen auf dem Flughafen braucht LuftSiG-Sicherheitsprogramm und Zulassung als bekannter Lieferant.
- Airline erhält nach LuftSiG-Inspektion Mangelliste und 30-Tage-Frist zur Abhilfe.

## Erste Schritte

1. Normadressat bestimmen: Flugplatzbetreiber (§ 8 LuftSiG) Luftfahrtunternehmen (§ 9 LuftSiG) andere Unternehmen mit Sicherheitsbereichszugang (§ 7 LuftSiG).
2. Sicherheitsprogramm prüfen: Flugplatz-Sicherheitsprogramm (§ 8 Abs. 2 LuftSiG) und Airline-Sicherheitsprogramm (§ 9 Abs. 2 LuftSiG) müssen EU-DVO 2015/1998 entsprechen.
3. Mängel kategorisieren: kritische Mängel (sofortige Abhilfe) gewöhnliche Mängel (30-Tage-Frist) Empfehlungen.
4. EU-Recht-Abgleich: EU-DVO 2015/1998 enthält technische Spezifikationen im Anhang.
5. Widerspruch gegen Auflagen: Verhältnismäßigkeit (LuftSiG § 8 Abs. 1 iVm VwVfG § 36).
6. Compliance-Plan erstellen: Maßnahmen Verantwortliche Fristen Nachweisdokumentation.

## Rechtsrahmen

- **LuftSiG § 1**: Zweck; Schutz vor Angriffen auf die Sicherheit des zivilen Luftverkehrs.
- **LuftSiG § 7**: Zuverlässigkeitsüberprüfung; Zugangsberechtigungen für Sicherheitsbereiche.
- **LuftSiG § 8**: Pflichten des Flugplatzbetreibers; Sicherheitsprogramm und Kontrollen.
- **LuftSiG § 9**: Pflichten der Luftfahrtunternehmen; eigenes Sicherheitsprogramm.
- **EU-DVO 2015/1998**: Technische Anforderungen für Luftsicherheitsmaßnahmen.
- **LuftSiG § 12**: Kein aufschiebende Wirkung von Widerspruch und Klage.
- **VwVfG § 36**: Beifügung von Auflagen; Verhältnismäßigkeitsprüfung.

## Prüfraster

1. Ist das Sicherheitsprogramm EU-DVO-2015/1998-konform und aktuell?
2. Sind Zugangskontrollen und Personenüberprüfungen vollständig dokumentiert?
3. Sind Inspektionsmängel korrekt kategorisiert?
4. Sind Auflagen verhältnismäßig?
5. Sind Fristen für Abhilfemaßnahmen realistisch?
6. Besteht Widerspruchsmöglichkeit gegen Ablehnungen?

## Typische Fallstricke

- Sicherheitsprogramm veraltet; automatische Auflage.
- Kritische Mängel nicht als solche erkannt; Betriebsunterbrechung droht.
- Widerspruch ohne aufschiebende Wirkung (§ 12 LuftSiG); Auflage sofort vollziehbar.
- EU-DVO-Anforderungen strenger als nationales Verständnis.

## Output

Compliance-Check-Vermerk mit Ampel-Rating je Sicherheitsbereich. Widerspruchs-Baustein gegen unverhältnismäßige Auflage. Abhilfeplan-Muster.

## Quellen

- LuftSiG: https://www.gesetze-im-internet.de/luftsig/
- EU-DVO 2015/1998: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32015R1998
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- EASA: https://www.easa.europa.eu/en/domains/aviation-safety-management

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Einschlägige Normen vor Mandatsbearbeitung vollständig auf aktuelle Fassung prüfen.
- Behördenanschreiben stets mit Aktenzeichen und Fristbenennung versehen.
- Klagefristen und Widerspruchsfristen sofort bei Mandatsannahme kalendarisch sichern.
- Bei grenzüberschreitenden Sachverhalten internationalen Normenkonflikt prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Luftrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 2. `luft-013-zuverlaessigkeitsueberpruefung`

**Fokus:** Person wurde Zuverlässigkeit nach LuftSiG § 7 versagt oder widerrufen. Prueft Versagungsgruende Vorstrafen Verfassungsschutz-Erkenntnisse Gesamtwürdigung Anhoerungspflicht Rechtsschutz vor VG und BVerfG 2 BvL 8/07 Grundrechtskonformitaet und liefert Widerspruchs-Schriftsatz-Baustein.

# Zuverlässigkeitsüberprüfung LuftSiG § 7 – Versagung, Widerruf und Rechtsschutz

## Mandantenfall

- Mitarbeiter eines Catering-Unternehmens am Flughafen erhält ablehnenden Bescheid der Luftsicherheitsbehörde wegen einer 8 Jahre alten Verurteilung; Arbeitsplatz gefährdet.
- Flugzeugführer verliert Zutrittsberechtigung nach Verfassungsschutzeintrag; Mandant bestreitet die Tatsachengrundlage.
- Flughafenbetreiber muss Mitarbeiter mit neuem Doppel-Arbeitsverhältnis neu überprüfen lassen; Verfahren läuft.

## Erste Schritte

1. Bescheid analysieren: welcher Versagungsgrund (§ 7 Abs. 1a LuftSiG)? Vorstrafe Verfassungsschutzeintrag Alkohol-/Drogenproblematik oder falsche Angaben?
2. Anhörung prüfen: wurde Person vor Entscheidung angehört (§ 7 Abs. 5 LuftSiG)? Verletzung führt zur Aufhebbarkeit.
3. Mitwirkungspflicht prüfen: hat Mandant alle angeforderten Unterlagen eingereicht?
4. Widerspruch einlegen: keine aufschiebende Wirkung (§ 7 Abs. 12 LuftSiG); paralleler Eilantrag § 80 Abs. 5 VwGO.
5. Gesamtwürdigung angreifen: Straftat lange zurückliegend seitdem unbelastet; Verhältnismäßigkeit.
6. Verfassungsrechtliche Dimension: BVerfG bestätigt Verfassungsmäßigkeit aber verlangt Verhältnismäßigkeit im Einzelfall.

## Rechtsrahmen

- **LuftSiG § 7 Abs. 1**: Pflicht zur Zuverlässigkeitsüberprüfung für Sicherheitsbereichszugang.
- **LuftSiG § 7 Abs. 1a**: Regel-Versagungsgründe: Freiheitsstrafe ab 60 Tagessätzen in letzten 5 Jahren; Verfassungsschutzeintrag.
- **LuftSiG § 7 Abs. 5**: Anhörungspflicht vor ablehnender Entscheidung.
- **LuftSiG § 7 Abs. 12**: Kein aufschiebende Wirkung von Widerspruch und Klage.
- **LuftSiG § 7 Abs. 11**: Löschungsfristen für gespeicherte Daten.
- **VwGO § 80 Abs. 5**: Eilantrag auf Wiederherstellung der aufschiebenden Wirkung.
- **BVerfGE v. 4.5.2010 - 2 BvL 8/07**: Verfassungsmäßigkeit § 7 Abs. 1 Satz 1 Nr. 4 LuftSiG.

## Prüfraster

1. Liegt anerkannter Regel-Versagungsgrund vor?
2. Wurde Anhörungspflicht (Abs. 5) gewahrt?
3. Ist Gesamtwürdigung des Einzelfalls vorgenommen worden?
4. Ist Verhältnismäßigkeit gewahrt (Zeitablauf Leumund seit Tat)?
5. Wurden alle Mitwirkungspflichten erfüllt?
6. Ist Eilantrag § 80 Abs. 5 VwGO notwendig um Arbeitsplatz zu sichern?

## Typische Fallstricke

- Widerspruch ohne parallelen Eilantrag; automatischer Vollzug.
- Verfassungsschutzeintrag unbekannt; Mandant hat keine Einsicht.
- Gesamtwürdigung als reiner Automatismus behandelt; Gericht kann aufheben.
- Löschungsfristen nicht beachtet; Daten länger als erlaubt gespeichert.

## Output

Widerspruchs-Schriftsatz-Baustein mit Verhältnismäßigkeitsargumentation. Eilantrag § 80 Abs. 5 VwGO Muster. Prüfschema Versagungsgrund.

## Quellen

- LuftSiG: https://www.gesetze-im-internet.de/luftsig/
- BVerfG Urteil 2 BvL 8/07: https://www.bverfg.de
- VwGO: https://www.gesetze-im-internet.de/vwgo/
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Einschlägige Normen vor Mandatsbearbeitung vollständig auf aktuelle Fassung prüfen.
- Behördenanschreiben stets mit Aktenzeichen und Fristbenennung versehen.
- Klagefristen und Widerspruchsfristen sofort bei Mandatsannahme kalendarisch sichern.
- Bei grenzüberschreitenden Sachverhalten internationalen Normenkonflikt prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Luftrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 3. `luft-014-drohnen-uas-betrieb`

**Fokus:** Drohnenbetreiber braucht Betriebsgenehmigung oder Mandant ist nach Drohnenflug-Unfall in Haftungsfragen verwickelt. Prueft EU-VO 2019/947 Betriebskategorien Open/Specific/Certified LuftVG § 21a Registrierungspflicht LBA Versicherungspflicht EU-VO 785/2004 und liefert Genehmigungs-Checkliste und Haftungs-Vermerk.

# Drohnen und UAS-Betrieb – Genehmigung, Registrierung und Haftung

## Mandantenfall

- Filmproduktionsfirma will kommerziellen Drohnenflug über Menschenansammlung durchführen; fragt nach notwendiger Genehmigung und Versicherung.
- Landwirt setzt Drohnen zur Feldbesprühung ein; LBA hat Betrieb ohne EASA-Zertifizierung beanstandet.
- Drohne kollidiert mit Kleinhubschrauber; Versicherung und Haftungsfragen stehen im Raum.

## Erste Schritte

1. Betriebskategorie bestimmen: Open (max. 25 kg keine Genehmigung Unterklassen A1/A2/A3) Specific (Risikoanalyse LBA-Genehmigung) oder Certified (Zulassungspflicht wie Flugzeug).
2. Registrierungspflicht prüfen: LBA-Registrierung für Drohnen ab 250 g Abfluggewicht oder mit Kamera.
3. Flugverbotszonen prüfen: Lufträume um Flughäfen Naturschutzgebiete Bahnanlagen.
4. EASA-Kompetenznachweis: Open-Kategorie A2 erfordert Online-Training; Specific braucht Operational Authorisation oder STS.
5. Versicherungspflicht: EU-VO 785/2004 gilt auch für unbemannte Luftfahrzeuge ab 20 kg.
6. Haftung bei Unfall: Halter-Haftung nach LuftVG § 33 (Gefährdungshaftung).

## Rechtsrahmen

- **EU-VO 2019/947 Art. 4-6**: Betriebskategorien Open/Specific/Certified.
- **EU-VO 2019/947 Art. 14**: Registrierungspflicht; LBA zuständig.
- **Delegierte VO EU 2019/945**: Technische Anforderungen an UAS-Klassen C0-C6.
- **LuftVG § 21a**: UAS-Betrieb im deutschen Luftraum.
- **LuftVG § 33**: Gefährdungshaftung des Luftfahrzeughalters; gilt auch für UAS.
- **EU-VO 785/2004**: Versicherungspflicht für Luftfahrzeuge; Mindestdeckungssummen.
- **BNatSchG § 44**: Naturschutz-Flugverbote.
- **LuftVG § 21e**: Nationales UAS-Register; Registrierungspflicht ab 250 g.
- **LuftVO § 21b**: Betriebsverbote und Beschränkungszonen; Kontrollluftraum.
- **EASA Easy Access Rules for UAS**: Konsolidierte Fassung aller UAS-Verordnungen.
## Prüfraster

1. In welche Betriebskategorie fällt der geplante Einsatz?
2. Ist Drohne korrekt beim LBA registriert?
3. Liegt EASA-Kompetenznachweis des Piloten vor?
4. Sind alle Flugverbotszonen geprüft?
5. Besteht ausreichende Haftpflichtversicherung?
6. Wurde LBA-Betriebsgenehmigung (Specific) korrekt beantragt?
7. Ist Betriebskategorie (offen/spezifisch/zertifiziert) korrekt eingestuft (EU-VO 2019/947 Art. 5)?
8. Liegt für spezifische Kategorie ein genehmigter SORA-Risikoplan vor?
## Typische Fallstricke

- Open-Kategorie angenommen obwohl kommerzieller Flug über Menschen Specific erfordert.
- Registrierungspflicht vergessen; Drohne ohne Registrierung ist Ordnungswidrigkeit.
- Versicherung nur für Personenschäden nicht für Sachschäden am Drittflugzeug.
- Naturschutzgebiet nicht überprüft; Einsatz illegal.
- Drohne über 250 g nicht im UAS-Register eingetragen; Bußgeld nach LuftVG § 58.
- Betriebszone ohne LBA-Genehmigung überflogen; Strafbarkeit nach § 315a StGB.
## Output

Genehmigungs-Checkliste je Betriebskategorie. Haftungs-Vermerk Drohnenunfall. Versicherungsnachweis-Muster. Betriebsgenehmigungsmatrix nach Kategorie. SORA-Risikoanalyse-Template.
## Quellen

- EU-VO 2019/947: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019R0947
- Delegierte VO 2019/945: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32019R0945
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- EASA Drohnen: https://www.easa.europa.eu/en/domains/civil-drones-rpas
- LBA UAS: https://www.lba.de/DE/Drohnen/Drohnen_node.html

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Drohnen und UAS-Betrieb ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Einschlägige Normen vor Mandatsbearbeitung vollständig auf aktuelle Fassung prüfen.
- Behördenanschreiben stets mit Aktenzeichen und Fristbenennung versehen.
- Klagefristen und Widerspruchsfristen sofort bei Mandatsannahme kalendarisch sichern.
- Bei grenzüberschreitenden Sachverhalten internationalen Normenkonflikt prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Drohnen und UAS-Betrieb sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 4. `luft-015-gefahrgut-luftfracht`

**Fokus:** Absender Spedition oder Airline hat Gefahrgut-Luftfrachtproblem: fehlerhafte Deklaration Versand verbotener Gueter oder Behoerdenuntersuchung. Prueft ICAO TI Doc 9284 IATA DGR LuftVG § 27 Gefahrgutbeauftragter und Strafbarkeit nach LuftVG § 58 und liefert Compliance-Check und Stellungnahme-Baustein.

# Gefahrgut-Luftfracht – Klassifizierung, Compliance und Haftung

## Mandantenfall

- Pharmaunternehmen will Lithium-Ionen-Batterien als Luftfracht versenden; Spediteur zweifelt an korrekter Deklaration nach IATA DGR.
- Airline erhält nach Rampen-Inspektion einen Finding-Report über undeklarierten Gefahrguttransport; Bußgeldverfahren eingeleitet.
- Bekannter Versender will Status als Known Consignor erlangen; Prüfung der Anforderungen.

## Erste Schritte

1. Gefahrgutklasse bestimmen: ICAO TI Doc 9284 / IATA DGR Klassenliste; Verpackungsanweisung Mengenbegrenzung Label.
2. Verbotsliste prüfen: bestimmte Güter sind vollständig verboten (Explosivstoffe bestimmte Klassen in Passagierflugzeugen).
3. Deklarations-Korrektheit prüfen: Shipper's Declaration (DGD) UN-Nummer korrekte Verpackungsanweisung Markierung.
4. Pflichten nach LuftVG § 27: Gefahrgutbeauftragter vorgeschrieben für bestimmte Luftfahrtunternehmen und Verlader.
5. Bei Verstoß: Bußgeldrahmen LuftVG § 58 Abs. 1; strafrechtliche Relevanz bei vorsätzlichem Handeln.
6. Airline-Compliance: Gefahrgut-Annahmeprozess Schulungsnachweise Dokumentation (IATA DGR 3.5).

## Rechtsrahmen

- **ICAO TI Doc 9284**: Basisregelwerk; jährlich aktualisiert; bindend für ICAO-Vertragsstaaten.
- **IATA DGR**: Operationale Umsetzung; strengere Anforderungen als ICAO TI.
- **LuftVG § 27**: Gefahrgutbeauftragter für Luftfahrtunternehmen und Verlader.
- **LuftVG § 58 Abs. 1**: Ordnungswidrigkeiten bei Gefahrgut-Verstößen.
- **EU-VO 300/2008**: Einbeziehung von Gefahrgut in die allgemeine Luftsicherheit.
- **Montreal Convention Art. 18**: Haftung des Luftfrachtführers für Gefahrgutschäden.
- **Montrealer Übereinkommen Art. 18**: Haftung des Luftfrachtführers für Beschädigung; Haftungsausschlüsse.
- **LuftVG § 44**: Nationale Verweisung auf Montrealer Übereinkommen für innerdeutsche Flüge.
- **EU-VO 300/2008 und DVO 2015/1998**: Sicherheitsanforderungen für Luftfracht; ACC3 und RA/KC-Status.
- **HGB § 475**: Frachtführerhaftung subsidiär; nur soweit MÜ keine Regelung trifft.
## Prüfraster

1. Ist Gut korrekt nach IATA DGR klassifiziert?
2. Ist DGD vollständig und korrekt ausgefüllt?
3. Bestehen Transportverbote für Passagierflugzeuge?
4. Ist Gefahrgutbeauftragter nach LuftVG § 27 bestellt und geschult?
5. Liegt Finding-Report-Befund in bußgeldrelevanter Schwere vor?
6. Sind Schulungsnachweise aller Beteiligten aktuell?
7. Ist Haftungsgrenze (22 SZR/kg) eingehalten oder Werterklärung im AWB vermerkt?
8. Ist die Frachtkette lückenlos dokumentiert (AWB Sicherheitsdeklaration Manifest)?
## Typische Fallstricke

- Lithium-Batterien nach falscher Verpackungsanweisung; schwerer Verstoß.
- DGD mit Mengenüberschreitung; Grenzwerte werden nicht jährlich geprüft.
- Gefahrgutbeauftragter formal bestellt aber nicht geschult; Haftung des Unternehmens.
- Bußgeldverfahren ohne anwaltliche Begleitung; falsche Aussagen.
- Haftungsregime Montrealer Übereinkommen mit HGB-Recht vermischt; falsche Haftungssumme.
- AWB fehlt oder unvollständig; Beweislastumkehr zulasten des Frachtführers.
## Output

Compliance-Check IATA DGR mit konkreter Sendung. Stellungnahme-Baustein für Behördenverfahren. Gefahrgutbeauftragten-Pflichtenübersicht. Haftungsanalyse nach MÜ. AWB-Prüfschema. Schadensmeldungs-Fristenübersicht.
## Quellen

- ICAO Doc 9284: https://www.icao.int/safety/dangerousgoods/pages/technical-instructions.aspx
- LuftVG: https://www.gesetze-im-internet.de/luftvg/BJNR006810922.html
- EU-VO 300/2008: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R0300
- EASA: https://www.easa.europa.eu/en/domains/air-operations/dangerous-goods
- LBA Luftfracht: https://www.lba.de

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftfrachtrecht und Warschauer/Montrealer System ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Einschlägige Normen vor Mandatsbearbeitung vollständig auf aktuelle Fassung prüfen.
- Behördenanschreiben stets mit Aktenzeichen und Fristbenennung versehen.
- Klagefristen und Widerspruchsfristen sofort bei Mandatsannahme kalendarisch sichern.
- Bei grenzüberschreitenden Sachverhalten internationalen Normenkonflikt prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Luftfrachtrecht und Warschauer/Montrealer System sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz

## 5. `luft-016-passagierrechte-schnittstelle`

**Fokus:** Passagier fordert Entschaedigung nach Flugumsetzung Annullierung oder Verspaetung. Prueft EU-VO 261/2004 Art. 5-7 Entschaedigungshoehe 250-600 EUR aussergewoehnliche Umstaende EuGH Sturgeon C-402/07 und Nelson C-581/10 Verbindungsflug-Rechtsprechung und liefert Klageschriftsatz-Baustein.

# Passagierrechte – EU 261/2004 Entschädigung und Durchsetzung

## Mandantenfall

- Passagier wird bei überbuchtem Flug umgesetzt (Denied Boarding); Airline bietet nur Voucher statt Bargeldzahlung nach Art. 7 an.
- Familie klagt nach fünfstündiger Ankunftsverspätung; Airline beruft sich auf Streik als außergewöhnlichen Umstand.
- Verbindungsflug mit Endstrecke außerhalb EU: Mandant fragt ob EU 261 gilt wenn erster Abschnitt von Berlin nach London führt.

## Erste Schritte

1. Anwendungsbereich prüfen: EU-Flughafen als Abflug oder EU-Carrier als Betreiber (Art. 3 VO 261/2004).
2. Tatbestand bestimmen: Denied Boarding (Art. 4) Annullierung (Art. 5) oder Verspätung von 3+ Stunden bei Ankunft (EuGH C-402/07 Sturgeon).
3. Entschädigungshöhe: Art. 7 – 250 EUR (bis 1500 km) 400 EUR (1500-3500 km) 600 EUR (über 3500 km).
4. Außergewöhnliche Umstände prüfen: Art. 5 Abs. 3; technische Defekte selten anerkannt (EuGH C-549/07 Wallentin-Hermann).
5. Verbindungsflug-Regel: Gesamtreiseverspätung maßgeblich; EU 261 gilt für gesamten Flug wenn Abflug-Flughafen in EU.
6. Klage: SÖP-Schlichtungsstelle oder direkt Klage beim AG; Verjährung 3 Jahre (§ 195 BGB).

## Rechtsrahmen

- **EU-VO 261/2004 Art. 3**: Anwendungsbereich; Abflugort oder EU-Carrier.
- **EU-VO 261/2004 Art. 4**: Denied Boarding; Entschädigungspflicht.
- **EU-VO 261/2004 Art. 5**: Annullierung; Entschädigung außer bei außergewöhnlichen Umständen.
- **EU-VO 261/2004 Art. 7**: Entschädigungshöhe 250/400/600 EUR.
- **EuGH C-402/07 (Sturgeon)**: Verspätung ab 3 Stunden Ankunft = Entschädigungsanspruch wie Annullierung.
- **EuGH C-581/10 (Nelson)**: Bestätigung Sturgeon.
- **EuGH C-549/07 (Wallentin-Hermann)**: Technischer Defekt selten außergewöhnlicher Umstand.

## Prüfraster

1. Greift EU-VO 261/2004 (Abflugort EU oder EU-Carrier)?
2. Liegt Denied Boarding Annullierung oder 3-h-Ankunftsverspätung vor?
3. Beruft sich Airline auf außergewöhnliche Umstände – sind diese belegt?
4. Ist Entschädigungshöhe korrekt berechnet (Entfernung)?
5. Hat Airline alternative Betreuungsleistungen (Art. 9) erbracht?
6. Ist Anspruch verjährt?

## Typische Fallstricke

- Außergewöhnliche Umstände zu weit angenommen; EuGH-Rechtsprechung einengend.
- Verbindungsflug: nur Teil-Verspätung berechnet statt Gesamt-Ankunftsverspätung.
- Voucher statt Barzahlung akzeptiert; Anspruch nicht vollständig abgegolten.
- SÖP-Schlichtung nicht genutzt; unnötige Klageverzögerung.

## Output

Klageschriftsatz-Baustein AG (EU-261-Anspruch). Außergewöhnliche-Umstände-Gegenargumentations-Liste. Entschädigungsberechnung-Tool.

## Quellen

- EU-VO 261/2004: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32004R0261
- EuGH Sturgeon C-402/07: https://eur-lex.europa.eu
- EuGH Nelson C-581/10: https://eur-lex.europa.eu
- EuGH Wallentin-Hermann C-549/07: https://eur-lex.europa.eu

## Hinweise für die Praxis

Dieser Skill deckt den Bereich Luftrecht ab. Folgende praktische Hinweise ergänzen die obigen Ausführungen:

- Einschlägige Normen vor Mandatsbearbeitung vollständig auf aktuelle Fassung prüfen.
- Behördenanschreiben stets mit Aktenzeichen und Fristbenennung versehen.
- Klagefristen und Widerspruchsfristen sofort bei Mandatsannahme kalendarisch sichern.
- Bei grenzüberschreitenden Sachverhalten internationalen Normenkonflikt prüfen.

### Dokumentationspflichten

Für Mandate im Bereich Luftrecht sind folgende Dokumente regelmäßig anzufordern:

- Aktueller LBA-Luftfahrzeugrolle-Auszug mit Eigentumsangaben
- AG-Braunschweig-Registerauszug (Luftfahrzeugpfandrecht)
- Cape-Town-Registerauszug (ICAO International Registry)
- Gültige Betriebsgenehmigung und AOC-Kopie
- Leasingvertrag oder Eigentumsnachweis
- Aktuelle Behördenbescheide und Aufsichtskorrespondenz
