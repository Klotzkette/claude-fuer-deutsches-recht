# Digital-Compliance — eCMR, FrachtPersV, KI-Routenoptimierung

Akte: Compliance-Analyse / Schwarmstedt Logistik GmbH
Verfasserin: Frederike Klemm (Referendarin), unter Aufsicht RAin Dr. Hammerschmidt
Stand: 10. April 2026

---

## 1. Ausgangslage

Im Rahmen der Mandatsbearbeitung wurden mehrere digitale Compliance-Defizite bei der Schwarmstedt Logistik GmbH identifiziert, die zwar nicht unmittelbar mit dem CMR-Transportschaden zusammenhängen, jedoch regulatorische Risiken begründen und im Rahmen der Gesamtberatung zu adressieren sind.

---

## 2. eCMR — Elektronischer Frachtbrief

### 2.1 Rechtsgrundlage

Der elektronische CMR-Frachtbrief (eCMR) ist durch das Zusatzprotokoll zur CMR vom 20. Februar 2008 (sog. e-CMR-Protokoll) zugelassen, dem Deutschland am 16. März 2020 beigetreten ist (BGBl. II 2020, Nr. 10, S. 218). Frankreich, Rumänien und zahlreiche weitere EU-Staaten sind ebenfalls Vertragsparteien.

Die eCMR ermöglicht die vollständige Digitalisierung des Frachtbriefaustauschs (Ausstellung, Übermittlung, Empfangsbestätigung) über interoperable Plattformen.

### 2.2 Festgestellte Mängel im Schadenstransport

Der CMR-Frachtbrief Nr. CMR-2026-DE-001-0018 wurde als Papier-Frachtbrief ausgestellt. Schwarmstedt nutzt für etwa 30% seiner EU-Transporte bereits die eCMR-Plattform "CargoSign" (Lieferant: CargoSign BV, Rotterdam). Im vorliegenden Transport wurde eCMR nicht eingesetzt.

**Unvollständige eCMR-Daten (sofern vorhanden):**
Das CargoSign-System enthält für andere Transporte im Januar 2026 lückenhafte Einträge:
- Fehlende GPS-Koordinaten bei Fahrtunterbrechungen
- Nicht vollständig eingetragene Unterschriften bei Übergabe/Übernahme (Empfängerbestätigung fehlt in 3 Fällen)
- Temperaturlogger-Daten nicht mit eCMR verknüpft (manueller Export erforderlich)

**Rechtliche Einordnung:** Unvollständige oder fehlende eCMR-Einträge begründen im Streitfall Beweisprobleme. Nach Art. 9 CMR hat der Frachtbrief Beweiskraft für Übernahme, Zustand und Gewicht der Güter. Wenn der eCMR unvollständig ist, entfällt diese Beweiskraft.

### 2.3 FrachtPersV-Anforderungen

Die Fahrpersonalverordnung (FrachtPersV) i.d.F. vom 01. März 2021 setzt die VO (EG) 561/2006 und die RL 2002/15/EG für die Arbeitszeitgestaltung um. § 1 Abs. 2 FrachtPersV definiert den Anwendungsbereich: alle Fahrzeuge mit einem zulässigen Gesamtgewicht über 3,5 Tonnen im gewerblichen Güterverkehr.

**Streitpunkt FrachtPersV:** Nach §§ 6 ff. FrachtPersV sind Aufzeichnungen über Arbeitszeiten, Lenkzeiten und Ruhezeiten zu führen und für mindestens 12 Monate aufzubewahren. Bei Schwarmstedt liegen die Tachographendaten in digitaler Form vor (Digi-Tach DTCO 3283, Hersteller: VDO/Continental). Der Abruf und die Archivierung erfolgen nach bisheriger Feststellung unregelmäßig — nicht alle Fahrerdaten werden nach jedem Einsatz heruntergeladen.

**BALM-Risiko:** Das BALM prüft bei Kontrollen regelmäßig die Vollständigkeit der Tachographenaufzeichnungen. Lücken in der Aufzeichnung (nicht heruntergeladene Daten) können als Verstoß gegen § 4 Abs. 3 FPersG (Aufzeichnungspflicht des Unternehmers) geahndet werden.

---

## 3. KI-Routenoptimierungstool "TruckMind" — Regulierung nach KI-VO

### 3.1 Das System

Schwarmstedt Logistik GmbH setzt seit Oktober 2025 probeweise das KI-Routenoptimierungssystem "TruckMind" ein (Hersteller: TruckMind Solutions GmbH, Stuttgart, Beta-Version 2.1.0). TruckMind nutzt maschinelles Lernen und Echtzeit-Verkehrsdaten zur Optimierung von Transportrouten, Fahrzeugbelegung und Fahrereinsatzplanung. Das System generiert auch Empfehlungen zur Lenk- und Ruhezeitplanung.

### 3.2 Anwendbarkeit der KI-Verordnung (EU) 2024/1689

