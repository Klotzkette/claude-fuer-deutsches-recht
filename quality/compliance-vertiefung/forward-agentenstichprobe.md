# Interne Agentenstichprobe am Compliance-Mini-Prompt

## 1 Durchführung und Grenze

Der ausführende Agent hat den finalen Mini-Prompt mit dem ursprünglichen Material der Fälle ME-22 und ME-28 angewendet. Die Basisentwürfe wurden vor Einarbeitung der Stücke 12 und 13 geschrieben und unverändert als entwurf-v1.md erhalten. Anschließend wurden beide Nachträge gelesen und dieselben Dateien entwurf.md gezielt fortgeschrieben. Die Input- und Promptprüfsummen sind je Fall in lauf-v1.json und lauf-v2.json dokumentiert; die gezielten Änderungen in fortschreibung.diff.json. Screenshots wurden visuell gelesen, DOCX-Absätze, CSV-Zeilen, Excel-Zeilen und PDF-Seiten vollständig extrahiert.

Es handelt sich um eine tatsächlich ausgeführte Agentenstichprobe innerhalb dieser Sitzung, nicht um einen automatisierten Benchmark oder eine Messung in einer externen Clientoberfläche. Die Skills des ausführenden Agenten wurden für diese Probe nicht angewendet. Der Mini-Prompt wurde von einem anderen Agenten geschrieben. Nachbesprechungen und quality/evals wurden nicht als Lösung gelesen. Der Testautor hat die fünf Skills derselben Komponente verfasst; damit besteht keine vollständig von der Komponentenbearbeitung unabhängige Versuchsumgebung. Aus zwei Fällen folgt keine allgemeine Erfolgsquote für die Sammlung.

## 2 Beobachtetes Verhalten bei ME-22

Das Produkt enthält den ausformulierten Bestätigungstext, vertraulichen Prüfauftrag, Zugriffskonzept und Fristenvermerk. Es behauptet keinen Versand. Der Eingang um 06:42 Uhr wird von der späteren E-Mail getrennt. Die Fristen sind auf den 19.10.2026 und 19.01.2027 gerechnet; interne Erledigung wird nicht als Rückmeldung ausgegeben. [forward-me22/entwurf.md, Z. 3 bis 19 und 52 bis 57.]

Die Quelle wird nicht allein durch Namensentfernung als anonym behandelt. Der nachträglich konkretisierte Suchauftrag an den Lagerleiter ist eng begrenzt; die unabhängige Qualitätssicherung bleibt für die Bewertung zuständig. Der Speicheraccount wird weder mit der handelnden noch mit der entscheidenden Person gleichgesetzt. Die drei Registerdarstellungen und der neue Belegabgleich werden nicht als unabhängige Mehrfachbestätigung gezählt. [Z. 30 bis 40 und 63.]

Die Fortsetzung hat keine neue allgemeine Mandatsaufnahme ausgelöst. Sie änderte den Bearbeitungsstand, ergänzte die Lagerleiterrolle, präzisierte die Kontozuordnung und den Rückmeldeweg und behielt den übrigen Entwurf bei.

In der nachgelagerten redaktionellen Gegenlese wurde ein Formulierungsfehler erkannt: „Die ursprünglichen … Protokolle sind deshalb gesichert und … abzugleichen“ hätte eine bereits erfolgte Sicherung nahelegen können. Die erhaltene Fassung entwurf-v2-vor-gegenlese.md zeigt den Fehler. Im endgültigen Agentenprodukt lautet es ausdrücklich „sind deshalb zu sichern und … abzugleichen“. Der Mini-Prompt verbietet bereits nicht belegte Ausführungsbehauptungen; daraus wird kein fehlender Promptschutz konstruiert. Die Probe wird daher nicht als fehlerfreie Erstausgabe bezeichnet.

## 3 Beobachtetes Verhalten bei ME-28

Der Bericht berechnet 588/600 = 98,00 %, 4/24 = 16,67 %, 2/24 = 8,33 %, 7/9 = 77,78 %, 26/460 = 5,65 % und 434/460 = 94,35 %. Der Rechenweg wurde separat mit Decimal nachgerechnet. Die letzte Quote wird ausdrücklich nicht als rechtzeitige Freigabequote verwendet. Die 26 ungeklärten Fälle werden weder rechtzeitig noch verspätet ausgezählt. Fehlende Uhrzeiten werden nicht durch 00:00 Uhr ersetzt. [forward-me28/entwurf.md, Z. 17 bis 23.]

Der risikobasierten 24er-Auswahl wird keine unbegründete Repräsentativität zugeschrieben. Die behauptete Papierfreigabe bleibt prüfbedürftig. Die 30er-Prüfung bleibt geplant; aus 0/30 wird kein Nullfehlerergebnis. Die unterschiedliche Branchenbasis und Befragungsquote werden gesondert behandelt. [Z. 18 bis 31.]

Die Fortsetzung übernimmt die mitgeteilte Verfügbarkeit der Übergangsliste als Aussage der Revision, ohne die nicht beigefügte Liste als bereits geprüft auszugeben. Sie ergänzt die getrennte Prüfung technischer Pflichtfelder und tatsächlicher Vorabkontrolle mit vorab definiertem Beobachtungsbeginn und Erfolgskriterium. Eine begrenzte Bestandsprüfung und konkrete Erweiterungsauslöser bleiben im selben Entwurf. [Z. 37 bis 55.]

## 4 Beurteilung

In diesen beiden ausgeführten Beispielen entstanden verwendbare vollständige Entwürfe, deren Zahlen, Fristen, Beleggrenzen und Gegenhypothesen nachvollziehbar sind. Nachträge wurden fallbezogen eingearbeitet, ohne ihre wiederholten Registerwerte zu Primärbeweisen aufzuwerten. Die Probe liefert Artefakte und konkrete Beobachtungen; sie ersetzt keine externe Clientprüfung oder juristische Freigabe. Der bei ME-22 gefundene und korrigierte Sprachfehler bleibt dokumentiert. Am Plugin, Mini-Prompt oder Skillbestand wurden während dieser Blindprobe keine Änderungen vorgenommen.
