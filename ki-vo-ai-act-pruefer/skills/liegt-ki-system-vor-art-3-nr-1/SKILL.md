---
name: liegt-ki-system-vor-art-3-nr-1
description: "Erster Schritt jeder KI-VO-Pruefung: Ist die Software, API, App, Automatisierung oder Modellkette ein KI-System nach Art. 3 Nr. 1 KI-VO? Prueft maschinenbasiertes System, Autonomie, optionale Adaptivitaet, Ziele, Inferenz, Output-Typen und Umweltbeeinflussung nach den Kommissionsleitlinien. Problematisiert Automation und Autonomie statt schematisch abzuhaken. Output: dokumentierbarer KI-System-Einordnungsvermerk mit Tatsachenbasis, Unsicherheiten und Folge-Skills."
---

# Liegt ein KI-System vor? — Art. 3 Nr. 1 KI-VO

## Zweck

Dieser Skill ist das Eingangstor der KI-VO-Prüfung. Er klärt, ob der geprüfte Gegenstand überhaupt ein KI-System im Sinne der Verordnung (EU) 2024/1689 ist. Ohne KI-System greifen die KI-VO-Pflichten grundsätzlich nicht; mit KI-System folgen Anwendungsbereich, Rollen und Risikoklasse.

Der Skill arbeitet nicht mit einem starren Alles-oder-Nichts-Schema. Er erstellt eine nachvollziehbare Einordnung anhand der sieben Elemente der Legaldefinition und dokumentiert, welche Tatsachen die Einordnung tragen.

## Prüfgegenstand sauber bestimmen

Vor der Definition immer zuerst klären:

1. Was genau wird geprüft: Modell, API, Chatbot-Oberfläche, Workflow-Automation, SaaS-Modul, eingebettete Komponente oder Gesamtprodukt?
2. Wer setzt es wofür ein: Anbieter, Betreiber, interne Fachabteilung, Kunde, Behörde?
3. Welche Eingaben werden verarbeitet und welche Ausgaben werden erzeugt?
4. Wird die Ausgabe nur angezeigt, als Vorschlag genutzt oder in Entscheidungen/Prozesse eingespeist?
5. Ist die fragliche Funktion selbst KI-basiert oder nur eine Umgebung um ein fremdes KI-System?

Wenn mehrere Komponenten zusammenwirken, trenne:
- KI-Komponente
- Umgebende konventionelle Software
- Menschliche Entscheidungsschritte
- Nachgelagerte Nutzung der Ausgaben

## Legaldefinition — Arbeitsfassung

Ein KI-System ist nach Art. 3 Nr. 1 KI-VO ein maschinenbasiertes System, das für einen Betrieb mit unterschiedlichem Grad an Autonomie ausgelegt ist, nach Einführung anpassungsfähig sein kann und aus Eingaben für explizite oder implizite Ziele ableitet, wie Ausgaben wie Vorhersagen, Inhalte, Empfehlungen oder Entscheidungen erzeugt werden, die physische oder virtuelle Umgebungen beeinflussen können.

Die Kommissionsleitlinien zur Definition des KI-Systems sind bei Grenzfällen ausdrücklich mitzudenken. Sie sind nicht selbst der Normtext, aber derzeit die wichtigste Auslegungshilfe.

## Sieben Elemente der Prüfung

### 1. Maschinenbasiertes System

Prüfe, ob Software, Hardware, Server, Cloud-Dienst, Edge-Gerät oder eine sonstige technische Infrastruktur die Funktion trägt.

Indizien:
- Ausführung auf Computer, Server, Smartphone, Sensor, Cloud oder eingebettetem Gerät
- API-Aufruf an ein Modell oder einen KI-Dienst
- Softwaremodul in einem Fachverfahren

Nicht ausreichend:
- rein menschliche Entscheidung ohne technische Ausgabegenerierung
- statisches Dokument, Checkliste oder manuelles Formular

### 2. Betrieb mit unterschiedlichem Grad an Autonomie

Autonomie bedeutet nicht, dass das System völlig allein handelt. Es genügt regelmäßig, dass es Ausgaben ohne menschliche Einzelbestimmung jedes Zwischenschritts erzeugt.

Prüffragen:
- Erzeugt das System nach Start oder Eingabe selbst eine Ausgabe, ohne dass ein Mensch jeden Rechenschritt vorgibt?
- Wählt, gewichtet, klassifiziert, generiert, priorisiert oder empfiehlt das System eigenständig?
- Kann ein Mensch die Ausgabe nur noch prüfen, übernehmen oder verwerfen?

