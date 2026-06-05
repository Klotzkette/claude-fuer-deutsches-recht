---
name: eisenbahn-digital-services-trusted-flagger
description: "Eisenbahn Digital Services Trusted Flagger: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Eisenbahn Digital Services Trusted Flagger

## Arbeitsbereich

Dieser Skill bündelt 8 sachlich verwandte Arbeitsschritte rund um **Eisenbahn Digital Services Trusted Flagger** im Plugin Bundesnetzagentur-Verfahren. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `digital-services-transparenzberichte-online-plattformen` | Digital Services / Transparenzberichte Online-Plattformen: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: DDG, DSA VO (EU) 2022/2065. |
| `digital-services-trusted-flagger-anerkennung` | Digital Services / Trusted Flagger Anerkennung: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: DDG, DSA VO (EU) 2022/2065. |
| `digital-services-vlop-vlose-koordination-eu-kommission` | Digital Services / VLOP VLOSE Koordination EU-Kommission: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: DDG, DSA VO (EU) 2022/2065. |
| `eisenbahn-anreizsetzung-schiene` | Eisenbahn / Anreizsetzung Schiene: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, AEG, EU-Eisenbahnrecht. |
| `eisenbahn-baumassnahmen-und-sperrpausen` | Eisenbahn / Baumaßnahmen und Sperrpausen: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, AEG, EU-Eisenbahnrecht. |
| `eisenbahn-beschwerde-evu-gegen-infrastrukturbetreiber` | Eisenbahn / Beschwerde EVU gegen Infrastrukturbetreiber: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, AEG, EU-Eisenbahnrecht. |
| `eisenbahn-eisenbahnregulierung-eregg` | Eisenbahn / Eisenbahnregulierung ERegG: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, AEG, EU-Eisenbahnrecht. |
| `eisenbahn-entgeltregulierung-schiene` | Eisenbahn / Entgeltregulierung Schiene: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, AEG, EU-Eisenbahnrecht. |

## Arbeitsweg

Im Plugin Bundesnetzagentur-Verfahren gilt für **Eisenbahn Digital Services Trusted Flagger**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `digital-services-transparenzberichte-online-plattformen`

**Fokus:** Digital Services / Transparenzberichte Online-Plattformen: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: DDG, DSA VO (EU) 2022/2065.

# Transparenzberichte nach DSA: Art. 15, 24, 42

## Zweck und Anwendungsfall
Anwaltliche Begleitung der Erstellung, Prüfung und Auswertung von DSA-Transparenzberichten. Drei Stufen sind zu unterscheiden: Art. 15 DSA (allgemeine Berichtspflicht aller Vermittlungsdienste, jährlich); Art. 24 DSA (zusätzliche Pflichten für Online-Plattformen, alle 6 Monate Nutzerzahlen); Art. 42 DSA (zusätzliche Pflichten für VLOPs/VLOSEs, halbjährliche Detailberichte einschl. Risikoindikatoren). Der Skill betreut Plattformen bei der Compliance, Verbände bei der Auswertung und die BNetzA-Schnittstelle bei Auskunftsverlangen zur Datengrundlage.

## Eingaben
- Plattform-Klassifizierung (Hosting, Online-Plattform, VLOP/VLOSE).
- Berichtszeitraum.
- Datenquellen: Moderationssysteme, Beschwerdesysteme, Behördenanordnungen, Trusted-Flagger-Meldungen.
- Format-Anforderungen (Kommissions-Templates, maschinenlesbar, Open Data).
- Konkrete Anlässe (Auskunftsverlangen BNetzA, Mängelrüge eines Verbands).

## Rechtsrahmen
- Art. 15 DSA (Berichte aller Vermittlungsdienste).
- Art. 24 DSA (Berichte Online-Plattformen; durchschnittliche monatliche Nutzer).
- Art. 42 DSA (Berichte VLOPs/VLOSEs; halbjährlich; Risikoindikatoren; Audit Art. 37).
- Art. 33 DSA (Schwellenwert 45 Mio. EU-Nutzer).
- Durchführungsverordnung der Kommission gem. Art. 15 Abs. 3 DSA (Berichtstemplates; vom Anwender im EUR-Lex zu verifizieren).
- §§ 12, 18, 19, 24 DDG.
- § 7 BNetzAG, § 30 VwVfG (Beschlüsse, Akteneinsicht).

## Ablauf
1. **Klassifizierung verifizieren.** Anzahl der durchschnittlichen monatlichen aktiven Nutzer in der EU; Berechnungsmethode nach Kommissions-Leitlinien zu Art. 24 Abs. 2 DSA.
2. **Datenarchitektur aufsetzen.** Source-Systeme, Aggregationsverfahren, Audit-Trail, Pseudonymisierung.
3. **Berichts-Bestandteile.** Anordnungen von Behörden (Art. 9, 10 DSA), Meldungen Art. 16 DSA, eigeninitiative Moderationsmaßnahmen, Beschwerden Art. 20 DSA, automatisierte Moderation, Trainingsdaten, Streitbeilegung Art. 21 DSA, Suspendierungen Art. 23 DSA.
4. **Format-Konformität.** Maschinenlesbarkeit, EU-Templates, mehrsprachige Verfügbarkeit, Veröffentlichungsstelle (eigene Webseite + Kommissionsdatenbank).
5. **VLOP-Spezifika.** Risikoindikatoren nach Art. 34 DSA, Effektivitätsmessung der Minderungsmaßnahmen Art. 35, Audit-Bericht Art. 37 DSA (extern, jährlich).
6. **Plausibilisierung.** Konsistenz mit dem Werbe-Repository Art. 39 DSA, mit der "Transparency Database" der Kommission und mit eigenen Quartalsberichten.
7. **Aufsichtsschnittstelle.** Reaktion auf BNetzA-Auskunftsverlangen § 18 DDG bei vermuteten Berichtsmängeln; Begründung bei Schwärzungen (Sicherheit, Geheimnisschutz).
8. **Sanktion.** § 24 DDG-Bußgelder bei unrichtigen oder unvollständigen Berichten; Höchstrahmen bis 6 Prozent des Jahresumsatzes.

