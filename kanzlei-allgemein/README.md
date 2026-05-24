# Kanzlei-Allgemein-Plugin

Technischer Plugin-Name: `kanzlei-allgemein`.

Eigenständiges großes Kanzlei-Plugin für den gesamten Arbeitszyklus einer Kanzlei: edles Cowork-Kommandocenter, Nachtblau/Silber/Orange-Look, Eingang, Intake, freundliche Menüführung, Mandatsannahme, Geldwäscheprüfung, KYC, PEP-Check, Kontoblatt, Schreib-Canvas, Klage- und Replik-Turbo, Vertragsentwurf, Rechtsprechungsrecherche, Handelsregisterabruf, Qualitätsgate, Konfliktcheck, Aktenanlage, Fristen, Action-Items, beA-Nachrichtenjournal, elektronisches Empfangsbekenntnis, Kanzleikalender, HR, Urlaub, Krankheit, Payroll-Vorbereitung, granulare Zeiterfassung mit Narrative, Mandatsvereinbarung, Honorar, GoBD-nahe Rechnungsvorbereitung, Geschäftskonto, offene Posten, Zahlungseingangs-Matching, E-Rechnung, XRechnung, ZUGFeRD, UStVA-Vorbereitung, Simulation, Output und Versandkontrolle.

Es ist **nicht** auf Großkanzleien beschränkt. Der Name meint den großen Kanzlei-Workflow: vom ersten Eingang bis zum versandfertigen Ergebnis.

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Kanzlei-Lebenszyklus (`kanzlei-allgemein`, dieses Plugin) | [kanzlei-allgemein.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-allgemein.zip) |
| Kanzlei-Cowork | [kanzlei-cowork.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-cowork.zip) |
| Prozessrecht | [prozessrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/prozessrecht.zip) |

Die URL ist stabil und zeigt auf die neueste Release-Version.

## Installation

1. ZIP herunterladen.
2. Claude Code oder Claude Desktop öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `kanzlei-allgemein.zip` hochladen.
5. In einer neuen Unterhaltung mit einem typischen Auftrag starten, etwa: „Starte das volle Kanzlei-Workflow-Plugin für diese neue Nachricht.“

Wichtig: Nicht das komplette Repository-ZIP hochladen. Das Upload-ZIP muss direkt `.claude-plugin/plugin.json`, `skills/` und `assets/` im ZIP-Root enthalten; `references/` ist optional, falls ein Plugin Referenzen mitliefert.

## Was das Plugin abbildet

