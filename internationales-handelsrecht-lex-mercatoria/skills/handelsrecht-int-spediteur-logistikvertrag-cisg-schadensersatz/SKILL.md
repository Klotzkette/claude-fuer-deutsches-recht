---
name: handelsrecht-int-spediteur-logistikvertrag-cisg-schadensersatz
description: "INT Spediteur Logistikvertrag CISG Schadensersatz: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# INT Spediteur Logistikvertrag CISG Schadensersatz

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **INT Spediteur Logistikvertrag CISG Schadensersatz** im Plugin Internationales Handelsrecht Lex Mercatoria. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ihl-025-spediteur-und-logistikvertrag` | Internationales Handelsrecht: Spediteurrecht national (HGB §§ 453-466) und international. FIATA-Dokumente (FBL, FCR, FWR), Spediteurslagerschein, Haftungsregimes bei Sammelladung, Haftungsdurchbrechung durch Kenntnis vom Inhalt und Multimodaltransport. |
| `ihl-007-cisg-schadensersatz-und-mitigation` | Internationales Handelsrecht: Schadensersatz nach CISG Art. 74-77. Voller Ersatz des Verlustes und entgangenen Gewinns (Art. 74), Deckungskauf/-verkauf (Art. 75), abstrakter Marktpreis (Art. 76), Schadenminderungspflicht (Art. 77) und Zinsen (Art. 78). |
| `ihl-033-sanktionen-und-embargos` | Internationales Handelsrecht: Handelssanktionen EU, USA (OFAC) und UK (OFSI). Blocking Statute (EU VO 2018/1100), SDN-Liste, Sektorsanktionen, Finanzsanktionen, Compliance-Pflichten und Konflikte zwischen EU- und US-Sanktionen. |
| `ihl-021-dap-dpu-ddp` | Internationales Handelsrecht: Ankunftsklauseln DAP, DPU und DDP nach Incoterms 2020. Gefahrübergang am Bestimmungsort, Entladepflicht (DPU), Verzollungspflicht (DDP), Risiken für Verkäufer und steuerrechtliche Implikationen. |

## Arbeitsweg

Im Plugin Internationales Handelsrecht Lex Mercatoria gilt für **INT Spediteur Logistikvertrag CISG Schadensersatz**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ihl-025-spediteur-und-logistikvertrag`

**Fokus:** Internationales Handelsrecht: Spediteurrecht national (HGB §§ 453-466) und international. FIATA-Dokumente (FBL, FCR, FWR), Spediteurslagerschein, Haftungsregimes bei Sammelladung, Haftungsdurchbrechung durch Kenntnis vom Inhalt und Multimodaltransport.

# Spediteur- und Logistikvertrag

## Worum es geht

Der Spediteur organisiert Transporte, schließt im eigenen Namen für Rechnung des Versenders ab (Fixkosten-Spediteur: §§ 459, 460 HGB) oder als Frachtführer (§ 458 HGB). Für internationale Spedition gibt FIATA standardisierte Dokumente heraus. Das Haftungsregime des Spediteurs ist komplex, da er verschiedene Subfrachtführer einsetzt.

## Kernnormen / Kernquellen

- **HGB § 453**: Speditionsvertrag — Definition
- **HGB § 454**: Pflichten des Spediteurs (Beförderung, Versicherung, Zoll, Benachrichtigung)
- **HGB § 459 Abs. 1**: Selbsteintritt als Frachtführer
- **HGB § 461**: Haftung des Spediteurs — HGB-Frachtrecht gilt entsprechend
- **FIATA Multimodal Transport Bill of Lading (FBL)**: Wertpapier für multimodale Transporte
- **FIATA FCR**: Forwarders Certificate of Receipt — nicht übertragbar
- **ADSp 2017**: Allgemeine Deutsche Spediteurbedingungen — AGB der Branche

## Schlüsselbegriffe

- Selbsteintritt §§ 458-460 HGB: Spediteur wird Frachtführer — eigene Haftung
- Sammelladung § 460 HGB: Haftungsregime bei Stückgutzusammenladung
- FIATA FBL: eigentliches Wertpapier (negotiable) — geeignet für Akkreditivzwecke
- Unbekannte Klausel im Konnossement: Spediteur haftet für Schäden wenn Inhalt nicht bekannt
- ADSp 2017 Haftungsgrenzen: 8,33 SZR/kg (wie CMR) aber mit Summenbegrenzungen

