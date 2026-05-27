# API-Abfrageplan: Emerald Liffey Bank plc

## Anlass

Die Bank will nach der ersten Portalveroeffentlichung nachweisen, dass die Dublin-plc als einheitlicher Rechtstraeger im Lobbyregister erscheint und die Frankfurter Zweigniederlassung nicht versehentlich oder durch parallele interne Arbeit als zweiter Eintrag veroeffentlicht wurde.

Bearbeiterin Compliance: Orlaine Keating, Dublin  
Bearbeiter Kanzlei: RAin Dr. Mareike Tamm  
Geplanter erster Abruf: 02.06.2026, 09:00 Uhr  
Interne Akte: ELB-LR-2026-05  
Erwartete Registernummer aus Portalbestaetigung: R009814

## Suchbegriffe

| Suchlauf | Begriff | Zweck | Erwartung |
|---|---|---|---|
| 1 | Emerald Liffey Bank | Haupttreffer Dublin finden | genau ein aktiver Treffer |
| 2 | Emerald Liffey Bank plc | Rechtstraegerbezeichnung exakt pruefen | R009814 |
| 3 | Emerald Liffey Frankfurt | Niederlassungs-Dublette pruefen | kein eigener zweiter Registereintrag |
| 4 | Emerald Liffey Bank Zweigniederlassung | Handelsregisterbezeichnung pruefen | kein eigener zweiter Registereintrag |
| 5 | ELB Digital Euro | Projektkuerzel im Register vermeiden | kein Treffer oder nur eigener Eintrag |

## Abfragebefehle

```bash
test -n "${LOBBYREGISTER_API_KEY:?LOBBYREGISTER_API_KEY fehlt}"

curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/registerentries?q=Emerald%20Liffey%20Bank&format=json" \
  > 2026-06-02_api_search_emerald_liffey_bank.json

curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/registerentries?q=Emerald%20Liffey%20Frankfurt&format=json" \
  > 2026-06-02_api_search_emerald_liffey_frankfurt.json

curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/registerentries/R009814?format=json" \
  > 2026-06-02_api_registerentry_R009814.json
```

## Cursor-Protokoll

| Lauf | Suchparameter | Cursor rein | Cursor raus | Treffer | Aktennotiz |
|---|---|---|---|---|---|
| 1 | `q=Emerald Liffey Bank` | keiner | `c-ELB-001-final` | 1 | Treffer R009814 |
| 2 | `q=Emerald Liffey Frankfurt` | keiner | `c-ELB-FRA-final` | 1 | Treffer ist derselbe Dublin-Eintrag |
| 3 | `q=Emerald Liffey Bank Zweigniederlassung` | keiner | `c-ELB-ZN-final` | 0 | keine zweite Registernummer |

## Entscheidungslogik

| Befund | Bewertung | Naechste Aktion |
|---|---|---|
| nur R009814 fuer Dublin-plc | Gruen | API-Diff in Akte legen |
| R009814 plus zweiter Treffer Frankfurt | Rot/Orange | Portalentwurf Frankfurt sperren, RfS-Anfrage aktualisieren |
| kein Treffer fuer Dublin | Rot | Veroeffentlichung oder Registernummer pruefen |
| Dublin-Treffer ohne klare Frankfurt-Erwaehnung | Orange | Portaltext Nachbesserung pruefen |
| Finanzdaten nur FRA-REG ohne Dublin-Steuerung | Orange | Kostenstellenmapping korrigieren |

## Zu pruefende API-Felder

- `registerNumber`
- `accountDetails.activeLobbyist`
- `accountDetails.firstPublicationDate`
- `accountDetails.lastUpdateDate`
- `registerEntryDetails.version`
- `registerEntryDetails.detailsPageUrl`
- `registerEntryDetails.pdfUrl`
- `lobbyistIdentity.companyName`
- `activitiesAndInterests`
- `employeesInvolvedInLobbying`
- `financialExpenses`
- `regulatoryProjects`
- `statements`
- `contracts`
- `codeOfConduct.ownCodeOfConduct`

## Aktenvermerk

Die API-Abfrage ist keine zweite Freigabe und ersetzt nicht die Portalbestaetigung. Sie ist der oeffentliche Nachweis, dass die im Portal freigegebene Dublin-Loesung nicht durch einen parallelen Frankfurt-Entwurf verwischt wurde.
