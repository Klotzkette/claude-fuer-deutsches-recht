---
name: integrationen-simulation-kanzlei
description: "Für Integrationen und Simulationsmodus: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# Integrationen und Simulationsmodus

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BRAO §§ 43, 43a, 43e, 45, 49b, 53, 59b, 73; BORA §§ 2, 3, 4, 5, 6, 10, 11, 12; RVG §§ 3a, 10; GwG §§ 2, 10, 11, 43; DSGVO Art. 5, 6, 9, 28, 32; BDSG § 26; ZPO § 130d; BRAO § 31a/beA und lokale Kammerhinweise live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Welche Integration ist konkret gemeint: E-Mail/Outlook, beA, Word, DMS, Buchhaltung, Fax, Messenger?
2. Ist die Integration echt angeschlossen oder soll ein Simulationsmodus aktiv werden?
3. Welche Daten dürfen in den Simulationsmodus eingegeben werden (Anonymisierung von Mandantendaten)?
4. Soll der Simulationsmodus für Training, Demo oder als dauerhafter Fallback genutzt werden?

## Zentrale Normen
- Art. 28 DSGVO — Auftragsverarbeitungsvertrag für externe Systemanbieter
- Art. 32 DSGVO — Technisch-organisatorische Maßnahmen auch für Simulationsumgebungen
- § 43a Abs. 2 BRAO — Verschwiegenheit: gilt auch im Simulationsmodus mit echten Daten
- § 203 StGB — Verletzung der Berufsgeheimnisse bei unerlaubter Datenweitergabe

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

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
