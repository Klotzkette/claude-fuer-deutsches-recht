---
name: kanzleitag-simulation-kanzlei
description: "Führt im Simulationsmodus durch einen achtstuendigen Kanzleitag für Training und Demo. Anwendungsfall Kanzlei will Arbeitsablaeufe testen neue Mitarbeiter einarbeiten oder Plugin-vorhalten. Abdeckt Mandatsannahme GwG Postlauf beA E-Mail Schreibcanvas Fristen Zeitnarrative Rechnung UStVA Eingangsr..."
---

# Kanzleitag-Simulation

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO §§ 43, 43a, 43e, 45, 49b, 53, 59b, 73; BORA §§ 2, 3, 4, 5, 6, 10, 11, 12; RVG §§ 3a, 10; GwG §§ 2, 10, 11, 43; DSGVO Art. 5, 6, 9, 28, 32; BDSG § 26; ZPO § 130d; BRAO § 31a/beA und lokale Kammerhinweise live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Triage zu Beginn
1. Soll die Simulation in Echtzeit oder beschleunigt ablaufen?
2. Welche Integrationen sind echt vorhanden (beA, E-Mail, DMS) und welche werden simuliert?
3. Welche Testakten und Mandanten sollen in der Simulation vorkommen?
4. Dient die Simulation Training, Onboarding, Demo oder Qualitaetssicherung?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 43a Abs. 2 BRAO — Verschwiegenheit: gilt auch im Simulationsmodus; keine echten Mandatsdaten ohne Anonymisierung
- Art. 32 DSGVO — TOM: Sicherheitsstandards gelten auch für Trainingsumgebungen
- § 43 BRAO — Fortbildungspflicht des Anwalts: Simulation als anerkanntes Fortbildungsmittel
- § 26 BDSG — Beschäftigtendatenschutz: gilt auch bei internem Onboarding mit Simulationsdaten

## Startfragen

1. Echtzeit oder beschleunigt?
2. Welche Integrationen sind echt angeschlossen?
3. Welche Integrationen sollen simuliert werden?
4. Welche Akten sollen vorkommen?
5. Soll der freundliche Copilot aktiv Hinweise geben?
6. Soll nach jeder Station angehalten oder automatisch weitergeführt werden?

## Acht-Stunden-Ablauf

```text
09:00 Tagesstart, offene Fristen, Kalender, Integrationen
10:00 Intake aus E-Mail, Messenger, Fax oder Screenshot
11:00 Postlauf mit beA-Journal, EB-Prüfung, ZIP-Archiv
12:00 Schreib-Canvas für Schriftsatz oder Mandantenbrief
13:00 Zeitnarrative und kurze Pause
14:00 Neue Mandatsanfrage: Konfliktcheck, GwG, KYC, PEP, Kontoblatt, Vorschuss
15:00 Eingangsrechnungen, Betriebsausgaben, UStVA-Vorbereitung, ELSTER-Fallback
16:00 HR, Urlaub, Krankheit, Kanzleikalender und Payroll-Vorbereitung
17:00 Rechnung, E-Rechnung oder Mandatsvereinbarung vorbereiten
17:30 Versandcheck, beA/Fax/E-Mail simulieren oder echt vorbereiten
18:00 Tagesabschluss, Fristen, offene Fragen, Zeit, Rechnung und Personal
```

## Tempo

Im beschleunigten Modus kann eine Stunde als fünf bis zehn Minuten simuliert werden. Vor risikoreichen Handlungen immer anhalten:

- Fristübernahme.
- EB-Abgabe.
- beA-Versand.
- Rechnung finalisieren.
- Mandat annehmen.
- Ausweisdokumente auslesen oder ablegen.
- Verdachtsmeldung oder Unstimmigkeitsmeldung vorbereiten.
- E-Rechnung validieren.
- UStVA übermitteln.
- Lohnabrechnung, SV-Meldung oder Lohnsteuer-Anmeldung übermitteln.
- Krankheitsdaten oder Personalakte ausgeben.

Wenn ELSTER oder Buchhaltung nicht angeschlossen ist, an `kanzlei-allgemein-ustva-simulation` übergeben und zwischen ELSTER-Online-Simulation, manuellem Eingabebogen, XML-Upload-Prüfung und Steuerberater-Paket wählen lassen.

Wenn Kalender, HR- oder Lohnsoftware nicht angeschlossen ist, an `kanzlei-allgemein-kanzleikalender`, `kanzlei-allgemein-hr-personal`, `kanzlei-allgemein-abwesenheiten-urlaub` und `kanzlei-allgemein-lohn-sv` übergeben und ausdrücklich als Simulation markieren.

Wenn Mandatsannahme oder GwG nicht echt angebunden ist, an `kanzlei-allgemein-mandatsannahme-gwg` übergeben und Ausweis-, Register-, PEP-, Mittelherkunfts- und Kontoblattprüfungen als Simulation markieren.

## Ausgabe

`assets/templates/kanzleitag-simulation.md` verwenden.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

