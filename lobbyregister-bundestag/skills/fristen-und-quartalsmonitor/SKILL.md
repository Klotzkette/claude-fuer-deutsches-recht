---
name: fristen-und-quartalsmonitor
description: "Baut Fristenkalender fuer unverzuegliche Updates, Quartalsfrist fuer Stellungnahmen, sechs Monate Finanzdaten, jaehrliche Bestaetigung und Nachholfristen. Output Fristenbuch."
---

# Fristen- und Quartalsmonitor

## Einsatz

Alle laufenden Lobbyregisterfristen in eine Arbeitssteuerung bringen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Regelungsvorhaben und Dokumente laufen?
2. Wann enden Quartale und Geschaeftsjahr?
3. Welche Portalwarnungen oder RfS-Schreiben liegen vor?
4. Welche API-Nachkontrolle ist nach Quartalsupload oder Jahresupdate faellig?

## API-Wiedervorlagen

Fuer jede Portalfrist soll der Monitor eine zweite Kontrollfrist setzen: Nach Veroeffentlichung API/API-Export abrufen, `sourceDate` und Version sichern, `updateMissing`, Stellungnahmen, Regelungsvorhaben und Finanzdaten gegen die Freigabeakte pruefen. Bleibt die erwartete Aenderung oeffentlich aus, Eskalation an Portalverantwortliche und Dokumentation im Fristenbuch.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Fristenbuch mit Trigger, Frist, Vorfrist, Verantwortlichem, Status, API-Nachkontrolle und Eskalationsregel.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
