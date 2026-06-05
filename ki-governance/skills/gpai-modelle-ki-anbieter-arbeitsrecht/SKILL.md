---
name: gpai-modelle-ki-anbieter-arbeitsrecht
description: "Gpai Modelle KI Anbieter Arbeitsrecht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Gpai Modelle KI Anbieter Arbeitsrecht

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Gpai Modelle KI Anbieter Arbeitsrecht** im Plugin KI-Governance. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gpai-modelle-systemic-risk` | General-Purpose-AI-Modelle Art. 51 ff. KI-VO: Standardpflichten (Dokumentation, Trainingsdaten, Urheberrecht), zusaetzliche Pflichten fuer Modelle mit systemischem Risiko ab 10E25 FLOPs Trainingsrechenleistung. Verhaltenskodex und CE-Modell. Compliance-Roadmap fuer Modellanbieter. |
| `ki-anbieter-pruefung` | Prüft KI-Anbieterverträge gegen die unternehmenseigenen Governance- Positionen; kennzeichnet Training auf Daten, Haftung, Modelländerungen und KI-Richtlinien-Konsistenz. Unterscheidet Anbieter/Betreiber-Rolle nach Art. 3 KI-VO; prüft Vertragspflichten nach Art. 25 KI-VO. Lädt, wenn der Nutzer "KI-Vertrag prüfen", "Anbietervertrag KI", "AI Act Art. 25 Vertragspflichten" oder "KI-AGB prüfen" sagt. |
| `ki-arbeitsrecht-mitbestimmung` | Arbeitsrechtliche Folgen des KI-Einsatzes: Mitbestimmung des Betriebsrats § 87 Abs. 1 Nr. 6 BetrVG technische Einrichtung zur Verhaltens- und Leistungskontrolle, Betriebsvereinbarung KI, Datenschutz BDSG-neu und DSGVO. Bewerber-KI und Auswahl-Algorithmen. Mustertexte und Verhandlungstaktik. |

## Arbeitsweg

Im Plugin KI-Governance gilt für **Gpai Modelle KI Anbieter Arbeitsrecht**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gpai-modelle-systemic-risk`

**Fokus:** General-Purpose-AI-Modelle Art. 51 ff. KI-VO: Standardpflichten (Dokumentation, Trainingsdaten, Urheberrecht), zusaetzliche Pflichten fuer Modelle mit systemischem Risiko ab 10E25 FLOPs Trainingsrechenleistung. Verhaltenskodex und CE-Modell. Compliance-Roadmap fuer Modellanbieter.

# GPAI: Systemic-Risk-Modelle

## Spezialwissen: GPAI: Systemic-Risk-Modelle
- **Spezialgegenstand:** GPAI: Systemic-Risk-Modelle / gpai modelle systemic risk. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AI, Art. 51, KI, VO, CE, GPAI.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `ki-anbieter-pruefung`

**Fokus:** Prüft KI-Anbieterverträge gegen die unternehmenseigenen Governance- Positionen; kennzeichnet Training auf Daten, Haftung, Modelländerungen und KI-Richtlinien-Konsistenz. Unterscheidet Anbieter/Betreiber-Rolle nach Art. 3 KI-VO; prüft Vertragspflichten nach Art. 25 KI-VO. Lädt, wenn der Nutzer "KI-Vertrag prüfen", "Anbietervertrag KI", "AI Act Art. 25 Vertragspflichten" oder "KI-AGB prüfen" sagt.

# KI-Anbieterprüfung

## Zweck

KI-Anbieterverträge sind der Ort, an dem Governance-Positionen tatsächlich
auf die Probe gestellt werden. Das Erstgespräch erfasst, was das Unternehmen
*will*. Diese Skill prüft, was es *vereinbart hat*.

Blickwinkel: Wir sind Betreiber/Käufer. Kein Rollenwechsel.

**AI Act Art. 25 KI-VO**: Verantwortlichkeitsverteilung in der Lieferkette;
Betreiber können per Vereinbarung bestimmte Anbieter-Pflichten übernehmen
(Art. 25 Abs. 1 KI-VO). Art. 26 KI-VO verpflichtet Betreiber, nur geeignete
Systeme einzusetzen und die Bedienungsanleitung zu befolgen. Beide Punkte
müssen im Vertrag explizit geregelt sein.

