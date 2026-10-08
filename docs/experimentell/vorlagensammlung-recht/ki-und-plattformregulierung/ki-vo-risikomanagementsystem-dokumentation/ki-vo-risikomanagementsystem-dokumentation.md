# Risikomanagementsystem-Dokumentation für Hochrisiko-KI-Systeme (KI-VO Art. 9)

---

Kurz-Hinweis: Diese Vorlage ist unverbindlich, ein experimenteller Text und keine Rechtsberatung. Nutzung nur auf eigene Gewähr, eigene Gefahr und ohne Gewähr. Die ausführlichen Hinweise zu § 43a Abs. 2 BRAO, § 203 StGB, DSGVO sowie Apache-2.0 OR MIT stehen in der README dieser Vorlage.

---

## Vorlage

[WARNHINWEIS — nicht Dokumentbestandteil, nicht mitverwenden]

Diese Vorlage ersetzt nicht die anwaltliche Eigenleistung. Sie liefert das Gerüst, nicht den Fall. Der Anwender bringt den Sachverhalt, die Beweismittel, die taktische Entscheidung und die Verantwortung; die Vorlage bringt Struktur, Sprache und die unbedingt zu prüfenden Stellen. Wer nur Platzhalter füllt, ohne den eigenen Sachverhalt zu durchdenken, hat noch kein verwendbares Dokument, sondern einen Entwurf.

Weitere Hinweise und ausführliche Praxis-Erläuterungen in der README dieser Vorlage.

---

### Rubrum, Beteiligte und Bearbeitungsstand

**Hochrisiko-KI, Risikomanagement und Nachweislage**

**RISIKOMANAGEMENTSYSTEM-DOKUMENTATION**

Hochrisiko-KI-System — Dokumentversion [X.Y] vom [TT.MM.JJJJ]

---

### 1 Geltungsbereich und Dokumentzweck

1.1 **KI-System:** [Bezeichnung des Systems]

1.2 **Version des Systems:** [Versionskennung]

1.3 **Dokumentzweck:** Dieses Dokument beschreibt das Risikomanagementsystem gemäß Art. 9 VO (EU) 2024/1689 für das oben bezeichnete Hochrisiko-KI-System. Es ist Teil der Technischen Dokumentation nach Anhang IV Nr. 5 KI-VO und Grundlage des Konformitätsbewertungsverfahrens nach Art. 43 KI-VO.

1.4 **Verantwortliche Stelle:** [Firma, Abteilung, Kontaktperson]

1.5 **Änderungshistorie:**

| Version | Datum | Änderung | Freigegeben von |
|---|---|---|---|
| 1.0 | [TT.MM.JJJJ] | Erstfassung | [Name, Funktion] |
| [X.Y] | […] | […] | […] |

---

### 2 Prozess des Risikomanagementsystems

2.1 **Kontinuierlicher Prozess**

Das Risikomanagementsystem wird als iterativer, kontinuierlicher Prozess über den gesamten Lebenszyklus des KI-Systems geführt. Die Prozessschritte sind:

1) Identifikation und Analyse bekannter und vernünftigerweise vorhersehbarer Risiken (Art. 9 Abs. 2 lit. a KI-VO);

2) Schätzung und Bewertung der Risiken bei bestimmungsgemäßer Verwendung und vernünftigerweise vorhersehbarem Missbrauch (Art. 9 Abs. 2 lit. b KI-VO);

3) Evaluierung der nach Ergreifung von Maßnahmen verbleibenden Restrisiken (Art. 9 Abs. 2 lit. c KI-VO);

4) Festlegung geeigneter Risikomanagementmaßnahmen (Art. 9 Abs. 2 lit. d i. V. m. Abs. 4 und 5 KI-VO).

2.2 **Verantwortlichkeiten**

| Aufgabe | Verantwortliche Rolle | Person / Funktion |
|---|---|---|
| RMS-Gesamtverantwortung | [Chief AI Officer / CTO] | [Name] |
| Risikoidentifikation und -bewertung | [Risk Owner] | [Name] |
| Maßnahmenimplementierung | [Entwicklungsteam] | [Name] |
| Prüfung und Freigabe | [Compliance / Legal] | [Name] |
| Post-Market Monitoring | [Operations] | [Name] |

---

### 3 Risikoidentifikation

3.1 **Methodik:** Zur Identifikation von Risiken werden eingesetzt: [z. B. FMEA (Failure Mode and Effects Analysis), strukturierte Experteninterviews, Red-Team-Übungen, Analyse historischer Vorfälle vergleichbarer Systeme, DPIA-Befunde gemäß DSGVO Art. 35].

3.2 **Risikokategorien:**

| Kategorie | Beschreibung | Relevanz für dieses System |
|---|---|---|
| Technisches Versagen | Fehlklassifikationen, Modellabweichungen, Ausfälle | [ja/nein; Begründung] |
| Datenbezogene Risiken | Bias, Datendrift, unzureichende Datenqualität | [ja/nein; Begründung] |
| Missbrauchsrisiken | Zweckentfremdung, adversarielle Angriffe | [ja/nein; Begründung] |
| Grundrechterisiken | Diskriminierung, Verletzung der Privatsphäre, Würde | [ja/nein; Begründung] |
| Sicherheitsrisiken | Cybersecurity, Integrität der Outputs | [ja/nein; Begründung] |
| Vulnerabilitäten bestimmter Gruppen | Minderjährige, vulnerable Personengruppen (Art. 9 Abs. 9 KI-VO) | [ja/nein; Begründung] |
| Betriebsrisiken | Ausfall, fehlerhafte Integration, Schnittstellen | [ja/nein; Begründung] |

