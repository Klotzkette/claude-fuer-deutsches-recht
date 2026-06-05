---
name: entscheidungsbaum-gesamt-owi-verfahren
description: "Entscheidungsbaum Gesamt OWI Verfahren: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Entscheidungsbaum Gesamt OWI Verfahren

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Entscheidungsbaum Gesamt OWI Verfahren** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `entscheidungsbaum-ki-vo-gesamt-workflow` | Master-fuer die vollstaendige KI-VO-Pruefung. Fuehrt von Art. 3 KI-System-Definition ueber Anwendungsbereich, Rollen, Art. 6 Abs. 2/Anhang III-Hochrisiko, Rueckausnahme, GPAI/Chatbot-Abgrenzung, Betreiber-Fehlgebrauch, Pflichten, Standards und Output-Dokumentation. Schwerpunkt: allgemeine Chatbots sind nicht automatisch Hochrisiko; Zweckbestimmung und tatsaechlicher Einsatz entscheiden. Output: strukturierter Pruefpfad mit Folge-Skills. |
| `ai-act-owi-verfahren-internal-investigation` | KI-VO-Ordnungswidrigkeiten und interne Untersuchung: Sachverhaltsaufklaerung ohne Selbstbelastungschaos, Legal Privilege/Geschuetztheit, Mitarbeiterinterviews, Datenexport, Behördenschreiben, Remediation und Verteidigungsakte. |
| `zeitlicher-geltungsbereich-uebergangsfristen` | Compliance-Beauftragter oder Unternehmen fragt: Ab wann muessen welche KI-VO-Pflichten eingehalten werden und welche Systeme sind schon heute betroffen? KI-VO Übergangsfristen und Zeitplan nach Art. 113 KI-VO. Prüfraster: Inkrafttreten 1. August 2024, Kapitel I/II und Verbote ab 2. Februar 2025, GPAI/Governance/Sanktionen ab 2. August 2025, allgemeine Anwendung ab 2. August 2026, Art. 6 Abs. 1 samt korrespondierenden Pflichten ab 2. August 2027, Bestandssysteme nach Art. 111. Output: Zeitplan-Tabelle mit Meilenstein-Checkliste und Fristen-Kalender für jede Systemkategorie. |
| `provider-deployer-vertragsmatrix` | Vertragsmatrix Anbieter/Betreiber: Pflichtenverschiebung vermeiden, Art. 25-Re-Provisioning, Art. 26-Betreiberpflichten, Art. 13-Informationen, GPAI-Downstream, Audit, Incident, Haftung und Change Control. |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Entscheidungsbaum Gesamt OWI Verfahren**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `entscheidungsbaum-ki-vo-gesamt-workflow`

**Fokus:** Master-fuer die vollstaendige KI-VO-Pruefung. Fuehrt von Art. 3 KI-System-Definition ueber Anwendungsbereich, Rollen, Art. 6 Abs. 2/Anhang III-Hochrisiko, Rueckausnahme, GPAI/Chatbot-Abgrenzung, Betreiber-Fehlgebrauch, Pflichten, Standards und Output-Dokumentation. Schwerpunkt: allgemeine Chatbots sind nicht automatisch Hochrisiko; Zweckbestimmung und tatsaechlicher Einsatz entscheiden. Output: strukturierter Pruefpfad mit Folge-Skills.

# Master-Workflow: KI-VO-Gesamtprüfung

## Zweck

Dieser Skill ist der zentrale Entscheidungsbaum des KI-VO-Prüfers. Er führt vom ersten Art.-3-Check bis zum dokumentierbaren Endvermerk. Er soll nicht nur klassifizieren, sondern den Prüfpfad so steuern, dass Zweckbestimmung, tatsächliche Nutzung und Off-label-Risiken sauber sichtbar werden.

## Grundsatz

Nicht der Produktname entscheidet, sondern der geprüfte Funktionszuschnitt und die Zweckbestimmung. Ein allgemeiner Chatbot oder ein GPAI-System ist nicht automatisch Hochrisiko. Wird er aber für Bewerberbewertung, Beschäftigtenmanagement, Kreditwürdigkeit, Bildung, Justiz, Migration, Strafverfolgung, Notfalltriage oder andere Anhang-III-Zwecke bestimmt oder faktisch eingesetzt, muss Art. 6 Abs. 2 i.V.m. Anhang III vertieft geprüft werden.

## Schritt 0 — Intake

Starte bei unklarer Lage mit `triage-ki-vo-vorpruefung` oder `ki-vo-ai-act-pruefer-allgemein`.

Mindestfragen:
1. Was genau ist das System oder die Komponente?
2. Wer ist Anbieter, Betreiber oder sonstiger Akteur?
3. Wofür ist das System bestimmt?
4. Wie wird es tatsächlich genutzt?
5. Sind natürliche Personen, kritische Infrastruktur oder öffentliche Aufgaben betroffen?
6. Soll ein Vermerk, Memo, Checkliste oder Maßnahmenplan entstehen?

## Schritt 1 — KI-System nach Art. 3 Nr. 1

Skill: `liegt-ki-system-vor-art-3-nr-1`

Prüfe:
- Maschinenbasiert
- Autonomiegrad ohne Überhöhung
- Adaptivität als optionales Indiz
- explizite/implizite Ziele
- Inferenz aus Eingaben
- Output-Typ
- Einfluss auf physische oder virtuelle Umgebung

Wenn Grenzfall: `abgrenzung-konventionelle-software-vs-ki-system`.

## Schritt 2 — Anwendungsbereich

Skills:
- `territorialer-anwendungsbereich-art-2`
- `sachlicher-ausschluss-art-2-abs-3-bis-12`

Prüfe EU-Bezug, Ausgaben in der EU, Inverkehrbringen, Betrieb und sachliche Ausnahmen.

## Schritt 3 — Rollen

Skills:
- `persoenlicher-anwendungsbereich-rollen-art-3`
- `rolle-anbieter-pruefen-art-3-nr-3`
- `rolle-betreiber-pruefen-art-3-nr-4`
- bei Zweckänderung: `anbieter-werden-art-25`

Besonders prüfen:
- Wer bestimmt den Zweck?
- Wer nimmt das System in eigener Verantwortung in Betrieb?
- Ändert ein Betreiber Zweck oder System wesentlich?
- Gibt es mehrere Rollen nebeneinander?

## Schritt 4 — Verbote kurz screenen

Skill: `verbotene-praktiken-art-5`

Nur wenn Treffer möglich, vertiefen. Der Fokus dieses Workflows liegt danach auf Art. 6 Abs. 2/Anhang III.

## Schritt 5 — Hochrisiko Pfad 1

Skill: `hochrisiko-art-6-abs-1-sicherheitsbauteil`

Prüfe Sicherheitsbauteil/Produkt, Anhang-I-Sektorrecht und Dritt-Konformitätsbewertung.

## Schritt 6 — Hochrisiko Pfad 2: Art. 6 Abs. 2 i.V.m. Anhang III

Skill: `hochrisiko-art-6-abs-2-anhang-iii`

Pflichtfragen:
- In welchem Anhang-III-Bereich wird das System eingesetzt?
- Geht es um Bewertung, Zugang, Ranking, Entscheidung, Priorisierung, Risiko, Rechtsanwendung oder Überwachung?
- Ist der Einsatz ausdrücklich intendiert, technisch angelegt, organisatorisch geduldet oder nur theoretisch möglich?
- Ist ein allgemeiner Chatbot/GPAI-System nur Hilfsmittel oder in einen sensiblen Entscheidungsprozess eingebettet?
- Wie werden Mitarbeitenden-Fehlgebrauch und Zweckabweichung verhindert?

## Schritt 7 — Rückausnahme Art. 6 Abs. 3

Skill: `rueckausnahme-art-6-abs-3`

Prüfe eng:
- Profiling natürlicher Personen sperrt die Rückausnahme.
- Kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte.
- Eine der vier Fallgruppen liegt wirklich vor.
- Dokumentation nach Art. 6 Abs. 4.

## Schritt 8 — GPAI und Chatbot

