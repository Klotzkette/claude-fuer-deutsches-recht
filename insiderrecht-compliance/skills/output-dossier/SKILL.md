---
name: output-dossier
description: "Erstellt ein vollstaendiges Compliance-Dossier für BaFin-Anfragen, interne Audits oder Strafverteidigung aus allen Insiderrecht-Workproducts."
---

# Compliance-Dossier für BaFin-Anfragen und Verteidigung

## Rechtlicher Rahmen

Bei einer BaFin-Untersuchung nach §§ 4, 6 WpHG oder einem staatsanwaltschaftlichen
Ermittlungsverfahren muss der Emittent auf Verlangen alle relevanten Compliance-Unterlagen
vorlegen. Ein vollständiges und gut strukturiertes Dossier ist die wichtigste Verteidigungsmaßnahme.
Unvollständige oder widersprüchliche Dokumentation erhöht das Bußgeld- und Strafrisiko erheblich.

Rechtsgrundlagen:
- §§ 4, 6 WpHG (BaFin-Befugnisse): https://www.gesetze-im-internet.de/wphg/__4.html
- Art. 18 Abs. 5 MAR (Aufbewahrungspflicht): https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32014R0596
- § 97 WpHG: https://www.gesetze-im-internet.de/wphg/__97.html
- § 119 WpHG: https://www.gesetze-im-internet.de/wphg/__119.html
- BaFin-Emittentenleitfaden: https://www.bafin.de/dok/8252648

## Ziel dieses Skills

Dieser Skill konsolidiert alle Compliance-Workproducts zu einem vollständigen Dossier und
prüft es auf Vollständigkeit, Widerspruchsfreiheit und BaFin-Anfragetauglichkeit.

## Arbeitsprogramm

### Schritt 1 – Dossier-Struktur

Empfohlene Gliederung:
1. Sachverhaltschronologie (Timeline mit Datum, Ereignis, Wissensträger)
2. Insiderinformations-Qualifikation (Insidervermerk nach Skill ins-001)
3. Zwischenschritte (falls zutreffend: Skill ins-002-Matrix)
4. Ad-hoc-Dokumentation (Entwürfe, Freigaben, Verbreitungsnachweis, BaFin-Quittung)
5. Aufschubakte (falls Aufschub: Skill ins-004-Beschluss und Dokumentation)
6. Insiderliste (aktuell, DVO-konform, mit Belehrungsnachweisen)
7. Directors' Dealings / Closed Periods (alle meldepflichtigen Transaktionen)
8. Leak-Response (falls Leak: Protokoll, Forensik, Maßnahmen)
9. Red-Team-Review (Schwachstellen und Maßnahmen)
10. Rechtliche Stellungnahmen (externe Kanzlei)

### Schritt 2 – Vollständigkeitsprüfung

Checkliste je Abschnitt:
- Sind alle Zeitstempel vorhanden und widerspruchsfrei?
- Sind alle Personen (intern und extern) vollständig dokumentiert?
- Stimmen Insiderliste, Insidervermerk und Ad-hoc-Datum zeitlich überein?
- Wurden alle Dokumente im Original oder als zertifizierte Kopie gesichert?
- Gibt es widersprüchliche Aussagen zwischen E-Mails und offiziellen Dokumenten?

### Schritt 3 – BaFin-Anfrage-Management

- Benenne einen einzigen Kommunikationskanal zur BaFin (i.d.R. Compliance-Officer mit
 externer Kanzlei im Hintergrund)
- Prüfe jede BaFin-Anfrage vor Beantwortung auf Umfang und Rechtsgrundlage
- Antworte vollständig, aber nicht über den Umfang der Anfrage hinaus
- Dokumentiere jede Kommunikation mit der BaFin

### Schritt 4 – Verteidigungsstrategie

- Externe Kanzlei mit MAR-Expertise einschalten
- Dossier auf interne Widersprüche prüfen, bevor es BaFin vorgelegt wird
- Zeuge vorbereiten (Compliance-Officer, CFO): Ablauf der Entscheidungsfindung
- Kooperation als Strafmilderungsgrund prüfen

### Schritt 5 – Aufbewahrung und Zugriffsschutz

- Aufbewahrung 5 Jahre ab letztem Eintrag (Art. 18 Abs. 5 MAR)
- Zugriff auf Compliance-Dossier: nur Compliance, CFO, General Counsel
- Unveränderbare Archivierung (kein Überschreiben, kein Löschen)
- IT-Datensicherung und Off-Site-Backup

## Red-Team-Fragen

- Ist die Sachverhaltschronologie vollständig und widerspruchsfrei?
- Stimmen alle Zeitstempel in den verschiedenen Dokumenten überein?
- Gibt es interne E-Mails oder Notizen, die eine frühere Kenntnis der Insiderinformation belegen?
- Ist das Dossier in einem Format, das BaFin und Gericht schnell durcharbeiten können?
- Wurden externe Berater-Unterlagen (Kanzlei-Stellungnahmen) einbezogen?

## Ausgabeformat

Erzeuge:
1. Dossier-Inhaltsverzeichnis (mit Checkboxen für Vollständigkeit)
2. Sachverhaltschronologie-Template
3. Vollständigkeitsprüfungs-Checkliste
4. BaFin-Kommunikationsprotokoll (Anfrage × Antwort × Datum × Bearbeiter)

Belege ausschließlich mit: eur-lex.europa.eu, gesetze-im-internet.de, bafin.de, bgh.de,
dejure.org, openjur.de.
