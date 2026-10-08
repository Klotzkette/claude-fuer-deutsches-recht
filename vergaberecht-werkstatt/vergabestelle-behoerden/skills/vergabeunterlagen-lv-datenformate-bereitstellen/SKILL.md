---
name: vergabeunterlagen-lv-datenformate-bereitstellen
description: 'Vergabeunterlagen aus Fach-, AVA- und Portalsystemen in GAEB, XML, Excel, PDF und ZIP bereitstellen. Prüft Feldautorität, Version, Gleichwertigkeit, direkten Zugang, unveränderbaren Rückgabeweg und Roundtrip. Output Unterlagenpaket, Formatmatrix, Delta, Bieterabfrage und Bereitstellungsvermerk.'
---

# Vergabeunterlagen und LV-Datenformate bereitstellen

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


Einsatzlage: Die Vergabestelle will Unterlagen, Leistungsverzeichnisse, Preisblätter, Formblätter und Portaldateien so bereitstellen, dass Bieter sie sicher auslesen und im verlangten Format beantworten können.

## Referenz

Bei technischen Formaten [FORMATE-UND-SCHNITTSTELLEN.md](../../references/FORMATE-UND-SCHNITTSTELLEN.md) laden. Bei SAP/ERP/AVA/DMS/Portal/API/MCP zusätzlich [LEGACY-SYSTEME-INTEGRATION.md](../../references/LEGACY-SYSTEME-INTEGRATION.md) laden.

## Unterlagenpaket

1. Vollständigkeit prüfen: Bekanntmachung, Bewerbungsbedingungen, Leistungsbeschreibung, LV, Preisblatt, Vertragsentwurf, Eignung, Zuschlagsmatrix, Anlagen, Fragen/Antworten.
2. Leitformat je Unterlage festlegen: GAEB, XML, Excel, PDF, ZIP oder Portalformular.
3. Lesefassung bereitstellen, wenn das Leitformat maschinenlesbar oder portalgebunden ist.
4. Bieterabfrage eindeutig gestalten: Welche Datei wird bepreist, welche Datei dient nur als Information, welche Anlage ist zwingend.
5. Dateinamen, Versionsnummern und Änderungslog konsistent halten.
6. Prüfen, ob technische Pflichtfelder, Dropdowns, Positionslogik oder gesperrte Zellen gleichwertige Produkte, alternative Materialien oder zulässige Nebenangebote faktisch ausschließen.
7. Für jedes aus einem Fachsystem übernommene Pflichtfeld Quelle, Originalschlüssel, Stand, Einheit, Transformation und Fachfreigabe dokumentieren.
8. Historische oder externe Daten nur als Vergabeunterlage verwenden, wenn Stichtag, Geltungsbereich und Verbindlichkeit für alle Bieter eindeutig sind.

## GAEB, XML, Excel und PDF

- GAEB: X83/D83/P83 als Angebotsaufforderung oder LV bereitstellen, Rückgabeformat für Angebot klar benennen.
- XML/eForms: Schema, Pflichtfelder, Zeichensatz und Validierung dokumentieren.
- Excel: geschützte Zellen, Formeln, Rundungen, Pflichtfelder und Plausibilitätsregeln sichtbar machen.
- PDF: Formularfelder oder Lesefassung prüfen; bei Scan eine maschinenlesbare Alternative anbieten, soweit möglich.
- ZIP: Ordnerstruktur und Inhaltsverzeichnis beilegen.
- Legacy-IT: SAP/ERP/AVA/DMS/SharePoint/E-Mail/SFTP/API/MCP nur über ein Integrations-Cluster anbinden: Quelle, Objekt, Schlüssel, Version, Hash, Mapping, Freigabe, Rückmeldung.
- Webdemo/Datenraum: veränderbare Inhalte nur ergänzend verlinken; fristgebundene Anforderungen und Nachweise als eingefrorene Datei im Portalbestand bereitstellen.

## Roundtrip-Prüfung

Vor Veröffentlichung einmal aus Sicht eines Bieters testen:

1. Unterlagen herunterladen oder aus Portal exportieren.
2. LV/Preisblatt öffnen und Pflichtfelder erkennen.
3. Testpreis eintragen oder Testangebot erzeugen.
4. Rückgabeformat wieder einlesen oder validieren.
5. Portalannahme mit identischer Datei, Hash, Dateiname, Größe und Schema testen.
6. Fehlerliste abarbeiten und Version neu dokumentieren.

## Rechtsprechungsanker

- EuGH, Urteil vom 16.04.2026, C-568/24, Sof Medica, ECLI:EU:C:2026:305: Typ-, Größen-, System- und Schnittstellenvorgaben mit `oder gleichwertig` öffnen, sofern sie nicht unvermeidbar aus dem Auftragsgegenstand folgen. Die Vergabestelle muss den Detaillierungsgrad proportional rechtfertigen können.
- EuGH, Urteil vom 16.01.2025, C-424/23, DYKA Plastics: Technische Spezifikationen und Materialvorgaben müssen Wettbewerbsoffenheit wahren. Das gilt auch in GAEB-, XML-, Excel- und Portalpflichtfeldern.
- EuGH, Urteil vom 03.07.2025, C-534/23 P und C-539/23 P, Instituto Cervantes: unmittelbar EU-Eigenvergabe; im deutschen Verfahren nur Integritätsanker neben § 53 VgV und Portalvorgabe. Verlangte Angebotsbestandteile als fristfesten Upload ermöglichen.
- OLG Düsseldorf, Beschluss vom 13.05.2019, Verg 47/18: Unterlagen einschließlich technischer Anlagen vollständig und direkt über den bekannt gemachten elektronischen Weg bereitstellen.
- OLG Düsseldorf, Beschluss vom 10.07.2024, Verg 2/24: Bestandskompatibilität kann eine spezifische Lösung tragen, braucht aber einen konkreten Bestands-, Schnittstellen-, Sicherheits- und Umstellungsbefund.

## Output

Liefere:

- Formatmatrix: Datei, Zweck, verbindlich oder Lesefassung, Rückgabeformat, Risiko.
- Bieterfreundliche Kurzabfrage: Was muss der Bieter ausfüllen, wie, bis wann, in welchem Format.
- Bereitstellungsvermerk für die Vergabeakte.
- Bei Mängeln: Berichtigungsvorschlag, Fristwirkung und Portal-/Veröffentlichungsbedarf.
- Bei Legacy-Anbindung: Hash- und Mapping-Manifest, Delta-Protokoll und Upload- oder Importauftrag.
- Bei Fachsystemdaten: Feldautoritäts- und Entscheidungsbrücke sowie die Vorlage `assets/templates/systemuebergabe-entscheidungsdaten.md`.

## Schnittstellen-Vorbereitung

Wenn ein Portal, Server oder MCP-Werkzeug angebunden werden soll, erstelle einen Schnittstellenauftrag mit Zielsystem, Aktion, Dateien, Hashes, Authentifizierung, Trockenlauf, Freigabe und Rückmeldung. Kein Upload ohne ausdrückliche Freigabe.
