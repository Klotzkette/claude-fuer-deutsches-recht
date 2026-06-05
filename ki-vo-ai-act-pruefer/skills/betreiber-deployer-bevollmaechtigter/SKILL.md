---
name: betreiber-deployer-bevollmaechtigter
description: "Betreiber Deployer Bevollmaechtigter: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Betreiber Deployer Bevollmaechtigter

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Betreiber Deployer Bevollmaechtigter** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `betreiber-deployer-pflichten-art-26` | Unternehmen oder Behoerde setzt ein Hochrisiko-KI-System, GPAI-System oder allgemeinen Chatbot ein und fragt nach Betreiberpflichten. Art. 26 KI-VO: bestimmungsgemaesse Verwendung, menschliche Aufsicht, Eingabedaten, Protokolle, Vorfallmeldungen, Informationspflichten; Art. 27 Grundrechte-Folgenabschaetzung. Besonderer Fokus: Off-label-Nutzung durch Mitarbeitende, Zweckaenderung, Art. 25 Anbieterwerden, Governance fuer allgemeine Chatbots in Hochrisiko-Kontexten. Output: Betreiber-Compliance-Checkliste mit Fehlgebrauchs- und Re-Evaluationsplan. |
| `bevollmaechtigter-und-produkthersteller-pflichten-art-22-und-25` | Drittstaaten-Anbieter ohne EU-Niederlassung oder Produkthersteller fragt: Wer vertritt uns in der EU und wer haftet für integrierte KI-Komponenten? Art. 22 KI-VO Bevollmaechtigter Art. 25 Produkthersteller. Prüfraster: Bevollmaechtigter als EU-Vertreter für Drittstaaten-Anbieter schriftliches Mandat Pflichten gegenüber Aufsichtsbehoerden. Produkthersteller-Verantwortung bei Integration von Hochrisiko-KI als Sicherheitsbauteil in eigenes Produkt. Output: Pflichtenliste und Muster-Bevollmaechtigungsvereinbarung. Abgrenzung zu rolle-anbieter-prüfen-art-3-nr-3 und einführer-importer-pflichten-art-23. |
| `biometrie-emotionserkennung-polizei-grenzen` | Biometrie, Gesichtserkennung und Emotionserkennung im KI-VO-Grenzbereich: Art. 5 Verbote, Anhang III, Strafverfolgungsausnahmen, oeffentlicher Raum, Schule/Arbeitsplatz, Transparenz, Datenschutz und Beweisverwertungsrisiken. |
| `code-of-practice-und-harmonisierte-normen` | Normen- und Standards-Landkarte fuer KI-VO-Compliance: Art. 40 harmonisierte Normen, Art. 41 gemeinsame Spezifikationen, Art. 56 GPAI Code of Practice, ISO/IEC 42001 / 23894 / 22989 / 23053 sowie Sicherheits- und Datenschutzstandards. Erklaert Vermutungswirkung nur bei im EU-Amtsblatt referenzierten harmonisierten Normen und nutzt ISO-Normen als Orientierung ohne falsche Konformitaetsvermutung. Output: standardsbasierter Massnahmenplan fuer KI-System, Hochrisiko oder GPAI. |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Betreiber Deployer Bevollmaechtigter**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `betreiber-deployer-pflichten-art-26`

**Fokus:** Unternehmen oder Behoerde setzt ein Hochrisiko-KI-System, GPAI-System oder allgemeinen Chatbot ein und fragt nach Betreiberpflichten. Art. 26 KI-VO: bestimmungsgemaesse Verwendung, menschliche Aufsicht, Eingabedaten, Protokolle, Vorfallmeldungen, Informationspflichten; Art. 27 Grundrechte-Folgenabschaetzung. Besonderer Fokus: Off-label-Nutzung durch Mitarbeitende, Zweckaenderung, Art. 25 Anbieterwerden, Governance fuer allgemeine Chatbots in Hochrisiko-Kontexten. Output: Betreiber-Compliance-Checkliste mit Fehlgebrauchs- und Re-Evaluationsplan.

