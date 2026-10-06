# 1. Rechtsquellen für Krankenhaus-IT, Datenschutz und KI

**Recherche- und Abrufstand: 06.10.2026.** Diese Quellenkarten verbinden Tatbestand, Nachweis und konkrete Arbeitsschritte. Sie sind keine pauschale Betriebsfreigabe. Die Karten betreffen Datenschutz, Schweigepflicht, Forschung und Datenübermittlungen. KI-Verordnung, Medizinprodukterecht und Cybersicherheitsrecht sind zusätzlich zu prüfen.

**Quellenstatus:** „Primärtext geprüft“ bedeutet, dass der bezeichnete amtliche Originaltext tatsächlich gelesen wurde. Beim ThürKHG ist die aktuelle amtliche Konsolidierung technisch nicht vollständig abrufbar gewesen; die unten ausdrücklich ausgewiesene Kombination aus amtlicher Änderung und nichtamtlichen Konsolidierungen darf nicht als vollständig amtlich verifizierter Stand ausgegeben werden. Keine Entscheidung wird allein wegen eines Jahres „2026“ als einschlägig behandelt.

## 1.1. Einstieg: sechs verschiedene Verarbeitungen auseinanderhalten

| Vorgang im Krankenhauskonzern | Gesonderte Prüfung | Konkretes Arbeitsprodukt |
|---|---|---|
| KI erstellt aus dem aktuellen Behandlungsgespräch einen Arztbrief | Erforderlichkeit für Behandlung, Art. 6 und Art. 9 DSGVO, § 27 ThürKHG, Aufzeichnung/Transkription und Anbieterzugriff getrennt | Verarbeitungsbeschreibung; menschliche Freigabe; Löschung der nicht benötigten Audio- und Zwischendaten |
| Konzern-IT betreibt das KIS für mehrere Klinik-GmbHs | Rolle je Rechtsträger und Tätigkeit, Art. 28/26, § 27b ThürKHG, § 203 StGB; kein Konzernprivileg | Datenflusskarte, Rollenmatrix, AVV/gegebenenfalls Art.-26-Regelung, Anzeigeprüfung |
| Klinik untersucht eigene Routinedaten für Qualität oder eigene medizinische Forschung | § 6 GDNG beziehungsweise besondere Landesnorm; rechtmäßige Erhebung; Zweck und Einrichtung klar abgrenzen | Projektsteckbrief, Abwägung, Pseudonymisierung, Rechte-/Rollenkonzept, Information und Veröffentlichungspflichten |
| Schwesterklinik, Universität oder Hersteller erhält Daten für ein Forschungsprojekt | Übermittlung eigenständig legitimieren; § 27a ThürKHG/§ 6 Abs. 3 GDNG/andere einschlägige Grundlage prüfen | Empfänger- und Rechtsgrundlagenvermerk; erforderliche behördliche Entscheidung vor Beginn |
| Anbieter trainiert ein allgemein verkäufliches Modell mit Behandlungsdaten | Eigenständiger Zweck und eigene Rolle; Art. 9-Ausnahme, Übermittlungsbefugnis und Geheimnisschutz; nicht automatisch Behandlungszweck | Training standardmäßig ausschließen, soweit keine konkret geprüfte Freigabe vorliegt; separate Forschungs-/Trainingentscheidung |
| US-Support oder Unterauftragnehmer greift auf KIS-/KI-Daten zu | Tatsächlicher Empfänger, Zugriff und Land; Art. 44 ff.; DPF oder SCC mit passender Prüfung | Transferregister, DPF-Nachweis oder SCC/TIA, Maßnahmen, Neubewertungsanlass |

Ein Datenschutzhinweis informiert; er schafft keine Rechtsgrundlage. Ein AVV regelt eine Rolle; er erlaubt keine ansonsten unzulässige Übermittlung. Einwilligung, Behandlung, Forschung und Training nicht in einer Sammelcheckbox verbinden. Eine Ethikbewertung ersetzt weder die datenschutzrechtliche Grundlage noch eine gesetzlich erforderliche Behördenentscheidung.

# 2. Normen und behördliche Auslegung

## 2.1. DSGVO: Gesundheitsdaten und Rechtsgrundlagen

