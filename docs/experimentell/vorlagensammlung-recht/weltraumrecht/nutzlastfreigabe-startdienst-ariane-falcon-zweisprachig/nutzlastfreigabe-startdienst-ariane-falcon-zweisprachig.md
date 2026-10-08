# Nutzlastfreigabedossier für Ariane- oder Falcon-Startdienst | Payload Release Dossier for an Ariane or Falcon Launch Service

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Freigabebestandteil, vor Übermittlung entfernen]

Diese Vorlage ersetzt nicht die technische, exportkontrollrechtliche und vertragliche Eigenleistung. Sie liefert das Freigabegerüst, nicht die Startdienstspezifikation. Der Anwender bringt das aktuelle Interface Control Document, das Safety Data Package, Testnachweise und behördliche Freigaben; die Vorlage bringt Abnahmepunkte, offene-Punkte-Logik und die unbedingt zu prüfenden Stellen.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

An den

[zuständigen Startdienstleister]

## Zweisprachiges Freigabedossier | Bilingual Release Dossier

| Deutsch | English |
|---|---|
| **1. Mission und Parteien** | **1. Mission and Parties** |
| 1.1 Mission: [Missionsname und Kennung]. Startdienst: [Ariane-Konfiguration / Falcon-Konfiguration / anderer Träger und Konfiguration]. Startplatz: [Startplatz]. Geplanter Starttermin oder Startzeitraum: [Datum oder Zeitraum]. | 1.1 Mission: [mission name and identifier]. Launch service: [Ariane configuration / Falcon configuration / other launch vehicle and configuration]. Launch site: [launch site]. Scheduled launch date or launch window: [date or period]. |
| 1.2 Nutzlasteigentümer: [Firma, Rechtsform, Sitz und Register]. Nutzlastintegrator: [Firma und Rolle]. Startdienstleister: [Firma und Rolle]. Betreiber nach Aussetzung: [Firma und Leitstelle]. | 1.2 Payload owner: [company, legal form, registered office and register]. Payload integrator: [company and role]. Launch services provider: [company and role]. Post-deployment operator: [company and control centre]. |
| 1.3 Dieses Dossier dokumentiert die Freigabereife der Nutzlast [Bezeichnung und Seriennummer] in der Konfiguration [Konfigurationskennung]. Maßgebliche Bezugsdokumente sind in Anlage 1 mit Titel, Dokumentnummer, Revision und Rangfolge aufgeführt. | 1.3 This dossier records the release readiness of payload [designation and serial number] in configuration [configuration identifier]. The governing documents are listed in Annex 1 by title, document number, revision and order of precedence. |
| **2. Freigabegegenstand und Vorbehalte** | **2. Scope of Release and Reservations** |
| 2.1 Freigegeben wird ausschließlich die in Anlage 2 konfigurierte Nutzlast einschließlich [Adapter / Dispenser / Separation System / Remove-Before-Flight-Elemente / Ground Support Equipment]. | 2.1 Release is limited to the payload configured in Annex 2, including [adapter / dispenser / separation system / remove-before-flight items / ground support equipment]. |
| 2.2 [Variante A — abschließende Freigabe: Sämtliche zwingenden Nachweise sind angenommen und alle sicherheits- und missionskritischen Punkte geschlossen.; Variante B — bedingte Freigabe: Die Freigabe steht unter den in Anlage 10 bezeichneten aufschiebenden Bedingungen. Ein Start ist erst nach dokumentierter Schließung zulässig.] | 2.2 [Option A — final release: All mandatory evidence has been accepted and all safety-critical and mission-critical items have been closed.; Option B — conditional release: Release is subject to the conditions precedent listed in Annex 10. Launch is not authorised until closure has been documented.] |
| 2.3 Die Freigabe erfasst keine Änderung nach dem Konfigurationsstichtag [Datum und Uhrzeit]. Hardware-, Software-, Stoff-, Batterie-, Druck-, Verkabelungs-, Massen- oder Dokumentänderungen bedürfen einer erneuten Folgenprüfung. | 2.3 This release does not cover changes made after the configuration freeze at [date and time]. Any hardware, software, substance, battery, pressure, wiring, mass or document change requires a new impact assessment. |
| **3. Masse, Geometrie und mechanische Schnittstellen** | **3. Mass, Geometry and Mechanical Interfaces** |
| 3.1 Startmasse: [Masse]. Abmessungen und dynamische Hüllkurve: [Werte und Zeichnungsreferenz]. Schwerpunkt und Trägheitstensor: [Werte, Toleranzen und Referenzsystem]. | 3.1 Launch mass: [mass]. Dimensions and dynamic envelope: [values and drawing reference]. Centre of gravity and inertia tensor: [values, tolerances and reference frame]. |
| 3.2 Die mechanische Schnittstelle entspricht [Interface Control Document, Abschnitt und Revision]. Verbindungselemente, Drehmomente, Sicherungen und zulässige Lasten sind in Anlage 3 nachgewiesen. | 3.2 The mechanical interface complies with [Interface Control Document, section and revision]. Fasteners, torque values, locking features and allowable loads are substantiated in Annex 3. |
| 3.3 Das Separation System [Bezeichnung] wurde in der Flugkonfiguration [Konfiguration] geprüft. Auslösesignal, Redundanz, Freisetzungsenergie, Tip-off, Kollisionsfreiheit und Statusrückmeldung entsprechen [Nachweis]. | 3.3 The [designation] separation system was tested in flight configuration [configuration]. The initiation signal, redundancy, release energy, tip-off, collision clearance and status feedback comply with [evidence]. |
| **4. Elektrische Schnittstelle, Software und Funk** | **4. Electrical Interface, Software and Radio Frequency** |
| 4.1 Versorgung, Massebezug, Steckverbinder, Pinbelegung, Einschaltfolge und Leistungsgrenzen entsprechen [Dokument und Revision]. Schutz gegen unbeabsichtigte Aktivierung besteht durch [Inhibits und Prüfverfahren]. | 4.1 Power supply, grounding, connectors, pin allocation, power-up sequence and power limits comply with [document and revision]. Protection against inadvertent activation is provided by [inhibits and verification method]. |
| 4.2 Flugsoftware und programmierbare Logik tragen die freigegebenen Stände [Versionen und Prüfsummen]. Startplatzänderungen sind auf [zulässige Parameter] beschränkt und werden protokolliert. | 4.2 Flight software and programmable logic are at the released baselines [versions and checksums]. Launch-site changes are limited to [permitted parameters] and are logged. |
| 4.3 Sender, Empfänger und Oszillatoren sind während Transport, Integration und Start [deaktiviert / in dem genehmigten Modus betrieben]. Frequenzen, Leistung, Aktivierungslogik und Frequenzzuteilung ergeben sich aus Anlage 4. | 4.3 Transmitters, receivers and oscillators remain [disabled / operated in the authorised mode] during transport, integration and launch. Frequencies, power levels, activation logic and frequency authorisations are set out in Annex 4. |
| **5. Gefahrstoffe und gespeicherte Energie** | **5. Hazardous Materials and Stored Energy** |
| 5.1 Anlage 5 erfasst vollständig Treibstoffe, Druckgase, Batterien, pyrotechnische Gegenstände, Laser, radioaktive Quellen, kryogene Stoffe, biologische Materialien, starke Magnete und sonstige gespeicherte Energie. Nicht aufgeführte Gefahrenträger sind nicht zugelassen. | 5.1 Annex 5 provides a complete inventory of propellants, pressurised gases, batteries, pyrotechnic devices, lasers, radioactive sources, cryogenic substances, biological materials, strong magnets and other stored energy. Hazard sources not listed are not accepted. |
| 5.2 Behälter, Ventile, Leitungen und Batterien wurden nach [Anforderung] qualifiziert. Maximalwerte, Sicherheitsfaktoren, Leckraten, Überwachungsgrößen und Entlastungswege sind in Anlage 5 angegeben. | 5.2 Vessels, valves, lines and batteries have been qualified to [requirement]. Maximum values, safety factors, leak rates, monitored parameters and relief paths are specified in Annex 5. |
| 5.3 Remove-Before-Flight-Elemente und Sicherheitsbarrieren sind nummeriert, in der Startplatzprozedur verortet und einer verantwortlichen Person zugewiesen. Entfernung oder Umschaltung wird im Close-out-Protokoll bestätigt. | 5.3 Remove-before-flight items and safety barriers are numbered, identified in the launch-site procedure and assigned to a responsible person. Removal or switching is confirmed in the close-out record. |
| **6. Umwelt- und Qualifikationstests** | **6. Environmental and Qualification Testing** |
| 6.1 Die Nutzlast wurde gegen die maßgeblichen Akzeptanz- oder Qualifikationspegel für [Vibration, Schock, Akustik, Thermovakuum, elektromagnetische Verträglichkeit und sonstige Umwelt] geprüft. | 6.1 The payload has been tested against the applicable acceptance or qualification levels for [vibration, shock, acoustics, thermal vacuum, electromagnetic compatibility and other environments]. |
| 6.2 Testkonfiguration, Grenzwerte, Abweichungen und Ergebnisse sind in Anlage 6 rückverfolgbar. Schäden, Übertest, Notching, Testunterbrechungen oder Nacharbeit wurden durch [Material Review Board oder gleichwertige Stelle] entschieden. | 6.2 Test configuration, limits, deviations and results are traceable in Annex 6. Damage, over-testing, notching, test interruptions or rework were dispositioned by [Material Review Board or equivalent body]. |
| 6.3 [OPTIONAL — nur bei einer Analyse anstelle eines Tests] Der Nachweis für [konkrete Anforderung] wird durch die validierte Analyse [Bezeichnung der Analyse] geführt. Modellkorrelation, Randbedingungen, Unsicherheiten und Sicherheitsmargen sind dokumentiert. | 6.3 [OPTIONAL — only where analysis is used in lieu of testing] Compliance with [specific requirement] is demonstrated by validated analysis [analysis designation]. Model correlation, boundary conditions, uncertainties and margins of safety are documented. |
| **7. Exportkontrolle, Zoll und Transport** | **7. Export Control, Customs and Transport** |
| 7.1 Güter, Software und Technologie sind in Anlage 7 positionsbezogen klassifiziert. Erforderliche Ausfuhr-, Verbringungs-, Reexport- und Einfuhrgenehmigungen liegen vor und decken Empfänger, Endverwendung, Werte, Mengen und Laufzeit ab. | 7.1 Goods, software and technology are classified item by item in Annex 7. All required export, transfer, re-export and import licences are in place and cover the consignee, end use, value, quantity and validity period. |
| 7.2 Transportkonfiguration, Verpackung, Gefahrgutklassifizierung, Zollverfahren, Carnet oder vorübergehende Verwendung, Frachtführer und Übergabepunkte entsprechen dem Logistikplan [Referenz]. | 7.2 The transport configuration, packaging, dangerous goods classification, customs procedure, carnet or temporary admission, carriers and custody transfer points comply with logistics plan [reference]. |
| **8. Regulatorische und versicherungsbezogene Nachweise** | **8. Regulatory and Insurance Evidence** |
| 8.1 Der Status von Frequenzzuteilung, ITU-Verfahren, SatDSiG, Registrierung, Datenschutz, Exportkontrolle und sonstigen missionsbezogenen Genehmigungen ist in Anlage 8 mit Behörde, Aktenzeichen, Umfang, Laufzeit und offenen Auflagen dokumentiert. | 8.1 The status of frequency authorisation, ITU filing, SatDSiG, registration, data protection, export control and other mission-specific approvals is documented in Annex 8 by authority, reference, scope, validity and outstanding conditions. |
| 8.2 Versicherungen für Transport, Vorstart, Start, In-Orbit-Test und Betrieb bestehen nach [Policen und Deckungszeiträume]. Ausschlüsse, Selbstbehalte und Meldepflichten, die die Startfreigabe berühren, sind [keine / wie folgt]. | 8.2 Insurance for transport, pre-launch, launch, in-orbit testing and operations is in place under [policies and coverage periods]. Exclusions, deductibles and notification obligations affecting launch release are [none / as follows]. |
| **9. Startplatzbetrieb und Close-out** | **9. Launch-Site Operations and Close-out** |
| 9.1 Der Startplatzablauf bezeichnet Wareneingang, Lagerung, Integration, Betankung oder Ladung, elektrische Tests, Softwarezugriff, Remove-Before-Flight-Schritte, Fairing-Schluss, Zugangssperre und Übergabe an den Startdienst. | 9.1 The launch-site flow identifies receipt, storage, integration, fuelling or charging, electrical testing, software access, remove-before-flight steps, fairing closure, access restrictions and handover to the launch services provider. |
| 9.2 Nur die in Anlage 9 benannten Personen dürfen Eingriffe vornehmen. Jede Tätigkeit verwendet eine freigegebene Prozedur, dokumentiert Ist-Werte und endet mit unabhängiger Kontrolle. | 9.2 Only the personnel listed in Annex 9 may perform interventions. Each activity uses an approved procedure, records as-performed values and concludes with independent verification. |
| 9.3 Der finale Close-out bestätigt Konfiguration, Software, Batteriestatus, Druck, Leckfreiheit, Sicherungen, Funkzustand, Redlines, offene Punkte und Übergabezeit. | 9.3 Final close-out confirms configuration, software, battery status, pressure, leak tightness, safety devices, RF status, redlines, open items and handover time. |
| **10. Abweichungen und offene Punkte** | **10. Deviations and Open Items** |
| 10.1 Jede Abweichung nennt Anforderung, Ist-Zustand, Ursache, technische und sicherheitsbezogene Folge, Kompensation, Laufzeit und Genehmiger. Eine konkludente Freigabe durch Fortsetzung der Integration ist ausgeschlossen. | 10.1 Each deviation identifies the requirement, actual condition, cause, technical and safety impact, compensating measures, validity period and approval authority. Continued integration does not constitute implied acceptance. |
| 10.2 Anlage 10 trennt Startverhinderer, bedingte Punkte und nach Start zu schließende Punkte. Jeder Punkt trägt Eigentümer, Nachweis, Fälligkeit und Eskalationsschwelle. | 10.2 Annex 10 separates launch constraints, conditional items and post-launch items. Each item has an owner, closure evidence, due date and escalation threshold. |
| **11. Freigabeentscheidung** | **11. Release Decision** |
| 11.1 Der Nutzlasteigentümer bestätigt, dass die Angaben vollständig sind und der freigegebenen Flugkonfiguration entsprechen. | 11.1 The payload owner confirms that the information is complete and reflects the released flight configuration. |
| 11.2 Der Nutzlastintegrator bestätigt die Annahme der Schnittstellen- und Integrationsnachweise für den in Abschnitt 2 bezeichneten Umfang. | 11.2 The payload integrator confirms acceptance of the interface and integration evidence for the scope defined in Section 2. |
| 11.3 [Final Go] Die Nutzlast ist für die Übergabe an den Startdienst freigegeben. [Conditional Go] Die Nutzlast ist nach dokumentierter Schließung der Bedingungen [Nummern der Bedingungen] freigegeben. [No-Go] Die Nutzlast ist wegen [konkreter Startverhinderer] nicht freigegeben. Nicht gewählte Alternativen sind zu streichen. | 11.3 [Final Go] The payload is released for handover to the launch services provider. [Conditional Go] The payload is released upon documented closure of conditions [condition numbers]. [No-Go] The payload is not released due to [specific launch constraints]. Delete all options not selected. |
| **12. Sprache und Auslegung** | **12. Language and Interpretation** |
| 12.1 Die deutsche und die englische Fassung stehen nebeneinander. Bei Widersprüchen ist die deutsche Fassung maßgeblich, soweit der zugrunde liegende Vertrag keine abweichende wirksame Sprachregel enthält. | 12.1 The German and English versions are presented side by side. In the event of inconsistency, the German version prevails unless the underlying agreement contains a different valid language clause. |

