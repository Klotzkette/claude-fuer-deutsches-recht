---
name: cra-produkt-mit-digitalen-elementen
description: "Für CRA für Roboter mit digitalen Elementen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: robotik-recht. Route: cra-produkt-mit-digitalen-elementen."
---

# CRA für Roboter mit digitalen Elementen

## Fachkern: CRA für Roboter mit digitalen Elementen
- **Normen-/Quellenanker:** EU-Maschinenverordnung, Produkthaftungsrecht, ProdSG/GPSR, AI Act, MDR/MPDG bei Medizinrobotik, DSGVO, Cybersecurity/NIS2 und Arbeitsschutz.
- **Entscheidende Weiche:** Prüfe Rolle Hersteller/Integrator/Betreiber, bestimmungsgemäße Verwendung, CE-Konformität, Sicherheitsfunktion, Lern-/Updateverhalten, Schadenpfad und Rückrufpflicht.

## Worum geht es konkret

Der Cyber Resilience Act (CRA, VO (EU) 2024/2847) führt eine horizontale CE-Pflicht für "Produkte mit digitalen Elementen" ein. Roboter mit eingebetteter Software, Steuerungs-Apps, Cloud-Komponenten und OTA-Updates fallen darunter und müssen Secure-by-Design entwickelt, Schwachstellen koordiniert behoben und Vorfälle gemeldet werden. Die Vorschriften gelten gestaffelt: Schwachstellen- und Vorfallmeldepflichten ab 11.09.2026, die Hauptpflichten ab 11.12.2027 (Art. 71 CRA). Prüfe Robotikprodukte gegen die CRA-Anforderungen.

## Wann dieses Modul hilft / Kaltstart-Fragen

1. **Rolle:** Hersteller, Importeur, Distributor, Notified Body (bei "wichtigen" Produkten Klasse I/II), CISO, Marktüberwachung.
2. **Robotertyp:** Industrie-/Cobot, AMR, Servicerobotik, IoT-Komponente; Funktion als "wichtige" Klasse?
3. **Software-Architektur:** Embedded, Companion-App, Cloud-Komponente, Drittsoftware, Open Source.
4. **Anlass:** Markteinführung, Vorfall, Schwachstelle, Audit, Kunden-Audit, Vertragsverhandlung.
5. **Unterlagen:** SBOM (CycloneDX/SPDX), Penetrationstest, Schwachstellen-Policy, OTA-Architektur, Incident-Response-Plan.

## Rechtlicher Rahmen

- **CRA** VO (EU) 2024/2847; Anhang I Cybersecurity Requirements (Teil I) und Vulnerability Handling (Teil II); Anhang III Wichtige/kritische Produkte.
- **Geltungsstaffelung Art. 71 CRA:** Vorfall- und Schwachstellenmeldungen ab 11.09.2026; Hauptpflichten 11.12.2027.
- **Schnittstellen:** MaschinenVO VO (EU) 2023/1230; KI-VO VO (EU) 2024/1689; NIS-2-RL (EU) 2022/2555 und BSIG; ProdHaftG/VO (EU) 2024/2853; RED-VO (EU) 2014/53 i. V. m. delegierter VO (EU) 2022/30 (RED-Cybersecurity).
- **Herstellermeldungen nach Artikel 14 CRA:** Aktiv ausgenutzte Schwachstellen und schwerwiegende Sicherheitsvorfälle getrennt prüfen. 24-/72-Stunden-Meldungen knüpfen an Kenntnis an; für den Abschlussbericht gelten je nach Pfad unterschiedliche Auslöser und Fristen (siehe Meldeplan).
- **Geldbußen** Art. 64 CRA: bis 15 Mio. EUR oder 2,5 % weltweiter Jahresumsatz für wichtigste Pflichtverstöße.

## Meldeplan nach Artikel 14 CRA

Artikel 14 gilt seit **11.09.2026** (Artikel 71 Absatz 2 CRA). Hersteller führen den Kenntniszeitpunkt für jeden Tatbestand gesondert. Eine bloße Auffälligkeit belegt noch keine aktiv ausgenutzte Schwachstelle. Bei einem Sicherheitsvorfall die Schwerekriterien des Artikels 14 Absatz 5 prüfen, insbesondere den Schutz sensibler oder wichtiger Daten/Funktionen und die Einführung oder Ausführung böswilligen Codes. Treffen beide Tatbestände zu, beide Pfade abarbeiten.

