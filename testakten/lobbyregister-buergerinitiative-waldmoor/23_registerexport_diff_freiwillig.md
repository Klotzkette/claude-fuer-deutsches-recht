# Registerexport-Diff: freiwillige Registrierung Waldmoor 2030

## Abgleich

- Interne Akte: WM-2030-LR-FREIWILLIG
- Portalaktion: freiwillige Registrierung als sonstige Organisation ohne eigene Rechtspersoenlichkeit
- Geplanter oeffentlicher Registereintrag: R010226
- API-Nachkontrolle: 10.06.2026
- Vorherige Suche: 20.05.2026 ohne Treffer

## Erwarteter oeffentlicher Datensatz

| Bereich | Interne Freigabe | Erwarteter API/API-Export | Risiko |
|---|---|---|---|
| Organisation | Buergerinitiative Waldmoor 2030 | Name exakt, keine Vereinsrechtsform | mittel |
| Organisationstyp | Netzwerk/sonstige Organisation ohne eigene Rechtspersoenlichkeit | `identity` Organisation, Rechtsformhinweis | mittel |
| Sprecherinnen | Luise Barmbek, Navid Sahin | als vertretungs-/sprechbefugte Personen | gering |
| Taetigkeit | Moratorium B 449n und Alternativenpruefung | nicht nur "Umweltschutz allgemein" | hoch |
| Petition | lokale und Petitionsphase gesondert | nicht als pauschale Lobbyregisterpflicht dargestellt | mittel |
| Bundeskommunikation | MdB, BMDV, Ausschusskontakte ab Mai | in Taetigkeit/Regelungsvorhaben sichtbar | hoch |
| Finanzierung | Spenden Privatpersonen und Vereine | Windpark-Spende nicht als angenommen | hoch |
| Gutachten | Karten- und Moorhydrologie-Gutachten | nur als Stellungnahme, wenn an Bundesadressaten versandt | mittel |
| Kodex | Ehrenamtsleitfaden akzeptiert | keine eigene Kodex-PDF erforderlich, wenn nicht vorhanden | gering |

## Fiktiver API-Schnipsel nach Veroeffentlichung

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
    "companyName": "Buergerinitiative Waldmoor 2030"
  },
  "activitiesAndInterests": {
    "generalInformation": "Interessenvertretung fuer ein Moratorium der Bundesfernstrassen-Trasse B 449n und fuer eine moorschutzfachliche Alternativenpruefung."
  }
}
```

## Red-Team-Pruefung

1. Wenn die API nur "Umweltschutz" zeigt, ist der Eintrag zu allgemein.
2. Wenn die Windpark-Spende als Finanzierungsquelle erscheint, obwohl sie noch nicht angenommen wurde, muss sofort korrigiert werden.
3. Wenn das Gutachten fehlt, ist zu pruefen, ob es ueberhaupt an Bundesadressaten gegeben wurde. Fehlen allein ist nicht automatisch ein Verstoss.
4. Wenn die API nach Registrierung weiter keinen Treffer liefert, Portalveroeffentlichung und Registernummer pruefen.

## Ergebnislogik

Gruen erst, wenn die freiwillige Registrierung nicht als Rueckwaertspflicht fuer die Petitionsphase missverstanden wird und die aktuelle Bundeskampagne transparent, aber nicht ueberdehnt beschrieben ist.
