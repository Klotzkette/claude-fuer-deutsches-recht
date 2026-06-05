---
name: sachlicher-ausschluss-schwerwiegender-vorfall
description: "Sachlicher Ausschluss Schwerwiegender Vorfall: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Sachlicher Ausschluss Schwerwiegender Vorfall

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Sachlicher Ausschluss Schwerwiegender Vorfall** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `sachlicher-ausschluss-art-2-abs-3-bis-12` | Unternehmen fragt: Faellt unser KI-System möglicherweise voellig aus dem Anwendungsbereich der KI-VO heraus? Art. 2 Abs. 3 bis 12 KI-VO sachliche Ausnahmen. Prüfraster: Militaer und nationale Sicherheit Art. 2 Abs. 3 wissenschaftliche Forschung Art. 2 Abs. 6 Open-Source-Ausnahmen Art. 2 Abs. 12 persoenliche nicht berufliche Nutzung Art. 2 Abs. 10. Enge Auslegung Fallstricke kommerzielle Nutzung schließt Ausnahme meist aus. Output: Ausnahme-Entscheidungsbaum mit Voraussetzungen. Abgrenzung zu rückausnahme-art-6-abs-3 (nur Hochrisiko-Ausnahme) und territorialer-anwendungsbereich-art-2 (räumlicher Bereich). |
| `schwerwiegender-vorfall-art-73-playbook` | Schwerwiegender KI-Vorfall nach Art. 73 KI-VO: Erkennen, Stabilisieren, Melden, Ursachenanalyse, Nutzerkommunikation, Marktaufsicht, Produkthaftungs-/DSGVO-Schnittstellen und Vorstandslagebild. |
| `shadow-ai-und-off-label-governance` | Shadow-AI und Off-label-Nutzung beherrschen: Wenn Mitarbeitende allgemeine Chatbots oder freigegebene KI-Tools entgegen Zweckbestimmung fuer Hochrisiko-nahe Aufgaben verwenden. Prueft Art. 3, Art. 6, Art. 25, Art. 26, Art. 50 KI-VO, Policy, Monitoring, Re-Evaluation und Beweisakte. |
| `spezial-mechanik-erstpruefung-und-mandatsziel` | Mechanik: Erstprüfung, Rollenklärung und Mandatsziel im Plugin ki vo ai act pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Sachlicher Ausschluss Schwerwiegender Vorfall**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `sachlicher-ausschluss-art-2-abs-3-bis-12`

**Fokus:** Unternehmen fragt: Faellt unser KI-System möglicherweise voellig aus dem Anwendungsbereich der KI-VO heraus? Art. 2 Abs. 3 bis 12 KI-VO sachliche Ausnahmen. Prüfraster: Militaer und nationale Sicherheit Art. 2 Abs. 3 wissenschaftliche Forschung Art. 2 Abs. 6 Open-Source-Ausnahmen Art. 2 Abs. 12 persoenliche nicht berufliche Nutzung Art. 2 Abs. 10. Enge Auslegung Fallstricke kommerzielle Nutzung schließt Ausnahme meist aus. Output: Ausnahme-Entscheidungsbaum mit Voraussetzungen. Abgrenzung zu rückausnahme-art-6-abs-3 (nur Hochrisiko-Ausnahme) und territorialer-anwendungsbereich-art-2 (räumlicher Bereich).

# Sachliche Ausschlüsse — Art. 2 Abs. 3 bis 12 KI-VO

## Zweck

Art. 2 KI-VO enthält eine Reihe expliziter sachlicher Ausnahmen. Dieser Skill prüft, ob eine dieser Ausnahmen einschlägig ist und damit der Anwendungsbereich der KI-VO insgesamt oder für bestimmte Pflichten ausgeschlossen ist.

## Ausnahme 1 — Militärische und nationale Sicherheitszwecke (Art. 2 Abs. 3 KI-VO)

Die KI-VO gilt nicht für KI-Systeme, die ausschließlich für militärische Zwecke oder für Zwecke der nationalen Sicherheit entwickelt oder eingesetzt werden.

**Prüffragen:**
- Ist der Einsatzzweck ausschließlich militärisch oder national sicherheitsbezogen?
- Handelt es sich um eine staatliche Sicherheitsbehörde oder Streitkräfte?

**Enge Auslegung:** Die Ausnahme gilt nur für den jeweiligen spezifischen Einsatzzweck. Ein System, das sowohl militärisch als auch zivil eingesetzt wird (Dual-Use), fällt für den zivilen Teil unter die KI-VO.

