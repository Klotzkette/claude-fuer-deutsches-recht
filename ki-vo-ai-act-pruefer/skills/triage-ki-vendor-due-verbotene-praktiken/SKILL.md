---
name: triage-ki-vendor-due-verbotene-praktiken
description: "Triage KI Vendor DUE Verbotene Praktiken: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Triage KI Vendor DUE Verbotene Praktiken

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Triage KI Vendor DUE Verbotene Praktiken** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `triage-ki-vo-vorpruefung` | Nutzer kommt mit unklarer KI-VO-Frage oder möglicherweise betroffener Software und fragt: Wie starte ich die KI-VO-Prüfung? Eingangs-Triage-Skill. Prüfraster: Erfassung ob eigene Softwareentwicklung fremder Dienst Produktintegration oder Beratungsanfrage. Eingangsfragen zu Systemart Branche Einsatzgebiet Rolle des Anfragenden. Output: Weiterleitung zum naechsten passenden Skill entscheidungsbaum-ki-vo-gesamt-oder risikoklassen-uebersicht-und-triage. Warnt vor typischen Fehlzuordnungen. Abgrenzung zu liegt-ki-system-vor-art-3-nr-1 (Vollprüfung KI-System-Definition). |
| `vendor-due-diligence-ai-act-beschaffung` | KI-Beschaffung und Vendor Due Diligence: Anbieterrolle, Hochrisiko, GPAI, Datenschutz, Urheberrecht, Security, Unterauftragnehmer, Audit-Rechte, Exit, Incident-Meldung und Vertragsanlagen fuer Einkauf und Legal. |
| `verbotene-praktiken-art-5` | Unternehmen prüft ob ein KI-Einsatz in den Bereich der absolut verbotenen KI-Praktiken faellt. Art. 5 KI-VO Verbotskatalog. Prüfraster: alle acht verbotenen Praktiken subliminale Techniken Vulnerabilitaetsausnutzung Social Scoring Predictive Policing biometrisches Categorisierung Echtzeit-RBI öffentlicher Raum Emotionserkennung Arbeitsplatz Untargeted Scraping Gesichtsdatenbanken. Output: Entscheidungsbaum je Verbotspraktik mit Begründung. Abgrenzung zu hochrisiko-art-6-abs-2-anhang-iii (Hochrisiko nicht verboten aber reguliert) und sachlicher-ausschluss-art-2-abs-3-bis-12. |
| `verhaeltnis-zu-anderen-unionsrechtsakten` | Anwalt oder Compliance-Beauftragter fragt: Gilt neben der KI-VO noch ein anderes EU-Gesetz für das gleiche System und wie interagieren die Pflichten? Art. 2 Abs. 2 KI-VO Verhältnis zu anderen Rechtsakten. Prüfraster: DSGVO Maschinenverordnung Produktsicherheits-VO MDR IVDR NIS-2 Cyber Resilience Act Kumulationseffekte Spezialitaet Verweisregelungen Doppelpflichten. Output: Normen-Konflikt-Matrix und Handlungsempfehlung. Abgrenzung zu falsche-wiese-warnung-ki-vo (Abgrenzung bei klaren Verwechslungen) und territorialer-anwendungsbereich-art-2. |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Triage KI Vendor DUE Verbotene Praktiken**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `triage-ki-vo-vorpruefung`

**Fokus:** Nutzer kommt mit unklarer KI-VO-Frage oder möglicherweise betroffener Software und fragt: Wie starte ich die KI-VO-Prüfung? Eingangs-Triage-Skill. Prüfraster: Erfassung ob eigene Softwareentwicklung fremder Dienst Produktintegration oder Beratungsanfrage. Eingangsfragen zu Systemart Branche Einsatzgebiet Rolle des Anfragenden. Output: Weiterleitung zum naechsten passenden Skill entscheidungsbaum-ki-vo-gesamt-oder risikoklassen-uebersicht-und-triage. Warnt vor typischen Fehlzuordnungen. Abgrenzung zu liegt-ki-system-vor-art-3-nr-1 (Vollprüfung KI-System-Definition).

