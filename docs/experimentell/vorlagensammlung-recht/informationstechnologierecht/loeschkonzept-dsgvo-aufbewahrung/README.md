# Löschkonzept und Aufbewahrungsmatrix nach DSGVO

## Download

- [⬇ Löschkonzept und Aufbewahrungsmatrix nach DSGVO – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/loeschkonzept-dsgvo-aufbewahrung/loeschkonzept-dsgvo-aufbewahrung.odt) — Offene Bürofassung (OpenDocument)
- [⬇ Löschkonzept und Aufbewahrungsmatrix nach DSGVO – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/loeschkonzept-dsgvo-aufbewahrung/loeschkonzept-dsgvo-aufbewahrung.md.zip) — Bearbeitbare Markdown-Fassung, gepackt für direkten Download

Vorschau im Repository: [`loeschkonzept-dsgvo-aufbewahrung.odt`](loeschkonzept-dsgvo-aufbewahrung.odt) · [`loeschkonzept-dsgvo-aufbewahrung.md`](loeschkonzept-dsgvo-aufbewahrung.md)

## Vorspruch und Nutzungsgrenze

Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung ausschließlich auf eigene Gewähr und eigene Gefahr. Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT sind zu beachten.

## Anwendungsbereich

Die Vorlage eignet sich für interne Datenschutzdokumentation, Due Diligence, Post-Closing-Sanierung, Datenschutz-Audit und Aufsichtsbehördenvorbereitung, wenn ein Unternehmen Daten zwar praktisch löscht, aber Fristen, Sperren, Backup-Rotation und Auftragsverarbeiter-Weisungen nicht prüfbar dokumentiert hat. Sie ergänzt `informationstechnologierecht/verzeichnis-verarbeitungstaetigkeiten-due-diligence/`, `informationstechnologierecht/datenschutz-gap-report-due-diligence/` und `informationstechnologierecht/auftragsverarbeiter-subprocessor-register-due-diligence/`.

## Einschlägige Normen

Art. 5 Abs. 1 lit. e DSGVO, Art. 5 Abs. 2 DSGVO, Art. 17 DSGVO, Art. 18 DSGVO, Art. 24 DSGVO, Art. 28 Abs. 3 lit. g DSGVO, Art. 30 DSGVO, Art. 32 DSGVO, § 257 HGB, § 147 AO, § 26 BDSG.