## Ausnahme 2 — Behörden von Drittstaaten und internationale Organisationen (Art. 2 Abs. 4 KI-VO)

KI-Systeme, die von Drittstaatsbehörden oder internationalen Organisationen im Rahmen von Kooperationsabkommen eingesetzt werden, können vom Anwendungsbereich ausgenommen sein.

**Hinweis:** Diese Ausnahme ist eng und setzt konkrete Abkommen voraus. Im Zweifel gilt die KI-VO.

## Ausnahme 3 — Wissenschaftliche Forschung und Entwicklung (Art. 2 Abs. 6 KI-VO)

KI-Systeme, die ausschließlich zum Zweck der wissenschaftlichen Forschung und Entwicklung entwickelt und eingesetzt werden, unterliegen bis zu ihrer Inverkehrbringung oder Inbetriebnahme nicht der KI-VO.

**Prüffragen:**
- Wird das System ausschließlich intern zu Forschungszwecken eingesetzt?
- Findet kein Inverkehrbringen oder keine Inbetriebnahme statt?
- Werden betroffene Personen nicht durch das System in relevantem Ausmaß beeinträchtigt?

**Fallstrick:** Sobald das System aus der Forschungsphase herausgeht und real eingesetzt wird, gilt die KI-VO. Pilotprojekte mit echten Nutzern oder Betroffenen fallen in der Regel bereits unter die KI-VO.

## Ausnahme 4 — Rein persönliche, nicht berufliche Nutzung (Art. 2 Abs. 10 KI-VO)

Die KI-VO gilt nicht für natürliche Personen, die KI-Systeme für rein persönliche, nicht berufliche Tätigkeiten nutzen.

**Prüffragen:**
- Nutzt der Nutzer das System als Privatperson, nicht im Rahmen einer beruflichen oder wirtschaftlichen Tätigkeit?
- Sind keine anderen Personen durch die Nutzung betroffen, die nicht eingewilligt haben?

**Fallstrick:** Sobald die Nutzung beruflich oder im Rahmen einer unternehmerischen Tätigkeit erfolgt, gilt diese Ausnahme nicht. Freiberufler und Selbstständige fallen nicht unter die Ausnahme, wenn sie das System für ihre berufliche Tätigkeit nutzen.

## Ausnahme 5 — Open-Source-KI-Systeme (Art. 2 Abs. 12 KI-VO)

Für KI-Systeme, deren Parameter einschließlich der Modellgewichte, der Architektur und der Modellnutzung unter einer Open-Source-Lizenz öffentlich zugänglich gemacht werden, gelten unter bestimmten Voraussetzungen reduzierte Anforderungen.

**Voraussetzungen:**
- Parameter einschließlich Gewichte müssen öffentlich zugänglich sein.
- Nicht anwendbar auf KI-Systeme, die als Hochrisiko-KI einzustufen sind oder verbotene Praktiken darstellen.
- GPAI-Modelle mit systemischem Risiko (über 10e25 FLOP) sind von der Open-Source-Ausnahme ausgeschlossen (Art. 52 Abs. 1 KI-VO).

**Hinweis:** Die Open-Source-Ausnahme befreit nicht vollständig von allen Pflichten. Transparenzpflichten nach Art. 50 KI-VO können trotzdem gelten.

## Weitere Ausnahmen im Überblick

- **Art. 2 Abs. 5:** KI-Systeme für Zwecke der Strafverfolgung in Drittstaaten, sofern keine EU-Bürger betroffen sind
- **Art. 2 Abs. 7 und 8:** Bestimmte Behörden im Rahmen von EU-Verordnungen

## Ergebnis und Routing

- **Ausnahme eindeutig gegeben:** KI-VO nicht anwendbar; endet. Hinweis auf möglicherweise anwendbares anderes Recht.
- **Ausnahme fraglich (z.B. Dual-Use, Forschung mit echten Nutzern):** Weiter mit Vorbehalt; Hinweis auf Klärungsbedarf; ggf. `mandatsabbruch-empfehlung-komplexe-faelle`
- **Keine Ausnahme:** Weiter zu `persoenlicher-anwendungsbereich-rollen-art-3`

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
PRUEFERGEBNIS — SACHLICHER AUSSCHLUSS ART 2 ABS 3 BIS 12
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 2 Abs. 3 Rn. 8]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 2. `schwerwiegender-vorfall-art-73-playbook`