# Betreiber-Pflichten (Deployer) — Art. 26 und 27 KI-VO

## Zweck

Betreiber sind natürliche oder juristische Personen, Behörden, Einrichtungen oder sonstige Stellen, die ein KI-System unter eigener Verantwortung verwenden. Dieser Skill prüft die Pflichten beim Einsatz von Hochrisiko-KI und ergänzt einen Governance-Check für allgemeine Chatbots/GPAI-Systeme, die intern zweckwidrig für Hochrisiko-Kontexte genutzt werden könnten.

## Pflicht 1 — Bestimmungsgemäße Verwendung

Betreiber müssen Hochrisiko-KI-Systeme nach der Gebrauchsanweisung des Anbieters verwenden.

Prüffragen:
- Liegt die Gebrauchsanweisung vor und ist sie intern umgesetzt?
- Ist der interne Use Case vom Anbieterzweck gedeckt?
- Werden Prompt-Vorlagen, Workflows, Rollenrechte oder Schnittstellen so gestaltet, dass keine unzulässige Zweckänderung entsteht?
- Gibt es ein Freigabeverfahren für neue KI-Use-Cases?

## Sonderthema — Mitarbeitende nutzen ein allgemeines KI-Tool hochriskant

Wenn Mitarbeitende ein allgemeines Tool entgegen der Zweckbestimmung für Personal, Kredit, Bildung, Verwaltung, Justiz oder andere Anhang-III-Kontexte einsetzen, prüfe die Organisationsverantwortung:

| Befund | Einordnung |
|---|---|
| Klare Richtlinie, Schulung, Rollenrechte, Logging, Sperren; isolierter Verstoß | Compliance-/Incident-Thema; Nutzung beenden, dokumentieren, nachschulen, ggf. Daten/Output entfernen |
| Fachabteilung nutzt es wiederholt und Führung weiß davon | tatsächlicher Betreiberzweck kann kippen; `hochrisiko-art-6-abs-2-anhang-iii` neu prüfen |
| Tool ist technisch offen und Hochrisiko-Nutzung naheliegend | vorhersehbarer Fehlgebrauch; Kontrollen, Warnungen, Freigaben und Re-Evaluation erforderlich |
| Betreiber ändert Zweck oder System wesentlich | `anbieter-werden-art-25` prüfen; Anbieterpflichten können ausgelöst werden |

Mindestmaßnahmen:
- KI-Richtlinie mit erlaubten und verbotenen Use Cases
- KI-Kompetenz/Schulung nach Art. 4
- Rollen- und Zugriffskonzept für sensible Bereiche
- Prompt- und Datenklassifizierungsregeln
- Logging/Audit für sensible Workflows
- Freigabeprozess für neue KI-Use-Cases
- Re-Evaluation bei Zweckänderung, Modellwechsel, neuer Integration oder auffälliger Nutzung

## Pflicht 2 — Menschliche Aufsicht

Betreiber müssen die vom Anbieter vorgesehenen Aufsichtsmaßnahmen tatsächlich umsetzen.

Prüffragen:
- Sind Aufsichtspersonen benannt und geschult?
- Können sie Output verstehen, kritisch prüfen, übersteuern oder stoppen?
- Ist Aufsicht mehr als nur formale Abzeichnung?
- Gibt es Eskalationsregeln bei Fehlern, Bias, Halluzinationen, Drift oder ungewöhnlichen Outputs?

## Pflicht 3 — Eingabedaten und Nutzungskontext

Wenn Betreiber Eingabedaten kontrollieren, müssen diese relevant und repräsentativ für den vorgesehenen Zweck sein.

Prüffragen:
- Welche Eingabedaten werden vom Betreiber bereitgestellt?
- Sind personenbezogene, vertrauliche oder besondere Daten betroffen?
- Sind die Daten zweckgeeignet und aktuell?
- Wird verhindert, dass Mitarbeitende sensible Personal-, Kredit-, Gesundheits- oder Justizdaten in allgemeine Tools eingeben?

