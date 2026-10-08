# Systemquellen, Datenherkunft und Übergabevertrag der Vergabestelle

Diese Referenz laden, sobald Bedarf, Auftragswert, Losbildung, Leistungsbeschreibung, Zuschlagskriterien, Wertung, Bekanntmachung oder Vergabeakte aus Fachsystemen gespeist oder in ein Zielsystem zurückgegeben werden sollen. Sie verbindet alte Dateien, moderne Schnittstellen und vergaberechtliche Entscheidungen, ohne ein Quellsystem zu ersetzen.

## Vier unverhandelbare Regeln

1. **Feldautorität statt Systemgläubigkeit:** Für jedes entscheidungserhebliche Feld wird bestimmt, welche Quelle es führen darf. Ein SAP-Budget ist nicht automatisch der geschätzte Auftragswert; eine Zustandsnote ist nicht automatisch ein Dringlichkeitsgrund.
2. **Original, Arbeitsstand und Ausgabe trennen:** Originalexport unverändert sichern, Transformation reproduzierbar protokollieren und Ausgabe gesondert hashen. Kein Rückschreiben in die führende Quelle ohne Freigabe.
3. **Tatsache, Annahme und Entscheidung trennen:** Ein Messwert ist eine Tatsache, eine Hochrechnung eine Annahme und die Los- oder Wertungsentscheidung ein begründungspflichtiger Behördenakt.
4. **Kein stilles Kriterium:** Historische Lieferantenbewertungen, Behördenfeedback oder Systemkennzahlen dürfen nicht verdeckt Eignung oder Zuschlag steuern. Maßgeblich sind nur bekannt gemachte, auftragsbezogene und überprüfbare Vorgaben.

## Quell- und Systemfamilien

| Familie | Typische Quellen und Formate | Zulässige Erstfunktion | Kritischer Kontrollpunkt |
|---|---|---|---|
| Bauwerk und Zustand | SIB-Bauwerke-nahe Register, Anlagenkataster, Heller-PMS-nahe PMS/BMS, Prüfberichte, CSV, XML, Datenbankexport | Bedarf, Zustand, Priorität, Objekt- und Losbezug vorbereiten | Objekt-ID, Prüfdatum, Zustandslogik, Fachfreigabe |
| Planung und Genehmigung | EPING-nahe Daten, Bestandspläne, Allplan, VESTRA, AwF-110-nahe Exporte, Genehmigungsplattformen | Mengen, Schnittstellen, Nebenbestimmungen, Zeitfenster | Planstand, Koordinatensystem, Genehmigungsstatus, Gültigkeit |
| Modelle und Netze | BIM/IFC, OKSTRA-nahe Netzdaten, GIS, DB-/WSV-nahe Exporte | Bauteile, Korridore, Mengen, Sperrpausen, technische Abhängigkeiten | Modellversion, Klassifikation, Geometrieprüfung, Verantwortlicher |
| Kosten, Termine und Nachträge | SAP ECC oder S/4HANA, MM/SRM/Ariba, MACH, proDoppik, historische Kosten, Nachtrags- und Bauzeitdaten | Auftragswert, Budget, Lebenszykluskosten, Risikopositionen vorbereiten | Preisbasis, Index, Umsatzsteuer, Leistungsumfang, Ausreißer |
| AVA und Leistungsverzeichnis | RIB iTWO, ORCA AVA, California, AVA.relax, GAEB 90/2000/DA XML | LV-Struktur, OZ, Menge, Einheit, Langtext, Rückgabeformat | Austauschphase, Rundung, Bedarfsposition, Text-/Datenwiderspruch |
| DMS und Vergabeakte | eAkte, SharePoint, enaio, d.velop, ELO, OpenText, Nextcloud, E-Mail | Version, Freigabe, Aktenstelle und Kommunikationsstand sichern | führende Version, Berechtigung, Zeitstempel, Aufbewahrung |
| Veröffentlichung und E-Vergabe | eForms, TED, DVAL, bund.de, Landes- und kommunale Portale | Bekanntmachung, Unterlagenzugang, Bieterkommunikation, Quittung | Notice-ID, Portal-ID, veröffentlichter Stand, direkter Zugang |
| Externe Fachquellen | DWD, Pegelonline, BfN, Schutzgebiete, technische Normen, Gesetze, Rechtsprechung | Klima-, Umwelt-, Normen- und Rechtsannahmen prüfen | amtliche Quelle, Stichtag, Lizenz, räumlicher und sachlicher Bezug |
| Transport und Anschluss | XML, CSV, JSON, XLSX, PDF/A, ZIP, SFTP, REST, SOAP, OData, IDoc, BAPI, MCP | lesen, validieren, übergeben, Rückmeldung empfangen | Authentifizierung, Schema, Rate Limit, Transaktionsgrenze, Freigabe |

## Eingangskanäle

