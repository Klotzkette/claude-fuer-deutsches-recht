> Veröffentlichte Lesekopie des tatsächlich erzeugten Probelaufs. Lokale absolute Dateipfade wurden neutralisiert und Leerzeichen am Zeilenende bereinigt; fachlicher Text unverändert. Original- und Lesekopien-Hashes stehen in `../dateinachweis.json`.

# Werkzeug- und Quellenprotokoll

## 1. Auftrag und Eingabegrenzen

Bearbeitet wurde der fiktive Fristenfall Mara Fenchel mit Arbeitsstand 23.03.2026. Die tatsächliche Bearbeitung und Recherche fand am 07.10.2026 statt. Fallgrundlage waren ausschließlich die mitgeteilten Tatsachen. Urteil, Zustellungsurkunde, Kanzleibestand, Kalender und Zeitaufzeichnungen lagen nicht zur Einsicht vor. Die als belegt und wirksam vorgegebene Inlandszustellung vom 20.03.2026 wurde als Falltatsache übernommen.

Als einzige lokale Arbeitsanweisung wurde `[Repository]/ki-native-kanzlei/ki-native-kanzlei-schnellstart.md` mit `exec_command` und `cat` gelesen. Die Datei wurde nach einer Mitteilung über eine redaktionelle Nachänderung nochmals gelesen. Der erste Lesestand enthielt noch die längere Formulierung und BGH-Anker ohne die später ergänzten Entscheidungsformen/Randnummern. Der abschließend gelesene Stand enthielt unter anderem den Fristenanker „BGH, Beschl. v. 04.03.2026 – XII ZB 338/24, Rn.10–17“. Es wird nicht behauptet, zu Beginn bereits einen finalen Hash oder die endgültige Fassung gelesen zu haben. Ein initialer Hash wurde nicht erhoben. Im erneuten Lesen ergab sich für die hier ausgeführte Berechnung und Dokumentation keine Änderung.

Keine quality-Dateien, Testskripte, Bewertungsrubriken oder anderen Agentenergebnisse wurden gelesen. Das optionale `fristen.py` und die Fristen-Rechenhilfe wurden nicht benötigt und nicht gelesen oder ausgeführt. Es gab keine Pluginänderung, keinen Git-Aufruf und keinen Commit.

## 2. Tatsächlich verwendete Werkzeuge

1. **`functions.exec` mit `tools.exec_command`:** Lesen der oben bezeichneten Schnellstartdatei; Ausführung kurzer Python-Skripte für öffentliche Quellenabrufe, Zeichensatzkorrektur, Textausgabe und reine Datumsarithmetik; Erstellen des vorgesehenen Ergebnisordners; anschließende Kontrolle der beiden Ergebnisdateien. Öffentliche Quellen wurden mit `urllib.request` abgerufen. Amtliche PDF-Inhalte wurden ohne Zwischendatei über den Speicher an `pdftotext` übergeben.
2. **`tools.web__run`:** Suchanfragen zu §§ 339/222 ZPO, Berliner Feiertagen 2026 und BGH XII ZB 338/24; Direktabrufe der benötigten amtlichen Normen, Berliner Verwaltungsseiten und des BGH-/BGBl-Angebots. Die Suche lieferte neben amtlichen Treffern automatisch auch nichtamtliche Treffer. Diese wurden nicht als tragende Quelle verwendet und nicht gezielt als Volltexte geöffnet. Die rechtlichen Feststellungen beruhen auf den unten bezeichneten amtlichen Texten.
3. **`collaboration.send_message`:** Zwei interne Fortschrittsmeldungen an den auftraggebenden Hauptagenten mit Fristergebnis und Stand des Primärquellennachweises. Es wurde keine Nachricht an Mandantin, Gericht oder Dritte versandt.
4. **`tools.mcp__codex_app__load_workspace_dependencies`:** Einmalige Abfrage verfügbarer Laufzeitpfade nach fehlendem Python-Paket. Die mitgeteilte zusätzliche Laufzeit wurde nicht benötigt; die Textgewinnung erfolgte mit dem bereits vorhandenen `pdftotext`.
5. **`tools.apply_patch`:** Tatsächliche Erstellung von `ergebnis.md` und `werkzeuglog.md` ausschließlich im vorgegebenen Ordner `[Prüfordner]/probe-fristen/`.