## Typische Streitfragen / Anwendungsfälle

1. Spediteur beauftragt Sub-Frachtführer — wer haftet bei Transportschaden gegenüber Versender?
2. FBL als Akkreditivdokument: Akzeptiert Bank FIATA FBL statt Sea BL?
3. ADSp 2017: Gelten AGB-Klauseln im grenzüberschreitenden Geschäft?
4. Multimodaler Transport: Welches Haftungsregime gilt bei unbekanntem Schadensort?
5. Spediteur als Exportkontrollverantwortlicher: Pflichten bei sanktionierten Ländern?

## Methodik

- Erstbestimmung Spediteur vs. Frachtführer: Pflicht zur Eigenbeförderung oder nur Organisation?
- Haftungsregime: bekannter Schadensort → Einzelregime (CMR, MÜ); unbekannt → ADSp/FIATA
- FBL für Akkreditive: nur wenn Bank ausdrücklich akzeptiert (UCP 600 Art. 19 Multimodal-Transport-Dokument)
- ADSp 2017: nur bei nationalen Verträgen; international: FIATA-Bedingungen besser

## Output

- Spediteur vs. Frachtführer Abgrenzungsschema
- FIATA-Dokumentenübersicht (FBL, FCR, FWR, FIATA Warrant)
- Haftungs-Flussdiagramm bei unbekanntem Schadensort

## Quellenregel

HGB §§ 453-466: gesetze-im-internet.de. ADSp 2017: dslv.org. FIATA-Dokumente: fiata.org. UCP 600: iccwbo.org. Unsicherheit bleibt sichtbar.

## 2. `ihl-007-cisg-schadensersatz-und-mitigation`

**Fokus:** Internationales Handelsrecht: Schadensersatz nach CISG Art. 74-77. Voller Ersatz des Verlustes und entgangenen Gewinns (Art. 74), Deckungskauf/-verkauf (Art. 75), abstrakter Marktpreis (Art. 76), Schadenminderungspflicht (Art. 77) und Zinsen (Art. 78).

# Schadensersatz und Schadensminderung (CISG Art. 74-78)

## Worum es geht

Das CISG-Schadensersatzsystem beruht auf dem Grundsatz der vollen Kompensation (Art. 74): Verlust und entgangener Gewinn, begrenzt durch die Vorhersehbarkeit zum Vertragsabschluss. Art. 75 und 76 bieten konkrete Berechnungsweisen bei Vertragsaufhebung. Art. 77 verpflichtet den Gläubiger zur Schadensminderung — Verstoß reduziert den Anspruch.

## Kernnormen / Kernquellen

- **Art. 74 CISG**: Voller Schadensersatz — Verlust + entgangener Gewinn, Vorhersehbarkeitsgrenze
- **Art. 75 CISG**: Konkrete Methode — Deckungsgeschäft (nach Vertragsaufhebung)
- **Art. 76 CISG**: Abstrakte Methode — Vertragspreisdifferenz zum laufenden Marktpreis
- **Art. 77 CISG**: Schadensminderungspflicht — angemessene Maßnahmen; Versäumnis → Reduktion
- **Art. 78 CISG**: Zinsen — kein expliziter Zinssatz (durch IPR zu ergänzen)
- **Art. 79 CISG**: Befreiung bei Hindernis (kein Schadensersatz, aber Aufhebungsrecht bleibt)

## Schlüsselbegriffe

- Vorhersehbarkeit: Typ des Verlustes zur Zeit des Vertragsabschlusses (nicht Höhe)
- Deckungskauf Art. 75: Angemessenheit, Unverzüglichkeit nach Aufhebung
- Marktpreis Art. 76: laufender Preis am Erfüllungsort (oder anderen Referenzmarkt)
- Mitigation: zumutbare Maßnahmen — kein Selbstopfer, aber aktive Gegenmaßnahmen
- Zinshöhe Art. 78: nationales Recht nach IPR (CISG bleibt stumm)

## Typische Streitfragen / Anwendungsfälle

1. Umfasst Art. 74 Rechtsverfolgungskosten und Gutachterkosten als ersatzfähigen Schaden?
2. Wann ist ein Deckungskauf "angemessen" i.S.d. Art. 75 (Preis, Timing, Marktzugang)?
3. Vorhersehbarkeit: Muss der Typ des Schadens oder der Betrag vorhersehbar sein?
4. Zinssatz Art. 78: Welches nationale Recht gilt — Schuld- oder Forderungsstatut?
5. Art. 77 Verstoß: Nur Schadensreduzierung oder vollständiger Anspruchsverlust?

