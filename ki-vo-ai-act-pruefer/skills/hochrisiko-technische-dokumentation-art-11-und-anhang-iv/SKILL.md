---
name: hochrisiko-technische-dokumentation-art-11-und-anhang-iv
description: "Anbieter von Hochrisiko-KI fragt: Was muss die technische Dokumentation enthalten und wie aktuell muss sie sein? Art. 11 i.V.m. Anhang IV KI-VO. Pruefraster: vollstaendiger Inhaltskatalog nach Anhang IV Systembeschreibung Entwicklungsprozess Datensaetze Leistungsmetriken Risikomanagement Konformitaetsbewertungsergebnis Aktualisierungspflichten bei Systemaenderungen. Output: Dokumentations-Checkliste nach Anhang IV und Strukturvorlage. Abgrenzung zu hochrisiko-aufzeichnungspflichten-logging-art-12 (laufende Logs) und output-konformitaetserklaerung-eu-anhang-v (Konformitaetserklaerung)."
---

# Technische Dokumentation — Art. 11 und Anhang IV KI-VO

## Zweck

Art. 11 KI-VO verpflichtet Anbieter von Hochrisiko-KI-Systemen, eine umfangreiche technische Dokumentation zu erstellen und aktuell zu halten. Diese Dokumentation ist Voraussetzung für die Konformitätsbewertung und muss Marktüberwachungsbehörden auf Anfrage vorgelegt werden.

## Zeitpunkt der Erstellung

Die technische Dokumentation muss vor dem Inverkehrbringen oder der Inbetriebnahme des Hochrisiko-KI-Systems erstellt sein. Sie ist bei wesentlichen Änderungen zu aktualisieren.

## Inhalt der technischen Dokumentation nach Anhang IV KI-VO

### Abschnitt 1 — Allgemeine Beschreibung des KI-Systems

- Name, Version und Zweck des Systems
- Vorgesehene Verwendung und bestimmungsgemäßer Einsatz
- Beschreibung der Wechselwirkungen mit Hardware oder Software, mit der das System zusammenarbeitet
- Kategorien natürlicher Personen, die vom System betroffen sind
- Beschreibung der Ausgaben und deren Verwendung
- Hardware-Anforderungen

### Abschnitt 2 — Detaillierte Beschreibung von Elementen und Entwicklungsprozess

- Entwicklungsmethoden und Verfahren (einschließlich Software-Entwicklungsverfahren)
- Systembeschreibung: Architektur, Methoden und Modelle
- Trainingsverfahren und -methodiken
- Beschreibung der Trainingsdaten und ihrer Eigenschaften (Herkunft, Umfang, Verarbeitungsschritte)
- Informationen über vortrainierte Modelle und externe Tools
- Ergebnisse der Validierungs- und Testverfahren
- Validierungs- und Testprotokolle

### Abschnitt 3 — Informationen über die Überwachung, den Betrieb und die Kontrolle

- Leistungsmetriken und Messmethoden
- Leistungsniveaus und Schwellenwerte
- Annahmen und Einschränkungen des Systems
- Bekannte oder vorhersehbare Risiken
- Datenpflege und Datenpipeline
- Mögliche Einsatzszenarien außerhalb der vorgesehenen Verwendung

### Abschnitt 4 — Überwachung nach dem Inverkehrbringen

- Plan für die Überwachung nach dem Inverkehrbringen (Art. 72 KI-VO)

### Abschnitt 5 — Konformitätsbewertungsverfahren

- Ergebnisse der Konformitätsbewertung
- Beteiligung benannter Stellen (falls zutreffend)
- EU-Konformitätserklärung

### Abschnitt 6 — EU-Konformitätserklärung

Verweis auf die EU-Konformitätserklärung nach Anhang V KI-VO.

### Abschnitt 7 — Einfache Beschreibung für Betreiber

Kurzfassung der wesentlichen Merkmale des Systems, die für Betreiber verständlich sein muss.

## Besonderheiten für GPAI-Modelle als Grundlage

Wenn das Hochrisiko-KI-System auf einem GPAI-Modell aufbaut, sind in der technischen Dokumentation auch die Eigenschaften des GPAI-Modells zu dokumentieren — soweit der Anbieter des GPAI-Modells entsprechende Informationen bereitgestellt hat (Art. 11 Abs. 3 KI-VO).

## Aktualisierungspflichten

Die technische Dokumentation ist aktuell zu halten. Eine Aktualisierung ist insbesondere erforderlich:
- Bei wesentlichen Änderungen des Systems
- Bei Änderungen des vorgesehenen Verwendungszwecks
- Wenn neue Risiken bekannt werden
- Bei Änderungen der Marktüberwachungsvorschriften

## Aufbewahrungspflichten

Die technische Dokumentation ist zehn Jahre nach Inverkehrbringen oder Inbetriebnahme aufzubewahren (Art. 18 KI-VO). Bei Hochrisiko-KI in sicherheitskritischen Bereichen können längere Fristen gelten.

## Prüffragen

- Liegt eine schriftliche, aktuelle technische Dokumentation vor, die alle Abschnitte nach Anhang IV abdeckt?
- Wurde die Dokumentation bei der letzten wesentlichen Systemänderung aktualisiert?
- Ist die Dokumentation für die zuständige nationale Marktüberwachungsbehörde auf Anfrage bereit?
- Liegt eine verständliche Kurzbeschreibung für Betreiber vor?

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
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 11 Rn. 5: Anwendungsbereich und Pflichten.
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
PRUEFERGEBNIS — HOCHRISIKO TECHNISCHE DOKUMENTATION ART 11 UND ANHANG IV
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 11 Rn. 5]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
