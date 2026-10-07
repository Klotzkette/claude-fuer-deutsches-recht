# KI-native Kanzlei: Prüfung der Vertiefung

Stand: 7. Oktober 2026. Komponentenfassung `445.33.4`. [Plugin und Downloads](../../ki-native-kanzlei/README.md).

## 1. Gegenstand und Umfang

Die bisherige Kanzleikomponente wurde auf Wunsch in **KI-native Kanzlei** umbenannt. AI-native und SI-native erscheinen im aktuellen Produktnamen nur als eingeklammerter Scherz. Historische Fallkennzeichen und alte Veröffentlichungen bleiben erhalten. 16 bisherige Skills wurden vertieft, zwei eigenständige Skills für Fristen und Anwaltsberufsrecht ergänzt. Es gibt insgesamt 18 Skills einschließlich Hauptskill, getrennte Werkstatt-, Mini- und Hauptproblem-Prompts sowie die vorhandenen 24 Fachanwaltsakten.

Die 18 Skills haben im tatsächlichen A4-Satz mit Times New Roman 11 pt jeweils 10–13 Seiten, zusammen **194 Seiten**. Der Fristenskill hat 13 Seiten, Berufsrecht 11, der Hauptskill 12. Das ist kein aus einer Wortzahl errechneter Seitenwert. [Umfang, Layout und Datei-Hashes](umfang.json) und [Buildprotokoll](logs/pdf-build.log) dokumentieren die erzeugten Lesefassungen. Die Werkstatt umfasst 11.163 Wörter; Mini und Hauptproblem bleiben mit 7.497 beziehungsweise 7.488 UTF-8-Bytes innerhalb der konservativen 7.500-Byte-Grenze. Die jeweiligen MD-/TXT-Paare sind byteidentisch.

## 2. Rechtsquellen

Die Fachprüfung wurde nach Arbeitsbereichen aufgeteilt. Die folgenden Berichte benennen Entscheidungen, tatsächlich gelesene Fundstellen, Anwendungsgrenzen und nicht erfolgreiche Abrufwege:

1. [Fristen, Berufsrecht, Annahme, Geldwäsche und Abschluss](beruf-fristen-quellen.md).
2. [Vergütung, Zeiten, Abrechnung, Buchhaltung und Verträge](verguetung-vertraege-quellen.md).
3. [Hauptworkflow, Recherche, Schriftsatz, Kommunikation und beA](sacharbeit-workflow-quellen.md).

Zu den neuen Ankern gehören BGH, Beschluss vom 04.03.2026 – XII ZB 338/24 zur Nachvollziehbarkeit von Fristenänderungen und BGH, Urteil vom 15.01.2026 – IX ZR 188/24 zu auftragsbezogenen Handakten bei einer konkreten Vertragsübernahme. Die BGH-Urteile vom 19.02.2026 – IX ZR 226/22 und IX ZR 227/22 werden bei Vergütung und Zeitaufstellungen mit ihrem konkreten Aussagegehalt verwendet. Die Zulassung einer Revision im BFH-Beschluss vom 26.02.2026 – V B 11/25 wird ausdrücklich nicht als abgeschlossene Sachentscheidung ausgegeben.

Die Quellenberichte unterscheiden vollständige Urteilslektüre, gezielt geprüfte Randnummern und amtliche Leitsätze. Ein dokumentierter früherer Primärquellenabgleich wird bei erneut gesperrtem Abruf nicht als erfolgreicher neuer Volltextabruf bezeichnet. Fachrechtliche Fallentwürfe verlangen weiterhin die Prüfung ihrer eigenen aktuellen Rechtsgrundlagen. Die Prüfung ist keine Zusage vollständiger Erfassung jeder denkbaren Entscheidung oder künftigen Rechtsänderung.

## 3. Tatsächlich ausgeführte technische Prüfungen

