---
name: lohn-sv-kanzlei-rechnung
description: "Lohn SV Kanzlei Rechnung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Lohn SV Kanzlei Rechnung

## Arbeitsbereich

Dieser Skill bündelt 2 sachlich verwandte Arbeitsschritte rund um **Lohn SV Kanzlei Rechnung** im Plugin Kanzlei-Allgemein. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kanzlei-allgemein-lohn-sv` | Bereitet Lohnabrechnung Sozialversicherungsmeldungen und Payroll-Übergabe für Kanzleimitarbeiter vor. Anwendungsfall monatliche Lohnabrechnung muss vorbereitet oder Daten für DATEV-Lohnsoftware oder Steuerkanzlei zusammengestellt werden. Normen SGB IV SGB V SGB VI EStG § 41b EStG Lohnsteuerbescheinigung. Prüfraster Bruttogehalt ELStAM-Steuerklasse SV-Beitraege Minijob Meldungen Bonus Gratifikation Fehlzeiten. Output Payroll-Zusammenfassung mit SV-Beitraegen Lohnsteuer Meldedaten und Übergabepaket für Fachsystem oder Steuerberater. Abgrenzung zu kanzlei-allgemein-hr-personal und kanzlei-allgemein-ustva-buchhaltung. |
| `kanzlei-allgemein-rechnung` | Bereitet Kanzleirechnungen Vorschussrechnungen RVG-Abrechnungen und Stundenhonorare vor. Anwendungsfall Mandat ist abgeschlossen oder Zeitpunkt für Zwischenrechnung ist gekommen. Normen § 10 RVG Pflichtangaben § 14 UStG Umsatzsteuerausweis GoBD Aufbewahrung § 3a RVG Honorarvereinbarung. Prüfraster Timesheet Narrative Auslagen Umsatzsteuer Zahlungsstatus Rechtsschutz GoBD-Protokoll. Output Honorarrechnung als PDF und Markdown mit Eintrag im Honorar-Tracker Übergabe an XRechnung oder ZUGFeRD möglich. Abgrenzung zu rechnungserstellung-rvg (ausführliches RVG-Abrechnungswerk) und kanzlei-allgemein-ustva-buchhaltung. |

## Arbeitsweg

Im Plugin Kanzlei-Allgemein gilt für **Lohn SV Kanzlei Rechnung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `kanzlei-allgemein-lohn-sv`

**Fokus:** Bereitet Lohnabrechnung Sozialversicherungsmeldungen und Payroll-Übergabe für Kanzleimitarbeiter vor. Anwendungsfall monatliche Lohnabrechnung muss vorbereitet oder Daten für DATEV-Lohnsoftware oder Steuerkanzlei zusammengestellt werden. Normen SGB IV SGB V SGB VI EStG § 41b EStG Lohnsteuerbescheinigung. Prüfraster Bruttogehalt ELStAM-Steuerklasse SV-Beitraege Minijob Meldungen Bonus Gratifikation Fehlzeiten. Output Payroll-Zusammenfassung mit SV-Beitraegen Lohnsteuer Meldedaten und Übergabepaket für Fachsystem oder Steuerberater. Abgrenzung zu kanzlei-allgemein-hr-personal und kanzlei-allgemein-ustva-buchhaltung.

# Lohn, Sozialversicherung und Payroll


## Triage zu Beginn
1. Welcher Monat und welche Mitarbeiter werden abgerechnet?
2. Gibt es Sonderzahlungen (Bonus, Gratifikation, Weihnachtsgeld) in diesem Monat?
3. Sind Minijobber oder Werkstudenten dabei, fuer die Sonderregeln gelten?
4. Sollen die Daten an DATEV, Lexware oder einen Steuerberater uebergeben werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 1 MiLoG — Gesetzlicher Mindestlohn (12,82 EUR pro Stunde ab 01.01.2025)
- §§ 14, 17 SGB IV — Arbeitsentgelt und Beitragsbemessungsgrundlage Sozialversicherung
- § 38 EStG — Lohnsteuerabzug: Arbeitgeberpflicht bei Entgeltauszahlung
- § 1 MiniJobG i.V.m. § 8 SGB IV — Minijob-Grenze: 556 EUR monatlich (ab 01.01.2025)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
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

## 2. `kanzlei-allgemein-rechnung`

**Fokus:** Bereitet Kanzleirechnungen Vorschussrechnungen RVG-Abrechnungen und Stundenhonorare vor. Anwendungsfall Mandat ist abgeschlossen oder Zeitpunkt für Zwischenrechnung ist gekommen. Normen § 10 RVG Pflichtangaben § 14 UStG Umsatzsteuerausweis GoBD Aufbewahrung § 3a RVG Honorarvereinbarung. Prüfraster Timesheet Narrative Auslagen Umsatzsteuer Zahlungsstatus Rechtsschutz GoBD-Protokoll. Output Honorarrechnung als PDF und Markdown mit Eintrag im Honorar-Tracker Übergabe an XRechnung oder ZUGFeRD möglich. Abgrenzung zu rechnungserstellung-rvg (ausführliches RVG-Abrechnungswerk) und kanzlei-allgemein-ustva-buchhaltung.

# Rechnungsvorbereitung und Abschluss


## Triage zu Beginn
1. Wird nach RVG (Gegenstandswert + Gebuehrentabelle) oder nach Stundenhonorarat (§ 3a RVG) abgerechnet?
2. Gibt es einen Vorschuss, der angerechnet werden muss?
3. Ist eine Rechtsschutzversicherung involviert (Direktabrechnung oder Erstattungsanspruch des Mandanten)?
4. Soll die Rechnung als E-Rechnung (XRechnung, ZUGFeRD) erstellt werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 10 RVG — Pflichtangaben auf der Honorarrechnung; Faelligkeit bei ordnungsgemaesser Berechnung
- § 3a RVG — Honorarvereinbarung: Schriftform und Mindestbetrag
- Anlage 2 RVG — Gebuehrentabelle: Grundlage der RVG-Abrechnung
- § 14b UStG — Aufbewahrungspflicht fuer Ausgangsrechnungen (10 Jahre)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill sammelt abrechnungsreife Informationen und erzeugt einen Rechnungsentwurf, Vorschussvorschlag oder eine Übergabe an den E-Rechnungs-Skill. Er ist die fachliche Rechnungsakte, nicht das Buchhaltungssystem.

## Datenquellen

- Zeit- und Narrative-Ledger.
- Mandatsvereinbarung.
- RVG-Hinweise.
- Auslagen.
- Gerichtskosten.
- Vorschüsse.
- Zahlungen.
- Rechtsschutzdeckung.
- Mandatsabschluss oder Zwischenrechnung.
- beA- und Postlauf-Journal für Versand- und Zustellaufwand.
- Fristen- und Action-Register für fristbezogene Tätigkeiten.
- Kosten- und Fremdgeldvermerke.
- Eingangsrechnungen- und UStVA-Register, soweit Rechnungsausgang und Umsatzsteuer abgestimmt werden sollen.

## Ablauf

1. Akte wählen.
2. Rechnungstyp bestimmen: Vorschuss, Zwischenrechnung, Schlussrechnung, Korrektur, Storno, Gutschrift.
3. Rechnungsempfänger und Kostenschuldner prüfen.
4. Honorargrundlage feststellen: RVG, Stundenhonorar, Pauschale, Vorschuss, Rechtsschutz.
5. Leistungszeitraum und Leistungsbeschreibung bestimmen.
6. Narrative und Zeiten aus `kanzlei-allgemein-zeitnarrative` übernehmen.
7. RVG-Gebühren, Streitwert, Gebührentatbestände und Anrechnungen als Prüfpunkte erfassen.
8. Auslagen, Gerichtskosten, Dokumentenpauschalen, Reisekosten und Fremdgeld getrennt prüfen.
9. Umsatzsteuer, Steuerbefreiung, Reverse Charge oder Kleinunternehmer nur nach konkreter Grundlage markieren.
10. Vorschüsse, Zahlungen und Rechtsschutzleistungen abziehen.
11. Summen netto, Steuer und brutto prüfen.
12. Pflichtangaben und GoBD-nahe Archivierung vorbereiten.
13. Formatbedarf klären: PDF, Papier, XRechnung, ZUGFeRD oder sonstiges.
14. Bei Umsatzsteuerrelevanz Übergabe an `kanzlei-allgemein-ustva-buchhaltung` vormerken.
15. Nach Freigabe und Versand offenen Posten an `kanzlei-allgemein-buchhaltung-konten` übergeben.
16. Rechnungsentwurf erzeugen.
17. Freigabe verlangen.

## Narrative-Übernahme

Aus dem Zeit- und Narrative-Ledger nicht blind alles abrechnen. Für jede Position prüfen:

- Akte und Mandat passen.
- Tätigkeit ist abrechenbar oder bewusst nicht abrechenbar.
- Narrative ist mandantenfähig, knapp und prüfbar.
- Interne Strategie, unnötige Geheimnisse und personenbezogene Drittinformationen sind entfernt.
- Zeit, Mindesttakt, Rundung und Bearbeiter sind nachvollziehbar.
- Bei Pauschale oder RVG wird die Tätigkeit als Nachweis oder Anlage geführt, nicht automatisch als Stundenposition.

## E-Rechnung und GoBD

Wenn der Empfänger Unternehmer oder öffentliche Stelle ist oder der Nutzer eine E-Rechnung verlangt, an `kanzlei-allgemein-erechnung` übergeben.

Immer vorbereiten:

- `assets/templates/rechnungsdatenblatt.md`.
- `assets/templates/gobd-rechnungsprotokoll.md`.

Bei E-Rechnung zusätzlich:

- `assets/templates/erechnung-datenblatt.md`.
- Formatentscheidung XRechnung oder ZUGFeRD.
- Validierungsvermerk.
- Archivierungsvermerk für strukturierte XML-Daten.

## Grenzen

Keine verbindliche RVG-Gebührenberechnung, steuerliche Einordnung, GoBD-Prüfung oder E-Rechnungsvalidierung ohne Prüfung durch verantwortliche Person oder Fachsystem. Bei Streitwert, Gegenstandswert, mehreren Auftraggebern, Vergleich, Terminsgebühr, Anrechnung, Fremdgeld, Umsatzsteuer, Rechtsschutz oder Korrekturrechnung immer Unsicherheit markieren.

## Ausgabe

- Rechnungsdatenblatt.
- Narrative-Liste.
- GoBD-Prüfprotokoll.
- E-Rechnungsdatenblatt, wenn erforderlich.
- Prüfhinweise und Validierungsstatus.
- Entwurf Rechnungstext.
- Offene Punkte.
- Offene-Posten-Übergabe nach Freigabe.