3.3 **Vollständige Risikoinventur:** Siehe Anlage 1 — Risikomatrix.

---

### 4 Risikoschätzung und -bewertung

4.1 **Bewertungsschema:**

Jedes identifizierte Risiko wird nach folgenden Dimensionen bewertet:

- **Schweregrad (S):** 1 (vernachlässigbar) — 2 (gering) — 3 (mittel) — 4 (schwer) — 5 (kritisch/irreversibel)
- **Eintrittswahrscheinlichkeit (W):** 1 (sehr selten) — 2 (selten) — 3 (möglich) — 4 (wahrscheinlich) — 5 (sehr wahrscheinlich)
- **Risikoprioritätszahl (RPZ):** S × W (Skala 1–25)

4.2 **Akzeptanzschwellen:**

| RPZ-Bereich | Einstufung | Handlungspflicht |
|---|---|---|
| 1–4 | Gering | Beobachtung; keine sofortige Maßnahme erforderlich |
| 5–9 | Mittel | Maßnahmen zu planen und zu dokumentieren |
| 10–16 | Hoch | Maßnahmen vor Inverkehrbringen umzusetzen |
| 17–25 | Kritisch | System darf nicht in Verkehr gebracht werden ohne Risikominderung auf ≤ 9 |

4.3 **Bewertungszyklus:** Neubewertung bei jeder wesentlichen Änderung des Systems sowie mindestens [halbjährlich / jährlich] im laufenden Betrieb.

---

### 5 Risikomanagementmaßnahmen

5.1 Für jedes Risiko mit RPZ ≥ 5 werden Maßnahmen nach folgendem Vorrangsystem festgelegt (Art. 9 Abs. 5 KI-VO):

1) Beseitigung oder technische Reduktion des Risikos durch Design- und Entwicklungsmaßnahmen (Vorrang);

2) Implementierung geeigneter Minderungs- und Kontrollmaßnahmen, wenn Beseitigung nicht technisch realisierbar;

3) Bereitstellung von Informationen nach Art. 13 KI-VO und ggf. Schulungen für Betreiber.

5.2 **Maßnahmenkatalog:** Siehe Anlage 1 — Risikomatrix, Spalten „Maßnahmen" und „Restrisiko nach Maßnahme".

---

### 6 Testing und Validierung

6.1 **Testplan:** Tests werden durchgeführt um sicherzustellen, dass geeignete und gezielte Risikomanagementmaßnahmen ergriffen worden sind (Art. 9 Abs. 6 KI-VO).

6.2 **Testphasen:**

| Testphase | Zeitpunkt | Methodik | Verantwortliche Stelle |
|---|---|---|---|
| Entwicklungsbegleitende Tests | Während Entwicklung | [z. B. Unit-Tests, Integrationstests] | […] |
| Vormarkt-Validierung | Vor Inverkehrbringen | [z. B. Adversarial Testing, Red Teaming] | […] |
| Post-Market Monitoring | Laufend nach Inverkehrbringen | [z. B. Performance-Überwachung, Vorfallsauswertung] | […] |

6.3 **Testergebnisse:** Zusammenfassung der Testergebnisse und Feststellungen:

[Narrative Zusammenfassung der Testergebnisse; detaillierte Testprotokolle als gesonderte Anlage zur Technischen Dokumentation]

---

### 7 Nachmarktüberwachung und Vorfallsmanagement

7.1 **Nachmarktüberwachungsplan:** Der Post-Market Monitoring Plan gemäß Art. 72 KI-VO ist in der Technischen Dokumentation (Anhang IV Nr. 6) gesondert dokumentiert.

7.2 **Schwerwiegende Vorfälle (Art. 73 KI-VO):** Betreiber sind anzuweisen, schwerwiegende Vorfälle und Fehlfunktionen, die Risiken für Gesundheit, Sicherheit oder Grundrechte darstellen, unverzüglich zu melden. Meldefrist: [15 Tage bei schwerwiegendem Vorfall; 2 Tage bei Risiko für Leben].

7.3 **Feedback-Schleife:** Die im Betrieb gewonnenen Erkenntnisse werden [quartalsweise] in die Risikoanalyse zurückgeführt.

---

### 8 Genehmigung und Freigabe

8.1 Diese Dokumentation wurde geprüft und freigegeben durch:

| Name | Funktion | Datum | Unterschrift |
|---|---|---|---|
| […] | [Chief AI Officer] | [TT.MM.JJJJ] | ________________ |
| […] | [Compliance / Legal Counsel] | [TT.MM.JJJJ] | ________________ |

---

### Schluss, Freigabe und Verwendung

**Freigebende Person / Stelle:** [Name, Funktion, Organisation]

[Ort], den [Datum]

_____________________________
[Unterschrift oder Freigabevermerk, Name, Funktion]

**Verwendung und Ablage:** [Adressat / Akte / Projekt], [Fassung], [Datum].

## Anlagen

| Anlage | Bezeichnung |
| --- | --- |
| Anlage 1 | Risikomatrix-Vorlage |

### Anlage 1 — Risikomatrix-Vorlage

1.2 Daten- und Plattformbezug: [Datenkategorie / Schnittstelle / Rollenverteilung / Risikokontrolle / Nachweis nach EU-Recht].

---

Lizenz: Apache-2.0 OR MIT.