| Phase | Skill | Zweck |
| --- | --- | --- |
| Kommandocenter | `kanzlei-allgemein-kommandocenter` | Ein-Satz-Schnellstart, Workflow-Routing, Freigabeampel, nächste beste Aktion und nur die nötigsten Rückfragen |
| Look and Feel | `kanzlei-allgemein-look-and-feel` | Cowork-taugliches Designsystem mit Statuskarten, Dashboard, Freigabeampel und Nachtblau/Silber/Orange-Tonwelt |
| Kanzleiprofil | `kanzlei-allgemein-kaltstart` | Kanzleikonventionen, Aktenzeichen, Kanäle, Fristenlogik, Honorarstandard, Versandregeln |
| Freundlicher Copilot | `kanzlei-allgemein-freundlicher-copilot` | Verzeihende Menüführung, kurze Hinweise, Nachziehmodus, Substanzcheck für junge Anwältinnen und Anwälte |
| Integrationen | `kanzlei-allgemein-integrationen-simulation` | Word, Outlook, beA, Fax, Messenger, DMS, Fristenkalender, Buchhaltung prüfen, anschließen oder simulieren |
| Mandatsannahme/GwG | `kanzlei-allgemein-mandatsannahme-gwg` | Mandatsannahme, KYC, Kataloggeschäft, Identifizierung, wirtschaftlich Berechtigte, PEP, Verdachtsfall, Kontoblatt, Mandatsvereinbarung und BRAK-nahe Dokumentation |
| Schreib-Canvas | `kanzlei-allgemein-schreibcanvas` | Padlet-ähnliches Arbeitsbrett für Entwürfe, Tatsachen, Beweise, Anlagen, Fristen, Versand und Rechnung |
| Qualitätsgate | `kanzlei-allgemein-qualitaetsgate-hardening` | Schnellcheck, Normal- und Profi-Prüfung für Substanz, Beweise, Anlagen, Fristen, Versand, Vertrag und Rechnung |
| Schriftsatz-Turbo | `kanzlei-allgemein-schriftsatz-turbo` | Klage, Replik, Antrag oder Schriftsatzantwort samt Antrag, Sachverhalt, Beweisen, Anlagen und beA-Versand vorbereiten |
| Rechtsprechung | `kanzlei-allgemein-rechtsprechungsrecherche` | Amtliche Bundes- und Länderdatenbanken, OpenJur/dejure-Ergänzung, Fundstellenregister, Verwertungsnotiz und Akten-/Online-Ablage |
| Vertragsentwurf | `kanzlei-allgemein-vertragsentwurf` | Vertragsentwürfe aus Mandantenangaben, Term Sheet oder Vorlage mit Klauselstruktur, Risiken und Registercheck |
| Handelsregister | `kanzlei-allgemein-handelsregisterabruf` | Handelsregisterabruf über offizielle Registerquellen für Partei, Vertretung, Vertrag, Klage und Anlagenprotokoll |
| Eingang | `kanzlei-allgemein-intake` | Brief, Fax, beA, E-Mail, SMS, iMessage, WhatsApp, Telegram, Teams, Screenshot und sonstige Eingänge strukturieren |
| beA-Journal | `kanzlei-allgemein-bea-journal` | Nachrichtenjournal einsehen, Screenshot sichern, eingegangene und versandte beA-Nachrichten als ZIP archivieren, entpacken, EB-Workflow anbieten |
| Akte | `kanzlei-allgemein-akte` | Mandat anlegen, Konfliktcheck, Datenschutz, GwG, Mandatsumfang, Aktenstruktur |
| Aktenzeichen | `kanzlei-allgemein-aktenzeichen` | Eigene Aktenzeichen mit Gericht, Behörde, Gegner, Versicherung und Mandant verknüpfen |
| Fristen | `kanzlei-allgemein-fristen-monitor` | Fristen, Vorfristen, Action-Items und Wiedervorlagen aus Akteninhalt ableiten |
| Kanzleikalender | `kanzlei-allgemein-kanzleikalender` | Termine, Fristen, beA, Postlauf, Urlaub, Krankheit, Payroll, UStVA und Jour fixe zusammenführen |
| HR | `kanzlei-allgemein-hr-personal` | Mitarbeiterstamm, Arbeitsverträge, Onboarding, Offboarding, Rollen, Bonus, Gratifikation und interne Abstimmung |
| Abwesenheiten | `kanzlei-allgemein-abwesenheiten-urlaub` | Urlaub, Krankmeldungen, Fehlzeiten, Resturlaub, Vertretung und Kalenderkonflikte verwalten |
| Lohn/SV | `kanzlei-allgemein-lohn-sv` | Lohnabrechnung, Sozialversicherung, ELStAM, Lohnsteuer, Minijobs, Bonus und Gratifikation für Fachsysteme vorbereiten |
| Tagespost | `kanzlei-allgemein-postlauf` | Täglicher 11-Uhr-Postlauf mit Eingang, Fristen, Aufgaben, Versandbedarf |
| Zeit | `kanzlei-allgemein-zeitnarrative` | Stündliche Zeiterinnerung, Narrative und Aktenzuordnung |
| Mandatsvereinbarung | `kanzlei-allgemein-mandatsvereinbarung` | Mandatsvereinbarung, Haftungsbegrenzung, Honorarvereinbarung, Vollmacht |
| Output | `kanzlei-allgemein-output-versand` | Schriftsatz, Brief, E-Mail, Messenger, Fax, beA, Versandkontrolle |
| Rechnung | `kanzlei-allgemein-rechnung` | Rechnungsvorbereitung nach RVG oder Honorarvereinbarung, Auslagen, Timesheet, GoBD-Protokoll |
| Buchhaltung/Konten | `kanzlei-allgemein-buchhaltung-konten` | Geschäftskonto, offene Posten, Zahlungseingänge, Rechnungsalter, Bankmatching, Klärfälle, Mahnwesen und DATEV-ähnliche Übergabe |
| E-Rechnung | `kanzlei-allgemein-erechnung` | XRechnung als strukturiertes XML, ZUGFeRD als PDF/A-3 mit eingebettetem XML, Validierung und Archivierung |
| UStVA | `kanzlei-allgemein-ustva-buchhaltung` | Ausgangsrechnungen, Eingangsrechnungen, Betriebsausgaben, Vorsteuer, UStVA-Vorbereitung und ELSTER-Übergabe |
| UStVA-Simulation | `kanzlei-allgemein-ustva-simulation` | ELSTER-Ausfall oder fehlender Anschluss: Simulation, manueller Eingabebogen, XML-Upload-Prüfung oder Steuerberater-Paket |
| Simulation | `kanzlei-allgemein-kanzleitag-simulation` | Acht-Stunden-Kanzleitag beschleunigt oder in Echtzeit mit simulierten Integrationen durchspielen |
| Automationen | `kanzlei-allgemein-automationen` | Vorschläge für stündliche Zeiterinnerung, tägliche Postrunde und Ordner-Monitoring |

