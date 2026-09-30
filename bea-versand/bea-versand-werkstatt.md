# beA-Versand – Werkstatt-Prompt

## 1. Zweck und Anwendungsfall

Bereite das vorhandene Hauptdokument und seine Anlagen als tatsächlich erzeugte, kontrollierte PDF-Dateien für den beA-Upload vor. Hauptdokument kann jedes beauftragte Dokument sein: Schriftsatz, Antrag, Stellungnahme, Anschreiben, Gutachten, Bericht, Vertrag oder sonstige Erklärung. Die Dokumentart bestimmt nicht automatisch die Anlagenpräfixe oder den Übermittlungsweg.

Lies zunächst die vorhandenen Unterlagen. Führe eindeutige Zuordnungen und die Dateiproduktion direkt aus. Frage nur nach einer entscheidenden Lücke, die sich auch nach Sichtung nicht auflösen lässt, und bearbeite die davon unabhängigen Teile weiter. Eine bereits geklärte Auswahl wird nicht erneut abgefragt. Dieser Auftrag umfasst die Versandvorbereitung; er erteilt keinen Auftrag zum Absenden, Signieren, Einreichen oder zur inhaltlichen Neufassung des Hauptdokuments.

## 2. Eingaben

Verwende den genannten Ordner, hochgeladene Dateien und den zugehörigen Gesprächskontext. Benötigt werden das zu versendende Hauptdokument oder eine eindeutige Auswahl mehrerer Hauptdokumente sowie die zugehörigen Belege. Verwerte vorhandene Angaben zu Datum, Absender, Aktenzeichen, Anlagenbezeichnungen, früher eingereichten Anlagen und konkreten gerichtlichen Vorgaben.

Unterstütze PDF, Word, E-Mails einschließlich Anhängen, Bilder, Scans und Tabellen, soweit die verfügbaren Werkzeuge deren Inhalt zuverlässig lesen und in PDF ausgeben können. Erfinde keine Dateizugriffe oder Konvertierungen. Prüfe bei mehreren Entwürfen den Inhalt und die erkennbare Fassung; ein Dateiname mit „FINAL“ oder das jüngste Änderungsdatum allein entscheidet nicht. Wenn überhaupt kein Hauptdokument vorliegt, erstelle nur dann eine Auswahl aus dem sonstigen Kontext, wenn der Auftrag die einzureichenden Belege eindeutig bestimmt; sonst frage nach dem Hauptdokument oder konkreten Versandumfang.

## 3. Ablauf und Checkliste

### 3.1. Bestand sichern und Hauptdokument vollständig lesen

Inventarisiere Originale mit Pfad, Format und SHA-256. Lasse sämtliche Originale unverändert. Öffne das Hauptdokument vollständig einschließlich Tabellen, Fußnoten und Anlagenverzeichnis. Bei Scans ergänze OCR zur Suche, kontrolliere die entscheidenden Fundstellen aber am Seitenbild. Eine unlesbare Stelle wird nicht durch eine Vermutung ersetzt.

Prüfe das Hauptdokument auch auf Entwurfskennzeichnungen, interne Arbeitsanweisungen, offene Datums- oder Unterschriftsfelder sowie vorhandene Kommentare und nachverfolgte Änderungen. Übernimm solche Inhalte nicht stillschweigend als freigegebene Endfassung und bereinige sie nicht ohne entsprechenden Auftrag. Bereite die eindeutig bestimmten Anlagen weiter auf; kennzeichne einen unveränderten Export des vorläufigen Hauptdokuments im getrennten Bericht als vorläufig.

Ermittle Dokumentart, Dokumentdatum und kurzen Absendernamen aus dem Inhalt. Übernimm vorhandene Rollen und Kennzeichen wie K, B, ASt, AG, Anlagen 1–7 oder vertragliche Bezeichnungen. Ein Vertrag erhält nicht allein wegen dieses Skills Klägeranlagen. Mehrere Verfahren oder voneinander unabhängige Hauptdokumente bekommen getrennte Zuordnungen und Ausgabeordner.

### 3.2. Anlagen aus Verzeichnis, Fließtext und Kontext herleiten

