---
name: hochrisiko-bestaetigt-end-to-end-roadmap
description: "Anbieter hat Hochrisiko-Einstufung des eigenen KI-Systems bestätigt und fragt: Was sind jetzt alle noetigen Schritte bis zur CE-Kennzeichnung und Marktfreigabe? End-to-End-Roadmap Hochrisiko-KI Art. 9 bis 49 KI-VO. Prüfraster: zwoelf Schritte Risikomanagementsystem Art. 9 Datenqualitaet Art. 10 t"
---

# Hochrisiko-KI bestätigt — die End-to-End-Roadmap

## Arbeitsbereich

Anbieter hat Hochrisiko-Einstufung des eigenen KI-Systems bestätigt und fragt: Was sind jetzt alle noetigen Schritte bis zur CE-Kennzeichnung und Marktfreigabe? End-to-End-Roadmap Hochrisiko-KI Art. 9 bis 49 KI-VO. Prüfraster: zwoelf Schritte Risikomanagementsystem Art. 9 Datenqualitaet Art. 10 technische Dokumentation Art. 11 Logging Art. 12 Transparenz Art. 13 menschliche Aufsicht Art. 14 Genauigkeit Art. 15 Konformitätsbewertung Art. 43 CE-Kennzeichnung Art. 47 EU-Datenbank Art. 49 Marktbeobachtung. Output: Projektplan mit Aufwandsschaetzung Akteuren und Fristen. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Art. 5 Verbote ab 02.02.2025, Art. 51-55 GPAI ab 02.08.2025, Hochrisiko Anhang III ab 02.08.2026, Hochrisiko Anhang I ab 02.08.2027, schwerwiegender Vorfall 15 Tage / 2 Tage (Tod).
- Tragende Normen verifizieren: KI-VO (EU 2024/1689) Art. 3, 5 (Verbote), 6 (Hochrisiko), 8-15 (Anforderungen), 16, 26 (Pflichten Anbieter/Betreiber), 50 (Transparenz), 51-55 (GPAI), 73, 99 (Sanktionen) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Anbieter, Betreiber, Importeur, Händler, Marktüberwachungsbehörde (BNetzA/BMDV), benannte Stelle, EU-AI-Office, AI Board.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Konformitätserklärung Art. 47, technische Dokumentation Anhang IV, Risikomanagement-System Art. 9, Datengovernance Art. 10, FRIA (Fundamental Rights Impact Assessment) Art. 27, EU-Datenbank-Registrierung Art. 49 — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Sie haben festgestellt: das System ist Hochrisiko nach Art. 6 Abs. 1 oder Abs. 2 i.V.m. Anhang I/III KI-VO. Die Rückausnahme nach Art. 6 Abs. 3 KI-VO greift nicht. **Was jetzt?**

Liefert den vollständigen Mandanten-von "Hochrisiko-Diagnose" bis "Marktreife mit CE-Kennzeichnung". Ziel ist Entdramatisierung: jeder Schritt ist mechanisch abarbeitbar.

---

## PFLICHT-DISCLAIMER

**Keine Rechtsberatung. Mechanischer Workflow.** Die konkrete Umsetzung erfordert produkt-/branchen-spezifische Detailprüfung durch Fachpersonal (interne Compliance, externe Beratung, Konformitätsbewertungsstelle).

---

## Vorbedingung — wer macht was?

| Akteur | Hauptpflichten | Roadmap relevant? |
|---|---|---|
| **Anbieter** (Art. 3 Nr. 3) | Art. 9-15, 16-21, 43-49 KI-VO | Alle 12 Schritte |
| **Betreiber** (Art. 3 Nr. 4) | Art. 26-27 KI-VO | Schritt 11-12 + Folgenabschätzung |
| **Einführer** (Art. 3 Nr. 6) | Art. 23 KI-VO | Schritt 7-9 (Verifikation) |
| **Händler** (Art. 3 Nr. 7) | Art. 24 KI-VO | Schritt 10 (Verifikation vor Vertrieb) |
| **Bevollmächtigter** (Art. 3 Nr. 5) | Art. 22 KI-VO | Schritt 1-12 stellvertretend |

