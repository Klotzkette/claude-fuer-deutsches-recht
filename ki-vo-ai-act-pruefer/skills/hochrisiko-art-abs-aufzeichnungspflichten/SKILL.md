---
name: hochrisiko-art-abs-aufzeichnungspflichten
description: "Hochrisiko ART ABS Aufzeichnungspflichten: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Hochrisiko ART ABS Aufzeichnungspflichten

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Hochrisiko ART ABS Aufzeichnungspflichten** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hochrisiko-art-6-abs-2-anhang-iii` | Vertiefter Hochrisiko-Checker fuer Art. 6 Abs. 2 i.V.m. Anhang III KI-VO. Prueft alle acht Anhang-III-Bereiche mit Untertatbestaenden, Zweckbestimmung, konkretem Einsatzkontext, GPAI/Chatbot-Abgrenzung und Mitarbeitenden-Fehlgebrauch. Erklaert, warum ein allgemeiner Chatbot nicht automatisch Hochrisiko ist, aber bei intendiertem Einsatz in Justiz, Personal, Bildung, Kredit, Migration usw. Hochrisiko werden kann. Output: dokumentierte Zuordnungsentscheidung mit Bereichsmatrix, Art. 6 Abs. 3-Routing und Governance-Massnahmen. |
| `hochrisiko-aufzeichnungspflichten-logging-art-12` | Anbieter von Hochrisiko-KI fragt: Was muss unser System automatisch aufzeichnen und wie lange muessen wir die Logs aufbewahren? Art. 12 KI-VO Logging-Pflichten. Prüfraster: Mindestinhalte der Logs Zeitstempel Eingabedaten Ausgaben Fehlermeldungen Aufbewahrungsfrist drei Jahre bzw. Vertragsdauer Verantwortlichkeitsteilung Anbieter vs. Betreiber. Besondere Anforderungen biometrische Identifikation Art. 12 Abs. 3. Output: Logging-Anforderungskatalog und Muster-Log-Schema. Abgrenzung zu hochrisiko-technische-dokumentation-art-11-und-anhang-iv (Dokumentationspflichten) und betreiber-deployer-pflichten-art-26. |
| `hochrisiko-bestaetigt-end-to-end-roadmap` | Anbieter hat Hochrisiko-Einstufung des eigenen KI-Systems bestätigt und fragt: Was sind jetzt alle noetigen Schritte bis zur CE-Kennzeichnung und Marktfreigabe? End-to-End-Roadmap Hochrisiko-KI Art. 9 bis 49 KI-VO. Prüfraster: zwoelf Schritte Risikomanagementsystem Art. 9 Datenqualitaet Art. 10 technische Dokumentation Art. 11 Logging Art. 12 Transparenz Art. 13 menschliche Aufsicht Art. 14 Genauigkeit Art. 15 Konformitätsbewertung Art. 43 CE-Kennzeichnung Art. 47 EU-Datenbank Art. 49 Marktbeobachtung. Output: Projektplan mit Aufwandsschaetzung Akteuren und Fristen. |
| `hochrisiko-datenqualitaet-und-data-governance-art-10` | Anbieter von Hochrisiko-KI fragt: Welche Anforderungen gelten für unsere Trainings- Validierungs- und Testdaten und wie dokumentieren wir unsere Data Governance? Art. 10 KI-VO Datenqualitaet und Data Governance. Prüfraster: Relevanz Repraesentativitaet Vollständigkeit Fehlerfreiheit Bias-Minderung Ausnahme besondere Datenkategorien Art. 10 Abs. 5. Output: Data-Governance-Checkliste und Vorlage Trainingsdaten-Dokumentation. Abgrenzung zu hochrisiko-technische-dokumentation-art-11-und-anhang-iv (Gesamtdokumentation) und hochrisiko-risikomanagementsystem-art-9 (Risikobewertung). |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Hochrisiko ART ABS Aufzeichnungspflichten**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `hochrisiko-art-6-abs-2-anhang-iii`

**Fokus:** Vertiefter Hochrisiko-Checker fuer Art. 6 Abs. 2 i.V.m. Anhang III KI-VO. Prueft alle acht Anhang-III-Bereiche mit Untertatbestaenden, Zweckbestimmung, konkretem Einsatzkontext, GPAI/Chatbot-Abgrenzung und Mitarbeitenden-Fehlgebrauch. Erklaert, warum ein allgemeiner Chatbot nicht automatisch Hochrisiko ist, aber bei intendiertem Einsatz in Justiz, Personal, Bildung, Kredit, Migration usw. Hochrisiko werden kann. Output: dokumentierte Zuordnungsentscheidung mit Bereichsmatrix, Art. 6 Abs. 3-Routing und Governance-Massnahmen.

# Hochrisiko-KI nach Art. 6 Abs. 2 i.V.m. Anhang III KI-VO

## Zweck

Dieser Skill prüft, ob ein bereits als KI-System eingeordnetes System nach Art. 6 Abs. 2 KI-VO Hochrisiko ist, weil es in einen der Anhang-III-Tatbestände fällt. Schwerpunkt ist die konkrete Zweckbestimmung und der reale Einsatzkontext, nicht der bloße Name des Modells oder Tools.

Wichtig: Ein allgemeiner Chatbot, ein GPAI-System oder eine ChatGPT-ähnliche Oberfläche ist nicht allein deshalb Hochrisiko, weil man ihn theoretisch in Personalwesen, Justiz, Bildung oder Verwaltung einsetzen könnte. Hochrisiko entsteht regelmäßig erst durch den intendierten oder tatsächlich verantworteten Einsatz für einen Anhang-III-Zweck.

## Vorfragen

Vor der Anhang-III-Prüfung immer erfassen:

1. Welches KI-System wird geprüft: Modell, API, Chatbot, Agent, Workflow, Fachmodul, Gesamtprodukt?
2. Wer bestimmt den Zweck: Anbieter, Betreiber, Fachabteilung, Kunde, öffentliche Stelle?
3. Was steht in Gebrauchsanweisung, Leistungsbeschreibung, Marketing, Prompt-Bibliothek, Systemrollen, Berechtigungskonzept und technischer Dokumentation?
4. Welche tatsächlichen Nutzungsszenarien sind erlaubt, geduldet, technisch möglich oder ausdrücklich verboten?
5. Betrifft die Ausgabe natürliche Personen oder kritische Infrastrukturen?
6. Wird die Ausgabe nur allgemein assistierend genutzt oder beeinflusst sie Entscheidung, Bewertung, Zugang, Priorisierung, Zuweisung oder Rechtsanwendung?

## Kernlogik: Zweckbestimmung vor Tool-Label

Prüfe getrennt:

| Ebene | Frage | Bedeutung |
|---|---|---|
| Anbieter-Zweckbestimmung | Für welchen konkreten Kontext wird das System laut Anbieter bestimmt? | Ausgangspunkt der Klassifikation |
| Betreiber-Zweck | Wofür nimmt der Betreiber das System in Betrieb? | Kann eigenen Hochrisiko-Einsatz begründen |
| Tatsächlicher Organisationsgebrauch | Wird ein kritischer Einsatz erlaubt, verlangt, geduldet oder systematisch genutzt? | Kann Zweckbild prägen und Pflichten auslösen |
| Vernünftigerweise vorhersehbarer Fehlgebrauch | Ist Off-label-Nutzung naheliegend, obwohl nicht intendiert? | Governance, Warnungen, Kontrollen, Re-Evaluation |
| Isolierter Regelverstoß | Nutzt ein Mitarbeiter das Tool entgegen klarer Regeln und Kontrollen? | Vorfall/Compliance-Thema, nicht automatisch neue Anbieter-Zweckbestimmung |

## Chatbot-/GPAI-Grundsatz

Ein General-Purpose-AI-Modell oder allgemeiner Chatbot ist typischerweise breit verwendbar. Die Hochrisiko-Einstufung knüpft aber an das KI-System und seine Zweckbestimmung in einem Anhang-III-Kontext an.

Prüfe deshalb:

- **Allgemeiner Assistent:** Textgenerierung, Recherche, Zusammenfassung, Übersetzung, Entwurfshilfe ohne Einsatz zur Entscheidung über natürliche Personen: regelmäßig nicht allein Hochrisiko; Art. 50 und ggf. GPAI-Pflichten prüfen.
- **Fachlich eingebetteter Assistent:** LLM wird in Recruiting, Kredit, Bildung, Justiz, Notfalltriage, Migration oder Strafverfolgung integriert: Anhang III konkret prüfen.
- **Nur theoretische Möglichkeit:** Mitarbeitende könnten ChatGPT missbrauchen, aber Zweck, Richtlinie, technische Sperren und Schulungen schließen dies aus: kein automatisches Hochrisiko, aber dokumentierte Governance nötig.
- **Geduldeter oder funktional angelegter Hochrisiko-Einsatz:** Tool wird trotz allgemeiner Bezeichnung faktisch für Bewerberranking, Leistungsbewertung, Kreditwürdigkeit, Rechtsanwendung usw. genutzt: Hochrisiko sehr naheliegend.
- **Zweckänderung oder wesentliche Änderung:** Betreiber, Importeur oder Händler kann nach Art. 25 KI-VO Anbieterpflichten auslösen; zusätzlich `anbieter-werden-art-25`.

## Anhang III: vollständige Bereichsmatrix

### Bereich 1 — Biometrie

Nur soweit der Einsatz nach Unions- oder nationalem Recht überhaupt erlaubt ist.

Hochrisiko-Tatbestände:
- Remote biometric identification, außer reine biometrische Verifikation zur Bestätigung, dass eine bestimmte Person die behauptete Person ist.
- Biometrische Kategorisierung nach sensiblen oder geschützten Attributen oder Merkmalen, soweit diese Attribute oder Merkmale inferiert werden.
- Emotionserkennung.

Prüffragen:
- Wird eine natürliche Person aus der Entfernung identifiziert?
- Geht es nur um 1:1-Authentifizierung oder um Identifikation gegen Referenzdatenbank?
- Werden sensible/protected attributes aus biometrischen Daten abgeleitet?
- Wird Emotion, Absicht oder innerer Zustand aus biometrischen Daten inferiert?
- Greift zusätzlich ein Verbot nach Art. 5, etwa Emotionserkennung am Arbeitsplatz/Bildung oder verbotene biometrische Kategorisierung?

### Bereich 2 — Kritische Infrastruktur

Hochrisiko sind KI-Systeme, die als Sicherheitskomponenten in Management und Betrieb folgender Bereiche eingesetzt werden:
- kritische digitale Infrastruktur
- Straßenverkehr
- Versorgung mit Wasser, Gas, Wärme oder Elektrizität

Prüffragen:
- Ist die KI-Komponente sicherheitsrelevant oder nur kaufmännisch/administrativ?
- Kann Fehlfunktion Gesundheit, Sicherheit, Versorgung, Verkehr oder Grundrechte ernsthaft beeinträchtigen?
- Steuert oder priorisiert das System Betrieb, Lasten, Warnungen, Zugriff, Wartung oder Ausfälle?

### Bereich 3 — Bildung und berufliche Ausbildung

Hochrisiko-Tatbestände:
- Zugang, Zulassung oder Zuweisung zu Bildungs- oder Ausbildungseinrichtungen
- Bewertung von Lernergebnissen, auch wenn diese den Lernprozess steuern
- Bewertung des angemessenen Bildungsniveaus oder Zugangs
- Überwachung und Erkennung verbotenen Verhaltens bei Prüfungen

Prüffragen:
- Bewertet das System Schüler, Studierende, Prüflinge oder Bewerber?
- Fließt die Ausgabe in Zulassung, Einstufung, Noten, Lernpfad, Prüfungsüberwachung oder Sanktion ein?
- Ist der Output nur redaktionelle Hilfe oder tatsächlicher Bewertungs-/Steuerungsfaktor?

### Bereich 4 — Beschäftigung, Arbeitnehmermanagement und Zugang zur Selbständigkeit

Hochrisiko-Tatbestände:
- Rekrutierung oder Auswahl natürlicher Personen, insbesondere gezielte Stellenanzeigen, Analyse/Filterung von Bewerbungen, Bewertung von Kandidaten
- Entscheidungen über Bedingungen arbeitsbezogener Beziehungen
- Beförderung oder Beendigung arbeitsbezogener Vertragsbeziehungen
- Aufgabenverteilung auf Grundlage individuellen Verhaltens oder persönlicher Eigenschaften/Merkmale
- Überwachung und Bewertung von Leistung oder Verhalten

Prüffragen:
- Wird das System für Bewerberfilter, Ranking, Shortlisting, Interviewauswertung oder Eignungsbewertung eingesetzt?
- Betrifft es Zielgruppensteuerung von Jobanzeigen?
- Beeinflusst es Einsatzplanung, Schicht, Aufgaben, Beförderung, Kündigung, Vergütung oder Performance-Management?
- Nutzt die Organisation einen allgemeinen Chatbot, um HR-Entscheidungen faktisch vorzubereiten? Dann Zweck und Governance streng prüfen.

### Bereich 5 — Zugang zu wesentlichen privaten und öffentlichen Dienstleistungen und Leistungen

Hochrisiko-Tatbestände:
- Öffentliche Stellen oder deren Beauftragte bewerten Anspruch/Berechtigung natürlicher Personen auf wesentliche öffentliche Unterstützungsleistungen und Dienste, einschließlich Gesundheitsdienste, oder gewähren, reduzieren, widerrufen oder fordern solche Leistungen zurück.
- Bewertung der Kreditwürdigkeit natürlicher Personen oder Erstellung eines Credit Score, ausgenommen Betrugsaufdeckung.
- Risikoabschätzung und Preisgestaltung gegenüber natürlichen Personen bei Lebens- und Krankenversicherung.
- Bewertung/Klassifizierung von Notrufen natürlicher Personen, Disposition oder Priorisierung von Notfalleinsätzen, einschließlich Polizei, Feuerwehr, medizinischer Hilfe und Notfall-Gesundheitstriage.

Prüffragen:
- Geht es um natürliche Personen, nicht nur Unternehmen?
- Ist der Output entscheidungsnah für Zugang, Preis, Leistung, Priorität oder Rückforderung?
- Ist Fraud Detection tatsächlich der Zweck oder nur Vorwand für Bonitätsbewertung?
- Bei Versicherungen: betrifft es Leben/Kranken und natürliche Personen?

### Bereich 6 — Strafverfolgung

Nur soweit der Einsatz nach Unions- oder nationalem Recht erlaubt ist.

Hochrisiko-Tatbestände:
- Risiko, Opfer einer Straftat zu werden
- Polygraphen oder ähnliche Werkzeuge
- Bewertung der Zuverlässigkeit von Beweismitteln in Ermittlung oder Strafverfolgung
- Risiko, dass eine natürliche Person Straftaten begeht oder erneut begeht, sofern nicht ausschließlich auf Profiling nach Richtlinie (EU) 2016/680 gestützt, oder Bewertung von Persönlichkeitsmerkmalen, Eigenschaften oder früherem strafrechtlichem Verhalten natürlicher Personen oder Gruppen
- Profiling natürlicher Personen im Zuge der Aufdeckung, Ermittlung oder Verfolgung von Straftaten

Prüffragen:
- Nutzt eine Strafverfolgungsbehörde oder jemand in ihrem Auftrag das System?
- Geht es um Personenrisiken, Beweisbewertung, Profiling oder kriminalitätsbezogene Einschätzung?
- Ist ein scheinbar allgemeines Analyse-/Chat-System in polizeiliche Fallbearbeitung integriert?

### Bereich 7 — Migration, Asyl und Grenzkontrolle

Nur soweit der Einsatz nach Unions- oder nationalem Recht erlaubt ist.

Hochrisiko-Tatbestände:
- Polygraphen oder ähnliche Werkzeuge
- Risikobewertung natürlicher Personen, die in das Gebiet eines Mitgliedstaats einreisen wollen oder eingereist sind, einschließlich Sicherheits-, irreguläre Migrations- oder Gesundheitsrisiken
- Unterstützung bei Prüfung von Asyl-, Visa- oder Aufenthaltstitelanträgen und zugehörigen Beschwerden hinsichtlich Anspruch/Berechtigung, einschließlich Bewertung der Zuverlässigkeit von Beweismitteln
- Erkennung, Wiedererkennung oder Identifizierung natürlicher Personen im Kontext von Migration, Asyl oder Grenzkontrolle, ausgenommen Überprüfung von Reisedokumenten

Prüffragen:
- Unterstützt das System die Entscheidung über Status, Einreise, Aufenthalt, Beschwerde oder Risiko?
- Bewertet es Glaubhaftigkeit, Dokumente, Beweise oder persönliche Risiken?
- Geht es nur um technische Dokumentenprüfung oder um Personenidentifikation/Bewertung?

### Bereich 8 — Rechtspflege und demokratische Prozesse

Hochrisiko-Tatbestände:
- Nutzung durch oder im Auftrag einer Justizbehörde zur Unterstützung bei Recherche und Auslegung von Tatsachen und Recht und bei Anwendung des Rechts auf einen konkreten Sachverhalt; ähnlich auch in alternativer Streitbeilegung.
- Beeinflussung des Ergebnisses einer Wahl oder eines Referendums oder des Wahlverhaltens natürlicher Personen. Nicht erfasst sind rein administrative/logistische Kampagnentools, deren Output natürlichen Personen nicht direkt ausgesetzt wird.

Prüffragen:
- Nutzt Gericht, Spruchkörper, Behörde mit Rechtsprechungsnähe oder ADR-Stelle das System?
- Unterstützt das System konkrete Rechtsanwendung, Tatsachenwürdigung oder Entscheidungsvorschlag?
- Ist der Output nur allgemeine Recherche für Anwälte/Parteien oder justizielle Entscheidungsassistenz?
- Wird politisches Verhalten direkt beeinflusst oder nur Kampagnenlogistik intern optimiert?

## Zweckbestimmung und Fehlgebrauch in der Organisation

### Fallgruppe A — Hochrisiko ausdrücklich intendiert

Beispiel: Anbieter bewirbt "KI für Bewerberranking" oder "KI für richterliche Entscheidungsunterstützung".

Ergebnis: Anhang-III-Prüfung regelmäßig positiv; Art. 6 Abs. 3 nur gesondert und eng prüfen.

### Fallgruppe B — Allgemeines Tool, Betreiber setzt es bewusst hochriskant ein

Beispiel: Unternehmen nutzt ChatGPT-ähnliches System systematisch zur Bewertung von Bewerbern oder Beschäftigten.

Ergebnis: Der konkrete Einsatz kann Hochrisiko sein, auch wenn das Basismodell/allgemeine System nicht als Hochrisiko vermarktet wird. Betreiberpflichten und ggf. Anbieterwerden nach Art. 25 prüfen.

### Fallgruppe C — Mitarbeitende handeln entgegen Zweckbestimmung

Prüfe:
- Gibt es klare KI-Richtlinie, Schulung nach Art. 4, Sperren, Rollenrechte, Logging und Kontrollen?
- Ist der Fehlgebrauch technisch möglich, naheliegend und bekannt?
- Wird er geduldet oder nur isoliert sanktioniert?

Bewertung:
- **Isolierter Verstoß trotz klarer Governance:** dokumentierter Compliance-Vorfall, Nachschulung, Sperre, Logging, Löschung/Separierung fehlerhafter Outputs; nicht automatisch Hochrisiko-Klassifikation des Systems.
- **Duldung oder systematische Praxis:** faktische Zweckbestimmung des Betreibers kann kippen; Hochrisiko neu prüfen.
- **Technisch angelegte Nutzung ohne Kontrollen:** vernünftigerweise vorhersehbarer Fehlgebrauch; Warnhinweise, Gebrauchsanweisung, Zugriffsbeschränkung und Re-Evaluation erforderlich.

### Fallgruppe D — Wesentliche Änderung oder Zweckänderung

Wenn ein Betreiber das System so verändert oder zweckentfremdet, dass eine neue Hochrisiko-Zweckbestimmung entsteht, zusätzlich prüfen:
- `anbieter-werden-art-25`
- `betreiber-deployer-pflichten-art-26`
- `hochrisiko-bestaetigt-end-to-end-roadmap`

## Art. 6 Abs. 3 nicht vergessen

Wenn ein Anhang-III-Tatbestand passt, ist die Prüfung noch nicht fertig:

1. Profiling natürlicher Personen? Wenn ja, keine Rückausnahme.
2. Kein erhebliches Risiko für Gesundheit, Sicherheit oder Grundrechte?
3. Eine der vier Fallgruppen: enge Verfahrensaufgabe, Verbesserung bereits abgeschlossener menschlicher Tätigkeit, Mustererkennung ohne Ersatz/Einfluss auf frühere menschliche Bewertung, vorbereitende Aufgabe?
4. Dokumentationspflicht und Registrierung nach Art. 6 Abs. 4 beachten, wenn Anbieter das System trotz Anhang III als nicht Hochrisiko einstuft.

Weiter: `rueckausnahme-art-6-abs-3`.

## Output-Template — Anhang-III-Zuordnungsvermerk

```text
ANHANG-III-ZUORDNUNGSVERMERK — ART. 6 ABS. 2 KI-VO
Datum: [DATUM]
System: [NAME]
Geprüfter Einsatz: [KONKRETER USE CASE]
Rolle des Mandanten: [ANBIETER / BETREIBER / IMPORTER / HAENDLER / UNKLAR]