Skills:
- `gpai-vorliegen-art-3-nr-63`
- `gpai-modelle-art-51-bis-55`
- `gpai-systemisches-risiko-schwelle-10e25-flop`
- `begrenztes-risiko-art-50-transparenzpflichten`

Leitsatz:
- Allgemeiner Chatbot: typischerweise Art. 50/GPAI prüfen, nicht automatisch Hochrisiko.
- Konkreter Fachin Anhang III: Hochrisiko-Prüfung aktivieren.

## Schritt 9 — Pflichten und Standards

Bei Hochrisiko:
- `hochrisiko-bestaetigt-end-to-end-roadmap`
- Art. 9 bis 15 Skills
- `hochrisiko-konformitaetsbewertung-art-43-bis-49`
- `eu-datenbank-registrierung-art-49-und-71`

Bei Betreiber:
- `betreiber-deployer-pflichten-art-26`
- `output-betreiber-checkliste-und-folgenabschaetzung`

Bei Standards:
- `code-of-practice-und-harmonisierte-normen`

## Schritt 10 — Prüfdokument

Skill: `output-pruefdokument-ki-vo-mit-warnhinweisen`

Das Enddokument muss enthalten:
- KI-System-Einordnung nach Art. 3
- Zweckbestimmung und tatsächliche Nutzung
- GPAI/Chatbot-Abgrenzung
- Anhang-III-Matrix
- Art. 6 Abs. 3-Bewertung
- Rollen und Pflichten
- Off-label-/Mitarbeitenden-Nutzungsplan
- Standards-/Normenhinweis
- offene Tatsachen und Re-Evaluation-Trigger

## Kompakter Routing-Plan

