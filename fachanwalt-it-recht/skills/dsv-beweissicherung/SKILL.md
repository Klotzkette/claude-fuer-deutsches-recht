---
name: dsv-beweissicherung
description: "Strukturiert die Beweissicherung nach einem Datenschutzvorfall so, dass die Beweismittel in einem späteren Bußgeldverfahren, Strafverfahren oder Zivilprozess verwertbar bleiben: Strukturiert die Beweissicherung nach einem Datenschutzvorfall so, dass die Bew — Arbeitskontext: Fachanwalt IT-Recht, Schwerpunkt dsv beweissicherung."
---

# Strukturiert die Beweissicherung nach einem Datenschutzvorfall so, dass die Beweismittel in einem späteren Bußgeldverfahren, Strafverfahren oder Zivilprozess verwertbar bleiben


## Aktenstart statt Formularstart

Wenn zu **It Recht Aufnahme Statusinformation Benachrichtigung Art** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt It Recht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; DSGVO; BDSG; TTDSG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturiert die Beweissicherung nach einem Datenschutzvorfall so, dass die Beweismittel in einem späteren Bußgeldverfahren, Strafverfahren oder Zivilprozess verwertbar bleiben. Behandelt: Chain of Custody; Logging-Sicherung; Speicherabbilder; Hashes; Zeugenidentifikation; Dokumentation der Wahrnehmungen; Aufbewahrungsfristen; Datenschutzbeschränkungen bei Mitarbeiterüberwachung; Telekommunikationsgeheimnis. Output: Beweissicherungs-Protokoll mit Checkliste und Übergabeformular. Abgrenzung: keine eigene Forensik; keine Strafanzeige.

### Beweissicherung nach Datenschutzvorfall — Chain of Custody

## Triage — kläre vor der Bearbeitung

1. Welche Systeme und Speichermedien sind potenziell Beweismittel?
2. Gibt es Hinweise auf einen Innentäter und damit besondere Anforderungen an die Vertraulichkeit?
3. Liegt Telekommunikationsgeheimnis nach § 3 TTDSG vor?
4. Welche Aufbewahrungsfristen gelten für die Logs?
5. Wer übernimmt die forensische Sicherung — interne IT oder externer Forensiker?
- Was will der Mandant wirklich erreichen? (gerichtsverwertbare Beweise; saubere Akte; spätere Verteidigung)

## Rechtsgrundlagen

- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.
- **Art. 32 DSGVO** angemessene Sicherheitsmaßnahmen.
- **Art. 33 Abs. 5 DSGVO** Dokumentationspflicht.
- **§ 26 BDSG** Mitarbeiterdatenverarbeitung.
- **§ 3 TTDSG** Fernmeldegeheimnis.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Beweisverwertungsverboten bei verdeckter Mitarbeiterkontrolle vor Ausgabe verifizieren.

## Zentrale Normen

Art. 5 Abs. 2; Art. 32; Art. 33 Abs. 5 DSGVO; § 26 BDSG; § 3 TTDSG.

## Praxisformulierung — Chain-of-Custody-Protokoll

Asset-ID; Beschreibung; Sicherungszeitpunkt; sichernde Person; Übergabezeitpunkt; übernehmende Person; Hashwert vor/nach Sicherung; Aufbewahrungsort; Zugriffsberechtigte; Zweck der Sicherung; Rechtsgrundlage der Verarbeitung der gesicherten Daten.

Logging: Welche Log-Quellen wurden eingefroren? Welche Retention war eingestellt? Welche Lücken gibt es?

Zeugen: Wer hat wann was wahrgenommen — in eigenen Worten und mit Zeitstempel protokollieren.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.
