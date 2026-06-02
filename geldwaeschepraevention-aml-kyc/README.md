# Geldwäscheprävention, AML und KYC

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`geldwaeschepraevention-aml-kyc`) | [`geldwaeschepraevention-aml-kyc.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/geldwaeschepraevention-aml-kyc.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Kanzlei Sandhof & Partner — AML/KYC-Versäumnisse Amrum — Strafverteidigung** (`aml-kyc-immobilienkanzlei-sandhof-amrum-russisches-vermoegen`) | [Gesamt-PDF lesen](../testakten/aml-kyc-immobilienkanzlei-sandhof-amrum-russisches-vermoegen/gesamt-pdf/aml-kyc-immobilienkanzlei-sandhof-amrum-russisches-vermoegen_gesamt.pdf) | [`testakte-aml-kyc-immobilienkanzlei-sandhof-amrum-russisches-vermoegen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-aml-kyc-immobilienkanzlei-sandhof-amrum-russisches-vermoegen.zip) |
| **Akte Geldwäscheprävention, AML und KYC: Musterholding GmbH** (`geldwaesche-aml-kyc-musterholding`) | [Gesamt-PDF lesen](../testakten/geldwaesche-aml-kyc-musterholding/gesamt-pdf/geldwaesche-aml-kyc-musterholding_gesamt.pdf) | [`testakte-geldwaesche-aml-kyc-musterholding.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-geldwaesche-aml-kyc-musterholding.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Großes, freistehendes Plugin für Geldwäscheprävention, AML/CFT, KYC, GwG-Risikomanagement, wirtschaftlich Berechtigte, PEP, Sanktionsscreening, Verdachtsmeldungen, Transparenzregister, interne Sicherungsmaßnahmen, Schulung, Audit, Behördenverfahren, Bußgeld und Reputationskrisen.

Dieses Plugin ist **vollständig freistehend**. Es benötigt keine anderen Plugins, keine externen Agenten und keine besondere Kanzlei- oder Compliance-Software. Wenn kein KYC-Tool, Screening-Tool, goAML-Zugang, Transparenzregisterzugang, CRM, ERP oder DMS angeschlossen ist, arbeitet es mit manuellen Uploads oder einem ausdrücklich markierten Simulationsmodus.

### Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **Musterholding (Geldwaesche AML/KYC)** | [testakte-geldwaesche-aml-kyc-musterholding.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-geldwaesche-aml-kyc-musterholding.zip) |

## Schnellstart

1. Plugin aktivieren oder ZIP aus dem Release installieren.
2. Neue Sache mit `geldwaesche-kommandocenter` starten.
3. Branche, Mandantenrolle, Kunde, Produkt, Länderbezug und Transaktion beschreiben.
4. KYC-Unterlagen, Registerdaten, Screening-Treffer, Transaktionsdaten oder Richtlinien hochladen oder simulieren.
5. Am Ende immer das Qualitätstor verlangen: Quellenstand, KYC/UBO/PEP/Sanktionen, Risikoampel, Freigabe, Stop/Freeze/Exit, Verdachtsmeldung, Aufbewahrung und nächste Schritte.

## Enthaltene Skills

- `geldwaesche-kommandocenter` - AML/KYC-Kommandocenter
- `geldwaesche-verpflichteten-check` - Verpflichtetenstatus nach GwG
- `geldwaesche-risikoanalyse-unternehmen` - Unternehmensweite Risikoanalyse
- `geldwaesche-sicherungsmassnahmen-icp` - Interne Sicherungsmaßnahmen und ICP
- `geldwaesche-kyc-onboarding` - KYC-Onboarding und Kundenprüfung
- `geldwaesche-ubo-wirtschaftlich-berechtigte` - Wirtschaftlich Berechtigte und UBO
- `geldwaesche-pep-hochrisikoland` - PEP, Hochrisikoland und verstärkte Sorgfalt
- `geldwaesche-sanktionsscreening` - Sanktionslistenprüfung und Embargoabgleich
- `geldwaesche-transaktionsmonitoring` - Transaktionsmonitoring und Red Flags
- `geldwaesche-verdachtsmeldung-fiu-goaml` - Verdachtsmeldung an FIU/goAML
- `geldwaesche-transaktionsstopp-freeze` - Transaktionsstopp, Freeze und Exit
- `geldwaesche-transparenzregister` - Transparenzregister und Unstimmigkeitsmeldung
- `geldwaesche-immobilien-gueterhaendler` - Immobilien, Güterhandel und Nichtfinanzsektor
- `geldwaesche-krypto-zahlungsdienstleister` - Krypto, Zahlungsdienste und FinTech
- `geldwaesche-gruppenweite-compliance` - Gruppenweite Compliance und Outsourcing
- `geldwaesche-schulung-awareness` - Schulung und Awareness
- `geldwaesche-audit-internal-revision` - Audit und interne Revision
- `geldwaesche-behoerdenverfahren` - Aufsicht, Prüfung und Behördenverfahren
- `geldwaesche-bussgeld-reputation` - Bußgeld, Haftung und Reputation
- `geldwaesche-datenqualitaet-register` - Datenqualität, Register und Screening-Tools
- `geldwaesche-simulation-testlauf` - AML/KYC-Simulationsmodus

## Vorlagen

- `assets/templates/aml-kyc-mandatskarte.md` - AML/KYC-Mandatskarte
- `assets/templates/verpflichtetenstatus-check.md` - Verpflichtetenstatus-Check
- `assets/templates/unternehmens-risikoanalyse.md` - Unternehmensweite Risikoanalyse
- `assets/templates/risiko-scoring-modell.md` - Risikoscoring-Modell
- `assets/templates/kyc-onboardingbogen.md` - KYC-Onboardingbogen
- `assets/templates/ubo-ermittlungslog.md` - UBO-Ermittlungslog
- `assets/templates/pep-hochrisikoland-check.md` - PEP- und Hochrisikoland-Check
- `assets/templates/sanktionslisten-trefferlog.md` - Sanktionslisten-Trefferlog
- `assets/templates/enhanced-due-diligence-plan.md` - Enhanced-Due-Diligence-Plan
- `assets/templates/transaktionsmonitoring-alert.md` - Transaktionsmonitoring-Alertkarte
- `assets/templates/verdachtsmeldung-goaml-entwurf.md` - Verdachtsmeldung-goAML-Entwurf
- `assets/templates/transaktionsstopp-freeze-plan.md` - Transaktionsstopp- und Freeze-Plan
- `assets/templates/transparenzregister-unstimmigkeit.md` - Transparenzregister- und Unstimmigkeitslog
- `assets/templates/interne-sicherungsmassnahmen-icp.md` - Interne Sicherungsmaßnahmen und ICP
- `assets/templates/geldwaeschebeauftragter-rollenkarte.md` - Geldwäschebeauftragter-Rollenkarte
- `assets/templates/schulungsplan-awareness.md` - Schulungs- und Awarenessplan
- `assets/templates/audit-testplan.md` - Audit- und Stichprobenplan
- `assets/templates/behoerdenverfahren-fristen.md` - Behördenverfahren- und Fristenplan
- `assets/templates/bussgeld-remediation-plan.md` - Bußgeld- und Remediationplan
- `assets/templates/presse-qanda-reputation.md` - Presse-Q&A und Reputationskarte
- `assets/templates/datenqualitaet-registerabgleich.md` - Datenqualitäts- und Registerabgleich
- `assets/templates/simulatormodus-tageslauf.md` - AML/KYC-Simulationstag

## Offizielle Startquellen

- [GwG auf gesetze-im-internet](https://www.gesetze-im-internet.de/gwg_2017/)
- [GwG § 5 Risikoanalyse](https://www.gesetze-im-internet.de/gwg_2017/__5.html)
- [GwG § 10 Allgemeine Sorgfaltspflichten](https://www.gesetze-im-internet.de/gwg_2017/__10.html)
- [GwG § 43 Meldepflicht](https://www.gesetze-im-internet.de/gwg_2017/__43.html)
- [BaFin Geldwäscheprävention und AuA](https://www.bafin.de/DE/Aufsicht/Geldwaeschepraevention/Rechtsquellen/BaFin_Vorgaben/BaFin_Vorgaben_node.html)
- [FIU goAML Portal](https://goaml.fiu.bund.de/home)
- [Zoll/FIU Verdachtsmeldungen](https://www.zoll.de/DE/FIU/Fachliche-Informationen/Verdachtsmeldungen/verdachtsmeldungen_node.html)
- [Transparenzregister](https://www.transparenzregister.de/treg/ueberuns)
- [EU-Sanktionsressourcen](https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/overview-sanctions-and-related-resources_en)
- [AMLA](https://www.amla.europa.eu/about-amla_en)
- [FATF Risk-Based Approach](https://www.fatf-gafi.org/en/publications/Fatfrecommendations/Risk-based-approach-banking-sector.html)

## Freistehende Leitplanken

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, wirtschaftlich Berechtigte, Zweck, Risiko und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-, Eigentums- und Kontrollprüfung.
- Keine Verdachtsmeldung ohne Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Fortführung einer Transaktion, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Rechtsannahmen: GwG, BaFin-/Länderhinweise, FIU/goAML, Transparenzregister, EU-Sanktionen, AMLA und FATF werden mit Abrufdatum geführt.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen.

## Download

- Plugin-ZIP: [geldwaeschepraevention-aml-kyc.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/geldwaeschepraevention-aml-kyc.zip)
- Akte: [testakte-geldwaesche-aml-kyc-musterholding.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-geldwaesche-aml-kyc-musterholding.zip)

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Geldwaeschepraevention AML KYC-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren... |
| `aml-kryptotransaktionen-mica-spezial` | Spezialfall Kryptotransaktionen und MiCA / Travel Rule: Identifizierung Kryptowallets, Reisedatenuebermittlung, schwellenfreie Pflichten. Pruefraster fuer CASP. |
| `aml-kyc-onboarding-bauleiter` | Bauleiter KYC-Onboarding: Identifizierung natuerliche und juristische Personen, wirtschaftlich Berechtigter, PEP-Pruefung, Sanktionslistenabgleich. Pruefraster fuer Verpflichtete. |
| `aml-trade-based-money-laundering-spezial` | Spezialfall Trade-Based-Money-Laundering: Over- und Underinvoicing, mehrfache Rechnungsstellung, Phantomgueter. Pruefraster fuer Handelsfinanzierung. |
| `aml-verdachtsmeldung-fiu-leitfaden` | Leitfaden Verdachtsmeldung an FIU: goAML, Schwellen, Tippoff-Verbot, Schutz der Mitarbeitenden. Pruefraster fuer Geldwaeschebeauftragten. |
| `geldwaesche-audit-internal-revision` | Interne Revision und Audit der AML/KYC-Kontrollen nach GwG. Anwendungsfall Compliance-Beauftragter oder externer Prüfer will AML-Kontrollsystem auf Wirksamkeit prüfen. Normen § 4 GwG interne Sicherungsmassnahmen § 6 GwG Risikomanagement... |
| `geldwaesche-behoerdenverfahren` | Begleitung von Behoerdenverfahren BaFin-Prüfungen FIU-Nachfragen und Massnahmenbescheiden. Anwendungsfall Aufsichtsbehoerde hat Auskunftsersuchen gestellt oder Vor-Ort-Prüfung angekündigt. Normen § 51 GwG Aufsichtsrecht § 52 GwG Bußgelde... |
| `geldwaesche-bussgeld-reputation` | Strukturierung von Bußgeldriskien Geschäftsleiterhaftung und Reputationsschaeden bei GwG-Verstoessen. Anwendungsfall Bußgeldbescheid nach GwG ist eingegangen oder negative Berichterstattung droht. Normen § 52 GwG Bußgelder bis 5 Mio EUR... |
| `geldwaesche-datenqualitaet-register` | Prüft Datenqualitaet im KYC-System und Transparenzregister-Abgleich. Anwendungsfall KYC-Daten enthalten Dubletten fehlerhafte Schreibweisen oder unvollständige UBO-Daten. Normen § 11 GwG Identifizierungspflicht § 20 GwG Transparenzregist... |
| `geldwaesche-gruppenweite-compliance` | Gruppenweite AML/KYC-Policies und Steuerung von Tochtergesellschaften und Dienstleistern. Anwendungsfall Muttergesellschaft will gruppenweite AML-Compliance sicherstellen und Tochtergesellschaften einbinden. Normen § 9 GwG Gruppenweite P... |
| `geldwaesche-immobilien-gueterhaendler` | AML/KYC-Prüfung für Immobilienmakler Gueterhaendler Kunsthandel Edelmetalle und sonstige Nichtfinanzunternehmen. Anwendungsfall Makler oder Gueterhaendler will prüfen ob GwG-Pflichten bestehen und wie KYC-Prozesse auszugestalten sind. No... |
| `geldwaesche-kommandocenter` | Kommandocenter für alle Geldwäsche- KYC- Sanktions- und Behoerdenfaelle vom Intake bis zum Massnahmenplan. Anwendungsfall Compliance-Beauftragter oder Anwalt erhaelt neuen Fall und muss schnell den richtigen Workflow starten. Normen GwG... |
| `geldwaesche-krypto-zahlungsdienstleister` | AML/KYC-Prüfung für Krypto-Assets Wallets Travel Rule und Zahlungsdienstleister. Anwendungsfall Krypto-Transaktion soll bewertet oder Krypto-Dienstleister muss KYC-Prozess aufsetzen. Normen § 2 Abs. 1 Nr. 10b GwG Kryptowertehandel Verord... |
| `geldwaesche-kyc-onboarding` | KYC-Onboarding neuer Kunden mit Identifizierung Risikoklassifizierung und Freigabe nach GwG. Anwendungsfall neue Geschäftsbeziehung soll aufgenommen werden und GwG-Identifizierung muss durchgeführt werden. Normen §§ 10 11 GwG allgemeine... |
| `geldwaesche-pep-hochrisikoland` | Verstaerkte KYC-Prüfung für PEP politisch exponierte Personen Hochrisikolaender und komplexe Strukturen nach GwG. Anwendungsfall Kunde ist PEP oder kommt aus Hochrisikoland und verstaerkte Sorgfaltspflichten greifen. Normen § 15 GwG vers... |
| `geldwaesche-risikoanalyse-unternehmen` | Risikobasierte AML/CFT-Risikoanalyse nach § 5 GwG für Verpflichtete. Anwendungsfall Unternehmen muss gesetzlich vorgeschriebene Risikoanalyse erstellen oder aktualisieren. Normen § 5 GwG Risikoanalyse § 6 GwG interne Sicherungsmassnahmen... |
| `geldwaesche-sanktionsscreening` | Sanktionsscreening von Kunden Transaktionen und Beteiligten gegen EU-US- und UN-Sanktionslisten. Anwendungsfall neues Geschäft soll abgeschlossen oder Transaktion freigegeben werden. Normen EU-Verordnungen 2580/2001 881/2002 Russland-VO... |
| `geldwaesche-schulung-awareness` | Zielgruppengerechte AML/KYC-Schulungen und Awareness-Massnahmen nach § 6 Abs. 2 Nr. 6 GwG. Anwendungsfall jaehrliche Pflichtschulung muss durchgeführt oder neue Mitarbeiter eingearbeitet werden. Normen § 6 Abs. 2 Nr. 6 GwG Schulungspflic... |
| `geldwaesche-sicherungsmassnahmen-icp` | Aufbau und Haertung interner Sicherungsmassnahmen ICP nach § 6 GwG. Anwendungsfall Verpflichteter muss ICP aufbauen oder bestehendes Kontrollsystem verbessern. Normen § 4 GwG Bestellung GwG-Beauftragter § 6 GwG interne Massnahmen § 7 GwG... |
| `geldwaesche-simulation-testlauf` | Simulation eines Compliance-Arbeitstags mit Onboarding Alerts Verdachtsprüfung und Behoerdenfragen. Anwendungsfall Team will GwG-Workflows trainieren oder Plugin demonstrieren. Deckt Onboarding Alert UBO-Luecke Sanktionshit Verdachtsprüf... |
| `geldwaesche-transaktionsmonitoring` | Erkennung auffälliger Transaktionsmuster und Red-Flags im Zahlungsverkehr nach GwG. Anwendungsfall Bank oder Zahlungsdienstleister will Transaktion auf Geldwäscherisiko prüfen. Normen § 10 Abs. 1 Nr. 5 GwG Transaktionsmonitoring § 43 GwG... |
| `geldwaesche-transaktionsstopp-freeze` | Transaktionsstopp Kontoeinfrierung und Nichtdurchführung bei Sanktions- oder Verdachtstreffer. Anwendungsfall Transaktion muss gestoppt oder Konto eingefroren werden weil Sanktionstreffer oder konkreter Verdacht vorliegt. Normen § 40 GwG... |
| `geldwaesche-transparenzregister` | Transparenzregister-Einsicht Abgleich und Unstimmigkeitsmeldung nach GwG. Anwendungsfall wirtschaftlich Berechtigte muessen im Transparenzregister geprüft oder Unstimmigkeit gemeldet werden. Normen § 20 GwG Meldepflicht § 23 GwG Einsicht... |
| `geldwaesche-ubo-wirtschaftlich-berechtigte` | Ermittlung wirtschaftlich Berechtigter UBO Kontrollketten und Trust-Stiftungsstrukturen nach GwG. Anwendungsfall neue Geschäftsbeziehung mit Unternehmen und wirtschaftlich Berechtigte muessen identifiziert werden. Normen § 3 GwG wirtscha... |
| `geldwaesche-verdachtsmeldung-fiu-goaml` | Vorbereitung und Einreichung von Verdachtsmeldungen nach § 43 GwG über goAML-Portal an die FIU. Anwendungsfall Sachverhalt mit Verdacht auf Geldwäsche oder Terrorismusfinanzierung ist festgestellt und Meldung muss erstattet werden. Norme... |
| `geldwaesche-verpflichteten-check` | Prüft ob und in welcher Rolle ein Unternehmen oder Berufsstraeger nach GwG verpflichtet ist. Anwendungsfall Unternehmen oder Kanzlei will wissen ob GwG-Pflichten bestehen und welche Konsequenzen das hat. Normen § 2 GwG Verpflichtetenkata... |
| `spezial-awareness-zahlen-schwellen-und-berechnung` | Awareness: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-behoerdenverfahren-schriftsatz-brief-und-memo-bausteine` | Behoerdenverfahren: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-chronologie-sonderfall-und-edge-case` | Chronologie: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-geldwaesche-verhandlung-vergleich-und-eskalation` | Geldwaesche: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-geldwaeschepraevention-erstpruefung-und-mandatsziel` | Geldwaeschepraevention: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-goaml-risikoampel-und-gegenargumente` | Goaml: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-gwg-tatbestand-beweis-und-belege` | GwG: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-kommandocenter-compliance-dokumentation-und-akte` | Kommandocenter: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-livecheck-red-team-und-qualitaetskontrolle` | Livecheck: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsquellen-formular-portal-und-einreichung` | Rechtsquellen: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-risikoanalyse-fristen-form-und-zustaendigkeit` | Risikoanalyse: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-risikoanalyse-und-verdachtsmeldeweiche` | GwG-Risikoanalyse und Verdachtsmeldeweiche: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-sanktionen-dokumentenmatrix-und-lueckenliste` | Sanktionen: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-schulung-livequellen-und-rechtsprechungscheck` | Schulung: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-simulation-mandantenkommunikation-entscheidungsvorlage` | Simulation: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-testlauf-beweislast-und-darlegungslast` | Testlauf: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-transaktionsmonitoring-international-schnittstellen` | Transaktionsmonitoring: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-transparenzregister-behoerden-gericht-und-registerweg` | Transparenzregister: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-verdachtsmeldung-mehrparteien-konflikt-und-interessen` | Verdachtsmeldung: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin geldwaeschepraevention-aml-kyc: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin geldwaeschepraevention-aml-kyc: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin geldwaeschepraevention-aml-kyc: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin geldwaeschepraevention-aml-kyc: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin geldwaeschepraevention-aml-kyc: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin geldwaeschepraevention-aml-kyc: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin geldwaeschepraevention-aml-kyc: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin geldwaeschepraevention-aml-kyc: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin geldwaeschepraevention-aml-kyc: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