# Triage: KI-VO-Vorprüfung — Was prüft der Nutzer?

## Zweck

Dieser Skill ist der Einstiegspunkt in den vollständigen Prüfungsder Verordnung (EU) 2024/1689 (KI-VO). Bevor Risikoklassen, Pflichten oder Verbote geprüft werden können, muss das System verstehen, welchen Sachverhalt der Nutzer einbringt und welche Rolle er in Bezug auf das fragliche System einnimmt.

## Eingangsfragen

Das System stellt folgende Fragen der Reihe nach:

**Frage 1 — Art des Gegenstands**

Was wird geprüft?
- (A) Ich habe selbst eine Software oder ein System entwickelt oder lasse es entwickeln.
- (B) Ich nutze einen fremden KI-Dienst (Cloud-Dienst, Drittanbieter-Produkt, API) in meinem Betrieb.
- (C) Ich integriere ein KI-System oder KI-Komponente in ein eigenes Produkt.
- (D) Ich berate Mandanten zu einem KI-System oder einer KI-VO-Fragestellung.
- (E) Ich weiß noch nicht genau — bitte führe mich.

**Frage 2 — Beschreibung des Systems**

Bitte beschreiben Sie in Stichpunkten:
- Was tut das System? (Beispiele: Bilderkennung, Textgenerierung, Scoring, Empfehlung, Entscheidungsunterstützung)
- In welchem Bereich wird es eingesetzt? (Beispiele: Personalwesen, Medizin, Kredit, Strafverfolgung, Bildung, allgemeine Nutzung)
- Wer sind die betroffenen Personen? (Beispiele: Bewerber, Patienten, Kreditnehmer, Bürger)

**Frage 3 — Standort und Markt**

- Wo soll das System eingesetzt werden? (EU / außerhalb EU / unklar)
- Werden Ausgaben des Systems in der EU verwendet, auch wenn das System außerhalb betrieben wird?

## Plausibilitätsprüfung

Das System prüft auf Basis der Eingaben:
- Handelt es sich möglicherweise gar nicht um ein KI-System im Sinne von Art. 3 Nr. 1 KI-VO? → Weiterleitung zu `liegt-ki-system-vor-art-3-nr-1`
- Liegt ein offensichtlicher Ausschluss nach Art. 2 Abs. 3 bis 12 vor (Militär, rein persönliche Nutzung)? → Weiterleitung zu `sachlicher-ausschluss-art-2-abs-3-bis-12`
- Verwechselt der Nutzer die KI-VO mit einem anderen Rechtsgebiet (DSGVO, Produkthaftung)? → Weiterleitung zu `falsche-wiese-warnung-ki-vo`

## Routing-Logik

| Antwort | Nächster Skill |
|---|---|
| Variante A oder C | `liegt-ki-system-vor-art-3-nr-1` → `rolle-anbieter-pruefen-art-3-nr-3` |
| Variante B | `liegt-ki-system-vor-art-3-nr-1` → `rolle-betreiber-pruefen-art-3-nr-4` |
| Variante D | `mandatsabbruch-empfehlung-komplexe-faelle` (Hinweis auf Grenzen des Mechanik-Workflows) |
| Variante E | Rückfragen zu Beschreibung, dann Routing nach Sachverhalt |

## Wichtige Einschränkungen

- Das System akzeptiert keine fiktiven Testdaten oder Mustersachverhalte.
- Unvollständige Sachverhalte führen zu unvollständigen Ergebnissen — das System weist ausdrücklich darauf hin.
- Dieser ist ein mechanisches Prüfinstrument, kein juristisches Gutachten.

## Warnblock

**Achtung — Keine Rechtsberatung:**
Dieser Skill erfasst nur, was der Nutzer mitteilt. Er kann nicht prüfen, ob die Sachverhaltsdarstellung vollständig oder korrekt ist. Alle Ergebnisse stehen unter dem Vorbehalt der vom Nutzer behaupteten Tatsachen.

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
PRUEFERGEBNIS — TRIAGE KI VO VORPRUEFUNG
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 2 Rn. 1]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 2. `vendor-due-diligence-ai-act-beschaffung`

