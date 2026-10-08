# Transfer Impact Assessment für SCC-Drittlandtransfer
Dokumentation der Schrems-II-Prüfung für Transfers auf Grundlage der EU-Standardvertragsklauseln.

## Download
- [⬇ Transfer Impact Assessment für SCC-Drittlandtransfer – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/transfer-impact-assessment-scc-dsgvo/transfer-impact-assessment-scc-dsgvo.odt) — Offene Bürofassung (OpenDocument)
- [⬇ Transfer Impact Assessment für SCC-Drittlandtransfer – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/transfer-impact-assessment-scc-dsgvo/transfer-impact-assessment-scc-dsgvo.md.zip) — Bearbeitbare Markdown-Fassung, gepackt für direkten Download

Vorschau im Repository: [`transfer-impact-assessment-scc-dsgvo.odt`](transfer-impact-assessment-scc-dsgvo.odt) · [`transfer-impact-assessment-scc-dsgvo.md`](transfer-impact-assessment-scc-dsgvo.md)

## Vorspruch und Nutzungsgrenze

Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Sie ist ein Struktur- und Formulierungsvorschlag, kein Gutachten und kein ungeprüft verwendbares Mandatsprodukt. Nutzung nur auf eigene Gewähr und eigene Gefahr; vor jedem Einsatz sind Sachverhalt, Rechtslage, Form, Fristen, Zuständigkeit, Vertretungsmacht, Datenschutz, Vollziehbarkeit und wirtschaftliche Folgen fachkundig zu prüfen, anzupassen und freizugeben.

Mandatsbezogene und personenbezogene Inhalte sind nach § 43a Abs. 2 BRAO, § 203 StGB und DSGVO zu schützen. Bei Verarbeitung in Drittsystemen sind Anonymisierung, Rechtsgrundlage, Auftragsverarbeitung und Löschkonzept zu prüfen.

Lizenz: Apache-2.0 OR MIT.

## Anwendungsbereich

Diese Vorlage gehört zum Drittlandtransfer-Paket und dient der Dokumentation oder Freigabe eines konkreten internationalen Datentransfers. Sie passt nur, wenn Datenkategorien, Empfänger, Drittland, Transfermechanismus und technische Schutzmaßnahmen bereits fallbezogen erhoben werden können.

## Einschlägige Normen

- Art. 44 DSGVO als Grundnorm für Übermittlungen personenbezogener Daten in Drittländer und an internationale Organisationen.
- Art. 45 DSGVO für Angemessenheitsbeschlüsse, insbesondere die jeweils aktuelle EU-Liste und den EU-US Data Privacy Framework-Beschluss.
- Art. 46 Abs. 1 und Abs. 2 Buchst. c DSGVO für Standarddatenschutzklauseln; Durchführungsbeschluss (EU) 2021/914 als SCC-Modulanker.
- Art. 47 DSGVO für Binding Corporate Rules und Art. 49 Abs. 1 DSGVO für eng auszulegende Ausnahmen.
- Art. 28, Art. 30, Art. 32, Art. 35 DSGVO, wenn Auftragsverarbeitung, Verzeichnis, Sicherheitsmaßnahmen oder Datenschutz-Folgenabschätzung berührt sind.

## Pflichtangaben

Benötigt werden SCC-Modul, Empfängerrolle, Datenkategorien, Betroffenenkategorien, Zugriffspfad, Zielland, Unterauftragskette, lokale Zugriffsbefugnisse öffentlicher Stellen, Empfängererfahrung mit Behördenzugriffen, technische Schutzmaßnahmen, Schlüsselverwaltung, Pseudonymisierung, Widerspruchs- und Benachrichtigungspflichten sowie Freigabeentscheidung.

## Mustertext mit Platzhaltern

Die Vorlage enthält ein ausformuliertes TIA mit Transferbeschreibung, Länder- und Zugriffsbewertung, SCC-Modulprüfung, Prüfung ergänzender Maßnahmen, Restrisikoentscheidung und Nachprüfungspflichten.

## Hinweise zur Verwendung

Der Transfer wird erst freigegeben, wenn Datenkategorien, Empfängerrolle, Land, Unterauftragnehmer, Zugriffsszenarien und Übermittlungsmechanismus getrennt dokumentiert sind. SCC, Angemessenheitsbeschluss, Data Privacy Framework, Binding Corporate Rules und Art. 49 DSGVO sind keine austauschbaren Etiketten, sondern unterschiedliche Rechtfertigungswege mit eigener Begründung.

Fristen- und Nachweisarchitektur: Rezertifizierung, Lieferantenbestätigung, Review des Transfer Impact Assessment, Unterauftragnehmerfreigabe, Betroffeneninformation und Abhilfemaßnahmen werden mit Datum, Verantwortlichem und Wiedervorlage geführt. Behördenzugriffe und Exportbeschränkungen werden nicht pauschal bewertet, sondern nach Datenart, Zugriffswahrscheinlichkeit, Verschlüsselung und organisatorischer Kontrolle.

Abgrenzung: Für SCC-Begleitvereinbarung `informationstechnologierecht/standardvertragsklauseln-scc-begleitvereinbarung/`; für TIA `informationstechnologierecht/transfer-impact-assessment-scc-dsgvo/`; für DPF-Prüfung `informationstechnologierecht/eu-us-data-privacy-framework-pruefung/`.