Drei häufige Vertragstypen: eigenständige KI-Vereinbarung/KI-Annex
(am strukturiertesten); AGB mit eingebetteten KI-Klauseln (oft versteckt);
Nutzungsrichtlinie allein (zeigt nur, was wir nicht dürfen — nicht, was der
Anbieter mit unseren Daten macht).

## Eingaben

- KI-Vertrag, KI-Annex oder AGB-KI-Abschnitt (Datei oder eingefügter Text)
- Praxisprofil aus `CLAUDE.md` (Anbieter-Governance-Positionen, KI-Richtlinien-
 Verpflichtungen, Anwendungsfall-Register)
- Anbieter-Name und Verwendungszweck

## Rechtlicher Rahmen

**Kernvorschriften**

- **AI Act Art. 3 Nr. 3/4 KI-VO**: Definitionen Anbieter/Betreiber; maßgeblich
 für Pflichtenzuordnung.
- **AI Act Art. 25 KI-VO**: Verantwortlichkeiten in der Lieferkette; vertragliche
 Pflichten-Übertragung; Betreiber darf keine Art. 5-Verbote veranlassen
 (Art. 25 Abs. 2 KI-VO).
- **AI Act Art. 26/29 KI-VO**: Betreiberpflichten (Eignung prüfen, Anleitung
 befolgen, menschliche Aufsicht sicherstellen, Protokollierung).
- **DSGVO Art. 28**: AVV-Pflichten bei KI-Auftragsverarbeitung; Prüfungsrecht
 Art. 28 Abs. 3 lit. h DSGVO.
- **GeschGehG §§ 2, 4**: Eingabe vertraulicher Daten in externe KI kann
 Geheimnisschutz gefährden, wenn Anbieter für Training nutzt.
- **BGB §§ 305 ff. (§ 307)**: AGB-Kontrolle; unangemessene
 Haftungsbeschränkungen können unwirksam sein.
- **Produkthaftungs-RL 2024/2853/EU**: KI-Systeme als Produkte; relevant bei
 Haftungsklauseln im Anbietervertrag.
- **UrhG § 44b**: Text-und-Data-Mining-Schranke; relevant bei Training auf
 lizenzierten Inhalten.

**Leitentscheidungen**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Vertragsgestaltung muss DSGVO Art. 22 Widerspruchs- und Prüfungsrechte
 operationalisieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 von Haftungsausschlüssen bei komplexen IT-Systemen; Maßstab für KI-
 Anbieter-Haftungsklauseln.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Anforderungen an Vertragsgestaltung zum Schutz von Geschäftsgeheimnissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Datenübermittlung an externe Dienstleister; übertragbar auf KI-AVV.

**Kommentare**

- Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 25 Rn. 5
 (Verantwortlichkeitsverteilung; vertragliche Pflichten-Übertragung; Doppelautoren-Kommentar).
- Hoffmann, in: Spindler/Schuster, Recht der elektronischen Medien, 4. Aufl. 2024,
 Teil IV Rn. 120 (Vertragsgestaltung bei KI-Diensten).
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
 bei IT-/Softwareverträgen; KI-Haftungsklauseln).
- Bertermann, in: Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 28 Rn. 30.

*Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im Einzelfall.*

## Ablauf

**Schritt 1 — Playbook und Stack klären**

`CLAUDE.md` → `## KI-Anbieter-Governance` und `## KI-Richtlinien-Verpflichtungen`.

KI-Stack kartieren vor Klausel-Prüfung:
1. End-User-SaaS (z. B. Legal-Tech-Tool)
2. API-Gateway/Orchestrierung (z. B. Azure OpenAI, AWS Bedrock, Vertex)
3. Modellanbieter (z. B. Anthropic, OpenAI, Google)
4. Wissensbasis/RAG-Quelle
5. Weitere Unterauftragnehmer

Bei gestapelten Anbietern: beide Vertragswerke prüfen. Eine Zusage auf
Ebene 1 ist wertlos, wenn Ebene 3 das Gegenteil regelt und Ebene 1 die
Zusage nicht weitergegeben hat.

**Schritt 2 — Klausel-für-Klausel-Prüfung**

| Klausel | Anbieter sagt | Unsere Position | Lücke | Schweregrad |
|---|---|---|---|---|
| Training auf unseren Daten | | | | |
| Vertraulichkeit der Eingaben | | | | |
| Modelländerungen | | | | |
| Ausgabe-IP / Rücklizenz | | | | |
| Haftung für Ausgaben (§ 307 BGB) | | | | |
| Vorfallbenachrichtigung | | | | |
| Menschliche Überprüfungsrechte | | | | |
| Nutzungsbeschränkungen | | | | |
| Prüfrechte / SOC 2 (Art. 28 Abs. 3 lit. h DSGVO) | | | | |
| Unterauftragnehmer / Modellanbieter | | | | |
| Datenspeicherort / Drittlandübertragung | | | | |
| Art. 25 KI-VO — Pflichten-Zuordnung | | | | |

Schweregrad (gegen CLAUDE.md-Positionen):
- ✅ **Aligned** — Standard oder besser
- ⚠️ **Hinweis** — innerhalb Fallback, schlechter als Standard
- 🟠 **Erheblich** — außerhalb Standard, innerhalb Fallback; Redline nötig
- ❌ **Kritisch** — außerhalb Fallback; Eskalation; kein Einsatz ohne Klärung

**Weitergabetest** bei gestapelten Anbietern: Vertrag auf Flow-Down-Klauseln
prüfen. Bei fehlender Weitergabe: konkrete Redline produzieren:
> "Ergänzen in § [X]: Anbieter stellt sicher, dass Unterauftragnehmer
> Pflichten zu [Datennutzung/Training/Vertraulichkeit] eingehen, die nicht
> weniger schützend sind als diese Vereinbarung."

**Schritt 3 — KI-Annex-Lückenprüfung**

AVV vorhanden, aber kein KI-Annex → kennzeichnen: bei Standard-Tier
tolerierbar; bei erhöhter/hoher Stufe ein ❌-Blocker (keine Regelung zu
Training, Modelländerungen, Art. 25 KI-VO, Haftung).

Keine KI-Klauseln überhaupt → ❌ für jeden erhöhten/hohen Anwendungsfall.

**Schritt 4 — KI-Richtlinien-Konsistenzprüfung**

Häufige Konflikte: Unsere Richtlinie verbietet Training → Anbieter erlaubt
es standardmäßig; unsere Richtlinie verlangt Human-Review → Anbieter-
Ausgaben sind final; Anbieter nicht auf Freigabeliste; DSGVO Art. 22
Widerspruchsrecht nicht operationalisiert. Jeden Widerspruch kennzeichnen.

**Schritt 5 — Redline-Granularität**

So klein wie möglich. Wort → Phrase → Unterklausel → Satz → Klausel.
Chirurgische Redlines signalisieren: wir haben sorgfältig gelesen.

## Ausgabeformat

```markdown
# KI-Anbieterprüfung: [Anbietername]
Geprüftes Dokument: [Typ] | Datum: [heute]
Anwendungsfall(e): [Zweck] | Governance-Stufe: [Standard/Erhöht/Hoch]

## Ergebnis
[2 Sätze: Können wir einsetzen? Was muss sich zuerst ändern?]
Befunde: [N]❌ [N]🟠 [N]⚠️ [N]✅

## Klausel-für-Klausel [Tabelle gem. Schritt 2]
## KI-Annex-Status [Vorhanden/Fehlend + Konsequenz]
## KI-Richtlinien-Konsistenz [✅/⚠️ Liste]
## Empfohlene Redlines [konsolidiert; vor Übermittlung mit Anwalt abstimmen]
## Wenn der Anbieter nicht nachgibt [Fallback oder Eskalation je Punkt]
```

Bei Nicht-Jurist-Rolle vor Unterzeichnungsempfehlung: anwaltliche Prüfung
abfragen; 1-seitigen Kurzüberblick generieren.

## Beispiel

**Anfrage:** "OpenAI Enterprise für interne Rechtsrecherche prüfen."
**Vorgehen:** Stack: OpenAI ist Modell- und SaaS-Ebene in einem.
Training: OpenAI Enterprise sieht kein Training auf Eingaben vor —
bestätigen; GeschGehG prüfen. Haftung: AGB-Ausschluss → § 307 BGB prüfen.
Art. 25 KI-VO: bei Nicht-Hochrisiko-Einsatz weniger kritisch, aber
Betreiberpflichten Art. 26/29 dokumentieren. AVV: DSGVO Art. 28 prüfen.

