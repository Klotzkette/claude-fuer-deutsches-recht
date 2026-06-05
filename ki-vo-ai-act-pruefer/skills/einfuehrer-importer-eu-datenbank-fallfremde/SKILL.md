---
name: einfuehrer-importer-eu-datenbank-fallfremde
description: "Einfuehrer Importer EU Datenbank Fallfremde: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Einfuehrer Importer EU Datenbank Fallfremde

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Einfuehrer Importer EU Datenbank Fallfremde** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `einfuehrer-importer-pflichten-art-23` | Importeur von KI-Systemen aus Drittstaaten fragt: Was muss ich prüfen bevor ich ein Hochrisiko-KI-System in der EU in Verkehr bringe? Art. 23 KI-VO Einführer-Pflichten. Prüfraster: Konformitätsbewertung durch Anbieter bereits durchgeführt CE-Kennzeichnung vorhanden technische Dokumentation und EU-Konformitätserklärung geprüft Bevollmaechtigter benannt. Wann wird Einführer zum Anbieter Art. 25 KI-VO. Output: Checkliste Einführer-Sorgfaltspflichten. Abgrenzung zu haendler-distributor-pflichten-art-24 (Vertrieb) und anbieter-werden-art-25 (Rollenwechsel). |
| `eu-datenbank-registrierung-art-49-und-71` | Anbieter oder Betreiber von Hochrisiko-KI fragt: In welcher EU-Datenbank muss ich mein KI-System registrieren und wann? Art. 49 und 71 KI-VO Registrierungspflichten. Prüfraster: Anbieter vor Inverkehrbringen Pflicht Art. 49 Abs. 1 öffentliche Stellen als Betreiber vor Verwendung Art. 49 Abs. 3. Inhalt nach Anhang VIII Fristen Vertraulichkeit vs. öffentliche Zugaenglichkeit Mindestfelder. Output: Registrierungs-Checkliste und Muster-Registrierungsdatensatz. Abgrenzung zu hochrisiko-konformitätsbewertung-art-43-bis-49 (Konformitätsbewertung) und hochrisiko-bestätigt-end-to-end-roadmap (Gesamt-Roadmap). |
| `fallfremde-textbausteine-prozessrisiko` | Fallfremde KI-Textbausteine erkennen und entschärfen: Namen, Daten, Aktenzeichen, Tatvorwürfe, falsche Anlagen, fremde Prozessgeschichte und bewusst/unbewusst irreführender Vortrag in Schriftsatz, Einspruch, Klage oder Behördenantwort. |
| `falsche-wiese-warnung-ki-vo` | Nutzer fragt eine KI-VO-Frage die eigentlich unter DSGVO Produkthaftung MDR oder Maschinenverordnung faellt. Warnt vor typischen Rechtsgebiets-Verwechslungen KI-VO versus DSGVO versus Produkthaftungsrichtlinie versus Medizinprodukteverordnung versus Maschinenverordnung versus Cyber Resilience Act. Prüfraster: Schluesselmerkmale zur Abgrenzung der Regelwerke. Output: Orientierungsmemo mit konkretem Verweis auf das tatsaechlich einschlaegige Recht. Abgrenzung zu verhältnis-zu-anderen-unionsrechtsakten (systematische Kumulationsprüfung) und territorialer-anwendungsbereich-art-2. |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Einfuehrer Importer EU Datenbank Fallfremde**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `einfuehrer-importer-pflichten-art-23`

**Fokus:** Importeur von KI-Systemen aus Drittstaaten fragt: Was muss ich prüfen bevor ich ein Hochrisiko-KI-System in der EU in Verkehr bringe? Art. 23 KI-VO Einführer-Pflichten. Prüfraster: Konformitätsbewertung durch Anbieter bereits durchgeführt CE-Kennzeichnung vorhanden technische Dokumentation und EU-Konformitätserklärung geprüft Bevollmaechtigter benannt. Wann wird Einführer zum Anbieter Art. 25 KI-VO. Output: Checkliste Einführer-Sorgfaltspflichten. Abgrenzung zu haendler-distributor-pflichten-art-24 (Vertrieb) und anbieter-werden-art-25 (Rollenwechsel).