## Freigaben | Approvals

| Nutzlasteigentümer | Payload Owner |
|---|---|
| [Ort und Datum] | [place and date] |
| [Unterschrift] | [signature] |
| [Name in Druckbuchstaben] | [name in block capitals] |
| [Funktion] | [title] |

| Nutzlastintegrator | Payload Integrator |
|---|---|
| [Ort und Datum] | [place and date] |
| [Unterschrift] | [signature] |
| [Name in Druckbuchstaben] | [name in block capitals] |
| [Funktion] | [title] |

| Startdienstleister | Launch Services Provider |
|---|---|
| [Ort und Datum] | [place and date] |
| [Unterschrift] | [signature] |
| [Name in Druckbuchstaben] | [name in block capitals] |
| [Funktion] | [title] |

## Anlagen | Annexes

| Deutsch | English |
|---|---|
| Anlage 1 — Bezugsdokumente und Rangfolge | Annex 1 — Governing Documents and Order of Precedence |
| Anlage 2 — Flugkonfiguration und Konfigurationsliste | Annex 2 — Flight Configuration and Configuration Item List |
| Anlage 3 — Mechanische Schnittstellen und Lastnachweise | Annex 3 — Mechanical Interfaces and Load Verification |
| Anlage 4 — Elektrik, Software und Funkstatus | Annex 4 — Electrical, Software and RF Status |
| Anlage 5 — Gefahrstoffe und gespeicherte Energie | Annex 5 — Hazardous Materials and Stored Energy |
| Anlage 6 — Umwelt- und Qualifikationstests | Annex 6 — Environmental and Qualification Testing |
| Anlage 7 — Export, Zoll und Logistik | Annex 7 — Export, Customs and Logistics |
| Anlage 8 — Genehmigungen und Versicherungen | Annex 8 — Approvals and Insurance |
| Anlage 9 — Startplatzprozeduren und Personal | Annex 9 — Launch-Site Procedures and Personnel |
| Anlage 10 — Abweichungen, Bedingungen und offene Punkte | Annex 10 — Deviations, Conditions and Open Items |

---

Lizenz: Apache-2.0 OR MIT.