**Fokus:** KI-Beschaffung und Vendor Due Diligence: Anbieterrolle, Hochrisiko, GPAI, Datenschutz, Urheberrecht, Security, Unterauftragnehmer, Audit-Rechte, Exit, Incident-Meldung und Vertragsanlagen fuer Einkauf und Legal.

# KI-Beschaffung: Vendor Due Diligence

## Ziel

Vor Einkauf eines KI-Tools muss klar sein, welche Pflichten beim Anbieter liegen, welche beim Betreiber landen und welche Nachweise vertraglich geliefert werden.

## Fragenkatalog

1. Ist das Produkt ein KI-System nach Art. 3 Nr. 1 KI-VO?
2. Welche Zweckbestimmung behauptet der Anbieter?
3. Hochrisiko nach Art. 6/Anhang III oder nur allgemeines Tool?
4. Nutzt das Produkt GPAI oder ein eigenes Modell?
5. Welche Dokumentation nach Art. 11, 13, 26, 53 wird geliefert?
6. Wie werden Logs, Fehler, Incidents und Modelländerungen gemeldet?
7. Welche Daten werden gespeichert, trainiert, weitergegeben?
8. Welche Rechte bestehen an Input, Output und Trainingsdaten?
9. Welche Audit- und Kündigungsrechte gibt es?

## Vertragsanlagen

- AI Act Compliance Schedule.
- Data Processing Agreement.
- Security Annex.
- Model Change Notice.
- Incident Reporting Annex.
- Acceptable Use und Off-label-Prohibition.

## Output

Ein Einkaufsvermerk mit Go/No-Go, Nachforderungen und Redlines.

## 3. `verbotene-praktiken-art-5`

**Fokus:** Unternehmen prüft ob ein KI-Einsatz in den Bereich der absolut verbotenen KI-Praktiken faellt. Art. 5 KI-VO Verbotskatalog. Prüfraster: alle acht verbotenen Praktiken subliminale Techniken Vulnerabilitaetsausnutzung Social Scoring Predictive Policing biometrisches Categorisierung Echtzeit-RBI öffentlicher Raum Emotionserkennung Arbeitsplatz Untargeted Scraping Gesichtsdatenbanken. Output: Entscheidungsbaum je Verbotspraktik mit Begründung. Abgrenzung zu hochrisiko-art-6-abs-2-anhang-iii (Hochrisiko nicht verboten aber reguliert) und sachlicher-ausschluss-art-2-abs-3-bis-12.

# Verbotene Praktiken — Art. 5 KI-VO (Entscheidungsbaum)

## Zweck

Art. 5 KI-VO enthält einen abschließenden Katalog von acht verbotenen KI-Praktiken. Diese Verbote sind seit dem 2. Februar 2025 anwendbar und mit den höchsten Sanktionen bewehrt (bis zu 35 Mio EUR oder sieben Prozent des weltweiten Jahresumsatzes). Dieser Skill prüft alle acht Verbotstatbestände systematisch.

## Verbotene Praktik 1 — Subliminale und manipulative Techniken (Art. 5 Abs. 1 lit. a KI-VO)

**Tatbestand:** KI-Systeme, die subliminale Techniken einsetzen, die einer Person nicht bewusst sind, oder täuschende Techniken, um die Autonomie, Entscheidungsfindung oder freie Meinungsbildung einer Person durch das Verzerren der Wahrnehmung zu unterlaufen.

**Prüffragen:**
- Beeinflusst das System Verhalten oder Wahrnehmung unterhalb der bewussten Wahrnehmungsschwelle?
- Nutzt es psychologische Manipulationstechniken, die auf Verzerrung oder Täuschung ausgerichtet sind?
- Führt die Manipulation zu einer dem Interesse der Person oder Dritter abträglichen Handlung?

**Auslegungshinweis:** Der Tatbestand setzt sowohl eine subliminale oder täuschende Technik als auch einen (potenzialem) Schaden voraus. Übliche Empfehlungssysteme fallen nicht darunter, solange sie keine manipulativen Verzerrungen einsetzen.

**Ergebnis:** Wenn alle Merkmale erfüllt → verboten; kein Rechtfertigungsgrund möglich.

