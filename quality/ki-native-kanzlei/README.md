# KI-native Kanzlei: Prüfung der Veredelung und der agentischen Schicht

Stand: 8. Oktober 2026. Komponentenfassung `445.33.9`. [Plugin und Downloads](../../ki-native-kanzlei/README.md).

**Aktuelle Prüfung: Abschnitt 11.** Die Abschnitte 1 bis 10 dokumentieren frühere Runden mit ihren damaligen Quellenlücken, Testzahlen und Seitenständen. Sie bleiben als Historie erhalten. Die Computerlauf-Erweiterung wird separat bewertet; unveränderte frühere Rechtsquellen werden nicht als erneute Lektüre ausgegeben.

## 1. Gegenstand und Umfang

Alle achtzehn Skills wurden in einer Runde veredelt. Jeder Skill erhält eine auslöserorientierte Beschreibung, einen Unterabschnitt zu Auslösern, Abgrenzung und Nachbarskills, eine Eingabentabelle mit dem Vorgehen bei fehlenden Angaben, wörtlich ausformulierte Rückfragen in der richtigen Reihenfolge, konkret benannte Normen statt allgemeiner Verweise, einen skillspezifischen Katalog typischer Fehler mit Gegenkontrolle, einen Unterabschnitt zur Übergabe an die Nachbarskills, Entscheidungsanker mit „Trägt“ und „Trägt nicht“, Abnahmekriterien im Ausgabeformat sowie mindestens zwei vollständig ausformulierte Endprodukte und ein Negativbeispiel. Prompts, Skripte, Referenzen zu Rechenhilfe und Mandatsordner sowie die 24 Fachanwaltsakten sind unverändert; die gemeinsame Arbeitsweise beschreibt neu die Skillauswahl nach Startsituation und die Pflicht, Fehlerkatalog und Abnahmekriterien tatsächlich durchzugehen.

Die 18 Skills haben im tatsächlichen A4-Satz mit 11 pt jeweils 15 bis 17 Seiten, zusammen **284 Seiten** und rund 118.800 Wörter (zuvor 194 Seiten und rund 79.600 Wörter). Das ist kein aus einer Wortzahl errechneter Seitenwert. [Umfang, Schrift, Layout und Datei-Hashes](umfang.json) und [Buildprotokoll](logs/pdf-build.log) dokumentieren die erzeugten Lesefassungen. Die Werkstatt umfasst 11.921 Wörter; Mini und Hauptproblem bleiben mit 7.381 beziehungsweise 7.488 UTF-8-Bytes innerhalb der konservativen 7.500-Byte-Grenze. Die jeweiligen MD-/TXT-Paare sind byteidentisch.

## 2. Rechtsquellen und Grenzen dieser Prüfrunde

Die Entscheidungsanker aller Skills sind auf die Entscheidungen beschränkt, die in der Vorfassung am amtlichen Volltext gelesen und in den drei Quellenberichten dokumentiert wurden; die Randnummern wurden von dort übernommen. Keine Entscheidung wurde neu aus Modellwissen aufgenommen, keine Kommentar- oder Aufsatzfundstelle zitiert.

1. [Fristen, Berufsrecht, Annahme, Geldwäsche und Abschluss](beruf-fristen-quellen.md).
2. [Vergütung, Zeiten, Abrechnung, Buchhaltung und Verträge](verguetung-vertraege-quellen.md).
3. [Hauptworkflow, Recherche, Schriftsatz, Kommunikation und beA](sacharbeit-workflow-quellen.md).

Eine wesentliche Grenze dieser Runde: Die Netzwerkrichtlinie der Bearbeitungsumgebung verweigerte den Abruf von gesetze-im-internet.de, EUR-Lex, BRAK und sämtlichen Gerichtsseiten (HTTP 403 am Ausgangsproxy, mit curl gegengeprüft). Neu eingeführte Normaussagen konnten daher nicht am amtlichen Volltext geöffnet werden. Die Bearbeitung hat deshalb drei Klassen unterschieden: Erstens Normaussagen, die bereits in [`references/rechtsquellen.md`](../../ki-native-kanzlei/references/rechtsquellen.md) oder den Quellenberichten am Volltext geprüft sind; sie wurden ohne Vorbehalt übernommen. Zweitens Normaussagen, die nur über Suchtreffer auf die amtlichen Einzelnormseiten oder sekundäre Gesetzesspiegel plausibilisiert wurden; sie tragen im Skill den Zusatz „am Volltext zu prüfen“ oder werden ohne Zahlenwert genannt. Drittens Aussagen, die sich nicht belegen ließen; sie wurden weggelassen. Betroffen sind insbesondere die Wertgrenzen in § 544 und § 511 ZPO nach der Änderung zum 1. Januar 2026, die Aufbewahrungsfristen nach § 147 AO und § 14b UStG nach dem Vierten Bürokratieentlastungsgesetz, einzelne Absatz- und Satzzuordnungen in BRAO und BORA sowie Schwellenwerte im GwG; die Abschlussberichte je Skill sind in Abschnitt 7 zusammengefasst. Vor einem Einsatz in der Praxis sind diese Markierungen am amtlichen Text aufzulösen; die Skills verlangen das ausdrücklich.

## 3. Tatsächlich ausgeführte technische Prüfungen

