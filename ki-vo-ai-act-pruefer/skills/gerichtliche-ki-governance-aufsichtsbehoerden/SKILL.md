---
name: gerichtliche-ki-governance-aufsichtsbehoerden
description: "Gerichtliche KI Governance Aufsichtsbehoerden: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert."
---

# Gerichtliche KI Governance Aufsichtsbehoerden

## Arbeitsbereich

Dieser Skill bündelt 4 sachlich verwandte Arbeitsschritte rund um **Gerichtliche KI Governance Aufsichtsbehoerden** im Plugin KI-VO / AI Act-Prüfer. Die Prüffelder bauen aufeinander auf: zuerst das tragende Feld nach der konkreten Aktenlage bestimmen, dann ergänzende Felder nur dort heranziehen, wo dieselbe Akte mehrere Punkte trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei sauber getrennt.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `gerichtliche-ki-assistenz-hochrisiko-justiz` | Justizielle KI als Hochrisiko-Kontext: Systeme zur Unterstuetzung richterlicher oder behördlicher Rechtsanwendung, Sachverhaltswuerdigung, Aktenpriorisierung und Entscheidungsvorbereitung nach Art. 6 Abs. 2 i.V.m. Anhang III KI-VO. |
| `governance-aufsichtsbehoerden-art-70` | Unternehmen oder Behoerde fragt: An wen muss ich mich in Deutschland und Europa wenden wenn ich Fragen zur KI-VO-Aufsicht habe oder eine Meldepflicht erfullen muss? Art. 70 ff. KI-VO Governance. Prüfraster: nationale Aufsichtsbehoerden Art. 70 Europaeisches KI-Buero Art. 64 KI-Ausschuss Art. 65 wissenschaftliches Gremium Art. 68 Beratungsforum Art. 67 Aufgaben Befugnisse Koordination. Output: Übersicht zuständige Stellen in Deutschland und EU mit Kontakthinweisen. Abgrenzung zu marktueberwachung-meldung-vorfaelle-art-72-bis-79 (Meldepflichten) und sanktionen-art-99-bis-101 (Bußgeldrahmen). |
| `gpai-code-of-practice-copyright-safety-evidence` | GPAI Code of Practice und Evidence-Logik: Copyright-Policy, Safety/Security, systemisches Risiko, Modellinformationen fuer Downstream-Anbieter, Standards-Uebergang und Nachweismappe ohne falsche Zertifizierungsbehauptung. |
| `gpai-modelle-art-51-bis-55` | Entwickler oder Anbieter eines Sprachmodells oder Basismodells fragt: Fallen wir unter die GPAI-Pflichten der KI-VO und was muessen wir konkret tun? Art. 51 bis 55 KI-VO GPAI-Modelle. Prüfraster: technische Dokumentation Anhang XI Urheberrechts-Compliance-Strategie Art. 53 Abs. 1 lit. c Zusammenfassung Trainingsdaten Art. 53 Abs. 1 lit. d. Output: GPAI-Pflichtencheckliste nach Risikostufe. Abgrenzung zu gpai-vorliegen-art-3-nr-63 (Vorliegen eines GPAI-Modells) und gpai-systemisches-risiko-schwelle-10e25-flop (erhoehte Pflichten bei systemischem Risiko). |

## Arbeitsweg

Im Plugin KI-VO / AI Act-Prüfer gilt für **Gerichtliche KI Governance Aufsichtsbehoerden**: zuerst das tragende Prüffeld auswählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Ergänzende Prüffelder nur heranziehen, wenn dieselbe Akte sie trägt. Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschten Output sauber getrennt halten. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `gerichtliche-ki-assistenz-hochrisiko-justiz`

**Fokus:** Justizielle KI als Hochrisiko-Kontext: Systeme zur Unterstuetzung richterlicher oder behördlicher Rechtsanwendung, Sachverhaltswuerdigung, Aktenpriorisierung und Entscheidungsvorbereitung nach Art. 6 Abs. 2 i.V.m. Anhang III KI-VO.

# Gerichtliche KI-Assistenz und Anhang III

## Kernfrage

Wird KI nur als allgemeines Schreibwerkzeug genutzt oder beeinflusst sie die Auslegung von Tatsachen, Rechtsfragen oder die Anwendung des Rechts auf einen konkreten Sachverhalt?

## Entscheidungsbaum