→ Rollenzuordnung vorher klären über `rolle-anbieter-pruefen-art-3-nr-3` bzw. `rolle-betreiber-pruefen-art-3-nr-4`.

---

## Die zwölf Schritte für Anbieter

### Schritt 1 — Risikomanagementsystem aufsetzen (Art. 9 KI-VO)

**Was:** kontinuierlicher iterativer Prozess über den gesamten Lebenszyklus.

**Mindestelemente:**
- Identifikation und Analyse bekannter und vernünftig vorhersehbarer Risiken
- Abschätzung möglicher Risiken bei bestimmungsgemäßer Verwendung und bei vernünftigerweise vorhersehbarer Fehlanwendung
- Bewertung anderer Risiken aus Post-Market-Daten
- geeignete und gezielte Risikomanagementmaßnahmen

**Output:** dokumentiertes RMS, Eingang in technische Dokumentation Anhang IV.

→ Detail-Skill: `hochrisiko-risikomanagementsystem-art-9`

---

### Schritt 2 — Daten-Governance und Trainingsdaten-Qualität (Art. 10 KI-VO)

**Was:** Trainings-, Validierungs- und Testdaten müssen Qualitätskriterien erfüllen.

**Mindestelemente:**
- Datenerhebungsverfahren dokumentiert
- relevante Datenaufbereitung (Annotation, Labelling, Bereinigung, Aktualisierung, Anreicherung, Aggregation)
- Untersuchung auf mögliche Verzerrungen, die zu Diskriminierung führen
- Datensätze relevant, hinreichend repräsentativ, fehlerfrei, vollständig
- Berücksichtigung geographischer, kontextueller, verhaltensbezogener und funktionaler Besonderheiten

**Output:** Daten-Governance-Dokumentation, Bias-Bewertung.

→ Detail-Skill: `hochrisiko-datenqualitaet-und-data-governance-art-10`

---

### Schritt 3 — Technische Dokumentation erstellen (Art. 11, Anhang IV KI-VO)

**Was:** vor Inverkehrbringen vollständig erstellt, aktuell gehalten.

**Inhalte (Anhang IV) — neun Hauptblöcke:**
1. Allgemeine Beschreibung des KI-Systems
2. Detaillierte Beschreibung der Elemente und Entwicklung
3. Detaillierte Informationen zur Überwachung, Funktionsweise und Kontrolle
4. Beschreibung der Eignung der Leistungskennzahlen
5. Detaillierte Beschreibung des Risikomanagementsystems
6. Beschreibung relevanter Änderungen
7. Liste der harmonisierten Normen
8. EU-Konformitätserklärung-Kopie
9. Detaillierte Beschreibung des Systems zur Bewertung der Leistung nach Inverkehrbringen

**Output:** Anhang-IV-Doku, mindestens zehn Jahre aufbewahren.

→ Detail-Skill: `hochrisiko-technische-dokumentation-art-11-und-anhang-iv`

---

### Schritt 4 — Aufzeichnungspflichten / Logging einrichten (Art. 12 KI-VO)

**Was:** automatische Aufzeichnung von Ereignissen während des Betriebs.

**Mindest-Loggings:**
- Zeitpunkt der Verwendung
- Referenzdatenbank, gegen die Input-Daten geprüft
- Input-Daten, die zu einem Treffer führten
- Identifizierung beteiligter natürlicher Personen bei Ergebnisverifikation

**Aufbewahrung:** angemessene Dauer, mindestens sechs Monate, sofern Unionsrecht oder nationales Recht nicht längere Dauer vorschreibt.

→ Detail-Skill: `hochrisiko-aufzeichnungspflichten-logging-art-12`

---

### Schritt 5 — Transparenz und Informationen für Betreiber (Art. 13 KI-VO)

**Was:** Gebrauchsanweisung mit präzisen, vollständigen, korrekten Informationen.