| Prüfung | Nachweis und Ergebnis |
| --- | --- |
| Fristen-Rechenhilfe | [18 Testmethoden](logs/fristen-tests.log) bestanden: Monatsenden, Schaltjahre, gesetzlich gewählte Verschiebung, Feiertagsabdeckung, Stundenfristen mit Zeitumstellung, Arbeitstagsdefinition, Eingabevalidierung, unveränderte Eingaben und Überschreibschutz. |
| Mandatsjournal | [19 Tests](logs/journal-tests.log) bestanden; Honorarphasen, tatsächliche Zeiten, Änderungen und Rechnungsentwurf. |
| Dokument-/Rechnungsexporte | [16 Tests](logs/export-tests.log) bestanden; keine Behauptung eines neuen produktiven Rechnungsversands oder einer erneuten externen KoSIT-Prüfung. |
| Quellenstruktur | [Strukturbericht](struktur-pruefung.json): 18 Skills mit den sechs Hauptabschnitten, Frontmatter, lokalen Links, Promptpaaren, Versionsdaten, Profil- und Quelldatei-Hashes. |
| Pakete und Originalerhaltung | [Paketbericht](paket-pruefung.json): beide Installationspakete quellidentisch, 18 Skills, drei Manifeste, Standalone-Prompts getrennt; sämtliche 240 Originale mit den Git-Objekten des unveränderten Tags `si-native-kanzlei-v445.33.3` verglichen. |
| Navigation | [Begrenzter Navigationslauf](navigation.json) über Plugin, Akten und zugehörige Einstiegsseiten; kein behaupteter erneuter Vollscan des gesamten Repositories. |

Die Claude-Pluginvalidierung und die lokale Codex-Manifestvalidierung waren erfolgreich. Die Fristenhilfe berechnet nur ein **zuvor rechtlich gewähltes und bestätigtes Profil** mit bereitgestelltem Feiertagskalender. Sie bestimmt weder selbständig den anwendbaren Fristentatbestand noch streitige Zustellung, Hemmung oder Neubeginn; sie schreibt keinen echten Kalender und betreibt keine dauernde Fristenüberwachung.

## 4. PDF-Prüfung

Der Builder vergleicht den geordneten Text aller Absätze und Tabellenzellen mit den erzeugten PDFs. Alle 194 Einzel-PDF-Seiten wurden zusätzlich auf innerhalb der Seite liegende Textgeometrie geprüft; [Geometriebericht](pdf-geometrie.json). Sein Feld `visual_review: pending` bezeichnet den Stand vor der anschließenden unabhängigen Sichtprüfung und ist kein widersprechendes aktuelles Urteil.

Eine zweite Instanz hat zunächst 54 tatsächliche Seitenbilder einzeln angesehen. Nach Korrektur eines unschön umgebrochenen Tabellenkopfs wurde der Hauptskill vollständig neu angesehen. Für die endgültige Fassung umfasst die Sichtkontrolle **63 Einzel-PDF-Seiten** (51 unveränderte Stichprobenseiten der übrigen 17 Skills und alle zwölf Hauptskillseiten) sowie **fünf Seiten des zusammengesetzten Handbuchs**, einschließlich seiner Tabelle. Keine Überlagerungen, abgeschnittenen Zeichen oder Ersatzkästchen sind offen. Ein kosmetischer Hinweis betrifft die nur zweizeilige Schlussseite des Honorarskills. [Sichtprüfbericht](pdf-sichtpruefung.md) und [Seiten-/Bildnachweise](pdf-sichtpruefung.json).

Die 63 Einzel-PDF-Seiten sind keine vollständige Sichtprüfung aller 194 Seiten. Die einzige Skill-Tabelle wurde auf beiden Seiten vollständig im Hauptskill und im zusammengesetzten Handbuch angesehen. Das zusammengesetzte Handbuch enthält die geprüften Einzel-PDF-Seiten in derselben Reihenfolge; seine Seitenzahl und Dateiidentität werden im Pakettest geprüft. Zusätzlich stimmen [alle 194 Seitentexte und Seitenformate](handbuch-zusammenfuegung.json) mit den jeweiligen Einzel-PDFs überein.

## 5. Zwei unabhängige Modell-Probeläufe

Zwei Instanzen ohne vorausgehende Unterhaltung erhielten jeweils den konkreten Auftrag und nur den zu prüfenden Mini-Prompt beziehungsweise Berufsrechtsskill sowie dessen Referenzen. Sie sollten die Fälle tatsächlich bearbeiten, durften Rechtsquellen und Werkzeuge benutzen und erhielten keine Bewertungskriterien, fremden Ergebnisse oder QA-Dateien. Die Hauptinstanz hat anschließend die vollständig vorliegenden Ergebnisse und Werkzeugprotokolle beurteilt.

### 5.1. Frist nach Versäumnisurteil in Berlin