1. **Allgemeines Tool:** Textformatierung, Übersetzung, Terminorganisation → meistens kein Justiz-Hochrisiko allein.
2. **Aktenanalyse:** Sachverhaltsextraktion, Priorisierung, Streitwert-/Fristenhinweise → genaue Zweck- und Wirkungskontrolle.
3. **Rechtsanwendung:** Vorschlag zu Anspruch, Schuld, Haftung, Sanktion, Beweiswürdigung → Anhang-III-Nähe sehr stark.
4. **Entscheidungsvorbereitung:** Score, Empfehlung, Tenorvorschlag → Hochrisiko intensiv prüfen.

## Mindestanforderungen

- menschliche Verantwortung sichtbar;
- Protokollierung der KI-Nutzung;
- keine verdeckte Entscheidungsautomation;
- Nachvollziehbarkeit der Datenbasis;
- Möglichkeit, Fehler zu erkennen und zu korrigieren;
- klare Trennung zwischen Entwurfshilfe und Entscheidung.

## Output

Erstelle:

- Hochrisiko-Vermerk.
- Governance-Check fuer Gericht/Behörde.
- Transparenz- und Akteneinsichtsfragen.
- Beweisverwertungs- und Gehörsrisiken.

## Warnung

Gerade bei Justiz-KI reicht "human in the loop" nicht als Zauberwort. Entscheidend ist, ob der Mensch fachlich und organisatorisch wirklich gegensteuern kann.

## 2. `governance-aufsichtsbehoerden-art-70`

**Fokus:** Unternehmen oder Behoerde fragt: An wen muss ich mich in Deutschland und Europa wenden wenn ich Fragen zur KI-VO-Aufsicht habe oder eine Meldepflicht erfullen muss? Art. 70 ff. KI-VO Governance. Prüfraster: nationale Aufsichtsbehoerden Art. 70 Europaeisches KI-Buero Art. 64 KI-Ausschuss Art. 65 wissenschaftliches Gremium Art. 68 Beratungsforum Art. 67 Aufgaben Befugnisse Koordination. Output: Übersicht zuständige Stellen in Deutschland und EU mit Kontakthinweisen. Abgrenzung zu marktueberwachung-meldung-vorfaelle-art-72-bis-79 (Meldepflichten) und sanktionen-art-99-bis-101 (Bußgeldrahmen).

# Governance und Aufsichtsbehörden — Art. 70 ff. KI-VO

## Zweck

Die KI-VO richtet eine mehrstufige Governance-Struktur ein: nationale Behörden, das Europäische KI-Büro und übergeordnete Gremien. Dieser Skill klärt, wer für was zuständig ist und wo in Deutschland der Ansprechpartner liegt.

## Nationale Ebene — Nationale Aufsichtsbehörden (Art. 70 KI-VO)

Jeder Mitgliedstaat benennt eine oder mehrere nationale zuständige Behörden, die für die Anwendung und Durchsetzung der KI-VO zuständig sind. Diese Behörden üben auch die Funktion der Marktüberwachungsbehörde aus.

**Aufgaben der nationalen Aufsichtsbehörden:**
- Marktüberwachung (Kontrolle von Hochrisiko-KI-Systemen auf dem Markt)
- Überprüfung von Konformitätsbewertungen
- Entgegennahme von Meldungen zu schwerwiegenden Vorfällen
- Befugnis, Informationen anzufordern und Prüfungen durchzuführen
- Befugnis, den Rückzug von Produkten vom Markt zu fordern

**Deutschland:** Die nationale Governance-Struktur für die KI-VO wird in Deutschland noch konkretisiert. Die Bundesnetzagentur und das Bundesamt für Sicherheit in der Informationstechnik (BSI) sind als potenzielle Anlaufstellen diskutiert worden. Für Datenschutzaspekte bleiben die Datenschutzaufsichtsbehörden (Landes- und Bundesdatenschutzbeauftragte) zuständig.

## EU-Ebene — Europäisches KI-Büro (Art. 64 KI-VO)

Das Europäische KI-Büro wurde innerhalb der Kommission eingerichtet (nicht als separate Agentur). Es ist zuständig für:
- Aufsicht über GPAI-Modelle (einschließlich solcher mit systemischem Risiko)
- Koordination der nationalen Aufsichtsbehörden
- Entwicklung und Überwachung von Verhaltenskodizes
- Durchführung von Untersuchungen bei GPAI-Modell-Anbietern
- Erlass von Beschlüssen bei Verstößen durch GPAI-Anbieter

