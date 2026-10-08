# Formate und Schnittstellen des Bieters

Diese Referenz steuert den Weg aus Kalkulation, Technik, Personal und Nachweisen in ein fristfestes Angebot. Entscheidend ist nicht nur, ob eine Datei geöffnet werden kann, sondern ob jede Angebotsaussage aus einer freigegebenen Quelle stammt und exakt in dem geforderten Kanal fixiert wurde.

## 1. Formatfamilien und Schutzregeln

| Format oder Kanal | Typische Nutzung | Schutzregel |
|---|---|---|
| GAEB DA XML, GAEB 90, GAEB 2000 | LV, Preisangebot, Nebenangebot | Austauschphase, Positionen, Mengen, Einheiten, Texte und Ordnungszahlen erhalten. |
| XML oder Portalformular | Eignung, Eigenerklärung, Angebot | Schema, Pflichtfelder, Zeichensatz und Portalvorschau prüfen. |
| Excel | Preisblatt, Personal-, Referenz- oder Qualitätsmatrix | Formeln, Blattnamen, Sperren, Rundungen und Pflichtfelder nicht verändern. |
| PDF | Konzept, Nachweis, Vertragserklärung, Formblatt | Lesbarkeit, Vollständigkeit, Signatur oder Textform und Seitenfolge prüfen. |
| ZIP oder Portalcontainer | Abgabepaket | Dateibaum, Originalnamen, Hashes, Virenprüfung und Entpackbarkeit sichern. |
| API, MCP, REST, SOAP, OData, IDoc, BAPI, SFTP | Import aus Unternehmenssystemen oder vorbereiteter Upload | Nur freigegebene Felder übernehmen; Lauf-ID, Mapping, Fehler und Rückmeldung protokollieren. |

## 2. Unternehmensquellen und Beweisautorität

| Angebotsaussage | Typische Quelle | Vor Übernahme zu klären |
|---|---|---|
| Einheitspreis und Gesamtpreis | ERP/SAP, Kalkulation, AVA | Kalkulationsstand, Währung, Rundung, Freigabe, enthaltene Leistungen |
| Leistungsversprechen | Planung, BIM/IFC, Arbeitsvorbereitung, technische Daten | Übereinstimmung mit LV, Terminplan und Produktnachweis |
| Personal und Verfügbarkeit | HR-System, Einsatzplanung, Verpflichtungserklärung | Person, Rolle, Zeitraum, Einwilligung und verbindliche Zusage |
| Referenz und Erfahrung | CRM, Projektakte, Abnahme, Referenzbescheinigung | Auftraggeber, Leistungsumfang, Zeitraum und Vergleichbarkeit |
| Qualität und Zertifizierung | QM-System, Zertifikat, Prüfbericht | Geltungsbereich, Aussteller, Laufzeit und Zuordnung zum Bieter |
| Nachunternehmer und Eignungsleihe | Lieferantenakte, Vertrag, Verpflichtungserklärung | Leistungsanteil, Verfügbarkeit, Ausschlussgründe und Signatur |
| Abgabe und Kommunikation | Vergabeportal, E-Mail, DMS | Fristzustand, Dateiversion, Nachricht, Quittung und Zeitstempel |

Ein Dashboardwert oder Datenbankeintrag genügt nur innerhalb seiner Beweisautorität. Eine interne Personalplanung ist keine Verpflichtungserklärung; ein CRM-Eintrag ist keine Referenzbescheinigung; ein freigegebener Preis beweist nicht die technische Erfüllung.

## 3. GAEB- und Fremdformat-Gate

- Phasen 81 bis 83 betreffen regelmäßig Leistungsbeschreibung, Kostenansatz und Angebotsaufforderung; Phase 84 das Preisangebot; Phase 85 das Nebenangebot; Phase 86 den Auftrag.
- Bei Bezeichnungen wie G48, GAE oder GAB nicht raten. Dateiendung, Binärheader oder XML-Root, Portalhinweis und Anleitung feststellen.
- Verbindliche native Datei und bloße Lesefassung unterscheiden.
- Nur vorgesehene Felder befüllen; Positionen, Lose, Mengen, Einheiten, Texte, Formeln und Pflichtkennzeichen erhalten.
- Datei nach Bearbeitung erneut mit verfügbarer Fachsoftware oder Validator öffnen und mit einer erzeugten Lesefassung vergleichen.

