# Incident-Response-Meldung bei Datenschutzverletzungen (Art. 33/34 DSGVO)
Protokoll und Meldevorlagen für Datenpannen: internes Erfassungsprotokoll, Meldung an die Aufsichtsbehörde (Art. 33), Betroffenenbenachrichtigung (Art. 34) und Verarbeitungsverzeichnis-Dokumentation (Art. 33 Abs. 5 DSGVO).

## Download
- [⬇ Incident Response Meldung bei Datenschutzverletzungen (Art. 33/34 DSGVO) – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/incident-response-meldung-dsk/incident-response-meldung-dsk.odt) — Offene Bürofassung (OpenDocument)
- [⬇ Incident Response Meldung bei Datenschutzverletzungen (Art. 33/34 DSGVO) – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/incident-response-meldung-dsk/incident-response-meldung-dsk.md.zip) — Bearbeitbare Markdown-Fassung, gepackt für direkten Download

Vorschau im Repository: [`incident-response-meldung-dsk.odt`](incident-response-meldung-dsk.odt) · [`incident-response-meldung-dsk.md`](incident-response-meldung-dsk.md)

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

Vorgehensreihenfolge: Teil A wird sofort bei Entdeckung eröffnet und mit Zeitstempeln geführt — er ist die Quelle, aus der alle späteren Teile schöpfen. Danach läuft die Dreifachspur: Eindämmung und Forensik (Sofortmaßnahmen in Teil A Ziffer 4), Risikobewertung nach den EDSA-Kriterien und parallel die Vorbereitung von Teil B, damit die Meldung binnen 72 Stunden auch bei unvollständiger Aufklärung hinausgehen kann. Teil C wird erst nach gesicherter Hochrisiko-Bewertung versandt, aber vorher textlich vorbereitet; Teil D wird in jedem Fall vervollständigt, auch wenn keine Meldepflicht bejaht wird. Vor jedem Versand läuft die Konsistenzprüfung nach Anlage 1.

Typische Einwände und Antwortlinien:

- „Erst intern klären, dann melden — sonst machen wir uns angreifbar." — Die Frist läuft ab Kenntnis; die gestufte Meldung (Erstmeldung mit angekündigter Ergänzung) ist der vorgesehene Weg, und § 43 Abs. 4 BDSG beschränkt die Verwendung der Meldung im Bußgeldverfahren gegen den Meldepflichtigen.
- „Die Passwörter waren gehasht, also kein Risiko." — Die Risikoaussage hängt von Hash-Verfahren, Salt und Angriffsszenario ab; eine pauschale Entwarnung ohne technische Bewertung trägt weder gegenüber der Behörde noch gegenüber Betroffenen.
- „Teil C alarmiert die Kunden unnötig, das übernimmt das Marketing weichgespült." — Art. 34 Abs. 2 DSGVO verlangt klare und einfache Sprache über Art und Folgen der Verletzung; eine beschönigte Benachrichtigung ist selbst ein Verstoß und wird in späteren Verfahren gegen das Unternehmen zitiert.
- „Der Vorfall liegt beim Dienstleister, wir warten auf dessen Bericht." — Die Meldung des Auftragsverarbeiters nach Art. 33 Abs. 2 DSGVO setzt die eigene Frist des Verantwortlichen in Gang; gewartet wird nicht auf den Abschlussbericht, sondern gemeldet nach Aktenstand.

Erledigungs- und Einigungskorridor: Behördenverfahren nach Meldungen enden regelmäßig ohne förmliche Maßnahme, wenn Zeitachse, Nachmeldungen und Maßnahmenplan konsistent sind und der Abschlussbericht pünktlich kommt; kritisch werden Verfahren bei Widersprüchen zwischen Meldung, Betroffenenbenachrichtigung und Pressekommunikation. Bei parallelen NIS2-, BSIG- oder DORA-Meldepflichten wird die Sachverhaltsdarstellung zentral geführt, damit alle Meldungen dieselben Fakten tragen.

Häufige Fehler:

- Teil A wird erst nachträglich rekonstruiert, und die Zeitstempel widersprechen den technischen Logs.
- Die Risikostufe wechselt zwischen Teil A, Teil B und der Entscheidung über Teil C, ohne dass die Änderung begründet wird.
- Die Ergänzungsmeldung wird angekündigt, aber nie versandt, sodass die Erstmeldung dauerhaft unvollständig bleibt.
- Teil C wird an alle Kunden statt an die betroffene Gruppe versandt oder umgekehrt zu eng gestreut.
- Teil D unterbleibt bei kein-Risiko-Vorfällen, obwohl Art. 33 Abs. 5 DSGVO gerade diese Dokumentation verlangt.

## Verwandte Vorlagen

- [Meldung einer Datenschutzverletzung](../data-breach-meldung-dsgvo/) — Alternative Meldevorlage im Fließformat, wenn kein Formularaufbau mit Teilen A bis D benötigt wird.
- [Auftragsverarbeitungsvertrag (Art. 28 DSGVO; SDM)](../auftragsverarbeitungsvertrag-dsgvo/) — AVV mit der Meldekette des Auftragsverarbeiters, die den Fristbeginn dieses Protokolls auslöst.
- [Anlage TOM zum Auftragsverarbeitungsvertrag](../avv-tom-anlage-dsgvo/) — TOM-Anlage als Maßstab für Ursachenanalyse und Präventionsmaßnahmen in Teil B Ziffer 6.
- [Managed Cybersecurity Service Vertrag](../cybersecurity-managed-service-vertrag/) — Vertragliche Steuerung des Security-Providers, dessen Detektionszeiten die 72-Stunden-Rechnung prägen.
- [Klage auf immateriellen Schadensersatz (Art. 82 DSGVO)](../klage-schadensersatz-art-82-dsgvo/) — Klageperspektive der Betroffenen, für die Teil C und Teil D später Beweismittel sind.