**Besondere Befugnis:** Für GPAI-Modelle mit systemischem Risiko ist das Europäische KI-Büro die primäre Aufsichtsbehörde — nationale Behörden haben insoweit eine sekundäre Rolle.

## EU-Ebene — KI-Ausschuss (Art. 65 KI-VO)

Der KI-Ausschuss setzt sich aus Vertretern der nationalen Aufsichtsbehörden zusammen. Er hat beratende Funktion:
- Unterstützung der kohärenten Anwendung der KI-VO in der EU
- Empfehlungen und Stellungnahmen
- Koordination bei grenzüberschreitenden Fällen

## EU-Ebene — Wissenschaftliches Gremium (Art. 68 KI-VO)

Das wissenschaftliche Gremium besteht aus unabhängigen Sachverständigen. Es unterstützt das Europäische KI-Büro bei der Bewertung systemischer Risiken von GPAI-Modellen und berät bei technischen Fragen.

## EU-Ebene — Beratungsforum (Art. 67 KI-VO)

Das Beratungsforum setzt sich aus Vertretern der Industrie, Zivilgesellschaft, Akademie und anderen Interessengruppen zusammen. Es berät den KI-Ausschuss und die Kommission.

## Praktische Bedeutung für Unternehmen

**Wer ist Ansprechpartner bei Anfragen?**
- Bei Marktüberwachungsfragen → nationale Aufsichtsbehörde des Mitgliedstaats, in dem Sie tätig sind
- Bei GPAI-Modell-Fragen → Europäisches KI-Büro
- Bei Datenschutzfragen im KI-Kontext → nationale Datenschutzaufsichtsbehörde

