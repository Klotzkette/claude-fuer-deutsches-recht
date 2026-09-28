# Form- und Technikregeln für die Versandmappe

Stand: 28. September 2026. Das Justizportal führt weiterhin die ERVB 2025 als aktuelle Bekanntmachung. Vor einem fristgebundenen Versand sind Normtext, Bekanntmachung und gerichtliche Sonderhinweise erneut zu prüfen.

## 1. Zweck

Diese Referenz hält ausschließlich formale und technische Versandregeln fest. Sie bewertet weder Anträge noch Sachvortrag, Beweisangebote oder materielles Recht.

## 2. Dokumentformat

ERVV Paragraf 2 verlangt grundsätzlich PDF. TIFF darf zusätzlich übermittelt werden, wenn bildliche Darstellungen in PDF nicht verlustfrei wiedergegeben werden können. PDF/A ist nicht generell vorgeschrieben. Das Versandwerkzeug prüft insbesondere Lesbarkeit, Verschlüsselung und bestimmte aktive oder eingebettete Inhalte; diese Teilprüfungen bescheinigen keine vollständige ERVV-Konformität. Kaum auslesbarer Text ist ein Qualitätsbefund, kein selbständiger Nachweis der Formunwirksamkeit. Jede Seite zusätzlich sichtbar auf Vollständigkeit prüfen.

Bereits elektronisch signierte Originale nicht automatisch stempeln, per OCR bearbeiten, zusammenführen oder neu ausdrucken. Unveränderte Bezugsdateien und abgesetzte Signaturdateien erhalten; Signaturstatus extern prüfen und dokumentieren. Eine byteidentische Kopie beweist allein keine gültige qES. Bei E-Mail-Quellen müssen Nachricht und Anhänge einzeln zugeordnet oder begründet ausgeschlossen werden; ein Textauszug erfasst die Anhänge nicht automatisch.

Amtlicher Normtext: https://www.gesetze-im-internet.de/ervv/__2.html

## 3. ERVB 2025

Die ERVB 2025 vom 16. Juli 2025 begrenzt eine Nachricht auf höchstens 1.000 Dateien und 200 Megabyte. Ein Dateiname darf einschließlich Endung höchstens 90 Zeichen lang sein. Erlaubt sind Buchstaben des deutschen Alphabets einschließlich Umlauten und scharfem S, Ziffern, Unterstrich und Minus sowie der Punkt als Trenner vor der Dateiendung.

Dieses Plugin verwendet bewusst ein strengeres Kanzleiprofil: ausschließlich ASCII, Wörter mit Unterstrich verbunden und höchstens 80 Zeichen einschließlich `.pdf`. Das ist eine interne Robustheitsregel, keine Behauptung über die gesetzliche Höchstgrenze.

Das beA-Handbuch nennt für gewöhnliche Anhänge eine Anwendungsgrenze von 84 Zeichen, für Signaturdateien 90 Zeichen einschließlich aller Endungen. Strukturdatei, Nachrichtentext und Signaturdateien zählen bei Größe und Anzahl mit. Dateien logisch nummerieren und Versandreserve lassen; die fertige Nachricht im Versanddialog prüfen. Das Werkzeug verwendet vorsorglich 200 Millionen Bytes und warnt ab 190 Millionen Bytes oder 950 Dateien. Diese Reserve ist keine zusätzliche gesetzliche Grenze.

Betriebsinformation: https://handbuch.bea-brak.de/arbeiten-mit-ihrem-bea/nachrichten/erstellen-und-senden/anhaenge-hochladen

Amtliche Bekanntmachung: https://justiz.de/laender-bund-europa/elektronische_kommunikation/bundesanzeiger_29_07_2025.pdf

## 4. Signaturroute

Für Zivilverfahren bestimmt ZPO Paragraf 130a Absatz 3 zwei alternative Formwege:

1. qualifizierte elektronische Signatur der verantwortenden Person oder
2. Signatur durch die verantwortende Person und Einreichung auf einem sicheren Übermittlungsweg.

Anlagen zu vorbereitenden Schriftsätzen sind nach Satz 2 von dieser Signaturanforderung ausgenommen. Eigenständige Formanforderungen bleiben unberührt. Für andere Verfahren insbesondere ArbGG Paragraf 46c, SGG Paragraf 65a, VwGO Paragraf 55a, FGO Paragraf 52a oder StPO Paragraf 32a gesondert lesen; die ZPO-Ausnahme nicht pauschal übertragen.

Beim persönlichen beA ohne qES müssen verantwortende, einfach signierende und tatsächlich versendende Person übereinstimmen. Mit qES der verantwortenden Person ist Versand durch berechtigtes Personal mit eigenem Zugang möglich; eine zusätzliche einfache Signatur ist dafür nicht zwingend. Gesellschaftspostfächer gesondert nach RAVPV Paragraf 23 Absatz 3 prüfen. Keine anwaltlichen Zugangsmittel weitergeben; RAVPV Paragraf 26 Absatz 1 beachten.

Amtliche Zugangsregeln: https://www.gesetze-im-internet.de/ravpv/__23.html und https://www.gesetze-im-internet.de/ravpv/__26.html

Prüfnachweise und ihre Grenzen: https://handbuch.bea-brak.de/arbeiten-mit-ihrem-bea/nachrichten/oeffnen-und-anzeigen/pruefen-einer-qualifizierten-elektronischen-signatur-qes

Amtlicher ZPO-Normtext: https://www.gesetze-im-internet.de/zpo/__130a.html

Das Plugin behandelt den Signaturweg als Stop-Punkt, wenn verantwortende Person, tatsächlicher Versender oder verwendetes Postfach nicht feststehen. Es erzeugt und prüft selbst keine qualifizierte elektronische Signatur.

## 5. Eingang und Störung

ZPO Paragraf 130a Absatz 5 knüpft den Eingang an die Speicherung auf der für den Empfang bestimmten Einrichtung des Gerichts und sieht eine automatisierte Bestätigung vor. ZPO Paragraf 130d regelt die Ersatzeinreichung bei vorübergehender technischer Unmöglichkeit. Das Plugin ersetzt weder die Prüfung der jeweiligen Verfahrensordnung noch die Glaubhaftmachung einer Störung.

Amtlicher Normtext: https://www.gesetze-im-internet.de/zpo/__130d.html

## 6. Nicht automatisierbare Freigaben

1. Verantwortender Anwalt und tatsächlicher Versender bestätigen die gewählte Signaturroute.
2. Jede konvertierte Seite wird visuell mit der Quelle verglichen.
3. Empfänger, Aktenzeichen, Dokumentart und Frist werden im Versanddialog erneut geprüft.
4. Erst die positive automatisierte Eingangsbestätigung beendet die Ausgangskontrolle.
5. Das Werkzeug löst niemals einen Versand aus und löscht niemals eine Frist.