Unabhängige, nicht voneinander abhängige Abrufe beziehungsweise Rechenschritte wurden teilweise mit `Promise.allSettled` gebündelt. Es wurde kein Browserkonto, beA, Kanzleikalender, Zeiterfassungs- oder Abrechnungssystem geöffnet oder verändert.

## 3. Tatsächlich gelesene tragende Quellen

Alle folgenden Quellen wurden am 07.10.2026 abgerufen. Der Text wurde gelesen; die Quellenliste behauptet keinen historischen Abruf zum fiktiven Arbeitsdatum.

| Quelle | Gelesener Inhalt und Verwendung |
|---|---|
| [§ 339 ZPO](https://www.gesetze-im-internet.de/zpo/__339.html) | Abs. 1: zwei Wochen, Notfrist, Zustellungsanknüpfung; Abs. 2–3: Abgrenzung der nicht vorliegenden Sonderzustellungen. Nach Web-Abrufproblemen direkt mit Python erfolgreich gelesen. |
| [§ 222 ZPO](https://www.gesetze-im-internet.de/zpo/__222.html) | Abs. 1–2: BGB-Berechnung und Verschiebung des Fristendes; Abs. 3 gelesen, hier keine Stundenfrist. |
| [§ 187 BGB](https://www.gesetze-im-internet.de/bgb/__187.html) | Abs. 1: Ereignistag nicht mitzählen; Abs. 2 als Abgrenzung gelesen. |
| [§ 188 BGB](https://www.gesetze-im-internet.de/bgb/__188.html) | Insbesondere Abs. 2: kalenderbezogene Wochenfrist. |
| [§ 224 ZPO](https://www.gesetze-im-internet.de/zpo/__224.html) | Abs. 1–2: Notfristeinordnung und begrenzte Verlängerbarkeit gesetzlicher Fristen. |
| [§ 340 ZPO](https://www.gesetze-im-internet.de/zpo/__340.html) | Abs. 1–3: Prozessgericht, notwendiger Inhalt, Verteidigung und Abgrenzung einer Begründungsverlängerung. |
| [§ 78 ZPO](https://www.gesetze-im-internet.de/zpo/__78.html) | Insbesondere Abs. 1: Anwaltszwang vor dem Landgericht. |
| [§ 130a ZPO](https://www.gesetze-im-internet.de/zpo/__130a.html) | Insbesondere Abs. 2–5: Eignung, Signatur, sicherer Übermittlungsweg, elektronischer Eingang und Bestätigung. |
| [§ 130d ZPO](https://www.gesetze-im-internet.de/zpo/__130d.html) | Elektronische Nutzungspflicht und Voraussetzungen der Ersatzeinreichung. |
| [Senatsverwaltung Berlin: Sonn- und Feiertagsrecht](https://www.berlin.de/sen/inneres/buerger-und-staat/verfassungs-und-verwaltungsrecht/artikel.1435639.php) | Amtliche Erklärung der Feiertagseigenschaft von Karfreitag und Ostermontag, mit Verweis auf § 1 FTG. Der dort verlinkte Volltext des FTG wurde aufgerufen, das Webwerkzeug lieferte jedoch nur die Datenbankhülle. Deshalb wird kein erfolgreicher Volltextabruf dieses Landesgesetzes behauptet. |
| [Hauptpersonalrat Berlin: Kalender 2026, Seite 1](https://www.berlin.de/hpr/wissenswertes/sitzungskalender/kalender-2026.pdf?ts=1763459016) | Amtliche Datumsbestätigung: Karfreitag 03.04.2026 und Ostermontag 06.04.2026. Textauszug des Webwerkzeugs gelesen. |
| [BGH, Beschluss vom 04.03.2026 – XII ZB 338/24](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/XII_ZS/2024/XII_ZB_338-24.pdf?__blob=publicationFile&v=1) | Amtliches PDF vollständig als Text gelesen, Schwerpunkt Rn. 10–16: Kontrolle sowie dauerhafte Erkennbarkeit gestrichener/geänderter Fristen auch in elektronischer Kalenderführung. Fundstelle über die amtliche BGH-Entscheidungssuche nach Aktenzeichen und Datum gefunden. |
| [ZPO-Gesamtfassung](https://www.gesetze-im-internet.de/zpo/BJNR005330950.html) | Insbesondere Standangaben gelesen: aktuelle Fassung enthält Änderungen aus Mai 2026. |
| [BGBl. 2026 I Nr. 152 vom 26.05.2026](https://www.recht.bund.de/bgbl/1/2026/152/regelungstext.pdf?__blob=publicationFile&v=1) | Art. 1–3 des Gesetzes zur weiteren Digitalisierung der Zwangsvollstreckung gelesen, um spätere ZPO-Änderungen gegenüber dem fiktiven Arbeitsdatum abzugrenzen. Die verwendeten ZPO-Normen werden durch diese Artikel nicht geändert. |

## 4. Abrufprobleme und tatsächliche Nachprüfungen

Das Webwerkzeug meldete mehrfach Timeouts oder interne Abruffehler bei einzelnen Normseiten. Das alte BGH-juris-Suchangebot war im Webwerkzeug nicht zugänglich und leitete beim direkten Abruf auf die neue amtliche BGH-Suche weiter. Deren Suchformular wurde gelesen; die Suche nach Aktenzeichen mit Datumsbegrenzung 04.03.2026 ergab das passende PDF. Webabrufe des BGH-PDFs und der BGBl-Seite scheiterten mit HTTP 403; direkte öffentliche Abrufe mit `urllib.request` funktionierten.

Ein erster direkter Python-Abruf der Gesetze-im-Internet-Seiten schlug bei UTF-8-Dekodierung fehl. Er wurde mit dem in den Seiten ausgewiesenen Zeichensatz ISO-8859-1 erfolgreich wiederholt. Ein Versuch, `pypdf` im System-Python zu importieren, scheiterte mit `ModuleNotFoundError`. Es wurde nichts nachinstalliert. `command -v pdftotext` bestätigte das vorhandene Werkzeug; damit wurden BGH- und BGBl-PDF anschließend erfolgreich im Speicher in Text umgewandelt.

Die zusätzliche Datumsrechnung mit Python `datetime` ergab: Zustellung Freitag, 20.03.2026; erster mitgerechneter Tag 21.03.2026; plus zwei Kalenderwochen 03.04.2026, Freitag; danach Samstag 04.04., Sonntag 05.04., Montag 06.04., Dienstag 07.04.2026. Auch die vorgeschlagenen Vorfristen 31.03.2026 und 02.04.2026 wurden als Dienstag beziehungsweise Donnerstag bestätigt. Python lieferte keine Feiertags- oder Rechtsprüfung; diese erfolgte anhand der amtlichen Quellen.

## 5. Ergebnis- und Ausführungsgrenzen

Erstellt wurden die beiden Markdown-Dateien in diesem Ordner. Markdown legt keine verlässliche Schriftart oder Punktgröße fest; eine Times-New-Roman-11-pt-Datei wurde nicht behauptet oder zusätzlich erzeugt.

Der Fristenvermerk enthält die berechnete Hauptfrist, vorgeschlagene interne Vorfristen, einen nachvollziehbaren Korrekturablauf und die spätere Eingangskontrolle. Zuständigkeiten sind als auszufüllende Rollen gekennzeichnet. Kein echter Kalender wurde eingesehen oder geändert; der Alttermin ist in Datum und ID unbekannt. Es wurden keine Erinnerungen oder Hintergrundaufgaben eingerichtet.

Arbeitszeit, ausführende Person, tatsächliches Leistungsdatum und Abrechenbarkeit sind offen. Der Zeitdatensatz im Vermerk ist ausdrücklich ungebuchter Entwurf. Keine bestätigte Zeitbuchung, Rechnungsfortschreibung oder Anpassung des 1.000-EUR-Deckels wurde vorgenommen. Die ungeklärte Netto-/Bruttobezugsgröße des Deckels wurde offengelegt. Antworten auf offene Rückfragen wurden nicht erfunden.

Es wurde kein Einspruch eingereicht, keine Nachricht an Außenstehende versandt und keine externe Handlung vorgenommen. Das Fristergebnis stellt keine Behauptung dar, der Einspruch sei bereits eingelegt oder die Frist bereits erledigt.
