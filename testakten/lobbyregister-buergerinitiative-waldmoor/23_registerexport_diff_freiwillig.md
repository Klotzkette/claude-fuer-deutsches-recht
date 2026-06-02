# Registerexport-Diff: freiwillige Registrierung Waldmoor 2030

## Abgleich

- Interne Akte: WM-2030-LR-FREIWILLIG
- Portalaktion: freiwillige Registrierung als sonstige Organisation ohne eigene Rechtspersönlichkeit
- Geplanter öffentlicher Registereintrag: R010226
- API-Nachkontrolle: 10.06.2026
- Vorherige Suche: 20.05.2026 ohne Treffer

## Erwarteter öffentlicher Datensatz

| Bereich | Interne Freigabe | Erwarteter API/API-Export | Risiko |
|---|---|---|---|
| Organisation | Bürgerinitiative Waldmoor 2030 | Name exakt, keine Vereinsrechtsform | mittel |
| Organisationstyp | Netzwerk/sonstige Organisation ohne eigene Rechtspersönlichkeit | `identity` Organisation, Rechtsformhinweis | mittel |
| Sprecherinnen | Luise Barmbek, Navid Sahin | als vertretungs-/sprechbefugte Personen | gering |
| Tätigkeit | Moratorium B 449n und Alternativenpruefung | nicht nur "Umweltschutz allgemein" | hoch |
| Petition | lokale und Petitionsphase gesondert | nicht als pauschale Lobbyregisterpflicht dargestellt | mittel |
| Bundeskommunikation | MdB, BMDV, Ausschusskontakte ab Mai | in Tätigkeit/Regelungsvorhaben sichtbar | hoch |
| Finanzierung | Spenden Privatpersonen und Vereine | Windpark-Spende nicht als angenommen | hoch |
| Gutachten | Karten- und Moorhydrologie-Gutachten | nur als Stellungnahme, wenn an Bundesadressaten versandt | mittel |
| Kodex | Ehrenamtsleitfaden akzeptiert | keine eigene Kodex-PDF erforderlich, wenn nicht vorhanden | gering |

## API-Schnipsel nach Veröffentlichung

```json
{
  "registerNumber": "R010226",
  "accountDetails": {
    "activeLobbyist": true,
    "lastUpdateDate": "2026-06-09T13:44:00.000+02:00",
    "accountHasCodexViolations": false
  },
  "registerEntryDetails": {
    "version": 1,
    "legislation": "GL2024",
    "validFromDate": "2026-06-09T13:44:00.000+02:00",
    "refusedAnything": false
  },
  "lobbyistIdentity": {
    "identity": "ORGANIZATION",
    "companyName": "Bürgerinitiative Waldmoor 2030"
  },
  "activitiesAndInterests": {
    "generalInformation": "Interessenvertretung fuer ein Moratorium der Bundesfernstrassen-Trasse B 449n und fuer eine moorschutzfachliche Alternativenpruefung."
  }
}
```

## Red-Team-Pruefung

1. Wenn die API nur "Umweltschutz" zeigt, ist der Eintrag zu allgemein.
2. Wenn die Windpark-Spende als Finanzierungsquelle erscheint, obwohl sie noch nicht angenommen wurde, muss sofort korrigiert werden.
3. Wenn das Gutachten fehlt, ist zu prüfen, ob es überhaupt an Bundesadressaten gegeben wurde. Fehlen allein ist nicht automatisch ein Verstoss.
4. Wenn die API nach Registrierung weiter keinen Treffer liefert, Portalveroeffentlichung und Registernummer prüfen.

## Ergebnislogik

Grün erst, wenn die freiwillige Registrierung nicht als Rueckwaertspflicht für die Petitionsphase missverstanden wird und die aktuelle Bundeskampagne transparent, aber nicht überdehnt beschrieben ist.