**Norm:** Verordnung (EU) 2016/679 v. 27.04.2016, insbesondere Art. 4 Nr. 1, 5 und 15; Art. 5, 6, 9; Erwägungsgründe 26, 35 und 48. **Status:** Primärtext geprüft. [Amtlicher Text](https://eur-lex.europa.eu/eli/reg/2016/679/oj/deu). Abruf: 06.10.2026.

**Tatbestand:** Auch indirekt aussagekräftige Medikations-, Termin- oder Metadaten können Gesundheitsdaten sein. Erkennbarkeit anhand realistischer Zusatzinformationen und Empfängerwissen prüfen. Für personenbezogene Gesundheitsdaten sind Art. 6 und eine tragfähige Ausnahme des Art. 9 Abs. 2 getrennt zu benennen. Behandlung kann Art. 9 Abs. 2 Buchst. h in Verbindung mit Abs. 3 tragen; die passende Art.-6-Grundlage hängt unter anderem von Vertrag, gesetzlicher Aufgabe und Träger ab. Forschung verlangt ihre eigene Grundlage, beispielsweise Art. 9 Abs. 2 Buchst. j mit konkret anwendbarem Recht und Art. 89. Art. 6 Abs. 1 Buchst. f beseitigt das Verbot aus Art. 9 nicht.

**Grenze:** Nicht alle Daten eines Krankenhauses sind Gesundheitsdaten; eine reine Ersatzteilnummer ohne Personenbezug ist anders einzuordnen als ein Supportticket mit Patientenkürzel, Stationsbezug und Befund. Gemeinsame Eigentümer oder Erwägungsgrund 48 schaffen kein allgemeines Konzernprivileg. „Pseudonymisiert“ bedeutet nicht automatisch „DSGVO-frei“.

**Workflowwirkung:** Für jeden Datenfluss Eingangsdatum, ursprünglichen Zweck, neuen Zweck, Kategorie, Personenbezug, Art. 6, Art. 9, besondere Krankenhausnorm und Empfänger erfassen. Ungeklärte Grundlage als offen markieren und vor Echtdatenbetrieb klären. Büroassistent ohne Patientendaten und klinische Entscheidungsunterstützung erhalten getrennte Freigaben.

## 2.2. DSGVO: Rollen, Verträge und technische Verantwortlichkeit

**Norm:** Art. 4 Nr. 7 und 8, Art. 24–28, 30 und 32 DSGVO. **Status:** Primärtext geprüft; [DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj/deu). Ergänzend: EDSA, Leitlinien 07/2020, Version 2.1, Rollen des Verantwortlichen und Auftragsverarbeiters; [amtliche Fassung](https://www.edpb.europa.eu/system/files/2023-10/EDPB_guidelines_202007_controllerprocessor_final_en.pdf). Abruf: 06.10.2026.

**Tatbestand:** Tatsächliche Entscheidungen über Zwecke und wesentliche Mittel zählen. Weisungsgebundener KIS-Betrieb kann Auftragsverarbeitung sein. Gemeinsam bestimmte Forschungszwecke können Art. 26 auslösen. Eigene Produktentwicklung des Lieferanten darf nicht durch die Überschrift „Auftragsverarbeitung“ verdeckt werden.

**Grenze:** Art. 26 ist kein Auffangvertrag für jede Kooperation. Zwei Klinik-GmbHs werden durch eine Holding nicht zu einem Verantwortlichen. Eine Person kann für verschiedene Verarbeitungsschritte unterschiedliche Rollen haben. Ein externer Supportdienst benötigt nicht automatisch Vollzugriff auf alle Patientenakten.

**Workflowwirkung:** Rechtsträger exakt benennen; je Vorgang Rollen entscheiden; Art.-28-Mindestinhalt, Unterauftragnehmer, Weisungen, Audits, Löschung/Rückgabe, Unterstützung bei Betroffenenrechten und Sicherheitsvorfällen konkretisieren. Im TOM-Anhang insbesondere Administrationszugänge, temporäre Freigaben, Protokollauswertung, Mandantentrennung, Schlüsselkontrolle, Wiederherstellungstest und Notbetrieb belegen. „ISO-zertifiziert“ ersetzt diese Prüfung nicht.

## 2.3. DSGVO: DSFA, Patienteninformation und Betroffenenrechte

**Norm:** Art. 12–15, 22, 25, 33–39 DSGVO. **Status:** Primärtext geprüft; [DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj/deu). Abruf: 06.10.2026.

**Tatbestand:** Groß angelegte Verarbeitung besonderer Datenkategorien und weitere Kriterien des Art. 35 können eine DSFA verlangen. Prüfen: Verarbeitung, Notwendigkeit/Verhältnismäßigkeit, konkrete Risiken für Betroffene, Maßnahmen und Restrisiko. Bei trotz Maßnahmen hohem Risiko Art. 36 beachten. Die Datenschutzbeauftragte berät und überwacht; die verantwortliche Leitung entscheidet und trägt Verantwortung.

**Grenze:** Ein TIA ersetzt keine DSFA, eine DSFA keine medizinische Nutzen-/Sicherheitsbewertung. Art. 22 setzt eine ausschließlich automatisierte Entscheidung mit rechtlicher oder ähnlich erheblicher Wirkung voraus. Bloßes Abnicken durch Personal ist keine wirksame menschliche Entscheidung. Für besondere Daten gilt zusätzlich Art. 22 Abs. 4; die Behandlungsausnahme des Art. 9 Abs. 2 Buchst. h allein genügt hierfür nicht.

**Workflowwirkung:** Informationen nach Art. 13/14 in verständlicher Sprache aus den tatsächlichen Datenflüssen erzeugen; Empfänger, Drittland, Zweck, Löschlogik und Rechte vollständig aufnehmen. KIS-Export und sichere Identitätsprüfung für Art.-15-Anfragen einrichten. Bei Vorfällen Kenntniszeitpunkt und Risikobewertung dokumentieren; Art.-33-Frist und Art.-34-Betroffeneninformation gesondert prüfen. Nicht jede technische Störung ist eine Datenschutzverletzung, eine unberechtigte Einsichtnahme kann aber auch ohne Datenverlust eine sein.

## 2.4. § 203 StGB: IT-Dienstleister und Geheimnisse

**Norm:** § 203 Abs. 1, 3 und 4 StGB. **Status:** Primärtext geprüft. [Amtlicher Text](https://www.gesetze-im-internet.de/stgb/__203.html). Abruf: 06.10.2026.

**Tatbestand:** Geheimnisse können sonstigen mitwirkenden Personen offengelegt werden, soweit dies für deren Mitwirkung an der beruflichen Tätigkeit erforderlich ist. Die Einbeziehung weiterer Dienstleister verlangt eine belastbare Verpflichtungskette; Abs. 4 enthält eigenständige Geheimhaltungs- und Absicherungspflichten.

**Grenze:** Ein Cloudvertrag erlaubt keinen beliebigen Zugriff. Nicht jeder Konzernmitarbeiter ist allein aufgrund seines Arbeitsverhältnisses zum Einblick in eine fremde Behandlungsakte befugt. Geheimnisschutz und DSGVO sind kumulativ zu prüfen.

**Workflowwirkung:** Patientenzugriff für Hosting, Support, Modellbetrieb und Debugging einzeln begründen; Geheimhaltungsverpflichtungen einschließlich Unterauftragnehmern dokumentieren; Zugriff auf das Erforderliche begrenzen. Ein Anbieterrecht zur eigenen Modellverbesserung nicht stillschweigend als notwendige Mitwirkung behandeln.

## 2.5. ThürKHG: besondere Landesprüfung

**Norm:** §§ 3, 27, 27a, 27b und 32 ThürKHG. **Quellenstatus mit Grenze:** Die aktuelle [amtliche Landesrechtsseite](https://landesrecht.thueringen.de/bsth/document/jlr-KHGTH2003rahmen) lieferte im Recherchezugang nur die JavaScript-Hülle. Die datenschutzrechtliche Anpassung durch Art. 31 des Gesetzes v. 06.06.2018 wurde im [amtlichen Gesetz- und Verordnungsblatt, S. 268](https://tlfdi.de/fileadmin/th3/tim/datenschutz/gesetz-und-verordnungsblatt-nr-06-2018.pdf) gelesen. Aktueller Wortlaut wurde ergänzend anhand der [nichtamtlichen Gesamtkonsolidierung](https://www.umwelt-online.de/regelwerk/gefstoff/gen_tech/th/lkhg.htm), [§ 27a](https://www.anwalt24.de/gesetze/thuerkhg/27a), [§ 27b](https://www.anwalt24.de/gesetze/thuerkhg/27b) und [§ 32](https://www.anwalt24.de/gesetze/thuerkhg/32) abgeglichen. Diese Konsolidierungen nennen als letzte Änderung Art. 2 des Gesetzes v. 30.12.2025, GVBl. 2026 S. 19. **Die vollständige amtliche Endfassung bleibt vor einer realen Einreichung nachzuprüfen.** Abruf aller Quellen: 06.10.2026.

### 2.5.1. Träger und Krankenhausgrenze

§ 3 bestimmt den Geltungsbereich; nach Abs. 3 erfassen insbesondere §§ 27–27b auch nicht öffentlich geförderte Krankenhäuser. § 27 Abs. 2 erfasst neben Patientenangaben auch im Behandlungszusammenhang bekannt gewordene Daten von Angehörigen und anderen Dritten. Die privatrechtliche Form einer kommunalen GmbH hebt die Krankenhausnormen nicht auf.

§ 27 Abs. 3 verlangt einen der bestimmten Verarbeitungszwecke beziehungsweise eine sonstige Erlaubnis oder Einwilligung; Abs. 4 unterscheidet unter anderem Forschung im Krankenhaus beziehungsweise dessen Forschungsinteresse und an den Krankenhausgewahrsam gebundene Mitwirkung Dritter. Abs. 5 begrenzt Verwaltungszwecke; Abs. 6 behandelt Übermittlungen außerhalb des Krankenhauses. Daraus keine allgemeine Datenfreigabe an die Holding ableiten.

**Workflowwirkung:** Klinikstandort, verantwortliche GmbH, aufnehmende Konzerngesellschaft und Gewahrsam/technischen Zugriff getrennt erfassen. Zusätzlich zur Spezialnorm klären, welches allgemeine Datenschutzrecht für den konkreten Träger und die Verarbeitung gilt; öffentliche Beherrschung und Teilnahme am Wettbewerb nicht aus dem Firmenzusatz „GmbH“ erraten. § 27 BDSG nicht ungeprüft auf jeden kommunalen Träger übertragen.

### 2.5.2. Externe Forschung: § 27a ThürKHG

Einwilligung ist ein gesetzlicher Weg. Der Weg ohne Einwilligung ist an die kumulativen Voraussetzungen des Abs. 2 gebunden, unter anderem den Schutz der Patientenbelange sowie eine konkrete Feststellung der obersten Krankenhausaufsicht zu erheblichem öffentlichem Forschungsinteresse und fehlender zumutbarer Alternative. Nach § 32 Abs. 1 trifft diese Feststellung das **für das Krankenhauswesen zuständige Ministerium**. DSB-Beteiligung, Übermittlungsdokumentation und Empfängerprüfung sind vorgesehen. Anonymisierung beziehungsweise Trennung identifizierender Merkmale richten sich nach dem Forschungszweck.

**Workflowwirkung:** Externe Forschungsdaten nicht allein nach einem positiven Ethikvotum versenden. Einwilligungsweg oder genau bezeichnete gesetzliche Alternative, erforderliche Behördenentscheidung, Empfängerprüfung und Veröffentlichungskonzept dokumentieren. GDNG als weitere Norm gesondert prüfen; keine pauschale Behauptung, Bundesrecht habe sämtliche Landesbedingungen beseitigt.

### 2.5.3. Outsourcing und Fernwartung: § 27b ThürKHG

Die geprüfte Fassung stellt die Verarbeitung im Krankenhaus an den Ausgangspunkt. Verarbeitung durch Auftragsverarbeiter verlangt die Voraussetzungen des Abs. 1: Vermeidung sonst unvermeidbarer Betriebsstörungen **oder** erhebliche Kostenvorteile für Teilvorgänge der automatischen Datenverarbeitung, Datenschutz/entsprechende Schweigepflicht sowie eine **rechtzeitige schriftliche Anzeige vor Auftragserteilung** über Art, Umfang und TOM. Adressat nach § 32 Abs. 2 ist das **Landesverwaltungsamt**. Der Vertrag muss die vorgesehenen Kontrollen ermöglichen. Abs. 3 erstreckt dies auf Wartung/Fernwartung, wenn personenbezogener Zugriff nicht ausgeschlossen werden kann.

**Workflowwirkung:** Cloud- und Wartungsbeschaffung erhalten einen eigenen Landesrechtsvermerk samt Nachweis der Voraussetzungen und Anzeigenentwurf. Anzeige nicht mit Genehmigung gleichsetzen. Ein Gespräch mit der DSB ist kein Ersatz für die Anzeige; §-27a-Forschungsentscheidung und Datenschutzaufsicht sind andere Zuständigkeiten.

## 2.6. GDNG: eigene Daten, konkrete Zwecke, Grenzen der Weitergabe

**Norm:** §§ 6–8 Gesundheitsdatennutzungsgesetz v. 22.03.2024. **Status:** Amtlicher Gesamttext und Einzelvorschriften geprüft; in dieser Fassung gibt es **keinen § 6a GDNG**. [Gesamttext](https://www.gesetze-im-internet.de/gdng/BJNR0660B0024.html), [§ 6](https://www.gesetze-im-internet.de/gdng/__6.html), [§ 7](https://www.gesetze-im-internet.de/gdng/__7.html), [§ 8](https://www.gesetze-im-internet.de/gdng/__8.html). Abruf: 06.10.2026.

**Tatbestand:** § 6 Abs. 1 betrifft die notwendige Weiterverarbeitung in den bezeichneten Einrichtungen rechtmäßig gespeicherter Gesundheitsdaten für Qualitätssicherung/Patientensicherheit, medizinische, rehabilitative oder pflegerische Forschung und Statistik einschließlich Gesundheitsberichterstattung. Die Voraussetzungen sind am tatsächlichen Projekt zu belegen. Pseudonymisierung, möglichst frühe Anonymisierung, Rechte-/Rollenkonzept und Protokollierung beachten. Die genannte Grenze von 30 Jahren ist eine äußerste Löschgrenze, keine pauschale Erlaubnis, sämtliche Projektdaten 30 Jahre aufzubewahren.

**Weitergabe:** § 6 Abs. 3 erlaubt keine freie konzernweite oder kommerzielle Weitergabe. Einwilligung oder eine konkrete andere gesetzliche Erlaubnis prüfen. Die besondere Möglichkeit für öffentlich geförderte Zusammenschlüsse von Gesundheitseinrichtungen, einschließlich Forschungsverbünden, verlangt eigene Voraussetzungen, angemessene Schutzmaßnahmen, eine tragfähige Interessenabwägung und die **Zustimmung der zuständigen Datenschutzaufsichtsbehörde**. Die gesetzliche Sollfrist von einem Monat macht Schweigen nicht zur Zustimmung. Eine Holding ist nicht allein wegen kommunaler Beteiligung ein qualifizierter öffentlich geförderter Forschungsverbund.

**Zusatzpflichten:** § 6 Abs. 4 verlangt zugängliche Information über Zwecke, Vorhaben und Ergebnisse sowie individuelle Erläuterung auf Anfrage. § 7 enthält Geheimhaltung und Reidentifizierungsverbote. § 8 regelt bei seiner Anwendung insbesondere Vorabregistrierung in einem WHO-anerkannten Primärregister, **soweit dieses die betreffende Projektart aufnehmen kann**, und Veröffentlichung anonymisierter Ergebnisse binnen 24 Monaten nach Abschluss; gesetzliche Ausnahmen und bereits erfüllte Registrierungspflichten prüfen.

**Workflowwirkung:** Für „Qualitätsdashboard“, „eigene Sepsisstudie“, „gemeinsame Konzernkohorte“ und „Hersteller-Fine-Tuning“ getrennte Projektkarten anlegen. Eine Karte muss Ursprung, Einrichtung, Zweck, Empfänger, Datenumfang, Rechtsweg, technische Schutzmaßnahmen, Öffentlichkeitsinformation, Registrierung und Ergebnisveröffentlichung enthalten. Die Wörter Forschung oder Qualität im Vertrag genügen nicht.

## 2.7. § 27 BDSG: wissenschaftliche Forschung

**Norm:** § 27 BDSG, insbesondere Abs. 1–4, mit § 22 Abs. 2. **Status:** Primärtext geprüft. [§ 27 BDSG](https://www.gesetze-im-internet.de/bdsg_2018/__27.html). Abruf: 06.10.2026.

**Tatbestand:** Soweit anwendbar, verlangt die einwilligungslose Verarbeitung besonderer Daten für wissenschaftliche Forschung insbesondere Erforderlichkeit, erhebliches Überwiegen des Forschungsinteresses und geeignete spezifische Sicherungen. Die Norm enthält differenzierte Regeln für Betroffenenrechte, Anonymisierung/Trennung und Veröffentlichung.

**Grenze:** „KI-Entwicklung ist Forschung“ ist keine Subsumtion. Auch ein wissenschaftliches Vorhaben hat die spezielle Krankenhaus- und Geheimnisschutzordnung sowie eine konkrete Übermittlungsbefugnis zu beachten. Die Anwendbarkeit des BDSG gegenüber einschlägigem Landesrecht ist beim kommunalen Träger zu begründen. Allgemeine Marketing- oder Produktanalyse nicht als Forschung etikettieren.

**Workflowwirkung:** Forschungsfrage, Methodik, Datenbedarf und mildere Mittel belegen; Interessenabwägung projektbezogen formulieren. Keine automatische Verweigerung sämtlicher Betroffenenrechte wegen Forschung; die jeweiligen Voraussetzungen einzeln prüfen.

## 2.8. EHDS: Planungspfad statt vorgezogener Datenerlaubnis

**Norm:** Verordnung (EU) 2025/327 v. 11.02.2025, insbesondere Art. 105. **Status:** Primärtext einschließlich Übergangsregelung geprüft. [Amtlicher Text](https://eur-lex.europa.eu/eli/reg/2025/327/oj/deu). Abruf: 06.10.2026.

| Zeitpunkt | Aussage für die Projektplanung |
|---|---|
| 26.03.2025 | Inkrafttreten; nicht mit allgemeiner Anwendbarkeit gleichsetzen |
| 26.03.2027 | Allgemeiner Anwendungsbeginn, vorbehaltlich der ausdrücklichen Sondertermine |
| 26.03.2029 | Wesentliche primäre Nutzungsregelungen für Patientenkurzakten, elektronische Verschreibungen/Abgaben; grundsätzlich Kapitel IV zur Sekundärnutzung, mit ausdrücklich bestimmten Ausnahmen |
| 26.03.2031 | Weitere prioritäre Kategorien, darunter Bildgebung, Laborergebnisse und Entlassungsberichte; besondere spätere Kategorien der Sekundärnutzung; Sonderregel für intern eingesetzte EHR-Systeme beachten |
| Weitere Sondertermine | Art. 105 enthält einzelne Ausnahmen bereits für 2027 sowie bis 2035; jede konkrete Pflicht am betreffenden Artikel verifizieren |

**Workflowwirkung:** Ein Krankenhausprojekt 2026 kann Interoperabilität, Datenqualität und spätere Antragswege vorbereiten. Es darf eine aktuelle Übermittlung an Hersteller oder Universität nicht allein mit „EHDS erlaubt Forschung“ begründen. Heutige Grundlage und künftige technische Zielarchitektur getrennt dokumentieren.

## 2.9. Drittlandübermittlung: DPF und SCC sind unterschiedliche Wege

**Normen:** Art. 44–49 DSGVO; Durchführungsbeschluss (EU) 2023/1795 v. 10.07.2023, insbesondere Art. 1; Durchführungsbeschluss (EU) 2021/914 v. 04.06.2021, Anhang, Klauseln 14–15. **Status:** Amtliche Volltexte geprüft. [DPF-Beschluss](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023D1795), [SCC-Beschluss](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32021D0914). Abruf: 06.10.2026.

**DPF-Weg:** Der Angemessenheitsbeschluss erfasst die vom Beschluss gedeckten Übermittlungen an die gelistete, passende US-Organisation. Konzernname, Zertifikat eines anderen Unternehmens oder reine EU-Rechenzentrumswerbung reichen nicht. Aktuellen Listenstatus, exakten Empfänger, erfasste Daten und Weiterübermittlungen dokumentieren. Für eine tatsächlich von Art. 45 gedeckte Übermittlung ist nicht zusätzlich automatisch ein SCC-TIA nach Klausel 14 nötig. Art. 6/9, AVV, § 203, Landesrecht und DSFA bleiben zu prüfen.

**SCC-Weg:** Richtiges Modul und ausgefüllte Anlagen verwenden. Klausel 14 verlangt die dokumentierte Bewertung des konkreten Transfers, der relevanten Gesetze und Praxis des Empfängerstaats und zusätzlicher Garantien; Klausel 15 betrifft Behördenzugriffe. Erforderliche ergänzende Maßnahmen tatsächlich technisch prüfen. Transportverschlüsselung schützt nicht vor jedem Klartextzugriff beim importierenden KI-Anbieter. Fehlen wirksame Garantien, Übermittlung aussetzen; keine grüne Ampel aus einer unterschriebenen Klausel ableiten.

**Workflowwirkung:** Verzeichnis mit Empfänger, Land, Zweck, Daten, Zugang, Subprozessoren, Rechtsinstrument, Nachweisdatum, Maßnahmen und Neubewertungsanlass. Supportzugriff, Telemetrie, Backups, Modell-Logging und Weitergabe einzeln erfassen. Art. 49 nicht als Regelersatz für laufenden Krankenhaus-Cloudbetrieb behandeln. EDSA-Empfehlungen 01/2020, Version 2.0 v. 18.06.2021, strukturieren Bestandsaufnahme, Instrument, Drittlandsbewertung, Ergänzungen, Formalitäten und laufende Kontrolle: [amtliche Fassung](https://www.edpb.europa.eu/system/files/2021-06/edpb_recommendations_202001vo.2.0_supplementarymeasurestransferstools_en.pdf).

**Aktualitätsgrenze:** Der DPF wurde im unten erläuterten Urteil T-553/23 nicht aufgehoben. Das Rechtsmittel C-703/25 P war im amtlich eingesehenen Register anhängig. Vor jeder realen Freigabe aktuellen Beschluss-, Gerichts- und Zertifizierungsstatus erneut prüfen; keine unveränderliche Zusicherung für die gesamte Vertragslaufzeit abgeben.

## 2.10. KI-Modell und Anonymität

**Quelle:** EDSA, Stellungnahme 28/2024 v. 17.12.2024, insbesondere Abschnitte 3.1–3.4. **Status:** Behördliche Auslegung, kein Gerichtsurteil; Volltext geprüft. [Amtliche Stellungnahme](https://www.edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf). Abruf: 06.10.2026.

**Aussage und Grenze:** Anonymität eines Modells ist fallbezogen zu prüfen, einschließlich Extraktions- und Ausgaberisiken. Eine Interessenabwägung nach Art. 6 ersetzt keine notwendige Art.-9-Ausnahme. Die Folgen einer rechtswidrigen Entwicklungsphase sind anhand des konkreten Entwicklungs- und Einsatzkontexts zu prüfen, nicht durch eine pauschale Aussage „jedes Modell ist rechtswidrig“ oder „Gewichte sind immer anonym“.

**Workflowwirkung:** Modellgewichte, Embeddings, Vektordatenbanken, Trainings- und Inferenzprotokolle in die Datenkarte aufnehmen. Den Lieferanten nach Trainingsquellen, Ausschluss eigener Nutzung, Löschung, Memorisationstests, Zugangsrechten und belegter Anonymitätsbewertung fragen. Bei kleinen Kohorten im ländlichen Krankenhaus auch seltene Kombinationen von Alter, Wohnort, Krankheitsverlauf und Zeitpunkten berücksichtigen.

# 3. Geprüfte Rechtsprechungsanker

Alle folgenden Entscheidungen wurden im amtlichen Original eingesehen; die Randnummern beziehen sich auf die jeweils verlinkte Fassung. **Abruf sämtlicher Originale: 06.10.2026.** Die Anwendung auf Krankenhaus-IT wird ausdrücklich als Übertragung gekennzeichnet, wenn der Ausgangsfall ein anderes Sachgebiet betrifft.

## 3.1. Gesundheitsdaten: Kontextprüfung auch 2026

**EuGH, Urt. v. 14.07.2026 – Az. C-474/24, AR u. a. / NADA Austria, ECLI:EU:C:2026:579, Rn. 57–73.** [Amtlicher Volltext](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62024CJ0474).

**Kern:** Im Zusammenhang mit veröffentlichten Anti-Doping-Verstößen hängt die Einordnung als Gesundheitsdaten von Aussagegehalt und Schlussfolgerungsmöglichkeiten ab. Nicht jede Information zu Medikamenten oder Sanktionen ist ohne Kontext bereits eine Gesundheitsangabe; konkrete Ableitbarkeit entscheidet.

**Workflowwirkung:** Übertragung auf die Krankenhaus-Datenklassifizierung: Ein Inventareintrag und ein patientenbezogenes Medikamenten-/Laborprotokoll sind getrennt zu bewerten; Kombinationen berücksichtigen. **Grenze:** Kein Urteil über Krankenhaus-KI. Die im österreichischen Dopingfall geprüfte Veröffentlichungsgrundlage lässt sich nicht auf eine Klinik übertragen.

## 3.2. Auskunft: enger Missbrauchseinwand

**EuGH, Urt. v. 19.03.2026 – Az. C-526/24, Brillen Rottler, ECLI:EU:C:2026:216, Rn. 29–45.** [Amtlicher Volltext](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62024CJ0526).

**Kern:** Auch ein erstes Auskunftsersuchen kann unter engen Voraussetzungen missbräuchlich sein; der Verantwortliche muss die erforderlichen objektiven und subjektiven Umstände nachweisen. Pauschales Misstrauen gegen eine anfragende Person genügt nicht.

**Workflowwirkung:** Ein Ausnahmefall ist durch die Rechtsstelle anhand belegter Tatsachen zu prüfen. Keine KI-gestützte Standardverweigerung für angebliche Serienanfragende. **Grenze:** Eine Patientin, die ihre Akte für einen Arzthaftungsprozess benötigt, verliert dadurch nicht den Anspruch auf erste kostenlose Kopie; zusätzlich 3.5 beachten.

## 3.3. Pseudonymisierung: Perspektive, Mittel und Zeitpunkt

**EuGH, Urt. v. 04.09.2025 – Az. C-413/23 P, EDSB / SRB, ECLI:EU:C:2025:645, Rn. 52, 68–80 und 100–112.** [Amtlicher Volltext](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62023CJ0413).

**Kern:** Pseudonymisierte Daten sind nicht notwendig für jeden Empfänger personenbezogen; entscheidend sind die praktisch vernünftigerweise nutzbaren Identifizierungsmittel und wirksamen Schutzmaßnahmen. Für den Absender mit Zuordnungsmöglichkeit bleiben sie personenbezogen. Die Informationspflicht wird nicht rückwirkend durch eine Pseudonymisierung beim Empfänger beseitigt.

**Workflowwirkung:** Klinikschlüssel, Zugriffsbefugnisse, Zusatzwissen, seltene Merkmale und Empfängerressourcen dokumentieren. **Grenze:** Ausgangsnorm ist die Verordnung (EU) 2018/1725; das Urteil behandelt die abgestimmte Begriffsauslegung zur DSGVO. Kein Freibrief, Studienexporte oder Modellgewichte mit „anonym“ zu etikettieren.

## 3.4. Nicht verschreibungspflichtig bedeutet nicht unsensibel

**EuGH, Urt. v. 04.10.2024 – Az. C-21/23, Lindenapotheke, ECLI:EU:C:2024:846, Rn. 76–90.** [Amtlicher Volltext](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62023CJ0021).

**Kern:** Bestelldaten zu apothekenpflichtigen, nicht verschreibungspflichtigen Arzneimitteln können Gesundheitsdaten sein, weil Rückschlüsse auf den Gesundheitszustand möglich sind; sichere Kenntnis einer Diagnose ist nicht erforderlich.

**Workflowwirkung:** Support-, Beschaffungs- und Portalprotokolle auf Patientenbezug und Gesundheitsinferenz prüfen. **Grenze:** Das Urteil legitimiert keine Übermittlung; die Einordnung eröffnet erst die strengere Rechtsgrundlagenprüfung.

## 3.5. Patientenakte: erste Kopie und verständlicher Inhalt

**EuGH, Urt. v. 26.10.2023 – Az. C-307/22, FT, ECLI:EU:C:2023:811, Rn. 31–43 und 75–79.** [Amtlicher Volltext](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62022CJ0307).

**Kern:** Die erste Kopie der personenbezogenen Daten ist grundsätzlich kostenlos; eine Begründung des Auskunftszwecks ist nicht erforderlich. Vollständige Dokumentwiedergabe kann nötig sein, damit die Daten verständlich sind.

**Workflowwirkung:** Der IT-Export muss die relevanten Originalinhalte bereitstellen können. Eine sprachlich geglättete KI-Zusammenfassung genügt nicht als Ersatz, wenn Befunde oder Verlauf im Original benötigt werden. Rechte Dritter, sichere Identifizierung und Übermittlung gesondert prüfen. **Grenze:** Nicht als ausnahmsloser Anspruch auf jedes fremde Dokument unabhängig von Inhalt und Drittrechten formulieren.

## 3.6. Indirekte sensible Aussagen durch Datenverknüpfung

**EuGH, Urt. v. 01.08.2022 – Az. C-184/20, Vyriausioji tarnybinės etikos komisija, ECLI:EU:C:2022:601, Rn. 123–128.** [Amtlicher Volltext](https://juris.curia.europa.eu/juris/document/document.jsf?docid=263721&doclang=DE).

**Kern:** Auch Angaben, aus denen durch gedankliche Kombination sensible Merkmale mittelbar hervorgehen, können besonderen Datenschutz auslösen.

**Workflowwirkung:** Übertragung auf klinische Metadaten und kleine regionale Kohorten: nicht nur ausdrückliche Diagnosefelder entfernen, sondern Verknüpfbarkeit prüfen. **Grenze:** Der Ausgangsfall betrifft die Veröffentlichung von Interessenerklärungen, nicht ein klinisches Forschungsprivileg.

## 3.7. SCC verlangen wirksamen Schutz

**EuGH, Urt. v. 16.07.2020 – Az. C-311/18, Schrems II, ECLI:EU:C:2020:559, insbesondere Rn. 134–135.** [Amtlicher Volltext](https://juris.curia.europa.eu/juris/document/document.jsf?docid=228677&doclang=DE).

**Kern:** Ob bei einem Transfer ausreichender Schutz besteht, ist konkret zu prüfen; erforderlichenfalls braucht es zusätzliche Garantien. Können sie nicht sichergestellt werden, muss der Transfer ausgesetzt beziehungsweise beendet werden.

**Workflowwirkung:** Bei SCC-basiertem KI-Support nicht bei der Unterschrift aufhören: Zugriffsarchitektur und tatsächliche Wirksamkeit der Maßnahmen prüfen. **Grenze:** Das Urteil erklärte den damaligen Privacy Shield für ungültig, nicht den erst 2023 erlassenen DPF. Den Rechtsstand beider Instrumente nicht verwechseln.

## 3.8. DPF: Urteil, Prüfzeitpunkt und Rechtsmittel

**EuG, Urt. v. 03.09.2025 – Az. T-553/23, Latombe / Kommission, ECLI:EU:T:2025:831, Rn. 22 und 204.** [Amtlicher Volltext](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:62023TJ0553).

**Kern:** Die Klage gegen den DPF-Angemessenheitsbeschluss wurde abgewiesen. Das Gericht beurteilt dessen Rechtmäßigkeit anhand des maßgeblichen Erlasszeitpunkts; daraus folgt keine unbegrenzte Garantie für jede spätere Entwicklung.

**Workflowwirkung:** DPF bei erfüllten Voraussetzungen als verfügbaren Transferweg prüfen und überwachen. Rechtsmittel **C-703/25 P** war im [amtlichen Verfahrensregister](https://infocuria.curia.europa.eu/tabs/redirect/juris/liste.jsf?language=de&num=C-703%2F25) bei Abruf anhängig; Registereintrag und späteren Endentscheid auseinanderhalten. **Grenze:** Keine Behauptung der Rechtskraft oder einer pauschalen Freigabe jedes US-Anbieters. Die [Kommissionsübersicht](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/eu-us-data-transfers_en) zusätzlich auf Veränderungen kontrollieren.

# 4. Quellen- und Entscheidungsnachweis im konkreten Projekt

Jede Freigabevorlage enthält mindestens: Verarbeitung und genaue Version; Rechtsträger und Rolle; Rechtsgrundlage mit Tatbestandsprüfung; Quelle und Abrufdatum; geprüfte Randnummer; tatsächlicher Beleg; Gegenargument; verbleibende Lücke; verantwortliche Stelle; nächste Prüfung. Ein älterer Grundsatz kann weiterhin tragen; eine neuere Entscheidung ersetzt ihn nur, soweit Aussage und Fallbezug dies rechtfertigen.

Eine Quellenlücke wird als solche markiert. Keine Rn., Aktenzeichen, Gesetzesnovelle oder Anbieterzertifizierung ergänzen, die nicht geprüft wurde. Bei neuer Rechtsprechung zuerst Tenor, Sachverhalt, tragende Gründe und Reichweite lesen; danach die konkrete Workflowentscheidung aktualisieren. Der hier dokumentierte Stand ist keine Zusage, dass nach dem 06.10.2026 keine Änderung eintritt.
