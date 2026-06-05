---
name: inventar-kontrollen-konformitaetsbewertung
description: "Inventar Kontrollen Konformitaetsbewertung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Inventar Kontrollen Konformitaetsbewertung

## Arbeitsbereich

Dieser Skill bündelt 3 sachlich verwandte Arbeitsschritte rund um **Inventar Kontrollen Konformitaetsbewertung** im Plugin KI-Governance. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-ki-inventar-governance-und-kontrollen` | KI-Inventar, Governance und Kontrollen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-konformitaetsbewertung-red-team-und-qualitaetskontrolle` | Konformitaetsbewertung: Red-Team und Qualitätskontrolle im Plugin ki governance; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-marketing-mandantenkommunikation-entscheidungsvorlage` | Marketing: Mandantenkommunikation und Entscheidungsvorlage im Plugin ki governance; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin KI-Governance gilt für **Inventar Kontrollen Konformitaetsbewertung**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `spezial-ki-inventar-governance-und-kontrollen`

**Fokus:** KI-Inventar, Governance und Kontrollen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output.

# KI-Inventar, Governance und Kontrollen

## Aufgabe
Dieser Skill ersetzt einen zu groben Spezial-Slot durch einen konkreten Fachim Plugin `ki-governance`. Kontext des Plugins: EU-KI-VO + DSGVO – Use-Case-Triage, KI-Inventar, AIA/DPIA, Vendor-Review, Drift-Monitoring der KI-Richtlinie.

Er arbeitet nicht lexikalisch, sondern fallbezogen: Er trennt zuerst Rollen, Ziel, Fristen, Zuständigkeiten und Belege, prüft dann die fachlichen Weichen und liefert ein Ergebnis, mit dem weitergearbeitet werden kann.

## Einstieg
Wenn Material vorliegt, nutze es zuerst. Frage nur nach, was für die nächste Entscheidung fehlt:

1. Wer handelt in welcher Rolle und gegen wen?
2. Welches praktische Ziel soll erreicht werden?
3. Welche Fristen, Termine, Zustellungen, Schwellenwerte oder Sanktionen stehen im Raum?
4. Welche Unterlagen, Daten, Registerauszüge, Bescheide, Verträge, Screenshots oder sonstigen Belege liegen vor?
5. Soll der Output intern, für Mandantschaft, Behörde, Gericht, Gegnerseite oder Gremium formuliert werden?

## Arbeitsworkflow
1. **Sortieren:** Sachverhalt, Dokumente und offene Punkte in eine knappe Fallmatrix bringen.
2. **Rechtsrahmen:** Einschlägige Normen, Zuständigkeiten, Verfahren, Fristen und formelle Anforderungen live prüfen, soweit Aktualität tragend ist.
3. **Materielle Weichen:** Die Kernfragen zu **KI-Inventar, Governance und Kontrollen** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
4. **Risikoampel:** Ergebnis in Grün/Gelb/Rot mit Begründung, Unsicherheiten und Beweisbedarf einordnen.
5. **Anschluss:** Passende weitere Skills desselben Plugins vorschlagen, wenn Spezialprüfung, Schriftsatz, Tabelle, Brief oder Verhandlungsstrategie sinnvoll ist.

## Pflichtelemente KI-Inventar
Das Inventar ist Voraussetzung für jede AI-Governance und Rückgrat der KI-VO-Konformität (Art. 12, 16, 49, 72 KI-VO):

- **Identifikation**: Use-Case-ID, interner Eigentümer, Geschäftsbereich, Status (Pilot, Produktion, abgeschaltet).
- **System-/Modellinformation**: Anbieter, Produktname, Version, Modellfamilie (z. B. GPAI gem. Art. 3 Nr. 63 KI-VO), Hosting-Region, Datenresidenz.
- **Rollenzuordnung**: Anbieter Art. 3 Nr. 3, Betreiber Art. 3 Nr. 4, Importeur Art. 3 Nr. 6, Händler Art. 3 Nr. 7. Wechselt die Rolle bei substantieller Modifikation (Art. 25 KI-VO)?
- **Risikoklassifizierung**: Verboten (Art. 5) / Hochrisiko (Anhang III) / Begrenztes Risiko (Art. 50) / Minimal.
- **Datenkategorien**: personenbezogen (Art. 4 Nr. 1 DSGVO), besondere Kategorien (Art. 9), Mandantengeheimnis, IP.
- **DSGVO-Status**: Rechtsgrundlage Art. 6, DSFA Art. 35 abgeschlossen, AVV Art. 28 abgeschlossen.
- **KI-VO-Status**: Risikomanagementsystem Art. 9, Datenqualität Art. 10, Technische Dokumentation Art. 11, Logging Art. 12, Transparenz Art. 13, Aufsicht Art. 14, Genauigkeit/Cyber Art. 15, Konformitätsbewertung Art. 43.

## Kontroll-Architektur
- **Governance-Komitee**: AI Officer, Datenschutzbeauftragte/r, CISO, Compliance, Fachbereich.
- **Three Lines of Defense**: Fachbereich → Compliance/Datenschutz → Interne Revision.
- **Lebenszyklus-Reviews**: Onboarding, jährlicher Review, anlassbezogene Reklassifizierung, Sunset/Off-Boarding mit Datenlöschung.
- **Vorfallmanagement**: Vorfälle Art. 73 KI-VO (Marktüberwachung-Meldung bei Hochrisiko), DSGVO Art. 33/34, NIS-2 falls einschlägig.

## Schnittstelle Kanzlei-Praxis
KI-Inventar ist auch für Berufsträger relevant (§§ 43e BRAO / 62a StBerG / 50a WPO): pro Tool dokumentieren, ob Mandantendaten verarbeitet werden, ob Verpflichtungserklärung gem. § 203 Abs. 4 StGB vorliegt, ob Trainingsausschluss vereinbart ist.

## Trade-off
Schlankes Inventar (Tabelle) ist schnell aufgesetzt, aber ohne Lebenszyklus- und Eskalations-Hooks substanzarm. Vollständige GRC-Tool-Integration (z. B. mit AIA/DPIA-Workflow) ist aufwendig, schafft aber Auditierbarkeit. Pragmatischer Mittelweg: Tabelle + Trigger-Mails bei Klassifizierungsänderung oder neuem Geltungstermin der KI-VO-Stufen.

## Output-Standard
- Kurzbild in fünf Sätzen: Lage, Ziel, Frist, Risiko, nächster Schritt.
- Prüfmatrix mit Punkt, Norm/Quelle, Tatsachen, Beleg, Bewertung, To-do.
- Konkreter Textbaustein oder Arbeitsprodukt passend zur Lage: Memo, Mandantenbrief, Behörden-/Gerichtsschreiben, Checkliste, Tabelle oder Verhandlungsagenda.
- Keine Scheingenauigkeit: Annahmen, Lücken und Live-Check-Bedarf offen markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwenden, wenn die Nutzerin oder der Nutzer den Text selbst bereitstellt; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `spezial-konformitaetsbewertung-red-team-und-qualitaetskontrolle`

**Fokus:** Konformitaetsbewertung: Red-Team und Qualitätskontrolle im Plugin ki governance; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Konformitaetsbewertung: Red-Team und Qualitätskontrolle

## Spezialwissen: Konformitaetsbewertung: Red-Team und Qualitätskontrolle
- **Spezialgegenstand:** Konformitaetsbewertung: Red-Team und Qualitätskontrolle / konformitaetsbewertung red team und qualitaetskontrolle. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EU, KI, VO, DSGVO, AIA, DPIA.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Konformitätsbewertung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Konformitätsbewertungsverfahren KI-VO (Art. 43)
- **Anhang VI — Interne Kontrolle**: Standardverfahren für die meisten Hochrisiko-KI-Systeme nach Anhang III, sofern harmonisierte Normen vollständig angewendet werden.
- **Anhang VII — Bewertung mit benannter Stelle**: für biometrische Identifikationssysteme nach Anhang III Nr. 1 lit. a, wenn keine harmonisierten Normen vollständig angewendet werden — oder freiwillig.
- **Konformitätsbewertung im Zuge anderer Unionsrechtsakte**: Wenn das KI-System Sicherheitsbauteil eines Produkts nach Anhang I ist (Medizinprodukt MDR, Maschine MaschinenVO etc.), wird die KI-VO-Bewertung in die bestehende Konformitätsbewertung integriert (Art. 43 Abs. 3).

## Pflichtdokumentation
- **Technische Dokumentation** Art. 11 i. V. m. Anhang IV: Systembeschreibung, Designspezifikationen, Trainingsdatenbeschreibung, Risikomanagement, Monitoring, Cybersicherheit.
- **Logging-Architektur** Art. 12: Aufzeichnungen über Lebenszyklus, Zweck-Erreichung, Identifikation problematischer Verhaltensweisen.
- **EU-Konformitätserklärung** Art. 47 i. V. m. Anhang V: 10 Jahre Aufbewahrung, Inhalt vorgeschrieben.
- **CE-Kennzeichnung** Art. 48 und **EU-Datenbankregistrierung** Art. 49 / 71 (Anhang VIII).

## Red-Team-Prüfungen
- **Robustheit**: adversariale Beispiele, Eingabestörungen, Edge Cases.
- **Bias / Fairness**: Tests über Untergruppen (Geschlecht, Alter, ethnische Herkunft, Region), Disparate-Impact-Analyse.
- **Cybersicherheit**: Prompt-Injection (bei LLM-basierten Systemen), Model Inversion, Membership Inference.
- **Datenleckage**: Aus Antworten rekonstruierbare Trainingsdaten (insb. bei Foundation Models).

## Qualitätskontrolle
- **Pre-Deployment**: vollständiger Konformitätsbewertungsbericht, abgenommen durch Compliance.
- **Pilotphase**: vorgesehene Stichprobe mit verstärktem Logging und Human Override.
- **Produktion**: Monitoring nach Art. 72 KI-VO (Marktbeobachtung durch Anbieter), Vorfallsmeldung nach Art. 73.
- **Substantielle Änderung**: bei Modellaktualisierung mit Performance-Verschiebung neue Bewertung nach Art. 43 Abs. 4.

## Trade-off
Interne Kontrolle (Anhang VI) ist günstiger und schneller, scheitert aber bei nicht-harmonisierten Aspekten. Beauftragung benannter Stelle (Anhang VII) gibt Rechtssicherheit, kostet Zeit (Wartezeit, Auditdurchläufe) und Geld; ist für Markteintritt sensibler Systeme aber empfehlenswert. Hybride Strategie: Anhang VI mit zusätzlichem freiwilligem externem Audit zur Vertrauensbildung.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 3. `spezial-marketing-mandantenkommunikation-entscheidungsvorlage`

**Fokus:** Marketing: Mandantenkommunikation und Entscheidungsvorlage im Plugin ki governance; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Marketing: Mandantenkommunikation und Entscheidungsvorlage

## Spezialwissen: Marketing: Mandantenkommunikation und Entscheidungsvorlage
- **Spezialgegenstand:** Marketing: Mandantenkommunikation und Entscheidungsvorlage / marketing mandantenkommunikation entscheidungsvorlage. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EU, KI, VO, DSGVO, AIA, DPIA.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Marketing-KI** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Mandantenkommunikation Marketing-KI
- **Sachstand:** Welches Marketing-Tool nutzt KI? Welche Funktion (Personalisierung, Predictive Targeting, Lookalike, dynamische Anzeigen, Chatbot)?
- **Rechtsrahmen:**
 - **DSGVO**: Art. 6 Rechtsgrundlage (oft Einwilligung Art. 6 Abs. 1 lit. a oder berechtigtes Interesse Art. 6 Abs. 1 lit. f); Art. 22 bei automatisierten Entscheidungen.
 - **TDDDG § 25**: Einwilligung bei Endgerätezugriff (Cookies, Tracking-Pixel) — zwingend vor der Verarbeitung.
 - **KI-VO Art. 50**: Transparenzpflicht bei KI-generierten Inhalten (z. B. Deepfakes), bei Chatbots klare Information.
 - **UWG §§ 5, 5a**: Irreführungsverbot — KI-Empfehlungen müssen als solche erkennbar sein.
- **Risiken:** Bußgelder DSGVO (4 %), KI-VO (3-7 %), UWG-Abmahnungen.
- **Empfehlung:** Transparenz-First-Strategie; klare Kennzeichnung, dokumentierte LIA, Opt-Out-Mechanismus.

## Praxis-Tipp
KI-generierte Werbung muss nach Art. 50 KI-VO als solche gekennzeichnet sein — sonst riskieren Marketingteams sowohl KI-VO-Sanktion als auch UWG-Abmahnung wegen Irreführung. Empfehlung: standardisierter Kennzeichnungs-im DAM/CMS einrichten, nicht ad hoc.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