## Sicherheitsleitplanken

Dieses Plugin ist eine Experimentier- und Arbeitsstruktur. Es ersetzt keine Kanzleisoftware, keinen Fristenkalender und keine anwaltliche Letztprüfung.

Besonders wichtig:

- **beA-Versand nur nach ausdrücklicher Einzelbestätigung.**
- **Bei beA-Connect Nachrichtenjournal einsehen, Screenshot sichern, jede eingegangene und versandte Nachricht als ZIP herunterladen oder exportieren, entpacken und ablegen.**
- **Elektronisches Empfangsbekenntnis nur nach ausdrücklicher Freigabe vorbereiten oder abgeben.**
- **Software-Token, PIN, Zertifikatsdateien und Passwörter nicht in Chat, Skill, Markdown, Log oder Akte speichern.**
- Wenn ein Nutzer trotzdem einen PIN oder Token im Chat nennt: nicht wiederholen, nicht protokollieren, Löschung oder Austausch empfehlen.
- Versand über beA, Fax, Messenger oder E-Mail immer mit Versandprotokoll und Verantwortlichem dokumentieren.
- Fristen nie nur vom Modell führen lassen. Das Plugin erzeugt Prüf- und Vorschlagslisten, die in einen berufsrechtlich geeigneten Fristenkalender übertragen und kontrolliert werden müssen.
- Mandatsannahme nie nur „gefühlt“ durchführen. Konfliktcheck, GwG-Anwendbarkeit, Identifizierung, wirtschaftlich Berechtigte, PEP-/Hochrisiko-Prüfung, Honorar, Kontoblatt und Annahmeentscheidung müssen dokumentiert werden.
- Ausweiskopien, Registerauszüge, Transparenzregisterdaten und GwG-Vermerke nur geschützt ablegen. Keine Ausweisnummern, sensiblen Dokumente oder Verdachtsdetails unnötig in Chat, Logs oder ungeschützte Markdown-Dateien kopieren.
- Verdachtsmeldungen, goAML, Unstimmigkeitsmeldungen und Mandatsablehnungen werden nur vorbereitet und zur Berufsträger-Freigabe vorgelegt, nicht automatisch ausgelöst.
- Rechnungen nie automatisch finalisieren, versenden oder buchen. Das Plugin erzeugt Rechnungsdatenblatt, GoBD-Protokoll und E-Rechnungsdatenblatt; Freigabe, technische Validierung und Buchung bleiben beim Nutzer oder Fachsystem.
- Geschäftskonto und Buchhaltung nur nach Freigabe anbinden oder simulieren. Keine Bankzugangsdaten, TANs, PINs oder API-Secrets im Chat speichern. Zahlungsaufträge, endgültige Buchungen und DATEV-Übertragungen nicht still ausführen.
- XRechnung wird als strukturiertes XML behandelt. ZUGFeRD wird als PDF/A-3-Hybrid mit eingebettetem XML behandelt; PDF und XML müssen konsistent sein.
- UStVA wird nur vorbereitet oder simuliert. Elektronische Übermittlung, Steuerberatung, Buchung und Fristenkontrolle bleiben bei Nutzer, Steuerkanzlei oder Fachsystem.
- Für ELSTER gilt: Ein frei erzeugtes PDF oder Markdown-Dokument ist keine echte UStVA-Abgabe. Ein Eingabebogen kann bei manueller Online-Erfassung helfen; XML-Upload nur mit passendem, validiertem ELSTER/ERiC-Datensatz oder Fachsoftware.
- HR, Urlaub, Krankheit und Payroll enthalten sensible Beschäftigtendaten. Diagnosen nicht erfassen, Lohn- und SV-Meldungen nicht still übermitteln, Fachsystem- oder Steuerkanzlei-Übergabe klar markieren.
- Kanzleikalender ist ein Koordinationswerkzeug. Verbindliche Fristenkontrolle, Lohnabrechnung und Steueranmeldungen bleiben in den zuständigen Fachsystemen.
- Klage, Replik, Vertrag und Handelsregisterabruf laufen durch ein Qualitätsgate. Das Plugin darf Entwürfe beschleunigen, aber nicht ohne Freigabe versenden oder als gerichtsfertig garantieren.
- Rechtsprechungsrecherche bevorzugt amtliche Volltexte der Bundesgerichte und Länder. OpenJur und dejure.org sind Ergänzungsquellen; jede Fundstelle braucht Quelle, URL, Abrufdatum, Aktenzeichen/ECLI, Rn./Seite und Aktualitätscheck.
- Handelsregisterdaten aus offiziellen Quellen abrufen und mit Quelle, Zeitstempel und Dokumentart protokollieren.
- Wenn Word, Outlook, beA, Fax, Messenger, DMS, Fristenkalender oder Buchhaltung nicht angeschlossen sind, fragt das Plugin, ob angeschlossen oder simuliert werden soll.
- Der freundliche Copilot darf Hinweise geben, soll aber nicht nerven: kurz, konkret, verzeihend und mit Nachziehmodus.
- Mandatsgeheimnis, § 203 StGB, § 43e BRAO, DSGVO, BORA, Aufbewahrungspflichten und Beschlagnahmeschutz bleiben beim Nutzer.