# Einführer-Pflichten (Importer) — Art. 23 KI-VO

## Zweck

Ein Einführer ist derjenige, der ein in einem Drittland in Verkehr gebrachtes Hochrisiko-KI-System in der EU in Verkehr bringt. Art. 23 KI-VO legt den Pflichtenkatalog für Einführer fest.

## Wer ist Einführer?

Ein Einführer ist eine in der EU niedergelassene natürliche oder juristische Person, die ein Hochrisiko-KI-System in der EU in Verkehr bringt, das von einem nicht in der EU niedergelassenen Anbieter stammt.

**Abgrenzung zum Händler:** Der Einführer bringt das System als Erster in der EU in Verkehr; der Händler stellt ein bereits in der EU in Verkehr gebrachtes System bereit.

**Abgrenzung zum Betreiber:** Der Einführer handelt auf der Marktseite; der Betreiber verwendet das System in eigener Verantwortung.

## Pflicht 1 — Sorgfaltsprüfung vor Inverkehrbringen (Art. 23 Abs. 1 KI-VO)

Bevor ein Einführer ein Hochrisiko-KI-System in der EU in Verkehr bringt, muss er sicherstellen, dass:
- Die Konformitätsbewertung nach Art. 43 bis 49 KI-VO durchgeführt wurde
- Der Anbieter die technische Dokumentation nach Art. 11 und Anhang IV erstellt hat
- Das System die CE-Kennzeichnung trägt
- Der Anbieter die EU-Konformitätserklärung nach Art. 47 ausgestellt hat
- Der Anbieter in der EU-Datenbank registriert ist (Art. 49 und 71 KI-VO)

**Prüffragen:**
- Haben Sie vom Anbieter alle genannten Dokumente und Nachweise erhalten?
- Haben Sie die CE-Kennzeichnung und die Konformitätserklärung geprüft?

## Pflicht 2 — Prüfung auf Anzeichen mangelnder Konformität (Art. 23 Abs. 1 lit. c KI-VO)

Der Einführer muss das Hochrisiko-KI-System auf Anzeichen prüfen, dass es nicht den Anforderungen der KI-VO entspricht. Er darf kein System in Verkehr bringen, wenn er Grund zur Annahme hat, dass es nicht konform ist.

**Prüffragen:**
- Gibt es Hinweise, dass das System fehlerhaft ist oder risikobehaftet ist?
- Hat der Anbieter bekannte Mängel nicht offengelegt?

## Pflicht 3 — Angabe der eigenen Kontaktdaten (Art. 23 Abs. 2 KI-VO)

Der Einführer muss seine Identifikationsangaben (Name, Anschrift) auf dem System oder der Begleitdokumentation anbringen, damit er für Marktüberwachungsbehörden und andere Stellen erreichbar ist.

## Pflicht 4 — Lagerung und Transport (Art. 23 Abs. 3 KI-VO)

Wenn das Hochrisiko-KI-System physisch vorhanden ist: Der Einführer muss sicherstellen, dass die Lagerungs- und Transportbedingungen die Konformität nicht beeinträchtigen.

## Pflicht 5 — Aufbewahrungspflichten (Art. 23 Abs. 4 KI-VO)

Der Einführer muss die Konformitätserklärung und — soweit zutreffend — die technische Dokumentation zehn Jahre aufbewahren und Behörden auf Anfrage vorlegen.

## Wann wird der Einführer zum Anbieter? (Art. 23 Abs. 5 KI-VO)

Der Einführer übernimmt die Pflichten eines Anbieters, wenn er:
- Den Namen oder die Marke des Anbieters durch seinen eigenen Namen oder seine eigene Marke ersetzt
- Das Hochrisiko-KI-System nach dem Inverkehrbringen wesentlich verändert

In diesen Fällen ist der Einführer vollständig für alle Anbieter-Pflichten nach Art. 16 bis 42 KI-VO verantwortlich.

