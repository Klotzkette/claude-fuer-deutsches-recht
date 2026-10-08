# Meldung einer Datenschutzverletzung

Formular zur Erfassung, Bewertung und Meldung einer Datenschutzverletzung an Aufsicht und Betroffene.

## Download
- [⬇ Meldung einer Datenschutzverletzung – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/data-breach-meldung-dsgvo/data-breach-meldung-dsgvo.odt) — OpenDocument-Arbeitsfassung
- [⬇ Meldung einer Datenschutzverletzung – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/data-breach-meldung-dsgvo/data-breach-meldung-dsgvo.md.zip) — Bearbeitbare Markdown-Fassung, gepackt für direkten Download

Vorschau im Repository: [`data-breach-meldung-dsgvo.odt`](data-breach-meldung-dsgvo.odt) · [`data-breach-meldung-dsgvo.md`](data-breach-meldung-dsgvo.md)

## Vorspruch und Nutzungsgrenze

Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Sie ist ein Struktur- und Formulierungsvorschlag, kein Gutachten und kein ungeprüft verwendbares Mandatsprodukt. Nutzung nur auf eigene Gewähr und eigene Gefahr; vor jedem Einsatz sind Sachverhalt, Rechtslage, Form, Fristen, Zuständigkeit, Vertretungsmacht, Datenschutz, Vollziehbarkeit und wirtschaftliche Folgen fachkundig zu prüfen, anzupassen und freizugeben.

Mandatsbezogene und personenbezogene Inhalte sind nach § 43a Abs. 2 BRAO, § 203 StGB und DSGVO zu schützen. Bei Verarbeitung in Drittsystemen sind Anonymisierung, Rechtsgrundlage, Auftragsverarbeitung und Löschkonzept zu prüfen.

Lizenz: Apache-2.0 OR MIT.

## Anwendungsbereich

Diese Vorlage dient der strukturierten Reaktion auf eine Datenschutzverletzung oder einen sicherheitsrelevanten Incident. Sie passt, wenn Ursache, Umfang, Risiko, Meldung, Betroffeneninformation und Abhilfemaßnahmen unter Zeitdruck dokumentiert werden müssen.

## Einschlägige Normen

- Art. 33 Abs. 1 DSGVO zur Meldung an die Aufsichtsbehörde binnen 72 Stunden nach Bekanntwerden.
- Art. 33 Abs. 3 DSGVO zum Mindestinhalt der Meldung und Art. 33 Abs. 5 DSGVO zur Dokumentationspflicht.
- Art. 34 Abs. 1 bis Abs. 3 DSGVO zur Benachrichtigung betroffener Personen und zu Ausnahmen.
- Art. 32 DSGVO zu Sicherheitsmaßnahmen und Art. 82 DSGVO zu Haftungsrisiken.
- Spezialpflichten aus NIS2-Umsetzung, BSIG oder DORA werden je nach Organisation zusätzlich geprüft.

## Hinweise zur Verwendung

Die Meldung muss zwischen Sicherheitsereignis, Datenschutzverletzung, meldepflichtigem Risiko und benachrichtigungspflichtigem hohem Risiko unterscheiden. Die 72-Stunden-Frist aus Art. 33 Abs. 1 DSGVO läuft ab Bekanntwerden der Verletzung, nicht erst ab vollständiger forensischer Aufklärung.

Fristen- und Beweisarchitektur: Erstmeldung, Nachmeldung, Betroffenenbenachrichtigung, Maßnahmenplan, Kommunikationsfreigabe und Abschlussbericht werden mit Zeitstempel geführt. Technische Logs, betroffene Systeme, Datenkategorien, Personenzahl, Eindämmung, Ursache und Lessons Learned gehören in eine konsistente Incident-Akte.

Abgrenzung: Für vertragliche Incident- und Providersteuerung `informationstechnologierecht/cybersecurity-managed-service-vertrag/`; für DSK-nahe Meldelogik `informationstechnologierecht/incident-response-meldung-dsk/`.

## Taktische Hinweise

Vorgehensreihenfolge: Als Erstes wird der Kenntniszeitpunkt mit Beleg fixiert (Alarm, Ticket, Meldung des Auftragsverarbeiters), denn an ihm hängt die gesamte 72-Stunden-Rechnung. Eindämmung und Beweissicherung laufen parallel, nicht nacheinander. Die Meldung geht auch bei unvollständiger Sachlage fristgerecht als vorläufige Erstmeldung hinaus; fehlende Angaben werden nach Art. 33 Abs. 4 DSGVO gestaffelt nachgereicht. Die Benachrichtigung betroffener Personen nach Art. 34 DSGVO wird getrennt geprüft (hohes Risiko, nicht bloß Risiko) und die Dokumentation nach Art. 33 Abs. 5 DSGVO wird auch dann geführt, wenn am Ende keine Meldepflicht bejaht wird.

