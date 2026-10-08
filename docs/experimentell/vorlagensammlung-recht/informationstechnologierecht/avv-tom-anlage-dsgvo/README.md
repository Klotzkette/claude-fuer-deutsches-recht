# Anlage TOM zum Auftragsverarbeitungsvertrag

Technisch-organisatorische Maßnahmen als Anlage zum AVV mit Kontrollmatrix, Subunternehmern und Löschkonzept.

## Download
- [⬇ Anlage TOM zum Auftragsverarbeitungsvertrag – ODT herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/avv-tom-anlage-dsgvo/avv-tom-anlage-dsgvo.odt) — OpenDocument-Arbeitsfassung
- [⬇ Anlage TOM zum Auftragsverarbeitungsvertrag – Markdown (ZIP) herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/raw/main/docs/experimentell/vorlagensammlung-recht/informationstechnologierecht/avv-tom-anlage-dsgvo/avv-tom-anlage-dsgvo.md.zip) — Bearbeitbare Markdown-Fassung, gepackt für direkten Download

Vorschau im Repository: [`avv-tom-anlage-dsgvo.odt`](avv-tom-anlage-dsgvo.odt) · [`avv-tom-anlage-dsgvo.md`](avv-tom-anlage-dsgvo.md)

## Vorspruch und Nutzungsgrenze

Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Sie ist ein Struktur- und Formulierungsvorschlag, kein Gutachten und kein ungeprüft verwendbares Mandatsprodukt. Nutzung nur auf eigene Gewähr und eigene Gefahr; vor jedem Einsatz sind Sachverhalt, Rechtslage, Form, Fristen, Zuständigkeit, Vertretungsmacht, Datenschutz, Vollziehbarkeit und wirtschaftliche Folgen fachkundig zu prüfen, anzupassen und freizugeben.

Mandatsbezogene und personenbezogene Inhalte sind nach § 43a Abs. 2 BRAO, § 203 StGB und DSGVO zu schützen. Bei Verarbeitung in Drittsystemen sind Anonymisierung, Rechtsgrundlage, Auftragsverarbeitung und Löschkonzept zu prüfen.

Lizenz: Apache-2.0 OR MIT.

## Anwendungsbereich

Diese Vorlage gehört zur Auftragsverarbeitung nach Art. 28 DSGVO. Sie passt, wenn ein Dienstleister personenbezogene Daten weisungsgebunden verarbeitet und die Parteien Weisungen, TOM, Unterauftragnehmer, Unterstützung, Löschung, Rückgabe und Audit belastbar regeln müssen.

## Einschlägige Normen

- Art. 28 Abs. 3 DSGVO mit Pflichtkatalog zu Weisungen, Vertraulichkeit, TOM, Unterauftragnehmern, Unterstützung, Löschung, Rückgabe und Audits.
- Art. 28 Abs. 2 und Abs. 4 DSGVO zu Genehmigung und Flow-down bei Unterauftragnehmern.
- Art. 32 DSGVO zu technischen und organisatorischen Maßnahmen.
- Art. 33, Art. 34 DSGVO zu Verletzungsmeldung und Benachrichtigung betroffener Personen.
- Art. 82 DSGVO zur Haftung und § 280 Abs. 1 BGB für vertragliche Nebenpflichtverletzungen.

## Hinweise zur Verwendung

Der AVV ist kein Datenschutzanhang mit Überschriften, sondern der operative Weisungs- und Kontrollvertrag nach Art. 28 Abs. 3 DSGVO. Gegenstand, Dauer, Kategorien betroffener Personen, Datenarten, TOM, Unterauftragnehmer, Meldeweg, Audit, Löschung und Rückgabe müssen ausfüllbar und prüfbar sein.

Fristen- und Nachweisarchitektur: Unterauftragnehmerwiderspruch, Sicherheitsvorfallmeldung, Auskunftsunterstützung, TOM-Review, Auditfenster und Löschbestätigung werden getrennt terminiert. Bei Drittlandbezug wird zusätzlich die passende Transfer-Vorlage aus `informationstechnologierecht/standardvertragsklauseln-scc-begleitvereinbarung/` oder `informationstechnologierecht/dpf-lieferantenbestaetigung-usa-transfer/` genutzt.

Abgrenzung: TOM-Anlage `informationstechnologierecht/avv-tom-anlage-dsgvo/`; Datenlizenz mit eigener Verantwortlichkeit `informationstechnologierecht/datenverarbeitungs-und-datenlizenzvertrag-b2b/`.

## Taktische Hinweise

