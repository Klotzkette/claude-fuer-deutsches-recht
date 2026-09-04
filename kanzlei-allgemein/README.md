# Kanzlei-Allgemein-Plugin

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Kanzlei-Allgemein-Plugin (fusioniert mit Cowork): edles Kommandocenter Mandatsannahme/GwG Klage/Replik Vertrag Rechtsprechung Handelsregister beA-Journal Rechnung UStVA Fristenbuch Timesheet RVG Versand-Vor-Check Posteingang Mandantenakte Mahnwesen Tagesbrief Geburtstage Weihnachtskarten.

Dieses Plugin gehört zum Marketplace mit 235 Plugins. Für die Installation nimm das Einzel-ZIP. Ohne Installation genügt zum Einstieg einer der beiden eigenständigen Markdown-Prompts: Schnellstart für den Kernvorgang, Werkstatt für die ausführliche Bearbeitung. Die Prompts ersetzen nicht sämtliche Spezialskills und Hilfsdateien des Plugins.

## Welche Datei wofür? / Which file should I use?

| Bestandteil | Deutsch | English | Wo? / Where? |
| --- | --- | --- | --- |
| Plugin-ZIP | Installiert das vollständige Plugin mit Skills, Referenzen und Hilfsdateien. | Installs the complete plugin with its skills, references and supporting files. | [`kanzlei-allgemein.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-allgemein.zip) |
| Skills | Arbeitsabläufe für einzelne Aufgaben. Wähle bei einem klaren Auftrag den passenden Skill ausdrücklich; die automatische Auswahl ist nicht garantiert. Einzeldownloads enthalten nur die jeweilige Markdown-Datei. | Focused task workflows. Select a known skill explicitly; automatic selection is not guaranteed. An individual download contains only that Markdown file. | [Skill-Liste öffnen / Open skill list](../skills-index/kanzlei-allgemein.md) |
| Werkstatt-Prompt | Ausführliche eigenständige Markdown-Datei für komplexe oder mehrstufige Vorgänge. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Detailed standalone Markdown file for complex or multi-step matters. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/kanzlei-allgemein-werkstatt.md) |
| Schnellstart / Mini-Prompt | Kompakte eigenständige Markdown-Datei für einen schnellen ersten Arbeitsstand. Sie ist kein Skill und nicht im Plugin-ZIP enthalten. | Compact standalone Markdown file for a fast first work product. It is not a skill and is not included in the plugin ZIP. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/kanzlei-allgemein-schnellstart.md) |
| Testakten | Separate Übungsunterlagen in PDF- und Originalformaten; sie werden nicht mit dem Plugin installiert. | Separate practice files in PDF and original formats; they are not installed with the plugin. | [Testakten-Übersicht / Test-file index](../testakten/README.md) |

Links mit „MD herunterladen / Download MD“ starten einen Dateidownload. Navigationslinks zu README- und Übersichtsseiten bleiben dagegen als GitHub-Seiten geöffnet.

Links labelled “MD herunterladen / Download MD” start a file download. Navigation links to README and index pages remain normal GitHub pages.

Die Skill-Liste bildet den Quellbestand ab. Im installierten Paket werden umfangreiche Spezialserien teilweise über einen Fachrouter bei Bedarf geladen und erscheinen dann nicht als eigene auswählbare Skills. Beim manuellen Einsatz eines einzelnen Skills müssen zusätzlich benötigte Referenzen oder Werkzeuge verfügbar sein.

The skill index lists the source collection. In the installed package, some specialist series are accessed through a topic router rather than separate menu entries. A standalone skill may need additional reference files or tools. Choose one entry point, then add only what the matter requires.

Direktnavigation: [30-Sekunden-Start](#in-30-sekunden-starten) · [Startseite](../README.md) · [Plugin-Katalog](../README.md#was-ist-drin) · [Skill-Gesamtübersicht](../SKILLS.md) · [Skills dieses Plugins](../skills-index/kanzlei-allgemein.md) · [Plugin-Dateien](.) · [Download-Index](../ASSET_INDEX.md) · [Testakten](../testakten/README.md)

## In 30 Sekunden starten

| Ausgangslage | Schnellster Weg |
| --- | --- |
| Plugin installiert | Passenden Fachskill in der [alphabetisch sortierten Skill-Liste](../skills-index/kanzlei-allgemein.md) wählen und den untenstehenden Startsatz mit dem Arbeitsordner absenden. |
| Noch keine Installation | Den Schnellstart unten als Markdown herunterladen und mit den Unterlagen in einer freigegebenen Arbeitsoberfläche bereitstellen. |
| Umfangreicher oder mehrstufiger Vorgang | Die Werkstatt laden; sie führt tiefer durch Fachrouten, Gegenposition und Endprodukt. |

Startsatz für Kanzlei-Allgemein-Plugin:

> Erfasse zuerst Dateinamen und Metadaten im ausgewählten Ordner. Lies zunächst die für den Auftrag tragenden Unterlagen; ergänze die Lektüre gezielt bei offenen Belegfragen. Beginne mit folgendem Arbeitsschritt: Mandatsblatt: Beteiligte, Gegner, Gegenstand, Umfang, Vollmacht, Interessenkontrolle, Frist, Bearbeiter, Budget und nächster Schritt. Wenn bereits ein konkretes Dokument verlangt ist, beginne unmittelbar damit. Frage nur einmal gebündelt nach, falls der nächste fachliche Schritt sonst falsch wäre; arbeite im Übrigen mit sichtbar markierten Lücken weiter.

Bei einem Folgewunsch den bisherigen Aktenstand fortführen. Bereits festgestellte Tatsachen, Berechnungen und Quellen nicht erneut abfragen oder ohne Anlass neu aufbauen.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`kanzlei-allgemein.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-allgemein.zip) |
| Kompakter Prompt (Schnellstart) | Markdown | [`kanzlei-allgemein-schnellstart.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/kanzlei-allgemein-schnellstart.md) |
| Großer Prompt (Werkstatt) | Markdown | [`kanzlei-allgemein-werkstatt.md`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/kanzlei-allgemein-werkstatt.md) |
| Zugeordnete Testakten | PDF / ZIP | [4 zugeordnete Akten](#zugeordnete-testakten) mit Gesamt-PDF, Originaldateien und Einzel-PDFs |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 235 Plugins. Wer alle Plugins auf einmal will, nimmt [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip). Alle Einzeldateien stehen im [Download-Index](../ASSET_INDEX.md); Werkstatt und Schnellstart bleiben direkte Markdown-Downloads.

## Zugeordnete Testakten

Jede Akte ist getrennt als lesbares Gesamt-PDF, ZIP mit Originaldateien und ZIP mit einzelnen PDFs erreichbar.

| Akte | Gesamt-PDF | Originaldateien | Einzel-PDFs |
| --- | --- | --- | --- |
| [Akte Kanzlei-Allgemein-Plugin](../testakten/kanzlei-allgemein-alltag/README.md) | [Gesamt-PDF](../testakten/kanzlei-allgemein-alltag/gesamt-pdf/kanzlei-allgemein-alltag_gesamt.pdf) | [`testakte-kanzlei-allgemein-alltag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzlei-allgemein-alltag.zip) | [`testakte-kanzlei-allgemein-alltag-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzlei-allgemein-alltag-einzelpdfs.zip) |
| [Falkenried & Partner mbB — Managementakte Q2/2026](../testakten/kanzlei-management-falkenried-partnerkreis-q2-2026/README.md) | [Gesamt-PDF](../testakten/kanzlei-management-falkenried-partnerkreis-q2-2026/gesamt-pdf/kanzlei-management-falkenried-partnerkreis-q2-2026_gesamt.pdf) | [`testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip) | [`testakte-kanzlei-management-falkenried-partnerkreis-q2-2026-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzlei-management-falkenried-partnerkreis-q2-2026-einzelpdfs.zip) |
| [Sieglinger gegen Burgwald Energietechnik GmbH](../testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/README.md) | [Gesamt-PDF](../testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/gesamt-pdf/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger_gesamt.pdf) | [`testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip) | [`testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger-einzelpdfs.zip) |
| [Klingenhain Musikschule / DRV-Statusprüfung](../testakten/statusfeststellung-drv-musikschule-gf-freelancer-klingenhain/README.md) | [Gesamt-PDF](../testakten/statusfeststellung-drv-musikschule-gf-freelancer-klingenhain/gesamt-pdf/statusfeststellung-drv-musikschule-gf-freelancer-klingenhain_gesamt.pdf) | [`testakte-statusfeststellung-drv-musikschule-gf-freelancer-klingenhain.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-statusfeststellung-drv-musikschule-gf-freelancer-klingenhain.zip) | [`testakte-statusfeststellung-drv-musikschule-gf-freelancer-klingenhain-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-statusfeststellung-drv-musikschule-gf-freelancer-klingenhain-einzelpdfs.zip) |

[Alle Testakten und Fachzuordnungen](../testakten/README.md)
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlägigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Technischer Plugin-Name: `kanzlei-allgemein`.

Eigenständiges großes Kanzlei-Plugin für den gesamten Arbeitszyklus einer Kanzlei. **Mit v11.0.0 wurden die Skills des früheren `kanzlei-cowork`-Plugins vollständig in `kanzlei-allgemein` integriert** — Fristenbuch, Timesheet, RVG-Rechnung, Versand-Vor-Check, beA-Versand-Prüfung, Posteingang/Postausgang, Mandantenakte, Aktenbestandspflege, Honorar-Mahnwesen, Mandantenbriefe, Geburtstage, Weihnachtskarten und Sekretariats-Tagesbrief.

Das Plugin deckt: edles Cowork-Kommandocenter, Nachtblau/Silber/Orange-Look, Eingang, Intake, freundliche Menüführung, Mandatsannahme, Geldwäscheprüfung, KYC, PEP-Check, Kontoblatt, Schreib-Canvas, Klage- und Replik-Turbo, Vertragsentwurf, Rechtsprechungsrecherche, Handelsregisterabruf, Qualitätsgate, Konfliktcheck, Aktenanlage, Fristen, Action-Items, beA-Nachrichtenjournal, elektronisches Empfangsbekenntnis, Kanzleikalender, HR, Urlaub, Krankheit, Payroll-Vorbereitung, granulare Zeiterfassung mit Narrative, Mandatsvereinbarung, Honorar, GoBD-nahe Rechnungsvorbereitung, Geschäftskonto, offene Posten, Zahlungseingangs-Matching, E-Rechnung, XRechnung, ZUGFeRD, UStVA-Vorbereitung, Simulation, Output und Versandkontrolle.

Es ist **nicht** auf Großkanzleien beschränkt. Der Name meint den großen Kanzlei-Workflow: vom ersten Eingang bis zum versandfertigen Ergebnis.

## Installation

1. ZIP herunterladen.
2. Plugin-Umgebung öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `kanzlei-allgemein.zip` hochladen.
5. In einer neuen Unterhaltung mit einem typischen Auftrag starten, etwa: "Starte das volle Kanzlei-Workflow-Plugin für diese neue Nachricht."

Wichtig: Nicht das komplette Repository-ZIP hochladen. Das Upload-ZIP muss direkt `.claude-plugin/plugin.json`, `skills/` und `assets/` im ZIP-Root enthalten; `references/` ist optional, falls ein Plugin Referenzen mitliefert.

## Was das Plugin abbildet

| Phase | Skill | Zweck |
| --- | --- | --- |
| Kommandocenter | `kanzlei-allgemein-kommandocenter` | Ein-Satz-Schnellstart, Workflow-Routing, Freigabeampel, nächste beste Aktion und nur die nötigsten Rückfragen |
| Look and Feel | `kanzlei-allgemein-look-and-feel` | Cowork-taugliches Designsystem mit Statuskarten, Dashboard, Freigabeampel und Nachtblau/Silber/Orange-Tonwelt |
| Kanzleiprofil | `kanzlei-allgemein-kaltstart` | Kanzleikonventionen, Aktenzeichen, Kanäle, Fristenlogik, Honorarstandard, Versandregeln |
| Freundlicher Copilot | `kanzlei-allgemein-freundlicher-copilot` | Verzeihende Menüführung, kurze Hinweise, Nachziehmodus, Substanzcheck für junge Anwälte |
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
- Rechtsgebietsplugins wie `arbeitsrecht`, `vertragsrecht`, `fachanwalt-sozialrecht`, `steuerrecht-anwalt-und-berater`, `insolvenzrecht`.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Das Plugin bildet Arbeitsabläufe und Sicherheitsgatter ab. Es ersetzt keine Fristenkontrolle durch Berufsträger, keine Kanzleisoftware und keine Prüfung der Zulässigkeit konkreter Kommunikation im Einzelfall.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Ein Klick auf einen Skill lädt seine Markdown-Datei; die alphabetische Komplettliste bleibt darunter erhalten.

English: Skills are grouped by typical work phase. Clicking a skill downloads its Markdown file; the complete alphabetical list remains below.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/einstieg-routing/SKILL.md), [`hr-personal-kanzlei-intake`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/hr-personal-kanzlei-intake/SKILL.md), [`intake`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/intake/SKILL.md), [`kaltstart-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kaltstart-routing/SKILL.md), [`kaltstart-routing-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kaltstart-routing-triage/SKILL.md), [`kanzlei-cowork-kaltstart-interview`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzlei-cowork-kaltstart-interview/SKILL.md), [`look-feel-mandatsannahme-gwg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/look-feel-mandatsannahme-gwg/SKILL.md), [`mandatsannahme-gwg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mandatsannahme-gwg/SKILL.md), [`mandatsvereinbarung-postlauf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mandatsvereinbarung-postlauf/SKILL.md), [`posteingang-ausgang-sekretariats-tagesbrief`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/posteingang-ausgang-sekretariats-tagesbrief/SKILL.md), [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/workflow-kaltstart-und-routing/SKILL.md) |
| 2. Unterlagen, Sachverhalt und Quellen | [`akte-anlegen-und-aktenzeichen-zuordnen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/akte-anlegen-und-aktenzeichen-zuordnen/SKILL.md), [`aktenbestand-pflege-bea-versand`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/aktenbestand-pflege-bea-versand/SKILL.md), [`aktenzeichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/aktenzeichen/SKILL.md), [`kanzlei-rechtsprechungsrecherche-fristenbuch`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzlei-rechtsprechungsrecherche-fristenbuch/SKILL.md), [`mandantenakte-anlegen-mandantenbrief-vorlagen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mandantenakte-anlegen-mandantenbrief-vorlagen/SKILL.md), [`timesheet-aktenzeitung-umgang-ki`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/timesheet-aktenzeitung-umgang-ki/SKILL.md), [`umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten/SKILL.md) |
| 3. Prüfung, Anspruch und Subsumtion | [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/juristischer-argumentationskern/SKILL.md), [`versand-check-weihnachtskarten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/versand-check-weihnachtskarten/SKILL.md) |
| 4. Gestaltung, Strategie und Verhandlung | [`monitor-vertragsentwurf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/monitor-vertragsentwurf/SKILL.md), [`vertragsentwurf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/vertragsentwurf/SKILL.md) |
| 5. Verfahren, Behörde und Gericht | [`fristenbuch-fuehren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/fristenbuch-fuehren/SKILL.md), [`handelsregisterabruf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/handelsregisterabruf/SKILL.md) |
| 6. Ergebnis, Schreiben und Kommunikation | [`mandantenbrief-vorlagen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mandantenbrief-vorlagen/SKILL.md), [`output-versand`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/output-versand/SKILL.md), [`sekretariats-tagesbrief`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/sekretariats-tagesbrief/SKILL.md) |
| 7. Kontrolle, Qualität und Gegenprüfung | [`qualitaetsgate-hardening-kanzlei`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/qualitaetsgate-hardening-kanzlei/SKILL.md) |
| 8. Spezialmodule und Schnittstellen | [`abwesenheiten-urlaub`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/abwesenheiten-urlaub/SKILL.md), [`bea-journal`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/bea-journal/SKILL.md), [`bea-versand-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/bea-versand-pruefen/SKILL.md), [`buchhaltung-konten-kanzlei-erechnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/buchhaltung-konten-kanzlei-erechnung/SKILL.md), [`erechnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/erechnung/SKILL.md), [`freundlicher-copilot-kanzlei`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/freundlicher-copilot-kanzlei/SKILL.md), [`geburtstage-feiertage-abwesenheiten-urlaub`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/geburtstage-feiertage-abwesenheiten-urlaub/SKILL.md), [`integrationen-simulation-kanzlei`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/integrationen-simulation-kanzlei/SKILL.md), [`kanzlei-automationen-bea-journal`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzlei-automationen-bea-journal/SKILL.md), [`kanzleikalender`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzleikalender/SKILL.md), [`kanzleitag-simulation-kanzlei`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzleitag-simulation-kanzlei/SKILL.md), [`ki-arbeitsauftrag-mahnwesen-honorar`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/ki-arbeitsauftrag-mahnwesen-honorar/SKILL.md), [`kommandocenter`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kommandocenter/SKILL.md), [`lohn-sv-kanzlei-rechnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/lohn-sv-kanzlei-rechnung/SKILL.md), [`mahnwesen-honorar`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mahnwesen-honorar/SKILL.md), [`postlauf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/postlauf/SKILL.md), [`rechnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/rechnung/SKILL.md), [`rechnungserstellung-rvg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/rechnungserstellung-rvg/SKILL.md), ... plus 6 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Überblick

Automatisch generierte Komplett-Liste aller 52 Skills in diesem Plugin. Jeder Skillname und der Downloadlink laden den unveränderten Inhalt der zugehörigen `SKILL.md` als Markdown-Datei. Der eindeutige Dateiname enthält Plugin und Skill; Beschreibungen stammen aus dem jeweiligen `description`-Feld.

English: Complete list of all 52 skills in this plugin. Both links in each row download the unchanged `SKILL.md` content as a Markdown file with a unique plugin-and-skill filename.

| Skill | Beschreibung | Markdown-Download |
| --- | --- | --- |
| [`abwesenheiten-urlaub`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/abwesenheiten-urlaub/SKILL.md) | Für Abwesenheiten, Urlaub, Krankheit: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/abwesenheiten-urlaub/SKILL.md) |
| [`akte-anlegen-und-aktenzeichen-zuordnen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/akte-anlegen-und-aktenzeichen-zuordnen/SKILL.md) | Für Akte, Konfliktcheck und Mandatsanlage: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/akte-anlegen-und-aktenzeichen-zuordnen/SKILL.md) |
| [`aktenbestand-pflege-bea-versand`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/aktenbestand-pflege-bea-versand/SKILL.md) | Für Aktenbestandspflege: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/aktenbestand-pflege-bea-versand/SKILL.md) |
| [`aktenzeichen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/aktenzeichen/SKILL.md) | Für Aktenzeichen und Verknüpfungen: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/aktenzeichen/SKILL.md) |
| [`bea-journal`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/bea-journal/SKILL.md) | Für beA-Nachrichtenjournal und EB-Workflow: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/bea-journal/SKILL.md) |
| [`bea-versand-pruefen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/bea-versand-pruefen/SKILL.md) | Prüft einen konkreten elektronischen Gerichtsversand vor und nach dem Absenden: bestimmt Verfahrensordnung, Empfänger und Frist, trennt qualifizierte Signatur vom persönlichen sicheren Übermittlungsweg, kontrolliert Hauptdokument und Anh... | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/bea-versand-pruefen/SKILL.md) |
| [`buchhaltung-konten-kanzlei-erechnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/buchhaltung-konten-kanzlei-erechnung/SKILL.md) | Für Kanzlei-Buchhaltung, Konten und Zahlungsabgleich: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/buchhaltung-konten-kanzlei-erechnung/SKILL.md) |
| [`einstieg-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/einstieg-routing/SKILL.md) | Für Einstieg und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Kanzlei-Allgemein. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/einstieg-routing/SKILL.md) |
| [`erechnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/erechnung/SKILL.md) | Für E-Rechnung, XRechnung, ZUGFeRD und GoBD: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/erechnung/SKILL.md) |
| [`freundlicher-copilot-kanzlei`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/freundlicher-copilot-kanzlei/SKILL.md) | Für Freundlicher Kanzlei-Copilot: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Schnittstellenkarte mit Zuständigkeits- und Nachweisfragen. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/freundlicher-copilot-kanzlei/SKILL.md) |
| [`fristenbuch-fuehren`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/fristenbuch-fuehren/SKILL.md) | Für Zentrales Fristenbuch der Kanzlei: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Fristen- und Risikoampel. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/fristenbuch-fuehren/SKILL.md) |
| [`geburtstage-feiertage-abwesenheiten-urlaub`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/geburtstage-feiertage-abwesenheiten-urlaub/SKILL.md) | Für Geburtstage und Feiertage: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/geburtstage-feiertage-abwesenheiten-urlaub/SKILL.md) |
| [`handelsregisterabruf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/handelsregisterabruf/SKILL.md) | Für Handelsregisterabruf: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Einreichungsplan mit Form- und Nachweischeck. Fachgebiet: Kanzlei-Allgemein. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/handelsregisterabruf/SKILL.md) |
| [`hr-personal-kanzlei-intake`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/hr-personal-kanzlei-intake/SKILL.md) | Für HR und Personalverwaltung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/hr-personal-kanzlei-intake/SKILL.md) |
| [`intake`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/intake/SKILL.md) | Für Intake und Eingangstriage: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/intake/SKILL.md) |
| [`integrationen-simulation-kanzlei`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/integrationen-simulation-kanzlei/SKILL.md) | Für Integrationen und Simulationsmodus: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/integrationen-simulation-kanzlei/SKILL.md) |
| [`juristischer-argumentationskern`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/juristischer-argumentationskern/SKILL.md) | Schaltet sich ein, wenn in Kanzlei Allgemein ein juristisches Arbeitsprodukt tragfähig begründet werden muss; verbindet konkrete Aktenfundstellen mit Tatbestandsmerkmal, Beweislast, stärkster Gegenposition und Rechtsfolge. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/juristischer-argumentationskern/SKILL.md) |
| [`kaltstart-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kaltstart-routing/SKILL.md) | Für Kanzlei-Allgemein Kaltstart: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kaltstart-routing/SKILL.md) |
| [`kaltstart-routing-triage`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kaltstart-routing-triage/SKILL.md) | Für Kaltstart Routing Triage: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kaltstart-routing-triage/SKILL.md) |
| [`kanzlei-automationen-bea-journal`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzlei-automationen-bea-journal/SKILL.md) | Für Automationen und Routinen: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzlei-automationen-bea-journal/SKILL.md) |
| [`kanzlei-cowork-kaltstart-interview`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzlei-cowork-kaltstart-interview/SKILL.md) | Für /kanzlei-allgemein:kanzlei-cowork-kaltstart-interview: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzlei-cowork-kaltstart-interview/SKILL.md) |
| [`kanzlei-rechtsprechungsrecherche-fristenbuch`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzlei-rechtsprechungsrecherche-fristenbuch/SKILL.md) | Für Rechtsprechungsrecherche und Fundstellenablage: prüft Frist, Form, Zuständigkeit und Eilbedarf; Ergebnis: Fristen- und Risikoampel. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzlei-rechtsprechungsrecherche-fristenbuch/SKILL.md) |
| [`kanzleikalender`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzleikalender/SKILL.md) | Für Kanzleikalender und interne Abstimmung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzleikalender/SKILL.md) |
| [`kanzleitag-simulation-kanzlei`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzleitag-simulation-kanzlei/SKILL.md) | Für Kanzleitag-Simulation: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kanzleitag-simulation-kanzlei/SKILL.md) |
| [`ki-arbeitsauftrag-mahnwesen-honorar`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/ki-arbeitsauftrag-mahnwesen-honorar/SKILL.md) | Für digitale Werkzeuge-Arbeitsauftrag Briefing: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/ki-arbeitsauftrag-mahnwesen-honorar/SKILL.md) |
| [`kommandocenter`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kommandocenter/SKILL.md) | Für Kommandocenter: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Kanzlei-Allgemein. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/kommandocenter/SKILL.md) |
| [`lohn-sv-kanzlei-rechnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/lohn-sv-kanzlei-rechnung/SKILL.md) | Für Lohn, Sozialversicherung und Payroll: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/lohn-sv-kanzlei-rechnung/SKILL.md) |
| [`look-feel-mandatsannahme-gwg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/look-feel-mandatsannahme-gwg/SKILL.md) | Für Look and Feel: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/look-feel-mandatsannahme-gwg/SKILL.md) |
| [`mahnwesen-honorar`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mahnwesen-honorar/SKILL.md) | Für Mahnwesen für Kanzleihonorar: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mahnwesen-honorar/SKILL.md) |
| [`mandantenakte-anlegen-mandantenbrief-vorlagen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mandantenakte-anlegen-mandantenbrief-vorlagen/SKILL.md) | Für Mandantenakte anlegen: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mandantenakte-anlegen-mandantenbrief-vorlagen/SKILL.md) |
| [`mandantenbrief-vorlagen`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mandantenbrief-vorlagen/SKILL.md) | Für Mandantenbrief-Vorlagen: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mandantenbrief-vorlagen/SKILL.md) |
| [`mandatsannahme-gwg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mandatsannahme-gwg/SKILL.md) | Für Mandatsannahme und Geldwäscheprüfung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mandatsannahme-gwg/SKILL.md) |
| [`mandatsvereinbarung-postlauf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mandatsvereinbarung-postlauf/SKILL.md) | Für Mandatsvereinbarung und Honorarstart: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/mandatsvereinbarung-postlauf/SKILL.md) |
| [`monitor-vertragsentwurf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/monitor-vertragsentwurf/SKILL.md) | Für Fristen- und Action-Monitor: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/monitor-vertragsentwurf/SKILL.md) |
| [`output-versand`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/output-versand/SKILL.md) | Für Output und Versandsteuerung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/output-versand/SKILL.md) |
| [`posteingang-ausgang-sekretariats-tagesbrief`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/posteingang-ausgang-sekretariats-tagesbrief/SKILL.md) | Für Posteingang und Postausgang: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/posteingang-ausgang-sekretariats-tagesbrief/SKILL.md) |
| [`postlauf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/postlauf/SKILL.md) | Für Postlauf um 11 Uhr: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/postlauf/SKILL.md) |
| [`qualitaetsgate-hardening-kanzlei`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/qualitaetsgate-hardening-kanzlei/SKILL.md) | Für Qualitätsgate und Hardening: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Gegenprüfung mit Beweis- und Fristencheck. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/qualitaetsgate-hardening-kanzlei/SKILL.md) |
| [`rechnung`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/rechnung/SKILL.md) | Für Rechnungsvorbereitung und Abschluss: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/rechnung/SKILL.md) |
| [`rechnungserstellung-rvg`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/rechnungserstellung-rvg/SKILL.md) | Für Rechnungserstellung Honorar (RVG oder Vereinbarung): ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/rechnungserstellung-rvg/SKILL.md) |
| [`schreibcanvas`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/schreibcanvas/SKILL.md) | Für Schreib-Canvas: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/schreibcanvas/SKILL.md) |
| [`sekretariats-tagesbrief`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/sekretariats-tagesbrief/SKILL.md) | Für Sekretariats-Tagesbrief: erstellt Entwurf mit Antrag, Beweis und Anlagen; Ergebnis: Schriftsatz mit Begründungs- und Anlagenlogik. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/sekretariats-tagesbrief/SKILL.md) |
| [`timesheet-aktenzeitung-umgang-ki`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/timesheet-aktenzeitung-umgang-ki/SKILL.md) | Für Timesheet und Aktenzeitung: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/timesheet-aktenzeitung-umgang-ki/SKILL.md) |
| [`turbo-zeitnarrative`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/turbo-zeitnarrative/SKILL.md) | Für Schriftsatz-Turbo: Klage, Replik, Antrag: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/turbo-zeitnarrative/SKILL.md) |
| [`umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten/SKILL.md) | Für Umgang mit dem digitale Werkzeuge-Vorwurf bei Sachverständigengutachten: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/umgang-mit-ki-vorwurf-bei-sachverstaendigengutachten/SKILL.md) |
| [`ustva-buchhaltung-simulation`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/ustva-buchhaltung-simulation/SKILL.md) | Für UStVA, Eingangsrechnungen und Kanzlei-Buchhaltung: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/ustva-buchhaltung-simulation/SKILL.md) |
| [`ustva-simulation`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/ustva-simulation/SKILL.md) | Für UStVA- und ELSTER-Simulation: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/ustva-simulation/SKILL.md) |
| [`versand-check-weihnachtskarten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/versand-check-weihnachtskarten/SKILL.md) | Für Versand-Vor-Check (Pflicht vor jedem Versand): ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/versand-check-weihnachtskarten/SKILL.md) |
| [`vertragsentwurf`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/vertragsentwurf/SKILL.md) | Für Vertragsentwurf und Vertrags-Canvas: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/vertragsentwurf/SKILL.md) |
| [`weihnachtskarten`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/weihnachtskarten/SKILL.md) | Für Weihnachtskarten Mandantenpflege: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/weihnachtskarten/SKILL.md) |
| [`workflow-kaltstart-und-routing`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/workflow-kaltstart-und-routing/SKILL.md) | Für Kaltstart und Routing: routet Rolle, Frist, Unterlagen und Fachschritt; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. Fachgebiet: Kanzlei-Allgemein. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/workflow-kaltstart-und-routing/SKILL.md) |
| [`zeitnarrative`](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/zeitnarrative/SKILL.md) | Für Zeitnarrative und Timesheet: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt. | [MD herunterladen / Download MD](https://klotzkette.github.io/claude-fuer-deutsches-recht/download.html?path=kanzlei-allgemein/skills/zeitnarrative/SKILL.md) |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