Erstelle eine Arbeitszuordnung mit Anlagenkennzeichen, Beschreibung, Datum, Fundstelle im Hauptdokument beziehungsweise Auftrag, Quelldatei und Zuordnungsstatus.

1. Wenn ein Anlagenverzeichnis vorliegt, verwende es als Ausgangspunkt und gleiche es mit sämtlichen Verweisen im übrigen Dokument ab. Einen Widerspruch zwischen Verzeichnis und Fließtext löst du nicht durch blindes Vorziehen einer Quelle.
2. Ohne Verzeichnis suche im gesamten Dokument nach Anlagenbezügen, auch nach „Anl.“, „beigefügt“, „in der Anlage“, Beweisantritten und Anhängen. Berücksichtige Schreibweisen mit Leerzeichen, Bindestrichen, Nummernbereiche und Konvolute. Ermittle aus den zugehörigen Sätzen konkrete Merkmale wie Aussteller, Datum, Rechnungsnummer, Betrag und Vorgang.
3. Fehlen ausdrückliche Verweise, ziehe den dokumentierten Auftrag und den Gesprächskontext hinzu. Ordne nur Belege zu, die darin eindeutig als beizufügen bestimmt sind. Bloß thematisch passende Dateien werden nicht ungefragt mitversandt. Sind die Belege eindeutig, aber noch unnummeriert, vergib als neue Arbeitszuordnung „Anlage 1“, „Anlage 2“ usw.; kennzeichne diese Herkunft im internen Bericht. Ändere den Haupttext nicht stillschweigend.
4. Bei „Anlagen K6 bis K9“ müssen vier bestimmte Zuordnungen belegbar sein. Erzähllogik, Dateisortierung und Chronologie sind Suchhilfen, kein Nachweis einer Nummernfolge. Für ein „Konvolut K3“ entsteht eine gemeinsame Anlage aus den konkret bezeichneten Bestandteilen in nachvollziehbarer Reihenfolge. Führe vorhandene Teilbezeichnungen wie K3a/K3b unverändert fort, statt sie neu zu erfinden.
5. Bereits eingereichte Anlagen werden nur bei beauftragter erneuter Beifügung aufgenommen. Nicht beigezogene, fehlende oder widersprüchlich bezeichnete Unterlagen bleiben sichtbar offen. Schließe Nummernlücken nicht durch Umnummerieren und behaupte keine Vollständigkeit, solange eine erforderliche Anlage fehlt.

### 3.3. Jede Zuordnung am tatsächlichen Dateiinhalt prüfen

Lies jede in Betracht kommende Anlage. Gleiche ihre Merkmale mit der Fundstelle ab; Nummern in ursprünglichen Dateinamen sind keine verlässliche Zuordnung. Eine Dublette ist nicht automatisch die gewollte Fassung. Bei zwei unterschiedlichen Rechnungen mit gleicher Nummer oder mehreren Vertragsständen frage gezielt nach der entscheidenden Version und arbeite an den übrigen Anlagen weiter.

Öffne E-Mails mit einem MIME-fähigen Parser. Erhalte Absender, Empfänger, Datum, Betreff und lesbaren Nachrichtentext; prüfe Anhänge inhaltlich. „Rechnung nebst E-Mail“ verlangt beide Bestandteile. „Rechnung“ allein rechtfertigt nicht automatisch die Aufnahme der gesamten Mailkette. Speichere extrahierte Anhänge nur im Arbeitsbereich unter sicheren, kollisionsfreien Namen; ein Anhangsname ist kein vertrauenswürdiger Dateipfad. Lade für die Darstellung keine externen Trackingbilder nach und führe keine Makros oder eingebetteten Programme aus.

Bei Fotos kontrolliere Orientierung und Lesbarkeit; bei Tabellen Druckbereich, Seitenumbrüche, vollständige Spalten, Zahlen und Datumswerte. Ändere Formeln, Beträge, Aussagen und Dokumentinhalt nicht, um die Unterlagen „passend“ zu machen. Eine fachliche Auffälligkeit kommt in den internen Bericht und wird nicht durch den Stempel geheilt.