Vorgehensreihenfolge: Zuerst bestimmt der Verantwortliche den Schutzbedarf der konkreten Verarbeitung (Datenkategorien, betroffene Personen, Risikoszenarien), erst danach werden die Ist-Maßnahmen des Anbieters über Fragebogen, Zertifikate und Systemdokumentation abgefragt. Anschließend werden die neun Kontrollbereiche dieser Anlage befüllt, alle Platzhalterwerte (Passwortlänge, Sperrfristen, Backup-Intervalle, RTO und RPO) bewusst festgelegt und das Prüf- und Bewertungsschema der Anlage 1 durchlaufen. Unterzeichnet wird die TOM-Anlage zeitgleich mit dem AVV und mit versioniertem Stand, damit spätere Änderungen nachvollziehbar bleiben.

Typische Einwände des Anbieters und Antwortlinien:

- „Unser ISO-27001-Zertifikat ersetzt die TOM-Beschreibung." — Das Zertifikat belegt ein Managementsystem, nicht die konkreten Maßnahmen für genau diese Verarbeitung; ergänzend sind das Statement of Applicability und die verarbeitungsbezogene Ausfüllung der Tabellen zu verlangen.
- „Die TOM sind Geschäftsgeheimnis und werden nicht offengelegt." — Ohne prüffähige TOM kann der Verantwortliche seine Auswahl- und Kontrollpflicht aus Art. 28 Abs. 1 DSGVO nicht erfüllen; verhandelbarer Mittelweg ist die abgestufte Offenlegung unter Vertraulichkeitsschutz.
- „Unsere Maßnahmen ändern sich laufend, eine feste Anlage ist unpraktikabel." — Ein dynamischer Verweis auf eine Online-TOM-Seite ist nur akzeptabel mit ausdrücklichem Verschlechterungsverbot, Änderungsmitteilung in Textform und archivierten Versionsständen.
- „MFA und Verschlüsselung sind bei unseren Altsystemen nicht umsetzbar." — Dann sind kompensierende Maßnahmen, eine feste Übergangsfrist mit Endtermin und ein dokumentiertes Restrisiko zu vereinbaren, das der Verantwortliche ausdrücklich freigibt oder ablehnt.

Erledigungs- und Einigungskorridor: Üblich ist die Kombination aus Verschlechterungsverbot gegenüber dem unterzeichneten Stand, jährlichem TOM-Review mit Protokoll, abgestuftem Nachweissystem (Zertifikate und Berichte im Regelfall, Vor-Ort-Prüfung bei konkretem Anlass) und einer Frist von [Frist in Tagen] für die Schließung festgestellter Lücken.

Häufige Fehler:

- Die Beispielwerte in eckigen Klammern werden ungeprüft übernommen und damit Vertragsinhalt, obwohl sie zum Schutzbedarf des konkreten Falls nicht passen.
- Die Anlage übernimmt den Marketingtext des Anbieters, ohne dass ein einziger Nachweis (Auditbericht, Testprotokoll, Konfigurationsauszug) vorgelegt wurde.
- Die Subprozessoren-Tabelle in Ziffer 8 wird einmalig befüllt und nie fortgeschrieben, sodass Widerspruchsfristen ins Leere laufen.
- Die Fristen in Ziffer 8 (Mitteilung und Widerspruch) widersprechen den Fristen im AVV-Hauptteil, weil beide Dokumente getrennt verhandelt wurden.
- Das Löschkonzept in Ziffer 9 wird unterschrieben, obwohl Backups technisch erst nach der zugesagten Frist überschrieben werden.

## Verwandte Vorlagen

- [Auftragsverarbeitungsvertrag (Art. 28 DSGVO; SDM)](../auftragsverarbeitungsvertrag-dsgvo/) — Der AVV-Hauptvertrag, dessen Bestandteil diese TOM-Anlage nach Art. 28 Abs. 3 lit. c DSGVO ist.
- [Auftragsverarbeiter- und Subprocessor-Register für Datenschutz-Due-Diligence](../auftragsverarbeiter-subprocessor-register-due-diligence/) — Fortgeschriebenes Register der Unterauftragsverarbeiter, das die Momentaufnahme der Ziffer 8 dauerhaft pflegt.
- [Löschkonzept und Aufbewahrungsmatrix nach DSGVO](../loeschkonzept-dsgvo-aufbewahrung/) — Ausführliches Löschkonzept mit Aufbewahrungsfristen, das die Kurzregelung der Ziffer 9 vertieft.
- [Transfer Impact Assessment für SCC-Drittlandtransfer](../transfer-impact-assessment-scc-dsgvo/) — Transfer Impact Assessment, wenn Unterauftragsverarbeiter aus Ziffer 8 in Drittländern sitzen.
- [Meldung einer Datenschutzverletzung](../data-breach-meldung-dsgvo/) — Meldeformular nach Art. 33 DSGVO für den Fall, dass die hier beschriebenen Maßnahmen versagen.
