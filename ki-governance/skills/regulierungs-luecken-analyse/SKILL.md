---
name: regulierungs-luecken-analyse
description: "Gleicht eine neue KI-Regulierung oder Behördenleitlinie mit der aktuellen Governance-Position ab — identifiziert Lücken, Prioritäten und einen Maßnahmenplan mit Verantwortlichen und Fristen. Lädt, wenn der Nutzer Lückenanalyse AI Act, gilt der AI Act für uns, Compliance-Prüfung KI, neue KI-Verordnung prüfen oder Regelungstext eingibt im Ki Governance."
---

# KI-Regulierungs-Lückenanalyse

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: KI-VO Geltungsbeginn gestaffelt (02.02.2025 Verbote, 02.08.2025 GPAI, 02.08.2026 Hochrisiko Anhang III), schwerwiegender Vorfall 15 Tage, DSGVO DPIA vorab.
- Tragende Normen verifizieren: EU KI-VO 2024/1689 Art. 9, 10, 14, 22, 27, 50, ISO/IEC 42001, NIST AI RMF 1.0, OECD AI Principles, DSGVO Art. 22, 35, Produkthaftungs-RL 2024/2853 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geschäftsleitung, KI-Officer, Datenschutzbeauftragter, Compliance, Aufsichtsrat, Marktüberwachung, externer Auditor, betroffene Personen.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: KI-Inventar, Risikoanalyse, FRIA (Fundamental Rights Impact Assessment), AI Governance Policy, Modellkarten, Audit-Bericht, DSGVO-DPIA, Schulungsnachweis — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Eingaben

- Regulierungs-Name oder Regelungstext (AI Act Hochrisiko, DSGVO Art. 22,
 DSA, DMA, RL 2024/2853, BSIG, Sektoren)
- Praxisprofil aus `CLAUDE.md` (regulatorischer Fußabdruck, Anwendungsfall-
 Register, KI-Richtlinien-Verpflichtungen, Anbieter-Positionen,
 Folgenabschätzungspraxis)

## Rechtlicher Rahmen

**Kernvorschriften (Referenzrahmen)**

- **AI Act (VO (EU) 2024/1689)**: Gestaffelte Anwendbarkeit: Art. 5 (verbotene
 Praktiken) ab 02.02.2025; Art. 53 ff. (Allgemeinzweck-KI) ab 02.08.2025;
 Hochrisiko-Pflichten Art. 9–15 (Anbieter), Art. 26/29 (Betreiber) ab
 02.08.2026. Hochrisiko: Art. 6 i.V.m. Anhang III. Bußgeld: Art. 99 bis
 35 Mio. € oder 7 % weltweiter Jahresumsatz bei Art. 5-Verstößen.
- **DSGVO Art. 22**: Automatisierte Einzelentscheidungen; Rechtsgrundlagen
 Art. 22 Abs. 2 lit. a–c.
- **DSA Art. 27, 38 (VO (EU) 2022/2065)**: Transparenz für Empfehlungs-
 systeme sehr großer Plattformen.
- **DMA Art. 6 (VO (EU) 2022/1925)**: KI-bezogene Pflichten für Torwächter.
- **Produkthaftungs-RL 2024/2853/EU** (ersetzt RL 85/374/EWG): KI-Systeme
 als Produkte; Beweislasterleichterungen.
- **GeschGehG, UrhG § 44b**: Trainingsdaten-Schutz; Text-und-Data-Mining.

**Leitentscheidungen**

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Kommentare**

- Wendehorst/Grinzinger, in: Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 6 Rn. 5 (Hochrisiko-Klassifikation; Anhang-III-Kategorien).
- Hoffmann-Riem (Hrsg.), Big Data, KI und das Recht, 2021, S. 115 ff.
 (regulatorische Lücken im KI-Recht).
- Spindler/Schuster, Recht der elektronischen Medien, 4. Aufl. 2024,
 Teil IV Rn. 110 (Compliance-Anforderungen AI Act).
- Ehmann/Selmayr, DS-GVO, 3. Aufl. 2024, Art. 22 Rn. 20

*Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im Einzelfall.*

## Ablauf

**Schritt 1 — Regulierung abgrenzen**

Bevor Lücken analysiert werden: Anwendbar? Jurisdiktion, Schwellenwert,
Sektor-Ausnahmen, Anbieter-/Betreiber-Unterscheidung (Art. 3 KI-VO).
Wann? Inkrafttreten; Durchsetzungsdatum; Phase-in-Fristen.
Was ist tatsächlich neu? Delta zum Status quo ermitteln, nicht Volltext
wiedergeben.
→ Bei eindeutiger Nichtanwendbarkeit: "Nicht anwendbar. Begründung: [Grund].
Kein Handlungsbedarf."

**Schritt 2 — Anforderungen extrahieren**

Jede substanzielle Anforderung auflisten:

| Nr. | Anforderung | Fundstelle | Kategorie |
|---|---|---|---|

Kategorien: Transparenz / Folgenabschätzung / Menschliche Aufsicht /
Genauigkeit+Prüfung / Governance / Vertrags-Weitergabepflichten /
Verbotene Praktiken / Betroffenenrechte.

**Schritt 3 — Abgleich mit dem Ist-Zustand**

Für jede Anforderung (Kurzformat):

