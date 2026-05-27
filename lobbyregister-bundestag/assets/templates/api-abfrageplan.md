# API-Abfrageplan Lobbyregister

## Zweck

- Mandat oder Monitoring:
- Eigener Eintrag, Gegenpartei, Auftraggeber, Unterauftragnehmer oder Marktbeobachtung:
- Rechts-/Compliance-Frage:
- Verantwortliche Person:
- Wiedervorlage:

## Offizielle Quelle

- Open Data/API: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/open-data-1049716
- API V2 YAML: https://api.lobbyregister.bundestag.de/rest/v2/R2.21-de.yaml
- Referenz im Plugin: ../../references/open-data-api-v2.md

## Suchprofil

| Suche | Begriff oder Registernummer | Ziel | Erwartetes Ergebnis | Risiko bei Abweichung |
|---|---|---|---|---|
| Freitext Organisation |  | eigener oder fremder Eintrag auffinden |  |  |
| Freitext Marke/Projekt |  | Varianten, Schreibweisen, Zweigniederlassungen finden |  |  |
| Registernummer |  | amtlichen Eintrag ziehen |  |  |
| Version |  | Aenderungshistorie pruefen |  |  |
| Statistik | `statistics/registerentries` | Datenstand der Abfrage dokumentieren |  |  |

## Abfragebefehle

```bash
test -n "${LOBBYREGISTER_API_KEY:?LOBBYREGISTER_API_KEY fehlt}"

curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/registerentries?q=Suchbegriff&format=json"

curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/registerentries/R001234?format=json"

curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/registerentries/R001234/1?format=json"
```

## Cursor-Protokoll

| Lauf | Suchparameter | Eingesetzter Cursor | Antwort-Cursor | Trefferzahl | Hash der Antwort | Naechste Aktion |
|---|---|---|---|---|---|---|
| 1 |  | keiner |  |  |  |  |
| 2 |  |  |  |  |  |  |
| Abschluss |  | unveraendert | unveraendert |  |  | Akte schliessen |

## Mindestpruefung

- `sourceDate` und Abrufzeitpunkt gesichert
- `registerNumber` und `version` gesichert
- `detailsPageUrl` und `pdfUrl` gesichert
- Status aktiv/inaktiv geprueft
- letzte Aktualisierung und fehlende Updates geprueft
- `refusedAnything` und Kodexverstoesse geprueft
- Name, Rechtsform, Adresse und betraute Personen gegen interne Akte geprueft
- Regelungsvorhaben, Stellungnahmen und Auftraggeber gegen interne Akte geprueft
- Finanzaufwendungen, Zuwendungen, Schenkungen, Mitgliedsbeitraege und Berichte gegen Freigabe geprueft

## Ergebnis

- Keine Treffer:
- Ein Treffer:
- Mehrere Treffer:
- Dublette oder Zweigniederlassungsrisiko:
- Aenderungsbedarf im Portal:
- Monitoring wiederholen am:
