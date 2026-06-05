---
name: ki-erforderlichkeit-no-training-mandanten
description: "Erforderlichkeit NO Training Mandanten: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Erforderlichkeit NO Training Mandanten

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Erforderlichkeit NO Training Mandanten** im Plugin Berufsrecht Ki Vertragspruefung. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ki-erforderlichkeit-ex-ante-vermerk` | Ex-ante-Vermerk zur Erforderlichkeit nach § 43e BRAO für KI-Outsourcing: Zweck der Offenlegung, Datenminimierung, Alternativen, Mandatsklassen, Kanzleiinfrastruktur, Einzelmandat, No-Training und Freigabebegründung dokumentieren. |
| `ki-no-training-modellverbesserung-telemetrie` | No-Training, Modellverbesserung und Telemetrie im KI-Vertrag prüfen: Mandatsdaten dürfen nicht für Training, Produktverbesserung, Benchmarks, Supportauswertung oder allgemeine Modelloptimierung abfließen; Klausel- und Rückfragebausteine. |
| `mandanten-aufklaerungspflicht-ki` | Aufklaerungspflicht gegenueber Mandanten beim KI-Einsatz: § 43 BRAO Vertrauensverhaeltnis, § 13 BORA, BGH-Rechtsprechung zur Informationsweitergabe. Mustertexte Mandantenanschreiben und Mandatsvertrag. Pruefraster fuer notwendigen Informationsumfang. |

## Arbeitsweg

Im Plugin Berufsrecht Ki Vertragspruefung gilt für **Erforderlichkeit NO Training Mandanten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `ki-erforderlichkeit-ex-ante-vermerk`

**Fokus:** Ex-ante-Vermerk zur Erforderlichkeit nach § 43e BRAO für KI-Outsourcing: Zweck der Offenlegung, Datenminimierung, Alternativen, Mandatsklassen, Kanzleiinfrastruktur, Einzelmandat, No-Training und Freigabebegründung dokumentieren.

# Ex-ante-Vermerk zur Erforderlichkeit

## Kern

Erforderlichkeit meint nicht: "Könnte man theoretisch ohne KI arbeiten?" Maßgeblich ist, ob der Zugang zu Berufsgeheimnissen für die konkret beauftragte Dienstleistung in der gewählten, vertretbar organisierten Kanzleiumgebung benötigt wird. Genau das muss vor dem Einsatz dokumentiert werden.

## Vermerkstruktur

1. **Tool und Zweck:** Dokumentenanalyse, Recherche, Zusammenfassung, Übersetzung, Diktat, Fristenassistenz, Chatbot, RAG.
2. **Datenklassen:** Welche Aktenbestandteile sind nötig, welche bleiben draußen?
3. **Alternativen:** anonymisierte Nutzung, lokales Tool, manuelle Bearbeitung, anderes Enterprise-Angebot.
4. **Datenminimierung:** Redaction, Mandantentrennung, Rollenrechte, keine Vollakte ohne Zweck.
5. **Vertragliche Grundlage:** Textform, Verschwiegenheit, Belehrung, Subunternehmer, No-Training.
6. **Drittstaat:** Hosting, Support, Muttergesellschaft, Zugriffsmöglichkeiten, zusätzliche Schutzmaßnahmen.
7. **Mandatsbezug:** Kanzleiinfrastruktur oder Einzelmandat mit zusätzlicher Mandantenentscheidung?
8. **Endkontrolle:** Wer prüft Output, Quellen, Fristen und taktische Aussage?

## Musterentscheidung

Nutze diese Logik, ohne Scheinsicherheit:

- "Freigegeben für anonymisierte und interne Kanzleidaten."
- "Freigegeben für Mandatsdaten der Klasse X nach Toolfreigabe und §-43e-Vertrag."
- "Nur nach Mandanteninformation/Einwilligung."
- "Nicht freigegeben, weil Training/Telemetrie/Subunternehmer/Drittstaat ungeklärt."

## Output

Erzeuge einen zwei- bis dreiseitigen Kanzleivermerk, der in die Toolakte gelegt werden kann:

- Ergebnis in einem Satz
- tragende Gründe
- Restrisiken
- Nachprüftermin
- Verantwortliche Person

## 2. `ki-no-training-modellverbesserung-telemetrie`

**Fokus:** No-Training, Modellverbesserung und Telemetrie im KI-Vertrag prüfen: Mandatsdaten dürfen nicht für Training, Produktverbesserung, Benchmarks, Supportauswertung oder allgemeine Modelloptimierung abfließen; Klausel- und Rückfragebausteine.

# No-Training, Modellverbesserung und Telemetrie

## Leitgedanke

Die Dienstleistung darf Mandatsdaten verarbeiten, soweit das für den beauftragten Zweck nötig ist. Daraus folgt nicht, dass der Anbieter diese Daten für Training, allgemeine Produktverbesserung, Benchmarks, Qualitätsdatenbanken oder Vertriebsanalysen nutzen darf.

## Prüffelder

- **Training:** Fine-Tuning, Reinforcement Learning, supervised review, synthetische Trainingsdaten aus Mandatsinput.
- **Produktverbesserung:** Qualitätsmetriken, Fehleranalyse, Modellvergleiche, Prompt-/Output-Sammlungen.
- **Telemetrie:** Prompt-Logs, Nutzungsprofile, Tokenstatistik mit Inhaltsbezug, Abuse Monitoring.
- **Support:** Einsicht durch Supportteams, Screenshots, Debugging, Ticketanhänge.
- **Subunternehmer:** Modellhoster, Vektor-Datenbank, Logging-Dienst, Security-Provider.
- **Retention:** Speicherdauer für Inputs, Outputs, Embeddings, Metadaten, Backups.

## Rote Formulierungen

- "may use Customer Content to improve services" ohne Berufsgeheimnis-Ausnahme
- "de-identified data" ohne strenge Lösch-/Reidentifikationsregeln
- "analytics and product development" als offene Generalklausel
- Supportzugriff ohne Need-to-know, Protokollierung und Kanzleifreigabe
- Subprocessor-Liste ohne Zustimmungsvorbehalt

## Mindestklauseln

Fordere:

1. Keine Nutzung von Mandatsdaten für Training oder allgemeine Modellverbesserung.
2. Keine dauerhafte Speicherung von Prompts/Outputs außerhalb der vereinbarten Retention.
3. Supportzugriffe nur fallbezogen, protokolliert, möglichst nach Freigabe.
4. Embeddings und Vektor-Datenbanken mandats- oder mandantengetrennt.
5. Subunternehmer nur mit Weiterverpflichtung und Änderungsnotice.
6. Lösch- und Exportpfad bei Vertragsende.

## Output

Erstelle eine Vertragslückenliste mit:

- Fundstelle im Vertrag
- Risiko für § 43e BRAO, § 203 StGB, DSGVO
- konkrete Nachverhandlungsklausel
- Anbieterfrage in höflicher, aber unmissverständlicher Sprache

## 3. `mandanten-aufklaerungspflicht-ki`

**Fokus:** Aufklaerungspflicht gegenueber Mandanten beim KI-Einsatz: § 43 BRAO Vertrauensverhaeltnis, § 13 BORA, BGH-Rechtsprechung zur Informationsweitergabe. Mustertexte Mandantenanschreiben und Mandatsvertrag. Pruefraster fuer notwendigen Informationsumfang.

# Mandanten-Aufklaerung KI

## Spezialwissen: Mandanten-Aufklaerung KI
- **Spezialgegenstand:** Mandanten-Aufklaerung KI / mandanten aufklaerungspflicht ki. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, BRAO, BORA, BGH.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Verträge, Auszuege liegen vor?
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
