---
name: krankenversicherung-bescheid-rechnung
description: "Erstkontakt im Krankenversicherungsrecht: Bescheid analysieren, Rechnung prüfen, Frist sichern – GKV und PKV."
---

# Kaltstart: Krankenversicherung – Bescheid, Rechnung und Frist

## Skill-Zweck

Steuert den **Erstkontakt** mit einem Krankenversicherungsproblem. Er stellt sicher, dass vor jeder inhaltlichen Prüfung die operativen Grundfragen geklärt sind: Wer ist betroffen, welches Dokument liegt vor, welche Frist läuft und was muss heute entschieden werden. Erst danach verzweigt der Skill in spezialisierte Prüfprogramme.

## Rechtlicher Rahmen

- **SGB V** §§ 1–11 (Grundsätze, Solidarprinzip, Leistungsanspruch), § 13 (Kostenerstattung), § 19 (Ende der Mitgliedschaft)
- **SGB X** §§ 31 ff. (Verwaltungsakt), §§ 80 ff. (Widerspruchsverfahren), § 45 (Rücknahme begünstigender VA)
- **SGG** §§ 78 ff. (Widerspruchsverfahren), § 86b (einstweiliger Rechtsschutz), §§ 143–150 (Berufung)
- **VVG** §§ 192–208 (Private Krankenversicherung), §§ 14, 28 (Fälligkeit, Obliegenheiten)
- **MB/KK 2009** Abschnitt I–IV (Musterbedingungen PKV)
- Rechtsprechung: BSG, Grundsatz der Vorverlagerung des Rechtsschutzes (BSG B 1 KR 10/18 R)

## Kaltstart-Protokoll (6 Pflichtfragen)

1. **Rolle**: Ist die Person gesetzlich oder privat versichert? Handelt es sich um eine Versicherte, einen Leistungserbringer (Arzt, Krankenhaus), eine Arbeitgeberin, eine Behörde oder eine Kanzlei?
2. **Dokumententyp**: Liegt ein Ablehnungsbescheid (GKV), eine Leistungsabrechnung (PKV), eine Rechnung eines Leistungserbringers, eine Mahnung, ein MDK-Gutachten, ein Arztbrief oder ein Vertragsangebot vor?
3. **Fristsituation**: Wann wurde das Dokument zugestellt (§ 37 SGB X: Bekanntgabe, 3-Tage-Fiktion)? Ist die 1-Monats-Widerspruchsfrist (§ 84 SGG) bereits abgelaufen? Besteht ein Eilbedarf (§ 86b SGG)?
4. **Streitwert und Kostenfolge**: Wie hoch ist der Betrag? Überschreitet er die Berufungsgrenze (750 €, § 144 SGG)? Ist anwaltliche Vertretung notwendig oder wirtschaftlich?
5. **Verfahrensstand**: Erstantrag, Widerspruch, Klage, Berufung, Revision oder außergerichtliche Beschwerde (Kassenaufsicht, Ombudsmann)?
6. **Gewünschter Output**: Fristenplan, Bescheidanalyse, Widerspruchsentwurf, PKV-Leistungsschreiben, Laienerklärung oder Checkliste für die nächste Prüfung?

## Prüfprogramm

### Schritt 1 – Dokument einordnen
- GKV-Bescheid: Liegt ein Verwaltungsakt i.S.d. § 31 SGB X vor? Enthält er Rechtsbehelfsbelehrung (§ 36 SGB X)?
- PKV-Schreiben: Handelt es sich um eine Leistungsablehnung, eine Beitragsanpassung (§ 203 VVG) oder einen Tarifwechselhinweis?
- Arztrechnung: GOÄ/GOZ korrekt angewandt? Rechnungspflichtangaben (§ 12 GOÄ) vorhanden?

### Schritt 2 – Fristen sichern
- Widerspruchsfrist GKV: 1 Monat ab Bekanntgabe (§ 84 Abs. 1 SGG)
- Klagefrist: 1 Monat nach Widerspruchsbescheid (§ 87 SGG)
- PKV: Verjährungsfrist 3 Jahre (§ 195 BGB), Ausschlussfristen im Tarif prüfen
- Zustellung: 3-Tage-Fiktion (§ 37 Abs. 2 SGB X), bei Einschreiben Nachweis prüfen

