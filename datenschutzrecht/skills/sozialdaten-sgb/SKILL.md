---
name: sozialdaten-sgb
description: "Bewertet einen Datenschutzvorfall bei Sozialleistungsträgern, Sozialversicherungen und sozialen Diensten nach den Sondervorschriften der Sozialgesetzbücher. Behandelt: Sozialdatenbegriff § 67 SGB X; Sozialgeheimnis § 35 SGB I; Verhältnis zur DSGVO; Meldepflicht nach § 83a SGB X; besondere Bußgeldvorschriften; Aufsichtsstruktur Bund/Länder. Output: Memo zur Meldepflicht-Doppelspur und Empfehlung. Abgrenzung: keine konkrete Behördenmeldung."
---

# Sozialdaten im Datenschutzvorfall — SGB I und SGB X

## Triage — kläre vor der Bearbeitung

1. Liegen Sozialdaten im Sinne § 67 SGB X vor?
2. Welche Stelle ist Verantwortlicher — Sozialleistungsträger, Krankenkasse, Berufsgenossenschaft?
3. Welche Aufsicht ist zuständig (Bundesbeauftragte oder Landesbeauftragte)?
4. Welche Meldewege überschneiden sich (DSGVO und SGB)?
5. Welche besonderen Strafvorschriften greifen (§ 85 SGB X)?
- Was will der Mandant wirklich erreichen? (Doppelmeldung sauber abwickeln; berufs- und beamtenrechtliche Folgen vermeiden)

## Rechtsgrundlagen

- **§ 35 SGB I** Sozialgeheimnis.
- **§ 67 SGB X** Definitionen.
- **§ 83a SGB X** Meldung Datenschutzverletzungen.
- **§ 85 SGB X** Bußgeldvorschriften.
- **Art. 33 DSGVO** allgemeine Meldepflicht.

## Aktuelle Rechtsprechung

Nicht aus Modellwissen; insbesondere zum Verhältnis § 83a SGB X zu Art. 33 DSGVO vor Ausgabe verifizieren.

## Zentrale Normen

§ 35; § 67; § 83a; § 85 SGB X; § 35 SGB I; Art. 33 DSGVO.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle (eur-lex.europa.eu, edpb.europa.eu, bfdi.bund.de, dejure.org, openjur.de, gesetze-im-internet.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. BeckRS-Fundstellen nur in Verbindung mit einer primaeren oder offenen Sekundaerquelle.

## Praxisformulierung — Doppelspur Meldung

DSGVO-Spur: Meldung an Aufsichtsbehörde (BfDI bei Bundesbehörde oder zuständige Landesbehörde).

SGB-Spur: zusätzliche Pflichten nach § 83a SGB X; ggf. Aufsicht durch Sozialministerium.

Berichtsformate parallel halten; Konsistenz beachten.

## Abgrenzung zu anderen Skills

- `dsv-aufnahme-statusinformation` bildet die strukturierte Erstaufnahme; dieser Skill setzt darauf auf.
- `dsv-meldung-art-33-pflichtangaben` deckt die Behördenmeldung ab; bei Bedarf zusätzlich ziehen.
- `dsv-benachrichtigung-art-34-betroffene` deckt die Benachrichtigung Betroffener ab.
- `dsv-bussgeldverteidigung-art-83` und `dsv-schadensersatz-art-82` decken die anwaltliche Nachbearbeitung ab.

- `dsv-art-9-besondere-kategorien` deckt Gesundheitsdaten ab.
- `dsv-paragraf-203-stgb-berufsgeheimnis` deckt aerztliches Geheimnis ab.
