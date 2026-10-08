# Formate und Schnittstellen der Vergabestelle

Diese Referenz steuert den belastbaren Weg von Bestands-, Planungs- und Vergabedaten in Vergabeunterlagen, Bekanntmachungen, Wertung und Vergabeakte. Technische Konvertierung ersetzt weder fachliche Freigabe noch vergaberechtliche Begründung.

## 1. Formatfamilien und Schutzregeln

| Format oder Kanal | Typische Nutzung | Schutzregel |
|---|---|---|
| GAEB DA XML | Bau-LV, Angebotsaufforderung, Angebot, Auftrag | Positionen, Mengen, Einheiten, Kurz- und Langtexte sowie Ordnungszahlen nicht frei umschreiben. |
| GAEB 90 und GAEB 2000 | Ältere Bau-LV mit D- oder P-Dateiendungen | Header, Austauschphase, Kodierung und Importprotokoll vor Bearbeitung sichern. |
| XML, eForms, TED | Bekanntmachung, Berichtigung, strukturierter Austausch | Schema, Pflichtfelder, Zeichensatz, Notice-ID und Rückmeldung prüfen. |
| Excel | Preisblatt, Eignungs- und Wertungsmatrix | Blattnamen, Formeln, Sperren, Rundungen und Pflichtfelder erhalten; sichtbare Werte und Formeln vergleichen. |
| PDF | Formblätter, Vertragsbedingungen, Pläne, Anlagen | Text-PDF, Scan und Formular unterscheiden; OCR-Ergebnis stets gegen Seitenbild prüfen. |
| ZIP oder Portalcontainer | Unterlagenpaket und Veröffentlichung | Dateibaum, Originalnamen, Hashes, Version und Entpackfehler protokollieren. |
| API, MCP, REST, SOAP, OData, IDoc, BAPI, SFTP | Lese-, Prüf- oder Rückkanal | Berechtigung, Feldmapping, Lauf-ID, Delta und Rückmeldung festhalten; keine ungeprüfte Schreibaktion. |

## 2. Quellsysteme nach fachlicher Funktion

| Datenfamilie | Typische Systeme oder Dateien | Zulässiger Beitrag zur Vergabe | Feldautorität vor Übernahme |
|---|---|---|---|
| Bauwerks- und Anlagenbestand | SIB-Bauwerke, Anlagenregister, Bestandsdatenbank | Objekt, Bauteil, Lage, Zustandsmerkmal | Verantwortliche Bestandsführung und Stichtag |
| Zustand und Erhaltung | PMS/BMS, Heller, EPING, Prüfberichte | Dringlichkeit, Schadensbild, Prüfdatum | Fachprüfung; Prognose und Befund getrennt |
| Planung und Geometrie | Bestandsplan, BIM/IFC, Allplan, VESTRA, AwF, OKSTRA | Mengenansatz, Geometrie, Korridor, Arbeitspaket | Freigegebener Planstand und Modellversion |
| Kosten und Termine | SAP/ERP, Haushaltsdaten, Nachträge, historische Kosten und Bauzeiten | Schätzung, Losbildung, Termin- und Risikomodell | Kostenstand, Preisbasis, Index und Freigabe |
| Umwelt und Regelwerk | Klima-, Pegel-, Schutzgebiets-, Normen- und Rechtsdaten | Ausführungsfenster, Mindestanforderung, Genehmigungsrisiko | Gültigkeitsstand und räumlicher Bezug |
| Vergabe und Kommunikation | DMS/E-Akte, eForms/TED, DVAL, Vergabeportal, E-Mail | Verfahrensstand, Veröffentlichung, Rückfrage, Entscheidung | Portalquittung oder freigegebener Aktenstand |

Eine Quelle ist nur für die benannten Felder maßgeblich. Ein Kostenexport beweist keine technische Eignung; ein Modellstand beweist keine Bekanntmachung; eine Prognose wird nicht durch Formatkonvertierung zum Befund.

