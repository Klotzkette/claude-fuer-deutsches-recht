---
name: regulierungs-luecken-analyse
description: "Gleicht eine neue KI-Regulierung oder Behördenleitlinie mit der aktuellen Governance-Position ab — identifiziert Lücken, Prioritäten und einen Maßnahmenplan mit Verantwortlichen und Fristen. Lädt, wenn der Nutzer „Lückenanalyse AI Act\", „gilt der AI Act für uns\", „Compliance-Prüfung KI\", „neue KI-Verordnung prüfen\" oder Regelungstext eingibt."
---

# KI-Regulierungs-Lückenanalyse

## Zweck

Der AI Act ist seit 01.08.2024 in Kraft — mit gestaffelter Anwendbarkeit.
Die Datenschutzaufsichtsbehörden präzisieren DSGVO Art. 22. Die neue
Produkthaftungs-RL (RL 2024/2853) erfasst KI-Systeme. Etwas bewegt sich —
und nun muss bekannt sein, was sich, wenn überhaupt, ändern muss.

Dieser Skill gleicht neue Anforderungen mit der aktuellen KI-Governance
ab (gem. `CLAUDE.md`) und produziert eine priorisierte Lückenliste mit
Maßnahmenplan. Wo Regelungstext tatsächlich mehrdeutig ist: klar sagen,
konservative Lesart nennen, bei Materialität externe Beratung empfehlen.

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

- EuGH, Urt. v. 07.12.2023 – C-634/21, NJW 2024, 126 Rn. 49 (Schufa-Score): Maßstab für Lückenanalysen zu DSGVO Art. 22 bei Scoring-Systemen; automatisiertes Profiling als Art. 22 Abs. 1-Entscheidung bei maßgeblicher Grundlage für Drittentscheidung.
- EuGH, Urt. v. 04.10.2024 – C-203/22, NJW 2025, 56 Rn. 38 (Dun & Bradstreet): Verantwortlicher muss Algorithmus-Logik verständlich offenlegen; Maßstab für Transparenzlücken.
- BGH, Urt. v. 13.01.2015 – VI ZR 204/14, NJW 2015, 1236 Rn. 12: Produkthaftung für fehlerhafte Informationsprodukte; übertragbar auf KI-Haftung unter RL 2024/2853.
- BVerwG, Urt. v. 04.04.2019 – 2 C 4/18, NVwZ 2019, 1283 Rn. 22: Transparenz algorithmischer Verwaltungsentscheidungen; relevant bei Behörden-KI.

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
→ Bei eindeutiger Nichtanwendbarkeit: „Nicht anwendbar. Begründung: [Grund].
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

## Ausgabeformat

Datiertes Markdown-Dokument; Maßnahmenplan-Tabelle wird zum Tracker.
Auch bei „keine Lücken" dokumentieren — nützlicher Compliance-Nachweis.

**Quellen-Tagging:**
- `[gesichert]` — stabile Normen (z. B. DSGVO Art. 22, VO (EU) 2024/1689).
- `[prüfen]` — Durchführungsrechtsakte, Leitlinien, Schwellenwerte.
- `[prüfen-pinpoint]` — konkrete Artikelnummern, Anhang-Referenzen: IMMER
  gegen Primärquelle (ABl., beck-online, juris) verifizieren. AI Act
  Artikelnummern haben sich während der Konsolidierung verschoben.

## Beispiel

**Anfrage:** „Gilt der AI Act für unsere interne Bewerbungs-Screening-KI?"

**Ablauf:** Betreiberrolle; Hochrisiko Anhang III Nr. 2 lit. a KI-VO
(Einstellungsentscheidung) `[prüfen-pinpoint]`. Betreiber-Pflichten:
Art. 26, 29 KI-VO `[prüfen]`; kein dokumentiertes Risikomanagementsystem
→ Teilweise Lücke. Maßnahme: Folgenabschätzung nach Art. 9 KI-VO erstellen,
Human-in-the-Loop dokumentieren, bis 01.08.2026.

## Risiken und typische Fehler

- Mehrdeutigkeit übergehen: bei echten Auslegungsfragen konservative Lesart
  nennen, nicht überdecken.
- Maßnahmen nicht implementieren: dieser Skill plant nur.
- Sektorspezifische Expertise nicht ersetzen (Medizinprodukte MDR/IVDR,
  Finanzdienstleistungen MaRisk-KI).

## Quellenpflicht

- **AI Act Art. 5, Art. 6 i.V.m. Anhang III, Art. 9–15, Art. 26/29, Art. 99.**
- **DSGVO Art. 22** bei automatisierten Entscheidungsverfahren.
- **EuGH C-634/21 (Schufa-Score)** und **C-203/22 (Dun & Bradstreet)**.
- **RL 2024/2853/EU** (Produkthaftung) bei Haftungslücken.
- **DSGVO Art. 35** bei Folgenabschätzungspflicht.
- **Wendehorst/Grinzinger, in: Wendehorst/Grinzinger, AI Act, 1. Aufl. 2024, Art. 6 Rn. 5.**
- **Hoffmann-Riem (Hrsg.), Big Data, KI und das Recht, 2021, S. 115.**