| Kanal | Mindestbehandlung | Nicht zulässig |
|---|---|---|
| Datei-Snapshot | unveränderte Datei, Exportzeit, Systemzeit, Version, Hash und Lesefassung sichern | stilles Überschreiben oder Zusammenführen ohne Delta |
| Datenbank-/API-Export | Query oder Endpunkt, Filter, Pagination, Zeitzone, Schema und Antwortstatus protokollieren | ungeklärte Teilmenge als Vollbestand behandeln |
| MCP- oder Werkzeugaufruf | Werkzeug, Aktion, Parameter, Umfang, Rückgabe und Freigabe in den Anschlussvermerk aufnehmen | Schreibaktion, Upload oder Veröffentlichung ohne Einzelauftrag |
| Portal-/Sitzungsexport | Portal-ID, Nutzerrolle, Downloadpfad, Zeitstempel, Quittung und Fehlermeldung sichern | Screenshot als alleiniger Beleg oder veränderlicher Link als Aktenoriginal |
| Scan/PDF/E-Mail | OCR nur als Arbeitskopie, Original und Header erhalten, unsichere Zeichen markieren | OCR-Text als fehlerfreies Original ausgeben |

## Kanonischer Datenumschlag

Jede übernommene Tabelle, Datei oder API-Antwort erhält mindestens diese Metadaten:

| Feld | Inhalt |
|---|---|
| Quellenidentität | System, Mandant, Modul, Datenhalter, Exportweg |
| Geschäftsobjekt | Bauwerk, Bauteil, Maßnahme, Vergabe, Los, OZ, Bieter, Bekanntmachung oder Vertrag |
| Quellschlüssel | Original-ID und zusätzlich verwendeter Vergabeschlüssel |
| Zeitbezug | gültig ab/bis, Mess- oder Buchungsdatum, Exportzeit, Zeitzone |
| Schema und Einheit | Format, Schemaversion, Zeichensatz, Einheit, Währung, Steuerbasis, Nullwertlogik |
| Herkunftsschutz | Dateipfad oder Endpunkt, SHA-256, Signatur/Siegel, unveränderter Originalstand |
| Transformation | Quellfeld, Zielfeld, Regel, Rundung, Filter, manuelle Ergänzung, Verantwortlicher |
| Datenqualität | vollständig, lückenhaft, widersprüchlich, veraltet, geschätzt; Begründung und Fachfreigabe |
| Rechtszweck | Bedarf, Schätzung, Los, LV, Eignung, Zuschlag, Aufklärung, Bekanntmachung oder Akte |
| Schutzbedarf | personenbezogen, geheim, lizenzbeschränkt, offen; Zugriffs- und Schwärzungsregel |
| Übergabe | Zielsystem, Datei/Endpunkt, Trockenlauf, Freigabe, Empfangs-ID, Rückmeldung, Delta |

## Feldautorität und vergaberechtliche Verwendung

| Quellbefund | Darf unmittelbar tragen | Braucht zusätzliche Prüfung | Darf nicht allein tragen |
|---|---|---|---|
| Zustandsnote oder Schadensbild | Bedarfs- und Priorisierungsprüfung | Dringlichkeit, Bündelung, Ausführungsfenster | Ausnahmeverfahren wegen äußerster Dringlichkeit |
| SAP-BANF, Kostenstelle oder Budget | Mittel- und Bedarfsbezug | Auftragswert nach Gesamtvergütung, Optionen, Laufzeit und Losen | Schwellenwert oder Verfahrenswahl |
| historische Kosten/Nachträge | Vergleichs- und Risikobasis | Preisstand, Leistungsidentität, Index, Marktveränderung | aktuelle Schätzung ohne Anpassung |
| BIM-/Planmenge | LV-Vorbereitung | Modellstand, Kollisions-/Plausibilitätsprüfung, Fachfreigabe | vertragliche Menge bei ungeklärtem Planstand |
| frühere Anbieterleistung | Markterkenntnis und Vertragscontrolling | bekannt gemachtes Eignungs- oder Zuschlagskriterium und zulässiger Nachweis | verdeckte Schlechterstellung eines Unternehmens |
| Portal-/TED-Datensatz | veröffentlichter Bekanntmachungsstand | Abgleich mit freigegebenem Ausgangsdatensatz | interner Entwurf oder nicht veröffentlichte Änderung |
| automatisch berechnete Punktzahl | Rechenkontrolle | Kriterienbezug, Eingabebeleg, Einzelfallbegründung, Quervergleich | Wertungsentscheidung ohne nachvollziehbare Erwägungen |

## Konfliktauflösung

1. Konflikt nicht mitteln oder still bereinigen, sondern beide Werte mit Quelle und Zeitbezug erhalten.
2. Feldautorität bestimmen: fachlich führende Quelle, rechtlich freigegebener Stand und veröffentlichter Stand können auseinanderfallen.
3. Konflikttyp markieren: Versionskonflikt, Einheitenkonflikt, Objektverwechslung, fehlender Datensatz, manuelle Änderung oder Transformationsfehler.
4. Entscheidung treffen: fachlich klären, Annahme mit Bandbreite bilden, Unterlage berichtigen oder Feld sperren.
5. Auswirkung prüfen: Bedarf, Auftragswert, Los, Frist, LV, Kriterium, Wertung und Bekanntmachung.
6. Delta mit Altwert, Neuwert, Grund, Freigabe und betroffenen Ausgaben dokumentieren.