| Meldestufe | Aktiv ausgenutzte Schwachstelle (Artikel 14 Absätze 1 und 2) | Schwerwiegender Sicherheitsvorfall mit Auswirkungen auf die Produktsicherheit (Artikel 14 Absätze 3 und 4) |
|---|---|---|
| Frühwarnung | Unverzüglich, spätestens 24 Stunden ab Kenntnis. Die Mitgliedstaaten nennen, in denen das Produkt nach Kenntnis des Herstellers bereitgestellt wurde. | Unverzüglich, spätestens 24 Stunden ab Kenntnis. Angeben, ob rechtswidrige oder böswillige Handlungen vermutet werden; gegebenenfalls die bekannten Bereitstellungs-Mitgliedstaaten nennen. |
| Meldung | Unverzüglich, spätestens 72 Stunden ab Kenntnis, soweit noch nicht vorgelegt: verfügbare Angaben zu Produkt, Schwachstelle und Ausnutzungsart, ergriffenen Korrektur-/Risikominderungsmaßnahmen und Handlungsmöglichkeiten der Nutzer; gegebenenfalls Sensibilität der Informationen angeben. | Unverzüglich, spätestens 72 Stunden ab Kenntnis, soweit noch nicht übermittelt: verfügbare Angaben zur Vorfallart, erste Bewertung, ergriffene Korrektur-/Risikominderungsmaßnahmen und Handlungsmöglichkeiten der Nutzer; gegebenenfalls Sensibilität der Informationen angeben. |
| Abschlussbericht | Soweit noch nicht vorgelegt: spätestens **14 Tage nach Verfügbarkeit einer Korrektur- oder Risikominderungsmaßnahme**. Schwachstelle, Schweregrad und Auswirkungen, verfügbare Informationen über ausnutzende böswillige Akteure sowie bereitgestellte Sicherheitsupdates oder andere Korrekturmaßnahmen beschreiben. | Soweit noch nicht übermittelt: **innerhalb eines Monats nach Übermittlung der Vorfallmeldung nach Absatz 4 Buchstabe b**. Vorfall einschließlich Schweregrad und Auswirkungen ausführlich beschreiben; wahrscheinliche Bedrohung/Ursache sowie getroffene und laufende Abhilfemaßnahmen angeben. |

Der **Zwischenbericht** nach Artikel 14 Absatz 6 enthält relevante Statusaktualisierungen und wird auf Aufforderung des ursprünglich empfangenden Koordinator-CSIRT vorgelegt. Er ist keine feste 72-Stunden-Meldestufe. Meldungen laufen über den einschlägigen CSIRT-Endpunkt der einheitlichen Meldeplattform und sind gleichzeitig für ENISA zugänglich (Artikel 14 Absatz 7, Artikel 16). Die 24-/72-Stunden-Grenzen sind Höchstfristen; erforderliche Meldungen nicht bis zu deren Ablauf aufschieben.

