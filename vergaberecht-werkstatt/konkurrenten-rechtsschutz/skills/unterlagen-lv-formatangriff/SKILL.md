---
name: unterlagen-lv-formatangriff
description: 'Konkurrenten prüfen Leistungsbeschreibung, LV, GAEB, XML, Excel, PDF, Portalfelder und Legacy-Schnittstellen auf Typbindung, fehlende Gleichwertigkeit, Widerspruch, unvollständigen Zugang und veränderliche Abgabewege. Output Rügefundstellen, Alternative, Beweiskette, Abhilfe und Frist.'
---

# Unterlagen, LV und Formatangriff

<!-- BEGIN output-format-block (autogen) -->

## Output-Format (verbindlich)

Schriftart Times New Roman, Schriftgrad 11 pt. Dezimalgliederung 1, 1.1, 1.1.1, 2, 2.1 fortlaufend ohne Lücken, maximal vier Ebenen. Aufzählungen mit Spiegelstrich oder Bullet. Hervorhebung nur durch Kursivsetzung bei Gesetzes- und Aktenzeichenfundstellen, kein Fettdruck, keine Unterstreichung. Vollständige Regeln in [`references/OUTPUT-FORMAT.md`](../../references/OUTPUT-FORMAT.md). Bei abweichenden Vorgaben der Stelle (Portal, Gericht, Kammer) gilt die Stelle.

<!-- END output-format-block (autogen) -->


## Prüfung

1. Unterlageninventar bilden: Bekanntmachung, Bewerbungsbedingungen, Leistungsbeschreibung, LV, Preisblatt, Vertragsentwurf, ESPD, Bewertungsmatrix, Portalnachrichten.
2. Leitformat bestimmen: GAEB/X83, XML, Excel, PDF, Portalformular, SAP/ERP/AVA/DMS-Export, API/MCP-Export oder Mischpaket.
3. Rückgabeformat prüfen: GAEB/X84, Excel, PDF, ZIP, Signatur, Dateinamen, Pflichtfelder.
4. Widersprüche erfassen: Textfassung gegen Datenformat, LV gegen Preisblatt, Bekanntmachung gegen Unterlagen.
5. Angriffspunkt formulieren: Transparenz, Gleichbehandlung, Produktneutralität, Angebotsvergleichbarkeit oder Zugang.
6. Prüfen, ob Pflichtfelder, gesperrte Zellen, GAEB-Positionen, Dropdowns oder Portalvalidierungen gleichwertige Produkte, andere Materialien oder Nebenangebote technisch verhindern.
7. Bei SAP/ERP/AVA/DMS/Portal/API/MCP [LEGACY-SYSTEME-INTEGRATION.md](../../references/LEGACY-SYSTEME-INTEGRATION.md) laden und Beweis-Cluster mit Quelle, Version, Hash, Mapping, Angriff und Rückmeldung erzeugen.
8. Abhängige Unterlagen auf direkten Zugang prüfen: zweite Website, Registrierung, E-Mail-Anforderung, fehlender Plan/Modellstand oder veränderlicher Datenraum.
9. Bestandskompatibilität als mögliche Rechtfertigung ernst nehmen und mit eigener Schnittstellen-, Migrations-, Sicherheits- und Gewährleistungsalternative widerlegen.

## Rechtsprechungsanker

- EuGH, Urteil vom 16.04.2026, C-568/24, Sof Medica, ECLI:EU:C:2026:305: Typ-, Größen-, System- und Schnittstellenanforderung ohne `oder gleichwertig` angreifen, sofern sie nicht unvermeidbar aus dem Auftragsgegenstand folgt.
- EuGH, Urteil vom 16.01.2025, C-424/23, DYKA Plastics: Der Angriff richtet sich nicht nur gegen den Wortlaut, sondern auch gegen Datenformate, die Gleichwertigkeit faktisch ausschließen.
- OLG Düsseldorf, Beschluss vom 10.07.2024, Verg 2/24: Bestandskompatibilität kann die Vergabestelle verteidigen; deshalb konkrete funktionale Alternative und Risikowiderlegung liefern.
- OLG Düsseldorf, Beschluss vom 13.05.2019, Verg 47/18: vollständigen und direkten elektronischen Zugang einschließlich technischer Anlagen prüfen.
- EuGH, Urteil vom 03.07.2025, C-534/23 P und C-539/23 P, Instituto Cervantes: unmittelbar EU-Eigenvergabe; im deutschen Verfahren nur Integritätsanker neben § 53 VgV und Portalvorgabe für den fristfesten Upload.
- Bei Formatfehlern konkrete Abhilfe verlangen: alternative native Datei, korrigierte Excel, neues GAEB, PDF-Lesefassung, Klarstellung im Portal und Fristverlängerung.

## Rechtsfolge

Bei berechtigtem Fehler verlangen: Klarstellung, Berichtigung, neue Unterlagenversion, Fristverlängerung, Rückversetzung oder Aufhebung.

## Output

Tabelle mit Datei, Fundstelle, Fehler, Auswirkung auf Angebot, Rügeformulierung und gewünschter Abhilfe.

Bei Legacy-Quellen zusätzlich Herkunftszone, Anschlussmatrix, Hash- und Beweismapping-Manifest, Delta-Protokoll, Schwärzungsvorschlag und Anlagenpaket nach `assets/templates/beweiskette-systemexport.md`.
