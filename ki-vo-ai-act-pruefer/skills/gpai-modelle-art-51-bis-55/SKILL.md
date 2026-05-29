---
name: gpai-modelle-art-51-bis-55
description: "Entwickler oder Anbieter eines Sprachmodells oder Basismodells fragt: Fallen wir unter die GPAI-Pflichten der KI-VO und was muessen wir konkret tun? Art. 51 bis 55 KI-VO GPAI-Modelle. Prüfraster: technische Dokumentation Anhang XI Urheberrechts-Compliance-Strategie Art. 53 Abs. 1 lit. c Zusammenfassung Trainingsdaten Art. 53 Abs. 1 lit. d. Output: GPAI-Pflichtencheckliste nach Risikostufe. Abgrenzung zu gpai-vorliegen-art-3-nr-63 (Vorliegen eines GPAI-Modells) und gpai-systemisches-risiko-schwelle-10e25-flop (erhoehte Pflichten bei systemischem Risiko)."
---

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