## Pflicht 4 — Protokolle und Nachvollziehbarkeit

Betreiber müssen Protokolle nach Maßgabe der KI-VO und anderer Rechtsvorschriften aufbewahren.

Prüffragen:
- Welche Logs erzeugt das System?
- Sind Prompt, Eingabe, Output, Nutzer, Zeitpunkt, Version und Entscheidungspfad nachvollziehbar?
- Wie werden Datenschutz, Geheimnisschutz und Löschpflichten berücksichtigt?
- Können Off-label-Nutzungen erkannt werden?

## Pflicht 5 — Überwachung, Meldung und Unterbrechung

Betreiber müssen bei ernsthaften Risiken, Fehlfunktionen oder schwerwiegenden Vorfällen reagieren und ggf. Anbieter sowie Behörden informieren.

Prüffragen:
- Gibt es ein Verfahren für Incidents und Near Misses?
- Wer entscheidet über Pausierung des Systems?
- Werden Outputs korrigiert, zurückgenommen oder betroffene Personen informiert?
- Ist `marktueberwachung-meldung-vorfaelle-art-72-bis-79` einzuschalten?

## Pflicht 6 — Informationspflicht gegenüber Betroffenen

Wenn ein Hochrisiko-KI-System für Entscheidungen gegenüber natürlichen Personen eingesetzt wird, ist transparent zu machen, dass KI beteiligt ist, soweit dies nicht ohnehin offensichtlich ist oder spezieller geregelt ist.

Prüffragen:
- Wer ist betroffen?
- Welche Entscheidung oder Vorbereitung wird beeinflusst?
- Welche Information erhält die Person?
- Gibt es Rechte auf Auskunft, menschliche Überprüfung oder Beschwerde nach KI-VO, DSGVO oder Fachrecht?

## Grundrechte-Folgenabschätzung — Art. 27 KI-VO

Prüfe Art. 27 insbesondere bei:
- öffentlichen Stellen
- privaten Betreibern, soweit sie Hochrisiko-KI für bestimmte wesentliche Dienste einsetzen
- Konstellationen mit Beschäftigung, Bildung, Kredit, Versicherung, Sozialleistungen, Justiznähe oder sonstiger Machtasymmetrie

Inhalt:
- Beschreibung des Systems und Zwecks
- betroffene Personen/Gruppen
- Nutzungsfrequenz und Dauer
- Risiken für Grundrechte
- menschliche Aufsicht und Abhilfemaßnahmen
- Daten- und Governance-Konzept
- Verbindung zur DSGVO-Datenschutz-Folgenabschätzung

## Output-Template — Betreiber-Compliance-Check

