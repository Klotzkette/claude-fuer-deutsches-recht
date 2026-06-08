---
name: anwendungsfall-triage
description: "Klassifiziert einen vorgeschlagenen KI-Anwendungsfall gegen das Unternehmensregister — freigegeben, bedingt oder nicht freigegeben — und erstellt Auflagenliste und nächste Schritte. Prüft gegen verbotene Praktiken (Art. 5 KI-VO) und Hochrisiko-Kategorien (Anhang III KI-VO). Lädt, wenn der Nutzer KI-Anwendungsfall triage, dürfen wir KI für X einsetzen, ist das freigegeben oder Hochrisiko-KI klassifizieren sagt im Ki Governance."
---

# KI-Anwendungsfall-Triage

## Aktenstart statt Formularstart

Wenn zu **Anwendungsfall Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Ki Governance** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Geltungsbeginn gestaffelt (02.02.2025 Verbote, 02.08.2025 GPAI, 02.08.2026 Hochrisiko Anhang III), schwerwiegender Vorfall 15 Tage, DSGVO DPIA vorab.
- Tragende Normen verifizieren: EU KI-VO 2024/1689 Art. 9, 10, 14, 22, 27, 50, ISO/IEC 42001, NIST AI RMF 1.0, OECD AI Principles, DSGVO Art. 22, 35, Produkthaftungs-RL 2024/2853 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsleitung, KI-Officer, Datenschutzbeauftragter, Compliance, Aufsichtsrat, Marktüberwachung, externer Auditor, betroffene Personen.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: KI-Inventar, Risikoanalyse, FRIA (Fundamental Rights Impact Assessment), AI Governance Policy, Modellkarten, Audit-Bericht, DSGVO-DPIA, Schulungsnachweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Beschreibung des KI-Anwendungsfalls: was tut die KI, wer ist betroffen,
 gibt es menschliche Überprüfung, welcher Anbieter?
- Praxisprofil aus `CLAUDE.md` (Anwendungsfall-Register, Rote Linien,
 Governance-Stufen, regulatorischer Fußabdruck)

## Rechtlicher Rahmen

**Kernvorschriften**

- **AI Act Art. 5 KI-VO (verbotene Praktiken)**: Social Scoring durch
 öffentliche oder private Stellen (Art. 5 Abs. 1 lit. c); subliminale
 Manipulation (Art. 5 Abs. 1 lit. a/b); Ausnutzung von Vulnerabilität
 (Art. 5 Abs. 1 lit. b); biometrische Kategorisierung nach geschützten
 Merkmalen (Art. 5 Abs. 1 lit. g); Echtzeitfernidentifizierung in
 öffentlichen Räumen (Art. 5 Abs. 1 lit. h); Emotionserkennung am
 Arbeitsplatz/Bildung (Art. 5 Abs. 1 lit. f). Ab 02.02.2025 anwendbar.
- **AI Act Art. 6 i.V.m. Anhang III KI-VO**: Hochrisiko-Kategorien —
 Nr. 1 Biometrie; Nr. 2 Beschäftigung (Bewerbungs-Screening, Leistungs-
 bewertung); Nr. 3 Wesentliche Dienstleistungen (Kredit, Versicherung);
 Nr. 4 Bildung; Nr. 5 Kritische Infrastruktur; Nr. 6 Strafverfolgung;
 Nr. 7 Migration; Nr. 8 Rechtspflege. Hochrisiko: Art. 9–15 (Anbieter),
 Art. 26/29 (Betreiber).
- **DSGVO Art. 22**: Vollautomatisierte Einzelentscheidungen mit Rechtswirkung
 oder erheblicher Beeinträchtigung nur nach Art. 22 Abs. 2 lit. a–c
 (Vertrag, gesetzliche Pflicht, ausdrückliche Einwilligung). Widerspruchs-
 und Transparenzpflichten.
- **§ 87 Abs. 1 Nr. 6 BetrVG**: Mitbestimmungsrecht des Betriebsrats bei
 KI-Tools zur Mitarbeiterüberwachung/-bewertung.

**Leitentscheidungen**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kommentare**

