# Angebotsdaten, Systemquellen und Abgabevertrag des Bieters

Diese Referenz laden, wenn Teilnahmeantrag, Angebot, Kalkulation, Referenz, Zertifikat, Personaleinsatz, Konzept, Rüge oder Portalabgabe aus internen Systemen, alten Dateien oder Schnittstellen gespeist wird. Sie trennt den laufenden Unternehmensbestand vom fristfesten Angebotsstand.

## Vier unverhandelbare Regeln

1. **Angebotsfreeze:** Ein Angebot braucht einen eindeutig eingefrorenen Datenstand. Live-Dashboard, externer Link oder später veränderliche Datei ersetzt keinen fristgerechten Upload.
2. **Nachweisautorität:** CRM-Eintrag, Personalliste oder ERP-Stammsatz ist nur eine Quelle. Die vergaberechtliche Erklärung muss durch aktuellen, freigegebenen und zum verlangten Stichtag passenden Nachweis getragen sein.
3. **Keine stille Transformation:** Einheit, Währung, Umsatzsteuer, Rundung, Zuschlag, Nachlass und Mengeneinheit werden nie ohne protokollierte Regel umgerechnet.
4. **Kein Senden ohne Freigabe:** Import, Portaltest und technische Validierung dürfen vorbereitet werden; Angebotsabgabe, Rügeversand oder Rückschreiben brauchen eine ausdrückliche Freigabe.

## Quell- und Systemfamilien

| Familie | Typische Quellen und Formate | Angebotsfunktion | Kritischer Kontrollpunkt |
|---|---|---|---|
| ERP, Material und Preis | SAP ECC/S/4HANA, MM/SD, Ariba, Oracle, Dynamics, Materialstamm, Konditionen, CSV/IDoc/OData | Artikel, Leistungsposition, Basispreis, Lieferweg, Kostenstelle | Gültigkeitsdatum, Währung, Einheit, Steuer, Konditionsfolge |
| Kalkulation und AVA | iTWO, ORCA, California, Excel-Kalkulation, GAEB-Konverter | OZ, Menge, Einheitspreis, Zuschlag, Nachlass, Gesamtpreis | Austauschphase, Formel, Rundung, freigegebener Kalkulationsstand |
| CRM und Referenzen | Salesforce, HubSpot, Eigenentwicklungen, Projektdatenbanken | Referenzkunde, Zeitraum, Leistung, Ansprechpartner, Auftragswert | Einwilligung, Vergleichbarkeit, tatsächliche Leistung, Bestätigung |
| Personal und Einsatz | HR-System, Ressourcenplanung, Zeiterfassung, Qualifikationsmatrix | Rolle, Verfügbarkeit, Qualifikation, Zertifikat, Lebenslauf | personenbezogene Daten, Bindung, Doppelverplanung, Stichtag |
| DMS und Nachweise | SharePoint, ELO, OpenText, d.velop, Nextcloud, Zertifikatsablage | Eigenerklärung, Zertifikat, Registerauszug, Vollmacht, Konzept | Gültigkeit, Unterschrift/Textform, führende Version, Geheimnisschutz |
| Portal und Kommunikation | E-Vergabe, TED/DVAL, Landes-/Kommunalportal, E-Mail | Unterlagen, Bieterfrage, Rüge, Upload, Quittung | Nutzerrolle, Frist, Dateiname, Signatur, Zeitstempel, Eingang |
| Transport und Anschluss | XML, CSV, JSON, XLSX, PDF/A, ZIP, SFTP, REST, SOAP, OData, IDoc, BAPI, MCP | lesen, mappen, validieren, Übergabe vorbereiten | Schema, Teilmenge, Authentifizierung, Rate Limit, Freigabe |

## Kanonischer Angebotsdaten-Umschlag