## Verbotene Praktik 2 — Ausnutzung von Schwächezuständen (Art. 5 Abs. 1 lit. b KI-VO)

**Tatbestand:** KI-Systeme, die Schwächezustände oder besondere Schutzbedürftigkeit bestimmter natürlicher Personen oder Gruppen (Alter, Behinderung, soziale oder wirtschaftliche Situation) ausnutzen, um deren Verhalten auf eine Weise zu beeinflussen, die ihren Interessen abträglich ist.

**Prüffragen:**
- Richtet sich das System an besonders schutzbedürftige Gruppen (Kinder, ältere Menschen, Personen mit Behinderung, wirtschaftlich Schwache)?
- Nutzt es diese Schutzbedürftigkeit gezielt aus?
- Ist das resultierende Verhalten den Interessen der Zielpersonen abträglich?

## Verbotene Praktik 3 — Social Scoring (Art. 5 Abs. 1 lit. c KI-VO)

**Tatbestand:** Bewertungssysteme, die öffentliche Behörden oder in ihrem Auftrag handelnde Stellen einsetzen, um das soziale Verhalten natürlicher Personen auf der Grundlage von KI-generierter Einstufung zu klassifizieren und zu bewerten, wenn diese Einstufung zu einer Benachteiligung führt, die außer Verhältnis zum Verhalten steht oder in einem anderen Lebensbereich erfolgt.

**Prüffragen:**
- Handelt es sich um eine öffentliche Behörde oder ein im öffentlichen Auftrag handelndes Unternehmen?
- Klassifiziert das System Personen auf der Basis sozialen Verhaltens?
- Führt die Klassifikation zu Benachteiligungen in anderen als dem ursprünglichen Kontext?

## Verbotene Praktik 4 — Predictive Policing (Art. 5 Abs. 1 lit. d KI-VO)

**Tatbestand:** Risikoabschätzungssysteme in der Strafverfolgung, die ausschließlich auf der Grundlage von Profiling oder der Bewertung von Persönlichkeitsmerkmalen und -zügen ohne individuelle Hinweise auf eine Beteiligung an einer Straftat Vorhersagen über das Begehen zukünftiger Straftaten treffen.

**Prüffragen:**
- Wird das System von Strafverfolgungsbehörden zur Vorhersage von Straftaten eingesetzt?
- Basiert die Vorhersage ausschließlich auf Profiling oder Persönlichkeitsbewertung?
- Gibt es keine individuellen Hinweise auf tatsächliche Beteiligung?

**Auslegungshinweis:** Systeme, die konkrete Hinweise auf eine Person verarbeiten, sind nicht automatisch verboten; die Grenze liegt beim reinen Persönlichkeitsprofiling ohne individuelle Anhaltspunkte.

## Verbotene Praktik 5 — Untargeted Facial Image Scraping (Art. 5 Abs. 1 lit. e KI-VO)

**Tatbestand:** Erstellung oder Erweiterung von Gesichtserkennungsdatenbanken durch ungezielte Auslese von Gesichtsbildern aus dem Internet oder aus Videoüberwachungsaufnahmen.

**Prüffragen:**
- Werden Gesichtsbilder aus dem Internet oder aus Überwachungskameras ungezielt gesammelt?
- Dient dies dem Aufbau oder der Erweiterung einer Datenbank zur Gesichtserkennung?

## Verbotene Praktik 6 — Emotionserkennung an Arbeitsplatz und Bildungseinrichtungen (Art. 5 Abs. 1 lit. f KI-VO)

**Tatbestand:** Emotionserkennungssysteme am Arbeitsplatz oder in Bildungseinrichtungen.

**Prüffragen:**
- Erkennt das System Emotionen natürlicher Personen?
- Wird es am Arbeitsplatz oder in Schulen, Universitäten oder anderen Bildungseinrichtungen eingesetzt?

**Ausnahmen:** Systeme, die aus medizinischen oder sicherheitsbezogenen Gründen eingesetzt werden, können unter engen Voraussetzungen ausgenommen sein.

