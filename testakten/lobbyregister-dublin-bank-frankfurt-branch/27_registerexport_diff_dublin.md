# Registerexport-Diff: R009814 Emerald Liffey Bank plc

## Abgleich

- Interne Freigabeakte: ELB-LR-2026-05
- Portalaktion: Erstregistrierung Dublin-plc, Frankfurt nur als unselbststaendige Zweigniederlassung
- Veroeffentlichter Registereintrag: R009814
- API-Abruf: 02.06.2026, 09:17 Uhr
- `sourceDate`: 2026-06-02T09:17:22.184+02:00
- Version: 1
- Bearbeitung: RAin Dr. Mareike Tamm und Orlaine Keating

## Kurzbefund

Der oeffentliche Eintrag bildet die Dublin-plc als einheitliche Organisation ab. Die Frankfurter Zweigniederlassung erscheint als weitere Adresse und in der Taetigkeitsbeschreibung, nicht als zweiter Rechtstraeger. Das ist konsistent mit dem Primaerentwurf und verhindert eine irrefuehrende Doppelzaehlung der Finanzaufwendungen.

Die Abfrage `Emerald Liffey Frankfurt` liefert denselben Eintrag R009814. Die Abfrage `Emerald Liffey Bank Zweigniederlassung` liefert keinen eigenen zweiten Eintrag.

## Feldvergleich

| Bereich | Interne Freigabe | API/API-Export | Bewertung | Aktion |
|---|---|---|---|---|
| Rechtstraeger | Emerald Liffey Bank plc, Dublin | `companyName` Emerald Liffey Bank plc | Gruen | keine |
| Zweigniederlassung | Frankfurt sichtbar, nicht eigener Rechtstraeger | weitere Adresse und Taetigkeitsbeschreibung | Gruen | Screenshot Detailseite sichern |
| Aktivstatus | aktiv ab Erstveroeffentlichung | `activeLobbyist` true | Gruen | keine |
| Version | Erstversion | Version 1 | Gruen | Version in Fristenbuch eintragen |
| Taetigkeit | Digital Euro, Instant Payments, Einlagensicherung | alle drei Themen sachlich erfasst | Gruen | keine |
| Betraute Personen | Byrne, Heidenreich, Krueger, Marin | vier Personen, 2.30 VZAE | Gruen | HR-Freigaben ablegen |
| Finanzaufwendungen | 180000 bis 190000 EUR nach Bereinigung | Range 180000 bis 190000 | Gruen | Kostenstellenmapping anhängen |
| Auftraggeber | keine Fremdvertretung | `contractsPresent` false | Gruen | keine |
| Stellungnahmen | noch keine grundlegende Stellungnahme versandt | `statementsPresent` false | Gruen | Quartalsmonitor bleibt offen |
| Verhaltenskodex | eigener Kodex vorhanden | `ownCodeOfConduct` true | Gruen | Link intern pruefen |
| verweigerte Angaben | keine | `refusedAnything` false | Gruen | keine |
| Kodexverstoesse | keine | `accountHasCodexViolations` false | Gruen | keine |

## Dubletten- und Zweigniederlassungscheck

| Suche | Ergebnis | Risiko | Entscheidung |
|---|---|---|---|
| Emerald Liffey Bank | ein Treffer R009814 | gering | Primaerentwurf bestaetigt |
| Emerald Liffey Frankfurt | ein Treffer R009814 | gering | Frankfurt wird nur im Dublin-Eintrag sichtbar |
| Emerald Liffey Bank Zweigniederlassung | kein Treffer | gering | kein Zweitentwurf veroeffentlicht |
| ELB Digital Euro | kein separater Treffer | gering | Projektkuerzel nicht als eigener Name genutzt |
| Taunusanlage 12 | kein separater Treffer | mittel | Adresse auf Detailseite optisch pruefen |

## Offene Punkte

1. Die API-Antwort zeigt eine `example.invalid`-URL im fiktiven Testfall. In einer echten Akte muesste die PDF-/Kodex-URL aus dem Register oder der Unternehmensseite geprueft werden.
2. Die RfS-Anfrage bleibt in der Akte, obwohl keine zweite Registrierung vorgenommen wurde. Sie dokumentiert die vorherige Unsicherheit.
3. Bei erster grundlegender Stellungnahme zum Digital-Euro-Begleitgesetz muss der Quartalsupload neu geprueft werden.

## Abschlussentscheidung

Status Gruen mit Wiedervorlage am 01.07.2026. Keine zweite Registrierung fuer Frankfurt vorbereiten. Falls das Portal spaeter einen zweiten Frankfurt-Eintrag anzeigt oder ein RfS-Hinweis eingeht, Streitvermerk neu oeffnen.
