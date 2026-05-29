---
name: aktualisierung-unverzueglich
description: "Steuert unverzuegliche Updates bei Stammdaten, Personen, Tätigkeitsbeschreibung, Vorhabenbereichen, Regelungsvorhaben, Auftraegen und Auftraggebern. Output Update-Ticket."
---

# Unverzuegliche Aktualisierung

## Einsatz

Aenderungen so schnell erfassen, dass keine verspaetete Aktualisierung entsteht.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Angabe hat sich wann geaendert?
2. Ist die Aenderung registerrelevant?
3. Wer muss Text, Beleg und Freigabe liefern?
4. Welche veroeffentlichten API-Felder muessen nach der Portalaktion kontrolliert werden?

## API-Nachkontrolle

Nach einer Portalaktualisierung soll der Skill eine Wiedervorlage fuer den oeffentlichen API-Abgleich anlegen:

1. Vorherige API-Antwort oder PDF-Version aus der Akte ziehen.
2. Nach Veroeffentlichung `GET /registerentries/{registerNumber}?format=json` abrufen.
3. Wenn die Version geaendert wurde, alte und neue Version gegenueberstellen.
4. `lastUpdateDate`, `validFromDate`, `fiscalYearUpdate.updateMissing`, `refusedAnything`, Regelungsvorhaben, Stellungnahmen, Personen und Finanzdaten pruefen.
5. Abweichungen in `assets/templates/registerexport-diff.md` dokumentieren.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Update-Ticket mit Ausloeser, Pflichtfeld, Deadline, Portaltext, Verantwortlichem, API-Nachkontrolle und Kontrollpunkt.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
- Nach der Veroeffentlichung wird die API-Antwort als Beleg gesichert oder die fehlende Veroeffentlichung eskaliert.