## 3. GAEB-Phasen

- Phase 81: Leistungsverzeichnis oder Leistungsbeschreibung.
- Phase 82: Kostenansatz oder Kostenberechnung, abhängig vom Formatstand.
- Phase 83: Angebotsaufforderung mit LV.
- Phase 84: Angebot mit Bieterpreisen.
- Phase 85: Nebenangebot.
- Phase 86: Auftrag oder Zuschlag.

Dateiendungen können je nach Formatstand als D, P oder X auftreten, etwa D83, P83 oder X83. Wenn eine Bezeichnung wie G48, GAE oder GAB genannt wird, nicht raten: Dateiendung, Binärheader oder XML-Root, Austauschphase, Portalhinweis und beigefügte Anleitung feststellen. Technischer Quellenanker: [GAEB FAQ zum Datenaustausch](https://www.gaeb.de/en/service/faq/data-exchange/).

## 4. Kanonischer Datenumschlag

Für jedes entscheidungsrelevante Feld erfassen:

| Feld | Pflichtinhalt |
|---|---|
| Objekt | Bauwerk, Los, Position, Kriterium oder Dokument |
| Herkunft | System, Datei, Tabellenblatt, Zeile, Modellobjekt oder API-Endpunkt |
| Feldautorität | Fachlich verantwortliche Stelle und Geltungsbereich |
| Stand | Exportzeit, Stichtag, Version und Hash |
| Rohwert | Unveränderter Quellwert |
| Transformation | Einheit, Rundung, Aggregation, Filter oder Berechnungsregel |
| Arbeitswert | In Planung oder Unterlage verwendeter Wert |
| Status | belegt, plausibilisiert, streitig, geschätzt oder offen |
| Vergaberelevanz | Bedarf, Menge, Mindestanforderung, Zuschlagskriterium, Schätzung oder Risiko |
| Freigabe | Person, Zeitpunkt, Umfang und Zielsystem |

Bei Widerspruch gilt: nicht still überschreiben. Beide Werte erhalten, zeitliche und fachliche Vorrangregel nennen, Konflikt entscheiden lassen und Entscheidung mit Grund protokollieren.

## 5. Vergabestellen-Gate

1. Leitformat und verbindliche Fassung bestimmen.
2. Feldautoritäten und Stichtage vor der ersten Transformation festlegen.
3. X83 oder D83 testweise ausgeben, leere Bepreisung prüfen und X84 oder D84 wieder einlesen.
4. Bekanntmachung, Bewerbungsbedingungen, LV, Preisblatt und Vertragsentwurf auf dieselben Begriffe, Lose und Pflichtfelder abgleichen.
5. Technische Vorgabe auf Leistungsbezug, Wettbewerbsoffenheit und Gleichwertigkeitszugang prüfen.
6. Bestands- oder Prognosedaten nur über eine dokumentierte Entscheidungsbrücke in Mindestanforderung, Zuschlagskriterium, Schätzung oder Losbildung überführen.
7. Jede Berichtigung mit Delta, Fristwirkung, ersetzten Dateien und Portalquittung in die Akte schreiben.

## 6. Rechtliche System-Gates

- **EuGH, 16.04.2026, C-568/24, Sof Medica:** Technische Spezifikationen dürfen den Wettbewerb nicht ohne sachlichen Leistungsbezug verengen. Bezeichnungen einer bestimmten Art, Herkunft oder Herstellung brauchen grundsätzlich den Gleichwertigkeitszugang, sofern der Auftragsgegenstand nicht unvermeidbar etwas anderes verlangt. Konsequenz: Systemkompatibilität konkret belegen und nicht als bloße Produktpräferenz formulieren.
- **OLG Düsseldorf, 10.07.2024, Verg 2/24:** Eine vorhandene IT-Landschaft, Systemsicherheit, Umstellungsrisiken und Gewährleistungsfragen können Produktbindung oder Bündelung tragen, wenn die Stelle die konkrete Ausgangslage und die Risiken vorab belastbar ermittelt und dokumentiert. Konsequenz: Schnittstelleninventar, Migrationsrisiko und Alternativenvergleich in die Vergabeakte.
- **OLG Düsseldorf, 13.05.2019, Verg 47/18:** Vergabeunterlagen müssen vollständig, unmittelbar und über den bekannt gemachten elektronischen Zugang erreichbar sein. Konsequenz: kein versteckter Pflichtbestandteil in einem nicht eindeutig eingebundenen Fremdsystem.
- **EuGH, 03.07.2025, verb. Rs. C-534/23 P und C-539/23 P, Instituto Cervantes:** Die Entscheidung betrifft unmittelbar eine EU-Eigenvergabe nach der EU-Haushaltsordnung und dient im deutschen Verfahren nur als Integritätsanker neben § 53 VgV und der konkreten Portalvorgabe. Ist ein Upload verlangt, ersetzt ein nach Fristablauf veränderbarer Hyperlink die hochzuladende Unterlage nicht.
- **OLG Düsseldorf, 24.03.2021, Verg 34/20:** Punktzahlen oder Bewertungsbögen allein tragen die qualitative Wertung nicht. Konsequenz: Eingabestand, konkrete Angebotsaussage, Einzelbegründung und Rechenweg zusammenführen.

## 7. Veröffentlichungs- und Rückkanal

| Feld | Inhalt |
|---|---|
| Zielsystem | DVAL, TED, Landesportal, E-Vergabe, DMS oder Fachsystem |
| Betriebsart | nur lesen, prüfen, Entwurf schreiben oder nach Freigabe senden |
| Objekt | Datei, Notice, Los, Nachricht oder Akteneintrag |
| Identität | Pfad, Dateiname, Version, Hash und fachlicher Schlüssel |
| Transformation | Schema- oder Feldmapping einschließlich ausgelassener Felder |
| Trockenlauf | Validatorergebnis und erwartete Rückmeldung |
| Freigabe | Berechtigte Person, Zeitpunkt und freigegebener Umfang |
| Rückkanal | Notice-ID, Upload-ID, Zeitstempel, Fehlerliste, Quittung und Delta |

Kein Upload, keine Portalabgabe und keine Bekanntmachung ohne ausdrückliche Freigabe. Für die Übergabe ist die Vorlage [`systemuebergabe-entscheidungsdaten.md`](../assets/templates/systemuebergabe-entscheidungsdaten.md) zu verwenden; ergänzend gilt [`LEGACY-SYSTEME-INTEGRATION.md`](LEGACY-SYSTEME-INTEGRATION.md).

## 8. Einreichung bei Vergabekammer oder Gericht

Vor jeder Stellungnahme oder Aktenübermittlung den aktuellen Zugang der konkret zuständigen Stelle prüfen. Für die Vergabekammern des Bundes weist das Bundeskartellamt gegenwärtig insbesondere auf den E-Mail-Zugang mit qualifizierter elektronischer Signatur für Nachprüfungsanträge, das besondere elektronische Behördenpostfach, sichere aktuelle Dateiformate und ein Größenlimit hin; Makrodateien sowie alte Office-Formate sind dort kein verlässlicher Versandweg. Maßgeblich bleiben die aktuelle [amtliche Seite zur elektronischen Kommunikation](https://www.bundeskartellamt.de/DE/Infothek_Service/Kontakt/ElektronischeKommunikation/elektronischekommunikation_node.html) und eine verfahrensbezogene Verfügung der Kammer oder des Gerichts.

Pflichtausgabe: zuständige Stelle, zulässiger Kanal, Signaturanforderung, Dateiformat, Größenlimit, Anlagenaufteilung, Versandfreigabe, Eingangsbestätigung und Abgleich mit der freigegebenen Aktenfassung. Originaldateien bleiben unverändert in der E-Akte; eine PDF-Fassung für den Versand erhält einen eigenen Hash und eine Transformationsnotiz.
