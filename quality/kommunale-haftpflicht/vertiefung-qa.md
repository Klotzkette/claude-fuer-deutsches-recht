# 1. Fallvertiefung Kommunale Haftpflicht

Prüfstand: 5. Oktober 2026. Die Erweiterung ergänzt drei neue Fälle (Kita-Platz, Feuerwehr, Kreisstraßenbaum) und vertieft sämtliche dreizehn Bestandsakten. Es gibt jetzt sechzehn Akten mit 380 nativen Arbeitsdateien. 160 Dateien kommen hinzu; die 220 Originaldateien des veröffentlichten Stands v445.31.3 bleiben byteidentisch. Ihre vollständige Pfad-/SHA256-Liste steht in `vertiefung-altbestand.json` und wird durch den neuen Regressionstest überprüft.

## 1.1. Fachliche Gegenprüfung

Alle sechzehn Akten enthalten einen ausgearbeiteten Word-Klageentwurf. Die zwölf früheren Entwürfe bleiben unverändert; drei neue Fälle und „Fiktives Verletzungsrisiko“ erhalten eigene Entwürfe. Anlagen K1 ff. sind konkret im Text verwendet und auf vorhandene Dokumente zurückgeführt. Der Geburtsschadenentwurf bleibt historisch und durch Vergleich und Zahlung überholt.

Die vier Quellenberichte dieser Vertiefung nennen die tatsächlich geprüften Normen, amtlichen Entscheidungen, Randnummern und Anwendungsgrenzen. Die gegenseitige Fachprüfung führte insbesondere zu einem lückenlosen Feststellungsantrag für weitere materielle Schäden, einem offenen Vertretungsnamen statt einer unbelegten Bürgermeisterperson und einer internen Vertragsauskunft anstelle einer künstlichen Rückversichererkorrespondenz im kleinen Rohrbruchfall. Anschriften aller neuen Bestandsbriefe wurden mit den vorhandenen Briefen abgeglichen. Die neuen Vertragsbedingungen sind ausschließlich fiktive Fallannahmen.

## 1.2. Artefakt- und Sichtprüfung

83 neue Worddateien mit 98 gerenderten Seiten wurden vollständig visuell geprüft. Dazu gehören 24 bearbeitbare Fassungen vorhandener Brief-PDFs. Die 16 Gesamt-PDFs umfassen zusammen 686 Seiten. Die Sichtprüfung deckt alle 380 Einzel-PDFs und 16 Gesamt-PDFs ab, insgesamt 1.133 Seitenvorkommen. Bereits tatsächlich gesichtete Seiten wurden nur bei bestätigter identischer RGB-Pixelfolge, gleichen Abmessungen und passenden PNG-Dateihashes übernommen. Neue unterschiedliche Seiten wurden einzeln in Originalauflösung angesehen.

| Gruppe | PDFs | Seitenvorkommen | SHA256 des abschließenden PDF-Prüfnachweises |
| --- | ---: | ---: | --- |
| Kita und Verletzungsrisiko | 144 | 414 | `24d7ac57a0c15940821b9c01cccf26ab78b641093008002ee312833172fbf5c8` |
| Feuerwehr | 117 | 333 | `49d2b7ac04f84b5c82f173dd7f20dc51bd184e54e78540e63a8b8ab3953c7a9e` |
| Kreisstraße | 135 | 386 | `79e1cc0ab1a27e94419848137ab61b7be96039adcbcff87408c8b8bc9836a5c0` |

Die Quellen-/PDF-Freigabe umfasst exakt 396 Dateien einschließlich der 16 Gesamt-PDFs. SHA256 des Freigabeverzeichnisses: `6a506d982afdfdbfd8f86eb4e3796a7a51762cf91d732de480d4f7e4f6aabff3`. Die vollständigen Prüfnachweise werden dem gesonderten Release-Build als gehashte Belege mitgegeben.

## 1.3. Technische Prüfungen

21 Integrationsprogramme sind bestanden, einschließlich Plugin-/Marketplace-Struktur, YAML, gesamter Aktenbestand, Dokumentqualität, README-Navigation, Downloadhinweise, Exportfilter, Promptprofile und kommunaler Fachregressionen. Die neue Vertiefungsregression enthält neun Prüfungen zu Bestandswahrung, genauem Dateiumfang, vollständigem Word-/PDF-Text, bearbeitbaren Altbriefen, MIME-Inhalten, K-Belegen, Lesezeichen, aktuellen README-Seitenzahlen und beiden ZIP-Formaten. Die 43 Offline-Tests der getrennten Releasehelfer sind ebenfalls bestanden.

Bei der Codeprüfung wurden zehn überlange MIME-Grenzen entdeckt und durch kurze deterministische Kennungen ersetzt. Decodierte Kopfzeilen, Textkörper und sämtliche Anlagenbytes blieben unverändert. Die kanonische PDF-Konvertierung aller zehn korrigierten E-Mails wurde erneut ausgeführt und lieferte exakt dieselben Bytes wie die bereits visuell freigegebenen PDFs. Die betroffenen nativen ZIPs wurden neu gebaut. Eine ausdrückliche Längenprüfung verhindert den Fehler künftig.

Die Word-/PDF-Fassungen eines Briefs erhalten unterscheidbare Lesezeichen. Dateien und E-Mail-Anlagen werden nicht als weitere unabhängige Beweise oder Schäden gezählt. Historische Dateizahlen sind als Grundbestand ausgewiesen; sämtliche aktuellen Gesamtseitenzahlen werden gegen die tatsächlich erzeugten PDFs geprüft. Kein Schreiben und kein Klageentwurf wurde versandt oder eingereicht.
