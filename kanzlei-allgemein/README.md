# Kanzlei-Allgemein-Plugin


<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Akte Kanzlei-Allgemein-Plugin** (`kanzlei-allgemein-alltag`) | [Gesamt-PDF lesen](../testakten/kanzlei-allgemein-alltag/gesamt-pdf/kanzlei-allgemein-alltag_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzlei-allgemein-alltag.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Technischer Plugin-Name: `kanzlei-allgemein`.

Eigenständiges großes Kanzlei-Plugin für den gesamten Arbeitszyklus einer Kanzlei. **Mit v11.0.0 wurden die Skills des früheren `kanzlei-cowork`-Plugins vollständig in `kanzlei-allgemein` integriert** — Fristenbuch, Timesheet, RVG-Rechnung, Versand-Vor-Check, beA-Versand-Prüfung, Posteingang/Postausgang, Mandantenakte, Aktenbestandspflege, Honorar-Mahnwesen, Mandantenbriefe, Geburtstage, Weihnachtskarten und Sekretariats-Tagesbrief.

Das Plugin deckt: edles Cowork-Kommandocenter, Nachtblau/Silber/Orange-Look, Eingang, Intake, freundliche Menüführung, Mandatsannahme, Geldwäscheprüfung, KYC, PEP-Check, Kontoblatt, Schreib-Canvas, Klage- und Replik-Turbo, Vertragsentwurf, Rechtsprechungsrecherche, Handelsregisterabruf, Qualitätsgate, Konfliktcheck, Aktenanlage, Fristen, Action-Items, beA-Nachrichtenjournal, elektronisches Empfangsbekenntnis, Kanzleikalender, HR, Urlaub, Krankheit, Payroll-Vorbereitung, granulare Zeiterfassung mit Narrative, Mandatsvereinbarung, Honorar, GoBD-nahe Rechnungsvorbereitung, Geschäftskonto, offene Posten, Zahlungseingangs-Matching, E-Rechnung, XRechnung, ZUGFeRD, UStVA-Vorbereitung, Simulation, Output und Versandkontrolle.

Es ist **nicht** auf Großkanzleien beschränkt. Der Name meint den großen Kanzlei-Workflow: vom ersten Eingang bis zum versandfertigen Ergebnis.

## ⬇️ Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **sachverstaendigengutachten ki vorwurf lg regensburg sieglinger** | [testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip) |

Im ZIP sind die Originalformate (PDF, DOCX, XLSX, CSV, JPEG) für realistische Tests.

## Direkt-Download

| Plugin | Direkt-Download |
| --- | --- |
| Kanzlei-Lebenszyklus (`kanzlei-allgemein`, dieses Plugin) | [kanzlei-allgemein.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-allgemein.zip) |
| Prozessrecht | [prozessrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/prozessrecht.zip) |

Die URL ist stabil und zeigt auf die neueste Release-Version.

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Kanzlei-Allgemein-Plugin** ([`testakten/kanzlei-allgemein-alltag/`](../testakten/kanzlei-allgemein-alltag/)).

Direkt-Download als ZIP: [testakte-kanzlei-allgemein-alltag.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzlei-allgemein-alltag.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## Installation

1. ZIP herunterladen.
2. Claude Code oder Claude Desktop öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `kanzlei-allgemein.zip` hochladen.
5. In einer neuen Unterhaltung mit einem typischen Auftrag starten, etwa: "Starte das volle Kanzlei-Workflow-Plugin für diese neue Nachricht."

Wichtig: Nicht das komplette Repository-ZIP hochladen. Das Upload-ZIP muss direkt `.claude-plugin/plugin.json`, `skills/` und `assets/` im ZIP-Root enthalten; `references/` ist optional, falls ein Plugin Referenzen mitliefert.

### Zum Ausprobieren: Testakte (separat)

Fiktive Mandatsakte zum sofortigen Testen — **kein Teil des Plugins**, separater Download:

| Testakte | Direkt-Download |
| --- | --- |
| **Kanzlei-Alltag** | [testakte-kanzlei-allgemein-alltag.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzlei-allgemein-alltag.zip) |

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

## Cowork-/Sekretariats-Skills (fusioniert aus `kanzlei-cowork`)

| Skill | Zweck |
| --- | --- |
| `aktenbestand-pflege` | Laufende Pflege des Aktenbestands — Aktualisierung Status (laufend/ruhend/abgeschlossen), Mandatsende mit Schlussrechnung, Archivierung nach Aufbewahrungspflicht |
| `bea-versand-pruefen` | Prüft den beA-Versand nach §§ 130a ZPO; 32d StPO; 65d SGG; 55a VwGO; 52d FGO sowie § 31a BRAO; sicherer Übermittlungsweg, qeS-Optionen, EB-Logik |
| `fristenbuch-fuehren` | Zentrales Fristenbuch mit Haupt- und Vorfristen, Berechnung nach ZPO/StPO/SGG/FGO/VwGO/FamFG/AO/BGB; Vier-Tages-Fiktion PostModG seit 1.1.2025 |
| `geburtstage-feiertage` | Mandanten- und Geschäftspartner-Geburtstagsverteiler, Firmenjubiläen, formell-warme Glückwunsch-Vorlagen |
| `kanzlei-cowork-kaltstart-interview` | Kaltstart-Interview für das Cowork-Profil der Kanzlei (Profil, Rechtsgebiete, Sekretariat, Aktenstruktur, beA-Profil, Versandregeln) |
| `mahnwesen-honorar` | Mahnwesen Honorarforderungen — Stufen Zahlungserinnerung, erste/zweite/dritte Mahnung nach § 286 BGB, Klagedrohung |
| `mandantenakte-anlegen` | Mandantenakte nach Kanzleikonvention — Stammdaten, Vollmacht, Mandatsumfang, Konflikt § 43a IV BRAO/§ 3 BORA, Art. 13 DSGVO, GwG-Identifizierung |
| `mandantenbrief-vorlagen` | Standardvorlagen Mandantenbrief — Anrede, Bezug, Sachstand, Empfehlung, nächste Schritte, Frist, Kostenhinweis, Berufsbezeichnung |
| `posteingang-ausgang` | Postein- und Postausgangsbuch — Empfangstag (Fristbeginn), Absender, Akte, Aktion; Versandbuch mit beA/Brief/Fax/E-Mail |
| `rechnungserstellung-rvg` | Honorarrechnungen nach RVG (Anlage 1 VV RVG, Anlage 2 Gebührentabelle) oder Honorarvereinbarung; Pflichtangaben § 10 RVG |
| `sekretariats-tagesbrief` | Tagesbrief mit Fristen heute und nächste Woche, Vorfristen, Posteingang Vortag, Wiedervorlagen, Termine, beA-Eingang |
| `timesheet-aktenzeitung` | Zeiterfassung pro Mandat (Aktenzeitung) in 6-Minuten-Blöcken, Abrechenbarkeit, Honorarsatz, Reports |
| `versand-vor-check` | Pflicht-Pre-Check vor Versand — Dokumentidentität, Unterschrift, Adressat, Anlagen, Versandweg, qeS bei beA |
| `weihnachtskarten` | Weihnachtskartenverteiler — postalisch oder digital, formell-zurückhaltend bis persönlich, Drucklisten |

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
- Mandatsannahme nie nur "gefühlt" durchführen. Konfliktcheck, GwG-Anwendbarkeit, Identifizierung, wirtschaftlich Berechtigte, PEP-/Hochrisiko-Prüfung, Honorar, Kontoblatt und Annahmeentscheidung müssen dokumentiert werden.
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
- (Hinweis: Das frühere Plugin `kanzlei-cowork` ist seit v11.0.0 vollständig in dieses Plugin fusioniert. Externe Verweise auf `kanzlei-cowork` zeigen jetzt auf `kanzlei-allgemein`.)
- `zitierweise-deutsches-recht` und `methodenlehre-buergerliches-recht` für juristische Ausgabequalität.
- Rechtsgebietsplugins wie `arbeitsrecht`, `vertragsrecht`, `sozialrecht-kanzlei`, `steuerrecht-anwalt-und-berater`, `insolvenzrecht`.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Das Plugin bildet Arbeitsabläufe und Sicherheitsgatter ab. Es ersetzt keine Fristenkontrolle durch Berufsträger, keine Kanzleisoftware und keine Prüfung der Zulässigkeit konkreter Kommunikation im Einzelfall.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 48 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenbestand-pflege` | Laufende Pflege des Aktenbestands der Kanzlei — Aktualisierung Aktenstatus (laufend / ruhend / abgeschlossen) Mandatsende mit Schlussrechnung und Aktenherausgabe an Mandant Archivierung nach Aufbewahrungspflicht (§ 50 BRAO sechs Jahre na... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Kanzlei Allgemein-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan.... |
| `bea-versand-pruefen` | Prüft den beA-Versand nach Pflichten des § 130a ZPO § 32d StPO § 65d SGG § 55a VwGO § 52d FGO sowie § 31a BRAO. Erforderliche Beachtung sicherer Übermittlungsweg (sUW durch persoenliches Versenden des beA-Inhabers) oder qualifizierte ele... |
| `fristenbuch-fuehren` | Zentrales Fristenbuch für die Kanzlei mit Haupt- und Vorfristen über alle Rechtsgebiete. Berechnet Fristbeginn nach den jeweiligen Verfahrensordnungen (ZPO StPO SGG FGO VwGO FamFG AO BGB) Vier-Tages-Fiktionen bei Postzustellung (PostModG... |
| `geburtstage-feiertage` | Pflegt einen Mandanten- und Geschäftspartner-Geburtstagsverteiler. Reminders einige Tage vor dem Tag. Vorlagen für kurze persoenliche Glueckwunsch-E-Mail (formell-warm). Bei Geschäftspartnern auch Firmenjubilaeen. Geburtstagsverteiler ge... |
| `kanzlei-allgemein-abwesenheiten-urlaub` | Verwaltung von Abwesenheiten in der Kanzlei — Urlaub Krankmeldung Elternzeit Pflegezeit Fortbildung. Anwendungsfall Anwalt oder Mitarbeiter meldet Urlaub oder Krankheit und Kanzlei muss Vertretung für Fristen beA Postlauf Mandantenkommun... |
| `kanzlei-allgemein-akte` | Anlage oder Zuordnung einer Kanzleiakte bei neuer Mandatsanfrage oder eingehendem Schriftstueck. Anwendungsfall Mandant erteilt neuen Auftrag oder Eingang ist keiner Akte zugeordnet. Normen § 43a Abs. 4 BRAO Konfliktcheck § 3 BORA Art. 1... |
| `kanzlei-allgemein-aktenzeichen` | Erkennung Normalisierung und Verknuepfung von Aktenzeichen in der Kanzlei. Anwendungsfall beA-Nachricht oder Brief enthaelt Aktenzeichen das einer Akte zugeordnet werden muss. Normen § 51 BRAO Organisationspflicht § 253 Abs. 2 Nr. 1 ZPO... |
| `kanzlei-allgemein-automationen` | Plant und dokumentiert wiederkehrende Kanzlei-Routinen als sichere automatisierte Ablaeufe. Anwendungsfall Kanzlei will Postlauf Fristencheck UStVA-Vorbereitung oder Payroll automatisieren. Normen Art. 6 Art. 28 Art. 32 DSGVO Auftragsver... |
| `kanzlei-allgemein-bea-journal` | Dokumentation von beA-Verbindungen Nachrichten Versand und Empfangsbekenntnissen. Anwendungsfall beA-Eingang oder Versand muss nachvollziehbar protokolliert werden mit Screenshot ZIP-Export und EB-Workflow. Normen § 130a ZPO § 31a BRAO §... |
| `kanzlei-allgemein-buchhaltung-konten` | Kanzlei-Buchhaltung mit Geschäftskonto offenen Posten Debitoren Kreditoren und Bankmatching. Anwendungsfall Anwalt oder Kanzleibuero will Zahlungseingang prüfen offene Posten abgleichen oder Buchhaltungsuebergabe an DATEV vorbereiten. No... |
| `kanzlei-allgemein-erechnung` | Elektronische Kanzleirechnung in XRechnung oder ZUGFeRD vorbereiten und validieren. Anwendungsfall Mandant oder öffentliche Hand verlangt Rechnung im Format XRechnung oder ZUGFeRD. Normen EN 16931 GoBD § 14 UStG Rechnungspflichtangaben.... |
| `kanzlei-allgemein-freundlicher-copilot` | Führt junge Anwaelte freundlich durch alle Kanzlei-Workflows mit Nachhilfemodus. Anwendungsfall Berufsanfaenger oder Quereinsteiger weiss nicht wie er Akte anlegen Rechnung schreiben oder beA nutzen soll. Prüft Luecken in beA Rechnung Fr... |
| `kanzlei-allgemein-fristen-monitor` | Scannt Akteninhalt auf Fristen Action-Items Wiedervorlagen und Zustellungen. Anwendungsfall Schriftsatz beA-Nachricht oder Urteil wurde hochgeladen und Fristen sollen automatisch erkannt werden. Normen § 222 ZPO §§ 187 188 BGB § 517 ZPO... |
| `kanzlei-allgemein-handelsregisterabruf` | Handelsregisterabruf über offizielle Quellen für Unternehmensprüfung in Mandaten. Anwendungsfall Mandant oder Gegner ist eine GmbH und Vertretung Gesellschafterstruktur und Prokura muessen geprüft werden. Normen §§ 15 17 HGB Registerrech... |
| `kanzlei-allgemein-hr-personal` | Verwaltung von Kanzlei-Personal mit Stammdaten Arbeitsvertraegen Onboarding und Offboarding. Anwendungsfall neue Kanzleimitarbeiterin wird eingestellt oder Mitarbeiter scheidet aus und HR-Dokumentation muss gepflegt werden. Normen BDSG §... |
| `kanzlei-allgemein-intake` | Strukturiert jeden Kanzlei-Eingang aus Brief Fax beA E-Mail SMS iMessage WhatsApp Telegram Teams Screenshot Upload oder Telefonnotiz. Erkennt Absender Akte Aktenzeichen Fristen Action-Items Datenschutzrisiken und nächsten Schritt. Fragt... |
| `kanzlei-allgemein-integrationen-simulation` | Prüft Kanzlei-Integrationen und führt Workflows im Simulationsmodus weiter. Anwendungsfall E-Mail Outlook beA Fax Telefon DMS oder Buchhaltung ist nicht verbunden und Kanzlei will trotzdem Workflows testen. Normen Art. 28 DSGVO Auftragsv... |
| `kanzlei-allgemein-kaltstart` | Kaltstart des Kanzlei-Allgemein-Plugins und Erfassung des Kanzleiprofils. Anwendungsfall erstes Oeffnen des Plugins oder Kanzlei will Stammprofil neu einrichten. Abfrageraster Kanzleiprofil Aktenzeichen-Konvention Eingangskanale Integrat... |
| `kanzlei-allgemein-kanzleikalender` | Führt einen Kanzleikalender für Termine Fristen Postlauf HR und Jour fixe. Anwendungsfall Anwalt will tagesaktuelle Übersicht über Termine Fristen Abwesenheiten UStVA-Fälligkeiten und interne Abstimmungen. Normen § 517 ZPO Berufungsfrist... |
| `kanzlei-allgemein-kanzleitag-simulation` | Führt im Simulationsmodus durch einen achtstuendigen Kanzleitag für Training und Demo. Anwendungsfall Kanzlei will Arbeitsablaeufe testen neue Mitarbeiter einarbeiten oder Plugin-Workflow vorhalten. Abdeckt Mandatsannahme GwG Postlauf be... |
| `kanzlei-allgemein-kommandocenter` | Schnellstart und Command Center für Kanzlei-Allgemein-Plugin. Erkennt aus einem Satz den passenden Kanzlei-Workflow, routet zu Mandatsannahme GwG Klage Replik Vertrag Rechtsprechung beA Fristen Rechnung Buchhaltung HR UStVA oder Simulati... |
| `kanzlei-allgemein-lohn-sv` | Bereitet Lohnabrechnung Sozialversicherungsmeldungen und Payroll-Übergabe für Kanzleimitarbeiter vor. Anwendungsfall monatliche Lohnabrechnung muss vorbereitet oder Daten für DATEV-Lohnsoftware oder Steuerkanzlei zusammengestellt werden.... |
| `kanzlei-allgemein-look-and-feel` | Gestaltet Ausgaben des Kanzlei-Allgemein-Plugins hochwertig ruhig und edel. Anwendungsfall Plugin-Output soll innerhalb Cowork-Grenzen professionell aussehen ohne CSS-Abhaengigkeit. Werkzeuge Markdown-Dashboards Statuskarten Freigabeampe... |
| `kanzlei-allgemein-mandatsannahme-gwg` | Führt Mandatsannahme und Geldwäscheprüfung für Kanzleien: Intake, Aktenanlage, Aktenzeichen, Kontoblatt, Konfliktcheck, Kataloggeschäft nach § 2 Abs. 1 Nr. 10 GwG, Identifizierung, Ausweiskopie, Handelsregister, wirtschaftlich Berechtigt... |
| `kanzlei-allgemein-mandatsvereinbarung` | Erstellt Mandatsvereinbarung Vollmacht Datenschutzhinweis Honorarvereinbarung und Vorschuss. Anwendungsfall neues Mandat soll foermlich begründet werden mit allen Pflichtdokumenten nach BRAO. Normen § 3a RVG Honorarvereinbarung § 49b BRA... |
| `kanzlei-allgemein-output-versand` | Steuert Output und Versand für Schriftsatz Brief E-Mail Fax beA SMS Messenger Teams und Mandantenportal. Fragt vor beA-Versand ausdrücklich nach Freigabe warnt vor PIN Token und Geheimnissen und dokumentiert Journal Screenshot ZIP-Archiv... |
| `kanzlei-allgemein-postlauf` | Führt den täglichen Postlauf ideal um 11 Uhr. Prüft neue Eingänge beA-Journal Fristen Action-Items nicht zugeordnete Akten Versandbedarf EB und Rückfragen. Erstellt ein Postlauf-Journal und übergibt an Akten Fristen Output Zeit und Rechn... |
| `kanzlei-allgemein-qualitaetsgate-hardening` | Haertet Kanzlei-Outputs mit mehrstufigen Qualitaetsgates für Anfaenger und Profis. Anwendungsfall Schriftsatz Vertrag oder beA-Versand soll vor Abgang auf Substanz Vollständigkeit und Haftungsrisiken geprüft werden. Normen § 51 BRAO Haft... |
| `kanzlei-allgemein-rechnung` | Bereitet Kanzleirechnungen Vorschussrechnungen RVG-Abrechnungen und Stundenhonorare vor. Anwendungsfall Mandat ist abgeschlossen oder Zeitpunkt für Zwischenrechnung ist gekommen. Normen § 10 RVG Pflichtangaben § 14 UStG Umsatzsteuerauswe... |
| `kanzlei-allgemein-rechtsprechungsrecherche` | Recherchiert Rechtsprechung zu einer konkreten Sache in amtlichen Datenbanken der Bundesgerichte und Länder, ergänzt OpenJur und dejure.org, bewertet Treffer, erstellt Zitier- und Verwertungsnotizen und legt Fundstellen samt Quellenproto... |
| `kanzlei-allgemein-schreibcanvas` | Bietet ein freies Schreib-Canvas für Schriftsaetze Briefe Rechnungen beA-Nachrichten und Mandantenkommunikation. Anwendungsfall Anwalt will einen Entwurf strukturieren oder schwache Stellen in einem laufenden Text aufdecken lassen. Prüfr... |
| `kanzlei-allgemein-schriftsatz-turbo` | Erstellt schnell Klage Replik Antrag Klageerwiderung oder Schriftsatzantwort mit Anlagenlogik. Anwendungsfall Frist laeuft und Schriftsatz muss schnell mit allen Pflichtbestandteilen erstellt werden. Normen § 253 ZPO Klageschrift § 276 Z... |
| `kanzlei-allgemein-ustva-buchhaltung` | Sammelt Rechnungsdaten und Belege für die monatliche Umsatzsteuervoranmeldung. Anwendungsfall Monat ist vorbei und UStVA-Unterlagen muessen für ELSTER oder Steuerkanzlei zusammengestellt werden. Normen §§ 18 21 UStG UStVA-Pflicht § 14 US... |
| `kanzlei-allgemein-ustva-simulation` | Fallback bei ELSTER-Stoerung oder fehlendem Steuersoftware-Zugang für UStVA-Simulation. Anwendungsfall ELSTER-Verbindung funktioniert nicht oder UStVA muss ohne Fachsoftware simuliert werden. Normen § 18 Abs. 1 UStG Abgabefrist § 149 AO... |
| `kanzlei-allgemein-vertragsentwurf` | Erstellt Vertragsentwuerfe aus Term Sheet Mandantenangaben oder Vorlagen für jede Vertragsart. Anwendungsfall Mandant braucht Vertragsentwurf und Ausgangsmaterial liegt als Term Sheet Stichpunkte oder Muster vor. Normen §§ 305 ff. BGB AG... |
| `kanzlei-allgemein-zeitnarrative` | Zeiterfassung mit abrechenbaren Narrativen für Kanzlei-Mandate. Anwendungsfall Anwalt hat Tätigkeit ausgeubt und will Zeit mit praezisem Narrativ erfassen für spaetere Rechnungsstellung. Normen § 10 RVG Pflichtangaben Narrative GoBD-Zeit... |
| `kanzlei-cowork-kaltstart-interview` | Kaltstart-Interview für das generische Kanzlei-Cowork-Plugin. Erfragt Kanzleiprofil (Solo / Sozietaet / GmbH / Partnerschaft) Rechtsgebiete-Mix Sekretariat (vorhanden Stellen) Aktenstruktur-Konvention beA-Profil Versandwege Buchhaltungss... |
| `mahnwesen-honorar` | Mahnwesen für eigene Honorarforderungen der Kanzlei gegenüber Mandanten. Anwendungsfall Mandant hat Rechnung nicht bezahlt und Kanzlei muss mahnen oder klagen. Normen § 286 BGB Verzugsbeginn § 288 BGB Verzugszinsen § 23 Nr. 1 GVG AG-Zust... |
| `mandantenakte-anlegen` | Legt eine Mandantenakte nach Kanzleikonvention an. Erfasst Stammdaten Bevollmaechtigte Mandatsumfang Konfliktprüfung (§ 43a Abs. 4 BRAO § 3 BORA) Datenschutzhinweis (Art. 13 DSGVO) Geldwäsche-Identifizierung (§§ 10 11 GwG) Honorarvereinb... |
| `mandantenbrief-vorlagen` | Standardvorlagen für den Mandantenbrief der Kanzlei. Aufbau Anrede Bezug Sachstand Empfehlung naechste Schritte Frist Kostenhinweis Unterschrift mit Berufsbezeichnung. Verschiedene Vorlagen für Mandatseroeffnung Zwischenbericht Beratungs... |
| `posteingang-ausgang` | Postein- und Postausgangsbuch führen. Posteingang erfasst Empfangstag (relevant für Fristbeginn nach BRAO Berufsregeln und § 188 ZPO § 122 AO § 37 SGB X) Absender Inhalt Akte Aktion (zur Akte / Antwort durch / Frist ans Fristenbuch). Pos... |
| `rechnungserstellung-rvg` | Erstellt Honorarrechnungen nach RVG (Anlage 1 VV RVG Anlage 2 RVG Gebührentabelle) oder nach Honorarvereinbarung mit Stundensatz. Pflichtangaben § 10 RVG (Aktenzeichen Mandant Gegenstand der Tätigkeit Verguetungstatbestaende Stundensaetz... |
| `sekretariats-tagesbrief` | Erzeugt morgens den Tagesbrief der Kanzlei mit allen Informationen die Anwalt und Sekretariat für den Tag brauchen — Fristen heute und in der naechsten Woche Vorfristen aus dem Fristenbuch eingegangene Post vom Vortag offene Mandantenrüc... |
| `timesheet-aktenzeitung` | Zeiterfassung pro Mandat (Aktenzeitung) — taegliche Erfassung mit Datum Anwalt Akte Tätigkeit Dauer in 6-Minuten-Bloecken Abrechenbarkeit (abrechenbar / pro bono / nicht abrechenbar) Honorarsatz und Notiz. Reports nach Mandat Anwalt Zeit... |
| `umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten` | Anwaltliche Strategie bei dem Vorwurf, ein gerichtliches Sachverständigengutachten sei unter Einsatz künstlicher Intelligenz erstellt worden. Höchstpersönliche Erstellungspflicht (§ 407a Abs. 1 ZPO), keine generelle KI-Kennzeichnungspfli... |
| `versand-vor-check` | Pflicht-Pre-Check vor jedem ausgehenden Versand — prüft Dokumentidentität (das richtige PDF? Stand vom richtigen Datum? Aktenzeichen passt?) Unterschrift (durch berechtigte Person? eigenhaendig oder qualifizierte elektronische Signatur?)... |
| `weihnachtskarten` | Pflegt den Weihnachtskartenversand der Kanzlei. Verteiler mit Empfaenger Anschrift E-Mail Versandart (postalisch / digital) Anredeform Bezug zur Kanzlei. Texte für formell-zurückhaltend warm und persoenlich. Druckliste für Postversand in... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
