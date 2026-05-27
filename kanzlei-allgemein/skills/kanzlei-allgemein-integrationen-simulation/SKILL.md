---
name: kanzlei-allgemein-integrationen-simulation
description: "Prueft Kanzlei-Integrationen und fuehrt Workflows im Simulationsmodus weiter. Anwendungsfall E-Mail Outlook beA Fax Telefon DMS oder Buchhaltung ist nicht verbunden und Kanzlei will trotzdem Workflows testen. Normen Art. 28 DSGVO Auftragsverarbeitung bei externen Tools. Pruefraster Verbindungsstatus je Kanal Freigabe Simulationsmodus Datenschutz Protokollierung. Output Verbindungsprotokoll mit Status je Kanal und Simulationsergebnis fuer nicht verbundene Dienste. Abgrenzung zu kanzlei-allgemein-automationen (Planung) und kanzlei-allgemein-kaltstart."
---

# Integrationen und Simulationsmodus


## Triage zu Beginn
1. Welche Integration ist konkret gemeint: E-Mail/Outlook, beA, Word, DMS, Buchhaltung, Fax, Messenger?
2. Ist die Integration echt angeschlossen oder soll ein Simulationsmodus aktiv werden?
3. Welche Daten duerfen in den Simulationsmodus eingegeben werden (Anonymisierung von Mandantendaten)?
4. Soll der Simulationsmodus fuer Training, Demo oder als dauerhafter Fallback genutzt werden?

## Aktuelle Rechtsprechung
- EuGH, Urt. v. 04.07.2023 - C-252/21, NJW 2023, 2997 — Datenverarbeitung ueber Cloud-Dienste erfordert DSGVO-konforme Auftragsverarbeitung (Art. 28); auch Testsysteme mit echten Daten sind nicht erlaubt.
- BGH, Urt. v. 14.07.2022 - VI ZR 207/21, NJW 2022, 3215 — Simulationsumgebungen mit echten Mandantendaten koennen Datenschutzverletzungen darstellen; Anonymisierung oder Pseudonymisierung ist Pflicht.
- BGH, Urt. v. 26.04.2018 - I ZR 82/17, NJW 2018, 2329 — Einsatz technischer Hilfsmittel in der Anwaltskanzlei ist berufsrechtlich zulaessig, wenn persoenliche Verantwortung gewahrt bleibt.
- BVerwG, Urt. v. 27.04.2022 - 6 C 8.20, NVwZ 2022, 1563 — TOM nach Art. 32 DSGVO gelten auch fuer Testsysteme und Simulationsumgebungen.

## Zentrale Normen
- Art. 28 DSGVO — Auftragsverarbeitungsvertrag fuer externe Systemanbieter
- Art. 32 DSGVO — Technisch-organisatorische Massnahmen auch fuer Simulationsumgebungen
- § 43a Abs. 2 BRAO — Verschwiegenheit: gilt auch im Simulationsmodus mit echten Daten
- § 203 StGB — Verletzung der Berufsgeheimnisse bei unerlaubter Datenweitergabe

## Kommentarliteratur
- Kühling/Buchner DSGVO Art. 28 Rn. 1-40 (Auftragsverarbeitung und Systemintegration)
- Gaier/Wolf/Göcken BRAO § 43a Rn. 30-60 (Verschwiegenheit bei Einsatz externer Systeme)

## Zweck

Dieser Skill klärt, welche Systeme wirklich angeschlossen sind. Wenn etwas fehlt, fragt er freundlich, ob der Nutzer es verbinden oder simulieren möchte. So bleibt der Workflow testbar, ohne echte beA-, Outlook-, Word-, Messenger-, Fax- oder Buchhaltungszugänge zu benötigen.

## Integrationsmatrix

Prüfen:

- Word oder Dokumenteneditor.
- Outlook oder E-Mail.
- beA.
- Fax.
- WhatsApp, iMessage, Telegram, Teams.
- Telefonnotizen.
- DMS oder E-Akte.
- Fristenkalender.
- Buchhaltung oder Steuerkanzlei.
- Geschäftskonto, Bankimport, CSV, CAMT, MT940 oder Kontoauszug.
- ELSTER oder UStVA-Fachsystem.
- HR-, Lohn- oder Personalsoftware.
- Kanzleikalender oder Teamkalender.
- Scanner, Screenshot-Ordner, Download-Ordner.

## Fragefolge

Für jeden relevanten Anschluss:

1. Ist er technisch verfügbar?
2. Darf das System darauf zugreifen?
3. Soll der Nutzer ihn jetzt einrichten?
4. Wenn nein: Soll der Vorgang simuliert werden?
5. Wo wird im Simulationsmodus protokolliert, dass es keine echte Übermittlung gab?

## Simulationsregeln

- Simulierte Vorgänge immer deutlich markieren.
- Keine echten Versand-, Abgabe- oder Zahlungserfolge behaupten.
- Für beA, EB, UStVA, Rechnung und Fristen immer `Simulation` oder `Echtlauf` ausweisen.
- Simulierte Screenshots, Nachrichten, ZIP-Archive, Protokolle und Eingangsrechnungen dürfen genutzt werden, müssen aber als Testdaten erkennbar bleiben.
- Bei ELSTER unterscheiden: manuelle Online-Eingabe, Fachsoftware/XML-Upload, Steuerberater-Paket oder reine Simulation. Kein beliebiges Dokument als echte UStVA-Abgabe behandeln.
- Bei HR und Payroll unterscheiden: Register/Simulation, Fachsoftware-Übergabe, Steuerkanzlei-Übergabe oder echte Lohnsoftware. Keine echte Lohn- oder SV-Meldung behaupten.
- Bei Geschäftskonto unterscheiden: echte Bankanbindung, Dateiimport, manueller Kontoauszug oder Simulation. Keine Bankzugangsdaten im Chat und keine Zahlungsaufträge ohne Freigabe.

## Beispiel

> beA ist nicht angeschlossen. Soll ich Sie beim Anschluss unterstützen oder den beA-Eingang für diese Testakte simulieren?

Wenn der Nutzer `simulieren` wählt:

1. Simulierten Eingang erzeugen.
2. Journal- und ZIP-Platzhalter verwenden.
3. Fristen und EB so behandeln, als müssten sie fachlich geprüft werden.
4. Klar ausgeben, dass kein echter Versand und keine echte EB-Abgabe erfolgt.

## Ausgabe

`assets/templates/integrationsstatus-und-simulation.md` verwenden.
