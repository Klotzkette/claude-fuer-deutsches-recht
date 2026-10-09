---
name: regulierungs-luecken-analyse
description: "Für digitale Werkzeuge-Regulierungs-Lückenanalyse: ordnet Akte, Belege und Lücken; Ergebnis: Prüfprodukt mit Risiko und nächstem Schritt."
---

# KI-Regulierungs-Lückenanalyse

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: Verordnung (EU) 2024/1689 in der Fassung 2026/1744: Kapitel III Abschnitte 1 bis 3 außer Artikel 6 Absatz 5 für Anhang III ab 02.12.2027, für Anhang I ab 02.08.2028. Artikel 4 neuer Fassung, Artikel 4a, Verbote und Transparenz gesondert prüfen; Vorfallfrist nach Tatbestand und Ereignis, Datenschutz-Folgenabschätzung vor riskanter Verarbeitung.
- Tragende Rechtsgrundlagen am amtlichen EUR-Lex-Text der KI-Verordnung und der gegebenenfalls einschlägigen DSGVO prüfen. ISO/IEC 42001, NIST AI RMF und OECD-Prinzipien sind keine Verordnungsartikel. Bei harmonisierten Normen konkrete Fassung, Amtsblattfundstelle und abgedeckte Anforderungen nach Artikel 40 feststellen; freiwilliges Managementzertifikat und Konformitätsverfahren nach Artikel 43 trennen. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
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

- **KI-Verordnung:** Beide Einstufungspfade nach Artikel 6, Ausnahme nach Absatz 3, Artikel 111/113 und rollenbezogene Pflichten prüfen. Artikel 29 betrifft Konformitätsbewertungsstellen, nicht den allgemeinen Betreiber. Sanktionen nach dem konkreten Absatz des Artikels 99 einschließlich KMU-Sonderregeln begründen.
- **DSGVO Art. 22**: Automatisierte Einzelentscheidungen; Rechtsgrundlagen
 Art. 22 Abs. 2 lit. a–c.
- **DSA Art. 27, 38 (VO (EU) 2022/2065)**: Transparenz für Empfehlungs-
 systeme sehr großer Plattformen.
- **DMA Art. 6 (VO (EU) 2022/1925)**: KI-bezogene Pflichten für Torwächter.
- **Produkthaftungs-RL 2024/2853/EU** (ersetzt RL 85/374/EWG): KI-Systeme
 als Produkte; Beweislasterleichterungen.
- **GeschGehG, UrhG § 44b**: Trainingsdaten-Schutz; Text-und-Data-Mining.

**Leitentscheidungen**


**Kommentare**

- Fachliche Aussage unmittelbar aus dem einschlägigen Artikel der konsolidierten KI-Verordnung herleiten. Eine nicht im Original geprüfte Kommentar- oder Randnummernfundstelle wird nicht als Beleg ausgegeben. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
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

**Ablauf:** Für Bewerbungsauswahl den konkreten Tatbestand des Anhangs III Nummer 4 Buchstabe a und Artikel 6 Absatz 3 prüfen. Menschliche Schlussentscheidung allein schließt Hochrisiko nicht aus. Artikel 26 betrifft den Betreiber, Artikel 9 den Anbieter; eine eigene Anbieterrolle nach Artikel 25 gesondert begründen. Eine FRIA fällt nur bei den Adressaten des Artikels 27 an. Betriebsrat und Umsetzungsdatum als eigene Prüfspuren führen. Artikel 113 Buchstabe c erfasst Kapitel III Abschnitte 1 bis 3 außer Artikel 6 Absatz 5: bei Anhang III ab 02.12.2027, bei Anhang I ab 02.08.2028. Artikel 111 und die Zeitverschränkung mit anderen Abschnitten gesondert prüfen; keine pauschale Verschiebung sämtlicher Pflichten. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)

## Risiken und typische Fehler

- Mehrdeutigkeit übergehen: bei echten Auslegungsfragen konservative Lesart
 nennen, nicht überdecken.
- Maßnahmen nicht implementieren: dieser Skill plant nur.
- Sektorspezifische Expertise nicht ersetzen (Medizinprodukte MDR/IVDR,
 Finanzdienstleistungen MaRisk-KI).

## Quellenpflicht

- **KI-Verordnung:** Artikel 5, beide Pfade des Artikels 6, Anbieteranforderungen Artikel 9 bis 17, Betreiberpflichten Artikel 26 und Sanktionen Artikel 99 nach Tatbestand und Zeit. Artikel 29 ist keine allgemeine Betreiberpflicht. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
- **DSGVO Art. 22** bei automatisierten Entscheidungsverfahren.
- **RL 2024/2853/EU** (Produkthaftung) bei Haftungslücken.
- **DSGVO Art. 35** bei Folgenabschätzungspflicht.
- Fachliche Aussage unmittelbar aus dem einschlägigen Artikel der konsolidierten KI-Verordnung herleiten. Eine nicht im Original geprüfte Kommentar- oder Randnummernfundstelle wird nicht als Beleg ausgegeben. [amtlicher Text, Prüfstand 09.10.2026](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02024R1689-20260727)
- **Hoffmann-Riem (Hrsg.), Big Data, KI und das Recht, 2021, S. 115.**

## Triage zu Beginn
1. Welches Regulierungsregime ist Gegenstand — KI-VO, DSGVO Art. 22, DSA, DMA, ProdHaft-RL?
2. Ist das Regime bereits in Kraft oder nur angekuendigt — welches Anwendungsdatum?
3. Betrifft das Regime die Rolle als Anbieter oder Betreiber (Art. 3 KI-VO-Unterscheidung)?
4. Welche Anwendungsfaelle aus dem Register sind potenziell lueckenhaft?
5. Gibt es bereits Maßnahmen oder laufende Compliance-Projekte — Delta zum Status quo ermitteln?

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

> Quellenregel: Entscheidungen nur nach Prüfung einer amtlichen oder frei zugänglichen Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage ausgeben.