Auftrag: Fiktiver Arbeitsstand 23.03.2026, wirksame Inlandszustellung am 20.03.2026, bisher falscher Fristeintrag 03.04.2026; ausführbarer Fristenvermerk, keine Einreichung. Honorar 200 Euro netto pro Stunde bei 1.000 Euro Deckel, tatsächliche Zeit unbekannt. Geprüft wurde der Mini-Prompt. Nach dem Lauf wurde ausschließlich ein überflüssiges Leerzeichen am Zeilenende entfernt; der Inhalt blieb gleich.

[Ergebnis](probelaeufe/fristen/ergebnis.md) · [Werkzeuge und Quellen](probelaeufe/fristen/werkzeuglog.md).

Alle vier für diesen Fall ausgewerteten Kriterien wurden erfüllt: Enddatum 07.04.2026 unter Einbeziehung von Karfreitag und Ostermontag; belegter Feiertagsort Berlin; keine erfundene Kalendereintragung; nachvollziehbare Korrekturanweisung unter Erhaltung des alten Eintrags. Zusätzlich blieb das Honorar unverändert, unbekannte Zeit wurde weder als null noch als erfundene Buchung behandelt. Eine echte kalenderseitige Ausführung wurde nicht getestet. Die unabhängige Datumsgegenkontrolle nutzte Python, nicht die getrennt getestete neue Plugin-Rechenhilfe.

### 5.2. Partnerausscheiden, digitale Handakte und Cloud

Auftrag: GmbH-Mandat; ausgeschiedener Partner verlangt Vollkopie in eine neue Cloud, behauptet Geschäftsführerzustimmung, aber Vertragsübernahme und Vollmacht sind nicht dokumentiert. AVV vorhanden, Drittlandsupport und Unterauftragnehmer ungeklärt; offene Honorarnote. Verlangt waren Prüfvermerk und vollständiger Antwortentwurf. Geprüft wurde der Berufsrechtsskill.

[Ergebnis](probelaeufe/beruf/ergebnis.md) · [Werkzeuge und Quellen](probelaeufe/beruf/werkzeuglog.md).

Alle vier ausgewerteten Kriterien wurden erfüllt: Mandantin und Übergangsmodelle getrennt; § 43e BRAO, § 203 StGB und Datenschutz konkret geprüft; Handakten-/Herausgabeanspruch und mögliches Zurückbehaltungsrecht differenziert; vollständiges Antwortschreiben ohne behauptete Übertragung oder Freigabe. Die Bearbeitung prüfte außerdem § 32 Abs. 5 BORA für Beendigung mit Neuauftrag. Sie machte das Fehlen dokumentierter Erklärungen nicht zum Beweis ihres Nichtbestehens. Honorar und tatsächliche Zeit blieben offen; eine kostenpflichtige Zusatzbeauftragung durch die GmbH wurde nicht unterstellt.

### 5.3. Aussagegrenzen

Das sind **zwei beobachtete Modellanwendungen**, keine statistische Erfolgsquote und keine Wiederholungsserie. Der [Kriterienkatalog](../evals/ki-native-kanzlei.json) enthält zehn Szenarien mit 40 Kriterien; acht davon wurden in dieser Vertiefungsrunde nicht als neue Modellläufe ausgeführt. Die veröffentlichten Probeläufe sind Lesekopien mit neutralisierten lokalen Dateipfaden und bereinigten Leerzeichen am Zeilenende. [Hashes von Originalen und Lesekopien](probelaeufe/dateinachweis.json) legen diese redaktionelle Änderung offen. Keine Tatsachen oder fachlichen Ergebnisse wurden dafür nachträglich verbessert.

## 6. Erhaltene Akten und Ausführungsgrenzen

Alle 24 Kurzfälle bleiben mit ihren bisherigen zehn Originalstücken erhalten. Nur README-Namen und Rückverweise wurden auf die neue Pluginbezeichnung umgestellt. Die bisherigen öffentlichen Fall-ZIPs behalten ihre alten unveränderlichen URLs; die neue Veröffentlichung ersetzt deren Assets nicht. Frühere Excel-/PDF-/E-Rechnungsprüfungen stehen im [historischen Nachweis](../si-native-kanzlei/rechtsquellen-pruefung.md) und werden nicht als neue Ausführung ausgegeben.

In dieser Prüfung gab es keinen echten beA-Versand, keinen produktiven Zugriff auf Mandantenakten, kein externes Fristenkalender-Schreiben, keine Bankbuchung und keine produktive Rechnungsausgabe. Die installierbaren Pakete enthalten keine Zugangsdaten. Ein Chat-Prompt ermöglicht nur diejenigen Datei- und Werkzeughandlungen, die sein konkreter Host tatsächlich unterstützt.