## Vorschau: Startbild

```text
Kanzlei-Allgemein-Plugin gestartet

| Akte | Ampel | Frist | Nächste Aktion |
| --- | --- | --- | --- |
| offen | GELB | offen | Eingang einordnen und Workflow wählen |

Tonwelt: Nachtblau für Aktenarbeit, Silber für Ablage, Orange für Entscheidungen.

1. Kommandocenter: Ziel erkennen, Ampel setzen, nächste drei Schritte
2. Workflow starten: Mandatsannahme, Post, Klage, Replik, Vertrag, Rechnung oder Simulation
3. Freigabegrenzen zeigen: nicht versenden, nicht annehmen, nicht buchen, nicht melden
```

## Ordner und Vorlagen

Das Plugin bringt Markdown-Vorlagen mit:

- `assets/templates/mandatsblatt-vorlage.md`
- `assets/templates/cowork-designsystem.md`
- `assets/templates/cowork-dashboard.md`
- `assets/templates/cowork-statuskarte.md`
- `assets/templates/cowork-freigabekarte.md`
- `assets/templates/workflow-kommandocenter.md`
- `assets/templates/workflow-schnellstartkarte.md`
- `assets/templates/workflow-freigabeampel.md`
- `assets/templates/workflow-naechste-beste-aktion.md`
- `assets/templates/mandatsannahme-gwg-start.md`
- `assets/templates/gwg-anwendbarkeit-kataloggeschaeft.md`
- `assets/templates/gwg-identifizierung-und-dokumente.md`
- `assets/templates/gwg-risikobewertung-mandat.md`
- `assets/templates/gwg-pep-sanktionen-transparenzregister.md`
- `assets/templates/gwg-verdachtsfall-entscheidungsvermerk.md`
- `assets/templates/mandatskontoblatt.md`
- `assets/templates/mandatsvereinbarung-ki-datenschutz-hinweis.md`
- `assets/templates/freundlicher-copilot-hinweise.md`
- `assets/templates/schreibcanvas.md`
- `assets/templates/qualitaetsgate-checkliste.md`
- `assets/templates/schriftsatz-turbo-geruest.md`
- `assets/templates/klage-replik-pruefmatrix.md`
- `assets/templates/anlagenverzeichnis-schriftsatz.md`
- `assets/templates/rechtsprechungsrecherche-suchplan.md`
- `assets/templates/rechtsprechungsfundstellen-register.md`
- `assets/templates/rechtsprechungsablage-protokoll.md`
- `assets/templates/rechtsprechungsmonitor.md`
- `assets/templates/vertragsentwurf-playbook.md`
- `assets/templates/vertragsrisiken-matrix.md`
- `assets/templates/handelsregisterabruf-protokoll.md`
- `assets/templates/integrationsstatus-und-simulation.md`
- `assets/templates/kanzleitag-simulation.md`
- `assets/templates/bea-nachrichtenjournal.md`
- `assets/templates/fristen-und-action-register.md`
- `assets/templates/zeit-narrative-ledger.md`
- `assets/templates/rechnungsdatenblatt.md`
- `assets/templates/erechnung-datenblatt.md`
- `assets/templates/gobd-rechnungsprotokoll.md`
- `assets/templates/buchhaltung-kontoauszug.md`
- `assets/templates/offene-posten-debitoren.md`
- `assets/templates/zahlungseingang-matching.md`
- `assets/templates/mahn-und-klaerfallregister.md`
- `assets/templates/datev-uebergabe-simulation.md`
- `assets/templates/eingangsrechnungen-register.md`
- `assets/templates/ustva-vorbereitungsblatt.md`
- `assets/templates/ustva-elster-simulation.md`
- `assets/templates/ustva-elster-eingabebogen.md`
- `assets/templates/ustva-xml-upload-pruefung.md`
- `assets/templates/ustva-steuerberater-paket.md`
- `assets/templates/personalstammblatt.md`
- `assets/templates/hr-onboarding-offboarding.md`
- `assets/templates/lohnabrechnung-vorbereitung.md`
- `assets/templates/abwesenheiten-register.md`
- `assets/templates/kanzleikalender.md`
- `assets/templates/jour-fixe-protokoll.md`
- `assets/templates/postlauf-journal.md`
- `assets/templates/output-versandprotokoll.md`

Diese Dateien sind bewusst textbasiert, damit sie in jeder Umgebung lesbar sind. Wenn die Laufzeit echte Automationen, lokale Ordnerüberwachung oder Kalender-Connectoren unterstützt, nutzt der Skill diese nur nach ausdrücklicher Zustimmung.

## Empfohlene Begleitplugins

Das Plugin funktioniert allein. Für fachliche Ausarbeitung sind je nach Mandat zusätzlich hilfreich:

- `prozessrecht` für gerichtliche Schriftsätze und Fristenlogik.
- `kanzlei-cowork` für bestehende Kanzlei-Cowork-Bausteine.
- `zitierweise-deutsches-recht` und `methodenlehre-buergerliches-recht` für juristische Ausgabequalität.
- Rechtsgebietsplugins wie `arbeitsrecht`, `vertragsrecht`, `sozialrecht-kanzlei`, `steuerrecht-anwalt-und-berater`, `insolvenzrecht`.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Das Plugin bildet Arbeitsabläufe und Sicherheitsgatter ab. Es ersetzt keine Fristenkontrolle durch Berufsträger, keine Kanzleisoftware und keine Prüfung der Zulässigkeit konkreter Kommunikation im Einzelfall.