## Mustertexte
- Gliederungs-Template für Art. 15-Bericht: Sachverhalt, Daten, Auswertung, methodische Anmerkungen.
- Audit-Begleitnotiz (Plattform an externen Auditor) mit Datengrundlage und Geheimhaltungsklausel.
- Stellungnahme an die BNetzA bei beanstandetem Bericht: Daten-Heritage, Aggregationsmethode, Nachreichung.

## Quellenpflicht
- EUR-Lex (DSA-Originaltext und Durchführungsverordnungen).
- Veröffentlichte Berichte sehr großer Plattformen als Vergleichsmaßstab.
- BNetzA-Mitteilungen, Kommissions-Reports.
- Zitierweise nach `references/zitierweise.md`.

## Ausgabeformat
- Compliance-Memo zur Berichtspflicht (10–20 Seiten).
- Audit-Checkliste für externe Prüfer.
- Stellungnahme an die BNetzA.

## Beispiele
- Online-Plattform veröffentlicht ihren ersten Art. 15-Bericht. Anwaltliche Begleitung der Aggregation und Schwärzung.
- BNetzA fordert ergänzende Erklärung zur Berechnung der monatlichen Nutzer (Art. 24 Abs. 2 DSA). Methodikbeschreibung mit statistischer Begründung.
- VLOP erhält Audit-Bericht nach Art. 37 DSA mit Beanstandungen. Erstellung der Action-Pläne nach Art. 37 Abs. 6 DSA.

## Qualitätsgate
Klassifizierung verifiziert? Datenquellen vollständig? Schwellenwerte korrekt berechnet? Format-Konformität (Kommissions-Template) geprüft? Veröffentlichungsstelle und -datum dokumentiert? Audit-Trail für jede Zahl vorhanden?

## 2. `digital-services-trusted-flagger-anerkennung`

**Fokus:** Digital Services / Trusted Flagger Anerkennung: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: DDG, DSA VO (EU) 2022/2065.

# Trusted Flagger: Anerkennung nach Art. 22 DSA

## Zweck und Anwendungsfall
Anwaltliche Begleitung des Anerkennungsverfahrens für vertrauenswürdige Hinweisgeber ("Trusted Flagger") gem. Art. 22 DSA. Anerkennung erfolgt durch die Bundesnetzagentur als Digital Services Coordinator nach § 20 DDG. Trusted Flagger erhalten von Online-Plattformen vorrangige Behandlung ihrer Meldungen. Anwendung: Bürgerrechtsorganisationen, Verbände, Kinderschutzorganisationen, Branchenverbände, Sicherheits-Initiativen (z. B. zu CSAM, Terrorinhalten, Verbraucherschutz, Urheberrecht).

## Eingaben
- Antragsteller: juristische Person oder Personengesellschaft mit eigener Rechtspersönlichkeit.
- Tätigkeitsbereich (Sachgebiet, Sprache, geografische Reichweite).
- Nachweise zur Sachkunde, Sorgfalt und Unabhängigkeit.
- Bestehende Kooperationen mit Plattformen.
- Beabsichtigtes Melde-Volumen und interne Qualitätssicherung.

## Rechtsrahmen
- Art. 22 DSA (Trusted Flagger).
- Art. 23 DSA (Maßnahmen gegen missbräuchliche Nutzung).
- § 20 DDG (Anerkennungszuständigkeit der BNetzA als DSC).
- § 18 DDG (Auskunftsverlangen DSC).
- §§ 35 ff. VwVfG (Verwaltungsverfahren), § 28 VwVfG (Anhörung).
- §§ 51 Abs. 1 Nr. 7 VwGO, § 75 VwGO (Klage VG Köln).
- DSGVO Art. 6, 9 (Rechtsgrundlage für Meldungstätigkeit bei personenbezogenen Daten).

## Ablauf
1. **Eignungsprüfung.** Erfüllt der Antragsteller die drei Kriterien des Art. 22 Abs. 2 DSA: (a) besondere Sachkunde in der Erkennung illegaler Inhalte; (b) Unabhängigkeit von Online-Plattformen; (c) sorgfältige, objektive Tätigkeitsweise?
2. **Sachkundenachweis.** Mitarbeiterprofile, Schulungen, Methodik (z. B. Standards der EU-Agenturen, INACH, NGO-Netzwerke).
3. **Unabhängigkeitsnachweis.** Finanzielle Struktur (Spenden, Mitgliedsbeiträge, öffentliche Förderung), Organisationsform, keine wesentliche Plattform-Finanzierung.
4. **Sorgfaltsnachweis.** Internes Qualitätssicherungs-Verfahren, Vier-Augen-Prinzip, Eskalations-Workflow, statistische Erfolgsquote der bisherigen Meldungen.
5. **Antrag stellen.** Antrag an die BNetzA mit umfassenden Nachweisen (Satzung, Tätigkeitsberichte, Personalstruktur, Methodikhandbuch, Datenschutzkonzept).
6. **Sektor-Eingrenzung.** Anerkennung erfolgt sektoriell (z. B. CSAM, Terrorpropaganda, Urheberrecht, Verbraucherschutz); klare Definition im Antrag erforderlich.
7. **Berichtspflichten.** Art. 22 Abs. 3 DSA verlangt jährliche Tätigkeitsberichte; Verlust der Anerkennung bei Missbrauch oder Untätigkeit.
8. **Rechtsschutz.** Bei Ablehnung Klage VG Köln (Verpflichtungsklage); bei Aberkennung Anfechtungsklage.

## Mustertexte
- Anerkennungsantrag nach Art. 22 DSA i. V. m. § 20 DDG: Identifikation des Antragstellers, Tätigkeitsbereich, Sachkundenachweis, Unabhängigkeitsnachweis, Sorgfaltsnachweis, Datenschutzkonzept.
- Jährlicher Tätigkeitsbericht: Meldungs-Anzahl, Erfolgsquote, Verfahrenslaufzeiten bei Plattformen, Beschwerdesumme.
- Stellungnahme zur Aberkennung: Sachverhalt, Gegenargumente, Verhältnismäßigkeit.