Amtliche Quellen: [DSGVO](https://eur-lex.europa.eu/eli/reg/2016/679/oj) · [BDSG](https://www.gesetze-im-internet.de/bdsg_2018/) · [HGB § 257](https://www.gesetze-im-internet.de/hgb/__257.html) · [AO § 147](https://www.gesetze-im-internet.de/ao_1977/__147.html).

## Hinweise zur Verwendung

Ein Löschkonzept ist kein Datenschutzvorfallregister und kein bloßer Systemkatalog. Es muss pro Datenklasse erklären, warum Daten gespeichert werden, wann der Zweck entfällt, welche gesetzlichen Aufbewahrungspflichten fortbestehen und wie die Löschung technisch nachgewiesen wird.

Praxisfehler sind pauschale Fristen ohne Fristbeginn, fehlende Backup-Regeln, unklare Sperrvermerke, nicht angewiesene Auftragsverarbeiter und Vermischung von Löschung mit Archivierung. In einer M&A-Prüfung ist besonders zu dokumentieren, ob Altbestände, Testdaten, Supportanhänge und lokale Exporte dieselbe Löschlogik tragen wie produktive Systeme.

## Taktische Hinweise

Vorgehensreihenfolge: Am Anfang stehen Systeminventar und Verzeichnis der Verarbeitungstätigkeiten, aus denen die Datenklassen gebildet werden — ohne diese Basis beschreibt das Konzept Fristen für Datenbestände, die niemand kennt. Danach wird je Klasse der Fristbeginn als technisch auswertbares Ereignis definiert, dann die Kollision zwischen Löschpflicht und Aufbewahrungspflichten (§ 257 HGB, § 147 AO) aufgelöst, anschließend die Löschhandlung einschließlich Backup-Strategie technisch festgelegt und zuletzt die Wirksamkeitskontrolle mit Stichproben nach Anlage 1 etabliert. Ein Konzept ohne ersten dokumentierten Löschlauf ist gegenüber Aufsicht und Käufer nur eine Absichtserklärung.

Typische Einwände und Antwortlinien:

- „Wir speichern pauschal bis zum Ablauf der längsten Verjährungsfrist." — Das Nachweisinteresse trägt nur je Datenklasse mit konkretem Anspruchsbezug; die pauschale Höchstfristspeicherung verstößt gegen die Speicherbegrenzung des Art. 5 Abs. 1 lit. e DSGVO und fällt in jeder Prüfung zuerst auf.
- „Aus Backups kann man nicht einzeln löschen." — Anerkannt ist die Kombination aus definierter Backup-Rotation und einem dokumentierten Sperrmechanismus, der gelöschte Datensätze bei einer Wiederherstellung erneut löscht; entscheidend ist, dass dieser Prozess beschrieben und getestet ist.
- „Wir anonymisieren statt zu löschen, das genügt." — Das genügt nur bei irreversibler Anonymisierung ohne Re-Identifizierungsrisiko; Pseudonymisierung mit fortbestehender Zuordnungstabelle ist keine Löschung.
- „Der Betroffene verlangt Löschung, aber wir müssen aufbewahren." — Die Antwort ist Art. 17 Abs. 3 lit. b DSGVO: keine Löschung, aber Einschränkung der Verarbeitung nach Art. 18 DSGVO mit Sperrvermerk und transparenter Erläuterung gegenüber der betroffenen Person.

Erledigungs- und Einigungskorridor: Gegenüber der Aufsichtsbehörde genügt bei Beanstandungen regelmäßig die Vorlage des Konzepts samt Nachweis der ersten Löschläufe und einem terminierten Maßnahmenplan für Altbestände; gegenüber Betroffenen erledigt sich der Streit über ein Löschbegehren meist durch Teillöschung, Sperrung des Rests und ein Erläuterungsschreiben, das die fortbestehenden Aufbewahrungspflichten mit Normbezug benennt.

Häufige Fehler:

- Fristen werden aus fremden Mustern für alle Datenklassen übernommen, obwohl weder Branche noch Anspruchslage passen.
- Der Fristbeginn „Vertragsende" ist in keinem System als Feld gepflegt, sodass kein automatischer Löschlauf je starten kann.
- Ticket- und E-Mail-Anhänge, lokale Exporte und Schattenlisten in Fachabteilungen bleiben außerhalb der Löschlogik.
- Die Löschprotokolle selbst enthalten vollständige personenbezogene Datensätze und konterkarieren die Löschung.
- Die jährliche Wiedervorlage nach Ziffer 6.1 existiert nur auf dem Papier, weil neue Systeme und Migrationen keinen Aktualisierungs-Trigger auslösen.

## Verwandte Vorlagen

- [Verzeichnis der Verarbeitungstätigkeiten für Datenschutz-Due-Diligence](../verzeichnis-verarbeitungstaetigkeiten-due-diligence/) — Art.-30-Verzeichnis, aus dem die Datenklassen und Zwecke dieses Konzepts abgeleitet werden.
- [Betroffenenrechte-Register nach DSGVO](../betroffenenrechte-register-dsgvo/) — Register für Löschbegehren nach Art. 17 DSGVO, die gegen dieses Konzept entschieden werden.
- [Auftragsverarbeitungsvertrag (Art. 28 DSGVO; SDM)](../auftragsverarbeitungsvertrag-dsgvo/) — AVV mit der Lösch- und Rückgabepflicht nach Art. 28 Abs. 3 lit. g DSGVO, die Abschnitt 5 operationalisiert.
- [Anlage TOM zum Auftragsverarbeitungsvertrag](../avv-tom-anlage-dsgvo/) — TOM-Anlage, deren Löschkonzept-Ziffer mit diesem Dokument konsistent sein muss.
- [Datenschutzerklärung für Websites (Art. 13/14 DSGVO; TDDDG)](../datenschutzerklaerung-website-dsgvo/) — Datenschutzerklärung, deren Speicherdauer-Angaben aus dieser Matrix stammen müssen.

## Rechtsprechungsstand 2026

- Gerichtshof der Europäischen Union, Urteil vom 18. Juni 2026 — C-484/24, NTH Haustechnik: Art. 17 Abs. 3 Buchstabe e DSGVO begrenzt den Löschungsanspruch, schafft aber keine eigenständige Rechtsgrundlage für die Verarbeitung. Auch bei Aufbewahrung und gerichtlicher Nutzung zur Rechtsverfolgung oder Rechtsverteidigung bleibt eine Rechtsgrundlage nach Art. 6 Abs. 1 DSGVO erforderlich; Datenminimierung und Verhältnismäßigkeit sind gesondert zu prüfen. Quelle: [EuGH C-484/24](https://juris.curia.europa.eu/juris/document/document.jsf?docid=312704&doclang=de).

Das Löschkonzept darf die Kategorie „Rechtsverteidigung“ deshalb nicht als pauschale Daueraufbewahrung führen. Es muss möglichen Anspruch, betroffenen Datenbestand, Beginn und Ende der Aufbewahrung, Zugriffsbeschränkung, Rechtsgrundlage und erneuten Prüftermin dokumentieren.