| Prüfung | Nachweis und Ergebnis |
| --- | --- |
| Strenge Vorprüfung aller Skills | Frontmatter nur `name` und `description` (höchstens 1024 Zeichen, keine Dezimalkommas), sechs Hauptabschnitte in fester Reihenfolge, ausschließlich dezimale Unterüberschriften, Pflichtwörter zu Format und Ausformulierung, keine verbotenen Zeichen, alle relativen Links vorhanden, Tabellen mit höchstens vier Spalten, Pflichtbausteine (Rückfragen, Fehlerkatalog, Übergabe, Abnahmekriterien, Negativbeispiel) in jedem Skill; alle Wochentagsangaben der Beispiele mit Python geprüft. |
| Fristen-Rechenhilfe | [18 Testmethoden](logs/fristen-tests.log) bestanden. |
| Mandatsjournal | [19 Tests](logs/journal-tests.log) bestanden. |
| Dokument-/Rechnungsexporte | [16 Tests](logs/export-tests.log) bestanden. |
| Quellenstruktur | [Strukturbericht](struktur-pruefung.json): 18 Skills, Promptpaare, Versionsdaten, Prüfprofil, Quelldatei-Hashes gegen den Umfangsbericht. |
| Pakete und Originalerhaltung | [Paketbericht](paket-pruefung.json): beide Installationspakete quellidentisch, 18 Skills, drei Manifeste, Standalone-Prompts getrennt; sämtliche 240 Originale mit den Git-Objekten des unveränderten Tags `si-native-kanzlei-v445.33.3` verglichen. |
| Skriptfunktion | Die in den Skills zitierten Befehle, Optionen, Felder und Meldungen von `kanzlei.py`, `fristen.py`, `xrechnung.py` und `build_anlagenkonvolut.py` wurden an der tatsächlichen Hilfeausgabe und dem Quelltext abgeglichen; Beispielrechnungen in Zeiterfassung und Abrechnung wurden mit dem Journal beziehungsweise mit Dezimalarithmetik nachgerechnet. |

Die Claude-Pluginvalidierung wurde für diese Fassung nicht erneut ausgeführt; die Manifeste sind bis auf die Versionsnummer unverändert. Die Fristenhilfe berechnet weiterhin nur ein **zuvor rechtlich gewähltes und bestätigtes Profil** mit bereitgestelltem Feiertagskalender.

## 4. PDF-Prüfung

Die Lesefassungen wurden in dieser Umgebung mit **Liberation Serif 11 pt** gesetzt, einer metrisch zu Times New Roman kompatiblen Schrift; Times New Roman war in der Umgebung nicht installiert. Der Umfangsbericht weist die Schrift aus; der Builder nimmt sie als ausdrückliche Option entgegen und bezeichnet sie nicht als Times New Roman. Ein Probelauf mit den unveränderten Skills der Vorfassung ergab unter Liberation Serif dieselben 194 Seiten wie der frühere Times-New-Roman-Satz; das stützt die Vergleichbarkeit, ist aber kein Beweis identischer Umbrüche für jede Seite.

Der Builder vergleicht den geordneten Text aller Absätze und Tabellenzellen mit den erzeugten PDFs. Alle 284 Seiten wurden auf innerhalb der Seite liegende Textgeometrie geprüft ([Geometriebericht](pdf-geometrie.json), keine Abweichung), und das Handbuch wurde seitenweise mit den Einzel-PDFs verglichen ([Zusammenfügungsbericht](handbuch-zusammenfuegung.json), alle Seitentexte und Seitenformate identisch). Sechs gerenderte Seiten wurden einzeln angesehen; ein kosmetischer Umbruch in der Fristenübersicht wurde korrigiert und der Satz wiederholt. [Sichtprüfbericht](pdf-sichtpruefung.md). Die frühere Sichtprüfung von 63 Seiten betraf die Vorfassung und wurde nicht wiederholt.

## 5. Zwei unabhängige Modell-Probeläufe der Vorfassung

Die beiden Probeläufe stammen aus der Vorfassung 445.33.4 und wurden für die veredelte Fassung 445.33.7 nicht wiederholt; sie betreffen den damals unveränderten Mini-Prompt und den damaligen Stand des Berufsrechtsskills. Zwei Instanzen ohne vorausgehende Unterhaltung erhielten jeweils den konkreten Auftrag und nur den zu prüfenden Mini-Prompt beziehungsweise Berufsrechtsskill sowie dessen Referenzen. Sie sollten die Fälle tatsächlich bearbeiten, durften Rechtsquellen und Werkzeuge benutzen und erhielten keine Bewertungskriterien, fremden Ergebnisse oder QA-Dateien. Die Hauptinstanz hat anschließend die vollständig vorliegenden Ergebnisse und Werkzeugprotokolle beurteilt.

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

## 7. Abschlussberichte der Skillbearbeitung

Je Skill wurde ein Abschlussbericht mit Wortzahl, Änderungen, Quellenstatus und offenen Punkten erstellt; die Kernaussagen sind hier zusammengefasst. Alle 18 Berichte nennen den gescheiterten Volltextabruf und listen die markierten Stellen. Die folgenden Punkte sind vor Praxiseinsatz am amtlichen Text zu prüfen: Wertgrenzen § 511 Abs. 2 und § 544 ZPO mit Übergangsregel (Fristen, Schriftsätze); § 147 AO und § 14b UStG nach dem Vierten Bürokratieentlastungsgesetz (Abrechnung, Zahlungen, Abschluss); § 19 UStG Grenzen und § 13 RVG Mindestgebühr (Abrechnung); § 4 BORA Anderkonto und Einbehaltsgrenzen (Zahlungen, Berufsrecht, Abschluss); § 3 BORA Absatzzuordnung, § 44, § 45, § 52, § 53, § 56 BRAO Wortlaut (Mandatsannahme, Berufsrecht); § 10 Abs. 3 GwG Schwelle und § 56 GwG Absatzstruktur (Geldwäsche); § 308 Nr. 1a und 1b, § 309 Nr. 9, § 202, §§ 474/476 BGB Werte (AGB-Prüfung, Vertragsgestaltung); § 203 Abs. 3 und 4 StGB sowie Art. 44 ff. DSGVO Reichweite (Übergabe, Akte); § 31 BVerfGG Reichweite (Recherche); § 2 Abs. 2 und § 11 BORA Wortlaut (Mandantenkommunikation); § 131, § 133, § 130a Abs. 5 und 6, § 130d ZPO Satzzuordnung (beA). Die Gebührentabelle nach § 13 RVG wurde in keinem Beispiel als Tabellenwert verwendet; das Rechenbeispiel der Abrechnung nennt seinen Rechenwert ausdrücklich als Annahme.

