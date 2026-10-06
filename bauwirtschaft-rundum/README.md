# 1 Bauwirtschaft rundum

Zwei eigenständig installierbare Pakete für die Arbeit in Planungsbüros, Bauüberwachung, Bauleitung und Vergabestellen. Die Grundlagen führen vom konkreten Beleg zum verwendbaren Dokument. Die Vertiefung verbindet mehrere Arbeitsschritte, führt Änderungen nachvollziehbar fort und bereitet Entscheidungen zur fachlichen Freigabe vor.

Der technische Ordnername lautet `bauwirtschaft-rundum`. Dieser Sammelordner ist selbst kein drittes Plugin. Die vorhandenen Pakete [Bauwirtschaft](../bauwirtschaft/README.md) und [Bauvergabe](../bauvergabe/README.md) bleiben erhalten.

## 1.1 Welches Paket passt?

| Paket | Für wen und wofür? | Einstieg |
| --- | --- | --- |
| [Bauwirtschaft für Anfänger](./bauwirtschaft-anfaenger/README.md) | Einzelne Projektunterlagen verlässlich bearbeiten: Begehungsprotokoll, Planungsabgleich, Bieterfragen, Behinderungsanzeige und Baugrundanforderungen. Dazu Dokumentenzugriff begrenzen und einen eigenen wiederverwendbaren Arbeitsbaustein entwickeln. | Einen Fall und ein gewünschtes Dokument auswählen; nicht erst den ganzen Projektordner zusammenfassen lassen. |
| [Bauwirtschaft für Fortgeschrittene](./bauwirtschaft-fortgeschrittene/README.md) | Rechnungen abgleichen, VgV-Bewerbungen vorbereiten, Angebote prüfen, Bauzeit-Claims bearbeiten und Nachträge entscheidungsreif vorlegen. Dazu Planänderungen verfolgen und Bürostandards kontrolliert einsetzen. | Einen konkreten Prüfauftrag mit vorhandener Akte beginnen; neue Unterlagen anschließend in denselben Vorgang übernehmen. |

Jedes Paket enthält acht Skills, einen separaten ausführlichen Werkstatt-Prompt und einen Mini-Prompt unter 7500 Bytes. Die Prompts sind Alternativen zur Plugin-Nutzung, keine zusätzlich zu ladenden Pflichtdateien. Die fünf Fallakten je Paket entsprechen den zehn Beispielen aus der Seminar-Fallbeschreibung. Werkstätten und Akten werden nicht mit den Plugin-ZIPs installiert.

## 1.2 In drei Schritten beginnen

1. Das passende Paket über seine Detailseite installieren oder dort einen einzelnen Werkstatt- beziehungsweise Mini-Prompt als Markdown herunterladen.
2. Eine Fallakte in genau einer Fassung verwenden: Gesamt-PDF zum Lesen, Einzel-PDF-ZIP für getrennte Dokumente oder Originalformat-ZIP für die Arbeit mit E-Mails, Tabellen und bearbeitbaren Bürodateien.
3. Den konkreten Auftrag nennen, etwa „Erstellen Sie den Entwurf des Begehungsprotokolls mit offenen Punkten“ oder „Prüfen Sie die dritte Abschlagsrechnung und erstellen Sie einen Prüfvermerk“. Bereits erkennbare Angaben werden aus den Dokumenten übernommen. Fehlende entscheidende Angaben werden gezielt nachgefragt.

Ein zweiter Durchgang mit einer ergänzten Unterlage prüft die Fortsetzung: Der Arbeitsstand muss aktualisiert werden, ohne erledigte Fragen erneut zu stellen. Fehlender Datei- oder Quellenzugriff wird benannt; das System darf weder Exporte noch durchgeführte Prüfungen erfinden. Wiederkehrende Überwachung benötigt eine tatsächlich eingerichtete Ausführungsumgebung. Eine Markdown-Anweisung richtet keine Überwachung im Hintergrund ein.

## 1.3 Zehn Praxisfälle

Die Fallseiten bieten jeweils Gesamt-PDF, Einzel-PDF-ZIP und Originalformat-ZIP. Beide ZIP-Varianten enthalten die einzelnen Dateien ohne Unterordner sowie den Herkunftshinweis in einer `README.txt`. Lösungen und interne Prüfkriterien gehören nicht in die Akten.

Die ergänzten Originale führen dieselben Vorgänge fort. Frühere Schreiben behalten ihren damaligen Stand; spätere Rückmeldungen können ihn ergänzen oder infrage stellen. Für einen zweiten Seminardurchgang lassen sich die fortlaufend hinzugefügten Unterlagen zunächst zurückhalten und anschließend zum laufenden Vorgang geben. Maßgebend ist jeweils das Dokumentdatum, nicht allein die Dateinummer.