```text
BETREIBER-COMPLIANCE-CHECK ART. 26/27 KI-VO
Datum: [DATUM]
System: [NAME]
Betreiber: [NAME]
Risikoklasse: [HOCHRISIKO / UNKLAR / ALLGEMEINES GPAI-SYSTEM]

1. Zweck und Gebrauchsanweisung
[Anbieterzweck, interner Zweck, Abweichungen]

2. Off-label-/Fehlgebrauchsrisiko
[isolierter Verstoß / vorhersehbarer Fehlgebrauch / geduldete Hochrisiko-Nutzung / Zweckänderung]
[Maßnahmen: Richtlinie, Schulung, Sperren, Logging, Freigabe]

3. Art. 26-Pflichten
- bestimmungsgemäße Verwendung: [...]
- menschliche Aufsicht: [...]
- Eingabedaten: [...]
- Protokolle: [...]
- Überwachung/Vorfälle: [...]
- Information Betroffener: [...]

4. Art. 27 Grundrechte-Folgenabschätzung
[erforderlich / nicht erforderlich / offen]
[Begründung]

5. Anbieterwerden Art. 25
[Risiko ja/nein/offen]

6. Nächste Skills
[hochrisiko-art-6-abs-2-anhang-iii / anbieter-werden-art-25 / output-betreiber-checkliste-und-folgenabschaetzung / marktueberwachung-meldung-vorfaelle-art-72-bis-79]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 3 Nr. 4, Nr. 12, Nr. 13 und Nr. 23, Art. 4, Art. 25, Art. 26 und Art. 27 KI-VO. Keine Rechtsberatung.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `bevollmaechtigter-und-produkthersteller-pflichten-art-22-und-25`

**Fokus:** Drittstaaten-Anbieter ohne EU-Niederlassung oder Produkthersteller fragt: Wer vertritt uns in der EU und wer haftet für integrierte KI-Komponenten? Art. 22 KI-VO Bevollmaechtigter Art. 25 Produkthersteller. Prüfraster: Bevollmaechtigter als EU-Vertreter für Drittstaaten-Anbieter schriftliches Mandat Pflichten gegenüber Aufsichtsbehoerden. Produkthersteller-Verantwortung bei Integration von Hochrisiko-KI als Sicherheitsbauteil in eigenes Produkt. Output: Pflichtenliste und Muster-Bevollmaechtigungsvereinbarung. Abgrenzung zu rolle-anbieter-prüfen-art-3-nr-3 und einführer-importer-pflichten-art-23.

# Bevollmächtigter und Produkthersteller — Art. 22 und 25 KI-VO

## Teil 1 — Bevollmächtigter (Art. 22 KI-VO)

### Wer muss einen Bevollmächtigten benennen?

Anbieter von Hochrisiko-KI-Systemen, die nicht in der EU niedergelassen sind, müssen vor dem Inverkehrbringen oder der Inbetriebnahme in der EU schriftlich einen Bevollmächtigten in der EU benennen.

**Prüffragen:**
- Ist der Anbieter des Systems in der EU oder einem Drittland ansässig?
- Wenn Drittland → Bevollmächtigter zwingend erforderlich

### Wer kann Bevollmächtigter sein?

Eine in der EU ansässige natürliche oder juristische Person, die vom Anbieter schriftlich bevollmächtigt wurde. Der Bevollmächtigte kann gleichzeitig Einführer sein.

### Pflichten des Bevollmächtigten (Art. 22 Abs. 3 KI-VO)

Der Bevollmächtigte muss mindestens folgende Aufgaben wahrnehmen:
- Registrierung in der EU-Datenbank nach Art. 49 und 71 KI-VO
- Vorlage der EU-Konformitätserklärung und der technischen Dokumentation an die Marktüberwachungsbehörde auf Anfrage
- Kooperation mit nationalen Behörden bei Anfragen, Prüfungen und Corrective Actions
- Weitergabe von Informationen an den Anbieter über schwerwiegende Vorfälle und Nichtkonformitäten

### Schriftliches Mandat (Art. 22 Abs. 2 KI-VO)

Das Mandat muss schriftlich erteilt werden und den Bevollmächtigten mindestens zu den oben genannten Aufgaben ermächtigen. Der Bevollmächtigte kann das Mandat kündigen, wenn der Anbieter gegen KI-VO-Anforderungen verstößt.

**Prüffragen:**
- Liegt ein schriftliches Mandat vor?
- Ist das Mandat ausreichend konkret, um die gesetzlichen Aufgaben zu ermöglichen?
- Welche Haftungsregelungen wurden zwischen Anbieter und Bevollmächtigtem vereinbart?

## Teil 2 — Produkthersteller (Art. 25 KI-VO)

### Wann hat ein Produkthersteller Anbieter-Pflichten?

Ein Produkthersteller übernimmt die Pflichten eines Anbieters, wenn er ein Hochrisiko-KI-System als Sicherheitsbauteil in sein Produkt integriert und dieses Produkt unter seinem eigenen Namen oder seiner eigenen Marke in Verkehr bringt.

**Prüffragen:**
- Integrieren Sie ein fremdes KI-System als Sicherheitsbauteil in ein eigenes Produkt?
- Bringen Sie das Gesamtprodukt unter eigenem Namen in Verkehr?
- Fällt das Produkt unter Anhang-I-Sektorrecht (Maschinenverordnung, MDR usw.)?

**Wenn ja:** Der Produkthersteller übernimmt die vollständigen Anbieter-Pflichten nach Art. 16 bis 42 KI-VO für das Hochrisiko-KI-System und muss die Konformitätsbewertung für das Gesamtprodukt einschließlich des KI-Systems durchführen.

### Verhältnis zum ursprünglichen Anbieter des KI-Systems

Der ursprüngliche Anbieter des KI-Systems (z.B. ein KI-Komponentenanbieter) muss dem Produkthersteller alle erforderlichen Informationen bereitstellen, damit dieser die Anbieter-Pflichten erfüllen kann (Art. 25 Abs. 3 KI-VO).

**Praktische Konsequenz:** Vertragliche Regelungen zwischen KI-Komponentenanbieter und Produkthersteller sind essenziell, um Informationsflüsse und Haftungsverteilung zu klären.

### Typische Szenarien

- Maschinenhersteller integriert ein fremdes KI-System zur Qualitätsprüfung als Sicherheitsbauteil → Produkthersteller wird zum Anbieter
- Medizingeräthersteller integriert ein fremdes Bildanalyse-Modell in ein Medizinprodukt → Produkthersteller wird zum Anbieter
- Cloud-Anbieter stellt generische KI-Infrastruktur bereit (kein Sicherheitsbauteil) → kein Produkthersteller nach Art. 25 KI-VO, aber möglicherweise Händler-Pflichten

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
PRUEFERGEBNIS — BEVOLLMAECHTIGTER UND PRODUKTHERSTELLER PFLICHTEN ART 22 UND 25
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 22 Rn. 4]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

## 3. `biometrie-emotionserkennung-polizei-grenzen`

**Fokus:** Biometrie, Gesichtserkennung und Emotionserkennung im KI-VO-Grenzbereich: Art. 5 Verbote, Anhang III, Strafverfolgungsausnahmen, oeffentlicher Raum, Schule/Arbeitsplatz, Transparenz, Datenschutz und Beweisverwertungsrisiken.

# Biometrie und Emotionserkennung

## Prüfziel

Dieser Skill trennt biometrische Identifizierung, biometrische Kategorisierung, Emotionserkennung und allgemeine Bildanalyse. Diese Unterscheidung entscheidet über Verbote, Hochrisiko und Transparenz.

## Entscheidungsbaum

1. Identifiziert das System eine konkrete Person?
2. Kategorisiert es Personen nach sensiblen Merkmalen?
3. Erkennt es Emotionen oder Absichten?
4. Findet der Einsatz im öffentlichen Raum, am Arbeitsplatz, in Bildung oder Strafverfolgung statt?
5. Greifen Art.-5-Verbote oder eng gefasste Ausnahmen?
6. Ist Anhang III einschlägig?

## Risikofelder

- Live-Fernidentifikation im öffentlichen Raum.
- Emotionserkennung bei Beschäftigten oder Lernenden.
- biometrische Kategorisierung sensibler Merkmale.
- polizeiliche Trefferlisten ohne hinreichende menschliche Nachprüfung.
- Zweckwechsel von Zugangskontrolle zu Überwachung.

## Output

- Verbots-/Hochrisiko-Ampel.
- Ausnahmeprüfung.
- Datenschutz- und Grundrechtsvermerk.
- technische Mindestkontrollen.

## Warnung

Bei biometrischen Systemen reicht ein allgemeiner "Security"-Zweck nie. Der konkrete Ort, Zweck, Personenkreis und Entscheidungsbezug müssen sauber feststehen.

## 4. `code-of-practice-und-harmonisierte-normen`

**Fokus:** Normen- und Standards-Landkarte fuer KI-VO-Compliance: Art. 40 harmonisierte Normen, Art. 41 gemeinsame Spezifikationen, Art. 56 GPAI Code of Practice, ISO/IEC 42001 / 23894 / 22989 / 23053 sowie Sicherheits- und Datenschutzstandards. Erklaert Vermutungswirkung nur bei im EU-Amtsblatt referenzierten harmonisierten Normen und nutzt ISO-Normen als Orientierung ohne falsche Konformitaetsvermutung. Output: standardsbasierter Massnahmenplan fuer KI-System, Hochrisiko oder GPAI.

# Verhaltenskodizes, harmonisierte Normen und ISO-Standards

## Zweck

Dieser Skill unterstützt die Compliance-Strategie für KI-Systeme, Hochrisiko-KI und GPAI-Modelle. Er trennt sauber:

- harmonisierte Normen nach Art. 40 KI-VO
- gemeinsame Spezifikationen nach Art. 41 KI-VO
- GPAI Code of Practice nach Art. 56 KI-VO
- internationale ISO/IEC-Standards als Orientierung

Wichtig: Nicht jede ISO-Norm ist automatisch eine harmonisierte Norm im Sinne der KI-VO. Eine Vermutungswirkung entsteht nur, soweit eine harmonisierte europäische Norm im Amtsblatt der EU referenziert ist und die einschlägigen Anforderungen abdeckt.

## Art. 40 KI-VO — harmonisierte Normen

Harmonisierte Normen konkretisieren KI-VO-Anforderungen technisch. Bei vollständiger Konformität mit einschlägigen, im EU-Amtsblatt veröffentlichten harmonisierten Normen wird die Konformität mit den abgedeckten Anforderungen vermutet.

Prüffragen:
- Gibt es für die konkrete KI-VO-Anforderung bereits eine harmonisierte Norm mit Amtsblatt-Fundstelle?
- Welche Anforderungen deckt sie ab: Risikomanagement, Datenqualität, technische Dokumentation, Logging, Transparenz, menschliche Aufsicht, Genauigkeit, Robustheit, Cybersicherheit, Qualitätsmanagement?
- Wurde die Norm vollständig umgesetzt oder nur als Orientierung genutzt?
- Gibt es Lücken, weil die Norm nicht alle Anforderungen abdeckt?

Dokumentationsregel:
- Nie pauschal schreiben "ISO-konform = KI-VO-konform".
- Immer benennen, welche Norm welche Anforderung abdeckt und ob eine EU-Vermutungswirkung besteht.

## Art. 41 KI-VO — gemeinsame Spezifikationen

Wenn harmonisierte Normen fehlen oder unzureichend sind, kann die Kommission gemeinsame Spezifikationen erlassen. Auch diese können für die praktische Compliance maßgeblich sein.

Prüffragen:
- Gibt es eine einschlägige gemeinsame Spezifikation?
- Ist sie verpflichtend oder gibt es eine begründete alternative technische Lösung?
- Wie wird Abweichung dokumentiert?

## Art. 56 KI-VO — GPAI Code of Practice

Für Anbieter von GPAI-Modellen ist der GPAI Code of Practice besonders relevant. Er kann als Brücke dienen, bis harmonisierte Normen und weitere sekundäre Rechtsakte die Pflichten konkretisieren.

Prüffragen:
- Ist der Mandant Anbieter eines GPAI-Modells?
- Hat er den Code of Practice gezeichnet oder befolgt?
- Deckt der Code technische Dokumentation, Copyright-Policy, Trainingsdaten-Zusammenfassung, Safety, Evaluierung und systemisches Risiko ab?
- Welche Lücken bleiben trotz Code?

## Standards-Landkarte

Diese Standards können als Arbeitsrahmen dienen, ohne automatisch KI-VO-Konformität zu beweisen:

| Standard | Nutzen im KI-VO-| Vorsicht |
|---|---|---|
| ISO/IEC 42001:2023 | AI Management System, Governance, Rollen, Richtlinien, kontinuierliche Verbesserung | nicht identisch mit allen KI-VO-Pflichten; keine Vermutungswirkung ohne harmonisierte Referenz |
| ISO/IEC 23894:2023 | AI Risk Management, Risikoidentifikation, Bewertung, Behandlung, Monitoring | an Art. 9 KI-VO anpassen, Grundrechte ausdrücklich ergänzen |
| ISO/IEC 22989:2022 | AI Concepts and Terminology | hilfreich für Begriffe, ersetzt nicht Art. 3 KI-VO |
| ISO/IEC 23053:2022 | Framework für KI-Systeme mit maschinellem Lernen | gut für technische Architektur- und Lifecycle-Beschreibung |
| ISO/IEC 27001:2022 | Informationssicherheits-Management | unterstützt Cybersicherheit, aber nicht spezifisch KI-VO |
| ISO/IEC 27701 | Datenschutz-Management als Erweiterung zu 27001/27002 | unterstützt DSGVO/Privacy, ersetzt keine KI-VO- oder DSFA-Prüfung |
| ISO/IEC 38507 | Governance implications of AI | Orientierung für Leitungs- und Aufsichtsgremien |

## Standards in die Sachprüfung einbauen

### Art. 3 KI-System-Check

Nutze ISO/IEC 22989 und 23053 nur als technische Begriffshilfe. Die rechtliche Definition bleibt Art. 3 Nr. 1 KI-VO. Dokumentiere besonders:
- maschinenbasiertes System
- Autonomiegrad
- Inferenz
- Output
- Umgebungseinfluss

### Art. 6 Abs. 2 / Anhang III

Standards helfen bei Risikomanagement und Kontrollen, entscheiden aber nicht allein über Hochrisiko. Die Hochrisiko-Klassifikation folgt Zweckbestimmung und Anhang III.

### Hochrisiko-Pflichten

Zuordnen:
- Art. 9 Risikomanagement: ISO/IEC 23894 plus KI-VO-Grundrechte
- Art. 10 Daten/Data Governance: Datenqualitäts- und Bias-Prozesse ergänzen
- Art. 11/Anhang IV Dokumentation: ISO/IEC 23053 als technische Strukturhilfe
- Art. 12 Logging: Sicherheits- und Audit-Standards ergänzend
- Art. 14 menschliche Aufsicht: Governance- und Human-oversight-Konzept gesondert
- Art. 15 Genauigkeit/Robustheit/Cybersicherheit: 27001/Threat-Modeling/Testkonzept ergänzend
- Art. 17 Qualitätsmanagement: ISO/IEC 42001 als Rahmen, KI-VO-spezifische Lücken schließen

## Output-Template — Normen- und Standardsplan

```text
NORMEN- UND STANDARDSPLAN KI-VO
Datum: [DATUM]
System / Modell: [NAME]
Risikoklasse: [Hochrisiko / begrenzt / GPAI / unklar]