## Verbotene Praktik 7 — Biometrische Kategorisierung nach sensiblen Merkmalen (Art. 5 Abs. 1 lit. g KI-VO)

**Tatbestand:** Biometrische Systeme, die natürliche Personen anhand biometrischer Daten nach ihrer Rasse, politischen Meinung, Gewerkschaftszugehörigkeit, Religionszugehörigkeit, sexuellen Orientierung oder anderen in Art. 9 Abs. 1 DSGVO genannten Merkmalen kategorisieren.

## Verbotene Praktik 8 — Echtzeit-Biometrische Fernidentifikation im öffentlichen Raum (Art. 5 Abs. 1 lit. h KI-VO)

**Tatbestand:** Einsatz biometrischer Echtzeit-Fernidentifikationssysteme in öffentlich zugänglichen Bereichen durch Strafverfolgungsbehörden, außer in den eng begrenzten Ausnahmefällen nach Art. 5 Abs. 2 KI-VO (z.B. Suche nach vermissten Personen, Terrorismusprävention bei konkreter Gefahr, Fahndung nach bestimmten Tätern).

**Prüffragen:**
- Ist der Betreiber eine Strafverfolgungsbehörde?
- Wird die biometrische Identifikation in Echtzeit in öffentlich zugänglichen Räumen durchgeführt?
- Liegt keine der Ausnahmen nach Art. 5 Abs. 2 KI-VO vor?

## Rechtsfolgen bei Verstoß

- Bußgeld bis zu 35 Mio EUR oder — sofern der Täter ein Unternehmen ist — bis zu sieben Prozent des gesamten weltweiten Jahresumsatzes des vorausgegangenen Geschäftsjahres, je nachdem welcher Betrag höher ist (Art. 99 Abs. 3 KI-VO).
- Keine Heilungs- oder Anpassungsmöglichkeit: verbotene Praktiken sind komplett einzustellen.
- Strafbarkeit nach nationalem Recht nicht ausgeschlossen.

## Faktische Updates (Stand 05/2026)

- **02.02.2025 — Anwendung Art. 5 KI-VO:** Die acht verbotenen Praktiken sind seit dem 02.02.2025 verbindlich. Quelle: VO (EU) 2024/1689, Art. 113 lit. a — eur-lex.europa.eu/eli/reg/2024/1689/oj.
- **Kommissions-Leitlinien zu Art. 5:** Die EU-Kommission hat Anfang 2025 Leitlinien zu Art. 5 KI-VO veroeffentlicht, die die Tatbestandsmerkmale fuer Anwender konkretisieren (u.a. Begriff "subliminale Technik", "Vulnerabilitaetsausnutzung", Abgrenzung zu zulaessigem Profiling). Stand und aktuelle Fassung live pruefen ueber digital-strategy.ec.europa.eu/en/policies/ai-act.
- **02.08.2025 — Sanktionen wirksam:** Art. 99 KI-VO ist seit dem 02.08.2025 vollumfaenglich anwendbar; Marktueberwachungsbehoerden in den Mitgliedstaaten koennen Bussgeldverfahren einleiten.

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Die KI-VO ist in Auslegung und Konkretisierung dynamisch; Leitlinien der Kommission und Durchführungsrechtsakte sind laufend zu beobachten.

## Aktuelle Rechtsprechung (v14.2)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)
- Art. 5 Abs. 1 lit. a KI-VO — subliminale und manipulative Techniken
- Art. 5 Abs. 1 lit. b KI-VO — Ausnutzung von Vulnerabilitaeten
- Art. 5 Abs. 1 lit. c KI-VO — Social Scoring
- Art. 5 Abs. 1 lit. d KI-VO — Predictive Policing
- Art. 5 Abs. 1 lit. e KI-VO — Untargeted Scraping biometrischer Daten
- Art. 5 Abs. 1 lit. f KI-VO — Emotionserkennung am Arbeitsplatz / Bildung
- Art. 5 Abs. 1 lit. g KI-VO — biometrische Kategorisierung nach geschuetzten Merkmalen
- Art. 5 Abs. 1 lit. h KI-VO — Echtzeit-Biometrie-Fernidentifizierung oeffentlicher Raum
- Art. 99 Abs. 3 KI-VO — Bussgelder bis 35 Mio. EUR / 7 % weltweiter Jahresumsatz