**Prüffragen:**
- Bringen Sie das System unter eigenem Namen oder eigener Marke in Verkehr?
- Nehmen Sie wesentliche Änderungen am System vor?

## Meldepflicht bei schwerwiegenden Risiken (Art. 23 Abs. 6 KI-VO)

Der Einführer muss dem Anbieter und der nationalen Marktüberwachungsbehörde unverzüglich Meldung erstatten, wenn das System eine Gefahr für Gesundheit, Sicherheit oder Grundrechte darstellt.

## Kooperation mit Marktüberwachungsbehörden (Art. 23 Abs. 7 KI-VO)

Der Einführer muss mit nationalen Behörden kooperieren und Unterlagen auf Anfrage vorlegen.

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
PRUEFERGEBNIS — EINFUEHRER IMPORTER PFLICHTEN ART 23
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 23 Rn. 3]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 2. `eu-datenbank-registrierung-art-49-und-71`

**Fokus:** Anbieter oder Betreiber von Hochrisiko-KI fragt: In welcher EU-Datenbank muss ich mein KI-System registrieren und wann? Art. 49 und 71 KI-VO Registrierungspflichten. Prüfraster: Anbieter vor Inverkehrbringen Pflicht Art. 49 Abs. 1 öffentliche Stellen als Betreiber vor Verwendung Art. 49 Abs. 3. Inhalt nach Anhang VIII Fristen Vertraulichkeit vs. öffentliche Zugaenglichkeit Mindestfelder. Output: Registrierungs-Checkliste und Muster-Registrierungsdatensatz. Abgrenzung zu hochrisiko-konformitätsbewertung-art-43-bis-49 (Konformitätsbewertung) und hochrisiko-bestätigt-end-to-end-roadmap (Gesamt-Roadmap).

# EU-Datenbank-Registrierung — Art. 49 und 71 KI-VO

## Zweck

Art. 49 und 71 KI-VO verpflichten Anbieter und bestimmte Betreiber, ihre Hochrisiko-KI-Systeme in einer öffentlich zugänglichen EU-Datenbank zu registrieren. Dieser Skill klärt, wer wann was registrieren muss.

## Wer muss sich registrieren?

### Anbieter von Hochrisiko-KI-Systemen (Art. 49 Abs. 1 KI-VO)

Anbieter von Hochrisiko-KI-Systemen nach Art. 6 Abs. 2 i.V.m. Anhang III KI-VO müssen sich und ihr System in der EU-Datenbank registrieren, bevor sie das System in Verkehr bringen oder in Betrieb nehmen.

**Ausnahme:** Hochrisiko-KI-Systeme nach Art. 6 Abs. 1 (Sicherheitsbauteile nach Anhang I) werden im Rahmen der sektorbezogenen Konformitätsbewertung registriert — eine separate Registrierung in der KI-VO-Datenbank ist nicht gesondert vorgeschrieben (Art. 49 Abs. 4 KI-VO).

### Betreiber aus dem öffentlichen Sektor (Art. 49 Abs. 3 KI-VO)

Betreiber, die öffentliche Einrichtungen sind (Behörden, staatliche Stellen), müssen sich ebenfalls registrieren, bevor sie ein Hochrisiko-KI-System nach Anhang III einsetzen. Dies gilt auch, wenn das System bereits vom Anbieter registriert wurde — Betreiber registrieren ihren Einsatz gesondert.

**Prüffragen für Betreiber:**
- Sind Sie eine Behörde oder sonstige öffentliche Einrichtung?
- Setzen Sie ein Hochrisiko-KI-System nach Anhang III ein?

### GPAI-Modell-Anbieter

Anbieter von GPAI-Modellen (auch solcher ohne systemisches Risiko) müssen bestimmte Informationen nach Art. 71 KI-VO in der EU-Datenbank registrieren.

## Zeitpunkt der Registrierung

**Anbieter:** Vor dem Inverkehrbringen oder der Inbetriebnahme des Hochrisiko-KI-Systems.

**Betreiber (öffentliche Stellen):** Vor der Inbetriebnahme des Systems.

**GPAI-Anbieter:** Vor dem Inverkehrbringen des GPAI-Modells.