1. Zweckbestimmung und Nutzung
- Anbieter-Zweckbestimmung: [...]
- Betreiber-Zweck / tatsächliche Nutzung: [...]
- Gebrauchsanweisung / Marketing / technische Dokumentation: [...]
- Erlaubte, geduldete und verbotene Nutzungen: [...]
- Vorhersehbarer Fehlgebrauch: [...]

2. GPAI/Chatbot-Abgrenzung
[Allgemeiner Assistent / eingebettetes Fachsystem / hochriskanter Zweck / nur theoretische Möglichkeit]

3. Anhang-III-Matrix
Nr. 1 Biometrie: [JA/NEIN/UNKLAR] — [Begründung]
Nr. 2 Kritische Infrastruktur: [JA/NEIN/UNKLAR] — [Begründung]
Nr. 3 Bildung: [JA/NEIN/UNKLAR] — [Begründung]
Nr. 4 Beschäftigung: [JA/NEIN/UNKLAR] — [Begründung]
Nr. 5 Wesentliche Dienste/Leistungen: [JA/NEIN/UNKLAR] — [Begründung]
Nr. 6 Strafverfolgung: [JA/NEIN/UNKLAR] — [Begründung]
Nr. 7 Migration/Asyl/Grenze: [JA/NEIN/UNKLAR] — [Begründung]
Nr. 8 Rechtspflege/demokratische Prozesse: [JA/NEIN/UNKLAR] — [Begründung]