```text
1. triage-ki-vo-vorpruefung / allgemein
2. liegt-ki-system-vor-art-3-nr-1
3. territorialer-anwendungsbereich-art-2
4. persoenlicher-anwendungsbereich-rollen-art-3
5. risikoklassen-uebersicht-und-triage
6. hochrisiko-art-6-abs-2-anhang-iii (wenn Zwecknaehe)
7. rueckausnahme-art-6-abs-3 (bei Anhang-III-Treffer)
8. gpai-vorliegen-art-3-nr-63 / begrenztes-risiko-art-50-transparenzpflichten (bei Chatbot/GPAI)
9. betreiber-deployer-pflichten-art-26 / anbieter-werden-art-25 (bei Zweckabweichung)
10. output-pruefdokument-ki-vo-mit-warnhinweisen
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 2, 3, 5, 6, 25, 26, 27, 40, 50, 51 bis 56 und Anhang III KI-VO. Keine Rechtsberatung.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `ai-act-owi-verfahren-internal-investigation`

**Fokus:** KI-VO-Ordnungswidrigkeiten und interne Untersuchung: Sachverhaltsaufklaerung ohne Selbstbelastungschaos, Legal Privilege/Geschuetztheit, Mitarbeiterinterviews, Datenexport, Behördenschreiben, Remediation und Verteidigungsakte.

# KI-VO-OWi und interne Untersuchung

## Ausgangslage

Bei KI-VO-Risiken braucht das Unternehmen schnell Tatsachen. Gleichzeitig kann eine schlecht geführte interne Untersuchung die spätere Verteidigung erschweren.

## Untersuchungsplan

1. Mandat und Zweck definieren: Compliance-Klärung, Behördenantwort, Verteidigung, Remediation.
2. Daten sichern: Logs, Prompts, Modellkarten, Freigaben, Tickets, Verträge, Trainingsdatenhinweise.
3. Interviewplan: wer weiß was, wer ist potenziell betroffen, wer darf teilnehmen?
4. Rechte und Pflichten erklären: keine falschen Zusagen, Datenschutz, Arbeitsrecht, Geheimhaltung.
5. Ergebnisse trennen: Tatsachenbericht, rechtliche Bewertung, Abhilfeplan.
6. Behördenstrategie festlegen: kooperieren, begrenzen, Akteneinsicht, Fristen.

## Risiko der Untersuchung

- zu breiter Datenzugriff;
- unklare Interviewbelehrung;
- ungeprüfte technische Aussagen;
- Dokumente mit voreiligen Schuldeingeständnissen;
- Vermischung von Legal Advice und Business-Kommunikation.

## Output

- Investigation Charter.
- Dokumentenanforderungsliste.
- Interviewleitfaden.
- Behördenantwort-Entwurf.
- Remediation-Tracker.

## Grundsatz

Erst Tatsachen sichern, dann rechtlich einordnen. Nicht umgekehrt eine schöne Geschichte schreiben und danach Belege suchen.

## 3. `zeitlicher-geltungsbereich-uebergangsfristen`

**Fokus:** Compliance-Beauftragter oder Unternehmen fragt: Ab wann muessen welche KI-VO-Pflichten eingehalten werden und welche Systeme sind schon heute betroffen? KI-VO Übergangsfristen und Zeitplan nach Art. 113 KI-VO. Prüfraster: Inkrafttreten 1. August 2024, Kapitel I/II und Verbote ab 2. Februar 2025, GPAI/Governance/Sanktionen ab 2. August 2025, allgemeine Anwendung ab 2. August 2026, Art. 6 Abs. 1 samt korrespondierenden Pflichten ab 2. August 2027, Bestandssysteme nach Art. 111. Output: Zeitplan-Tabelle mit Meilenstein-Checkliste und Fristen-Kalender für jede Systemkategorie.

# Zeitlicher Geltungsbereich und Übergangsfristen — KI-VO

## Zweck

Die KI-VO ist nicht sofort und vollständig anwendbar. Sie trat zwar am 1. August 2024 in Kraft, ihre einzelnen Kapitel und Vorschriften werden jedoch schrittweise verbindlich. Dieser Skill gibt einen vollständigen Überblick über die Fristen und hilft dem Nutzer, seinen aktuellen Compliance-Handlungsbedarf einzuordnen.

## Zeitstrahl

### 1. August 2024 — Inkrafttreten

Die KI-VO ist am 1. August 2024 in Kraft getreten (20 Tage nach Veröffentlichung im Amtsblatt der EU am 12. Juli 2024).

Noch nicht anwendbar: Die meisten inhaltlichen Pflichten. Es gelten ab diesem Zeitpunkt:
- Beginn der institutionellen Aufbauphase (Europäisches KI-Büro, Art. 64 KI-VO)
- Beginn der Normungsarbeit durch CEN/CENELEC

### 2. Februar 2025 — Verbotene Praktiken (Art. 5 KI-VO)

Ab dem 2. Februar 2025 sind verbotene KI-Praktiken nach Art. 5 KI-VO verboten und strafbewehrt. Unternehmen, die KI-Systeme mit den verbotenen Eigenschaften einsetzen, müssen diese bis zu diesem Datum abschalten oder umgestalten.

**Praxisrelevanz:** Systeme zur biometrischen Echtzeitidentifikation im öffentlichen Raum, Social-Scoring-Systeme und Systeme zur Manipulation von Verhalten müssen sofort überprüft werden.

Ebenfalls ab 2. Februar 2025 anwendbar:
- Kapitel I (allgemeine Bestimmungen, insbesondere Begriffe wie KI-System, Anbieter, Betreiber, GPAI)
- Kapitel II (verbotene Praktiken)

**Wichtig:** Art. 6 KI-VO ist nicht bereits als eigene Hochrisiko-Pflichtenmechanik seit Februar 2025 voll anwendbar. Die Klassifikation wird zwar praktisch vorlaufend gebraucht, die Verbindlichkeit folgt aber dem Stufenplan in Art. 113 KI-VO.

### 2. August 2025 — GPAI-Modelle

Ab dem 2. August 2025 gelten die Pflichten für Anbieter von GPAI-Modellen (Art. 51 bis 55 KI-VO sowie Kapitel V KI-VO vollständig).

**Praxisrelevanz:** Anbieter von General-Purpose-KI-Modellen müssen bis dahin technische Dokumentation nach Anhang XI, Urheberrechts-Compliance-Strategie und gegebenenfalls Meldung des systemischen Risikos implementiert haben.

Ebenfalls ab 2. August 2025:
- Kapitel III (Abschnitt 4 — Benannte Stellen) für Hochrisiko
- Kapitel III (Abschnitt 5 — CE-Kennzeichnung)
- Art. 78 KI-VO (Vertraulichkeit)
- Art. 99 und 100 KI-VO (Sanktionen)

### 2. August 2026 — Allgemeine Anwendung und Hochrisiko-KI nach Anhang III

Ab dem 2. August 2026 gilt die KI-VO grundsätzlich. Damit werden insbesondere die Hochrisiko-Pflichten für Systeme nach Art. 6 Abs. 2 i.V.m. Anhang III praktisch scharf, soweit keine Sonderregel oder Bestandssystemregel greift.

**Praxisrelevanz:** Anbieter von Hochrisiko-KI-Systemen müssen bis dahin:
- Risikomanagementsystem (Art. 9 KI-VO) implementiert haben
- Technische Dokumentation nach Anhang IV erstellt haben
- Konformitätsbewertung durchgeführt haben (Art. 43 bis 49 KI-VO)
- CE-Kennzeichnung angebracht haben
- In der EU-Datenbank registriert sein (Art. 71 KI-VO)

### 2. August 2027 — Art. 6 Abs. 1 und Produkt-Sicherheitskomponenten

Art. 6 Abs. 1 und die korrespondierenden Pflichten gelten nach Art. 113 KI-VO ab dem 2. August 2027. Das betrifft den Pfad über KI als Sicherheitsbauteil oder selbst reguliertes Produkt im Zusammenspiel mit Anhang I.

## Relevanz für bestehende Systeme

Systeme, die vor dem jeweiligen Anwendungsdatum bereits in Verkehr gebracht wurden, können von Bestandsschutz profitieren — aber nur bis zu wesentlichen Änderungen. Eine wesentliche Änderung löst erneute Konformitätsbewertungspflichten aus.

## Aktueller Handlungsbedarf (Stand: 06/2026)

- **Verbote Art. 5:** Seit 02.02.2025 vollständig verbindlich; bei Bestandssystemen sofortige Abschaltungs- oder Umgestaltungspflicht.
- **GPAI-Pflichten Art. 51-55:** Seit 02.08.2025 vollständig verbindlich; technische Dokumentation (Anhang XI), Informationen fuer nachgelagerte Anbieter, Urheberrechts-Compliance-Strategie und Trainingsdaten-Zusammenfassung im Kommissions-Format Pflicht.
- **Hochrisiko Anhang III:** Ab 02.08.2026 im Grundsatz verbindlich. **Jetzt zeitkritisch** — Konformitaetsbewertung, technische Dokumentation und EU-Datenbank-Registrierung muessen vorbereitet sein; bei Bestands- und Public-Sector-Faellen Art. 111 KI-VO gesondert pruefen.
- **Hochrisiko Anhang I / Art. 6 Abs. 1 (KI als Sicherheitskomponente oder reguliertes Produkt):** Art. 6 Abs. 1 und die korrespondierenden Pflichten gelten nach Art. 113 ab 02.08.2027.
- **Bestandssysteme und oeffentliche Hand:** Art. 111 KI-VO enthaelt Sonderregeln, insbesondere fuer vor dem 02.08.2026 platzierte oder in Betrieb genommene Hochrisiko-Systeme und Hochrisiko-Systeme fuer oeffentliche Stellen. Diese Regeln nie uebersehen.
- **GPAI mit systemischem Risiko (>= 10^25 FLOPs Trainings-Compute, Art. 51 KI-VO):** Modellbewertungen, adversarial testing, Risikominderung und Cybersicherheits-Mass­nahmen seit 02.08.2025 Pflicht. Quelle: VO 2024/1689 Art. 55; Konkretisierung durch GPAI Code of Practice.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Faktische Updates (Stand 06/2026)

- **02.08.2025 — GPAI-Pflichten in Kraft:** Anbieter von General-Purpose-KI-Modellen (Art. 51 ff. KI-VO) muessen seit dem 02.08.2025 technische Dokumentation nach Anhang XI sowie eine Zusammenfassung der Trainingsdaten in dem von der Kommission bereitgestellten Template veroeffentlichen (Art. 53 Abs. 1 lit. d KI-VO). Quelle: VO (EU) 2024/1689, eur-lex.europa.eu/eli/reg/2024/1689/oj.
- **GPAI Code of Practice:** Die Kommission und das EU-AI-Office foerdern einen Code of Practice fuer GPAI-Modellanbieter; bei freiwilligem Anschluss sollen Anbieter als pflichtkonform vermutet werden (Art. 56 KI-VO). Quelle live pruefen ueber digital-strategy.ec.europa.eu sowie das EU AI Office.
- **02.08.2026 — allgemeiner Anwendungsbeginn / Hochrisiko Anhang III:** Anbieter- und Betreiberpflichten fuer Hochrisiko-Systeme nach Anhang III werden im Grundsatz relevant: Risikomanagement (Art. 9), Datenqualitaet (Art. 10), technische Dokumentation (Art. 11 i.V.m. Anhang IV), Logging (Art. 12), Transparenz (Art. 13), menschliche Aufsicht (Art. 14), Genauigkeit/Robustheit/Cybersicherheit (Art. 15), Konformitaetsbewertung (Art. 43-49), CE-Kennzeichnung (Art. 48), EU-Datenbank-Registrierung (Art. 71). Achtung: Konkretisierung durch Durchfuehrungsrechtsakte und harmonisierte Normen laufend; vor Ausgabe Stand pruefen.
- **02.08.2027 — Art. 6 Abs. 1 / Anhang I-Pfad:** Art. 6 Abs. 1 und korrespondierende Pflichten gelten erst ab diesem Datum. Nicht mit dem Anhang-III-Pfad vermischen.
- **Sanktionen Art. 99 KI-VO:** ab 02.08.2025 vollumfaenglich anwendbar — bis 35 Mio. EUR / 7 % weltweiter Jahresumsatz bei Verstoss gegen Art. 5; bis 15 Mio. EUR / 3 % bei Hochrisiko- oder GPAI-Pflichtverletzungen; bis 7.5 Mio. EUR / 1 % bei Falschangaben gegenueber Behoerden.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (curia.europa.eu) verifizieren.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 51-55 KI-VO — GPAI-Modelle (ab 02.08.2025)
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz
- Art. 113 KI-VO — Inkrafttreten und Stufenplan

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
PRUEFERGEBNIS — ZEITLICHER GELTUNGSBEREICH UEBERGANGSFRISTEN
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 113 Rn. 3]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 4. `provider-deployer-vertragsmatrix`

**Fokus:** Vertragsmatrix Anbieter/Betreiber: Pflichtenverschiebung vermeiden, Art. 25-Re-Provisioning, Art. 26-Betreiberpflichten, Art. 13-Informationen, GPAI-Downstream, Audit, Incident, Haftung und Change Control.

# Anbieter-Betreiber-Vertragsmatrix

## Problem

KI-Verträge scheitern oft daran, dass technische und regulatorische Verantwortung unklar verteilt ist. Dieser Skill baut eine Matrix, die KI-VO-Rollen und Vertragsklauseln zusammenführt.

## Matrixfelder

| Thema | Anbieter | Betreiber | Vertrag |
|---|---|---|---|
| Zweckbestimmung | definiert und dokumentiert | hält Einsatz daran | Use Case Schedule |
| Hochrisiko | Konformität, Dokumentation | Betreiberpflichten | AI Act Annex |
| Human Oversight | Funktionen bereitstellen | Menschen schulen | RACI |
| Logs | technische Aufzeichnung | Auswertung/Retention | Logging Annex |
| Incident | Mitteilung, Abhilfe | Meldung/Koordination | Incident Clause |
| Modelländerung | Change Notice | Re-Evaluation | Change Control |
| GPAI | Downstream-Infos | Weitergabe in Systemakte | Model Info Annex |

## Red Flags

- Anbieter lehnt jede KI-VO-Aussage ab.
- Betreiber darf Zweck massiv ändern.
- Kein Zugriff auf Modell- oder Versionsinformationen.
- Keine Incident-Fristen.
- Unklare Haftung bei Outputfehlern.

## Output

Vertragsredlines und eine Verantwortlichkeitsmatrix.
