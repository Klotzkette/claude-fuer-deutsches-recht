# API-Monitoringplan: Spreebogen Regulatory GmbH / Wasserstoffmandate

## Anlass

Nach Korrektur des zu breiten Auftraggebertextes soll die Agentur monatlich prüfen, ob der öffentliche Registereintrag die Mandate HansaH2 Storage AG und Nordsee Elektrolyse Konsortium GbR sauber trennt und ob die grundlegenden Stellungnahmen nach Quartalsupload sichtbar sind.

Verantwortlich intern: Malte Kruschke, Compliance Operations  
Verantwortlich Kanzlei: RA Dr. Theodor Albrecht  
Registernummer Agentur: R008442  
Monitoring-Start: 05.07.2026  
Takt: monatlich und zusätzlich nach jedem Quartalsupload

## Suchprofil

| Suchlauf | Suchbegriff | Zweck | Erwartung |
|---|---|---|---|
| Agentur | Spreebogen Regulatory | eigener Eintrag und Version prüfen | R008442 |
| Auftraggeber 1 | HansaH2 Storage | Auftraggeberbezug im Agentureintrag und möglicher eigener Eintrag | Agentur und HansaH2-Eintrag |
| Auftraggeber 2 | Nordsee Elektrolyse Konsortium | Konsortium richtig abgegrenzt | Agenturtreffer und ggf. Konsortium |
| Unterauftrag | OpenGrid Events | Unterauftrag sichtbar oder intern nachweisbar | kein eigener Auftraggeberfehler |
| Vorhaben | Wasserstoffbeschleunigungsgesetz | Regelungsvorhaben auffindbar | Agentur und themennahe Einträge |

## Abfragebefehle

```bash
test -n "${LOBBYREGISTER_API_KEY:?LOBBYREGISTER_API_KEY fehlt}"

curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/registerentries/R008442?format=json" \
  > 2026-07-05_api_registerentry_R008442.json

curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/registerentries?q=HansaH2%20Storage&format=json" \
  > 2026-07-05_api_search_hansah2_storage.json

curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/registerentries?q=Wasserstoffbeschleunigungsgesetz&format=json" \
  > 2026-07-05_api_search_wasserstoffbeschleunigungsgesetz.json
```

## Alarmregeln

| Auslöser | Bewertung | Sofortaktion |
|---|---|---|
| Auftraggebertext wieder "deutsche Wasserstoffwirtschaft" | Rot | Portaltext korrigieren, Mandantenfreigabe einholen |
| HansaH2 und Konsortium in einem Sammelauftrag vermengt | Orange | Auftraggebermatrix neu prüfen |
| OpenGrid als reiner Logistiker dargestellt | Orange | Unterauftragnehmerrolle im Register und Vertragsakte prüfen |
| Stellungnahme vom 28.05.2026 fehlt nach Quartalsupload | Rot | Upload-Log und Portalbestaetigung prüfen |
| Version geändert ohne internes Ticket | Rot | Revisionsspur öffnen |
| `refusedAnything` true | Rot | Geschäftsführung und Kanzlei informieren |

## Monitoringvermerk 05.07.2026

Die Suche nach HansaH2 Storage ergibt zwei relevante Treffer: den eigenen Auftraggeber und den Agentureintrag R008442. Der Agentureintrag nennt das konkrete Wasserstoffbeschleunigungsgesetz und grenzt HansaH2 von Nordsee Elektrolyse ab. Die alte Formulierung "deutsche Wasserstoffwirtschaft" ist nicht mehr sichtbar.

Offen bleibt, ob die Rolle von OpenGrid Events UG als inhaltlicher Unterauftragnehmer deutlich genug ist. Das nächste Update-Ticket soll nicht nur die Rechnungen, sondern auch das Stakeholder-Mapping aus Datei `18_stakeholder_mapping_opengrid.csv` einbeziehen.
