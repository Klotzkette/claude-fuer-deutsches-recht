---
name: dsv-risikobewertung-enisa-schweregrad
description: "Wendet die ENISA-Methodik Recommendations for a methodology of the assessment of severity of personal data breaches auf einen konkreten Vorfall an: Wendet die ENISA-Methodik Recommendations for a methodology of the assessment of severity of personal data br"
---

# Wendet die ENISA-Methodik Recommendations for a methodology of the assessment of severity of personal data breaches auf einen konkreten Vorfall an


## Direktstart: lesen, entscheiden, liefern

Beginne nicht mit einem Fragenkatalog. Wenn Material vorliegt, lies es zuerst und starte mit einer verwertbaren Arbeitshypothese:

- Frist oder Sofortrisiko.
- erkannte Rolle, Zielrichtung und Verfahrensstand.
- tragende Tatsachen aus dem Material.
- bester nächster Arbeitsschritt mit direkt nutzbarem Output.

Frage höchstens zwei Punkte nach, und nur wenn ohne diese Antwort der nächste Schritt falsch oder riskant würde. Fehlt Material vollständig, verlange nicht allgemein alle Unterlagen, sondern nenne die drei wichtigsten Dokumente und arbeite mit sichtbaren Annahmen weiter.

Starte mit einem Arbeitsprodukt, nicht mit einer Inventarliste: Kurzvermerk, Fristenblatt, Prüfmatrix, Entwurf, Fragenliste oder Entscheidungsvorschlag. Routing ist nur Mittel zum Zweck. Wenn ein Fachskill eindeutig passt, arbeite unmittelbar in dessen Richtung weiter.

Arbeitsmodus: Liefere zuerst einen nutzbaren Zwischenstand in höchstens sieben Sätzen und dann den nächsten konkreten Schritt. Frage nur nach, wenn Frist, Zuständigkeit, Beweis, Betrag oder Rechtsfolge sonst nicht belastbar bestimmbar sind. Tabellen nur für Fristen, Belege, Beträge, Varianten oder Streitstoff.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Wendet die ENISA-Methodik Recommendations for a methodology of the assessment of severity of personal data breaches auf einen konkreten Vorfall an. Behandelt: Data Processing Context DPC; Ease of Identification EI; Circumstances of Breach CB; Schweregradformel SE = DPC × EI + CB; vier Stufen Low Medium High Very High; Übersetzung in Meldepflicht Art. 33 und Benachrichtigung Art. 34 DSGVO. Output: quantitative ENISA-Bewertung mit Faktoren und Schwellenwerten. Abgrenzung: keine EDSA-Beispielmethodik; keine Behördenmeldung.

### ENISA-Methodik zur Schweregradbewertung von Datenschutzverletzungen

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