## Quellenpflicht
- DSA-Originaltext (EUR-Lex).
- DDG-Originaltext (BGBl. 2024 I Nr. 149).
- BNetzA-Veröffentlichungen zur Trusted-Flagger-Liste.
- VG Köln-Entscheidungen mit Az., Datum, Fundstelle.
- Zitierweise nach `references/zitierweise.md`.

## Ausgabeformat
- Antragsdossier (20–60 Seiten je nach Komplexität).
- Methodikhandbuch (Anlage).
- Tätigkeitsbericht (Vorlage).

## Beispiele
- Kinderschutz-NGO beantragt Anerkennung für Meldung von CSAM. Sektorale Anerkennung erforderlich, Datenschutzkonzept besonders kritisch.
- Branchenverband beantragt Anerkennung für Markenrechtsmeldungen. Plattformen müssen vorrangig prüfen, jedoch eigene Kollisionsentscheidung beibehalten.
- Verbraucherzentrale beantragt sektorübergreifende Anerkennung. Tendenz: schmalere Anerkennung pro Sektor.

## Qualitätsgate
Sachkundenachweis konkret (nicht nur abstrakt)? Unabhängigkeit von Plattformen finanziell tragfähig nachgewiesen? Datenschutzkonzept DSGVO-konform? Beschwerde- und Eskalationswege intern dokumentiert? Sektor-Definition präzise?

## 3. `digital-services-vlop-vlose-koordination-eu-kommission`

**Fokus:** Digital Services / VLOP VLOSE Koordination EU-Kommission: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: DDG, DSA VO (EU) 2022/2065.

# VLOP/VLOSE-Koordination zwischen EU-Kommission und BNetzA

## Zweck und Anwendungsfall
Anwaltliche Steuerung von Mandaten an der Schnittstelle zwischen ausschließlicher Kommissionszuständigkeit (Sehr-große-Online-Plattformen und Suchmaschinen, Art. 33 ff. DSA) und nationaler DSC-Zuständigkeit. Die EU-Kommission setzt das DSA gegenüber VLOPs/VLOSEs in Bezug auf die Pflichten aus Kapitel III Abschnitt 5 DSA (Art. 34–48) ausschließlich um (Art. 56 Abs. 2 und Art. 64 ff. DSA). Die BNetzA als DSC bleibt für die übrigen Pflichten zuständig und nimmt unterstützende Funktionen wahr (Art. 60 DSA, gemeinsame Untersuchungen). Mandate erfordern parallele Verteidigungs- und Compliance-Strategien.

## Eingaben
- Plattform-Klassifizierung (VLOP/VLOSE-Designierung der EU-Kommission, Nutzerzahlen).
- Pflichtenanker (Kap. III Abschn. 5 vs. übrige DSA-Pflichten).
- Aktuelle Verfahren (Kommissions-Untersuchung, BNetzA-Vorermittlung).
- Rolle: Plattform, Beschwerdeführer, Drittinteressierter.
- Fristen (Kommissions-Verfahren häufig 30 Tage; nationale Verfahren VwVfG).

## Rechtsrahmen
- VO (EU) 2022/2065 (DSA), insbesondere Art. 33 (Schwellenwerte), 34/35 (Systemrisiken/Minderung), 36 (Krisenreaktion), 37 (Audit), 38 (nicht-profilbasierte Option), 39 (Werbe-Repository), 40 (Datenzugang Forschung), 41 (Compliance-Funktion), 42 (Transparenzberichte), 44 (Standards), 45 (Verhaltenskodizes), 56–88 (Aufsicht).
- Art. 73 DSA (Verpflichtungszusagen).
- Art. 74 DSA (Geldbußen bis 6 Prozent des Jahresumsatzes).
- §§ 12, 23 DDG (Zuständigkeit BNetzA, Zusammenarbeit).
- Art. 261 AEUV (gerichtliche Kontrolle EuG/EuGH).
- Verfahrensordnung der Kommission, Durchführungsrechtsakt zur DSA-Aufsicht (vom Anwender im EUR-Lex zu verifizieren).

## Ablauf
1. **VLOP/VLOSE-Status klären.** Designierungsentscheidung der Kommission, Nutzerschwellen, Reklassifizierungs-Antrag.
2. **Pflichtenfeld kartieren.** Welche Pflicht ist Kap. III Abschn. 5 (ausschließlich Kommission) vs. übrige Pflichten (DSC mit Unterstützung)?
3. **Verfahrensschiene wählen.** Kommissions-Verfahren: Auskunftsverlangen Art. 67 DSA, Befragung Art. 68 DSA, Vor-Ort-Inspektion Art. 69 DSA, einstweilige Maßnahmen Art. 70 DSA, Verpflichtungszusagen Art. 73 DSA, Bußgeld Art. 74 DSA.
4. **BNetzA-Schnittstelle.** Nationale Mitwirkung über Art. 60 DSA (gemeinsame Untersuchungen) und § 23 DDG; informelle Vorermittlungen können vor BNetzA stattfinden.
5. **Verteidigungslinien.** In Kommissionsverfahren: schriftliche Stellungnahme, Verpflichtungszusagen-Strategie, Akteneinsicht über Hearing Officer, Sprachen-Wahl. In nationalen Verfahren: § 28 VwVfG-Anhörung.
6. **Verpflichtungszusagen Art. 73 DSA.** Inhalt konkret, messbar, evaluierbar, ggf. zeitlich befristet; Marktest durch Kommission möglich.
7. **Gerichtliche Kontrolle.** Klage zum EuG (Art. 263 AEUV) gegen Kommissions-Entscheidung; nationale Verfahren VG Köln.
8. **Risikoindikatoren-Bericht.** Art. 35 DSA-Minderungsmaßnahmen müssen mit Effektivitätsmessung dokumentiert sein; Audit Art. 37 DSA durch unabhängige Stelle.

## Mustertexte
- Antwort auf Kommissions-Auskunftsverlangen Art. 67 DSA: strukturierte Tabelle, Schwärzungen mit Begründung, Konsolidierung mit BNetzA-Stellungnahme.
- Verpflichtungszusagen-Angebot Art. 73 DSA mit Implementierungsplan.
- Mitteilung an den DSC (BNetzA) mit Bezug auf das laufende Kommissions-Verfahren (§ 23 DDG-Kooperationsklarheit).