**Fokus:** Schwerwiegender KI-Vorfall nach Art. 73 KI-VO: Erkennen, Stabilisieren, Melden, Ursachenanalyse, Nutzerkommunikation, Marktaufsicht, Produkthaftungs-/DSGVO-Schnittstellen und Vorstandslagebild.

# Schwerwiegender Vorfall — Art. 73 Playbook

## Wann nutzen?

Wenn ein KI-System Schaden verursacht, Sicherheitsrisiken zeigt, diskriminierend wirkt, falsche Hochrisiko-Entscheidungen ausgibt, Daten preisgibt oder ein Behörden-/Nutzerhinweis eingeht.

## Sofort-Triage

1. Ist das System Hochrisiko?
2. Liegt ein schwerwiegender Vorfall im Sinne der KI-VO nahe?
3. Wer ist Anbieter, Betreiber, Importeur, Händler?
4. Welche Personen, Daten, Rechtsgüter, Märkte sind betroffen?
5. Muss parallel DSGVO, Produktsicherheit, Medizinprodukterecht oder Strafrecht geprüft werden?

## Maßnahmen

- System stabilisieren oder temporär deaktivieren.
- Logs sichern.
- Modellversion einfrieren.
- Nutzer und interne Owner informieren.
- Meldefristen und Adressaten prüfen.
- Root-Cause-Analyse starten.
- Korrekturmaßnahme dokumentieren.

## Output

- Vorfall-Erstmeldung.
- Incident Timeline.
- Root-Cause-Fragen.
- Behörden- und Kundenkommunikation.
- Lessons-Learned-Vermerk.

## Qualitätsregel

Nicht jede Fehlfunktion ist meldepflichtig. Aber jeder potenziell schwerwiegende Vorfall braucht eine nachvollziehbare Entscheidung, warum gemeldet oder nicht gemeldet wurde.

## 3. `shadow-ai-und-off-label-governance`

**Fokus:** Shadow-AI und Off-label-Nutzung beherrschen: Wenn Mitarbeitende allgemeine Chatbots oder freigegebene KI-Tools entgegen Zweckbestimmung fuer Hochrisiko-nahe Aufgaben verwenden. Prueft Art. 3, Art. 6, Art. 25, Art. 26, Art. 50 KI-VO, Policy, Monitoring, Re-Evaluation und Beweisakte.

# Shadow-AI und Off-label-Governance

## Worum geht es?

Ein allgemeiner Chatbot ist nicht automatisch Hochrisiko. Gefährlich wird es, wenn Mitarbeitende ihn faktisch fuer Bewerberranking, Leistungsbeurteilung, Kreditvorauswahl, medizinische Triage, Behördenentscheidungen oder Justiznahe Sachverhaltsbewertung einsetzen, obwohl die Organisation ihn nur als Schreib- oder Recherchehilfe freigegeben hat.

## Prüfspur

1. **Tool bestimmen:** Consumer-Chatbot, Enterprise-Instanz, API, Plugin, lokales Modell, Fachsystem.
2. **Zweckbestimmung trennen:** Anbieterzweck, Betreiberfreigabe, tatsaechliche Nutzung.
3. **Anhang-III-Naehe prüfen:** Personal, Bildung, Kredit, Justiz, Migration, Strafverfolgung, Biometrie, kritische Infrastruktur.
4. **Rollenrisiko:** Wird der Betreiber durch Zweckänderung oder wesentliche Änderung selbst Anbieter? Art. 25 KI-VO prüfen.
5. **Betreiberpflichten:** Art. 26 KI-VO, Eingabedatenkontrolle, menschliche Aufsicht, Logik der Nutzung.
6. **Transparenz:** Art. 50 KI-VO, wenn Nutzer mit KI interagieren oder Deepfakes/synthetische Inhalte entstehen.
7. **Schnittstellen:** DSGVO Art. 22, Betriebsrat, Geheimnisschutz, Urheberrecht, Berufsrecht.

## Abhilfedesign

Erzeuge einen "Use-Case-Fence":

- Erlaubt: Textentwurf, Zusammenfassung, Ideensammlung, nicht entscheidende Vorarbeit.
- Nur nach Freigabe: personenbezogene Auswertung, Ranking, Risiko-Scoring, Aktenanalyse, Rechtsprüfung, Kundenselektion.
- Verboten: autonome Entscheidung, verdecktes Profiling, Upload von Geheimnissen in nicht freigegebene Systeme, automatisiertes Bewerber- oder Kreditranking ohne Rechtsprüfung.