4. Ergebnis Art. 6 Abs. 2
[Hochrisiko nach Anhang III wahrscheinlich / nicht ersichtlich / offen]

5. Art. 6 Abs. 3
[Rückausnahme zu prüfen / Profiling sperrt Rückausnahme / Rückausnahme offensichtlich fernliegend]

6. Governance bei Off-label-Nutzung
[Richtlinie, Sperren, Logging, Schulung, Freigabeprozess, Re-Evaluation, Incident Handling]

7. Nächste Skills
[rueckausnahme-art-6-abs-3 / betreiber-deployer-pflichten-art-26 / anbieter-werden-art-25 / begrenztes-risiko-art-50-transparenzpflichten / gpai-vorliegen-art-3-nr-63 / output-pruefdokument-ki-vo-mit-warnhinweisen]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 3 Nr. 12, Nr. 13 und Nr. 23, Art. 6 Abs. 2 bis 5 und Anhang III KI-VO sowie die Kommissionsmaterialien zur Hochrisiko-Klassifikation. Die im Mai 2026 veröffentlichten Hochrisiko-Leitlinien waren zum Stand dieses Skills als Entwurf/Konsultationsmaterial zu behandeln, bis sie formal angenommen sind. Keine Rechtsberatung.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `hochrisiko-aufzeichnungspflichten-logging-art-12`

