---
name: gpai-systemisches-risiko-urheberrecht-policy
description: "Gpai Systemisches Risiko Urheberrecht Policy: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Gpai Systemisches Risiko Urheberrecht Policy

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Gpai Systemisches Risiko Urheberrecht Policy** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gpai-systemisches-risiko-schwelle-10e25-flop` | Anbieter eines sehr grossen Basismodells fragt: Haben wir die Schwelle für systemisches Risiko ueberschritten und welche Zusatzpflichten gelten dann? Art. 51 und 55 KI-VO GPAI systemisches Risiko. Prüfraster: Schwellenwert 10 hoch 25 FLOP Trainingsrechenleistung Notifikationspflicht Kommission Art. 52 Abs. 1. Zusatzpflichten Art. 55: Modellbewertungen Gegenmassnahmen Vorfallmeldung Cybersicherheit adversarielle Tests. Output: Pflichtenprogramm systemisches-Risiko mit Fristen und Nachweisdokumentation. Abgrenzung zu gpai-modelle-art-51-bis-55 (Basis-GPAI-Pflichten). |
| `gpai-urheberrecht-policy-art-53` | GPAI-Urheberrechtspflichten nach Art. 53 KI-VO: Copyright-Policy, Trainingsdaten-Zusammenfassung, Rechtekette, TDM/Opt-out, Output-Risiko, Anbieterkommunikation und Evidence-Pack fuer Basismodelle und darauf aufsetzende Systeme. |
| `gpai-vorliegen-art-3-nr-63` | Prueft, ob ein Modell oder Dienst ein General-Purpose-AI-Modell oder GPAI-System nach der KI-VO ist und grenzt GPAI von Hochrisiko-KI ab. Behandelt ChatGPT-aehnliche Systeme, Foundation Models, API-Nutzung, GPAI-System Art. 3 Nr. 66, systemisches Risiko und Zweckbestimmung. Kernpunkt: GPAI/allgemeiner Chatbot ist nicht automatisch Hochrisiko; Hochrisiko entsteht erst bei konkreter Integration oder intendiertem Einsatz fuer Art. 6 Abs. 2/Anhang III-Zwecke. Output: GPAI-Einordnung und Routing zu Art. 50, Art. 51-55 oder Anhang-III-Pruefung. |
| `grundrechte-folgenabschaetzung-art-27-praxis` | Grundrechte-Folgenabschaetzung nach Art. 27 KI-VO in der Praxis: betroffene Gruppen, Zweck, Risiko, Diskriminierung, Datenschutz, menschliche Aufsicht, Beteiligung, Abhilfe, Residualrisiko und Board-Vorlage. |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Gpai Systemisches Risiko Urheberrecht Policy**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gpai-systemisches-risiko-schwelle-10e25-flop`

**Fokus:** Anbieter eines sehr grossen Basismodells fragt: Haben wir die Schwelle für systemisches Risiko ueberschritten und welche Zusatzpflichten gelten dann? Art. 51 und 55 KI-VO GPAI systemisches Risiko. Prüfraster: Schwellenwert 10 hoch 25 FLOP Trainingsrechenleistung Notifikationspflicht Kommission Art. 52 Abs. 1. Zusatzpflichten Art. 55: Modellbewertungen Gegenmassnahmen Vorfallmeldung Cybersicherheit adversarielle Tests. Output: Pflichtenprogramm systemisches-Risiko mit Fristen und Nachweisdokumentation. Abgrenzung zu gpai-modelle-art-51-bis-55 (Basis-GPAI-Pflichten).

# GPAI-Modelle mit systemischem Risiko — Art. 51 bis 55 KI-VO

## Zweck

Bestimmte GPAI-Modelle mit sehr hoher Trainingsrechenleistung gelten als Modelle mit systemischem Risiko und unterliegen verschärften Pflichten. Dieser Skill klärt den Schwellenwert, die Notifikationspflicht und die zusätzlichen Anforderungen.

## Schwellenwert — 10e25 FLOP (Art. 51 Abs. 1 lit. a KI-VO)

Ein GPAI-Modell gilt als Modell mit systemischem Risiko, wenn die kumulierte Trainingsrechenleistung 10e25 FLOP (Floating Point Operations) übersteigt.

**Was ist FLOP?** FLOP ist eine Maßeinheit für Rechenoperationen. 10e25 FLOP entspricht zehn hoch 25 Rechenoperationen — eine sehr hohe Schwelle, die zum Zeitpunkt der Verabschiedung der KI-VO nur von den größten bekannten Grundmodellen überschritten wurde.