Wichtig für die Bewertung:
- Hohe Automation spricht deutlich für ein KI-System, wenn Ausgaben aus Eingaben abgeleitet werden.
- Reine Automation ist nicht allein entscheidend: Ein Skript, das starr kopiert, sortiert oder feste Regeln ausführt, kann konventionelle Software bleiben.
- Autonomie darf nicht überhöht werden. Auch ein System mit menschlicher Freigabe kann KI-System sein, wenn die eigentliche Ausgabegenerierung inferenzbasiert erfolgt.

### 3. Adaptivität nach Einführung

Adaptivität ist optional. Ein System kann KI-System sein, obwohl es nach Deployment nicht weiterlernt.

Indizien:
- Training, Fine-Tuning, Reinforcement Learning, Online Learning
- Anpassung an Nutzerverhalten oder Kontext
- Modellupdates oder Retrieval-/Tool-Konfigurationen, die Verhalten verändern

Bewertung:
- Adaptivität verstärkt die KI-Einordnung.
- Fehlende Adaptivität schließt die KI-Einordnung nicht aus.

### 4. Explizite oder implizite Ziele

Prüfe, welchem Zweck die Ausgaben dienen.

Beispiele:
- Bewerber ranken
- Ausfallwahrscheinlichkeit prognostizieren
- Rechtsfrage zusammenfassen
- Notrufe priorisieren
- Bildinhalt erkennen
- Kundenanfrage beantworten

Auch implizite Ziele zählen, etwa Optimierung von Conversion, Produktivität, Risikosenkung oder Entscheidungsvorbereitung.

### 5. Inferenz aus Eingaben

Inferenz ist der Kern. Das System muss aus Eingaben ableiten, wie es eine Ausgabe erzeugt.

Typische Inferenz:
- maschinelles Lernen, neuronale Netze, Transformer, generative Modelle
- Klassifikation, Scoring, Ranking, Clustering, Regression
- Empfehlungen auf Grundlage gelernter Muster
- Bild-, Sprach-, Text- oder Mustererkennung

Grenzfälle:
- Einfache Suche, Sortierung, SQL-Abfrage oder Formularvalidierung reicht regelmäßig nicht.
- Ein hartcodierter Entscheidungsbaum ist regelmäßig keine KI, wenn alle Regeln und Schwellen ausschließlich menschlich festgelegt sind.
- Statistik ist nicht automatisch KI. Deskriptive Statistik bleibt regelmäßig draußen; Vorhersage-, Klassifikations- oder Empfehlungssysteme überschreiten die Schwelle eher.

### 6. Ausgabetyp

Mindestens ein typischer Ausgabetyp muss vorliegen:
- Vorhersage, Score, Wahrscheinlichkeit, Risikoindikator
- Inhalt, etwa Text, Bild, Audio, Video, Code
- Empfehlung, Ranking, Priorisierung, Next-best-action
- Entscheidung, Klassifikation, Freigabe, Ablehnung, Zuweisung

Der Begriff ist weit. Auch ein "nur vorbereitender" Score kann ein relevanter Output sein.

### 7. Einfluss auf physische oder virtuelle Umgebungen

Die Ausgabe muss physische oder virtuelle Umgebungen beeinflussen können. Ein mittelbarer Einfluss genügt.

Beispiele:
- Mensch übernimmt Empfehlung in Personal-, Kredit-, Versicherungs- oder Verwaltungsentscheidung
- System steuert Prozess, Maschinenlogik, Zugriff, Priorisierung oder Anzeige
- Ausgabe prägt Kommunikation, Sachbearbeitung, Aktenauswertung oder Dokumentation

Wenn eine Ausgabe nur testweise erzeugt und nie verwendet wird, dokumentiere das. Für Produktivsysteme reicht oft schon die reale Möglichkeit, dass Ausgaben in Prozesse einfließen.

## Entscheidungsmatrix

| Befund | Ergebnisrichtung |
|---|---|
| Maschinenbasiert + Inferenz + Output mit möglichem Einfluss | starkes Indiz für KI-System |
| Generatives Modell oder LLM/API im Workflow | regelmäßig KI-System-Komponente |
| Nur feste Wenn-Dann-Regeln ohne gelernte Parameter und ohne Inferenz | regelmäßig kein KI-System |
| Nur Suche, Filterung, Formatierung, Kopieren, Validieren | regelmäßig kein KI-System |
| Automation ohne Inferenz | nicht genug, aber genauer prüfen |
| Autonomie gering, aber Output wird inferenzbasiert erzeugt | KI-System häufig trotzdem naheliegend |
| Nur Modell ohne konkrete Anwendung | ggf. GPAI-Modell prüfen, aber KI-System-Einsatz gesondert bestimmen |

## Typische Beispiele