## Quellenpflicht
- EUR-Lex (DSA, delegierte Rechtsakte, Durchführungsverordnungen).
- Pressemitteilungen und Entscheidungen der EU-Kommission (Webseite GD CNECT).
- EuG/EuGH-Rechtsprechung mit Az., Datum, freier Fundstelle.
- BNetzA-Stellungnahmen.
- Zitierweise nach `references/zitierweise.md`.

## Ausgabeformat
- Verfahrenslandkarte (Kommission vs. BNetzA).
- Stellungnahme an die Kommission mit Akteneinsicht-Begleitschrift.
- Verpflichtungszusagen-Entwurf.

## Beispiele
- VLOP erhält Auskunftsverlangen der Kommission zu Art. 34 DSA-Risiken. Strategie: vollständige Antwort, Schwärzungen wegen Sicherheits- und Geschäftsgeheimnissen, Begleitkommunikation an BNetzA.
- VLOSE muss erstmals Art. 42-Bericht veröffentlichen. Anwaltliche Compliance-Audit-Begleitung.
- Verband stellt Beschwerde bei der BNetzA gegen Werbe-Repository (Art. 39 DSA). BNetzA leitet weiter an die Kommission, da Kap. III Abschn. 5-Pflicht.

## Qualitätsgate
VLOP/VLOSE-Status verifiziert? Zuständigkeitskaskade (Kommission vs. DSC) korrekt? Akteneinsicht bei der Kommission geprüft? Verpflichtungszusagen realistisch? Fristen aus Kommissions-Verfahrensordnung kalendarisiert?

## 4. `eisenbahn-anreizsetzung-schiene`

**Fokus:** Eisenbahn / Anreizsetzung Schiene: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, AEG, EU-Eisenbahnrecht.

# Anreizsetzungssystem im Eisenbahnverkehr (ASS) nach § 39 ERegG

## Zweck und Anwendungsfall
Anwaltliche Begleitung des Anreizsetzungssystems (ASS) für Pünktlichkeit und Zuverlässigkeit im Eisenbahnverkehr. Eisenbahninfrastrukturunternehmen (insbesondere DB InfraGO AG) müssen nach § 39 ERegG ein leistungsabhängiges Bonus-Malus-System gegenüber Eisenbahnverkehrsunternehmen (EVU) anwenden. Die Bundesnetzagentur prüft das System auf Diskriminierungsfreiheit, sachgerechte Kalibrierung der Schwellen und transparente Verrechnung. Anwaltliche Mandate: EVU bei Streit über Malus-Berechnung; EIU bei Verteidigung der eigenen Systemausgestaltung; Verbände bei Konsultationen.

## Eingaben
- Beteiligte Unternehmen (EVU, EIU).
- Aktuell geltendes Anreizsystem (Schienennetz-Benutzungsbedingungen SNB).
- Konkrete Streitpunkte (Schwellenwerte, Verspätungs- und Stornierungsdefinition, Datengrundlage, Sanktionierung).
- Verfahrensstand bei der BNetzA (Konsultation, Festlegungsentwurf, Beschluss).
- Schnittstellen zu Trassenpreissystem und Stationspreissystem.

## Rechtsrahmen
- § 39 ERegG (Anreizsetzung im Eisenbahnverkehr).
- §§ 26–32 ERegG (Schienennetz-Benutzungsbedingungen SNB).
- §§ 45 ff. ERegG (Entgeltregulierung).
- §§ 66–68 ERegG (Beschwerdeverfahren und einstweilige Anordnung der BNetzA).
- § 76 ERegG (Genehmigungsvorbehalt für Entgelte).
- § 79 ERegG (sofortige Vollziehbarkeit).
- Anhang VI RL (EU) 2012/34 (SERA-Richtlinie, performance scheme).
- DVO (EU) 2015/909 (direkte Kosten).

## Ablauf
1. **Klassifizierung des ASS prüfen.** Anwendungsbereich (Personen- und Güterverkehr unterschiedlich), Verspätungsdefinition (in Deutschland regelmäßig ab 6 Minuten), Ausnahmen (höhere Gewalt, Streik, gegenseitige Verursachung).
2. **Datenbasis prüfen.** Quelle (Leit- und Steuerungssystem, automatisierte Erfassung), Datenqualität, Audit.
3. **Bonus-Malus-Logik prüfen.** Symmetrie (Bonus bei pünktlichem EIU vs. Malus bei verspätetem EVU), Kappung, Übergangsfristen, sektorbezogene Differenzierung (Personenfern, Personennah, Güter).
4. **Diskriminierungsfreiheit Art. 56 RL 2012/34/EU.** Gleichbehandlung verschiedener EVU, kein Vorteil für integrierte Wettbewerber.
5. **Verfahren bei der BNetzA.** Konsultation der SNB nach § 26 ERegG, Festlegung und Genehmigung; Beschwerde nach § 66 ERegG bei EVU-Konstellationen.
6. **Stellungnahme entwerfen.** Tatsachen-Substantiierung (Belastung im konkreten Geschäftsjahr), Vergleich zu Best Practice in anderen EU-Mitgliedstaaten, Verhältnismäßigkeitsgrenzen.
7. **Eilverfahren.** § 68 ERegG (einstweilige Anordnung BNetzA); VG Köln § 80 Abs. 5 VwGO gegen § 79 ERegG-Vollziehbarkeit.
8. **Schnittstellen.** Auswirkungen auf Trassenpreis (§ 31 ERegG), Stationsentgelte (§ 33 ERegG), Kapazitätszuweisung (§§ 51 ff. ERegG).

## Mustertexte
- EVU-Beschwerde nach § 66 ERegG gegen Malus-Berechnung mit Datentabellen.
- EIU-Stellungnahme im Konsultationsverfahren mit Datenbasis und Verteilungsmodell.
- Antrag auf einstweilige Anordnung § 68 ERegG bzw. § 80 Abs. 5 VwGO VG Köln.