**Fokus:** Anbieter von Hochrisiko-KI fragt: Was muss unser System automatisch aufzeichnen und wie lange muessen wir die Logs aufbewahren? Art. 12 KI-VO Logging-Pflichten. Prüfraster: Mindestinhalte der Logs Zeitstempel Eingabedaten Ausgaben Fehlermeldungen Aufbewahrungsfrist drei Jahre bzw. Vertragsdauer Verantwortlichkeitsteilung Anbieter vs. Betreiber. Besondere Anforderungen biometrische Identifikation Art. 12 Abs. 3. Output: Logging-Anforderungskatalog und Muster-Log-Schema. Abgrenzung zu hochrisiko-technische-dokumentation-art-11-und-anhang-iv (Dokumentationspflichten) und betreiber-deployer-pflichten-art-26.

# Aufzeichnungspflichten und Logging — Art. 12 KI-VO

## Zweck

Art. 12 KI-VO verpflichtet Anbieter von Hochrisiko-KI-Systemen, sicherzustellen, dass das System automatisch Ereignisse protokolliert. Diese Logs dienen der Rückverfolgung, der Überwachung nach dem Inverkehrbringen und der Aufklärung von Vorfällen.

## Grundanforderung: Automatische Protokollierung (Art. 12 Abs. 1 KI-VO)