1. Harmonisierte Normen Art. 40
[vorhanden / nicht vorhanden / Amtsblatt-Fundstelle offen]
[abgedeckte KI-VO-Anforderungen]

2. Gemeinsame Spezifikationen Art. 41
[vorhanden / nicht vorhanden / prüfen]

3. GPAI Code of Practice Art. 56
[einschlägig ja/nein; Umsetzung]

4. ISO/IEC-Arbeitsrahmen
- ISO/IEC 42001: [Governance-Maßnahmen]
- ISO/IEC 23894: [Risikomanagement-Maßnahmen]
- ISO/IEC 22989/23053: [Begriffe/Architektur]
- Sicherheits-/Datenschutzstandards: [27001/27701/weitere]

5. KI-VO-Lücken trotz Standards
[Grundrechte, Zweckbestimmung, Art. 6, Art. 10, Art. 14, Art. 26/27, Dokumentation]

6. Konformitätsaussage
[Welche Norm begründet Vermutungswirkung? Welche Standards sind nur Orientierung?]
```

## Quellen- und Aktualitätshinweis

Stand: 05/2026. Maßgeblich sind Art. 40, 41, 56 und 95 KI-VO sowie die jeweils aktuell im Amtsblatt der EU referenzierten harmonisierten Normen. Vor jeder finalen Aussage ist der Normenstand zu aktualisieren. Keine Rechtsberatung.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