## Quellenpflicht
- ERegG aktueller Stand.
- RL (EU) 2012/34 und DVO (EU) 2015/909 aus EUR-Lex.
- BNetzA-Beschlüsse, Az. (z. B. BK10-XX-XXX-XX) generisch; konkretes Az. vom Anwender zu verifizieren.
- BVerwG/VG Köln-Rechtsprechung mit Datum, Az., freier Fundstelle.
- Zitierweise nach `references/zitierweise.md`.

## Ausgabeformat
- Stellungnahme oder Beschwerde (10–25 Seiten).
- Datenanlagen (Verspätungsdaten, Malus-Tabellen).
- Risikoampel: Erfolgsaussicht beim BNetzA-Verfahren und beim VG Köln.

## Beispiele
- EVU rügt unverhältnismäßigen Malus bei Verspätungen, die durch Bautätigkeit des EIU verursacht wurden. Bezug auf § 39 i. V. m. Verursacherprinzip.
- EIU verteidigt Differenzierung Personen- vs. Güterverkehr mit unterschiedlichen Pünktlichkeitsmetriken.
- Verband BNE oder mofair stellt im Konsultationsverfahren Vergleich zu österreichischem oder schweizerischem System dar.

## Qualitätsgate
ASS-Definition und Verspätungs-Schwellen klar? Datenbasis vor Streitwert genau beziffert? Diskriminierungs-Maßstab vergleichend belegt? Verfahrensstand bei der BNetzA korrekt eingeordnet? Eil-Optionen § 68 ERegG / VG Köln benannt?

## 5. `eisenbahn-baumassnahmen-und-sperrpausen`

**Fokus:** Eisenbahn / Baumaßnahmen und Sperrpausen: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, AEG, EU-Eisenbahnrecht.

# Baumaßnahmen und Sperrpausen im Schienennetz

## Zweck und Anwendungsfall
Anwaltliche Begleitung bei Streitigkeiten über Baumaßnahmen, Sperrpausen, Bauumleitungen und temporäre Kapazitätseinschränkungen ("Temporary Capacity Restrictions", TCR) im Schienennetz. Die Generalsanierung von Korridoren der DB InfraGO (z. B. Riedbahn-Konzept) hat den Streitstoff stark anwachsen lassen. Anwaltliche Mandate: Eisenbahnverkehrsunternehmen (EVU) gegen Anordnungen der Sperrpause, Kapazitätsanmelder, Halterverbände, Schienengüter-Logistiker, Trassenbörsen-Akteure. Adressat der Aufsicht ist die Bundesnetzagentur als Regulierungsbehörde Eisenbahn nach § 67 ERegG.

## Eingaben
- Konkrete Baumaßnahme (Strecke, Zeitraum, Sperrpausen-Konzept).
- Auswirkung auf einzelne Trassen, Umleitung, Schienenersatzverkehr.
- Beteiligte EVU (Personen-, Güterverkehr).
- Eilbedürftigkeit (z. B. Folge-Buchungen, Just-in-Time-Verkehre).
- Konsultations- und Anmeldestand.

## Rechtsrahmen
- §§ 49–55 ERegG (Kapazitätszuweisung, Vorrang im Konfliktfall).
- §§ 56–58 ERegG (Konfliktlösungsverfahren, einvernehmliche Bauplanung).
- § 39 ERegG (Anreizsetzung; Verspätungen durch Baumaßnahmen sind häufig Streitpunkt).
- § 66 ERegG (Beschwerde EVU gegen EIU).
- § 68 ERegG (einstweilige Anordnung der BNetzA).
- § 79 ERegG (sofortige Vollziehbarkeit).
- VO (EU) 2017/2177 (Serviceeinrichtungen, ergänzend).
- Anhang VII RL (EU) 2012/34 (Bau- und Instandhaltungsplanung; "TCR-Leitlinie" der RailNetEurope als Standard).
- AEG (Allgemeines Eisenbahngesetz), §§ 5a, 14 AEG (Eisenbahnaufsicht durch EBA, Schnittstelle zur BNetzA).

## Ablauf
1. **TCR-Anmeldung prüfen.** Hat das EIU rechtzeitig (TCR-Veröffentlichung mind. 12 Monate vor Sperrpause für große Maßnahmen) angemeldet und konsultiert?
2. **Konsultation und Konfliktlösung.** § 56 ERegG: einvernehmliches Bemühen, Kompensationsangebote, Umleitungen, Zeitfenster.
3. **Vorrangregel prüfen.** § 51 ERegG-Vorrangkriterien (Standard-Trassenmuster, Vertaktung, Anschlusswahrscheinlichkeit).
4. **Auswirkungs-Memo.** Zahlen zur Beeinträchtigung (Trassen pro Tag, Tonnage, Fahrgäste), Vergleich Vor/Nach, Kompensation.
5. **Beschwerde nach § 66 ERegG.** Bei diskriminierender oder unverhältnismäßiger Anordnung; Anträge auf Modifikation, Kompensation, Zeitverschiebung.
6. **Einstweilige Anordnung § 68 ERegG.** Bei drohender Trassenabsage prüfen; Frist eng, Antrag im laufenden Beschwerdeverfahren.
7. **Rechtsschutz.** Klage VG Köln gegen ablehnende BNetzA-Entscheidung; § 80 Abs. 5 VwGO gegen sofort vollziehbare Verfügungen.
8. **Schadensersatz.** Zivile Ansprüche gegen EIU bei vertraglicher Trassenzusage (§§ 280, 281 BGB analog; § 33 EVO-Charta) parallel verfolgen.

## Mustertexte
- Beschwerde § 66 ERegG: Sachverhalt, Verspätungs- und Umleitungsdaten, betroffene Trassen, Anträge.
- Eilantrag § 68 ERegG mit Glaubhaftmachung (Buchungslagen, Drittverträge).
- Stellungnahme im TCR-Konsultationsverfahren: Vorschläge zur Verkürzung der Sperrpause, Mehrarbeit nachts, Splittung in mehrere Pakete.

## Quellenpflicht
- ERegG aktueller Stand.
- BNetzA-Veröffentlichungen zur Trassen- und TCR-Praxis.
- Az. von BNetzA-Beschlüssen generisch; konkrete Beschlüsse vom Anwender zu verifizieren.
- VG Köln, OVG Münster, BVerwG mit Datum, Az., freier Fundstelle.
- Zitierweise nach `references/zitierweise.md`.