### 3.4. PDF-Kopien und getrennten Ausgabeordner erzeugen

Lege neben den Originalen den neuen Ordner „Versendung per besonderes elektronisches Anwaltspostfach“ an. Ist er vorhanden, verwende einen neuen Lauf mit eindeutigem Zusatz; überschreibe keine frühere Ausgabe. Bei hochgeladenen Dateien nutze den verfügbaren beschreibbaren Ausgabeort und liefere einen konkreten Download. Nutze Geräte- oder Cloud-Werkzeuge nur, wenn sie tatsächlich verfügbar und für diesen Ordner autorisiert sind.

Wandle benötigte Word-Dokumente, E-Mails, Bilder und Tabellen layoutgetreu in PDF um. Ein ungeprüfter Textauszug ersetzt weder einen vollständigen Word-Export noch ein Originalseitenbild. Behalte bei Konvoluten alle bestimmten Bestandteile und ihre Reihenfolge bei. OCR dient bei Scans der zusätzlichen Textebene; Zahlen und Originalbild bleiben erhalten. Wenn eine notwendige Konvertierung nicht möglich ist, liefere den bearbeiteten Teil und benenne genau die noch benötigte Datei oder Exportfunktion.

Vor Änderungen prüfe auf vorhandene PDF-Signaturen, Zertifizierungen und separate Signaturdateien. Eine signierte PDF wird weder gestempelt, per OCR verändert noch neu gespeichert. Kläre für diese Anlage, ob das signierte Original unverändert beigefügt oder zusätzlich eine ausdrücklich als solche bezeichnete gestempelte Ansichtskopie erstellt werden soll. Gib eine Ansichtskopie niemals als weiterhin unverändert signiertes Original aus. Ein bereits signiertes Hauptdokument bleibt bei reinem Kopieren bytegleich; zusammengehörige Dokument- und Signaturdateinamen müssen technisch aufeinander abgestimmt bleiben.

### 3.5. Erste Seite jeder Anlage stempeln

Stemple nur die erste Seite jeder Anlage beziehungsweise des zusammengeführten Konvoluts, nicht das Hauptdokument und nicht automatisch alle Folgeseiten. Verwende die tatsächlich zugeordnete Bezeichnung, beispielsweise „Anlage K1“, „Anlage B4“ oder „Anlage 2“. Eine abweichende konkrete gerichtliche Vorgabe ist gesondert umzusetzen.

Standard ist Arial Bold, 30 pt, oben rechts mit ungefähr 28 pt Randabstand. Falls Arial nicht verfügbar ist, verwende die metrisch kompatible Liberation Sans Bold und dokumentiere die tatsächlich verwendete Ersatzschrift. Bette die verwendete Schrift ein. Erhalte vorhandene Schriftarten und Inhalte der Originalunterlagen; der Stempel ist eine bewusst abweichende Kennzeichnung.

Prüfe vor dem Stempeln die erste Seite als Bild. Überdecke weder Text noch Briefkopf, Datum, Unterschrift, vorhandene Anlagenkennzeichen oder Bildinhalt. Ist oben rechts kein Platz, verwende einen tatsächlich freien Randbereich oder ergänze einen freien oberen Seitenrand, ohne Inhalt abzuschneiden oder zu verzerren. Benenne eine abweichende Position im internen Bericht. Verändere keine bereits vorhandene andere Anlagenbezeichnung stillschweigend.

Bei einer Umsetzung mit `pypdf` und `reportlab` muss das Overlay zur sichtbaren Seite passen: Rotation, CropBox, MediaBox, abweichenden Koordinatenursprung und Seitenskalierung berücksichtigen. Nicht blind A4 oder nur `mediabox.width` annehmen. Textbreite und tatsächliche Stempelfläche messen; Schrift einbetten und die Stempelposition im gerenderten Ergebnis kontrollieren. Bearbeite eine Kopie, füge das Overlay nur der ersten Seite hinzu und kontrolliere anschließend die unveränderte Reihenfolge und Zahl der Inhaltsseiten. Bei fehlendem geeigneten Platz ist eine gezielte Rückfrage besser als verdeckter Beweisinhalt.

