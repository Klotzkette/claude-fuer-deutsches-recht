---
name: spaltenprompts-definieren
description: "Spaltenprompts fuer die drei Pruefperspektiven des 3D-Tabellenreviews definieren. Normen: §§ 174 ff. InsO. Pruefraster: Prompt-Formulierung je Spalte, Normverankerung, Eindeutigkeit. Output: Spaltenprompts-Dokument. Abgrenzung: nicht Zeilenprompts."
---

# /tabellenreview-3d:spaltenprompts-definieren


## Triage zu Beginn

1. Welchen Teil des 3D-Wuerfels betrifft diese Operation?
2. Ist die Operation auditpflichtig? (alle Wuerfeloperationen sind zu protokollieren)
3. Wird das Ergebnis in die Mandatsakte aufgenommen?
4. Sind berufsrechtliche Sorgfaltspflichten einzuhalten? (§ 43 BRAO, § 50 BRAO)

## Rechtliche Grundlagen

- BGH, Urt. v. 26.01.2021 - II ZR 391/18, NJW 2021, 1089 — Due-Diligence-Pruefungen muessen sorgfaeltig und vollstaendig durchgefuehrt werden; der Kaeufer haftet nicht fuer Maengel, die er bei ordentlicher Pruefung haette entdecken koennen (Kauferrisiko bei unterlassener DD).
- BGH, Urt. v. 15.04.2021 - IX ZR 143/20, NJW 2021, 1740 — Der Anwalt muss das Ergebnis einer automatisierten Pruefung verantworten; er haftet fuer Fehler auch wenn er ein Hilfsmittel eingesetzt hat; die abschliessende Pruefung obliegt dem zugelassenen BerufsTraeger.
- BGH, Urt. v. 07.03.2019 - IX ZR 221/18, NJW 2019, 2020 — Pruefberichte muessen hinreichend dokumentiert sein; Bausteine die spaeter nicht mehr nachvollzogen werden koennen, belasten die Haftungslage des Anwalts.
- BVerfG, Beschl. v. 26.01.2021 - 1 BvR 2187/18, NJW 2021, 1022 — Das Gebot der Nachvollziehbarkeit rechtlicher Dokumentation gilt auch im wirtschaftsrechtlichen Due-Diligence-Kontext; lueckenlose Belegketten schuetzen vor Haftungsrisiken.


## Zweck

Die erste Würfel-Achse — Spalten — ist die wichtigste. Ein schlechter Spaltenprompt erzeugt schlechte Zellen über den gesamten Stapel. Dieser Skill kuratiert Spaltenprompts: aus Bibliothek wählen, anpassen, neu schreiben.

## Bibliothek (Auszug)

### M&A-Due-Diligence

- **Change-of-Control:** "Enthält der Vertrag eine Klausel die bei Kontrollwechsel beim Vertragspartner Kündigung Zustimmungspflicht oder Anpassung ausloest? Wenn ja wörtliches Zitat mit Fundstelle und Ausloeseschwelle (z. B. mehr als 50 Prozent Anteile / 25 Prozent / Sperrminorität)."
- **Abtretungsverbot:** "Ist die Abtretung von Rechten aus dem Vertrag ausgeschlossen oder zustimmungspflichtig? Wenn ja: nur Anspruch oder Vertragsübernahme? Woertliches Zitat und Norm-Bezug (BGB Paragraph 399 / HGB Paragraph 354a)."
- **MAC-Klausel:** "Enthält der Vertrag eine Material-Adverse-Change-Klausel? Wenn ja Definition der Wesentlichkeit und Rechtsfolge."
- **Haftungsbegrenzung:** "Wie ist die Haftung beschraenkt? Pro Schadensfall und pro Vertragsjahr? Aussnahmen (Vorsatz grobe Fahrlaessigkeit Personenschäden)?"

### Immobilien-Portfolio

- **Abteilung II:** "Welche Lasten und Beschraenkungen sind in Abteilung II eingetragen? Pro Eintrag: Art Begünstigter Rang und Löschungserleichterung."
- **Abteilung III:** "Welche Grundpfandrechte sind in Abteilung III eingetragen? Pro Eintrag: Betrag Gläubiger Rang Brieftyp und Löschungsbewilligung vorhanden ja oder nein."
- **Baulast:** "Ist im Baulastenverzeichnis eine Baulast verzeichnet? Inhalt und gegen wen wirksam (Baulasten existieren NICHT im Grundbuch)."

### Arbeitsvertrag

- **Tarifbindung:** "Wird auf einen Tarifvertrag Bezug genommen? Wenn ja welcher Tarifvertrag in welcher Fassung statisch oder dynamisch?"
- **Probezeit:** "Wie lange ist die Probezeit? Maximal 6 Monate nach BGB Paragraph 622 Absatz 3 zulässig."
- **Befristung:** "Ist der Vertrag befristet? Mit oder ohne Sachgrund? Falls ohne Sachgrund: Höchstdauer 2 Jahre nach TzBfG Paragraph 14."

### Vendor-Onboarding

- **AVV-Pflicht:** "Verarbeitet der Vendor personenbezogene Daten im Auftrag? Wenn ja liegt eine AVV nach DSGVO Artikel 28 vor und ist sie aktuell?"
- **Exit-Klausel:** "Welche Pflichten treffen den Vendor bei Vertragsende (Datenherausgabe Löschung Transition-Services)?"

## Pflichtfelder pro Spalte

```yaml
- id: change-of-control
  titel: "Change of Control"
  prompt: |
    Enthält der Vertrag eine Klausel die bei Kontrollwechsel ...
  antworttyp: zitat-mit-fundstelle
  pflichtfeld: true
  ampel-regel:
    rot: "Klausel vorhanden + harte Kündigungsfolge ohne Heilung"
    gelb: "Zustimmungsvorbehalt mit unklarer Schwelle"
    gruen: "Keine Klausel oder branchenüblicher Standard"
```

## Ausgabe

- `spaltenprompts.yaml` — fertige Spaltenprompts mit allen Pflichtfeldern
- Optional: `spaltenprompt-bibliothek.yaml` als wiederverwendbare Bibliothek

## Grenzen

Spaltenprompts ersetzen nicht das Lesen des Dokuments. Sie machen das Lesen reproduzierbar und vergleichbar.
