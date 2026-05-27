---
name: hochrisiko-art-6-abs-2-anhang-iii
description: "Unternehmen prueft ob sein KI-System in einen der acht sensiblen Anwendungsbereiche der KI-VO faellt. Art. 6 Abs. 2 i.V.m. Anhang III KI-VO Hochrisiko-Zuordnung. Pruefraster: Durchlauf aller acht Anhang-III-Bereiche Biometrie kritische Infrastruktur Bildung Beschaeftigung wesentliche Dienste Strafverfolgung Migration Justiz. Rueckausnahme Art. 6 Abs. 3 beachten. Output: strukturierte Zuordnungsentscheidung mit Begruendung je Bereich. Abgrenzung zu hochrisiko-art-6-abs-1-sicherheitsbauteil (Anhang-I-Sektorrecht) und rueckausnahme-art-6-abs-3 (Ausnahmen)."
---

# Hochrisiko-KI: Anhang III — Art. 6 Abs. 2 KI-VO (Entscheidungsbaum)

## Zweck

Art. 6 Abs. 2 KI-VO i.V.m. Anhang III ist der zweite und in der Praxis häufigste Pfad zur Hochrisiko-Einstufung. Dieser Skill geht alle acht Anhang-III-Bereiche systematisch durch.

## Prüfmethodik

Das System fragt den Nutzer für jeden der acht Bereiche, ob das KI-System in diesem Bereich tätig ist oder dort eingesetzt wird. Bereits bei einem positiven Treffer liegt (vorbehaltlich der Rückausnahme nach Art. 6 Abs. 3) Hochrisiko vor.

## Bereich 1 — Biometrische Identifikation und Kategorisierung (Anhang III Nr. 1)

**Systemtypen:**
- Biometrische Fernidentifikationssysteme (ausgenommen solche zur Strafverfolgungsverifizierung in Echtzeit, die unter Art. 5 fallen)
- Systeme zur biometrischen Kategorisierung nach biometrischen Daten
- Emotionserkennungssysteme (außerhalb von Art. 5-Verboten und außerhalb von sicherheits-/medizinischen Ausnahmen)

**Prüffragen:**
- Identifiziert oder verifiziert das System Personen anhand biometrischer Daten?
- Kategorisiert es Personen nach biometrischen Merkmalen?

## Bereich 2 — Kritische Infrastruktur (Anhang III Nr. 2)

**Systemtypen:**
- KI-Systeme zur Verwaltung und zum Betrieb kritischer Infrastruktur: Strom, Wasser, Gas, Wärme, Verkehr, Telekommunikation

**Prüffragen:**
- Wird das System für die Steuerung, Überwachung oder Verwaltung kritischer Infrastruktur eingesetzt?

## Bereich 3 — Bildung und Berufsausbildung (Anhang III Nr. 3)

**Systemtypen:**
- KI-Systeme zur Bestimmung des Zugangs zu Bildungseinrichtungen
- KI-Systeme zur Zuweisung zu Bildungseinrichtungen
- KI-Systeme zur Bewertung von Lernergebnissen (Prüfungen, Lernstandserhebungen)
- KI-Systeme zur Bewertung der Eignung von Schülern oder Studierenden
- KI-Systeme zur Überwachung unzulässigen Verhaltens bei Prüfungen

**Prüffragen:**
- Entscheidet das System über Zulassung, Bewertung oder Zugang in Bildungskontexten?

## Bereich 4 — Beschäftigung und Arbeitnehmerverwaltung (Anhang III Nr. 4)

**Systemtypen:**
- KI-Systeme für die Personalauswahl (Recruiting, Screening)
- KI-Systeme für Beförderungsentscheidungen
- KI-Systeme für Aufgabenverteilung und Leistungsüberwachung
- KI-Systeme für Kündigungsentscheidungen oder zur Bewertung des Leistungsverhaltens

**Prüffragen:**
- Wird das System für Entscheidungen über Beschäftigungsverhältnisse eingesetzt?
- Bewertet es Mitarbeitende oder trifft automatisierte Entscheidungen über Beschäftigte?

## Bereich 5 — Wesentliche private und öffentliche Dienstleistungen (Anhang III Nr. 5)

**Systemtypen:**
- KI-Systeme für Kreditwürdigkeitsprüfung und Bonitätsbewertung (Ausnahme: Betrugsaufdeckung)
- KI-Systeme für Risikobewertung bei Versicherungen (Leben und Kranken)
- KI-Systeme für die Beurteilung und Klassifizierung von Notrufen
- KI-Systeme für die Gewährung von Sozialleistungen oder öffentlicher Unterstützung
- KI-Systeme für die Bewertung des Bedarfs an Sozialhilfe

**Prüffragen:**
- Entscheidet das System über Kreditvergabe, Versicherungsleistungen, Sozialleistungen oder Notfallpriorisierung?

## Bereich 6 — Strafverfolgung (Anhang III Nr. 6)

**Systemtypen:**
- Risikoabschätzung und Profiling im Strafverfolgungskontext (mit individuellen Hinweisen)
- Polygraphenähnliche Systeme zur Vertrauenswürdigkeitsbewertung
- Bewertung der Zuverlässigkeit von Beweismitteln
- Vorhersage von Straftaten in Gebieten (geographisches Predictive Policing)
- Profiling in Strafverfolgung und Strafverfolgungsassistenz

**Prüffragen:**
- Wird das System von Strafverfolgungsbehörden für Risikoabschätzung, Profiling oder Beweismittelbewertung genutzt?

## Bereich 7 — Migration, Asyl und Grenzkontrolle (Anhang III Nr. 7)

**Systemtypen:**
- Risikoabschätzungssysteme für Personen, die EU-Grenzen überschreiten
- Systeme zur Überprüfung der Echtheit von Dokumenten
- Systeme zur Prüfung von Asyl- und Aufenthaltsanträgen
- Systeme zur Überwachung und Vorhersage von Migrationsbewegungen

**Prüffragen:**
- Wird das System für Grenzkontrollen, Asylverfahren oder Migrationsbehörden eingesetzt?

## Bereich 8 — Justiz und demokratische Prozesse (Anhang III Nr. 8)

**Systemtypen:**
- KI-Systeme zur Unterstützung von Richtern oder Staatsanwälten bei der Bewertung von Beweisen oder Erstellung von Urteilen
- KI-Systeme zur Beeinflussung von Wahlen oder zur personalisierten politischen Werbung

**Prüffragen:**
- Wird das System in Gerichtsverfahren oder politischen Prozessen eingesetzt?

## Nächste Schritte

- **Mindestens ein Bereich zutreffend:** → Hochrisiko nach Art. 6 Abs. 2 i.V.m. Anhang III KI-VO. Prüfe Rückausnahme: → `rueckausnahme-art-6-abs-3`
- **Kein Bereich zutreffend:** → Kein Hochrisiko nach Art. 6 Abs. 2. Prüfe begrenztes Risiko: → `begrenztes-risiko-art-50-transparenzpflichten`

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
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 6 Abs. 2 Rn. 8: Anwendungsbereich und Pflichten.
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
PRUEFERGEBNIS — HOCHRISIKO ART 6 ABS 2 ANHANG III
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 6 Abs. 2 Rn. 8]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
