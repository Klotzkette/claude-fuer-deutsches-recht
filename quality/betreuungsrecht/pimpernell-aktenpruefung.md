# 1. Prüfung der Originalakte Pimpernell

Stand: 08.10.2026. Dieser redaktionelle Nachweis liegt außerhalb der ausgelieferten Testakte.

## 1.1. Bestand

Der Aktenbuilder erzeugt 205 Originaldateien: 161 PDF-Dokumente, acht Word-Dokumente, vier Bildschirmabbildungen und 32 E-Mails. Zusammen mit den zwei separat erzeugten Excel-Dateien enthält die Akte 207 Originaldateien. Die Akten-README zählt nicht als Aktenstück. Unter den PDFs sind 72 monatliche Kontoauszüge für Giro- und Sparkonto, 83 Rechnungen und Quittungen, fünf Jahresabrechnungen und eine Bestellungsmitteilung. Die Original-PDFs umfassen 195 Seiten; die Gesamtlesefassung wird anschließend durch den zentralen Builder erzeugt.

Die Rechnungen und Kontoauszüge enthalten ihre Beleg- beziehungsweise Buchungsreferenzen. Die E-Mails führen gültige MIME-Header, eindeutige Message-IDs, das Datum mit der Zeitzone Europe/Berlin und ausgewählte tatsächliche Originalanhänge. Der letzte Aktenbuild wurde nach dem endgültigen Export der Excel-Dateien ausgeführt. Der Bankexport ist daher auch als E-Mail-Anhang bytegleich enthalten.

## 1.2. Fachliche Konstruktion

Die Akte enthält 584 Kontobewegungen zwischen dem 01.10.2023 und dem 30.09.2026. Anfangs- und Endbestände sind je Konto und Monat fortgeschrieben. 30 Buchungszeilen bilden 15 interne Umbuchungen ab. Die getrennten Kontrollwerte in `pimpernell-kontrollwerte.json` belegen die Kontenüberleitung; sie sind keine Dateien der Testakte.

Belegbetrag und Überweisung müssen nicht immer identisch sein: Die Fensterrechnung W-24051 über 3.600 EUR steht einer Überweisung von 4.200 EUR an den Sohn und einer Rückzahlung von 600 EUR gegenüber. Der Leistungsort liegt am Haus des Sohnes. Ob die verbleibende Zuwendung ein Geschenk oder ein zurückzuzahlender Betrag war, bleibt nach den unterschiedlichen Erinnerungen offen. Die Akte enthält keine Musterlösung und keinen abschließenden Missbrauchsbefund.

Bargeldabhebungen werden nicht als belegte Verbrauchsausgaben ausgegeben. Erstattungen und Doppelabbuchung sind eigenständige Bewegungen. Ein ausdrücklich gewünschtes Streamingangebot steht neben ungeklärten Bestellungen. Ein gerichtlich nicht bestellter Helfer behauptet unterschiedliche Gründe für Zahlungen; die Betreute äußert eigene Wünsche. Die Unterlagen verknüpfen diese Angaben, ohne sie als bewiesen zusammenzufassen.

## 1.3. Format und Prüfung

Alle acht Word-Dokumente wurden mit dem im Documents-Skill vorgegebenen `render_docx.py` und der gebündelten LibreOffice-Version gerendert. Jede der acht Seiten wurde geöffnet und visuell geprüft. Bei der ersten Sichtprüfung aufgefallene Theme-Schriften und eine blaue Titellinie wurden aus der Word-Vorlage entfernt. Die abschließenden Fassungen verwenden Times New Roman mit 11 pt im Text, schwarze Titel und keine Titellinie. Alle Word-Dokumente haben eine Seite und keine abgeschnittenen Texte.

Für sämtliche 161 Original-PDFs wurden die extrahierten Textbegrenzungen gegen die Seitengrenzen geprüft; kein Textblock liegt außerhalb der Seite. Giroauszug einschließlich Folgeseite, Sparauszug, Haushaltshilfe-, Handwerker- und Geräterechnung sowie Betriebskosten- und Stromabrechnung wurden zusätzlich als Seitenbilder geöffnet. Alle vier Bildschirmabbildungen wurden geöffnet. Keine Überlappung oder fehlenden Zeichen fiel auf. Die Abbildungen zeigen erfundene Anwendungen; ihre Einordnung steht in der Akten-README.

Der Regressionslauf `python3 scripts/test-betreuungsrecht-unterlagen.py` war nach dem letzten Originalbuild erfolgreich: acht aktive Tests und ein zum damaligen Stand erwartungsgemäß übersprungener Pakettest. Die anschließende Paket- und Gesamt-PDF-Prüfung wird im übergeordneten Releasebericht nachgetragen.

Die unabhängige Anwendungsprobe fand anschließend eine versehentliche Monatsangabe in der E-Mail vom 12.08.2026. Der dort rückblickend erwähnte Monat wurde vor dem PDF-Build von September auf Juli berichtigt; EML und Generator stimmen überein.

## 1.4. Reproduktion

`python3 scripts/build-betreuung-pimpernell.py --data-only` erzeugt die kanonischen Quelldaten. Danach erzeugt der Tabellenbuilder die Excel-Dateien. Abschließend führt `python3 scripts/build-betreuung-pimpernell.py` den Originalbuild mit aktuellen Anhängen aus. Die Dokumentenerzeugung benötigt ReportLab, python-docx und PyMuPDF. Times New Roman wird aus den installierten Systemschriften geladen; als ausdrücklicher technischer Ersatz ist Liberation Serif vorgesehen. Vor einer Auslieferung sind der zentrale Gesamt-PDF-Builder und die beiden ZIP-Builder zusätzlich auszuführen.
