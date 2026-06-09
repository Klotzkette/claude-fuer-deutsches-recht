---
name: abgrenzung-konventionelle-software-vs-ki-system
description: "Grenzfall-Skill zur Abgrenzung konventioneller Software, Automation, Statistik, Expertensystemen, Workflows und KI-Systemen nach Art. 3 Nr. 1 KI-VO. Problematisiert Automation, Autonomie, Inferenz, gelernte Parameter, LLM/API-Komponenten und menschliche Freigabe. Output: Einordnungsmatrix mit bel — Arbeitskontext: KI-VO/AI Act Prüfer, Schwerpunkt abgrenzung konventionelle software vs ki system."
---

# Abgrenzung: Konventionelle Software versus KI-System

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Art. 5 Verbote ab 02.02.2025, Art. 51-55 GPAI ab 02.08.2025, Hochrisiko Anhang III ab 02.08.2026, Hochrisiko Anhang I ab 02.08.2027, schwerwiegender Vorfall 15 Tage / 2 Tage (Tod).
- Tragende Normen verifizieren: KI-VO (EU 2024/1689) Art. 3, 5 (Verbote), 6 (Hochrisiko), 8-15 (Anforderungen), 16, 26 (Pflichten Anbieter/Betreiber), 50 (Transparenz), 51-55 (GPAI), 73, 99 (Sanktionen) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anbieter, Betreiber, Importeur, Händler, Marktüberwachungsbehörde (BNetzA/BMDV), benannte Stelle, EU-AI-Office, AI Board.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Konformitätserklärung Art. 47, technische Dokumentation Anhang IV, Risikomanagement-System Art. 9, Datengovernance Art. 10, FRIA (Fundamental Rights Impact Assessment) Art. 27, EU-Datenbank-Registrierung Art. 49 — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Leitgedanke

Automation ist ein starkes Warnsignal, aber kein alleiniger Test. Entscheidend ist, ob das System aus Eingaben ableitet, wie Vorhersagen, Inhalte, Empfehlungen oder Entscheidungen erzeugt werden. Autonomie muss vorhanden sein, darf aber nicht überhöht werden: Auch ein Mensch-in-der-Schleife-System kann KI sein, wenn die Ausgabe inferenzbasiert entsteht.

## Abgrenzungsmatrix

### Regelmäßig konventionelle Software

| Systemtyp | Warum regelmäßig kein KI-System |
|---|---|
| SQL-Abfrage | Suche/Filter nach festen Kriterien, keine inferenzbasierte Ausgabe |
| Makro/Skript | starrer Ablauf, keine Ableitung aus Daten |
| Fristenrechner | mathematische oder juristische Regeln vollständig vorgegeben |
| Formularvalidierung | prüft Pflichtfelder oder Format, bewertet nicht |
| Dashboard mit Summen/Mittelwerten | deskriptive Statistik ohne Vorhersage/Empfehlung |
| Hartcodierter Entscheidungsbaum | Regeln und Schwellen komplett menschlich festgelegt |

### Grenzfälle

| Systemtyp | Entscheidend |
|---|---|
| Expertensystem | Nur Wissensbasis oder zusätzlich gelernte/inferenzbasierte Bewertung? |
| Scoring-Excel | Manuelle Gewichtung oder aus Daten gelernte Parameter? |
| Workflow-Automation | Nur Routing nach Regeln oder KI-Komponente mit Bewertung? |
| Suchmaschine | Reine Volltextsuche oder lernbasiertes Ranking/Personalisierung? |
| Fraud-Detection | Feste Schwellen oder Anomalie-/Klassifikationsmodell? |
| Chatbot | Skriptbaum oder generatives/LLM-basiertes System? |
| Rechts-/HR-Assistent | Nur Textentwurf oder Bewertung natürlicher Personen/Rechtsanwendung? |

### Regelmäßig KI-System oder KI-Komponente

| Systemtyp | Typisches KI-Merkmal |
|---|---|
| LLM, Transformer, generativer Chatbot | Inhalte/Empfehlungen durch Inferenz |
| Klassifikator, Random Forest, XGBoost, SVM | gelernte Muster und Zuordnung |
| Regression mit Prognosezweck | Vorhersage aus Eingaben |
| Clustering / Embeddings | Musterbildung oder Ähnlichkeit aus Daten |
| Bild-, Sprach- oder Emotionserkennung | inferenzbasierte Erkennung/Kategorisierung |
| Recommendation Engine | Empfehlung aus Nutzungs- oder Kontextdaten |
| RAG-System mit LLM-Auswertung | Retrieval plus generative/inferenzbasierte Antwort |

## Prüffragen

1. Werden Trainingsdaten, Modellgewichte, Embeddings, gelernte Parameter oder ein externes Modell genutzt?
2. Erzeugt das System aus variablen Eingaben eigenständig eine Ausgabe?
3. Ist die Ausgabe Vorhersage, Inhalt, Empfehlung, Score, Ranking, Klassifikation oder Entscheidung?
4. Kann ein Mensch die Ausgabe nur noch prüfen, übernehmen oder verwerfen?
5. Ist die Automation bloß Ablaufsteuerung oder trägt sie die inhaltliche Bewertung?
6. Ist eine KI-API oder ein GPAI-System eingebunden, auch wenn die eigene Software drumherum konventionell ist?
7. Wird das System in sensiblen Kontexten wie Beschäftigung, Bildung, Kredit, Justiz oder Verwaltung genutzt?

## Typische Fehlannahmen

**"Es lernt nicht im Betrieb, also keine KI."**
Falsch. Adaptivität nach Deployment ist optional; ein eingefrorenes trainiertes Modell kann KI-System sein.

**"Der Mensch entscheidet am Ende, also keine KI."**
Falsch. Menschliche Freigabe beseitigt die KI-Eigenschaft nicht, wenn die inhaltliche Ausgabe inferenzbasiert generiert wird.

**"Es ist nur eine API."**
Die API kann KI-System oder Bestandteil eines KI-Systems sein. Für den Betreiber zählt der konkrete Einsatz.

**"Es ist nur ein Chatbot."**
Ein skriptbasierter FAQ-Bot kann konventionell sein. Ein LLM-basierter Chatbot ist regelmäßig KI-System; Hochrisiko hängt aber erst vom Zweck ab.

**"Es ist nur Statistik."**
Deskriptive Statistik bleibt häufig draußen. Prognose, Klassifikation, Ranking oder individuelle Bewertung sprechen deutlich für KI.

## Ergebnislogik

- **KI-System wahrscheinlich:** `liegt-ki-system-vor-art-3-nr-1` dokumentierend abschließen, danach Risikoklasse prüfen.
- **Konventionelle Software wahrscheinlich:** Negativvermerk erstellen; Re-Evaluation bei neuer KI-Komponente oder Zweckänderung.
- **KI-Komponente in konventionellem System:** Gesamtarchitektur trennen und KI-Komponente separat durch die KI-VO-Prüfung führen.
- **GPAI/Chatbot betroffen:** `gpai-vorliegen-art-3-nr-63` und `begrenztes-risiko-art-50-transparenzpflichten`.
- **Sensible Zwecknähe:** zusätzlich `hochrisiko-art-6-abs-2-anhang-iii`.

## Output-Template — Abgrenzungsmatrix

```text
ABGRENZUNG KONVENTIONELLE SOFTWARE / KI-SYSTEM
Datum: [DATUM]
System / Komponente: [NAME]

1. Technischer Befund
[Regelwerk / / Statistik / ML-Modell / LLM / API / RAG / Hybrid]

2. Automation und Autonomie
[Was läuft automatisch? Wo greift ein Mensch ein? Ist die Ausgabe menschlich vorbestimmt?]

3. Inferenz
[Keine / möglich / wahrscheinlich / bestätigt]
[Begründung: Trainingsdaten, Modell, Gewichtung, Ranking, Generierung]

4. Output
[Vorhersage / Inhalt / Empfehlung / Entscheidung / nur Datenweitergabe]

5. Ergebnis
[konventionelle Software / KI-System / KI-Komponente im Gesamtsystem / Grenzfall]

6. Folgeprüfung
[liegt-ki-system-vor-art-3-nr-1 / gpai-vorliegen-art-3-nr-63 / hochrisiko-art-6-abs-2-anhang-iii / keine KI-VO]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 3 Nr. 1 KI-VO, Erwägungsgrund 12 und die Kommissionsleitlinien zur Definition des KI-Systems. Keine Rechtsberatung.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 KI-VO (verbotene Praktiken)
- Art. 6, 7 KI-VO (Hochrisiko-KI-Systeme)
- Art. 9, 10, 11 KI-VO (Risikomanagement, Daten, Technische Dokumentation)
- Art. 13, 14 KI-VO (Transparenz, menschliche Aufsicht)
- Art. 16 KI-VO (Pflichten Anbieter)
- Art. 26, 27 KI-VO (Pflichten Betreiber)
- Art. 50 KI-VO (Transparenz GPAI/Deepfakes)
- Art. 53-55 KI-VO (Pflichten GPAI-Anbieter)
- Art. 99-101 KI-VO (Sanktionen)
- VO 2024/1689 (KI-VO, Inkrafttreten)

### Leitentscheidungen

- EuGH C-634/21 (automatisierte Entscheidung Art. 22 DSGVO)
- EuGH C-203/22 (Profiling, Auskunftsrechte)
- BVerfG 1 BvR 2017/21 (automatisierte Datenverarbeitung Polizei)
- OLG Köln 6 U 32/24 (Deepfake-Werbung)
- OLG Stuttgart 2 U 63/22 (Mängel KI-System B2B)

### Anwendung im Skill

- KI-System-Klassifikation Art. 6 KI-VO: Risikoeinstufung vor Compliance-Pflichten pruefen.
- Transparenz Art. 50 KI-VO erfasst auch Deepfakes; OLG Koeln 6 U 32/24 als Praxisbeispiel.
- GPAI-Pflichten Art. 53-55 KI-VO ab August 2025; technische Dokumentation Annex XI vorhalten.
