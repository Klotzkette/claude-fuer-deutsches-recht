---
name: gpai-vorliegen-art-3-nr-63
description: "Unternehmen fragt: Ist unser KI-Modell ein General-Purpose-KI-Modell nach der KI-VO und welche Besonderheiten gelten dann? Art. 3 Nr. 63 KI-VO GPAI-Definition. Pruefraster: Training auf grosser Datenmenge selbstueberwachtes oder halbselbstueberwachtes Lernen allgemeine Aufgabenerfuellung grosse Parameteranzahl. Abgrenzung GPAI-Modell Art. 3 Nr. 63 vs. GPAI-System Art. 3 Nr. 66 KI-VO. Output: Einordnungsmatrix GPAI-Modell vs. Spezialsystem. Abgrenzung zu gpai-modelle-art-51-bis-55 (Pflichten bei GPAI-Modell) und liegt-ki-system-vor-art-3-nr-1 (KI-System Grunddefinition)."
---

# Liegt ein GPAI-Modell vor? — Art. 3 Nr. 63 KI-VO

## Zweck

GPAI-Modelle (General-Purpose-KI-Modelle) unterliegen einem eigenen Pflichtenkatalog nach Art. 51 bis 55 KI-VO, der seit dem 2. August 2025 anwendbar ist. Dieser Skill klärt, wann ein GPAI-Modell vorliegt und wie es vom GPAI-System abzugrenzen ist.

## Legaldefinition — Art. 3 Nr. 63 KI-VO

Ein GPAI-Modell ist ein KI-Modell, das Folgendes aufweist:
- Es wird mit großen Datenmengen unter Verwendung von selbstüberwachtem oder unüberwachtem Lernen in großem Maßstab trainiert
- Es ist so konzipiert, dass es für eine allgemeine Ausgabe ausreichend generalisiert ist
- Es kann eine Vielzahl unterschiedlicher Aufgaben kompetent ausführen
- Es kann in eine Vielzahl nachgelagerter Systeme oder Anwendungen integriert werden

## Tatbestandsmerkmale — Checkliste

### Merkmal 1 — Großskaliges Training auf großen Datenmengen

**Prüffragen:**
- Wurde das Modell auf einer sehr großen Datenmenge trainiert (in der Größenordnung von Milliarden von Parametern, Terabytes an Trainingsdaten)?
- War das Training ressourcenintensiv (erhebliche Rechenleistung, nicht auf einem einzelnen Server in kurzer Zeit)?

### Merkmal 2 — Selbstüberwachtes oder unüberwachtes Lernen

**Prüffragen:**
- Wurde das Modell ohne vollständig manuelle Annotation aller Trainingsdaten trainiert?
- Wurden Methoden wie Self-Supervised Learning, Pretraining auf Rohdaten (Text, Bilder, Code) oder ähnliche Verfahren eingesetzt?

**Hinweis:** Auch Modelle, die zuerst self-supervised vortrainiert und dann mit überwachtem Lernen feinabgestimmt wurden (Fine-Tuning, RLHF), fallen unter die GPAI-Definition, wenn das Vortraining die wesentliche Grundlage bildet.

### Merkmal 3 — Allgemeine Aufgabenerfüllung (Generalisierung)

**Prüffragen:**
- Kann das Modell kompetent eine breite Palette verschiedener Aufgaben erfüllen, ohne für jede Aufgabe separat trainiert worden zu sein?
- Ist das Modell nicht ausschließlich auf eine sehr spezifische Aufgabe ausgerichtet?

**Abgrenzung:** Ein Modell, das ausschließlich auf eine eng definierte Aufgabe (z.B. Bildklassifikation in einer Produktkategorie) spezialisiert wurde und keine Generalisierung über verschiedene Domänen hinweg zeigt, ist in der Regel kein GPAI-Modell.

### Merkmal 4 — Integrierbarkeit in nachgelagerte Systeme

**Prüffragen:**
- Kann das Modell als Grundlage (Foundation) für verschiedene nachgelagerte Anwendungen verwendet werden?
- Bieten Sie das Modell über eine API oder als Infrastruktur anderen Entwicklern an?

## Typische GPAI-Modell-Kategorien (nicht abschließend)

- Große Sprachmodelle (Large Language Models) mit breiten Fähigkeiten
- Multimodale Modelle (Text + Bild, Text + Audio, Text + Code)
- Foundation-Modelle für Bildgenerierung und -analyse
- Code-Generierungsmodelle mit breitem Sprachspektrum

## Abgrenzung: GPAI-Modell versus GPAI-System

**GPAI-Modell (Art. 3 Nr. 63 KI-VO):** Das Modell selbst — die trainierten Gewichte, die Architektur, das Ergebnis des Trainingsprozesses. Anbieter eines GPAI-Modells sind in der Regel Unternehmen, die das Training durchgeführt haben und das Modell anderen zur Nutzung bereitstellen.

**GPAI-System (Art. 3 Nr. 66 KI-VO):** Ein KI-System, das auf einem GPAI-Modell basiert und für eine Vielzahl von Zwecken eingesetzt werden kann, einschließlich wenn es direkt mit dem Nutzer interagiert oder einen Inhalt erstellt. Anbieter eines GPAI-Systems sind Unternehmen, die das Modell in einer Anwendung (Chatbot, Zusammenfassungstool, Codierungshilfe) bereitstellen.

**Praktische Konsequenz:** Wer nur ein auf dem GPAI-Modell basierendes GPAI-System betreibt, ohne selbst das Modell entwickelt zu haben, ist Betreiber. Die GPAI-Modell-Pflichten nach Art. 51 bis 55 KI-VO treffen primär den Modellanbieter.

## Ergebnis und Routing

- **GPAI-Modell bestätigt:** → Pflichten nach Art. 51 bis 55 KI-VO → `gpai-modelle-art-51-bis-55`
- **GPAI-Modell mit systemischem Risiko (über 10e25 FLOP oder Kommissionsbeschluss):** → Zusätzliche Pflichten → `gpai-systemisches-risiko-schwelle-10e25-flop`
- **Kein GPAI-Modell, aber KI-System:** → Risikoklassen-Triage → `risikoklassen-uebersicht-und-triage`

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
- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 3 Nr. 63 Rn. 2: Anwendungsbereich und Pflichten.
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
PRUEFERGEBNIS — GPAI VORLIEGEN ART 3 NR 63
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 3 Nr. 63 Rn. 2]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
    1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