## Inhalt der Registrierung (Anhang VIII KI-VO)

Die Registrierung muss folgende Informationen enthalten:

**Angaben zum Anbieter:**
- Name und Anschrift sowie — sofern vorhanden — Handelsregisternummer des Anbieters
- Kontaktdaten
- Gegebenenfalls Name und Anschrift des Bevollmächtigten

**Angaben zum KI-System:**
- Handelsnamen und Bezeichnung des Systems
- Beschreibung des Verwendungszwecks
- Status des Systems (in Verkehr gebracht, in Betrieb genommen, zurückgezogen)
- Typ und Art des KI-Systems
- Kurzbeschreibung der Fähigkeiten und Grenzen des Systems
- Mitgliedstaat(en), in dem/denen das System in Verkehr gebracht wurde
- Angaben zur Konformitätsbewertung (Modul, beteiligte benannte Stelle, Bescheinigungsnummer)

**Für Betreiber (öffentliche Stellen) zusätzlich:**
- Bezeichnung und Beschreibung des Einsatzkontexts
- Zeitraum und geografischer Bereich der Verwendung
- Kategorie der betroffenen natürlichen Personen

## Öffentliche Zugänglichkeit und Vertraulichkeit

Die EU-Datenbank ist öffentlich zugänglich, soweit keine berechtigten Vertraulichkeitsinteressen entgegenstehen. Anbieter können für bestimmte Informationen Vertraulichkeit beantragen — z.B. für Betriebs- und Geschäftsgeheimnisse.

Die Datenbank wird von der Kommission eingerichtet und verwaltet (Art. 71 KI-VO). Sie dient als Transparenzinstrument für Öffentlichkeit, Behörden und Betroffene.

## Technische Umsetzung

Die EU-Datenbank ist unter folgender URL zugänglich (sobald verfügbar): https://ai-act.eu (Domäne noch nicht final — genaue URL durch Kommission zu bestätigen). Im Aufbau befindet sich das System seit 2024.

## Folgen der Nichtregistrierung

Fehlende oder fehlerhafte Registrierung ist ein Verstoß gegen die KI-VO (Art. 49 KI-VO i.V.m. Art. 99 Abs. 4 KI-VO) und kann mit Bußgeldern bis zu 15 Mio EUR oder drei Prozent des weltweiten Jahresumsatzes geahndet werden.

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
PRUEFERGEBNIS — EU DATENBANK REGISTRIERUNG ART 49 UND 71
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 49 Rn. 2]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 3. `fallfremde-textbausteine-prozessrisiko`

**Fokus:** Fallfremde KI-Textbausteine erkennen und entschärfen: Namen, Daten, Aktenzeichen, Tatvorwürfe, falsche Anlagen, fremde Prozessgeschichte und bewusst/unbewusst irreführender Vortrag in Schriftsatz, Einspruch, Klage oder Behördenantwort.

# Fallfremde Textbausteine

## Warum dieser Skill wichtig ist

KI-gestützte Textarbeit produziert manchmal flüssige, aber fremde Inhalte: anderer Fall, falsche Behörde, unpassender Tatvorwurf, erfundene Anlage, falscher Streitgegenstand. Im Prozess kann das die Glaubwürdigkeit zerstören und berufsrechtliche Folgefragen auslösen.

## Norm- und Prozessanker

- ZPO § 138 für Wahrheitspflicht und Erklärungslast im Zivilprozess; ZPO §§ 130, 130a für formale Schriftsatzanforderungen.
- StPO/OWiG und VwGO/SGG/FGO jeweils gesondert prüfen: falsche Tatsachen können je nach Verfahren andere Folgen haben.
- BRAO § 43a, BORA und Mandatsvertrag für anwaltliche Sorgfalt, Verschwiegenheit und Verantwortung.
- StGB §§ 153 ff., 164, 263 nur als Warnanker bei bewusst falschen Angaben, falscher Verdächtigung oder Täuschung.
- Datenschutz/Geheimnisschutz prüfen, wenn fremde Mandatsdaten in den Textbaustein geraten sind.

