---
name: eskalationsmatrix
description: "Definiert eine Eskalationsmatrix vom Erstmelder über Service-Desk und Datenschutzbeauftragten bis zur Geschäftsleitung und externen Beratern. Behandelt: Schwellenwerte für Eskalation; Erreichbarkeit außerhalb der Bürozeiten; Stellvertreter; Wochenend- und Feiertagsregelung; Eskalationsprotokoll; Ausweichkommunikation bei IT-Ausfall. Output: Matrix mit Stufen und Verantwortlichen plus Erreichbarkeitsplan. Abgrenzung: keine konkrete Stakeholder-Information."
---

# Eskalationsmatrix Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Welche Schwellenwerte rechtfertigen welche Eskalationsstufe?
2. Welche Erreichbarkeit ist außerhalb der Bürozeiten gewährleistet?
3. Wer entscheidet über externe Eskalation (Anwalt, Versicherung, Behörde)?
4. Welche Ausweichkommunikation gilt bei IT-Ausfall (Mobilfunk, persönlich, Pager)?
5. Wer dokumentiert die Eskalationsentscheidung?
- Was will der Mandant wirklich erreichen? (klare Entscheidungswege; keine Eskalation läuft ins Leere)

## Rechtsgrundlagen

- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Art. 24 DSGVO** Verantwortung des Verantwortlichen.
- **Art. 32 DSGVO** technische und organisatorische Maßnahmen.
- **Art. 33 Abs. 1 DSGVO** Meldepflicht binnen 72 Stunden.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Bußgeldfälle wegen verspäteter Meldung infolge Eskalationsversagen vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 2; Art. 24; Art. 32; Art. 33 Abs. 1 DSGVO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Eskalationsstufen

Stufe 1: Erstmelder → Service-Desk (innerhalb 30 Minuten).
Stufe 2: Service-Desk → DSB / IT-Sicherheit (innerhalb 1 Stunde).
Stufe 3: DSB → Geschäftsleitung und Anwalt (innerhalb 4 Stunden).
Stufe 4: Geschäftsleitung → Cyberversicherung und Aufsichtsbehörde (innerhalb 24 Stunden ab Kenntnisnahme).
Stufe 5: Pressemitteilung und Mitarbeiter-Information (nach Lagebeurteilung).

Erreichbarkeit: Hauptkontakt + zwei Stellvertreter je Stufe; 24/7-Rufbereitschaft definieren.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.
