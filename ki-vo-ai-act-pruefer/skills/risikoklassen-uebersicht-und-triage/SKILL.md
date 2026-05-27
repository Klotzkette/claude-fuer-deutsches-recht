---
name: risikoklassen-uebersicht-und-triage
description: "Nutzer weiss nicht in welche Risikoklasse das KI-System faellt und muss schnell eine Ersteinschaetzung erhalten. Art. 5 Art. 6 Anhang III Art. 50 KI-VO vier Risikoklassen. Pruefraster: verbotene Praktiken Art. 5 Hochrisiko Art. 6 begrenztes Risiko Art. 50 minimales Risiko. Systematischer Entscheidungsbaum mit klaren Verzweigungen und Weiterleitung zu Detailskills. Output: Risikoklassen-Erstdiagnose. Abgrenzung zu entscheidungsbaum-ki-vo-gesamt-workflow (vollstaendiger Pruefpfad) und triage-ki-vo-vorpruefung (Einstiegsinterview)."
---

# Risikoklassen-Übersicht und Triage — KI-VO

## Zweck

Die KI-VO kennt keine einheitlichen Pflichten für alle KI-Systeme. Sie unterscheidet vier Risikokategorien mit stark unterschiedlichen Rechtsfolgen. Dieser Skill liefert den Entscheidungsbaum, mit dem die zutreffende Kategorie ermittelt wird.

## Die vier Kategorien im Überblick

| Kategorie | Rechtsgrundlage | Rechtsfolge |
|---|---|---|
| Verboten | Art. 5 KI-VO | Komplettverbot; keine Ausnahmen für verbotene Praktiken |
| Hochrisiko | Art. 6 i.V.m. Anhang I oder III KI-VO | Umfangreiche Pflichtenkataloge vor Inverkehrbringen |
| Begrenzt | Art. 50 KI-VO | Transparenzpflichten (Chatbot-Hinweis, Deepfake-Kennzeichnung) |
| Minimal | Keine Spezialregelung | Keine zusätzlichen KI-VO-Pflichten; freiwillige Verhaltenskodizes möglich |

## Entscheidungsbaum

### Schritt 1 — Verbotene Praktik?

Frage: Weist das System eines der folgenden Merkmale auf?
- Sublimale oder unterschwellige Techniken zur unbewussten Verhaltensbeeinflussung (Art. 5 Abs. 1 lit. a KI-VO)
- Ausnutzung von Schwächezuständen (Alter, Behinderung, soziale Lage) zur Verhaltensbeeinflussung (Art. 5 Abs. 1 lit. b KI-VO)
- Social-Scoring-Systeme für öffentliche Behörden oder in deren Auftrag (Art. 5 Abs. 1 lit. c KI-VO)
- Predictive Policing auf Basis von Persönlichkeitsmerkmalen ohne individuelle Hinweise (Art. 5 Abs. 1 lit. d KI-VO)
- Biometrische Fernidentifikation in Echtzeit im öffentlichen Raum durch Strafverfolgungsbehörden außerhalb der Ausnahmen (Art. 5 Abs. 1 lit. h KI-VO)
- Biometrische Kategorisierung nach sensiblen Merkmalen (Rasse, politische Meinung, Religion etc.) (Art. 5 Abs. 1 lit. g KI-VO)
- Emotionserkennung am Arbeitsplatz oder in Bildungseinrichtungen (Art. 5 Abs. 1 lit. f KI-VO)
- Untargeted Scraping von Gesichtsbildern aus dem Internet oder Überwachungskameras zum Aufbau von Datenbanken (Art. 5 Abs. 1 lit. e KI-VO)

**Wenn ja zu einem oder mehreren Punkten:** → `verbotene-praktiken-art-5` (Detailprüfung); Ergebnis: System ist verboten, darf nicht in Betrieb genommen werden.

**Wenn nein:** → weiter zu Schritt 2.

### Schritt 2 — Hochrisiko-KI?

**Pfad A (Art. 6 Abs. 1 KI-VO):**
Frage: Ist das KI-System ein Sicherheitsbauteil eines Produkts, das unter eine der in Anhang I genannten Unionsvorschriften fällt, und unterliegt es für dieses Produkt einer Konformitätsbewertung durch Dritte?
- Wenn ja → Hochrisiko nach Art. 6 Abs. 1 KI-VO → `hochrisiko-art-6-abs-1-sicherheitsbauteil`

**Pfad B (Art. 6 Abs. 2 KI-VO):**
Frage: Ist das KI-System in Anhang III der KI-VO in einem der acht Bereiche aufgeführt oder fällt es unter die Beschreibung eines dieser Bereiche?
- Bereiche: biometrische Identifikation, kritische Infrastruktur, Bildung, Beschäftigung, wesentliche Dienstleistungen (Kredit, Sozialleistungen), Strafverfolgung, Migration, Justiz
- Wenn ja → Hochrisiko nach Art. 6 Abs. 2 i.V.m. Anhang III KI-VO → `hochrisiko-art-6-abs-2-anhang-iii`

**Rückausnahme Art. 6 Abs. 3 KI-VO:**
Greift eine der vier Rückausnahmen? → `rueckausnahme-art-6-abs-3`

**Wenn Hochrisiko bestätigt:** → Pflichten nach Art. 9 bis 15 KI-VO (Anbieter), Art. 26 und 27 KI-VO (Betreiber)

**Wenn nein:** → weiter zu Schritt 3.

### Schritt 3 — Begrenztes Risiko?

Frage: Trifft eines der folgenden Merkmale zu?
- Das System ist ein Chatbot oder ein System, das direkt mit natürlichen Personen interagiert, ohne Emotionserkennung oder biometrische Kategorisierung?
- Das System erzeugt Deepfakes (KI-generierte Bilder, Videos, Audio mit Ähnlichkeit zu realen Personen)?
- Das System erzeugt Texte, die öffentlich zugänglich sind, ohne erkennbar als KI-generiert zu sein?

**Wenn ja:** → Transparenzpflichten nach Art. 50 KI-VO → `begrenztes-risiko-art-50-transparenzpflichten`

**Wenn nein:** → Schritt 4.

### Schritt 4 — Minimales Risiko

Alle anderen KI-Systeme haben minimales Risiko. Keine spezifischen KI-VO-Pflichten. Freiwillige Verhaltenskodizes nach Art. 95 KI-VO sind möglich und können empfohlen werden.

## Hinweis zur Parallelprüfung

Ein System kann gleichzeitig mehreren Kategorien zugehören — etwa ein Hochrisiko-KI-System, das zugleich Chatbot-Eigenschaften hat (begrenzt) und damit sowohl umfangreichen Hochrisiko-Pflichten als auch Art. 50-Transparenzpflichten unterliegt.

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
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 5-6 Rn. 1: Anwendungsbereich und Pflichten.
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
PRUEFERGEBNIS — RISIKOKLASSEN UEBERSICHT UND TRIAGE
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 5-6 Rn. 1]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