**Prüffragen:**
- Kennt Ihr Unternehmen die kumulierte Trainingsrechenleistung des Modells?
- Überschreitet diese Rechenleistung 10e25 FLOP?

**Wenn unklar:** Die Berechnung der FLOP-Trainingsrechenleistung hängt von Architektur, Datenmenge und Trainingszeit ab. Im Zweifelsfall sind technische Experten und das Europäische KI-Büro zu konsultieren.

## Systemisches Risiko durch Kommissionsbeschluss (Art. 51 Abs. 1 lit. b KI-VO)

Unabhängig von der FLOP-Schwelle kann die Kommission ein GPAI-Modell durch Beschluss als Modell mit systemischem Risiko einstufen, wenn es auf der Grundlage bestimmter Kriterien ein systemisches Risiko darstellt. Solche Beschlüsse können auch für Modelle unterhalb der FLOP-Schwelle gelten.

**Kriterien für einen Kommissionsbeschluss:**
- Anzahl der Nutzer (Erreichung kritischer Masse)
- Einsatz in Hochrisikobereichen
- Marktmacht des Anbieters
- Potenzielle Auswirkungen auf demokratische Prozesse

## Notifikationspflicht (Art. 52 Abs. 1 KI-VO)

Anbieter von GPAI-Modellen, die die FLOP-Schwelle überschreiten, müssen dies der Kommission vor dem Inverkehrbringen des Modells mitteilen.

**Inhalt der Notifikation:**
- Identität des Anbieters
- Trainingsrechenleistung
- Datum des Inverkehrbringens oder der Bereitstellung

Anbieter können auch freiwillig eine Selbsteinstufung vornehmen, wenn sie meinen, dass ihr Modell systemisches Risiko aufweist.

## Zusätzliche Pflichten für Modelle mit systemischem Risiko (Art. 55 KI-VO)

### Pflicht 1 — Modellbewertung (Art. 55 Abs. 1 lit. a KI-VO)

Anbieter müssen:
- Das Modell auf der Grundlage standardisierter Protokolle und Tools evaluieren
- Systemische Risiken identifizieren und bewerten
- Red-Teaming-Übungen durchführen, um Adversarial-Risiken zu erkennen

### Pflicht 2 — Gegenmaßnahmen (Art. 55 Abs. 1 lit. b KI-VO)

Anbieter müssen angemessene Maßnahmen ergreifen, um festgestellte systemische Risiken zu mindern:
- Technische Schutzmaßnahmen
- Informations- und Sicherheitsrichtlinien
- Kooperation mit anderen Anbietern (gemeinsame Risikobewertung)

### Pflicht 3 — Vorfallmeldung (Art. 55 Abs. 1 lit. c KI-VO)

Anbieter von Modellen mit systemischem Risiko müssen schwerwiegende Vorfälle und mögliche Korrektivmaßnahmen unverzüglich der Kommission und der nationalen Behörde melden. Fristen werden durch Durchführungsrechtsakte konkretisiert.

### Pflicht 4 — Cybersicherheit (Art. 55 Abs. 1 lit. d KI-VO)

Anbieter müssen ein angemessenes Niveau an Cybersicherheitsschutz sicherstellen — sowohl für das Modell selbst als auch für die physische Infrastruktur.

## Verhältnis zu Codes of Practice (Art. 56 KI-VO)

Anbieter von GPAI-Modellen (mit und ohne systemisches Risiko) sollen an der Ausarbeitung von Verhaltenskodizes mitwirken. Für Modelle mit systemischem Risiko können Verhaltenskodizes als Konkretisierung der Pflichten aus Art. 55 KI-VO dienen. → `code-of-practice-und-harmonisierte-normen`

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

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Massnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — GPAI SYSTEMISCHES RISIKO SCHWELLE 10E25 FLOP
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 51 Abs. 1 lit. b Rn. 8]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 2. `gpai-urheberrecht-policy-art-53`

**Fokus:** GPAI-Urheberrechtspflichten nach Art. 53 KI-VO: Copyright-Policy, Trainingsdaten-Zusammenfassung, Rechtekette, TDM/Opt-out, Output-Risiko, Anbieterkommunikation und Evidence-Pack fuer Basismodelle und darauf aufsetzende Systeme.

# GPAI: Urheberrechtliche Policy nach Art. 53 KI-VO

## Ziel