## Triage zu Beginn
1. Welche der acht verbotenen Praktiken (lit. a-h) koennte potentiell einschlaegig sein?
2. Sind staatliche oder private Akteure beteiligt (Social Scoring lit. c gilt fuer beide)?
3. Richten sich Techniken an besonders schutzbeduertige Personen (Vulnerabilitaet lit. b)?
4. Sind biometrische Daten oder Emotionserkennung beteiligt (lit. f, g, h)?
5. Gibt es Ausnahmen nach Art. 5 Abs. 2-8 KI-VO (Echtzeit-RBI in Ausnahmefaellen)?

## Output-Template — Verbotene-Praktiken-Pruefung
**Adressat:** Pruefer / Rechtsberater — Tonfall: entscheidungsbaum-strukturiert
```
VERBOTENE-PRAKTIKEN-PRUEFUNG ART. 5 KI-VO
[DATUM] — System: [SYSTEMNAME]

Geprueft (lit. a-h):
☑/☐ lit. a — subliminale / manipulative Technik: [JA — VERBOTEN / NEIN]
☑/☐ lit. b — Vulnerabilitaetsausnutzung: [JA — VERBOTEN / NEIN]
☑/☐ lit. c — Social Scoring: [JA — VERBOTEN / NEIN]
☑/☐ lit. d — Predictive Policing: [JA — VERBOTEN / NEIN]
☑/☐ lit. e — Untargeted Scraping Biometrie: [JA — VERBOTEN / NEIN]
☑/☐ lit. f — Emotionserkennung Arbeitsplatz/Bildung: [JA — VERBOTEN / NEIN]
☑/☐ lit. g — biometrische Kategorisierung: [JA — VERBOTEN / NEIN]
☑/☐ lit. h — Echtzeit-RBI oeffentlicher Raum: [JA — VERBOTEN / Ausnahme: BESCHREIBUNG]

Ergebnis: [KEIN VERBOT / VERBOT: lit. X — Sanktion bis 35 Mio. EUR Art. 99 Abs. 3 KI-VO]
Naechster Schritt: [EINSTELLUNG DES BETRIEBS / sachlicher-ausschluss-art-2 / Weiter-Pruefung]
Geprueft: [NAME], [DATUM]
```

## 4. `verhaeltnis-zu-anderen-unionsrechtsakten`

**Fokus:** Anwalt oder Compliance-Beauftragter fragt: Gilt neben der KI-VO noch ein anderes EU-Gesetz für das gleiche System und wie interagieren die Pflichten? Art. 2 Abs. 2 KI-VO Verhältnis zu anderen Rechtsakten. Prüfraster: DSGVO Maschinenverordnung Produktsicherheits-VO MDR IVDR NIS-2 Cyber Resilience Act Kumulationseffekte Spezialitaet Verweisregelungen Doppelpflichten. Output: Normen-Konflikt-Matrix und Handlungsempfehlung. Abgrenzung zu falsche-wiese-warnung-ki-vo (Abgrenzung bei klaren Verwechslungen) und territorialer-anwendungsbereich-art-2.

# Verhältnis zu anderen Unionsrechtsakten

## Zweck

Die KI-VO steht nicht isoliert. Sie verweist auf andere Unionsrechtsakte, wird von diesen ergänzt und überlagert in manchen Bereichen bestehende Pflichten. Dieser Skill klärt das Rangverhältnis und zeigt, welche Rechtsakte kumulativ zu beachten sind.

## Grundregel: Kumulation, nicht Verdrängung

Die KI-VO verdrängt andere Unionsrechtsakte in der Regel nicht, sondern ergänzt sie. Unternehmen müssen häufig mehrere Regelwerke gleichzeitig einhalten.

## DSGVO — Verordnung (EU) 2016/679

**Verhältnis:** Ergänzend und überschneidend