- Wendehorst/Grinzinger, in: Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 5 Rn. 8 (verbotene Praktiken) und Art. 6 i.V.m. Anhang III Rn. 15 (Hochrisiko-Klassifikation).
- Ehmann/Selmayr, in: Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 10.
- Müller-Glöge, in: Erfurter Kommentar, 25. Aufl. 2025, § 87 BetrVG Rn. 32.
- Spindler/Schuster, Recht der elektronischen Medien, 4. Aufl. 2024,
 Teil IV Rn. 88.

*Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im Einzelfall.*

## Ablauf

**Schritt 1 — Anwendungsfall verstehen**

Bei vager Beschreibung fragen: Was tut die KI genau? Auf wen/was wirkt sie?
Prüft ein Mensch vor Wirkung? Welcher Anbieter? Nur intern oder Kunden/Dritte?

**Schritt 2 — Art. 5-Prüfung (ERSTE PRIORITÄT)**

Vor dem Register prüfen: Liegt ein absolutes Verbot vor?
- Social Scoring, subliminale Manipulation, Vulnerabilitäts-Ausnutzung
- Biometrische Kategorisierung nach geschützten Merkmalen
- Echtzeitbiometrie in öffentlichen Räumen
- Emotionserkennung am Arbeitsplatz/Bildung

Bei Treffer: sofort melden, ohne Abmilderung:
> "Dieser Anwendungsfall berührt [Art. 5 KI-VO]. Verbotene Praktiken sind
> absolute Verbote. Wenn etwas anders ist: anwaltliche Entscheidung nötig,
> keine Triage-Freigabe."

**Schritt 3 — Register-Abgleich**

Direkttreffer → anwenden. Nahes Match → kennzeichnen. Kein Treffer →
BEDINGT (Folgenabschätzung ausstehend); vorläufige Risikoeinschätzung
einschließlich Anhang-III-Prüfung ausgeben.

**Schritt 4 — Jurisdiktionaler Anwendungsbereich und Anhang-III-Prüfung**

Alle Regime aus `## Regulatorischer Fußabdruck` prüfen. Striktest
anwendbare Behandlung bei Mehrfach-Jurisdiktion. Anhang-III-Kategorien
(Nr. 1–8) explizit gegen den Anwendungsfall prüfen; bei Hochrisiko:
Betreiberpflichten Art. 26/29 KI-VO vermerken.

**Schritt 5 — DSGVO Art. 22-Prüfung**

Vollautomatisiert + Rechtswirkung/erhebliche Beeinträchtigung? → Art. 22
Abs. 1 greift; Rechtsgrundlage nach Abs. 2 dokumentieren und Human-in-the-
Loop oder Einwilligung sicherstellen.

**Schritt 6 — Klassifikation und Ausgabe**

Bei Nicht-Jurist-Rolle: vor FREIGEGEBEN-Klassifikation anwaltliche Prüfung
abfragen; 1-seitigen Kurzüberblick für das Anwaltsgespräch generieren.

---

**ANWENDUNGSFALL:** [Anwendungsfall wie verstanden]
**KLASSIFIKATION:** [FREIGEGEBEN / BEDINGT / NICHT FREIGEGEBEN]
**Art. 5 KI-VO:** [Kein Verbot / [Verbotene Praxis] — ABSOLUTES VERBOT]
**Anhang III KI-VO:** [Nicht einschlägig / Hochrisiko Kategorie [Nr.]]
**DSGVO Art. 22:** [Nicht einschlägig / Einschlägig — Rechtsgrundlage: [Abs. 2]]
**Begründung:** [1–3 Sätze]
**Ausgelöste Rote Linien:** [Keine / Liste]

*Bei BEDINGT:*

| Anforderung | Verantwortlich | Erledigt? |
|---|---|---|
| KI-Folgenabschätzung (ggf. DSFA Art. 35 DSGVO) | [KI-Beauftragter] | ☐ |
| DSGVO Art. 22 Rechtsgrundlage dokumentieren | [DSB] | ☐ |
| Human-in-the-Loop — keine vollautomatisierten Entscheidungen | [Produkt] | ☐ |
| Offenlegung ggü. Betroffenen (Art. 13/14 DSGVO) | [Produkt/Recht] | ☐ |
| Betriebsrats-Beteiligung (§ 87 Abs. 1 Nr. 6 BetrVG) | [HR/Recht] | ☐ |

**Governance-Stufe:** [Standard / Erhöht / Hoch]

## Beispiel

