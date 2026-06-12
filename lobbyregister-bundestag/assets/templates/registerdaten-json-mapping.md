# Registerdaten JSON-Mapping

## Zweck

Diese Vorlage übersetzt interne Registerdaten in eine JSON-nahe Arbeitsstruktur. Sie dient der Qualitaetssicherung und dem spaeteren Abgleich mit der oeffentlichen API-Antwort. Sie ist keine technische Einreichung an das Lobbyregister.

## Quellen

- JSON-Schema Registereintrag: https://www.lobbyregister.bundestag.de/json-schemas/current/Lobbyregister-Registereintrag-schema.json
- API/Open-Data-Referenz: ../../references/open-data-api-v2.md

## Mapping-Tabelle

| Oeffentliches JSON-Feld | Interne Quelle | Portalabschnitt | Freigabestatus | Abgleich nach Veroeffentlichung |
|---|---|---|---|---|
| `registerNumber` |  | automatisch nach Veroeffentlichung |  |  |
| `accountDetails.activeLobbyist` | Compliance-Entscheidung | Kontostatus |  |  |
| `accountDetails.firstPublicationDate` | API/API-Export | Veroeffentlichung |  |  |
| `accountDetails.lastUpdateDate` | Portalhistorie | Änderungen |  |  |
| `registerEntryDetails.version` | API/API-Export | Version |  |  |
| `registerEntryDetails.legislation` | API/API-Export | Gesetzeslage |  |  |
| `registerEntryDetails.detailsPageUrl` | API/API-Export | Oeffentliche Seite |  |  |
| `registerEntryDetails.pdfUrl` | API/API-Export | PDF |  |  |
| `lobbyistIdentity.identity` | Rechtstraegerpruefung | Person/Organisation |  |  |
| `lobbyistIdentity.companyName` | Registerauszug/Satzung | Name |  |  |
| `activitiesAndInterests` | Taetigkeitsbeschreibung | Interessen und Taetigkeit |  |  |
| `employeesInvolvedInLobbying` | HR/Projektliste | Betraute Personen |  |  |
| `financialExpenses` | Finance/Controlling | Finanzaufwendungen |  |  |
| `mainFundingSources` | Finance | Hauptfinanzierung |  |  |
| `publicAllowances` | Zuwendungsbuchhaltung | Oeffentliche Zuwendungen |  |  |
| `donators` | Spenden-/Schenkungsregister | Schenkungen |  |  |
| `membershipFees` | Mitgliederverwaltung | Mitgliedsbeitraege |  |  |
| `annualReports` | Jahresabschluss | Berichte |  |  |
| `regulatoryProjects` | Public-Affairs-Log | Regelungsvorhaben |  |  |
| `statements` | Dokumentenmanagement | Stellungnahmen/Gutachten |  |  |
| `contracts` | Vertragsregister | Auftrag/Auftraggeber |  |  |
| `codeOfConduct.ownCodeOfConduct` | Compliance | Verhaltenskodex |  |  |

## Stop-Punkte

- Ein internes Feld hat keine belastbare Quelle.
- Portaltext und JSON-nahe Arbeitsstruktur weichen inhaltlich voneinander ab.
- Ein Zweigentwurf bildet dieselbe juristische Person ein zweites Mal ab.
- Finanzdaten werden doppelt gezaehlt oder auf nicht vergleichbare Geschäftsjahre verteilt.
- Das Plugin soll eine technische Einreichung behaupten, obwohl nur ein lesender API-Abruf belegt ist.

## Ergebnis

- Freigabefaehiges Portal-Mapping:
- Noch offene Felder:
- Nach Veroeffentlichung per API zu prüfen:
- Naechste Portalaktion:
