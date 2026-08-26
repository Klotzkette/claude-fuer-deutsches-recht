---
name: zeitleiste
description: "Für Zeitleiste des Datenschutzvorfalls — minutiöse Rekonstruktion: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Zeitleiste des Datenschutzvorfalls — minutiöse Rekonstruktion

## Triage — kläre vor der Bearbeitung

1. Aus welchen Quellen lässt sich der Zeitstrahl rekonstruieren — Logs, E-Mails, Tickets, Aussagen?
2. Welche Zeitstempel sind in welcher Zeitzone protokolliert?
3. Wann genau hat der Verantwortliche im Sinne Art. 33 DSGVO Kenntnis erlangt?
4. Wann beginnt der 72-Stunden-Lauf — Erstwahrnehmung oder qualifizierte Kenntnis?
5. Gibt es Lücken, die durch Zeugenaussagen geschlossen werden müssen?
- Was will der Mandant wirklich erreichen? (verteidigungsfähige Zeitachse; Begründung Fristbeginn)

## Rechtsgrundlagen

- **Art. 33 Abs. 1 DSGVO** Kenntnisbegriff und 72-Stunden-Frist.
- **Erwägungsgrund 87 DSGVO** unverzügliche Feststellung.
- **Art. 33 Abs. 4 DSGVO** schrittweise Übermittlung.
- **Art. 5 Abs. 2 DSGVO** Rechenschaftspflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zur Auslegung Kenntnisbegriff und zum Beginn der 72-Stunden-Frist vor Ausgabe verifizieren.

## Zentrale Normen

Art. 33 Abs. 1; Art. 33 Abs. 4; Art. 5 Abs. 2 DSGVO; Erwägungsgrund 87.

## Praxisformulierung — Zeitleisten-Spalten

Datum/Uhrzeit (Zeitzone); Ereignis; Quelle; Akteur; Rechtsfolge; Anmerkungen; Beweismittel.

Wichtig: Kenntnisbegriff sauber dokumentieren — ein bloßer Verdacht oder Hinweis löst noch nicht den Fristlauf aus; maßgeblich ist die qualifizierte Kenntnis im Sinne Erwägungsgrund 87.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

## Vertiefung bei Bedarf

- Bei `dsv-zeitleiste` beziehungsweise Erstellt eine minutiös rekonstruierte Zeitleiste vom Eintritt der Verletzung bis zur Meldung und Benachrichtigung: [die zusätzliche Vertiefung laden](./references/vertiefung-dsv-zeitleiste.md).