Die Verordnung (EU) 2024/1689 des Europäischen Parlaments und des Rates über künstliche Intelligenz (KI-VO, "AI Act") ist am 01. August 2024 in Kraft getreten; die Verbote für unakzeptable Risiken gelten ab 02. Februar 2025, weitere Vorschriften ab 02. August 2025 (für Hochrisiko-KI-Systeme).

**Einordnung TruckMind:**

Art. 6 Abs. 2 KI-VO i.V.m. Anhang III KI-VO listet Hochrisiko-KI-Systeme auf. Relevant sind:
- Anhang III Nr. 3: "KI-Systeme für den Betrieb kritischer Infrastrukturen" — Logistik ist nicht explizit genannt, aber Gefahrguttransport könnte unter kritische Infrastruktur fallen
- Anhang III Nr. 9: "KI-Systeme für die Personalverwaltung, insbesondere die Rekrutierung und Auswahl von Arbeitnehmern" — die Fahrereinsatzplanung durch TruckMind könnte hierunter fallen

**Vorläufige Einschätzung:** TruckMind ist wahrscheinlich **kein Hochrisiko-KI-System** nach Anhang III, da es primär Routenoptimierung (kein biometrisches Screening, keine Entscheidung über grundlegende Rechte) betreibt. Es unterliegt jedoch den allgemeinen Transparenzpflichten nach Art. 50 KI-VO.

### 3.3 Transparenz- und Protokollierungspflichten

Auch wenn TruckMind nicht als Hochrisiko-System einzustufen ist, sollte Schwarmstedt folgendes sicherstellen:

**(a) Art. 50 KI-VO (Transparenzpflichten):** Fahrer müssen informiert sein, dass KI-Empfehlungen für ihre Routenplanung genutzt werden. TruckMind muss sich als KI-System zu erkennen geben.

**(b) Protokollierung (Logging):** Für spätere Streitfälle sollte dokumentiert sein, welche KI-Empfehlungen gegeben und welche tatsächlich umgesetzt wurden. Im vorliegenden CMR-Schadensfall: Hat TruckMind eine Routenempfehlung gegeben, die zu dem Halt bei Bourg-en-Bresse geführt hat? Kann die KI für den Standort des Halts mitverantwortlich sein?

**(c) Haftung für KI-Entscheidungen:** Nach dem Entwurf der KI-Haftungsrichtlinie (KI-HaftungsRL, COM(2022) 496) kann der Nutzer eines KI-Systems unter Umständen für fehlerhafte KI-Empfehlungen haftbar sein. Diese Richtlinie ist noch nicht in Kraft, der Gedanke ist aber bei der Haftungsabgrenzung zu berücksichtigen.

### 3.4 Datenschutz (DSGVO) — Fahrerdaten

TruckMind verarbeitet GPS-Daten, Tachographendaten und Lenk- und Ruhezeitdaten der Fahrer (personenbezogene Daten i.S.d. Art. 4 Nr. 1 DSGVO). Schwarmstedt hat als Arbeitgeber (Controller nach Art. 4 Nr. 7 DSGVO):
- Informationspflicht nach Art. 13 DSGVO gegenüber Fahrern erfüllt? → zu prüfen
- Auftragsverarbeitungsvertrag (AVV) mit TruckMind Solutions GmbH abgeschlossen? → nach Auskunft Funkbruch: noch nicht abgeschlossen (**dringlicher Handlungsbedarf**)

---

## 4. Empfehlungspaket Digital-Compliance

| Maßnahme | Priorität | Frist |
|---|---|---|
| eCMR-Integration mit Temperaturlogger DataTrack (API-Anbindung) | Hoch | Q3 2026 |
| Vollständige Tachographen-Daten-Routine (tägl. Download) | Hoch | Sofort |
| AVV mit TruckMind Solutions GmbH | Sehr hoch | 30. April 2026 |
| Fahrerinformation zu TruckMind (Transparenz KI-VO) | Mittel | 30. April 2026 |
| Sanktionslisten-Screening-System (s. Akte 09) | Sehr hoch | Sofort |
| Revision Subunternehmerprüfungsprotokoll (GDP, GüKG) | Hoch | Q2 2026 |
| eCMR-Vollständigkeitsprüfung (Unterzeichnungsroutine) | Mittel | Q2 2026 |

---

## 5. Relevanz für das Hauptverfahren LG Hannover

Die digitalen Compliance-Lücken sind für das Hauptverfahren mittelbar relevant:

- MediVita SE könnte argumentieren, dass die fehlende eCMR-Integration ein Indiz für mangelnde GDP-Konformität des Transports ist
- Lückenhafte Tachographen-Protokollierung erschwert die Verteidigung gegen den Art. 29-Vorwurf
- TruckMind-Protokolldaten könnten als Beweismittel dienen (Routenplanung, Haltepositionen)

**Empfehlung:** TruckMind-Protokolldaten für den 12./14. Januar 2026 sofort sichern (Beweissicherung).
