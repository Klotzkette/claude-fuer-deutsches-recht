# Fristen: Rechtsprofil und überprüfbare Kalenderrechnung

## 1. Aufgabe und Grenze

`../scripts/fristen.py` rechnet aus einem **ausdrücklich vorgegebenen und fachlich geprüften Rechtsprofil**. Das Programm entscheidet nicht, welches Rechtsmittel eröffnet ist, ob eine Zustellung wirksam war oder welche Fristnorm gilt. Diese Fragen bearbeitet der Skill `fristen-berechnen-ueberwachen` anhand der Originalbelege. Das Ergebnis ist ein Rechenvermerk; es bewirkt weder einen Kalendereintrag noch eine Erinnerung.

Die Rechenhilfe unterstützt Ereignis- und Anfangsfristen in Tagen, Wochen, Monaten und Jahren, ausdrücklich definierte Werktage, feste Enddaten sowie zwei ausdrücklich gewählte Stundenregeln. Hemmung, Ablaufhemmung, Neubeginn, Höchstfristen, gerichtliche Verlängerung und Zugangsfiktionen müssen gesondert rechtlich modelliert werden; entsprechende freie Zusatzfelder werden abgewiesen. Eine halbe Monatsfrist ist ebenfalls kein unterstütztes `unit` und darf nicht als 0,5 Monate eingegeben werden. § 189 BGB und gegebenenfalls eine Sondernorm sind vorgelagert zu prüfen.

## 2. Berechnung vorbereiten

Kläre zuerst Normfassung und konkreten Tatbestand, auslösendes Ereignis samt Nachweis, Beginn nach Ereignis oder Tagesanfang, Einheit und Länge, erlaubte Verschiebung des Endes sowie den maßgeblichen Kalenderort. Der Kanzleisitz ist nicht automatisch der nach § 193 BGB maßgebliche Leistungsort oder der für ein Verfahrensrecht entscheidende Ort.

`calendar.holidays` ist eine vollständige, vom Bearbeiter überprüfte Liste der für den gewählten Ort geltenden gesetzlichen Feiertage **im angegebenen Geltungszeitraum**. Der Helfer erzeugt keine Feiertage selbst. Er verlangt Quelle, Ort, Zeitraum und die ausdrückliche Kennzeichnung `verified: true`; diese Eingabe ist eine Dokumentation der vorgelagerten Prüfung, keine maschinelle Bestätigung ihrer Wahrheit. Lokale Feiertage und einmalige Änderungen sind einzubeziehen. Fehlt die Abdeckung des Zielzeitraums, bricht die Rechnung ab. Ein leeres Array bedeutet eine ausdrücklich geprüfte Abwesenheit von Feiertagen im konkreten Zeitraum, nicht „noch nicht recherchiert“.

