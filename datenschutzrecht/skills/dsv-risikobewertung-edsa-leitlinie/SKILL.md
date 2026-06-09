---
name: dsv-risikobewertung-edsa-leitlinie
description: "Führt die Risikobewertung eines Datenschutzvorfalls anhand der EDSA-Leitlinie 9/2022 zu Beispielen für die Meldung von Datenschutzverletzungen durch: Führt die Risikobewertung eines Datenschutzvorfalls anhand der EDSA-Leitlinie 9/2022 zu Beispielen für die — Arbeitskontext: Datenschutzrecht DSGVO/BDSG, Schwerpunkt dsv risikobewertung edsa leitlinie."
---

# Führt die Risikobewertung eines Datenschutzvorfalls anhand der EDSA-Leitlinie 9/2022 zu Beispielen für die Meldung von Datenschutzverletzungen durch


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Führt die Risikobewertung eines Datenschutzvorfalls anhand der EDSA-Leitlinie 9/2022 zu Beispielen für die Meldung von Datenschutzverletzungen durch. Behandelt: Beispielfallgruppen Ransomware; Datenexfiltration; Insider; Verlust; Fehlversand; soziale Ingenieurkunst; jeweils mit Schwere-Schwellen für Meldepflicht Art. 33 DSGVO und Benachrichtigungspflicht Art. 34 DSGVO. Output: strukturierte Bewertung mit Bezug auf konkrete Beispielfallgruppe und begründeter Empfehlung Meldung Ja/Nein und Benachrichtigung Ja/Nein. Abgrenzung: keine Behördenmeldung; keine ENISA-Methodik.

### Risikobewertung nach EDSA-Leitlinie 9/2022

## Triage — kläre vor der Bearbeitung

1. Welcher EDSA-Beispielfallgruppe ist der Vorfall am nächsten?
2. Welche Schutzziele sind verletzt — Vertraulichkeit, Integrität, Verfügbarkeit?
3. Wie hoch ist die Anzahl Betroffener und welche Datenkategorien sind involviert?
4. Welche technischen und organisatorischen Maßnahmen waren wirksam?
5. Welche Risikoabmilderung wurde bereits umgesetzt?
- Was will der Mandant wirklich erreichen? (begründete Risikoeinschätzung; Behörden-feste Argumentation)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 DSGVO** Meldepflicht außer kein Risiko.
- **Art. 34 Abs. 1 DSGVO** Benachrichtigung bei hohem Risiko.
- **Erwägungsgrund 75; 76 DSGVO** Risikofaktoren.
- **EDSA-Leitlinien 9/2022** Beispiele für die Meldung von Datenschutzverletzungen (englisch: Examples regarding Personal Data Breach Notification).
- **EDSA-Leitlinien 4/2022** Berechnung von Geldbußen.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; aktuelle Anwendungspraxis der Aufsichtsbehörden zu EDSA-Beispielen vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 Abs. 1; Art. 34 Abs. 1 DSGVO; Erwägungsgrund 75; 76; EDSA-Leitlinien 9/2022.

## Praxisformulierung — Anwendung EDSA-Beispiele

Fallgruppe identifizieren: Ransomware mit/ohne Exfiltration; Datenexfiltration Hashes Passwörter; Insider absichtlich/unabsichtlich; Verlust verschlüsselt/unverschlüsselt; Fehlversand mit Empfängerrückläufer; soziale Ingenieurkunst.

Schwellenwerte EDSA: Meldung an Aufsichtsbehörde regelmäßig bei Ransomware mit unverschlüsselten Daten oder Exfiltration; Benachrichtigung Betroffene bei Klartext-Passwörtern, Finanzdaten, Gesundheitsdaten.

Risikomatrix: Eintrittswahrscheinlichkeit × Schwere; Begründung mit EDSA-Referenz und Begründung aus dem konkreten Fall.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-risikobewertung-enisa-schweregrad` ergaenzt um quantitative ENISA-Methodik.
