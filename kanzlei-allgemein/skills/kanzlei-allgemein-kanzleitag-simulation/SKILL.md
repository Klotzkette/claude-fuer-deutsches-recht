---
name: kanzlei-allgemein-kanzleitag-simulation
description: "Führt im Simulationsmodus durch einen achtstuendigen Kanzleitag für Training und Demo. Anwendungsfall Kanzlei will Arbeitsablaeufe testen neue Mitarbeiter einarbeiten oder Plugin-Workflow vorhalten. Abdeckt Mandatsannahme GwG Postlauf beA E-Mail Schreibcanvas Fristen Zeitnarrative Rechnung UStVA Eingangsrechnungen und Tagesabschluss. Output Simulationsprotokoll mit Tagesereignissen Fehlerliste Lernhinweisen und Leistungsbewertung. Abgrenzung zu kanzlei-allgemein-automationen (Echtbetrieb) und kanzlei-allgemein-kaltstart."
---

# Kanzleitag-Simulation


## Triage zu Beginn
1. Soll die Simulation in Echtzeit oder beschleunigt ablaufen?
2. Welche Integrationen sind echt vorhanden (beA, E-Mail, DMS) und welche werden simuliert?
3. Welche Testakten und Mandanten sollen in der Simulation vorkommen?
4. Dient die Simulation Training, Onboarding, Demo oder Qualitaetssicherung?

## Aktuelle Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen
- § 43a Abs. 2 BRAO — Verschwiegenheit: gilt auch im Simulationsmodus; keine echten Mandatsdaten ohne Anonymisierung
- Art. 32 DSGVO — TOM: Sicherheitsstandards gelten auch fuer Trainingsumgebungen
- § 43 BRAO — Fortbildungspflicht des Anwalts: Simulation als anerkanntes Fortbildungsmittel
- § 26 BDSG — Beschaeftigtendatenschutz: gilt auch bei internem Onboarding mit Simulationsdaten

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill führt durch einen realistisch wirkenden Kanzleitag, ohne echte Systeme zu benötigen. Er eignet sich für Training, Demo, Testakte und Onboarding junger Anwältinnen und Anwälte.

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
