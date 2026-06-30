# Geldwäscheprävention, AML und KYC

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Freistehendes Plugin für Geldwäscheprävention, AML, KYC, GwG-Risikoanalyse, UBO, PEP, Sanktionen, FIU/goAML, Transparenzregister und Behördenverfahren.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`geldwaeschepraevention-aml-kyc.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/geldwaeschepraevention-aml-kyc.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/geldwaeschepraevention-aml-kyc/geldwaeschepraevention-aml-kyc-werkstatt.md" download><code>geldwaeschepraevention-aml-kyc-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/geldwaeschepraevention-aml-kyc/geldwaeschepraevention-aml-kyc-schnellstart.md" download><code>geldwaeschepraevention-aml-kyc-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Kanzlei Sandhof & Partner — AML/KYC-Versäumnisse Amrum — Strafverteidigung: [Gesamt-PDF](../testakten/aml-kyc-immobilienkanzlei-sandhof-amrum-russisches-vermoegen/gesamt-pdf/aml-kyc-immobilienkanzlei-sandhof-amrum-russisches-vermoegen_gesamt.pdf), [`testakte-aml-kyc-immobilienkanzlei-sandhof-amrum-russisches-vermoegen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-aml-kyc-immobilienkanzlei-sandhof-amrum-russisches-vermoegen.zip), [`testakte-aml-kyc-immobilienkanzlei-sandhof-amrum-russisches-vermoegen-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-aml-kyc-immobilienkanzlei-sandhof-amrum-russisches-vermoegen-einzelpdfs.zip); Akte Geldwäscheprävention, AML und KYC: Musterholding GmbH: [Gesamt-PDF](../testakten/geldwaesche-aml-kyc-musterholding/gesamt-pdf/geldwaesche-aml-kyc-musterholding_gesamt.pdf), [`testakte-geldwaesche-aml-kyc-musterholding.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-geldwaesche-aml-kyc-musterholding.zip), [`testakte-geldwaesche-aml-kyc-musterholding-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-geldwaesche-aml-kyc-musterholding-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Großes, freistehendes Plugin für Geldwäscheprävention, AML/CFT, KYC, GwG-Risikomanagement, wirtschaftlich Berechtigte, PEP, Sanktionsscreening, Verdachtsmeldungen, Transparenzregister, interne Sicherungsmaßnahmen, Schulung, Audit, Behördenverfahren, Bußgeld und Reputationskrisen.

Dieses Plugin ist **vollständig freistehend**. Es benötigt keine anderen Plugins, keine externen Agenten und keine besondere Kanzlei- oder Compliance-Software. Wenn kein KYC-Tool, Screening-Tool, goAML-Zugang, Transparenzregisterzugang, CRM, ERP oder DMS angeschlossen ist, arbeitet es mit manuellen Uploads oder einem ausdrücklich markierten Simulationsmodus.

#

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

- GwG auf gesetze-im-internet
- GwG § 5 Risikoanalyse
- GwG § 10 Allgemeine Sorgfaltspflichten
- GwG § 43 Meldepflicht
- BaFin Geldwäscheprävention und AuA
- FIU goAML Portal
- Zoll/FIU Verdachtsmeldungen
- Transparenzregister
- EU-Sanktionsressourcen
- AMLA
- FATF Risk-Based Approach

## Freistehende Leitplanken

- Keine KYC-Freigabe ohne dokumentierte Identifizierung, wirtschaftlich Berechtigte, Zweck, Risiko und offene Nachweise.
- Keine Sanktionsfreigabe ohne aktuelle Quellenprüfung, Alias-, Eigentums- und Kontrollprüfung.
- Keine Verdachtsmeldung ohne Sachverhaltskern, Belegliste, interne Freigabe und Dokumentation der Entscheidungsgründe.
- Keine Fortführung einer Transaktion, wenn Mittelherkunft, Sanktionshit oder Verdachtslage ungeklärt bleibt.
- Keine starren Rechtsannahmen: GwG, BaFin-/Länderhinweise, FIU/goAML, Transparenzregister, EU-Sanktionen, AMLA und FATF werden mit Abrufdatum geführt.
- Keine echten Mandats- oder Kundendaten in ungeprüfte Cloud- oder KI-Umgebungen.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 57 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aml-kryptotransaktionen-mica-spezial` | Spezialfall Kryptotransaktionen und MiCA / Travel Rule: Identifizierung Kryptowallets, Reisedatenuebermittlung, schwellenfreie Pflichten. Prüfraster für CASP im Geldwaeschepraevention Aml Kyc. |
| `aml-kyc-start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Geldwaeschepraevention AML KYC-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitspl... |
| `aml-trade-based-money-laundering-spezial` | Spezialfall Trade-Based-Money-Laundering: Over- und Underinvoicing, mehrfache Rechnungsstellung, Phantomgueter. Prüfraster für Handelsfinanzierung im Geldwaeschepraevention Aml Kyc. |
| `aml-verdachtsmeldung-fiu-leitfaden` | Leitfaden Verdachtsmeldung an FIU: goAML, Schwellen, Tippoff-Verbot, Schutz der Mitarbeitern. Prüfraster für Geldwaeschebeauftragten im Geldwaeschepraevention Aml Kyc. |
| `anschluss-routing` | Anschluss-Routing für Geldwäscheprävention AML/KYC: wählt den nächsten Spezial-Skill nach Engpass (Verdachtsmeldung unverzüglich § 43 GwG, KYC-Akte, Risk Assessment, Compliance-Manual), dokumentiert Router-Entscheidung mit Begründung. |
| `awareness-zahlen-schwellen-und-berechnung` | Awareness: Zahlen, Schwellenwerte und Berechnung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `behoerdenverfahren-schriftsatz-brief-und-memo-bausteine` | Behördenverfahren: Schriftsatz-, Brief- und Memo-Bausteine. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `dokumente-intake` | Dokumentenintake für Geldwäscheprävention AML/KYC: sortiert KYC-Akte, Risk Assessment, Compliance-Manual, prüft Datum, Absender, Frist und Beweiswert (Dokumente wirtschaftlich Berechtigter, Transaction Logs); markiert Lücken; berücksicht... |
| `einstieg-routing` | Einstieg, Triage und Routing für Geldwäscheprävention AML/KYC: ordnet Rolle (Verpflichteter (Bank, Anwalt, Notar), Kunde, FIU), markiert Frist (Verdachtsmeldung unverzüglich § 43 GwG), wählt Norm (GwG, FATF 40 Recommendations, EU-AMLD VI... |
| `geldwaesche-audit-internal-datenqualitaet` | Interne Revision und Audit der AML/KYC-Kontrollen nach GwG. Anwendungsfall Compliance-Beauftragter oder externer Prüfer will AML-Kontrollsystem auf Wirksamkeit prüfen. Normen § 4 GwG interne Sicherungsmassnahmen § 6 GwG Risikomanagement... |
| `geldwaesche-behoerdenverfahren` | Begleitung von Behördenverfahren BaFin-Prüfungen FIU-Nachfragen und Maßnahmenbescheiden. Anwendungsfall Aufsichtsbehoerde hat Auskunftsersuchen gestellt oder Vor-Ort-Prüfung angekündigt. Normen § 51 GwG Aufsichtsrecht § 52 GwG Bußgelder... |
| `geldwaesche-bussgeld-reputation` | Strukturierung von Bußgeldriskien Geschäftsleiterhaftung und Reputationsschaeden bei GwG-Verstoessen. Anwendungsfall Bußgeldbescheid nach GwG ist eingegangen oder negative Berichterstattung droht. Normen § 52 GwG Bußgelder bis 5 Mio EUR... |
| `geldwaesche-datenqualitaet-register` | Prüft Datenqualitaet im KYC-System und Transparenzregister-Abgleich. Anwendungsfall KYC-Daten enthalten Dubletten fehlerhafte Schreibweisen oder unvollständige UBO-Daten. Normen § 11 GwG Identifizierungspflicht § 20 GwG Transparenzregist... |
| `geldwaesche-gruppenweite-compliance` | Gruppenweite AML/KYC-Policies und Steuerung von Tochtergesellschaften und Dienstleistern. Anwendungsfall Muttergesellschaft will gruppenweite AML-Compliance sicherstellen und Tochtergesellschaften einbinden. Normen § 9 GwG Gruppenweite P... |
| `geldwaesche-immobilien-gueterhaendler` | AML/KYC-Prüfung für Immobilienmakler Gueterhaendler Kunsthandel Edelmetalle und sonstige Nichtfinanzunternehmen. Anwendungsfall Makler oder Gueterhaendler will prüfen ob GwG-Pflichten bestehen und wie KYC-Prozesse auszugestalten sind. No... |
| `geldwaesche-krypto-zahlungsdienstleister` | AML/KYC-Prüfung für Krypto-Assets Wallets Travel Rule und Zahlungsdienstleister. Anwendungsfall Krypto-Transaktion soll bewertet oder Krypto-Dienstleister muss KYC-Prozess aufsetzen. Normen § 2 Abs. 1 Nr. 10b GwG Kryptowertehandel Verord... |
| `geldwaesche-krypto-zahlungsdienstleister-kyc` | Kommandocenter für alle Geldwäsche- KYC- Sanktions- und Behördenfaelle vom Intake bis zum Maßnahmenplan. Anwendungsfall Compliance-Beauftragter oder Anwalt erhaelt neuen Fall und muss schnell den richtigen starten. Normen GwG gesamt § 43... |
| `geldwaesche-kyc-onboarding` | KYC-Onboarding neuer Kunden mit Identifizierung Risikoklassifizierung und Freigabe nach GwG. Anwendungsfall neue Geschäftsbeziehung soll aufgenommen werden und GwG-Identifizierung muss durchgeführt werden. Normen §§ 10 11 GwG allgemeine... |
| `geldwaesche-pep-hochrisikoland-risikoanalyse` | Verstaerkte KYC-Prüfung für PEP politisch exponierte Personen Hochrisikolaender und komplexe Strukturen nach GwG. Anwendungsfall Kunde ist PEP oder kommt aus Hochrisikoland und verstaerkte Sorgfaltspflichten greifen. Normen § 15 GwG vers... |
| `geldwaesche-risikoanalyse-unternehmen` | Risikobasierte AML/CFT-Risikoanalyse nach § 5 GwG für Verpflichtete. Anwendungsfall Unternehmen muss gesetzlich vorgeschriebene Risikoanalyse erstellen oder aktualisieren. Normen § 5 GwG Risikoanalyse § 6 GwG interne Sicherungsmassnahmen... |
| `geldwaesche-sanktionsscreening` | Sanktionsscreening von Kunden Transaktionen und Beteiligten gegen EU-US- und UN-Sanktionslisten. Anwendungsfall neues Geschäft soll abgeschlossen oder Transaktion freigegeben werden. Normen EU-Verordnungen 2580/2001 881/2002 Russland-VO... |
| `geldwaesche-schulung-awareness` | Zielgruppengerechte AML/KYC-Schulungen und Awareness-Maßnahmen nach § 6 Abs. 2 Nr. 6 GwG. Anwendungsfall jaehrliche Pflichtschulung muss durchgeführt oder neue Mitarbeiter eingearbeitet werden. Normen § 6 Abs. 2 Nr. 6 GwG Schulungspflich... |
| `geldwaesche-sicherungsmassnahmen-simulation` | Aufbau und Haertung interner Sicherungsmassnahmen ICP nach § 6 GwG. Anwendungsfall Verpflichteter muss ICP aufbauen oder bestehendes Kontrollsystem verbessern. Normen § 4 GwG Bestellung GwG-Beauftragter § 6 GwG interne Maßnahmen § 7 GwG... |
| `geldwaesche-simulation-testlauf` | Simulation eines Compliance-Arbeitstags mit Onboarding Alerts Verdachtsprüfung und Behördenfragen. Anwendungsfall Team will GwG-Workflows trainieren oder Plugin demonstrieren. Deckt Onboarding Alert UBO-Luecke Sanktionshit Verdachtsprüfu... |
| `geldwaesche-transaktionsmonitoring` | Erkennung auffälliger Transaktionsmuster und Red-Flags im Zahlungsverkehr nach GwG. Anwendungsfall Bank oder Zahlungsdienstleister will Transaktion auf Geldwäscherisiko prüfen. Normen § 10 Abs. 1 Nr. 5 GwG Transaktionsmonitoring § 43 GwG... |
| `geldwaesche-transaktionsstopp-freeze` | Transaktionsstopp Kontoeinfrierung und Nichtdurchführung bei Sanktions- oder Verdachtstreffer. Anwendungsfall Transaktion muss gestoppt oder Konto eingefroren werden weil Sanktionstreffer oder konkreter Verdacht vorliegt. Normen § 40 GwG... |
| `geldwaesche-transparenzregister` | Transparenzregister-Einsicht Abgleich und Unstimmigkeitsmeldung nach GwG. Anwendungsfall wirtschaftlich Berechtigte muessen im Transparenzregister geprüft oder Unstimmigkeit gemeldet werden. Normen § 20 GwG Meldepflicht § 23 GwG Einsicht... |
| `geldwaesche-ubo-wirtschaftlich-berechtigte` | Ermittlung wirtschaftlich Berechtigter UBO Kontrollketten und Trust-Stiftungsstrukturen nach GwG. Anwendungsfall neue Geschäftsbeziehung mit Unternehmen und wirtschaftlich Berechtigte muessen identifiziert werden. Normen § 3 GwG wirtscha... |
| `geldwaesche-verdachtsmeldung-verpflichteten` | Vorbereitung und Einreichung von Verdachtsmeldungen nach § 43 GwG über goAML-Portal an die FIU. Anwendungsfall Sachverhalt mit Verdacht auf Geldwäsche oder Terrorismusfinanzierung ist festgestellt und Meldung muss erstattet werden. Norme... |
| `geldwaesche-verhandlung-vergleich-und-eskalation` | Geldwaesche: Verhandlung, Vergleich und Eskalation. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `geldwaesche-verpflichteten-check` | Prüft ob und in welcher Rolle ein Unternehmen oder Berufsstraeger nach GwG verpflichtet ist. Anwendungsfall Unternehmen oder Kanzlei will wissen ob GwG-Pflichten bestehen und welche Konsequenzen das hat. Normen § 2 GwG Verpflichtetenkata... |
| `geldwaeschepraevention-erstpruefung-und-mandatsziel` | Geldwaeschepraevention: Erstprüfung, Rollenklärung und Mandatsziel. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `goaml-gwg-spezial-kommandocenter` | Goaml: Risikoampel, Gegenargumente und Verteidigungslinien. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `gwg-tatbestand-beweis-und-belege` | GwG: Tatbestandsmerkmale, Beweisfragen und Beleglage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `kommandocenter-compliance-dokumentation-und-akte` | Kommandocenter: Compliance-Dokumentation und Aktenvermerk. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `livecheck-red-risikoanalyse` | Livecheck: Red-Team und Qualitätskontrolle. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `onboarding-bauleiter-trade-based` | Bauleiter KYC-Onboarding: Identifizierung natuerliche und juristische Personen, wirtschaftlich Berechtigter, PEP-Prüfung, Sanktionslistenabgleich. Prüfraster für Verpflichtete im Geldwaeschepraevention Aml Kyc. |
| `output-waehlen` | Output-Wahl für Geldwäscheprävention AML/KYC: stimmt Adressat (Verpflichteter (Bank, Anwalt, Notar), Kunde, FIU), Frist (Verdachtsmeldung unverzüglich § 43 GwG) und Form auf den Zweck ab — typische Outputs: KYC-Dossier, SAR-Entwurf, Risi... |
| `quellen-livecheck` | Quellen-Live-Check für Geldwäscheprävention AML/KYC: prüft Normen (GwG, FATF 40 Recommendations, EU-AMLD VI) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt FIU und Quellenhygiene nach references/quellenhygiene.md. |
| `rechtsquellen` | Rechtsquellen: Quellenprüfung; Formular, Portal und Einreichungslogik: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `risikoanalyse-geldwaesche-bussgeld` | Risikoanalyse: Fristen, Form, Zuständigkeit und Rechtsweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `risikoanalyse-und-verdachtsmeldeweiche` | GwG-Risikoanalyse und Verdachtsmeldeweiche: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Geldwaeschepraevention Aml Kyc. |
| `sanktionen-geldwaesche-gruppenweite-aml` | Sanktionen: Dokumentenmatrix, Lückenliste und Nachforderung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `schulung-quellenkarte` | Schulung Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `simulation-mandantenkommunikation-entscheidungsvorlage` | Simulation: Mandantenkommunikation und Entscheidungsvorlage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `sonderfall-edge-geldwaesche` | Chronologie: Sonderfall und Edge-Case-Prüfung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `spezial-behoerdenverfahren-schriftsatz-brief-und-memo-bausteine` | Behoerdenverfahren: Schriftsatz-, Brief- und Memo-Bausteine. |
| `spezial-schulung-livequellen-und-rechtsprechungscheck` | Schulung: Livequellen- und Rechtsprechungscheck. |
| `testlauf-beweislast-transaktionsmonitoring` | Testlauf: Beweislast, Darlegungslast und Substantiierung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `transaktionsmonitoring-international-schnittstellen` | Transaktionsmonitoring: Internationaler Bezug und Schnittstellen. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `transparenzregister-behoerden-gericht-und-registerweg` | Transparenzregister: Behörden-, Gerichts- oder Registerweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Geldwäscheprävention AML/KYC: trennt fehlende Tatsachen von fehlenden Belegen (KYC-Akte, Risk Assessment, Compliance-Manual), nennt pro Lücke Beweisthema, Beschaffungsweg (FIU), Frist und Ersatznachweis. |
| `verdachtsmeldung-mehrparteien-konflikt-und-interessen` | Verdachtsmeldung: Mehrparteienkonflikt und Interessenmatrix: Verdachtsmeldung: Mehrparteienkonflikt und Interessenmatrix. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Geldwaeschepraevention Aml Kyc. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Geldwaeschepraevention Aml Kyc. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
