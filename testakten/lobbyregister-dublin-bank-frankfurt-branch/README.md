# Testakte Lobbyregister: Emerald Liffey Bank plc / Zweigniederlassung Frankfurt

Fiktive Akte fuer das Plugin `lobbyregister-bundestag`. Sie testet die schwierige Eintragungseinheit bei einer auslaendischen Bank mit unselbststaendiger deutscher Zweigniederlassung.

## Sachverhalt

Die **Emerald Liffey Bank plc** ist eine nach irischem Recht gegruendete public limited company mit Sitz in Dublin. Sie besitzt eine Banklizenz der Central Bank of Ireland und betreibt in Deutschland eine unselbststaendige Zweigniederlassung in Frankfurt am Main. Die Zweigniederlassung ist im Handelsregister Frankfurt eingetragen, hat eigene Geschaeftsadresse, eigene Leitung fuer Deutschland und nutzt eine BaFin-notifizierte Erlaubnis im Rahmen des europaeischen Passporting. Sie ist aber keine eigene juristische Person.

Im Mai 2026 bereitet die Bank Interessenvertretung gegenueber dem Bundesministerium der Finanzen, Mitgliedern des Finanzausschusses des Deutschen Bundestages und Mitarbeitenden mehrerer Abgeordnetenbueros vor. Es geht um die nationale Umsetzung eines Digital-Euro-Begleitgesetzes, Instant-Payment-Fraud-Regeln und die Behandlung grenzueberschreitender Einlagensicherungsbeitraege. Die Public-Policy-Abteilung in Dublin steuert das Thema, aber die Frankfurter Zweigniederlassung fuehrt die meisten deutschen Termine.

Die Compliance-Abteilung schwankt zwischen zwei Wegen: Nur **Emerald Liffey Bank plc, Dublin** registrieren und Frankfurt als Zweigniederlassung, Hauptstadtkontakt, betraute Personen und Kostenstelle abbilden; oder zusaetzlich die **Emerald Liffey Bank plc Zweigniederlassung Frankfurt am Main** als eigenstaendigen Registereintrag anlegen. Beides hat Risiken: Untererfassung und Bussgeldangst einerseits, irrefuehrende Doppelregistrierung und doppelte Finanzdaten andererseits.

## Kernfrage

Muss, darf oder soll die Bank im Lobbyregister einmal oder zweimal erscheinen?

## Dateien

