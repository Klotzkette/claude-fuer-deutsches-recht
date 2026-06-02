---
name: dsv-art-9-besondere-kategorien
description: "Bewertet einen Datenschutzvorfall mit besonderen Kategorien personenbezogener Daten nach Art. 9 DSGVO. Behandelt: rassische/ethnische Herkunft; politische Meinungen; religiöse/weltanschauliche Überzeugungen; Gewerkschaftszugehörigkeit; genetische und biometrische Daten zur eindeutigen Identifizierung; Gesundheitsdaten; Daten zum Sexualleben oder zur sexuellen Orientierung. Folgen: regelmäßige Annahme hohen Risikos; Benachrichtigung Art. 34 DSGVO; Bußgeldverschärfung Art. 83 Abs. 5. Output: Memo mit Schutzbedarfsanalyse. Abgrenzung: § 203 StGB getrennt; Sozialdaten getrennt."
---

# Besondere Kategorien Art. 9 DSGVO im Datenschutzvorfall

## Triage — kläre vor der Bearbeitung

1. Liegen Daten im Sinne Art. 9 Abs. 1 DSGVO vor — wenn ja welche konkret?
2. Wie viele Betroffene und welche Mengen?
3. Sind die Daten im Klartext oder verschlüsselt oder pseudonymisiert?
4. Welche besondere Aufsicht (Sektorbehörde) ist zuständig?
5. Welche besondere Bußgeldhöhe droht (Art. 83 Abs. 5 DSGVO)?
- Was will der Mandant wirklich erreichen? (Schadensbegrenzung; rechtskonforme Benachrichtigung)

## Rechtsgrundlagen

- **Art. 9 Abs. 1 DSGVO** Verbot mit Erlaubnisvorbehalt; **Art. 9 Abs. 2 DSGVO** Ausnahmen.
- **Art. 34 Abs. 1 DSGVO** Benachrichtigung bei hohem Risiko — bei Art. 9 regelmäßig zu bejahen.
- **Art. 83 Abs. 5 lit. a DSGVO** verschärfter Bußgeldrahmen bis 20 Mio. EUR oder 4 Prozent.
- **Erwägungsgrund 75 DSGVO** besondere Risiken bei sensiblen Daten.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zu Gesundheitsdaten-Leaks und Bußgeldhöhen vor Ausgabe verifizieren.

## Zentrale Normen

Art. 9 Abs. 1; Art. 9 Abs. 2; Art. 34 Abs. 1; Art. 83 Abs. 5 lit. a DSGVO; Erwägungsgrund 75.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Schutzbedarfsanalyse Art. 9

Welche Kategorie liegt vor; in welcher Form (Klartext / pseudonymisiert / verschlüsselt); welche Anzahl; welche Folgen sind plausibel.

Conclusion: bei Art. 9-Daten im Klartext regelmäßig Meldung Art. 33 und Benachrichtigung Art. 34; Begründung schriftlich für die Akte.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-paragraf-203-stgb-berufsgeheimnis` deckt strafrechtliche Geheimnistraeger ab.
- `dsv-sozialdaten-sgb` deckt Sozialdaten ab.