## Methodik

- Vorhersehbarkeit immer auf Vertragsabschluss beziehen, nicht auf Verletzung
- Art. 75 vor Art. 76 prüfen (konkret vor abstrakt)
- Mitigation-Pflicht als eigenen Prüfpunkt anlegen
- Zinsen Art. 78: Renvoi auf anwendbares nationales Recht nach Rom I

## Output

- Schadensberechnungs-Schema (Art. 74/75/76 alternativ)
- Mitigation-Analyse: Was hätte Gläubiger tun müssen?
- Zinsenberechnung mit Rechtswahlanalyse

## Quellenregel

CISG Art. 74-78: uncitral.un.org. Rechtsprechung: CISG-online.ch, jusmundi.com. CISG Advisory Council Opinion No. 6 (Art. 74, 77). Schrifttum: Gotanda in Kröll/Mistelis/Viscasillas (2018) Art. 74. Unsicherheit bleibt sichtbar.

## 3. `ihl-033-sanktionen-und-embargos`

**Fokus:** Internationales Handelsrecht: Handelssanktionen EU, USA (OFAC) und UK (OFSI). Blocking Statute (EU VO 2018/1100), SDN-Liste, Sektorsanktionen, Finanzsanktionen, Compliance-Pflichten und Konflikte zwischen EU- und US-Sanktionen.

# Sanktionen und Embargos

## Worum es geht

Handelssanktionen beschränken oder verbieten Handels-, Finanz- und Servicetransaktionen mit bestimmten Ländern, Unternehmen oder Personen. Die EU verhängt Sanktionen nach Art. 29 EUV (GASP) und Art. 215 AEUV. OFAC (USA) und OFSI (UK) haben teils extraterritoriale Wirkung. Der EU Blocking Statute (VO 2018/1100) verbietet EU-Unternehmen, bestimmten US-Sekundärsanktionen zu folgen.

## Kernnormen / Kernquellen

- **VO (EU) 2024/1485 (Russland 14. Sanktionspaket)**: aktuellstes EU-Sanktionsrecht Russland
- **VO (EG) 765/2006 und 208/2014**: Sanktionen Belarus und Ukraine-Konflikt
- **EU Blocking Statute VO (EG) 2271/96 i.d.F. 2018/1100**: Schutz vor US-Sekundärsanktionen
- **OFAC SDN-Liste**: US-Treasury, Specially Designated Nationals and Blocked Persons
- **OFAC Sectoral Sanctions (SSI-Liste)**: sektorbezogene Beschränkungen Russland (Energie, Finanzen)
- **UK OFSI Financial Sanctions**: gov.uk/government/organisations/office-of-financial-sanctions-implementation

## Schlüsselbegriffe

- Primärsanktionen: Beschränkungen des sanktionierenden Staates auf eigene Staatsbürger/Firmen
- Sekundärsanktionen (USA): Beschränkungen gegen Drittstaaten-Unternehmen bei Russland/Iran-Handel
- Blocking Statute: EU-Unternehmen dürfen US-Sekundärsanktionen nicht befolgen (Konflikt)
- SDN-Matching: 50%-Regel — Unternehmen mit >50% SDN-Beteiligung ebenfalls blockiert
- Wind-Down-Lizenz: OFAC erlaubt befristeten Abbau von Transaktionen

## Typische Streitfragen / Anwendungsfälle

1. EU-Blocking-Statute: Was tut ein EU-Unternehmen wenn US-Bank Transaktion blockiert?
2. SDN 50%-Regel: Tochtergesellschaft eines SDN-Unternehmens — automatisch blockiert?
3. Russland-Sanktionen: Kann russisches Unternehmen über Dubai-Tochter EU-Güter beziehen?
4. Sanktionsklausel im Vertrag: Wie formulieren, damit Force-Majeure-Wirkung entsteht?
5. OFSI UK nach Brexit: Parallele Pflichten zu OFAC und EU?

## Methodik

