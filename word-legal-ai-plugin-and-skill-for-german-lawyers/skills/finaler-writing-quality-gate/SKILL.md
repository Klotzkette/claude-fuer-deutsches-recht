---
name: finaler-writing-quality-gate
description: "Finales Quality Gate für juristische Texte vor Versand. Prüft Rechtsfrage, Antrag oder Klauselzweck, Adressat, Stil, Zitate, Normen, Anlagen, Beweise, Fristen, Platzhalter, Zahlen, Namen, Datenschutz, Metadaten, Word-Hygiene und Versandfassung. Liefert Freigabeampel und letzte Reparaturliste im Word Legal Ai Plugin And Skill For German Lawyers: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Finaler Writing Quality Gate

## Arbeitsbereich

Finales Quality Gate für juristische Texte vor Versand. Prüft Rechtsfrage, Antrag oder Klauselzweck, Adressat, Stil, Zitate, Normen, Anlagen, Beweise, Fristen, Platzhalter, Zahlen, Namen, Datenschutz, Metadaten, Word-Hygiene und Versandfassung. Liefert Freigabeampel und letzte Reparaturliste. Die Prüfung konzentriert sich auf dieses Prüfungslinie und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: DSGVO Art. 33 Datenpanne 72h, ZPO § 130d aktive beA-Nutzung seit 01.01.2022, GwG § 8 Aufbewahrung 5 Jahre, KI-VO Art. 50 Kennzeichnung.
- Tragende Normen verifizieren: BRAO §§ 43a, 49b, DSGVO Art. 6, 28, 32, 35, BORA § 19a (technische Sorgfalt), beA-Bedingungen, ZPO § 130a (eVa), § 130d (aktive Nutzungspflicht), GwG § 8 Aufbewahrung — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anwalt, Sekretariat, IT-Verantwortlicher, Datenschutzbeauftragter, KI-Anbieter (Auftragsverarbeiter), Kammer.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Word-Dokumentvorlage, beA-Schriftsatz, AV-Vertrag mit KI-Anbieter, DSFA, Sicherheitskonzept, AGB-/Mandantenklauseln zu KI-Einsatz — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Dieser Skill ist der letzte Blick vor Versand. Er prüft nicht noch einmal alles dogmatisch von vorne, sondern fragt: Kann dieser Text jetzt so an Mandant, Gericht, Gegenseite oder Partnerin gehen?

## Ampelprüfung

| Ampel | Bedeutung |
|---|---|
| Grün | sendefähig nach kleiner Schlusskontrolle |
| Gelb | sendefähig nach konkreten Reparaturen |
| Rot | nicht versenden; Risiko, Fehler oder Lücke zu groß |

## Prüfungslinien

1. **Zweck:** Ist klar, was der Text erreichen soll?
2. **Adressat:** Passt Ton und Tiefe?
3. **Rechtsanker:** Sind Normen, Klauseln und Begriffe korrekt und nötig?
4. **Zitate:** Gibt es nur überprüfbare Rechtsprechung mit Gericht, Datum und Aktenzeichen?
5. **Sachverhalt:** Stimmen Namen, Daten, Beträge, Fristen und Rollen?
6. **Belege:** Stimmen Anlagenverweise und Beweisangebote?
7. **Struktur:** Ergebnis vorne, keine Wiederholungen, sinnvolle Überschriften.
8. **Sprache:** Keine Polemik, keine Platzhalter, keine leeren Floskeln.
9. **Word:** Formatvorlagen, Nummerierung, Track Changes, Kommentare, Metadaten.
10. **Versand:** richtige Fassung, richtiger Dateiname, richtige Anlagen.

## Harte Stopper

- Platzhalter im Text.
- Unverifizierte Rechtsprechungsfundstelle.
- Falscher Mandantenname oder falsche Parteirolle.
- Unklare Frist.
- Sichtbare interne Kommentare, wenn Clean Version versendet werden soll.
- Widerspruch zwischen Antrag und Begründung.
- Anlagenverweis auf nicht vorhandene Anlage.

## Output

```text
Freigabeampel: Gelb

Vor Versand reparieren:
1. ...
2. ...
3. ...

Kann danach raus als:
- clean PDF
- redline DOCX
- Mandantenmemo
```

## Querverweise

- `word-dokument-finish-und-layout`
- `deutscher-kanzleistil-kalibrieren`
- `schriftsatz-ueberarbeiten-richterlesbar`
- `englischer-vertrag-deutsches-recht`

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