| Feld | Inhalt |
|---|---|
| Quellenidentität | System, Mandant, Modul, Datenhalter, Exportweg |
| Angebotsobjekt | Vergabe, Los, OZ, Preis, Nachweis, Referenz, Person, Konzept oder Nachricht |
| Schlüssel | Vergabenummer, TED-ID, Los, OZ, Material-/Projekt-/Dokument-ID |
| Zeitbezug | gültig ab/bis, Leistungszeitraum, Exportzeit, Freeze-Zeit, Zeitzone |
| Schema und Einheit | Format, Schemaversion, Zeichensatz, Einheit, Währung, Steuer- und Rundungslogik |
| Originalschutz | Pfad/Endpunkt, SHA-256, Signatur/Siegel, unveränderter Export |
| Transformation | Quellfeld, Angebotsfeld, Regel, Filter, Rundung, manuelle Ergänzung, Verantwortlicher |
| Nachweisstatus | vorhanden, gültig, passend, unterschrieben, freigegeben, geheimnissensibel |
| Freeze | Angebotsversion, Freeze-Zeit, Inhaltsverzeichnis, Hashliste und Freigabeumfang |
| Abgabe | Zielportal, Slot, Datei, Reihenfolge, Signatur, Trockenlauf, Upload-ID, Eingangsquittung |

## Feldautorität im Bieterteam

| Angebotsfeld | mögliche führende Quelle | zusätzliche Freigabe | typische Fehlannahme |
|---|---|---|---|
| Einheitspreis | freigegebene Kalkulation/AVA | Kalkulation und Zeichnungsberechtigter | ERP-Listenpreis sei der Angebotspreis |
| Menge und OZ | veröffentlichte LV-/GAEB-Version | Angebotsleitung nach Delta-Abgleich | interne Materialmenge dürfe das LV ersetzen |
| Referenz | Projektakte und Auftraggeberbestätigung | Projektverantwortlicher/Recht | CRM-Status beweise allein die vergleichbare Leistung |
| Personal | Ressourcenplan plus Qualifikationsnachweis | Personalverantwortlicher und benannte Person, soweit nötig | bloße Stammdaten belegten Verfügbarkeit |
| Zertifikat | ausstellende Stelle/DMS-Original | Compliance oder Qualitätsmanagement | Dateiname beweise Gültigkeit und Geltungsbereich |
| Konzeptkennzahl/SLA | freigegebenes Leistungskonzept und Betriebsdaten | fachlicher Angebotsverantwortlicher | historische Bestleistung sei verbindliche Zusage |
| Portalstatus | Portalquittung und Exportlog | Angebotsleitung | lokaler Uploadbalken beweise Eingang |

## Angebotsfreeze

1. Veröffentlichte Unterlagenversion und Portalstand festhalten.
2. Alle Quellstände exportieren und hashen; Live-Ansichten als Arbeitsquelle kennzeichnen.
3. Preis-, Nachweis-, Personal- und Konzeptfelder in eine Freigabematrix überführen.
4. Native Dateien erzeugen: GAEB X84, geforderte XML/Excel/PDF, Portalformulare und ZIP-Struktur.
5. Lesefassungen und Inhaltsverzeichnis erzeugen, ohne native Dateien umzuschreiben.
6. Freeze-ID aus Vergabenummer, Los, Angebotsversion und Zeitpunkt bilden.
7. Nach Freeze nur kontrolliertes Delta: Änderungsgrund, betroffene Datei/Feld, erneute Fachfreigabe, neuer Hash.
8. Portaltest mit identischer Struktur; produktive Abgabe erst auf Einzelanweisung.
9. Quittung, Serverzeit, Upload-ID und tatsächlich angenommene Dateiliste gegen Freeze-Manifest prüfen.

## Rechtsprechungs- und Normengates