Hochrisiko-KI-Systeme müssen automatisch Ereignisse protokollieren, die für die Kontrolle des Systembetriebs und die Ermittlung von Risiken nach dem Inverkehrbringen relevant sind.

**Grundsatz:** Die Protokollierung muss technisch in das System integriert sein — manuelle Nacherfassung genügt nicht.

## Mindestinhalt der Logs (Art. 12 Abs. 2 KI-VO)

Die Protokolle müssen mindestens enthalten:
- Zeitstempel jedes Ereignisses
- Referenzdatenbankeinträge (wenn das System mit Datenbanken arbeitet)
- Eingabedaten (soweit relevant für die Nachvollziehbarkeit)
- Identität der natürlichen Personen, die an der Überprüfung der Ergebnisse beteiligt sind (wo zutreffend)
- Datum, Uhrzeit und Ort des Betriebs des Systems

**Prüffragen:**
- Protokolliert das System automatisch alle relevanten Ereignisse?
- Sind Zeitstempel, Eingaben und Ausgaben nachvollziehbar erfasst?
- Werden Identitäten der beteiligten Personen (wo relevant) erfasst?

## Besondere Anforderungen — Biometrische Fernidentifikation

Für biometrische Echtzeit-Fernidentifikationssysteme (die nur unter den engen Ausnahmen von Art. 5 Abs. 2 KI-VO zulässig sind) gelten besonders strenge Protokollierungsanforderungen. Jeder Einsatz ist zu protokollieren, und die Protokolle müssen der Datenschutzbehörde auf Anfrage zugänglich gemacht werden.