- Screening-Prozess: SDN-Liste + EU-konsolidierte Sanktionsliste täglich (OFAC/EU API)
- Ownership-Prüfung: 50%-Regel für verbundene Unternehmen
- Blocking-Statute-Konflikt: EU-Unternehmens-Rechtsabteilung und BAFA/Generaldirektion Handel informieren
- Sanctions-Klausel: vertragliche Regelung wer bei Sanktionsverstoß haftet

## Output

- Sanktions-Screening-Checkliste
- Blocking-Statute-Konflikt-Handlungsplan
- Sanctions-Klausel-Muster

## Quellenregel

EU-Sanktionen: eur-lex.europa.eu. OFAC: home.treasury.gov/policy-issues/office-of-foreign-assets-control-sanctions. OFSI: gov.uk. Blocking Statute VO 2271/96: eur-lex.europa.eu. Unsicherheit bleibt sichtbar.

## 4. `ihl-021-dap-dpu-ddp`

**Fokus:** Internationales Handelsrecht: Ankunftsklauseln DAP, DPU und DDP nach Incoterms 2020. Gefahrübergang am Bestimmungsort, Entladepflicht (DPU), Verzollungspflicht (DDP), Risiken für Verkäufer und steuerrechtliche Implikationen.

# DAP, DPU, DDP: Ankunftsklauseln

## Worum es geht

DAP (Delivered at Place), DPU (Delivered at Place Unloaded, neu in 2020 statt DAT) und DDP (Delivered Duty Paid) sind Ankunftsklauseln: der Verkäufer trägt Gefahr und Kosten bis zum Bestimmungsort. DDP ist die verkäuferfreundlichste Klausel für den Käufer — der Verkäufer übernimmt Import, Zölle und alle Kosten. DPU verpflichtet den Verkäufer zur Entladung.

## Kernnormen / Kernquellen

- **Incoterms 2020 DAP A2/B2**: Gefahrübergang am Bestimmungsort (benannte Stätte), vor Entladung
- **Incoterms 2020 DPU A2/B2**: Gefahrübergang nach Entladung am Bestimmungsort; früher DAT
- **Incoterms 2020 DDP A2/B2**: Gefahrübergang wie DAP; plus Importzoll und alle Abgaben Sache Verkäufer
- **Unionszollkodex (UZK) VO (EU) 952/2013**: Importeur als Zollschuldner
- **VAT-Regelungen**: DDP kann Umsatzsteuer-Registrierungspflicht im Importland auslösen

## Schlüsselbegriffe

- DAP vs. DPU: Unterschied bei Entladung — DPU schließt Entladung ein
- DDP-Risiko Verkäufer: Exportkontrolle, Importlizenzen, Zölle, USt.-Registrierung im Käuferland
- Named Place: Terminal-Name vs. Käuferwerk — unterschiedliche Kostenträgerschaft
- Entladeverzögerung: wer trägt Kosten bei Wartezeit am Bestimmungsort?
- DDP und Mehrwertsteuer: Verkäufer muss USt. im Importland abführen → steuerliche Compliance

## Typische Streitfragen / Anwendungsfälle

1. DDP EU → Russland/Iran: Exportkontrolle und Sanktionen — DDP praktisch unmöglich?
2. DPU: Muss Verkäufer Entladegerät stellen oder reicht Abladen von LKW?
3. DAP: Wann beginnt Gefahrübergang genau — Terminal-Einfahrt oder Käufer-Abladebereich?
4. DDP und Reverse-Charge-Verfahren: Kann Käufer USt. selbst abführen statt Verkäufer?
5. DDP mit "exclusive of VAT": Zulässige Modifikation oder Widerspruch zur Klausel?

## Methodik

- D-Klauseln: Kosten/Gefahranalyse immer am benannten Ort beginnen
- DDP: Vor Wahl prüfen ob Verkäufer USt.-Nummer im Importland hat/braucht
- Exportkontrolle: Bei sanktionierten Ländern DDP oder DAP nicht wählen
- Named Place DPU: explizit Terminal-Name + Entladefazilität spezifizieren

## Output

- DAP/DPU/DDP Vergleichstabelle: Gefahrübergang, Kosten, Pflichten
- DDP-Risiko-Check (Steuer, Zoll, Exportkontrolle)
- Named-Place-Spezifikations-Muster

## Quellenregel

Incoterms 2020: iccwbo.org. UZK (VO 952/2013): eur-lex.europa.eu. Schrifttum: Ramberg, ICC Guide to Incoterms 2020 (2019). Unsicherheit bleibt sichtbar.
