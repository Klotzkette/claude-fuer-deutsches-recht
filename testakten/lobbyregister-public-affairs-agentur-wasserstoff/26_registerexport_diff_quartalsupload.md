# Registerexport-Diff: Quartalsupload Q2/2026

## Abgleich

- Registereintrag: Spreebogen Regulatory GmbH, R008442
- Portalaktion: Korrektur Auftraggebertext und Upload zweier grundlegender Dokumente für Q2/2026
- API-Abruf: 05.07.2026, 10:34 Uhr
- `sourceDate`: 2026-07-05T10:34:48.553+02:00
- Version: 4
- Interne Tickets: SPR-H2-2026-Q2-UPL, SPR-H2-2026-AGT-KORR

## Kurzbefund

Die API-Antwort zeigt die neue, engere Tätigkeitsbeschreibung. HansaH2 Storage AG und Nordsee Elektrolyse Konsortium GbR sind getrennt abgebildet. Die beiden grundlegenden Dokumente erscheinen als `statements`. Der frühere Fehler "deutsche Wasserstoffwirtschaft" ist im öffentlichen Datensatz nicht mehr sichtbar.

Rot bleibt die Dokumentationsfrage OpenGrid Events UG: Die API-Antwort nennt OpenGrid als Unterauftragnehmer mit Stakeholder-Mapping. Das ist inhaltlich richtig, muss aber mit Rechnung, Vertrag und interner Freigabe zusammenpassen.

## Feldvergleich

| Bereich | Interne Freigabe | API/API-Export | Bewertung | Aktion |
|---|---|---|---|---|
| Tätigkeitsbeschreibung | einzelne Unternehmen und Konsortien | gleichlautend | Grün | keine |
| Auftraggeber HansaH2 | Speicher- und Kavernenfragen | eigener Client | Grün | Vertrag beilegen |
| Auftraggeber Konsortium | Elektrolyse und Netzanbindung | eigener Client | Grün | GbR-Freigabe nachheften |
| Unterauftrag OpenGrid | Stakeholder-Mapping und Eventvorbereitung | als Contractor genannt | Orange | Unterauftragnehmer-Check neu freigeben |
| Stellungnahme HansaH2 | versandt 28.05.2026 | veröffentlicht 03.07.2026 | Grün | PDF sichern |
| Kurzgutachten Konsortium | versandt 03.06.2026 | veröffentlicht 03.07.2026 | Grün | PDF sichern |
| Version | erwartete Version 4 | Version 4 | Grün | Fristenbuch aktualisieren |
| verweigerte Angaben | keine | `refusedAnything` false | Grün | keine |
| Kodexverstoesse | keine | `accountHasCodexViolations` false | Grün | keine |

## Schlechte Arbeitsnotiz aus dem Datenraum

Malte hatte am 04.07.2026 in Slack geschrieben: "Passt doch, API findet HansaH2, wir müssen OpenGrid nicht extra anfassen." Das ist zu knapp. Gerade weil OpenGrid im API-Datensatz auftaucht, muss die Abgrenzung zwischen Logistik, Stakeholder-Mapping und inhaltlicher Interessenvertretung aktenfest sein.

## Nächste Schritte

1. Datei `17_invoice_opengrid.csv` gegen `18_stakeholder_mapping_opengrid.csv` prüfen.
2. Mandantenfreigabe HansaH2 und Konsortium für die OpenGrid-Darstellung einholen.
3. Quartalskalender um Nachcheck 05.10.2026 ergänzen.
4. API-Rohantwort und PDF-Version in der Revisionsspur ablegen.