## Taktische Hinweise

Vorgehensreihenfolge: Das TIA beginnt beim Datenfluss, nicht beim Zielland: Erst wenn feststeht, welche Datenarten in welcher Form (Klartext, verschlüsselt, pseudonymisiert) wem zugänglich werden, lässt sich das Ziellandrecht sinnvoll bewerten. Danach folgt die Stufenprüfung der Anlage 1 (Rechtsgrundlage, Instrument, Ziellandrecht, ergänzende Maßnahmen, Dokumentation). Die Importeur-Auskünfte nach Ziffer 2.3 werden früh angefordert, weil sie erfahrungsgemäß Wochen brauchen; die Freigabe wird mit automatischer Sperrfolge nach Ziffer 6.4 verbunden, damit offene Auflagen nicht in den Dauerbetrieb rutschen.

Typische Einwände und Antwortlinien:

- „Das TIA des Anbieters liegt doch bei, das übernehmen wir." — Anbieter-TIAs argumentieren aus Importeursicht und kennen weder die konkreten Datenarten noch den Schutzbedarf des Exporteurs; sie sind Quelle, nicht Ergebnis, und die Bewertung der Zugriffswahrscheinlichkeit muss auf den eigenen Transfer bezogen werden.
- „Das Ziellandrecht können wir nicht abschließend beurteilen." — Verlangt ist keine völkerrechtliche Expertise, sondern eine dokumentierte Bewertung nach verfügbaren Quellen (Gesetzestexte, Transparenzberichte, Importeur-Auskünfte, Leitlinien; Suchanker: EDSA Empfehlungen 01/2020 wesentliche Garantien); Lücken werden als [noch zu klären: …] ausgewiesen statt überspielt.
- „Verschlüsselung im Transport reicht als Zusatzmaßnahme." — Gegen Behördenzugriff beim Importeur hilft nur Verschlüsselung oder Pseudonymisierung, bei der die Schlüssel oder Zusatzinformationen ausschließlich im EWR liegen; Transportverschlüsselung schützt nur die Strecke.
- „Vertragsklauseln mit Anfechtungspflicht lösen das Problem." — Vertragliche und organisatorische Maßnahmen binden Behörden des Ziellands nicht; sie flankieren technische Maßnahmen, ersetzen sie aber bei problematischer Rechtslage nicht (Suchanker: EuGH Schrems II ergänzende Maßnahmen).

Erledigungs- und Einigungskorridor: Fällt die Stufenprüfung negativ aus, ist der praktikable Korridor selten der Verzicht auf den Dienst, sondern die Reduktion: weniger Datenfelder, Pseudonymisierung vor Export, EU-Region mit dokumentierter Zugriffsbeschränkung oder Schlüsselverwaltung im EWR; die Freigabe erfolgt dann für den reduzierten Umfang. Gegenüber Aufsichtsbehörden trägt ein methodisch sauberes TIA mit ausgewiesenen Restrisiken deutlich weiter als ein geschöntes Ergebnis ohne Quellen.

Häufige Fehler:

- Das TIA wird nach Vertragsschluss und Produktivstart erstellt und dokumentiert damit den laufenden Verstoß.
- Die Zugriffswahrscheinlichkeit wird ohne einzige Quelle als „niedrig" bewertet, was in jeder Behördenprüfung sofort kippt.
- Die SCC-Anlagen bleiben pauschal („alle Datenkategorien, alle Zwecke"), sodass das TIA einen Transfer bewertet, den der Vertrag gar nicht abbildet.
- Fernzugriffe (Support, Administration, Monitoring) fehlen in der Transferbeschreibung, obwohl sie die zugriffskritischste Strecke sind.
- Die Nachprüfung nach Abschnitt 7 hat kein Datum und keinen Anlasskatalog-Verantwortlichen, sodass Rechtsänderungen im Zielland unbemerkt bleiben.

## Verwandte Vorlagen

- [SCC-Begleitvereinbarung für Drittlandtransfer](../standardvertragsklauseln-scc-begleitvereinbarung/) — Vertragliche Umsetzung der SCC, deren Anlagen dieses TIA in Stufe 2 prüft.
- [EU-US Data Privacy Framework Prüfvermerk](../eu-us-data-privacy-framework-pruefung/) — DPF-Prüfung, die bei US-Importeuren vor dem SCC-Weg steht oder ihn ergänzt (Ziffer 3.4).
- [Prüfvermerk Behördenzugriff bei Drittlandtransfer](../drittlandtransfer-behoerdenzugriff-pruefvermerk/) — Vertiefter Prüfvermerk zur Zugriffslage im Zielland als Zulieferung zur Stufe 3.
- [Prüfvermerk Drittlandtransfer nach DSGVO](../drittlandtransfer-pruefvermerk-dsgvo/) — Freigabevermerk, der das TIA-Ergebnis in die dokumentierte Transferentscheidung überführt.
- [Drittlandtransfer Aussetzung und Abhilfeplan](../drittlandtransfer-aussetzung-abhilfeplan/) — Aussetzungsplan für den Fall, dass die Nachprüfung das Schutzniveau entfallen sieht.