Diese Testakte wurde mit KI generiert und ist ein Experiment. Benutzung auf eigene Verantwortung und eigene Gefahr.

This test case file was generated with AI and is an experiment. Use at your own responsibility and risk.

| Stufe | Fall | Ausgangsmaterial und Ziel der Bearbeitung |
| --- | --- | --- |
| Anfänger 1 | [Begehung in Einbeck](../testakten/bau-rundum-begehung-einbeck/README.md) | Begehungsnotizen, Ortsdokumentation, Serviceberichte, Höhenablesungen und Materialbelege für ein fortschreibbares Protokoll. |
| Anfänger 2 | [Baubeschreibung und Leistungsverzeichnis in Detmold](../testakten/bau-rundum-lv-abgleich-detmold/README.md) | Unterschiedliche Planstände, örtliche Boden- und Türbefunde, Sockelstrecken und Lieferauskünfte für einen belegten Abgleich. |
| Anfänger 3 | [Leistungsbeschreibung und Bieterfragen in Celle](../testakten/bau-rundum-bieterfragen-celle/README.md) | Vergabeunterlagen, Bieterpost, Lieferantendaten, Leitungsaufnahme und Rasterablesungen für abgestimmte Antwortentwürfe. |
| Anfänger 4 | [Behinderung in Soest](../testakten/bau-rundum-behinderung-soest/README.md) | Diktat, Bautagesdaten, Rohrstegmontage, Pumpendisposition und Polierbuch für eine konkrete Behinderungsanzeige. |
| Anfänger 5 | [Baugrund in Verden](../testakten/bau-rundum-baugrund-verden/README.md) | Gutachten, Kontrollnivellement, Probenannahme, fortgeschriebene Maschinenlasten und Wasserbeobachtungen für eine belegte Anforderungsliste. |
| Fortgeschrittene 1 | [Abschlagsrechnung in Lemgo](../testakten/bau-rundum-abschlagsrechnung-lemgo/README.md) | Rechnungen, Zahlungen, Aufmaß, Geräteaufzeichnungen und Nacharbeitsberichte für eine prüfbare Abrechnung. |
| Fortgeschrittene 2 | [VgV-Bewerbung in Hameln](../testakten/bau-rundum-vgv-bewerbung-hameln/README.md) | Anforderungen, Referenzen, ARGE-Leistungsabgrenzung, Versicherungs- und Personalunterlagen für eine belegte Bewerbung. |
| Fortgeschrittene 3 | [Angebotsprüfung in Goslar](../testakten/bau-rundum-angebotspruefung-goslar/README.md) | Angebote, Elementabmessungen, Zugriffsjournal, Kapazitätsvorbehalte und Preiserklärung für eine nachvollziehbare Prüfung. |
| Fortgeschrittene 4 | [Bauzeit-Claim in Minden](../testakten/bau-rundum-bauzeit-claim-minden/README.md) | Terminpläne, Tagesaufzeichnungen, Kranmiete, Gerätestunden und Kolonnenfreigabe für eine belegte Störungschronologie. |
| Fortgeschrittene 5 | [Nachtrag in Northeim](../testakten/bau-rundum-nachtrag-northeim/README.md) | Leistungsänderung, Kalkulation, Lagerbestände, bedingte Rücknahmeauskunft und Kolonneneinsatz für die Nachtragsprüfung. |

## 1.4 Fachliche Kontrolle

Das Protokoll ersetzt keine technische Abnahme, die Gutachtenauswertung keine geotechnische Bemessung und der Preisspiegel keine Zuschlagsentscheidung. Vertragsgrundlage, Vertragsfassung und Verfahrensbeginn bestimmen, welche Regelungen anzuwenden sind. Bei Bauvergaben und Planungsvergaben gelten nicht automatisch dieselben Vorschriften. Jede tragende Feststellung muss zu einer tatsächlich lesbaren Unterlage oder überprüften Quelle zurückführen.

Die Seminarankündigungen geben die Lernziele vor; sie werden nicht als Rechtsquelle oder Nachweis einer Produktzertifizierung behandelt. Anbieter-, Datenschutz- und Nutzungsfragen erläutert der [Repository-Leitfaden](../README.md). Vertrauliche echte Projektunterlagen nur in dafür freigegebene Systeme geben.

## 1.5 English guide

This folder groups two separately installable construction-industry plugins: beginner and advanced. Each provides eight task skills, a standalone workshop prompt, a compact prompt and five practice files. The beginner course develops evidence-based documents; the advanced course connects invoice review, procurement and change management with explicit human approval points. The grouping folder is not another plugin.

Use one package and one case at a time. Download formats are explained on the linked case pages. Tool access, file export and scheduled execution depend on the actual host environment; no cross-client live certification is claimed. Engineering judgement, procurement decisions and external communications remain with the responsible professional.
