# Registerexport-Diff: R009814 Emerald Liffey Bank plc

## Abgleich

- Interne Freigabeakte: ELB-LR-2026-05
- Portalaktion: Erstregistrierung Dublin-plc, Frankfurt nur als unselbstständige Zweigniederlassung
- Veröffentlichter Registereintrag: R009814
- API-Abruf: 02.06.2026, 09:17 Uhr
- `sourceDate`: 2026-06-02T09:17:22.184+02:00
- Version: 1
- Bearbeitung: RAin Dr. Mareike Tamm und Orlaine Keating

## Kurzbefund

Der öffentliche Eintrag bildet die Dublin-plc als einheitliche Organisation ab. Die Frankfurter Zweigniederlassung erscheint als weitere Adresse und in der Tätigkeitsbeschreibung, nicht als zweiter Rechtsträger. Das ist konsistent mit dem Primaerentwurf und verhindert eine irreführende Doppelzählung der Finanzaufwendungen.

Die Abfrage `Emerald Liffey Frankfurt` liefert denselben Eintrag R009814. Die Abfrage `Emerald Liffey Bank Zweigniederlassung` liefert keinen eigenen zweiten Eintrag.

## Feldvergleich

| Bereich | Interne Freigabe | API/API-Export | Bewertung | Aktion |
|---|---|---|---|---|
| Rechtsträger | Emerald Liffey Bank plc, Dublin | `companyName` Emerald Liffey Bank plc | Grün | keine |
| Zweigniederlassung | Frankfurt sichtbar, nicht eigener Rechtsträger | weitere Adresse und Tätigkeitsbeschreibung | Grün | Screenshot Detailseite sichern |
| Aktivstatus | aktiv ab Erstveröffentlichung | `activeLobbyist` true | Grün | keine |
| Version | Erstversion | Version 1 | Grün | Version in Fristenbuch eintragen |
| Tätigkeit | Digital Euro, Instant Payments, Einlagensicherung | alle drei Themen sachlich erfasst | Grün | keine |
| Betraute Personen | Byrne, Heidenreich, Krüger, Marin | vier Personen, 2.30 VZAE | Grün | HR-Freigaben ablegen |
| Finanzaufwendungen | 180000 bis 190000 EUR nach Bereinigung | Range 180000 bis 190000 | Grün | Kostenstellenmapping anhängen |
| Auftraggeber | keine Fremdvertretung | `contractsPresent` false | Grün | keine |
| Stellungnahmen | noch keine grundlegende Stellungnahme versandt | `statementsPresent` false | Grün | Quartalsmonitor bleibt offen |
| Verhaltenskodex | eigener Kodex vorhanden | `ownCodeOfConduct` true | Grün | Link intern prüfen |
| verweigerte Angaben | keine | `refusedAnything` false | Grün | keine |
| Kodexverstoesse | keine | `accountHasCodexViolations` false | Grün | keine |

## Dubletten- und Zweigniederlassungscheck

| Suche | Ergebnis | Risiko | Entscheidung |
|---|---|---|---|
| Emerald Liffey Bank | ein Treffer R009814 | gering | Primaerentwurf bestätigt |
| Emerald Liffey Frankfurt | ein Treffer R009814 | gering | Frankfurt wird nur im Dublin-Eintrag sichtbar |
| Emerald Liffey Bank Zweigniederlassung | kein Treffer | gering | kein Zweitentwurf veröffentlicht |
| ELB Digital Euro | kein separater Treffer | gering | Projektkürzel nicht als eigener Name genutzt |
| Taunusanlage 12 | kein separater Treffer | mittel | Adresse auf Detailseite optisch prüfen |

## Offene Punkte

1. Die API-Antwort zeigt eine `example.invalid`-URL aus dem Exportbeispiel. In einer echten Akte müsste die PDF-/Kodex-URL aus dem Register oder der Unternehmensseite geprüft werden.
2. Die RfS-Anfrage bleibt in der Akte, obwohl keine zweite Registrierung vorgenommen wurde. Sie dokumentiert die vorherige Unsicherheit.
3. Bei erster grundlegender Stellungnahme zum Digital-Euro-Begleitgesetz muss der Quartalsupload neu geprüft werden.

## Abschlussentscheidung

Status Grün mit Wiedervorlage am 01.07.2026. Keine zweite Registrierung für Frankfurt vorbereiten. Falls das Portal später einen zweiten Frankfurt-Eintrag anzeigt oder ein RfS-Hinweis eingeht, Streitvermerk neu öffnen.