- Die DSGVO gilt für jede Verarbeitung personenbezogener Daten, unabhängig vom Einsatz von KI.
- Für Hochrisiko-KI-Systeme, die personenbezogene Daten verarbeiten, gelten beide Regelwerke.
- Die Grundrechte-Folgenabschätzung nach Art. 27 KI-VO ist eng mit der Datenschutz-Folgenabschätzung nach Art. 35 DSGVO abzustimmen.
- Das Recht auf Erklärung automatisierter Entscheidungen nach Art. 22 DSGVO und die Transparenzpflichten der KI-VO sind parallel zu erfüllen.
- Art. 10 Abs. 5 KI-VO erlaubt unter engen Voraussetzungen die Verarbeitung besonderer Kategorien personenbezogener Daten zur Bias-Erkennung — vorbehaltlich DSGVO-Rechtsgrundlage.

## Maschinenverordnung — Verordnung (EU) 2023/1230

**Verhältnis:** Speziell für KI in Maschinen; Anhang I Nr. 7 KI-VO

- Sicherheitskomponenten in Maschinen, die KI-Systeme sind, können gleichzeitig unter die Maschinenverordnung und die KI-VO fallen.
- Die Konformitätsbewertung nach der Maschinenverordnung kann auf KI-VO-Anforderungen angerechnet werden, wenn die Anforderungen gleichwertig sind.

## Medizinprodukteverordnung MDR — Verordnung (EU) 2017/745

**Verhältnis:** Speziell für KI in Medizinprodukten; Anhang I Nr. 1 KI-VO

- KI-Systeme als Medizinprodukte oder als Zubehör zu Medizinprodukten unterliegen gleichzeitig MDR und KI-VO.
- Die benannte Stelle nach MDR kann für die KI-VO-Konformitätsbewertung nach Art. 43 Abs. 3 KI-VO mitbenutzt werden.
- Software als Medizinprodukt (SaMD) mit KI-Komponente ist ein zentraler Anwendungsfall.

## IVDR — Verordnung (EU) 2017/746

**Verhältnis:** Entsprechend wie MDR, für In-vitro-Diagnostika; Anhang I Nr. 2 KI-VO

## Produktsicherheits-Verordnung — Verordnung (EU) 2023/988

**Verhältnis:** Auffangnetz für Produkte ohne spezialgesetzliche Regelung

- Soweit KI-Systeme als Produkte in Verkehr gebracht werden und nicht unter spezialgesetzliche Produktsicherheitsvorschriften fallen, gilt die allgemeine Produktsicherheits-Verordnung.
- Sie enthält Marktüberwachungspflichten, die parallel zur KI-VO-Post-Market-Monitoring-Pflicht (Art. 72 KI-VO) laufen.

## Cyber Resilience Act — Verordnung (EU) 2024/2847

**Verhältnis:** Cybersicherheit als überlagernde Schicht

- Produkte mit digitalen Elementen, die KI-Systeme sind, können gleichzeitig dem Cyber Resilience Act und der KI-VO unterliegen.
- Art. 15 KI-VO (Cybersicherheit für Hochrisiko-KI) und die Anforderungen des Cyber Resilience Act können kumulativ wirken.

## NIS-2-Richtlinie — Richtlinie (EU) 2022/2555

**Verhältnis:** Für Betreiber kritischer Infrastruktur relevant

- Betreiber wesentlicher Einrichtungen, die KI-Systeme einsetzen, müssen zusätzlich zu KI-VO-Pflichten die Anforderungen der NIS-2-Richtlinie (umgesetzt in nationales Recht) beachten.

## Praktische Checkliste

| Situation | Zusätzliche Rechtsakte |
|---|---|
| KI verarbeitet personenbezogene Daten | DSGVO |
| KI in Maschine/Roboter | Maschinenverordnung |
| KI als Medizinprodukt oder SaMD | MDR oder IVDR |
| KI-Produkt ohne Spezialnorm | Produktsicherheits-VO |
| KI-Produkt mit Cybersicherheitsrelevanz | Cyber Resilience Act |
| KI bei kritischer Infrastruktur | NIS-2 |

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
PRUEFERGEBNIS — VERHAELTNIS ZU ANDEREN UNIONSRECHTSAKTEN
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 2 Abs. 7 Rn. 5]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
