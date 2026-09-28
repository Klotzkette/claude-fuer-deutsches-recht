# 1. beA-Versand: Prüfung am 28.09.2026

## 1.1. Gegenstand und Methode

Geprüft wurde das neue Plugin `bea-versand` mit genau einem Skill `bea-anlagen-versand` und einem handkuratierten Werkstatt-Prompt in den byteidentischen Formaten MD und TXT. Die Ausgangsvorlage wurde für beliebige Hauptdokumente verallgemeinert. Die Prüfung umfasste redaktionelle Kontrolle, aktuelle Primärquellen, zwei manuell ausgeführte agentische Anwendungsläufe mit echten PDF-Ausgaben und technische Regressionen der Promptveröffentlichung. Sie ist keine automatische Modellbewertung und kein Nachweis universeller ERVB-Konformität.

## 1.2. Modefuchs: tatsächliche Dateiproduktion

Ein unabhängiger Agent erhielt den Skill und ausschließlich die zehn Originaldateien der bestehenden Cowork-Sonderfallakte. Akten-README, Bewertungsrubrik, vorhandenes Gesamt-PDF und frühere Testausgaben wurden nicht als Lösung herangezogen. Das Hauptdokument und die Belege wurden tatsächlich gelesen; die Scans und das Foto wurden visuell ausgewertet.

Erzeugt wurden acht PDF-Dateien mit 13 Seiten: das vierseitige Hauptdokument sowie sieben Anlagen mit insgesamt neun Seiten. K1 enthält die Abtretung, K2 die Bestellbestätigung, K3 den echten Rechnungs-MIME-Anhang samt Übersendungsmail, K4 die Zahlungserinnerung, K5 die Mahnung vom 05.05.2025, K6 die Mahnung vom 22.05.2025 samt Einlieferungsfoto und K7 die Schuldner-E-Mail. Das interne Excel-Forderungskonto wurde nicht als zusätzliche Anlage aufgenommen. Der irreführende Scan-Dateiname vom 10.06.2025 wurde nicht zum Dokumentdatum der Mahnung erklärt.

Jede erste Anlagenseite erhielt einen sichtbaren Stempel in eingebettetem Arial Bold mit 30 pt. Hauptdokument und Konvolut-Folgeseiten blieben ungestempelt. Alle sieben Stempelseiten, beide Konvolut-Folgeseiten und die vier Hauptdokumentseiten wurden tatsächlich angesehen. Die Mailtexte und Kopfwerte waren vollständig enthalten; sämtliche DOCX-Absätze einschließlich der Anlagentabelle waren im Export nachweisbar. Die Scanbilder ließen sich nach der Stempelung bytegleich extrahieren. Alle zehn Originaldateien waren im Vorher-/Nachher-SHA-256-Vergleich unverändert.

Die Dateinamen waren NFC-normalisiert, auch ohne Groß-/Kleinschreibungsunterscheidung eindeutig und höchstens 60 Zeichen lang. Die acht PDFs waren insgesamt 3.471.235 Byte groß. Ausgabezuordnung, Seitenzahlen, Stempeldaten und Hashes stehen im [Praxistest-Manifest](praxistest-manifest.json). Die lokalen Testausgaben sind keine zusätzlichen Aktenoriginale und werden nicht in das Plugin installiert.

Der Hauptentwurf enthält interne Bearbeitungsanweisungen sowie offene Datums- und Unterschriftsfelder. Diese wurden nicht heimlich entfernt oder ergänzt. Daraus folgte eine konkrete Verbesserung von Skill und Werkstatt: sichtbare Entwurfsvermerke, Platzhalter, Kommentare und nachverfolgte Änderungen ausdrücklich prüfen und einen vorläufigen Hauptdokumentexport im getrennten Bericht kennzeichnen. Die finale Textfassung wurde nach dieser gezielten Ergänzung redaktionell geprüft; eine erneute vollständige Modellmessung wird nicht behauptet.

## 1.3. Generalisierung ohne Klage und ohne Anlagenverzeichnis

Ein zweiter Agent erzeugte für einen getrennten lokalen Test einen nichtprozessualen Prüfbericht mit verstreuten Verweisen. Eine Rechnung und eine Abtretung waren eindeutig bezeichnet; eine weitere Mahnung war absichtlich ohne unterscheidendes Datum genannt. Als Belege dienten tatsächlich vorhandene Modefuchs-Originale und der echte PDF-MIME-Anhang.

Der Lauf erzeugte drei PDFs mit insgesamt 411.486 Byte: die bytegleich übernommene Haupt-PDF und zwei gestempelte PDFs als neutrale „Anlage 1“ und „Anlage 2“. Es entstanden keine K-/B-Rollen und kein erfundenes Anlagenverzeichnis. Alle drei endgültigen Seiten wurden tatsächlich angesehen. Beide Belegseiten waren beim Vergleich mit 144 dpi außerhalb der Stempelflächen pixelidentisch; Arial Bold mit 30 pt war eingebettet.

Die undatierte Anlage 3 blieb offen, weil zwei unterschiedliche Mahnungen zum Verweis passten. Es entstand keine zusätzliche Versanddatei. Der Bericht stellte die konkrete Fassungsfrage und unterschied fertige Teile vom noch unvollständigen Gesamtpaket. Die zehn Repository-Originale blieben unverändert. Dieser Zusatzlauf prüft keine Rotation, keine Mehrseitenkonvertierung und keine Signaturvalidierung.

## 1.4. Quellen und Grenzen

Die aktuelle Bekanntmachungsübersicht, ERVB 2025, § 2 ERVV, § 130a ZPO und die einschlägigen BRAK-Handbuchseiten wurden am 28.09.2026 tatsächlich abgerufen. Die einzelnen geprüften Aussagen und Quellen sind im [Prüfprofil](../evals/bea-versand.json) dokumentiert. Für normale beA-Anhänge wird die Uploadgrenze von 84 Zeichen einschließlich Endung von der 90-Zeichen-Grenze für Signaturdateien getrennt. Umlaute sind erlaubt, PDF/A ist keine pauschale Pflicht. Stempelschrift und zusätzliche OCR sind Qualitätsentscheidungen dieses Workflows.

Es wurde nichts signiert, hochgeladen, versendet oder eingereicht. Die vorhandenen Entwurfs- und Rechenwidersprüche der Testakte wurden als Quellenbefunde belassen; ihre README beschreibt sie jetzt zutreffend. Die Originale der Testakte wurden nicht verändert. Die automatische Profilprüfung kontrolliert Veröffentlichung, Dateiumfang, MD-/TXT-Identität und Paketgrenzen; sie ersetzt keine inhaltliche Sichtung beliebiger neuer Akten.