## 8. Zweite Runde: agentische Schicht (445.33.6)

Die Fassung 445.33.6 ergänzt eine [Referenz zu Mandatslauf und Freigabestufen](../../ki-native-kanzlei/references/mandatslauf-und-freigaben.md) und den Helfer `scripts/mandatslauf.py`. Er führt je Mandat Phase, Nebenläufe, Produktregister mit SHA-256 der führenden Fassung, die Gates G1 bis G8, offene Fragen, Revision und Historie, schreibt atomar, verweigert das Überschreiben eines vorhandenen Laufs und weist Freigaben durch Maschinenbezeichnungen ab. [15 Tests](logs/lauf-tests.log) bestanden, darunter Freigabe nur durch benannte Person, Freigabe nur nach geprüfter Fassung, Vorrang eines offenen Fristgates in `next`, Sperre der Abschlussphase bis zur Entscheidung über G4, G5 und G8 sowie Zurückweisung von Steuerzeichen und Pfaden außerhalb des Mandatsordners.

Alle achtzehn Skills erhielten einen Unterabschnitt „Agentischer Lauf und Freigabestufe“ mit Phase, Verhalten auf den Stufen 0 bis 3, geöffneten Gates, Produktregister, einem gegen den Helfer tatsächlich ausgeführten Beispielaufruf und einer Stoppregel. Die Übergabeartefakte heißen nun einheitlich führende Fassung, Fristobjekt, Honorarstand, Zeitstand, offene Gates und offene Fragen. Jeder Skill wurde in derselben Runde ein zweites Mal fachlich gelesen; dabei wurden Dubletten gestrafft, ein falsches Datum (Schlussrechnung nach Mahnung) und ein Samstagszugang in Beispielen korrigiert, widersprüchliche Beispielpositionen in der Zeiterfassung bereinigt und weitere nicht verifizierte Absatz- und Wertangaben mit Prüfvorbehalt versehen oder gestrichen. Die Absatzzuordnung von § 356 Abs. 5 BGB wurde auf den im Prüfprofil dokumentierten Prüfstand vereinheitlicht. Die Zuordnung der Skills zu Phasen und Gates ist in Abschnitt 1.9 der Referenz tabellarisch zusammengefasst.

Werkstatt-Prompt (Kapitel 29) und Mini-Prompt (Abschnitt 7, 7.436 Bytes) beschreiben den Mandatslauf; der Hauptproblem-Prompt ist unverändert. Die Übergabedatei für eine nachfolgende Glättung mit Codex liegt unter [`docs/codex-uebergabe-ki-native-kanzlei.json`](../../docs/codex-uebergabe-ki-native-kanzlei.json). Netzabrufe auf amtliche Gesetzes- und Gerichtsseiten blieben auch in dieser Runde gesperrt; die Grenzen aus Abschnitt 2 gelten unverändert.

## 9. Dritte Runde: Kanzleialltag und Normabgleich (445.33.7)

### 9.1. Kanzleialltag in Claude Cowork und ChatGPT

Die Fassung 445.33.7 bildet den Arbeitstag einer Kanzlei als wiederkehrende Abläufe ab. Die [Referenz Kanzleialltag](../../ki-native-kanzlei/references/kanzleialltag-workflows.md) beschreibt Tagesstart, neue Anfrage, Posteingang, Fristsache, Schriftsatz bis zur Einreichung, Vertragsprojekt, Mandantenkommunikation, Zeiten, Wochenabschluss, Monatsabrechnung und Zahlungen, Übergabe an externe Dienste, Mandatsende, Freigaben und die Einführung in der Kanzlei. Fünfzehn Befehle im Ordner `commands` rufen diese Abläufe in Claude Cowork und Claude Code auf; ChatGPT erhält dieselben Abläufe über den Mini-Prompt als Projektanweisung und die [Einrichtungsanleitung](../../ki-native-kanzlei/references/chatgpt-und-cowork-einrichtung.md). Der Helfer `mandatslauf.py` kennt den neuen Befehl `cockpit`, der alle Mandatsläufe unter einem Wurzelordner nach offenen Fristgates, sonstigen Gates und offenen Fragen ordnet und ausdrücklich keine externe Handlung erlaubt. [18 Lauftests](logs/lauf-tests.log) bestanden, darunter drei neue Cockpittests. Eine Vorlage für die Kanzleiorganisation (wer welches Gate freigibt) und ein Demo-Bestand mit drei Mandaten liegen unter `assets`.

### 9.2. Normabgleich über GitHub Actions

