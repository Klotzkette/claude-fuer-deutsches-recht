# Quellenbericht – Playbook-Prüfer

## 1. Umfang und Stichtag

Am **2. Oktober 2026** wurden gezielt die für das neue Playbook-Prüfer-Plugin relevanten NDA- und Arbeitsvertragsfragen anhand amtlicher Primärquellen überprüft. Das Quellenregister in [normen.json](normen.json) verzeichnet 34 gelesene Normgruppen und neun Entscheidungen mit Datum, Entscheidungsform, Aktenzeichen, konkreten Randnummern und URL. Die rechtlichen Aussagen, Anwendungsschritte und Übertragungsgrenzen stehen in [rechtsprechungsanker.md](../../../playbook-pruefer/references/rechtsprechungsanker.md).

## 2. Recherche und Aktualität

Die Suche umfasste die Begriffe NDA, Geschäftsgeheimnisse, Verschwiegenheit, Vertragsstrafe, Überstunden, Arbeitsvertrag, Freistellung und Homeoffice, jeweils mit gezielter Suche nach BGH-/BAG-Primärquellen und zusätzlichen Jahresfiltern 2026. Der verifizierte neue Anker BAG, Urt. v. 25.03.2026 – Az. 5 AZR 108/25 wird ausschließlich für das Thema Freistellung bei Kündigung verwendet. Ältere einschlägige Entscheidungen behalten ihr echtes Entscheidungsdatum. Ein Suchtreffer, anberaumter Termin oder fremder Bericht wird nicht als gesicherte neue Entscheidung behandelt. Eine lückenlose Gesamterfassung aller 2026 veröffentlichten Urteile wird nicht behauptet.

## 3. Verifikationsweg und Einschränkungen

Die BAG-Volltexte wurden in der gerichtlichen Entscheidungsdatenbank geöffnet. Der EuGH-Volltext C-55/18 wurde über die ECLI-Ansicht von EUR-Lex auf Deutsch gelesen; andere EUR-Lex-URLs lieferten zeitweilig lediglich eine JavaScript-Hinweisseite. Beim BGH leiteten alte juris-Links nach einem Datenbankumzug auf die Suche um. Deshalb wurde das Aktenzeichen in der neuen amtlichen Entscheidungssuche ermittelt, anschließend der amtliche PDF-Volltext heruntergeladen und gelesen. Der Hash steht im Register.

Bundesrecht wurde über Gesetze im Internet gelesen; wenn eine Einzelnorm vorübergehend nicht abrufbar war, wurden die dortige Gesamtausgabe oder der vollständig angezeigte Primärquellenwortlaut verwendet. Für die DSGVO wurde zusätzlich die amtliche BfDI-Normwiedergabe mit Stand März 2026 direkt als PDF abgerufen. Aus einer bloß erfolgreichen HTTP-Antwort wurde keine inhaltliche Verifikation abgeleitet.

## 4. Fachliche Trennung

Der Quellenabgleich trennt Unternehmensstandard und gesetzliche Grenze, Vertragszitat und Rechtsquelle, NDA und tatsächliche Geheimhaltungsmaßnahme, Arbeitszeiterfassung und Vergütungsanspruch sowie Vertragswirksamkeit und Nachweisform. Die Referenzdatei benennt die jeweilige Grenze der Übertragung. Die Prüfung der später erzeugten Modellantworten und ihrer tatsächlichen Vertragsbelege ist hiervon unabhängig.

## 5. Schlusskontrolle

Den dokumentierten Stand der Gegenprüfung von Skills, Prompts und Arbeitsakten enthält [rechtliche-pruefung.json](rechtliche-pruefung.json). Die vollständige Gegenlektüre erfasst 55 dort bezeichnete Dateifassungen: elf Skills, drei eigenständige Prompts, sechs Referenzen, die Rechenhilfe sowie die beiden Originalakten mit je README und redaktioneller Rubrik. Sechs tatsächliche Mailanlagen wurden zusätzlich selbst byteidentisch mit den Wordoriginalen abgeglichen. Die gezielten Fallkriterien stehen im [individuellen Eval-Profil](../../evals/playbook-pruefer.json); das Profil ist strukturell validiert, enthält aber keinen behaupteten Live-Modelllauf. Nur die im Audit mit SHA-256 erfassten Dateifassungen gelten als gelesen. Ein strukturell bestandener Validator ist keine juristische Vollprüfung.