## Dokumentation

Am Ende immer ein Kurzprotokoll:

- Freigegebener Zweck.
- Nicht freigegebene Hochrisiko-nahe Zwecke.
- Technische und organisatorische Sperren.
- Schulung nach Art. 4 KI-VO.
- Re-Evaluationstermin.

## Warnsignal

Wenn die Fachabteilung sagt: "Das Tool entscheidet nicht, es empfiehlt nur", trotzdem prüfen, ob die Empfehlung praktisch entscheidungsleitend ist. Entscheidend ist die reale Wirkung im Workflow, nicht das Etikett.

## 4. `spezial-mechanik-erstpruefung-und-mandatsziel`

**Fokus:** Mechanik: Erstprüfung, Rollenklärung und Mandatsziel im Plugin ki vo ai act pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Mechanik: Erstprüfung, Rollenklärung und Mandatsziel

## Spezialwissen: Mechanik: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Mechanik: Erstprüfung, Rollenklärung und Mandatsziel / mechanik erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, VO, EU, GPAI, Art. 43, CE, DB.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **KI-VO-Mechanik** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Mechanik der KI-VO-Erstprüfung
1. **Liegt ein KI-System vor (Art. 3 Nr. 1 KI-VO)?** Maschinengestütztes System, das mit unterschiedlicher Autonomiestufe konzipiert ist; konventionelle Software ohne lernende Komponente fällt nicht darunter.
2. **Territorialer Anwendungsbereich (Art. 2 KI-VO)?** Anbieter, deren System in der EU in Verkehr gebracht/in Betrieb genommen wird; Betreiber in der EU; Anbieter/Betreiber außerhalb der EU, deren Output in der EU genutzt wird.
3. **Sachlicher Ausschluss (Art. 2 Abs. 3-12 KI-VO)?** Z. B. Verteidigung/nationale Sicherheit, ausschließliche Forschung, freie Software für persönliche Zwecke.
4. **Rolle bestimmen (Art. 3 Nr. 3-8)?** Anbieter, Betreiber, Importeur, Händler — entscheidet das gesamte Pflichtenprofil.
5. **Risikoklasse (Art. 5, 6, 50)?** Verbotene Praktiken / Hochrisiko / Begrenztes Risiko / Minimal.
6. **GPAI-Schicht (Art. 51 ff.)?** Wenn ein Modell mit allgemeinem Verwendungszweck zugrunde liegt, eigener Pflichtenkanon.

## Geltungsstaffelung
- **Art. 5 Verbote**: gilt ab **02.02.2025**.
- **GPAI-Pflichten (Art. 51-55)** und **Governance (Art. 57 ff.)**: gilt ab **02.08.2025**.
- **Anhang III Hochrisiko** und allgemeine Pflichten: gilt ab **02.08.2026**.
- **Hochrisiko unter Anhang I (Sicherheitsbauteile bestehender Produktrichtlinien)**: gilt ab **02.08.2027**.

## Mandatsziel präzisieren
- **Compliance-Roadmap** für Anbieter: typischerweise 6-18 Monate je nach Risikoklasse.
- **Konformitätsbewertung**: bei Hochrisiko vor Inverkehrbringen; bei substantieller Änderung neu (Art. 43 Abs. 4).
- **EU-Datenbank Registrierung** (Art. 49) für Hochrisiko-Anbieter; öffentliche Liste durch Kommission.
- **Vertretung** (Art. 22): Anbieter aus Drittstaaten brauchen Bevollmächtigten in der Union.

## Sanktionsrahmen (Art. 99 KI-VO)
- **Verbotene Praktiken Art. 5**: bis **35 Mio. EUR oder 7 % weltweiter Jahresumsatz** (höherer Betrag).
- **Hochrisiko / GPAI-Pflichten**: bis **15 Mio. EUR oder 3 %**.
- **Falsche / unvollständige Informationen**: bis **7,5 Mio. EUR oder 1 %**.
- Geldbußen für KMU und Start-ups gedeckelt nach Maßgabe Art. 99 Abs. 6 (jeweils niedrigerer Betrag).

## Trade-off
Frühe Klassifizierung als "kein KI-System" oder "minimales Risiko" spart Aufwand, kann aber bei späterer Aufsichtsfeststellung doppelte Kosten und Marktausschluss verursachen. Empfehlung: konservative Klassifizierung mit dokumentierter Begründung statt einer Selbsteinschätzung "nicht erfasst".

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