Die beigefügte Beispielkonfiguration gilt für Berlin und das Kalenderjahr 2026. Feiertagsbestand: [Senatsverwaltung für Inneres](https://www.berlin.de/sen/inneres/buerger-und-staat/verfassungs-und-verwaltungsrecht/artikel.1435639.php); Datumsabgleich: [amtliche Jahresübersicht 2026 des Bezirksamts Lichtenberg](https://www.berlin.de/ba-lichtenberg/politik-und-verwaltung/bezirksverordnetenversammlung/wissenswertes/ds-1470-ix_anlage-jahresuebersicht-sitzungstermine-2026.pdf?ts=1734532540). Das Beispiel ist eine isolierte Rechendemonstration ohne echtes Mandat. Für andere Orte und Jahre nicht einfach übernehmen.

## 3. Ausführen

Python 3.10 oder neuer und eine verfügbare IANA-Zeitzonendatenbank genügen. Im Pluginordner:

```sh
python3 scripts/fristen.py --data assets/fristen-beispiel-berlin-2026.json --out /tmp/fristen-demo-neu
```

Das Ausgabeziel darf noch nicht bestehen. Es entstehen `fristenvermerk.json` und `fristenvermerk.md`. Ohne `--out` wird nur JSON auf der Konsole ausgegeben. Bestehende Berechnungen werden nicht überschrieben. Eine Korrektur erhält einen neuen Zielordner; im führenden Fristenregister werden alte und neue Fassung, Grund, Prüfer und tatsächliche Kalenderänderung verbunden. Der SHA-256-Wert identifiziert die kanonisch serialisierte Eingabe, nicht den Dateistand irgendeines Originalbelegs.

## 4. Felder und Rechtswahl

`schema_version` ist die ganze Zahl 1. `matter_id` benennt den zugehörigen Vorgang. Im `profile` stehen `norm`, `rule_source` und `trigger_source` als konkrete Textangaben sowie `rule_verified: true`. Zulässig sind folgende Modi:

| Modus | Erforderliche zusätzliche Felder | Berechnung |
| --- | --- | --- |
| `event` | `trigger`, `amount`, `unit` | Auslösertag ausgeschlossen; bei Wochen/Monaten/Jahren kalenderbezogener Endtag. |
| `start` | `trigger`, `amount`, `unit` | Anfangstag eingeschlossen; § 188 Absatz 2 und fehlender Endtag nach Absatz 3 getrennt. |
| `fixed` | `trigger` | Vorgabe ist bereits das feste Enddatum; keine neue Fristlänge. |
| `hours` | `trigger`, `amount`, `zone`, `hour_rule` | Tatsächlicher Zeitpunkt mit explizitem Offset; gewählte Stundenregel. |

In `event` und `start` ist `unit` eines von `days`, `weeks`, `months`, `years`, `working_days`. `amount` ist positiv und ganzzahlig. Bei `working_days` sind zusätzlich `weekdays` (0 Montag bis 6 Sonntag) und `working_day_definition` erforderlich. „Werktag“ wird nicht ungeprüft mit Montag bis Freitag gleichgesetzt. Gesetzliche Feiertage aus dem vorgegebenen Kalender werden beim Werktagszählen ausgelassen. Eine abweichende vertragliche Definition, die Feiertage einschließt, muss gesondert gerechnet werden.

Alle Modi benötigen `end_adjustment` und `adjustment_basis`. `none` bedeutet die ausdrücklich begründete Nichtverschiebung. `next_working_day` bedeutet Verschiebung eines Endes am Samstag, Sonntag oder aufgeführten Feiertag auf den folgenden nicht ausgeschlossenen Tag. Die Zulässigkeit dieser Verschiebung ergibt sich **nicht** aus dem Namen des Programms. Sie muss sich aus der konkreten Verfahrens- oder Sachnorm ergeben.

Für `hours` muss `end_adjustment: none` gesetzt sein. `hour_rule: elapsed` zählt reale verstrichene Stunden über UTC. `exclude_nonworking_days` zählt Zeitanteile von Samstagen, Sonntagen und gesetzlichen Feiertagen nicht mit; dies bildet bei entsprechend gewählter Rechtsgrundlage § 222 Absatz 3 ZPO ab. Es sind keine „Bürostunden“ von 9 bis 17 Uhr. Ein Stundenende exakt um 00:00 bezeichnet die Grenze am Ende des vorherigen gezählten Tages. Eine vermeintlich feste Frist um 12:00 Uhr ist nicht als `fixed` ohne Uhrzeit einzugeben; `fixed` unterstützt nur das Tagesende. Für eine solche Vorgabe muss ein eigener, ungeänderter Fristvermerk außerhalb der Rechenhilfe erstellt werden.

## 5. Kontrollbeispiele

Bei einem isolierten Ereignisprofil mit Auslöser am 31. Januar 2026 und einem Monat ist das unverschobene Ende der 28. Februar 2026. Ohne begründete Endverschiebung bleibt es dabei; nur bei anwendbarer Wochenendregel ergibt sich Montag, 2. März 2026. Bei einer Anfangsfrist ab 31. Januar mit einem Monat führt der fehlende maßgebliche Tag im Februar ebenfalls zum Monatsletzten; es wird nicht mechanisch erst auf den 28. Februar gekürzt und dann ein weiterer Tag abgezogen.

Zwei Wochen ab einem Ereignis am 20. März 2026 enden zunächst am Karfreitag, 3. April 2026. Im geprüften Berliner Kalender führt die ausdrücklich anwendbare Endverschiebung über Karfreitag, Samstag, Sonntag und Ostermontag zum 7. April. Das Programm zeigt die ausgeschlossenen Tage einzeln. Eine materiellrechtliche Frist ohne diese Verschiebungsregel bleibt im anderen Profil am 3. April.

24 reale Stunden ab 28. März 2026, 12:00 Uhr MEZ enden am 29. März, 13:00 Uhr MESZ. Diese Rechnung belegt keine Anwendung der Realstundenregel auf jede gesetzliche Stundenfrist. Ein lokaler Zeitstempel in der nicht existierenden Stunde des Sommerzeitwechsels oder mit widersprechendem Offset wird abgewiesen. Für die doppelte Stunde im Herbst entscheidet der ausdrücklich eingegebene Offset über den tatsächlichen Zeitpunkt.

## 6. Vor Kalenderübernahme

Kontrolliere Rechtswahl, Zugang/Zustellung, Ereignisart, maßgeblichen Ort und vollständigen Feiertagsbestand unabhängig. Prüfe anschließend vorgeschriebene Form, Empfänger und zulässigen Übermittlungsweg. Trage eine angemessene Vorfrist und die verantwortliche Vertretung anhand der Kanzleiorganisation ein. Erst ein tatsächlich ausgeführter und kontrollierter Kalendereintrag darf als gespeichert bezeichnet werden. Belege die Erledigung anhand des erforderlichen Empfangs- oder Eingangsbelegs; die Existenz einer PDF-Datei oder ein Signaturprotokoll genügt dafür nicht.

Quellen: [§ 187 BGB](https://www.gesetze-im-internet.de/bgb/__187.html), [§ 188 BGB](https://www.gesetze-im-internet.de/bgb/__188.html), [§ 193 BGB](https://www.gesetze-im-internet.de/bgb/__193.html), [§ 222 ZPO](https://www.gesetze-im-internet.de/zpo/__222.html). Prüfstand 7. Oktober 2026; spätere Rechts- und Kalenderänderungen vor Verwendung prüfen.
