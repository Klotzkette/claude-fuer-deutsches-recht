# Freigabe native Fallakten – 30. September 2026

Die beiden Originalbestände sind fertig und für die zentrale Erstellung von Gesamt-PDF und ZIP-Paketen freigegeben. Es bestehen keine offenen Fehler der hier geprüften Originaldateien.

## Ablage und Bestand

- `testakten/sozialversicherung-musikakademie-prenzlauer-berg`: Mara Noémi Zwirn, Musikakademie am Mauerpark gGmbH, Geschäftsführer Kunibert Schnurr. 27 Originale: 5 DOCX, 9 PDF, 8 EML, 3 TXT, 1 CSV, 1 XLSX.
- `testakten/sozialversicherung-programmierer-leipzig`: Jonas „Juno“ Kern-Knörz, Nordlicht Projektvermittlung GmbH, Elster Logistiksysteme GmbH; interne Kollegin Aylin Bao Wendel. Gleicher Formatmix, 27 Originale.
- Builder: `scripts/build-sv-lehre-programmierung-akten.py` und `scripts/build-sv-lehre-programmierung-tabellen.mjs`.
- README und der durch Root ergänzte `rubric.yaml` sind redaktionelle Begleitdateien und keine Originalaktenstücke. Die README enthält den unveränderten zweisprachigen Hinweis unmittelbar vor der Downloadtabelle und den Marker `<!-- reserved-example-contacts -->`.

## Inhaltliche Konsistenz

Musik: Vertrag 2022, Honoraranpassung 2024, spätere Unterrichtsorganisation, tatsächliche Vertretung 2023 und abgelehnte Vertretung 2025. Die für Januar 2025 zunächst berechneten 2.592 Euro werden durch eine gesonderte korrigierte Rechnung über 2.448 Euro ersetzt; die 144 Euro Differenz entsprechen vier Einheiten. Der Kontobeleg weist die tatsächliche Zahlung aus. 27,80 Euro Notenerstattung bleiben außerhalb des Honorars; 72 Euro Probespiel gehören zu Februar. Akademiehonorar 2025: 25.200 Euro. Weitere Einnahmen: 8.460 Euro; die noch ausstehende Aufteilung einzelner Workshops/Auftritte wird im Originalblatt kenntlich gemacht. Formular, Portalimport und zeitnahe E-Mails widersprechen sich nachvollziehbar beim Zugang beziehungsweise der Freigabe der Zustimmung. KSK-Nachfrage und persönliche Vorsorgeangaben sind als eigene Vorgänge vorhanden.

Programmierer: Rahmenvertrag und eigener Migrationsabruf 2024, Übergabe, danach veränderte Betriebsbegleitung. Vermittlervertrag, tatsächliche Aufgabenverteilung beim Endkunden, Gerätezugang, Vertretungsversuch, Tickets und Chatnachrichten ermöglichen getrennte Feststellungen. Die Arbeitgeberprüfung wird am 24. August 2026 allgemein angekündigt; am 27. August wird der Einsatz namentlich angefordert. Svens anders verstandene Auskunft vom 2. September liegt als E-Mail vor; Jonas stellt am 4. September den Antrag. Erst spätere Weiterleitung erschließt ihm das frühere Schreiben. Keine Entscheidung oder rechtliche Lösung wird vorweggenommen. 2025: 1.512 Stunden × 105 Euro = 158.760 Euro netto bei Nordlicht, 18.400 Euro netto bei Linde, zusammen 177.160 Euro netto. Rechnungs- und Zahlungstermine sind getrennt; Bankdaten fallen auf plausible Werktage.

## Durchgeführte Prüfung

- Alle zehn DOCX mit dem kanonischen `documents/.../render_docx.py` gerendert, ausschließlich mit dem gebündelten Python und dessen gebündeltem LibreOffice. Keine Desktop-LibreOffice-Instanz verwendet. Finale zwölf DOCX-Seiten vollständig visuell angesehen.
- Alle 18 ursprünglichen PDFs mit Poppler gerendert; sämtliche 18 Seiten vollständig visuell angesehen. Texte durchsuchbar, A4, keine Überläufe oder abgeschnittenen Inhalte.
- Zwei XLSX mit dem öffentlichen `@oai/artifact-tool` erzeugt; vier Arbeitsblätter vollständig gerendert und visuell angesehen. Rechenwerte unabhängig mit JavaScript gerechnet, Excel-Formeln nach Änderungen neu berechnet, Fehlerzellen gesucht. Exportierte Formel-Caches anschließend mit `openpyxl` ausschließlich lesend geprüft.
- Musikblatt: Unterrichtseingabe B5 um eine Einheit erhöht. Jahreshonorar und Querbezug steigen um 36 Euro; Zahlungsdifferenz wird −36 Euro. Eingabe zurückgesetzt, Differenz wieder null.
- Programmiererblatt: B5 von 128 auf 129 Stunden erhöht. Netto steigt um 105 Euro, Umsatzsteuer um 19,95 Euro, Jahresquerbezug um 105 Euro. Eingabe zurückgesetzt; Januarbrutto erneut 15.993,60 Euro.
- Alle 54 Originale lesbar; lokale Qualitätsfunktionen auf Sprache, Metamarker, Mindestumfang der formalen Texte, A4 und Kontaktmarker angewendet. Ergebnis: keine Fehler.
- MIME/UTF-8 und E-Mail-Header geprüft. Sämtliche eingebetteten Anhänge stimmen bytegenau mit den mitgelieferten Original-PDFs überein.
- Die Word-Standardvorlage wurde explizit von der geerbten blauen Titellinie und Theme-Font-Verweisen bereinigt; finale Word-Texte verwenden Times New Roman. Ein allein auf Seite 2 stehender Abschluss wurde bereinigt und erneut gerendert.

Prüfnachweise: `final-native-audit.json` enthält Dateihashes, Umfang und die Liste aller 34 endgültig geprüften Seiten-/Blattbilder. `tabellen-pruefung.json` enthält Eingabeänderungstests, Formeln und Zellwerte. Renderbilder und kanonische DOCX-PDFs liegen in den Unterordnern dieses QA-Verzeichnisses. Frühere Smoke-/Zwischenrender in `programmer-01` und `juno-final` sind nicht maßgeblich; maßgeblich sind die im Audit gelisteten `sozialversicherung-...__...`-Pfade.

## Portabilität und zentrale Restarbeit

Der JS-Builder verwendet den normalen Package-Import `@oai/artifact-tool` und erhält den Repositorypfad als Argument. Es gibt keinen hart kodierten Benutzerpfad. Für die lokale Ausführung wurde eine Kopie in einem temporären Verzeichnis mit einem Symlink auf die gebündelten Node-Pakete verwendet. Der Python-Builder löst seinen Repositorypfad relativ zu sich selbst auf. PDF-Schriften lassen sich über `SV_TIMES_FONT` und `SV_TIMES_BOLD_FONT` setzen; zusätzlich existieren macOS-Times- sowie Linux-Times-/Liberation-Serif-Fallbacks.

Gesamt-PDF, Einzel-PDF-ZIP, Original-ZIP, deren finale Seitenkontrolle sowie globale README-/Release-Validatoren übernimmt wie vereinbart Root. Diese Auslieferungen wurden von diesem Subagenten noch nicht gebaut. Die Freigabe bezieht sich auf die Originale und ihre oben nachgewiesenen Renderings, nicht auf noch nicht erzeugte zusammengesetzte Pakete.
