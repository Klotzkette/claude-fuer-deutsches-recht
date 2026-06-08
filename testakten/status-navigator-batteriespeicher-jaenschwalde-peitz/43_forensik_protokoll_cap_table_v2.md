# Forensik-Protokoll Cap-Table V2 (Inkubator-IT Cottbus GmbH)

**Auftraggeber:** Karlheinz Bauernfeind als Geschäftsführer LausitzStorage 200 GmbH
**Auftrag erteilt:** 09.06.2026 nach Eingang Anwaltsschreiben Lindenthal (Akte 39)
**Auftragnehmer:** Inkubator-IT Cottbus GmbH, Berliner Straße 14, 03046 Cottbus
**Verantwortlicher Forensiker:** Dipl.-Inf. Henning Trostein (zertifizierter IT-Sachverständiger nach §§ 36, 37 SchfHwG)
**Protokoll erstellt:** 11.06.2026
**Aktenzeichen Inkubator-IT:** ICTC-2026/0609-LausitzStorage-Forensik

## I. Auftragsbeschreibung

Untersuchung der Frage, ob die in der Cap-Table-Datei `cap_table_aktuell.xlsx` (gepflegt durch das Sekretariat Bauernfeind im Geschäftsführungs-NAS-Pfad `\\NAS\GF\Beteiligung\`) in Variante V2 ausgewiesene Beteiligungsstruktur (NordCap 30,61 % statt 30,00 %, Gesamtkapital 78.780 EUR statt 78.000 EUR) in der **Außenkommunikation** der Gesellschaft im Zeitraum **01.02.2026 bis 09.06.2026** verwendet worden ist.

## II. Untersuchungsumfang

- 18.247 Mailpostfacher-Eingänge/Ausgänge der Geschäftsführungsadressen
  - karlheinz.bauernfeind@lausitzstorage.de (Hauptpostfach)
  - sekretariat@lausitzstorage.de
  - finanzen@lausitzstorage.de (Steuerberater Hentschel)
  - reporting@lausitzstorage.de (Investor Relations)
- 8.412 ausgehende Dateianhänge mit Cap-Table-relevanter Dateibezeichnung (Stichwortsuche: `cap`, `beteiligung`, `gesell`, `anteil`, `78`)
- Geschäftsführungs-NAS `\\NAS\GF\Beteiligung\` — sämtliche Versionsstände der Datei `cap_table_aktuell.xlsx` (Excel-Versionshistorie, OneDrive-Sync-Backups)
- Kommunikation mit externen Empfängern: NordCap, Lindenthal, Stadtwerke Cottbus, ILB, Commerzbank, Linklaters, Sungrow, 50Hertz, LEAG, Notar Dr. Albers, Pohlmann & Pohlmann, Schweikart Knabel und Partner

## III. Methodik

Volltext-Scan der Mailpostfächer mit folgenden Stichwort-Kombinationen:
- `78.780` oder `78,780.00` oder `78.780,00`
- `24.180` oder `24,180.00` oder `24.180,00`
- `30,61` oder `30.61`
- `Cap-Table V2` oder `Cap Table V2` oder `CapTableV2`
- Dateinamens-Hashes der V2-Excel-Datei (SHA-256 vor und nach jeder identifizierten Bearbeitung)

Zusätzlich wurde die Versionshistorie des Excel-Dokuments forensisch ausgelesen — alle 47 Änderungs-Snapshots zwischen 22.02.2026 (V2-Erstanlage) und 09.06.2026 (V2-Löschung, siehe unten) wurden dokumentiert.

## IV. Befunde

### IV.1 Interne Verwendung

- Die Datei `cap_table_aktuell.xlsx` mit V2-Linie wurde **zwischen 22.02.2026 und 09.06.2026** ausschließlich im Geschäftsführungs-NAS gepflegt.
- Zugriffsberechtigung: Bauernfeind (lesen/schreiben), Sekretariat Pawlowski (lesen/schreiben), Steuerberater Hentschel (nur lesen, Zugriff erst ab 14.03.2026).
- Hentschel hat in seinen Buchhaltungs-/Bilanzauswertungen ausschließlich die V1-Linie verwendet (verifiziert durch Stichproben in der DATEV-Mandantenarchivierung 01.03.2026 – 31.05.2026).

### IV.2 Externe Verwendung — Befund: KEINE

> **Im untersuchten Zeitraum wurde die V2-Linie zu keinem Zeitpunkt in einer Außenkommunikation der LausitzStorage 200 GmbH verwendet.**

Konkret:

- 12 Investor-Update-Mails an NordCap im Zeitraum 01.02.2026 – 31.05.2026: alle enthalten V1-Linie (verifiziert durch Anhangs-Inspektion).
- 7 Mails an Lindenthal (vorrangig kommunikatorisch): keine Cap-Table-Anlagen.
- 14 Mails an Stadtwerke Cottbus: keine Cap-Table-Anlagen mit V2.
- 8 ILB-Kommunikationen (Avalrahmenanträge, Berichte): nur V1.
- Commerzbank-Kommunikation (Konto-Sicherheiten, Limit-Erhöhungen): nur V1.
- Linklaters (Security Agent): Cap-Table-Sektion in Quartalsbericht — nur V1.
- Sungrow, 50Hertz, LEAG: keine Cap-Table-Anlagen.
- Notar Albers: nur V1-Linie in Beurkundungsvorbereitungen.

### IV.3 Versionshistorie V2

- **Erstanlage V2:** 22.02.2026, 14:17 Uhr (Excel-Versionshistorie Zelleneditierung B3 von 23.400 auf 24.180, B7 von 78.000 auf 78.780)
- **Hintergrund:** Bauernfeind-Notiz in Zelle K3: „Antizipation Teilwandlung NordCap aus 02.03.2026-Sondierung". Diese Notiz spricht für die Erklärung „Vorschau, nicht Beschluss" — sie nimmt zeitlich auf eine Mail Bezug, die nachweislich am 02.03.2026 von NordCap an Bauernfeind erging.
- **Bereinigung:** 09.06.2026, 11:47 Uhr — V2-Werte zurückgesetzt auf V1-Werte. Bestätigung durch Pawlowski-Sekretariats-Protokoll.

## V. Gutachterliche Bewertung

> „Auf Grundlage der vorliegenden technischen Befunde kann mit hoher Sicherheit ausgeschlossen werden, dass die in der V2-Linie ausgewiesene Beteiligungsstruktur (NordCap 30,61 % / Gesamtkapital 78.780 EUR) im Zeitraum 22.02.2026 bis 09.06.2026 von der Geschäftsführung der LausitzStorage 200 GmbH in der Außenkommunikation gegenüber Banken, Investoren, Aufsichtsbehörden, Vertragspartnern oder Mitgesellschaftern verwendet worden ist. Die V2-Werte waren ausschließlich interne Vorausplanung."

## VI. Hinweise für die Geschäftsführung

1. Künftige interne Voraus-Planungen sind in einem **separaten Dokument** (`cap_table_forecast.xlsx`) zu führen, das nicht mit der aktuellen Cap-Table verwechselt werden kann.
2. Jeder Voraus-Plan ist mit einem **expliziten Vermerk** „NICHT BESCHLOSSEN, VORAUSSCHAU" zu kennzeichnen.
3. Der Zugang von Steuerberater Hentschel zum Voraus-Plan-Dokument ist zu sperren (Vermeidung von Bilanzkonfusion).
4. Eine **interne Compliance-Note** mit Verteiler an die Mitgesellschafter über die V2-Entstehung, V2-Bereinigung und die Maßnahmen 1-3 ist zu erstellen — Entwurf wird durch Pohlmann & Pohlmann beigesteuert.

## VII. Aktenlage

- Forensik-Protokoll Original (89 Seiten mit Anhängen): Inkubator-IT Cottbus, Auftragsdokumentation
- Beglaubigte Kopie: LausitzStorage und Pohlmann & Pohlmann
- Anhang zur Stellungnahme Bauernfeind in der Gesellschafterversammlung 24.06.2026 (Akte 40 Anlage 3)

## VIII. Verbindung zur Step-Plan-Führung

Mit Vorlage dieses Protokolls in der Gesellschafterversammlung 24.06.2026 wird:
- Tagesordnungspunkt 2 (Abberufung Bauernfeind) **entscheidend entlastet** — der Vorwurf „Cap-Table-Manipulation" wird widerlegt im Sinne einer fehlenden Außenverwendung
- Tagesordnungspunkt 8 (Sonderprüfung) **noch nicht erübrigt** — Lindenthal kann auf eigene Untersuchungsbreite bestehen
- Der Status der Statusplan-Führung im Step-Plan-Sheet `25_step_plan_excel_lausitzstorage.xlsx`, Reiter „Beteiligung" wird von gelb (offene Cap-Table-Frage) auf grün gesetzt; Aktenstücke 16, 17, 18 erhalten den Vermerk „forensisch geprüft, V2 nur intern, bereinigt 09.06.2026".

## Normbezug

- §§ 36, 37 SchfHwG (Sachverständigeneigenschaft Forensiker)
- § 51a GmbHG (Auskunftsrecht der Gesellschafter — entlastend belegt)
- § 43 Abs. 1 GmbHG (Sorgfaltspflicht — entlastend für Bauernfeind, soweit Außenkommunikation betroffen)
- § 263 StGB (Betrug — keine Anzeichen, da keine Vermögensverfügung Dritter auf Basis V2 erfolgt ist)