**Pflichtinhalte:**
- Identität und Kontaktdaten des Anbieters
- Merkmale, Fähigkeiten und Leistungsgrenzen
- ggf. bekannte oder vernünftig vorhersehbare Umstände, die zu Risiken führen können
- ggf. technische Fähigkeiten und Kennwerte
- Leistung in Bezug auf spezifische Personen oder Personengruppen
- Anforderungen an Eingabedaten
- ggf. Informationen zur Datenverarbeitung durch das System

→ Detail-Skill: `hochrisiko-transparenz-und-informationen-für-betreiber-art-13`

---

### Schritt 6 — Menschliche Aufsicht ermöglichen (Art. 14 KI-VO)

**Was:** Hochrisiko-KI muss so konzipiert sein, dass natürliche Personen wirksam beaufsichtigen können.

**Befähigungen, die der Mensch haben muss:**
- die Fähigkeiten und Grenzen des Systems vollständig verstehen
- die Tendenz zum Automatisierungsbias kennen und einkalkulieren
- die Ausgaben des Systems korrekt interpretieren
- die Verwendung des Systems ablehnen, dessen Verwendung übergehen, rückgängig machen
- in den Betrieb eingreifen oder den Betrieb durch Stopp-Taste unterbrechen

**Bei biometrischer Fernidentifizierung:** Vier-Augen-Prinzip nach Art. 14 Abs. 5 KI-VO.

→ Detail-Skill: `hochrisiko-menschliche-aufsicht-art-14`

---

### Schritt 7 — Genauigkeit, Robustheit, Cybersicherheit (Art. 15 KI-VO)

**Was:** angemessene Genauigkeit, Robustheit und Cybersicherheit über den gesamten Lebenszyklus.

**Pflichten:**
- Genauigkeitsgrade und einschlägige Genauigkeitsmetriken in Gebrauchsanweisung
- Robustheit gegen Fehler, Störungen, Inkonsistenzen
- Resilienz gegen Versuche unberechtigter Dritter, Verwendung zu ändern (z.B. durch Ausnutzung von Schwachstellen)
- bei lernfähigen Systemen: Schutz gegen verzerrte Ausgaben (Feedback Loops) durch geeignete Maßnahmen
- Anfälligkeit gegen "Data Poisoning", "Model Poisoning", "Model Evasion", "Adversarial Examples", "Confidentiality Attacks" adressieren

→ Detail-Skill: `hochrisiko-genauigkeit-robustheit-cybersicherheit-art-15`

---

### Schritt 8 — Qualitätsmanagementsystem (Art. 17 KI-VO)

**Was:** dokumentiertes QMS mit schriftlichen Vorschriften, Verfahren und Anweisungen.

**Mindestelemente (Art. 17 Abs. 1 KI-VO):**
- Strategie für die Einhaltung der Regulierung einschließlich Konformitätsbewertungsverfahren
- Verfahren für Design, Designkontrolle und Designverifikation
- Verfahren für Entwicklung, Qualitätskontrolle und Qualitätssicherung
- Untersuchung, Test- und Validierungsverfahren vor, während und nach Entwicklung
- anwendbare technische Spezifikationen einschließlich Normen
- Systeme und Verfahren für Datenverwaltung
- Risikomanagementsystem nach Art. 9
- Aufstellung und Umsetzung Post-Market-Monitoring-System nach Art. 72
- Meldeverfahren für schwerwiegende Vorfälle nach Art. 73
- Kommunikation mit zuständigen Behörden, notifizierten Stellen, Kunden
- Aufzeichnungssysteme und -verfahren
- Ressourcenmanagement einschließlich Versorgungssicherheit
- Rechenschaftsrahmen mit klaren Verantwortlichkeiten

---

### Schritt 9 — Konformitätsbewertungsverfahren wählen (Art. 43 KI-VO)

**Was:** Vor Inverkehrbringen / Inbetriebnahme nachweisen, dass alle Anforderungen aus Art. 8-15 KI-VO erfüllt sind.

