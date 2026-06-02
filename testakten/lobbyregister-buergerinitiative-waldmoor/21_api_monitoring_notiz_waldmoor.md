# API-Monitoringnotiz: Bürgerinitiative Waldmoor 2030

## Anlass

Die Initiative ist unsicher, ob sie nach Petition, Anhörung und späterer Bundeskampagne freiwillig oder verpflichtend registriert werden soll. Vor einer freiwilligen Registrierung soll geprüft werden, ob es bereits öffentliche Treffer gibt und ob eine Namensverwechslung mit anderen Waldmoor-Gruppen droht.

Bearbeitung: Luise Barmbek und RAin Julia Stern
Erster API-Test: 20.05.2026
Geplanter zweiter API-Test nach freiwilliger Registrierung: 10.06.2026

## Suchprofil vor Registrierung

| Suchlauf | Suchbegriff | Zweck | Erwartung |
|---|---|---|---|
| 1 | Bürgerinitiative Waldmoor 2030 | eigener Treffer? | kein Treffer |
| 2 | Waldmoor 2030 | Schreibvarianten und Mediennamen | kein Lobbyregistertreffer |
| 3 | B 449n Moortrasse | Vorhabenbezug | kein eigener Registereintrag |
| 4 | Moortrasse Moratorium | Kampagnenbegriff | kein Treffer oder themennahe Organisationen |

## API-Testbefehl

```bash
test -n "${LOBBYREGISTER_API_KEY:?LOBBYREGISTER_API_KEY fehlt}"

curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/registerentries?q=Waldmoor%202030&format=json" \
  > 2026-05-20_api_search_waldmoor_2030.json
```

## Bewertung vor Registrierung

Kein Treffer ist hier nicht automatisch "kein Risiko". Die Akte zeigt, dass die bundespolitische Kampagne Mitte Mai qualitativ anders wird: Telefonat mit BMDV, vorbereitete Anhörung, Gutachten, Spenden und direkte MdB-Kommunikation. Die API beantwortet nur, was veröffentlicht ist. Die Pflicht- oder Freiwilligkeitsfrage bleibt eine LobbyRG-Pruefung.

## Monitoring nach freiwilliger Registrierung

Nach freiwilliger Registrierung soll die API kontrollieren:

- Rechtsform als Organisation ohne eigene Rechtspersönlichkeit
- Sprecherinnen und vertretende Personen
- Tätigkeitsbeschreibung "Moratorium und Alternativenpruefung"
- Finanzierungsquellen ohne angenommene Windpark-Spende
- keine irreführende Aussage, dass alle lokalen Petitionstaetigkeiten registerpflichtig waren
- `statements` für das Gutachten nur, wenn Versand an Bundesadressaten und Uploadpflicht bejaht wurden

## Schlechte Praxis, die die Akte testen soll

Luise schreibt im Chat: "Wenn wir freiwillig drinstehen, ist doch alles safe." Das ist falsch. Freiwillige Registrierung löst Pflege-, Richtigkeits- und Offenlegungsfragen aus. Das Plugin soll diese Aussage stoppen und ein echtes Fristen- und Freigabesystem verlangen.
