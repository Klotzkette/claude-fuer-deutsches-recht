---
name: signaturweg-und-absender-pruefen
description: "Prüft für eine vorbereitete Versandmappe Verantwortung, tatsächlichen Versender, Postfach und Formroute. Unterscheidet persönlichen Versand mit einfacher Signatur vom berechtigten Personalversand mit qualifizierter elektronischer Signatur und dokumentiert offene Nachweise, ohne eine Signaturvalidierung vorzutäuschen."
---

# Signaturweg und Absender prüfen

## 1. Pflichtangaben

Ermittle aus Schriftsatz und Auftrag:

1. verantwortender Anwalt,
2. Name in der einfachen Signatur am Dokumentende,
3. tatsächlicher Versender,
4. persönliches Postfach oder Gesellschaftspostfach und konkrete Versandberechtigung,
5. einschlägige Verfahrensordnung,
6. gewählte Route `persönlich-sicher` oder `qualifizierte elektronische Signatur`.

Frage diese Punkte nur nach, soweit sie nicht bereits eindeutig vorliegen. Fasse die Frage zusammen: `Verantwortet und versendet [Name] persönlich aus seinem zugeordneten Postfach, oder wird das Dokument vor Versand qualifiziert elektronisch signiert?`

## 2. Formroute

ZPO Paragraf 130a Absatz 3 verlangt für das Hauptdokument entweder:

1. qualifizierte elektronische Signatur der verantwortenden Person oder
2. Signatur durch die verantwortende Person und Einreichung auf einem sicheren Übermittlungsweg.

Nur Anlagen zu vorbereitenden Schriftsätzen sind von dieser Signaturanforderung nach Satz 2 ausgenommen. Eine eigenständige formbedürftige Erklärung wird nicht allein durch die Bezeichnung „Anlage“ signaturfrei. Wähle bei Arbeits-, Sozial-, Verwaltungs-, Finanz- oder Strafverfahren die entsprechende Vorschrift und dokumentiere sie im Freigabevermerk; die ZPO-Ausnahme nicht ungeprüft übertragen.

## 3. Entscheidungsmatrix

| Verantwortung und Versand | Route | Status |
| --- | --- | --- |
| dieselbe Person, eigenes sicheres Postfach, Name im Dokument | persönlich-sicher | nach Schlusskontrolle möglich |
| berechtigter Mitarbeiter löst Versand mit eigenem Zugang aus | qualifizierte elektronische Signatur des Verantwortlichen | nach dokumentierter Signaturprüfung möglich; zusätzliche einfache Signatur nicht zwingend |
| anderer Anwalt versendet aus eigenem Postfach | qualifizierte elektronische Signatur des Verantwortlichen oder neue eindeutige Verantwortung | bis Klärung stop |
| Gesellschaftspostfach | Berechtigung nach RAVPV Paragraf 23 Absatz 3 und konkrete Formroute prüfen | nicht pauschal dem persönlichen Postfach gleichsetzen |
| Postfach oder Person unklar; Namenszeile fehlt bei einfacher Signatur | keine belegte Route | stop bis Klärung |

Eine Namensübereinstimmung beweist keine Versandberechtigung. Zugangsmittel und PIN des Anwalts nicht an Mitarbeiter weitergeben. Ein fremdes Postfach oder eine abweichende Namenszeile erfordern eine Routenprüfung, nicht automatisch ein Unwirksamkeitsurteil.

## 4. Grenze

Dieser Skill bringt keine qualifizierte elektronische Signatur an und behauptet nicht, eine Signatur technisch validiert zu haben. Er dokumentiert nur die getroffene Route und den Prüfstatus. Übergib das Ergebnis an `versandfreigabe-und-eingang-sichern`.

Signierte Originale byteidentisch erhalten, zugehörige abgesetzte Signaturdateien sichern und ihre Mitübermittlung prüfen. Nach Stempeln, OCR, Zusammenführen oder Neudruck gehört die bisherige Signaturprüfung nicht ohne Weiteres zur neuen Fassung. Für eine neue qES zuerst die endgültige PDF erzeugen, dann signieren und diese Fassung nicht mehr bearbeiten.

## 5. Quellen und Ergebnis

Nutze die [Form- und Technikregeln](../../references/ERVV-ERVB-VERSANDREGELN.md) mit amtlichen Normtexten und Betriebsinformationen. Dokumentiere Person, Postfachart, Route, finale Datei samt Hash und tatsächlich vorliegenden Prüfnachweis. Der kurze Freigabevermerk enthält vollständige Sätze und benennt bei Stop genau den fehlenden Nachweis; ein gesetztes Kontrollkästchen oder Werkzeugparameter ist kein Signaturprüfbericht.