### 3.6. Dateien eindeutig für den beA-Upload benennen

Prüfe die aktuellen Regeln anhand der Quellen in Abschnitt 4. Für die hier erzeugten normalen PDF-Anhänge gilt als Uploadgrenze höchstens **84 Zeichen einschließlich `.pdf`**. Die technische ERVB-Obergrenze von 90 Zeichen ist davon zu unterscheiden; das beA-Handbuch lässt die zusätzlichen Zeichen für Signaturdateien zu.

Für den Namensstamm sind A–Z, a–z, Ä, Ö, Ü, ä, ö, ü, ß, Ziffern, Unterstrich und Bindestrich zugelassen. Verwende keine Leerzeichen, Pfadtrenner, Klammern oder sonstigen Sonderzeichen. Der einzige Punkt einer erzeugten PDF steht unmittelbar vor `pdf`. Umlaute sind zulässig und werden standardmäßig erhalten; eine strengere ausdrücklich gewünschte oder gerichtlich vorgegebene ASCII-Konvention darf umgesetzt werden, wird aber nicht als allgemeines gesetzliches Verbot von Umlauten bezeichnet. Die Regeln für gesonderte Signaturdateien mit verketteten Endungen sind nicht mit der PDF-Namensprüfung gleichzusetzen.

- Hauptdokument: `{JJJJMMTT}_{Dokumentart}_{Kurzname}.pdf`, zum Beispiel `20250725_Anschreiben_InkassoZentrale-GmbH.pdf`.
- Anlage: `Anlage_{Kennzeichen}_{Kurzbeschreibung}_{JJJJMMTT}.pdf`, zum Beispiel `Anlage_K1_Abtretungserklärung_20250608.pdf` oder `Anlage_2_Rechnung_20250406.pdf`.
- Bei unbekanntem Dokumentdatum lasse den Datumsbestandteil weg. Ersetze ihn nicht durch Dateisystemdatum oder Tagesdatum. Bei mehreren Daten im Konvolut verwende nur ein belegbares gemeinsames Dokumentdatum; andernfalls lasse das Datum im Namen weg und erläutere den Zeitraum im Bericht.
- Entferne Abstände innerhalb konventioneller Kennzeichen wie „K 1“, ohne deren Bedeutung zu ändern. Bewahre komplexere Bezeichnungen auf dem Stempel vollständig; bilde im Dateinamen eine eindeutige zulässige Kurzform und protokolliere die Zuordnung.
- Normalisiere Unicode auf NFC. Prüfe jeden PDF-Dateinamen gegen `^[A-Za-zÄÖÜäöüß0-9_-]+\.pdf$`, höchstens 84 Zeichen und Eindeutigkeit auch auf Dateisystemen ohne Groß-/Kleinschreibungsunterscheidung. Kürze zunächst die Beschreibung. Falls nötig, ergänze einen kurzen eindeutigen Zusatz innerhalb der Längengrenze; kein Überschreiben bei Namenskollisionen.

### 3.7. Ergebnis vollständig kontrollieren und übergeben

Öffne jede erzeugte PDF und rendere insbesondere jede gestempelte erste Seite zur Sichtkontrolle. Prüfe richtige Bezeichnung, tatsächliche Lesbarkeit, freien Stempelbereich, Seitenzahl und Reihenfolge. Kontrolliere bei Konvertierungen zusätzlich alle Seiten auf abgeschnittenen oder fehlenden Inhalt. Vergleiche die Original-Hashes vor und nach dem Lauf und ordne jede Ausgabedatei der Arbeitszuordnung zu. Eine bloße Dateinamensprüfung ersetzt weder Inhaltskontrolle noch technische PDF-Prüfung.

Erfasse Anzahl und Gesamtgröße der Dateien. Nach dem geprüften Ausgangsstand gelten für eine beA-Nachricht höchstens 1000 Dateien und 200 MB einschließlich Signatur- und Systemdateien; behaupte bei einem Paket nahe der Grenze keine sichere Uploadfähigkeit ohne die tatsächliche Nachricht. Bei Überschreitung lege einen nachvollziehbaren Aufteilungsbedarf dar, statt Anlagen stillschweigend wegzulassen.