## Risiken und typische Fehler

- Training-auf-Daten-Klausel ist die am häufigsten übersehene: nie aus
 Reputation annehmen; in Schriftform bestätigen lassen.
- Stack nicht kartieren: modern KI ist geschichtet; nur die Oberfläche zu
 prüfen ist der häufigste Fehler.
- Nutzungsrichtlinie mit Datennutzungsklausel verwechseln: AUP ≠ Data Terms.
- Verlängerungen als Hebel nutzen: Lücken jetzt dokumentieren.

## Quellenpflicht

- **AI Act Art. 3 Nr. 3/4, Art. 25, Art. 26/29** — VO (EU) 2024/1689.
- **DSGVO Art. 28** bei Auftragsverarbeitung.
- **GeschGehG § 2 Nr. 1** bei Training-auf-Daten.
- **BGB §§ 305 ff. (§ 307)** bei AGB-Haftungsklauseln.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 25 Rn. 5** (Doppelautoren-Kommentar).
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- **Bertermann, in: Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 28 Rn. 30.**

## Triage zu Beginn
1. Welcher KI-Stack liegt vor — End-User-SaaS, API-Gateway, Modellanbieter, mehrere Schichten?
2. Ist der Anbietervertrag ein eigenstaendiger KI-Annex oder nur AGB mit eingebetteten Klauseln?
3. Erlaubt der Anbieter Training auf Eingabedaten — explizit oder per Schweigen in AGB?
4. Ist der Anbieter in einem Drittland — laeuft Art. 28 DSGVO AVV und Drittlandstransfer-Pruefung?
5. Liegt ein Hochrisiko-Anwendungsfall vor — gelten Art. 25/26 KI-VO Betreiberpflichten?

## Output-Template — KI-Anbieter-Pruefungsbericht
**Adressat:** Rechts-/Compliance-Team — Tonfall: sachlich-strukturiert
```
KI-ANBIETER-PRUEFUNGSBERICHT
[DATUM] — Anbieter: [ANBIETERNAME] — Anwendungsfall: [BESCHREIBUNG]

ERGEBNIS: [FREIGABE / FREIGABE MIT AUFLAGEN / ABGELEHNT]
Befunde: [N] kritisch / [N] erheblich / [N] Hinweis / [N] aligned

KLAUSEL-PRUEFUNG (Auswahl):
| Klausel | Anbieter-Position | Unsere Position | Schweregrad |
|---|---|---|---|
| Training auf Daten | [ANBIETERTEXT] | Kein Training | [STATUS] |
| Haftung fuer Ausgaben | [ANBIETERTEXT] | § 307 BGB | [STATUS] |
| Art. 25 KI-VO Pflichten | [ANBIETERTEXT] | Klar geregelt | [STATUS] |
| DSGVO Art. 28 AVV | [STATUS] | Erforderlich | [STATUS] |

EMPFOHLENE REDLINES:
1. [KLAUSEL-REF]: [REDLINE-VORSCHLAG]

WENN ANBIETER NICHT NACHGIBT:
[FALLBACK ODER ESKALATIONSWEG]

Erstellt: [NAME], [DATUM] — Vor Unterzeichnung anwaltliche Pruefung einholen.
```

## 3. `ki-arbeitsrecht-mitbestimmung`

**Fokus:** Arbeitsrechtliche Folgen des KI-Einsatzes: Mitbestimmung des Betriebsrats § 87 Abs. 1 Nr. 6 BetrVG technische Einrichtung zur Verhaltens- und Leistungskontrolle, Betriebsvereinbarung KI, Datenschutz BDSG-neu und DSGVO. Bewerber-KI und Auswahl-Algorithmen. Mustertexte und Verhandlungstaktik.

# KI: Arbeitsrecht und BR

## Spezialwissen: KI: Arbeitsrecht und BR
- **Spezialgegenstand:** KI: Arbeitsrecht und BR / ki arbeitsrecht mitbestimmung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, BetrVG, BDSG, DSGVO, BR.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
