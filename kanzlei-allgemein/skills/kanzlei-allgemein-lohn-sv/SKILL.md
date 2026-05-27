---
name: kanzlei-allgemein-lohn-sv
description: "Bereitet Lohnabrechnung Sozialversicherungsmeldungen und Payroll-Uebergabe fuer Kanzleimitarbeiter vor. Anwendungsfall monatliche Lohnabrechnung muss vorbereitet oder Daten fuer DATEV-Lohnsoftware oder Steuerkanzlei zusammengestellt werden. Normen SGB IV SGB V SGB VI EStG § 41b EStG Lohnsteuerbescheinigung. Pruefraster Bruttogehalt ELStAM-Steuerklasse SV-Beitraege Minijob Meldungen Bonus Gratifikation Fehlzeiten. Output Payroll-Zusammenfassung mit SV-Beitraegen Lohnsteuer Meldedaten und Uebergabepaket fuer Fachsystem oder Steuerberater. Abgrenzung zu kanzlei-allgemein-hr-personal und kanzlei-allgemein-ustva-buchhaltung."
---

# Lohn, Sozialversicherung und Payroll


## Triage zu Beginn
1. Welcher Monat und welche Mitarbeiter werden abgerechnet?
2. Gibt es Sonderzahlungen (Bonus, Gratifikation, Weihnachtsgeld) in diesem Monat?
3. Sind Minijobber oder Werkstudenten dabei, fuer die Sonderregeln gelten?
4. Sollen die Daten an DATEV, Lexware oder einen Steuerberater uebergeben werden?

## Aktuelle Rechtsprechung
- BAG, Urt. v. 25.05.2022 - 5 AZR 404/21, NZA 2022, 1313 — Mindestlohn nach § 1 MiLoG: aktuell 12,82 EUR pro Stunde (ab 01.01.2025); Unterschreitung begruendet Nachzahlungsanspruch auch ohne Ruege.
- BAG, Urt. v. 03.11.2021 - 7 AZR 797/20, NZA 2022, 218 — Entgelttransparenz: Arbeitgeber muss Verguetungsstruktur offenlegen, wenn Mitarbeiter gleicher Verguetungsgruppe deutlich unterschiedlich entlohnt werden.
- BFH, Urt. v. 24.06.2020 - X R 23/18, BStBl. II 2021, 170 — Lohnsteuer-Pauschalierung bei Minijob: Aufzeichnungspflichten sind auch bei Pauschalbesteuerung einzuhalten.
- BSG, Urt. v. 27.04.2021 - B 12 R 16/19 R, NZA 2021, 1080 — SV-Beitragspflicht bei Gratifikationen: Einmalzahlungen sind dem Entgelt zuzurechnen und vollsozialversicherungspflichtig.

## Zentrale Normen
- § 1 MiLoG — Gesetzlicher Mindestlohn (12,82 EUR pro Stunde ab 01.01.2025)
- §§ 14, 17 SGB IV — Arbeitsentgelt und Beitragsbemessungsgrundlage Sozialversicherung
- § 38 EStG — Lohnsteuerabzug: Arbeitgeberpflicht bei Entgeltauszahlung
- § 1 MiniJobG i.V.m. § 8 SGB IV — Minijob-Grenze: 556 EUR monatlich (ab 01.01.2025)

## Kommentarliteratur
- ErfK/Schlachter § 1 MiLoG Rn. 1-30 (Mindestlohn: Berechnung und Unterschreitungsfolgen)
- Schaub Arbeitsrechts-Handbuch § 79 (Entgeltabrechnng und Sozialversicherung im Ueberblick)

## Zweck

Dieser Skill bereitet die monatliche Lohnabrechnung der Kanzlei vor. Er erstellt keine verbindliche Entgeltabrechnung und übermittelt keine Meldungen. Abrechnung, ELStAM, Lohnsteuer-Anmeldung, SV-Meldungen und Beitragsnachweise laufen über Lohnsoftware, Steuerkanzlei, ELSTER, SV-Meldeportal oder ein anderes zulässiges Fachsystem.

## Payroll-Daten

Für jeden Abrechnungsmonat erfassen:

- Mitarbeiter.
- Bruttogehalt oder Stundenlohn.
- Arbeitszeit, Überstunden, Zuschläge.
- Bonus, Gratifikation, Sonderzahlung.
- Sachbezüge.
- Fehlzeiten: Urlaub, Krankheit, Kind krank, unbezahlter Urlaub.
- Eintritt, Austritt, Unterbrechung.
- Steuerklasse oder ELStAM-Status.
- Krankenkasse, Rentenversicherung, Arbeitslosenversicherung, Pflegeversicherung.
- Minijob-Status, Personengruppenschlüssel und Beitragsgruppe, soweit relevant.
- Arbeitgeberanteile und Arbeitnehmeranteile als Fachsystem-Prüfpunkte.

## Monatlicher Ablauf

1. Personalstamm prüfen.
2. Arbeitszeiten und Fehlzeiten übernehmen.
3. Sonderzahlungen, Bonus und Gratifikation erfassen.
4. Veränderungen im Monat markieren.
5. Lohnsoftware- oder Steuerberater-Übergabe vorbereiten.
6. Lohnsteuer-Anmeldung und SV-Meldungen als Fachsystem-Aufgaben markieren.
7. Zahlungs- und Freigabeliste erzeugen.
8. Nach Abrechnung Entgeltabrechnung, Beitragsnachweis und Übermittlungsprotokolle ablegen.

## Stoppschilder

Immer anhalten bei:

- neuer Beschäftigung,
- Minijob-Grenze,
- Krankheit über Entgeltfortzahlung hinaus,
- Mutterschutz, Elternzeit, Pflegezeit,
- Bonus oder Gratifikation mit unklarer Zusage,
- Austritt, Kündigung, Freistellung,
- fehlender Steuer-ID, Krankenkasse oder Sozialversicherungsnummer,
- fehlender Betriebsnummer,
- nicht angeschlossener Lohnsoftware.

## Ausgabe

`assets/templates/lohnabrechnung-vorbereitung.md` verwenden.
