---
name: code-of-practice-und-harmonisierte-normen
description: "Normen- und Standards-Landkarte für KI-VO-Compliance: Art. 40 harmonisierte Normen, Art. 41 gemeinsame Spezifikationen, Art. 56 GPAI Code of Practice, ISO/IEC 42001 / 23894 / 22989 / 23053 sowie Sicherheits- und Datenschutzstandards. Erklaert Vermutungswirkung nur bei im EU-Amtsblatt referenzierten harmonisierten Normen und nutzt ISO-Normen als Orientierung ohne falsche Konformitaetsvermutung. Output: standardsbasierter Massnahmenplan für KI-System, Hochrisiko oder GPAI."
---

# Verhaltenskodizes, harmonisierte Normen und ISO-Standards

## Zweck

Dieser Skill unterstützt die Compliance-Strategie für KI-Systeme, Hochrisiko-KI und GPAI-Modelle. Er trennt sauber:

- harmonisierte Normen nach Art. 40 KI-VO
- gemeinsame Spezifikationen nach Art. 41 KI-VO
- GPAI Code of Practice nach Art. 56 KI-VO
- internationale ISO/IEC-Standards als Orientierung

Wichtig: Nicht jede ISO-Norm ist automatisch eine harmonisierte Norm im Sinne der KI-VO. Eine Vermutungswirkung entsteht nur, soweit eine harmonisierte europäische Norm im Amtsblatt der EU referenziert ist und die einschlägigen Anforderungen abdeckt.

## Art. 40 KI-VO — harmonisierte Normen

Harmonisierte Normen konkretisieren KI-VO-Anforderungen technisch. Bei vollständiger Konformität mit einschlägigen, im EU-Amtsblatt veröffentlichten harmonisierten Normen wird die Konformität mit den abgedeckten Anforderungen vermutet.

Prüffragen:
- Gibt es für die konkrete KI-VO-Anforderung bereits eine harmonisierte Norm mit Amtsblatt-Fundstelle?
- Welche Anforderungen deckt sie ab: Risikomanagement, Datenqualität, technische Dokumentation, Logging, Transparenz, menschliche Aufsicht, Genauigkeit, Robustheit, Cybersicherheit, Qualitätsmanagement?
- Wurde die Norm vollständig umgesetzt oder nur als Orientierung genutzt?
- Gibt es Lücken, weil die Norm nicht alle Anforderungen abdeckt?

Dokumentationsregel:
- Nie pauschal schreiben "ISO-konform = KI-VO-konform".
- Immer benennen, welche Norm welche Anforderung abdeckt und ob eine EU-Vermutungswirkung besteht.

## Art. 41 KI-VO — gemeinsame Spezifikationen

Wenn harmonisierte Normen fehlen oder unzureichend sind, kann die Kommission gemeinsame Spezifikationen erlassen. Auch diese können für die praktische Compliance maßgeblich sein.

Prüffragen:
- Gibt es eine einschlägige gemeinsame Spezifikation?
- Ist sie verpflichtend oder gibt es eine begründete alternative technische Lösung?
- Wie wird Abweichung dokumentiert?

## Art. 56 KI-VO — GPAI Code of Practice

Für Anbieter von GPAI-Modellen ist der GPAI Code of Practice besonders relevant. Er kann als Brücke dienen, bis harmonisierte Normen und weitere sekundäre Rechtsakte die Pflichten konkretisieren.

Prüffragen:
- Ist der Mandant Anbieter eines GPAI-Modells?
- Hat er den Code of Practice gezeichnet oder befolgt?
- Deckt der Code technische Dokumentation, Copyright-Policy, Trainingsdaten-Zusammenfassung, Safety, Evaluierung und systemisches Risiko ab?
- Welche Lücken bleiben trotz Code?

## Standards-Landkarte

Diese Standards können als Arbeitsrahmen dienen, ohne automatisch KI-VO-Konformität zu beweisen:

