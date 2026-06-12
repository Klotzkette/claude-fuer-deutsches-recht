---
name: hochrisiko-genauigkeit-konformitaetsbewertung
description: "Anbieter von Hochrisiko-KI fragt: Welche Leistungsstandards für Genauigkeit Robustheit und Cybersicherheit muessen wir nachweisen und dokumentieren? Art. 15 KI-VO Mindeststandards. Prüfraster: Genauigkeitsmetriken und Leistungserklärung Fehlertoleranz-Anforderungen Resilienz gegen adversarielle E"
---

# Genauigkeit, Robustheit und Cybersicherheit — Art. 15 KI-VO

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Art. 5 Verbote ab 02.02.2025, Art. 51-55 GPAI ab 02.08.2025, Hochrisiko Anhang III ab 02.08.2026, Hochrisiko Anhang I ab 02.08.2027, schwerwiegender Vorfall 15 Tage / 2 Tage (Tod).
- Tragende Normen verifizieren: KI-VO (EU 2024/1689) Art. 3, 5 (Verbote), 6 (Hochrisiko), 8-15 (Anforderungen), 16, 26 (Pflichten Anbieter/Betreiber), 50 (Transparenz), 51-55 (GPAI), 73, 99 (Sanktionen) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anbieter, Betreiber, Importeur, Händler, Marktüberwachungsbehörde (BNetzA/BMDV), benannte Stelle, EU-AI-Office, AI Board.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Konformitätserklärung Art. 47, technische Dokumentation Anhang IV, Risikomanagement-System Art. 9, Datengovernance Art. 10, FRIA (Fundamental Rights Impact Assessment) Art. 27, EU-Datenbank-Registrierung Art. 49 — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

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
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Maßnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Prüfergebnis
**Adressat:** Prüfer / Rechtsberater — Tonfall: strukturiert-rechtlich
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