Anbieter von GPAI-Modellen müssen urheberrechtliche Compliance nicht nur behaupten, sondern dokumentieren. Dieser Skill baut dafür eine Policy und ein Evidence-Pack.

## Normanker

- Art. 53 KI-VO: technische Dokumentation, Informationen für Downstream-Anbieter, Urheberrechtspolitik, Zusammenfassung der Trainingsinhalte.
- Art. 51 ff. KI-VO: GPAI und systemisches Risiko.
- § 44b UrhG und unionsrechtliche TDM-Regeln als deutsche Schnittstelle.

## Prüfschritte

1. Modell und Anbieterrolle bestimmen.
2. Trainingsdatenquellen clustern: frei, lizenziert, eigene Daten, Webcrawl, Kundenmaterial, synthetische Daten.
3. Opt-out-Mechanismen prüfen: maschinenlesbare Vorbehalte, Vertragsverbote, Rechteinhaberhinweise.
4. Rechtekette dokumentieren.
5. Zusammenfassung der Trainingsinhalte so formulieren, dass sie hinreichend aussagekräftig ist, aber keine Geschäftsgeheimnisse unnötig offenlegt.
6. Downstream-Informationen bereitstellen.

## Output

- Copyright-Policy.
- Trainingsdaten-Kategorienübersicht.
- Opt-out-Handling.
- Vendor-/Modelcard-Fragen.
- Lückenliste für nicht belegte Datenquellen.

## Warnung

Urheberrechtliche Compliance ist nicht mit "Daten waren öffentlich im Internet" erledigt. Prüfe Lizenz, TDM-Ausnahme, Opt-out und Reproduktionsrisiko getrennt.

## 3. `gpai-vorliegen-art-3-nr-63`

**Fokus:** Prueft, ob ein Modell oder Dienst ein General-Purpose-AI-Modell oder GPAI-System nach der KI-VO ist und grenzt GPAI von Hochrisiko-KI ab. Behandelt ChatGPT-aehnliche Systeme, Foundation Models, API-Nutzung, GPAI-System Art. 3 Nr. 66, systemisches Risiko und Zweckbestimmung. Kernpunkt: GPAI/allgemeiner Chatbot ist nicht automatisch Hochrisiko; Hochrisiko entsteht erst bei konkreter Integration oder intendiertem Einsatz fuer Art. 6 Abs. 2/Anhang III-Zwecke. Output: GPAI-Einordnung und Routing zu Art. 50, Art. 51-55 oder Anhang-III-Pruefung.

# GPAI, allgemeiner Chatbot und Hochrisiko-Abgrenzung

## Zweck

Dieser Skill klärt, ob ein Modell oder Dienst ein General-Purpose-AI-Modell (GPAI-Modell) oder ein GPAI-System ist und wie dies zur Hochrisiko-Einstufung nach Art. 6 KI-VO steht.

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


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `grundrechte-folgenabschaetzung-art-27-praxis`

**Fokus:** Grundrechte-Folgenabschaetzung nach Art. 27 KI-VO in der Praxis: betroffene Gruppen, Zweck, Risiko, Diskriminierung, Datenschutz, menschliche Aufsicht, Beteiligung, Abhilfe, Residualrisiko und Board-Vorlage.

# Grundrechte-Folgenabschätzung nach Art. 27 KI-VO

## Ziel

Der Skill macht aus Art. 27 KI-VO eine konkrete Prüfung, die nicht nach Ethikpapier aussieht, sondern Entscheidungen, Risiken und Abhilfen dokumentiert.

## Prüffragen

1. Ist das System Hochrisiko?
2. Wer ist Betreiber und fällt in den Art.-27-Pflichtenkreis?
3. Welche Personen oder Gruppen sind betroffen?
4. Welche Grundrechte können berührt sein: Gleichbehandlung, Datenschutz, Meinungsfreiheit, Berufsfreiheit, effektiver Rechtsschutz?
5. Welche Fehler wären besonders schädlich?
6. Gibt es Schutzmaßnahmen: menschliche Kontrolle, Widerspruch, Transparenz, Monitoring, Bias-Test?
7. Was bleibt als Residualrisiko?

## Output

Erzeuge:

- FRIA-Template.
- Risikomatrix.
- Abhilfenplan.
- Freigabeentscheidung.
- Re-Evaluation-Trigger.

## Qualitätsregel

Grundrechte nicht ornamental nennen. Immer erklären, welche konkrete Systemfunktion welches konkrete Recht wie berührt.