### Schritt 3 – Materielle Vorprüfung
- Anspruchsgrundlage identifizieren (SGB V oder Versicherungsvertrag/Tarif)
- Ablehnungsgrund der Kasse herausarbeiten: fehlende Leistungspflicht, Wirtschaftlichkeit (§ 12 SGB V), Ausschluss, MDK-Empfehlung
- Gegenbeweis skizzieren: ärztliche Attest, Leitlinien, Fachliteratur

### Schritt 4 – Weiterleitungsempfehlung
- Skill kv-024 (Widerspruch), kv-025 (Eilverfahren), kv-029 (PKV-Leistungspflicht) oder spezialisierten Skill aufrufen

## Typische Fallen

- **Zustellungsfiktion übersehen**: Frist beginnt 3 Tage nach Aufgabe zur Post, nicht bei tatsächlichem Empfang.
- **Fehlende Rechtsbehelfsbelehrung**: Verlängert die Frist auf 1 Jahr (§ 66 Abs. 2 SGG), bedeutet aber nicht, dass kein Rechtsbehelf nötig ist.
- **GKV und PKV verwechseln**: Sachleistungsprinzip (GKV) vs. Kostenerstattungsprinzip (PKV) führen zu völlig unterschiedlichen Prüfpfaden.
- **Beitragsrückstand**: Ruhen der Leistung (§ 16 Abs. 3a SGB V) kann laufende Behandlungsansprüche blockieren – immer prüfen.
- **Scheingenauigkeit bei Normen**: Keine Fundstelle erfinden; bei Unsicherheit Live-Check empfehlen.

## Output-Formate

| Format | Wann sinnvoll |
|--------|--------------|
| Fristenkalender | Bei mehreren parallelen Fristen oder unklarer Zustellung |
| Bescheidanalyse | Ablehnungsbescheid liegt vor, Begründung unklar |
| Widerspruchsentwurf | Frist läuft, materieller Angriffspunkt identifiziert |
| PKV-Leistungsschreiben | Privatversicherter, Arztrechnung liegt vor |
| Laienerklärung | Versicherter versteht Bescheid nicht |
| Checkliste nächste Schritte | Erstberatung, Prioritäten noch unklar |

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen und Normen

- [§ 31 SGB X – Verwaltungsakt](https://www.gesetze-im-internet.de/sgb_10/__31.html)
- [§ 84 SGG – Widerspruchsfrist](https://www.gesetze-im-internet.de/sgg/__84.html)
- [§ 37 SGB X – Bekanntgabe](https://www.gesetze-im-internet.de/sgb_10/__37.html)
- [§ 12 SGB V – Wirtschaftlichkeitsgebot](https://www.gesetze-im-internet.de/sgb_5/__12.html)
- [§ 192 VVG – Leistungspflicht PKV](https://www.gesetze-im-internet.de/vvg_2008/__192.html)
- [BSG-Rechtsprechungsdatenbank](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [dejure.org – SGB V](https://dejure.org/gesetze/SGB_V)
## Schritt 5 – Dokumentation und Aktenführung

- Alle Schriftstücke chronologisch ablegen (Eingangsdatum notieren)
- Kopien vor Absendung anfertigen; Einschreiben/Rückschein für fristwahrende Schriftsätze
- Gesprächsnotizen bei telefonischen Auskünften der Kasse (Datum, Name, Inhalt)
- Fristenkalender mit 1-Woche-Voralarm führen

## Hinweis zur Beweisvorsorgepflicht

Im sozialgerichtlichen Verfahren gilt der **Amtsermittlungsgrundsatz** (§ 103 SGG); dennoch ist der Versicherte gut beraten, frühzeitig Beweise zu sichern:
- Ärztliche Atteste und Befundberichte zeitnah anfordern
- MDK-Gutachten stets anfordern (§ 276 Abs. 2 SGB V)
- Widerspruchsbegründung mit konkreten Nachweisen belegen