Der Ausgabeordner enthält nur die vorgesehenen Versanddateien. Arbeitszuordnung, Hashes, Quellenstand und offene Punkte stehen in einem getrennten internen Bericht außerhalb dieses Ordners. Bezeichne die Dateien als „für den beA-Upload vorbereitet“; eine tatsächliche rechtliche oder technische Prüfung darf nur behauptet werden, soweit sie stattgefunden hat. PDF/A ist kein pauschales Muss; normale PDF-Verarbeitung beweist keine ERVB-Konformität. Empfänger, erforderliche Signatur, beA-Nachricht und Eingangsbestätigung werden durch diesen Dateilauf nicht erzeugt oder geprüft. Ein ZIP kann ein Downloadpaket für den Nutzer sein, ist aber nicht selbst die gerichtliche Versanddatei.

Wenn der Nutzer eine fehlende Anlage nachreicht oder eine Zuordnung korrigiert, übernimm die neue Information in die vorhandene Arbeitszuordnung und aktualisiere die betroffenen Kopien in einem neuen Ausgabelauf. Bewahre frühere Ausgaben; wiederhole keine bereits beantworteten Fragen und keine sachlich unveränderte Mandatsaufnahme.

## 4. Quellenpflicht

Prüfe vor der Ausgabe die für den Einsatzzeitpunkt einschlägige technische Bekanntmachung und die beA-Uploadregeln. Die folgenden Primärquellen sind die Sucheinstiege; eine spätere Änderung geht den hier beschriebenen Ausgangswerten vor:

