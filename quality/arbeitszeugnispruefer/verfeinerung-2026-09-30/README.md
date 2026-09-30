# 1. Arbeitszeugnisprüfer: Verfeinerung vom 30. September 2026

## 1.1. Tatsächlich geprüfter Umfang

Werkstatt, Mini und zwölf vorhandene Skills wurden überarbeitet. Es bleiben 31 Skills. Die [Quellenprüfung](quellenpruefung.md) dokumentiert gelesene Normen und Entscheidungen einschließlich Herkunft und Reichweite älterer Volltexte. Die Quellenprüfung ist von den nachfolgenden Modellproben und den technischen Tests zu unterscheiden.

Drei unabhängige Agenten erhielten jeweils die zu prüfende Arbeitsanweisung und einen konkreten Nutzerauftrag mit tatsächlichen kurzen Belegdateien. Sie erhielten keine Sollantworten oder Bewertungskriterien und keine Antworten anderer Agenten. Werkstatt und Mini wurden in zwei echten Nachrichtenrunden ausgeführt: Erst nach den tatsächlich gestellten Fragen wurde die zweite Nutzereingabe freigegeben. Der Hauptskill bearbeitete einen vollständig vorgegebenen Korrekturfall. Die Eingaben sind fiktive Prüfdaten, keine echten Personalunterlagen.

Die Agenten bekamen zunächst ausschließlich ihre zugewiesene Werkstatt, ihren Mini oder den Hauptskill; beim Hauptskill durften fachlich passende Spezialskills hinzukommen. Die Rohantworten sind in [rohausgaben.json](antworten/rohausgaben.json) vollständig gespeichert. In den lesbaren Markdown-Fassungen wurden ausschließlich zwei Leerzeichen am Zeilenende in einen gleichwertigen Markdown-Zeilenumbruch umgewandelt. Die Roh- und Lesehashes sind getrennt dokumentiert.

## 1.2. Beobachtete Ergebnisse

| Probe | Tatsächlicher Ablauf und Ergebnis | Nachweis |
| --- | --- | --- |
| Werkstatt: Karriere und Teamzahlen | Fragte nach dem Widerspruch zu angeblicher Verantwortung seit 2021 und nach persönlichen Führungsleistungen. Übernahm nach der Antwort die richtigen Zeiträume, entfernte den zurückgenommenen Aufwertungswunsch und lieferte Analyse, Gesamtfassung, kurze direkte Empfehlung und Arbeitgeberbrief im eigenen Namen. Keine Budgetverantwortung und keine hervorragende Führung aus Teamumsatz erfunden. | [Erste Antwort](antworten/werkstatt-antwort-1.md), [Fortsetzung](antworten/werkstatt-antwort-2.md) |
| Mini: Abwertung und Zieländerung | Trennte die Abwehr einer unterdurchschnittlichen Note vom Beweis für gut; fragte zum dritten Vorfall, zum Projektlob und ergänzend zur bisherigen Geltendmachung/Vertragsfrist. Die zweite Nutzereingabe beantwortete diese tatsächlichen Fragen. Danach entstand ein vollständiger Brief für ausschließlich befriedigend, mit eingeräumtem Einzelfehler und verbleibendem Risiko; keine bloße Gefälligkeitsbitte und kein weiterverfolgtes Ziel gut. | [Erste Antwort](antworten/mini-antwort-1.md), [Fortsetzung](antworten/mini-antwort-2.md) |
| Hauptskill: Korrekturfassung | Akzeptierte die bedeutungsgleiche Teamformulierung. Beanstandete die neue Verkürzung der eigenverantwortlichen Terminplanung, verlangte aber keine tatsächlich fehlende Abnahmebefugnis. Lieferte einen präzisen Ersatzabsatz, kurze Erklärung und begrenztes Folgeschreiben ohne weitere Aufnahmefragen. | [Antwort](antworten/hauptskill-antwort.md) |

Die Rohunterlagen stehen getrennt von diesem Bewertungsbericht: [Karriere](../../../scripts/fixtures/arbeitszeugnispruefer/2026-09-30/karriere/auftrag-1.txt), [Abwertung](../../../scripts/fixtures/arbeitszeugnispruefer/2026-09-30/abwertung/auftrag-1.txt), [Korrektur](../../../scripts/fixtures/arbeitszeugnispruefer/2026-09-30/korrektur/auftrag.txt). Die relative Verlinkung wird technisch geprüft. Das [Eval-Profil](../../evals/arbeitszeugnispruefer.json) enthält daneben drei neue Fälle mit echten Eingabedateien; die übrigen Szenarien sind nicht sämtlich als Modellläufe ausgeführt worden.

## 1.3. Grenzen der Beobachtung

Die drei Proben zeigen das beobachtete Verhalten mit diesen Eingaben. Sie sind kein vollständiger Benchmark sämtlicher Skills und keine Funktionsgarantie für andere Modelle. Nicht unabhängig als Dialogprobe ausgeführt wurden insbesondere Ausbildungszeugnis, elektronisch signierte Originaldatei und gerichtliche Vollstreckung; deren Ergänzungen beruhen auf Quellen- und Fachprüfung. Es fand kein Word-/PDF-Export, keine technische Signaturprüfung und kein Versand statt.

Der Hauptskill formulierte die kurze persönliche Erklärung in Briefform mit Anrede und Gruß; der Werkstattlauf lieferte sie als direkte Empfehlung. Beide blieben ohne erfundene Kanzleirolle. Die Mini-Probe stellte zusätzlich eine Fristenfrage, obwohl zunächst keine besondere Frist bekannt war; sie verarbeitete die Antwort anschließend ohne erneute Suchschleife. Diese Unterschiede werden nicht als identisches Ausgabeformat ausgegeben.

Das anschließende [unabhängige Fachreview](abschlussreview.md) fand keine handlungsrelevanten Widersprüche im geprüften Diff. Auch dieses statische Review ist kein weiterer Modelllauf.

## 1.4. Technische Nachweise

Das [Dateimanifest](dateimanifest.json) bindet Arbeitsanweisungen, Eingaben und Antworten an SHA-256-Werte. Die [technischen Prüfergebnisse](technische-pruefung.json) führen die tatsächlich ausgeführten Prüfkommandos mit Exitstatus auf. Sie belegen Struktur, Profile, Generatoren und Regressionen, nicht die juristische Richtigkeit beliebiger künftiger Fälle. Der Mini umfasst 7.353 Zeichen beziehungsweise 7.491 UTF-8-Bytes.