| Standard | Nutzen im KI-VO-| Vorsicht |
|---|---|---|
| ISO/IEC 42001:2023 | AI Management System, Governance, Rollen, Richtlinien, kontinuierliche Verbesserung | nicht identisch mit allen KI-VO-Pflichten; keine Vermutungswirkung ohne harmonisierte Referenz |
| ISO/IEC 23894:2023 | AI Risk Management, Risikoidentifikation, Bewertung, Behandlung, Monitoring | an Art. 9 KI-VO anpassen, Grundrechte ausdrücklich ergänzen |
| ISO/IEC 22989:2022 | AI Concepts and Terminology | hilfreich für Begriffe, ersetzt nicht Art. 3 KI-VO |
| ISO/IEC 23053:2022 | Framework für KI-Systeme mit maschinellem Lernen | gut für technische Architektur- und Lifecycle-Beschreibung |
| ISO/IEC 27001:2022 | Informationssicherheits-Management | unterstützt Cybersicherheit, aber nicht spezifisch KI-VO |
| ISO/IEC 27701 | Datenschutz-Management als Erweiterung zu 27001/27002 | unterstützt DSGVO/Privacy, ersetzt keine KI-VO- oder DSFA-Prüfung |
| ISO/IEC 38507 | Governance implications of AI | Orientierung für Leitungs- und Aufsichtsgremien |

## Standards in die Sachprüfung einbauen

### Art. 3 KI-System-Check

Nutze ISO/IEC 22989 und 23053 nur als technische Begriffshilfe. Die rechtliche Definition bleibt Art. 3 Nr. 1 KI-VO. Dokumentiere besonders:
- maschinenbasiertes System
- Autonomiegrad
- Inferenz
- Output
- Umgebungseinfluss

### Art. 6 Abs. 2 / Anhang III

Standards helfen bei Risikomanagement und Kontrollen, entscheiden aber nicht allein über Hochrisiko. Die Hochrisiko-Klassifikation folgt Zweckbestimmung und Anhang III.

### Hochrisiko-Pflichten

Zuordnen:
- Art. 9 Risikomanagement: ISO/IEC 23894 plus KI-VO-Grundrechte
- Art. 10 Daten/Data Governance: Datenqualitäts- und Bias-Prozesse ergänzen
- Art. 11/Anhang IV Dokumentation: ISO/IEC 23053 als technische Strukturhilfe
- Art. 12 Logging: Sicherheits- und Audit-Standards ergänzend
- Art. 14 menschliche Aufsicht: Governance- und Human-oversight-Konzept gesondert
- Art. 15 Genauigkeit/Robustheit/Cybersicherheit: 27001/Threat-Modeling/Testkonzept ergänzend
- Art. 17 Qualitätsmanagement: ISO/IEC 42001 als Rahmen, KI-VO-spezifische Lücken schließen

## Output-Template — Normen- und Standardsplan

```text
NORMEN- UND STANDARDSPLAN KI-VO
Datum: [DATUM]
System / Modell: [NAME]
Risikoklasse: [Hochrisiko / begrenzt / GPAI / unklar]

1. Harmonisierte Normen Art. 40
[vorhanden / nicht vorhanden / Amtsblatt-Fundstelle offen]
[abgedeckte KI-VO-Anforderungen]

2. Gemeinsame Spezifikationen Art. 41
[vorhanden / nicht vorhanden / prüfen]

3. GPAI Code of Practice Art. 56
[einschlägig ja/nein; Umsetzung]

4. ISO/IEC-Arbeitsrahmen
- ISO/IEC 42001: [Governance-Maßnahmen]
- ISO/IEC 23894: [Risikomanagement-Maßnahmen]
- ISO/IEC 22989/23053: [Begriffe/Architektur]
- Sicherheits-/Datenschutzstandards: [27001/27701/weitere]

5. KI-VO-Lücken trotz Standards
[Grundrechte, Zweckbestimmung, Art. 6, Art. 10, Art. 14, Art. 26/27, Dokumentation]

6. Konformitätsaussage
[Welche Norm begründet Vermutungswirkung? Welche Standards sind nur Orientierung?]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 40, 41, 56 und 95 KI-VO sowie die jeweils aktuell im Amtsblatt der EU referenzierten harmonisierten Normen. Vor jeder finalen Aussage ist der Normenstand zu aktualisieren. Keine Rechtsberatung.

## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
