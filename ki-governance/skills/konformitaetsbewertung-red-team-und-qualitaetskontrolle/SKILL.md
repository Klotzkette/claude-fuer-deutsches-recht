---
name: konformitaetsbewertung-red-team-und-qualitaetskontrolle
description: "Konformitaetsbewertung: Red-Team und Qualitätskontrolle im Plugin ki governance im Ki Governance."
---

# Konformitaetsbewertung: Red-Team und Qualitätskontrolle

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Geltungsbeginn gestaffelt (02.02.2025 Verbote, 02.08.2025 GPAI, 02.08.2026 Hochrisiko Anhang III), schwerwiegender Vorfall 15 Tage, DSGVO DPIA vorab.
- Tragende Normen verifizieren: EU KI-VO 2024/1689 Art. 9, 10, 14, 22, 27, 50, ISO/IEC 42001, NIST AI RMF 1.0, OECD AI Principles, DSGVO Art. 22, 35, Produkthaftungs-RL 2024/2853 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsleitung, KI-Officer, Datenschutzbeauftragter, Compliance, Aufsichtsrat, Marktüberwachung, externer Auditor, betroffene Personen.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: KI-Inventar, Risikoanalyse, FRIA (Fundamental Rights Impact Assessment), AI Governance Policy, Modellkarten, Audit-Bericht, DSGVO-DPIA, Schulungsnachweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Konformitaetsbewertung: Red-Team und Qualitätskontrolle
- **Normen-/Quellenanker:** EU, KI, VO, DSGVO, AIA, DPIA.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Konformitätsbewertung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Konformitätsbewertungsverfahren KI-VO (Art. 43)
- **Anhang VI — Interne Kontrolle**: Standardverfahren für die meisten Hochrisiko-KI-Systeme nach Anhang III, sofern harmonisierte Normen vollständig angewendet werden.
- **Anhang VII — Bewertung mit benannter Stelle**: für biometrische Identifikationssysteme nach Anhang III Nr. 1 lit. a, wenn keine harmonisierten Normen vollständig angewendet werden — oder freiwillig.
- **Konformitätsbewertung im Zuge anderer Unionsrechtsakte**: Wenn das KI-System Sicherheitsbauteil eines Produkts nach Anhang I ist (Medizinprodukt MDR, Maschine MaschinenVO etc.), wird die KI-VO-Bewertung in die bestehende Konformitätsbewertung integriert (Art. 43 Abs. 3).

## Pflichtdokumentation
- **Technische Dokumentation** Art. 11 i. V. m. Anhang IV: Systembeschreibung, Designspezifikationen, Trainingsdatenbeschreibung, Risikomanagement, Monitoring, Cybersicherheit.
- **Logging-Architektur** Art. 12: Aufzeichnungen über Lebenszyklus, Zweck-Erreichung, Identifikation problematischer Verhaltensweisen.
- **EU-Konformitätserklärung** Art. 47 i. V. m. Anhang V: 10 Jahre Aufbewahrung, Inhalt vorgeschrieben.
- **CE-Kennzeichnung** Art. 48 und **EU-Datenbankregistrierung** Art. 49 / 71 (Anhang VIII).

## Red-Team-Prüfungen
- **Robustheit**: adversariale Beispiele, Eingabestörungen, Edge Cases.
- **Bias / Fairness**: Tests über Untergruppen (Geschlecht, Alter, ethnische Herkunft, Region), Disparate-Impact-Analyse.
- **Cybersicherheit**: Prompt-Injection (bei LLM-basierten Systemen), Model Inversion, Membership Inference.
- **Datenleckage**: Aus Antworten rekonstruierbare Trainingsdaten (insb. bei Foundation Models).

## Qualitätskontrolle
- **Pre-Deployment**: vollständiger Konformitätsbewertungsbericht, abgenommen durch Compliance.
- **Pilotphase**: vorgesehene Stichprobe mit verstärktem Logging und Human Override.
- **Produktion**: Monitoring nach Art. 72 KI-VO (Marktbeobachtung durch Anbieter), Vorfallsmeldung nach Art. 73.
- **Substantielle Änderung**: bei Modellaktualisierung mit Performance-Verschiebung neue Bewertung nach Art. 43 Abs. 4.

## Trade-off
Interne Kontrolle (Anhang VI) ist günstiger und schneller, scheitert aber bei nicht-harmonisierten Aspekten. Beauftragung benannter Stelle (Anhang VII) gibt Rechtssicherheit, kostet Zeit (Wartezeit, Auditdurchläufe) und Geld; ist für Markteintritt sensibler Systeme aber empfehlenswert. Hybride Strategie: Anhang VI mit zusätzlichem freiwilligem externem Audit zur Vertrauensbildung.

