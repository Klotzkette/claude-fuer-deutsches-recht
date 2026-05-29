# Lobbyregister Bundestag - Leitplanken

Stand: 27.05.2026. Dieses Plugin arbeitet mit offiziellen Bundestags- und Gesetzesquellen und markiert unklare Punkte als Pruefbedarf. Es ersetzt keine rechtliche Pruefung durch verantwortliche Berufstraegerinnen oder Compliance-Verantwortliche.

## Kernlogik

1. Interessenvertretung pruefen: Kontaktaufnahme zur unmittelbaren oder mittelbaren Einflussnahme auf Willensbildung oder Entscheidung.
2. Adressat pruefen: Bundestag, Mitglieder, Organe, Fraktionen, Gruppen, Mitarbeitende oder Bundesregierung einschliesslich der im LobbyRG genannten Leitungsebenen.
3. Registrierungspflicht pruefen: Schwellen nach § 2 Abs. 1 LobbyRG und Ausnahmen nach § 2 Abs. 2 oder Abs. 3 LobbyRG.
4. Registerdaten vorbereiten: Stammdaten, Personen, Drehtuerangaben, Taetigkeit, Bereiche, Vorhaben, Auftraege, Finanzdaten und Dokumente.
5. Freigabe sichern: Richtigkeit und Vollstaendigkeit bestaetigen, bei Organisationen durch eine geeignete Leitungsperson oder vertretungsberechtigte Person.
6. Laufende Pflege: unverzuegliche Updates, Quartalsupload fuer Stellungnahmen/Gutachten, Finanzdaten nach Geschaeftsjahr und Jahresaktualisierung.
7. Open-Data-Kontrolle: nach Veroeffentlichung den oeffentlichen Registereintrag per API/API-Export gegen die interne Freigabeakte pruefen.
8. Kontaktverhalten: Offenheit, Transparenz, Ehrlichkeit, Integritaet, Identitaet, Anliegen und Auftraggeber offenlegen.

## Pflichtquellen

- [Lobbyregister FAQ fuer Interessenvertreter](https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572)
- [Lobbyregister A-Z](https://www.lobbyregister.bundestag.de/informationen-und-hilfe/lobbyregister-a-z-863568)
- [Handbuch zur Eintragung Version 2.0](https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch)
- [LobbyRG bei gesetze-im-internet](https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html)
- [Verhaltenskodex Anlage 6 BTGO](https://www.gesetze-im-internet.de/btgo2025anl_6/BJNR0FA0I0025BJNE000100000.html)
- [Sanktionen bei Verstoessen](https://www.lobbyregister.bundestag.de/informationen-und-hilfe/sanktionen-bei-verstoessen-1014438)
- [Inhalte der Interessenvertretung](https://www.lobbyregister.bundestag.de/inhalte-der-interessenvertretung?lang=de)
- [Registerfuehrende Stelle](https://www.lobbyregister.bundestag.de/informationen-und-hilfe/registerfuehrende-stelle-rfs--863578)
- [Open Data/API](https://www.lobbyregister.bundestag.de/informationen-und-hilfe/open-data-1049716)
- [API V2 YAML](https://api.lobbyregister.bundestag.de/rest/v2/R2.21-de.yaml)
- [API V2 Swagger UI](https://api.lobbyregister.bundestag.de/rest/v2/swagger-ui/)
- [JSON-Schema Registereintrag](https://www.lobbyregister.bundestag.de/json-schemas/current/Lobbyregister-Registereintrag-schema.json)

## Open Data und API

Die offizielle API V2 ermoeglicht einen umfassenden **lesenden** Zugriff auf oeffentliche Registerinhalte. Das Plugin verwendet sie fuer Suche, Registernummernabfrage, Versionsvergleich, Statistik, Dublettenmonitoring und Nachkontrolle eigener Portalangaben. Die API darf nicht als Einreichungsweg fuer Erstregistrierung, Aktualisierung, Bestaetigung oder Stellungnahmen-Upload dargestellt werden.

Arbeitsregel:

1. Vor Portalabgabe interne Daten JSON-nah auf das oeffentliche Schema mappen.
2. Nach Veroeffentlichung per API die Registernummer, Version, `sourceDate`, Detailseite und PDF sichern.
3. Jede Abweichung zwischen Freigabeakte und API/API-Export als rechtlich relevant, technisch relevant oder nur Anzeige-/Schemaeffekt klassifizieren.
4. Bei Schreibvarianten, Zweigniederlassungen, Auftraggebern und Unterauftragnehmern eine Suchabfrage mit Cursor-Protokoll dokumentieren.

Technische Details: [open-data-api-v2.md](open-data-api-v2.md).

## Qualitaetsgate

- Pflichtgrund und Ausnahme wurden getrennt geprueft.
- Jede Annahme hat Quelle, Datum oder Verantwortliche.
- Personenlisten trennen Vertretung, betraute Personen, Backoffice und nur gelegentliche Beteiligung.
- Finanzangaben lassen sich auf Geschaeftsjahr und Berechnungsmethode zurueckfuehren.
- Regelungsvorhaben sind konkret genug und mit Kontaktstart/Updatepflicht verknuepft.
- Stellungnahmen und Gutachten haben Versanddatum, Empfaengerkreis, Regelungsvorhaben und Quartalsfrist.
- Portaltexte sind nicht irrefuehrend, nicht zu knapp und nicht breiter als die belegten Tatsachen.
- Verhaltenskodex und Offenlegungssaetze sind fuer Erstkontakte vorbereitet.
- API-Diffs trennen Portalpflicht, oeffentlichen Datenstand und technische Schemaeffekte.