[Amtlicher CRA-Text, Artikel 14 Absätze 1 bis 7 und Artikel 71 Absatz 2; geprüft 01.11.2026](https://eur-lex.europa.eu/eli/reg/2024/2847/oj).

## Schritt für Schritt

1. **Produkt-Klassifikation.** Standardprodukt vs. "wichtige" Klasse I/II vs. "kritische" Klasse (Anhang III/IV CRA).
2. **Secure-by-Design.** Anhang I Teil I: Standard-Konfiguration ohne bekannte Schwachstellen, Schutz vor unautorisiertem Zugriff, Vertraulichkeit, Integrität, Verfügbarkeit; Update-Mechanismus; minimal-privilege.
3. **Vulnerability Handling.** Anhang I Teil II: Schwachstellen-Policy, Coordinated Vulnerability Disclosure (CVD), SBOM, Sicherheitsupdates während Support-Periode.
4. **SBOM.** Maschinenlesbar (CycloneDX/SPDX), per Update aktualisiert; Hash der Lieferung.
5. **Penetration Testing** und Threat Modeling vor Inverkehrbringen.
6. **Vorfall- und Schwachstellenmeldungen.** Seit 11.09.2026 den vorstehenden Meldeplan anwenden: Tatbestand und Kenntniszeitpunkt, zuständigen CSIRT-Endpunkt, Pflichtangaben jeder Stufe und fristauslösendes Ereignis des Abschlussberichts dokumentieren. Zwischenberichte nach Absatz 6 nur auf entsprechende Aufforderung vorlegen.
7. **Konformitätsbewertung** Modul nach Anhang VIII CRA; bei kritischen Produkten Pflicht zur Notified Body.
8. **Support-Periode.** Mindestens 5 Jahre, sofern Lebenszyklus nicht kürzer (Art. 13 Abs. 8 CRA).
9. **Vertragsklauseln** mit Zulieferern: SBOM-Pflicht, Schwachstellen-SLA, Update-Bereitstellung.

## Trade-off-Matrix

| Architektur | Pro CRA | Contra | Empfehlung |
|---|---|---|---|
| Embedded ohne Update-Pfad | – | nicht CRA-konform | OTA mit Signaturkette |
| OTA-Update kontinuierlich | sicher | erneute Konformitätsbewertung bei wesentlicher Änderung | Update-Klassifikation Cosmetic/Functional/Security |
| Cloud-Komponente | flexibel | Abhängigkeit, DSGVO, NIS-2 | hybrid: kritische Steuerung Edge, Telemetrie Cloud |
| Open Source | Auditierbarkeit | Verantwortlichkeit unklar | OSS-Stewards Art. 24 CRA; eigene Verantwortung dokumentieren |

## Praxistipps

- **PSIRT** (Product Security Incident Response Team) etablieren.
- **CVE-Monitoring** automatisiert.
- **Bug Bounty** als Bestandteil der CVD.
- **Roll-back-Mechanismus** bei fehlerhaftem Update.
- **Signatur-Schlüssel** in HSM, getrennte Rolle für Signatur-Freigabe.

## Mustertexte

**Schwachstellen-Policy (Auszug):**

> Wir nehmen Schwachstellenmeldungen an psirt@[Firma].de entgegen. Acknowledgment binnen 48 Stunden; Status-Update alle 14 Tage. Schweregradkategorien CVSS v3.1; kritische Schwachstellen erhalten Patch binnen 30 Tagen, hoch innerhalb 90 Tagen. Wir veröffentlichen Security Advisories in CycloneDX VEX-Format. Wir verpflichten uns zur koordinierten Offenlegung gemäß ISO/IEC 29147 und Art. 13 Abs. 8 CRA.

**Vertragsklausel mit Zulieferer:**

> Der Lieferant stellt mit jeder Lieferung eine SBOM im CycloneDX-Format zur Verfügung. Der Lieferant verpflichtet sich, sicherheitsrelevante Schwachstellen seiner gelieferten Komponenten innerhalb von 24 Stunden nach Bekanntwerden gegenüber dem Auftraggeber zu melden und innerhalb von 72 Stunden eine Risikoeinschätzung zu liefern. Sicherheitsupdates werden im Rahmen der CRA-Support-Periode von 5 Jahren bereitgestellt.

**Frühwarnung einer aktiv ausgenutzten Schwachstelle (auszufüllendes Beispiel):**

> Wir, [Hersteller], melden gemäß Artikel 14 Absatz 1 und Absatz 2 Buchstabe a CRA eine aktiv ausgenutzte Schwachstelle in [Produkt und betroffene Versionen]. Wir haben am [Datum/Uhrzeit mit Zeitzone] Kenntnis von [konkret beschriebener Schwachstelle] und ihrer aktiven Ausnutzung erlangt; dies wird durch [Beleg der Ausnutzung] gestützt. Nach unserem derzeitigen Kenntnisstand wurde das Produkt in [Mitgliedstaaten] bereitgestellt. Die Schwachstellenmeldung nach Absatz 2 Buchstabe b übermitteln wir unverzüglich, spätestens bis [Datum/Uhrzeit innerhalb von 72 Stunden ab Kenntnis], soweit die betreffenden Informationen noch nicht vorliegen. Ansprechpartner ist [Name, E-Mail, Telefon].

Eine lediglich vermutete Angriffshandlung nicht als belegte aktive Schwachstellenausnutzung ausgeben. Liegt stattdessen ein schwerwiegender Sicherheitsvorfall vor, den Pfad nach Absatz 3 und 4 verwenden und bereits in dessen Frühwarnung den Verdacht rechtswidriger oder böswilliger Handlungen ausdrücklich mit ja/nein/derzeit ungeklärt erläutern.

## Typische Fehler

- **SBOM unvollständig** – Drittlieferanten fehlen.
- **OTA ohne Signaturkette** – Manipulation des Update-Pfads.
- **Keine PSIRT-Adresse** öffentlich – CRA verlangt sie.
- **Support-Periode nicht definiert** im Datenblatt.
- **Meldepflicht-Fristen überschritten** – Bußgeldrisiko Art. 64 CRA.

## Quellen Stand 06/2026

- VO (EU) 2024/2847 (CRA), Art. 13, 14, 24, 64, 71; Anhang I, III, VIII.
- VO (EU) 2023/1230 (MaschinenVO).
- VO (EU) 2024/1689 (KI-VO).
- RL (EU) 2022/2555 (NIS-2); BSIG.
- VO (EU) 2014/53 (RED) i. V. m. delegierter VO (EU) 2022/30.
- ISO/IEC 29147 (CVD); ISO/IEC 30111.
- Live-Verifikation auf eur-lex.europa.eu, enisa.europa.eu, bsi.bund.de; lizenzierte Datenbanken (beck-online, juris) nur bei vorhandenem Zugang.
Für den KI-bezogenen Teil dieses Arbeitsschritts gilt die [fachbezogene Normen- und Fallprüfung](../../references/ki-normen-und-fallpruefung.md). Ordnen Sie Sensorik, Sicherheitsfunktion, Steuerungssoftware und vorgesehene Änderungen getrennt ein. Prüfen Sie den Maschinenpfad in Anhang I Abschnitt B und die Begrenzung durch Artikel 2 Absatz 2, bevor Sie sämtliche Systempflichten übertragen. Dokumentieren Sie den Gegenbeleg und übernehmen Sie nur die tatsächlich tragfähige Rechtsfolge in das bestellte Arbeitsprodukt.