**Verfahrenswahl je nach Systemart:**

| Konstellation | Verfahren | Notifizierte Stelle? |
|---|---|---|
| Anhang-III-Hochrisiko (außer biometrisch) | Anhang VI — interne Kontrolle | nein |
| Anhang-III-Bereich 1 (biometrische Identifizierung) ohne anwendbare Norm | Anhang VII — Bewertung durch notifizierte Stelle | ja |
| Anhang-III-Bereich 1 mit anwendbarer Norm vollständig befolgt | Anhang VI — interne Kontrolle | nein, aber Norm verbindlich |
| Anhang-I-Hochrisiko (Sicherheitsbauteil) | Verfahren des einschlägigen Sektor-Rechtsakts (z.B. Medizinprodukte: MDR-Verfahren mit KI-VO-Integration) | nach Sektor-Recht |

**Output:** EU-Konformitätserklärung nach Anhang V.

→ Detail-Skills: `hochrisiko-konformitaetsbewertung-art-43-bis-49`, `output-konformitaetserklaerung-eu-anhang-v`, `output-konformitaetsbescheinigung-evidence-pack`, `code-of-practice-und-harmonisierte-normen`

---

### Schritt 10 — CE-Kennzeichnung anbringen (Art. 48 KI-VO)

**Was:** sichtbar, leserlich, dauerhaft.

**Erforderlich:**
- digitale CE-Kennzeichnung möglich, wenn nicht über physisches Produkt zugänglich
- Identifikationsnummer der notifizierten Stelle hinzufügen, wenn an Konformitätsbewertung beteiligt
- in Gebrauchsanweisung und Begleitdokumentation

---

### Schritt 11 — EU-Datenbank-Registrierung (Art. 49, 71 KI-VO)

**Wer ist registrierungspflichtig?**

| Konstellation | Pflicht zur EU-DB-Registrierung |
|---|---|
| Anbieter Hochrisiko **Anhang III** (außer Strafverfolgung/Migration/Asyl) | ja, Art. 49 Abs. 1 KI-VO |
| Anbieter Hochrisiko **Anhang III** Strafverfolgung/Migration/Asyl | ja, aber gesonderter, nicht öffentlicher Teil der Datenbank (Art. 49 Abs. 4, Art. 71 Abs. 5 KI-VO) |
| Anbieter Hochrisiko **Anhang I** (Sicherheitsbauteile) | **nein** — Konformität läuft über den sektoralen Rechtsakt (z.B. MDR, MaschinenVO); KI-VO-EU-Datenbank greift hier grundsätzlich nicht |
| **Betreiber** als Behörde, EU-Organ oder im Auftrag öffentlicher Stelle | ja, vor Einsatz (Art. 49 Abs. 3 KI-VO) — gilt nur für Anhang-III-Systeme |
| Anbieter, der sich auf Rückausnahme Art. 6 Abs. 3 beruft | gesonderte Registrierung der Selbsteinschätzung (Art. 49 Abs. 2 KI-VO) |

**Faustregel:** Die EU-Datenbank nach Art. 71 KI-VO ist die **Anhang-III-Schiene**. Anbieter von Sicherheitsbauteilen nach Anhang I (MDR-Implantate, IVDR-Diagnostika, MaschinenVO-Komponenten etc.) erfüllen ihre Eintragungspflichten in den sektoralen Registern (EUDAMED, NANDO, etc.) und sind von Art. 49 KI-VO **nicht** erfasst.

**Was wird registriert (Anhang VIII Abschnitt A KI-VO):**
- Identität, Kontaktdaten Anbieter (ggf. Bevollmächtigter)
- Handelsname und etwaige weitere eindeutige Kennung des KI-Systems
- Anhang-III-Bereich
- Status der Konformitätsbewertung
- Kopie der EU-Konformitätserklärung
- elektronische Gebrauchsanweisung (außer Strafverfolgung/Migration/Asyl)
- URL für zusätzliche Informationen