Weil die Sitzungsumgebung amtliche Gesetzesseiten nicht erreicht, ruft der Workflow `ki-native-kanzlei-normcheck.yml` die 93 im Plugin tragenden Normen aus einem GitHub-Runner ab und legt den Bericht im Zweig ab. Der [erste Lauf](normcheck/normcheck-2026-10-07.md) lieferte 51 auswertbare Texte: BORA (Stand 01.12.2025, PDF der BRAK), Rom I und Brüssel Ia amtlich, 48 Einzelnormen über dejure.org als ausdrücklich gekennzeichnete Sekundärquelle, weil gesetze-im-internet.de vom Runner aus nicht antwortete. 42 Abrufe scheiterten an Zeitüberschreitung oder HTTP 503. Der gedrosselte [Nachlauf](normcheck/normcheck-2026-10-07-2046.md) lieferte 39 davon nach, sodass 90 der 93 Normtexte gelesen vorliegen; offen blieben nur die RVG-Gebührentabelle (Anlage 2), Teil 7 VV RVG und § 47 EGZPO, die über die Websuche abgeglichen wurden. Die berichtigten Aussagen wurden anschließend gegen diese Texte gegengelesen: § 4a Absatz 1 und 3 RVG, § 4b RVG, § 53 Absatz 1 BRAO, § 43a Absatz 2 Satz 4 BRAO, § 8 Absatz 2 und 4 GwG, § 10 Absatz 3 GwG, § 16a Absatz 3 GwG, § 43 Absatz 4 GwG, § 4 Absatz 2 DL-InfoV, § 5 ERVV, § 309 Nummer 8 Buchstabe b BGB, § 356 Absatz 4 BGB, § 66 Absatz 2 GKG und § 4 BORA stimmen mit dem übernommenen Wortlaut überein.

### 9.3. Websuche-Abgleich und Übernahme in die Skills

Alle bisher mit Prüfvermerk versehenen Normaussagen wurden zusätzlich über die Websuche gegen amtliche Einzelnormseiten und Spiegel abgeglichen. Der [Befundbericht](normcheck/normbefunde-websuche-2026-10-07.md) zählt 85 bestätigte, 12 berichtigte und 5 nicht ermittelbare Aussagen und nennt je Skill Zeile, alten und neuen Satzteil. Alle 100 Änderungen wurden in 17 Skills übernommen; der Vermerk „am Volltext zu prüfen“ blieb nur dort, wo der Wert nicht ermittelbar war. Die wichtigsten Berichtigungen betreffen § 4a RVG (geltende Fassung „bei verständiger Betrachtung … abgehalten“ statt der bis 30.09.2021 geltenden wirtschaftlichen Verhältnisse; Pflichtangaben nach Absatz 3), § 4b RVG (Reichweite), § 53 BRAO (keine Anzeigepflicht gegenüber der Kammer mehr), § 8 Absatz 2 und 4 GwG (Kopien, Fristbeginn mit Jahresschluss, Vernichtung spätestens nach zehn Jahren), § 43 Absatz 4 GwG, § 4 BORA (kein allgemeines Einbehaltsrecht), §§ 2 bis 4 DL-InfoV, Nr. 7000 VV RVG, § 309 Nummer 8 Buchstabe b Doppelbuchstabe ff BGB und § 5 ERVV. Bestätigt und nun ohne Vorbehalt verwendet werden unter anderem § 13 Absatz 3 RVG (15 Euro), § 8 Absatz 1 RVG, § 4a Absatz 1 RVG (2.000 Euro), §§ 44, 52 und 53 BRAO, § 511 Absatz 2 Nummer 1 ZPO (1.000 Euro), § 544 Absatz 2 Nummer 1 ZPO (25.000 Euro) mit § 47 EGZPO, § 23 Nummer 1 GVG (10.000 Euro seit 01.01.2026) mit § 44 EGGVG, § 66 GKG (300 Euro), § 147 AO und § 14b UStG (acht Jahre) mit Art. 97 § 19a EGAO, § 10 Absatz 3 GwG (15.000 Euro), § 16a GwG und die BORA-Vorschriften §§ 3, 4, 11 und 17.

Grenzen: Der Websuche-Abgleich stützt sich auf Suchtreffer-Auszüge; eine amtliche Seite wurde dabei nicht vollständig geöffnet. Nicht ermittelbar blieben § 476 Absatz 1 BGB (negative Beschaffenheitsvereinbarung), § 45 BRAO ab Absatz 2, die Doppelbuchstabenzuordnung in § 2 Absatz 1 Nummer 10 GwG und die Fristentabelle im Fristenskill. Rechtsprechung wurde in dieser Runde nicht neu aufgenommen.

## 10. Glättungsrunde Codex

Stand: 08.10.2026. Komponentenfassung 445.33.8. Bearbeitet wurden alle 18 Skills, drei Promptpaare, die acht benannten Referenzen und fünfzehn Befehle. Die 24 Testakten mit 240 Originaldateien bleiben unverändert. Die neue Runde ersetzt die Quellenvorbehalte der Abschnitte 2, 7 und 9 für die nun bearbeiteten Aussagen; die alten Berichte bleiben als nachvollziehbare Historie erhalten.

### 10.1. Amtlicher Normabgleich und Rechtsprechung

Die einschlägigen amtlichen Gesetzes- und Entscheidungstexte wurden erneut abgerufen und in den jeweiligen Absätzen beziehungsweise Randnummern gelesen. Die 18 Einzelberichte nennen URL, Lesedatum, gelesenen Umfang, Korrektur und Selbsttest. Sie unterscheiden tatsächliche Lektüre von Abruf und Suchtreffer. Entscheidungsanker behalten „Trägt“ und „Trägt nicht“; Kommentar-, Handbuch- und Aufsatzbelege wurden ausgeschlossen. Es wurden keine Entscheidungen aus Modellwissen ergänzt.