## Rechtsprechungs- und Normengates

| Gate | Arbeitsregel |
|---|---|
| § 121 GWB, § 31 VgV | Daten dürfen Bedarf und technische Anforderungen präzisieren; Typ-, Produkt- und Schnittstellenbezüge bleiben auf Gleichwertigkeit und Verhältnismäßigkeit zu prüfen. |
| EuGH, 16.04.2026, C-568/24, *Sof Medica*, ECLI:EU:C:2026:305 | Je detaillierter eine Typ- oder Systemanforderung, desto wichtiger der Nachweis, dass sie unvermeidbar aus dem Auftragsgegenstand folgt; andernfalls Gleichwertigkeit öffnen. Die objektive Begründung muss nicht vollständig in den Unterlagen stehen, aber belastbar vorhanden sein. |
| EuGH, 16.01.2025, C-424/23, *DYKA Plastics* | Produkt-, Material- und technische Vorgaben dürfen den Wettbewerb nicht ungerechtfertigt verengen. Das gilt auch für Pflichtfelder, Schemas und proprietäre Schnittstellen. |
| OLG Düsseldorf, 10.07.2024, Verg 2/24 | Reale Bestandskompatibilität, Systemsicherheit und Umstellungsrisiken können eine produktspezifische Gesamtvergabe tragen; erforderlich ist ein konkreter Bestands-, Schnittstellen- und Risikobefund, kein pauschales Lock-in-Etikett. |
| § 41 VgV; OLG Düsseldorf, 13.05.2019, Verg 47/18 | Alle Vergabeunterlagen müssen über den bekannt gemachten Weg vollständig, direkt und ohne wesentlichen Medienbruch zugänglich sein. Externe Fachquellen daher als eingefrorene Anlage oder klar zugänglichen Unterlagenbestand bereitstellen. |
| §§ 127 GWB, 58 und 59 VgV | Qualitäts-, Zeit-, Umwelt- und Lebenszyklusdaten müssen auftragsbezogen, transparent und effektiv überprüfbar in ein bekannt gemachtes Kriterium übersetzt werden. |
| § 8 VgV; OLG Düsseldorf, 24.03.2021, Verg 34/20 | Punkte und Systemlogs ersetzen keine Begründung. Eingabedaten, konkrete qualitative Erwägungen, Gewichtung und Quervergleich müssen nachvollziehbar bleiben. |
| EuGH, 03.07.2025, C-534/23 P und C-539/23 P, *Instituto Cervantes*, ECLI:EU:C:2025:523 | Unmittelbar EU-Eigenvergabe nach der EU-Haushaltsordnung; im deutschen Verfahren Integritätsanker neben § 53 VgV und Portalvorgabe. Ist ein Upload verlangt, Portaldesign und Unterlagenpaket auf fristfesten Inhalt und Datenintegrität ausrichten. |

## Rückgabe- und Schreibvertrag

Vor jeder Übergabe ausgeben:

1. **Zielobjekt:** SAP-BANF/Bestellung, AVA-LV, DMS-Aktenstück, eForms-Notice, Portalunterlage, Wertungsmatrix oder MCP/API-Auftrag.
2. **Operationsart:** neu anlegen, ergänzen, ersetzen, berichtigen oder nur prüfen. Keine unbestimmte Aktion wie synchronisieren.
3. **Idempotenzschlüssel:** Vergabenummer, Los, Dokument-ID, Version und Hash; erneuter Lauf darf keine Dublette erzeugen.
4. **Transaktionsgrenze:** Was wird gemeinsam freigegeben und was bleibt Entwurf?
5. **Trockenlauf:** Schema-, Pflichtfeld-, Roundtrip- und Berechtigungsprüfung vor produktiver Übergabe.
6. **Freigabe:** Fachbereich für Fachinhalt, Vergabestelle für Rechts-/Verfahrensinhalt, Systemverantwortlicher für technischen Lauf.
7. **Rückkanal:** Empfangs-ID, Zeitstempel, veröffentlichter/importierter Hash, Warnung, Fehler, Teilannahme und Rollbackstatus.

## Pflichtoutput

- System- und Quelleninventar mit Feldautorität.
- Datenumschlag und Mapping-Manifest je entscheidungserheblichem Feld.
- Konflikt- und Delta-Liste.
- Entscheidungsbrücke: Datenbefund, Norm, Annahme, Behördenentscheidung, Aktenbeleg.
- Export-/Uploadauftrag mit Trockenlauf, Freigabe und Rückkanal.
- Vergabeaktenvermerk nach der Vorlage [`systemuebergabe-entscheidungsdaten.md`](../assets/templates/systemuebergabe-entscheidungsdaten.md).