## Ausgabeformat
- Beschwerdeschrift mit Auswirkungs-Datenanlagen.
- Eilantrag § 68 ERegG.
- Kommunikationsplan EVU-EIU-BNetzA (Eskalationspfad).

## Beispiele
- EVU Schienengüter rügt 6-monatige Vollsperrung ohne ausreichende Umleitungstrasse. Beschwerde § 66 ERegG mit Antrag auf Korridoröffnung am Wochenende.
- Personennahverkehr-EVU beanstandet Sperrpausenkonzept ohne Schienenersatzverkehr. Beschwerde plus Schadensersatz nach Verkehrsverträgen ÖPNV.
- TCR-Konsultation zu Generalsanierung Korridor 2026: Stellungnahme eines Halterverbands mit Alternativvorschlägen.

## Qualitätsgate
TCR-Anmeldung fristgemäß? Vorrangkriterien § 51 ERegG bewertet? Eilbedürftigkeit dargelegt? Kompensationsangebote dokumentiert? Schadensersatzweg getrennt geprüft? Parallelverfahren EBA-Eisenbahnaufsicht reflektiert?

## 6. `eisenbahn-beschwerde-evu-gegen-infrastrukturbetreiber`

**Fokus:** Eisenbahn / Beschwerde EVU gegen Infrastrukturbetreiber: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, AEG, EU-Eisenbahnrecht.

# Beschwerde eines EVU gegen den Infrastrukturbetreiber nach § 66 ERegG

## Zweck und Anwendungsfall
Anwaltliche Führung einer Beschwerde eines Eisenbahnverkehrsunternehmens (EVU) oder eines Zugangsberechtigten gegen ein Eisenbahninfrastrukturunternehmen (EIU) bei der Bundesnetzagentur nach § 66 ERegG. Typische Streitgegenstände: Diskriminierung beim Trassenzugang, beim Zugang zu Serviceeinrichtungen, beim Stationszugang, in den Schienennetz-Benutzungsbedingungen, bei Entgelten und Bonus-Malus-Anwendung. Adressat ist die BNetzA als Regulierungsstelle Eisenbahn (Spartenkammer für Eisenbahn nach BNetzAG; konkrete BK-Bezeichnung vom Anwender zu verifizieren).

## Eingaben
- Beschwerdeführer (EVU, Zugangsberechtigter, Halterverband, Schienenpersonenverkehr-Besteller).
- Beschwerdegegner (DB InfraGO, regionaler Betreiber, Halterstation-Betreiber, Wartungseinrichtung).
- Konkreter Streitgegenstand und Datum der Maßnahme.
- Vorprozessuale Schritte (interne Reklamation, Schlichtung).
- Bestehende Verträge (Infrastruktur-Nutzungs-Vertrag INV, Trassen-Vereinbarung).

## Rechtsrahmen
- §§ 66–73 ERegG (Beschwerdeverfahren der BNetzA).
- § 66 ERegG (Beschwerderecht der Zugangsberechtigten).
- § 67 ERegG (Auskunfts- und Prüfungsrechte BNetzA).
- § 68 ERegG (einstweilige Anordnung).
- § 73 ERegG (Verpflichtung des EIU, BNetzA-Entscheidungen umzusetzen).
- § 76 ERegG (Genehmigungsvorbehalt Entgelte).
- § 79 ERegG (sofortige Vollziehbarkeit).
- RL (EU) 2012/34 (SERA-Richtlinie), VO (EU) 2017/2177 (Serviceeinrichtungen).
- §§ 5a, 14, 14f AEG (Aufsicht EBA als Schnittstelle).
- §§ 19, 20 GWB (Diskriminierungs- und Behinderungsverbote als Parallelweg).

## Ablauf
1. **Aktivlegitimation prüfen.** EVU mit Sicherheitsbescheinigung, Halter, Trassenanmelder mit eigenem Recht; § 1 Abs. 12 ERegG-Definition prüfen.
2. **Verfahrensgegenstand strukturieren.** Konkrete Maßnahme (Ablehnung Trasse, Entgeltforderung, Sperrpausen-Anordnung, AGB-Klausel SNB).
3. **Tatsachenbasis dokumentieren.** Datum, Korrespondenz, Trassen-Anmeldung, Antworten EIU, alternative Marktdaten.
4. **Diskriminierungs-Vergleich.** Vergleich zu konzernverbundenen EVU (DB-Konzern); Bündelungs- und Vorzugsbehandlungs-Indikatoren.
5. **Konkrete Anträge.** Untersagung, Modifikation, Festsetzung des Entgelts, Verpflichtung zur Zuweisung, einstweilige Anordnung § 68 ERegG.
6. **Parallel-Verfahren.** Kartellrechtliche Klage nach §§ 19, 20 GWB beim LG bzw. OLG Frankfurt für Kartellbeschwerden; nicht durch ERegG ausgeschlossen.
7. **Akteneinsicht.** § 71 i. V. m. § 67 ERegG; Schwärzungs-Streit (siehe Schwärzungs-Skill im selben Plugin).
8. **Rechtsschutz.** Klage VG Köln gegen ablehnende BNetzA-Entscheidung; § 80 Abs. 5 VwGO gegen § 79 ERegG-Vollziehbarkeit.

## Mustertexte
- Beschwerdeschrift § 66 ERegG: Beschwerdeführer, Beschwerdegegner, Sachverhalt, Diskriminierungs-/Verstoß-Beleg, Anträge, Beweismittel.
- Eilantrag § 68 ERegG mit Glaubhaftmachung.
- Stellungnahme des EIU als Beschwerdegegner: Verteidigung der Entscheidung, Verhältnismäßigkeit, Alternativvorschläge.

## Quellenpflicht
- ERegG aktueller Stand.
- BNetzA-Berichte (Marktuntersuchungen Eisenbahn, Jahresbericht Eisenbahn).
- Az. BNetzA-Beschlüsse generisch (z. B. BK10-XX-XXX-XX); konkretes Az. vom Anwender zu verifizieren.
- VG Köln, OVG Münster, BVerwG mit Datum, Az., freier Fundstelle.
- EuGH zu RL 2012/34 mit konkretem Datum und Az.
- Zitierweise nach `references/zitierweise.md`.