Der [Nachtrag zum Normbefund](normcheck/normbefunde-websuche-2026-10-07.md#9-nachtrag-gelesene-amtliche-volltexte-vom-08102026) dokumentiert insbesondere die zwölf berichtigten Normbereiche, § 356 und § 356a BGB, die Übergänge in EGZPO, EGGVG, GKG und EGAO sowie die vollständigen Fassungen von § 45 BRAO, § 476 BGB und § 2 Absatz 1 Nummer 10 GwG. Die Fristenübersicht wurde zeilenweise gegen die einschlägigen Normen geprüft. Die Anlagentabelle des RVG und Teil 7 VV RVG wurden gelesen; das Gebührenbeispiel nutzt nun den belegten Tabellenwert statt eines Ersatzwerts.

Der erste breite Actions-Nachlauf erreichte das Runner-Zeitlimit. Der [gezielte Nachlauf](normcheck/normcheck-2026-10-08-0613.md) erreichte alle 22 Zieltexte amtlich. Seine Ausschnittgrenzen werden im Nachtrag offengelegt; die zusätzlichen direkten Volltextlektüren schließen die für den Prüfauftrag relevanten Auslassungen. Die früheren 85 Suchtreffer-Bestätigungen werden nicht rückwirkend als Volltextprüfung bezeichnet.

Konkrete Korrekturen betreffen unter anderem RVG-Erfolgshonorar und Formfolgen, Mindest-/Tabellengebühren, die Trennung von Fälligkeit und Einforderbarkeit, E-Rechnungsübermittlung im Übergangszeitraum, Aufbewahrungsbeginn nach Dokumentkategorie und besonderen Übergängen, BGB-Verbraucher- und AGB-Ausnahmen, GwG-Identifizierung und PEP-Nachwirkung sowie differenzierte Rechtsmittel- und Wiedereinsetzungsfristen. Der Quellenstand ist fallbezogen am tatsächlichen Bearbeitungstag weiterzuführen; er verspricht keine automatische Beobachtung künftiger Änderungen.

### 10.2. Abschlussbericht je Skill

Körperwortzahlen ohne YAML-Frontmatter, Vergleich mit dem Ausgangsstand 445.33.7. Insgesamt 119.996 Wörter; jeder Skill hält den verlangten Korridor ein, der Fristenskill die gesonderte Obergrenze von 7.000. Die Berichte enthalten zusätzlich den abschließenden SHA-256.

| Skill | Vorher | Nachher | Quellen, Korrekturen und Selbsttest |
| --- | --- | --- | --- |
| `abrechnung-e-rechnung` | 6.498 | 6.736 | [Einzelbericht](glaettung-2026-10-08/skills/abrechnung-e-rechnung.md) |
| `akte-fristen-anlegen` | 6.563 | 6.533 | [Einzelbericht](glaettung-2026-10-08/skills/akte-fristen-anlegen.md) |
| `anwaltsberufsrecht-pruefen` | 6.643 | 6.743 | [Einzelbericht](glaettung-2026-10-08/skills/anwaltsberufsrecht-pruefen.md) |
| `bea-anlagen-vorbereiten` | 6.537 | 6.560 | [Einzelbericht](glaettung-2026-10-08/skills/bea-anlagen-vorbereiten.md) |
| `fristen-berechnen-ueberwachen` | 6.995 | 6.976 | [Einzelbericht](glaettung-2026-10-08/skills/fristen-berechnen-ueberwachen.md) |
| `geldwaesche-pruefen` | 6.645 | 6.741 | [Einzelbericht](glaettung-2026-10-08/skills/geldwaesche-pruefen.md) |
| `honorar-budget-vereinbaren` | 6.647 | 6.789 | [Einzelbericht](glaettung-2026-10-08/skills/honorar-budget-vereinbaren.md) |
| `ki-kanzlei-steuern` | 6.475 | 6.552 | [Einzelbericht](glaettung-2026-10-08/skills/ki-kanzlei-steuern.md) |
| `mandantenkommunikation` | 6.452 | 6.491 | [Einzelbericht](glaettung-2026-10-08/skills/mandantenkommunikation.md) |
| `mandat-abschliessen` | 6.648 | 6.709 | [Einzelbericht](glaettung-2026-10-08/skills/mandat-abschliessen.md) |
| `mandatsannahme-interessenkollision` | 6.648 | 6.712 | [Einzelbericht](glaettung-2026-10-08/skills/mandatsannahme-interessenkollision.md) |
| `recht-recherchieren` | 6.521 | 6.420 | [Einzelbericht](glaettung-2026-10-08/skills/recht-recherchieren.md) |
| `schriftsaetze-entwerfen` | 6.547 | 6.743 | [Einzelbericht](glaettung-2026-10-08/skills/schriftsaetze-entwerfen.md) |
| `vertraege-agb-pruefen` | 6.699 | 6.778 | [Einzelbericht](glaettung-2026-10-08/skills/vertraege-agb-pruefen.md) |
| `vertraege-gestalten` | 6.598 | 6.646 | [Einzelbericht](glaettung-2026-10-08/skills/vertraege-gestalten.md) |
| `workflow-uebergabe` | 6.469 | 6.562 | [Einzelbericht](glaettung-2026-10-08/skills/workflow-uebergabe.md) |
| `zahlungen-buchhaltung` | 6.716 | 6.791 | [Einzelbericht](glaettung-2026-10-08/skills/zahlungen-buchhaltung.md) |
| `zeiten-erfassen` | 6.482 | 6.514 | [Einzelbericht](glaettung-2026-10-08/skills/zeiten-erfassen.md) |

### 10.3. Mandatslauf, Übergaben und Prompts

Die [Zuordnungsmatrix](../../ki-native-kanzlei/references/mandatslauf-und-freigaben.md) enthält alle achtzehn Skills mit Phase, Gate und Produktkennung sowie 126 gerichtete Übergaben mit Eingangsprodukt und Rückgabe. Dokumentarbeit, fachliche Prüfung, tatsächliche menschliche Erklärung und externer Vollzug bleiben getrennt. Fristeintragungsauftrag ist kein Kalendernachweis; das offene G2 blockiert unabhängige Arbeit nicht. G4 umfasst die endgültige Rechnungsnummer. Ein abgelegter Name ist keine Freigabe.

Werkstatt-Kapitel 29 und 30, Mini-Abschnitt 7, Hauptproblem-Prompt, Befehle und Referenzen verwenden denselben Statuskern. Mini: 7457 UTF-8-Bytes; Hauptproblem: 7479 UTF-8-Bytes; Werkstatt: 12594 Wörter. Alle MD-/TXT-Paare sind byteidentisch und die vier verlangten Hashfelder im Prüfprofil aktualisiert. Ein vollständiger Textstatus ersetzt mangels Dateizugriffs keine behauptete Speicherung.

### 10.4. Tatsächlich ausgeführte Probeläufe

Die Hauptinstanz führte fünf fiktive Mandate auf Stufe 2 in einem Scratch-Kanzleiordner durch: die drei Alltagssituationen und zusätzlich Cloud-Aktenübergabe und Honorarreichweite. Das [Helferprotokoll](glaettung-2026-10-08/probelauf-protokoll.json) enthält 58 Aufruf-/Prüfeinträge, darunter die erwartete Verweigerung eines verfrühten Abschlusses. Das Szenario einer ausdrücklich vorgegebenen menschlichen Freigabe ist als fiktive Eingabe gekennzeichnet; sie wurde nicht vom Modell erzeugt.

| Mandat | Offenes Gate | Nächstes Produkt | Benannte Verantwortung |
| --- | --- | --- | --- |
| Versäumnisurteil Berlin | G2 | `rechenvermerk-vu` | RA Bertram Brecht |
| Vertragsprüfung mit Auftragserweiterung | G4 | `rechnung` | RAin Ada Ahrens |
| Mandatsende mit Fremdgeld | G5/G8 | `zahlungsstand` | RA Emil Eberhardt |
| Partnerausscheiden und Cloud | G6 | `uebergabevermerk` | RAin Ada Ahrens |
| Stundenhonorar-Reichweite | G1 | `honorarstand` | RA Bertram Brecht |

Zusätzlich bearbeiteten zwei frische Modellinstanzen ohne QA-Rubrik oder fremde Ergebnisse die drei Alltagssituationen im Textmodus und die beiden Fachfälle mit tatsächlichem Helferzugriff. Der Fachlauf erzeugte vier ausformulierte Arbeitsprodukte und 46 erfolgreiche Helferaufrufe; die offenen Freigaben und fehlenden Tatsachen blieben sichtbar. Der Textlauf erstellte sieben aufeinander aufbauende Antworten. [Ergebnisse, unveränderte Lesekopien und Bewertung](glaettung-2026-10-08/proben/README.md).

Die erste Textantwort zur Rechnung hatte fünf Spalten; die Abschlussantwort bezeichnete die Phase trotz offener Gates als Abschluss. Beide Befunde wurden ausdrücklich nachgeschärft und in einem getrennt ausgewiesenen Nachtest behoben. Die ursprünglichen Ergebnisse bleiben erhalten. Es handelt sich um beobachtete lokale Helfer-/Modellanwendungen, nicht um einen Test der nativen Cowork- oder ChatGPT-Oberflächen und nicht um eine Erfolgsquote für alle zehn Szenarien des Prüfprofils.

### 10.5. Durch Tests begründete Skriptkorrekturen

Die ursprünglichen 18 Mandatslauftests waren grün. Zunächst fehlschlagende neue Tests belegten verloren gehende Gate-Verantwortliche, festes statt produktbezogenes Routing, Freigabe trotz geänderter Fassung, fehlende namentliche Produktfreigabe, unzureichende erneute Öffnung bei Änderungen, Abschluss trotz Ablehnung und die unvollständige Isolation beschädigter Cockpitdaten. Die Korrekturen behalten Produkt- und Entscheidungshistorie, binden registrierte Produkte an Hash und Fachskill und lassen abgelehnte Abschlussgates blockieren. Zwei anschließende Regressionen sichern den Skillwechsel bei unverändertem Hash und ungültige Nebenlaufdaten. Nun bestehen 30 Tests. [Vorher-/Nachher-Logs](glaettung-2026-10-08/logs/).

Der PDF-Fuß und die Paket-README trugen im ersten tatsächlichen Build noch den 07.10.2026. Erst nach diesem nachgewiesenen Fehler wurden die beiden Datumsangaben in den Buildern berichtigt. Weitere produktive Helfer wurden nicht verändert. Der Mandatslauf bleibt ein lokales Journal, kein Authentifizierungs- oder Berechtigungssystem und kein Beleg einer tatsächlich ausgeführten Außenhandlung.

### 10.6. Lesefassungen und technische Abnahme

Alle 18 Skills wurden zweimal tatsächlich als A4 gesetzt: lokal mit Times New Roman 11 pt und als Release-Projektion mit Liberation Serif 2.1.5, ebenfalls 11 pt. Beide Sätze umfassen je Skill 15 bis 18 Seiten und insgesamt 291 Seiten. Der zentrale [Umfangsnachweis](umfang.json) gehört zur Release-Projektion; der separate [Times-New-Roman-Nachweis](glaettung-2026-10-08/umfang-tnr.json) kennzeichnet die lokale Fassung. Das Release verwendet die im Workflow ausdrücklich festgelegte Liberation Serif, weil dort Times New Roman nicht bereitgestellt wird.

Der Builder fand alle gerenderten Quellabsätze und Tabellenzellen in unveränderter Reihenfolge wieder. In beiden Sätzen liegen sämtliche Wortgeometrien innerhalb der Seite; das Handbuch stimmt seitenweise mit den Einzel-PDFs überein. Acht gerenderte Seiten wurden tatsächlich angesehen. [Sichtprüfung](glaettung-2026-10-08/pdf-sichtpruefung.md), [TNR-Geometrie](glaettung-2026-10-08/pdf-geometrie-tnr.json), [Release-Geometrie](glaettung-2026-10-08/pdf-geometrie-liberation.json).

Die vollständigen Befehle und Rückgabecodes stehen im [Prüfprotokoll](glaettung-2026-10-08/pruefbefehle.json). Ausgeführt wurden Quellenprüfung, 30 Lauf-, 18 Fristen-, 19 Journal- und 16 Exporttests, Skillaktivierungs-Audit, YAML-, Markdown- und Pluginstrukturprüfung, Marketplace-Importtests, Quality-Lab-Audit sowie Handbuch-, Release- und Paketbuild. Die Paketprüfung vergleicht auch alle 240 Testaktenoriginale mit dem unveränderten Ausgangstag. Build und Umfang unterscheiden die beiden Schriftfassungen ausdrücklich.

### 10.7. Veröffentlichung und verbleibende Ausführungsgrenzen

Die Manifeste, Marketplace-Eintrag, Komponententests, README-Verweise, Indizes und Downloadziele führen einheitlich 445.33.8. Das allgemeine Repository-Release bleibt davon unabhängig. Die Veröffentlichung erfolgt über den vorgesehenen manuellen Komponentenworkflow mit `tag=ki-native-kanzlei-v445.33.8`; er setzt den Tag auf den geprüften Commit.

Keine produktiven Mandantenakten, beA-Nachrichten, Kalender, Bankkonten oder Rechnungsausgaben wurden angesprochen. Slash-Befehle und Werkzeuge hängen vom konkreten Host ab. Menschliche Zuständigkeit, fachliche Prüfung, tatsächliche Freigabe und Vollzugsnachweis bleiben erforderlich, soweit der konkrete Schritt sie verlangt.

### 10.8. Integration der zwischenzeitlichen Main-Änderungen

Vor dem Merge wurden die parallel veröffentlichten Erweiterungen aus #528, #529 und die Prüfinfrastruktur aus #530 integriert. Ihre Quellenarchive, Testakten und Fachtexte bleiben erhalten. Der globale Aktivierungs-Audit meldete dabei 16 bereits mit diesen Importen hinzugekommene Beschreibungen über 360 Zeichen. Ausschließlich deren description-Zeilen wurden auf 271 bis 324 Zeichen gestrafft und die betroffenen Anzeigezeilen synchronisiert; alle Textkörper sind byteidentisch. [Vorher-/Nachher-Nachweis](glaettung-2026-10-08/integration-description-korrektur.json). Diese begrenzte Integrationskorrektur ändert keine rechtliche Aussage und keinen Skill-Ablauf der Nachbarplugins. Die ursprünglichen fehlgeschlagenen Integrationsprüfungen und die abschließende Wiederholung werden getrennt dokumentiert.

Die [abschließende Integrationsprüfung](glaettung-2026-10-08/integration-final-pruefbefehle.json) ist grün. Zusätzlich wurden 34 Release-Routing-Tests und die Vergabe-Importprüfung ausgeführt; letztere kennzeichnet drei ohne externe Buildartefakte nicht ausgeführte Zusatzprüfungen ausdrücklich als übersprungen. Die Kanzlei-Paketprüfung einschließlich der 240 Originale lief vollständig.

## 11. Computerlauf, Postfächer und kontrollierter beA-Ablauf (445.33.9)

### 11.1. Umfang und tatsächliche Fähigkeiten

Stand: 08.10.2026. Die 18 Skills bleiben erhalten; Steuerung und beA wurden überarbeitet. Werkstatt, Mini und Hauptproblem führen denselben Arbeitsfluss von Eingang und Akte über Frist/Sachprodukt bis zu konkreter menschlicher Entscheidung, erlaubter Ausführung und Nachweiskontrolle. Die 17 Befehle enthalten jetzt `/computerlauf` und `/bea`. Der lokale Helfer dokumentiert Sitzungsgrenzen, gebundene Versandfassungen und einzelne Versuche. Er enthält keinen eigenen Mail- oder beA-Transport und authentifiziert keine Freigabeperson. Reale Ausführung hängt von tatsächlich vorhandenen und erlaubten Hostwerkzeugen ab. Keine Appfreischaltung wird durch das Plugin behauptet.

Die README warnt vor tatsächlicher Außenwirkung, Geheimnisoffenbarung und PIN-/Tokenkompromittierung. Die geöffnete Herstellerwarnung gegen sensible juristische Computersteuerung ist ausdrücklich enthalten. Der persönliche beA-Schlussakt wird nicht als Agentenklick ausgegeben; jedes eEB bleibt im Prototyp persönlich. Geheimnisse werden nicht durch das Plugin gespeichert oder ausgelesen. Ein Journal ist eine kooperative Organisationshilfe, keine manipulationssichere Schutzgrenze gegen einen Agenten mit denselben Dateirechten.

### 11.2. Quellen, Texte und Lesefassungen

[Abschlussberichte der Skills](agentisch-2026-10-08/skillberichte.md) · [32 gelesene beA-Primärquellen](agentisch-2026-10-08/bea-quellen.md) · [Herstellerquellen](../../ki-native-kanzlei/references/computersteuerung-und-postfaecher.md#19-geprüfte-herstellerquellen-und-grenzen).

Die beiden geänderten Skills umfassen 6.514 und 6.736 Körperwörter; insgesamt enthalten die 18 Skills 120.134 Wörter. Die Kurzprompts haben 7.472 beziehungsweise 7.493 UTF-8-Bytes, die Werkstatt 121.006 Bytes. Die drei MD/TXT-Paare sind byteidentisch; ihre Hashes stehen im Prüfprofil. Alle Skillstrukturen, lokalen Links, Beschreibungslängen, Tabellenbreiten und unmittelbar angegebenen Wochentage wurden erneut geprüft. Die übrigen sechzehn Skills blieben byteidentisch zur Ausgangsfassung.

Beide Schriftvarianten haben 292 tatsächliche A4-Seiten. Release: Liberation Serif 11 pt; zusätzlich lokal Times New Roman 11 pt. [Sichtprüfung](agentisch-2026-10-08/pdf-sichtpruefung.md) und [Geometrie-/Zusammenfügungsprüfung](agentisch-2026-10-08/pdf-pruefung.json) dokumentieren Umfang und Aussagegrenzen. Die 240 Originalstücke der 24 Testakten wurden nicht bearbeitet.

### 11.3. Tatsächlich ausgeführte Prüfungen

Die Protokolle der folgenden Befehle liegen im [Prüfverzeichnis](agentisch-2026-10-08/logs/). Die neuen Computerlauf-Tests betreffen unter anderem Konten-/Bereichsgrenzen, Manipulation von Dateien oder Freigabebeleg, Parallelstarts, abgebrochene Reservierungen, Sitzungswechsel, doppelte Nachrichten, Timeouts und persönlichen beA-Versand.

```text
python3 scripts/test-ki-native-kanzlei-computerlauf.py
python3 scripts/test-ki-native-kanzlei-source.py
python3 scripts/test-ki-native-kanzlei-lauf.py
python3 scripts/test-ki-native-kanzlei-fristen.py
python3 scripts/test-si-native-kanzlei.py
python3 scripts/test-si-native-kanzlei-exporte.py
python3 scripts/audit-skill-activation.py
python3 scripts/validate-yaml-frontmatter.py
node scripts/validate-plugin-structure.mjs
python3 scripts/test-marketplace-import.py
python3 scripts/validate-markdown-structure.py
python3 scripts/quality-lab.py audit
python3 scripts/build-ki-native-kanzlei-handbuch.py --out /tmp/kk339/pdf --font-dir /tmp/kk338/liberation --font-family liberation-serif
python3 scripts/build-ki-native-kanzlei-handbuch.py --out /tmp/kk339/pdf-tnr
```

Der Katalog enthält 13 definierte Szenarien mit 52 Kriterien. Ein vorhandener Katalog ist kein beobachteter Modelltest. Konkrete neue Anwendungsproben und Paketnachweise werden im folgenden Unterabschnitt getrennt dokumentiert.

### 11.4. Ergebnisse und Aussagegrenzen

Alle oben genannten Prüfungen sind bestanden: 35 neue Computerlauf-Tests, 30 Mandatslauf-, 18 Fristen-, 19 Journal-, 16 Export- und 5 Marketplace-Tests. Der globale Aktivierungsaudit erfasst 23.158 Skills; die Strukturvalidierung meldet keine YAML-Fehler oder Warnungen und der Qualitätsaudit 290 vollständige Pluginprofile. Diese globalen Strukturprüfungen sind keine erneute fachliche Rechtsprüfung aller übrigen Plugins.

Die [reproduzierbare Offline-Demo](agentisch-2026-10-08/computerlauf.md) durchlief 22 Schritte mit den drei erwarteten Sperren. Eine [unabhängige Anwendung](agentisch-2026-10-08/anwendungsprobe-bewertung.md) lieferte die angeforderten Arbeitsprodukte und hielt persönliche beA-Handlung, eEB, unklare Sendung und echte Freigabe getrennt. Ergebnisse, Rohdateien und Lese-/Werkzeugprotokoll sind beigefügt; keine behauptete Erfolgsquote über nicht ausgeführte Szenarien.

Zusätzlich wurden `build-ki-native-kanzlei-release.py --dist /tmp/kk339/dist --pdf-dir /tmp/kk339/pdf` und `test-ki-native-kanzlei-pakete.py /tmp/kk339/dist` ausgeführt. Beide Installationspakete sind quellidentisch, Promptdownloads separat; die PDF-Hashes stimmen. Alle 240 Originaldateien stimmen mit dem ursprünglichen Fallakten-Tag überein. [Paketbericht](paket-pruefung.json).

Es gab keinen produktiven Postfachzugriff, keine echte Einreichung, keinen Kalender-Schreibtest und keine produktive Rechnungsausgabe. Ein eingebauter universeller Transport und ein sicherer Geheimnisspeicher sind nicht Bestandteil dieser Fassung. Das Journal lässt sich bei entsprechenden Schreibrechten verändern und ist keine technisch erzwungene Sicherheitsgrenze. Die Warnungen und die Abhängigkeit von tatsächlichen Hostrechten gehören deshalb zum freigegebenen Funktionsumfang.