## Suchmuster

Prüfe gezielt:

- Namen, Firmen, Orte, Gerichte, Behörden.
- Aktenzeichen und Geschäftsnummern.
- Datumslogik und Fristen.
- Anlagenbezeichnungen und Anlagenreihenfolge.
- Beträge, Kontonummern, Vertragsdaten, Bescheidnummern.
- Rechtsgebietssprünge: Strafrecht im Zivilprozess, Mietrecht im Datenschutzfall, falsche Verfahrensordnung.

## Ampel

- **Grün:** Aktenbezug eindeutig.
- **Gelb:** plausibel, aber nicht belegt.
- **Rot:** fremd, erfunden, widersprüchlich oder gefährlich.

## Output

Erstelle:

1. Korrekturliste mit Fundstelle im Dokument.
2. Ersatzformulierung ohne fremden Tatsachenkern.
3. Hinweis, ob eine Berichtigung gegenüber Gericht/Behörde erforderlich sein kann.
4. Kanzlei-Lernpunkt fuer Prompt- und Reviewprozess.
5. Eskalationshinweis: intern korrigieren, Mandant informieren, Gericht/Behörde berichtigen oder Fristverlängerung beantragen.

## Qualitätsregel

Wenn ein Satz wie "unstreitig" oder "nachweislich" auftaucht, muss ein Aktenbeleg daneben stehen. Sonst neutralisieren.

## 4. `falsche-wiese-warnung-ki-vo`

**Fokus:** Nutzer fragt eine KI-VO-Frage die eigentlich unter DSGVO Produkthaftung MDR oder Maschinenverordnung faellt. Warnt vor typischen Rechtsgebiets-Verwechslungen KI-VO versus DSGVO versus Produkthaftungsrichtlinie versus Medizinprodukteverordnung versus Maschinenverordnung versus Cyber Resilience Act. Prüfraster: Schluesselmerkmale zur Abgrenzung der Regelwerke. Output: Orientierungsmemo mit konkretem Verweis auf das tatsaechlich einschlaegige Recht. Abgrenzung zu verhältnis-zu-anderen-unionsrechtsakten (systematische Kumulationsprüfung) und territorialer-anwendungsbereich-art-2.

# Warnung: Falsche Wiese — Verwechslung der Rechtsgebiete

## Zweck

Ein häufiger Fehler in der Praxis besteht darin, die KI-VO auf Sachverhalte anzuwenden, die tatsächlich von einem anderen Rechtsgebiet erfasst werden — oder umgekehrt: KI-spezifische Pflichten zu übersehen, weil der Nutzer glaubt, DSGVO-Konformität genüge. Dieser Skill klärt die Abgrenzung.

## Verwechslungsfall 1 — KI-VO versus DSGVO

**Häufiges Szenario:** Nutzer fragt nach Datenschutzpflichten beim Einsatz eines KI-Systems.

**Richtigstellung:**
- Die DSGVO (Verordnung (EU) 2016/679) regelt den Schutz personenbezogener Daten und gilt für jede Verarbeitung personenbezogener Daten, unabhängig davon, ob KI eingesetzt wird.
- Die KI-VO (Verordnung (EU) 2024/1689) regelt zusätzliche Anforderungen an KI-Systeme als solche: Risikoklassen, Konformitätsbewertung, Transparenzpflichten, menschliche Aufsicht.
- Beide Regelwerke können gleichzeitig gelten und ergänzen sich. DSGVO-Konformität ersetzt keine KI-VO-Konformität.
- Praktische Schnittstelle: Art. 27 KI-VO (Grundrechte-Folgenabschätzung für Betreiber) ist eng verzahnt mit Datenschutz-Folgenabschätzung nach Art. 35 DSGVO.

**Routing:** Wenn primär Datenschutzfragen bestehen → anderes Plugin (Datenschutzrecht). Wenn KI-spezifische Pflichten geprüft werden sollen → weiter in diesem Workflow.

## Verwechslungsfall 2 — KI-VO versus Produkthaftungsrichtlinie

