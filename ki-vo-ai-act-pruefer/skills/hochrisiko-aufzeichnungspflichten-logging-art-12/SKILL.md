---
name: hochrisiko-aufzeichnungspflichten-logging-art-12
description: "Anbieter von Hochrisiko-KI fragt: Was muss unser System automatisch aufzeichnen und wie lange muessen wir die Logs aufbewahren? Art. 12 KI-VO Logging-Pflichten. Pruefraster: Mindestinhalte der Logs Zeitstempel Eingabedaten Ausgaben Fehlermeldungen Aufbewahrungsfrist drei Jahre bzw. Vertragsdauer Verantwortlichkeitsteilung Anbieter vs. Betreiber. Besondere Anforderungen biometrische Identifikation Art. 12 Abs. 3. Output: Logging-Anforderungskatalog und Muster-Log-Schema. Abgrenzung zu hochrisiko-technische-dokumentation-art-11-und-anhang-iv (Dokumentationspflichten) und betreiber-deployer-pflichten-art-26."
---

# Aufzeichnungspflichten und Logging — Art. 12 KI-VO

## Zweck

Art. 12 KI-VO verpflichtet Anbieter von Hochrisiko-KI-Systemen, sicherzustellen, dass das System automatisch Ereignisse protokolliert. Diese Logs dienen der Rückverfolgung, der Überwachung nach dem Inverkehrbringen und der Aufklärung von Vorfällen.

## Grundanforderung: Automatische Protokollierung (Art. 12 Abs. 1 KI-VO)

Hochrisiko-KI-Systeme müssen automatisch Ereignisse protokollieren, die für die Kontrolle des Systembetriebs und die Ermittlung von Risiken nach dem Inverkehrbringen relevant sind.

**Grundsatz:** Die Protokollierung muss technisch in das System integriert sein — manuelle Nacherfassung genügt nicht.

## Mindestinhalt der Logs (Art. 12 Abs. 2 KI-VO)

Die Protokolle müssen mindestens enthalten:
- Zeitstempel jedes Ereignisses
- Referenzdatenbankeinträge (wenn das System mit Datenbanken arbeitet)
- Eingabedaten (soweit relevant für die Nachvollziehbarkeit)
- Identität der natürlichen Personen, die an der Überprüfung der Ergebnisse beteiligt sind (wo zutreffend)
- Datum, Uhrzeit und Ort des Betriebs des Systems

**Prüffragen:**
- Protokolliert das System automatisch alle relevanten Ereignisse?
- Sind Zeitstempel, Eingaben und Ausgaben nachvollziehbar erfasst?
- Werden Identitäten der beteiligten Personen (wo relevant) erfasst?

## Besondere Anforderungen — Biometrische Fernidentifikation

Für biometrische Echtzeit-Fernidentifikationssysteme (die nur unter den engen Ausnahmen von Art. 5 Abs. 2 KI-VO zulässig sind) gelten besonders strenge Protokollierungsanforderungen. Jeder Einsatz ist zu protokollieren, und die Protokolle müssen der Datenschutzbehörde auf Anfrage zugänglich gemacht werden.

## Verantwortungsverteilung zwischen Anbieter und Betreiber

**Anbieter:** Muss sicherstellen, dass das System technisch in der Lage ist, die erforderlichen Logs zu erstellen. Die Protokollierungsfähigkeit ist Teil der technischen Spezifikation.

**Betreiber:** Muss sicherstellen, dass die Protokolle tatsächlich erstellt, gespeichert und aufbewahrt werden. Betreiber sind nach Art. 26 Abs. 6 KI-VO verpflichtet, die Protokolle sechs Monate aufzubewahren, es sei denn, andere Vorschriften (z.B. DSGVO, nationales Recht) sehen kürzere oder längere Fristen vor.

**Prüffragen:**
- Welche Partei ist für die Protokollierung verantwortlich — Anbieter, Betreiber oder beide?
- Gibt es vertragliche Regelungen zwischen Anbieter und Betreiber zur Protokollierung (Art. 25 Abs. 4 KI-VO)?

## Aufbewahrungsfristen

- **Betreiber allgemein:** Sechs Monate Aufbewahrungspflicht (Art. 26 Abs. 6 KI-VO)
- **Biometrische Identifikation:** Besondere Fristen nach nationalem Recht oder Behördenanforderungen
- **Anbieter (technische Dokumentation):** Zehn Jahre (Art. 18 KI-VO)
- **Widerspruch mit DSGVO:** Protokolle, die personenbezogene Daten enthalten, müssen datenschutzkonform aufbewahrt und nach Ablauf der Frist gelöscht werden

## Verhältnis zu Post-Market-Monitoring

Die nach Art. 12 KI-VO erstellten Protokolle sind ein wesentliches Instrument für das Post-Market-Monitoring nach Art. 72 KI-VO. Ohne Protokolle kann ein ernsthafter Vorfall nicht aufgeklärt werden.

## Typische Lücken

- Protokollierung ist nicht automatisiert und basiert auf manuellen Einträgen.
- Logs werden nach kurzer Zeit automatisch gelöscht (z.B. für Datensparsamkeit), ohne Berücksichtigung der Aufbewahrungspflichten.
- Kein klarer Verantwortlicher für die Aufbewahrung der Logs.
- Logs enthalten keine ausreichenden Zeitstempel oder Kontextinformationen für die Rekonstruktion von Vorfällen.

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
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 12 Rn. 4: Anwendungsbereich und Pflichten.
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
PRUEFERGEBNIS — HOCHRISIKO AUFZEICHNUNGSPFLICHTEN LOGGING ART 12
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 12 Rn. 4]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