Technischer Quellenanker: [GAEB FAQ zum Datenaustausch](https://www.gaeb.de/en/service/faq/data-exchange/).

## 4. Source-to-Offer-Mapping

Für jede wertungs- oder eignungsrelevante Aussage erfassen:

| Feld | Pflichtinhalt |
|---|---|
| Angebotsziel | Formularfeld, LV-Position, Konzeptstelle oder Anlage |
| Quellobjekt | System, Datei, Datensatz, Tabellenzelle oder Modellobjekt |
| Verantwortliche Quelle | Fachbereich und freigegebener Stand |
| Rohwert | Unveränderter Quellwert |
| Transformation | Auswahl, Umrechnung, Rundung oder Textübertragung |
| Beleg | Nachweisdatei, Seite, Signatur und Gültigkeit |
| Angebotswert | Tatsächlich eingetragene Aussage |
| Status | bestätigt, bedingt, widersprüchlich oder offen |
| Freeze-Hash | Hash der finalen Datei oder des finalen Containers |

Widersprüche nie durch stilles Überschreiben lösen. Preis, Termin, Personal und Leistungsbeschreibung wechselseitig prüfen, Verantwortliche entscheiden lassen und Änderung vor dem Freeze erneut freigeben.

## 5. Rechtliche System-Gates

- **EuGH, 03.07.2025, verb. Rs. C-534/23 P und C-539/23 P, Instituto Cervantes:** Die Entscheidung betrifft unmittelbar eine EU-Eigenvergabe nach der EU-Haushaltsordnung und dient im deutschen Verfahren nur als Integritätsanker neben § 53 VgV und der konkreten Portalvorgabe. Ist ein Upload verlangt, zählen Datei, Hash, Portalvorschau und Quittung des fristgerechten Angebotszustands.
- **OLG Düsseldorf, 13.05.2019, Verg 47/18:** Die Vergabestelle muss vollständige Unterlagen unmittelbar über den bekannt gemachten elektronischen Weg bereitstellen. Fehlt dort ein erkennbar verbindlicher Bestandteil, Fundort, Zeitpunkt und Auswirkung sichern und rechtzeitig nachfragen oder rügen.
- **EuGH, 16.04.2026, C-568/24, Sof Medica:** Eine technische Festlegung darf Gleichwertigkeit nicht ohne zwingenden Auftragsbezug abschneiden. Gleichwertigkeit deshalb feldgenau mit Funktion, Messwert und Beleg zeigen, nicht nur ein alternatives Produkt benennen.
- **OLG Düsseldorf, 10.07.2024, Verg 2/24:** Konkrete Bestandskompatibilität und Systemrisiken können enge Vorgaben tragen. Der Bieter muss daher die behauptete Schnittstellen-, Migrations- oder Sicherheitsäquivalenz mit dem vorhandenen Systemzustand abgleichen.

## 6. Angebotsfreeze und Abgabe

1. Originalunterlagen mit Namen, Version, Quelle und Hash einfrieren.
2. Pflicht- und Ausschlussfelder aus Portal, Bewerbungsbedingungen, LV und Formblättern abgleichen.
3. Source-to-Offer-Mapping auf offene, bedingte und widersprüchliche Aussagen prüfen.
4. Native Datei, Lesefassung, Anlagen, Signatur- oder Textformnachweis als genau bezeichnetes Paket fixieren.
5. Roundtrip, Summen, Formeln, Seiten, Virenprüfung und Dateigrößen kontrollieren.
6. Upload nur nach Freigabe ausführen; Portalvorschau und Dateiliste vor endgültigem Senden vergleichen.
7. Quittung, serverseitigen Zeitstempel, Dateinamen, Größen und soweit verfügbar Hashes gegen den Freeze abgleichen.
8. Abweichung vor Frist beheben; nach Frist nichts verdeckt ersetzen, sondern Rechtslage und Portalnachweis sichern.

Für die Übergabe ist die Vorlage [`angebotsfreeze-systemuebergabe.md`](../assets/templates/angebotsfreeze-systemuebergabe.md) zu verwenden; ergänzend gilt [`LEGACY-SYSTEME-INTEGRATION.md`](LEGACY-SYSTEME-INTEGRATION.md). Kein Upload ohne ausdrückliche Freigabe.

## 7. VK- und Gerichtsversand

Den zulässigen Einreichungsweg der konkret zuständigen Vergabekammer oder des Gerichts vor Fertigstellung des Schriftsatzes live prüfen. Für einen Nachprüfungsantrag per E-Mail an die Vergabekammern des Bundes verlangt die aktuell veröffentlichte Information eine qualifizierte elektronische Signatur; daneben ist das besondere elektronische Behördenpostfach als Zugang beschrieben. Die Seite nennt PDF und gängige Bildformate als sicher verarbeitbar, schließt Makrodateien aus, warnt vor alten DOC- und XLS-Dateien und nennt ein Größenlimit. Diese Angaben nicht auf eine Landesvergabekammer oder ein OLG übertragen, sondern deren aktuelle Vorgaben gesondert feststellen: [Bundeskartellamt, elektronische Kommunikation](https://www.bundeskartellamt.de/DE/Infothek_Service/Kontakt/ElektronischeKommunikation/elektronischekommunikation_node.html).

Pflichtausgabe: Zuständigkeit, Frist, Kanal, Signatur, zulässige Formate, Größenlimit, Anlagenaufteilung, Absenderberechtigung, Versandhash und Eingangsbestätigung. Eine intern bearbeitbare Legacy-Datei wird nur als Arbeitsfassung behalten; eingereicht wird die zugelassene, visuell geprüfte Fassung mit Anlagenindex.