**Anfrage:** "HR will KI zur automatischen Bewerbungs-Vorselektion einsetzen."
**Triage:** Art. 5: kein Verbot. Art. 6 Abs. 2 i. V. m. Anhang III Nr. 4 lit. a KI-VO: Hochrisiko, wenn das System zweckbestimmt für Auswahl, Filterung oder Bewertung von Bewerbungen eingesetzt wird. DSGVO Art. 22 Abs. 1 bei Vollautomatisierung.
§ 87 Abs. 1 Nr. 6 BetrVG: Betriebsrats-Beteiligung prüfen.
**Klassifikation: BEDINGT.** Folgenabschätzung + DSFA; Human-in-the-Loop;
Betriebsrat einbeziehen; Offenlegung ggü. Bewerber:innen (Art. 13 DSGVO).

## Risiken und typische Fehler

- Art. 5 KI-VO ist Pflichtprüfung — immer zuerst, vor dem Register.
- "Nur intern" reduziert das Risiko nicht: Mitarbeiter-KI oft höheres
 Risiko als kundenseitige KI.
- "Wir testen nur" ist keine Ausnahme bei echten Personen-Daten.
- "Der Anbieter sagt, es ist sicher" ersetzt nicht die eigene Folgenabschätzung.

## Quellenpflicht

- **AI Act Art. 5** und **Art. 6 i.V.m. Anhang III** (mit konkreter Nr.) bei
 jeder Klassifikation.
- **DSGVO Art. 22** bei automatisierten Entscheidungen.
- **§ 87 Abs. 1 Nr. 6 BetrVG** bei Mitarbeiter-Überwachungs-/Bewertungstools.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Wendehorst/Grinzinger, in: Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 5 Rn. 8 und Anhang III Rn. 15.**
- **Ehmann/Selmayr, in: Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 10.**
- **Müller-Glöge, in: Erfurter Kommentar, 25. Aufl. 2025, § 87 BetrVG Rn. 32.**

## Triage zu Beginn
1. Was tut die KI genau — assistierend, augmentierend oder vollautomatisiert?
2. Sind Betroffene schutzbeduertige Gruppen (Minderjaerige, Arbeitnehmer, Kreditnehmer)?
3. Liegt eine Hochrisiko-Kategorie nach Anhang III KI-VO vor (Nr. 1-8 pruefen)?
4. Ist eine vollautomatisierte Einzelentscheidung mit Rechtswirkung moeglich (Art. 22 DSGVO)?
5. Besteht ein § 87 Abs. 1 Nr. 6 BetrVG-Mitbestimmungsrecht (Mitarbeiterbewertung)?

## Output-Template — Triage-Ergebnis KI-Anwendungsfall
**Adressat:** Governance-Team / Fachabteilung — Tonfall: klar, strukturiert
```
TRIAGE-ERGEBNIS KI-ANWENDUNGSFALL
[DATUM] — [ANWENDUNGSFALL-ID]

ANWENDUNGSFALL: [BESCHREIBUNG]
KLASSIFIKATION: [FREIGEGEBEN / BEDINGT / NICHT FREIGEGEBEN]

Art. 5 KI-VO (verbotene Praktiken): [Kein Verbot / VERBOTEN: BEGRUENDUNG]
Anhang III KI-VO (Hochrisiko): [Nicht einschlaegig / Hochrisiko Kat. Nr. X]
DSGVO Art. 22: [Nicht einschlaegig / Einschlaegig — Rechtsgrundlage: Art. 22 Abs. 2 lit. X]
§ 87 Abs. 1 Nr. 6 BetrVG: [Nicht einschlaegig / Mitbestimmung erforderlich]

Begruendung: [1-3 Saetze]

Bei BEDINGT — Auflagen:
1. [AUFLAGE + VERANTWORTLICHER + FRIST]
2. [AUFLAGE + VERANTWORTLICHER + FRIST]

Governance-Stufe: [Standard / Erhoeht / Hoch]
Naechste Pruefung: [DATUM]

Erstellt: [NAME], [DATUM]
```

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 35 DSGVO
- § 203 StGB
- Art. 22 DSGVO
- Art. 28 DSGVO
- § 87 BetrVG
- § 26 BDSG
- § 44b UrhG
- Art. 36 DSGVO
- Art. 9 DSGVO
- Art. 79 DSGVO
- Art. 32 DSGVO
- § 29 VwVfG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

