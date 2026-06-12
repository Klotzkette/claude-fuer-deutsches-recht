# Open-Data-Monitoring-Plan

## Monitoring-Gegenstand

- Organisation oder Person:
- Registernummer:
- Beobachteter Themenbereich:
- Suchbegriffe und Schreibweisen:
- Zweck: Eigenkontrolle, Gegenparteiencheck, Marktmonitoring oder Verdachtspruefung
- Startdatum:
- Frequenz:
- Verantwortliche Stelle:

## Datenquellen

| Quelle | URL oder Endpunkt | Zweck | Frequenz | Ablage |
|---|---|---|---|---|
| Oeffentliche Detailseite |  | Sichtpruefung |  |  |
| PDF des Eintrags |  | Aktenversion |  |  |
| API Einzelabruf | `/registerentries/{registerNumber}` | maschinenlesbarer Diff |  |  |
| API Version | `/registerentries/{registerNumber}/{version}` | Historie |  |  |
| API Suche | `/registerentries?q=...` | Dubletten und Markt |  |  |
| Statistik | `/statistics/registerentries` | Datenstand belegen |  |  |

## Alarmregeln

| Ausloeser | Bewertung | Sofortaktion | Frist |
|---|---|---|---|
| eigener Eintrag inaktiv | Rot | Portalstatus prüfen | sofort |
| `updateMissing` wahr | Rot | Aktualisierungsakte oeffnen | sofort |
| neue Version ohne interne Freigabeakte | Rot | Revisionsspur prüfen | sofort |
| neue Stellungnahme fehlt im Register | Orange | Quartalsupload prüfen | naechster Arbeitstag |
| Auftraggeber/Unterauftrag weicht ab | Orange | Vertragsregister abgleichen | naechster Arbeitstag |
| Zweigniederlassung als zweiter Treffer | Orange/Rot | Doppelregistrierungsvermerk | naechster Arbeitstag |
| Kodexverstoss markiert | Rot | Compliance und Geschäftsleitung informieren | sofort |
| Gegenpartei neu registriert | Gruen/Orange | Due-Diligence-Akte aktualisieren | naechster Lauf |

## Ergebnisformat

- letzte erfolgreiche Abfrage:
- letzte API-Version:
- letzter API-Cursor:
- Anzahl Treffer:
- gespeicherte Antwortdateien:
- offene Warnungen:
- Portalaktion:
- naechster Lauf:
