---
name: gpai-vorliegen-art-3-nr-63
description: "Prüft, ob ein Modell oder Dienst ein General-Purpose-AI-Modell oder GPAI-System nach der KI-VO ist und grenzt GPAI von Hochrisiko-KI ab. Behandelt ChatGPT-aehnliche Systeme, Foundation Models, API-Nutzung, GPAI-System Art. 3 Nr. 66, systemisches Risiko und Zweckbestimmung. Kernpunkt: GPAI/allgem..."
---

# GPAI, allgemeiner Chatbot und Hochrisiko-Abgrenzung

## Zweck

Kläre, ob ein Modell oder Dienst ein General-Purpose-AI-Modell (GPAI-Modell) oder ein GPAI-System ist und wie dies zur Hochrisiko-Einstufung nach Art. 6 KI-VO steht.

Der wichtigste praktische Punkt: Ein allgemeines Sprachmodell oder ein ChatGPT-ähnlicher Chatbot ist nicht automatisch Hochrisiko-KI. Hochrisiko hängt an der konkreten Zweckbestimmung und dem Einsatz als KI-System in einem regulierten Kontext, insbesondere Art. 6 Abs. 2 i.V.m. Anhang III.

## Begriffe trennen

| Begriff | Prüfgegenstand | Typische Pflichten |
|---|---|---|
| GPAI-Modell | trainiertes Basismodell / Foundation Model | Art. 51 bis 55 KI-VO, ggf. systemisches Risiko |
| GPAI-System | Anwendung auf Basis eines GPAI-Modells, die vielfältige Zwecke erfüllen kann | ggf. Art. 50, Rollen- und Risikoprüfung |
| Hochrisiko-KI-System | konkrete Anwendung mit Anhang-I- oder Anhang-III-Zweck | Art. 9 bis 15, 26, 27, 43 bis 49 |
| Allgemeiner Chatbot | Benutzeroberfläche für breite Text-/Multimodalaufgaben | nicht automatisch Hochrisiko; Einsatz prüfen |

## GPAI-Modell nach Art. 3 Nr. 63 KI-VO

Prüfe:
- Wurde das Modell mit großen Datenmengen und erheblichem Rechenaufwand trainiert?
- Nutzt es typischerweise selbstüberwachtes, unüberwachtes oder vergleichbares großskaliges Training?
- Generalisiert es über eine breite Vielzahl verschiedener Aufgaben?
- Kann es in viele nachgelagerte Systeme oder Anwendungen integriert werden?
- Ist es nicht nur ein eng spezialisiertes Modell für eine einzelne Aufgabe?

Beispiele:
- große Sprachmodelle
- multimodale Foundation Models
- breite Bild-, Audio-, Video- oder Code-Modelle
- Modelle, die als API oder Model Weight für viele Anwendungen bereitgestellt werden

Nicht automatisch GPAI:
- kleines Fachmodell für genau eine Klassifikationsaufgabe
- klassische Fachsoftware ohne generische Modellfähigkeiten
- rein regelbasiertes Expertensystem

## GPAI-System nach Art. 3 Nr. 66 KI-VO

Ein GPAI-System ist ein KI-System auf Basis eines GPAI-Modells, das für eine Vielzahl von Zwecken eingesetzt werden kann, auch wenn es direkt mit Nutzern interagiert oder Inhalte erzeugt.

Prüffragen:
- Gibt es eine Chat-, Agenten-, API- oder Tool-Oberfläche für Nutzer?
- Kann das System Texte, Bilder, Code, Empfehlungen oder andere Inhalte für viele Zwecke erzeugen?
- Ist das System in einen konkreten Facheingebettet oder bleibt es allgemeiner Assistent?

## Hochrisiko-Abgrenzung

### Allgemeiner Chatbot

Ein allgemeiner Assistent für Entwurf, Zusammenfassung, Übersetzung oder Recherche ist regelmäßig nicht schon wegen seiner abstrakten Einsatzmöglichkeiten Hochrisiko. Prüfe aber:
- Art. 50 Transparenzpflichten bei Interaktion mit natürlichen Personen oder KI-generierten Inhalten
- GPAI-Pflichten des Modellanbieters
- Datenschutz, Berufsrecht, Geheimnisschutz, Urheberrecht

### Konkrete Hochrisiko-Integration

Wird das GPAI-System in einen Anhang-III-Prozess integriert, kann die konkrete Anwendung Hochrisiko sein.

Beispiele:
- Bewerberranking oder Eignungsbewertung
- Beschäftigtenüberwachung oder Leistungsbewertung
- Kreditwürdigkeitsprüfung natürlicher Personen
- Bewertung von Sozialleistungsansprüchen
- Notrufpriorisierung
- justizielle Rechtsanwendung auf konkrete Fälle durch oder für ein Gericht
- Asyl-/Visa-/Grenzrisikobewertung

Dann weiter zu `hochrisiko-art-6-abs-2-anhang-iii`.

### Mitarbeitende nutzen Chatbot entgegen Zweckbestimmung

Wenn Mitarbeitende ein allgemeines Tool zweckwidrig für Hochrisiko-Fragen nutzen:

- **Isolierter Regelverstoß trotz klarer Richtlinie und Kontrollen:** als Compliance-Vorfall behandeln; nicht automatisch Hochrisiko-Einstufung des gesamten Tools.
- **Systematische oder geduldete Praxis:** tatsächlicher Betreiberzweck kann Hochrisiko-Einsatz begründen.
- **Vorhersehbarer Fehlgebrauch ohne Schutzmaßnahmen:** Governance verschärfen; Art. 4 KI-Kompetenz, Richtlinien, Rollenrechte, Logging, technische Sperren, Prompt-Blockaden und Re-Evaluation dokumentieren.
- **Zweckänderung oder wesentliche Änderung:** `anbieter-werden-art-25` prüfen.

## Prüffragen für die Dokumentation

1. Handelt es sich um ein Modell, ein System oder eine konkrete Fachanwendung?
2. Wer ist Modellanbieter, Systemanbieter und Betreiber?
3. Ist der Zweck breit-allgemein oder fachlich auf einen Anhang-III-Kontext zugeschnitten?
4. Gibt es Use-Case-Beschränkungen in Terms, Policy, Systemprompt, UI, Rollenrechten oder Schulungen?
5. Werden Hochrisiko-Einsätze technisch verhindert, nur organisatorisch untersagt oder faktisch geduldet?
6. Erzeugt das System nur allgemeine Inhalte oder bewertet es natürliche Personen, Rechte, Risiken oder Zugang?

## Routing

- **GPAI-Modell bestätigt:** `gpai-modelle-art-51-bis-55`; ggf. `gpai-systemisches-risiko-schwelle-10e25-flop`.
- **Allgemeiner Chatbot/GPAI-System:** `begrenztes-risiko-art-50-transparenzpflichten`, zusätzlich Datenschutz/Geheimnisschutz prüfen.
- **Einsatz in Anhang-III-Kontext:** `hochrisiko-art-6-abs-2-anhang-iii`, danach `rueckausnahme-art-6-abs-3`.
- **Zweckwidrige Mitarbeitenden-Nutzung:** `betreiber-deployer-pflichten-art-26`, `anbieter-werden-art-25`, `output-pruefdokument-ki-vo-mit-warnhinweisen`.

## Output-Template — GPAI-/Chatbot-Einordnung

```text
GPAI- UND CHATBOT-EINORDNUNG NACH KI-VO
Datum: [DATUM]
System / Modell / Dienst: [NAME]

1. Technischer Zuschnitt
[Modell / GPAI-System / allgemeiner Chatbot / Fachanwendung / API-Integration]

2. GPAI-Modell
[Ja/Nein/Unklar] — [Begründung]

3. GPAI-System / allgemeiner Assistent
[Ja/Nein/Unklar] — [Begründung]

4. Zweckbestimmung
- Anbieter-Zweck: [...]
- Betreiber-Zweck: [...]
- Verbotene/ausgeschlossene Nutzungen: [...]
- Bekannte tatsächliche Nutzung: [...]

5. Hochrisiko-Relevanz
[Nicht automatisch Hochrisiko / Anhang-III-Prüfung erforderlich / Hochrisiko naheliegend]
[Begründung mit konkretem Zweck]

6. Off-label-/Mitarbeitenden-Nutzung
[Risiko, Kontrollen, Governance-Maßnahmen, Re-Evaluation]

7. Folge-Skills
[gpai-modelle-art-51-bis-55 / begrenztes-risiko-art-50-transparenzpflichten / hochrisiko-art-6-abs-2-anhang-iii / betreiber-deployer-pflichten-art-26]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 3 Nr. 1, Nr. 12, Nr. 13, Nr. 63 und Nr. 66, Art. 50 sowie Art. 51 bis 55 KI-VO. Keine Rechtsberatung.