| Datei | Inhalt |
|---|---|
| [00_aktenuebersicht.md](00_aktenuebersicht.md) | Aktenplan, Lernziele und Arbeitsauftrag |
| [01_mandatsanfrage_email.txt](01_mandatsanfrage_email.txt) | E-Mail der Bank an die Kanzlei |
| [02_cro_registerauszug_dublin.md](02_cro_registerauszug_dublin.md) | Fiktiver irischer Registerauszug |
| [03_handelsregister_frankfurt_zweigniederlassung.md](03_handelsregister_frankfurt_zweigniederlassung.md) | Fiktiver Handelsregisterauszug der Zweigniederlassung |
| [04_bafin_passporting_notiz.md](04_bafin_passporting_notiz.md) | Notiz zu BaFin/Passporting und Erlaubnislage |
| [05_organigramm_legal_entity.md](05_organigramm_legal_entity.md) | Rechtstraeger- und Niederlassungsstruktur |
| [06_kontaktlog_bundestag_bmf.csv](06_kontaktlog_bundestag_bmf.csv) | Kontaktlog mit Bundestag/BMF-Kontakten |
| [07_regelungsvorhaben_digital_euro.md](07_regelungsvorhaben_digital_euro.md) | Regelungsvorhaben und Interessenbeschreibung |
| [08_lobbyregister_entwurf_dublin.json](08_lobbyregister_entwurf_dublin.json) | Primaerentwurf Registereintrag Dublin |
| [09_lobbyregister_entwurf_frankfurt_zweigniederlassung.json](09_lobbyregister_entwurf_frankfurt_zweigniederlassung.json) | Streitiger Zweitentwurf Frankfurt |
| [10_streitvermerk_doppelregistrierung.md](10_streitvermerk_doppelregistrierung.md) | Variantenvermerk mit Risiken |
| [11_rfs_anfrage_entwurf.md](11_rfs_anfrage_entwurf.md) | Anfrage an die registerfuehrende Stelle |
| [12_finanzaufwendungen_deutschland.csv](12_finanzaufwendungen_deutschland.csv) | Kostenaufteilung Dublin/Frankfurt/Berlin |
| [13_vorstandsbeschluss_public_policy.md](13_vorstandsbeschluss_public_policy.md) | Board-Minutes und Freigabeproblem |
| [14_finalcheck_arbeitsblatt.md](14_finalcheck_arbeitsblatt.md) | Qualitaetsgate fuer den Wizard |
| [15_emailthread_dublin_frankfurt_chaos.eml](15_emailthread_dublin_frankfurt_chaos.eml) | E-Mail-Thread Dublin/Frankfurt mit widerspruechlicher interner Haltung |
| [16_portal_screenshot_abschrift_dublin.md](16_portal_screenshot_abschrift_dublin.md) | Abschrift des Dublin-Portalentwurfs |
| [17_portal_screenshot_abschrift_frankfurt_abgebrochen.md](17_portal_screenshot_abschrift_frankfurt_abgebrochen.md) | Abgebrochener Zweitentwurf fuer Frankfurt |
| [18_telefonnotiz_rfs_vorfrage.md](18_telefonnotiz_rfs_vorfrage.md) | Telefonnotiz zur unverbindlichen RfS-Vorfrage |
| [19_meeting_notes_bmf_terminvorbereitung.md](19_meeting_notes_bmf_terminvorbereitung.md) | BMF-Terminvorbereitung mit Offenlegungsproblem |
| [20_offenlegungssaetze_varianten.md](20_offenlegungssaetze_varianten.md) | Gute und schlechte Offenlegungssaetze |
| [21_interne_risikoampel.xlsx.md](21_interne_risikoampel.xlsx.md) | MD-Vorschau einer Risikoampel |
| [21_interne_risikoampel.csv](21_interne_risikoampel.csv) | Rohdaten Risikoampel als CSV |
| [22_kalendereinladung_bundestag.ics](22_kalendereinladung_bundestag.ics) | Kalendereinladung fuer Bundestagstermin |
| [23_datenschutz_personenfreigabe.md](23_datenschutz_personenfreigabe.md) | Freigaben betrauter Personen fuer Registerdaten |
| [24_kostenstellen_mapping_dublin_frankfurt.md](24_kostenstellen_mapping_dublin_frankfurt.md) | Kostenstellenmapping Dublin/Frankfurt/Berlin |
| [25_api_abfrageplan_open_data.md](25_api_abfrageplan_open_data.md) | API-Abfrageplan fuer Dublin/Frankfurt-Dublettencheck |
| [26_api_mock_response_dublin.json](26_api_mock_response_dublin.json) | Fiktive API-Antwort fuer den veroeffentlichten Dublin-Eintrag |
| [27_registerexport_diff_dublin.md](27_registerexport_diff_dublin.md) | Diff zwischen Freigabeakte und oeffentlichem API/API-Export |

## Lernziel

Die Akte zwingt das Plugin, `personen-organisationstyp`, `konzern-netzwerk-plattform`, `erstregistrierung-ausfuellen`, `registereintrag-finalcheck`, `registerfuehrende-stelle-kontakt`, `suche-open-data-monitor` und `fristen-und-quartalsmonitor` zusammenzuspielen. Entscheidend ist nicht eine voreilige Antwort, sondern eine saubere Registerpraxis: Primaerentwurf, Streitvermerk, RfS-Anfrage, API-Dublettencheck und keine Doppelung ohne Klaerung.

## Disclaimer

Alle Angaben sind frei erfunden. Die Akte ist eine Schulungsakte und keine Aussage zur echten Registerpraxis.