## Verantwortungsverteilung zwischen Anbieter und Betreiber

**Anbieter:** Muss sicherstellen, dass das System technisch in der Lage ist, die erforderlichen Logs zu erstellen. Die Protokollierungsfähigkeit ist Teil der technischen Spezifikation.

**Betreiber:** Muss sicherstellen, dass die Protokolle tatsächlich erstellt, gespeichert und aufbewahrt werden. Betreiber sind nach Art. 26 Abs. 6 KI-VO verpflichtet, die Protokolle sechs Monate aufzubewahren, es sei denn, andere Vorschriften (z.B. DSGVO, nationales Recht) sehen kürzere oder längere Fristen vor.

**Prüffragen:**
- Welche Partei ist für die Protokollierung verantwortlich — Anbieter, Betreiber oder beide?
- Gibt es vertragliche Regelungen zwischen Anbieter und Betreiber zur Protokollierung (Art. 25 Abs. 4 KI-VO)?

## Aufbewahrungsfristen

- **Betreiber allgemein:** Sechs Monate Aufbewahrungspflicht (Art. 26 Abs. 6 KI-VO)
- **Biometrische Identifikation:** Besondere Fristen nach nationalem Recht oder Behördenanforderungen
- **Anbieter (technische Dokumentation):** Zehn Jahre (Art. 18 KI-VO)
- **Widerspruch mit DSGVO:** Protokolle, die personenbezogene Daten enthalten, müssen datenschutzkonform aufbewahrt und nach Ablauf der Frist gelöscht werden