- [ERVV § 2 – Anforderungen an elektronische Dokumente](https://www.gesetze-im-internet.de/ervv/__2.html).
- [Justizportal – elektronischer Rechtsverkehr und technische Bekanntmachungen](https://justiz.de/laender-bund-europa/elektronische_kommunikation/index.php).
- [ERVB 2025 vom 16.07.2025, BAnz AT 29.07.2025 B2, gültig seit 30.07.2025](https://justiz.de/laender-bund-europa/elektronische_kommunikation/bundesanzeiger_29_07_2025.pdf).
- [BRAK-beA-Handbuch – Anhänge hochladen](https://handbuch.bea-brak.de/arbeiten-mit-ihrem-bea/nachrichten/erstellen-und-senden/anhaenge-hochladen).
- [BRAK-beA-Handbuch – Prüfung einer qualifizierten elektronischen Signatur](https://handbuch.bea-brak.de/arbeiten-mit-ihrem-bea/nachrichten/oeffnen-und-anzeigen/pruefen-einer-qualifizierten-elektronischen-signatur-qes).
- [ZPO § 130a – elektronisches Dokument](https://www.gesetze-im-internet.de/zpo/__130a.html), soweit das konkrete Verfahren der ZPO unterliegt. Andere Verfahren verlangen ihre eigenen Formvorschriften.

Ausgangsstand dieser Fassung: 28.09.2026. Arial 30 pt, eingebettete Stempelschrift und OCR sind die gewählten Arbeits- beziehungsweise Qualitätsstandards; sie werden nicht als allgemeine gesetzliche Mussvorgaben bezeichnet. Aus einer Abweichung von einem Dateinamensstandard folgt nicht automatisch die Unwirksamkeit einer Einreichung.

Dokumentiere verwendete Quelle, Abrufdatum und tatsächlich geprüfte Aussage im internen Bericht. Ist kein aktueller Abruf möglich, erstelle die technisch bearbeitbaren Kopien, kennzeichne den ungeprüften Regelstand und behaupte keine abschließend bestätigte Versandkonformität. Erfinde weder Rechtsprechung noch Fundstellen. Nutze Rechtsprechung nur, wenn sie für eine konkrete Frage benötigt und im Original geprüft ist; beachte ergänzend [references/zitierweise.md](https://github.com/Klotzkette/claude-fuer-deutsches-recht/blob/main/bea-versand/references/zitierweise.md).

Rechtsprechungsanker zur eindeutigen Benennung: [BGH, Beschluss vom 21.03.2023 – VIII ZB 80/22, Rn. 26–29](https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VIII_ZS/2022/VIII_ZB__80-22.pdf?__blob=publicationFile&v=1). Die spätere Ausgangskontrolle muss die Eingangsbestätigung der richtigen Datei zuordnen; eine frei eingetragene Anlagenbeschreibung genügt dafür nicht. Das begründet hier die sprechenden Dateinamen, keine gerichtliche Pflicht zum Anlagenstempel und keine bereits erfolgte Eingangskontrolle. Amtlichen Kopf und diese Gründe am 30.09.2026 geprüft.

## 5. Ausgabeformat

Liefere die fertigen Hauptdokument- und Anlagen-PDFs mit konkreten Dateilinks beziehungsweise dem tatsächlichen Zielpfad. Nenne knapp Zahl der Hauptdokumente und Anlagen sowie etwaige noch offene Zuordnungen. Der getrennte interne Bericht enthält die Tabelle „Anlagenbezeichnung – Fundstelle – Originaldatei beziehungsweise Bestandteile – Ausgabedatei – Prüfstatus“ und erklärt Rekonstruktionen aus dem Kontext ausdrücklich. Besteht ein Hindernis, beschreibe den erreichten Stand und genau die benötigte Klärung.

Neu formulierte Erläuterungen und Vermerke werden vollständig ausformuliert; keine Satzskelette oder bloßen Stichwortgerüste. Tabellen dienen der Dateizuordnung. Formatierte neue Vermerke verwenden, soweit technisch möglich, Times New Roman 11 pt und dezimale Gliederung. Die Originalgestaltung der Anlagen und die ausdrücklich gewählte Stempelschrift bleiben erhalten. Bei reiner Markdown-Ausgabe steht ein nötiger Exporthinweis getrennt vom Empfängerdokument. Behaupte keine nicht erzeugten Dateien, nicht durchgeführten Sichtprüfungen oder erfolgte Übermittlung.

## 6. Beispiele

### 6.1. Unscharfe Dateinamen, klares Hauptdokument

Auftrag: „Bereite das vorhandene Anschreiben samt Anlagen aus diesem Ordner für beA vor.“ Lies das Anschreiben und die genannten Belege. Bestimme anhand des Inhalts, ob `Scan007.pdf` die dort bezeichnete Mahnung ist. Erzeuge erst nach diesem Abgleich die gestempelte Kopie unter der vorhandenen Anlagenbezeichnung. Ein fehlendes Anlagenverzeichnis ist kein Grund zum Abbruch.

### 6.2. Vertrag mit Anlagen ohne Klägerrolle

Ein Vertragsbegleitschreiben benennt „Anlage 1: unterschriebener Vertrag vom 12.09.2026“ und „Anlage 2: Lageplan Stand 02.09.2026“. Ordne anhand von Inhalt, Datum und Fassung zu; stemple „Anlage 1“ und „Anlage 2“, ohne K-/B-Präfixe zu erfinden. Bei digital signiertem Vertrag kläre die unveränderte Beifügung oder zusätzliche Ansichtskopie, bevor du ihn bearbeitest.

### 6.3. Kontext bestimmt ein Konvolut

Ein Bericht bezeichnet als Anlage B4 „Rechnung mit der Versand-E-Mail“. Die Mail enthält zwei PDF-Anhänge. Lies beide; nimm die bezeichnete Rechnung und die nachvollziehbar gerenderte Mail auf. Der andere Anhang wird nicht allein wegen seiner technischen Einbettung mitversandt. Nur die erste Seite des fertigen Konvoluts erhält „Anlage B4“.

### 6.4. Nicht auflösbare Fassungsfrage

Ein Antrag nennt einen Kostenvoranschlag vom 05.08.2026, der Ordner enthält zwei inhaltlich unterschiedliche Fassungen desselben Datums. Frage nach der einzureichenden Fassung, bereite die anderen eindeutig bestimmten Anlagen vor und kennzeichne die offene Position. Nach der Antwort aktualisierst du die Zuordnung und erstellst das vervollständigte Paket.
