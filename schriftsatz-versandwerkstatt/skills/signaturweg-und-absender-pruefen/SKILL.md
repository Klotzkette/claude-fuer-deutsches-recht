---
name: signaturweg-und-absender-pruefen
description: "Klärt vor der Freigabe die verantwortende Person, den tatsächlichen Versender, das verwendete sichere Postfach und die verfahrensbezogene Formroute; unterscheidet persönlichen sicheren Versand mit einfacher Signatur von der qualifizierten elektronischen Signatur, prüft die Namenszeile im Hauptdokument und stoppt bei fremdem Postfach, Mitarbeiter-Versand."
---

# Signaturweg und Absender prüfen

## 1. Pflichtangaben

Ermittle aus Schriftsatz und Auftrag:

1. verantwortender Anwalt,
2. Name in der einfachen Signatur am Dokumentende,
3. tatsächlicher Versender,
4. verwendetes persönlich zugeordnetes Postfach,
5. einschlägige Verfahrensordnung,
6. gewählte Route `persönlich-sicher` oder `qualifizierte elektronische Signatur`.

Frage diese Punkte nur nach, soweit sie nicht bereits eindeutig vorliegen. Fasse die Frage zusammen: `Verantwortet und versendet [Name] persönlich aus seinem zugeordneten Postfach, oder wird das Dokument vor Versand qualifiziert elektronisch signiert?`

## 2. Formroute

ZPO Paragraf 130a Absatz 3 verlangt für das Hauptdokument entweder:

1. qualifizierte elektronische Signatur der verantwortenden Person oder
2. Signatur durch die verantwortende Person und Einreichung auf einem sicheren Übermittlungsweg.

Anlagen benötigen danach keine eigene Signatur. Wähle bei Arbeits-, Sozial-, Verwaltungs-, Finanz- oder Strafverfahren die entsprechende Vorschrift der Verfahrensordnung und dokumentiere sie im Freigabevermerk.

## 3. Entscheidungsmatrix

| Verantwortung und Versand | Route | Status |
| --- | --- | --- |
| dieselbe Person, eigenes sicheres Postfach, Name im Dokument | persönlich-sicher | nach Schlusskontrolle möglich |
| Mitarbeiter löst Versand aus | qualifizierte elektronische Signatur des Verantwortlichen | ohne geprüfte Signatur stop |
| anderer Anwalt versendet aus eigenem Postfach | qualifizierte elektronische Signatur des Verantwortlichen oder neue eindeutige Verantwortung | bis Klärung stop |
| Postfach, Person oder Namenszeile unklar | keine Route | stop |

## 4. Grenze

Dieser Skill bringt keine qualifizierte elektronische Signatur an und behauptet nicht, eine Signatur technisch validiert zu haben. Er dokumentiert nur die getroffene Route und den Prüfstatus. Übergib das Ergebnis an `versandfreigabe-und-eingang-sichern`.
