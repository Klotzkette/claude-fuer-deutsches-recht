---
name: dsv-benachrichtigung-art-34-schwelle-hohes-risiko
description: "Bewertet, ob die Schwelle voraussichtlich hohes Risiko nach Art. 34 Abs. 1 DSGVO erreicht ist. Behandelt: Abgrenzung zur Meldeschwelle Art. 33 Abs. 1 DSGVO; EDSA-Beispielfallgruppen; Faktoren Schwere und Wahrscheinlichkeit; Sondergruppen Art. 9 DSGVO und Minderjährige; Klartext-Passwörter; Finanzdaten; Gesundheitsdaten; Bewertungsmemo für die Akte. Output: Schwellenentscheidung mit Begründung und Bezug auf EDSA. Abgrenzung: keine konkrete Benachrichtigung; keine Ausnahmenprüfung."
---

# Schwelle hohes Risiko nach Art. 34 Abs. 1 DSGVO

## Triage — kläre vor der Bearbeitung

1. Welche Schwere der Folgen ist plausibel und welche Wahrscheinlichkeit?
2. Welche EDSA-Beispielfallgruppe passt (Klartext-Passwort-Leak; Gesundheitsdaten-Leak; Finanzdaten-Leak)?
3. Sind besondere Schutzbedürftige betroffen (Kinder, Patienten)?
4. Welche Beweislast trifft den Verantwortlichen?
5. Welche Folgewirkung hat die Entscheidung auf Pressekommunikation und Bußgeldverfahren?
- Was will der Mandant wirklich erreichen? (begründete Entscheidung; Verteidigungsfähigkeit)

## Rechtsgrundlagen

- **Art. 34 Abs. 1 DSGVO** Schwellenwert.
- **Erwägungsgrund 75; 76; 86 DSGVO**.
- **EDSA-Leitlinien 9/2022** Beispiele.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Entscheidungen zur Schwellenwertentscheidung Art. 34 DSGVO vor Ausgabe verifizieren.

## Zentrale Normen

Art. 34 Abs. 1; Art. 5 Abs. 2 DSGVO; Erwägungsgrund 75; 76; 86; EDSA-Leitlinien 9/2022.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Bewertungsraster

Faktor 1 Schwere: gering / mittel / hoch / sehr hoch.

Faktor 2 Wahrscheinlichkeit: gering / mittel / hoch.

Faktor 3 Datenkategorie: normale Daten / Art. 9 / Finanzdaten / Identitätsdaten.

Faktor 4 Personengruppe: Erwachsene / Minderjährige / Patienten / besonders Schutzbedürftige.

Conclusion: hohes Risiko ab Schwere hoch + Wahrscheinlichkeit mittel; bei Art. 9 + Kinder regelmäßig zu bejahen.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-risikobewertung-edsa-leitlinie` und `dsv-risikobewertung-enisa-schweregrad` liefern methodische Tiefe.