## Ausgabeformat
- Beschwerdeschrift (15–40 Seiten).
- Datenanlagen (Trassen-Anfragen, Antworten, Vergleichswerte).
- Eilantrag (separat oder im Beschwerde-Schriftsatz).

## Beispiele
- Privates Güter-EVU rügt Ablehnung einer Trasse zugunsten DB Cargo. Beschwerde § 66 ERegG, Beweis durch Vergleich Trassen-Anfrage und -Bescheid.
- EVU Personenverkehr rügt überhöhte Stationsentgelte. Beschwerde § 66 ERegG, gleichzeitig Genehmigungsverfahren § 33 ERegG.
- Schienenersatzverkehr-Logistiker rügt Zugang zu Wartungseinrichtung. Beschwerde § 66 ERegG i. V. m. § 11 ERegG.

## Qualitätsgate
Aktivlegitimation tragfähig? Streitgegenstand präzise eingegrenzt? Diskriminierungs-Vergleich belegt? Eilfristen kalendarisiert? Parallelweg GWB-Klage abgewogen? Akteneinsicht/Schwärzungs-Strategie geklärt?

## 7. `eisenbahn-eisenbahnregulierung-eregg`

**Fokus:** Eisenbahn / Eisenbahnregulierung ERegG: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, AEG, EU-Eisenbahnrecht.

# Eisenbahnregulierung nach dem ERegG: Überblick und anwaltlicher Einstieg

## Zweck und Anwendungsfall
Anwaltlicher Allgemein-Skill für Mandate nach dem Eisenbahnregulierungsgesetz (ERegG). Das ERegG setzt die SERA-Richtlinie (RL 2012/34/EU) um und ordnet die regulatorische Aufsicht der Bundesnetzagentur über die Eisenbahninfrastruktur, das Trassen- und Entgeltsystem und die Wettbewerbsneutralität zwischen integrierten und nicht-integrierten EVU. Der Skill steuert die Erfassung des Mandats, die Wahl des passenden Fachmodule (Trassenzugang, Entgelte, Serviceeinrichtungen, Beschwerde EVU gegen EIU usw.) und die Sicherung der Fristen.

## Eingaben
- Mandantenrolle (EVU, EIU, Halter, Trassenbörse, Verband, Aufgabenträger ÖPNV, Speditions-Kunde).
- Sektor (Personenfern, Personennah, Güter, Werks- und Anschlussbahnen).
- Regulierungsanliegen (Zugang, Entgelt, Diskriminierung, Sperrpause, Anreizsystem, Genehmigung).
- Verfahrensstand bei BNetzA, EBA, EuGH.
- Vertragslage (Infrastrukturnutzungsvertrag INV, Trassenvereinbarung, Bahnhofs-Nutzungsvertrag).

## Rechtsrahmen
- ERegG vom 29. August 2016 in der jeweils aktuellen Fassung.
- Allgemeines Eisenbahngesetz (AEG); §§ 5a, 14, 14f AEG.
- RL (EU) 2012/34 (SERA, einheitlicher europäischer Eisenbahnraum); RL (EU) 2016/2370 (vierter Eisenbahnpaket, market pillar).
- DVO (EU) 2015/909 (direkte Kosten); DVO (EU) 2015/10 (Antragsberechtigte); VO (EU) 2017/2177 (Serviceeinrichtungen); VO (EU) 2018/545 (Fahrzeuggenehmigung); VO (EU) 2017/2225 (Lizenzen).
- §§ 102 ff. GWB (Vergaberecht bei Beschaffungen für Eisenbahninfrastruktur).
- Eisenbahnbundesamt (EBA) als Sicherheits- und Aufsichtsbehörde (§ 5 AEG).

## Ablauf
1. **Mandatsstruktur erfassen.** Rolle, Streitwert, Zeithorizont, Konflikt mit DB-Konzern oder regionalem Betreiber.
2. **Verfahrensschiene wählen.** Konsultation der Schienennetz-Benutzungsbedingungen (§§ 26 ff. ERegG), Beschwerde § 66 ERegG, Genehmigungsverfahren Entgelte § 76 ERegG, einstweilige Anordnung § 68 ERegG.
3. **EU-Rechtsbezug klären.** SERA-Konformität, EuGH-Auslegung, Schnittstelle zu RailNetEurope-Standards.
4. **Schnittstelle EBA und sonstige Behörden.** Sicherheits- und Aufsichtsfragen (EBA), Genehmigungen, Schnittstelle zu Aufgabenträgern (Bestellerentgelte SPNV).
5. **Vertrags-Layer.** Welche Klauseln im INV sind Streitthema? Schnittstelle zu §§ 280, 281 BGB-Schadensersatz bei vertraglicher Trassenzusage.
6. **Wettbewerbsrechtlicher Parallelweg.** § 19 GWB (marktbeherrschender Infrastrukturbetreiber), § 20 GWB (Diskriminierungsverbot), private Durchsetzung beim LG.
7. **Akteneinsicht und Schwärzungen.** § 71 i. V. m. § 67 ERegG; Bezug zum Skill aktenzugang-geschaeftsgeheimnisse-schwaerzung.
8. **Rechtsschutz.** Klage VG Köln gegen BNetzA-Entscheidungen; § 80 Abs. 5 VwGO gegen § 79 ERegG-Vollziehbarkeit; Vorlage EuGH bei unklarer SERA-Auslegung.

## Mustertexte
- Mandats-Triage-Memo: Rolle, Sachverhalt, Fachmodul-Routing, Frist, erste Maßnahmen.
- Beschwerde § 66 ERegG (Grobgliederung).
- Stellungnahme im Konsultationsverfahren §§ 26, 56 ERegG.

