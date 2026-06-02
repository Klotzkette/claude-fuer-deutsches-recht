---
name: dsv-risikobewertung-enisa-schweregrad
description: "Wendet die ENISA-Methodik Recommendations for a methodology of the assessment of severity of personal data breaches auf einen konkreten Vorfall an. Behandelt: Data Processing Context DPC; Ease of Identification EI; Circumstances of Breach CB; Schweregradformel SE = DPC × EI + CB; vier Stufen Low Medium High Very High; Übersetzung in Meldepflicht Art. 33 und Benachrichtigung Art. 34 DSGVO. Output: quantitative ENISA-Bewertung mit Faktoren und Schwellenwerten. Abgrenzung: keine EDSA-Beispielmethodik; keine Behördenmeldung."
---

# ENISA-Methodik zur Schweregradbewertung von Datenschutzverletzungen

## Triage — kläre vor der Bearbeitung

1. Welche Verarbeitungskontextstufe (DPC) liegt vor — einfach, behavior, sensitive, oder highly sensitive?
2. Wie leicht sind Betroffene identifizierbar (EI von 0,25 bis 1)?
3. Welche Umstände erhöhen oder mindern das Risiko (CB-Faktoren)?
4. Welche Daten sind besonders schutzbedürftig?
5. Wie ist die quantitative Bewertung zu kommunizieren?
- Was will der Mandant wirklich erreichen? (objektivierte Bewertung; Verteidigung gegen Behörde)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 DSGVO** Meldepflicht.
- **Art. 34 Abs. 1 DSGVO** Benachrichtigung.
- **Erwägungsgrund 75; 76 DSGVO**.
- **ENISA Recommendations for a methodology of the assessment of severity of personal data breaches** (2013, weiterhin in Praxis verwendet).
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Akzeptanz der ENISA-Methodik durch deutsche Aufsichtsbehörden vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 Abs. 1; Art. 34 Abs. 1; Art. 5 Abs. 2 DSGVO; ENISA-Methodik 2013.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — ENISA-Berechnung

DPC: simple data 1; behavioural data 2; sensitive data 3; highly sensitive data 4.

EI: negligible 0,25; limited 0,5; significant 0,75; maximum 1.

CB: -2 bis +0,5 je nach Umständen (Loss of confidentiality, integrity, availability; malicious intent; etc.).

SE = DPC × EI + CB.

Stufen: SE < 2 Low; 2-3 Medium; 3-4 High; > 4 Very High.

Conclusion: Meldung Art. 33 ab Medium; Benachrichtigung Art. 34 ab High.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-risikobewertung-edsa-leitlinie` ergaenzt um qualitative Beispielfallgruppen.