## Verhältnis zu Post-Market-Monitoring

Die nach Art. 12 KI-VO erstellten Protokolle sind ein wesentliches Instrument für das Post-Market-Monitoring nach Art. 72 KI-VO. Ohne Protokolle kann ein ernsthafter Vorfall nicht aufgeklärt werden.

## Typische Lücken

- Protokollierung ist nicht automatisiert und basiert auf manuellen Einträgen.
- Logs werden nach kurzer Zeit automatisch gelöscht (z.B. für Datensparsamkeit), ohne Berücksichtigung der Aufbewahrungspflichten.
- Kein klarer Verantwortlicher für die Aufbewahrung der Logs.
- Logs enthalten keine ausreichenden Zeitstempel oder Kontextinformationen für die Rekonstruktion von Vorfällen.

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
PRUEFERGEBNIS — HOCHRISIKO AUFZEICHNUNGSPFLICHTEN LOGGING ART 12
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 12 Rn. 4]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 3. `hochrisiko-bestaetigt-end-to-end-roadmap`

**Fokus:** Anbieter hat Hochrisiko-Einstufung des eigenen KI-Systems bestätigt und fragt: Was sind jetzt alle noetigen Schritte bis zur CE-Kennzeichnung und Marktfreigabe? End-to-End-Roadmap Hochrisiko-KI Art. 9 bis 49 KI-VO. Prüfraster: zwoelf Schritte Risikomanagementsystem Art. 9 Datenqualitaet Art. 10 technische Dokumentation Art. 11 Logging Art. 12 Transparenz Art. 13 menschliche Aufsicht Art. 14 Genauigkeit Art. 15 Konformitätsbewertung Art. 43 CE-Kennzeichnung Art. 47 EU-Datenbank Art. 49 Marktbeobachtung. Output: Projektplan mit Aufwandsschaetzung Akteuren und Fristen.

# Hochrisiko-KI bestätigt — die End-to-End-Roadmap

## Zweck

Sie haben festgestellt: das System ist Hochrisiko nach Art. 6 Abs. 1 oder Abs. 2 i.V.m. Anhang I/III KI-VO. Die Rückausnahme nach Art. 6 Abs. 3 KI-VO greift nicht. **Was jetzt?**

Dieser Skill liefert den vollständigen Mandanten-von "Hochrisiko-Diagnose" bis "Marktreife mit CE-Kennzeichnung". Ziel ist Entdramatisierung: jeder Schritt ist mechanisch abarbeitbar.

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

→ Detail-Skill: `hochrisiko-transparenz-und-informationen-fuer-betreiber-art-13`

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

## Querverweise

- `entscheidungsbaum-ki-vo-gesamt-workflow` — Master-vorgelagert
- `nicht-hochrisiko-bestaetigt-end-to-end-roadmap` — alternative Pfade
- `rueckausnahme-art-6-abs-3` — falls Diagnose noch unsicher
- `sanktionen-art-99-bis-101` — was passiert, wenn nichts unternommen wird
- `mandatsabbruch-empfehlung-komplexe-faelle` — wenn intern nicht stemmbar

---

Hinweis: Keine Rechtsberatung. Mechanische Roadmap. Konkrete Umsetzung erfordert produkt-/branchen-spezifische Detailprüfung.

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

## 4. `hochrisiko-datenqualitaet-und-data-governance-art-10`

**Fokus:** Anbieter von Hochrisiko-KI fragt: Welche Anforderungen gelten für unsere Trainings- Validierungs- und Testdaten und wie dokumentieren wir unsere Data Governance? Art. 10 KI-VO Datenqualitaet und Data Governance. Prüfraster: Relevanz Repraesentativitaet Vollständigkeit Fehlerfreiheit Bias-Minderung Ausnahme besondere Datenkategorien Art. 10 Abs. 5. Output: Data-Governance-Checkliste und Vorlage Trainingsdaten-Dokumentation. Abgrenzung zu hochrisiko-technische-dokumentation-art-11-und-anhang-iv (Gesamtdokumentation) und hochrisiko-risikomanagementsystem-art-9 (Risikobewertung).

# Datenqualität und Data Governance — Art. 10 KI-VO

## Zweck

Art. 10 KI-VO stellt spezifische Anforderungen an die Daten, mit denen Hochrisiko-KI-Systeme trainiert, validiert und getestet werden. "Garbage in, garbage out" ist keine Entschuldigung — mangelhafte Datenqualität begründet einen Pflichtverstoß.

## Pflichten im Überblick (Art. 10 Abs. 2 KI-VO)

### Anforderung 1 — Geeignete Datenverwaltungspraktiken

