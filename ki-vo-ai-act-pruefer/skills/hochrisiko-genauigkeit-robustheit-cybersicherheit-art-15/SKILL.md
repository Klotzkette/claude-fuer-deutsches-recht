---
name: hochrisiko-genauigkeit-robustheit-cybersicherheit-art-15
description: "Anbieter von Hochrisiko-KI fragt: Welche Leistungsstandards fuer Genauigkeit Robustheit und Cybersicherheit muessen wir nachweisen und dokumentieren? Art. 15 KI-VO Mindeststandards. Pruefraster: Genauigkeitsmetriken und Leistungserklaerung Fehlertoleranz-Anforderungen Resilienz gegen adversarielle Eingaben Datenvergiftung Modell-Extraktion Backdoor-Angriffe. Output: Anforderungskatalog und Muster-Testprotokolle. Abgrenzung zu hochrisiko-risikomanagementsystem-art-9 (Risikobewertung) und hochrisiko-konformitaetsbewertung-art-43-bis-49 (Bewertungsverfahren)."
---

# Genauigkeit, Robustheit und Cybersicherheit — Art. 15 KI-VO

## Zweck

Art. 15 KI-VO stellt Mindestanforderungen an die technische Zuverlässigkeit von Hochrisiko-KI-Systemen. Das System muss eine angemessene Genauigkeit erreichen, robust gegenüber Fehlern und Störungen sein und gegen Cyberangriffe geschützt werden.

## Anforderung 1 — Angemessene Genauigkeit (Art. 15 Abs. 1 KI-VO)

Hochrisiko-KI-Systeme müssen hinsichtlich ihrer Leistung, einschließlich der Genauigkeit, Robustheit und Cybersicherheit, auf das Niveau gebracht werden, das im Hinblick auf ihren Verwendungszweck angemessen ist und dem Stand der Technik entspricht.

**Prüffragen:**
- Wurden Leistungsmetriken definiert und gemessen (Genauigkeit, Präzision, Recall, F1-Score, AUC usw.)?
- Entspricht die erzielte Leistung dem Stand der Technik für den jeweiligen Anwendungsfall?
- Wurden Leistungsniveaus im Vergleich zu Baseline-Systemen oder Industriestandards gemessen?

**Hinweis:** Die KI-VO schreibt keine konkreten Schwellenwerte vor — dies soll durch harmonisierte Normen und technische Spezifikationen konkretisiert werden. Bis dahin gilt der Stand der Technik als Maßstab.

## Anforderung 2 — Robustheit und Fehlertoleranz (Art. 15 Abs. 3 KI-VO)

Das System muss so resilient wie möglich gegen Fehler, Störungen oder Inkonsistenzen sein, die innerhalb des Systems oder in seiner Umgebung auftreten können. Es muss vorhersehbaren Fehlerszenarien standhalten.

**Maßnahmen zur Robustheit:**
- Redundanz-Mechanismen für kritische Systemfunktionen
- Fallback-Verhalten bei Datenmängeln oder Systemausfällen
- Graceful Degradation: Das System reagiert auf Störungen geordnet, ohne kritische Fehler zu verursachen
- Out-of-Distribution-Erkennung: Das System erkennt Eingaben, die außerhalb seiner Trainingsdaten liegen

**Prüffragen:**
- Gibt es definierte Fallback-Verhalten für den Fall von Systemausfällen?
- Wird Out-of-Distribution-Input erkannt und entsprechend behandelt?
- Wurden Stress-Tests und Adversarial-Tests durchgeführt?

## Anforderung 3 — Cybersicherheit (Art. 15 Abs. 4 und 5 KI-VO)

Hochrisiko-KI-Systeme müssen so konzipiert sein, dass sie widerstandsfähig gegen den unbefugten Zugriff Dritter sind, der die Nutzung, das Verhalten, die Leistung oder die Sicherheit des Systems gefährden könnte.

**Spezifische Bedrohungsszenarien, die adressiert werden müssen:**

- **Datenvergiftung (Data Poisoning):** Manipulation von Trainingsdaten, um das Systemverhalten zu beeinflussen
- **Modelldiebstahl (Model Extraction):** Unbefugtes Auslesen von Modelleigenschaften durch gezielte Anfragen
- **Adversarielle Eingaben (Adversarial Attacks):** Gezielt veränderte Eingaben, die das System täuschen
- **Backdoor-Angriffe:** Einschleusung versteckter Verhaltensweisen in das trainierte Modell
- **Inferenzangriffe (Membership Inference):** Rekonstruktion von Trainingsdaten aus Modellantworten

**Prüffragen:**
- Gibt es eine dokumentierte Bedrohungsanalyse (Threat Model) für das KI-System?
- Wurden Maßnahmen gegen die oben genannten Angriffsvektoren implementiert?
- Ist das System regelmäßig auf Sicherheitslücken geprüft worden?
- Gibt es ein Incident-Response-Verfahren für Cybersicherheitsvorfälle?

## Verhältnis zum Cyber Resilience Act

Wenn das Hochrisiko-KI-System unter den Cyber Resilience Act (Verordnung (EU) 2024/2847) fällt, gelten dessen Anforderungen zusätzlich. Die Anforderungen von Art. 15 KI-VO und des Cyber Resilience Act sind kumulativ zu erfüllen.

## Technische Nachweise

Für die Konformitätsbewertung sind folgende Nachweise in der Regel erforderlich:
- Dokumentierte Leistungsmetriken aus Validierungs- und Testverfahren
- Ergebnisse von Robustheits- und Stresstests
- Ergebnisse von Sicherheits-Audits oder Penetrationstests
- Dokumentation der implementierten Cybersicherheitsmaßnahmen

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
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 15 Rn. 4: Anwendungsbereich und Pflichten.
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
PRUEFERGEBNIS — HOCHRISIKO GENAUIGKEIT ROBUSTHEIT CYBERSICHERHEIT ART 15
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 15 Rn. 4]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