**Was tun bei behördlichen Anfragen?**
- Unverzüglich kooperieren (Art. 78 KI-VO: Vertraulichkeit der Informationen beachten)
- Anwalt hinzuziehen bei Verdacht auf Bußgeldverfahren (`mandatsabbruch-empfehlung-komplexe-faelle`)
- Unterlagen bereitlegen: technische Dokumentation, Konformitätserklärung, Protokolle

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
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Governance und Aufsichtsbehoerden-Anforderungen Art. 70 KI-VO pruefen | Pruefergebnis nach Schema; Template unten |
| Variante A — Behörde hat bereits Anfrage gestellt | Antwort-Vorlage statt Pruefprotokoll; Fristen beachten |
| Variante B — System kein Hochrisiko keine Art. 70 Pflicht | Kurzdokumentation der Nicht-Anwendbarkeit |
| Variante C — Mehrere Jurisdiktionen EU und national | Separate Pruefung pro Mitgliedstaat; Koordination erforderlich |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template — Pruefergebnis
**Adressat:** Pruefer / Rechtsberater — Tonfall: strukturiert-rechtlich
```
PRUEFERGEBNIS — GOVERNANCE AUFSICHTSBEHOERDEN ART 70
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 70 Rn. 5]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## 3. `gpai-code-of-practice-copyright-safety-evidence`

**Fokus:** GPAI Code of Practice und Evidence-Logik: Copyright-Policy, Safety/Security, systemisches Risiko, Modellinformationen fuer Downstream-Anbieter, Standards-Uebergang und Nachweismappe ohne falsche Zertifizierungsbehauptung.

# GPAI Code of Practice: Evidence statt Etikett

## Ziel

Der GPAI Code of Practice kann Compliance operationalisieren, ersetzt aber nicht die eigentliche Prüfung der KI-VO. Dieser Skill übersetzt Code-, Normen- und Leitlinienanforderungen in eine Nachweismappe.

## Prüffelder

- Modelltyp und Anbieterrolle.
- GPAI oder GPAI mit systemischem Risiko.
- Technische Dokumentation.
- Informationen für Downstream-Anbieter.
- Urheberrechtspolitik und Trainingsdatenzusammenfassung.
- Safety- und Security-Maßnahmen.
- Red-Team- und Incident-Prozesse.
- Versionierung und Modelländerungen.

## Output-Struktur

1. Compliance Claim: Was wird behauptet?
2. Evidence: Welcher Nachweis belegt es?
3. Owner: Wer hält den Nachweis aktuell?
4. Update Trigger: Wann muss neu geprüft werden?
5. Lücke: Was fehlt?

## Vorsicht

Nicht schreiben: "Code erfüllt, damit automatisch rechtssicher." Besser: "Code/Standard wird als Nachweisbaustein genutzt; finale KI-VO-Bewertung bleibt artikelspezifisch."

## 4. `gpai-modelle-art-51-bis-55`

**Fokus:** Entwickler oder Anbieter eines Sprachmodells oder Basismodells fragt: Fallen wir unter die GPAI-Pflichten der KI-VO und was muessen wir konkret tun? Art. 51 bis 55 KI-VO GPAI-Modelle. Prüfraster: technische Dokumentation Anhang XI Urheberrechts-Compliance-Strategie Art. 53 Abs. 1 lit. c Zusammenfassung Trainingsdaten Art. 53 Abs. 1 lit. d. Output: GPAI-Pflichtencheckliste nach Risikostufe. Abgrenzung zu gpai-vorliegen-art-3-nr-63 (Vorliegen eines GPAI-Modells) und gpai-systemisches-risiko-schwelle-10e25-flop (erhoehte Pflichten bei systemischem Risiko).

# GPAI-Modelle — Art. 51 bis 55 KI-VO

## Zweck

Art. 51 bis 55 KI-VO enthalten einen eigenen Pflichtenkatalog für Anbieter von GPAI-Modellen (General-Purpose-KI-Modelle). Diese Pflichten gelten unabhängig davon, ob das GPAI-Modell als Hochrisiko-KI eingesetzt wird. Sie sind seit dem 2. August 2025 anwendbar.

## Abgrenzung: GPAI-Modell versus GPAI-System

**GPAI-Modell (Art. 3 Nr. 63 KI-VO):** Ein KI-Modell, das mit großer Datenmenge mit selbstüberwachtem Lernen in großem Maßstab trainiert wird und eine Reihe von allgemeinen Aufgaben erfüllen kann, auch wenn es für einen bestimmten spezifischeren Zweck eingesetzt wird.

**GPAI-System (Art. 3 Nr. 66 KI-VO):** Ein KI-System, das auf einem GPAI-Modell basiert und für eine Vielzahl von Zwecken eingesetzt werden kann.

**Praxisrelevanz:** Das GPAI-Modell ist die Grundlage (z.B. ein Foundation-Modell); das GPAI-System ist die Anwendung darauf (z.B. ein Chatbot oder eine spezifische Anwendung). Pflichten treffen primär den Modellanbieter.

→ Detailprüfung: `gpai-vorliegen-art-3-nr-63`

## Pflicht 1 — Technische Dokumentation (Art. 53 Abs. 1 lit. a KI-VO i.V.m. Anhang XI KI-VO)

Anbieter von GPAI-Modellen müssen eine technische Dokumentation erstellen und aktuell halten. Der Inhalt richtet sich nach Anhang XI KI-VO und umfasst:

- Allgemeine Beschreibung des GPAI-Modells einschließlich seines Bestimmungszwecks
- Beschreibung der Modellarchitektur und der Anzahl der Parameter
- Informationen über Trainingsverfahren und -daten (auf hoher Abstraktionsebene)
- Beschreibung des Leistungsniveaus anhand geeigneter Metriken
- Bekannte Grenzen und Schwächen

**Prüffragen:**
- Liegt eine vollständige technische Dokumentation nach Anhang XI vor?
- Wurde die Dokumentation bei wesentlichen Modellanpassungen aktualisiert?

## Pflicht 2 — Informationen und Dokumentation für nachgelagerte Anbieter (Art. 53 Abs. 1 lit. b KI-VO)

Anbieter von GPAI-Modellen müssen nachgelagerten Anbietern, die das Modell in ihre KI-Systeme integrieren, ausreichende Informationen und Dokumentation bereitstellen, damit diese ihre eigenen Pflichten nach der KI-VO erfüllen können.

**Prüffragen:**
- Stellen Sie Ihren Nutzern (Entwicklern, Integrierern) ausreichende technische Informationen bereit?
- Enthält Ihre Dokumentation Hinweise auf bekannte Risiken und Einschränkungen, die für Hochrisiko-Einsätze relevant sein könnten?

## Pflicht 3 — Urheberrechts-Compliance-Strategie (Art. 53 Abs. 1 lit. c KI-VO)

Anbieter von GPAI-Modellen müssen eine Strategie zur Einhaltung des Urheberrechts der Union implementieren. Diese Pflicht ist eng mit Art. 4 Abs. 3 der Richtlinie (EU) 2019/790 (DSM-Richtlinie) verknüpft.

**Inhalt der Strategie:**
- Maßnahmen zur Erkennung und Respektierung von Text-und-Data-Mining-Vorbehalten (TDM-Vorbehalte nach Art. 4 Abs. 3 DSM-Richtlinie)
- Verfahren zur Überprüfung von Trainingsdaten auf urheberrechtlich geschützte Inhalte
- Dokumentation, welche Quellen für das Training verwendet wurden

**Prüffragen:**
- Wurde bei der Datenerhebung für das Training geprüft, ob Webseiten oder Quellen einen TDM-Vorbehalt haben (z.B. robots.txt, Nutzungsbedingungen)?
- Wie wird mit urheberrechtlich geschützten Trainingsdaten umgegangen?

## Pflicht 4 — Summary of Training Content (Art. 53 Abs. 1 lit. d KI-VO)

Anbieter von GPAI-Modellen müssen eine ausreichend detaillierte Zusammenfassung der für das Training verwendeten Inhalte veröffentlichen, gemäß einem Format, das das Europäische KI-Büro bereitstellt.

**Inhalt:**
- Wesentliche Datenquellen
- Verarbeitungsschritte
- Umfang der Trainingsdaten (Größenordnung)

**Prüffragen:**
- Liegt eine solche Zusammenfassung vor und ist sie veröffentlicht?

## Open-Source-Erleichterungen (Art. 53 Abs. 2 KI-VO)

Für GPAI-Modelle mit offenen Gewichten (Open-Source-Modelle) gelten reduzierte Dokumentationspflichten — sofern das Modell kein systemisches Risiko darstellt (unter 10^25 FLOP) und unter freier und offener Lizenz veroeffentlicht wird (Parameter, Architektur, Nutzung).

## Faktische Updates (Stand 05/2026)

- **02.08.2025 — Anwendung Kapitel V KI-VO:** Die Pflichten fuer GPAI-Modellanbieter (Art. 51-55) sind seit dem 02.08.2025 verbindlich. Quelle: VO (EU) 2024/1689, Art. 113 lit. b — eur-lex.europa.eu/eli/reg/2024/1689/oj.
- **Trainingsdaten-Zusammenfassung (Art. 53 Abs. 1 lit. d):** Die Veroeffentlichung erfolgt nach dem von der Kommission/EU-AI-Office bereitgestellten Template. Stand der Template-Bereitstellung und ggf. Updates live pruefen ueber digital-strategy.ec.europa.eu.
- **GPAI Code of Practice (Art. 56 KI-VO):** Der General-Purpose-AI-Code-of-Practice strukturiert sich in den Saeulen Transparenz, Urheberrecht und Safety/Security. Anbieter, die den Code zeichnen, geniessen Vermutung der Pflichtenkonformitaet. Quelle: digital-strategy.ec.europa.eu (live pruefen).
- **Systemisches Risiko Art. 51 KI-VO:** Bei Trainings-Compute >= 10^25 FLOPs gilt die Vermutung des systemischen Risikos; zusaetzliche Pflichten nach Art. 55 (Modellbewertungen, adversarial testing, Meldepflicht bei schweren Vorfaellen, Cybersicherheit).
- **EU AI Office:** Zustaendig fuer GPAI-Durchsetzung, Modellbewertung und Code-of-Practice (Art. 64 KI-VO).

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
PRUEFERGEBNIS — GPAI MODELLE ART 51 BIS 55
[DATUM] — System: [SYSTEMNAME] — Mandant: [NAME MANDANT]
[AKTENZEICHEN]

Gepruefte Norm(en): [Art. 51 Rn. 4]

Ergebnis:
[ ] Anforderung erfuellt
[ ] Anforderung nicht erfuellt — Massnahmen erforderlich:
 1. [MASSNAHME — Verantwortlicher: NAME — Frist: DATUM]
[ ] Nicht einschlaegig — Begruendung: [BEGRUENDUNG]

Sanktionsrisiko: [NIEDRIG / MITTEL / HOCH — bis [BETRAG] nach Art. 99 KI-VO]
Naechster Skill: [FOLGE-SKILL]
Geprueft: [NAME], [DATUM]
```