Anbieter müssen geeignete Datenverwaltungspraktiken umsetzen, die Folgendes umfassen:
- Klare Festlegung des Entwicklungsziels und der vorgesehenen Verwendungszwecke
- Verfahren zur Datenerhebung
- Analyse auf mögliche Verzerrungen (Bias)
- Erkennung und Behebung von Datenlücken und Mängeln

**Prüffragen:**
- Gibt es eine schriftlich dokumentierte Datenstrategie?
- Wurden Herkunft, Erhebungsmethode und Qualitätsmerkmale der Datensätze dokumentiert?

### Anforderung 2 — Relevanz und Repräsentativität (Art. 10 Abs. 3 KI-VO)

Trainings-, Validierungs- und Testdatensätze müssen:
- Relevant für den vorgesehenen Zweck des Systems sein
- Repräsentativ für die Bedingungen sein, unter denen das System eingesetzt werden soll
- Hinreichend vollständig und fehlerfrei sein (unter Berücksichtigung des Einsatzbereichs)
- Die spezifischen Eigenschaften und Merkmale der vorgesehenen Einsatzsituation aufweisen

**Prüffragen:**
- Deckt der Datensatz die Vielfalt der Einsatzbedingungen ab?
- Sind bestimmte Bevölkerungsgruppen, Szenarien oder Randfälle unterrepräsentiert?
- Wurden bekannte Datenmängel dokumentiert und ihr Einfluss auf die Systemleistung bewertet?

### Anforderung 3 — Bias-Erkennung und Bias-Minderung (Art. 10 Abs. 2 lit. f KI-VO)

Anbieter müssen Daten auf mögliche Verzerrungen analysieren und geeignete Maßnahmen zur Bias-Minderung ergreifen. Dies gilt insbesondere bei Systemen, die auf Merkmale wie Alter, Geschlecht, ethnische Zugehörigkeit oder andere geschützte Kategorien zugreifen können.

**Prüffragen:**
- Wurden Bias-Analysen durchgeführt (z.B. Fairness-Metriken, Subgruppen-Analysen)?
- Sind die Maßnahmen zur Bias-Minderung dokumentiert und auf ihre Wirksamkeit geprüft?
- Welche Restverzerrungen verbleiben nach den Minderungsmaßnahmen?

### Anforderung 4 — Trennung der Datensätze

Trainings-, Validierungs- und Testdatensätze müssen klar voneinander getrennt sein. Insbesondere darf der Testdatensatz nicht für das Training oder die Parameteroptimierung verwendet worden sein.

**Prüffragen:**
- Sind die drei Datensätze klar getrennt und dokumentiert?
- Wurde der Testdatensatz ausschließlich für die abschließende Leistungsbeurteilung verwendet?

## Ausnahme für besondere Datenkategorien (Art. 10 Abs. 5 KI-VO)

Für die Zwecke der Erkennung und Korrektur von Verzerrungen in Hochrisiko-KI-Systemen ist die Verarbeitung besonderer Kategorien personenbezogener Daten nach Art. 9 Abs. 1 DSGVO (Rasse, Gesundheit, Religion, sexuelle Orientierung usw.) unter engen Voraussetzungen erlaubt:
- Wirksame technisch-organisatorische Sicherheitsvorkehrungen müssen vorhanden sein
- Die Verarbeitung darf ausschließlich zu diesem Zweck erfolgen
- Die Daten dürfen nicht zu anderen Zwecken verarbeitet werden
- Die Daten dürfen nicht übermittelt werden
- Die Daten sind nach Abschluss der Bias-Analyse zu löschen

**Prüffragen:**
- Liegt eine DSGVO-konforme Rechtsgrundlage für die Verarbeitung besonderer Kategorien vor?
- Sind die Sicherheitsvorkehrungen dokumentiert?
- Wird die Verarbeitung strikt auf den Bias-Korrekturzweck beschränkt?

## Verhältnis zu anderen Pflichten

Art. 10 KI-VO ist eng verzahnt mit:
- Art. 9 KI-VO (Risikomanagement — schlechte Daten erzeugen Risiken)
- Art. 11 und Anhang IV KI-VO (Technische Dokumentation — Datensätze sind zu beschreiben)
- DSGVO — Datenschutz gilt parallel für alle personenbezogenen Trainingsdaten

## Typische Praxisprobleme

- Trainingsdaten wurden nicht dokumentiert; keine Herkunftsnachweise.
- Test- und Validierungsdaten überlappen mit Trainingsdaten.
- Bias-Analyse wurde durchgeführt, aber Ergebnisse nicht dokumentiert.
- Besondere Datenkategorien wurden ohne DSGVO-Rechtsgrundlage verarbeitet.

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
PRUEFERGEBNIS — HOCHRISIKO DATENQUALITAET UND DATA GOVERNANCE ART 10
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 10 Rn. 6]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
