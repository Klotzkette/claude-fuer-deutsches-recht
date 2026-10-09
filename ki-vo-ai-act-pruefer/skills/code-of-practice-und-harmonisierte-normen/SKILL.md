---
name: code-of-practice-und-harmonisierte-normen
description: "Für Verhaltenskodizes, harmonisierte Normen und ISO-Standards: ordnet Norm, Beweislast und Gegenargument; Ergebnis: Tatbestands- oder Anspruchsmatrix."
---

# Verhaltenskodizes, harmonisierte Normen und ISO-Standards

## Zweck

Unterstützt die Compliance-Strategie für KI-Systeme, Hochrisiko-KI und GPAI-Modelle. Er trennt sauber:

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

Artikel 41 Absatz 3 begründet eine abdeckungsbezogene Vermutung bei Einhaltung einschlägiger gemeinsamer Spezifikationen. Nach Absatz 5 muss ein Anbieter bei Nichtbefolgung hinreichend gleichwertige technische Lösungen nachweisen; keine beliebige Abweichungsfreiheit annehmen.

## Art. 56 KI-VO — GPAI Code of Practice

Für Anbieter von GPAI-Modellen ist der GPAI Code of Practice besonders relevant. Er kann als Brücke dienen, bis harmonisierte Normen und weitere sekundäre Rechtsakte die Pflichten konkretisieren.

Prüffragen:
- Ist der Mandant Anbieter eines GPAI-Modells?
- Hat er den Code of Practice gezeichnet oder befolgt?
- Deckt der Code technische Dokumentation, Copyright-Policy, Trainingsdaten-Zusammenfassung, Safety, Evaluierung und systemisches Risiko ab?
- Welche Lücken bleiben trotz Code?

Artikel 53 Absatz 4 und Artikel 55 Absatz 2 unterscheiden den Nachweis über Praxisleitfäden von der Vermutung bei Einhaltung einer einschlägigen harmonisierten Norm. Bloßes Zeichnen eines Kodex begründet keine automatische umfassende Konformität. Transparenzkodex nach Artikel 50 Absatz 7 und GPAI-Kodex nach Artikel 56 getrennt behandeln.

## Standards-Landkarte

Diese Standards können als Arbeitsrahmen dienen, ohne automatisch KI-VO-Konformität zu beweisen:

| Standard | Nutzen im KI-VO-| Vorsicht |
|---|---|---|
| ISO/IEC 42001:2023 | AI Management System, Governance, Rollen, Richtlinien, kontinuierliche Verbesserung | nicht identisch mit allen KI-VO-Pflichten; keine Vermutungswirkung ohne harmonisierte Referenz |
| ISO/IEC 23894:2023 | AI Risk Management, Risikoidentifikation, Bewertung, Behandlung, Monitoring | an Art. 9 KI-VO anpassen, Grundrechte ausdrücklich ergänzen |
| ISO/IEC 22989:2022 | AI Concepts and Terminology | hilfreich für Begriffe, ersetzt nicht Art. 3 KI-VO |
| ISO/IEC 23053:2022 | Framework für KI-Systeme mit maschinellem Lernen | gut für technische Architektur- und Lifecycle-Beschreibung |
| ISO/IEC 27001:2022 | Informationssicherheits-Management | unterstützt Cybersicherheit, aber nicht spezifisch KI-VO |
| ISO/IEC 27701 | Datenschutzmanagement nach der konkret vorgelegten Ausgabe | unterstützt DSGVO/Privacy, ersetzt keine KI-VO- oder DSFA-Prüfung |
| ISO/IEC 38507 | Governance implications of AI | Orientierung für Leitungs- und Aufsichtsgremien |

Die Zuordnungen sind mögliche Arbeitshilfen, keine Aussage, dass ein ungelesener Standardabschnitt erfüllt sei. Konkrete Ausgabe und zugänglichen Volltext verlangen. Artikel 9 ist systembezogen, Artikel 17 betrifft Anbieter-Qualitätsmanagement und Artikel 27 die Folgenabschätzung bestimmter Betreiber. Ein universelles Risikoregister oder ISO-Zertifikat ersetzt diese unterschiedlichen Produkte nicht. [Normenabdeckung prüfen](../harmonisierte-normen-gap-uebergang/SKILL.md).

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
Prüfpfade: [Hochrisiko ja/nein/offen; Artikel 50 ja/nein/offen; GPAI gesondert]

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

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen- und Aktualitätshinweis

Normabgleich: 9. Oktober 2026. Maßgeblich sind Art. 40, 41, 56 und 95 KI-VO sowie die jeweils aktuell im Amtsblatt der EU referenzierten harmonisierten Normen. Vor jeder finalen Aussage ist der Normenstand zu aktualisieren. Keine Rechtsberatung.
