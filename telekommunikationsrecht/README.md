# Telekommunikationsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`telekommunikationsrecht.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/telekommunikationsrecht.md) (33 KB)
- Im Repo: [`testakten/megaprompts/telekommunikationsrecht.md`](../testakten/megaprompts/telekommunikationsrecht.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`telekommunikationsrecht`) | [`telekommunikationsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/telekommunikationsrecht.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Großes Arbeitsplugin für Telekommunikationsrecht: vom defekten Internetanschluss bis zur Beschlusskammer der Bundesnetzagentur, vom Glasfaserausbau bis zu Frequenzen, Nummerierung, Netzneutralität, Sicherheitsvorfall und Sonderkartellrecht.

## Was dieses Plugin gut kann

- Verbraucher- und Geschäftskundenfälle zu Anschluss, Störung, Anbieterwechsel, Rufnummer und SLA sauber dokumentieren.
- BNetzA-Verfahren mit Akteneinsicht, Anhörung, Geschäftsgeheimnissen, Stellungnahmen und Eilrechtsschutz führen.
- Marktanalyse, Zugang, Entgelt, Frequenzen, Nummerierung, Open Access und Missbrauchsaufsicht fachlich trennen.
- Datenschutz, Standort-/Verkehrsdaten, IT-Sicherheit, NIS2/BSI und Notfallkommunikation integrieren.

## Startlogik

Beginne mit `tk-allgemeiner-kaltstart`. Der Skill trennt Verbraucherstreit, Geschäftskunden-SLA, Netzbetrieb, Frequenz, Nummerierung, Marktmacht, Infrastruktur, Datenschutz/Sicherheit und BNetzA-Verfahren. Danach wird nur gezielt in Spezial-Skills verzweigt.

## Rechtsweg-Kompass

Telekommunikationsrecht ist gemischt: Vertragliche Ansprüche laufen regelmäßig zivilrechtlich; regulierungsrechtliche Maßnahmen der Bundesnetzagentur sind öffentlich-rechtlich; Missbrauchs- und Wettbewerbsfragen können zivil-, verwaltungs- oder kartellrechtliche Schnittstellen haben. Deshalb prüft jeder streitige Skill zuerst Bescheid, Anspruch, Norm und Rechtsbehelfsbelehrung.

## Quellenhygiene

TKG, Nebengesetze, EU Electronic Communications Code, BNetzA-Verfügungen und Verwaltungspraxis werden live geprüft. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 57 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abhoerschnittstellen-sicherheitsbehoerden` | TK-Überwachung, Schnittstellen, Auskunftsersuchen, Bestandsdaten, Verkehrsdaten, Strafverfolgung und Geheimnisschutz im Telekommunikationsrecht. |
| `abmahnung-tk-anbieterwechsel` | Abmahnungen bei TK-Marketing, Preiswerbung, Rufnummernmissbrauch, Vergleichsportalen und Informationspflichten im Telekommunikationsrecht. |
| `anbieterwechsel-rufnummernmitnahme` | Anbieterwechsel, Versorgungslücke, Rufnummernportierung, Entschädigung, Weiterversorgungspflicht und BNetzA-Beschwerde im Telekommunikationsrecht. |
| `anschlussbereitstellung-tk` | Bereitstellung von Festnetz-, Glasfaser-, Mobilfunk- oder Business-Anschluss: Terminversäumnis, Verzug, Entschädigung, Rücktritt, Ersatzlösung und Beweis im Telekommunikationsrecht. |
| `bauarbeiten-kabelschaden` | Kabelschäden: Leitungsauskunft, Verkehrssicherung, Tiefbau, Schadensersatz, Betriebsunterbrechung und Beweissicherung im Telekommunikationsrecht. |
| `behoerdenkommunikation-kooperationsstrategie` | Kommunikationsstrategie gegenüber der Bundesnetzagentur: kooperativ, präzise, aktenfest, geheimnisschonend und entscheidungsorientiert im Telekommunikationsrecht. |
| `beschwerde-tk-beweisplan` | Dashboard für Massenbeschwerden: Anbieterwechsel, Störung, Rufnummer, Werbeanruf, Rechnung, Missbrauch und Fristen im Telekommunikationsrecht. |
| `beweisplan-messung-stoerung-protokoll` | Technischer Beweisplan für TK-Streit: Breitbandmessung, Ausfallprotokoll, Routerlogs, Technikertermine, Fotos, Tickets, SLA und Zeugen im Telekommunikationsrecht. |
| `bundesnetzagentur-tk-zustaendigkeits` | Verfahren vor der Bundesnetzagentur: Anhörung, Akteneinsicht, Geschäftsgeheimnisse, Beiladung, Fristen, Beschlusskammerlogik und gerichtliche Anschlussstrategie im Telekommunikationsrecht. |
| `callcenter-tk-campusnetze` | Telefonwerbung, Einwilligung, Rufnummernanzeige, Dokumentation, Bußgeldrisiko und Callcenter-Verträge im Telekommunikationsrecht. |
| `campusnetze-private-5g` | Campusnetze/private 5G: lokale Frequenzen, Betreiberrolle, Sicherheit, SLA, Industrieanwendung und Drittzugang im Telekommunikationsrecht. |
| `cloud-tk-cookies` | Cloud-PBX/VoIP: Notruf, Standort, Datenschutz, Aufzeichnung, Ausfallsicherheit, Rufnummern und internationale Nutzer im Telekommunikationsrecht. |
| `cookies-telemedien-ttdsg-tdddg` | Telemedien-/TK-Schnittstelle: Cookies, Einwilligung, Endgerätezugriff, Consent-Banner und Telekommunikationsdienste im Telekommunikationsrecht. |
| `datacenter-tk-eilrechtsschutz` | Rechenzentrumskonnektivität: Carrier Meet-Me, Cross-Connects, SLA, Wegerecht im Gebäude, Datenschutz/Sicherheit und Ausfallhaftung im Telekommunikationsrecht. |
| `eilrechtsschutz-bnetza-beschluss` | Eilrechtsschutz bei Frequenz-, Entgelt-, Zugang-, Nummerierungs- oder Missbrauchsmaßnahmen im Telekommunikationsrecht. |
| `entgeltgenehmigung-tk-eu` | Entgeltregulierung, Kostenunterlagen, Effizienzmaßstab, Genehmigung, Margin Squeeze und Eilrechtsschutz im Telekommunikationsrecht. |
| `eu-eecc-router` | EU-Router für TK-Recht: Richtlinie (EU) 2018/1972, Verbraucherrechte, Marktregulierung, Nummerierung, Universaldienst, Netzneutralität und nationale Umsetzung im TKG im Telekommunikationsrecht. |
| `frequenznutzung-tk-frequenzzuteilung` | Funkstörungen, EMV, Störungsmeldung, Messung, Unterlassung und BNetzA-Eingriff im Telekommunikationsrecht. |
| `frequenzzuteilung-auktionsdesign` | Frequenzzuteilung, Vergabeverfahren, Auktionsdesign, Versorgungsauflagen, Nebenbestimmungen und Rechtsschutz im Telekommunikationsrecht. |
| `glasfaser-tk-infrastruktursharing` | Glasfaser- und Hausanschlussprojekte: Grundstückszugang, Gebäudenetz, Wegerecht, Gestattung, Wohnungseigentum, Open Access und Baukoordination im Telekommunikationsrecht. |
| `infrastruktursharing-open-access` | Open-Access-Modelle, Infrastruktursharing, Wholesale-Only, Kooperationsverträge, Nichtdiskriminierung und Beihilfe-/Förderschnittstelle im Telekommunikationsrecht. |
| `iot-tk-kartellrecht` | IoT-/M2M-Konnektivität: SIM-Karten, Roaming, Nummerierung, Sicherheit, Datenzugriff, Produkthaftung und Vertragsketten im Telekommunikationsrecht. |
| `kaltstart-routing` | Allgemeiner Einstieg ins Telekommunikationsrecht: Anschluss, Internet, Mobilfunk, Anbieterwechsel, BNetzA-Bescheid, Frequenz, Nummerierung, Marktmacht, Datenschutz und Sicherheitsvorfall sortieren. |
| `kartellrecht-schnittstelle-gwb-eu` | TK-Verträge und Kooperationen mit Kartellrechtsbezug: Open Access, Ausbaukooperation, Exklusivität, Wholesale, Joint Venture im Telekommunikationsrecht. |
| `marktanalyse-tk-meldepflicht` | Marktanalyse, Marktdefinition, SMP/beträchtliche Marktmacht, Konsultation, EU-Abstimmung und Regulierungsverfügung im Telekommunikationsrecht. |
| `meldepflicht-it-sicherheitsvorfall` | Sicherheitsvorfälle bei TK-Anbietern: BNetzA/BSI/DSGVO-Meldungen, Kundenkommunikation, Ursachenanalyse und Abhilfe im Telekommunikationsrecht. |
| `mindestvertragslaufzeit-tk-umzug` | TK-Verträge: Mindestlaufzeit, automatische Verlängerung, monatliche Kündbarkeit, Kündigungsbutton/Onlinekündigung, AGB und Nachweis im Telekommunikationsrecht. |
| `missbrauchsaufsicht-tk-mitnutzung` | Missbrauchsaufsicht im TK-Recht: Marktmacht, Diskriminierung, Behinderung, Margin Squeeze, Zugang und Verhältnis zu GWB/AEUV im Telekommunikationsrecht. |
| `mitnutzung-gebaeude-netze` | Mitnutzung von Gebäudenetzen, Leerrohren, Masten, Schächten und passiver Infrastruktur im Telekommunikationsrecht. |
| `netzneutralitaet-tk-nis2` | Netzneutralität: Zero-Rating, Priorisierung, Drosselung, Spezialdienste, Traffic Management und Beschwerde-/Abmahnrisiken im Telekommunikationsrecht. |
| `nis2-kritis-bsi-schnittstelle` | NIS2/KRITIS/BSI-Anforderungen für TK-Unternehmen, Rechenzentren, Managed Services und kritische Kommunikation im Telekommunikationsrecht. |
| `notfall-tk-notrufpflicht` | Notfallkommunikation, Resilienz, Priorisierung, Cell Broadcast, Behördenkommunikation und Business Continuity im Telekommunikationsrecht. |
| `notrufpflicht-112` | Notruf 112/110, Standortdaten, Ausfallsicherheit, VoIP, Alarmierung, Unternehmensanschlüsse und Haftungsrisiko im Telekommunikationsrecht. |
| `nummerierung-tk-open` | Rufnummernzuteilung, Nutzung, Entzug, Mehrwertdienste, geografische Nummern, 0800/0900, M2M und Nummernportierung im Telekommunikationsrecht. |
| `open-ran-lieferketten` | Open-RAN-/Netzkomponenten: Lieferkette, Sicherheit, Interoperabilität, Ausfall, Exportkontrolle und kritische Komponenten im Telekommunikationsrecht. |
| `output-beschwerde-antrag-klage` | Formate im Telekommunikationsrecht: BNetzA-Beschwerde, Verbraucher-Schlichtung, verwaltungsrechtlicher Antrag, Widerspruch/Anfechtung, zivilrechtliche Klage und Stellungnahme. |
| `redteam-regulierungsrisiko` | Red-Team für TK-Projekte: Marktmacht, Zugangs-/Entgeltregulierung, Wegerecht, Sicherheit, Datenschutz, BNetzA, Kartellrecht und politische Sichtbarkeit. |
| `routerfreiheit-tk-rufnummernmissbrauch` | Routerfreiheit, Netzabschlusspunkt, Endgerätefreiheit, Providerrouter, Konfigurationsdaten, Glasfaser-ONT und Gewährleistung/Sicherheit im Telekommunikationsrecht. |
| `rufnummernmissbrauch-abschaltung` | Rufnummernmissbrauch, Ping-Anrufe, Spam, Mehrwertdienste, Abschaltung, Rechnungslegungs-/Inkassoverbot und Beschwerde im Telekommunikationsrecht. |
| `satellite-tk-schlichtung` | Satelliteninternet/NTN: Frequenzen, Genehmigung, Endgeräte, Verbrauchervertrag, Resilienz und nationale Sicherheitsaspekte im Telekommunikationsrecht. |
| `schlichtung-verbraucher` | Verbraucherschlichtung bei TK-Streit: Voraussetzungen, Antrag, Unterlagen, Hemmung/Fristen, Verhältnis zu Klage und BNetzA-Beschwerde im Telekommunikationsrecht. |
| `sla-tk-standardangebot` | Geschäftskunden-SLA: Verfügbarkeit, Reaktions-/Entstörzeiten, Credits, Schadensersatz, Haftungsbegrenzung und Force Majeure im Telekommunikationsrecht. |
| `standardangebot-reference-offer` | Standardangebotspflichten, Prüfung von Klauseln, Änderungsanordnung, Zugangsnachfrage und Nichtdiskriminierung im Telekommunikationsrecht. |
| `stoerung-tk-streitbeilegung` | Internet-/Telefonstörung: Minderung, Ausfallentschädigung, Entstörungspflichten, Messprotokolle, SLA und Schadensersatz im Telekommunikationsrecht. |
| `streitbeilegung-bnetza` | Streitbeilegung bei Zugang, Mitnutzung, Entgelt, Nummerierung oder Anbieterwechsel mit BNetzA-Beteiligung im Telekommunikationsrecht. |
| `towerco-tk-traffic` | Mobilfunkstandorte: Miet-/Gestattungsvertrag, Baurecht, Immissionsschutz, Standortsharing, Rückbau und Eigentümerkonflikt im Telekommunikationsrecht. |
| `traffic-location-data-privacy` | Verkehrsdaten, Standortdaten, Einzelverbindungsnachweis, Abrechnung, Einwilligung, Sicherheit und Löschung im Telekommunikationsrecht. |
| `umzug-vertragsanpassung` | Umzug bei TK-Vertrag: Fortführung, Sonderkündigung, Leistungsfähigkeit am neuen Standort, Glasfaser-/Kabelanschluss und Kosten im Telekommunikationsrecht. |
| `universalservice-tk-verwaltungsrecht` | Universaldienst/Mindestversorgung mit Telekommunikationsdiensten: Unterversorgung, Anspruch, BNetzA-Verfahren, technische Zumutbarkeit und Alternativen im Telekommunikationsrecht. |
| `verwaltungsrecht-anfechtung-bnetza` | Anfechtung, Verpflichtung oder Eilrechtsschutz gegen BNetzA-Beschlüsse und Nebenbestimmungen im Telekommunikationsrecht. |
| `vorratsdaten-tk-wegerecht` | Vorratsdatenspeicherung, Quick Freeze, Sicherheitsbehördenanfragen und EuGH/BVerfG-Linie live prüfen im Telekommunikationsrecht. |
| `wegerecht-oeffentliche-wege` | Wegerecht, Mitverlegung, Baustellenkoordination, Zustimmung, Wiederherstellung und Streit mit Straßenbaulastträgern im Telekommunikationsrecht. |
| `wholesale-tk-bauarbeiten` | Wholesale-, Reseller- und MVNO-Verträge: Zugang, SLA, Entgelt, Nummerierung, Kundenschutz, Datenschutz und Exit im Telekommunikationsrecht. |
| `zivilklage-tk-abhoerschnittstellen` | Zivilrechtliche TK-Klagen: Entgeltforderungen, Rückzahlung, Schadensersatz, SLA, AGB, Minderung und Verbraucher-/Businessstreit im Telekommunikationsrecht. |
| `zugangsregulierung-tk-zusammenschaltung` | Zugang zu Netzen, Vorleistungsprodukten, TAL/Bitstrom, Glasfaser, Nichtdiskriminierung und technische Schnittstellen im Telekommunikationsrecht. |
| `zusammenschaltung-interconnection` | Zusammenschaltung, Terminierung, IP-Interconnection, Qualität, Entgelte und Streitbeilegung im Telekommunikationsrecht. |
| `zustaendigkeits-router-bnetza-vg-lg` | Rechtsweg- und Zuständigkeitsrouter für TK-Streitigkeiten: Verbraucheranspruch, BNetzA-Regulierungsverfahren, zivilrechtlicher Vertrag, verwaltungsgerichtlicher Eilrechtsschutz und Kartell-/Missbrauchsschnittstelle im Telekommunikationsr... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
