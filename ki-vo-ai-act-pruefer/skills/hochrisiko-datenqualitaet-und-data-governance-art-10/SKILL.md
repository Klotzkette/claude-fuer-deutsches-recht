---
name: hochrisiko-datenqualitaet-und-data-governance-art-10
description: "Anbieter von Hochrisiko-KI fragt: Welche Anforderungen gelten fuer unsere Trainings- Validierungs- und Testdaten und wie dokumentieren wir unsere Data Governance? Art. 10 KI-VO Datenqualitaet und Data Governance. Pruefraster: Relevanz Repraesentativitaet Vollstaendigkeit Fehlerfreiheit Bias-Minderung Ausnahme besondere Datenkategorien Art. 10 Abs. 5. Output: Data-Governance-Checkliste und Vorlage Trainingsdaten-Dokumentation. Abgrenzung zu hochrisiko-technische-dokumentation-art-11-und-anhang-iv (Gesamtdokumentation) und hochrisiko-risikomanagementsystem-art-9 (Risikobewertung)."
---

# Datenqualität und Data Governance — Art. 10 KI-VO

## Zweck

Art. 10 KI-VO stellt spezifische Anforderungen an die Daten, mit denen Hochrisiko-KI-Systeme trainiert, validiert und getestet werden. „Garbage in, garbage out" ist keine Entschuldigung — mangelhafte Datenqualität begründet einen Pflichtverstoß.

## Pflichten im Überblick (Art. 10 Abs. 2 KI-VO)

### Anforderung 1 — Geeignete Datenverwaltungspraktiken

Anbieter müssen geeignete Datenverwaltungspraktiken umsetzen, die Folgendes umfassen:
- Klare Festlegung des Entwicklungsziels und der vorgesehenen Verwendungszwecke
- Verfahren zur Datenerhebung
- Analyse auf mögliche Verzerrungen (Bias)
- Erkennung und Behebung von Datenlücken und Mängeln

**Prüffragen:**
- Gibt es eine schriftlich dokumentierte Datenstrategie?
- Wurden Herkunft, Erhebungsmethode und Qualitätsmerkmale der Datensätze dokumentiert?

### Anforderung 2 — Relevanz und Repräsentativität (Art. 10 Abs. 3 KI-VO)

Trainings-, Validierungs- und Testdatensätze müssen:
- Relevant für den vorgesehenen Zweck des Systems sein
- Repräsentativ für die Bedingungen sein, unter denen das System eingesetzt werden soll
- Hinreichend vollständig und fehlerfrei sein (unter Berücksichtigung des Einsatzbereichs)
- Die spezifischen Eigenschaften und Merkmale der vorgesehenen Einsatzsituation aufweisen

**Prüffragen:**
- Deckt der Datensatz die Vielfalt der Einsatzbedingungen ab?
- Sind bestimmte Bevölkerungsgruppen, Szenarien oder Randfälle unterrepräsentiert?
- Wurden bekannte Datenmängel dokumentiert und ihr Einfluss auf die Systemleistung bewertet?

### Anforderung 3 — Bias-Erkennung und Bias-Minderung (Art. 10 Abs. 2 lit. f KI-VO)

Anbieter müssen Daten auf mögliche Verzerrungen analysieren und geeignete Maßnahmen zur Bias-Minderung ergreifen. Dies gilt insbesondere bei Systemen, die auf Merkmale wie Alter, Geschlecht, ethnische Zugehörigkeit oder andere geschützte Kategorien zugreifen können.

**Prüffragen:**
- Wurden Bias-Analysen durchgeführt (z.B. Fairness-Metriken, Subgruppen-Analysen)?
- Sind die Maßnahmen zur Bias-Minderung dokumentiert und auf ihre Wirksamkeit geprüft?
- Welche Restverzerrungen verbleiben nach den Minderungsmaßnahmen?

### Anforderung 4 — Trennung der Datensätze

Trainings-, Validierungs- und Testdatensätze müssen klar voneinander getrennt sein. Insbesondere darf der Testdatensatz nicht für das Training oder die Parameteroptimierung verwendet worden sein.

**Prüffragen:**
- Sind die drei Datensätze klar getrennt und dokumentiert?
- Wurde der Testdatensatz ausschließlich für die abschließende Leistungsbeurteilung verwendet?

## Ausnahme für besondere Datenkategorien (Art. 10 Abs. 5 KI-VO)

Für die Zwecke der Erkennung und Korrektur von Verzerrungen in Hochrisiko-KI-Systemen ist die Verarbeitung besonderer Kategorien personenbezogener Daten nach Art. 9 Abs. 1 DSGVO (Rasse, Gesundheit, Religion, sexuelle Orientierung usw.) unter engen Voraussetzungen erlaubt:
- Wirksame technisch-organisatorische Sicherheitsvorkehrungen müssen vorhanden sein
- Die Verarbeitung darf ausschließlich zu diesem Zweck erfolgen
- Die Daten dürfen nicht zu anderen Zwecken verarbeitet werden
- Die Daten dürfen nicht übermittelt werden
- Die Daten sind nach Abschluss der Bias-Analyse zu löschen

**Prüffragen:**
- Liegt eine DSGVO-konforme Rechtsgrundlage für die Verarbeitung besonderer Kategorien vor?
- Sind die Sicherheitsvorkehrungen dokumentiert?
- Wird die Verarbeitung strikt auf den Bias-Korrekturzweck beschränkt?

## Verhältnis zu anderen Pflichten

Art. 10 KI-VO ist eng verzahnt mit:
- Art. 9 KI-VO (Risikomanagement — schlechte Daten erzeugen Risiken)
- Art. 11 und Anhang IV KI-VO (Technische Dokumentation — Datensätze sind zu beschreiben)
- DSGVO — Datenschutz gilt parallel für alle personenbezogenen Trainingsdaten

## Typische Praxisprobleme

- Trainingsdaten wurden nicht dokumentiert; keine Herkunftsnachweise.
- Test- und Validierungsdaten überlappen mit Trainingsdaten.
- Bias-Analyse wurde durchgeführt, aber Ergebnisse nicht dokumentiert.
- Besondere Datenkategorien wurden ohne DSGVO-Rechtsgrundlage verarbeitet.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- EuGH, Urt. v. 07.12.2023 — C-634/21 (SCHUFA-Score), NJW 2024, 248 Rn. 49: KI-Scoring-System als automatisierte Einzelentscheidung nach Art. 22 DSGVO — Masstab fuer Hochrisiko-Klassifikation und Betreiberpflichten nach KI-VO.
- EuGH, Urt. v. 04.10.2024 — C-203/22 (Dun & Bradstreet), NJW 2025, 56 Rn. 38: Betreiber muss Entscheidungslogik offenlegen — Art. 13 KI-VO Transparenzpflicht und Art. 26 Abs. 6 Korrekturrecht.
- BGH, Urt. v. 19.06.2018 — VI ZR 184/17, NJW 2018, 2877 Rn. 15: Organisationspflichten bei technischen Systemen — massgeblich fuer KI-VO Betreiberpflichten und interne Governance.
- EuGH, Urt. v. 16.07.2020 — C-311/18 (Schrems II), NJW 2020, 2557 Rn. 87: Drittlandtransfer bei KI-APIs erfordert Schutzgarantien; Art. 28 DSGVO AVV in KI-Lieferkette.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Kommentarliteratur
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 10 Rn. 6: Anwendungsbereich und Pflichten.
- Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 10: Wechselwirkung KI-VO und DSGVO.

## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Massnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — HOCHRISIKO DATENQUALITAET UND DATA GOVERNANCE ART 10
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 10 Rn. 6]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
