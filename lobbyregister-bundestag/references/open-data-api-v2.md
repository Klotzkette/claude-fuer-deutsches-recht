# Lobbyregister Open Data und API V2

Stand: 27.05.2026. Diese Referenz beschreibt die technische Kontrollschicht des Plugins für oeffentliche Lobbyregisterdaten. Sie ersetzt keine bereitgestellten Lehrmaterialien und keine verifizierte Quellenarbeit.

## Offizielle Quellen

- Open Data/API: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/open-data-1049716
- API V2 Basis-URL: https://api.lobbyregister.bundestag.de/rest/v2
- API V2 YAML: https://api.lobbyregister.bundestag.de/rest/v2/R2.21-de.yaml
- API V2 Swagger UI: https://api.lobbyregister.bundestag.de/rest/v2/swagger-ui/
- JSON-Schema Registereintrag: https://www.lobbyregister.bundestag.de/json-schemas/current/Lobbyregister-Registereintrag-schema.json
- JSON-Schema Suchergebnisliste: https://www.lobbyregister.bundestag.de/json-schemas/current/Lobbyregistersuche-Registereintrag-schema.json
- JSON-Schema Suchergebnisliste mit Details: https://www.lobbyregister.bundestag.de/json-schemas/current/Lobbyregistersuche-Registereintrag-Details-schema.json

## Was die API kann

- oeffentliche Registereintraege anhand einer Registernummer abrufen
- bestimmte Versionen eines oeffentlichen Registereintrags abrufen
- Freitextsuche über oeffentliche Registereintraege ausfuehren
- Statistikdaten zum Register abrufen
- veroeffentlichte Angaben nach Portalaktion gegen interne Freigabeakten vergleichen
- Watchlists, Gegenparteienpruefungen, Dublettenchecks und Aktualisierungsmonitore speisen

## Was die API nicht leisten soll

- keine Erstregistrierung im Namen einer Interessenvertreterin absenden
- keine Änderungsmeldung, Quartalsmeldung oder Stellungnahme im Portal einreichen
- keine Bestaetigungsdokumente oder Portal-Freigaben ersetzen
- keine Aussage "XML-Einreichung möglich" treffen, solange die offizielle Dokumentation nur den lesenden Abruf oeffentlicher Inhalte belegt
- keinen API-Key fest in Akten, Skripten oder Mandatsdaten speichern

## Authentifizierung

Alle API-Abfragen benoetigen einen gueltigen API-Key. Die Bundestagsseite nennt einen aktuell gueltigen Key und verweist für dauerhafte Nutzung auf die Moeglichkeit eines individuellen Keys. Das Plugin soll Beispiele mit einer Umgebungsvariable schreiben:

```bash
test -n "${LOBBYREGISTER_API_KEY:?LOBBYREGISTER_API_KEY fehlt}"
```

Danach bevorzugt das Plugin den HTTP-Header:

```bash
curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/statistics/registerentries?format=json"
```

Der Query-Parameter `apikey` ist dokumentiert, sollte aber nur für schnelle Tests verwendet werden, weil er leichter in Logs landet.

## Endpunkte

| Zweck | Methode und Pfad | Typischer Einsatz |
|---|---|---|
| Einzelner Eintrag | `GET /registerentries/{registerNumber}?format=json` | veroeffentlichten Registereintrag nach Registernummer prüfen |
| Versionierter Eintrag | `GET /registerentries/{registerNumber}/{version}?format=json` | Änderungshistorie und Diff zwischen Versionen prüfen |
| Freitextsuche | `GET /registerentries?q={suchbegriff}&format=json` | Organisation, Branche, Vorhaben oder Gegenpartei suchen |
| Statistik | `GET /statistics/registerentries?format=json` | Datenstand, Plausibilitaet und Monitoring-Kontext dokumentieren |

Die Registernummer folgt dem Muster `R` plus sechs Ziffern, zum Beispiel `R001234`.

## Cursor-Paginierung

Bei Suchanfragen muss das Plugin die Cursor-Regel aus der YAML-Dokumentation beachten:

1. erste Anfrage mit allen Suchparametern senden
2. `cursor` der Antwort sichern
3. Folgeanfrage mit denselben Suchparametern plus `cursor` senden
4. wiederholen, bis sich der Cursor nicht mehr ändert
5. jede Antwort mit `sourceDate`, Suchbegriff, Cursor und Hash in der Akte speichern

## Beispielabfragen

```bash
# Freitextsuche
curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/registerentries?q=Energie&format=json"

# Eintrag nach Registernummer
curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/registerentries/R001234?format=json"

# Bestimmte Version
curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/registerentries/R001234/1?format=json"

# Statistik
curl -H "Authorization: ApiKey ${LOBBYREGISTER_API_KEY}" \
  "https://api.lobbyregister.bundestag.de/rest/v2/statistics/registerentries?format=json"
```

## Pflichtfelder für API-Diffs

Bei jedem Abgleich zwischen interner Registerakte und oeffentlicher API-Antwort prüft das Plugin mindestens:

- `source`, `sourceUrl`, `sourceDate`, `jsonDocumentationUrl`
- `registerNumber`
- `accountDetails.activeLobbyist`
- `accountDetails.firstPublicationDate`
- `accountDetails.lastUpdateDate`
- `accountDetails.accountHasCodexViolations`
- `registerEntryDetails.version`
- `registerEntryDetails.legislation`
- `registerEntryDetails.detailsPageUrl`
- `registerEntryDetails.pdfUrl`
- `registerEntryDetails.validFromDate`
- `registerEntryDetails.fiscalYearUpdate.updateMissing`
- `registerEntryDetails.fiscalYearUpdate.lastFiscalYearUpdate`
- `registerEntryDetails.refusedAnything`
- `lobbyistIdentity.identity`
- `lobbyistIdentity.companyName` oder Namensfelder natuerlicher Personen
- `activitiesAndInterests`
- `employeesInvolvedInLobbying`
- `financialExpenses`
- `mainFundingSources`
- `publicAllowances`
- `donators`
- `membershipFees`
- `annualReports`
- `regulatoryProjects`
- `statements`
- `contracts`
- `codeOfConduct.ownCodeOfConduct`
- `codeOfConduct.codeOfConductPdfUrl`

## Arbeitsregel für das Plugin

Bei jeder API-Nutzung muss die Ausgabe unterscheiden:

- **Portalpflicht:** Was muss im Lobbyregisterportal eingetragen, aktualisiert, bestaetigt oder hochgeladen werden?
- **API-Kontrolle:** Was kann nach Veroeffentlichung automatisiert abgefragt, verglichen und ueberwacht werden?
- **Datenmodell:** Welche internen Felder lassen sich auf das oeffentliche JSON-Schema mappen?
- **Risiko:** Welche Abweichung ist rechtlich relevant, technisch unklar oder nur ein Anzeige-/Schemaeffekt?

Die API ist damit ein Kontroll- und Monitoringinstrument. Sie ist kein Ersatz für die registerfuehrende Stelle, das Portal oder eine rechtliche Freigabe.