**Wann:** vor Inverkehrbringen / Inbetriebnahme.

→ Detail-Skill: `eu-datenbank-registrierung-art-49-und-71`

---

### Schritt 12 — Marktbeobachtung und Vorfallsmeldung (Art. 72-79 KI-VO)

**Was:** Post-Market-Monitoring-System aktiv betreiben.

**Pflichten:**
- aktive systematische Sammlung relevanter Daten zur Leistung über Lebenszyklus
- Bewertung kontinuierlicher Einhaltung der Anforderungen aus Art. 8-15
- Plan für Post-Market-Monitoring (Anhang VIII)
- Meldung schwerwiegender Vorfälle binnen fünfzehn Tagen an Marktaufsichtsbehörde (Art. 73)
- bei Tod: binnen zehn Tagen; bei groß angelegtem Verstoß: binnen zwei Tagen
- Kooperation mit Marktaufsichtsbehörden
- Korrekturmaßnahmen bei Nichtkonformität (Rückruf, Rücknahme, Nachbesserung)

→ Detail-Skill: `marktueberwachung-meldung-vorfaelle-art-72-bis-79`

---

## Ergänzungs-für Betreiber

Wer das System **einsetzt** (Art. 3 Nr. 4 KI-VO), durchläuft einen kürzeren Workflow:

### Betreiber-Schritt 1 — Einsatzbedingungen prüfen (Art. 26 KI-VO)

- Verwendung gemäß Gebrauchsanweisung
- Sicherstellung menschlicher Aufsicht (geschulte, befugte Personen)
- Eingabedaten relevant und hinreichend repräsentativ
- Betriebsüberwachung mit Information des Anbieters bei Auffälligkeiten
- Logging nach Art. 12 für eigene Aufzeichnungen
- Information natürlicher Personen, die Hochrisiko-KI ausgesetzt sind
- bei Beschäftigten: Information vor Inbetriebnahme

### Betreiber-Schritt 2 — Folgenabschätzung Grundrechte (Art. 27 KI-VO)

Pflicht für **öffentliche Stellen** und einige private Betreiber (z.B. Banken bei Kreditwürdigkeit, Versicherer bei Lebens-/Krankenversicherung):

- Beschreibung Prozesse, in denen Hochrisiko-KI eingesetzt wird
- Beschreibung Einsatzzeitraum und -häufigkeit
- Kategorien betroffener Personen
- Risiken für Grundrechte
- Beschreibung Aufsichtsmaßnahmen
- Maßnahmen bei Risikoeintritt

→ Detail-Skill: `output-betreiber-checkliste-und-folgenabschaetzung`

---

## Realistische Aufwands-Einordnung

| Schritt | typischer Zeitaufwand kleine/mittlere Anbieter | typischer Zeitaufwand bei vorhandenem ISO-9001/27001/14971 |
|---|---|---|
| RMS aufsetzen | 4-8 Wochen | 2-4 Wochen |
| Daten-Governance | 6-12 Wochen | 3-6 Wochen |
| Technische Dokumentation | 8-16 Wochen | 4-8 Wochen |
| Logging | 2-4 Wochen | 1-2 Wochen |
| Transparenz/Gebrauchsanweisung | 2-4 Wochen | 1-2 Wochen |
| Menschliche Aufsicht | 2-4 Wochen | 1-2 Wochen |
| Genauigkeit/Robustheit | 6-12 Wochen | 3-6 Wochen |
| QMS | 8-16 Wochen | bereits vorhanden, nur ergänzen |
| Konformitätsbewertung | 4-8 Wochen interne / 12-26 Wochen notifizierte Stelle | wie links |
| CE und EU-DB | 1-2 Wochen | 1 Woche |
| Marktbeobachtung-Setup | 4-8 Wochen | 2-4 Wochen |

**Hinweis:** Übergangsfristen beachten — Hochrisiko Anhang III: ab 2.8.2026 anwendbar; Hochrisiko Anhang I (Sicherheitsbauteile): ab 2.8.2027 anwendbar. → `zeitlicher-geltungsbereich-uebergangsfristen`.