## Quellenpflicht
- ERegG, AEG, einschlägige Durchführungsverordnungen aus dem amtlichen Quellen (BGBl., BAnz, EUR-Lex).
- BNetzA-Marktuntersuchung Eisenbahn (Jahresbericht).
- BNetzA-Beschluss-Az. (z. B. BK10-XX-XXX-XX) generisch; konkrete Beschlüsse vom Anwender zu verifizieren.
- BVerwG, OVG Münster, VG Köln, EuGH mit Datum, Az., freier Fundstelle.
- Zitierweise nach `references/zitierweise.md`.

## Ausgabeformat
- Triage-Memo (1–3 Seiten).
- Routing-Empfehlung in den Fachmodul des Plugins (Trassenzugang, Entgelte, Serviceeinrichtungen, Stationszugang, Beschwerde EVU gegen EIU, Sperrpausen, Netznutzungsbedingungen, Anreizsetzung, Kapazitätskonflikt).
- Erste Maßnahmenliste (Fristen, Beweissicherung, Konsultations-Stellungnahme).

## Beispiele
- Personenfern-EVU bittet um Erstkontakt zur Streitlage Trassen 2026. Triage: Routing in Fachmodul eisenbahn-trassenzugang.
- Aufgabenträger SPNV bittet um Memo zu Stationsentgelten. Triage: Routing in eisenbahn-stationszugang.
- Schienengüter-EVU bittet um Erstkontakt wegen Bonus-Malus. Triage: Routing in eisenbahn-anreizsetzung-schiene.

## Qualitätsgate
Mandantenrolle eindeutig? Fachmodul-Routing klar? Frist sofort kalendarisiert? Konsultations- und Konflikt-Statuspunkt erfasst? EuGH-Vorlagerisiko reflektiert?

## 8. `eisenbahn-entgeltregulierung-schiene`

**Fokus:** Eisenbahn / Entgeltregulierung Schiene: anwaltlicher für Verfahren, Anzeigen, Beschwerden, Stellungnahmen, Compliance und Rechtsschutz bei der Bundesnetzagentur. Quellenanker: ERegG, AEG, EU-Eisenbahnrecht.

# Eisenbahn: Entgeltregulierung Schiene

## Fachkern: Eisenbahn: Entgeltregulierung Schiene
- **Spezialgegenstand:** Eisenbahn: Entgeltregulierung Schiene - genau diese Verfahrenslage wird als eigenes Mandat behandelt, nicht als allgemeiner BNetzA-Chat.
- **Normen- und Behördenanker:** ERegG, AEG, Nutzungsbedingungen, Trassen-/Serviceeinrichtungszugang, Entgeltkontrolle, Diskriminierungsverbot und Beschwerdeverfahren.
- **Spezifische Weiche:** Kläre Infrastrukturbetreiber, Zugangsprodukt, Fahrplan-/Trassenperiode, Entgeltbestandteil, Nutzungsbedingung und ob vorab eine Unterrichtung oder nachträglich eine Beschwerde läuft.
- **Beleglogik:** Jede Zahl, Schwelle, Netzkomponente, Frist oder technische Behauptung braucht Quelle: Bescheid, Konsultationsdokument, Erhebungsbogen, Registerauszug, Vertrag, Messdaten, Ticket oder Behördenmail.
- **Taktischer Output:** Erzeuge nicht nur eine Checkliste, sondern eine Beschlusskammer-taugliche Kurzposition mit Antrag/Einwand, Beleganlage, offener Live-Quelle und nächstem Verfahrensschritt.

## Fachliche Weichenfragen
- Wer fragt in welcher Rolle und welches Arbeitsergebnis wird gebraucht?
- Welche Frist, Zuständigkeit, Behörde, Gericht oder Vertragssituation ist erkennbar?
- Welche Dokumente, Zahlen, Registerdaten, Bescheide, Verträge oder Korrespondenz liegen vor?
- Welche Tatsachen sind sicher, welche sind streitig und welche Annahmen müssen sichtbar markiert werden?
- Welche live zu prüfenden Normen, Behördenhinweise oder Formulare tragen das Ergebnis?

## Prüf- und Arbeitslogik
1. **Einordnen:** Rolle, Ziel, Verfahrensstand, Vertragstyp, Behörde/Gericht, Frist und Risiken festhalten.
2. **Normen live prüfen:** Vor tragenden Aussagen den aktuellen Stand aus amtlichen oder frei zugänglichen Quellen kontrollieren. Besonders prüfen: die im Fachkern genannten Normen-/Quellenanker, aktuellen amtlichen oder frei zugänglichen Fachquellen und die für diese Speziallage tragenden Formulare/Behördenhinweise.
3. **Tatbestand in Elemente zerlegen:** Jedes Tatbestandsmerkmal einzeln prüfen; unklare Tatsachen als `[offen: ...]` markieren.
4. **Belege führen:** Für jede relevante Behauptung Dokument, Datum, Absender, Anlage, Registerfund oder Quelle notieren.
5. **Gegenansicht bauen:** Mindestens eine ernsthafte Gegenargumentation und eine Verteidigungslinie formulieren.
6. **Ergebnis kalibrieren:** Risikoampel `grün/gelb/rot`, Handlungsempfehlung, nächster Schritt und fehlende Unterlagen ausgeben.

## Output
Erzeuge je nach Auftrag eines oder mehrere dieser Arbeitsergebnisse: Kurzvermerk, Prüfschema, Risikoampel, Fragenliste, Dokumentenanforderung, Entwurfsbausteine und nächster Handlungsschritt. Wenn der Nutzer unsicher ist, schlage zuerst einen Minimalpfad vor: Frist sichern, Dokumente sortieren, Kernfrage beantworten, danach Spezialprüfung vertiefen.

## Quellenhygiene
- Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen erfinden.
- Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei/amtlich prüfbarer Quelle nennen.
- Bei EU-Recht den aktuellen EUR-Lex-Text und einschlägige Kommissions-/Agenturhinweise prüfen.
- Bei Behördenverfahren aktuelle Formulare, Merkblätter, Konsultationen und Fristen der zuständigen Behörde prüfen.

## Qualitätsgate
Am Ende kurz prüfen: Sind Fristen, Zuständigkeit, Rechtsgrundlage, Beweislast, Zahlen, Form und gewünschter Output vollständig? Ist erkennbar, was sicher ist und was noch Sachverhaltsarbeit braucht?