**Regelmäßig KI-System:**
- ChatGPT-ähnlicher Assistent, der Texte generiert oder Entscheidungen vorbereitet
- Bewerberranking mit LLM, Embeddings oder Scoringmodell
- Bonitätsscore per ML-Modell
- Bildklassifikation mit neuronalen Netzen
- Anomalieerkennung durch Clustering oder trainiertes Modell
- RAG-System, das Dokumente auswertet und rechtliche/geschäftliche Empfehlungen erzeugt

**Regelmäßig kein KI-System:**
- starres Makro zur Dokumentenumbenennung
- SQL-Suche ohne Rankingmodell
- Taschenrechner, Fristenrechner oder Steuerrechner mit ausschließlich fixen Regeln
- reines Formular, das Pflichtfelder prüft
- Dashboard mit Summen, Mittelwerten und statischen Filtern

**Prüfungsbedürftige Grenzfälle:**
- Expertensystem mit komplexer Wissensbasis
- scoringartige Excel-Modelle mit manuell gesetzten Gewichtungen
- Prozessautomation mit einzelnen KI-APIs
- LLM nur als Texteditor ohne Entscheidungskontext
- KI-Assistenz in juristischen, Personal-, Bildungs- oder Kreditprozessen

## Routing

- **KI-System wahrscheinlich:** weiter zu `territorialer-anwendungsbereich-art-2`, danach `persoenlicher-anwendungsbereich-rollen-art-3` und `risikoklassen-uebersicht-und-triage`.
- **Konventionelle Software wahrscheinlich:** Ergebnis dokumentieren; bei Grenzfällen zusätzlich `abgrenzung-konventionelle-software-vs-ki-system`.
- **GPAI oder allgemeiner Chatbot betroffen:** zusätzlich `gpai-vorliegen-art-3-nr-63`, `begrenztes-risiko-art-50-transparenzpflichten` und bei Hochrisiko-Kontexten `hochrisiko-art-6-abs-2-anhang-iii`.
- **Unklare Tatsachen:** offene Punkte im Output markieren und nicht mit Scheinsicherheit entscheiden.

## Output-Template — KI-System-Einordnungsvermerk

```text
KI-SYSTEM-EINORDNUNGSVERMERK NACH ART. 3 NR. 1 KI-VO
Datum: [DATUM]
System / Komponente: [NAME]
Geprüfter Funktionszuschnitt: [MODELL / API / APP / WORKFLOW / GESAMTPRODUKT]
Quelle der Tatsachen: [NUTZERANGABEN / DOKUMENTE / TECHNISCHE UNTERLAGEN]

1. Sachverhalt in Kurzform
[Was tut das System, welche Eingaben, welche Ausgaben, welche Nutzung?]

2. Tatbestandsmerkmale
- Maschinenbasiertes System: [JA/NEIN/UNKLAR] — [Begründung]
- Autonomiegrad: [JA/NEIN/UNKLAR] — [nicht überhöhen; menschliche Freigabe einordnen]
- Adaptivität nach Einführung: [JA/NEIN/UNKLAR/NICHT ERFORDERLICH] — [Begründung]
- Explizite oder implizite Ziele: [JA/NEIN/UNKLAR] — [Zweck]
- Inferenz aus Eingaben: [JA/NEIN/UNKLAR] — [Methode/Indizien]
- Ausgabetyp: [Vorhersage/Inhalt/Empfehlung/Entscheidung/anderer Output]
- Einfluss auf physische oder virtuelle Umgebung: [JA/NEIN/UNKLAR] — [Wirkpfad]

3. Würdigung
[Warum spricht die Automation für/gegen KI-System? Warum ist Autonomie hier ausreichend oder nicht? Welche Rolle spielt Adaptivität?]

4. Ergebnis
[KI-System liegt wahrscheinlich vor / liegt wahrscheinlich nicht vor / Grenzfall]

5. Dokumentationshinweis
Diese Einordnung beruht auf den angegebenen Tatsachen. Bei geänderter Zweckbestimmung, Modellwechsel, Integration in Hochrisiko-Prozesse oder neuem Nutzerkreis ist neu zu prüfen.

6. Nächste Skills
[territorialer-anwendungsbereich-art-2 / risikoklassen-uebersicht-und-triage / hochrisiko-art-6-abs-2-anhang-iii / gpai-vorliegen-art-3-nr-63 / abgrenzung-konventionelle-software-vs-ki-system]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Zu berücksichtigen sind Art. 3 Nr. 1, Nr. 12, Nr. 13 und Nr. 23 KI-VO, Erwägungsgrund 12 sowie die Kommissionsleitlinien zur Definition des KI-Systems. Keine Rechtsberatung; die Einordnung bleibt abhängig vom konkreten Tatsachenvortrag.
