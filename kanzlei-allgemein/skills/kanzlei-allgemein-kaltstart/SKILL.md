---
name: kanzlei-allgemein-kaltstart
description: "Kaltstart des Kanzlei-Allgemein-Plugins und Erfassung des Kanzleiprofils. Anwendungsfall erstes Oeffnen des Plugins oder Kanzlei will Stammprofil neu einrichten. Abfrageraster Kanzleiprofil Aktenzeichen-Konvention Eingangskanale Integrationen Fristen HR Honorarpraxis UStVA Kanzleikalender Simulationsmodus. Output Kanzleiprofil-Datei Konfigurationsprotokoll und Weiterleitung zum passenden Workflow. Abgrenzung zu kanzlei-cowork-kaltstart-interview (erweitertes Profilinterview) und kanzlei-allgemein-kommandocenter."
---

# Kanzlei-Allgemein-Plugin Kaltstart


## Triage zu Beginn
1. Handelt es sich um eine Ersteinrichtung oder ein Plugin-Reset (Profil loeschen und neu beginnen)?
2. Welchen Kanzleityp haben wir: Einzelanwalt, Buerogemeinschaft, Sozietaet, PartG, GmbH, Rechtsabteilung?
3. Welche Rechtsgebiete und Mandatsarten sind typisch fuer diese Kanzlei?
4. Sind beA, E-Mail, DMS oder Buchhaltungssoftware bereits vorhanden und angebunden?

## Aktuelle Rechtsprechung
- BVerfG, Beschl. v. 14.01.2020 - 1 BvR 2316/19, NJW 2020, 897 — Berufsrechtliche Organisationspflichten gelten von Beginn der Kanzleitaetigkeit an; keine Schonfrist bei Berufseinstieg.
- BGH, Urt. v. 14.11.2019 - IX ZR 222/18, NJW 2020, 691 — Kanzleieinrichtung mit Fristenbuch, Postlauf und Mandatsorganisation ist Teil der Sorgfaltspflicht nach § 43 BRAO.
- BGH, Urt. v. 07.02.2019 - IX ZR 5/18, NJW 2019, 1513 — Kanzleiprofil (Abrechnungsart RVG oder Vereinbarung) muss von Anfang an klar definiert sein; spaetere Aenderungen koennen vertragliche Konsequenzen haben.
- BVerwG, Beschl. v. 09.11.2020 - 2 B 35.20, NVwZ 2021, 488 — Rechtsform der Kanzlei (PartG, GmbH) bestimmt Haftungsrahmen; Kaltstart muss Rechtsform korrekt erfassen.

## Zentrale Normen
- §§ 43, 43a BRAO — Allgemeine Berufspflichten: gelten ab erstem Mandatstag
- § 51 BRAO — Pflichtversicherung: muss bei Kanzleigruendung bestehen
- § 31a BRAO — beA-Nutzungspflicht: sofort bei Zulassung
- § 8 PartGG — Haftung in der Partnerschaftsgesellschaft: wichtig fuer Kanzleistruktur-Entscheidung

## Kommentarliteratur
- Gaier/Wolf/Göcken BRAO § 43 Rn. 1-30 (Berufspflichten: Inhalt und Geltung)
- Henssler/Prütting BRAO § 31a Rn. 1-20 (beA: Einrichtungspflicht und Nutzung)

## Zweck

Dieser Skill richtet das Plugin für eine Kanzlei, ein Dezernat oder einen Einzelanwalt ein. Ziel ist ein handhabbares Betriebsprofil, das spätere Workflows nicht blockiert.

## Pflichtfragen

Einmalig am Anfang fragen:

1. Kanzleityp: Einzelanwalt, Bürogemeinschaft, Sozietät, PartG, GmbH, Rechtsabteilung.
2. Rechtsgebiete und typische Mandatsarten.
3. Arbeitsmodus: Kommandocenter zuerst, Spezialskills direkt oder Simulation.
4. Aktenzeichen-Schema.
5. Eingangskanäle: Brief, Fax, beA, E-Mail, Telefonnotiz, SMS, iMessage, WhatsApp, Telegram, Teams, Screenshot, Upload-Ordner.
6. Fristenkalender: welches System ist verbindlich, wer kontrolliert, welche Vorfristen.
7. Honorar: RVG, Stundenhonorar, Pauschale, Vorschuss, Rechtsschutz.
8. Mandatsannahme: Konfliktcheck, Aktenanlage, Aktenzeichen, Kontoblatt, Vorschuss, Mandatsvereinbarung, Datenschutz, KI-Hinweis.
9. GwG: Kataloggeschäfte, Identifizierung, wirtschaftlich Berechtigte, PEP, Hochrisiko, Verdachtsfall, BRAK-Dokumentationsbögen, goAML-Status.
10. Output: Standardwege für Mandant, Gericht, Behörde, Gegner, Versicherung.
11. beA: nur vorbereiten, Versandcheck führen, Nachrichtenjournal sichern, ZIP-Archive herunterladen und entpacken oder technische Versandunterstützung möglich.
12. Zeiterfassung: Taktung, Mindestzeiteinheit, Bearbeiterrollen, Narrative-Stil, Rechnungsfreigabe.
13. Rechnung: Rechnungsnummernkreis, Pflichtangaben, GoBD-Ablage, E-Rechnungsformat, XRechnung, ZUGFeRD, Validierung, Korrekturrechnung.
14. Buchhaltung: Eingangsrechnungen, Betriebsausgaben, Vorsteuer, UStVA-Zeitraum, ELSTER oder Steuerkanzlei.
15. HR: Mitarbeiterstamm, Rollen, Arbeitsverträge, Urlaub, Krankheit, Fehlzeiten, Fortbildung, Zugänge.
16. Lohn/SV: Lohnsoftware oder Steuerkanzlei, ELStAM, Lohnsteuer-Anmeldung, SV-Meldungen, Minijobs, Bonus, Gratifikation.
17. Kanzleikalender: Fristen, Termine, Postlauf, beA, Urlaub, Krankheit, Payroll, UStVA, Jour fixe.
18. Integrationen: Word, Outlook, beA, Fax, Messenger, DMS, Fristenkalender, Buchhaltung, ELSTER, Kalender.
19. Simulationsmodus: fehlende Integrationen anschließen oder realistisch simulieren.
20. Output-Turbo: Klage, Replik, Antrag, Vertragsentwurf, Rechtsprechungsrecherche, Handelsregisterabruf, Anlagenverzeichnis.
21. Begleitmodus: knappe Hinweise, junge-Anwalt-Menüführung, Schreib-Canvas, Substanzcheck.
22. Datenschutz-Sicherheitsstufe: Testdaten, pseudonymisierte Mandate, echte Mandate.

## Sichere Defaults

Wenn der Nutzer nichts vorgibt:

- Aktenzeichen: `JAHR-RECHTSGEBIET-LFDNR`.
- Fristen: Hauptfrist plus Vorfrist; Übertragung in verbindlichen Kanzleikalender ausdrücklich bestätigen lassen.
- Versand: keine automatische Versendung, nur Entwurf und Versandcheck.
- beA: keine PINs oder Token im Chat; bei beA-Connect Journal, Screenshot, ZIP-Archiv, entpackte Nachricht und EB-Entscheidung protokollieren.
- Zeit: 6-Minuten-Takt mit kurzer, mandantenfähiger Narrative.
- Rechnung: Entwurf und GoBD-Protokoll vorbereiten, finale Rechnung erst nach Freigabe; E-Rechnung nur mit Validierungsvermerk.
- Integrationen: nichts heimlich verbinden; bei fehlendem Anschluss Simulationsmodus anbieten.
- Begleitmodus: freundlich, verzeihend, kurze hilfreiche Hinweise statt Daueralarm.
- Mandatsannahme/GwG: keine Annahme ohne dokumentierten Konfliktcheck, Annahmeentscheidung, GwG-Anwendbarkeitsprüfung und Kontoblatt. GwG-Verdacht nie still normalisieren.
- UStVA: nur vorbereiten und Übergabe an ELSTER, Buchhaltung oder Steuerkanzlei markieren.
- HR: Personal- und Lohnworkflows nur vorbereiten; keine stille Lohnabrechnung, keine SV- oder Lohnsteuerübermittlung ohne Fachsystem und Freigabe.
- Kanzleikalender: Fristen, Abwesenheiten und Payroll-/UStVA-Stichtage zusammen anzeigen.
- Kommandocenter: immer zuerst Ziel, Ampel und nächste drei Schritte ausgeben, wenn der Nutzer keinen Spezialskill nennt.

## Ausgabe

Ein `Kanzlei-Lebenszyklus-Profil` mit:

- Konventionen.
- Sicherheitsgattern.
- Ordnerstruktur.
- Integrationsstatus.
- Simulationsregeln.
- Begleitmodus-Regeln.
- Kommandocenter-Regeln.
- HR- und Payroll-Grundregeln.
- Mandatsannahme-, GwG- und Kontoblatt-Regeln.
- Kanzleikalender-Struktur.
- Qualitätsgate-Modus.
- Schriftsatz- und Vertrags-Turbo-Regeln.
- Rechtsprechungsrecherche- und Ablageregeln.
- Standard-Checklisten.
- Offenen Punkten, die noch nicht sicher entschieden sind.

## Übergabe

Danach an `kanzlei-allgemein-kommandocenter`, `kanzlei-allgemein-integrationen-simulation`, `kanzlei-allgemein-freundlicher-copilot`, `kanzlei-allgemein-kanzleikalender`, `kanzlei-allgemein-intake` und bei neuer Akte an `kanzlei-allgemein-mandatsannahme-gwg`, sobald ein Eingang oder eine neue Akte vorliegt.