| Gate | Arbeitsregel |
|---|---|
| EuGH, 03.07.2025, C-534/23 P und C-539/23 P, *Instituto Cervantes*, ECLI:EU:C:2025:523 | Unmittelbar EU-Eigenvergabe nach der EU-Haushaltsordnung; im deutschen Verfahren Integritätsanker neben § 53 VgV und Portalvorgabe. Ist ein Upload verlangt, braucht jede Webdemo zusätzlich den fristfesten Nachweis im geforderten System. |
| § 53 VgV und Vergabeunterlagen | Verbindliches Abgabeformat, Textform/Signatur, Portalweg und Dateigrenzen vor dem Freeze bestimmen. Lokale Erstellung ersetzt keinen formgerechten Eingang. |
| EuGH, 16.04.2026, C-568/24, *Sof Medica*, ECLI:EU:C:2026:305 | Bei Typ-, System-, Größen- oder Schnittstellenvorgaben prüfen, ob die Unterlagen Gleichwertigkeit eröffnen. Funktionale Gleichwertigkeit feldgenau belegen; bei Sperre Bieterfrage/Rüge vor Ablauf der Präklusionsfrist. |
| EuGH, 16.01.2025, C-424/23, *DYKA Plastics* | Produkt-, Material- und technische Formatverengung mit konkreter Alternativlösung und Nachweisweg angreifen, nicht nur abstrakt als diskriminierend bezeichnen. |
| OLG Düsseldorf, 10.07.2024, Verg 2/24 | Eine Bestands- oder Kompatibilitätsbegründung kann berechtigt sein. Der Bieter muss daher nicht nur Offenheit verlangen, sondern Schnittstellenfähigkeit, Migrationspfad, Systemsicherheit und Gewährleistungszuordnung seiner Alternative belegen. |
| § 41 VgV; OLG Düsseldorf, 13.05.2019, Verg 47/18 | Fehlende, verstreute oder nur auf Anforderung erreichbare Unterlagen sofort in Unterlagenmatrix und Rügefrist übernehmen. |
| OLG Düsseldorf, 12.06.2024, Verg 36/23 | Bei internem Konkurrenzwissen darf aus belastbaren Indizien gerügt werden, obwohl der Bieter nur begrenzten Einblick hat; Quelle, Tatsachenkern und plausible Folge müssen aber konkret benannt werden. |

## System-zu-Angebot-Mapping

1. Quellfeld und Quellschlüssel angeben.
2. Gefordertes Angebotsfeld und Unterlagenfundstelle angeben.
3. Transformation einschließlich Einheit, Rundung und Filter ausweisen.
4. Nachweis oder Freigabe benennen, der die Aussage trägt.
5. Risiko klassifizieren: Ausschluss, Wertungsverlust, Widerspruch, Geheimnis, Datenschutz oder Portalfehler.
6. Native Ausgabedatei und Lesefassung bestimmen.
7. Delta- und Rückkanal definieren.

## Stoppsignale

- Verlangtes Feld ist im Unternehmen nicht belastbar: nicht erfinden; Lücke, Ersatznachweis oder Bieterfrage ausgeben.
- Quelle ist nach Freeze verändert: nicht still aktualisieren; Delta und erneute Freigabe.
- Weblink ist einziger Angebotsnachweis: festen Upload oder zulässige Portalalternative herstellen.
- GAEB/XML/Excel kann nicht schemafest erzeugt werden: Fachwerte liefern, native Abgabe aber bis Konverter-/Portaltest offen markieren.
- Preis, Referenz oder Personalangabe widerspricht einer anderen Anlage: Abgabe sperren, bis der Widerspruch aufgelöst ist.
- Personen- oder Geschäftsgeheimnis ohne Erforderlichkeit: minimieren, kennzeichnen und getrennten Schutzvermerk bilden.

## Pflichtoutput

- Quell- und Angebotsmapping mit Feldautorität.
- Nachweis-, Gültigkeits- und Geheimnisschutzmatrix.
- Freeze-Manifest mit Dateien, Versionen und SHA-256.
- Format-/Roundtrip-Bericht.
- Uploadauftrag und Abgabequittungs-Abgleich.
- Ausgefüllte Vorlage [`angebotsfreeze-systemuebergabe.md`](../assets/templates/angebotsfreeze-systemuebergabe.md).