---

## Beteiligte Akteure / Wo melde ich was?

| Akteur | Rolle | Wann kontaktieren? |
|---|---|---|
| **Notifizierte Stelle** | externe Konformitätsbewertung | bei Anhang VII, biometrischer Fernidentifizierung, sektorspezifischen Vorgaben |
| **Nationale Marktaufsichtsbehörde** | Aufsicht, Vorfallsmeldung | bei schwerwiegenden Vorfällen (Art. 73), Anfragen, Inspektionen |
| **Notifizierungsbehörde** | Aufsicht über notifizierte Stellen | indirekt relevant |
| **EU-KI-Büro** (AI Office, Kommission GD CONNECT) | GPAI-Modelle, Code of Practice | wenn auch GPAI-Anbieter |
| **EU-KI-Datenbank** (Art. 71 KI-VO) | Registrierung Hochrisiko-Systeme | vor Inverkehrbringen — Anhang III; bei Anhang I über sektorale Register (EUDAMED, NANDO etc.) |
| **EDPB / nationale DSchB** | DSGVO-Schnittstelle | bei personenbezogenen Daten |
| **Sektor-Regulatoren** (BaFin, BNetzA, BfArM, ...) | sektorale Aufsicht | je nach Anwendungsbereich |

---

## Mini-Checkliste vor Markteintritt

- [ ] Risikomanagementsystem dokumentiert und auf aktuellem Stand
- [ ] Daten-Governance abgeschlossen, Bias-Bewertung vorhanden
- [ ] Technische Dokumentation Anhang IV vollständig
- [ ] Logging aktiv, Speicherdauer eingestellt
- [ ] Gebrauchsanweisung vollständig nach Art. 13
- [ ] Menschliche Aufsicht implementiert und beschrieben
- [ ] Genauigkeitsmetriken dokumentiert, Robustheitstests durchgeführt
- [ ] Cybersicherheitskonzept vorhanden
- [ ] QMS aufgesetzt und dokumentiert
- [ ] Konformitätsbewertungsverfahren durchlaufen
- [ ] EU-Konformitätserklärung Anhang V erstellt
- [ ] CE-Kennzeichnung angebracht
- [ ] EU-Datenbank-Registrierung erfolgt (nur Anhang III; bei Anhang I über sektoralen Rechtsakt)
- [ ] Post-Market-Monitoring-Plan aktiv
- [ ] Vorfalls-Meldesystem etabliert
- [ ] interne Verantwortlichkeiten zugewiesen
- [ ] Mitarbeiter geschult (KI-Kompetenz Art. 4 KI-VO)

→ Output-Skill: `output-pruefdokument-ki-vo-mit-warnhinweisen`

---

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 3 Nr. 3/4 KI-VO — Anbieter / Betreiber-Definition
- Art. 5 KI-VO — verbotene Praktiken (absolut ab 02.02.2025)
- Art. 6 i.V.m. Anhang III KI-VO — Hochrisiko-Klassifikation
- Art. 26 KI-VO — Betreiberpflichten
- Art. 99 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % Jahresumsatz

## Triage zu Beginn
1. Welche Rolle hat das Unternehmen im KI-Lieferkette (Art. 3 KI-VO — Anbieter, Betreiber, Importeur)?
2. Liegt ein Hochrisiko-System vor (Art. 6 i.V.m. Anhang III Nr. 1-8 KI-VO)?
3. Sind verbotene Praktiken nach Art. 5 KI-VO ausgeschlossen?
4. Welche konkreten Pflichten aus dem aktuellen Skill-Kontext sind einschlaegig?
5. Ist die Maßnahme fristgerecht umgesetzt (KI-VO Stufenplan bis 02.08.2026)?

## Output-Template — Prüfergebnis
**Adressat:** Prüfer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — HOCHRISIKO BESTAETIGT END TO END ROADMAP
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 9 Rn. 1]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
