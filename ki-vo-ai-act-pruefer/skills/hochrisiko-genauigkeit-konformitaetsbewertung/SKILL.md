---
name: hochrisiko-genauigkeit-konformitaetsbewertung
description: "Hochrisiko Genauigkeit Konformitaetsbewertung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Hochrisiko Genauigkeit Konformitaetsbewertung

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Hochrisiko Genauigkeit Konformitaetsbewertung** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hochrisiko-genauigkeit-robustheit-cybersicherheit-art-15` | Anbieter von Hochrisiko-KI fragt: Welche Leistungsstandards für Genauigkeit Robustheit und Cybersicherheit muessen wir nachweisen und dokumentieren? Art. 15 KI-VO Mindeststandards. Prüfraster: Genauigkeitsmetriken und Leistungserklärung Fehlertoleranz-Anforderungen Resilienz gegen adversarielle Eingaben Datenvergiftung Modell-Extraktion Backdoor-Angriffe. Output: Anforderungskatalog und Muster-Testprotokolle. Abgrenzung zu hochrisiko-risikomanagementsystem-art-9 (Risikobewertung) und hochrisiko-konformitätsbewertung-art-43-bis-49 (Bewertungsverfahren). |
| `hochrisiko-konformitaetsbewertung-art-43-bis-49` | Anbieter von Hochrisiko-KI fragt: Muessen wir eine benannte Stelle einschalten oder koennen wir die Konformitätsbewertung selbst durchführen? Art. 43 bis 49 KI-VO Konformitätsbewertung. Prüfraster: Entscheidungsbaum Selbstbewertung Modul A vs. Drittstellenprüfung Modul H vollständiges QMS. CE-Kennzeichnung EU-Konformitätserklärung Anhang V Registrierung EU-Datenbank. Output: Verfahrensauswahl-Entscheidungsbaum und Zeitplanung. Abgrenzung zu output-konformitaetserklaerung-eu-anhang-v und output-konformitaetsbescheinigung-evidence-pack. |
| `hochrisiko-risikomanagementsystem-art-9` | Anbieter von Hochrisiko-KI fragt: Wie setzen wir ein KI-VO-konformes Risikomanagementsystem auf und was muss es enthalten? Art. 9 KI-VO Risikomanagementsystem. Prüfraster: kontinuierlicher iterativer Prozess Risikoidentifikation Risikoabschaetzung Risikominderungsmassnahmen Restrisiko-Bewertung und -Akzeptanz Dokumentationspflicht. Typische Luecken fehlende Iterationszyklen unvollständige Risikolandkarte. Output: Risikomanagementsystem-Rahmenwerk und Vorlage Risikodokumentation. Abgrenzung zu hochrisiko-datenqualitaet-und-data-governance-art-10 und hochrisiko-konformitätsbewertung-art-43-bis-49. |
| `hochrisiko-technische-dokumentation-art-11-und-anhang-iv` | Anbieter von Hochrisiko-KI fragt: Was muss die technische Dokumentation enthalten und wie aktuell muss sie sein? Art. 11 i.V.m. Anhang IV KI-VO. Prüfraster: vollständiger Inhaltskatalog nach Anhang IV Systembeschreibung Entwicklungsprozess Datensaetze Leistungsmetriken Risikomanagement Konformitätsbewertungsergebnis Aktualisierungspflichten bei Systemaenderungen. Output: Dokumentations-Checkliste nach Anhang IV und Strukturvorlage. Abgrenzung zu hochrisiko-aufzeichnungspflichten-logging-art-12 (laufende Logs) und output-konformitätserklärung-eu-anhang-v (Konformitätserklärung). |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Hochrisiko Genauigkeit Konformitaetsbewertung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `hochrisiko-genauigkeit-robustheit-cybersicherheit-art-15`

**Fokus:** Anbieter von Hochrisiko-KI fragt: Welche Leistungsstandards für Genauigkeit Robustheit und Cybersicherheit muessen wir nachweisen und dokumentieren? Art. 15 KI-VO Mindeststandards. Prüfraster: Genauigkeitsmetriken und Leistungserklärung Fehlertoleranz-Anforderungen Resilienz gegen adversarielle Eingaben Datenvergiftung Modell-Extraktion Backdoor-Angriffe. Output: Anforderungskatalog und Muster-Testprotokolle. Abgrenzung zu hochrisiko-risikomanagementsystem-art-9 (Risikobewertung) und hochrisiko-konformitätsbewertung-art-43-bis-49 (Bewertungsverfahren).

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

## 2. `hochrisiko-konformitaetsbewertung-art-43-bis-49`

**Fokus:** Anbieter von Hochrisiko-KI fragt: Muessen wir eine benannte Stelle einschalten oder koennen wir die Konformitätsbewertung selbst durchführen? Art. 43 bis 49 KI-VO Konformitätsbewertung. Prüfraster: Entscheidungsbaum Selbstbewertung Modul A vs. Drittstellenprüfung Modul H vollständiges QMS. CE-Kennzeichnung EU-Konformitätserklärung Anhang V Registrierung EU-Datenbank. Output: Verfahrensauswahl-Entscheidungsbaum und Zeitplanung. Abgrenzung zu output-konformitaetserklaerung-eu-anhang-v und output-konformitaetsbescheinigung-evidence-pack.

# Konformitätsbewertung — Art. 43 bis 49 KI-VO

## Zweck

Vor dem Inverkehrbringen oder der Inbetriebnahme eines Hochrisiko-KI-Systems muss eine Konformitätsbewertung durchgeführt werden. Dieser Skill liefert den Entscheidungsbaum: Wer bewertet? Welches Verfahren? Was ist danach zu tun?

Wenn das Ergebnis anschließend druckreif als Bescheinigung, EU-Konformitätserklärung, Evidence Index und Lückenliste ausgegeben werden soll, an `output-konformitaetsbescheinigung-evidence-pack` übergeben.

## Entscheidungsbaum — Selbstbewertung oder benannte Stelle?

### Schritt 1 — Anhang-I-Systeme oder Anhang-III-Systeme?

**Anhang-I-Systeme (Art. 6 Abs. 1 KI-VO):** KI-Systeme als Sicherheitsbauteil in Produkten, die unter Anhang-I-Sektorrecht fallen.

Für diese Systeme richtet sich das Konformitätsbewertungsverfahren nach dem jeweiligen Sektorrecht (z.B. MDR, Maschinenverordnung). Wenn das Sektorrecht eine Konformitätsbewertung durch Dritte vorschreibt, gilt diese auch für das KI-System. In diesem Fall ist die Einbindung einer benannten Stelle obligatorisch.

**Anhang-III-Systeme (Art. 6 Abs. 2 KI-VO):** KI-Systeme, die in einem der acht Hochrisiko-Bereiche des Anhangs III tätig sind.

→ weiter zu Schritt 2.

### Schritt 2 — Biometrische Fernidentifikation?

Wenn das Hochrisiko-KI-System zur biometrischen Fernidentifikation von Personen verwendet wird:
- **Verpflichtend: Konformitätsbewertung durch benannte Stelle (Modul H)** — keine Selbstbewertung möglich (Art. 43 Abs. 1 lit. a KI-VO)

→ weiter zu Modul H.

### Schritt 3 — Alle anderen Anhang-III-Systeme

Für alle anderen Hochrisiko-KI-Systeme aus Anhang III besteht eine Wahlmöglichkeit:

**Option A — Selbstbewertung (Modul A nach Art. 43 Abs. 2 KI-VO)**
- Der Anbieter bewertet das System selbst anhand der in Art. 9 bis 15 KI-VO und Anhang IV festgelegten Anforderungen
- Interne Kontrolle der technischen Dokumentation
- Erstellung der EU-Konformitätserklärung
- CE-Kennzeichnung

**Voraussetzung:** Das System muss vollständig mit harmonisierten Normen (Art. 40 KI-VO) oder gemeinsamen Spezifikationen (Art. 41 KI-VO) konform sein.

**Option B — Konformitätsbewertung durch benannte Stelle (Modul H)**
- Vollständiges Qualitätsmanagementsystem (QMS) nach Anhang IX KI-VO
- Oder Bewertung der technischen Dokumentation durch benannte Stelle nach Anhang X KI-VO
- Benannte Stelle prüft, ob die Anforderungen erfüllt sind, und stellt eine Bescheinigung aus
- Anbieter erstellt EU-Konformitätserklärung und bringt CE-Kennzeichnung an

**Prüffragen:**
- Liegt für alle wesentlichen Anforderungen eine vollständige Abdeckung durch harmonisierte Normen vor?
- Hat der Anbieter ausreichende interne Kapazitäten für eine belastbare Selbstbewertung?
- Fordern Vertragspartner oder Kunden eine unabhängige Zertifizierung?

## EU-Konformitätserklärung (Art. 47 KI-VO / Anhang V KI-VO)

Nach erfolgter Konformitätsbewertung muss der Anbieter eine EU-Konformitätserklärung ausstellen. Diese enthält:
- Name und Anschrift des Anbieters
- Name und Nummer der benannten Stelle (falls zutreffend)
- Bezeichnung des KI-Systems
- Erklärung, dass das System den Anforderungen der KI-VO entspricht
- Verweis auf angewandte harmonisierte Normen oder gemeinsame Spezifikationen
- Ort und Datum der Ausstellung
- Unterschrift

Die EU-Konformitätserklärung wird zehn Jahre aufbewahrt.

## CE-Kennzeichnung (Art. 48 KI-VO)

Nach ausgestellter Konformitätserklärung ist am Hochrisiko-KI-System die CE-Kennzeichnung anzubringen. Bei rein digital bereitgestellten Systemen ist die CE-Kennzeichnung in der Benutzeroberfläche oder Begleitdokumentation anzubringen. Die Kennzeichnung muss gut sichtbar, lesbar und dauerhaft sein.

## Registrierung in der EU-Datenbank (Art. 49 und 71 KI-VO)

→ Detailskill: `eu-datenbank-registrierung-art-49-und-71`

Kurzüberblick:
- Anbieter registrieren vor Inverkehrbringen
- Betreiber (öffentliche Stellen) registrieren vor Nutzung
- Inhalte nach Anhang VIII KI-VO
- Datenbank ist öffentlich zugänglich (soweit nicht als vertraulich eingestuft)

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
PRUEFERGEBNIS — HOCHRISIKO KONFORMITAETSBEWERTUNG ART 43 BIS 49
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 43 Rn. 3]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 3. `hochrisiko-risikomanagementsystem-art-9`

**Fokus:** Anbieter von Hochrisiko-KI fragt: Wie setzen wir ein KI-VO-konformes Risikomanagementsystem auf und was muss es enthalten? Art. 9 KI-VO Risikomanagementsystem. Prüfraster: kontinuierlicher iterativer Prozess Risikoidentifikation Risikoabschaetzung Risikominderungsmassnahmen Restrisiko-Bewertung und -Akzeptanz Dokumentationspflicht. Typische Luecken fehlende Iterationszyklen unvollständige Risikolandkarte. Output: Risikomanagementsystem-Rahmenwerk und Vorlage Risikodokumentation. Abgrenzung zu hochrisiko-datenqualitaet-und-data-governance-art-10 und hochrisiko-konformitätsbewertung-art-43-bis-49.

# Risikomanagementsystem — Art. 9 KI-VO

## Zweck

Art. 9 KI-VO verpflichtet Anbieter von Hochrisiko-KI-Systemen, ein Risikomanagementsystem einzurichten und zu betreiben. Es ist kein einmaliger Akt, sondern ein kontinuierlicher, iterativer Prozess, der den gesamten Lebenszyklus des KI-Systems begleitet.

## Anforderungen an das Risikomanagementsystem

### Merkmal 1 — Kontinuierlicher iterativer Prozess

Das Risikomanagementsystem muss über den gesamten Lebenszyklus des KI-Systems aufrechterhalten und aktualisiert werden. Es beginnt vor dem Inverkehrbringen und endet nicht mit der Markteinführung.

**Prüffragen:**
- Gibt es einen formalen Prozess, der regelmäßig Risiken des Systems bewertet?
- Wird der Prozess bei wesentlichen Änderungen des Systems oder seiner Einsatzbedingungen aktualisiert?
- Sind Verantwortlichkeiten für das Risikomanagement klar zugewiesen?

### Merkmal 2 — Risikoidentifikation (Art. 9 Abs. 2 KI-VO)

Das System muss bekannte und hinreichend vorhersehbare Risiken für Gesundheit, Sicherheit oder Grundrechte identifizieren und dokumentieren, die aus dem KI-System entstehen können — sowohl bei bestimmungsgemäßem Gebrauch als auch bei vernünftigerweise vorhersehbarem Missbrauch.

**Prüffragen:**
- Wurden alle relevanten Risikoarten analysiert: technisches Versagen, Bias, Datenmängel, Missbrauch, Cyberangriffe?
- Wurden auch indirekte Risiken für Dritte (nicht nur direkte Nutzer) berücksichtigt?

### Merkmal 3 — Risikoabschätzung und Risikopriorisierung (Art. 9 Abs. 2 lit. b KI-VO)

Die identifizierten Risiken müssen bewertet werden — nach Schwere, Wahrscheinlichkeit und Reversibilität der Schäden. Dabei sind die spezifischen Eigenschaften der vorgesehenen Nutzer (Alter, Vulnerabilität) zu berücksichtigen.

**Prüffragen:**
- Werden Risiken nach Schwere und Wahrscheinlichkeit eingestuft?
- Werden betroffene Bevölkerungsgruppen und ihre besonderen Schutzbedürfnisse berücksichtigt?

### Merkmal 4 — Risikominderungsmaßnahmen (Art. 9 Abs. 4 KI-VO)

Für jedes identifizierte Risiko müssen angemessene Minderungsmaßnahmen getroffen werden. Die Maßnahmen sind in folgender Reihenfolge zu priorisieren:
1. Risikominderung durch Design und Entwicklung
2. Risikominderung durch Schutzmaßnahmen (technische und organisatorische Sicherheitsvorkehrungen)
3. Informationsmaßnahmen für Betreiber und Nutzer

**Prüffragen:**
- Wurden für jedes Risiko konkrete Maßnahmen definiert und dokumentiert?
- Wurden Design-Alternativen geprüft, bevor auf externe Schutzmaßnahmen zurückgegriffen wurde?

### Merkmal 5 — Restrisiko-Bewertung (Art. 9 Abs. 6 KI-VO)

Risiken, die trotz Minderungsmaßnahmen verbleiben (Restrisiken), müssen bewertet werden. Das Hochrisiko-KI-System darf nur in Verkehr gebracht werden, wenn das Gesamtrestrisiko als akzeptabel eingestuft wird.

**Prüffragen:**
- Ist das verbleibende Restrisiko dokumentiert?
- Hat eine zuständige Stelle das Restrisiko als akzeptabel eingestuft?

### Merkmal 6 — Testing und Validierung (Art. 9 Abs. 7 und 8 KI-VO)

Das KI-System muss vor dem Inverkehrbringen getestet werden. Bei Hochrisiko-KI in bestimmten Bereichen (biometrische Identifikation in Echtzeit, Strafverfolgung) können Real-World-Tests unter kontrollierten Bedingungen (Art. 60 KI-VO) vorgesehen sein.

**Prüffragen:**
- Gibt es eine dokumentierte Teststrategie?
- Wurden Tests mit repräsentativen Datensätzen und unter realistischen Einsatzbedingungen durchgeführt?

## Typische Lücken in der Praxis

- **Statisches Risikomanagement:** Das System wurde einmal analysiert und dann nie wieder überprüft.
- **Kein Bezug auf Grundrechte:** Technische Risiken werden bewertet, Grundrechtsrisiken (Diskriminierung, Freiheit, Würde) werden übersehen.
- **Fehlende Dokumentation:** Risiken wurden mündlich besprochen, aber nicht schriftlich festgehalten.
- **Kein Eskalationsprozess:** Es fehlt ein klar definierter Prozess, wie bei Risikovorfällen eskaliert wird.

## Verhältnis zu anderen Pflichten

Das Risikomanagementsystem nach Art. 9 KI-VO ist eng verknüpft mit:
- Art. 10 KI-VO (Datenqualität — schlechte Trainingsdaten erzeugen Risiken)
- Art. 12 KI-VO (Logging — Risikovorfälle müssen protokolliert werden)
- Art. 72 KI-VO (Post-Market-Monitoring — Risiken nach Inverkehrbringen)

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
PRUEFERGEBNIS — HOCHRISIKO RISIKOMANAGEMENTSYSTEM ART 9
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 9 Rn. 7]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 4. `hochrisiko-technische-dokumentation-art-11-und-anhang-iv`

**Fokus:** Anbieter von Hochrisiko-KI fragt: Was muss die technische Dokumentation enthalten und wie aktuell muss sie sein? Art. 11 i.V.m. Anhang IV KI-VO. Prüfraster: vollständiger Inhaltskatalog nach Anhang IV Systembeschreibung Entwicklungsprozess Datensaetze Leistungsmetriken Risikomanagement Konformitätsbewertungsergebnis Aktualisierungspflichten bei Systemaenderungen. Output: Dokumentations-Checkliste nach Anhang IV und Strukturvorlage. Abgrenzung zu hochrisiko-aufzeichnungspflichten-logging-art-12 (laufende Logs) und output-konformitätserklärung-eu-anhang-v (Konformitätserklärung).

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