**Häufiges Szenario:** Nutzer fragt nach Haftung für Schäden durch ein KI-System.

**Richtigstellung:**
- Die KI-VO ist keine Haftungsregelung. Sie begründet öffentlich-rechtliche Pflichten und Sanktionen, aber keine privatrechtlichen Schadensersatzansprüche.
- Die neue EU-Produkthaftungsrichtlinie (2024/2853) und die KI-Haftungsrichtlinie (Entwurf) betreffen Haftungsfragen. Diese sind vom KI-VO-zu trennen.
- Compliance mit der KI-VO kann jedoch haftungsmindernd wirken, wenn ein Verstoß zugleich eine Sorgfaltspflichtverletzung darstellt.

**Routing:** Haftungsfragen → Fachanwalt IT-Recht / Produkthaftung; KI-VO-Compliance → dieser Workflow.

## Verwechslungsfall 3 — KI-VO versus Medizinprodukteverordnung (MDR/IVDR)

**Häufiges Szenario:** KI-System in einem Medizinprodukt oder für Diagnose/Behandlung.

**Richtigstellung:**
- Die MDR (Verordnung (EU) 2017/745) und IVDR (Verordnung (EU) 2017/746) gelten für Medizinprodukte und In-vitro-Diagnostika.
- Ein KI-System, das in einem Medizinprodukt eingesetzt wird, kann gleichzeitig der MDR und der KI-VO unterliegen.
- Für KI-Systeme, die als Sicherheitsbauteil eines Medizinprodukts eingestuft werden, gilt Art. 6 Abs. 1 KI-VO i.V.m. Anhang I Nr. 1 KI-VO (MDR ist dort gelistet).
- Konformitätsbewertung nach MDR durch benannte Stelle kann teilweise auf KI-VO-Anforderungen angerechnet werden (Art. 43 Abs. 3 KI-VO).

**Routing:** Medizinprodukt-Konformität → Fachanwalt Medizinrecht; KI-VO-Schicht → weiter in diesem Workflow.

## Verwechslungsfall 4 — KI-VO versus Maschinenverordnung

**Häufiges Szenario:** KI-System in einer Maschine (Roboter, Produktionsanlage, Fahrzeug).

**Richtigstellung:**
- Die Maschinenverordnung (Verordnung (EU) 2023/1230) regelt die Sicherheit von Maschinen.
- KI-Systeme in Maschinen können gleichzeitig der KI-VO unterliegen, wenn sie Sicherheitsbauteile sind.
- Anhang I Nr. 7 KI-VO listet die Maschinenverordnung als relevanten Unionsrechtsakt; damit kann das KI-System als Hochrisiko nach Art. 6 Abs. 1 KI-VO einzustufen sein.

## Verwechslungsfall 5 — KI-VO versus Cyber Resilience Act

**Häufiges Szenario:** Nutzer fragt nach Cybersicherheitspflichten für KI-Produkte.

**Richtigstellung:**
- Der Cyber Resilience Act (Verordnung (EU) 2024/2847) regelt Cybersicherheitsanforderungen für Produkte mit digitalen Elementen.
- Für KI-Systeme, die unter den Cyber Resilience Act fallen, können beide Rechtsakte gleichzeitig gelten.
- Art. 15 KI-VO (Genauigkeit, Robustheit, Cybersicherheit für Hochrisiko-KI) greift unabhängig vom Cyber Resilience Act.

## Checkliste — Welches Recht gilt?

| Situation | Relevantes Recht |
|---|---|
| Datenschutzverletzung durch KI | DSGVO + ggf. KI-VO |
| Schaden durch KI-Fehler | Produkthaftung + ggf. KI-VO |
| KI in Medizinprodukt | MDR/IVDR + KI-VO |
| KI in Maschine/Roboter | Maschinenverordnung + KI-VO |
| KI-Produktsicherheit allgemein | Produktsicherheits-VO + KI-VO |
| KI-spezifische Risikopflichten | KI-VO primär |

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
PRUEFERGEBNIS — FALSCHE WIESE WARNUNG KI VO
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 6 Rn. 10]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
