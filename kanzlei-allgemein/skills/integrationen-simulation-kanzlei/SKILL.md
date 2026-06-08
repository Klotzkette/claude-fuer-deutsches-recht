---
name: integrationen-simulation-kanzlei
description: "Prüft Kanzlei-Integrationen und führt Workflows im Simulationsmodus weiter. Anwendungsfall E-Mail Outlook beA Fax Telefon DMS oder Buchhaltung ist nicht verbunden und Kanzlei will trotzdem Workflows testen. Normen Art. 28 DSGVO Auftragsverarbeitung bei externen Tools. Prüfraster Verbindungsstatus je Kanal Freigabe Simulationsmodus Datenschutz Protokollierung. Output Verbindungsprotokoll mit Status je Kanal und Simulationsergebnis für nicht verbundene Dienste. Abgrenzung zu kanzlei-allgemein-automationen (Planung) und kanzlei-allgemein-kaltstart im Kanzlei Allgemein: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Integrationen und Simulationsmodus

## Arbeitsbereich

Prüft Kanzlei-Integrationen und führt Workflows im Simulationsmodus weiter. Anwendungsfall E-Mail Outlook beA Fax Telefon DMS oder Buchhaltung ist nicht verbunden und Kanzlei will trotzdem Workflows testen. Normen Art. 28 DSGVO Auftragsverarbeitung bei externen Tools. Prüfraster Verbindungsstatus je Kanal Freigabe Simulationsmodus Datenschutz Protokollierung. Output Verbindungsprotokoll mit Status je Kanal und Simulationsergebnis für nicht verbundene Dienste. Abgrenzung zu kanzlei-allgemein-automationen (Planung) und kanzlei-allgemein-kaltstart. Die Prüfung konzentriert sich auf diese Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StAG §§ 4, 5, 8-17, 25, 27, 30; DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welche Integration ist konkret gemeint: E-Mail/Outlook, beA, Word, DMS, Buchhaltung, Fax, Messenger?
2. Ist die Integration echt angeschlossen oder soll ein Simulationsmodus aktiv werden?
3. Welche Daten duerfen in den Simulationsmodus eingegeben werden (Anonymisierung von Mandantendaten)?
4. Soll der Simulationsmodus für Training, Demo oder als dauerhafter Fallback genutzt werden?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- Art. 28 DSGVO — Auftragsverarbeitungsvertrag für externe Systemanbieter
- Art. 32 DSGVO — Technisch-organisatorische Massnahmen auch für Simulationsumgebungen
- § 43a Abs. 2 BRAO — Verschwiegenheit: gilt auch im Simulationsmodus mit echten Daten
- § 203 StGB — Verletzung der Berufsgeheimnisse bei unerlaubter Datenweitergabe

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill klärt, welche Systeme wirklich angeschlossen sind. Wenn etwas fehlt, fragt er freundlich, ob der Nutzer es verbinden oder simulieren möchte. So bleibt der testbar, ohne echte beA-, Outlook-, Word-, Messenger-, Fax- oder Buchhaltungszugänge zu benötigen.

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