Typische Einwände und Antwortlinien:

- „Wir melden erst, wenn die Forensik abgeschlossen ist." — Die Frist läuft ab Kenntnis der Verletzung, nicht ab vollständiger Aufklärung; wer wartet, riskiert einen eigenständigen Verstoß gegen Art. 33 DSGVO, obwohl die gestaffelte Meldung genau für diese Lage vorgesehen ist.
- „Die Meldung war verspätet." (Aufsichtsbehörde) — Antwortlinie ist die saubere Kenntniszeitpunkt-Argumentation: Kenntnis setzt hinreichende Gewissheit über das Vorliegen einer Verletzung voraus, nicht den ersten vagen Verdacht; der interne Verifikationszeitraum wird mit Zeitstempeln belegt und eine etwaige Überschreitung nach Art. 33 Abs. 1 Satz 2 DSGVO begründet.
- „Es besteht kein Risiko, also melden wir nicht." — Die Ausnahme greift nur, wenn die Verletzung voraussichtlich zu keinem Risiko führt; diese Prognose ist zu dokumentieren und hält bei exfiltrierten unverschlüsselten Daten regelmäßig nicht.
- „Die Meldung belastet uns im Bußgeldverfahren selbst." — Nach § 43 Abs. 4 BDSG darf die Meldung in einem Bußgeldverfahren gegen den Meldepflichtigen nur mit dessen Zustimmung verwendet werden; kooperatives Meldeverhalten wirkt zudem bei der Bußgeldzumessung nach Art. 83 Abs. 2 DSGVO mildernd.
- „Unser Cloud-Anbieter hat den Vorfall, nicht wir." — Die Meldepflicht gegenüber der Behörde trifft den Verantwortlichen; der Auftragsverarbeiter meldet nur an ihn (Art. 33 Abs. 2 DSGVO), und dessen Verzögerung entlastet nicht.

Erledigungs- und Einigungskorridor: Aufsichtsverfahren nach einer Meldung enden erfahrungsgemäß häufig ohne förmliche Maßnahme, wenn der Verantwortliche fristgerecht gemeldet, nachvollziehbar nachgemeldet, einen konkreten Maßnahmenplan mit Terminen vorgelegt und den Abschlussbericht geliefert hat; konfrontativ wird es vor allem bei verschleierten Zeitachsen und bei Diskrepanzen zwischen Meldung und späterer Presseberichterstattung.

Häufige Fehler:

- Der Kenntniszeitpunkt wird nicht dokumentiert und lässt sich später nur noch zulasten des Verantwortlichen rekonstruieren.
- Die Meldung geht an die falsche Aufsichtsbehörde, weil Hauptniederlassung und Betriebsstätte verwechselt werden.
- Die Meldung des Auftragsverarbeiters an den Verantwortlichen wird intern als erledigte Behördenmeldung abgelegt.
- Die Schwellen von Art. 33 (Risiko) und Art. 34 (hohes Risiko) werden gleichgesetzt, sodass entweder zu viel benachrichtigt oder zu wenig gemeldet wird.
- Die Zeitachse in Abschnitt 8 widerspricht den technischen Logdaten, was in einer späteren behördlichen Prüfung schwerer wiegt als die Verletzung selbst.

## Verwandte Vorlagen

- [Incident-Response-Meldung bei Datenschutzverletzungen (Art. 33/34 DSGVO)](../incident-response-meldung-dsk/) — Meldung entlang der DSK-Formularlogik, wenn die Behörde ein strukturiertes Online-Formular mit abweichender Feldstruktur verlangt.
- [Auftragsverarbeitungsvertrag (Art. 28 DSGVO; SDM)](../auftragsverarbeitungsvertrag-dsgvo/) — AVV mit dem Meldeweg des Auftragsverarbeiters nach Art. 33 Abs. 2 DSGVO, der dieser Meldung zeitlich vorgelagert ist.
- [Anlage TOM zum Auftragsverarbeitungsvertrag](../avv-tom-anlage-dsgvo/) — TOM-Anlage, deren Maßnahmenkatalog bei der Ursachenanalyse und den Abhilfemaßnahmen in Abschnitt 5 abgeglichen wird.
- [Klage auf immateriellen Schadensersatz (Art. 82 DSGVO)](../klage-schadensersatz-art-82-dsgvo/) — Klagevorlage der Gegenseite; zeigt, welche Angaben aus der Meldung später anspruchsbegründend verwendet werden.
- [Managed Cybersecurity Service Vertrag](../cybersecurity-managed-service-vertrag/) — Vertragliche Steuerung des Security-Dienstleisters, dessen Detektions- und Meldefristen den Zeitstrahl dieser Meldung bestimmen.