```
### [Nr.]: [Kurzbezeichnung]
Verordnung verlangt: [Anforderung]
Unser Ist-Zustand: [aus CLAUDE.md]
Lücke: [Keine | Teilweise | Vollständig]
Was fehlt: [konkret]
Aufwand: [Richtlinienänderung | Prozess | System | Folgenabschätzung |
 Anbieter-Nachverhandlung | Registrierung]
Risiko: [Bußgeldrahmen; Durchsetzungswahrscheinlichkeit]
```

**Schritt 4 — Priorisieren**

1. Harte Frist + Sanktionen (Art. 99 KI-VO; Art. 83 DSGVO)
2. Verbotene Praktiken (Art. 5 KI-VO): erste Priorität unabhängig
 vom Durchsetzungsdatum
3. Aufwand-Wirkung-Verhältnis
4. Anwendungsfall-Überschneidung

**Schritt 5 — Maßnahmenplan**

```markdown

## Maßnahmenplan: [Regulierungsname]
Anwendungsdatum: [Datum] | Betrifft uns als: [Anbieter/Betreiber/beides]

### Muss-Maßnahmen vor Durchsetzungsbeginn
| Lücke | Maßnahme | Verantwortlich | Frist | Status |

### Soll-Maßnahmen
[gleiche Tabelle]

### Bereits compliant [Liste]
### Akzeptierte Lücken [mit Begründung und Akzeptant]
```

## Beispiel

**Anfrage:** "Gilt der AI Act für unsere interne Bewerbungs-Screening-KI?"

**Ablauf:** Betreiberrolle; Hochrisiko nach Art. 6 Abs. 2 i. V. m. Anhang III Nr. 4 lit. a KI-VO, wenn das System zweckbestimmt für Auswahl, Filterung oder Bewertung von Bewerbungen eingesetzt wird. Betreiber-Pflichten aus Art. 26 KI-VO und ggf. Grundrechte-Folgenabschätzung nach Art. 27 KI-VO; bei eigener Anbieterrolle zusätzlich Anbieterpflichten, insbesondere Risikomanagement nach Art. 9 KI-VO. Maßnahme: Rollen sauber trennen, Human-in-the-Loop dokumentieren, Betriebsrat einbeziehen und Umsetzungsfrist im Maßnahmenplan führen.

## Risiken und typische Fehler

- Mehrdeutigkeit übergehen: bei echten Auslegungsfragen konservative Lesart
 nennen, nicht überdecken.
- Maßnahmen nicht implementieren: dieser Skill plant nur.
- Sektorspezifische Expertise nicht ersetzen (Medizinprodukte MDR/IVDR,
 Finanzdienstleistungen MaRisk-KI).

## Quellenpflicht

- **AI Act Art. 5, Art. 6 i.V.m. Anhang III, Art. 9–15, Art. 26/29, Art. 99.**
- **DSGVO Art. 22** bei automatisierten Entscheidungsverfahren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **RL 2024/2853/EU** (Produkthaftung) bei Haftungslücken.
- **DSGVO Art. 35** bei Folgenabschätzungspflicht.
- **Wendehorst/Grinzinger, in: Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 6 Rn. 5.**
- **Hoffmann-Riem (Hrsg.), Big Data, KI und das Recht, 2021, S. 115.**

## Triage zu Beginn
1. Welches Regulierungsregime ist Gegenstand — KI-VO, DSGVO Art. 22, DSA, DMA, ProdHaft-RL?
2. Ist das Regime bereits in Kraft oder nur angekuendigt — welches Anwendungsdatum?
3. Betrifft das Regime die Rolle als Anbieter oder Betreiber (Art. 3 KI-VO-Unterscheidung)?
4. Welche Anwendungsfaelle aus dem Register sind potenziell lueckenhaft?
5. Gibt es bereits Massnahmen oder laufende Compliance-Projekte — Delta zum Status quo ermitteln?

## Output-Template — Lueckenanalyse KI-Regulierung
**Adressat:** Compliance- / Rechts-Team — Tonfall: sachlich, priorisiert
```
LUECKENANALYSE KI-REGULIERUNG
[DATUM] — Regime: [REGULIERUNGSNAME] — Anwendungsbereich: [JA/NEIN/TEILWEISE]

ANWENDBARES REGIME: [BEGRUENDUNG IN 1-2 SAETZEN]
Inkrafttreten: [DATUM] — Durchsetzung ab: [DATUM]

LUECKENTABELLE:
| Nr. | Anforderung | Fundstelle | Status | Luecke | Prioritaet | Verantwortlicher | Frist |
|---|---|---|---|---|---|---|---|
| 1 | [ANFORDERUNG] | Art. X KI-VO | [BESTEHT/FEHLT/LUECKE] | [BESCHREIBUNG] | HOCH/MITTEL/NIEDRIG | [PERSON] | [DATUM] |

GESAMTBEWERTUNG: [N] kritische Luecken / [N] material / [N] gering

NICHT-ANWENDBAR-POSTEN:
- [ANFORDERUNG]: nicht anwendbar wegen [BEGRUENDUNG]

NAECHSTE SCHRITTE:
1. [MASSNAHME — Verantwortlicher: NAME — bis: DATUM]

Erstellt: [NAME], [DATUM]
```

